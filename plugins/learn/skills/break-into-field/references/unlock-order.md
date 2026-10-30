# The unlock order: what waits on what

Ash's organising principle (Oct 30 2026): "You cannot design the UI of an app if you've not defined what it's supposed to be. Some problems run in parallel, some only after the previous one." It orders chapters in a book, tickets in a phase and phases in a project, with one question.

**The question, asked of every problem:** "What has to be solved before this can be solved?"

## The rules

1. **Every problem lists what it waits on.** In Fuji that is the ticket's `Blocked by` line. In a book it is an arrow on the problem map.
2. **A problem that waits on nothing is open.** Open problems can run in parallel. The Wayfinder calls them the frontier.
3. **Layers are phases.** Everything open now is layer 1. What layer 1 unlocks is layer 2, and so on. A phase is one layer, so phases are cut by the map, never by feel.
4. **The first chapter, ticket or phase is the open problem the most others wait on.** Count the arrows out of each open problem; the biggest count goes first.
5. **A chapter ends by naming what it unlocked:** the problems now open because this one is solved.
6. **Some problems are the same size as a ticket, some as a phase.** The rule is the same at every size. A problem too big to answer in one chapter is split, and its pieces get their own arrows.

## Drawing it

- The outcome at the top, named as a problem.
- Groups of at most four problems under it, with a plain name each (students find it and enjoy using it; it remembers what students share; it thinks and acts for us; the team builds it together).
- A line from each problem to the ones that wait on it. Open problems are marked. Every chapter is marked with its number.
- The ideas he'll pick up sit on the problem that teaches them, in small type, never in a separate table.
- **Drawn as a moving map,** by `moving-map.md`: a motif that draws itself on, layer by layer, as he scrolls.

## Choosing the next chapters

After each chapter, recount on the arrows that remain: every problem whose waits are all solved is open. **The next chapter is the open problem the most others wait on.** On a tie, take the one that fully opens more problems (those that wait on nothing else); then the one closer to the book's spine.

## The technology map, every arrow

IDs are for this file and the map's code only; chapters use the plain names.

| Problem | Waits on |
|---|---|
| A1 one simple dashboard a student opens every day | nothing (open) |
| B1 students hand in work on the site | nothing (open) |
| D1 people and agents change the site without breaking it | nothing (open) |
| D2 where the site runs, and what it costs at 10× | nothing (open) |
| A2 seeing which day students stop | B1 |
| A3 the site works on a cheap phone on hostel wifi | A1 |
| A4 a new student starts without a call | A1 |
| B2 finding Week 2 work again in Week 6 | B1 |
| B3 anonymous reflections that stay anonymous | B1 |
| B4 one record of each student across every tool | B1 |
| C1 the course answers from its own lessons | B1 |
| C2 an agent drafts feedback on every hand-in overnight | B1 |
| D3 each person sees only what they should | B1 |
| C3 outreach and onboarding messages go out on their own | A2, B4 |
| C4 knowing the AI's answers are right | C1, C2 |
| D4 where software stops and leadership takes over | C2 |

**Layers:** open now A1, B1, D1, D2. Opens next A2, A3, A4, B2, B3, B4, C1, C2, D3. Opens last C3, C4, D4.
**Chapters so far:** 1 is B1 (seven wait on it). After B1, A1 and C2 tie at two each; A1 fully opens two (A3, A4) and C2 fully opens one (D4), so 2 is A1 and 3 is C2. After those, the open problems with someone waiting are A2, B4 (C3) and C1 (C4); C1 fully opens C4, so 4 is C1.
The arrows A1 → A3, A4; B1 → B4; A2, B4 → C3; C2 → D4 were inferred by the v2 build and are Ash's to confirm.

## What Fuji changes

- `Blocked by` on every ticket already carries the arrows. Phases should be cut from the layers: a phase holds the tickets that are open together.
- `gear/check-maps.py` could draw the layers from `Blocked by` with no AI. Not built yet; a candidate for a Fuji ticket.
