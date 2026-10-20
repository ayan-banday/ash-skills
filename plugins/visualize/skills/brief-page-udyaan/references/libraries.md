# Libraries

A brief page is static, so most pages need **no library at all**: plain HTML, CSS grid, inline SVG and a few lines of vanilla JS for measured connectors. Fewer moving parts means fewer ways for the file to break when it is forwarded, opened offline or printed.

## What to use

| Need | Use | Version pinned |
|---|---|---|
| Snakes, switchboard cords, leader lines between HTML elements | vanilla JS + inline SVG (`getBoundingClientRect`) | none |
| Crates, routes, sieves, isotype rows, unit grids, tiles | inline SVG with `<symbol>` and `<use>` | none |
| Funnels, rails, rulers, trees, segmented bars | CSS grid, `clip-path`, borders | none |
| Force layouts, computed orbits, constellations with many leaves | D3 | 7.9.0, only if positions can't be set by hand |
| A route that draws itself once to show order | GSAP | 3.12.5, only if the motion explains |
| Scroll story with a building panel | `IntersectionObserver` | none |
| A real chart of data you were given | inline SVG by hand, or Chart.js 4.4.1 | optional |

Pick exact versions at least two weeks old. Never `latest`.

## How to get and ship them

`python scripts/fetch_libs.py <work>/libs` downloads D3, GSAP and ScrollTrigger from jsDelivr. `scripts/build.py` replaces these markers with the library source, so the page stays one portable file:

```html
<script>/*__D3__*/</script>
<script>/*__GSAP__*/</script>
<script>/*__ST__*/</script>
```

Leave a marker out and the library is not inlined. The starter ships with no markers; add one only when a pattern needs it.

Google Fonts stay as a `<link>` with real fallback stacks, so the page reads correctly offline with system fonts.

## Rules

- **Check the global before use:** `if (window.d3)`. If a library fails, the page still shows all content.
- **No D3 transitions.** They freeze mid-draw in headless captures and some embeds. Compute positions and draw once.
- **No `opacity: 0` starting states,** ever. Anything that animates starts visible or has a finished state under reduced motion and `?final=1`.
- **Draw measured connectors after fonts load** (`document.fonts.ready.then(draw)`) and again on a throttled `resize`, or the cords point at where the text used to be.
- **Do not add** icon fonts, UI frameworks, extra animation libraries, 3D, or anything that needs a build step.
- **Windows path limit.** Paths over 260 characters make Python and Chrome report "file not found" for files that exist. Build in a short path (for example `C:\Users\<name>\AppData\Local\Temp\htmlbuild`) and copy the result.
