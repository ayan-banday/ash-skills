# Kolam · "threshold" (proven: JAIN University to TVS)

**Picture it:** white rice-powder loops drawn around a grid of dots on a dark wooden threshold, with a small cube at the centre.
**Swatch:** `#3A2B22 #F1EDE4 #ECD9A6 #C6CFDA #DDB09A #9E3B2A`

**Suits:** education, partnerships, onboarding and admissions, hospitality, community programmes, FMCG with home rituals, any South Indian client or partner. Tone: warm, considered, auspicious, crafted. Audience: Indian leadership teams, alumni, families, cross-cultural partners who will recognise it.
**Avoid when:** the client has no South Asian tie (it reads as exotic decoration); a fintech or hard-tech brief wants speed; the client requires strict religious neutrality (kolam is broadly cultural but tied to domestic Hindu ritual).
**Cultural note:** a daily practice, mostly by Tamil women at dawn, drawn as a welcome at the threshold; it is meant to be walked over and to fade. Fitting when the project is literally a threshold (a new partnership, an intake, an onboarding) and the client is South Indian or works there. Generate original patterns from the dot-grid rule, credit it in the footer ("Direction: kolam, the threshold drawing of Tamil Nadu"), and keep out deities, lamps-as-Diwali clichés and Sanskrit slogans. It becomes appropriation when used as a generic "Indian pattern" on unrelated products.

**Story device.** The centre, a cube of three rhombi with curls at its tips, is the client's own way of working: three faces, one solid object. Three interlaced triple-strand loops at 120 degrees are the client's three needs; the three strands of each loop are our three moves on that need. Six petal flowers on the outer ring are design touchpoints. The over-under weave says the needs depend on each other.
**Badge:** section 1 lights `core`; the three needs sections light `s1`, `s2`, `s3`; the design section lights `design` (all six flowers).

**SVG recipe**
- **Geometry:** 9×9 pulli dots at 40px. Hexagon r46 split into three rhombi from the centre. Curls are 300-degree arcs (r9) tangent at the three outer tips. Each loop is three concentric ellipses (rx 84±9, ry 30±9) pushed 92px out along -90, 30 and 150 degrees. Flowers: six lens petals (two quadratic curves each), r17, at 60-degree steps on r168.
- **Over-under:** draw all three loops with a ground-coloured casing, then redraw the outer half of each loop (with its casing) on top. That alternates which loop crosses over.
- **Stroke stack:** 6px powder at 35% under 2.8px solid powder, so each line has a soft halo like trailed powder.
- **Texture filter:** the proven powder filter, applied once to the whole group: fractalNoise .035 to displacement 5, grit 1.1 to displacement 2.4, blur 1.1.
- **Draw-on:** dots fade in (300ms), core (rank 0), loops (ranks 1 to 3), flowers (rank 4); 1100ms per rank, 110ms stagger, cubic-bezier(.65,0,.35,1).
- **Complexity:** 34 paths, 15.9 KB of SVG, 0.55 ms to generate in Node, 1 filter on the hero. The only direction with a two-turbulence filter on the hero, so keep the hero at or under about 640px.

```js
function kolam(o = {}) {
  const c = 200, inner = [], L = o.badge ? [{ c: 'var(--m1)', w: 7 }] : [{ c: 'var(--m1)', w: 6, o: .35 }, { c: 'var(--m1)', w: 2.8 }];
  let dots = ''; for (let i = -4; i <= 4; i++) for (let j = -4; j <= 4; j++) dots += K.circ(c + i * 40, c + j * 40, 2.2);
  if (!o.badge) inner.push(K.fill(dots, 'var(--m2)'));
  const v = [...Array(6)].map((_, k) => K.pt(c, c, 46, -90 + k * 60));            // hexagon -> cube of 3 rhombi
  let core = [0, 2, 4].map(k => K.poly([[c, c], v[k], v[(k + 1) % 6], v[(k + 2) % 6]])).join('');
  [1, 3, 5].forEach(k => { const a = -90 + k * 60, cc = K.pt(c, c, 55, a), e = K.pt(cc[0], cc[1], 9, a + 180 + 300);
    core += `M${K.P(v[k][0], v[k][1])}A9 9 0 1 1 ${K.P(e[0], e[1])}`; });                // curl at each outer tip
  for (let k = 0; k < 3; k++) {                                                      // 3 triple-strand bands at 120deg
    const ell = (rx, ry) => `M${-rx} 0a${rx} ${ry} 0 1 0 ${2 * rx} 0a${rx} ${ry} 0 1 0 ${-2 * rx} 0`;
    const strands = [-9, 0, 9].map(dv => ell(84 + dv, 30 + dv)).join('');
    const half = [-9, 0, 9].map(dv => `M0 ${-(30 + dv)}A${84 + dv} ${30 + dv} 0 0 1 0 ${30 + dv}`).join('');
    const g = `translate(${c} ${c}) rotate(${k * 120 - 90}) translate(92 0)`;
    inner.push(K.part('s' + (k + 1), `<g transform="${g}">${K.stack(strands, [{ c: 'var(--bgc)', w: 26, o: .9 }, ...L], 1 + k)}</g>`));
    inner.push(`<g class="part" data-part="s${k + 1}" transform="${g}">${K.stack(half, [{ c: 'var(--bgc)', w: 26 }, ...L], 1 + k)}</g>`); // re-draw half on top = over/under
  }
  inner.push(K.part('core', K.fill(K.circ(c, c, 54), 'var(--bgc)') + K.stack(core, L, 0)));   // centre sits on top of the loops
  for (let k = 0; k < 6; k++) {                                                      // six petal flowers = design
    const [x, y] = K.pt(c, c, 168, k * 60); let fl = '';
    for (let p = 0; p < 6; p++) { const a = p * 60, t = K.pt(x, y, 17, a), l = K.pt(x, y, 9, a - 28), r = K.pt(x, y, 9, a + 28);
      fl += `M${K.P(x, y)}Q${K.P(l[0], l[1])} ${K.P(t[0], t[1])}Q${K.P(r[0], r[1])} ${K.P(x, y)}`; }
    inner.push(K.part('p' + (k + 1), K.stack(fl, L, 4), 'data-group="design"'));
  }
  const body = o.badge ? inner.join('') : `<g filter="url(#powder)">${inner.join('')}</g>`;
  return { w: 400, h: 400, defs: o.badge ? '' : FX.powder(), inner: body };
}
```

**Hero slots:** `--bgc` ground · `--m1` paper · `--m2` ground-2 · `--m3` card · `--f1` accent-1 · `--f2` accent-2 · `--f3` marker

**Palette** (token names are the materials):
```
--ground   #3A2B22               wood
--ground-2 #47362B               wood-2
--paper    #F1EDE4               paper
--card     #FAF7F0               card
--ink      #241D18               ink
--muted    #6B6158               muted
--line     rgba(36,29,24,.14)    line
--tint-1   #ECD9A6               haldi   OKLCH L 0.89 C 0.069 h 90
--tint-2   #C6CFDA               neel   OKLCH L 0.85 C 0.018 h 253
--tint-3   #DDB09A               laterite   OKLCH L 0.79 C 0.061 h 47
--marker   #F2C94C               marker
--accent-1 #9E3B2A               kumkum
--accent-2 #3F4A7A               indigo
```
Extra token from the proven site: `--powder #F4F1EA` (the drawing medium on wood; powder on wood 12.02:1, ink on powder 14.73:1).
**Contrast:** ink/paper **14.22** · ink/card 15.53 · ink/tint-1 11.90 · ink/tint-2 10.55 · ink/tint-3 8.51 · muted/paper **5.17** · paper/ground **11.61** · paper/ground-2 9.82 · ink/marker 10.47 · accent-1/paper 5.77 · accent-2/paper 7.27. All body-text pairs pass 4.5:1.

**Type:** display **Newsreader**, body **Hanken Grotesk**, labels **JetBrains Mono**, hand **Caveat**.
**Texture:** paper grain at about 9% multiply on paper sections; on wood sections the woodgrain filter at 10%; the powder filter on every motif.
**Motion:** slow and deliberate, like a hand trailing powder. 1.1s strokes, ease-in-out, no bounce. Static once drawn.
**Reference:** [Asian Art Museum, "Diwali Festival and Threshold Art"](https://education.asianart.org/resources/diwali-festival-and-threshold-art): rice-flour technique, dot grids, the threshold as an invitation.

---
