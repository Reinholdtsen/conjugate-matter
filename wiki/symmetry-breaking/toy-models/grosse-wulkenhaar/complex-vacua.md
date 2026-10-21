---
title: "Complex-model vacua and the polarization Δ(β)"
weight: 50
status: alive
description: "Condensed vacua with a free relative phase β that the duality shifts by π; the vacuum's position-versus-momentum sharpness varies as Δ(0) cos β."
provenance: [V]
sources:
  - "papers/reciprocity-toy-models.md §1"
  - "papers/reciprocity-toy-models.md §3"
  - "verify/toy_gw.py S2"
  - "verify/toy_gw.py 'S3/S5 start'"
  - "review/round4-adjudication.md 'Revisions' 3"
  - "review/round4-preregistration.md 'Predictions'"
  - "review/round4/referee/audit-notes.md Step 2(b)"
  - "notes/toy-lagrangian.md 'Chunk 2 results'"
---

*The vacua of the complex [model II](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar) are its classical lowest-action configurations at μ² = 4, λ = 1: the two lowest oscillator levels are occupied, or condensed, with fixed magnitudes, and the relative phase β between them is free. The duality shifts β by π, so it maps every vacuum to a different one and none is symmetric: classically, the vacuum breaks the exchange of position and momentum. The polarization Δ(β), the difference in spatial spread between a vacuum and its dual, varies as cos β, so the β = 0 vacuum is broader in position than in momentum and β = π is its mirror image, as a narrow pulse has a broad spectrum and the reverse. The breaking is classical only: quantization restores the symmetry.*

**Status:** Alive, classical only — [V] (criteria S1–S3 for this route, in `verify/toy_gw.py`; [the toy-model scripts](/wiki/method/verification/toy-model-scripts)) — reproduced by the round-4 referee, including the sign of Δ(0); the breaking does not survive quantization ([quantum restoration](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/quantum-restoration)).

## Key facts

- **Vacua** (μ² = 4, λ = 1). "Gradient descent from random starts always reaches a diagonal φ with |φ_mm|² = (1.5, 0.5, 0, …) and S_min = −2.5", with |φ_mm|² = q_m = max(0, −(2m+1−μ²)/(2λ)) (worklog). The referee found no lower minimum in 200 further restarts.
- **The flat angle.** "The relative phase β of φ₀₀ and φ₁₁ is free. The duality maps β → β + π, so no vacuum is invariant." The worklog: β is "a flat direction (a Goldstone mode)" ([the polarization as a Goldstone angle](/wiki/symmetry-breaking/goldstone-angle)).
- **The polarization.** "Δ(β) = ⟨x²⟩_vacuum − ⟨x²⟩_dual equals Δ(0) cos β, with Δ(0) > 0. β = 0 is broader in position than in momentum; β = π is its image." It is odd under the duality, Δ(β + π) = −Δ(β), and serves as this route's order parameter (criterion S3).

  ```text
  Δ(β) = ⟨x²⟩_vacuum − ⟨x²⟩_dual = Δ(0) cos β,    Δ(0) > 0
  ```

- **The sign, once reversed.** The worklog's first version of this line "had the sign reversed" (corrected 2026-10-19), and the round-4 pre-registration named the Δ sign convention as a likely error site. The referee confirmed the sign with an independent Fourier quadrature. The gate prints Δ(0) = 10.8828 ("quoted +10.88"); the referee's normalization gives +0.866025 (√3/2), with the same sign.
- **Novelty, as stated.** The worklog called this, "as far as the S0 search found, the first explicit statement that the self-dual Grosse–Wulkenhaar vacua break the Langmann–Szabo duality — in the complex model, not the real one." Version 2 credits the earlier study of these vacua and minima ([9], [10]) and says only that "their behaviour under the duality" had not been studied ([noncommutative field theory](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/noncommutative-field-theory)).
- **Restricted to the complex model.** Round 4 restricted the Goldstone-angle reading to the complex model (revision 3). The real model's sign-vacua are discrete and are split explicitly at one loop ([the real model's lead](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/real-model-lead)); the reason is that the duality is a symmetry only for complex fields ([complex versus real fields](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/complex-and-real-fields)).

## Sources

- `papers/reciprocity-toy-models.md` §3, §1 — the vacua, the flat angle and the polarization, quoted above; the prior work on these vacua
- `verify/toy_gw.py` S2, 'S3/S5 start' — the gated vacuum and polarization checks, including Δ(0)
- `review/round4/referee/audit-notes.md` Step 2(b) — the independent reproduction, the extra restarts and the referee's normalization of Δ(0)
- `review/round4-adjudication.md` 'Revisions' 3 — the restriction to the complex model
- `review/round4-preregistration.md` 'Predictions' — the sign convention as a predicted error site
- `notes/toy-lagrangian.md` 'Chunk 2 results' — the occupation formula, the sign correction and the novelty statement
