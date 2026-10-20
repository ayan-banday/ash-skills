# Design system

Every brief page gets its own palette and type pairing, so no two pages look like one template. What stays fixed is the structure: the token names, the theme shape, the drawn line language, the layout rules. Shasta study pages override the palette with their own look (see `D:\Shasta\_rules\Clusters.md`, "Design"); everything else here still applies to them.

## Contents
- The palette, one per page
- Picking the base hue
- Tokens and what each one means
- Light and dark
- Type pairings
- The drawn line language
- Layout and spacing
- Components
- Motion
- Responsive rules
- Accessibility

## The palette, one per page

The method combines polished-doc' seeded generator with pitch-site's habit of taking colour from the subject's world.

1. **Pick the base hue** from the subject when it has a material colour (below). Otherwise let the seed choose.
2. **Preview six candidates:** `python scripts/palette.py --seed N --count 6 --sheet palettes.html [--hue H] [--harmony analogous]`. Screenshot the sheet (`shots.py` or headless Chrome) and look at it. Each card shows the light and dark theme with a sample heading, marker, tints and status words.
3. **Pick one** that fits the tone, then build with `python scripts/build.py ... --seed N [--hue H --harmony X]`. The build swaps the block between `/* PALETTE START */` and `/* PALETTE END */` in the template.
4. **Record the seed** in a CSS comment (the script writes it) and in the hand-off note.

Every palette is contrast-checked in both themes. `palette.py` exits with an error and names the failing check when a seed can't pass; pick another seed.

**Harmony:** analogous or split-complementary for a calm default; monochromatic for a formal one-topic page; complementary or triadic only with a small accent. Tone guide: decisions and money lean cool; people, learning and making lean warm. A cool brand takes a warm accent and the other way round.

## Picking the base hue

Ask what the subject is made of, then take a hue from it:

- **Kraft card, crates, parcels:** about 60 to 70.
- **Terracotta, brick, clay:** about 35 to 45.
- **Paper ledgers, ink:** about 250 to 270 with a warm accent.
- **Chalkboard, slate:** about 200 to 220.
- **Indigo dye, denim:** about 270 to 285.
- **Turmeric, marigold:** about 80 to 90.
- **Plum, beetroot:** about 340 to 355.

Avoid by default: navy night heroes, Anthropic's clay and ivory, purple-to-blue gradients. Green is allowed for a brief page when the subject calls for it, but Ash dislikes it in pitch work, so it is never the default.

## Tokens and what each one means

| Token | Job | Meaning rule |
|---|---|---|
| `--bg` | page | tinted toward the brand hue, never pure white or black |
| `--surface` | sheets, mockups, slips | near white (light) or one step up from bg (dark) |
| `--ink` | body text and drawn lines | 7:1 on bg |
| `--muted` | small labels, struck old values | 4.5:1 on bg and surface |
| `--line` | rules, sheet edges | quiet |
| `--soft` | quiet fills | ink on it 7:1 |
| `--brand` | the main subject's mark: headings' eyebrow numbers, the thing the page is about | 4.5:1 on bg; `--brand-ink` on it 4.5:1 |
| `--accent` | the one part a drawing points at | 3:1 for shapes; never body text |
| `--accent-soft` | one highlighted panel per screen | ink on it 7:1 |
| `--marker` | the highlighter behind what the reader gets or decides | ink on it 7:1 |
| `--alert` | goes away, goes wrong, still open | always with a word |
| `--ok` | done, kept, works | always with a word |
| `--tint-1..3` | up to three groups, only when the groups carry meaning | ink on each 7:1; label every group in words |

Neutrals carry a trace of the brand hue, so nothing looks like default grey. 60-30-10: about 60% page and text, 30% quiet layer (lines, soft fills, muted text), 10% or less brand, accent and marker.

## Light and dark

The page works in three states: system light, system dark, and an explicit `data-theme`. `palette.py` writes exactly this shape:

```css
:root { /* light values */ color-scheme: light; }
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) { /* dark values */ color-scheme: dark; }
}
:root[data-theme="dark"] { /* the same dark values */ color-scheme: dark; }
body { background: var(--bg); color: var(--ink); }
```

In dark mode `--brand` is light, so text on a brand fill uses `--brand-ink`. The marker turns into a dim band behind light text. Check every filled shape and every SVG in both themes; SVG strokes use `var(--ink)` so they flip with the theme.

## Type pairings

Pick one pairing per page, and change it from the last page you built. Each has a display face, a body face, a hand face for notes and pen labels, and a mono face for small labels. All are on Google Fonts; fallback stacks are required.

| Pairing | Display | Body | Hand | Mono | Feels like |
|---|---|---|---|---|---|
| **Workshop** | Barlow Condensed 600 | Public Sans 400/600/700 | Kalam 400 | IBM Plex Mono 500 | crates, tools, building things |
| **Field notes** | Fraunces 600 (opsz) | Source Sans 3 400/600/700 | Caveat 500 | JetBrains Mono 500 | research, learning, people |
| **Drafting** | Archivo Narrow 600 | IBM Plex Sans 400/500/600 | Architects Daughter | IBM Plex Mono 500 | plans, systems, engineering |
| **Ledger** | Newsreader 600 (opsz) | Figtree 400/600/700 | Patrick Hand | DM Mono 500 | money, decisions, reports |

- Body 17px, line-height 1.55, 66ch max width.
- h2 `clamp(1.7rem, 4vw, 2.6rem)`, max width 28ch, `text-wrap: balance`. Question headings run longer than slogans, so they get a little more width and a little less size than the old answer headlines.
- Hand face at 1.05 to 1.25rem, in `--ink` or `--alert`, never for anything longer than 12 words.
- Mono for eyebrows and small labels: uppercase, letter-spacing 0.08 to 0.12em.
- `font-variant-numeric: tabular-nums` wherever digits line up.

## The drawn line language

Taken from pitch-site's drafting direction, static.

- **One stroke family:** `.ln` 1.8px round caps and joins, `.ln.thin` 0.9px for leader lines, `.ln.guide` dashed "3 5" at 30% for construction lines, `.ln.hid` dashed "6 4" for removed or hidden things.
- **Sheets, not cards.** Mockups, slips and notes are paper sheets: `--surface` fill, 1px `--line` edge, corners 2 to 4px. Big radii belong only to real devices drawn in the story (a phone).
- **A pen for emphasis:** the marker band, the pen circle, the wavy underline, the strike line. They look hand-made, sit at fixed positions, and never animate in a loop.
- **No icon sets.** Small objects (a crate, a sheet, a key, a person) are drawn in the line kit as `<symbol>`s and reused with `<use>`.

## Layout and spacing

- One wrapper: `max-width: 1080px`, centred, 16px side padding on `body` (more with safe areas).
- Sections are bands with 64px vertical padding (46px on phones), separated by space or a 1px line. Alternate the band background between `--bg` and `--soft` sparingly to mark the top screen, the short answer and the close.
- Inside a section: eyebrow, heading (the question), the answer line, then the drawing and detail in a grid with `gap: 24px` to `32px`.
- Use grid and `gap`, not sibling margins. Every grid child that holds text has `min-width: 0`.
- No sticky nav by default: the page is short and read top to bottom. A small "jump to the decisions" link on the top screen is enough. Long pages (eight or more sections) may add a slim sticky bar with section numbers.

## Components

- **Eyebrow:** mono, uppercase, muted: "3 of 7".
- **Answer line:** the first line under the heading, 1.15rem, ink, one bold phrase.
- **"You'll decide" box:** on the top screen, an `--accent-soft` panel with one line per decision.
- **Sheet:** `.sheet` frame for mockups, with a title bar reading "Example view".
- **Still open:** a small line starting with the mono label "Still open" in `--alert`.
- **Decision slip:** `.slip`, a paper sheet with the question, the options and the pen circle.
- **Pill:** mono 0.7rem, uppercase, used for status words only.

## Motion

- Default: none. The page is static and complete at rest.
- Allowed only when the motion is the explanation: a route drawing itself once to show order, a before/after toggle the reader clicks. Each such motion has a finished static state shown under `prefers-reduced-motion` and in screenshots.
- Hover snaps (no slow fades), nothing follows the cursor, nothing loops.

## Responsive rules

- Test at 400px and 1280px. The body never scrolls sideways. Wide tables and rulers scroll inside their own `.scroll`.
- Breakpoints: 900px (three columns become two, margin notes drop under their paragraph), 700px (drawings with small labels switch to their list twin; switchboards become grouped lists), 560px (one column).
- Respect safe areas: `padding-inline: max(16px, env(safe-area-inset-left))`.

## Accessibility

- Text contrast at least 4.5:1 in both themes (the palette script checks the tokens; check any colour you mix yourself).
- Status always in a word as well as a colour.
- SVG drawings have `role="img"` and an `aria-label` saying what they show; decorative strokes are `aria-hidden`.
- Visible keyboard focus (`outline` on `:focus-visible`).
