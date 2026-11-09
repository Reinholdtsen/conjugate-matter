#!/usr/bin/env python3
"""Fetch GitHub's rendered HTML for every Markdown file at HEAD (as pushed to origin/main) and record, per
file, the heading texts from the source and the anchor ids GitHub gave them, in order. Output:
work/papers-move/github-anchors.json. Used once, to verify the GitHub slug rule the gate uses offline."""
import json, re, subprocess, sys, html
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
import importlib.util
s = importlib.util.spec_from_file_location("cw", ROOT / "scripts" / "check-wiki.py"); cw = importlib.util.module_from_spec(s); s.loader.exec_module(cw)

files = [f for f in subprocess.run(["git", "ls-tree", "-r", "--name-only", "HEAD"], cwd=ROOT, capture_output=True,
         text=True, check=True).stdout.split("\n") if f.endswith(".md") and not f.startswith("site/")]

def headings(path):
    text = subprocess.run(["git", "show", f"HEAD:{path}"], cwd=ROOT, capture_output=True, text=True, check=True).stdout
    _, body, off = cw.split_frontmatter(text)
    clean, _ = cw.strip_code(body, off)
    return [m.group(2) for _, line in clean if (m := cw.HEADING_RE.match(line)) and m.group(2).strip()]

def fetch(path):
    r = subprocess.run(["gh", "api", "-H", "Accept: application/vnd.github.html", f"/repos/Reinholdtsen/conjugate-matter/contents/{path}?ref=main"],
                       capture_output=True, text=True)
    ids = re.findall(r'<a id="user-content-([^"]*)" class="anchor"', r.stdout)
    return path, [html.unescape(i) for i in ids], r.returncode

out = {}
with ThreadPoolExecutor(8) as ex:
    for path, ids, rc in ex.map(fetch, files):
        out[path] = {"headings": headings(path), "github_ids": ids, "rc": rc}
Path(ROOT / "work/papers-move/github-anchors.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
bad = [p for p, v in out.items() if v["rc"] or len(v["headings"]) != len(v["github_ids"])]
print(f"{len(out)} files, {sum(len(v['headings']) for v in out.values())} headings; files where counts differ or fetch failed: {len(bad)}")
for p in bad[:10]:
    print("  ", p, len(out[p]["headings"]), len(out[p]["github_ids"]), out[p]["rc"])
