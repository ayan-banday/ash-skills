# Warli · "the tarpa circle"

**Picture it:** white stick-figure dancers, each two triangles and a dot head, spiralling around one musician on a red mud wall.
**Swatch:** `#4A2A21 #F2EDE3 #E6C0AB #DCC9B4 #C7D1DD #A0432B`

**Suits:** community and livelihood programmes, agriculture, NGOs and CSR, Maharashtra-based clients, children's education, rural distribution, people and team proposals. Tone: joyful, communal, humble. Audience: CSR heads, foundations, government programmes, field teams.
**Avoid when:** luxury, finance or hard-sell briefs; there is no Maharashtra or Adivasi link; the client's work touches tribal land rights in a contested way.
**Cultural note:** Warli is the art of the Warli Adivasi community of Palghar and Thane, traditionally painted on hut walls by married women for harvest and weddings; Jivya Soma Mashe took it to paper and to the world. It is heavily copied commercially with little return to the community. Fitting when the project serves or involves the community's own themes (harvest, shared work). Generate abstract figures, never copy a specific painting or the sacred chauk, credit, and commission or license a Warli artist for the hero when budget allows. It becomes appropriation as "tribal" wallpaper for a corporate brand.

**Story device.** The tarpa dance. One musician at the centre is the client's leader or mission; the spiral of dancers holding each other is the team and partners. Each turn of the spiral is a phase; the figures on that turn are the workstreams in it. Sections can also carry small Warli scenes (sowing, harvest) as illustrations.
**Badge:** the spiral with one turn lit (`s1`, `s2`, `s3`), or the musician (`core`).

**SVG recipe**
- **Geometry:** an Archimedean spiral r = 30 + 8.28θ from θ = 2.2π to 6.2π, stepped at equal 21px arc length (dθ = 21/r). Each figure is two triangles meeting at the waist plus a circle head, rotated to face out from the centre. The musician is a 46px figure with a curved tarpa.
- **Stroke stack:** figures are fills (rice paste); the spiral guide is 1.4px at 60%.
- **Texture filter:** rough displacement (frequency .05, scale 2.5) for paste edges; on the section, a low-frequency mud noise at 8% multiply.
- **Draw-on:** the spiral guide draws (1.6s); figures appear in order along the spiral, 18ms apart (opacity plus a 4px outward slide); then the spiral turns once every 90s (paused under reduced motion).
- **Complexity:** 6 paths, 13.7 KB of SVG, 1.06 ms to generate in Node, 1 filter on the hero.

```js
function warli(o = {}) {
  const c = 200, figs = { s1: '', s2: '', s3: '' }, a = 30, b = 52 / (2 * Math.PI);
  const fig = (x, y, h, ang) => {                      // two triangles meeting at the waist + circle head, rotated radially
    const R = (dx, dy) => { const t = (ang + 90) * Math.PI / 180; return [x + dx * Math.cos(t) - dy * Math.sin(t), y + dx * Math.sin(t) + dy * Math.cos(t)]; };
    return K.poly([R(-h * .32, -h * .5), R(h * .32, -h * .5), R(0, 0)]) + K.poly([R(0, 0), R(-h * .3, h * .5), R(h * .3, h * .5)]) + K.circ(...R(0, -h * .72), h * .17);
  };
  let th = 2.2 * Math.PI, spiral = [];
  while (th < 6.2 * Math.PI) {                         // equal arc-length steps along an Archimedean spiral
    const r = a + b * th, [x, y] = [c + r * Math.cos(th), c + r * Math.sin(th)];
    spiral.push([x, y]); const turn = th < 3.6 * Math.PI ? 's1' : th < 4.9 * Math.PI ? 's2' : 's3';
    figs[turn] += fig(x, y, 24, th * 180 / Math.PI); th += 21 / r;
  }
  const player = fig(c, c + 6, 46, -90) + `M${K.P(c + 8, c - 6)}Q${K.P(c + 34, c - 10)} ${K.P(c + 40, c + 22)}`;
  const inner = K.stack(K.pl(spiral), [{ c: 'var(--m1)', w: 1.4, o: .6 }], 0)
    + K.part('core', K.fill(player, 'var(--m1)') + K.stack(`M${K.P(c + 8, c - 6)}Q${K.P(c + 34, c - 10)} ${K.P(c + 40, c + 22)}`, [{ c: 'var(--m1)', w: 3 }], 0))
    + ['s1', 's2', 's3'].map(s => K.part(s, K.fill(figs[s], 'var(--m1)'))).join('');
  return { w: 400, h: 400, defs: o.badge ? '' : FX.rough('wrough', .05, 2.5), inner: o.badge ? inner : `<g filter="url(#wrough)">${inner}</g>` };
}
```

**Hero slots:** `--bgc` ground · `--m1` paper · `--m2` ground-2 · `--m3` card · `--f1` accent-1 · `--f2` accent-2 · `--f3` marker

**Palette:**
```
--ground   #4A2A21               geru-wall
--ground-2 #5B3529               geru-wall-2
--paper    #F2EDE3               rice-paste
--card     #FAF7F1               lime-wash
--ink      #2A1D17               soot
--muted    #6F6057               mud
--line     rgba(42,29,23,.14)    line
--tint-1   #E6C0AB               geru-wash   OKLCH L 0.83 C 0.052 h 51
--tint-2   #DCC9B4               mud-plaster   OKLCH L 0.85 C 0.036 h 70
--tint-3   #C7D1DD               monsoon-sky   OKLCH L 0.86 C 0.020 h 253
--marker   #EDC55B               paddy
--accent-1 #A0432B               geru
--accent-2 #5E3A5A               jamun
```
**Contrast:** ink/paper **13.99** · ink/card 15.26 · ink/tint-1 9.71 · ink/tint-2 10.15 · ink/tint-3 10.57 · muted/paper **5.16** · paper/ground **10.95** · paper/ground-2 9.06 · ink/marker 9.90 · accent-1/paper 5.40 · accent-2/paper 8.08. All body-text pairs pass 4.5:1.

**Type:** display **Tiro Devanagari Marathi**, body **Hind**, labels **DM Mono**, hand **Kalam**.
**Texture:** mud-wall noise on ground sections; rough edges on all figures; paper grain on paper.
**Motion:** rhythmic and gentle. Ease-out entries, one slow ambient rotation.
**Reference:** [Sarmaya, "A Return to the Land: A History of Warli Paintings"](https://sarmaya.in/spotlight/a-return-to-the-land-a-history-of-warli-paintings/): wall paintings by married women, Mashe's move to paper.

---
