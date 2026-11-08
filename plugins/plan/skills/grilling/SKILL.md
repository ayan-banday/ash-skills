---
name: "grilling (matt)"
description: "[helper] How do I get grilled in short, light chats that ask only what I can decide? Grills by layer (the problem, how it works, the plan and build), one layer per chat. Each layer has a fixed goal, and every question is self-contained and drawn from Ash's brain dump. Ends in a ready ticket, never a build. Also runs studies alone after a 1-2 question mini-grill. Use when Ash says 'grill', 'grill me', 'stress-test this', or 'study:'. The engine behind grill-idea, grill-with-docs and chart-project-wayfinder."
---

Ash's limit is his own thinking: about 2 hours, then rest. Every rule here exists to spend less of it. **Light** is the leading word: short messages, few questions, one layer.

## Steps

1. **Find the layer.** Read `references/layers.md` once per chat: each layer's goal, its slots, what it may and may not ask, and two worked examples. Ash names the layer, or you infer it: a new problem, and any side grill, starts at Layer 1; a ticket handed down from Layer 2 starts Layer 3. **One chat works one layer.**
   - **Name the chat and say its layer** by `references/chats.md`: the title is `Layer <N> · <Topic>: <what it's about>`, under about 28 characters, and the first message opens with "This is Layer <N>: <its goal>." (Ash, 2026-11-08: the sidebar shows one level, so the title carries the layer and the topic). Read it once per chat.
   Done when you can name the layer and its goal, and the chat's title shows both.
2. **Read what's written before asking.** In Fuji: `olympus.md`, the map's Destination, the phase's `phase.md` and the ticket; elsewhere, the repo's docs and the chat. Done when you know what's already decided above this layer.
3. **Open the layer.**
   - **Layer 1:** ask for the brain dump in one line ("Tell me everything about it: what's happening, what you've tried, what bugs you.") and nothing else. If his first message already is the dump, skip this.
   - **Layer 2:** the Layer 1 decisions in two lines, then the first questions.
   - **Layer 3:** what the ticket decided in two lines, then 1 or 2 questions about what he wants it to do for him.
   Done when he has one thing to react to.
4. **Fill the slots.** After each answer, silently write the layer's slots (`references/layers.md`) and mark each one filled from his own words or empty. **Ask only about empty slots** whose prerequisites are filled. At most **3 questions a round**, each passing the test in `references/questions.md`. Finding facts is your job (send a sub-agent); decisions are his. Done when every question in the round fills an empty slot.
5. **Park what's off-layer.** When Ash drifts into another layer, don't answer or ask about it here. Note it quietly in the right place (in Fuji, the phase's `fog.md`; elsewhere, a "Parked" list in the ticket) and say "parked for later: N ideas" once, at the end.
6. **Close when the slots are full.** Say "I've got what Layer N needs. Anything else you want to talk about?" When he's done, send the final message: the summary of what was decided (the only summary in the chat), then save the decisions (not his words) to the ticket, mark where it stands, and name the next chat in one line: "Saved. Next chat: Layer 2." **When Ash asks for the next chat,** open it by `references/chats.md` ("Opening the next chat"): one layer down, a Layer 2 may open several Layer 3 chats, and a side grill that doesn't fit the topic gets a line for Ash to open himself. In Fuji, saving follows `gear/rulebook.md` section 3 ("Ending"). Done when the ticket holds the decisions and the next chat is named.

## The message format

Every round:

```
**Goal:** <one line: what this chat settles>
**Problem:** <one line, in his words>

**1. <a self-contained question>**
Looking for: <the slot it fills, in plain words>

**2. ...**
```

- **In Layer 3,** the two lines on what the ticket decided take the Problem line's place.
- **Questions follow `references/questions.md`:** self-contained, one ask, open, 7th-grade words, built from his brain dump.
- **Options go in a tap widget** (`AskUserQuestion`), never typed as a list. The widget may hide the chat, so its question names everything it asks about. Layer 1 options never mark a recommended one; Layers 2 and 3 may put a recommended option first.
- **Leave out:** "Suggestion:" lines, progress bars, say-back lists, "got it" lines, recaps and summaries before the final message.
- **Phone first.** Short lines, no tables, no list longer than 3 items without sub-groups.

## Studies that run on their own

When Ash says "study: <question>" (in chat, from his phone), follow `references/study.md`: a mini-grill of 1 or 2 questions with suggestions, then run alone, then a phone page (an artifact link, never a file path) and a notification. His saying "study:" is his yes to run it.

## Taste

Anything Ash will see (a prototype, a study page) reads his taste library first: his design language, colours, typography and writing voice. The words live in `/write:match-ash-writing` (`../../../write/skills/match-ash-writing/SKILL.md`); the look and colours in `/visualize:match-ash-design` (`../../../visualize/skills/match-ash-design/SKILL.md`), which has a "Phone study page" case. Formatting is decided from these, never asked.
