---
title: "The collaboration: roles, attribution and conventions"
weight: 20
status: method
description: "Paul (conjecture, direction, veto) and Claude (derivations, counterexamples, verification, drafting), the attribution line, the calibration Paul relies on, the working pattern, and the prose register with its analogy rules."
sources:
  - "CLAUDE.md 'Working with Paul'"
  - "CLAUDE.md preamble"
  - "HANDOFF.md §1"
  - "HANDOFF.md §7"
  - "HANDOFF.md §6"
  - "papers/broken-born-checkpoint-v2.md footer"
  - "papers/broken-born-checkpoint-v2.md §2"
  - "notes/broken-born-program-v1.md §11"
  - "review/round3-adjudication.md 'Decisions'"
---

*The Broken-Born program is the work of two parties: Paul (P.R.), an independent developer, and Claude, an AI model made by Anthropic. Paul supplies conjectures and direction and holds a veto; Claude supplies derivations, counterexamples, verification and drafting, and the papers carry an attribution line that records this split. Paul cannot independently verify most of the technical physics, so the provenance tags, the machine checks and the review predictions written down in advance are his means of telling sound results from confabulation. The same conventions fix how work is divided into resumable chunks and how the science is written.*

**Status:** Method, in force — untagged — root `CLAUDE.md` ('Working with Paul'); `HANDOFF.md` §1 and §7.

## Key facts

- **Roles.** "Paul — conjecture, direction, veto. Claude — derivations, counterexamples, drafting, verification." (root `CLAUDE.md`). `HANDOFF.md` §1: "Attribution in all papers follows this split." Checkpoint #11 describes itself as "produced in dialogue between a human (intuition, direction, veto power) and an AI (derivation, counterexamples, drafting)" (§2).
- **The attribution line.** "conjecture and direction, P.R.; derivations, counterexamples, verification, drafting, Claude (Anthropic)." (root `CLAUDE.md`; `HANDOFF.md` §7). #11's footer reads "Provenance: conjecture and direction, P. R.; derivations, counterexamples, verification battery, and drafting, Claude (Anthropic)." The v1 paper's note names no verification role: "conjecture and direction by P. R.; derivations, counterexamples, and drafting by Claude (Anthropic)" (#9 §11).
- **Paul.** "Paul is an independent developer (Stanford Ginzton Lab background in scanning acoustic microscopy, which is where the Fourier-domain intuition comes from). Never describe Paul as retired." (root `CLAUDE.md`). `HANDOFF.md` §7 records that he corrected this explicitly.
- **The calibration.** "Paul cannot independently verify most of the technical physics and relies on the tags, the machine checks and pre-registration to tell sound results from confabulation. Keep that calibration explicit." (root `CLAUDE.md`). `HANDOFF.md` §7: he "has asked for explicit legit-vs-hallucination calibration: keep the tier tags, keep machine-verifying, keep pre-registering, keep reporting negative results prominently. Honest obituaries are part of the deliverable." Each element has its page: [provenance tags](/wiki/method/provenance-tags), [claim tiers](/wiki/method/claim-tiers), [verification](/wiki/method/verification), [pre-registration](/wiki/method/review/pre-registration) and [negative results](/wiki/method/negative-results).
- **Delegated decisions.** After review round 3: "Paul delegated these on 2026-10-19 ("You make the decisions for me and give rational"). Claude made them. Paul keeps the veto." (`review/round3-adjudication.md`, 'Decisions'; see [Round-3 decisions and lessons](/wiki/method/review/round-3/decisions)). #11's footer records its v2.1 amendments as "decisions delegated by P. R. to Claude".
- **Working pattern.** "Work in chunks and save state after each one, so a cold session can resume. Paul continues with "go"." "Working communication: simple bullets. Make the call and recommend; don't ask questions Paul can't answer." (root `CLAUDE.md`).
- **Prose register.** "Science prose: a serious scientist explaining abstract material in plain language. No anthropomorphizing, no moralizing, no detective-story reveals. Wave/Fourier analogies work; ball-rolling and ledger/bookkeeping metaphors don't." "Papers: every section opens with an italic plain-language passage, then the tagged technical record." (root `CLAUDE.md`). `HANDOFF.md` §7 gives the reason: Paul reads such phrasing, its example being "nature plays favorites", as "glib AI". Some of #11's own passages break the register ("plays favorites" in §1; "one event, two ledgers" in Appendix A); the wiki quotes such phrases only as history and writes "two descriptions" instead (`wiki/CLAUDE.md`, 'Voice').
- **Where the work happened.** The program "was developed with Claude on claude.ai in September–October 2026 and continues here" (root `CLAUDE.md`). The move to Claude Code was made for code execution: "Claude Code's native execution removes this failure mode — that's the main reason the project is moving to you" (`HANDOFF.md` §6), the failure mode being the referees' unaided arithmetic ([the iron rule](/wiki/method/verification/iron-rule)). The transfer document is described on [The handoff document](/wiki/history/documents/handoff), and the dates are on [the timeline](/wiki/history/timeline).

## Sources

- Root `CLAUDE.md` 'Working with Paul' — roles, attribution line, calibration, working pattern, prose register; preamble — where the work was done
- `HANDOFF.md` §1, §7 — participants, Paul's background and his explicit correction of how he is described, the calibration request, the register and its reasons
- `HANDOFF.md` §6 — why the project moved to Claude Code
- `papers/broken-born-checkpoint-v2.md` §2 and footer — the dialogue described in #11, its provenance line, the delegated v2.1 decisions
- `notes/broken-born-program-v1.md` §11 — the v1 provenance note
- `review/round3-adjudication.md` 'Decisions' — the delegation of the round-3 decisions and Paul's veto
