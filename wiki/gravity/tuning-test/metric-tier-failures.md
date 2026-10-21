---
title: "The metric tier fails twice"
weight: 20
status: alive
description: "Potentials built from metrics give a mass with no Fierz–Pauli trace term (T4: 66.58 vs 63.72) and a nonlinear structure outside the Hassan–Rosen span (T7: rms 3.29), so the Boulware–Deser ghost returns."
provenance: [D, V]
sources:
  - "notes/debt1a-iii-tuning-test.md §2"
  - "papers/broken-born-checkpoint-v2.md §7.2"
  - "papers/broken-born-checkpoint-v2.md §2"
  - "verify/battery.py T4"
  - "verify/battery.py T7"
  - "HANDOFF.md §5"
---

*The metric tier is the attempt to build the momentum graviton's mass term from metric-level, second-order quantities in the [misalignment potential](/wiki/gravity/tuning-test/misalignment-potential), and it fails the ghost-freedom test in two independent ways. At quadratic order it gives the metric fluctuation h a mass term m²Tr(h²) without the −(Tr h)² term that the [Fierz–Pauli](/wiki/gravity/spin-2-fields/fierz-pauli) form requires; at nonlinear order it produces Tr(g²), which lies outside the family of ghost-free [Hassan–Rosen](/wiki/gravity/spin-2-fields/hassan-rosen-bimetric) potentials. Either failure brings back the Boulware–Deser ghost, an extra mode with negative kinetic energy [T]. The result is a derived negative [D — rigorous], which calc note #7 calls "theorem-grade", and both failures are machine-checked [V] by battery tests T4 and T7.*

**Status:** Alive, as a negative result — [D — rigorous] in calc note #7 (`notes/debt1a-iii-tuning-test.md` §2); [D][V] in [checkpoint #11](/wiki/history/documents/checkpoint) §7.2 — tests T4 and T7 of [the verification battery](/wiki/method/verification/battery) pass. The failure of a second invariant is derived only.

## Key facts

- Failure 1, calc note #7 §2 (see [The Debt-1 calc notes](/wiki/history/documents/debt-1-notes)): "With Y = 1 + h, X = x: S = 2h + x² + O(3), A = [h, x] + O(3). Any potential of the class Tr({J,I}²)-with-positive-norm gives, at quadratic order, m²Tr(h²) — a graviton mass without the −(Tr h)² companion. That violates Fierz–Pauli already at linear order: Boulware–Deser ghost, immediately."
- Test T4 [V] computes Tr(S²)/ε² for a random h (seed 0) and compares it with 4Tr(h²) and with the Fierz–Pauli form, which the script computes as 4(Tr(h²) − (Tr h)²). Its output in the current gate run:

  ```text
  T4 eps=0.0001: 66.5772 vs 4Tr(h^2)=66.5770 vs FP=63.7221
  T4 eps=1e-05: 66.5770 vs 4Tr(h^2)=66.5770 vs FP=63.7221
  PASS  T4 parity: 66.58 vs 63.72 as quoted  [66.58 vs 63.72]
  ```

- Where "66.58 vs 63.72" is quoted: `HANDOFF.md` §5 gives "66.58 vs 63.72 at seed 0". #11 §7.2 refers to "the 66.58-vs-63.72 test of §2", but #11 §2 describes the test ("Tr(S²)/ε² → 4Tr(h²) to six digits, visibly ≠ the Fierz–Pauli form") without printing the two figures.
- Failure 2, #7 §2: "The X = 0 slice gives Tr(S²) = Tr(g²) + Tr(g⁻²) − 2d. The Hassan–Rosen ghost-free family is linear combinations Σβₙeₙ(√(g⁻¹f)) (constants βₙ); Tr(g²) = p₄ of the square-root eigenvalues is a nonlinear polynomial in the eₙ, hence outside the family. Fail again, independently of the linearized check." The eₙ are [elementary symmetric polynomials](/wiki/gravity/spin-2-fields/elementary-symmetric-polynomials).
- Test T7 [V] fits p₄ by least squares as a linear combination of e₀ … e₄ over 300 random samples and finds a nonzero residual: `PASS  T7 p4 outside span of e_n (rms residual nonzero)  [rms=3.2853]`. #11 §2 quotes "rms residual 3.29". Scope: #11 §7.2 says Tr(g²) + Tr(g⁻²) is "provably outside the linear-in-eₙ span (T7)", but T7 tests p₄ numerically; the proof is the derivation [D], and the script checks it on samples.
- A second invariant, #7 §2: "A second natural invariant (built from [J, I] + 2K, which vanishes at the vacuum) was computed the same way: it does give X a quadratic mass — again as Tr(x²) with no trace subtraction. Same disease." No battery test covers it, so it stays [D].
- The verdict on this tier, #7 §2: "Every metric-tier (second-order, H-coupled) misalignment invariant tested lands off the tuning. This half of the test is a theorem-grade negative: the naive implementation of η-selection has the Boulware–Deser ghost." The rescue is [the frame tier](/wiki/gravity/tuning-test/frame-tier), and the combined outcome is [a conditional pass](/wiki/gravity/tuning-test/conditional-pass).

## Sources

- `notes/debt1a-iii-tuning-test.md` §2 — both failures and the second invariant [D — rigorous]
- `papers/broken-born-checkpoint-v2.md` §7.2 — the current statement [D][V]; §2 for the battery's description and "rms residual 3.29"
- `verify/battery.py` T4, T7 — the machine checks and their parity checks against the quoted figures
- `HANDOFF.md` §5 — the battery summary with "66.58 vs 63.72 at seed 0"
