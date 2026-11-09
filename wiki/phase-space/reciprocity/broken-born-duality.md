---
title: "Broken Born duality: the Freidel–Leigh–Minic precedent"
weight: 90
status: established
description: "Freidel, Leigh and Minic made η dynamical, wrote that a preferred polarization breaks Born duality and proposed to make the split into space and momentum space dynamical, carried by solutions; a later paper puts a breaking tied to the polarization in the vacuum, for a dual Lorentz symmetry that is not ρ; none gives a potential or an order parameter, and the spontaneous breaking of the exact ρ with η as order parameter is the program's addition."
provenance: [T]
sources:
  - "wiki/papers/broken-born-checkpoint-v2.md §3"
  - "wiki/papers/broken-born-checkpoint-v2.md ref [26]"
  - "wiki/papers/broken-born-checkpoint-v2.md ref [3]"
  - "wiki/papers/broken-born-checkpoint-v2.md §4"
  - "wiki/papers/broken-born-checkpoint-v2.md §5"
  - "wiki/papers/reciprocity-toy-models.md Abstract"
  - "wiki/papers/reciprocity-toy-models.md §1"
  - "wiki/papers/reciprocity-toy-models.md ref [1]"
  - "notes/toy-lagrangian.md 'Success criteria'"
  - "notes/toy-lagrangian.md 'Chunk 1 results'"
  - "notes/toy-lagrangian.md 'Chunk 4 (in progress, 2026-10-19): S5'"
  - "review/round3/referee/audit-notes.md Step 1"
  - "review/round3-adjudication.md 'What survives v3'"
  - "review/round3-adjudication.md 'Decisions'"
  - "review/round4/referee/audit-notes.md Step 1"
  - "review/round4/referee/audit-notes.md Step 3"
  - "review/round4-adjudication.md 'Rulings'"
  - "notes/dual-sector.md §4"
  - "notes/dual-sector.md §8"
  - "notes/dual-sector.md §9"
  - "review/wiki-build-flags.md items 70, 71"
  - "notes/broken-born-program-v1.md §1"
  - "popsci/angle-of-the-mirror.md opening"
---

*Broken Born duality is Freidel, Leigh and Minic's phrase for what happens when all physical probes agree on which phase-space directions are space-time: the agreement is a preferred polarization, a preferred choice of which directions count as position, and it breaks the position–momentum symmetry they call Born duality. In their work on [Born geometry](../born-geometry/_index.md) and metastring theory they made the [neutral metric η](../born-geometry/born-structures.md) dynamical and described space-time as a choice of Lagrangian subspace. They call the split of phase space into space and momentum space kinematical in general relativity, and propose to make it dynamical, carried by the solutions of the theory rather than by its formulation. A later paper of theirs places a symmetry breaking tied to the choice of polarization in the vacuum, but for another symmetry, one of the doubled phase space of their string theory, not Born duality. None of these papers gives a potential for η or an order parameter. The program's central idea therefore has a literature precedent. The program's [checkpoint](../../history/documents/checkpoint.md) credits them, and claims as its own the reading of the breaking as spontaneous, with η as the order parameter; what was not found in their papers is the spontaneous breaking of Born duality itself, exact in the laws, with η as order parameter and a potential.*

**Status:** Established — literature, with live-searched citations [S] ([#11](../../papers/broken-born-checkpoint-v2.md) ref. [26]; the worklog's prior-art search); the [round-4](../../method/review/round-4.md) referee found the quotation verbatim in the source; [#11 §3](../../papers/broken-born-checkpoint-v2.md#3-the-question) gives the credit.

## The statement

[#11 §3](../../papers/broken-born-checkpoint-v2.md#3-the-question) quotes Freidel, Leigh and Minic: "if all probes agree on what we mean by space-time, then we have broken Born duality — there is a preferred choice of polarization, the space-time one" [26S, p. 3]. It goes on: "They treat the breaking as kinematical and call the choice 'a dynamical question'."

In the metastring paper ([arXiv:1502.08005](https://arxiv.org/abs/1502.08005)) and in their Int. J. Mod. Phys. D paper of 2014, "kinematical" is the word for general relativity's split of phase space, which they credit to Born, and their proposal is the reverse: "the purely kinematical splitting of phase space into space and momentum space has to be made dynamical" ([Freidel, Leigh and Minic 2014, Int. J. Mod. Phys. D](https://arxiv.org/abs/1405.3949), §1.3). #11's "They treat the breaking as kinematical" gives their description of general relativity, not their proposal ([`notes/dual-sector.md` §8](../../../notes/dual-sector.md#8-the-vacuum-and-the-choice-of-polarization); flag 70, pending).

"Born duality" is their name for [Born reciprocity](born-reciprocity.md), the quarter-turn (x, p) → (p, −x). A polarization is a choice of [Lagrangian subspace](lagrangian-polarizations.md) to serve as position. Their sentence links the two: a world in which every probe reads the same directions as space-time has a preferred polarization, and a preferred polarization is not invariant under the duality, which exchanges it with its partner.

The referee of [review round 4](../../method/review/round-4.md) retrieved the source and found the quotation verbatim in the metastring paper's source file (audit notes, Step 1, ref. [1c]).

## What Freidel, Leigh and Minic built

Their work, as the program's documents report it:

- **Born geometry.** Phase space carrying a [symplectic form](symplectic-form.md) ω, a neutral metric η and a generalized metric H, with I = ω⁻¹H, J = η⁻¹H and K = η⁻¹ω forming a split-quaternion algebra ([#11 §5](../../papers/broken-born-checkpoint-v2.md#5-the-kinematic-core-and-the-compatibility-theorem), ref. [3]†). The citation audit of [review round 3](../../method/review/round-3/_index.md) found the name at p. 11 of the metastring paper: such phase spaces "were referred to as Born geometries" (audit notes, Step 1). See [the structures ω, η, H](../born-geometry/born-structures.md).
- **A dynamical η.** In [arXiv:1307.7080](https://arxiv.org/abs/1307.7080), "both elements (η, J) of the chiral structure are dynamical. The solutions are labelled by bi-Lagrangians and spacetime is a derived dynamical concept"; [arXiv:1405.3949](https://arxiv.org/abs/1405.3949) "ties fixed η to locality and finds linearized solutions that depend 'only on X or only on P'" (worklog, "Chunk 1 results"). The round-4 referee confirmed the second paper's "we have to make eta dynamical" (audit notes, Step 1, ref. [1b]).
- **The split carried by solutions.** In the Int. J. Mod. Phys. D paper quoted above (§2), the split of phase space belongs to solutions, not to the formulation: "This formulation does not require the presence of a bi-Lagrangian structure" K, the structure whose two eigenspaces are a transverse pair of Lagrangian subspaces, such as the position and momentum halves of phase space [T]; "However when we look at solutions of string theory, we find this extra structure." A split absent from the formulation and present in its solutions has the logical form of a spontaneous breaking, without the word, a potential or an order parameter ([`notes/dual-sector.md` §8](../../../notes/dual-sector.md#8-the-vacuum-and-the-choice-of-polarization)).
- **Space-time as a choice of Lagrangian.** "Freidel, Leigh and Minic make η dynamical and describe spacetime as a choice of Lagrangian [1]" ([toy-model note §1](../../papers/reciprocity-toy-models.md#1-setting-and-prior-work)).
- **The section condition from locality.** In double field theory and its relatives, fields depend on only half of the doubled coordinates. The metastring paper derives this from worldsheet locality (§6 of [arXiv:1502.08005](https://arxiv.org/abs/1502.08005); worklog, chunk 4, "S5 literature"). The worklog listed it with the other derivations and wrote "Every derivation selects only the pair"; round 4 restricted that statement to d = 1, and the toy note says only that the derivations it cites leave the section undetermined within a family, "a pair for d = 1, a continuous family for d > 1" ([§1](../../papers/reciprocity-toy-models.md#1-setting-and-prior-work)). Which member is space-time stays open. See [double field theory](../born-geometry/double-field-theory.md) and [the section condition](../../symmetry-breaking/section-condition.md).
- **The compatibility statement.** "writing the η-compatible H in terms of (G, B), H is related to ω through a complex structure exactly when B vanishes [26S, §2.1]" ([#11 §5](../../papers/broken-born-checkpoint-v2.md#5-the-kinematic-core-and-the-compatibility-theorem)). This is the statement of the program's [compatibility theorem](../born-geometry/compatibility-theorem.md), which [#11 §5](../../papers/broken-born-checkpoint-v2.md#5-the-kinematic-core-and-the-compatibility-theorem) credits to them. Its positive form, H = diag(q, q⁻¹) with q positive, is stated in group language in [Freidel, Leigh and Minic 2016](https://arxiv.org/abs/1606.01829) (§2), without the block proof ([`notes/dual-sector.md` §9](../../../notes/dual-sector.md#9-other-overlaps); flag 71, pending).

## What they did not do

The worklog's prior-art search, with every citation retrieved [S], concluded: "**They have priority on the idea and must be cited.** They write no potential and do no symmetry-breaking analysis, and call Born's breaking kinematical, not spontaneous." (worklog, "Chunk 1 results"). The round-4 referee searched the three papers' sources for "spontan" and found no symmetry-breaking analysis, consistent with that verdict (audit notes, Step 1).

In their papers "kinematical" names general relativity's split, which they propose to make dynamical ([the statement](#the-statement)). Two later papers, each with Minic among its authors, go further, though not to a potential: one ([Freidel, Kowalski-Glikman, Leigh and Minic 2021](https://arxiv.org/abs/2104.00802)) places a symmetry breaking tied to the choice of polarization in the vacuum, for the dual Lorentz symmetry of their doubled phase space, which is not ρ, and another ([Berglund, Hübsch and Minic 2023](https://arxiv.org/abs/2212.06086), §4.3) calls that symmetry "effectively spontaneously broken". None of them gives a potential, an order parameter or a [Goldstone angle](../../symmetry-breaking/goldstone-angle.md) ([neighbours in the literature](#neighbours-in-the-literature); [`notes/dual-sector.md` §8](../../../notes/dual-sector.md#8-the-vacuum-and-the-choice-of-polarization); flag 70, pending).

## The program's addition

- **Spontaneous breaking.** [#11 §3](../../papers/broken-born-checkpoint-v2.md#3-the-question): "This program's addition is to read it as *spontaneous* breaking, with η as the order parameter (§5; the toy models in [`wiki/papers/reciprocity-toy-models.md`](../../papers/reciprocity-toy-models.md))." In [spontaneous symmetry breaking](../../symmetry-breaking/spontaneous-symmetry-breaking.md) the laws keep a symmetry that their lowest-energy state lacks; the program applies this to Born duality, with the vacuum choosing the polarization ([the hard core](../../program/hard-core.md)).
- **η as the order parameter.** P2′: "That η should be dynamical rather than fixed was argued independently in metastring theory [26S]; the reading of η as the order parameter of broken reciprocity is this program's." ([#11 §4](../../papers/broken-born-checkpoint-v2.md#4-postulates); [P2′](../../program/postulates/p2-prime.md); [the order parameter](../../symmetry-breaking/order-parameter.md)).
- **An explicit model.** The toy-model note's [model I](../../symmetry-breaking/toy-models/coset-model/_index.md) is an action in which ρ is an exact symmetry and the vacuum breaks it, with η = ωK as order parameter, under caveats the note states: [the twisted element](../../symmetry-breaking/twisted-element.md), and order shown only in [the frozen-H reduction](../../symmetry-breaking/toy-models/coset-model/frozen-h-reduction.md) ([toy models of broken reciprocity](../../symmetry-breaking/toy-models/_index.md); [acceptance criterion 1](../../symmetry-breaking/toy-models/acceptance-criterion.md)). Its abstract: "The idea has been stated before, but we found no explicit model of ρ itself being spontaneously broken."

What was not found in their papers is narrower than "spontaneous breaking": the spontaneous breaking of the exact ρ, which preserves ω, with η as order parameter, a ρ-preserving potential and a Goldstone angle, and the toy models' explicit action; a breaking tied to the choice of polarization in the vacuum, for another symmetry, is published ([neighbours in the literature](#neighbours-in-the-literature); [`notes/dual-sector.md` §8](../../../notes/dual-sector.md#8-the-vacuum-and-the-choice-of-polarization); flag 70, pending).

## Is there an earlier explicit model?

The worklog's search found none: "**no existing action has Born reciprocity exactly symmetric and spontaneously broken with η or K as order parameter.** Zero phrase hits on INSPIRE full text and arXiv abstracts. INSPIRE's coverage is incomplete, so this is evidence of absence, not proof." (worklog, "Chunk 1 results").

The round-4 referee repeated the search independently. Full-text searches for "Langmann-Szabo duality" with "spontaneous" (6 hits) and for "Born reciprocity" with "spontaneously broken" (14 hits) turned up no prior explicit model in which vacua spontaneously break the [Langmann–Szabo duality](../../symmetry-breaking/toy-models/grosse-wulkenhaar/noncommutative-field-theory.md) (audit notes, Step 1). Its conceptual audit adds that no prior model "with eta=omega K as a dynamical order parameter" turned up either (Step 3).

The nearest case in the literature is Smolin's [arXiv:2007.05957](https://arxiv.org/abs/2007.05957), an explicit model in which a larger symmetry, a triality, is spontaneously broken; the referee said it "partially undercuts" the claim of no explicit model. The adjudication ruled that it does not contradict it: "Smolin breaks a triality *down to* Born duality, leaving it unbroken, so it does not contradict 'no model breaks ρ itself'. It still has to be cited." (round-4 adjudication, "Rulings"). The toy note cites it.

The dual-sector note's reading of the papers of Freidel, Leigh, Minic and their coauthors found no such model either ([`notes/dual-sector.md` §8](../../../notes/dual-sector.md#8-the-vacuum-and-the-choice-of-polarization)).

## Neighbours in the literature

Work near the idea, as the toy note, the worklog and the dual-sector note ([`notes/dual-sector.md` §8](../../../notes/dual-sector.md#8-the-vacuum-and-the-choice-of-polarization)) list it:

- **A selection rule, stated in words.** Freidel, Rudolph and Svoboda ([arXiv:1706.07089](https://arxiv.org/abs/1706.07089)) suggest the choice "might be subject to a dynamical selection rule" ([toy-model note §1](../../papers/reciprocity-toy-models.md#1-setting-and-prior-work)). The referee notes that the subject of their sentence is "the kinematical structure of spacetime itself", not literally the choice, and calls the paraphrase acceptable (audit notes, Step 1, ref. [2]).
- **Polarization by gauging.** "Born sigma models choose the polarization by gauging [3]" ([toy-model note §1](../../papers/reciprocity-toy-models.md#1-setting-and-prior-work)): Marotta and Szabo, [arXiv:1910.09997](https://arxiv.org/abs/1910.09997), where the polarization is part of the target structure rather than a field (audit notes, Step 1).
- **Broken O(D, D).** Angus, Kim and Park ([arXiv:2111.07947](https://arxiv.org/abs/2111.07947)) break the doubled symmetry of double field theory spontaneously, but "there H is the order parameter, with η fixed" (worklog, "Chunk 1 results").
- **A contraction.** Govaerts, Jarvis, Morgan and Low ([arXiv:0706.3736](https://arxiv.org/abs/0706.3736)): "contraction, not breaking" (worklog).
- **Claims in words only.** Bernardo, Brandenberger and Franzmann ([arXiv:1901.01209](https://arxiv.org/abs/1901.01209)), whose support is "a personal communication"; the worklog finds that a mechanism picking one section over its partner is open in the literature (chunk 4, "S5 literature").
- **A breaking in the vacuum sector.** [Freidel, Kowalski-Glikman, Leigh and Minic 2021](https://arxiv.org/abs/2104.00802) work in the doubled phase space of metastring theory, in which a dual coordinate x̃, with a momentum of its own, joins x and fails to commute with it. "The symmetry breaking happens at the level of the vacuum sector, and thus a choice of ground state fixes a value of" the parameter that fixes which commuting combination of x and x̃ serves as spacetime, and "We now propose that the expansion of the Universe can act as a mechanism that selects the decoupling frame". The broken symmetry is the dual Lorentz symmetry of the doubled space, which they call "fundamentally broken at the quantum level" because its action is not a canonical transformation, one that preserves the symplectic form; it is not ρ, which preserves ω. The paper gives no potential and no order parameter.
- **The dual Lorentz group, called spontaneously broken.** [Berglund, Hübsch and Minic 2023](https://arxiv.org/abs/2212.06086) (§4.3) say of the same symmetry, the dual Lorentz group O(1, d−1)₂, that within the sector of fixed non-zero dual momentum p̃ it "is effectively spontaneously broken". Again the symmetry is not ρ, and no potential or order parameter is given.
- **A speculation in a thesis.** [Yargic 2021](https://inspirehep.net/literature/1923123), a doctoral thesis at the University of Waterloo with Freidel on the committee, works on one phase space at ℏ, as the program does. It suggests that if a modular gauge symmetry "is somehow broken, this may be used as a mechanism to fix the quantum configuration space", and that this "may explain the absence of Born reciprocity between position and momentum variables in the classical world". It gives no potential or order parameter.

The other overlaps of these authors' papers with the program, and the proposal of Minic and coauthors that dark matter is the dual of visible matter, are on [the dual Standard Model](../../dark-matter/conjugate-matter/dual-standard-model.md#further-overlaps-with-the-program).

## How the credit entered the program

The program reached Freidel, Leigh and Minic twice, and the same way each time: a statement it had presented as its own was found in their papers.

1. **The idea uncredited.** [The v1 paper](../../history/documents/checkpoint.md) presents the move without credit: "promote ρ to an exact, spontaneously broken symmetry" ([#9 §1](../../../notes/broken-born-program-v1.md#1-the-question)). The [popular article](../../history/documents/popular-articles.md) [#10](../../../popsci/angle-of-the-mirror.md) describes [Born's question](../../program/borns-question.md) as having "spent eighty-eight years in a drawer" (opening); it predates both credits below.
2. **The compatibility theorem (round 3, 2026-10-19).** The round-3 referee found the compatibility statement in the metastring paper and listed it under "Uncited claims / prior art that should be cited" (audit notes, Step 1). The adjudication kept the theorem only as literature, pending a comparison with Freidel, Leigh and Minic ("What survives v3"), and made checking that prior art part of the cleanup before the toy Lagrangian (decision 4). [#11 §5](../../papers/broken-born-checkpoint-v2.md#5-the-kinematic-core-and-the-compatibility-theorem) tags the theorem [T][V] and credits them; the machine check is battery test T1 ([the verification battery](../../method/verification/battery.md)).
3. **The lesson as a rule.** The toy-model worklog made a prior-art search its first success criterion, S0 ([success criteria S0–S5](../../symmetry-breaking/toy-models/success-criteria.md)), citing that episode: "(Lesson of the compatibility theorem, which turned out to be Freidel–Leigh–Minic's.)" (worklog, "Success criteria").
4. **Broken Born duality.** The S5 literature search (worklog, chunk 4) found the quotation, and the worklog recorded: "**[#11 §3](../../papers/broken-born-checkpoint-v2.md#3-the-question) must cite FLM for the idea.** What is the program's own: the order-parameter (spontaneous) formulation and its consequences." (chunk 4; FLM is Freidel–Leigh–Minic). [#11 §3](../../papers/broken-born-checkpoint-v2.md#3-the-question) gives the attribution.

## References

- #11 [26][S] L. Freidel, R. G. Leigh, D. Minic, "Metastring theory and modular space-time," JHEP 06 (2015) 006, [arXiv:1502.08005](https://arxiv.org/abs/1502.08005) — the toy note's [1c].
- #11 [3]† L. Freidel, R. G. Leigh, D. Minic, "Born reciprocity in string theory and the nature of spacetime," Phys. Lett. B 730, 302 (2014); "Quantum gravity, dynamical phase space and string theory," Int. J. Mod. Phys. D 23, 1442006 (2014). The toy note lists the same two papers as [1a] ([arXiv:1307.7080](https://arxiv.org/abs/1307.7080)) and [1b] ([arXiv:1405.3949](https://arxiv.org/abs/1405.3949)), and the round-4 referee retrieved both and confirmed the statements attributed to them (audit notes, Step 1). #11 still marks [3] †.
- Toy-model note [2] (Freidel–Rudolph–Svoboda), [3] (Marotta–Szabo) and [4] (Smolin), all retrieved.
- Read for [`notes/dual-sector.md`](../../../notes/dual-sector.md) [S]: L. Freidel, R. G. Leigh, D. Minic, "Quantum Spaces are Modular," Phys. Rev. D 94, 104052 (2016), [arXiv:1606.01829](https://arxiv.org/abs/1606.01829); L. Freidel, J. Kowalski-Glikman, R. G. Leigh, D. Minic, "Quantum gravity phenomenology in the infrared," Int. J. Mod. Phys. D 30, 2141002 (2021), [arXiv:2104.00802](https://arxiv.org/abs/2104.00802); P. Berglund, T. Hübsch, D. Minic, "On de Sitter Spacetime and String Theory," Int. J. Mod. Phys. D 32, 2330002 (2023), [arXiv:2212.06086](https://arxiv.org/abs/2212.06086); Y. Yargic, "Born Reciprocal Representations of the Quantum Algebra," doctoral thesis, University of Waterloo (2021), [INSPIRE 1923123](https://inspirehep.net/literature/1923123).

## Used by

- [The hard core: spontaneously broken Born reciprocity](../../program/hard-core.md) — the spontaneous reading is the program's addition to this precedent.
- [Mandatory breaking: the uncertainty argument](../../symmetry-breaking/mandatory-breaking.md) — [#11 §3](../../papers/broken-born-checkpoint-v2.md#3-the-question) credits the preferred-polarization idea here.
- [P2′: only the symplectic form is rigid](../../program/postulates/p2-prime.md) — η dynamical, as in metastring theory.
- [P5: the vacuum selects a polarization](../../program/postulates/p5-spontaneous-selection.md) — the preferred-polarization idea is credited here.
- [The order parameter: J, η and K](../../symmetry-breaking/order-parameter.md) — η as the order parameter, the program's own step.
- [The compatibility theorem](../born-geometry/compatibility-theorem.md) — the same authors' statement, which [#11 §5](../../papers/broken-born-checkpoint-v2.md#5-the-kinematic-core-and-the-compatibility-theorem) credits to them.
- [Acceptance criterion 1: the toy Lagrangian](../../symmetry-breaking/toy-models/acceptance-criterion.md) — the explicit model the literature lacked.
- [Model I: action and symmetries](../../symmetry-breaking/toy-models/coset-model/action-and-symmetries.md) — the prior-art survey that credits the idea and finds no earlier action.

## Sources

- [`wiki/papers/broken-born-checkpoint-v2.md` §3](../../papers/broken-born-checkpoint-v2.md#3-the-question) and ref. [26] — the quotation, the attribution, and what the program adds.
- [`wiki/papers/broken-born-checkpoint-v2.md` §4](../../papers/broken-born-checkpoint-v2.md#4-postulates), [§5](../../papers/broken-born-checkpoint-v2.md#5-the-kinematic-core-and-the-compatibility-theorem) and ref. [3] — P2′ on metastring theory; the compatibility statement and its attribution; Born geometry.
- [`wiki/papers/reciprocity-toy-models.md`](../../papers/reciprocity-toy-models.md) Abstract, [§1](../../papers/reciprocity-toy-models.md#1-setting-and-prior-work) and ref. [1] — prior work: the idea, the selection rule, Born sigma models, Smolin; "no explicit model".
- [`review/round3-adjudication.md`](../../../review/round3-adjudication.md) "What survives v3", "Decisions" — the theorem kept as literature pending the comparison; the cleanup in decision 4.
- [`review/round4-adjudication.md`](../../../review/round4-adjudication.md) "Rulings" — Smolin does not contradict "no model breaks ρ itself"; the section "pair" holds only for d = 1.
- [`review/round3/referee/audit-notes.md`](../../../review/round3/referee/audit-notes.md) Step 1 — the compatibility statement and "Born geometries" found in the metastring paper.
- [`review/round4/referee/audit-notes.md`](../../../review/round4/referee/audit-notes.md) Step 1, Step 3 — the quotation verbatim; refs [1a]–[2] checked; the independent search for an earlier model.
- [`notes/toy-lagrangian.md`](../../../notes/toy-lagrangian.md) "Success criteria", "Chunk 1 results", chunk 4 — S0 and its reason; the live-searched prior-art survey and the priority verdict; the section-selection literature and the instruction to credit the idea.
- [`notes/dual-sector.md` §4](../../../notes/dual-sector.md#4-what-their-dual-is), [§8](../../../notes/dual-sector.md#8-the-vacuum-and-the-choice-of-polarization), [§9](../../../notes/dual-sector.md#9-other-overlaps) — the doubled phase space of metastring theory, with a dual coordinate x̃ that has its own momentum; "kinematical" as their word for general relativity's split, the split made dynamical and carried by solutions; the vacuum-sector breaking of the dual Lorentz symmetry and "effectively spontaneously broken"; the Yargic thesis; what was not found; the positive form of the compatibility statement in the 2016 paper.
- [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md) items 70, 71 — [#11 §3](../../papers/broken-born-checkpoint-v2.md#3-the-question)'s attribution and [§5](../../papers/broken-born-checkpoint-v2.md#5-the-kinematic-core-and-the-compatibility-theorem)'s compatibility statement; pending.
- [`notes/broken-born-program-v1.md` §1](../../../notes/broken-born-program-v1.md#1-the-question) — the program's move, uncredited (v1).
- [`popsci/angle-of-the-mirror.md`](../../../popsci/angle-of-the-mirror.md) opening — "eighty-eight years in a drawer" (popular article; never a status source).
