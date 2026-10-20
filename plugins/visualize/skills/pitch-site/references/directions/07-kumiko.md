# Kumiko · "the lattice"

**Picture it:** a glowing hexagon of fine cedar lattice with hemp-leaf stars in every triangle, lit softly from behind like a paper screen.
**Swatch:** `#2B2522 #F3EFE6 #E9D9BE #E3C6B3 #D6CEDC #A8353A`

**Suits:** architecture, engineering, premium manufacturing, real estate, hospitality, wellness, enterprise software with a precision story, consulting. Tone: quiet, exact, premium. Audience: executives, architects, engineers.
**Avoid when:** a loud consumer brand; a Japanese client who would read it as faux-Japan.
**Cultural note:** kumiko is Japanese joinery, with roots in the Asuka period, that assembles thin wooden strips without nails; it is widely taught and used in contemporary design. Fitting for precision and fit stories. Use the geometry and the idea of nail-free fit; skip faux-Japanese tropes (brush fonts, random kanji, cherry blossoms). Low appropriation risk when credited.

**Story device.** Frame and fill. The frame is the client's existing structure; each hemp-leaf infill is a capability we add, and it fits without nails: no disruption. The six innermost triangles form the core hexagon (the client's core team); the six sectors are six workstreams.
**Badge:** the lattice with one sector's infill lit (`s1` to `s6`) or the core.

**SVG recipe**
- **Geometry:** a hexagon R180 split into six triangles, each subdivided into n² small triangles (n = 3; badges use n = 2). The frame is every small triangle's outline; the infill is three lines from each vertex to the centroid (the hemp leaf, asanoha).
- **Stroke stack:** frame 4.6px shadow, 3px wood, 0.8px highlight offset (-0.6, -0.6) for a bevel; infill 2.6px shadow under 1.6px wood.
- **Texture:** a radial "lamp" gradient behind the lattice (marker colour to transparent); at large sizes the anisotropic woodgrain filter (noise .012 by .45) on the strips.
- **Draw-on:** frame first (600ms), then infill lines slide in per sector, 450ms, cubic-bezier(.2,.7,.2,1), 60ms stagger.
- **Complexity:** 17 paths, 14.1 KB of SVG, 0.47 ms to generate in Node, 0 filters on the hero.

```js
function kumiko(o = {}) {
  const c = 200, R = 180, n = o.badge ? 2 : 3, parts = { core: '' }, frame = [];
  for (let s = 0; s < 6; s++) {                                     // 6 big triangles, each split into n*n small ones
    parts['s' + (s + 1)] = '';
    const A = [c, c], B = K.pt(c, c, R, s * 60 - 90), C = K.pt(c, c, R, s * 60 - 30);
    const at = (i, j) => [A[0] + (B[0] - A[0]) * i / n + (C[0] - B[0]) * j / n, A[1] + (B[1] - A[1]) * i / n + (C[1] - B[1]) * j / n];
    for (let i = 0; i < n; i++) for (let j = 0; j <= i; j++) {
      const tris = [[at(i, j), at(i + 1, j), at(i + 1, j + 1)]]; if (j < i) tris.push([at(i, j), at(i + 1, j + 1), at(i, j + 1)]);
      tris.forEach(t => { const g = [(t[0][0] + t[1][0] + t[2][0]) / 3, (t[0][1] + t[1][1] + t[2][1]) / 3];
        frame.push(K.poly(t)); const leaf = t.map(v => K.seg(v, g)).join('');
        if (i === 0) parts.core += leaf; else parts['s' + (s + 1)] += leaf; });
    }
  }
  const glow = o.badge ? '' : `<circle cx="${c}" cy="${c}" r="${R}" style="fill:url(#lamp)"/>`;
  const F = o.badge ? [{ c: 'var(--m1)', w: 3 }] : [{ c: 'var(--m2)', w: 4.6 }, { c: 'var(--m1)', w: 3 }, { c: 'var(--m3)', w: .8, o: .5, t: '-.6 -.6' }];
  const I = o.badge ? [{ c: 'var(--m1)', w: 2 }] : [{ c: 'var(--m2)', w: 2.6 }, { c: 'var(--m1)', w: 1.6 }];
  const inner = glow + `<g class="frame">${K.stack(frame.join(''), F, 0)}</g>` + Object.keys(parts).map((p, i) => K.part(p, K.stack(parts[p], I, 1 + i))).join('');
  return { w: 400, h: 400, defs: `<radialGradient id="lamp"><stop offset="0" style="stop-color:var(--f1);stop-opacity:.9"/><stop offset="1" style="stop-color:var(--f1);stop-opacity:0"/></radialGradient>`, inner };
}
```

**Hero slots:** `--bgc` ground · `--m1` tint-1 · `--m2` ground-2 · `--m3` card · `--f1` marker · `--f2` tint-2 · `--f3` tint-3

**Palette:**
```
--ground   #2B2522               yakisugi
--ground-2 #3A322D               yakisugi-2
--paper    #F3EFE6               washi
--card     #FAF8F2               shoji
--ink      #221E1B               sumi
--muted    #6A625B               nezumi
--line     rgba(34,30,27,.14)    line
--tint-1   #E9D9BE               hinoki   OKLCH L 0.89 C 0.040 h 81
--tint-2   #E3C6B3               sugi   OKLCH L 0.85 C 0.042 h 55
--tint-3   #D6CEDC               fuji-nezumi   OKLCH L 0.86 C 0.021 h 311
--marker   #F1CF7A               andon
--accent-1 #A8353A               beni
--accent-2 #34466E               ai
```
**Contrast:** ink/paper **14.41** · ink/card 15.58 · ink/tint-1 11.92 · ink/tint-2 10.24 · ink/tint-3 10.81 · muted/paper **5.21** · paper/ground **13.16** · paper/ground-2 10.93 · ink/marker 10.99 · accent-1/paper 5.66 · accent-2/paper 8.14. All body-text pairs pass 4.5:1.

**Type:** display **Shippori Mincho B1**, body **Zen Kaku Gothic New**, labels **IBM Plex Mono**, hand **Klee One**.
**Texture:** washi fibre overlay on paper (fractalNoise ".01 .3" at 5%); the lamp glow on ground.
**Motion:** quiet and exact. Ease-out, no overshoot; the backlight breathes between 0.9 and 1 over 6s.
**Reference:** [Tanihata, "About Kumiko"](https://kumikowoodworking.com/takumi/kumiko/index.htm) (redirected from tanihata.co.jp): nail-free assembly; a 1000×2000mm hemp-leaf panel has 3,496 parts.

---
