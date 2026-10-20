---
name: make-skill
description: "[skill maker · uses skill-creator] How do I make a new skill that lands in the right plugin with a clear name? Names, writes, installs and commits a skill in Ash's ash-skills plugins by the repo's CONVENTIONS.md, or fixes an existing skill's name or description. Use when Ash says 'make a skill', 'turn this into a skill' or 'rename this skill'. Use instead of skill-creator for Ash's own skills."
---

Make or fix one skill in Ash's plugin repo, `D:\ash-skills`, so it is **filed, named and described by the rulebook**.

## Start here, every run

1. **Read `D:\ash-skills\CONVENTIONS.md` in full.** It holds every naming, writing and shipping rule. This file only gives the order.
2. **List every skill** with the listing command at the end of CONVENTIONS.md. Keep the list for clash and look-alike checks.
3. **Pick the branch.** Ash names an existing skill, or says rename or fix: go to "Fix a skill". Otherwise: "Make a skill".

## Make a skill

1. **Learn what it's for.** When the conversation already shows the workflow ("turn this into a skill"), take the answers from it. Otherwise ask Ash one question that names the subject: what he's doing when he'd reach for it, and what it hands back.
   Done when you can say the skill's job in one sentence and name one phrase Ash would say to start it.
2. **Decide the five calls** by CONVENTIONS.md: plugin, name, bracket, question, who can start it. The name ends in its tag (`-udyaan`, `-matt`) whenever one fits, since the name is the only thing Ash can search. Check the list for a name clash and for a look-alike the description must tell apart. Show them to Ash in one line and wait:
   > **visualize:brief-page-udyaan** · [Udyaan teammates · was clear-visual-html] How do I brief a teammate on a plan with a page they read alone? · only Ash types it · existing plugin. OK?
   Done when Ash says yes, or gives changes you applied.
3. **Draft the SKILL.md** at `D:\ash-skills\plugins/<plugin>/skills/<name>/SKILL.md`, with the frontmatter from step 2 and the body by "Writing the body" in CONVENTIONS.md.
   - For anything longer than a page, or with scripts or reference files, call the Skill tool with "anthropic-skills:skill-creator" to draft, write test prompts and tune the description. Override its defaults: save to the repo path above, keep the frontmatter from step 2, and skip its packaging step.
   - Copied from a known source: keep the original body, add the licence file and the README credit.
   Done when the description is 200 to 450 characters, its question makes sense with the name hidden, and every step in the body ends on a done test.
4. **Test it.** Write two or three prompts Ash would really type. For each, hand a subagent the SKILL.md path and the prompt, tell it to stay read-only, and ask for its final answer plus every step that was unclear or failed. Fix the body where a run goes wrong. For a skill Claude can fire, also check one prompt that should fire it and one look-alike prompt that should go to another skill.
   Done when every test prompt gets what the skill promises.
5. **Ship it** by "Saving and shipping a skill" in CONVENTIONS.md: new plugin files if needed, version bump, validate, marketplace update, install or update.
   Done when `claude plugin details <plugin>@ash-skills` lists the skill.
6. **Commit** only the files this run touched, named one by one: `git -C D:/ash-skills add <paths>` then `git -C D:/ash-skills commit`, then `git -C D:/ash-skills push` so cloud sessions and other laptops get it. Message: `Add <plugin>:<name>: <question>`.
7. **Tell Ash** the command to type, `/<plugin>:<name>`, and that it shows in sessions started after the install, or after `/reload-plugins`.

## Fix a skill

1. **Check the skill** against CONVENTIONS.md: plugin, name, bracket, question, the one-sentence summary, triggers, and who can start it.
2. **Show each change** as old to new with one line of why, and wait for Ash's yes. A rename breaks the command Ash already types, so say so.
3. **Apply.** For a rename: `git -C D:/ash-skills mv` the folder, change `name:`, then search the repo for the old name (`/<plugin>:<old>`, `"<plugin>:<old>"`, README) and update every hit.
   Done when a search for the old name finds nothing outside git history.
4. **Ship and commit** as in steps 5 to 7 above, with a patch version bump. Message: `Fix <plugin>:<name>: <what changed>`.

## Guardrails

- **Edit only `D:\ash-skills`.** Installed copies under `~/.claude/plugins/cache/` and skills in `~/.claude/skills/` stay as they are.
- **Commit and push every change.** Ash wants each skill available everywhere, including cloud sessions.
