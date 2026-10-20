# Herbarium · "the specimen plate"

**Picture it:** a pressed plant in fine sepia line on cream mount board, one hand-tinted flower, numbered detail circles and a label slip.
**Swatch:** `#33261F #F2EDE2 #EBC8C6 #EEDCA4 #D2CBE0 #9C2C44`

**Suits:** agriculture, food, pharma and life sciences, ayurveda and wellness, beauty, research partnerships, universities, environment work. Tone: scholarly, careful, natural. Audience: researchers, regulators, premium consumers, farmer organisations (with simple copy).
**Avoid when:** a speed or tech brand; a client who expects green foliage (Ash rejects green, so leaves stay sepia line).
**Cultural note:** the European botanical plate tradition (Curtis's Botanical Magazine from 1787) grew partly from colonial plant collecting, including Indian plants. For Indian clients, avoid colonial framing ("discovered"); Indian Company-school botanical painting is a respectful cousin worth crediting.

**Story device.** The plant is the organisation: the root is its history, the stem is the client's core, each branch is an initiative, the flower is the outcome, and the numbered details (1., 2., 3.) are close-ups for the deep-dive sections. The label slip carries the proposal's facts.
**Badge:** one branch (`b1` to `b4`; `initiatives` lights all), the flower, or a numbered detail (`f1` to `f3`).

**SVG recipe**
- **Geometry:** a stem polyline with five nodes; alternating branches as quadratic curves to seeded endpoints; each leaf is a lens with a midrib and three vein pairs; a five-petal flower; detail circles r26 in the right margin.
- **Stroke stack:** sepia lines only, 0.9 to 1.6px.
- **Hand tint:** the flower's fill is offset (2.5, 1.5) from its outline and passed through a wash filter (displacement 4, blur 0.7), like off-register watercolour.
- **Texture:** foxing (6 to 10 random brown dots, r1 to r4, at 6%); laid-paper lines (1px every 3px at 2%).
- **Draw-on:** the stem grows (2s ease-out), branches unfold 600ms each with 180ms stagger, the tint washes in (900ms opacity), details last.
- **Complexity:** 15 paths, 5.2 KB of SVG, 0.14 ms to generate in Node, 1 filter on the hero.

```js
function herbarium(o = {}) {
  const r = K.rng(o.seed || 21), stem = [[200, 372], [196, 300], [204, 230], [198, 160], [200, 104]];
  const leaf = (x, y, ang, len) => { const tip = K.pt(x, y, len, ang), l = K.pt(x, y, len * .55, ang - 22), rr = K.pt(x, y, len * .55, ang + 22);
    let d = `M${K.P(x, y)}Q${K.P(l[0], l[1])} ${K.P(tip[0], tip[1])}Q${K.P(rr[0], rr[1])} ${K.P(x, y)}Z` + K.seg([x, y], tip);
    for (let t = .25; t < .8; t += .18) { const b = K.pt(x, y, len * t, ang), e1 = K.pt(b[0], b[1], len * .18, ang - 40), e2 = K.pt(b[0], b[1], len * .18, ang + 40);
      d += K.seg(b, e1) + K.seg(b, e2); } return d; };
  let parts = '';
  for (let i = 0; i < 4; i++) { const [x, y] = stem[i + 0].map((v, k) => (v + stem[i + 1][k]) / 2), side = i % 2 ? 1 : -1, ang = side > 0 ? -25 - r() * 20 : -155 + r() * 20;
    const end = K.pt(x, y, 58 + r() * 20, ang);
    parts += K.part('b' + (i + 1), K.stack(`M${K.P(x, y)}Q${K.P((x + end[0]) / 2, y - 10)} ${K.P(end[0], end[1])}` + leaf(end[0], end[1], ang + side * 10, 46), [{ c: 'var(--m1)', w: 1.1 }], 2 + i), 'data-group="initiatives"'); }
  let petals = '', pl = ''; for (let k = 0; k < 5; k++) { const a = k * 72 - 90, t = K.pt(200, 76, 34, a), l = K.pt(200, 76, 22, a - 30), rr = K.pt(200, 76, 22, a + 30);
    const d = `M200 76Q${K.P(l[0], l[1])} ${K.P(t[0], t[1])}Q${K.P(rr[0], rr[1])} 200 76Z`; petals += d; }
  const tint = o.badge ? K.fill(petals, 'var(--f1)') : `<g transform="translate(2.5 1.5)" filter="url(#wash)">${K.fill(petals, 'var(--f1)', 'opacity=".85"')}</g>`; // hand colour, off-register
  const figs = [0, 1, 2].map(i => K.part('f' + (i + 1), K.stack(K.circ(340, 120 + i * 80, 26), [{ c: 'var(--m1)', w: .9 }], 7) + `<text x="306" y="${100 + i * 80}" style="font:italic 12px var(--font-display);fill:var(--m1)">${i + 1}.</text>`
    + K.stack(i === 0 ? `M340 104Q352 120 340 136Q328 120 340 104Z` : i === 1 ? K.circ(340, 200, 7) + K.circ(340, 200, 2) : 'M326 290L354 270M330 294L358 274', [{ c: 'var(--m1)', w: .9 }], 7), 'data-group="detail"')).join('');
  const inner = K.part('core', K.stack(`M${stem.map(p => K.P(...p)).join('L')}` + 'M200 372l-14 16M200 372l10 18M200 372l-2 20', [{ c: 'var(--m1)', w: 1.6 }], 0)) + parts
    + K.part('flower', tint + K.stack(petals + K.circ(200, 76, 5), [{ c: 'var(--m1)', w: 1.1 }], 6)) + figs
    + K.stack('M24 330H140V384H24Z', [{ c: 'var(--m1)', w: .8 }], 8) + K.fill('M150 380l26 -10l4 10l-26 10z', 'var(--f2)', 'opacity=".7"');
  return { w: 400, h: 400, defs: FX.wash('wash'), inner };
}
```

**Hero slots:** `--bgc` paper · `--m1` ink · `--m2` line · `--m3` card · `--f1` accent-1 · `--f2` marker · `--f3` tint-3

**Palette:**
```
--ground   #33261F               walnut-ink
--ground-2 #42332A               walnut-2
--paper    #F2EDE2               mount-board
--card     #FAF7EF               label
--ink      #2A1F19               sepia
--muted    #6E6157               faded-sepia
--line     rgba(42,31,25,.14)    line
--tint-1   #EBC8C6               rose-madder-wash   OKLCH L 0.86 C 0.040 h 22
--tint-2   #EEDCA4               gamboge-wash   OKLCH L 0.90 C 0.075 h 92
--tint-3   #D2CBE0               iris-wash   OKLCH L 0.85 C 0.030 h 301
--marker   #EDC24C               gamboge
--accent-1 #9C2C44               madder-lake
--accent-2 #5A4A8C               iris
```
**Contrast:** ink/paper **13.75** · ink/card 14.99 · ink/tint-1 10.40 · ink/tint-2 11.78 · ink/tint-3 10.21 · muted/paper **5.12** · paper/ground **12.51** · paper/ground-2 10.35 · ink/marker 9.49 · accent-1/paper 6.30 · accent-2/paper 6.44. All body-text pairs pass 4.5:1.

**Type:** display **Cormorant Garamond**, body **Literata**, labels **Courier Prime**, hand **Homemade Apple** (for the collector's label).
**Texture:** foxing and laid lines on paper; wash on tints.
**Motion:** slow, organic, unhurried. Growth easing (ease-out).
**Reference:** [University of Glasgow Archives & Special Collections, Curtis's Botanical Magazine](https://www.gla.ac.uk/myglasgow/archivespecialcollections/digitisedcollections/birdsbeesandblooms/blooms/curtissbotanicalmagazine/): founded 1787, plates hand-coloured until 1948.

---
