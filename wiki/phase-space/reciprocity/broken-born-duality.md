---
title: "Broken Born duality: the Freidel–Leigh–Minic precedent"
weight: 90
status: established
description: "Freidel, Leigh and Minic made η dynamical and wrote that a preferred polarization breaks Born duality; they gave no potential and no symmetry-breaking analysis, and reading the breaking as spontaneous, with η as order parameter, is the program's addition."
provenance: [T]
sources:
  - "papers/broken-born-checkpoint-v2.md §3"
  - "papers/broken-born-checkpoint-v2.md ref [26]"
  - "papers/broken-born-checkpoint-v2.md ref [3]"
  - "papers/broken-born-checkpoint-v2.md §4"
  - "papers/broken-born-checkpoint-v2.md §5"
  - "papers/reciprocity-toy-models.md Abstract"
  - "papers/reciprocity-toy-models.md §1"
  - "papers/reciprocity-toy-models.md ref [1]"
  - "notes/toy-lagrangian.md 'Success criteria'"
  - "notes/toy-lagrangian.md 'Chunk 1 results'"
  - "notes/toy-lagrangian.md 'Chunk 4 (in progress, 2026-10-19): S5'"
  - "review/round3/referee/audit-notes.md Step 1"
  - "review/round3-adjudication.md 'What survives v3'"
  - "review/round3-adjudication.md 'Decisions'"
  - "review/round4/referee/audit-notes.md Step 1"
  - "review/round4/referee/audit-notes.md Step 3"
  - "review/round4-adjudication.md 'Rulings'"
  - "notes/broken-born-program-v1.md §1"
  - "popsci/angle-of-the-mirror.md opening"
---

*Broken Born duality is Freidel, Leigh and Minic's phrase for what happens when all physical probes agree on which phase-space directions are space-time: the agreement is a preferred polarization, a preferred choice of which directions count as position, and it breaks the position–momentum symmetry they call Born duality. In their work on Born geometry and metastring theory they made the [neutral metric η](/wiki/phase-space/born-geometry/born-structures) dynamical and described space-time as a choice of Lagrangian subspace, but they wrote no potential for η and treated the breaking as kinematical, not as spontaneous symmetry breaking. The program's central idea therefore has a literature precedent. Since version 2.2 the program's checkpoint credits them, and claims as its own only the reading of the breaking as spontaneous, with η as the order parameter.*

**Status:** Established — literature, with live-searched citations [S] (#11 ref. [26]; the worklog's prior-art search); the round-4 referee found the quotation verbatim in the source — the credit was added to #11 §3 in version 2.2 (2026-10-20).

## The statement

#11 §3 quotes Freidel, Leigh and Minic: "if all probes agree on what we mean by space-time, then we have broken Born duality — there is a preferred choice of polarization, the space-time one" [26S, p. 3]. It goes on: "They treat the breaking as kinematical and call the choice 'a dynamical question'."

"Born duality" is their name for [Born reciprocity](/wiki/phase-space/reciprocity/born-reciprocity), the quarter-turn (x, p) → (p, −x). A polarization is a choice of [Lagrangian subspace](/wiki/phase-space/reciprocity/lagrangian-polarizations) to serve as position. Their sentence links the two: a world in which every probe reads the same directions as space-time has a preferred polarization, and a preferred polarization is not invariant under the duality, which exchanges it with its partner.

The referee of [review round 4](/wiki/method/review/round-4) retrieved the source and found the quotation verbatim in the metastring paper's source file (audit notes, Step 1, ref. [1c]).

## What Freidel, Leigh and Minic built

Their work, as the program's documents report it:

- **Born geometry.** Phase space carrying a symplectic form ω, a neutral metric η and a generalized metric H, with I = ω⁻¹H, J = η⁻¹H and K = η⁻¹ω forming a split-quaternion algebra (#11 §5, ref. [3]†). The citation audit of [review round 3](/wiki/method/review/round-3) found the name at p. 11 of the metastring paper: such phase spaces "were referred to as Born geometries" (audit notes, Step 1). See [the structures ω, η, H](/wiki/phase-space/born-geometry/born-structures).
- **A dynamical η.** In arXiv:1307.7080, "both elements (η, J) of the chiral structure are dynamical. The solutions are labelled by bi-Lagrangians and spacetime is a derived dynamical concept"; arXiv:1405.3949 "ties fixed η to locality and finds linearized solutions that depend 'only on X or only on P'" (worklog, "Chunk 1 results"). The round-4 referee confirmed the second paper's "we have to make eta dynamical" (audit notes, Step 1, ref. [1b]).
- **Space-time as a choice of Lagrangian.** "Freidel, Leigh and Minic make η dynamical and describe spacetime as a choice of Lagrangian [1]" (toy-model note §1).
- **The section condition from locality.** In double field theory and its relatives, fields depend on only half of the doubled coordinates. The metastring paper derives this from worldsheet locality (§6 of arXiv:1502.08005; worklog, chunk 4, "S5 literature"). Like the other derivations, it leaves the section undetermined within a family, "a pair for d = 1, a continuous family for d > 1" (toy-model note §1); the worklog's "Every derivation selects only the pair" was restricted to d = 1 in round 4. Which member is space-time stays open. See [double field theory](/wiki/phase-space/born-geometry/double-field-theory) and [the section condition](/wiki/symmetry-breaking/section-condition).
- **The compatibility statement.** "writing the η-compatible H in terms of (G, B), H is related to ω through a complex structure exactly when B vanishes [26S, §2.1]" (#11 §5). This is the statement of the program's [compatibility theorem](/wiki/phase-space/born-geometry/compatibility-theorem), credited to them since #11 v2.1.

## What they did not do

The worklog's prior-art search, with every citation retrieved [S], concluded: "**They have priority on the idea and must be cited.** They write no potential and do no symmetry-breaking analysis, and call Born's breaking kinematical, not spontaneous." (worklog, "Chunk 1 results"). The round-4 referee searched the three papers' sources for "spontan" and found no symmetry-breaking analysis, consistent with that verdict (audit notes, Step 1).

## The program's addition

- **Spontaneous breaking.** #11 §3: "This program's addition is to read it as *spontaneous* breaking, with η as the order parameter (§5; the toy models in `papers/reciprocity-toy-models.md`)." In [spontaneous symmetry breaking](/wiki/symmetry-breaking/spontaneous-symmetry-breaking) the laws keep a symmetry that their lowest-energy state lacks; the program applies this to Born duality, with the vacuum choosing the polarization ([the hard core](/wiki/program/hard-core)).
- **η as the order parameter.** P2′: "That η should be dynamical rather than fixed was argued independently in metastring theory [26S]; the reading of η as the order parameter of broken reciprocity is this program's." (#11 §4; [P2′](/wiki/program/postulates/p2-prime); [the order parameter](/wiki/symmetry-breaking/order-parameter)).
- **An explicit model.** The toy-model note builds actions in which ρ is an exact symmetry and the vacuum breaks it, with η = ωK as order parameter, under caveats it states itself: the twisted element, and order shown only in the frozen-H reduction ([toy models of broken reciprocity](/wiki/symmetry-breaking/toy-models); [acceptance criterion 1](/wiki/symmetry-breaking/toy-models/acceptance-criterion)). Its abstract: "The idea has been stated before, but we found no explicit model of ρ itself being spontaneously broken."

## Is there an earlier explicit model?

The worklog's search found none: "**no existing action has Born reciprocity exactly symmetric and spontaneously broken with η or K as order parameter.** Zero phrase hits on INSPIRE full text and arXiv abstracts. INSPIRE's coverage is incomplete, so this is evidence of absence, not proof." (worklog, "Chunk 1 results").

The round-4 referee repeated the search independently. Full-text searches for "Langmann-Szabo duality" with "spontaneous" (6 hits) and for "Born reciprocity" with "spontaneously broken" (14 hits) turned up no prior explicit model in which vacua spontaneously break the [Langmann–Szabo duality](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/noncommutative-field-theory) (audit notes, Step 1). Its conceptual audit adds that no prior model "with eta=omega K as a dynamical order parameter" turned up either (Step 3).

The nearest case in the literature is Smolin's arXiv:2007.05957, an explicit model in which a larger symmetry, a triality, is spontaneously broken; the referee said it "partially undercuts" the claim of no explicit model. The adjudication ruled that it does not contradict it: "Smolin breaks a triality *down to* Born duality, leaving it unbroken, so it does not contradict 'no model breaks ρ itself'. It still has to be cited." (round-4 adjudication, "Rulings"). The toy note's v2 cites it.

## Neighbours in the literature

Work near the idea, as the toy note and the worklog list it:

- **A selection rule, stated in words.** Freidel, Rudolph and Svoboda (arXiv:1706.07089) suggest the choice "might be subject to a dynamical selection rule" (toy-model note §1). The referee notes that the subject of their sentence is "the kinematical structure of spacetime itself", not literally the choice, and calls the paraphrase acceptable (audit notes, Step 1, ref. [2]).
- **Polarization by gauging.** "Born sigma models choose the polarization by gauging [3]" (toy-model note §1): Marotta and Szabo, arXiv:1910.09997, where the polarization is part of the target structure rather than a field (audit notes, Step 1).
- **Broken O(D, D).** Angus, Kim and Park (arXiv:2111.07947) break the doubled symmetry of double field theory spontaneously, but "there H is the order parameter, with η fixed" (worklog, "Chunk 1 results").
- **A contraction.** Govaerts, Jarvis, Morgan and Low (arXiv:0706.3736): "contraction, not breaking" (worklog).
- **Claims in words only.** Bernardo, Brandenberger and Franzmann (arXiv:1901.01209), whose support is "a personal communication"; the worklog finds that a mechanism picking one section over its partner is open in the literature (chunk 4, "S5 literature").

## How the credit entered the program

The program reached Freidel, Leigh and Minic twice, and the same way each time: a statement it had presented as its own was found in their papers.

1. **The idea uncredited.** The v1 paper presents the move without credit: "promote ρ to an exact, spontaneously broken symmetry" (#9 §1). The popular article #10 describes Born's question as having "spent eighty-eight years in a drawer" (opening); it predates both credits below.
2. **The compatibility theorem (round 3, 2026-10-19).** The round-3 referee found the compatibility statement in the metastring paper and listed it under "Uncited claims / prior art that should be cited" (audit notes, Step 1). The adjudication kept the theorem only as literature, pending a comparison with Freidel, Leigh and Minic ("What survives v3"), and made checking that prior art part of the cleanup before the toy Lagrangian (decision 4). #11 v2.1 re-tagged the theorem [T][V] and credited them (§5).
3. **The lesson as a rule.** The toy-model worklog made a prior-art search its first success criterion, S0 ([success criteria S0–S5](/wiki/symmetry-breaking/toy-models/success-criteria)), citing that episode: "(Lesson of the compatibility theorem, which turned out to be Freidel–Leigh–Minic's.)" (worklog, "Success criteria").
4. **Broken Born duality (v2.2, 2026-10-20).** The S0 search found the quotation, and the worklog recorded: "**#11 §3 must cite FLM for the idea.** What is the program's own: the order-parameter (spontaneous) formulation and its consequences." (chunk 4; FLM is Freidel–Leigh–Minic). #11 v2.2 added the attribution to §3.

## References

- #11 [26][S] L. Freidel, R. G. Leigh, D. Minic, "Metastring theory and modular space-time," JHEP 06 (2015) 006, arXiv:1502.08005 — the toy note's [1c].
- #11 [3]† L. Freidel, R. G. Leigh, D. Minic, "Born reciprocity in string theory and the nature of spacetime," Phys. Lett. B 730, 302 (2014); "Quantum gravity, dynamical phase space and string theory," Int. J. Mod. Phys. D 23, 1442006 (2014). The toy note lists the same two papers as [1a] (arXiv:1307.7080) and [1b] (arXiv:1405.3949), and the round-4 referee retrieved both and confirmed the statements attributed to them (audit notes, Step 1). #11 still marks [3] †.
- Toy-model note [2] (Freidel–Rudolph–Svoboda), [3] (Marotta–Szabo) and [4] (Smolin), all retrieved.

## Used by

- [The hard core: spontaneously broken Born reciprocity](/wiki/program/hard-core) — the spontaneous reading is the program's addition to this precedent.
- [Mandatory breaking: the uncertainty argument](/wiki/symmetry-breaking/mandatory-breaking) — #11 §3 credits the preferred-polarization idea here.
- [P2′: only the symplectic form is rigid](/wiki/program/postulates/p2-prime) — η dynamical, as in metastring theory.
- [P5: the vacuum selects a polarization](/wiki/program/postulates/p5-spontaneous-selection) — the preferred-polarization idea is credited here.
- [The order parameter: J, η and K](/wiki/symmetry-breaking/order-parameter) — η as the order parameter, the program's own step.
- [The compatibility theorem](/wiki/phase-space/born-geometry/compatibility-theorem) — the same authors' statement, credited since #11 v2.1.
- [Acceptance criterion 1: the toy Lagrangian](/wiki/symmetry-breaking/toy-models/acceptance-criterion) — the explicit model the literature lacked.

## Sources

- `papers/broken-born-checkpoint-v2.md` §3 and ref. [26] — the quotation, the attribution, and what the program adds.
- `papers/broken-born-checkpoint-v2.md` §4, §5 and ref. [3] — P2′ on metastring theory; the compatibility statement and its attribution; Born geometry.
- `papers/reciprocity-toy-models.md` Abstract, §1 and ref. [1] — prior work: the idea, the selection rule, Born sigma models, Smolin; "no explicit model".
- `review/round3-adjudication.md` "What survives v3", "Decisions" — the theorem kept as literature pending the comparison; the cleanup in decision 4.
- `review/round4-adjudication.md` "Rulings" — Smolin does not contradict "no model breaks ρ itself"; the section "pair" holds only for d = 1.
- `review/round3/referee/audit-notes.md` Step 1 — the compatibility statement and "Born geometries" found in the metastring paper.
- `review/round4/referee/audit-notes.md` Step 1, Step 3 — the quotation verbatim; refs [1a]–[2] checked; the independent search for an earlier model.
- `notes/toy-lagrangian.md` "Success criteria", "Chunk 1 results", chunk 4 — S0 and its reason; the live-searched prior-art survey and the priority verdict; the section-selection literature and the instruction to credit the idea.
- `notes/broken-born-program-v1.md` §1 — the program's move, uncredited (v1).
- `popsci/angle-of-the-mirror.md` opening — "eighty-eight years in a drawer" (popular article; never a status source).
