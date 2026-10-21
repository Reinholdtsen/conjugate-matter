---
title: "Hassan–Rosen bimetric gravity"
weight: 50
status: established
description: "Two dynamical metrics with the ghost-free potential V = 2m²M² Σ βₙ eₙ(√(g⁻¹f)) and its exchange identity Sₙ(g, f) = S₄₋ₙ(f, g)."
provenance: [T]
sources:
  - "papers/broken-born-checkpoint-v2.md §7.1"
  - "papers/broken-born-checkpoint-v2.md §7.4"
  - "papers/broken-born-checkpoint-v2.md refs [10]–[11]"
  - "review/round3/referee/audit-notes.md Step 1"
  - "notes/debt1a-iv-beta-coefficients.md §1"
  - "notes/debt1a-iii-tuning-test.md §2"
  - "notes/debt1a-iii-tuning-test.md §4"
  - "notes/knot-dark-matter-standalone.md §1"
---

*Hassan–Rosen bimetric gravity is a theory with two dynamical metrics, g and f, each with its own Einstein–Hilbert term, coupled through a potential that is free of the Boulware–Deser ghost. The potential is a sum of five terms with constant coefficients β₀ to β₄, the n-th term being the elementary symmetric polynomial eₙ of the matrix √(g⁻¹f); exchanging the two metrics reverses the order of the terms. Its spectrum contains one massless and one massive spin-2 field. The program's geometric sector lands in this theory with the second frame confined to a compact space, and [Born reciprocity](/wiki/phase-space/reciprocity/born-reciprocity) then constrains the coefficients βₙ.*

**Status:** Established — [T] — cited in the [checkpoint](/wiki/history/documents/checkpoint) as [10†, 11†], from model memory; the round-3 audit found that the two Hassan–Rosen papers support the ghost-free (bi)metric structure (`review/round3/referee/audit-notes.md` Step 1). #8 §1 writes the potential under its [D] heading.

## Key facts

- The potential, as #8 §1 writes it for the program's two frames (e, f = E₀[J]):

  ```text
  V = 2m²M² Σₙ₌₀⁴ βₙ eₙ(𝕏),    𝕏 = √(g⁻¹f)
  exchange identity:  Sₙ(g, f) = S₄₋ₙ(f, g)
  ```

  The note does not define Sₙ, m or M. The eₙ are the [elementary symmetric polynomials](/wiki/gravity/spin-2-fields/elementary-symmetric-polynomials) of the eigenvalues of 𝕏.
- References (#11): [10†] S. F. Hassan, R. A. Rosen, "Resolving the ghost problem in non-linear massive gravity," Phys. Rev. Lett. 108, 041101 (2012), arXiv:1106.3344; [11†] S. F. Hassan, R. A. Rosen, "Bimetric gravity from ghost-free massive gravity," JHEP 1202, 126 (2012), arXiv:1109.3515.
- The family is linear in the eₙ: "The Hassan–Rosen ghost-free family is *linear* combinations Σβₙeₙ(√(g⁻¹f)) (constants βₙ)" (#7 §2). A potential that is nonlinear in the eₙ therefore lies outside it, which is the second metric-tier failure ([the metric tier fails twice](/wiki/gravity/tuning-test/metric-tier-failures)).
- Spectrum [T] (#7 §4): one massless combination, the graviton, which couples to the stress of Standard Model matter, and one massive combination, which in the program is X. The theory's cosmological branches have known instabilities, which bear on X at equal Planck masses ([bimetric cosmology and its instabilities](/wiki/gravity/spin-2-fields/bimetric-cosmology)).
- The interchange-symmetric parameter choice already appears in the [partially massless](/wiki/gravity/spin-2-fields/partially-massless-gravity) bimetric literature, and at α = 1 the partially massless point lies inside the branch βₙ = β₄₋ₙ (#11 §7.4). The program derives that branch from reciprocity ([the palindrome](/wiki/gravity/palindromic-branch/palindrome)).
- The program's version (#7 §4, [D — structural]): "Hassan–Rosen bimetric gravity with the second frame constrained to a compact moduli space Λ(d)", a "predictive truncation" of bimetric theory; see [constrained bimetric gravity](/wiki/gravity/tuning-test/constrained-bimetric) and [the Lagrangian Grassmannian Λ(d)](/wiki/phase-space/modular-field/lagrangian-grassmannian).

## Used by

- [Constrained bimetric gravity](/wiki/gravity/tuning-test/constrained-bimetric) — the program's truncation of the theory.
- [The palindrome βₙ = β₄₋ₙ](/wiki/gravity/palindromic-branch/palindrome) — reciprocity acting through the exchange identity.
- [The vacuum-energy identity V(1) = 2T](/wiki/gravity/palindromic-branch/vacuum-energy-identity) — the potential evaluated at the aligned point.
- [The metric tier fails twice](/wiki/gravity/tuning-test/metric-tier-failures) — battery T7 places a metric-built potential outside the family.
- [Spectrum, parameters and reciprocity parity](/wiki/gravity/momentum-graviton/spectrum-and-parity) — the five βₙ reduced to two.

## Sources

- `papers/broken-born-checkpoint-v2.md` §7.1, §7.4, refs [10]–[11] — the consistent structure for massive spin-2; the interchange-symmetric choice in the literature; the citations, marked †.
- `review/round3/referee/audit-notes.md` Step 1 — the audit of #14's reference [3], the same two papers.
- `notes/debt1a-iv-beta-coefficients.md` §1 — the potential and its exchange identity.
- `notes/debt1a-iii-tuning-test.md` §2, §4 — linearity in the eₙ; the spectrum; the constrained picture.
- `notes/knot-dark-matter-standalone.md` §1 — the instabilities of bimetric cosmological branches and the equal-Planck-mass condition (manuscript withdrawn for unrelated arithmetic).
