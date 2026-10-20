# Change and choice patterns

Family: comparison, before-after, cause-effect, choice-fork. Built from slice 3 (56 raw entries). 43 entries: 12 kept, 25 adapted, 6 new; 6 raw entries cut. Starred (★) entries are the best fifth.

## Family picker

Find your content shape, then the row with your item count and relation. Starred entries come first.

**Capability, then its impact on the reader**
- 1 problem per item, same four slots, 3-6 items · sequential → CHG-01★, CHG-06
- 3-6 capabilities acting on one place the reader knows · sequential → CHG-02★, CHG-27★
- raw input turned into structure using the same words, 3-6 phrases · linked → CHG-03★, CHG-04
- "you send X, you get Y back", 1 pair · opposed → CHG-04, CHG-06
- 1 capability whose value takes 2-4 steps of reasoning · linked → CHG-05, CHG-01★
- 1 problem, 3 impacts · grouped → CHG-07, CHG-01★
- a what-if on 1-2 numbers · linked → CHG-08, CHG-27★

**Before and after**
- 1 pair, same framing, the change is visual · opposed → CHG-10★, CHG-15
- a manual artefact going digital, 3-6 rows · opposed → CHG-09★, CHG-12
- 3-8 dimensions with worded states · opposed per row → CHG-11, CHG-13
- 3-8 measured values · opposed per row → CHG-13, CHG-11
- an existing process edited, 5-15 lines · sequential → CHG-12, CHG-14
- additions and removals that net out, 3-8 · sequential → CHG-14, CHG-12
- a plan opening into operation, 2-4 parts · grouped → CHG-16, CHG-02★
- a change of direction, 1 path · opposed → CHG-37★, CHG-17

**Comparison**
- 1 value against a benchmark or baseline · opposed → CHG-18, CHG-19
- the size of the change is the story, 2 series · opposed → CHG-19, CHG-18
- 2-4 approaches on the same task · opposed → CHG-20, CHG-26
- 2 parties sharing one system, 4-10 rows · grouped → CHG-21, CHG-11
- 4-16 units with one repeated structure · equal → CHG-22, CHG-23
- 3-8 look-alikes to tell apart · equal → CHG-23, CHG-22
- 1 set seen 2-4 ways · sequential → CHG-24, CHG-27★
- a wrong belief, 1 trend or number · opposed → CHG-25, CHG-18
- 2-6 mistakes and their fixes · opposed → CHG-26, CHG-12

**Cause and effect**
- 1 mechanism, one variable, 4-7 chapters · sequential → CHG-27★, CHG-05
- 3-8 hidden problems on a familiar surface · sequential → CHG-28★, CHG-31
- 3-6 cause families behind 1 problem · grouped → CHG-31, CHG-28★
- 3-5 causes meeting at 1 problem · linked → CHG-35, CHG-31
- 1 change, 3-6 knock-on effects · linked → CHG-34, CHG-05
- 6-15 ideas and how they connect · linked → CHG-29, CHG-34
- lost potential across 3-12 items · opposed → CHG-30, CHG-11
- what flows along 1 relationship · linked → CHG-32, CHG-29
- 1 reveal (price, result, reframe) · sequential → CHG-33, CHG-10★

**Choice and fork**
- the closing ask, 2-4 exclusive options · equal → CHG-36★, CHG-40
- act now or wait, 2 roads · opposed → CHG-37★, CHG-30
- 1 winner out of 3-6 by hard tests · ranked → CHG-38, CHG-40
- 2-4 options on 3-6 criteria · ranked → CHG-40, CHG-41
- options balancing 3 qualities · ranked → CHG-41, CHG-40
- 3-6 questions leading to a recommendation · sequential → CHG-39, CHG-38
- 4-12 items or 3-5 packages placed on two judgements · grouped → CHG-42, CHG-41
- 3-5 paths from one shared start · sequential → CHG-43, CHG-37★

## Shorthand used in the entries

- **pen draw**: `stroke-dashoffset` from the path length to 0; duration = length / 600 px/s, clamped to 0.6-2.2s; ease cubic-bezier(.45,.05,.35,1); the next stroke starts at 80-85% of the previous one.
- **arrive**: opacity 0 to 1 plus translateY of 16px or less, 0.6-1.0s, cubic-bezier(.22,1,.36,1); runs once and always finishes.
- **construction line**: `stroke-dasharray:3 5` at 25-30% ink; it inks solid with a pen draw when its caption explains it.
- **marker sweep**: the TVS `mark`; background-size 0% to 100% over .7s cubic-bezier(.19,1,.22,1) after .35s.
- **stage**: a sticky drawing inside a wrapper of 300vh or less; captions scroll past in normal flow; each step changes one thing; an n / N counter; below 768px a stacked static twin.
- **stagger**: 60-110ms per item, total capped at 450ms.
- Scroll-linked values are linear in scroll progress. No back, elastic or bounce curves anywhere.

---

## Capability, then impact

### CHG-01 ★ Problem stop card
- For: capability-impact, cause-effect, people-roles · 1 problem per card, 3-6 cards in a run
- Instead of: a list of services with a benefits paragraph under each
- Reader sees: A card that reads top to bottom: "THE PROBLEM" in small red caps, the problem as one serif sentence in the reader's words, the chip of the team that solves it, one muted line on what they do, then "WHAT YOU GET" with the outcome under a yellow marker.
- Moves: in-view - the card arrives (12px, .75s); the outcome gets a marker sweep once the card settles; in a run of cards, the TVS snake line reaches each card's knot by scroll.
- Build: `.prob-k` mono 11px .09em kumkum; `.prob` serif clamp(22px,2vw,27px)/1.22, `text-wrap:balance`, margin 6px 0 16px; `.solver` chips 14.5px, padding 7px 13px; `.does` 15px muted; `.gets` margin-top 16px, padding-top 14px, top hairline, mono 11px label, `mark` serif 19.5px/1.45.
  Card radius 18px, padding 26px 28px 24px, shadow `0 0 0 1px var(--line), 0 16px 30px -26px rgba(36,29,24,.55)`.
- Narrow: Below 820px: full width on a left rail · Reduced motion: card and marker shown complete.
- Use when: every item fills the same four slots and the payoff is where the eye should land · Avoid when: outcomes are vague (the marker then highlights filler).
- Effort: S · Needs lib: no · Code: TVS harvest · Sources: P014 (TVS site, page.html ~L294-307, L564-571) · Verdict: KEEP

### CHG-02 ★ Pinned scene, one capability per step (new)
- For: capability-impact, cause-effect · 3-6 capabilities acting on one place
- Instead of: a features grid of icon cards with a benefit line under each
- Reader sees: A line drawing of the reader's own world (their shop floor, their classroom, their inbox) stays pinned; each caption that scrolls past names one capability, a faint dashed leader runs from the caption to the exact spot it touches, the leader inks solid, and the impact lands as a short marked label on that spot.
- Moves: scroll-linked - the base drawing pen-draws once on entry; per step the leader appears as a construction line, then pen-draws solid (0.6-0.9s); the impact label arrives (8px, .6s) and gets a marker sweep; earlier labels dim to 45% and stay; n / N counter.
- Build: stage wrapper = steps x 50vh, capped at 300vh; inner `position:sticky; top:0; height:100vh` holds one SVG plus HTML labels placed from SVG coordinates (`getScreenCTM()`); captions are `<section data-step>` watched by one IntersectionObserver (`rootMargin:"-45% 0px -45% 0px"`).
  The active step sets `data-step` on the stage and CSS does the rest; leaders are `<path pathLength="1">`, `stroke-dasharray:.02 .02` before, `1 1` with dashoffset 1 to 0 when drawn.
- Narrow: Below 768px: static twin, one small copy of the drawing per step showing only that step's leader and label · Reduced motion: final scene, every leader solid, every label placed.
- Use when: all the capabilities act on one place or object the reader recognises and the message is "here is what changes, and where" · Avoid when: capabilities touch different worlds (use CHG-01 in a run), or more than 6 steps.
- Effort: L · Needs lib: no · Sources: new; built from the Washington Post pinned-subject reference, P433 and P191 · Verdict: NEW

### CHG-03 ★ Phrase-to-field threads
- For: capability-impact, before-after · 3-6 phrases
- Instead of: a screenshot of the output captioned "we turn chaos into order"
- Reader sees: A messy message thread on the left and a tidy card on the right (owner, due date, amount); one at a time, a phrase in the mess gets a marker, a thin line draws from it to its labelled field, and the same words appear in that field.
- Moves: in-view - per phrase: marker sweep on the source; a construction line appears, then pen-draws solid from source to field (0.6-1.0s); the field text arrives (8px, .6s) as the line lands; the next phrase starts at 85% of the previous line; delivered source phrases dim to 50%.
- Build: phrases as `<mark data-to="owner">`; one absolute SVG overlay spans both panes; on trigger and on resize, measure source and target rects relative to the overlay and write `M sx sy C sx+dx*.5 sy, tx-dx*.5 ty, tx ty`; draw with `getTotalLength()` and dashoffset.
  Lines stay after drawing so the whole mapping reads at the end.
- Narrow: Below 820px: source above target, threads run downward with the same curve rule · Reduced motion: all threads drawn, fields filled, sources and fields share the marker.
- Use when: the service turns raw input (calls, chat notes, receipts) into structure using the same words · Avoid when: the words change in the transformation, or more than 6 phrases (threads cross).
- Effort: M · Needs lib: no · Sources: P173 (https://linear.app) · Verdict: ADAPT (the phrase flight across the screen became a drawn thread; nothing flies in from the side)

### CHG-04 Ask and result flip
- For: capability-impact, before-after · 1 pair
- Instead of: "You send us X, we send you Y" written as two sentences
- Reader sees: A switch labelled "1. What you send" and "2. What you get back" above one card that first shows the raw request, then flips to the finished output.
- Moves: in-view + tap - when the card crosses 60% of the viewport it flips once to the result; tapping either label flips back and forth; the thumb slides .3s cubic-bezier(.22,1,.36,1); panels crossfade .4s in one grid cell with no travel.
- Build: two radio inputs styled as a segmented control with a sliding `::before` thumb (`translateX`); panels share `grid-area:1/1`; `:checked ~ .panels .result{opacity:1}`; one IntersectionObserver checks the result radio once and disconnects.
- Narrow: Below 820px: same · Reduced motion: both panels stacked, request above result, a short drawn arrow between.
- Use when: the promise is "you tell us X, we hand back Y" and Y is concrete · Avoid when: the result needs a long explanation.
- Effort: S · Needs lib: no · Sources: P172 (https://claude.com/product/overview) · Verdict: ADAPT (the 1.5s timer flip became a one-time scroll flip; curve set to the house ease-out)

### CHG-05 So-that chain (new)
- For: capability-impact, cause-effect · 1 capability, 2-4 links
- Instead of: a benefits paragraph that says "which leads to" three times
- Reader sees: A capability in a small ink-ringed box; below it a short line drops through two to four rungs, each joined by the words "so that", ending on the reader's outcome in a dark payoff card with a marker.
- Moves: in-view - each connector pen-draws downward (0.6s); the next rung arrives (8px, .6s) as the line lands; the next connector starts at 80% of the previous; the last rung's key phrase gets the marker sweep.
- Build: `<ol class="sothat">` with `li` rungs; connectors are 2px SVG lines, 48px tall, with "so that" in mono 11px beside each; the end rung is the TVS dark payoff card (ink bg, serif 23px/1.3, marker pill on dark). Four rungs at most; this is a contained diagram, never a line running down the page.
- Narrow: Below 820px: same (it is already a column) · Reduced motion: all rungs and lines shown, marker set.
- Use when: one capability's value needs two or three steps of reasoning before it reaches the reader · Avoid when: the link is obvious in one step (one sentence with a marker is enough).
- Effort: S · Needs lib: no · Sources: new; built from the TVS dark payoff card and P140 verbs on lines · Verdict: NEW

### CHG-06 Gutter closure
- For: capability-impact, before-after, cause-effect · 2 panels
- Instead of: a process explainer of steps the reader does not care about
- Reader sees: Two line-drawn panels side by side, the mess and then the result, with a narrow gap between them captioned "this is where we work"; the mind fills in the action.
- Moves: in-view - panel 1 pen-draws (1.2-1.6s); a held beat of 600ms; panel 2 pen-draws; the gutter caption arrives last (8px, .6s).
- Build: flex row, `gap:28px`; both panels the same frame size, 1.5px ink outline, radius 6px, tilt no more than .4deg; drawings are SVG paths drawn in order; the gutter caption is mono 11px on a marker tab set across the gap.
- Narrow: Below 820px: panels stack; the gutter becomes a horizontal band holding the caption · Reduced motion: both panels drawn, caption shown.
- Use when: the process is dull to watch and the outcome is what matters · Avoid when: the reader must understand the process (use CHG-02 or CHG-05).
- Effort: S · Needs lib: no · Sources: P262 (https://en.wikipedia.org/wiki/Understanding_Comics) · Verdict: ADAPT (comic panels with yellow caption boxes became self-drawing line panels with one marker caption)

### CHG-07 Brief and impact pair
- For: capability-impact, cause-effect · 1 problem + 3 impacts
- Instead of: a "Problem" heading followed by a "Solution" heading
- Reader sees: Two cards side by side: a light one stating the problem, and a dark one listing three impacts, each on a solid yellow marker pill.
- Moves: in-view - the light card arrives, the dark card follows 100ms later.
- Build: `.brief` grid 1.1fr .9fr, gap 16px; cards radius 18px, padding 28px 30px; h3 clamp(26px,2.4vw,32px); `.impact` ink bg, list serif 21px/1.3, gap 12px; on dark, `mark{color:var(--ink);background:var(--marker);padding:1px 6px;border-radius:4px}`.
- Narrow: Below 820px: stacked · Reduced motion: static.
- Use when: framing a worked example before walking through it · Avoid when: more than 3-4 impacts.
- Effort: S · Needs lib: no · Sources: P024 (TVS site, page.html ~L313-322, L816-830) · Verdict: KEEP

### CHG-08 Reactive sentence
- For: capability-impact, cause-effect, quantity-scale · 1-2 variables
- Instead of: a pricing tier table full of "up to" numbers
- Reader sees: "If you publish **3** posts a week, about **1,200** people see you each month." The first number has a dotted underline; tapping it steps through three preset values and the rest of the sentence rewrites itself.
- Moves: tap - the number swaps; dependent numbers count to their new value over .6s cubic-bezier(.22,1,.36,1); changed words get a short marker sweep.
- Build: `<button class="knob" data-values="1,3,5" aria-live="polite">`; tap, Enter or Space cycles presets; a small model function recomputes dependent spans, and wording can switch ("a trickle", "a steady stream"). The default is the recommended plan so readers who never tap read the right story.
  Optional on fine pointers: horizontal drag with pointer capture, one unit per 8px, `cursor:ew-resize`.
- Narrow: Below 820px: same (tap) · Reduced motion: values swap instantly.
- Use when: the reader will ask "what if we did less?" and the model is honest · Avoid when: the model would be guesswork.
- Effort: M · Needs lib: no · Sources: P068 (https://worrydream.com/ExplorableExplanations/) · Verdict: ADAPT (drag-to-scrub became tap through three presets; drag kept only for mouse users)

---

## Before and after

### CHG-09 ★ Paper vs screen
- For: before-after, comparison · 3-6 rows
- Instead of: two columns headed "Today" and "With us"
- Reader sees: Left, a slightly tilted paper check sheet where blue handwritten ticks appear one by one and a scrawled note lands; a thin arrow captioned with the change; right, a dark tablet where the same rows fill as bars and one row reads a yellow "Stopped".
- Moves: in-view (threshold .45) - ticks pen-write in reading order, each .25s (opacity plus scale .6 to 1), the next at 80% (every 200ms); the note fades .4s after the last tick; the screen arrives 700ms later; bars scaleX 0 to 1 over .9s cubic-bezier(.22,1,.36,1), staggered 80ms; the halt dot blinks three times (1.2s each) and then holds.
- Build: `.p2s` grid 1fr 120px 1fr, gap 20px, max 980px. `.sheet` #FFFDF6, radius 6px, rotate(-1.2deg), shadow `0 1px 0 var(--line), 0 12px 28px -18px rgba(36,29,24,.4)`; rows grid 1fr 54px 54px with #D8D0C2 rules; ticks Caveat 24px #2B4A8B.
  `.screen` ink, radius 22px; `.srow` grid 76px 1fr 70px; `.bar` 8px track with `<i style="--w:92%">` scaleX fill; the running state dot is a 2px powder ring (was green #8DB38B); `.halt` dot filled marker.
- Narrow: Below 820px: stacks, the sheet untilts, the arrow rotates 90° · Reduced motion: every tick, note, bar and state shown complete, no blink.
- Use when: the change is from a manual artefact to a digital one and the same rows can be shown both ways · Avoid when: the "after" has no concrete rows to repeat.
- Effort: M · Needs lib: no · Code: TVS harvest · Sources: P017 (TVS site, page.html ~L120-140, L670-689, L978-986) · Verdict: ADAPT (green running dot became a powder ring; endless blink cut to three; tick rhythm set to the pen rule)

### CHG-10 ★ Same frame, scroll wipe
- For: before-after · 1 pair, up to 4 states at one framing
- Instead of: two photos side by side captioned Before and After
- Reader sees: One line drawing (their shelf, their site, their screen) pinned at an identical crop; as captions scroll past, an inky edge travels down it and, behind the edge, the same scene appears in its new state; a small date or state stamp in the corner flips at the halfway point.
- Moves: scroll-linked - the edge position equals step progress; the stamp swaps at 50%; tap route: a "Hold to see before" pill swaps instantly on pointerdown and restores on pointerup (Space when focused), and a range handle lets anyone scrub.
- Build: two stacked SVGs or images in a stage, `position:absolute; inset:0`; the after layer gets `clip-path: inset(0 0 calc((1 - var(--p)) * 100%) 0)` with `--p` from section progress; wrapper 200-250vh.
  Ink edge variant: mask the after layer with a path whose top edge sits at y = p x 1000, run through a static `feTurbulence` (fractalNoise, baseFrequency .045 .055, 4 octaves) plus `feDisplacementMap` (scale 100) filter; only the path `d` changes, the filter never animates. Keep crop, scale and line weight identical so the only visible change is the change.
- Narrow: Below 768px: static twin, before and after stacked with captions and a still drawn line between · Reduced motion: after shown in full with a small before thumbnail and a labelled divider.
- Use when: the change is spatial or visual and both states can be drawn at the same framing · Avoid when: the states cannot share a frame, or the change needs explaining (use CHG-02).
- Effort: M · Needs lib: no · Sources: P045 (https://www.reuters.com/graphics/MYANMAR-ROHINGYA/010051VB46G/), P407 (https://heronaiapp.com), P447 (https://www.concretemanagement.fr), P100 (https://bost.ocks.org/mike/algorithms/) · Verdict: ADAPT (four swap devices merged; scroll drives the wipe; drag and hold kept as the tap route)

### CHG-11 Gap dumbbells on a worded scale
- For: before-after, comparison · 3-8 rows
- Instead of: a before and after table of adjectives
- Reader sees: Rows of tracks marked with words (by hand, on phone, automatic); on each, a hollow "today" dot is joined by an inked bar to a solid "with us" dot further along.
- Moves: in-view - row by row, the bar pen-draws from the hollow dot to the solid one (0.6-0.9s); the solid dot fills as the line arrives; the next row starts at 80% of the previous.
- Build: each track is a 1px line with 3-5 word stops at even x; dots are SVG circles (hollow: 2px ink ring on paper; solid: ink, or marker on the one row that matters most); the bar is a `<line>` drawn by dashoffset. Dots sit on stops, never between them; no numbers.
- Narrow: Below 820px: stop labels sit above the track in mono 10.5px caps · Reduced motion: final state.
- Use when: several dimensions each move from one state to a better one · Avoid when: only one dimension moves (one sentence with a marker is enough).
- Effort: S · Needs lib: no · Sources: P120 (https://datavizproject.com/data-type/dumbbell-plot/) · Verdict: KEEP

### CHG-12 Track-changes rewrite
- For: before-after, sequence · 3-7 pains (paired rows) or 5-15 process lines (edited in place)
- Instead of: two columns headed Before and After
- Reader sees: The client's current process, or their pains, as plain lines; a pen line strikes through what goes, and the new wording appears beside or below each in ink, with a one-line margin note on why.
- Moves: in-view per line - the strike pen-draws left to right (0.45-0.6s); the replacement arrives (8px, .6s) starting at 80% of the strike; lines change in reading order, one at a time.
- Build: `<ol>` of steps; struck text in `<del>` with an absolute SVG stroke over it (a slightly wobbly path, 2px, `vector-effect:non-scaling-stroke`) instead of CSS line-through; `<ins>` without underline, the key phrase in a `mark`; margin notes in a right column (mono 11px label plus a 15px muted line).
  Pain and fix layout: grid 1fr 1fr, gap 32px.
- Narrow: Below 820px: margin notes become inline italic lines; pain stacks over fix · Reduced motion: final marked-up state with strikes drawn.
- Use when: the offer improves an existing workflow and the reader recognises the old lines as theirs · Avoid when: the change is a total replacement, or the pains are guesses.
- Effort: S · Needs lib: no · Sources: P067 (https://www.redblobgames.com/pathfinding/a-star/introduction.html), P343 (https://roughnotation.com/) · Verdict: ADAPT (two near-identical entries merged; the library strike became one vanilla SVG stroke; insertions rise 8px instead of sliding in)

### CHG-13 Slope pairs
- For: before-after, comparison, quantity-scale · 3-8 items
- Instead of: a "then and now" table of figures
- Reader sees: A "Today" column and a "With us" column of values; each item is a line climbing or falling from its today value to its new value, labelled at both ends.
- Moves: in-view - left dots arrive together; lines pen-draw left to right one at a time (0.6-0.8s), the next at 80%; improving lines in the accent, flat ones in muted ink.
- Build: SVG with two x positions and y from real values on one shared scale; left labels carry the name and old value, right labels the new value; nudge colliding labels in 14px steps.
- Narrow: Below 820px: two columns still fit with short labels, otherwise stacked "from, to" rows · Reduced motion: static.
- Use when: every item has a measured before and after · Avoid when: you only have after-numbers, or values would be invented.
- Effort: M · Needs lib: no · Sources: P320 (https://github.com/Financial-Times/chart-doctor/tree/main/visual-vocabulary) · Verdict: KEEP

### CHG-14 Plus-minus staircase
- For: before-after, cause-effect · 3-8 changes
- Instead of: two lists headed "What we add" and "What we remove"
- Reader sees: One stepped pen line that starts at "today", steps up for each thing added (training, a tool) and steps down for each burden removed (double entry), ending at "after", with a short label on every riser.
- Moves: scroll-linked - one riser per caption: the line pen-draws to the next step (0.6s) and that riser's label arrives (8px, .6s); removals get a pen strike on their label.
- Build: one SVG polyline built from a running level (`y -= stepH` for an addition, `y += stepH` for a removal) at equal x spacing; draw by dashoffset to the length at each step (`getTotalLength` per vertex, stored once); additions labelled in ink, removals muted; caption "each step is one change, not a measured amount".
- Narrow: Below 820px: a vertical list where the running level becomes indentation · Reduced motion: the whole staircase drawn.
- Use when: the offer is additions and removals that net out to a better state · Avoid when: size should matter but you have no data.
- Effort: S · Needs lib: no · Sources: P123 (https://github.com/Financial-Times/chart-doctor/tree/main/visual-vocabulary) · Verdict: ADAPT (a row of offset blocks became one self-drawing stepped line, so it never reads as a step strip)

### CHG-15 Shared-frame split
- For: before-after, comparison · 2 states
- Instead of: two columns headed Without and With
- Reader sees: One drawing split by a horizon line: above it, today's way; below it, the new way; the line between them is the point.
- Moves: in-view - the horizon pen-draws across (1.0-1.2s); then each half's caption arrives (8px, .6s), top first, 100ms apart.
- Build: one SVG with two `clipPath` groups sharing the horizon y; a single `<line>` drawn by dashoffset; captions placed inside each half.
- Narrow: Below 820px: halves stack with the horizon between · Reduced motion: shown finished.
- Use when: a stark contrast fits in one image (old process and new, without and with) · Avoid when: each side needs many details (use CHG-09 or CHG-12).
- Effort: S · Needs lib: no · Sources: P420 (http://plastic-ocean.com) · Verdict: KEEP (ease set to the house draw curve)

### CHG-16 Unfold into working shape
- For: before-after, part-whole · 2-4 parts
- Instead of: a "Phase 2: full rollout" box
- Reader sees: A packed-up object (a folded plan, a closed kit) opens its parts outward and becomes ready to work, each part labelled as it opens.
- Moves: in-view - parts scale out from their attachment points together, .8s cubic-bezier(.22,1,.36,1); detail lines then pen-draw with a 60ms stagger; the body rotates 10° at most.
- Build: each part in its own `<g>` with `transform-box:fill-box; transform-origin:left center` (mirrored on the other side), `scaleX(0)` to 1; detail strokes use `pathLength="1"` and dashoffset 1 to 0; labels arrive after their part.
- Narrow: Below 820px: same · Reduced motion: the unfolded state with a dotted outline of the packed shape.
- Use when: a plan goes from proposal to operating, or a feature set opens up · Avoid when: the parts are not attached to one body.
- Effort: M · Needs lib: no · Sources: P462 (video study, key_08_satellite-panels-unfolding.png, burst_08_panels-unfold.png) · Verdict: KEEP (detail stagger raised from 40ms to the house 60ms)

### CHG-17 Pivot to a new heading
- For: before-after, choice-fork · 1 path, 2 directions
- Instead of: an "Our new direction" heading over a paragraph
- Reader sees: An arrow drawn as a line slowly turns from the old direction to the new one as you read why, the old heading left behind as a faint ghost.
- Moves: scroll-linked - rotation goes from 0 to at most 30° across about 35vh, linear with scroll; the ghost stays at 25%.
- Build: `transform:rotate(calc(var(--p) * 22deg))` with `transform-box:fill-box; transform-origin:50% 55%`; `--p` from section progress; the ghost is a copy of the arrow at opacity .25 drawn as a construction line.
- Narrow: Below 820px: same · Reduced motion: two arrows, the old one ghosted at 25%.
- Use when: a strategy, route or plan changes direction for a stated reason · Avoid when: nothing actually changed course.
- Effort: S · Needs lib: no · Sources: P469 (video study, key_06_rocket-pivot-gravity-turn.png, burst_06_gravity-turn.png) · Verdict: KEEP

---

## Comparison

### CHG-18 Benchmark outline, then the real bar
- For: comparison, proof-trust, quantity-scale · 2-3 values, one of them a benchmark
- Instead of: two bold numbers side by side
- Reader sees: "Industry reply time: 4 hours" as a dashed outline bar; then "Yours today: 19 hours" as a solid ink bar that grows far past it, the overshoot hatched. Or an outlined "today, 1x" against a solid "with us, 6.4x".
- Moves: in-view - the dashed outline appears first; 300ms later the real bar grows from scaleX(0) over .9s cubic-bezier(.22,1,.36,1); the number counts up on the same curve and duration.
- Build: SVG rects; the benchmark is `fill:none; stroke-dasharray:4 4`; the real bar is ink with `transform-origin:left`; the overshoot is a static `<pattern>` hatch clipped to the area past the benchmark; numbers in serif 48px; every bar carries a source footnote.
  Optional tabs for 2-6 tasks replay the grow when tapped.
- Narrow: Below 820px: bars stay horizontal and fluid · Reduced motion: final bars and numbers.
- Use when: a credible outside benchmark or an honest current baseline exists · Avoid when: the benchmark would be invented.
- Effort: S · Needs lib: no · Sources: P047 (https://www.reuters.com/graphics/MYANMAR-ROHINGYA/010051VB46G/), P194 (https://www.apple.com/macbook-pro/) · Verdict: ADAPT (two bar devices merged; the grey baseline bar became the dashed construction outline)

### CHG-19 Baseline, then the shock
- For: comparison, emphasis, time · 2 series
- Instead of: a line chart with two series and a legend
- Reader sees: First a "normal good month" line drawn as the reference; then the new line draws on the same chart and the axis rescales, so the old peak shrinks to a ripple near the floor, still labelled.
- Moves: scroll-linked - step 1 pen-draws the baseline; in step 2 the y-axis maximum follows scroll progress while the new line draws; the annotation keeps pointing at the shrinking baseline.
- Build: stage of 2 steps, 200vh or less, counter 1 / 2; one SVG chart keeps the baseline's scale in step 1; in step 2 the domain max interpolates by `--p` and a rAF loop rewrites path `d` only when `--p` changes; the annotation is anchored to a data point and recomputed per frame.
- Narrow: Below 768px: static twin, two small charts at the final scale, the first boxed "before" · Reduced motion: the same two charts.
- Use when: the size of the change is the story · Avoid when: the baseline is cherry-picked.
- Effort: M · Needs lib: no · Sources: P096 (https://pudding.cool/2018/08/wiki-death/) · Verdict: ADAPT (the timed 800ms rescale became scroll-tied inside a two-step stage)

### CHG-20 Same job, two ways, one clock
- For: comparison, before-after, choice-fork · 2-4 approaches
- Instead of: a pros and cons list of "do it yourself" against "us"
- Reader sees: Identical small line drawings side by side, each running a different approach on the same task; scrolling moves one shared clock, a counter under each shows wasted effort, and the naive way visibly jams where the real design flows.
- Moves: scroll-linked - section progress drives one shared time value for every pane (the clock is the one moving thing); the failure moment is marked with a shape and a word, never colour alone; the recommended pane gets the accent outline at the end.
- Build: one small model per approach, all stepped from one `t` taken from scroll progress; render by changing SVG attributes only; counters ("cells checked", "hours spent") under each pane; stage 250vh or less.
- Narrow: Below 768px: static twin, panes stacked with the naive one on top, each frozen at its failure or finish with its counter · Reduced motion: final frames with counters.
- Use when: the client's instinct is the naive version and the comparison is fair · Avoid when: the naive side is a straw man or the race is rigged.
- Effort: L · Needs lib: no · Sources: P054 (https://ciechanow.ski/mechanical-watch/), P064 (https://www.redblobgames.com/pathfinding/a-star/introduction.html) · Verdict: ADAPT (two entries merged; the ambient loop became scroll-driven so the motion explains and stops)

### CHG-21 Mirror rows
- For: comparison, people-roles · 2 parties, 4-10 shared rows
- Instead of: two lists headed "For you" and "For them"
- Reader sees: A centre column of labels, with chips growing left for one party (the client's team) and right for the other (their customers), so each finds their half of the same system.
- Moves: in-view - the centre spine pen-draws top to bottom (1.0-1.4s); then each row's chips grow outward from it together, rows staggered 80ms, .6s cubic-bezier(.22,1,.36,1).
- Build: CSS grid `1fr auto 1fr`; left cells `justify-self:end; transform-origin:right`, scaleX 0 to 1; no numbers: chips name what each side gets, or a three-step length (none, some, main) only when stated.
- Narrow: Below 820px: label, left chip, right chip stacked, each chip with a side tag · Reduced motion: static.
- Use when: two parties share one thing and each needs to find their side · Avoid when: three or more parties.
- Effort: S · Needs lib: no · Sources: P121 (https://datavizproject.com/data-type/butterfly-chart/) · Verdict: KEEP (a pen-drawn spine added before the chips grow)

### CHG-22 Small multiples
- For: comparison, list-of-equals, place-network · 4-16 equal units
- Instead of: one crowded chart with a line per unit and a legend
- Reader sees: A grid of identical tiny drawings or charts, one per site, team or month, all on the same scale, so the one that behaves differently jumps out.
- Moves: in-view - panels pen-draw in reading order, 80ms stagger capped at 450ms; tapping a panel drops the others to 25% and outlines the same element in every panel.
- Build: one SVG `<symbol>` or a JS `panel(data)` template; grid `repeat(auto-fill, minmax(150px, 1fr))`; every cell uses the same `viewBox="0 0 100 40"` and one shared y-scale computed once, never per panel; a tap toggles `.focus` on the grid.
- Narrow: Below 820px: 2 columns, same scale · Reduced motion: all panels drawn at once.
- Use when: one structure repeats across places or groups and the differences are the message · Avoid when: fewer than 3 units, or panels would need different templates or scales.
- Effort: M · Needs lib: no · Sources: P124 (https://en.wikipedia.org/wiki/Small_multiple), P228 (https://en.wikipedia.org/wiki/Small_multiple), P334 (https://github.com/Financial-Times/chart-doctor/tree/main/visual-vocabulary) · Verdict: KEEP (three duplicates merged)

### CHG-23 Field-guide plate
- For: comparison, definitions-jargon · 3-8 look-alikes
- Instead of: a glossary of types with a definition each
- Reader sees: A plate of similar line drawings (customer types, risks, competing offers) in the same pose and scale, each with a short arrow pointing at the one mark that tells it apart, captioned "look for: ...".
- Moves: in-view - the drawings arrive together; arrows pen-draw to their marks one by one (0.6s each, the next at 80%); tapping a plate enlarges it 1.15x and dims the rest to 40%.
- Build: grid of SVG illustrations at identical scale; arrows are short paths drawn by dashoffset, with the head fading in as the shaft lands; captions are a mono 11px label plus serif 18px; a tap toggles `.focus`.
- Narrow: Below 820px: plates stack in one column with arrows kept · Reduced motion: arrows drawn.
- Use when: readers confuse similar things and must tell them apart fast · Avoid when: the items differ obviously.
- Effort: M · Needs lib: no · Sources: P277 (https://en.wikipedia.org/wiki/Peterson_Field_Guides) · Verdict: ADAPT (the narrow carousel became a stacked column; arrows that "shoot in" became pen draws)

### CHG-24 Same pieces, regrouped
- For: comparison, part-whole · 2-4 views of one set
- Instead of: tabs that show the same plan by cost, by team and by time
- Reader sees: One pinned diagram of the same pieces; each caption that scrolls past regroups them to answer a different question (by cost, by team, by time), with a "2 / 3" counter.
- Moves: scroll-linked - when a caption becomes active, pieces glide to their new spots over .8s cubic-bezier(.22,1,.36,1) and labels crossfade .3s; tapping the counter steps to the next view.
- Build: pieces as absolutely placed elements or SVG groups with per-view coordinates in `data-v0` to `data-v3`; FLIP transforms; stage of 70vh per view, 300vh at most; the step observer sets `data-view` on the stage; a button cycles views for tap.
- Narrow: Below 768px: static twin, one small diagram per view, stacked · Reduced motion: instant switch per step.
- Use when: the same parts answer different questions · Avoid when: the views do not share pieces, or one view is enough.
- Effort: M · Needs lib: no · Sources: P445 (https://www.fps.hu), P242 (https://en.wikipedia.org/wiki/Architectural_drawing) · Verdict: ADAPT (tap-only cycling became stage steps; the 3D axonometric tilt cut)

### CHG-25 The usual guess, then the truth
- For: comparison, cause-effect, proof-trust · 1 trend or 1 number
- Instead of: "Most people think X, but actually Y" in a paragraph
- Reader sees: A chart where the line most teams assume is drawn dashed and labelled "what most teams expect"; then the real line draws solid beside it, the gap between them shades in, and one sentence names the gap.
- Moves: scroll-linked - step 1 shows the dashed assumption; step 2 pen-draws the real line (1.0-1.6s by length) and the gap fill fades in over .6s once it lands.
- Build: SVG; the assumption path is a construction line at 40% ink; the real path is 2px ink drawn by dashoffset; the gap is a path between the two lines filled with a static hatch; one serif sentence below with the gap phrase marked.
- Narrow: Below 820px: same (the chart is fluid) · Reduced motion: both lines and the shaded gap shown.
- Use when: the reader holds a wrong belief worth surfacing and the usual guess is documented · Avoid when: the guess would be invented or would embarrass a senior reader.
- Effort: S · Needs lib: no · Sources: P049 (https://mucollective.northwestern.edu/theydrawit) · Verdict: ADAPT (the reader no longer draws; we draw the common guess as a construction line)

### CHG-26 Do and don't pairs
- For: comparison, before-after, emphasis · 2-6 pairs
- Instead of: a "Common mistakes" bullet list
- Reader sees: Pairs of small line drawings in identical frames, made for their situation: the wrong way gets crossed out in two pen strokes, the right way gets a check.
- Moves: in-view per pair - the X draws in two strokes over the wrong panel (0.35s each, the second at 80%); the check pen-draws on the right panel at 80% of the X.
- Build: drawings of their actual artefacts and moments in identical frames, never generic figures; X and check are short paths drawn by dashoffset; the meaning lives in a one-line caption under each pair and in `aria-label`; card radius 14px, flat, no sheen.
- Narrow: Below 820px: pairs stack vertically · Reduced motion: marks shown.
- Use when: the reader is making common mistakes now, or readers face language barriers · Avoid when: the tone must stay gentle; crossed-out panels can scold.
- Effort: S · Needs lib: no · Sources: P246 (https://en.wikipedia.org/wiki/Aircraft_safety_card) · Verdict: ADAPT (wordless pictograms became drawings of their own artefacts; laminated sheen dropped)

---

## Cause and effect

### CHG-27 ★ Fixed stage, one knob per chapter
- For: cause-effect, sequence · 4-7 chapters, one variable
- Instead of: a paragraph per step, each with its own unrelated picture
- Reader sees: One line drawing stays pinned; each chapter of text that scrolls past changes just one thing in it (more water, a later date, a bigger team), so cause and effect are obvious, with "03 / 06" in the corner.
- Moves: scroll-linked - within each chapter, progress maps to one parameter; the drawing follows the target with a 0.3s exponential follow so it never jumps; each chapter title arrives once (16px, .7s).
- Build: chapters as `<section data-param="rain" data-from="0" data-to="1">`; one scroll handler finds the active chapter and sets `target`; a rAF loop runs `value += (target - value) * (1 - Math.exp(-dt / 0.3))` and writes SVG attributes only when the value changes.
  Counter `01 / 07`; the stage stays at 300vh or less (about 45-75vh per chapter).
- Narrow: Below 768px: static twin, each chapter shows two small frames (from, to) · Reduced motion: the value jumps per chapter; the drawing is static between.
- Use when: explaining a mechanism (how spend drives reach, how practice drives skill) · Avoid when: several things change together.
- Effort: L · Needs lib: no · Sources: P433 (http://chladni-plate-experiment.vercel.app) · Verdict: ADAPT (title travel cut from 24px to 16px; pinned height capped at 3 viewports; static twin added)

### CHG-28 ★ X-ray of hidden problems
- For: cause-effect, before-after, definitions-jargon · 1 drawing, 3-8 hidden marks
- Instead of: a bulleted list of pain points
- Reader sees: A plain line drawing of something the reader knows (their floor plan, a ledger page, their workflow); as captions scroll past, an x-ray circle sweeps over it and one hidden problem at a time shows in the accent with a short label; found problems stay marked.
- Moves: scroll-linked - per step the x-ray circle grows over one problem area with scroll; the mark pen-draws and its label arrives (8px, .6s); tap route: "Show all" reveals every mark; on fine pointers a lens may also follow the pointer (lerp .2).
- Build: two stacked SVG layers in a stage; the annotated layer gets `clip-path: circle(var(--r) at var(--x) var(--y))`, with x, y and r set per step from a list of problem coordinates; found marks copy into an always-visible layer; one accent colour for every mark; n / N counter.
  Tap-only variant: small hinged windows over each spot that open to the "inside" drawing.
- Narrow: Below 768px: static twin, the drawing once with all marks numbered, then a numbered list · Reduced motion: annotated layer shown in full.
- Use when: showing losses or risks the reader cannot see on their own · Avoid when: the problems are already obvious.
- Effort: M · Needs lib: no · Sources: P191 (https://heronaiapp.com/), P283 (https://en.wikipedia.org/wiki/Pattachitra) · Verdict: ADAPT (the drag lens became scroll steps like the Washington Post x-ray; hinged windows folded in as a variant)

### CHG-29 Concept map with verbs on the lines
- For: cause-effect, many-to-many, definitions-jargon · 6-15 concepts
- Instead of: a paragraph of "this leads to that"
- Reader sees: Idea boxes joined by lines with short verbs written along them ("weekly review" catches "late orders"), so every pair reads as a sentence; cross-links stay dashed.
- Moves: scroll-linked - the top idea first; each box, verb and box appears as its sentence passes: the edge starts as a construction line and pen-draws solid as the verb is explained; dashed cross-links come last and stay dashed.
- Build: SVG boxes and path edges; verbs on `<textPath startOffset="50%" text-anchor="middle">`; broadest idea at the top; a focus question as the section heading; edges have two states, `.construct` and `.drawn`.
- Narrow: Below 820px: a chain of sentences with the two concepts as chips and the verb as plain text · Reduced motion: the whole map visible.
- Use when: explaining how ideas connect (why one habit leads to income) · Avoid when: every link is "and then" (use a sequence form).
- Effort: M · Needs lib: no · Sources: P140 (https://cmap.ihmc.us/docs/theory-of-concept-maps) · Verdict: KEEP

### CHG-30 Ghost remainder lines
- For: cause-effect, emphasis, before-after · 3-12 lines
- Instead of: "you are leaving money on the table" in bold
- Reader sees: Lines that run solid for what happens today and continue as faint dotted ghosts for what is still possible, so the gap reads as something lost.
- Moves: in-view - each solid part pen-draws, then its ghost fades in over .6s at 80% of the draw; lines start 90ms apart, capped at 450ms.
- Build: two paths per item: the solid one drawn by dashoffset; the ghost `stroke-dasharray:2 6; opacity:.4`; the axis is a stated span (a season, a programme); lengths only for stated spans, otherwise stage stops.
- Narrow: Below 820px: lines run vertical · Reduced motion: static.
- Use when: the cost of doing nothing should feel real · Avoid when: the tone must stay purely upbeat.
- Effort: S · Needs lib: no · Sources: P164 (https://guns.periscopic.com/) · Verdict: KEEP

### CHG-31 Fishbone of causes
- For: cause-effect · 1 problem, 3-6 cause families, 2-4 causes each
- Instead of: a list of reasons the problem exists
- Reader sees: A fish-skeleton line pointing at the problem; each bone is a family of causes (people, tools, timing, market) with small causes along it, and each bone ends in a chip naming the part of the offer that fixes it.
- Moves: scroll-linked - the spine pen-draws on entry; one bone per caption: the bone draws, its causes arrive (8px, .6s, 80ms stagger), and the fix chip lands last with a marker sweep.
- Build: horizontal spine; bones at ±60°, alternating above and below; causes as short horizontal ticks with HTML labels placed from computed coordinates; every stroke drawn by dashoffset; fix chips use the team chip colours.
- Narrow: Below 768px: a vertical spine with each bone as a stacked card (family, causes, fix) · Reduced motion: fully drawn with chips.
- Use when: the reader blames one cause and you need to show several · Avoid when: one cause clearly dominates.
- Effort: M · Needs lib: no · Sources: P143 (https://datavizproject.com/data-type/fishbone-diagram/) · Verdict: ADAPT (tap-to-see-the-fix became a fix chip per bone shown in sequence; narrow expanders became cards)

### CHG-32 Live line
- For: cause-effect, place-network · 1 active line at a time
- Instead of: a static arrow labelled "data flows"
- Reader sees: On the one connection being discussed, small dashes walk slowly from giver to receiver; every other line is still.
- Moves: ambient, only while its step is active and in view - `stroke-dashoffset` 0 to -18px per cycle, 2.4-3.2s linear, `stroke-dasharray:5 6`; stops when the step ends.
- Build: `@keyframes flow{to{stroke-dashoffset:-18px}}` on `.edge.is-live`; the step observer sets `.is-live`; `animation-play-state:paused` off-screen; draw the path from source to target so a negative offset reads as forward. TVS alternative: one marker dot moving along `getPointAtLength()`.
- Narrow: Below 820px: same · Reduced motion: the live line drawn solid with an arrowhead.
- Use when: showing what flows (money, data, produce) along one relationship · Avoid when: more than one flow matters at once.
- Effort: S · Needs lib: no · Sources: P412 (https://townhouse.dev, static/index.BN4-bxXu.css) · Verdict: KEEP

### CHG-33 Setup, then the turn
- For: cause-effect, emphasis · 1 reveal, 3 per page at most
- Instead of: the price or the result buried mid-paragraph
- Reader sees: A screen ends on a question or an "until..." at the bottom; the answer sits alone on the next screen, its drawing completing as it arrives.
- Moves: in-view - nothing moves on the setup; on the next screen the answer arrives (16px, .8s) and its key phrase gets the marker sweep.
- Build: the setup section is `min-height:100svh` with the question at the bottom (`display:flex; justify-content:flex-end`); the answer section starts on the next screen; no `scroll-snap`, no clip wipe; the payoff never shares a screen with its setup.
- Narrow: Below 820px: same · Reduced motion: answer shown, marker set.
- Use when: revealing the price, the result or the reframe · Avoid when: used more than 3 times; readers start to feel pushed.
- Effort: S · Needs lib: no · Sources: P266 (https://www.melissastoller.com/its-all-about-page-turns/) · Verdict: ADAPT (mandatory scroll-snap and the page-turn wipe cut as scroll hijack)

### CHG-34 Knock-on ripple (new)
- For: cause-effect · 1 change, 3-6 effects
- Instead of: an unordered bullet list of benefits
- Reader sees: One change in a small ink circle at the centre; as you scroll, effects appear on widening rings in the order they happen (this week, this month, this year), each joined to its cause by a short line that inks from dashed to solid.
- Moves: scroll-linked - one ring per caption: the ring pen-draws as a construction circle (1.0-1.4s), then its effects' links pen-draw solid from the inner ring (0.6s each, the next at 80%) and their labels arrive (8px, .6s).
- Build: SVG viewBox 600x600 with 2-3 concentric circles (r 90, 170, 250) as construction lines; effect nodes sit on the rings at chosen angles, each linked to a node on the inner ring (not always the centre) so second-order effects read as knock-ons; HTML labels placed from coordinates; ring names in mono 11px.
- Narrow: Below 768px: an indented list, the change first, then effects grouped under their ring name, each with a short "because" line · Reduced motion: all rings and links drawn.
- Use when: one change sets off several effects and their order matters · Avoid when: the effects are independent (use CHG-07).
- Effort: M · Needs lib: no · Sources: new; built from the TVS constellation and orbit (dashed rings, drawn links) · Verdict: NEW

### CHG-35 Converging causes (new)
- For: cause-effect · 3-5 causes, 1 problem
- Instead of: "Several factors contribute to..." in a paragraph
- Reader sees: Three to five short cause labels down the left; as captions scroll past, a thread draws from each cause and bends right into one trunk; when the last thread joins, the trunk thickens and lands on the problem in one serif sentence, and the offer appears as a single chip at the joining point.
- Moves: scroll-linked - one thread per caption, pen-draw (0.8-1.2s); once all threads join, the trunk stroke goes from 1.6px to 3px over .6s; the fix chip arrives at the knot (8px, .6s) with a marker sweep.
- Build: SVG; thread paths `M x0 yi C xm yi, xm yk, xk yk` into one shared knot; trunk from the knot to the problem box; a stroke-width transition on the trunk; HTML labels placed from coordinates.
- Narrow: Below 768px: vertical version, causes stacked, threads joining downward into the problem card · Reduced motion: all threads drawn, trunk thick, chip placed.
- Use when: several causes feed one problem and the offer acts where they meet · Avoid when: each cause needs its own fix (use CHG-31).
- Effort: M · Needs lib: no · Sources: new; built from the TVS snake path maths and P143 · Verdict: NEW

---

## Choice and fork

### CHG-36 ★ Fork of three choices
- For: choice-fork, call-to-action · 3 options (2-4 by moving endpoints)
- Instead of: three pricing cards in a row
- Reader sees: "Step 6 / You decide what happens next", then a thin line that drops and splits into three branches, each landing on a card: Scale it, Extend it, Stop it.
- Moves: in-view - the trunk pen-draws down (0.6s); the three branches draw together from the split (0.8s, draw ease); the option cards arrive as the branches land (8px, .6s, 80ms stagger).
- Build: SVG viewBox 900x70, `preserveAspectRatio="none"`, height 70px, path `M450 0 V24 M450 24 C450 46 150 30 150 70 M450 24 V70 M450 24 C450 46 750 30 750 70`; `vector-effect:non-scaling-stroke` keeps 1.6px at any width; endpoints at 1/6, 1/2 and 5/6 meet a 3-column grid (gap 16px); `.opt` cards centred, serif 25px titles.
  Draw it with a top-down clip (`clip-path:inset(0 0 100% 0)` to `inset(0)`, .9s draw ease), which avoids dash glitches on non-scaling strokes.
- Narrow: Below 820px: fork hidden, options stack · Reduced motion: fork and cards shown.
- Use when: closing a pilot or the page with explicit, mutually exclusive decisions; the page ends in the ask · Avoid when: the options are not mutually exclusive.
- Effort: S · Needs lib: no · Code: TVS harvest · Sources: P025 (TVS site, page.html ~L341-349, L836-844) · Verdict: ADAPT (the reveal-only fork now draws like a pen and the cards land with the branches)

### CHG-37 ★ Two roads from today (new)
- For: choice-fork, cause-effect, before-after · 2 options (act or wait)
- Instead of: a "cost of doing nothing" paragraph next to a "with us" paragraph
- Reader sees: One dot marked "today" and two roads leaving it: the "if you wait" road draws in muted dashes and thins to a ghost that ends on what is lost; the "with us" road draws in solid ink and ends on the outcome with a marker; a hand-drawn ring then loops around the split, where the ask sits.
- Moves: scroll-linked - caption 1 draws the wait road (dashed, linear with scroll); caption 2 draws the "with us" road solid and its outcome label arrives as the line lands; the ring pen-draws around the split last (1.1s, .3s delay).
- Build: stage of 200vh or less, counter 1 / 2; SVG viewBox 900x420; both roads are cubic paths from one start point; the wait road is `stroke-dasharray:4 7` with a gradient stroke fading from .7 to .25 and is revealed by a solid copy animating inside a `<mask>` (dashes cannot also carry the draw).
  The solid road is 2.4px ink drawn by dashoffset; the ring reuses the TVS path `M150 6C70 4 8 14 8 36s70 30 146 28 142-8 140-30S220 4 128 10`.
- Narrow: Below 768px: static twin, two short cards ("if you wait" with a dashed border above "with us" with an ink border), the ask below · Reduced motion: both roads drawn, ring set.
- Use when: the real choice is acting now or waiting, and the cost of waiting can be named · Avoid when: waiting costs nothing concrete (it then reads as a scare).
- Effort: M · Needs lib: no · Sources: new; built from P164 ghost lines, P469 pivot and the TVS hand-drawn ring · Verdict: NEW

### CHG-38 Elimination by tests (new)
- For: choice-fork, comparison · 3-6 options, 2-4 tests
- Instead of: a comparison matrix of ticks and crosses
- Reader sees: The options listed as plain lines; each caption that scrolls past names one test ("must run without a tech team"), and the options that fail it get a pen strike and fade; one option is left at the end, and the pen loops a ring around it.
- Moves: scroll-linked - per test, failing options get a strike (0.45s pen draw, the next at 80%) and fade to 35% over .4s; after the last test the survivor gets the TVS ring (1.1s, .3s delay).
- Build: `<ul>` of options, each with `data-fails="2"` (the test that removes it); the step observer sets `data-step` on the list and CSS like `[data-step="2"] [data-fails="2"]` triggers the strike; strike and ring are SVG paths drawn by dashoffset with `vector-effect:non-scaling-stroke`; test captions carry a mono 11px "test 2 / 3".
- Narrow: Below 768px: the list stays; each test appears under it as a static note with the struck options already marked · Reduced motion: final list with strikes and ring.
- Use when: you recommend one option and the reasons are hard tests, not trade-offs · Avoid when: options trade off on balance (use CHG-40 or CHG-41).
- Effort: S · Needs lib: no · Sources: new; built from the P343 strike and the TVS hand-drawn ring · Verdict: NEW

### CHG-39 Walked decision tree
- For: choice-fork, sequence · 3-6 questions, 2-4 endings
- Instead of: an interactive quiz the reader has to answer
- Reader sees: A small hand-drawn flowchart in faint dashed lines from "START"; as captions scroll past, the reader's own answer to each question is given ("No tech team on staff: yes"), the taken arrow inks solid, and the path ends at the recommendation.
- Moves: scroll-linked - per question, the taken branch pen-draws solid (0.6-0.9s); untaken branches stay as construction lines at 25%; the outcome box gets the ring at the end.
- Build: SVG nodes and edges with `data-from` and `data-to`; a path list for this reader (`['q1:yes','q2:no','endB']`); `.taken` animates dashoffset to 0; an optional static `feTurbulence` wobble filter on the line layer; the outcome card carries the ask.
- Narrow: Below 768px: one question per row with its answer and a short down arrow between · Reduced motion: final path drawn.
- Use when: the recommendation comes from a few honest questions and the reader should see the reasoning · Avoid when: there is only one question (use CHG-36), or the answers for this reader are unknown.
- Effort: M · Needs lib: no · Sources: P162 (https://datavizcatalogue.com/search/concepts.html), P273 (https://xkcd.com/518/) · Verdict: ADAPT (two interactive flowcharts merged; the reader no longer answers, we walk their path)

### CHG-40 Option lines across criteria
- For: choice-fork, comparison · 2-4 options x 3-6 criteria
- Instead of: a feature comparison table with ticks
- Reader sees: Upright posts for each thing that matters (cost, speed, local support, training), with each option drawn as a line threading between them at low, medium or high; the recommended option draws last as a steady high line in the accent.
- Moves: in-view - posts arrive together; option lines pen-draw left to right one at a time (1.0-1.4s, the next at 85%), the recommendation last; tapping an option chip brings its line forward and fades the others to 20%.
- Build: posts at even x with 3 stops each; one polyline per option, `stroke-linejoin:round`; order the posts so the recommended option reads as a steady line; a three-level scale from stated assessments only; option chips double as the legend.
- Narrow: Below 820px: one card per option with three-dot meters per criterion · Reduced motion: all lines drawn.
- Use when: showing why the recommended option wins on balance · Avoid when: more than 4 options (the lines tangle).
- Effort: S · Needs lib: no · Sources: P149 (https://github.com/Financial-Times/chart-doctor/tree/main/visual-vocabulary) · Verdict: ADAPT (lines now draw in sequence with the recommendation last; tap kept as an extra)

### CHG-41 Trade-off triangle
- For: choice-fork, comparison · 3 corners, 2-5 options
- Instead of: a "fast, good, cheap: pick two" sentence
- Reader sees: A triangle whose corners are three things you cannot all max at once (fast, thorough, low-cost), with each option a dot pulled toward what it favours and a short label; the recommended dot is ringed.
- Moves: in-view - the triangle pen-draws as one path (1.2s); dots arrive at their spots one by one (8px, .6s, 90ms stagger); the ring draws on the recommended dot last.
- Build: barycentric to screen: x = b + c/2, y = c x √3/2 for weights (a, b, c) summing to 1, from stated emphasis such as 2:1:1; coarse weights only (0, 1 or 2 parts) with a caption saying so; the reasons for each placement are listed under the triangle, not hidden behind a tap.
- Narrow: Below 820px: the triangle at 280px with the reasons as a list below · Reduced motion: static with ring.
- Use when: comparing options that balance three qualities · Avoid when: options differ on more than three things (use CHG-40).
- Effort: S · Needs lib: no · Sources: P148 (https://datavizproject.com/data-type/ternary-plot/) · Verdict: ADAPT (dots drifting from the centre became short arrivals; tap explanations moved into a visible list)

### CHG-42 Worded two-axis field
- For: choice-fork, comparison · 4-12 items, or 3-5 package zones
- Instead of: a SWOT grid of four boxes
- Reader sees: A cross of two worded axes (quick to start or slow, small change or big) drawn as construction lines; items land in their quarters one group at a time, and the corner to begin in gets the accent wash. Variant: curved zones (do it yourself, we coach you, we run it) with the client's pin already placed in theirs.
- Moves: in-view - the axes pen-draw outward from the centre (0.8s); items arrive in their spots by quarter (8px, .6s, 80ms stagger capped at 450ms); the chosen corner's wash fades in over .6s last.
- Build: CSS grid 2x2 under an SVG axis layer; items placed by `left` and `top` percentages from the stated judgement; zones are SVG paths with curved borders; no tick values, axes labelled "placed by our judgement"; in-control versus outside and helps versus hurts axes give the SWOT reading as a place.
- Narrow: Below 820px: four stacked quarter cards in priority order, the chosen one first · Reduced motion: static.
- Use when: helping the reader prioritise, or showing which package fits where they are · Avoid when: items do not differ on both axes, or a quarter would hold one lonely item.
- Effort: S · Needs lib: no · Sources: P145 (https://datavizproject.com/data-type/2x2-matrix/), P146 (https://datavizproject.com/data-type/swot-analysis/), P147 (https://datavizproject.com/data-type/phase-diagram/) · Verdict: ADAPT (three placement fields merged; the compass needle overshoot and the reader-dragged pin cut)

### CHG-43 Fan of choice threads
- For: choice-fork, sequence, comparison · 3-5 threads, 3-10 choices each
- Instead of: three case-study cards with a "result" line each
- Reader sees: Threads rising from one shared root, each bending left for one kind of choice and right for the other, ending at different outcomes; the reader's likely thread draws last in the accent.
- Moves: in-view - threads pen-draw one at a time from the root (1.0-2.0s by length, the next at 85%); each end label arrives as its thread lands.
- Build: each choice adds a segment turned ±θ, with θ x 0.85 and length x 0.92 per step so threads settle (as in Notabilia); polylines with round joins; a caption says what left and right mean; threads are real scenarios or worked examples.
- Narrow: Below 820px: same, at most 5 threads · Reduced motion: all threads drawn.
- Use when: small choices from the same start lead to different places · Avoid when: there is a single decision (use CHG-36 or CHG-37).
- Effort: M · Needs lib: no · Sources: P153 (https://truth-and-beauty.net/projects/notabilia) · Verdict: ADAPT (threads draw in sequence with house timing; the reader's thread last in the accent; capped at 5)

---
