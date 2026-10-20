/* Madhubani · "the double-line frame": motif generator. Needs kit.js (K, FX). */
function madhubani(o = {}) {
  const c = 200, rect = i => `M${i} ${i}H${400 - i}V${400 - i}H${i}Z`;
  let comb = '', zig = '', chain = '';
  for (let t = 18; t < 382; t += 6) comb += `M${t} 12V24M${t} 376V388M12 ${t}H24M376 ${t}H388`;   // band 1: double line + comb hatch
  const zz = (y, flip) => { let d = `M36 ${y}`; for (let x = 36, k = 0; x <= 364; x += 12, k++) d += `L${x} ${k % 2 ? y + (flip ? -10 : 10) : y}`; return d; };
  zig = zz(32, 0) + zz(368, 1);
  zig += zig.replace(/M(\d+\.?\d*) (\d+\.?\d*)|L(\d+\.?\d*) (\d+\.?\d*)/g, (m, a1, b1, a2, b2) => a1 ? `M${b1} ${a1}` : `L${b2} ${a2}`); // transpose for sides
  for (let t = 60; t <= 340; t += 20) [[t, 54], [t, 346], [54, t], [346, t]].forEach(([x, y]) => chain += `M${x - 7} ${y}Q${x} ${y - 6} ${x + 7} ${y}Q${x} ${y + 6} ${x - 7} ${y}Z`);
  let lotus = ''; for (let k = 0; k < 8; k++) { const t = K.pt(c, c, 46, k * 45 - 90), l = K.pt(c, c, 26, k * 45 - 112), r = K.pt(c, c, 26, k * 45 - 68);
    lotus += `M${K.P(c, c)}Q${K.P(l[0], l[1])} ${K.P(t[0], t[1])}Q${K.P(r[0], r[1])} ${K.P(c, c)}Z`; }
  const fish = (sx) => { const g = (x, y) => [c + sx * x, c + y];
    const P = (x, y) => K.P(...g(x, y));
    let d = `M${P(-30, 0)}Q${P(-60, -54)} ${P(-118, -20)}L${P(-138, -40)}L${P(-130, 0)}L${P(-138, 40)}L${P(-118, 20)}Q${P(-60, 54)} ${P(-30, 0)}Z`;
    let sc = ''; for (let x = -100; x <= -55; x += 12) for (let y = -14; y <= 14; y += 14) sc += `M${P(x, y - 6)}Q${P(x + 8, y)} ${P(x, y + 6)}`;
    return { body: d, detail: sc + K.circ(...g(-48, -6), 3.5) }; };
  const L = [{ c: 'var(--m1)', w: 1.6 }], fL = fish(1), fR = fish(-1);
  const inner = K.part('s1', K.stack(rect(12) + rect(24) + comb, L, 0)) + K.part('s2', K.stack(zig, L, 1)) + K.part('s3', K.fill(chain, 'var(--f2)') + K.stack(chain, L, 2))
    + K.part('p1', K.fill(fL.body, 'var(--f2)') + K.stack(fL.body + fL.detail, L, 3), 'data-group="pair"')
    + K.part('p2', K.fill(fR.body, 'var(--f3)') + K.stack(fR.body + fR.detail, L, 3), 'data-group="pair"')
    + K.part('core', K.fill(lotus, 'var(--f1)') + K.stack(lotus + K.circ(c, c, 8), L, 4));
  return { w: 400, h: 400, defs: '', inner };
}
