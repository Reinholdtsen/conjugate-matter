---
title: "The collaboration: roles, attribution and conventions"
weight: 20
status: method
description: "Paul (conjecture, direction, veto) and Claude (derivations, counterexamples, verification, drafting), the attribution line, the calibration Paul relies on, decisions and their delegation, the working pattern, and the prose register."
sources:
  - "CLAUDE.md 'Working with Paul'"
  - "CLAUDE.md preamble"
  - "HANDOFF.md §1"
  - "HANDOFF.md §7"
  - "HANDOFF.md §6"
  - "HANDOFF.md §3"
  - "HANDOFF.md preamble"
  - "papers/broken-born-checkpoint-v2.md footer"
  - "papers/broken-born-checkpoint-v2.md §2"
  - "papers/broken-born-checkpoint-v2.md Appendix A"
  - "notes/broken-born-program-v1.md §11"
  - "review/round3-adjudication.md 'Decisions'"
  - "review/round3-preregistration.md"
  - "review/round4-adjudication.md 'Pre-registration scored'"
  - "review/v3-worklog.md 'Findings neither referee raised', 'New open items', 'Next chunks'"
  - "notes/toy-lagrangian.md 'Next (Claude's call, under Paul's delegation)'"
  - "review/wiki-build-flags.md preamble"
---

*The Broken-Born program is the work of two parties: Paul (P.R.), an independent developer, and Claude, an AI model made by Anthropic. Paul supplies conjectures and direction and holds a veto; Claude supplies derivations, counterexamples, verification and drafting, and the papers carry an attribution line that records this split. Paul cannot independently verify most of the technical physics, so the provenance tags, the machine checks and the review forecasts written down in advance are his means of telling sound results from confabulation. The same conventions fix how decisions are taken and delegated, how work is divided into chunks that a new session can resume, and how the science is written.*

**Status:** Method, in force — untagged — root `CLAUDE.md` ('Working with Paul'); `HANDOFF.md` §1 and §7.

## The two roles

The root `CLAUDE.md` states the division: "Paul — conjecture, direction, veto. Claude — derivations, counterexamples, drafting, verification." `HANDOFF.md` §1 gives the same list and adds: "Attribution in all papers follows this split." [Checkpoint #11](/wiki/history/documents/checkpoint) describes itself as "produced in dialogue between a human (intuition, direction, veto power) and an AI (derivation, counterexamples, drafting)" (§2).

**Conjecture and direction.** The program began from Paul's suppositions, and #11 keeps them on record with what became of each: Appendix A, "Audit of founding suppositions (P.R., with fates)", lists eleven, from "Symmetrize QM around conjugate variables" (QM being quantum mechanics), now the [hard core](/wiki/program/hard-core), to "Matter clumps in momentum space", now "dead as dynamics" ([Founding suppositions and their fates](/wiki/program/founding-suppositions); [Obituary: velocity clumping, the founding image](/wiki/dark-matter/momentum-clumping/founding-image)). One fate quotes him directly: [monopoles in the conjugate space](/wiki/electric-magnetic-duality/conjugate-monopoles) survive as ontology, "alive and consequence-bearing (P.R.'s "true-but-irrelevant is measure zero")" (Appendix A item 5).

**Derivations, counterexamples, verification and drafting.** Claude does the calculations, writes the documents and the `verify/` scripts, and adjudicates the [blind reviews](/wiki/method/review); the adjudications are written in Claude's first person ("My arbitration", "I agree", `review/round3-adjudication.md`). The referees of rounds 3 and 4 were fresh subagents of the same model family as the author, a limitation the pre-registrations state: "It does not remove correlated blind spots" (`review/round3-preregistration.md`; [the blind-review protocol](/wiki/method/review/review-protocol)).

## The attribution line

The root `CLAUDE.md` and `HANDOFF.md` §7 give the line papers carry: "conjecture and direction, P.R.; derivations, counterexamples, verification, drafting, Claude (Anthropic)." The documents carry two earlier wordings:

- #11's footer: "Provenance: conjecture and direction, P. R.; derivations, counterexamples, verification battery, and drafting, Claude (Anthropic)."
- The v1 paper's provenance note, which names no verification role: "conjecture and direction by P. R.; derivations, counterexamples, and drafting by Claude (Anthropic)" (#9 §11). The verification battery entered with #11 ([The verification battery T1–T7](/wiki/method/verification/battery)).

Among the current documents, #11 is the one that carries the line. #13 ([conjugate special relativity](/wiki/conjugate-relativity)) has none, and the [toy-model note](/wiki/symmetry-breaking/toy-models) is an "Anonymous working manuscript submitted for adversarial review", without names by design ([the blind-review protocol](/wiki/method/review/review-protocol)).

## Paul

"Paul is an independent developer (Stanford Ginzton Lab background in scanning acoustic microscopy, which is where the Fourier-domain intuition comes from). Never describe Paul as retired." (root `CLAUDE.md`). `HANDOFF.md` §7 records that he corrected this explicitly, and the handoff's inventory carries the same register note for the first [popular article](/wiki/history/documents/popular-articles), #10 (§3). The Fourier-domain intuition is the source of the analogy the program prefers: position and momentum relate as a waveform and its spectrum, and the Fourier transform implements the [Born rotation ρ](/wiki/phase-space/reciprocity/born-reciprocity) exactly ([the Fourier transform](/wiki/phase-space/reciprocity/fourier-transform)).

## The calibration

"Paul cannot independently verify most of the technical physics and relies on the tags, the machine checks and pre-registration to tell sound results from confabulation. Keep that calibration explicit." (root `CLAUDE.md`). `HANDOFF.md` §7 puts his request as "explicit legit-vs-hallucination calibration: keep the tier tags, keep machine-verifying, keep pre-registering, keep reporting negative results prominently. Honest obituaries are part of the deliverable." #11 §2 names the risk: "AI-generated physics has a known failure mode — fluent confabulation".

Each element of the calibration has its page and its record:

- **Tags.** Every claim says where it came from ([provenance tags](/wiki/method/provenance-tags)), and #11 ranks its claims in [tiers](/wiki/method/claim-tiers), with an "honest prior per claim ~50–80%" for its new structural physics (#11 §2).
- **Machine checks.** Asserted numbers are computed by scripts in `verify/`, which [the gate](/wiki/method/verification/the-gate) runs before any work counts as finished ([the iron rule](/wiki/method/verification/iron-rule)).
- **Pre-registration.** Before each blind review the expected verdict is committed in advance. The record across four rounds: "Verdicts: 2/2 (rounds 1–2), miss (round 3), hit (round 4)" (`review/round4-adjudication.md`; [pre-registration](/wiki/method/review/pre-registration)).
- **Negative results.** Failures are reported prominently and stay dead ([negative results and dead claims](/wiki/method/negative-results)).

## Decisions and the veto

The record shows three ways a decision is taken.

- **Paul decides.** During the revision of [the soliton manuscript #14](/wiki/dark-matter/candidates/soliton-candidate) the worklog records "Decided (Paul, 2026-10-19):" twice: [moving the monopole benchmark](/wiki/dark-matter/candidates/soliton-candidate/overproduction#superseded-the-point-not-a-window-of-the-v3-worklog) to M ≈ 3×10¹³ GeV, and adopting [a reading of which coupling sets the soliton mass](/wiki/dark-matter/candidates/soliton-candidate/alpha-d-coupling#superseded-f2-which-coupling-sets-the-soliton-mass) (`review/v3-worklog.md`, items F1 and F2). It also records a problem he raised: "fix #13's two cones and settle which construction governs (raised by Paul, 2026-10-19)" ([Open: the two dual cones](/wiki/conjugate-relativity/two-cones-inconsistency)).
- **Paul delegates.** After review round 3: "Paul delegated these on 2026-10-19 ("You make the decisions for me and give rational"). Claude made them. Paul keeps the veto." (`review/round3-adjudication.md`, 'Decisions'; [Round-3 decisions and lessons](/wiki/method/review/round-3/decisions)). #11's footer records the v2.1 amendments as "decisions delegated by P. R. to Claude". The toy-model worklog marks its route choices the same way, "Route decision for S4–S5 (Claude, under Paul's delegation)" and "Next (Claude's call, under Paul's delegation)" (`notes/toy-lagrangian.md`).
- **Paul rules.** Suspected errors in the source documents found while building this wiki are quoted faithfully, not corrected; "each needs Paul's ruling" (`review/wiki-build-flags.md`).

The working instruction behind the delegation is "Make the call and recommend; don't ask questions Paul can't answer." (root `CLAUDE.md`).

## Working pattern

"Work in chunks and save state after each one, so a cold session can resume. Paul continues with "go"." (root `CLAUDE.md`). `HANDOFF.md` §7 gives the reason: "he may be away — save progress so any session can resume cold." The worklogs follow it; each opens with "State is saved here after each chunk so any session can resume cold" (`review/v3-worklog.md`; `notes/toy-lagrangian.md`), and the wiki keeps a build-state section for the same purpose (`wiki/CLAUDE.md`). Working communication is in "simple bullets" (root `CLAUDE.md`).

## The prose register

"Science prose: a serious scientist explaining abstract material in plain language. No anthropomorphizing, no moralizing, no detective-story reveals. Wave/Fourier analogies work; ball-rolling and ledger/bookkeeping metaphors don't." "Papers: every section opens with an italic plain-language passage, then the tagged technical record." (root `CLAUDE.md`). `HANDOFF.md` §7 gives the reason: Paul reads such phrasing, its example being "nature plays favorites", as "glib AI", and ball-rolling and dual-ledger metaphors "did not land".

Some of #11's own passages predate the rule or break it ("everything else in physics plays favorites" in §1; "one state, two ledgers" in Appendix A). The wiki quotes such phrases only as history and writes "two descriptions" where #11 says "two ledgers" (`wiki/CLAUDE.md`, 'Voice').

## Where the work happened

The program "was developed with Claude on claude.ai in September–October 2026 and continues here" (root `CLAUDE.md`). On claude.ai the review rounds 1 and 2 ran through [the skeptic review console](/wiki/method/review/skeptic-console), and a running record was kept in the claude.ai memory store, which the handoff says "corroborates but adds nothing critical beyond this document" (`HANDOFF.md`, preamble). The move to Claude Code on 2026-10-19 was made for code execution: the referees of rounds 1–2 had been "unreliable on unaided arithmetic", and "Claude Code's native execution removes this failure mode — that's the main reason the project is moving to you" (`HANDOFF.md` §6; [the measured referee failure mode](/wiki/method/review/referee-failure-mode)). The transfer document is described on [The handoff document](/wiki/history/documents/handoff), the standing instructions on [CLAUDE.md and the README](/wiki/history/documents/project-instructions), and the dates on [the timeline](/wiki/history/timeline).

## Sources

- Root `CLAUDE.md` 'Working with Paul' — roles, attribution line, Paul's background, calibration, working pattern, prose register; preamble — where the work was done
- `HANDOFF.md` §1, §7 — participants, the explicit correction of how Paul is described, the calibration request, the register and its reasons; §3 — the register note on #10; §6 — why the project moved to Claude Code; preamble — the claude.ai memory store
- `papers/broken-born-checkpoint-v2.md` §2, Appendix A and footer — the dialogue, the founding suppositions credited to P.R., the provenance line, the delegated v2.1 decisions
- `notes/broken-born-program-v1.md` §11 — the v1 provenance note
- `review/round3-adjudication.md` 'Decisions' — the delegation and the veto
- `review/round3-preregistration.md` — the same-model-family limitation
- `review/round4-adjudication.md` 'Pre-registration scored' — the verdict record across four rounds
- `review/v3-worklog.md` 'Findings neither referee raised' (F1, F2), 'New open items', 'Next chunks' — Paul's decisions of 2026-10-19 and the problem he raised
- `notes/toy-lagrangian.md` — route decisions under delegation
- `review/wiki-build-flags.md` preamble — flags awaiting Paul's ruling
