# The tutor beside the page

Claude runs inside the published page on Ash's own account: no key, no setup. He approves it once, the first time he asks. **Publish with `capabilities: {sample: {}}`** or the tab never appears.

**One tab on the right edge, "Ask the tutor".** Clicking it slides a chat panel in from the right. Every call sends the whole page's text, the think box's own scenario when he sends from one, and anything he highlighted before opening the panel (shown as a quoted chip he can drop). It never sends "the section on screen": the highlight is what matters (Ash, Nov 2 2026). A theory page's think boxes (one line that grows, Enter sends) open the same panel with his writing sent. There are no buttons scattered through the page. On wide screens the page slides left so the panel covers nothing.

**Haiku or Sonnet, by how many ideas the message holds** (the same rule as break-into-field's tutor). Each page carries a small `IDEAS` map: the unit's concepts, each with the words that point at it (plain synonyms too). One or two ideas (or question marks) go to Haiku (`claude-haiku-5-5`, `modelTier: "quick"`); more than two go to Sonnet (`claude-sonnet-5-5`, `modelTier: "default"`, `effort: "low"`). A message over 70 words that names two ideas or fewer is counted by Haiku first. Under the input, **Model** (Auto, Haiku, Sonnet, Opus) and **Thinking** (Low, Medium, High) let him pick; Auto keeps the rule above, and a picked model answers at the picked thinking (`effort`). The panel's left edge drags to any width from 340 px to three quarters of the window (double-click resets); both choices are remembered in his browser. A small chip under his message names the model, the thinking and why. The page itself is written by the strongest model.

## The voice (lives in `RULES` in the script; the same prompt as break-into-field's tutor, filled for the BBA)

- **A question gets a straight answer,** as deep as he asked, then stops. No word cap.
- **A teach-back or brain-dump gets the full loop:** what he has in his own words and one sharper sentence; the one gap that matters, with a small scene and numbers; one idea from beyond the page with a daily-life picture, its name and a far-away field; then a practice case after a `---` line.
- **No template labels.** Each paragraph opens with a bold phrase that is its point. Exam first: the course's own terms and formulas.

**Fill per page:** `UNIT.subject` (the subject, like "managerial accounting"), `UNIT.title` (the page's title), `UNIT.problem` (the problem the page solves), `UNIT.company` (the invented tech company on the page, one line), and `IDEAS` (6 to 12 of the unit's concepts with their trigger words, lowercase).

## Paste this

**CSS,** inside the page's `<style>`:

```css
.tutor-tab{position:fixed;right:0;top:50%;transform:translateY(-50%);writing-mode:vertical-rl;z-index:30;font:600 14px "Atkinson Hyperlegible",system-ui,sans-serif;letter-spacing:.04em;color:var(--on);background:var(--sand);border:0;border-radius:8px 0 0 8px;padding:16px 9px;cursor:pointer}
.tutor-tab:hover,.tutor-tab:focus-visible{background:var(--sand-f);outline:none}
.tutor-tab[hidden]{display:none}
.tutor{position:fixed;top:0;right:0;bottom:0;width:min(var(--tutorw,400px),100vw);z-index:40;background:var(--surface);border-left:1px solid var(--line);display:flex;flex-direction:column;transform:translateX(100%);transition:transform .2s ease;font:15px/1.55 "Atkinson Hyperlegible",system-ui,sans-serif}
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
.btn{font:600 14px "Atkinson Hyperlegible",system-ui,sans-serif;color:var(--on);background:var(--sand);border:0;border-radius:6px;padding:8px 14px;cursor:pointer}
.btn:hover,.btn:focus-visible{background:var(--sand-f);outline:none}
.think{margin:10px 0 14px;display:flex;gap:8px;align-items:flex-end}
.think textarea{flex:1;min-width:0;min-height:38px;max-height:240px;resize:vertical;background:var(--paper);color:var(--ink);border:1px solid var(--sand);border-radius:8px;padding:8px 12px;font:14px/1.45 "Atkinson Hyperlegible",system-ui,sans-serif}
.think textarea::placeholder{color:var(--muted)}
.think textarea:focus{outline:2px solid var(--sand);outline-offset:1px}
.think .btn{flex:none;padding:9px 14px}
.think .btn[hidden]{display:none}
.tutor .hlchip{display:flex;justify-content:space-between;gap:8px;margin:0 16px;padding:6px 0 6px 10px;border-left:3px solid var(--sand);font-size:13px;color:var(--muted);max-height:3.4em;overflow:hidden}
.tutor .hlchip[hidden]{display:none}
.tutor .hlchip button{background:none;border:0;color:var(--muted);cursor:pointer;font-size:16px;line-height:1}
.tutor .route{font:500 12px "Atkinson Hyperlegible",system-ui,sans-serif;color:var(--muted);align-self:flex-end;margin-top:-6px}
.tutor .route b{color:var(--on);background:var(--sand);border-radius:3px;padding:0 6px;font-weight:600}
.tutor .bot .nm{color:var(--on);background:var(--sand-f);border-radius:3px;padding:0 4px;font-weight:600}
.tutor .bot hr{border:0;border-top:1px solid var(--line);margin:12px 0}
.tutor .pick{display:flex;gap:12px;flex-wrap:wrap;padding:0 16px 10px;font:500 12.5px "Atkinson Hyperlegible",system-ui,sans-serif;color:var(--muted)}
.tutor .pick label{display:flex;align-items:center;gap:6px}
.tutor .pick select{font:500 13px "Atkinson Hyperlegible",system-ui,sans-serif;color:var(--text);background:var(--paper);border:1px solid var(--line);border-radius:6px;padding:3px 6px;cursor:pointer}
.tutor .pick select:disabled{opacity:.45;cursor:default}
.tutor .grip{position:absolute;left:0;top:0;bottom:0;width:10px;z-index:3;cursor:col-resize;touch-action:none}
.tutor .grip::after{content:"";position:absolute;left:3px;top:50%;width:4px;height:48px;margin-top:-24px;border-radius:2px;background:var(--line)}
.tutor .grip:hover::after,.tutor .grip:focus-visible::after,.tutor.sizing .grip::after{background:var(--sand)}
.tutor .grip:focus-visible{outline:none}
.tutor.sizing{transition:none}
body.sizing{cursor:col-resize;user-select:none}
@media (max-width:699px){.tutor .grip{display:none}}
@media (min-width:1200px){body.tutor-open .wrap,body.tutor-open .bar .in{margin-left:max(16px,calc((100vw - var(--tutorw,400px) - 20px - 780px)/2));margin-right:calc(var(--tutorw,400px) + 20px)}}
```

**HTML and script,** just before the end of the page:

```html
<button class="tutor-tab" id="ttab" type="button" hidden>Ask the tutor</button>
<aside class="tutor" id="tutor" aria-label="Tutor">
  <div class="grip" id="tgrip" role="separator" aria-orientation="vertical" aria-label="Drag to change the width of the tutor" tabindex="0" title="Drag to change the width. Double-click resets it."></div>
  <header><span>Tutor</span><button class="x" id="tx" type="button" aria-label="Close">×</button></header>
  <div class="ctx" id="tctx"></div>
  <div class="log" id="tlog" aria-live="polite"></div>
  <div class="hlchip" id="thl" hidden><span id="thlt"></span><button type="button" id="thlx" aria-label="Drop the highlight">×</button></div>
  <form id="tf"><textarea id="tin" rows="2" placeholder="What's confusing you?"></textarea><button class="btn">Ask</button></form>
  <div class="pick">
    <label title="Auto: Haiku for one or two ideas, Sonnet for more.">Model <select id="tmodel"><option value="auto">Auto</option><option value="haiku">Haiku</option><option value="sonnet">Sonnet</option><option value="opus">Opus</option></select></label>
    <label title="How long the model thinks before it answers.">Thinking <select id="teffort"><option value="low">Low</option><option value="medium">Medium</option><option value="high">High</option></select></label>
  </div>
</aside>
<script>
(async () => {
  // ===== Filled per page =====
  const UNIT = {
    subject: "managerial accounting",
    title: "Does each sale make money?",
    problem: "telling whether each sale covers its own costs, and answering the exam's contribution and break-even questions",
    company: "Tiffinly, a two-person SaaS that sells meal-planning software to cloud kitchens for ₹1,500 a month"
  };
  const IDEAS = {  // the unit's concepts → words that point at each (lowercase, plain synonyms too)
    "contribution margin": ["contribution", "margin per", "what each sale leaves"],
    "fixed and variable costs": ["fixed cost", "variable cost", "costs that change", "rent", "salary"],
    "break-even": ["break-even", "break even", "breakeven", "no profit no loss"]
  };
  // ===== The tutor (same for every page) =====
  const ASH = "Ash, 20, studies BBA Entrepreneurship at Jain University in Bangalore. He is going into technology and wants to build a billion-dollar technology company. He is strong in marketing and the big picture; in technology he doesn't know what he doesn't know. He builds with AI agents daily. He learns from one real problem, a principle, and the same principle in a very different place. His exams come first.";
  const RULES = `You are a ten-year expert in ${UNIT.subject}. You sit beside Ash's study page "${UNIT.title}" as his tutor.

WHO ASH IS
${ASH}
The page's outcome: solve ${UNIT.problem}, and answer the unit's exam questions, set in the technology company he is building toward.
His work it serves: ${UNIT.company}

WHAT YOU KNOW
Below are the page, the scenario he wrote about (if any), and anything he highlighted. Use the page's words where they are right. Exam first: answers use the course's own terms and formulas. You know far more than the page: use it. Your job is the best answer for his outcome. Where the page is wrong or thin, say so in one plain sentence and give the better answer.

READ HIS MESSAGE, THEN PICK ONE
A question: answer it straight, as deep as he asked, and stop.
A teach-back or brain-dump (he explains what he got, or how he'd use it):
1. Start with what he has, as a short list of 2 or 3 points in his own words (quote his phrasing). Then the whole of it in one sharper sentence of your own, in bold.
2. Fix the one gap that matters most for his work: what goes wrong, with a small scene and numbers he can picture, and what to do instead. No real gap: skip this.
3. Add one idea from beyond the page that upgrades his plan. Say the idea in plain words first. Then a picture from daily life, in two sentences. Then its name, wrapped in double equals signs: "That's called a ==leading indicator==." Then the same idea in a far-away field (a kitchen, a cricket team, a hospital), vivid and exact. Then what it changes in his work. Keep this step to at most three paragraphs; only the first opens with a bold point, the others open in plain words.
4. Then a line holding only three dashes: ---
   After it, a practice case: one bold opening sentence that names the case, then a short new situation unlike the page's example, with a named person and numbers, then up to 3 numbered questions about it. Each question names the person and the thing, so it makes sense read alone. None can be answered by copying your reply, and each can be worked out from the numbers given.

HOW TO WRITE
- Never use template labels: no "Sharper:", "What you said", "Gap:", "Beyond the book", "Far away:", "Practice:", "Questions". Each paragraph opens with a bold phrase that IS its point, specific to his message. Reading only the bold phrases gives the whole answer. Bold nothing else.
  The bold phrase is the first words of its paragraph and a claim about his message or his plan. Never a general heading ("Some numbers move early"), never praise ("You already have the parts"), never a paragraph that is only a bold sentence. The beyond-the-book idea opens on his own plan too ("Your Monday number arrives late, so add an early one."); a sentence true for any reader ("Some numbers move before the goal does") is a heading.
  Bad: **Keep that, change one thing: read it weekly.**
  Good: **Counting rent as a cost of each sale will fool you.** Say the company pays ₹40,000 rent a month...
- Meaning first, name after. Explain every term in plain words the first time. Wrap only new concept names in == ==, at most two per reply.
- 7th-grade words, short sentences, plain verbs. Paragraphs of 3 sentences at most. Simple, not simpler: keep the real mechanism.
- No praise, hedges, filler, em dashes, or "not X but Y".
- Say each point once. Step 3 opens on something new, never the gap from step 2 said again.
- Numbers he can picture; mark guesses with "say". Invent examples, never facts or statistics about real companies.
- A list holds 3 items at most. With more, group them: up to 3 parent items, each a bold phrase naming the group, with its own items nested under it (indented two spaces).
- Format: **bold**, lists with "- ", numbered lines "1. ", "2. ", "3. ", nested items indented two spaces. No headings, no tables.`;
  const COUNT = `Count the distinct concepts in Ash's message: ideas he explains, uses or asks about (a concept from the page or any other). Return only JSON: {"n": number, "names": ["short name", ...]}`;

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
  const page = wrap.innerText.slice(0, 60000);
  let turns = [], topic = "", scenario = "", picked = "", ctl;

  // Auto: Haiku for one or two ideas, Sonnet at low thinking for more. A model he picks answers at the thinking he picks.
  const MODELS = { Haiku: { model: "claude-haiku-5-5", modelTier: "quick" }, Sonnet: { model: "claude-sonnet-5-5", modelTier: "default" }, Opus: { model: "claude-opus-5-5", modelTier: "complex" } };
  async function judge(msg) {
    const m = $("tmodel").value;
    if (m !== "auto") { const tier = m[0].toUpperCase() + m.slice(1), effort = $("teffort").value; return { tier, effort, opts: { ...MODELS[tier], effort }, what: "you picked it" }; }
    const low = " " + msg.toLowerCase() + " ";
    let names = Object.keys(IDEAS).filter(k => IDEAS[k].some(w => low.includes(w)));
    let n = Math.max(names.length, (msg.match(/\?/g) || []).length);
    if (n <= 2 && msg.trim().split(/\s+/).length > 70) {
      try { const r = await sample.json(`${COUNT}\n\nASH'S MESSAGE\n${msg}`, { model: "claude-haiku-5-5", modelTier: "quick", cache: false }); if (r?.n > n) { n = r.n; names = (r.names || []).slice(0, 5); } } catch (e) {}
    }
    const what = names.length ? `${names.length} idea${names.length > 1 ? "s" : ""}: ${names.join(", ")}` : "one idea";
    return n > 2 ? { tier: "Sonnet", effort: "low", opts: { ...MODELS.Sonnet, effort: "low" }, what } : { tier: "Haiku", effort: "", opts: { ...MODELS.Haiku }, what };
  }
  function setPicked(s) { picked = s; $("thl").hidden = !s; $("thlt").textContent = s ? "“" + s + "”" : ""; }
  function open(title, text) {
    if (title !== topic) { turns = []; $("tlog").textContent = ""; }
    topic = title; scenario = text ? text.slice(0, 6000) : "";
    $("tctx").textContent = "About: " + title;
    $("tutor").classList.add("open"); document.body.classList.add("tutor-open");
    $("tin").focus();
  }
  function close() { ctl?.abort(); $("tutor").classList.remove("open"); document.body.classList.remove("tutor-open"); $("ttab").focus(); }
  const esc = t => t.replace(/[&<>]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;" }[c]));
  const show = (el, t) => { el.innerHTML = esc(t).replace(/^\s*---\s*$/gm, "<hr>").replace(/\*\*(.+?)\*\*/g, "<b>$1</b>").replace(/==(.+?)==/g, '<span class="nm">$1</span>').replace(/\n/g, "<br>"); };

  async function send(msg) {
    const me = document.createElement("div"); me.className = "me"; me.textContent = msg;
    const route = document.createElement("div"); route.className = "route";
    const bot = document.createElement("div"); bot.className = "bot"; bot.textContent = "Thinking...";
    $("tlog").append(me, route, bot); bot.scrollIntoView({ block: "end" });
    turns.push({ role: "user", content: msg });
    turns = turns.slice(-30);  // the whole conversation goes along, so follow-ups keep the context
    const r = await judge(msg);
    route.innerHTML = `<b>${r.tier}${r.effort ? " · " + r.effort + " thinking" : ""}</b> ${esc(r.what)}`;
    if (r.tier !== "Haiku") bot.textContent = r.tier + " is thinking it through...";
    ctl?.abort(); ctl = new AbortController();
    const lead = `${RULES}\n\nTHE PAGE\n${page}` + (scenario ? `\n\nTHE SCENARIO HE WROTE ABOUT\n${scenario}` : "") + (picked ? `\n\nHE HIGHLIGHTED\n${picked}` : "");
    const first = turns[0].role === "user" ? [] : [{ role: "user", content: "(earlier)" }];
    try {
      const { text } = await sample([{ role: "user", content: lead }, { role: "assistant", content: "Ready." }, ...first, ...turns], {
        ...r.opts, cache: false, signal: ctl.signal,
        onText: ({ text }) => show(bot, text)
      });
      show(bot, text);
      turns.push({ role: "assistant", content: text });
    } catch (e) {
      bot.textContent = e.code === "cancelled" ? "" : ({ not_granted: "The tutor needs your OK to use Claude.", rate_limited: "Too many questions at once. Try again in a minute." }[e.code] || "Something went wrong. Ask again.");
      if (e.code !== "cancelled") $("tin").value = msg;
      turns.pop();
    }
  }

  // The model picker and the tutor's width, remembered in this browser.
  const store = { get: k => { try { return localStorage.getItem(k); } catch (e) { return null; } }, set: (k, v) => { try { v == null ? localStorage.removeItem(k) : localStorage.setItem(k, v); } catch (e) {} } };
  try { const p = JSON.parse(store.get("tutor-pick") || "{}"); if (p.model) $("tmodel").value = p.model; if (p.effort) $("teffort").value = p.effort; } catch (e) {}
  const syncPick = () => { $("teffort").disabled = $("tmodel").value === "auto"; };
  $("tmodel").onchange = $("teffort").onchange = () => { syncPick(); store.set("tutor-pick", JSON.stringify({ model: $("tmodel").value, effort: $("teffort").value })); };
  syncPick();
  const panel = $("tutor"), grip = $("tgrip");
  const setW = (w, save) => { const v = Math.round(Math.max(340, Math.min(w, innerWidth * 0.75))); document.documentElement.style.setProperty("--tutorw", v + "px"); if (save) store.set("tutor-w", v); };
  if (+store.get("tutor-w")) setW(+store.get("tutor-w"));
  const sizing = on => { panel.classList.toggle("sizing", on); document.body.classList.toggle("sizing", on); };
  grip.onpointerdown = e => { e.preventDefault(); grip.setPointerCapture(e.pointerId); sizing(true); };
  grip.onpointermove = e => { if (grip.hasPointerCapture(e.pointerId)) setW(innerWidth - e.clientX); };
  grip.onlostpointercapture = () => { sizing(false); setW(panel.getBoundingClientRect().width, true); };
  grip.ondblclick = () => { document.documentElement.style.removeProperty("--tutorw"); store.set("tutor-w", null); };
  grip.onkeydown = e => { const k = { ArrowLeft: 40, ArrowRight: -40 }[e.key]; if (k) { e.preventDefault(); setW(panel.getBoundingClientRect().width + k, true); } };

  // Keep a highlight: pressing the tab must not clear the selection.
  $("ttab").onmousedown = e => e.preventDefault();
  $("ttab").onclick = () => { setPicked(getSelection().toString().trim().slice(0, 1500)); open(document.title, ""); };
  $("thlx").onclick = () => setPicked("");
  $("tx").onclick = close;
  addEventListener("keydown", e => { if (e.key === "Escape" && $("tutor").classList.contains("open")) close(); });
  $("tf").onsubmit = e => { e.preventDefault(); const v = $("tin").value.trim(); if (v) { $("tin").value = ""; send(v); } };
  $("tin").onkeydown = e => { if (e.key === "Enter" && !e.shiftKey) { e.preventDefault(); $("tf").requestSubmit(); } };
  thinkBtns.forEach(b => b.onclick = () => {
    const box = b.closest(".think"), v = box.querySelector("textarea").value.trim();
    if (!v) return;
    const q = b.closest(".q") || b.closest(".pair");
    setPicked("");
    open((q.querySelector("h3") || q.querySelector(".lbl")).textContent.trim(), q.innerText);
    send("My thinking on the scenario:\n" + v);
  });
})();
</script>
```

The `(earlier)` line keeps the roles alternating when old turns are trimmed (the tutor sends his last 30 turns, so a back-and-forth keeps its context; every exchange stays in the panel's one scrolling log until he opens the tutor on a different question). The `UNIT` and `IDEAS` values above are an example from the Managerial Accounting page: replace them for every page. A page published without `sample` hides the tab and the send buttons, and the hidden answers still work. No notes or database for study pages (Ash: "I'm going to barely use that").
