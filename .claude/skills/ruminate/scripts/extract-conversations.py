#!/usr/bin/env python3
"""
Extract and batch conversation history from Claude Code JSONL files.

Usage:
    python3 extract-conversations.py [options]

Options:
    --project-dir DIR   Project conversation directory (auto-detected if omitted)
    --after DATE        Only include conversations after DATE (YYYY-MM-DD)
    --before DATE       Only include conversations before DATE (YYYY-MM-DD)
    --batches N         Number of output batches (default: 5)
    --max-msg-len N     Max characters per message (default: 3000 for user, 800 for assistant)
    --output-dir DIR    Output directory (default: temp/ruminate/)
"""

import argparse
import json
import os
import sys
from datetime import datetime
from pathlib import Path


def find_project_dir():
    """Auto-detect the Claude project conversation directory."""
    claude_dir = Path.home() / ".claude" / "projects"
    if not claude_dir.exists():
        return None

    # Find directories matching the current project path
    cwd = os.getcwd()
    # Claude encodes paths with dashes
    encoded = cwd.replace("/", "-").lstrip("-")

    for d in claude_dir.iterdir():
        if d.is_dir() and encoded in d.name:
            return d

    return None


def parse_jsonl(filepath, after=None, before=None):
    """Parse a single JSONL conversation file."""
    messages = []
    try:
        with open(filepath, "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    entry = json.loads(line)
                    # Extract timestamp if available
                    ts = entry.get("timestamp", entry.get("created_at", ""))
                    if ts and after:
                        try:
                            entry_date = datetime.fromisoformat(
                                ts.replace("Z", "+00:00")
                            ).date()
                            if entry_date < after:
                                continue
                        except (ValueError, TypeError):
                            pass
                    if ts and before:
                        try:
                            entry_date = datetime.fromisoformat(
                                ts.replace("Z", "+00:00")
                            ).date()
                            if entry_date > before:
                                continue
                        except (ValueError, TypeError):
                            pass

                    role = entry.get("role", "")
                    content = ""

                    # Handle different content formats
                    raw = entry.get("content", entry.get("message", ""))
                    if isinstance(raw, str):
                        content = raw
                    elif isinstance(raw, list):
                        parts = []
                        for block in raw:
                            if isinstance(block, str):
                                parts.append(block)
                            elif isinstance(block, dict):
                                text = block.get("text", block.get("content", ""))
                                if text:
                                    parts.append(text)
                        content = "\n".join(parts)

                    if role and content:
                        messages.append({"role": role, "content": content})
                except json.JSONDecodeError:
                    continue
    except (IOError, OSError) as e:
        print(f"Warning: Could not read {filepath}: {e}", file=sys.stderr)

    return messages


def truncate_messages(messages, max_user=3000, max_assistant=800):
    """Truncate messages to stay within size limits."""
    result = []
    for msg in messages:
        content = msg["content"]
        limit = max_user if msg["role"] == "user" else max_assistant
        if len(content) > limit:
            content = content[:limit] + "\n[...truncated]"
        result.append({"role": msg["role"], "content": content})
    return result


def batch_conversations(conversations, n_batches):
    """Split conversations into N roughly equal batches."""
    batches = [[] for _ in range(n_batches)]
    for i, conv in enumerate(conversations):
        batches[i % n_batches].append(conv)
    return [b for b in batches if b]  # Remove empty batches


def main():
    parser = argparse.ArgumentParser(description="Extract Claude conversation history")
    parser.add_argument("--project-dir", type=str, help="Project conversation directory")
    parser.add_argument("--after", type=str, help="Only after DATE (YYYY-MM-DD)")
    parser.add_argument("--before", type=str, help="Only before DATE (YYYY-MM-DD)")
    parser.add_argument("--batches", type=int, default=5, help="Number of output batches")
    parser.add_argument("--max-msg-len", type=int, default=3000)
    parser.add_argument("--output-dir", type=str, default="temp/ruminate/")
    args = parser.parse_args()

    # Find project dir
    project_dir = Path(args.project_dir) if args.project_dir else find_project_dir()
    if not project_dir or not project_dir.exists():
        print("Error: Could not find project conversation directory.", file=sys.stderr)
        print("Use --project-dir to specify it manually.", file=sys.stderr)
        sys.exit(1)

    # Parse date filters
    after = datetime.strptime(args.after, "%Y-%m-%d").date() if args.after else None
    before = datetime.strptime(args.before, "%Y-%m-%d").date() if args.before else None

    # Find and parse conversation files
    jsonl_files = sorted(project_dir.glob("*.jsonl"))
    if not jsonl_files:
        print(f"No conversation files found in {project_dir}", file=sys.stderr)
        sys.exit(1)

    print(f"Found {len(jsonl_files)} conversation files in {project_dir}")

    conversations = []
    for f in jsonl_files:
        messages = parse_jsonl(f, after=after, before=before)
        if messages:
            messages = truncate_messages(messages, max_user=args.max_msg_len)
            conversations.append(
                {"file": f.name, "message_count": len(messages), "messages": messages}
            )

    if not conversations:
        print("No conversations found matching filters.", file=sys.stderr)
        sys.exit(1)

    print(f"Extracted {len(conversations)} conversations with messages")

    # Batch and write output
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    batches = batch_conversations(conversations, args.batches)
    for i, batch in enumerate(batches):
        output_file = output_dir / f"batch-{i + 1}.json"
        with open(output_file, "w") as f:
            json.dump(batch, f, indent=2)
        total_msgs = sum(c["message_count"] for c in batch)
        print(f"  Batch {i + 1}: {len(batch)} conversations, {total_msgs} messages → {output_file}")

    print(f"\nDone. {len(batches)} batches written to {output_dir}")


if __name__ == "__main__":
    main()
