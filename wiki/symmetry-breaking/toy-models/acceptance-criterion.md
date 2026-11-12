---
title: "Acceptance criterion 1: the toy Lagrangian (OP11)"
weight: 10
status: alive
description: "The referees' standing demand for an action in which ρ is a genuine Noether symmetry, spontaneously broken, with η as order parameter; met in their wording by model I with a bounded potential; what remains open, the superseded first verdict, and the unaddressed electric-sublattice clause, which #11 lists first among what the magnetic-mirror conjecture needs."
sources:
  - "wiki/papers/broken-born-checkpoint-v2.md §14 item 11"
  - "wiki/papers/broken-born-checkpoint-v2.md §4"
  - "wiki/papers/broken-born-checkpoint-v2.md §11.4"
  - "wiki/papers/broken-born-checkpoint-v2.md §12"
  - "CLAUDE.md 'Since the handoff'"
  - "wiki/papers/reciprocity-toy-models.md §2"
  - "wiki/papers/reciprocity-toy-models.md §4"
  - "wiki/papers/reciprocity-toy-models.md §5"
  - "wiki/papers/reciprocity-toy-models.md §6"
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

*Acceptance criterion 1 is the referees' demand for one explicit action, a toy model being enough, in which [Born reciprocity](../../phase-space/reciprocity/born-reciprocity.md) ρ, the exchange (x, p) → (p, −x), is a genuine symmetry that the vacuum breaks, with the [neutral metric](../../phase-space/born-geometry/born-structures.md) η as the [order parameter](../order-parameter.md). In ordinary quantum mechanics ρ is only a change of description, carried out by the [Fourier transform](../../phase-space/reciprocity/fourier-transform.md); the program claims more, and the referees asked to see it in a model. The referees of review rounds 1 and 2 named it independently, and the program made it the first acceptance criterion for anything it proposes. [Checkpoint #11](../../history/documents/checkpoint.md) records it as met in the referees' wording by [model I](coset-model/_index.md), a [sigma model](coset-model/sigma-models.md) of a phase-space metric and a real structure, with a bounded ρ-preserving potential. A simulation with all fields dynamical, a derivation of the potential and forced locality of matter remain open. One clause of an older wording, that η also select the electric sublattice, is not addressed; [#11](../../papers/broken-born-checkpoint-v2.md) lists it first among what P.R.'s open [magnetic-mirror conjecture](../../electric-magnetic-duality/magnetic-identification.md) needs.*

**Status:** Alive — met "in the referees' wording" ([#11 §14 item 11](../../papers/broken-born-checkpoint-v2.md#14-open-problems); "done to the referees' wording", root [`CLAUDE.md`](../../../CLAUDE.md)), with the remaining parts tagged [O]. Model I's checks run in [`verify/toy_coset.py`](../../../verify/toy_coset.py) and [`verify/toy_s4.py`](../../../verify/toy_s4.py) ([the toy-model scripts](../../method/verification/toy-model-scripts.md)); the [toy-model note](_index.md) was graded B in [review round 4](../../method/review/round-4.md) and revised to version 2.

## The demand

The referees' wording, as the toy-Lagrangian worklog records it: "an action in which ρ is a genuine Noether symmetry, spontaneously broken, with η the order parameter" ('Success criteria'). It has four parts:

- **An explicit action.** A specified field theory, not an argument about one; "a toy model suffices", in the wording of [a withdrawn paper on monopole dark matter, §6](../../../notes/knot-dark-matter-standalone.md#6-status-of-claims-and-acceptance-criteria).
- **A genuine Noether symmetry.** The action is invariant under ρ. This is the point the referees pressed: in ordinary quantum mechanics ρ is carried out by the [Fourier transform](../../phase-space/reciprocity/fourier-transform.md), a unitary change from the position description of a state to its momentum description. Such a change of description is available in any quantum theory, so by itself it does not make ρ a symmetry of the dynamics ([unitary equivalence versus Noether symmetry](../../phase-space/reciprocity/unitary-equivalence.md)). That paper conceded the point at its outset: "as usually encountered, rho is a unitary equivalence between representations of the canonical commutation relations, not a Noether symmetry of a specified action" ([§1](../../../notes/knot-dark-matter-standalone.md#1-framework)).
- **Spontaneously broken.** The vacua are not invariant under ρ, which maps one vacuum to another ([spontaneous symmetry breaking](../spontaneous-symmetry-breaking.md)).
- **η the order parameter.** The quantity that distinguishes the vacua is the neutral metric η, whose choice fixes which Lagrangian subspace of phase space counts as position ([Lagrangian polarizations](../../phase-space/reciprocity/lagrangian-polarizations.md)).

These are the program's own claims put in testable form: the postulates say that the laws are ρ-invariant ([P3](../../program/postulates/p3-reciprocity.md)), that η is not rigid but emergent, the order parameter of the breaking ([P2′](../../program/postulates/p2-prime.md)), and that the vacuum selects a polarization ([P5](../../program/postulates/p5-spontaneous-selection.md)). In the toy models η is built from a real structure K, η = ωK; #11's statement of P2′ writes η = HJ instead, "with the real structure J chosen spontaneously" ([§4](../../papers/broken-born-checkpoint-v2.md#4-postulates)). No document reconciles the two notations ([the order parameter](../order-parameter.md)).

## Where it came from

- **Rounds 1 and 2.** The handoff records the demand among the valid hits of round 1: "toy-Lagrangian demand adopted as acceptance criterion [#1](../../../notes/broken-born-theory.md)" ([`HANDOFF.md` §6](../../../HANDOFF.md#6-review-history-and-the-measured-failure-mode)). Its open-problems list: "Toy Lagrangian in which ρ is a genuine Noether symmetry, spontaneously broken, η the order parameter also selecting the electric sublattice (acceptance criterion #1; both reviewers independently named it)" (§2). See [review rounds 1 and 2](../../method/review/rounds-one-and-two.md) and [the handoff](../../history/documents/handoff.md).
- **The withdrawn paper's statement.** It listed the criterion first among three: "(1) exhibition of an action - a toy model suffices - in which rho is a genuine Noether symmetry, spontaneously broken, with eta the order parameter selecting both the position polarization and the hidden sector's electric description" ([§6](../../../notes/knot-dark-matter-standalone.md#6-status-of-claims-and-acceptance-criteria)). Its "hidden sector" is the separate copy of electromagnetism in which it placed its monopoles.
- **The queue.** The handoff ranked it fourth: "**Toy Lagrangian** (acceptance criterion #1) — the item both independent reviewers named as the gate to verdict A. Hardest; highest value. Start in 0+1 or 1+1 dimensions on the Siegel disk." (§8 item 4).
- **Round 3.** The third referee added the deeper objection that [the framework does no work](../../program/framework-does-no-work.md). The adjudication's Decision 4 made the toy Lagrangian the next task: "Every referee across three rounds converges on 'the framework does no work'. The toy action is the only item that can change that, and it is acceptance criterion 1 for anything the program proposes." ([round-3 decisions](../../method/review/round-3/decisions.md)).

## From the demand to tests

Before building anything, the worklog fixed six pass-or-fail criteria in two tiers: "The first tier is the referees' letter; the second is what would answer round 3." ('Success criteria'). Tier 1 is S0, prior work cited; S1, a symmetric action; S2, vacua that ρ permutes; and S3, an order parameter built from η. Tier 2 is S4, survival under quantum fluctuations, and S5, a consequence for matter's locality. The criteria and the forecasts made with them are on [success criteria S0–S5](success-criteria.md).

## The verdict

[#11 §14 item 11](../../papers/broken-born-checkpoint-v2.md#14-open-problems):

> **Toy Lagrangian** (acceptance criterion 1 of every program proposal). Met in the referees' wording by the coset model of (H, K) with a bounded ρ-preserving potential, in [`wiki/papers/reciprocity-toy-models.md`](../../papers/reciprocity-toy-models.md):
> - ρ is a symmetry of an explicit action, and η = ωK is the order parameter;
> - the vacuum is stable with H dynamical;
> - there is an ordered ℤ₂ phase in 1+1 in the frozen-H reduction (Monte Carlo).

Each line rests on a part of model I:

- **The action and the order parameter.** Model I's fields are a phase-space metric H and a real structure K on a 1+1-dimensional base. Its action is invariant under the whole [symplectic group](../../phase-space/reciprocity/symplectic-form.md) Sp(2, ℝ), "checked for generic symplectic S, so for ρ", and under a separate flip K → −K ([toy-model note §2](../../papers/reciprocity-toy-models.md#2-model-i-a-coset-sigma-model-of-h-k); [action and symmetries](coset-model/action-and-symmetries.md)). At H = 1 the vacua form a circle K(φ), ρ maps K(φ) to −K(φ), and "O = K₁₁ flips sign under ρ" ([§2](../../papers/reciprocity-toy-models.md#2-model-i-a-coset-sigma-model-of-h-k); [the vacua](coset-model/vacua.md)).
- **Stability with H dynamical.** A definite polarization needs a potential that keeps ρ and reduces the continuous circle to two vacua, ±K_ref. The first such potential is unbounded below once H moves, as round 4 found ([Under review: the naive ρ-preserving potential](coset-model/naive-potential.md)). Its replacement V_b is bounded, and "With H dynamical, (1, K_ref) is a stable minimum: Hessian eigenvalues 0, 0.764, 2, 5.236" (§4; [the bounded potential V_b](coset-model/bounded-potential.md)). The zero eigenvalue belongs to a flat line that, in version 2's words, "is not symmetry-protected"; #11's line does not mention it.
- **The ordered phase.** In 1+1 dimensions the continuous angle cannot order ([Mermin–Wagner–Coleman](../mermin-wagner-coleman.md)), but the two vacua ±K_ref can. A lattice Monte Carlo of the polarization angle at H = 1 finds ⟨|m|⟩ = 0.954 ± 0.0001 "at every size" (L = 16, 32 and 64; see flag 13 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md)) with the potential, and no true order without it (§4; [the frozen-H reduction](coset-model/frozen-h-reduction.md); [the Monte Carlo](coset-model/monte-carlo.md)).

#11 adds two qualifications in its refinement of P2′. "A definite polarization needs a ρ-preserving potential on that angle — a rigid, unordered pair of axes, so more structure than ω alone, though less than a rigid η." And "the breaking of ρ is physical only once matter couples to the sign of K (P4): without such a coupling, a twisted element ρ∘(K → −K) leaves the vacuum invariant" ([#11 §4](../../papers/broken-born-checkpoint-v2.md#4-postulates); [the twisted element](../twisted-element.md); [P4](../../program/postulates/p4-polarized-matter.md)).

Model II, the self-dual Grosse–Wulkenhaar model, was tried first and does not meet the criterion: its complex version breaks the position–momentum duality only classically ([quantum restoration](grosse-wulkenhaar/quantum-restoration.md)), and its real version has no duality symmetry to break ([Model II](grosse-wulkenhaar/_index.md)).

### The review behind it

The note's first version was graded B in round 4: "Referee: B (flawed but salvageable), confidence ~0.75. I agree." The reason: "The only claim of actual quantum symmetry breaking (§4, model I in 1+1) rests on a potential that is unbounded below once H is dynamical"; and "It is repairable." ([`review/round4-adjudication.md`](../../../review/round4-adjudication.md), 'Verdict'). The pre-registration had placed the weakest link there, on the rigid background the potential introduces, and the adjudication scored it "**Partial**: right location, missed severity" ([pre-registration](../../method/review/pre-registration.md)). Version 2 applies the accepted revisions, except the comparison with Langmann, Szabo and Zarembo's exact solution of a related model that revision 4 asked for, which it says it has not carried out (§4; [quantum restoration](grosse-wulkenhaar/quantum-restoration.md#open-the-comparison-with-the-exact-solution)). #11's item ends "Round-4 blind review: verdict B; v2 applies the accepted revisions", and the adjudication and the worklog record every accepted revision as applied (flag 42 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md)).

The referee's assessment of how spontaneous the 1+1 breaking is: with H frozen, an Ising-type breaking of the remaining ℤ₂, "But the potential fixes the unordered axis pair by hand, so the vacuum chooses only which of two pre-set axes is 'position'." With H dynamical, as the model was first written, the breaking was "not established" (audit notes, Step 3). The bounded potential answers the second point for the vacuum's stability; a simulation with H dynamical has not been run.

## How far it answers round 3

The worklog's assessment, written before round 4: "The round-3 critique ('the framework does no work') is only partly answered. The toy makes the program's structures cohere (η as order parameter; τ as the polarization angle), but matter's x-locality still enters through the P4-type coupling." It assigns the idea to prior work: "Prior art: FLM have the idea. The explicit realization appears new per S0." ('Assessment against the predictions'; FLM is Freidel–Leigh–Minic, [broken Born duality](../../phase-space/reciprocity/broken-born-duality.md)). Here τ is the program's dark-energy field, which it places on the polarization circle ([τ quintessence](../../cosmology/dark-energy/tau-quintessence.md)). The round-4 referee's searches found no earlier explicit model "with eta=omega K as a dynamical order parameter", and judged that "Model I appears new as a field theory, but it is a simple coset" (audit notes, Step 3).

The forecast written before construction: if S1–S4 passed and S5 failed, "acceptance criterion 1 as the referees worded it is too weak to answer 'the framework does no work'". It was scored "Hit": "Criterion 1 as worded is now met (coset + τ potential). The round-3 critique is only partly answered" ('Assessment against the predictions'). The τ potential of that scoring is the [naive ρ-preserving potential](coset-model/naive-potential.md), which is under review, and the verdict built on it is superseded ([below](#superseded-the-worklogs-first-verdict)). The matter-locality side is on [locality from an (H, K)-built coupling](../matter-coupling.md) and [Open: forced locality and the P4 lock](../strong-locality.md).

## Open: the parts not yet met

[#11 §14 item 11](../../papers/broken-born-checkpoint-v2.md#14-open-problems): "Still open [O]: a Monte Carlo with H dynamical; a derivation of the potential; locality of matter beyond the weak (Yukawa-like) form, which in the toy reduces to P4." The root [`CLAUDE.md`](../../../CLAUDE.md) lists the open ends of the toy Lagrangian as "a Monte Carlo with H dynamical; a derivation of the ρ-preserving potential; the strong form of matter locality; the real Grosse–Wulkenhaar model's one-loop preference for the position-sharp vacuum, a lead."

- **[A Monte Carlo with H dynamical](coset-model/dynamical-h-monte-carlo.md).** The ordered phase is established for the frozen-H reduction only. Whether ρ's compact SO(2) breaks in the coupled model, where the metric sector is a hyperbolic model that can order in two dimensions, is also open ([the frozen-H reduction](coset-model/frozen-h-reduction.md); [Open: does ρ's SO(2) break in the coupled model?](coset-model/so2-question.md)).
- **A derivation of the potential.** The potential that makes the polarization definite is chosen, not derived, and it "introduces a rigid, unordered pair of axes" (note §6; [Open: the origin of the ρ-preserving potential](../rho-preserving-potential.md)).
- **Locality beyond the weak form.** Matter becomes local in the selected polarization only if it interacts through a coupling built from (H, K), "as fermion masses follow from a Higgs vacuum value once Yukawa couplings are given. Nothing here forces that coupling." (note §5; [Goldstone modes and the Higgs mechanism](../goldstone-and-higgs.md); [Yukawa couplings](../../gravity/spin-2-fields/yukawa-forces.md#a-name-collision-the-yukawa-coupling); [Open: forced locality and the P4 lock](../strong-locality.md)).
- **The real-model lead.** Not part of #11's list: [Open: the real model's one-loop preference](grosse-wulkenhaar/real-model-lead.md).

All four are registered at [open problems](../../status/open-problems.md). The queue in the root [`CLAUDE.md`](../../../CLAUDE.md) adds one optional item for this work: "a round-6 review of the toy note, but only before any external use."

## The electric-sublattice clause

Two older wordings of the criterion ask more of η. The handoff: "η the order parameter also selecting the electric sublattice" ([`HANDOFF.md` §2](../../../HANDOFF.md#2-scientific-state-one-screen)). The withdrawn paper: η "selecting both the position polarization and the hidden sector's electric description" (the electric description of its separate copy of electromagnetism) ([§6](../../../notes/knot-dark-matter-standalone.md#6-status-of-claims-and-acceptance-criteria)). The clause ties the order parameter to the program's identification of electric–magnetic duality frames with phase-space polarizations ([the symplectic charge lattice](../../electric-magnetic-duality/symplectic-charge-lattice.md)). The worklog's statement of the referees' wording, its criteria S0–S5 and [#11 §14 item 11](../../papers/broken-born-checkpoint-v2.md#14-open-problems) omit the clause, and #11 declares the criterion met. The root [`CLAUDE.md`](../../../CLAUDE.md) wording, "done to the referees' wording", governs ([source conflicts](../../history/documents/source-conflicts.md#status-changes-since-the-handoff)). Nothing in the record addresses the clause. [#11 §11.4](../../papers/broken-born-checkpoint-v2.md#114-the-magnetic-mirror-conjecture-o-pr-v23) lists it first among what P.R.'s magnetic-mirror conjecture needs, in either form: "a mechanism by which one order parameter makes both choices (the electric-sublattice clause of acceptance criterion 1, never attempted; the toy models of §14 item 11 contain no gauge field)". The root [`CLAUDE.md`](../../../CLAUDE.md) lists it among its open items on monopoles, not queued ([Open: the electric-sublattice clause](../../electric-magnetic-duality/unified-modular-structure.md#open-the-electric-sublattice-clause); [what the conjecture needs](../../electric-magnetic-duality/magnetic-identification.md#what-it-needs)).

## Superseded: the worklog's first verdict

**The first statement.** Before round 4 the worklog declared: "**Verdict on acceptance criterion 1.** Met, in the referees' wording, by the coset toy plus a τ-type potential", with "It is spontaneously broken (Ising class in 1+1, Monte Carlo verified)." ('Assessment against the predictions').

**What replaced it.** [#11 §14 item 11](../../papers/broken-born-checkpoint-v2.md#14-open-problems): met "by the coset model of (H, K) with a bounded ρ-preserving potential", with "an ordered ℤ₂ phase in 1+1 in the frozen-H reduction".

**Why.** The "τ-type potential", −μ[Tr(K K_ref)]², is unbounded below once H is dynamical, so its intended vacuum is a saddle and the Monte Carlo had simulated a reduction with H frozen, not model I (round-4 findings F1 and F2, both upheld; [Under review: the naive ρ-preserving potential](coset-model/naive-potential.md)). Data at one temperature deep in the ordered phase establish order, not a universality class, so revision 1 replaced "Ising class" with "ordered ℤ₂ phase" ([the frozen-H reduction](coset-model/frozen-h-reduction.md)). The adjudicator had also checked the potential only at frozen H ('Rulings' F2). Round-4 lesson 1 became a rule of the program's [method](../../method/_index.md): when numerics run on a reduced model, check the unreduced model's stability ([reduced-model stability](../../method/verification/reduced-model-stability.md)). The register of [superseded statements](../../status/superseded.md) lists the "Ising class" wording.

## Beyond the withdrawn paper

The withdrawn paper's other two criteria served its own model, which placed its monopoles at points in space, a different object from P.R.'s candidate ([Conjecture: magnetic monopoles abundant in momentum space](../../dark-matter/candidates/momentum-space-monopoles.md)). Criterion 1 outlived the paper that stated it: round 3 made it "acceptance criterion 1 for anything the program proposes" (Decision 4), since it tests the program's [hard core](../../program/hard-core.md) rather than any one candidate.

## Sources

- [`wiki/papers/broken-born-checkpoint-v2.md` §14 item 11](../../papers/broken-born-checkpoint-v2.md#14-open-problems) — the current verdict and its open parts [O]
- [`wiki/papers/broken-born-checkpoint-v2.md` §4](../../papers/broken-born-checkpoint-v2.md#4-postulates) — the P2′ refinement: the potential's rigid pair of axes, the twisted element
- [`wiki/papers/broken-born-checkpoint-v2.md` §11.4](../../papers/broken-born-checkpoint-v2.md#114-the-magnetic-mirror-conjecture-o-pr-v23) — the electric-sublattice clause, "never attempted", listed first among what the magnetic-mirror conjecture needs [O]
- [`wiki/papers/broken-born-checkpoint-v2.md` §12](../../papers/broken-born-checkpoint-v2.md#12-the-dark-sector-question-three-candidates) — the third candidate, P.R.'s open conjecture, never modeled
- [`CLAUDE.md`](../../../CLAUDE.md) 'Since the handoff' — "done to the referees' wording"; the open ends, including the real-model lead; the optional round 6; the clause among the open items on monopoles
- [`wiki/papers/reciprocity-toy-models.md` §2](../../papers/reciprocity-toy-models.md#2-model-i-a-coset-sigma-model-of-h-k), [§4](../../papers/reciprocity-toy-models.md#4-quantum-stability), [§5](../../papers/reciprocity-toy-models.md#5-matter-and-locality), [§6](../../papers/reciprocity-toy-models.md#6-summary-and-limitations) — model I's symmetry, vacua and order parameter; the bounded potential and the Monte Carlo; the Yukawa analogy; "Not shown"
- [`review/round3-adjudication.md`](../../../review/round3-adjudication.md) 'Decisions' 4 — why the toy Lagrangian came next
- [`review/round4-adjudication.md`](../../../review/round4-adjudication.md) 'Verdict', 'Rulings' — the B grade; findings F1 and F2 and the adjudicator's account
- [`review/round4-preregistration.md`](../../../review/round4-preregistration.md) 'Predictions' — the predicted weakest link
- [`review/round4/referee/audit-notes.md`](../../../review/round4/referee/audit-notes.md) Step 3 — how spontaneous the 1+1 breaking is; the novelty of model I
- [`notes/toy-lagrangian.md`](../../../notes/toy-lagrangian.md) 'Success criteria', 'Assessment against the predictions' — the referees' wording and the two tiers; the first verdict, its prior-art statement and the scored forecast
- [`HANDOFF.md` §2](../../../HANDOFF.md#2-scientific-state-one-screen), [§6](../../../HANDOFF.md#6-review-history-and-the-measured-failure-mode), [§8 item 4](../../../HANDOFF.md#8-ranked-next-actions-queue) — the electric-sublattice wording; the criterion's adoption in round 1; the original queue item
- [`notes/knot-dark-matter-standalone.md` §1](../../../notes/knot-dark-matter-standalone.md#1-framework), [§6](../../../notes/knot-dark-matter-standalone.md#6-status-of-claims-and-acceptance-criteria) — the withdrawn paper's concession and its acceptance criteria
- [`review/round4-adjudication.md`](../../../review/round4-adjudication.md) 'Revisions for v2 of the note'; [`notes/toy-lagrangian.md`](../../../notes/toy-lagrangian.md) 'Write-up and review (2026-10-19/20)'; [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md) item 42 — every accepted revision recorded as applied, against the comparison version 2 did not make (pending)
