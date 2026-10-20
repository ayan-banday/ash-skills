/* Origami · "one sheet": motif generator. Needs kit.js (K, FX). */
function origami(o = {}) {
  const cols = 6, rows = 7, w = 56, h = 46, z = 16, x0 = 32, y0 = 38, V = (i, j) => [x0 + j * w + (i % 2) * z, y0 + i * h];
  const facets = { s1: '', s2: '', s3: '', core: '' }; let mtn = '', val = '';
  for (let i = 0; i < rows; i++) for (let j = 0; j < cols; j++) {
    const q = K.poly([V(i, j), V(i, j + 1), V(i + 1, j + 1), V(i + 1, j)]), key = (i >= 2 && i <= 4 && j >= 2 && j <= 3) ? 'core' : 's' + (1 + Math.floor(j / 2));
    facets[key] += K.fill(q, (i + j) % 2 ? 'var(--f1)' : 'var(--f2)');
  }
  for (let j = 1; j < cols; j++) { const d = K.pl([...Array(rows + 1)].map((_, i) => V(i, j))); j % 2 ? (mtn += d) : (val += d); }   // zigzag lines alternate M/V
  for (let i = 1; i < rows; i++) for (let j = 0; j < cols; j++) { const d = K.seg(V(i, j), V(i, j + 1)); (i + j) % 2 ? (mtn += d) : (val += d); } // straight-line segments alternate
  const edge = K.poly([...[...Array(rows + 1)].map((_, i) => V(i, cols)), ...[...Array(rows + 1)].map((_, i) => V(rows - i, 0))]);
  const inner = Object.keys(facets).map(k => K.part(k, facets[k])).join('')
    + K.stack(edge, [{ c: 'var(--m1)', w: 1.6 }], 0) + K.stack(mtn, [{ c: 'var(--m1)', w: 1.2, dash: '10 3 2 3' }], 1) + K.stack(val, [{ c: 'var(--m1)', w: 1.2, dash: '6 4' }], 1);
  return { w: 400, h: 400, defs: '', inner };
}
