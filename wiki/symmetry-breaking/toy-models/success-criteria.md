---
title: "Success criteria S0–S5 and the pre-registered predictions"
weight: 20
status: method
description: "The six criteria fixed before construction (the letter, S0–S3; the spirit, S4–S5), the S0 prior-art survey, the self-scored predictions and the unpredicted findings."
sources:
  - "notes/toy-lagrangian.md 'Success criteria'"
  - "notes/toy-lagrangian.md 'Predictions'"
  - "notes/toy-lagrangian.md 'Chunk 1 results'"
  - "notes/toy-lagrangian.md 'Chunk 2 results'"
  - "notes/toy-lagrangian.md 'Chunk 3 results'"
  - "notes/toy-lagrangian.md 'Chunk 4: S5'"
  - "notes/toy-lagrangian.md 'Assessment against the predictions'"
  - "papers/reciprocity-toy-models.md §1"
  - "review/round4-adjudication.md 'Rulings'"
---

*The success criteria are six pass-or-fail tests, S0 to S5, written down on 19 October 2026 before either toy model was built, together with a forecast of how each would come out. Four of them encode the referees' literal demand: prior work is cited, the action is symmetric, the symmetry permutes the vacua, and an order parameter distinguishes them. Two encode the deeper objection that the framework does no work: the breaking must survive quantum fluctuations, and it must make matter's interactions local in position. Fixing the tests first means the results are judged by standards chosen before the results were known. The worklog scored all four forecasts as hits, before the round-4 review narrowed several of the results.*

**Status:** Method — the criteria carry no tags; the prior-art survey's citations are [S] ("every citation retrieved [S], nothing from memory") — written down and self-scored in `notes/toy-lagrangian.md`, before [review round 4](/wiki/method/review/round-4).

## Key facts

- **Tier 1, "the letter".** S0 prior art: "Each element of the toy is either new or cited." S1 symmetry of an action: "S is invariant, not merely related to its image by a unitary equivalence" ([unitary equivalence versus Noether symmetry](/wiki/phase-space/reciprocity/unitary-equivalence)). S2 ρ-related degenerate vacua: "no vacuum is ρ-invariant, and ρ maps each vacuum to another one." S3 η as order parameter: "A local operator built from η (equivalently the real structure K, with η = ωK) has a nonzero expectation value in each vacuum and is odd under ρ." ([spontaneous symmetry breaking](/wiki/symmetry-breaking/spontaneous-symmetry-breaking); [the order parameter](/wiki/symmetry-breaking/order-parameter))
- **Tier 2, "the spirit".** S4 quantum stability: "The breaking survives quantum fluctuations in the stated dimension"; the toy starts in 1+1 because "In 0+1 dimensions (quantum mechanics), tunnelling restores any symmetry" ([the Mermin–Wagner–Coleman theorem](/wiki/symmetry-breaking/mermin-wagner-coleman)). S5: matter acquires "interactions local in the selected Lagrangian (x) and nonlocal in its complement (p)", "the analogue of a Yukawa coupling giving masses through a vacuum expectation value".
- **Why S0 exists.** It is the lesson of the [compatibility theorem](/wiki/phase-space/born-geometry/compatibility-theorem), which was found after the fact to be Freidel–Leigh–Minic's. The S0 survey (2026-10-19): "no existing action has Born reciprocity exactly symmetric and spontaneously broken with η or K as order parameter"; "INSPIRE's coverage is incomplete, so this is evidence of absence, not proof." Related but different: Born sigma models choose the polarization by gauging (Marotta–Szabo); double field theory with spontaneously broken O(D,D) has H as the order parameter, with η fixed (Angus–Kim–Park); Smolin "breaks a triality down to Born duality, which stays unbroken" (version 2, §1).
- **What round 4 added to S0.** The referee found prior work missing from the first version of the note, accepted "as citations and reframing": the Langmann–Szabo–Zarembo exact solution, Smolin's triality paper, Marotta–Szabo, Fosco–Moreno, Grosse–Wulkenhaar's matrix-base paper and Royer's parity-operator form of Weyl symbols.
- **The forecasts**, written before construction and later self-scored "Hit": "S1–S3 will pass easily"; "S4 will pass only for a discrete reduction" (or via a non-amenability exception); "S5 is the real test, and I expect it not to pass at the first attempt"; and if S1–S4 passed while S5 failed, criterion 1 "as the referees worded it is too weak to answer 'the framework does no work'". The forecasts cite one recalled source (†, the Langmann–Szabo duality and the Grosse–Wulkenhaar model), retrieved [S] in the S0 survey. Every review round follows the same practice ([pre-registration](/wiki/method/review/pre-registration)).
- **The scorecard** (worklog, chunks 2–4). S1–S3: "Pass in both toys, as predicted". S4: "Pass for coset + τ potential; fail for both exactly self-dual versions in 1+1 / at fixed μ²". S5: the weak form passes [V]; the strong form ("locality forced, not chosen") is "not achieved" ([locality from an (H, K)-built coupling](/wiki/symmetry-breaking/matter-coupling); [forced locality](/wiki/symmetry-breaking/strong-locality)). The "τ potential" of the S4 pass is the [naive ρ-preserving potential](/wiki/symmetry-breaking/toy-models/coset-model/naive-potential), unbounded once H is dynamical; version 2 restates the pass with the [bounded potential](/wiki/symmetry-breaking/toy-models/coset-model/bounded-potential), for the [frozen-H reduction](/wiki/symmetry-breaking/toy-models/coset-model/frozen-h-reduction) only.
- **Findings that were not predicted.** (1) "At every self-dual point, ρ sits inside a continuous U(1)" ([the polarization as a Goldstone angle](/wiki/symmetry-breaking/goldstone-angle)). (2) The complex Grosse–Wulkenhaar vacua "break the Langmann–Szabo duality classically, as a cos β polarization", and "The breaking does not survive quantization" ([complex-model vacua](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/complex-vacua)). (3) In 1+1, "A ρ-preserving potential on the polarization circle is required" ([the origin of that potential, open](/wiki/symmetry-breaking/rho-preserving-potential)).

## Sources

- `notes/toy-lagrangian.md` 'Success criteria' — the six criteria, quoted above
- `notes/toy-lagrangian.md` 'Predictions' — the four forecasts and the one recalled citation
- `notes/toy-lagrangian.md` 'Chunk 1 results' — the S0 prior-art survey [S]
- `notes/toy-lagrangian.md` 'Chunk 2 results', 'Chunk 3 results', 'Chunk 4: S5' — the scorecards and the S5 conclusion
- `notes/toy-lagrangian.md` 'Assessment against the predictions' — the scoring and the unpredicted findings
- `papers/reciprocity-toy-models.md` §1 — the prior work as version 2 states it
- `review/round4-adjudication.md` 'Rulings' — the omitted prior work added in round 4
