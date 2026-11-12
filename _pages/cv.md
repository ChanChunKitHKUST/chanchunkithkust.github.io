---
layout: academic
permalink: /cv/
title: Experience & CV
description: ChunKit Chan’s research experience at NVIDIA and Amazon, education at HKUST, honors, and academic service. Updated November 2026.
nav: true
nav_order: 2
---
<section class="page-intro"><h1>Experience & CV</h1><p>ChunKit Chan · Ph.D. candidate at HKUST</p><div class="profile-links"><a class="button button-primary" href="mailto:{{ site.email }}">Contact Me ↗</a><button class="button button-secondary" type="button" data-print>Print / Save CV</button></div><p class="updated-note">Updated November 2026 · {{ site.email }}</p></section>
<div class="cv-content">
<section class="cv-section"><h2>Profile</h2><div><p>I am a Ph.D. candidate in Computer Science and Engineering at HKUST, supported by the Hong Kong PhD Fellowship and advised by Prof. Yangqiu Song. My research brings together <strong>Large Language Models, Theory of Mind, Mental World Models, and Post-Training</strong>.</p><p>I investigate how models infer and revise beliefs, desires, and intentions, and how these representations can support reasoning and action. My goal is to connect mental-state understanding with better decisions through Mental World Models, reinforcement fine-tuning, and agents that adapt to people and changing contexts.</p></div></section>
<section class="cv-section"><h2>Research Experience</h2><div>{% for job in site.data.profile.experience %}<article class="cv-entry"><div class="cv-entry-heading"><h3>{{ job.organization }}</h3><span>{{ job.dates }}</span></div><p class="cv-role">{{ job.role }}{% if job.location %} · {{ job.location }}{% endif %}</p><ul class="cv-bullets">{% for detail in job.details %}<li>{{ detail }}</li>{% endfor %}</ul></article>{% endfor %}</div></section>
<section class="cv-section"><h2>Education</h2><div>{% for education in site.data.profile.education %}<article class="cv-entry"><p class="cv-date">{{ education.dates }}</p><h3>{{ education.degree }}</h3><p>{{ education.institution }}</p>{% if education.note %}<p class="muted">{{ education.note }}</p>{% endif %}</article>{% endfor %}</div></section>
<section class="cv-section"><h2>Research Interests</h2><div>{% for topic in site.data.profile.research %}<article class="cv-entry"><h3>{{ topic.title }}</h3><p>{{ topic.description }}</p></article>{% endfor %}</div></section>
<section class="cv-section"><h2>Honors & Awards</h2><ul class="honors">{% for award in site.data.profile.honors %}<li><span>{{ award.name }}</span><span>{{ award.year }}</span></li>{% endfor %}</ul></section>
<section class="cv-section" id="service"><h2>Academic Service</h2><div><article class="cv-entry"><h3>Area Chair</h3><p>ACL Rolling Review (2025), ACL 2025, EMNLP 2025.</p></article><article class="cv-entry"><h3>Conference & Journal Reviewer</h3><p>ACL Rolling Review, ACL, and EMNLP (2022–2024); COLING (2024); COLM, AAAI, and Artificial Intelligence Journal (2025).</p></article></div></section>
<section class="cv-section"><h2>Publications</h2><div><p>See the <a href="{{ '/publications/' | relative_url }}">complete publication list</a> for published papers, preprints, and clearly labeled under-review manuscripts, or visit <a href="https://scholar.google.com/citations?user={{ site.scholar_userid }}">Google Scholar</a>.</p><p class="muted">First-author and co-first-author work includes XToM, NegotiationToM, the Guandan study, Persona Knowledge-Aligned Prompt Tuning, DiscoPrompt, and research on abductive inference.</p></div></section>
</div>
