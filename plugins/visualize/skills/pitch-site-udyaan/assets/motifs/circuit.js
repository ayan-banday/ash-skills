/* Circuit · "copper on Kapton": motif generator. Needs kit.js (K, FX). */
function circuit(o = {}) {
  const c = 200, cu = o.badge ? [{ c: 'var(--m1)', w: 3 }] : [{ c: 'var(--m2)', w: 6 }, { c: 'var(--m1)', w: 3.6 }, { c: 'var(--m3)', w: 1, o: .5 }];
  const groups = { s1: '', s2: '', s3: '', s4: '' }, pads = { s1: '', s2: '', s3: '', s4: '' }; let pins = '';
  for (let side = 0; side < 4; side++) for (let i = 0; i < 4; i++) {
    const off = -27 + i * 18, rot = side * 90, R = (x, y) => { const a = rot * Math.PI / 180; return [c + x * Math.cos(a) - y * Math.sin(a), c + x * Math.sin(a) + y * Math.cos(a)]; };
    const p0 = R(off, -50), p1 = R(off, -70), p2 = R(off + (off < 0 ? -1 : 1) * (40 + Math.abs(off)), -110 - Math.abs(off)), p3 = R(off + (off < 0 ? -1 : 1) * (40 + Math.abs(off)), -150);
    pins += K.fill(`M${K.P(...R(off - 4, -50))}L${K.P(...R(off + 4, -50))}L${K.P(...R(off + 4, -38))}L${K.P(...R(off - 4, -38))}Z`, 'var(--m3)');
    groups['s' + (side + 1)] += K.pl([p0, p1, p2, p3]); pads['s' + (side + 1)] += K.circ(...p3, 7) + K.circ(...p2, 3.5);
  }
  const inner = K.fill(`M0 0H400V400H0Z`, 'var(--bgc)')
    + Object.keys(groups).map((s, i) => K.part(s, K.stack(groups[s], cu, i) + K.fill(pads[s], 'var(--f1)') + K.stack(pads[s], [{ c: 'var(--m1)', w: 2 }], i))).join('')
    + K.part('core', K.fill('M150 150H250V250H150Z', 'var(--m2)') + pins + K.fill(K.circ(162, 162, 4), 'var(--m3)') + `<text x="200" y="205" text-anchor="middle" style="font:12px var(--font-label);fill:var(--m3)">U1</text>`);
  return { w: 400, h: 400, defs: '', inner };
}
