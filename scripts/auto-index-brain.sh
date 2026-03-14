#!/bin/bash
# Keeps brain/index.md in sync with files on disk.
# Additive: adds bare links for new files, removes links to deleted files.
# Preserves all other content (descriptions, headers, structure).
# Triggered by PostToolUse hook whenever a tool touches brain/.

set -euo pipefail

BRAIN_DIR="brain"
INDEX="$BRAIN_DIR/index.md"

# Nothing to index if no brain dir
[ -d "$BRAIN_DIR" ] || exit 0

# Collect all .md files except index.md
mapfile -t FILES < <(find "$BRAIN_DIR" -name '*.md' ! -name 'index.md' -type f | sort)

# If no brain files, nothing to do
[ ${#FILES[@]} -gt 0 ] || exit 0

# If no index exists, create one from scratch
if [ ! -f "$INDEX" ]; then
  {
    echo "# Brain"
    echo ""
    for f in "${FILES[@]}"; do
      rel="${f#$BRAIN_DIR/}"
      rel="${rel%.md}"
      echo "- [[$rel]]"
    done
  } > "$INDEX"
  exit 0
fi

# Build set of expected wikilinks from files on disk
declare -A EXPECTED
for f in "${FILES[@]}"; do
  rel="${f#$BRAIN_DIR/}"
  rel="${rel%.md}"
  EXPECTED["$rel"]=1
done

# Find which links already exist in the index
declare -A FOUND
while IFS= read -r link; do
  FOUND["$link"]=1
done < <(grep -oP '\[\[\K[^\]]+' "$INDEX" 2>/dev/null || true)

# Remove lines containing links to files that no longer exist
TEMP=$(mktemp)
while IFS= read -r line; do
  link=$(echo "$line" | grep -oP '\[\[\K[^\]]+' 2>/dev/null || true)
  if [ -n "$link" ] && [ -z "${EXPECTED[$link]+x}" ]; then
    # Dead link — skip this line
    continue
  fi
  echo "$line"
done < "$INDEX" > "$TEMP"
mv "$TEMP" "$INDEX"

# Append bare links for new files not yet in the index
NEW_FILES=()
for rel in "${!EXPECTED[@]}"; do
  if [ -z "${FOUND[$rel]+x}" ]; then
    NEW_FILES+=("$rel")
  fi
done

if [ ${#NEW_FILES[@]} -gt 0 ]; then
  IFS=$'\n' SORTED=($(sort <<<"${NEW_FILES[*]}")); unset IFS
  echo "" >> "$INDEX"
  for rel in "${SORTED[@]}"; do
    echo "- [[$rel]]" >> "$INDEX"
  done
fi
