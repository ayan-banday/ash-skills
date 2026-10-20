/* Patola · "the double ikat": motif generator. Needs kit.js (K, FX). */
function patola(o = {}) {
  const r = K.rng(o.seed || 5), u = 7, J = () => o.badge ? 0 : (r() - .5) * u * .9;   // J = thread-bundle feathering
  const diamond = (cx, cy, n, col) => { let d = '';
    for (let j = -n; j <= n; j++) { const w = (n - Math.abs(j) + .5) * u, x0 = cx - w + J(), x1 = cx + w + J();
      d += `M${K.f(x0)} ${cy + j * u - u / 2}H${K.f(x1)}V${cy + j * u + u / 2}H${K.f(x0)}Z`; }
    return K.fill(d, col); };
  const cell = (cx, cy) => diamond(cx, cy, 9, 'var(--f1)') + diamond(cx, cy, 6, 'var(--f2)') + diamond(cx, cy, 3, 'var(--f3)') + diamond(cx, cy, 1, 'var(--m3)');
  const rows = { s1: '', s2: '', s3: '' }, ids = ['s1', 's2', 's3']; let core = '';
  for (let ri = 0; ri < 5; ri++) for (let x = ri % 2 ? 5 : 70; x <= 400; x += 130) {      // diamond lattice: rows 65 apart, staggered
    const y = 70 + ri * 65, key = ri < 2 ? 's1' : ri === 2 ? 's2' : 's3';
    if (ri === 2 && x === 200) core += cell(x, y); else rows[key] += cell(x, y); }
  const blur = o.badge ? '' : ' filter="url(#ikat)"';
  const inner = K.fill('M0 0H400V400H0Z', 'var(--bgc)') + ids.map(s => K.part(s, `<g${blur}>${rows[s]}</g>`)).join('') + K.part('core', `<g${blur}>${core}</g>`);
  return { w: 400, h: 400, defs: FX.hblur('ikat', 1.3), inner };
}
