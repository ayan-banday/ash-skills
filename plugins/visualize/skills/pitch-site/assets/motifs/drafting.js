/* Drafting · "the engineering drawing": motif generator. Needs kit.js (K, FX). */
function drafting(o = {}) {
  const c = [150, 150], vis = [{ c: 'var(--m1)', w: 1.8 }], thin = [{ c: 'var(--m1)', w: .7 }];
  let bolts = ''; for (let k = 0; k < 6; k++) bolts += K.circ(...K.pt(c[0], c[1], 52, k * 60), 6);
  const cl = [{ c: 'var(--m1)', w: .7, dash: '16 4 3 4' }], hid = [{ c: 'var(--m1)', w: 1, dash: '6 4' }];
  let hatch = ''; for (let x = 100; x < 334; x += 7) hatch += `M${x} 244L${x + 188} 56`;            // 45deg section hatch
  let tb = 'M210 318H390V388H210ZM210 341H390M210 364H390M300 318V388';
  const inner = K.stack(`M${c[0] - 115} ${c[1]}H${c[0] + 115}M${c[0]} ${c[1] - 115}V${c[1] + 115}M260 ${c[1]}H360`, cl, 0)
    + K.part('s1', K.stack(K.circ(...c, 94) + K.circ(...c, 80), vis, 1))
    + K.part('core', K.stack(K.circ(...c, 24) + K.circ(...c, 10) + bolts, vis, 2))
    + K.part('s2', `<g clip-path="url(#hclip)">${K.stack(hatch, thin, 3)}</g>` + K.stack('M290 56H330V244H290Z', vis, 3) + K.stack('M290 140H330M290 160H330', hid, 3))
    + K.part('s3', K.stack(`M${c[0] - 94} 268H${c[0] + 94}M${c[0] - 94} 258V276M${c[0] + 94} 258V276`, thin, 4).replace(/stroke-linejoin="round"\/>$/, 'stroke-linejoin="round" marker-start="url(#arr)" marker-end="url(#arr)"/>')
      + `<text x="${c[0]}" y="262" text-anchor="middle" style="font:11px var(--font-label);fill:var(--m1)">&#8960; 188</text>`)
    + K.part('tb', K.stack(tb, vis, 5), 'data-group="facts"');
  return { w: 400, h: 400, defs: `<marker id="arr" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 2L10 5L0 8Z" style="fill:var(--m1)"/></marker><clipPath id="hclip"><path d="M290 56H330V140H290ZM290 160H330V244H290Z"/></clipPath>` + (o.badge ? '' : FX.rough('graphite', .9, .8)), inner: o.badge ? inner : `<g filter="url(#graphite)">${inner}</g>` };
}
