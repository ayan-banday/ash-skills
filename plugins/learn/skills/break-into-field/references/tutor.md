# The tutor inside the book

Ash reads a book alone, and nothing checks what he understood. The tutor fixes that (Fuji ticket 08, Nov 2 2026): beside each big concept sits a **station**. He opens it, says what he got or asks anything, and Claude answers as a ten-year expert in the field. His notes on each station are saved in the page's database, so later sessions know where he stands.

**Paste the code; don't rewrite it.** The CSS is `assets/tutor.css`, the desk and the script are `assets/tutor.html`. Both are the same for every book and use only the 12 palette tokens (`look.md`). Per book you write only three things: where the stations go, a `window.TUTOR` config, and the example exchange.

## What it does

- **Each station is its own chat.** It keeps its own history (saved, restored on return), and nothing crosses from one station to another apart from the book itself and that station's notes.
- **Every call knows:** who Ash is, the book's outcome and the work it serves, the whole book's text (capped near 60,000 characters), the station's concept and question, anything he highlighted, and that station's notes so far. **Not** where he is scrolled: the highlight is what matters.
- **A question gets a straight answer,** as deep as he asked, and stops. No word cap.
- **A teach-back or brain-dump gets the full loop:** what he has, in his own words, then one sharper sentence in bold; the one gap that matters for his work, with a small scene and numbers; one idea from beyond the book (plain idea, a daily-life picture, its `==name==`, the same idea in a far-away field, what it changes); then `---` and a practice case with a named person, numbers and up to 3 standalone questions.
- **No template labels, ever** ("Sharper:", "Gap:", "Beyond the book"): each paragraph opens with a bold phrase that is its point. It may disagree with the book in one plain sentence when the book is wrong or thin.
- **Haiku or Sonnet, by how many ideas the message holds.** The page counts locally: the ideas in the chapter's `IDEAS` map whose words appear, or the question marks, whichever is bigger. Over 70 words with two ideas or fewer, Haiku counts first. One or two ideas go to Haiku (`claude-haiku-5-5`, `quick`); more go to Sonnet (`claude-sonnet-5-5`, `default`, `effort: "low"`). That rule is **Auto**. Under the input, **Model** (Auto, Haiku, Sonnet, Opus) and **Thinking** (Low, Medium, High) let him pick instead: a picked model answers at the picked thinking (`effort`), Opus on `modelTier: "complex"`. His pick is remembered in his browser. A route chip under his message names the model, the thinking and why ("you picked it", or the ideas).
- **Notes are written for Ash first,** after every reply, by Haiku: what you've got (his words quoted), still open (0 to 3), your plan. Later Claude sessions read the same notes.
- **The prompts (`RULES`, `NOTES`, `COUNT`) live in `assets/tutor.html`, verbatim from the spec.** Change them there, for every book at once.

## Where it sits and how it looks

- **Stations** sit in the right margin beside their concept at 1200 px and wider: a ring (filled once taught back) and the question in small type, and "N still open" under it. Under 1200 px, and in wide parts (the map, the shelves), a station is an inline card above its heading.
- **A sticky rail** on the right edge shows the current chapter's stations as a short transit line. The station nearest above the reading line is the big ring, with its question beside it. So a clickable station is in view at every scroll position. It hides while the desk is open and under 900 px.
- **The selection dot:** highlight any text and a small ✦ dot appears. It opens the nearest station above with the highlight attached as a removable chip.
- **The desk** slides in from the right (480 px; the page shifts left at 1200 px and wider; Esc closes). **Its left edge drags** to any width from 360 px to three quarters of the window, full height always, so he can split the screen half and half; arrow keys on the edge move it 40 px, double-click resets, and the width is remembered in his browser. The desk holds: the chapter kicker, the concept, the chapter's station line, tabs **Talk** and **My notes**. A fresh station shows its question and 2 or 3 suggested questions. A conversation is one scrolling thread per station (Ash, Nov 2: one exchange per page with number chips read as "a new chat every time"): every exchange stacks, his bubble, the route chip, the reply, and the newest opens at its top. Only the newest reply's "Try it" card has an answer box. Every message sends the station's last 30 turns, so follow-ups keep the context. Under the input sit three standing moves, the same on every station: **Give me a practice case**, **Apply it to <the outcome, short>**, **Let me explain it back**. My notes shows one pink card per station.

## How to add it to a book

1. **Fonts and palette first** (`look.md`): the tutor uses `--bg` to `--acc` and Overpass, Atkinson Hyperlegible, Overpass Mono.
2. **Place 3 to 6 stations per chapter,** one per big concept: the idea that fixes it, each key habit, how you'd build it. Parts before the chapters get one only where teaching back helps (one per part at most). Put an empty button right before the concept's heading, inside the chapter's `.wrap`:
   ```html
   <button class="stn" type="button" data-s="c1-idea"></button>
   <h3>The idea that fixes it</h3>
   ```
   In a wide part (the map, the shelves), add `inline`: `<button class="stn inline" ...>`.
3. **Paste `assets/tutor.css`** after the book's CSS.
4. **Add a "My notes" button to the top bar:** `<button class="notesbtn" id="notesbtn" type="button">My notes</button>`.
5. **Write the config as JSON** (double quotes, no comments; `check_tutor.py` parses it), in a `<script>` just before `</body>`. `id` is stable (notes are saved under it), `short` names the outcome for the "Apply it to ..." move, `TEXT` is the element holding the book's text, `STATIONS` are in reading order with ids matching `data-s`, `IDEAS` maps each chapter's ideas to the words that point at them:
   ```js
   window.TUTOR = {
     "BOOK": {
       "id": "breaking-into-growth",
       "title": "Breaking Into Growth",
       "field": "growth: how a free product gets found, tried, shared and come back to",
       "outcome": "Get chatform.in to 50,000 page views a month with no money for ads, and know each week whether it's working.",
       "work": "chatform.in, a chat-style form builder that Ash runs with his friend Mohit.",
       "short": "chatform"
     },
     "ASH": "Ash, 20, studies BBA Entrepreneurship at Jain University in Bangalore. He is going into technology and wants to build a billion-dollar technology company. He is strong in marketing and the big picture; in technology he doesn't know what he doesn't know. He builds with AI agents daily. He learns from one real problem, a principle, and the same principle in a very different place.",
     "TEXT": "main",
     "STATIONS": {
       "c1-idea": { "chapter": "Chapter 1", "name": "One weekly number, judged against a four-week line",
         "q": "How would you and Mohit judge chatform's next move?",
         "sug": ["Why does a four-week average beat last week's number?", "How big a rise should chatform need before you keep a move?"] }
     },
     "IDEAS": {
       "Chapter 1": { "noise": ["wobble", "noise", "swing", "spike", "fluke", " luck"] }
     },
     "EXAMPLE": { "station": "c1-idea", "me": "...", "bot": "...", "route": { "deep": true, "names": ["..."] } }
   };
   ```
   - **`q`** ties the concept to the book's outcome and stands alone. **`sug`**: 2 or 3 questions written for that exact part, each naming its thing, never generic.
   - **`IDEAS`:** 6 to 12 per chapter, 3 to 6 per part, with plain synonyms ("wobble" and "noise" are one idea). Start every word of 4 letters or fewer with a space (`" rank"`, `" loop"`, `" ga "`) so it matches only as a whole word (simple endings like "ranks" or "ranked" still count): "rank" alone would also count "frank", and "loop" would count "loophole", inflating the count toward Sonnet.
   - **`EXAMPLE`** (optional, one per book): a real-sounding teach-back and the reply the tutor should give, shown on the first chapter's first station until Ash sends his own. It shows him what a good exchange looks like. It is never saved or sent.
6. **Paste `assets/tutor.html`** after the config, before `</body>`.
7. **Run `python scripts/check_tutor.py <book.html>`.** Done when it prints no FAIL.
8. **Publish with `capabilities: {sample: {}, db: {}}`.** Without `sample` the stations and notes still show and the input says the tutor needs Claude.

## Where his notes live

- `notes/<bookId>__<stationId>`: `{book, chapter, concept, got, open: [], plan, updated}`, rewritten after every reply.
- `gaps/<bookId>__<stationId>__<gid>`: `{gid, station, book, chapter, concept, marked, note, status, created, closed?}`, one per press of **Mark as a gap** (beside Send: saves the highlight and what he typed as something he doesn't fully get yet; Ash, Nov 4 2026). Open gaps show first in My notes with "Work on it" and "Got it now", count on the station's ring, and go to the tutor with every call at that station.
- `chats/<bookId>__<stationId>`: `{book, chapter, concept, turns: [{role, content, route}], updated}`, the last 40 turns.
- **A later session reads them** with the `ArtifactData` tool on the book's artifact: `list` the collection `notes` (or `chats`). Read `notes` before writing the book's next chapter or planning his next move: "still open" is what to teach next.

## Check it (only what changed)

- **Playwright at 1280 px**, with a fake `window.claude` (below): stations beside their concepts; dragging the desk to half the window keeps the reading column clear of it; a picked model and thinking reach `sample()`; the rail at five scroll positions through a chapter, each with a readable, clickable station; the desk on a fresh station, on the example and on My notes; the selection dot opening the right station with the highlight chip; no console errors; at 390 px no sideways scroll.
- **Fake `window.claude`** so the page runs outside Claude: `window.claude = {use: async n => n === "sample" ? fakeSample : n === "db" ? fakeDb : null}`, where `fakeSample(msgs, opts)` returns `{text}` and calls `opts.onText`, `fakeSample.json` returns `{got, open, plan}` or `{n, names}`, and `fakeDb` is an in-memory `{doc(p){return {set, get}}, collection(p){return {get}}}`.
- **The tutor's voice can't run outside Claude,** so test a prompt change with a Haiku agent given `RULES` (filled) and the chapter text, then one critic against "How it writes".
- **After publishing,** `ArtifactData` `list` `notes` and `list` `chats` on the artifact: an empty list is fine; the read must work.
