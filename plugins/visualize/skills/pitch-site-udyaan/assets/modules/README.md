# Modules

Proven section fragments from the TVS site (v7), rebuilt on the starter's tokens and helpers. Each file is a header comment (catalogue ID, content shape, how to adapt, the data), then `<section class="band ...">`, a `<style>` scoped by the module prefix, and a `<script>` IIFE whose first lines are `DATA`. Change `DATA` and the heading copy; leave the mechanics. Every module lands on its finished, fully labelled state under `?final=1` or reduced motion. The marker colour marks only what the reader gets; lit states and current steps use ink.

- `kolam-hero.html` · WRD-01 (kolam direction) · `kol-` · opening screen: one promise beside a self-drawing kolam, plus a three-badge key that lights one strand each (exposes `window.kolDraw` and `<svg data-kol-mini="s2">` badges for later sections) · `DATA.key [{part, label, means}]`
- `snake.html` · SEQ-01 · `snk-` · 3-6 problems in order, each with one team and one outcome, ending in one result; the line follows the scroll · `DATA.problemLabel, getsLabel, stops [{problem, team, chip, does, gets}], end {label, text}`
- `constellation.html` · STR-01 · `cst-` · one goal, 3-5 branches, 2-4 leaves each with the team that owns it (16 leaves at most); computed layout, list twin below 820px · `DATA.centre, branches [{name, chip, leaves [{text, team}]}]`
- `translator.html` · WRD-08 · `trn-` · 3-8 technical terms, each with a plain meaning and one result at the client; tappable progress bars · `DATA.client, step, terms [{term, means, soAt}]`
- `orbit-fork.html` · SEQ-22 + CHG-36 · `orb-` · one worked project in 4-6 steps around it (one lap of the dot), then a decision between 2-4 options · `DATA.project {label, title}, steps [{title, text, chips}], decide {label, title}, options [{title, text}]`
- `ring.html` · TVS teaching circle · `rng-` · one person or core feeding a group of 4-8, four stages in the corners, one result · `DATA.centre, people, callouts [{title, text, chip}] (4), gets {label, text}`
- `ladder.html` · STR-17 · `lad-` · 3-5 ordered levels (senior first) and what each level gets; the spine rises from the bottom · `DATA.heads [who, what], levels [{level, gets}]`
- `start-portrait.html` · PPL-28 + PPL-01 + PPL-27 · `srt-` · the close: three pictured first steps (pick one, meet one person, get one draft), then the contact card with a line portrait and a copy-email button · `DATA.steps [{kicker, title, text, pic, caption, options, picked}] (3), contact {kicker, name, line, email, copy, copied, fallback}`

Gallery: `assets/gallery.html` shows all eight working, built from `assets/gallery-src/` (the starter filled with the kolam direction, plus `frag-NNa-label.html` and a copy of each module as `frag-NNb-<module>.html`). Rebuild with `python scripts/build.py assets/gallery-src --out ../gallery.html` after copying changed modules in.

## More proven sections (Coastline example, drafting direction)

Full fragments in `assets/examples/coastline-src/`, built on the same starter and reviewed twice. They draw on a
hand-made motif object (`TRUCK` in that folder's `starter.html`): copy the mechanics, redraw the object for your client.

- `frag-1-hero.html` · WRD-01 + SEQ-03 · `hero-` · full-screen hero; the client's own object draws itself on in plotter order (construction lines, centre lines, object lines, dimension, title block), then one redline note asks the question the page answers
- `frag-2-echo.html` · WRD-15 adapted · `echo-` · the asks hang off the lit parts of one big drawing by red leader lines, measured and pen-drawn; stacks with badges below 900px
- `frag-3-stage.html` · ARC-02 + SEQ-02 + STR-25 + MOT-04 + STR-26 · `stg-` · the pinned stage: five steps, one change each (x-ray, sensors land, one hue floods, a signal, a pull-back onto a real map); active caption at full strength; a static still of the last step under `?final=1`
- `frag-4-paper.html` · CHG-09 + EMP-16 · `p2s-` · paper log with handwritten ticks beside the same rows live; strike-and-replace goal line
- `frag-5-roads.html` · CHG-37 · `road-` · two roads from today (dashed ghost versus inked dimension line), each ending on a drawn sheet; a pen ring around the split
- `frag-6-switch.html` · STR-02 · `swb-` · switchboard: asks with badges on the left, team tiles on the right, cords inked ask by ask as you scroll
- `frag-7-cta.html` · PPL-27 + PPL-01 + the motif's close · `cta-` · the motif returns finished on the dark band with an empty title-block cell circled, then the contact card with a portrait inside a detail circle
