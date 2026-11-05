# The layers

Ash's definition (Nov 2, reworked Nov 5, 2026). Grilling goes down by depth, **one layer per chat.** Each layer has a **goal** that is the same for every problem (code, a course, a habit, a business), and a short list of **slots**: the things the chat must know to reach that goal. Questions exist only to fill empty slots. A question that fills no slot of this layer is parked.

## Layer 1: the problem and the direction

**Goal:** know what is really going wrong, why, and what a good fix must do, so the direction is clear before anyone designs anything.

**Slots, in order** (gap selling: current state, cause, future state):
1. **The story:** the last real time the problem happened, from his brain dump or a Mom Test question.
2. **What he's tried:** workarounds and fixes he already used, and why they stopped working.
3. **The real problem:** picked from 2 or 3 candidates in his words (tap widget).
4. **Cause versus symptom:** checked by "if this were fixed, what would still go wrong?"
5. **What a fix must do:** in his words. Then what a normal day looks like once it works.
6. **Phases,** only for a whole project, and only after slot 5. A single ticket has none.

**May ask:** stories from the past, causes, trade-offs between things he values, what a fix must do.
**May not ask:** how it works, tools, specifics, success metrics, anything about an existing build. Never recommend an option.

## Layer 2: how it works, in general

**Goal:** know the principle of the fix and how its parts work together, in a form that would work for any field or case, so Layer 3 has rules to build from.

**Slots:**
1. **The principle:** the one rule the fix runs on.
2. **The parts and their order:** what goes in, what comes first.
3. **How it changes by case:** for example facts versus steps versus knowing when versus performing in front of people; a normal day versus a bad day.
4. **Who or what does each part:** a person, the system, someone else.

**May ask:** principles, parts, order, cases, who does what.
**May not ask:** tools, wording, timing, sources, how it looks. If the Layer 1 problem looks wrong, say so in one line and offer a Layer 1 chat.

## Layer 3: the plan, then the build

A new chat, handed the ticket.

**Goal:** agree a plan he has edited, then build a quick prototype he reacts to.

**Slots:**
1. **His intent:** what he wants this build to make easier, in his words.
2. **The plan, edited by him:** what gets prototyped, what doesn't, the look (colours and mood from his taste library), and what happens after.
3. **His reactions to the prototype.**

**Opens with:** what the ticket decided, in two lines, then 1 or 2 intent questions. **Then the plan** as four short lines (Prototype, Not prototyped, Look, Then), and "What would you change in this plan before I build it?" Build only after he answers.
**May ask:** intent, the plan, the look, reactions.
**May not ask:** why we're doing it (that's Layer 1 or 2: say so in one line). Formatting (spacing, bold, line length) is decided from his taste skills and never asked.

## Example 1: "I order food delivery most nights"

**Layer 1** (after his brain dump):
- "What were you doing right before you ordered food delivery the last time?" Looking for: the story.
- "What have you already tried to cook or eat at home more, and what made each one stop?" Looking for: what he's tried.
- Widget: "Why do you end up ordering food delivery most nights?" a) by dinner time you're too tired to decide what to eat; b) there's no ready-to-eat food at home; c) delivery is your reward after a long work day.
- "If ready-to-eat food were always at home, what would still make you order delivery?" Looking for: cause versus symptom.
- "What would a fix for ordering delivery most nights need to do for you?"
- Closes: "I've got what Layer 1 needs. Anything else you want to talk about?"

**Layer 2:**
- "Which food choices should be made once a week, and which should be left for the moment you're hungry?"
- Widget: "Who should decide tonight's dinner: you on Sunday, a default meal that repeats, or someone else, like a cook?"
- "How should dinner on a normal workday differ from dinner on a day you're out past 9 pm?"

**Layer 3:**
- "What should the Sunday dinner plan make easier for you: shopping, cooking or deciding?"
- The plan: Prototype: a Sunday menu card on the week page. Not prototyped: the grocery order. Look: warm food colours, one card, read in 10 seconds. Then: a one-week try.
- "What would you change in this plan before I build the menu card?"

## Example 2: "Udyaan students quit after week 2"

**Layer 1:**
- "When the last student quit the Udyaan course, what was going on in their week right before they stopped coming?"
- "What does a student who finished all 14 days of the Udyaan course do differently from one who quit in week 2?"
- Widget: "Why do most Udyaan students quit after week 2?" a) the course needs its own hour each day; b) students can't see what the course will get them; c) nobody notices when a student starts slipping.

**Layer 2:**
- Widget: "Who should bring a slipping Udyaan student back: a mentor, an automatic message or their teammates?"
- "How should bringing back a student who is behind on facts differ from bringing back one who is scared to pitch in front of the class?"

**Layer 3:**
- "Here is the WhatsApp message an Udyaan student gets after missing two days: 'Hey Riya, we missed you on Tuesday and Wednesday. Your team is presenting Friday. Want a 10-minute catch-up call today?' Which line feels too pushy?"

## Going back up

If a lower layer turns up something that breaks a higher decision, stop, say it in one line, and offer a chat at the higher layer. Never re-grill the higher layer inside the lower chat.
