# QA checklist

Run this before handing anything over. Most layout bugs only show in the rendered pages, so reading the HTML is not enough.

## Steps

1. **Copy scan.** `python scripts/scan_copy.py doc.html`. Fix every hit except quoted "before" examples. Then read for what the script cannot catch: headings that name a slot, counts that don't match their list, bold whole sentences, invented numbers.
2. **Build.** `python scripts/build_pdf.py doc.html doc.pdf --seed N --footer "..."`.
3. **Page check.** `python scripts/check_pages.py doc.pdf --allow 1 --sheets shots/`. Fix every SHORT, GAP, and STRAGGLER (fixes are in layout-and-design.md), rebuild, re-check.
4. **Look at every page.** Open the sheets. Look for:
   - a heading alone at a page bottom, or a caption away from its figure
   - labels overlapping lines or each other in sketches, or cut off at the edge
   - a flow row wrapping onto a second line (shorten labels)
   - matrix labels far from their dots
   - colours that look neon, muddy, or too alike
5. **Faithfulness.** Compare with the original document: same sections, same order, every fact and number present. Every addition is highlighted and listed.
6. **Other formats** (if asked): follow export.md and look at the rendered pages again.
7. **Hand-off note** (below).

## Hand-off note

Short, in the reply, after the file link:
- what changed, in the writer's terms (headings rewritten, hedges cut, two lists grouped, three visuals added)
- **every addition to flag:** new deadlines, reasons, or facts to confirm
- anything kept on purpose that the rules would normally cut, and why
- the palette seed
- anything not verified (fonts offline, Word not checked)

## Bugs already hit, and the fixes

| Symptom | Cause | Fix |
|---|---|---|
| Nine half-empty pages | Every part forced onto a new page | Parts flow; only the cover breaks |
| A page ends after one figure, two thirds empty | The next table refused to split | Tables split by row; heading becomes the caption |
| Heading stranded at a page bottom | Chrome ignores `break-after: avoid` | `keepnext.py` wraps headings with their next block (automatic in build_pdf.py) |
| A part's title split across two pages | Same | Same, and give every h2 a lede paragraph |
| One box alone on the last page | A few lines spilled | Two-column grid for short items, or trim |
| Before and After labels on one page, the boxes on the next | Column heads not kept with content | Wrap the two columns in `.cols keep` |
| Label "late results" over the figure's hand | Long label in a tight sketch | One-word label ("late"), say the rest in text |
| Stairs label crossing the riser | Label wider than the tread | Shorter label, centred on the tread |
| Flow row wrapping | Long step names | "Request" not "Refund request" |
| Matrix labels away from dots | Text placed by eye | Put each label 14 px right of its dot |
| Section screenshots blank in brief-page's shots.py | That script hides wrappers | Use check_pages.py sheets for documents |
| `sed` or heredoc errors | Quotes and `#` in replacements | Use Python or the file tool for edits |
| Part heading alone at a page bottom | No lede after the h2 | Write a lede after every h2; with none, keepnext keeps the h2 with the next block |
| One table row orphaned on the next page | Short tables could split | Tables of 8 rows or fewer never split |
| Highlighted text unreadable in the decision box | `<mark>` tint on a dark fill | `.decide mark` uses a light band with white text |
| Short document had no title | h1 only existed in the cover | Use `.titleblock` for documents under 4 pages |
| Final HTML kept the template palette | build_pdf applied the seed to a temp file | Use `--save-html` |
| "Dr." flagged as a one-word sentence | Abbreviation read as a sentence end | scan_copy skips common abbreviations |
