"""Check that the wiki differs from the pre-task snapshot only by the links in author-year-links.tsv; with
--restore, put the listed pages back to the snapshot (only if the check passes)."""
import csv, shutil, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
snap = HERE / "snapshot" / "wiki-before-authoryear"
rows = list(csv.DictReader(open(HERE / "author-year-links.tsv", encoding="utf-8"), delimiter="\t"))
by = {}
for r in rows:
    by.setdefault(r["file"], []).append(r)
bad = 0
for f, rs in by.items():
    old = (snap / f[len("wiki/"):]).read_text(encoding="utf-8").split("\n")
    new = (ROOT / f).read_text(encoding="utf-8").split("\n")
    if len(old) != len(new):
        print("line count differs", f); bad += 1; continue
    lines = {int(r["line"]) for r in rs}
    for i, (a, b) in enumerate(zip(old, new), start=1):
        if a == b:
            continue
        if i not in lines:
            print("UNEXPECTED change", f, i); bad += 1; continue
        restored = b
        for r in (r for r in rs if int(r["line"]) == i):
            link = f"[{r['label']}]({r['url']})"
            if link not in restored:
                print("missing link", f, i, link); bad += 1; continue
            restored = restored.replace(link, r["label"], 1)
        if restored != a:
            print("MISMATCH", f, i); bad += 1
for p in snap.rglob("*"):
    if p.is_file():
        rel = "wiki/" + p.relative_to(snap).as_posix()
        if rel not in by and p.read_bytes() != (ROOT / rel).read_bytes():
            print("page changed but not listed", rel); bad += 1
extra = {p.relative_to(ROOT / "wiki").as_posix() for p in (ROOT / "wiki").rglob("*") if p.is_file()} - \
        {p.relative_to(snap).as_posix() for p in snap.rglob("*") if p.is_file()}
for e in sorted(extra):
    print("new file since snapshot", e); bad += 1
print(f"{len(rows)} links on {len(by)} pages; problems: {bad}")
if "--restore" in sys.argv and not bad:
    for f in by:
        shutil.copyfile(snap / f[len("wiki/"):], ROOT / f)
    print("restored", len(by), "pages")
sys.exit(1 if bad else 0)
