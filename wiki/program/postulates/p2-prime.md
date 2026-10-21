---
title: "P2′: only the symplectic form is rigid"
weight: 40
status: alive
description: "The corrected postulate: only ω (the constancy of ℏ) is fixed and η = HJ is chosen by the vacuum; v2.2 adds that the polarization is a Goldstone angle needing a ρ-preserving potential and made physical only by a K-odd coupling."
provenance: [P]
sources:
  - "papers/broken-born-checkpoint-v2.md §4"
  - "papers/broken-born-checkpoint-v2.md §10"
  - "papers/broken-born-checkpoint-v2.md §14 item 11"
  - "notes/debt1a-geometric-core.md §B"
  - "notes/broken-born-theory.md 'Addendum (v0.3)'"
  - "papers/reciprocity-toy-models.md §1"
  - "papers/reciprocity-toy-models.md §2"
  - "papers/reciprocity-toy-models.md §4"
---

*P2′ is the program's corrected second axiom: of the structures on phase space, only the symplectic form ω is fixed in advance, and fixing it is the same as saying that Planck's constant does not change. The neutral metric η, which marks which directions count as position, is not part of the background. It is a property of the vacuum, and it serves as the order parameter of the broken symmetry: the quantity whose value tells a vacuum from its mirror image. The original P2 had fixed η as well, and the nontriviality theorem showed that this left the program with no content of its own. Checkpoint v2.2 added two qualifications from the toy models: with only ω fixed the choice of polarization is a continuous angle, so pinning it needs an additional potential, and the choice has physical consequences only once matter couples to it.*

**Status:** Alive — [P]; the correction from the original P2 is forced [D] by [the nontriviality theorem](/wiki/program/postulates/nontriviality-theorem); the v2.2 Goldstone-angle refinement is [D][V], checked by the [toy-model scripts](/wiki/method/verification/toy-model-scripts).

## Key facts

- Statement (#11 §4):

  ```text
  P2′  Only ω is rigid (symplectic rigidity ≡ constancy of ℏ). The neutral
       metric η is emergent — the order parameter, η = HJ, with the real
       structure J chosen spontaneously.                                 [P]
  ```

- The repair as first derived (#5 §B):

  ```text
  the fundamental pair is (ω, H); the derived complex structure is
  I = ω⁻¹H; the vacuum spontaneously selects a real structure J (an
  involution anticommuting with I), and η ≡ HJ.
  ```

  The possible choices form "{J} ≅ U(d)/O(d) = Λ(d), the Lagrangian Grassmannian — π₁ = ℤ, Maslov circle intact, τ restored", and "the earlier observation that reciprocity flips η now reads correctly as *the broken symmetry moving the order parameter*". See [the original P2](/wiki/program/postulates/original-p2), [the Lagrangian Grassmannian](/wiki/phase-space/modular-field/lagrangian-grassmannian) and [the order parameter](/wiki/symmetry-breaking/order-parameter).
- Precedent and credit (#11 §4): "That η should be dynamical rather than fixed was argued independently in metastring theory [26S]; the reading of η as the order parameter of broken reciprocity is this program's." See [broken Born duality](/wiki/phase-space/reciprocity/broken-born-duality).
- Refinement (#11 §4, v2.2): "with only ω rigid, ρ sits inside a continuous U(1), and the polarization is a Goldstone angle rather than a discrete choice [D][V]." See [the polarization as a Goldstone angle](/wiki/symmetry-breaking/goldstone-angle).
- "A definite polarization needs a ρ-preserving potential on that angle — a rigid, unordered pair of axes, so more structure than ω alone, though less than a rigid η" (#11 §4). No derivation of that potential exists ([the origin of the ρ-preserving potential](/wiki/symmetry-breaking/rho-preserving-potential)). In the coset toy model the naive potential is unbounded below once H is dynamical ([its obituary](/wiki/symmetry-breaking/toy-models/coset-model/naive-potential)); a normalized form is bounded and stable ([the bounded potential V_b](/wiki/symmetry-breaking/toy-models/coset-model/bounded-potential)).
- "And the breaking of ρ is physical only once matter couples to the sign of K (P4): without such a coupling, a twisted element ρ∘(K → −K) leaves the vacuum invariant" (#11 §4). See [the twisted element](/wiki/symmetry-breaking/twisted-element) and [P4](/wiki/program/postulates/p4-polarized-matter).
- Notation, unresolved between the sources: #11 §4 names J as the real structure the vacuum selects (the display above). The toy-model note and #11 §14 item 11 name K instead, with η = ωK, "K a real structure, K² = 1" (toy note abstract) and Kᵀ ω K = −ω (toy note §1). The sources do not reconcile the two names; this page quotes each in its own notation.

## Sources

- `papers/broken-born-checkpoint-v2.md` §4 — the statement, the forced correction and the v2.2 refinement; §10 and §14 item 11 — the toy-model support
- `notes/debt1a-geometric-core.md` §B — the repair as derived: the pair (ω, H), the real structure J and Λ(d)
- `notes/broken-born-theory.md` 'Addendum (v0.3)' — the axiom correction as first recorded
- `papers/reciprocity-toy-models.md` §1, §2, §4 — the real structure K, the Goldstone angle, the twisted element and the potential
