# Motion and atmosphere: moments, texture, mood

Pattern library family for `pitch-site-udyaan`. 24 entries (5 starred), curated from slice6, motion family (44 raw entries).
Verdicts: 4 KEEP, 18 ADAPT, 2 NEW, 19 CUT (listed at the end; 3 of the cuts moved to architecture).

**Shorthand used in every entry (house motion values):**
- **pen draw**: `stroke-dashoffset` from the path length to 0; duration = length / 600 px/s, clamped to 0.6-2.2s; the next stroke starts at 80-85% of the previous one; ease cubic-bezier(.45,.05,.35,1). Lines never overshoot, bounce or erase themselves.
- **arrive**: opacity 0 to 1 plus a rise of 16px or less, 0.6-1.0s, cubic-bezier(.22,1,.36,1); runs once and always finishes. Nothing enters from the side, rotates or flies.
- **scroll-linked**: linear, tied 1:1 to native scroll. Drawings may follow scroll back and forth; text never does.
- **stagger**: 60-110ms per item, total capped at 450ms. Taps and UI: 0.2-0.3s. Ambient loops: 3-7s.
- **budget**: one moving thing per screen, at most one ambient loop per screen, asleep off-screen (ARC-25). If a line, a number and a mark share a screen, play them in that order at 0.3s gaps or cut two.
- **finished state**: reduced motion, repeat visits and `?final=1` all land on the finished drawing with labels (ARC-24). Every effect has a static twin below 768px.
- **accent**: one colour does the pointing; everything else is ink, paper and flat chalky tints. Texture never animates.

**Cross-family overlaps to settle at assembly:** MOT-02 and order-time SEQ-01 (snake); MOT-03 and change-choice CHG-10 (scroll wipe); MOT-05 and structure-links STR-26 (pullback); MOT-09 and CHG-27 / SEQ-02 (one knob per step). This file holds the motion mechanics; the sibling entries hold the content devices.

---

## Picker: purpose to pattern

Starred first. One purpose per screen.

- **Reveal a relationship** (this feeds that, these two connect): MOT-01 ★, MOT-02 ★, MOT-06.
- **Show a change** (today, then with us): MOT-03 ★, MOT-04 ★, MOT-07.
- **Show scale** (a detail inside the whole, a jump in size): MOT-05 ★, MOT-08, MOT-06.
- **Walk through steps on one drawing**: MOT-04 ★, MOT-09, MOT-07.
- **Mark progress or a chapter**: MOT-04 ★, MOT-22 (counters and rulers live in architecture: ARC-28, ARC-29).
- **Show an amount or a gain**: MOT-10, MOT-11.
- **Point at the key phrase or part**: MOT-12, MOT-16.
- **Open a section**: MOT-13, MOT-14, MOT-23.
- **Land the ask**: MOT-15, then MOT-18 if the closing drawing needs warmth.
- **Set mood** (texture, identity, warmth): MOT-19, MOT-21, MOT-18. Further options: MOT-20, MOT-17, MOT-24.

---

## Relationship, change and scale

### MOT-01 ★ Travelling pulse
- For: cause-effect, place-network · 1 line at a time, 1-3 per section
- Instead of: an arrow icon between two boxes
- Reader sees: a small accent dot runs along the line from the cause to the result, and the result gets a pen ring when the dot arrives.
- Moves: in-view, after the line has drawn - the dot travels `offset-distance` 0% to 100% over max(2.4s, length / 250 px/s), ease cubic-bezier(.45,.05,.35,1), once (twice at most); on arrival the end node gets a pen-drawn accent ring (0.6s). Only the line being discussed pulses.
- Build: dot is a 6-8px accent circle with `offset-path: path(<the connector's own d>)` and `offset-rotate: 0deg`; start it with the Web Animations API, chained to the connector draw's `finished` promise.
  If it must loop (it counts as the screen's one ambient loop): 4.4s period with the dot visible for the first 45%, paused off-screen (ARC-25). The TVS constellation loop never stopped and ran while hidden; fix both.
- Narrow: below 768px the static twin shows the connector with an arrowhead and the end ring · Reduced motion: no dot; arrowhead plus end ring.
- Use when: "this input feeds that result", or a handoff between two teams. · Avoid when: the line is not the subject of the current caption, or something else on screen moves.
- Effort: S · Needs lib: no · Code: TVS harvest (2.3 pulse loop) · Sources: P351 https://developer.mozilla.org/en-US/docs/Web/CSS/offset-path, TVS constellation pulse (01-tvs-harvest 2.3) · Verdict: ADAPT, changed: 1.6s ease-in-out traverse slowed to 2.4s or more on the pen ease; the end node's scale pop became a drawn ring; runs once.

### MOT-02 ★ Scroll-drawn connector over a faint guide
- For: sequence, cause-effect · 1 path per section, 3-6 stops
- Instead of: numbered cards with arrow icons between them
- Reader sees: a faint dotted path links the cards of one section; as they scroll, a solid ink line traces it, and each stop's knot fills when the ink reaches it.
- Moves: scroll-linked - ink path `stroke-dashoffset = L × (1 - reach / height)` with reach = clamp(0, height, 0.62 × innerHeight - top), linear; knot fill 0.3s ease-out when reached. Short connector between two blocks: pen draw on view instead.
- Build: two paths with the same `d`: the guide (`stroke-dasharray: 1 8` at 22% ink, or dash-dot `.93 2.8 9.35 2.8`) and the ink line (2.4px). The path runs through measured knot centres with `C x0 (y0+dy×.55), x1 (y1-dy×.55), x1 y1`; rebuild on resize, load and `document.fonts.ready`, debounced.
  Read layout once per scroll inside requestAnimationFrame (TVS read it on every scroll event). CSS-only variant: `pathLength="1"`, `stroke-dasharray: 1`, `animation-timeline: view()`, `animation-range: entry 50% cover 60%`, inside `@supports`.
  The line lives inside one section. It never runs behind the copy for the whole page.
- Narrow: below 820px the path becomes a left rail (one column, margin-left 46px, segments wiggle ±14px); below 768px drawn and static · Reduced motion: line fully drawn, every knot filled.
- Use when: a chain of problem-then-answer stops should read as one journey and scrolling is the progress. · Avoid when: stops are unordered, there are more than 6, or the line would run through the whole page (Ash rejected that).
- Effort: M · Needs lib: no · Code: TVS harvest (2.2 Snake) · Sources: P345 https://developer.chrome.com/docs/css-ui/scroll-driven-animations, TVS snake (01-tvs-harvest Part 1 and 2.2) · Verdict: ADAPT, changed: added the faint guide and knot fill from the TVS snake; pen-draw fallback; rAF-throttled reads; scoped to one section.

### MOT-03 ★ Scrubbed before/after wipe
- For: before-after · 1 pair per section
- Instead of: two pictures side by side labelled "Before" and "After"
- Reader sees: the "today" line drawing is wiped away by the "with us" drawing as they scroll, behind a thin pen-line divider that rides the edge.
- Moves: scroll-linked - top layer `clip-path: inset(0 100% 0 0)` to `inset(0)` across `contain 0%` to `contain 70%`, linear; the drawing holds still for the last 30%; when the wipe completes, the "With us" label gets a marker sweep.
- Build: two SVGs in the same viewBox, stacked in one figure; both share outlines so only the changed parts catch the eye. Divider is a 1.5px ink line with a small hand-drawn grip mark, placed by the same progress value.
  `@supports (animation-timeline: view())`, with an IntersectionObserver fallback that plays the wipe once over 1.2s cubic-bezier(.45,.05,.35,1).
- Narrow: below 768px the pair stacks, today above and with us below, labelled · Reduced motion: the stacked labelled pair.
- Use when: the offer visibly changes one scene (a shop floor, a form, a week). · Avoid when: the difference is small or lives in the words; use a strike-and-replace instead.
- Effort: S · Needs lib: no · Sources: P367 https://emilkowal.ski/ui/the-magic-of-clip-path · Verdict: ADAPT, changed: photos became matched line drawings; the divider is a pen line; the fallback plays once on the draw ease; static twin below 768px.

### MOT-04 ★ Colour arrives one hue at a time (new)
- For: before-after, part-whole, sequence · 3-6 hues across one stage or one page
- Instead of: a full-colour illustration shown all at once
- Reader sees: the drawing starts as ink lines on paper; each step floods one region with a flat chalky tint (the suppliers turn turmeric, then the plant turns indigo-grey), so by the ask the picture is fully coloured and every colour has been explained.
- Moves: in-view per step on a pinned stage, or per section - the step's region `fill-opacity` 0 to 1 over 0.8s cubic-bezier(.22,1,.36,1); the caption names the part with a chip in the same tint. One hue per step; earlier hues stay.
- Build: one SVG; each region is a `<path>` with `fill: var(--tint-n); fill-opacity: 0` beneath the ink layer, so lines stay crisp. The step writes cumulative `data-hue="1 2 3"` on the stage; CSS `[data-hue~="2"] .r-2 { fill-opacity: 1 }`.
  Flat fills only; grain sits above as static texture. Tints come from the page's section palette, so a region's colour matches the band that explains it.
- Narrow: below 768px each step's static twin shows the drawing with hues up to that step · Reduced motion: hues for the current step present without the fade.
- Use when: several parts of one system each need a name and the reader should end on the whole picture (Ash's Washington Post reference). · Avoid when: colour would be the only label (always name the part), or there are more than 6 parts.
- Effort: S · Needs lib: no · Sources: new; built from the Washington Post pinned-subject reference and the TVS section tints (01-tvs-harvest Part 3) · Verdict: NEW

### MOT-05 ★ Pull-back reveal
- For: part-whole, big-idea · 1 per page, 2-3 zoom levels
- Instead of: opening with the full system diagram
- Reader sees: the section opens close on one detail (a single form, one worker's hands), and as they scroll the view pulls back to the whole system that detail sits in, with labels arriving last.
- Moves: scroll-linked - pinned drawing `scale(3)` to `scale(1)` with `transform-origin` at the detail, linear, over 1-1.5 viewport heights; then labels arrive (0.6s, 80ms apart, capped at 450ms).
- Build: one SVG drawn at full detail; strokes use `vector-effect: non-scaling-stroke` so line weight stays even while scaling. Sticky wrapper inside a 200-250svh section (pin under 3 viewport heights); progress from `animation-timeline: view()` with an rAF fallback writing `--p`.
  Two-stop version: 3 to 1.6 to 1, with one caption at each stop.
- Narrow: below 768px two static crops (the detail, then the whole) with a "zoom out" caption between · Reduced motion: 0.6s crossfade from the cropped detail to the whole.
- Use when: "one small thing explains the whole picture" (one late invoice explains the cash problem). · Avoid when: used more than once per page (big zooms are a vestibular trigger), or the drawing blurs at 3×.
- Effort: M · Needs lib: no · Sources: P362 https://www.smashingmagazine.com/2020/09/design-reduced-motion-sensitivities/ · Verdict: ADAPT, changed: line drawing with non-scaling strokes; pin capped under 3 viewport heights; labels wait for the move to end; static twin added.

### MOT-06 Reach rings
- For: place-network, quantity-scale · 1 boundary, 5-7 rings
- Instead of: a shaded circle labelled "reach"
- Reader sees: soft parallel rings draw outward from an edge (a campus, a district), fading as they spread like contour lines, to show how far an effect travels.
- Moves: in-view, once - each ring is a 0.6s pen draw, started 70ms after the previous (whole group within 450ms); static afterwards.
- Build: concentric `<circle>` or offset `<path>` strokes, opacity stepping from 0.35 down to 0.03; the true boundary is the brightest line, in ink; rice-powder filter (MOT-19) at displacement scale 1.5 for the hand feel. Label the outer ring with the real distance or count.
- Narrow: below 768px 4 rings, static · Reduced motion: rings drawn.
- Use when: an edge or a reach is the point (villages served, a market's radius). · Avoid when: the rings are only mood; then cut them.
- Effort: S · Needs lib: no · Sources: P467 (video-anim-study, key_05 zoom-out limb bands, key_09 satellite) · Verdict: ADAPT, changed: 60ms × 12 rings broke the stagger cap, so 5-7 rings at 70ms; pen ease; labelled outer ring.

### MOT-07 State morph
- For: before-after, part-whole · 2-4 states
- Instead of: two separate diagrams with "becomes" printed between them
- Reader sees: one shape smoothly becomes another in place: a messy pile of forms becomes one neat stack, a scatter of dots lines up into a row.
- Moves: in-view or per step - shapes move between states over 0.9s cubic-bezier(.45,.05,.35,1); one morph at a time.
- Build: same-document `document.startViewTransition(() => setState(n))` with unique `view-transition-name`s and `::view-transition-group(*) { animation-duration: .9s; animation-timing-function: cubic-bezier(.45,.05,.35,1) }`. For SVG paths, interpolate `d` between paths with matching command counts. Unsupported browsers get a 0.4s crossfade.
- Narrow: below 768px both states stacked with "becomes" between · Reduced motion: 0.4s crossfade (reduced motion still gets a gentle change).
- Use when: the offer turns one thing into another the reader recognises. · Avoid when: the two shapes share nothing (the morph reads as a glitch).
- Effort: M · Needs lib: no · Sources: P349 https://developer.chrome.com/docs/web-platform/view-transitions/same-document · Verdict: ADAPT, changed: curve moved to the house in-out at 0.9s; one morph per screen; stacked twin.

### MOT-08 Match-cut on scale (new)
- For: quantity-scale, part-whole · 1 per page
- Instead of: a big number followed by "that's like 40 football fields"
- Reader sees: one outline (a single grain of rice) grows until it fills the frame, and in the same place an identical outline reappears as something huge (a field shaped like the grain), so the eye jumps scales without losing its place.
- Moves: scroll-linked, inside one pinned stage step - outline A scales up linearly until it fills the frame; at progress 0.6 it fades out over 0.3s while drawing B, whose matching outline is already in place, pen-draws its inner detail (0.6-1.2s); the caption gives the real ratio.
- Build: two SVG drawings whose key outline uses the same path `d`, B positioned so the outlines coincide at the cut; `vector-effect: non-scaling-stroke`. The cut fires once at the threshold and only reverses when the reader scrolls back past it.
- Narrow: below 768px two stills with a caption such as "same shape, 4,000 times bigger" · Reduced motion: the two stills side by side.
- Use when: a jump in scale is the argument (one student's notebook to a whole district). · Avoid when: the ratio is invented, or the two shapes only loosely match.
- Effort: M · Needs lib: no · Sources: new; built from the Washington Post match-cut on scale · Verdict: NEW

### MOT-09 Caption steps change one thing
- For: sequence, part-whole · 3-5 steps per pinned stage
- Instead of: one diagram per point
- Reader sees: a drawing holds still while short captions scroll past; as each caption reaches the middle, exactly one thing in the drawing changes; the current caption is full ink and the others are faded.
- Moves: in-view at the mid-line - the step's change plays once (a pen draw, or a fill or label arriving over 0.6-0.8s); captions fade from .35 to 1 over 0.3s; the n / N counter updates (ARC-29).
- Build: one IntersectionObserver with `rootMargin: "-45% 0px -45% 0px"` writes `data-step` on the stage; CSS keys every state off `[data-step]`, cumulatively. Step spacing in px from `innerHeight` (phone bars change vh). The change finishes within the first half of the caption's travel, so the drawing rests while the caption is read. Scrolling back shows the previous state instantly.
- Narrow: below 820px the stage pins to the top 50svh with captions as solid paper cards beneath; below 768px the static twin, one drawing per step · Reduced motion: each step's end state, 150ms opacity swaps only.
- Use when: one drawing can carry the argument in stages (page structure: ARC-02). · Avoid when: a step needs a different drawing, or a pin would need more than 5 steps.
- Effort: M · Needs lib: no · Sources: P346 https://pudding.cool/process/how-to-implement-scrollytelling/, P364 (merged: active-step focus) · Verdict: ADAPT, changed: one change per step; house durations; counter added; the change completes before the caption is half read.

---

## Amounts and emphasis

### MOT-10 Number counts to its value
- For: quantity-scale, before-after · 1-3 numbers per screen
- Instead of: a static big number
- Reader sees: a key figure counts up to its value as it arrives; when there is an old value, its digits roll from old to new.
- Moves: in-view, once - count over 0.9s cubic-bezier(.22,1,.36,1); roll variant: each digit column slides over 0.75s on the same curve; numbers sharing a screen start 0.3s apart.
- Build: `font-variant-numeric: tabular-nums` so the width never jumps. The real value is the HTML text and the accessible name; JS animates a visual copy only. Integers via `@property --n { syntax: '<integer>'; inherits: false; initial-value: 0 }` with `counter-reset: n var(--n)`; decimals via rAF on the same curve.
- Narrow: same · Reduced motion: final value.
- Use when: the number is the gain, or a value changes from today to after. · Avoid when: more than 3 numbers share a screen, or the figure is a guess.
- Effort: S · Needs lib: no · Sources: P347 https://css-tricks.com/animating-number-counters/, P348 https://number-flow.barvian.me/ · Verdict: ADAPT, changed: count-up and odometer merged; 1.2s expo became the 0.9s house arrival; 0.3s spacing between numbers.

### MOT-11 Scrubbed gauge
- For: quantity-scale · 1 per section
- Instead of: a progress bar that animates on page load
- Reader sees: a hand-drawn meter fills as they read the section ("hours back each week"), and the value is printed where the fill ends.
- Moves: scroll-linked - fill `scaleX(0)` to `scaleX(var(--v))`, linear, `animation-range: entry 20% cover 50%`; the value label arrives (0.6s) when the fill completes.
- Build: `@property --v`; the track is a pen outline with the rice-powder filter, the fill is the accent. IntersectionObserver fallback plays the fill once over 1.0s cubic-bezier(.45,.05,.35,1). The value is always printed as text.
- Narrow: same · Reduced motion: filled, value shown.
- Use when: one measure of gain or progress per section. · Avoid when: the exact number matters more than the fill (use MOT-10).
- Effort: S · Needs lib: no · Sources: P366 https://developer.chrome.com/docs/css-ui/scroll-driven-animations · Verdict: ADAPT, changed: pen-drawn track, accent fill, printed value, house curve on the fallback.

### MOT-12 Teacher's marks in order
- For: emphasis, proof-trust · 2-3 marks per screen
- Instead of: bold text plus a yellow highlight on everything
- Reader sees: on their document or a screenshot, a pen circles one phrase, then underlines another, then brackets a paragraph, one after another, like a teacher marking.
- Moves: in-view - each mark is a pen draw; each next mark starts at 80-85% of the previous; all marks in the one accent.
- Build: hand-drawn SVG paths (an ellipse with an overshooting tail, a wavy underline, a bracket) generated around measured text boxes from `Range.getClientRects()`, in an absolutely positioned overlay; rebuild on resize; chain each draw on the previous animation's `finished` promise.
- Narrow: same, re-measured on resize · Reduced motion: all marks present.
- Use when: walking through their brief, a contract clause or a screenshot. · Avoid when: more than 3 marks per screen, or a marker sweep is already playing in view.
- Effort: M · Needs lib: no · Sources: P365 https://github.com/rough-stuff/rough-notation · Verdict: ADAPT, changed: Rough Notation replaced by vanilla pen paths on house timing; capped at 3 marks per screen; one accent.

---

## Section openers and the close

### MOT-13 Headline lines rise from masks
- For: big-idea · 1-3 line headline, 2-3 per page
- Instead of: the whole heading fading in as one block
- Reader sees: each line of a chapter headline slides up from behind an invisible edge, one line after another.
- Moves: in-view, once (top at 88% of the viewport) - inner span translateY(105%) to 0 over 0.9s cubic-bezier(.22,1,.36,1); lines 80ms apart, capped at 450ms; always finishes.
- Build: split by measured lines (wrap words in spans, group by `offsetTop`, re-split on resize); line wrapper `overflow: clip`; spans `aria-hidden` while the heading keeps its full text for screen readers. Headings visible at load render in place.
- Narrow: re-split at the new width · Reduced motion: visible, no motion.
- Use when: chapter openers, and the hero headline once its drawing is under way. · Avoid when: body text, or more than 3 split headlines on the page.
- Effort: S · Needs lib: no · Sources: P354 https://studiomeyer.io/en/blog/kinetische-typografie · Verdict: ADAPT, changed: house arrival curve; 80ms line stagger capped at 450ms; measured lines; plays once.

### MOT-14 Picture unveils in place
- For: proof-trust · 1 image per screen
- Instead of: an image that pops in or slides from the side
- Reader sees: a real screenshot or site photo is uncovered from top to bottom in its final spot, with no layout jump.
- Moves: in-view, once (100px inside the viewport) - `clip-path: inset(0 0 100% 0)` to `inset(0)` over 0.9s cubic-bezier(.22,1,.36,1).
- Build: IntersectionObserver `rootMargin: '0px 0px -100px 0px'`; the frame reserves its size with `aspect-ratio` so nothing shifts. Raster images only; line drawings pen-draw instead.
- Narrow: same · Reduced motion: visible.
- Use when: proof images (real screenshots, site photos). · Avoid when: the image holds text the reader would try to read mid-reveal.
- Effort: S · Needs lib: no · Sources: P355 https://emilkowal.ski/ui/the-magic-of-clip-path · Verdict: ADAPT, changed: curve moved from (.77,0,.175,1) to the house arrival; limited to raster proof images.

### MOT-15 Ask lands, pen underlines the contact
- For: call-to-action · 1 per page
- Instead of: a big button that bounces or pulses
- Reader sees: the closing card with a named person arrives, a single pen line draws under the person's name (or a ring around the one button), and then everything sits still.
- Moves: in-view, once - the card arrives (12px, 0.8s); then the underline pen-draws (0.9s) in the accent; the button presses to scale .96 over 150ms.
- Build: the underline is a hand-drawn SVG path sized to the name's measured width, chained after the card's arrival. No spring, no overshoot. This is the last meaningful motion on the page; earlier motion resolves into it.
- Narrow: same · Reduced motion: card present, underline drawn.
- Use when: every page; the page ends in the ask. · Avoid when: two buttons compete at the close (cut one).
- Effort: S · Needs lib: no · Sources: P370 https://developer.chrome.com/docs/css-ui/css-linear-easing-function · Verdict: ADAPT, changed: the spring overshoot (.94 to 1.02 to 1) removed; a pen underline does the pointing.

---

## Identity and atmosphere

### MOT-16 Motif with addressable parts
- For: atmosphere, part-whole · 1 motif with 3-6 named parts, reused 3-7 times
- Instead of: a decorative hero image used once
- Reader sees: the client's own motif (the TVS kolam) draws itself in the hero, returns as a key where each part stands for one ask, and shrinks to a badge beside each ask's section with that part lit.
- Moves: on call - `play()` draws the parts in reading order with pen timing; `focus(part)` fades the other strokes to 16% over 0.6s ease-out; `finish()` renders it complete.
- Build: one function `drawMotif(svg, opts)` returns `{ play, finish, focus }`; every stroke carries `data-stage` (centre, band0-2, flower0-5) so `focus('flower')` matches by prefix; unique ids per instance for filters and clipPaths.
  Fix the TVS bugs: give the focus fade its own `transition: opacity .6s` (appending to `none` made it invalid); compute costly geometry (the kolam's crossing search) once and reuse it for every instance; skip `play()` on hidden instances.
- Narrow: scales with its viewBox · Reduced motion: `finish()`.
- Use when: one culturally right motif can carry the structure (each ask maps to a part). · Avoid when: the motif is borrowed decoration with no meaning, or a static SVG would do.
- Effort: L · Needs lib: no · Code: TVS harvest (2.12) · Sources: P002 (TVS site, preview/kolam.js L1-128) · Verdict: ADAPT, changed: generalised from the kolam to any client motif; focus-fade and repeated-cost bugs fixed.

### MOT-17 Grains settle into the line
- For: atmosphere, big-idea · 1 per page, at the opening or the close
- Instead of: a logo fade-in
- Reader sees: scattered powder grains drift and gather into the page's motif or the outline of the idea, then the crisp line appears under them, as if the pattern had always been in the dust.
- Moves: in-view, once - 1.5-3k grains ease toward target points over 2.5s while their jitter decays to zero; then the SVG line pen-draws or arrives over 0.6s; the loop stops when settled.
- Build: Canvas 2D, devicePixelRatio aware; targets sampled along the SVG path with `getPointAtLength` every 1-2px; each grain steps toward a random nearby target in proportion to its distance; stop rAF once every grain is within 0.5px; never re-run; pause off-screen. No WebGL.
- Narrow: 1-1.5k grains · Reduced motion: final line over a static grain texture.
- Use when: the motif is made of powder, seed, sand or thread and the opening needs one memorable beat. · Avoid when: anything else on the screen moves, or a hero draw-on already uses the opening.
- Effort: L · Needs lib: no · Sources: P434 http://chladni-plate-experiment.vercel.app · Verdict: ADAPT, changed: settle capped at 2.5s; the line follows as a pen draw; never repeats; one per page.

### MOT-18 One breathing detail
- For: atmosphere · 1 per screen, 1-2 per page
- Instead of: a looping animated illustration
- Reader sees: in an otherwise still drawing, one small thing gently breathes (the kolam's centre dot, a lamp's glow, a sleeping dog), so the page feels alive without asking for attention.
- Moves: ambient - scale 1 to 1.004-1.013 (never past 1.015) and/or translateY of 2px or less, 3.2-4.7s ease-in-out, infinite; optionally one tiny accent every 9s (an ear twitch).
- Build: CSS keyframes on one `<g>` with `transform-box: fill-box; transform-origin: center bottom`; starts only after the drawing finishes; sleeps off-screen (ARC-25); stops under the Still switch (ARC-26).
- Narrow: same · Reduced motion: still.
- Use when: a hero or closing drawing needs warmth after its draw-on. · Avoid when: anything else on the screen moves.
- Effort: S · Needs lib: no · Sources: P414 https://foxvaluations.com.au, https://townhouse.dev · Verdict: KEEP

### MOT-19 Rice-powder line filter
- For: atmosphere · any stroked SVG line art
- Instead of: crisp vector lines that look machine-made
- Reader sees: lines that look poured or chalked by hand, with a slight waver, gritty edges and a soft bloom.
- Moves: none (a static filter; texture never animates).
- Build: feTurbulence fractalNoise baseFrequency .035, 2 octaves, seed 7, into feDisplacementMap scale 5 (hand wobble); feTurbulence 1.1, 1 octave, seed 3, into feDisplacementMap scale 2.4 on that result (grit); feGaussianBlur 1.1; feMerge [blurred, gritty]. Filter region -5% / 110%.
  Small drawings (about 200px): .05 / 2.6, 1.2 / 1.4, blur .55. Apply it to the stroke group; dashoffset draws still play under it.
- Narrow: same · Reduced motion: n/a (static).
- Use when: line art should feel chalk, powder or brush made, especially on a dark ground. · Avoid when: text or icons under about 16px, or many large filtered SVGs animate at once (filter repaint cost).
- Effort: S · Needs lib: no · Code: TVS harvest (2.12 filter defs) · Sources: P003 (TVS site, preview/kolam.js L10-16; page.html L1162-1168) · Verdict: KEEP

### MOT-20 Paper and wood grain
- For: atmosphere · every band
- Instead of: flat digital fills
- Reader sees: a faint paper tooth on the light sections and long wood-grain streaks on the dark ones.
- Moves: none (static).
- Build: JS prepends `<span class="grain" aria-hidden="true">` to every `.band` (absolute, inset 0, z-index 1, pointer-events none). Paper: data-URI SVG, 240px tile, fractalNoise .9, 3 octaves, stitchTiles, colour matrix to brown (.12, .09, .07) at alpha .08; layer opacity .55, multiply.
  Wood: 600px tile, baseFrequency `.004 .32` (stretched noise reads as streaks), seed 4, alpha row `.55 -.18`; opacity 1, normal blend.
- Narrow: same · Reduced motion: n/a.
- Use when: flat colour feels too digital for a craft or heritage story. · Avoid when: the page is photo-heavy (grain doubles up).
- Effort: S · Needs lib: no · Code: TVS harvest (Part 3 base layer) · Sources: P036 (TVS site, page.html ~L35-37, L938) · Verdict: KEEP

### MOT-21 Chalk section tints with dark doorstep bands
- For: atmosphere, grouped-list · 8-13 bands, 3-4 of them dark
- Instead of: white sections divided by rules, or a nav menu
- Reader sees: every section is a full-width flat chalky wash (paper, turmeric, indigo-grey, laterite), and 3-4 deep brown bands with cream text act as doorsteps: the hero, the key, the turning idea and the close.
- Moves: none; a change of colour marks a new chapter and tints stay flat.
- Build: `.band { position: relative; padding-block: clamp(80px, 11vw, 140px); overflow-x: clip }`, colour set inline or by class; content in `.wrap` (max 1180px, gutters max(24px, safe-area)) at z-index 2 above the grain.
  `.woodbg { background: #3A2B22; color: #F4F1EA }` with label #C9B8A6, lede #E6DCCF, body #D9CDBF. Cards on washes use rgba(255,255,255,.4-.5); on dark, rgba(244,241,234,.06) with a .12-.14 ring.
  New clients get new hues on the same rules: chalky and flat; no navy hero, no green, and never Anthropic's clay with ivory.
- Narrow: padding clamps down to 80px · Reduced motion: n/a.
- Use when: a long single scroll needs chapters without a nav (ARC-01). · Avoid when: dark bands pass 1 in 3 sections, or two adjacent sections share a topic (keep one colour).
- Effort: S · Needs lib: no · Code: TVS harvest (Part 3) · Sources: P035, P037 (TVS site, page.html ~L8-39, L466-878) · Verdict: KEEP (merged; palette guard added)

### MOT-22 Chapter numeral wall graphic
- For: atmosphere, sequence · 4-8 chapters
- Instead of: a small "Section 3" eyebrow on its own
- Reader sees: each chapter opens with an enormous numeral painted across the screen like a wall graphic, cropped at the edges and faint behind the headline, so they always know which "floor" they are on.
- Moves: none; the numeral is already in place when the chapter arrives.
- Build: the numeral in the display serif at `font-size: 40vw; opacity: .07; position: absolute; z-index: 0`, cropped by the band's `overflow: clip`; `aria-hidden`, with the real number in the eyebrow text. Same numeral style as the stage counter (ARC-29), so wayfinding reads as one system.
- Narrow: 55vw · Reduced motion: n/a.
- Use when: a long page has 4 or more chapters that might blur together. · Avoid when: fewer than 4 chapters, or the band already holds a large drawing.
- Effort: S · Needs lib: no · Sources: P260 https://www.pentagram.com/work/museum-fuer-film-und-fernsehen-2376/story · Verdict: ADAPT, changed: parallax and sticky removed; a static numeral cropped by its band.

### MOT-23 Historiated initial
- For: atmosphere, emphasis · 1 per chapter, 3-6 chapters
- Instead of: a plain drop cap or a stock icon
- Reader sees: a chapter's first letter is large and holds a tiny scene of what the chapter is about (a farmer inside the F), drawn in the same line as the motif.
- Moves: in-view, once - the letter's outline pen-draws, then the scene inside starts at 80% of the outline's draw.
- Build: `<span class="dropcap" aria-hidden="true"><svg>` floated left with `width: 4.2em; shape-outside: margin-box`; the real letter stays in the text, visually hidden, for screen readers; `initial-letter: 3` sizes the plain fallback.
- Narrow: 3em initial · Reduced motion: drawn.
- Use when: chapters open with a paragraph long enough to wrap around it, and the scene previews the chapter's point. · Avoid when: sections are short cards or two-sentence spines.
- Effort: M · Needs lib: no · Sources: P253 https://en.wikipedia.org/wiki/Initial · Verdict: ADAPT, changed: house pen timing; the scene must preview the chapter's point.

### MOT-24 Margin drolleries, drawn once
- For: atmosphere, people-roles · 2-4 per page
- Instead of: a dry paragraph with no human touch
- Reader sees: a tiny figure in the margin reacts to the text beside it (a snail racing the old manual process), with a one-line handwritten aside.
- Moves: in-view, once - the doodle pen-draws (0.6-1.0s) when its paragraph reaches the middle of the screen, then stays still.
- Build: absolutely placed SVGs in a margin grid column; one IntersectionObserver toggles a class; the aside is set in the hand face. No idle loops (loops beside text break the house rules).
- Narrow: below 820px the doodle moves inline as a small icon after its paragraph · Reduced motion: drawn.
- Use when: a long, dry stretch needs personality without a new section. · Avoid when: beside data, beside sad content, or next to another moving thing.
- Effort: S · Needs lib: no · Sources: P255 https://en.wikipedia.org/wiki/Marginalia · Verdict: ADAPT, changed: idle loops removed; drawn once; capped at 4 per page.

---
