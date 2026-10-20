# Structure and links: hierarchy, many-to-many, part-whole, place-network

Pattern library family for `pitch-site`. 42 entries (9 starred), curated from slice2 (67 raw entries).
Verdicts: 7 KEEP, 28 ADAPT, 7 NEW, 15 CUT (listed at the end). 17 raw entries were merged into others; every entry lists all its source ids.

**Shorthand used in every entry (house motion values):**
- **pen draw**: stroke-dashoffset from length to 0, duration = length / 600 px/s, clamped 0.6-2.2s, next stroke starts at 80-85% of the previous one, ease cubic-bezier(.45,.05,.35,1).
- **arrives**: opacity 0 to 1 plus a rise of 16px or less (12px default), 0.6-1.0s, cubic-bezier(.22,1,.36,1). Staggers 60-110ms, total capped at 450ms. Nothing enters from the side.
- **reveals once**: text arrives the first time it enters the view and always finishes; it never reverses on scroll-up.
- **scroll-linked**: linear, tied 1:1 to progress. Drawings may follow scroll back and forth; text never does.
- **construction line**: the faint dashed version of a link (about 25% ink, dash "2 6") shown before it is explained; it pen draws solid when its caption arrives.
- **pinned**: a sticky stage whose section is 3 viewport heights or less, with an `n / N` counter, and a stacked static twin below 768px.
- **accent**: the one colour that points. Everything else is ink, paper and chalky flat tints. Texture never animates.
- **team chips**: the TVS colour-coded pills (P010); a team keeps its tint everywhere on the page and always shows its name.

---

## Family picker

Pick by what the content is, how many items, and how the items relate. Starred first. If unsure: who-does-what goes to STR-02, a hierarchy to STR-01, a part-whole to STR-24, a place to STR-36.
Cross-family: problems that form a chain go to the snake (SEQ-01); one team per need goes to need cards (P009); a generic pinned drawing with captions is SEQ-02.

**Who does what (many teams to many problems, the most common proposal shape)**
- Teams and problems, 3-7 each, linked, told one problem at a time: STR-02 ★, STR-06, STR-07.
- The team is the subject (3-6 teams), 4-8 problems pass by, linked: STR-03 ★, STR-08.
- One centre, 3-5 services, up to 16 leaves each tagged with a team, grouped: STR-01 ★, STR-10.
- 16-30 leaves under 4-6 services, grouped: STR-10, STR-20.
- Needs, our work and outcomes, 3-6 per column, linked: STR-04 ★, STR-05.
- Proving no need is left uncovered, 4-8 needs by 3-8 teams, grouped: STR-05, STR-07.
- One organisation whose teams work at the same time, 4-12, equal: STR-03 ★, STR-08.
- Separate organisations or sites with hand-offs, 5-12, linked: STR-09, STR-37 (exactly two parties).
- Teams working in parallel toward shared hand-offs, 2-4 streams, sequential: STR-40, STR-06.
- Problems shared by most teams, joint ownership is the point, 3-6 teams: STR-02 ★, STR-06.

**Many-to-many beyond teams**
- Today's tangle against our single centre, 4-7 parties, opposed: STR-11 ★, STR-13.
- Parts that strengthen each other, 4-8, linked equals: STR-12, STR-13.
- Many pieces serve one result, 4-12, equal: STR-13, STR-18.
- Many sources feed every output, 3-8, linked: STR-04 ★, STR-16.
- Reach spreading through people, 8-30 nodes, sequential: STR-14, STR-15.
- One route through a network, 5-15 nodes, sequential: STR-15, STR-36.

**Hierarchy**
- Ranked levels, 3-6, built from the ground up: STR-17 ★, STR-18.
- Nested levels around one centre, 2-5, grouped: STR-18, STR-21.
- 1 root, 3-6 branches, up to 24 leaves, grouped: STR-01 ★, STR-19.
- Branches that all finish one sentence, 3-6: STR-19, STR-20.
- 12-40 items, up to 3 deep, grouped: STR-20, STR-10.
- In scope against out of scope, 2-5 sets, opposed: STR-21, STR-31.
- Layers that exist at the same time, 3-6, equal: STR-22, STR-08.
- Whole down to one detail, 3-5 nested levels, sequential: STR-26 ★ (pulling out), STR-23 (zooming in).

**Part-whole**
- A system of 4-8 parts built up one at a time, sequential: STR-24 ★, STR-27.
- What is hidden inside a familiar thing, 1 shell and 1-4 parts: STR-25 ★, STR-29.
- One piece inside a much larger whole, 1 in 1: STR-26 ★, STR-23.
- A bundle of 3-7 parts the client never sees, equal: STR-27, STR-28.
- Naming 4-20 parts across several drawings, equal: STR-28, STR-30.
- One joint or hand-off where the risk lives, 1-4 details: STR-29, STR-23.
- Two or three overlapping sets, opposed then joined: STR-31, STR-21.
- Shares of time or budget, 4-15, ranked by size: STR-32, STR-34.
- Amounts of very different sizes, 5-30, ranked: STR-34, STR-32.
- One share of a crowd, or n equal deliverables, 6-100 units: STR-33, STR-35.
- Auditing 3-12 units against one standard, grouped: STR-35, STR-05.
- Proof that the plan is measured, 3-12 notes: STR-30, STR-28.

**Place-network**
- Two parties exchanging things, 3-6 crossings, opposed sides: STR-37, STR-09.
- 3-8 stops in order, sequential: STR-36, STR-40.
- One world told scene by scene, 5-12 scenes, sequential: STR-38, STR-39.
- A landscape and where the client stands in it, 5-15 places: STR-39, STR-41.
- 6-40 regions by phase, grouped: STR-41, STR-33.
- Feel the scale of a place before the detail, 1 in 1: STR-26 ★, STR-23.
- Place matters behind another drawing, modifier: STR-42.

---

## Who does what

### STR-01 ★ Constellation mind map
- For: many-to-many, hierarchy, place-network · 1 centre, 3-5 branches, 8-16 leaves
- Instead of: a bulleted list of teams under each service
- Reader sees: The core idea in the middle, four branch names around it, and leaves that pair a short phrase with a small-caps team name; the map grows outward from the centre, and touching a branch quiets the others.
- Moves: in-view (threshold .3) - delay by distance from the centre: delay = .08 + .72 × min(1, dist / 560) s; lines pen draw (pathLength 1, dashoffset 1 to 0, .9s) at delay × .8; dots fade .5s at delay + .2; labels arrive (16px rise, .9s) at delay + .35 (+.05 phrase, +.12 team). Ambient, after the draw: one 2.6px accent pulse at a time walks the edges from the centre outward (first 45% of a 4400ms cycle, opacity sin(πu) × .9). Hover or tap a branch: the other groups dim to .22 over .3s; tap outside clears.
- Build: one SVG, viewBox 1100×700, hand-placed coordinates in a MAP object; three groups (lines, dots, text) so text sits on top; text `paint-order:stroke` with a 12px halo in the section colour; centre serif 36px, branch serif 27px, leaf sans 16px, team mono 11px caps. Every element carries `data-g` (branch id); `setHot(g)` is bound to pointerenter on hover devices and to click everywhere.
- Narrow: <768px (TVS used 820px) the SVG hides and `.map-list`, built from the same MAP, shows each branch as an h3 plus a list (phrase, team in mono caps) · Reduced motion: drawn at once, no pulse.
- Use when: showing who serves what across a whole offer on one screen. · Avoid when: more than ~16 leaves (use STR-10), or the content changes often (coordinates are hand-placed).
- Effort: M · Needs lib: no · Code: TVS harvest · Sources: P022 (TVS page.html L184-199, L246-250, L801-802, L1207-1259), P039 (list twin) · Verdict: ADAPT, changed: pulses run one at a time instead of on every edge at once; tap now does what hover did; label rise 18 to 16px and 1.1s to .9s; lines on the pen ease.

### STR-02 ★ Switchboard (new)
- For: many-to-many, people-roles · 3-7 problems by 3-7 teams, up to ~20 links
- Instead of: a bulleted list of teams under each problem
- Reader sees: Problems in a left column and teams in a right column, with the real links pencilled between them as faint dashed lines; each chapter inks one problem's links solid, and the last chapter shows how many problems each team carries.
- Moves: scroll-linked (pinned) - entering a chapter pen draws that problem's cords and gives the problem and its teams the accent; earlier cords settle to 40% ink; scrolling back un-inks the step; captions reveal once. Final chapter: a count pill arrives beside each team ("carries 3").
- Build: section height min(300vh, chapters × 50vh) with a sticky 100vh stage; two HTML label columns under one SVG overlay. Each link is two copies of `M x0,y0 C xm,y0 xm,y1 x1,y1` measured from the label edges on load, resize and `document.fonts.ready`: a construction line, and an ink copy with `pathLength="1"` drawn from dashoffset 1 to 0. Links carry `data-p` and `data-t`; the chapter index comes from an IntersectionObserver on caption blocks with `rootMargin:"-50% 0px -50% 0px"`.
- Narrow: <768px static twin: one card per problem with team chips in an "answered by" footer (P009), then one line per team with its count · Reduced motion: all cords inked, counts shown.
- Use when: several teams each take several problems and the reader asks "who handles mine?" · Avoid when: more than ~7 per side or ~20 links (use STR-05).
- Effort: M · Needs lib: no · Sources: new; cord curve from P111, construction line plus ink copy from the TVS snake (P013), "answered by" footer from P009 · Verdict: NEW

### STR-03 ★ Pinned cast, problems scroll past (new)
- For: many-to-many, people-roles · 3-6 teams, 4-8 problems per pinned section
- Instead of: a team section of names and bios followed by a separate problem list
- Reader sees: One line drawing of the whole team, each team drawn as its own bench or tool (a lectern, a ledger, a loom) with its chip, stays pinned while problem captions scroll past; at each caption only the teams who take that problem ink in and take the accent, the rest stay pencil-faint.
- Moves: scroll-linked (pinned) - each caption crossing mid-screen sets the step; the involved teams' outlines pen draw and fill with the accent tint over .6s; the others fade to 30%; captions reveal once (12px, .7s). The last step lights every team with its problem count.
- Build: two-column grid; `figure` is `position:sticky; top:10vh; height:80vh`; `.step` captions sit 40vh apart; section 300vh or less (split into two sections past 8 steps). Each step carries `data-teams="b d"`; an IntersectionObserver with `rootMargin:"-45% 0px -45% 0px"` sets `figure.dataset.step` and toggles `.on` on the matching `<g data-team>`. Team outlines use `pathLength="1"`; idle teams wear the construction-line dash at 30% ink. Never a face icon.
- Narrow: <768px static twin: each caption card carries a 120px copy of the stage (`<use href="#stage">`) with its teams lit, plus team chips · Reduced motion: the final step (all teams, counts) with captions as static cards.
- Use when: the team itself is the pitch and the reader should feel the same people cover everything. · Avoid when: each problem has exactly one team (use need cards, P009), or more than 6 teams crowd the stage.
- Effort: M · Needs lib: no · Sources: new; pinned subject with one change per step from the Washington Post scrollytelling reference; step mechanics from SEQ-02 (P167, P102) · Verdict: NEW

### STR-04 ★ Effort river (needs, work, outcomes)
- For: many-to-many, cause-effect · 3-6 needs, 3-6 work streams, 2-4 outcomes, up to ~25 links
- Instead of: three bulleted columns: "your needs", "our services", "results"
- Reader sees: Three columns (your needs, our work, what changes) joined by soft ribbons; one need at a time lights its whole path through the work to its results.
- Moves: scroll-linked (pinned) - every ribbon starts as a construction line; each chapter pen draws one need's path solid from left to right and dims the rest to 12%; the last chapter shows every ribbon at 35% with the caption "lines show what feeds what, not how much". Outside the pinned run, tapping a need does the same.
- Build: nodes are rects at column x 0, 45% and 90%, stacked with 10px gaps. Each link is `M x0,y0 C xm,y0 xm,y1 x1,y1`, stroke-opacity .35, every ribbon the same 12-16px width. Vary width only when the brief states shares (then filled ribbons wiped in with `clip-path: inset(0 100% 0 0)` to `inset(0)`). Link ids live in each node's `data-links`; toggle `.lit`. With worked cases, draw one equal band per real case, named on tap.
- Narrow: <768px static twin turned vertical (needs at top, outcomes at the bottom), each need a card listing its work and outcomes · Reduced motion: the final state; tap highlight still works.
- Use when: many needs map to overlapping work and outcomes, and the reader asks "which part is for my problem?" · Avoid when: links are one-to-one (need cards do it), more than ~25 links, or the flows cross heavily.
- Effort: M · Needs lib: no · Sources: P111 https://datavizcatalogue.com/methods/sankey_diagram.html, P328 https://github.com/Financial-Times/chart-doctor/tree/main/visual-vocabulary, P112 https://datavizcatalogue.com/methods/parallel_sets.html · Verdict: ADAPT, changed: told one need per chapter instead of flowing in at once; ribbons start as construction lines; parallel sets folded in as the worked-cases mode.

### STR-05 Who-covers-what dot matrix
- For: many-to-many, people-roles, proof-trust · 4-8 needs by 3-8 teams or capabilities
- Instead of: a team list with skills under each name
- Reader sees: Their needs down the side, the team across the top, a dot wherever someone answers a need, and a count at the end of each row, so no need is left empty.
- Moves: scroll-linked or in-view - rows fill top to bottom as each need is named, dots arrive 90ms apart (capped at 450ms per row); the most important need is lit by default. Hover or tap a cell, a team or a need: its row and column light like a crosshair, the rest drop to 30%.
- Build: CSS grid, no table rules. A dot means yes; use strength levels (empty, ring, half, full, with a legend) only when the brief states them. Crosshair via a JS class on the row and column, or `.m:has([data-p="2"]:hover) [data-p="2"]{opacity:1}` plus a click handler that does the same. Row end shows a derived count ("3 cover this"); an empty row gets a dashed accent ring as the honest gap.
- Narrow: <768px static twin: one open card per need listing its team chips · Reduced motion: static, all dots shown.
- Use when: proving coverage, every need answered by someone. · Avoid when: the mapping is one-to-one, or the team is one or two people (use the persona portrait).
- Effort: S · Needs lib: no · Sources: P132 https://www.rawgraphs.io/learning, P258 https://vicosight.com/news/5-design-trends-for-annual-reports · Verdict: ADAPT, changed: yes or no dots by default; rows fill as needs are named; tap added for every hover; gaps marked in the accent.

### STR-06 Round table (new)
- For: many-to-many, people-roles · 3-6 teams, 3-8 problems
- Instead of: a "how we will work together" paragraph
- Reader sees: A line drawing of one round table seen from above with a seat for each team and its chip; each chapter lays a problem card in the middle, lines draw from it to the seats that pick it up, and those seats each gain a small numbered token, so by the end every seat shows its load.
- Moves: scroll-linked (pinned) - the table pen draws once; per chapter the card arrives (8px, .7s), its lines pen draw from the centre to each seat, tokens arrive .6s after their line lands; the previous card fades out but its tokens stay.
- Build: SVG viewBox 800×800, table circle r 200, seats at angle 2πi/n on r 260 (geometry as the TVS teaching circle, P026); problem card is HTML centred over the SVG; lines are straight paths with `pathLength="1"`; tokens are 18px circles carrying the problem number, stacked along each seat's outer edge.
- Narrow: <768px static twin: problem cards with seat chips, then a row per team showing its tokens · Reduced motion: the final table with every token and a numbered problem key beside it.
- Use when: the pitch is shared ownership and most problems need two or more teams. · Avoid when: hand-off order matters (use STR-40), or each problem has one team.
- Effort: M · Needs lib: no · Sources: new; seat geometry from P026 (TVS teaching circle) · Verdict: NEW

### STR-07 Kolam loop matrix (new)
- For: many-to-many · 3-6 problems by 3-6 teams
- Instead of: a tick table of who does what
- Reader sees: A grid of kolam dots, teams named across the top and problems down the side; for each problem one unbroken line runs along its row and loops around the dots of the teams that take it on, so the finished drawing is both a kolam and the answer.
- Moves: in-view or scroll-linked per row - each row's line pen draws left to right (whole row 2.2s or less), the next row starting at 80-85%; each looped dot fills with the accent as the pen passes it.
- Build: SVG, 6px dots at 64px spacing. One path per row: straight runs between columns, a cursive loop that circles an involved dot once (two cubic segments, radius about 18px), a shallow dip under an uninvolved one. Record the path length at each loop while building the `d` string (measure a temporary path); dot delay = length at loop / total length × duration. Static rice-powder filter (P003) on the strokes. Caption under the grid: "a loop means this team takes it on".
- Narrow: <768px up to 5 teams at 44px spacing, drawn static; beyond that, need cards with team chips · Reduced motion: all loops drawn, looped dots filled.
- Use when: the reader is Indian or craft-minded and the who-does-what grid should feel made, not filled in. · Avoid when: more than 6 per side, or the loops would read as decoration (test the caption on someone).
- Effort: M · Needs lib: no · Sources: new; kolam stroke and filter from P001 and P003 (TVS harvest) · Verdict: NEW

### STR-08 Floor plan with the roofs off
- For: part-whole, many-to-many, people-roles · 4-12 rooms in 2-4 wings
- Instead of: an org chart of boxes
- Reader sees: A line-drawn floor plan of one organisation or offer seen from above, each room a team or part, doorways where rooms hand work to each other; each chapter lifts one room's roof to show the work inside and inks its doorways.
- Moves: in-view then scroll-linked (pinned) - walls pen draw once, one wing at a time; per chapter one roof lifts and fades (8px, .7s), its doorway paths go from construction line to solid. No sideways pan.
- Build: CSS grid with `grid-template-areas`; rooms are divs with 2px walls; doorways are gaps made with pseudo-elements. Or one oblique SVG with a roof `<g>` per room. Rooms are equal within a wing, captioned "room size is not importance". Chapter steps from an IntersectionObserver on the captions.
- Narrow: <768px static twin: wings stack, two rooms per row, every roof off · Reduced motion: roofs off, walls drawn.
- Use when: the offer or team should feel like one structure whose parts work at the same time. · Avoid when: the parts are steps in order (use the snake, SEQ-01).
- Effort: M · Needs lib: no · Sources: P137 https://datavizcatalogue.com/methods/treemap.html, P285 https://en.wikipedia.org/wiki/Emakimono · Verdict: ADAPT, changed: the handscroll's sideways pan dropped; roofs lift one per chapter on a pinned plan; walls pen draw.

### STR-09 Village of teams
- For: place-network, many-to-many · 5-12 parties
- Instead of: a partner logo wall
- Reader sees: The programme drawn as a small village: each team or partner is a house, paths between them are the hand-offs, district names sit in small caps, and tapping a house opens its card.
- Moves: in-view - houses pen draw in two waves (outlines, then details); paths start as construction lines. scroll-linked - each chapter inks one hand-off path and lifts its two houses 2px. Tap a house: it lifts 2px, unrelated paths dim to 30%, its card arrives (.6s).
- Build: one flat hand-drawn SVG (top-down or simple isometric, no WebGL); `<g data-node>` per house; paths carry `data-from` and `data-to`; district labels in mono caps. The tap handler toggles `.focus` on the node and every path whose ends match; the card is an aside or a `<dialog>`.
- Narrow: <768px static twin: the map at full width with every path inked, then one card per house listing its hand-offs · Reduced motion: map finished, all paths solid.
- Use when: the reader needs to see who exists and how they connect, especially separate organisations. · Avoid when: the parts have no real relations (use a list).
- Effort: L · Needs lib: no · Sources: P411 https://townhouse.dev · Verdict: ADAPT, changed: hand-off paths start dashed and ink one per chapter; card opens at house arrival timing.

### STR-10 Constellation in chapters (new)
- For: hierarchy, many-to-many · 1 centre, 4-6 branches, 16-30 leaves
- Instead of: squeezing 30 leaves into one radial map, or one long list per service
- Reader sees: The constellation's centre and branch names stand pencil-faint; as you scroll, one branch at a time inks itself and its leaves arrive, the branches already explained settle to grey, and the final step shows the whole map lit.
- Moves: scroll-linked (pinned) - the branch and its leaf lines pen draw in distance order; leaves arrive (12px, .7s) 80ms apart, capped at 450ms; one accent pulse runs once along the new branch toward the centre; settled branches drop to 45% opacity.
- Build: reuse the TVS constellation (MAP object, three SVG groups, `data-g` per branch) and replace its single `.pre` class with one class per branch, toggled by an IntersectionObserver on the chapter captions. Leaves past 4 per branch sit on a second ring 140 units further out; the viewBox may grow to 1100×800.
- Narrow: <768px the TVS map-list twin (an h3 per branch, leaves with the team in mono caps) · Reduced motion: whole map drawn, every branch at full ink.
- Use when: the map has too many leaves to land in one glance. · Avoid when: fewer than ~12 leaves (use STR-01).
- Effort: M · Needs lib: no · Code: TVS harvest (base map) · Sources: new; built on P022 and P039 · Verdict: NEW

---

## Many-to-many beyond teams

### STR-11 ★ Tangle to line
- For: many-to-many, before-after, opposed · 4-7 parties or tools
- Instead of: a "today" and "with us" pair of bulleted columns
- Reader sees: Five boxes (today's tools or middlemen) joined by crossing, knotted lines; as you scroll, the knots unpick and every line reroutes through one centre.
- Moves: scroll-linked (pinned) - the new centre shows first as a dashed outline; each connector morphs from its tangled path to its clean path with progress, boxes glide to their tidy places by transform, and the centre draws solid when the last line arrives; the caption states the cost ("it takes 6 systems to pay one bill").
- Build: SVG. Author each connector twice, "tangled" and "clean", with identical command structure; parse their numbers and lerp them by p. Boxes move with `transform`. Cap the section with `min(200vh,1600px)` on tablets and `min(300vh,2800px)` on laptops, as Ramp does, under a 200-260px top fade in the paper colour.
- Narrow: <768px static twin: the before and after drawings stacked, captioned "today" and "with us" · Reduced motion: before and after side by side.
- Use when: the reader's current setup is many disconnected parties or tools. · Avoid when: the "after" is still complicated.
- Effort: L · Needs lib: no · Sources: P192 https://ramp.com · Verdict: ADAPT, changed: centre drawn dashed then solid; fade in paper colour, not white; static twin on narrow.

### STR-12 Ring of mutual support
- For: many-to-many, part-whole · 4-8 parts, up to 15 links
- Instead of: "an integrated approach" in a sentence
- Reader sees: The capabilities sit around a circle; curved lines across the middle join the ones that feed each other, one pair explained at a time.
- Moves: in-view then scroll-linked - the rim pen draws once; every real link shows as a construction line; each step pen draws one pair solid and names it in a caption ("training feeds the pilots"). Tap a capability to keep only its chords lit.
- Build: nodes are arcs on radius R via `A` commands, each 360/n degrees minus a 4° gap. Chords are single strokes `M a Q 0,0 b` inside a group translated to the centre. Switch to filled ribbons (`M a1 Q 0,0 b1 A r r 0 0 1 b2 Q 0,0 a2 Z`, fill-opacity .3) only when width means something. Equal arcs; a chord exists only where the brief says one thing supports another.
- Narrow: <768px static twin: a 320px ring with every chord inked, labels in a key below, plus "X helps Y" lines · Reduced motion: final state.
- Use when: the pitch is "these parts make each other stronger". · Avoid when: the relation is a sequence, or more than ~8 parts.
- Effort: M · Needs lib: no · Sources: P113 https://datavizcatalogue.com/methods/chord_diagram.html · Verdict: ADAPT, changed: single-stroke chords drawn one pair per step instead of filled ribbons growing at once.

### STR-13 Hub and spokes
- For: many-to-many (many to one), hierarchy · 1 centre, 4-12 around it
- Instead of: a list of services under "everything you need"
- Reader sees: The reader's goal in a circle at the centre; people, tools and partners sit around it, each joined by a spoke, so every piece visibly serves one result.
- Moves: in-view - the hub arrives; spokes pen draw outward clockwise; satellites arrive at the spoke ends; then one accent pulse travels each spoke inward once (`offset-distance` 0 to 100%, .8s), one spoke at a time. No rotation.
- Build: SVG; satellite angle = i / n × 360°, positions computed once. Optional gentle swirl: `M rim Q c 0,0` with the control point at rim × 0.4 rotated 15°. Labels are absolutely positioned HTML so they wrap. Type (people, tools, partners) shows as a chalk tint; the accent is kept for the pulse.
- Narrow: <768px static twin: a vertical spine with spokes as short horizontal ticks and labels as a list · Reduced motion: static, no pulse.
- Use when: everything serves one outcome. · Avoid when: the items have an order, more than ~12 satellites, or the satellites also link to each other (use STR-12).
- Effort: S · Needs lib: no · Sources: P115 https://datavizproject.com/data-type/radial-convergence/, P325 https://developer.mozilla.org/en-US/docs/Web/CSS/offset-path · Verdict: ADAPT, changed: radial convergence and hub-and-orbit merged; one inward pulse per spoke, once, one at a time.

### STR-14 Ripple by hops
- For: many-to-many, place-network, cause-effect · 8-30 nodes
- Instead of: "your message will reach thousands" as a bare claim
- Reader sees: A network of dots; one node is lit, then step by step the rings it reaches light up (one hop, two hops, three hops) with a running count.
- Moves: scroll-linked (pinned) - one step per hop with "2 / 3 hops · 14 reached"; that hop's edges pen draw from construction lines to solid, then its nodes fill with the accent (.4s); earlier hops settle to ink.
- Build: precompute hop distance with breadth-first search; nodes carry `data-hop`; step n adds `.lit` to every node with hop ≤ n and inks its edges. Positions hand-placed or precomputed (no runtime force simulation).
- Narrow: <768px static twin: the final graph with at most 12 nodes, shaded by hop · Reduced motion: final graph shaded by hop.
- Use when: reach compounds through relationships (partners sharing to their own audiences). · Avoid when: the network is invented.
- Effort: M · Needs lib: no · Sources: P072 https://distill.pub/2021/gnn-intro/ · Verdict: ADAPT, changed: edges go from construction line to solid per hop; counter added; static twin on narrow.

### STR-15 One path through the network
- For: many-to-many, place-network, sequence · 5-15 nodes
- Instead of: a list of integrations or touchpoints
- Reader sees: Dots joined by faint lines; one path through the network lights up node by node, the reader's own journey, while the other links stay faint.
- Moves: in-view - nodes arrive 60ms apart (capped at 450ms); then the path pen draws node to node; visited nodes fill with the accent.
- Build: precomputed SVG positions (no force simulation); every link a `pathLength="1"` path; base links are construction lines; the path's links ink in order.
- Narrow: <768px static twin: only the highlighted path, vertical, with the caption "and 9 more connections" · Reduced motion: static, path drawn.
- Use when: integrations, partners or touchpoints with one route that matters. · Avoid when: the whole network is the message and has more than 15 nodes (use STR-14).
- Effort: M · Needs lib: no · Sources: P327 https://github.com/Financial-Times/chart-doctor/tree/main/visual-vocabulary · Verdict: KEEP (stagger raised from 40 to 60ms; link draw on pen values).

### STR-16 Provenance chips
- For: many-to-many, proof-trust · 3-8 sources feeding many lines
- Instead of: a list of "data sources we use"
- Reader sees: Every finding or output line carries a small chip ("From WhatsApp", "From the ledger", "From the field visit"), so the reader sees the work draws on what they already have.
- Moves: in-view - each chip arrives (4px, .6s) just after its line.
- Build: inline-flex chip 22px tall, 1px hairline border (0.5px on 2x screens, as Linear does), 14px icon, 12px label: `<span class="from"><svg/>From Gmail</span>`. One tint per source, kept across the page like team chips.
- Narrow: <768px chips drop below their line · Reduced motion: static.
- Use when: the value is joining sources the reader already uses. · Avoid when: there is only one source.
- Effort: S · Needs lib: no · Sources: P186 https://claude.com/product/overview · Verdict: ADAPT, changed: the 160ms scale pop replaced by a small arrival.

---

## Hierarchy

### STR-17 ★ Layers ladder
- For: hierarchy, ranked-list · 3-6 levels
- Instead of: a bulleted list of audiences or levels
- Reader sees: Stacked translucent rows, senior or outcome at the top and foundation at the bottom, with a vertical line at the left that rises from the bottom; the dot beside each row turns marker yellow as the line passes.
- Moves: in-view (threshold .4) - spine scaleY 0 to 1 over 2.2s cubic-bezier(.45,.05,.35,1) after .3s; each row lights when the spine reaches it (TVS: 600ms + i × 560ms for 4 rows); dot fill .4s ease.
- Build: `.layers` grid gap 12px, padding-left 46px, max 880px; `.spine` absolute left 14px, top and bottom 22px, 2px ink, transform-origin bottom; `.layer` grid 200px | 1fr, gap 24px, padding 18px 22px, radius 14px, background rgba(255,255,255,.5); `::before` 14px dot at left -38px with a 2px ink ring, `.lit` fills it with the marker. Mono 12px for who, serif 20px for what, with one `<mark>`. Layer-cake use: label left, impact right, foundation at the bottom.
- Narrow: <768px (TVS used 820px) label stacks over text, one column, gap 4px · Reduced motion: all lit, spine full.
- Use when: one offer differs by level, or "what has to be true before X", and building from the ground up should be implied. · Avoid when: the levels are not ordered or not dependent.
- Effort: S · Needs lib: no · Code: TVS harvest · Sources: P016 (TVS page.html L100-108, L553-559, L965-976), P344 https://github.com/Financial-Times/chart-doctor/tree/main/visual-vocabulary · Verdict: KEEP (spine 2.4 to 2.2s; layer cake folded in).

### STR-18 Rings drawn inside out
- For: hierarchy, grouped-list · 2-5 nested rings around one centre
- Instead of: "core team, extended team, partners" as three bullets
- Reader sees: Circles draw themselves around a centre one at a time, nearest first, each getting its name at 12 o'clock.
- Moves: in-view - each ring pen draws from 12 o'clock (duration from its circumference), the next starting at 80% of the previous; each label arrives (8px, .6s) 220ms after its ring closes. Optional: one accent dot travels once around the outer ring after it closes.
- Build: `<circle pathLength="1" stroke-dasharray="1" stroke-dashoffset="1" transform="rotate(-90 cx cy)">` to dashoffset 0. Thick bands are a wide stroke at 15-20% of one chalk tint; boundaries are hairline dashes. Labels sit on top of their ring at 12 o'clock, coloured to match it.
- Narrow: <768px at most 4 rings, labels move to a legend below · Reduced motion: all rings and labels static.
- Use when: levels of distance, influence, priority or reach around one centre. · Avoid when: the levels are not nested.
- Effort: S · Needs lib: no · Sources: P465 (video study key_12, burst_13; Washington Post scrollytelling reference) · Verdict: ADAPT, changed: rings draw on the pen ease with length-based duration instead of 700ms ease-out with a 150ms stagger.

### STR-19 Sentence tree
- For: hierarchy, list-of-equals · 1 root, 3-6 branches, 2-4 twigs each
- Instead of: "three pillars, each with three moves" as nested bullets
- Reader sees: One phrase on the left ("With this, your managers can") branching into endings that branch again, so following any branch reads as a full sentence.
- Moves: in-view - level by level, branch curves pen draw and endings arrive at the tips (12px, .7s) 80ms apart, capped at 450ms. Fully drawn by default; nothing to tap open.
- Build: tidy layout by leaf counts (a node's y = mean of its children, x by depth); SVG text plus bezier links `M x0,y0 C xm,y0 xm,y1 x1,y1`; one font size throughout. When the endings do not finish a sentence, label the branches as pillars and use elbow connectors (the branching-tree form).
- Narrow: <768px static twin: an indented tree, root as a heading, branches as open nested lists with elbow lines · Reduced motion: fully drawn.
- Use when: capabilities that all finish the same sentence; "lists are not lists" at its purest. · Avoid when: more than ~6 branches, long endings, or deeper than 3 levels.
- Effort: M · Needs lib: no · Sources: P158 https://www.jasondavies.com/wordtree/, P338 https://datavizcatalogue.com/search.html · Verdict: ADAPT, changed: drawn fully by default, tap-to-expand removed; branching tree folded in as the pillar form.

### STR-20 Drawn outline tree (new)
- For: hierarchy · 12-40 items, up to 3 levels
- Instead of: nested bullet points
- Reader sees: A large-type indented outline where a ruled line draws down beside each group and short elbow ticks reach out to each child as you arrive, like a pen ruling a family tree in the margin.
- Moves: in-view per group (threshold .35) - the vertical rule pen draws; elbow ticks follow 80ms apart, capped at 450ms; child text reveals once (12px, .7s); one key phrase per group gets the marker sweep.
- Build: nested `<ul>` with padding-left 28px; each `ul` holds an absolutely positioned 2px rule (scaleY 0 to 1, transform-origin top, pen ease) and `li::before` ticks 16px × 1.5px scaled from 0 with transform-origin left. TVS `onView` helper per group. Type: top level serif 24px, second sans 17px, third 15px muted.
- Narrow: <768px same, indent 18px · Reduced motion: rules and ticks drawn.
- Use when: many items with a real parent-child structure that the reader must be able to scan. · Avoid when: under ~10 items (use STR-19 or STR-01).
- Effort: S · Needs lib: no · Sources: new; draw-on idiom and `onView` from the TVS harvest (2.1) · Verdict: NEW

### STR-21 Scope nest
- For: hierarchy, part-whole, definitions-jargon, opposed · 2-5 sets
- Instead of: an "in scope" and "out of scope" bullet pair
- Reader sees: Nested rounded shapes showing what sits inside what (phase 1 inside the full plan inside your goal), with a separate dashed shape off to the side for what is out of scope.
- Moves: in-view - shapes pen draw from the outside in; the out-of-scope shape draws last as a dashed outline in its own place; each label arrives (.6s) after its shape closes.
- Build: SVG rects with a large rx, or ellipses, each `pathLength="1"`; labels at the top inside each shape; out of scope uses `stroke-dasharray: 4 6`. Euler rules: inside means subset, apart means separate, no empty overlaps.
- Narrow: <768px same, scaled; labels may move to chips below · Reduced motion: final layout.
- Use when: clarifying scope, eligibility, or "this is part of that". · Avoid when: overlaps carry the meaning (use STR-31).
- Effort: S · Needs lib: no · Sources: P138 https://en.wikipedia.org/wiki/Euler_diagram · Verdict: ADAPT, changed: the out-of-scope shape draws in place instead of sliding away.

### STR-22 Section cut
- For: hierarchy, part-whole · 3-6 strata that exist at once
- Instead of: a stack of boxes labelled "layers of our approach"
- Reader sees: An architectural slice through the client's world (soil, roots, water; or front desk, operations, data), cut surfaces bold and filled, everything beyond the cut in thin lines.
- Moves: scroll-linked - a cutting plane sweeps across the outside view and the section appears behind it; a section marker "A-A" travels with it.
- Build: SVG with an elevation group and a section group; a clipPath rect whose x follows `--p` reveals the section. Cut elements `stroke-width:3; fill:var(--ink)`; elements beyond `stroke-width:.75; stroke:var(--ctx)`. Section marker: circle, arrow and label. Pinned 150vh or less.
- Narrow: <768px static: the section only, no sweep · Reduced motion: elevation and section side by side.
- Use when: layers coexist at the same time. · Avoid when: the layers are steps or ranks (use STR-17).
- Effort: M · Needs lib: no · Sources: P241 https://en.wikipedia.org/wiki/Architectural_drawing · Verdict: KEEP

### STR-23 Zoom ladder with a scale bar
- For: hierarchy, place-network, part-whole · 3-5 nested levels
- Instead of: a paragraph that sets context before the detail
- Reader sees: One drawing; each step tightens the frame (region, site, zone, a ten-metre patch; or company, department, team, one desk) while a scale bar relabels and a small locator inset shows where you are.
- Moves: scroll-linked (pinned) - the view moves between preset frames in proportion to scroll inside each step's band, then holds; the new level's labels reveal once when the move passes 80%.
- Build: one large SVG; each step stores a viewBox string, interpolated in requestAnimationFrame (or write `--p` and use `transform: scale()` on a group with transform-origin at the target, the telescope method). The locator inset is a tiny copy of the whole with a `<rect>` mirroring the current view. Hide fine detail below a scale threshold.
- Narrow: <768px static twin: a column of framed stills, one per level · Reduced motion: hard cuts between levels.
- Use when: the problem lives in a detail that only matters once the context is set. · Avoid when: the levels are not truly nested, or there are many targets.
- Effort: M · Needs lib: no · Sources: P046 https://www.reuters.com/graphics/MYANMAR-ROHINGYA/010051VB46G/, P190 https://tympanus.net/Tutorials/TelescopeZoom/ · Verdict: ADAPT, changed: zoom ladder and telescope zoom merged; camera tied linearly to scroll; counter added; stills on narrow.

---

## Part-whole

### STR-24 ★ Build-up drawing, one part per chapter
- For: part-whole, sequence · 4-8 parts
- Instead of: a "what's included" grid of icons
- Reader sees: One pinned line drawing with the client's business as the base; each chapter draws one new part onto it in the accent, earlier parts settle to grey ink, and the last chapter shows the whole thing working.
- Moves: scroll-linked (pinned) - the new part's strokes pen draw in place, then its chalk fill arrives (.6s); captions reveal once; nothing slides in from the side.
- Build: sticky 100vh stage inside a section of 300vh or less; one SVG `<g data-step>` per part over a base drawing; paths use `pathLength="1"`; the step comes from an IntersectionObserver on the captions. Only the newest part carries the accent; each caption names the part and what it does for the reader (site, CRM, content engine, reporting).
- Narrow: <768px static twin: stacked frames, one per part, each with its new part in the accent · Reduced motion: finished drawing with numbered callouts.
- Use when: the offer is a system of parts that only works together. · Avoid when: the parts are independent, or the layers are not visually distinct.
- Effort: M · Needs lib: no · Sources: P052 https://ciechanow.ski/mechanical-watch/, P431 https://bluntumbrellas.com · Verdict: ADAPT, changed: parts draw in place instead of sliding from (120px, -60px); the soft scroll snap dropped (no scroll hijack).

### STR-25 ★ X-ray: the inside shows through
- For: part-whole, definitions-jargon, cause-effect · 1 shell, 1-4 inner parts
- Instead of: "what's under the hood" as a paragraph
- Reader sees: The outside of a familiar thing (their shop, their phone, the price) fades to a ghost and the important part inside draws itself exactly where it sits.
- Moves: scroll-linked - shell opacity 1 to .25 over ~25vh while the inner parts draw on in the accent; the shell exits .25 to 0 over the next ~12vh. The accent appears here for the first time.
- Build: two `<g>` layers at identical coordinates; shell opacity from `--p`; inner paths `stroke-dasharray:1; stroke-dashoffset:calc(1 - var(--p))` with `pathLength="1"`; leader-line labels reveal once each part is exposed. Cutaway variant, when the outside must stay readable: a mask hole whose circle radius grows 0 to 45%, its edge roughened once by `feDisplacementMap` (static).
- Narrow: <768px same · Reduced motion: ghost shell and inner parts together, static.
- Use when: the real subject is hidden inside a familiar container (the product inside the service, the cost inside the price). · Avoid when: the inner part is not physically or logically inside the outer one, or the reader has no picture of the outside.
- Effort: S · Needs lib: no · Sources: P461 (video study key_07, burst_07; Washington Post scrollytelling reference), P239 https://en.wikipedia.org/wiki/Cutaway_drawing · Verdict: KEEP (cutaway folded in as a variant).

### STR-26 ★ Pullback to the bigger picture
- For: part-whole, place-network, hierarchy, quantity-scale · 1 part inside 1 whole
- Instead of: "this is part of a larger national effort" in a sentence
- Reader sees: The camera slowly pulls back and the thing you were looking at turns out to be one small piece of something much larger, still circled in the accent.
- Moves: scroll-linked (pinned) - one scene group scales from ~8 to 1 over ~50vh, linear in log space, no overshoot; fine detail fades out below a scale threshold.
- Build: wrap the scene in one `<g>`; `s = s0 * Math.pow(s1 / s0, p)` written to `transform` each requestAnimationFrame; transform-origin at the point the reader should keep watching (often bottom centre). Hide small text below a threshold so it never shrinks into mush. Hand-drawn SVG by default.
- Narrow: <768px static twin: two stacked frames, the part close up, then the whole with the part circled · Reduced motion: the whole with the part circled in a drawn ring.
- Use when: the reader needs to feel scale or context before the details. · Avoid when: the whole is not yet introduced in words.
- Effort: M · Needs lib: no (d3-geo + topojson-client only for a true globe or map) · Sources: P460 (video study key_05, burst_05; Washington Post scrollytelling reference) · Verdict: ADAPT, changed: the camera curve cubic-bezier(.65,0,.35,1) replaced by linear scroll in log space; static twin on narrow.

### STR-27 Exploded offer
- For: part-whole, hierarchy · 3-7 parts
- Instead of: a "what you get" checklist
- Reader sees: The whole offer as one object (a kit, a box, a stacked device) that comes apart into numbered, named pieces as you scroll, each with a leader line saying what it does for them, then closes back up.
- Moves: scroll-linked (pinned) - across the first half parts move apart 24-60px along their own axes, with dashed alignment lines showing where each came from; once separation passes 80%, leader lines pen draw and labels reveal once; parts reassemble across the second half.
- Build: SVG groups with per-part `--dx` and `--dy`; `transform: translate(calc(var(--dx) * var(--p)), calc(var(--dy) * var(--p)))`; labels are HTML with leader lines in an SVG overlay. Flat line drawing, no 3D tilt.
- Narrow: <768px static twin: the exploded state, parts separated vertically, with a numbered legend · Reduced motion: exploded state with labels.
- Use when: the client pays for parts they never see (research, design, build, support) and the bundle should feel tangible. · Avoid when: the parts do not share a physical form, or there are more than 7 (IKEA dropped exploded views after customers found them confusing).
- Effort: L · Needs lib: no · Sources: P150 https://datavizproject.com/data-type/exploded-view-drawing/, P238 https://en.wikipedia.org/wiki/Exploded-view_drawing, P339 https://ciechanow.ski/mechanical-watch/ · Verdict: ADAPT, changed: three exploded views merged; the rotateX(55deg) rotateZ(-45deg) tilt dropped; one pinned scene.

### STR-28 Numbered callouts that hold across drawings
- For: part-whole, definitions-jargon · 4-20 parts
- Instead of: a glossary list under a diagram
- Reader sees: Clean line drawings with small numbers and thin lead lines; the same part keeps the same number in every drawing on the page, and a plain-language key sits below.
- Moves: in-view - lead lines pen draw from number to part (.6s each). Hover or tap key row 12, or number 12: part 12 lights in every drawing at once.
- Build: every SVG part and key row carries `data-ref="12"`; one delegated listener toggles `.hl` on all `[data-ref="12"]` for click and pointerenter. Number clockwise from 1, lead lines never cross, never on a hatched area, minimum 12px. Plus-marker hotspots ("+" turning to "×" in .2s, one note open at a time) only when a key cannot fit.
- Narrow: <768px the key becomes tap chips that light parts, every label listed · Reduced motion: no line draw.
- Use when: the same components reappear across several diagrams and consistency builds trust. · Avoid when: fewer than 4 parts.
- Effort: M · Needs lib: no · Sources: P240 https://blueironip.com/ufaqs/how-should-reference-characters-be-used-in-patent-drawings/, P432 https://bluntumbrellas.com · Verdict: ADAPT, changed: tap now does what hover did; plus markers kept only as the overflow form.

### STR-29 Detail bubble
- For: part-whole, emphasis · 1 overview, 1-4 details
- Instead of: a zoomed screenshot pasted under the diagram
- Reader sees: An overview drawing with a small circle on one spot; the circle swells along a leader line into an enlarged round "Detail A, 1:5" showing exactly how two pieces join (how the hand-over works).
- Moves: in-view or on its caption step - the leader line pen draws, then the circle scales up along it into a large round panel (.8s cubic-bezier(.22,1,.36,1)); tap the panel to send it back to its marker.
- Build: the detail is a second SVG inside `clip-path: circle()`; animate `transform: translate() scale()` from the marked spot's coordinates to the panel position. Label "Detail A, 1:5" in drawing-office caps (mono 11px).
- Narrow: <768px the detail opens full width below the overview · Reduced motion: detail shown beside the overview.
- Use when: one joint or hand-off is where the risk lives. · Avoid when: every part needs equal detail.
- Effort: M · Needs lib: no · Sources: P243 https://en.wikipedia.org/wiki/Architectural_drawing · Verdict: KEEP (timing set to the house arrival).

### STR-30 Workings layer
- For: part-whole, proof-trust · 1 drawing, 3-12 notes
- Instead of: an appendix of assumptions nobody opens
- Reader sees: A clean drawing of the plan that, in its last chapter, gains its construction lines, measurements and margin notes, the way an architect shows the plan behind a rendering; a small "show the workings" switch lets them replay it.
- Moves: scroll-linked step, then tap - guides pen draw .6s each, 60ms apart (capped at 450ms); notes arrive (.6s); the switch hides them again at 1.5× speed.
- Build: two SVG layers (`.final`, `.workings`); a real `<button aria-pressed>` toggles `data-xray` on the figure once the step has played; CSS transitions dashoffset on `.workings path` and opacity on the labels. No drag lens (it fights scrolling on tablets).
- Narrow: <768px workings shown under the drawing by default · Reduced motion: workings shown, instant swap.
- Use when: the reader may want proof that the plan is measured (budgets, layouts, timelines). · Avoid when: more than ~12 notes.
- Effort: S · Needs lib: no · Sources: P410 https://heronaiapp.com, https://metic.studio/en · Verdict: ADAPT, changed: plays as a chapter first so nobody has to find the switch; stagger 40 to 60ms.

### STR-31 Venn sweet spot
- For: part-whole, comparison, opposed then joined · 2-3 sets
- Instead of: "we combine X and Y" in a sentence
- Reader sees: Two or three named circles; the overlap fills with the accent and is named as what the reader gets.
- Moves: in-view - circles pen draw in place (~1s each); the overlap fills with the accent .3s after the last circle closes (.6s); the overlap label reveals once.
- Build: SVG circles with `mix-blend-mode:multiply`, or an explicit intersection via clipPath for the accent fill; circle labels outside, overlap label inside.
- Narrow: <768px scaled down, labels below · Reduced motion: static.
- Use when: "you need both X and Y, and we're the only one with both". · Avoid when: more than 3 sets, or nesting carries the meaning (use STR-21).
- Effort: S · Needs lib: no · Sources: P326 https://github.com/Financial-Times/chart-doctor/tree/main/visual-vocabulary · Verdict: ADAPT, changed: circles draw in place instead of sliding 40px from the sides.

### STR-32 Proportional tiles
- For: part-whole, hierarchy · 4-15 weighted parts
- Instead of: a percentage list of where time or budget goes
- Reader sees: One block split into tiles whose areas are shares of time or budget; the biggest tile names the main work, and the tiles part slightly so the unequal sizes show.
- Moves: in-view - the block arrives whole, then tiles separate by `clip-path: inset()` in size order (.6s each, 80ms apart, capped at 450ms). Optional scroll-linked nudge: each tile moves out from the centre by at most 12px.
- Build: precompute a squarified layout once (or a hand-set CSS grid with spans close to the ratios); labels only in tiles big enough for one line, others numbered; the nudge is `translate(calc(var(--k) * dx), calc(var(--k) * dy))` with k from 0 to .15; label the largest and smallest once they part.
- Narrow: <768px stacked full-width bars in the same order · Reduced motion: static, parted.
- Use when: "where the effort goes", or the whole hides an imbalance. · Avoid when: shares are near-equal (tiles look random).
- Effort: M · Needs lib: no · Sources: P323 https://github.com/Financial-Times/chart-doctor/tree/main/visual-vocabulary, P058 https://pudding.cool/2025/08/onions/ · Verdict: ADAPT, changed: explode toggle folded in as a nudge capped at 12px; stagger capped.

### STR-33 Unit grid (1 in N, or one square per deliverable)
- For: part-whole, quantity-scale, list-of-equals · 6-100 units
- Instead of: a big bold percentage, or a deliverables checklist
- Reader sees: A 10 × 10 field of dots where a share lights up ("37 of every 100 enquiries"), or n squares where each square is one thing we hand over, filling as each is explained.
- Moves: in-view (share) - lit cells arrive in five bands of two rows, 90ms apart (450ms total), the label counting up in step. Scroll-linked (inventory) - one cell fills as each deliverable is named, with an `n / N` counter.
- Build: CSS grid `repeat(10, 1fr)`, cells `aspect-ratio:1; border-radius:3px`, `--i` per cell, lit when i < share. Inventory: n cells = n real deliverables in 5 or 6 columns, caption "each square is one thing we hand over"; add `.filled` to the first `Math.round(p * n)` cells. Reuse the same grid for later numbers so the reader learns it once. Plain dots, never faces.
- Narrow: <768px the 10 × 10 shrinks fine; inventory goes to 5 columns · Reduced motion: lit or filled, item names listed beside.
- Use when: proportions, coverage, adoption, or "all of this, accounted for". · Avoid when: precision matters (37.4% is a label), more than 5 categories, or deliverables differ a lot in weight (use STR-32).
- Effort: S · Needs lib: no · Sources: P198 https://www.raycast.com, P322 https://github.com/Financial-Times/chart-doctor/tree/main/visual-vocabulary, P085 https://pudding.cool/2025/02/middle-school/, P108 https://datavizproject.com/data-type/percentage-grid/ · Verdict: ADAPT, changed: four grids merged; faces replaced by dots; per-cell 8-15ms staggers replaced by five 90ms bands.

### STR-34 Nested squares
- For: part-whole, quantity-scale, comparison · 5-30 amounts of very different sizes
- Instead of: two big numbers side by side
- Reader sees: Squares sized by amount, smaller ones tucked into the corner of bigger ones, so "your ad spend" against "revenue lost to slow follow-up" lands at once.
- Moves: in-view - squares grow from their shared corner, largest first (.8s cubic-bezier(.22,1,.36,1), 90ms apart, capped at 450ms).
- Build: side = `Math.sqrt(value) * k` so the area is honest; every square anchored bottom-left (transform-origin bottom left); label inside when there is room, otherwise with a leader line.
- Narrow: <768px same, scaled · Reduced motion: static.
- Use when: comparing amounts of very different sizes. · Avoid when: values are close (bars read better).
- Effort: S · Needs lib: no · Sources: P092 https://informationisbeautiful.net/visualizations/the-billion-pound-o-gram/ · Verdict: KEEP

### STR-35 Audit strips
- For: part-whole, grouped-list, proof-trust · 3-12 strips of 10-60 blocks
- Instead of: an audit table of pass and fail
- Reader sees: Each item (a page of the client's site, a claim, a process) is a strip of small blocks shaded by status in three plain levels, with the overall share at the strip's end.
- Moves: in-view - each strip wipes left to right (`clip-path: inset()`, .6s ease-out), strips 90ms apart, capped at 450ms.
- Build: a flex row of small divs or SVG rects; three chalk tints with one-line definitions in the legend ("works", "works with help", "broken"); tap a block for its note.
- Narrow: <768px blocks wrap into two rows per strip · Reduced motion: static.
- Use when: auditing many units against one standard. · Avoid when: the levels are subjective and have no notes.
- Effort: S · Needs lib: no · Sources: P091 https://informationisbeautiful.net/visualizations/based-on-a-true-true-story/ · Verdict: ADAPT, changed: five levels cut to three; one wipe per strip instead of 10ms per block.

---

## Place-network

### STR-36 Route drawn by the schedule
- For: place-network, sequence · 3-8 stops
- Instead of: an itinerary table
- Reader sees: A pinned line-drawn map beside the schedule; as you scroll the schedule, the route draws on the map like a pen and each stop fills as the line reaches it.
- Moves: scroll-linked (pinned) - dashoffset tracks progress with a small accent dot riding the line's tip; stops fill when passed; the frame holds still (no camera chase).
- Build: SVG `viewBox="0 0 1500 1500"` with `preserveAspectRatio="xMidYMid slice"`; `len = path.getTotalLength()`, `strokeDasharray = len`, `strokeDashoffset = len * (1 - p)`; dot at `path.getPointAtLength(len * p)`; stops are circles that fill when passed. For a long route, step the frame once per stop instead of following the dot.
- Narrow: <768px static twin: the full route with numbered stops above the schedule · Reduced motion: full route drawn with numbered stops.
- Use when: anything with place and order (a supply route, a field visit, a delivery chain, an event day). · Avoid when: geography does not matter to the decision.
- Effort: M · Needs lib: no · Sources: P188 https://tympanus.net/codrops/2026/05/21/creating-scroll-driven-svg-map-animations-with-gsap/ · Verdict: ADAPT, changed: camera chase (scale 2.5 to 4 with 1s smoothing) and GSAP dropped; static twin on narrow.

### STR-37 Bridge between two places (new)
- For: place-network, many-to-many · 2 places, 3-6 things that cross
- Instead of: two logos joined by a plus sign
- Reader sees: Two line-drawn places (the campus and the plant) on either side of the stage with one road between them; each chapter sends one thing across (people, a curriculum, live problems, results) and names it on the side where it lands, so by the end both sides list what they gave and got.
- Moves: in-view - both places and the road pen draw once. scroll-linked (pinned) - each chapter sends one accent dot along the road in its direction (`offset-distance` 0 to 100%, 1.2s, cubic-bezier(.45,.05,.35,1)); on arrival its label arrives on that side (12px, .7s).
- Build: SVG viewBox 1000×420; places as self-drawing line illustrations (P020 draw-on idiom); road path with `pathLength="1"`; the dot uses `offset-path: path(...)` or `getPointAtLength` in requestAnimationFrame; each chapter carries `data-dir="ab"` or `"ba"`; labels are HTML lists under each place.
- Narrow: <768px static twin: places stacked top and bottom with a vertical road and two lists, "From A to B" and "From B to A" · Reduced motion: road drawn, both lists shown, no dot.
- Use when: a partnership of two parties where exchange in both directions is the point (a university and a company). · Avoid when: more than two parties (use STR-09).
- Effort: M · Needs lib: no · Sources: new; draw-on idiom (P020) and pulse along a line (P022) from the TVS harvest · Verdict: NEW

### STR-38 Lamp spotlight on one panorama
- For: place-network, part-whole, sequence · 1 panorama, 5-12 scenes
- Instead of: a series of separate section illustrations
- Reader sees: One wide line-drawn panorama of the client's world under a soft paper veil; as you scroll, a clear circle of light moves to each scene in turn and its narration appears; the client is drawn largest.
- Moves: scroll-linked (pinned) - the light's centre moves between scene centres with progress; the rest stays veiled; narration reveals once (12px, .7s). No flicker.
- Build: overlay `background: radial-gradient(circle at var(--x) var(--y), transparent 0 14vmin, rgb(var(--paper-rgb) / .6) 22vmin)`; JS interpolates `--x` and `--y` between scene centres from `--p`. Hierarchical scale: the hero figure is 2× everyone else. Past 8 scenes, split into two pinned sections.
- Narrow: <768px static twin: the panorama fully lit with numbered scene markers, narration as numbered cards below · Reduced motion: all lit, numbered markers.
- Use when: everything happens in one world and you want both the whole and its parts (also works for who-does-what inside one organisation). · Avoid when: the scenes are unrelated.
- Effort: L · Needs lib: no · Sources: P281 https://www.astaguru.com/blogs/phad-painting-%E2%80%93-the-grand-storytelling-art-of-rajasthan-966 · Verdict: ADAPT, changed: lamp flicker dropped (texture never animates); the dark rgba(20,10,0,.65) veil replaced by a paper veil; static twin.

### STR-39 Story-world map
- For: place-network, many-to-many · 5-15 places
- Instead of: a market landscape slide of logos
- Reader sees: A hand-drawn map of the client's world (markets, competitors, villages, risks drawn as reefs), a legend, a compass rose whose points are named for what matters (Trust, Growth), and a route drawn to where they want to be.
- Moves: in-view - the coastline pen draws; landmarks arrive 80ms apart (capped at 450ms); then the route pen draws once as a dotted line; the compass settles with no overshoot. Tap a place for its note.
- Build: SVG with the static rice-powder or ink filter; landmarks as `<symbol>` pictographs (mountain, tree, tower); the dotted route (`stroke-dasharray: 4 6`) is revealed by a solid mask path drawn with dashoffset, so the dots never march; places are buttons that open notes.
- Narrow: <768px the map scales to fit, places listed below as cards linked to pins · Reduced motion: static map.
- Use when: explaining a landscape (market, region, ecosystem) and where the client stands; the map can openly show a point of view. · Avoid when: real geography exists and would be misread.
- Effort: L · Needs lib: no · Sources: P275 https://en.wikipedia.org/wiki/Fantasy_map · Verdict: ADAPT, changed: the compass's 10deg overshoot and the marching dashes dropped; the route draws once.

### STR-40 Transit map of the workstreams
- For: place-network, many-to-many, people-roles, sequence · 2-4 lines, 6-20 stations
- Instead of: a Gantt chart or a dated plan
- Reader sees: A metro map where each coloured line is a team or workstream, stations are milestones spaced evenly (no dates), and interchange rings are the moments teams hand over to each other.
- Moves: scroll-linked (pinned) - one line per chapter: the line pen draws and its stations fill as the tip passes; an interchange ring takes the accent once both its lines have reached it. One moving thing at a time; no trains on every line at once.
- Build: SVG paths in 0, 45 and 90 degree segments on a 20px grid; stations evenly spaced regardless of duration (Beck's rule); interchange = paper circle with a 3px ink stroke; tip position via `path.getPointAtLength(p * len)`; one chalk tint per workstream, the accent kept for interchanges.
- Narrow: <768px static twin: a vertical trunk with branches, every line drawn · Reduced motion: full map, interchanges marked.
- Use when: several teams work in parallel with shared hand-off points. · Avoid when: the plan is one straight sequence (use the snake, SEQ-01), or readers would read stations as dates.
- Effort: L · Needs lib: no · Sources: P235 https://en.wikipedia.org/wiki/Harry_Beck · Verdict: ADAPT, changed: one line per chapter instead of trains running every line together.

### STR-41 Hex-tile region map
- For: place-network, list-of-equals · 6-40 regions
- Instead of: a list of districts by phase
- Reader sees: A simplified map where every district is the same hexagon placed roughly where it lies, filled by phase, so small districts count as much as big ones.
- Moves: in-view or scroll-linked - tiles fill one phase at a time (phase 1 first), each phase as one arrival (.6s).
- Build: axial coordinates (q, r) to x = size × √3 × (q + r/2), y = size × 1.5 × r; hand-place the tiles to resemble the real outline; 2-3 letter codes as labels; categorical chalk fills only (phase, served or not yet).
- Narrow: <768px codes only, with a key · Reduced motion: final state.
- Use when: geography matters but real area would mislead. · Avoid when: the reader needs real locations (use a proper map).
- Effort: M · Needs lib: no · Sources: P161 https://github.com/Financial-Times/chart-doctor/tree/main/visual-vocabulary · Verdict: KEEP

### STR-42 Context settles underneath
- For: place-network, atmosphere · 1 underlay behind any drawing (a modifier)
- Instead of: a separate map section that explains where
- Reader sees: A faint map or field quietly appears behind the main drawing so you know where this is happening.
- Moves: scroll-linked - underlay opacity 0 to 1 over ~16vh; no drift, no scale.
- Build: underlay `<g>` with `opacity: var(--p)`, drawn in one chalk tint at 15-25% strength so the subject keeps its contrast; optional rice-powder mask (feTurbulence noise as a `mask`) that never animates.
- Narrow: <768px same · Reduced motion: underlay present from the start.
- Use when: the place changes the meaning. · Avoid when: the setting is generic (it becomes wallpaper).
- Effort: S · Needs lib: no · Sources: P459 (video study key_04, burst_04; Washington Post scrollytelling reference) · Verdict: ADAPT, changed: the 8vh drift and 5% shrink dropped; fade only.

---
