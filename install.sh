#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_NAME="math-visual-solver"
SKILL_SRC="$SCRIPT_DIR/$SKILL_NAME"
CODEX_HOME_DIR="${CODEX_HOME:-$HOME/.codex}"
DEST_ROOT="$CODEX_HOME_DIR/skills"
DEST="$DEST_ROOT/$SKILL_NAME"

echo "Installing $SKILL_NAME for Codex..."
echo "Package: $SCRIPT_DIR"
echo "Target:  $DEST"
echo

if [[ ! -d "$SKILL_SRC" || ! -f "$SKILL_SRC/SKILL.md" ]]; then
  echo "ERROR: Cannot find bundled skill directory: $SKILL_SRC" >&2
  echo "Keep this installer together with the $SKILL_NAME directory." >&2
  exit 1
fi

mkdir -p "$DEST_ROOT"

if [[ -e "$DEST" ]]; then
  BACKUP="$DEST.backup-$(date +%Y%m%d-%H%M%S)"
  echo "Existing skill found. Moving it to:"
  echo "$BACKUP"
  mv "$DEST" "$BACKUP"
fi

cp -R "$SKILL_SRC" "$DEST"
chmod +x "$DEST/scripts/scaffold_math_pdf.py" 2>/dev/null || true

required_files=(
  "SKILL.md"
  "agents/openai.yaml"
  "references/workflow.md"
  "scripts/scaffold_math_pdf.py"
)

for rel in "${required_files[@]}"; do
  if [[ ! -f "$DEST/$rel" ]]; then
    echo "ERROR: Missing installed file: $DEST/$rel" >&2
    exit 1
  fi
done

echo
echo "Installed successfully."
echo "Restart Codex to pick up the new skill."
echo
echo "After restart, use:"
echo '  使用 $math-visual-solver ...'
