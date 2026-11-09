#!/usr/bin/env python3
"""Turn the papers' numbered bold run-in subsection titles (**7.1 The chain [D + T].** text) into
### headings followed by the paragraph, so that each subsection has an anchor on the site and on GitHub.
The words are unchanged; the title's closing period goes, as for every heading."""
import re
from pathlib import Path
LEAD = re.compile(r"^\*\*(\d+\.\d+ [^*]+?)[.:]?\*\*\s*(.*)$")
for p in sorted(Path("wiki/papers").glob("*.md")):
    lines, n = p.read_text(encoding="utf-8").split("\n"), 0
    out = []
    for line in lines:
        m = LEAD.match(line)
        if m:
            out += [f"### {m.group(1)}", "", m.group(2)] if m.group(2) else [f"### {m.group(1)}"]
            n += 1
        else:
            out.append(line)
    if n:
        p.write_text("\n".join(out), encoding="utf-8")
    print(f"{p.name}: {n}")
