# Intake: the brief, the facts sheet, the inspiration

Ask only for what is missing and changes the result. Ash prefers one short round of questions, then a playback.
If he is away or says "don't ask", infer, state every assumption in the hand-off note, and keep going.

## Contents
- The grilling: one session on what the page must say
- What you need before writing anything
- The facts sheet
- The one inspiration question
- The playback (the story map)

## The grilling: one session on what the page must say

Every build opens with one grilling, before research or design (Ash, 2026-10-30: "I keep fucking up. I'm not clear
with what I want to communicate", and later: "a lot of times the copy is written in a manner that doesn't
communicate what I want to communicate"). One session is the default; run a second only when his answers change the
message itself. It settles two things: **exactly what the page communicates, and which motif, if any.**

**1. Lead with your best interpretation, before any question.** Ash reacts faster to a guess than to a blank. Write,
in plain words:
- **What happened:** the meeting, the feedback or the moment that led to this page, as you understand it.
- **The reader:** who opens it, what they already know, what they care about.
- **The message spine:** the 3 to 6 questions the reader would ask, in the order they'd ask them, each with a
  one-line plain answer and no personal pronouns (`copy-rules.md`, "Headlines are the reader's questions"). Show it
  as the page structure: one row per page, headline question | answer. The last row is the action. This is what
  the copy is written from and checked against. Ash's final spine for the Udyaan onboarding page (2026-11-02):

  | Headline (the reader's question) | The answer |
  |---|---|
  | How do we find out what students want as incentives? | We send them a form. |
  | What do students get? | What they asked for, from their own project. |
  | What about trophies and money? | Trophies and certificates still come after Day 14, read out in class. Money goes to Shraddha ma'am. |
  | How does feedback get simpler? | A quick WhatsApp update every 2 or 3 days; AI drafts the feedback, the mentor checks it. |
  | Who works with whom? | Teams of two, three at most. |
  | How do we test this? | Small batches of 5, as Hardik said. |
  | (the close) | Send 5 high-intent, high-energy students for the first batch. If not, reply "Change." |

- **The motif call:** whether the page needs a motif at all. A plain list of steps for a team may need none. When
  Ash names a format he has used before ("the calendar"), reuse it and skip this. Otherwise, if one helps, offer 2
  or 3 formats, recommended first. "No motif" is a real option.

**Name each option, then say it plainly.** Ash likes getting format and design options with their real names: they
give him words to design in. What lost him was a name with no explanation ("a deck you deal": "I have no idea what
you're talking about"). So every option is its name plus what the reader will see and do: "a deck you deal: cards
sit in a stack and you flick the top one away, so the pile shrinks"; "a tear-off calendar: one question per page,
tap to tear it off, so the pad gets thinner".

**2. Ask only where you are unsure,** at most four questions (skip any the brief already answers, such as the device), each standing on its own, with lettered options and
the recommended one first so "A" accepts it. Always include the voice ("Do you want to use 'I'? Default: no
pronouns.") and the device:
> "Where will they open it? A) phone only, B) a laptop page plus a phone appetizer that sends them to it,
> C) laptop only, phones see the gate."

Phone only is often enough (the Udyaan 14-day plan). Always ask the stakes too, since it sets how many tokens the
build spends (SKILL.md, "Two paths"):
> "How much rides on it? A) low: a presentation, a team plan, an internal page (fast path), B) high: an outside
> reader decides on it (full path), C) high, and check the hero before building the rest."

Recommend A for anything Ash presents himself or sends to his own team; B for a client, partner or funder.
Other good questions: which spine answer matters most if the
reader keeps only one; what the reader distrusts; the inspiration question below.

**3. Save the agreed spine** to `work/message.md`, and write `work/facts.md` in the same pass: every number, name
and example the page may use, with its source. Anything marked undecided gets no number on a page for the people it
would be promised to (students see "a stipend is one idea", never "₹2,000–3,000"). Each fear the interpretation
names for the reader gets a spine row, or a note that the page leaves it out on purpose. The spine names none of
the sender's tools or internal specifics the reader doesn't need ("a short form", never the form tool's name);
those go to the full plan. Every screen's copy is written from one spine row, and the
copy check compares the two (`references/copy-rules.md`). Build only after he answers.

## What you need before writing anything

1. **The reader:** who opens the link, their role, what they already know, what they distrust, the device
   (from the grilling: phone, laptop or both; `references/phone.md` covers phones).
2. **Their asks, verbatim:** from the meeting notes, an email, a transcript or Ash's dictation. Three or four is the
   sweet spot; more than five means some are sub-points.
3. **What we offer:** the teams or capabilities, each with what they actually do.
4. **Proof we may use, and how:** named, unnamed ("mention vaguely"), or not at all.
5. **The one action:** what the reader chooses, who they talk to (a real named person with an email), what arrives
   next and when.
6. **The sender's own rules:** brand colours to avoid or keep, names that must not appear, tone.

Check facts about the client against public sources when the brief makes claims about them (the TVS fact-check
found two different bodies being confused). Confirm spellings from written sources: Ash dictates by voice.

## The facts sheet

Write `work/facts.md` before any copy: every number, name, place, date, price and promise the page may use, each
with its source. The copy scan and the clarity reviewer diff the page against it. Anything not on it is either cut,
written as a goal, or labelled as part of an example.

## The one inspiration question

Ask exactly once, before design work:

> "Any inspiration for the look? A craft, a material or a place, like the kolam we used for TVS. Or say 'show me'."

Then follow references/directions/00-intake.md:
- **A named direction from the library:** confirm in one line and build ("Going with Transit: three lines, one hub.
  The hub is the client, the lines are the three needs.").
- **Something new** (a photo, a site, a craft): study it properly. For a website, fetch its raw HTML and CSS and
  read the real colours, easings and layout. For a video, extract frames with ffmpeg (contact sheets
  `fps=1/N,scale=320:-1,tile=6x5`, scene frames `select='gt(scene,0.25)'`, 10fps bursts around each move) and read the
  frames, never the video. For a photo of an object, match its geometry exactly. Then derive a palette from its
  materials (00-intake Part 3) and answer: what is its centre, its strands, its repeated parts, its levels.
- **"Show me" or no answer:** offer 3 to 5 directions, each as a name, one line a non-designer can picture, and a
  swatch line. The first is the recommendation. Apply the connection test: a culture's motif only when the client,
  partner, place or subject has a real tie to it. When Ash is away, take the recommendation and say why in one line.

## The playback (the story map)

Before building, show Ash in chat, briefly:
- the one belief after the first screen, and the hero line
- the direction, with what the motif's parts stand for
- the page architecture (catalogue ARC-) and the section list, each with its pattern ID and one line of what it shows
- the close: the three steps and the named person
Ash approves or redirects. If he is away, proceed and include the story map in the hand-off note.
