/* Smith's Farm — minimal interactions (no dependencies) */
(function () {
  'use strict';

  /* Mobile nav toggle */
  var burger = document.querySelector('.nav__burger');
  var mobile = document.getElementById('mobile-menu');
  if (burger && mobile) {
    burger.addEventListener('click', function () {
      var open = burger.getAttribute('aria-expanded') === 'true';
      burger.setAttribute('aria-expanded', String(!open));
      burger.setAttribute('aria-label', open ? '메뉴 열기' : '메뉴 닫기');
      mobile.hidden = open;
    });
    mobile.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () {
        burger.setAttribute('aria-expanded', 'false');
        mobile.hidden = true;
      });
    });
  }

  /* Menu tabs */
  var tabs = Array.prototype.slice.call(document.querySelectorAll('.tab[role="tab"]'));
  tabs.forEach(function (tab) {
    tab.addEventListener('click', function () { activate(tab); });
    tab.addEventListener('keydown', function (e) {
      var i = tabs.indexOf(tab);
      if (e.key === 'ArrowRight') { activate(tabs[(i + 1) % tabs.length], true); }
      if (e.key === 'ArrowLeft')  { activate(tabs[(i - 1 + tabs.length) % tabs.length], true); }
    });
  });
  function activate(tab, focus) {
    tabs.forEach(function (t) {
      var on = t === tab;
      t.classList.toggle('is-active', on);
      t.setAttribute('aria-selected', String(on));
      var panel = document.getElementById(t.getAttribute('aria-controls'));
      if (panel) { panel.hidden = !on; }
    });
    if (focus) { tab.focus(); }
  }

  /* Reveal on scroll */
  var targets = document.querySelectorAll('.card, .tile, .gallery__item, .story, .trust__grid li, .faq details');
  targets.forEach(function (el) { el.classList.add('reveal'); });
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('is-in'); io.unobserve(en.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.1 });
    targets.forEach(function (el) { io.observe(el); });
  } else {
    targets.forEach(function (el) { el.classList.add('is-in'); });
  }
})();

/* Sticky mobile reservation bar: show once hero scrolls out of view */
(function () {
  'use strict';
  var bar = document.getElementById('sticky-cta');
  var hero = document.querySelector('.hero');
  if (!bar || !hero) { return; }
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        bar.classList.toggle('is-visible', !en.isIntersecting);
      });
    }, { rootMargin: '-56px 0px 0px 0px' });
    io.observe(hero);
  } else {
    bar.classList.add('is-visible');
  }
})();

/* Lightbox: zoom menu photos (native <dialog>, keyboard + screen-reader friendly) */
(function () {
  'use strict';
  var dlg = document.getElementById('lightbox');
  if (!dlg || typeof dlg.showModal !== 'function') { return; }
  var img = document.getElementById('lightbox-img');
  var cap = document.getElementById('lightbox-caption');
  var opener = null;

  function open(btn) {
    opener = btn;
    var src = btn.getAttribute('data-large');
    var text = btn.getAttribute('data-caption') || '';
    var thumb = btn.querySelector('img');
    img.src = src;
    img.alt = thumb ? thumb.alt : text;
    cap.textContent = text;
    dlg.showModal();
    dlg.querySelector('[data-close]').focus();
  }
  function close() {
    if (dlg.open) { dlg.close(); }
  }
  document.querySelectorAll('.zoom[data-large]').forEach(function (btn) {
    btn.addEventListener('click', function () { open(btn); });
  });
  dlg.querySelector('[data-close]').addEventListener('click', close);
  dlg.addEventListener('click', function (e) {
    if (e.target === dlg) { close(); }            /* backdrop click */
  });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && dlg.open) { e.preventDefault(); close(); }
  });
  dlg.addEventListener('cancel', function (e) { e.preventDefault(); close(); });
  dlg.addEventListener('close', function () {
    img.removeAttribute('src');
    if (opener) { opener.focus(); opener = null; } /* return focus */
  });
})();
