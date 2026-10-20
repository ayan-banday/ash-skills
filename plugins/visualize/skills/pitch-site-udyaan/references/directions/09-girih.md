# Girih · "the ten-fold star"

**Picture it:** a ten-pointed star with interlaced double-line strapwork, a ring of kites and small stars at the edge, in lapis on stucco.
**Swatch:** `#33241F #F2EDE3 #C5CCE3 #EBD5A8 #E2BBA6 #2F3F86`

**Suits:** architecture, mathematics and data, engineering, universities, heritage, Islamic finance, clients in the Middle East, Central Asia or North Africa, Islamic-heritage institutions. Tone: ordered, deep, timeless. Audience: senior leaders, academics, government.
**Avoid when:** a playful brand; alcohol, gambling or similar (an offensive pairing); any request to add Arabic script as decoration.
**Cultural note:** geometric pattern is one of the main non-figural decorative traditions of Islamic art; girih tilings developed between the 13th and 15th centuries and reached near quasi-crystalline order at the Darb-i Imam shrine in Isfahan. Fitting with a regional, institutional or mathematical tie. Use geometry only, never Arabic text as ornament (it may be sacred), no mosque silhouettes. It becomes appropriation as "Arabian nights" decoration.

**Story device.** One rule, an infinite pattern. The centre star is the client's vision; the ten kites are ten principles; the outer stars are the places the pattern meets the world (markets, campuses). Because the pattern can tile forever, it argues for scale.
**Badge:** one kite per principle section (`p1` to `p10`), the star (`core`), or the outer ring (`s1`).

**SVG recipe**
- **Geometry:** ten vertices on r70; the star polygon joins vertex k to k+3 ({10/3}); kites between r70 and r132 (shoulders on r108 at ±18 degrees); five-point stars on r162. Dashed construction circles (r70, r132, r162) at 30%.
- **Stroke stack:** strapwork 7px lapis with a 3.4px background-coloured line inside, which makes the double line. For true over-under, split each line at its crossings and alternate which casing sits on top.
- **Texture:** a 6% radial glaze sheen per kite; stucco grain on paper.
- **Draw-on:** compass first: construction circles fade in (400ms); star lines draw from the centre outward in symmetric pairs, 1.2s ease-in-out-sine; kites fill after.
- **Complexity:** 36 paths, 10.2 KB of SVG, 0.22 ms to generate in Node, 0 filters on the hero.

```js
function girih(o = {}) {
  const c = 200, v = [...Array(10)].map((_, k) => K.pt(c, c, 70, k * 36 - 90));
  const star = v.map((p, k) => K.seg(p, v[(k + 3) % 10])).join('');
  const kites = [...Array(10)].map((_, k) => K.poly([K.pt(c, c, 70, k * 36 - 90), K.pt(c, c, 108, k * 36 - 108), K.pt(c, c, 132, k * 36 - 90), K.pt(c, c, 108, k * 36 - 72)]));
  const st5 = (x, y, R) => K.poly([...Array(10)].map((_, k) => K.pt(x, y, k % 2 ? R * .45 : R, k * 36 - 90)));
  const outer = [...Array(10)].map((_, k) => st5(...K.pt(c, c, 162, k * 36 - 72), 20)).join('');
  const strap = o.badge ? [{ c: 'var(--m1)', w: 4 }] : [{ c: 'var(--m1)', w: 7 }, { c: 'var(--bgc)', w: 3.4 }];
  const guides = o.badge ? '' : K.stack(K.circ(c, c, 70) + K.circ(c, c, 132) + K.circ(c, c, 162), [{ c: 'var(--m1)', w: .6, o: .3, dash: '3 5' }], 0);
  const inner = guides + kites.map((d, k) => K.part('p' + (k + 1), K.fill(d, k % 2 ? 'var(--f1)' : 'var(--f2)') + K.stack(d, strap, 2), 'data-group="principles"')).join('')
    + K.part('core', K.stack(star, strap, 1)) + K.part('s1', K.fill(outer, 'var(--f3)') + K.stack(outer, strap, 3));
  return { w: 400, h: 400, defs: '', inner };
}
```

**Hero slots:** `--bgc` paper · `--m1` accent-1 · `--m2` line · `--m3` card · `--f1` tint-1 · `--f2` tint-2 · `--f3` marker

**Palette:**
```
--ground   #33241F               brick-shadow
--ground-2 #432F28               brick-2
--paper    #F2EDE3               stucco
--card     #FAF7F0               plaster
--ink      #22191A               ink
--muted    #6B5E5A               muted
--line     rgba(34,25,26,.14)    line
--tint-1   #C5CCE3               lapis-wash   OKLCH L 0.85 C 0.033 h 272
--tint-2   #EBD5A8               saffron-stucco   OKLCH L 0.88 C 0.064 h 85
--tint-3   #E2BBA6               brick-wash   OKLCH L 0.82 C 0.054 h 50
--marker   #E9C259               gilt
--accent-1 #2F3F86               lapis
--accent-2 #9A2E3C               pomegranate
```
**Contrast:** ink/paper **14.73** · ink/card 16.06 · ink/tint-1 10.74 · ink/tint-2 11.96 · ink/tint-3 9.73 · muted/paper **5.33** · paper/ground **12.74** · paper/ground-2 10.74 · ink/marker 10.09 · accent-1/paper 8.27 · accent-2/paper 6.36. All body-text pairs pass 4.5:1.
Turquoise, the classic girih glaze, is left out because it falls in the green band.

**Type:** display **Reem Kufi**, body **Readex Pro**, labels **Noto Sans Mono**, hand **Aref Ruqaa** (only to set a real name in Arabic, checked by a native reader).
**Texture:** stucco grain, glaze sheen.
**Motion:** measured, symmetric, inevitable.
**Reference:** [Paul Steinhardt, "Islamic Tilings" (Princeton)](https://paulsteinhardt.org/islamic-tilings/): girih from the 13th to 15th centuries, Darb-i Imam, and Lu and Steinhardt, Science 315 (2007).

---
