#!/usr/bin/env python3
"""Invert relink.py on the wiki as it stands, giving the text before the rewrite, in work/papers-move/pre-relink/.
Links relink.py made (to repository files, section citations, artifact first mentions) become their labels;
other links go back to absolute /wiki/... form. Checked against git: for a page not edited by hand, the result
must equal HEAD's text with rewrite_paths.py's substitution applied."""
import importlib.util, os, re, subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
s = importlib.util.spec_from_file_location("cw", ROOT / "scripts" / "check-wiki.py"); cw = importlib.util.module_from_spec(s); s.loader.exec_module(cw)
s2 = importlib.util.spec_from_file_location("rp", ROOT / "work/papers-move/rewrite_paths.py")
OUT = ROOT / "work/papers-move/pre-relink"
SEC_LABEL = re.compile(r"^(?:#\d+(?:'s|’s|,)? )?(?:§|App(?:\.|endix) )|^`[^`]+`(?: (?:§|App(?:\.|endix) ).*)?$|^#\d+$")
ARTIFACT_FILES = {"wiki/papers/broken-born-checkpoint-v2.md", "wiki/papers/conjugate-special-relativity.md"}

def url_of(page):
    return cw.page_url(page)

def invert(f, text):
    fm_lines, _, offset = cw.split_frontmatter(text)
    lines = text.split("\n")
    out, fence = lines[:offset - 1], None
    for line in lines[offset - 1:]:
        m = cw.FENCE_RE.match(line)
        if m:
            marker, info = m.group(2), m.group(3).strip()
            if fence is None: fence = (marker[0], len(marker))
            elif marker[0] == fence[0] and len(marker) >= fence[1] and not info: fence = None
            out.append(line); continue
        if fence or cw.HEADING_RE.match(line):
            out.append(line); continue
        codes = [(m.start(), m.end()) for m in cw.INLINE_CODE_RE.finditer(line)]
        masked = list(line)
        for a, b in codes: masked[a:b] = "\x00" * (b - a)
        masked = "".join(masked)
        res, pos = [], 0
        for lm in cw.LINK_FULL_RE.finditer(masked):
            label, target = line[lm.start(1):lm.end(1)], lm.group(2)
            res.append(line[pos:lm.start()]); pos = lm.end()
            kind, path, anchor = cw.resolve(f, target)
            whole = line[lm.start():lm.end()]
            if kind == "external" or kind == "bad":
                res.append(whole); continue
            paper = kind == "page" and path.parent.name == "papers" and path.name != "_index.md"
            if kind == "repo" or (paper and (anchor or re.fullmatch(r"#\d+", label) or "§" in label)) \
               or (kind == "page" and re.fullmatch(r"`[^`]+`(?: .*)?", label)):
                res.append(label); continue
            url = url_of(path) + (f"#{anchor}" if anchor else "")
            if target.startswith("#"):
                url = target
            res.append(whole.replace(f"]({target}", f"]({url}", 1))
        res.append(line[pos:])
        out.append("".join(res))
    return "\n".join(out)

PLAIN = re.compile(r"(?<![\w.:/\-])papers/(broken-born-checkpoint-v2|conjugate-special-relativity|phase-space-diameter|reciprocity-toy-models)\.md")
PREF = re.compile(r"(\.\./|\{REPO\}/|/conjugate-matter/)papers/(broken-born-checkpoint-v2|conjugate-special-relativity|phase-space-diameter|reciprocity-toy-models)\.md")
def head_rewritten(rel):
    r = subprocess.run(["git", "show", f"HEAD:{rel}"], cwd=ROOT, capture_output=True, text=True)
    if r.returncode: return None
    t = PLAIN.sub(r"wiki/papers/\1.md", r.stdout)
    return PREF.sub(r"\1wiki/papers/\2.md", t)

same = differ = new = 0; diffs = []
for f in sorted(p for p in cw.WIKI.rglob("*.md") if p.name != "CLAUDE.md" and not (p.parent.name == "papers" and p.name != "_index.md")):
    rel = f.relative_to(ROOT).as_posix()
    pre = invert(f, f.read_text(encoding="utf-8"))
    dest = OUT / rel; dest.parent.mkdir(parents=True, exist_ok=True); dest.write_text(pre, encoding="utf-8")
    h = head_rewritten(rel)
    if h is None: new += 1
    elif h == pre: same += 1
    else: differ += 1; diffs.append(rel)
print(f"identical to HEAD with paths rewritten: {same}; differ: {differ}; not in HEAD: {new}")
for d in diffs: print("  ", d)
