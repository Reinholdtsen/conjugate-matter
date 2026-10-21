---
title: "Model II: the matrix base and the action"
weight: 20
status: alive
description: "The matrix base f_mn of the Moyal plane with its anchors, the diagonal Ω = 1 kinetic form 8π(m + n + 1)|φ_mn|² computed with exact derivatives, and the action for complex and real fields."
provenance: [V]
sources:
  - "papers/reciprocity-toy-models.md §3"
  - "verify/toy_gw.py (anchors, kinetic form)"
  - "review/round4/referee/audit-notes.md Step 2(b)"
  - "notes/toy-lagrangian.md 'Chunk 2 results'"
---

*The matrix base is a set of functions f_mn on the noncommutative plane, built from harmonic-oscillator states, in which the star product of two functions becomes a product of matrices. Writing the field as a combination of these functions turns [model II](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar) into a matrix model: at Ω = 1 the kinetic term is diagonal, 8π(m + n + 1)|φ_mn|², and the interaction is the trace of a fourth power of the matrix. Every formula was checked against independent anchors before use, and the diagonal kinetic form was computed with exact derivatives after a check with finite differences failed. This page is the set-up on which the lemma, the vacua and the restoration argument of model II are computed.*

**Status:** Alive as a toy — [V] (the matrix-base anchors and the kinetic form in `verify/toy_gw.py`; [the toy-model scripts](/wiki/method/verification/toy-model-scripts)) — reproduced by the round-4 referee with an independent construction; the route as a whole fails criterion S4 ([quantum restoration](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/quantum-restoration)).

## Key facts

- **Matrix base** of the Moyal plane [x₁, x₂] = iθ (θ = 1), "as in [9, App. A]" ([noncommutative field theory](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/noncommutative-field-theory)):

  ```text
  f₀₀ = 2e^{−x²/θ},   f_mn = (m! n! θ^{m+n})^{−1/2} ā^{⋆m} ⋆ f₀₀ ⋆ a^{⋆n}
  f_mn ⋆ f_kl = δ_nk f_ml,   H ⋆ f_mn = θ(m + ½) f_mn,   f_mn ⋆ H = θ(n + ½) f_mn,   H = ½x²
  ```

  Here H is the oscillator function ½x², not model I's phase-space metric.
- **Anchors.** "The explicit Laguerre form … is checked exactly against the H-eigen-relations, and numerically for orthogonality and ∫ f_mn = 2πθ δ_mn." The referee also matched the Laguerre form to the Weyl symbol of |m⟩⟨n| built independently from Hermite functions, with a maximum error of 5.63e-14 for m, n ≤ 3 ([the Wigner function and Weyl symbols](/wiki/phase-space/reciprocity/wigner-function)).
- **Kinetic form [V].** "The Ω = 1 quadratic form ∫ |∂φ|² + x̃²|φ|² equals 8π(m + n + 1)|φ_mn|², diagonal, computed with exact derivatives." The worklog: "A first check used finite-difference derivatives and failed at the 0.3% level. The fix was exact derivatives, not a looser tolerance." The gate prints the ratio "25.1327 (8 pi = 25.1327)".
- **Action, complex fields.** "In units where the kinetic coefficient is 1, S[φ] = Σ_mn (m + n + 1 − μ²)|φ_mn|² + λ Tr((φ†φ)²)." Here † is the Hermitian adjoint, not the citation mark.
- **Action, real fields.** The field is real in position, so its matrix φ is Hermitian (f_mn† = f_nm) and the quartic term is Tr φ⁴. Because "Πφ is not Hermitian", the duality "maps the real field space out of itself", and the real action is only covariant ([complex versus real fields](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/complex-and-real-fields)).
- **The duality's normalization.** Version 2 uses "the two-dimensional form of [6, eq. 1] — p = x̃ = 2θ⁻¹x and normalization π√|det θ|"; the gate's anchor is that the duality leaves f₀₀ unchanged, "D f_00 = f_00 (the normalization pi sqrt|det theta|)" ([the duality on the matrix base](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/matrix-base-lemma)).
- **Where the inputs come from.** "Inputs come from the sources: the matrix base from de Goursac–Tanasa–Wallet App. A; the duality from Grosse–Wulkenhaar hep-th/0402093 eq. 1" (worklog, chunk 2), not from memory.

## Sources

- `papers/reciprocity-toy-models.md` §3 — the matrix base, its anchors, the kinetic form and the action, quoted above
- `verify/toy_gw.py` — the gated anchors, the kinetic-form check and the normalization anchor
- `review/round4/referee/audit-notes.md` Step 2(b) — the referee's independent construction and its measured deviations
- `notes/toy-lagrangian.md` 'Chunk 2 results' — the sources of the inputs and the finite-difference episode
