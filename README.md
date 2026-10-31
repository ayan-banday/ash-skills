# ash-skills

**Claude Code skills for people who build with AI every day and want the result to be clear, simple and right.** Ash Banday made them while running Udyaan, an agriculture startup program for students, and building his own tools with Claude. They come in five plugins, one for each moment you're in: writing, showing, planning, building or learning.

**Every skill is named for what it does and described by the question it answers.** If the question sounds like your problem, that's the skill.

## Install

In Claude Code:

```bash
claude plugin marketplace add ayan-banday/ash-skills
claude plugin install plan@ash-skills    # or write, visualize, build, learn
```

Then type `/` and a plugin's name to see its skills: `/write`, `/visualize`, `/plan`, `/build`, `/learn`. Any word in a skill's name finds it too: `/design`, `/grill`, `/prototype`. New or updated skills show up in sessions started after the install, or after `/reload-plugins`.

## How to read a skill's name

- **The command is `/plugin:skill`,** like `/plan:design-like-expert`.
- **A word in brackets says where the skill came from or who it's tuned for.** The skill still works elsewhere; read those names as examples.
  - **(matt):** copied from [Matt Pocock's skills](https://github.com/mattpocock/skills) and renamed.
  - **(udyaan):** tuned for Udyaan's brand, students and team.
  - **(shasta):** tuned for Shasta, Ash's learning library.
  - **(substack):** tuned for writing a Substack newsletter.
- **A helper** is loaded by other skills. You don't type it.
- **Some skills Claude starts on its own** when your words match them. The rest run only when you type them, because they're long or meant to run on purpose.

## Where to start

| You want to… | Type |
|---|---|
| Get the design a ten-year expert would make, and learn why it works | `/plan:design-like-expert` |
| Find the holes in an idea before you commit to it | `/plan:grill-idea` |
| Learn the field behind what you're building, while agents build | `/learn:teach-side-chat` |
| Make an outside reader say yes to a proposal | `/visualize:pitch-site` |
| Turn a messy draft into a clean PDF | `/visualize:polished-doc` |
| Find the real cause of a bug | `/build:find-bug` |
| Not sure | `/learn:which-skill`, then say what you're doing |

## /write: How do I write words people read, and docs Claude reads?

**The problem:** AI drafts sound like AI. They hedge, pad and name things before saying what they mean, so people skim them. Agents skip rules buried in long docs too. These skills write plain words people finish and docs agents follow.

| Skill | The problem it solves | What you get |
|---|---|---|
| `course-lesson (udyaan)` | How do I write a Day N lesson or course page students actually read? | Lessons in a plain, spoken voice. Each day moves the student one step, follows one running student as the example, and ends in one small task. It can also run a whole week past fresh reviewers. |
| `headline-angles (substack)` | How do I find the headline that makes people open my Substack post? | 10 headline and subheadline angles, ranked, built from your idea and your reader's fear and wanted outcome. |
| `re-explain (matt)` | How do I get Claude to re-explain a reply that didn't make sense? | Claude stops and pitches its last message again, more simply. |
| `agent-docs (matt)` | How do I write a skill or CLAUDE.md that Claude follows every time? | The rules for writing for agents: steps with done tests, pointers that fire, and cutting what Claude would do anyway. |

## /visualize: How do I show an idea so people get it without reading much?

**The problem:** most people won't read a wall of text, even a good one. These skills turn ideas into pages, documents and stories people get at a glance, and each one suits a different reader.

| Skill | The problem it solves | What you get |
|---|---|---|
| `story-plan` | How do I turn an abstract idea into a story people watch? | A thesis, a living metaphor and a storyboard checked by a script, ready for another skill to build. |
| `polished-doc` | How do I turn my draft into a clean PDF or Word file? | Your draft rewritten clearer, with the same structure and visuals only where they explain faster, exported as PDF, Word, Google Docs or HTML. |
| `brief-page (udyaan)` | How do I brief a teammate so they arrive knowing what we're deciding? | A page a teammate reads alone. Every heading is the question they'd ask, and every answer is drawn as well as written. |
| `pitch-site (udyaan)` | How do I make an outside reader say "Hell yeah, let's do this"? | A one-file proposal website for readers who won't read, with a phone version, ending in one concrete ask. |
| `post-page-online` | How do I put a page I made online so friends outside Claude can open it? | Your page tested in a browser, published to GitHub Pages, and its public link. |

**Which one?** A draft you hand over as a file: `polished-doc`. Notes a teammate must understand alone: `brief-page`. An outsider must say yes: `pitch-site`. An abstract or list-like idea: `story-plan` first. Finished and should be seen outside Claude: `post-page-online`. To make a desktop page work on phones, follow [docs/mobile-site-playbook.md](docs/mobile-site-playbook.md).

## /plan: How do I decide what to build before building it?

**The problem:** with AI, building is fast and cheap, so the costly mistakes happen before the build. You solve the wrong problem, leave a decision unchecked, or start a plan too big for one session. These skills settle what to build first.

| Skill | The problem it solves | What you get |
|---|---|---|
| `design-like-expert` | How do I get the design a ten-year expert would make, and learn why it works? | Claude works out which experts your goal needs and lists the big problems in your chat. For the one you pick, it designs the smallest solution that fully works: the root cause, the idea and its name, the thing itself drawn out, what's left out, when it stops working, and only the calls that are yours. |
| `grill-idea (matt)` | How do I find the holes in an idea before I commit to it? | A relentless interview, in rounds, with a recommended answer for every question. |
| `grill-with-docs (matt)` | How do I sharpen a feature and keep a record of what we decided? | The same interview, plus a glossary and decision records written as you go. |
| `chart-project-wayfinder (matt)` | How do I plan a project too big for one session when I can't see the route yet? | A map of decision tickets on your issue tracker, worked one at a time until the way is clear. |
| `write-spec (matt)` | How do I turn what we just decided into one written plan? | A spec built from the conversation, with no new interview, published to your tracker. |
| `split-tickets (matt)` | How do I split a spec into tasks Claude can build one at a time? | Thin end-to-end tickets, each naming what blocks it. |
| `try-prototype (matt)` | How do I test whether a design feels right before building it properly? | A throwaway prototype: a clickable logic demo, or several very different versions of a screen. |
| `gather-facts (matt)` | How do I get facts checked against official sources while I keep working? | A background agent that reads primary sources and saves what it finds to a file. |
| `ask-someone (matt)` | How do I get an answer that's in someone else's head? | A questionnaire aimed at what they know and you don't. |
| `setup-tracker (matt)` | Where should my plans and tickets be saved? | One-time setup of your repo's issue tracker and labels, for the skills that use it. |
| `grilling`, `domain-modeling` | Helpers | The question engine and the glossary keeper behind the grilling skills. |

**Which one?** You want Claude to do the thinking and show you the best design: `design-like-expert`. You want to be questioned until your own plan holds up: `grill-idea`. The plan is decided and needs writing down: `write-spec`. It's too big for one session: `chart-project-wayfinder`.

## /build: How do I build and fix code, and the tools Claude uses?

**The problem:** agents write code fast, and they redesign things nobody asked them to. These skills keep a build to what was decided, prove it works with tests, and find the real cause when something breaks.

| Skill | The problem it solves | What you get |
|---|---|---|
| `build-ticket (matt)` | How do I get one decided ticket built without Claude redesigning it? | One ticket built as specified. |
| `build-whole-spec (matt)` | How do I build a whole spec at once with several helpers? | A spec's tickets built by several agents. |
| `test-first (matt)` | How do I build a feature so tests prove it works? | Red, green, refactor: a failing test first, then the code that passes it. |
| `find-bug (matt)` | How do I find the real cause of a bug instead of guessing? | A diagnosis loop for hard bugs and slowdowns. |
| `review-code (matt)` | How do I check changes before merging them? | Two reviews side by side: does the code follow the repo's standards, and does it do what the spec asked? |
| `find-simplifications (matt)` | How do I find parts of the code that are more complicated than they need to be? | A visual report of places to simplify, then a grilling on the one you pick. |
| `setup-walkthrough (matt)` | How do I get through setup steps only I can do, like pasting API keys? | An interactive script that walks you through each manual step. |
| `write-pr (matt)` | How do I write a pull request someone can review fast? | A pull request description written to be reviewed quickly. |
| `improve-next-time (matt)` | How do I make the next build go smoother than this one? | A short look back at the session and what to change. |
| `handoff (matt)` | How do I move this work to a new folder, tool or person? | A handoff document another agent can pick up from. |
| `make-skill` | How do I make a new skill that lands in the right plugin with a clear name? | A skill named, written, tested and shipped by this repo's [CONVENTIONS.md](CONVENTIONS.md). |
| `codebase-design (matt)` | Helper | Shared words for shaping code into simple, deep parts. |

## /learn: How do I learn a topic, or make sense of a pile of files?

**The problem:** when you build with AI every day, you can ship in a field you don't understand without knowing what you're missing. These skills turn the work you're already doing into learning.

| Skill | The problem it solves | What you get |
|---|---|---|
| `teach-side-chat (shasta)` | How do I learn the field behind what I'm building, while agents work beside me? | A menu of the big problems in your chat, then a short chapter from a ten-year expert on the one you pick. |
| `study (shasta)` | How do I learn a topic the Shasta way? | An evening from your first question to an approved learning brief, then a study page. |
| `break-into-field (shasta)` | How do I break into a whole field I know nothing about, starting from a real problem in my work? | A study book: a map of the field's problems in the order they unlock, and chapters that each solve one. |
| `graphify` | How do I see how everything in a folder connects? | A knowledge graph of any folder, from code and docs to papers and videos, that you can query. |
| `which-skill` | Which of my skills should I use right now? | The one command to type for what you're doing, with one line of why. |

**Which one?** Learn from the chat you're in: `teach-side-chat`. A topic you choose: `study`. A whole field: `break-into-field`.

## Using these in Claude Code on the web

Cloud sessions don't install plugins from a repo's settings, so an environment's setup script does it. Paste this into the environment's **Setup script** (claude.ai/code → the environment selector under the message box → edit):

```bash
#!/bin/bash
claude plugin marketplace add ayan-banday/ash-skills || claude plugin marketplace update ash-skills
bash "$HOME/.claude/plugins/marketplaces/ash-skills/cloud/setup.sh" || echo "ash-skills: setup failed"
exit 0
```

- **The real work is in [cloud/setup.sh](cloud/setup.sh),** so changes there need no new paste. It installs every plugin and tells Claude where to find a skill that didn't load. It also holds lines for Ash's own private repos; copy it and remove those for your own setup.
- **A skill pushed today can take up to about 7 days to reach cloud sessions,** because environments cache the setup. Until then, ask for the skill by name: Claude pulls this repo and reads its SKILL.md.

## How this repo is built

- **Every rule for naming, describing, writing and shipping a skill** is in [CONVENTIONS.md](CONVENTIONS.md). `/build:make-skill` follows it.
- **The skills here are the master copies.** `docs/build_all.py` ran once, on 2026-10-20, to copy and rename them. Running it again would overwrite every edit since.

## Credits

Skills tagged `(matt)` are copied from Matt Pocock's skills (https://github.com/mattpocock/skills, MIT licence, see `LICENSE-matt-pocock` in each plugin) and renamed. They no longer receive his updates. `design-like-expert` borrows its "smallest change that fully works" ladder from [ponytail](https://github.com/dietrichgebert/ponytail) (MIT).
