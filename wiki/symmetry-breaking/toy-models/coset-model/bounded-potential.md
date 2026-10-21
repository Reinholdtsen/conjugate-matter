---
title: "The bounded potential V_b"
weight: 50
status: alive
description: "The normalized form −μ[Tr(K K_ref)]²/(2 Tr KᵀK) is bounded by Cauchy–Schwarz and gives a stable vacuum with H dynamical (Hessian 0, 0.764, 2, 5.236); its zero mode is not symmetry-protected."
provenance: [D, V]
sources:
  - "papers/reciprocity-toy-models.md §4"
  - "papers/reciprocity-toy-models.md §6"
  - "papers/broken-born-checkpoint-v2.md §4"
  - "papers/broken-born-checkpoint-v2.md §10"
  - "papers/broken-born-checkpoint-v2.md §14 item 11"
  - "verify/toy_coset.py"
  - "review/round4-adjudication.md 'Rulings' F2"
  - "review/round4/referee/audit-notes.md Step 3"
---

*V_b is the repaired ρ-preserving potential of [model I](/wiki/symmetry-breaking/toy-models/coset-model): the [naive potential](/wiki/symmetry-breaking/toy-models/coset-model/naive-potential) divided by a normalizing factor, 2 Tr KᵀK, which keeps it between −μ and 0 for every real structure K. Like the naive form it is unchanged by [Born reciprocity](/wiki/phase-space/reciprocity/born-reciprocity) ρ and by the flip K → −K, and it reduces the circle of real structures to the pair ±K_ref; unlike the naive form, it leaves the vacuum a stable minimum when the metric H is free to vary. The round-4 referee proposed it, version 2 of the toy-model note adopted it, and checkpoint #11 records [acceptance criterion 1](/wiki/symmetry-breaking/toy-models/acceptance-criterion) as met with it. Where such a potential comes from is not derived.*

**Status:** Alive, not derived — [D][V] (#11 §10 tags its toy-model paragraph [D][V]) — stability with H dynamical is checked in `verify/toy_coset.py` ([the toy-model scripts](/wiki/method/verification/toy-model-scripts)); upheld in [review round 4](/wiki/method/review/round-4) as "the repair". Its origin is [open](/wiki/symmetry-breaking/rho-preserving-potential).

## Key facts

- **Definition and bound.** "The normalized form V_b = −μ[Tr(K K_ref)]² / (2 Tr KᵀK) is bounded, −μ ≤ V_b ≤ 0 by Cauchy–Schwarz, since Tr K_refᵀK_ref = 2." "It is ρ- and flip-invariant."

  ```text
  V_b = −μ [Tr(K K_ref)]² / (2 Tr KᵀK),      −μ ≤ V_b ≤ 0
  ```

- **Stable with H dynamical.** "With H dynamical, (1, K_ref) is a stable minimum: Hessian eigenvalues 0, 0.764, 2, 5.236", at λ = μ = 1 in the coordinates of `verify/toy_coset.py`; the naive form has a negative eigenvalue, −6.47, at the same point ([the obituary](/wiki/symmetry-breaking/toy-models/coset-model/naive-potential)).
- **Boosts penalized.** Along the boost family on which the naive form runs away, "the boost family rises from −1 to −0.5" (adjudication).
- **Vacuum manifold.** "{diag(y, 1/y)} × {±K_ref}". At H = 1, V_b = −(μ/2)(1 + cos 2φ), against −2μ(1 + cos 2φ) for the naive form.
- **The zero mode.** "The zero mode is the classical flat line H = diag(y, 1/y), K = K_ref. It is not symmetry-protected, because V_b breaks the squeeze away from K = ±K_ref." The adjudication had called it "the residual diagonal squeeze, which is an exact symmetry"; version 2 outranks the adjudication on this point. #11 §14 item 11 ("the vacuum is stable with H dynamical") does not mention the zero mode.
- **Its origin.** The referee proposed it as a bounded variant and noted that its normalization, the Euclidean Tr KᵀK, breaks the residual boosts explicitly, so the vacuum analysis with H dynamical had to be redone; version 2 redid it (above). A derivation of the potential, "which introduces a rigid, unordered pair of axes", is not shown (version 2, §6) and is open [O] (#11 §14 item 11).
- **What rests on it.** #11 §14 item 11: criterion 1 is met "by the coset model of (H, K) with a bounded ρ-preserving potential". #11 §10: "That potential must be bounded with all fields dynamical — the round-4 review found the naive form unbounded once H moves." The [lattice simulation](/wiki/symmetry-breaking/toy-models/coset-model/monte-carlo) uses V_b at H = 1, "up to a constant and normalization". #11 P2′ names the price: "a rigid, unordered pair of axes, so more structure than ω alone, though less than a rigid η" ([P2′](/wiki/program/postulates/p2-prime)).

## Sources

- `papers/reciprocity-toy-models.md` §4, §6 — the definition, bound, Hessian, zero mode and vacuum manifold, quoted above; the underived potential listed as not shown
- `papers/broken-born-checkpoint-v2.md` §4, §10, §14 item 11 — P2′'s price, the boundedness requirement [D][V], and the criterion met with V_b
- `verify/toy_coset.py` — the gated boundedness, stability, zero-mode and boost checks
- `review/round4-adjudication.md` 'Rulings' F2 — "This is the repair"; the boost-family values; the adjudicator's reading of the zero mode
- `review/round4/referee/audit-notes.md` Step 3 — the referee's proposal and its caveat about the residual boosts
