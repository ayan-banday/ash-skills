---
name: brief-page-udyaan
description: "[Udyaan teammates] How do I brief a teammate so they arrive knowing what we're deciding? Turn an idea, plan or decision into a self-guided web page that briefs a teammate, boss or partner before a session. They read it alone, with nobody presenting, and arrive knowing what they're walking into and what they'll be asked to decide. Each section heading is the question the reader would ask, each answer is drawn as well as written (drawn patterns instead of lists, card rows and step strips, never the same visual twice), the page always shows how the finished thing looks, and every page gets its own contrast-checked palette in light and dark. Use whenever Ash wants to brief, prime or update someone (\"send Mohit a page on this\", \"brief my boss before Thursday\", \"explain the plan so they get it without me\", \"make this visual\", \"show this as HTML\", \"put this in HTML\", \"a page they can read on their own\"), or wants a plan, process, onboarding flow, report, framework or explainer turned into a page someone reads on screen. Also the build step for Shasta study pages. Use polished-doc instead when Ash already has a draft and wants the same structure back as a clean printable PDF or Word file. Use pitch-site-udyaan when the page must persuade an outside reader who won't read."
---

# Clear visual HTML: the brief page

This skill turns an idea into one HTML page that a teammate reads alone before a session. **Nobody presents it.** The page has to explain itself to someone who dislikes reading, so they arrive primed: they know the plan, why it is shaped that way, what it will look like, and what they'll be asked to decide.

Two jobs matter equally. **The words answer the reader's questions in plain sentences,** and **every idea with a shape gets a drawing that shows the shape.** The drawings come from pitch-site-udyaan's catalogue, kept static: they explain, they don't perform.

## When this skill, and when another

- **This skill:** Ash has an idea, plan or update and wants a page someone reads on screen, alone, before talking to him. He may hand over notes or just talk; the skill builds the structure.
- **polished-doc** (`../polished-doc/`): Ash already has a draft and wants it back clearer as a PDF or Word file, same sections. It prints; this one scrolls.
- **pitch-site-udyaan** (`../pitch-site-udyaan/`): the reader is outside, has to be persuaded, and won't read. Motion, a motif that draws itself, one ask.
- **story-plan** (`../story-plan/`): plans a living metaphor when the idea is abstract (values, a framework). This skill builds what it plans.

## What good looks like

The reference build is `assets/examples/plugins-brief.html` (source: `plugins-brief.template.html`): Ash briefing Mohit, his micro-SaaS partner, on packing his Claude skills into five plugins. Open it before building. Its qualities:

- **The top screen says what the page is for:** the question it answers, who it's for, how long it takes to read, and what the reader will decide in the session.
- **The short answer comes first,** in three sentences, so a reader who stops there still knows the plan.
- **Every heading is a question the reader would ask,** naming the thing and the situation: "Which of Ash's skills go into which plugin?", never "The new structure".
- **Every section has at most one drawing, and no drawing repeats:** copies drifting apart, a crate opened up, a switchboard of cords, struck names with new ones written in, a sieve, a slash menu.
- **"How will it look?" gets its own section** with the finished thing shown concretely.
- **It ends on the decisions,** each with Ash's recommendation circled, so the session starts at the choice instead of the explanation.

`assets/reference-deck.template.html` is the older onboarding build. Copy its wiring for a funnel, a rail or a scroll story with a building panel; ignore its forest-green theme and its answer-style headings.

## Workflow

1. **Get the facts and the reader.** Who reads it, what they already know, what session it prepares for, what they'll decide. Use only numbers and names you were given. Leave Ash's private context (his other projects, reflections) out unless he says otherwise. If Ash is away, infer, and log each assumption for the hand-off note.
2. **Write the reader's questions.** List what the reader would ask, in the order they'd ask it. Each becomes a section, phrased by the heading rules in `references/writing-rules.md`. If Ash gave a structure, keep his sections and order, and still phrase each heading as the reader's question. The default page order is in `references/page-shape.md`.
3. **Write the copy first,** section by section, in plain text before any markup. Each section answers its question so the reader could explain it back in two or three sentences. Cut every line that doesn't help answer it.
4. **Pick one drawing per section** from `references/visual-patterns.md`: find the lazy default in your draft (a list, a card row, a step strip, a bold number) and use the drawn pattern that replaces it. **Record each pick in a `data-pattern` attribute;** the scan fails a page that uses one twice. Some sections need no drawing.
5. **Pick the palette and type.** Run `python scripts/palette.py --seed N --count 6 --sheet palettes.html` (add `--hue` when the subject has a material colour), screenshot the sheet, pick one, and pick a type pairing. Method in `references/design-system.md`.
6. **Build from the starter.** Copy `assets/starter.template.html` to a short work path. Fill sections, copying pattern markup from the reference build. Then `python scripts/build.py --template T --libs L --out OUT --seed N` swaps in the palette, inlines any libraries, and runs the copy scan.
7. **QA with `references/qa-checklist.md`:** copy scan clean, section screenshots read in both themes, 400px overflow probe clean, the cover test (pictures alone, then words alone).
8. **Hand over:** what the file is, where it is, the seed and type pairing, and one short list of what you invented (names, draft labels, decisions you framed) so Ash can correct it. When Ash will share a link, add `--artifact <path>` to the build and publish that copy as a private artifact (load artifact-design first).

## Rules that are easy to get wrong

- **It explains itself.** Every term is explained where it first appears. Every "this" and "it" has its thing named nearby. A reader with no Ash beside them never has to guess.
- **Headings are questions that name the thing and the situation.** No slogans, no answer headlines, no counting the contents. See the Headings section of `references/writing-rules.md`.
- **Each section answers its question.** After reading it, the reader can say the answer in two or three sentences of their own. If they could only repeat labels, rewrite it.
- **Show how it looks.** When the page describes something being built or changed, one section shows the finished thing: a mockup, a filled-in example, a before and after. Describing the parts is never enough.
- **Never the same drawing twice on one page,** unless repeating it is the point (the same crate shown before and after). The scan checks `data-pattern`.
- **Lists that are really shapes get drawn.** A sequence, a split, a sorting, a before and after, a choice: each has a drawing in `references/visual-patterns.md`. A plain list stays a list only when its items have no relation to show.
- **Drawings show something true.** Counts, widths and positions mean something stated in the text. With no data, show order or grouping only, and say what the shape means in one line.
- **Text lives in HTML, shapes in SVG.** Short labels inside the drawing, sentences beside or below it, so nothing shrinks to 6px on a phone.
- **Static by default.** Everything is readable at rest and in a screenshot. Motion is allowed only where it explains (a pen line drawing the order of a route once). No scroll-triggered fades, no count-ups, no loops.
- **One colour, one meaning.** The marker means "what the reader gets or decides"; alert means "goes away or goes wrong"; brand marks the main subject. Never colour five categories just to tell them apart; label them in words.
- **A page of its own.** New seed, new type pairing, new drawings. Two briefs side by side should not look like one template.
- **No emoji, no icon sets, no gradients, no wall of identical cards.**

## Files

- `references/page-shape.md`: the default page order, the top screen, section anatomy, the decision close.
- `references/writing-rules.md`: copy rules with good and bad pairs, question headings, emphasis, lists, banned words, the scan.
- `references/visual-patterns.md`: the lazy-default index, the drawn patterns by content shape, data drawings, "how it looks" patterns, static build notes.
- `references/design-system.md`: per-page palette, type pairings, the drawn line language, tokens, light and dark, layout, responsive rules.
- `references/libraries.md`: what to inline, if anything.
- `references/qa-checklist.md`: the checks and the bugs already hit.
- `assets/starter.template.html`: the page skeleton with palette markers, line classes, marker, pen circle and one sample section.
- `assets/examples/plugins-brief.template.html` and `plugins-brief.html`: the reference build.
- `assets/reference-deck.template.html`: the older onboarding build, for funnel, rail and story-panel wiring.
- `scripts/palette.py`, `scripts/build.py`, `scripts/scan_copy.py`, `scripts/shots.py`, `scripts/fetch_libs.py`.
