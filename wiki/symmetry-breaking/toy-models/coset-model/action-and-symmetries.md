---
title: "Model I: action and symmetries"
weight: 20
status: alive
description: "The Euclidean Lagrangian with an H-contracted kinetic term for K and a compatibility potential, invariant under Sp(2, ℝ) and a separate ℤ₂ K → −K (criterion S1, verify/toy_coset.py)."
provenance: [V]
sources:
  - "papers/reciprocity-toy-models.md §1"
  - "papers/reciprocity-toy-models.md §2"
  - "verify/toy_coset.py S1"
  - "review/round4/referee/audit-notes.md Step 2(a)"
  - "notes/toy-lagrangian.md 'Chunk 1 results'"
  - "papers/broken-born-checkpoint-v2.md §4"
---

*Model I's action is the integral, over a flat two-dimensional base, of a Lagrangian with three terms: two kinetic terms, which cost action when the fields vary from point to point, and a potential that vanishes exactly when the two fields are compatible. The fields are a phase-space metric H, parametrized by a point of the upper half-plane, and a real structure K, which marks which line of the phase plane is "position". The action is unchanged by every symplectic (area-preserving) linear map of the phase plane, which includes [Born reciprocity](/wiki/phase-space/reciprocity/born-reciprocity) ρ, and by the separate flip K → −K. That invariance is criterion S1, checked symbolically, and it supplies the "genuine Noether symmetry" that [acceptance criterion 1](/wiki/symmetry-breaking/toy-models/acceptance-criterion) asks for.*

**Status:** Alive — [V] (criterion S1 in `verify/toy_coset.py`; [the toy-model scripts](/wiki/method/verification/toy-model-scripts)) — confirmed independently with sympy by the round-4 referee ("all three terms Sp(2,R)-invariant").

## Key facts

- **Setting** (version 2, §1). Phase space ℝ² with [symplectic form](/wiki/phase-space/reciprocity/symplectic-form) ω = [[0, 1], [−1, 0]]; "ρ = [[0, 1], [−1, 0]] is symplectic and squares to −1." "A real structure K with K² = 1 and Kᵀ ω K = −ω defines a neutral metric η = ωK. Its null lines are the two eigenlines L± of K, which are Lagrangian. Choosing K is choosing which line is 'position'." ([Lagrangian polarizations](/wiki/phase-space/reciprocity/lagrangian-polarizations); [Born geometry's structures](/wiki/phase-space/born-geometry/born-structures))
- **Fields** on a 1+1-dimensional base: "H, a positive symmetric symplectic matrix, H(Z) = [[Y + X²/Y, X/Y], [X/Y, 1/Y]] for Z = X + iY in the upper half-plane, with I ≡ ω⁻¹H, I² = −1"; and "K, traceless with det K = −1. Its target is the one-sheeted hyperboloid a² + bc = 1, which is two-dimensional de Sitter space." ([the Siegel domain](/wiki/phase-space/modular-field/siegel-domain); [coset and hyperbolic sigma models](/wiki/symmetry-breaking/toy-models/coset-model/sigma-models))
- **Euclidean Lagrangian**, with couplings f_H, f_K and λ:

  ```text
  L = (f_H²/8) Tr(H⁻¹∂H H⁻¹∂H) + (f_K²/4) Tr(H⁻¹ ∂Kᵀ H ∂K) + (λ/8) Tr(H⁻¹ Cᵀ H C),   with C = KI + IK
  ```

- **No ghost.** "The K kinetic term is contracted with H and is positive definite. The naive Tr(∂K ∂K) is indefinite on the hyperboloid (2 db dc at K₀ = diag(1, −1))." The round-4 referee found the H-contracted form equal to db² + dc² at H = 1, and positive on random samples.
- **The potential** "vanishes exactly when K is compatible with H." At H = 1 the gate finds |C|² = 2(b − c)², so the potential is zero exactly when K is symmetric.
- **Symmetries [V].** "Sp(2,ℝ) acts by H → SᵀHS, K → S⁻¹KS, and the action is invariant (checked for generic symplectic S, so for ρ). There is a separate ℤ₂, K → −K." The worklog: "S1 pass [V]: all three terms are invariant under a generic symplectic S (H → SᵀHS, K → S⁻¹KS), under ρ, and under K → −K." Criterion S1 asks that the action be invariant, "not merely related to its image by a unitary equivalence" ([success criteria](/wiki/symmetry-breaking/toy-models/success-criteria)).
- **Why the flip matters.** Because K → −K is also a symmetry, the twisted element ρ∘(K → −K) leaves the vacuum invariant, and "Breaking ρ is physical only once a coupling odd in K is present" ([the twisted element](/wiki/symmetry-breaking/twisted-element); [model I vacua](/wiki/symmetry-breaking/toy-models/coset-model/vacua)).
- **Notation.** These pages follow the toy-model note: K is the real structure and η = ωK, as in #11 §14 item 11. Checkpoint #11's P2′ writes the real structure as J, with η the matrix product H J; the sources do not reconcile the two conventions ([notation](/wiki/notation); [P2′](/wiki/program/postulates/p2-prime)).

## Sources

- `papers/reciprocity-toy-models.md` §1, §2 — the setting, the fields, the Lagrangian and the symmetries, quoted above
- `verify/toy_coset.py` S1 — the gated invariance and positivity checks
- `review/round4/referee/audit-notes.md` Step 2(a) — the referee's independent symbolic confirmation
- `notes/toy-lagrangian.md` 'Chunk 1 results' — the S1 pass [V] and the reason for the H-contracted kinetic term
- `papers/broken-born-checkpoint-v2.md` §4 — P2′'s J notation for the real structure
