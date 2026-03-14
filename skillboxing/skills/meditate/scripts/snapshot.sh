#!/bin/bash
# Concatenate all brain files into a single snapshot for review.
# Usage: snapshot.sh [directory]
# Output goes to stdout.

set -euo pipefail

DIR="${1:-brain}"

[ -d "$DIR" ] || { echo "No brain directory found at $DIR"; exit 1; }

find "$DIR" -name '*.md' -type f | sort | while read -r file; do
  echo "=== $file ==="
  cat "$file"
  echo ""
done
