---
title: "The duality on the matrix base"
weight: 30
status: alive
description: "By direct numerical Fourier integration the duality is left multiplication by parity, D f_mn = (−1)^m f_mn, recorded as a lemma crediting Grosse–Wulkenhaar, Royer and Langmann–Szabo."
provenance: [V]
sources:
  - "papers/reciprocity-toy-models.md §3 'Lemma'"
  - "verify/toy_gw.py"
  - "review/round4-adjudication.md 'Revisions' 3"
  - "review/round4/referee/audit-notes.md Step 2(b)"
  - "review/round4/referee/audit-notes.md Step 3"
  - "notes/toy-lagrangian.md 'Chunk 1 results'"
  - "notes/toy-lagrangian.md 'Chunk 2 results'"
---

*The lemma states how the Langmann–Szabo duality, a Fourier transform that exchanges position and momentum, acts on the matrix-base functions f_mn of [model II](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar): it multiplies each one by (−1)^m, a sign set by its left index alone. In matrix language the duality is left multiplication by the parity operator, and because Grosse and Wulkenhaar alternate the sign of the Fourier exponent from one factor to the next, parity acts on the left index of one factor and on the right index of the next. The result was obtained by direct numerical Fourier integration, which settled a clash between recalled conventions. Round 4 judged it correct but not new, and asked that it be presented as a lemma with credit to the work it follows from.*

**Status:** Alive — [V] (`verify/toy_gw.py`, "D f_mn = (-1)^m f_mn for all m, n < 4"; [the toy-model scripts](/wiki/method/verification/toy-model-scripts)) — confirmed by the round-4 referee for θ = 1, 1/2 and 3, who called it "Correct, but not a new structural fact".

## Key facts

- **Statement.** "D f_mn = (−1)^m f_mn for m, n < 4, to ≲ 10⁻¹¹. The opposite sign of the exponent gives (−1)^n." The gate prints a maximum deviation of 1.4e-12 and asserts a tolerance of 1e-7.
- **The map.** With "p = x̃ = 2θ⁻¹x and normalization π√|det θ|", the note implements "D f(x) = (πθ)⁻¹ ∫ d²y e^{−i x̃·y} f(y) by direct numerical integration" ([the Fourier transform as a phase-space rotation](/wiki/phase-space/reciprocity/fourier-transform)).

  ```text
  D f(x) = (πθ)⁻¹ ∫ d²y e^{−i x̃·y} f(y),    x̃ = 2θ⁻¹x
  D f_mn = (−1)^m f_mn
  ```

- **Parity.** "It is left multiplication by parity, Π = e^{−iπN}" (worklog). "The duality is therefore parity acting on the left index for one factor and on the right for the next. That is the alternation of [6], and is consistent with the parity-operator form of Weyl symbols [16]." ([the Wigner function and Weyl symbols](/wiki/phase-space/reciprocity/wigner-function))
- **Credit.** "Grosse and Wulkenhaar already note that the duality is manifest in the matrix base [6b]; we record the explicit form because the rest of the analysis turns on it." Revision 3 asked to "Present the matrix-base duality as a lemma, crediting Grosse–Wulkenhaar (manifest in the matrix base), Royer (the parity form) and Langmann–Szabo (the complex formulation)."
- **The clash it settled.** In chunk 1 the recalled Fourier eigenvalues, "(−i)^{m+n}, or (−1)^m with the B rotation", could not make the quartic term invariant, "which contradicts Grosse–Wulkenhaar's stated invariance. So a recalled convention is wrong somewhere." Chunk 2 computed the map instead: "a direct numerical 2D Fourier integral with Grosse–Wulkenhaar's kernel, not a recalled eigenvalue."
- **What turns on it.** Because the duality acts as parity, it shifts the relative phase of the complex-model vacua by π, so that no vacuum is invariant once level 1 condenses ([complex-model vacua](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/complex-vacua)); and it makes Πφ non-Hermitian for a real field, so the real model is only covariant ([complex versus real fields](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/complex-and-real-fields)).

## Sources

- `papers/reciprocity-toy-models.md` §3 'Lemma' — the statement, the map, the parity reading and the credit, quoted above
- `verify/toy_gw.py` — the gated lemma check, its tolerance and the normalization anchor
- `review/round4-adjudication.md` 'Revisions' 3 — the required lemma form and credits
- `review/round4/referee/audit-notes.md` Step 2(b), Step 3 — the referee's exact confirmation at three values of θ and the novelty judgement
- `notes/toy-lagrangian.md` 'Chunk 1 results', 'Chunk 2 results' — the convention clash and its resolution [V]
