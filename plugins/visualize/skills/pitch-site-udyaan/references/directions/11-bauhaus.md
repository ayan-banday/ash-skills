# Bauhaus · "the three forms"

**Picture it:** a yellow triangle, a red square and a blue circle overlapping on a linen grid, with one black bar and a dot.
**Swatch:** `#2A2624 #F2EEE6 #EFD99A #C3CDE3 #EDC0B6 #C8352B`

**Suits:** design schools, manufacturing, product, architecture, startups that want "function first", education programmes, any client wanting modern but warm. Tone: confident, functional, clear. Audience: broad and international; non-designers get it instantly.
**Avoid when:** the brief is heritage or craft; primary colours would read childish (keep the chalk tints dominant).
**Cultural note:** a design school and movement (Weimar, Dessau and Berlin, 1919 to 1933). No appropriation concern; the risk is cliché, so hold palette discipline.

**Story device.** Three basic forms are the three needs. They overlap, and the form on top is the priority, so the stacking order is the argument. The dot is the client's decision point.
**Badge:** one form solid (`s1` triangle, `s2` square, `s3` circle), the others faint; `core` is the dot.

**SVG recipe**
- **Geometry:** circle r92, square 160, triangle with a 240 base, a 40px grid, a 6px bar.
- **Stroke stack:** flat fills, each with a 3px background-coloured outline so overlaps read as layers. No `mix-blend-mode: multiply` here: the blue circle over the yellow triangle turns green.
- **Texture:** lithographic paper grain at 4%, nothing else.
- **Draw-on:** the grid draws first (300ms); forms slide in from off-grid on orthogonal paths, 600ms cubic-bezier(.7,0,.3,1), 120ms stagger.
- **Complexity:** 9 paths, 1.4 KB of SVG, 0.07 ms to generate in Node, 0 filters on the hero. The lightest in the library.

```js
function bauhaus(o = {}) {
  let grid = ''; for (let x = 40; x < 400; x += 40) grid += `M${x} 0V400M0 ${x}H400`;
  const tri = K.poly([[40, 360], [280, 360], [160, 152]]), sq = 'M180 60H340V220H180Z', ci = K.circ(150, 170, 92);
  const inner = (o.badge ? '' : K.stack(grid, [{ c: 'var(--m2)', w: .6 }], 0))
    + [[tri, 'var(--f3)', 's1'], [sq, 'var(--f1)', 's2'], [ci, 'var(--f2)', 's3']].map(([d, col, id], i) => K.part(id, K.fill(d, col) + K.stack(d, [{ c: 'var(--bgc)', w: 3 }], 1 + i))).join('') // stacked, no multiply: blue over yellow turns green
    + K.stack('M40 380H360', [{ c: 'var(--m1)', w: 6, cap: 'butt' }], 1) + K.part('core', K.fill(K.circ(212, 196, 12), 'var(--m1)'));
  return { w: 400, h: 400, defs: '', inner };
}
```

**Hero slots:** `--bgc` paper · `--m1` ink · `--m2` line · `--m3` card · `--f1` accent-1 · `--f2` accent-2 · `--f3` marker

**Palette:**
```
--ground   #2A2624               anthracite
--ground-2 #383330               anthracite-2
--paper    #F2EEE6               linen
--card     #FAF8F3               card
--ink      #1E1B19               ink
--muted    #67615C               steel
--line     rgba(30,27,25,.14)    line
--tint-1   #EFD99A               yellow-chalk   OKLCH L 0.89 C 0.084 h 91
--tint-2   #C3CDE3               blue-chalk   OKLCH L 0.85 C 0.033 h 266
--tint-3   #EDC0B6               red-chalk   OKLCH L 0.84 C 0.054 h 33
--marker   #F2C230               signal-yellow
--accent-1 #C8352B               bauhaus-red
--accent-2 #24459A               bauhaus-blue
```
**Contrast:** ink/paper **14.80** · ink/card 16.14 · ink/tint-1 12.29 · ink/tint-2 10.74 · ink/tint-3 10.45 · muted/paper **5.27** · paper/ground **12.95** · paper/ground-2 10.77 · ink/marker 10.22 · accent-1/paper 4.54 · accent-2/paper 7.58. All body-text pairs pass 4.5:1.

**Type:** display **League Spartan**, body **Jost**, labels **Space Mono**, no hand.
**Texture:** paper grain only.
**Motion:** mechanical and decisive. Strong ease-in-out.
**Reference:** [Harvard Art Museums, special collection "The Bauhaus"](https://www.harvardartmuseums.org/collections/special-collections/the-bauhaus).

---
