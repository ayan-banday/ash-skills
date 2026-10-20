/* Ajrakh · "the printing table": motif generator. Needs kit.js (K, FX). */
function ajrakh(o = {}) {
  const c = 200, r = K.rng(o.seed || 11), mis = () => o.badge ? '0 0' : `${K.f((r() - .5) * 2.4)} ${K.f((r() - .5) * 2.4)}`;
  const star = (x, y, R) => K.poly([...Array(16)].map((_, k) => K.pt(x, y, k % 2 ? R * .765 : R, k * 22.5 - 90)));
  let teeth = ''; for (let s = 0; s < 4; s++) for (let i = 0; i < 18; i++) {
    const t0 = 28 + i * 19.1, t1 = t0 + 19.1, tm = (t0 + t1) / 2, pts = [[t0, 28], [tm, 14], [t1, 28]];
    teeth += K.poly(pts.map(([x, y]) => { const [X, Y] = [x - c, y - c], a = s * Math.PI / 2; return [c + X * Math.cos(a) - Y * Math.sin(a), c + X * Math.sin(a) + Y * Math.cos(a)]; })); }
  let corners = ''; [[0, 0], [400, 0], [0, 400], [400, 400]].forEach(([x, y]) => corners += star(x, y, 70));
  let petals = ''; for (let k = 0; k < 8; k++) { const t = K.pt(c, c, 52, k * 45), a = K.pt(c, c, 22, k * 45 - 22), b = K.pt(c, c, 22, k * 45 + 22);
    petals += `M${K.P(c, c)}Q${K.P(a[0], a[1])} ${K.P(t[0], t[1])}Q${K.P(b[0], b[1])} ${K.P(c, c)}Z`; }
  let dots = ''; for (let k = 0; k < 24; k++) { const [x, y] = K.pt(c, c, 104, k * 15); dots += K.circ(x, y, 3.2); }
  const pass1 = K.fill(`M28 28H372V372H28Z` + corners + star(c, c, 100), 'var(--f2)', 'fill-rule="evenodd" clip-path="url(#ajclip)"'); // indigo field, stars resisted
  const pass2 = K.fill(star(c, c, 100) + teeth, 'var(--f1)') + K.fill(corners, 'var(--f1)', 'clip-path="url(#ajclip)"');       // madder
  const pass3 = K.stack(star(c, c, 100) + 'M14 14H386V386H14Z M28 28H372V372H28Z' + petals, [{ c: 'var(--m1)', w: 2.4 }], 1)
    + `<g clip-path="url(#ajclip)">${K.stack(corners, [{ c: 'var(--m1)', w: 2.4 }], 1)}</g>`;                                   // kat black outline
  const pass4 = K.fill(dots + K.circ(c, c, 7), 'var(--m3)');                                                  // white resist dots
  const inner = [K.part('p1', `<g transform="translate(${mis()})">${pass1}</g>`, 'data-group="indigo"'),
    K.part('p2', `<g transform="translate(${mis()})">${pass2}</g>`, 'data-group="madder"'),
    K.part('core', `<g transform="translate(${mis()})">${pass3}</g>`),
    K.part('p3', `<g transform="translate(${mis()})">${pass4}</g>`, 'data-group="resist"')].join('');
  return { w: 400, h: 400, defs: `<clipPath id="ajclip"><rect x="28" y="28" width="344" height="344"/></clipPath>` + (o.badge ? '' : FX.speckle('ajspk', .8)),
    inner: o.badge ? inner : `<g filter="url(#ajspk)">${inner}</g>` };
}
