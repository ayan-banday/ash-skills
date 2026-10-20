# Madhubani · "the double-line frame"

**Picture it:** a cream panel framed by bands of comb hatching, zigzags and petals, with two fish facing a pink lotus, all in fine black double lines.
**Swatch:** `#2B2020 #F3ECDD #EBC2C6 #EED9A0 #C5CCE0 #B33A27`

**Suits:** celebrations and weddings, food and FMCG, women-led enterprises, family healthcare, education, craft retail, Bihar or Mithila ties. Tone: festive, detailed, warm. Audience: consumer brands, foundations, women's livelihood programmes.
**Avoid when:** a sober B2B brief; the brief would need deity imagery; an ultra-minimal brand.
**Cultural note:** Mithila painting is made by women of the Mithila region (Bihar and Nepal); W.G. Archer first documented it in 1949; much of it shows Hindu deities and wedding rites. Fitting with a Mithila or Bihar tie, or for celebration and abundance themes. Use the nature motifs (fish for abundance, lotus, birds), never deities; credit; commission a Mithila artist for the hero when possible. It becomes appropriation as deity images on packaging or a pastiche of a named artist.

**Story device.** The frame and the pair. Three border bands are three commitments: the outer comb is governance, the zigzag is delivery rhythm, the petal chain is care and support. Two fish facing a lotus are the two partners circling one shared goal; the lotus is the client's outcome.
**Badge:** one band inked (`s1`, `s2`, `s3`), the pair (`pair`) for the partnership section, or the lotus (`core`).

**SVG recipe**
- **Geometry:** rectangles inset 12 and 24 with comb ticks every 6px; a zigzag at 12px pitch, transposed for the sides; a petal chain at 20px pitch; an 8-petal lotus; fish as a closed curve of two quadratics with a forked tail, scales as small arcs every 12px.
- **Stroke stack:** a single 1.6px kajal line. Double lines come from drawing two insets, as in kachni (line) style; fills are flat, as in bharni (filled) style.
- **Texture filter:** none on the motif; a handmade-paper fibre overlay on the page (fractalNoise ".02 .9" at 5%).
- **Draw-on:** like a nib, steady and linear, about 1s per element: frame outside-in, then the fish, then the lotus; fills fade in 400ms after their outlines.
- **Complexity:** 10 paths, 10.9 KB of SVG, 0.55 ms to generate in Node, 0 filters on the hero.

```js
function madhubani(o = {}) {
  const c = 200, rect = i => `M${i} ${i}H${400 - i}V${400 - i}H${i}Z`;
  let comb = '', zig = '', chain = '';
  for (let t = 18; t < 382; t += 6) comb += `M${t} 12V24M${t} 376V388M12 ${t}H24M376 ${t}H388`;   // band 1: double line + comb hatch
  const zz = (y, flip) => { let d = `M36 ${y}`; for (let x = 36, k = 0; x <= 364; x += 12, k++) d += `L${x} ${k % 2 ? y + (flip ? -10 : 10) : y}`; return d; };
  zig = zz(32, 0) + zz(368, 1);
  zig += zig.replace(/M(\d+\.?\d*) (\d+\.?\d*)|L(\d+\.?\d*) (\d+\.?\d*)/g, (m, a1, b1, a2, b2) => a1 ? `M${b1} ${a1}` : `L${b2} ${a2}`); // transpose for sides
  for (let t = 60; t <= 340; t += 20) [[t, 54], [t, 346], [54, t], [346, t]].forEach(([x, y]) => chain += `M${x - 7} ${y}Q${x} ${y - 6} ${x + 7} ${y}Q${x} ${y + 6} ${x - 7} ${y}Z`);
  let lotus = ''; for (let k = 0; k < 8; k++) { const t = K.pt(c, c, 46, k * 45 - 90), l = K.pt(c, c, 26, k * 45 - 112), r = K.pt(c, c, 26, k * 45 - 68);
    lotus += `M${K.P(c, c)}Q${K.P(l[0], l[1])} ${K.P(t[0], t[1])}Q${K.P(r[0], r[1])} ${K.P(c, c)}Z`; }
  const fish = (sx) => { const g = (x, y) => [c + sx * x, c + y];
    const P = (x, y) => K.P(...g(x, y));
    let d = `M${P(-30, 0)}Q${P(-60, -54)} ${P(-118, -20)}L${P(-138, -40)}L${P(-130, 0)}L${P(-138, 40)}L${P(-118, 20)}Q${P(-60, 54)} ${P(-30, 0)}Z`;
    let sc = ''; for (let x = -100; x <= -55; x += 12) for (let y = -14; y <= 14; y += 14) sc += `M${P(x, y - 6)}Q${P(x + 8, y)} ${P(x, y + 6)}`;
    return { body: d, detail: sc + K.circ(...g(-48, -6), 3.5) }; };
  const L = [{ c: 'var(--m1)', w: 1.6 }], fL = fish(1), fR = fish(-1);
  const inner = K.part('s1', K.stack(rect(12) + rect(24) + comb, L, 0)) + K.part('s2', K.stack(zig, L, 1)) + K.part('s3', K.fill(chain, 'var(--f2)') + K.stack(chain, L, 2))
    + K.part('p1', K.fill(fL.body, 'var(--f2)') + K.stack(fL.body + fL.detail, L, 3), 'data-group="pair"')
    + K.part('p2', K.fill(fR.body, 'var(--f3)') + K.stack(fR.body + fR.detail, L, 3), 'data-group="pair"')
    + K.part('core', K.fill(lotus, 'var(--f1)') + K.stack(lotus + K.circ(c, c, 8), L, 4));
  return { w: 400, h: 400, defs: '', inner };
}
```

**Hero slots:** `--bgc` paper · `--m1` ink · `--m2` line · `--m3` card · `--f1` tint-1 · `--f2` marker · `--f3` tint-3

**Palette:**
```
--ground   #2B2020               lampblack
--ground-2 #3A2A2A               lampblack-2
--paper    #F3ECDD               handmade
--card     #FBF7EE               card
--ink      #231B1B               kajal
--muted    #6C5E5A               bark
--line     rgba(35,27,27,.14)    line
--tint-1   #EBC2C6               kusum   OKLCH L 0.85 C 0.047 h 12
--tint-2   #EED9A0               haldi   OKLCH L 0.89 C 0.077 h 90
--tint-3   #C5CCE0               neel   OKLCH L 0.85 C 0.029 h 270
--marker   #F0C64A               haldi-bright
--accent-1 #B33A27               sindoor
--accent-2 #A23A6B               kusum-deep
```
**Contrast:** ink/paper **14.35** · ink/card 15.79 · ink/tint-1 10.50 · ink/tint-2 12.11 · ink/tint-3 10.52 · muted/paper **5.27** · paper/ground **13.42** · paper/ground-2 11.56 · ink/marker 10.35 · accent-1/paper 5.03 · accent-2/paper 5.32. All body-text pairs pass 4.5:1.

**Type:** display **Rozha One**, body **Laila**, labels **Red Hat Mono**, hand **Amita**.
**Texture:** handmade-paper fibres; no grain on the motif lines.
**Motion:** patient and nib-like. Linear, no bounce.
**Reference:** [V&A IS.83-1983, Madhubani painting by Sunila Kumari (c. 1973)](https://collections.vam.ac.uk/item/O82478/painting-unknown): ink and paint on paper, from the Naylor bequest.

---
