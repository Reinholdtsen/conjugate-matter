---
title: "Timeline"
weight: 10
status: record
description: "Dated events from 1938 to the pending DESI DR3 release: the claude.ai era, the move to Claude Code, rounds 3 and 4, and the checkpoint's versions."
sources:
  - "CLAUDE.md 'Since the handoff'"
  - "papers/broken-born-checkpoint-v2.md header"
  - "papers/broken-born-checkpoint-v2.md §12"
  - "papers/broken-born-checkpoint-v2.md References"
  - "review/round4-adjudication.md"
  - "review/round3-adjudication.md"
  - "review/round3-preregistration.md"
  - "HANDOFF.md §2"
  - "HANDOFF.md §3"
  - "HANDOFF.md §6"
  - "notes/toy-lagrangian.md"
  - "review/v3-worklog.md"
  - "notes/knot-dark-matter-standalone.md banner"
  - "notes/broken-born-theory.md header"
---

*The timeline lists the program's events in date order, from Max Born's 1938 question to the third data release of the Dark Energy Spectroscopic Instrument (DESI), which the program treats as the decisive test of its dark-energy prediction. Most of the work done on claude.ai in September and October 2026 carries no dates; those events follow the creation order of the artifacts in `HANDOFF.md` §3. From the move to this repository on 2026-10-19 onward, the documents and the commit history date each step: review round 3 and the retirement of the soliton candidate, the toy models and review round 4, and the checkpoint's versions 2.1 and 2.2.*

**Status:** Record, current to 2026-10-20 — untagged — dates come from the documents' own headers and dated entries and from `git log` (commit times are local, −0700). The order of the undated claude.ai events follows `HANDOFF.md` §3; where review rounds 1 and 2 fall in that order is inferred, not recorded.

## Key facts

- **Before the program (the literature).** Max Born, "A suggestion for unifying quantum theory and relativity," Proc. R. Soc. Lond. A 165, 291 (1938) [1†], and "Reciprocity theory of elementary particles," Rev. Mod. Phys. 21, 463 (1949) [2†], are the origin of [Born's question](/wiki/program/borns-question). Among the later works the program builds on or is measured against: Snyder's quantized space-time (1947) [4†] ([curved momentum space](/wiki/phase-space/reciprocity/curved-momentum-space)); the [multi-graviton no-go](/wiki/gravity/spin-2-fields/multi-graviton-no-go) (2001) [8†]; Freidel, Leigh and Minic on Born reciprocity (2014) [3†] and the metastring (2015, arXiv:1502.08005) [26S] ([broken Born duality](/wiki/phase-space/reciprocity/broken-born-duality)); DESI's Data Release 2, DR2 (arXiv:2503.14738, 2025) [21S]; and Liveoak, Maharana and Wells on hidden monopoles (arXiv:2607.20843, 2026) [29S] ([topological dark matter](/wiki/dark-matter/candidates/soliton-candidate/prior-art)). Bracketed numbers are #11's reference list ([References](/wiki/references)).
- **September 2026: the lab notebook.** #1, "Version 0.1, September 2026": postulates P1–P5 with the [original P2](/wiki/program/postulates/original-p2), an action, a predictions table with rows 1–10, open problems 1–6 and "three named debts standing between this document and a paper" ([the lab notebook](/wiki/history/documents/lab-notebook); [the three debts](/wiki/history/debts)).
- **The claude.ai era, undated, in `HANDOFF.md` §3's creation order.** The calc notes #2–#4 close Debt 3 negative (addendum v0.2; [the Debt-3 notes](/wiki/history/documents/debt-3-notes)); #5, an "overnight" note, and #6–#8 settle Debt 1 in structure (addenda v0.3–v0.6; [the Debt-1 notes](/wiki/history/documents/debt-1-notes)). Then #9, the program v1.0; #10, "The Angle of the Mirror"; #11 v2.0 ([the checkpoint](/wiki/history/documents/checkpoint)); #12, "The Universe's Other Half" ([the popular articles](/wiki/history/documents/popular-articles)); #13, [conjugate special relativity](/wiki/conjugate-relativity); #14 v1, the soliton manuscript for blind review; and #15, [the skeptic review console](/wiki/method/review/skeptic-console). Review round 1 (verdict B / medium) and round 2 (B near B/C) ran on #14 v1 and v2 through #15 ([rounds 1 and 2](/wiki/method/review/rounds-one-and-two)). On 2026-10-17 a first attempt at round 3, dispatched from claude.ai, "died partway on a rate limit" (`HANDOFF.md` §6).
- **2026-10-18 and 19: the move to Claude Code.** The repository's initial commit is 6b8f599 (2026-10-18 23:07). [The handoff document](/wiki/history/documents/handoff) was "prepared 2026-10-19 from the originating claude.ai session". The chat's files were imported (8d588f6, 10:28) and restructured into `papers/`, `notes/`, `popsci/`, `review/` and `verify/`, with the battery as the first [gate](/wiki/method/verification/the-gate) (008c3ee, 10:35); #1–#10, #12, #13 and `HANDOFF.md` have not changed since. The v3 worklog began with every number of #14 v2 recomputed (678e48a, 10:41), and #14 v3 was cut (5dbaa82, 14:42).
- **2026-10-19: round 3 and the retirement of the soliton candidate.** Round 3 was pre-registered (cc05705, 14:48) with the predicted verdict in the commit subject, which the auditor's git status showed. A blind subagent with shell, Python and web access audited v3, and the adjudication followed: "v3 fails (verdict C) on the Kibble normalization" (96f58da, 15:47). #14 was withdrawn the same day. The decisions of 17:14 (5b6efaa) made sector separation strict, retired the soliton candidate, dropped the √N floor and set the toy Lagrangian as the next task; #11 became v2.1 at 17:29 (e1c1f67). See [review round 3](/wiki/method/review/round-3) and [the obituary](/wiki/dark-matter/candidates/soliton-candidate/obituary).
- **2026-10-19 and 20: the toy models and round 4.** The toy work fixed its [success criteria](/wiki/symmetry-breaking/toy-models/success-criteria) "before any construction" (d9e61f0, 18:37), ran chunks 1–4 (0e0f51e at 18:40 to bed9306 at 22:16), and was submitted as the toy-model note v1 with the round-4 pre-registration under a neutral commit subject (d9a06ac, 22:26). At 22:29 #11 §3 credited Freidel–Leigh–Minic for "broken Born duality" (6ee74d0). The round-4 adjudication, verdict B, followed on 2026-10-20 at 11:13 (e3ce9eb), and the note v2 and #11 v2.2 at 18:54 (6606734; the revisions marked applied in 5ca7d81). The wiki gate, `scripts/check-wiki.py`, joined `scripts/check.sh` at 23:39 (17e1338). See [toy models](/wiki/symmetry-breaking/toy-models) and [review round 4](/wiki/method/review/round-4).
- **Pending.** The root `CLAUDE.md` queue ([CLAUDE.md and the README](/wiki/history/documents/project-instructions)): the partially-massless comparison, the † literature battery and the phase-space-diameter note, then an optional round-5 review of the toy note, "but only before any external use" ([open problems and the queue](/wiki/status/open-problems)). #11 is "not for submission until the † audit (open item 10) completes" ([the literature battery](/wiki/method/literature-battery)). DESI's Data Release 3, DR3, is "expected late 2026" (`HANDOFF.md` §2): a robust constant w = −1 kills the τ sector, a robust intrinsic w < −1 kills the framework, and continued thawing keeps it alive ([row 4](/wiki/predictions/dark-energy-drift)).

## Sources

- `CLAUDE.md` 'Since the handoff' — the post-handoff decisions and the current queue
- `papers/broken-born-checkpoint-v2.md` header — the v2.1 (2026-10-19) and v2.2 (2026-10-20) changes; §12 — the soliton candidate "retired 2026-10-19"; References — the literature entries and their † and [S] marks
- `review/round4-adjudication.md`, `review/round3-adjudication.md`, `review/round3-preregistration.md` — the review rounds, verdicts, decisions and the commit-subject lesson
- `HANDOFF.md` §3 — the creation order of #1–#15; §6 — rounds 1–2 and the first round-3 attempt of 2026-10-17; §2 — DESI DR3 as the external clock; the footer — the handoff date
- `notes/toy-lagrangian.md` — the dated toy-model chunks (2026-10-19/20)
- `review/v3-worklog.md` — the recomputation of #14 v2 and the cutting of v3 (2026-10-19)
- `notes/knot-dark-matter-standalone.md` banner — "Withdrawn (2026-10-19)"
- `notes/broken-born-theory.md` header — "Version 0.1, September 2026"
- `git log` — commit hashes and times
