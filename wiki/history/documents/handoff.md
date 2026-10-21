---
title: "The handoff document"
weight: 20
status: record
description: "HANDOFF.md, the transfer from claude.ai on 2026-10-19: its one-screen state, artifact inventory, chat-only results and queue, and which parts are superseded."
sources:
  - "HANDOFF.md"
  - "CLAUDE.md 'Since the handoff'"
  - "CLAUDE.md 'Layout'"
  - "wiki/CLAUDE.md 'The wiki is derivative'"
  - "papers/broken-born-checkpoint-v2.md §10"
  - "papers/broken-born-checkpoint-v2.md §12"
  - "review/round3-adjudication.md 'Pre-registration scored'"
  - "review/round3-adjudication.md 'Decisions'"
  - "review/round4-adjudication.md 'Pre-registration scored'"
---

*`HANDOFF.md` is the note that carried the program from the claude.ai conversation where it was developed to Claude Code and this repository. It was prepared on 2026-10-19 so that a fresh session could continue without the original chat: it gives the scientific state on one screen, numbers the artifacts #1–#15, lists the results that exist only in the chat, and records the method, the review history, the working conventions and a ranked list of next actions. Much of it still stands, but its soliton dark-matter candidate and its work queue were superseded on 2026-10-19 and 2026-10-20, and the root `CLAUDE.md` now ranks above it.*

**Status:** Record, superseded in part — untagged (it marks machine-checked results with ✓ rather than [V]) — rank 5 in the wiki's precedence order, with its §2 soliton candidate and §8 queue superseded (`wiki/CLAUDE.md`; root `CLAUDE.md` "Since the handoff"). The file is unchanged since the import of 2026-10-19 (8d588f6).

## Key facts

- **Purpose and date.** "Everything a fresh Claude Code session needs to continue this project. Read this first; the artifacts listed in §3 travel with it. It is self-sufficient — nothing essential lives only in the originating chat session or in claude.ai memory." The footer: "Handoff prepared 2026-10-19 from the originating claude.ai session."
- **Contents.** §1 what the project is; §2 the scientific state on one screen (alive, dead, open, and the external clock); §3 the artifact inventory in creation order; §4 the results that exist only in the chat; §5 the verification protocol; §6 the review history and the referees' measured failure mode; §7 working conventions; §8 the ranked queue; §9 a suggested repository layout; Appendix A the code of the seven-test battery, now `verify/battery.py` ([the battery](/wiki/method/verification/battery)). Its Appendix A is the battery; #11's Appendix A is the [audit of founding suppositions](/wiki/program/founding-suppositions).
- **What still stands.** The §2 list "Dead (killed by own calculations — keep dead)": dark matter clumping in momentum space as dynamics, "Conjugate collapse powers our expansion", conjugate monopoles as the explanation of our monopole non-detection, and α_d ≈ 34 via Dirac quantization against our photon ([the graveyard](/wiki/status/graveyard)). The root `CLAUDE.md` repeats the rule: "Claims listed as dead in HANDOFF §2 stay dead." Also standing: the §4 chat-only results, at conjecture tier ([chat-only and popsci-only conjectures](/wiki/status/conjectures)); the §5 method, carried into the root `CLAUDE.md` as "Method (HANDOFF §5)"; and the §7 conventions ([the collaboration](/wiki/method/collaboration)).
- **What is superseded: the soliton candidate and the queue.** §2 names as the "Current best" dark-matter candidate "superheavy (~10¹³–10¹⁷ GeV) topological solitons (π₂ monopole-class) of a separate, strongly coupled dual gauge sector"; that candidate has been dead since 2026-10-19 ([the obituary](/wiki/dark-matter/candidates/soliton-candidate/obituary)). The §8 queue served it in items 1–3. Items 1 and 2, cutting v3 and re-running the blind audit, were done on 2026-10-19; item 3, the √N-floor estimate, was dropped; item 4, the toy Lagrangian, is "done to the referees' wording"; and items 5–7 are the current queue (root `CLAUDE.md`; [Open problems and the queue](/wiki/status/open-problems)).
- **What is superseded: statuses and readings.** §2's "Consistent with DESI DR1/DR2 drift hints" (Data Release 1 and Data Release 2 of the Dark Energy Spectroscopic Instrument) is replaced by Data Release 2's phantom crossing above z ≈ 0.4, which puts the dark-energy sector "under real pressure" (root `CLAUDE.md`; [DESI DR2's phantom crossing](/wiki/cosmology/dark-energy/desi-dr2-phantom-crossing)). §3 lists #11 as "v2.0 — CURRENT REFERENCE" (it is v2.2) and #14 as "v2 — CURRENT blind-review manuscript" (it went to v3 and was withdrawn). §6 calls round 3 "incomplete", but it was completed on 2026-10-19 with verdict C ([review round 3](/wiki/method/review/round-3)). §5's pre-registration record, "scored 2-for-2 on verdicts", became a miss in round 3 and a hit in round 4 ([pre-registration](/wiki/method/review/pre-registration)). Its read order, "#11 → #14 → §6 of this handoff → calc notes", is replaced by the root `CLAUDE.md`'s ([CLAUDE.md and the README](/wiki/history/documents/project-instructions)).
- **The referees' failure mode** (§6). In rounds 1–2, "fresh LLM referees are strong on structure, literature and logic; unreliable on unaided arithmetic" (LLM: large language model), "Hence the iron rule", and the execution tools of Claude Code were "the main reason the project is moving to you". Round 3 moved the failure mode: "the author's verification checks the author's model" (`review/round3-adjudication.md`). See [the measured referee failure mode](/wiki/method/review/referee-failure-mode) and [rounds 1 and 2](/wiki/method/review/rounds-one-and-two).
- **Not reconciled inside the document.** §1 says "Three blind AI reviews returned verdict B ("flawed but salvageable")", while §6 records two completed rounds, B / medium and B near B/C, and an incomplete third. No document reconciles the count ([Conflicts between sources](/wiki/history/documents/source-conflicts)).

## Sources

- `CLAUDE.md` 'Since the handoff' — which parts of the handoff are dead, dropped or replaced; 'Layout' — the replacement read order
- `wiki/CLAUDE.md` 'The wiki is derivative' — the handoff's rank and its superseded parts
- `papers/broken-born-checkpoint-v2.md` §12 — the soliton obituary; §10 — the DESI reading "Under pressure (v2.1)"
- `review/round3-adjudication.md` 'Pre-registration scored' and 'Decisions' — round 3's completion, the moved failure mode, and the queue decisions; `review/round4-adjudication.md` 'Pre-registration scored' — the round-4 hit
- `HANDOFF.md` §1–§9 and Appendix A — the document itself
