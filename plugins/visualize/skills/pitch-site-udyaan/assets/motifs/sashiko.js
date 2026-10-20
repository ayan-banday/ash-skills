/* Sashiko · "the mending stitch": motif generator. Needs kit.js (K, FX). */
function sashiko(o = {}) {
  const txt = (o.text || 'TVS x JAIN University').replace(/\s/g, ''), N = 16, s = 22, m = 24;
  const bits = (t, k) => [...Array(N + 1)].map((_, i) => (t.charCodeAt(i % t.length) + (k ? i : 0)) % 2);
  const br = bits(txt, 0), bc = bits([...txt].reverse().join(''), 1);
  let st = '';
  for (let i = 0; i <= N; i++) for (let j = br[i]; j < N; j += 2) st += `M${m + j * s + 3} ${m + i * s}H${m + (j + 1) * s - 3}`;
  for (let j = 0; j <= N; j++) for (let i = bc[j]; i < N; i += 2) st += `M${m + j * s} ${m + i * s + 3}V${m + (i + 1) * s - 3}`;
  const patch = (x, y, w, h, col) => K.fill(`M${m + x * s} ${m + y * s}h${w * s}v${h * s}h${-w * s}z`, col);
  const inner = K.part('core', patch(6, 6, 4, 4, 'var(--f1)')) + K.part('s1', patch(1, 2, 4, 3, 'var(--f2)')) + K.part('s2', patch(11, 3, 4, 4, 'var(--f3)')) + K.part('s3', patch(3, 11, 6, 4, 'var(--f2)'))
    + `<g class="stitch">${K.stack(st, o.badge ? [{ c: 'var(--m1)', w: 2.4 }] : [{ c: 'var(--m2)', w: 2.4, o: .35, t: '.6 .9' }, { c: 'var(--m1)', w: 2.2 }], 0)}</g>`;
  return { w: N * s + 2 * m, h: N * s + 2 * m, defs: '', inner };
}
