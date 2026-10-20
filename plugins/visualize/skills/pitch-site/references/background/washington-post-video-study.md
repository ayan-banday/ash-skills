---
date created: 2026-10-17
date updated: 2026-10-17
---

# Video Animation Study: scroll-told rocket-to-orbit explainer

Source: `C:\Users\ayanb\Downloads\aPtPAA1A3I1zxDhwmiGXyFA8FN4.mp4` (studied only through extracted frames).
All images referenced below sit next to this file.

Image set:
- `sheet_01.png`, `sheet_02.png`: whole video at 2 frames per second, timestamped.
- `scenes_sheet.png`: every frame the scene detector flagged (threshold 0.08).
- `burst_01` to `burst_13`: 10 fps, 1 second each, timestamped, read left to right, top to bottom.
- `fine_20fps_*`, `fine_40fps_streaks.png`: 20 to 40 fps strips for the fastest moves.
- `key_01` to `key_14`: 960 px stills.

---

## A. Overview

**What it is.** A 26.15 s screen recording of a dark-mode scrollytelling news article ("What would happen if Russia detonated a nuclear bomb in space?", July 2024). Every motion in it is driven by the reader scrolling. A fixed full-screen picture sits behind narrow text cards that scroll up the left side. One ad interrupts from 15.0 s to 17.5 s; ignore it.

**Specs.** 2874 x 1620 px (a Retina capture of a ~1437 x 810 CSS viewport), 1.77:1 (16:9), 120 fps source, 3,138 frames. No hard cuts in the story; the scene detector found only the ad and the globe-to-diagram handoff at 19.5 s.

**Scroll speed in the recording.** Text cards travel about 35 to 45% of the viewport height per second (measured at 0 to 1.8 s and 18.6 to 19.7 s). Read every duration below as a scroll distance: **1 s of video ≈ 40vh of scroll**.

**Story beats (one camera, never cut).**
1. 0 to 3 s: title; line-drawn rocket pinned centre; flame ignites; smoke blooms and falls away (key_01, key_02).
2. 3 to 6 s: ascent; faint speed streaks pass a fixed rocket (key_03).
3. 6 to 8 s: a dark map fades in under the rocket, then the camera pulls back until the map curves into a globe with a banded atmosphere (key_04, key_05).
4. 8 to 10.5 s: the rocket tilts into orbit, the engine cuts, the rocket goes ghostly and the gold satellite inside it appears (key_06, key_07).
5. 10.5 to 15 s: the satellite tumbles, unfolds its solar panels, the globe surface lights up, a name label fades in (key_08, key_09, key_10).
6. 18 to 20 s: the camera pulls far back; satellite shrinks to nothing; the globe becomes a small disc in a flat orbit diagram; rings fade in (key_11, key_12).
7. 21.6 to 22.5 s: labels arrive one ring at a time, inner first (key_13, key_14).

**Palette (sampled from full-resolution frames).**
- Ground: `#000000` pure black, no texture.
- Line art and flame: `#FFFFFF`.
- Smoke, four flat tones: `#9C9C9C`, `#787878`, `#6C6C6C`, `#4E4E4E`.
- Speed streaks: `#1E1E1E` to `#3C3C3C`.
- Map land (first appearance): `#121212` on black.
- Atmosphere rim: `#989898`, then ~11 stepped bands fading `#575757 > #4C4C4C > #454545 > #3D3D3D > #353535 > #2E2E2E > #282828 > #222222 > #1B1B1B > #161616 > #101010 > #060606`, each band ~15 CSS px tall.
- Globe surface: ocean `#181818`, land `#2A2A2A` to `#4E4E4E`, rim highlight `#969696`.
- Satellite accent (the only warm colour, first used at 9.7 s): yellow-gold `#E4E04E`.
- Radiation belts: deep navy `#0C1218` (thick annuli).
- Belt label: sky blue `#33B0F0`. Orbit label: `#FFFFFF`.
- Orbit path: white hairline dashes.
- Text cards: black fill, 1 px border `#2A2A2A` to `#363636`, text `#F6F6F6`.

**Type.** Headline in a high-contrast editorial serif, ~40 px. Body in a book serif, ~16 px, inside boxed cards ~250 px wide. Diagram labels in a grotesque sans (Franklin-style), ~15 px, two centred lines, coloured to match the thing they name.

**Illustration style.** Geometric technical line art with a CAD or blueprint feel: uniform strokes of about 1 to 1.5 CSS px, no fill, no texture, no hand wobble. Detail lives in small marks (tick dashes under the rocket nose, hatched solar panels). Volume comes only from flat posterised tones (smoke circles, stepped atmosphere); there are no smooth gradients or shading. The diagram drops illustration altogether: thick flat rings, a hairline dashed circle and plain labels. Colour is rationed. Everything is greyscale until the satellite appears in gold, then blue enters for the belts. **A new colour means a new concept.**

---

## B. Motion vocabulary

Rule that governs everything: **the protagonist stays pinned and the world moves around it.** The rocket never leaves screen centre; smoke falls away, streaks pass, the map slides under it and the globe sinks behind it. Rising is shown by everything else moving down.

### B1. Sticky stage with scrolling cards
- What moves: text cards (left, ~18% of width) scroll up over a fixed full-screen picture.
- How: plain document scroll; the picture is `position: sticky`. Cards are spaced ~1 viewport apart, so one card is on screen at a time.
- Timing: reader-paced. Each card has the screen to itself for roughly 1.5 to 3 s of scroll.
- Easing: none (native scroll).
- Enter/exit: cards enter from the bottom edge and leave from the top. The graphic changes while a card crosses the middle third of the screen.
- Evidence: every sheet; clearest in burst_12.

### B2. Flame ignites and flickers
- What moves: a white teardrop at the rocket base.
- How: grows from a tiny point (0.3 s) to a full rounded flame (0.5 s), scaling from its top edge. During ascent it swaps between a pointed and a round silhouette (a 2-pose stepped flicker, no tween).
- Timing: ignite ~200 ms; flicker poses change every ~100 to 300 ms.
- Easing: ignite feels ease-out (fast start, soft landing). Flicker is stepped.
- Exit: at engine cut (9.3 to 9.6 s) the flame thins to a curved tail and disappears in ~300 ms.
- Evidence: burst_01 (0.3 to 0.5 s), burst_03, burst_06 last frame, burst_07 first three frames.

### B3. Smoke bloom
- What moves: 10 to 15 opaque flat circles in four greys, layered so lighter ones sit in front.
- How: circles scale up from the flame point and spread outward and sideways into a wide cloud. One small circle flies off to the right (0.6 s). Tones shuffle as circles overlap.
- Timing: first puff at 0.6 s, cloud fills the bottom third by 1.2 s (~600 ms), keeps swelling slowly to 2.2 s. Exit: the whole cloud slides down off-screen from 2.2 to 3.0 s (~800 ms) as the rocket "rises".
- Easing: each circle ease-out (big growth early, slow at the end). Exit linear with scroll.
- Stagger: ~50 to 100 ms between new circles, centre first, then outward.
- Evidence: burst_01, burst_02, key_02.

### B4. Speed streaks
- What moves: sparse, very faint vertical dashes (1 px, 20 to 120 px long, `#1E1E1E` to `#3C3C3C`) scattered across the black.
- How: drift downward past the fixed rocket; some hold position for 250 ms or more, then others appear elsewhere. Reads as altitude sliding past.
- Timing: continuous from ~3.5 to 6 s, fades with the arrival of the map. Speed is low-contrast and hard to measure (medium confidence).
- Easing: linear.
- Evidence: burst_03, fine_40fps_streaks.png (contrast-boosted), key_03.

### B5. Context underlay fades in and drifts
- What moves: a dark map of Russia and Europe (`#121212` land on black) behind the rocket.
- How: opacity 0 to 1 while the whole map slides slowly downward and shrinks slightly (the rocket is climbing away from it).
- Timing: 6.3 to 6.7 s to full opacity (~400 ms ≈ 16vh), then keeps drifting.
- Easing: fade linear; drift linear with scroll.
- Evidence: burst_04, key_04.

### B6. Camera pull-back reveals curvature
- What moves: the whole world layer (map plus a new atmosphere rim).
- How: the camera zooms out. The flat map turns out to be the surface of a globe: a bright limb enters at the top-right corner (7.2 s), sweeps into a full arc across the top of the screen and keeps sinking and shrinking. Land shapes stay registered to the globe the whole time (continuous camera, no crossfade).
- Timing: big move 7.2 to 7.6 s (~400 ms), settle 7.6 to 8.1 s, then a slower continuing sink 8.4 to 11 s.
- Easing: ease-out on the reveal (fast entry, slow landing), then linear with scroll.
- Evidence: burst_05, burst_06, scenes_sheet (row 1 to 3), key_05.

### B7. Stepped atmosphere bands (a treatment that moves with the camera)
- What it is: the globe edge drawn as ~11 concentric bands of decreasing grey (a posterised gradient), topped with a brighter rim line. Looks like contour lines or an engraving.
- Motion: none of its own; it scales and translates with the globe.
- Evidence: key_05, key_09, burst_08.

### B8. Pivot tilt (gravity turn)
- What moves: the rocket.
- How: rotates clockwise around a point near its middle, from 0° to ~22°, while sliding a little to the right. The globe keeps sinking behind it.
- Timing: 8.5 to 9.4 s (~900 ms ≈ 36vh).
- Easing: linear with scroll, soft start.
- Evidence: burst_06, key_06.

### B9. X-ray reveal (shell ghosts, payload appears)
- What moves: the rocket's strokes dim; a gold satellite line drawing fades in inside the nose fairing, already at the right size and angle.
- How: pure crossfade, no motion. Rocket opacity 100% to ~25% (9.65 to 10.25 s), satellite 0 to 100% over the same window. The ghost rocket then fades out entirely by ~10.6 s, leaving the satellite where the fairing was.
- Timing: ~600 ms crossfade + ~350 ms ghost exit.
- Easing: linear crossfade.
- Why it works: the payload appears exactly where it physically sits, so the eye never has to search. This is a **match on position**.
- Evidence: fine_20fps_xray-reveal.png, burst_07, key_07.

### B10. Slow tumble
- What moves: the satellite.
- How: rotates slowly about its centre (roughly 10 to 15° per second) while holding its screen position.
- Timing: 10.5 to 14.3 s, scroll-linked.
- Easing: linear.
- Evidence: sheet_01 rows 3 to 5.

### B11. Parts unfold
- What moves: two hatched solar panels on the satellite.
- How: panels start as short stubs at the body and extend outward on both sides at once, as if sliding out of the body. The body keeps rotating ~20° clockwise during the unfold.
- Timing: 13.35 to 14.25 s (~900 ms ≈ 36vh).
- Easing: close to linear, slight ease-out at full extension.
- Stagger: none; both panels move together.
- Evidence: fine_20fps_panels-unfold.png, burst_08, key_08, key_09.

### B12. Surface fills in
- What moves: the inside of the globe arc.
- How: goes from black (bands only) to a flat grey surface with land shapes (`#181818` ocean, `#2A2A2A`+ land).
- Timing: 14.5 to 15.3 s (~800 ms).
- Easing: linear fade.
- Evidence: burst_09, compare key_09 with key_10.

### B13. Name label fades in beside the object
- What moves: "Cosmos 2553 / satellite", two lines of gold sans, set to the right of the satellite.
- How: opacity only; no slide, no scale, no leader line.
- Timing: 14.95 to 15.15 s (~200 ms).
- Easing: ease-out fade.
- Evidence: burst_09, key_10.

### B14. Scale-out to context, then handoff to a schematic
- What moves: the entire scene (globe, satellite, label).
- How: the camera pulls back hard. Satellite and label shrink together toward their anchor and vanish by ~19.4 s. The globe shrinks from a screen-wide arc to a full disc, then to a small disc in the centre (diameter roughly 1/8 of the screen height).
- Handoff: at 19.5 s the shaded globe is swapped for the diagram's small globe disc at the same size and position. A white dashed orbit circle appears already shrinking into its final size (it is still part of the same zoom), so the switch reads as continuous. This is a **match-cut on scale**.
- Timing: slow phase 17.9 to 19.1 s (scale ~1 to ~0.6), fast phase 19.1 to 19.5 s (diameter drops ~4x), land at 19.55 s. Total ~1.6 s ≈ 60vh.
- Easing: ease-in into the handoff (slow then fast), with a short ease-out landing on the diagram. Linear interpolation of scale makes the end feel rushed; see E for a calmer mapping.
- Evidence: burst_10, burst_11, fine_20fps_zoom-handoff.png, key_11, key_12.

### B15. Diagram layers arrive at the matched scale
- What moves: two thick navy annuli (the radiation belts) inside the dashed orbit.
- How: opacity 0 to 1 at their final size; no draw-on, no growth.
- Timing: 19.65 to 19.85 s (~200 to 250 ms), right after the dashed orbit settles.
- Stagger: dashed orbit first (19.5), then both belts together (19.65).
- Evidence: burst_11 second row, fine_20fps_zoom-handoff.png, key_12.

### B16. Labels arrive one ring at a time, inside out
- What moves: "Van Allen / radiation belts" (blue, placed on the inner belt) then "Geosynchronous / orbit" (white, placed on the dashed outer orbit).
- How: opacity only, each label sits on top of the ring it names, centred at 12 o'clock.
- Timing: inner label 21.8 to 22.0 s, outer label 22.1 to 22.3 s. ~200 ms each, ~300 ms stagger. Triggered as a new card ("The outermost satellites...") enters.
- Evidence: burst_13, key_13, key_14.

### B17. Hold
- What moves: nothing. From 19.9 to 21.6 s the card keeps scrolling but the picture is frozen.
- Why it matters: the reader gets a still picture while reading. Motion happens between reading beats, never during them.
- Evidence: burst_12.

**Trigger model (medium confidence).** Camera moves (B5, B6, B8, B10, B14) progress in step with card travel, so they are scrubbed by scroll. Small arrivals (B13, B15, B16) complete in ~200 ms regardless, so they are short tweens fired when a card crosses a line. Between steps the picture holds (B17).

---

## C. Transitions between scenes

The piece is one continuous camera with no cuts. Each scene hands off to the next by one of four devices:

1. **Pinned subject, moving world** (title to launch to ascent, 0 to 6 s). The rocket never moves; smoke exits downward, streaks pass. Continuity comes from the fixed protagonist.
2. **Fade-in underlay, then continuous camera pull-back** (ascent to Earth, 6 to 8 s). A context layer fades in beneath the subject, then the zoom-out reveals that layer is the surface of something larger (map becomes globe).
3. **Crossfade match on position** (rocket to satellite, 9.65 to 10.6 s). The new object appears inside the old one, at the same place; the old one ghosts out.
4. **Match-cut on scale** (illustrated scene to schematic diagram, 19.5 s). The zoom-out shrinks the shaded globe until it equals the diagram's globe disc, then swaps rendering style. The dashed orbit enters mid-zoom so the cut hides inside the motion.

No wipes, no morphs between unlike shapes, no zoom-through.

---

## D. How the motion serves clarity

**Motion that explains.**
- **Pull-backs set scale.** Map to globe tells you the rocket has left the country and reached the edge of space. Globe to orbit diagram tells you the satellite is a speck inside much bigger structures. Each pull-back answers "where are we now?" without a caption.
- **The x-ray shows containment.** The satellite is revealed inside the rocket, so the reader learns "the rocket was only the delivery" with zero words.
- **The unfold shows a state change.** Packed satellite becomes working satellite. Before and after in one move.
- **One fixed protagonist.** Pinning the rocket while the world moves keeps attention on the subject and turns "altitude" into something you watch happen.
- **Colour enters with the concept.** Gold appears exactly when the satellite does, blue exactly with the belts. The colour itself becomes a label.
- **Diagram builds one layer at a time.** Globe, then orbit, then belts, then belt label, then orbit label. Each layer arrives only after the previous one is readable, and labels go inside out (near to far).
- **Holds during reading.** The picture freezes while a card is read (burst_12). Motion never competes with text.

**Motion that decorates.**
- Flame ignite and flicker, smoke bloom, speed streaks, slow tumble. They add drama and a sense of physical motion but carry no information. The smoke is the most expensive move in the piece and explains nothing.
- The stepped atmosphere bands are mostly mood, though they also make the globe edge legible against black.

---

## E. Translation to the web (vanilla JS + SVG/CSS)

**Shared scaffolding.**
- Layout: `<section class="story">` containing a `position: sticky; top: 0; height: 100vh` stage and a column of `.step` cards with `margin-bottom: 90vh`.
- Steps: one `IntersectionObserver` with `rootMargin: "-45% 0px -45% 0px"` sets `data-step` on the stage. CSS transitions do the small arrivals.
- Scrubbed ranges: one passive `scroll` listener feeding a `requestAnimationFrame` that computes `p = clamp((scrollY - start) / (end - start), 0, 1)` per range and writes CSS variables (`--p`). Optionally upgrade to CSS `animation-timeline: view()` where supported; keep the JS path as the fallback.
- Calm house curves: arrive `cubic-bezier(0.22, 1, 0.36, 1)`; camera `cubic-bezier(0.65, 0, 0.35, 1)`; fade `cubic-bezier(0.4, 0, 0.2, 1)`.
- Reduced motion: `@media (prefers-reduced-motion: reduce)` sets every step to its end state, keeps 150 ms opacity fades only, disables scrubbing.

**Per move.**
- B1 sticky stage: as above. On narrow screens the stage becomes the top 55vh and cards scroll beneath it on a paper-coloured panel.
- B2 flame ignite: `transform: scaleY(0 → 1)` with `transform-origin: 50% 0%`, 200 ms, arrive curve. Flicker: swap two `<path>` elements via a 2-frame `steps(1)` keyframe at 180 ms. Skip for the house style.
- B3 smoke bloom: 10 to 15 `<circle>` elements, each `transform: scale(0 → 1)` with `transform-box: fill-box; transform-origin: center`, 600 to 900 ms ease-out, `transition-delay: calc(var(--i) * 60ms)`, sorted centre-out. Exit with a scrubbed `translateY`.
- B4 streaks: 20 absolutely positioned 1 px lines, `translateY` driven by `scrollY * 0.6` (parallax). Reject for the house style.
- B5 underlay fade and drift: `opacity: calc(var(--p) * 1)` and `transform: translateY(calc(var(--p) * 8vh)) scale(calc(1 - var(--p) * 0.05))`, scrubbed over ~16vh.
- B6 pull-back that reveals curvature: render the world as an orthographic globe (one SVG) and scrub `transform: scale()` from ~8 to 1 with `transform-origin: 50% 100%`. Interpolate scale in log space so the zoom feels even: `s = s0 * Math.pow(s1 / s0, ease(p))`. Library flag: an accurate globe with land needs **d3-geo + topojson-client** (orthographic projection); a static pre-rendered SVG globe avoids the library if it never rotates.
- B7 stepped bands: 10 to 12 concentric `<circle>` strokes with descending stroke opacity (0.35 to 0.03), or a single radial gradient with hard stops. No library.
- B8 pivot tilt: `transform: rotate(calc(var(--p) * 22deg)) translateX(calc(var(--p) * 3vw))` with `transform-box: fill-box; transform-origin: 50% 55%`, scrubbed over ~35vh.
- B9 x-ray reveal: two stacked `<g>` layers at identical coordinates. Shell `opacity: 1 → 0.25`, inner `opacity: 0 → 1`, scrubbed over ~25vh, then shell `0.25 → 0` over the next ~12vh. In the house style the inner part should draw on with `stroke-dashoffset` instead of fading.
- B10 tumble: `rotate(calc(var(--p) * 40deg))` across the scene's scroll range. In the house style cap it at ±3° or drop it.
- B11 parts unfold: each panel in its own `<g>` with `transform-origin` at its attachment point, `scaleX(0 → 1)` (one panel mirrored), 700 to 900 ms, arrive curve, both together. Then draw the hatch lines on with `stroke-dashoffset` staggered 40 ms.
- B12 surface fill: fade a fill layer `opacity 0 → 1` over 600 to 800 ms. In the house style, apply the rice-powder texture mask during the fade so it reads as chalk settling.
- B13 name label: `opacity 0 → 1` 200 to 250 ms, fade curve. House version: add a 1 px leader line that draws on first (250 ms), then the label fades, then a marker-sweep highlight under the key word (`background-size: 0% → 100%`, 450 ms, arrive curve).
- B14 scale-out to schematic: scrub one scene `<g>` with log-space scale from 1 to ~0.12 over ~50vh using the camera curve. At p = 0.92 cross-swap the illustrated globe for the diagram globe (same `r`, same centre) in a 120 ms opacity swap. Start the dashed orbit at p = 0.85 so it enters during the zoom. No library: the "cut" is two elements with matched geometry.
- B15 diagram layers: in the video they fade (200 ms). In the house style draw each ring on with `stroke-dasharray: C; stroke-dashoffset: C → 0`, starting at 12 o'clock (`rotate(-90deg)` on the circle), 700 ms, arrive curve, 150 ms stagger inside out.
- B16 staggered labels: `transition: opacity 220ms cubic-bezier(0.4,0,0.2,1)` with `transition-delay: calc(var(--i) * 300ms)`, ordered inner ring to outer ring.
- B17 hold: give every step a dead zone. Scrub ranges should cover only the first 40 to 50% of each card's travel so the picture is still for the rest.

**Moves that need a library.** Only the accurate globe (d3-geo + topojson-client). Nothing in the video morphs between unlike shapes; every change of object is a crossfade or a matched swap, so flubber or GSAP MorphSVG are unnecessary.

---

## F. Fit with the house style

Target: Anthropic and Claude craft (warm paper neutrals, hand-drawn line illustration, calm editorial pacing, connecting lines between ideas, a moving mind map) plus the TVS site (kolam drawing itself on with rice-powder texture, chalky tints, marker-sweep highlight, pulses along lines, snake line drawn by scroll).

Global adaptations for every kept move: black ground becomes warm paper (`#F0EEE6` range) or warm near-black; white geometric strokes become hand-drawn ink strokes with slight wobble and rice-powder texture; the single-accent rule stays (one chalky tint per new concept); arrivals draw on rather than fade where a line is involved.

- B1 sticky stage with cards: **fits as is.** It is the backbone of calm editorial pacing. Paper cards with a hairline border.
- B2 flame ignite and flicker: **reject.** Subject-specific and flashy.
- B3 smoke bloom: **adapt.** Keep the idea (things emerge from a seed and spread out) as a slow cluster bloom of chalk-tinted circles, 900 ms, no churn, no flying puff. Use it only when the items actually come from one source.
- B4 speed streaks: **reject.** Visual noise with no information; fights clarity.
- B5 underlay fade and drift: **fits, adapt colour.** A faint context layer (a map, a field, a kolam grid of dots) settling under the subject is exactly the calm establishing move the house style wants.
- B6 pull-back reveals curvature: **adapt.** Keep the "zoom out to see what this is part of" camera; drop the photoreal limb glow. In the house style the bigger whole should be a hand-drawn diagram or the full kolam.
- B7 stepped bands: **adapt.** Recast as concentric hand-drawn contour rings in chalk tints, drawn on outward with a 60 ms stagger. They echo kolam rings.
- B8 pivot tilt: **adapt, sparingly.** A slow rotate of a pointer or path to show a change of direction (a pivot, a fork). Keep it at most 30°, scrubbed, no overshoot.
- B9 x-ray reveal: **fits, adapt technique.** One of the best explaining moves in the piece. Shell goes to a 25% ghost, inner parts draw on in a chalk tint at their true position.
- B10 slow tumble: **reject** (or ±3° breathing at most). Decorative.
- B11 parts unfold: **fits, adapt.** Parts extend from their attachment points, then their detail lines draw on. Good for "packed idea becomes working system".
- B12 surface fill: **adapt.** Fill fades in through a rice-powder mask so it reads as chalk being laid down.
- B13 name label: **fits, adapt.** Add a drawn leader line and a marker-sweep under the key word.
- B14 scale-out to schematic: **fits, adapt.** The match-cut on scale from illustration to diagram is the strongest structural idea here. Calm it: log-space scale, camera curve, 50vh, no rush at the end.
- B15 diagram layers: **adapt.** Rings draw on (stroke-dashoffset) from 12 o'clock instead of fading; optionally a pulse travels once around each ring after it closes.
- B16 inside-out labels: **fits as is.** Ordered, quiet, one at a time.
- B17 hold: **fits as is.** Core to calm pacing.

---

## G. Catalogue entries

### Pinned stage, cards scroll past
- Shape: utility, sequence · fits 3-9 steps
- Reader sees: a still picture fills the screen while short notes slide up beside it, and the picture changes a little at each note.
- Moves: scroll-linked - native scroll for cards; picture changes fire as each card crosses the middle of the screen; picture holds still for the rest of the card.
- Build: `.stage{position:sticky;top:0;height:100vh}` beside a column of `.step` cards with `margin-bottom:90vh`.
  One IntersectionObserver, `rootMargin:"-45% 0px -45% 0px"`, writes `data-step` on the stage; CSS handles each state.
  Scrub ranges cover only the first 40-50% of each card's travel so the picture rests while the card is read.
- Narrow: stage becomes the top 55vh, cards scroll below on a solid paper panel · Reduced motion: every step shows its end state; 150 ms opacity swaps only.
- Use when: one picture can carry a whole argument in stages · Avoid when: each step needs a different picture altogether (use separate sections).
- Effort: M · Source: video, key_01_sticky-rocket-title.png / burst_12_hold-static.png

### One subject pinned, the world moves
- Shape: sequence, time-roadmap, before-after · fits 1 subject, 3-6 stages
- Reader sees: the main character stays in the middle of the screen while the background changes around it to show how far it has travelled.
- Moves: scroll-linked - background layers translate and scale under a fixed subject; subject changes only at named beats.
- Build: subject in its own `<g>` with no transform; background `<g>` gets `translateY(calc(var(--p) * 40vh))` per stage.
  Each stage swaps or fades its background layer (field, map, horizon) over ~16vh of scroll.
  Keep one background layer moving at a time.
- Narrow: same, subject scaled to 60% · Reduced motion: one still per stage, crossfaded 150 ms.
- Use when: telling a journey of one thing (a product, a farmer, a proposal) through stages · Avoid when: there are several equal actors.
- Effort: M · Source: video, key_03_speed-streaks-ascent.png / burst_04_map-underlay-fade.png

### Context settles underneath
- Shape: place-network, atmosphere · fits 1 layer
- Reader sees: a faint map or field quietly appears behind the main drawing so you know where this is happening.
- Moves: scroll-linked - underlay opacity 0 to 1 over ~16vh while drifting 8vh down and shrinking 5%, linear.
- Build: underlay `<g>` with `opacity:var(--p)` and `transform:translateY(calc(var(--p)*8vh)) scale(calc(1 - var(--p)*.05))`.
  Draw it in one chalk tint at 15-25% strength so the subject keeps contrast.
  Optional rice-powder mask (feTurbulence noise as `mask`) so it settles like powder.
- Narrow: same, drift reduced to 4vh · Reduced motion: underlay present at full opacity from the start.
- Use when: place or setting changes the meaning · Avoid when: the setting is generic; it becomes wallpaper.
- Effort: S · Source: video, key_04_map-underlay-fades-in.png / burst_04_map-underlay-fade.png

### Zoom out to the bigger picture
- Shape: part-whole, hierarchy, quantity-scale · fits 1 part inside 1 whole
- Reader sees: the camera slowly pulls back and the thing you were looking at turns out to be a small piece of something much larger.
- Moves: scroll-linked - one scene group scales from ~8 to 1 over ~50vh, log-space interpolation, camera curve `cubic-bezier(0.65,0,0.35,1)`, no overshoot.
- Build: wrap the scene in one `<g>`; `s = s0 * Math.pow(s1/s0, ease(p))` written to `transform` each rAF.
  `transform-origin` at the point the reader should keep watching (often bottom centre).
  Hide fine detail below a scale threshold so small text never shrinks into mush.
  Accurate globe or map: d3-geo + topojson-client; otherwise a hand-drawn SVG.
- Narrow: start scale 5 instead of 8 so the part stays visible · Reduced motion: show the whole with the part circled in a drawn ring.
- Use when: the reader needs to feel scale or context before the details · Avoid when: the whole is not yet introduced in words.
- Effort: M · Source: video, key_05_zoom-out-earth-limb-bands.png / burst_05_zoom-out-limb.png

### X-ray: what's inside
- Shape: part-whole, definitions-jargon, cause-effect · fits 1 shell, 1-4 inner parts
- Reader sees: the outside of a thing fades to a ghost and the important part inside appears exactly where it sits.
- Moves: scroll-linked - shell opacity 1 to 0.25 over ~25vh while inner parts draw on (stroke-dashoffset) in one accent tint; shell exits 0.25 to 0 over the next ~12vh.
- Build: two `<g>` layers at identical coordinates; shell `opacity` from `--p`.
  Inner paths: `stroke-dasharray:L; stroke-dashoffset:calc(L * (1 - var(--p)))` with `pathLength="1"` to avoid measuring.
  Accent colour appears for the first time here.
- Narrow: same · Reduced motion: ghost shell plus inner parts shown together, static.
- Use when: the real subject is hidden inside a familiar container (the product inside the service, the cost inside the price) · Avoid when: the inner part is not physically or logically inside the outer one.
- Effort: S · Source: video, key_07_xray-shell-to-payload.png / burst_07_xray-payload-reveal.png

### Unfold into working shape
- Shape: before-after, part-whole, sequence · fits 2-4 parts
- Reader sees: a packed-up object opens its parts outward and becomes ready to work.
- Moves: in-view - each part `scaleX(0 to 1)` from its attachment point, 700-900 ms, `cubic-bezier(0.22,1,0.36,1)`, parts together; detail lines then draw on with a 40 ms stagger.
- Build: each part in its own `<g>` with `transform-box:fill-box; transform-origin:left center` (mirror the opposite side).
  Hatch or detail strokes use `pathLength="1"` and dashoffset 1 to 0.
  Body may rotate at most 10° during the unfold.
- Narrow: same · Reduced motion: show unfolded state with a dotted outline of the packed shape.
- Use when: showing a plan going from proposal to operating, or a feature set opening up · Avoid when: the parts are not attached to one body.
- Effort: M · Source: video, key_08_satellite-panels-unfolding.png / burst_08_panels-unfold.png

### Name tag with a drawn leader
- Shape: definitions-jargon, emphasis · fits 1-3 labels per view
- Reader sees: a short name appears next to the thing it describes, in the same colour as the thing.
- Moves: in-view - leader line draws on 250 ms, then label fades in 220 ms `cubic-bezier(0.4,0,0.2,1)`, then a marker sweep under the key word 450 ms.
- Build: leader `<path pathLength="1">` dashoffset 1 to 0; label `opacity` transition with 250 ms delay.
  Marker sweep: `background:linear-gradient(chalk-tint,chalk-tint) no-repeat 0 85%/0% 40%` to `100% 40%`.
  Label colour equals the object's accent; never more than two lines.
- Narrow: label moves below the object, leader shortened · Reduced motion: label and highlight present, no draw.
- Use when: a new term or proper noun first appears · Avoid when: more than 3 labels would appear at once.
- Effort: S · Source: video, key_10_satellite-label-fades-in.png / burst_09_label-fade.png

### Picture hands off to a diagram
- Shape: big-idea, part-whole, hierarchy · fits 1 object to 1 diagram
- Reader sees: a drawing of a real thing shrinks until it becomes the centre dot of a clean diagram, and the diagram builds around it.
- Moves: scroll-linked - scene scales down (log space) over ~50vh; at p 0.85 the diagram's outer ring starts arriving inside the zoom; at p 0.92 the drawn object swaps for the diagram's centre shape in 120 ms.
- Build: two groups with matched geometry: illustrated object and diagram centre share centre and radius at p 0.92.
  Swap with a 120 ms opacity crossfade so the cut hides inside the motion.
  Small labels on the illustrated layer fade out before p 0.6 so they never shrink to specks.
- Narrow: shorten the zoom to ~30vh · Reduced motion: show the illustration and the diagram as two stills side by side.
- Use when: moving from a story about one case to the system it belongs to · Avoid when: the diagram's centre is not the same thing as the illustrated object.
- Effort: L · Source: video, key_11_zoom-out-full-globe.png / burst_11_scale-out-handoff.png

### Rings build inside out
- Shape: hierarchy, quantity-scale, grouped-list · fits 2-5 rings
- Reader sees: circles draw themselves around a centre one at a time, from nearest to farthest, and each gets its name.
- Moves: in-view - each ring draws on from 12 o'clock, 700 ms `cubic-bezier(0.22,1,0.36,1)`, 150 ms stagger inside out; each label fades 220 ms after its ring closes, 300 ms apart.
- Build: `<circle pathLength="1" stroke-dasharray="1" stroke-dashoffset="1" transform="rotate(-90 cx cy)">` to dashoffset 0.
  Thick bands: wide stroke at 15-20% opacity of one tint; boundaries: hairline dashes.
  Labels sit on top of their ring at 12 o'clock, coloured to match it.
  Optional: one pulse dot travels once around the outer ring after it closes (offset-path or dashoffset on a short dash).
- Narrow: limit to 4 rings, labels move to a legend below · Reduced motion: all rings and labels static.
- Use when: showing levels of distance, influence, priority or scale around one centre · Avoid when: the levels are not nested.
- Effort: S · Source: video, key_12_orbit-rings-fade-in.png / burst_13_label-stagger.png

### Labels arrive one at a time
- Shape: list-of-equals, ranked-list, grouped-list · fits 2-6 labels
- Reader sees: names appear one after another in reading order instead of all at once.
- Moves: in-view - opacity 0 to 1, 220 ms `cubic-bezier(0.4,0,0.2,1)`, 300 ms stagger, ordered near to far or most to least important.
- Build: `transition-delay:calc(var(--i)*300ms)` on each label, set `--i` in markup.
  No slide, no scale; opacity only keeps it calm.
  Fire on the step, not on scroll position, so the order is always complete.
- Narrow: same · Reduced motion: all labels shown at once.
- Use when: a finished diagram needs naming in a deliberate order · Avoid when: labels are already readable in the prose next to it.
- Effort: S · Source: video, key_13_first-label-inner-belt.png / burst_13_label-stagger.png

### Contour bands
- Shape: atmosphere, quantity-scale · fits 1 boundary
- Reader sees: the edge of a shape is drawn as a set of soft parallel rings that fade outward, like contour lines.
- Moves: in-view - 8-12 rings draw on outward from the edge, 600 ms each, 60 ms stagger; afterwards static and carried by the camera.
- Build: concentric `<circle>` or offset `<path>` strokes, stroke opacity stepping 0.35 to 0.03.
  Hand wobble via `feTurbulence` + `feDisplacementMap` (scale 1.5) and rice-powder mask.
  Brightest line on the true boundary.
- Narrow: 6 rings · Reduced motion: rings static.
- Use when: an edge or boundary is the point (a market's reach, a field's border, a zone of influence) · Avoid when: it is only there for mood; then cut it.
- Effort: S · Source: video, key_05_zoom-out-earth-limb-bands.png / key_09_satellite-deployed.png

### Seed bloom
- Shape: part-whole, grouped-list, cause-effect · fits 5-15 items from 1 source
- Reader sees: a small cluster of soft circles grows out of one point and spreads, showing many things coming from one source.
- Moves: in-view - circles scale 0 to 1, 900 ms `cubic-bezier(0.22,1,0.36,1)`, 60 ms stagger centre-out; no drifting afterwards.
- Build: `<circle>` set with `transform-box:fill-box; transform-origin:center; transform:scale(0)`, `--i` sorted by distance from the seed.
  Three chalk tints, lighter ones in front; rice-powder mask on the group.
  Labels (if any) fade after the bloom finishes.
- Narrow: cap at 8 circles · Reduced motion: final cluster static.
- Use when: one decision, input or source produces many outputs · Avoid when: the circles would carry no meaning (that is the smoke in the video: pure decoration).
- Effort: S · Source: video, key_02_smoke-billow-flat-circles.png / burst_01_flame-ignite-smoke.png

### Pivot to a new heading
- Shape: choice-fork, before-after, cause-effect · fits 1 path, 2 directions
- Reader sees: an arrow or path slowly turns from one direction to another as you read why it changed.
- Moves: scroll-linked - rotate 0 to at most 30° over ~35vh, linear with scroll, soft start, no overshoot.
- Build: `transform:rotate(calc(var(--p)*22deg))` with `transform-box:fill-box; transform-origin:50% 55%`.
  Pair with a drawn trail behind the pivot point so the old heading stays visible as a ghost.
- Narrow: same · Reduced motion: two arrows, old one ghosted at 25%.
- Use when: a strategy, route or plan changes direction for a stated reason · Avoid when: nothing actually changed course.
- Effort: S · Source: video, key_06_rocket-pivot-gravity-turn.png / burst_06_gravity-turn.png
