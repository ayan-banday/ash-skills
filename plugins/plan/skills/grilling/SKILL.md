---
name: "grilling (matt)"
description: "[helper] How do I get grilled in short, light chats that ask only what I can decide? Grills by layer (big picture, how a phase works, details, formatting), one layer per chat, each message just the goal and questions with a suggestion, and ends in a ready ticket, never a build. Also runs studies alone after a 1-2 question mini-grill. Use when Ash says 'grill', 'grill me', 'stress-test this', or 'study:'. The engine behind grill-idea, grill-with-docs and chart-project-wayfinder."
---

Ash's limit is his own thinking: about 2 hours, then rest. Every rule here exists to spend less of it. **Light** is the leading word: short messages, few questions, one layer.

## Steps

1. **Find the layer.** Read `references/layers.md` once per chat. Ash names the layer, or you infer it: a new project or a new phase starts at Layer 1. **One chat works one layer.** Done when you can name the layer in one word.
2. **Know his goals before asking anything.** Read what's there: in Fuji, `olympus.md`, the map's Destination, the phase's `phase.md` (Done when) and the ticket; elsewhere, the repo's docs and the chat. Ask for a goal only when none is written down. Done when you could state the goal without him.
3. **Open with a plan to poke holes in.** First message of the chat: the goal (your guess), a short plan of action you inferred (Layer 1: the phases; Layer 2: how this phase works; Layer 3: a quick prototype), and the first questions. Done when he has something to react to, not a blank page.
4. **Grill in rounds** (format below). Each round asks only the **frontier**: the open questions whose prerequisites are settled. At most **3 questions a round**. Finding facts is your job (send a sub-agent); decisions are his.
5. **Park what's off-layer.** When Ash drifts into another layer, don't answer or ask about it in this chat. Note it quietly in the right place (in Fuji, the phase's `fog.md`; elsewhere, a "Parked" list in the ticket) and say "parked for later: N ideas" once, at the end.
6. **End in a document, never a build.** When the layer's questions are settled, save the decisions (not his words) to the ticket, mark it ready, and name the next chat in one line: "Saved. Next chat: Layer 2, Phase 1." Ash ends the session; until he does, keep going. In Fuji, saving follows `gear/rulebook.md` section 3 ("Ending").

## The message format

Every message, every round:

```
**Goal:** <one line>

**1. <question that stands on its own, with the context it needs>**
Suggestion: <your answer, one line, with the reason if it isn't obvious>

**2. ...**
```

- **Goal, then questions.** A Problem line only in a big grilling (a new project's Layer 1).
- **A suggestion, not options.** Give lettered options only when the question is genuinely hard and the choices really differ. Word the suggestion so "yes" accepts it.
- **Leave out:** progress bars, say-back lists, "got it" lines, "decided" lists, recaps. Show what was decided only when he asks.
- **Phone first.** He reads on his phone: short lines, no tables, no list longer than 3 items without sub-groups.

## Studies that run on their own

When Ash says "study: <question>" (in chat, from his phone), follow `references/study.md`: a mini-grill of 1 or 2 questions with suggestions, then run alone, then a phone page (an artifact link, never a file path) and a notification. His saying "study:" is his yes to run it.

## Taste

Anything Ash will see (a prototype, a study page) reads his taste library first: his design language, colours, typography and writing voice. The words live in `/write:match-ash-writing` (`../../../write/skills/match-ash-writing/SKILL.md`); the look and colours in `/visualize:match-ash-design` (`../../../visualize/skills/match-ash-design/SKILL.md`), which has a "Phone study page" case.
