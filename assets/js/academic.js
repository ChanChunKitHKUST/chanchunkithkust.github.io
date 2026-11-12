(() => {
  'use strict';
  const search = document.querySelector('[data-publication-search]');
  if (search) {
    const items = [...document.querySelectorAll('.bibliography > li')];
    const groups = [...document.querySelectorAll('.bibliography')];
    const status = document.querySelector('[data-search-status]');
    const statusFilter = document.querySelector('[data-publication-status]');
    const filter = () => {
      const query = search.value.trim().toLocaleLowerCase();
      let count = 0;
      items.forEach(item => {
        const text = item.querySelector('.publication-search-text');
        const publication = item.querySelector('[data-status]');
        const wantedStatus = statusFilter ? statusFilter.value : 'all';
        const statusMatches = wantedStatus === 'all' || (publication && publication.dataset.status === wantedStatus);
        const matches = statusMatches && (text || item).textContent.toLocaleLowerCase().includes(query);
        item.hidden = !matches;
        if (matches) count++;
      });
      groups.forEach(group => {
        const empty = ![...group.children].some(item => !item.hidden);
        group.hidden = empty;
        const heading = group.previousElementSibling;
        if (heading && /^H[2-6]$/.test(heading.tagName)) heading.hidden = empty;
      });
      status.textContent = count ? `${count} publication${count === 1 ? '' : 's'}${query ? ' found' : ''}` : 'No matching publications. Try another search or publication status.';
    };
    search.addEventListener('input', filter);
    if (statusFilter) statusFilter.addEventListener('change', filter);
    filter();
    document.querySelector('[data-search-controls]').hidden = false;
  }
  const printButton = document.querySelector('[data-print]');
  if (printButton) printButton.addEventListener('click', () => window.print());
})();
