# Build brief: Coastline Cold Chain proposal (prototype)

You are one of four builders making ONE scroll-told proposal website together. Each builder writes its own
section fragment files. A build script joins them under a shared starter. Quality bar: a calm, crafted,
award-level editorial site (think Anthropic's claude.com and the Washington Post's line-drawn scrollytelling),
never a generic template. Clarity first: a reader who won't read must get the point from headlines,
drawings and highlighted phrases alone.

Folder: C:\Users\ayanb\AppData\Local\Temp\claude\S--Charlotte\521832f6-9e00-4497-bede-9f5f9128747b\scratchpad\proto\
- starter.html: READ IT FIRST. Tokens, fonts, base classes, helpers, the truck drawing. Do not edit it.
- patterns.md: the pattern recipes your sections use (by ID). Follow their values.
- build.py, shot.py: build and screenshot tools (below).

## The story (fictional sample brief)
Tidewater Studio (a small product and sensor studio in Kochi) proposes a pilot to Coastline Cold Chain,
which drives fresh fish from Kochi harbour to restaurants and hotels in Bengaluru, Chennai and Coimbatore
in 38 refrigerated trucks. Drivers log temperatures on paper at each stop. Last summer some buyers turned
away loads they said arrived warm. Tidewater has four teams: Sensors, App, Data, Field.
The motif is an engineering drawing of Coastline's own truck (see TRUCK in starter.html). The box stands
for ask 1, the cab for ask 2, the dimension line (the route) for ask 3.

## House rules (all builders)
- Use ONLY the copy given below, word for word. Do not add sentences, numbers, claims or em dashes.
- Use the starter's tokens (var(--ink), var(--red), var(--tint-1)...), never new hex colours.
- Namespace every class and id with your section prefix (given per section) to avoid collisions.
  Shared classes you may use as-is: band paper/card/t1/t2/t3/dark, wrap, band-head, lede, label, hand,
  chip c-sensors/c-app/c-data/c-field, chips, rv (reveal; add style="--d:.1s" to stagger), ln thin/hid/cl/guide/red/cyan,
  svg-label, svg-hand, btn, mark.
- A <mark> must sit inside running text (inside a <p>), never as a direct child of a grid or flex box.
- Motion: one moving thing per screen. Lines draw like a pen with penDraw() (length-based duration, house ease).
  Arrivals use .rv. Never bounce, elastic or overshoot. Text plays once. Scroll-linked motion is linear.
  Texture never animates. Nothing flies in from the side.
- Every animation must respect FINAL (already handled by onView, prepDraw, penDraw, .rv). Under FINAL the
  section must show its finished, fully labelled state. Check it with shot.py --final.
- Laptop first (1280x800); must also work at 1024x768 and 768x1024 (tablet). Below 768px a stacked static
  version is fine. No horizontal overflow at any of those widths.
- Plain vanilla JS + SVG + CSS. No libraries. Put your CSS in a <style> and JS in a <script> (wrap the JS in
  an IIFE: (() => { ... })();) inside your fragment, after your markup.
- Use the helpers: $, $$, onView(el, fn, threshold), prepDraw(paths), penDraw(paths, {delay, parallel}),
  drawTruck(svgOrG, {parts, cls, labels}), truckBadge('box'|'cab'|'trip'), TRUCK (path data, crates,
  warm crate index, sensor points), NS, FINAL, reduce.
- Section badges: put truckBadge(...) markup (about 120px wide) above the eyebrow label where the copy says BADGE.

## Tools
Build only your fragments:  python build.py --only frag-3 --out test-B.html
Screenshot:                 python shot.py test-B.html shot-B1.png --sel "#stg" --final
                            python shot.py test-B.html shot-B2.png --sel "#stg" --scroll 1.2   (live, mid-scroll)
                            add --width 1024 --height 768 or --width 768 --height 1024 for tablets
Run python without -I. LOOK at every screenshot you take (Read the png). Fix what looks wrong: overlaps,
labels crossing lines, cut-off text, empty gaps, overflow, console errors. Take at least 4 screenshots.

---

## SECTION 1 · frag-1-hero.html · prefix hero- · Builder A
Pattern: WRD-01-style self-drawing hero motif + SEQ-03 construction lines to finished drawing.
Full screen (min-height 100svh, nothing from the next section visible). Background var(--paper).
Layout: copy top-left, the big truck drawing (drawTruck with all parts incl. 'hatch' and 'ext', inside
<g filter="url(#graphite)">) filling the lower two thirds, right-aligned, max-width 980px.
Draw-on (plotter order, total under 3.5s): faint construction guides first (a light dashed bounding box and
a horizontal datum line, .ln.guide, drawn fast), then the centre lines, then object lines (cab, box, door,
wheels, chassis) with penDraw, then the dimension line + its text, then the title block last. The guides stay
faint afterwards. Add one red hand note (class svg-hand) beside the box after the drawing finishes:
"what's inside?" with a small red arrow pointing at the box.
Copy:
- label: PROPOSAL · TIDEWATER STUDIO FOR COASTLINE COLD CHAIN
- h1: Keep every load cold, and prove it.
- lede: You told us three things at our meeting in Kochi. This page answers each one by following a single night's run from Kochi to Bengaluru.
- small cue at the bottom: Scroll to follow the load ↓
- tiny corner tag (top right, label style): Prototype · sample brief, fictional companies

## SECTION 2 · frag-2-echo.html · prefix echo- · Builder A
Pattern: WRD-15 echo cards with "answered by" + a motif key row of three badges. Band: card.
- h2: What you told us
- lede: Three problems, in your words. Each one gets its own answer below.
Three cards (grid of 3; each card: small badge at top, tag label, h3 title, the quote in italic serif-like
style using var(--font-body) italic 19px, footer pinned to the bottom with label ANSWERED BY and chips):
1. BADGE truckBadge('box') · tag: ASK 1 · THE BOX · title: See inside every truck · quote: "We lose fish we can't see going bad." · chips: Sensors (c-sensors), Data (c-data)
2. BADGE truckBadge('cab') · tag: ASK 2 · THE CAB · title: Put the logbook on a screen · quote: "Drivers write temperatures on paper, and nobody reads it." · chips: App (c-app), Field (c-field)
3. BADGE truckBadge('trip') · tag: ASK 3 · THE TRIP · title: Prove every trip · quote: "When a buyer complains, we can't prove what happened." · chips: Data (c-data), App (c-app)
Under the grid, one line in the hand font, red: The drawing keeps this order all the way down: the box, the cab, the trip.
Cards arrive with .rv staggered 0 / .1 / .2s. Each badge's red part pen-draws once when its card arrives.

## SECTION 3 · frag-3-stage.html · prefix stg- · Builder B (the centrepiece)
Pattern: ARC-02 / SEQ-02 pinned line-drawn stage, using STR-25 x-ray, MOT-04 colour one hue at a time,
MOT-05 / STR-26 pull-back. Band: t1 (the pale cyanotype wash). id="stg".
Head (normal flow, before the pinned part):
- label: AN EXAMPLE NIGHT, CHOSEN TO SHOW HOW IT WORKS
- h2: Follow one load of tuna through the night
- lede: One truck, one night, five changes. The drawing stays still while you scroll.
Pinned part: wrapper about 300vh max. Desktop: two columns, the stage (sticky, top 10vh, height 80vh)
on the left at ~60% width, captions scrolling in a right column at ~34% width, each caption block
min-height ~60vh, caption text on a var(--card) panel with radius 14px and a 1px var(--line) ring.
A counter "01 / 05" in label style sits at the stage's top-left and updates. One IntersectionObserver with
rootMargin "-45% 0px -45% 0px" sets stage.dataset.step (1-5). Scrolling back must undo steps.
The stage SVG: the truck (drawTruck, parts ground cl chassis cab box ribs door wheels ext dim tb) plus layers:
crates (TRUCK.crates, hidden until step 2), sensors (3 small circles r 7 at TRUCK.sensors with a leader line
and label text BOX / DOOR / CAB, hidden until step 3), a temperature line under the route (step 4), and a
route map for the pull-back (step 5).
Steps (each changes exactly ONE thing):
1. Today: truck drawn normally, box closed (ribs visible, crates hidden).
   eyebrow: 6 PM · KOCHI HARBOUR · caption: The load leaves Kochi at 6 pm. From here to Bengaluru, nobody can see inside the box.
2. X-ray: the box outline and ribs fade to a ghost (opacity .25) while the 12 crates pen-draw inside; the warm
   crate (TRUCK.warm) draws in var(--red) and gets a soft red fill (fill var(--tint-3)).
   eyebrow: 2 AM · THE SALEM STOP · caption: At the 2 am stop the door stays open too long. The crate nearest the door warms up, and nobody knows.
3. Sensors: three sensor dots arrive (scale .96 to 1 + opacity) with pen-drawn leader lines and labels; the box
   region floods with a flat var(--tint-1) fill (MOT-04: one hue arrives). chip under caption: Sensors.
   eyebrow: THE FIX · ASK 1 · caption: We fit three small sensors: one inside the box, one on the door, one in the cab.
4. Signal: a temperature line pen-draws along the route (a gentle flat line with one bump near the Salem stop,
   bump marked in red with a small label WARM, then a red dashed alert line from the bump up to a small phone
   glyph near the title block labelled NIGHT MANAGER). chips: Sensors, Data.
   eyebrow: THE FIX · ASK 1 · caption: Each sensor reports through the night. When a crate warms, your night manager gets a message <mark>while there is still time to shut the door and save the load.</mark>
5. Pull-back: the whole truck group scales down (linear with scroll progress inside this step, transform
   origin at the truck's centre, vector-effect non-scaling-stroke on strokes) until it is a small truck on a
   route map: three faint routes from a dot labelled KOCHI to BENGALURU, CHENNAI, COIMBATORE, with tiny
   truck ticks along them (drawn as small marks, about 12 in total). The Kochi to Bengaluru route is ink, the others faint.
   eyebrow: ZOOM OUT · caption: Now picture all 38 trucks. Every load, on every route, shows up on one screen in your office.
Below 820px: stage pins to the top (50svh) with captions under it as solid cards. Below 768px: a stacked
static version (five small stills, one per step, each with its caption) is acceptable.
Under FINAL: show step 4's full state (crates, warm crate, sensors, tint, temperature line, alert), with all
five captions readable in the column.

## SECTION 4 · frag-4-paper.html · prefix p2s- · Builder C
Pattern: CHG-09 paper vs screen, plus EMP-16 strike and replace. Band: t2 (trace yellow).
- BADGE truckBadge('cab'), label: ASK 2 · THE CAB
- h2: Put the logbook on a screen
- a "You told us" block (frosted box, label YOU TOLD US, quote in 20px): "Drivers write temperatures on paper, and nobody reads it."
- body: Your drivers keep the habit they have. At each stop they tap the reading on a tablet instead of writing it down. The office sees it the moment it is entered.
- line with strike and replace: The goal: a warm reading gets noticed <del>the next morning</del> <ins>the same minute</ins>.
- chips: App, Field · and one line: Our Field team rides along on the first week's runs to show each driver the tablet.
Visual (label above it: AN EXAMPLE LOG): left a slightly tilted paper sheet (rotate -1.2deg, untilted below
820px) titled DRIVER LOG, with rows KOCHI 6 PM, COIMBATORE 10 PM, SALEM 2 AM, HOSUR 5 AM, BENGALURU 7 AM, a
"TEMP OK?" column filled by handwritten ticks (font-hand, var(--cyan)) that write in one by one; the SALEM row
gets a scrawled "?" and a hand note "door stuck?" in red. Middle: a thin arrow with the label same rows, live.
Right: a dark tablet (var(--ground), radius 22px) with the same five rows as bars that fill; the SALEM row reads
WARM in var(--marker) with a dot that blinks three times then holds. No temperatures as numbers anywhere.

## SECTION 5 · frag-5-switch.html · prefix swb- · Builder C
Pattern: STR-02 switchboard (no pin needed: link sets ink in one by one as the section scrolls through,
scroll-linked like the snake; under FINAL all inked). Band: paper.
- label: WHO DOES WHAT
- h2: Four small teams, one clear job each
- lede: Scroll to see which team answers which problem.
Left column (problems, each a card with a small red number): 1 Crates warm up unseen · 2 Paper logs go unread · 3 Complaints can't be checked · 4 Drivers are new to tablets
Right column (teams, each a card with its chip colour as a left edge and one line):
Sensors: fits and looks after the sensors · App: builds the driver tablet and the office screen · Data: keeps a record of every trip · Field: trains drivers on their own routes
Links (curved cords between card edges, faint dashed construction lines first, then inked one problem at a time):
1 to Sensors and Data · 2 to App and Field · 3 to Data and App · 4 to Field and App.
After the last problem inks, a small pill arrives beside each team: carries 1 / carries 3 / carries 2 / carries 2
(Sensors 1, App 3, Data 2, Field 2).
Closing line under the board: <mark>One person, Meera, keeps all four teams on the same plan.</mark>
Below 820px: one card per problem with its team chips in an ANSWERED BY footer.

## SECTION 6 · frag-6-roads.html · prefix road- · Builder D
Pattern: CHG-37 two roads from today. Band: t3 (redline wash).
- BADGE truckBadge('trip'), label: ASK 3 · THE TRIP
- h2: Two ways this summer can go
- lede: Last summer, some buyers turned away loads they said arrived warm.
Visual (SVG ~900x420): a dot labelled TODAY at left; two roads leave it. Upper road ("if nothing changes"):
muted dashed line that thins and fades, ending on text. Lower road ("with the pilot"): solid ink, ending on text
with a marker highlight. Then a hand-drawn red ring loops around the split point with a hand label "you choose here".
Sequence on scroll through the section (or in-view steps): wait road first, then the pilot road, then the ring.
Road end texts (put them in HTML positioned beside the road ends, not long SVG text):
- If nothing changes: Loads still get turned away at the door, and there is still no record to show what happened.
- With the pilot: <mark>Every load arrives with its own temperature record,</mark> ready to show any buyer.
chips under the pilot text: Data, App
Below 768px: two stacked cards, dashed border then ink border.

## SECTION 7 · frag-7-cta.html · prefix cta- · Builder D
Pattern: PPL-28 three pictured steps that end at one person, PPL-27 contact card, PPL-01 drawn portrait
(adapted: no kolam braid; instead the portrait sits inside a drafting "DETAIL A" circle: a thin circle with
small tick marks around it like a protractor and a label DETAIL A). Band: dark.
- h2: How we start
- lede: Three small steps, starting with one route.
Three cards, each with a small line drawing at top (stroke var(--paper), marker accents):
1. Pick one route · drawing: a short list KOCHI → BENGALURU / KOCHI → CHENNAI / KOCHI → COIMBATORE with a yellow
   pen ring (EMP-10 path) drawn around the first · text: We suggest Kochi to Bengaluru. It is your longest night run.
2. Talk to one person · drawing: a small portrait disc with signal arcs · text: Meera Nair runs the pilot from start to end. She is your one point of contact.
3. Get a one-page plan · drawing: a sheet with a title block and a yellow tick · text: Within a week you get a one-page plan for the pilot route: which trucks, which stops, and what you will see.
Then the contact card (light, radius 22px, max-width 820px): the portrait (a calm line drawing of a woman with
shoulder-length hair, drawn in a few ink strokes on var(--card), pen-drawn on view, never a generic avatar or
emoji face), label YOUR TIDEWATER CONTACT, name Meera Nair, line Project lead, Tidewater Studio, line
Send her the route you pick. She replies with the one-page plan within a week., the email in a mono pill
meera.nair@tidewater.example (user-select: all), and a Copy email button (navigator.clipboard with a select
fallback; label becomes Copied for 1.8s; clear the old timer first).
Footer line (small, muted, below the card): Sample proposal made with the pitch-site prototype. Coastline Cold Chain, Tidewater Studio and Meera Nair are fictional.

---

## Builder assignments
- Builder A: frag-1-hero.html, frag-2-echo.html
- Builder B: frag-3-stage.html
- Builder C: frag-4-paper.html, frag-5-switch.html
- Builder D: frag-6-roads.html, frag-7-cta.html
Write only your own files (plus your test-X.html and shot-X*.png). When done, report in 5 lines: what you
built, what you checked in screenshots, and anything still wrong.
