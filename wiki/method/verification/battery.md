---
title: "The verification battery T1–T7"
weight: 70
status: method
description: "Seven seeded tests of the Tier-1 algebra: the compatibility theorem, the Siegel parametrization, the anticommutator blocks, the non-Fierz–Pauli mass, the palindrome identity, the eₙ coefficients and the span test."
provenance: [V]
sources:
  - "verify/battery.py"
  - "HANDOFF.md §5"
  - "HANDOFF.md 'Appendix A'"
  - "papers/broken-born-checkpoint-v2.md §2"
  - "papers/broken-born-checkpoint-v2.md §5"
  - "papers/broken-born-checkpoint-v2.md §6"
  - "papers/broken-born-checkpoint-v2.md §7.2"
  - "papers/broken-born-checkpoint-v2.md §7.3"
---

*The verification battery is a set of seven numerical and exact-integer tests, T1 to T7, of the matrix algebra at the core of the program: the compatibility theorem, the parametrization of the modular field, and the algebra behind the mass of the momentum graviton and the zero vacuum energy of its potential. It was written and run on claude.ai, carried into the repository as Appendix A of the handoff document, and now runs unchanged, with the same random seed, as `verify/battery.py` in the gate. Checkpoint #11 counts the results it confirms as its Tier 1 and tags them [V]. Most tests evaluate an identity on one randomly drawn matrix, so they confirm the algebra numerically rather than prove it, and none of them tests whether the algebra describes nature.*

**Status:** Method — the results carry [V] in #11 §2 ("All seven passed [V]") — runs in [the gate](/wiki/method/verification/the-gate); the last recorded run passed every check and ended "OK — all battery checks pass (numpy 2.5.4)."

## Key facts

- **Setup.** "the machine-verification battery from HANDOFF.md Appendix A. Seven tests (T1–T7) of the program's Tier-1 algebra." Dimension d = 4, ω = [[0, I], [−I, 0]] and η = [[0, I], [I, 0]] in d × d blocks, `np.random.seed(0)`. The docstring states that the computations, seeds and order of random draws are Appendix A's, unchanged, "so the printed figures are the ones quoted" in the papers. `HANDOFF.md` §5: "Code in Appendix A — re-run it first to confirm environment parity."
- **T1, [the compatibility theorem](/wiki/phase-space/born-geometry/compatibility-theorem)** [T][V]: `T1a diag(g,g^-1) satisfies (eta^-1 H)^2=1 and (omega^-1 H)^2=-1`; `T1b generic H violates at least one condition`; and the proof's block identities, `T1c proof block (J^2)_21 = A C^T + C A` and `T1c proof block (I^2)_21 = C A - A C^T`. #11 §5: "(Both directions and the individual block identities machine-checked.)"
- **T2, the Siegel parametrization** of [the modular field Z](/wiki/phase-space/modular-field/modular-field-z) on [the Siegel domain](/wiki/phase-space/modular-field/siegel-domain): `T2 I[Z]^2 = -1`, `T2 H_Z symmetric`, `T2 det H_Z = 1  [det=1.000000000000]`, `T2 H_Z positive definite`. #11 §2 states "I[Z]² = −1, H > 0, det H = 1 across the whole family"; the test draws one member of the family.
- **T3 and T4, the graviton-mass algebra.** T3 checks the anticommutator blocks of [the misalignment potential](/wiki/gravity/tuning-test/misalignment-potential): `T3 {J0,I[Z]} = [[S,A],[A,S]]`, with "S = Y + XY⁻¹X − Y⁻¹, A = [X, Y⁻¹] (blocks machine-verified)" (#11 §7.2). T4 checks the non-Fierz–Pauli mass ([the metric tier fails twice](/wiki/gravity/tuning-test/metric-tier-failures)): the run prints `T4 eps=1e-05: 66.5770 vs 4Tr(h^2)=66.5770 vs FP=63.7221` and passes `T4 Tr(S^2)/eps^2 -> 4Tr(h^2) (rel 1e-5 at eps=1e-5)` and `T4 limit differs from Fierz-Pauli form (rel > 1%)`. #11 §7.2: a "quadratic mass m²Tr(h²) with no −(Tr h)²", not of the [Fierz–Pauli](/wiki/gravity/spin-2-fields/fierz-pauli) form.
- **T5 and T6, the vacuum-energy algebra.** T5 checks the palindrome identity of [the vacuum-energy identity](/wiki/gravity/palindromic-branch/vacuum-energy-identity): `T5 V(1) - 2T = [0,0,0]  [V1=[2, 8, 6] T=[1, 4, 3]]`, computed in exact integers; #11 §7.3 [D][V]: "V(1) = 2T exactly (integer identity: [2,8,6] = 2·[1,4,3])". See also [the palindrome βₙ = β₄₋ₙ](/wiki/gravity/palindromic-branch/palindrome). T6 checks the linear coefficients of the [elementary symmetric polynomials](/wiki/gravity/spin-2-fields/elementary-symmetric-polynomials): `T6 e_n(1+delta) linear coefficients = C(3,n-1) = [0,1,3,3,1]  [[0.0, 1.0, 3.0, 3.0, 1.0]]`.
- **T7, the span test**: `T7 p4 outside span of e_n (rms residual nonzero)  [rms=3.2853]`, a least-squares fit over 300 random samples (Appendix A). #11 §7.2 says "Tr(g²) + Tr(g⁻²) provably outside the linear-in-eₙ span (T7)"; the test checks the power sum p₄ numerically, which is how `HANDOFF.md` §5 describes it ("p₄ outside linear span of eₙ (lstsq rms ≈ 3.29)").
- **Parity checks.** `T4 parity: 66.58 vs 63.72 as quoted` and `T7 parity: rms 3.29 as quoted` confirm that this environment still reproduces the figures the papers print: "a parity failure means this environment no longer reproduces the numbers the papers cite." They are reproductions, not [independent anchors](/wiki/method/verification/independent-anchors). The docstring places both figures in #11 §2, but §2 gives only "rms residual 3.29"; "66.58 vs 63.72 at seed 0" is in `HANDOFF.md` §5, and #11 §7.2 refers to "the 66.58-vs-63.72 test of §2".
- **What it does not show.** "a verification script confirms arithmetic, not the model it encodes" (#11 §2). See [Verification checks arithmetic, not the model](/wiki/method/verification/arithmetic-not-model) and [Claim tiers and selection bias](/wiki/method/claim-tiers).

## Sources

- `verify/battery.py` — the tests, the check names, the parity checks
- `HANDOFF.md` §5 and 'Appendix A' — the battery as handed over, its expected outputs, "re-run it first"
- `papers/broken-born-checkpoint-v2.md` §2 — Tier 1 and "All seven passed [V]"; §5, §6, §7.2, §7.3 — the claims the tests confirm
