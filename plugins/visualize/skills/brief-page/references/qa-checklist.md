# QA checklist

Run this before handing the page over. Rendering bugs hide from reading the code, and a page read alone has no one to cover for a confusing line. Most fixes below came from looking at actual screenshots.

## Steps

1. **Build.** `python scripts/build.py --template T --libs L --out OUT --seed N`. It swaps in the palette, inlines any libraries, runs the copy scan, and syntax-checks the page script with Node when Node is installed.
2. **Fix every copy-scan hit.** The scan checks dashes, banned words, hedges, negative parallelism, long paragraphs, section headings that aren't questions, and repeated `data-pattern` names. Re-run until clean.
3. **Read for what a script can't catch:**
   - Does each heading name its thing and its situation, so it reads right alone?
   - Is the answer in the first line under each heading?
   - Could the reader explain each section's answer in two or three sentences?
   - Is every term explained where it first appears? Any "this" or "it" with nothing named nearby?
   - Is there a "How will it look?" section when something is being built or changed, showing the finished thing itself?
   - Does the page end on the decisions, with a pick circled?
   - Are open questions marked "Still open"?
4. **The cover test.** Cover the drawings and read the words: if the whole story still arrives, a drawing is decoration, so move a relation or a size into it. Cover the words and look at the drawings: they alone should show what is sorted, what changes, and what it ends as.
5. **Screenshot each section alone.** `python scripts/shots.py OUT --outdir DIR` renders every `<section>` at 1280px and 500px. Open the PNGs and read them.
6. **Both themes.** Re-run with `--theme dark` and `--theme light`. Check every filled shape, the marker, and muted text.
7. **Probe overflow at 400px.** `python scripts/shots.py OUT --overflow 400`. It prints the scroll width and any element past the edge.
8. **Hand-off note.** The seed and type pairing, and what you invented (names, draft labels, framed decisions, mockup content) so Ash can correct it.

## What to look for in screenshots

- Cords or snake lines pointing at the wrong place (drawn before fonts loaded, or not redrawn on resize).
- A drawing whose labels shrink below about 12px at phone width (needs its list twin).
- Shapes overlapping, text clipped inside shapes.
- The pen circle missing its target after text reflows.
- The marker invisible in dark mode or too loud in light mode.
- Muted text too faint in dark mode.
- Two drawings that look the same (a repeat the `data-pattern` names hid).
- A section with only text where the content had a shape.
- Content missing at rest.

## Bugs already hit, and the fixes

| Symptom | Cause | Fix |
|---|---|---|
| Funnel renders as stacked diamonds | `clip-path: polygon` points in order TL, TR, BL, BR | Order TL, TR, BR, BL |
| Bubbles overlap | Center force stronger than collision | Seed positions across the canvas, forceX 0.012, forceY 0.03, collide iterations 8, 400 ticks |
| Orbit shows only some circles | D3 transition frozen mid-draw in headless | No D3 transitions, draw once |
| Last funnel label clipped | Label too long for a narrow tier | Shorten it, lower the font size |
| Python or Chrome says file not found for a file that exists | Path over 260 characters on Windows | Build in a short temp path, copy the result |
| Anchor-link screenshots come out blank | Smooth scrolling and a sticky nav in headless capture | Isolate the section with injected CSS (what `shots.py` does) |
| Phone screenshot cut off at the right | Headless Chrome minimum window width of about 500px | Use the iframe overflow probe for the real 400px |
| A personal side project appeared in a doc for others | Copied from the user's private notes | Leave user-private context out |
| Switchboard cords end short of their sockets | Drawn before web fonts swapped in | Draw after `document.fonts.ready` and on resize |

## Done means

- Copy scan: zero hits.
- Overflow probe at 400px: scroll width under the viewport, nothing listed.
- Every section screenshot read in both themes, no overlaps or clipped text.
- At least three different drawings where the old way would have used lists or cards, and no silent repeats.
- A "How will it look?" section when something is built or changed.
- The hand-off note lists the seed, the type pairing and the invented details.
