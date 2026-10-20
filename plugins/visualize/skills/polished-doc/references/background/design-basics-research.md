# Design basics research for a document-clarity skill

Scope: the Figma Resource Library "Design basics" hub and the principle articles it leads to, translated to printed or PDF/Word documents (reports, proposals, memos, lessons). Figma's articles are written for web and app UI, so the "On a document page" parts and the checks are my translation. Where a point comes from general document-design practice and not from the Figma text, it is marked (adds).

Note on sources: the hub itself is a filtered list of 129 articles with no single "principles" page. The principle content lives mainly in the "13 graphic design principles" article, with supporting detail in the UI principles, consistency, and typography articles.

## Principles

### 1. Hierarchy
**Meaning.** Order the content by importance so a reader sees what matters first and can tell main points from support. Size, weight, colour, position and spacing are the levers.

**On a document page.**
- Headings: three visibly distinct levels at most (title, section, subsection), each clearly bigger or heavier than the one below.
- Paragraphs: body text is the quiet baseline; nothing in it competes with headings.
- Figures and tables: captions are smaller than body text; the takeaway belongs in the heading or a lead sentence, not buried in the chart.
- Callouts: one per page at most, for the "must not miss" item.
- Page breaks: put the most important thing at the top of the page or section.

**Do.** Open a section with a bold heading that states the conclusion, then the supporting paragraphs in plain body type.
**Don't.** Style every heading level in the same size and weight, or give a minor note the same visual rank as a key finding.

**Quick check.** Squint test: blur or zoom out the page. Can you still name the top three things in order? Also read only the headings; do they tell the story?

### 2. Contrast
**Meaning.** A clear difference between elements draws the eye and marks what is important. It can come from size, weight, colour, shape or texture, not only colour. Too much contrast becomes jarring and loses its effect.

**On a document page.**
- Headings vs body: differ in size and weight, not by one small tweak.
- Text vs background: dark text on a light ground at full strength; lighter greys only for secondary text, and still readable.
- Tables: header row set apart (weight or a tint), body rows quiet.
- Callouts: a tint or rule that separates them from body without a heavy box.

**Do.** Use a clearly different heading style and keep body text near-black on white.
**Don't.** Use light grey text or pale colour on colour, or make a heading only slightly larger than body so the difference looks like a mistake.

**Quick check.** Greyscale test: convert the page to greyscale. Do the heading, table header and callout still stand out, and is every line still easy to read? Check body contrast against accessibility guidance (adds: roughly 4.5:1 minimum).

### 3. Emphasis
**Meaning.** Choose one focal point and make it stand out so the message lands quickly. Emphasis works only if it is rare: when everything is bold, nothing is.

**On a document page.**
- Paragraphs: bold a short key phrase, not whole sentences; avoid stacking bold, colour, italics and underline.
- Figures: highlight the one bar, line or cell the reader should look at; mute the rest.
- Callouts: reserve for a single critical warning, decision or number.

**Do.** Bold the one phrase per paragraph that carries the answer, and colour only the key data point in a chart.
**Don't.** Bold whole paragraphs, use ALL CAPS for long passages, or combine bold, colour and underline on the same words.

**Quick check.** Count emphasised elements on the page. If emphasis covers more than about a tenth of the text (adds), cut it back.

### 4. Proximity
**Meaning.** Items placed near each other read as related; items far apart read as separate. Spacing is the cheapest way to show structure.

**On a document page.**
- Headings: closer to the text that follows than to the text before.
- Captions: tight to their figure or table, with a clear gap to the next paragraph.
- Lists and callouts: related lines grouped; a clear gap between unrelated groups.
- Page breaks: never leave a heading alone at the bottom of a page or a caption on a different page from its figure (adds: keep-with-next).

**Do.** Put more space above a heading than below it, so it attaches to its own section.
**Don't.** Space everything evenly, so a heading floats halfway between two sections and nothing looks grouped.

**Quick check.** For each heading and caption, ask which block it belongs to. Does the gap say the same thing? Look for orphaned headings at page bottoms.

### 5. Alignment
**Meaning.** Line elements up on shared edges, centres or baselines. It creates order, makes the page look deliberate, and guides the eye down the page. A grid helps. Left alignment is the usual default for text.

**On a document page.**
- Headings, body, captions, figures and table edges share the same left margin.
- Tables: text columns left-aligned, numbers right-aligned (adds), headers aligned to their columns.
- Figures: align to the text column or span it fully; do not float at arbitrary indents.
- Margins: the same on every page.

**Do.** Left-align body text and headings to one margin and set figures flush to the column.
**Don't.** Centre long paragraphs, or mix centred, left and indented alignment for similar elements on one page.

**Quick check.** Overlay a vertical line on the left margin of the PDF. Do headings, text, figure edges and captions land on it? Count distinct left edges; fewer is better.

### 6. White space
**Meaning.** The empty space around and between elements gives breathing room, aids readability, supports balance and keeps a page from feeling overwhelming. How much to use depends on purpose: dense reference material can run tighter than an executive summary.

**On a document page.**
- Margins: generous enough that the text block is not crammed to the edge.
- Paragraphs: a visible gap between them; line spacing around 1.15 to 1.5 (Figma's type article gives about 112 to 120 percent of font size as a baseline; long document text often reads better slightly looser) (adds).
- Tables and figures: padding inside cells and clear space around figures.
- Page breaks: do not fill every page to the last line to save pages.

**Do.** Give tables cell padding and leave clear space before each major section.
**Don't.** Shrink margins and font size to squeeze content onto fewer pages.

**Quick check.** Hold the page at arm's length. Does it look like a wall of text? Is there a clear gap between every pair of blocks? Does any cell text touch a border?

### 7. Repetition and consistency
**Meaning.** Reuse the same colours, fonts, shapes and spacing so the document feels like one thing. Readers learn the pattern once and then move faster. Change a pattern only with a reason.

**On a document page.**
- Headings: each level looks the same everywhere (size, weight, spacing, colour).
- Callouts, captions, tables and lists: one style each, reused.
- Limit to two or three type styles and a small palette: one primary colour, one accent, tints, black and white.
- Recurring items (titles, running headers, page numbers) sit in the same place page to page.

**Do.** Define styles once (in the Word template or CSS) and apply them, so every level-2 heading matches.
**Don't.** Introduce a new font, colour or callout look partway through the document.

**Quick check.** Flip through the PDF at thumbnail size. Do all pages look like siblings? List the fonts and colours used; is the count small?

### 8. Typography (scale, weight, line length, leading)
**Meaning.** Size signals importance; weight and style add emphasis; and body type must be comfortable over long stretches. Bold or high contrast overused hurts legibility.

**On a document page.**
- Body: a readable size (adds: 10 to 12 pt in print and PDF), lines of about 40 to 60 characters per Figma (print practice often tolerates up to about 75), and leading loose enough for long reading. Longer lines need more leading.
- Headings: scale steps big enough to read as a hierarchy.
- ALL CAPS: only for short labels, with a little extra letter-spacing.
- Tables and captions: smaller than body but still readable (adds: not below roughly 8 to 9 pt).
- Pair at most two typefaces; one is usually enough.

**Do.** Use one clean typeface family, a steady size scale, and a comfortable line length.
**Don't.** Run full-page-width lines of small type, or set long passages in capitals or all bold.

**Quick check.** Count characters on a typical body line (aim for roughly 50 to 75). Check the smallest text on the page is still legible at 100% zoom.

### 9. Balance and proportion
**Meaning.** Spread visual weight so the page does not feel lopsided. Large or heavy elements read as more important, so relative sizes also carry hierarchy. Balance can be symmetrical or deliberately uneven.

**On a document page.**
- A big figure beside a little text, or a heavy table that dominates a page of prose, tips the balance.
- Size figures to their importance: a key chart can be wide; a minor one small.
- Avoid a page that is dense on one half and empty on the other without intent.

**Do.** Size a figure to match its importance to the argument and place it near the text that discusses it.
**Don't.** Drop a full-page graphic for a minor point, or stack three heavy callouts on one page.

**Quick check.** Step back from the page. Is visual weight spread sensibly, and does the heaviest element match the most important idea?

### 10. Movement and rhythm
**Meaning.** Movement is the path the eye follows through the page. Readers scan in common patterns (Z, F, or layered bands), so key items should sit where the eye lands. Rhythm is repeated elements spaced predictably, which makes the flow feel steady.

**On a document page.**
- Put the lead point at the top-left of the page and of each section.
- Use headings and bold lead-ins as stepping stones for scanners.
- Repeat a regular pattern (heading, short paragraph, figure) so the reader learns the beat; vary it only at key moments.
- Page breaks: end pages and sections at natural pauses.

**Do.** Give each section the same shape (heading, one-line takeaway, support) so scanning is easy.
**Don't.** Scatter callouts, pull quotes and figures at random positions so the eye jumps around.

**Quick check.** Trace your eye from the top of the page without reading. Does it hit the title, then the key headings, in a sensible order, without detours?

### 11. Unity
**Meaning.** Unity is the sum of the others: consistent colour, type, shapes, spacing and grid so the whole reads as one harmonious piece.

**On a document page.**
- Cover, body pages, appendices and tables look like they belong to one document.
- Charts reuse the same palette and fonts as the text.
- Grid and margins are shared across all pages.

**Do.** Apply one template to the whole document, including charts and tables.
**Don't.** Paste in charts or tables that carry their own fonts, colours and borders.

**Quick check.** Put the first, middle and last pages side by side. Do they look like they came from one source?

### 12. Colour (supporting)
**Meaning.** Colour sets mood and brand, but must stay distinguishable, including for people with colour-vision deficiency. Keep the palette small.

**On a document page.**
- Use colour for meaning (heading accent, key data point, callout tint), not decoration.
- Do not rely on colour alone to carry meaning in charts or tables (adds: add labels or patterns).
- Check it survives greyscale printing.

**Do.** One accent colour for headings and key highlights, with labels as well as colour in charts.
**Don't.** Use red versus green as the only cue, or colour many unrelated things differently.

**Quick check.** Greyscale test and a colour-blind simulation on the finished page; is every distinction still readable?

## Rules worth making mandatory

Ranked by how much each improves clarity for a busy reader:

1. **Clear heading hierarchy with takeaway headings.** At most three visibly distinct levels, each level styled identically throughout, headings that say the point. (Hierarchy)
2. **Comfortable body text.** Readable size, loose enough leading, lines of roughly 50 to 75 characters. No long passages in capitals or all bold. (Typography)
3. **Proximity that matches structure.** More space above a heading than below; captions tight to figures; no heading orphaned at a page bottom; no figure split from its caption. (Proximity)
4. **One shared left edge.** Headings, body, captions, figures and table edges align to the same margin; text left-aligned, numbers right-aligned in tables. (Alignment)
5. **Emphasis is rare.** At most one short bolded phrase per paragraph, no stacked styles, one callout per page, one highlighted data point per chart. (Emphasis)
6. **Strong text contrast.** Near-black on white for body, header rows clearly distinct, nothing in pale grey that fails accessibility contrast; must still work in greyscale. (Contrast)
7. **Define styles once, reuse everywhere.** Two typefaces max, a small palette, one style each for callouts, captions, lists and tables, applied by style and not by hand. (Repetition, unity)
8. **Generous white space.** Real margins, cell padding in tables, clear space between sections; never shrink type or margins to save pages. (White space)
9. **Colour is never the only signal.** Labels or patterns alongside colour in charts and tables; palette limited to one primary and one accent plus neutrals. (Colour)
10. **Proportion fits importance.** Size figures and callouts to how much they matter, and keep page weight evenly spread. (Balance, proportion)

Why this order: the first four decide whether a reader can find and read the content at all; 5 to 7 decide whether the important parts get noticed and the document feels trustworthy; 8 to 10 are refinements that matter once the basics hold.

Suggested final gate for the skill: after rendering the PDF, run the squint test, greyscale test, left-edge test and orphan test on every page, and fix failures before delivery.

## Sources

URLs read (all fetched during this research):
- https://www.figma.com/resource-library/design-basics/ (hub; lists article titles, no dedicated principle pages)
- https://www.figma.com/resource-library/graphic-design-principles/ (13 graphic design principles; main source)
- https://www.figma.com/resource-library/ui-design-principles/ (hierarchy, contrast, proximity, alignment, consistency)
- https://www.figma.com/resource-library/consistency-in-design/ (repetition, limited type and colour, emphasis overuse)
- https://www.figma.com/resource-library/typography-in-design/ (type hierarchy, 40 to 60 character lines, leading, caps)
- https://www.figma.com/resource-library/typography-anatomy/ (contrast, hierarchy, scale, weights, legibility)

Not found: guessed URLs for dedicated "visual-hierarchy", "design-principles" and "what-is-alignment-in-design" pages returned 404.

Caveats: Figma's articles target digital UI, so the document-specific advice and every item marked (adds) is my adaptation, not a Figma claim. A web search snippet (Design Force) also suggested a greyscale test, which I used in the contrast check; I did not read that page.
