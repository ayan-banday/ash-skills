# Colour

Each document gets its own random but harmonious palette: muted, professional, and contrast-checked. `scripts/palette.py` builds it from a seed so it can be rebuilt exactly. The full research behind these numbers is in `references/background/colour-research.md`.

## Contents
- How to pick a palette
- The five harmony types
- The eleven roles
- 60-30-10 on a page
- Choosing a base hue by document type
- What the palette never does

## How to pick a palette

1. **One document, one seed.** Pick a random seed unless the user named one or the document belongs to a series (then reuse the series seed so the set matches).
2. Preview candidates: `python scripts/palette.py --count 6 --seed <N> --sheet palettes.html`, then screenshot or open the sheet. Pick the one that fits the document's tone (see base hue below).
3. Apply it at build time: `python scripts/build_pdf.py doc.html doc.pdf --seed <N>`. The script swaps the block between `/* PALETTE START */` and `/* PALETTE END */`.
4. Record the seed in the cover footer or the hand-off note.

Other `palette.py` options: `--harmony analogous|monochromatic|complementary|split-complementary|triadic`, `--hue <0-360>` to fix the base hue, `--format json|css`. Every palette is contrast-checked; a role that cannot pass is listed under `failed` in the JSON. Never use a palette with a failure.

## The five harmony types

| Type | Built from | Character | Use |
|---|---|---|---|
| Analogous | Primary and a neighbour 30° away | Calm, natural | Quiet default |
| Split-complementary | Primary and a hue beside its opposite | Contrast with little tension | Quiet default |
| Monochromatic | One hue at two lightness levels | Cleanest, can feel flat | Formal, single-topic pieces |
| Complementary | Primary and its opposite | Energetic, easy to overdo | Only with a small accent |
| Triadic | Three hues 120° apart | Lively | Only with muted chroma; third hue for charts |

## The eleven roles

| Role | Job | Limit |
|---|---|---|
| bg | Page background, near white, tinted toward the primary hue | White for print |
| surface | Panels and figure backgrounds | Near white |
| ink | Body text | 7:1 contrast on bg |
| muted | Captions, labels, footers | 4.5:1 |
| line | Rules and borders | Light enough to stay quiet |
| primary | Headings accents, key shapes, decision box | 4.5:1, white text on it 4.5:1 |
| primary-soft | Tinted fills, callouts, table tier rows | Ink on it 7:1 |
| accent | One or two highlights a page | 3:1 for shapes |
| accent-soft | One highlight band or note | Ink on it 7:1 |
| alert | Costs, slow steps, risks; always with a word | 4.5:1, brick not fire-engine red |
| ok | Good outcomes; always with a word | 4.5:1, kept apart from alert in hue and lightness |

## 60-30-10 on a page

- About **60%**: page and body text.
- About **30%**: the quiet layer of rules, soft fills, captions, table bands.
- **10% or less**: primary and accent. Headings marks, key bars, the decision box, at most one or two accent spots per page.
- Squint test: a page thumbnail is mostly white and grey, with primary giving structure and one small spot of accent.

## Choosing a base hue by document type

- **Reports, proposals, finance, health:** cool hues (teal, slate blue, blue-green). Avoid a red primary.
- **Course pages, memos, personal pieces:** warm or earthy hues (olive, terracotta, ochre) are welcome.
- **Mix temperature:** a cool primary takes a warm accent, and the other way round.

## What the palette never does

- **No neon and no gradients.** Flat, muted fills print cleanly.
- **No pure grey or pure black.** Neutrals carry a trace of the primary hue.
- **No colour as the only signal.** Alert and ok always come with a word, icon, or position.
- **No equal-strength opposites.** In a complementary palette one colour leads and the other stays small.
- **No more than two hue families** for primary and accent; extra harmony hues only inside charts, at most four series.
- **No coloured page background** in documents meant for print.
