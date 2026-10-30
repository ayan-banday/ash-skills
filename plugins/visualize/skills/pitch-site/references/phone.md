# Phone pages: the appetizer

How to build the phone version of a pitch, or a page that only ever lives on a phone. It comes from Ash's brief on
2026-10-30 (references: the Microduck explainer, Zerodha's ZERO01 carousel, an HG comic carousel), and two builds:
`assets/examples/phone/tvs-bike.html` (a website) and `assets/examples/phone/udyaan-14-days.html` (a swipe-through).

## Contents
- What a phone page is for
- Website or swipe-through
- The motif has to add information
- Progress, never "1 of 7"
- Copy for a thumb
- The screen kit
- Mechanics that worked
- Checks and the critic
- Bugs already hit

## What a phone page is for

The reader opens a WhatsApp link and will not read. **The phone page is the appetizer:** the bare points, clear at a
glance, with some awe, and then a push to the full page on a laptop when one exists ("read the full proposal on your
desktop"). It is a funnel: every screen earns the next one, and the close hands over the laptop link (copy it, email
it to yourself, or open it anyway) plus the one person to write to. For many pages (a team plan, a short brief) the
phone page is the whole thing, and that is fine.

The TVS desktop page on a phone was 2,166 words over 28 phone screens; its phone cut says the same four asks in
about 350 words over 10 screens, cards and labels included.

## Website or swipe-through

- **Website (the default).** A vertical scroll. Copy sits at the top of each screen; the motif is pinned below it
  (the right half on a laptop) and changes as each section passes a line 45% down the screen. Use it for proposals
  and anything with a motif that builds.
- **Swipe-through.** One idea per slide, swiped sideways like an Instagram carousel, with a Next button and arrow
  keys. Use it for short sequences people step through: a plan by day, a process, a recipe.
- **Never a video-caption layout.** Microduck's centred character with 4-word captions works because it is a film;
  on a scrolled page the captions read as subtitles with nothing playing.

## The motif has to add information

Each screen, the motif shows something the words do not: which part we're on, what's done, how big a thing is, what
changes. Clarity first, always. The Mughal-garden build (Udyaan onboarding, 2026-10-22) held too many ideas at once
(water, sluice gates, cracks, brass stones, tags) and confused the team. The test:

- **One job per part,** said in one line: handlebar = leaders, engine = suppliers, dashboard = systems, body =
  design, frame = the TVS Way (which TVS already has, so the metaphor credits them).
- **A real tie to the reader's world:** TVS makes motorbikes; Udyaan is agriculture, so a seedling.
- **Cover the words:** the motif alone still shows where you are and what changed.
- **Out of focus when it's backdrop.** Blur it (3px, 40% opacity) behind a hero or a close; sharpen it when it speaks.

Phone motif ideas, each with the information it carries (add to this list as builds land):

- **The client's own product, built part by part** (bike, truck, phone, building): each part is one ask; done parts in
  ink, the current part in the accent, future parts as dashed construction lines.
- **A growth chart** (seedling beside a ruler): height = how far through a plan; the ruler range = how long a phase is.
- **A train line with stations:** a station per step; the train sits at the current one.
- **A jar or tank filling:** money raised, seats taken, progress toward a target.
- **A cricket over (six balls):** six short points, one ball bowled per screen.
- **A dabba or tiffin stacking:** layers of an offer, one tier per screen.
- **A map pin walking a route:** a journey or a rollout by city.

## Progress, never "1 of 7"

A counter is lazy. Progress lives in the motif: the bike assembling, the plant growing up the ruler, the jar filling.
If the motif can't carry it, use something from the subject's world (a fuel gauge, a crop row, a scoreboard).

## Copy for a thumb

- **One headline per screen** that says the point, in the display face; one or two short lines under it. There is no
  fixed word budget; the critic checks that every screen reads in about three seconds.
- **Bold the one line that says what the reader gets,** and put the proof in the card above the motif (the
  Microduck number card): one big phrase, one small line.
- **Teach through the metaphor** in Ash's voice: "Leaders steer. Give them the whole road." "Every student project
  starts as a seed."
- **Quotation marks only for trivia.** No "you told us" quote blocks.
- **Label examples as examples** on screen, and keep every fact on the facts sheet.

## The screen kit

- **Number card:** small mono label, one big phrase with the marker, one small line. Sits above the motif.
- **Live board:** three rows with a status each; one row in the accent blinks a few times, then holds.
- **Circled choice:** dashed chits, one circled by a hand-drawn ellipse in the accent.
- **Seed packets:** open options nobody has picked yet, two by two.
- **Trial rows:** "don't guess, test": rows of five sprouts, one row grows tallest, then a field for everyone.
- **Gathering dots:** scattered coloured dots move into a ring (a team forming).
- **The funnel close:** "That was the short version", what the full page has, then Copy the link for your laptop,
  Email it to yourself, the address as selectable text, and "open it here anyway".
- **The contact close:** the one person, their email as selectable text, a Copy button.

## Mechanics that worked

- **Website:** a `position:fixed` stage at the bottom 54svh holds the card slot and the motif; sections are
  `min-height:100svh`; a scroll handler picks the section whose top has passed 45% of the screen and sets
  `data-state` on the stage; CSS does everything else (part classes `todo`, `now`, `done`; one card per state). The
  copy block has a paper gradient behind it so text never sits on line art. At 900px and up the stage moves to the
  right half and the copy centres on the left.
- **Swipe-through:** a flex row with `scroll-snap-type:x mandatory` and `scroll-snap-stop:always`; the index comes
  from `scrollLeft / clientWidth`; Next and back buttons in a bottom bar; arrow keys; `window.__go(i)` for
  screenshots. Each slide keeps a right gutter (96px) for the progress motif. On a laptop the deck is a 460px column.
- **One-off animations** fire when a state starts (crates slide into the engine, wheels turn twice, dots gather) and
  hold their end state. Reduced motion turns them off and keeps the states.

## Checks and the critic

```bash
python scripts/phone_shots.py http://localhost:PORT/page.html shots/ --mode scroll   # or --mode flip, add --dark
```
It saves one 390x844 frame per section or slide plus `sheet.jpg`, and prints console errors, horizontal overflow and
the word count. Look at the sheet in light and dark, fix what you see, then run one critic agent per page in the
background with: the screenshots, the source, the full page it funnels to, Ash's brief in his words, and
`taste.md`. It does two passes (an uninitiated reader at three seconds a screen, then a creative director on the
metaphor, progress, type size and layout), scores clarity and awe, and returns six ranked fixes with exact copy.

## Bugs already hit

- A stroke with `stroke-dashoffset:1` and round caps still draws a dot at the path's end; hide it at zero.
- `pathLength="1"` rescales every dash value, so a dashed construction style (`3 4`) becomes solid.
- Zooming the motif on a narrow screen crops labels at the edge; keep labels inside the frame or drop the zoom.
- A named contact gets their name, never a guessed pronoun ("Write to Jinto").
