---
title: "Open: a Monte Carlo with H dynamical"
weight: 75
status: open
description: "Model I's ordered ℤ₂ phase has been simulated only with the metric H held at 1; a simulation with H fluctuating too is open [O]. What the reduction shows, why round 4 required it to be named, the classical check with all four field directions free (Hessian 0, 0.764, 2, 5.236, one flat line that no symmetry protects), how the full model differs, and what would close the item."
provenance: [O]
sources:
  - "papers/broken-born-checkpoint-v2.md §14 item 11"
  - "papers/reciprocity-toy-models.md §2"
  - "papers/reciprocity-toy-models.md §4"
  - "papers/reciprocity-toy-models.md §6"
  - "papers/reciprocity-toy-models.md v1 (commit d9a06ac) §4, §6"
  - "CLAUDE.md 'Since the handoff'"
  - "CLAUDE.md 'Method'"
  - "CLAUDE.md 'The gate'"
  - "review/round4-adjudication.md 'Rulings' F1–F2"
  - "review/round4-adjudication.md 'Rulings' (MC start)"
  - "review/round4-adjudication.md 'Revisions' 1"
  - "review/round4-adjudication.md 'Lessons'"
  - "review/round4/adjudicator/arb.out"
  - "review/round4/referee/audit-notes.md Step 2(a)"
  - "review/round4/referee/audit-notes.md Step 3"
  - "verify/toy_coset.py"
  - "verify/toy_s4.py"
  - "notes/toy-lagrangian.md 'Success criteria'"
  - "notes/toy-lagrangian.md 'Chunk 3 results'"
  - "review/wiki-build-flags.md item 12"
  - "review/wiki-build-flags.md item 40"
---

*A Monte Carlo with H dynamical is a lattice simulation of [model I](/wiki/symmetry-breaking/toy-models/coset-model) in which the phase-space metric H varies from point to point and fluctuates together with the real structure K, instead of being held at the constant value H = 1. The program's simulation is of the simpler model with H held fixed, [the frozen-H reduction](/wiki/symmetry-breaking/toy-models/coset-model/frozen-h-reduction), which keeps only the polarization angle, the angle that sets which line of the phase plane counts as position. With [the bounded potential V_b](/wiki/symmetry-breaking/toy-models/coset-model/bounded-potential) added, that angle stays near one of the two values that [Born reciprocity](/wiki/phase-space/reciprocity/born-reciprocity) ρ exchanges: an ordered ℤ₂ phase. Whether the order survives when H fluctuates as well has not been computed. [Round 4](/wiki/method/review/round-4) required the lattice result to be stated for the reduction only, after finding that the first potential tried, stable in the reduction, fell without limit once H was allowed to move. For the full model there is a classical check instead: the vacuum is a minimum of the potential with all four field directions free, though along one of them the potential is flat and no symmetry keeps it so. [Checkpoint #11](/wiki/history/documents/checkpoint) lists the simulation as open, and no source says how it would be set up.*

**Status:** Open — [O] ([#11](/wiki/history/documents/checkpoint) §14 item 11: "Still open [O]: a Monte Carlo with H dynamical") — first in the list of what is "Not shown" in version 2 of the toy-model note (§6), and first among the toy work's open ends in the root `CLAUDE.md`. No script simulates model I with H dynamical; the classical check with H free is gated in `verify/toy_coset.py`, and the frozen-H simulation in `verify/toy_s4.py` ([the toy-model scripts](/wiki/method/verification/toy-model-scripts)). It qualifies [the ordered ℤ₂ phase](/wiki/symmetry-breaking/toy-models/coset-model/monte-carlo) and the third part of [acceptance criterion 1](/wiki/symmetry-breaking/toy-models/acceptance-criterion). Registered at [open problems](/wiki/status/open-problems#the-toy-model-open-ends).

## The open item

#11 §14 item 11 records acceptance criterion 1, the referees' demand for an action in which ρ is a symmetry that the vacuum breaks spontaneously, with the neutral metric η as [order parameter](/wiki/symmetry-breaking/order-parameter), as "Met in the referees' wording by the coset model of (H, K) with a bounded ρ-preserving potential". It lists what that covers and what it leaves open:

> - ρ is a symmetry of an explicit action, and η = ωK is the order parameter;
> - the vacuum is stable with H dynamical;
> - there is an ordered ℤ₂ phase in 1+1 in the frozen-H reduction (Monte Carlo).
>
> Still open [O]: a Monte Carlo with H dynamical; a derivation of the potential; locality of matter beyond the weak (Yukawa-like) form, which in the toy reduces to P4.

The [toy-model note](/wiki/symmetry-breaking/toy-models) (`papers/reciprocity-toy-models.md`, version 2; "the note" below) puts "a Monte Carlo of model I with H dynamical" first in its list of what is "Not shown" (§6). The root `CLAUDE.md` names "a Monte Carlo with H dynamical" first among the four open ends of the toy Lagrangian ('Since the handoff'). The other three have their own pages: [the origin of the ρ-preserving potential](/wiki/symmetry-breaking/rho-preserving-potential), [forced locality and the P4 lock](/wiki/symmetry-breaking/strong-locality) and [the real model's one-loop preference](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/real-model-lead).

### What "H dynamical" means

In model I, H is a field. At every point of the 1+1-dimensional base it is "a positive symmetric symplectic matrix", equivalently a point Z of the [upper half-plane](/wiki/phase-space/modular-field/siegel-domain), and it has its own kinetic term, (f_H²/8) Tr(H⁻¹∂H H⁻¹∂H) (note §2; [the H kinetic term](/wiki/symmetry-breaking/toy-models/coset-model/action-and-symmetries#the-h-kinetic-term)). "H dynamical" means that this field varies and fluctuates as K does. "Frozen" means that it is held at H = 1, the point Z = i, which is the one metric that ρ leaves in place.

The two parts of the criterion that mention H are statements of different kinds. "The vacuum is stable with H dynamical" is classical: it concerns the potential near one configuration of the fields. "An ordered ℤ₂ phase" is statistical: it concerns what fluctuating fields do over a large region, and it has been shown with H frozen only. The open item asks for the second kind of statement about the full model.

#11 places the item under the criterion met "with a bounded ρ-preserving potential", and the note lists the coupled model without a potential as a separate item (§6; [below](#the-related-question-without-a-potential)). In this wiki's reading the open simulation is therefore of model I with V_b, the model whose reduction was simulated; no source says so in as many words.

## What the frozen-H simulation shows

Holding H at 1 and keeping K on its circle of compatible values, K(φ) = [[cos φ, sin φ], [sin φ, −cos φ]], leaves one angle φ per point of the base. Its stiffness comes from K's kinetic term, and at H = 1 the potential is "V_b = −(μ/2)(1 + cos 2φ)" (note §4). On a square lattice the note simulates

```text
E = −J Σ⟨ij⟩ cos(φ_i − φ_j) − h Σ_i cos 2φ_i
```

"model I's polarization angle at H = 1, with V_b up to a constant and normalization. H is not simulated." (§4). A Monte Carlo simulation of this kind samples configurations of the angles with the Boltzmann weight of their energy at a temperature T, by accepting or rejecting random local changes [T] ([the algorithm](/wiki/symmetry-breaking/toy-models/coset-model/monte-carlo#the-algorithm)). ρ acts as φ → φ + π, and the order parameter is the lattice average m of cos φ, which ρ reverses.

With the potential (J = h = 1, T = 0.6) the mean of |m| is 0.954 at all three lattice sizes, L = 16, 32 and 64, with a Binder cumulant of 0.667, which the note reads as an "Ordered ℤ₂ phase". Without the potential (h = 0) the order falls with lattice size, "No true order", and a control at T = 3.0 is disordered (§4; reproduced by `verify/toy_s4.py`). The runs, their error bars and their limits are at [Monte Carlo: an ordered ℤ₂ phase](/wiki/symmetry-breaking/toy-models/coset-model/monte-carlo).

Version 2 states the result at that scope: "Model I: an ordered ℤ₂ phase in the frozen-H reduction in 1+1." (§6, under "Shown"). With the potential, only the shift by π survives among the shifts of the angle; a discrete symmetry of this kind can break in two dimensions, while a continuous compact one cannot [T] ([the Mermin–Wagner–Coleman theorem](/wiki/symmetry-breaking/mermin-wagner-coleman)). A classical lattice in two dimensions stands for the quantum theory in 1+1 dimensions because model I's Lagrangian is Euclidean [T] ([why a two-dimensional lattice tests 1+1 dimensions](/wiki/symmetry-breaking/toy-models/coset-model/frozen-h-reduction#why-a-two-dimensional-lattice-tests-11-dimensions)).

## Why the result is stated for the reduction

### The first potential, once H moves

The worklog took the step as a reduction: "Reduction: at H = 1 the polarization field is the angle φ of K(φ), and ρ acts as φ → φ + π." ('Chunk 3 results'). The first version of the note took it without comment, "At H = 1 the polarization field is φ, with XY stiffness (f_K²/2)(∂φ)²" (v1 §4, commit d9a06ac), and listed among its results "Ising-class breaking of ρ in model I in 1+1, once a ρ-preserving potential is added" (v1 §6). The potential then was the naive form, "−μ[Tr(K K_ref)]² = −2μ(1 + cos 2φ)" at H = 1 (v1 §4).

Round 4 tested that potential with H free. Finding F1, upheld: "The §4 potential −μ[Tr(K K_ref)]² is unbounded below in model I". Along a family of constant fields in which a boost of the phase plane moves H and K together, so that the compatibility term stays zero, the potential "reaches −8.9 × 10⁶ μ at boost parameter 4" (note §4). Finding F2, upheld: "So (1, K_ref) is a saddle, and the Monte Carlo simulates a frozen-H reduction, not model I" (`review/round4-adjudication.md`, 'Rulings'), with "Hessian eigenvalue −6.47 at λ = μ = 1" (note §4). The referee: "The 'two vacua K=+-K_ref' exist only if H is frozen at 1, which the manuscript asserts ('At H = 1 the polarization field is phi') but does not justify; H is a dynamical hyperbolic sigma field." (`review/round4/referee/audit-notes.md`, Step 2(a)). The failure is recorded at [Obituary: the naive ρ-preserving potential](/wiki/symmetry-breaking/toy-models/coset-model/naive-potential).

### What the referee concluded about the simulation

"The Monte Carlo is of the textbook XY + two-fold-field model with H frozen, not of model I. Sec. 6's 'Ising-class breaking of rho in model I in 1+1' is therefore not established." (Step 3, point C3). Asked whether "spontaneous breaking" fairly describes model I in 1+1, the referee answered yes for the reduction, an Ising-type breaking of the remaining ℤ₂ with the pair of axes fixed by the potential, and for the full model: "With H dynamical as written: not established (C3)." (Step 3). The referee was reading the first version, whose potential was the naive form ([how spontaneous the breaking is](/wiki/symmetry-breaking/toy-models/coset-model/frozen-h-reduction#how-spontaneous-the-breaking-is)).

### What version 2 changed

Revision 1 required: "Use the bounded potential. Show it is stable with H dynamical" and "Present the Monte Carlo as the frozen-H reduction, explicitly." Version 2, applied on 2026-10-20 in commit 6606734, did both. Its simulation is headed "Monte Carlo of the frozen-H reduction" and says "H is not simulated." (§4), and "Ising-class breaking" became "an ordered ℤ₂ phase" ([Superseded: Ising-class breaking in model I](/wiki/symmetry-breaking/toy-models/coset-model/frozen-h-reduction#superseded-ising-class-breaking-in-model-i)). The simulation was rerun with four independent seeds, but for the reduction only.

### The rule it left

Round-4 lesson 1, as the root `CLAUDE.md` carries it ('Method'): "When numerics run on a reduced model (fields frozen), check the unreduced model's stability — boundedness, and the Hessian with all fields dynamical — and say in the text that it is a reduction. Round 4 found a potential that was bounded only at frozen H." The last sentence holds for the reduction as the documents define it, with K kept on its circle K(φ). With H held at 1 but K free on its hyperboloid, the naive potential is unbounded below at λ = μ = 1 and bounded only for λ ≥ 4μ; the flag's audit rated the sentence as depending on how "frozen H" is read (flag 40 in `review/wiki-build-flags.md`, awaiting Paul's ruling).

The rule asks for two things: a classical stability check of the unreduced model, and a statement of the reduction. It does not ask for the simulation to be repeated without the reduction. Both requirements were met ([the reduced-model stability rule](/wiki/method/verification/reduced-model-stability)); the simulation of the unreduced model is the part that remains open.

## What exists instead: the classical check

The referee, proposing V_b, added that "the vacuum analysis with H dynamical would have to be redone" (Step 3, point C3). The adjudicator redid it and ruled "This is the repair." ('Rulings' F2). Version 2 reports: "With H dynamical, (1, K_ref) is a stable minimum: Hessian eigenvalues 0, 0.764, 2, 5.236." (§4). The Hessian here is the matrix of second derivatives of the full potential, compatibility term included, at the vacuum, with the four field directions free: two for H and two along K's hyperboloid ([the spectrum](/wiki/symmetry-breaking/toy-models/coset-model/vacua#the-spectrum-three-flat-directions-and-one-massive)). [The gate](/wiki/method/verification/the-gate) prints [−0., 0.7639, 2., 5.2361] and passes "with V_b, (1, K_ref) is stable: Hessian eigenvalues >= 0 with exactly one zero" (`verify/toy_coset.py`). Both computations use one choice of couplings, λ = μ = 1: the gate's check names them, and the adjudicator's output reads "bounded variant (lam=1)" (`review/round4/adjudicator/arb.out`). On the boost family along which the naive form fell without limit, V_b rises instead; in the adjudication's words, "the boost family rises from −1 to −0.5" ('Rulings' F2). #11 records the result as "the vacuum is stable with H dynamical" (§14 item 11). The details are at [stability with H dynamical](/wiki/symmetry-breaking/toy-models/coset-model/bounded-potential#stability-with-h-dynamical).

### The flat line

One eigenvalue is zero. Version 2: "The zero mode is the classical flat line H = diag(y, 1/y), K = K_ref. It is not symmetry-protected, because V_b breaks the squeeze away from K = ±K_ref." (§4). The [vacuum manifold](/wiki/symmetry-breaking/topological-defects#the-vacuum-manifold-t) is "{diag(y, 1/y)} × {±K_ref}": the real structure is fixed up to sign, and the metric can still move along the line of diagonal metrics diag(y, 1/y), y > 0. The gate passes "the zero mode is the squeeze line H = diag(y, 1/y), K = K_ref: V = -1 all along it". The frozen-H reduction sits at one point of the line, y = 1.

The sources disagree about whether a symmetry protects the line. The adjudication called the zero mode "the residual diagonal squeeze, which is an exact symmetry" ('Rulings' F2). Flag 12 in `review/wiki-build-flags.md` reports a sympy check that finds V_b not invariant under the squeeze away from K = ±K_ref, and calls version 2's statement the accurate one; its audit adds: "The zero mode is an exact classical flat line, but the fluctuation masses vary along it, so no symmetry protects it." Version 2 also ranks above the adjudication in the wiki's source precedence, and the wiki follows it ([the vacuum manifold and the zero mode](/wiki/symmetry-breaking/toy-models/coset-model/bounded-potential#the-vacuum-manifold-and-the-zero-mode); [conflicts between sources](/wiki/history/documents/source-conflicts#postulates-and-the-toy-models), entry C28). The flag awaits Paul's ruling.

### What the check does not reach [T]

A Hessian describes the potential near one configuration of constant fields. Non-negative eigenvalues mean that no small displacement of the constant fields lowers the energy, to second order. The check says nothing about fields that vary from point to point and fluctuate, which is what a Monte Carlo samples, and so nothing about whether the order found in the reduction persists in the full model. A flat direction that comes from a broken symmetry stays flat when higher-order terms and quantum corrections are included; one that does not come from a symmetry has no such guarantee [T] ([Goldstone modes and the Higgs mechanism](/wiki/symmetry-breaking/goldstone-and-higgs)).

## How the full model differs from the reduction

The sources do not say whether the ordered phase survives when H fluctuates, and this page draws no conclusion. They do record three differences between the full model and the reduction.

- **The two fields are coupled.** K's kinetic term, (f_K²/4) Tr(H⁻¹ ∂Kᵀ H ∂K), is contracted with H, and the compatibility term ties K to H (note §2). At H = 1 the kinetic term reduces to the angle's stiffness, "(f_K^2/4)Tr(dK^T dK) = (1/2) f_K^2 (dphi)^2" (referee, Step 2(a)); with H free, the cost of a gradient in K depends on H ([the K kinetic term](/wiki/symmetry-breaking/toy-models/coset-model/action-and-symmetries#the-k-kinetic-term-and-the-ghost); [the two sectors are coupled](/wiki/symmetry-breaking/toy-models/coset-model/so2-question#the-two-sectors-are-coupled)).
- **The metric sector is non-compact.** On its own, the H sector is "the SO(1,2)/SO(2) hyperbolic sigma model" (referee, Step 3, point C2). Version 2: "The non-compact half-plane sector is a hyperbolic model, where symmetry breaking in 2D does occur [15]." (§4). Reference [15] is Niedermaier and Seiler, and Duncan, Niedermaier and Seiler, retrieved by live search in the worklog's prior-art survey [S]. The theorem by which the compact angle cannot order on its own in two dimensions applies to "the compact SO(2) containing ρ" (§4), not to this sector ([hyperbolic sigma models](/wiki/symmetry-breaking/toy-models/coset-model/sigma-models#hyperbolic-sigma-models-the-non-compact-exception); [the restriction to the compact SO(2)](/wiki/symmetry-breaking/mermin-wagner-coleman#model-i-the-restriction-to-the-compact-so2)).
- **A flat direction in H.** With V_b the classical vacua form the line of metrics diag(y, 1/y) times the pair ±K_ref, and the reduction holds H at the point y = 1 of that line. Along the line the potential is constant, but the line "is not symmetry-protected" (note §4), and "the fluctuation masses vary along it" (flag 12's audit).

### The related question without a potential

A separate open item asks whether the coupled model breaks ρ's SO(2) with no potential at all: "whether ρ's SO(2) breaks in the coupled model without a potential" (note §6; [Open: does ρ's SO(2) break in the coupled model?](/wiki/symmetry-breaking/toy-models/coset-model/so2-question)). Both items concern the coupled model. Without a potential the symmetry in question is the continuous SO(2) of rotations of the phase plane, which contains ρ; with V_b it is the ℤ₂ whose breaking the reduction shows, the choice between +K_ref and −K_ref. The note lists the two as separate items of "Not shown"; #11 §14 item 11 and the root `CLAUDE.md` name only the simulation with H dynamical.

## What would close it

The sources give no method for the simulation: no lattice form of the H field, no couplings, no expected result.

The standard that the reduced simulation was run to meet is [criterion S4](/wiki/symmetry-breaking/toy-models/success-criteria#tier-2-the-spirit), fixed before any construction: "The breaking survives quantum fluctuations in the stated dimension", where a pass "requires a citation-backed argument, and preferably a lattice simulation showing the order parameter stays nonzero" (worklog, `notes/toy-lagrangian.md`, 'Success criteria'). In this wiki's reading, the item is closed by a simulation of model I itself, with H fluctuating together with K, judged by that standard, whichever way the result comes out. An order parameter that keeps its value as the lattice grows would carry the ordered ℤ₂ phase from the reduction to model I; one that falls with lattice size would leave the ordered phase a property of the reduction.

Rules already in force would apply to such a run:

- "Monte Carlo numbers need error bars from independent runs. A fixed seed makes a number reproducible, not accurate." (root `CLAUDE.md`, 'Method'; [the Monte Carlo error-bar rule](/wiki/method/verification/monte-carlo-error-bars)).
- Round 4's ruling on start conditions, made after hot starts at L = 64 were found trapped in metastable domains in the reduction: "Cold starts are standard for ordered-phase measurements, but they must be stated." (`review/round4-adjudication.md`, 'Rulings'; [start conditions](/wiki/symmetry-breaking/toy-models/coset-model/monte-carlo#start-conditions-hot-starts-trap)).
- "New verification scripts get wired into" the gate, `scripts/check.sh` (root `CLAUDE.md`, 'The gate').

The item is not on the current work queue, which the root `CLAUDE.md` gives as `HANDOFF.md` §8 items 5–7 (the partially-massless comparison, the † literature battery and the phase-space-diameter note), followed by an optional round-5 review of the toy note, "but only before any external use". The sources record no attempt at the simulation.

## The claims it qualifies

- [Monte Carlo: an ordered ℤ₂ phase](/wiki/symmetry-breaking/toy-models/coset-model/monte-carlo), which stands for the frozen-H reduction only.
- [Acceptance criterion 1](/wiki/symmetry-breaking/toy-models/acceptance-criterion#open-the-parts-not-yet-met): its third part, "there is an ordered ℤ₂ phase in 1+1 in the frozen-H reduction (Monte Carlo)", which #11 counts toward the criterion being "Met in the referees' wording".
- [The frozen-H reduction](/wiki/symmetry-breaking/toy-models/coset-model/frozen-h-reduction), which states the scope of the lattice result.
- The open ends recorded for [the polarization as a Goldstone angle](/wiki/symmetry-breaking/goldstone-angle#open-what-the-toy-models-leave-undecided), for postulate [P2′](/wiki/program/postulates/p2-prime#open-the-extra-structure-the-refinement-needs) and for postulate [P5](/wiki/program/postulates/p5-spontaneous-selection#open-what-a-derived-selection-still-lacks), each of which lists this simulation.

## History

- **2026-10-19, chunk 3 of the worklog.** The reduction is made, and criterion S4 is reported to pass "only with the τ-type potential [V]", with ρ breaking as "a Z₂ (Ising class)" ('Chunk 3 results').
- **The first version of the note** (commit d9a06ac) simulates the angle at H = 1 without stating a reduction (v1 §4) and lists "Ising-class breaking of ρ in model I in 1+1" among its results; its list of what is "Not established" has no entry about H (v1 §6).
- **Round 4.** Findings F1 and F2 show that the naive potential is unbounded below once H moves and that "the Monte Carlo simulates a frozen-H reduction, not model I"; the referee proposes the bounded form, and the adjudicator rules it "the repair" ('Rulings' F1–F2; [review round 4](/wiki/method/review/round-4)).
- **Version 2 of the note**, applied on 2026-10-20 in commit 6606734: the bounded potential, the classical check with H dynamical, the "Monte Carlo of the frozen-H reduction", and "a Monte Carlo of model I with H dynamical" listed as not shown (§4, §6).
- **#11 v2.2** (amended 2026-10-20) records the criterion as met and "a Monte Carlo with H dynamical" as "Still open [O]" (§14 item 11). The root `CLAUDE.md` lists it first among the toy work's open ends.

## Sources

- `papers/broken-born-checkpoint-v2.md` §14 item 11 — the criterion's three parts and "Still open [O]: a Monte Carlo with H dynamical"
- `papers/reciprocity-toy-models.md` §2, §4, §6 — the fields and the Lagrangian; the simulated reduction and "H is not simulated", the classical check, the flat line, the hyperbolic sector and the theorem's restriction to the compact SO(2); "Shown" and "Not shown"
- `papers/reciprocity-toy-models.md` v1 (commit d9a06ac) §4, §6 — the reduction made without comment; the first version's results and its list of what was not established
- `review/round4-adjudication.md` 'Rulings' F1–F2 and the ruling on start conditions, 'Revisions' 1, 'Lessons' — the frozen-H finding, the repair and the adjudicator's reading of the zero mode; the required reframing; the reduced-model rule
- `review/round4/adjudicator/arb.out` — the bounded variant's Hessian at λ = 1
- `review/round4/referee/audit-notes.md` Step 2(a), Step 3 — the vacua that "exist only if H is frozen at 1" and the stiffness at H = 1; points C2 and C3, the proposal of V_b, and "not established" with H dynamical
- `verify/toy_coset.py` — the gated Hessian with H dynamical and the flat line
- `verify/toy_s4.py` — the frozen-H simulation
- `notes/toy-lagrangian.md` 'Success criteria', 'Chunk 3 results' — criterion S4 and its standard for a pass; the reduction as first made
- `CLAUDE.md` 'Since the handoff', 'Method', 'The gate' — the open end and the queue; the reduced-model and error-bar rules; new scripts wired into the gate
- `review/wiki-build-flags.md` item 12 — the zero mode's protection, with the audit; item 40 — "bounded only at frozen H", with the audit; both await Paul's ruling
