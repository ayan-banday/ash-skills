# Amounts and ranks: quantity-scale, ranked-list

Pattern library family for `pitch-site-udyaan`. 29 entries (6 starred), curated from slice4 (31 raw entries in this family, plus P075 and P341 moved in from people-proof-ask).
Verdicts: 4 KEEP, 19 ADAPT, 6 NEW, 3 CUT (listed at the end).
KEEP means the device ships as found, with at most timing values brought to the house rule. ADAPT means the trigger, motion, content rule or layout changed.

**The number rule.** Never invent a number. Proposals usually carry 0-3 real figures, so every entry below says, in its Build line under "Figures:", what it needs and what to do with fewer. Count the sourced figures in the brief before you pick.

**Shorthand used in every entry (house motion values):**
- **pen draw**: stroke-dashoffset from length to 0, duration = length / 600 px/s, clamped 0.6-2.2s, next stroke starts at 80-85% of the previous one, ease cubic-bezier(.45,.05,.35,1).
- **arrives**: opacity 0 to 1 plus a rise of 12px (16px at most), 0.6-1.0s, cubic-bezier(.22,1,.36,1). Staggers 60-110ms, total capped at 450ms. Nothing enters from the side.
- **reveals once**: text arrives the first time it enters the view and always finishes.
- **scroll-linked**: linear, tied 1:1 to progress. Drawings and gauges may follow scroll; text never does.
- **construction line**: the faint dashed version of a line (about 25% ink, dash "2 6"), drawn solid when its caption explains it.
- **pinned**: a sticky stage whose section is 3 viewport heights or less, with an `n / N` counter, and a stacked static twin below 768px.
- **accent**: the one colour that points (the reader's bar, the client's dot, the gain). Everything else is ink, paper and chalky flat tints.
- **no count-ups**: numbers arrive finished. A number moves only when the moving is the meaning (a scroll gauge, a running total).

---

## Family picker

Pick by how many sourced figures you have, then by shape and relation. Starred first. If unsure: 1-3 figures go to AMT-02, a count goes to AMT-04, ranks with no numbers go to AMT-20.

**Figures check (an index by how many real figures the brief gives you; the rules below pick)**
- 0 figures: AMT-01 ★ (qualitative form), AMT-07, AMT-08; ranks only: AMT-20 ★, AMT-27, AMT-28, AMT-29. Scale with no numbers: STR-26 Pullback (structure-links).
- 1-3 figures: AMT-02 ★, AMT-01 ★, AMT-03 ★, AMT-04 ★, AMT-05, AMT-09, AMT-11, AMT-12; as proof cards: PPL-18 ★.
- 2 bounds of an estimate: AMT-06.
- A full series or dataset: AMT-15 to AMT-19, AMT-22, AMT-23.

**Quantity and scale**
- 1 abstract size or duration the reader cannot feel: AMT-01 ★, AMT-05.
- 1-3 sourced figures as headline proof, equal: AMT-02 ★, PPL-18 ★.
- 1 count of things already done, up to 40: AMT-03 ★, AMT-04 ★.
- 1-6 counts of people or things compared, equal or opposed: AMT-04 ★, AMT-09. Shares of a whole: STR-33 Unit grid (structure-links).
- 2 values with a 10x or bigger gap, opposed: AMT-09, CHG-18 (change-choice, when one value is a benchmark).
- An estimate that is honestly a range: AMT-06, PPL-26. Over time with no numbers: SEQ-40 (order-time).
- Scope or reach with no numbers, 3-5 worded sizes, ranked: AMT-07, STR-26 (structure-links).
- Effort that becomes simpler, no numbers, opposed (before, after): AMT-08, CHG-09 (change-choice).
- One wait or wasted gap: AMT-11, AMT-10.
- Many items placed along one dimension, 3-12 markers, sequential: AMT-10, AMT-23.
- A price, 1-2 figures: AMT-12, AMT-13.
- 3-10 line items that add up or offset, grouped: AMT-13, AMT-14.
- 3-8 contributions that explain one result, linked: AMT-14, AMT-13.
- A trend mentioned inside a sentence, 6-24 points: AMT-15, AMT-16.
- A trend that carries the argument, 6-30 points: AMT-16, AMT-17.
- Growth where the start looks like nothing, 8-40 points: AMT-17, AMT-16.
- A flow that loses people at each stage, 4-10 sourced waypoints, sequential: AMT-18, AMT-09.
- 30-1000 real records, spread or consistency: AMT-19, PPL-12.
- One real story standing for many: PPL-11.

**Ranked lists**
- 2-4 options with one recommended: AMT-27, PPL-29. Chosen by tests: CHG-38 (change-choice).
- 3-7 items, ranks only, each with a reason: AMT-28, AMT-25. Ranked levels built from the ground: STR-17 (structure-links).
- 4-10 items reshuffled from now to after, opposed: AMT-20 ★, AMT-24.
- 3-7 items whose order changes across 3-6 phases, sequential: AMT-24, AMT-25.
- 4-10 items with a sourced value each: AMT-22, AMT-23.
- A few that matter plus many that prove breadth, 3 + 5-80: AMT-21 ★, AMT-29.
- 8-20 items where only tiers are defensible, grouped: AMT-29, AMT-28 (if you can cut it to 7).
- Where the client stands among 5-100, ranked on one sourced value: AMT-23, AMT-22.
- 5-9 items read one at a time in a set order: AMT-25, AMT-28.
- Paragraphs within a section, ranked by importance: AMT-26.

---

## Quantity and scale: few or no numbers

### AMT-01 ★ Familiar-object scale stamp
- For: quantity-scale, definitions-jargon · 1-3 sizes or durations against 1 everyday object
- Instead of: a number with a unit nobody can feel ("0.4 mm", "38 hours")
- Reader sees: An everyday object drawn in outline (a credit card, an A4 sheet, a cup of tea, a cricket pitch) beside the subject at the same true scale, so the size is felt rather than read.
- Moves: in-view - pen draw: the familiar outline first (0.6-1.2s by length), then the subject beside it, starting at 80-85% of the first.
- Build: one SVG with both shapes at one shared scale (credit card 85.6 × 53.98 mm, A4 210 × 297 mm); 1.8-2.4px strokes with the wobble filter (static); a mono caption names both sizes. Figures: needs 1 sourced size or duration; with none, use the qualitative form ("about one cup of tea", "a stack of forms this high") only where the brief supports it.
- Narrow: same, scales with width · Reduced motion: both drawn.
- Use when: an abstract amount needs a physical anchor. · Avoid when: no everyday object fits honestly, or the two differ by more than about 50x (use AMT-09 or AMT-10).
- Effort: S · Needs lib: no · Sources: P055 https://ciechanow.ski/mechanical-watch/ · Verdict: KEEP

### AMT-02 ★ Key figures with drawn notes
- For: quantity-scale, proof-trust · 1-3 sourced figures, equal
- Instead of: a row of giant count-up numbers
- Reader sees: One to three big serif numbers, each with a short handwritten note and a pen-drawn arrow from the number to the note saying what changed and why it matters, plus a muted source line.
- Moves: in-view - the number arrives finished (rise 12px, 0.7s cubic-bezier(.22,1,.36,1)); its arrow pen draws (0.6-0.9s); the note arrives (opacity, 0.6s). The next figure starts at 80-85% of the previous arrow.
- Build: number serif clamp(4rem,10vw,8rem), `tabular-nums`, `line-height:.9`, formatted with `Intl.NumberFormat('en-IN')` so lakh and crore group correctly; arrows hand-drawn SVG paths; notes in the hand face (Caveat 500), 12 words at most; source line mono 11px. Figures: built for 1-3; with one, centre it alone with a longer note; with none, use AMT-07 or AMT-08. Cap at 3 even when more exist (the rest go in AMT-22).
- Narrow: below 820px stacked, numerals 18vw · Reduced motion: final numbers, arrows drawn, notes shown.
- Use when: proving impact at the start or the close with the few real figures you have. · Avoid when: the numbers are small or unflattering without context, or unsourced.
- Effort: S · Needs lib: no · Sources: P257 https://vicosight.com/news/5-design-trends-for-annual-reports, P341 https://developer.mozilla.org/en-US/docs/Web/CSS/font-variant-numeric · Verdict: ADAPT, changed: merged with the number wall; count-ups cut; capped at 3; arrows pen drawn.

### AMT-03 ★ Hand-drawn tally
- For: quantity-scale, proof-trust · 1 sourced count, 1-40 marks
- Instead of: "We have already held 23 sessions" in a sentence
- Reader sees: Chalky tally marks, four upright strokes and a slash per gate, counting things already done (meetings held, farms visited), with a label under each row naming what was counted.
- Moves: in-view - pen draw by gate: each gate of five is one path drawn the way a hand would (uprights, then the slash), 0.6-0.8s per gate, next gate at 80-85%; tallies over 4 gates follow scroll instead (drawn fraction tied linearly to progress) so nobody waits. No overshoot on the slash.
- Build: each gate one `<path>` with five subpaths and a slight seeded bezier wobble (control points ±1.5px); dashoffset on a multi-subpath path draws them in order; chalk stroke 2.4px with the rice-powder filter on the section tint. Figures: needs exactly 1 sourced, past count; never tally a promise.
- Narrow: same, wraps by gate · Reduced motion: marks shown drawn.
- Use when: proof of work already done, at a small human scale. · Avoid when: the count passes about 40 (use AMT-04 with 1 figure = 5 or 10).
- Effort: S · Needs lib: no · Sources: P109 https://datavizproject.com/data-type/tally-chart/ · Verdict: ADAPT, changed: 180ms per stroke became pen timing per gate; slash overshoot cut; long tallies follow scroll.

### AMT-04 ★ Isotype counting rows
- For: quantity-scale, comparison · 1-6 rows, 3-60 figures per row
- Instead of: a bar chart or a big number for counts of people or things
- Reader sees: Rows of identical small line figures (houses, trainers, batches), one per real thing or one per stated unit ("1 figure = 10 farmers"), so "12" is twelve houses they can count; more means more figures, never a bigger figure.
- Moves: in-view - figures arrive in groups of ten (opacity plus 8px rise, 0.6s cubic-bezier(.22,1,.36,1)), groups 80ms apart capped at 450ms; the row that carries the point tints to the accent last.
- Build: one `<symbol id="u-house">` in a hidden SVG; rows are flex or grid containers of `<svg><use href="#u-house"/></svg>` at 24-36px; a partial unit uses a `clipPath` rect sized to the fraction; each row label states the key; no perspective. Figures: needs 1-3 sourced counts; without a count, show distinct icons as a roster and drop the counting claim.
- Narrow: below 820px wrap at 10 per line so rows read as tens; icons stay 24px or larger · Reduced motion: all figures shown.
- Use when: a real count is the point and the reader should feel its size. · Avoid when: counts are estimates, differ by more than about 100x, or decimals matter (for shares of a whole use STR-33).
- Effort: S · Needs lib: no · Sources: P107 https://en.wikipedia.org/wiki/Isotype_(picture_language), P233 (same source), P321 http://datavizcatalogue.com/methods/pictogram.html · Verdict: ADAPT, changed: three Isotype entries merged; per-icon 25-40ms staggers became groups of ten capped at 450ms.

### AMT-05 Same amount, said three ways
- For: quantity-scale · 1 sourced figure
- Instead of: a unit switcher the reader never taps
- Reader sees: One number pinned mid-screen; as captions scroll past its unit changes once per caption, "38 hours a month", then "almost five working days", then "one person's whole first week", each a fair restatement of the same figure.
- Moves: scroll-linked (pinned) - one stage, one knob: each caption swaps the unit; the old value fades out and the new one arrives (rise 8px, 0.6s cubic-bezier(.22,1,.36,1)); counter "1 / 3"; pin 2 viewport heights at most.
- Build: sticky stage; a conversion map in JS (`{hours:1, workdays:1/8}`) so every restatement is computed from the one sourced value, never typed by hand; one IntersectionObserver on the captions sets the index; the text twin lists all three. Figures: needs exactly 1 sourced figure and conversions the brief supports (an 8-hour day, a 6-day week).
- Narrow: below 768px a static stack of the three restatements · Reduced motion: all three shown as a list.
- Use when: a raw number feels abstract and one restatement makes it land (put the most vivid last). · Avoid when: the conversions would be silly or need assumptions the brief does not state.
- Effort: S · Needs lib: no · Sources: P076 https://joshworth.com/dev/pixelspace/pixelspace_solarsystem.html · Verdict: ADAPT, changed: tap chips became scroll steps, so nothing depends on tapping.

### AMT-06 Estimate drawn as a band (new)
- For: quantity-scale, proof-trust · 1 estimate given as a low and a high
- Instead of: a single precise-looking forecast ("47 new students")
- Reader sees: A short ruler with a soft chalky band between the low and the high estimate, both ends labelled, a muted line "our estimate, not a promise" and one line on what pushes it toward the high end.
- Moves: in-view - the ruler pen draws (0.6s); the band widens from its midpoint to both ends (0.8s cubic-bezier(.22,1,.36,1)); the end labels arrive last. Once.
- Build: SVG ruler with ticks only at the two bounds; the band is a `rect` in the section's chalky tint with a hand-drawn edge (wobble filter, static); labels serif with `tabular-nums`; pair with the PPL-26 caveat for method. Figures: needs the 2 sourced bounds; with 1 figure use AMT-02; never invent a range around a single number.
- Narrow: same, full width · Reduced motion: band shown.
- Use when: the honest answer is a range (enrolment, savings, time to first result). · Avoid when: the bounds are guesses, or the range is so wide it says nothing.
- Effort: S · Needs lib: no · Sources: new; built from P094 (https://pudding.cool/2017/03/film-dialogue/) and the outcome fan idea in SEQ-40 · Verdict: NEW

### AMT-07 Worded size ruler (new)
- For: quantity-scale, ranked-list · 0 figures, 3-5 sizes named in the brief
- Instead of: "this can scale across the organisation" with no picture
- Reader sees: One ruler drawn by pen with marks named only in the brief's words ("one welder", "the paint shop", "the Hosur plant", "every plant"); a solid accent line runs from the start to where this proposal reaches, and a faint dashed extension runs on to where it could go, labelled "if the pilot works".
- Moves: in-view - the ruler and its marks pen draw (one stroke, up to 2.2s); then the accent segment pen draws to the "now" mark; the dashed extension and its label arrive last (opacity, 0.6s). Once.
- Build: one SVG line with tick subpaths at even spacing (the spacing is order, not amount, and the caption says so); mark labels serif 18px, the "now" mark in the accent with the TVS hand-drawn ring around its label; the extension is a construction line (`stroke-dasharray: 2 6`, 25% ink). Figures: needs none; if the brief gives a count for a mark, add it to that label with its source.
- Narrow: below 820px the ruler runs vertically, marks reading top to bottom · Reduced motion: drawn, ringed, extension shown.
- Use when: the scale of the opportunity matters but the brief has no reliable numbers. · Avoid when: the marks would imply sizes the client has not confirmed. For a camera pullback version, use STR-26.
- Effort: S · Needs lib: no · Code: TVS harvest · Sources: new; built from the TVS hand-drawn ring (harvest section 2.14) and the worded scales in CHG-11 · Verdict: NEW

### AMT-08 The pile and the page (new)
- For: quantity-scale, before-after · 0 figures, 1 before and 1 after
- Instead of: "saves a lot of time", or an invented percentage
- Reader sees: On the left, a hand-drawn pile of the real things the work takes today (forms, registers, phone calls, trips); on the right, the single thing it becomes (one screen, one page); one caption, no number.
- Moves: in-view - the pile pen draws item by item from the bottom up (each 0.6s, next at 80-85%, the whole pile done within 3s); then the single page pen draws (0.8s); then the caption arrives.
- Build: one SVG; pile items are 4-8 reused symbols (sheet, register, phone, bus) stacked with slight build-time rotations (±4deg); every drawn item is a real input named in the brief; caption serif 22px with one marker-swept phrase. Figures: needs none; if one is sourced ("from 6 registers to 1 screen"), write it in the caption and draw exactly that many items.
- Narrow: below 820px pile above, page below, a short drawn arrow between · Reduced motion: both drawn.
- Use when: the gain is simplification and you have no measured saving. · Avoid when: the after is not really one thing, or the story is a process change (use CHG-09 Paper vs screen).
- Effort: S · Needs lib: no · Sources: new; built from the TVS paper vs screen device (CHG-09) and P055 · Verdict: NEW

### AMT-09 Scale shock bar
- For: quantity-scale, comparison · 2 sourced values, ratio 10x or more
- Instead of: "20x more" in a sentence
- Reader sees: A short stub labelled "usual" and a second line so long it runs the full width and folds back like a ribbon, with the multiple waiting at its end.
- Moves: in-view - the long bar pen draws (dashoffset at 600 px/s, capped at 2.2s); the multiple arrives at its end as the line lands (rise 12px, 0.6s cubic-bezier(.22,1,.36,1)). No counter.
- Build: SVG where the long line is literally N times the stub (stroke-width 14-18px, round caps); when N × stub exceeds the width, fold it into rows (a zigzag ribbon) rather than scrolling sideways. Figures: needs 2 sourced values; with one, use AMT-01 or AMT-02.
- Narrow: below 820px fold into more rows · Reduced motion: final bar with the number.
- Use when: one dramatic multiple (10x, 20x, 100x) is the argument. · Avoid when: the gap is under about 3x (it looks petty) or either value is estimated. Against a published benchmark, use CHG-18.
- Effort: S · Needs lib: no · Sources: P195 https://mercury.com · Verdict: ADAPT, changed: cubic-bezier(.16,1,.3,1) became the pen curve; counter cut; overflow folds instead of scrolling sideways.

### AMT-10 Scroll ruler: the distance you scroll is the amount
- For: quantity-scale, sequence · 1 sourced range, 3-12 markers on one axis
- Instead of: a tall bar chart of depth, time or distance
- Reader sees: A ruler running down the page with a reading line; a number beside it counts exactly as fast as they scroll (metres, years, kilometres), and items appear at their true place on the ruler.
- Moves: scroll-linked - value = from + (to - from) × progress between two markers, linear, rounded to meaningful steps; the tick under the reading line lights; the section may shift between two chalky tints at most, never to near-black.
- Build: two invisible marker elements; a rAF-throttled scroll handler computes the viewport centre's progress between them; `textContent = Math.round(v/step)*step` with `toLocaleString('en-IN')`; items absolutely placed at `top = value × pxPerUnit`; section capped at 3 viewport heights (compress the scale and say so). CSS-only option: `@property --n {syntax:"<integer>"}` with `animation-timeline: view()` inside `@supports`. Figures: needs the 2 sourced endpoints and every marker's position; with none, do not use.
- Narrow: same, shorter · Reduced motion: final value with the range ("0 to 10,000 m") and all items placed.
- Use when: scale along one dimension is the point (how deep, how long, how far). · Avoid when: the number must be read exactly at every moment, or the items do not share one scale.
- Effort: S · Needs lib: no · Sources: P078 https://neal.fun/deep-sea/, P417 http://plastic-ocean.com, https://piergorelli.com · Verdict: ADAPT, changed: merged; capped at 3 viewport heights; the slide to near-black cut.

### AMT-11 The long wait
- For: quantity-scale, atmosphere · 1 sourced gap (days, weeks, steps)
- Instead of: "approvals currently take 14 days"
- Reader sees: A deliberately quiet stretch of page with almost nothing in it, a small fixed counter ticking up ("day 3 of 14, waiting") and two or three dry captions placed in the emptiness; a skip link sits at the top.
- Moves: scroll-linked - the counter tracks scroll progress linearly; captions reveal once.
- Build: section height in proportion to the gap, capped at 3 viewport heights; the counter is `position: sticky` inside the section so it leaves with it; captions at fixed distances; "skip to the other side" link at the top. Once per page. Figures: needs exactly 1 sourced gap; with none, do not use.
- Narrow: below 768px 2 screens · Reduced motion: one screen with the number and the skip link.
- Use when: the waste or the wait is the whole message. · Avoid when: used more than once per page.
- Effort: S · Needs lib: no · Sources: P077 https://joshworth.com/dev/pixelspace/pixelspace_solarsystem.html · Verdict: ADAPT, changed: 6 screens capped to 3 viewport heights.

### AMT-12 Price as a formula
- For: quantity-scale, big-idea · 1-2 headline prices
- Instead of: a pricing table of tiers and ticks
- Reader sees: One or two very large numbers, each with a one-line condition underneath, and every add-on written as a plain sentence with an "Included" tag where nothing extra is charged.
- Moves: in-view - the numbers arrive (rise 12px, 0.7s cubic-bezier(.22,1,.36,1)); nothing else moves.
- Build: a `<figure>` per price, numerals 96-120px, weight 500, tracking -0.03em; condition line 15px muted; add-ons as a `<dl>` with an "Included" pill; format with `Intl.NumberFormat('en-IN', {style:'currency', currency:'INR'})`. Figures: needs the real agreed price; with no price yet, put "Priced after the site visit" in the same slot.
- Narrow: below 820px numbers stack · Reduced motion: static.
- Use when: the pricing is simple and you want it to feel honest. · Avoid when: there are several tiers with many differences.
- Effort: S · Needs lib: no · Sources: P209 https://stripe.com/pricing · Verdict: KEEP

---

## Quantity and scale: many numbers

### AMT-13 Receipt that adds up
- For: quantity-scale, part-whole · 3-10 line items, additive or net
- Instead of: a bulleted list of deliverables, or a price with no breakdown
- Reader sees: A till receipt printing line by line, each line a deliverable with its value or "Included"; offsets (subsidies, credits, savings) subtract below a rule; the total sits under a double rule.
- Moves: in-view - lines print top to bottom (`clip-path: inset(0 0 100% 0)` to `inset(0)`, 0.6s cubic-bezier(.22,1,.36,1)), 80ms apart capped at 450ms; the running total line updates as each line lands and the final total arrives last.
- Build: `<ol>` of rows with `data-amount`; JS sums only the data present; monospace, right-aligned `tabular-nums`, dashed separators, perforated edge from a `radial-gradient` mask; offsets in muted ink with a minus sign; final row a 1px hairline plus a double rule. Figures: works with real amounts only; with no prices, print the deliverables with "Included" and end on "All of this, for one agreed fee".
- Narrow: same (receipts are narrow) · Reduced motion: fully printed, total shown.
- Use when: value stacking ("all of this, included") or net cost after offsets. · Avoid when: you would show prices the client has not agreed to see, or offsets are uncertain (footnote their conditions).
- Effort: S · Needs lib: no · Sources: P210 https://stripe.com/atlas, P333 https://css-tricks.com/animating-number-counters/ · Verdict: ADAPT, changed: ledger and receipt merged; stagger capped; the counting total cut; a no-price version added.

### AMT-14 Waterfall build-up
- For: quantity-scale, cause-effect · 3-8 sourced steps that add up
- Instead of: "here is how we get you from 12 to 40" in a sentence
- Reader sees: Bars that each start where the last one ended, stepping up to the total; costs step down in a muted tint; the total bar is the only one in the accent.
- Moves: in-view - bars arrive one by one (rise 12px, 0.6s cubic-bezier(.22,1,.36,1)), 80ms apart capped at 450ms; a faint dashed connector then pen draws across the bar tops; the total fills last.
- Build: CSS grid columns; each bar offset by its running base; labels and values printed on the bars in `tabular-nums`; connectors 1px dashed SVG. Figures: needs every step sourced; with only the start and end, use AMT-09 or AMT-02, never invent the steps.
- Narrow: below 820px the waterfall runs top to bottom · Reduced motion: static.
- Use when: several known contributions explain one result. · Avoid when: the steps are not additive or not each sourced.
- Effort: M · Needs lib: no · Sources: P340 https://github.com/Financial-Times/chart-doctor/tree/main/visual-vocabulary · Verdict: ADAPT, changed: the 16px drop became a 12px rise; stagger capped; connectors added.

### AMT-15 Sparkline inside the sentence
- For: quantity-scale, emphasis · 1-4 per page, 6-24 points each
- Instead of: a separate chart for a trend mentioned in passing
- Reader sees: A word-sized line chart inside a sentence ("calls fell every month since March" followed by a tiny line), the height of the text, with an accent dot on the latest value.
- Moves: in-view (sentence at mid-screen) - the line pen draws left to right (0.6s minimum); the end dot appears as it lands, no pop.
- Build: `<svg class="spark" viewBox="0 0 60 16" style="height:1em;width:3.75em;vertical-align:-.15em">`; normalise data to 0-16 and write a `polyline`; end dot r 1.6 in the accent; optional faint normal-range `rect`; dasharray from `getTotalLength()`. Figures: needs a real series of 6 or more points; with fewer, write the two values in words.
- Narrow: unchanged, already word-sized · Reduced motion: static line and dot.
- Use when: a claim in the copy has a trend behind it. · Avoid when: the reader needs exact values, or the trend is flat noise.
- Effort: S · Needs lib: no · Sources: P229 https://en.wikipedia.org/wiki/Sparkline · Verdict: KEEP (dot pop removed, draw set to pen timing)

### AMT-16 Chart that draws in reading order
- For: quantity-scale, time-roadmap · 1 line of 6-30 points, or 3-8 bars
- Instead of: a static chart dropped into the page
- Reader sees: A simple chart builds itself as they read: the axis first, then the line travelling left to right, the points landing, the labels last.
- Moves: scroll-linked - from when the chart's top passes 85% of the viewport to when its bottom passes 60%, linear: line `pathLength="1"` dashoffset 1 to 0; points appear as the line passes them (opacity only); bars scaleX 0 to 1 from 35% of progress. Labels reveal once from 40% and stay.
- Build: SVG chart; one scroll handler computes p for the chart and sets each element's local progress `clamp((p - start) / dur, 0, 1)`; text is excluded from scrubbing; a table twin sits in `<details>`. Figures: needs the real series; with 1-3 figures use AMT-02.
- Narrow: below 768px played once on view at pen timing instead of scrubbed · Reduced motion: finished chart.
- Use when: one trend carries the argument. · Avoid when: the reader must compare exact values (lead with the table twin).
- Effort: M · Needs lib: no · Sources: P424 https://piergorelli.com · Verdict: ADAPT, changed: scaling point pops became plain arrivals; labels reveal once instead of scrubbing.

### AMT-17 Pullback: one point, then the whole trend
- For: quantity-scale, time-roadmap · 1 series, 8-40 real points
- Instead of: a full growth chart shown at once, where the start looks like nothing
- Reader sees: The chart opens close in on the first data point; as they scroll the line draws forward and the view pulls back until the whole trend is visible.
- Moves: scroll-linked (pinned) - linear with progress: the line draws (dasharray), the camera scale goes from 2 to the full view and pans to follow the line's head; points appear as the head passes them; `n / N` counter optional.
- Build: one SVG group transformed by `translate() scale()` computed per frame from progress; head point from `getPointAtLength(p × L)`; dots get `r` set once the head's x passes theirs; no easing on scroll progress; section capped at 3 viewport heights. Figures: needs a real series; never use for 1-3 figures.
- Narrow: below 768px the finished chart with axis labels, played once on view · Reduced motion: complete chart, no camera.
- Use when: a growth story where the start looks small and the whole looks dramatic. · Avoid when: the data is noisy or flat, or the start is cherry-picked. For a non-chart pullback, use STR-26.
- Effort: M · Needs lib: no · Sources: P189 https://tympanus.net/Tutorials/ScrollGraph/ · Verdict: ADAPT, changed: expo.inOut and 0.3s smoothing removed (scroll-linked is linear); pin capped.

### AMT-18 Shrinking band
- For: quantity-scale, cause-effect · 1 flow with 4-10 sourced waypoints
- Instead of: a funnel chart of drop-off percentages
- Reader sees: One thick band following a route (enquiry to enrolment, field to market) whose width is the number of people or units, visibly thinning at each point where some are lost; a slim strip below names the cause of each loss.
- Moves: scroll-linked (pinned) - the band grows along its route linearly with progress; each waypoint's number reveals once as the band passes it.
- Build: band polygon from centreline points offset by ±width/2 along each segment's normal; revealed by a `mask` whose stroked centreline uses dashoffset tied to `--p`; width scale fixed and stated (Minard used 1 mm per 10,000 men); the cause strip shares the x positions so the eye drops straight down; one accent for the band, causes in ink; section capped at 3 viewport heights. Figures: needs a sourced count at every waypoint; with only start and end use AMT-09; with none use AMT-08.
- Narrow: below 768px the route runs down the page, static, all labels shown · Reduced motion: complete band with labels.
- Use when: telling the story of leakage or attrition and its cause. · Avoid when: there is no single flow, or the waypoints are estimates.
- Effort: L · Needs lib: no · Sources: P231 https://en.wikipedia.org/wiki/Charles_Joseph_Minard · Verdict: ADAPT, changed: second-colour return trip dropped (one accent); pin capped; static twin added.

### AMT-19 One dot per thing
- For: quantity-scale, proof-trust · 30-1000 real records
- Instead of: an average with no spread, or "hundreds of happy customers"
- Reader sees: A cloud of small dots, each a real item (an order, a farmer, a project) placed by one measure, with faint guide lines; for consistency stories, a running-average line settles into a narrow band ("after 40 projects, delivery averaged 6 weeks").
- Moves: in-view - dots arrive (opacity, scale from .4, 0.6s cubic-bezier(.22,1,.36,1)) with per-dot delay `min(i × 2ms, 450ms)`; the average line pen draws last.
- Build: SVG `<circle r="2.5">` per record from data; guide lines 0.5px; an IntersectionObserver adds `.on`; the average and its band are computed from the records, never drawn by hand. Figures: needs the real records; under about 30, show the items themselves (AMT-04).
- Narrow: below 820px sample the dots and state the sampling · Reduced motion: static cloud and line.
- Use when: showing spread, consistency or improvement across many real cases. · Avoid when: under about 30 items, or the records are not yours to show.
- Effort: S · Needs lib: no · Sources: P199 https://linear.app, P075 https://seeing-theory.brown.edu/basic-probability/index.html · Verdict: ADAPT, changed: merged with the running average; total delay capped at 450ms.

---

## Ranked lists

### AMT-20 ★ Priority slopegraph
- For: ranked-list, before-after · 4-10 items, ranks only
- Instead of: two numbered lists, "now" and "after", side by side
- Reader sees: Two columns, "what eats your week now" and "what will after", joined by lines showing each item climbing or sinking; only the one or two lines that tell the story are in the accent.
- Moves: in-view - lines start flat (both ends at the left rank) and swing to their right-hand rank over 0.9s cubic-bezier(.22,1,.36,1), 80ms apart capped at 450ms; each right-hand label arrives as its line lands.
- Build: left y = rank × rowH, right y = newRank × rowH; one `<line>` per item with `y2` moved by a CSS transition; quiet grey 1.5px lines, story lines in the accent at 3px; labels aligned to the line ends; caption "order, not amount". Figures: needs none; ranks come from stated priorities.
- Narrow: below 820px keep it; shorten labels, column gap 40% of width · Reduced motion: final positions.
- Use when: the story is a reshuffle of priorities or attention. · Avoid when: nothing moves more than one place.
- Effort: S · Needs lib: no · Sources: P118 https://www.edwardtufte.com/notebook/slopegraphs-for-comparing-gradients-slopegraph-theory-and-practice/ · Verdict: KEEP (swing set to the house ease and stagger)

### AMT-21 ★ Top three, then the tail
- For: ranked-list, emphasis · 3 headline items plus 5-80 more
- Instead of: a long numbered list where item 14 looks as important as item 1
- Reader sees: The top three as large rows, each with a small drawing and one line on why it ranks there; everything else compressed below into a thin row of tiny ticks labelled "and 81 more".
- Moves: in-view - the three rows arrive in order (rise 12px, 0.7s cubic-bezier(.22,1,.36,1), 100ms apart); then the tail pen draws as one path left to right (0.6-1.2s by length).
- Build: top rows are full components (serif 25px title, one line, a `mark` on the key phrase); the tail is one SVG path with a 2px tick per item (an `M x y v 10` subpath each), so it draws in one pass; an optional `<details>` "show all" opens a plain list. Figures: needs ranks only; values print only when sourced.
- Narrow: same; ticks wrap to two lines past 60 · Reduced motion: static.
- Use when: a few items matter and the rest prove breadth. · Avoid when: all items matter equally (use a grouped list).
- Effort: S · Needs lib: no · Sources: P097 https://pudding.cool/2018/08/wiki-death/ · Verdict: ADAPT, changed: rows rise instead of sliding in; the tail ripple became one pen-drawn path.

### AMT-22 Ordered bars with labels inside
- For: ranked-list, quantity-scale · 4-10 items in one unit
- Instead of: a vertical column chart with an axis and a legend
- Reader sees: Horizontal bars, longest on top, each with its label and value written inside; the reader's biggest win is the only bar in the accent.
- Moves: in-view - bars grow `scaleX(0)` to `scaleX(1)` from the left, 0.8s cubic-bezier(.22,1,.36,1), 80ms apart top-down capped at 450ms; values are printed, not counted.
- Build: div bars with `transform: scaleX(var(--v))` on an inner child so text is not scaled; no axis when values are printed; `tabular-nums`. Figures: needs a sourced value per bar; with ranks only, use AMT-28 or AMT-21.
- Narrow: unchanged (bars suit narrow screens) · Reduced motion: static.
- Use when: position in the order matters more than precise values. · Avoid when: the items are not in the same unit.
- Effort: S · Needs lib: no · Sources: P319 https://github.com/Financial-Times/chart-doctor/tree/main/visual-vocabulary · Verdict: ADAPT, changed: count-up cut.

### AMT-23 Where you stand: dots on one line
- For: ranked-list, comparison · 5-100 items ranked on one sourced value
- Instead of: a league table, or "we are among the best"
- Reader sees: One long line with every item placed as a dot by its score, a few well-known benchmarks labelled, and the client's own dot ringed in yellow pen.
- Moves: in-view - dots arrive in place (opacity plus 8px rise, 0.6s cubic-bezier(.22,1,.36,1)) in groups capped at 450ms; the client's dot lands last and the hand-drawn ring pen draws around it (1.1s).
- Build: SVG linear scale (or CSS `left: calc(var(--v) * 100%)` under 20 items); a simple beeswarm for crowds (sort by x, nudge y to avoid overlap); labels only on the client, 2-3 benchmarks and the two extremes; TVS ring path around the client's dot. Figures: needs the sourced metric for every dot.
- Narrow: below 820px the line turns vertical · Reduced motion: static, ring drawn.
- Use when: "where do we stand?" is the question (site speed, review score, cost per student). · Avoid when: the metric is disputed, or the reader needs every name.
- Effort: M · Needs lib: no · Code: TVS harvest · Sources: P095 https://pudding.cool/projects/vocabulary/, P335 https://github.com/Financial-Times/chart-doctor/tree/main/visual-vocabulary; ring from TVS harvest section 2.14 · Verdict: ADAPT, changed: merged; dots no longer slide in from the left edge; the client's dot gets the TVS ring.

### AMT-24 Focus bump chart across phases
- For: ranked-list, time-roadmap · 3-7 items over 3-6 phases, ranks only
- Instead of: a phase table that repeats the same priorities in every column
- Reader sees: Thick bands weaving between phase columns, showing which concern leads in each phase (setup first, then training, then hand-over); the band the text is discussing is in the accent.
- Moves: scroll-linked (pinned) - a `clipPath` rect's width follows progress linearly, revealing one phase column at a time as its caption passes; `n / N` counter; pin 2 viewport heights at most.
- Build: x per phase, y per rank; each item a path of cubic segments with flat tangents (`C x+dx/2,y0 x+dx/2,y1 x1,y1`), stroke-width 10, round caps; band colours from the actor colour contract (PPL-03); caption "top = main focus this phase"; phases named, never dated. Figures: needs none.
- Narrow: below 768px a static stack of phases, each a short ranked list with the band colour carried as a chip · Reduced motion: full chart.
- Use when: emphasis shifts over time and the reader should see attention being handed over. · Avoid when: the order never changes.
- Effort: M · Needs lib: no · Sources: P119 https://www.rawgraphs.io/learning/how-to-make-a-bump-chart · Verdict: ADAPT, changed: narrow tabs became a stacked list; phases relative, never dated; pin capped.

### AMT-25 Focus wheel list
- For: ranked-list, list-of-equals · 5-9 items
- Instead of: a bullet list the eye skims past
- Reader sees: A column of names rolls past a fixed reading line; the name on the line is full ink, its neighbours fade with distance, a short note beside it changes to match, and a "3 / 7" counter shows the place.
- Moves: scroll-linked (pinned for (n-1) × 300px, 3 viewport heights at most) - the list's translateY keeps the active index centred, linear with scroll; opacity by distance 1 / .5 / .25 / .1; the side note swaps when progress is within .15 of an index (old fades, new rises 8px, 0.6s cubic-bezier(.22,1,.36,1)).
- Build: sticky container; `vi = p * (n - 1)`; `list.style.transform = translateY(mid - (vi * itemH + itemH / 2))`; per-item opacity from `Math.abs(i - vi)`; the note swaps on `Math.round(vi)`; no forced snap. Ranked items run top to bottom. Figures: needs none.
- Narrow: below 768px a normal list with each note under its name · Reduced motion: normal list.
- Use when: clients, regions or priorities read best one at a time in a set order. · Avoid when: the reader needs to compare items side by side.
- Effort: M · Needs lib: no · Sources: P439 https://www.roveia.com · Verdict: ADAPT, changed: pin capped at 3 viewport heights; `n / N` counter added.

### AMT-26 Stop-anywhere section
- For: ranked-list, hierarchy · 3-7 paragraphs per section, ranked by importance
- Instead of: building up to the point at the end of a section
- Reader sees: Every section opens with its whole answer in one larger sentence with the key phrase marker-swept; each paragraph after it is a little smaller and quieter, so stopping after line one still gives the point.
- Moves: in-view - the lead sentence arrives (rise 12px, 0.75s); the marker sweep follows (0.7s after .35s); the quieter paragraphs reveal once with their block. No decorative margin triangle.
- Build: `.lead` serif clamp(22px,2.2vw,28px)/1.35; following paragraphs step down 19px, 17px, 16px, each a little nearer `--muted` via `color-mix(in oklab, var(--ink), var(--muted) 30%)`; the tail sits in a `<details>` "more" (the web version of an editor cutting from the bottom). Figures: not applicable.
- Narrow: unchanged · Reduced motion: static, sweep complete.
- Use when: busy readers skim the first line of everything. · Avoid when: the section is a story that needs suspense.
- Effort: S · Needs lib: no · Code: TVS harvest · Sources: P251 https://en.wikipedia.org/wiki/Inverted_pyramid_(journalism); marker from TVS harvest section 2.9 · Verdict: ADAPT, changed: the narrowing margin triangle cut; the marker sweep marks the answer.

### AMT-27 Recommended pick, ringed (new)
- For: ranked-list, choice-fork · 2-4 options, 1 recommended
- Instead of: a pros-and-cons table, or a ranked list with no stated winner
- Reader sees: Our recommendation as one large card with a hand-drawn yellow ring around its name and one line on why; the other options sit smaller beneath it, each with one honest "why not now" line.
- Moves: in-view - the winning card arrives (rise 12px, 0.7s cubic-bezier(.22,1,.36,1)); the ring pen draws around its name (1.1s after .3s); the runners-up arrive together 100ms later. Once.
- Build: winner card with a serif 30px title and a `mark` on the reason; runners-up in a 2-3 column grid at about 60% size in muted ink; the TVS ring SVG (viewBox 300×70, `preserveAspectRatio="none"`, 3px marker, non-scaling stroke) placed over the winner's name, overflowing by 16px and 13px; the ranking criterion is written on the card ("ranked on speed to first result"). Figures: needs none.
- Narrow: below 820px runners-up stack under the winner · Reduced motion: ring shown drawn.
- Use when: you recommend one option among a few and the others deserve a fair word. · Avoid when: the options can all happen together (use a grouped list); to show how the winner was chosen, use CHG-38.
- Effort: S · Needs lib: no · Code: TVS harvest · Sources: new; built from the TVS hand-drawn ring (harvest section 2.14) and the fork of three choices (CHG-36) · Verdict: NEW

### AMT-28 Cascade by rank (new)
- For: ranked-list · 3-7 items, ranks only
- Instead of: a numbered list where every line has the same weight
- Reader sees: Cards stacked down the page, the first priority largest and in full ink with a small drawing, each next card a step smaller and quieter, every one carrying a hand-drawn circled numeral and one line on why it sits there.
- Moves: in-view - cards arrive in rank order (rise 12px, 0.7s cubic-bezier(.22,1,.36,1)), 100ms apart capped at 450ms; each circled numeral pen draws as its card lands (0.6s).
- Build: a single-column `<ol>`; card scale steps 100%, 88%, 78%, 70%, 64% via font-size and padding (never transform, so text stays crisp); ink steps toward `--muted`; numerals inside a small hand-drawn ring path; the first card gets the marker on its reason; caption "order, not amount". Figures: needs none; order comes from stated priorities.
- Narrow: same, single column; size steps flatten below 560px · Reduced motion: static, rings drawn.
- Use when: the order of importance is the message and each rank has a reason. · Avoid when: items are equal (use a grouped list), more than 7 (use AMT-29), or they are levels built from the ground (use STR-17).
- Effort: S · Needs lib: no · Sources: new; applies the inverted-pyramid rule of P251 to items, with the TVS hand-drawn ring (harvest section 2.14) · Verdict: NEW

### AMT-29 Tier shelves: must, should, could (new)
- For: ranked-list, grouped-list · 8-20 items, ranks only
- Instead of: a 15-item ranked list nobody reads past item five
- Reader sees: Three drawn shelves, the top one labelled "Must", then "Should", then "Could"; each item is a short chip standing on its shelf, and the top shelf is the only one in full ink.
- Moves: in-view - shelves pen draw top to bottom (each 0.6-0.9s, next at 80-85%); each shelf's chips arrive as it lands (rise 8px, 0.6s cubic-bezier(.22,1,.36,1), 60ms apart capped at 450ms per shelf); lower shelves settle at 60% ink.
- Build: three rows, each a 2px hand-drawn SVG line (wobble filter, static) with chips in a flex-wrap row above it; chip colours from PPL-03 when items belong to parties; tier labels mono 12px caps; order inside a tier follows the brief, and the caption says ranks are by tier only. Figures: needs none.
- Narrow: same, chips wrap · Reduced motion: shelves drawn, chips shown, tiers at final ink.
- Use when: a long list has a real order but only the tiers are defensible. · Avoid when: the exact order of every item matters (use AMT-22 or AMT-21); for when-not-what tiers use SEQ-33.
- Effort: S · Needs lib: no · Sources: new; MoSCoW prioritisation https://en.wikipedia.org/wiki/MoSCoW_method · Verdict: NEW

---
