"""Build every plugin in ash-skills from docs/BUILD-PLAN.md's name map.

Copies Ash's skills from ~/.claude/skills and Matt Pocock's from the installed plugin cache,
renames them, rewrites their descriptions and the links between them. Safe to re-run: it
rebuilds the copied skill folders and leaves Ash-made skills (make-skill, which-skill) in place.
Ran once on 2026-10-20. Guarded: see the bottom of the file.
"""
import json, re, shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HOME = Path.home()
ASH = HOME / ".claude/skills"
MATT = HOME / ".claude/plugins/cache/claude-plugins-official/mattpocock-skills/1.3.1"

PLUGINS = {
 "write": "How do I write words people read, and docs Claude reads?",
 "visualize": "How do I show an idea so people get it without reading much?",
 "plan": "How do I decide what to build before building it?",
 "build": "How do I build and fix code in Charlotte or the micro-SaaS, and the tools Claude uses?",
 "learn": "How do I learn a topic, or make sense of a pile of files?",
}

# (plugin, new name, source dir, bracket, question)
A, M = ASH, MATT / "skills"
SKILLS = [
 ("write", "course-lesson-udyaan", A/"course-writer", "[Udyaan course · was course-writer]", "How do I write a Day N lesson or course page students actually read?"),
 ("write", "headline-angles-substack", A/"newsletter-headlines", "[Substack · was newsletter-headlines]", "How do I find the headline that makes people open my Substack post?"),
 ("write", "re-explain-matt", M/"productivity/wait-what", "[Matt: wait-what]", "How do I get Claude to re-explain a reply that didn't make sense?"),
 ("write", "agent-docs-matt", M/"productivity/writing-for-agents", "[Matt: writing-for-agents]", "How do I write a skill or CLAUDE.md that Claude follows every time?"),

 ("visualize", "story-plan", A/"visual-storytelling", "[was visual-storytelling]", "How do I turn an abstract idea into a story people watch?"),
 ("visualize", "polished-doc", A/"clear-documents", "[was clear-documents]", "How do I turn my draft into a clean PDF or Word file?"),
 ("visualize", "brief-page-udyaan", A/"clear-visual-html", "[Udyaan teammates · was clear-visual-html]", "How do I brief a teammate so they arrive knowing what we're deciding?"),
 ("visualize", "pitch-site-udyaan", A/"clear-proposal-site", "[Udyaan · website · was clear-proposal-site]", "How do I make an outside reader say 'Hell yeah, let's do this'?"),

 ("plan", "grill-idea-matt", M/"productivity/grill-me", "[Matt: grill-me]", "How do I find the holes in an idea before I commit to it?"),
 ("plan", "grill-with-docs-matt", M/"engineering/grill-with-docs", "[Matt: grill-with-docs]", "How do I sharpen a feature and keep a record of what we decided?"),
 ("plan", "chart-project-wayfinder-matt", M/"engineering/wayfinder", "[Matt: wayfinder]", "How do I plan a project too big for one session when I can't see the route yet?"),
 ("plan", "write-spec-matt", M/"engineering/to-spec", "[Matt: to-spec]", "How do I turn what we just decided into one written plan?"),
 ("plan", "split-tickets-matt", M/"engineering/to-tickets", "[Matt: to-tickets]", "How do I split a spec into tasks Claude can build one at a time?"),
 ("plan", "setup-tracker-matt", M/"engineering/setup-matt-pocock-skills", "[Matt: setup-matt-pocock-skills]", "Where should my plans and tickets be saved? Run once per repo before chart-project-wayfinder-matt, split-tickets-matt or build-ticket-matt."),
 ("plan", "try-prototype-matt", M/"engineering/prototype", "[Matt: prototype]", "How do I test whether a design feels right before building it properly?"),
 ("plan", "gather-facts-matt", M/"engineering/research", "[Matt: research]", "How do I get facts checked against official sources while I keep working?"),
 ("plan", "ask-someone-matt", M/"productivity/to-questionnaire", "[Matt: to-questionnaire]", "How do I get an answer that's in someone else's head?"),
 ("plan", "grilling-matt", M/"productivity/grilling", "[Matt: grilling · helper]", "The question engine behind grill-idea-matt, grill-with-docs-matt and chart-project-wayfinder-matt."),
 ("plan", "domain-modeling-matt", M/"engineering/domain-modeling", "[Matt: domain-modeling · helper]", "Keeps a project's names consistent in GLOSSARY.md."),

 ("build", "build-ticket-matt", M/"engineering/implement", "[Matt: implement]", "How do I get one decided ticket built without Claude redesigning it?"),
 ("build", "build-whole-spec-matt", M/"engineering/implement-spec", "[Matt: implement-spec]", "How do I build a whole spec at once with several helpers?"),
 ("build", "test-first-matt", M/"engineering/tdd", "[Matt: tdd]", "How do I build a feature so tests prove it works?"),
 ("build", "find-bug-matt", M/"engineering/diagnosing-bugs", "[Matt: diagnosing-bugs]", "How do I find the real cause of a bug instead of guessing?"),
 ("build", "review-code-matt", M/"engineering/code-review", "[Matt: code-review]", "How do I check changes before merging them?"),
 ("build", "find-simplifications-matt", M/"engineering/improve-codebase-architecture", "[Matt: improve-codebase-architecture]", "How do I find parts of the code that are more complicated than they need to be?"),
 ("build", "setup-walkthrough-matt", M/"engineering/wizard", "[Matt: wizard]", "How do I get through setup steps only I can do, like pasting API keys?"),
 ("build", "write-pr-matt", M/"engineering/pr", "[Matt: pr]", "How do I write a pull request someone can review fast?"),
 ("build", "improve-next-time-matt", M/"engineering/retro", "[Matt: retro]", "How do I make the next build go smoother than this one?"),
 ("build", "handoff-matt", M/"productivity/handoff", "[Matt: handoff]", "How do I move this work to a new folder, tool or person?"),
 ("build", "codebase-design-matt", M/"engineering/codebase-design", "[Matt: codebase-design · helper]", "Words for shaping code into simple parts, used by test-first-matt and find-simplifications-matt."),

 ("learn", "study-shasta", A/"study", "[Shasta · was study]", "How do I learn a topic the Shasta way?"),
 ("learn", "graphify", A/"graphify", "[files to knowledge graph]", "How do I see how everything in a folder connects?"),
]

# Ash-made skills already in the repo: only their leading (bracket) becomes [bracket].
KEEP = {"build": ["make-skill"], "learn": ["which-skill"]}

NEW = {name: f"{p}:{name}" for p, name, *_ in SKILLS}

# Matt skill names -> new names, used where one skill calls another.
MATT_CALLS = {
 "grilling": "grilling-matt", "domain-modeling": "domain-modeling-matt", "research": "gather-facts-matt",
 "prototype": "try-prototype-matt", "code-review": "review-code-matt", "codebase-design": "codebase-design-matt",
 "tdd": "test-first-matt", "wayfinder": "chart-project-wayfinder-matt", "grill-with-docs": "grill-with-docs-matt",
 "setup-matt-pocock-skills": "setup-tracker-matt", "improve-codebase-architecture": "find-simplifications-matt",
 "to-spec": "write-spec-matt", "to-tickets": "split-tickets-matt", "implement": "build-ticket-matt",
 "implement-spec": "build-whole-spec-matt", "grill-me": "grill-idea-matt", "handoff": "handoff-matt",
 "retro": "improve-next-time-matt", "pr": "write-pr-matt", "wizard": "setup-walkthrough-matt",
 "diagnosing-bugs": "find-bug-matt", "wait-what": "re-explain-matt", "writing-for-agents": "agent-docs-matt",
 "to-questionnaire": "ask-someone-matt",
}
# Ash's old skill names -> new. Unique tokens, safe to replace everywhere in his skills.
ASH_NAMES = {
 "visual-storytelling": "story-plan", "clear-documents": "polished-doc", "clear-visual-html": "brief-page-udyaan",
 "clear-proposal-site": "pitch-site-udyaan", "course-writer": "course-lesson-udyaan",
 "newsletter-headlines": "headline-angles-substack",
}
TEXT = {".md", ".html", ".py", ".sh", ".js", ".txt", ".json", ".yaml", ".yml", ".css"}


def full(old):
    new = MATT_CALLS[old]
    return NEW[new]


def rewrite_matt(t):
    # `Skill tool with "x"` and `for "x" and "y"` on lines that mention the Skill tool
    def line(l):
        if "Skill tool" not in l:
            return l
        return re.sub(r'(["`])([a-z-]+)\1', lambda m: f'{m.group(1)}{full(m.group(2))}{m.group(1)}' if m.group(2) in MATT_CALLS else m.group(0), l)
    t = "\n".join(line(l) for l in t.split("\n"))
    # `/old` commands in backticks
    t = re.sub(r"`/([a-z-]+)`", lambda m: f"`/{full(m.group(1))}`" if m.group(1) in MATT_CALLS else m.group(0), t)
    t = t.replace("Skills like `to-tickets`, `triage`, and `to-spec`",
                  "Skills like `plan:split-tickets-matt` and `plan:write-spec-matt`")
    return t


def rewrite_ash(t):
    for old, new in ASH_NAMES.items():
        t = t.replace(old, new)
    return t


def frontmatter(text, name, desc):
    assert text.startswith("---"), "no frontmatter"
    head, body = text[3:].split("\n---", 1)
    old = re.search(r"^description:\s*(.*)$", head, re.M).group(1).strip()
    if old[:1] in "\"'":
        old = old[1:-1]
    old = re.sub(r"^[\(\[][^\)\]]*[\)\]]\s*", "", old)  # drop any earlier bracket
    full_desc = desc if desc is not None else old
    head = re.sub(r"^name:.*$", f"name: {name}", head, count=1, flags=re.M)
    head = re.sub(r"^description:.*$", "description: " + json.dumps(full_desc, ensure_ascii=False), head, count=1, flags=re.M)
    return "---" + head + "\n---" + body, old


def build():
    report = []
    for p, q in PLUGINS.items():
        d = ROOT / "plugins" / p
        (d / ".claude-plugin").mkdir(parents=True, exist_ok=True)
        (d / "skills").mkdir(exist_ok=True)
        keep = set(KEEP.get(p, []))
        for child in (d / "skills").iterdir():
            if child.name not in keep:
                shutil.rmtree(child)
        pj = d / ".claude-plugin/plugin.json"
        ver = json.loads(pj.read_text(encoding="utf-8")).get("version", "0.0.0") if pj.exists() else "0.0.0"
        major, minor, _ = (int(x) for x in ver.split("."))
        pj.write_text(json.dumps({"name": p, "version": f"{major}.{minor + 1}.0", "description": q,
                                  "author": {"name": "Ash Banday"}}, indent=2) + "\n", encoding="utf-8")
        has_matt = any(src.is_relative_to(MATT) for pp, _, src, *_ in SKILLS if pp == p)
        lic = d / "LICENSE-matt-pocock"
        if has_matt:
            shutil.copy(MATT / "LICENSE", lic)
        elif lic.exists():
            lic.unlink()

    for p, name, src, bracket, question in SKILLS:
        dst = ROOT / "plugins" / p / "skills" / name
        shutil.copytree(src, dst, ignore=shutil.ignore_patterns("agents", "__pycache__", ".graphify_version"))
        is_matt = src.is_relative_to(MATT)
        for f in dst.rglob("*"):
            if not f.is_file() or f.suffix not in TEXT:
                continue
            t = f.read_text(encoding="utf-8")
            t = rewrite_matt(t) if is_matt else rewrite_ash(t)
            if f == dst / "SKILL.md":
                t, old = frontmatter(t, name, None)
                desc = f"{bracket} {question} {old}".strip()
                t, _ = frontmatter(t, name, desc)
                report.append((len(desc), f"{p}:{name}"))
            f.write_text(t, encoding="utf-8", newline="\n")
        if (src / ".graphify_version").exists():
            shutil.copy(src / ".graphify_version", dst / ".graphify_version")

    # Ash-made skills: (bracket) -> [bracket]
    for p, names in KEEP.items():
        for n in names:
            f = ROOT / "plugins" / p / "skills" / n / "SKILL.md"
            if f.exists():
                t = f.read_text(encoding="utf-8")
                t = re.sub(r'^(description:\s*"?)\(([^)]*)\)', r"\1[\2]", t, count=1, flags=re.M)
                f.write_text(t, encoding="utf-8", newline="\n")

    mp = ROOT / ".claude-plugin/marketplace.json"
    m = json.loads(mp.read_text(encoding="utf-8"))
    m["plugins"] = [{"name": p, "source": f"./plugins/{p}", "description": q} for p, q in PLUGINS.items()]
    mp.write_text(json.dumps(m, indent=2) + "\n", encoding="utf-8")

    for n, s in sorted(report, reverse=True)[:5]:
        print(f"longest descriptions: {n:5d} chars  {s}")
    over = [s for n, s in report if n > 1536]
    print("over 1536:", over or "none")
    print("skills built:", len(report))


if __name__ == "__main__":
    import sys
    if "--i-know-this-overwrites-edits" not in sys.argv:
        sys.exit("One-time migration, already run on 2026-10-20. The skills in plugins/ are now the master copies; "
                 "re-running overwrites edits. Pass --i-know-this-overwrites-edits to run anyway.")
    build()
