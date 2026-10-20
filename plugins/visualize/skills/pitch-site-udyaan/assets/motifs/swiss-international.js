/* Swiss International · "the grid and the rings": motif generator. Needs kit.js (K, FX). */
function swiss(o = {}) {
  let grid = ''; for (let x = 0; x <= 400; x += 400 / 6) grid += `M${K.f(x)} 0V400M0 ${K.f(x)}H400`;
  const ring = (r, w) => K.stack(K.circ(130, 270, r), [{ c: 'var(--m1)', w }], Math.round(r / 30));
  const grp = (a, b) => { let d = ''; for (let r = a; r <= b; r += 30) d += ring(r, r % 90 === 0 ? 7 : 2.2); return d; };
  const inner = (o.badge ? '' : K.stack(grid, [{ c: 'var(--m2)', w: .6 }], 0))
    + `<g clip-path="url(#swclip)">${K.fill('M130 270V-200A470 470 0 0 1 600 270Z', 'var(--f1)')}${K.part('s1', grp(30, 90))}${K.part('s2', grp(120, 180))}${K.part('s3', grp(210, 420))}</g>`
    + K.part('core', K.fill(K.circ(130, 270, 9), 'var(--m1)'));
  return { w: 400, h: 400, defs: '<clipPath id="swclip"><rect width="400" height="400"/></clipPath>', inner };
}
