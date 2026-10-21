---
title: "Obituary: the naive ρ-preserving potential"
weight: 40
status: dead
description: "−μ[Tr(K K_ref)]² is unbounded below once H is dynamical (−8.9 × 10⁶ μ at boost parameter 4), so its intended vacuum is a saddle; round 4's findings F1–F2, kept as the counterexample."
sources:
  - "papers/reciprocity-toy-models.md §4"
  - "review/round4-adjudication.md 'Rulings' F1–F2"
  - "review/round4-adjudication.md 'Lessons'"
  - "review/round4/referee/audit-notes.md Step 2(a)"
  - "review/round4/referee/audit-notes.md Step 2(c)"
  - "review/round4/referee/audit-notes.md Step 3"
  - "verify/toy_coset.py"
  - "verify/toy_s4.py"
  - "notes/toy-lagrangian.md 'Chunk 1 results'"
  - "notes/toy-lagrangian.md 'Chunk 3 results'"
---

*The naive ρ-preserving potential was the term −μ[Tr(K K_ref)]², added to [model I](/wiki/symmetry-breaking/toy-models/coset-model) to reduce its continuous circle of vacua to two, so that the breaking of [Born reciprocity](/wiki/phase-space/reciprocity/born-reciprocity) could survive in two dimensions. It is symmetric under ρ and gives two vacua when the metric H is held fixed, but once H is allowed to vary it is unbounded below: along a family of boosted configurations its energy falls without limit while the compatibility term stays zero, and the intended vacuum is a saddle. The worklog's first pass of criterion S4 rested on it. The round-4 referee found the defect, the adjudication upheld it, and the potential is kept only as the counterexample that the [bounded potential V_b](/wiki/symmetry-breaking/toy-models/coset-model/bounded-potential) answers.*

**Status:** Dead as a stabilizing potential; kept as the counterexample — untagged in the sources — killed by round-4 findings F1 and F2, both upheld ([review round 4](/wiki/method/review/round-4)); the runaway and the saddle are checked in `verify/toy_coset.py` ([the toy-model scripts](/wiki/method/verification/toy-model-scripts)). Listed in [the graveyard](/wiki/status/graveyard).

## Key facts

- **What was claimed.** The worklog's fallback for criterion S4: "Discrete reduction by a τ-type potential −μ[Tr(K K_ref)]². It keeps ρ and leaves two vacua (±K_ref) exchanged by ρ, which is Ising-like, so the breaking survives in 1+1." At H = 1 it equals −2μ(1 + cos 2φ). Its cost was noted then: "a rigid, unordered pair of axes".
- **How it was tested.** Only with H frozen at 1, in the lattice simulation of chunk 3. The adjudicator: "I should have caught F1 myself: I checked the potential only at frozen H."
- **Why it failed: F1, unbounded below.** Along H = SᵀS, K = S⁻¹K₀S with S a boost, "the λ-term is ~0 while V_μ = −4, −56.6, −2983, −8.9×10⁶ at t = 0, 1, 2, 4" (adjudication). The referee found V_μ = −4μ cosh²(2t) on this family: "Constant fields, so no kinetic cost."
- **Why it failed: F2, a saddle.** "The point (1, K_ref) is a saddle (Hessian eigenvalue −6.47 at λ = μ = 1)" (version 2, in the coordinates of `verify/toy_coset.py`); the referee's coordinates give −3.3723, and the negative mode persists at λ = 10 and 100. The two values are coordinate-dependent and agree in sign. So the two vacua ±K_ref exist only with H frozen, and the simulation was "of the textbook XY + two-fold-field model with H frozen, not of model I" (referee).
- **The residual symmetry.** With the potential added, the referee found (with sympy) that it leaves a non-compact subgroup diag(a, 1/a) of Sp(2, ℝ) unbroken, plus ℤ₄ = {±1, ±ρ} in SO(2): "in model I proper, the boost direction is where the potential runs away."
- **What it brought down.** The worklog's S4 pass and its verdict on [acceptance criterion 1](/wiki/symmetry-breaking/toy-models/acceptance-criterion) used this potential. The docstring of `verify/toy_s4.py` still calls it "the tau-type potential", a wording lag only: the lattice energy −h cos 2φ equals the bounded form at H = 1 up to a constant and a factor. Round 4 turned the episode into a rule, now in the root `CLAUDE.md`: check the unreduced model's stability when numerics run on a reduced one ([the reduced-model stability rule](/wiki/method/verification/reduced-model-stability)).
- **What survives.** The [bounded potential V_b](/wiki/symmetry-breaking/toy-models/coset-model/bounded-potential), proposed by the referee and adopted in version 2, bounded by Cauchy–Schwarz and stable with H dynamical; and the [Monte Carlo](/wiki/symmetry-breaking/toy-models/coset-model/monte-carlo), restated as a result about the [frozen-H reduction](/wiki/symmetry-breaking/toy-models/coset-model/frozen-h-reduction). #11 §10 now requires that the ρ-preserving potential "must be bounded with all fields dynamical". Where any such potential comes from is [open](/wiki/symmetry-breaking/rho-preserving-potential).

## Sources

- `papers/reciprocity-toy-models.md` §4 — the runaway at boost parameter 4 and the saddle eigenvalue −6.47, as version 2 states them
- `review/round4-adjudication.md` 'Rulings' F1–F2, 'Lessons' — the upheld findings, the runaway values, the adjudicator's admission and the reduced-model lesson
- `verify/toy_coset.py` — the gated runaway and saddle checks
- `review/round4/referee/audit-notes.md` Step 2(a), Step 2(c), Step 3 — the referee's derivation of F1–F2, the residual symmetry, and the reading of the simulation as a frozen-H model
- `notes/toy-lagrangian.md` 'Chunk 1 results', 'Chunk 3 results' — the original fallback and the S4 pass that used it
- `verify/toy_s4.py` — the docstring's wording lag
