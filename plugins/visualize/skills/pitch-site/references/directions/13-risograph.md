# Risograph · "the overprint"

**Picture it:** three halftone circles in fluorescent pink, purple and yellow overlapping slightly off-register on recycled paper.
**Swatch:** `#2A2527 #F1EDE3 #F2C6DA #D8CDEA #F4D9A0 #E8459B`

**Suits:** creative agencies, youth and student programmes, events, festivals, culture, community work, newsletters, startups pitching to young audiences. Tone: playful, DIY, energetic. Audience: students, creatives, community.
**Avoid when:** conservative finance, legal or medical briefs; long dense data.
**Cultural note:** Riso Kagaku (Tokyo, 1946) made the Risograph for offices and schools; independent publishers adopted it. No concern.

**Story device.** Drums and overprint. Each ink drum is one party or need (pink = the client, purple = us, yellow = the end users). Where two overlap a new colour appears (pink and yellow make red, purple and yellow make brown, pink and purple make plum): shared work. Where all three overlap is the outcome. Purple replaces Riso's usual blue on purpose: blue printed over yellow makes green.
**Badge:** one circle printed (`s1`, `s2`, `s3`), the others ghosted; `core` is the centre.

**SVG recipe**
- **Geometry:** three circles r98 on a triangle; a halftone `<pattern>` of 7px dots at screen angles 15, 75 and 45 degrees; each layer is a 55% solid plus the halftone; seeded offsets of ±3px for misregistration.
- **Stroke stack:** none.
- **Texture filter:** speckle dropouts (noise threshold) on the whole print; a paper-fibre overlay.
- **Draw-on:** layers drop in like drum passes: translateY -8 to 0 plus opacity, 260ms, `steps(4)` for a mechanical feel, 200ms apart.
- **Complexity:** 7 paths, 1.9 KB of SVG, 0.04 ms to generate in Node, 1 filter on the hero, plus three small patterns. Halftone fills cost more on very large areas.

```js
function riso(o = {}) {
  const r = K.rng(o.seed || 3), off = () => o.badge ? 0 : K.f((r() - .5) * 6);
  const pat = (id, col, ang) => `<pattern id="${id}" width="7" height="7" patternUnits="userSpaceOnUse" patternTransform="rotate(${ang})"><circle cx="3.5" cy="3.5" r="2.6" style="fill:${col}"/></pattern>`;
  const C = [[200, 145], [140, 250], [260, 250]], cols = ['var(--f1)', 'var(--f2)', 'var(--f3)'], ang = [15, 75, 45];
  const inner = C.map(([x, y], i) => K.part('s' + (i + 1), `<g transform="translate(${off()} ${off()})" style="mix-blend-mode:multiply">${K.fill(K.circ(x, y, 98), cols[i], 'opacity=".55"')}${K.fill(K.circ(x, y, 98), `url(#ht${i})`)}</g>`)).join('')
    + K.part('core', K.fill(K.circ(200, 215, 14), 'var(--m1)'));
  return { w: 400, h: 400, defs: C.map((_, i) => pat('ht' + i, cols[i], ang[i])).join('') + (o.badge ? '' : FX.speckle('rspk', 1.2)), inner: o.badge ? inner : `<g filter="url(#rspk)">${inner}</g>` };
}
```

**Hero slots:** `--bgc` paper · `--m1` ink · `--m2` line · `--m3` card · `--f1` accent-1 · `--f2` accent-2 · `--f3` marker

**Palette:**
```
--ground   #2A2527               riso-black
--ground-2 #3A3436               riso-black-2
--paper    #F1EDE3               bond
--card     #F9F7F1               card
--ink      #211D1F               ink
--muted    #665F60               muted
--line     rgba(33,29,31,.14)    line
--tint-1   #F2C6DA               pink-20   OKLCH L 0.87 C 0.056 h 349
--tint-2   #D8CDEA               purple-20   OKLCH L 0.87 C 0.041 h 303
--tint-3   #F4D9A0               sunflower-20   OKLCH L 0.89 C 0.079 h 85
--marker   #F7DC45               riso-yellow
--accent-1 #E8459B               fluoro-pink
--accent-2 #6A4F9E               riso-purple
```
**Contrast:** ink/paper **14.25** · ink/card 15.56 · ink/tint-1 11.00 · ink/tint-2 10.98 · ink/tint-3 12.12 · muted/paper **5.33** · paper/ground **12.90** · paper/ground-2 10.42 · ink/marker 12.12 · accent-1/paper 3.12 · accent-2/paper 5.57. All body-text pairs pass 4.5:1. **accent-1 is display-only** (3.12:1): use it for fills and type at 24px or larger, never body text or links.

**Type:** display **Bricolage Grotesque**, body **Work Sans**, labels **Chivo Mono**, hand **Gochi Hand**.
**Texture:** speckle and fibre everywhere, including tint blocks.
**Motion:** playful and stepped: colour passes arrive one at a time in 3 to 4 `steps()`. The misregistration is fixed in place and never jitters.
**Reference:** [It's Nice That, "The View From Tokyo: the origins and resurgence of Risograph in Japan"](https://www.itsnicethat.com/articles/the-view-from-tokyo-risograph-in-japan-print-graphic-design-261124).

---
