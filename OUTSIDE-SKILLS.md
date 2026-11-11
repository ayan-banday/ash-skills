# Outside skills: other people's skills, ready when a build needs them

Skills here come from other people's repos. A few are installed in every cloud session. The rest stay on the shelf until a project needs them. Ash's own skills are in [README.md](README.md). This file also keeps the UI libraries he has saved.

## For Claude: how to use this file

1. **Before a major build** (a new app, site or tool, or work that takes more than one session), ask Ash once: "This is a big build. Want me to check your outside skills for any that could help?" Skip the question for small jobs.
2. **Fetch nothing until he says yes.** Then pick at most three skills from the shelf below that fit the job, and name each in one line with why.
3. **For a skill he picks, fetch it for this project only:**
   ```bash
   git clone --depth 1 <repo url> /tmp/outside-skills/<repo name>
   ```
   Read `<path>/SKILL.md` and the files it points to in the same folder, then follow it as if it had been invoked. Don't install it permanently.
4. **If a skill earns its place** (Ash uses it on two projects), suggest moving it to "Installed" below. That needs one line in `cloud/setup.sh`.
5. **When Ash saves a new skill or library,** add a row here: the name, where it lives, and when to reach for it.

An outside skill never overrides Ash's own rules. Where one disagrees with `match-ash-writing`, `match-ash-design` or a project's CLAUDE.md, Ash's rules win.

## Installed in every cloud session

`cloud/setup.sh` copies these into `~/.claude/skills` when a session starts. On Ash's PC, install them with `npx skills@latest add emilkowalski/skills`.

| Skill | From | What it does | Starts |
|---|---|---|---|
| `emil-design-eng` | Emil Kowalski | His rules for UI polish and animation: the right easing, shadows instead of solid borders, the details that make an interface feel good. | On its own, when building UI |
| `pick-ui-library` | Emil Kowalski | Picks a trusted library for a frontend job (toasts, charts, command menus, drag and drop) so Claude doesn't hand-roll one or install an abandoned package. | Only when typed |
| `mobile-native` | Emil Kowalski | Small fixes that make a web page feel like an app on a phone: the 100vh bug, inputs that zoom the page, tap flashes, safe areas. Pairs with `docs/mobile-site-playbook.md`. | On its own, for phone pages |

## The shelf

**Where each source lives:**

| Source | Repo | Skill path | Licence |
|---|---|---|---|
| Emil Kowalski | https://github.com/emilkowalski/skills | `skills/<name>/SKILL.md` | MIT |
| Ponytail | https://github.com/dietrichgebert/ponytail | `skills/<name>/SKILL.md` | MIT |
| Matt Pocock | https://github.com/mattpocock/skills | `skills/<group>/<name>/SKILL.md` | MIT |
| Anthropic | https://github.com/anthropics/skills | `skills/<name>/SKILL.md` | see repo |

### Building pages, apps and UI

| Skill | From | Reach for it when |
|---|---|---|
| `animate` | Emil | Building one animation from scratch: whether to animate at all, then the curve, the length and how it exits. |
| `choreograph` | Emil | Several things move together, like a hero entrance or a list that staggers in. |
| `gestures` | Emil | Anything dragged or swiped: sheets, drawers, swipe-to-dismiss, drag-to-reorder. |
| `apple-design` | Emil | You want an Apple feel: springs, fluid motion, frosted materials, depth. |
| `animation-vocabulary` | Emil | Ash can describe a motion but not name it ("the bouncy thing when it opens"). |
| `animation-performance` | Emil | An animation stutters or drops frames. |
| `review-animations` | Emil | A strict check of a page's motion before it ships. Only when typed. |
| `find-animation-opportunities` | Emil | A page feels flat and you want to know where motion would help. Read-only. |
| `remove-animations` | Emil | A page has too much motion. It only takes things away. |
| `improve-animations` | Emil | A whole codebase's motion needs an audit and a plan. |
| `break-ui` | Emil | Testing a page with worst-case data: long names, empty lists, huge numbers. |
| `prototype` | Emil | Several different versions of one UI piece, side by side with a switcher. Ash's `try-prototype` covers most of this. |
| `ask-sonner` | Emil | Working with the Sonner toast library. |
| `animate-expo` | Emil | A React Native or Expo phone app. |
| `write-swift` | Emil | A native iPhone app in Swift. |
| `frontend-design` | Anthropic | A new UI that must not look templated. Ash's `match-ash-design` comes first. |
| `web-artifacts-builder` | Anthropic | A claude.ai artifact too big for one HTML file: React, Tailwind, shadcn/ui. |
| `webapp-testing` | Anthropic | Clicking through a local web app in a browser to test it and take screenshots. |
| `theme-factory` | Anthropic | Ten ready colour-and-font themes for slides, docs or pages. |
| `canvas-design` | Anthropic | A poster or a still piece of art as a PNG or PDF. |
| `algorithmic-art` | Anthropic | Generative art made with code (p5.js). |
| `slack-gif-creator` | Anthropic | A small animated GIF for Slack. |

### Keeping code small and safe

| Skill | From | Reach for it when |
|---|---|---|
| `ponytail` | Ponytail | Any coding task where you want the smallest change that fully works, and a reply a busy person gets in one read. `design-like-expert` already borrows its ladder. |
| `ponytail-review` | Ponytail | Checking one change: right, safe, holds under load, tested, every line needed. |
| `ponytail-audit` | Ponytail | Auditing a whole repo for bugs, security holes and what to delete. A copy lives in Fuji at `ranges/udyaan/course/research/ponytail/`. |
| `ponytail-debt` | Ponytail | Listing every shortcut Ponytail left for later. |
| `git-guardrails-claude-code` | Matt | Blocking risky git commands (force push, hard reset) with a hook. |
| `setup-pre-commit` | Matt | Formatting, type checks and tests that run before every commit. |
| `mcp-builder` | Anthropic | Building an MCP server so Claude can use an outside service. |

**Ponytail as an always-on mode:** the full plugin adds hooks and a status line to every session. Install it with `claude plugin marketplace add DietrichGebert/ponytail`, then `claude plugin install ponytail@ponytail`. Only do that with Ash's yes, because it changes how every session behaves.

### Planning and writing

| Skill | From | Reach for it when |
|---|---|---|
| `triage` | Matt | Many issues or outside pull requests need sorting into ready-to-build briefs. |
| `teach` | Matt | Learning a concept inside the current project. Close to Ash's `teach-side-chat`. |
| `doc-coauthoring` | Anthropic | Writing a spec, proposal or decision doc together, step by step. |

**Already copied into Ash's skills, so don't fetch them:** Matt's grilling, grill-me, grill-with-docs, wayfinder, to-spec, to-tickets, to-questionnaire, prototype, research, tdd, diagnosing-bugs, code-review, pr, wizard, handoff, retro, wait-what, writing-for-agents, domain-modeling, codebase-design, improve-codebase-architecture, setup-matt-pocock-skills, implement and implement-spec. Anthropic's docx, pdf, pptx, xlsx and skill-creator already come with claude.ai.

## UI libraries Ash has saved

These are code libraries, not skills. Use them when a build is a real React app. For a single HTML page, copy the look in plain HTML and CSS. A live before-and-after of each: https://claude.ai/artifact/BiQSawBx4bEteEs5uYFdyJ

| Library | What it is | Use it for |
|---|---|---|
| [shadcn/ui](https://ui.shadcn.com) | Clean components, copied into your project so you own the code | The default for any React app |
| [Radix](https://www.radix-ui.com) and [Base UI](https://base-ui.com) | Unstyled pieces that handle the keyboard, focus and screen readers | What shadcn sits on; rarely picked directly |
| [Sonner](https://sonner.emilkowal.ski) | Toast messages that slide in and stack | "Saved" messages |
| [Vaul](https://vaul.emilkowal.ski) | A bottom sheet you swipe down to close | Phone menus and filters |
| [cmdk](https://cmdk.paco.me) | A ⌘K command menu | Search-and-run in tools and dashboards |
| [NumberFlow](https://number-flow.barvian.me) | Numbers that roll to their new value | Prices, counts, dashboards |
| [Magic UI](https://magicui.design) | Animated landing-page pieces: shimmer buttons, marquees | One eye-catching section |
| [Aceternity UI](https://ui.aceternity.com) | Bold effects: 3D cards, spotlights, beams | A hero section |
| [RareUI](https://rareui.in) and [Beautiful UI](https://beautifului.dev) | Smaller galleries of copy-paste effects | Ideas when the others don't have it |
| [21st.dev](https://21st.dev) | A marketplace of shadcn-style components, with an AI maker | Finding a specific piece, like a pricing table |
