# Toy explainer · "the little robot on the desk"

**Picture it:** a small, quirky robot (one big camera eye in a white shell, orange trim, thin neck, chunky feet)
standing on a wooden desk under a desk lamp, against a warm plaster wall. Frosted paper cards float above it with one
number each, and a handwritten caption sits on a strip of tape below.
**Swatch:** `#3C3F4C #F4EEE3 #D0C7BA #B38A68 #CA7A5B #D98BA6`

**Source:** the Microduck explainer Ash sent on 2026-10-30 (Hugging Face and Pollen Robotics' $399 walking robot),
studied frame by frame. Key frames: `assets/reference-frames/microduck/` (`00_contact_sheet.jpg` shows the whole film).
Ash: "I actually quite liked the typography, the translucent background, the robot moving", and "the weird yet quirky
design of that robot".

**Suits:** products and tech explained to non-experts, student and youth audiences, startup pitches to investors who
won't read, onboarding, anything where a friendly character can stand in for the product or the reader. Tone:
curious, warm, a little funny. Audience: anyone on a phone.
**Avoid when:** a formal institutional proposal where a mascot would read as unserious (pair it with drafting there
instead), or grief, health and money-loss topics.
**Cultural note:** a toy character with no culture of its own. Give it a local prop when the client has one (a
tiffin, a cricket bat, a seed packet) rather than a costume.

## What makes it work

- **One character, always on screen, and the world changes around it.** The wood desk turns into a pink simulator
  floor with 4,096 copies of the duck, then back to the desk. The character is the constant; the scene carries the
  information.
- **The character is quirky, not cute-generic.** Odd proportions (a head as big as the body, a single huge eye,
  spindly neck, oversized feet), visible mechanical parts (servo bolts, a cable), and expressions made only with the
  eye: it widens, squints, and a sweat drop appears when it struggles. It falls over, gets up, tilts its head.
- **Frosted, translucent cards hold the facts.** A paper card with a soft blur behind it floats above the character:
  "0 lines / of walking code", "4,096 / grid 64 x 64", "50 Hz / 50 decisions a second", "$399". One big number, one
  tiny label. Some cards are small app windows ("walk.py") or a chart with one rising line.
- **Handwritten type on tape.** Captions sit on a cream strip of paper tape, in a rounded hand-lettered face, 3 to 5
  words per strip, so a sentence runs across several frames. Numbers on the cards use the same hand.
- **Light does the pointing.** A desk lamp casts a warm pool under the character; a spotlight ring opens the film.
- **Paper grain everywhere.** Wall, floor and cards all carry a fine paper texture, so it reads as drawn, not
  rendered.

## Story device

The character is the reader (or the product) and each section puts it in a new situation. A number card above
answers the section's question; the character's reaction shows how it feels (struggling, then fine). The close
returns to the first scene with the character changed: it walks, holds the price tag, or holds the ask.
**Badge:** the eye alone, in the section's colour.

## Recipe

- **Character:** build it from simple SVG shapes: a rounded box head (white shell `#F4EEE3`, 2px graphite outline,
  an orange band along the bottom), one eye (a dark ring, an orange iris `#CA7A5B` and a white highlight), a two-
  segment neck, a short body, two legs with chunky orange feet. Keep every part a separate group so it can move.
  Expressions: scale the iris (surprise), squash the eyelid path (squint), add a teardrop sweat drop (effort).
- **Scene layers:** wall (`#D0C7BA` with grain), a wooden floor band (`#B38A68` with darker plank lines `#8E6A50`), a
  lamp glow (radial gradient `#F3D9A4` at 50% fading to clear). The "other world" swaps the floor for a pink checker
  (`#D98BA6` and `#C97894`).
- **Frosted card:** `background: color-mix(in srgb, var(--card) 78%, transparent); backdrop-filter: blur(8px)
  saturate(1.1); border: 1.5px solid var(--ink); border-radius: 10px; box-shadow: 0 6px 18px -8px rgb(0 0 0 / .25)`.
  Always set a solid fallback for browsers without `backdrop-filter`.
- **Caption tape:** a cream strip `#EFE3C8` with slightly ragged ends (`clip-path` polygon), rotated by 0.5 to 1
  degree, text in the hand face.
- **Texture:** an SVG `feTurbulence` grain at 4 to 6% over the whole page; never a photo texture.
- **Scope the stage CSS to the stage SVG** (`.frame > svg`, never `.frame svg`): cards and icons live outside it. In
  the first test, a broad `svg{position:absolute;inset:0}` blew a card's checkbox icon up over its text.
- **Label any progress strip once** with its first and last value ("Day 0" at the left, "Day 14" at the flag).
- **`palette_check.py` expects token names** like `paper`, `ground`, `marker`: map this palette onto them before
  running it.

## Palette

```
--ground   #3C3F4C   graphite (outlines, dark base, night scenes)
--paper    #D0C7BA   plaster wall
--card     #F4EEE3   frosted card and robot shell
--ink      #2B2D35   text
--muted    #6A6C74   small labels
--wood     #B38A68   desk
--wood-2   #8E6A50   plank lines
--accent-1 #CA7A5B   toy orange (the eye, the trim, the one bright thing)
--accent-2 #D98BA6   simulator pink (the "other world")
--glow     #F3D9A4   lamp light
--tape     #EFE3C8   caption tape
```
Check text contrast with the checker in `00-intake.md` Part 3.3 before building: ink on card and ink on tape must pass 4.5:1;
orange is for shapes and big numbers, never small text.

**Type:** hand **Patrick Hand** (captions, card numbers), body **Nunito** (rounded, friendly), labels **Nunito**
600 in small caps. Both on Google Fonts.

**Motion:** small toy moves that each tell something: a bob while idle, a blink, a head tilt when a question comes
up, one hop when something works, a fall and a get-up when something fails. A crowd of copies fans out when a number
gets big. Every move plays once and holds; nothing loops forever, nothing follows the pointer.

## How it maps to a phone page

- **Fill the screen:** the character takes at least 45% of the screen height, the card overlaps its head or the
  wall edge so the frosting has something to blur, and the caption tape sits directly under the headline. No dead
  band of empty wall.
- **Every prop changes what the reader knows** (a trophy on demo day, a form on Day 0). A prop that only acts out
  the verb is cut.
- **A direction Ash picks overrides a brand kit's fonts and colours;** keep the client's logo.
- **Website:** the character stands in the lower half of the screen (the stage from `phone.md`), the frosted card
  sits above it, and the copy at the top. Each section changes the scene or the character's state.
- **Swipe deck:** one situation per slide; the character moves between slides (walks in from the right).
- **The caption tape replaces the body line on short screens:** one plain sentence, written to `copy-rules.md`.
