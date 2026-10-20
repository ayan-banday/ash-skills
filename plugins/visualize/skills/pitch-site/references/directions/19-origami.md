# Origami · "one sheet"

**Picture it:** a sheet of washi creased into a zigzag Miura fold, pale and lilac facets, with dashed valley and dot-dash mountain lines.
**Swatch:** `#2A2626 #F3F1EC #F0CFC7 #D4CDE6 #EBD6B0 #C23A47`

**Suits:** consumer products and packaging, design and architecture, flat-pack logistics, space and engineering (Miura-fold solar panels), education, transformation programmes. Tone: calm, clever, elegant. Audience: designers, product teams, executives.
**Avoid when:** a data-heavy brief; a rough-craft feel is wanted.
**Cultural note:** Japanese paper folding, now practised worldwide; the line notation (valley dashed, mountain dot-dash) comes from Akira Yoshizawa's system. Low risk. Skip the crane cliché unless its meaning (peace, healing) fits.

**Story device.** One sheet is the client's organisation: we add nothing and cut nothing, everything comes from what they already have. The crease pattern is the plan; each fold band is a step; the folded form is the outcome. Mountain folds are what we raise; valley folds are what we tuck away.
**Badge:** the crease pattern with one fold band lit (`s1`, `s2`, `s3`) or the centre (`core`).

**SVG recipe**
- **Geometry:** Miura-ori, 6×7 parallelograms (56 by 46, zigzag offset 16). Facets alternate light and shade to fake relief. Zigzag lines alternate mountain and valley by column; straight segments alternate by (row + column), which satisfies the M − V = ±2 rule at every vertex.
- **Stroke stack:** 1.2px lines in Yoshizawa notation (valley "6 4", mountain "10 3 2 3"); a 1.6px outline.
- **Texture:** kozo fibres (fractalNoise ".01 .3" at 5%); soft facet shadows.
- **Draw-on:** facets fade in by fold band (500ms, ease-in-out-cubic); crease lines fade (dashed lines cannot draw on); optionally the sheet breathes (scaleX 0.96, skewY 2 degrees).
- **Complexity:** 45 paths, 4.9 KB of SVG, 0.23 ms to generate in Node, 0 filters on the hero.

```js
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
```

**Hero slots:** `--bgc` paper · `--m1` ink · `--m2` line · `--m3` card · `--f1` card · `--f2` tint-2 · `--f3` tint-1

**Palette:**
```
--ground   #2A2626               kurogami
--ground-2 #383333               kurogami-2
--paper    #F3F1EC               washi
--card     #FBFAF7               card
--ink      #1F1C1C               sumi
--muted    #65605E               muted
--line     rgba(31,28,28,.14)    line
--tint-1   #F0CFC7               momo   OKLCH L 0.88 C 0.039 h 34
--tint-2   #D4CDE6               fuji   OKLCH L 0.86 C 0.035 h 298
--tint-3   #EBD6B0               kuchiba   OKLCH L 0.88 C 0.055 h 82
--marker   #F0C340               yamabuki
--accent-1 #C23A47               beni
--accent-2 #2F3C78               kon
```
**Contrast:** ink/paper **14.99** · ink/card 16.21 · ink/tint-1 11.65 · ink/tint-2 11.02 · ink/tint-3 11.91 · muted/paper **5.49** · paper/ground **13.25** · paper/ground-2 11.01 · ink/marker 10.14 · accent-1/paper 4.66 · accent-2/paper 9.13. All body-text pairs pass 4.5:1.

**Type:** display **Syne**, body **Lexend**, labels **Sometype Mono**, no hand.
**Texture:** kozo fibres on paper.
**Motion:** smooth and crisp, like paper turning. Ease-in-out.
**Reference:** [Mingei International Museum, "Origami Masterworks" (2003 to 2005)](https://mingei.org/exhibitions/origami-masterworks): about 200 works by 42 folders, including Yoshizawa and Tomoko Fusé.

---
