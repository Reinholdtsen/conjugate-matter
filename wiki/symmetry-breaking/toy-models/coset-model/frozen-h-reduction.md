---
title: "The frozen-H reduction"
weight: 60
status: alive
description: "Holding H = 1 turns model I into a two-dimensional spin model of the polarization angle; what the 1+1 result establishes for that reduction only, how spontaneous its breaking is, why 'Ising class' became 'ordered ℤ₂ phase', and the open simulation with H dynamical."
sources:
  - "papers/reciprocity-toy-models.md §4"
  - "papers/reciprocity-toy-models.md §6"
  - "papers/reciprocity-toy-models.md v1 (commit d9a06ac) §4, §6"
  - "papers/broken-born-checkpoint-v2.md §4"
  - "papers/broken-born-checkpoint-v2.md §14 item 11"
  - "CLAUDE.md 'Method'"
  - "CLAUDE.md 'Since the handoff'"
  - "review/round4-adjudication.md 'Rulings' F2"
  - "review/round4-adjudication.md 'Revisions' 1"
  - "review/round4-adjudication.md 'Lessons'"
  - "review/round4-adjudication.md 'Pre-registration scored'"
  - "review/round4-preregistration.md 'Predictions'"
  - "review/round4/referee/audit-notes.md Step 2(a)"
  - "review/round4/referee/audit-notes.md Step 2(c)"
  - "review/round4/referee/audit-notes.md Step 3"
  - "verify/toy_s4.py"
  - "verify/toy_coset.py"
  - "notes/toy-lagrangian.md 'Success criteria'"
  - "notes/toy-lagrangian.md 'Chunk 3 results'"
  - "notes/toy-lagrangian.md 'Assessment against the predictions'"
---

*The frozen-H reduction is [model I](/wiki/symmetry-breaking/toy-models/coset-model) with its metric field held fixed at H = 1, so that the only remaining field is the polarization angle φ of the real structure K(φ). In that form the model is a two-dimensional spin model of one angle, with a stiffness term and a ρ-preserving potential, and it can be simulated on a lattice. The ordered ℤ₂ phase the simulation finds is a result about this reduction; with H dynamical, ordering is not established. Round 4 required the text to say so, after showing that the first potential tried was stable only while H stayed frozen. It also replaced the claim of "Ising-class" breaking with "an ordered ℤ₂ phase", because data at one temperature establish order but not a universality class.*

**Status:** Alive, as the stated scope of the lattice result — untagged — required by round-4 revision 1 ("Present the Monte Carlo as the frozen-H reduction, explicitly"), stated in version 2, §4 and §6, and in [#11](/wiki/history/documents/checkpoint) §14 item 11; simulated in `verify/toy_s4.py` ([the toy-model scripts](/wiki/method/verification/toy-model-scripts)).

## What the reduction is

H = 1 is the point Z = i of the upper half-plane, the one metric that [Born reciprocity](/wiki/phase-space/reciprocity/born-reciprocity) ρ leaves in place ([model I vacua](/wiki/symmetry-breaking/toy-models/coset-model/vacua)). Holding H there removes the metric sector, and restricting K to its circle of compatible values K(φ) = [[cos φ, sin φ], [sin φ, −cos φ]] removes the compatibility term. What is left is one angle per point of the base. The pieces, as the sources give them:

```text
K kinetic term at H = 1:   (f_K²/4) Tr(∂Kᵀ ∂K) = (f_K²/2)(∂φ)²        an XY stiffness
V_b at H = 1:              −(μ/2)(1 + cos 2φ)
ρ at H = 1:                φ → φ + π
lattice energy:            E = −J Σ⟨ij⟩ cos(φ_i − φ_j) − h Σ_i cos 2φ_i
```

The stiffness is the referee's check, "(f_K^2/4)Tr(dK^T dK) = (1/2) f_K^2 (dphi)^2 -> matches (f_K^2/2)(dphi)^2" (`review/round4/referee/audit-notes.md`, Step 2(a)), and `verify/toy_s4.py` calls it "an XY stiffness". The potential is [the bounded potential V_b](/wiki/symmetry-breaking/toy-models/coset-model/bounded-potential) on the circle (toy-model note §4). The action of ρ is the worklog's: "at H = 1 the polarization field is the angle φ of K(φ), and ρ acts as φ → φ + π" ('Chunk 3 results').

Version 2 states the simulated model and its scope in one sentence: "We simulate the lattice model E = −J Σ cos(φ_i − φ_j) − h Σ cos 2φ_i: model I's polarization angle at H = 1, with V_b up to a constant and normalization. H is not simulated." (§4). On the lattice the first sum runs over neighbouring sites. For small differences, 1 − cos(φ_i − φ_j) is about half the squared difference, so the first sum is the lattice form of the stiffness term, with J setting the stiffness [T]. The second sum is the potential, with h setting its strength: −h cos 2φ "equals the bounded V_b at H = 1 up to a constant and a factor (both depend on phi only through cos 2 phi)" (`verify/toy_s4.py`). The lattice coupling J has nothing to do with the J that #11's postulate P2′ uses for the real structure.

In statistical mechanics this is the XY model, a lattice of planar spins, with a two-fold symmetry-breaking field [T]: the referee's "textbook XY + two-fold-field model" (Step 3, point C3), the first version's "two-fold anisotropic planar model". The cos 2φ term has two minima per turn of the angle, at φ = 0 and φ = π.

### Symmetries of the reduced model

The shift φ → φ + π, which is ρ, leaves both sums unchanged and reverses the sign of cos φ = K₁₁, the [order parameter](/wiki/symmetry-breaking/order-parameter). With h = 0 every shift φ → φ + α is a symmetry, the continuous U(1) of the XY model; with h ≠ 0 only the shift by π survives among the shifts [T]. So the potential reduces the continuous symmetry of the circle to a discrete ℤ₂. A discrete symmetry lies outside [the Mermin–Wagner–Coleman theorem](/wiki/symmetry-breaking/mermin-wagner-coleman) and can break in two dimensions, as the two-dimensional Ising model shows [T].

### Why a two-dimensional lattice tests 1+1 dimensions

Model I's Lagrangian is Euclidean. The Euclidean action of a field theory in 1+1 dimensions has the form of the energy of a classical system in two dimensions, so sampling the lattice model at a temperature T samples the quantum fluctuations of the 1+1-dimensional theory, with T in the role of the coupling [T]. `verify/toy_s4.py` describes its lattice as "a square lattice (Euclidean 2D)". That is why a classical Monte Carlo answers criterion S4, "The breaking survives quantum fluctuations in the stated dimension" (worklog, 'Success criteria').

## Why the scope had to be stated

The first version of the note made the reduction without naming it: "At H = 1 the polarization field is φ, with XY stiffness (f_K²/2)(∂φ)²." (v1 §4, commit d9a06ac). With the potential it used then, H frozen was the only setting in which the intended vacua exist. Round-4 finding F2, upheld: "So (1, K_ref) is a saddle, and the Monte Carlo simulates a frozen-H reduction, not model I" (`review/round4-adjudication.md`). The referee: "The 'two vacua K=+-K_ref' exist only if H is frozen at 1, which the manuscript asserts ('At H = 1 the polarization field is phi') but does not justify; H is a dynamical hyperbolic sigma field." (Step 2(a)). The failure is recorded at [Obituary: the naive ρ-preserving potential](/wiki/symmetry-breaking/toy-models/coset-model/naive-potential).

Revision 1 required: "Present the Monte Carlo as the frozen-H reduction, explicitly." Version 2 says "H is not simulated" (§4), and the script's docstring now reads: "This is the frozen-H reduction of the coset toy (H = 1 held fixed); the unreduced model's stability with the bounded potential V_b is checked in toy_coset.py." (`verify/toy_s4.py`; capitals lowered here). The second half of that sentence is the check that the [reduced-model stability rule](/wiki/method/verification/reduced-model-stability) now demands: with V_b the unreduced vacuum is a stable minimum with H dynamical (`verify/toy_coset.py`). The simulation itself still covers only the angle.

## What it establishes

Version 2, §6, under "Shown": "Model I: an ordered ℤ₂ phase in the frozen-H reduction in 1+1." [Checkpoint #11](/wiki/history/documents/checkpoint) §14 item 11 lists the same result as one of three parts of [acceptance criterion 1](/wiki/symmetry-breaking/toy-models/acceptance-criterion): "there is an ordered ℤ₂ phase in 1+1 in the frozen-H reduction (Monte Carlo)", next to "the vacuum is stable with H dynamical". The numbers, error bars and controls are at [Monte Carlo: an ordered ℤ₂ phase](/wiki/symmetry-breaking/toy-models/coset-model/monte-carlo).

## How spontaneous the breaking is

The referee asked whether "spontaneous breaking" is a fair description of model I in 1+1, and answered (Step 3; its notes abbreviate spontaneous symmetry breaking as SSB):

> With H frozen: yes, standard Ising-type SSB of the residual Z2 = <rho>/<rho^2> (the potential's SO(2) residue is {+-1, +-rho}, sympy). But the potential fixes the unordered axis pair by hand, so the vacuum chooses only which of two pre-set axes is "position". The manuscript says this in Sec. 6 ("rigid unordered pair of axes"); the abstract's "rho is spontaneously broken" should carry the qualifier and the frozen-H caveat. With H dynamical as written: not established (C3).

So in the reduction one thing is put in and one is chosen. The potential fixes the unordered pair {x-axis, p-axis}, which is K_ref up to sign; the vacuum chooses which member of the pair counts as position. The worklog had named the same cost: "The price is a rigid, unordered pair of axes (K_ref up to sign). That is more rigid structure than P2′'s 'only ω is rigid', though less than a rigid η." ('Chunk 3 results'). #11 carries it into the refinement of [P2′](/wiki/program/postulates/p2-prime): "A definite polarization needs a ρ-preserving potential on that angle — a rigid, unordered pair of axes, so more structure than ω alone, though less than a rigid η." (§4).

The [pre-registration](/wiki/method/review/pre-registration) had predicted this as round 4's weakest link: "in 1+1, the 'spontaneous' breaking of ρ rests on an explicit, rigid background. The ρ-preserving potential needs a fixed unordered pair of axes K_ref. A referee can reasonably call model I's 1+1 result an ordinary Z₂ breaking of an explicitly chosen axis pair. Model I without it is a coset construction by definition." (`review/round4-preregistration.md`). The adjudication scored it "Partial: right location, missed severity": the referee found a worse defect at the same spot, the unbounded potential.

The worklog's revised conclusion describes what the toy supports: "'broken reciprocity' in the form 'a pseudo-Goldstone polarization angle with a ρ-symmetric potential', not 'only ω rigid, nothing else'." ('Chunk 3 results'). A pseudo-Goldstone mode is a flat direction given a small energy cost by a small explicit breaking of the symmetry [T] ([the polarization as a Goldstone angle](/wiki/symmetry-breaking/goldstone-angle)).

## Superseded: Ising-class breaking in model I

The first version of the note listed, among the results "Established here", "Ising-class breaking of ρ in model I in 1+1, once a ρ-preserving potential is added" (v1 §6). Its §4 called the lattice model "the two-fold anisotropic planar model, whose ordered phase is Ising-like [12]". The worklog had written "Then ρ breaks as a Z₂ (Ising class), with vacua ±K_ref: 'x is position' and 'p is position'" ('Chunk 3 results'), and its verdict on acceptance criterion 1 says "It is spontaneously broken (Ising class in 1+1, Monte Carlo verified)" ('Assessment against the predictions').

Round 4 narrowed the claim in two ways.

1. **From model I to the reduction.** "Sec. 6's 'Ising-class breaking of rho in model I in 1+1' is therefore not established." (referee, Step 3, point C3). The simulation never let H move.
2. **From a universality class to order.** "'Ising-class': data at a single T deep in the ordered phase establish order only, not universality class. Minor wording." (referee, Step 2(c)). Revision 1: "Say 'ordered Z₂ phase', not 'Ising class'." Version 2: "We call the first row an ordered ℤ₂ phase. We did not measure critical exponents." (§4).

The distinction [T]: a universality class is fixed by the critical exponents of a phase transition, which depend on the dimension and the symmetry rather than on details; the two-dimensional Ising class has exact exponents (Onsager 1944†). A simulation at one temperature, here T = 0.6, deep in the ordered phase shows that the ℤ₂ is broken there, but says nothing about the exponents at the transition. The current statement is "an ordered ℤ₂ phase in the frozen-H reduction in 1+1" (version 2, §6; #11 §14 item 11). The change is listed among the [superseded statements](/wiki/status/superseded).

## Open: a Monte Carlo with H dynamical

#11 §14 item 11: "Still open [O]: a Monte Carlo with H dynamical; a derivation of the potential; ..." Version 2 lists "a Monte Carlo of model I with H dynamical" under "Not shown" (§6), and the root `CLAUDE.md` names it first among the toy work's open ends ('Since the handoff').

What exists instead is a classical check at one point: with V_b the vacuum (1, K_ref) is a minimum of the potential with all four field directions free ([the bounded potential V_b](/wiki/symmetry-breaking/toy-models/coset-model/bounded-potential#stability-with-h-dynamical)). Whether the ordered phase survives when H also fluctuates has not been computed, and the sources do not say how such a simulation would be set up. A related but separate question, whether ρ's SO(2) breaks in the coupled model without any potential, is [also open](/wiki/symmetry-breaking/toy-models/coset-model/so2-question). Both are registered at [open problems](/wiki/status/open-problems).

## The rule it produced

Round-4 lesson 1: "When numerics run on a reduced model (some fields frozen), check the stability of the unreduced model — boundedness, and the Hessian with all fields dynamical — and state the reduction in the text." (`review/round4-adjudication.md`, 'Lessons'). The root `CLAUDE.md` carries it in its Method section, adding "Round 4 found a potential that was bounded only at frozen H." The episode that produced it is the adjudicator's: "I should have caught F1 myself: I checked the potential only at frozen H." See [the reduced-model stability rule](/wiki/method/verification/reduced-model-stability).

## Sources

- `papers/reciprocity-toy-models.md` §4, §6 — the reduction as simulated; "Shown" and "Not shown"; "We did not measure critical exponents"
- `papers/reciprocity-toy-models.md` v1 (commit d9a06ac) §4, §6 — the unstated reduction and the superseded "Ising-class" claim
- `papers/broken-born-checkpoint-v2.md` §4, §14 item 11 — P2′'s price; the result as the checkpoint records it, and the open simulation [O]
- `review/round4-adjudication.md` 'Rulings' F2, 'Revisions' 1, 'Lessons', 'Pre-registration scored' — the frozen-H finding, the required reframing, the rule and the scored weakest link
- `review/round4-preregistration.md` 'Predictions' — the predicted weakest link
- `review/round4/referee/audit-notes.md` Step 2(a), Step 2(c), Step 3 — the stiffness check, the universality-class point, point C3 and the reading of how spontaneous the breaking is
- `verify/toy_s4.py` — the reduction as coded, and its docstring
- `verify/toy_coset.py` — the unreduced model's stability with V_b
- `notes/toy-lagrangian.md` 'Success criteria', 'Chunk 3 results', 'Assessment against the predictions' — criterion S4; the reduction as first made; the Ising-class wording and the price of the potential
- `CLAUDE.md` 'Method', 'Since the handoff' — the reduced-model rule; the open simulation
