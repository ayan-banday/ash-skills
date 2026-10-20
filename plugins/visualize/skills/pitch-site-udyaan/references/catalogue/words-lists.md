# Words and lists: big idea, definitions, equal items, groups

Pattern library family for `pitch-site-udyaan`. 36 entries (7 starred), curated from slice5 words-lists (55 raw entries, including the four "Lists that are not lists" entries assigned to this family).
Verdicts: 17 KEEP, 15 ADAPT, 4 NEW, 10 CUT (listed at the end). 3 raw entries moved to emphasis-type (P221 into EMP-06, P256 into EMP-28, P441 into EMP-29). Every entry lists all its source ids.

KEEP means the device stays as researched, with values snapped to the house tokens. ADAPT means its trigger, motion, material or interaction changed to meet the house rules; the verdict says what changed. NEW was invented to fill a gap.

**Shorthand used in every entry (house values):**
- **pen draw**: stroke-dashoffset from length to 0, duration = length / 600 px/s, clamped 0.6-2.2s, ease cubic-bezier(.45,.05,.35,1).
- **arrives**: opacity 0 to 1 with a 12px rise (16px max, blur 6px max), .8s cubic-bezier(.22,1,.36,1). Nothing enters from the side.
- **stagger**: 90ms (60-110ms), total capped at 450ms; items past the cap share the last start.
- **reveals once**: text arrives the first time it enters view, always finishes, never reverses.
- **scroll-linked**: linear, tied to progress; text never un-reveals.
- **steps**: a sticky stage plus caption blocks; one IntersectionObserver with rootMargin "-45% 0px -45% 0px" sets `data-step`. One change per step.
- **tokens**: paper #F1EDE4, card #FAF7F0, ink #241D18, muted #6B6158, line rgba(36,29,24,.14), chalk tints haldi #ECD9A6, neel #C6CFDA, laterite #DDB09A, dark bands wood #3A2B22 with powder #F4F1EA text. The one accent is marker yellow: `--marker` #F2C94C for bands and pills, `--marker-ink` #A87410 for thin strokes on paper. Kumkum #9E3B2A only for problem kickers. No green, no navy, no clay.
- **marker sweep**: EMP-01. **pen circle**: EMP-10.

---

## Family picker

Name the shape, count the items, name how they relate, then take the first ID whose "Avoid when" does not fire. Starred first. Rule zero: no bullet list longer than three items ships without a device from this page or a sibling family.

**One big idea**
- The opening, with a motif you will reuse later: WRD-01 ★, with EMP-29 for the headline.
- A cross-cutting idea framed as three concrete uses: WRD-07.
- A system too complex to start with: WRD-03, then the full drawing (STR-24, STR-26).
- Three to five sentences that must land in order: WRD-02, EMP-28.
- The whole proposal on one screen (who, how much, where, when, how, why): WRD-05, WRD-06.
- The recap before the ask, 3-5 promises: WRD-06, WRD-20.
- Every section, by default: WRD-04.
- "We sit where these three meet": STR-31 (structure-links).

**Definitions and jargon**
- 4-8 terms, each tied to a result, read one at a time: WRD-08 ★, WRD-12.
- A motif or diagram to decode, 3-6 parts linked to the whole: WRD-09 ★, WRD-10.
- 2-6 new names on one picture: WRD-10, WRD-09 ★.
- 6-15 terms the reader must compare side by side: WRD-12, WRD-11.
- Terms in passing across the page, 3-20: WRD-11, WRD-12.

**Equal items**
- Exactly 3, with names of one or two words: WRD-13 ★, WRD-14 ★, WRD-07.
- 3-4 client asks to echo before answering: WRD-15 ★, WRD-16.
- 3-6 problems or reasons that do not cause each other: WRD-16, WRD-15 ★.
- 4-7 parts that all live on one picture: SEQ-02 ★ (order-time), CHG-02 ★ (change-choice).
- 4-9 capabilities with one lead: WRD-17, WRD-18.
- 3-12 things the client will hold: WRD-19, WRD-14 ★.
- 8-15 facts, fees or deliverables: WRD-20, WRD-21.
- 16 or more: WRD-22, then WRD-31 if they fall into families.

**Ranked**
- 4-7 options in a recommended order: WRD-23, WRD-20.
- One lead, the rest in support: WRD-17, WRD-23.
- 4-15 initiatives by stage reached: WRD-24, WRD-20.
- 16 or more, by group size or along a worded scale: WRD-33, WRD-25.

**Linked**
- Asks linked to the teams that answer them, 3-4: WRD-15 ★, then STR-02 for many-to-many.
- Parts linked to one whole, 3-6: WRD-09 ★, WRD-10.
- Many requests handled in one place, 4-6: WRD-26, PPL-33.
- 4-9 ideas where the kind of idea matters: WRD-27; when the links matter more, STR-01.

**Grouped**
- 6-15 in 2-4 families: WRD-28, WRD-29.
- 3-6 regions in the client's own words: WRD-30, WRD-27.
- 5-20 areas that should feel like territory: WRD-29, WRD-31.
- 16-40 in families: WRD-31, WRD-29.
- 50 or more comments or items: WRD-32, WRD-33.
- Placed on two dimensions: CHG-42 (change-choice).

**Sequential**
- 3-5 argument beats: WRD-02, WRD-06.
- Terms played in turn: WRD-08 ★.
- One idea built up in beats: WRD-03.
- Steps, phases and chains: the order-time family (SEQ-01 ★ for chains, SEQ-08 for build-ups).

**Opposed**
- Wrong theories against the real cause, 4-7: WRD-35 ★, CHG-38.
- Ready against still missing, 4-9: WRD-34, SEQ-13.
- Where we stand between two poles, 3-7: WRD-36, CHG-41.
- Today against with us, row by row: CHG-21, CHG-13 (change-choice).

**Coverage check (every size and relation has at least two options here)**
- 3 items: WRD-13, 14, 07, 15, 16, 06, 02.
- 4-7: WRD-17, 23, 26, 35, 09, 08, 05, 27, 34, 36.
- 8-15: WRD-20, 12, 19, 21, 24, 28, 29, 11.
- 16+: WRD-22, 31, 32, 33, 25.
- Equal: 13, 14, 16, 17, 19, 20, 22. Ranked: 23, 24, 25, 33. Linked: 15, 09, 10, 26, 27. Grouped: 28 to 33. Sequential: 02, 08, 03. Opposed: 35, 34, 36.

**Family rules**
- Sequential reading only. No tabs, accordions, flip cards, pickers or tap-to-reveal; a tap may revisit, never gate.
- One moving thing and one highlight per screen; the accent lands on the one item being argued.
- Every device ends with the whole list readable at once; that finished state is also the reduced-motion state.
- Item names stay as plain text in the DOM, in reading order, for screen readers.

---

## One big idea

### WRD-01 ★ Self-drawing hero motif
- For: big-idea, atmosphere · 1 headline, 1 lede, 1 drawn motif (20-120 strokes)
- Instead of: a stock hero photo or a dark gradient banner
- Reader sees: a large serif headline on the left while, on the right, one line drawing (a kolam, a building, a machine) draws itself stroke by stroke and settles complete.
- Moves: load - every stroke pen draws (TVS: centre 1.4s, bands 2.2s each starting 1.0s, 1.5s, 2.0s, flowers 1.2s from 3.6s + k × 0.18s; done in about 5.7s; a generic drawing should finish in 2.5-3.5s), grouped outline first, detail next; the headline and lede arrive in parallel and never wait for the drawing.
- Build: hero band min-height 100svh, grid 2 × minmax(0,1fr), gap 40px, padding-block 96px 72px; h1 max 13ch, lede max 40ch; drawing box aspect-ratio 1/1, max-width min(620px,74svh). Per path: `L = getTotalLength()`, set dasharray and dashoffset to L, then add the transition with inline duration and delay; start after a double requestAnimationFrame. A sessionStorage flag can render it finished on a second visit. The motif must return later, as a key (WRD-09) or badges (EMP-37).
- Narrow: below 820px one column, drawing first (order:-1) at max min(420px,46svh); hide `.detail` paths below 700px · Reduced motion: drawing shown complete, no transition.
- Use when: the opening must set a cultural or emotional register and the motif returns as a decoder · Avoid when: the reader needs the answer in under 3 seconds, or there is no real object to draw.
- Effort: M (L with a generator) · Needs lib: no · Code: TVS harvest · Sources: P001 (TVS page.html L48-57, L465-476, L941-942; harvest 2.12), P405 (https://heronaiapp.com, https://foxvaluations.com.au) · Verdict: KEEP

### WRD-02 Argument that stacks
- For: big-idea, sequence · 3-5 sentences
- Instead of: an intro paragraph nobody reads
- Reader sees: one large sentence alone on a calm screen; each scroll step adds the next sentence under it while the earlier ones settle to muted ink, so the whole argument stands assembled at the end.
- Moves: steps - each new sentence arrives once as its step crosses mid-screen; earlier sentences fade to the muted colour over .4s; nothing fades out; the last sentence's key phrase gets the marker sweep.
- Build: one sticky stage (min-height 100svh) holding all sentences; 3-5 empty step blocks of 70-90vh scroll past; the observer sets `data-step`; JS adds `.on` to sentence n and `.past` to the ones before, and never removes them. Sentences serif clamp(28px,3.6vw,48px), max 22ch.
- Narrow: below 820px same, sentence size 7vw, steps 60vh · Reduced motion: all sentences shown as one stacked block, last phrase marked.
- Use when: the opening argument has 3-5 beats that must land in order · Avoid when: more than 5 sentences, or any beat needs a picture.
- Effort: S · Needs lib: no · Sources: P220 (https://heronaiapp.com/) · Verdict: ADAPT, changed: sentences no longer fade out and replace each other; they stack and dim, so the finished state holds the whole argument.

### WRD-03 Toy world first
- For: big-idea, definitions-jargon · 1 core idea in 3-5 drawn elements
- Instead of: opening with the full system diagram
- Reader sees: a tiny line-drawn scene (one person, one inbox, three customers) that builds one element per step, each in the chalk tint it keeps for the rest of the page.
- Moves: steps - the scene is pinned; each step pen draws one element while its caption arrives; one element changes per step.
- Build: SVG with five or fewer big elements; each gets the tint it keeps all page (haldi, neel, laterite); define each as a `<symbol>` and reuse it later with `<use>` so the toy world becomes the legend. Captions are plain sentences ("Three customers write in at night").
- Narrow: below 820px the scene sticks in the top 45% of the screen and captions scroll under it · Reduced motion: final scene with all labels.
- Use when: the real system is too complex to start with · Avoid when: the reader is already expert.
- Effort: S · Needs lib: no · Sources: P060 (https://ciechanow.ski/gps/) · Verdict: KEEP

### WRD-04 Finding as headline
- For: big-idea, proof-trust · 1 finding per section
- Instead of: topic headings like "Our approach"
- Reader sees: every section heading is the conclusion as a full sentence ("Most of your leads arrive after 6 pm"), then one figure, two or three short sentences, and a small source line.
- Moves: in-view - the heading arrives; the figure arrives 110ms later; nothing else moves.
- Build: a content rule as much as a layout: h2 is a sentence (max 18ch at clamp(34px,4.2vw,56px)); exactly one figure; a caption that points ("see the evening spike"); source in 13px muted. Pair with the split header (EMP-36) when the figure needs a how-to-read line.
- Narrow: below 820px same order, one column · Reduced motion: static.
- Use when: always, as the default section skeleton · Avoid when: the section is a story beat rather than a claim.
- Effort: S · Needs lib: no · Sources: P093 (https://ourworldindata.org/data-insights/how-many-people-in-the-world-identify-with-a-particular-religion) · Verdict: KEEP

### WRD-05 Six-picture napkin
- For: big-idea, many-to-many · exactly 6 (who, how much, where, when, how, why)
- Instead of: an executive summary in six paragraphs
- Reader sees: a paper napkin with six quick pen sketches (a portrait, a small chart, a map, a timeline, a flow, a "why" plot), each with a one-line caption: the whole proposal on one screen.
- Moves: in-view - cells pen draw in reading order, who to why, starting 90ms apart (capped at 450ms, so later cells overlap); each caption arrives after its sketch.
- Build: 3 × 2 CSS grid; each cell an SVG with the TVS wobble filter (`feTurbulence baseFrequency=".04"` + `feDisplacementMap scale="2"`, static); a faint static fold line from `repeating-linear-gradient`; each cell is an anchor to the section that expands it.
- Narrow: below 820px 2 × 3 grid · Reduced motion: static sketches.
- Use when: the opening summary or closing recap of a full proposal · Avoid when: you cannot answer all six honestly (an empty "why" shows).
- Effort: M · Needs lib: no · Sources: P237 (https://www.antoinebuteau.com/lessons-from-dan-roam/) · Verdict: KEEP

### WRD-06 Promises that come back
- For: big-idea, call-to-action · 3-5 promises
- Instead of: a "Summary" bullet list before the call to action
- Reader sees: just before the ask, the 3-5 promises made along the way return as short claim lines, each beside a small thumbnail of the drawing that proved it.
- Moves: in-view - lines arrive in order with the stagger; thumbnails are already drawn; the last line's key phrase gets the marker sweep.
- Build: thumbnails reuse earlier SVGs with `<use href="#fig-3">` at 72-96px; each line links to its section anchor; each line is a claim ("Your Friday invoices go out on Monday morning") worded exactly as it first appeared, so recognition does the work.
- Narrow: below 820px thumbnail above each line · Reduced motion: static, marker shown.
- Use when: the page is long and 3-5 promises must be remembered · Avoid when: you cannot get it to five or fewer.
- Effort: S · Needs lib: no · Sources: P080 (https://ncase.me/remember/), P084 (https://ncase.me/polygons/) · Verdict: ADAPT, changed: the tap-to-flip recall cards are gone (readers will not tap); the reprise keeps their idea and borrows the takeaway's thumbnails.

### WRD-07 Icon rows on a dark band
- For: big-idea, list-of-equals · 3 uses + 1 large motif
- Instead of: a "Why it matters" paragraph
- Reader sees: a dark wood section: on the left a heading with one italic phrase, a lede with its key terms on a soft yellow band, and three translucent rows, each with a cream icon, a title and one line; on the right the motif with only its centre lit.
- Moves: in-view - rows arrive with the stagger; the motif is static.
- Build: `.way` grid 1fr 1fr, gap 56px; `h2 strong` 500 italic; lede terms in powder 600 over `rgba(242,201,76,.35)` at `0 90% / 100% 40%` (the soft band is safe on wood because it is translucent); rows grid 44px | 1fr, gap 16px, padding 20px, radius 14px, background rgba(244,241,234,.06), ring rgba(244,241,234,.12); body #D9CDBF.
- Narrow: below 820px one column, motif under the rows · Reduced motion: static.
- Use when: a cross-cutting idea needs its own moment, framed as concrete uses · Avoid when: there are no concrete uses to list.
- Effort: S · Needs lib: no · Sources: P021 (TVS page.html L174-182, L774-789) · Verdict: KEEP

## Definitions and jargon

### WRD-08 ★ Jargon translator card
- For: definitions-jargon, sequence · 4-8 terms (6 proven)
- Instead of: a glossary table
- Reader sees: a card with three stacked slots: WE CALL IT (a technical term types itself), IT MEANS (a plain sentence fades in word by word), SO AT [CLIENT] (the concrete result, swept with the marker); thin segments along the bottom fill as each term plays.
- Moves: in-view (threshold .4; pauses when it leaves view) - per term 6800ms: jargon types at 34ms per character; 300ms pause; plain words every 100ms, each .3s ease-out from opacity 0, blur 4px, 12px rise; 700ms pause; the outcome fades .5s and rises 8px over .75s; marker sweeps 0 to 100% over .7s after .35s; hold at least 800ms; the active segment fills linearly; tap, Enter or Space jumps to a term at once. This is the one sanctioned timed sequence.
- Build: `.prompt` radius 18px, padding 28px, 1.5px ink ring, min-height 330px, flex column gap 8px, aria-live polite; jargon mono 20px #4A4038; plain serif clamp(24px,2.3vw,31px)/1.18; outcome serif clamp(20px,1.8vw,24px)/1.32 with its `mark` inside the paragraph. Segments have 15px hit areas drawing a 3px line. A generation counter and cancellable waits stop the loop cleanly; empty the cancel list after each term (the TVS build leaks about 150 closures per cycle). Layout grid .8fr 1.2fr, gap 48px, intro text on the left.
- Narrow: below 820px the intro stacks above the card · Reduced motion: term 1 shown complete; segment taps swap terms statically.
- Use when: technical terms must land with non-technical readers, each tied to a concrete result · Avoid when: readers need to compare terms side by side (WRD-12), or the copy is long.
- Effort: M · Needs lib: no · Code: TVS harvest · Sources: P019 (TVS page.html L143-162, L728-743, L988-1038; harvest 2.4) · Verdict: KEEP

### WRD-09 ★ Motif key: one part per step
- For: definitions-jargon, part-whole, linked · 3-6 parts
- Instead of: a legend box under a diagram
- Reader sees: the full motif pinned on one side; as each short row scrolls past ("THE CENTRE: your way of working", "STRAND ONE: need 1"), that part of the drawing stays bright and the rest fades back; the last step lights everything.
- Moves: steps - when a row crosses mid-screen, its part holds at opacity 1 and the others fade to .22 over .4s ease-out; the final step restores the whole; rows can still be tapped to revisit a part.
- Build: every motif part carries `data-part`; rows are `<button data-part="band0">` in a grid 120px | 1fr, gap 18px, padding 16px 18px, radius 12px; mono 11.5px label #C9B8A6, serif 22px meaning in powder; `.on` background rgba(244,241,234,.08). Section grid .9fr / 1.1fr, gap 56px; motif `position:sticky; top:15vh`, max 520px. The step observer calls `key.focus(part)` and toggles `.on`. Fix two TVS bugs: set the opacity transition once instead of appending it on every focus, and drop `role="listitem"` from the buttons.
- Narrow: below 820px one column, motif sticky in the top 40% at max 380px, label stacks above meaning · Reduced motion: full motif, all rows listed, taps still focus.
- Use when: one symbol or diagram carries meaning through the page and the reader needs a decoder once · Avoid when: parts do not map one to one to ideas, or more than 6 parts.
- Effort: S (given the motif) · Needs lib: no · Code: TVS harvest · Sources: P004 (TVS page.html L70-80, L522-538, L944-957; harvest 2.12), P051 (https://pudding.cool/2018/02/waveforms/) · Verdict: ADAPT, changed: the 2200ms auto-cycle is replaced by scroll steps over a pinned motif (the Washington Post pinned subject), so the reader sets the pace.

### WRD-10 Leader-line labels
- For: definitions-jargon, part-whole, linked · 2-6 labels on one picture
- Instead of: a numbered key under an image
- Reader sees: a line drawing, screenshot or evidence photo with thin pen lines running from each part to a short name, written in the same colour as the part it names.
- Moves: in-view - per label, in reading order (near to far, or most to least important): a 4px dot fades in (.3s), the leader pen draws, then the label arrives (opacity only, .3s); labels start 90ms apart; the one key word gets the marker sweep last.
- Build: `<figure>` with the image and an SVG overlay whose viewBox matches the image's pixel size; leaders are `<path pathLength="1">` drawn by dashoffset 1 to 0; labels are HTML placed in % (crisp and selectable), never more than two lines. Fire on view or on the step, never on scroll position, so the set always completes. For the same parts across several drawings use STR-28.
- Narrow: below 820px numbered dots stay on the picture and labels move below as a numbered key · Reduced motion: all labels and leaders shown.
- Use when: a new term or part first appears, or evidence needs pointing at (a client dashboard, a shop floor) · Avoid when: more than 6 parts (use WRD-09), or the picture is decorative.
- Effort: S · Needs lib: no · Sources: P048 (https://www.reuters.com/graphics/MYANMAR-ROHINGYA/010051VB46G/), P463 (video study, key_10_satellite-label-fades-in.png, burst_09_label-fade.png), P466 (video study, key_13_first-label-inner-belt.png, burst_13_label-stagger.png) · Verdict: ADAPT, changed: a line drawing or screenshot replaces the stock photo by default, dots fade instead of popping, and the 300ms label stagger is cut to 90ms.

### WRD-11 Term gloss in the margin
- For: definitions-jargon, utility · 3-20 terms per page
- Instead of: a glossary at the end, or tap-to-open tooltips
- Reader sees: a calm main column with a narrow margin; each unfamiliar term has a dotted underline, and its plain one-line meaning, with a tiny line icon, sits in the margin level with that line.
- Moves: in-view - each gloss fades in (opacity .6s cubic-bezier(.22,1,.36,1), no travel) as its line reaches mid-screen; nothing else moves.
- Build: the Tufte CSS pattern: `span.sidenote` floated right with a negative right margin into a gutter about 30% wide; the term is a `<dfn>` with `text-decoration: underline dotted var(--muted)` (the accent stays free for the argument); glosses in 14.5px sans, muted ink, at most one per three lines of body. Sourced proof notes share the rail (see PPL-24).
- Narrow: below 820px each gloss sits inline right after its paragraph as a haldi-tint strip in 14px, always visible, no toggle · Reduced motion: glosses visible, no fade.
- Use when: a mixed audience includes non-experts · Avoid when: the term is central (define it in the sentence, or use WRD-08), or notes would outweigh the main text.
- Effort: S · Needs lib: no · Sources: P069 (https://worrydream.com/ExplorableExplanations/), P254 (https://edwardtufte.github.io/tufte-css/) · Verdict: ADAPT, changed: the tap-to-open peek card and the narrow-screen toggle are gone; meanings are always on the page, because skimmers will not tap.

### WRD-12 Side-by-side glossary ledger (new)
- For: definitions-jargon, list-of-equals · 6-15 terms
- Instead of: a two-column glossary table with borders
- Reader sees: a ruled ledger with one term per row: the term in mono on the left, its plain meaning in serif in the middle, and what it changes for the client in a short phrase on the right; one row's outcome carries the marker.
- Moves: in-view - each row's rule draws left to right (scaleX 0 to 1, .8s cubic-bezier(.22,1,.36,1)); its words arrive 150ms later (opacity .6s); rows start 90ms apart; after the last row the marker sweeps the one outcome being argued.
- Build: `<dl>` where each row is a `div` grid `minmax(120px,.7fr) 1.4fr 1fr`, gap 24px, padding-block 14px; the rule is `::after` (1px var(--line), transform-origin left), the WRD-20 recipe. Term mono 11.5px caps .08em; meaning serif 19px/1.35; outcome sans 15px. Keep the `mark` inside the `dd` text, never as a direct grid child.
- Narrow: below 820px each row stacks term, meaning, outcome · Reduced motion: rules and text visible, marker shown.
- Use when: readers must compare terms, or there are too many for the translator card · Avoid when: fewer than 4 terms (use WRD-10 or define inline), or meanings run past two lines.
- Effort: S · Needs lib: no · Sources: new; built from P421 (https://foxvaluations.com.au) and the WE CALL IT / IT MEANS / SO AT slots of P019 · Verdict: NEW, fills the 6-15 term gap the one-at-a-time translator cannot serve.

## Equal items

### WRD-13 ★ Sentence list
- For: list-of-equals · exactly 3, short names
- Instead of: three bullets
- Reader sees: the three items woven into one sentence, each a small chip with a tiny line icon: "We find them, warm them, and close them", with only the outcome chip marked.
- Moves: in-view - chips arrive as one line (opacity, 8px rise, .8s cubic-bezier(.22,1,.36,1), 90ms stagger); .35s after the last chip lands, the marker sweeps under the outcome chip's text.
- Build: a normal `<p>`, never a flex or grid parent, so wrapping and the marker behave; chips are `<span class="chip">` inline-block, `white-space:nowrap`, radius 999px, padding 2px 10px 2px 6px, 1px ring, 18px icon from the sprite; the `mark` wraps the text inside the outcome chip. The sentence reads naturally to screen readers.
- Narrow: below 820px chips wrap with the sentence · Reduced motion: static, marker shown.
- Use when: exactly three equal items whose names are one or two words · Avoid when: items need explanation.
- Effort: S · Needs lib: no · Sources: P331 (https://baymard.com/blog/highlighting-text-online) · Verdict: KEEP

### WRD-14 ★ Three drawn figures
- For: list-of-equals, atmosphere · 3 (max 4)
- Instead of: three icon-and-text feature cards
- Reader sees: three cream panels, each with a simple line drawing (a helmet, a phone screen, a video frame) that draws itself, a chalk fill that blooms into one area, a small "FIG 01" caption, a name and one sentence.
- Moves: in-view (threshold .35) - each path pen draws (TVS: 1.4s, delay (i%6) × .12s + floor(i/6) × .1s); panels start 110ms apart; the fill fades 0 to .9 over .6s after .9s; captions follow 200ms after their drawing.
- Build: grid 3 columns, gap 16px; SVG viewBox 240×180, aspect 4/3, background #FFFDF6, radius 10px; `.draw` fill none, 2.2px ink, round caps and joins, `vector-effect:non-scaling-stroke`; save any original dasharray in `data-dash` and restore it after 2400ms. Figcaption starts with a mono figure number ("FIG 0.1").
- Narrow: below 820px one column, drawing left and text right · Reduced motion: drawn and filled.
- Use when: showing kinds of output, or three principles, where a photo would be too specific · Avoid when: the object cannot be drawn in about six strokes.
- Effort: S-M · Needs lib: no · Code: TVS harvest · Sources: P020 (TVS page.html L164-172, L757-770, L1040-1049; draw-on idiom in harvest 2.1), P178 (https://linear.app) · Verdict: KEEP

### WRD-15 ★ Echo cards with "answered by"
- For: list-of-equals, many-to-many · 3-4 client asks
- Instead of: "You asked for:" followed by bullets
- Reader sees: four equal cards, each with a hand-drawn icon, a small "NEED 1 · LEADERS" tag, a serif title, the client's own words in italic, and, pinned to the bottom under a hairline, "ANSWERED BY" with colour chips for the teams.
- Moves: in-view - cards arrive with the TVS delays 0, .1, .2, .3s; chips are static.
- Build: grid repeat(4,minmax(0,1fr)), gap 16px; card radius 16px, padding 26px 24px 22px, flex column gap 14px, 1px ring; h3 25px/1.15; the quote serif italic 18px/1.4 #3E342C; `.by` margin-top auto (pins the footer), padding-top 14px, border-top 1px var(--line), 13px muted, `.by b` mono 10.5px block label. Chips are the TVS team chips (PPL-03), never avatars; each team keeps its tint on its own section later.
- Narrow: below 980px 2 columns; below 560px 1 column · Reduced motion: static.
- Use when: echoing back a short set of client asks before answering each one · Avoid when: items differ in weight or need ranking.
- Effort: S · Needs lib: no · Sources: P009 (TVS page.html L59-68, L285, L488-517) · Verdict: KEEP

### WRD-16 Numbered cards on a construction line
- For: list-of-equals · 3-6 problems or reasons
- Instead of: a numbered list of problems
- Reader sees: problem cards labelled [01] to [04], joined by a faint dash-dot drafting line, each card's small line icon drawing itself as the card arrives.
- Moves: in-view - each card arrives (12-16px rise, .8s ease-out); its icon pen draws over 1.0s after .2s; the connector to the next card pen draws; cards start 90ms apart, total capped at 450ms.
- Build: CSS grid of cards; the connector is an absolutely placed SVG path with `stroke-dasharray: .93 2.8 9.35 2.8` at about 22% ink for the base, and a solid ink copy drawn over it by dashoffset on reveal. Labels mono 11-12px in kumkum ("[01] MANUAL"); icons 1.5px line drawings with `class="draw"`.
- Narrow: below 820px one column, the connector runs down the left gutter · Reduced motion: everything visible, connectors solid.
- Use when: listing 3-6 problems or reasons before the solution · Avoid when: the items cause one another (use the snake, SEQ-01).
- Effort: S · Needs lib: no · Sources: P408 (https://heronaiapp.com) · Verdict: KEEP

### WRD-17 Bento with one lead cell
- For: list-of-equals, hierarchy, proof-trust · 4-9 capabilities
- Instead of: a 3 × 3 grid of identical icon cards
- Reader sees: lunchbox compartments of different sizes: the big cell carries the lead capability, smaller cells the supports, and each cell shows one small line-drawn instrument (a gauge, a mini chart, a ticked list) with an honest reading and a one-line gain.
- Moves: in-view - cells arrive in reading order, lead first, with the stagger; each instrument plays only after its cell lands: strokes pen draw, a number counts up over .8s once, bars grow scaleX once.
- Build: CSS grid repeat(6,1fr) with `grid-template-areas`; the lead spans 2 × 2 (or 4 columns); each cell is one claim, one SVG instrument and one caption naming the reader's gain; counters in requestAnimationFrame with `font-variant-numeric: tabular-nums`. Instruments are ink lines on card colour with one chalk tint; no icons, no gradients.
- Narrow: below 820px 2 columns, 1 below 560px, lead first; instruments keep their aspect ratio · Reduced motion: final values, static.
- Use when: parallel capabilities with one headline, each with a measurable effect · Avoid when: you would have to invent numbers, the items are a sequence, or every cell is only text (a list in boxes).
- Effort: M · Needs lib: no · Sources: P176 (https://www.framer.com), P324 (https://www.saasframe.io/blog/the-bento-layout-trend) · Verdict: ADAPT, changed: Framer's product-UI tiles are redrawn as ink-line instruments on paper and merged with the lead-cell bento.

### WRD-18 Boxes that draw their own border
- For: list-of-equals, grouped-list · 2-8 boxes or chips
- Instead of: static bordered cards or tag pills
- Reader sees: each card or pill traces its outline in ink, then the ink softens to a light rule and the contents appear.
- Moves: in-view - the four sides grow over .9s with the pen ease; at 75% the colour eases from ink to the line tone; contents arrive as the trace ends; chips wipe left to right over .7s; 70ms stagger, capped at 450ms.
- Build: `background: linear-gradient(var(--draw),var(--draw)) top left / 0 1px no-repeat, ...` for the four sides, animated to `100% 1px` and `1px 100%`; chips use `clip-path: inset(0 100% 0 0 round 999px)` to `inset(0 round 999px)`. Swap to the TVS box-shadow ring once drawn.
- Narrow: below 820px same · Reduced motion: drawn.
- Use when: options, packages, team chips · Avoid when: boxes are large panels (the trace reads slow).
- Effort: S · Needs lib: no · Sources: P429 (https://metic.studio/en) · Verdict: KEEP

### WRD-19 Deliverables drawn as objects
- For: list-of-equals, part-whole · 3-12 outputs
- Instead of: a "What you get" bullet list
- Reader sees: the things the client will hold (a report, a training kit, a dashboard, a weekly price sheet) drawn as simple line objects with a label pill and one line on what is inside; 3-5 sit along one shelf line, 6-12 form a mosaic around the headline.
- Moves: in-view - the shelf line pen draws first; objects pen draw with the stagger (later objects share the last start); labels arrive after their drawing; no hover, no tilt, no ambient brightening.
- Build: shelf: flex row over a 1.5px ink line; mosaic: CSS grid with mixed spans and `grid-auto-flow: dense`, the headline on a clear centre block. Each object is a `<figure>` with an SVG of 6-12 strokes and a mono label pill. claude.com's product page opens with this kind of labelled task mosaic. For past work shown as proof, use PPL-22.
- Narrow: below 820px the shelf becomes a 2-column grid; the mosaic becomes a 2-row strip above the headline · Reduced motion: all objects drawn, labels shown.
- Use when: the service produces concrete artefacts the reader can picture · Avoid when: the offer is abstract (strategy, advice), or there is nothing to hold.
- Effort: M · Needs lib: no · Sources: P187 (https://claude.com/product/overview), P217 (https://press.stripe.com) · Verdict: ADAPT, changed: the 3D book shelf with hover tilt and the mosaic's ambient brightening became flat self-drawing objects with labels always visible.

### WRD-20 Ledger rules that draw in
- For: list-of-equals, ranked-list, proof-trust · 3-12 rows
- Instead of: a bullet list of facts, fees or deliverables
- Reader sees: rows of a neat ledger where each ruled line draws itself left to right and then its words appear, row by row, like someone filling in a report.
- Moves: in-view - rule scaleX 0 to 1 over .8s cubic-bezier(.22,1,.36,1), delay min(i × 90ms, 450ms); text fades in over .7s, 150ms after its rule; a long section rule takes 1.4-1.6s with the pen ease.
- Build: `.row{position:relative}` `.row::after{content:"";position:absolute;left:0;right:0;bottom:-1px;height:1px;background:var(--line);transform:scaleX(0);transform-origin:left}` plus an `.in` state; `--row-delay` set inline; IntersectionObserver rootMargin "0px 0px 12% 0px". For a ranked list, put the rank in mono on the left and the marker on row one only.
- Narrow: below 820px same · Reduced motion: rules and text visible.
- Use when: key facts, fee lines, what-you-get lists, short ranked lists · Avoid when: rows are long paragraphs.
- Effort: S · Needs lib: no · Sources: P421 (https://foxvaluations.com.au, https://jithinrp.com) · Verdict: KEEP

### WRD-21 Petal glyphs
- For: list-of-equals, comparison · 3-12 items by 4-8 yes/no features
- Instead of: a tick table
- Reader sees: a row of small line flowers, one per item (each programme or crop), where each petal slot stands for one feature and a petal is there only if the item has it; a labelled legend flower comes first.
- Moves: in-view - the legend flower pen draws first; then each flower's petals pen draw as ink outlines and take their chalk fill (.5s); flowers start 90ms apart, capped at 450ms.
- Build: petal path `M0,0 C6,-8 6,-22 0,-28 C-6,-22 -6,-8 0,0` rotated by 360/k per slot; each slot keeps one chalk tint across all flowers; a missing petal shows as a faint dotted outline so absence reads. Use petal length only for real scores.
- Narrow: below 820px 3 flowers per row · Reduced motion: static, filled.
- Use when: comparing several items on the same yes/no features, warmer than a tick table · Avoid when: more than 8 features.
- Effort: S · Needs lib: no · Sources: P152 (https://truth-and-beauty.net/projects/oecd-better-life-index) · Verdict: ADAPT, changed: petals pen draw as outlines and then fill in chalk instead of unfurling, and missing petals show as dotted ghosts.

### WRD-22 The number and the five that matter (new)
- For: list-of-equals · 16 or more equal items
- Instead of: a 20-line bullet list of every module, school or service
- Reader sees: one giant count ("24 workshops") with a short caption, five drawn examples picked for this reader, and the full list set small in a quiet ruled ledger underneath for anyone who wants it.
- Moves: in-view - the count arrives; the five examples pen draw with the stagger; the full list is static; the marker lands on the example closest to this client's need.
- Build: a grid with the numeral column (clamp(6rem,18vw,14rem), line-height .8, tabular lining figures; the EMP-14 recipe) and five figures in a row; the full list as a multi-column `<ul>` (`columns: 3 18ch`, 13.5px, muted) under a 1px rule. Choose the five by the reader's needs, never alphabetically.
- Narrow: below 820px numeral above, examples 2 per row, full list in 2 columns · Reduced motion: static, marker shown.
- Use when: the inventory is long and equal, and the reader only needs to know it is big and see what applies to them · Avoid when: the items fall into clear families (use WRD-31).
- Effort: S · Needs lib: no · Sources: new; combines P371 (giant numeral) and P421 (ledger) · Verdict: NEW, fills the 16+ equal-items gap.

## Ranked

### WRD-23 Pen-ranked shortlist (new)
- For: ranked-list · 4-7 options
- Instead of: a numbered list "1. 2. 3."
- Reader sees: a short list of options in serif; a pen writes a rank number beside each one in turn, best first, then loops a circle around the top choice.
- Moves: in-view - rank numerals in the hand face write in by a left-to-right clip-path wipe (.4s each, pen ease), 110ms apart from rank 1 down; .35s after the last numeral, the pen circle (EMP-10) draws around option 1 in the accent.
- Build: an `<ol>` with `list-style:none`, items in the order you rank them; each `li` has a `span.rank` (Caveat 500, 28px, ink) in a 48px left gutter, revealed with `clip-path: inset(0 100% 0 0)` to `inset(0)`; the circle is the TVS ring path `M150 6C70 4 8 14 8 36s70 30 146 28 142-8 140-30S220 4 128 10` with `vector-effect:non-scaling-stroke`. Rank numbers are real text, so screen readers hear the order.
- Narrow: below 820px gutter 36px · Reduced motion: numerals and circle shown.
- Use when: recommending an order among a few options, so it reads as a considered judgement · Avoid when: the ranks are numeric scores (amounts-ranks family), or you only need the one pick (PPL-29).
- Effort: S · Needs lib: no · Sources: new; built on P028 (TVS ring, harvest 2.14) and P444 (https://www.fps.hu) · Verdict: NEW, fills the ranked 4-7 gap.

### WRD-24 Stem garden
- For: list-of-equals, time-roadmap, ranked by stage · 4-15 initiatives
- Instead of: a status table with traffic lights
- Reader sees: a row of ink-drawn plant stems rising from a soil line, one per initiative; height shows the stage reached (seed, growing, harvest) and each leaf is a team involved.
- Moves: in-view - stems pen draw up from the soil line with the stagger; leaves fade and scale from .8 to 1 over .5s after their stem; stems that reached the top stage get a marker-yellow bud last.
- Build: each stem is a leaning cubic path, height snapped to 3 stage lines labelled on the left in mono; leaves are ellipses rotated ±40° along the stem, outlined in ink with a haldi or laterite fill; soft shapes, a legend, no axes, no percentages.
- Narrow: below 820px two rows · Reduced motion: final garden.
- Use when: the status of several initiatives in a growth or farming story · Avoid when: the metaphor clashes with the brand, or the stages are not real.
- Effort: M · Needs lib: no · Sources: P156 (https://www.designboom.com/design/data-federica-fragapane-soft-forms-hard-facts-inequalities-shapes-triennale-milano-interview-06-08-2025/) · Verdict: ADAPT, changed: green foliage became ink stems with chalk-tint leaves, and buds no longer open with motion.

### WRD-25 Example swarm on a worded scale
- For: grouped-list, ranked, proof-trust · 10-60 real examples
- Instead of: a logo wall or a long case list
- Reader sees: dots for real examples spread along a worded scale from "simple" to "complex", piling up where most sit; the client's own case is a marker-yellow dot with a label.
- Moves: in-view - dots arrive in place (opacity, 6px rise, .6s cubic-bezier(.22,1,.36,1)), bin by bin from left to right, 90ms between bins (capped at 450ms); the client's dot lands last with a pen circle.
- Build: x = worded bin centre plus a little jitter; y by simple collision (try 0, ±d, ±2d until clear; O(n²) is fine up to 60); dots 8px ink at 60%; every key example already carries a label, and a tap may show more. No numbers: bins are words, every dot is a real case.
- Narrow: below 820px vertical swarm, scale running top to bottom · Reduced motion: final swarm.
- Use when: showing range, and where most cases sit, for credibility · Avoid when: fewer than about 10 examples.
- Effort: M · Needs lib: no · Sources: P166 (https://www.rawgraphs.io/learning/how-to-make-a-beeswarm-plot) · Verdict: ADAPT, changed: dots no longer fall from above; they fade in place by bin, and the reader's own case takes the one accent.

## Linked

### WRD-26 Many asks into one door
- For: linked (many to one), list-of-equals · 4-6 requests
- Instead of: a list of everything the service handles
- Reader sees: four to six everyday requests ("order", "pay", "complain", "reorder") down the left; one by one, a pen line runs from each into a single drawn door on the right, which then takes its name ("one WhatsApp number").
- Moves: in-view, once - each connector pen draws (about .6-.9s), starting 110ms apart, capped at 450ms; when the last one arrives, a marker-yellow dot lands on the door and its label arrives (.6s). Nothing loops.
- Build: requests as HTML rows; one SVG overlay whose connectors are cubic paths from each row's right edge (measured with getBoundingClientRect) to the door's left edge; rebuild on resize and after `document.fonts.ready`. The door is a simple 6-stroke drawing. For a closing that ties every idea to one person, see PPL-33.
- Narrow: below 820px requests above, door below, connectors run downward · Reduced motion: all lines drawn, dot and label shown.
- Use when: many small tasks are handled through one place · Avoid when: each task needs its own explanation.
- Effort: S · Needs lib: no · Sources: P184 (https://mercury.com) · Verdict: ADAPT, changed: Mercury's infinite 10s highlight loop became connectors that pen draw once into the one door.

### WRD-27 Sketchnote containers with meaning
- For: grouped-list, many-to-many, cause-effect · 4-9 ideas
- Instead of: a bullet list of discovery notes
- Reader sees: ideas drawn in hand-drawn containers whose shape means something (a box is a fact, a cloud is a belief, a banner is a commitment), joined by arrows and dotted lines, with a small three-shape legend.
- Moves: in-view - the legend draws first; containers pen draw with the stagger; text arrives inside each (opacity .5s); connectors pen draw last, with arrowheads.
- Build: JS generates rough rectangles and clouds as paths with ±2px jitter, drawn twice slightly offset for a marker look; arrows via `marker-end`; one chalk tint per container type; only the commitment banner may carry the accent.
- Narrow: below 820px a linear stack with down arrows between · Reduced motion: static.
- Use when: playing back a workshop or discovery call in the client's terms · Avoid when: the links matter more than the kinds of idea (use STR-01).
- Effort: M · Needs lib: no · Sources: P287 (https://en.wikipedia.org/wiki/Sketchnoting) · Verdict: KEEP

## Grouped

### WRD-28 Pictogram family with group tints
- For: grouped-list, utility, definitions-jargon · 6-15 items in 2-4 groups
- Instead of: a categorised bullet list
- Reader sees: one family of hand-drawn line pictograms, one per capability, each on a small chalk-tint disc that names its group; the same small icons return as section badges, so the page becomes signposted.
- Moves: in-view - pictograms pen draw group by group (90ms between groups, capped at 450ms); their twins in the section headers are drawn finished.
- Build: draw every icon on a 24-unit grid, one stroke weight (1.75px), round caps; define each once as a `<symbol>` stroked `currentColor` in ink; group colour lives only in the disc behind (`--zone-a`, `--zone-b` from haldi, neel, laterite); apply the static TVS wobble filter for a hand line.
- Narrow: below 820px 3 per row, the group label above each group · Reduced motion: static icons.
- Use when: the page has repeated categories that must be recognised at a glance · Avoid when: fewer than 4 categories (icons become decoration).
- Effort: M · Needs lib: no · Sources: P234 (https://en.wikipedia.org/wiki/Otl_Aicher) · Verdict: ADAPT, changed: Aicher's strict geometric strokes in group colours became the house hand-drawn ink line, with group colour moved to a chalk disc.

### WRD-29 Organic cells map
- For: grouped-list, part-whole, atmosphere · 5-20 cells in 2-5 families
- Instead of: a services list split under subheadings
- Reader sees: a pebble-like mosaic where each irregular cell is one area of work; cells of the same family cluster together, share a chalk tint and carry their names inside.
- Moves: in-view - family outlines pen draw (heavier stroke), then the cell borders inside, family by family 110ms apart; names arrive after their family; no drift.
- Build: Voronoi in about 40 lines: for each seed, start with the bounding-box polygon and clip it by the perpendicular bisector with every other seed (Sutherland-Hodgman); O(n²) is fine for 20 cells. Hand-place seeds so families sit together and spacing stays even; caption "areas are equal".
- Narrow: below 820px keep the shape; long names move to a numbered key · Reduced motion: static, all drawn.
- Use when: a domain of many related areas should feel like territory · Avoid when: exact order matters.
- Effort: M · Needs lib: no · Sources: P136 (https://datavizproject.com/data-type/convex-treemap/) · Verdict: ADAPT, changed: the ambient seed drift and the tap-out cards are gone; borders pen draw and names sit in the cells.

### WRD-30 Their words in a drawn template
- For: grouped-list, utility · 3-6 regions
- Instead of: "What we heard" bullet points
- Reader sees: a large pre-drawn template (a road, a mountain, a river with banks) whose empty regions fill with the client's own words, as if recorded live at the meeting.
- Moves: in-view - the template pen draws first; then each region's words write in left to right (clip-path, .9s, pen ease), regions 110ms apart; every region always finishes.
- Build: an SVG template with HTML text regions placed over it in %; reveal by `clip-path: inset(0 100% 0 0)` to `inset(0)`; quotes in serif italic with a mono attribution; reuse the same regions in later sections so the categories stay fixed.
- Narrow: below 820px regions become stacked labelled cards under a small template thumbnail · Reduced motion: text shown.
- Use when: proving you listened, using their words in a shared structure · Avoid when: you do not have their words.
- Effort: M · Needs lib: no · Sources: P288 (https://www.imagethink.net/graphic-facilitation-templates/) · Verdict: ADAPT, changed: the scroll-scrubbed write-in became a timed write that always finishes, and the marker-cap cursor was dropped.

### WRD-31 Labelled tile grid
- For: grouped-list · 16-40 items in families
- Instead of: a long service catalogue
- Reader sees: square tiles like a periodic table, each with a two-letter code, a name and a one-line impact; the family is the chalk tint, and gaps between families show the structure.
- Moves: in-view - families arrive one at a time, 90ms apart (capped at 450ms), each family's tiles together (opacity, 8px rise, .7s cubic-bezier(.22,1,.36,1)); then the one tile being argued gets an ink box (EMP-11).
- Build: CSS grid with an explicit `grid-area` per tile; codes serif 28px, names 13px sans, impact 12px muted; a family legend in mono above.
- Narrow: below 820px 4 columns, one family per row group · Reduced motion: static.
- Use when: a big inventory must feel organised (services, modules) · Avoid when: the reader needs every item explained.
- Effort: M · Needs lib: no · Sources: P337 (https://datavizcatalogue.com/search.html) · Verdict: KEEP

### WRD-32 Voice clusters
- For: grouped-list, many-to-many, proof-trust · 50-500 comments in 4-8 groups
- Instead of: a page of testimonial quotes
- Reader sees: hundreds of tiny dots, each one real comment, gather from a loose grid into labelled clouds ("price", "trust", "speed"), and one real quote rises out of each cloud.
- Moves: scroll-linked - dots move from grid positions to cluster positions linearly with section progress; at the end each cloud's label and quote arrive once.
- Build: positions computed offline (no runtime clustering); each dot gets a random point in a disc around its cluster centre; clouds take chalk tints; labels name the most common concern; quotes are real and attributed. These are data points, so size follows count.
- Narrow: below 820px sample down to about 120 dots, clouds stacked vertically · Reduced motion: final clusters with labels and quotes.
- Use when: you have qualitative research to show · Avoid when: fewer than about 30 comments.
- Effort: M · Needs lib: no · Sources: P098 (https://pudding.cool/2018/11/dearabby/) · Verdict: KEEP

### WRD-33 Unit columns by topic
- For: grouped-list, part-whole, ranked · 20-300 items in 3-8 groups
- Instead of: a bar chart of topic counts
- Reader sees: each item is a small square stacked into a column by topic, so the tallest column is the biggest concern and every square is still one real item; one example per column is labelled.
- Moves: in-view - columns fill bottom up, 90ms apart (capped at 450ms), each column's squares fading in together over .6s; the example labels arrive last.
- Build: a CSS grid per column with `grid-auto-flow: row`, 10 squares per row; topic label under each column; squares in ink at 70%, the argued column in the accent; a tap on a square may show that item.
- Narrow: below 820px columns become rows · Reduced motion: static.
- Use when: counts and individuality both matter · Avoid when: more than 8 groups.
- Effort: S · Needs lib: no · Sources: P099 (https://pudding.cool/2018/11/dearabby/) · Verdict: KEEP

## Opposed

### WRD-34 Mise en place tray
- For: grouped-list, opposed (ready against missing), utility · 4-9 items
- Instead of: a kickoff checklist
- Reader sees: a top-down board with small bowls, each holding one prepared item (logo files, photos, logins, price list); bowls still empty are dashed and labelled "we need this from you".
- Moves: in-view - bowls pen draw with the stagger; filled bowls take their chalk fill (.5s); empty ones stay dashed, and one marker-yellow dot lands on the most urgent missing bowl.
- Build: SVG circles as bowls with chalk fills; missing bowls get a dashed stroke; labels in the hand face; the board is flat card colour with no animated texture. For a full "what you bring, what we do" split, see SEQ-13.
- Narrow: below 820px 2 rows · Reduced motion: static, dashed outlines, dot shown.
- Use when: a readiness checklist before kickoff · Avoid when: more than 9 items.
- Effort: S · Needs lib: no · Sources: P249 (https://en.wikipedia.org/wiki/Mise_en_place) · Verdict: ADAPT, changed: the looping wobble on missing bowls became one marker dot on the most urgent gap.

### WRD-35 ★ Suspect lineup
- For: list-of-equals, cause-effect, opposed (wrong theories against the real cause) · 4-7 candidates
- Instead of: "Why other approaches fail" bullets
- Reader sees: one pinned reference line (what actually happened, or the client's goal); each scroll step asks "Is it X?" and lays one candidate over it; the candidate visibly misses and greys; the real cause draws last in the accent and fits. A wall of small identical panels closes the section.
- Moves: steps - each candidate pen draws (about .6-1.0s) when its question crosses mid-screen, then drops to 20% opacity when the next arrives; the winner pen draws last at full weight in the accent, then a pen circle lands on its label. The closing wall arrives with an 80ms stagger.
- Build: a sticky SVG with one thick reference path and one `<path class="suspect" id="s1..sN">` per candidate, all pre-rendered hidden; steps set `data-step=N`; CSS `[data-step="3"] #s3{opacity:1;stroke-dashoffset:0}` and `.suspect.ruled-out{opacity:.2}`. Headings are questions ("Is it the logo?"); the last heading is the answer ("It is follow-up speed."); each suspect gets a one-word verdict tag in kumkum mono. Close with CHG-22 small multiples on shared scales, reusing the paths with `<use href="#s3">`.
- Narrow: below 820px each suspect becomes its own small panel with the reference line repeated · Reduced motion: final state, all suspects grey, the winner in the accent.
- Use when: the client holds wrong theories you must clear before your answer can land · Avoid when: you cannot honestly show the alternatives failing; for options failing plain tests, use CHG-38.
- Effort: M · Needs lib: no · Sources: P041 (https://www.bloomberg.com/graphics/2015-whats-warming-the-world/), P042 (same source) · Verdict: KEEP (P042's verdict wall folded in as the closing step)

### WRD-36 Pole lines with a settled dot (new)
- For: opposed (tensions between two poles) · 3-7 pairs
- Instead of: "We balance speed and quality" sentences
- Reader sees: three to seven short lines, each with a plain word at both ends (fast and careful, cheap and lasting); a dot sits where this proposal stands on each line, with a one-line reason underneath.
- Moves: in-view - each line pen draws from the left; as the pen passes the dot's position, the dot lands there (opacity and scale .6 to 1, .3s ease-out); lines start 90ms apart, capped at 450ms; on the one line being argued, the dot is marker yellow and gets a pen circle.
- Build: rows grid `10ch 1fr 10ch`, gap 16px; the line a 1.5px ink SVG path; dot 12px ink placed by `--pos` percent and timed by `--pos × draw duration`; pole words serif 18px, the nearer pole in ink and the farther in muted.
- Narrow: below 820px pole words sit above each end of the line · Reduced motion: lines drawn, dots in place.
- Use when: positioning the proposal on trade-offs the client already feels · Avoid when: the poles are not real opposites, or every dot sits in the middle (nothing to argue); for a today-to-with-us move, use CHG-11.
- Effort: S · Needs lib: no · Sources: new; a worded relative of P166 (one worded scale) and P335 (dot strip) · Verdict: NEW, the opposed relation had only two kept entries here.

---
