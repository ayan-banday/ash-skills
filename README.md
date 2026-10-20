# ash-skills

Ash's Claude skills, packed into plugins by action. You type `/plugin:skill`, like `/plan:chart-project-wayfinder`.

| Plugin | The question it answers | Status |
|---|---|---|
| `plan` | How do I decide what to build before building it? | **Built (pilot)** |
| `write` | How do I write words people read, and docs Claude reads? | Next |
| `visualize` | How do I show an idea so people get it without reading much? | Next |
| `build` | How do I build and fix code in Charlotte or the micro-SaaS? | Next |
| `learn` | How do I learn a topic, or make sense of a pile of files? | Next |

## How a skill is named

- **Name:** what it does, as a verb and an object: `write-spec`, `try-prototype`.
- **Description starts with a bracket**, then the question it answers: `(Matt: to-spec) How do I turn what we just decided into one written plan?` The bracket says who it's for or where it came from. Claude Code shows this line next to the name when you type `/`.

## How to add a skill

1. Make a folder `plugins/<plugin>/skills/<skill-name>/` with a `SKILL.md`.
2. Start its description with the bracket and the question.
3. Bump `version` in `plugins/<plugin>/.claude-plugin/plugin.json`, then run `claude plugin update <plugin>@ash-skills`.

## How to add a plugin

1. Copy `plugins/plan/` as a template and rename it.
2. Add it to `.claude-plugin/marketplace.json`.
3. Run `claude plugin install <plugin>@ash-skills`.

## Credits

Skills marked `(Matt: ...)` are copied from Matt Pocock's skills (https://github.com/mattpocock/skills, MIT licence, see `plugins/plan/LICENSE-matt-pocock`) and renamed. They no longer receive his updates.
