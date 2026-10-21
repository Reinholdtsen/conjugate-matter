---
title: "The Fierz–Pauli mass term and the Boulware–Deser ghost"
weight: 20
status: established
description: "The unique healthy linear mass term for spin-2, the ghost that generic nonlinear completions revive, and why no ungauged symmetric tensor has a ghost-free kinetic term (the signature obstruction)."
provenance: [T]
sources:
  - "papers/broken-born-checkpoint-v2.md §7.1"
  - "papers/broken-born-checkpoint-v2.md §7.2"
  - "verify/battery.py T4"
  - "HANDOFF.md §5"
  - "notes/debt1a-ii-X-classification.md §2"
  - "notes/debt1a-ii-X-classification.md §3"
  - "notes/debt1a-iii-tuning-test.md §2"
  - "notes/debt1a-iii-tuning-test.md §3"
  - "notes/debt1a-iii-tuning-test.md §5"
  - "notes/debt1a-iv-beta-coefficients.md §3"
---

*The Fierz–Pauli mass term is the only mass term that gives a free spin-2 field a mass at quadratic order without a ghost, a mode whose energy has the wrong sign: in matrix notation it is proportional to Tr(h²) − (Tr h)², where h is the field. When the theory is made nonlinear, a generic completion brings a ghost back, the Boulware–Deser ghost, and avoiding it takes the special dRGT and Hassan–Rosen potentials. A related standard fact, the signature obstruction, says that a symmetric tensor without gauge symmetry has no ghost-free kinetic term at all. The program uses all three facts to decide what its second field, the [momentum graviton X](/wiki/gravity/momentum-graviton), can be, and its [tuning test](/wiki/gravity/tuning-test) checks X's mass term against the Fierz–Pauli form.*

**Status:** Established — [T] — textbook massive-gravity theory, with the signature obstruction tagged "[T — standard]" in [#6](/wiki/history/documents/debt-1-notes) §2. The program's comparison of its own mass term with the Fierz–Pauli form is machine-checked as battery test T4 [V] (see [the verification battery](/wiki/method/verification/battery)).

## Key facts

- The Fierz–Pauli combination, Tr(h²) − (Tr h)², is the healthy linear mass term for a spin-2 field h [T]. Battery T4 compares against the same structure, written 4(Tr(h²) − (Tr h)²) in `verify/battery.py`.
- "Massive spin-2 coupled to gravity has exactly one known consistent structure: the Fierz–Pauli tuning at quadratic order completed by a dRGT/Hassan–Rosen-class potential" [T: HR 2011], and "a generic potential reintroduces the Boulware–Deser ghost" (#6 §3); see [dRGT massive gravity](/wiki/gravity/spin-2-fields/drgt-massive-gravity) and [Hassan–Rosen bimetric gravity](/wiki/gravity/spin-2-fields/hassan-rosen-bimetric).
- The signature obstruction [T — standard] (#6 §2): "Without the gauge invariance, no ghost-free two-derivative kinetic term for a Lorentz-covariant symmetric tensor exists (mixed time–space components enter with the wrong sign under any invariant contraction; this is why the Fierz–Pauli structure and its accidental gauge symmetry exist at all)." The [checkpoint](/wiki/history/documents/checkpoint) uses it to exclude an ungauged X (#11 §7.1); see [why X must be massive](/wiki/gravity/momentum-graviton/forcing-chain).
- The program's misalignment potentials built from metrics fail this test (#7 §2, [D — rigorous]): any potential of the class Tr({J, I}²) gives "m²Tr(h²) — a graviton mass **without** the −(Tr h)² companion. That violates Fierz–Pauli already at linear order: Boulware–Deser ghost, immediately." See [the metric tier fails twice](/wiki/gravity/tuning-test/metric-tier-failures).
- Battery T4 [V], as printed by `verify/battery.py` at seed 0: Tr(S²)/ε² → 4Tr(h²) = 66.5770, against the Fierz–Pauli form 63.7221. Here S is the diagonal block of the [misalignment measure](/wiki/gravity/tuning-test/misalignment-potential) {J₀, I[Z]}, evaluated at Y = 1 + εh and X = εx for small ε. The checkpoint quotes this as "the 66.58-vs-63.72 test" (#11 §7.2); the figures belong to one seeded random h ("66.58 vs 63.72 at seed 0", HANDOFF §5).
- In frame variables the Fierz–Pauli structure is "automatic" (#7 §3); see [the vielbein formulation](/wiki/gravity/spin-2-fields/vielbein-formulation) and [the frame tier](/wiki/gravity/tuning-test/frame-tier).
- After the palindrome, X's mass is the Fierz–Pauli combination m_FP² ∝ β₁ + 2β₂ + β₃ = 2(β₁+β₂) (#8 §3, [D + T]); no battery test covers it. See [spectrum, parameters and reciprocity parity](/wiki/gravity/momentum-graviton/spectrum-and-parity).

## Used by

- [Why X must be massive](/wiki/gravity/momentum-graviton/forcing-chain) — the signature obstruction excludes an ungauged X.
- [The metric tier fails twice](/wiki/gravity/tuning-test/metric-tier-failures) — the missing Fierz–Pauli trace term (T4).
- [The frame tier: the symplectic vielbein](/wiki/gravity/tuning-test/frame-tier) — the Fierz–Pauli structure comes out automatically.
- [Spectrum, parameters and reciprocity parity](/wiki/gravity/momentum-graviton/spectrum-and-parity) — M_X as the Fierz–Pauli mass combination.

## Sources

- `papers/broken-born-checkpoint-v2.md` §7.1, §7.2 — the exclusion of an ungauged X; the metric-tier failure and the "66.58-vs-63.72" test (which §7.2 attributes to §2, where the numbers do not appear).
- `verify/battery.py` T4 — the printed comparison, 66.5770 against 63.7221.
- `HANDOFF.md` §5 — the test's description, "at seed 0".
- `notes/debt1a-ii-X-classification.md` §2, §3 — the signature obstruction; the one known consistent structure and the Boulware–Deser criterion.
- `notes/debt1a-iii-tuning-test.md` §2, §3, §5 — the missing trace term; Fierz–Pauli automatic in frame variables; the name "signature obstruction".
- `notes/debt1a-iv-beta-coefficients.md` §3 — the Fierz–Pauli mass combination after the palindrome.
