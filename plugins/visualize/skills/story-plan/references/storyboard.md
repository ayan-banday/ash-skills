# The storyboard: plan any visual as shots

Films are planned as shot lists before anything is filmed. Plan every visual story the same way, before any markup,
slide or drawing exists. The storyboard is this skill's main output: the host skill (a proposal site, an HTML
explainer, a document, a lesson) builds from it.

## Contents
- The format
- How to fill it
- What the checker enforces
- Worked example 1: Pixar's *Up* montage (the bar)
- Worked example 2: the Mauna Kea dive, re-told
- Worked example 3: a proposal section

## The format

Write it in plain markdown, in the host skill's work folder (`work/storyboard.md` unless the host says otherwise),
under a heading `## Storyboard`, as one table with exactly these columns:

```markdown
## Storyboard

Thesis: <the one sentence the story proves, said at the start and returned at the end>
World: <the one world everything happens in>  ·  Verb: <what the reader does to travel>  ·  Thread: <the object that recurs and shows progress>

| # | Beat | Shot | Bright | Moves | Words | Tension | Plant or payoff |
|---|---|---|---|---|---|---|---|
| 1 | character, want | extreme wide | ... | ... | ... | 2 | plant: lamp |
```

- **Beat:** one or more of `character`, `want`, `obstacle`, `action`, `outcome`, `reaction` (the story spine,
  `film-craft.md`).
- **Shot:** `extreme wide`, `wide`, `medium`, `close-up` or `extreme close-up`.
- **Bright:** the one thing lit or largest on this screen. A reaction row may light everything together.
- **Moves:** the one thing that moves, or `nothing`.
- **Words:** the words on screen, 20 or fewer. Quote real copy, not a description of it.
- **Tension:** 1 to 5.
- **Plant or payoff:** `plant: <key>` or `payoff: <key>`, a short key like `lamp`; leave empty otherwise.

Then check it: `python scripts/storyboard_check.py work/storyboard.md`.

## How to fill it

1. **Write the thesis first.** One sentence. If you cannot, the story has no point yet; go back to the content.
2. **Pick the world, the verb and the thread** (`living-metaphors.md` for abstract ideas; the reader's own world for
   anything concrete: their truck, their campus, their day).
3. **One row per screen, stop or section.** 5 to 9 rows is the usual range. More than 12 means the story is two
   stories; split it or cut.
4. **Run the spine across the rows.** The first rows set character and want, the middle rows obstacle and action, the
   last rows outcome and reaction. Each section may also run a small spine of its own.
5. **Shots go wide, in, then wide.** Open on the establishing shot; go in for the parts; pull back to the opening
   framing at the end.
6. **Score tension honestly,** then read the column as a curve. Raise it with a problem or a deeper layer; release it
   with an answer. The peak comes late, then a clear release.
7. **Plant early, pay off late.** Every plant pays off; every payoff was planted.
8. **Write the words last,** 20 or fewer per row, after the picture already says most of it. Run the covered tests
   on the finished board: read the Words column alone, then read the Bright and Moves columns alone.

## What the checker enforces

`scripts/storyboard_check.py` reads the table and fails it when:
- a row has more than 20 words, or no Bright, or more than one thing moving;
- a row that is not a reaction lights more than one thing (`and`, `+` or a comma in Bright);
- the first shot is not `wide` or `extreme wide`, or the last shot is not the first shot again;
- no row is `close-up` or tighter (the story never goes in);
- three or more rows in a row share the same tension (a flat run), the peak is in the first third, or the last row
  is not below the peak;
- a beat of the spine is missing from the whole board;
- a plant has no later payoff, or a payoff has no earlier plant;
- there are fewer than 3 or more than 12 rows.

It also prints the tension curve as a small bar chart so you can see the shape.

## Worked example 1: Pixar's *Up* montage (the bar)

Four and a half minutes, a whole marriage, no words. Read it as the standard every board aims at.

Thesis: a shared dream survives everything except time.
World: one house and its neighbourhood · Verb: time passing · Thread: the savings jar.

| # | Beat | Shot | Bright | Moves | Words | Tension | Plant or payoff |
|---|---|---|---|---|---|---|---|
| 1 | character | wide | the couple at the altar | the loud side of the church cheers | none | 2 | plant: church |
| 2 | want | medium | the cloud shaped like a baby | the cloud changes shape | none | 2 | |
| 3 | obstacle | close-up | the doctor's face | she lowers her head | none | 4 | |
| 4 | action | medium | the savings jar | coins go in | none | 3 | plant: jar |
| 5 | obstacle | medium | the smashed jar | the jar breaks for the flat tyre | none | 4 | |
| 6 | action | close-up | Carl's tie | the tie is re-knotted, year after year | none | 3 | |
| 7 | outcome | close-up | the tickets in the picnic basket | Ellie cannot climb the hill | none | 5 | payoff: jar |
| 8 | reaction | wide | Carl alone in the church | nothing | none | 1 | payoff: church |

The last shot returns to the first place, changed: full circle. The thread (the jar) carries progress and setbacks.
The tie shows time by repetition. The hardest moment (the doctor) is told in two shots.

## Worked example 2: the Mauna Kea dive, re-told

Ash's four values, from The Range. The dive itself was loved; the summit's clicky stops were not. This is the dive
planned as a board.

Thesis: the more aware you are, the deeper you can see.
World: the ocean under Mauna Kea · Verb: dive · Thread: the searchlight's reach on the depth gauge.

| # | Beat | Shot | Bright | Moves | Words | Tension | Plant or payoff |
|---|---|---|---|---|---|---|---|
| 1 | character, want | extreme wide | the bathysphere on the surface | the sphere tips into the water | What drives me sits below the waterline. | 2 | plant: lamp |
| 2 | obstacle | wide | the narrow cone of light | the cable pays out | The more aware you are, the deeper you can see. | 3 | plant: gauge |
| 3 | action, outcome | medium | the fish school | the school turns as one | Goals. A school turns together, with no single leader. | 3 | |
| 4 | action, outcome | medium | the nautilus | it moves into its newest chamber | Identity. It lives in the newest chamber it built. | 4 | |
| 5 | action, outcome | close-up | the hermit crab | it steps into a bigger shell | Acquired values. A shell it found, not one it grew. | 4 | |
| 6 | obstacle, outcome | extreme close-up | the hotspot | the heat flares | Natural values. The heat that built the island. | 5 | |
| 7 | reaction | extreme wide | every part, lit together | nothing | The more aware you are, the deeper you can see. | 2 | payoff: lamp, payoff: gauge |

## Worked example 3: a proposal section

One ask from a fleet proposal (the Coastline build), as a small story inside a page. The host is
pitch-site-udyaan; the board sets what each screen of the pinned stage shows.

Thesis: one trip record replaces three logbooks.
World: the client's own truck, drawn in line · Verb: scroll the truck along its route · Thread: the trip record.

| # | Beat | Shot | Bright | Moves | Words | Tension | Plant or payoff |
|---|---|---|---|---|---|---|---|
| 1 | character, want | wide | the truck on the client's real route | the route draws on | "We need to know where every load is." | 2 | plant: record |
| 2 | obstacle | medium | the three paper logbooks in the cab | a page is copied by hand | Today each trip is written three times. | 3 | |
| 3 | obstacle | close-up | the late load's empty pin on the map | the three logbooks disagree | A late load: three logbooks, three answers. | 4 | |
| 4 | action | close-up | the driver tablet | one tap logs the stop | The driver logs it once. | 3 | |
| 5 | outcome | medium | the trip record | the record fills as the truck moves | Office, driver and client see the same record. | 2 | payoff: record |
| 6 | reaction | wide | the truck at the depot, route complete | nothing | One trip, one record. | 1 | |
