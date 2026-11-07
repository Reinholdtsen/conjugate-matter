"""One-off: turn every unlinked paper identifier in wiki prose into a link to the paper (Paul, 2026-11-06:
"whenever referenced include a link to the paper itself if possible"). Frontmatter, fenced code, inline code
and existing links are left alone. Prints each change; --dry-run writes nothing."""
import importlib.util, re, sys, urllib.parse
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
spec = importlib.util.spec_from_file_location("cw", ROOT / "scripts" / "check-wiki.py")
cw = importlib.util.module_from_spec(spec); spec.loader.exec_module(cw)
dry = "--dry-run" in sys.argv

def url_for(m):
    if m.group(1) or m.group(4):
        version = re.search(r"v\d+$", m.group(0))
        return "https://arxiv.org/abs/" + (m.group(1) or m.group(4)) + (version.group(0) if version else "")
    if m.group(2):
        return "https://doi.org/" + urllib.parse.quote(m.group(2), safe="/:;.-_")
    return "https://hdl.handle.net/" + m.group(3)

total = 0
for f in sorted((ROOT / "wiki").rglob("*.md")):
    if f.name == "CLAUDE.md":
        continue
    raw = f.read_text(encoding="utf-8")
    lines = raw.split("\n")
    fm, body, off = cw.split_frontmatter(raw)
    clean, _ = cw.strip_code(body, off)
    changed = 0
    for lineno, line in clean:
        blank = cw.INLINE_CODE_RE.sub(lambda c: " " * len(c.group(0)), line)
        spans = [(lm.start(), lm.end()) for lm in cw.LINK_FULL_RE.finditer(blank)]
        hits = [m for m in cw.PAPER_ID_RE.finditer(blank) if not any(a <= m.start() < b for a, b in spans)]
        if not hits:
            continue
        if cw.HEADING_RE.match(line):
            print(f"SKIP heading {f.relative_to(ROOT)}:{lineno}")
            continue
        new = line
        for m in reversed(hits):  # right to left, so earlier offsets stay valid
            text = line[m.start():m.end()]
            new = new[:m.start()] + f"[{text}]({url_for(m)})" + new[m.end():]
        assert lines[lineno - 1] == line
        lines[lineno - 1] = new
        changed += len(hits)
    if changed:
        total += changed
        print(f"{f.relative_to(ROOT)}: {changed}")
        if not dry:
            f.write_text("\n".join(lines), encoding="utf-8")
print("total", total, "(dry run)" if dry else "")
