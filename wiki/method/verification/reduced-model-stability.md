---
title: "The reduced-model stability rule"
weight: 40
status: method
description: "When numerics run on a model with fields frozen, check the full model's boundedness and Hessian with all fields dynamical, and say in the text that it is a reduction — round 4's first lesson, from a potential checked only at frozen H and unbounded once H moves."
sources:
  - "CLAUDE.md 'Method'"
  - "review/round4-adjudication.md 'Lessons (into CLAUDE.md)'"
  - "review/round4-adjudication.md 'Rulings'"
  - "review/round4-adjudication.md 'Pre-registration scored'"
  - "review/round4-adjudication.md 'Revisions for v2 of the note (all accepted; applied 2026-10-20 in commit 6606734)'"
  - "review/round4-preregistration.md 'Predictions'"
  - "papers/reciprocity-toy-models.md §4"
  - "papers/reciprocity-toy-models.md §6"
  - "papers/broken-born-checkpoint-v2.md §10"
  - "papers/broken-born-checkpoint-v2.md §14 item 11"
  - "notes/toy-lagrangian.md 'Chunk 3 results (2026-10-19): S4, quantum stability'"
  - "verify/toy_coset.py"
  - "verify/toy_s4.py"
  - "review/wiki-build-flags.md items 12, 40"
  - "review/wiki-build-checks/squeeze_check.py"
  - "review/wiki-build-checks/frozen_h_naive.py"
---

*The reduced-model stability rule says that when a calculation simplifies a model by holding some of its fields fixed, the full model's stability must still be checked with every field free to move, and the text must say that the calculation used a reduction. Review round 4 supplied the reason: the potential first used in the program's [coset toy model](/wiki/symmetry-breaking/toy-models/coset-model) had been checked only with the phase-space metric H held fixed, and it is unbounded below once H is allowed to vary, so the model's intended vacuum was a saddle. The repaired potential was checked with all fields dynamical, and the toy-model note and its lattice script now name the simulation as a frozen-H reduction.*

**Status:** Method, in force (round-4 lesson 1, now in root `CLAUDE.md`) — untagged — applied in `verify/toy_coset.py`, which checks the bounded potential with H dynamical, and stated in `verify/toy_s4.py` and the [toy-model note](/wiki/symmetry-breaking/toy-models) §4.

## The rule

Root `CLAUDE.md`, 'Method': "When numerics run on a reduced model (fields frozen), check the unreduced model's stability — boundedness, and the Hessian with all fields dynamical — and say in the text that it is a reduction. Round 4 found a potential that was bounded only at frozen H."

The last sentence is right for the documents' frozen-H reduction, which holds H at 1 and also keeps the real structure K on its circle of compatible values K(φ). Read as holding H fixed alone, with K free, it is not: at the couplings λ = μ = 1 that `verify/toy_coset.py` uses, [the naive potential](/wiki/symmetry-breaking/toy-models/coset-model/naive-potential) is then unbounded below and its intended vacuum is a saddle, with the frozen-H Hessian eigenvalue −6 (flag 40 in `review/wiki-build-flags.md`, check `review/wiki-build-checks/frozen_h_naive.py`). The flag's audit rated it as depending on that reading.

Round-4 lesson 1, from which it comes: "When numerics run on a reduced model (some fields frozen), check the stability of the unreduced model — boundedness, and the Hessian with all fields dynamical — and state the reduction in the text." (`review/round4-adjudication.md`).

## Reduced models and stability [T]

This section is the wiki's reading of standard material [T].

A reduction fixes some fields of a model at chosen values and studies the rest. It is often the only way to simulate a model, and it is legitimate as long as the result is stated for the reduced model. The danger is in stability. A vacuum of a field theory is stable at the classical level when the potential is bounded below and the vacuum is a minimum: the Hessian, the matrix of second derivatives of the potential with respect to all the fields, has no negative eigenvalue there. Zero eigenvalues are flat directions, such as [Goldstone modes](/wiki/symmetry-breaking/goldstone-and-higgs).

Freezing fields restricts the potential to a slice of field space. A point can be a minimum on every slice the calculation looks at and still be a saddle of the whole, if the descending direction moves the frozen and the free fields together. A potential can likewise be bounded on the slice and unbounded off it. Only the Hessian over all fields, and a bound that holds for all field values, settles it.

## The episode: round 4

### The naive potential

[Model I](/wiki/symmetry-breaking/toy-models/coset-model) has two fields, a phase-space metric H and a real structure K. Its polarization is a [Goldstone angle](/wiki/symmetry-breaking/goldstone-angle) that [cannot order in 1+1 dimensions](/wiki/symmetry-breaking/mermin-wagner-coleman), so the note added a potential that keeps ρ and reduces the continuous symmetry to a discrete group ([the ρ-preserving potential](/wiki/symmetry-breaking/rho-preserving-potential)). The first choice, [the naive potential](/wiki/symmetry-breaking/toy-models/coset-model/naive-potential), was −μ[Tr(K K_ref)]². The worklog studied it at H = 1 on the circle of vacua K(φ), where it becomes "−2μ(1 + cos 2φ)", and the lattice simulation ran at H = 1 ('Chunk 3 results').

### What the referee found

Rulings F1 and F2, both upheld (`review/round4-adjudication.md`):

- **F1.** "The §4 potential −μ[Tr(K K_ref)]² is unbounded below in model I". The adjudicator's check: "along H = SᵀS, K = S⁻¹K₀S (S a boost), the λ-term is ~0 while V_μ = −4, −56.6, −2983, −8.9×10⁶ at t = 0, 1, 2, 4." Moving H and K together along a boost keeps the compatibility term at zero while the potential falls without limit.
- **F2.** "So (1, K_ref) is a saddle, and the Monte Carlo simulates a frozen-H reduction, not model I". The Hessian with H free "has a negative eigenvalue at λ = 1, 10, 100 (−6.47, −4.40, −4.04 in my coordinates)."

The adjudicator's comment: "I should have caught F1 myself: I checked the potential only at frozen H." See [Obituary: the naive ρ-preserving potential](/wiki/symmetry-breaking/toy-models/coset-model/naive-potential) and [Review round 4](/wiki/method/review/round-4).

### What the pre-registration expected

The round-4 pre-registration had named the right place: "in 1+1, the "spontaneous" breaking of ρ rests on an explicit, rigid background" (K_ref). The outcome was scored "**Partial**: right location, missed severity", with the summary "Weakest-link location has improved. Severity is still underestimated." ([Pre-registration and its calibration record](/wiki/method/review/pre-registration)).

## The repair, checked with all fields free

Revision 1 of the note: "Use the bounded potential. Show it is stable with H dynamical (local minimum up to the exact residual squeeze)." The note v2, §4: "The normalized form V_b = −μ[Tr(K K_ref)]² / (2 Tr KᵀK) is bounded, −μ ≤ V_b ≤ 0 by Cauchy–Schwarz, since Tr K_refᵀK_ref = 2", and "With H dynamical, (1, K_ref) is a stable minimum: Hessian eigenvalues 0, 0.764, 2, 5.236." See [the bounded potential V_b](/wiki/symmetry-breaking/toy-models/coset-model/bounded-potential).

`verify/toy_coset.py` checks the repair under the heading "The bounded rho-preserving potential, with H dynamical (round-4 repair)":

```text
PASS  Tr(Kref^T Kref) = 2, so Cauchy-Schwarz gives -1 <= V_b <= 0
PASS  sampled V_b stays in [-1, 0] on the hyperboloid  [min -0.9770]
PASS  the unnormalized potential makes (1, K_ref) a saddle (negative Hessian eigenvalue)  [[-6.472  0.     2.472  8.   ]]
PASS  with V_b, (1, K_ref) is stable: Hessian eigenvalues >= 0 with exactly one zero  [[-0.      0.7639  2.      5.2361]]
PASS  quoted: unbounded below - at boost t = 4 the compatibility term is ~0 and -[Tr(K K_ref)]^2 = -8.9e6  [-8.8861e+06]
PASS  the zero mode is the squeeze line H = diag(y, 1/y), K = K_ref: V = -1 all along it
PASS  boosts are penalized: V_b rises from -1 toward -1/2 along the boost family  [[-1.     -0.6329 -0.5183 -0.5   ]]
```

The Hessians are taken over all four field coordinates, two for H and two for K, so they are the unreduced check the rule asks for. Their scope is a single point, (1, K_ref), at λ = μ = 1, computed by finite differences; the eigenvalues at λ = 10 and 100 are the adjudicator's and are not gated. The bound is checked through its input, Tr(K_refᵀK_ref) = 2, and by sampling 20000 points on K's hyperboloid; the Cauchy–Schwarz inequality is the note's argument. See [the toy-model scripts](/wiki/method/verification/toy-model-scripts).

## Saying it is a reduction

The second half of the rule is about the text:

- The note's heading reads "Monte Carlo of the frozen-H reduction", with "H is not simulated" (§4).
- The docstring of `verify/toy_s4.py`: `This is the FROZEN-H reduction of the coset toy (H = 1 held fixed); the unreduced model's stability with the bounded potential V_b is checked in toy_coset.py.` Its closing line: "OK — S4: rho is spontaneously broken in 1+1 (frozen-H reduction) only with the rho-preserving potential."
- #11 §14 item 11 records "an ordered ℤ₂ phase in 1+1 in the frozen-H reduction (Monte Carlo)", and §10 adds: "That potential must be bounded with all fields dynamical — the round-4 review found the naive form unbounded once H moves".

See [the frozen-H reduction](/wiki/symmetry-breaking/toy-models/coset-model/frozen-h-reduction) and [Monte Carlo: an ordered ℤ₂ phase](/wiki/symmetry-breaking/toy-models/coset-model/monte-carlo).

## The zero mode: where the sources disagree

The stable minimum keeps one zero eigenvalue, along the line H = diag(y, 1/y), K = K_ref. The adjudication called it "the residual diagonal squeeze, which is an exact symmetry" (F2), and revision 1 speaks of "the exact residual squeeze". The note v2 says instead: "It is not symmetry-protected, because V_b breaks the squeeze away from K = ±K_ref." The gate checks only that the line is flat (`V = -1 all along it`), which both statements agree on.

The wiki build applied the rule's question, whether a property seen on a slice holds off it, to this disagreement. Its executed check, `review/wiki-build-checks/squeeze_check.py`, applies the squeeze to a general K and prints, besides the general formula for the change:

```text
lambda-term invariant under squeeze: True
numeric example (a=2, K=[[1/2,1],[3/4,-1/2]]): V_b change = 320/1683
on the line K = K_ref: 0
```

The squeeze leaves the λ-term unchanged and V_b unchanged on the line K = K_ref, but changes V_b off it, so the flat direction is not a symmetry of the potential. Flag 12 in `review/wiki-build-flags.md` records this and calls the note's statement the accurate one. In the wiki's precedence the note (rank 2) also outranks the adjudication (rank 3), so the wiki follows the note; the adjudication's wording stands in the record unamended, pending Paul's ruling on the flag.

## What the rule leaves open

The rule was satisfied for the classical vacuum, not for the simulation: the Monte Carlo is still of the reduced model. The note lists "a Monte Carlo of model I with H dynamical" as not shown (§6), and #11 §14 item 11 keeps it open: "Still open [O]: a Monte Carlo with H dynamical". It is registered on [the frozen-H reduction](/wiki/symmetry-breaking/toy-models/coset-model/frozen-h-reduction#open-a-monte-carlo-with-h-dynamical) and under [acceptance criterion 1](/wiki/symmetry-breaking/toy-models/acceptance-criterion). Related, and also open: whether ρ's SO(2) breaks in the coupled model without a potential ([Open: does ρ's SO(2) break in the coupled model?](/wiki/symmetry-breaking/toy-models/coset-model/so2-question)).

## Sources

- Root `CLAUDE.md` 'Method' — the rule
- `review/round4-adjudication.md` 'Lessons (into CLAUDE.md)' (lesson 1), 'Rulings' (F1, F2), 'Pre-registration scored', 'Revisions for v2 of the note' (revision 1) — the failure, the adjudicator's comment, the scored prediction, the repair asked for
- `review/round4-preregistration.md` 'Predictions' — the predicted weakest link
- `papers/reciprocity-toy-models.md` §4 — the bounded potential, the zero mode, the reduction stated; §6 — what is not shown
- `papers/broken-born-checkpoint-v2.md` §10, §14 item 11 — the result as #11 records it, and the open Monte Carlo
- `notes/toy-lagrangian.md` 'Chunk 3 results (2026-10-19): S4, quantum stability' — the potential as first studied at H = 1
- `verify/toy_coset.py` — the gated saddle, the stable minimum, the flat line; `verify/toy_s4.py` — the reduction stated in the script
- `review/wiki-build-flags.md` item 12 and `review/wiki-build-checks/squeeze_check.py` with its `.out` — the zero mode is not a symmetry
- `review/wiki-build-flags.md` item 40 and `review/wiki-build-checks/frozen_h_naive.py` — the rule's last sentence read with only H held fixed, and the audit's verdict; awaiting Paul's ruling
