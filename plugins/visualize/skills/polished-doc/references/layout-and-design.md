# Layout and design

How a page is built so the reader sees the right thing first and no space is wasted. The research behind the ten rules is in `references/background/design-basics-research.md`.

## Contents
- Ten design rules in three tiers
- Page setup
- No wasted space
- Keeping things together
- Components and when to use them
- Bad layouts

## Ten design rules in three tiers

**Can the reader find and read it?**
1. **Headings in three levels or fewer**, each stating its point. Check: read only the headings.
2. **Comfortable body text:** 10 to 12 pt, line height about 1.5, 50 to 75 characters a line. Check: count a typical line.
3. **Spacing matches structure:** more space above a heading than below; captions tight to figures. Check: for each heading, ask which block it belongs to.
4. **One shared left edge,** numbers right-aligned in tables. Check: draw a line down the left margin.

**Do the key parts stand out?**

5. **Rare emphasis:** one or two bold phrases a paragraph, one callout a page. Check: count the bold.
6. **Strong text contrast** that survives greyscale. Check: view the page in greyscale.
7. **Styles defined once and reused:** two typefaces (serif headings, sans body), one palette, one callout style. Check: compare the first, middle, and last pages.

**Does it feel finished?**

8. **Generous white space** in margins, tables, and between sections, and never wasted space (see below). Check: hold the page at arm's length.
9. **Colour backed by a word,** label, or position. Check: greyscale again.
10. **Size follows importance:** big figures for big points. Check: the heaviest thing on the page should match the main idea.

## Page setup

- A4 by default (`--size Letter` for US readers). Margins 16 to 18 mm, set in `build_pdf.py`.
- Footer on every page: document name on the left, page number of total on the right.
- Serif for headings (Source Serif 4, fallback Georgia), sans for body (Source Sans 3, fallback Segoe UI), hand-lettered font (Patrick Hand) only inside sketches.
- Body 10.6 pt. h1 28 pt, h2 19 pt, h3 12.5 pt, eyebrow 7.6 pt uppercase.
- Light theme only. Documents print.

## No wasted space

The user's rule: **no page with one visual and empty space under it.** White space between blocks is good; a third of a page left blank because the next block didn't fit is not.

How the template prevents it:
- **No forced page breaks** except after the cover. Parts flow on, separated by a 3 px primary rule and spacing. (Forcing every part onto a new page left nine pages half empty in testing.)
- **Tables split between rows** (`tr { break-inside: avoid }`), with the header row repeating. A table that refuses to split leaves a gap the size of the table.
- **Short parallel items in two columns** (`.dgrid`, `.cols`) instead of a long single column.

How to fix a page that `check_pages.py` flags:

| Flag | Cause | Fix |
|---|---|---|
| SHORT, with a figure on the next page | Figure too tall for the space left | Cap the figure's width (`style="max-width:500px;margin:0 auto"`), or move a paragraph after it |
| SHORT, with a table on the next page | Table locked as one block | Put its heading right before it so the build makes it a caption; never wrap a table in `.keep` |
| SHORT, with a heading block on the next page | A part head pulled a big block with it | Give the part a lede paragraph so the head keeps with the lede, not the big block |
| STRAGGLER | A few lines spilled onto a last page | Lay short items in two columns, trim spacing, or tighten one paragraph |
| GAP | A blank band inside the content | Usually a forced break or an oversized `min-height`; remove it |

## Keeping things together

Chrome's print engine ignores `break-after: avoid` on headings, so a heading can end a page with its content on the next. `build_pdf.py` runs `keepnext.py`, which wraps, at the top level of each section:
- eyebrow + h2 + up to two lede paragraphs (write a lede after every h2); with no lede, the first block after the h2
- a `.grp` group header + its first item
- an h3 + the next element
- an h3 right before a table becomes the table's `<caption>`, so the table can still split by row
- tables of 8 rows or fewer never split, so a single row is never orphaned

For this to work, write top-level elements in a section with two-space indentation, exactly like the template. Elements nested deeper are left alone.

`figure`, `.vis`, `.rule`, `.keep`, `.decide`, `.pal`, `.gbox`, and the decision tree never split. Inside the decision box, `<mark>` turns into a light band so flagged text stays readable on the dark fill.

## Components and when to use them

| Component | Class | Use for |
|---|---|---|
| Part | `section.part` | One section of the writer's document |
| Eyebrow | `.eyebrow` | "Part 2 · Writing": the part number and topic |
| Lede | `.lede` | The cover's summary paragraph |
| Group header | `.grp` | Splitting a long run of items into named groups |
| Rule block | `.rule` with `.ba` | A numbered item with before and after |
| Soft callout | `.soft` | The one thing to remember on a page |
| Note callout | `.note` | A side point in the accent tint |
| Two columns | `.cols` | Before and after, stays and changes |
| Two-column grid | `.dgrid` | Six short decisions or items |
| Table | `table` with `thead` | Look-ups and comparisons |
| Tier row | `tr.tier` | Group header inside a table |
| Decision box | `.decide` | The one action at the end |
| Cover | `section.cover` | Documents of 4 or more pages (own page) |
| Title block | `header.titleblock` | Documents under 4 pages, instead of a cover |

## Bad layouts

- Every part forced onto a new page.
- A heading alone at the bottom of a page.
- A caption on a different page from its figure.
- Centred body text, or three different left edges on one page.
- Three callouts on one page.
- A cover on a one-page memo.
- A table of contents for a document under 4 pages.
