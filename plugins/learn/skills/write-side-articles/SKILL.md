---
name: "write-side-articles (shasta)"
description: "How do I learn the side skills behind a note I wrote, as short articles I read later instead of a grilling? Turns up to five problems from the note into swipe decks, one artifact each, every one with its own colours, drawings and an Ask pane that answers in cards. Use when Ash says 'Articles:', 'send me articles', 'side-skill articles' or 'make it a deck'. Use teach-side-chat to learn live beside a build."
---

# Write side articles

Each problem in Ash's note becomes **one article, built as its own swipe deck**: one card per phone screen, a trail of four parts on top, an island at the bottom of every card that opens the Ask pane. **teach-side-chat owns how to teach** (the mechanism, the idea, the metaphor, the writing rules); `$SKILL_DIR/references/article-format.md` owns the deck's cards; `$SKILL_DIR/assets/deck-template.html` is the engine Ash approved (Fuji ticket 39, Nov 5 2026). The worked example is `references/example-culture.article.html`.

**Runs alone.** Ask Ash nothing; he reads the published decks.

**Paths.** `SKILL_DIR` is the folder holding this SKILL.md, wherever it's installed. `ASH` is the ash-skills plugins folder that holds every plugin side by side: `~/.claude/plugins/marketplaces/ash-skills/plugins` (on Ash's PC, `D:\ash-skills\plugins`). Run every command below with those full paths, from wherever you work (in Fuji, the Fuji folder), and write articles, decks and shots in the scratchpad.

**You write the copy, in this session, on the strongest model.** Subagents may fetch sources; they never write a card, and Haiku never writes copy (Ash, Nov 5).

## Steps

1. **Read the rules.** teach-side-chat's "How the idea and its metaphor are made" and "Writing rules" (`$ASH/learn/skills/teach-side-chat/SKILL.md`), `/write:match-ash-writing`, `/visualize:match-ash-design`, then `$SKILL_DIR/references/article-format.md` in full. Where teach-side-chat and article-format disagree, article-format wins for every card. Done when you can name the 15 card kinds in order.
2. **Read his note raw,** never editing it, and pick the problems: every one strong enough to teach its own idea, at most five (Ash, 2026-11-03). Done when each has a "How do you…" question that stands alone with the note hidden.
3. **For each problem, choose the idea by its mechanism, then a far field** (Ash, 2026-11-03: "always a far field").
   - **Mechanism first:** the problem's cause and effect, someone doing something ("the team copies what the founder rewards").
   - **Then a far field whose experts run that same cause and effect** under a named practice, sharing nothing with the problem's subject. Keep the name only if an expert there would explain it with that same cause and effect.
   - **Three worlds per deck:** the problem, the daily-life metaphor (the `why` card), and the far field (the `far` card). No deck reuses a far field or a metaphor scene (in Fuji: `python gear/articles.py worlds`).
   Done when every deck has its three worlds and a real name for the big concept.
4. **Give each deck its own look.** `python $ASH/visualize/skills/match-ash-design/scripts/palette.py --place dark --seed "<deck title>"`. If its number is one an earlier deck used (in Fuji: `python gear/articles.py combos`; elsewhere: this chat's decks), run it again with another seed. Pick `--island` and the four part colours from that combination (`article-format.md`, "The file you write"); if `build_deck.py` says two parts look alike, re-seed. Done when no two decks, this run or earlier, share a number.
5. **Write each article file** in the scratchpad as `<id>.article.html`, card by card in the order, from expert knowledge first. Draw every picture new, from the article's own world. Done when every card reads alone with the others hidden.
6. **Check facts after the draft, never before.** Cut any name, date or number the idea doesn't need, then look up the real facts left in primary or high-trust sources. A wrong fact is fixed or cut; research never adds cards or detail. Sources go in the answer card's folded `<details>`; who coined a term goes there too, never on a card. Done when every real fact has a source.
7. **Build and check in code.** `python $SKILL_DIR/scripts/build_deck.py <id>.article.html --out <id>.html --avoid <numbers> --avoid-worlds "<scenes and fields>"`, then `node $SKILL_DIR/scripts/deck_shots.js <id>.html <shots dir>` (Playwright is pre-installed in cloud sessions; on a laptop, `npm i -g playwright` once). Fix the article until both print nothing but "built" and "ok", then look at every shot yourself for what code can't see: a drawing that doesn't explain, a picture and its words that disagree, two things fighting for the eye. Done when both pass and the shots show none of those.
8. **Critic pass, then fix:**
   - **The metaphor check** from teach-side-chat on every `why` card. A metaphor that is the same activity in another job gets replaced.
   - **The copy scan** `python $ASH/visualize/skills/brief-page/scripts/scan_copy.py <id>.html`, fixing every hit in the cards except what belongs to brief pages: "usually" in the `wrong` card's fixed heading, the `data-pattern` line, a formula's brackets and the years in Sources.
   - **Read it as Ash on his phone:** hedging, a card that points back, a heading that isn't his question, a line he'd skip.
   Done when all three find nothing.
9. **Publish each deck as its own artifact:** file `<id>.html`, icon `book`, capabilities `{"sample": {}, "db": {}}` (the Ask pane talks to Claude; reaching the answer card saves `progress/read`). Then one `ArtifactData list` of collection `progress` on its URL, which should be empty. Done when every link opens.
10. **In Fuji, file each deck:** `python gear/articles.py add --name "<question>" --url <link> --topics "<topic>; metaphor: <scene>; far: <field>" --combo <N> --excite <1-10>` (excite: how much Ash will want to open it, your judgment against what's unread), log to `ranges/learning/shasta` with `gear/log.py`, `python gear/check-maps.py`, commit to `main` (a run without Ash ends the message with `Fuji-Run: side-skill articles`), push. The daily runs place the reading session and refresh the reading list (`gear/articles.md`); a session never calls Google Calendar. Done when every deck is under Unread.
11. **Reply** with one line per deck: its question, its link, its metaphor. In Fuji, tag the session `next: read side-skill articles (parked YYYY-MM-DD HH:MM)`, India time. Done when the reply is sent.

## Files

- `references/article-format.md`: the article file, the card order, how each card is written, the visual weights, the drawings. Open on every run.
- `references/example-culture.article.html` and `references/example-money.article.html`: two whole articles that pass every check, one on a team habit and one on a finance concept with numbers.
- `assets/deck-template.html`: the engine. Change it only to change every deck; its Ask prompts read `world`, `expert`, `reader` and `asker` from each article.
- `scripts/build_deck.py`: puts an article into the engine and checks the rules code can check.
- `scripts/deck_shots.js`: screenshots every card at 390 by 844 and reports scroll, overlap with the island, tiny or cut-off text.
