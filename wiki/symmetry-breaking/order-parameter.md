---
title: "The order parameter: J, η and K"
weight: 50
status: alive
description: "Reciprocity is broken iff the vacuum carries η: J = η⁻¹H in v0.1, η = HJ in P2′, η = ωK in the toy note; the superseded ℤ₄ → ℤ₂ pattern and the unreconciled J/K notation."
provenance: [P]
sources:
  - "papers/broken-born-checkpoint-v2.md §4"
  - "papers/broken-born-checkpoint-v2.md §5"
  - "papers/broken-born-checkpoint-v2.md §13 row 9"
  - "papers/broken-born-checkpoint-v2.md §14 item 11"
  - "papers/reciprocity-toy-models.md §1"
  - "papers/reciprocity-toy-models.md §2"
  - "notes/debt1a-geometric-core.md §B"
  - "notes/broken-born-theory.md §2"
  - "notes/broken-born-theory.md 'Addendum (v0.3)'"
  - "notes/toy-lagrangian.md 'Chunk 1 results'"
  - "verify/toy_coset.py S3"
---

*An order parameter is the quantity that distinguishes a broken-symmetry state from a symmetric one, as a magnet's magnetization does: it vanishes, or is symmetric, while the symmetry is intact and takes a definite direction once the symmetry is broken. In the Broken-Born program that role belongs to the neutral metric η, the structure on phase space that marks which directions count as position and which as momentum, and reciprocity is broken exactly when the vacuum carries a definite η. The program has written this order parameter in three notations over its history, using J, η and K, and the documents do not agree on which of J and K to call the real structure. An early description of the breaking as a discrete pattern has been replaced by the Goldstone-angle picture.*

**Status:** Alive — [P] (P2′, #11 §4, where "the reading of η as the order parameter of broken reciprocity is this program's") — in the coset toy model a ρ-odd order parameter O = K₁₁ is checked [V] (`verify/toy_coset.py`, S3); the J/K naming is unresolved between #11 and the toy-model note.

## Key facts

- **Three notations.** #11 §5 defines three endomorphisms built from the structures ω, η and H ([The structures ω, η, H](/wiki/phase-space/born-geometry/born-structures)), and the documents write the order parameter, in the sense of [spontaneous symmetry breaking](/wiki/symmetry-breaking/spontaneous-symmetry-breaking), with different ones:

  ```text
  I = ω⁻¹H,   J = η⁻¹H,   K = η⁻¹ω;    I² = −1,   J² = K² = +1,   IJ = K     (#11 §5)

  J = η⁻¹H               the order parameter in the lab notebook v0.1 (#1 §2), superseded
  η = HJ                 P2′ (#11 §4) and the v0.3 addendum (#1)
  η = ωK,   K² = 1       the toy-model note §1 and #11 §14 item 11
  ```

- **The lab notebook's definition (v0.1, superseded).** "The order parameter of the theory is J = η⁻¹H — equivalently, the choice of which Lagrangian splitting H aligns with. Reciprocity is broken iff ⟨J⟩ ≠ 0 in the vacuum." (#1 §2).
- **Reciprocity moves it.** The Born rotation "preserves ω (it is symplectic), preserves H (it is orthogonal), and flips the sign of η, hence flips J and K while preserving I. [D]" (#1 §2; [Born reciprocity](/wiki/phase-space/reciprocity/born-reciprocity)).
- **The old breaking pattern (superseded).** "ρ²: (x,p) → (−x,−p) preserves all three structures. The breaking pattern is ℤ₄ → ℤ₂ [D]", with ℤ₂ = {1, ρ²} (#1 §2). It assumed the rigid η of [the original P2](/wiki/program/postulates/original-p2); #11 v2.2 replaces the discrete picture with [a Goldstone angle](/wiki/symmetry-breaking/goldstone-angle). #11's photon-dispersion row still cites ρ² ("Linear exactly zero (ρ²-protected)", §13 row 9), a rationale written out only in #1 ([Row 9](/wiki/predictions/photon-dispersion)). For ρ alone the toy's stabilizer is still {±1}: "Only {±1} leaves a vacuum fixed, so Sp(2,R) → Z₂ = {1, ρ²}" (worklog, 'Chunk 1 results').
- **The current postulate [P].** P2′: "Only ω is rigid (symplectic rigidity ≡ constancy of ℏ). The neutral metric η is emergent — the order parameter, […] with the real structure J chosen spontaneously." (#11 §4; formula above). The correction from the original P2 is forced by a [nontriviality theorem](/wiki/program/postulates/nontriviality-theorem) [D] ([P2′](/wiki/program/postulates/p2-prime)).
- **Its vacuum manifold.** Under P2′ "the vacuum spontaneously selects a real structure J (an involution anticommuting with I)", and "The space of H-compatible real structures on (ℝ^{2d}, I) is {J} ≅ U(d)/O(d) = Λ(d)"; "the earlier observation that reciprocity flips η now reads correctly as the broken symmetry moving the order parameter" (Debt-1 Chunk A §B; [The Lagrangian Grassmannian Λ(d)](/wiki/phase-space/modular-field/lagrangian-grassmannian)).
- **The toy-model form.** "A real structure K with K² = 1 and Kᵀ ω K = −ω defines a neutral metric η = ωK. Its null lines are the two eigenlines L± of K, which are Lagrangian. Choosing K is choosing which line is 'position'." (toy-model note §1; [the section condition](/wiki/symmetry-breaking/section-condition)). In model I "O = K₁₁ flips sign under ρ" (§2), and the worklog records "S3 pass [V]: O = K₁₁ is +1 in (1, K₀) and −1 in its ρ-image" ([Model I vacua](/wiki/symmetry-breaking/toy-models/coset-model/vacua); [The toy-model scripts](/wiki/method/verification/toy-model-scripts)). #11 §14 item 11: "η = ωK is the order parameter".
- **Notation, unresolved.** #11 P2′ calls J "the real structure"; #11 §5 defines both J = η⁻¹H and K = η⁻¹ω; the toy-model note and #11 §14 item 11 call K the real structure, with η = ωK; the lab notebook calls J = η⁻¹H the order parameter. No document reconciles the names. This page writes K for the real structure, as the toy-model note does, and uses J only when quoting P2′ or the notebook ([Notation](/wiki/notation); [Conflicts between sources](/wiki/history/documents/source-conflicts)).

## Sources

- `papers/broken-born-checkpoint-v2.md` §4 — P2′: η emergent as the order parameter [P]
- `papers/broken-born-checkpoint-v2.md` §5 — the definitions of I, J, K and their algebra
- `papers/broken-born-checkpoint-v2.md` §13 row 9 — the remaining reliance on ρ²
- `papers/broken-born-checkpoint-v2.md` §14 item 11 — η = ωK as the toy's order parameter
- `papers/reciprocity-toy-models.md` §1–§2 — K, η = ωK and its null lines; O = K₁₁
- `notes/debt1a-geometric-core.md` §B — the forced repair: J selected from Λ(d)
- `notes/broken-born-theory.md` §2 — v0.1: J = η⁻¹H and the ℤ₄ → ℤ₂ pattern (superseded)
- `notes/broken-born-theory.md` 'Addendum (v0.3)' — η emergent, "the order parameter itself"
- `notes/toy-lagrangian.md` 'Chunk 1 results' — S3 pass [V]; the stabilizer {±1}
- `verify/toy_coset.py` — the S3 check of O = K₁₁
