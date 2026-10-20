# People, proof and the ask: people-roles, proof-trust, call-to-action

Pattern library family for `pitch-site-udyaan`. 33 entries (7 starred), curated from slice4 (47 raw entries in this family).
Verdicts: 6 KEEP, 23 ADAPT, 4 NEW, 9 CUT (listed at the end). 2 raw entries moved to amounts-ranks (P075 into AMT-19, P341 into AMT-02).
KEEP means the device and its code ship as found, with at most timing values brought to the house rule. ADAPT means the trigger, motion, content rule or layout changed.

**Shorthand used in every entry (house motion values):**
- **pen draw**: stroke-dashoffset from length to 0, duration = length / 600 px/s, clamped 0.6-2.2s, next stroke starts at 80-85% of the previous one, ease cubic-bezier(.45,.05,.35,1).
- **arrives**: opacity 0 to 1 plus a rise of 12px (16px at most), 0.6-1.0s, cubic-bezier(.22,1,.36,1). Staggers 60-110ms, total capped at 450ms. Nothing enters from the side.
- **reveals once**: text arrives the first time it enters the view and always finishes.
- **scroll-linked**: linear, tied 1:1 to progress. Drawings may follow scroll; text never does.
- **construction line**: the faint dashed version of a line (about 25% ink, dash "2 6"), drawn solid when its caption explains it.
- **pinned**: a sticky stage whose section is 3 viewport heights or less, with an `n / N` counter, and a stacked static twin below 768px.
- **accent**: the one colour that points. Actor colours (PPL-03) identify; they never point.
- **people are drawn**: a line portrait (PPL-01 recipe) or a role glyph. Never a stock photo, a monogram circle or a generic avatar.
- **real words, real numbers**: quotes are verbatim, numbers carry a source. No placeholder data dressed as real.

---

## Family picker

Pick by what the content is, how many items, and how they relate. Starred first. If unsure: one person goes to PPL-01, proof goes to PPL-16, the close goes to PPL-28.

**People and roles**
- 1 named person who leads the work or closes the page: PPL-01 ★, PPL-27 ★.
- 2-8 named people, each entering the story at a different moment, sequential: PPL-02 ★, PPL-07.
- 2 parties, a simple experience hiding real work, opposed (what you see, what we do): PPL-04 ★, PPL-08.
- 2 parties, work handed over gradually, linked: PPL-05, SEQ-34 (order-time, the roadmap version).
- 3-9 parties that recur across many sections: PPL-03 (use alongside any other entry).
- 3-8 people by 4-12 tasks, "who do I call?", linked: PPL-06, PPL-03.
- 3-15 roles that join and leave across phases, sequential: PPL-07, PPL-08.
- 2-4 parties passing work along a process, sequential and linked: PPL-08, PPL-06.
- 3-30 people working in groups, grouped: PPL-09, PPL-14.
- 12-200 people with a real count and three who agreed to be named, equal: PPL-14, PPL-12.
- 10-150 members of a coalition or cohort, grouped by role: PPL-12, PPL-14.
- One real story standing for many, 1 hero plus a crowd: PPL-11, PPL-14.
- Access to people through a network, 8-30 nodes, linked: PPL-10, STR-15 (structure-links).
- Anonymous people doing the work, Indian folk-line fit: PPL-13, PPL-14.
- 3-6 stakeholders who see the problem differently, opposed: PPL-15, PPL-20.

**Proof and trust**
- The client's own words, 1 per section: PPL-16 ★, PPL-15.
- 1-3 sourced numbers a sceptic might doubt: PPL-18 ★, AMT-02 ★.
- 1 prior result in one sentence, with or without a number: PPL-17, PPL-25.
- 1-5 audit scores the reader will not decode: PPL-19, AMT-23 (against peers).
- 1-3 strong testimonials with one real outcome each: PPL-20, PPL-15.
- Past work with no numbers, 3-8 pieces, equal: PPL-22, PPL-21.
- A deliverable the reader cannot picture, 1 artefact: PPL-21, PPL-22.
- Money, data or safety worries, 4-6 rules, equal: PPL-23, PPL-26.
- 2-6 side facts per section that support without interrupting: PPL-24, AMT-15.
- 1 verified endorsement or approval: PPL-25, PPL-17.
- An example that could read as a promise, or a number that is an estimate: PPL-26, AMT-06.

**The ask (every close names what to choose, who to contact, and what arrives next, and the page ends on it)**
- Default close, 3 small first steps plus 1 contact: PPL-28 ★, PPL-27 ★.
- 1 contact, the reader already convinced: PPL-27 ★, PPL-30.
- 1 decision left after the evidence: PPL-30, PPL-29.
- 2-4 next steps with one recommended, ranked: PPL-29, AMT-27.
- 2 options for readers at different readiness, opposed (start now, talk first): PPL-32, PPL-31.
- Reader unsure what to write, 2-3 first steps: PPL-31, PPL-29.
- 3-6 earlier sections that should converge on one person, linked: PPL-33, PPL-27 ★ as its card (PPL-33 is built around it).

---

## People and roles

### PPL-01 ★ Drawn portrait of the named contact
- For: people-roles, atmosphere · 1 person (2 at most; each face is hand-authored)
- Instead of: a stock photo, a monogram circle or a generic avatar
- Reader sees: A round dark disc with the contact's face drawn in one pale powder line (face, hair, collar), ringed by two interwoven wavy strands with dots between them like a doorstep kolam, and a small marker-yellow knot at the chest.
- Moves: in-view (threshold .5) - pen draw: braid strand one, then strand two at 80% of the first (each about 0.8-1.1s at 600 px/s), then the ten face strokes in drawing order, each at least 0.6s, next at 80-85%; draws once and stays.
- Build: SVG 200×200 shown at 150px, `border-radius:50%`, ring plus `0 14px 30px -18px rgba(36,29,24,.6)` shadow; wood disc r 99; strands r(t) = 84 + 7·sin(12t + phase) for phase 0 and π, 240 samples, closed; 12 pulli dots r 1.8 on r 84; about 10 hand-authored face paths at 1.8-3px in powder #F4F1EA; rice-powder filter (two feTurbulence plus feDisplacementMap passes, blur .55). For a client outside India, swap the braid for the page's own motif ring.
- Narrow: below 820px the contact card stacks and the portrait stays 150px · Reduced motion: drawn complete at once.
- Use when: one named person leads the work or closes the page and a photo would clash with line illustration. · Avoid when: the person has not approved a likeness, or there are more than two people (use PPL-02 glyphs or PPL-14).
- Effort: M · Needs lib: no · Code: TVS harvest · Sources: P029 (TVS page.html ~L391-397, L913, L1157-1197; harvest section 2.15) · Verdict: KEEP (strokes retimed: TVS started them .22s apart, the house pen rule starts each at 80-85% of the last)

### PPL-02 ★ Bio card at first mention
- For: people-roles, proof-trust · 2-8 named people, sequential
- Instead of: a team section of headshots, names and titles in a grid
- Reader sees: The first time a person is named in the story, a small card appears in the margin beside that paragraph: their drawn line portrait, name, role, and one line on what they will do for the reader.
- Moves: in-view (paragraph at mid-screen) - the card arrives (rise 12px, 0.7s cubic-bezier(.22,1,.36,1)), then its 64px portrait pen draws; once. Later mentions only tint the person's name chip in their PPL-03 colour.
- Build: grid `minmax(0,680px) 220px` (text plus a margin column, gap 32px); `aside.bio` placed on its paragraph's row with `grid-row`; portrait is a simplified 6-8 stroke line face in the PPL-01 style, or a role glyph when no likeness is approved; name serif 20px, role mono 11px caps, one sans 15px sentence starting with a verb ("Runs your weekly review"). Never a CV.
- Narrow: below 820px the card sits inline under its paragraph, full width · Reduced motion: card and portrait shown complete.
- Use when: trust rests on named people and each one enters the story at a clear moment. · Avoid when: the team is large or anonymous (use PPL-09 or PPL-14).
- Effort: S · Needs lib: no · Sources: P089 https://en.wikipedia.org/wiki/Snow_Fall · Verdict: ADAPT, changed: the 12px slide from the side became a 12px rise; photo became a drawn portrait; "what they do for you" line made mandatory.

### PPL-03 Actor colour contract with team chips
- For: people-roles, many-to-many · 3-9 parties recurring across sections
- Instead of: repeating "our team" and "your team" in prose and hoping the reader keeps track
- Reader sees: Each party (the client, each of our teams) owns one pastel chip with its name and a small icon, and the same colour marks that party in every diagram from the first section to the last.
- Moves: load - static. Colour carries identity, so it never animates.
- Build: `.chip` inline-flex, gap 6px, sans 13px/600, line-height 1.2, padding 5px 10px, radius 999px, ink text, `background:var(--chip)`, 17px icon from the wobble sprite; tested pastel set on cream: #C9D2EA, #DCCDEB, #EBCB86, #F0C1AE, #EFC0D1, #BCD0DF, #E6D5BE, #F3D894, #D9D3CB (fallback #E4DED3). Declare each as `--c-<actor>` on `:root` and reuse the same variables as SVG fills. Tint chips and shapes, never body text (pastels fail contrast). Keep the name on every chip; colour is never the only cue. Sizes: 14.5px with 7px 13px padding on cards, 12px inside diagrams.
- Narrow: chips wrap (flex-wrap, gap 6px) · Reduced motion: no change.
- Use when: the same parties recur across many sections. · Avoid when: more than 9 parties, or an actor colour would be confused with the accent.
- Effort: S · Needs lib: no · Code: TVS harvest · Sources: P010 (TVS page.html ~L279-283; harvest section 2.11), P061 https://ciechanow.ski/gps/ · Verdict: KEEP (P061's CSS-variable contract folded in; its tinted prose dropped)

### PPL-04 ★ Line of visibility: what you see, what we do behind it
- For: people-roles, sequence, proof-trust · 4-8 steps, 2 layers (your side, our side)
- Instead of: a list of "our services", or a process diagram of boxes and arrows
- Reader sees: One pinned line drawing of the client's simple experience across the top, a dashed line labelled "what you see", and under it the hidden work drawn faint; each caption that scrolls past turns one piece of backstage work solid and connects it up to the visible step it makes possible.
- Moves: scroll-linked (pinned) - one stage, one knob: each caption step pen draws one backstage piece from construction line to solid, then its connector up to the visible step; the active step is the only one in the accent, the rest sit at 30%; captions reveal once; `n / N` counter.
- Build: sticky stage (`top:10vh; height:80vh`) inside a section of N caption blocks at about 60vh each, capped at 3 viewport heights; one SVG with three bands (your actions / the dashed visibility line with a mono label chip / behind the scenes); every backstage path uses `pathLength="1"` so dashoffset 1 to 0 is uniform; one IntersectionObserver with `rootMargin:"-45% 0px -45% 0px"` sets `stage.dataset.step`. Roles and actions only, no numbers.
- Narrow: below 768px static twin: one card per visible step with its backstage work listed under a "behind this" label, all lines drawn · Reduced motion: whole blueprint finished, connectors solid, active accent on step 1.
- Use when: the value is invisible work behind a simple experience (the Washington Post x-ray move). · Avoid when: the reader has no interest in process (lead with outcomes).
- Effort: M · Needs lib: no · Sources: P088 https://pudding.cool/2026/03/ivf/, P129 https://www.nngroup.com/articles/service-blueprints-definition/ · Verdict: ADAPT, changed: two lanes and the service blueprint merged; the tap curtain became scroll steps; backstage starts as construction lines.

### PPL-05 Who carries it, handing over
- For: people-roles, comparison · 4-12 tasks, 2 parties
- Instead of: a RACI table, or "we will support you" in prose
- Reader sees: One bar per task split by a marker into "we carry" and "you carry"; when the caption moves from "at the start" to "at hand-over", the markers slide so the reader's share grows.
- Moves: in-view (two caption steps) - step 1 places the markers (arrive, 0.8s cubic-bezier(.22,1,.36,1)); step 2 slides them to hand-over positions over 0.8s with the same ease, 80ms apart capped at 450ms; counter "1 / 2".
- Build: each bar a flex row of two divs in the two PPL-03 colours; `--split` takes only 25%, 50% or 75% (mostly us / shared / mostly you), never fine percentages; `transition: flex-basis .8s cubic-bezier(.22,1,.36,1)`; phase names relative ("at the start", "at hand-over"), never dates.
- Narrow: below 820px full-width bars; below 768px both states shown as two stacked static sets · Reduced motion: hand-over state shown, with a faint ghost marker at the start position.
- Use when: work is handed over gradually and the reader worries about being left alone. · Avoid when: responsibility is all-or-nothing (use PPL-06). See also SEQ-34 (order-time) for the same idea across a roadmap.
- Effort: S · Needs lib: no · Sources: P122 https://github.com/Financial-Times/chart-doctor/tree/main/visual-vocabulary · Verdict: ADAPT, changed: the Month 1 / Month 6 tap toggle became two scroll steps with relative phase names.

### PPL-06 Who holds the pen
- For: people-roles, many-to-many · 3-8 people by 4-12 tasks
- Instead of: a RACI spreadsheet or a list of names and job titles
- Reader sees: Tasks down the side, drawn faces across the top, and a mark in each cell: a solid dot for the one person answerable, a ring for whoever does the work, a half dot for "asked first", a small dot for "kept in the loop"; a sentence below reads, for example, "Ravi owns 2 tasks, does 4, is asked on 3".
- Moves: tap - tapping a face (a real `<button>`) lights that column and swaps the sentence (arrives, 0.6s cubic-bezier(.22,1,.36,1)); on load the reader's main contact is already lit, so nothing depends on tapping.
- Build: CSS grid; glyphs are tiny SVGs (filled circle, stroked ring, half via `clipPath`, r 2 dot) with a one-line legend above; `console.assert` exactly one solid dot per row; the sentence counts real cells only, so its numbers are honest by construction.
- Narrow: below 820px one card per person listing their tasks grouped by mark · Reduced motion: static, default column lit.
- Use when: the reader asks "who do I call?" or worries about accountability. · Avoid when: fewer than 3 people (say it in a sentence).
- Effort: S · Needs lib: no · Sources: P131 https://en.wikipedia.org/wiki/Responsibility_assignment_matrix · Verdict: ADAPT, changed: a default column is pre-lit so tapping is optional; monograms became drawn faces.

### PPL-07 Cast list across phases
- For: people-roles, time-roadmap · 3-15 roles or workstreams over 3-6 phases
- Instead of: a staffing table, or an org chart that hides when people arrive and leave
- Reader sees: One thin horizontal bar per person or role, starting in the phase they join and ending where they leave, grouped in bands by team like a cast list across acts, with a "you are here" line at the current phase.
- Moves: scroll-linked - the "now" line moves linearly with section progress across the phase columns; bars it has crossed sit in full ink, bars ahead at 30%; names ride on the bars and reveal once.
- Build: CSS grid, one column per phase; each bar `grid-column: start / end` with its label inside, coloured from PPL-03; the line sits at `left: calc(var(--p) * 100%)`; group rows under thin header rows per team (Priestley grouped lives by field) and put the reader's own people on the bottom band. Phase names only; dates only if the brief states them. If made sticky, pin for 2 viewport heights at most.
- Narrow: below 820px phases become rows, each listing the people chips active in it · Reduced motion: no moving line; the current phase column highlighted.
- Use when: the reader asks "who will I deal with, and when?" · Avoid when: everyone is there throughout (use PPL-09), or one person does everything.
- Effort: S · Needs lib: no · Sources: P126, P278 https://en.wikipedia.org/wiki/A_Chart_of_Biography · Verdict: ADAPT, changed: two Priestley entries merged; bars dim ahead of the line instead of growing; phases, never dates.

### PPL-08 Swimlane hand-offs
- For: people-roles, sequence · 2-4 lanes, 5-12 steps
- Instead of: a numbered process list that never says who acts
- Reader sees: Lanes named for each party (You, Us, Your customers); step cards sit in their lane, every hand-off between lanes is an elbow arrow, and hand-offs (the moments that fail in real life) carry a small dot.
- Moves: scroll-linked (pinned) - one hand-off per caption step: its elbow arrow pen draws from construction line to solid and the active card lifts by shadow only (no travel); `n / N` counter.
- Build: CSS grid, rows = lanes, columns = step order (never weeks or dates); cards placed with `grid-row` / `grid-column`; overlay SVG builds elbow paths (8px corner radius) from card `getBoundingClientRect()` pairs on load, resize and `document.fonts.ready`; lane tints from PPL-03; section capped at 3 viewport heights.
- Narrow: below 768px a vertical step list; each step carries its lane chip and ends "hands to: Us" · Reduced motion: all arrows drawn, no lift.
- Use when: the reader needs to see who acts at each step and where work changes hands. · Avoid when: one party does everything (use a single sequence).
- Effort: M · Needs lib: no · Sources: P128 https://datavizproject.com/data-type/swimlane-flow-chart/, P330 https://pudding.cool/process/how-to-implement-scrollytelling/ · Verdict: ADAPT, changed: merged; week columns became step order; the sweeping playhead became one arrow drawn per step.

### PPL-09 Team pods
- For: people-roles, hierarchy, grouped-list · 2-6 pods, 3-30 people
- Instead of: a boxy org tree or a grid of headshots
- Reader sees: One big drawn circle for the whole team holding smaller circles, one per pod, with small line faces inside; each pod carries a one-line label on what it does for the reader.
- Moves: in-view - the outer circle pen draws, then the pods in reading order (next at 80-85%), then names arrive (rise 12px, 0.7s, 80ms apart capped at 450ms). Tap a pod to enlarge it: the viewBox interpolates over 0.8s cubic-bezier(.22,1,.36,1). Every name is also listed under the drawing, so nothing hides behind a tap.
- Build: hand-place pod circles for small sets; people inside on a sunflower spiral (angle 137.5°, r = c × √i); pod size follows real headcount, or is equal when roles matter more (the caption says which); zoom by interpolating the viewBox array in rAF.
- Narrow: below 820px pods become stacked cards, each with its face row and label · Reduced motion: complete drawing; tap zoom is instant.
- Use when: the team works as groups rather than a chain of command. · Avoid when: reporting lines are the point (use a tidy tree), or under 4 people (use PPL-02).
- Effort: M · Needs lib: no · Sources: P134 https://datavizcatalogue.com/methods/circle_packing.html · Verdict: ADAPT, changed: circles pen draw; the zoom became optional with a list twin; each pod must say what it does for the reader.

### PPL-10 Introduction chain
- For: people-roles, place-network · 8-30 people, one authored path of 2-5 hops
- Instead of: "we have a strong network" over a row of partner logos
- Reader sees: A soft field of small named nodes joined by faint dashed links; the reader's node on one side, the person they need on the other, and the chain of introductions between them drawing solid, hop by hop.
- Moves: in-view - the field sits as construction lines; then the chain pen draws one hop at a time (each 0.6-0.9s, next at 80-85%) and each node it reaches fills with the accent; once.
- Build: nodes hand-placed, or a 200-iteration force pass run at build time and frozen into the HTML; links are only named relationships from the brief ("trained by", "buys from"), written on the link; hops are paths with `pathLength="1"`. The path is chosen by the author, not searched at runtime.
- Narrow: below 820px a vertical chain of drawn faces with the relationship written on each link · Reduced motion: the chain shown solid.
- Use when: the value on offer is access to people (a cooperative, a partner chain, an alumni network). · Avoid when: the network is tiny (say it in a sentence) or the reader is not part of it.
- Effort: M · Needs lib: no · Sources: P117 https://www.visualcinnamon.com/portfolio/royal-constellations/ · Verdict: ADAPT, changed: the two-tap shortest-path explorer became one authored path drawn on view.

### PPL-11 One person, then everyone like them
- For: people-roles, quantity-scale · 1 hero plus a crowd (0 or 1 sourced count)
- Instead of: a big audience number with no face
- Reader sees: One named person's path through the client's service drawn as a single accent line; then, faintly behind it, many copies of the same path in grey, and a caption: "and 340 more like her this year" when the count is real, or "and every apprentice after her" when it is not.
- Moves: scroll-linked (pinned) - step 1 pen draws the hero line (1.2-2.2s by length); step 2 brings in the crowd, its opacity tied linearly to progress (up to .08 per path); the count, if any, arrives finished in the caption (no spin-up).
- Build: SVG stage, map optional; hero `<path>` 3px in the accent; crowd as a few merged `<path>` elements (concatenated `d` strings of jittered copies of the hero path, ±6px) so dozens cost little; the caption is the only place a number appears, with its source in a PPL-18 receipt.
- Narrow: below 768px static: hero line drawn, crowd as soft shading, caption below · Reduced motion: final frame with the caption.
- Use when: empathy must come before scale and one real story stands for many. · Avoid when: the hero story would be invented or unrepresentative (label composites "a typical apprentice").
- Effort: M · Needs lib: no · Sources: P044 https://www.theguardian.com/us-news/ng-interactive/2017/dec/20/bussed-out-america-moves-homeless-people-country-study · Verdict: ADAPT, changed: the running counter became a finished number shown only when sourced; a no-number caption added.

### PPL-12 Seat chart
- For: people-roles, part-whole · 10-150 real people or member organisations
- Instead of: "a coalition of 60 partners" in a sentence, or a logo wall
- Reader sees: A half circle of seats, one per real person or member group, coloured by role so the groups form wedges, like a parliament of everyone involved; the reader's own seats ringed in yellow pen.
- Moves: in-view - seats arrive row by row from the inside out (opacity, 0.6s cubic-bezier(.22,1,.36,1)), rows 80ms apart capped at 450ms; then the hand-drawn ring pen draws around the reader's wedge.
- Build: rows r with radius R_r and seats per row in proportion to R_r; seat angle = π × k / (n_r - 1); sort colours by angle so groups form wedges; colours from PPL-03; caption states "one seat = one member" and the source.
- Narrow: below 820px 320px wide with the legend below · Reduced motion: final state, ring drawn.
- Use when: showing a coalition, cooperative, committee or cohort whose size is sourced. · Avoid when: only a handful of people (use PPL-09 or PPL-02), or the count is an estimate.
- Effort: S · Needs lib: no · Sources: P159 https://github.com/Financial-Times/chart-doctor/tree/main/visual-vocabulary · Verdict: ADAPT, changed: row stagger capped at 450ms; the reader's wedge gets the TVS ring.

### PPL-13 Folk-line figures
- For: people-roles, atmosphere · 3-12 anonymous figures in one scene
- Instead of: stock photos of "happy workers" or generic person icons
- Reader sees: Small people built from two triangles and a circle head, drawn in pale rice-paste line on a chalky earth tint, doing the actual work the proposal describes (carrying, teaching, gathering).
- Moves: in-view - each figure pen draws as one path (head, body, limbs), next figure at 80-85%; then still. No idle limb motion.
- Build: one `<symbol>` per pose built from two `polygon` triangles, a `circle` head and line limbs (pose angles fixed at build time); reuse the rice-powder filter from PPL-01 so the motif family stays one; background a flat laterite-family tint (#DDB09A) with static grain.
- Narrow: below 820px fewer figures per scene at the same size · Reduced motion: figures shown drawn.
- Use when: the page needs anonymous people (a class, a crew, a village) in the same folk-line language as a kolam. · Avoid when: the client has no link to the culture (borrowed folk art becomes costume); draw figures in the page's own line style instead.
- Effort: M · Needs lib: no · Sources: P284 https://en.wikipedia.org/wiki/Warli_painting · Verdict: ADAPT, changed: the idle limb loop cut; deep red ground softened to a chalky section tint.

### PPL-14 Crowd sketch with three named faces (new)
- For: people-roles, proof-trust · 12-200 people, 3 of them named
- Instead of: a wall of 25 headshots, or "trusted by thousands"
- Reader sees: A loose crowd of tiny line figures (one per real person, or one per ten with the key stated), and three of them lifted out by leader lines to a small drawn portrait, a name, a role and one line on what changed for them.
- Moves: in-view - the crowd arrives as one block (opacity, 0.7s, no per-figure stagger); then the three leader lines pen draw one after another (0.6-0.9s each, next at 80-85%), each callout arriving after its line (rise 12px, 0.7s cubic-bezier(.22,1,.36,1)).
- Build: one `<symbol>` figure placed on a seeded jitter grid (hand-scattered look, stable between loads); the three named figures in the accent; leader paths built from `getBoundingClientRect()` on load and resize; caption states the key ("1 figure = 1 student") and the source; portraits from the PPL-01 recipe.
- Narrow: below 820px the crowd becomes a band at the top and the three callouts stack below it, each with a short leader · Reduced motion: crowd, lines and callouts all shown.
- Use when: proving "people like you already did this" with a real count and three people who agreed to be named. · Avoid when: the count is estimated, or nobody agreed to be named (show the crowd alone with its key).
- Effort: M · Needs lib: no · Sources: new; replaces P204 (https://www.raycast.com) and borrows the counting rule of P107 Isotype (https://en.wikipedia.org/wiki/Isotype_(picture_language)) · Verdict: NEW

### PPL-15 Voices in the room
- For: people-roles, proof-trust · 3-6 real voices
- Instead of: a testimonial carousel, or a paragraph summarising "stakeholder feedback"
- Reader sees: A short exchange: one plain question from us, then one-line answers from different people (the plant head, a supervisor, an apprentice), each beside a small drawn face, followed straight away by the drawing that settles the question.
- Moves: in-view - bubbles arrive in reading order (rise 12px, 0.7s cubic-bezier(.22,1,.36,1)), 100ms apart capped at 450ms; once.
- Build: a `figure` per voice with drawn portrait or role glyph, name, role and one serif line; the question sits left, answers indented; voice tints from PPL-03. Quote real words exactly; label composites as composites.
- Narrow: below 820px same, one column · Reduced motion: all bubbles shown.
- Use when: stakeholders see the problem differently and their own words make the case. · Avoid when: quotes would be invented or paraphrased.
- Effort: S · Needs lib: no · Sources: P086 https://pudding.cool/2025/02/middle-school/ · Verdict: ADAPT, changed: monogram avatars became drawn faces; 150ms stagger capped at 450ms; real words only.

---

## Proof and trust

### PPL-16 ★ "You told us" echo
- For: proof-trust, emphasis · 1 quote per section
- Instead of: opening each section with our own pitch
- Reader sees: Under each section heading, a soft frosted box headed "YOU TOLD US" with the client's own words in serif, before any answer is given.
- Moves: in-view - arrives with its header (rise 12px, 0.75s); the one key phrase may take the marker sweep (background-size 0% to 100% at 52% height, 0.7s cubic-bezier(.22,1,.36,1) after .35s).
- Build: `.said-block` margin-top 26px, padding 20px 24px, radius 14px, background rgba(255,255,255,.42) so it frosts over any section tint, ring `0 0 0 1px var(--line)`, max-width 58ch; tag mono 11px caps .08em on its own line; quote serif 20px/1.4. Quote the brief or the meeting verbatim and say where it was said.
- Narrow: same at all widths · Reduced motion: static, sweep complete.
- Use when: answering a brief; restating the ask in their words before the answer builds trust. · Avoid when: you do not have the reader's own words (never put a paraphrase in quote marks).
- Effort: S · Needs lib: no · Sources: P011 (TVS page.html ~L86-88, L548) · Verdict: KEEP

### PPL-17 Proof strip
- For: proof-trust · 1 claim
- Instead of: a paragraph of credentials, or a logo row
- Reader sees: A slim frosted bar with a hand-drawn check-circle and one sentence of evidence, its key phrase in the marker highlight.
- Moves: in-view - arrives with its parent block (rise 12px, 0.75s); the icon and highlight are static.
- Build: `.proof` margin-top 40px, flex, gap 14px, padding 16px 20px, radius 14px, background rgba(255,255,255,.45), ring `0 0 0 1px var(--line)`, max-width 640px, 16px text; `#i-check` at 44px from the wobble icon sprite; one sourced sentence, its source in a muted mono line or a PPL-18 receipt.
- Narrow: same, text wraps · Reduced motion: static.
- Use when: one prior result makes the proposal credible. · Avoid when: you have several proofs (use PPL-18 or PPL-22), or the result is unsourced.
- Effort: S · Needs lib: no · Sources: P018 (TVS page.html ~L141, L690) · Verdict: KEEP

### PPL-18 ★ Number with its receipt
- For: proof-trust, quantity-scale · 1-3 sourced figures
- Instead of: a big count-up stat with no source
- Reader sees: A big serif number with a short plain caption and, right under it, a small underlined "how we know"; tapping it opens the source, date and method, or the quote and name behind the number.
- Moves: in-view - the number arrives finished (rise 12px, 0.7s cubic-bezier(.22,1,.36,1)), no count-up; tap - the receipt opens in place (opacity plus 4px rise, 0.6s, same ease).
- Build: `<figure class="stat"><data value="0.42">42%</data><figcaption>…</figcaption><button aria-expanded="false">How we know</button><div class="receipt" hidden>…</div></figure>`, or `<details>`/`<summary>` with no JS. Number serif clamp(48px,7vw,88px) with `tabular-nums`, unit in mono; receipt mono 12.5px (source, date, method) or an italic serif quote with name and role. Figures: built for 1-3 sourced numbers; with none, use PPL-16 or PPL-22, never a placeholder.
- Narrow: below 820px numbers stack; the receipt opens inline · Reduced motion: number static, receipts may start open.
- Use when: any number a sceptical reader might doubt. · Avoid when: you cannot name the source.
- Effort: S · Needs lib: no · Sources: P197 https://stripe.com, P453 https://twain.ai, https://www.wafer.ai · Verdict: ADAPT, changed: merged; count-ups cut; the popover became an inline receipt that never covers the page.

### PPL-19 Number with a verdict chip
- For: proof-trust, emphasis · 1-5 scores from a real audit
- Instead of: raw scores the reader has to interpret
- Reader sees: Each number carries a plain-word chip ("strong", "fair", "at risk") with a shape cue (filled circle, half circle, ring), so nobody has to decode it.
- Moves: in-view - the number arrives (rise 12px, 0.7s cubic-bezier(.22,1,.36,1)); its chip follows 300ms later with opacity only. No scale bounce.
- Build: a thresholds array maps value to label, and the thresholds come from a named standard (a published benchmark, the client's own target) stated under the row; chips use shape plus a muted section tint, never red, amber or green. Figures: works with 1 sourced score; with none, put the chip on a qualitative finding ("Paper registers: at risk").
- Narrow: below 820px the chip drops under the number · Reduced motion: static.
- Use when: reporting an audit of the client's site, process or people to readers who will not decode raw numbers. · Avoid when: the thresholds would be invented.
- Effort: S · Needs lib: no · Sources: P059 https://pudding.cool/2025/08/onions/ · Verdict: ADAPT, changed: bounce cut; thresholds must be sourced; traffic-light colours replaced by shapes.

### PPL-20 Spec-sheet testimonial
- For: proof-trust, people-roles · 1-3 testimonials
- Instead of: a carousel of one-line compliments
- Reader sees: A quote card beside a small drawn portrait, with a three-line data strip: who they are, what they used, what changed (one sourced fact).
- Moves: in-view - the quote arrives (rise 12px, 0.7s cubic-bezier(.22,1,.36,1)); the strip follows at 100ms; values are printed, not counted.
- Build: `<figure>` with `<blockquote>` (serif 22px/1.4) and a `<dl>` of three pairs (Who / Used / What changed), mono 11px labels and sans 15px values; 64px portrait from the PPL-01 recipe or a role glyph; if there is a video, show its running time beside the play button.
- Narrow: below 820px the strip moves under the quote · Reduced motion: static.
- Use when: you have 1-3 strong, specific testimonials, each with one real outcome. · Avoid when: all you have is general praise.
- Effort: S · Needs lib: no · Sources: P202 https://www.raycast.com · Verdict: ADAPT, changed: count-up cut; photo became a drawn portrait; strip fixed at three facts.

### PPL-21 The real deliverable, built
- For: proof-trust, part-whole · 1 artefact
- Instead of: a vague illustration of "a report" or "a dashboard"
- Reader sees: The actual thing they will receive (the weekly report, the filled form, the lesson sheet) built in HTML at reduced size, with one part circled in yellow pen and a short label on what it tells them.
- Moves: in-view - the artefact arrives (rise 12px, 0.7s); then the ring pen draws around the one part that matters (1.1s cubic-bezier(.45,.05,.35,1) after .3s) and its label arrives. No ambient updates.
- Build: semantic HTML and CSS (not a screenshot) scaled in a frame (`transform: scale(.8); transform-origin: top left`); content from the brief, or clearly example content carrying the PPL-26 tag; TVS ring path `M150 6C70 4 8 14 8 36s70 30 146 28 142-8 140-30S220 4 128 10`, 3px marker, `vector-effect: non-scaling-stroke`.
- Narrow: below 820px crop to the circled part with a fade mask at the edge · Reduced motion: static, ring drawn.
- Use when: the deliverable is a document or screen the reader cannot picture. · Avoid when: you would have to invent IDs, names or counts to make it look real.
- Effort: M · Needs lib: no · Code: TVS harvest · Sources: P179 https://linear.app; ring from TVS harvest section 2.14 · Verdict: ADAPT, changed: ambient card shuffling cut; "plausible" invented data banned; one ringed detail does the explaining.

### PPL-22 Object and its label
- For: proof-trust, list-of-equals · 3-8 past projects or results
- Instead of: a case-study grid of thumbnails with "Read more"
- Reader sees: Each piece of past work shown like a museum object: a line drawing or photo of the result, a short factual label (name, for whom, when, what was made) and a longer note that starts with what the reader can see and says why it matters to them.
- Moves: in-view - the object arrives (rise 12px, 0.7s cubic-bezier(.22,1,.36,1)); its label follows at 100ms. No spotlight sweep, nothing slides out from behind.
- Build: `figure` on a flat section tint; `aside.tombstone` mono 11px caps with `tabular-nums`; `.interpretive` serif 18px/1.45, title under 7 words, note at most 3 lines; one object per screen height in a single column so they are read in order.
- Narrow: below 820px label sits under the object · Reduced motion: static.
- Use when: proof of past work, especially when there are no numbers. · Avoid when: more than about 8 objects (pick the best 3), or the work is not yours to show.
- Effort: S · Needs lib: no · Sources: P259 https://www.catalogit.app/masterit/creating-exhibition-labels-with-catalogit · Verdict: ADAPT, changed: spotlight gradient and sliding placard cut; one column read in order.

### PPL-23 Safeguard switchboard
- For: proof-trust, list-of-equals · 4-6 safeguards
- Instead of: a wall of certificate badges, or "secure and compliant"
- Reader sees: A panel of hand-drawn switches, each beside one plain rule ("Two people approve every payment"); the switches turn on one after another and a closing line says "All on from day one".
- Moves: in-view - switches turn on in order (thumb travel 0.6s cubic-bezier(.22,1,.36,1)), 100ms apart capped at 450ms; the closing line arrives last. Turning on is the meaning, so this motion explains.
- Build: `<ul>` of rows; each switch an SVG track and thumb in the page's line style with `role="img"` and an `aria-label` stating the state; the "on" track fills with the accent. Rules must be the client's real defaults.
- Narrow: same, one column · Reduced motion: all switches on.
- Use when: money, data or safety worries the reader. · Avoid when: the safeguards are optional extras (never imply defaults).
- Effort: S · Needs lib: no · Sources: P212 https://mercury.com · Verdict: ADAPT, changed: 250ms stagger and Mercury curve brought to house values; switches drawn, not app chrome.

### PPL-24 Margin rail of proof
- For: proof-trust, definitions-jargon · 2-6 side notes per section
- Instead of: footnotes nobody reads, or proof that interrupts the argument
- Reader sees: The main story in a centre column; small quotes, sourced numbers and definitions sit in the margin beside the paragraph they support, joined to it by a short leader line.
- Moves: in-view - each note arrives when its paragraph reaches mid-screen (rise 12px, 0.7s cubic-bezier(.22,1,.36,1)); its leader pen draws from construction line to solid (0.6s); once.
- Build: `grid-template-columns: 216px minmax(0,680px) 216px` with 32px gaps; notes placed on their paragraph's row; leader a 1px path from the paragraph edge to the note.
- Narrow: below 820px notes sit inline after their paragraph as small boxed asides · Reduced motion: static, leaders solid.
- Use when: proof and side facts should support the argument without interrupting it. · Avoid when: the note is essential (it belongs in the main column).
- Effort: S · Needs lib: no · Sources: P218 https://claude.com/product/overview · Verdict: ADAPT, changed: the narrow swipe track (a carousel) became inline asides; leader lines added.

### PPL-25 Approval stamp
- For: proof-trust, emphasis · 1 per page
- Instead of: a row of certification badges
- Reader sees: A round ink stamp ("Approved by the board", "Funded", "Delivered") lands slightly tilted on a card, like an official mark on paper.
- Moves: in-view - from rotate(-14deg) scale(1.1) opacity 0 to rotate(-11deg) scale(1) opacity 1, 0.6s cubic-bezier(.22,1,.36,1), once; ink texture static.
- Build: SVG circle with its words on a circular `textPath`, the grain or rice-powder filter applied once (static); class toggled by the shared `onView` helper; wording exactly as the approving body would use it.
- Narrow: same · Reduced motion: shown in place.
- Use when: one verified proof point (an endorsement, a certification, a past approval). · Avoid when: the claim is not verified, or a second stamp is tempting (one per page or it stops meaning anything).
- Effort: S · Needs lib: no · Sources: P430 https://metic.studio/en · Verdict: ADAPT, changed: 0.4s landing lengthened to 0.6s; start scale cut from 1.15 to 1.1.

### PPL-26 Honest label: example tag and caveat note
- For: proof-trust · 1-3 per page
- Instead of: a disclaimer in the footer, or letting an example read as a promise
- Reader sees: Under a worked example, a small outlined mono label, "AN EXAMPLE, CHOSEN TO SHOW HOW WE WOULD WORK"; beside an estimate, a calm note, "This estimate is not perfect. Here is what it misses.", with one line on method.
- Moves: load - static. Calm is the point.
- Build: tag `.illus` inline-block, margin-top 24px, mono 11px caps .08em, padding 6px 10px, radius 8px, 1px ring, muted; caveat `aside.caveat` with a 2px left rule and a small icon, method detail in `<details>`. Place each right beside what it qualifies, never in a footer.
- Narrow: same · Reduced motion: same.
- Use when: an illustrative scenario could be read as a commitment, or a number is an estimate. · Avoid when: the example is real (say so instead), or it turns into hedging on every line.
- Effort: S · Needs lib: no · Sources: P038 (TVS page.html ~L213, L845), P094 https://pudding.cool/2017/03/film-dialogue/ · Verdict: KEEP (the two honesty devices merged)

---

## The ask

### PPL-27 ★ Contact card with copy button
- For: call-to-action, utility · 1 named contact (2 at most)
- Instead of: "Contact us" with a generic inbox, or a form
- Reader sees: A light rounded card on the dark closing band: the drawn portrait, "YOUR [ORGANISATION] CONTACT", a big serif name, one line on exactly what to send and what comes back, the email in a mono pill, and an ink "Copy email" button that answers "Copied".
- Moves: tap - the button presses to scale .96 over .15s ease-out; its label becomes "Copied" (or "Select and copy" when the clipboard fails) for 1800ms. The portrait pen draws on view (PPL-01).
- Build: `.contact-card` grid 150px | 1fr, gap 32px, powder background, ink text, radius 22px, padding 30px 34px, max-width 820px; name clamp(32px,3.4vw,44px); `.addr` mono 15px, `user-select: all`, paper pill radius 10px, `overflow-wrap: anywhere`; button 600 14px sans, ink, radius 10px, padding 11px 18px; `navigator.clipboard.writeText`, falling back to `getSelection().selectAllChildren(addr)`. Clear the previous reset timer before setting a new one (TVS bug 16). The "what comes back" line names the deliverable and a relative time ("a one-page plan within a week of your reply"). Two contacts: two cards stacked, each naming the one thing to send that person.
- Narrow: below 820px one column, padding 24px, portrait above the name · Reduced motion: no press scale.
- Use when: the page ends with one person to write to. · Avoid when: a form or a procurement portal is required (link it from the card, still under a named person).
- Effort: S · Needs lib: no · Code: TVS harvest · Sources: P030 (TVS page.html ~L391-405, L912-920, L1199-1205; harvest sections 2.10, 2.15) · Verdict: KEEP (the "what comes back" line and the timer fix added)

### PPL-28 ★ Three pictured steps that end at one person (new)
- For: call-to-action, sequence · 3 steps plus 1 contact
- Instead of: "Next steps: 1, 2, 3" as bullets, or a bare horizontal step strip
- Reader sees: On the dark closing band, three cards, each opening with a small drawing: a short list of options with the recommended one circled in yellow pen (what to choose), the contact in a yellow disc with signal lines (who to talk to), a document with a yellow tick (what you get next); directly below, the contact card with the drawn portrait.
- Moves: in-view - the three cards arrive at 0 / 100 / 200ms (rise 12px, 0.75s); the ring pen draws around the recommended option (1.1s cubic-bezier(.45,.05,.35,1) after .3s); the contact card's portrait pen draws when it enters view. One moving thing at a time.
- Build: the steps are SEQ-05 in order-time (`.start` grid 3 columns, gap 16px, cards rgba(244,241,234,.06) with ring rgba(244,241,234,.14), radius 16px, `.pic` 160px with 130×96 pictograms) followed by PPL-27 with PPL-01. Content rule: step 1 names the real choice and circles our pick, step 2 names the real person, step 3 names the real thing they receive and a relative time. The page ends here.
- Narrow: below 820px one column, contact card follows · Reduced motion: static, ring and portrait shown drawn.
- Use when: closing any proposal; this is the proven TVS close. · Avoid when: the first step needs more than two lines to explain (simplify the step first).
- Effort: S · Needs lib: no · Code: TVS harvest · Sources: new assembly of TVS P027 (SEQ-05), P029, P030 (TVS page.html ~L215-220, L377-405, L887-920; harvest sections 2.10, 2.14, 2.15) · Verdict: NEW

### PPL-29 Decision slip with the pick already circled (new)
- For: call-to-action, choice-fork · 2-4 options, 1 recommended
- Instead of: "Let us know how you would like to proceed"
- Reader sees: A paper slip, slightly tilted, filled in like a form: "I'd like to:" with two to four options and our recommendation circled in yellow pen, "Send to:" with the contact's name and email, "You'll get:" with the next deliverable; under it, a "Copy this reply" button.
- Moves: in-view - the slip arrives (rise 12px, 0.7s cubic-bezier(.22,1,.36,1)); the ring pen draws around the recommended option (1.1s cubic-bezier(.45,.05,.35,1)). Tap - choosing another option redraws the ring there (0.6s pen draw) and updates the reply text.
- Build: `.sheet` background #FFFDF6, radius 6px, `transform: rotate(-1.2deg)`, ruled rows 1px #D8D0C2, filled-in words in the hand face (Caveat 500) in ink #2B4A8B; options are real radio inputs styled as text, with the TVS ring SVG placed on the checked one; "Copy this reply" copies a short plain-text reply built from the checked option, using the PPL-27 clipboard code; a `mailto:` link carries a subject only, no personal data in the URL.
- Narrow: below 820px no tilt, full width · Reduced motion: ring shown drawn; it moves instantly on change.
- Use when: the reader must pick one of a few concrete next steps and you have a recommendation. · Avoid when: there is only one next step (use PPL-30 or PPL-28).
- Effort: S · Needs lib: no · Code: TVS harvest · Sources: new; built from the TVS paper sheet and hand-drawn ring (harvest section 2.14) and the prefilled brief idea in P082 (https://ncase.me/remember/) · Verdict: NEW

### PPL-30 The only question left
- For: call-to-action, big-idea · 1 question, 1 action
- Instead of: a closing section with three buttons and a newsletter sign-up
- Reader sees: After the evidence, a near-empty screen on the closing tint with one large line ("The only question left: which batch starts first?"), the key words swept by the marker, and one button that names the action and the person ("Write to Priya").
- Moves: in-view - the line arrives (rise 12px, 0.8s cubic-bezier(.22,1,.36,1)); the marker sweep follows (0.7s after .35s); the button arrives 0.4s after the line (rise 12px). Nothing else on the screen moves.
- Build: section `min-height: 80svh`, grid `place-items: center`; h2 serif clamp(2rem,5vw,3.5rem); exactly one `<a class="cta">`, no secondary links on this screen; it goes to the PPL-27 card or a `mailto:` with a subject. The question is the one the evidence left open, phrased so yes is the natural answer.
- Narrow: same · Reduced motion: static, sweep complete.
- Use when: the page has removed every other doubt and one decision remains. · Avoid when: the reader still needs price or terms first (put AMT-12 or PPL-18 before it).
- Effort: S · Needs lib: no · Sources: P043 https://www.bloomberg.com/graphics/2015-whats-warming-the-world/ · Verdict: ADAPT, changed: marker sweep added; the button must name the person and the action.

### PPL-31 Reply already written
- For: call-to-action, utility · 2-3 first steps
- Instead of: an empty contact form, or a "Get in touch" button that leaves the reader wondering what to say
- Reader sees: Under the closing question, two or three chips, each a real first step ("Book the site visit", "Send me the sample lesson"), one of them primary; each has a one-line "what happens next" under it, and tapping one opens an email or WhatsApp message to the named contact, already written.
- Moves: tap - the chip presses (translateY 1px, .15s ease-out); nothing else moves.
- Build: chips are links to `mailto:<contact>?subject=…&body=…` or `https://wa.me/<number>?text=…` with generic prefilled text (no personal data in URLs); the primary chip takes the accent fill, the others a 1px ring; a "Copy the message" fallback uses the PPL-27 clipboard code.
- Narrow: below 820px chips stack full width · Reduced motion: no press.
- Use when: readers hesitate because they do not know what to write. · Avoid when: you would need more than 3 chips, or the contact does not use that channel.
- Effort: S · Needs lib: no · Sources: P214 https://www.framer.com, P082 https://ncase.me/remember/ · Verdict: ADAPT, changed: merged; capped at 3 chips; the editable textarea brief became prefilled messages; arrow nudge cut.

### PPL-32 Two doors, each with its time and its person
- For: call-to-action, choice-fork · 2 options
- Instead of: one "Contact us" button for readers at different stages of readiness
- Reader sees: Two large cards at the end, one to start now ("Start the pilot") and one to talk first ("A short call with Priya"); each says how long it takes, who answers, and what arrives next.
- Moves: tap - the whole card is the link; hover and focus deepen the shadow only (no travel), focus ring 2px in the accent; no arrow animation.
- Build: two-column grid of anchor cards, gap 16px, radius 18px; a mono time pill on each ("about 10 min"); the start card in the accent fill, the talk card with a 1px ring; each ends with the contact's name and a 40px portrait from PPL-01.
- Narrow: below 820px stacked, start card first · Reduced motion: no shadow change.
- Use when: readers arrive with mixed readiness. · Avoid when: a third door seems needed, or one option is clearly right (use PPL-30).
- Effort: S · Needs lib: no · Sources: P215 https://stripe.com · Verdict: ADAPT, changed: the arrow out-and-back hover cut; each door names who answers and what comes next.

### PPL-33 Every thread ends at one name (new)
- For: call-to-action, many-to-many · 3-6 earlier sections converging on 1 contact
- Instead of: a recap list of everything the page said, placed before the button
- Reader sees: The page's recurring drawings (the needs, the teams, the steps) come back as small line icons around the closing band, and a pen line runs from each one into the contact's portrait at the centre, so every idea visibly ends at one person and one ask.
- Moves: in-view - the icons sit as construction lines; then each thread pen draws from its icon to the portrait (0.6-1.2s by length, next at 80-85%), and each icon turns full ink as its thread leaves; the ask line and button arrive last (rise 12px, 0.7s cubic-bezier(.22,1,.36,1)). Once.
- Build: SVG overlay on the closing band; icons reused from the page's sprite (`<use href="#i-…">`); thread paths from icon and portrait centres measured with `getBoundingClientRect()` on load, resize and `document.fonts.ready`, curved like the TVS snake (`C x0 (y0+dy×.55), x1 (y1-dy×.55), x1 y1`); portrait from PPL-01, card from PPL-27.
- Narrow: below 768px static twin: the icons in one row above the portrait with short straight threads, all drawn · Reduced motion: all threads drawn.
- Use when: the page covered several needs and the reader should feel they all come down to one decision and one person. · Avoid when: the page has one idea (use PPL-30), or earlier sections had no recurring drawings to call back.
- Effort: M · Needs lib: no · Code: TVS harvest · Sources: new; built from the TVS snake curve and constellation (harvest sections 2.2, 2.3); keeps the "close gathers the proof" idea of P216 (https://tympanus.net/codrops/2026/03/02/sticky-grid-scroll/) without its 425vh pin · Verdict: NEW

---
