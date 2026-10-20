# How the TVS site was made: feedback rounds, reviews, decisions

Background for this skill. Ash's feedback on "Carrying the TVS Way" in his own words, what changed after each round, what the reviewers found, the Anthropic design teardown, the reference-video method, and every decision with its reason. Read it when a rule in SKILL.md needs its reason, or when a new brief resembles TVS.

## 1. Ash's feedback, in order, and what changed

### Round 1: the original brief on the old 13-page brochure (07:30)
- "the thematics is not specific enough and we're not telling a singular story."
  → Story rebuilt around TVS's needs: one line plus three outcomes, every JAIN unit placed inside the outcome it serves.
- "these are the problems you may have from our discussion, these are the university resources we have, and this is how it gets mapped."
  → Problem, then resource, then mapping became the page order.
- "instead of having a long list of eight things, we want to structure it much more around the impact"
  → The eight-department catalogue was dropped for outcome sections.
- "For the titles instead of "A Shared Opportunity," make it a little bit more specific."
  → Headline rewrites ("A shared opportunity" became "What we heard from TVS IQL", and so on).
- Next steps: "Identify priority areas", "Confirm institutional representatives", "How would we scope the problem, approval"
  → A 90-day page with named owners on both sides (later replaced by three pictured steps).
- "TBS is actually TVS. You can go ahead and confirm the facts within the documents I've given."
  → Fact-check agent; it found TVS IQL and IFQM are different bodies, which became question 1.

### Round 2: answers to four clarifying questions (AskUserQuestion, 07:51)
- Proof question answered "Mention vaguely".
  → Past tools (QCMS, EIT) never named; "JAIN has already built digital tools for TVS".
- "IKS is one of the most important ways because they described it themselves. It is a very named concept"
  → "The Indian way of doing things" became the thread, with IKS in bold and a concrete use.
- "confirm what you understand, its specifications, and the design we're going to use... Get me a proposal."
  → `JAIN x TVS IQL Brochure Proposal.md`: understanding, story, 12-page plan, design (polished-doc PDF, JAIN maroon). A Sonnet "builder check" agent reviewed it before hand-over.

### Round 3: /jmo-workflow:better-ui with claude.com/product/overview (08:16)
- "The CMDC thing is just an interview that can be helpful to create the leadership study material"
  → CMDC reduced to "JAIN's interview method" in the supplier story.
- "nothing gets in isolation... why should they care? We have this capability, and this can impact you."
  → Hard rule: no buzzword in isolation. Seeded the jargon translator.
- "We don't want to commit to an ITD plan, but we want to show them the steps"
  → Dated plans removed; one example project shown as steps, labelled as an example.
- "I want to follow something like what Anthropic does... this connecting line across each data point."
  → Live DOM teardown of claude.com's constellation map and time rail; the page thread idea.
- "suggest really fucking creative ways for us to communicate that while not fully depending on words."
  → "Five ways to tell it" (kolam, transit map, jargon translator, pick your layer, paper companion) shown with an inline storyboard widget; recommended kolam + translator + mind map + rail pilot; palette "indigo and turmeric".
- "We can just have that as a website link"
  → The deliverable became a single-page website artifact.
- "The point is to be creative as fuck." / "Yet, still being clear, that's the most important part"
- Also asked for a compaction prompt first, in chat, not markdown (see section 8).

### Round 4: the prototype brief (08:33, with claude.com/resources/articles, the LinkedIn video, two images)
- "I wouldn't want it to have rails. I wouldn't want it to have them choosing their own adventure."
  → Rail with role picker dropped. Sequential page only.
- "It's going to be more like feeding it down the throat because I want them to understand things"
  → One fixed scroll order, no branching.
- "We can have the Golem thing. I would love to have an Indian-inspired design there." / "of course we need the translator."
  → Kolam motif and translator kept.
- "'Pick your layer': I don't want that." / paper companion: "I don't want that."
  → Both cut.
- "I don't want you to add any information from Charlotte. Truncate that."
  → Udyaan's four gates removed; memory file `feedback-no-vault-content-in-client-work.md` written.
- "I want to still see another example where we can demonstrate the Indian way of doing things"
  → Pilot two: a guru-shishya mentoring pilot for Dojo trainers (later drawn as the teaching circle).
- "I don't trust your abilities to create really good design. I want the look and feel of Anthropic's design."
  → Three background research agents (design teardown, GitHub scout, skills scout).
- "I don't want videos and things like that."
  → All motion built in code.
- "taking what somebody has already built... making it much better and specific to us so it doesn't look like a random HTML file."
- "They use really good icons and I want to have kind of like those icons as well."
  → Icon study in the teardown; inline `<symbol>` icon set with a wobble filter.
- "that video is absolutely core. Have something like that inside the website."
  → ffmpeg frame study (section 5); translator card copied the film's prompt card and marker.
- "curves going through each slide that actually showed that there's something else going on."
  → A page-long scroll thread (later cut).
- "create me a very small prototype so that I can actually see if we're moving in the right direction"
  → Prototype v1: particle swarm settling into a kolam, translator card, constellation map, one thread. Creative-director agent reviewed it; fixes applied; published privately.

### Round 5: first feedback on the prototype (08:52, with the Udyaan PDF, a prototype screenshot and a kolam photo)
- "I don't like the first color, the Jain University blue."
  → Navy hero #161A2E dropped. New "threshold" palette: dark wood ground with rice-powder white, haldi, neel, laterite, kumkum.
- "when you open the first page it doesn't show the entire thing. Right now the other content is bleeding into it"
  → Hero set to a full screen (100svh); nothing from the next section shows.
- "the line going through it is distracting from the message"
  → Page-long thread removed; replaced by mini motif badges and lines kept inside each visual.
- "Instead of having all the data packed into the headline, I want it to tell us what the section is about"
  → Headlines name the section plainly; detail moved to body.
- "the different types of motion design we can have, and the different types of visual artifacts"
  → More pattern variety (layers ladder, paper-vs-live screen, mini badges).
- "We're not trying to have emotional or informational density."
- "I want to see improvements in the copywriting as well, with copy that tells a story."
- On his PDF: "see the way I write things: everything is focused on clarity. That's what I want you to learn."
  → Copy model: open with the reader's ask in their words, map each ask to where it is answered ("You told us" blocks, need cards with "Answered by" chips).
- "Have Fable 5.0.1 as your advisor model"
  → Fable "uninitiated reader" clarity review.
- "the Kolam that you had given us, it was not specific to that. It doesn't look like a Kolam."
  → Kolam rebuilt on a separate test page to match his photo (cube of three rhombi with curls, three triple-strand interlaced bands, six petal flowers with lattice and fringe), chalk filter, wood ground.
- "Go ahead and plan it out and think through it... give me a high-fidelity draft."
  → v2 published at 09:10.

### Round 6: detailed feedback on v2 (09:29)
- "it's not that we're building leaders at every level of TVS. It's more like we're supporting them and giving them data"
  → Leaders copy reframed as support and data.
- FMS: "Make it a little bit more visible and a little bit more bold, so things actually jump out to them."
- "instead of just making it bold, with different color palettes that make the text that is important get highlighted."
  → One chip colour per JAIN team; marker highlight on the payoff phrase.
- "JAIN Online: make sure the visual weights are there, because right now I can't tell the difference."
- "Indian Knowledge System: how TVS uses it? It's not specific enough."
- Systems: "it's also the processes that are not yet digitified: the sensors on the machine and EV, etc."
  → Systems copy covers sensors and EV work, not just paper.
- Pilot one: "Show that in less of a stepwise, horizontal way."
  → Orbit: project in the centre, five steps on an ellipse, a travelling dot, then a fork where TVS chooses scale, extend or stop.
- Pilot two: "step one: payer capture, shape, measure. It's not clear enough to tell me what exactly is going on."
- "I want something that's kind of non-linear, but not so much. Think about the mind map we have."
  → Teaching circle: guru at the centre, ring of new hires, four corner callouts highlighting in turn.
- "Right now, the last step is absolute garbage, and the CTA needs to be extremely clear."
  → Three pictured steps: choose an area (list with one hand-circled), one point of contact, a draft proposal.
- "circle things out so it's easier for them to see (more visual kind of shit), and name the people"
- "His name is Gento... make him into a nice person that's abstractly shown"
  → Named contact (Jinto Johnson, spelled from his email) with a persona disc and a contact card with a Copy button.
- "add a little bit more of a funk there"
  → Action need headlines: "Give every leader the full picture", "See inside your supplier plants", "Bring every process online", "Make ideas easy to see and teach".
- "we don't want to take too much credit. It's more like, "How can we collaborate?" so we're not roasting them."
  → Collaborative headlines ("How JAIN can support...").
- "CMDC School of Design faculty... It's kind of garbage right now."
- "School of Design comes at a stage where they have that, kind of like a snake going on."
- "It's not a list of things. It's more importance-based: what problem each faculty designs."
- "this is far too lazy to have a horizontal thing going on"
  → The snake: problem-first stop cards alternating left and right, one scroll-drawn line through numbered knots, a dark "Where this leads" end card. v3 published 09:37.
- Closing instruction: "Go make those changes"

### Round 7: phone gate (09:47)
- "if they open it on their phone, the only thing that they see is, open this on your laptop."
  → Gate at max-width 760px with a turmeric laptop sketch on wood.
- "If you're reasonably sure, then you don't have to do a thorough double check."

### Round 8: queued mid-turn message (09:48)
- "the Jinto person image, I don't want it to be like a generic image"
- "make it something that looks unbelievably like, yeah, this was created by the same designer"
  → Portrait redrawn as a chalk line drawing on wood inside a two-strand kolam braid around 12 pulli dots, with the turmeric knot; draws itself on. Refined after self-review (hair read as a helmet, dot eyes as an emoji). v5.

### Round 9: name and tablets (09:55)
- "his spelling is, by the way, Jento as well."
  → Kept "Jinto" because it matches the email.
- "Some people use Samsung tablets or an iPad as their laptop"
  → Gate changed from 760px to the screen's short side under 540px (CSS plus JS). Tested iPad mini, iPad portrait and landscape, Galaxy Tab. Tilt removed below 820px and `overflow-x: clip` added. v6.

### Round 10: bug screenshots, original session only (10:04)
- "There are a lot of places where the things are not loading up properly."
- "verify that things work fully and properly, and that it's production-ready."
  → Three screenshot bugs fixed, a class-collision scan, an independent QA agent at five sizes, ten more fixes. v7 at 10:27.

### Round 11: skill request, fork only (10:09 to 10:23)
- "codify all of this into something that can be used for any next project of mine."
- "the decisions we took along the lines of having inspirations that you can ask for... the cobra thing"
- "If it doesn't have the inspiration, it can give me some options"
- "Make sure that it's not just the things that we did, but also the things that we could have done instead"
- "Of course, it runs the verifier at the end"
- "presenting things in really different ways that are even more creative than the clear document skill."
- "lists are not lists, and it's clear."
- "it understands that and then can apply that to any way in different color schemes, different designs."
- "have an orchestrated agent that makes sure that the design quality seems in the taste and manner"
- "Give me a test skill that is at the level that we can create documents like that in one shot."
- "I don't want you to just catalog the TBS patterns only."
- "It's going to be a lot bigger of a catalog... it needs to be pretty thorough and specific and a pretty huge catalog."

---

## 3. Reviewers' main findings and what was applied

### Builder check on the proposal (Sonnet, foreground)
Seven ranked questions a builder would need answered: is the current brochure available and final (logo, maroon, fonts, photos); where "in their words" quotes come from; the page-12 action, date and contacts; whether the IKS and Talent pages can ship as drafted; whether pilot ideas are invented; whether polished-doc scripts exist; exact unit names.
Applied: answered in the proposal or surfaced to Ash as three open items (contacts and date, IKS offer and KEMI, FET's official name). Unconfirmed items ship as highlighted placeholders.

### Tough creative director on prototype v1 (Opus, background)
- Works: palette, Newsreader with mono eyebrows, the translator card as the closest echo of the film, the knots idea, hero pacing.
- Problems ranked: (1) translator gives definitions, not impact on TVS: add "So at TVS:" and group terms by need; (2) glossary under the card spoils the animation, and striking through JAIN's own capability names reads badly; (3) the thread hurts layout: stray scratch in the hero, slices the map label, leaves the right edge, hidden on mobile; make it the kolam line itself; (4) the map is "a static Visio tree": add node dots, idle drift, edge pulses, tap to open, delete the bridge line through "Suppliers", hide the hover note on touch; (5) little of the film's language came through: no word-built shapes, pink panel, head window or grain; swarm is a "diagonal smear"; kolam "reads as chain-link fence".
- Verdict: "better than a random HTML file and well short of Anthropic-level." Single biggest move: make the kolam line the page's structure.
- Copy: headings that describe instead of answer ("Every capability, said in your words", eyebrow "How we get there"); unexplained jargon (CMDC, FET, ECE, Industry 4.0, CS & IT, E & EE, IKS, Launchpad); a contradiction (capsules for shop-floor staff vs leaders); a possible overclaim ("counts toward a degree"); scaffolding text ("Prototype · three of seven sections").
- Applied in one pass: "So at TVS" line on the translator; thread starts in the kolam and ends at the map centre; map got node dots, distance-based growth and pulses; wider swarm; paper grain on panels; copy fixes. The later Fable review saw no glossary under the card, so it was removed. Not applied: word-built shapes, pink panel, head-silhouette window (listed later as "ideas from the film not used yet"). Superseded by Ash's next round: the thread was cut entirely and the kolam rebuilt from his photo.

### Fable "uninitiated reader" clarity advisor on v2 (model `fable`, ran as claude-fable-5-1)
- 3-second test passed: the hero reads as "JAIN's written answer to things TVS asked for at a meeting". The "Answered by" tags were called the best thing on the page.
- Findings: kolam key restated the needs under new names and "The TVS Way" was undefined (two maps of one thing); "You told us" wording did not match the need cards; CMDC and MSME never explained; auto-playing six-term carousel on a 6.8s clock (reader cannot set the pace); jargon (stewardship, value chains, powertrain, motion artists, incubator); overreach (measuring change level by level with no capability shown; outcomes stated as fact; Arthashastra beyond the facts); hedge "Students could work..."; visible placeholder stub text.
- Top three: one wording per need everywhere; cut the kolam key to a caption; replace the carousel with a static list and spell out CMDC.
- Applied (`fix_copy.py`): one wording per need reused word for word; "small supplier plants (MSMEs)" and "CMDC (JAIN's interview method)" glossed on first use; "The TVS Way" defined; kolam key legend uses the exact need names; overclaim rewritten to "Get a short report after each programme on what changed at each level"; "The goal:" before outcomes; Arthashastra replaced by "Ideas on duty and good leadership from Indian texts"; pilot intros tied to named needs; "An example, chosen to show the steps"; map leaves renamed to the section team names; "motion artists" became "video makers"; powertrain glossed.
- Two judgment calls against the advisor: the kolam key stayed (Ash asked the kolam to carry the story) but was tied to the need names; the translator kept its animation but its progress bars became tappable buttons so the reader sets the pace (the static list was rejected).
- The copy scan (polished-doc `scan_copy.py`) then caught "Nothing here is fixed yet" as a hedge; cut.

### Production QA sweep on v6 (Opus, background)
Ten findings, no blockers; all fixed in `fix_qa.py` (details in section 7). Verified working: no horizontal overflow, no console errors, phone gate, kolam legend, snakes switching to a vertical timeline at 768, translator jump, map halos and hover dimming, orbit and fork, Copy fallback.

### Research agents (what they found and what was used)
- Brochure craft (Sonnet): university partnership pages (Imperial, NUS, Cambridge Judge, Stanford, MIT ILP) lead with catalogues, so leading with partner problems stands out. Principles: their problem in their words; outcome headlines; headline-only test; three themes; group by problem; one map; repeat problem, what we bring, what changes; one framing line for "proposed" status instead of hedging every line; diagnose-first; one named next step; short copy. Used in the proposal; the dated 30/60/90 plan was later dropped at Ash's request.
- Vault mining (Explore): transferable rules (headings state the answer, pain before product, specificity, never invent a number, one example carried through, regroup long lists, visuals only where content has a shape, end on one action); voice bans; warned that brief-page defaults to forest green #1D5A47 and must be overridden; flagged Udyaan's status as unclear. Ash later cut all vault content.
- TVS fact-check (Sonnet): TVS IQL is TVS Motor's corporate university at Attibele (learning centre 1987, IQL 2011, corporate university 2018, six academies); the MSME clusters, JUSE links, "Indian Way" and Viksit Bharat language belong to IFQM, a separate foundation; "Three I" unidentifiable; QCMS and EIT not public. Phrases to mirror: TVS Way, Dojo, Daily Work Management, First Time Right, "Inspire Learning to Excel". Used: Ash chose to address IQL anyway; "Three I" never named.
- Skills scout (Sonnet): use frontend-design (direction plus anti-default critique), animate, better-ui, brief-page QA scripts (skip its look), polished-doc `palette.py`; impeccable and ui-ux-pro-max worth installing only with Ash's approval (never approved); skip web-artifacts-builder, canvas-design, algorithmic-art, brand-guidelines, theme-factory.
- GitHub scout (Sonnet): GSAP 3.15.0 is fully free including ScrollTrigger, DrawSVG, ScrambleText, SplitText, MorphSVG; Lenis 1.3.27 optional; rough.js 4.6.6 for sketchy shapes; wobble filter by hand; no kolam library exists (write one); d3-force unnecessary for a fixed radial map; CSS `:has()` hover-dim one-liner. Study: ncase.me/trust, plastic-ocean.com, The Pudding, Codrops scroll-driven SVG map article. The final build stayed vanilla JS and SVG.

---

## 4. Design teardown of anthropic.com and claude.com

Method that worked: WebFetch returns stripped text, so the agent pulled raw HTML, CSS and SVG with curl and read them as text. The main thread also inspected claude.com live in the browser pane with `javascript_tool` (class names, computed styles, transitions).

### Colour (read from `--swatch--*` on anthropic.com and `--color-*` on claude.com)
- Neutrals: ivory #FAF9F5, #F0EEE6, #E8E6DC; oat #E3DACC; cloud greys #D1CFC5, #B0AEA5, #87867F; slate #5E5D59, #3D3D3A, #141413.
- Tints for colour blocks: cloud #C5D3E0, heather #CBCADB, peach #EBC9B7, cactus #BCD1CA, coral #EBCECE, manilla #EBDBBC, matcha #CED6BF, orchid #E5CADA.
- Strong colours, used rarely: clay #D97757 (accent #C6613F), sky #6A9BCC, olive #788C5D, fig #C46686, plum #827DBD, kraft #D4A27F.
- Illustrations use three fills only: ivory #FAF9F5, ink #141413, sometimes sky #6A9BCC.
- Principles: warm yellow-grey neutrals, never pure white; tints at about 80 to 90% lightness and 15 to 35% saturation (chalky); one strong accent, rare; each section or card is one flat block; ink and paper flip on dark sections; hover moves one step along the same ramp.
- Agent's proposed palette (split-complementary, low saturation): paper #EEEAE0, card #F7F4ED, ink #1C1F2B, muted #5A5E6B, hairline ink at 12%, accent indigo #3F4A7A, turmeric #C9963A (illustration highlights only), section tints neel #BCC5D4, haldi #E6D3A5, laterite #CC9A85, closing CTA indigo night #232A44. Indigo #3F4A7A survived into the final palette; the tints were adjusted (final haldi #ECD9A6, neel #C6CFDA, laterite #DDB09A).

### Typography
- anthropic.com: Anthropic Sans headings bold, 4rem, line-height 1.1, letter-spacing 0, `text-wrap: balance`; body Anthropic Serif 1.125 to 1.5rem, line-height about 1.5.
- Articles: Copernicus display weight 400, line-height 1.2, 48px (-1.44px) and 64px (-1.92px), about -0.03em; Styrene sans display weight 500, line-height 1.0 to 1.15, about -0.02em; body 17 to 20px, line-height 1.55; `font-feature-settings: "pnum","lnum","liga"`.
- Google Fonts picks: Newsreader (opsz 72, 400, -0.025em) or Source Serif 4 Display; Instrument Sans or Hanken Grotesk 400/500; IBM Plex Mono labels; Noto Serif Kannada or Devanagari if Indic script is needed. Final: Newsreader, Hanken Grotesk, JetBrains Mono, Caveat.

### Illustrations and icons
- Article-card art is static SVG on a 1000x1000 square, 10 to 40 KB, 2 to 7 paths. A CMS `lottieUrl` field exists but was null everywhere.
- No `stroke` attributes: drawn by hand with a brush, vectorised, outlines filled, so line width wobbles. Two-tone: ivory silhouette under black line shapes, sometimes one sky-blue area. Line weight about 1.5 to 2.5% of the frame (estimate).
- Framing: 120px art (240px on featured cards) on a 16:10 plate in a theme tint, inside a card with a 1px border and 16px radius.
- Make our own: draw with a dry-ink brush, trace with vtracer, potrace or Illustrator, keep two layers. Code options: perfect-freehand (closest), rough.js roughness 0.6 to 1 and bowing 1, or an `feTurbulence` 0.02 + `feDisplacementMap` scale 2 filter over Tabler or Lucide icons. Nearest ready sets: Streamline Freehand, Doodle Icons.
- Painterly images are PNG/JPG. claude.com puts a brush texture over panels with `mask-image` (`--ov-tex`, alpha 0.8) and shows photos in grayscale with `mix-blend-mode: multiply`.

### Motion
- Easing tokens: out-power2 `cubic-bezier(.25,1,.5,1)`; out-expo `(.19,1,.22,1)`; out-quart `(.165,.84,.44,1)`; travel `(.77,0,.175,1)`.
- Reveal: opacity 0 and `translateY(10px)` to rest over 0.75s out-power2, 0.1s stagger. Headings: each word fades in over 1s.
- Constellation map: starts when 25% visible (IntersectionObserver plus scroll fallback). Labels start at `translateY(18px)`; opacity 0.5s, transform 1.1s out-expo; delay = 0.08 + 0.72 x (distance from centre / largest distance). Lines: `pathLength="1"`, `stroke-dasharray: 1`, dashoffset 1 to 0 over 0.9s. Primary lines 1.67px, secondary 1.11px, grey #D1CFC5.
- Hover dimming: inactive labels to opacity 0.22, lines to 0.55, active to 1, 0.3s transition.
- Step panel: active step springs with `cubic-bezier(.34,1.42,.64,1)` over 0.52s, scale 0.965 to 1. Vertical 1px "loom" line driven by `scaleY(var(--loom-line))`.
- Colour hovers 0.2s; cards gain a shadow.
- anthropic.com's large CTA block: GSAP ScrollTrigger scrub 0.8, grows from an inset rounded card to full width, radius to 0, power2.out.
- Everything off under `prefers-reduced-motion`.
- Main-thread live inspection of the claude.com time rail (`RolesBand__timerail`): 15 ticks, each 15px x 1px, rgb(48,48,46), `transition: background-color .25s .085s`; the dot moves with `transform 0.6s cubic-bezier(0.77,0,0.175,1)`; a role picker (Everyone, Marketing, Sales, Finance, HR, Legal, Product) swaps the whole day; each stop swaps the headline and plays a scripted demo with Replay. The constellation (`ConstellationMap` module) is one SVG of lines with HTML labels on top and becomes a grouped list on mobile. Neither uses an animation library.

### Layout
- anthropic.com: site width 89.5rem (1432px), 64px side margins, 12 columns, 2rem gutters; narrow content 56.25rem (900px). Section spacing tokens 2, 4, 6, 10, 14rem; 12rem at the top.
- Articles: grid to 1920px, margins 32, 48, 80px by width.
- claude.com constellation frame: 1456x695 desktop, 780x640 tablet, 360x900 mobile. Radii tokens 8, 16, 24px.
- Rhythm: lots of ivory space, then one full-width tint block per idea.

### The connecting curve
Not present on either site as one continuous curve. Nearest: the constellation threads and the loom line. Build recipe given: one absolutely positioned SVG over the page; cubic Bezier through an anchor per section, recomputed on resize; `pathLength="1"`, `stroke-dasharray: 1`; dashoffset from 1 minus scroll progress (ScrollTrigger scrub about 0.8); node circles appear as progress passes anchors; 1.25 to 1.6px, `vector-effect: non-scaling-stroke`, ink at about 45% or laterite; reduced motion draws it whole. Lesson: Ash then found the page-long version distracting, so keep lines inside visuals or gutters.

---

## 5. Video study method and what the reference video taught

The video: `C:\Users\ayanb\Downloads\linkedin-video.mp4`, 33 MB, 1138x640, 30 fps, 327 s (about 5.5 min). Ash called it Anthropic's "global workspace" research film. It was never loaded into context; only frames were.

Environment: ffmpeg 8.1.1 was on PATH (WinGet Gyan.FFmpeg). Python `cv2` and `imageio_ffmpeg` were not installed.

Commands, in order:
```bash
ffprobe -v error -show_entries format=duration:stream=width,height,r_frame_rate,codec_type -of compact "C:/Users/ayanb/Downloads/linkedin-video.mp4"

D=".../scratchpad/video"; mkdir -p "$D"; cd "$D"
ffmpeg -v error -i "C:/Users/ayanb/Downloads/linkedin-video.mp4" -vf "select='gt(scene,0.25)',scale=380:-1,showinfo" -vsync vfr f_%03d.jpg 2> info.txt
ls f_*.jpg | wc -l                      # 19 scene frames
grep -o "pts_time:[0-9.]*" info.txt     # timestamps of each scene change

ffmpeg -v error -i "C:/Users/ayanb/Downloads/linkedin-video.mp4" -vf "fps=1/6,scale=320:-1,tile=6x5:padding=4" -frames:v 2 sheet_%d.jpg
ffmpeg -v error -i f_%03d.jpg -vf "tile=5x4:padding=4" -frames:v 1 scenes.jpg
```
Then `sheet_1.jpg` and `sheet_2.jpg` were read as images (one frame every 6 s, 30 per sheet, covering the whole film). The same two sheets were handed to the creative-director agent as the reference.

Observation from viewing the outputs while mining (not stated in the session): the scene-change filter at 0.25 spent 18 of its 19 frames on the noisy particle-swarm stretch, because particle motion trips the scene detector. The fixed-interval contact sheets carried the whole narrative. For films with particles or grain, lead with `fps=1/N` tiles and treat scene detection as a supplement (or raise the threshold).

What the film shows (frame by frame on the sheets): painterly sailing ships on a desaturated sea; white line-drawn fish on black; a particle murmuration; a head silhouette used as a window onto the sea scene; clouds and a boat built from repeated words ("CLOUDS", "BOAT") with a small black label tag; thought bubbles inside a head ("I'm tired", "4y=20", a paper boat); a flat pink panel with a rounded prompt card ("(4 + 17) * 2 + 7 =") where one token gets a yellow marker, beside a shape built from repeated numbers; a butter-yellow panel with a prompt card and a marker-highlighted phrase, beside a bridge built from words; black panels with a bilingual prompt card; grey word-fields with a red highlighted cluster; a starling murmuration in a painterly sky; a crow, a flag, a ship; the logo.

What it taught, and what was used:
- Used: the prompt card with a typed prompt and a yellow marker sweep became the translator card ("We call it" typed in mono, "It means" word by word, "So at TVS" marker); the marker became the page's emphasis device; flat colour-block panels became one tint per section; calm pacing set slow reveal timings; paper grain on panels.
- Prototyped then cut: the particle swarm settling into a shape (the hero swarm, cut when the kolam carried the hero).
- Not used yet: shapes built from repeated words; the head silhouette as a window; flat pink and butter panels; painterly public-domain art (Daniell's Madurai aquatints were suggested as the Indian analogue).
- The creative director's verdict was that "little of the film's visual language came through": borrowing one device (the prompt card) is not enough; pick two or three signature devices and build them properly.

---

## 6. Decisions, reasons, and alternatives rejected

### Audience and content
- Address TVS IQL, keep the MSME theme. Reason: Ash said "We're mostly focused on TVS". Rejected: readdress to IFQM; a joint IQL and IFQM brochure.
- Never name the past tools; "Mention vaguely". Rejected: QCMS and EIT as the headline proof.
- Never name the "Three I" framework. Reason: no public source matches it.
- IKS and "the Indian way of doing things" as the thread. Reason: TVS named the concept themselves, so it is their language.
- No Charlotte vault content (Udyaan's four gates cut). Reason: "I don't want you to add any information from Charlotte."
- Collaborative tone, no credit-taking. Reason: "we're not roasting them".
- Sourced numbers only (75+ startups, NAAC A++); outcomes softened to "The goal: ...". Reason: no invented numbers; the Fable advisor flagged outcomes stated as fact.
- Name a real contact from his email (Jinto Johnson) over Ash's dictated spellings.

### Format and structure
- Website over PDF. Reason: Ash allowed "a website link", and motion adds clarity ("we can communicate much more"). Rejected: the 12-page polished-doc PDF in JAIN maroon (the first proposal); the "copy deck + page spec" option offered in the clarifying questions.
- Sequential only. Reason: "feeding it down the throat". Rejected: claude.com-style rail with a role picker; "Pick your layer"; any choose-your-own-adventure.
- Story order: hero with the point, "What you told us" need cards, motif key, one section per need (badge, "You told us", example visual, snake), translator, the Indian way, mind map, two worked examples, how we start. Reason: Ash's PDF model (ask in their words, then where it is answered).
- No dated plan. Reason: "We don't want to commit to an ITD plan". Rejected: the 90-day timeline page and the 30/60/90 pattern from the craft research.
- CTA as three pictured steps plus a named contact. Reason: the earlier step list was "absolute garbage".
- Paper leave-behind with QR code: rejected ("I don't want that").
- Transit-map metaphor (lines are needs, stations are teams): offered as the fallback if the mind map read as decoration; never needed.

### Visual system
- Kolam as the motif. Reason given: it is a dot-grid line drawing done at doorways each morning, Tamil, and TVS has Tamil roots; it gives "the Indian way" and "connecting lines across data points" in one image before anyone reads. The motif carries the story: centre = the TVS Way, strands = needs, flowers = design.
- Kolam geometry from Ash's reference photo, tuned on its own test page (`preview/kolam.html`). Rejected: a generated mirror-curve lattice (read as circles, then "chain-link fence").
- Palette: "threshold" (wood, rice powder, turmeric, kumkum) derived from the motif's own materials. Rejected: "indigo and turmeric" night hero #12142A / #161A2E (Ash disliked the navy); JAIN maroon #6E0E29 and Georgia Pro (old brochure look); Anthropic's clay and ivory; green.
- One chip colour per JAIN team, reused everywhere that team appears. Reason: Ash wanted FMS and JAIN Online to "jump out" with colour, not bold alone.
- Marker highlight on the payoff phrase. Reason: Ash asked for colour highlighting; the film's marker device.
- Mini motif badges per section. Rejected: the page-long scroll thread (tried, "distracting from the message").
- Snake for "who does what". Rejected: team lists ("garbage") and horizontal step strips ("far too lazy").
- Orbit plus a three-way fork for pilot one; teaching circle for pilot two. Rejected: horizontal steps ("less of a stepwise, horizontal way").
- Persona portrait in the page's own language. Rejected: a generic avatar.
- Single light-paper theme with dark wood bands. Deliberate; no dark-mode toggle.
- Hero: particle swarm then kolam in v1; swarm cut in v2 so the kolam draws itself on a full-screen wood hero.

### Build
- One static HTML artifact, vanilla JS and SVG, no libraries. The build plan named GSAP 3.15.0 (ScrollTrigger, DrawSVG); the shipped page used none. The only reason recorded: claude.com's two showpieces are "plain CSS and SVG with no animation library, so I can rebuild them from scratch." Lenis, rough.js and perfect-freehand were scouted and not used.
- Source page plus spliced modules with Python (`page.html` holds `/*KOLAM*/`; `build.py` writes `index.html` and a doctype-wrapped `preview/index.html`; it prints an em-dash count). Separate sections were written as `new_sections.html`, `add.css`, `add.js` and spliced with `splice.py`.
- Local preview through a `.claude/launch.json` config ("tvs-site", python http.server, port 8931). Reason: the browser pane cannot act on `file://` pages.
- Copy button plus selectable email. Reason: mailto is unreliable in artifacts; the clipboard can be blocked, so the button falls back to "Select and copy".
- Phone gate keyed to the screen's short side under 540px (CSS media query plus JS screen check). Reasons: 760px blocked an upright iPad mini (744px); small Samsung tablets are about 600px; the largest phones are about 430px; the JS screen check catches a phone held sideways, which CSS width alone misses.
- Translator kept animated with tappable progress bars. Rejected: the Fable advisor's static six-row list.
- Kolam key kept (tied to the exact need names). Rejected: the Fable advisor's "cut it to a caption".
- Outside skills (impeccable, ui-ux-pro-max): listed for approval, never installed.

---

## 8. How Ash wants to work (process preferences, quoted briefly)

- Delegates research and names the model: "Maybe run a subagent, Sonnet 5.5"; "Have Fable 5.0.1 as your advisor model".
- Wants orchestration and review loops: "launch in some multiple agents and have orchestration there to see if the vision and the things are getting there".
- Wants a small prototype before a big build: "create me a very small prototype so that I can actually see if we're moving in the right direction".
- Wants understanding played back first: "first understand what exactly it is that we're trying to build, and then suggest".
- Plan first: "confirm what you understand, its specifications, and the design... Get me a proposal."; "Go ahead and plan it out and think through it".
- Side questions are welcome: "You may want to confirm a few things with me on the side as well."
- Treats skills as optional tools: "See if the skill I'm getting out of the better UI one is helpful. If not, you can ignore it completely."
- Distrusts unaided taste, wants real references studied: "I don't trust your abilities to create really good design."
- Gives style models as documents, not visuals: "Don't use it as a visual... see the way I write things".
- Compaction on demand, in chat: "give me a compaction prompt that I can put in so that I can keep you smart."; "don't put it in Markdown. Just give it to me in this chat."
- Wants alternatives recorded, not only what was done: "not just the things that we did, but also the things that we could have done instead".
- Runs `/verify` himself and wants it at the end: "Of course, it runs the verifier at the end".
- Proportional checking: "If you're reasonably sure, then you don't have to do a thorough double check."
- Works in parallel forks: "There are some bugs, but I've asked another fork of the chat to solve for that."
- Short go-aheads after long feedback: "Go make those changes".
- Feedback arrives as long dictated paragraphs, bug screenshots and reference photos; he names what he loves concretely (the claude.com rail and mind map, the Briefing card's blue-grey with a hand-drawn globe, the kolam photo, the film) and expects them studied in detail.
- For the skill: wants options when no inspiration is given ("it just gives me a few options"), one-shot quality, a quality-control agent "in the taste and manner", and a large pattern catalogue beyond this project.
- Standing rules restated in the session: no em dashes, no "not X but Y", no hedges, no invented numbers, 7th-grade words, no tables or green in reports for him, never git, plan first and ask before vault writes, they/them for unnamed people.
