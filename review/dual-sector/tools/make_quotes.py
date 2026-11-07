#!/usr/bin/env python3
"""Build review/dual-sector/quotes.json: every quotation from the literature that notes/dual-sector.md uses, found
again by code in its source, with an excerpt and a hash of the text it was found in.

A quoted passage (three or more words in double quotes) that occurs in a repository document other than the note and
its record is a record quotation and needs no entry. Every other passage is mapped to its source through the verified
statements of the record (review/dual-sector/panel/statements.json and missed.md, matched by text) or through LOCAL
and IMAGE below, then found again: by tools/lit.py's check in the abstract or the arXiv full text, or, for a source
lit.py cannot read, in a text extracted here from a downloaded copy (LOCAL). The handwritten Belgrade slides cannot be
read by code (IMAGE); their entries say who read them. Adapted 2026-11-06 from review/literature-check/tools/
make_quotes.py. Run from the repository root with the repo's venv; it prints the passages it could not place.
"""
import glob
import hashlib
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import lit  # noqa: E402

REPO = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
NOTE = os.path.join(REPO, "notes", "dual-sector.md")
REC = os.path.join(REPO, "review", "dual-sector")
OUT = os.path.join(REC, "quotes.json")
SCRATCH = os.path.join(REPO, "work", "dual-sector", "scratch")
PDFPY = os.path.join(REPO, "work", "dual-sector", "pdfenv", "bin", "python")
TODAY = "2026-11-06"

# Sources lit.py cannot read: (identifier, glob of the downloaded file under scratch/, how it was obtained).
LOCAL = {
    "recid:1923123": ("r8-outside*/**/*argic*.pdf", "the thesis PDF from UWSpace, downloaded by r8-outside"),
    "doi:10.55277/researchhub.unu7fof1.2": ("r8-outside*/**/*[Rr]an*.pdf", "the report PDF (v2, CC-BY) from ResearchHub"),
    "pdf:1206.4590": ("v-winn/dl/arxiv_1206.4590v1.pdf", "the arXiv PDF v1 of Winn 2012, downloaded by round 2's verifier"),
    "indico:lp2025-winn": ("v-winn/dl/summary.pdf", "the written summary (10 November 2025) of Winn's Lepton-Photon 2025 talk, from Indico"),
}
# Passages read only from slide images (handwritten): identifier and who read them.
IMAGE = {"slides:minic-belgrade-2019": "slides 5 and 6 (PDF pp. 24-25), read from the images by r1-priority, "
                                      "r1-priority-verify and the critic; the text is in capitals on the slides"}
# Passages to attribute by hand: the first words of the passage (normalized) and the source.
MANUAL = {
    "each particle of the standard model has a": "slides:minic-belgrade-2019",
    "dual particles → dual standard model": "slides:minic-belgrade-2019",
    "dark matter quanta correlated to visible": "slides:minic-belgrade-2019",
    "dark matter sensitive to": "slides:minic-belgrade-2019",
    "decreases with the velocity": "1901.00075",
    "at colliders, dark matter direct detection": "1709.04388",
    "a susy is proposed that interchanges": "1206.4590",
    "there are no electrically charged superpartners": "pdf:1206.4590",
    "the resulting strong magnetic force": "pdf:1206.4590",
    "for each sm elementary particle": "indico:lp2025-winn",
    "in this early stage simplistic description": "indico:lp2025-winn",  # also in 1601.00662; the note cites the 2017 paper's ending
    "may explain the absence of born reciprocity": "recid:1923123",
    "the group of transformations that preserves the symplectic": "1606.01829",
    "squeezes the modular cell": "1606.01829",
    "dark matter from dual-manifold coupling": "doi:10.55277/researchhub.unu7fof1.2",
}


def body_of(path):
    text = open(path, encoding="utf-8").read()
    cut = text.find("\n## References")
    return text[:cut] if cut > 0 else text


def spans_of(body):
    return [re.sub(r"\s+", " ", s).strip() for s in re.findall(r'"([^"]+)"', body, flags=re.S)
            if len(s.split()) >= 3]


def repo_texts():
    paths = (glob.glob(os.path.join(REPO, "papers", "*.md")) + glob.glob(os.path.join(REPO, "notes", "*.md"))
             + glob.glob(os.path.join(REPO, "popsci", "*.md"))
             + glob.glob(os.path.join(REPO, "review", "**", "*.md"), recursive=True)
             + [os.path.join(REPO, "HANDOFF.md"), os.path.join(REPO, "CLAUDE.md")])
    out = {}
    for p in paths:
        ap = os.path.abspath(p)
        if ap == NOTE or ap.startswith(REC + os.sep):
            continue
        out[os.path.relpath(p, REPO)] = lit.norm(re.sub(r"\*\*?", "", open(p, encoding="utf-8").read()))
    return out


def candidates(span):
    """Paper ids whose verified statements or missed passages contain the span."""
    ns, ids = lit.norm(span), []
    for s in json.load(open(os.path.join(REC, "panel", "statements.json"), encoding="utf-8")):
        if ns in lit.norm(s["quote"]) and s["paper"] not in ids:
            ids.append(s["paper"])
    for line in open(os.path.join(REC, "panel", "missed.md"), encoding="utf-8"):
        m = re.match(r'- \[[^\]]+\] (\S+) \(.*?\): "(.*)" — ', line)  # the quoted passage, not the commentary
        if m and ns in lit.norm(m.group(2)) and m.group(1) not in ids:
            ids.append(m.group(1))
    return ids


def local_text(ident):
    pattern, how = LOCAL[ident]
    files = sorted(glob.glob(os.path.join(SCRATCH, pattern), recursive=True))
    if not files:
        return None, None, how
    out = subprocess.run([PDFPY, "-I", "-c", "import pypdf,sys; r=pypdf.PdfReader(sys.argv[1]); "
                          "print('\\n'.join(p.extract_text() or '' for p in r.pages))", files[0]],
                         capture_output=True, text=True, check=True).stdout
    return files[0], out, how


def main():
    body = body_of(NOTE)
    docs = repo_texts()
    old = {e["text"]: e for e in json.load(open(OUT, encoding="utf-8"))} if os.path.exists(OUT) else {}
    out, unplaced = [], []
    for span in spans_of(body):
        ns = lit.norm(span)
        if span in old and old[span]["source"] == "image":
            out.append(old[span])
            continue
        ids = [i for i in MANUAL if ns.startswith(i)]
        ids = [MANUAL[i] for i in ids] or candidates(span)
        if not ids and any(ns in d for d in docs.values()):
            continue  # a record quotation: no paper's statement holds it, and a repository document does
        entry = None
        for ident in ids:
            if ident in IMAGE:
                entry = {"id": ident, "text": span, "source": "image", "found": IMAGE[ident], "checked": TODAY}
                break
            if ident in LOCAL:
                path, text, how = local_text(ident)
                if text and ns in lit.norm(text):
                    nt = lit.norm(text)
                    k = nt.find(ns)
                    entry = {"id": ident, "text": span, "source": "local text", "found": f"FOUND in {how}",
                             "excerpt": nt[max(0, k - 200):k + len(ns) + 200],
                             "sha256": hashlib.sha256(nt.encode()).hexdigest(), "checked": TODAY}
                    break
                continue
            verdict, where, context = lit.check_quote(ident, span)
            if not verdict.startswith("FOUND"):
                continue
            entry = {"id": ident, "text": span, "source": "abstract" if where.startswith("abstract") else "full text",
                     "found": f"{verdict} in {where}", "checked": TODAY}
            if entry["source"] == "full text":
                url, text, _ = lit.fulltext(ident if not ident.startswith(("recid:", "doi:")) else "")
                nt = lit.norm(text)
                k = nt.find(ns)
                entry["excerpt"] = nt[max(0, k - 200):k + len(ns) + 200] if k >= 0 else span
                if k < 0:
                    entry["excerpt_note"] = "found only after removing punctuation; the excerpt is the quotation"
                entry["url"], entry["sha256"] = url, hashlib.sha256(nt.encode()).hexdigest()
            else:
                entry["excerpt"] = context or span  # the abstract around the quotation (Crossref abstracts are not stored)
                if verdict == "FOUND (loose)":
                    entry["excerpt_note"] = "found in the abstract only after removing punctuation"
            break
        if entry:
            out.append(entry)
        else:
            unplaced.append((ids, span))
    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=1, ensure_ascii=False)
    print(f"{len(out)} literature quotations written to {os.path.relpath(OUT, REPO)}")
    print(f"{len(unplaced)} quoted passages placed nowhere:")
    for ids, span in unplaced:
        print(f"   {ids or '-'}: {span[:120]}")
    return 1 if unplaced else 0


if __name__ == "__main__":
    sys.exit(main())
