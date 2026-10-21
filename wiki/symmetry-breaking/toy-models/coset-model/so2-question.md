---
title: "Open: does ρ's SO(2) break in the coupled model?"
weight: 80
status: open
description: "By Mermin–Wagner the compact angle cannot order in 1+1, but model I's H-sector is a hyperbolic model that can break; whether the full coupled model breaks ρ's SO(2) without a potential is open."
sources:
  - "papers/reciprocity-toy-models.md §4"
  - "papers/reciprocity-toy-models.md §6"
  - "review/round4-adjudication.md 'Rulings'"
  - "review/round4-adjudication.md 'Revisions' 1"
  - "review/round4/referee/audit-notes.md Step 1"
  - "review/round4/referee/audit-notes.md Step 3"
  - "notes/toy-lagrangian.md 'Chunk 1 results'"
  - "notes/toy-lagrangian.md 'Assessment against the predictions'"
---

*The open question is whether [model I](/wiki/symmetry-breaking/toy-models/coset-model), with its metric field H free to vary and no added potential, spontaneously breaks the compact rotation group SO(2) that contains [Born reciprocity](/wiki/phase-space/reciprocity/born-reciprocity) ρ. In two dimensions a compact continuous symmetry cannot break on its own ([the Mermin–Wagner–Coleman theorem](/wiki/symmetry-breaking/mermin-wagner-coleman)), so the polarization angle by itself cannot order. But model I's metric sector is a hyperbolic sigma model, a known case in which a non-compact symmetry does break in two dimensions, and the two sectors are coupled. Round 4 required the toy-model note to restrict the theorem to the compact SO(2) and to state the coupled case as open; the note lists it as not shown.*

**Status:** Open — untagged — raised by the round-4 referee (conceptual point C2), upheld as a literature point in the adjudication, and listed under "Not shown" in version 2, §6. Registered at [open problems](/wiki/status/open-problems).

## Key facts

- **The theorem, restricted.** Version 2: "In 1+1 the compact angle φ cannot order: Mermin–Wagner [13, 14] applies to the compact SO(2) containing ρ."
- **The exception.** "The non-compact half-plane sector is a hyperbolic model, where symmetry breaking in 2D does occur [15]. Whether ρ's SO(2) stays unbroken in the full coupled model is open." ([coset and hyperbolic sigma models](/wiki/symmetry-breaking/toy-models/coset-model/sigma-models))
- **Where it came from.** The referee's point C2: model I's group Sp(2,ℝ) is non-amenable, and its H-sector is the SO(1,2)/SO(2) hyperbolic sigma model, for which Duncan, Niedermaier and Seiler report spontaneous breaking in two dimensions; the first version had applied Mermin–Wagner to the whole continuous breaking. The adjudication: "The Mermin–Wagner statement must be restricted to the compact SO(2) containing ρ. Whether that SO(2) is broken in the coupled model is open."
- **What the note does instead.** To get a definite polarization it adds a potential that "is invariant under ρ and under K → −K, and reduces the U(1) to a discrete group" ([the bounded potential V_b](/wiki/symmetry-breaking/toy-models/coset-model/bounded-potential)), and it simulates the [frozen-H reduction](/wiki/symmetry-breaking/toy-models/coset-model/frozen-h-reduction), in which the angle orders only with that potential ([the Monte Carlo](/wiki/symmetry-breaking/toy-models/coset-model/monte-carlo)).
- **As the note lists it.** "Not shown: … whether ρ's SO(2) breaks in the coupled model without a potential" (version 2, §6), next to "a Monte Carlo of model I with H dynamical", which #11 §14 item 11 also lists as open [O].
- **The worklog's earlier framing.** Chunk 1 called S4 "the open question": "in 1+1 the compact circle mode should restore ⟨K⟩ (Coleman–Mermin–Wagner) unless the non-amenable directions change that." The final assessment recorded the non-amenability route as "not needed, not tested". The worklog's separate remark that the continuous breaking is allowed in 3+1 dimensions is recorded at [the polarization as a Goldstone angle](/wiki/symmetry-breaking/goldstone-angle).

## Sources

- `papers/reciprocity-toy-models.md` §4, §6 — the restricted theorem, the open question and the "Not shown" list
- `review/round4-adjudication.md` 'Rulings' ("Mermin–Wagner vs [11]"), 'Revisions' 1 — upheld (literature); the required restriction
- `review/round4/referee/audit-notes.md` Step 1, Step 3 — the hyperbolic-model citation and conceptual point C2
- `notes/toy-lagrangian.md` 'Chunk 1 results', 'Assessment against the predictions' — the worklog's framing and its non-amenability verdict
