---
name: post-page-online
description: "[GitHub Pages · sites repo] How do I put a page I made online so friends outside Claude can open it? Wraps a finished HTML page, tests it in a browser, pushes it to ayan-banday/sites and hands back its public github.io link. Use when Ash says 'post this online', 'publish this page' or 'host this'. Use instead of a claude.ai artifact when people outside Ash's organization must see it."
---

Put one finished page on **https://ayan-banday.github.io/sites/<slug>/**, served by GitHub Pages from the public repo `ayan-banday/sites`. Free, no database, no server: the visitor gets the same single file Claude built.

## Steps

1. **Find the page and name it.** The page is the built file: a pitch-site or brief-page build is `work/index.html`; an artifact is the file it was published from. If its title or content does not match what Ash described, say so and ask before going on. The slug is the page's `<title>` in lowercase words joined by hyphens (`The Range` is `the-range`).
   Done when you have the source path and the slug. If the slug is already a folder in the repo (step 3), Ash has said whether to replace it or pick a new slug.

2. **Check it is safe to make public.** The repo and the page are public: anyone with the link sees the page and its source. Read the page for private things: personal quotes, client names, prices, emails, keys. Look for runtime calls that only work inside Claude: `window.claude`, artifact capabilities, a shared database.
   Search rather than reading every line: `grep -n -i -E "window\.claude|@[a-z0-9-]+\.[a-z]|api[_-]?key|token|password|₹|\$[0-9]" <source.html>`. Outside requests to Google Fonts or a script CDN are fine.
   Done when Ash has said yes to anything private going public, and the page has no Claude-only calls (or you told Ash which part will not work and he said go).

3. **Get the repo.** Use an existing clone first: `D:\sites` on Ash's laptop, `/home/user/sites` in a cloud session. Only when there is none: on the laptop `git clone https://github.com/ayan-banday/sites D:\sites`; in the cloud attach it with `add_repo` (owner `ayan-banday`, repo `sites`, access `push`) and clone it to `/home/user/sites`. Then `git pull` on `main`, and `ls <repo>` to see which slugs exist.
   Done when `git -C <repo> log -1` shows the latest commit on `main`.

4. **Wrap it into the repo.** The scripts live in this skill's `scripts/` folder.
   ```bash
   python <skill>/scripts/wrap_page.py <source.html> <repo>/<slug>/index.html
   ```
   Artifact pages have no doctype or head; the script adds the skeleton the artifact viewer normally adds. A page that is already a full HTML document is copied unchanged. Copy any files the page loads by relative path (images, data) into `<repo>/<slug>/` too.
   If `git -C <repo> status` shows no change, the same page is already live: stop and give Ash the existing link.
   Done when `<repo>/<slug>/index.html` starts with `<!doctype html>`.

5. **Test it like a visitor.**
   ```bash
   python <skill>/scripts/check_page.py <repo>/<slug>/index.html --out <scratch>/shots
   ```
   `<scratch>` is Claude's scratchpad, or any temp folder outside the repo. It needs Playwright with Chromium (installed in cloud sessions; on a laptop `pip install playwright` then `python -m playwright install chromium`). A "wider than the screen" note is expected on a horizontal page and does not fail the check. Then look at both screenshots. For a page with stops, buttons or a dive, click through it once in Playwright as well.
   Done when the script prints PASS and the screenshots look like the page Ash saw.

6. **List it and push.** Add the page to the repo's root `index.html` and `README.md`. While the repo holds one page, the root forwards to it with a `<meta http-equiv="refresh">` line; from the second page on, delete that line and make the root a plain list of links, one per page, newest first. Commit only the files you touched, by name, on `main`, with the message `Post <slug>`, then `git push`.
   Done when the push succeeds.

7. **Confirm it is live.** GitHub builds the site in a minute or two. Check the build, then the page:
   - Build: `GET https://api.github.com/repos/ayan-banday/sites/actions/runs?per_page=3` shows `pages build and deployment` with conclusion `success` and a `head_sha` equal to `git -C <repo> rev-parse HEAD`.
   - Page: on the laptop, open the link. In a cloud session `github.io` is blocked, so take a Firecrawl screenshot of the link with `maxAge: 0` and look at it.
   Done when the page returns 200 and the screenshot matches step 5.

8. **Tell Ash** the link, `https://ayan-banday.github.io/sites/<slug>/`, and show the live screenshot.

## Reference

- **Already set up:** the repo `ayan-banday/sites` is public, with GitHub Pages on `main`, folder `/ (root)`, and a `.nojekyll` file so files are served as they are. First page: `the-range/` (2026-10-20).
- **Updating a page:** wrap and push to the same slug; the link stays the same.
- **Taking a page down:** delete its folder and its line in the root `index.html` and `README.md`, then push. Copies others saved stay with them.
- **A 404 right after posting** means the build is still running, or the address is missing `/sites/<slug>/`. A hard refresh (Ctrl+Shift+R) clears a cached 404.
- **Cloud session limits:** the session token cannot create repositories or change Pages settings (both refused by the proxy). A new repo or a Pages switch is Ash's click on github.com.
- **Private viewing** (a page only some people can open) needs a paid GitHub plan or another host. Say so and stop; the sites repo is public.
- **Vercel instead:** needs `api.vercel.com` allowed in the environment's network settings and a token in the `VERCEL_TOKEN` variable. Until both exist, use this repo.
