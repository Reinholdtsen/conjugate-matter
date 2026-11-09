#!/usr/bin/env python3
"""Give each paper in wiki/papers/ Hugo frontmatter: its # H1 becomes the title (the site's layout renders
the title as the page's one h1), plus weight, status record and a description. Also escape the asterisk of
a starred symbol (v* -> v\\*) outside code, as scripts/check-wiki.py's `star` check asks; the rendered text
is unchanged. Idempotent: a file that already has frontmatter is skipped."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PAPERS = {
    "broken-born-checkpoint-v2.md": (10,
        "Checkpoint #11, the current reference for the full program: postulates, the compatibility theorem and the "
        "modular field, the massive momentum graviton, conjugate matter and the gate, momentum clumping, cosmology, "
        "charge lattices, the three dark-matter candidates, predictions, open problems and the founding suppositions."),
    "reciprocity-toy-models.md": (20,
        "The toy-model note: a coset sigma model and the self-dual Grosse–Wulkenhaar model, two explicit models in "
        "which Born reciprocity is spontaneously broken, written in blind-review format and graded B in review round 4."),
    "phase-space-diameter.md": (30,
        "The phase-space-diameter note: the size of the universe in position and in momentum, what Born reciprocity "
        "adds, and a self-dual length; graded B in review round 5."),
    "conjugate-special-relativity.md": (40,
        "Paper #13: the kinematics of the momentum polarization, with a second light cone, force boosts, force "
        "dilation, the mass and length shells and a maximum force; never blind-reviewed."),
}
STARRED = re.compile(r"(?<![\\*\w])([A-Za-zα-ωΑ-Ω])\*(?!\*)")
CODE = re.compile(r"(`[^`]*`)")

for name, (weight, desc) in PAPERS.items():
    p = ROOT / "wiki" / "papers" / name
    text = p.read_text(encoding="utf-8")
    if text.startswith("---\n"):
        print(f"{name}: has frontmatter, skipped")
        continue
    first, _, rest = text.partition("\n")
    assert first.startswith("# "), (name, first)
    title = first[2:].strip()
    out, fenced, stars = [], False, 0
    for line in rest.split("\n"):
        if re.match(r"^\s*(```|~~~)", line):
            fenced = not fenced
        if not fenced:
            parts = CODE.split(line)
            for i in range(0, len(parts), 2):
                parts[i], n = STARRED.subn(r"\1\\*", parts[i])
                stars += n
            line = "".join(parts)
        out.append(line)
    fm = (f'---\ntitle: "{title}"\nweight: {weight}\nstatus: record\ndescription: "{desc}"\n---\n\n')
    p.write_text(fm + "\n".join(out), encoding="utf-8")
    print(f"{name}: title {title!r}, weight {weight}, {stars} starred symbols escaped")
