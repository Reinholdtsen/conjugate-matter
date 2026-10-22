---
title: "Open: does ρ's SO(2) break in the coupled model?"
weight: 80
status: open
description: "In 1+1 the compact polarization angle cannot order by itself (Mermin–Wagner–Coleman), but model I's metric sector is a hyperbolic sigma model, which can break in two dimensions; whether the full coupled model breaks ρ's SO(2) without a potential is open."
sources:
  - "papers/reciprocity-toy-models.md §1"
  - "papers/reciprocity-toy-models.md §4"
  - "papers/reciprocity-toy-models.md §6"
  - "papers/reciprocity-toy-models.md v1 (commit d9a06ac) §1, §4"
  - "review/round4-adjudication.md 'Rulings'"
  - "review/round4-adjudication.md 'Revisions' 1"
  - "review/round4/referee/audit-notes.md Step 1"
  - "review/round4/referee/audit-notes.md Step 3"
  - "notes/toy-lagrangian.md 'Success criteria'"
  - "notes/toy-lagrangian.md 'Predictions'"
  - "notes/toy-lagrangian.md 'Chunk 1 results'"
  - "notes/toy-lagrangian.md 'Chunk 2 results'"
  - "notes/toy-lagrangian.md 'Chunk 3 results'"
  - "notes/toy-lagrangian.md 'Assessment against the predictions'"
  - "papers/broken-born-checkpoint-v2.md §14 item 11"
  - "verify/toy_s4.py"
---

*The open question is whether [model I](/wiki/symmetry-breaking/toy-models/coset-model), with its metric field H free to vary and no added potential, [spontaneously breaks](/wiki/symmetry-breaking/spontaneous-symmetry-breaking) the rotation group SO(2) of the phase plane, the circle of symmetries that contains [Born reciprocity](/wiki/phase-space/reciprocity/born-reciprocity) ρ. Breaking it would mean that the vacuum settles on one polarization angle despite quantum fluctuations. In two dimensions a compact continuous symmetry cannot break on its own ([the Mermin–Wagner–Coleman theorem](/wiki/symmetry-breaking/mermin-wagner-coleman)), so the polarization angle by itself cannot order. But model I's metric sector is a hyperbolic sigma model, a known case in which a non-compact symmetry does break in two dimensions, and the two sectors are coupled. [Round 4](/wiki/method/review/round-4) required the toy-model note to restrict the theorem to the compact SO(2) and to state the coupled case as open; the note lists it as not shown.*

**Status:** Open — untagged — raised by the round-4 referee (conceptual point C2), upheld as a literature point in the adjudication, and listed under "Not shown" in version 2, §6. Registered at [open problems](/wiki/status/open-problems).

## The question

Version 2 of the [toy-model note](/wiki/symmetry-breaking/toy-models): "Whether ρ's SO(2) stays unbroken in the full coupled model is open." (§4). Its list of what is "Not shown" includes "whether ρ's SO(2) breaks in the coupled model without a potential" (§6).

ρ's SO(2) is the group of rotations of the (x, p) plane. Among the [symplectic maps](/wiki/phase-space/reciprocity/symplectic-form) they are the ones that leave the metric H = 1 unchanged, the stabilizer of the point Z = i of the upper half-plane [T] ([the Siegel domain](/wiki/phase-space/modular-field/siegel-domain)). Acting on the real structure, they turn K around its circle of vacua K(φ), and ρ is the quarter-turn among them. The worklog calls this circle group "the U(1) stabilizer of H that rotates K" ('Chunk 2 results'); SO(2) and U(1) are the same group [T]. If SO(2) broke spontaneously, the vacuum would hold one definite angle φ, one definite polarization. "Without a potential" means with model I's own three terms only ([Model I: action and symmetries](/wiki/symmetry-breaking/toy-models/coset-model/action-and-symmetries)).

## What is known

### The compact angle by itself cannot order

"In 1+1 the compact angle φ cannot order: Mermin–Wagner [13, 14] applies to the compact SO(2) containing ρ." (§4). In two dimensions the long-wavelength fluctuations of a compact angle grow without limit and wash out any preferred value [T]. The lattice simulation of the angle with H frozen shows this: without the potential the order decays with lattice size, "⟨|M|⟩ = |⟨e^{iφ}⟩| = 0.8369 ± 0.0007, 0.8025 ± 0.0039, 0.7736 ± 0.0038" at L = 16, 32, 64, read as "No true order" (§4; `verify/toy_s4.py`, see [the toy-model scripts](/wiki/method/verification/toy-model-scripts); [Monte Carlo: an ordered ℤ₂ phase](/wiki/symmetry-breaking/toy-models/coset-model/monte-carlo#without-the-potential-no-true-order)).

### The metric sector can break

"The non-compact half-plane sector is a hyperbolic model, where symmetry breaking in 2D does occur [15]." (§4). The round-4 referee's point C2: "Model I's group Sp(2,R) is non-amenable and its H-sector is the SO(1,2)/SO(2) hyperbolic sigma model", for which Duncan, Niedermaier and Seiler report spontaneous breaking in two dimensions, "For D=2 this shows that the systems evade the Mermin-Wagner theorem" (`review/round4/referee/audit-notes.md`, Step 3). The literature is explained at [coset and hyperbolic sigma models](/wiki/symmetry-breaking/toy-models/coset-model/sigma-models#hyperbolic-sigma-models-the-non-compact-exception).

### The two sectors are coupled

In model I the two sectors do not decouple. K's kinetic term is contracted with H, and the compatibility potential ties K to H ([the K kinetic term](/wiki/symmetry-breaking/toy-models/coset-model/action-and-symmetries#the-k-kinetic-term-and-the-ghost)). The theorem speaks about a compact symmetry, and the hyperbolic result about a non-compact one; the adjudication accordingly restricts the theorem and leaves the coupled case open: "The Mermin–Wagner statement must be restricted to the compact SO(2) containing ρ. Whether that SO(2) is broken in the coupled model is open." (`review/round4-adjudication.md`, 'Rulings', "Mermin–Wagner vs [11]"; [11] is the first version's number for reference [15]).

## How the question arose

The worklog anticipated the issue when it fixed [criterion S4](/wiki/symmetry-breaking/toy-models/success-criteria): "A continuous compact one cannot (Coleman–Mermin–Wagner), though there is a claimed exception for non-amenable groups, to be checked." ('Success criteria'). Its forecast: "S4 will pass only for a discrete reduction (the symmetry group cut down to the group generated by ρ) or via the non-amenability exception. The continuous U(1) of phase-space rotations that contains ρ would be restored in 1+1." ('Predictions').

After the first construction it wrote: "S4 is the open question. The breaking is continuous, so in 1+1 the compact circle mode should restore ⟨K⟩ (Coleman–Mermin–Wagner) unless the non-amenable directions change that. Waiting on the S0 literature check." ('Chunk 1 results'). The prior-art survey retrieved the hyperbolic-model papers [S], and the worklog listed two ways forward: a discrete reduction by a potential, "Or the non-amenability route (Duncan–Niedermaier–Seiler), whose applicability to this target is unchecked." It took the first ([Obituary: the naive ρ-preserving potential](/wiki/symmetry-breaking/toy-models/coset-model/naive-potential)). The assessment records the second as "Non-amenability not needed, not tested" ('Assessment against the predictions').

Round 4 returned to it. The referee's point C2 continues: "The statement must be restricted to the compact SO(2) containing rho, with an argument." (Step 3). The adjudication upheld the point from the literature, and revision 1 required version 2 to "Restrict Mermin–Wagner to the compact SO(2)" and to cite the hyperbolic-model papers "for the hyperbolic H-sector, noting the open question". Version 2, applied on 2026-10-20, does both (§4, §6).

## Superseded: the first version's unrestricted theorem

The first version of the note (commit d9a06ac) stated the theorem for continuous symmetries in general, with non-amenable groups as an exception, and then applied it to the whole of model I's continuous breaking without that exception. Its §1: "Continuous symmetries cannot break spontaneously in two dimensions [9, 10]. Non-amenable groups are an exception [11]." Its §4: "In the exactly symmetric model the continuous breaking is forbidden [9, 10]." In that numbering [9, 10] are Mermin–Wagner and Coleman, and [11] is the hyperbolic-model pair, now [13, 14] and [15].

The referee found the two sections at odds: §4's statement "ignores [11] for model I's own (non-amenable) Sp(2,R)" (Step 1). Version 2 replaces it with the restricted statement quoted above, and the change is listed among the [superseded statements](/wiki/status/superseded).

## What the note does instead

Version 2 obtains a definite polarization without answering the question, in two steps. It adds a potential: "To get a definite polarization we add a potential that is invariant under ρ and under K → −K, and reduces the U(1) to a discrete group." (§4; [the bounded potential V_b](/wiki/symmetry-breaking/toy-models/coset-model/bounded-potential)). And it simulates the angle with H frozen, where the reduced symmetry orders: "an ordered ℤ₂ phase in the frozen-H reduction in 1+1" (§6; [the frozen-H reduction](/wiki/symmetry-breaking/toy-models/coset-model/frozen-h-reduction)). The program's one ordered phase is therefore obtained with an explicit potential in a [reduced model](/wiki/method/verification/reduced-model-stability). The coupled model without a potential has been neither simulated nor analysed.

The worklog's third unpredicted finding was stated for 1+1: "In 1+1, 'only ω rigid' is not enough for a definite polarization. A ρ-preserving potential on the polarization circle is required." ('Assessment against the predictions'). Version 2 keeps the coupled case apart, listing "whether ρ's SO(2) breaks in the coupled model without a potential" as not shown.

## What the sources leave unsaid

The sources give no method for settling the question and no expectation for its answer. The note lists it beside "a Monte Carlo of model I with H dynamical" (§6), which [#11](/wiki/history/documents/checkpoint) §14 item 11 also keeps open [O] ([the frozen-H reduction](/wiki/symmetry-breaking/toy-models/coset-model/frozen-h-reduction#open-a-monte-carlo-with-h-dynamical)); the note lists the two as separate items. The worklog's separate remark that the continuous breaking is allowed in 3+1 dimensions, where the theorem does not apply, is an uncomputed remark recorded at [the polarization as a Goldstone angle](/wiki/symmetry-breaking/goldstone-angle); the note covers only 1+1 with d = 1.

## Sources

- `papers/reciprocity-toy-models.md` §1, §4, §6 — the theorem and its exception, the restricted statement, the open question and the "Not shown" list
- `papers/reciprocity-toy-models.md` v1 (commit d9a06ac) §1, §4 — the unrestricted statement, now superseded
- `review/round4-adjudication.md` 'Rulings' ("Mermin–Wagner vs [11]"), 'Revisions' 1 — upheld (literature); the required restriction
- `review/round4/referee/audit-notes.md` Step 1, Step 3 — the hyperbolic-model citation and its non-application in v1; conceptual point C2
- `notes/toy-lagrangian.md` 'Success criteria', 'Predictions', 'Chunk 1 results', 'Chunk 2 results', 'Chunk 3 results', 'Assessment against the predictions' — criterion S4, the forecast, the framing as "the open question", the U(1) stabilizer, and the non-amenability verdict
- `papers/broken-born-checkpoint-v2.md` §14 item 11 — the Monte Carlo with H dynamical kept open [O]
- `verify/toy_s4.py` — the run without the potential
