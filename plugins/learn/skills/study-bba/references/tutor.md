# The tutor beside the book

**A small tutor sits beside every big concept** (Ash, Nov 3 2026: "i had made it so there will be mini ai tutors everywhere"). It is break-into-field's station tutor, pasted as is: a ring in the margin beside each concept, each ring its own saved chat, a rail just inside the chapter tabs so a ring is always in reach, the ✦ and the gap symbol on any highlight, the desk with the model and thinking dots, and three standing moves. **BBA books have no notes** (Ash, Nov 4 2026: "I don't see any value in it"): no "My notes" panel and no "taught back" counter; a "Gaps" button in the top bar opens the gaps he saved.

**Read `../break-into-field/references/tutor.md` for what it does and the config shape. Paste `../break-into-field/assets/tutor.css` and `../break-into-field/assets/tutor.html` unchanged, with `assets/tabs.css` and `assets/tabs.html` before them** (page-shape.md, "The frame"). Per book you write only the rings, the `window.TUTOR` config and the layout lines below.

## The book's layout, so rings sit in the margin

- **One `.wrap` per part,** all inside one `<main>`: the cover, each chapter section and the founder questions (page-shape.md, "The frame"). No outer `.wrap` around the parts: the tutor moves each `.part > .wrap` left at 1200 px and wider to make room for the margin, the rail and the tabs.
- **Add to the book's CSS:** `.part > .wrap{position:relative}` (the margin rings are placed against it) and, so the top bar moves with the column, `@media (min-width:1200px){body.tutor .bar .in{max-width:1230px;margin-left:max(8px,calc((100vw - 760px - 470px - var(--tabsw,48px))/2 - 16px));margin-right:auto}body.desk-open .bar .in{max-width:calc(100vw - var(--deskw,480px) - 32px)}}` and `.bar .in{justify-content:space-between;align-items:center}`.
- **The "Gaps" button** goes last in the top bar: `<button class="notesbtn" id="gapsbtn" type="button">Gaps</button>`. The tutor fills in the count ("Gaps · 2").
- **The tutor's tokens:** run `palette.py --place dark --no-red --seed "<book title>"` with the same seed as the book's study tokens and paste its `--bg2` to `--onacc` lines into the same `:root`. Each chapter's block from `palette.py --chapters` carries its own tutor tokens, so the rings, the rail and the desk take the open chapter's colours. Add Overpass, Overpass Mono and Atkinson Hyperlegible to the fonts link if the book lacks them.
- **Every control takes its text and its background from the same side** (Ash, Nov 3 2026, after the model picker showed pale words on a pale box). Never pair a panel colour with a paper colour. `scripts/check_contrast.py` fails the build when a pair can't be read.

## Where the rings go

- **Each chapter gets 3 to 6:** one before each problem section, and one before "The idea that fixes it" while that keeps it at 6 (page-shape.md, "A chapter"), in reading order. Put the empty button right before it, inside the `.wrap`: `<button class="stn" type="button" data-s="c2-q1"></button>`. Prefix each id with its chapter (`c1-`, `c2-`, `fq-`).
- **The founder questions get one,** before the first question.
- **Name each chapter in the config "Chapter: <its tab name>"** (the checker counts 3 to 6 only for names starting "Chapter"); the founder questions take "Questions a founder might still have".
- **Theory books:** "Your turn: think it through" ends with its scenario and the hidden strong answer. He works it at the ring beside that question. No `.think` box.

## The config, filled for the BBA

- **`BOOK.id`:** stable for the unit's life (`bba-ma-u2`): his chats and gaps are saved under it, and a new chapter keeps it. **A book that replaces older pages on the same link maps their saved ids in `"LEGACY"`** (list the old `gaps` and `chats` with `ArtifactData` first; each document id is `<old bookId>__<old stationId>__…`), so his old gaps and chats show at the ring that now teaches that concept.
- **`BOOK.field`:** the subject, the university and the unit: "managerial accounting at Jain BBA, Unit 2: budgeting and variance analysis".
- **`BOOK.outcome`:** what the book lets him do, then "and answer the professor's questions in the course's own terms". **`BOOK.work`:** the book's invented company in one line with its numbers, then "and the tech company Ash will build". **`BOOK.short`:** the company and the period ("Sensa's quarter").
- **`ASH`:** break-into-field's line, ending "His exams come first: answers use the course's own terms and formulas (the professor's <subject> course)." Never a teacher's name, here or anywhere in the config.
- **Switches:** `"NOTES": false`, `"GAPS": true`, `"SCOPE": "chapter"` (each ring reads only the cover and its own chapter, so a long book stays under the tutor's 60,000-character cap).
- **`TEXT`:** `"main"`. **`STATIONS`:** each `q` ties the concept to the book's company and stands alone; `sug` holds 2 or 3 questions for that exact part, one of them exam-shaped. **`IDEAS`:** one map per chapter and for the founder questions, words of 4 letters or fewer starting with a space.

## Gaps

**Highlighting any text, on the page or in a tutor's reply, shows two symbols: ✦ asks about it, and the bookmark saves it as a gap** (Ash, Nov 4 2026). The bookmark opens a small box, "What aren't you sure of?"; his line is saved with the highlight, the chapter, the concept and that ring's last exchange, in the book's `gaps` collection. Nothing else happens until he chooses to deal with it.

**Fuji's hourly sync copies them into Jain-BBA** (`system/tools/pull_gaps.py`, playbook 07): one database file per unit, `gaps/<Subject>/<Unit_N>_marked.jsonl`, one gap per line, and a readable list per chapter generated from it, `gaps/<Subject>/<Unit_N>_marked.md`. So after publishing a new book, add its one line to Jain-BBA `system/tools/gap_pages.json`: `{"key": "u2", "title": "<book title>", "url": "<artifact link>", "db": "gaps/<Subject>/<Unit_N>_marked.jsonl", "list": "gaps/<Subject>/<Unit_N>_marked.md"}`. Each gap carries its own chapter, so a new chapter needs no new line.

## Check and publish

- **`python ../break-into-field/scripts/check_tutor.py <book.html>`** must print PASS, beside the other checks in step 4.
- **Playwright at 1280 px** (fake `window.claude` as in break-into-field's tutor.md): each tab flips to its chapter and its colours; rings beside their concepts and the rail just inside the tabs; a ring in a closed chapter, opened from the Gaps list, flips its tab; a highlight shows both symbols, on the page and in a reply; the gap box asks "What aren't you sure of?" and the saved gap carries the highlight, his line, the chapter, the concept and the last exchange; the model and thinking dots reach `sample()`; no console errors; at 390 px no sideways scroll.
- **Publish with `capabilities: {sample: {}, db: {}}`,** then `ArtifactData` `list` `gaps` on the artifact: an empty list is fine; the read must work.
