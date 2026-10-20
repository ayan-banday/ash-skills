# Memphis · "the laminate party"

**Picture it:** a pink circle, a yellow triangle and a blue squiggle with thick black outlines and hard shadows, among confetti and a small black grid.
**Swatch:** `#232021 #F4F0E8 #F2C3CF #BFD7EA #F3DE9F #DE3F3A`

**Suits:** youth brands, entertainment, media, food and beverage, events, creative agencies, teen edtech, D2C. Tone: cheeky, loud, optimistic. Audience: Gen Z, marketing teams.
**Avoid when:** serious B2B, healthcare, government, anything about loss.
**Cultural note:** the Memphis group (Milan, 1981 to 1988, Ettore Sottsass). No appropriation concern. Do not copy Sottsass's Bacterio laminate exactly, and skip the movement's mint and teal (green rule).

**Story device.** Each shape is a pillar: the circle is people, the triangle is growth, the squiggle is energy and creativity, the grid is structure. The ring at the centre is the client.
**Badge:** one shape coloured (`s1` circle, `s2` triangle, `s3` squiggle, `s4` grid) or the ring (`core`).

**SVG recipe**
- **Geometry:** 22 confetti pieces by seeded rejection sampling (at least 46px apart, outside r120 from the centre); a sine squiggle (amplitude 16); circle r70; triangle; a 100×80 grid.
- **Stroke stack:** 4px ink outlines; the squiggle is 13px ink under 8px blue, an outlined stroke; hard shadows are the same shape offset (6, 6) in ink.
- **Texture:** none (flat laminate), or a Bacterio-style blob fill on one card.
- **Draw-on:** shapes arrive with a quick scale-in (0.94 to 1, 420ms, cubic-bezier(.22,1,.36,1)), 90ms apart, outlines pen-drawn; hard shadows appear with their shape; confetti fades in last.
- **Complexity:** 12 paths, 3.9 KB of SVG, 0.29 ms to generate in Node, 0 filters on the hero.

```js
function memphis(o = {}) {
  const r = K.rng(o.seed || 9), pts = [];
  for (let t = 0; t < 5000 && pts.length < 22; t++) { const p = [20 + r() * 360, 20 + r() * 360]; if (pts.every(q => Math.hypot(q[0] - p[0], q[1] - p[1]) > 46) && Math.hypot(p[0] - 200, p[1] - 200) > 120) pts.push(p); }
  let conf = ''; pts.forEach(([x, y], i) => { const a = r() * 180; conf += i % 3 === 0 ? K.circ(x, y, 4) : i % 3 === 1 ? K.poly([K.pt(x, y, 7, a), K.pt(x, y, 7, a + 120), K.pt(x, y, 7, a + 240)]) : `M${K.P(...K.pt(x, y, 9, a))}L${K.P(...K.pt(x, y, 9, a + 180))}`; });
  let sq = 'M60 300'; for (let x = 60; x <= 340; x += 10) sq += `L${x} ${300 + 16 * Math.sin((x - 60) / 14)}`;
  let grid = ''; for (let k = 0; k <= 80; k += 10) grid += `M250 ${40 + k}H350M${250 + k * 1.25} 40V120`;
  const O = [{ c: 'var(--m1)', w: 4 }], shadow = d => o.badge ? '' : `<g transform="translate(6 6)">${K.fill(d, 'var(--m1)')}</g>`;
  const ci = K.circ(140, 170, 70), tri = K.poly([[230, 290], [330, 290], [280, 200]]);
  const inner = (o.badge ? '' : K.stack(conf, [{ c: 'var(--m1)', w: 3 }], 0))
    + K.part('s4', K.stack(grid, [{ c: 'var(--m1)', w: 1.4 }], 1)) + K.part('s1', shadow(ci) + K.fill(ci, 'var(--f1)') + K.stack(ci, O, 2))
    + K.part('s2', shadow(tri) + K.fill(tri, 'var(--f3)') + K.stack(tri, O, 3)) + K.part('s3', K.stack(sq, [{ c: 'var(--m1)', w: 13 }, { c: 'var(--f2)', w: 8 }], 4))
    + K.part('core', K.fill(K.circ(200, 220, 12), 'var(--m3)') + K.stack(K.circ(200, 220, 12), O, 5));
  return { w: 400, h: 400, defs: '', inner };
}

const GENERATORS = { kolam, ajrakh, warli, madhubani, patola, truckart, kumiko, sashiko, girih, azulejo, bauhaus, swiss, riso, drafting, herbarium, transit, letterpress, circuit, origami, memphis };
```

**Hero slots:** `--bgc` paper · `--m1` ink · `--m2` line · `--m3` card · `--f1` tint-1 · `--f2` accent-2 · `--f3` marker

**Palette:**
```
--ground   #232021               laminate-black
--ground-2 #322E2F               laminate-2
--paper    #F4F0E8               paper
--card     #FCFAF5               card
--ink      #1E1B1C               ink
--muted    #645E5E               muted
--line     rgba(30,27,28,.14)    line
--tint-1   #F2C3CF               flamingo   OKLCH L 0.86 C 0.056 h 1
--tint-2   #BFD7EA               pool-blue   OKLCH L 0.87 C 0.037 h 242
--tint-3   #F3DE9F               banana   OKLCH L 0.90 C 0.084 h 92
--marker   #F8D23C               yellow
--accent-1 #DE3F3A               memphis-red
--accent-2 #2A49B8               cobalt
```
**Contrast:** ink/paper **15.04** · ink/card 16.38 · ink/tint-1 10.97 · ink/tint-2 11.49 · ink/tint-3 12.83 · muted/paper **5.59** · paper/ground **14.21** · paper/ground-2 11.79 · ink/marker 11.62 · accent-1/paper 3.79 · accent-2/paper 6.73. All body-text pairs pass 4.5:1. **accent-1 is display-only** (3.79:1): use it for fills and type at 24px or larger, never body text or links.

**Type:** display **Archivo Black**, body **Rubik**, labels **Space Mono**, hand **Shadows Into Light**.
**Texture:** none.
**Motion:** fast and cheerful. The loudness lives in shape, colour and hard shadows; motion stays inside the house rules (no spring, no bounce, no rotation).
**Reference:** [V&A collections, Memphis](https://collections.vam.ac.uk/context/organisation/A5933/memphis): 13 objects made between 1981 and 1988, including Sottsass's Casablanca sideboard.


---
