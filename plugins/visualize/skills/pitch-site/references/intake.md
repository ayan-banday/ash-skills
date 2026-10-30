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
- **The message spine:** the 3 to 6 sentences the page must get across, in order, each one a full sentence a person
  would say out loud ("We collect each student's details with one form." "We help students form teams by subject.").
  The last one is the action. This is what the copy is written from and checked against.
- **The motif call:** whether the page needs a motif at all. A plain list of steps for a team may need none. If one
  helps, offer 2 or 3, each with the one piece of information it carries ("a tear-off calendar: how far through the
  14 days"), recommended first. "No motif" is a real option.

**2. Ask only where you are unsure,** at most four questions (skip any the brief already answers, such as the device), each standing on its own, with lettered options and
the recommended one first so "A" accepts it. Always include the device:
> "Where will they open it? A) phone only, B) a laptop page plus a phone appetizer that sends them to it,
> C) laptop only, phones see the gate."

Phone only is often enough (the Udyaan 14-day plan). Other good questions: which spine sentence matters most if the
reader keeps only one; what the reader distrusts; the inspiration question below.

**3. Save the agreed spine** to `work/message.md`, and write `work/facts.md` in the same pass: every number, name
and example the page may use, with its source. Anything marked undecided gets no number on a page for the people it
would be promised to (students see "a stipend is one idea", never "₹2,000–3,000"). Each fear the interpretation
names for the reader gets a spine sentence, or a note that the page leaves it out on purpose. Every screen's copy is written from one spine sentence, and the
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
