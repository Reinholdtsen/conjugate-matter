#!/usr/bin/env python3
"""Rewrite the wiki's links as paths relative to each file (wiki/CLAUDE.md, Links, from 2026-11-07).

1. Every absolute /wiki/... link becomes a relative path to the page's file (a.md or a/_index.md).
2. Every inline-code repository path that exists becomes a link to that file or folder.
3. Every section citation becomes a link to the section's heading in its document, when the document is
   certain by one of these rules, in order:
     attached      the section follows the document directly: "#11 §9", "`notes/x.md` §4", "HANDOFF §8"
     continuation  it continues such a citation: "§9 and §10", "§5, §6 and §15", "§3–§6"
     nearest       the nearest document named earlier on the same line, with no outside citation between
     sources       the only document in the page's frontmatter `sources` that lists this section
   Otherwise it stays plain text and is listed. A section the document does not have is never linked.
4. The first plain mention of an artifact number (#1 to #15) on a page links to its document.

Headings, fences, frontmatter, existing link labels and the papers in wiki/papers/ are left alone.
Usage: relink.py [--write]     (default: dry run; writes work/papers-move/relink-*.tsv either way)
"""
import csv, importlib.util, os, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
s = importlib.util.spec_from_file_location("cw", ROOT / "scripts" / "check-wiki.py")
cw = importlib.util.module_from_spec(s); s.loader.exec_module(cw)
WIKI, OUT = cw.WIKI, ROOT / "work" / "papers-move"
PRE = OUT / "pre-relink"  # the wiki as it was before the rewrite (unlink.py rebuilt it and checked it against git)
WRITE = "--write" in sys.argv

ARTIFACTS = {  # HANDOFF.md §3's numbers; the paths of the documents register (wiki/history/documents/_index.md)
    1: "notes/broken-born-theory.md", 2: "notes/stream-stability.md", 3: "notes/wave-island.md",
    4: "notes/ufd-endpoint.md", 5: "notes/geometric-core.md", 6: "notes/x-classification.md",
    7: "notes/tuning-test.md", 8: "notes/beta-coefficients.md", 9: "notes/broken-born-program-v1.md",
    10: "popsci/angle-of-the-mirror.md", 11: "wiki/papers/broken-born-checkpoint-v2.md",
    12: "popsci/universes-other-half.md", 13: "wiki/papers/conjugate-special-relativity.md",
    14: "notes/knot-dark-matter-standalone.md", 15: "review/skeptic-review-console.html",
}

# --- section labels of a document ------------------------------------------------------------------
_SECTIONS = {}
def sections(doc):
    """{label: anchor} for a Markdown document: '9' for '## 9. ...', '7.1' for '### 7.1 ...', 'A' for '## A. ...',
    'App. A' for '## Appendix A...'. A label two headings share is ambiguous and maps to None."""
    if doc in _SECTIONS:
        return _SECTIONS[doc]
    out, p = {}, ROOT / doc
    if p.suffix == ".md" and p.is_file():
        _, body, off = cw.split_frontmatter(p.read_text(encoding="utf-8"))
        clean, _ = cw.strip_code(body, off)
        heads = [m.group(2) for _, l in clean if (m := cw.HEADING_RE.match(l)) and m.group(2).strip()]
        ids = cw.github_ids(p)
        for h, a in zip(heads, ids):
            m = (re.match(r"^§?\s?(\d+(?:\.\d+)*)\.?\s", h) or re.match(r"^([A-Z])\.\s", h)
                 or re.match(r"^Appendix ([A-Z])\b", h))
            if not m:
                continue
            label = ("App. " + m.group(1)) if h.startswith("Appendix") else m.group(1)
            out[label] = None if label in out else a
    _SECTIONS[doc] = out
    return out

# --- patterns -----------------------------------------------------------------------------------------
SUFFIX = r"(?: (?:items?|rows?) \d+(?:[–-]\d+)?)?"
SEC_RE = re.compile(r"(?<!§)§\s?(\d+(?:\.\d+)*|[A-Z](?![\w]))" + SUFFIX + r"|\bApp(?:\.|endix) ([A-Z])\b" + SUFFIX)
NAMES = {  # documents the wiki names in words; each name means one document throughout the wiki
    "toy-model note": "wiki/papers/reciprocity-toy-models.md", "toy note": "wiki/papers/reciprocity-toy-models.md",
    "phase-space-diameter note": "wiki/papers/phase-space-diameter.md", "diameter note": "wiki/papers/phase-space-diameter.md",
    "closed-universe note": "notes/closed-universe.md", "velocity-gated-gravity note": "notes/velocity-gated-gravity.md",
    "gate-mechanism note": "notes/gate-mechanism.md", "literature-check note": "notes/literature-check.md",
    "dual-sector note": "notes/dual-sector.md", "lab notebook": "notes/broken-born-theory.md",
    "checkpoint": "wiki/papers/broken-born-checkpoint-v2.md",
}
NAME_ALT = "|".join(sorted(map(re.escape, NAMES), key=len, reverse=True))
DOC_RE = re.compile(r"(?<![\w&/#\[])#(1[0-5]|[1-9])(?!\d)|\bHANDOFF\b(?!\.md)|\b(" + NAME_ALT + r")\b"
                    r"|\b(note)(?=(?:'s|’s)? §)")  # "note §6": the working note the page's sources name first
LABEL_DOC_RE = re.compile(r"(?:the )?(?:#(1[0-5]|[1-9])|(" + NAME_ALT + r"))(?:'s|’s)?")


NOTE_PAPERS = ("wiki/papers/reciprocity-toy-models.md", "wiki/papers/phase-space-diameter.md")


def doc_of(m):
    """The document a DOC_RE or LABEL_DOC_RE match names."""
    if m.group(1):
        return ARTIFACTS[int(m.group(1))]
    if m.lastindex == 2:
        return NAMES[m.group(2)]
    return "HANDOFF.md"
# "§2–§6 of `notes/x.md`", "§7 of the checkpoint": the document follows the sections
OF_RE = re.compile(r"^(?:§\s?[\dA-Z.]*[\dA-Z](?:\s*(?:,|,? and|,? or|–|-|to)\s*)?)+\s+of\s+"
                   r"(?:`(?P<code>[^`]+)`|#(?P<num>1[0-5]|[1-9])(?!\d)|(?:the )?(?P<name>" + NAME_ALT + r")\b"
                   r"|(?P<ckpt>the checkpoint)\b|(?P<nb>the (?:lab )?notebook)\b|(?P<note>the note)\b|(?P<ext>\[[^\]]*\]\(https?:))")
DOC_NOUN_BEFORE_RE = re.compile(
    r"(?:\b(?:note|notes|paper|papers|notebook|worklog|manuscript|draft|adjudication|pre-?registration|report|"
    r"briefing|script|record|article|essay|book|chapter|thesis|review|version|handoff|its|their|his|her)(?:'s|’s)?"
    r"|\bv\d+(?:\.\d+)*(?:'s|’s)?),?\s*\(?\s*$", re.I)
ATTACH_RE = re.compile(r"^(?:\s|'s\s|’s\s|,\s)$")
CONT_RE = re.compile(r"^\s*(?:,|,? and|,? or|–|-|to|;)?\s*$")
# An outside work just before a section: an author–year citation, a reference number, "their"/"his"/"Eq."
EXTERNAL_BEFORE_RE = re.compile(
    r"(?:(?!(?:January|February|March|April|May|June|July|August|September|October|November|December)\b)[A-Z][\w'’\-]+(?:,? (?:et al\.|and [A-Z][\w'’\-]+))?,? (?:1[89]|20)\d\d[a-z]?|\bref\. \[\d+\]|\b(?:their|his|Eq\.)|\]\(https?://[^)\s]*\)),?\s*\(?\s*$")
AUTHOR_YEAR_RE = re.compile(r"(?!(?:January|February|March|April|May|June|July|August|September|October|November|December)\b)[A-Z][\w'’\-]+(?:,? (?:et al\.|and [A-Z][\w'’\-]+))?,? (?:1[89]|20)\d\d[a-z]?\b")


def rel(f, repo_path, anchor=""):
    target = os.path.relpath(ROOT / repo_path, f.parent)
    if (ROOT / repo_path).is_dir():
        target += "/"
    return target + (f"#{anchor}" if anchor else "")


def url_to_file(url):
    """/wiki/a/b -> wiki/a/b.md or wiki/a/b/_index.md (repo-relative), or None."""
    rest = url.strip("/")
    for cand in (f"{rest}.md", f"{rest}/_index.md"):
        if (ROOT / cand).is_file():
            return cand
    return None


def frontmatter_sources(fm):
    """{label: set(docs)} from the page's frontmatter sources ('doc §5, §6 and App. A')."""
    out = {}
    for entry in fm.get("sources", []) if isinstance(fm.get("sources"), list) else []:
        doc, _, rest = entry.partition(" ")
        for m in SEC_RE.finditer(rest):
            label = ("App. " + m.group(2)) if m.group(2) else m.group(1)
            out.setdefault(label, set()).add(doc)
    return out


links_made, unresolved, converted = [], [], {"absolute": 0, "code": 0, "artifact": 0}


def process_line(f, lineno, line, state):
    # Mask code spans (same length) so that link syntax inside code is not read as a link.
    codes = [(m.start(), m.end(), m.group(1)) for m in cw.INLINE_CODE_RE.finditer(line)]
    masked = list(line)
    for a, b, _ in codes:
        masked[a:b] = "\x00" * (b - a)
    masked = "".join(masked)
    links = [(m.start(), m.end(), m) for m in cw.LINK_FULL_RE.finditer(masked)]
    segs, pos = [], 0  # (kind, start, end, data)
    items = sorted([(a, b, "link", m) for a, b, m in links] +
                   [(a, b, "code", t) for a, b, t in codes if not any(la <= a < lb for la, lb, _ in links)])
    for a, b, kind, data in items:
        if a > pos:
            segs.append(("text", pos, a, None))
        segs.append((kind, a, b, data))
        pos = b
    if pos < len(line):
        segs.append(("text", pos, len(line), None))

    out = []
    last_doc = None          # (doc, out_len_at_end) of the nearest document named so far on this line
    last_external = -1       # output length just after the latest outside citation
    prev_sec = None          # (doc, raw text position just after it) of the previous linked section
    pending_code = None      # (out index, doc, label) of a code-path link that a section may still attach to
    groups = []              # [{"rule", "bad", "members": [(out index, plain text, links_made index)]}]
    prev_plain = None        # raw text position just after the previous section left plain

    def resolve_free(label, text_before):
        if EXTERNAL_BEFORE_RE.search(text_before):
            return None, "external"
        if DOC_NOUN_BEFORE_RE.search(text_before):
            return None, "doc-noun"
        def in_quote(s):
            s = re.sub(r"\]\([^)]*\)", "]", re.sub(r"`[^`]*`", "", s))
            return s.count('"') % 2 == 1 or s.count("“") > s.count("”")
        if in_quote(text_before):
            return None, "in-quote"
        if last_doc and in_quote(text_before[:last_doc[1]]) and not state["no_nearest"]:
            return None, "doc-in-quote"  # a document named inside a quotation is not the citing document after it
        if last_doc and not state["no_nearest"]:
            # an outside work (a URL link or an author–year citation) between the document and the section
            # may be the section's owner, so the nearest document is not used
            tail = text_before[last_doc[1]:]
            if last_external < last_doc[1] and "](http" not in tail and not AUTHOR_YEAR_RE.search(tail):
                doc = last_doc[0]
                if label in sections(doc):
                    return doc, "nearest"
        return None, "no-doc"

    def emit_section(label_text, label, doc, rule, ctx):
        anchor = sections(doc).get(label)
        if anchor is None:
            unresolved.append((f.relative_to(ROOT), lineno, label_text, doc,
                               "ambiguous-label" if label in sections(doc) else "missing-section", ctx))
            return label_text, False
        links_made.append((f.relative_to(ROOT), lineno, label_text, doc, rule, ctx))
        return f"[{label_text}]({rel(f, doc, anchor)})", True

    for kind, a, b, data in segs:
        raw = line[a:b]
        if kind == "link":
            m = data
            label, target = line[m.start(1):m.end(1)], m.group(2)
            new = target
            if target.startswith("/wiki"):
                path, _, frag = target.partition("#")
                file = url_to_file(path)
                if file:
                    new = rel(f, file, frag)
                    converted["absolute"] += 1
            if re.match(r"^https?:", target):
                last_external = len("".join(out)) + len(raw)
            out.append(raw.replace(f"]({target}", f"]({new}", 1))
            pending_code = None
            # a link labelled with a document's number or name ("[#11](...)") names that document
            lm = LABEL_DOC_RE.fullmatch(label.strip())
            nums = re.findall(r"(?<![\w&/#])#(1[0-5]|[1-9])(?!\d)", label)
            label_doc = doc_of(lm) if lm else (ARTIFACTS[int(nums[0])] if len(set(nums)) == 1 else None)
            if label_doc and (ROOT / label_doc).suffix == ".md":
                last_doc = (label_doc, len("".join(out)))
                pending_code = (None, label_doc, None)
            continue
        if kind == "code":
            code = data.strip()
            if cw.REPO_PATH_RE.match(code) and (ROOT / code).exists():
                converted["code"] += 1
                target = code.rstrip("/") + "/_index.md" if (ROOT / code).is_dir() and code.startswith("wiki/") else code
                out.append(f"[{raw}]({rel(f, target)})")
                pending_code = (len(out) - 1, code, raw)
                last_doc = (code, len("".join(out)))
            else:
                out.append(raw)
                pending_code = None
            continue
        # text: walk documents and sections in order
        i = 0
        tokens = sorted([(m.start(), "doc", m) for m in DOC_RE.finditer(raw)] +
                        [(m.start(), "sec", m) for m in SEC_RE.finditer(raw)], key=lambda t: t[0])
        consumed_to = 0
        for start, tk, m in tokens:
            if start < consumed_to:
                continue
            between = raw[consumed_to:start]
            ctx = line[max(0, a + start - 90): a + start + 60]
            if tk == "sec":
                label = ("App. " + m.group(2)) if m.group(2) else m.group(1)
                text = m.group(0)
                # attached to a code path just before this text segment
                if pending_code and pending_code[0] is None and consumed_to == 0 and ATTACH_RE.match(between) and start <= 2:
                    # after a link that names a document: link the section on its own
                    doc = pending_code[1]
                    groups.append({"rule": "attached", "bad": False, "members": []})
                    linked, ok = emit_section(text, label, doc, "attached", ctx)
                    out.append(between + linked)
                    prev_sec = (doc, a + m.end()) if ok else None
                    consumed_to = m.end()
                    pending_code = None
                    continue
                if pending_code and consumed_to == 0 and ATTACH_RE.match(between) and start <= 2:
                    idx, doc, code_raw = pending_code
                    groups.append({"rule": "attached", "bad": False, "members": []})
                    linked, ok = emit_section(f"{code_raw}{between}{text}", label, doc, "attached", ctx)
                    if ok:
                        out[idx] = linked
                        prev_sec = (doc, a + m.end())
                        consumed_to = m.end()
                        pending_code = None
                        last_doc = (doc, len("".join(out)))
                        continue
                    prev_sec = None
                    out.append(between + text)
                    consumed_to = m.end()
                    pending_code = None
                    continue
                pending_code = None
                om = OF_RE.match(line[a + start:])
                of_doc = None
                if om:
                    if om.group("code") and cw.REPO_PATH_RE.match(om.group("code")) and (ROOT / om.group("code")).is_file():
                        of_doc = om.group("code")
                    elif om.group("num"):
                        of_doc = ARTIFACTS[int(om.group("num"))]
                    elif om.group("name"):
                        of_doc = NAMES[om.group("name")]
                    elif om.group("ckpt"):
                        of_doc = ARTIFACTS[11]
                    elif om.group("nb"):
                        of_doc = ARTIFACTS[1]
                    elif om.group("note"):
                        of_doc = state["note"]
                if om and om.group("ext"):
                    doc, rule = None, "external"
                elif of_doc:
                    doc, rule = of_doc, "of"
                elif prev_sec and CONT_RE.match(line[prev_sec[1]:a + start]):
                    doc, rule = prev_sec[0], "continuation"
                elif prev_plain is not None and CONT_RE.match(line[prev_plain:a + start]):
                    doc, rule = None, "continues-plain"
                else:
                    doc, rule = resolve_free(label, "".join(out) + raw[consumed_to:start])
                out.append(between)
                if doc is None:
                    unresolved.append((f.relative_to(ROOT), lineno, text, "", rule, ctx))
                    out.append(text)
                    prev_sec = None
                    prev_plain = a + m.end()
                else:
                    n_before = len(links_made)
                    linked, ok = emit_section(text, label, doc, rule, ctx)
                    out.append(linked)
                    if rule != "continuation":
                        groups.append({"rule": rule, "bad": False, "members": []})
                    if groups:
                        g = groups[-1]
                        if ok:
                            g["members"].append((len(out) - 1, text, n_before))
                        else:
                            g["bad"] = True
                    prev_sec = (doc, a + m.end()) if ok else None
                    prev_plain = None if ok else a + m.end()
                consumed_to = m.end()
                continue
            # a document: #N, HANDOFF or a document's name, possibly with a section attached
            if m.lastindex == 3:  # "note": the page's working note, if its sources name exactly one first
                if not state["note"]:
                    continue
                doc = state["note"]
            else:
                doc = doc_of(m)
            name = m.group(0)
            after = raw[m.end():]
            sm = re.match(r"((?:'s|’s|,)?\s)(" + SEC_RE.pattern + ")", after)
            out.append(between)
            if sm and (ROOT / doc).suffix == ".md":
                s2 = SEC_RE.match(sm.group(2))
                label = ("App. " + s2.group(2)) if s2.group(2) else s2.group(1)
                text = name + sm.group(1) + sm.group(2)
                groups.append({"rule": "attached", "bad": False, "members": []})
                linked, ok = emit_section(text, label, doc, "attached", ctx)
                out.append(linked)
                if ok:
                    state["named"].add(doc)
                prev_sec = (doc, a + m.end() + sm.end()) if ok else None
                consumed_to = m.end() + sm.end()
            else:
                if m.group(1) and doc not in state["named"]:
                    out.append(f"[{name}]({rel(f, doc)})")
                    state["named"].add(doc)
                    converted["artifact"] += 1
                else:
                    out.append(name)
                prev_sec = None
                consumed_to = m.end()
            last_doc = (doc, len("".join(out)))
        rest = raw[consumed_to:]
        out.append(rest)
        if rest.strip():
            pending_code = None
    for g in groups:
        if g["bad"] and g["rule"] in ("nearest", "sources"):
            for idx, plain, k in g["members"]:
                out[idx] = plain
                row = links_made[k]
                links_made[k] = None
                unresolved.append(row[:4] + ("group-reverted",) + row[5:])
    return "".join(out)


def main():
    files = sorted(p for p in WIKI.rglob("*.md")
                   if p.name != "CLAUDE.md" and not (p.parent.name == "papers" and p.name != "_index.md"))
    changed = 0
    for f in files:
        snap = PRE / f.relative_to(ROOT)
        text = (snap if snap.exists() else f).read_text(encoding="utf-8")
        fm_lines, _, offset = cw.split_frontmatter(text)
        fm, _ = cw.parse_frontmatter(fm_lines)
        srcs = [e.split()[0] for e in fm.get("sources", []) if isinstance(fm.get("sources"), list) and e.split()]
        notes = [d for d in dict.fromkeys(srcs) if d.startswith("notes/") or d in NOTE_PAPERS]
        rel_page = f.relative_to(WIKI).as_posix()
        state = {"sources": frontmatter_sources(fm), "named": set(), "note": notes[0] if len(notes) == 1 else None,
                 # a bare section on these pages means the page's own subject document, which no rule can name
                 "no_nearest": rel_page.startswith("history/documents/") or rel_page == "references.md"}
        all_lines = text.split("\n")
        out, fence = all_lines[: offset - 1], None  # the frontmatter block, verbatim
        for k, line in enumerate(all_lines[offset - 1:]):
            m = cw.FENCE_RE.match(line)
            if m:  # fences as strip_code reads them
                marker, info = m.group(2), m.group(3).strip()
                if fence is None:
                    fence = (marker[0], len(marker))
                elif marker[0] == fence[0] and len(marker) >= fence[1] and not info:
                    fence = None
                out.append(line)
                continue
            if fence or cw.HEADING_RE.match(line):
                out.append(line)
                continue
            out.append(process_line(f, offset + k, line, state))
        new = "\n".join(out)
        if new != text:
            changed += 1
            if WRITE:
                f.write_text(new, encoding="utf-8")
    links_made[:] = [r for r in links_made if r is not None]
    for name, rows in (("relink-links.tsv", links_made), ("relink-unresolved.tsv", unresolved)):
        with open(OUT / name, "w", encoding="utf-8", newline="") as fh:
            w = csv.writer(fh, delimiter="\t")
            w.writerow(["file", "line", "label", "doc", "rule", "context"])
            w.writerows(rows)
    by_rule = {}
    for r in links_made:
        by_rule[r[4]] = by_rule.get(r[4], 0) + 1
    by_why = {}
    for r in unresolved:
        by_why[r[4]] = by_why.get(r[4], 0) + 1
    print(f"{'wrote' if WRITE else 'would change'} {changed} files; absolute links {converted['absolute']}, "
          f"code paths {converted['code']}, artifact first mentions {converted['artifact']}")
    print(f"section links {len(links_made)}: " + ", ".join(f"{k} {v}" for k, v in sorted(by_rule.items())))
    print(f"sections left plain {len(unresolved)}: " + ", ".join(f"{k} {v}" for k, v in sorted(by_why.items())))


if __name__ == "__main__":
    main()
