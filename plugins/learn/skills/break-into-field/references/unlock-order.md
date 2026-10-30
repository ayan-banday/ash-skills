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
- An arrow from each problem to the ones that wait on it. Open problems are marked. The first chapter is marked.
- The ideas he'll pick up sit on the branch of the problem that teaches them, in small type, never in a separate table.

## The technology map, as an example

Open now: one simple dashboard (A1), students hand in work on the site (B1), two people change the site without clashing (D1), where the site runs (D2).
B1 unlocks: seeing which day students stop (A2), finding Week 2 work in Week 6 (B2), the course answering from its lessons (C1), an agent drafting feedback (C2), anonymous reflections (B3), logins and roles (D3).
So B1 is chapter 1. A2 and B2 and C1 are layer 2. Knowing the AI is right (C4) waits on C1 and C2, so it is layer 3.

## What Fuji changes

- `Blocked by` on every ticket already carries the arrows. Phases should be cut from the layers: a phase holds the tickets that are open together.
- `gear/check-maps.py` could draw the layers from `Blocked by` with no AI. Not built yet; a candidate for a Fuji ticket.
