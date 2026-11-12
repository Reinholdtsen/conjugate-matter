---
title: "The 'framework does no work' critique"
weight: 60
status: record
description: "The referees' consensus over rounds 1–3 that nothing numerical in the dark-matter proposal depended on Born reciprocity; why it set the toy models as the next step, and how far they answer it."
sources:
  - "review/round3-preregistration.md 'Predictions'"
  - "review/round3/referee/audit-notes.md Step 4(d)"
  - "review/round3/referee/audit-notes.md Step 5"
  - "review/round3-adjudication.md 'Verdict'"
  - "review/round3-adjudication.md 'Pre-registration scored'"
  - "review/round3-adjudication.md 'Lessons'"
  - "review/round3-adjudication.md 'Decisions' 2, 4"
  - "notes/knot-dark-matter-standalone.md §1, §2, §6"
  - "HANDOFF.md §2"
  - "HANDOFF.md §3"
  - "HANDOFF.md §6"
  - "notes/toy-lagrangian.md 'Success criteria'"
  - "notes/toy-lagrangian.md 'Predictions'"
  - "notes/toy-lagrangian.md 'Chunk 4'"
  - "notes/toy-lagrangian.md 'Assessment against the predictions'"
  - "wiki/papers/broken-born-checkpoint-v2.md §12"
  - "wiki/papers/broken-born-checkpoint-v2.md §14 item 11"
  - "wiki/papers/broken-born-checkpoint-v2.md §11.4"
  - "wiki/papers/reciprocity-toy-models.md §5"
  - "review/round4-adjudication.md 'Rulings' F3"
  - "verify/toy_s5.py"
  - "CLAUDE.md 'Since the handoff'"
---

*"The framework does no work" is the referees' objection that the program's phase-space framework, [Born reciprocity](../phase-space/reciprocity/born-reciprocity.md) included, contributed nothing to the results of its dark-matter proposal. It was stated most fully in the [third review round](../method/review/round-3/_index.md), against [a withdrawn paper on monopole dark matter](../../notes/knot-dark-matter-standalone.md), which placed its monopoles at points in space, as ordinary particles of a separate copy of electromagnetism. The referee found that every number in it came from standard particle physics plus one choice of coupling, which the framework motivated but did not fix. The objection shaped what came next. The program retired the paper's model rather than claim a version of it that did not depend on the framework, and it made its next task an explicit model: an action in which reciprocity is a genuine symmetry that the vacuum breaks. The [toy models](../symmetry-breaking/toy-models/_index.md) meet the referees' wording of that demand, but by the program's assessment they answer the objection only in part, because the locality of ordinary matter in position still enters through an assumed coupling rather than following from the vacuum.*

**Status:** Record — untagged. A review finding: predicted as the weakest link in the round-3 pre-registration, returned as the referee's second weakest link (audit notes, Step 4(d) and Step 5), and the reason given for round-3 Decision 4. The toy models answer it "only partly" (toy worklog, 'Assessment against the predictions').

## The objection

In the referee's usage, a framework does work in a proposal when some number or choice in the proposal depends on it: remove the framework, and something changes or becomes undetermined. The round-3 pre-registration put the test in one sentence: "Nothing numerical depends on Born reciprocity, the compatibility theorem or the polarization identification." The referee's audit asked the question in its Step 4(d), "Does the phase-space framework do any work?", and answered "No."

The objection is about the dark-matter proposal under review, not a verdict on the program's other sectors. Round-3 Decision 4 drew the general consequence: an explicit action is "acceptance criterion 1 for anything the program proposes".

## The proposal it was made against

The paper under review, [`notes/knot-dark-matter-standalone.md`](../../notes/knot-dark-matter-standalone.md), now withdrawn, proposed monopoles of a separate copy of electromagnetism, which it identified "with the momentum-polarized half of a spontaneously broken Born reciprocity" (its Abstract) and described with ordinary kinematics, at points in space: a different object from P.R.'s candidate of monopoles localized in momentum ([Conjecture: magnetic monopoles abundant in momentum space](../dark-matter/candidates/momentum-space-monopoles.md)).

The paper was explicit about how little of the framework it used:

- **One choice of coupling.** It set the separate sector's smallest charge equal to the electron's, which fixes its monopoles' coupling through [Dirac quantization](../electric-magnetic-duality/monopoles/dirac-quantization.md). Its motivation: "reciprocity exchanges the two polarizations; if it acts on gauge couplings at all, the minimal action is to equate the elementary charges of the two sectors" ([its §2](../../notes/knot-dark-matter-standalone.md#2-the-hidden-sector-and-its-coupling)). The choice was motivated rather than derived.
- **Its use of the charge lattice.** [Its §2](../../notes/knot-dark-matter-standalone.md#2-the-hidden-sector-and-its-coupling) notes that the electric–magnetic charge lattice is a symplectic space and that "the S generator of electric-magnetic duality and the Born rotation are represented by the same matrix", then adds: "We use this only as motivation … No numerical result below depends on it." ([the symplectic charge lattice](../electric-magnetic-duality/symplectic-charge-lattice.md)).
- **Its status of reciprocity.** [Its §1](../../notes/knot-dark-matter-standalone.md#1-framework) conceded that "as usually encountered, rho is a unitary equivalence between representations of the canonical commutation relations, not a Noether symmetry of a specified action", and [§6](../../notes/knot-dark-matter-standalone.md#6-status-of-claims-and-acceptance-criteria) lists "that rho is a genuine, spontaneously broken symmetry" and its choice of coupling as conjectural ([unitary equivalence versus Noether symmetry](../phase-space/reciprocity/unitary-equivalence.md)).

## Before round 3

The demand that answers the objection is older than its name. In round 1 the referee asked for a toy Lagrangian, and the demand was "adopted as acceptance criterion [#1](../../notes/broken-born-theory.md)"; in round 2 the weakest link was the derivation of the paper's coupling ("'matrix coincidence ≠ physical identity' / 'numerology'"), the step that leaned on the shared matrix ([`HANDOFF.md` §6](../../HANDOFF.md#6-review-history-and-the-measured-failure-mode); [review rounds 1 and 2](../method/review/rounds-one-and-two.md)). [The handoff](../history/documents/handoff.md)'s list of open problems gives the criterion as a "Toy Lagrangian in which ρ is a genuine Noether symmetry, spontaneously broken, η the order parameter also selecting the electric sublattice (acceptance criterion #1; both reviewers independently named it)" ([`HANDOFF.md` §2](../../HANDOFF.md#2-scientific-state-one-screen)). The round-1 and round-2 reports themselves are not in the repository; P.R. holds them, and the handoff's §6 summarizes them ([`HANDOFF.md` §3](../../HANDOFF.md#3-artifact-inventory-creation-order)).

The documents frame the history in two ways. Round-3 Decision 4 reads the three rounds as one objection: "Every referee across three rounds converges on 'the framework does no work'." The toy worklog separates them: "The referees' wording (rounds 1–2): 'an action in which ρ is a genuine Noether symmetry, spontaneously broken, with η the order parameter'. Round 3 adds that the framework does no work." The paper's own criterion stated what such an action would add: deriving its choice of coupling from it "would make the coupling a prediction" ([its §6](../../notes/knot-dark-matter-standalone.md#6-status-of-claims-and-acceptance-criteria)), a coupling derived from the framework rather than chosen.

## Round 3: predicted and found

**The forecast.** The pre-registration, committed before the referee was dispatched, named the objection as the weakest link: "Nothing numerical depends on Born reciprocity, the compatibility theorem or the polarization identification." It expected "the auditor to say the dark-matter proposal stands or falls independently of the phase-space framework" ([`review/round3-preregistration.md`](../../review/round3-preregistration.md); [round-3 pre-registration](../method/review/round-3/preregistration.md)).

**The finding.** The referee's Step 4(d) gives the reasons for its "No":

- "The compatibility theorem (true) is never used after Sec. 1", and the choice of coupling "is motivated, not derived". The rest of the paper's assumptions "are all postulated", and its kinematics section treats its particles with ordinary relativistic quantum field theory.
- The proposal is a standard monopole model of published particle physics, which "stands or falls on that literature, independently of Born reciprocity".
- Even the choice of coupling does little: matching the separate sector's charge to e/3, the smallest charge in the Standard Model, instead of to the electron's charge e gives a different coupling (the referee's [`review/round3/referee/step2a.out`](../../review/round3/referee/step2a.out)), "and the framework gives no way to choose".

The referee's verdict was grade C (fundamentally flawed), with medium confidence. Its reason: the headline mass is wrong on two independent counts, every downstream number "hangs on it", "and the 'selected by phase-space duality' claim does no work" (Step 5). Its single weakest link was "the Kibble abundance / mass determination"; "Second: the framework does no work" ([round-3 verdict and rulings](../method/review/round-3/rulings.md)). The adjudication scored the forecast "**Miss on #1** (hit on [#2](../../notes/stream-stability.md))".

The same audit verified the compatibility theorem, the one framework result the paper cited, and identified it as "essentially the Born-geometry result of Freidel–Leigh–Minic", uncited in the paper; [the checkpoint](../history/documents/checkpoint.md) re-tagged it [T] in v2.1 ([the compatibility theorem](../phase-space/born-geometry/compatibility-theorem.md)).

**A caveat on blindness.** The referee's environment displayed a git status whose latest commit subject mentioned the pre-registered verdict. The referee's notes say it "was not consulted for any finding"; the adjudication adds that its verdict differed from the prediction, "which argues against anchoring. But the round was less blind than intended" ('Lessons' 1). Since then, predictions have been kept out of commit subjects.

## What the critique decided

Two of round 3's four decisions rest on it ([`review/round3-adjudication.md`](../../review/round3-adjudication.md), 'Decisions'; [round-3 decisions](../method/review/round-3/decisions.md)):

- **Decision 2: retire the paper's model.** Of the three ways forward, the low-mass version "works, but it is Murayama–Shu's and Liveoak–Maharana–Wells's model. Nothing in it depends on Born reciprocity (the referee and the pre-registration agree), so claiming it would add no testable content and would misattribute it." The model placed its monopoles at points in space, so the decision says nothing about P.R.'s candidate of monopoles localized in momentum, which has never been modeled ([#11 §12](../papers/broken-born-checkpoint-v2.md#12-the-dark-sector-question-three-candidates); [Conjecture: magnetic monopoles abundant in momentum space](../dark-matter/candidates/momentum-space-monopoles.md)).
- **Decision 4: the toy Lagrangian next.** "Every referee across three rounds converges on 'the framework does no work'. The toy action is the only item that can change that, and it is acceptance criterion 1 for anything the program proposes." "Candidate-level work is downstream of it." ([acceptance criterion 1](../symmetry-breaking/toy-models/acceptance-criterion.md)).

## The answer so far: the toy models

The toy worklog fixed its success criteria before building anything, and split them to match the two readings of the history: "The first tier is the referees' letter; the second is what would answer round 3" ([success criteria S0–S5](../symmetry-breaking/toy-models/success-criteria.md)). The first tier (S0–S3) asks for prior art checked, an action invariant under ρ, vacua that ρ permutes, and an [order parameter](../symmetry-breaking/order-parameter.md) built from η. The second tier asks that the breaking survive quantum fluctuations (S4) and that "the vacuum choice has a consequence for matter" (S5): matter coupled to the order parameter should interact locally in position in one vacuum and locally in momentum in its mirror. The worklog also forecast the outcome: if S1–S4 passed and S5 failed, acceptance criterion 1 "as the referees worded it is too weak to answer 'the framework does no work'" (toy worklog, 'Predictions').

**What was met.** [#11 §14 item 11](../papers/broken-born-checkpoint-v2.md#14-open-problems) records the criterion as "Met in the referees' wording by the coset model of (H, K) with a bounded ρ-preserving potential": ρ is a symmetry of an explicit action, and η = ωK is the order parameter; the vacuum is stable with H dynamical; and there is an ordered ℤ₂ phase in 1+1 dimensions in the [frozen-H reduction](../symmetry-breaking/toy-models/coset-model/frozen-h-reduction.md) ([Monte Carlo](../symmetry-breaking/toy-models/coset-model/monte-carlo.md)).

**What S5 found.** The weak form passes [V]: an interaction of matter built from H and K is local in position in the vacuum +K_ref and local in momentum in −K_ref, and for the toy-model note's test state the two vacua give 0.4070 and 0.3600 ([`verify/toy_s5.py`](../../verify/toy_s5.py), see [the toy-model scripts](../method/verification/toy-model-scripts.md); [locality from an (H, K)-built coupling](../symmetry-breaking/matter-coupling.md)). The strong form, locality forced rather than chosen, was not achieved. In the worklog's words: "The lock is P4 (x-polarized matter, and its ρ-image, p-polarized matter)", and "It does not derive x-locality from nothing" (toy worklog, 'Chunk 4'). The note: "Locality in the selected Lagrangian therefore follows from the vacuum once matter couples this way, as fermion masses follow from a Higgs vacuum value once Yukawa couplings are given. Nothing here forces that coupling" ([toy-model note §5](../papers/reciprocity-toy-models.md#5-matter-and-locality); [Yukawa couplings](../gravity/spin-2-fields/yukawa-forces.md#a-name-collision-the-yukawa-coupling)). The round-4 review added the [twisted element](../symmetry-breaking/twisted-element.md): without a coupling odd in K, the vacuum keeps a symmetry that acts on H exactly as ρ does, so the coupling is what gives the breaking physical content; the adjudication says this "sharpens the S5 conclusion rather than contradicting it" ([`review/round4-adjudication.md`](../../review/round4-adjudication.md), F3).

**The verdict.** The worklog's assessment scored the forecast a hit: "Criterion 1 as worded is now met (coset + τ potential). The round-3 critique is only partly answered." Its verdict paragraph: "The round-3 critique ('the framework does no work') is only partly answered. The toy makes the program's structures cohere (η as order parameter; τ as the polarization angle), but matter's x-locality still enters through the P4-type coupling." The worklog wrote this before round 4, when its potential was the "τ-type" form later found unbounded below ([Under review: the naive ρ-preserving potential](../symmetry-breaking/toy-models/coset-model/naive-potential.md)); [#11 §14 item 11](../papers/broken-born-checkpoint-v2.md#14-open-problems) gives the current statement, with [the bounded potential](../symmetry-breaking/toy-models/coset-model/bounded-potential.md).

## What remains unanswered

- **Forced locality.** [#11 §14 item 11](../papers/broken-born-checkpoint-v2.md#14-open-problems) keeps open "locality of matter beyond the weak (Yukawa-like) form, which in the toy reduces to P4" [O], together with [a Monte Carlo with H dynamical](../symmetry-breaking/toy-models/coset-model/dynamical-h-monte-carlo.md) and a derivation of the potential ([Open: forced locality and the P4 lock](../symmetry-breaking/strong-locality.md); [Open: the origin of the ρ-preserving potential](../symmetry-breaking/rho-preserving-potential.md)).
- **The electric sublattice.** The handoff's version of the criterion has η "also selecting the electric sublattice", and the withdrawn paper's has it selecting "the hidden sector's electric description" (the electric description of its separate copy of electromagnetism; [its §6](../../notes/knot-dark-matter-standalone.md#6-status-of-claims-and-acceptance-criteria)). The toy worklog's criteria and [#11 §14 item 11](../papers/broken-born-checkpoint-v2.md#14-open-problems) do not take up that clause; the root [`CLAUDE.md`](../../CLAUDE.md) describes the toy Lagrangian as "done to the referees' wording". The clause is unaddressed. The related conjecture, that the phase-space and charge-lattice polarizations are parts of one structure, is [Open: one modular structure for both polarizations (OP8)](../electric-magnetic-duality/unified-modular-structure.md). [#11 §11.4](../papers/broken-born-checkpoint-v2.md#114-the-magnetic-mirror-conjecture-o-pr-v23) lists the clause first among what stays open for P.R.'s magnetic-mirror conjecture, which #11 calls what [§11.3](../papers/broken-born-checkpoint-v2.md#113-the-identification-d--structural-math-t)'s conjecture would give "if one vacuum event selected both the position polarization and the electric sublattice": "a mechanism by which one order parameter makes both choices (the electric-sublattice clause of acceptance criterion 1, never attempted; the toy models of §14 item 11 contain no gauge field)" ([Conjecture: the momentum sector as the magnetic mirror](../electric-magnetic-duality/magnetic-identification.md#what-it-needs)).
- **Review.** The toy-model note has had one [blind review](../method/review/_index.md) (round 4, verdict B; [review round 4](../method/review/round-4.md)). The project's queue lists a round-6 review of the note as optional, "but only before any external use" (root [`CLAUDE.md`](../../CLAUDE.md)).

## Sources

- [`review/round3-preregistration.md`](../../review/round3-preregistration.md) 'Predictions' — the critique as the pre-registered weakest link
- [`review/round3/referee/audit-notes.md`](../../review/round3/referee/audit-notes.md) Step 4(d), Step 5 — the referee's finding, its verdict and the blindness note; [`review/round3/referee/step2a.out`](../../review/round3/referee/step2a.out) — the coupling variants
- [`review/round3-adjudication.md`](../../review/round3-adjudication.md) 'Verdict', 'Pre-registration scored', 'Lessons', 'Decisions' 2 and 4 — the verdict, the scoring, the blindness lesson and the decisions the critique drove, with the scope of Decision 2; the compatibility theorem identified as Freidel–Leigh–Minic's
- [`notes/knot-dark-matter-standalone.md`](../../notes/knot-dark-matter-standalone.md) Abstract, [§1](../../notes/knot-dark-matter-standalone.md#1-framework), [§2](../../notes/knot-dark-matter-standalone.md#2-the-hidden-sector-and-its-coupling), [§6](../../notes/knot-dark-matter-standalone.md#6-status-of-claims-and-acceptance-criteria) — the withdrawn paper, its choice of coupling, "No numerical result below depends on it", and its acceptance criteria
- [`HANDOFF.md` §2](../../HANDOFF.md#2-scientific-state-one-screen), [§3](../../HANDOFF.md#3-artifact-inventory-creation-order), [§6](../../HANDOFF.md#6-review-history-and-the-measured-failure-mode) — the criterion with its electric-sublattice clause; where the round-1 and round-2 reports are; the summaries of those rounds
- [`notes/toy-lagrangian.md`](../../notes/toy-lagrangian.md) 'Success criteria', 'Predictions', 'Chunk 4', 'Assessment against the predictions' — the two tiers, the forecast, the P4 lock and "only partly answered"
- [`wiki/papers/broken-born-checkpoint-v2.md` §12](../papers/broken-born-checkpoint-v2.md#12-the-dark-sector-question-three-candidates) — the withdrawn paper's model of a different object; §14 item 11 — what the toy models meet and what stays open; §11.4 — the electric-sublattice clause as the first open item of the magnetic-mirror conjecture [O]
- [`wiki/papers/reciprocity-toy-models.md` §5](../papers/reciprocity-toy-models.md#5-matter-and-locality) — "Nothing here forces that coupling"
- [`review/round4-adjudication.md`](../../review/round4-adjudication.md) 'Rulings' F3 — the twisted element
- [`verify/toy_s5.py`](../../verify/toy_s5.py) — the machine check of the weak form of S5
- [`CLAUDE.md`](../../CLAUDE.md) 'Since the handoff' — "done to the referees' wording", and the optional round 6
