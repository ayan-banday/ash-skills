---
name: "write-side-articles (shasta)"
description: "How do I learn the side skills behind a note I wrote, as short articles I read later instead of a grilling? Runs teach-side-chat's chapter on up to five problems from the note, each teaching one idea from a far field with a metaphor I'll remember, on one phone page. Use when Ash says 'Articles:', 'send me articles' or 'side-skill articles'. Use teach-side-chat to learn live beside a build."
---

# Write side articles

A thin wrapper around `/learn:teach-side-chat`. **teach-side-chat owns how to teach:** the chapter shape, the idea, the metaphor and the writing rules. This skill picks the problems from a note, runs that chapter once per problem, and puts the chapters on one page. Set One is the approved result: `references/example-set-one.html` (https://claude.ai/artifact/CHTmK8XgKcUodMic31r1Lh).

**Runs alone.** Ask Ash nothing; he reviews the published set.

## Steps

1. **Read teach-side-chat in full** (`../teach-side-chat/SKILL.md`, with `references/example-chapter.md`), then match-ash-writing and match-ash-design as it says. Done when you can say teach-side-chat's "How the idea and its metaphor are made" steps from memory.
2. **Read his note raw,** never editing it, and pick the problems: every one strong enough to teach its own idea, at most five (Ash, 2026-11-03). Order them as teach-side-chat's menu does. Done when each has a "How do you…" title that stands alone with the note hidden.
3. **For each problem, choose an idea from a far field** (Ash, 2026-11-03: "always a far field"). Name the field the problem sits in, then take the idea from a field nothing like it: a body-language problem gets its idea from sport, music or medicine, never theatre or public speaking. The far field supplies three things: **the idea, its name** (a real term that field uses, like andon or ready position, never a coaching phrase made up for the article) **and the "Far away" example.** The metaphor still comes from daily life, a third world. No two articles share a field. Done when every idea has a real name from a field that differs from its problem's field and from the other ideas'.
4. **Write each article as teach-side-chat's chapter (its step 2), from expert knowledge first.** Teach before you research: find the mechanism, write the idea sentence, build the metaphor, all by teach-side-chat. Close each article with "Other questions" codes as its menu does, gathered on the page's last section.
5. **Check facts after the draft, never before.** Look up only the real numbers, names, dates and quotes the draft already uses, in primary or high-trust sources. A fact that turns out wrong gets fixed or cut; the research never adds sections, findings or detail to the teaching. Sources go in a folded `<details>` at the end. Material of Ash's own (a clip, a score, a draft) goes in only where his note asks for it, and in "Where you are now" or "In your world", never in place of the idea. Done when every real fact has a source and the teaching sections read the same as before the check.
6. **Build one page on the example's layout,** phone first: dark, one Wada combination from match-ash-design's `palette.py --place dark --seed "<set name>"` (a different number from the last set's CSS comment), an index of the set (question, idea, metaphor), one tab per article routed on `#hash`, at most one picture per article where it explains faster than words (SVG, 360-wide viewBox). Done when every article opens from its tab.
7. **Critic pass:**
   - **The metaphor check** from teach-side-chat ("How the idea and its metaphor are made", its done test) on every article. A metaphor that is the same activity in another job gets replaced.
   - **The copy scan** `../../../visualize/skills/brief-page/scripts/scan_copy.py`, fixing every hit except the chapter's fixed headings.
   - **Screenshots** of each tab at 390 by 844 with Playwright, fixing tiny labels, overlaps and sideways scroll.
   Done when all three find nothing.
8. **Publish** as a claude.ai artifact, icon `book`, titled "Side Skills, Set N" with N in digits: in Fuji, one more than the last set in `gear/articles.md`; elsewhere, one more than the last in this chat. Done when the link opens.
9. **In Fuji, file it:** the library steps in `gear/articles.md`, log to `ranges/learning/shasta` with `gear/log.py`, `python gear/check-maps.py`, commit to `main` (a run without Ash ends the message with `Fuji-Run: side-skill articles`), push. Done when the set is under Unread and its reading block is placed.
10. **Reply** with the link and one line per article: the idea and its metaphor. In Fuji, tag the session `next: review side-skill articles (parked YYYY-MM-DD HH:MM)`, India time. Done when the reply is sent.
