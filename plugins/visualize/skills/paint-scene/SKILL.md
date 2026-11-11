---
name: paint-scene
description: "[helper · runs inside match-ash-design] How do I give a page, post or slide character without losing clarity? Two looks from ready kits, Watercolour (blooms, stepped light, ink figures) or Ring Eyes (flat colour, hand lettering, 26 ring-eyed characters, 11 formats), each at Touch, Scene or Commission level, with PNG export. Use when match-ash-design's case allows it, or Ash says 'add character', 'paint a scene', 'ring eyes' or 'commission'."
---

# Paint a scene

Character from a ready kit, in one of two looks, both made Ash's own with Wada colours and **the coral ball as the one bright thing**:
- **Watercolour:** blooms, light as steps instead of gradients, ink figures, survey-grid texture (`references/character.md`).
- **Ring Eyes:** one flat colour, wobbly hand lettering with one huge word, black characters with white ring eyes cropped by the frame (`references/ring-eyes.md`).

Claude picks parts by name; nothing is drawn by hand below the Commission level.

**This skill runs inside `/visualize:match-ash-design`** (`../match-ash-design/SKILL.md`): that skill picks the case and the palette, this one adds the character. Words still follow `/write:match-ash-writing`.

## Steps

1. **Set the look and the level.** Find the case in "The level per case" in `references/character.md`. Ash's own pages: Watercolour Touch at most, never asked. Pages for others: the answer to the one character question the building skill already asked ("none, Touch or Scene; Watercolour or Ring Eyes?"); with no answer on the look, pick by "Ring Eyes or Watercolour" in `references/ring-eyes.md`. Commission only on Ash's words. Done when you can say both in one line ("An Udyaan post, Ring Eyes Scene, Ash picked it in the intake").
2. **Check the picture earns its place.** Run match-ash-design's "When to draw" and its two covered tests. Name the one message the light will point at. Done when you can name that message, or the level drops to Touch or nothing.
3. **Pick the parts by name.** Watercolour: "The menu" in `references/character.md`, one bloom, one kind of light, figures and props, where the ball goes. Ring Eyes: "The cast" and "Formats and settings" in `references/ring-eyes.md`, one format, one lead character, one big word. Done when every part is a name from `python scripts/kit.py list` and the piece has one bloom or one big word, one light at most, and one ball.
4. **Build it.**
   - **Touch:** Watercolour, the ink.css classes from "Touch recipes"; Ring Eyes, one `<i data-ring="…">` mark.
   - **Scene:** Watercolour, settings from "Scene settings", starting from `examples/scene-post.src.html`; Ring Eyes, one `Ring.piece` call, copying the nearest settings block in `scripts/ring-gallery.src.html`.
   - **Commission:** the "Commission" section of the look's reference file; save every new part back into the kit.
   Then `python scripts/kit.py bundle page.html out.html`. Done when the bundle prints what it inlined.
5. **Check it once.** `python scripts/kit.py shot out.html shot.png --width 1280` (390 for phone-first cases), or `kit.py png out.html --dir pngs` for Scenes, and look at the image for three things only: the art reads, the light (or the big word) carries the message, nothing covers text or crops through eyes. Fix once. Done when kit.py prints no WARN, no SIDEWAYS SCROLL, and the image passes the three looks.
6. **Hand it over** the way the building skill does; for a Scene also give the PNG path for Figma or slides.

## Reference files

- `references/character.md`: open on every run. The level per case and the look question, the clarity rules, and the Watercolour menu, Touch recipes, Scene settings and Commission.
- `references/ring-eyes.md`: open for a Ring Eyes run. Why it works, what breaks it, the rules, Ring Eyes or Watercolour, the cast, expressions and poses, formats and settings, Commission.
- `gallery.html` (Watercolour) and `ring-gallery.html` (Ring Eyes): every part with its name. Open one to choose by eye.
- `scripts/kit.py`: `bundle` (inline only what the page uses), `png` (export scenes and Ring Eyes pieces), `shot` (screenshot and overflow check), `svgs` (every Ring Eyes character to `assets/ring/`), `list` (every name).
- `scripts/paint_assets.py` and `scripts/painter.html`: repaint the masks and tiles with p5.brush. Run only when a Commission adds one.
- `examples/`: a Touch on a dark page (`touch-dark.src.html`) and a 4:5 post Scene (`scene-post.src.html`, `handoff-post.png`).
- `assets/ink.css`, `assets/ink.js`, `assets/masks/`, `assets/tiles/`: the Watercolour kit. `assets/ring.js` and `assets/ring/*.svg`: the Ring Eyes kit.
