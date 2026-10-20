/* Transit map · "the network": motif generator. Needs kit.js (K, FX). */
function transit(o = {}) {
  const round = (pts, rr = 16) => { let d = `M${K.P(...pts[0])}`;            // rounded corners at each bend
    for (let i = 1; i < pts.length - 1; i++) { const [a, b, c] = [pts[i - 1], pts[i], pts[i + 1]];
      const u = (p, q) => { const L = Math.hypot(q[0] - p[0], q[1] - p[1]); return [(q[0] - p[0]) / L, (q[1] - p[1]) / L]; };
      const u1 = u(b, a), u2 = u(b, c); d += `L${K.P(b[0] + u1[0] * rr, b[1] + u1[1] * rr)}Q${K.P(...b)} ${K.P(b[0] + u2[0] * rr, b[1] + u2[1] * rr)}`; }
    return d + `L${K.P(...pts[pts.length - 1])}`; };
  const lines = [
    { id: 's1', col: 'var(--f1)', pts: [[20, 120], [100, 120], [180, 200], [260, 200], [320, 260], [380, 260]] },
    { id: 's2', col: 'var(--f2)', pts: [[200, 20], [200, 120], [220, 140], [220, 200], [220, 300], [160, 360], [60, 360]] },
    { id: 's3', col: 'var(--f3)', pts: [[40, 340], [120, 260], [180, 260], [240, 200], [300, 140], [380, 140]] }];
  const ticks = l => { let d = ''; for (let i = 0; i < l.pts.length - 1; i++) { const [a, b] = [l.pts[i], l.pts[i + 1]], mx = (a[0] + b[0]) / 2, my = (a[1] + b[1]) / 2;
    const L = Math.hypot(b[0] - a[0], b[1] - a[1]), nx = -(b[1] - a[1]) / L, ny = (b[0] - a[0]) / L; d += `M${K.P(mx, my)}L${K.P(mx + nx * 9, my + ny * 9)}`; } return d; };
  const inner = lines.map((l, i) => K.part(l.id, K.stack(round(l.pts), [{ c: 'var(--bgc)', w: 14 }, { c: l.col, w: 8 }], i) + K.stack(ticks(l), [{ c: l.col, w: 4, cap: 'butt' }], i))).join('')
    + K.part('core', K.fill(K.circ(220, 200, 13), 'var(--m3)') + K.stack(K.circ(220, 200, 13), [{ c: 'var(--m1)', w: 4 }], 3))
    + K.fill(K.circ(120, 260, 8) + K.circ(300, 140, 8), 'var(--m3)') + K.stack(K.circ(120, 260, 8) + K.circ(300, 140, 8), [{ c: 'var(--m1)', w: 3 }], 3);
  return { w: 400, h: 400, defs: '', inner };
}
