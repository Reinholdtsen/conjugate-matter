---
title: "Open: the real model's one-loop preference (a lead)"
weight: 70
status: open
description: "The real model's two sign-vacua are classically degenerate but split at one loop, F(+) − F(−) = 2.634 at N = 6, 8, 10, in favour of the position-sharp one: an explicit, not spontaneous, selection, not yet followed through renormalization."
sources:
  - "CLAUDE.md 'Since the handoff'"
  - "papers/reciprocity-toy-models.md §3"
  - "papers/reciprocity-toy-models.md §4"
  - "papers/reciprocity-toy-models.md §6"
  - "verify/toy_gw.py"
  - "review/round4-adjudication.md 'Rulings' F4"
  - "review/round4-adjudication.md 'Revisions' 3"
  - "review/round4/adjudicator/arb.out"
  - "review/round4/referee/audit-notes.md Step 2(b)"
  - "review/round4/referee/audit-notes.md Step 3"
  - "review/round4/referee/out_model2_vac.txt"
  - "notes/toy-lagrangian.md 'Chunk 1 results'"
  - "notes/toy-lagrangian.md 'Write-up and review'"
---

*In the real-field version of [model II](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar) the vacua are discrete: the two condensed oscillator levels carry either the same sign or opposite signs, and the duality maps one choice to the other. The two have exactly the same classical action, but the quantum fluctuations around them differ, and at one loop the free energy is lower for the opposite-sign vacuum, which is the one sharper in position than in momentum. That is a selection of the position-sharp polarization, but an explicit one: the real model is not symmetric under the duality, because its field is real in position, so nothing is broken spontaneously. The round-4 referee found the split, the adjudicator identified which vacuum it favours, and the toy-model note's second version showed the value unchanged at three truncations. It is recorded as a lead, not a result: it holds at a fixed bare mass, and its fate in the renormalized large-N limit is not known.*

**Status:** Open — "a lead" (root `CLAUDE.md`), untagged in the sources. It is round-4 finding F4, "Upheld, with a consequence the referee did not draw" ([review round 4](/wiki/method/review/round-4)); the split, its sign at N = 6, 8 and 10 and the identification of the preferred vacuum are gated in `verify/toy_gw.py` ([the toy-model scripts](/wiki/method/verification/toy-model-scripts)). "The large-N, renormalized fate of the real model's one-loop selection" is listed as not shown. Registered at [open problems](/wiki/status/open-problems).

## The statement

The toy-model note, version 2 (§3):

> - The vacua are diag(±√q₀, ±√q₁). Up to the global sign, the two relative signs are classically degenerate (S = −2.5) but have different fluctuation spectra.
> - Their one-loop Gaussian free energies differ by F(+) − F(−) = 2.634. The value is the same at truncations N = 6, 8, 10, because the sign-dependent term involves only the modes coupling levels 0 and 1.
> - **The preferred vacuum, diag(a₀, −a₁), is the β = π configuration, the one sharper in position.**
> - This is explicit, not spontaneous selection, because the real model is not duality-symmetric: its field is real in position. It holds at fixed bare μ², and is not followed through renormalization (§4).

## The real model's vacua

A field that is real on the noncommutative plane is a Hermitian matrix on the matrix base, with quartic term Tr φ⁴ ([the matrix base and the action](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/model-and-matrix-base)). The worklog explained in chunk 1 why its minima are diagonal: "At Ω = 1 the matrix-base action depends on φ only through φ² ... With distinct level energies, every minimum is then diagonal, φ = diag(±√q_m) over the condensed levels." ('Chunk 1 results'). The occupations are those of the complex model, q₀ = 1.5 and q₁ = 0.5 at μ² = 4 and λ = 1 ([complex-model vacua](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/complex-vacua)), with a₀ = √q₀ and a₁ = √q₁.

A real entry has no phase, only a sign. The action is even in φ, so flipping both signs changes nothing, and two vacua remain:

```text
v+ = diag(a₀, +a₁)        the β = 0 configuration
v− = diag(a₀, −a₁)        the β = π configuration
```

They are the two points β = 0 and β = π of the complex model's vacuum circle; the rest of the circle is not available to a real field. A diagonal matrix commutes with the parity matrix Π, so the duality keeps these vacua real and exchanges them: "for diagonal phi, Pi phi stays Hermitian, so the duality maps v+ = diag(a0,a1) to v- = diag(a0,-a1), classically degenerate (S_r = -2.5 both)" (the round-4 referee, audit notes, Step 2(b); [complex versus real fields](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/complex-and-real-fields#the-vacua-it-does-relate)).

## Equal action, different fluctuations

The duality exchanges the two vacua but not the fluctuations around them. A fluctuation of a real field is a general Hermitian matrix, and the duality takes such a matrix out of the real field space, so nothing requires the fluctuation spectra at v+ and v− to agree. The referee: "But the fluctuation spectra differ" (audit notes, Step 2(b)). In the complex model, where the duality is a symmetry, they agree exactly: "complex model: max |eig(v+) - eig(v-)| = 0.0" (`review/round4/referee/out_model2_vac.txt`). The gate confirms that both real vacua are true local minima: "both sign-vacua have the same classical action (-2.5) and positive-definite Hessians".

The referee and the adjudicator both printed the lowest Hessian eigenvalues at the two vacua, and the adjudicator noted that "the referee's normalization is half of mine" ('Rulings' F4). The two lists are not reconciled mode by mode, so this page quotes only the free-energy difference, which does not depend on the normalization.

## The one-loop free energy

In the Gaussian, or one-loop, approximation the action is expanded to second order about a vacuum, and the integral over fluctuations is done exactly [T]. The result, the one-loop free energy, is the classical action plus half the sum of the logarithms of the Hessian's eigenvalues, up to constants that are the same for every vacuum [T]. A vacuum whose fluctuations are softer, with smaller eigenvalues, has more room to fluctuate and so a lower free energy. Here the classical actions are equal, so only the logarithms differ. The gate computes the difference as half the difference of the two sums of logarithms; the adjudicator's output notes that "eigenvalue-normalization dependent constants cancel" (`review/round4/adjudicator/arb.out`).

```text
F(+) − F(−) = 2.634        at N = 6, 8 and 10        (note §3; verify/toy_gw.py)
```

The values in the record:

- the referee, at N = 8: "one-loop free energies differ by 2.633916" (`review/round4/referee/out_model2_vac.txt`);
- the adjudicator, at N = 8: "F(+) − F(−) = 2.634, exactly the referee's number" ('Rulings' F4; `arb.out`);
- the gate, at each truncation: "N= 6: ... F(+) - F(-) = 2.634", and the same at N = 8 and N = 10. It asserts the value at N = 8 ("F(+) - F(-) = 2.634 at N = 8 (matching the round-4 referee)") and the sign at all three ("F(+) > F(-) at N = 6, 8, 10: the opposite-sign vacuum diag(a0, -a1) is preferred at one loop").

The difference is positive, so v− has the lower free energy. The note explains why the value does not move with the truncation: "the sign-dependent term involves only the modes coupling levels 0 and 1" (§3).

## Which vacuum is preferred

The adjudicator drew the consequence the referee had not: "**The lower free energy belongs to diag(a₀, −a₁), the β = π vacuum, which is the one sharper in position** (Δ(π) = −Δ(0) < 0). The real model therefore selects the position-sharp polarization at one loop." ('Rulings' F4).

The identification rests on the polarization Δ(β) = ⟨x²⟩_vacuum − ⟨x²⟩_dual = Δ(0) cos β of the complex model, with Δ(0) > 0: β = 0 is broader in position than in momentum, and β = π, its image, is sharper in position ([complex-model vacua](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/complex-vacua)). That sign was written reversed in the worklog's first draft and corrected before the review; the referee confirmed the corrected sign independently ([the reversed sign](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/complex-vacua#superseded-the-reversed-sign-of-the-polarization)). The gate checks the identification: "diag(a0, -a1) is the beta = pi vacuum, i.e. the one sharper in x (Delta(pi) = -Delta(0) < 0)".

## Explicit, not spontaneous

In [spontaneous symmetry breaking](/wiki/symmetry-breaking/spontaneous-symmetry-breaking) the laws are symmetric and the vacuum is not; the symmetry keeps the vacua exactly degenerate, and the choice among them is not made by the laws. In explicit breaking the laws themselves favour one outcome [T]. The real model is of the second kind. "This is explicit, not spontaneous selection, because the real model is not duality-symmetric: its field is real in position." (§3). Requiring the field to be real is a condition stated in the position description; the duality's image of a real field is not real ([complex versus real fields](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/complex-and-real-fields)), so the model does not treat the two descriptions alike, and the one-loop preference for the position-sharp vacuum reflects that asymmetry.

The program's hard core claims a spontaneous selection: an exactly symmetric law whose vacuum picks position ([the hard core](/wiki/program/hard-core); [P5](/wiki/program/postulates/p5-spontaneous-selection), which postulates that ours is the x-tilted vacuum). The real model shows a field theory in which the position-sharp vacuum wins, but by a law that already distinguishes position.

## Why it is a lead and not a result

The adjudication: "It is recorded as a lead, not a result: truncation dependence and its interpretation are unchecked." ('Rulings' F4). Version 2 has since checked the truncation over a range: the same value at N = 6, 8 and 10 (§3). Two things remain open.

- **Renormalization.** The split "holds at fixed bare μ², and is not followed through renormalization" (§3). In this model the bare μ² is itself renormalized: the level-0 tadpole grows with N, "so fixed bare μ² is not a consistent large-N limit" (§4; [the bare mass runs with the truncation](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/quantum-restoration#caveat-1-the-bare-mass-runs-with-the-truncation)). A computation at fixed bare μ² therefore does not settle what happens as N grows. The note lists "the large-N, renormalized fate of the real model's one-loop selection" under "Not shown" (§6).
- **Interpretation.** What the selection means is the second unchecked item of the ruling, and no later document addresses it. Version 2 states only that the selection is explicit.

The root `CLAUDE.md` lists it among the open ends of the toy Lagrangian as "the real Grosse–Wulkenhaar model's one-loop preference for the position-sharp vacuum, a lead", beside those of [acceptance criterion 1](/wiki/symmetry-breaking/toy-models/acceptance-criterion). Checkpoint #11 does not mention it; this is an absence rather than a conflict between the documents.

## What it qualifies: the Goldstone angle is model-specific

The finding also limits a generalization. Where the duality sits inside a continuous U(1), as in model I and the complex model II, the polarization is an angle on a circle of degenerate vacua ([the polarization as a Goldstone angle](/wiki/symmetry-breaking/goldstone-angle)). The real model has no such circle. The referee: "So in the real model the polarization is a discrete classical choice lifted explicitly at one loop -- not a Goldstone angle." The first version of the note had said that "in both models" ρ is one element of a continuous U(1), and the referee found this "true of the two models chosen, not of the [Grosse–Wulkenhaar] model the duality literature is about" (audit notes, Step 2(b), capitals lowered in "discrete"). The adjudication's revision 3: "Restrict 'Goldstone angle' to the complex model." and "Add F4 (the real model's discrete, one-loop-lifted vacua) as a lead."

## History

- **Found in round 4.** The referee reported it as an "ADDITIONAL FINDING (supports the manuscript's real/complex distinction, but shows the 'Goldstone angle' structure is model-specific)", with the split computed at N = 8 (audit notes, Step 2(b); Step 3: "free energies differ by 2.634 at N=8").
- **Upheld, with its consequence.** The adjudication upheld F4 "with a consequence the referee did not draw": that the preferred vacuum is the position-sharp one ('Rulings' F4).
- **Into version 2.** The worklog's record of the revisions: "the real model's discrete vacua, split at one loop (ΔF = 2.634 at N = 6, 8, 10) in favour of the position-sharp one — a lead" ('Write-up and review'). It deferred a fifth review round: "No round 5 for now. v2 fixes and narrows claims rather than adding new ones; the real-model lead is labelled as a lead."
- **Into the gate.** The adjudicator's script, `review/round4/adjudicator/arb.py`, stays in `review/round4/adjudicator/` and is not run by the gate; the F4 check was carried into `verify/toy_gw.py`, in the section "Real model: the two sign-vacua are classically degenerate but split at one loop (round-4 F4)".

## Sources

- `CLAUDE.md` 'Since the handoff' — its status as an open end and "a lead"
- `papers/reciprocity-toy-models.md` §3, §4, §6 — the vacua, the one-loop split and its limits, quoted above; the tadpole; "Not shown"
- `verify/toy_gw.py` — the gated split at N = 6, 8, 10, its asserted value and sign, and the identification of the preferred vacuum
- `review/round4-adjudication.md` 'Rulings' F4, 'Revisions' 3 — upheld, the β = π identification, "a lead, not a result"; the restriction of "Goldstone angle"
- `review/round4/adjudicator/arb.out` — the adjudicator's free-energy difference at N = 8 and the cancelling constants
- `review/round4/referee/audit-notes.md` Step 2(b), Step 3 — the referee's finding F4 and its reading of the Goldstone-angle claim
- `review/round4/referee/out_model2_vac.txt` — the referee's printed split and the identical complex-model spectra
- `notes/toy-lagrangian.md` 'Chunk 1 results', 'Write-up and review' — why the real model's minima are diagonal; the lead as added in version 2
