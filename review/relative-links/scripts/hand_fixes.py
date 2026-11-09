#!/usr/bin/env python3
"""Fixes by hand to links relink.py got wrong, found by the audits (work/papers-move/audit/). Run after relink.py --write.
Each fix replaces one exact link on one line; it fails loudly if the text is not there."""
import importlib.util
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
s = importlib.util.spec_from_file_location("cw", ROOT / "scripts" / "check-wiki.py"); cw = importlib.util.module_from_spec(s); s.loader.exec_module(cw)
gm = [a for a in cw.github_ids(ROOT / "notes/gate-mechanism.md")]
gm2 = next(a for a in gm if a.startswith("2-")); gm3 = next(a for a in gm if a.startswith("3-"))
FIXES = [
    # C24: "#11 v2.0 at commit 008c3ee, §12" cites v2.0's §12, which the current §12 no longer holds: plain text
    ("wiki/dark-matter/candidates/polarization-genesis.md", 99,
     "[§12](../../papers/broken-born-checkpoint-v2.md#12-the-dark-sector-question-three-candidates-and-the-failure-of-one-model)", "§12"),
    # C45: the s-channel bullet cites the gate-mechanism note's §2, not #1's
    ("wiki/dark-matter/conjugate-matter/gate-mechanism.md", 101,
     "[§2](../../../notes/broken-born-theory.md#2-kinematic-core)", f"[§2](../../../notes/gate-mechanism.md#{gm2})"),
    # audit A: in #11's source-list item, "§2 — negative results as the most reliable Tier-3 items" is #11 §2
    ("wiki/method/negative-results.md", 101,
     "[§2](../../notes/knot-dark-matter-standalone.md#2-the-hidden-sector-and-its-coupling)",
     "[§2](../papers/broken-born-checkpoint-v2.md#2-methodological-preface-provenance-and-verification)"),
    # audit B: "the note searched `papers/`, `notes/` and `HANDOFF.md` (§3)" is the gate-mechanism note's §3
    ("wiki/dark-matter/conjugate-matter/gate-mechanism.md", 138,
     "[§3](../../../HANDOFF.md#3-artifact-inventory-creation-order)", f"[§3](../../../notes/gate-mechanism.md#{gm3})"),
]
for path, n, old, new in FIXES:
    p = ROOT / path
    lines = p.read_text(encoding="utf-8").split("\n")
    assert lines[n - 1].count(old) == 1, (path, n, old)
    lines[n - 1] = lines[n - 1].replace(old, new)
    p.write_text("\n".join(lines), encoding="utf-8")
    print(f"{path}:{n}: {old[:40]}… -> {new[:60]}")
