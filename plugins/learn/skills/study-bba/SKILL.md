---
name: "study-bba (jain)"
description: "How do I study a Jain BBA unit from my notes, slides or past papers so I can solve its questions and use it in a tech company? Reads what I drop in, offers up to three problems it solves, then builds one tabbed book for the unit: a chapter per problem, each starting from a founder's problem, with worked examples, a Claude tutor beside every concept and a gap I can mark on any highlight. Use learn:study for topics outside the BBA."
disable-model-invocation: true
---

# Study a BBA unit

**Read `/write:match-ash-writing` and `/visualize:match-ash-design` first** (`../../../write/skills/match-ash-writing/SKILL.md`, `../../../visualize/skills/match-ash-design/SKILL.md`): Ash's writing rules, and his design rules and colours, for every case. This skill's own rules win where they are newer or more specific.

Ash drops in his BBA material and gets **one book per unit (or per study session): one link, a tab per chapter**, with Claude beside every concept as his tutor. Each problem the opening offers becomes a chapter; the book ends with "Questions a founder might still have". The look and depth of `references/example-page.html` (Managerial Accounting, "Does each sale make money?") still hold for a chapter's insides; `references/page-shape.md` holds the book's shape, which wins over the example wherever they differ.

**Read `references/ash.md` before the opening.** It holds who he is and where examples come from. Never ask him these again.

## Steps

### 1. Read only what he gave you

Read every file he dropped in (PDF: `pdftotext -layout`; images: read them). No web search, no repo lookups: everything else you need is in this skill.

Done when you have written down for yourself: every concept the material teaches, in the course's own words; any questions his professor set, any answer key and any assignment; the names of his teachers (only so `check_book.py --names` can keep them off the page); whether the subject is **procedural** (numbers and methods: accounting, finance, statistics) or **theory** (ideas and judgement: design thinking, ethics, UHV, critical thinking, English); and which concepts he has already studied (a book or chapter that already exists, or he says so), with the gaps he marked on them (Jain-BBA `gaps/<Subject>/<Unit>_marked.jsonl`).

### 2. The opening, one message

Send only this shape, then wait:

> **From what you gave me, you can learn these concepts:** the course's terms, grouped under 2 or 3 bold labels so he can find them later.
>
> **Here are [two or three] problems they let you solve.** [One sentence of unlock order: which comes first and why.]
>
> **A. How do you …?** (the concepts it uses)
> **B. How do you …?** (…)
> **C. How do you …?** (…)
>
> **Pick a letter, or say "all of them" for the whole book.**

- **Each problem is a question a founder of a tech company would ask,** set in his world (`references/ash.md`), and it makes sense with the material hidden.
- **Together the problems cover every concept in the material.** Order them by what waits on what: the problem the others build on goes first.
- **Each problem becomes one chapter tab of the book,** named for its concept in the course's words. The problem set stays in the opening; it isn't printed on the cover.
- **No answers, no session plan, no steps.** He rejected a step-by-step script as too complicated.

Done when he picks a letter, says all of them, or names his own question.

### 3. Build the book

Write the book straight into HTML by `references/page-shape.md`: copy the `<head>`, CSS and class names from `references/example-page.html`, then paste `assets/tabs.css`, break-into-field's `assets/tutor.css`, and at the end `assets/tabs.html` and break-into-field's `assets/tutor.html`. Follow `references/writing-rules.md` for every line (it opens with break-into-field's rules) and `references/tutor.md` for the tutors.

- **Colours (Ash, Nov 4 2026: a different palette for each chapter, never red):** the book's own tokens from `python ../../../visualize/skills/match-ash-design/scripts/palette.py --place dark --format study --no-red --seed "<book title>"`, the tutor's from the same command without `--format study`, and one palette per tab (every chapter and the founder questions) from `palette.py --format study --chapters <tabs> --seed "<book title>"`. Paste each block as printed; write every colour through the tokens, pictures included (`--ink` for labels and lines on the board, `--on` for text inside a filled shape).
- **Procedural subjects:** each concept ends in a worked example pair: the worked example in exam layout, then "Your turn" with new numbers and the answer hidden in `<details>`.
- **Theory subjects:** each concept ends in a worked scenario pair: one scenario reasoned through step by step, then "Your turn: think it through" with a new scenario, which he works at the ring beside it, and one strong answer hidden in `<details>` to compare.
- **The professor's questions live inside the chapters:** a strong one becomes the worked example or "Your turn" of the section that teaches its concept; weak or repeat ones are dropped; an assignment gets one line where its concept is taught. No class-questions section.
- **A chapter he has already studied goes short:** re-teach only the gaps he marked there (page-shape.md, "A short chapter").
- **Write it with the strongest model available.** Haiku and Sonnet only answer inside the book (`references/tutor.md`): a Haiku-written page came out thinner than the example.

Done when every concept from step 1 that belongs to the picked problems is taught and practised, and every number adds up (recheck each sum).

### 4. Check it

Run all four from this skill's folder and fix every FAIL:

- `python ../break-into-field/scripts/check_chapter.py <book.html>`: the writing rules, chapter by chapter.
- `python scripts/check_contrast.py <book.html>`: every box with a text colour and a background, the tutor's controls included, reads at 4.5 to 1 or better.
- `python ../break-into-field/scripts/check_tutor.py <book.html>`: 3 to 6 rings per chapter, one per later part, each with a question and 2 or 3 suggestions, and the current tutor code.
- `python scripts/check_book.py <book.html> --names <his teachers, from step 1>`: the book's shape, the tabs and palettes, no class-questions part, no teacher's name, problem headings.

Done when none prints a FAIL.

### 5. One critic pass

Dispatch one fresh agent by `references/critic.md` (break-into-field's critic, with the BBA changes). Never this chat. Apply its fixes, rerun the checks.

Done when the fixes are applied and the checks pass again.

### 6. Publish and save

- **Publish** with the Artifact tool, `capabilities: {sample: {}, db: {}}` (the rings need both: Claude, and his saved gaps and chats). One book per unit keeps one link: a new chapter for the same unit is published to the same `url`. Desktop check only: Ash never studies on a phone.
- **Save the HTML** into the Jain-BBA repo when the material came from there: `<Subject>/<Unit folder>/<Unit_N>_book.html` (for example `Managerial_Accounting/Unit_2_Marginal_Costing_and_Budgeting/Unit_2_book.html`), following the folders already there. An older page this book replaces becomes a one-line pointer to its chapter's tab (`<link>#chN`), republished to its own link. Commit and push straight to `main`.
- **Name the book in Jain-BBA's gap list:** one line in `system/tools/gap_pages.json` for a new book (`references/tutor.md`, "Gaps"); none for a new chapter of a book already listed.
- **Log it in Fuji:** `python gear/log.py ranges/learning/jain-university "<subject, unit: book built or chapter added>" log.md`, then `python gear/check-maps.py`, commit and push.

Done when Ash has the link and one line on what the book covers.

## Follow-ups in the chat

- **He pastes answers:** check them against the book's own working, say which line went wrong and why, in under 120 words each.
- **He asks for the next problem:** add it as the next chapter tab of the same book by steps 3 to 6, with the same running company where it fits.
- **He gives feedback on a book:** fix the book, then **rewrite the rule his feedback belongs to, where it lives**: the book's shape in `references/page-shape.md`, how a line reads in `references/writing-rules.md`, the tutor and gaps in `references/tutor.md` (or break-into-field's `assets/tutor.*` and `references/tutor.md` when the shared tutor changes), the steps here, and a new check in `scripts/check_book.py` when a script can catch it. Change the rule in place, with his words and the date; never add a numbered rule to a list. Then bump the learn plugin's version.
