---
name: "write-side-articles (shasta)"
description: "How do I learn the side skills behind a note I wrote, as short articles I read later instead of a grilling? Picks one to five problems from the note and publishes one phone page of chapters, each teaching one named idea from another field with a metaphor I'll remember. Use when Ash says 'Articles:', 'send me articles' or 'side-skill articles'. Use teach-side-chat to learn live beside a build."
---

# Write side articles

Ash writes a note (a reflection, an Asana task, a chat message) about what he's building and reading. This skill turns it into a set of short articles that each add **a new dot**: one named idea from a field he hasn't studied, with a daily-life metaphor he can retell (Ash, 2026-11-03: "send me articles that teach me the side skills without the grilling"; "category-defining"; "I want to create more dots"). Set One is the approved example: `references/example-set-one.html`, published at https://claude.ai/artifact/CHTmK8XgKcUodMic31r1Lh.

**Runs alone.** Ask Ash nothing; he reviews the published set.

## Steps

1. **Read the three skills it builds on:** `../teach-side-chat/SKILL.md` with its `references/example-chapter.md` (the chapter shape), `../../../write/skills/match-ash-writing/` with `references/writing.md`, and `../../../visualize/skills/match-ash-design/` with `references/design.md`. Then skim `references/example-set-one.html` for the page. Done when all are read.
2. **Read his note raw,** never editing it. Pull out every problem he's wrestling with, in his words. Done when you can name each in one line.
3. **Pick the problems yourself, one to five** (Ash, 2026-11-03: "any number of articles but not more than five"). Take every problem strong enough to teach its own new idea; an aside that overlaps another problem joins it. Stop at five. Order: the one he says he most wants first, then the rest by unlock order. Each article gets a "How do you…" title that stands alone with the note hidden, plus two more questions of its own for "Other questions". Done when every title makes sense to a stranger.
4. **Choose one named idea per problem from a field he hasn't studied.** It adds to what he worked out and never restates it (he knew self-determination theory, so culture got Schein's embedding mechanisms). Each idea gets:
   - **a daily-life metaphor** he can retell in one sentence (a worn path across a lawn; flatmates sharing a kitchen; a bus stop cord),
   - **a far-away real example** from a different world than the metaphor (NUMMI, Germany 1990, the WHO surgical checklist),
   - **an "in your world" example** from Udyaan, Fuji, Shasta or the micro-SaaS with Mohit.
   Done when no two ideas share a field, no field is one the note already names, and every idea has all three.
5. **Check facts against primary or high-trust sources.** His asking for articles is his say-so for this research. Use the original book or paper, HBR, MIT Sloan, NEJM, Britannica, official pages. Every real number, date, person and company has a source; invented people and scenes go in a "made up" line under each article. Done when nothing real lacks a source.
6. **Write each article in the teach-side-chat chapter shape,** about 1,000 to 1,300 words, by match-ash-writing: lists of 3 at most, no dashes, meaning before name, three new names at most. Sources fold into `<details>` at the end. Done when every article has every section.
7. **Draw at most one picture per article, only where it explains faster than words** (a loop, a grid, a timeline). SVG at a 360-wide viewBox so labels read on a phone; every colour a token. Done when each picture passes match-ash-design's two covered tests.
8. **Build one page, phone first,** on the example's layout: dark, Overpass / Atkinson Hyperlegible / Overpass Mono, one Wada combination from match-ash-design's `palette.py --place dark --seed "<set name>"` (a different number from the one in the last set's CSS comment; Set One was No. 232), an index of the set (question, idea, metaphor), a sticky tab bar with one tab per article routed on `#hash`, and "Other questions" at the bottom. Done when every article opens from its tab.
9. **Critic pass:** run `../../../visualize/skills/brief-page/scripts/scan_copy.py` and fix every hit except the chapter's fixed headings; screenshot each tab at 390 by 844 with Playwright and fix tiny labels, overlaps and sideways scroll; then "Read it as Ash" from writing.md. Done when the scan is clean and the screenshots show nothing to fix.
10. **Publish** as a claude.ai artifact, icon `book`, titled "Side Skills, Set N" with N in digits: in Fuji, one more than the last set in `gear/articles.md`; elsewhere, one more than the last set in this chat. Done when the link opens.
11. **In Fuji, file it:** follow the library steps in `gear/articles.md`, log to `ranges/learning/shasta` with `gear/log.py`, run `python gear/check-maps.py`, commit to `main` (a run without Ash ends the message with `Fuji-Run: side-skill articles`) and push. Done when the set is under Unread and its reading block is placed.
12. **Reply** with the link and one line per article: the idea and its metaphor. In Fuji, tag the session `next: review side-skill articles (parked YYYY-MM-DD HH:MM)`, India time. Done when the reply is sent.
