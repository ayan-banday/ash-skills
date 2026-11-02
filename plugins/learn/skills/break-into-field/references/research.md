# Research, cheap

The aim is how the field's experts think: philosophies, mental models, first principles and the reasoning behind them. Not tools, never syntax.

## Steps

The pipeline is Shasta's "A research run" in `_rules/Taking In Sources.md` (any field, any project). For a book it runs like this:

1. **Write a brief for the chapter** before any reading: the reader, the chapter's problem, four to six numbered questions the chapter needs answered, and the output format. One paragraph each. The brief is what every agent gets.
2. **Check in, then pick sources yourself.** Ash approves the outcome, the problems and the trusted channels or people (in the grilling, or in answers he gives up front). Within those, the run picks the best source per question by its own judgment; a source outside them waits for his yes. Never a ranked list of people: ask who has thought hardest about this exact question.
3. **Grep before fetching.** The field's findings file (Shasta, beside the field's book: `<area>ooks\<book title> findings.md`) and the areas' `Sources Index.md` files. What they already answer or hold is never fetched or read again.
4. **Scout, then fetch, with Haiku agents only.** One scout lists two or three candidate videos per question from the trusted channels. Fetchers (5 or 6 videos each) save the transcript in full through TubeLab first (the chain in `Taking In Sources.md`), and write the index plus three "What it's about" lines in that same read. The main chat never calls TubeLab: short transcripts come back inline into whoever called.
5. **One reader per question, index first.** Each Haiku agent (model `haiku`) gets the brief, its question and the `## Index` of its sources, picks blocks from the index, prints only those (`transcript.py show`), and returns findings in the file's shape: question number, the idea in one plain line, the exact quote, one line of context, the source with `[mm:ss]`. No summaries.
6. **Later readers report only what's new** against the findings file.
   - A suggestion, not a rule: when a question needs only a handful of blocks, the main chat opens them with `transcript.py show` instead of starting a 55k-token agent.
7. **Sonnet only to combine,** when a chapter needs synthesis notes. The main chat reads findings and indexes, never a whole transcript.
8. **Append the findings** to the field's file under the chapter's brief. Grow the file; never rewrite old findings.

## What the chapter takes from the findings

- The plain idea and its reasoning, rewritten in Ash's words. The quote stays in the research file, not in the chapter, unless it is the clearest sentence available.
- The source goes under the book's Sources, nowhere else.

## From the first run (technology, Oct 30 2026)

Readers: Karpathy (context, the LLM wiki), Pocock and Alexis King ("parse, don't validate"), CS50 Week 7, Lenny's Newsletter. Codd 1970 added for the why. Four readers, about 115k tokens each, gave 47 findings, of which the chapter used about ten. Next time: fewer readers with sharper angles, and skip the history reader unless the chapter needs the why in more than one line. Since then (Oct 30, Fuji ticket 14): sources are indexed once in Shasta and readers open only the blocks they need; the measured saving is in that ticket.
