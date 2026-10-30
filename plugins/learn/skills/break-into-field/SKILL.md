---
name: "break-into-field (shasta)"
description: "How do I break into a whole field I know nothing about, like technology or finance, starting from a real problem in my work? Grills the field's outcome, then builds a Shasta study book: a problem map ordered by what waits on what, the field's shelves, and chapters that each solve one problem, checked by a critic before Ash sees them. Use when Ash says 'break into', 'build the map for', 'the technology book' or 'study a whole field'. Use learn:study for one topic or one study page."
---

# Break into a field

Build a study book that takes Ash from "I don't know what I don't know" to seeing which problems in his work the field can solve, and briefing Claude to build the answer. Technology was the first field (Fuji ticket 34, Oct 30 2026). The rules below came from Ash's feedback on that first version, so follow them over your own taste.

**Shasta's rules still hold** (`CLAUDE.md` and `_rules/Clusters.md` in the Shasta repo). Where this skill is more specific, it wins: a book is not one study page, so the page checker's shape rules don't apply to it.

## Steps

1. **Grill before any map.** Follow `references/grilling.md`. Done when Ash has said yes to: the outcome in his own words, the one real project that is the book's spine, the field's shelves, and the sources. Save the decisions to the ticket, never his words.
2. **Draw the problem map.** Follow `references/unlock-order.md`. Done when every problem names what it waits on, the open problems are marked, and the first chapter is the open problem the most others wait on.
3. **Draw the shelves.** Follow "The shelves" in `references/book-shape.md`. Done when each shelf has its fields, each field has its words and one problem from Ash's world, and the shelves he hasn't touched carry suggested problems.
4. **Research only what the next chapter needs.** Follow `references/research.md`. Done when the brief's questions each have the one best source, read by cheap agents that return exact quotes with context.
5. **Write the chapter as markdown first.** Follow the chapter skeleton in `references/book-shape.md` and every rule in `references/writing-rules.md`. Run `python scripts/check_chapter.py <file.md>`. Done when it prints no FAIL.
6. **Run the critic.** Follow `references/critic.md`: one fresh agent reads the markdown as Ash and checks it against the writing rules. Fix, rerun, at most three rounds. Done when the critic's answer to the chapter's question matches the chapter's own answer and no rule fails.
7. **Only then build the HTML** by `references/look.md`, publish it as a private artifact, and check it at desktop width only. Ash doesn't study on a phone. Done when the page renders and the artifact link is in the ticket.
8. **Close the session by Fuji's rule book:** save Building progress to the ticket, log, `python gear/check-maps.py`, the timeline note, commit and push. Add one line to Shasta's `study log.md`.

## Where things live

- **The book's HTML:** Shasta, `<Area>/books/<Book title>.html`, plus the artifact link in the Fuji ticket.
- **Research findings:** Fuji, `ranges/self/build-fuji/research/<ticket>-<field>-sources.md`, one file per field, grown by each chapter.
- **The grilling's decisions:** the Fuji ticket's Answer. The field's book gets one ticket per chapter once the map exists, ordered by the unlock order.

## Reference

- `references/grilling.md`: the questions to ask before a map, and what "ready" means.
- `references/book-shape.md`: the book's parts in order, and the chapter skeleton with heading wording.
- `references/writing-rules.md`: how Ash wants to be taught. A to B, the plain sentence before the metaphor, no quotes, outcomes in business terms, the answer with the words embedded.
- `references/unlock-order.md`: what waits on what; how it orders chapters, phases and tickets.
- `references/research.md`: the source pipeline, cheap.
- `references/critic.md`: the critic agent's prompt and the cheap markdown test.
- `references/look.md`: the look, from Shasta's palettes, kept simpler, checked on desktop only.
- `scripts/check_chapter.py`: the mechanical check on a markdown chapter.
