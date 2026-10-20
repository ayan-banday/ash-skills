# Visual patterns

Find the lazy default in your draft, swap in the drawn pattern that replaces it, and check the page's ledger so nothing repeats. The patterns come from pitch-site-udyaan's catalogue (`../../pitch-site-udyaan/references/catalogue/`), cut down to the ones that work **static**, for a reader alone. IDs in brackets match that catalogue, so you can open the full entry when you need more detail; ignore its motion lines unless the motion explains.

## Contents
- How to pick, in three steps
- Principles for every drawing
- The lazy default and what replaces it
- Order and time
- Structure and parts
- Change and choice
- Amounts, splits, comparisons and timelines
- Words and terms
- How it looks
- Emphasis marks
- Abstract ideas
- Static build kit
- What bad looks like

## How to pick, in three steps

1. **Find the lazy default.** Scan your plain-text draft for a list, a card row, a left-to-right step strip, a bold number, a two-column "before / after". Look it up in the index below.
2. **Check the shape.** Ask what the items do to each other: happen in order, split a whole, sort into groups, change, compete, add up. The shape picks the family.
3. **Check the ledger.** Every drawing carries `data-pattern="NAME"` on its wrapper. One name once per page, unless the repeat is the point (the same crate before and after) and you mark the second `data-pattern-repeat`. `scan_copy.py` fails a page with a silent repeat. Aim for **at least three different drawings** on a page of five or more sections, and some sections with none.

## Principles for every drawing

1. **It shows something stated in the text,** and one line under the heading says what the shape means: "Each cord is one skill; its socket is the plugin it moves into."
2. **No invented data.** Counts, lengths and positions come from numbers you were given, or they show order and grouping only. Mockups are labelled "Example view".
3. **Short words in SVG, sentences in HTML.** Two-word labels and numbers inside the drawing; explanations in an HTML grid beside or below it, lined up with the drawing on desktop, stacked on phones.
4. **One hand draws everything.** The same line kit (`.ln`, `.ln.thin`, `.ln.guide`, `.ln.hid`) and the same hand face for notes across the page. A device in the story (a phone, a terminal) is a drawn sheet in that line, never a glossy UI slab.
5. **One bright thing per drawing.** Everything is ink and quiet tint except the one part the eye should land on: the marker, the accent, or a pen circle.
6. **Static at rest.** The finished drawing is what a skim reader, a screenshot and a printout see. No scroll fades, no count-ups, no loops.
7. **Colour carries one meaning, and words carry it too.** "Goes away" is alert-coloured and says "goes away".

## The lazy default and what replaces it

If the draft has the thing on the left, draw the thing on the right.

- a bulleted list of problems → **Snake of stops** (SEQ-01)
- a numbered list of steps → **Route that drops deliverables** (SEQ-06), or **Snake of stops** if each step has a problem
- "Phase 1 / Phase 2 / Phase 3" boxes → **Construction lines to finished drawing** (SEQ-03)
- a horizontal step strip with arrows → **Route that drops deliverables**, or a **Metro map** if steps run in parallel
- a cycle drawn as arrows in a circle → **Loop** (SEQ-23) or **Orbit around one thing** (SEQ-22)
- "weekly call, monthly review" in a sentence → **Rhythm dial** (SEQ-25)
- a dated roadmap table → **Now, next, later horizon** (SEQ-33) or **Week ruler with a now line** (SEQ-37)
- a process list that never says who acts → **Swimlane hand-offs** (PPL-08)
- a "what's inside" paragraph or a feature list → **Opened crate** (STR-27 / STR-25)
- teams or tools listed under each need → **Switchboard** (STR-02)
- a list of things sorted into categories → **Switchboard** or **Constellation** (STR-01)
- core, extended, outside as three bullets → **Scope nest** (STR-21)
- ranked levels or audiences as a list → **Layers ladder** (STR-17)
- nested bullets, a folder tree as text → **Drawn outline tree** (STR-20)
- an org chart of boxes → **Floor plan with the roofs off** (STR-08)
- two columns, "Before" and "After" → **Same frame, before and after** (CHG-10, static pair)
- "from X to Y" in plain text, or old names and new names → **Strike and replace** (EMP-16)
- "we'll stop doing A, B and C" → **Cross off what goes away** (EMP-17)
- "today it's messy, after it's simple" → **Tangle to line** (STR-11)
- "if we wait" next to "if we act" → **Two roads from today** (CHG-37)
- "we looked at 30 options and kept 3" → **Sieve** (SEQ-18)
- a pros and cons table → **Fork with the pick circled** (CHG-36 + EMP-10) or **Elimination by tests** (CHG-38)
- "we balance speed, cost and quality" → **Trade-off triangle** (CHG-41)
- a "common mistakes" list → **Do and don't pairs** (CHG-26)
- a big bold number → **Key figure with a drawn note** (AMT-02)
- a count of people or things → **Isotype rows** (AMT-04)
- a percentage or a split of a whole → **Unit grid** (STR-33) or **Proportional tiles** (STR-32)
- "20 times more" → **Scale ribbon** (AMT-09)
- "takes 14 days" → **The long wait** (AMT-11)
- a duration or size nobody can feel → **Familiar-object scale** (AMT-01)
- costs or parts that add up → **Receipt** (AMT-13) or **Waterfall** (AMT-14)
- a bar chart → **Ordered bars with labels inside** (AMT-22)
- a league table → **Dots on one line** (AMT-23)
- "now" and "after" priority lists → **Slopegraph** (AMT-20)
- a 15-item list where three matter → **Top three, then the tail** (AMT-21)
- a precise-looking forecast → **Estimate drawn as a band** (AMT-06)
- a trend mentioned in passing → **Sparkline in the sentence** (AMT-15)
- a glossary table → **Translator ledger** (WRD-08)
- three bullets of equal weight → **Sentence list** (WRD-13)
- "the new screen will show..." in a paragraph → **The real thing, built** (PPL-21)
- a screenshot with a legend under it → **Annotated mockup with numbered callouts** (STR-28)
- "let me know how you'd like to proceed" → **Decision slip with the pick circled** (PPL-29)
- bold on a key phrase → **Marker** (EMP-01), at most one per screen

## Order and time

### Snake of stops (SEQ-01)
- **Use for:** 3 to 6 problems or steps in order, each with what happens and what it gives.
- **Draw:** stops alternate left and right down the page; one hand-drawn line weaves through numbered knots beside each stop. Each stop: the problem in one sentence, what's done, what you get (marker on the gain). The line ends at one result block.
- **Build:** stops are HTML; the line is one SVG path measured from the knots' centres at load and on resize (`getBoundingClientRect` relative to the wrapper), drawn once. Base path dotted at 25% ink, inked path solid.
- **Narrow:** below 820px stops stack in one column, the line runs down the left edge through the knots.
- **Avoid:** more than six stops; stops with no relation but order (use a sentence list).

### Route that drops deliverables (SEQ-06)
- **Use for:** a sequence where each step leaves something behind (a file, a decision, a working thing).
- **Draw:** a single road or wire running across, gently curved; at each stop a small drawn object hangs below it (a sheet, a box, a key) with its name. The reader sees what exists after each step.
- **Build:** inline SVG road, stops at fixed percentages; objects as small SVG symbols; step text in an HTML grid lined up to the stops. Under 700px the road turns vertical and objects sit beside their step.
- **Avoid:** steps that produce nothing (use the snake).

### Construction lines to finished drawing (SEQ-03)
- **Use for:** phases where the thing gets more finished each time.
- **Draw:** the same object drawn three or four times in a row: first as dashed construction lines, then partly inked, then complete, with one new part in accent each time. Phase name and one line under each.
- **Build:** one SVG symbol with parts as groups; each copy toggles classes (`.ln.guide` for not yet, `.ln` for done, accent stroke for the new part). This is one of the patterns where repeating the drawing is the point.

### Orbit around one thing (SEQ-22) and Loop (SEQ-23)
- **Use for:** steps that circle one project (orbit), or a cycle where the end feeds the start (loop).
- **Draw:** the thing in the centre; 4 to 6 steps on a ring with a hand-drawn arrowed path between them; for a loop, one arrow visibly re-enters the start and says what it carries back.
- **Build:** positions computed at fixed angles from the top; labels two words in SVG, details in an HTML list twin below. No animation.

### Rhythm dial (SEQ-25)
- **Use for:** a repeating cadence (weekly, fortnightly, monthly).
- **Draw:** a clock-like ring of weeks; small ticks for the weekly beat, rings for the fortnightly event, one filled accent mark for the monthly one. A legend in words.

### Now, next, later horizon (SEQ-33)
- **Use for:** a roadmap without firm dates.
- **Draw:** three bands receding like a landscape: "now" large and sharp, "next" smaller, "later" faint construction lines. Items sit on their band; confidence shows as line strength, not dates.

### Week ruler with a now line (SEQ-37) and Workstream metro (SEQ-31)
- **Use for:** a dated plan (ruler) or parallel workstreams that join (metro).
- **Draw:** a ruler of weeks with a "now" line in alert and spans for each piece of work; or metro lines (labelled in words) that run in parallel and meet at interchange stations where work must join.
- **Build:** CSS grid columns for weeks; spans with `grid-column`; inside `.scroll` on phones.

### Swimlane hand-offs (PPL-08)
- **Use for:** a process where the actor changes.
- **Draw:** one lane per person or tool; the work is a single line that drops from lane to lane at each hand-off, with the handed-over thing named on the drop.
- **Build:** a CSS grid with lanes as rows, SVG overlay for the line. Max four lanes.

### Rail and scroll story (kept from the older build)
- **Rail:** a fixed number of days with key days marked. `.days`, `.bands` in `assets/reference-deck.template.html`.
- **Scroll story with a building panel:** one person through the whole plan while the artifact they make fills in beside them. `#story`, `.panel`, `.pi` in the same file. This is the one place scroll-linked change explains, so it stays.

## Structure and parts

### Opened crate (STR-27 exploded offer, STR-25 x-ray)
- **Use for:** "what is this thing, and what's inside it?": a product, a plugin, a package, a team.
- **Draw:** the container drawn plainly (a crate, a box, a folder) with its lid lifted; the parts float above it on thin leader lines, each with a two-word label. One part in accent if the section is about it. Sentences go in an HTML key below, numbered to match.
- **Build:** one SVG; parts as groups at fixed positions; leader lines as `.ln.thin`. The key under it is a numbered grid.

### Switchboard (STR-02)
- **Use for:** sorting many items into a few groups, or matching needs to the people or tools that meet them.
- **Draw:** items as small plugs on the left, groups as sockets on the right, and one inked cord per item curving from plug to socket. A group with no cords shows an empty socket, which says something on its own.
- **Build:** both columns are HTML; cords are one SVG overlay computed from the elements' positions at load and on resize (cubic curves, horizontal tangents). Under 700px the board turns into grouped lists: each socket with its plugs under it.

### Constellation (STR-01)
- **Use for:** one goal with 3 to 5 branches and a few leaves each.
- **Draw:** the goal in the middle, branches as short hand-drawn lines, leaves as small dots with labels. Computed layout; a nested list twin below 820px.

### Scope nest (STR-21) and Layers ladder (STR-17)
- **Scope nest:** rings drawn inside out (us, close partners, everyone else) with items placed in their ring; "out of scope" sits outside with a dashed edge.
- **Layers ladder:** 3 to 5 ordered levels as rungs rising from the ground; each rung says who and what they get.

### Drawn outline tree (STR-20)
- **Use for:** a folder structure, a hierarchy, nested points.
- **Draw:** a hand-drawn trunk line with branches to each child, children indented, the one branch that matters inked darker or ringed.
- **Build:** a nested `<ul>` styled with border lines (`::before` elbows), so it stays text and wraps on phones. No SVG needed.

### Floor plan with the roofs off (STR-08)
- **Use for:** who sits where, which team owns which room of the work.
- **Draw:** a plan view of rooms with people as small figures inside and doors where work passes.

## Change and choice

### Same frame, before and after (CHG-10, static pair)
- **Use for:** one thing that changes.
- **Draw:** the identical frame twice, side by side (or stacked on phones), "Today" and "After". Only the parts that change differ; the changed parts are the only coloured marks in the "After" frame.
- **Build:** one SVG symbol rendered twice with different classes. Mark the second `data-pattern-repeat`.

### Strike and replace (EMP-16)
- **Use for:** old names, old numbers, old rules being replaced.
- **Draw:** the old value in muted text with a hand-drawn strike line through it; the new value written beside it in ink with a marker underlay. Group rows under labels when there are more than seven.
- **Build:** `<s class="was">` with a wavy SVG strike placed over it; `<mark>` for the new value.

### Cross off what goes away (EMP-17)
- **Use for:** things being removed or no longer needed.
- **Draw:** the items as small drawn tiles; the removed ones get a hand-drawn cross and drop to muted; the kept ones stay in ink, and an arrow carries them to where they go.

### Sieve (SEQ-18)
- **Use for:** "we looked at many and kept a few", and showing how they were chosen.
- **Draw:** a mesh line across the drawing; many small items above, the few that pass below, the test written on the mesh. Items that didn't pass stay above, muted.

### Tangle to line (STR-11)
- **Use for:** a messy present becoming a simple setup.
- **Draw:** a knot of crossing lines on the left resolving into one clean line on the right; labels on both ends.

### Two roads from today (CHG-37)
- **Use for:** acting versus waiting.
- **Draw:** one stem splits; the "wait" road is a dashed ghost ending on an empty sheet, the "act" road is inked and ends on the finished thing. One line of text at each end.

### Fork with the pick circled (CHG-36 + EMP-10) and Elimination by tests (CHG-38)
- **Fork:** 2 to 4 options as branches, each with one line; the recommended branch ringed with the pen circle and a handwritten "Ash's pick".
- **Elimination by tests:** the options in a column, the tests across the top; each failed test strikes the option out, so the survivor is obvious.

### Decision slip with the pick circled (PPL-29)
- **Use for:** the page's close: what the reader decides.
- **Draw:** a paper slip per decision: the question, the options as plain lines, the recommendation pen-circled with a handwritten reason beside it. Looks like something to bring to the meeting.

### Trade-off triangle (CHG-41) and Do and don't pairs (CHG-26)
- **Triangle:** three goals at the corners, the plan as one dot placed honestly inside, with a line on why there.
- **Do and don't:** pairs side by side, each leading with the pick and its impact; the "don't" side muted with a small cross.

## Amounts, splits, comparisons and timelines

**First count the real figures.** Zero figures: show order or grouping only (slopegraph, top three, worded sizes). One to three: draw each so it can be felt. A full series: chart it plainly.

### Key figure with a drawn note (AMT-02)
- **Use for:** 1 to 3 real numbers that carry the point.
- **Draw:** the number large in the display face (`tabular-nums`), a pen arrow curving to a handwritten note of 12 words or fewer saying what it means, and a small source line.
- **Avoid:** a row of five big numbers. Cap at three.

### Isotype rows (AMT-04)
- **Use for:** a count of people or things, or a few counts compared.
- **Draw:** rows of identical small line figures (people, sheets, boxes), one per thing or one per stated unit ("1 sheet = 1 copy"). More means more figures, never bigger figures.
- **Build:** one `<symbol>` and `<use>` per unit; rows wrap at 10 on phones.

### Unit grid, 1 in N (STR-33) and Proportional tiles (STR-32)
- **Use for:** shares of a whole (replaces the pie and the dot field).
- **Unit grid:** 100 (or N) small squares, filled in blocks by group so the proportion reads at a glance; labels in words beside each block.
- **Proportional tiles:** one rectangle split into tiles whose areas are the shares, each tile labelled inside when it fits and by a leader line when it doesn't.

### Nested squares (STR-34) and Scale ribbon (AMT-09)
- **Nested squares:** two amounts as squares sharing a corner, area proportional, for gaps of 2x to 20x.
- **Scale ribbon:** a short stub and a long line literally N times its length, folding back like a ribbon when it runs out of width, the multiple written at its end. For 10x or more.

### Familiar-object scale (AMT-01) and The long wait (AMT-11)
- **Familiar object:** an everyday object (a phone, an A4 sheet, a cricket pitch) drawn at the same scale as the thing measured.
- **The long wait:** a duration drawn as a long dotted line with small day ticks and a figure standing at the start, so "14 days" looks like 14 days.

### Receipt (AMT-13) and Waterfall (AMT-14)
- **Receipt:** line items on a paper slip with a torn edge, amounts aligned, the total underlined twice.
- **Waterfall:** bars that step up or down from a start to an end, each step labelled with what moved it.

### Ordered bars with labels inside (AMT-22) and Dots on one line (AMT-23)
- **Ordered bars:** horizontal bars, longest first, label and value written inside each; the one bar that matters in accent. No axis when values are printed.
- **Dots on one line:** every item as a dot on one scale; a few labelled; the subject's dot pen-circled.

### Slopegraph (AMT-20) and Top three, then the tail (AMT-21)
- **Slopegraph:** two columns ("now", "after") joined by lines; only the one or two lines that tell the story in accent. Ranks only, so it needs no data.
- **Top three, then the tail:** three large rows with a reason each, then a thin row of tiny ticks labelled "and 24 more".

### Estimate drawn as a band (AMT-06) and Sparkline in the sentence (AMT-15)
- **Band:** a range shown as a shaded band with the low and high ends labelled, never one precise line.
- **Sparkline:** a word-sized line chart inside the sentence that mentions the trend.

### Segmented bar, true funnel, shrinking band (kept)
- **Segmented bar:** a timed split, widths proportional to minutes (`.seg` in the older build).
- **True funnel:** many narrowing to one, continuous edges (`#fn`; clip-path points in the order top-left, top-right, bottom-right, bottom-left).
- **Shrinking band (AMT-18):** a flow that loses people at each real waypoint, the band's width the count.

### Timelines, in short
- Dated plan → Week ruler with a now line. Parallel work → Workstream metro. No dates → Now, next, later. Fixed days → Rail. A thing that grows over time → Construction lines to finished drawing. Pick the one whose question matches: "when?", "who in parallel?", "how sure?", "how long?", "how finished?".

## Words and terms

### Translator ledger (WRD-08)
- **Use for:** 3 to 8 terms the reader needs.
- **Draw:** a ledger with three columns: the term in mono, what it means in plain words, and what it means for the reader. Ruled lines, no boxes. Static (no tapping).

### Sentence list (WRD-13)
- **Use for:** three equal points with no shape between them.
- **Draw:** one sentence per point, each opening with a bold phrase, set large with generous space and a small numeral in the margin.

### Margin notes and pen arrows (EMP-22, EMP-25, WRD-11)
- **Use for:** a caveat, a definition, or "Ash's take" beside the main text.
- **Draw:** handwritten note in the margin with a pen arrow to the word it explains. Below 900px the note drops under its paragraph.

## How it looks

Use one of these in the "How will it look?" section (`page-shape.md`). Every mockup is labelled "Example view".

### The real thing, built (PPL-21)
- **Use for:** a screen, a menu, a file, a message, a form that will exist.
- **Draw:** the thing as a drawn sheet in the page's line (a terminal is a sheet with a mono prompt; a phone is a rounded outline), filled with realistic content, never lorem ipsum. Plain, so it doesn't pass for a screenshot.
- **Build:** HTML inside a `.sheet` frame (1px ink line, near-square corners, a title bar with the label "Example view"). Text stays real text.

### Annotated mockup with numbered callouts (STR-28)
- **Use for:** pointing the reader at the parts of the finished thing.
- **Draw:** the mockup with two or three numbered circles on it; a key beside it says what the reader will notice or do at each number. Pen arrows instead of numbers when there are only one or two.

### Filled-in example
- **Use for:** a template, a rule file, a plan format.
- **Draw:** the actual filled-in block (a short file, a form, a list with real entries) on a paper sheet, with a handwritten margin note on the one line that matters.

### Dashboard mock (kept)
- `.mock`, `.mini` in the older build: one person's view and one team table, status in words and colour.

## Emphasis marks

- **Marker (EMP-01):** a highlighter band behind the phrase that says what the reader gets or decides. At most one per screen.
- **Pen circle (EMP-10):** a hand-drawn ellipse, slightly open at the top, around the recommended option or the key number.
- **Pen underline (EMP-04):** a wavy underline under one word that carries the turn.
- **Only the working part in colour (EMP-18):** a drawing in ink and tint with only the part under discussion coloured.

## Abstract ideas

A section about values, a framework or a mental model with 3 to 6 parts that differ in kind can be a living metaphor: one world, one creature or object per part, each backed by a real fact, met in order. Plan it with the story-plan skill (`../../story-plan/references/living-metaphors.md`) and build its storyboard here, static.

## Static build kit

The starter carries these; copy them, don't reinvent.

- **Line classes:** `.ln` (1.8px ink, round caps), `.ln.thin` (0.9px), `.ln.guide` (dashed at 30% ink, for construction lines and "not yet"), `.ln.hid` (dashed, for hidden or removed), `.ln.acc` (accent), `.ln.alert`.
- **Hand face:** `.hand` for notes and labels written "by pen" (one face per page, from the type pairing).
- **Pen circle:** `.pen-ring`, an SVG ellipse left slightly open, placed over the target; accent stroke 2.4px.
- **Wobble:** for a drawn feel, give paths a few control points with ±1.5px seeded jitter (`jit()` helper in the starter). Never randomise per load; the same page renders the same.
- **Measured connectors:** cords, snakes and leader lines that join HTML elements are computed once at load and on `resize` (throttled) from `getBoundingClientRect()` relative to their wrapper. Without JS, the HTML still reads: the cords are a bonus, the grouped content is the content.
- **Phone twins:** any drawing whose labels would drop under 12px at 400px gets a list twin (`.twin`) shown below 700px, and the drawing hides or shrinks.
- **`data-pattern`:** on the wrapper of every drawing, the pattern's name. The scan reads it.

## What bad looks like

- Every section a row of three rounded cards with an icon.
- A left-to-right strip of numbered circles joined by arrows.
- The same drawing used for two different ideas on one page.
- A pie or bar chart with invented values, or a count-up number.
- An SVG with paragraph-length labels that shrinks to 5px on a phone.
- A drawing with no sentence saying what its shape means.
- Five categories in five colours with a legend to decode.
- A glossy UI screenshot look-alike with fake brand details.
- Content that fades in on scroll and is blank in a screenshot.
