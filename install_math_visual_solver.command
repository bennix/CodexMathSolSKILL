#!/bin/zsh
set -euo pipefail

SCRIPT_DIR="${0:A:h}"
"$SCRIPT_DIR/install.sh"

echo
read -r "?Press Return to close..."
