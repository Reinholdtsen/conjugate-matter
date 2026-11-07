"""Survey paper identifiers in wiki prose: where they sit (code span, link, heading, frontmatter, prose)."""
import re, sys, json, collections
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "scripts"))
import importlib.util
spec = importlib.util.spec_from_file_location("cw", ROOT / "scripts" / "check-wiki.py")
cw = importlib.util.module_from_spec(spec); spec.loader.exec_module(cw)
ID_RE = re.compile(r"\b(arXiv:(?:[a-z\-]+(?:\.[A-Z]{2})?/\d{7}|\d{4}\.\d{4,5}))(v\d+)?|\b(doi:10\.\d{4,9}/[^\s,;)\]]+)", re.I)
where = collections.Counter(); occ = []
for f in sorted((ROOT / "wiki").rglob("*.md")):
    if f.name == "CLAUDE.md": continue
    fm, body, off = cw.split_frontmatter(f.read_text(encoding="utf-8"))
    clean, _ = cw.strip_code(body, off)
    for lineno, line in clean:
        spans = [(m.start(), m.end()) for m in cw.INLINE_CODE_RE.finditer(line)]
        links = [(m.start(), m.end()) for m in cw.LINK_RE.finditer(line)]
        heading = bool(cw.HEADING_RE.match(line))
        for m in ID_RE.finditer(line):
            s = m.start()
            kind = ("code" if any(a <= s < b for a, b in spans) else
                    "link" if any(a <= s < b for a, b in links) else
                    "heading" if heading else "prose")
            where[kind] += 1
            occ.append({"file": str(f.relative_to(ROOT)), "line": lineno, "id": (m.group(1) or m.group(3)), "kind": kind,
                        "before": line[max(0, s - 160):s]})
print(dict(where))
ids = collections.Counter(o["id"] for o in occ if o["kind"] == "prose")
print("distinct prose ids:", len(ids))
json.dump(occ, open(Path(__file__).with_name("occurrences.json"), "w"), indent=1, ensure_ascii=False)
for o in occ:
    if o["kind"] != "prose": print(o["kind"], o["file"], o["line"], o["id"])
