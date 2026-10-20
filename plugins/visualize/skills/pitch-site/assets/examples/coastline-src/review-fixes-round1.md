# Prototype v2: fixes from the two reviewers

Two reviewers read v1. A tough creative director: REVISE, 37/60 ("a truck drawing that clearly belongs to this
client opens strong, then drifts into rounded cards and never comes back"). A first-time reader: NEARLY, 41/60
(could not tell who the sender is or what they would buy; the three asks got renamed further down; some specifics
were not in the facts). The aim of v2: the drawing carries the whole page from hero to close, every surface looks
like part of a drafting sheet, and every line traces to facts.md.

## Global rules for v2 (all builders)
- starter.html now has `--r-sheet: 2px`. Every card, panel, stage, quote box and contact card uses
  `border-radius: var(--r-sheet)`. Only a drawn device (the dark tablet) keeps a big radius. Chips are 3px.
- No middle dots ( · ) in HTML text or labels: use a comma ("ASK 1, THE BOX"). Middle dots may stay inside SVG
  drawing labels only.
- No kicker labels above headings unless listed below. No text that narrates the page ("Scroll to...", "The drawing
  stays still while you scroll").
- No 1px ring plus big radius on everything. Prefer drafting language: a thin ink rule, a sheet edge, a title block.
- Keep everything that was not mentioned. Keep the house motion rules from brief.md.
- Copy below is final: use it word for word. facts.md is updated; nothing may appear that is not in it.

---

## Builder A: frag-1-hero.html and frag-2-echo.html

### Hero
- Delete the bottom cue "Scroll to follow the load" entirely.
- Label: TIDEWATER STUDIO FOR COASTLINE COLD CHAIN (no dots).
- Lede becomes: Tidewater Studio fits sensors, a driver tablet and a trip record to your trucks. Follow one night's run from Kochi to Bengaluru to see how, then pick one route for a pilot.
- Corner tag stays: Prototype, sample brief, fictional companies (comma, no dot). At 899px and below, set it absolutely at the bottom right of the hero (bottom: clamp(16px,2.6vh,26px); right: var(--gutter); text-align:right), so the first words read are the proposal label.
- At tall portrait screens (`@media (max-aspect-ratio: 4/5)`): hero height auto, the drawing full-bleed (`margin: 48px calc(-1 * var(--gutter)) 0; width: 100vw`) so the truck does not float between empty bands.
- Make sure the title block is fully on screen at 1280x800 with a little air below it.

### Echo (What you told us): stop being three identical cards
- h2: What you told us
- lede: Three problems, in your words, from our meeting in Kochi. Each one gets its own answer below.
- one line under the lede (body size, muted): Sensors, App, Data and Field are our four teams. Who does what is further down.
- Layout: one large SVG of the truck (drawTruck with parts cab, box, door, chassis, wheels, ext, dim; strokes at opacity .45) spanning the content width. Light the three parts in red (`.ln.red`, stroke-width 2.4): box plus door, cab, ext plus dim. Three ask blocks sit around the drawing, each joined to its part by a thin red leader line that pen-draws when the section enters: the cab block above-left (leader from the cab roof up), the box block above-right (leader from the box top up), the trip block below the drawing (leader from the dimension line down). Use a 12-column grid: row 1 cab block columns 1-4 and box block columns 7-11; row 2 the SVG across all columns; row 3 the trip block columns 4-9. Leader lines are drawn in one absolutely positioned SVG overlay measured from the blocks and the drawing (recompute on resize and document.fonts.ready), or inside the main SVG with the blocks positioned to match; choose whichever stays exact.
- Each block: label (ASK 1, THE BOX / ASK 2, THE CAB / ASK 3, THE TRIP), h3, the quote in italic, then ANSWERED BY with chips. No background, no border, no radius. No thumbnail badges.
  1. ASK 1, THE BOX · See inside every truck · "We lose fish we can't see going bad." · Sensors, Data
  2. ASK 2, THE CAB · Put the logbook on a screen · "Drivers write temperatures on paper, and nobody reads it." · App, Field
  3. ASK 3, THE TRIP · Prove every trip · "When a buyer complains, we can't prove what happened." · Data, App
  (the " · " above only separates fields in this brief; on the page each is its own element)
- Delete the red hand line "The drawing keeps this order...".
- At 899px and below: the full-width SVG first, then the three blocks stacked, each with truckBadge(...) at 96px.
- Section padding-bottom clamp(48px,6vw,80px) so there is no empty strip before the next section.

---

## Builder B: frag-3-stage.html

- Remove the section kicker label above the h2. h2: Follow one load of fish through the night
- lede: One truck, one night, Kochi harbour at 6 pm to Bengaluru at 7 am.
- Counter reads: EXAMPLE NIGHT 01 / 05 (so the night stays labelled as an example).
- Caption labels without dots: 6 PM, KOCHI HARBOUR / 2 AM, THE SALEM STOP / THE FIX, ASK 1 / THE FIX, ASK 1 / ZOOM OUT
- Step 3 caption: Our Sensors team fits two small sensors: one inside the box, one on the door. (Remove the CAB sensor dot and its label; keep BOX and DOOR.)
- Step 4 caption: Each sensor reports through the night. When a crate warms, your office gets a message <mark>while the truck is still on the road.</mark>  The drawing's phone label NIGHT MANAGER becomes YOUR OFFICE.
- Step 5 caption: Now picture all 38 trucks. Every load, on every route, shows up on one screen in your office.
- Active caption: in apply(), toggle `is-on` on the current block; `#stg .stg-block:not(.is-on) .stg-card{opacity:.38}` with `transition: opacity .4s var(--ease-out)` (not under FINAL). Remove `rv` from the five caption cards.
- Hide the title block inside the stage (`#stg .t-tb, #stg .t-tbtext {display:none}`); raise stage SVG labels: `.stg-lbl` 16px, `.t-dimtext` 15px (in SVG user units scaled to read at about 11 to 12px on screen; check the screenshot).
- Ticks: 16 evenly spaced (t from .3 to .95) on the Bengaluru road, 10 on the Coimbatore road, 12 on the Chennai road.
- FINAL / reduced motion:
  (a) when `reduce` is true and the URL has no `final=1`: keep the observers and scroll listener, switch steps instantly (`apply(n, true)`), and set `place(1)` at step 5, `place(0)` otherwise; nothing scrubs.
  (b) when `final=1`: show step 4 on the stage, hide the counter, and prepend to the step-5 caption card a static clone of the stage SVG showing the finished pull-back (`place(1)` transform applied to the clone's truck, `--zf: 1`, ids removed). CSS: `#stg .stg-card > svg{display:block;width:100%;height:auto;margin-bottom:8px}`.
- Tablet (max-width 819px): stage height 46svh with a soft bottom shadow; captions padding-top 48svh, padding-bottom 16svh; blocks min-height 30svh, aligned to the top; the narrow reading line .68 of the viewport.
- Stage and caption cards use var(--r-sheet).

---

## Builder C: frag-4-paper.html and frag-5-switch.html

### Paper vs screen
- Label above h2: ASK 2, THE CAB (comma). Keep the cab badge.
- Field line becomes: Our Field team shows each driver the tablet on their own route.
- Delete the "AN EXAMPLE LOG" kicker; the paper sheet title becomes DRIVER LOG, EXAMPLE NIGHT.
- The tablet: replace the five identical bars with small temperature traces: an inline SVG per row
  `<svg class="p2s-trace" viewBox="0 0 160 18"><path d="M0 12H160"/></svg>`; the SALEM row uses `M0 12H58C68 12 72 3 80 3C88 3 92 12 102 12H160`. CSS `.p2s-trace{width:100%;height:18px;overflow:visible}.p2s-trace path{fill:none;stroke:rgba(240,237,229,.55);stroke-width:1.6;stroke-linecap:round}.p2s-srow.warm .p2s-trace path{stroke:var(--tint-3);stroke-width:2.2}`. Pen-draw the traces (prepDraw, penDraw) when the screen arrives.
- WARM uses var(--tint-3) for its dot and text (same colour family as the stage's warm crate). Delete the blink animation: the dot is simply on.
- Delete the "OK" words on the tablet rows (not in the copy); a row that is fine shows only its trace.
- Remove the dead space under the heading at 1280px: put the heading, the YOU TOLD US box, the body and the goal line in one column (max-width 720px), then the paper and the tablet side by side below.
- Every panel uses var(--r-sheet) except the tablet (a device keeps 22px).

### Switchboard
- Remove the WHO DOES WHAT kicker. h2: Four small teams, one clear job each
- lede: Each of your three asks has two of our teams on it.
- Left column (three asks, same names as everywhere else; delete problem 4):
  See inside every truck / Put the logbook on a screen / Prove every trip.
  Replace the red numerals with truckBadge('box'), truckBadge('cab'), truckBadge('trip') at 64px wide.
- Links: ask 1 to Sensors and Data; ask 2 to App and Field; ask 3 to Data and App.
- Team cards: delete the 6px side stripe; the whole card takes its chip tint as background (`background: var(--tint-n)`), no ring, padding 18px 22px, radius var(--r-sheet). Keep each team's one line.
- Delete the four "carries N" pills.
- Close line: <mark>One person, Meera Nair, our project lead, is your contact for all four teams.</mark>  (`max-width: none; text-wrap: balance`)
- Remove `rv` from the board itself (the cords already animate).

---

## Builder D: frag-6-roads.html and frag-7-cta.html

### Two roads
- Label: ASK 3, THE TRIP (comma). Keep the trip badge.
- Road labels: IF NOTHING CHANGES / WITH A ONE-ROUTE PILOT
- The pilot road reads as the drawing's dimension line: add `marker-start="url(#arr)" marker-end="url(#arr)"` to it.
- Replace the pilot road's end node with a small drawn trip record: a sheet `M548 296H620V352H548Z` (class ln), a title strip `M548 340H620M590 340V352` (ln thin) and a temperature trace `M556 324C566 320 572 326 582 322S600 320 612 323` (ln). Replace the wait road's end node with an empty dashed sheet `M548 68H620V124H548Z` (class "ln hid"). Adjust coordinates so they sit exactly at each road's end in your SVG.
- End texts stay as they are (they are in the facts).
- Panels and cards use var(--r-sheet).

### The close: the truck comes back
- h2: Start with one route
- lede: Pick the route. Meera sends the one-page plan within a week.
- Replace the three icon cards with ONE drawing of the truck on the dark band: an SVG (viewBox about "0 0 1000 470") with drawTruck(g, {labels:true}) and these overrides inside #cta: `.ln{stroke:var(--paper)}`, `.svg-label{fill:var(--paper)}`. Fill the box region `M238 92H782V266H238Z` with var(--tint-1) at fill-opacity .18. Draw the two sensor dots at TRUCK.sensors.box and TRUCK.sensors.door (r 7, fill var(--ground), stroke var(--paper)). Draw the dimension line and its text in var(--marker). Extend the title block with a fourth cell `M884 404H984V438H884Z` labelled APPROVED BY in the top row, its value cell left empty, and give that empty cell a yellow pen ring (the EMP-10 loop) that pen-draws last: this is where the reader signs off.
  The drawing pen-draws when the section enters (house pen rule, plotter order: centre lines, object lines, dimension, title block, then the ring).
- Under the drawing, the three steps as plain text in a 3-column grid (no background, border or radius), each column under its part of the drawing:
  1. Pick one route. We suggest Kochi to Bengaluru, the run this page follows.
  2. Talk to one person. Meera Nair, our project lead, is your one point of contact.
  3. Get a one-page plan. Within a week she sends a one-page plan for that route, including what the pilot costs.
  (h3 = the first sentence, body = the rest.)
- Contact card stays (portrait in DETAIL A ring, name, email pill, Copy button), radius var(--r-sheet), with the line:
  Send her the route you pick. Within a week she replies with a one-page plan for that route, including what the pilot costs.
- The tiny portrait label DETAIL A becomes MEERA NAIR (a reader does not know drawing-office terms).
- Remove `rv` from the steps and the contact card (the drawing is the one moving thing here).
- Footer line stays.
