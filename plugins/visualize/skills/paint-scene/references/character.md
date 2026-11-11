# Character: the level per case, and the Watercolour look

Open on every run. "The level per case" and "Clarity rules" cover both looks; the rest is the Watercolour look. Ring Eyes has its own file, `ring-eyes.md`. The Watercolour parts are listed by name; the gallery (`gallery.html`) shows each one. `python scripts/kit.py list` prints the same names.

## Contents
- The level per case
- Clarity rules
- The menu
- Touch recipes (ink.css)
- Scene settings (ink.js)
- Commission: making new parts

## The level per case

**Ash's decisions, Nov 11 2026.** The case comes from match-ash-design's table.

| Case | Level | Asked? |
|---|---|---|
| Ash's own pages: study pages, books, his tools, week page | **Touch at most, often nothing** | Never asked |
| Briefs, pitches, business messages (Udyaan included), slides, posts | None, Touch or Scene | One question inside the building skill's own questions |
| Printed documents | **Grain and hatching only** | Same question, print answers |
| Anything, when Ash says "commission", "paint it", "go heavy" | **Commission** | His words are the answer |

- **Udyaan is a business project,** so it follows the "for others" row. **Character art never takes the Udyaan brand colours:** its tokens come from `palette.py` even on an Udyaan post or pitch. (match-ash-design's "Udyaan brand wins" covers the course pages students read, not the art.)
- **The question** Ash sees, one line added to the building skill's intake (never a separate prompt): "Character: none, Touch or Scene; and the look, Watercolour (blooms and light) or Ring Eyes (flat colour, ring-eyed characters, one huge word)?" Defaults when he skips it: Touch on pages, Scene on post cards and slide covers; the look by "Ring Eyes or Watercolour" in `ring-eyes.md`.
- **Ash's own pages are never asked:** Watercolour Touch at most, or one small Ring Eyes mark in an empty state.

## Clarity rules

1. **A picture explains something.** Run match-ash-design's "When to draw, when to write" and its two covered tests first. A Scene that fails them becomes a Touch or nothing.
2. **One bloom per screen. One kind of light per screen.**
3. **The light points at the one message:** the decision line, the ball, the figure doing the thing. Light on nothing is decoration; cut it.
4. **Text never sits on a bloom.** ink.css keeps a heading bloom past the last word; ink.js warns (`canvas.dataset.inkWarn`, and `kit.py` prints it) when the title box meets the bloom. Light steps and grain may sit under text; they are quiet.
5. **The ball is the one bright thing,** with the marker's meaning: what the reader gets or decides. One ball per screen, and no other coral or hot accent fighting it (pick a palette with `--no-red` on Ash's pages when the accent is pink or coral).
6. **Contours are for one hero piece only,** never on every frame. Ash rejected rings everywhere (Nov 11 2026). Steps is the default light.
7. **No gradients.** Light is flat steps, a dashed trail, rings or crosses. Every band has a hard edge.
8. **Print:** grain and hatching only; `ink.css` hides blooms, steps and the grid under `@media print`.

## The menu

**Blooms** (watercolour masks, tint to any colour): `round`, `core` (dense centre, faint ring), `halo` (two layers), `pair`, `cloud`, `pool` (wide), `drift` (a bloom with a tail), `splash` (with satellite drops), `spots` (a scatter), `tall`, `crescent`, `sweep` (an arch), `corner` (runs off the top-right, for cards), `band` (runs off both sides), `ground` (a land wash, runs off the sides and bottom).

**Paper:** `grain` (static specks), hatching `fine` (horizontal), `slant` (45°), `cross`.

**Light:** `steps` (default: flat stepped pools on the message, with a stepped wedge from the source), `trail` (a dashed route that leads the eye), `contours` (rings, one hero only), `grid` (survey crosses that step brighter near the message).

**Figures** (face right; `{dir:-1}` flips; anchors in brackets):
- Standing: `stand` (hand, head), `stand-raise` (hand up: holding the ball high), `stand-point` (hand), `stand-phone` (hand), `walk` (hand), `stand-basket` (hat and basket: field work).
- Seated on a chair: `sit-write` (reaching to a desk: hand), `sit-read` (book: hand), `sit-think` (chin on hand).
- Other: `sit-ground` (knees up with a book: golf tasks, solo reading), `hand-phone` (close-up hand with chat bubbles: capture), `pair-table` (two people, two chairs, a table: a call, a meeting; middle), `audience` (five heads: a talk).

**Props** (anchors in brackets): `desk` (top, left, right), `table` (top), `chair` (seat), `lamp` (light), `laptop` (screen), `window` (centre), `stage` (top), `hills` (peak), `field-rows` (far), `skyline` (top), `flag` (top), `plant` (top), `seedling` (top: a crop or first growth), `book` (top), `phone` (screen), `basket` (top).

**Signature:** the coral ball `#F58E84` (`.ink-ball`, `ball:`), the Wada number stamp (`.ink-stamp`, `stamp:"No. 273"`), the field tag (`.ink-tag`, `tag:"Field 04"`: a survey label; on Fuji pages name the system, "Shasta · field 07").

## Touch recipes (ink.css)

Put `<link rel="stylesheet" href="ink.css">` after the palette block, then `python scripts/kit.py bundle page.html out.html`. The bundle inlines only what the page uses.

```html
<body class="ink-page ink-grain ink-grid">                     <!-- grain and survey grid on the ground -->
<h1 class="ink-bloom" data-bloom="drift" style="--bloom-c:var(--b2)">Reading week</h1>
<div class="card ink-bloom" data-at="corner" data-bloom="corner">…</div>   <!-- keep the card's top-right quarter free of words -->
<figure class="ink-bloom" data-at="behind" data-bloom="round"><svg>…</svg></figure>
<div class="ink-steps" style="--lx:18%;--ly:50%">…the one message…</div>  <!-- light centred on the message -->
<ol class="ink-trail">…</ol>          <!-- add data-end="ball" only when no other ball is on screen -->
<p><span class="ink-ball"></span><b>The decision.</b></p>
<span class="ink-stamp">No. 33</span> <span class="ink-tag">Shasta · field 07</span>
<div data-hatch="slant" style="--hatch-c:var(--mu)">…</div>   <!-- print: hatching and grain only -->
```

- **Variables:** `--bloom-c`, `--bloom-o`, `--bloom-size`; `--light`, `--lx`, `--ly`, `--la` (stair angle); `--grid-c`, `--grid-o`; `--grain-o`; `--hatch-c`, `--hatch-o`, `--hatch-size`.
- **Light paper:** add `data-ink="light"` on `<html>` so the ball gets an ink edge (coral is under 3:1 on paper).
- **Phone:** the heading bloom shrinks to 34vw; `.ink-page` on `<body>` stops sideways scroll.

## Scene settings (ink.js)

A Scene is about ten lines. Start from `examples/scene-post.src.html`.

```js
Ink.scene("#c", {
  shape: "4:5",                       // 16:9 | 4:5 | 9:16 | 3:1 | 1:1
  tokens: {bg:"#ECF7F7", tx:"#231F0E", mu:"#5E5B4B", p1:"#95E1E3", b2:"#78CDD0", b3:"#8B835B"},  // from palette.py --format json
  text: {title: "…", sub: "…", at: "top"},          // top | bottom | left; checked against the bloom
  bloom: {name: "pair", at: [.66,.58], size: .62, c: "b2", o: .7},
  land: {c: "p2", top: .86},                       // the ground wash (mask "ground" unless name: is given)
  parts: [["desk", .44, .86, 1.15], ["laptop", "desk.left", 1.15], ["sit-write", .7, .86, 1.15, {dir:-1, id:"me"}]],
  light: {kind: "steps", from: "laptop.screen", to: "me.hand"},
  ball: "me.hand", rim: "b2", stamp: "No. 41", tag: "Field 01", alt: "…"
});
```

- **A part** is `[name, x, y, scale, {options}]`, with x and y from 0 to 1 of the frame at the part's feet; or `[name, "id.anchor", scale, {options}]` to stand it on any earlier part's anchor, figure or prop (a flag in a raised hand: `["flag","f2.hand",.6]`). Scale 1 makes a standing figure a third of the short side.
- **Options:** `id` (the name anchors use; defaults to the part's name, so give an `id` when a part appears twice), `dir:-1` (flip; its anchors flip with it), `c` (ink colour), `rim`, `light`.
- **Anchors** (`"me.hand"`) aim `light.from`, `light.to` and `ball`. `light.to` defaults to the ball.
- **Sizes** (`bloom.size`, `light.size`, `ballSize`) are fractions of the short side. Defaults: bloom .6, light .28 (contours .3), ball .018; `land.top` .7 of the height.
- **Text:** `at:"top"` or `"bottom"` runs full width; `"left"` uses the left 42%, centred down the frame. When kit.py warns that text sits on the bloom, move `bloom.at` away; never move the words onto the art.
- **Tokens:** paste the `tokens` object from `palette.py --place <place> --format json`, plus its `book` colours as `b1` to `b4`. The kit reads `bg` (ground), `tx` (title; ink on light grounds), `mu` (sub, stamp, tag) and `p1` (the light's default); any other token is there for you to name. Missing ones fall back to safe defaults.
- **Colours** are a token name (`"b2"`, `"p1"`), `"ball"`, or a hex. `rim` is the rim-light colour behind figures (an offset silhouette, the "rim light" of the reference video); no rim when it is left out.
- **Optional:** `grid:false`, `grain:false`, `hatch:{tile:"slant", area:[0,.85,1,1], c:"b3"}`, `ink:"#…"`, `light.size`, `light.rings` (contours), `ballSize`.
- **Export:** `python scripts/kit.py png out.html --dir pngs` writes every canvas as a PNG (named by its id) for Figma and slides, and prints any clarity warning. `Ink.png(canvas, "name.png")` saves from the page. `Ink.svg("sit-read", "#1d1715")` gives one part as SVG.

## Commission: making new parts

Only when Ash says so ("commission", "paint it", "go heavy"). The gallery in Fuji (`ranges/self/personal-brand/research/art-style-study.html`, eight frames) is the reference for a fully painted piece.

- **Fully painted piece:** p5.brush in the page, the way the Fuji gallery does it. Load `https://cdn.jsdelivr.net/npm/p5.brush@2.2.3/dist/brush.js` (global `brush`), `brush.createCanvas(w,h,{parent})`, wrap drawing in `brush.push(); brush.translate(-w/2,-h/2)` (the origin is the centre), and `brush.render()` before reading pixels. Brushes: pen, rotring, 2B, HB, 2H, cpencil, pastel, crayon, charcoal, spray, marker; fills `brush.fill`, `fillBleed`, `fillTexture`; hatching `hatchStyle` and `hatch`.
- **The pigment trap:** p5.brush only darkens, so colours vanish on dark ground and turn near-white on a transparent canvas. Paint each colour in black on `brush.clear('#ffffff')`, read the pixels, and set alpha = (255 − luminance) × 2.1 with the real colour as RGB: `bpass()` in the Fuji gallery, `paint()` in `scripts/painter.html`.
- **Save every new part back into the kit:**
  - A new bloom or tile: add a function to `BLOOMS` (or a tile) in `scripts/painter.html`, run `python scripts/paint_assets.py --sheet sheet.png`, look at the sheet.
  - A new figure or prop: add an entry to `P` in `assets/ink.js` (units: a standing figure is 200 tall, feet at 0,0, y up is negative; ops `c e r p s u`, a leading `L`, `l` or `B` draws in light, faint light or ground colour), with its box `b` and anchors `a`.
  - Then add its name to "The menu" above, rebuild the gallery (`python scripts/kit.py bundle scripts/gallery.src.html gallery.html --all`), and commit.
