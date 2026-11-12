---
title: "The collaboration: roles, attribution and conventions"
weight: 20
status: method
description: "The two parties, Paul (conjecture, direction, veto) and Claude (derivations, counterexamples, verification, drafting): the attribution line, the calibration Paul relies on, how decisions are taken, the working pattern, the prose register and where the work happened."
sources:
  - "CLAUDE.md 'Working with Paul'"
  - "CLAUDE.md 'Method (HANDOFF §5)'"
  - "CLAUDE.md preamble"
  - "HANDOFF.md §1"
  - "HANDOFF.md §7"
  - "HANDOFF.md §6"
  - "HANDOFF.md preamble"
  - "wiki/papers/broken-born-checkpoint-v2.md footer"
  - "wiki/papers/broken-born-checkpoint-v2.md §2"
  - "wiki/papers/broken-born-checkpoint-v2.md Appendix A"
  - "wiki/papers/broken-born-checkpoint-v2.md §12"
  - "notes/broken-born-program-v1.md §11"
  - "review/round3-adjudication.md 'Decisions'"
  - "review/round3-preregistration.md"
  - "review/round5-preregistration.md"
  - "review/round5-adjudication.md 'Pre-registration scored'"
  - "wiki/papers/phase-space-diameter.md provenance note"
  - "review/v3-worklog.md 'Findings neither referee raised', 'New open items', 'Next chunks'"
  - "notes/toy-lagrangian.md 'Next (Claude's call, under Paul's delegation)'"
  - "review/wiki-build-flags.md preamble"
  - "review/wiki-build-flags.md items 55, 60, 63"
  - "wiki/papers/broken-born-checkpoint-v2.md §11.4"
---

*The Comatter program is the work of two parties: Paul (P.R.), an independent developer, and Claude, an AI model made by Anthropic. Paul supplies conjectures and direction and holds a veto; Claude supplies derivations, counterexamples, verification and drafting, and the papers carry an attribution line that records this split. Paul cannot independently verify most of the technical physics, so the provenance tags, the machine checks and the review forecasts written down in advance are his means of telling sound results from confabulation. The same conventions fix how decisions are taken and delegated, how work is divided into chunks that a new session can resume, and how the science is written.*

**Status:** Method, in force — untagged — root [`CLAUDE.md`](../../CLAUDE.md) ('Working with Paul', 'Method'); [`HANDOFF.md` §1](../../HANDOFF.md#1-what-this-project-is) and [§7](../../HANDOFF.md#7-working-conventions-and-user-preferences).

## The two roles

The root [`CLAUDE.md`](../../CLAUDE.md) states the division: "Paul — conjecture, direction, veto. Claude — derivations, counterexamples, drafting, verification." [`HANDOFF.md` §1](../../HANDOFF.md#1-what-this-project-is) gives the same list and adds: "Attribution in all papers follows this split." [Checkpoint #11](../history/documents/checkpoint.md) describes itself as "produced in dialogue between a human (intuition, direction, veto power) and an AI (derivation, counterexamples, drafting)" ([§2](../papers/broken-born-checkpoint-v2.md#2-methodological-preface-provenance-and-verification)).

**Conjecture and direction.** The program began from Paul's suppositions, and [#11](../papers/broken-born-checkpoint-v2.md) keeps them on record with where each stands: [Appendix A](../papers/broken-born-checkpoint-v2.md#appendix-a-audit-of-founding-suppositions-pr-with-fates), "Audit of founding suppositions (P.R., with fates)", lists eleven, from "Symmetrize QM around conjugate variables" (QM being quantum mechanics), now the [hard core](../program/hard-core.md), to "Matter clumps in momentum space", his open conjecture [O], with the evidence against it stated in the item ([Founding suppositions and their fates](../program/founding-suppositions.md); [Conjecture: velocity clumping, the founding image](../dark-matter/momentum-clumping/founding-image.md)). One entry quotes him directly: [monopoles in the conjugate space](../electric-magnetic-duality/conjugate-monopoles.md), as ontology, are "alive and consequence-bearing (P.R.'s 'true-but-irrelevant is measure zero')", with his conjecture that such monopoles are abundant in momentum space ([Appendix A item 5](../papers/broken-born-checkpoint-v2.md#appendix-a-audit-of-founding-suppositions-pr-with-fates)). [Appendix A](../papers/broken-born-checkpoint-v2.md#appendix-a-audit-of-founding-suppositions-pr-with-fates) calls item 4, "Dark matter is conjugate matter", "P.R.'s core conjecture", and records the explanation half of item 5, [the monopole explanation of the null result](../electric-magnetic-duality/monopole-explanation.md), and item 9, [conjugate collapse powering our expansion](../cosmology/scale-factor-duality/collapse-powered-expansion.md), as his open conjectures [O]. His [magnetic-mirror conjecture](../electric-magnetic-duality/magnetic-identification.md) [O], that each electrically charged x-polarized particle has a magnetically charged p-polarized analog, joins items 5 and 11 ([#11 §11.4](../papers/broken-born-checkpoint-v2.md#114-the-magnetic-mirror-conjecture-o-pr-v23)); [#14](../../notes/knot-dark-matter-standalone.md) v2 stated a related identification, the momentum-polarized sector as the S-dual image of the electric sector. The worklog of #14's revision also records a problem he raised: "fix [#13](../papers/conjugate-special-relativity.md)'s two cones and settle which construction governs (raised by Paul, 2026-10-19)" ([Open: the two dual cones](../conjugate-relativity/two-cones-inconsistency.md)).

**Derivations, counterexamples, verification and drafting.** Claude does the calculations, writes the documents and the `verify/` scripts, and adjudicates the [blind reviews](review/_index.md); the adjudications are written in Claude's first person ("My arbitration", "I agree", [`review/round3-adjudication.md`](../../review/round3-adjudication.md)). The referees of rounds 3 to 5 were fresh subagents of the same model family as the author, a limitation the pre-registrations state: "It does not remove correlated blind spots" ([`review/round3-preregistration.md`](../../review/round3-preregistration.md); [the blind-review protocol](review/review-protocol.md)).

## The attribution line

The root [`CLAUDE.md`](../../CLAUDE.md) and [`HANDOFF.md` §7](../../HANDOFF.md#7-working-conventions-and-user-preferences) give the line papers carry: "conjecture and direction, P.R.; derivations, counterexamples, verification, drafting, Claude (Anthropic)." The documents carry three other wordings:

- #11's footer: "Provenance: conjecture and direction, P. R.; derivations, counterexamples, verification battery, and drafting, Claude (Anthropic)."
- The [phase-space-diameter note](../cosmology/scale-factor-duality/phase-space-diameter.md)'s closing line: "Provenance: conjecture and direction, P. R.; derivations, counterexamples, verification and drafting, Claude (Anthropic)."
- The v1 paper's provenance note, which names no verification role: "conjecture and direction by P. R.; derivations, counterexamples, and drafting by Claude (Anthropic)" ([#9 §11](../../notes/broken-born-program-v1.md#11-assessment)). The verification battery entered with #11 ([The verification battery T1–T7](verification/battery.md)).

Among the current documents, #11 and the phase-space-diameter note carry the line. #13 ([conjugate special relativity](../conjugate-relativity/_index.md)) has none, and the [toy-model note](../symmetry-breaking/toy-models/_index.md) is an "Anonymous working manuscript submitted for adversarial review", without names by design ([the blind-review protocol](review/review-protocol.md)).

## Paul

"Paul is an independent developer (Stanford Ginzton Lab background in scanning acoustic microscopy, which is where the Fourier-domain intuition comes from)." (root [`CLAUDE.md`](../../CLAUDE.md)). The Fourier-domain intuition is the source of the analogy the program prefers: position and momentum relate as a waveform and its spectrum, and the Fourier transform implements the [Born rotation ρ](../phase-space/reciprocity/born-reciprocity.md) exactly ([the Fourier transform](../phase-space/reciprocity/fourier-transform.md)).

## The calibration

"Paul cannot independently verify most of the technical physics and relies on the tags, the machine checks and pre-registration to tell sound results from confabulation." (root [`CLAUDE.md`](../../CLAUDE.md)). [`HANDOFF.md` §7](../../HANDOFF.md#7-working-conventions-and-user-preferences) lists what that asks of the work: the tier tags, machine verification, pre-registration and prominent reporting of negative results. [#11 §2](../papers/broken-born-checkpoint-v2.md#2-methodological-preface-provenance-and-verification) names the risk: "AI-generated physics has a known failure mode — fluent confabulation".

Each element of the calibration has its page and its record:

- **Tags.** Every claim says where it came from ([provenance tags](provenance-tags.md)), and #11 ranks its claims in [tiers](claim-tiers.md), with a stated prior of ~50–80% per claim for its new structural physics ([#11 §2](../papers/broken-born-checkpoint-v2.md#2-methodological-preface-provenance-and-verification)).
- **Machine checks.** Asserted numbers are computed by scripts in `verify/`, which [the gate](verification/the-gate.md) runs before any work counts as finished ([the iron rule](verification/iron-rule.md)).
- **Pre-registration.** Before each blind review the expected verdict is written down and fixed in advance, by a commit or by a recorded hash. The record across five rounds: "Verdicts: 2/2 (rounds 1–2), miss (round 3), hit (round 4), hit (round 5)." ([`review/round5-adjudication.md`](../../review/round5-adjudication.md); [pre-registration](review/pre-registration.md)).
- **Negative results.** A failed calculation or a contrary datum is stated in full where the claim is discussed, and a dead claim gets an obituary of its own ([negative results and dead claims](negative-results.md); [claims under review](../status/under-review.md)).

## Decisions and the veto

P.R. decides, may delegate a decision to Claude, and keeps a veto. The worklog of the revision of [the soliton manuscript #14](../dark-matter/candidates/soliton-candidate/_index.md) records two of his decisions: [moving the monopole benchmark](../dark-matter/candidates/soliton-candidate/overproduction.md#superseded-the-point-not-a-window-of-the-v3-worklog) to M ≈ 3×10¹³ GeV, and adopting [a reading of which coupling sets the soliton mass](../dark-matter/candidates/soliton-candidate/alpha-d-coupling.md#superseded-f2-which-coupling-sets-the-soliton-mass), in which [S-duality](../electric-magnetic-duality/s-duality.md) does not fix the dual coupling α_d ([`review/v3-worklog.md`](../../review/v3-worklog.md), items F1 and F2). The second decision is withdrawn; F2's finding, that #14 v2 used both a weak and a strong value of the dual coupling, stands (flag 60 in [`review/wiki-build-flags.md`](../../review/wiki-build-flags.md)). The decisions after review round 3 were delegated, and Claude made them ([Round-3 decisions and lessons](review/round-3/decisions.md)). [Decision 2](review/round-3/decisions.md#decision-2-14s-model-retired) covers #14's model, which used ordinary kinematics; the candidate it modeled, conjugate monopoles localized in momentum, has not been tested and is P.R.'s open conjecture ([#11 §12](../papers/broken-born-checkpoint-v2.md#12-the-dark-sector-question-three-candidates)). #11's footer records the v2.1 amendments as "decisions delegated by P. R. to Claude", and the toy-model worklog marks its route choices the same way, "Route decision for S4–S5 (Claude, under Paul's delegation)" and "Next (Claude's call, under Paul's delegation)" ([`notes/toy-lagrangian.md`](../../notes/toy-lagrangian.md)). Suspected errors in the source documents are quoted as written, not corrected, and flagged for a ruling ([`review/wiki-build-flags.md`](../../review/wiki-build-flags.md); [pending rulings](../status/open-problems.md#pending-rulings)); flags pending include flag 55, on the tag of the dark-matter gate, and flag 63: #11's prediction rows 7 and 11 name two dark-sector candidates where [§12](../papers/broken-born-checkpoint-v2.md#12-the-dark-sector-question-three-candidates) counts three. A claim is recorded as dead only when theory and data kill it and P.R. agrees.

## Working pattern

Work proceeds in chunks, with state saved after each one, so that a new session can resume cold (root [`CLAUDE.md`](../../CLAUDE.md); [`HANDOFF.md` §7](../../HANDOFF.md#7-working-conventions-and-user-preferences)). The worklogs follow it; each opens with "State is saved here after each chunk so any session can resume cold" ([`review/v3-worklog.md`](../../review/v3-worklog.md); [`notes/toy-lagrangian.md`](../../notes/toy-lagrangian.md)), and the wiki's build kept a build-state section in [`wiki/CLAUDE.md`](../CLAUDE.md) for the same purpose until the build was complete ([timeline](../history/timeline.md)).

## The prose register

The science is written as a serious scientist explains abstract material in plain language, without anthropomorphizing, moralizing or detective-story reveals; wave and Fourier analogies are used, ball-rolling and ledger metaphors are not, and every section of a paper opens with an italic plain-language passage, then the tagged technical record (root [`CLAUDE.md`](../../CLAUDE.md); [`HANDOFF.md` §7](../../HANDOFF.md#7-working-conventions-and-user-preferences)). Some of #11's own passages predate the rule or break it ("everything else in physics plays favorites" in [§1](../papers/broken-born-checkpoint-v2.md#1-two-abstracts)), and the wiki quotes such phrases only as history ([`wiki/CLAUDE.md`](../CLAUDE.md), 'Voice').

## Where the work happened

The program "was developed with Claude on claude.ai in September–October 2026 and continues here" (root [`CLAUDE.md`](../../CLAUDE.md)). On claude.ai the review rounds 1 and 2 ran through [the skeptic review console](review/skeptic-console.md), and a running record was kept in the claude.ai memory store, which the handoff says "corroborates but adds nothing critical beyond this document" ([`HANDOFF.md`](../../HANDOFF.md), preamble). The move to Claude Code on 2026-10-19 was made for code execution: the referees of rounds 1–2 had been "unreliable on unaided arithmetic", and "Claude Code's native execution removes this failure mode — that's the main reason the project is moving to you" ([`HANDOFF.md` §6](../../HANDOFF.md#6-review-history-and-the-measured-failure-mode); [the measured referee failure mode](review/referee-failure-mode.md)). The transfer document is described on [The handoff document](../history/documents/handoff.md), the standing instructions on [CLAUDE.md and the README](../history/documents/project-instructions.md), and the dates on [the timeline](../history/timeline.md).

## Sources

- Root [`CLAUDE.md`](../../CLAUDE.md) 'Working with Paul' — roles, attribution line, Paul's background, calibration, working pattern, prose register; 'Method ([HANDOFF §5](../../HANDOFF.md#5-verification-protocol-the-method--keep-using-it))' — when a claim is recorded as dead; preamble — where the work was done
- [`HANDOFF.md` §1](../../HANDOFF.md#1-what-this-project-is), [§7](../../HANDOFF.md#7-working-conventions-and-user-preferences) — participants, the calibration, the working pattern and the prose register; [§6](../../HANDOFF.md#6-review-history-and-the-measured-failure-mode) — why the project moved to Claude Code; preamble — the claude.ai memory store
- [`wiki/papers/broken-born-checkpoint-v2.md` §2](../papers/broken-born-checkpoint-v2.md#2-methodological-preface-provenance-and-verification), [Appendix A](../papers/broken-born-checkpoint-v2.md#appendix-a-audit-of-founding-suppositions-pr-with-fates) and footer — the dialogue, the founding suppositions credited to P.R. with items 3, 4, 5 and 9, the provenance line, the delegated v2.1 decisions; [§12](../papers/broken-born-checkpoint-v2.md#12-the-dark-sector-question-three-candidates) — the candidate #14 modeled, untested and P.R.'s open conjecture
- [`notes/broken-born-program-v1.md` §11](../../notes/broken-born-program-v1.md#11-assessment) — the v1 provenance note
- [`review/round3-adjudication.md`](../../review/round3-adjudication.md) 'Decisions' — the delegation and the veto, and Decision 2's scope
- [`review/round3-preregistration.md`](../../review/round3-preregistration.md), [`review/round5-preregistration.md`](../../review/round5-preregistration.md) — the same-model-family limitation
- [`review/round5-adjudication.md`](../../review/round5-adjudication.md) 'Pre-registration scored' — the verdict record across five rounds
- [`wiki/papers/phase-space-diameter.md`](../papers/phase-space-diameter.md) provenance note — its wording of the attribution line
- [`review/v3-worklog.md`](../../review/v3-worklog.md) 'Findings neither referee raised' (F1, F2), 'New open items', 'Next chunks' — the decisions on F1 and F2, the finding that stands, and the problem Paul raised
- [`wiki/papers/broken-born-checkpoint-v2.md` §11.4](../papers/broken-born-checkpoint-v2.md#114-the-magnetic-mirror-conjecture-o-pr-v23) — P.R.'s magnetic-mirror conjecture [O], #14 v2's related identification and F2's finding
- [`notes/toy-lagrangian.md`](../../notes/toy-lagrangian.md) — route decisions under delegation
- [`review/wiki-build-flags.md`](../../review/wiki-build-flags.md) preamble — suspected errors quoted as written and flagged for a ruling; item 55 — the tag of the dark-matter gate; item 60 — F2's finding; item 63 — rows 7 and 11
