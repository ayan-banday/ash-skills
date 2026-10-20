# Swiss International · "the grid and the rings"

**Picture it:** a strict six-column grid with black concentric rings spreading from one point and one red quadrant.
**Swatch:** `#252220 #F3F1EC #EEC4BD #DDD5CA #C8D2DE #C42B24`

**Suits:** finance, consulting, B2B SaaS, pharma, institutions, government, annual-report style proposals, multinationals. Tone: rational, credible, calm. Audience: CFOs, procurement, boards.
**Avoid when:** warmth or craft is the brief; a very young audience.
**Cultural note:** the International Typographic Style (Zurich and Basel, 1950s; Josef Müller-Brockmann). No concern.

**Story device.** The ripple. The centre dot is the client's decision; the rings are phases spreading outward (inner = phase 1, middle = phase 2, outer = phase 3); the red quadrant is the focus area. Grid columns are workstreams.
**Badge:** one ring band in accent (`s1`, `s2`, `s3`) or the dot (`core`).

**SVG recipe**
- **Geometry:** a 6×6 module grid; rings from r30 to r420 every 30px around (130, 270), every third ring 7px; a red quadrant path clipped to the frame.
- **Stroke stack:** single strokes (2.2px and 7px).
- **Texture:** none (purity is the point), or offset-paper grain at 3%.
- **Draw-on:** rings draw from the inside out, 700ms each, cubic-bezier(.2,0,0,1), 70ms stagger.
- **Complexity:** 17 paths, 3.1 KB of SVG, 0.06 ms to generate in Node, 0 filters on the hero.

```js
function swiss(o = {}) {
  let grid = ''; for (let x = 0; x <= 400; x += 400 / 6) grid += `M${K.f(x)} 0V400M0 ${K.f(x)}H400`;
  const ring = (r, w) => K.stack(K.circ(130, 270, r), [{ c: 'var(--m1)', w }], Math.round(r / 30));
  const grp = (a, b) => { let d = ''; for (let r = a; r <= b; r += 30) d += ring(r, r % 90 === 0 ? 7 : 2.2); return d; };
  const inner = (o.badge ? '' : K.stack(grid, [{ c: 'var(--m2)', w: .6 }], 0))
    + `<g clip-path="url(#swclip)">${K.fill('M130 270V-200A470 470 0 0 1 600 270Z', 'var(--f1)')}${K.part('s1', grp(30, 90))}${K.part('s2', grp(120, 180))}${K.part('s3', grp(210, 420))}</g>`
    + K.part('core', K.fill(K.circ(130, 270, 9), 'var(--m1)'));
  return { w: 400, h: 400, defs: '<clipPath id="swclip"><rect width="400" height="400"/></clipPath>', inner };
}
```

**Hero slots:** `--bgc` paper · `--m1` ink · `--m2` line · `--m3` card · `--f1` accent-1 · `--f2` accent-2 · `--f3` marker

**Palette:**
```
--ground   #252220               press-black
--ground-2 #33302D               press-black-2
--paper    #F3F1EC               offset
--card     #FBFAF7               card
--ink      #1C1A19               ink
--muted    #625D59               muted
--line     rgba(28,26,25,.14)    line
--tint-1   #EEC4BD               red-tint   OKLCH L 0.85 C 0.049 h 29
--tint-2   #DDD5CA               stone   OKLCH L 0.88 C 0.017 h 76
--tint-3   #C8D2DE               cool-tint   OKLCH L 0.86 C 0.020 h 253
--marker   #F3D35A               signal
--accent-1 #C42B24               swiss-red
--accent-2 #2B3F9E               ultramarine
```
**Contrast:** ink/paper **15.36** · ink/card 16.61 · ink/tint-1 10.95 · ink/tint-2 11.93 · ink/tint-3 11.34 · muted/paper **5.76** · paper/ground **14.01** · paper/ground-2 11.62 · ink/marker 11.79 · accent-1/paper 5.00 · accent-2/paper 8.06. All body-text pairs pass 4.5:1.

**Type:** display **Inter Tight** (700 to 800, tracking -2%), body **Inter**, labels **Geist Mono**, no hand.
**Texture:** none or 3% grain.
**Motion:** precise and quick. No overshoot.
**Reference:** [V&A E.1306-2004, Musica Viva poster by Josef Müller-Brockmann (1959)](https://collections.vam.ac.uk/item/O110243).

---
