# Copy rules: say what Ash means, in as few plain words as it takes

These rules apply to every pitch page, phone and laptop. They sit on top of `writing-rules.md` (asks, honesty,
banned words, the scan). They come from Ash's corrections on 2026-10-30 to the TVS phone page, and from his course
rules (`/write:course-lesson` and its round-2 changes), cut down to what a page for a busy reader needs.

The first TVS phone draft talked in its metaphor ("Leaders steer. Let them see the road ahead." "TVS already has the
frame.") and Ash called it garbage: "we don't really talk like that". The fix made every headline a question, which
was clearer but long, and some lines still said something other than what he meant.

## Contents
- The two tests
- Write from the message spine
- Question or statement
- The drawing carries the metaphor
- Plain, full sentences
- Cutting words without losing clarity
- Bold and cards
- Before and after
- The copy check

## The two tests

1. **Would Ash say it this way, out loud, to this reader?** If it sounds like a slogan, a riddle or a brochure, it
   fails.
2. **Does it say the spine sentence it was written from?** A clear line that says the wrong thing fails too.

## Write from the message spine

The grilling ends with the message spine: 3 to 6 plain sentences the page must get across, in order, ending in the
action (`intake.md`). Each screen traces to one spine sentence. When the content is a sequence (a 14-day plan),
one spine sentence may cover several screens, one step each; the screens still say that sentence between them. Write the copy from it, then check the copy
against it line by line. If a screen's headline and bold phrase, read alone, don't give its spine sentence, rewrite
the screen. Polish never fixes a line that says the wrong thing.

## Question or statement

Not everything is a question. Pick by what the reader needs at that point.

- **A statement when the content is a step or a fact they just need to know.** Steps in a plan, what we do, what
  they get. Say it in "we" or "they" as a person would: "We collect each student's details with one form." "We help
  students form teams." A question here only delays the answer.
- **A question when the reader would actually wonder:** an open decision, a doubt, a choice they make. "What do
  students get?" (nobody has decided yet), "Where should we start?", "Who do we talk to?".
- **A choice the reader makes may be a question** ("Which farm problem will you pick?"), because they are the one
  deciding.
- **The hero can be the one big question the page answers,** or the plain promise.
- **Never a question whose answer is already on screen** (a "When do teams form?" page with a huge 4 printed on it),
  and never two questions in a row that ask the same thing ("Where should we start?" then "How do we start?").
- **Rough balance:** a plan or a process is mostly statements; a pitch to a client mixes both; a page about an open
  choice can lean on questions.

## The drawing carries the metaphor

- **Every line makes sense with the drawing hidden.** The metaphor lives in the picture and in small labels
  ("Handlebar: your leaders"), never in the headline sentence.
- **Explain the metaphor once, in plain words,** where it first appears: "We drew TVS as one of its own motorbikes.
  The frame is the TVS Way, how TVS already works." After that the reader never decodes it again.
- **No aphorisms or slogans.** "A dashboard shows trouble the moment it starts" sounds wise and says nothing about
  the reader.

## Plain, full sentences

- **Full sentences with a subject and a verb.** No fragments for rhythm ("The two-minute version."), no one-word
  sentences, and no things that act like people ("the full proposal waits on your laptop").
- **Instructions said straight:** "This is the 2-minute version. Open this on a laptop to see the full proposal."
- **Words the reader already uses.** Plain words first, the term second: "small supplier plants (MSMEs)". A term the
  reader uses every day (Dojo, NAAC A++, PG Diploma) stays as it is.
- **Explain or cut the sender's own words.** "Campus chit sheet" and "the dashboard" mean nothing to a student on
  day one: say what it is ("a list of real farm problems from your campus") or leave it for the full page.
- **No tagline or brand slogan anywhere on the page,** including small caps at the close ("Real Problems. Student
  Builders. Possible Ventures." is the banned tricolon). The logo is enough.
- **Ranges in words inside sentences:** "Days 5 to 8". A big printed numeral on a calendar page may read "5–8",
  because it is a drawn number, not a sentence.
- **The impact sits in the claim's own sentence:** "Many line checks still happen on paper, so a stopped machine is
  found late."
- **No hedges, no brochure lines,** no "not X but Y", no em dashes, no lead-ins ("Here's how").

## Cutting words without losing clarity

- **Headline: eight words or fewer.** "How do we help experts lead people?" (7) beats "How can JAIN support TVS
  leaders at every level?" (9).
- **One sentence under the headline, two at most.** Cut the setup sentence when the headline already carries it:
  "Who teaches experts to lead?" makes "TVS promotes experts for their skill, then asks them to lead" unneeded.
- **The card holds the proof,** so the body doesn't repeat it.
- **Name the sender once per screen.** The reader knows who is talking; "JAIN" three times on one screen is padding.
- **Cut what the picture already shows.** The big "14" needs no "on Day 14"; the live board needs no "Press 2 has
  stopped".
- **Keep the clarity.** If cutting a word makes the reader guess, put it back.

## Bold and cards

- **Bold the key phrase, never a whole sentence.** Reading only the bold gives the pitch.
- **Cards are labels:** one big plain phrase and one small line. Fragments are fine on a card because it is not a
  sentence.
- **A card carries one fact the headline doesn't:** a number, a name, a date, a result. "1 form" under "Fill in one
  form to start" says it twice; cut the card or give it something new.
- **On a phone page this file wins over `writing-rules.md` on emphasis:** bold the key phrase in the body; the
  marker sweep is for the card's big phrase only.

## Before and after

| Before | After | Why |
|---|---|---|
| Four things TVS asked for, on one bike. | How can JAIN help with the four things TVS asked for? | Says what the page answers; the bike is explained later. |
| The two-minute version. The full proposal waits on your laptop. | This is the 2-minute version. Open this on a laptop to see the full proposal. | Full sentences; a straight instruction. |
| TVS already has the frame. | What does the motorbike stand for? (then one plain explanation) | The metaphor is explained once instead of decoded. |
| Leaders steer. Let them see the road ahead. | How do we help experts lead people? | Says the need in the reader's words. |
| When do teams form? (on a page printed "Day 4") | We help students form teams. | A step is a statement; the day is already on screen. |
| How does a student join? | We collect each student's details with one form. | A plain step; nothing to wonder about. |
| What do students get? | What do students get? | Stays a question: it is still undecided. |

## The copy check

1. Put the spine sentences next to each screen's headline and bold phrase. Every pair must match in meaning.
2. Read the headlines alone, in order. They should tell the message without the body.
3. Count questions: none whose answer is on screen, no two in a row asking the same thing.
4. Run `python scripts/scan.py` (dashes, hedges, hype, negative parallelism, slot headings, unsourced numbers).
5. Put each card next to its headline: the card must add a fact. Repeats fail.
6. Check the reader's fears from the grilling: each is answered on the page or knowingly left out.
7. For phone pages, the critic agent in `phone.md` also reads every screen at three seconds each.
