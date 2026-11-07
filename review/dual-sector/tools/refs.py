"""Print the reference list of notes/dual-sector.md from review/dual-sector/sources.json, each entry linked to the
paper (Paul, 2026-11-06), sorted by first author and year. Two entries without a metadata snapshot are added by hand
below (the talk's slides; Winn's talk, after round 2)."""
import json, re, sys, unicodedata
sys.path.insert(0, "work/dual-sector/tools")
from make_sources import initials  # noqa: E402
S = json.load(open("review/dual-sector/sources.json", encoding="utf-8"))
SPECIAL = {
    "recid:1923123": "Y. Yargic, \"Born Reciprocal Representations of the Quantum Algebra\", PhD thesis, University of Waterloo (2021; supervisor L. Smolin), [INSPIRE 1923123](https://inspirehep.net/literature/1923123)",
    "doi:10.55277/researchhub.unu7fof1.1": "S. Ran, \"Dark Matter from Dual-Manifold Coupling\", ResearchHub report (2025; posted 24 December 2025, v2 read), [doi:10.55277/researchhub.unu7fof1.1](https://doi.org/10.55277/researchhub.unu7fof1.1)",
}
HAND = [
    ("winn", "2025", "D. R. Winn, \"A Dual to Ordinary Matter Yielding Composite Flavored Scalar Dark Matter\", talk at Lepton-Photon 2025, Madison, 25 August 2025, with a written summary of 10 November 2025, [indico.cern.ch/event/1493037/contributions/6549576](https://indico.cern.ch/event/1493037/contributions/6549576)"),
    ("minic", "2019", "D. Minic, \"From string theory and quantum gravity to dark matter and dark energy\", slides of the invited talk at the 10th Mathematical Physics Meeting, Belgrade, 9 September 2019, [mphys10.ipb.ac.rs/slides/Minic.pdf](https://www.mphys10.ipb.ac.rs/slides/Minic.pdf) (handwritten; read from the images)"),
]
def fold(s): return "".join(c for c in unicodedata.normalize("NFKD", s) if not unicodedata.combining(c)).lower()
def line(k, s):
    if k in SPECIAL: return SPECIAL[k]
    names = [initials(a) for a in s["authors"]]
    who = ", ".join(names) if len(names) <= 4 else f"{names[0]} et al. ({len(names)} authors)"
    title = s["title"].rstrip(" †").replace("$H_0$", "H₀").replace(" -- ", " — ")
    j = s.get("journal") or ""
    yr = str(s.get("earliest_date") or "")[:4]
    bits = [who, f"\"{title}\"" + ("" if j else f" ({yr})")]
    if j:
        bits.append(j)
    if s.get("arxiv"):
        bits.append(f"[arXiv:{s['arxiv']}](https://arxiv.org/abs/{s['arxiv']})")
        if j and yr and f"({yr})" not in j:
            bits[-2] = f"{j}, posted {yr}"
    elif s.get("dois"):
        d = s["dois"][-1] if k.startswith("recid:") else s["dois"][0]
        bits.append(f"[doi:{d}](https://doi.org/{d})")
    elif k.startswith("recid:"):
        bits.append(f"[INSPIRE {k[6:]}](https://inspirehep.net/literature/{k[6:]})")
    return ", ".join(b for b in bits if b)
rows = []
for k, s in S.items():
    first = s["authors"][0] if s["authors"] else ""
    sur = first.split(",")[0] if "," in first else first.split()[-1]
    rows.append((fold(sur), str(s.get("earliest_date") or "")[:4], line(k, s)))
rows += HAND
for _, _, l in sorted(rows):
    print("- " + l)
