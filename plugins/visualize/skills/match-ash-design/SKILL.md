---
name: "match-ash-design (wada)"
description: "[helper] How do I design and colour anything Ash or his readers will see, so it looks like his and never the same twice? Picks one numbered combination from Wada Sanzo's colour book, turns it into contrast-checked colour tokens for that place, and applies Ash's design rules by case. Use before any page, prototype, picture or deck, and when Ash says 'my design rules', 'my colours' or 'a palette from the book'. For words, use match-ash-writing."
---

# Match Ash's design

Ash's second most common correction, after copy, is the look: pages too dense, colours he dislikes, pictures that decorate. This skill holds those corrections and his colours in one place: **every page takes one numbered combination from Wada Sanzo's *A Dictionary of Color Combinations*** (1933, 348 combinations), checked in code. **The words follow `/write:match-ash-writing`** (`../../../write/skills/match-ash-writing/SKILL.md`); a page runs both.

**The building skill decides the job; this skill decides the look.** When the two disagree, the rule with the newer date wins; with no date on either, the building skill wins for its own artifact.

## Steps

1. **Name the case and its screen.** Find the row in "The look per case" below. No reader given? It's **for Ash**. Done when you can say the reader, the screen that comes first, and the palette place in one line ("A study result for Ash, phone first, place dark").
2. **Decide the visuals.** Apply "When to draw, when to write" in `references/design.md`. Done when you can name what each picture explains faster than words, or the page has none.
3. **Pick the combination.** Run `python scripts/palette.py --place <place> --seed "<page title>"` and paste its `:root{...}` block (on dark, also its key-line CSS). "My colours" means a combination from the book; a preset (`--preset 1|2|3`) only when Ash names it. Ash named a number? `--combo N`. Want to choose? `--count 6 --sheet sheet.html` and screenshot it. Brief pages use their own script with `--combo N` (`/visualize:brief-page`). Done when the page's CSS opens with the combination's number and names in a comment and every colour on the page is a token.
4. **Apply the look.** Use your case's section of "The look for each case", then "Phone and laptop" and "Simple" in `references/design.md`. Done when nothing on the page is in "What Ash rejects".
5. **Check it yourself before Ash sees it.** Screenshot at the case's width (`../brief-page/scripts/shots.py`, or Playwright) (390px for phone, 1280px for laptop) and look for: anything a fixed bar covers, a chart mark with no number, text that runs off or wraps badly, two accents fighting, the same thing shown twice, and sideways scroll. Done when the screenshot shows none of them.
6. **Show it.** Follow step 4 of `/write:match-ash-writing`, and name the combination ("No. 273, Rose and wine") so Ash can ask for another by number.
7. **When Ash corrects the look in a way this skill should have caught,** add the rule to `references/design.md` in one line, with his words and the date, and bump the version.

## The look per case

| Case | Screen first | Theme | Palette place |
|---|---|---|---|
| Study result, report, prototype for Ash | Phone (from a notification) | Dark | `dark` |
| Study page or book, the week page, Ash's own tools | Laptop | Dark | `dark` |
| Brief for someone who decides | Laptop, check 400px too | Light and dark | brief-page `--combo` |
| Pitch for an outsider | Phone (a WhatsApp link) | Warm paper | `pitch` |
| Course page for students, Udyaan | Phone | Light; the Udyaan brand wins on its pages | `light` |
| Slides, post cards, anything else for others | Its own frame | Light or dark | `light` (dark slides: `dark`) |
| Printed document | Paper | Light only | `print` |

## Reference files

- `references/design.md`: open on every run. Colour from the book, when to draw, the look per case, phone and laptop, simple, what Ash rejects, and the phone study page.
- `scripts/palette.py`: one combination into checked tokens for a place. `--list` counts what fits each place; `--test` checks every combination and the three approved presets; `--preset 1|2|3` gives Graphite and chalk, Ink and clay, Charcoal and rose.
- `assets/wada-colors.json`: the book's 159 colours and which of the 348 combinations each belongs to (MIT, `assets/LICENSE-wada-colors`; compiled by Dain M. Blodorn Kim, fixed by Matt DesLauriers).
