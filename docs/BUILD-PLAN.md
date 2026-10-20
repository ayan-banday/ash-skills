# Build plan: every skill into five plugins

The spec for finishing ash-skills. Settled with Ash on 2026-10-20 and carried out the same day by `docs/build_all.py` (one run, now guarded).

## The naming rule (replaces the bracket-search rule)

**Every word Ash searches by goes into the name,** because the `/` menu matches only words in a name. Ash tested this in his app: `/wayfinder` finds `plan:chart-project-wayfinder`, and `/skills` search does nothing there.

- **Name = `<what-it-does>[-<old-name>][-<tag>]`.** Lowercase, hyphens.
- **Old name:** keep a memorable original name as a word (`wayfinder`). Skip it when the new name is clear enough.
- **Tag:** who it's for or where it came from: `udyaan`, `shasta`, `substack`, `matt`. No tag when nothing fits.
- **Description starts with a square bracket:** the context and the old name, like `[Udyaan · was clear-visual-html]` or `[Matt: wayfinder]`. Then the "How do I..." question, then one sentence on what it does, then the triggers. The bracket is for reading; search runs on the name.

## The name map

### write
| New name | Was | Bracket |
|---|---|---|
| `course-lesson-udyaan` | course-writer (Ash) | `[Udyaan course · was course-writer]` |
| `headline-angles-substack` | newsletter-headlines (Ash) | `[Substack · was newsletter-headlines]` |
| `re-explain-matt` | wait-what (Matt) | `[Matt: wait-what]` |
| `agent-docs-matt` | writing-for-agents (Matt) | `[Matt: writing-for-agents]` |
| `post-draft-substack` | not built yet | later, once 3 or 4 posts exist |

### visualize
| New name | Was | Bracket |
|---|---|---|
| `story-plan` | visual-storytelling | `[was visual-storytelling]` |
| `polished-doc` | clear-documents | `[was clear-documents]` |
| `brief-page-udyaan` | clear-visual-html | `[Udyaan teammates · was clear-visual-html]` |
| `pitch-site-udyaan` | clear-proposal-site | `[Udyaan · website · was clear-proposal-site]` |

### plan (rename the pilot)
| New name | Was | Bracket |
|---|---|---|
| `grill-idea-matt` | grill-me | `[Matt: grill-me]` |
| `grill-with-docs-matt` | grill-with-docs | `[Matt: grill-with-docs]` |
| `chart-project-wayfinder-matt` | wayfinder | `[Matt: wayfinder]` |
| `write-spec-matt` | to-spec | `[Matt: to-spec]` |
| `split-tickets-matt` | to-tickets | `[Matt: to-tickets]` |
| `setup-tracker-matt` | setup-matt-pocock-skills | `[Matt: setup-matt-pocock-skills]` |
| `try-prototype-matt` | prototype | `[Matt: prototype]` |
| `gather-facts-matt` | research | `[Matt: research]` |
| `ask-someone-matt` | to-questionnaire | `[Matt: to-questionnaire]` |
| `grilling-matt` | grilling (helper) | `[Matt: grilling · helper]` |
| `domain-modeling-matt` | domain-modeling (helper) | `[Matt: domain-modeling · helper]` |

### build
| New name | Was | Bracket |
|---|---|---|
| `build-ticket-matt` | implement | `[Matt: implement]` |
| `build-whole-spec-matt` | implement-spec | `[Matt: implement-spec]` |
| `test-first-matt` | tdd | `[Matt: tdd]` |
| `find-bug-matt` | diagnosing-bugs | `[Matt: diagnosing-bugs]` |
| `review-code-matt` | code-review | `[Matt: code-review]` |
| `find-simplifications-matt` | improve-codebase-architecture | `[Matt: improve-codebase-architecture]` |
| `setup-walkthrough-matt` | wizard | `[Matt: wizard]` |
| `write-pr-matt` | pr | `[Matt: pr]` |
| `improve-next-time-matt` | retro | `[Matt: retro]` |
| `handoff-matt` | handoff | `[Matt: handoff]` |
| `codebase-design-matt` | codebase-design (helper) | `[Matt: codebase-design · helper]` |
| `make-skill` | new (built 2026-10-20) | `[skill maker · uses skill-creator]` |

### learn
| New name | Was | Bracket |
|---|---|---|
| `study-shasta` | study | `[Shasta · was study]` |
| `graphify` | graphify | `[files to knowledge graph]` |
| `which-skill` | new (built 2026-10-20) | `[skill guide]` |

**Left out:** Matt's ask-matt, triage and teach. **Stays installed as is:** jmo-workflow, Anthropic's skills.

## Steps, each with its done test

1. **Copy and rename.** Ash's skills come from `~/.claude/skills/` (master copies; clear-visual-html is the upgraded one). Matt's come from the installed `mattpocock-skills` 1.3.1 cache, without their `agents/` folders. Done: every folder above exists under `plugins/<plugin>/skills/<name>/`.
2. **Rewrite frontmatter.** `name:` is the new name; `description:` is the bracket plus the question and the old description's trigger text. Keep `disable-model-invocation` as it was. Done: every SKILL.md's name matches its folder.
3. **Fix links between skills.** Replace old names with new ones in `../old-folder/` paths, in `Skill tool with "old"` lines, in `` `/old` `` commands, and in prose naming Ash's old skills (clear-documents and the rest). Leave tracker labels like `wayfinder:map` and ticket types like `research` alone. Done: a grep for the old names finds only brackets, credits and labels.
4. **Plugin files.** One `plugin.json` per plugin, all five in `marketplace.json`, Matt's licence copied into every plugin that holds his skills. Done: `claude plugin details <p>@ash-skills` lists the right skills for all five.
5. **Rules and map.** Update `CONVENTIONS.md` to the naming rule above. Rewrite `README.md` as the map: every skill, its question, what it was. Done: make-skill's next run follows the new rule.
6. **Clean up.** Uninstall `mattpocock-skills`. Move `~/.claude/skills/` copies to `~/.claude/skills-backup-2026-10-20/`. Delete `.claude/skills/` and `sync-skills.ps1` in Shasta, Charlotte and Jain-BBA, uncommitted, and point each `SKILLS.md` at ash-skills. Point `~/.claude/CLAUDE.md`, `D:\Shasta\_rules\Clusters.md` and `D:\Jain-BBA\CLAUDE.md` at the new names. Done: no skill shows twice in a new session.
7. **Not done without Ash's yes:** pushing ash-skills to GitHub, and committing the deletions in the three repos. Until the push, cloud sessions have no skills.
