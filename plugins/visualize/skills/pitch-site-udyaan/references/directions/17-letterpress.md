# Letterpress · "the front page"

**Picture it:** a newspaper front page: thick-thin rules, a heavy headline, three ruled columns and a boxed "stop press" with a pointing hand.
**Swatch:** `#24201D #EFEADF #E6DCC4 #F0CDBE #CDD3DD #B8302A`

**Suits:** media and publishing, PR, launches and announcements, universities, public-sector reports, research findings, annual results. Tone: authoritative, newsy, decisive. Audience: leaders who read headlines only, which makes it ideal for non-readers.
**Avoid when:** soft wellness briefs; visual product demos.
**Cultural note:** the newspaper and wood-type tradition, shared by Indian-language papers. Never imitate a real paper's masthead (impersonation).

**Story device.** The headline is the single promise; the three columns are the three needs; the boxed stop press with the pointing hand is the ask (the decision needed); the dateline is the timeline.
**Badge:** one column inked (`s1`, `s2`, `s3`), the headline (`core`) or the box (`ask`).

**SVG recipe**
- **Geometry:** 6px plus 1.5px thick-thin rules; a headline bar, or real `<text>` in the display font (pass `title`); column text as 3.2px bars every 9px with the last line at 60%; column rules; a double-bordered box.
- **Stroke stack:** mostly fills; the box is 3px plus a 1px inner line.
- **Texture filter:** ink squeeze (an eroded alpha rim darkened 35%) inside speckle dropouts; a newsprint-fibre overlay at 6%; a slight deboss on cards (inset highlight and shadow of 1px).
- **Draw-on:** "press kiss": blocks appear with scale 1.012 to 1 and opacity in 140ms ease-out, 70ms apart, top to bottom, headline first.
- **Complexity:** 13 paths, 3.2 KB of SVG, 0.11 ms to generate in Node, 2 filters on the hero. Two nested filters over the block: moderate cost, keep it to the hero.

```js
function letterpress(o = {}) {
  const bars = (x, y, w, n, lh = 9) => { let d = ''; for (let i = 0; i < n; i++) d += `M${x} ${y + i * lh}h${i === n - 1 ? w * .6 : w}v3.2h${-(i === n - 1 ? w * .6 : w)}z`; return d; };
  const head = o.title ? `<text x="200" y="74" text-anchor="middle" style="font:44px var(--font-display);fill:var(--m1)">${o.title}</text>` : K.fill('M60 46H340V80H60Z', 'var(--m1)');
  const inner = K.fill('M20 20H380V26H20ZM20 30H380V31.5H20Z', 'var(--m1)') + K.part('core', head + K.fill('M90 92H310V100H90Z', 'var(--m1)', 'opacity=".55"'))
    + K.fill('M20 112H380V113.5H20ZM20 116H380V120H20Z', 'var(--m1)')
    + [0, 1, 2].map(i => K.part('s' + (i + 1), K.fill(`M${24 + i * 120} 134h108v18h-108z`, 'var(--m1)') + K.fill(bars(24 + i * 120, 164, 108, 18), 'var(--m1)', 'opacity=".55"'))).join('')
    + K.fill('M138 134h1v240h-1zM258 134h1v240h-1z', 'var(--m1)')
    + K.part('box', K.stack('M150 300h100v74h-100z', [{ c: 'var(--m1)', w: 3 }], 0) + K.stack('M156 306h88v62h-88z', [{ c: 'var(--m1)', w: 1 }], 0) + `<text x="200" y="346" text-anchor="middle" style="font:22px var(--font-display);fill:var(--f1)">&#9758;</text>`, 'data-group="ask"');
  return { w: 400, h: 400, defs: o.badge ? '' : FX.squeeze('press') + FX.speckle('nspk', 1.4, 8), inner: o.badge ? inner : `<g filter="url(#nspk)"><g filter="url(#press)">${inner}</g></g>` };
}
```

**Hero slots:** `--bgc` paper · `--m1` ink · `--m2` line · `--m3` card · `--f1` accent-1 · `--f2` accent-2 · `--f3` marker

**Palette:**
```
--ground   #24201D               press-ink
--ground-2 #322D29               press-ink-2
--paper    #EFEADF               newsprint
--card     #F8F5EE               card
--ink      #1C1916               ink
--muted    #615A53               muted
--line     rgba(28,25,22,.14)    line
--tint-1   #E6DCC4               aged-newsprint   OKLCH L 0.90 C 0.034 h 88
--tint-2   #F0CDBE               sporting-pink   OKLCH L 0.87 C 0.045 h 45
--tint-3   #CDD3DD               proof-blue   OKLCH L 0.86 C 0.015 h 261
--marker   #F2D45C               proof-yellow
--accent-1 #B8302A               spot-red
--accent-2 #24518F               process-blue
```
**Contrast:** ink/paper **14.59** · ink/card 16.07 · ink/tint-1 12.83 · ink/tint-2 11.82 · ink/tint-3 11.63 · muted/paper **5.65** · paper/ground **13.47** · paper/ground-2 11.34 · ink/marker 11.96 · accent-1/paper 5.01 · accent-2/paper 6.61. All body-text pairs pass 4.5:1.

**Type:** display **Abril Fatface**, masthead only **UnifrakturMaguntia** (one use), body **Libre Caslon Text**, labels **Courier Prime**.
**Texture:** newsprint fibre and speckle; deboss on cards.
**Motion:** decisive, short, percussive.
**Reference:** [Hamilton Wood Type & Printing Museum, About](https://woodtype.org/pages/about): about 1.5 million pieces of wood type, a working letterpress museum.

---
