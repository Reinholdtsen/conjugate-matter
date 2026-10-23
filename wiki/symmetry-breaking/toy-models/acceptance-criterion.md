---
title: "Acceptance criterion 1: the toy Lagrangian (OP11)"
weight: 10
status: alive
description: "The referees' standing demand for an action in which ρ is a genuine Noether symmetry, spontaneously broken, with η as order parameter; met in their wording by model I with a bounded potential; what remains open, the superseded first verdict, and the unaddressed electric-sublattice clause."
sources:
  - "papers/broken-born-checkpoint-v2.md §14 item 11"
  - "papers/broken-born-checkpoint-v2.md §4"
  - "CLAUDE.md 'Since the handoff'"
  - "papers/reciprocity-toy-models.md §2"
  - "papers/reciprocity-toy-models.md §4"
  - "papers/reciprocity-toy-models.md §5"
  - "papers/reciprocity-toy-models.md §6"
  - "review/round3-adjudication.md 'Decisions' 4"
  - "review/round4-adjudication.md 'Verdict'"
  - "review/round4-adjudication.md 'Rulings'"
  - "review/round4-preregistration.md 'Predictions'"
  - "review/round4/referee/audit-notes.md Step 3"
  - "notes/toy-lagrangian.md 'Success criteria'"
  - "notes/toy-lagrangian.md 'Assessment against the predictions'"
  - "HANDOFF.md §2"
  - "HANDOFF.md §6"
  - "HANDOFF.md §8"
  - "notes/knot-dark-matter-standalone.md §1"
  - "notes/knot-dark-matter-standalone.md §6"
  - "review/round4-adjudication.md 'Revisions for v2 of the note (all accepted; applied 2026-10-20 in commit 6606734)'"
  - "notes/toy-lagrangian.md 'Write-up and review (2026-10-19/20)'"
  - "review/wiki-build-flags.md item 42"
---

*Acceptance criterion 1 is the referees' demand for one explicit action, a toy model being enough, in which [Born reciprocity](/wiki/phase-space/reciprocity/born-reciprocity) ρ, the exchange (x, p) → (p, −x), is a genuine symmetry that the vacuum breaks, with the [neutral metric](/wiki/phase-space/born-geometry/born-structures) η as the [order parameter](/wiki/symmetry-breaking/order-parameter). In ordinary quantum mechanics ρ is only a change of description, carried out by the [Fourier transform](/wiki/phase-space/reciprocity/fourier-transform); the program claims more, and the referees asked to see it in a model. The referees of review rounds 1 and 2 named it independently, and the program made it the first acceptance criterion for anything it proposes. [Checkpoint #11](/wiki/history/documents/checkpoint) records it as met in the referees' wording by [model I](/wiki/symmetry-breaking/toy-models/coset-model), a [sigma model](/wiki/symmetry-breaking/toy-models/coset-model/sigma-models) of a phase-space metric and a real structure, with a bounded ρ-preserving potential. A simulation with all fields dynamical, a derivation of the potential and forced locality of matter remain open. One clause of an older wording, that η also select the electric sublattice, is not addressed.*

**Status:** Alive — met "in the referees' wording" (#11 §14 item 11; "done to the referees' wording", root `CLAUDE.md`), with the remaining parts tagged [O]. Model I's checks run in `verify/toy_coset.py` and `verify/toy_s4.py` ([the toy-model scripts](/wiki/method/verification/toy-model-scripts)); the [toy-model note](/wiki/symmetry-breaking/toy-models) was graded B in [review round 4](/wiki/method/review/round-4) and revised to version 2.

## The demand

The referees' wording, as the toy-Lagrangian worklog records it: "an action in which ρ is a genuine Noether symmetry, spontaneously broken, with η the order parameter" ('Success criteria'). It has four parts:

- **An explicit action.** A specified field theory, not an argument about one; "a toy model suffices", in the wording of [#14](/wiki/dark-matter/candidates/soliton-candidate) §6.
- **A genuine Noether symmetry.** The action is invariant under ρ. This is the point the referees pressed: in ordinary quantum mechanics ρ is carried out by the [Fourier transform](/wiki/phase-space/reciprocity/fourier-transform), a unitary change from the position description of a state to its momentum description. Such a change of description is available in any quantum theory, so by itself it does not make ρ a symmetry of the dynamics ([unitary equivalence versus Noether symmetry](/wiki/phase-space/reciprocity/unitary-equivalence)). #14 conceded the point at its outset: "as usually encountered, rho is a unitary equivalence between representations of the canonical commutation relations, not a Noether symmetry of a specified action" (§1).
- **Spontaneously broken.** The vacua are not invariant under ρ, which maps one vacuum to another ([spontaneous symmetry breaking](/wiki/symmetry-breaking/spontaneous-symmetry-breaking)).
- **η the order parameter.** The quantity that distinguishes the vacua is the neutral metric η, whose choice fixes which Lagrangian subspace of phase space counts as position ([Lagrangian polarizations](/wiki/phase-space/reciprocity/lagrangian-polarizations)).

These are the program's own claims put in testable form: the postulates say that the laws are ρ-invariant ([P3](/wiki/program/postulates/p3-reciprocity)), that η is not rigid but emergent, the order parameter of the breaking ([P2′](/wiki/program/postulates/p2-prime)), and that the vacuum selects a polarization ([P5](/wiki/program/postulates/p5-spontaneous-selection)). In the toy models η is built from a real structure K, η = ωK; #11's statement of P2′ writes η = HJ instead, "with the real structure J chosen spontaneously" (§4). No document reconciles the two notations ([the order parameter](/wiki/symmetry-breaking/order-parameter)).

## Where it came from

- **Rounds 1 and 2.** The handoff records the demand among the valid hits of round 1: "toy-Lagrangian demand adopted as acceptance criterion #1" (`HANDOFF.md` §6). Its open-problems list: "Toy Lagrangian in which ρ is a genuine Noether symmetry, spontaneously broken, η the order parameter also selecting the electric sublattice (acceptance criterion #1; both reviewers independently named it)" (§2). See [review rounds 1 and 2](/wiki/method/review/rounds-one-and-two) and [the handoff](/wiki/history/documents/handoff).
- **#14's statement.** The soliton manuscript, now withdrawn, listed it as the first of three acceptance criteria: "(1) exhibition of an action - a toy model suffices - in which rho is a genuine Noether symmetry, spontaneously broken, with eta the order parameter selecting both the position polarization and the hidden sector's electric description; deriving hypothesis H from that action would make the coupling a prediction" (§6).
- **The queue.** The handoff ranked it fourth: "**Toy Lagrangian** (acceptance criterion #1) — the item both independent reviewers named as the gate to verdict A. Hardest; highest value. Start in 0+1 or 1+1 dimensions on the Siegel disk." (§8 item 4).
- **Round 3.** The third referee added the deeper objection that [the framework does no work](/wiki/program/framework-does-no-work). The adjudication's Decision 4 made the toy Lagrangian the next task: "Every referee across three rounds converges on 'the framework does no work'. The toy action is the only item that can change that, and it is acceptance criterion 1 for anything the program proposes." ([round-3 decisions](/wiki/method/review/round-3/decisions)).

## From the demand to tests

Before building anything, the worklog fixed six pass-or-fail criteria in two tiers: "The first tier is the referees' letter; the second is what would answer round 3." ('Success criteria'). Tier 1 is S0, prior work cited; S1, a symmetric action; S2, vacua that ρ permutes; and S3, an order parameter built from η. Tier 2 is S4, survival under quantum fluctuations, and S5, a consequence for matter's locality. The criteria and the forecasts made with them are on [success criteria S0–S5](/wiki/symmetry-breaking/toy-models/success-criteria).

## The verdict

#11 §14 item 11, current since version 2.2 (2026-10-20):

> **Toy Lagrangian** (acceptance criterion 1 of every program proposal). Met in the referees' wording by the coset model of (H, K) with a bounded ρ-preserving potential, in `papers/reciprocity-toy-models.md`:
> - ρ is a symmetry of an explicit action, and η = ωK is the order parameter;
> - the vacuum is stable with H dynamical;
> - there is an ordered ℤ₂ phase in 1+1 in the frozen-H reduction (Monte Carlo).

Each line rests on a part of model I:

- **The action and the order parameter.** Model I's fields are a phase-space metric H and a real structure K on a 1+1-dimensional base. Its action is invariant under the whole [symplectic group](/wiki/phase-space/reciprocity/symplectic-form) Sp(2, ℝ), "checked for generic symplectic S, so for ρ", and under a separate flip K → −K (toy-model note §2; [action and symmetries](/wiki/symmetry-breaking/toy-models/coset-model/action-and-symmetries)). At H = 1 the vacua form a circle K(φ), ρ maps K(φ) to −K(φ), and "O = K₁₁ flips sign under ρ" (§2; [the vacua](/wiki/symmetry-breaking/toy-models/coset-model/vacua)).
- **Stability with H dynamical.** A definite polarization needs a potential that keeps ρ and reduces the continuous circle to two vacua, ±K_ref. The first such potential was unbounded below once H moves, and died in round 4 ([obituary: the naive ρ-preserving potential](/wiki/symmetry-breaking/toy-models/coset-model/naive-potential)). Its replacement V_b is bounded, and "With H dynamical, (1, K_ref) is a stable minimum: Hessian eigenvalues 0, 0.764, 2, 5.236" (§4; [the bounded potential V_b](/wiki/symmetry-breaking/toy-models/coset-model/bounded-potential)). The zero eigenvalue belongs to a flat line that, in version 2's words, "is not symmetry-protected"; #11's line does not mention it.
- **The ordered phase.** In 1+1 dimensions the continuous angle cannot order ([Mermin–Wagner–Coleman](/wiki/symmetry-breaking/mermin-wagner-coleman)), but the two vacua ±K_ref can. A lattice Monte Carlo of the polarization angle at H = 1 finds ⟨|m|⟩ = 0.954 ± 0.0001 "at every size" (L = 16, 32 and 64; see flag 13 in `review/wiki-build-flags.md`) with the potential, and no true order without it (§4; [the frozen-H reduction](/wiki/symmetry-breaking/toy-models/coset-model/frozen-h-reduction); [the Monte Carlo](/wiki/symmetry-breaking/toy-models/coset-model/monte-carlo)).

Version 2.2 of #11 adds two qualifications in its refinement of P2′. "A definite polarization needs a ρ-preserving potential on that angle — a rigid, unordered pair of axes, so more structure than ω alone, though less than a rigid η." And "the breaking of ρ is physical only once matter couples to the sign of K (P4): without such a coupling, a twisted element ρ∘(K → −K) leaves the vacuum invariant" (#11 §4; [the twisted element](/wiki/symmetry-breaking/twisted-element); [P4](/wiki/program/postulates/p4-polarized-matter)).

Model II, the self-dual Grosse–Wulkenhaar model, was tried first and does not meet the criterion: its complex version breaks the position–momentum duality only classically ([quantum restoration](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/quantum-restoration)), and its real version has no duality symmetry to break ([Model II](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar)).

### The review behind it

The note's first version was graded B in round 4: "Referee: B (flawed but salvageable), confidence ~0.75. I agree." The reason: "The only claim of actual quantum symmetry breaking (§4, model I in 1+1) rests on a potential that is unbounded below once H is dynamical"; and "It is repairable." (`review/round4-adjudication.md`, 'Verdict'). The pre-registration had placed the weakest link there, on the rigid background the potential introduces, and the adjudication scored it "**Partial**: right location, missed severity" ([pre-registration](/wiki/method/review/pre-registration)). Version 2 applies the accepted revisions, except the comparison with Langmann, Szabo and Zarembo's exact solution of a related model that revision 4 asked for, which it says it has not carried out (§4; [quantum restoration](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/quantum-restoration#open-the-comparison-with-the-exact-solution)). #11's item ends "Round-4 blind review: verdict B; v2 applies the accepted revisions", and the adjudication and the worklog record every accepted revision as applied (flag 42 in `review/wiki-build-flags.md`).

The referee's assessment of how spontaneous the 1+1 breaking is: with H frozen, an Ising-type breaking of the remaining ℤ₂, "But the potential fixes the unordered axis pair by hand, so the vacuum chooses only which of two pre-set axes is 'position'." With H dynamical, as the model was first written, the breaking was "not established" (audit notes, Step 3). The bounded potential answers the second point for the vacuum's stability; a simulation with H dynamical has not been run.

## How far it answers round 3

The worklog's assessment, written before round 4: "The round-3 critique ('the framework does no work') is only partly answered. The toy makes the program's structures cohere (η as order parameter; τ as the polarization angle), but matter's x-locality still enters through the P4-type coupling." It assigns the idea to prior work: "Prior art: FLM have the idea. The explicit realization appears new per S0." ('Assessment against the predictions'; FLM is Freidel–Leigh–Minic, [broken Born duality](/wiki/phase-space/reciprocity/broken-born-duality)). Here τ is the program's dark-energy field, which it places on the polarization circle ([τ quintessence](/wiki/cosmology/dark-energy/tau-quintessence)). The round-4 referee's searches found no earlier explicit model "with eta=omega K as a dynamical order parameter", and judged that "Model I appears new as a field theory, but it is a simple coset" (audit notes, Step 3).

The forecast written before construction: if S1–S4 passed and S5 failed, "acceptance criterion 1 as the referees worded it is too weak to answer 'the framework does no work'". It was scored "Hit": "Criterion 1 as worded is now met (coset + τ potential). The round-3 critique is only partly answered" ('Assessment against the predictions'). The τ potential of that scoring is the [naive ρ-preserving potential](/wiki/symmetry-breaking/toy-models/coset-model/naive-potential), now dead, and the verdict built on it is superseded ([below](#superseded-the-worklogs-first-verdict)). The matter-locality side is on [locality from an (H, K)-built coupling](/wiki/symmetry-breaking/matter-coupling) and [Open: forced locality and the P4 lock](/wiki/symmetry-breaking/strong-locality).

## Open: the parts not yet met

#11 §14 item 11: "Still open [O]: a Monte Carlo with H dynamical; a derivation of the potential; locality of matter beyond the weak (Yukawa-like) form, which in the toy reduces to P4." The root `CLAUDE.md` lists the open ends of the toy Lagrangian as "a Monte Carlo with H dynamical; a derivation of the ρ-preserving potential; the strong form of matter locality; the real Grosse–Wulkenhaar model's one-loop preference for the position-sharp vacuum, a lead."

- **[A Monte Carlo with H dynamical](/wiki/symmetry-breaking/toy-models/coset-model/dynamical-h-monte-carlo).** The ordered phase is established for the frozen-H reduction only. Whether ρ's compact SO(2) breaks in the coupled model, where the metric sector is a hyperbolic model that can order in two dimensions, is also open ([the frozen-H reduction](/wiki/symmetry-breaking/toy-models/coset-model/frozen-h-reduction); [Open: does ρ's SO(2) break in the coupled model?](/wiki/symmetry-breaking/toy-models/coset-model/so2-question)).
- **A derivation of the potential.** The potential that makes the polarization definite is chosen, not derived, and it "introduces a rigid, unordered pair of axes" (note §6; [Open: the origin of the ρ-preserving potential](/wiki/symmetry-breaking/rho-preserving-potential)).
- **Locality beyond the weak form.** Matter becomes local in the selected polarization only if it interacts through a coupling built from (H, K), "as fermion masses follow from a Higgs vacuum value once Yukawa couplings are given. Nothing here forces that coupling." (note §5; [Goldstone modes and the Higgs mechanism](/wiki/symmetry-breaking/goldstone-and-higgs); [Yukawa couplings](/wiki/gravity/spin-2-fields/yukawa-forces#a-name-collision-the-yukawa-coupling); [Open: forced locality and the P4 lock](/wiki/symmetry-breaking/strong-locality)).
- **The real-model lead.** Not part of #11's list: [Open: the real model's one-loop preference](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/real-model-lead).

All four are registered at [open problems](/wiki/status/open-problems). The queue in the root `CLAUDE.md` adds one optional item for this work: "a round-5 review of the toy note, but only before any external use."

## The electric-sublattice clause

Two older wordings of the criterion ask more of η. The handoff: "η the order parameter also selecting the electric sublattice" (`HANDOFF.md` §2). #14: η "selecting both the position polarization and the hidden sector's electric description" (§6). The clause ties the order parameter to the program's identification of electric–magnetic duality frames with phase-space polarizations ([the symplectic charge lattice](/wiki/electric-magnetic-duality/symplectic-charge-lattice)). The worklog's statement of the referees' wording, its criteria S0–S5 and #11 §14 item 11 omit the clause, and #11 declares the criterion met. The root `CLAUDE.md` wording, "done to the referees' wording", governs ([source conflicts](/wiki/history/documents/source-conflicts#status-changes-since-the-handoff)). Nothing in the record addresses the clause, and no current document lists it as open.

## Superseded: the worklog's first verdict

**The first statement.** Before round 4 the worklog declared: "**Verdict on acceptance criterion 1.** Met, in the referees' wording, by the coset toy plus a τ-type potential", with "It is spontaneously broken (Ising class in 1+1, Monte Carlo verified)." ('Assessment against the predictions').

**What replaced it.** #11 §14 item 11 in version 2.2: met "by the coset model of (H, K) with a bounded ρ-preserving potential", with "an ordered ℤ₂ phase in 1+1 in the frozen-H reduction".

**Why.** The "τ-type potential", −μ[Tr(K K_ref)]², is unbounded below once H is dynamical, so its intended vacuum is a saddle and the Monte Carlo had simulated a reduction with H frozen, not model I (round-4 findings F1 and F2, both upheld; [obituary: the naive ρ-preserving potential](/wiki/symmetry-breaking/toy-models/coset-model/naive-potential)). Data at one temperature deep in the ordered phase establish order, not a universality class, so revision 1 replaced "Ising class" with "ordered ℤ₂ phase" ([the frozen-H reduction](/wiki/symmetry-breaking/toy-models/coset-model/frozen-h-reduction)). The adjudicator had also checked the potential only at frozen H ('Rulings' F2). Round-4 lesson 1 became a rule of the program's [method](/wiki/method): when numerics run on a reduced model, check the unreduced model's stability ([reduced-model stability](/wiki/method/verification/reduced-model-stability)). The register of [superseded statements](/wiki/status/superseded) lists the "Ising class" wording.

## #14's other criteria

#14 §6 listed two more criteria: "(2) either a gauged hidden charge conjugation, or a demonstration that the millicharged psi window survives existing constraints" and "(3) the strong-coupling relic freeze-out calculation of Sec. 3, in the hidden plasma". Both served the superheavy soliton candidate, which round 3 retired and which stays dead ([obituary: the soliton candidate](/wiki/dark-matter/candidates/soliton-candidate/obituary)). Criterion 1 outlived the manuscript that stated it: round 3 made it "acceptance criterion 1 for anything the program proposes" (Decision 4), since it tests the program's [hard core](/wiki/program/hard-core) rather than any one candidate.

## Sources

- `papers/broken-born-checkpoint-v2.md` §14 item 11 — the current verdict and its open parts [O]
- `papers/broken-born-checkpoint-v2.md` §4 — the P2′ refinement: the potential's rigid pair of axes, the twisted element
- `CLAUDE.md` 'Since the handoff' — "done to the referees' wording"; the open ends, including the real-model lead; the optional round 5
- `papers/reciprocity-toy-models.md` §2, §4, §5, §6 — model I's symmetry, vacua and order parameter; the bounded potential and the Monte Carlo; the Yukawa analogy; "Not shown"
- `review/round3-adjudication.md` 'Decisions' 4 — why the toy Lagrangian came next
- `review/round4-adjudication.md` 'Verdict', 'Rulings' — the B grade; findings F1 and F2 and the adjudicator's account
- `review/round4-preregistration.md` 'Predictions' — the predicted weakest link
- `review/round4/referee/audit-notes.md` Step 3 — how spontaneous the 1+1 breaking is; the novelty of model I
- `notes/toy-lagrangian.md` 'Success criteria', 'Assessment against the predictions' — the referees' wording and the two tiers; the first verdict, its prior-art statement and the scored forecast
- `HANDOFF.md` §2, §6, §8 item 4 — the electric-sublattice wording; the criterion's adoption in round 1; the original queue item
- `notes/knot-dark-matter-standalone.md` §1, §6 — #14's concession and its acceptance criteria (1)–(3), in a withdrawn document
- `review/round4-adjudication.md` 'Revisions for v2 of the note'; `notes/toy-lagrangian.md` 'Write-up and review (2026-10-19/20)'; `review/wiki-build-flags.md` item 42 — every accepted revision recorded as applied, against the comparison v2 did not make; awaiting Paul's ruling
