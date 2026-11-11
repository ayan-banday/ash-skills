#!/bin/bash
# Runs inside a cloud environment's setup script, before Claude starts.
# The script pasted into the environment only fetches this repo and calls this file,
# so every change here reaches the next fresh cloud session with no new paste.

MP="$HOME/.claude/plugins/marketplaces/ash-skills"
[ -d "$MP/plugins" ] || { echo "ash-skills: marketplace not found at $MP" >&2; exit 0; }

# 1. Install every plugin in the marketplace, so /write, /visualize, /plan, /build and /learn load.
for d in "$MP"/plugins/*/; do
  p=$(basename "$d")
  claude plugin install "$p@ash-skills" --scope user || echo "ash-skills: could not install $p" >&2
done

# 1b. Install the outside skills marked "Installed" in OUTSIDE-SKILLS.md (keep the two lists the same).
EMIL_SKILLS="emil-design-eng pick-ui-library mobile-native"
TMP=$(mktemp -d)
if git clone -q --depth 1 https://github.com/emilkowalski/skills "$TMP/emil" 2>/dev/null; then
  mkdir -p "$HOME/.claude/skills"
  for s in $EMIL_SKILLS; do
    if [ -d "$TMP/emil/skills/$s" ]; then
      rm -rf "$HOME/.claude/skills/$s" && cp -r "$TMP/emil/skills/$s" "$HOME/.claude/skills/$s"
    else
      echo "ash-skills: Emil's $s not found" >&2
    fi
  done
else
  echo "ash-skills: could not fetch emilkowalski/skills" >&2
fi
rm -rf "$TMP"

# 2. Tell Claude where to find a skill that didn't load, or one newer than this session's copy.
mkdir -p "$HOME/.claude"
touch "$HOME/.claude/CLAUDE.md"
sed -i '/<!-- ash-skills:start -->/,/<!-- ash-skills:end -->/d' "$HOME/.claude/CLAUDE.md"
cat >> "$HOME/.claude/CLAUDE.md" <<EOF
<!-- ash-skills:start -->
# Ash's skills

Ash's skills live in the GitHub repo \`ayan-banday/ash-skills\`, with a copy in this session at \`$MP\`.
Each skill is \`plugins/<plugin>/skills/<skill>/SKILL.md\`. The README there lists them all.

When Ash names a skill that isn't loaded, or asks for one from his skills repo:
1. Run \`claude plugin marketplace update ash-skills\` to get the newest copy.
2. Find the skill's SKILL.md under \`$MP/plugins/\`, read it, and follow it as if it had been invoked.
3. Read the files it points to (references, scripts, assets) from the same skill folder.

**Before a major build** (a new app, site or tool, or work that takes more than one session), ask Ash once: "This is a big build. Want me to check your outside skills for any that could help?" With his yes, follow \`$MP/OUTSIDE-SKILLS.md\`: it lists other people's skills that aren't installed (Emil Kowalski, Ponytail, Matt Pocock, Anthropic), how to fetch one for a single project, and the UI libraries he has saved. Fetch nothing without his yes, and skip the question for small jobs.
<!-- ash-skills:end -->
EOF

# 3. Tell Claude how to reach Fuji when it isn't in the session.
sed -i '/<!-- fuji:start -->/,/<!-- fuji:end -->/d' "$HOME/.claude/CLAUDE.md"
cat >> "$HOME/.claude/CLAUDE.md" <<'EOF'
<!-- fuji:start -->
# Fuji

Fuji is Ash's self-regulation system: the private repo `ayan-banday/fuji`. When the work is about Fuji (his week page, maps, tickets, Sherpas, the night run) and it isn't in this session, attach it with `add_repo` (owner `ayan-banday`, repo `fuji`, access `push`) before anything else, clone it to the path the tool gives, and follow its CLAUDE.md.
<!-- fuji:end -->
EOF

exit 0
