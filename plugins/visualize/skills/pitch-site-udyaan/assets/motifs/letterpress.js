/* Letterpress · "the front page": motif generator. Needs kit.js (K, FX). */
function letterpress(o = {}) {
  const bars = (x, y, w, n, lh = 9) => { let d = ''; for (let i = 0; i < n; i++) d += `M${x} ${y + i * lh}h${i === n - 1 ? w * .6 : w}v3.2h${-(i === n - 1 ? w * .6 : w)}z`; return d; };
  const head = o.title ? `<text x="200" y="74" text-anchor="middle" style="font:44px var(--font-display);fill:var(--m1)">${o.title}</text>` : K.fill('M60 46H340V80H60Z', 'var(--m1)');
  const inner = K.fill('M20 20H380V26H20ZM20 30H380V31.5H20Z', 'var(--m1)') + K.part('core', head + K.fill('M90 92H310V100H90Z', 'var(--m1)', 'opacity=".55"'))
    + K.fill('M20 112H380V113.5H20ZM20 116H380V120H20Z', 'var(--m1)')
    + [0, 1, 2].map(i => K.part('s' + (i + 1), K.fill(`M${24 + i * 120} 134h108v18h-108z`, 'var(--m1)') + K.fill(bars(24 + i * 120, 164, 108, 18), 'var(--m1)', 'opacity=".55"'))).join('')
    + K.fill('M138 134h1v240h-1zM258 134h1v240h-1z', 'var(--m1)')
    + K.part('box', K.stack('M150 300h100v74h-100z', [{ c: 'var(--m1)', w: 3 }], 0) + K.stack('M156 306h88v62h-88z', [{ c: 'var(--m1)', w: 1 }], 0) + `<text x="200" y="346" text-anchor="middle" style="font:22px var(--font-display);fill:var(--f1)">&#9758;</text>`, 'data-group="ask"');
  return { w: 400, h: 400, defs: o.badge ? '' : FX.squeeze('press') + FX.speckle('nspk', 1.4, 8), inner: o.badge ? inner : `<g filter="url(#nspk)"><g filter="url(#press)">${inner}</g></g>` };
}
