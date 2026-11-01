# The tutor beside the page

Claude runs inside the published page on Ash's own account: no key, no setup. He approves it once, the first time he asks. **Publish with `capabilities: {sample: {}}`** or the tab never appears.

**One tab on the right edge, "Ask the tutor".** Clicking it slides a chat panel in from the right. The panel already holds the whole page's text and the section on his screen (the last heading above the middle of the window), plus any text he highlighted. A theory page's think boxes (one line that grows, Enter sends) open the same panel with his writing sent. There are no buttons scattered through the page. On wide screens the page slides left so the panel covers nothing.

**Haiku answers, by name.** The script asks for `claude-haiku-5-5` with `modelTier: "quick"`, so it falls back to the fast tier if Haiku is unavailable. Ash chose it: fast and smart enough. The page itself is written by the strongest model.

## The voice (lives in `RULES` in the script)

- **It answers only what he asked,** in under about 120 words, meaning first and the name after, with one tiny tech-company example if it helps.
- **No praise, no suggestions he didn't ask for.** For "how do I apply this to myself", it uses the tech company he's building toward.
- **A theory brain-dump gets a thorough reply:** what he got right, the one thing missing, and a sharper version in his own words.

## Paste this

**CSS,** inside the page's `<style>`:

```css
.tutor-tab{position:fixed;right:0;top:50%;transform:translateY(-50%);writing-mode:vertical-rl;z-index:30;font:600 14px Inter,system-ui,sans-serif;letter-spacing:.04em;color:var(--ink);background:var(--sand);border:0;border-radius:8px 0 0 8px;padding:16px 9px;cursor:pointer}
.tutor-tab:hover,.tutor-tab:focus-visible{background:var(--sand-f);outline:none}
.tutor-tab[hidden]{display:none}
.tutor{position:fixed;top:0;right:0;bottom:0;width:min(400px,100vw);z-index:40;background:var(--surface);border-left:1px solid var(--line);display:flex;flex-direction:column;transform:translateX(100%);transition:transform .2s ease;font:15px/1.55 Inter,system-ui,sans-serif}
.tutor.open{transform:none}
@media (prefers-reduced-motion: reduce){.tutor{transition:none}}
.tutor header{display:flex;justify-content:space-between;align-items:center;padding:12px 16px;border-bottom:1px solid var(--line);color:var(--head);font-weight:600}
.tutor .x{background:none;border:0;color:var(--muted);font-size:24px;line-height:1;cursor:pointer}
.tutor .ctx{padding:8px 16px;color:var(--muted);font-size:13px;border-bottom:1px solid var(--line)}
.tutor .log{flex:1;overflow-y:auto;padding:14px 16px;display:flex;flex-direction:column;gap:10px}
.tutor .me{align-self:flex-end;max-width:85%;background:var(--hl);color:var(--hl-text);padding:8px 12px;border-radius:10px 10px 2px 10px;white-space:pre-wrap}
.tutor .bot{max-width:95%;color:var(--text)}
.tutor .bot b{color:var(--bold)}
.tutor form{display:flex;gap:8px;padding:12px 16px;border-top:1px solid var(--line)}
.tutor textarea{flex:1;resize:none;background:var(--bg);color:var(--text);border:1px solid var(--line);border-radius:6px;padding:8px 10px;font:inherit}
.btn{font:600 14px Inter,system-ui,sans-serif;color:var(--ink);background:var(--sand);border:0;border-radius:6px;padding:8px 14px;cursor:pointer}
.btn:hover,.btn:focus-visible{background:var(--sand-f);outline:none}
.think{margin:10px 0 14px;display:flex;gap:8px;align-items:flex-end}
.think textarea{flex:1;min-width:0;min-height:38px;max-height:240px;resize:vertical;background:var(--paper);color:var(--ink);border:1px solid var(--sand);border-radius:8px;padding:8px 12px;font:14px/1.45 Inter,system-ui,sans-serif}
.think textarea::placeholder{color:#8a817a}
.think textarea:focus{outline:2px solid var(--sand);outline-offset:1px}
.think .btn{flex:none;padding:9px 14px}
.think .btn[hidden]{display:none}
@media (min-width:1200px){body.tutor-open .wrap,body.tutor-open .bar .in{margin-left:max(16px,calc((100vw - 420px - 780px)/2));margin-right:420px}}
```

**HTML and script,** just before the end of the page:

```html
<button class="tutor-tab" id="ttab" type="button" hidden>Ask the tutor</button>
<aside class="tutor" id="tutor" aria-label="Tutor">
  <header><span>Tutor</span><button class="x" id="tx" type="button" aria-label="Close">×</button></header>
  <div class="ctx" id="tctx"></div>
  <div class="log" id="tlog" aria-live="polite"></div>
  <form id="tf"><textarea id="tin" rows="2" placeholder="What's confusing you?"></textarea><button class="btn">Ask</button></form>
</aside>
<script>
(async () => {
  const RULES = `You are Ash's tutor, sitting beside a study page. Ash is 20, a BBA student at Jain University, going into tech: he wants to build a billion-dollar technology company. Answer only what he asks, in under 120 words. Use 7th-grade words and short sentences, meaning first and the name after. Give one tiny example if it helps, set in a tech company. No praise, no suggestions he did not ask for, no em dashes. Plain text in short paragraphs; bold only the key phrase with **double asterisks**. When he sends his thinking on a scenario, be thorough: say what he got right, the one thing missing, and a sharper version in his own words.`;
  const $ = id => document.getElementById(id);
  const thinkBtns = document.querySelectorAll(".think .btn");
  thinkBtns.forEach(b => b.hidden = true);
  const sample = await claude.use("sample");
  if (!sample) return;
  $("ttab").hidden = false; thinkBtns.forEach(b => b.hidden = false);
  // The think box: one line that grows as he writes; Enter sends, Shift+Enter adds a line.
  document.querySelectorAll(".think textarea").forEach(t => {
    t.placeholder += " Enter sends.";
    t.oninput = () => { t.style.height = "auto"; t.style.height = Math.min(t.scrollHeight + 2, 240) + "px"; };
    t.onkeydown = e => { if (e.key === "Enter" && !e.shiftKey) { e.preventDefault(); t.nextElementSibling.click(); } };
  });
  const wrap = document.querySelector(".wrap");
  const page = wrap.innerText.slice(0, 24000);
  let turns = [], topic = "", section = "", ctl;

  // The section on screen: the last heading above the middle of the window.
  function here() {
    const hs = [...wrap.querySelectorAll("h1, h2, h3")];
    let h = hs[0];
    for (const x of hs) if (x.getBoundingClientRect().top < innerHeight * 0.5) h = x;
    const box = h.closest(".q");
    if (box) return [h.textContent.trim(), box.innerText];
    let text = h.innerText, n = h.nextElementSibling;
    while (n && !/^H[1-3]$/.test(n.tagName) && !n.querySelector("h2, h3")) { text += "\n" + n.innerText; n = n.nextElementSibling; }
    return [h.textContent.trim(), text];
  }
  function open(title, text) {
    if (title !== topic) { turns = []; $("tlog").textContent = ""; }
    topic = title; section = text.slice(0, 6000);
    $("tctx").textContent = "About: " + title;
    $("tutor").classList.add("open"); document.body.classList.add("tutor-open");
    $("tin").focus();
  }
  function close() { ctl?.abort(); $("tutor").classList.remove("open"); document.body.classList.remove("tutor-open"); $("ttab").focus(); }
  const show = (el, t) => { el.innerHTML = t.replace(/[&<>]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;" }[c])).replace(/\*\*(.+?)\*\*/g, "<b>$1</b>").replace(/\n/g, "<br>"); };

  async function send(msg) {
    const picked = getSelection().toString().trim().slice(0, 1500);
    const me = document.createElement("div"); me.className = "me"; me.textContent = msg;
    const bot = document.createElement("div"); bot.className = "bot"; bot.textContent = "Thinking...";
    $("tlog").append(me, bot); bot.scrollIntoView({ block: "end" });
    turns.push({ role: "user", content: msg });
    turns = turns.slice(-10);
    ctl?.abort(); ctl = new AbortController();
    const lead = `${RULES}\n\nThe whole page:\n${page}\n\nThe section he is on:\n${section}` + (picked ? `\n\nHe highlighted:\n${picked}` : "");
    const first = turns[0].role === "user" ? [] : [{ role: "user", content: "(earlier)" }];
    try {
      const { text } = await sample([{ role: "user", content: lead }, { role: "assistant", content: "Ready." }, ...first, ...turns], {
        model: "claude-haiku-5-5", modelTier: "quick", cache: false, signal: ctl.signal,
        onText: ({ text }) => show(bot, text)
      });
      show(bot, text);
      turns.push({ role: "assistant", content: text });
    } catch (e) {
      bot.textContent = e.code === "cancelled" ? "" : e.text || ({ not_granted: "The tutor needs your OK to use Claude.", rate_limited: "Too many questions at once. Try again in a minute." }[e.code] || "Something went wrong. Ask again.");
      turns.pop();
    }
  }

  $("ttab").onclick = () => { const [t, s] = here(); open(t, s); };
  $("tx").onclick = close;
  addEventListener("keydown", e => { if (e.key === "Escape" && $("tutor").classList.contains("open")) close(); });
  $("tf").onsubmit = e => { e.preventDefault(); const v = $("tin").value.trim(); if (v) { $("tin").value = ""; send(v); } };
  $("tin").onkeydown = e => { if (e.key === "Enter" && !e.shiftKey) { e.preventDefault(); $("tf").requestSubmit(); } };
  thinkBtns.forEach(b => b.onclick = () => {
    const box = b.closest(".think"), v = box.querySelector("textarea").value.trim();
    if (!v) return;
    const q = b.closest(".q") || b.closest(".pair");
    open((q.querySelector("h3") || q.querySelector(".lbl")).textContent.trim(), q.innerText);
    send("My thinking on the scenario:\n" + v);
  });
})();
</script>
```

The `(earlier)` line keeps the roles alternating when old turns are trimmed. A page published without `sample` hides the tab and the send buttons, and the hidden answers still work.
