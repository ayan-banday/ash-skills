# Transit map · "the network"

**Picture it:** three coloured lines that run only straight or at 45 degrees, with station ticks, crossing at one bold ringed interchange.
**Swatch:** `#2A2522 #F3F0E9 #F2DE9C #C2D5E8 #E3C2D3 #BC3429`

**Suits:** mobility, logistics, smart cities, multi-workstream programmes, onboarding journeys, education pathways, platforms and ecosystems, consulting roadmaps. Tone: clear, purposeful, modern. Audience: everyone. The most readable direction for people who will not read.
**Avoid when:** an emotional heritage story; a brand that already uses a metro-map cliché.
**Cultural note:** Harry Beck's 1933 London Underground diagram, which borrowed from electrical circuit diagrams. Never copy TfL's roundel, line names or exact line colours (trademarks); use this palette.

**Story device.** Lines are workstreams, one colour per need; stations are milestones; interchanges are integration points; the central hub is the client. A "you are here" dot can travel to the current section's station.
**Badge:** one line in colour (`s1`, `s2`, `s3`), the others faint; the hub is `core`.

**SVG recipe**
- **Geometry:** waypoints on a 20px grid with only 0, 45 and 90-degree segments; corners rounded with a quadratic at each bend (r16); a tick at each segment's midpoint along the normal; interchanges as rings.
- **Stroke stack:** a 14px background casing under an 8px line, so crossings separate cleanly; ticks 4px with butt caps.
- **Texture:** none, or printed-map grain at 3%.
- **Draw-on:** each line draws at constant speed like a train (linear, duration = length ÷ 0.35px per ms), lines 250ms apart; then interchange rings pop (scale 0.6 to 1, 240ms ease-out-back). Optional train dot via `getPointAtLength`.
- **Complexity:** 13 paths, 3 KB of SVG, 0.15 ms to generate in Node, 0 filters on the hero.

```js
function transit(o = {}) {
  const round = (pts, rr = 16) => { let d = `M${K.P(...pts[0])}`;            // rounded corners at each bend
    for (let i = 1; i < pts.length - 1; i++) { const [a, b, c] = [pts[i - 1], pts[i], pts[i + 1]];
      const u = (p, q) => { const L = Math.hypot(q[0] - p[0], q[1] - p[1]); return [(q[0] - p[0]) / L, (q[1] - p[1]) / L]; };
      const u1 = u(b, a), u2 = u(b, c); d += `L${K.P(b[0] + u1[0] * rr, b[1] + u1[1] * rr)}Q${K.P(...b)} ${K.P(b[0] + u2[0] * rr, b[1] + u2[1] * rr)}`; }
    return d + `L${K.P(...pts[pts.length - 1])}`; };
  const lines = [
    { id: 's1', col: 'var(--f1)', pts: [[20, 120], [100, 120], [180, 200], [260, 200], [320, 260], [380, 260]] },
    { id: 's2', col: 'var(--f2)', pts: [[200, 20], [200, 120], [220, 140], [220, 200], [220, 300], [160, 360], [60, 360]] },
    { id: 's3', col: 'var(--f3)', pts: [[40, 340], [120, 260], [180, 260], [240, 200], [300, 140], [380, 140]] }];
  const ticks = l => { let d = ''; for (let i = 0; i < l.pts.length - 1; i++) { const [a, b] = [l.pts[i], l.pts[i + 1]], mx = (a[0] + b[0]) / 2, my = (a[1] + b[1]) / 2;
    const L = Math.hypot(b[0] - a[0], b[1] - a[1]), nx = -(b[1] - a[1]) / L, ny = (b[0] - a[0]) / L; d += `M${K.P(mx, my)}L${K.P(mx + nx * 9, my + ny * 9)}`; } return d; };
  const inner = lines.map((l, i) => K.part(l.id, K.stack(round(l.pts), [{ c: 'var(--bgc)', w: 14 }, { c: l.col, w: 8 }], i) + K.stack(ticks(l), [{ c: l.col, w: 4, cap: 'butt' }], i))).join('')
    + K.part('core', K.fill(K.circ(220, 200, 13), 'var(--m3)') + K.stack(K.circ(220, 200, 13), [{ c: 'var(--m1)', w: 4 }], 3))
    + K.fill(K.circ(120, 260, 8) + K.circ(300, 140, 8), 'var(--m3)') + K.stack(K.circ(120, 260, 8) + K.circ(300, 140, 8), [{ c: 'var(--m1)', w: 3 }], 3);
  return { w: 400, h: 400, defs: '', inner };
}
```

**Hero slots:** `--bgc` paper · `--m1` ink · `--m2` line · `--m3` card · `--f1` accent-1 · `--f2` accent-2 · `--f3` marker

**Palette:**
```
--ground   #2A2522               platform
--ground-2 #3A3330               platform-2
--paper    #F3F0E9               map-paper
--card     #FBFAF6               card
--ink      #1F1B19               ink
--muted    #645E5A               muted
--line     rgba(31,27,25,.14)    line
--tint-1   #F2DE9C               line-yellow-chalk   OKLCH L 0.90 C 0.087 h 93
--tint-2   #C2D5E8               line-sky-chalk   OKLCH L 0.86 C 0.033 h 248
--tint-3   #E3C2D3               line-magenta-chalk   OKLCH L 0.85 C 0.044 h 346
--marker   #F5CC3A               line-yellow
--accent-1 #BC3429               line-red
--accent-2 #1F3F95               line-blue
```
**Contrast:** ink/paper **15.01** · ink/card 16.36 · ink/tint-1 12.78 · ink/tint-2 11.37 · ink/tint-3 10.51 · muted/paper **5.61** · paper/ground **13.31** · paper/ground-2 10.88 · ink/marker 11.05 · accent-1/paper 5.04 · accent-2/paper 8.37. All body-text pairs pass 4.5:1.

**Type:** display **Overpass**, body **Atkinson Hyperlegible**, labels **Overpass Mono**, no hand.
**Texture:** none.
**Motion:** purposeful, constant speed, punctual.
**Reference:** [V&A E.815-1979, London Underground map by Harry Beck (1933)](https://collections.vam.ac.uk/item/O1067382/london-underground-map-print-beck-harry/): vertical, horizontal and diagonal lines only, inspired by circuit diagrams.

---
