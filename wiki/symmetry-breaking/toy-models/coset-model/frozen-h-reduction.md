---
title: "The frozen-H reduction"
weight: 60
status: alive
description: "Holding H = 1 turns model I into a 2D spin model of the polarization angle; what the 1+1 result establishes for the reduction only, and why 'Ising class' became 'ordered ℤ₂ phase'."
sources:
  - "papers/reciprocity-toy-models.md §4"
  - "papers/reciprocity-toy-models.md §6"
  - "papers/broken-born-checkpoint-v2.md §14 item 11"
  - "CLAUDE.md 'Method'"
  - "review/round4-adjudication.md 'Revisions' 1"
  - "review/round4-adjudication.md 'Pre-registration scored'"
  - "review/round4-preregistration.md 'Predictions'"
  - "review/round4/referee/audit-notes.md Step 2(a)"
  - "review/round4/referee/audit-notes.md Step 2(c)"
  - "review/round4/referee/audit-notes.md Step 3"
  - "verify/toy_s4.py"
---

*The frozen-H reduction is [model I](/wiki/symmetry-breaking/toy-models/coset-model) with its metric field held fixed at H = 1, so that the only remaining field is the polarization angle φ of the real structure K(φ). In that form the model is a two-dimensional spin model of one angle, with a stiffness term and the ρ-preserving potential, and it can be simulated on a lattice. The ordered ℤ₂ phase that the simulation finds is a result about this reduction; with H dynamical, ordering is not established. Round 4 required the text to say so, and replaced the worklog's "Ising class" with "ordered ℤ₂ phase", because data at one temperature establish order but not a universality class.*

**Status:** Alive, as the stated scope of the lattice result — untagged — required by round-4 revision 1 ("Present the Monte Carlo as the frozen-H reduction, explicitly"), stated in version 2, §4 and §6, and in #11 §14 item 11; simulated in `verify/toy_s4.py` ([the toy-model scripts](/wiki/method/verification/toy-model-scripts)).

## Key facts

- **The reduction.** "We simulate the lattice model E = −J Σ cos(φ_i − φ_j) − h Σ cos 2φ_i: model I's polarization angle at H = 1, with V_b up to a constant and normalization. H is not simulated." At H = 1, ρ acts as φ → φ + π, and K's kinetic term is an XY stiffness, (f_K²/4) Tr(∂Kᵀ∂K) = (f_K²/2)(∂φ)² (`verify/toy_s4.py`; confirmed by the round-4 referee). ([the bounded potential V_b](/wiki/symmetry-breaking/toy-models/coset-model/bounded-potential))
- **What it establishes.** "Model I: an ordered ℤ₂ phase in the frozen-H reduction in 1+1" (version 2, §6, "Shown"); #11 §14 item 11 records "an ordered ℤ₂ phase in 1+1 in the frozen-H reduction (Monte Carlo)" ([the Monte Carlo](/wiki/symmetry-breaking/toy-models/coset-model/monte-carlo)).
- **What it does not.** "a Monte Carlo of model I with H dynamical" (version 2, §6, "Not shown"), still open [O] in #11 §14 item 11. With H dynamical the [naive potential](/wiki/symmetry-breaking/toy-models/coset-model/naive-potential) is unbounded below, so round 4 ruled that the first version's simulation was of "a frozen-H reduction, not model I" (finding F2), a reduction the text had not stated.
- **How spontaneous the breaking is.** The referee: with H frozen, the breaking is the standard Ising-type breaking of the residual ℤ₂, "But the potential fixes the unordered axis pair by hand, so the vacuum chooses only which of two pre-set axes is 'position'." "With H dynamical as written: not established."
- **Predicted as the weakest link.** The round-4 pre-registration named this spot: "in 1+1, the 'spontaneous' breaking of ρ rests on an explicit, rigid background. The ρ-preserving potential needs a fixed unordered pair of axes K_ref." It was scored "Partial: right location, missed severity", since the defect found there was worse ([pre-registration](/wiki/method/review/pre-registration)).
- **The narrowed claim.** The first version's §6 claimed "Ising-class breaking of rho in model I in 1+1"; the referee: "data at a single T deep in the ordered phase establish order only, not universality class." Revision 1: "Say 'ordered Z₂ phase', not 'Ising class'." Version 2: "We did not measure critical exponents."
- **The rule it produced.** Root `CLAUDE.md`, Method: "When numerics run on a reduced model (fields frozen), check the unreduced model's stability — boundedness, and the Hessian with all fields dynamical — and say in the text that it is a reduction." ([the reduced-model stability rule](/wiki/method/verification/reduced-model-stability))
- **What lies beyond it.** Whether the full coupled model, whose H-sector is a hyperbolic sigma model, orders ρ's compact SO(2) without a potential is [a separate open question](/wiki/symmetry-breaking/toy-models/coset-model/so2-question).

## Sources

- `papers/reciprocity-toy-models.md` §4, §6 — the reduction as simulated; "Shown" and "Not shown"
- `papers/broken-born-checkpoint-v2.md` §14 item 11 — the result as the checkpoint records it, and the open simulation [O]
- `CLAUDE.md` 'Method' — the reduced-model rule
- `review/round4-adjudication.md` 'Revisions' 1, 'Pre-registration scored' — the required reframing and the scored weakest link
- `review/round4-preregistration.md` 'Predictions' — the predicted weakest link
- `review/round4/referee/audit-notes.md` Step 2(a), Step 2(c), Step 3 — the stiffness check, the universality-class point and the reading of how spontaneous the breaking is
- `verify/toy_s4.py` — the reduction as coded, and its docstring
