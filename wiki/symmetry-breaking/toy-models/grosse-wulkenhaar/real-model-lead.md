---
title: "Open: the real model's one-loop preference (a lead)"
weight: 70
status: open
description: "The real model's two sign-vacua are classically degenerate but split at one loop, F(+) − F(−) = 2.634, in favour of the position-sharp one: explicit, not spontaneous, selection, not followed through renormalization."
sources:
  - "CLAUDE.md 'Since the handoff'"
  - "papers/reciprocity-toy-models.md §3"
  - "papers/reciprocity-toy-models.md §6"
  - "verify/toy_gw.py"
  - "review/round4-adjudication.md 'Rulings' F4"
  - "review/round4/adjudicator/arb.out"
  - "review/round4/referee/audit-notes.md Step 2(b)"
  - "review/round4/referee/audit-notes.md Step 3"
---

*In the real-field version of [model II](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar), the two vacua that differ only in the relative sign of their two condensed levels have exactly the same classical action, but the quantum fluctuations around them differ, and at one loop the free energy is lower for the vacuum that is sharper in position. That is a selection of the position-sharp polarization, but an explicit one: the real model is not symmetric under the duality, because its field is real in position, so nothing is broken spontaneously. The round-4 referee found the split, the adjudicator identified which vacuum it favours, and the result is recorded as a lead: it holds at fixed bare mass and has not been followed through renormalization.*

**Status:** Open, "a lead" (root `CLAUDE.md`) — untagged — round-4 finding F4, "Upheld, with a consequence the referee did not draw"; the numbers are gated in `verify/toy_gw.py` ([the toy-model scripts](/wiki/method/verification/toy-model-scripts)), and the large-N, renormalized fate is listed as not shown. Registered at [open problems](/wiki/status/open-problems).

## Key facts

- **Two vacua, one action.** "The vacua are diag(±√q₀, ±√q₁). Up to the global sign, the two relative signs are classically degenerate (S = −2.5) but have different fluctuation spectra."
- **The split.** "Their one-loop Gaussian free energies differ by F(+) − F(−) = 2.634. The value is the same at truncations N = 6, 8, 10, because the sign-dependent term involves only the modes coupling levels 0 and 1." The gate prints 2.634 at all three truncations. The referee's and the adjudicator's eigenvalue lists differ by a normalization ("the referee's normalization is half of mine"), so only the difference F(+) − F(−) is quoted.
- **Which vacuum.** "The preferred vacuum, diag(a₀, −a₁), is the β = π configuration, the one sharper in position" (Δ(π) = −Δ(0) < 0; [complex-model vacua](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/complex-vacua)). The adjudication: "The real model therefore selects the position-sharp polarization at one loop."
- **Explicit, not spontaneous.** "This is explicit, not spontaneous selection, because the real model is not duality-symmetric: its field is real in position. It holds at fixed bare μ², and is not followed through renormalization." ([complex versus real fields](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/complex-and-real-fields); [spontaneous symmetry breaking](/wiki/symmetry-breaking/spontaneous-symmetry-breaking))
- **Why a lead, not a result.** The adjudication: "It is recorded as a lead, not a result: truncation dependence and its interpretation are unchecked." Version 2 has since shown the value unchanged at N = 6, 8, 10. What remains is "the large-N, renormalized fate of the real model's one-loop selection" (version 2, §6, "Not shown"); the level-0 tadpole grows with N, so a fixed bare μ² is not a consistent large-N limit ([quantum restoration](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/quantum-restoration)).
- **What it qualifies.** The referee's finding shows that the Goldstone-angle structure is model-specific: in the real model, where the duality literature lives, the polarization is a discrete classical choice lifted explicitly at one loop, not a Goldstone angle ([the polarization as a Goldstone angle](/wiki/symmetry-breaking/goldstone-angle)).
- **Where it is carried.** The root `CLAUDE.md` lists it among the open ends of the toy Lagrangian, "a lead", next to those of [acceptance criterion 1](/wiki/symmetry-breaking/toy-models/acceptance-criterion); checkpoint #11 does not mention it.

## Sources

- `CLAUDE.md` 'Since the handoff' — its status as an open end and "a lead"
- `papers/reciprocity-toy-models.md` §3, §6 — the vacua, the one-loop split and its limits, quoted above; "Not shown"
- `verify/toy_gw.py` — the gated split at N = 6, 8, 10 and the identification of the preferred vacuum
- `review/round4-adjudication.md` 'Rulings' F4 — upheld, the β = π identification, and "a lead, not a result"
- `review/round4/adjudicator/arb.out` — the adjudicator's spectra and free-energy difference at N = 8
- `review/round4/referee/audit-notes.md` Step 2(b), Step 3 — the referee's finding F4 and its reading of the Goldstone-angle claim
