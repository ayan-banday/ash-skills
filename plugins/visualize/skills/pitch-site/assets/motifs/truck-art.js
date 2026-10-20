/* Truck art · "the tailgate": motif generator. Needs kit.js (K, FX). */
function truckart(o = {}) {
  const c = 200; let scal = '', dia = '', chain = '', petals = '';
  for (let x = 20; x < 380; x += 20) scal += `M${x} 20A10 10 0 0 0 ${x + 20} 20`;
  for (let i = 0; i < 14; i++) { const x = 32 + i * 24.5; dia += K.fill(K.poly([[x, 312], [x + 12, 300], [x + 24, 312], [x + 12, 324]]), i % 2 ? 'var(--f1)' : 'var(--f2)'); }
  for (let k = 0; k < 12; k++) { const t = K.pt(c, 150, 62, k * 30 - 90), l = K.pt(c, 150, 30, k * 30 - 108), r = K.pt(c, 150, 30, k * 30 - 72);
    petals += `M${K.P(c, 150)}Q${K.P(l[0], l[1])} ${K.P(t[0], t[1])}Q${K.P(r[0], r[1])} ${K.P(c, 150)}Z`; }
  const arch = 'M50 290V150Q50 70 200 34Q350 70 350 150V290Z';
  const plates = [0, 1, 2].map(i => K.part('s' + (i + 1), K.fill(`M${62 + i * 94} 236h88v40h-88z`, 'var(--f3)') + K.stack(`M${62 + i * 94} 236h88v40h-88z`, [{ c: 'var(--m1)', w: 2.5 }], 2 + i)
    + (o.labels ? `<text x="${106 + i * 94}" y="262" text-anchor="middle" style="font:700 13px var(--font-label);fill:var(--m1)">${o.labels[i]}</text>` : ''))).join('');
  for (let i = 0; i < 8; i++) chain += K.part('m' + (i + 1), K.stack(K.circ(46 + i * 44, 352, 9), [{ c: 'var(--m1)', w: 3 }], 6) + K.stack(`M${55 + i * 44} 352H${81 + i * 44}`, [{ c: 'var(--m1)', w: 2 }], 6), 'data-group="timeline"');
  const inner = K.fill('M10 10H390V390H10Z', 'var(--bgc)') + K.stack(scal, [{ c: 'var(--f1)', w: 5 }], 0) + K.fill(arch, 'var(--f2)') + K.stack(arch, [{ c: 'var(--m1)', w: 3 }, { c: 'var(--m3)', w: 1, o: .6, t: '-1.5 -1.5' }], 1)
    + K.part('core', K.fill(petals, 'var(--f1)') + K.stack(petals, [{ c: 'var(--m1)', w: 2 }], 2) + K.fill(K.circ(c, 150, 16), 'var(--f3)') + K.stack(K.circ(c, 150, 16), [{ c: 'var(--m1)', w: 2 }], 2))
    + plates + dia + chain;
  return { w: 400, h: 400, defs: '', inner };
}
