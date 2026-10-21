---
title: "The verdict: a conditional pass"
weight: 40
status: alive
description: "The theory fails in second-order variables and passes iff formulated in first-order ones, the formulation the geometry prefers; what a failure would have left of the program."
provenance: [D, V]
sources:
  - "papers/broken-born-checkpoint-v2.md §7.2"
  - "notes/debt1a-iii-tuning-test.md §3"
  - "notes/debt1a-iii-tuning-test.md §5"
  - "notes/debt1a-ii-X-classification.md §5"
  - "notes/broken-born-theory.md 'Addendum (v0.5)'"
  - "HANDOFF.md §2"
  - "papers/broken-born-checkpoint-v2.md §15"
---

*The verdict of the tuning test is a conditional pass: the program's mass term for the momentum graviton X carries the Boulware–Deser ghost when written in metric (second-order) variables and is ghost-free when written in frame (first-order) variables. The condition is the choice of formulation, and the calc notes argue that it is the formulation the geometry already prefers, because the polarization J and the symplectic vielbein E are both first-order objects. A failure would have reduced the program to a phenomenological shell, gated self-interacting dark matter plus a quintessence field on the Maslov circle, with the geometric story demoted to heuristics. [Checkpoint #11](/wiki/history/documents/checkpoint) §7.2 tags the tuning test [D][V]; the machine checks cover the block algebra and the metric-tier failures, not the frame-tier pass.*

**Status:** Alive — [D][V] in #11 §7.2 — [the verification battery](/wiki/method/verification/battery) checks the metric-tier half (tests T3, T4, T7, all passing); the frame-tier half is [D — structural, resting on T] in `notes/debt1a-iii-tuning-test.md` §3 and has no test.

## Key facts

- Calc note #7 §3 (see [The Debt-1 calc notes](/wiki/history/documents/debt-1-notes)): "Verdict of the tuning test: the theory fails in second-order (metric) variables and passes in first-order (frame) variables. Since the first-order formulation is independently the natural one, this is a conditional pass with the condition being the formulation the geometry already prefers."
- `HANDOFF.md` §2 and the lab notebook's v0.5 addendum both state it as: the theory "passes iff formulated in first-order variables".
- The two halves are [The metric tier fails twice](/wiki/gravity/tuning-test/metric-tier-failures) and [The frame tier: the symplectic vielbein](/wiki/gravity/tuning-test/frame-tier); the object under test is [the misalignment potential](/wiki/gravity/tuning-test/misalignment-potential).
- What a pass does not deliver (#7 §3): "What a pass does not yet deliver: the βₙ coefficients. Those follow from expanding the E–J wedge sector, and they determine M_X, the X–h mixing, and a vacuum-energy contribution." Calc note #8 supplied them: [the palindrome βₙ = β₄₋ₙ](/wiki/gravity/palindromic-branch/palindrome) and [the vacuum-energy identity](/wiki/gravity/palindromic-branch/vacuum-energy-identity).
- The failure branch, as calc note #6 §5 posed it before the test: "Fail ⇒ the Boulware–Deser ghost kills the geometric sector, and [the program] survives only as its phenomenological shell (gated SIDM + Maslov quintessence with the geometric story demoted to heuristics)." SIDM is self-interacting dark matter, here gated by [the velocity gate](/wiki/dark-matter/conjugate-matter/velocity-gate); the quintessence is [τ on the Maslov circle](/wiki/cosmology/dark-energy/tau-quintessence).
- #6 §5 also said that a pass would make "theory" "the defensible word". #11 §15 supersedes this: "the word 'theory' still waits on items 1–3" of §14, the first of which is [deriving the wedge sector from S_H](/wiki/gravity/tuning-test/wedge-reduction).
- The picture that results is [constrained bimetric gravity](/wiki/gravity/tuning-test/constrained-bimetric).
- The count of such tests: #7 §5 counts "three structural tests in a row (multi-graviton no-go, signature obstruction, tuning test)" that "could each have killed the geometric sector outright"; #11 §15, which governs, counts four and lists "forced convergence onto consistency islands" among the program's progressive signs ([Assessment: a live research program](/wiki/program/assessment)).

## Sources

- `papers/broken-born-checkpoint-v2.md` §7.2 — the current statement [D][V]; §15 for "theory" and the count of tests
- `notes/debt1a-iii-tuning-test.md` §3 — the verdict; §5 for the "three structural tests" note
- `notes/debt1a-ii-X-classification.md` §5 — the pass and fail branches as posed before the test
- `notes/broken-born-theory.md` 'Addendum (v0.5)' — the lab notebook's "passes iff" statement
- `HANDOFF.md` §2 — the handoff's summary of the verdict
