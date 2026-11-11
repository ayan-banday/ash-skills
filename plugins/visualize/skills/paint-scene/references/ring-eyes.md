# Ring Eyes: the flat look

One flat Wada colour, wobbly hand lettering with one huge punchline word, and simple black characters with white ring eyes, cropped by the frame edge. Taken from a reel Ash liked and made his: Wada grounds, ink `#111314`, the coral ball `#F58E84`, and lines from his own systems. Ash approved the first cast on Nov 11 2026 ("I quite like this"; Fuji `ranges/self/personal-brand/research/ring-eyes-cast.html`).

Open on every Ring Eyes run. The gallery (`ring-gallery.html`) shows every character, expression, pose and format; `python scripts/kit.py list` prints the names.

## Contents
- Why it works
- What breaks it
- Rules
- Ring Eyes or Watercolour
- The cast
- Expressions and poses
- Formats and settings
- Touch, Scene, Commission

## Why it works

- **Silhouette first.** A solid shape reads before any detail. Cover the eyes and the racket is still a racket.
- **Two rings carry the feeling.** With almost no face, the reader fills in the mood, so a small change in the rings reads as a big change.
- **The big word is the message.** One huge Amatic SC word is the headline. The character reacts to it and never repeats it.
- **The crop implies a world.** A character cut by the frame edge lives beyond the frame, and it leaves the word room.
- **Flat colour survives a thumbnail.** One ground, ink and coral still read in a 48px feed preview.
- **Coral means "what you get or decide",** the marker's meaning, so the eye knows where to land.
- **The wobble feels human.** Gaegu and a slight tilt say a person made this, and keep the piece calm.

## What breaks it

- **Features creeping back:** noses, teeth, limbs on every character. The ring-eye signature disappears into generic cartoon.
- **Gradients, shadows, highlights, outlines on the body.**
- **Two big words,** or a big word over 10 letters: no entry point, and it can't be huge.
- **A crowd.** Past three characters on a post the piece becomes a scene to decode.
- **Character and word fighting:** both big, both busy. One leads.
- **Eyes too small:** under about 15% of the character's width they turn to dots at thumbnail size.
- **Colour creep:** a second ground, a third accent, a coral tint. The coral stops meaning anything.
- **Text on a character** or across its eyes.

## Rules

1. **One idea per piece, one lead character.** Others are small and support it.
2. **At most three characters** on a post, story, dark post or dialogue. Banners, stickers and avatars are lineups and may hold more.
3. **One big word, at most 10 letters,** in Amatic SC 700 capitals. Every other line is Gaegu. `Ring.piece` warns on a second big word or a long one.
4. **Colours: one Wada ground, ink, white, coral, and at most one more.** The ground comes from one numbered combination (`palette.py`, the book colours `b1` to `b4`, or any single colour of the book), named in a CSS comment.
5. **Coral appears once per piece:** the ball, the compass needle, a tiny accent. On the thing the reader gets or decides.
6. **Crop the lead character 20 to 45% with the frame edge on posts and stories, never through its eyes.**
7. **Text sits on the ground only.** Never on a character, never across the eyes or the ball.
8. **Character and big word touch at most at a corner.**
9. **Faces stay minimal:** ring eyes, and the dot mouth only on characters that have one (fuji, ball). Expressions change the eyes.
10. **Limbs are opt-in:** a pose only when the action is the message ("cheer" for a win, "point" at the word, "walk" for a journey). Default `still`.
11. **The covered tests apply** (match-ash-design): cover the picture and the words still make sense; cover the words and the character still shows who and the mood.
12. **No gradients anywhere.** Light, when a piece needs it (the dark post), is one flat translucent wedge.

## Ring Eyes or Watercolour

The look question goes with the level question (`references/character.md`, "The level per case"). No answer: pick by this table.

| | Ring Eyes | Watercolour |
|---|---|---|
| Reader | Fast scrollers, friends, a feed, a team chat | Someone who stays and looks |
| Format | Posts, stories, stickers, comics, covers, icons, empty states, slides that explain a method | One large scene, a hero, a page's atmosphere, print |
| Tone | Wry, light, one beat, a reaction | Warm, reflective, a mood, a slow reveal |
| Cost | Minutes: templates plus settings | Minutes for a Scene, hours for a painted piece |

- **Ring Eyes when the idea is one beat** and the reader gives it three seconds.
- **Watercolour when the idea needs a world** or a mood.
- **Ash's own pages:** never asked. Watercolour Touch by default; a Ring Eyes mark (one small character) fits an empty state or a section the page wants to make friendly.
- **Print:** Watercolour grain and hatching only. Ring Eyes prints fine as flat colour when Ash asks for it.

## The cast

Each is in a 200x200 box, black by default (`body:` any colour; light bodies get ink eyes). SVG files: `assets/ring/<name>.svg`.

- **Fuji's own:**
  - `fuji` (a map or system; the dot mouth)
  - `range` (all the maps; Olympus)
  - `tent` (base camp)
  - `map` (one outcome)
  - `compass` (direction; coral needle)
  - `flag` (a finish line, a timebox)
  - `fog` (ideas with no map)
- **Work and the loop:**
  - `ball` (a tennis task, what the reader gets; coral)
  - `racket` (back-and-forth work)
  - `loop` (an open loop set the night before)
  - `calendar` (a day set the night before)
  - `clock` (a timebox, a golf task)
  - `ticket` (one piece of work)
  - `folder` (the three-maps rule)
  - `scroll` (the log)
  - `sandwich` (the study method)
  - `laptop` (a build session with Claude)
- **Writing and capture:**
  - `note` (a raw reflection)
  - `pencil` (writing)
  - `phone` (capture on the phone)
  - `bubble` (a WhatsApp message)
  - `book` (Shasta)
- **Body and world:**
  - `lamp` (focus, the night run)
  - `moon` (Callisto, 12:47 am)
  - `kettle` (the plateau: food, a break)
  - `seedling` (Udyaan, growth, a first step)

**Weakest at 48px** (the drawing agents' own notes): `map`, `clock`, `range`, `kettle`, `moon`. Use them at 120px or more, or pick another.

## Expressions and poses

- **`expr`:**
  - `open`: calm, the default.
  - `closed`: content, resting.
  - `happy`: a win.
  - `side`: curious, or looking at the word; `look:-1` looks left.
  - `surprised`: a reveal.
  - `worried`: unsure, a risk.
  - `sleepy`: "go to bed", dormant.
  - `wink`: an aside.
- **`pose`:**
  - `still`: the default.
  - `stand` and `walk`: a journey.
  - `wave`: hello, bye.
  - `cheer`: a win.
  - `point`: at the word.
  - `hold`: offering the ball.
  - `shrug`.
  - `sit`.
  - `hop`.
  - Characters without shoulder or hip points stay limbless.
- **Also:** `tilt` (degrees), `flip`, `body`, `eye`, `limb`.

## Formats and settings

Load the fonts (Gaegu 400 and 700, Amatic SC 700) and `<script src="ring.js"></script>`, then one call per piece. `ring-gallery.src.html` has a working settings block for every format: copy the nearest one.

```js
Ring.piece("#el", {format:"post", bg:"#f9c1ce", id:"night-before",
  words:["Set","tomorrow","the night",{big:"BEFORE."}],
  cast:[{who:"calendar", at:"right:-10%;bottom:-3%", w:58, tilt:-8, expr:"happy"}]});
```

| Format | Shape | Settings beyond `bg` and `cast` |
|---|---|---|
| `post` | 4:5 | `words` (strings are lines, `{big:"WORD."}` the punchline, `{mid:"…"}` a bold line) |
| `story` | 9:16 | `words`, `bigSize` |
| `stat` | 4:5 | `number`, `words`; the cast sits in a row on the bottom edge |
| `dark` | 4:5 on ink | `words`, `light` (the character's colour and the wedge), `wedge` (an SVG path in 100x125) |
| `slide` | 16:9 | `words`, `note`, `points:[["Tennis","Claude finds my gaps"],…]` (up to 3) |
| `banner` | 3:1 | `words`, `paradeAt` (where the lineup starts, %) |
| `comic` | 16:5, three panels | `panels:[{bg, say:[…], cast:[…]}, …]` |
| `dialogue` | 4:5 | `say:["first bubble","reply"]`, two cast members |
| `stickers` | 1:1 | `title`, `cols`; each member may have `label` |
| `empty` | 4:5 (or `ratio`) | `line`, `big`, `button` |
| `avatars` | a row of 1:1 | each member has its own `bg`; `square:true` for app icons |

- **A cast member:** `{who, at:"right:-8%;bottom:-12%", w:55, expr, pose, tilt, flip, look, body, eye, sticker}`. `at` is CSS position inside the piece; `w` is percent of the piece's width. Each format has a sensible default `at` and `w`, so `{who:"fog"}` alone works.
- **Words** size by the piece's width (container units), so a piece looks the same at any size.
- **Export:** `python scripts/kit.py png page.html --dir pngs` writes every piece as a 2x PNG named by its `id`, and prints any warning.

## Touch, Scene, Commission

- **Touch:** one small character on a page. `<i data-ring="loop" data-expr="sleepy"></i>` plus `ring.js`; `Ring.mount()` runs on load. Or paste `assets/ring/<name>.svg` inline. One per screen, beside a heading or in an empty state, never inside body text.
- **Scene:** a format plus settings, as above. Two minutes.
- **Commission** (Ash says so): a new character, pose or format built with full effort, then saved into the kit.
  - **A new character:** add `Ring.add("name",{meaning, body(c), face:{eyes:[[x,y],[x,y]], r, sw, mouth}, arms:{l,r}, feet:{l,r}})` under the `@@CAST@@` line in `assets/ring.js`. Body only, a solid fill in `c.body`, at most one detail (`c.detail` or coral); eye ring radius 13 to 19, at least 15% of the body's width. Check it at 200px and 48px in the gallery, then run `python scripts/kit.py svgs` and add it to "The cast" above.
  - **A new pose:** add a limb shape to `ARM` or a leg case in `legs()`, and its name to `POSE` and `Ring.POSES`.
  - **A new format:** add a function to `Ring.FORMATS` that returns `{ratio, html}`, using `lines()`, `member()` and `at()`, and a settings block in `scripts/ring-gallery.src.html`.
  - **Then** rebuild the gallery (`python scripts/kit.py bundle scripts/ring-gallery.src.html ring-gallery.html`), screenshot it once, and commit.
