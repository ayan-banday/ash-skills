# Azulejo · "the pattern tile"

**Picture it:** four cobalt-blue painted tiles that meet to form one flower at their shared corner, on lightly crackled cream glaze.
**Swatch:** `#35262F #F2EFE8 #C4CEE4 #EEDBA6 #E3BEA8 #2A4BA0`

**Suits:** hospitality, travel, food and beverage, real estate, retail, cultural institutions, architecture, Goa, Portugal or Lusophone ties. Tone: sunny, crafted, friendly. Audience: hotel groups, F&B, tourism boards, consumers.
**Avoid when:** a data-heavy or hard-tech brief.
**Cultural note:** Portuguese tin-glazed tiles with Hispano-Moresque roots; pattern tiles are built from repeating modules, and cobalt blue on white dominated the Baroque period. Low appropriation risk. In Goa the tiles carry colonial history: good for hospitality, careful in political or heritage contexts.

**Story device.** The module. One tile alone shows a quarter of a flower; the full flower appears only where four tiles meet, and that shared corner is the client. A 2×2 module is four pillars; 4×4 is the full programme. Section blocks can be tiles themselves.
**Badge:** the module with one tile glazed in colour (`s1` to `s4`) or the centre (`core`).

**SVG recipe**
- **Geometry:** a 180px tile with a quarter rosette (four lens petals) at its origin corner, a quarter ring r84, a corner fleuron and edge half-discs. Compose 2×2 by rotating 180, 270, 90 and 0 degrees around the shared corner, with a 4px grout gap. Repeat with `<pattern>` for backgrounds.
- **Stroke stack:** cobalt fill at 85% under a 1.6px manganese outline.
- **Texture filter:** crackle (turbulence thresholded into thin lines at 9%); a per-tile radial highlight for glaze; for pooling, feMorphology dilate 0.4 on the cobalt.
- **Draw-on:** tiles flip in (rotateY 90 to 0, 450ms, ease-out) in checker order; then the centre medallion pops.
- **Complexity:** 15 paths, 4.5 KB of SVG, 0.07 ms to generate in Node, 1 filter on the hero.

```js
function azulejo(o = {}) {
  const T = 180, g = 4, m = 18;
  let q = '', fl = '', edge = '';
  for (let k = 0; k < 4; k++) { const a = k * 22.5 + 11.25, t = K.pt(0, 0, 74, a), l = K.pt(0, 0, 40, a - 12), r = K.pt(0, 0, 40, a + 12);
    q += `M0 0Q${K.P(l[0], l[1])} ${K.P(t[0], t[1])}Q${K.P(r[0], r[1])} 0 0Z`; }   // quarter rosette at the shared corner
  q += 'M84 0A84 84 0 0 1 0 84'; fl = `M${T} ${T - 40}A40 40 0 0 0 ${T - 40} ${T}L${T} ${T}Z`;
  edge = `M${T / 2 - 22} ${T}A22 22 0 0 1 ${T / 2 + 22} ${T}ZM${T} ${T / 2 - 22}A22 22 0 0 0 ${T} ${T / 2 + 22}Z`;
  const tile = (id, rot, tx, ty) => K.part(id, `<g transform="translate(${tx} ${ty}) rotate(${rot})">${K.fill(`M0 0H${T}V${T}H0Z`, 'var(--m3)')}${K.fill(q + fl + edge, 'var(--f1)', 'opacity=".85"')}${K.stack(q + fl + edge, [{ c: 'var(--m1)', w: 1.6 }], 1)}</g>`);
  const C = m + T + g / 2, inner = K.fill(`M0 0H400V400H0Z`, 'var(--m2)')
    + tile('s1', 180, C - g / 2, C - g / 2) + tile('s2', 270, C + g / 2, C - g / 2) + tile('s3', 90, C - g / 2, C + g / 2) + tile('s4', 0, C + g / 2, C + g / 2)
    + K.part('core', K.fill(K.circ(C, C, 14), 'var(--f2)') + K.stack(K.circ(C, C, 14), [{ c: 'var(--m1)', w: 1.6 }], 2));
  return { w: 400, h: 400, defs: o.badge ? '' : FX.crackle('crk'), inner: o.badge ? inner : `<g filter="url(#crk)">${inner}</g>` };
}
```

**Hero slots:** `--bgc` paper · `--m1` accent-2 · `--m2` card · `--m3` paper · `--f1` accent-1 · `--f2` marker · `--f3` tint-3

**Palette:**
```
--ground   #35262F               manganese
--ground-2 #45333D               manganese-2
--paper    #F2EFE8               glaze
--card     #FBF9F4               faience
--ink      #211C24               ink
--muted    #665E66               muted
--line     rgba(33,28,36,.14)    line
--tint-1   #C4CEE4               cobalt-wash   OKLCH L 0.85 C 0.033 h 266
--tint-2   #EEDBA6               antimony-wash   OKLCH L 0.89 C 0.072 h 91
--tint-3   #E3BEA8               terracotta   OKLCH L 0.83 C 0.052 h 52
--marker   #EEC85A               antimony
--accent-1 #2A4BA0               cobalt
--accent-2 #6B3A5E               manganese-violet
```
**Contrast:** ink/paper **14.56** · ink/card 15.89 · ink/tint-1 10.58 · ink/tint-2 12.19 · ink/tint-3 9.71 · muted/paper **5.45** · paper/ground **12.44** · paper/ground-2 10.19 · ink/marker 10.38 · accent-1/paper 7.00 · accent-2/paper 7.65. All body-text pairs pass 4.5:1.

**Type:** display **Fraunces** (raise the SOFT axis), body **Alegreya Sans**, labels **DM Mono**, no hand.
**Texture:** crackle and glaze highlight on tiles; paper grain on paper.
**Motion:** crisp and ceramic. Short flips, no bounce.
**Reference:** [Museu Nacional do Azulejo, "The Azulejo in Portugal" (Google Arts & Culture)](https://artsandculture.google.com/story/agUB70vTvN7aIg): pattern modules from 2×2 to 12×12, cobalt on white in the Baroque.

---
