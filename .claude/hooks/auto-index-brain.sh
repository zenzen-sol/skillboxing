#!/bin/bash
# Rebuilds brain/index.md when brain files change on disk.
# Triggered by PostToolUse hook whenever a tool touches brain/.

set -euo pipefail

BRAIN_DIR="$CLAUDE_PROJECT_DIR/brain"
INDEX="$BRAIN_DIR/index.md"

# Collect all .md files except index.md itself
mapfile -t FILES < <(find "$BRAIN_DIR" -name '*.md' ! -name 'index.md' -type f | sort)

# Collect current wikilinks from index
CURRENT_LINKS=""
if [ -f "$INDEX" ]; then
  CURRENT_LINKS=$(grep -oP '\[\[.*?\]\]' "$INDEX" 2>/dev/null || true)
fi

# Build expected links
EXPECTED_LINKS=""
for f in "${FILES[@]}"; do
  # Strip brain dir prefix and .md extension
  rel="${f#$BRAIN_DIR/}"
  rel="${rel%.md}"
  EXPECTED_LINKS+="[[$rel]]"$'\n'
done

# Compare — rebuild if drift detected
if [ "$CURRENT_LINKS" = "$EXPECTED_LINKS" ]; then
  exit 0
fi

# Rebuild index grouped by top-level directory
{
  echo "# Brain"
  echo ""

  prev_section=""
  for f in "${FILES[@]}"; do
    rel="${f#$BRAIN_DIR/}"
    rel="${rel%.md}"

    # Determine section from first path component
    if [[ "$rel" == */* ]]; then
      section="${rel%%/*}"
    else
      section="root"
    fi

    # Print section header on change
    if [ "$section" != "$prev_section" ]; then
      section_title="$(echo "$section" | sed 's/-/ /g' | sed 's/\b\(.\)/\u\1/g')"
      echo ""
      echo "## $section_title"
      echo ""
      prev_section="$section"
    fi

    echo "- [[$rel]]"
  done
} > "$INDEX"
