# Circuit · "copper on Kapton"

**Picture it:** copper traces fanning out at 45 degrees from a black chip across amber polyimide film, ending in gold pads.
**Swatch:** `#2A211C #F2EEE6 #F0D2A0 #CDD3DE #E9C1AD #A04A28`

**Suits:** semiconductors, EV and automotive electronics, IoT, AI and data infrastructure, deep tech, telecom, integration-heavy SaaS. Tone: precise, energetic, technical. Audience: CTOs, engineers, investors.
**Avoid when:** the client expects a green PCB (Ash rejects green: this uses amber Kapton); non-technical, warm briefs.
**Cultural note:** none. Paul Eisler's 1942 radio used the first printed circuit boards.

**Story device.** The chip is the client's core; its pins are the interfaces; each side's traces are a workstream; the pads are deliverables; pulses running along a trace are value flowing.
**Badge:** one side's traces in copper with a pulse (`s1` to `s4`), or the chip (`core`).

**SVG recipe**
- **Geometry:** a 100px IC body; four pins per side, generated once and rotated 0, 90, 180, 270; each trace has three segments (straight 20px, a 45-degree diagonal, straight to the pad); vias at the bends.
- **Stroke stack:** 6px dark mask edge, 3.6px copper, 1px highlight at 50%.
- **Texture:** Kapton translucency (fractalNoise .02 at 5% amber variation on the board); a low-frequency noise on copper for oxidation (never a green patina).
- **Draw-on:** traces draw from the chip outward (600ms ease-in-out) one side at a time, 120ms apart; then marker-coloured pulses run along traces via `getPointAtLength` (700ms ease-in-out, every 3s).
- **Complexity:** 39 paths, 8.1 KB of SVG, 0.16 ms to generate in Node, 0 filters on the hero.

```js
function circuit(o = {}) {
  const c = 200, cu = o.badge ? [{ c: 'var(--m1)', w: 3 }] : [{ c: 'var(--m2)', w: 6 }, { c: 'var(--m1)', w: 3.6 }, { c: 'var(--m3)', w: 1, o: .5 }];
  const groups = { s1: '', s2: '', s3: '', s4: '' }, pads = { s1: '', s2: '', s3: '', s4: '' }; let pins = '';
  for (let side = 0; side < 4; side++) for (let i = 0; i < 4; i++) {
    const off = -27 + i * 18, rot = side * 90, R = (x, y) => { const a = rot * Math.PI / 180; return [c + x * Math.cos(a) - y * Math.sin(a), c + x * Math.sin(a) + y * Math.cos(a)]; };
    const p0 = R(off, -50), p1 = R(off, -70), p2 = R(off + (off < 0 ? -1 : 1) * (40 + Math.abs(off)), -110 - Math.abs(off)), p3 = R(off + (off < 0 ? -1 : 1) * (40 + Math.abs(off)), -150);
    pins += K.fill(`M${K.P(...R(off - 4, -50))}L${K.P(...R(off + 4, -50))}L${K.P(...R(off + 4, -38))}L${K.P(...R(off - 4, -38))}Z`, 'var(--m3)');
    groups['s' + (side + 1)] += K.pl([p0, p1, p2, p3]); pads['s' + (side + 1)] += K.circ(...p3, 7) + K.circ(...p2, 3.5);
  }
  const inner = K.fill(`M0 0H400V400H0Z`, 'var(--bgc)')
    + Object.keys(groups).map((s, i) => K.part(s, K.stack(groups[s], cu, i) + K.fill(pads[s], 'var(--f1)') + K.stack(pads[s], [{ c: 'var(--m1)', w: 2 }], i))).join('')
    + K.part('core', K.fill('M150 150H250V250H150Z', 'var(--m2)') + pins + K.fill(K.circ(162, 162, 4), 'var(--m3)') + `<text x="200" y="205" text-anchor="middle" style="font:12px var(--font-label);fill:var(--m3)">U1</text>`);
  return { w: 400, h: 400, defs: '', inner };
}
```

**Hero slots:** `--bgc` tint-1 · `--m1` accent-1 · `--m2` ground-2 · `--m3` marker · `--f1` marker · `--f2` tint-2 · `--f3` tint-3

**Palette:**
```
--ground   #2A211C               conformal
--ground-2 #3A2E26               conformal-2
--paper    #F2EEE6               silkscreen
--card     #FAF8F3               card
--ink      #211B17               ink
--muted    #675D55               muted
--line     rgba(33,27,23,.14)    line
--tint-1   #F0D2A0               kapton   OKLCH L 0.88 C 0.073 h 80
--tint-2   #CDD3DE               solder   OKLCH L 0.87 C 0.017 h 263
--tint-3   #E9C1AD               copper-wash   OKLCH L 0.84 C 0.054 h 48
--marker   #EBC24E               gold-pad
--accent-1 #A04A28               copper
--accent-2 #2D55A8               status-blue
```
**Contrast:** ink/paper **14.71** · ink/card 16.04 · ink/tint-1 11.70 · ink/tint-2 11.32 · ink/tint-3 10.29 · muted/paper **5.54** · paper/ground **13.62** · paper/ground-2 11.35 · ink/marker 10.02 · accent-1/paper 5.18 · accent-2/paper 6.10. All body-text pairs pass 4.5:1.

**Type:** display **Space Grotesk**, body **IBM Plex Sans**, labels **Martian Mono** (silkscreen feel), no hand.
**Texture:** Kapton translucency on the board; paper grain elsewhere.
**Motion:** crisp, fast, electric. One pulse travels the trace being discussed (MOT-01), then stops.
**Reference:** [Science Museum Group, Paul Eisler (1907 to 1995)](https://collection.sciencemuseumgroup.org.uk/people/cp39953/paul-eisler): credited with the first printed circuit board, in a 1942 radio.

---
