(function () {
  const tabs = [...document.querySelectorAll('[data-platform-tab]')];
  const panels = [...document.querySelectorAll('[data-platform-panel]')];

  function selectPlatform(platform, focus) {
    tabs.forEach((tab) => {
      const selected = tab.dataset.platformTab === platform;
      tab.setAttribute('aria-selected', String(selected));
      tab.tabIndex = selected ? 0 : -1;
      if (selected && focus) tab.focus();
    });
    panels.forEach((panel) => { panel.hidden = panel.dataset.platformPanel !== platform; });
  }

  if (tabs.length) {
    tabs.forEach((tab, index) => {
      tab.addEventListener('click', () => selectPlatform(tab.dataset.platformTab));
      tab.addEventListener('keydown', (event) => {
        if (!['ArrowLeft', 'ArrowRight'].includes(event.key)) return;
        event.preventDefault();
        const direction = event.key === 'ArrowRight' ? 1 : -1;
        const next = tabs[(index + direction + tabs.length) % tabs.length];
        selectPlatform(next.dataset.platformTab, true);
      });
    });
    const prefersMac = /Mac|iPhone|iPad/i.test(navigator.platform) || /Macintosh/i.test(navigator.userAgent);
    selectPlatform(prefersMac ? 'macos' : 'windows');
  }

  const search = document.getElementById('feature-search');
  if (search) {
    const sections = [...document.querySelectorAll('[data-search-section]')];
    const quick = document.querySelector('.quick-answer');
    const status = document.getElementById('search-status');
    const noResults = document.getElementById('no-results');
    search.addEventListener('input', () => {
      const query = search.value.trim().toLocaleLowerCase('zh-CN');
      let visible = 0;
      sections.forEach((section) => {
        const hit = !query || section.textContent.toLocaleLowerCase('zh-CN').includes(query);
        section.hidden = !hit;
        if (hit) visible += 1;
      });
      quick.hidden = !!query;
      noResults.hidden = visible > 0;
      status.textContent = query ? `找到 ${visible} 个相关部分` : '';
    });
  }

  const railLinks = [...document.querySelectorAll('.manual-rail nav a')];
  const observed = railLinks
    .map((link) => document.querySelector(link.getAttribute('href')))
    .filter(Boolean);
  if ('IntersectionObserver' in window && observed.length) {
    const observer = new IntersectionObserver((entries) => {
      const current = entries
        .filter((entry) => entry.isIntersecting && !entry.target.hidden)
        .sort((a, b) => a.boundingClientRect.top - b.boundingClientRect.top)[0];
      if (!current) return;
      railLinks.forEach((link) => link.classList.toggle('current', link.hash === `#${current.target.id}`));
    }, { rootMargin: '-18% 0px -68% 0px' });
    observed.forEach((section) => observer.observe(section));
  }
})();
