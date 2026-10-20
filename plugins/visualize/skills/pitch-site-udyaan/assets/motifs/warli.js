/* Warli · "the tarpa circle": motif generator. Needs kit.js (K, FX). */
function warli(o = {}) {
  const c = 200, figs = { s1: '', s2: '', s3: '' }, a = 30, b = 52 / (2 * Math.PI);
  const fig = (x, y, h, ang) => {                      // two triangles meeting at the waist + circle head, rotated radially
    const R = (dx, dy) => { const t = (ang + 90) * Math.PI / 180; return [x + dx * Math.cos(t) - dy * Math.sin(t), y + dx * Math.sin(t) + dy * Math.cos(t)]; };
    return K.poly([R(-h * .32, -h * .5), R(h * .32, -h * .5), R(0, 0)]) + K.poly([R(0, 0), R(-h * .3, h * .5), R(h * .3, h * .5)]) + K.circ(...R(0, -h * .72), h * .17);
  };
  let th = 2.2 * Math.PI, spiral = [];
  while (th < 6.2 * Math.PI) {                         // equal arc-length steps along an Archimedean spiral
    const r = a + b * th, [x, y] = [c + r * Math.cos(th), c + r * Math.sin(th)];
    spiral.push([x, y]); const turn = th < 3.6 * Math.PI ? 's1' : th < 4.9 * Math.PI ? 's2' : 's3';
    figs[turn] += fig(x, y, 24, th * 180 / Math.PI); th += 21 / r;
  }
  const player = fig(c, c + 6, 46, -90) + `M${K.P(c + 8, c - 6)}Q${K.P(c + 34, c - 10)} ${K.P(c + 40, c + 22)}`;
  const inner = K.stack(K.pl(spiral), [{ c: 'var(--m1)', w: 1.4, o: .6 }], 0)
    + K.part('core', K.fill(player, 'var(--m1)') + K.stack(`M${K.P(c + 8, c - 6)}Q${K.P(c + 34, c - 10)} ${K.P(c + 40, c + 22)}`, [{ c: 'var(--m1)', w: 3 }], 0))
    + ['s1', 's2', 's3'].map(s => K.part(s, K.fill(figs[s], 'var(--m1)'))).join('');
  return { w: 400, h: 400, defs: o.badge ? '' : FX.rough('wrough', .05, 2.5), inner: o.badge ? inner : `<g filter="url(#wrough)">${inner}</g>` };
}
