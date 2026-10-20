/* Azulejo · "the pattern tile": motif generator. Needs kit.js (K, FX). */
function azulejo(o = {}) {
  const T = 180, g = 4, m = 18;
  let q = '', fl = '', edge = '';
  for (let k = 0; k < 4; k++) { const a = k * 22.5 + 11.25, t = K.pt(0, 0, 74, a), l = K.pt(0, 0, 40, a - 12), r = K.pt(0, 0, 40, a + 12);
    q += `M0 0Q${K.P(l[0], l[1])} ${K.P(t[0], t[1])}Q${K.P(r[0], r[1])} 0 0Z`; }   // quarter rosette at the shared corner
  q += 'M84 0A84 84 0 0 1 0 84'; fl = `M${T} ${T - 40}A40 40 0 0 0 ${T - 40} ${T}L${T} ${T}Z`;
  edge = `M${T / 2 - 22} ${T}A22 22 0 0 1 ${T / 2 + 22} ${T}ZM${T} ${T / 2 - 22}A22 22 0 0 0 ${T} ${T / 2 + 22}Z`;
  const tile = (id, rot, tx, ty) => K.part(id, `<g transform="translate(${tx} ${ty}) rotate(${rot})">${K.fill(`M0 0H${T}V${T}H0Z`, 'var(--m3)')}${K.fill(q + fl + edge, 'var(--f1)', 'opacity=".85"')}${K.stack(q + fl + edge, [{ c: 'var(--m1)', w: 1.6 }], 1)}</g>`);
  const C = m + T + g / 2, inner = K.fill(`M0 0H400V400H0Z`, 'var(--m2)')
    + tile('s1', 180, C - g / 2, C - g / 2) + tile('s2', 270, C + g / 2, C - g / 2) + tile('s3', 90, C - g / 2, C + g / 2) + tile('s4', 0, C + g / 2, C + g / 2)
    + K.part('core', K.fill(K.circ(C, C, 14), 'var(--f2)') + K.stack(K.circ(C, C, 14), [{ c: 'var(--m1)', w: 1.6 }], 2));
  return { w: 400, h: 400, defs: o.badge ? '' : FX.crackle('crk'), inner: o.badge ? inner : `<g filter="url(#crk)">${inner}</g>` };
}
