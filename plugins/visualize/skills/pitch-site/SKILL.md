---
name: "pitch-site (udyaan)"
description: "[website] How do I make an outside reader say 'Hell yeah, let's do this'? Build a single-file proposal or marketing website for readers who won't read, published as a claude.ai artifact. A motif from the client's world draws itself on and carries the story, each of the reader's asks gets its own answered section, lists become drawn patterns, impact is highlighted in colour, and the page ends in one concrete ask with a named person. Reads as a vertical scroll, a paper deck turned page by page, or a horizontal scroll painting, with a phone appetizer (a short website or a swipe-through) that funnels to the laptop page or stands alone. Opens with a short grilling. Use whenever Ash wants a proposal, pitch, partnership offer, capabilities brochure, \"website instead of a brochure\", a site \"like the TVS one\", or says \"they won't read it\", \"make it a link\", \"make it creative but clear\", \"lists shouldn't be lists\", \"one page then the next page\", \"horizontal scroll\", \"phone version\", \"make it work on mobile\", \"swipe-through\". For a document someone will actually read, use brief-page; for a PDF or Word file, use polished-doc."
---

# Clear proposal site

This skill turns a brief into one web page that a busy reader understands without reading: their own asks quoted
back, a drawing from their world that draws itself on and carries the argument, one answered section per ask, the
capabilities shown as drawn patterns instead of lists, what the reader gets highlighted in colour, and one concrete
next step with a named person. It codifies "Carrying the TVS Way" (JAIN University to TVS IQL), which took six rounds
of Ash's feedback, plus two rounds of reviewer agents on a second build. The skill front-loads those rounds.
It also builds for phones (`references/phone.md`): a short appetizer that gets the points across on a WhatsApp
link and funnels the reader to the laptop page, or stands alone when a phone page is enough.

## What good looks like

Open these before building, and copy their mechanics:
- `assets/examples/tvs.html`: the original (scroll, kolam). Loved by Ash; its later review is in `references/background/`.
- `assets/examples/coastline.html` with source in `assets/examples/coastline-src/`: scroll, drafting direction, a
  pinned stage that x-rays the client's truck and pulls back onto a real map, and a close where the drawing returns
  finished with an empty PILOT ROUTE cell circled. Reviewed twice; the strongest build so far.
- `../story-plan/assets/examples/range-src/`: the Mauna Kea dive from The Range, a horizontal scroll
  painting. Below the waterline is the model for a living metaphor (ARC-33); the numbered stops on the summit above it
  are the counter-example. It belongs to the story-plan skill.
- `assets/gallery.html`: every module working on one page.
- `assets/architectures/demo-paged.html` and `demo-horizontal.html`: the same sections as a paper deck and as a scroll painting.

Their shared qualities:
- **The reader's asks open the page, in their words,** each answered once in its own section, named the same everywhere.
- **One drawing from the client's world carries the story:** it draws itself on in the hero, builds part by part
  through the page, and returns finished at the close with the ask inside it.
- **Nothing is a list.** Who does what is a snake or a switchboard; a process is a pinned stage or an orbit; the close is pictured.
- **Every capability ends in what the reader gets,** marked with the marker sweep, one per screen.
- **Calm, explanatory motion:** lines draw like a pen, one moving thing per screen, everything readable at rest.
- **A palette from the subject's own materials,** never a default, and no two builds alike.
- **The picture holds the information.** When an idea is abstract (values, a framework, a mental model), cast it as a
  world the reader travels through, one creature per part, instead of writing it out (the story-plan skill).
- **It is watched, not read.** Each section runs a small story (who, what they want, what is in the way, what we
  do, what they get, the world changed), the sections rise and release like a film, and the close returns to the
  hero's scene, changed. The story-plan skill plans this as a storyboard.

## Two paths: the grilling picks one

Most of Ash's pages are low stakes (a presentation, a team plan), and he wants them fast and cheap. The stakes
question in the grilling sets the path. **Clarity never drops:** both paths keep the message spine, the facts
sheet, the copy scan, the sweep's word and marker checks, and the uninitiated reader.

- **Fast (low stakes).** Steps 0, 1, 5, 7, 8 and 10 as written. Step 2: take the recommended direction in one line
  unless Ash named one. Steps 3 and 4 shrink to the story map in the playback: no story-plan storyboard, no
  builds-log rotation. Step 6: use a direction generator or a module as it is; no separate motif test page. Step 7:
  write the fragments yourself, no builder agents. Step 8: `sweep.py --sizes laptop` (add `ipad` only if it will be
  shown on a tablet), no `--live`. Step 9: the uninitiated reader alone, one round; fix and ship.
- **Full (high stakes).** Every step as written, both reviewers, up to three rounds.
- **Full, hero first (option C).** As full, but after the starter and the hero fragment, sweep the laptop size and
  run the creative director's hero check (`references/review.md`) before building any other section. A failed
  concept then costs one fragment, not the page.

## Workflow

### 0. Grill first: one session on what the page must say
Ash is often not yet clear on what the page must say, so every build opens with one grilling
(`references/intake.md`, "The grilling"). Lead with your best interpretation: what happened, the reader, **the
message spine** (3 to 6 plain sentences the page must get across, ending in the action) and **the motif call**
(whether a motif helps at all, and if so 2 or 3 options, each with the information it carries). Then at most four
lettered questions where you are unsure, always including **phone, laptop or both** and **the stakes** (which sets
the path above). Save the agreed spine to `work/message.md`. Nothing is built before he answers, unless he says
"don't ask".

### 1. Brief and facts
Follow `references/intake.md`. Get the reader, their asks verbatim, what we offer, what proof may be used and how,
and the one action with a real named contact. Write `work/facts.md`: every number, name, quote and promise the page
may use, including the asks word for word and every capability specific (counts, roles, durations, price). Confirm
spellings from written sources; Ash dictates by voice. If Ash is away, infer and log every assumption.

### 2. Direction
Ask the one inspiration question in `references/intake.md`. A named direction: open its file in
`references/directions/`. Something new: study it properly (raw CSS for a site, ffmpeg frames for a video, exact
geometry for an object) and derive the palette from its materials (`directions/00-intake.md` Part 3). No answer:
offer 3 to 5 directions, recommendation first; when Ash is away, take the recommendation and say why in one line.

### 3. Recipe
Choose the architecture (`scroll`, `paged`, `horizontal`), the signature move and the close from
`references/recipes.md`. Read the last five lines of `references/builds-log.md` and change at least two of the four
choices from the previous build. Judge anything the catalogue does not cover with `references/taste.md`.

### 4. The argument and the story map
Follow `references/story.md`: write the argument (reader, asks, the one belief after the first screen, a claim and
proof per ask, the action, 8 to 12 things only this client has, the competitor test). Pick one pattern per section
from `references/catalogue/00-picker.md`; for an abstract idea with 3 to 6 parts, test ARC-33 first with
`../story-plan/references/living-metaphors.md`; the picker's "lazy default and what replaces it" index turns
every list, card row and step strip in the draft into a drawn pattern. Then run the story-plan skill on the
story map: it writes `work/storyboard.md` (one row per screen: beat, shot, the one bright thing, the one mover, the
words, tension) and checks it; `../story-plan/references/handoff.md` says how this skill builds from it. Play the story map
and storyboard back to Ash before building.

### 5. Copy first
Write all copy into `work/story.md` before any markup, one screen per spine sentence from `work/message.md`,
following `references/copy-rules.md` (question or statement, plain full sentences, fewest words) and
`references/writing-rules.md`, then run
`python scripts/scan.py work/story.md --facts work/facts.md`.

### 6. The motif
Draw the client's own object (their truck, their plant, their product) as named parts, or use the direction's
generator (`assets/motifs/kit.js` plus `<direction>.js`). Tune it on its own test page against the reference before
splicing it in. Plan its states: the hero, one stage per section (done parts solid, the current part drawing, future
parts as construction lines), and the finished close.

### 7. Build
Copy `assets/starter.html` to `work/starter.html` and fill its tokens and fonts from the direction. For `paged` or
`horizontal`, add the shell from `assets/architectures/` as `work/frag-00-arch.html`. One fragment per section
(`work/frag-N-name.html`), copied from `assets/modules/` or `assets/examples/coastline-src/` where one fits, built from
the catalogue entry otherwise. Prefix every class. For a big page, write the starter, facts and all copy yourself,
then give each builder agent one or two fragments with exact copy and pattern IDs (`references/architecture.md`).

### 8. Check
```bash
python scripts/build.py work/
python scripts/scan.py work/index.html --facts work/facts.md
python scripts/palette_check.py work/starter.html
python scripts/sweep.py work/index.html --out work/shots/ --live
```
Run them with plain `python`. Fix every hit, then look at every frame (`references/qa-checklist.md`). The sweep
measures each laptop screen (over 80 words, text painted under a shape, more than one marker, marker and accent over
8%), so fix those before any reviewer runs; reviewers are for what a script cannot see. Preview in the browser
pane through a `.claude/launch.json` http.server entry; judge layout with `?final=1`.

### 9. Review
Write `work/plan.md` (the concept sentence, the motif and what each part stands for, palette tokens, type pairing,
the signature move) so the creative director can open it after its cold read. Fast path: the uninitiated reader
alone, one round. Full path: the creative director and the uninitiated reader in
parallel as background agents (`references/review.md`). Apply the fixes, rebuild, re-sweep. Two rounds is usually
enough; three at most. A deliberate break of a slop tell goes in the page's exceptions block, not into an argument
with the reviewer.

### 10. Publish, hand over, log
Load artifact-design, publish `work/index.html` as a private artifact, and write the hand-off note: the link, the
recipe and story map in two lines, every assumption or example to confirm, the reviewer scores, anything not
verified (for example, the artifact viewer cannot be opened from the browser pane without signing in). Append the
build to `references/builds-log.md`. Tell Ash to run `/verify`; the model cannot invoke it.

## Rules that are easy to get wrong

- **The motif adds information or it goes.** On every screen it shows something the words do not (which part, what is done, how far along). The Mughal-garden build held too many ideas and confused its readers.
- **The copy says the spine, in Ash's spoken words.** Each screen says one sentence of the agreed message; a line that is clear but says something else still fails. Steps and facts are statements ("We help students form teams."); a question only where the reader would wonder (`references/copy-rules.md`).
- **Phones get the appetizer, never a squeezed desktop page.** Phone only: build `references/phone.md` alone. Both: the laptop page plus a phone cut from the same facts that ends by sending the reader to the laptop page. Laptop only: the phone gate.
- **The motif carries the whole page, hero to close.** Two builds "opened strong, then drifted into rounded cards and never came back" (creative director, on TVS and on the first Coastline draft). Asks hang off the drawing; the close resolves every ask on it.
- **The motif builds down the page.** Each section shows the drawing one stage further on. Identical dimmed copies of the finished motif read as "a paperclip".
- **One colour, one meaning.** The marker means "what the reader gets"; each tint means one ask; the accent marks one part at a time. On TVS the yellow sat on 30+ phrases and "means nothing".
- **Cards are not the default and lists are not lists.** Three identical cards read as a SaaS row; team lists were "garbage"; horizontal step strips "far too lazy". Use the picker's lazy-default index.
- **Every mark is drawn by the same hand.** A device in the story (a tablet, an office screen) is drawn as a sheet in the direction's line, never as a rendered UI slab with bars and a glowing dot.
- **One wording per ask, said once.** Quote the asks once; later sections name each by its part of the motif. The reader reviewer caught asks renamed further down and a fourth problem nobody raised.
- **Every specific comes from facts.md.** Quotes verbatim only; counts, roles, durations, dates and prices only if listed; outcomes as goals; examples labelled on screen, not only in a counter.
- **The first screen says who, what and what you get,** and fills exactly one screen with nothing from the next section showing.
- **Surfaces come from the direction's material.** Drafting gets near-square sheets; one radius and a 1px ring on everything is a slop tell. Strip kickers, middle dots, "Scroll to...", and captions that narrate the page.
- **Match the reference exactly.** The first kolams read as "circles" and "chain-link fence". Maps use real geography; a draft put Chennai west of Kochi.
- **Lines live inside visuals, and reading is sequential.** A page-long line behind the copy was "distracting from the message". No role pickers, no choose-your-own-adventure.
- **Collaborative, never credit-taking,** and never Ash's own vault projects in client work.
- **A metaphor carries meaning or it goes.** Each creature or object needs a real, checkable fact that maps onto the idea, said in one line. Labelled rings and caption boxes were "boring"; scattered markers to click were "clicky". Tell the journey in order, one stop per step.
- **Pictures carry what words would bloat; words carry what pictures cannot.** Cover the pictures: if the copy
  alone tells the whole story, the drawings are decoration. Cover the words: the frames alone should show who, what
  changes and how it ends. Names, numbers, quotes and the ask are always written; ambiguity is for extras only.
- **One bright thing per frame, and the eye is led to it.** Light, scale, focus, leading lines and lead space
  decide the first look; start wide, go in, pull back wide at the close (story-plan skill).
- **Hover snaps, never glides.** Nothing follows the pointer; only moves between places ease (`references/motion.md` rule 16).
- **Loops run once and everything has a finished state.** Under `?final=1` and reduced motion every section shows its end state with labels; behind the phone gate nothing measures or animates.

## Files

- `references/intake.md`: the grilling (interpretation first, the message spine, the motif call), the brief, the facts sheet, the inspiration question, the story-map playback.
- `references/copy-rules.md`: writing from the message spine, question or statement, the metaphor in the drawing, cutting words, before and after pairs, the copy check.
- `references/phone.md`: the phone appetizer: three templates (scroll website, swipe deck, tear-off pad) and how to invent the next, motifs that add information, progress without counters, the screen kit, the critic.
- `references/story.md`: the argument, the default page order, section anatomy, the close, narrative frames, routes and alternatives.
- `references/recipes.md`: architecture, direction, signature move and close; eight recipes that read differently.
- `references/taste.md`: what Ash loves and rejects, how he works, five questions for judging something new.
- `references/writing-rules.md`: proposal copy rules on top of brief-page's.
- The story-plan skill (`../story-plan/`): living metaphors, film craft, the storyboard and its checker, the story reviewer. This skill builds what it plans.
- `references/motion.md`: the house motion rules, exact values, the pinned stage, loops, reduced motion, the phone gate.
- `references/architecture.md`: the work folder, starter, fragments, modules, the three architectures, build, preview, publish, libraries, devices.
- `references/review.md`: the creative director and uninitiated reader prompts with rubrics and the slop list.
- `references/qa-checklist.md`: the checks, done means, and every bug already hit.
- `references/catalogue/`: 317 patterns in nine families (64 starred), `00-picker.md`, and `considered-and-cut.md` (the alternatives).
- `references/directions/`: `00-intake.md` (intake, colour rules, deriving a palette), 21 direction files, `motif-engine.md`; 21 is the toy explainer (Microduck), with key frames in `assets/reference-frames/microduck/`.
- `references/builds-log.md`: one line per published build.
- `references/background/`: how the TVS site was made (Ash's feedback rounds verbatim, reviews, decisions), the Washington Post video study and the Awwwards study behind the motion rules.
- `assets/starter.html`: tokens, helpers, reveal, marker, chips, phone gate, motif slot.
- `assets/architectures/`: the `paged` and `horizontal` shells, with demos.
- `assets/modules/`: proven section fragments with data at the top (see its README).
- `assets/motifs/`: the motif kit and 20 direction generators.
- `assets/examples/`: `tvs.html`, `coastline.html` and `coastline-src/`; `phone/tvs-bike.html` (phone website), `phone/udyaan-14-days.html` (swipe deck) and `phone/udyaan-calendar.html` (tear-off pad).
- `assets/gallery.html`: every module on one page; `assets/gallery-src/` rebuilds it.
- `assets/reference-frames/`: key stills from the Washington Post scrollytelling reference.
- `scripts/build.py`, `scripts/scan.py`, `scripts/palette_check.py`, `scripts/sweep.py`, `scripts/phone_shots.py`.
