# Intake: the brief, the facts sheet, the inspiration

Ask only for what is missing and changes the result. Ash prefers one short round of questions, then a playback.
If he is away or says "don't ask", infer, state every assumption in the hand-off note, and keep going.

## Contents
- What you need before writing anything
- The facts sheet
- The one inspiration question
- The playback (the story map)

## What you need before writing anything

1. **The reader:** who opens the link, their role, what they already know, what they distrust, the device
   (laptop or tablet; phones get the gate).
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
