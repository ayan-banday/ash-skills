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
# Each entry is owner/repo:skill,skill. Each fetch gives up after 30 seconds, so a slow network never blocks the session.
OUTSIDE="emilkowalski/skills:emil-design-eng,pick-ui-library,mobile-native backnotprop/pstack:ketchup,sharpen,interrogate,arena,in-your-own-words,bro"
TMP=$(mktemp -d 2>/dev/null)
if [ -n "$TMP" ] && [ -d "$TMP" ]; then
  mkdir -p "$HOME/.claude/skills"
  for entry in $OUTSIDE; do
    repo=${entry%%:*}
    dir="$TMP/${repo/\//-}"
    if GIT_TERMINAL_PROMPT=0 timeout 30 git clone -q --depth 1 "https://github.com/$repo" "$dir" 2>/dev/null; then
      IFS=, read -ra names <<< "${entry#*:}"
      for s in "${names[@]}"; do
        if [ -d "$dir/skills/$s" ]; then
          rm -rf "$HOME/.claude/skills/$s" && cp -r "$dir/skills/$s" "$HOME/.claude/skills/$s"
        else
          echo "ash-skills: $s not found in $repo" >&2
        fi
      done
    else
      echo "ash-skills: could not fetch $repo" >&2
    fi
  done
  rm -rf "$TMP"
fi

# 1c. pstack's interrogate and arena name Grok by default, which Claude Code can't run. Point them at Claude models,
# unless a models file already exists (it may be Ash's own choice).
mkdir -p "$HOME/.claude/rules"
[ -f "$HOME/.claude/rules/pstack-models.md" ] || cat > "$HOME/.claude/rules/pstack-models.md" <<'EOF'
# pstack models (written by ash-skills cloud/setup.sh; only Claude models exist here)
arena runners: claude-opus-5-5, claude-sonnet-5-5
arena cross-judge pool: claude-opus-5-5
interrogate reviewers: claude-opus-5-5, claude-sonnet-5-5
EOF

# 2. Tell Claude where to find a skill that didn't load, or one newer than this session's copy.
mkdir -p "$HOME/.claude"
touch "$HOME/.claude/CLAUDE.md"
# Make sure the file ends in a line break, or the block markers glue onto Ash's last line and the next run deletes it.
[ -n "$(tail -c1 "$HOME/.claude/CLAUDE.md")" ] && echo >> "$HOME/.claude/CLAUDE.md"
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
