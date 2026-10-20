/* Memphis · "the laminate party": motif generator. Needs kit.js (K, FX). */
function memphis(o = {}) {
  const r = K.rng(o.seed || 9), pts = [];
  for (let t = 0; t < 5000 && pts.length < 22; t++) { const p = [20 + r() * 360, 20 + r() * 360]; if (pts.every(q => Math.hypot(q[0] - p[0], q[1] - p[1]) > 46) && Math.hypot(p[0] - 200, p[1] - 200) > 120) pts.push(p); }
  let conf = ''; pts.forEach(([x, y], i) => { const a = r() * 180; conf += i % 3 === 0 ? K.circ(x, y, 4) : i % 3 === 1 ? K.poly([K.pt(x, y, 7, a), K.pt(x, y, 7, a + 120), K.pt(x, y, 7, a + 240)]) : `M${K.P(...K.pt(x, y, 9, a))}L${K.P(...K.pt(x, y, 9, a + 180))}`; });
  let sq = 'M60 300'; for (let x = 60; x <= 340; x += 10) sq += `L${x} ${300 + 16 * Math.sin((x - 60) / 14)}`;
  let grid = ''; for (let k = 0; k <= 80; k += 10) grid += `M250 ${40 + k}H350M${250 + k * 1.25} 40V120`;
  const O = [{ c: 'var(--m1)', w: 4 }], shadow = d => o.badge ? '' : `<g transform="translate(6 6)">${K.fill(d, 'var(--m1)')}</g>`;
  const ci = K.circ(140, 170, 70), tri = K.poly([[230, 290], [330, 290], [280, 200]]);
  const inner = (o.badge ? '' : K.stack(conf, [{ c: 'var(--m1)', w: 3 }], 0))
    + K.part('s4', K.stack(grid, [{ c: 'var(--m1)', w: 1.4 }], 1)) + K.part('s1', shadow(ci) + K.fill(ci, 'var(--f1)') + K.stack(ci, O, 2))
    + K.part('s2', shadow(tri) + K.fill(tri, 'var(--f3)') + K.stack(tri, O, 3)) + K.part('s3', K.stack(sq, [{ c: 'var(--m1)', w: 13 }, { c: 'var(--f2)', w: 8 }], 4))
    + K.part('core', K.fill(K.circ(200, 220, 12), 'var(--m3)') + K.stack(K.circ(200, 220, 12), O, 5));
  return { w: 400, h: 400, defs: '', inner };
}

const GENERATORS = { kolam, ajrakh, warli, madhubani, patola, truckart, kumiko, sashiko, girih, azulejo, bauhaus, swiss, riso, drafting, herbarium, transit, letterpress, circuit, origami, memphis };
