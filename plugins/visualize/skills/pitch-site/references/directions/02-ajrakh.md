# Ajrakh · "the printing table"

**Picture it:** a deep indigo and madder-red cloth with an eight-point star, white resist dots and a saw-tooth border, printed in visible layers.
**Swatch:** `#2E1F1D #F2ECE2 #E7C3BC #C3CBDD #E8D7AE #9C2F2A`

**Suits:** textiles, fashion, natural dyes and sustainability, craft-led D2C, heritage hospitality, Gujarat, Kutch or Sindh ties, and process-heavy proposals (manufacturing, supply chain) where stages matter. Tone: rich, rigorous, earthy. Audience: founders, craft and design buyers, CSR teams.
**Avoid when:** the brand is minimal-tech; the client sells synthetic fast fashion (it contradicts the slow-dye story); a light, airy site is wanted (ajrakh is dense).
**Cultural note:** ajrakh is the craft of the Khatri block printers of Kutch (Ajrakhpur, Dhamadka) and Sindh, a largely Muslim artisan lineage; the knowledge is the many-day cycle of resist, mordant and dye baths. Credit the Khatri printers, generate original geometry (never copy a named block), and for the hero consider licensing a real block or commissioning a printer. It becomes appropriation as a digital "ajrakh-style" print sold as ajrakh, or used to make synthetic goods look handmade.

**Story device.** The pass. Ajrakh is printed in passes: resist, outline, madder, indigo. Each section adds one pass, so the page prints the client's solution as the reader scrolls. The centre star is the client. The saw-tooth border is the guardrails (governance, timeline). The white resist dots are what we protect: the things that stay untouched.
**Badge:** the tile with only the current pass printed solid (`indigo`, `madder`, `resist`, or `core` for the outline pass).

**SVG recipe**
- **Geometry:** a 16-vertex star (R100, inner radius 0.765R); four corner stars clipped to the field; 72 border teeth rotated per side; 8 lens petals; 24 resist dots on r104.
- **Misregistration:** each pass is a group translated by a seeded random ±1.2px, so colours sit slightly off each other the way hand blocks do.
- **Stroke stack:** one 2.4px kat-black outline; colour is carried by fills.
- **Texture filter:** speckle (fractal noise thresholded into small dropouts) for ink starvation on a wooden block; plus a 2px crosshatch cloth overlay at 4%.
- **Draw-on:** "stamp" each pass: opacity 0 to 1 and scale 1.015 to 1 in 220ms ease-out, 260ms between passes; then the outline draws in 900ms.
- **Complexity:** 6 paths, 7.9 KB of SVG, 0.53 ms to generate in Node, 1 filter on the hero.

```js
function ajrakh(o = {}) {
  const c = 200, r = K.rng(o.seed || 11), mis = () => o.badge ? '0 0' : `${K.f((r() - .5) * 2.4)} ${K.f((r() - .5) * 2.4)}`;
  const star = (x, y, R) => K.poly([...Array(16)].map((_, k) => K.pt(x, y, k % 2 ? R * .765 : R, k * 22.5 - 90)));
  let teeth = ''; for (let s = 0; s < 4; s++) for (let i = 0; i < 18; i++) {
    const t0 = 28 + i * 19.1, t1 = t0 + 19.1, tm = (t0 + t1) / 2, pts = [[t0, 28], [tm, 14], [t1, 28]];
    teeth += K.poly(pts.map(([x, y]) => { const [X, Y] = [x - c, y - c], a = s * Math.PI / 2; return [c + X * Math.cos(a) - Y * Math.sin(a), c + X * Math.sin(a) + Y * Math.cos(a)]; })); }
  let corners = ''; [[0, 0], [400, 0], [0, 400], [400, 400]].forEach(([x, y]) => corners += star(x, y, 70));
  let petals = ''; for (let k = 0; k < 8; k++) { const t = K.pt(c, c, 52, k * 45), a = K.pt(c, c, 22, k * 45 - 22), b = K.pt(c, c, 22, k * 45 + 22);
    petals += `M${K.P(c, c)}Q${K.P(a[0], a[1])} ${K.P(t[0], t[1])}Q${K.P(b[0], b[1])} ${K.P(c, c)}Z`; }
  let dots = ''; for (let k = 0; k < 24; k++) { const [x, y] = K.pt(c, c, 104, k * 15); dots += K.circ(x, y, 3.2); }
  const pass1 = K.fill(`M28 28H372V372H28Z` + corners + star(c, c, 100), 'var(--f2)', 'fill-rule="evenodd" clip-path="url(#ajclip)"'); // indigo field, stars resisted
  const pass2 = K.fill(star(c, c, 100) + teeth, 'var(--f1)') + K.fill(corners, 'var(--f1)', 'clip-path="url(#ajclip)"');       // madder
  const pass3 = K.stack(star(c, c, 100) + 'M14 14H386V386H14Z M28 28H372V372H28Z' + petals, [{ c: 'var(--m1)', w: 2.4 }], 1)
    + `<g clip-path="url(#ajclip)">${K.stack(corners, [{ c: 'var(--m1)', w: 2.4 }], 1)}</g>`;                                   // kat black outline
  const pass4 = K.fill(dots + K.circ(c, c, 7), 'var(--m3)');                                                  // white resist dots
  const inner = [K.part('p1', `<g transform="translate(${mis()})">${pass1}</g>`, 'data-group="indigo"'),
    K.part('p2', `<g transform="translate(${mis()})">${pass2}</g>`, 'data-group="madder"'),
    K.part('core', `<g transform="translate(${mis()})">${pass3}</g>`),
    K.part('p3', `<g transform="translate(${mis()})">${pass4}</g>`, 'data-group="resist"')].join('');
  return { w: 400, h: 400, defs: `<clipPath id="ajclip"><rect x="28" y="28" width="344" height="344"/></clipPath>` + (o.badge ? '' : FX.speckle('ajspk', .8)),
    inner: o.badge ? inner : `<g filter="url(#ajspk)">${inner}</g>` };
}
```

**Hero slots:** `--bgc` paper · `--m1` ink · `--m2` line · `--m3` card · `--f1` accent-1 · `--f2` accent-2 · `--f3` marker

**Palette:**
```
--ground   #2E1F1D               kat
--ground-2 #3B2724               kat-2
--paper    #F2ECE2               resist
--card     #FAF6EF               cotton
--ink      #231A18               kat-ink
--muted    #6E5F59               clay
--line     rgba(35,26,24,.14)    line
--tint-1   #E7C3BC               madder-wash   OKLCH L 0.85 C 0.042 h 31
--tint-2   #C3CBDD               indigo-wash   OKLCH L 0.84 C 0.027 h 267
--tint-3   #E8D7AE               harda   OKLCH L 0.88 C 0.057 h 88
--marker   #EDC46A               myrobalan
--accent-1 #9C2F2A               madder
--accent-2 #2F3F73               indigo
```
**Contrast:** ink/paper **14.50** · ink/card 15.82 · ink/tint-1 10.49 · ink/tint-2 10.47 · ink/tint-3 11.98 · muted/paper **5.19** · paper/ground **13.44** · paper/ground-2 11.90 · ink/marker 10.31 · accent-1/paper 6.26 · accent-2/paper 8.59. All body-text pairs pass 4.5:1.

**Type:** display **Gloock**, body **Mukta Vaani** (also sets Gujarati), labels **IBM Plex Mono**, hand **Kalam**.
**Texture:** cloth crosshatch at 4% on tint blocks; speckle on the motif; paper grain elsewhere.
**Motion:** printerly thumps. Quick, firm, ease-out, no bounce.
**Reference:** [V&A Ajrakh Sample Book by Ismail Mohammad Khatri (2006), on Google Arts & Culture](https://artsandculture.google.com/asset/SgEDqn4X-G4g5g): samples sewn into a book to show the process stages.

---
