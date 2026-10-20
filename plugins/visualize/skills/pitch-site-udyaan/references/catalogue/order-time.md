# Order and time: sequence, cycle, roadmap

Pattern library family for `pitch-site-udyaan`. 41 entries (8 starred), curated from slice1 (61 raw entries).
Verdicts: 2 KEEP, 34 ADAPT, 5 NEW, 11 CUT (listed at the end).

**Shorthand used in every entry (house motion values):**
- **pen draw**: stroke-dashoffset from length to 0, duration = length / 600 px/s, clamped 0.6-2.2s, next stroke starts at 80-85% of the previous one, ease cubic-bezier(.45,.05,.35,1).
- **arrives**: opacity 0 to 1 plus a rise of 16px or less (12px default), 0.6-1.0s, cubic-bezier(.22,1,.36,1). Staggers 60-110ms, total capped at 450ms. Nothing enters from the side.
- **reveals once**: text arrives the first time it enters the view and always finishes; it never reverses on scroll-up.
- **scroll-linked**: linear, tied 1:1 to progress. Drawings may follow scroll back and forth; text never does.
- **construction line**: the faint dashed version of a line (about 25% ink, dash "2 6") shown before it is explained; it draws solid when its caption arrives.
- **pinned**: a sticky stage whose section is 3 viewport heights or less, with an `n / N` counter, and a stacked static twin below 768px.
- **accent**: the one colour that points. Everything else is ink, paper and chalky flat tints. Texture never animates.

---

## Family picker

Pick by what the content is, how many items, and how the items relate. Starred first. If unsure: sequence goes to SEQ-01, cycle to SEQ-22, roadmap to SEQ-30.

**Sequence (things happen in order)**
- Problems with answers, 3-6, sequential, should feel like one journey: SEQ-01, SEQ-20.
- Parts of one thing explained in order, 3-6, all linked to one picture: SEQ-02, SEQ-08.
- One deliverable going from idea to finished, 3 stages: SEQ-03, SEQ-09.
- Pain across phases, 4-7, opposed (pain, then relief): SEQ-04, SEQ-12.
- Steps that each hand over something tangible, 3-5: SEQ-06, SEQ-13.
- Steps that stack toward one outcome, 3-6, cumulative: SEQ-07, SEQ-19.
- Offer that grows feature by feature, 4-12, additive: SEQ-08, SEQ-09.
- Automatic process with one decision, 4-6 nodes: SEQ-10, SEQ-18.
- Early steps enable late ones, 5-12, linked: SEQ-11, SEQ-07.
- Delay and hand-offs are the pain, 4-10, opposed (today versus with us): SEQ-04, SEQ-12.
- Client must contribute, 3-8 steps with inputs, linked: SEQ-13, SEQ-06.
- One insight told as a story, exactly 4: SEQ-14, SEQ-15.
- Backstory or chronology, 4-8 frames: SEQ-01, SEQ-15.
- "You ask, it's done" speed, 1 task with 3-8 beats: SEQ-16, SEQ-17.
- How a shortlist was chosen, 8-40 candidates, ranked by filtering: SEQ-18, SEQ-19.
- Journey toward one focused goal, 3-5 rings, ranked by closeness: SEQ-19, SEQ-07.
- Chunky phases that build on each other, 3-4, one screen each: SEQ-01, SEQ-20.
- Next steps at the close, exactly 3: SEQ-05, SEQ-09.
- Long page needs orientation, 4-9 chapters: SEQ-21 (works alongside any entry).

**Cycle (it repeats)**
- Steps around one object, 4-6, equal: SEQ-22, SEQ-24.
- Reinforcing loop (flywheel), 3-6, linked cause and effect: SEQ-23, SEQ-25.
- One person or core feeding a group, 4 stages, people: SEQ-24, SEQ-29.
- Operating rhythm that produces an output, 3-6 phases: SEQ-25, SEQ-26.
- Meeting and reporting cadence, 2-6 activity types, grouped: SEQ-26, SEQ-25.
- One-time setup, then a repeating rhythm, 2-4 plus 3-5: SEQ-27, SEQ-25.
- Seasonal or yearly cycle, 7-12 segments: SEQ-28, SEQ-26.
- Two sides passing work back and forth, 2 parties, 2-4 passes, opposed: SEQ-29, SEQ-34.

**Time and roadmap (when things happen)**
- One thing changing over time, 3-5 bands: SEQ-30, SEQ-33.
- Parallel workstreams sharing milestones, 2-5 streams, grouped and linked: SEQ-31, SEQ-36.
- One stream of milestones, 4-10, sequential: SEQ-32, SEQ-35.
- No firm dates, certainty falls with distance, 3 horizons, ranked: SEQ-33, SEQ-40.
- Responsibility moves to the client, 3-5 phases, linked: SEQ-34, SEQ-29.
- Whole plan in one glance, 5-12 rounds: SEQ-35, SEQ-36.
- Long programme where pacing matters, 6-20 milestones: SEQ-37, SEQ-32.
- What an ordinary day looks like after, 3-5 moments: SEQ-38, SEQ-14.
- Past results: SEQ-39, SEQ-41. Future range: SEQ-40 (pairs after SEQ-39).

---

## Sequence

### SEQ-01 ★ Snake of problem stops
- For: sequence, cause-effect · 3-6 stops + 1 end card
- Instead of: a numbered list of problems and fixes
- Reader sees: Cards zig-zag down the section; a faint dotted line weaves between numbered knots on their inner edges, an ink line traces it as they scroll, each knot turns marker-yellow when the line reaches it, and the path ends on a dark "where this leads" card.
- Moves: scroll-linked - reach = clamp(0, height, innerHeight × .62 - snakeTop); strokeDashoffset = L × (1 - reach / height); knot gets `.lit` when reach ≥ knotY - 4 (background .4s ease); card text reveals once (12px, .75s).
- Build: `.snake` flex column, gap 30px, with an absolute SVG holding `.sl-base` (2px, dash "1 8", 22% ink, the construction line) and `.sl` (2.4px ink). Stops are `calc(50% - 70px)` wide, even ones `align-self:flex-end`; a 36px knot hangs 18px off the inner edge. Path runs through measured knot centres with `C x0 (y0+dy×.55), x1 (y1-dy×.55), x1 y1`, rebuilt on resize, load and `document.fonts.ready`. Light variant: short labels beside small stones instead of cards, stone positions from `getPointAtLength`.
- Narrow: ≤820px one column, margin-left 46px, knots form a left rail at -64px, segments wiggle ±14px · Reduced motion: line fully drawn, all knots lit.
- Use when: a chain of problem-to-answer steps should feel like one journey and the scroll is the progress bar. · Avoid when: steps are unordered, more than 6, or you are tempted to run the line through the whole page.
- Effort: M · Needs lib: no · Code: TVS harvest · Sources: P013 (TVS page.html L287-310, L411-415, L562-596, L1052-1082), P317 https://css-tricks.com/svg-line-animation-works/ · Verdict: KEEP (P317 folded in as the label-only variant)

### SEQ-02 ★ Pinned line-drawn stage
- For: sequence, part-whole · 3-6 steps about one subject
- Instead of: a feature list with an icon per item
- Reader sees: One line drawing stays parked on one side while short captions scroll past on the other; each caption changes exactly one thing in the drawing (a label lands on its spot, an x-ray layer shows the inside, or the view pulls back to show the world around it), with a "2 / 5" counter.
- Moves: scroll-linked step index - one change per step: new strokes pen draw; a callout arrives at its anchor (scale .96 to 1 with opacity, .6s ease-out); a pullback scales the background group linearly with scroll under a subject that never moves; captions reveal once.
- Build: two-column grid; stage column `position:sticky; top:12vh; height:76vh`; every state lives in one SVG (same viewBox, one group per step). Caption blocks are `min-height:60vh`; one IntersectionObserver with `rootMargin:"-45% 0px -45% 0px"` sets `stage.dataset.step` and CSS shows `[data-for~="n"]`. Callouts sit at viewBox percentages so they stay on their spot. One progress value drives picture, caption and counter so they can never disagree. Section ≤ 3 viewport heights.
- Narrow: <768px static twin: each caption gets its own cropped still of the drawing in that state, stacked · Reduced motion: final state with all callouts numbered and a legend.
- Use when: explaining parts of one thing (a service, a site, a plot of land, a dashboard) where the picture is the anchor. · Avoid when: items are unrelated and each needs its own visual, or there is nothing in the drawing to point at.
- Effort: M · Needs lib: no · Sources: P167 https://superhuman.com, P409 https://heronaiapp.com, P056 https://ciechanow.ski/mechanical-watch/, P458 (video reference: speed-streaks ascent, map-underlay fade) · Verdict: ADAPT, changed: whole-picture crossfades became one change per step; caption strip folded in as the n / N counter; pin capped at 3 screens; narrow uses stills instead of a sticky band.

### SEQ-03 ★ Construction lines to finished drawing
- For: sequence, before-after, big-idea · 3 stages of one deliverable
- Instead of: "Phase 1 / Phase 2 / Phase 3" boxes
- Reader sees: The deliverable first appears as pale dashed construction lines with pencil notes, then the real parts draw over them in ink and fill with chalky tints, then the finished thing is uncovered behind a single scan line; a small label reads Plot, Build, Live with the current word underlined.
- Moves: scroll-linked (pinned) - Plot: guides pen draw, notes reveal once; Build: real strokes pen draw over the guides, guides dim to .2, tints fade in over .6s; Live: `clip-path: inset()` widens linearly with scroll with a 1px accent scan line at its edge.
- Build: sticky stage in a 250-300vh section. One SVG with groups `.plot`, `.build`, `.live`; paths use `pathLength="1"` so dashoffset 1 to 0 is uniform. Progress feeds a hand-rolled timeline: an array of `{el, prop, from, to, start, end}` interpolated each scroll frame. The stage label underline follows the stage.
- Narrow: <768px three stacked frames (Plot, Build, Live), each pen drawn once on view · Reduced motion: three finished frames labelled Plot, Build, Live.
- Use when: showing how an idea becomes a deliverable, or that value arrives early and then sharpens (launch, tuned, complete). · Avoid when: you cannot draw the plot stage honestly, or each phase is a different deliverable.
- Effort: L · Needs lib: no · Sources: P423 https://piergorelli.com, P062 https://www.redblobgames.com/articles/visibility/ · Verdict: ADAPT, changed: blur-to-sharp replaced by dashed-to-solid lines; clickable tab bar became a passive stage label; GSAP removed; pin capped.

### SEQ-04 ★ Feelings line
- For: sequence, before-after, people-roles, opposed · 4-7 phases
- Instead of: a bulleted list of pain points
- Reader sees: The phases of their year sit as columns with one hand-drawn wavy line running through them, high where things feel fine and low where they hurt; at each dip a small note hangs on a dashed tie: "we step in here".
- Moves: scroll-linked - the line draws with dashoffset = L × (1 - p); each dip note arrives once the line reaches its x; the notes are the only accent.
- Build: points at x per phase, y on a 3-level band (low, neutral, high), smoothed Catmull-Rom to bezier. Notes are HTML at the dip x on dashed ties. The y axis is a worded band from interviews ("how it feels"), never a score. An optional faint "with us" line pen draws on view after the first finishes.
- Narrow: ≤820px phases run downward and the line wiggles left and right · Reduced motion: final line, all notes shown.
- Use when: the pitch is empathy first, then relief. · Avoid when: nothing in research or the brief supports the feelings (never guess emotions).
- Effort: M · Needs lib: no · Sources: P130 https://www.nngroup.com/articles/journey-mapping-101/ · Verdict: ADAPT, changed: popping tags replaced by notes that arrive on dashed ties; optional "with us" line added.

### SEQ-05 Pictured start steps
- For: sequence, call-to-action · exactly 3
- Instead of: "Next steps: 1, 2, 3" bullets
- Reader sees: Three cards on the dark closing band, each opening with a small line picture (a list with one option circled by hand, a person in a yellow disc with signal lines, a document with a yellow tick), then "STEP 1" and a serif title.
- Moves: in-view - cards arrive with 0 / 100 / 200ms stagger; the hand-drawn ring pen draws over 1.1s after .3s.
- Build: `.start` grid 3 columns, gap 16px; card background rgba(244,241,234,.06), ring rgba(244,241,234,.14), radius 16px, padding 26px; `.pic` 160px tall; pictograms are 130×96 SVGs with 2.4-2.6px strokes and the last stroke in marker. Ring path `M150 6C70 4 8 14 8 36s70 30 146 28 142-8 140-30S220 4 128 10`, 3px marker, `vector-effect:non-scaling-stroke`.
- Narrow: ≤820px one column · Reduced motion: static, ring shown drawn.
- Use when: the close must make the first step feel small and concrete, right before the ask. · Avoid when: steps need more than 2 lines each, or mid-page (it is a closer, not a step strip).
- Effort: S · Needs lib: no · Code: TVS harvest · Sources: P027 (TVS page.html L215-220, L377-390, L887-911; harvest section 2.14) · Verdict: KEEP

### SEQ-06 Steps that drop deliverables
- For: sequence, part-whole · 3-5 steps
- Instead of: a list of steps with a separate deliverables table
- Reader sees: Numbered steps run down the page; as each step passes, a small line-drawn document chip (Signed agreement, Site plan, Training kit) settles into a tray pinned at the bottom of the section, and the tray reads "3 of 5".
- Moves: in-view per step - that step's chip arrives with a 16px drop and fade (.6s ease-out); the tray count swaps once; nothing else moves.
- Build: steps as an `<ol>`; tray is `position:sticky; bottom:1rem` inside the section so it leaves with it. An IntersectionObserver per step appends that step's chip from a `<template>`. Each step names what it produces and a relative span ("first two weeks"), never a date.
- Narrow: <768px tray becomes the line "3 of 5 documents"; chips also sit under each step · Reduced motion: tray pre-filled, chips also under each step.
- Use when: each step hands the reader something they will own. · Avoid when: steps produce nothing visible.
- Effort: M · Needs lib: no · Sources: P182 https://stripe.com/atlas · Verdict: ADAPT, changed: 24px drop cut to 16px; Ramp curve swapped for house ease-out; day stamps made relative.

### SEQ-07 Staircase to the outcome
- For: sequence, cause-effect · 3-6 cumulative steps
- Instead of: a numbered list where the order hides the dependency
- Reader sees: One ink line draws a staircase climbing to the right; each tread names one capability, and the top step holds the reader's outcome in a marker highlight.
- Moves: in-view - the staircase pen draws as one stroke (max 2.2s); each tread label arrives as the pen passes it; the marker sweep on the top label runs last.
- Build: one SVG polyline of treads (x step = width / n, rise = height / n). Labels are HTML in a `repeat(n,1fr)` grid with `align-items:end` so they wrap; each label's delay = its tread's fraction of the path length × the draw duration.
- Narrow: ≤820px a vertical stack, step 1 first, each card indented 12px more than the last so the climb still shows, outcome last · Reduced motion: staircase drawn, labels shown, top highlighted.
- Use when: each item unlocks the next and the end is one outcome. · Avoid when: items are independent (stairs imply dependency).
- Effort: S · Needs lib: no · Sources: P318 https://developer.mozilla.org/en-US/docs/Web/CSS/offset-path · Verdict: ADAPT, changed: rising blocks became one drawn line; the hopping dot was cut.

### SEQ-08 New pieces in accent
- For: sequence, part-whole · 4-12 additive steps
- Instead of: a feature list
- Reader sees: One line drawing gets built step by step; the pieces added at each step are drawn in the accent while earlier pieces settle to grey ink, and a small corner note lists exactly what this step adds ("+ weekly report"), with "4 / 9".
- Moves: scroll-linked step index (pinned) - new pieces pen draw in the accent; the previous step's accent fades to ink over .6s; the corner note arrives (12px).
- Build: SVG groups with `data-step`; at step n earlier groups get `.old` (50% ink), step n gets `.new` (accent stroke). Same sticky stage as SEQ-02. Above 6 steps, group sub-steps under one scroll step but keep the main numbering so the count reads as progress.
- Narrow: <768px static twin: one cropped still per step with the new parts in accent · Reduced motion: final drawing with each part labelled by the step that added it.
- Use when: the offer builds feature by feature and each addition should feel concrete. · Avoid when: steps are not additive.
- Effort: M · Needs lib: no · Sources: P245 https://bricknerd.com/home/how-lego-instructions-have-changed-over-time-a-forest-of-discovery-10-17-22 · Verdict: ADAPT, changed: overshoot drop-in replaced by pen drawing; range capped by the 3-screen pin.

### SEQ-09 Build-up that folds into the button
- For: sequence, call-to-action, big-idea · 4-6 steps, then 1 ask
- Instead of: a summary paragraph above a "Get started" button
- Reader sees: The last section rebuilds the page's main drawing in a few strokes (a line, a frame, the parts), a counter reads "built 60%", and on the final step the drawing shrinks into the one button they are asked to press.
- Moves: scroll-linked (pinned) - each step adds one layer (pen draw, or tint fade .6s); the counter follows progress linearly; final step: the group moves from its box into the button's box over .9s ease-out, then the real button takes its place.
- Build: pinned stage, about 50vh per step. SVG layers per step; progress gives step index plus local progress. The collapse is FLIP: measure the button rect, transform the group from its box to the button box. A real, focusable `<a class="cta">` replaces the drawing.
- Narrow: <768px short vertical stack of the steps, then the real button · Reduced motion: the button with a numbered list of what it buys.
- Use when: closing on "everything above is what this one decision buys". · Avoid when: the ask is not a single action.
- Effort: L · Needs lib: no · Sources: P427 https://metic.studio/en · Verdict: ADAPT, changed: pencil size guides dropped; collapse uses house ease-out; pin capped.

### SEQ-10 Pipeline with one gate
- For: sequence, cause-effect · 4-6 nodes + 1 decision
- Instead of: a flowchart image
- Reader sees: A column of labelled boxes joined by a line (request, check, score, decide); one accent pulse runs down it, pauses at a hand-drawn diamond and takes the "yes" lane, while the "no" lane stays dashed.
- Moves: in-view - the connecting line pen draws first; then one pulse rides it once (`offset-distance` 0 to 100%, linear, 2.4s); each box gets an ink outline as the pulse arrives (.4s ease); at the gate the chosen lane pen draws. A "run again" tap replays.
- Build: one SVG path through node centres; the pulse is a 10px circle with `offset-path:path(...)` animated by WAAPI; a node lights when `animation.currentTime` passes its fraction (read in rAF). The two lanes are separate paths; "no" stays a construction line.
- Narrow: already vertical; ≤820px boxes go full width · Reduced motion: diagram drawn, nodes numbered, chosen lane solid.
- Use when: an automatic process has one decision (approve or reject, fit or not). · Avoid when: there are nested branches, or the reader is the one choosing.
- Effort: M · Needs lib: no · Sources: P180 https://attio.com · Verdict: ADAPT, changed: looping 5s token became one pass with a replay tap; layout turned vertical; unchosen lane kept as a construction line.

### SEQ-11 Dependency arcs
- For: sequence, linked · 5-12 steps, up to 15 links
- Instead of: "this step depends on that one" footnotes
- Reader sees: The steps sit as dots on one line; faint dashed arches join early steps to the late steps they make possible, and each arch draws solid when its step is explained, with the one being explained in the accent.
- Moves: scroll-linked - the diagram is sticky while captions scroll beneath; as each caption passes, its arcs draw with dashoffset tied to that caption's progress; unexplained arcs stay construction lines.
- Build: nodes evenly spaced; arc `M xi,y A r,r 0 0 1 xj,y` with r = |xj - xi| / 2 (above means "relies on", below means "unlocks"). Two copies per arc: a dashed base and a solid copy driven by dashoffset. Constant stroke width; a real frequency ("every week") becomes a label on the arc. Section ≤ 3 viewport heights.
- Narrow: ≤820px the line turns vertical and arcs bulge to the right; <768px all arcs drawn, captions listed below · Reduced motion: all arcs solid and labelled.
- Use when: early steps quietly enable late ones and the reader must see why order matters. · Avoid when: more than about 15 links (arcs nest into noise).
- Effort: S · Needs lib: no · Sources: P114 https://datavizcatalogue.com/methods/arc_diagram.html · Verdict: ADAPT, changed: added the dashed-to-solid rule, one accent for the arc being explained, and a sticky diagram.

### SEQ-12 Waiting made visible
- For: sequence, before-after, opposed · 4-10 steps
- Instead of: "the current process is slow" in a paragraph
- Reader sees: Today's steps sit along a line that rises for real work and dips for waiting, each dip labelled ("waits for approval"), so the waiting looks as big as it feels; a second "with us" line below has shallow dips.
- Moves: scroll-linked - the "today" line draws linearly with scroll and dip labels reveal once as it reaches them; then the "with us" line pen draws on view.
- Build: polyline alternating between two y levels; wait widths come from the brief, otherwise equal widths with a "not to scale" note. Labels name the wait and never invent a duration. Vertical form: stacked work panels whose gap is the wait, holding a dotted line and a small clock label, `margin-top: clamp(8px, calc(var(--days) * 2px), 120px)`.
- Narrow: ≤820px the vertical form · Reduced motion: both lines drawn, labels shown.
- Use when: the pain is delay and hand-offs, not the work itself. · Avoid when: the steps themselves are the problem, or wait times are guesses.
- Effort: S · Needs lib: no · Sources: P142 https://en.wikipedia.org/wiki/Value-stream_mapping, P263 https://en.wikipedia.org/wiki/Panel_(comics) · Verdict: ADAPT, changed: comic gutter idea folded in as the vertical form; its horizontal scroll strip dropped.

### SEQ-13 Recipe card: what you bring, what we do
- For: sequence, linked, call-to-action · 4-10 inputs + 3-8 steps
- Instead of: a "client responsibilities" bullet list
- Reader sees: An index card on paper: title, time and "serves" at the top; on the left what the client provides (data, access, two hours a week) in the order it is used; on the right the numbered method. As each method step becomes active, the inputs it uses get a marker underline.
- Moves: scroll-linked step index - the active step gets an ink rule; its inputs get a marker sweep (.6s ease-out, left to right); one step at a time.
- Build: `grid-template-columns:1fr 2fr`; inputs carry `data-steps="2 4"`; an IntersectionObserver per method step sets `data-active` on the card and `:has()` selectors light the matching inputs. Inputs column is sticky; ruled lines via `repeating-linear-gradient` (static).
- Narrow: ≤820px inputs stack above the method and each method step lists its inputs inline · Reduced motion: every input shows its step numbers, no sweeps.
- Use when: the client must contribute and needs to know exactly what and when. · Avoid when: the client provides nothing.
- Effort: S · Needs lib: no · Sources: P248 https://www.adobe.com/acrobat/guides/recipe-card-template · Verdict: ADAPT, changed: slide-out-of-the-box entrance and saved tick boxes cut; lighting became the marker sweep.

### SEQ-14 Four-beat story strip
- For: sequence, cause-effect, big-idea · exactly 4
- Instead of: a problem paragraph followed by a solution paragraph
- Reader sees: Four equal line-drawn panels stacked down the page (setup, development, twist, result); the twist panel carries the marker highlight that turns the reader's view of their problem.
- Moves: in-view - each panel's drawing pen draws as it enters; its caption reveals once; the twist's marker sweep runs after its drawing finishes.
- Build: CSS grid of 4 rows, each panel `aspect-ratio:4/3`, max 720px wide; one SVG per panel with strokes queued at 80% of the previous stroke.
- Narrow: natively vertical; panels full width · Reduced motion: all panels drawn, marker shown.
- Use when: one insight works as a ten-second story. · Avoid when: you have more than one point.
- Effort: S · Needs lib: no · Sources: P265 https://en.wikipedia.org/wiki/Yonkoma · Verdict: ADAPT, changed: tilt on panel 3 cut; emphasis moved to the marker sweep.

### SEQ-15 Unrolling scroll story
- For: sequence, time · 4-8 frames
- Instead of: a "background" or "how we got here" section
- Reader sees: A tall painted-scroll strip inside a thin kolam-dot border unrolls one frame at a time; each frame is a line drawing with a two-line caption beneath, like the song a patua sings while unrolling.
- Moves: scroll-linked - the strip's bottom clip follows scroll linearly; when a frame is fully uncovered its strokes pen draw; captions reveal once.
- Build: `clip-path: inset(0 0 calc((1 - var(--p)) * 100%) 0)` on the strip; frames stacked inside; a 1px rule at the clip edge; the border is a static repeating SVG motif that never animates. Captions two lines at most.
- Narrow: unchanged (it is vertical); <768px the clip is removed and frames pen draw on view · Reduced motion: fully unrolled, frames drawn.
- Use when: a chronological backstory needs rhythm (how the client got here). · Avoid when: captions need paragraphs, or the snake already carries the story.
- Effort: M · Needs lib: no · Sources: P282 https://en.wikipedia.org/wiki/Pattachitra · Verdict: ADAPT, changed: roller with cylinder shadow and painted borders cut; frames draw on instead of appearing painted.

### SEQ-16 Scripted mini-demo with Replay
- For: sequence, cause-effect · 1 task, 3-5 beats
- Instead of: "it's fast and easy" claims
- Reader sees: A small line-drawn app window plays a tiny film: a request types itself, the send button gets a hand-drawn ring, three working lines write themselves, then the finished result settles in. A Replay link sits underneath.
- Moves: in-view, once (threshold .5) - typing via `clip-path: inset(0 100% 0 0)` to `inset(0)` over `steps(chars)`; a 1px caret blinks `1s step-end` only while typing; the click ring pen draws (.6s); working lines write in at 80% overlap; the result arrives (12px, .6s). Replay is a tap.
- Build: one container whose `data-phase` moves through typing, clicked, working, done; an async function awaits small cancellable waits between phases (a generation number kills a run mid-flight); all visuals are CSS keyed on `[data-phase]`. Replay bumps the generation and reruns.
- Narrow: window scales to .85 or drops its side panel · Reduced motion: request and finished result side by side, no Replay.
- Use when: the service is "you ask, it's done" and the reader should feel the speed. · Avoid when: the real process takes days (a 6-second film then misleads).
- Effort: M · Needs lib: no · Sources: P170 https://claude.com/product/overview · Verdict: ADAPT, changed: clay colour, overshoot panel entrance and pulsing "thinking" rows (a loader) removed; the click ring is hand-drawn.

### SEQ-17 Work receipt
- For: sequence, proof-trust · 4-8 lines
- Instead of: "we handle the busywork" claims
- Reader sees: A paper receipt prints line by line ("Read 128 messages", "Matched 14 invoices") with a running time in the margin, ending in a total line with the marker on it: "Done in 4 min".
- Moves: in-view, once - lines arrive every 600-900ms (8px rise, .6s); the time ticks with `step-end`; the final line's marker sweep runs last; the receipt always finishes.
- Build: `<ol class="receipt">` with lines hidden; a setTimeout chain reveals them in order; monospace 13-14px at line-height 1.52; a static perforated top edge in SVG; ticks are SVG checks, never emoji.
- Narrow: top 4 lines plus the total · Reduced motion: full receipt with the final time.
- Use when: the work is invisible (checking, reconciling, analysing) and the reader should feel the effort they skip. · Avoid when: the numbers are not real.
- Effort: S · Needs lib: no · Sources: P185 https://mercury.com · Verdict: ADAPT, changed: terminal look became a paper receipt; token counter dropped.

### SEQ-18 Sieve: how the shortlist was chosen
- For: sequence, ranked · 8-40 candidates, 3-5 sieves
- Instead of: "we evaluated 30 options and picked 3"
- Reader sees: Real candidates (sites, crops, partners) as small chips resting on line-drawn sieve layers; at each layer the ones that stop stay behind in grey with the reason written beside them, and the rest settle to the next layer.
- Moves: scroll-linked step index (pinned) - at each sieve, passing chips move down one layer (.6s ease-out, 60ms stagger capped at 450ms); stopped chips fade to 40% and their reason tag arrives.
- Build: absolutely positioned chips; per stage compute each chip's target y; reason tags are HTML beside the layer. All sieve layers are the same width (a tapering funnel implies shares). Real counts only when the brief has them.
- Narrow: <768px static twin: one list per layer with "stopped here because" under each · Reduced motion: the final layer plus where each chip stopped.
- Use when: the reader should trust the selection. · Avoid when: you don't have the real candidates.
- Effort: M · Needs lib: no · Sources: P163 https://datavizproject.com/data-type/funnel-chart/ · Verdict: ADAPT, changed: sieve shake and random jitter cut; house ease and stagger cap applied.

### SEQ-19 Bullseye: stepping in to the goal
- For: sequence, big-idea, ranked · 3-5 rings
- Instead of: a progression list that ends in "the goal"
- Reader sees: Concentric dashed rings with the outcome at the centre; a marker steps inward one ring per stage, and each ring it enters draws solid and fills with a chalky tint.
- Moves: scroll-linked step index - the marker moves along a spiral path to the next ring (.8s, pen ease); the ring pen draws from dashed to solid; its tint fades in over .6s.
- Build: circles at r = R × (n - i) / n; ring names on `textPath` arcs; the marker's position comes from `getPointAtLength` on a spiral path. Rings are equal width (stages, not quantities).
- Narrow: 300px wide, captions below · Reduced motion: marker at the centre, all rings solid and labelled.
- Use when: a journey toward one focused goal. · Avoid when: stages branch.
- Effort: S · Needs lib: no · Sources: P144 https://datavizproject.com/data-type/target-diagram/ · Verdict: ADAPT, changed: added the dashed-to-solid ring rule and tint fill.

### SEQ-20 Card pile
- For: sequence, list-of-equals · 3-4 chunky phases
- Instead of: a long column of phase sections
- Reader sees: One card per phase; each new card slides up over the last, and earlier cards stay peeking above it in a neat pile, so the order is felt.
- Moves: scroll-linked - each card's inner content is sticky; earlier cards scale to about .94 (1 - .02 × depth), linear, over the `exit-crossing` range; no rotation.
- Build: stickiness on the inner `.card__content`, not the card, so scroll length stays honest; `top: calc(10vh + var(--index) * 1.5rem)` so earlier edges peek. The scale runs on `animation-timeline: view()` inside `@supports`; the fallback is plain sticky with peeking edges. Cards ≤ 70svh tall.
- Narrow: <768px plain stacked cards · Reduced motion: plain stacked cards, no scale.
- Use when: phases each build on the last and each fills a screen. · Avoid when: items must be compared side by side (the pile hides earlier ones).
- Effort: S · Needs lib: no · Sources: P193 https://scroll-driven-animations.style/demos/stacking-cards/css/, P332 (same demo) · Verdict: ADAPT, changed: shrink softened from .7 to about .94 so earlier cards stay legible; capped at 4 to respect the 3-screen rule.

### SEQ-21 Chapter rail with n / N
- For: sequence, utility · 4-9 chapters
- Instead of: a nav bar nobody uses
- Reader sees: Each chapter opens with a large serif numeral and a short title; a slim rail at the side lists every chapter with the current one inked and a thin line filling as they read; on tablets a top bar reads "02 / 07".
- Moves: scroll-linked - the rail line's `scaleY` follows page progress; the current label gets ink and a dot (.3s); the numeral arrives once (12px, .8s).
- Build: chapters are `<section data-ch>`; one IntersectionObserver with `rootMargin:"-40% 0px -55% 0px"` sets the active one; the rail is a fixed `<nav>` of anchor links (tap to jump). Progress via `animation-timeline: scroll(root)` inside `@supports`, else one passive scroll handler.
- Narrow: ≤820px rail hides; a thin top bar shows previous, current and next names with "02 / 07" · Reduced motion: no fills; current chapter still marked.
- Use when: the page has 4 or more chapters and readers need to know where they are. · Avoid when: under 4 chapters; never let the rail become a line through the copy.
- Effort: S · Needs lib: no · Sources: P415 https://townhouse.dev, http://chladni-plate-experiment.vercel.app; P236 https://en.wikipedia.org/wiki/Wayfinding · Verdict: ADAPT, changed: train-door strip map merged in as the narrow bar; numeral rise cut to 12px.

---

## Cycle

### SEQ-22 ★ Orbit of steps around one project
- For: cycle, sequence, equal · 4-6 steps + 1 centre
- Instead of: a clip-art ring of circular arrows
- Reader sees: A dotted ellipse around a turmeric disc ("Five steps around one project"); numbered icon nodes sit on the ring with labels outside, and a small accent dot travels the ring once, lighting each step yellow as it passes.
- Moves: in-view (threshold .3) - rAF loop, linear, 11000ms per lap from -90° (the top); a node is `.lit` once the dot's angle ≥ node angle - 2° (background .4s ease); after one lap the dot parks at the top with every node lit; a "go round again" tap replays the lap.
- Build: box `aspect-ratio:1000/640`, max 1000px; SVG ellipse cx 500 cy 320 rx 250 ry 215, 1.6px dashed "2 9" round. Nodes are HTML at x = 500 + 250·cos a, y = 320 + 215·sin a, set as % (left x/10, top y/6.4). Label sits right of the node when cos a > -.2, else left, offset 4.4%, width 24%, with a paper background that masks the ring. Centre disc 27% wide; node 56px with a 2px ink ring, 28px icon, 22px ink number badge.
- Narrow: ≤820px orbit hidden; `.orbit-list` built from the same data shows numbered cards (48px node, then text) · Reduced motion: all nodes lit, dot hidden.
- Use when: every step revolves around one object and "this repeats" should be implied. · Avoid when: steps branch, or label lengths vary a lot (labels collide).
- Effort: M · Needs lib: no · Code: TVS harvest · Sources: P023 (TVS page.html L323-340, L417-422, L831-835, L1084-1120) · Verdict: ADAPT, changed: endless loop with reset now runs one lap and rests lit, with replay on tap; dot uses the single accent.

### SEQ-23 ★ Flywheel loop
- For: cycle, cause-effect, linked · 3-6 nodes
- Instead of: a circular arrow diagram with plus icons
- Reader sees: Three to six line-drawn circles joined by curved arrows marked "+"; the loop starts as faint dashed lines, each arrow draws solid as its caption explains it, and once the loop is closed a single accent pulse runs round it once, each circle's ring thickening as it passes.
- Moves: scroll-linked step index - arrow n pen draws when its caption arrives; after the last arrow, one pulse lap (900ms per arrow, linear); each node ring goes 1px to 2.5px on arrival (.4s ease). No endless loop.
- Build: SVG paths, each with a dashed construction copy beneath; the pulse is a small circle placed by `getPointAtLength` in rAF; node labels are HTML. A "spin again" tap replays the lap. Section ≤ 2 viewport heights.
- Narrow: same diagram at 320px with captions below; <768px no pin, arrows pen draw on view · Reduced motion: loop drawn solid with numbered arrows.
- Use when: the pitch is a flywheel (better content brings traffic, traffic brings data, data makes better content). · Avoid when: the loop is wishful or one link is unproven.
- Effort: M · Needs lib: no · Sources: P074 https://ncase.me/loopy/ · Verdict: ADAPT, changed: ambient endless pulses and swelling nodes replaced by draw-when-explained plus one pulse lap.

### SEQ-24 Teaching circle with stepped callouts
- For: cycle, people-roles, linked · 1 centre figure, 6 ring figures, 4 stages
- Instead of: a team list or an org chart
- Reader sees: A yellow disc holding a line-drawn figure (the guide) inside a ring of six small people; dashed leaders run to four numbered corner cards; lines draw from the guide to each person and they turn yellow one by one, while the card for the current stage gets an ink outline, with "2 / 4".
- Moves: scroll-linked step index (pinned, 4 steps) - active callout ring goes 1px to 2.5px ink (.4s ease); on stage 1 the six lines pen draw at 120ms + i×80ms (total stagger under 450ms), and each person fills marker 450ms after its line.
- Build: box `aspect-ratio:1000/640`; SVG outer dashed circle r 190, inner circle r 120, 4 dashed leaders to the corners, guide r 54 in marker with a head-and-shoulders path; people at r 120 every 60° (r 17 circle + r 5 ink head); teaching line from r 58 to r 98. Callouts absolute, 30% wide in the four corners, radius 16px, 26px ink number badge. Replace the harvest's `setInterval` with the step index from SEQ-02's observer.
- Narrow: ≤820px the SVG becomes a 260px banner and callouts stack as cards; <768px no pin · Reduced motion: all people filled, lines drawn, all four callouts outlined.
- Use when: one person or core feeds a group and four stages happen around it. · Avoid when: the stages are strictly linear (use SEQ-01).
- Effort: M · Needs lib: no · Code: TVS harvest · Sources: P026 (TVS page.html L351-374, L408-409, L424-427, L858-874, L1122-1148) · Verdict: ADAPT, changed: 3.2s auto-rotating callouts (a carousel) replaced by scroll steps; 260ms line stagger cut to fit the 450ms cap.

### SEQ-25 Rhythm dial
- For: cycle, cause-effect · 3-6 repeating phases
- Instead of: "we meet weekly and review monthly" in a sentence
- Reader sees: A dial with phase names around its rim (plan, make, ship, review) and a hand that turns as they scroll; the current phase arc thickens, and beside the dial a small drawing of what the rhythm produces (a report, a harvest, a release) draws itself when the turn completes.
- Moves: scroll-linked (pinned, ≤ 2 viewport heights) - hand angle maps 0-360° linearly to progress; the current arc goes 1.5px to 4px (.4s ease); at 360° the output drawing pen draws.
- Build: phase arcs are SVG `A` arc paths on the rim; the hand is a line rotated around the centre; phase index = floor(angle / (360 / n)). The output drawing is a separate SVG group.
- Narrow: <768px static twin: dial with all phases drawn, phase captions listed below · Reduced motion: dial with the hand at the top, all phases labelled, output drawn.
- Use when: a repeating rhythm causes an output (a monthly operating cycle, a retainer). · Avoid when: the steps happen only once.
- Effort: M · Needs lib: no · Sources: P057 https://ciechanow.ski/internal-combustion-engine/ · Verdict: ADAPT, changed: the engine mechanism became an output drawing; no gauge numbers.

### SEQ-26 Rhythm calendar
- For: cycle, time-roadmap, grouped · 2-6 activity types over 4-12 weeks
- Instead of: a cadence table ("Weekly: call. Monthly: review.")
- Reader sees: A calendar grid of weeks with a small line glyph in each day for what happens (check-in, visit, review), so the rhythm of working together shows at a glance; a legend of chips sits above.
- Moves: in-view - cells fill in calendar order, per-cell delay = 450ms / cell count; tap or hover a legend chip to ink every day of that type and dim the rest (.3s ease).
- Build: CSS grid of 7 columns; cells hold `<svg><use>` glyphs per activity type; schedules are arrays of day numbers; legend chips (buttons) toggle `data-type` on the grid. Only stated cadence, no intensity colours; rows are "Week 1", "Week 2", never dates.
- Narrow: ≤820px 4 weeks at a time, stacked one block under another (no swiping) · Reduced motion: filled.
- Use when: the reader asks "how much of my time will this take?" · Avoid when: the cadence is irregular or unknown.
- Effort: S · Needs lib: no · Sources: P160, P342 https://github.com/Financial-Times/chart-doctor/tree/main/visual-vocabulary; P081 https://ncase.me/remember/ · Verdict: ADAPT, changed: looping day cursor cut; months stack instead of swiping; relative weeks instead of dates.

### SEQ-27 Line that closes into a loop (new)
- For: sequence then cycle · 2-4 setup steps, then 3-5 repeating steps
- Instead of: a setup timeline followed by a separate "ongoing support" section
- Reader sees: One ink line runs down through the one-time setup steps, then curls into a closed loop where the repeating work lives (report, review, adjust), with the loop labelled "every month from here".
- Moves: scroll-linked - the lead-in draws with scroll like SEQ-01 and its knots light as reached; when the line enters the loop, the whole loop pen draws as one stroke (≤ 2.2s) and the loop's labels arrive at 80% of their arc.
- Build: one SVG path: a gently curved lead-in through the setup knots, then a loop of two cubic beziers whose start meets the lead-in's tangent. Knot and label positions from `getPointAtLength`; labels are HTML. Lead-in uses SEQ-01's reach formula; the loop triggers in-view at threshold .5.
- Narrow: ≤820px the lead-in becomes the left rail and the loop shrinks to 220px with its labels listed beside it · Reduced motion: lead-in and loop drawn, all knots lit.
- Use when: a project has a one-time setup and then a repeating rhythm (build, then retain). · Avoid when: nothing repeats after setup.
- Effort: M · Needs lib: no · Sources: (new) built from P013 and P023 · Verdict: NEW

### SEQ-28 Year wheel (new)
- For: cycle, time · 7-12 segments (months or seasons)
- Instead of: a 12-row table of monthly activities
- Reader sees: A circle split into twelve months like a clock face, seasons in chalky flat tints; a hand sweeps round as they scroll, and the month it points at shows one line of what happens then, with "Jun · 6 / 12".
- Moves: scroll-linked (pinned, ≤ 3 viewport heights) - the hand angle maps linearly to progress; the ring behind the hand draws solid while the ring ahead stays a construction line; the month line arrives (12px) at each month.
- Build: 30° wedges as SVG arc paths; seasonal tints are static fills; the hand is a line rotated around the centre; month index = floor(progress × 12). Skip months with nothing to say (the hand passes them without a caption) so every stop carries content.
- Narrow: <768px static twin: the wheel drawn once with month initials, then a stacked list of only the months that have content · Reduced motion: wheel solid, months with content listed beside it.
- Use when: the work follows the year (crop seasons, academic terms, a festival calendar) and repeats next year. · Avoid when: the months are not set by the season or term (that becomes a dated plan).
- Effort: M · Needs lib: no · Sources: (new) extends P057 and P160 · Verdict: NEW

### SEQ-29 Back-and-forth handover loop (new)
- For: cycle, linked, opposed · 2 parties, 2-4 passes
- Instead of: "we'll work collaboratively with your team"
- Reader sees: Two line-drawn figures face each other (our team, your team); an arched line goes over from one to the other and the next arch comes back, each pass labelled (we draft, you review, we adjust, you approve), and the arches get lower with each pass as the work settles.
- Moves: scroll-linked step index - each arch pen draws in the direction of the handover; the receiving figure gets a marker disc behind it (.4s ease); earlier arches drop to 40% ink.
- Build: two figure groups at left and right in one SVG; arches are quadratic paths with height h × .75^i so the loop visibly tightens; labels are HTML at each arch's midpoint. Pin ≤ 2 viewport heights.
- Narrow: ≤820px figures top and bottom with side-bulging arches; <768px static drawing plus a numbered list of passes · Reduced motion: all arches drawn, the last in the accent.
- Use when: the process is a review loop between two sides and the reader should see their part. · Avoid when: one side does all the work (use SEQ-01).
- Effort: S · Needs lib: no · Sources: (new) uses the TVS self-drawing line and figure idioms from P013 and P026 · Verdict: NEW

---

## Time and roadmap

### SEQ-30 ★ Growing drawing across time bands
- For: time-roadmap, before-after · 1 subject, 3-5 time bands
- Instead of: a phased roadmap table
- Reader sees: One line drawing stays in the middle (a field, a building, a classroom, a ledger) and grows as they scroll; on the left the time band ("First month", "Months 2-3", "Year 1"), on the right one plain fact for that band, with "2 / 4".
- Moves: scroll-linked (pinned) - at each band threshold the new parts pen draw on top of the previous state and nothing else moves; band label and fact arrive (12px, .6s).
- Build: section ≤ 3 viewport heights with a sticky 100vh stage; p = clamp(-rect.top / (rect.height - innerHeight), 0, 1); band = floor(p × n). States are stacked SVG groups in one viewBox so lines stay in register; each band adds a group and never replaces one.
- Narrow: <768px static twin: each band as a still with its label and fact, stacked · Reduced motion: final drawing, with the bands as a column of stills.
- Use when: the argument is "this is how it changes over time" and there is one object to watch. · Avoid when: there is no single object that changes, or the bands need calendar dates.
- Effort: M · Needs lib: no · Sources: P416 http://plastic-ocean.com · Verdict: ADAPT, changed: crossfades replaced by additive pen drawing; bands × 100vh capped at 3 screens; relative time labels only.

### SEQ-31 ★ Workstream metro map
- For: time-roadmap, grouped, linked · 2-5 streams, 4-8 milestones each
- Instead of: a Gantt chart
- Reader sees: A subway map where each line is a workstream (Build, Train, Launch), each station a milestone, and capsule interchanges mark where streams meet; the lines draw station to station and the station names ink in as their line arrives.
- Moves: scroll-linked - lines draw with dashoffset as the map passes through the viewport (SEQ-01's reach formula), one stream at a time; the stream being explained is the accent, the rest ink; station names reveal once.
- Build: paths with only 0°, 45° and 90° segments; stations are paper circles with an ink ring; interchanges are capsules spanning lines. Streams differ by dash pattern and a chalky flat tint behind the line, never by a rainbow of colours. Even spacing; relative phases only.
- Narrow: ≤820px rotated so lines run downward; <768px static map with the stream list under it · Reduced motion: full map drawn.
- Use when: several parallel streams share milestones. · Avoid when: there is one stream (use SEQ-32).
- Effort: M · Needs lib: no · Sources: P151 https://datavizproject.com/data-type/transit-map/ · Verdict: ADAPT, changed: one colour per line replaced by dash patterns plus a single accent for the stream being explained; no dates.

### SEQ-32 Level map roadmap
- For: time-roadmap, sequential · 4-10 milestones
- Instead of: a vertical timeline with dots
- Reader sees: A hand-drawn map with numbered stops like levels in a game; the path between stops draws as they reach each one, each stop has a one-line goal, and a small counter reads "Stop 3 / 8".
- Moves: in-view per stop - the segment to that stop pen draws; the stop marker fills with the accent (.4s ease); its label arrives (12px). The path ahead stays a construction line.
- Build: SVG map with stop circles and one path; segments via cumulative lengths (`stroke-dasharray` plus a per-segment offset); stops observed by an IntersectionObserver against an HTML list twin beside the map. Terrain (hills, a river) is static line art and never animates.
- Narrow: ≤820px the map becomes a vertical winding path with stops stacked · Reduced motion: map drawn, all stops marked.
- Use when: programme phases each have one goal. · Avoid when: milestones aren't sequential, or the map metaphor would need explaining.
- Effort: M · Needs lib: no · Sources: P456 https://pigeonsmission.com, P087 https://pudding.cool/2026/03/ivf/ · Verdict: ADAPT, changed: one-time alarm ring cut; P087's isometric climbing figure reduced to the n / N counter.

### SEQ-33 Now, next, later horizon (new)
- For: time-roadmap, ranked by certainty · 3 horizons, 2-4 items each
- Instead of: a dated roadmap, or three equal columns
- Reader sees: A line-drawn road runs from the foreground to a horizon; "Now" sits large and fully inked in front, "Next" smaller in the middle distance, and "Later" small and still in faint dashed construction lines at the horizon, so certainty shrinks with distance.
- Moves: scroll-linked step index (pinned, ≤ 2 viewport heights, "1 / 3") - each horizon's items pen draw when its step arrives (Now in ink, Next at 70% ink, Later stays dashed); labels arrive once.
- Build: one SVG with a perspective road (two lines converging to a vanishing point) and three groups scaled 1, .7 and .45; item labels are HTML placed by viewBox percentages at 100%, 85% and 72% font size.
- Narrow: <768px three stacked bands, Now first, each paler than the last, with Later's drawing dashed · Reduced motion: road and all three horizons drawn.
- Use when: the plan is honest about certainty and there are no firm dates. · Avoid when: the Later items are actually committed.
- Effort: M · Needs lib: no · Sources: (new) replaces the "Now / Next / Later columns" fallback named in P206 · Verdict: NEW

### SEQ-34 Ownership line: ours, shared, yours (new)
- For: time-roadmap, linked · 3-5 phases with a handover
- Instead of: a "transition plan" paragraph
- Reader sees: One line runs through the phases (build, train, run together, hand over); a small line-drawn figure for our team walks it first, the client's figure joins halfway, and by the end only theirs holds the line, while the label beside it changes from "we do" to "together" to "you do".
- Moves: scroll-linked - the line draws with scroll; at each phase boundary one change only: a figure arrives or leaves (.6s ease-out) or the label swaps.
- Build: SVG path with phase ticks; figures are small SVG groups placed at `getPointAtLength` of each phase's midpoint; the ownership label is HTML pinned beside the line. Phase boundaries come from the brief.
- Narrow: ≤820px the line runs down the left with figures beside each phase; <768px static, figures shown at each phase · Reduced motion: line drawn, all figures in place.
- Use when: responsibility shifts to the client and they need to see when they take over. · Avoid when: there is no handover (use SEQ-32).
- Effort: S · Needs lib: no · Sources: (new) uses the TVS self-drawing line and figure idioms from P013 and P026 · Verdict: NEW

### SEQ-35 Round-by-round rows
- For: time-roadmap, sequence · 5-12 rounds
- Instead of: a week-by-week bullet plan
- Reader sees: The whole plan as stacked rows, one per round ("Week 1", "Week 2"), each row a small picture of the deliverable with done parts filled and pending parts dashed, and on the right the one thing that changed that round.
- Moves: in-view - rows arrive top to bottom as they enter (12px, 80ms stagger capped at 450ms); in each row the part that just got done is the accent, earlier parts ink.
- Build: each row is a snapshot SVG in the same viewBox (filled shapes for done parts, construction-line outlines for pending ones) so the eye compares straight down. Left label gives the relative week; right label the one change.
- Narrow: same, thinner cells; the right label drops under the row · Reduced motion: all rows shown.
- Use when: the reader needs the whole plan in one glance. · Avoid when: the rounds are not comparable.
- Effort: S · Needs lib: no · Sources: P101 https://bost.ocks.org/mike/algorithms/ · Verdict: ADAPT, changed: pending parts drawn as construction lines; a single accent marks each round's change.

### SEQ-36 Workstream spans
- For: time-roadmap, grouped · 3-8 workstreams over 3-5 phases
- Instead of: a dated Gantt chart
- Reader sees: Thick chalky lines float over a phase ruler (Set up, Run, Hand over), overlapping where work runs in parallel, with small hand-drawn diamonds for named milestones (Pilot, Launch, Review), so the shape of the work shows instead of a list of dates.
- Moves: in-view - the ruler pen draws first; then each span pen draws from its start edge in order of start; diamonds arrive (.6s ease-out) as their span passes them.
- Build: CSS grid with one column per phase or relative week; spans placed with `grid-column: start / end`, each an SVG line (or a block with `transform-origin:left` scaled on the pen timing). Diamonds are 10px squares rotated 45°. Caption "lengths show phase, not dates" when durations aren't firm.
- Narrow: ≤820px time runs downward and spans become vertical capsules in 2-3 tracks · Reduced motion: static.
- Use when: parallel work and overlaps matter. · Avoid when: steps run strictly one after another (use SEQ-32), or someone will read it as a promise of dates.
- Effort: S · Needs lib: no · Sources: P127 https://datavizproject.com/data-type/span-chart/, P329 https://github.com/Financial-Times/chart-doctor/tree/main/visual-vocabulary, P206 https://linear.app · Verdict: ADAPT, changed: month columns and "today" line dropped (no dated plans); bars draw like pen strokes; one colour plus tints.

### SEQ-37 Week ruler with a now line
- For: time-roadmap, sequence · 6-20 milestones over relative weeks
- Instead of: a long dated timeline
- Reader sees: A ruler of weeks runs down the left edge; a thin "now" line holds mid-screen, and each milestone card brightens to full ink as its week passes the line, so scrolling literally moves time.
- Moves: scroll-linked - cards within one card-height of the line go from .5 to 1 opacity, linear with distance; nothing scales; card text reveals once.
- Build: section height = weeks × 140px (20 weeks at most); cards absolutely placed at their week; the now line is `position:sticky; top:50vh` inside the section, not fixed to the page. Ruler ticks are static SVG.
- Narrow: ≤820px the ruler shrinks to week numbers and cards go full width · Reduced motion: plain list of weeks and milestones at full ink.
- Use when: the pacing of a long programme matters. · Avoid when: under 6 milestones (use SEQ-32), or the weeks are guesses.
- Effort: M · Needs lib: no · Sources: P079 https://vallandingham.me/scroll_talk/ · Verdict: ADAPT, changed: card scaling cut; now line made sticky inside the section; relative weeks instead of dates.

### SEQ-38 Day on a sun arc
- For: time-roadmap, people-roles · 3-5 moments in one day
- Instead of: a "here's what a typical day looks like" paragraph
- Reader sees: A line-drawn scene of the person's workplace under a dashed arc from 06:00 to 18:00; a small sun travels the arc as they scroll, and at each named hour the scene changes one thing while a one-sentence card says what happens for them then.
- Moves: scroll-linked (pinned, ≤ 2.5 viewport heights) - sun position = `getPointAtLength(p × L)`, linear; the arc behind the sun draws solid; at each hour the scene's one change pen draws and the card arrives (12px).
- Build: sticky 100vh stage; the arc is one SVG path with hour ticks, each hour at (hour - 6) / 12 of the arc length; scene changes are stacked SVG groups; cards are HTML under the scene.
- Narrow: <768px a vertical hairline down the left with times stacked and one small still per moment · Reduced motion: sun parked at the last hour, all moments shown.
- Use when: showing what changes in an ordinary working day after the change (for a farmer, a student, a manager). · Avoid when: the change spans weeks or months (use SEQ-30).
- Effort: M · Needs lib: no · Sources: P181 https://claude.com/product/overview, P443 https://aicommon.creamu.co.jp · Verdict: ADAPT, changed: the horizontal rail became an arc over a pinned scene; one change per hour.

### SEQ-39 Proof line with milestone pins
- For: time-roadmap, quantity-scale, proof-trust · 1 line, 2-4 pins
- Instead of: "results so far" bullet stats
- Reader sees: One rising hand-drawn line draws across from left to right, and pins hang from it on dashed ties at the moments that mattered ("pilot done, 230 to 315").
- Moves: in-view - the line pen draws (≤ 2.2s); each pin arrives (8px) as the pen passes its x.
- Build: SVG path from real data points; pins are HTML on dashed ties: `width:2px; height:45px; background:linear-gradient(currentColor 0 13px, #0000 13px 33px, currentColor 33px 45px)`. Pin delay = draw duration × (pin x / width).
- Narrow: ≤820px 2 pins, shorter ties · Reduced motion: line drawn, pins visible.
- Use when: showing real progress over time, such as the results of a pilot. · Avoid when: the data is noisy or invented (draw the trend honestly).
- Effort: S · Needs lib: no · Sources: P436 https://www.wafer.ai · Verdict: ADAPT, changed: the soft-edged 3s mask sweep replaced by the house pen draw.

### SEQ-40 Honest outcome fan
- For: time-roadmap, proof-trust · 1 path, 2-3 bands
- Instead of: a single confident growth projection
- Reader sees: One path forward widens into soft chalky bands labelled "likely", "possible" and "if everything goes right", with no numbers on the axis.
- Moves: in-view - the centre path pen draws; at 80% of it the bands fade in from the centre outward (.6s ease-out, 100ms apart).
- Build: three closed paths (upper and lower bezier edges) as flat tints at .25, .15 and .08 around a 2px centre path; band names with one example outcome each as HTML labels. No y-axis values. Placed after SEQ-39, the past runs solid into the fan.
- Narrow: same, labels below · Reduced motion: static.
- Use when: outcomes depend on things outside your control and you want to be believed. · Avoid when: the reader needs a commitment, not a range.
- Effort: S · Needs lib: no · Sources: P165 https://github.com/Financial-Times/chart-doctor/tree/main/visual-vocabulary · Verdict: ADAPT, changed: the "bloom" became a timed fade after the pen line; tints flat.

### SEQ-41 Shipped log
- For: time-roadmap, proof-trust · 4-8 entries
- Instead of: "we have a track record" claims
- Reader sees: A short dated list of things already delivered, newest first, one sentence each, so the promises ahead feel backed by momentum.
- Moves: in-view - entries arrive once (12px, 80ms stagger); the newest entry's key phrase gets the marker sweep; no pulsing dot.
- Build: vertical list with the date in a 96px monospace column and hairline rules between entries. Dates are real past deliveries (records, not a plan).
- Narrow: ≤820px the date sits above each entry · Reduced motion: static, marker shown.
- Use when: proposing an ongoing relationship and you can show recent real deliveries. · Avoid when: the dates are old enough to look stale.
- Effort: S · Needs lib: no · Sources: P205 https://linear.app · Verdict: ADAPT, changed: endless pulse dot replaced by one marker sweep; "See all" link dropped.

---
