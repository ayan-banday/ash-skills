---
name: polished-doc
description: "How do I turn my draft into a clean PDF or Word file? Make any document clearer and better designed while keeping its structure, then export it as a PDF (default), Word, Google Docs, or HTML. Rewrites the words (cuts hedges, filler, negative parallelism; headings that give the answer; one running example; visible impact), regroups long lists into three groups, nested outlines, mind maps, or decision trees, adds visuals only where they explain faster than words (stick-figure scenes, story strips, contrast pairs, flows, timelines, funnels, matrices and more), gives each document its own random but harmonious muted colour palette, and lays pages out with no wasted space. Use this whenever the user shares a draft, report, proposal, memo, plan, handout, policy, SOP, speech script, or notes and asks to make it clearer, cleaner, more readable, more professional, \"less AI\", better designed, or \"turn this into a nice PDF\", even if they only say \"fix this doc\", \"make this look good\", \"clean this up\", or \"make me a PDF\". For scrolling, animated screen pages use brief-page; for course lessons use course-lesson."
---

# Clear Documents

This skill takes a document someone already has and gives it back **clearer, with the same sections in the same order**: plainer words, long lists broken into shapes a reader can hold, visuals where a picture beats a paragraph, a harmonious palette, and pages with no wasted space. The output is a document first, PDF by default, in any format the user needs.

It exists because busy readers give each sentence a second or two and each page a glance. A document passes when a reader who skims the headings gets the argument, and a reader who reads everything never meets a sentence that wastes their time.

## What good looks like

The proven example is `assets/reference-playbook.html` (a 16-page playbook describing this skill, built with it). Its qualities:

- **The writer's structure survives.** Same parts, same order, same facts. Only the wording, list shapes, visuals, and layout change.
- **Headings state the answer.** "Leads wait for the morning sort before anyone owns them", never "The problem".
- **No long flat lists.** Ten rules sit in three named groups; twelve visuals become a two-question decision tree; a 40-item overview becomes a nested outline and a mind map.
- **Visuals only where the content has a shape**, in two styles: hand-lettered stick-figure sketches for people and situations, clean charts for amounts and order.
- **A palette from a seed**, muted and contrast-checked, different for every document.
- **Full pages.** No page holds one visual with empty space under it; no heading sits alone at a page bottom.

## Workflow

### 1. Read the document and map it

Before changing anything, list its sections in order, the facts and numbers it contains, its reader (a boss, a client, students, a panel), and what the reader must do after reading. Note the writer's voice: formal, warm, personal. Ask only for what is missing and changes the result: the reader if it is unclear, the output format if they named none (default to PDF and say so), and whether a deadline or ask exists.

### 2. Rewrite the words

Follow `references/writing-rules.md`: ten rules in three groups (cut what carries no weight, make it specific, connect it and keep the voice). Rewrite headings so each gives its section's answer. Keep the writer's vivid lines. **Never invent a fact, number, quote, or result.** Anything new you must add (a deadline, a reason, a missing step) is highlighted in the document with `<mark>` and listed in the hand-off note for the writer to confirm.

### 3. Fix long lists

Follow `references/lists.md`. Up to 7 items stay a list. 8 to 15 become three named groups. 16 to 30 nest. Bigger, or items that link, become a mind map or a decision tree. Apply this to the writer's lists and to any long run of parallel items in the document's structure.

### 4. Add visuals where they explain faster than words

Follow `references/visuals.md`. Ask the two questions: what is the content about (people, steps and time, or amounts and choices), then which shape fits. Draw only when the test passes; a document may need none. Never chart numbers the writer didn't give.

### 5. Choose a palette

Follow `references/colour.md`. Pick a seed (random, or the series seed), preview with `python scripts/palette.py --count 6 --seed N --sheet palettes.html` (it also prints JSON; the sheet is what you look at), choose one that fits the document's tone.

### 6. Build the HTML

Copy `assets/template.html` to a short working folder (Windows paths over 260 characters break Chrome). Replace its sample content with the document, one `section.part` per section, top-level elements indented two spaces as in the template. Copy visual markup from `assets/reference-playbook.html`. Layout rules and components are in `references/layout-and-design.md`. Use a cover only for documents of four or more pages; shorter documents open with the commented-out `.titleblock` in the template.

### 7. Export and check

```bash
python scripts/scan_copy.py doc.html
python scripts/build_pdf.py doc.html doc.pdf --seed N --footer "Document name · draft" --save-html final.html
python scripts/check_pages.py doc.pdf --sheets shots/          # add --allow 1 only if page 1 is a cover
```

`--save-html` writes the palette-applied HTML, which is the HTML deliverable. Fix every scan hit (quoted bad examples excepted) and every SHORT, GAP, or STRAGGLER page, rebuild, and **look at every page** in `shots/`. The full list of checks and past bugs is in `references/qa-checklist.md`. For Word, Google Docs, or HTML output, follow `references/export.md` after the PDF passes.

### 8. Hand over

Give the file, then a short note: what changed in the writer's terms, every flagged addition, anything kept on purpose that the rules would cut, the palette seed, and anything not verified.

## Rules that are easy to get wrong

- **Don't restructure the document.** Rewording headings is the job; merging, reordering, or dropping sections needs the writer's yes. The user's own words: it takes a document and makes it clearer "by keeping most of the document structure and things the same".
- **Impact needs no number.** Show what changes for the reader in words. A made-up statistic is worse than none.
- **Visuals are earned, not sprinkled.** One per section is the brief-page habit, not this skill's. Clarity first, decoration never.
- **No wasted space.** Don't force page breaks between parts. Let tables split by row. Size figures to fit. Run `check_pages.py` every time; the user specifically does not want one visual on a page with empty space under it.
- **Check your own edits.** In testing, the editor's first fixes introduced two new negative parallelisms. Scan the rewritten text with the same rules.
- **Keep the voice.** A clear document that no longer sounds like its writer has failed.
- **Colour through variables.** In copied SVG, use the classes (`.ln`, `.fp`, `text.red`) or `style="fill:var(--primary)"`; hex attributes ignore the palette seed.
- **Sketch labels are one to three words.** Long labels overlap figures; say the rest in the text.

## Files

- `references/writing-rules.md`: the ten rules with bad and good pairs, what to flag, headings, emphasis, banned phrases.
- `references/lists.md`: size thresholds, grouping into three, nesting, mind maps, trees, bad patterns.
- `references/visuals.md`: the two-question picker, twelve visuals in three groups, drawing stick figures, sketch versus chart style, sizing, bad visuals.
- `references/colour.md`: picking a seed, harmony types, eleven roles, 60-30-10, base hue by document type, what never to do.
- `references/layout-and-design.md`: ten design rules in tiers, page setup, no wasted space and how to fix each flag, keeping headings with content, components.
- `references/export.md`: PDF, Word (with figures.py and docx_helpers.js), Google Docs, HTML, setup and troubleshooting.
- `references/qa-checklist.md`: the checks, the hand-off note, bugs already hit.
- `references/worked-examples.md`: a memo, a two-page proposal, and a speech, each before and after.
- `references/background/`: the colour and design research from Figma's resource library that the rules rest on.
- `assets/template.html`: the starter, with every style, the stick-figure symbols, and one sample of each common pattern.
- `assets/reference-playbook.html`: the full proven example with all twelve visuals, the decision tree, nested outline, mind map, palette strips, and a before/after memo.
- `scripts/palette.py`: seeded harmonious palette generator with contrast checks.
- `scripts/build_pdf.py`: applies a palette seed, keeps headings with their content, prints the PDF with a footer.
- `scripts/keepnext.py`: the heading-keeping step (run automatically by build_pdf.py).
- `scripts/check_pages.py`: flags short pages, blank gaps, and a straggling last page; writes page sheets to look at.
- `scripts/scan_copy.py`: copy scan for hedges, lead-ins, negative parallelism, generic headings, em dashes.
- `scripts/figures.py`: exports each figure as PNG for Word or Google Docs.
- `scripts/docx_helpers.js`: docx-js helpers that rebuild the document in Word with the same palette.
