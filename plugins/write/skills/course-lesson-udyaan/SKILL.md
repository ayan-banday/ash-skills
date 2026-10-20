---
name: course-lesson-udyaan
description: "[Udyaan course · was course-writer] How do I write a Day N lesson or course page students actually read? Write or rewrite student-facing course content in a plain, spoken, 7th-grade-clear voice, as a daily module (\"Day N\" lesson with a fixed skeleton, labeled mini-examples, rules with good and bad picks, and a GPT-based Do) or as a welcome page, week intro, or any page a busy student reads. Use whenever Ash asks to draft, rewrite, tighten, or \"make clearer\" a Day, module, lesson, welcome page, or course page for Udyaan, the Agriculture Edition, or any future course. Also use for \"write day 4\", \"next module\", \"week 2 lessons\", \"student-facing\", \"make it less AI\", \"bold and bullet this\", \"do it like Dan Koe or Nicolas Cole\", pasted course text that sounds stiff, or questions about what a module should contain. Use it even when he only says \"write the next day\". Replaces the old course-page-writer and course-module-writer skills."
---

# Course Writer

Writes the pages a student reads in a course. Two kinds:

- **Daily module:** a "Day N" page a student reads in about five minutes, then does one small action. It has a fixed skeleton, described below.
- **Other pages:** a welcome page, week intro, or any student-facing page. Ash gives the structure, and this skill supplies the voice. See `references/welcome-page.md`.

The goal of every page is that the student knows what to do, why it matters, and what to avoid, with no question left hanging.

## Why the rules are strict

The reader skims between classes and quits on any paragraph that does not pay them back. Every rule below came from a correction Ash made while rewriting the course by hand. The recurring complaint was filler that sounds like writing ("garbage sentences"), so the whole skill serves one test: **would a 7th grader get this on the first read, and does this sentence add something?**

## Who owns what

Ash decides what the course teaches and, for non-module pages, how the page is structured. This skill owns voice and form, and the daily-module skeleton Ash approved. Never invent a week plan, a statistic, a credential, or a real company's result. If an input is missing, ask.

## Before you write

1. **Read the reader and the promise.** For the Agriculture Edition, read `03 Projects Archive/Udyaan - From Idea to Business/[C] Agriculture Edition Hybrid Course Spec.md`, plus the week plan for the day's question, belief, Do, and GPT job. For another course, read its spec.
2. **Read `references/examples.md`** for a module, or `references/welcome-page.md` for any other page. Match their feel, not their words.
3. **Collect the day's inputs** for a module:
   - the question the day answers
   - the belief to break
   - what the student made yesterday and where it is saved
   - the one decision or rule of the day
   - what the GPT does in the Do
   - tomorrow's question
4. **Take audience details from the spec and examples only.** Degrees, campus, and daily-life details come from what Ash has given. This skill holds no audience facts, so the same rules work for any course.

## Voice

Ash's newsletter voice with the edges filed down. The page sounds like a friendly senior who is also a student, talking in a corridor.

- **Peer, plain, spoken.** Use contractions. Say "figure out", "spot", "find", "try". Avoid "demystify", "identify", "leverage", "journey", "empower", "crucial", "optimize", and "link" for a stage of a chain.
- **Second person.** Talk to "you". Put the student's private doubts into "Maybe you..." or "If you study..." lines.
- **Keep out** curses, war or military metaphors, and personal crisis stories. One light joke is welcome, usually near the author block. A pop-culture beat goes in only when Ash asks for one.
- **The author appears once,** in a short "Who am I?" block on a welcome page: role, a nerd line, credibility, one joke. Credentials never lead. Daily modules carry no author block.

## The daily-module skeleton

Every module uses this order. Parts 5 to 7 flex with what the day's decision needs. Details and the content structures behind each part are in `references/structure.md`.

| # | Part | Job | Size |
|---|---|---|---|
| 1 | Title | "Day N: Topic" | one line |
| 2 | Bridge | What the student made yesterday, then what today does | 2 lines |
| 3 | Opener | Belief or wrong move, what people do because of it (bullets), the impact | heading, 1 line, 3-4 bullets, 1 line |
| 4 | Truth | The replacement idea, plus a one-line plain definition | 1-3 lines |
| 5 | Mini example | The simplest possible picture, in labeled lines | 3-4 lines |
| 6 | Real example | One ordinary-life case, shown as a contrast pair | 2 short paragraphs |
| 7 | Domain example and rule | A case from the course's field, then a rule with a test, a good pick, and a bad pick | 150-250 words |
| 8 | Objections | Answered inside the section that raises them | 1-2 sentences each |
| 9 | The Do | One plain explanation, the GPT link and trigger word, a named doc to save into | 3-5 lines |
| 10 | Week map and tomorrow | This week's days with today marked, then tomorrow in one line | 5 bullets, 1-2 lines |

The order is fixed: the Do (part 9) comes before the week map and tomorrow (part 10). Every module has parts 1 to 4, 9, and 10. Use as many of 5 to 8 as the day's single decision requires. Length follows the content, usually 600 to 1,100 words. If the student can finish the Do without a paragraph, cut it or move it to the GPT.

## Sentence rules

Each rule has bad and good pairs in `references/good-and-bad.md`. Read that file before drafting.

1. **Say it once, plainly.** No setup such as "one of two things happened", and no splitting one thought into two sentences.
2. **Every sentence adds a fact, an example, or an action.** Cut sentences that comment on the page ("All three are real"), label ("Both groups make the same error"), or reassure.
3. **Short words, short clauses, mixed lengths.** A long, flowing sentence sits next to a short one, because matched lengths read as machine-written. Use the plain word for the action. The week plan may say "red-team" or "audit", and the page says "poke holes in" or "check".
4. **Write full thoughts.** Skip fragments used for rhythm and one-word sentences.
5. **Put the impact in the claim's own sentence.** "The biggest problem is spoilage. A company can't open two new cities if a fifth of its fruit rots." The result follows the claim immediately.
6. **No lead-ins.** "Here's what it looks like", "Here's the thing", "Let's dive in", and "It's worth noting" are out. Write "For example:" or go straight into the point.
7. **No "not X, but Y", matched triplets, or em dashes.** State the point positively.
8. **Define a term in the sentence where it first appears,** in plain words. Course terms (Workbook, Offer Document, Change Log) wait for the module that uses them.
9. **Ask a question only when the reader would ask it.** Questions are optional connectors and never a template. A section may simply follow the one before it.
10. **Specific beats general.** "Search for startup ideas on YouTube and Instagram" beats "research the idea". To find the real behaviors for an opener, ask what this student would type, open, ask, or buy this week because of the belief. If you cannot name one, you do not know the reader well enough yet, so go back to the spec.
11. **No claims about how many people do something.** "Most founders make two or three of these" and "almost every beginner" are invented statistics. State what happens to this student instead.
12. **Count what you list.** If you write "five mistakes", there are five, and any summary line matches the list.
13. **Numbers are exact when the course has them** ("20 to 40 minutes", "under 7 minutes"). Take them from Ash or the spec.

## Formatting rules

1. **Headings give the content or the answer.** "Starting with an idea leaves you stuck", never "Why start here" or "Mistakes to avoid". A heading never claims how many people do something. A plain question heading is fine on a welcome page ("Who is this for?"). Never a clever heading: no counting the contents, no aphorisms, no slogans (see `references/good-and-bad.md`).
2. **Bullets for three or more parallel items.** Each opens with a bold phrase.
3. **Numbered lists for actions in order.**
4. **Bold one or two phrases per paragraph,** never a whole sentence. Reading only the bold should give the point.
5. **Block quotes** for labeled examples, templates, and anything the student pastes or fills.
6. **One to three sentences per paragraph,** with white space between.
7. **No parenthetical side notes** and no "(made up)" labels. If a note matters, it becomes a sentence in the right section. The one exception is a single quiet offer on a welcome page, such as "(If you have a question, send it to me.)".
8. **End on one next step,** with the next module named and, where known, how long it takes.

## Examples

- **The first example is the simplest one possible,** in labeled lines, like Goal, Problem, Solution with a vending machine.
- **One idea per example.** A contrast pair carries the lesson: the baker who wants to grow and the baker who does not.
- **Say it, then show it.** Every claim is followed by a concrete example in the next paragraph.
- **Invent fresh examples for every module.** The examples in `references/examples.md` show the shape and are not material to reuse. The same snack, baker, canteen queue, or fruit pulp case must not appear in a new day, apart from a one-line callback to yesterday. A reused example makes the course feel recycled.
- **An example must be a working model of the lesson.** Check its logic before you keep it. An offer example needs a real payer and a real price, and a problem example needs a group you could find. If the example would fail the rule the day teaches, replace it.
- **Invented details are fine** and carry no label. Never invent a statistic, a real company's result, or a quote.
- **Mistakes live inside examples and rules,** at the point they happen. There is no mistakes section.
- **Rules use one format:** the rule in bold, a one-line test, then "Good pick" and "Bad pick", each leading with the pick and then its impact.
- **Write a new test for each day's rule.** Day 1's test ("If this blocker disappeared tomorrow, how much closer would they be?") fits the blocker rule only. A different rule needs a question that fits it.

## When the day's content is a list

Some days teach a list, such as five beginner mistakes or five offer lines. The list appears once, as the opener or as the truth section, in bullets with a bold lead and one plain line each. Every item gets a concrete picture of what the student would do, so it is more than a label.

Then pick one item and run it through a contrast pair, so the student sees it caught and fixed. The list never appears a second time, and no section only re-announces it. The student's own work from the earlier day is what they check each item against, so name that work in the Do.

In testing, the failure was a module that listed the five mistakes in the opener and again under a new heading. If a second list is tempting, add the missing detail to the first list instead.

## The Do

The page explains in plain words, links the GPT, and names a Google Doc to save the output into. The GPT holds the case, the interview, and the summary, so the lesson page holds none of them. Add a "Short on time?" line with a smaller version. Put the time in the heading, "(20 to 30 minutes)".

## Variation

The structure and the voice stay fixed, and the wording changes so the course does not read like a template. Never open two days in a row the same way, and use "Most people believe" at most once in a week. Open with a scene, a direct instruction, the student's own voice, a recap, or the cost of the mistake. The catalogue, with the Dan Koe moves it comes from, is in `references/variation.md`.

## Before you show the draft

Self-review is not enough. In testing, drafts that read as compliant still carried em dashes, parenthetical asides, and fragments, because the rules were treated as advice. So the check is mechanical.

1. **Save the draft to a scratch file** (the session scratchpad, not the project). Include only the page, from the title to the last line.
2. **Run the linter** and fix every `[FIX]` line:
   - Daily module: `python -I <this skill's base directory>/scripts/lint_module.py <draft.md>` (the skill may be installed in `~/.claude/skills/` or in a repo's `.claude/skills/`; use the base directory shown when the skill loads)
   - Welcome page or other page: add `--type page`
3. **Look at every `[REVIEW]` line** and either change it or decide it is fine. Examples: a short heading that still holds the answer, a callback to yesterday's example.
4. **Re-run until it prints PASS**, or until only reviewed items remain.
5. **Then do the judgment checks the linter cannot do:**
   - Does every sentence add something?
   - Would a 7th grader follow each example on the first read?
   - Does the example model the lesson, and does every count match its list?
   - Does the opener differ from yesterday's and from the rest of the week's?
   - Is every number, name, and credential from Ash or the spec, or plainly an invented example?
   - Do the week map and tomorrow line match the plan?

## How to deliver

1. Your final reply is the page itself. Print it from the scratch file, starting with the title line. Put process notes (what the linter said, what you checked) after the judgment calls or leave them out, because anything before the title ends up in the page. A checklist with tick marks before the title is the same mistake as "Now I'll draft Day 4".
2. Draft in chat. Do not save a course file until Ash says to.
3. After the draft, add a "Judgment calls" heading with a few plain bullets: anything chosen without being told, such as an invented example, a trigger word, or a number. Describe the choice and leave the skill's internal terms ("rotation plan", "variant") out of it.
4. When Ash corrects something, apply it, then append a dated line under Refinements below and bump the version.

## References

- `references/structure.md`: the module skeleton in detail and the content structures to use inside it.
- `references/good-and-bad.md`: bad and good pairs for every rule, and the banned patterns.
- `references/variation.md`: how to keep modules fresh, with Dan Koe moves.
- `references/examples.md`: approved Day 1 and two working drafts, Days 2 and 3.
- `references/welcome-page.md`: the approved welcome page and the rules for non-module pages.
- `references/legacy-passages.md`: two older voice samples, used for tone only.
- `scripts/lint_module.py`: mechanical check for banned patterns, run before every draft is shown.

## Refinements

- 2026-10-12 v7: Ash dropped the "To test it, ask" lines from the Day 2 rules. A rule is shown by its bold statement and its good and bad picks only, so the student learns it by example and is not handed a question to ask. Day 3 follows the same form. Day 1 still carries its test line until Ash says to cut it. Also: a day with two kinds of student (has a problem, has none) gives the no-problem student the most room, and the with-a-problem section only helps them find where the biggest impact sits. Openers on belief days use "might" and "may", and the Do for the GPT stays two short lines with no "Short on time?" line.
- 2026-10-12 v6: Ash banned the word "link" for parts of the agriculture chain (it is jargon that helps no one). Say "stage" instead, and keep "link" only for web links. Day 2 also changed: the with-a-problem case checks the stages before and after the solution and aims it at the stage that loses the most, the no-problem case starts from interests, and the GPT Do is short and has no "Short on time?" line.
- 2026-10-12 v5: Merged course-page-writer into this skill and renamed it from course-module-writer. Module rules take precedence where they conflict: no "(made up)" labels and no bracketed asides (a single quiet offer on a welcome page is the exception). Kept from course-page-writer: the voice notes and avoid-word list, the author-block rule, the welcome page and its facts-to-confirm note, the "say it, then show it" and term-definition rules, and the older teaching passages. Added `--type page` to the linter and filler words from the old avoid list.
- 2026-10-12 v4: Third test run (Day 4) passed the lint and kept the list once, but put the week map before the Do, folded a question-only section into the middle, used a rule that did not match its heading, and again opened its final reply with a tick-mark checklist. Added lint checks for section order, one "(today)" marker, and question-only sections.
- 2026-10-12 v3: Second test run passed the lint and was much closer, but still listed the five mistakes twice, put a frequency claim in a heading, kept the plan's jargon ("red-teams") in the Do, used ", not X" phrasing, and put a tick-mark checklist before the title. Added the list-once rule, plain-word rule, heading rule, final-reply rule, and lint patterns for each.
- 2026-10-12 v2: First test run (Day 4 and Day 5 written by a fresh agent) showed em dashes, a leaked preamble, parenthetical asides, fragments, a reused canteen example, invented frequency claims, a miscounted list, and an offer example with no payer. Added the lint script and delivery steps, fresh-example and working-model rules, a new-test-per-rule rule, a list-day pattern, and a no-statistics rule.
- 2026-10-12 v1: Built from Ash's rewrites of Days 1 to 3, the Dan Koe course (Days 2 to 30), and Nicolas Cole's five-part module framework (reasons why, mistakes to avoid, steps, objections, walkthrough).
- 2026-10-09 (course-page-writer v1): Built from welcome page drafts 1 to 4 and two teaching samples. Ash dropped the fixed section template, wanted more bullets and bold, varied sentence lengths, forward questions, and a spoken, less professional sound.
