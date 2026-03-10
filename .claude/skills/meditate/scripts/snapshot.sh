#!/bin/bash
# Concatenate all .md files in a directory into a single snapshot.
# Usage: snapshot.sh <directory>
# Output goes to stdout.

set -euo pipefail

DIR="${1:-.}"

find "$DIR" -name '*.md' -type f | sort | while read -r file; do
  echo "=== $file ==="
  cat "$file"
  echo ""
  echo ""
done
