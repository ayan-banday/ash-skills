# Example: the menu and one chapter Ash approved

Made beside the Fri Oct 30 grilling of Fuji ticket 34, where Ash designed a pipeline for reading YouTube transcripts. Match its shape, its plainness and its order of meaning before name. The quotes and timestamps in it are made up.

---

**Your chat has two big problems. The first unlocks the second: you can only map a new field once you can read its sources cheaply. Pick a question.**

**A. How do you get the useful ideas out of 20 hours of YouTube videos, without paying an AI to read all 20 hours every time you ask something?**
1. How do you stop paying an AI to re-read the same 20 hours of video every time you ask Shasta a new question?
2. How do you check that a cheap AI reading a transcript didn't skip the one line you needed?
3. How do you pay less for AI work that can wait until morning, like Fuji's night run?

**B. How do you get an AI to show you a whole field you know nothing about, like UI/UX, so you know what's worth learning?**
1. How do experts split a field like UI/UX into its main parts?
2. How do you find the parts of a field you've never heard of?
3. How do you tell whether a map of a field is good or just long?

**Pick a letter and a number, or ask your own.**

---

### How do you stop paying an AI to re-read the same 20 hours of video every time you ask Shasta a new question?

**Where you are now**
- **You have 20 YouTube transcripts** from Greg Isenberg, Lenny and others, about 20 hours of talk.
- **Each time you ask Shasta a question, a cheap AI reads all 20 from the start.** Ten questions cost ten full readings, and YouTube starts blocking you for fetching the same videos again.

**After you read this, you can ask Shasta any question about those 20 videos, any week, and pay for about one hour of reading instead of 20.**

**What usually happens**
1. **Monday:** you ask about pricing. The AI reads all 20 hours and gives you the quotes.
2. **Thursday:** you ask about landing pages. The AI reads the same 20 hours again, because nothing from Monday was kept except Monday's answer.
3. **Week 3:** you add two new videos. Now every question costs 22 hours of reading.

**Where the problem lies**

**The AI reads, answers and forgets.** Nobody wrote down what each part of each video is about, so every question has to start from the first word.

**The idea that fixes it**

**Have an AI read each video once, when it arrives, and write down what every two minutes of it is about. When you ask a question later, Shasta looks in that list, finds the few parts that match, and the AI reads only those.**

A textbook does this for you already. At the back is a list of topics with page numbers: "pricing: 42, 118". Someone wrote that list once, when the book was printed, so you find pricing in ten seconds without reading 400 pages. That list is called an **index**.

**How it works, from a new video to an answer**
1. **A transcript arrives.** Shasta cuts it into pieces of about two minutes, and each piece keeps its start time, like 31:00.
2. **A cheap AI reads each piece once** and writes one line about it: "31:00 Greg: charge before you build, the payment page is the test." All those lines go into one file, the index.
3. **You ask a question.** The AI reads the index, not the videos. For 20 hours of video the index is about 600 lines, a few minutes of reading.
4. **It picks the pieces whose lines match your question,** say 25 of the 600.
5. **A strong AI reads those 25 pieces and answers,** with timestamps. When a piece is too thin on its own, it reads the pieces around it, or the whole transcript.

```
ONCE, when a video arrives:
  transcript → 2-minute pieces → one line per piece → added to the index

EVERY question:
  your question → AI reads the index → picks the matching pieces
               → strong AI reads those (and more, if it needs context) → answer with timestamps
```

| | Shasta today | Shasta with an index |
|---|---|---|
| **A new question** | A cheap AI reads all 20 hours | The AI reads 600 lines, then about 25 pieces |
| **A new video** | Adds to the cost of every future question | Read once, 30 lines added to the index |
| **Where the answer came from** | You trust the AI | Every quote carries its minute in the video |

**How you'd build it, and what changes for you**

You need five parts. Each exists so the one after it has less to do.
- **A folder of transcripts,** one file per video. You have this.
- **A cutter:** a short script that splits each transcript into two-minute pieces with their start times. A plain program, no AI.
- **A labeller:** a cheap AI that reads each piece and writes its one line. Run once per video.
- **The index file:** every line from every video, in one place.
- **A finder:** an AI that reads the index, picks the matching lines, and hands those pieces to the strong AI, which can pull in more of the transcript when it needs context.

What changes for you:
- **A video is paid for on the day it arrives,** not every time you're curious.
- **Adding a video is one step,** and nothing else changes.

**How it looks when you use it**

> **You ask Shasta:** "What do my 20 videos say about charging money before the product exists?"
> **Shasta:** finds 25 matching lines in the index, from 6 of the 20 videos.
> **The strong AI answers:** "Four videos say to put up the payment page first. None of them talk about pricing for businesses rather than people."
> **What you paid for:** 600 lines plus 25 pieces, about an hour of video, not 20.

**Where else the same idea works**

**Far away: a restaurant kitchen**
- **Before dinner, cooks spend two hours chopping onions, making sauces and cutting meat.** Chefs call it **mise en place**: everything in its place.
- **During dinner, each order takes four minutes,** because it's put together from food that's already prepared.
- **A kitchen that cooks every order from raw onions is Shasta today.** It works for one table and falls apart when the restaurant is full.

**In your world: Udyaan's weekly reflections**
- **120 students write one reflection each week.**
- **The day one comes in, a cheap AI writes one line about it:** "Rhea, week 3: stuck on what to charge, scared to ask."
- **In week 3 you ask "Who is stuck on pricing?"** The AI reads 120 lines and opens the six that match.

**When it isn't enough**
- **Up to a few hundred documents, a written index wins.** It's cheap, an AI reads it in minutes, and a wrong line can be fixed by hand.
- **Past a few thousand pieces, the index gets too long to read every time.** Then each piece becomes numbers, so pieces about the same idea sit close together even when the words differ; those numbers are called **embeddings**, and the method built on them is **RAG**.
- **The test:** if the index can be read in under five minutes, keep it written. If not, move to embeddings.

**The answer**

**Every video gets read once, when it arrives, and a cheap AI writes one line per two minutes into one file, called an index. A question reads the index and then only the matching pieces.** You pay for each video once, and every answer points at the exact minute. A kitchen does the same with mise en place: the slow work happens before anyone orders.

**Want to save these questions?** (A1 with this chapter, plus A2, A3 and B1 to B3)
