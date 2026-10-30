# Research, cheap

The aim is how the field's experts think: philosophies, mental models, first principles and the reasoning behind them. Not tools, never syntax.

## Steps

1. **Write a brief for the chapter** before any reading: the reader, the chapter's problem, four to six numbered questions the chapter needs answered, and the output format. One paragraph each. The brief is what every reader agent gets.
2. **Pick the best source per question,** never a ranked list of people. Some people are best for philosophy (for AI: Karpathy, Matt Pocock), some for the practical side (Greg Isenberg for sites), some for the basics (CS50), some for product thinking (Lenny). Ask: who has thought hardest about this exact question?
3. **Grep the field's findings file before any reading.** Shasta, beside the field's book: `<area>\books\<book title> findings.md` (technology: `03 Build Software (Computer Science)\books\Breaking Into Technology findings.md`; moved from Fuji on Oct 30 2026). What it already answers is never read again. Its shape and the one-line rule for appending are in Shasta's `_rules/Menus and Learning Briefs.md`, "Findings files".
4. **Text first, saved once.** A source is fetched by the chain in Shasta's `_rules/Taking In Sources.md` (Firecrawl's YouTube transcript, a text transcript page, the laptop script, or stop) and saved in Shasta with a summary and an index of two-minute blocks. That save is the only full read it ever gets. Never guess what a video says.
5. **One cheap reader per angle, not per person, reading index first.** Each Haiku agent (model `haiku`) gets the brief, one angle (philosophy, agents, practice) and the `## Index` of its sources, picks blocks from the index, prints only those (`transcript.py show`), and returns findings in the file's shape: question number, the idea in one plain line, the exact quote, one line of context, the source with `[mm:ss]`. No summaries. A different angle per reader is how an idea is paid for once.
6. **Later readers report only what's new** against the findings file.
   - A suggestion, not a rule: when a question needs only a handful of blocks, the main chat opens them with `transcript.py show` instead of starting a 55k-token agent. Agents are for reading across many blocks or sources. (Shasta's `_rules/Menus and Learning Briefs.md`, "Reading transcripts".)
7. **Sonnet only to combine,** when a chapter needs synthesis notes. The main chat never reads a transcript.
8. **Append the findings** to the field's file under the chapter's brief. Grow the file; never rewrite old findings.

## What the chapter takes from the findings

- The plain idea and its reasoning, rewritten in Ash's words. The quote stays in the research file, not in the chapter, unless it is the clearest sentence available.
- The source goes under the book's Sources, nowhere else.

## From the first run (technology, Oct 30 2026)

Readers: Karpathy (context, the LLM wiki), Pocock and Alexis King ("parse, don't validate"), CS50 Week 7, Lenny's Newsletter. Codd 1970 added for the why. Four readers, about 115k tokens each, gave 47 findings, of which the chapter used about ten. Next time: fewer readers with sharper angles, and skip the history reader unless the chapter needs the why in more than one line. Since then (Oct 30, Fuji ticket 14): sources are indexed once in Shasta and readers open only the blocks they need; the measured saving is in that ticket.
