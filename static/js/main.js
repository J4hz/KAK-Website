'use strict';

// ---- Navbar: transparent over hero, white when scrolled ----
(function () {
  var nav = document.querySelector('nav.site-nav');
  if (!nav) return;
  function update() {
    if (window.scrollY > 20) { nav.classList.add('scrolled'); }
    else { nav.classList.remove('scrolled'); }
  }
  window.addEventListener('scroll', update, { passive: true });
  update();
})();

// ---- Mobile nav toggle (matches original body.nav-open approach) ----
(function () {
  var toggle = document.getElementById('nav-toggle');
  if (!toggle) return;
  toggle.addEventListener('click', function () {
    var isOpen = document.body.classList.toggle('nav-open');
    toggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
  });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') {
      document.body.classList.remove('nav-open');
      toggle.setAttribute('aria-expanded', 'false');
    }
  });
})();

// ---- Dismiss alert messages ----
(function () {
  document.querySelectorAll('.alert__close').forEach(function (btn) {
    btn.addEventListener('click', function () { btn.closest('.alert').remove(); });
  });
})();

// ---- Smooth scroll for # links ----
(function () {
  document.querySelectorAll('a[href^="#"]').forEach(function (a) {
    a.addEventListener('click', function (e) {
      var target = document.querySelector(this.getAttribute('href'));
      if (!target) return;
      e.preventDefault();
      target.scrollIntoView({ behavior: 'smooth' });
    });
  });
})();
