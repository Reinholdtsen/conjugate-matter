---
title: "Acceptance criterion 1: the toy Lagrangian (OP11)"
weight: 10
status: alive
description: "The referees' standing demand for an action in which ρ is a genuine Noether symmetry, spontaneously broken, with η as order parameter; met in their wording by model I with a bounded potential; what remains open, including the unaddressed electric-sublattice clause."
sources:
  - "papers/broken-born-checkpoint-v2.md §14 item 11"
  - "CLAUDE.md 'Since the handoff'"
  - "review/round3-adjudication.md 'Decisions' 4"
  - "review/round4-adjudication.md 'Verdict'"
  - "notes/toy-lagrangian.md 'Success criteria'"
  - "notes/toy-lagrangian.md 'Assessment against the predictions'"
  - "HANDOFF.md §2"
  - "HANDOFF.md §6"
  - "HANDOFF.md §8"
  - "notes/knot-dark-matter-standalone.md §6"
---

*Acceptance criterion 1 is the referees' demand for one explicit action, a toy model being enough, in which [Born reciprocity](/wiki/phase-space/reciprocity/born-reciprocity) ρ, the exchange (x, p) → (p, −x), is a genuine symmetry that the vacuum breaks, with the neutral metric η as the [order parameter](/wiki/symmetry-breaking/order-parameter). The referees of review rounds 1 and 2 named it independently, and the program made it the first acceptance criterion for anything it proposes. Checkpoint #11 records it as met in the referees' wording by [model I](/wiki/symmetry-breaking/toy-models/coset-model) with a bounded ρ-preserving potential. A simulation with all fields dynamical, a derivation of the potential and forced locality of matter remain open, and one clause of an older wording, that η also select the electric sublattice, is not addressed.*

**Status:** Alive — met "in the referees' wording" (#11 §14 item 11; "done to the referees' wording", root `CLAUDE.md`), with the remaining parts tagged [O] — model I's checks run in `verify/toy_coset.py` and `verify/toy_s4.py` ([the toy-model scripts](/wiki/method/verification/toy-model-scripts)); the toy-model note was graded B in [review round 4](/wiki/method/review/round-4).

## Key facts

- **The demand.** The referees' wording (rounds 1–2): "an action in which ρ is a genuine Noether symmetry, spontaneously broken, with η the order parameter". Round 3 added that the framework does no work ([the critique](/wiki/program/framework-does-no-work)). The worklog turned the demand into [success criteria S0–S5](/wiki/symmetry-breaking/toy-models/success-criteria): "The first tier is the referees' letter; the second is what would answer round 3." (`notes/toy-lagrangian.md`, 'Success criteria'; [review rounds 1 and 2](/wiki/method/review/rounds-one-and-two)).
- **Why it came next.** Round-3 Decision 4: "Every referee across three rounds converges on 'the framework does no work'. The toy action is the only item that can change that, and it is acceptance criterion 1 for anything the program proposes." The handoff's queue had called it "the item both independent reviewers named as the gate to verdict A. Hardest; highest value. Start in 0+1 or 1+1 dimensions on the Siegel disk." ([round-3 decisions](/wiki/method/review/round-3/decisions); [the handoff document](/wiki/history/documents/handoff)).
- **The verdict** (#11 §14 item 11): "Met in the referees' wording by the coset model of (H, K) with a bounded ρ-preserving potential": ρ is a symmetry of an explicit action, and η = ωK is the order parameter ([action and symmetries](/wiki/symmetry-breaking/toy-models/coset-model/action-and-symmetries)); the vacuum is stable with H dynamical ([the bounded potential V_b](/wiki/symmetry-breaking/toy-models/coset-model/bounded-potential)); there is an ordered ℤ₂ phase in 1+1 in the frozen-H reduction ([the frozen-H reduction](/wiki/symmetry-breaking/toy-models/coset-model/frozen-h-reduction); [the Monte Carlo](/wiki/symmetry-breaking/toy-models/coset-model/monte-carlo)).
- **Still open [O]** (#11 §14 item 11): "a Monte Carlo with H dynamical; a derivation of the potential; locality of matter beyond the weak (Yukawa-like) form, which in the toy reduces to P4." The root `CLAUDE.md` lists the same open ends and adds "the real Grosse–Wulkenhaar model's one-loop preference for the position-sharp vacuum, a lead" ([origin of the potential](/wiki/symmetry-breaking/rho-preserving-potential); [forced locality](/wiki/symmetry-breaking/strong-locality); [the real model's lead](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/real-model-lead); [open problems](/wiki/status/open-problems)).
- **How far it answers round 3.** The worklog's verdict: "The round-3 critique ('the framework does no work') is only partly answered. The toy makes the program's structures cohere (η as order parameter; τ as the polarization angle), but matter's x-locality still enters through the P4-type coupling." It credits the idea to Freidel–Leigh–Minic and finds that "The explicit realization appears new per S0" ([broken Born duality](/wiki/phase-space/reciprocity/broken-born-duality)).
- **The electric-sublattice clause, unaddressed.** `HANDOFF.md` §2 words the criterion as "η the order parameter also selecting the electric sublattice", and the withdrawn #14 §6 asks for η "selecting both the position polarization and the hidden sector's electric description". The worklog's criteria and #11 §14 item 11 omit the clause while declaring the criterion met. The root `CLAUDE.md` wording, "done to the referees' wording", governs; nothing yet addresses the clause ([the symplectic charge lattice](/wiki/electric-magnetic-duality/symplectic-charge-lattice)).
- **#14's other criteria.** #14 §6 listed two more: (2) a gauged hidden charge conjugation, or a demonstration that the millicharged ψ window survives existing constraints; (3) "the strong-coupling relic freeze-out calculation of Sec. 3, in the hidden plasma". Both belonged to the [superheavy soliton candidate](/wiki/dark-matter/candidates/soliton-candidate/obituary), which round 3 retired and which stays dead.
- **Wording that predates round 4.** The worklog declared the criterion met "by the coset toy plus a τ-type potential", with breaking of "Ising class in 1+1". That potential is the [naive ρ-preserving potential](/wiki/symmetry-breaking/toy-models/coset-model/naive-potential), now dead; version 2 of the note uses the bounded form and says "ordered ℤ₂ phase" for the frozen-H reduction only. A round-5 review of the note is optional, "but only before any external use" (root `CLAUDE.md`).

## Sources

- `papers/broken-born-checkpoint-v2.md` §14 item 11 — the current verdict and its open parts [O]
- `CLAUDE.md` 'Since the handoff' — "done to the referees' wording"; the open ends, including the real-model lead; the optional round 5
- `review/round3-adjudication.md` 'Decisions' 4 — why the toy Lagrangian came next
- `review/round4-adjudication.md` 'Verdict' — the B grade and the repair
- `notes/toy-lagrangian.md` 'Success criteria', 'Assessment against the predictions' — the referees' wording; the worklog's verdict and its prior-art statement
- `HANDOFF.md` §2, §6, §8 item 4 — the electric-sublattice wording; the criterion's adoption in round 1; the original queue item
- `notes/knot-dark-matter-standalone.md` §6 — #14's acceptance criteria (1)–(3), in a withdrawn document
