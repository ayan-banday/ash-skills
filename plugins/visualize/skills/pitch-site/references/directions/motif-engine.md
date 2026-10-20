## Part 4. The shared engine

All 20 generators use one small kit. It builds SVG as strings, so the same code runs in the browser and in Node (for tests or server-side rendering).

### 4.1 The motif colour slots

Generators never hard-code colours. They paint with seven CSS custom properties, and the page decides what those mean in each context:

- `--m1` main line, `--m2` under-line, shadow or casing, `--m3` highlight
- `--f1`, `--f2`, `--f3` fills
- `--bgc` the local background (used for over/under gaps and casings)

Each direction lists its hero mapping. Badges use one shared mapping (4.3). Because custom properties inherit, a lit badge part only has to redefine `--m1` and `--f1`.

### 4.2 Kit, filters, draw-on and badges

```js
/* ===================== SHARED KIT (string-based, works in browser and Node) ===================== */
const K = {
  f: n => Math.round(n * 100) / 100,
  P: (x, y) => `${K.f(x)} ${K.f(y)}`,
  pt: (cx, cy, r, deg) => [cx + r * Math.cos(deg * Math.PI / 180), cy + r * Math.sin(deg * Math.PI / 180)],
  poly: pts => 'M' + pts.map(p => K.P(p[0], p[1])).join('L') + 'Z',
  pl: pts => 'M' + pts.map(p => K.P(p[0], p[1])).join('L'),
  seg: (a, b) => `M${K.P(a[0], a[1])}L${K.P(b[0], b[1])}`,
  circ: (cx, cy, r) => `M${K.P(cx - r, cy)}a${K.f(r)} ${K.f(r)} 0 1 0 ${K.f(2 * r)} 0a${K.f(r)} ${K.f(r)} 0 1 0 ${K.f(-2 * r)} 0`,
  rng(seed = 7) { let a = seed >>> 0; return () => { a = (a + 0x6D2B79F5) >>> 0; let t = Math.imul(a ^ (a >>> 15), 1 | a); t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t; return ((t ^ (t >>> 14)) >>> 0) / 4294967296; }; },
  // stroke stacking: same geometry, several strokes, bottom layer first. data-o = draw-on order rank.
  stack: (d, layers, o = 0) => layers.map(l => `<path d="${d}" data-o="${o}" style="fill:none;stroke:${l.c};stroke-width:${l.w}${l.o != null ? `;opacity:${l.o}` : ''}${l.dash ? `;stroke-dasharray:${l.dash}` : ''}" stroke-linecap="${l.cap || 'round'}" stroke-linejoin="round"${l.t ? ` transform="translate(${l.t})"` : ''}/>`).join(''),
  fill: (d, c, extra = '') => `<path d="${d}" style="fill:${c};stroke:none" ${extra}/>`,
  part: (id, inner, extra = '') => `<g class="part" data-part="${id}" ${extra}>${inner}</g>`,
  svg: (m, label = '') => `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${m.w} ${m.h}" role="img" aria-label="${label}"><defs>${m.defs || ''}</defs>${m.inner}</svg>`,
};

/* Filters. Apply ONE filter per group, never per path (cost scales with filtered area x count). */
const FX = {
  powder: (id = 'powder', k = 1) => `<filter id="${id}" x="-5%" y="-5%" width="110%" height="110%"><feTurbulence type="fractalNoise" baseFrequency=".035" numOctaves="2" seed="3" result="warp"/><feDisplacementMap in="SourceGraphic" in2="warp" scale="${5 * k}" xChannelSelector="R" yChannelSelector="G" result="a"/><feTurbulence type="fractalNoise" baseFrequency="1.1" seed="9" result="grit"/><feDisplacementMap in="a" in2="grit" scale="${2.4 * k}" xChannelSelector="R" yChannelSelector="G" result="b"/><feGaussianBlur in="b" stdDeviation="${1.1 * k}"/></filter>`,
  rough: (id, freq = .04, scale = 3, seed = 2) => `<filter id="${id}" x="-5%" y="-5%" width="110%" height="110%"><feTurbulence type="fractalNoise" baseFrequency="${freq}" numOctaves="2" seed="${seed}" result="n"/><feDisplacementMap in="SourceGraphic" in2="n" scale="${scale}" xChannelSelector="R" yChannelSelector="G"/></filter>`,
  hblur: (id, x = 1.2) => `<filter id="${id}" x="-5%" width="110%"><feGaussianBlur stdDeviation="${x} 0"/></filter>`,
  speckle: (id, freq = .9, seed = 4) => `<filter id="${id}"><feTurbulence type="fractalNoise" baseFrequency="${freq}" seed="${seed}" result="n"/><feColorMatrix in="n" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 -5 0 0 0 4" result="m"/><feComposite in="SourceGraphic" in2="m" operator="in"/></filter>`,
  squeeze: (id) => `<filter id="${id}"><feMorphology in="SourceAlpha" operator="erode" radius=".7" result="e"/><feComposite in="SourceAlpha" in2="e" operator="out" result="edge"/><feFlood flood-color="#000" flood-opacity=".35"/><feComposite in2="edge" operator="in" result="rim"/><feMerge><feMergeNode in="SourceGraphic"/><feMergeNode in="rim"/></feMerge></filter>`,
  woodgrain: (id) => `<filter id="${id}"><feTurbulence type="fractalNoise" baseFrequency=".012 .45" numOctaves="3" seed="5" result="g"/><feColorMatrix in="g" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1.4 0 0 0 -.55" result="ga"/><feComposite in="ga" in2="SourceGraphic" operator="in" result="gm"/><feFlood flood-color="#000" flood-opacity=".22"/><feComposite in2="gm" operator="in" result="dark"/><feMerge><feMergeNode in="SourceGraphic"/><feMergeNode in="dark"/></feMerge></filter>`,
  crackle: (id) => `<filter id="${id}"><feTurbulence type="turbulence" baseFrequency=".05" numOctaves="1" seed="11" result="t"/><feColorMatrix in="t" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 -24 0 0 0 1" result="c"/><feFlood flood-color="#000" flood-opacity=".09"/><feComposite in2="c" operator="in" result="lines"/><feComposite in="lines" in2="SourceAlpha" operator="in" result="cl"/><feMerge><feMergeNode in="SourceGraphic"/><feMergeNode in="cl"/></feMerge></filter>`,
  wash: (id) => `<filter id="${id}" x="-5%" y="-5%" width="110%" height="110%"><feTurbulence type="fractalNoise" baseFrequency=".06" numOctaves="3" seed="6" result="n"/><feDisplacementMap in="SourceGraphic" in2="n" scale="4" xChannelSelector="R" yChannelSelector="G" result="d"/><feGaussianBlur in="d" stdDeviation=".7"/></filter>`,
};

/* ===================== BROWSER: draw-on staging + section badges ===================== */
function drawOn(svg, { stagger = 110, dur = 1100, ease = 'cubic-bezier(.65,0,.35,1)' } = {}) {
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  const ps = [...svg.querySelectorAll('path[data-o]')].filter(p => !p.style.strokeDasharray);   // dashed lines reveal via fade instead
  const ranks = [...new Set(ps.map(p => +p.dataset.o))].sort((a, b) => a - b);
  ps.forEach(p => { const L = Math.ceil(p.getTotalLength()); p.style.strokeDasharray = L; p.style.strokeDashoffset = L;
    p.style.transition = `stroke-dashoffset ${dur}ms ${ease} ${ranks.indexOf(+p.dataset.o) * stagger}ms`; });
  const io = new IntersectionObserver(([e]) => { if (e.isIntersecting) { ps.forEach(p => p.style.strokeDashoffset = 0); io.disconnect(); } }, { threshold: .3 });
  io.observe(svg);
}
function badge(gen, lit, opts = {}) {
  const host = document.createElement('span'); host.className = 'badge';
  host.innerHTML = K.svg(gen({ ...opts, badge: true }));
  host.querySelectorAll('.part').forEach(g => g.classList.toggle('lit', g.dataset.part === lit || g.dataset.group === lit));
  return host;
}
```

### 4.3 Badge and grain CSS

```css
/* Section badge: whole motif in muted, the section's part lit in accent-1 */
.badge{display:inline-block;width:56px;height:56px;
  --m1:var(--muted);--m2:var(--line);--m3:var(--card);--f1:var(--tint-1);--f2:var(--tint-2);--f3:var(--tint-3);--bgc:var(--card)}
.badge svg{width:100%;height:100%}
.badge .part{opacity:.3;transition:opacity .4s}
.badge .part.lit{opacity:1;--m1:var(--accent-1);--f1:var(--accent-1);--f2:var(--marker);--f3:var(--accent-2)}

/* Paper grain over the whole page, about 9% noise, multiplied */
body::after{content:"";position:fixed;inset:0;pointer-events:none;z-index:50;mix-blend-mode:multiply;opacity:.55;
  background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='240' height='240'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='2' stitchTiles='stitch'/%3E%3CfeColorMatrix values='0 0 0 0 .14 0 0 0 0 .11 0 0 0 0 .09 0 0 0 .09 0'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E")}

@media (prefers-reduced-motion: reduce){*{animation:none!important;transition:none!important}}
```

Usage:

```js
const hero = document.querySelector('#hero-motif');
hero.innerHTML = K.svg(kolam(), 'Kolam: three needs around one way of working');
drawOn(hero.querySelector('svg'));
document.querySelectorAll('[data-badge]').forEach(el => el.append(badge(kolam, el.dataset.badge))); // data-badge="s2"
```

### 4.4 Performance notes

- Apply a filter to one wrapping group, never to each path. Filter cost scales with filtered area times count.
- `feTurbulence` is the most expensive primitive. Keep filtered heroes under about 700px wide; badges never use filters (every generator skips them when `badge:true`).
- Generator timings below were measured in Node 24 (average of 20 runs). All are under 2 ms, so generate at load; there is no need to pre-render.

---

