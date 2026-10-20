/* Bauhaus · "the three forms": motif generator. Needs kit.js (K, FX). */
function bauhaus(o = {}) {
  let grid = ''; for (let x = 40; x < 400; x += 40) grid += `M${x} 0V400M0 ${x}H400`;
  const tri = K.poly([[40, 360], [280, 360], [160, 152]]), sq = 'M180 60H340V220H180Z', ci = K.circ(150, 170, 92);
  const inner = (o.badge ? '' : K.stack(grid, [{ c: 'var(--m2)', w: .6 }], 0))
    + [[tri, 'var(--f3)', 's1'], [sq, 'var(--f1)', 's2'], [ci, 'var(--f2)', 's3']].map(([d, col, id], i) => K.part(id, K.fill(d, col) + K.stack(d, [{ c: 'var(--bgc)', w: 3 }], 1 + i))).join('') // stacked, no multiply: blue over yellow turns green
    + K.stack('M40 380H360', [{ c: 'var(--m1)', w: 6, cap: 'butt' }], 1) + K.part('core', K.fill(K.circ(212, 196, 12), 'var(--m1)'));
  return { w: 400, h: 400, defs: '', inner };
}
