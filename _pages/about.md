---
layout: academic
title: About
permalink: /
description: ChunKit Chan is a Ph.D. candidate at HKUST working on Large Language Models, Post-Training, Theory of Mind, and Mental World Models, with research experience at NVIDIA and Amazon.
---
<section class="hero" aria-labelledby="intro-title">
  <div class="hero-copy">
    <h1 id="intro-title">ChunKit Chan</h1>
    <p class="hero-role">{{ site.data.profile.role }}</p>
    <p class="bio">I’m a Ph.D. candidate at <a href="https://hkust.edu.hk/">HKUST</a>, advised by <a href="https://cse.hkust.edu.hk/~yqsong/">Prof. Yangqiu Song</a> and supported by the Hong Kong PhD Fellowship. I am currently a Scientist Intern at <strong>NVIDIA</strong> and previously an Applied Scientist Intern at <strong>Amazon</strong>.</p>
    <div class="profile-links" aria-label="Profile links">
      <a class="button button-primary" href="mailto:{{ site.email }}">Get in Touch <span aria-hidden="true">↗</span></a>
      <a href="https://scholar.google.com/citations?user={{ site.scholar_userid }}">Google Scholar <span aria-hidden="true">↗</span></a>
      <a href="https://github.com/{{ site.github_username }}">GitHub <span aria-hidden="true">↗</span></a>
      <a href="{{ '/cv/' | relative_url }}">View CV <span aria-hidden="true">↗</span></a>
    </div>
  </div>
  <figure class="portrait">
    <img src="{{ '/assets/img/portrait.jpg' | relative_url }}?v=20261112b" alt="ChunKit Chan standing outdoors" width="600" height="800" fetchpriority="high">
    <figcaption>ChunKit Chan <span>HKUST · Computer Science & Engineering</span></figcaption>
  </figure>
</section>
<aside class="opportunity" aria-label="Career availability">
  <div><span class="status-dot" aria-hidden="true"></span><strong>Open to Full-Time Opportunities</strong><p>AI Research & Applied Science</p></div>
  <a href="mailto:{{ site.email }}?subject=Full-time%20opportunity">Let’s Talk <span aria-hidden="true">↗</span></a>
</aside>
<section class="section" aria-labelledby="research-title">
  <div class="section-heading"><div><h2 id="research-title">Research Interests</h2></div></div>
  <p class="section-intro">I work toward language models and agents that understand people and make better decisions. My research connects Theory of Mind and Mental World Models with Post-Training and agent behavior.</p>
  <div class="research-grid">
    {% for topic in site.data.profile.research %}
    <article class="research-topic">
      <h3>{{ topic.title }}</h3>
      <div class="research-body">
        <p>{{ topic.description }}</p>
        <ul class="research-papers" aria-label="Related papers for {{ topic.title | escape }}">
          {% for paper in topic.papers %}
          <li><a href="{% if paper.url contains '://' %}{{ paper.url }}{% else %}{{ paper.url | relative_url }}{% endif %}">{{ paper.title }}</a>{% if paper.note %}<span class="research-paper-note">{{ paper.note }}</span>{% endif %}</li>
          {% endfor %}
        </ul>
      </div>
    </article>
    {% endfor %}
  </div>
</section>
<section class="section" aria-labelledby="selected-title">
  <div class="section-heading"><div><h2 id="selected-title">Selected Work</h2></div><a class="text-link" href="{{ '/publications/' | relative_url }}">Full Publication List <span aria-hidden="true">↗</span></a></div>
  <p class="section-intro">Selected first- and second-author work on mental-state understanding, motivation reasoning, and Post-Training. Manuscripts under review are labeled separately from accepted publications.</p>
  <div class="selected-papers">
    {% for paper in site.data.selected_research %}
    <article class="selected-paper">
      <div class="paper-label"><span{% if paper.status == 'Under review' %} class="review-venue"{% endif %}>{{ paper.venue }}</span><span>{{ paper.topic }}</span></div>
      <div class="paper-copy"><h3>{% if paper.status == 'Under review' %}<a href="{{ paper.url | relative_url }}">{{ paper.title }}</a>{% else %}<a href="{{ paper.url }}">{{ paper.title }} <span class="paper-arrow" aria-hidden="true">↗</span></a>{% endif %}</h3><p>{{ paper.summary }}</p><p class="paper-authorship">{{ paper.authorship }}{% if paper.status == 'Under review' %} · ACL ARR, October 2026 · Not Yet Accepted{% endif %}</p></div>
    </article>
    {% endfor %}
  </div>
</section>
<section class="section" aria-labelledby="experience-title">
  <div class="section-heading"><div><h2 id="experience-title">Research Experience</h2></div><a class="text-link" href="{{ '/cv/' | relative_url }}">Experience & CV <span aria-hidden="true">↗</span></a></div>
  <div class="experience-list">{% for job in site.data.profile.experience %}<article class="experience-row"><div class="experience-organization"><h3>{{ job.organization }}</h3><p>{{ job.dates }}</p></div><div><h4>{{ job.role }}{% if job.location %}<span> · {{ job.location }}</span>{% endif %}</h4><p>{{ job.summary }}</p></div></article>{% endfor %}</div>
</section>
<section class="section academic-details" aria-label="Recognition and academic service">
  <div><h2>Honors & Awards</h2><ul class="honors">{% for award in site.data.profile.honors %}<li><span>{{ award.name }}</span><span>{{ award.year }}</span></li>{% endfor %}</ul></div>
  <div><h2>Academic Service</h2><h3>Area Chair</h3><p>ACL Rolling Review, ACL 2025, and EMNLP 2025.</p><h3>Reviewer</h3><p>ACL Rolling Review, ACL, EMNLP, COLING, COLM, AAAI, and Artificial Intelligence Journal.</p><a class="text-link service-link" href="{{ '/cv/#service' | relative_url }}">Service Details <span aria-hidden="true">↗</span></a></div>
</section>
