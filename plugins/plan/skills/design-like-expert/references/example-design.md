# Example: a menu and one design

Made beside a Fuji session where Ash planned how Shasta reads YouTube transcripts. Match its shape, its plainness, its order of meaning before name, and how the design draws the thing itself. The numbers and quotes are made up.

---

**The prompt I gave myself:** *You've built search for libraries and newsrooms for ten years. Ash opens Shasta on a weeknight with 20 minutes to learn about pricing. What are the two questions he's really asking, and what's the smallest thing that answers each?*

**Your chat has two big problems. The first unlocks the second: you can only map a new field once reading its sources is cheap. I'd start with A.**

**A. How do you get the useful ideas out of 20 hours of YouTube videos, without paying an AI to read all 20 hours every time you ask something?**
1. How do you stop paying an AI to re-read the same videos every time you ask a new question?
2. How do you check that a cheap AI reading a transcript didn't skip the one line you needed?
3. How do you pay less for AI work that can wait until morning?

**B. How do you get an AI to show you a whole field you know nothing about, so you know what's worth learning?**
1. How do experts split a field like UI/UX into its main parts?
2. How do you tell whether a map of a field is good or just long?

**Pick a letter for the whole design, a number for one piece, or name your own.**

---

*(Ash: A1)*

### How do you stop paying an AI to re-read the same videos every time you ask a new question?

**The real problem**

**Every question to Shasta pays for reading all 20 hours of video again.**
1. **Monday:** you ask about pricing, and an AI reads all 20 hours to find six quotes.
2. **Thursday:** you ask about landing pages, and it reads the same 20 hours again, because nothing from Monday was kept.
3. **Week 3:** you add two videos, YouTube starts blocking the repeat fetches, and every question costs 22 hours of reading.

**Done when:** by Sunday, a new question about the 20 videos costs about one hour of reading, and every answer points at the minute it came from.

**Where the problem lies**

**The AI reads, answers and forgets.** Nobody writes down what each part of each video is about, so every question starts from the first word.

**The idea**

**Have an AI read each video once, when it arrives, and write one line about every two minutes of it. A later question reads those lines first, and the AI opens only the parts that match.**

A textbook's back pages say "pricing: 42, 118", so you find pricing without reading 400 pages. That list is called an **index**.
- **Far away:** a restaurant kitchen chops onions and makes sauces for two hours before dinner, so each order takes four minutes. Chefs call it mise en place.
- **In your world:** when a Udyaan student's weekly reflection arrives, a cheap AI writes one line about it, so "who is stuck on pricing?" reads 120 lines, not 120 reflections.

**The design**

The index is one plain file, one line per two minutes of video:

```
greg-isenberg-pricing.md
  00:00  Greg: why most first products are priced too low
  02:00  Greg: charge before you build; the payment page is the test
  31:00  Greg: one customer paying beats ten saying "cool"
lenny-landing-pages.md
  00:00  Lenny: the first screen answers "is this for me?"
  ...

A question:  read the index → pick ~25 lines → open those pieces → answer with minutes
```

Build order: the cutter, then label one video and read its lines, then the rest, then point Shasta's question step at the index.

**What stays, what changes**
- **The transcripts folder stays as it is:** one file per video. Have it.
- **A cutter splits each transcript into two-minute pieces with start times.** New, a short script with no AI.
- **The labeller writes one line per piece.** Reuse the cheap model the night run already calls.
- **The index file holds every line.** New, `shasta/index.md`.
- **Shasta's question step reads the index first,** then opens only the pieces it picks. Reuse it, pointed at the index.
- **The night run labels any video added that day.** One new job in a run you have.

**Checks:** read one labelled video's 30 lines against the video once; ask last week's pricing question again and get the same quotes.

**Left out, and why**
- **A search database (not needed):** an AI reads 600 lines in a few minutes.
- **Re-labelling old videos with a better model (later, when an answer misses a quote you know is there).**

**When it stops working**
- **Past a few thousand pieces, the index takes too long to read every time.** Then each piece becomes numbers, so pieces about the same idea sit close together even when the words differ; those numbers are called **embeddings**.
- **The test:** if the index reads in under five minutes, keep it written. If not, move to embeddings.

**Your call**
1. **Shasta's index will be about 600 lines for 20 videos, across Technology and Marketing.** Should it be one file per field, or one for everything?
   - A. One per field, so a pricing question never reads the UI/UX lines (recommended).
   - B. One file for everything, simpler until there are a few thousand lines.
2. **Every later answer trusts the labeller's lines.** Should you read the first video's lines before the rest are labelled?
   - A. Yes: one video, about 30 lines, five minutes (recommended).
   - B. No, check only when an answer looks wrong.

**Say "A to all" or change any.** A2, A3 and B are their own designs. **Want the chapter on the index?**
