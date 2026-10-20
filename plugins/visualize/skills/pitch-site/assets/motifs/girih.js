/* Girih · "the ten-fold star": motif generator. Needs kit.js (K, FX). */
function girih(o = {}) {
  const c = 200, v = [...Array(10)].map((_, k) => K.pt(c, c, 70, k * 36 - 90));
  const star = v.map((p, k) => K.seg(p, v[(k + 3) % 10])).join('');
  const kites = [...Array(10)].map((_, k) => K.poly([K.pt(c, c, 70, k * 36 - 90), K.pt(c, c, 108, k * 36 - 108), K.pt(c, c, 132, k * 36 - 90), K.pt(c, c, 108, k * 36 - 72)]));
  const st5 = (x, y, R) => K.poly([...Array(10)].map((_, k) => K.pt(x, y, k % 2 ? R * .45 : R, k * 36 - 90)));
  const outer = [...Array(10)].map((_, k) => st5(...K.pt(c, c, 162, k * 36 - 72), 20)).join('');
  const strap = o.badge ? [{ c: 'var(--m1)', w: 4 }] : [{ c: 'var(--m1)', w: 7 }, { c: 'var(--bgc)', w: 3.4 }];
  const guides = o.badge ? '' : K.stack(K.circ(c, c, 70) + K.circ(c, c, 132) + K.circ(c, c, 162), [{ c: 'var(--m1)', w: .6, o: .3, dash: '3 5' }], 0);
  const inner = guides + kites.map((d, k) => K.part('p' + (k + 1), K.fill(d, k % 2 ? 'var(--f1)' : 'var(--f2)') + K.stack(d, strap, 2), 'data-group="principles"')).join('')
    + K.part('core', K.stack(star, strap, 1)) + K.part('s1', K.fill(outer, 'var(--f3)') + K.stack(outer, strap, 3));
  return { w: 400, h: 400, defs: '', inner };
}
