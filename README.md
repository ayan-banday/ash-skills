# ash-skills

Ash's Claude skills, packed into five plugins by the action you're in. **Type `/` and the plugin to see its skills:** `/write`, `/visualize`, `/plan`, `/build`, `/learn`. Any word in a name finds it too: `/udyaan`, `/matt`, `/wayfinder`.

- **Make a new skill:** `/build:make-skill`. It follows [CONVENTIONS.md](CONVENTIONS.md) and files the skill in the right plugin.
- **Not sure which skill:** `/learn:which-skill`, then say what you're doing.
- **New or changed skills show up** in sessions started after the install, or after `/reload-plugins`.

## /write: How do I write words people read, and docs Claude reads?

| Skill | Was | The question it answers |
|---|---|---|
| `course-lesson (udyaan)` | course-writer | How do I write a Day N lesson or course page students actually read? |
| `headline-angles (substack)` | newsletter-headlines | How do I find the headline that makes people open my Substack post? |
| `re-explain (matt)` | Matt: wait-what | How do I get Claude to re-explain a reply that didn't make sense? |
| `agent-docs (matt)` | Matt: writing-for-agents | How do I write a skill or CLAUDE.md that Claude follows every time? |

## /visualize: How do I show an idea so people get it without reading much?

| Skill | Was | The question it answers |
|---|---|---|
| `story-plan` | visual-storytelling | How do I turn an abstract idea into a story people watch? |
| `polished-doc` | clear-documents | How do I turn my draft into a clean PDF or Word file? |
| `brief-page (udyaan)` | clear-visual-html | How do I brief a teammate so they arrive knowing what we're deciding? |
| `pitch-site (udyaan)` | clear-proposal-site | How do I make an outside reader say "Hell yeah, let's do this"? |
| `post-page-online` | new | How do I put a page I made online so friends outside Claude can open it? |

**Making a desktop page work on phones:** follow [docs/mobile-site-playbook.md](docs/mobile-site-playbook.md), the steps and decisions from the TVS page.

**Which one?** A draft you hand over as a file: `polished-doc`. Notes a teammate must understand alone: `brief-page`. An outsider must say yes: `pitch-site`. Abstract or list-like: `story-plan` first. Finished and should be seen outside Claude: `post-page-online`.

## /plan: How do I decide what to build before building it?

| Skill | Was | The question it answers |
|---|---|---|
| `grill-idea (matt)` | Matt: grill-me | How do I find the holes in an idea before I commit to it? |
| `grill-with-docs (matt)` | Matt: grill-with-docs | How do I sharpen a feature and keep a record of what we decided? |
| `chart-project-wayfinder (matt)` | Matt: wayfinder | How do I plan a project too big for one session when I can't see the route yet? |
| `write-spec (matt)` | Matt: to-spec | How do I turn what we just decided into one written plan? |
| `split-tickets (matt)` | Matt: to-tickets | How do I split a spec into tasks Claude can build one at a time? |
| `setup-tracker (matt)` | Matt: setup-matt-pocock-skills | Where should my plans and tickets be saved? (once per repo) |
| `try-prototype (matt)` | Matt: prototype | How do I test whether a design feels right before building it properly? |
| `gather-facts (matt)` | Matt: research | How do I get facts checked against official sources while I keep working? |
| `ask-someone (matt)` | Matt: to-questionnaire | How do I get an answer that's in someone else's head? |
| `grilling`, `domain-modeling` | Matt helpers | Loaded by the skills above; you don't type them. |

## /build: How do I build and fix code, and the tools Claude uses?

| Skill | Was | The question it answers |
|---|---|---|
| `build-ticket (matt)` | Matt: implement | How do I get one decided ticket built without Claude redesigning it? |
| `build-whole-spec (matt)` | Matt: implement-spec | How do I build a whole spec at once with several helpers? |
| `test-first (matt)` | Matt: tdd | How do I build a feature so tests prove it works? |
| `find-bug (matt)` | Matt: diagnosing-bugs | How do I find the real cause of a bug instead of guessing? |
| `review-code (matt)` | Matt: code-review | How do I check changes before merging them? |
| `find-simplifications (matt)` | Matt: improve-codebase-architecture | How do I find parts of the code that are more complicated than they need to be? |
| `setup-walkthrough (matt)` | Matt: wizard | How do I get through setup steps only I can do, like pasting API keys? |
| `write-pr (matt)` | Matt: pr | How do I write a pull request someone can review fast? |
| `improve-next-time (matt)` | Matt: retro | How do I make the next build go smoother than this one? |
| `handoff (matt)` | Matt: handoff | How do I move this work to a new folder, tool or person? |
| `make-skill` | new | How do I make a new skill that lands in the right plugin with a clear name? |
| `codebase-design (matt)` | Matt helper | Loaded by test-first and find-simplifications. |

## /learn: How do I learn a topic, or make sense of a pile of files?

| Skill | Was | The question it answers |
|---|---|---|
| `study (shasta)` | study | How do I learn a topic the Shasta way? |
| `graphify` | graphify | How do I see how everything in a folder connects? |
| `which-skill` | new | Which of my skills should I use right now? |

## Not here

- **Still installed separately:** jmo-workflow (better-ui, animate, interview, ste, agentation, codex), frontend-design in Charlotte, and Anthropic's skills (pdf, docx, pptx, xlsx, skill-creator).
- **Left out of Matt's set:** ask-matt (which-skill replaces it), triage, teach (study covers it).
- **Later:** `post-draft-substack`, once three or four posts exist for it to learn your voice from.

## On your phone and in cloud sessions

Cloud sessions don't install plugins from a repo's settings, so a cloud environment's setup script does it. **Paste this once** into the environment's **Setup script** (claude.ai/code → environment selector under the message box → edit), and pick that environment for new sessions:

```bash
#!/bin/bash
claude plugin marketplace add ayan-banday/ash-skills || claude plugin marketplace update ash-skills
bash "$HOME/.claude/plugins/marketplaces/ash-skills/cloud/setup.sh" || echo "ash-skills: setup failed"
exit 0
```

- **The real work is in [cloud/setup.sh](cloud/setup.sh),** so changes there need no new paste. It installs every plugin and tells Claude where to find a skill that didn't load.
- **A skill pushed today can lag up to about 7 days,** because cloud environments cache the setup. Until then, ask for it by name: Claude pulls this repo and reads the skill's SKILL.md.

## How this repo is built

- **The rules:** [CONVENTIONS.md](CONVENTIONS.md). **The plan it was built from:** [docs/BUILD-PLAN.md](docs/BUILD-PLAN.md).
- **`docs/build_all.py` ran once,** on 2026-10-20, to copy and rename every skill. **Don't run it again:** the skills here are now the master copies, and a re-run would overwrite edits made since. Edit skills here, or with `/build:make-skill`.

## Credits

Skills ending in `-matt` are copied from Matt Pocock's skills (https://github.com/mattpocock/skills, MIT licence, see `LICENSE-matt-pocock` in each plugin) and renamed. They no longer receive his updates.
