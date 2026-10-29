---
title: "The verification battery T1–T7"
weight: 70
status: method
description: "verify/battery.py: seven tests of #11's Tier-1 algebra (compatibility theorem, Siegel parametrization, anticommutator blocks, non-Fierz–Pauli mass, palindrome identity, eₙ coefficients, span test), mostly on one random draw each, plus two parity checks."
provenance: [V]
sources:
  - "verify/battery.py"
  - "HANDOFF.md 'Appendix A'"
  - "HANDOFF.md §5"
  - "papers/broken-born-checkpoint-v2.md §2"
  - "papers/broken-born-checkpoint-v2.md §5"
  - "papers/broken-born-checkpoint-v2.md §6"
  - "papers/broken-born-checkpoint-v2.md §7.2"
  - "papers/broken-born-checkpoint-v2.md §7.3"
  - "review/round3-adjudication.md 'Rulings'"
  - "review/wiki-build-flags.md items 3, 4, 14, 36"
---

*The verification battery is a set of seven numerical and exact-integer tests, T1 to T7, of the matrix algebra at the core of the program: the compatibility theorem, the parametrization of the modular field, and the algebra behind the mass of the [momentum graviton](/wiki/gravity/momentum-graviton) and the zero vacuum energy of its potential. It was written and run on claude.ai, carried into the repository as Appendix A of the handoff document, and now runs as `verify/battery.py` in the gate, with the same computations and random seeds. Checkpoint #11 calls the results it confirms Tier 1 and tags them [V]. Six of the tests evaluate an identity at randomly drawn sample points and one is exact integer arithmetic, so the battery confirms the algebra at sample points rather than proving it, and none of the tests asks whether the algebra describes nature.*

**Status:** Method, in force — the results it confirms carry [V] in #11 §2 ("All seven passed **[V]**") — runs first in [the gate](/wiki/method/verification/the-gate); in the run of 2026-10-21 every check passed and the script ended "OK — all battery checks pass (numpy 2.5.4)."

## What it is

The script's docstring describes it as "the machine-verification battery from HANDOFF.md Appendix A. Seven tests (T1–T7) of the program's Tier-1 algebra. Every verdict is a boolean or a number against a tolerance, never a judgement." [Checkpoint #11](/wiki/history/documents/checkpoint) §2 places these results in Tier 1, "explicit algebra", the most trusted of its [claim tiers](/wiki/method/claim-tiers), and the [V] tag they carry is defined on [Provenance tags and citation marks](/wiki/method/provenance-tags).

### From Appendix A to the gate

The [handoff](/wiki/history/documents/handoff) carried the battery as a code listing that printed booleans and numbers, followed by the expected result: "Expected: T1–T3 all True; T4 converges to 4Tr(h²) and visibly ≠ FP; T5 = [0,0,0]; T6 = [0,1,3,3,1]; T7 rms ≈ 3.3." (`HANDOFF.md`, Appendix A; FP is Fierz–Pauli). Its instruction was "Code in Appendix A — re-run it first to confirm environment parity" (§5). `verify/battery.py` keeps the computations and turns each printed expectation into a check with a stated tolerance. Its docstring says that the computations, the seeds and the order of the random draws are Appendix A's, unchanged, "so the printed figures are the ones quoted". It adds two parity checks on the figures the documents quote (see [Parity checks](#parity-checks)).

### Setup

The tests work in dimension d = 4, with the [symplectic form](/wiki/phase-space/reciprocity/symplectic-form) ω = [[0, 1], [−1, 0]] and the [neutral metric](/wiki/phase-space/born-geometry/born-structures) η = [[0, 1], [1, 0]], where 0 and 1 stand for the d × d zero and identity blocks. T1, T2, T4 and T6 draw their random matrices from numpy's legacy generator after `np.random.seed(0)` (T3 reuses T2's draw, and T5 draws nothing); T7 uses a separate generator, `np.random.default_rng(1)`. Two helpers draw the matrices: a random symmetric matrix, and a random positive-definite one built as a aᵀ plus d times the identity. Because the order of the draws is fixed, every run in the same environment draws the same matrices, which is what makes the quoted figures reproducible.

Each test calls a helper `check(name, ok, detail)` that prints `PASS` or `FAIL`, the check's name and, where given, a measured value in brackets. The script exits with status 1 if any check fails ([the check line](/wiki/method/verification/the-gate#the-check-line)).

## The tests

### T1: the compatibility theorem

[The compatibility theorem](/wiki/phase-space/born-geometry/compatibility-theorem) says that a positive [generalized metric](/wiki/phase-space/born-geometry/double-field-theory) H satisfies both (η⁻¹H)² = 1 and (ω⁻¹H)² = −1 exactly when H = diag(g, g⁻¹) (#11 §5, tagged [T][V]). T1 has three parts:

- **T1a** draws a random positive-definite g, forms H = diag(g, g⁻¹), and checks that J = η⁻¹H squares to the identity and I = ω⁻¹H squares to minus the identity. This is the "if" direction at one point.
- **T1b** draws a generic H = [[A, C], [Cᵀ, B]], with A and B positive definite and C a random block scaled by 0.3, and checks that it violates at least one of the two conditions.
- **T1c** checks, for that generic H, the block identities on which the proof's "only if" direction rests: the (2,1) block of J² equals A Cᵀ + C A, and that of I² equals C A − A Cᵀ. #11 §5's proof sets both to zero and concludes C = 0.

#11 §5: "(Both directions and the individual block identities machine-checked.)" What the gate checks is one random g for the first direction, one random counterexample for the second, and the block identities on that counterexample; the theorem itself is the literature result plus the block proof. The round-3 review also re-derived it "(sympy, including a Groebner basis at d = 2; random tests at d = 3, 4)" (`review/round3-adjudication.md`); those checks are the review's and are not part of the gate.

### T2: the Siegel parametrization

T2 draws a random symmetric X and a random positive-definite Y, builds the generalized metric of [the modular field Z](/wiki/phase-space/modular-field/modular-field-z) = X + iY on [the Siegel domain](/wiki/phase-space/modular-field/siegel-domain),

```text
H_Z = [[Y + X Y⁻¹ X,  X Y⁻¹],
       [Y⁻¹ X,        Y⁻¹  ]],        I[Z] = ω⁻¹ H_Z
```

and checks four properties: I[Z]² = −1, H_Z symmetric, det H_Z = 1 (the value is printed) and H_Z positive definite. #11 §2 states "I[Z]² = −1, H > 0, det H = 1 across the whole family", and §5 says det H = 1 "machine-verified — persists across the whole modular family of §6". The test draws one member of the family off the vacuum slice X = 0.

### T3: the anticommutator blocks

T3 checks the block form of the anticommutator on which [the misalignment potential](/wiki/gravity/tuning-test/misalignment-potential) is built. With the same X and Y as T2 it computes ηI[Z] + I[Z]η and compares its four blocks with

```text
S = Y + X Y⁻¹ X − Y⁻¹,        A = X Y⁻¹ − Y⁻¹ X = [X, Y⁻¹]
```

#11 §7.2: "S = Y + XY⁻¹X − Y⁻¹, A = [X, Y⁻¹] (blocks machine-verified)". T3 checks the block form only. A statement in [calc note #7](/wiki/history/documents/field-equation-notes) about where those blocks vanish is a suspected source error, and its executed check prints a vanishing anticommutator at a point with X ≠ 0 (see flag 3 in `review/wiki-build-flags.md`; `review/wiki-build-checks/zero_locus.out`). T3 neither supports nor contradicts that statement, because it evaluates the blocks at one random point.

### T4: the linearized potential is not of Fierz–Pauli form

T4 tests the first of [the metric tier's two failures](/wiki/gravity/tuning-test/metric-tier-failures). It draws random symmetric h and x, sets Y = 1 + εh and X = εx, forms S from them, and compares Tr(S²)/ε² with two candidate limits: 4Tr(h²), and the [Fierz–Pauli](/wiki/gravity/spin-2-fields/fierz-pauli) combination 4(Tr(h²) − (Tr h)²). The Fierz–Pauli mass term needs the trace term −(Tr h)² to avoid a [ghost](/wiki/gravity/spin-2-fields/ghosts) [T]; a limit of 4Tr(h²) lacks it. The run prints, at ε = 10⁻⁴ and 10⁻⁵:

```text
      T4 eps=0.0001: 66.5772 vs 4Tr(h^2)=66.5770 vs FP=63.7221
      T4 eps=1e-05: 66.5770 vs 4Tr(h^2)=66.5770 vs FP=63.7221
```

The checks pass when, at ε = 10⁻⁵, the value agrees with 4Tr(h²) to a relative tolerance of 10⁻⁵, and when it differs from the Fierz–Pauli value by more than 1%. #11 §2 describes this as "Tr(S²)/ε² → 4Tr(h²) to six digits, visibly ≠ the Fierz–Pauli form", and §7.2 as a "quadratic mass m²Tr(h²) with no −(Tr h)²". Calc note #7's written expansion of S omits a second-order term −h²; the flag records that T4 is unaffected, since at quadratic order it uses only the linear term (flag 4; `review/wiki-build-checks/s_expansion.out`).

### T5: the palindrome identity in exact integers

T5 checks [the vacuum-energy identity](/wiki/gravity/palindromic-branch/vacuum-energy-identity) V(1) = 2T under [the palindrome βₙ = β₄₋ₙ](/wiki/gravity/palindromic-branch/palindrome). It builds the coefficient vectors over (β₀, β₁, β₂) from binomial coefficients, V(1) as [C(4,0) + C(4,4), C(4,1) + C(4,3), C(4,2)] and T as [C(3,3), C(3,0) + C(3,2), C(3,1)], and checks in exact integers that V(1) − 2T = [0, 0, 0]. #11 §7.3 [D][V]: "V(1) = 2T exactly (integer identity: [2,8,6] = 2·[1,4,3])". The test confirms the integer arithmetic; which binomial coefficients belong to V(1) and to T is the derivation's step, taken from calc note #8.

### T6: the linear coefficients of eₙ

T6 checks the expansion behind T5. It draws a symmetric δ with entries of order 10⁻⁶, takes the eigenvalues of 1 + δ, and computes for n = 0 to 4 the ratio (eₙ − C(4, n))/Tr δ, where eₙ is the n-th [elementary symmetric polynomial](/wiki/gravity/spin-2-fields/elementary-symmetric-polynomials) of the eigenvalues. The check passes when the five ratios match C(3, n − 1) = [0, 1, 3, 3, 1] to an absolute tolerance of 10⁻³.

### T7: p₄ lies outside the span of the eₙ

T7 tests the second metric-tier failure. It draws 300 samples of four numbers, each uniform between 0.5 and 2.0, and fits the power sum p₄ = Σ sᵢ⁴ by least squares as a linear combination of e₀ to e₄. The check passes when the root-mean-square residual exceeds 10⁻⁶; the run prints `rms=3.2853`. A nonzero residual means p₄ is not a linear combination of the eₙ at those samples [T]. #11 §7.2 states the conclusion for the program's invariant: "Tr(g²) + Tr(g⁻²) provably outside the linear-in-eₙ span (T7)". The test checks p₄ numerically, which is how `HANDOFF.md` §5 describes it ("p₄ outside linear span of eₙ (lstsq rms ≈ 3.29)"); the identification of Tr(g²) with p₄ of a set of eigenvalues is calc note #7's step, and flag 14 records a suspected notational slip in it that leaves the conclusion standing (`review/wiki-build-checks/sqrt_eig_check.out`).

## Parity checks

Two checks compare the computed figures with the figures the documents print:

```text
PASS  T4 parity: 66.58 vs 63.72 as quoted  [66.58 vs 63.72]
PASS  T7 parity: rms 3.29 as quoted  [rms=3.2853]
```

The docstring: "a parity failure means this environment no longer reproduces the numbers the papers cite." A parity check detects a change of environment, such as a numpy version that draws different random numbers. It is a reproduction of the documents' own figures, not an [independent anchor](/wiki/method/verification/independent-anchors), and it does not claim to be one. The docstring places both figures in #11 §2, but §2 gives only "rms residual 3.29"; "66.58 vs 63.72 at seed 0" is in `HANDOFF.md` §5, and #11 §7.2 refers to "the 66.58-vs-63.72 test of §2" (flag 36 in `review/wiki-build-flags.md`; recorded on [conflicts between the documents](/wiki/history/documents/source-conflicts#tags-attribution-and-what-the-checks-cover)).

## What the battery does not show

- **Generality.** T1 to T4, T6 and T7 evaluate at random sample points. A pass shows the identity holds there to floating-point tolerance; the general statements rest on the derivations, which the [D] and [T] tags record.
- **The surrounding statements.** Each test checks the algebra written into it. Flags 3, 4 and 14, found during the wiki build, concern statements next to tested algebra (where the blocks vanish, a second-order term, a notation), and the tests that pass beside them do not touch them.
- **The physics.** #11 §2 added in v2.1: "a verification script confirms arithmetic, not the model it encodes". See [Verification checks arithmetic, not the model](/wiki/method/verification/arithmetic-not-model).
- **No anchors.** The battery has no anchor section of the kind the later scripts have. Its tests are identities whose truth does not depend on the papers' numbers, and its two parity checks are reproductions.

## The recorded output

The battery's lines from the run of `scripts/check.sh` on 2026-10-21:

```text
PASS  T1a diag(g,g^-1) satisfies (eta^-1 H)^2=1 and (omega^-1 H)^2=-1
PASS  T1b generic H violates at least one condition
PASS  T1c proof block (J^2)_21 = A C^T + C A
PASS  T1c proof block (I^2)_21 = C A - A C^T
PASS  T2 I[Z]^2 = -1
PASS  T2 H_Z symmetric
PASS  T2 det H_Z = 1  [det=1.000000000000]
PASS  T2 H_Z positive definite
PASS  T3 {J0,I[Z]} = [[S,A],[A,S]]
      T4 eps=0.0001: 66.5772 vs 4Tr(h^2)=66.5770 vs FP=63.7221
      T4 eps=1e-05: 66.5770 vs 4Tr(h^2)=66.5770 vs FP=63.7221
PASS  T4 Tr(S^2)/eps^2 -> 4Tr(h^2) (rel 1e-5 at eps=1e-5)
PASS  T4 limit differs from Fierz-Pauli form (rel > 1%)
PASS  T4 parity: 66.58 vs 63.72 as quoted  [66.58 vs 63.72]
PASS  T5 V(1) - 2T = [0,0,0]  [V1=[2, 8, 6] T=[1, 4, 3]]
PASS  T6 e_n(1+delta) linear coefficients = C(3,n-1) = [0,1,3,3,1]  [[0.0, 1.0, 3.0, 3.0, 1.0]]
PASS  T7 p4 outside span of e_n (rms residual nonzero)  [rms=3.2853]
PASS  T7 parity: rms 3.29 as quoted  [rms=3.2853]

OK — all battery checks pass (numpy 2.5.4).
```

## Sources

- `verify/battery.py` — the docstring, the setup, every check and tolerance quoted above
- `HANDOFF.md` Appendix A — the original listing and its expected output; §5 — the battery summary, "66.58 vs 63.72 at seed 0", "re-run it first"
- `papers/broken-born-checkpoint-v2.md` §2 — Tier 1 and "All seven passed [V]"; §5 — the compatibility theorem and its proof; §6 — I[Z]² = −1; §7.2 — the blocks, the non-Fierz–Pauli mass and the span test; §7.3 — the integer identity
- `review/round3-adjudication.md` 'Rulings' — the review's own re-derivation of the compatibility theorem
- `review/wiki-build-flags.md` items 3, 4, 14, with `review/wiki-build-checks/zero_locus.out`, `s_expansion.out` and `sqrt_eig_check.out` — suspected source errors next to the tested algebra; item 36 — where the parity figures are printed
