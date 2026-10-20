# QA checklist

Run this before the reviewers and again before publishing. Most bugs on these pages only show in the render, at a
particular width, or mid-animation, so reading the code is not enough.

## Steps
1. **Build:** `python scripts/build.py work/` (prints size and the dash count in copy; must be 0).
2. **Copy scan:** `python scripts/scan.py work/index.html --facts work/facts.md`. Fix every hit except quoted examples.
3. **Sweep:** `python scripts/sweep.py work/index.html --out work/shots/`. It writes final-state frames at
   1280x800, 1024x768, 768x1024 and 744x1133 (iPad mini), live mid-scroll frames at 1280x800, a 390x844 frame (must show
   only the phone gate), and prints console errors, horizontal overflow and class-name collisions.
4. **Look at every frame.** Things to look for:
   - the hero fills exactly one screen and nothing from the next section shows
   - labels crossing lines, labels over each other, text cut at an SVG edge
   - a heading glued to the block under it (a hidden spacer), dead space under a heading
   - cards in a row with misaligned footers
   - the pinned stage actually pinned, its counter matching the caption
   - the marker covering every wrapped line, and readable on dark bands
   - colours that look neon, muddy or too alike; any green
5. **Covered tests** (`../story-plan/references/film-craft.md`): read the copy alone, then look at the frames alone. Move any claim
   the words carry that a picture should, and cut any line that only narrates its picture.
6. **Faithfulness:** every ask quoted verbatim, every number in facts.md, one name per need everywhere.
7. **Reviewers:** references/review.md.
8. **Publish** as a private artifact (load the artifact-design skill first), then tell Ash to run `/verify`
   (the model cannot invoke it).

## Done means
Zero scan hits, zero console errors, no overflow at the four tablet and laptop sizes, the phone gate at 390px,
creative director SHIP or REVISE with every HIGH fix applied, reader CLEAR, published, hand-off note written.

## Bugs already hit, and the fixes

**Layout and CSS**
- Generic class names (`.use`, `.tr`, `.stop`, `.head`, `.c-label`) collided across sections and silently broke
  layouts. Fix: prefix every class with its section (`stg-`, `swb-`); sweep.py lists collisions.
- A `<mark>` inside a grid or flex parent is blockified: the highlight covers only the last line, or gaps appear
  around it. Fix: keep marks inside a `<p>` of running text.
- The 40%-height marker band on dark cards hides the top half of dark text. Fix: a full-height pill on dark.
- A rotated element (the tilted check sheet) overflowed sideways on upright tablets. Fix: `overflow-x: clip` on
  bands and no tilt below 820px.
- A `transform: rotate(90deg)` element reserves its unrotated height; the arrow ran through its caption. Fix: give
  it explicit width, height and margin.
- `display: none` on the only spacer glued a heading to the cards below. Fix: explicit margins.
- Lines ran through labels (orbit ring, map edges). Fix: labels get a paper background halo and `z-index: 1`.
- Absolutely positioned labels crossed the page gutter at 1024px. Fix: narrower ellipse and fixed label width.
- Cards of different heights misaligned their "Answered by" rows. Fix: CSS subgrid or `margin-top: auto` footers.
- Callouts of different heights did not line up. Fix: equalise heights on load, resize and `document.fonts.ready`.
- Diagonal connectors pointed at nothing once callouts stacked on tablets. Fix: hide connectors below 820px.
- One-column frames at 768px made 1,900px of scroll. Fix: smaller frames, tighter padding below 820px.
- The Copy button grew when its label changed. Fix: `min-width: 140px`.
- The page looked 10px too wide on a phone check: it was the scrollbar. Compare `scrollWidth` with `clientWidth`.
- `position: sticky` did nothing inside a band with `overflow-x: clip`. Fix: the stage band sets `overflow: visible`.
- Behind the phone gate `main` is hidden, so every measured layout (leader lines, cords) computed NaN and filled the
  console with errors. Fix: return early when the measured box has no width or height. sweep.py's phone frame checks it.
- The final-state still showed step 4 of a pinned stage next to all five captions, and the pull-back never appeared in
  any still. Fix: under `?final=1` hide the counter and put a static still of the last step inside its caption card.

**Drawing and motion**
- The first kolams read as "circles", then "chain-link fence". Fix: tune a motif on its own test page against the
  reference photo before splicing it in.
- The hero kolam looked unfinished in a screenshot: the hidden browser pane pauses animation frames. Fix: judge
  layout with `?final=1`, judge motion with the pane visible.
- A page-long line behind the copy was "distracting from the message". Fix: lines live inside one visual or gutter.
- The mind map "drew once and died". Fix: node dots, distance-based label delays, one slow pulse on the active edge.
- A hover hint showed on touch devices. Fix: hover hints only under `@media (hover: hover)`.
- The translator's jump waited for a pending timer. Fix: cancellable waits (a generation counter and `cancelAll()`).
- An auto-advancing six-term carousel set the reader's pace. Fix: progress bars are tappable buttons (24px hit area).
- penDraw turned dashed guide lines solid. Fix: draw dashed lines through a mask, or fade them in.
- Drawn icons misread at small size (a "new product" sketch read as a food cloche; the portrait's hair as a helmet,
  dot eyes as an emoji). Fix: check each drawing at its real size; eyelid strokes and a fringe line for faces.
- Copy button timers stacked on rapid clicks. Fix: clear the previous timeout first.
- The snake read layout on every scroll event. Fix: read once per frame inside requestAnimationFrame.
- The constellation pulse kept running off-screen. Fix: loops sleep when their section leaves the viewport.

**Tooling**
- The browser pane refuses `file://` pages. Fix: serve with `python -m http.server` from a `.claude/launch.json` entry.
- `python -I` drops user site-packages, so Playwright fails to import. Fix: run the skill's scripts with plain `python`.
- Bash heredocs broke on quotes in edit scripts. Fix: write edit scripts to a file, or use the Edit tool.
- Edit scripts that silently matched nothing. Fix: every find-and-replace prints `missing:` for unmatched strings.
- Emulated viewports larger than the pane get scaled. Fix: confirm `innerWidth` with JS or use sweep.py.
- `/verify` cannot be invoked by the model. Fix: run this checklist and tell Ash to type `/verify`.
- **A device drawn as a rendered slab.** The Coastline tablet shipped as a dark rounded panel with a glowing dot and
  broke the "same hand" rule; it is now an outlined sheet in the drawing's line with the warm reading in red.
- **Paged sheets taller than a portrait tablet.** At 768x1024 the echo, paper and close sheets overflow, so Next
  reads "More" and scrolls the sheet first. Acceptable; check it reads well. The shells were tested in Chromium only:
  iPad Safari, Firefox and printing are unverified.
