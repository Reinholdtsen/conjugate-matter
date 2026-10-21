---
title: "Spectrum, parameters and reciprocity parity"
weight: 80
status: alive
description: "Five βₙ reduce to two (the Fierz–Pauli mass and one cubic shape); the massless graviton is the reciprocity-even combination and X the odd one, with equal Planck masses forced and reciprocity a vertex selection rule."
provenance: [D]
sources:
  - "notes/debt1a-iv-beta-coefficients.md §3"
  - "notes/debt1a-iv-beta-coefficients.md §1"
  - "papers/broken-born-checkpoint-v2.md §7.5"
  - "papers/broken-born-checkpoint-v2.md §13"
  - "notes/debt1a-iii-tuning-test.md §4"
  - "notes/broken-born-program-v1.md §5"
---

*This page covers what is left of the momentum graviton's potential once reciprocity has acted on it, and how the two spin-2 fields sort under reciprocity. The [Hassan–Rosen potential](/wiki/gravity/spin-2-fields/hassan-rosen-bimetric) has five coefficients βₙ; the [palindrome](/wiki/gravity/palindromic-branch/palindrome) removes two and the flat-vacuum condition removes one, leaving two numbers: the combination that sets X's mass M_X, and one parameter that shapes its cubic self-interactions. Of the two spin-2 combinations, the one that reciprocity leaves unchanged is the ordinary graviton and is exactly massless, while X changes sign under reciprocity and is massive; the same symmetry forces the two frames to have equal Planck masses. These are derived results [D] in [checkpoint #11](/wiki/history/documents/checkpoint) §7.5, not machine-checked, and the masslessness of the even combination is prediction row 6.*

**Status:** Alive — [D] in #11 §7.5; [D + T] in calc note #8 (`notes/debt1a-iv-beta-coefficients.md` §3) — derivations only: no battery test covers the parameter count or m_FP². Tested observationally by [Row 6: the exactly massless graviton](/wiki/predictions/massless-graviton).

## Key facts

- The parameter count, from calc note #8 §3 [D + T] (see [The Debt-1 calc notes](/wiki/history/documents/debt-1-notes)): "five βₙ → palindrome (−2) → T = 0 (−1) → two: the Fierz–Pauli mass combination m_FP² ∝ β₁ + 2β₂ + β₃ = 2(β₁+β₂), i.e. M_X, and one orthogonal shape parameter controlling cubic interactions." The condition T = 0 comes from [the vacuum-energy identity](/wiki/gravity/palindromic-branch/vacuum-energy-identity).
- #11 §7.5 [D]: "Five βₙ → two parameters (M_X ∝ 2(β₁+β₂); one cubic shape)." No source fixes a value of M_X.
- Parity (#8 §3): "the massless graviton is the reciprocity-even combination (e + f); X is reciprocity-odd (e − f). Reciprocity is a selection rule on vertices." Here e and f = E₀[J] are the two frames of the wedge potential (#8 §1; [The frame tier](/wiki/gravity/tuning-test/frame-tier)).
- Planck masses (#8 §3): "With equal effective Planck masses (forced by the same symmetry), SM matter — coupled to g — sees both eigenstates with comparable strength". What this means for Standard Model matter is [Safety by range: X and ordinary matter](/wiki/gravity/momentum-graviton/fifth-force-safety); what it means for cosmological stability is [Open: stability at equal Planck masses](/wiki/gravity/momentum-graviton/equal-planck-mass-stability).
- Graviton-mass bounds from gravitational waves: #11 §7.5 states "Massless graviton = reciprocity-even" with those bounds "satisfied identically", and #8 §3 says they "apply to the even eigenstate, which is exactly massless". Calc note #7 §4 had instead treated the bound, "m_g ≲ 10⁻²³ eV territory", as a check on a mixing angle; #8 and #11 supersede that reading.
- Row 6 of #11 §13: standard expectation "m_g = 0"; Broken-Born requirement "Massless eigenstate exactly massless (reciprocity-even)"; killed by "Nonzero mass attributed to the even eigenstate".
- The two-parameter count quantifies the "predictive truncation" of [constrained bimetric gravity](/wiki/gravity/tuning-test/constrained-bimetric): in #8 §3's words, the five-function freedom of Hassan–Rosen bimetric gravity "collapses to two numbers".

## Sources

- `notes/debt1a-iv-beta-coefficients.md` §3 — the count, the parities and the Planck masses [D + T]; §1 for the frames e and f
- `papers/broken-born-checkpoint-v2.md` §7.5 — the current statement [D]; §13 row 6 for the test
- `notes/debt1a-iii-tuning-test.md` §4 — the earlier mixing-angle reading of the graviton-mass bound
- `notes/broken-born-program-v1.md` §5 — the superseded v1 statement
