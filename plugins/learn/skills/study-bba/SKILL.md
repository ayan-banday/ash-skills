---
name: "study-bba (jain)"
description: "How do I study a Jain BBA unit from my notes, slides or past papers so I can solve its questions and use it in a tech company? Reads what I drop in, offers up to three problems it solves, then builds a study page with worked examples and a Claude tutor beside it. Use learn:study for topics outside the BBA."
disable-model-invocation: true
---

# Study a BBA unit

Ash drops in his BBA material and gets one study page he learns from, with Claude in the page as his tutor. The approved standard is `references/example-page.html` (Managerial Accounting, "Does each sale make money?"): match its look, depth and worked examples, and apply the fixes in `references/writing-rules.md`, which came from his comments on it.

**Read `references/ash.md` before the opening.** It holds who he is and where examples come from. Never ask him these again.

## Steps

### 1. Read only what he gave you

Read every file he dropped in (PDF: `pdftotext -layout`; images: read them). No web search, no repo lookups: everything else you need is in this skill.

Done when you have written down for yourself: every concept the material teaches, in the course's own words; any questions his professor set and any answer key; and whether the subject is **procedural** (numbers and methods: accounting, finance, statistics) or **theory** (ideas and judgement: design thinking, ethics, UHV, critical thinking, English).

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
> **Pick a letter, or tell me what you want to study today.**

- **Each problem is a question a founder of a tech company would ask,** set in his world (`references/ash.md`), and it makes sense with the material hidden.
- **Together the problems cover every concept in the material.** Order them by what waits on what: the problem the others build on goes first.
- **No answers, no session plan, no steps.** He rejected a step-by-step script as too complicated.

Done when he picks a letter or names his own question.

### 3. Build the page

Write the page straight into HTML. Copy the `<head>`, CSS and nav from `references/example-page.html`, and follow `references/page-shape.md` for the parts in order, `references/writing-rules.md` for every line, and `references/tutor.md` for the tutor tab (paste its HTML, CSS and script as given).

- **Procedural subjects:** each concept ends in a worked example pair: the worked example in exam layout, then "Your turn" with new numbers and the answer hidden in `<details>`.
- **Theory subjects:** each concept ends in a worked scenario pair: one scenario reasoned through step by step, then "Your turn: think it through" with a new scenario, a box he writes in, a send button to the tutor, and one strong answer hidden in `<details>` to compare.
- **Write it with the strongest model available.** The cheap model only answers inside the page: a Haiku-written page came out thinner than the example.

Done when every concept from step 1 that belongs to the picked problem is taught and practised, and every number adds up (recheck each sum).

### 4. Check it

Run `python ../break-into-field/scripts/check_chapter.py <page.html>` from this skill's folder and fix every FAIL.

Done when it prints no FAIL.

### 5. One critic pass

Dispatch one fresh agent (Agent tool, model `sonnet`) with the prompt in `references/critic.md`, the page path and the writing rules path. Never this chat. Apply its fixes, rerun the checker.

Done when the fixes are applied and the checker passes again.

### 6. Publish and save

- **Publish** with the Artifact tool, `capabilities: {sample: {}}` (the tutor needs it). Desktop check only: Ash never studies on a phone.
- **Save the HTML** into the Jain-BBA repo when the material came from there: `D:\Jain-BBA\<Subject>\<Unit folder>\<Letter>_<short_question_slug>.html`, following the folders already there. Commit and push straight to `main`.
- **Log it in Fuji:** `python gear/log.py ranges/learning/jain-university "<subject, unit, problem letter: page built>" log.md`, then `python gear/check-maps.py`, commit and push.

Done when Ash has the link and one line on what the page covers.

## Follow-ups in the chat

- **He pastes answers:** check them against the page's own working, say which line went wrong and why, in under 120 words each.
- **He asks for the next problem:** build it by steps 3 to 6, with the same running company where it fits.
- **He gives feedback on a page:** fix the page, then add the rule to `references/writing-rules.md` with its bad and good line, so the next page has it.
