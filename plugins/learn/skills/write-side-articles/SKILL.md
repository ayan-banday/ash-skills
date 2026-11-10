---
name: "write-side-articles (shasta)"
description: "How do I turn what I just read or thought through into one article I can read in the same sitting? Turns a brain dump or note into one swipe deck built on the one insight that makes all its questions easy, with its own colours, drawings and an Ask pane, and posts the link in minutes while a critic polishes it in the background. Use when Ash says 'Articles:', 'send me an article', 'side-skill articles', 'make it a deck', or brain-dumps what he learned from a book, a video or a study. Use teach-side-chat to learn live beside a build."
---

# Write side articles

Ash's note becomes **one article, built as one swipe deck**: one card per phone screen, a trail of four parts on top, an island at the bottom of every card that opens the Ask pane. **teach-side-chat owns how to teach** (the mechanism, the idea, the metaphor, the writing rules); `$SKILL_DIR/references/article-format.md` owns the deck's cards; `$SKILL_DIR/assets/deck-template.html` is the engine Ash approved (Fuji ticket 39, Nov 5 2026). The worked examples are the two in `references/` (step 1).

**Fast, and the first draft is the good one** (Ash, 2026-11-10). He reads the deck in the same sitting he wrote the note, while he still cares, so the link reaches him in minutes. Speed comes from cutting waiting, never from cutting the copy: one deck, the rules read in one go, checks in code, and the critic running after the link. Quality wins over a minute saved.

**Runs alone.** Ask Ash nothing; he reads the published deck.

**Paths.** `SKILL_DIR` is the folder holding this SKILL.md, wherever it's installed. `ASH` is the ash-skills plugins folder that holds every plugin side by side: `~/.claude/plugins/marketplaces/ash-skills/plugins` (on Ash's PC, `D:\ash-skills\plugins`). Run every command below with those full paths, from wherever you work (in Fuji, the Fuji folder), and write articles and decks in the scratchpad.

**You write the copy, in this session, on the strongest model.** Subagents may check facts and critique; they never write a card, and Haiku never writes copy (Ash, Nov 5).

## Steps

1. **Read the rules in one command,** in full, never from a summary, with the example nearest the topic (`example-culture` for people and teams, `example-money` for numbers):
   ```bash
   cat $ASH/learn/skills/teach-side-chat/SKILL.md $ASH/write/skills/match-ash-writing/SKILL.md $ASH/write/skills/match-ash-writing/references/writing.md $ASH/visualize/skills/match-ash-design/SKILL.md $SKILL_DIR/references/article-format.md $SKILL_DIR/references/weak-spots.md $SKILL_DIR/references/example-culture.article.html
   ```
   If the output spills to a file, Read that file whole in one call. From teach-side-chat, use only "How the idea and its metaphor are made" and "Writing rules"; skip its menu, its pick and its "Want it?", since this skill asks Ash nothing. Where teach-side-chat and article-format disagree, article-format wins for every card. Done when you can name the 15 card kinds in order and the weak spots.
2. **Read his note raw, never editing it, and find its one insight:** the chunk that, once Ash gets it, makes every question in the note easy (Ash, 2026-11-10). The deck's question asks for that chunk. The note is context, not content: it tells you where he is and what he's trying to solve. Every question that hangs from the insight gets answered inside the cards where it serves it. Choose details for the message; never cover the note line by line or summarise it back. Where his thinking is rough, write his best version as the starting point. A topic that doesn't hang from the insight is left out and named in the reply in one line. **Write two things in the scratchpad before the first card** (the Nov 10 run broke both even after reading the weak spots): every question Ash asks in the note, each with the card that answers it or "left out: <why>"; and card 1's where-he-is in his own frames (the names he uses, his people, his deadline), sharpened to what a smart operator meant. Done when the question stands alone with the note hidden and every question in the note has a card or a reason.
3. **Choose the idea by its mechanism, then a far field** (Ash, 2026-11-03: "always a far field").
   - **Mechanism first:** the problem's cause and effect, someone doing something ("the team copies what the founder rewards").
   - **Then a far field whose experts run that same cause and effect** under a named practice, sharing nothing with the problem's subject. Keep the name only if an expert there would explain it with that same cause and effect.
   - **Three worlds per deck:** the problem, the daily-life metaphor (the `why` card), and the far field (the `far` card). No deck reuses a far field or a metaphor scene (in Fuji: `python gear/articles.py worlds`).
   Done when the deck has its three worlds and a real name for the big concept.
4. **Pick a look at random:** `python $ASH/visualize/skills/match-ash-design/scripts/palette.py --place dark --seed random`. No check against earlier decks. Pick the `--island` token and the four part colours from that combination (`article-format.md`, "The file you write"); only if `build_deck.py` says two parts look alike, run it again. Done when the tokens are in the article.
5. **Write the article file** in the scratchpad as `<id>.article.html`, card by card in the order, from expert knowledge. Draw a picture wherever article-format calls for one, new, from the article's own world. Facts, from what you know, with no lookups before the link: cut any name, date or number the idea doesn't need; who coined a term goes in the answer card's folded Sources, never on a card; every real fact left gets a source there. Before moving on, check the draft against every line of `weak-spots.md`. Done when every card reads alone with the others hidden and no weak spot shows.
6. **Check in code:** `python $SKILL_DIR/scripts/build_deck.py <id>.article.html --out <id>.html --avoid-worlds "<scenes and fields>"`, then `python $ASH/visualize/skills/brief-page/scripts/scan_copy.py <id>.html`, fixing every hit in the cards except what belongs to brief pages: "usually" in the `wrong` card's fixed heading, the `data-pattern` line, a formula's brackets and the years in Sources. No screenshots: the engine and the card layouts are tested on a phone whenever the skill changes (`scripts/deck_shots.js`). Done when the build prints "built" and the scan finds nothing to fix.
7. **Publish, and send the link at once:** file `<id>.html`, icon `book`, capabilities `{"sample": {}, "db": {}}` (the Ask pane talks to Claude; reaching the answer card saves `progress/read`). Send Ash one line right away, before anything else: the question and the link. Done when he has the link.
8. **Start the critic in the background** (`references/critic.md`: one agent, its prompt filled in, `run_in_background`). While it runs, do step 9. Done when it's started.
9. **In Fuji, file the deck:** `python gear/articles.py add --name "<question>" --url <link> --topics "<topic>; metaphor: <scene>; far: <field>" --combo <N> --excite <1-10>` (excite: how much Ash will want to open it, your judgment against what's unread), log to `ranges/learning/shasta` with `gear/log.py`, `python gear/check-maps.py`, commit, push (a run without Ash ends the message with `Fuji-Run: side-skill articles`). The daily runs refresh the reading list (`gear/articles.md`); a session never calls Google Calendar. Done when the deck is under Unread.
10. **Fix and republish from its comments.** Drop a comment that contradicts article-format or Ash's words. Never drop one that says a question Ash asked went unanswered, unless step 2's list left it out for a reason. Fix the rest in the article, rerun step 6, publish the same file again so the same link updates, and tell Ash in one line what changed. Add each new kind of mistake to `weak-spots.md` (one dated line); in Fuji, attach ash-skills now (`add_repo`, access push; not at the start, where it delays the link), commit it there with a version bump and push, so the next first draft avoids it; otherwise put the dated line in the reply for Ash to add. Done when the deck is republished and the weak spots are saved.
11. **Reply** with the deck's question, its link, its metaphor and far field, what the critic changed, and any topic left out. Done when the reply is sent.

## Files

- `references/article-format.md`: the article file, the card order, how each card is written, the visual weights, the drawings. Open on every run.
- `references/weak-spots.md`: where first drafts go wrong; read before writing, grows after every critic pass.
- `references/critic.md`: the background critic's prompt.
- `references/example-culture.article.html` and `references/example-money.article.html`: two whole articles that pass every check, one on a team habit and one on a finance concept with numbers.
- `assets/deck-template.html`: the engine. Change it only to change every deck; its Ask prompts read `world`, `expert`, `reader` and `asker` from each article.
- `scripts/build_deck.py`: puts an article into the engine and checks the rules code can check.
- `scripts/deck_shots.js`: screenshots every card at 390 by 844 and reports scroll, overlap with the island, tiny or cut-off text and dead space. Run it on both examples whenever the engine, the format or a card's rules change; not on every deck.
