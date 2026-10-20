# Sashiko · "the mending stitch"

**Picture it:** rows of short indigo running stitches on unbleached cotton that lock into crosses and boxes, over a few soft patches.
**Swatch:** `#2E2620 #F2EEE6 #C9D3DE #E4C6AE #DCCACB #2E4372`

**Suits:** sustainability, repair and renewal, turnaround and long-term partnerships, care and healthcare, education, slow fashion, NGOs. Tone: patient, honest, warm, frugal. Audience: CSR, public sector, care organisations.
**Avoid when:** a hype launch; flashy consumer work; any framing where "mending" implies the client is broken (pitch it as reinforcement).
**Cultural note:** sashiko began as rural Japanese reinforcement stitching on indigo work clothes; it is now a global mending craft. Fitting for strengthen-what-exists stories. Credit the origin; skip kanji decoration and "boro poverty chic". Low risk.

**Story device.** Hitomezashi, "one stitch". Each row and column is a yes or no, and the whole pattern emerges from many small consistent stitches. The bits come from the client's name, so the pattern is literally theirs (pass `text`). Patches are where we reinforce: the centre patch is the client's core; three patches are the three needs.
**Badge:** the grid with one patch filled (`core`, `s1`, `s2`, `s3`).

**SVG recipe**
- **Geometry:** a 16×16 grid at 22px. Row i stitches start at offset bit(i) and skip every other cell; columns the same. Each stitch stops 3px short of the grid point. Row bits = character-code parity of the name; column bits = parity of the reversed name plus the index.
- **Stroke stack:** thread shadow 2.4px ink at 35% offset (0.6, 0.9), thread 2.2px.
- **Texture:** a 2px diagonal cotton weave at 4% on paper; indigo mottling only on tint blocks (fractalNoise .015 at 6%).
- **Draw-on:** all stitches live in one path, so the dash animation runs stitch by stitch like a needle: 2.4s, linear. Patches fade in first.
- **Complexity:** 6 paths, 6.8 KB of SVG, 0.21 ms to generate in Node, 0 filters on the hero. The cheapest dense motif.

```js
function sashiko(o = {}) {
  const txt = (o.text || 'TVS x JAIN University').replace(/\s/g, ''), N = 16, s = 22, m = 24;
  const bits = (t, k) => [...Array(N + 1)].map((_, i) => (t.charCodeAt(i % t.length) + (k ? i : 0)) % 2);
  const br = bits(txt, 0), bc = bits([...txt].reverse().join(''), 1);
  let st = '';
  for (let i = 0; i <= N; i++) for (let j = br[i]; j < N; j += 2) st += `M${m + j * s + 3} ${m + i * s}H${m + (j + 1) * s - 3}`;
  for (let j = 0; j <= N; j++) for (let i = bc[j]; i < N; i += 2) st += `M${m + j * s} ${m + i * s + 3}V${m + (i + 1) * s - 3}`;
  const patch = (x, y, w, h, col) => K.fill(`M${m + x * s} ${m + y * s}h${w * s}v${h * s}h${-w * s}z`, col);
  const inner = K.part('core', patch(6, 6, 4, 4, 'var(--f1)')) + K.part('s1', patch(1, 2, 4, 3, 'var(--f2)')) + K.part('s2', patch(11, 3, 4, 4, 'var(--f3)')) + K.part('s3', patch(3, 11, 6, 4, 'var(--f2)'))
    + `<g class="stitch">${K.stack(st, o.badge ? [{ c: 'var(--m1)', w: 2.4 }] : [{ c: 'var(--m2)', w: 2.4, o: .35, t: '.6 .9' }, { c: 'var(--m1)', w: 2.2 }], 0)}</g>`;
  return { w: N * s + 2 * m, h: N * s + 2 * m, defs: '', inner };
}
```

**Hero slots:** `--bgc` paper · `--m1` accent-1 · `--m2` ink · `--m3` card · `--f1` tint-1 · `--f2` tint-2 · `--f3` tint-3 (a light hero: indigo thread on kinari cotton, which keeps blue off the hero background).

**Palette:**
```
--ground   #2E2620               kakishibu-dark
--ground-2 #3C322B               kakishibu-2
--paper    #F2EEE6               kinari
--card     #FAF8F3               sarashi
--ink      #221F1D               sumi
--muted    #66605B               nezumi
--line     rgba(34,31,29,.14)    line
--tint-1   #C9D3DE               kamenozoki   OKLCH L 0.86 C 0.019 h 251
--tint-2   #E4C6AE               kakishibu   OKLCH L 0.85 C 0.047 h 61
--tint-3   #DCCACB               sakura-nezumi   OKLCH L 0.85 C 0.020 h 14
--marker   #F0CB6B               kuchinashi
--accent-1 #2E4372               ai
--accent-2 #9A4E2E               kaki
```
**Contrast:** ink/paper **14.16** · ink/card 15.44 · ink/tint-1 10.81 · ink/tint-2 10.13 · ink/tint-3 10.42 · muted/paper **5.35** · paper/ground **12.83** · paper/ground-2 10.78 · ink/marker 10.50 · accent-1/paper 8.39 · accent-2/paper 5.18. All body-text pairs pass 4.5:1.

**Type:** display **Zen Old Mincho**, body **Zen Maru Gothic**, labels **M PLUS 1 Code**, hand **Yomogi**.
**Texture:** cotton weave and indigo mottling as above.
**Motion:** steady, linear, rhythmic. No easing flourishes.
**Reference:** [V&A FE.108-1982, sashiko sledge-hauling jacket, Shonai (1870 to 1900)](https://collections.vam.ac.uk/item/O24578): quilted diamonds; a white band reinforces where the rope rubbed.

---
