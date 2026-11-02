# The layers

Ash's definition (Nov 2, 2026). Grilling goes down by depth, one layer per chat. Each layer has a **test**: before asking a question, check it. If it fails, it belongs to another layer: park it.

| Layer | What it settles | The test before every question | Opens with |
|---|---|---|---|
| **1. Big picture** | the outcome, the problem, the hypothesis, trade-offs between things he values, the project's phases | Would the answer change the goal, the problem, the hypothesis or the phases? | goal + the phases you inferred |
| **2. How a phase works** | one phase's implementation: what goes in, the order, how the parts work together (the course's UI/UX with its content) | Would the answer change what's in this phase or its order? | the phase's Done when + a build order you inferred |
| **3. Details** | colours, typography, the AI setup, minute specifics | Would the answer change how something looks or runs? | a quick prototype (cheap fast model, under a minute) he reacts to |
| **4. Formatting** | text formatting, spacing, very low details | (never asked) | you decide from his taste library |

## Examples: the same project, each layer

Project: a YouTube channel for Udyaan.

**Layer 1, asked:**
- "Is the goal students, or proof that you can teach? Suggestion: students; proof follows."
- "Your face on camera, or faceless? Suggestion: your face, because trust sells the course." (a trade-off between things he values)
- "Phases: find the format, a weekly rhythm with Mohit, then scale. Suggestion: yes."

**Layer 1, parked** (Ash says it, or you're tempted to ask):
- "Shorts with Hindi captions" → Layer 2 or 3. Park.
- "Who edits the videos?" → Layer 2. Park.
- "What colour are the thumbnails?" → Layer 3. Park.

**Layer 2, asked** (in a new chat, Phase 1: find the format):
- "Who edits, you or Mohit? Suggestion: Mohit; you review."
- "Script first or record first? Suggestion: script, so each video tests one idea."

**Layer 2, parked:** "Which font on the thumbnail?" → Layer 3. "Should we do YouTube at all?" → Layer 1: say so in one line and offer a Layer 1 chat.

**Layer 3, asked** (a new chat, prototype first): "Here's the thumbnail mock. Warmer or cooler? Suggestion: warmer, it matches the course."

**Layer 4:** caption line length, bold or not: decided, never asked.

## Going back up

If a lower layer turns up something that breaks a higher decision (the format test shows the goal is wrong), stop, say it in one line, and offer a chat at the higher layer. Never re-grill the higher layer inside the lower chat.
