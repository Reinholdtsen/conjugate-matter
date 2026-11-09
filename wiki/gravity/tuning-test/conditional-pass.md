---
title: "The verdict: a conditional pass"
weight: 40
status: alive
description: "The theory fails in second-order variables and passes iff formulated in first-order ones, which the calc notes argue are the natural variables; what a failure would have left of the program."
provenance: [D, V]
sources:
  - "wiki/papers/broken-born-checkpoint-v2.md §7.2"
  - "wiki/papers/broken-born-checkpoint-v2.md §7"
  - "wiki/papers/broken-born-checkpoint-v2.md §15"
  - "wiki/papers/broken-born-checkpoint-v2.md §14 item 1"
  - "wiki/papers/broken-born-checkpoint-v2.md §2"
  - "wiki/papers/broken-born-checkpoint-v2.md §1"
  - "notes/tuning-test.md header"
  - "notes/tuning-test.md §3"
  - "notes/tuning-test.md §5"
  - "notes/x-classification.md §3"
  - "notes/x-classification.md §5"
  - "notes/geometric-core.md §D"
  - "notes/beta-coefficients.md §3"
  - "notes/beta-coefficients.md §5"
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

*The verdict of [the tuning test](_index.md) is a conditional pass. The potential that gives the [momentum graviton X](../momentum-graviton/_index.md) its mass carries the [Boulware–Deser ghost](../spin-2-fields/fierz-pauli.md) when it is written in metric, or second-order, variables, and it is [ghost-free](../spin-2-fields/ghosts.md) when it is written in frame, or first-order, variables. The condition is the choice of variables, and the [calc notes](../../history/documents/field-equation-notes.md) argue that the first-order formulation is the natural one anyway, because the [polarization J](../../symmetry-breaking/order-parameter.md) and the [symplectic vielbein E](frame-tier.md) are both first-order objects. Before the test, calc note [#6](../../../notes/x-classification.md) had spelled out what a failure would leave: only a phenomenological shell of [gated](../../dark-matter/conjugate-matter/velocity-gate.md) [self-interacting dark matter](../../dark-matter/halo-astrophysics/self-interacting-dark-matter.md) and [a dark-energy field on the Maslov circle](../../cosmology/dark-energy/tau-quintessence.md), with the geometric story demoted to heuristics. [Checkpoint #11](../../history/documents/checkpoint.md) tags the tuning test [D][V]. The machine checks cover the [metric-tier failures](metric-tier-failures.md); the frame-tier pass is a structural argument with no test, and its potential was selected rather than derived.*

**Status:** Alive — [D][V] in [#11 §7.2](../../papers/broken-born-checkpoint-v2.md#72-the-tuning-test-dv) — the metric-tier half is machine-checked by battery tests T3, T4 and T7, all passing ([the verification battery](../../method/verification/battery.md)); the frame-tier half is [D — structural, resting on T] in calc note [#7 §3](../../../notes/tuning-test.md#3-the-frame-tier-d--structural-resting-on-t) and has no test; the passing class was selected, not derived ([Open: deriving the wedge sector from S_H (OP1)](wedge-reduction.md)).

## The verdict

Calc note #7 ([the field-equation calc notes](../../history/documents/field-equation-notes.md)) states it at the end of its §3:

> **Verdict of the tuning test:** the theory *fails* in second-order (metric) variables and *passes* in first-order (frame) variables. Since the first-order formulation is independently the natural one, this is a conditional pass with the condition being the formulation the geometry already prefers.

The note's opening status line summarizes the work behind it: "Status: computed. Outcome: conditional pass — the condition identified, both branches computed or classified, and the failure mode exhibited explicitly." The lab notebook's v0.5 addendum gives the short form that later documents repeat: "the theory passes iff formulated in first-order variables, which is the formulation the geometry prefers anyway" ([the lab notebook](../../history/documents/lab-notebook.md)). [#11 §7.2](../../papers/broken-born-checkpoint-v2.md#72-the-tuning-test-dv) closes the test with the reason for the condition: "J, E, and the Born connection share the first-order tier, so this is the geometrically minimal formulation."

## The two halves

The test asked whether the potential of [the misalignment potential](misalignment-potential.md), the energy cost of a mismatch between the polarization J and the [modular field](../../phase-space/modular-field/modular-field-z.md) Z, lands in the ghost-free family of Fierz–Pauli, de Rham–Gabadadze–Tolley (dRGT) and Hassan–Rosen potentials ([#7 §1](../../../notes/tuning-test.md#1-the-object-to-test)). The answer depends on the variables in which the potential is written.

| Tier | Variables | The potential is built from | Outcome | Tag | Machine check |
| --- | --- | --- | --- | --- | --- |
| Metric | second-order: the phase-space metric H | the blocks S and A of {J₀, I[Z]} | fails twice: no Fierz–Pauli trace term; Tr(g²) outside the Hassan–Rosen span | [D — rigorous] ([#7 §2](../../../notes/tuning-test.md#2-explicit-computation-metric-tier-d--rigorous)); [D][V] ([#11 §7.2](../../papers/broken-born-checkpoint-v2.md#72-the-tuning-test-dv)) | T3, T4, T7 |
| Frame | first-order: the symplectic vielbein E, with H = EᵀE | wedge polynomials of (E, E₀[J]) | ghost-free by construction, Fierz–Pauli automatic | [D — structural, resting on T] ([#7 §3](../../../notes/tuning-test.md#3-the-frame-tier-d--structural-resting-on-t)) | none |

The negative half is set out on [the metric tier fails twice](metric-tier-failures.md) and the positive half on [the frame tier](frame-tier.md). The standard results the test is measured against are on [the Fierz–Pauli mass term and the Boulware–Deser ghost](../spin-2-fields/fierz-pauli.md), [dRGT massive gravity](../spin-2-fields/drgt-massive-gravity.md) and [Hassan–Rosen bimetric gravity](../spin-2-fields/hassan-rosen-bimetric.md).

## Why the pass is conditional

**The condition is a formulation, not a coefficient.** "The rescue is not a tuning but a *tier change*" ([#7 §3](../../../notes/tuning-test.md#3-the-frame-tier-d--structural-resting-on-t)). No coefficient of a metric-tier potential was adjusted. The coupling was rewritten in other variables, frames instead of metrics, in which the ghost-free potentials are the wedge polynomials of two frames ([the vielbein formulation](../spin-2-fields/vielbein-formulation.md)) and there is "no tuning to miss" ([#7 §3](../../../notes/tuning-test.md#3-the-frame-tier-d--structural-resting-on-t)).

**The case for the condition.** The notes do not treat the choice of variables as free. [#7 §3](../../../notes/tuning-test.md#3-the-frame-tier-d--structural-resting-on-t) places the polarization J and the symplectic vielbein E on one "geometric tier (first-order structures on the tangent, like the Born connection), while H = EᵀE is second-order", and concludes: "Since the first-order formulation is independently the natural one, this is a conditional pass" ([the Born connection](../../phase-space/born-geometry/born-connection.md)).

**What the condition leaves open.** The frame-tier class was argued for, not derived from the program's [geometric action](geometric-action.md): "the class was selected by minimality + consistency, not derived line-by-line" ([#8 §5](../../../notes/beta-coefficients.md#5-what-remains-honest-close-out)). #11 keeps that derivation as open problem 1, "First-principles reduction of the frame-tier wedge sector from S_H (class selected, not derived) [O]" ([#11 §14 item 1](../../papers/broken-born-checkpoint-v2.md#14-open-problems); [Open: deriving the wedge sector from S_H (OP1)](wedge-reduction.md)).

## What was at stake

The test was the end of a narrowing that began in calc note [#5](../../../notes/geometric-core.md). That note defined "the decisive check" as a three-way classification of X: "healthy propagating", "auxiliary" or "ghost", with "Outcomes 1 and 2 both serve the program; only 3 kills" ([#5 §D](../../../notes/geometric-core.md#d-quadratic-spectrum-and-the-ghost-question-partial)). Calc note #6 resolved the classification by symmetry and no-go arguments: "*massive spin-2, conditionally healthy*" ([#6 §5](../../../notes/x-classification.md#5-the-field-equation-problem-after-this-chunk); [why X must be massive](../momentum-graviton/forcing-chain.md)). It left one condition, the one the tuning test checked: "The geometric sector is healthy iff the potential generated by the η-selection lands in the Hassan–Rosen class; a generic potential reintroduces the Boulware–Deser ghost" ([#6 §3](../../../notes/x-classification.md#3-the-mass-mechanism-and-the-endpoint-d--structural)). The notebook's v0.4 addendum records that "The field-equation problem has been reduced to that single tuning computation" ([the three main problems](../../history/main-problems.md)).

[#6 §5](../../../notes/x-classification.md#5-the-field-equation-problem-after-this-chunk) spelled out both branches before the computation:

> **The single remaining computation of the field-equation problem:** derive the X-potential from the η-selection (J–Z) sector and test it against the dRGT coefficient family. Pass ⇒ the geometric core stands and "theory" becomes the defensible word. Fail ⇒ the Boulware–Deser ghost kills the geometric sector, and BBT survives only as its phenomenological shell (gated SIDM + Maslov quintessence with the geometric story demoted to heuristics).

BBT is Broken-Born theory, the program's earlier name, and SIDM is self-interacting dark matter. The shell consists of the dark-matter self-interaction cut off by [the velocity gate](../../dark-matter/conjugate-matter/velocity-gate.md) and the dark-energy field τ on the [Maslov circle](../../phase-space/modular-field/maslov-phase.md) ([τ as quintessence](../../cosmology/dark-energy/tau-quintessence.md)). In the failure branch both would have remained, with the geometric story behind them demoted to heuristics. The pass branch's claim about the word "theory" was later superseded (below).

## What a pass did not deliver

[#7 §3](../../../notes/tuning-test.md#3-the-frame-tier-d--structural-resting-on-t) marks the limit of the result: "What a pass does **not** yet deliver: the βₙ coefficients. Those follow from expanding the E–J wedge sector, and they determine M_X, the X–h mixing, and a vacuum-energy contribution. That coefficient computation is the closing stone of the field-equation problem." Its §5 ranks what remained: "(i) the βₙ coefficient derivation from the E–J wedge sector — the last computation; (ii) τ-not-eaten verification; (iii) Lorentzian dressing of the Euclidean skeleton; (iv) SM-coupling/graviton-mass parametrics. Items (ii)–(iv) are checks; item (i) is the substance" ([#7 §5](../../../notes/tuning-test.md#5-status-of-the-field-equation-problem)), SM being the Standard Model.

Calc note #8 took up item (i). [Reciprocity](../../phase-space/reciprocity/born-reciprocity.md) forces the [palindrome βₙ = β₄₋ₙ](../palindromic-branch/palindrome.md); under it, a flat aligned vacuum forces the wedge sector's vacuum energy to vanish ([the vacuum-energy identity](../palindromic-branch/vacuum-energy-identity.md)); and the five coefficients reduce to two parameters ([spectrum, parameters and reciprocity parity](../momentum-graviton/spectrum-and-parity.md)). #8 closes with "The field-equation problem: solved in structure" and an "Open residue, none of it existential", led by the first-principles reduction of the wedge sector ([#8 §5](../../../notes/beta-coefficients.md#5-what-remains-honest-close-out)).

## How it is verified

- **The metric half is machine-checked.** [#11 §7.2](../../papers/broken-born-checkpoint-v2.md#72-the-tuning-test-dv) tags the tuning test [D][V]. Battery test T3 checks the blocks of the misalignment potential, T4 the missing Fierz–Pauli trace term and T7 the exclusion of p₄ from the span of the [elementary symmetric polynomials](../spin-2-fields/elementary-symmetric-polynomials.md) ([`verify/battery.py`](../../../verify/battery.py); [the verification battery](../../method/verification/battery.md)). All three pass in the current [gate run](../../method/verification/the-gate.md).
- **The frame half is not.** No test covers the frame tier, which stays [D — structural, resting on T] ([#7 §3](../../../notes/tuning-test.md#3-the-frame-tier-d--structural-resting-on-t)). #7's own status line says "both branches computed or classified", and its §5 says "the consistent branch is identified and class-certified (frame tier)" ([#7 §5](../../../notes/tuning-test.md#5-status-of-the-field-equation-problem)): the frame branch was classified by its membership in a known class, not computed term by term. The v1 program paper's tag, "[D — both branches computed]" ([#9 §5 item 4](../../../notes/broken-born-program-v1.md#5-the-second-graviton-and-its-mass-the-field-equation-problem-solved)), is broader than #7's wording.
- **Euclidean skeleton.** The computation assumes a positive-definite metric ([#7 §2](../../../notes/tuning-test.md#2-explicit-computation-metric-tier-d--rigorous)). Its extension to spacetime signature is open problem 3 ([Open: Lorentzian dressing (OP3)](../../phase-space/born-geometry/lorentzian-dressing.md)).

## The count of structural tests

#7 closes with a "Program-level note" that counts the tuning test as the third of three structural tests in a row (the multi-graviton no-go, the signature obstruction, the tuning test). At each, the geometric sector was restricted to "the unique known consistent structure at that junction". The note reads the sequence in the terms of [Lakatos's methodology of research programmes](../../method/lakatosian-methodology.md), as the opposite of a degenerating program. [#11 §15](../../papers/broken-born-checkpoint-v2.md#15-assessment), which governs, counts four such tests and lists them among the program's progressive signs, as does [`HANDOFF.md` §1](../../../HANDOFF.md#1-what-this-project-is); how the program assesses itself on this count is on [the assessment](../../program/assessment.md). Both drop the "known" that #7 keeps (see flag 7 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md)). The lists differ. #7, written before calc note #8, names the [no-go](../spin-2-fields/multi-graviton-no-go.md), the [signature obstruction](../spin-2-fields/signature-obstruction.md) and the tuning test; the v1 program paper names "no-go → Higgs → HR class → palindrome" ([#9 §11](../../../notes/broken-born-program-v1.md#11-assessment)), HR being Hassan–Rosen; [#11 §15](../../papers/broken-born-checkpoint-v2.md#15-assessment) gives the count without a list, while its technical abstract names "A chain of structural results (a compatibility theorem [T][V]; the multi-graviton no-go [8†]; a signature obstruction; an explicit tuning test [V])" ([#11 §1](../../papers/broken-born-checkpoint-v2.md#1-two-abstracts)).

#11 also records the caution that goes with such readings. Its §2 acknowledges "the selection-versus-derivation bias" ([claim tiers and selection bias](../../method/claim-tiers.md)), and [§14 item 1](../../papers/broken-born-checkpoint-v2.md#14-open-problems) marks the frame-tier class as "selected, not derived".

## Superseded: a pass as the threshold for "theory"

Before the test, [#6 §5](../../../notes/x-classification.md#5-the-field-equation-problem-after-this-chunk) made the pass the threshold: "Pass ⇒ the geometric core stands and 'theory' becomes the defensible word." Later documents moved the threshold. The v1 program paper: "The word 'theory' awaits items 1–2 of §10" ([#9 §11](../../../notes/broken-born-program-v1.md#11-assessment)), its items 1 and 2 being the first-principles wedge reduction and the Lorentzian dressing ([#9 §10](../../../notes/broken-born-program-v1.md#10-open-problems)). Checkpoint #11, which governs: "That is a live research program; the word 'theory' still waits on items 1–3 above" ([#11 §15](../../papers/broken-born-checkpoint-v2.md#15-assessment)). Those items are the derivation of the very class that passed ([OP1](wedge-reduction.md)), [the partially-massless comparison (OP2)](../palindromic-branch/pm-comparison.md) and [the Lorentzian dressing (OP3)](../../phase-space/born-geometry/lorentzian-dressing.md). The pass stands, and the word still waits on those three items.

## History

- **Calc note #5 and the v0.3 addendum.** The decisive computation is defined as the healthy / auxiliary / ghost classification of X ([#5 §D](../../../notes/geometric-core.md#d-quadratic-spectrum-and-the-ghost-question-partial); notebook 'Addendum (v0.3, overnight)').
- **Calc note #6 and the v0.4 addendum.** X is a massive spin-2 field, healthy if and only if its potential lands in the Hassan–Rosen class ([#6 §3](../../../notes/x-classification.md#3-the-mass-mechanism-and-the-endpoint-d--structural), [§5](../../../notes/x-classification.md#5-the-field-equation-problem-after-this-chunk)).
- **Calc note #7 and the v0.5 addendum.** "The dRGT tuning test is done": a conditional pass ([#7 §3](../../../notes/tuning-test.md#3-the-frame-tier-d--structural-resting-on-t); notebook 'Addendum (v0.5)').
- **Calc note #8 and the v0.6 addendum.** The coefficients βₙ under reciprocity; the field-equation problem "solved in structure" ([#8 §5](../../../notes/beta-coefficients.md#5-what-remains-honest-close-out)).
- **The v1 program paper** ([#9 §5 item 4](../../../notes/broken-born-program-v1.md#5-the-second-graviton-and-its-mass-the-field-equation-problem-solved), superseded by #11): "The tuning test [D — both branches computed]".
- **Checkpoint #11** ([§7.2](../../papers/broken-born-checkpoint-v2.md#72-the-tuning-test-dv)): "The tuning test [D][V]". Its plain-language opening of [§7](../../papers/broken-born-checkpoint-v2.md#7-the-massive-momentum-graviton): "The health check came down to a tuning test — failed in one formulation, passed in the one the geometry prefers".
- **The handoff** ([`HANDOFF.md` §2](../../../HANDOFF.md#2-scientific-state-one-screen)) lists the frame tier's pass among the results that stand: "passes iff formulated in first-order variables" ([the handoff](../../history/documents/handoff.md)).

## Sources

- [`wiki/papers/broken-born-checkpoint-v2.md` §7.2](../../papers/broken-born-checkpoint-v2.md#72-the-tuning-test-dv) — the current statement [D][V]; [§7](../../papers/broken-born-checkpoint-v2.md#7-the-massive-momentum-graviton) — the plain-language opening; [§15](../../papers/broken-born-checkpoint-v2.md#15-assessment) — the four tests, the progressive signs and "theory" waiting on items 1–3; [§1](../../papers/broken-born-checkpoint-v2.md#1-two-abstracts) — the chain of structural results; [§14 item 1](../../papers/broken-born-checkpoint-v2.md#14-open-problems) — the open derivation; [§2](../../papers/broken-born-checkpoint-v2.md#2-methodological-preface-provenance-and-verification) — the selection-versus-derivation bias.
- [`notes/tuning-test.md`](../../../notes/tuning-test.md) header — the note's status line; [§3](../../../notes/tuning-test.md#3-the-frame-tier-d--structural-resting-on-t) — the verdict and what a pass does not deliver; [§5](../../../notes/tuning-test.md#5-status-of-the-field-equation-problem) — the remaining items, "class-certified", and the three tests.
- [`notes/x-classification.md` §3](../../../notes/x-classification.md#3-the-mass-mechanism-and-the-endpoint-d--structural), [§5](../../../notes/x-classification.md#5-the-field-equation-problem-after-this-chunk) — the health criterion; the pass and fail branches as posed before the test.
- [`notes/geometric-core.md` §D](../../../notes/geometric-core.md#d-quadratic-spectrum-and-the-ghost-question-partial) — the three-way classification.
- [`notes/beta-coefficients.md` §3](../../../notes/beta-coefficients.md#3-spectrum-parameters-selection-structure-d--t), [§5](../../../notes/beta-coefficients.md#5-what-remains-honest-close-out) — the two parameters; the field-equation problem "solved in structure" and its residue.
- [`notes/broken-born-theory.md`](../../../notes/broken-born-theory.md) 'Addendum (v0.3, overnight)', 'Addendum (v0.4)', 'Addendum (v0.5)' — the notebook's record of each step, including "passes iff".
- [`notes/broken-born-program-v1.md` §5](../../../notes/broken-born-program-v1.md#5-the-second-graviton-and-its-mass-the-field-equation-problem-solved), [§10](../../../notes/broken-born-program-v1.md#10-open-problems), [§11](../../../notes/broken-born-program-v1.md#11-assessment) — "[D — both branches computed]"; the v1 open items; "theory" awaiting items 1–2 and the four-step list.
- [`HANDOFF.md` §1](../../../HANDOFF.md#1-what-this-project-is), [§2](../../../HANDOFF.md#2-scientific-state-one-screen) — four consecutive tests; the handoff's summary of the verdict.
- [`verify/battery.py`](../../../verify/battery.py) T3, T4, T7 — the machine checks of the metric half.
- [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md) item 7 — "the unique consistent structure" without the "known" that [#6 §3](../../../notes/x-classification.md#3-the-mass-mechanism-and-the-endpoint-d--structural) and [#7 §5](../../../notes/tuning-test.md#5-status-of-the-field-equation-problem) keep; pending.
