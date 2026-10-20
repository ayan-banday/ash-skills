# Visuals

A visual earns its place when the content has a shape and a reader gets the point faster from the picture than from the sentence. This file covers when to draw, the twelve visuals in three groups, how to draw stick figures, and what bad looks like.

## Contents
- The test, and when to keep the words
- Pick a visual: two questions
- Group A: People and situations (scene, story strip, contrast pair, hub)
- Group B: Steps, time, and action (flow, timeline, stairs, decision box)
- Group C: Amounts and choices (dot split, funnel, bars, matrix)
- Drawing stick figures
- Sketch style or chart style
- Sizing and placement on the page
- Bad visuals

All markup lives in `assets/reference-playbook.html` (Part 5 has every visual, numbered 5.1 to 5.12) and the common ones in `assets/template.html`. Copy the markup and change the content.

## The test, and when to keep the words

**Draw it** when the content has a shape: people and forces, steps in order, time, a share, a narrowing, two factors, one centre with many parts.

**Keep the words when:**
- **A short story already works.** Two good sentences about a customer beat a drawing of them.
- **There is one number.** Bold it inside the sentence.
- **The picture would only decorate.** Every shape must stand for something the text says.
- **The reader needs to look things up.** Use a table.
- **The document is short** (a one-page memo). Add a visual only if it carries the main point.

A document can have zero visuals. A demo memo in this skill's examples gets none, and that is correct.

## Pick a visual: two questions

**First question: what is the content about?** People and situations, steps and time, or amounts and choices.

| People and situations | Steps, time, and action | Amounts and choices |
|---|---|---|
| One person, many pressures? **Scene** | Order, with one slow step? **Flow** | A share of a small group? **Dot split** |
| A mistake that unfolds? **Story strip** | Dates or durations? **Timeline** | A group that narrows? **Funnel** |
| Two cases, one difference? **Contrast pair** | Levels that build? **Stairs** | Two or three amounts? **Bars** |
| One thing, many parts? **Hub** | One thing to do, by a date? **Decision box** | Two factors at once? **Matrix** |

## Group A: People and situations

Drawn as stick-figure sketches with hand-lettered labels.

**Scene** (5.1). Use when the reader needs to picture a person and the forces on them. Skip when a name and a role say enough. Example: a team lead pulled three ways by email, chat, and calls. One figure in the middle, three icons around, dashed lines to each.

**Story strip** (5.2). Use when a mistake unfolds in steps and the last step costs something. Skip when nothing is lost. Example: writer, then a 40-page report, then grey readers with a red "?" and "Readers stop at page 2". Three panels joined by arrows, the cost in the alert colour.

**Contrast pair** (5.3). Use when two cases look alike and one detail decides the outcome. Skip when they differ in many ways. Example: two clinics with the same late lab results; one wants a second clinic and would pay, one wants to stay small and won't. Two identical sketches side by side, one changed element, a "Would pay" or "Won't pay" pill, and two sentences under each.

**Hub** (5.4). Use when one thing touches many parts. Skip when the parts form a chain (use a flow). Example: a proposal in the centre, five sign-off teams around it. Five or six satellites at most; one may be in the ok colour if it is special (the client).

## Group B: Steps, time, and action

**Flow** (5.5). Use when order matters and one step causes the trouble. Skip when there are two steps or every step is fine. Built from HTML chips (`.flow .st`), not SVG, so it wraps on narrow pages. Mark the slow step `.hot` with a small label ("Up to 7 days"), the good result `.key`. A "Today / Proposed" pair shows the fix.

**Timeline** (5.6). Use when dates or durations carry the point. Skip when only order matters. A small Gantt: rows for activities, week columns, bars in primary, the lost time as a dashed alert-tinted bar labelled in words ("Waiting, nothing moves"), the launch as an accent marker.

**Stairs** (5.7). Use when levels build on each other. Skip when items can happen in any order. Four steps rising left to right with a short label on each tread and a figure on the bottom step. Keep labels short enough to fit the tread without touching the riser.

**Decision box** (5.8). Use once, at the end, when the reader must decide or act by a date. Skip when nothing is asked. A filled primary box: the action and date as the heading ("Approve the rota by Friday 23 October"), then what happens if they say yes and what to reply if they want a change.

## Group C: Amounts and choices

Drawn as clean charts with plain labels.

**Dot split** (5.9). Use when a share is the point and the group is small enough to count (under about 60). Skip for thousands. One dot per person, filled dots in primary, a big number beside it ("12 of 40") and one line of meaning.

**Funnel** (5.10). Use when a group narrows through stages. Centred bars whose width is proportional to the count, labels on the left, numbers on the right, the last stage in accent. Caption says what width means. Never draw a decorative funnel shape with made-up proportions.

**Bars** (5.11). Use when two or three amounts are the point. One bar per amount, the value written inside or beside it. The new or better amount in primary, the old one in grey.

**Matrix** (5.12). Use when items differ on two traits at once. A 2x2 with named axes ("More effort", "More impact"), quadrant names that say what to do ("Do first", "Skip"), dots with labels placed next to their dot. Tint only the best quadrant.

## Drawing stick figures

The figures are SVG symbols defined once at the top of the template (`#fig`, `#fig-up` arms raised, `#fig-hold` holding something). Place them with `<use href="#fig-hold" class="ink" x y width="40" height="90"/>`.

- **Lines:** `class="ln"` (ink, 3px, round caps). Add `soft` for grey, `red` for alert, `green` for ok, `blue` for primary, `dash` for dashed, `thin` for 2px.
- **Fills:** `fp` paper white (to sit on top of lines), `fr` alert, `fg` ok.
- **Ghost figures** (people who are absent, uninterested, or imagined): `<use class="ghost" ...>`.
- **Ground line** under every scene: `<line class="ln soft" ...>`.
- **Labels** under each element, centred, one to three words, in the hand font. The cost or problem label in `class="red"`; the good outcome in `class="green"`.
- **Icons** are drawn from simple shapes: an envelope is a rectangle plus a V; a house is a triangle on a square; a clinic adds a cross; a report stack is three offset rectangles with grey lines; a phone is a tall rounded rectangle.
- **One idea per sketch.** If a sketch needs a paragraph to explain, it is two sketches or none.
- Every sketch gets `role="img"` and an `aria-label` that says in words what it shows.

## Sketch style or chart style

- **Sketch style** (white panel `.sk`, hand-lettered labels): people, stories, situations, mind maps, stairs, hubs.
- **Chart style** (white panel `.panel`, the body font): amounts, timelines, flows, matrices, tables.
- The mix tells the reader at a glance whether they are looking at an idea or at data. A page can hold one of each.
- For a formal document (legal, finance, board pack), the user may ask for chart style everywhere; then use the body font in sketches too.

## Sizing and placement on the page

- A figure sits right after the paragraph that introduces it, never pages away.
- Figures never split (`break-inside: avoid` is on `figure`). Size them so they fit in the space they need: if a figure would leave a third of a page empty above it, shrink it (cap the SVG with `style="max-width:500px;margin:0 auto"`) or move a paragraph after it.
- Number figures by part (2.1, 2.2) only when the document has numbered parts. Captions say what to notice, not what the figure is.
- Text inside SVG stays short. Longer explanations go in HTML beside or below the figure.

## Bad visuals

- **Decorative charts** with invented numbers. If the writer gave no numbers, the visual shows a shape with words, or the content stays text.
- **A visual per section** out of habit. This skill draws only where it helps.
- **Labels cut off** at the SVG edge or overlapping lines. Widen the viewBox or shorten the label.
- **Labels far from their dot** in a matrix. Place each label beside its own mark.
- **Colour as the only signal.** The slow step is red and says "Up to 7 days".
- **Emoji, icon fonts, gradients, 3D, drop shadows.**
- **Two figures that show the same thing.**
