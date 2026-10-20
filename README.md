# ash-skills

Ash's Claude skills, packed into plugins by action. You type `/plugin:skill`, like `/plan:chart-project-wayfinder`.

| Plugin | The question it answers | Status |
|---|---|---|
| `plan` | How do I decide what to build before building it? | **Built (pilot)** |
| `write` | How do I write words people read, and docs Claude reads? | Next |
| `visualize` | How do I show an idea so people get it without reading much? | Next |
| `build` | How do I build and fix code in Charlotte or the micro-SaaS, and the tools Claude uses? | Started: `make-skill` |
| `learn` | How do I learn a topic, or make sense of a pile of files? | Started: `which-skill` |

## How a skill is named

- **Name:** what it does, as a verb and an object: `write-spec`, `try-prototype`.
- **Description starts with a bracket**, then the question it answers: `(Matt: to-spec) How do I turn what we just decided into one written plan?` The bracket says who it's for or where it came from. Claude Code shows this line next to the name when you type `/`.
- **The full rules live in [CONVENTIONS.md](CONVENTIONS.md):** which plugin, the name, the four parts of a description, the body, and shipping.

## How to add a skill

**Type `/build:make-skill`** and say what the skill is for. It reads [CONVENTIONS.md](CONVENTIONS.md), picks the plugin, name, bracket and question, and shows them in one line for your yes. Then it drafts the skill, tests it, bumps the plugin version, installs it and commits.

- **To fix a skill's name or description,** type `/build:make-skill` and name the skill.
- **Not sure a skill exists already?** Type `/learn:which-skill` and say what you're doing.
- **New skills show up in sessions started after the install,** or after `/reload-plugins`.

## How to add a plugin

**`/build:make-skill` creates the plugin** when a new skill needs one of the five that isn't built yet. To do it by hand, follow "A new plugin" in [CONVENTIONS.md](CONVENTIONS.md).

## Credits

Skills marked `(Matt: ...)` are copied from Matt Pocock's skills (https://github.com/mattpocock/skills, MIT licence, see `plugins/plan/LICENSE-matt-pocock`) and renamed. They no longer receive his updates.
