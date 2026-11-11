---
name: paint-scene
description: "[helper · runs inside match-ash-design] How do I give a page, post or slide painted character without losing clarity? Adds watercolour blooms, stepped light, ink figures and the coral ball from a ready kit, at three levels: Touch (CSS), Scene (a picture from ten lines of settings, PNG export) or Commission (painted with p5.brush). Use when match-ash-design's case allows it, or Ash says 'add character', 'paint a scene' or 'commission'."
---

# Paint a scene

Character from a ready kit, inspired by a watercolour-and-ink explainer style and made Ash's own: one Wada combination, light as steps instead of gradients, survey-grid texture, and **the coral ball as the one bright thing**. Claude picks parts by name; nothing is drawn by hand below the Commission level.

**This skill runs inside `/visualize:match-ash-design`** (`../match-ash-design/SKILL.md`): that skill picks the case and the palette, this one adds the character. Words still follow `/write:match-ash-writing`.

## Steps

1. **Set the level.** Find the case in "The level per case" in `references/character.md`. Ash's own pages: Touch at most, never asked. Pages for others: the answer to the character question the building skill already asked. Commission only on Ash's words. Done when you can say the level in one line ("A pitch for Udyaan, Scene, Ash said so in the intake").
2. **Check the picture earns its place.** Run match-ash-design's "When to draw" and its two covered tests. Name the one message the light will point at. Done when you can name that message, or the level drops to Touch or nothing.
3. **Pick the parts by name** from "The menu" in `references/character.md`: one bloom, one kind of light, the figures and props, where the ball goes. Done when every part is a name from the menu (`python scripts/kit.py list`), and there is one bloom, one light and one ball.
4. **Build it.**
   - **Touch:** add the ink.css classes from "Touch recipes".
   - **Scene:** write the settings from "Scene settings", starting from `examples/scene-post.src.html`.
   - **Commission:** follow "Commission"; save every new part back into the kit.
   Then `python scripts/kit.py bundle page.html out.html`. Done when the bundle prints the masks and tiles it inlined.
5. **Check it once.** `python scripts/kit.py shot out.html shot.png --width 1280` (390 for phone-first cases), or `kit.py png out.html --dir pngs` for Scenes, and look at the image for three things only: the art reads, the light sits on the message, nothing covers text. Fix once. Done when kit.py prints no WARN, no SIDEWAYS SCROLL, and the image passes the three looks.
6. **Hand it over** the way the building skill does; for a Scene also give the PNG path for Figma or slides.

## Reference files

- `references/character.md`: open on every run. The level per case, the clarity rules, the menu, Touch recipes, Scene settings, and Commission.
- `gallery.html`: every mask, tile, light, figure and prop with its name, plus the four shapes. Open it to choose by eye.
- `scripts/kit.py`: `bundle` (inline only what the page uses), `png` (export scenes), `shot` (screenshot and overflow check), `list` (every name).
- `scripts/paint_assets.py` and `scripts/painter.html`: repaint the masks and tiles with p5.brush. Run only when a Commission adds one.
- `examples/`: a Touch on a dark page (`touch-dark.src.html`) and a 4:5 post Scene (`scene-post.src.html`, `handoff-post.png`).
- `assets/ink.css`, `assets/ink.js`, `assets/masks/`, `assets/tiles/`: the kit itself.
