"""Structural checks of the local review preview; uses only Python's standard library."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import re

class Page(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.path, self.links, self.ids, self.canonicals = path, [], [], []
        self.h1 = self.publications = 0
    def handle_starttag(self, tag, attributes):
        a = dict(attributes)
        if tag == 'h1': self.h1 += 1
        if tag == 'article' and a.get('class') == 'publication': self.publications += 1
        if 'id' in a: self.ids.append(a['id'])
        if tag == 'img': assert a.get('alt'), f'Missing image alt in {self.path}'
        if tag == 'link' and a.get('rel') == 'canonical': self.canonicals.append(a['href'])
        if tag in ('a', 'link', 'script', 'img'):
            target = a.get('href') or a.get('src')
            if target: self.links.append(target)

root = Path('_site')
for route in ('', 'publications', 'cv', '404.html'):
    path = root / route if route.endswith('.html') else root / route / 'index.html'
    raw = path.read_text()
    page = Page(path)
    page.feed(raw)
    assert page.h1 == 1, f'Expected one H1: {path}'
    assert len(page.ids) == len(set(page.ids)), f'Duplicate IDs: {path}'
    assert len(page.canonicals) == 1
    assert page.canonicals[0] == 'https://chanchunkithkust.github.io/' + (route if route.endswith('.html') else route + '/' if route else '')
    assert 'Albert Einstein' not in raw and 'example_pdf' not in raw and 'You can even add' not in raw
    assert not re.search(r'{%|{{\s*(site|page|paper|content)\b', raw), f'Unrendered Liquid: {path}'
    for href in page.links:
        u = urlsplit(href)
        if not u.scheme and not u.netloc:
            dest = root / unquote(u.path).lstrip('/') if u.path else path
            if dest.is_dir(): dest = dest / 'index.html'
            assert dest.exists(), f'Broken internal link {href} in {path}'
            if u.fragment:
                target_page = Page(dest)
                target_page.feed(dest.read_text())
                assert unquote(u.fragment) in target_page.ids, f'Broken fragment {href} in {path}'
        elif u.scheme == 'http':
            raise AssertionError(f'Insecure URL {href}')
    if route == 'publications': assert page.publications == 27
    print(f'PASS: {path} — heading, links, images, canonical, IDs, template cleanup')

css = Path('assets/css/academic.css').read_text()
assert css.count('{') == css.count('}')
for feature in ('prefers-reduced-motion', '@media print', ':focus-visible', '[hidden]', 'max-width:580px'):
    assert feature in css
print('PASS: responsive, print, reduced-motion and keyboard-focus rules present')

home = (root / 'index.html').read_text()
cv = (root / 'cv/index.html').read_text()
assert '<h1 id="intro-title">ChunKit Chan</h1>' in home
for removed in ('AI Research · HKUST', 'class="hero-statement"', 'class="intro"', 'class="contact-section"', 'agent collaboration'):
    assert removed not in home, f'Removed content returned: {removed}'
assert 'ChunKit Chan<span aria-hidden="true">.</span>' not in home
assert 'B.Eng.' not in cv and 'City University of Hong Kong' not in cv
for expected in ('Mental World Models', '>Agents</h3>', 'Selected Work', 'Get in Touch', 'MuSeToM', 'From Mind to Action'):
    assert expected in home, f'Missing requested refinement: {expected}'
assert home.count('ACL ARR, October 2026 · Not Yet Accepted') == 2
assert 'Lion:' not in home
assert 'LLM-Hanabi' not in home and 'Second-Author Work' in home
assert 'mental world models' not in home and 'Mental World Models' in cv
assert 'class="topic-number"' not in home and 'class="topic-examples"' not in home
assert '<p class="eyebrow">Research</p>' not in home
assert 'class="opportunity"' in home, 'Keep the unmarked job-availability banner'
print('PASS: annotated removals, mental world models, Agents, capitalization, representative papers, and retained job banner')

publications = (root / 'publications/index.html').read_text()
assert '<p>Large Language Models, Post-Training, and Theory of Mind.</p>' in publications
assert '.research-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr))' in css
assert '.research-grid{grid-template-columns:1fr;gap:18px}' in css
assert '.hero h1{font-family:Newsreader,Georgia,serif;' in css
assert 'class="research-papers"' in home
print('PASS: restored responsive cards, distinctive name typography, paper links, and requested publication subtitle')

for text in (home, cv, publications):
    assert 'Discourse-Aware Prompt for Argument Impact Classification' not in text
    assert 'chan2023discourse' not in text
for text in (home, cv):
    assert text.count('ACL Outstanding Reviewers Award') == 1
    assert text.index('Hong Kong PhD Fellowship', text.index('Honors &amp; Awards') if 'Honors &amp; Awards' in text else text.index('Honors & Awards')) < text.index('ACL Outstanding Reviewers Award')
    assert 'class="honors service-awards"' not in text
    assert text.index('ACL Outstanding Reviewers Award') < text.index('<h2>Academic Service</h2>')
print('PASS: agent-card substitution, fellowship ordering, service award placement, and removed publication')

for key in ('chan2023discourse', 'li2025backdoor', 'li-etal-2024-privlm', 'chan-privacy'):
    assert f'id="{key}"' not in publications
print('PASS: all four requested publication removals')
