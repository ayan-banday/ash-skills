---
name: "course-lesson (udyaan)"
description: "[course] How do I write a Day N lesson or course page students actually read? Write or rewrite student-facing course content in a plain, spoken, 7th-grade-clear voice: question-led days that each move the student one step from A to B, answer every question they raise in full, follow one running student as the worked example, and end in one low-effort Do with a GPT. Also writes welcome pages and week openers, and runs a whole week with fresh reviewers. Use whenever Ash asks to draft, rewrite, tighten, or \"make clearer\" a Day, module, lesson, week, welcome page, or course page for Udyaan, the Agriculture Edition, or any future course. Also use for \"write day 4\", \"next module\", \"week 2 lessons\", \"student-facing\", \"make it less AI\", \"bold and bullet this\", \"do it like Dan Koe or Nicolas Cole\", pasted course text that sounds stiff, or questions about what a module should contain. Use it even when he only says \"write the next day\". Replaces the old course-page-writer and course-module-writer skills."
---

# Course Writer

Writes the pages a student reads in a course. Two kinds:

- **Daily module:** a "Day N" page a student reads in a few minutes, then does one small action. Its jobs and their order are below.
- **Other pages:** a welcome page, a week opener, or any student-facing page. Ash gives the structure, and this skill supplies the voice. See `references/welcome-page.md`.

The goal of every page: the student knows what to do, why it matters, and what to avoid, with **no question left hanging**.

**Writing a whole week or more?** Follow `references/write-a-week.md` as well: a plan first, one fact sheet for the running student's story, and a fresh reviewer for every week.

## Why the rules are strict

The reader skims between classes and quits on any paragraph that does not pay them back. Every rule below came from a correction Ash made while rewriting the course by hand, or from his feedback on drafts (October 2026). Two tests carry the whole skill:

- **Would a 7th grader get this on the first read, and does this sentence add something?**
- **After this section, could a student new to the subject answer its heading in two or three sentences of their own, and take the first step today?**

## Who owns what

Ash decides what the course teaches and, for non-module pages, how the page is structured. This skill owns voice and form. Never invent a week plan, a statistic, a credential, a quote, or a real company's result. If an input is missing, ask.

## Before you write

1. **Read the course's own rules and story, when they exist.** For the Agriculture Edition they live in the Fuji repo under `ranges/udyaan/course/output/`: `how-ash-writes-the-course.md` (the rules), `ash-course-philosophy.md` (how Ash thinks), `a-to-b-outline.md` (every week and day), and the running student's fact sheet (`round-2/gia-canon.md`). **Ash's Week 1 page is the benchmark** for content and for where pictures sit: `output/week-1/Udyaan Week 1 Course Page/Udyaan Week 1.html`. A course page and this skill agree; where a course page is more specific, it wins. **When course files disagree,** the order is: the rules page, then the fact sheet, then the week's plan, then the outline. Follow the higher one and name the clash under Judgment calls. To read the benchmark HTML, pull out its text and note where each `<figure>` or `<svg>` sits between the paragraphs.
2. **Read `references/examples.md`** for a module, or `references/welcome-page.md` for any other page. Match their feel, not their words.
3. **Write the day's A-to-B before any sentence.** Five lines:
   - **The problem the student has when the day starts:** the one thing yesterday left unsolved, named sharply.
   - **The day's question:** the mini question that solves it, in words the student already knows.
   - **A → B:** what they have now, and what they'll have at the end.
   - **The running student's version:** how the worked-example student does today, and what surprises them.
   - **The deliverable:** the one thing saved in their doc that tomorrow uses.
4. **Pick the learning mode** that fits the A-to-B (see "The daily module" below).
5. **Check every fact you'll use against its source,** including the fact sheet's. Where the source says less or something else, follow the source and flag it under Judgment calls.
6. **Know what the course GPT does on this day:** its day card (for the Agriculture Edition, `Prompt for wN.md` in the week's folder) or, when there's none, what the days before it say the GPT does. The steps describe only what the GPT really returns.
7. **Take audience details from the course's spec, rules and examples only.** This skill holds no audience facts, so the same rules work for any course.

## Voice

Ash's newsletter voice with the edges filed down. The page sounds like a friendly senior who is also a student, talking in a corridor.

- **Peer, plain, spoken.** Use contractions. Say "figure out", "spot", "find", "try". Avoid "demystify", "identify", "leverage", "journey", "empower", "crucial", "optimize", and "link" for a stage of a chain.
- **Second person.** Talk to "you". Put the student's private doubts into "You may think..." or "If you study..." lines.
- **Plain words first.** When a technical word helps, give the plain words, then the term in brackets: "devices that talk to your phone (IoT)". **Explain every new word the first time it appears**, in one short phrase: "rewinding (the repair for a burnt motor)".
- **Every phrase stands on its own, seen from the customer's side.** A search phrase, a label or an example a stranger couldn't follow on the first read fails. "Farmer pump night electricity" fails; "why farmers water their fields at night" works, because the reader learns the fact as they read it.
- **Plain over brochure.** "Udyaan has your back" becomes "Udyaan helps you through it"; "the farmer's words do the heavy lifting" becomes "the farmer's words matter most".
- **Keep out** curses, war or military metaphors, and personal crisis stories. One light joke is welcome, usually near the author block. A pop-culture beat goes in only when Ash asks for one.
- **The author appears once,** in a short "Who am I?" block on a welcome page. Daily modules carry no author block.

## Questions lead, Shasta's way

- **Each week opens with one big question** the student is answering: "How do I find out if people want my solution, before I spend money on it?"
- **The day's title is the mini question** that gets them one step closer: "Day 6: Where Are Farmers Already Talking About My Problem?"
- **Every heading is the question the student would ask next** at that point: "Where do I find what they say?", "What do I type into the search bar?", "What do I ask the GPT?". The Do heading is an instruction with its time: "Collect what farmers say (40 minutes)". Tomorrow stays "Tomorrow".
- **Questions use words a newcomer already knows.** A course word (offer, quote, lead list) enters a question only after a day has taught it. "Do people want my offer?" fails on a student's first week; "Do people want my solution?" works.
- **Every question gets a full answer.** The section under a heading answers it so the student can say the answer back in two or three sentences and act today. A question the section raises gets answered right there, or cut. Nothing on the page needs a teacher in the room.
- **Answer the places students get stuck,** one line each, where they happen: "No 'Show transcript' button? Copy the comments only." "If the GPT says your paste is too long, download the tab and attach it."

## The daily module: fixed jobs, a shape that fits the day

Every module does these jobs, in this order. How much room each gets depends on the day's A-to-B. Details and the content structures behind each job are in `references/structure.md`.

| # | Job | What it does |
|---|---|---|
| 1 | **Title** | "Day N: <the day's question>" |
| 2 | **Recap and problem** | "Till now you have..." (what they made, named concretely), the problem it leaves, and **what ignoring it costs** in money or time. Then what today does, with the skill it builds woven in ("It builds evidence seeking: finding out what's true from the people who live it"). |
| 3 | **What you think** | The wrong belief or wrong move, what the student does because of it (bullets with real apps and places), and its impact. |
| 4 | **The right move** | The replacement idea, with a one-line plain definition. |
| 5 | **How it looks** | Examples: the simplest picture first, then the running student doing exactly this, step by step, including the GPT step and where they push back. |
| 6 | **Rule and picks** | The rule in bold, a Good pick and a Bad pick, each leading with the pick and then its impact. |
| 7 | **The Do** | One task with its time. Steps a student can't get stuck on, the exact GPT question, the named tab to save in, an Applied and an Excelled line, and a "Short on time?" line. |
| 8 | **Tomorrow** | What they have now, and the next problem in one line. |

Jobs 1, 2, 7 and 8 are in every module; use as much of 3 to 6 as the day needs. **Length follows the content: usually 900 to 1,800 words of prose,** not counting drawing notes. A day that also shows the running student step by step and serves two kinds of customer sits near the top of that range; cut words before you cut a step the student needs.

**The default order inside the day:** what you think → what it costs you → the right move → how it looks → do it. Bend it to the learning mode the A-to-B needs:

| Mode | Order | Use it for |
|---|---|---|
| **Rule first** | the rule → examples → yours | a tool they need fast |
| **Examples first** | examples → they spot the rule | an idea that sticks better found than told |
| **Options** | choices → they pick | no single right answer |
| **Go do it** | how it looks, step by step → they do the real thing | real-world work: collecting, outreach, calls |
| **Build it** | everything so far → one piece of work | the end of a week |

**Each day cascades:** it starts from yesterday's deliverable and ends with one concrete thing in their doc that tomorrow uses. The week map ("Your week, day by day"), a teach-back section, a "watch the example first" step and progress trackers belong to the page design, so the module leaves them out.

## Sentence rules

Each rule has bad and good pairs in `references/good-and-bad.md`. Read that file before drafting.

1. **Say it once, plainly.** No setup such as "one of two things happened", and no splitting one thought into two sentences.
2. **Every sentence adds a fact, an example, or an action.** Cut sentences that comment on the page ("All three are real"), label ("Both groups make the same error"), or reassure.
3. **Short words, short clauses, mixed lengths.** A long, flowing sentence sits next to a short one, because matched lengths read as machine-written. Use the plain word for the action: the week plan may say "red-team" or "audit", and the page says "poke holes in" or "check".
4. **Write full thoughts.** Skip fragments used for rhythm and one-word sentences.
5. **Put the impact in the claim's own sentence.** "The biggest problem is spoilage. A company can't open two new cities if a fifth of its fruit rots." The result follows the claim immediately.
6. **No lead-ins.** "Here's what it looks like", "Here's the thing", "Let's dive in", and "It's worth noting" are out. Write "For example:" or go straight into the point.
7. **No "not X, but Y", matched triplets, or em dashes.** State the point positively.
8. **Define a term in the sentence where it first appears,** in plain words. Course terms (Offer Document, Change Log) wait for the module that uses them.
9. **No claims about how many people do something.** "Most founders make two or three of these" and "almost every beginner" are invented statistics. State what happens to this student instead.
10. **Specific beats general.** "Search for startup ideas on YouTube and Instagram" beats "research the idea". To find the real behaviors for an opener, ask what this student would type, open, ask, or buy this week because of the belief.
11. **Count what you list, and keep numbers the same everywhere.** If you write "five mistakes", there are five. The time in the recap, the Do's heading and the steps match.
12. **Numbers are exact when the course has them.** Take them from Ash, the spec, or the fact sheet.

## Formatting rules

1. **Headings are the student's questions** (see "Questions lead"). Never a slot name ("Mistakes to avoid"), a label ("Five kinds of places hold your customers' words"), a clever line, or a claim about how many people do something.
2. **Bold carries the day.** Bold the one or two key phrases in every paragraph and list item, so **a student who reads only the bold gets the point of every section**. Never bold a whole sentence.
3. **Bullets for three or more parallel items.** Each opens with a bold phrase.
4. **Numbered lists for actions in order.**
5. **Block quotes** for labeled examples, templates, GPT questions and answers, and anything the student pastes or fills.
6. **One to three sentences per paragraph,** with white space between.
7. **No parenthetical side notes** and no "(made up)" labels. Short brackets for a technical term or a plain meaning are fine: "(IoT)", "(planned power cuts)". The one other exception is a single quiet offer on a welcome page.
8. **Pictures come after the words they explain.** One idea each, adding to the words, never as the first thing under a heading. Mark a picture's place in a draft with a block quote starting `**Drawing:**` that says what it shows.

## Examples

- **One running student carries the course,** introduced once on the welcome page and followed to the last day (Gia, in the Agriculture Edition). Never introduce them again. Say once, where they're introduced, that they and the people they talk to are made up and that quotes with a named source are real.
- **Their example shows exactly how to do the day,** step by step, so a student could copy it: what they typed, what the GPT said, where they pushed back, what they saved.
- **The example obeys the day's own rule.** Check it before you keep it: a problem sentence fits the template the day teaches, a check question asks about a real past time without stating the guess, a blocker is one a business could remove, an offer names a payer and a price.
- **Each example teaches a surprise** the student wouldn't have guessed: Gia finds farmers talk about burnt motors as much as night walks, and her offer only fixed the walk.
- **Every kind of customer the course serves appears every day,** in the places to look, the examples and the Do. In the Agriculture Edition that's farmers and agri entrepreneurs, because many students solve for the entrepreneur.
- **Other people get plain everyday names,** kept few, and the same name every time they appear.
- **The simplest example comes first,** in labeled lines. One idea per example, and a contrast pair carries the lesson.
- **Short examples are fresh every day.** The examples in `references/examples.md` show the shape and are not material to reuse. The running student's story is the one thread that repeats.
- **Real quotes only, copied exactly, mistakes and all,** cited as the person by place or role, the publication and the year ("a farmer in Belagavi district, The Better India, 2019"). Read the source carefully before using it: a cost a person paid before they fixed the problem is a "before" cost.
- **The running student's story may invent what it needs:** dialogue, times, small numbers in their own life. Mark an invented number as a Guess on the page and list it under Judgment calls. Numbers about the real world come from a source or from Ash.
- **Mistakes live inside examples and rules,** at the point they happen. There is no mistakes section.
- **Rules use one format:** the rule in bold, then "Good pick" and "Bad pick", each leading with the pick and then its impact.

## When the day's content is a list

Some days teach a list, such as five beginner mistakes or five offer lines. The list appears once, in bullets with a bold lead and one plain line each, and every item gets a concrete picture of what the student would do. Then pick one item and run it through a contrast pair. If a second list is tempting, add the missing detail to the first list instead.

## The Do

- **One task, time in the heading:** "Collect what farmers say (40 minutes)". The time comes from the week's plan; with none, match similar days and flag it.
- **Mechanical, low-effort steps.** Say exactly what to click and copy: "Select everything, copy it, paste it raw. Don't read it or tidy it; the GPT sorts it." Collecting is copying; checking one number is a pinpoint read ("press Ctrl+F, type the number, read the paragraphs around it"), which is fine.
- **The exact question to ask the GPT,** in a block quote with a slot for the student's problem: "What do farmers say about **[your problem]**?" The page says why the problem goes in the question.
- **A "how it looks" picture for any step with several parts:** the real screens (the YouTube transcript selected, the raw Google Doc tab, the GPT's answer). It sits in the running student's example just before the Do, or inside the Do; either way the Do's steps match it. Describe only screens you know: an interface detail you can't confirm goes under Judgment calls.
- **The tab to save in,** named.
- **Applied and Excelled,** one line each. Excelled needs proof from outside the chat: a quote, a photo, a real reply.
- **"Short on time?"** with a smaller version.

The GPT holds the case, the interview and the summary, so the lesson page holds none of them.

## Variation

The jobs and the voice stay fixed, and the wording changes so the course does not read like a template. **Vary both openings:** the recap line ("Till now you have...", "Yesterday you...", "Your Day 7 tab shows...", a one-line scene) and the hook in job 3. Never open two days in a row the same way, and use "Most people believe" at most once in a week. The catalogue, with the Dan Koe moves it comes from, is in `references/variation.md`.

## Before you show the draft

Self-review is not enough. Drafts that read as compliant still carried em dashes, asides and fragments, so the check is mechanical first.

1. **Save the draft to a scratch file** (the session scratchpad, not the project), from the title to the last line.
2. **Run the linter** and fix every `[FIX]` line:
   - Daily module: `python -I <this skill's base directory>/scripts/lint_module.py <draft.md>`
   - Welcome page, week opener or other page: add `--type page`
3. **Look at every `[REVIEW]` line** and either change it or decide it is fine.
4. **Re-run until it prints PASS**, or until only reviewed items remain.
5. **Then the judgment checks the linter can't do:**
   - **Full answers:** cover everything but one section and its heading; could a newcomer answer the heading and act today?
   - **Cascade:** does the day start from yesterday's deliverable and name what ignoring the problem costs? Does it end with one thing tomorrow uses?
   - **The example:** does it obey the day's own rule, show every step including the GPT, and teach a surprise? Is it consistent with the fact sheet?
   - **Every customer type** in the places, the examples and the Do?
   - **Plain words:** every new word explained the first time, every phrase clear on its own, no brochure lines?
   - **Bold:** reading only the bold, do you get each section's point?
   - **Numbers and names:** the same everywhere, and every number, name and quote from Ash, the spec, the fact sheet, or a cited source?

## How to deliver

1. **One module:** your final reply is the page itself, starting with the title line. Draft in chat, and save a course file only when Ash says to.
2. **A whole week or more:** files, a plan and a fresh review, as `references/write-a-week.md` says.
3. **After the draft, a "Judgment calls" heading** with a few plain bullets: anything chosen without being told, such as an invented example, a trigger word, or a number. Plain words only; no internal terms.
4. **When Ash corrects something,** apply it, then add a dated line under Refinements and bump the version.

## References

- `references/write-a-week.md`: writing a whole week or more: the plan, the fact sheet, writers and fresh reviewers, and the consistency pass.
- `references/structure.md`: the module's jobs in detail, the learning modes, and the content structures inside them.
- `references/good-and-bad.md`: bad and good pairs for every rule, including round 2's corrections.
- `references/variation.md`: how to keep modules fresh, with Dan Koe moves.
- `references/examples.md`: approved Days 1 to 3, and Day 6 in the question-led shape.
- `references/welcome-page.md`: the approved welcome page and the rules for non-module pages.
- `references/legacy-passages.md`: two older voice samples, used for tone only.
- `scripts/lint_module.py`: mechanical check for banned patterns, run before every draft is shown.

## Refinements

- 2026-10-30 v8.1: A cold test (a fresh agent writing Week 2 Day 8 from this skill alone) passed the linter and reached the right surprise, and named 13 places it guessed. Added: the order among course files, checking facts against their sources, where the GPT's behaviour comes from, a 900 to 1,800 word range, varying both openings, invented numbers in the running student's story marked Guess, pinpoint reads, where the Do's picture sits, the Do's time, and the citation form. The linter now splits sentences after a closing quote.
- 2026-10-30 v8: Built from Ash's feedback on the round 1 drafts of Weeks 2 to 6 and the round 2 rewrite (Fuji: `ranges/udyaan/course/output/copywriting-changes.md`). Headings are now the student's questions, with a big question per week and a question per day, in words a newcomer knows. Every question gets a full answer (Shasta's rule). Each day is written from an A-to-B, cascades from yesterday's deliverable and names the cost of the problem. The skeleton became fixed jobs with a shape chosen by learning mode. One running student carries the course and their example must obey the day's rule and teach a surprise. Steps are mechanical (copy everything raw, the GPT sorts it), the exact GPT question carries the student's problem, and multi-step Dos get "how it looks" pictures. Bold carries every section. The week map and teach-back left the module. Added `references/write-a-week.md` and Day 6 to the examples; the linter drops the week map and flags label headings.
- 2026-10-12 v7: Ash dropped the "To test it, ask" lines from the Day 2 rules. A rule is shown by its bold statement and its good and bad picks only. A day with two kinds of student (has a problem, has none) gives the no-problem student the most room. Openers on belief days use "might" and "may".
- 2026-10-12 v6: Ash banned the word "link" for parts of the agriculture chain. Say "stage" instead, and keep "link" only for web links.
- 2026-10-12 v5: Merged course-page-writer into this skill. Module rules take precedence where they conflict.
- 2026-10-12 v4: Added lint checks for section order and question-only sections after a test run.
- 2026-10-12 v3: Added the list-once rule, plain-word rule, heading rule and final-reply rule.
- 2026-10-12 v2: Added the lint script, delivery steps, fresh-example and working-model rules.
- 2026-10-12 v1: Built from Ash's rewrites of Days 1 to 3, the Dan Koe course, and Nicolas Cole's five-part module framework.
