# How Ash's skills are made

The one rulebook for every skill in this repo. `/build:make-skill` reads it before it names, writes or fixes a skill. Change a rule here and every new skill follows it.

## Which plugin a skill goes in: the action you're in when you need it

| Plugin | You're in it when you... | Its question |
|---|---|---|
| `write` | write words people or agents read: posts, course pages, docs, prompts | How do I write words people read, and docs Claude reads? |
| `visualize` | show an idea visually: pages, diagrams, decks, stories | How do I show an idea so people get it without reading much? |
| `plan` | decide what to build before building it | How do I decide what to build before building it? |
| `build` | build and fix code, and the tools Claude uses (skills, hooks, plugins) | How do I build and fix code in Charlotte or the micro-SaaS, and the tools Claude uses? |
| `learn` | study a topic, or make sense of a pile of files or skills | How do I learn a topic, or make sense of a pile of files? |

**Pick by the moment Ash needs it.** A skill that writes a study page is `visualize` if it draws the page and `learn` if it runs the study session. When two fit, pick the one where Ash would go looking first.

**A sixth plugin needs three skills that fit none of these.** Until then, file the skill in the closest one.

## The name: what it does, then the tag in round brackets

Ash finds skills by typing words of the name in the `/` menu (see "How Ash finds a skill"). So **every word he'd search for goes in the name.**

**The pattern** (confirmed by Ash on 2026-10-20; change it here and nowhere else):

> folder: `<what-it-does>` · `name: "<what-it-does> (<tag>)"`

The menu then shows `/visualize:brief-page (udyaan)`, and Ash types `/visualize:brief-page`.

- **What it does:** a verb and an object, saying what it makes: `write-spec`, `try-prototype`, `brief-page`. Start with a verb Ash would say out loud: write, make, try, split, grill, chart, ask, draw, check. This is the folder name and the command.
- **The tag, in round brackets after it:** one lowercase word for who it's for or where it came from: `udyaan`, `shasta`, `substack`, `matt`. It never goes in the folder name.
- **A memorable original name stays in the name:** `chart-project-wayfinder (matt)`, from Matt's `wayfinder`, so `/wayf` finds it.
- **No tag when nothing fits:** then `name:` is just the folder name, with no brackets: `story-plan`, `which-skill`, `make-skill`.

**Examples:** `/plan:chart-project-wayfinder (matt)`, `/visualize:brief-page (udyaan)`, `/write:headline-angles (substack)`, `/learn:study (shasta)`.

**Also:**
- **Lowercase words joined by hyphens,** at most 64 characters. Aim for four words or fewer.
- **Quote the `name:` line** when it has brackets, so YAML reads it as one string.
- **No two skills share a folder name,** across all five plugins. Check with the listing command under "Shipping".
- **Links between skills use the folder name:** `/plan:grilling`, `../grilling/`, never the bracketed name.

**Bad:** `wayfinder` (no verb), `domain-modeling` (names a field, with no verb), `brief-page-udyaan` (the tag is in the folder name).
**Good:** `chart-project-wayfinder (matt)`, `brief-page (udyaan)`, `make-skill`.

## The description: four parts, in this order

Written as one YAML line in double quotes. Use single quotes inside it.

1. **A square bracket, only when it adds something the name's tag doesn't:** what kind of skill it is or what it leans on. It shows at the start of the hover card.
   - `[helper]` for a skill other skills call, `[course]` or `[website]` for what it makes, `[skill maker · uses skill-creator]` for one that leans on another skill.
   - **Never repeat the tag.** `(matt)` is already in the name, so no `[Matt]`.
   - **No old names.** A renamed skill drops what it used to be called; git history keeps it.
   - **Nothing to add, no bracket.** The description starts straight with its question.
2. **The question it answers, in Ash's voice.** Usually "How do I ...?". "Which", "Where" or "What" are fine when they read more naturally.
   - **It names the topic and the situation,** so it makes sense read alone, with the skill name hidden.
   - Bad: "How do I plan it?" / "How do I get unstuck?"
   - Good: "How do I plan a project too big for one session when I can't see the route yet?"
   - **Why:** Ash scans the `/` menu by these questions. A vague one could sit under a hundred skills, so it tells him nothing.
   - Source: the "Questions" rules in `D:\Shasta\_rules\Menus and Learning Briefs.md` and "Headings" in `D:\Shasta\_rules\Clusters.md`.
3. **One sentence on what it does,** naming the thing it produces. "Breaks a spec into thin tickets, each naming what blocks it."
4. **When to reach for it.** Only for skills Claude can fire on its own (see "Who can start it"):
   - **The trigger phrases,** one per distinct case: "Use when Ash says 'make a skill', 'turn this into a skill', or 'fix this skill's name'."
   - **The look-alike line,** when another skill sounds similar: "Use instead of skill-creator for Ash's own skills."
   - For a skill only Ash types, keep the look-alike line and drop the trigger list.

**Length:** aim for **200 to 450 characters**. The skill listing cuts the description (plus `when_to_use`, if set) at **1,536 characters**, and every word costs context in every session for skills Claude can fire.

**Full example:**

```yaml
name: "write-spec (matt)"
description: "How do I turn what we just decided into one written plan? Turns the current conversation into a spec and publishes it to the project's issue tracker. No interview, just what was already discussed."
```

## Who can start it: Claude, or only Ash

- **Claude can fire it** (no `disable-model-invocation`): when Ash's words should start it without the slash command, or another skill calls it. Its description must carry the trigger phrases.
- **Only Ash types it** (`disable-model-invocation: true`): when it should run only on purpose, like a one-time setup or a long interview. It costs nothing in context, but Ash has to remember it, which is what `/learn:which-skill` is for.

**Default to "only Ash types it"**, except when the skill has a real trigger phrase Ash says in chat, or another skill calls it.

## How Ash finds a skill (from the Claude Code docs)

- **The `/` menu matches the name only,** from the start of the name or of any word in it. Typing `/wayf` finds `chart-project-wayfinder`. The description shows beside the name, and the menu picks its top match from names.
- **The plugin name counts too.** Typing `/plan` lists every plan skill.
- **`/skills` doesn't work in Ash's app,** so description words are never a way to find a skill. The docs say `/skills` filters by name, description and source, but Ash can't use it.
- **Skills can't have aliases.** The name is the only handle in the `/` menu, so it carries every word Ash would type.
- **The full name is `/plugin:skill`,** like `/plan:write-spec`.
- **What the menu row shows:** `plugin:` plus the `name:` line. The folder sets the command Ash types. A plain `name:` also shows again in round brackets as a short alias (`/build:make-skill (make-skill)`). A `name:` with a bracketed tag shows as written: `/visualize:brief-page (udyaan)`, tested by Ash on 2026-10-20.
- **The `name:` line is the folder name, plus ` (<tag>)` when there is one.** Anything else makes the menu show one name while the command runs under another.

## Writing the body (from Matt Pocock's writing-for-agents rules)

The body is read by Claude, so it follows these rules. Anything the skill says to Ash follows Ash's style: plain words, short sentences, bold key phrases, no em dashes, no "not X but Y".

**What goes where**
- **Steps first:** what Claude does, in order. Each step ends on a **done test** Claude can check: "every skill listed with its plugin" beats "understand the skills".
- **Reference next:** rules and facts Claude looks up while working. Keep each idea's definition, rules and caveats under one heading.
- **Push the rest into a sibling file,** linked by one line that says when to open it. Inline what every run needs; move out what only some runs need. A long body thins Claude's attention across every line.

**Pointers that fire**
- **A description is a pointer:** it says what the material is and the cases that should reach it. Put the leading word first. One trigger phrase per distinct case; synonyms for the same case are one case.
- **A line that names another file works the same way.** If Claude skips a file it needs, sharpen the line before you paste the file in.

**Words that steer**
- **Use a leading word:** one compact word the model already knows (_tracer bullet_, _frontier_, _relentless_) instead of a sentence describing it. Repeat the word and skip the explanation.
- **Say what to do.** "Write one-line comments" beats "don't write long comments": a ban puts the banned thing in Claude's head. Keep a ban only as a hard guardrail, paired with the thing to do instead.

**Cutting**
- **One source of truth.** Each rule lives in one place; other files point to it. This file is that place for naming.
- **Point at the environment instead of copying it.** Name the command or file Claude can read (`claude plugin --help`, the folder layout). Write down only what Claude can't find by looking: the reason behind a choice, the gotcha.
- **Delete no-ops:** any sentence Claude would obey anyway. Delete the whole sentence.

## Saving and shipping a skill

**Files**
- **Edit the repo, never the installed copy.** The repo is `D:\ash-skills`. Installed copies under `~/.claude/plugins/cache/` are overwritten on update.
- **Folder:** `plugins/<plugin>/skills/<what-it-does>/SKILL.md`. `name:` is the folder name, plus ` (<tag>)` when there is one.
- **Copied skills keep their licence** in the plugin folder (like `plugins/plan/LICENSE-matt-pocock`) and their credit in README.md.

**A new plugin**
- Create `plugins/<plugin>/.claude-plugin/plugin.json` with `name`, `version: "0.1.0"`, `description` (its question from the table above) and `author: {"name": "Ash Banday"}`.
- Add it to `.claude-plugin/marketplace.json` with `name`, `source: "./plugins/<plugin>"` and its question as `description`.
- Mark it built in the README plugin table.

**Versions:** a new skill bumps the minor number (0.1.0 to 0.2.0). A fixed name, description or body bumps the last number (0.2.0 to 0.2.1).

**Load it, check it, commit it** (run from `D:\ash-skills`):

```bash
claude plugin validate .
claude plugin marketplace update ash-skills
claude plugin install <plugin>@ash-skills
claude plugin update <plugin>@ash-skills
claude plugin details <plugin>@ash-skills
```

- `install` for a new plugin, `update` for one already installed.
- **Bump the version on every change.** Sessions load a copy in `~/.claude/plugins/cache/ash-skills/<plugin>/<version>/`, and `update` refreshes that copy only when the version went up. Tested 2026-10-20: an edit with no bump stayed out of the copy, even though the docs say local plugins reload without one.
- `details` must list the skill. Then commit only the files this skill touched, by name.
- **Then `git push`.** The repo is `github.com/ayan-banday/ash-skills` (private). This laptop reads `D:sh-skills` directly; cloud sessions and other laptops install from GitHub through each repo's `.claude/settings.json`, so an unpushed skill exists only here.
- **The skill appears in sessions started after the update,** or after `/reload-plugins` in an open session.

**List every skill and its description** (for name clashes and look-alikes):

```bash
grep -H -E '^(name|description|disable-model-invocation):' D:/ash-skills/plugins/*/skills/*/SKILL.md
```
