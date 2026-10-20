/* Herbarium · "the specimen plate": motif generator. Needs kit.js (K, FX). */
function herbarium(o = {}) {
  const r = K.rng(o.seed || 21), stem = [[200, 372], [196, 300], [204, 230], [198, 160], [200, 104]];
  const leaf = (x, y, ang, len) => { const tip = K.pt(x, y, len, ang), l = K.pt(x, y, len * .55, ang - 22), rr = K.pt(x, y, len * .55, ang + 22);
    let d = `M${K.P(x, y)}Q${K.P(l[0], l[1])} ${K.P(tip[0], tip[1])}Q${K.P(rr[0], rr[1])} ${K.P(x, y)}Z` + K.seg([x, y], tip);
    for (let t = .25; t < .8; t += .18) { const b = K.pt(x, y, len * t, ang), e1 = K.pt(b[0], b[1], len * .18, ang - 40), e2 = K.pt(b[0], b[1], len * .18, ang + 40);
      d += K.seg(b, e1) + K.seg(b, e2); } return d; };
  let parts = '';
  for (let i = 0; i < 4; i++) { const [x, y] = stem[i + 0].map((v, k) => (v + stem[i + 1][k]) / 2), side = i % 2 ? 1 : -1, ang = side > 0 ? -25 - r() * 20 : -155 + r() * 20;
    const end = K.pt(x, y, 58 + r() * 20, ang);
    parts += K.part('b' + (i + 1), K.stack(`M${K.P(x, y)}Q${K.P((x + end[0]) / 2, y - 10)} ${K.P(end[0], end[1])}` + leaf(end[0], end[1], ang + side * 10, 46), [{ c: 'var(--m1)', w: 1.1 }], 2 + i), 'data-group="initiatives"'); }
  let petals = '', pl = ''; for (let k = 0; k < 5; k++) { const a = k * 72 - 90, t = K.pt(200, 76, 34, a), l = K.pt(200, 76, 22, a - 30), rr = K.pt(200, 76, 22, a + 30);
    const d = `M200 76Q${K.P(l[0], l[1])} ${K.P(t[0], t[1])}Q${K.P(rr[0], rr[1])} 200 76Z`; petals += d; }
  const tint = o.badge ? K.fill(petals, 'var(--f1)') : `<g transform="translate(2.5 1.5)" filter="url(#wash)">${K.fill(petals, 'var(--f1)', 'opacity=".85"')}</g>`; // hand colour, off-register
  const figs = [0, 1, 2].map(i => K.part('f' + (i + 1), K.stack(K.circ(340, 120 + i * 80, 26), [{ c: 'var(--m1)', w: .9 }], 7) + `<text x="306" y="${100 + i * 80}" style="font:italic 12px var(--font-display);fill:var(--m1)">${i + 1}.</text>`
    + K.stack(i === 0 ? `M340 104Q352 120 340 136Q328 120 340 104Z` : i === 1 ? K.circ(340, 200, 7) + K.circ(340, 200, 2) : 'M326 290L354 270M330 294L358 274', [{ c: 'var(--m1)', w: .9 }], 7), 'data-group="detail"')).join('');
  const inner = K.part('core', K.stack(`M${stem.map(p => K.P(...p)).join('L')}` + 'M200 372l-14 16M200 372l10 18M200 372l-2 20', [{ c: 'var(--m1)', w: 1.6 }], 0)) + parts
    + K.part('flower', tint + K.stack(petals + K.circ(200, 76, 5), [{ c: 'var(--m1)', w: 1.1 }], 6)) + figs
    + K.stack('M24 330H140V384H24Z', [{ c: 'var(--m1)', w: .8 }], 8) + K.fill('M150 380l26 -10l4 10l-26 10z', 'var(--f2)', 'opacity=".7"');
  return { w: 400, h: 400, defs: FX.wash('wash'), inner };
}
