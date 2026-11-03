# How Ash designs

Every rule traces to where Ash said it. **[3+]** means three or more of his skills say it. The building skills hold the full systems (tokens, scripts, catalogues); this file says which applies when, and what holds everywhere.

## Contents
- Colour from the book
- When to draw, when to write
- The look for each case
- Phone and laptop
- Simple
- What Ash rejects
- Phone study page

## Colour from the book

**Every page takes one numbered combination from Wada Sanzo's *A Dictionary of Color Combinations*** (配色事典, 1933): 348 combinations of 2 to 4 colours. "I love all of these colors." (Ash, Nov 3 2026, after seeing them on mockups of every kind of page)

- **Pick it with the script:** `python scripts/palette.py --place <dark|light|pitch|print> --seed "<page title>"`. The same seed gives the same combination; `--combo N` takes one by its number; `--count 6 --sheet sheet.html` shows six to choose from. The script turns the combination into tokens, checks contrast, and refuses a combination that fails.
- **How a combination becomes a page:**
  - **Dark (Ash's pages):** the darkest colour becomes the near-black ground, the light colours become the pastels, the strongest becomes the accent.
  - **Light (for others):** the lightest colour becomes the paper, the darkest becomes the ink, and every colour becomes a soft fill.
- **The lean to his favourites** (Ash, Nov 3 2026: "I quite like the color palettes that I was using"): on dark pages a seeded pick lands about 75% of the time on a combination that reimagines a palette he already liked (Shasta's Espresso and Sand, Charcoal Rose, Ink and Clay, Night Plum; the presets Graphite and chalk, Ink and clay, Charcoal and rose). The rest of the book shares the other 25%, so pages still vary. `--near "<favourite>"` keeps one favourite's look (Shasta's four each fit a topic, listed in the script); `--any` turns the lean off.
- **Study pages Ash studies from** (BBA pages, Shasta study pages, study books) are always dark. BBA and Shasta pages take `--format study`, which prints their own token names with a dark picture board.
- **Which place:** `dark` for Ash's own pages; `light` for briefs, slides, posts, Udyaan; `pitch` for outsiders (drops green); `print` for paper (quieter). Brief pages use their own script with `--combo N`, which takes the same book's hues.
- **How many fit:** run `--list`. On Nov 3: dark 342, light 347, pitch 314, print 347 of 348.
- **The book's colours as printed** (`--b1` to `--b4`) go on big shapes only: a post card's blocks, a slide's diagram, a seedling's leaves. Never behind text.
- **Name it on the page:** put `No. 273, Hermosa Pink + Pansy Purple + ...` in a CSS comment, so Ash can ask for it again by number.
- **A little new each time:** don't reuse the last page's combination. When the subject has a material colour (kraft, turmeric, indigo), pick a combination that carries it.
- **The look Ash approved:** the gallery of mockups at https://claude.ai/artifact/X5ksGgHaPb9gcA2Mi6TSAH (study pages, books, week page, charts, pitches, briefs, slides, print, Udyaan, post cards).

## When to draw, when to write

**Draw when the content has a shape:** an order, a split, a sort, a change, a choice, a share, a narrowing, or one centre with many parts. [3+] (polished-doc visuals "The test"; brief-page visual-patterns)

**Write when:** a short story already works, there's one number (bold it in the sentence), the picture would only decorate, or the reader looks things up (use a table). A page may have no pictures at all. [3+]

**By case:**
- **For others, when the stakes are big** (a brief for someone who decides, a pitch): draw. The lazy default gets a drawn pattern: a list of problems becomes a snake of stops, steps become a route, before and after becomes the same frame drawn twice, a choice becomes a fork with the pick circled. (brief-page visual-patterns; pitch-site catalogue)
  - **Always show how the finished thing looks:** a mockup labelled "Example view", or a before and after. Ash calls "How does it look?" "one of the best questions". (brief-page page-shape)
  - An abstract idea with 3 to 6 parts becomes **one living metaphor**: one world, one creature or object per part. Plan it with `/visualize:story-plan`. (story-plan)
- **For Ash** (chat, study results, plans): **mostly words.** Bullets, bold, a table for comparisons. Draw only the one picture that saves him reading: the shape of a plan, the verdict at a glance. (teach-side-chat rule 11; study-bba writing-rules rule 3)
- **For students:** a picture comes after the words it explains, one idea each, never first under a heading. (course-lesson formatting rule 8)

**Never start with a picture.** "Visuals are there to just make things clear, not to start things out with." Too many visuals that serve nothing get cut. (Ash, Oct 29)
**Don't reuse one picture across pages or projects:** each gets a scene from its own world. "The mountain is not helpful." (Ash, Oct 25 and Nov 2)

**Two covered tests** for any page with pictures. [3+] (story-plan; brief-page qa-checklist)
- Cover the pictures: if the words alone tell the whole story, the pictures were decoration.
- Cover the words: the pictures alone should show who, what changes, and how it ends.

**Every bar or mark carries its own number;** an empty outline never stands for a value. Whatever is compared sits on one scale.

**Picture labels follow the writing rules:** 1 to 3 plain words saying what happens. Jargon labels were "garbage". (break-into-field look)

## The look for each case

**Everywhere** [3+]
- **One combination from the book per page,** contrast-checked in code ("Colour from the book" above). No two pages in a row alike.
- **Lean to the subject's own world:** kraft, terracotta, indigo dye, turmeric, plum. Pick a combination that carries it. (brief-page design-system "Picking the base hue")
- **60-30-10:** about 60% page and text, 30% a quiet layer, 10% or less brand, accent and marker.
- **Colour carries one meaning,** and a word carries it too. The marker means "what you get or decide"; alert means "goes wrong or goes away". Never colour five things just to tell them apart.
- **One bright thing per screen.** One accent does the pointing. One marker per screen; a second cancels the first.
- **Contrast:** body text 7:1, muted text 4.5:1, accent 3:1 and only for shapes.
- **Chrome stays quiet:** buttons and counts on neutral surfaces in plain text. Never a coloured shape inside another one. (Ash on a pink pill with an orange chip: "garbage". break-into-field look)
- **Type:** body 17 to 18px, line height about 1.6, at most 68 characters a line. Two or three faces with jobs: headings, body, mono for small labels, a hand face for notes only.
- **One drawn language:** one stroke weight with round caps, sheets with near-square corners (2 to 4px), a pen for emphasis (a marker band, a circle, a strike). (brief-page design-system "The drawn line language")

**Calm** (Ash, Oct 23 and 27)
- **Easy on the eyes:** never too bright, no flickering grain, the normal cursor.
- **Motion barely noticeable.**
- **Simple colour,** a little new each time ("a little bit new every week"), with colour only on what matters in the text.

**Pages for Ash** (study pages, study results, his own tools)
- **Dark.** "I would never want to read things in white." Near-black charcoal grounds. (break-into-field look)
- **Pastels do the colour, from any colour in the book,** greens and blues included (Ash, Nov 3 2026). **Grounds stay near-black, never tinted blue or green. No yellow marker** ("I'm not a fan of yellow"), so the lead pastel is never yellow; a muted sand is fine. The approved presets stay available: Ink and clay, Charcoal and rose, Graphite and chalk. (break-into-field look)
- **Fonts:** Overpass for headings, Atkinson Hyperlegible for body, Overpass Mono for labels. The old serif is out. (break-into-field look, Nov 2)

**Pages for others**
- **Briefs:** light and dark both, with an explicit theme switch. (brief-page design-system)
- **Pitches:** warm paper, at most two dark bands. **No green in any shade** (mint, teal, aqua). No navy night hero. (pitch-site intake 2.5)
- **Printed documents:** light only, a muted palette. (polished-doc)
- **Udyaan pages:** the Udyaan brand wins; read its README in Fuji `ranges/udyaan/brand/` first.

## Phone and laptop

**Which screen comes first:**
- **Phone first:** anything Ash opens from a notification (study results, reports, prototypes he judges), pitches for outsiders (a WhatsApp link), course pages, messages.
- **Laptop first:** study books (he studies on a laptop), briefs (check at both 400px and 1280px).

**Sending to people:** they open it from WhatsApp, inside the chat, never as a download. The phone version is the short one: **more visuals, less data.** The laptop version holds the bigger data. (Ash, Oct 27 to Nov 2)

**Not dense.** "Dense as fuck... too many things there." His most repeated look correction. (Ash, Oct 23 to Nov 1)
- **What matters goes at the front,** so nobody has to scroll for it.
- **Each thing shows once** on a screen.
- **Less on the side;** no extra boxes nobody asked for.

**Phone rules** [3+] (brief-page design-system; docs/mobile-site-playbook.md; pitch-site phone)
- **16px side gutter,** with safe-area padding. **No sideways scroll.** Wide tables scroll inside their own box.
- **One headline and one sentence per screen** on phone pitches; reads in about 3 seconds.
- **Tap targets at least 44px.** Hover becomes tap. Labels never under 12px.
- **Fixed bars never cover content:** pad the page by their height. A prototype's version switcher docks at the top.
- **A phone page is built for the phone,** never a squeezed laptop page. A wide drawing becomes one tall picture or a list twin.
- **Check it** with a 390px screenshot before you send, and zoom into small parts.

## Simple

- **Clarity wins every tie.** "Creative as fuck. Yet, still being clear." [3+] (pitch-site taste)
- **The smallest design that fully works,** counted in what people must do: new steps, numbers, rules. Cut it, then reuse what Ash has, then use a standard way, and only then build new. (design-like-expert)
- **Fewest words on screen.** At most 80 words a laptop screen on a pitch; cut what the picture already shows. (pitch-site)
- **Motion explains or it doesn't ship.** One moving thing per screen, everything readable at rest. Briefs are still by default. [3+] (pitch-site motion; brief-page)
- **Throwaway prototypes:** beautiful but restrained, one accent colour, no animation. (try-prototype)
- **Show 2 or 3 structurally different directions** when the question is how it should look. Never four colour tweaks of one layout. (try-prototype UI; Fuji rulebook 3: "Ask questions; don't guess four options")
- **Visual work goes in layers:** the look first (colour, type, feel), then the layout. (Fuji rulebook 3 "Visual tickets go in layers")

## What Ash rejects

Ash's words in quotes. (pitch-site taste "What he rejects"; story-plan taste; break-into-field look)
- **Layouts:** horizontal step strips ("far too lazy"); three identical cards; cards inside cards; team lists ("garbage"); a first screen where the next section bleeds in; anything that looks like "a random HTML file" or a template.
- **Colour:** gradients; pure white or black; navy night heroes; Anthropic's clay and ivory; neon; green in pitches; a yellow marker on his own pages.
- **Decoration:** emoji and icon sets, stock photos, videos in the page, a line running behind the copy ("distracting"), glows that follow the cursor, smooth gliding hover.
- **Metaphors that don't carry meaning:** labelled rings, caption boxes, click-to-reveal markers, the mountain by default.

## Phone study page

For a study result, a report or a hypothesis check Ash opens from a notification on his phone. (Ash, Nov 2, via the grilling-layers session; `/plan:grilling`)

**What it holds, in this order. Everything above Sources fits one phone screen (390 by 844px):**
1. **The hypothesis,** in one line, in his words.
2. **The verdict,** big: **Holds**, **Doesn't hold**, or **Not sure yet**, with one line on why. The colour matches the word (a pastel per verdict) and the word is always there.
3. **Up to three reasons,** one line each, the bold phrase first, each a new fact. Never restate the verdict.
4. **One next step,** with what's done when.
5. **Sources and method,** folded behind a tap (`<details>`).

**Look:** the "Pages for Ash" rules (dark, pastels, Overpass and Atkinson Hyperlegible). Body 17px, a 16px gutter, no picture unless it shows the verdict faster than the line does.

**Check:** a screenshot at 390 by 844px shows items 1 to 4 with no scrolling; the copy scan is clean.

**Send:** publish it as a claude.ai artifact and give Ash the link with the verdict in one line.
