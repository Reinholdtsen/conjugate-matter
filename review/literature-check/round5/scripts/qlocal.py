#!/usr/bin/env python3
"""qlocal.py FILE 'QUOTE' ...: check that each quote occurs in a local copy of a source (HTML: visible text and meta
contents; JSON: every string value), after lit.py's own norm() (and loose() as fallback). For sources lit.py quote
cannot reach. Run with python3 -I; lit.py is imported from the check's tools folder, the file is read as data."""
import html.parser, json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "tools"))
import lit  # noqa: E402

class T(html.parser.HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True); self.parts = []; self.skip = 0
    def handle_starttag(self, t, a):
        if t in ("script", "style"): self.skip += 1
        c = dict(a).get("content")
        if t == "meta" and c: self.parts.append(" " + c + " ")
    def handle_endtag(self, t):
        if t in ("script", "style"): self.skip = max(0, self.skip - 1)
    def handle_data(self, d):
        if not self.skip: self.parts.append(d)

def strings(o):
    if isinstance(o, dict):
        for v in o.values(): yield from strings(v)
    elif isinstance(o, list):
        for v in o: yield from strings(v)
    elif isinstance(o, str):
        yield o

path = sys.argv[1]
raw = open(path, encoding="utf-8", errors="replace").read()
if path.endswith((".json", ".body")) and raw.lstrip().startswith(("{", "[")):
    text = " \n ".join(strings(json.loads(raw)))
else:
    p = T(); p.feed(raw); text = "".join(p.parts)
nt, lt = lit.norm(text), lit.loose(text)
for q in sys.argv[2:]:
    v = "FOUND" if lit.norm(q) in nt else ("FOUND (loose)" if lit.loose(q) in lt else "NOT FOUND")
    print(f"{v}: {path.split('/round5/')[-1]} — \"{q[:90]}{'…' if len(q) > 90 else ''}\"")
