#!/usr/bin/env python3
"""Rewrite repo paths of the four papers from papers/X.md to wiki/papers/X.md in every tracked text file.

Rewritten: papers/X.md not preceded by a word character, '.', ':', '/' or '-' (so git refs such as
d9a06ac:papers/X.md, which name the file inside an old commit, and URLs keep their form); and the
prefixed forms ../papers/X.md, {REPO}/papers/X.md and the absolute .../conjugate-matter/papers/X.md.
Only the four files that moved: papers/knot-dark-matter-standalone.md (moved to notes/ on 2026-10-19)
is a historical path and is left alone, and so is a bare papers/ (handled by hand).
Usage: rewrite_paths.py [--dry]
"""
import re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
NAMES = r"(broken-born-checkpoint-v2|conjugate-special-relativity|phase-space-diameter|reciprocity-toy-models)\.md"
PLAIN = re.compile(r"(?<![\w.:/\-])papers/" + NAMES)
PREFIXED = re.compile(r"(\.\./|\{REPO\}/|/conjugate-matter/)papers/" + NAMES)

dry = "--dry" in sys.argv
files = subprocess.run(["git", "ls-files", "-z"], cwd=ROOT, capture_output=True, check=True).stdout.split(b"\0")
total, changed = 0, []
for name in filter(None, files):
    p = ROOT / name.decode()
    if not p.is_file() or p.suffix in {".pdf", ".png", ".jpg", ".gz"}:
        continue
    try:
        text = p.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        continue
    new, n1 = PLAIN.subn(r"wiki/papers/\1.md", text)
    new, n2 = PREFIXED.subn(r"\1wiki/papers/\2.md", new)
    if n1 + n2:
        total += n1 + n2
        changed.append((n1 + n2, name.decode()))
        if not dry:
            p.write_text(new, encoding="utf-8")
by_top = {}
for n, f in changed:
    top = f.split("/")[0] if "/" in f else f
    by_top[top] = by_top.get(top, 0) + n
print(f"{'would rewrite' if dry else 'rewrote'} {total} paths in {len(changed)} files")
for k, v in sorted(by_top.items()):
    print(f"  {k}: {v}")
