# Architecture: whole-page structures and frame devices

Pattern library family for `pitch-site`. 33 entries (7 starred): 20 whole-page structures (ARC-01 to ARC-19, plus ARC-33) and 13 frame devices (ARC-20 to ARC-32). Curated from slice6, architecture family (38 raw entries), plus three entries moved over from the motion family (P356, P358, P360) and the TVS page skeleton.
Verdicts: 5 KEEP, 23 ADAPT, 4 NEW, 4 CUT (listed at the end).

**How to read a structure entry.** The first line of Build starts with "Map:", which places the proposal's four parts (the reader's asks, what we offer, examples, the ask) onto the structure. "Use when" says whether reading is strictly sequential. "Avoid when" names the risk to clarity. "Narrow" says how it degrades on a tablet (landscape, then portrait below 820px, then the stacked static twin below 768px; phones get the gate, ARC-27).

**Shorthand (house motion values):**
- **pen draw**: `stroke-dashoffset` from length to 0; length / 600 px/s, clamped 0.6-2.2s; next stroke at 80-85% of the previous; cubic-bezier(.45,.05,.35,1).
- **arrive**: opacity plus a rise of 16px or less, 0.6-1.0s, cubic-bezier(.22,1,.36,1); once; always finishes. Staggers 60-110ms, capped at 450ms.
- **scroll-linked**: linear, 1:1 with native scroll. No smooth-scroll library, no snapping on reading sections, no loaders.
- **pinned**: a sticky stage whose section is 3 viewport heights or less, with an n / N counter (ARC-29) and a static twin below 768px.
- **finished state**: reduced motion, repeat visits and `?final=1` land on every drawing finished (ARC-24).
- Every page is read top to bottom, once, in one order. No role pickers, no choose-your-own path, no auto-advancing anything. The first frame is a full-screen hero with nothing from the next section showing. The page ends in the ask.

**Cross-family overlaps to settle at assembly:** ARC-02 and order-time SEQ-02 / change-choice CHG-02 (pinned stage as a section device); ARC-03 and structure-links STR-24 (pinned build-up drawing); ARC-05 and STR-10 (constellation in chapters); ARC-06 and people PPL-16 ("You told us" echo); ARC-28 and SEQ-21 (chapter rail). The sibling entries are section devices; these are page skeletons.

---

## Picker: content and audience to structure

Starred first. Every structure also carries the frame kit below.

- **The client gave 3-6 separate asks; mixed audience; they will scroll once**: ARC-01 ★, ARC-05 ★, ARC-06.
- **One system or one place explains the whole offer**: ARC-02 ★, ARC-03 ★, ARC-07.
- **The offer changes a routine, a place or a workflow (before and after)**: ARC-04 ★, ARC-02 ★, ARC-07.
- **The offer's parts depend on each other and add up to a whole**: ARC-03 ★, ARC-05 ★, ARC-19.
- **We read their brief or plan and are answering it**: ARC-06, ARC-13, ARC-04 ★.
- **Diagnosis or audit (symptoms, root cause, fix)**: ARC-12, ARC-09, ARC-13.
- **An abstract idea with 3-6 parts that differ in kind (values, a framework, a mental model)**: ARC-33 ★, ARC-12.
- **A programme over time (onboarding, a pilot, the first 90 days)**: ARC-11, ARC-16, ARC-14.
- **Place matters (several sites, a region, a campus)**: ARC-10, ARC-11, ARC-08.
- **A big system that must feel personal first**: ARC-08, ARC-09, ARC-15.
- **The story is about one person (a student, a farmer, their customer)**: ARC-14, ARC-15, ARC-08.
- **A busy senior reader with two minutes who expects a deck**: ARC-20 ★, ARC-17, ARC-18.
- **Value stacking, scope or price is the argument**: ARC-19, ARC-18.

**Frame kit every page carries:** ARC-20 ★ headline spine, ARC-21 reading order, ARC-22 fade-up, ARC-23 list twins, ARC-24 finished-state switch, ARC-25 sleeping loops, ARC-27 phone gate, ARC-29 counters on any stage. Add ARC-28 when the page runs past 6 screens.

---

## Whole-page structures

### ARC-01 ★ One long scroll with section colour blocks (baseline)
- For: grouped-list, sequence · 8-13 bands, 3-6 asks
- Instead of: a PDF proposal pasted into a web page
- Reader sees: a full-screen dark hero whose motif draws itself, then one flat-tinted band per idea down the page, each opening with a claim headline, dark doorstep bands at the key turns, and a pictured three-step close with a named contact.
- Moves: load (hero draw-on), then in-view per band - each band brings one signature visual; reveals and draws on house values; nothing pins unless a band chooses a stage.
- Build: Map: hero (the promise) → their asks as cards → the key (the motif decoded, one part per ask) → one band per ask with the same inner order (badge, their words, visual, problem → who answers → outcome) → the cross-cutting idea (dark) → the whole picture (constellation) → 1-2 worked examples → the ask (dark: three pictured steps and a named contact).
  Bands and tints per MOT-21 (`.band`, `.wrap`, `.woodbg`); TVS order: dark doorsteps at bands 1, 3, 8 and the last, washes between.
  Give each ask band its own signature visual (snake, translator, ladder) so the repeated inner order never feels samey.
- Narrow: tablet landscape keeps everything; below 820px single column, diagrams swap to list twins (ARC-23) and the snake becomes a left rail; below 768px every pinned or scrubbed piece shows its static twin · Reduced motion: every drawing finished, no reveals.
- Use when: 3-6 separate asks, a mixed audience, and a reader who scrolls once top to bottom. Sequential: yes, strictly. · Avoid when: the content fills under 5 screens (bands feel padded). Risk: length (TVS ran 12 bands); every headline must be a claim so a skimmer still gets the deal.
- Effort: M · Needs lib: no · Code: TVS harvest (Part 2 shell and helpers, Part 3 system and page skeleton) · Sources: P035, TVS site page.html (01-tvs-harvest Part 3, "Page skeleton, in order") · Verdict: KEEP (the proven baseline)

### ARC-02 ★ One pinned stage, captions scroll past
- For: sequence, part-whole · 3-5 steps per stage, 1-2 stages per page
- Instead of: one diagram per point, each with its own paragraph
- Reader sees: one line-drawn subject (their plant, their week) holds still while short captions scroll past; each caption changes exactly one thing in the drawing, and a small "02 / 05" says where they are.
- Moves: scroll-triggered steps, each played once (MOT-09); the step vocabulary is hue arriving (MOT-04), pull-back (MOT-05), match-cut (MOT-08), morph (MOT-07); the stage releases after its last step.
- Build: Map: step 1 = the subject as it is today with their ask named on it; steps 2-4 = what we offer, one change each; examples follow in normal bands after the release; the ask comes after the stage, never inside it.
  Laptop layout: side by side (stage `position: sticky; top: 10svh; height: 80svh`, captions in a 40% column), or a full-bleed stage with caption cards (`max-width: 34ch`, 92% paper) when the drawing is wide. One IntersectionObserver with `rootMargin: "-45% 0px -45% 0px"` writes `data-step`; step spacing 55-60svh in px from `innerHeight`.
  Pin 3 viewport heights or less, so 5 steps at most; a second stage needs a normal reading band before it.
- Narrow: tablet landscape keeps side by side; below 820px the stage pins to the top 50svh with captions as solid paper cards beneath; below 768px the static twin (one drawing per step, each with its caption) · Reduced motion: each step's end state, no transitions.
- Use when: one drawing can carry the argument (Ash's Washington Post reference). Sequential: yes, strictly. · Avoid when: each point needs a different picture. Risk: captions laid over drawings get skipped, and a stage that never releases reads as broken.
- Effort: M · Needs lib: no · Sources: P385 https://pudding.cool/process/responsive-scrollytelling/, P102 https://github.com/russellsamora/scrollama, P386 https://pudding.cool/process/how-to-implement-scrollytelling/, P457 (video-anim-study, sticky stage keys), P103 (merged as the full-bleed layout) · Verdict: ADAPT, changed: five sticky-stage entries merged; one change per step; pin capped at 3 viewport heights; counter added; static twin below 768px.

### ARC-03 ★ Cumulative assembly
- For: part-whole, sequence · 4-8 sections, one part each
- Instead of: a feature list followed by an architecture diagram
- Reader sees: every section shows the same machine drawing with one more part drawn in; explained parts sit in ink and parts still to come are faint guides, so by the end the whole offer stands built in front of them.
- Moves: in-view per section (not pinned) - the new part pen-draws in the accent, then settles to ink when the next section arrives; the last section runs one pulse through the finished machine (MOT-01).
- Build: Map: each section opens with one ask in their words; the part that answers it is drawn into the machine; one small "seen at" example card per part; the last section shows the whole machine working, then the ask.
  One master SVG `<symbol>`; each section embeds a `<use>` with `data-show="n"`: parts 1 to n-1 in ink, part n drawn in the accent, later parts as dash-dot guides (`.93 2.8 9.35 2.8`) at 22% ink. Part names in the copy carry chips in the part's chalk tint.
- Narrow: inline drawings scale with their viewBox on tablets; below 768px each drawing is static with the new part ringed · Reduced motion: finished drawings, new part ringed.
- Use when: the offer's parts depend on each other (problem, the part that fixes it, repeat). Sequential: yes, strongly. · Avoid when: the parts are unrelated. Risk: length; it needs claim headings and a drawing simple enough to read at 600px wide.
- Effort: L · Needs lib: no · Sources: P387 https://ciechanow.ski/mechanical-watch/ · Verdict: ADAPT, changed: future parts shown as faint guides; one accent for the new part; closing pulse leads into the ask.

### ARC-04 ★ Mirror halves (today, then with us)
- For: before-after, comparison · 3-5 paired sections
- Instead of: a "Problem" section and a "Solution" section in different layouts
- Reader sees: the first half walks through their day as it is, in ink on bare paper; a pivot screen wipes "today" into "with us"; the second half replays the same scenes in the same layout, now in colour, with the offer in place.
- Moves: in-view - the same reveals in both halves; at the pivot a scrubbed wipe (MOT-03); in the second half each scene's hue arrives (MOT-04).
- Build: Map: each "today" scene names one ask as a pain in their words; its mirror shows the same scene fixed by our offer; one example per mirrored scene; the ask closes the second half.
  Two sets of sections with matched markup (`today-3`, `after-3`). The "today" half uses ink and paper only, so colour itself signals the offer. Keep "today" under 40% of the page.
- Narrow: same order on tablets; below 768px the pivot wipe becomes a stacked labelled pair · Reduced motion: no wipe, hues present.
- Use when: the offer changes a routine, a place or a workflow. Sequential: yes. · Avoid when: the change is invisible or purely financial. Risk: the grey half can feel dull and readers may leave before the payoff; keep each "today" scene to one screen.
- Effort: M · Needs lib: no · Sources: P403 https://emilkowal.ski/ui/the-magic-of-clip-path · Verdict: ADAPT, changed: the grey half became ink on paper; colour arrives hue by hue as the proof of change.

### ARC-05 ★ Map between chapters (new)
- For: part-whole, place-network · 3-6 chapters
- Instead of: a sticky table of contents
- Reader sees: the page opens with a faint map of the whole offer, one numbered node per ask; between chapters the same map returns for half a screen with the finished branch now inked and the next node circled in pen ("next: suppliers"); at the end the whole map is inked and its centre becomes the contact.
- Moves: in-view per interstitial - the finished branch pen-draws from guide to ink, then the next node gets a pen ring (0.6s); on the closing map one pulse runs along each branch toward the centre (MOT-01), then the centre opens into the contact card.
- Build: Map: asks = numbered branch nodes; offer = leaves inked chapter by chapter; examples = leaves marked with a small star ("seen in the pilot"); the ask = the centre node.
  One data array renders the opening map, every interstitial and the list twin (TVS constellation code with `data-done` and `data-next` per branch). Interstitials are 50-60svh, unpinned. Hover or tap on a branch dims the others.
- Narrow: the map scales on tablets; below 820px the list twin with finished items ticked and the next one underlined · Reduced motion: each interstitial shows its finished state.
- Use when: several asks belong to one picture and the reader needs to know where they are in the whole. Sequential: yes; the numbered map shows the order and offers no jump links. · Avoid when: more than 6 chapters (the map crowds). Risk: repetition; keep interstitials short and change one branch each time.
- Effort: M · Needs lib: no · Code: TVS harvest (2.3 constellation, base for the map) · Sources: new; built on the TVS constellation mind map (01-tvs-harvest 2.3, P039 list twin) and the Anthropic moving mind map · Verdict: NEW

### ARC-06 Asked and answered (new)
- For: proof-trust, comparison · 3-6 asks
- Instead of: restating the brief in our own words
- Reader sees: each ask appears in the client's own words as a quoted card on the left; a pen line draws across to our answer card on the right (one sentence and a small drawing); the ask gets a tick; the last pair reads "What you need from us now" with the contact.
- Moves: in-view per pair - the quote arrives (0.8s); the connector pen-draws; the answer arrives at 80% of the draw; the tick draws last (0.4s).
- Build: Map: asks = left cards quoting the brief or the meeting (date and speaker in mono); offer = right cards; examples = a "seen at" line under each answer; the ask = the final pair.
  Pairs of cards in a two-column grid with a short SVG connector between; no table markup and no grid rules; 3-6 pairs, then a closing band.
- Narrow: tablets keep two columns above 820px; below 820px each answer stacks under its ask and the connector becomes a short vertical pen stroke · Reduced motion: all pairs present, ticks drawn.
- Use when: the client wrote a brief or said specific things you can quote. Sequential: yes. · Avoid when: the asks were vague (quotes would expose that). Risk: it reads like a compliance checklist if answers run past two sentences.
- Effort: S · Needs lib: no · Sources: new; built on the TVS "You told us" echo block (01-tvs-harvest Part 1) · Verdict: NEW

### ARC-07 One object that transforms
- For: before-after, part-whole · 3-5 states
- Instead of: screenshots of the deliverable
- Reader sees: one thing the reader owns (their shop front, their monthly report, their onboarding kit) sits centre-stage and changes chapter by chapter: cluttered, cleaned, connected, growing.
- Moves: per step on a pinned stage - the change plays by morph (MOT-07) or hue (MOT-04); one change per step.
- Build: Map: state 1 = the object today with each ask labelled on it; states 2-4 = each part of the offer applied; examples = real photos after the pin releases; the ask = the finished object tagged "yours from <month>" with the contact.
  Sticky object plus caption steps (ARC-02 mechanics); states as cumulative SVG groups; pin 3 viewport heights or less.
- Narrow: tablet portrait pins a smaller object to the top 50svh; below 768px one card per state · Reduced motion: each state's end, crossfades only.
- Use when: the offer transforms one concrete thing the reader recognises. Sequential: yes. · Avoid when: the change is abstract. Risk: a reader who sees no motion sees only the end state, so caption every state.
- Effort: L · Needs lib: no · Sources: P388 https://css-tricks.com/lets-make-one-of-those-fancy-scrolling-animations-used-on-apple-product-pages/ · Verdict: ADAPT, changed: frame sequences replaced by SVG states; pin capped; the ask sits on the finished object.

### ARC-08 Pull-back structure
- For: part-whole, big-idea · 3-4 zoom levels
- Instead of: opening with the org chart
- Reader sees: the page opens on one small human detail and each chapter steps back: one order, one day, one plant, the whole company, with labels arriving at each level.
- Moves: scroll-linked between levels - scale steps 3 → 2 → 1.4 → 1, each over under one viewport height, linear; labels arrive after each step (MOT-05); normal reading bands between levels.
- Build: Map: the first detail = the reader's ask made personal; each level adds what we offer at that scale; examples are labelled inside the drawing; the final full view carries the ask.
  One large SVG with `vector-effect: non-scaling-stroke`; each level sets `--scale` and `--origin`; total pinned length 3 viewport heights or less, split by the reading bands.
- Narrow: tablets swap live scaling for one crop per level; below 768px static crops stacked · Reduced motion: crossfades between crops.
- Use when: a big system should feel personal first. Sequential: yes. · Avoid when: the drawing cannot hold detail at 3×. Risk: zoom discomfort; keep to 3-4 levels.
- Effort: L · Needs lib: no · Sources: P402 https://developer.chrome.com/docs/css-ui/scroll-driven-animations · Verdict: ADAPT, changed: capped at 4 levels; pins split by reading bands; non-scaling strokes.

### ARC-09 Nested zoom (scene inside a scene)
- For: hierarchy, cause-effect · 3-4 levels
- Instead of: a root-cause paragraph
- Reader sees: each chapter is found inside the previous one: from the company, into a team, onto one desk, into one screen where the problem lives; a breadcrumb at the top keeps their place.
- Moves: scroll-linked - scale into a marked spot over under one viewport height per level, linear; the next scene pen-draws at full zoom; the breadcrumb's new segment arrives (0.3s).
- Build: Map: level 1 = their ask at company level; the deepest level = the root cause, where the offer acts; one pull-back then shows the fix spreading up, with an example at each level on the way out; the ask sits at the top level.
  Each scene is an SVG with a target rect; zoom by `transform: scale()` with the origin at the target; breadcrumb in mono ("Company › Plant › Line 3 › Tablet").
- Narrow: tablets crossfade between scenes with an "inside this" caption; below 768px scenes stacked · Reduced motion: crossfades with captions.
- Use when: diagnosing a root cause ("the problem lives here"). Sequential: yes. · Avoid when: more than 4 levels. Risk: vestibular discomfort, and readers lose their place without the breadcrumb.
- Effort: L · Needs lib: no · Sources: P391 https://blacknerdproblems.com/looking-at-the-infinite-canvas-and-digital-comics/ · Verdict: ADAPT, changed: capped at 4 levels; breadcrumb required; one pull-back out to the ask.

### ARC-10 One drawing, a window per chapter
- For: place-network, sequence · 4-8 chapters
- Instead of: a map image with numbered pins and a legend
- Reader sees: one large line drawing of the client's world (a map, a site plan, a campus) frames each chapter through a window; as a chapter arrives the view glides from the last window to this one, and the last chapter shows the whole drawing with every visited place inked.
- Moves: in-view per chapter (not pinned) - the SVG `viewBox` tweens from the previous window to this one over 1.0-1.4s cubic-bezier(.45,.05,.35,1); the place's detail then pen-draws; a mini locator shows where the window sits.
- Build: Map: asks = the places where each problem lives; offer = what gets drawn into each place; examples = annotated spots; the ask = the whole drawing with the contact.
  One SVG source reused per chapter through `<use>`; each chapter stores its window rect; tween `viewBox` in rAF on the house curve. No map service, no tiles.
- Narrow: windows scale on tablets; below 768px static crops with the locator · Reduced motion: jump cuts with a 0.4s crossfade.
- Use when: logistics, territory, multi-site or campus proposals. Sequential: yes. · Avoid when: places do not matter to the argument. Risk: long glides disorient; keep each under 1.5s.
- Effort: L · Needs lib: no · Sources: P390 https://github.com/mapbox/storytelling · Verdict: ADAPT, changed: Mapbox replaced by one SVG drawing with viewBox tweens; unpinned; ends on the whole view.

### ARC-11 Route on a pinned map
- For: time-roadmap, sequence · 4-6 stops per leg
- Instead of: a horizontal timeline strip
- Reader sees: a route drawn on a pinned map from today to the goal, which is already marked with their ask; as captions scroll, a marker moves stop to stop, each finished segment turns from dotted guide to ink, and a counter reads "Day 30 / 90".
- Moves: per step - the marker moves along `offset-path` over 1.0-1.4s cubic-bezier(.45,.05,.35,1); the segment inks as it goes; the counter updates (0.25s).
- Build: Map: the destination flag = what they asked for; stops = what we deliver in each phase; small sketches at the stops = examples; the ask = "Step 1 starts here" at the start line, revisited at the end.
  Pinned stage (ARC-02 mechanics) with the route as guide and ink paths (MOT-02); 4-6 stops per pin; a longer programme splits into two legs with a reading band between. The road stays on the map and never runs behind the copy.
- Narrow: tablet portrait pins the map to the top half; below 768px the route straightens into a left rail of stops · Reduced motion: route inked to the current stop, marker at the stop.
- Use when: onboarding, a pilot, a programme over months. Sequential: yes, the clearest metaphor for it. · Avoid when: the stops are not truly ordered. Risk: scenery upstaging the stops; keep the map to line work.
- Effort: L · Needs lib: no · Sources: P392 https://joshworth.com/dev/pixelspace/pixelspace_solarsystem.html · Verdict: ADAPT, changed: the page-long road moved onto a pinned map (Ash rejected lines running through the copy); legs capped at 6 stops.

### ARC-12 Descent with a depth gauge
- For: cause-effect, hierarchy · 4-7 layers
- Instead of: a findings list
- Reader sees: the page is a dive: surface symptoms at the top on paper, each section a shade deeper in warm brown, a gauge on the left marking depth, the root cause at the bottom, and the fix climbing back up to light paper and the ask.
- Moves: scroll-linked - gauge fill `scaleY` on `scroll()`, linear; section tints stay flat and change at section edges.
- Build: Map: their asks are the surface symptoms; the root cause sits in the deepest band; the offer is the climb back, one band per fix; examples sit at mid-depth on the way up; the ask is back at the surface.
  Tint ramp from paper to dark wood (no navy); fixed gauge with labelled ticks at section starts and a depth counter; check contrast on every band.
- Narrow: tablets keep the gauge as a thin left rail; below 768px it becomes the top reading ruler (ARC-28) · Reduced motion: gauge static per section.
- Use when: audits and diagnostics (symptom, root cause, fix). Sequential: yes. · Avoid when: the client is sensitive about "how deep the problems go". Risk: dark bands need contrast checks, and the descent must never outweigh the climb.
- Effort: M · Needs lib: no · Sources: P393 https://webkit.org/blog/17101/a-guide-to-scroll-driven-animations-with-just-css/ · Verdict: ADAPT, changed: ramp in warm browns with flat tints (no colour crossfades); the climb back to paper ends in the ask.

### ARC-33 ★ Expedition through a living metaphor (new)
- For: definitions-jargon, hierarchy, part-whole, mental models · 3-6 parts
- Instead of: values, a framework or a mental model drawn as labelled layers, rings or a stacked diagram
- Reader sees: one world (a sea, a forest, a sky) that the reader travels through with one verb (dive, climb, dig); at each stop a creature or object switches on whose real behaviour is the idea (a nautilus living in the newest chamber it built is identity), with one line beside it; the journey ends with the whole metaphor lit at once.
- Moves: one eased camera move per stop (the `viewBox`, 650-1500ms); parts switch on in a stepped flicker; words write in whole, about 40ms apart; the vehicle and a depth gauge hold still on screen.
- Build: Map: the thesis opens the journey; each part of the idea is one stop, in a told order; examples are the creatures' real facts; the finished picture returns the thesis and leads to the ask.
  Method, casting bank and mechanics in `../story-plan/references/living-metaphors.md`; plan it with that skill's storyboard. Tall SVG (1600 × 1800) seen through a 1600 × 900 viewBox; gauge lists every stop at rest; drive by scroll or one forward control, never scattered hotspots.
- Narrow: same scene inside a sideways-panning frame; the gauge stays · Reduced motion: full height at once, every part lit, every line written.
- Use when: the subject is abstract and has 3-6 parts that differ in kind. Sequential: yes. · Avoid when: a creature's link to the idea needs a paragraph; the parts are numbers (use AMT); the client's world has no natural place for the metaphor. Risk: clip art if worlds mix; clicky if the reader must hunt.
- Effort: L · Needs lib: no · Sources: The Range, Mauna Kea dive (2026-10-19), `../story-plan/assets/examples/range-src/` · Verdict: NEW, loved by Ash.

### ARC-13 Annotated document
- For: proof-trust, emphasis · 1 document, 4-8 marked passages
- Instead of: "We reviewed your plan and found..."
- Reader sees: their own plan or brief set as one clean page, marked up as they read: circles, underlines, margin notes in a hand face, strike-and-replace edits, arriving in order.
- Moves: in-view per passage - pen marks draw in sequence (MOT-12); margin notes arrive (0.8s); an edit strikes with a pen line, then the replacement arrives.
- Build: Map: the asks are their own lines, circled; the offer is the margin notes and replacements; examples are small margin sketches; the ask is a handwritten note at the end, signed by the named contact.
  Tufte-style wide right margin (`grid-template-columns: minmax(0, 62ch) 1fr`); notes anchored to passages; one accent for every mark; at most one mark per screen.
- Narrow: tablet landscape keeps the margin; below 820px notes move inline as tinted strips under their passage · Reduced motion: every mark present.
- Use when: audits, plan reviews, "we read what you sent". Sequential: yes. · Avoid when: you have no document of theirs to mark. Risk: it looks like a corrected exam if marks pile up.
- Effort: M · Needs lib: no · Sources: P399 https://edwardtufte.github.io/tufte-css/ · Verdict: ADAPT, changed: Rough Notation replaced by vanilla pen marks; one mark per screen; a signed close.

### ARC-14 Comic strip panels
- For: sequence, people-roles · 6-10 panels
- Instead of: a persona paragraph
- Reader sees: the story told in line-drawn panels down the page: a person, a problem, a turn, a result, each panel with one caption; longer gaps between panels mean time has passed.
- Moves: in-view per panel - the panel's line art pen-draws (0.8-1.6s); its caption arrives at 80% of the draw.
- Build: Map: panels 1-3 = their asks as moments in one person's day; the turn panel = our offer arriving; result panels = examples; the last panel = the person pointing to the contact card.
  A vertical strip of SVG panels with HTML captions; gutter length sets the pace; one drawing hand for every panel; never horizontal.
- Narrow: native on tablets (vertical strips suit narrow screens); panels go full width below 820px · Reduced motion: panels drawn.
- Use when: explaining a customer or student journey to readers who will not read. Sequential: yes. · Avoid when: you cannot draw consistently. Risk: it can feel childish to senior B2B readers.
- Effort: L · Needs lib: no · Sources: P400 https://blacknerdproblems.com/looking-at-the-infinite-canvas-and-digital-comics/ · Verdict: ADAPT, changed: panels pen-draw; vertical only; the last panel is the ask.

### ARC-15 Guided tour with one character
- For: people-roles, sequence · 5-8 chapters
- Instead of: generic "you" copy
- Reader sees: one simple drawn figure (the reader's customer, a student, a supervisor) stands beside every chapter heading, pointing at what matters and reacting as things change.
- Moves: in-view per chapter - the pose swaps by a 0.3s crossfade; a pointing arrow pen-draws (0.6s); the figure never slides in from the side.
- Build: Map: the character's problems are the asks; what changes for them is the offer; scenes of them using it are the examples; at the close they hand over the contact card.
  One SVG character with 4-6 pose groups; each chapter sets `data-pose`; the character never says more than the copy.
- Narrow: tablets shrink the figure to a corner badge beside headings · Reduced motion: pose swaps with no crossfade.
- Use when: the story is about a person. Sequential: yes. · Avoid when: the audience is senior and formal. Risk: a cute guide can upstage or trivialise the offer; test the tone.
- Effort: L · Needs lib: no · Sources: P395 https://github.com/ncase/trust · Verdict: ADAPT, changed: side slides removed; the pointer is a pen draw.

### ARC-16 Chapter covers with a progress motif
- For: sequence · 4-6 chapters, 10+ screens
- Instead of: a long page with no felt chapters
- Reader sees: each chapter opens with a full-screen cover (big numeral, claim headline, one small drawing) that shrinks into a slim header ("2 / 5 · Suppliers") as they read on; a motif in the header gains one part per chapter.
- Moves: scroll-linked - cover height 100svh down to a 48px header, linear, over the chapter's first 90svh; the header motif's new part pen-draws when the chapter enters.
- Build: Map: cover 1 (the hero) = what you asked; covers 2-4 = the offer, need by need; cover 5 = examples; the last chapter = the ask.
  A fixed header with `body` padding compensation (sticky would steal scroll distance); `animation-timeline: scroll()` with an rAF fallback; header 48px at most.
- Narrow: covers drop to 70svh on tablet portrait and the header shows only "2 / 5"; below 768px static headers · Reduced motion: static slim header, full covers.
- Use when: long proposals over about 10 screens. Sequential: yes. · Avoid when: under 6 screens (covers feel pompous). Risk: covers add scrolling, and a fixed header steals height on landscape tablets.
- Effort: M · Needs lib: no · Sources: P396, P358 https://scroll-driven-animations.style/demos/cover-to-fixed-header/css/ · Verdict: ADAPT, changed: merged with the cover-shrink motion entry; header capped at 48px; the motif grows by pen draw.

### ARC-17 One idea per screen
- For: sequence, big-idea · 6-12 screens
- Instead of: a PDF deck attached to an email
- Reader sees: one sentence and one drawing per screen, each screen full height, like a deck they scroll through.
- Moves: in-view per screen - picture, then headline, then detail (ARC-21); native scroll with no snapping.
- Build: Map: screen 1 = the promise; one screen per ask; one per part of the offer; one per example; the last screen = the ask with a named person.
  Sections `min-height: 100svh`, content centred; two sentences at most per screen; no `scroll-snap` (Ash's rule: no snapping on reading sections).
- Narrow: tablet landscape keeps full-height screens; portrait uses min-height 80svh; below 768px plain content-height sections · Reduced motion: everything visible.
- Use when: a senior reader expects a deck and has two minutes. Sequential: yes. · Avoid when: screens would hold uneven amounts of text. Risk: it can feel thin; every screen still needs a claim headline.
- Effort: S · Needs lib: no · Sources: P397 https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_scroll_snap/Basic_concepts · Verdict: ADAPT, changed: snapping removed; picture, headline, details order added.

### ARC-18 Stacking deck
- For: sequence · 4-6 chapter cards
- Instead of: equal sections separated by dividers
- Reader sees: each chapter is a card that scrolls normally; once its end is reached the next card slides up over it, and the earlier cards wait as a slim pile of title strips at the top, a physical sense of progress.
- Moves: scroll-linked - the covered card scales to .96 and dims to 85% across the overlap, linear; nothing else moves.
- Build: Map: card 1 = their asks; cards 2-4 = the offer; card 5 = examples; the last card = the ask, which nothing covers.
  Each card `position: sticky; top: min(0px, calc(100svh - var(--h)))` with `--h` measured in JS, so a tall card is read in full before the next slides over it; the pile shows title strips at 12px offsets. All motion is tied to native scroll.
- Narrow: tablets keep it with cards up to one screen tall; below 768px plain stacked sections · Reduced motion: plain sections.
- Use when: short proposals with 4-6 chunky chapters. Sequential: yes. · Avoid when: chapters run past about 1.5 screens. Risk: readers cannot glance back without scrolling up.
- Effort: M · Needs lib: no · Sources: P398 https://scroll-driven-animations.style/demos/stacking-cards/css/, P356 (merged from motion) · Verdict: ADAPT, changed: cards stick only after they are fully read; the pile shows titles; the final card stays uncovered.

### ARC-19 Running receipt
- For: quantity-scale, part-whole · 5-8 sections
- Instead of: a pricing table at the end
- Reader sees: a slim receipt at the side; every section they pass prints a line (what they get and its value) and the total ticks up; the last section shows the full receipt and the ask.
- Moves: in-view per section - the line prints by a 0.25s clip; the total counts over 0.8s cubic-bezier(.22,1,.36,1) (MOT-10).
- Build: Map: each ask's answer prints as a line; examples print as "included" lines; the total and the ask close the page.
  A fixed receipt panel (220px wide, mono, paper surface); sections carry `data-line` and `data-value`; an ordered queue makes sure lines always print in page order.
- Narrow: tablet portrait shows only a bottom bar with the total; below 768px no panel, and the full receipt sits at the end · Reduced motion: lines present, total final.
- Use when: value stacking with real, defensible numbers. Sequential: yes. · Avoid when: the values are soft or speculative. Risk: a fixed panel costs reading width and gives the eye a second thing to watch.
- Effort: M · Needs lib: no · Sources: P401 https://css-tricks.com/animating-number-counters/ · Verdict: ADAPT, changed: house count curve; ordered print queue; panel dropped below 768px.

---

## Frame devices

### ARC-20 ★ Headline spine
- For: hierarchy, utility · 6-12 sections, every page
- Instead of: topic headings such as "About us" or "Our approach"
- Reader sees: big claim-shaped headings that tell the whole story in order; under each, one visual and at most two sentences.
- Moves: in-view - heading, then visual, then body (ARC-21).
- Build: write the headings first as a stand-alone script and read it aloud; if the headings alone sell the deal, build. Each heading front-loads the key word and states an answer.
  Reuse the same words for chapter bar names, map labels and counter captions, so wayfinding repeats the story.
- Narrow: native · Reduced motion: static.
- Use when: always, under any structure. Sequential: yes. · Avoid when: n/a. Risk: weak, topic-only headings push readers into the slower F-pattern.
- Effort: S · Needs lib: no · Sources: P404 https://www.nngroup.com/articles/layer-cake-pattern-scanning/ · Verdict: KEEP

### ARC-21 Picture, then headline, then details
- For: utility, hierarchy · every section with a visual
- Instead of: everything in a section fading in together
- Reader sees: in each section the picture settles first, the headline lines rise next, and only then the small facts appear, so the eye always knows where to start.
- Moves: in-view, once - picture fades over 0.7s and scales 1.06 to 1 over 1.0s cubic-bezier(.22,1,.36,1); headline lines rise from masks from 0.2s, 80ms apart; body from 0.35s; detail chips rise 12px from 0.45s, 60ms apart; each group's stagger capped at 450ms. Scrolling back up shows everything (no reverse play).
- Build: one timeline per section through custom properties: each element gets `--t` and `.in` sets `transition-delay: var(--t)`; line masks per MOT-13. A drawing that pen-draws takes the picture slot.
- Narrow: same order, delays ×0.7 · Reduced motion: all visible.
- Use when: every content section. · Avoid when: the section has no visual (use the plain fade-up).
- Effort: S · Needs lib: no · Sources: P422 https://jithinrp.com/site.js · Verdict: ADAPT, changed: the 35ms body stagger raised to the house 60ms minimum; the in-out picture scale moved to the arrival curve.

### ARC-22 Below-the-fold fade-up, once
- For: utility · every block below the fold
- Instead of: an animate-on-scroll library that fades everything, the hero included
- Reader sees: blocks rise a few pixels and fade in as they arrive; anything visible at load is simply there; nothing moves again.
- Moves: in-view, once (threshold .15, bottom margin -6%) - opacity 0 to 1 and translateY 12px to 0 over 0.8s cubic-bezier(.22,1,.36,1); siblings 80ms apart, capped at 450ms.
- Build: JS adds `.pre` only to elements whose top sits below 95% of the viewport at load, then removes it with a one-shot IntersectionObserver; without IntersectionObserver nothing is hidden. Add the `js` class only when motion is allowed, so no reader without JS loses content. Under `html.final` (ARC-24) `.pre` is never added.
- Narrow: same · Reduced motion: nothing hidden, no transitions.
- Use when: always, as the baseline motion. · Avoid when: above the fold (render it visible).
- Effort: S · Needs lib: no · Code: TVS harvest (2.1) · Sources: P034 (TVS site, page.html ~L44-46, L932-936), P442 https://aicommon.creamu.co.jp · Verdict: ADAPT, changed: merged; TVS's .75s on (.25,1,.5,1) moved to the house arrival at 0.8s; stagger capped.

### ARC-23 Diagram with a list twin
- For: utility · every absolutely positioned diagram
- Instead of: a diagram squeezed until its labels are unreadable
- Reader sees: on a laptop, the map or orbit; on a narrow screen, a clean stacked list with exactly the same words.
- Moves: none (a static swap).
- Build: render both from one data array (map to `#map-list` sections; orbit to `<ol class="orbit-list">` cards); CSS swaps them at 820px (`#constellation { display: none }` with `.map-list { display: grid }`).
  Stop every loop on the hidden diagram (the TVS pulses kept running while hidden).
- Narrow: this is the fallback · Reduced motion: n/a.
- Use when: a diagram uses absolute positions or a viewBox containing text. · Avoid when: the diagram stays legible when scaled.
- Effort: S · Needs lib: no · Code: TVS harvest (2.3, 2.5) · Sources: P039 (TVS site, page.html ~L199, L246-250, L340, L417-422) · Verdict: KEEP

### ARC-24 Finished-state switch (new)
- For: utility · whole page, every animated component
- Instead of: hoping screenshots catch drawings at the right moment
- Reader sees: nothing new; a returning reader, a reduced-motion reader, or a screenshot taken with `?final=1` lands on every drawing finished and every label in place.
- Moves: none; it removes motion.
- Build: one registry: each component calls `register({ play, finish })`. At startup `FINAL = new URLSearchParams(location.search).has('final') || reduced motion || sessionStorage 'seen' || document.visibilityState === 'hidden'`; when true, call every `finish()` and add `html.final` with `transition: none !important; animation: none !important`.
  Wrap storage in try/catch; set 'seen' after the first full play. On `visibilitychange` to hidden, finish anything mid-draw, because a hidden pane throttles requestAnimationFrame and timers and strands drawings half-drawn.
  Scroll-linked pieces keep following scroll but jump to their state without transitions.
- Narrow: same · Reduced motion: this is the reduced-motion path.
- Use when: always; builders need `?final=1` for QA screenshots. · Avoid when: never.
- Effort: S · Needs lib: no · Sources: new; built from the TVS reduce flag (01-tvs-harvest 2.1), house rule 14 on repeat visits (10-awwwards-picks D) and the known hidden-pane throttling bug · Verdict: NEW

### ARC-25 Loops that sleep off-screen
- For: utility · every ambient loop and rAF loop
- Instead of: loops that run forever (the TVS orbit, pulses and teaching circle never stopped)
- Reader sees: nothing; the page stays fast and still wherever they are not looking.
- Moves: in-view - CSS and SMIL loops pause when out of view and resume where they left off.
- Build: one IntersectionObserver per animated figure; on leave `el.getAnimations({ subtree: true }).forEach(a => a.pause())` and `svg.pauseAnimations()`; on enter `play()` and `unpauseAnimations()`; rAF loops check a `visible` flag and stop scheduling; also pause on `visibilitychange`; reduced motion cancels and renders finished.
- Narrow: same · Reduced motion: loops off.
- Use when: always, if anything loops. · Avoid when: never.
- Effort: S · Needs lib: no · Sources: P437 https://www.wafer.ai, https://www.roveia.com · Verdict: KEEP

### ARC-26 Still switch
- For: utility · whole page, when anything loops or draws for long
- Instead of: no way to stop motion short of the operating-system setting
- Reader sees: a small "Stop motion" toggle at the end of the chapter bar; one tap finishes every drawing and stills every loop.
- Moves: tap - toggles `html.still`; the label swaps over 0.2s.
- Build: the toggle calls the ARC-24 registry (drawings jump to finished, never frozen mid-stroke) and pauses loops (ARC-25); its state lives in sessionStorage as a per-viewer convenience; it starts on when the system asks for reduced motion. 44px tap target.
- Narrow: same · Reduced motion: starts on.
- Use when: the page has an ambient loop or a sequence longer than 5s (WCAG 2.2.2). · Avoid when: nothing moves.
- Effort: S · Needs lib: no · Sources: P105 https://ciechanow.ski/gps/ · Verdict: ADAPT, changed: finishes drawings instead of pausing them; lives in the chapter bar.

### ARC-27 Phone gate
- For: utility · 1 message
- Instead of: a cramped phone layout of a laptop story
- Reader sees: on a phone, a dark screen with a line-drawn laptop, "Open this on your laptop", and a "Copy link" button.
- Moves: none.
- Build: inline script before `<main>`: if `navigator.maxTouchPoints > 0` and the screen's short side is under 540px, add `html.phone`; CSS hides main and footer and shows `.gate` (flex column, centred, min-height 100svh, safe-area gutters, dark doorstep background). CSS fallback `(pointer: coarse) and (max-width: 539px)` only, so narrow desktop windows still get the page.
  The gate title is a `<p>` so the hero keeps the only `h1`; laptop icon in a 3px marker stroke; Copy link reuses the TVS copy button.
- Narrow: this is the narrow state; tablets (short side 540px or more) get the page · Reduced motion: n/a.
- Use when: the story is laptop-first, which is this skill's default. · Avoid when: most readers will first open the link on a phone; build a stacked phone twin instead.
- Effort: S · Needs lib: no · Code: TVS harvest (2.8, 2.10) · Sources: P031 (TVS site, page.html ~L262-277, L455-463) · Verdict: ADAPT, changed: narrow desktop windows no longer gated; one h1; copy-link button added.

### ARC-28 Chapter bar with reading ruler
- For: utility, call-to-action · 4-8 chapters, pages past about 6 screens
- Instead of: a hamburger menu or a full nav
- Reader sees: after the hero, a thin bar at the top with the current chapter's name, "03 / 06", a 2px ruler that fills as they read, and one button on the right that goes to the ask.
- Moves: scroll-linked - ruler `transform: scaleX()` on `animation-timeline: scroll(root)`, linear (never width); the bar arrives over 0.3s once the hero has left; the chapter name swaps by a 0.2s crossfade.
- Build: `position: sticky; top: 0; height: 44px`; an IntersectionObserver on chapters sets the name and count; the ruler's range excludes the footer (`animation-range: 0% calc(100% - 500px)`), with an rAF fallback writing `--p`. Chapter names are plain labels; the ask button is the bar's only link, so reading stays in order. Optional "35%" tag via an `@property --pct` counter.
  Side-rail variant for 6-9 chapters on wide screens: one dot per chapter at the left edge, filled once passed, the current name beside it.
- Narrow: tablet portrait keeps "03 / 06" and the ruler, with the name truncated · Reduced motion: the ruler stays (it follows the reader), no arrival.
- Use when: a long single page with 4 or more chapters. · Avoid when: the page fits in 3 screens, or while the hero is in view (never cover the first frame).
- Effort: S · Needs lib: no · Sources: P104 https://seeing-theory.brown.edu/basic-probability/index.html, P219 https://www.apple.com/macbook-pro/, P425 https://piergorelli.com, P360 https://webkit.org/blog/17101/a-guide-to-scroll-driven-animations-with-just-css/ · Verdict: ADAPT, changed: rail, bar and ruler merged; chapter jump links removed; one ask button.

### ARC-29 Stage counter, n / N (new)
- For: utility, sequence · every pinned stage, route or chapter set
- Instead of: unnumbered steps the reader cannot place
- Reader sees: a small mono "02 / 05" in the corner of the stage with a five-dot strip beside it, so they always know where they are and how much is left.
- Moves: in-view per step - the digit swaps with an 8px vertical slide and fade over 0.25s cubic-bezier(.22,1,.36,1); the next dot fills (0.2s).
- Build: `<p class="count" aria-live="polite">` with `font-variant-numeric: tabular-nums`, written by the same observer that sets `data-step`; the dots are a word-sized glyph (ARC-31); same numeral style as the chapter numerals (MOT-22).
- Narrow: stays on the pinned top strip; in the static twin each card carries its own "n / N" · Reduced motion: instant swap.
- Use when: any stage, route or sequence of 3 or more steps. · Avoid when: a single step.
- Effort: S · Needs lib: no · Sources: new; built from house rules 8 and 12 (10-awwwards-picks D) and the counters at Metic, Heron and Townhouse (10-awwwards-picks B7) · Verdict: NEW

### ARC-30 Scroll cue
- For: utility · 1, in the hero
- Instead of: a bouncing arrow
- Reader sees: "SCROLL" in tiny caps at the bottom of the full-screen hero, with a thin line under it that grows down and drains away.
- Moves: ambient - starts only after the hero drawing finishes; scaleY 0 to 1 from the top, then 1 to 0 from the bottom, 2.4s per cycle, 3 cycles, then rests as a static line; hides on the first scroll.
- Build: absolute, centred, bottom 28px; mono 11px, tracking .12em, in the doorstep label tone (#C9B8A6 on wood); an `<i>` 1px × 38px with a gradient to transparent. It stays inside the hero; nothing of the next section shows in the first frame.
- Narrow: same · Reduced motion: static line.
- Use when: a full-screen hero hides that there is more below. · Avoid when: the hero is shorter than the viewport.
- Effort: S · Needs lib: no · Sources: P006 (TVS site, page.html ~L55-57, L475) · Verdict: ADAPT, changed: waits for the hero draw and stops after 3 cycles, so it never competes with the drawing.

### ARC-31 Word-sized glyphs
- For: utility, emphasis, sequence · 1 per paragraph at most
- Instead of: "Step 3 of 5" spelled out, or icons in a separate column
- Reader sees: tiny drawings inside sentences, such as a five-dot strip for "step 3 of 5" or a small route squiggle, so text and picture read as one.
- Moves: in-view, once - the glyph pen-draws or its dot fills (0.6s) when its sentence enters.
- Build: inline `<svg class="wg" viewBox="0 0 40 10" width="2.6em" height=".65em">` with `vertical-align: -.05em`; generators `steps(n, i)` returns circles and `route(points)` returns a polyline; one accent plus grey; the sentence's text carries the meaning for screen readers.
- Narrow: same · Reduced motion: static glyph.
- Use when: dense paragraphs need anchors without breaking the read. · Avoid when: the glyph would need a legend.
- Effort: S · Needs lib: no · Sources: P125 https://www.edwardtufte.com/notebook/sparkline-theory-and-practice-edward-tufte/ · Verdict: ADAPT, changed: house pen timing; at most one per paragraph.

### ARC-32 Hand-drawn icon set with wobble
- For: utility, atmosphere · up to about 20 icons
- Instead of: a stock icon font
- Reader sees: simple 2px line icons (leader, factory, chat, box, chip, seedling, book) with a faint hand wobble that matches the drawings.
- Moves: none (static).
- Build: one hidden `<svg width="0" height="0">` holding `<symbol viewBox="0 0 48 48">` icons (fill none, stroke currentColor, stroke-width 2.2, round caps and joins), used as `<svg class="ico"><use href="#i-lead"/></svg>`; `.ico use { filter: url(#wobble) }` with fractalNoise .045, 2 octaves, seed 2, displacement scale 1.6. Sizes: 44px default, 40 on dark rows, 30 in step discs, 28 in orbit nodes, 17 in chips.
- Narrow: same · Reduced motion: n/a.
- Use when: one warm icon voice is needed across chips, nodes and cards. · Avoid when: icons must stay crisp at 16px.
- Effort: S · Needs lib: no · Code: TVS harvest (2.13) · Sources: P032 (TVS site, page.html ~L41-42, L432-453) · Verdict: KEEP

---
