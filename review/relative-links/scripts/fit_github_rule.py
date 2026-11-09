import json, re, unicodedata, importlib.util
from pathlib import Path
s = importlib.util.spec_from_file_location("cw", "scripts/check-wiki.py"); cw = importlib.util.module_from_spec(s); s.loader.exec_module(cw)
data = json.loads(Path("work/papers-move/github-anchors.json").read_text(encoding="utf-8"))

def gh_slug(text):
    t = re.sub(r"`([^`]*)`", r"\1", text)          # code spans keep their text
    t = re.sub(r"\\([!-/:-@\[-`{-~])", r"\1", t)     # backslash escapes
    t = t.lower()
    keep = lambda c: c in " -" or unicodedata.category(c)[0] in "LM" or unicodedata.category(c) in ("Nd", "Pc")
    return "".join(c for c in t if keep(c)).replace(" ", "-")

def ids(texts, f):
    used, out = {}, []
    for t in texts:
        base = f(t)
        n = used.get(base, 0)
        out.append(base if n == 0 else f"{base}-{n}")
        used[base] = n + 1
    return out

ok = bad = hugo_diff = 0; bads = []; diffs = []
for path, v in data.items():
    if len(v["headings"]) != len(v["github_ids"]): continue
    mine = ids(v["headings"], gh_slug)
    for h, m, g in zip(v["headings"], mine, v["github_ids"]):
        if m == g: ok += 1
        else: bad += 1; bads.append((path, h[:60], m[:50], g[:50]))
    if path.startswith("wiki/") or path.startswith("papers/"):
        used = set()
        for h, g in zip(v["headings"], v["github_ids"]):
            sl = cw.slugify(h)
            hid = "" if sl is None else cw.heading_id(sl, used)
            if hid != g: hugo_diff += 1; diffs.append((path, h[:60], hid[:50], g[:50]))
print(f"GitHub rule: {ok} match, {bad} differ")
for b in bads[:12]: print("  ", b)
print(f"wiki and papers: Hugo id (check-wiki) differs from GitHub's on {hugo_diff} headings")
for d in diffs[:12]: print("  ", d)
