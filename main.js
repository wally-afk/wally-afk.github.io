/* ═══════════════════════════════════════════════════════════════
   WALEED SABIR — PORTFOLIO JAVASCRIPT
   Configuration, data, and all interactivity
   ═══════════════════════════════════════════════════════════════ */

'use strict';

/* ─── SITE CONFIGURATION ────────────────────────────────────────────
   Replace empty strings with your actual URLs.
   Links remain visually disabled until configured.
   ─────────────────────────────────────────────────────────────── */
const siteConfig = {
  github: 'https://github.com/wally-afk',
  linkedin: 'https://www.linkedin.com/in/waleedsabir08',
  email: 'waleedsabir08@gmail.com',
  resume: './assets/Waleed_Sabir_CV.pdf',

  // Project-specific links
  olistGithub: '',   // Olist project repo
  olistCase: '',   // Case study / live project link
  automationGithub: '',  // Automation project repo
  sequenceGithub: '',   // Sequence mining repo
};

/* ─── TELEMETRY DATA ──────────────────────────────────────────────── */
const telemetryData = [
  { id: 'projects', value: 6, suffix: '', label: 'Selected Projects' },
  { id: 'orders', value: 96480, suffix: '', label: 'Processed Orders' },
  { id: 'tech', value: 15, suffix: '+', label: 'Core Technologies' },
  { id: 'domains', value: 6, suffix: '+', label: 'Modeled Data Domains' },
];

/* ─── SCHEMA NODE METADATA ───────────────────────────────────────────
   Source for confirmed numbers: Olist public dataset (Kaggle).
   ─────────────────────────────────────────────────────────────── */
const schemaNodes = {
  'fact-order': {
    name: 'FACT_ORDER',
    type: 'Fact Table',
    grain: '1 row per order',
    rows: '99,441',
    purpose: 'Modeled central fact table tracking core order lifecycle events. Contains foreign keys to dimensional context.',
    source: 'Modeled · Olist public dataset',
  },
  'dim-customer': {
    name: 'DIM_CUSTOMER',
    type: 'Dimension Table',
    grain: '1 row per customer',
    rows: '99,441',
    purpose: 'Modeled customer dimension mapped to geographic attributes (city, state, zip).',
    source: 'Modeled · Olist public dataset',
  },
  'dim-product': {
    name: 'DIM_PRODUCT',
    type: 'Dimension Table',
    grain: '1 row per product',
    rows: '~32,951',
    purpose: 'Modeled product dimension containing category and physical specification attributes.',
    source: 'Modeled · Olist public dataset',
  },
  'dim-seller': {
    name: 'DIM_SELLER',
    type: 'Dimension Table',
    grain: '1 row per seller',
    rows: '~3,095',
    purpose: 'Modeled seller dimension with location hierarchies.',
    source: 'Modeled · Olist public dataset',
  },
  'dim-date': {
    name: 'DIM_DATE',
    type: 'Dimension Table',
    grain: '1 row per calendar date',
    rows: 'Generated',
    purpose: 'Generated date dimension for DAX time-intelligence (YTD, QTD, YoY calculations).',
    source: 'Calculated · Calendar dimension',
  },
  'fact-payment': {
    name: 'FACT_PAYMENT',
    type: 'Fact Table',
    grain: '1 row per payment installment',
    rows: '~103,886',
    purpose: 'Secondary fact table for payment transactions. Captures multiple payment methods per order.',
    source: 'Modeled · Olist public dataset',
  },
};

/* ─── TECH ARSENAL DATA ──────────────────────────────────────────── */
const techArsenal = {
  'Data': [
    { name: 'Python', uses: ['Data cleaning', 'Statistical analysis', 'Machine learning', 'Automation'] },
    { name: 'SQL', uses: ['Transformation queries', 'Dimensional modeling', 'Complex joins'] },
    { name: 'PostgreSQL', uses: ['Relational storage', 'Workflow data persistence', 'Indexing'] },
    { name: 'Pandas', uses: ['DataFrame manipulation', 'Analysis', 'Data cleaning'] },
    { name: 'Scikit-learn', uses: ['ML modeling', 'Classification', 'Clustering', 'Evaluation'] },
  ],
  'Analytics & BI': [
    { name: 'Power BI', uses: ['Dashboard development', 'KPI visualization', 'Report design'] },
    { name: 'DAX', uses: ['Calculated measures', 'Time intelligence', 'Custom aggregations'] },
    { name: 'SSAS', uses: ['Analytical services', 'Tabular model definition'] },
    { name: 'SSRS', uses: ['Paginated reporting', 'Scheduled report delivery'] },
    { name: 'Star Schemas', uses: ['Dimensional modeling', 'Fact & dimension design', 'Query optimization'] },
  ],
  'Engineering & Automation': [
    { name: 'Docker', uses: ['Container orchestration', 'Service isolation', 'Reproducible environments'] },
    { name: 'Docker Compose', uses: ['Multi-container stacks', 'Service networking'] },
    { name: 'n8n', uses: ['Workflow automation', 'Event-driven pipelines', 'API routing'] },
    { name: 'Caddy', uses: ['Reverse proxy', 'Automatic HTTPS', 'Server configuration'] },
    { name: 'Linux CLI', uses: ['Server administration', 'Bash scripting', 'File & process management'] },
  ],
};

/* ═══════════════════════════════════════════════════════════════
   INITIALISATION
   ═══════════════════════════════════════════════════════════════ */
document.addEventListener('DOMContentLoaded', () => {
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  initNav();
  initMobileMenu();
  injectConfigLinks();
  buildTelemetry();
  buildArsenal();
  initExpandToggles();
  initSchemaInspector();
  initScrollReveal(reducedMotion);
  initCountUp(reducedMotion);
});

/* ─── NAVIGATION ─────────────────────────────────────────────────── */
function initNav() {
  const nav = document.getElementById('site-nav');
  if (!nav) return;

  const onScroll = () => {
    nav.classList.toggle('scrolled', window.scrollY > 20);
  };
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  // Smooth-scroll nav links; close mobile menu after click
  nav.querySelectorAll('a[href^="#"]').forEach(link => {
    link.addEventListener('click', e => {
      const target = document.querySelector(link.getAttribute('href'));
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth' });
      }
    });
  });
}

/* ─── MOBILE MENU ────────────────────────────────────────────────── */
function initMobileMenu() {
  const toggle = document.getElementById('nav-toggle');
  const menu = document.getElementById('nav-mobile');
  if (!toggle || !menu) return;

  const open = () => { menu.classList.add('open'); toggle.setAttribute('aria-expanded', 'true'); };
  const close = () => { menu.classList.remove('open'); toggle.setAttribute('aria-expanded', 'false'); };
  const isOpen = () => menu.classList.contains('open');

  toggle.addEventListener('click', () => isOpen() ? close() : open());

  document.addEventListener('keydown', e => { if (e.key === 'Escape' && isOpen()) close(); });

  menu.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
      close();
      const target = document.querySelector(link.getAttribute('href'));
      if (target) setTimeout(() => target.scrollIntoView({ behavior: 'smooth' }), 50);
    });
  });
}

/* ─── CONFIG LINK INJECTION ──────────────────────────────────────── */
function injectConfigLinks() {
  const map = {
    'olist-case': siteConfig.olistCase,
    'olist-github': siteConfig.olistGithub,
    'automation-github': siteConfig.automationGithub,
    'sequence-github': siteConfig.sequenceGithub,
    'github': siteConfig.github,
    'linkedin': siteConfig.linkedin,
    'email': siteConfig.email,
    'resume': siteConfig.resume,
  };

  document.querySelectorAll('[data-config-link]').forEach(el => {
    const key = el.dataset.configLink;
    const val = map[key];

    if (val) {
      if (key === 'email') {
        el.href = 'mailto:' + val;
      } else {
        el.href = val;
        el.target = '_blank';
        el.rel = 'noopener noreferrer';
      }
    } else {
      el.classList.add('btn--disabled');
      el.setAttribute('aria-disabled', 'true');
      el.setAttribute('title', 'Link not configured — update siteConfig in main.js');
      el.removeAttribute('href');
    }
  });
}

/* ─── TELEMETRY GRID ─────────────────────────────────────────────── */
function buildTelemetry() {
  const grid = document.getElementById('telemetry-grid');
  if (!grid) return;

  telemetryData.forEach(item => {
    const cell = document.createElement('div');
    cell.className = 'telemetry-metric';

    const valEl = document.createElement('span');
    valEl.className = 'telemetry-metric__value';
    valEl.dataset.countup = '';
    valEl.dataset.target = item.value;
    valEl.dataset.suffix = item.suffix;
    valEl.textContent = '0' + item.suffix;

    const lblEl = document.createElement('span');
    lblEl.className = 'telemetry-metric__label';
    lblEl.textContent = item.label;

    cell.append(valEl, lblEl);
    grid.appendChild(cell);
  });
}

/* ─── TECH ARSENAL ───────────────────────────────────────────────── */
function buildArsenal() {
  const grid = document.getElementById('arsenal-grid');
  if (!grid) return;

  Object.entries(techArsenal).forEach(([category, techs]) => {
    const card = document.createElement('div');
    card.className = 'arsenal-card';

    const header = document.createElement('div');
    header.className = 'arsenal-col-header';
    header.textContent = category;

    const tagsDiv = document.createElement('div');
    tagsDiv.className = 'arsenal-tags';

    techs.forEach(tech => {
      const wrap = document.createElement('div');
      wrap.className = 'arsenal-tag-wrap';

      const tag = document.createElement('span');
      tag.className = 'tech-tag';
      tag.setAttribute('tabindex', '0');
      tag.textContent = tech.name;

      const tooltip = document.createElement('div');
      tooltip.className = 'arsenal-tooltip';
      tooltip.setAttribute('role', 'tooltip');

      const tName = document.createElement('span');
      tName.className = 'arsenal-tooltip__name';
      tName.textContent = tech.name;
      tooltip.appendChild(tName);

      tech.uses.forEach(use => {
        const u = document.createElement('span');
        u.className = 'arsenal-tooltip__use';
        u.textContent = use;
        tooltip.appendChild(u);
      });

      wrap.append(tag, tooltip);
      tagsDiv.appendChild(wrap);
    });

    card.append(header, tagsDiv);
    grid.appendChild(card);
  });
}

/* ─── EXPAND / COLLAPSE ──────────────────────────────────────────── */
function initExpandToggles() {
  document.querySelectorAll('.expand-trigger').forEach(trigger => {
    const panelId = trigger.getAttribute('aria-controls');
    const panel = document.getElementById(panelId);
    if (!panel) return;

    trigger.addEventListener('click', () => {
      const expanded = trigger.getAttribute('aria-expanded') === 'true';

      trigger.setAttribute('aria-expanded', String(!expanded));
      panel.classList.toggle('open', !expanded);

      // Trigger count-up for any metrics inside the panel on first open
      if (!expanded) {
        panel.querySelectorAll('[data-countup]:not(.counted)').forEach(el => {
          animateCountUp(el);
          el.classList.add('counted');
        });
      }
    });
  });
}

/* ─── SCHEMA NODE INSPECTOR ──────────────────────────────────────── */
function initSchemaInspector() {
  const detail = document.getElementById('schema-detail');
  if (!detail) return;

  document.querySelectorAll('.schema-node').forEach(node => {
    const activate = () => {
      const id = node.dataset.nodeId;
      const data = schemaNodes[id];
      if (!data) return;

      // Update selection
      document.querySelectorAll('.schema-node').forEach(n => n.classList.remove('selected'));
      node.classList.add('selected');

      // Render detail
      detail.innerHTML = `
        <div class="schema-detail__name">${data.name}</div>
        <div class="schema-detail__field">
          <span class="schema-detail__field-label">Type</span>
          <span class="schema-detail__field-value">${data.type}</span>
        </div>
        <div class="schema-detail__field">
          <span class="schema-detail__field-label">Grain</span>
          <span class="schema-detail__field-value">${data.grain}</span>
        </div>
        <div class="schema-detail__field">
          <span class="schema-detail__field-label">Rows</span>
          <span class="schema-detail__field-value">${data.rows}</span>
        </div>
        <div class="schema-detail__field">
          <span class="schema-detail__field-label">Purpose</span>
          <span class="schema-detail__field-value">${data.purpose}</span>
        </div>
        <div class="schema-detail__field">
          <span class="schema-detail__field-label">Source</span>
          <span class="schema-detail__field-value">${data.source}</span>
        </div>
      `;
    };

    node.addEventListener('click', activate);
    node.addEventListener('keydown', e => {
      if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); activate(); }
    });
  });
}

/* ─── COUNT-UP ANIMATION ─────────────────────────────────────────── */
function initCountUp(reducedMotion) {
  const elements = document.querySelectorAll('[data-countup]:not(.counted)');
  if (reducedMotion) {
    elements.forEach(el => {
      el.textContent = formatNumber(Number(el.dataset.target)) + (el.dataset.suffix || '');
      el.classList.add('counted');
    });
    return;
  }

  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const el = entry.target;
        if (el.classList.contains('counted')) return;
        el.classList.add('counted');
        animateCountUp(el);
        observer.unobserve(el);
      }
    });
  }, { threshold: 0.5 });

  elements.forEach(el => observer.observe(el));
}

function animateCountUp(el) {
  const target = Number(el.dataset.target);
  const suffix = el.dataset.suffix || '';
  const duration = Math.min(1400, Math.max(800, target * 0.015));
  const start = performance.now();

  const tick = now => {
    const progress = Math.min((now - start) / duration, 1);
    const eased = 1 - Math.pow(1 - progress, 3);
    const current = Math.floor(eased * target);
    el.textContent = formatNumber(current) + suffix;
    if (progress < 1) requestAnimationFrame(tick);
    else el.textContent = formatNumber(target) + suffix;
  };

  requestAnimationFrame(tick);
}

function formatNumber(n) {
  return n >= 1000 ? n.toLocaleString('en-US') : String(n);
}

/* ─── SCROLL REVEAL ──────────────────────────────────────────────── */
function initScrollReveal(reducedMotion) {
  if (reducedMotion) return;

  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.08, rootMargin: '0px 0px -40px 0px' });

  document.querySelectorAll('[data-reveal]').forEach(el => observer.observe(el));
}
