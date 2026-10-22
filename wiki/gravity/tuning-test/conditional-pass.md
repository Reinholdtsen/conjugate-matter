---
title: "The verdict: a conditional pass"
weight: 40
status: alive
description: "The theory fails in second-order variables and passes iff formulated in first-order ones, which the calc notes argue are the natural variables; what a failure would have left of the program."
provenance: [D, V]
sources:
  - "papers/broken-born-checkpoint-v2.md §7.2"
  - "papers/broken-born-checkpoint-v2.md §7"
  - "papers/broken-born-checkpoint-v2.md §15"
  - "papers/broken-born-checkpoint-v2.md §14 item 1"
  - "papers/broken-born-checkpoint-v2.md §2"
  - "papers/broken-born-checkpoint-v2.md §1"
  - "notes/debt1a-iii-tuning-test.md header"
  - "notes/debt1a-iii-tuning-test.md §3"
  - "notes/debt1a-iii-tuning-test.md §5"
  - "notes/debt1a-ii-X-classification.md §3"
  - "notes/debt1a-ii-X-classification.md §5"
  - "notes/debt1a-geometric-core.md §D"
  - "notes/debt1a-iv-beta-coefficients.md §3"
  - "notes/debt1a-iv-beta-coefficients.md §5"
  - "notes/broken-born-theory.md 'Addendum (v0.3, overnight)'"
  - "notes/broken-born-theory.md 'Addendum (v0.4)'"
  - "notes/broken-born-theory.md 'Addendum (v0.5)'"
  - "notes/broken-born-program-v1.md §5"
  - "notes/broken-born-program-v1.md §10"
  - "notes/broken-born-program-v1.md §11"
  - "HANDOFF.md §1"
  - "HANDOFF.md §2"
  - "verify/battery.py T3"
  - "verify/battery.py T4"
  - "verify/battery.py T7"
  - "review/wiki-build-flags.md item 7"
---

*The verdict of [the tuning test](/wiki/gravity/tuning-test) is a conditional pass. The potential that gives the [momentum graviton X](/wiki/gravity/momentum-graviton) its mass carries the [Boulware–Deser ghost](/wiki/gravity/spin-2-fields/fierz-pauli) when it is written in metric, or second-order, variables, and it is ghost-free when it is written in frame, or first-order, variables. The condition is the choice of variables, and the [calc notes](/wiki/history/documents/debt-1-notes) argue that the first-order formulation is the natural one anyway, because the [polarization J](/wiki/symmetry-breaking/order-parameter) and the [symplectic vielbein E](/wiki/gravity/tuning-test/frame-tier) are both first-order objects. Before the test, calc note #6 had spelled out what a failure would leave: only a phenomenological shell of [gated](/wiki/dark-matter/conjugate-matter/velocity-gate) [self-interacting dark matter](/wiki/dark-matter/halo-astrophysics/self-interacting-dark-matter) and [a dark-energy field on the Maslov circle](/wiki/cosmology/dark-energy/tau-quintessence), with the geometric story demoted to heuristics. [Checkpoint #11](/wiki/history/documents/checkpoint) tags the tuning test [D][V]. The machine checks cover the [metric-tier failures](/wiki/gravity/tuning-test/metric-tier-failures); the frame-tier pass is a structural argument with no test, and its potential was selected rather than derived.*

**Status:** Alive — [D][V] in #11 §7.2 — the metric-tier half is machine-checked by battery tests T3, T4 and T7, all passing ([the verification battery](/wiki/method/verification/battery)); the frame-tier half is [D — structural, resting on T] in calc note #7 §3 and has no test; the passing class was selected, not derived ([Open: deriving the wedge sector from S_H (OP1)](/wiki/gravity/tuning-test/wedge-reduction)).

## The verdict

Calc note #7 ([the Debt-1 calc notes](/wiki/history/documents/debt-1-notes)) states it at the end of its §3:

> **Verdict of the tuning test:** the theory *fails* in second-order (metric) variables and *passes* in first-order (frame) variables. Since the first-order formulation is independently the natural one, this is a conditional pass with the condition being the formulation the geometry already prefers.

The note's opening status line summarizes the work behind it: "Status: computed. Outcome: conditional pass — the condition identified, both branches computed or classified, and the failure mode exhibited explicitly." The lab notebook's v0.5 addendum gives the short form that later documents repeat: "the theory passes iff formulated in first-order variables, which is the formulation the geometry prefers anyway" ([the lab notebook](/wiki/history/documents/lab-notebook)). #11 §7.2 closes the test with the reason for the condition: "J, E, and the Born connection share the first-order tier, so this is the geometrically minimal formulation."

## The two halves

The test asked whether the potential of [the misalignment potential](/wiki/gravity/tuning-test/misalignment-potential), the energy cost of a mismatch between the polarization J and the [modular field](/wiki/phase-space/modular-field/modular-field-z) Z, lands in the ghost-free family of Fierz–Pauli, de Rham–Gabadadze–Tolley (dRGT) and Hassan–Rosen potentials (#7 §1). The answer depends on the variables in which the potential is written.

| Tier | Variables | The potential is built from | Outcome | Tag | Machine check |
| --- | --- | --- | --- | --- | --- |
| Metric | second-order: the phase-space metric H | the blocks S and A of {J₀, I[Z]} | fails twice: no Fierz–Pauli trace term; Tr(g²) outside the Hassan–Rosen span | [D — rigorous] (#7 §2); [D][V] (#11 §7.2) | T3, T4, T7 |
| Frame | first-order: the symplectic vielbein E, with H = EᵀE | wedge polynomials of (E, E₀[J]) | ghost-free by construction, Fierz–Pauli automatic | [D — structural, resting on T] (#7 §3) | none |

The negative half is set out on [the metric tier fails twice](/wiki/gravity/tuning-test/metric-tier-failures) and the positive half on [the frame tier](/wiki/gravity/tuning-test/frame-tier). The standard results the test is measured against are on [the Fierz–Pauli mass term and the Boulware–Deser ghost](/wiki/gravity/spin-2-fields/fierz-pauli), [dRGT massive gravity](/wiki/gravity/spin-2-fields/drgt-massive-gravity) and [Hassan–Rosen bimetric gravity](/wiki/gravity/spin-2-fields/hassan-rosen-bimetric).

## Why the pass is conditional

**The condition is a formulation, not a coefficient.** "The rescue is not a tuning but a *tier change*" (#7 §3). No coefficient of a metric-tier potential was adjusted. The coupling was rewritten in other variables, frames instead of metrics, in which the ghost-free potentials are the wedge polynomials of two frames ([the vielbein formulation](/wiki/gravity/spin-2-fields/vielbein-formulation)) and there is "no tuning to miss" (#7 §3).

**The case for the condition.** The notes do not treat the choice of variables as free. #7 §3 places the polarization J and the symplectic vielbein E on one "geometric tier (first-order structures on the tangent, like the Born connection), while H = EᵀE is second-order", and concludes: "Since the first-order formulation is independently the natural one, this is a conditional pass" ([the Born connection](/wiki/phase-space/born-geometry/born-connection)).

**What the condition leaves open.** The frame-tier class was argued for, not derived from the program's [geometric action](/wiki/gravity/tuning-test/geometric-action): "the class was selected by minimality + consistency, not derived line-by-line" (#8 §5). #11 keeps that derivation as open problem 1, "First-principles reduction of the frame-tier wedge sector from S_H (class selected, not derived) [O]" (#11 §14 item 1; [Open: deriving the wedge sector from S_H (OP1)](/wiki/gravity/tuning-test/wedge-reduction)).

## What was at stake

The test was the end of a narrowing that began in calc note #5. That note defined "the decisive check" as a three-way classification of X: "healthy propagating", "auxiliary" or "ghost", with "Outcomes 1 and 2 both serve the program; only 3 kills" (#5 §D). Calc note #6 resolved the classification by symmetry and no-go arguments: "*massive spin-2, conditionally healthy*" (#6 §5; [why X must be massive](/wiki/gravity/momentum-graviton/forcing-chain)). It left one condition, the one the tuning test checked: "The geometric sector is healthy iff the potential generated by the η-selection lands in the Hassan–Rosen class; a generic potential reintroduces the Boulware–Deser ghost" (#6 §3). The notebook's v0.4 addendum records that "Debt 1 has been reduced to that single tuning computation" ([the three debts](/wiki/history/debts)).

#6 §5 spelled out both branches before the computation:

> **The single remaining computation of Debt 1:** derive the X-potential from the η-selection (J–Z) sector and test it against the dRGT coefficient family. Pass ⇒ the geometric core stands and "theory" becomes the defensible word. Fail ⇒ the Boulware–Deser ghost kills the geometric sector, and BBT survives only as its phenomenological shell (gated SIDM + Maslov quintessence with the geometric story demoted to heuristics).

BBT is the Broken-Born program, and SIDM is self-interacting dark matter. The shell consists of the dark-matter self-interaction cut off by [the velocity gate](/wiki/dark-matter/conjugate-matter/velocity-gate) and the dark-energy field τ on the [Maslov circle](/wiki/phase-space/modular-field/maslov-phase) ([τ as quintessence](/wiki/cosmology/dark-energy/tau-quintessence)). In the failure branch both would have remained, with the geometric story behind them demoted to heuristics. The pass branch's claim about the word "theory" was later superseded (below).

## What a pass did not deliver

#7 §3 marks the limit of the result: "What a pass does **not** yet deliver: the βₙ coefficients. Those follow from expanding the E–J wedge sector, and they determine M_X, the X–h mixing, and a vacuum-energy contribution. That coefficient computation is the closing stone of Debt 1." Its §5 ranks what remained: "(i) the βₙ coefficient derivation from the E–J wedge sector — the last computation; (ii) τ-not-eaten verification; (iii) Lorentzian dressing of the Euclidean skeleton; (iv) SM-coupling/graviton-mass parametrics. Items (ii)–(iv) are checks; item (i) is the substance" (#7 §5), SM being the Standard Model.

Calc note #8 took up item (i). [Reciprocity](/wiki/phase-space/reciprocity/born-reciprocity) forces the [palindrome βₙ = β₄₋ₙ](/wiki/gravity/palindromic-branch/palindrome); under it, a flat aligned vacuum forces the wedge sector's vacuum energy to vanish ([the vacuum-energy identity](/wiki/gravity/palindromic-branch/vacuum-energy-identity)); and the five coefficients reduce to two parameters ([spectrum, parameters and reciprocity parity](/wiki/gravity/momentum-graviton/spectrum-and-parity)). #8 closes with "Debt 1: structurally paid" and an "Open residue, none of it existential", led by the first-principles reduction of the wedge sector (#8 §5).

## How it is verified

- **The metric half is machine-checked.** #11 §7.2 tags the tuning test [D][V]. Battery test T3 checks the blocks of the misalignment potential, T4 the missing Fierz–Pauli trace term and T7 the exclusion of p₄ from the span of the [elementary symmetric polynomials](/wiki/gravity/spin-2-fields/elementary-symmetric-polynomials) (`verify/battery.py`; [the verification battery](/wiki/method/verification/battery)). All three pass in the current [gate run](/wiki/method/verification/the-gate).
- **The frame half is not.** No test covers the frame tier, which stays [D — structural, resting on T] (#7 §3). #7's own status line says "both branches computed or classified", and its §5 says "the consistent branch is identified and class-certified (frame tier)" (#7 §5): the frame branch was classified by its membership in a known class, not computed term by term. The v1 program paper's tag, "[D — both branches computed]" (#9 §5 item 4), is broader than #7's wording.
- **Euclidean skeleton.** The computation assumes a positive-definite metric (#7 §2). Its extension to spacetime signature is open problem 3 ([Open: Lorentzian dressing (OP3)](/wiki/phase-space/born-geometry/lorentzian-dressing)).

## Forced convergence: how the program reads the result

#7 closes with a "Program-level note":

> three structural tests in a row (multi-graviton no-go, signature obstruction, tuning test) could each have killed the geometric sector outright; each instead forced it into the unique known consistent structure at that junction. Repeated forced convergence onto consistency islands is the opposite of degeneration.

"Degeneration" is the term of [Lakatos's methodology of research programmes](/wiki/method/lakatosian-methodology) for a program that only redescribes what it meets: in the v1 paper's words, "Programs that keep predicting novel facts are progressive; programs that only redescribe are degenerating" (#9 §11). #11 §15, which governs, counts four such tests, "four consecutive consistency tests each forced the theory onto the unique consistent structure available", and lists "forced convergence onto consistency islands" first among the program's progressive signs ([the assessment](/wiki/program/assessment)). The handoff says the same: "the structural core survived four consecutive consistency tests by being forced onto unique consistent structures each time" (`HANDOFF.md` §1). Both drop the "known" that #7 keeps (see flag 7 in `review/wiki-build-flags.md`). The lists differ. #7, written before calc note #8, names the [no-go](/wiki/gravity/spin-2-fields/multi-graviton-no-go), the [signature obstruction](/wiki/gravity/spin-2-fields/fierz-pauli#the-signature-obstruction) and the tuning test; the v1 program paper names "no-go → Higgs → HR class → palindrome" (#9 §11), HR being Hassan–Rosen; #11 §15 gives the count without a list, while its technical abstract names "A chain of structural results (a compatibility theorem [T][V]; the multi-graviton no-go [8†]; a signature obstruction; an explicit tuning test [V])" (#11 §1).

#11 also records the caution that goes with such readings. Its §2 acknowledges "the selection-versus-derivation bias" ([claim tiers and selection bias](/wiki/method/claim-tiers)), and §14 item 1 marks the frame-tier class as "selected, not derived".

## Superseded: a pass as the threshold for "theory"

Before the test, #6 §5 made the pass the threshold: "Pass ⇒ the geometric core stands and 'theory' becomes the defensible word." Later documents moved the threshold. The v1 program paper: "The word 'theory' awaits items 1–2 of §10" (#9 §11), its items 1 and 2 being the first-principles wedge reduction and the Lorentzian dressing (#9 §10). Checkpoint #11, which governs: "That is a live research program; the word 'theory' still waits on items 1–3 above" (#11 §15). Those items are the derivation of the very class that passed ([OP1](/wiki/gravity/tuning-test/wedge-reduction)), [the partially-massless comparison (OP2)](/wiki/gravity/palindromic-branch/pm-comparison) and [the Lorentzian dressing (OP3)](/wiki/phase-space/born-geometry/lorentzian-dressing). The pass stands, and the word still waits on those three items.

## History

- **Calc note #5 and the v0.3 addendum.** The decisive computation is defined as the healthy / auxiliary / ghost classification of X (#5 §D; notebook 'Addendum (v0.3, overnight)').
- **Calc note #6 and the v0.4 addendum.** X is a massive spin-2 field, healthy if and only if its potential lands in the Hassan–Rosen class (#6 §3, §5).
- **Calc note #7 and the v0.5 addendum.** "The dRGT tuning test is done": a conditional pass (#7 §3; notebook 'Addendum (v0.5)').
- **Calc note #8 and the v0.6 addendum.** The coefficients βₙ under reciprocity; Debt 1 "structurally paid" (#8 §5).
- **The v1 program paper** (#9 §5 item 4, superseded by #11): "The tuning test [D — both branches computed]".
- **Checkpoint #11** (§7.2): "The tuning test [D][V]". Its plain-language opening of §7: "The health check came down to a tuning test — failed in one formulation, passed in the one the geometry prefers".
- **The handoff** (`HANDOFF.md` §2) lists the frame tier's pass among the results that stand: "passes iff formulated in first-order variables" ([the handoff](/wiki/history/documents/handoff)).

## Sources

- `papers/broken-born-checkpoint-v2.md` §7.2 — the current statement [D][V]; §7 — the plain-language opening; §15 — the four tests, the progressive signs and "theory" waiting on items 1–3; §1 — the chain of structural results; §14 item 1 — the open derivation; §2 — the selection-versus-derivation bias.
- `notes/debt1a-iii-tuning-test.md` header — the note's status line; §3 — the verdict and what a pass does not deliver; §5 — the remaining items, "class-certified", and the three tests.
- `notes/debt1a-ii-X-classification.md` §3, §5 — the health criterion; the pass and fail branches as posed before the test.
- `notes/debt1a-geometric-core.md` §D — the three-way classification.
- `notes/debt1a-iv-beta-coefficients.md` §3, §5 — the two parameters; Debt 1 "structurally paid" and its residue.
- `notes/broken-born-theory.md` 'Addendum (v0.3, overnight)', 'Addendum (v0.4)', 'Addendum (v0.5)' — the notebook's record of each step, including "passes iff".
- `notes/broken-born-program-v1.md` §5, §10, §11 — "[D — both branches computed]"; the v1 open items; "theory" awaiting items 1–2 and the four-step list.
- `HANDOFF.md` §1, §2 — four consecutive tests; the handoff's summary of the verdict.
- `verify/battery.py` T3, T4, T7 — the machine checks of the metric half.
- `review/wiki-build-flags.md` item 7 — "the unique consistent structure" without the "known" that #6 §3 and #7 §5 keep; awaiting Paul's ruling.
