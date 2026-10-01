#!/usr/bin/env bash
# Checks that the AI-SDLC artefacts are present and consistent. Runs in CI.

set -uo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

failures=0
fail() { echo "✗ $1"; failures=$((failures + 1)); }

for f in AGENTS.md docs/INDEX.json docs/TASKS.md docs/PROJECT.md \
         docs/STANDARDS.md docs/AGENT-GUIDANCE.md \
         docs/specs/UC-TEMPLATE.md docs/adr/ADR-TEMPLATE.md \
         .github/copilot-instructions.md; do
  [ -f "$f" ] || fail "missing $f"
done

for dir in skills/*/; do
  [ -f "${dir}SKILL.md" ] || fail "missing ${dir}SKILL.md"
  python3 -m json.tool "${dir}index.json" > /dev/null 2>&1 || fail "missing or invalid ${dir}index.json"
done

python3 - <<'PY' || failures=$((failures + 1))
import json, os, sys
try:
    index = json.load(open("docs/INDEX.json"))
except Exception as e:
    print(f"✗ docs/INDEX.json is not valid JSON: {e}")
    sys.exit(1)
paths = [p["skill"] for p in index["phases"]] + [p["detail"] for p in index["phases"]]
paths += [f["path"] for f in index["key_files"]]
missing = [p for p in paths if not os.path.exists(p)]
for p in missing:
    print(f"✗ docs/INDEX.json references missing path {p}")
sys.exit(1 if missing else 0)
PY

phase=$(sed -n 's/^PHASE: *//p' docs/TASKS.md | head -1)
status=$(sed -n 's/^STATUS: *//p' docs/TASKS.md | head -1)
[[ "$phase" =~ ^[0-5]$ ]] || fail "docs/TASKS.md PHASE must be 0-5 (found '$phase')"
[[ "$status" =~ ^(ready|in-progress|done|blocked)$ ]] || fail "docs/TASKS.md STATUS must be ready, in-progress, done or blocked (found '$status')"

if [[ "$phase" =~ ^[1-5]$ ]] && grep -q 'TBD' docs/PROJECT.md; then
  fail "docs/PROJECT.md still contains TBD after BOOTSTRAP (PHASE $phase)"
fi

headings=$(grep '^## ' docs/specs/UC-TEMPLATE.md)
for uc in docs/specs/UC-*.md; do
  [ "$uc" = docs/specs/UC-TEMPLATE.md ] && continue
  [ -e "$uc" ] || continue
  while IFS= read -r h; do
    grep -qxF "$h" "$uc" || fail "$uc is missing section '$h'"
  done <<< "$headings"
done

if [ "$failures" -eq 0 ]; then
  echo "✓ AI-SDLC lifecycle checks passed"
else
  echo "$failures lifecycle problem(s) found."
  exit 1
fi
