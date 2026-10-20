/* Kolam · "threshold" (proven: JAIN University to TVS): motif generator. Needs kit.js (K, FX). */
function kolam(o = {}) {
  const c = 200, inner = [], L = o.badge ? [{ c: 'var(--m1)', w: 7 }] : [{ c: 'var(--m1)', w: 6, o: .35 }, { c: 'var(--m1)', w: 2.8 }];
  let dots = ''; for (let i = -4; i <= 4; i++) for (let j = -4; j <= 4; j++) dots += K.circ(c + i * 40, c + j * 40, 2.2);
  if (!o.badge) inner.push(K.fill(dots, 'var(--m2)'));
  const v = [...Array(6)].map((_, k) => K.pt(c, c, 46, -90 + k * 60));            // hexagon -> cube of 3 rhombi
  let core = [0, 2, 4].map(k => K.poly([[c, c], v[k], v[(k + 1) % 6], v[(k + 2) % 6]])).join('');
  [1, 3, 5].forEach(k => { const a = -90 + k * 60, cc = K.pt(c, c, 55, a), e = K.pt(cc[0], cc[1], 9, a + 180 + 300);
    core += `M${K.P(v[k][0], v[k][1])}A9 9 0 1 1 ${K.P(e[0], e[1])}`; });                // curl at each outer tip
  for (let k = 0; k < 3; k++) {                                                      // 3 triple-strand bands at 120deg
    const ell = (rx, ry) => `M${-rx} 0a${rx} ${ry} 0 1 0 ${2 * rx} 0a${rx} ${ry} 0 1 0 ${-2 * rx} 0`;
    const strands = [-9, 0, 9].map(dv => ell(84 + dv, 30 + dv)).join('');
    const half = [-9, 0, 9].map(dv => `M0 ${-(30 + dv)}A${84 + dv} ${30 + dv} 0 0 1 0 ${30 + dv}`).join('');
    const g = `translate(${c} ${c}) rotate(${k * 120 - 90}) translate(92 0)`;
    inner.push(K.part('s' + (k + 1), `<g transform="${g}">${K.stack(strands, [{ c: 'var(--bgc)', w: 26, o: .9 }, ...L], 1 + k)}</g>`));
    inner.push(`<g class="part" data-part="s${k + 1}" transform="${g}">${K.stack(half, [{ c: 'var(--bgc)', w: 26 }, ...L], 1 + k)}</g>`); // re-draw half on top = over/under
  }
  inner.push(K.part('core', K.fill(K.circ(c, c, 54), 'var(--bgc)') + K.stack(core, L, 0)));   // centre sits on top of the loops
  for (let k = 0; k < 6; k++) {                                                      // six petal flowers = design
    const [x, y] = K.pt(c, c, 168, k * 60); let fl = '';
    for (let p = 0; p < 6; p++) { const a = p * 60, t = K.pt(x, y, 17, a), l = K.pt(x, y, 9, a - 28), r = K.pt(x, y, 9, a + 28);
      fl += `M${K.P(x, y)}Q${K.P(l[0], l[1])} ${K.P(t[0], t[1])}Q${K.P(r[0], r[1])} ${K.P(x, y)}`; }
    inner.push(K.part('p' + (k + 1), K.stack(fl, L, 4), 'data-group="design"'));
  }
  const body = o.badge ? inner.join('') : `<g filter="url(#powder)">${inner.join('')}</g>`;
  return { w: 400, h: 400, defs: o.badge ? '' : FX.powder(), inner: body };
}
