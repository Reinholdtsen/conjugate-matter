---
title: "The blind-review protocol and verdict scale"
weight: 10
status: method
description: "Five steps — citations, every number in code, independent re-derivation, conceptual audit, an A/B/C verdict — given to a fresh subagent with only the manuscript; the scale's two glosses and the protocol's limits."
sources:
  - "review/round3-preregistration.md 'Protocol (HANDOFF §6, round 3)'"
  - "review/round4-preregistration.md"
  - "review/round3/referee/audit-notes.md Step 1–Step 5"
  - "review/round4/referee/audit-notes.md Step 1–Step 4"
  - "review/skeptic-review-console.html SYSTEM"
  - "review/round3-adjudication.md"
  - "review/round4-adjudication.md"
  - "HANDOFF.md §6"
---

*The blind-review protocol is the fixed procedure the program uses to test a manuscript: a fresh AI subagent receives a copy of the manuscript and nothing else, then checks every citation against its source, re-runs every number in its own code, re-derives the mathematics independently, audits the argument for consistency and omissions, and returns a grade of A, B or C with the single weakest link named. The grade scale is defined in the referee prompt of the [skeptic review console](/wiki/method/review/skeptic-console), the tool of rounds 1 and 2, and the later rounds kept it. Rounds 3 and 4 ran the five-step form, with a referee that could execute code; the author then rules on each finding, re-running disputed numbers in separate scripts. The protocol's own stated limit is that the referee is the same model family as the author.*

**Status:** Method, in force — untagged — written into the pre-registrations of [round 3](/wiki/method/review/round-3/preregistration) (`review/round3-preregistration.md`) and [round 4](/wiki/method/review/round-4) (`review/round4-preregistration.md`), and used in both rounds.

## Key facts

- **The referee.** In round 3 the auditor is "a fresh subagent with shell, Python (numpy/sympy/scipy) and web search. It gets only a copy of the manuscript and the protocol below, with no repo, worklog or handoff context." Round 4 used "the same five-step protocol as round 3: citations, numbers, an independent re-derivation, a conceptual audit, and a verdict with four lists." In journal peer review, "double-blind" means the referee is not told who wrote the paper [T]; here the referee also has no access to the project. In rounds 1 and 2 the console's prompt also told the referee that the manuscript "may have been generated wholly or partly by an AI".
- **The five steps** (round 3, `review/round3-preregistration.md`):
  1. "Verify every citation against INSPIRE, arXiv or the publisher, including that each one supports what it is cited for."
  2. "Re-check every number in Secs. 2–4 in Python from independently chosen constants."
  3. "Re-derive the compatibility theorem independently, symbolically (sympy) and with random numerical tests." [The compatibility theorem](/wiki/phase-space/born-geometry/compatibility-theorem) is the theorem #14 stated in its §1; in round 4 the re-derivation covered the toy note's own algebra.
  4. "Conceptual audit: internal consistency, omitted constraints (by literature search), and the kinetic-mixing claims."
  5. "Verdict A/B/C with a confidence, four lists (verified / failed / unverifiable / omitted constraints), and the single weakest link."
- **The verdict scale**, from the console's prompt: "(A) coherent speculative physics that uses established results correctly, (B) flawed but containing salvageable ideas, or (C) confabulation." Rounds 3 and 4 gloss B as "flawed but salvageable" and the round-3 referee glossed C as "fundamentally flawed". The two glosses of C differ, and both are on record.
- **How the citations were checked.** Round 3 queried the INSPIRE database for each reference, read arXiv abstracts and grepped the full texts for "the specific claim each reference is cited for" (`review/round3/referee/audit-notes.md` Step 1). Round 4's referee: "Citation and omission indictments rest on retrieved sources (INSPIRE API, arXiv e-print sources), none from memory."
- **Every number in code.** Round 3: "Every one of its 16 numerical findings rests on executed code." Round 4: "All 9 of its numerical and algebraic indictments rest on executed code." This step removes [the measured failure mode](/wiki/method/review/referee-failure-mode) of rounds 1–2, the referees' unaided arithmetic, which is also why the handoff calls [the iron rule](/wiki/method/verification/iron-rule) "load-bearing".
- **Adjudication.** The author arbitrates each finding with separate scripts (`review/round3/adjudicator/`, `review/round4/adjudicator/`) and rules it upheld, accepted without re-checking, accepted, or overturned; see [the round-3 rulings](/wiki/method/review/round-3/rulings) and [the round-3 arbitration](/wiki/method/review/round-3/arbitration). Before dispatch, the expected verdict and weakest link are committed ([pre-registration](/wiki/method/review/pre-registration)).
- **Its limit**, "stated up front" in the round-3 pre-registration: "the auditor is the same model family as the author. It removes the arithmetic failure mode of rounds 1–2, which had no code execution. It does not remove correlated blind spots." Round 4 repeats "same model family as the author".
- **Its origin.** The handoff describes the five steps as the plan for an "execution-verified blind audit agent" dispatched from claude.ai on 2026-10-17, which "died partway on a rate limit" (`HANDOFF.md` §6); the protocol first ran to completion in [round 3](/wiki/method/review/round-3).

## Sources

- `review/round3-preregistration.md` 'Protocol (HANDOFF §6, round 3)' — the five steps, the referee's set-up and the stated limitation
- `review/round4-preregistration.md` — the same protocol reused for the toy-model note
- `review/round3/referee/audit-notes.md` Step 1–Step 5 — the protocol as executed, with the C gloss
- `review/round4/referee/audit-notes.md` Step 1–Step 4 — the round-4 execution and its evidence statement
- `review/skeptic-review-console.html` — the A/B/C scale in the referee prompt
- `review/round3-adjudication.md`, `review/round4-adjudication.md` — the arbitration step and the counts of executed findings
- `HANDOFF.md` §6 — the protocol's first, incomplete dispatch
