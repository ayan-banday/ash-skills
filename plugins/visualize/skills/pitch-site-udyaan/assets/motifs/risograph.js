/* Risograph · "the overprint": motif generator. Needs kit.js (K, FX). */
function riso(o = {}) {
  const r = K.rng(o.seed || 3), off = () => o.badge ? 0 : K.f((r() - .5) * 6);
  const pat = (id, col, ang) => `<pattern id="${id}" width="7" height="7" patternUnits="userSpaceOnUse" patternTransform="rotate(${ang})"><circle cx="3.5" cy="3.5" r="2.6" style="fill:${col}"/></pattern>`;
  const C = [[200, 145], [140, 250], [260, 250]], cols = ['var(--f1)', 'var(--f2)', 'var(--f3)'], ang = [15, 75, 45];
  const inner = C.map(([x, y], i) => K.part('s' + (i + 1), `<g transform="translate(${off()} ${off()})" style="mix-blend-mode:multiply">${K.fill(K.circ(x, y, 98), cols[i], 'opacity=".55"')}${K.fill(K.circ(x, y, 98), `url(#ht${i})`)}</g>`)).join('')
    + K.part('core', K.fill(K.circ(200, 215, 14), 'var(--m1)'));
  return { w: 400, h: 400, defs: C.map((_, i) => pat('ht' + i, cols[i], ang[i])).join('') + (o.badge ? '' : FX.speckle('rspk', 1.2)), inner: o.badge ? inner : `<g filter="url(#rspk)">${inner}</g>` };
}
