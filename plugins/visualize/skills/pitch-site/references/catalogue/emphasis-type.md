# Emphasis and type: the impact phrase, numbers, headlines, type as image

Pattern library family for `pitch-site`. 37 entries (7 starred), curated from slice5 emphasis-type (70 raw entries) plus 3 moved in from words-lists (P221, P256, P441).
Verdicts: 23 KEEP, 12 ADAPT, 2 NEW, 21 CUT (listed at the end). Every entry lists all its source ids.

KEEP means the device stays as researched, with values snapped to the house tokens. ADAPT means its trigger, motion, material or interaction changed to meet the house rules; the verdict says what changed. NEW was invented to fill a gap.

**Shorthand used in every entry (house values):**
- **pen draw**: stroke-dashoffset from length to 0, duration = length / 600 px/s, clamped 0.6-2.2s, ease cubic-bezier(.45,.05,.35,1).
- **arrives**: opacity 0 to 1 with a 12px rise (16px max, blur 6px max), .8s cubic-bezier(.22,1,.36,1). Nothing enters from the side; no back, elastic or bounce easing.
- **lands**: the moment its text has finished arriving. Highlights start .3-.35s after the text lands.
- **stagger**: 90ms (60-110ms), total capped at 450ms.
- **accent**: marker yellow, the only colour that points. `--marker` #F2C94C for bands and pills; `--marker-ink` #A87410 for thin strokes on paper, where a 2-3px yellow line vanishes on cream. Ink #241D18, muted #6B6158, paper #F1EDE4, wood #3A2B22, powder #F4F1EA, kumkum #9E3B2A (problem labels only, never pointing).

---

## Family picker

**How many per screen (the budget)**
1. One highlight per screen. If two marked things share a viewport, neither is the point.
2. One accent, arriving through motion (a sweep, a pen circle, a dot) on exactly the thing being argued.
3. One dialect per meaning, fixed for the whole page: marker band = the reader's gain; pen circle = the pick or the proof number; strike = what goes away; handwritten note = the human aside. Never two on one phrase. Choose EMP-01 or EMP-03 as the page's marker, never both.
4. Mark about a tenth of the page at most. Test: read only the marked phrases, in order; they should tell the story on their own.
5. A highlight fires .3-.35s after its text lands, runs once, and never loops.
6. Once per page at most: EMP-06, EMP-23, EMP-24, EMP-29, EMP-31. At most three EMP-28 screens per page, and one type-as-image device per section.
7. Bold is for scanning only. Anything that matters gets colour.

**Tone and context, to the best two or three devices**
- The reader's gain in body copy, any tone: EMP-01 ★; EMP-02 ★ when the phrase wraps to 2-3 lines.
- Sober page (finance, legal, procurement): EMP-01 ★, EMP-11, EMP-05.
- Warm, hand-made, founder voice: EMP-24 ★, EMP-03, EMP-25.
- On a wood or ink band: EMP-07 ★, EMP-08, EMP-09.
- One number proves the claim: EMP-10 ★, EMP-13, EMP-14.
- The pick among a few options: EMP-10 ★, EMP-12.
- Something changes or goes away: EMP-16 ★, EMP-17; whole lines rewritten: CHG-12.
- One part of a pinned diagram matters at each step: EMP-18 ★, EMP-19.
- A chart or screenshot needs one sentence of meaning: EMP-22, EMP-20, EMP-21.
- Their own people said it best: EMP-26, then PPL-16.
- A chapter thesis, or a finding that must survive a five-second glance: EMP-28, EMP-30, EMP-31.
- The opening headline: EMP-29, beside WRD-01 ★.
- The one paragraph not to skip: EMP-05, EMP-06.
- A counter-intuitive answer the reader should guess first: EMP-33.
- The key price or figure that should feel measured: EMP-23, EMP-11.
- A short label such as "Included": EMP-32; an official mark: PPL-25.
- Pacing toward a climax: EMP-34.
- Wayfinding on every section: EMP-35, EMP-36, EMP-37, with EMP-27 under card grids.

**Known bugs (apply everywhere)**
- A `mark` that is a direct child of a grid or flex parent is blockified, so its band covers only the last line. Keep every `mark` inside a `<span>` or `<p>`, or draw the band from measured rects (EMP-02).
- On dark cards the 40%-high band hides light text. Use the full-height pill (EMP-07, EMP-08) or yellow words (EMP-09).

---

## Marking a phrase

### EMP-01 ★ Marker sweep
- For: emphasis, the reader's gain · 1 phrase per screen, up to about 12 words
- Instead of: bold text
- Reader sees: a translucent yellow highlighter band slides in under the one phrase that says what the reader gains, as if someone just marked it.
- Moves: in-view - background-size 0% to 100% at 40% band height over .8s cubic-bezier(.22,1,.36,1) (TVS ships .7s cubic-bezier(.19,1,.22,1); both are in range), starting .35s after the paragraph's reveal so the eye arrives before the ink; once.
- Build: `mark{background:linear-gradient(var(--marker),var(--marker)) no-repeat 0 100% / 0 40%;color:inherit;padding:0 2px;-webkit-box-decoration-break:clone;box-decoration-break:clone;transition:background-size .8s cubic-bezier(.22,1,.36,1) .35s}` and `.in mark{background-size:100% 40%}`. Animate a gradient image, never background-color, so the size can tween; `clone` gives each wrapped line its own band. Keep the `mark` inside inline text (see Known bugs). On wood, a soft rgba(242,201,76,.35) band at `0 90% / 100% 40%` works; on ink cards use EMP-07.
- Narrow: below 768px rewrite the phrase to two lines or fewer · Reduced motion: band at 100% from first paint.
- Use when: one sentence per section carries the reader's gain · Avoid when: another highlight is on screen, or the phrase runs past about 12 words (it becomes a coloured paragraph).
- Effort: S · Needs lib: no · Code: TVS harvest · Sources: P033 (TVS page.html L40, L155-156, L177, L284, L322; harvest 2.9), P289 (https://blog.master.dev/highlight-text-when-a-user-scrolls-down-to-that-piece-of-text/) · Verdict: KEEP

### EMP-02 ★ Line-by-line marker
- For: emphasis, sequence · 1 phrase that wraps to 2-3 lines
- Instead of: a sweep that inks every wrapped line at the same moment
- Reader sees: a slightly uneven highlighter stroke dragged along line one, then line two, in reading order, following the phrase across its line breaks like a real marker.
- Moves: in-view - per rendered line, an SVG stroke pen draws (duration = line width / 600 px/s, clamped .4-1.0s); each line starts as the previous one ends; once.
- Build: `range.getClientRects()` on the phrase, merged by row; per row a path `M x0 y C x0+.3w y1, x0+.7w y2, x1 y3` with a seeded wobble of ±6% of the line height; one SVG overlay behind the text, stroke var(--marker), width 45% of the line height on the lower half, round caps, `mix-blend-mode:multiply` on paper. Recompute on resize (debounced 150ms) and after `document.fonts.ready`. Because it draws from measured rects, the blockified-mark bug cannot happen.
- Narrow: below 768px rects recompute, same behaviour · Reduced motion: all strokes shown.
- Use when: the impact claim is a full sentence that wraps · Avoid when: the phrase fits on one line (use EMP-01), or runs past 12 words.
- Effort: S-M · Needs lib: no · Sources: P292 (https://splitting.js.org/guide.html), P451 (https://twain.ai, assets/routes-DJXdf6qw.js) · Verdict: ADAPT, changed: the fixed .45s per line became pen speed per line width, and twain's 72%-high stroke dropped to a lower-half band so the words stay readable.

### EMP-03 Chisel-tip marker
- For: emphasis · 1 phrase
- Instead of: a flat rectangular band
- Reader sees: a highlighter band with slanted ends, like a chisel-tip marker, on every wrapped line.
- Moves: in-view - the EMP-01 sweep (.8s cubic-bezier(.22,1,.36,1), .35s after the text lands), the slanted caps arriving with the band.
- Build: three gradient layers on `mark`: the left and right caps are diagonal gradients with a hard 50% stop, the middle a solid fill sized `calc(100% - 2*var(--skew) + 1px)` (the 1px overlap kills hairline gaps); `no-repeat`; `box-decoration-break:clone` with the `-webkit-` prefix. To animate, register `@property --p {syntax:'<percentage>';inherits:false;initial-value:0%}` and drive all three layers from `--p`.
- Narrow: below 768px same · Reduced motion: static band.
- Use when: the page is hand-made, warm and editorial and the marker should look held · Avoid when: the page is cool or corporate (the slant reads playful).
- Effort: M · Needs lib: no · Sources: P291 (https://pepelsbey.dev/articles/skewed-highlight/) · Verdict: KEEP

### EMP-04 Pen underline
- For: emphasis · 1-4 words on one line, in a headline or lede
- Instead of: a plain underline or italics
- Reader sees: a loose pen stroke with a slight wave draws itself under a short claim ("in four days").
- Moves: in-view - one stroke pen draws (about .6-.9s), .35s after the headline lands; once.
- Build: `<span class="u">phrase<svg viewBox="0 0 200 12" preserveAspectRatio="none" aria-hidden="true"><path pathLength="1" d="M2 8 C 50 2, 120 12, 198 5"/></svg></span>`; svg absolute, `bottom:-.25em; width:100%; height:.5em`; stroke var(--marker-ink) 2.5px, round caps, `vector-effect:non-scaling-stroke`; `white-space:nowrap` on the span.
- Narrow: below 768px, if the phrase would wrap, fall back to EMP-01 · Reduced motion: drawn.
- Use when: a deadline, a guarantee, a short claim in a heading · Avoid when: links nearby are underlined (readers take it for a link), or the phrase wraps.
- Effort: S · Needs lib: no · Sources: P295 (https://css-tricks.com/svg-line-animation-works/), P296 (https://github.com/rough-stuff/rough-notation) · Verdict: ADAPT, changed: the Rough Notation double underline became one accent pen stroke in plain SVG, kept to headings so it never reads as a link.

### EMP-05 Margin bracket
- For: emphasis, hierarchy · 1 paragraph per section
- Instead of: a boxed "key point" callout
- Reader sees: a hand-drawn bracket in the left margin beside one paragraph, saying "if you read one paragraph, read this".
- Moves: in-view - the bracket pen draws top to bottom (about .8-1.2s for a six-line paragraph); once.
- Build: an SVG in viewBox 0 0 20 100 with the path `M16 2 C6 2 8 8 8 20 L8 80 C8 92 6 98 16 98`, `preserveAspectRatio="none"`, `vector-effect:non-scaling-stroke`, absolutely placed at `left:-28px` and stretched to the paragraph's height; stroke var(--marker-ink) 2.5px, round caps.
- Narrow: below 820px swap to a 3px accent rule on the left that grows scaleY 0 to 1 from the top over .6s cubic-bezier(.22,1,.36,1) · Reduced motion: static bracket or rule.
- Use when: a section has one paragraph that holds the deal · Avoid when: several neighbouring paragraphs compete (pick one).
- Effort: S · Needs lib: no · Sources: P297 (https://github.com/rough-stuff/rough-notation) · Verdict: ADAPT, changed: drawn as one plain SVG pen stroke instead of a Rough Notation bracket, so no library is needed.

### EMP-06 Scroll-lit statement
- For: emphasis, big-idea · 1 statement of 15-40 words per page
- Instead of: a bold manifesto paragraph
- Reader sees: a large statement that starts in soft grey and turns to ink word by word as they scroll, with the two or three impact words landing last in the accent.
- Moves: scroll-linked - word i moves from unread to ink over a rolling window of 3 words, linear with progress (block top at 80% to block bottom at 40% of the viewport); it latches, so words never un-light on scroll up; if the reader stops with words still unlit, after 1.2s the rest finish at 60ms per word.
- Build: split into word spans (keep `aria-label` on the parent); value `clamp((p*(n+3) - i)/3, 0, 1)`, stored as max(previous, new); colour by `color-mix(in oklab, var(--ink) calc(v*100%), var(--unread))` with `--unread` at 45% ink so dim words stay readable; update only words whose value changed, quantised to .02. Impact words mix toward var(--marker-ink) instead of ink. A native option: per-word `animation-timeline: view()` inside `@supports`.
- Narrow: below 768px same, font 7-8vw · Reduced motion: fully lit, not pinned, impact words in the accent.
- Use when: the "why this matters" paragraph, once per page · Avoid when: the statement carries detail the reader must parse, or another scroll-paced device shares the screen.
- Effort: S · Needs lib: no · Sources: P221 (https://tympanus.net/codrops/2024/04/17/some-on-scroll-text-highlight-animations/), P302 (https://cruip.com/create-a-gradient-text-reveal-on-scroll-with-tailwind-css-and-js/), P450 (https://twain.ai) · Verdict: ADAPT, changed: it latches and always finishes, unread words start at 45% ink instead of pale grey, and only the impact words take the accent.

## On dark bands

### EMP-07 ★ Dark payoff card with a marker pill
- For: emphasis, cause-effect · 1 sentence closing a sequence
- Instead of: a "Result:" line in bold
- Reader sees: a centred ink-dark card at the end of a sequence: a tiny mono label ("WHERE THIS LEADS", "WHAT YOU GET") and one serif sentence with its key phrase on a solid yellow pill.
- Moves: in-view - the card arrives (12px rise, .75s); the pill is static, or sweeps as in EMP-08.
- Build: ink background, powder text, radius 18px, padding 24px 30px, centred, max 540px (end of a snake) or 780px (a band); label #C9B8A6 mono 11px .08em caps; sentence serif 23px/1.3. On dark, `mark` is a full-height pill: `color:var(--ink);background:var(--marker);padding:1px 6px;border-radius:4px`, because a 40% band would hide the powder text. Keep the `mark` inside the `p`.
- Narrow: below 820px, when it ends the snake, it left-aligns onto the rail (margin-left 46px) · Reduced motion: static.
- Use when: closing a sequence with the one result to remember · Avoid when: there are several outcomes (use a ledger, WRD-20).
- Effort: S · Needs lib: no · Code: TVS harvest · Sources: P015 (TVS page.html L308-310, L372-374, L653, L874; harvest 2.2, 2.9) · Verdict: KEEP

### EMP-08 Pill sweep on dark (new)
- For: emphasis on dark bands · 1-6 words on one line
- Instead of: a static pill, or a 40% band that hides light text
- Reader sees: on a dark card, a solid yellow pill wipes across the key phrase from the left, and the letters turn from powder to ink exactly where the pill passes.
- Moves: in-view - the top copy's `clip-path: inset(0 100% 0 0 round 4px)` opens to `inset(0 0 0 0 round 4px)` over .7s with the pen ease, .35s after the sentence lands; once.
- Build: a wrapper `display:inline-grid` holding two copies of the phrase in the same grid cell: the base copy in powder, the top copy (`aria-hidden="true"`) in ink on var(--marker) with `padding:1px 6px; border-radius:4px` and the clip; `white-space:nowrap`, because clip-path across line breaks fails. The inline-grid wrapper sits correctly in running text.
- Narrow: below 768px keep the phrase to four words or fewer · Reduced motion: pill shown with ink text.
- Use when: the payoff sentence sits on wood or ink and should feel marked live · Avoid when: the phrase may wrap (use EMP-07's static pill or EMP-09).
- Effort: S · Needs lib: no · Sources: new; built from P303 (https://emilkowal.ski/ui/the-magic-of-clip-path) and the TVS dark pill in P015 · Verdict: NEW, the dark-band context had only one kept device.

### EMP-09 Marker-yellow words on dark (new)
- For: emphasis on dark bands · 1 phrase of 2-8 words, may wrap
- Instead of: bold powder text on wood
- Reader sees: on a dark wood band, the key phrase turns from powder to marker yellow, and a thin yellow line draws under it.
- Moves: in-view - colour powder to var(--marker) over .6s cubic-bezier(.22,1,.36,1), .35s after the text lands; then a 1.5px underline grows left to right under each rendered line at pen speed; once.
- Build: `.lit{color:var(--powder);transition:color .6s cubic-bezier(.22,1,.36,1) .35s}` and `.in .lit{color:var(--marker)}`; the underline is `background: linear-gradient(var(--marker),var(--marker)) no-repeat 0 100% / 0 1.5px` growing to `100% 1.5px`, with `box-decoration-break:clone` so it follows wrapped lines. #F2C94C on #3A2B22 is about 8.5:1, fine at body sizes.
- Narrow: below 768px same · Reduced motion: yellow text and underline shown.
- Use when: a phrase on a dark band must be marked and may wrap · Avoid when: on paper (yellow text fails contrast on light grounds), or a second highlight shares the band.
- Effort: S · Needs lib: no · Sources: new; grown from the TVS soft marker on wood in P033 · Verdict: NEW, the dark-band context had only one kept device.

## Proof: the pick and the number

### EMP-10 ★ Pen circle
- For: emphasis, choice-fork, quantity-scale · 1 word, number or option per screen
- Instead of: bolding the chosen option or the key number
- Reader sees: a loose yellow pen loop circles the one word, number or option that matters, its ends overlapping like a real pen.
- Moves: in-view (threshold .5) - the loop pen draws over about 1.1s, .3-.5s after its text lands, or .3s after a count-up ends; once.
- Build: an absolute SVG overflowing the target by 16px left and right and 13px top and bottom, viewBox 300×70, `preserveAspectRatio="none"`; path `M150 6C70 4 8 14 8 36s70 30 146 28 142-8 140-30S220 4 128 10` (an open loop that overshoots its start); stroke var(--marker) on dark or var(--marker-ink) on paper, 3px, round caps, `vector-effect:non-scaling-stroke`; the target gets `position:relative; white-space:nowrap`.
- Narrow: below 768px same, stroke 2px · Reduced motion: loop shown drawn.
- Use when: showing the pick among options, or the one number that proves the claim · Avoid when: the target wraps, or another highlight shares the screen.
- Effort: S · Needs lib: no · Code: TVS harvest · Sources: P028 (TVS page.html L379-383, L889-894, L1150-1155; harvest 2.14), P294 (https://roughnotation.com/), P444 (https://www.fps.hu, line-anim.json) · Verdict: KEEP

### EMP-11 Ink box
- For: emphasis, definitions-jargon · 1 term, price or deadline
- Instead of: a bold price
- Reader sees: a slightly rough rectangle drawn around a figure or term, like an accountant boxing the total.
- Moves: in-view - the box pen draws as one stroke (about .8s), .35s after the figure lands; once.
- Build: an SVG `<rect pathLength="1" rx="3">`, or a hand-authored four-corner path with ±1.5px jitter and overlapping ends, absolutely placed at `inset: -.2em -.35em`; stroke var(--marker-ink) 2px, `vector-effect:non-scaling-stroke`; the target `white-space:nowrap`.
- Narrow: below 768px same · Reduced motion: static box.
- Use when: the price, the deadline, or the one deliverable · Avoid when: the boxed text is long (boxes around sentences look like errors).
- Effort: S · Needs lib: no · Sources: P298 (https://roughnotation.com/) · Verdict: KEEP

### EMP-12 Recommended card traced once
- For: emphasis, choice-fork · 1 of 2-4 options
- Instead of: a "Recommended" ribbon or a glowing animated border
- Reader sees: among the option cards, one has its edge traced by a pen line that runs once around it and then stays as a quiet accent border.
- Moves: in-view - after the cards land, the trace pen draws once around the card from its top-left corner (the perimeter at pen speed, capped at 2.2s); then it stays still.
- Build: an SVG `<rect pathLength="1" rx="16">` over the card (`inset:-1px`, `overflow:visible`), stroke var(--marker-ink) 1.5px, dashoffset 1 to 0; the card's own ring stays underneath; an "OUR PICK" label in mono 11px above the card title.
- Narrow: below 820px cards stack with the traced card first · Reduced motion: static accent border.
- Use when: recommending one of a few options · Avoid when: more than one card would be traced, or there is no real recommendation.
- Effort: S · Needs lib: no · Sources: P211 (https://ramp.com, https://vercel.com, https://linear.app) · Verdict: ADAPT, changed: the infinite conic spin and the orbiting dot became one pen trace that stops.

### EMP-13 Count from their number
- For: quantity-scale, proof-trust, before-after · 1 number per screen
- Instead of: a static stat in bold
- Reader sees: the impact number counts from the reader's current value to the new one while the unit stays still ("12 to 40 leads a week").
- Moves: in-view - the number tweens over 1.0s cubic-bezier(.22,1,.36,1), .3s after its line lands, from the honest baseline (their number today), never from 0 when the claim is a change; once. Odometer variant: digit strips roll with the same timing.
- Build: `@property --n {syntax:'<integer>';inherits:false;initial-value:0}`, `.num{counter-reset:n var(--n);transition:--n 1s cubic-bezier(.22,1,.36,1) .3s}`, `.num::after{content:counter(n)}`, `.in .num{--n:40}`; for decimals or separators use requestAnimationFrame with `Intl.NumberFormat`; `font-variant-numeric: tabular-nums` so digits do not jitter; the real value in `aria-label`, animated digits `aria-hidden`. Odometer: each digit is an `overflow:hidden; height:1em` window over a 0-9 column moved by `translateY(calc(var(--d) * -1em))`. Pair with a source line (PPL-18).
- Narrow: below 768px same · Reduced motion: final number.
- Use when: the number is the reader's gain · Avoid when: tiny values (counting 0 to 3 looks silly), several counters on one screen, or more than 6 digits.
- Effort: S (M for the odometer) · Needs lib: no · Sources: P304 (https://css-tricks.com/animating-number-counters/), P305 (https://number-flow.barvian.me/) · Verdict: KEEP

### EMP-14 Giant numeral as the image
- For: quantity-scale, big-idea · 1 number per section
- Instead of: a stat card with an icon
- Reader sees: one huge number fills half the screen ("14 days") with a small caption beside it; the number is the picture.
- Moves: in-view - the numeral arrives (.9s); it may count from the baseline (EMP-13) or fill with ink (EMP-31); the caption follows 110ms later.
- Build: `font-size: clamp(8rem, 30vw, 22rem); line-height:.8; font-variant-numeric: tabular-nums lining-nums;` serif at weight 300-400; caption in mono small caps on the numeral's baseline; the numeral in ink, the unit in muted.
- Narrow: below 820px 38vw, caption below · Reduced motion: static number.
- Use when: one number is the whole argument of a section · Avoid when: the number needs a unit explanation longer than 6 words.
- Effort: S · Needs lib: no · Sources: P371 (https://developer.mozilla.org/en-US/docs/Web/CSS/font-variant-numeric) · Verdict: KEEP

### EMP-15 Size ladder
- For: quantity-scale, before-after · 3-5 rungs
- Instead of: "grows 3x" in a sentence
- Reader sees: the same word set at growing sizes ("reach reach reach REACH"), so the growth is felt before it is read; the last rung is in the accent.
- Moves: in-view - rungs arrive left to right (8px rise, .7s) with the stagger; sizes are already set and nothing scales.
- Build: font sizes proportional to the real values (size = base × value / first value); the last rung coloured var(--marker-ink); each rung carries its number in mono underneath.
- Narrow: below 768px cap the largest rung at 18vw · Reduced motion: static.
- Use when: a growth claim backed by real numbers · Avoid when: the steps are not proportional to real values (type size implies magnitude).
- Effort: S · Needs lib: no · Sources: P382 (https://github.com/Financial-Times/chart-doctor/tree/main/visual-vocabulary) · Verdict: KEEP

## What changes or goes away

### EMP-16 ★ Strike and replace
- For: before-after, emphasis · 1 old phrase and 1 new phrase
- Instead of: "from 3 weeks to 4 days" in plain text
- Reader sees: the old way is crossed out by a pen line and fades back, and the new way writes in beside it: 3 weeks struck, 4 days in ink.
- Moves: in-view - the strike line grows scaleX 0 to 1 from the left over .45s with the pen ease; the old text fades to .4 opacity (.3s, from .35s); the new phrase arrives at .55s (8px rise, .6s); an optional marker sweep on the new phrase at 1.2s.
- Build: `<del>3 weeks</del> <ins>4 days</ins>`; `del{text-decoration:none;position:relative}` and `del::after{content:'';position:absolute;left:-2px;right:-2px;top:55%;height:2px;background:currentColor;rotate:-2deg;transform:scaleX(0);transform-origin:left}`; `ins{text-decoration:none}`. Screen readers announce the deletion and insertion. For whole lines rewritten, use CHG-12.
- Narrow: below 768px stack the new phrase under the old one if both do not fit on one line · Reduced motion: final state, struck and new both visible.
- Use when: the impact is a change in a number or habit the reader recognises as theirs · Avoid when: the old value is not the reader's own.
- Effort: S · Needs lib: no · Sources: P299 (https://roughnotation.com/) · Verdict: KEEP

### EMP-17 Cross off what goes away
- For: before-after, choice-fork · 1-3 chores, or a cloud of 8-20 words with 1 survivor
- Instead of: "We take care of X, Y and Z"
- Reader sees: the chores, tools or jargon the reader will no longer deal with get crossed off by pen, one after another, until one word is left standing and takes the marker.
- Moves: in-view - each strike or X pen draws (about .3-.5s); strikes start 90ms apart; a cloud goes in waves of 4-5 (each wave capped at 450ms, three waves at most); the survivor's marker sweep starts .35s after the last strike.
- Build: words in an inline flow (a `<p>`, never flex); each struck word wraps an SVG line or X drawn by dashoffset, ink 1.5px at ±2deg; the survivor is a `mark` (EMP-01). Rough Notation `crossed-off` with `annotationGroup` is a drop-in if a library is acceptable.
- Narrow: below 768px trim the cloud to 8 words · Reduced motion: all struck except the survivor, marker shown.
- Use when: "we take all this off your plate" · Avoid when: a crossed item is the reader's current vendor or their own team by name (it reads as an attack).
- Effort: S · Needs lib: no (Rough Notation optional) · Sources: P300 (https://github.com/rough-stuff/rough-notation), P383 (https://roughnotation.com/) · Verdict: KEEP

## Diagrams, charts and pictures

### EMP-18 ★ Only the working part in colour
- For: emphasis, cause-effect, people-roles · 3-10 parts or people
- Instead of: a fully coloured process diagram
- Reader sees: one pinned line-drawn diagram where everything is grey except the part doing the work at this step; as captions scroll past, the colour hands off through the system like a baton.
- Moves: scroll-linked steps - when a caption crosses mid-screen, the active part moves to the accent over .3s ease-out and the previous one returns to grey; one part changes per step.
- Build: all parts `fill:var(--muted)` at low opacity with ink strokes; each step lists ids in `data-active="brief,design"`; JS toggles `.active` (a chalk-tint fill with a var(--marker-ink) stroke); each caption names who is on point. The figure is `position:sticky`, the Washington Post pinned subject; one IntersectionObserver with rootMargin "-45% 0px -45% 0px".
- Narrow: below 820px the figure sticks in the top 42% and captions scroll under it · Reduced motion: a row of small frames, one per stage, each with its active part coloured.
- Use when: explaining hand-offs and ownership, who does what and when · Avoid when: many parts work at once.
- Effort: S · Needs lib: no · Sources: P053 (https://ciechanow.ski/mechanical-watch/) · Verdict: KEEP

### EMP-19 One-time alarm ring
- For: emphasis, cause-effect · 1 problem point per screen (3 at most per diagram)
- Instead of: a red warning icon or a pulsing dot
- Reader sees: a single ring ripples out once from the spot where things break, then a calm accent dot stays there to say "here".
- Moves: in-view - the ring scales 1 to 1.18 (in SVG, radius r to 1.8r) while opacity goes .9 to 0 over .7s cubic-bezier(.22,1,.36,1), exactly once; the dot stays in the accent.
- Build: an SVG `<circle class="ring">` duplicated at the node; on reveal add `.ping` with `animation: ping .7s cubic-bezier(.22,1,.36,1) 1 forwards`; never infinite; a tap on the node may ring it once more.
- Narrow: below 820px same · Reduced motion: no ring; the dot only.
- Use when: pointing at the one broken link, risk or bottleneck · Avoid when: everything is "a problem" (pick one).
- Effort: S · Needs lib: no · Sources: P413 (https://townhouse.dev) · Verdict: KEEP

### EMP-20 Grey context, one line in ink
- For: emphasis, quantity-scale · 1 key series and 2-8 context series
- Instead of: a multi-coloured line chart
- Reader sees: a chart where gridlines, labels and the other series sit in pale grey, and only the line that matters is in strong ink with an accent dot and label at its end.
- Moves: in-view - the key series pen draws; the context series are already grey and still; the end label arrives as the line finishes.
- Build: `--ctx:#cfc8bc`; context strokes 1px var(--ctx), the key series 2.5px var(--ink) with an 8px var(--marker-ink) end dot; gridlines at 15% opacity, never black; direct labels at line ends instead of a legend.
- Narrow: below 820px drop the gridlines and keep the key label at the line end · Reduced motion: final state.
- Use when: a busy chart has one story · Avoid when: every series matters equally.
- Effort: S · Needs lib: no · Sources: P230 (https://www.antoinebuteau.com/lessons-from-edward-tufte.md) · Verdict: ADAPT, changed: the "all equal, then fade" sequence, the show-all toggle and tap-to-zoom are gone; context starts grey and only the key line moves.

### EMP-21 Barcode with a few lit
- For: emphasis, time-roadmap · 20-200 ticks with 3-6 highlights
- Instead of: the full task list for the year
- Reader sees: a thin strip of many short grey ticks (every task in the year) where a handful stand taller, inked and labelled: the moments that need the reader.
- Moves: in-view - the grey strip is already drawn; the highlight ticks grow upward (scaleY 0 to 1, .6s cubic-bezier(.22,1,.36,1)) in time order with the stagger; their labels arrive with them.
- Build: one SVG about 60px high; tick x = index / total × width, or a real date position; grey ticks 1px × 24px in var(--ctx); highlights 2px × 52px in var(--marker-ink); labels are HTML with short leaders, alternating above and below. Caption "order of work, not to scale" when positions follow order.
- Narrow: below 820px rotate to a vertical strip on the left with labels on the right · Reduced motion: final state.
- Use when: lots happens, but only a few moments need the reader · Avoid when: the reader must know what every tick is.
- Effort: S · Needs lib: no · Sources: P110 (https://github.com/Financial-Times/chart-doctor/tree/main/visual-vocabulary) · Verdict: KEEP

### EMP-22 Pen arrow callout
- For: emphasis, proof-trust, cause-effect · 1-3 callouts on one visual
- Instead of: a legend, or a caption under a screenshot
- Reader sees: a small two-line note (a title, then what it means for them) with a loose hand-drawn arrow curving to the exact spot on a chart, screenshot or drawing.
- Moves: in-view - a small ring marks the target (scale .6 to 1, .3s); the note arrives (8px rise, .6s); the arrow shaft pen draws (about .6-.9s) and its head, a separate path, fades in at 85% of the draw; callouts start 110ms apart in reading order.
- Build: generate the arrow `d` once with Rough.js (roughness about 1.2, bowing about 2) and paste it in, or hand-author it; place it in a `position:relative` wrapper; a `ResizeObserver` recomputes the endpoints; note text wraps at about 120px.
- Narrow: below 820px notes collapse to numbered dots on the visual with numbered captions below · Reduced motion: drawn.
- Use when: a screenshot or chart needs one sentence of meaning · Avoid when: more than 3 callouts (it becomes a legend), or two arrows would cross.
- Effort: M · Needs lib: no · Sources: P308 (https://roughjs.com/), P309 (https://d3-annotation.susielu.com/) · Verdict: KEEP

### EMP-23 Assemble with construction guides
- For: emphasis, proof-trust · 1 block per page (a key figure, price or deliverable)
- Instead of: a plain fade-in of the key figure
- Reader sees: before the block appears, thin pencil guide lines cross where it will sit with a small measurement note; then the guides fade and the block settles exactly into that spot.
- Moves: in-view - the horizontal guide grows to full width by 38% of 1.7s, then fades; the vertical guide starts 90ms later; the note shows from 22% to 70%; the block arrives at .52-.64s (14px rise, blur 4px to 0, .9s cubic-bezier(.22,1,.36,1)).
- Build: `.cx-h` and `.cx-v` are absolutely placed 1px lines in ink at 25%; `@keyframes cx-h{0%{scale:0 1}38%{scale:1}to{opacity:0}}`; `.is-built` added by an IntersectionObserver; `--d` per block; the note in mono 10.5px.
- Narrow: below 820px same, shorter guides · Reduced motion: no guides; the block visible.
- Use when: the "this was measured" moment for a key figure · Avoid when: used on more than one block per page.
- Effort: S · Needs lib: no · Sources: P428 (https://metic.studio/en, _next/static/chunks/11yn5wfwhtw_z.css) · Verdict: KEEP

## Human voice

### EMP-24 ★ Pen-written word
- For: emphasis, people-roles, atmosphere · 1 word, name or signature
- Instead of: the client's name in bold, or a typed sign-off
- Reader sees: one word (the client's name, their town, a signature under the promise) writes itself in pen, long strokes taking longer than short ones, then the ink settles.
- Moves: in-view (threshold .4) or load - stroke i lasts its length at 600 px/s, so most words take 1.2-1.9s in total; each stroke starts at 82% of the previous one; pen ease; an optional fill fades in over .5s at the end. Anything waiting on it waits 1.9s at most.
- Build: SVG strokes (hand-lettered, or from a single-line font) with `pathLength="1"`; compute lengths, build start times cumulatively (`t += d * .82`), set per-path `transition-delay` and `transition-duration` inline; one IntersectionObserver triggers it; the last stroke's `transitionend` adds a class that releases the section's other arrivals, with a 1.9s timeout as backstop.
- Narrow: below 820px same · Reduced motion: the word fully written, everything visible.
- Use when: a personal touch, the one moment that should feel signed · Avoid when: used more than once per page, or other drawings are on screen.
- Effort: S · Needs lib: no · Sources: P224 (https://superhuman.com), P406 (https://jithinrp.com/site.js) · Verdict: ADAPT, changed: Superhuman's fixed .4s strokes became pen-speed strokes, and its image gate is capped at 1.9s so the section never stalls on the word.

### EMP-25 Handwritten margin note
- For: emphasis, definitions-jargon · 1 note per section
- Instead of: an "Our take" box
- Reader sees: a short handwritten note in the margin ("this is the bit that saves Friday") with a curved arrow to the phrase it is about.
- Moves: in-view - the note fades in (opacity .6s, no travel), then the arrow pen draws; the note sits rotated -3deg.
- Build: the note floated right into the margin with a negative margin (the Tufte pattern); the hand face (Caveat 500) at 1.15 × body size in the TVS handwriting ink #2B4A8B; the arrow an absolutely placed SVG path.
- Narrow: below 820px the note sits inline after its paragraph in a tinted strip, never behind a toggle · Reduced motion: static.
- Use when: adding a human voice next to formal copy · Avoid when: the note carries information the reader needs (margins read as optional).
- Effort: M · Needs lib: no · Sources: P307 (https://edwardtufte.github.io/tufte-css/) · Verdict: KEEP

### EMP-26 Pull quote landmark
- For: emphasis, proof-trust · 1 per 3-5 screens
- Instead of: a testimonial carousel
- Reader sees: one real line from the client's own people, set large in the serif, breaking out of the column near where it is discussed, between two ink rules.
- Moves: in-view - the quote mark pen draws; the text arrives; the rules grow from the left (scaleX, .8s); no overshoot and no slide from the edge.
- Build: `blockquote.pull{font-size:clamp(1.5rem,3.5vw,2.6rem);margin-inline:-8vw;border-block:1.5px solid var(--ink)}`, floated right at 40% width on wide screens; the quote glyph an SVG path drawn by dashoffset; attribution in mono 11px caps.
- Narrow: below 820px full width, no float · Reduced motion: static.
- Use when: a stakeholder said it better than you can, and the page needs landmarks · Avoid when: the quote is invented, or repeats the paragraph above word for word.
- Effort: S · Needs lib: no · Sources: P252 (https://en.wikipedia.org/wiki/Pull_quote) · Verdict: ADAPT, changed: the slide from the column edge with an overshoot became a short rise, and the rules now draw in.

### EMP-27 Thread note
- For: emphasis, cause-effect · 1 line under a card grid
- Instead of: a second lede paragraph
- Reader sees: one muted sentence under a grid of cards naming what runs through every item, with its key phrase marked.
- Moves: in-view - it arrives with the grid; the marker sweeps .35s after it lands (EMP-01).
- Build: `.thread-note` margin-top 28px, 16px muted, flex with gap 10px, baseline-aligned: a small icon, then a `<span>` holding the sentence and its `mark`. The span matters: a `mark` placed straight in the flex row is blockified and its band covers only the last line.
- Narrow: below 820px same · Reduced motion: static, marker shown.
- Use when: a cross-cutting theme deserves a pointer before its own section · Avoid when: it grows into a second lede.
- Effort: S · Needs lib: no · Sources: P012 (TVS page.html L67-68, L518) · Verdict: KEEP

## Headlines and type as image

### EMP-28 Statement alone on a screen
- For: big-idea, emphasis, proof-trust · 1 sentence of up to 20 words
- Instead of: a heading followed by a paragraph that restates it
- Reader sees: a single sentence alone on a calm screen at display size, every line the same length, with the evidence set small in side rails or just below for anyone who wants it.
- Moves: in-view - the sentence arrives (.9s); its one marked phrase sweeps .35s later; the stillness is the design.
- Build: `text-wrap: balance` (applies to six lines or fewer in Chromium), `max-width: 18ch`, font-size clamp(2.4rem, 6vw, 5rem), serif 400; the section min-height 80svh, centred; optional rails `grid-template-columns: 1fr 3fr 1fr` at .85rem with small figures.
- Narrow: below 820px 9vw, rails move below the sentence · Reduced motion: static, marker shown.
- Use when: the chapter thesis, or the one finding that must survive a five-second glance · Avoid when: the sentence runs past about 20 words, or this would be the fourth on the page.
- Effort: S · Needs lib: no · Sources: P384 (https://developer.mozilla.org/en-US/docs/Web/CSS/text-wrap), P256 (https://revistapesquisa.fapesp.br/en/straight-to-the-point/) · Verdict: ADAPT, changed: the poster's shrink-to-sticky-header motion is dropped; its evidence rails stay, still.

### EMP-29 Headline set line by line
- For: big-idea, emphasis · 1-3 lines (the hero, and at most one closing line)
- Instead of: a whole headline fading in at once, or letters flying in one by one
- Reader sees: the opening headline appears one line at a time, each line settling into place like type being set.
- Moves: load - each line arrives (12px rise, .8s cubic-bezier(.22,1,.36,1)), lines 90ms apart; the lede follows at +.3s; nothing moves sideways and no letter moves alone.
- Build: measure the real line breaks (wrap words in spans, group them by `getClientRects()` bottom), then rewrap as `<span class="ln" style="--li:i">`; re-measure after `document.fonts.ready` and on width change; keep the plain text for screen readers with `aria-label` on the h1 and the spans `aria-hidden`.
- Narrow: below 820px same, re-measured · Reduced motion: visible at once.
- Use when: the hero headline, and maybe one closing line · Avoid when: every heading (the plain reveal serves the rest).
- Effort: S · Needs lib: no · Sources: P441 (https://aicommon.creamu.co.jp assets/js/main.js, https://townhouse.dev), P375 (https://splitting.js.org/guide.html), P378 (https://www.awwwards.com/inspiration/typography-based-layout) · Verdict: ADAPT, changed: the full-height mask rise, the letter-by-letter rise and the alternating sideways slides all broke the 16px travel rule, so lines now rise 12px with a 90ms stagger.

### EMP-30 Blur-to-sharp line
- For: emphasis, big-idea · 1 statement per screen
- Instead of: a plain fade on the section thesis
- Reader sees: a key sentence comes into focus as it arrives, like eyes adjusting, and then stays sharp.
- Moves: in-view (threshold .5, once) - opacity 0 to 1, blur 6px to 0 and a 12px rise over .9s cubic-bezier(.22,1,.36,1); by words at 60-80ms (capped at 450ms), or by lines at 110ms.
- Build: split words into spans (keep `aria-label` on the parent); a CSS transition on `filter, opacity, transform`; an IntersectionObserver adds `.in`; it never fades out while in view; keep it to short lines, since large blurred areas stutter on tablets.
- Narrow: below 768px same; drop the blur below 600px if it stutters · Reduced motion: visible at once.
- Use when: the one sentence the reader must remember from a section, especially about clarity or seeing · Avoid when: body text, or more than one statement per screen.
- Effort: S · Needs lib: no · Sources: P419 (http://plastic-ocean.com, https://metic.studio/en, https://neutomni.com), P223 (https://ramp.com) · Verdict: KEEP (P419's values; Ramp's 24px blur and 120px travel dropped)

### EMP-31 Ink fills the outline
- For: emphasis, big-idea · 1-3 words, or a thesis line of 5-12 words
- Instead of: a big bold chapter title
- Reader sees: a headline first appears as hollow outline letters, then each word fills with solid ink from left to right until the whole line is solid; the last word may fill in the accent.
- Moves: in-view, once - each word's solid copy wipes left to right by clip-path at pen speed (about .4-.7s a word), word k starting when word k-1 is 60% done; the line always finishes.
- Build: two stacked copies: `.outline` (`-webkit-text-stroke:1.5px var(--ink); color:transparent`) and a `.solid` per word with `clip-path: inset(-.35em calc(100% - var(--w)*100%) -.45em 0)`; drive `--w` per word from a timed JS sequence, never from scroll; use 1.5px or more at display sizes, since the stroke straddles the glyph edge.
- Narrow: below 768px same · Reduced motion: solid text.
- Use when: the promise or thesis line, or chapter titles · Avoid when: more than once per page, or with a thin typeface (the stroke eats the counters).
- Effort: S · Needs lib: no · Sources: P426 (https://piergorelli.com), P372 (https://developer.mozilla.org/en-US/docs/Web/CSS/-webkit-text-stroke), P311 (https://css-tricks.com/how-to-do-knockout-text/) · Verdict: ADAPT, changed: scroll-scrubbed filling, which can stall half done, became a timed fill that always finishes; P311's gradient fill folded in as the same left-to-right wipe.

### EMP-32 Ink label chip
- For: emphasis · 1-4 words on one line (a label-like phrase)
- Instead of: a coloured badge
- Reader sees: a solid ink block wipes across a short phrase from the left and the letters flip to paper colour under it, like a selected tab: "Done for you", "Included".
- Moves: in-view - the top layer's `clip-path: inset(0 100% 0 0)` opens to `inset(0)` over .6s with the pen ease, .35s after the line lands; once.
- Build: a wrapper `display:inline-grid` holding two copies of the phrase in one grid cell; the top copy (`aria-hidden`) has inverted colours, `border-radius:.2em` and the clip; `white-space:nowrap`.
- Narrow: below 768px same, four words at most · Reduced motion: inverted state, static.
- Use when: a label-like phrase: "Done for you", "Included", "Week 1" · Avoid when: the phrase may wrap, or a marker is already on screen.
- Effort: S · Needs lib: no · Sources: P303 (https://emilkowal.ski/ui/the-magic-of-clip-path) · Verdict: KEEP

### EMP-33 Hold that thought
- For: emphasis, big-idea · 1 question per section, 3-5 per page at most
- Instead of: a flap or a "click to reveal"
- Reader sees: a bold question; the one-line answer beneath is softly blurred and sharpens as the reader scrolls a little further, a beat to guess without clicking.
- Moves: scroll-linked - blur goes from 6px to 0, linear, as the card crosses from 70% to 45% of the viewport; it latches sharp and never blurs again.
- Build: `.answer{filter:blur(calc((1 - var(--p)) * 6px))}` with `--p` from a progress observer, stored as max(previous, current); the copy pattern is a question line, a one-line answer, and one sentence of why. No tap target, so the flow stays sequential.
- Narrow: below 768px same · Reduced motion: the answer shown sharp under a visible "Answer" label.
- Use when: an insight is counter-intuitive · Avoid when: the answer is obvious (the pause feels patronising).
- Effort: S · Needs lib: no · Sources: P050 (https://pudding.cool/2025/08/onions/) · Verdict: ADAPT, changed: the blur is capped at 6px (from 8px) and latches, so the answer never blurs again on scroll up.

### EMP-34 Growing frame
- For: emphasis by pacing, atmosphere, before-after · 4-8 beats
- Instead of: every picture at the same size
- Reader sees: drawings start small inside wide paper margins and grow section by section until they fill the screen at the climax, then shrink back for the calm ending.
- Moves: on each step - the frame's inset moves to its new value over .8s cubic-bezier(.22,1,.36,1); one change per section.
- Build: `figure{clip-path: inset(calc(var(--m) * 1%) round 8px)}`; JS maps the section index to `--m` (30, 20, 10, 0, 0, 15) with `transition: clip-path .8s`; the drawing inside keeps its scale while the frame opens around it.
- Narrow: below 820px the same steps at half the inset · Reduced motion: stepped insets without animation.
- Use when: pacing intensity toward a climax (the problem escalates, then the turn) · Avoid when: the page is reference material.
- Effort: S · Needs lib: no · Sources: P267 (https://www.neolemon.com/blog/picture-book-page-turn-anticipation) · Verdict: KEEP

## Wayfinding

### EMP-35 Eyebrow label with numbered ring
- For: emphasis, sequence · 1 per section
- Instead of: section numbers inside the heading
- Reader sees: a tiny uppercase mono line above each heading, sometimes led by a number in a thin circle ("(1) LEADERS").
- Moves: none; it arrives with its heading.
- Build: `.eyebrow{font-family:var(--mono);font-size:12px;letter-spacing:.09em;text-transform:uppercase;color:var(--muted);display:flex;align-items:center;gap:10px;margin-bottom:22px}` and `.eyebrow .n{display:inline-grid;place-items:center;min-width:24px;height:24px;border-radius:12px;border:1px solid currentColor;font-size:11px;padding:0 6px}`; on wood #C9B8A6. The same mono recipe (11px, .08-.09em, caps) serves every card kicker; problem kickers in kumkum.
- Narrow: below 820px same · Reduced motion: n/a.
- Use when: always; it is the page's wayfinding layer · Avoid when: the label needs more than about 5 words.
- Effort: S · Needs lib: no · Code: TVS harvest · Sources: P008 (TVS page.html L26-27; harvest Part 3 base layer) · Verdict: KEEP

### EMP-36 Split section header
- For: emphasis · 1 heading and 1 how-to-read lede
- Instead of: a heading with a centred subtitle
- Reader sees: the eyebrow and a big serif heading on the left; a short "how to read this" paragraph on the right, bottom-aligned with the heading.
- Moves: in-view - it arrives (12px rise, .75s).
- Build: `.head{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,.9fr);gap:56px;align-items:end;margin-bottom:56px}`; h2 max 18ch; `.head .lede{margin-top:0}`.
- Narrow: below 820px one column · Reduced motion: static.
- Use when: the heading states the answer and the lede tells the reader how to read the visual below · Avoid when: the lede runs past about 3 lines.
- Effort: S · Needs lib: no · Code: TVS harvest · Sources: P007 (TVS page.html L33-34; harvest Part 3 base layer) · Verdict: KEEP

### EMP-37 Mini motif badge
- For: emphasis, atmosphere · 1 per section (each section owns one part of a whole)
- Instead of: a section icon
- Reader sees: a small dark disc beside each section heading holding the hero's motif, with only that section's part lit.
- Moves: none; drawn finished, then focused.
- Build: `.mini` a 96px circle, wood background, `overflow:hidden`, the svg at `transform:scale(1.18)` to crop; `<svg data-mini="band1">` then `const k = drawKolam(s); k.finish(); k.focus(s.dataset.mini)`; the heading layout is a grid 96px | 1fr, gap 28px.
- Narrow: below 820px a 64px badge, gap 18px · Reduced motion: same (static).
- Use when: each section owns one part of a whole and needs a stamp · Avoid when: the motif has not been decoded yet (WRD-09 comes first).
- Effort: S · Needs lib: no · Code: TVS harvest · Sources: P005 (TVS page.html L83-85, L544, L959; harvest 2.12) · Verdict: KEEP

---
