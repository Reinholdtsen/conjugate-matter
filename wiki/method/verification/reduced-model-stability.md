---
title: "The reduced-model stability rule"
weight: 40
status: method
description: "When numerics run on a model with fields frozen, check the full model's boundedness and Hessian with all fields dynamical, and say in the text that it is a reduction — round 4's first lesson."
sources:
  - "CLAUDE.md 'Method'"
  - "review/round4-adjudication.md 'Lessons (into CLAUDE.md)'"
  - "review/round4-adjudication.md 'Rulings'"
  - "papers/reciprocity-toy-models.md §4"
  - "papers/reciprocity-toy-models.md §6"
  - "papers/broken-born-checkpoint-v2.md §14 item 11"
  - "verify/toy_coset.py"
  - "verify/toy_s4.py"
---

*The reduced-model stability rule says that when a calculation simplifies a model by holding some of its fields fixed, the full model's stability must still be checked with every field free to move, and the text must say that the calculation used a reduction. Review round 4 supplied the reason: the potential used in the first toy model was bounded below while the phase-space metric H was held fixed, and unbounded below once H was allowed to vary, so the model's claimed vacuum was a saddle. The repaired potential was checked with all fields dynamical, and the toy-model note now names its lattice simulation as a frozen-H reduction.*

**Status:** Method, in force (a round-4 lesson, now in root `CLAUDE.md`) — untagged — applied in `verify/toy_coset.py`, which checks the bounded potential with H dynamical, and stated in `verify/toy_s4.py` and the toy-model note §4.

## Key facts

- **The rule.** "When numerics run on a reduced model (fields frozen), check the unreduced model's stability — boundedness, and the Hessian with all fields dynamical — and say in the text that it is a reduction. Round 4 found a potential that was bounded only at frozen H." (root `CLAUDE.md`). Round-4 lesson 1 states the same, ending "and state the reduction in the text."
- **The failure (F1).** "The §4 potential −μ[Tr(K K_ref)]² is unbounded below in model I" — upheld: "along H = SᵀS, K = S⁻¹K₀S (S a boost), the λ-term is ~0 while V_μ = −4, −56.6, −2983, −8.9×10⁶ at t = 0, 1, 2, 4." See [Obituary: the naive ρ-preserving potential](/wiki/symmetry-breaking/toy-models/coset-model/naive-potential).
- **The consequence (F2).** "So (1, K_ref) is a saddle, and the Monte Carlo simulates a frozen-H reduction, not model I" — upheld, with a negative Hessian eigenvalue "at λ = 1, 10, 100 (−6.47, −4.40, −4.04 in my coordinates)". The adjudicator: "I should have caught F1 myself: I checked the potential only at frozen H." (`review/round4-adjudication.md`; [Review round 4](/wiki/method/review/round-4)).
- **The repair, checked with H dynamical.** The toy-model note v2: "The normalized form V_b = −μ[Tr(K K_ref)]² / (2 Tr KᵀK) is bounded, −μ ≤ V_b ≤ 0 by Cauchy–Schwarz"; "With H dynamical, (1, K_ref) is a stable minimum: Hessian eigenvalues 0, 0.764, 2, 5.236." The gate prints `with V_b, (1, K_ref) is stable: Hessian eigenvalues >= 0 with exactly one zero  [[-0.      0.7639  2.      5.2361]]` beside `the unnormalized potential makes (1, K_ref) a saddle (negative Hessian eigenvalue)  [[-6.472  0.     2.472  8.   ]]` (`verify/toy_coset.py`). See [The bounded potential V_b](/wiki/symmetry-breaking/toy-models/coset-model/bounded-potential).
- **The zero mode: sources disagree.** The adjudication called the remaining flat direction "the residual diagonal squeeze, which is an exact symmetry"; the note v2 says "It is not symmetry-protected, because V_b breaks the squeeze away from K = ±K_ref." In the wiki's precedence order the note (rank 2) outranks the adjudication (rank 3), so the wiki follows the note. The gate checks only that the line is flat: `the zero mode is the squeeze line H = diag(y, 1/y), K = K_ref: V = -1 all along it`.
- **Saying it is a reduction.** The docstring of `verify/toy_s4.py`: `This is the FROZEN-H reduction of the coset toy (H = 1 held fixed); the unreduced model's stability with the bounded potential V_b is checked in toy_coset.py.` The note's heading reads "Monte Carlo of the frozen-H reduction", with "H is not simulated." #11 §14 item 11 records "an ordered ℤ₂ phase in 1+1 in the frozen-H reduction (Monte Carlo)". See [The frozen-H reduction](/wiki/symmetry-breaking/toy-models/coset-model/frozen-h-reduction) and [Monte Carlo: an ordered ℤ₂ phase](/wiki/symmetry-breaking/toy-models/coset-model/monte-carlo).
- **What is still open.** "Still open [O]: a Monte Carlo with H dynamical" (#11 §14 item 11); the note lists "a Monte Carlo of model I with H dynamical" as not shown (§6). See [Acceptance criterion 1: the toy Lagrangian](/wiki/symmetry-breaking/toy-models/acceptance-criterion).

## Sources

- Root `CLAUDE.md` 'Method' — the rule
- `review/round4-adjudication.md` 'Lessons (into CLAUDE.md)' (lesson 1) and 'Rulings' (F1, F2) — the failure and the repair
- `papers/reciprocity-toy-models.md` §4, §6 — the bounded potential, the zero mode, the reduction stated, what is not shown
- `papers/broken-born-checkpoint-v2.md` §14 item 11 — the result as #11 records it, and the open Monte Carlo
- `verify/toy_coset.py` — the gated saddle, the stable minimum and the flat line
- `verify/toy_s4.py` — the reduction stated in the script
