---
title: "The iron rule: no arithmetic by eyeball"
weight: 10
status: method
description: "Every asserted or disputed number gets executed code with printed output, kept in verify/; why the AI referees' arithmetic errors made this load-bearing."
sources:
  - "CLAUDE.md 'Method'"
  - "HANDOFF.md §5"
  - "HANDOFF.md §6"
  - "review/round3-adjudication.md 'Pre-registration scored'"
  - "review/round3-adjudication.md header"
  - "review/round4-adjudication.md header"
  - "scripts/check.sh"
  - "wiki/CLAUDE.md 'The wiki is derivative'"
---

*The iron rule is the program's requirement that no number be accepted on inspection: every number a document asserts, and every number a reviewer disputes, is computed by code that is actually run and prints its result, and the code is kept in the repository's `verify/` folder. It was adopted after the first two blind reviews, in which AI referees made three confident accusations of order-of-magnitude errors that all came from their own unit mistakes. The rule makes the arithmetic checkable by anyone who runs the scripts. It does not make the physics right, which round 3 showed.*

**Status:** Method, in force — untagged — root `CLAUDE.md` ('Method') and `HANDOFF.md` §5; enforced by [the gate](/wiki/method/verification/the-gate).

## Key facts

- **The rule.** "Iron rule: no arithmetic by eyeball. Every asserted or disputed number gets executed code with printed output, kept in `verify/`." (root `CLAUDE.md`). The handoff's version adds: "This is load-bearing — see §6." (`HANDOFF.md` §5).
- **Why it is load-bearing.** After review rounds 1 and 2, `HANDOFF.md` §6 recorded the referees' failure mode. The referees were large language models working blind: "fresh LLM referees are strong on structure, literature and logic; unreliable on unaided arithmetic (3 confident order-of-magnitude indictments, all reviewer unit errors, 0 surviving). Hence the iron rule." See [The measured referee failure mode](/wiki/method/review/referee-failure-mode).
- **The errors it answered.** Round 1's referee errors included a "GeV→gram conversion off 10³" and "σ_T/M misread as σ_T (off ~10⁴³)"; round 2's referee "fed ρ_DM = 1.26×10⁻³ GeV/cm³ instead of 1.26×10⁻⁶ (the manuscript's own number) — with the right input the closure lands within 3%" (`HANDOFF.md` §6; [Review rounds 1 and 2](/wiki/method/review/rounds-one-and-two)). Each was settled by executed code ("machine-arbitrated").
- **Why the project moved.** "Claude Code's native execution removes this failure mode — that's the main reason the project is moving to you." (`HANDOFF.md` §6; [The collaboration](/wiki/method/collaboration)). Since the move the referees run code as well: in round 3 "Every one of its 16 numerical findings rests on executed code", and in round 4 "All 9 of its numerical and algebraic indictments rest on executed code" (adjudication headers).
- **How it is enforced.** The scripts in `verify/` run in `scripts/check.sh`, the gate that must pass before work is called finished ([The gate](/wiki/method/verification/the-gate)).
- **Its limit.** Round 3 found a wrong physical input in a manuscript whose every number had been computed by a gated script: "The failure mode has moved. In rounds 1–2 it was the referee's unaided arithmetic. In round 3 it is that the author's verification checks the author's model: a wrong physics input passes a gate that tests only arithmetic." (`review/round3-adjudication.md`). See [Verification checks arithmetic, not the model](/wiki/method/verification/arithmetic-not-model) and [Independent anchors](/wiki/method/verification/independent-anchors).
- **In the wiki.** The wiki applies the rule to itself: every number on a page is copied from a source document or a `verify/` output, and "Nothing is computed, rounded or converted by eye" (`wiki/CLAUDE.md`).

## Sources

- Root `CLAUDE.md` 'Method' — the rule as now stated
- `HANDOFF.md` §5 — the rule at the handoff; §6 — the referee failure mode and the move to Claude Code
- `review/round3-adjudication.md` 'Pre-registration scored' and header; `review/round4-adjudication.md` header — the shifted failure mode; referees' findings resting on executed code
- `scripts/check.sh` — the gate that runs the scripts
- `wiki/CLAUDE.md` 'The wiki is derivative' — the rule applied to the wiki
