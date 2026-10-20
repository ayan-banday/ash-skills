# Drafting · "the engineering drawing"

**Picture it:** a pencil engineering drawing of a wheel hub on pale vellum: front view, a hatched side section, dimension arrows and a title block.
**Swatch:** `#2B2927 #F0EDE5 #C6D3E2 #EDE0B8 #EBC6C0 #B3322E`

**Suits:** automotive and two-wheelers (TVS-type clients), manufacturing, infrastructure, engineering services, hardware startups, R&D partnerships, technical universities. Tone: precise, honest, transparent. Audience: engineers, plant heads, CTOs.
**Avoid when:** emotional consumer storytelling. Never switch to a blueprint (navy) ground: Ash rejected the navy night hero, so this stays vellum and graphite.
**Cultural note:** technical drawing convention (ISO line types). No concern.

**Story device.** The title block holds the proposal's facts (client, date, scale, revision). The views are the needs seen from different sides; the hatched section is the deep dive; dimension lines are the targets (swap ø188 for "₹2.4 Cr" or "40% faster").
**Badge:** one view in heavy line: rim (`s1`), side section (`s2`), dimensions (`s3`), hub (`core`), title block (`facts`).

**SVG recipe**
- **Geometry:** rim circles r94 and r80; hub r24 and r10; six bolt holes on r52; a side view 40×188 with hidden bore lines; 45-degree hatching clipped to the section; a dimension line with SVG markers (`orient="auto-start-reverse"`); a title-block grid.
- **Stroke stack (ISO weights):** visible 1.8px, hidden 1px dashed 6 4, centre 0.7px dashed 16 4 3 4, dimension 0.7px.
- **Texture filter:** graphite (rough, frequency .9, scale .8) for pencil tooth; a vellum overlay (fractalNoise .8 at 4%); a few eraser smudges (blurred blobs at 3%).
- **Draw-on:** plotter-like: centre lines fast (400ms), then object lines at constant speed (linear), then dimensions, title block last; 90ms stagger. Dashed lines fade in.
- **Complexity:** 10 paths, 3.1 KB of SVG, 0.06 ms to generate in Node, 1 filter on the hero.

```js
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
```

**Hero slots:** `--bgc` paper · `--m1` ink · `--m2` line · `--m3` card · `--f1` accent-1 · `--f2` accent-2 · `--f3` marker

**Palette:**
```
--ground   #2B2927               graphite
--ground-2 #393633               graphite-2
--paper    #F0EDE5               vellum
--card     #F9F8F4               drafting-film
--ink      #22201E               lead
--muted    #64605B               hb
--line     rgba(34,32,30,.14)    line
--tint-1   #C6D3E2               cyanotype-wash   OKLCH L 0.86 C 0.025 h 252
--tint-2   #EDE0B8               trace-yellow   OKLCH L 0.91 C 0.054 h 92
--tint-3   #EBC6C0               redline-wash   OKLCH L 0.86 C 0.043 h 29
--marker   #F4D54E               highlighter
--accent-1 #B3322E               redline
--accent-2 #23508E               cyanotype
```
**Contrast:** ink/paper **13.88** · ink/card 15.28 · ink/tint-1 10.68 · ink/tint-2 12.34 · ink/tint-3 10.34 · muted/paper **5.33** · paper/ground **12.39** · paper/ground-2 10.26 · ink/marker 11.19 · accent-1/paper 5.26 · accent-2/paper 6.88. All body-text pairs pass 4.5:1.

**Type:** display **Barlow Condensed**, body **IBM Plex Sans**, labels **IBM Plex Mono**, hand **Architects Daughter** (for redline notes).
**Texture:** vellum and graphite as above.
**Motion:** linear, mechanical, methodical.
**Reference:** [Science Museum Group YA1995.128/PL/1/048, "Drawing of steam chest"](https://collection.sciencemuseumgroup.org.uk/documents/aa110141987/drawing-of-steam-chest): an engineering drawing at 1:2 with draughtsman's initials.

---
