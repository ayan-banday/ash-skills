# Truck art · "the tailgate"

**Picture it:** a hand-painted lorry tailgate: an enamel-blue arch, a red flower medallion, yellow plates, diamond reflector tape and a chain fringe.
**Swatch:** `#2F2420 #F3EEE6 #F0D99A #BFD3E3 #EDC0CC #B5302B`

**Suits:** automotive and two-wheelers, logistics, mobility, highways, food delivery, rural distribution, festivals, Indian consumer brands with swagger. Tone: loud, proud, playful. Audience: dealers, drivers, young consumers, marketing teams.
**Avoid when:** conservative boards, healthcare, legal; any context where it could read as mocking "chaotic India".
**Cultural note:** truck art is a living vernacular of self-taught painters across India and Pakistan; each state has its own style and lettering, and stickers are replacing the painters. Fitting when the project serves drivers, roads or vehicles, or celebrates Indian street craft. Celebrate and credit the painters, commission hand lettering for the hero when possible, keep out religious and political slogans, and never use "Horn OK Please" as a punchline. It becomes appropriation as a kitsch "Indian chaos" skin for a brand with no tie.

**Story device.** The tailgate is the proposal. The arch is the promise; the centre medallion is the client; the three plates are the three needs (their labels are painted on); the chain fringe is the timeline, one link per milestone; the reflector band is the guarantees.
**Badge:** one plate (`s1`, `s2`, `s3`), the medallion (`core`), or the current chain link (`m1` to `m8`; `timeline` lights all).

**SVG recipe**
- **Geometry:** a pointed arch from two quadratics; 18 scallops; a 12-petal medallion; 3 plates; a band of 14 rhombi; 8 chain links. Pass `labels: ['Skills','Plant','Pipeline']` to paint text on the plates.
- **Stroke stack:** enamel = flat fill, 3px ink outline, and a 1px paper highlight offset (-1.5, -1.5) for gloss.
- **Texture:** an 8% white linear gradient on fills for enamel sheen; a fine noise mask with animated opacity for reflector sparkle; road dust at 4%.
- **Draw-on:** snappy. Plates arrive one by one (opacity and a 12px rise, 380ms, cubic-bezier(.22,1,.36,1)); the medallion petals pen-draw; chain links arrive 60ms apart. No overshoot.
- **Complexity:** 45 paths, 7.5 KB of SVG, 0.21 ms to generate in Node, 0 filters on the hero.

```js
function truckart(o = {}) {
  const c = 200; let scal = '', dia = '', chain = '', petals = '';
  for (let x = 20; x < 380; x += 20) scal += `M${x} 20A10 10 0 0 0 ${x + 20} 20`;
  for (let i = 0; i < 14; i++) { const x = 32 + i * 24.5; dia += K.fill(K.poly([[x, 312], [x + 12, 300], [x + 24, 312], [x + 12, 324]]), i % 2 ? 'var(--f1)' : 'var(--f2)'); }
  for (let k = 0; k < 12; k++) { const t = K.pt(c, 150, 62, k * 30 - 90), l = K.pt(c, 150, 30, k * 30 - 108), r = K.pt(c, 150, 30, k * 30 - 72);
    petals += `M${K.P(c, 150)}Q${K.P(l[0], l[1])} ${K.P(t[0], t[1])}Q${K.P(r[0], r[1])} ${K.P(c, 150)}Z`; }
  const arch = 'M50 290V150Q50 70 200 34Q350 70 350 150V290Z';
  const plates = [0, 1, 2].map(i => K.part('s' + (i + 1), K.fill(`M${62 + i * 94} 236h88v40h-88z`, 'var(--f3)') + K.stack(`M${62 + i * 94} 236h88v40h-88z`, [{ c: 'var(--m1)', w: 2.5 }], 2 + i)
    + (o.labels ? `<text x="${106 + i * 94}" y="262" text-anchor="middle" style="font:700 13px var(--font-label);fill:var(--m1)">${o.labels[i]}</text>` : ''))).join('');
  for (let i = 0; i < 8; i++) chain += K.part('m' + (i + 1), K.stack(K.circ(46 + i * 44, 352, 9), [{ c: 'var(--m1)', w: 3 }], 6) + K.stack(`M${55 + i * 44} 352H${81 + i * 44}`, [{ c: 'var(--m1)', w: 2 }], 6), 'data-group="timeline"');
  const inner = K.fill('M10 10H390V390H10Z', 'var(--bgc)') + K.stack(scal, [{ c: 'var(--f1)', w: 5 }], 0) + K.fill(arch, 'var(--f2)') + K.stack(arch, [{ c: 'var(--m1)', w: 3 }, { c: 'var(--m3)', w: 1, o: .6, t: '-1.5 -1.5' }], 1)
    + K.part('core', K.fill(petals, 'var(--f1)') + K.stack(petals, [{ c: 'var(--m1)', w: 2 }], 2) + K.fill(K.circ(c, 150, 16), 'var(--f3)') + K.stack(K.circ(c, 150, 16), [{ c: 'var(--m1)', w: 2 }], 2))
    + plates + dia + chain;
  return { w: 400, h: 400, defs: '', inner };
}
```

**Hero slots:** `--bgc` paper · `--m1` ink · `--m2` line · `--m3` card · `--f1` accent-1 · `--f2` accent-2 · `--f3` marker

**Palette:**
```
--ground   #2F2420               chassis
--ground-2 #3D2F29               chassis-2
--paper    #F3EEE6               primer
--card     #FBF8F2               card
--ink      #221B18               enamel-black
--muted    #685D56               road-dust
--line     rgba(34,27,24,.14)    line
--tint-1   #F0D99A               tailgate   OKLCH L 0.89 C 0.084 h 90
--tint-2   #BFD3E3               sky-enamel   OKLCH L 0.86 C 0.031 h 242
--tint-3   #EDC0CC               rose-enamel   OKLCH L 0.85 C 0.054 h 1
--marker   #F5C83A               reflector
--accent-1 #B5302B               lorry-red
--accent-2 #2C55A0               cab-blue
```
**Contrast:** ink/paper **14.69** · ink/card 16.00 · ink/tint-1 12.19 · ink/tint-2 11.02 · ink/tint-3 10.51 · muted/paper **5.53** · paper/ground **13.04** · paper/ground-2 11.11 · ink/marker 10.67 · accent-1/paper 5.31 · accent-2/paper 6.24. All body-text pairs pass 4.5:1.

**Type:** display **Shrikhand** (a Gujarati and Latin display face with a hand-lettered feel), body **Mukta**, labels **Rajdhani** (uppercase, tracked +6%), no hand (the display is the lettering).
**Texture:** enamel sheen and sparkle on the motif; paper grain on paper.
**Motion:** quick and cheerful, the fastest tempo the house rules allow. The loudness lives in colour, shape and lettering; motion never bounces. The fringe sways ±3 degrees once on hover or tap.
**Reference:** [Homegrown, "This Collective Is Taking India's Unique Truck Art To The World"](https://homegrown.co.in/homegrown-voices/this-collective-is-taking-indias-unique-truck-art-to-the-world): All India Permit, painters on steel, state-by-state lettering.

---
