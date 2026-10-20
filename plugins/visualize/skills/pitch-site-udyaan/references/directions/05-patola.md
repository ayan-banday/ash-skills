# Patola · "the double ikat"

**Picture it:** rows of stepped diamonds in lac red, saffron and indigo with soft feathered edges, like silk threads dyed before weaving.
**Swatch:** `#3A1F25 #F4EEE3 #E5BFC2 #EED4A6 #C8CDE0 #9E2A3A`

**Suits:** partnerships and joint ventures, luxury, silk and fashion, weddings, family businesses, heritage banking, Gujarat ties. Tone: precious, exact, celebratory. Audience: family-business boards, luxury buyers, JV partners.
**Avoid when:** the audience is young and casual; the brief is data-heavy (keep the blur on the motif, never on text).
**Cultural note:** Patan patola is woven by the Salvi family; both warp and weft are resist-dyed before weaving, and one sari takes months. Fitting with a Gujarat tie or a partnership story. Generate original stepped geometry (never reproduce a named design such as the parrot-and-elephant pattern), credit. It becomes appropriation as "patola print" on mass goods implying the real weave.

**Story device.** Warp and weft. Both sets of threads are dyed separately before they meet, and the pattern only appears when both align: the client's threads and ours. Rows of diamonds are the stages; the centre diamond is the client; the feathered edges are the honest blur before alignment.
**Badge:** the current section's row sharp (registered), the other rows blurred and faint (`s1`, `s2`, `s3`, `core`).

**SVG recipe**
- **Geometry:** a diamond lattice with rows 65px apart, staggered 65px. Each diamond is a stack of horizontal bars (u = 7px thread bundles) whose widths step by u; four nested diamonds (n = 9, 6, 3, 1). Bar ends jitter by a seeded ±0.45u: that is the thread bleed.
- **Stroke stack:** none; all fills.
- **Texture filter:** horizontal-only blur, `stdDeviation="1.3 0"`, the ikat signature; a 4% linear-gradient sheen for silk.
- **Draw-on:** "weaving": a clip rectangle sweeps each row left to right like a shuttle, 500ms per row, ease-in-out; then the blur eases from 2.4 to 1.3 as the pattern registers.
- **Complexity:** 69 paths, 26.4 KB of SVG, 1.2 ms to generate in Node, 1 filter on the hero. The heaviest SVG in the library, still small.

```js
function patola(o = {}) {
  const r = K.rng(o.seed || 5), u = 7, J = () => o.badge ? 0 : (r() - .5) * u * .9;   // J = thread-bundle feathering
  const diamond = (cx, cy, n, col) => { let d = '';
    for (let j = -n; j <= n; j++) { const w = (n - Math.abs(j) + .5) * u, x0 = cx - w + J(), x1 = cx + w + J();
      d += `M${K.f(x0)} ${cy + j * u - u / 2}H${K.f(x1)}V${cy + j * u + u / 2}H${K.f(x0)}Z`; }
    return K.fill(d, col); };
  const cell = (cx, cy) => diamond(cx, cy, 9, 'var(--f1)') + diamond(cx, cy, 6, 'var(--f2)') + diamond(cx, cy, 3, 'var(--f3)') + diamond(cx, cy, 1, 'var(--m3)');
  const rows = { s1: '', s2: '', s3: '' }, ids = ['s1', 's2', 's3']; let core = '';
  for (let ri = 0; ri < 5; ri++) for (let x = ri % 2 ? 5 : 70; x <= 400; x += 130) {      // diamond lattice: rows 65 apart, staggered
    const y = 70 + ri * 65, key = ri < 2 ? 's1' : ri === 2 ? 's2' : 's3';
    if (ri === 2 && x === 200) core += cell(x, y); else rows[key] += cell(x, y); }
  const blur = o.badge ? '' : ' filter="url(#ikat)"';
  const inner = K.fill('M0 0H400V400H0Z', 'var(--bgc)') + ids.map(s => K.part(s, `<g${blur}>${rows[s]}</g>`)).join('') + K.part('core', `<g${blur}>${core}</g>`);
  return { w: 400, h: 400, defs: FX.hblur('ikat', 1.3), inner };
}
```

**Hero slots:** `--bgc` ground · `--m1` ink · `--m2` line · `--m3` card · `--f1` accent-1 · `--f2` marker · `--f3` tint-3

**Palette:**
```
--ground   #3A1F25               lac-deep
--ground-2 #4A2830               lac-deep-2
--paper    #F4EEE3               raw-silk
--card     #FBF8F1               silk
--ink      #251A1C               ink
--muted    #6E5E60               muted
--line     rgba(37,26,28,.14)    line
--tint-1   #E5BFC2               lac-rose   OKLCH L 0.84 C 0.044 h 13
--tint-2   #EED4A6               saffron-wash   OKLCH L 0.88 C 0.067 h 82
--tint-3   #C8CDE0               indigo-haze   OKLCH L 0.85 C 0.027 h 274
--marker   #F0B94A               saffron
--accent-1 #9E2A3A               lac
--accent-2 #4A2F5C               jamuni
```
**Contrast:** ink/paper **14.63** · ink/card 15.93 · ink/tint-1 10.11 · ink/tint-2 11.75 · ink/tint-3 10.67 · muted/paper **5.30** · paper/ground **12.97** · paper/ground-2 11.11 · ink/marker 9.45 · accent-1/paper 6.39 · accent-2/paper 9.82. All body-text pairs pass 4.5:1.

**Type:** display **Bodoni Moda**, body **Mukta Vaani**, labels **DM Mono**, no hand.
**Texture:** silk sheen on the motif; fine horizontal thread lines (1px every 3px at 3%) on tint blocks.
**Motion:** smooth and horizontal. Sweep, then settle into focus.
**Reference:** [V&A IS.189-1960, Patola sari, Patan (c. 1900 to 1920)](https://collections.vam.ac.uk/item/O477926/patola-sari/): double ikat silk.

---
