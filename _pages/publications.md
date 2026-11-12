---
layout: academic
permalink: /publications/
title: Publications
description: ChunKit Chan’s publications on Theory of Mind, LLM post-training, social reasoning, and AI agents. Published papers, preprints, and under-review manuscripts are labeled separately.
nav: true
nav_order: 1
---
<section class="page-intro"><h1>Publications<span class="accent">.</span></h1><p>Large Language Models, Post-Training, and Theory of Mind.</p><a class="text-link" href="https://scholar.google.com/citations?user={{ site.scholar_userid }}">Google Scholar <span aria-hidden="true">↗</span></a></section>
<p class="archive-note">Updated November 2026 from my CV, Google Scholar, and publisher records. Published versions are listed once, using their publication year. Preprints and under-review manuscripts are labeled explicitly; under-review papers are not accepted publications.</p>
<div class="search-controls" data-search-controls hidden><div><label for="publication-search">Find a Publication</label><input type="search" id="publication-search" data-publication-search placeholder="Search by title, author, or year…" autocomplete="off"></div><div><label for="publication-status">Publication Status</label><select id="publication-status" data-publication-status><option value="all">All Work</option value="Published">Published</option><option value="Preprint">Preprints</option><option value="Under review">Under Review</option></select></div><p class="search-status" data-search-status role="status" aria-live="polite" aria-atomic="true"></p></div>
<div class="publication-archive">
{% bibliography -f {{ site.scholar.bibliography }} -T academic-bib %}
</div>
