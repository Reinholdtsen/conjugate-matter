"""For each identifier in wiki prose: does the registered first author's surname appear in its citation segment?"""
import json, re, sys, unicodedata
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
occ = json.load(open(Path(__file__).with_name("occurrences.json")))
reg = {}
for line in (ROOT / "scripts/wiki-papers.tsv").read_text().splitlines():
    if line.startswith("#") or not line.strip(): continue
    c = line.split("\t"); reg[c[0]] = c
def fold(s): return "".join(ch for ch in unicodedata.normalize("NFKD", s) if not unicodedata.combining(ch)).lower()
def nid(raw):
    raw = re.sub(r"v\d+$", "", raw)
    if raw.lower().startswith("doi:"): return "doi:" + raw[4:].lower().rstrip(".")
    return raw
# group occurrences by (file, line) to find the previous id on the same line
bad = []
by_line = {}
for o in occ: by_line.setdefault((o["file"], o["line"]), []).append(o)
for (f, ln), items in by_line.items():
    text = (ROOT / f).read_text(encoding="utf-8").splitlines()[ln - 1]
    pos = 0; prev = None
    for o in items:
        pid = nid(o["id"]); row = reg.get(pid)
        i = text.find(o["id"], pos)
        seg = text[pos:i]
        pos = i + len(o["id"])
        if not row:
            bad.append((f, ln, pid, "UNREGISTERED", seg[-120:])); prev = None; continue
        names = row[1].split("|")
        ok = any(fold(n) in fold(seg) for n in names if n)
        if not ok and prev and reg.get(prev) and reg[prev][1] == row[1]: ok = True
        if not ok: bad.append((f, ln, pid, row[1] + " | " + row[3][:60], seg[-150:]))
        prev = pid
print(len(bad), "occurrences without the first author in their segment")
for b in bad: print(f"{b[0]}:{b[1]}  {b[2]}  [{b[3]}]\n      ...{b[4]!r}")
