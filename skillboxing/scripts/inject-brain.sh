#!/bin/bash
# Injects brain/index.md into context at session start.
# If no brain folder exists yet, says so — /reflect will create it.

BRAIN_INDEX="brain/index.md"

if [ -f "$BRAIN_INDEX" ]; then
  echo "Project brain loaded — read relevant files before acting:"
  echo ""
  cat "$BRAIN_INDEX"
else
  echo "No project brain found. Use /skillboxing:reflect to start capturing knowledge."
fi
