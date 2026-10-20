/* Kumiko · "the lattice": motif generator. Needs kit.js (K, FX). */
function kumiko(o = {}) {
  const c = 200, R = 180, n = o.badge ? 2 : 3, parts = { core: '' }, frame = [];
  for (let s = 0; s < 6; s++) {                                     // 6 big triangles, each split into n*n small ones
    parts['s' + (s + 1)] = '';
    const A = [c, c], B = K.pt(c, c, R, s * 60 - 90), C = K.pt(c, c, R, s * 60 - 30);
    const at = (i, j) => [A[0] + (B[0] - A[0]) * i / n + (C[0] - B[0]) * j / n, A[1] + (B[1] - A[1]) * i / n + (C[1] - B[1]) * j / n];
    for (let i = 0; i < n; i++) for (let j = 0; j <= i; j++) {
      const tris = [[at(i, j), at(i + 1, j), at(i + 1, j + 1)]]; if (j < i) tris.push([at(i, j), at(i + 1, j + 1), at(i, j + 1)]);
      tris.forEach(t => { const g = [(t[0][0] + t[1][0] + t[2][0]) / 3, (t[0][1] + t[1][1] + t[2][1]) / 3];
        frame.push(K.poly(t)); const leaf = t.map(v => K.seg(v, g)).join('');
        if (i === 0) parts.core += leaf; else parts['s' + (s + 1)] += leaf; });
    }
  }
  const glow = o.badge ? '' : `<circle cx="${c}" cy="${c}" r="${R}" style="fill:url(#lamp)"/>`;
  const F = o.badge ? [{ c: 'var(--m1)', w: 3 }] : [{ c: 'var(--m2)', w: 4.6 }, { c: 'var(--m1)', w: 3 }, { c: 'var(--m3)', w: .8, o: .5, t: '-.6 -.6' }];
  const I = o.badge ? [{ c: 'var(--m1)', w: 2 }] : [{ c: 'var(--m2)', w: 2.6 }, { c: 'var(--m1)', w: 1.6 }];
  const inner = glow + `<g class="frame">${K.stack(frame.join(''), F, 0)}</g>` + Object.keys(parts).map((p, i) => K.part(p, K.stack(parts[p], I, 1 + i))).join('');
  return { w: 400, h: 400, defs: `<radialGradient id="lamp"><stop offset="0" style="stop-color:var(--f1);stop-opacity:.9"/><stop offset="1" style="stop-color:var(--f1);stop-opacity:0"/></radialGradient>`, inner };
}
