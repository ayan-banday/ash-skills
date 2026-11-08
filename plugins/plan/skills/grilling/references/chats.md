# Chats: names and families

Ash's rule (2026-11-08). He follows grillings in the Claude app's sidebar, so every chat's title has to tell him its layer and topic at a glance. Tested that day: the sidebar shows only one level. Every chat started from a chat, however deep, appears flat under the top chat of its family, cut off at about 28 characters.

## The title

`Layer <N> · <Topic>: <what it's about>`

- **Topic:** one word for the big topic this chat serves, like Week, Gym, WhatsApp. Every chat in a family uses the same word, except a side grill, which takes its own.
- **What it's about:** 2 to 4 words. Layer 1 names the problem, Layer 2 the principle, Layer 3 what gets built or planned.
- **Under about 28 characters in total,** so the sidebar shows all of it. Shorten the words, never drop the layer or the topic.
- Set it with the claude-code-remote tool `set_session_title` (its own id from `get_session`) before the first question.

```
Layer 1 · Week: Falls apart
Layer 2 · Week: How a plan works
Layer 3 · Week: Page design
Layer 3 · Week: Sunday ritual
Layer 1 · Gym: Skip busy weeks
```

## The family

- **A big topic's Layer 1 is the family's top chat.** Ash opens it himself, so it heads its own group in the sidebar.
- **A side grill that fits the big topic** starts at its own Layer 1 with its own topic word, opened from a chat in that family, so it lands in the same group.
- **A side grill that doesn't fit** gets no chat from here. Say in one line: "This doesn't fit <topic>. Open a new chat and start with: <one line he can paste>." His new chat heads its own group.
- **If Ash asks a chat outside grilling to start a new big topic,** start it, and say once that it will sit under that chat in the sidebar.

## Opening the next chat

Only when Ash asks ("open the next layer", "open a chat for the content one"):

- Start it from this chat with `create_session`, one layer down: Layer 1 opens Layer 2, Layer 2 opens Layer 3. A side grill opens at Layer 1.
- **Layer 2 may open several Layer 3 chats,** one per ticket it produced, each when he asks for it. A ticket nobody asked about waits without a chat.
- Title it by the rule above. Its prompt stands alone: the ticket's path, what the layers above decided, and this layer's goal.
- Reply with the new chat's title, in one line.

## The chat's first line

Every grilling chat's first message opens with where it stands, before anything else:

`This is Layer <N>: <its goal in plain words>.`
