---
name: story-plan
description: "How do I turn an abstract idea into a story people watch? Turn any content into a visual story the reader watches instead of reads, then hand it to the skill that builds it. Finds the one-sentence thesis, casts abstract ideas as a living metaphor (one world, one creature or object per part, each backed by a real fact), and writes a storyboard (one row per screen with its story beat, shot size, the one bright thing, the one thing that moves, 20 words or fewer, a tension score, and plants and payoffs), checked by a script. Uses film craft (the covered tests, the story spine, the tension curve, where the eye goes, setup and payoff, full circle) with guardrails that keep names, numbers and the ask in plain words. Use whenever Ash says \"visual story\", \"visual storytelling\", \"tell it as a story\", \"show, don't tell\", \"make it a story, not a list\", \"visual metaphor\", \"mental model as a picture\", \"storyboard this\", \"it's too clicky\", \"too much information\", or wants values, a framework, a process, a pitch, a lesson or a personal map shown as a journey. Works with pitch-site-udyaan, brief-page-udyaan, polished-doc and course-lesson-udyaan, which build what it plans."
---

# Visual storytelling

This skill plans a story the reader can follow with their eyes. It does not build pages. It gives any building skill
a thesis, a world, and a storyboard that says, screen by screen, what is bright, what moves, which few words
appear and how tense the moment is. Words carry names, numbers, quotes and the ask; the picture carries everything
words would bloat. It codifies the Mauna Kea dive from The Range, which Ash loved, the parts of the same build he
called "clicky", "boring" and "garbage", and five films and video essays on visual storytelling he chose.

## What good looks like

Open these before planning, and copy their thinking:
- `references/storyboard.md`: three worked boards. Pixar's *Up* montage (the bar: a marriage in four and a half
  minutes, no words), the Mauna Kea dive re-told as seven shots, and one section of a fleet proposal.
- `assets/examples/range-src/`: the dive as built. Below the waterline is the model: four values found one by one as
  a fish school, a nautilus, a hermit crab and the Hawaiian hotspot. The numbered stops on the summit are the
  counter-example.
- `references/examples.md`: good and bad, side by side, each with the reason, from Ash's builds and the films.

Their shared qualities:
- **One sentence holds the story.** "The more aware you are, the deeper you can see." It opens the journey and
  returns at the end.
- **The picture holds the information.** "A visual metaphor can encompass so much detail." Each part is a creature
  or object whose real behaviour is the idea, so one line beside it is enough.
- **It is told, not clicked.** One forward motion (scroll or one control), one change per step, the earlier parts
  staying dimly visible so the picture builds.
- **The eye is led.** One bright thing per screen; wide to establish, close for the part that matters, wide again
  at the end.
- **It has a shape.** Tension rises to a late peak and releases; what was planted early pays off at the close; the
  last frame is the first one, changed.

## Workflow

### 1. Content, reader and host
Get what the story must carry (the facts, numbers, names, quotes, the ask), who will see it, and which skill builds
it: pitch-site-udyaan, brief-page-udyaan, polished-doc, course-lesson-udyaan, or a deck. Keep the facts in the host's
facts sheet; the story never invents one. If Ash is away, infer and log every assumption.

### 2. Thesis and shape
Write the thesis in one sentence. Then name the shape of the idea: depth (how far down you can see), growth over
time, a journey from A to B, before and after, borrowed against innate, moving together, exchange, balance. The shape
picks the world (`references/living-metaphors.md`, The method).

### 3. World, verb and thread
Concrete content uses the reader's own world: their truck, their campus, their day. An abstract idea with 3 to 6
parts that differ in kind becomes a living metaphor: run the five-point test and cast from the bank in
`references/living-metaphors.md`. Pick one verb for the reader (dive, climb, dig, sail, grow) and one thread: the
object that recurs and shows progress (the savings jar, the searchlight's reach, the trip record).

### 4. Storyboard
Write the board in the format in `references/storyboard.md`, one row per screen, using the craft in
`references/film-craft.md`. Then run:
```bash
python scripts/storyboard_check.py work/storyboard.md
```
Fix every failure. Read the printed tension curve: a flat run or an early peak is a story problem, not a layout one.

### 5. Covered tests, then play it back
Read the Words column alone: if it tells the whole story, the pictures are decoration; move a claim into a picture.
Read the Bright and Moves columns alone: they should show who, what changes and how it ends. Then show Ash the thesis,
the world and the board before anything is built. He reacts to what he sees; a board is cheap to change.

### 6. Hand it to the host
Follow `references/handoff.md` for what each host does with the board (a pinned stage, a scroll story, a sequence of
figures, a lesson). The host keeps its own rules for copy, design and QA.

### 7. Story review
After the host's first render, run the story reviewer in `references/review.md` on the screenshots as a background
agent (Sonnet is enough). It checks the board against what was built. Apply its fixes through the host skill.

### 8. Learn
When Ash reacts, add his words to `references/taste.md` (loved or rejected, with the reason) and, if a new device
or failure appears, to `references/examples.md`.

## Rules that are easy to get wrong

- **A story, not a set of buttons.** The Range's summit had eight numbered stops scattered over the scene: "still
  clicky, still too much information, still not like a story." The order is told; markers are shortcuts, never the
  way through; nothing is hidden for the reader to hunt.
- **A metaphor carries meaning or it goes.** Four values drawn as labelled rings were "such a boring way to show
  things." Every creature needs a real, checkable fact that maps onto the idea in one line. The mountain itself was
  pretty and said little.
- **Words carry what pictures cannot; pictures carry what words would bloat.** Names, numbers, quotes, the ask and
  the next step are always written plainly. A line that narrates its picture ("the truck reaches the depot") is cut;
  the line says what it means.
- **20 words or fewer per screen.** "Too much information" was the second complaint. The picture holds the rest.
- **One bright thing per screen.** Light, size, focus, leading lines and where figures face decide the first look.
  Two lit things fight.
- **Start wide, go in, end wide on the first frame, changed.** *Up* ends in the church where it began.
- **Act, then words.** The part moves first and its line writes after. Never delay the main point: the first screen
  says what this is about.
- **Nothing follows the pointer.** A glow that followed the cursor was "kind of garbage"; hover that glided was
  "not a fan of how smooth it is." Hover snaps; only moves between places ease.
- **Hidden extras are never needed.** Fixed lamps that light an easter egg at night were loved. Nothing the reader
  needs lives in them.
- **One world, one verb.** Mixing worlds turns a metaphor into clip art; two journeys on one page never share a verb.
- **Ash's own story stays his.** The Range's quotes and values never appear in client work; copy the mechanics.

## Files

- `references/film-craft.md`: the rules borrowed from cinema: the covered tests, the story spine, the opening, two layers, tension and rhythm, where the eye goes, devices from *Up* and *Better Call Saul*, clarity guardrails.
- `references/storyboard.md`: the board format, how to fill it, what the checker enforces, three worked boards.
- `references/living-metaphors.md`: showing an abstract idea as a world: the test, the method, story rules, a casting bank, vehicles and verbs, build mechanics for the dive, what failed.
- `references/handoff.md`: what each host skill does with the board.
- `references/examples.md`: good and bad side by side, with reasons.
- `references/taste.md`: Ash's verdicts on stories, in his words.
- `references/review.md`: the story reviewer prompt.
- `references/background/story-plan-videos.md`: cleaned notes on the five videos behind film-craft.md. The raw transcripts are in Shasta, `04 Make It Feel Right (UI-UX)/sources/`.
- `assets/examples/range-src/`: the Mauna Kea dive source (engine, panel, starter) and its README.
- `scripts/storyboard_check.py`: checks a board and prints its tension curve.
