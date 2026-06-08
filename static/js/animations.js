'use strict';

// ---- Stat counter animation (IntersectionObserver) ----
(function () {
  const items = document.querySelectorAll('[data-target]');
  if (!items.length) return;

  function easeOut(t) { return 1 - Math.pow(1 - t, 3); }

  function animateCounter(el) {
    const raw = el.getAttribute('data-target').replace(/[^0-9.]/g, '');
    const end = parseFloat(raw);
    if (isNaN(end)) return;

    const suffix = el.getAttribute('data-suffix') || '';
    const counterEl = el.querySelector('.stat-counter');
    if (!counterEl) return;

    const duration = 1800;
    const startTime = performance.now();
    const isFloat = raw.includes('.');

    function tick(now) {
      const elapsed = now - startTime;
      const progress = Math.min(elapsed / duration, 1);
      const value = easeOut(progress) * end;
      counterEl.textContent = isFloat ? value.toFixed(1) : Math.round(value).toLocaleString();
      if (progress < 1) requestAnimationFrame(tick);
    }
    requestAnimationFrame(tick);
  }

  const observer = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) {
        animateCounter(entry.target);
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.3 });

  items.forEach(function (el) { observer.observe(el); });
})();

// ---- Fade-in on scroll ----
(function () {
  const style = document.createElement('style');
  style.textContent = `
    .fade-in { opacity: 0; transform: translateY(24px); transition: opacity 0.6s ease, transform 0.6s ease; }
    .fade-in.visible { opacity: 1; transform: none; }
  `;
  document.head.appendChild(style);

  const targets = document.querySelectorAll(
    '.program-row, .program-full, .news-card, .team-card, .testimonial-card, .stat-item, .gallery-item'
  );
  targets.forEach(function (el) { el.classList.add('fade-in'); });

  const observer = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });

  targets.forEach(function (el) { observer.observe(el); });
})();
