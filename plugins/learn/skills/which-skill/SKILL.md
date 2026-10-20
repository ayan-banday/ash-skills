---
name: which-skill
description: "(skill guide) Which of my skills should I use right now? Reads every installed skill's name and description fresh, then names the one command to type for what Ash is doing, with one line of why. Use when Ash asks 'which skill should I use', 'is there a skill for this' or 'what do I type'. Use before make-skill, to check a skill doesn't already exist."
---

Name the **one command Ash should type** for what he's doing now, from the skills installed today.

## Steps

1. **Get what Ash is doing.** When his message says it, use that. Otherwise ask one question: "What are you working on right now, and what do you want to have at the end? For example: 'pricing for the micro-SaaS, and I want a plan Mohit can read.'"
   Done when you can name the task and the thing he wants back.
2. **Read the skills fresh, every run.** The list changes as Ash adds skills, so the only source is the files on disk today:
   - **Ash's plugins:** `grep -H -E '^(name|description|disable-model-invocation):' D:/ash-skills/plugins/*/skills/*/SKILL.md`. The folder after `plugins/` is the plugin. Typed as `/<plugin>:<name>`.
   - **Ash's loose skills:** the same grep over `C:/Users/ayanb/.claude/skills/*/SKILL.md`. Typed as `/<name>`.
   - **Other plugins:** `claude plugin list` names the enabled ones as `<plugin>@<marketplace>` with their versions. Their skills sit anywhere under `C:/Users/ayanb/.claude/plugins/cache/<marketplace>/<plugin>/<version>/skills/`, sometimes in category folders, so grep it recursively for `SKILL.md`. Skip `in-progress` folders and every version but the listed one. Typed as `/<plugin>:<name>`.
   - **Anthropic's and Claude Code's own skills** (`anthropic-skills:...`, `/code-review`, `/simplify`): from your own skill listing in this session.
   Done when every source above was read in this run.
3. **Pick the skill.** Match Ash's task to each description's question first, then to its trigger and look-alike lines.
   - **Prefer Ash's own copy.** A bracket like `(Matt: to-spec)` marks a skill copied from another pack: name the ash-skills one (`/plan:write-spec`) over the original (`/mattpocock-skills:to-spec`). The same goes for a loose skill that now also lives in a plugin.
   - **Weigh the skills only Ash can type** (`disable-model-invocation: true`) like the rest. They're the ones he forgets.
   - **Several fit:** pick the one whose question names his situation most closely, and give the runner-up on line two.
   Done when one skill fits, only a nearby one does, or none does.
4. **Answer in three lines or fewer:**
   > **Type `/plan:write-spec`.** It turns what you just decided into one written plan.
   > Then `/plan:split-tickets`, to break the plan into tasks Claude builds one at a time.
   - **Line one:** the command in bold and what it hands back, in Ash's words.
   - **Line two, when it helps:** the next skill in the chain, or the look-alike and why this one wins.
   - **Only a nearby skill fits:** name it, and say in line two what it leaves out.
   - **No skill fits:** say so in one line and offer `/build:make-skill` to make one.
