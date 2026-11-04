# The tutor beside the page

**A small tutor sits beside every big concept** (Ash, Nov 3 2026: "i had made it so there will be mini ai tutors everywhere"). It is break-into-field's station tutor, pasted as is: a ring in the margin beside each concept, each ring its own saved chat, a rail on the right edge so a station is always in reach, a ✦ dot on any highlight, the desk with Model and Thinking pickers, three standing moves, and "My notes" saved in the page's database. The single "Ask the tutor" tab is retired.

**Read `../break-into-field/references/tutor.md` for what it does and the config shape. Paste `../break-into-field/assets/tutor.css` and `../break-into-field/assets/tutor.html` unchanged.** Per page you write only the stations, the `window.TUTOR` config and the layout lines below.

## The page's layout, so stations sit in the margin

- **One `.wrap` per part:** `<header class="cover part"><div class="wrap">…</div></header>` and `<section class="part" id="…"><div class="wrap">…</div></section>`, all inside one `<main>`. No outer `.wrap` around the parts: the tutor moves each `.part > .wrap` left at 1200 px and wider to make room for the margin and the rail.
- **Add to the page's CSS:** `.part > .wrap{position:relative}` (the margin rings are placed against it) and, so the top bar moves with the column, `@media (min-width:1200px){body.tutor .bar .in{max-width:1230px;margin-left:max(8px,calc((100vw - 760px - 470px)/2 - 16px));margin-right:auto}body.desk-open .bar .in{max-width:calc(100vw - var(--deskw,480px) - 32px)}}`.
- **The "My notes" button** goes last in the top bar: `<button class="notesbtn" id="notesbtn" type="button">My notes</button>`.
- **The tutor's tokens:** run `palette.py --place dark --seed "<page title>"` with the same seed as the study tokens (same seed, same combination) and paste its `--bg2` to `--onacc` lines into the same `:root`. Add Overpass, Overpass Mono and Atkinson Hyperlegible to the fonts link if the page lacks them.
- **Every control takes its text and its background from the same side** (Ash, Nov 3 2026, after the model picker showed pale words on a pale box). Never pair a panel colour with a paper colour. `scripts/check_contrast.py` fails the build when a pair can't be read.

**Mark as a gap** (beside Send) saves what he doesn't fully get into the page's `gaps` collection. A Jain-BBA session copies them into the chapter's `marked_gaps/` file (Jain-BBA `system/playbooks/07_pull_marked_gaps.md`), so add each new page's link to that playbook's list.

## Where the stations go

- **The chapter (`#ch1`) gets 3 to 6:** one before "The idea that fixes it" and one before each `.q` block, in reading order. Put the empty button right before it, inside the `.wrap`: `<button class="stn" type="button" data-s="b-q1"></button>`.
- **Each later part gets one:** the exam section, and any assignment section.
- **Name the chapter in the config "Chapter: <short name>"** (the checker counts 3 to 6 only for names starting "Chapter"); parts take their own names.
- **Theory pages:** "Your turn: think it through" ends with its scenario and the hidden strong answer. He writes his thinking at the station beside that question, which keeps it in his notes. No `.think` box.

## The config, filled for the BBA

- **`BOOK.field`:** the subject, the university and the unit: "managerial accounting at Jain BBA, Unit 2: budgeting and the master budget".
- **`BOOK.outcome`:** what the page lets him do, then "and answer <professor>'s questions in the course's own terms". **`BOOK.work`:** the page's invented company in one line with its numbers, then "and the tech company Ash will build". **`BOOK.short`:** the company and the period ("Rollcall's quarter").
- **`ASH`:** break-into-field's line, ending "His exams come first: answers use the course's own terms and formulas (<professor>'s <subject> course)."
- **`TEXT`:** `"main"`. **`STATIONS`:** each `q` ties the concept to the page's company and stands alone; `sug` holds 2 or 3 questions for that exact part, one of them exam-shaped. **`IDEAS`:** one map per chapter and part, words of 4 letters or fewer starting with a space.

## Check and publish

- **`python ../break-into-field/scripts/check_tutor.py <page.html>`** must print PASS, beside the two checks in step 4.
- **Playwright at 1280 px** (fake `window.claude` as in break-into-field's tutor.md): rings beside their concepts, the bar's "My notes" fully visible, a station's desk opening, no console errors; at 390 px no sideways scroll.
- **Publish with `capabilities: {sample: {}, db: {}}`,** then `ArtifactData` `list` `notes` on the artifact: an empty list is fine; the read must work.
