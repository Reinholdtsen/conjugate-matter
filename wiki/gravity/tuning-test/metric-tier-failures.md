---
title: "The metric tier fails twice"
weight: 20
status: alive
description: "Potentials built from metrics give a mass with no Fierz–Pauli trace term (T4: 66.58 vs 63.72) and a nonlinear structure outside the Hassan–Rosen span (T7: rms 3.29), so the Boulware–Deser ghost returns."
provenance: [D, V]
sources:
  - "wiki/papers/broken-born-checkpoint-v2.md §7.2"
  - "wiki/papers/broken-born-checkpoint-v2.md §2"
  - "wiki/papers/broken-born-checkpoint-v2.md §5"
  - "wiki/papers/broken-born-checkpoint-v2.md §6"
  - "notes/tuning-test.md §2"
  - "notes/tuning-test.md §3"
  - "notes/tuning-test.md §5"
  - "verify/battery.py T4"
  - "verify/battery.py T7"
  - "HANDOFF.md §5"
  - "HANDOFF.md §2"
  - "HANDOFF.md Appendix A"
  - "notes/x-classification.md §3"
  - "notes/x-classification.md §5"
  - "notes/broken-born-theory.md 'Addendum (v0.5)'"
  - "notes/broken-born-program-v1.md §5"
  - "popsci/angle-of-the-mirror.md 'The method is the message'"
  - "review/wiki-build-flags.md items 4, 14, 36"
  - "review/wiki-build-checks/sqrt_eig_check.out"
---

*The metric tier is the naive way, in [calc note #7](../../history/documents/field-equation-notes.md)'s word, of writing the mass term of the [momentum graviton X](../momentum-graviton/_index.md): as a function of metric-level, second-order quantities, the blocks of the [misalignment potential](misalignment-potential.md). It fails the [ghost-freedom](../spin-2-fields/ghosts.md#how-ghost-freedom-is-checked-t) test in two independent ways. At quadratic order the natural potential gives the metric fluctuation h a mass term proportional to Tr(h²) without the −(Tr h)² term that the [Fierz–Pauli](../spin-2-fields/fierz-pauli.md) form requires. Beyond quadratic order it contains Tr(g²), which is not a linear combination of the [elementary symmetric polynomials](../spin-2-fields/elementary-symmetric-polynomials.md) from which every ghost-free [Hassan–Rosen](../spin-2-fields/hassan-rosen-bimetric.md) potential is built. Either failure lets the Boulware–Deser ghost, an extra mode with negative kinetic energy, propagate [T]. Calc note [#7](../../../notes/tuning-test.md) calls the result a "theorem-grade negative", and tests T4 and T7 of [the verification battery](../../method/verification/battery.md) check both failures by machine. The way out was a change of variables, to [the frame tier](frame-tier.md).*

**Status:** Alive, as a [negative result](../../method/negative-results.md) — [D — rigorous] in calc note [#7 §2](../../../notes/tuning-test.md#2-explicit-computation-metric-tier-d--rigorous), which calls it "theorem-grade"; [D][V] in [checkpoint #11](../../history/documents/checkpoint.md) [§7.2](../../papers/broken-born-checkpoint-v2.md#72-the-tuning-test-dv) — battery tests T4 and T7 pass ([the verification battery](../../method/verification/battery.md)); the second invariant, and [#11](../../papers/broken-born-checkpoint-v2.md)'s "provably" for the full structure Tr(g²) + Tr(g⁻²), rest on the derivation [D] alone.

## The claim

Calc note #7 ([the field-equation calc notes](../../history/documents/field-equation-notes.md)) heads its §2 "Explicit computation, metric tier [D — rigorous]" and closes it:

> **Every metric-tier (second-order, H-coupled) misalignment invariant tested lands off the tuning.** This half of the test is a theorem-grade negative: the naive implementation of η-selection has the Boulware–Deser ghost.

Checkpoint #11 states both failures in one sentence [D][V] ([#11 §7.2](../../papers/broken-born-checkpoint-v2.md#72-the-tuning-test-dv)): "*Metric-tier* implementations fail twice: quadratic mass m²Tr(h²) with no −(Tr h)² (non-FP at linear order — the 66.58-vs-63.72 test of §2), and nonlinear structure Tr(g²) + Tr(g⁻²) provably outside the linear-in-eₙ span (T7). Boulware–Deser ghost." FP stands for Fierz–Pauli.

"Metric tier" names the variables. The potential is built from H, the phase-space metric, through the anticommutator {J₀, I[Z]} = [[S, A], [A, S]], with S = Y + XY⁻¹X − Y⁻¹ and A = [X, Y⁻¹] ([the misalignment potential](misalignment-potential.md)). [#7 §3](../../../notes/tuning-test.md#3-the-frame-tier-d--structural-resting-on-t) calls H = EᵀE, which is quadratic in the frame E, "second-order", and calls E and the [polarization J](../../symmetry-breaking/order-parameter.md) "first-order structures on the tangent" ([the frame tier](frame-tier.md)). "The tuning" is the special set of coefficients that makes a spin-2 mass term ghost-free.

## What a ghost-free mass term needs [T]

A massive spin-2 field in four dimensions has five polarizations ([#6 §3](../../../notes/x-classification.md#3-the-mass-mechanism-and-the-endpoint-d--structural)). Two standard results fix what its mass term may look like [T]:

- **At quadratic order, the Fierz–Pauli form.** A quadratic mass term for a symmetric tensor fluctuation h is built from Tr(h²) and (Tr h)². Only the combination proportional to Tr(h²) − (Tr h)² propagates the five polarizations alone. Any other ratio adds a further mode with negative kinetic energy, a ghost. The fixed ratio is the "Fierz–Pauli tuning" ([the Fierz–Pauli mass term and the Boulware–Deser ghost](../spin-2-fields/fierz-pauli.md)).
- **Beyond quadratic order, the dRGT and Hassan–Rosen potentials.** A generic nonlinear completion of the Fierz–Pauli term brings the ghost back; this is the Boulware–Deser ghost. The ghost-free completions are the potentials of de Rham–Gabadadze–Tolley (dRGT) massive gravity and of Hassan–Rosen bimetric gravity, which [#7 §2](../../../notes/tuning-test.md#2-explicit-computation-metric-tier-d--rigorous) characterizes as "*linear* combinations Σβₙeₙ(√(g⁻¹f)) (constants βₙ)". Here eₙ is the n-th [elementary symmetric polynomial](../spin-2-fields/elementary-symmetric-polynomials.md) of the eigenvalues of the matrix square root √(g⁻¹f), and f is the second, or reference, metric ([dRGT massive gravity](../spin-2-fields/drgt-massive-gravity.md); [Hassan–Rosen bimetric gravity](../spin-2-fields/hassan-rosen-bimetric.md)).

A candidate potential therefore has two checks to pass: its quadratic part must have the Fierz–Pauli ratio, and the full potential must be a linear combination of the eₙ. The metric tier fails each one.

## Failure 1: a mass with no Fierz–Pauli trace term

### The expansion

[#7 §2](../../../notes/tuning-test.md#2-explicit-computation-metric-tier-d--rigorous) expands the blocks around the vacuum frame, where the reference metric is the identity, writing the metric as Y = 1 + h and the momentum graviton as X = x:

> 2. **Linearized spectrum of the quadratic invariant.** With Y = 1 + h, X = x: S = 2h + x² + O(3), A = [h, x] + O(3). Any potential of the class Tr({J,I}²)-with-positive-norm gives, at quadratic order, m²Tr(h²) — a graviton mass **without** the −(Tr h)² companion. That violates Fierz–Pauli already at linear order: Boulware–Deser ghost, immediately.

S begins at first order with 2h, so its square begins at second order with 4h², and Tr(S²) is 4Tr(h²) to that order. That is the limit [#11 §2](../../papers/broken-born-checkpoint-v2.md#2-methodological-preface-provenance-and-verification) records: "Tr(S²)/ε² → 4Tr(h²) to six digits, visibly ≠ the Fierz–Pauli form". The result has a Tr(h²) term and no (Tr h)² term, a ratio other than the Fierz–Pauli one. The mass is a mass for h, the fluctuation of the ordinary metric; a quadratic mass for X comes from the second invariant below. A suspected slip in #7's expansion of S is flag 4 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md), which notes that the quadratic-order test is unaffected; this page quotes #7 as written.

### The machine check: battery test T4

Test T4 of [`verify/battery.py`](../../../verify/battery.py) draws a random symmetric h and x at d = 4 from the seeded generator (seed 0), sets Y = 1 + εh and X = εx, and evaluates Tr(S²)/ε² at two small values of ε (`1e-4` and `1e-5` in the script). It compares the result with 4Tr(h²) and with the Fierz–Pauli form, which the script computes as 4(Tr(h²) − (Tr h)²). The current [gate run](../../method/verification/the-gate.md) prints:

```text
      T4 eps=0.0001: 66.5772 vs 4Tr(h^2)=66.5770 vs FP=63.7221
      T4 eps=1e-05: 66.5770 vs 4Tr(h^2)=66.5770 vs FP=63.7221
PASS  T4 Tr(S^2)/eps^2 -> 4Tr(h^2) (rel 1e-5 at eps=1e-5)
PASS  T4 limit differs from Fierz-Pauli form (rel > 1%)
PASS  T4 parity: 66.58 vs 63.72 as quoted  [66.58 vs 63.72]
```

The first check passes when, at ε = `1e-5`, the value agrees with 4Tr(h²) to a relative tolerance of `1e-5`. The second passes when it differs from the Fierz–Pauli value by more than 1% relative. The third, a parity check, confirms that this environment reproduces the figures the documents quote. The two figures belong to one random h: "66.58 vs 63.72 at seed 0" ([`HANDOFF.md` §5](../../../HANDOFF.md#5-verification-protocol-the-method--keep-using-it)). The general statement is the derivation [D]; the test confirms it at that point.

### Where the figures are quoted

[#11 §7.2](../../papers/broken-born-checkpoint-v2.md#72-the-tuning-test-dv) refers to "the 66.58-vs-63.72 test of §2", and the docstring of [`verify/battery.py`](../../../verify/battery.py) also places the figures in [#11 §2](../../papers/broken-born-checkpoint-v2.md#2-methodological-preface-provenance-and-verification). [#11 §2](../../papers/broken-born-checkpoint-v2.md#2-methodological-preface-provenance-and-verification) describes the test in words without printing the two numbers, which appear in [`HANDOFF.md` §5](../../../HANDOFF.md#5-verification-protocol-the-method--keep-using-it) and in the script's output. The wiki cites [#11 §7.2](../../papers/broken-born-checkpoint-v2.md#72-the-tuning-test-dv) and battery test T4 for them ([conflicts between the documents](../../history/documents/source-conflicts.md); see flag 36 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md)).

## A second invariant, the same defect

[#7 §2](../../../notes/tuning-test.md#2-explicit-computation-metric-tier-d--rigorous) also tried a second metric-tier invariant:

> A second natural invariant (built from [J, I] + 2K, which vanishes at the vacuum) was computed the same way: it does give X a quadratic mass — again as Tr(x²) with no trace subtraction. Same disease.

K is the third structure of Born geometry, K = η⁻¹ω ([#11 §5](../../papers/broken-born-checkpoint-v2.md#5-the-kinematic-core-and-the-compatibility-theorem); [the structures ω, η, H](../../phase-space/born-geometry/born-structures.md)). This invariant gives the momentum graviton a quadratic mass, and that mass also lacks the trace term. No battery test covers it, so the second invariant is derived [D] and not machine-checked.

## Failure 2: outside the Hassan–Rosen family

### The X = 0 slice

The third consequence [#7 §2](../../../notes/tuning-test.md#2-explicit-computation-metric-tier-d--rigorous) reads off the blocks is a nonlinear one:

> 3. **Nonlinear check against the dRGT span.** The X = 0 slice gives Tr(S²) = Tr(g²) + Tr(g⁻²) − 2d. The Hassan–Rosen ghost-free family is *linear* combinations Σβₙeₙ(√(g⁻¹f)) (constants βₙ); Tr(g²) = p₄ of the square-root eigenvalues is a *nonlinear* polynomial in the eₙ, hence outside the family. Fail again, independently of the linearized check.

On the slice X = 0 the block S reduces to Y − Y⁻¹, and Y is the metric g ([#11 §6](../../papers/broken-born-checkpoint-v2.md#6-the-modular-field)). The square of g − g⁻¹ has trace Tr(g²) + Tr(g⁻²) − 2d, because g g⁻¹ is the d-dimensional identity. The relation is exact on the slice, not an expansion.

### Why Tr(g²) lies outside the family

The power sum p₄ of a set of numbers is the sum of their fourth powers. Newton's identities express each power sum through the elementary symmetric polynomials of the same numbers, and the expression for p₄ contains products of them [T], so p₄ is not a linear combination of e₀ to e₄ with constant coefficients. #7's argument applies this to Tr(g²), which it calls "p₄ of the square-root eigenvalues": as a nonlinear polynomial in the eₙ, it lies outside the Hassan–Rosen family, whose potentials are all linear in them.

The argument needs p₄ and the eₙ to be taken over the same numbers, so it matters which square root supplies them. In #7's vacuum frame the reference metric f is the identity, so √(f⁻¹g) is √g and √(g⁻¹f) is √(g⁻¹). Tr(g²) is p₄ of the eigenvalues of √(f⁻¹g). The Hassan–Rosen eₙ are those of √(g⁻¹f), and for that matrix p₄ is Tr(g⁻²). Flag 14 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md) records the difference as a minor point of notation, with an executed check that prints both identities ([`review/wiki-build-checks/sqrt_eig_check.out`](../../../review/wiki-build-checks/sqrt_eig_check.out)), and finds that the conclusion stands (battery T7). The flags' audit rated it as depending on a convention: #7 fixes neither the square root nor the measure, and with a fixed measure the exchange identity of calc note [#8 §1](../../../notes/beta-coefficients.md#1-what-reciprocity-does-to-the-wedge-potential-d) makes the √(f⁻¹g) presentation equivalent. On the wiki's reading, the slice's Tr(S²) = Tr(g²) + Tr(g⁻²) − 2d contains both traces, so it contains p₄ of the eigenvalues of √(g⁻¹f), the numbers whose eₙ the Hassan–Rosen potential uses.

The argument does not use the linearized check, which is why #7 counts it as a second, independent failure.

### The machine check: battery test T7

Test T7 checks the algebraic fact on numbers. It draws 300 random sets of four eigenvalues, each uniform between 0.5 and 2.0 (a separate generator, seeded with 1), computes e₀ to e₄ and p₄ for each set, and fits p₄ by least squares as a linear combination of e₀ to e₄. If p₄ were in their span, the residual would vanish up to rounding. The current gate run prints:

```text
PASS  T7 p4 outside span of e_n (rms residual nonzero)  [rms=3.2853]
PASS  T7 parity: rms 3.29 as quoted  [rms=3.2853]
```

The first check passes when the rms residual exceeds `1e-6`; the second confirms the figure the documents quote, "rms residual 3.29" ([#11 §2](../../papers/broken-born-checkpoint-v2.md#2-methodological-preface-provenance-and-verification)) and "lstsq rms ≈ 3.29" ([`HANDOFF.md` §5](../../../HANDOFF.md#5-verification-protocol-the-method--keep-using-it)).

**What T7 does and does not show.** [#11 §7.2](../../papers/broken-born-checkpoint-v2.md#72-the-tuning-test-dv) says the nonlinear structure Tr(g²) + Tr(g⁻²) is "provably outside the linear-in-eₙ span (T7)". T7 tests p₄ alone, numerically, on random positive numbers that are not tied to any metric. The [V] covers the fact that p₄ is outside the span; the statement about Tr(g²) + Tr(g⁻²) rests on the derivation [D] ([conflicts between the documents](../../history/documents/source-conflicts.md)).

## The verdict on the metric tier

The two failures are independent: one is in the quadratic mass, the other in the nonlinear structure, and either one brings back the Boulware–Deser ghost. [#7 §2](../../../notes/tuning-test.md#2-explicit-computation-metric-tier-d--rigorous) concludes that "the naive implementation of η-selection has the Boulware–Deser ghost", and its §5 records that "the failure mode is exhibited explicitly (metric tier)".

Before the test, calc note #6 had set out what a failure would mean: "Fail ⇒ the Boulware–Deser ghost kills the geometric sector" ([#6 §5](../../../notes/x-classification.md#5-the-field-equation-problem-after-this-chunk)). The metric-tier negative was not the outcome of the whole test, because [#7 §3](../../../notes/tuning-test.md#3-the-frame-tier-d--structural-resting-on-t) found a different formulation in which the potential passes: "The rescue is not a tuning but a *tier change*" ([the frame tier](frame-tier.md); [the verdict: a conditional pass](conditional-pass.md)).

## Scope and caveats

- **"Every … invariant tested."** #7 names two invariants, Tr({J, I}²) and the one built from [J, I] + 2K, and states its conclusion for "Every metric-tier (second-order, H-coupled) misalignment invariant tested".
- **Euclidean skeleton.** The computation is done "in the vacuum frame (g₀ = 1), Euclidean skeleton" ([#7 §2](../../../notes/tuning-test.md#2-explicit-computation-metric-tier-d--rigorous)), with a positive-definite metric. Extending the program's Euclidean results to the Lorentzian signature of spacetime is open problem 3 ([Open: Lorentzian dressing (OP3)](../../phase-space/born-geometry/lorentzian-dressing.md)).
- **What the battery covers.** T4 checks the first invariant's mass for h at one random point; T7 checks that p₄ lies outside the span of the eₙ. The second invariant has no test. The parity checks reproduce the documents' own figures, so they confirm the arithmetic in this environment and are not independent anchors ([independent anchors](../../method/verification/independent-anchors.md); [verification confirms arithmetic, not the model](../../method/verification/arithmetic-not-model.md)).

## How the record describes it

- **The lab notebook**, v0.5 addendum: metric-tier Higgs potentials "produce m²Tr(h²) with no −(Tr h)² companion (non-Fierz–Pauli at linear order) and Tr(g±²)-type nonlinear structure outside the Hassan–Rosen span; Boulware–Deser ghost, exhibited twice independently" ([the lab notebook](../../history/documents/lab-notebook.md)).
- **The v1 program paper** ([#9 §5 item 4](../../../notes/broken-born-program-v1.md#5-the-second-graviton-and-its-mass-the-field-equation-problem-solved), superseded by #11; [the checkpoint](../../history/documents/checkpoint.md)): metric-tier implementations "fail twice over", with Tr(g²) + Tr(g⁻²) "provably outside the linear-in-eₙ Hassan–Rosen span", under the tag "[D — both branches computed]".
- **[#11 §2](../../papers/broken-born-checkpoint-v2.md#2-methodological-preface-provenance-and-verification)** lists both among the seven Tier-1 tests of its battery and records "All seven passed [V]" ([claim tiers and selection bias](../../method/claim-tiers.md)).
- **The handoff** marks both failures with its machine-check sign: "Metric-tier Higgs potentials fail Fierz–Pauli (m²Tr h², no −(Tr h)² ✓; Tr(g²)+Tr(g⁻²) outside HR span ✓)" ([`HANDOFF.md` §2](../../../HANDOFF.md#2-scientific-state-one-screen)), HR being Hassan–Rosen. Its Appendix A gives the battery's code and the expected output, "T4 converges to 4Tr(h²) and visibly ≠ FP; … T7 rms ≈ 3.3" ([the handoff](../../history/documents/handoff.md)).
- **The popular article [#10](../../../popsci/angle-of-the-mirror.md)** counts the numerical signature of a ghost that the argument required among the battery's seven checks, all of which passed, without naming the test ([the popular articles](../../history/documents/popular-articles.md)).

## Sources

- [`notes/tuning-test.md` §2](../../../notes/tuning-test.md#2-explicit-computation-metric-tier-d--rigorous) — both failures and the second invariant [D — rigorous], and the verdict on the metric tier; [§3](../../../notes/tuning-test.md#3-the-frame-tier-d--structural-resting-on-t) — "a *tier change*" and the order of the tiers; [§5](../../../notes/tuning-test.md#5-status-of-the-field-equation-problem) — "the failure mode is exhibited explicitly".
- [`wiki/papers/broken-born-checkpoint-v2.md` §7.2](../../papers/broken-born-checkpoint-v2.md#72-the-tuning-test-dv) — the current statement [D][V], "the 66.58-vs-63.72 test of §2" and "provably outside"; [§2](../../papers/broken-born-checkpoint-v2.md#2-methodological-preface-provenance-and-verification) — the Tier-1 descriptions of T4 and T7 and "rms residual 3.29"; [§5](../../papers/broken-born-checkpoint-v2.md#5-the-kinematic-core-and-the-compatibility-theorem), [§6](../../papers/broken-born-checkpoint-v2.md#6-the-modular-field) — K = η⁻¹ω; Y = Im Z = g.
- [`verify/battery.py`](../../../verify/battery.py) T4, T7 — the machine checks, their thresholds and their parity checks against the quoted figures.
- [`HANDOFF.md` §5](../../../HANDOFF.md#5-verification-protocol-the-method--keep-using-it) — the battery summary, "66.58 vs 63.72 at seed 0" and "lstsq rms ≈ 3.29"; [§2](../../../HANDOFF.md#2-scientific-state-one-screen) — the failures with check marks; [Appendix A](../../../HANDOFF.md#appendix-a--machine-verification-battery-re-run-first) — the battery code and expected output.
- [`notes/x-classification.md` §3](../../../notes/x-classification.md#3-the-mass-mechanism-and-the-endpoint-d--structural), [§5](../../../notes/x-classification.md#5-the-field-equation-problem-after-this-chunk) — five polarizations; what a failure would mean.
- [`notes/broken-born-theory.md`](../../../notes/broken-born-theory.md) 'Addendum (v0.5)' — the notebook's account.
- [`notes/broken-born-program-v1.md` §5](../../../notes/broken-born-program-v1.md#5-the-second-graviton-and-its-mass-the-field-equation-problem-solved) — the v1 statement.
- [`popsci/angle-of-the-mirror.md`](../../../popsci/angle-of-the-mirror.md) 'The method is the message' — the popular description of the battery.
- [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md) item 4 — the suspected slip in #7's expansion of S; item 14 — which square root's eigenvalues give Tr(g²); item 36 — where the figures 66.58 and 63.72 are printed. All pending.
- [`review/wiki-build-checks/sqrt_eig_check.py`](../../../review/wiki-build-checks/sqrt_eig_check.py) and [`review/wiki-build-checks/sqrt_eig_check.out`](../../../review/wiki-build-checks/sqrt_eig_check.out) — p₄ of the eigenvalues of √(g⁻¹f) and of √(f⁻¹g) against Tr(g⁻²) and Tr(g²) in the vacuum frame.
