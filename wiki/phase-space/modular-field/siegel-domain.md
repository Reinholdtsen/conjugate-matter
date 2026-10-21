---
title: "The Siegel domain Sp(2d, ℝ)/U(d)"
weight: 10
status: established
description: "Symmetric complex matrices Z with positive imaginary part, acted on by fractional-linear (Möbius) maps; the standard H_Z parametrization and battery test T2."
provenance: [D, V]
sources:
  - "notes/debt1a-geometric-core.md §C"
  - "notes/debt1a-iii-tuning-test.md §2"
  - "verify/battery.py T2"
  - "HANDOFF.md §5"
  - "notes/debt1a-geometric-core.md §D"
  - "notes/debt1a-ii-X-classification.md §1"
  - "notes/debt1a-ii-X-classification.md §3"
  - "papers/broken-born-checkpoint-v2.md §6"
  - "papers/reciprocity-toy-models.md §2"
  - "review/round3/referee/audit-notes.md Step 3"
---

*The Siegel domain is the space of symmetric complex matrices Z = X + iY whose imaginary part Y is positive definite; for a single coordinate (d = 1) it is the upper half of the complex plane. It is also the space of all positive phase-space metrics compatible with a fixed [symplectic form](/wiki/phase-space/reciprocity/symplectic-form): each point Z names one such metric H_Z, and the symplectic group acts on the points by fractional-linear (Möbius) maps. The program uses it as the arena of [the modular field](/wiki/phase-space/modular-field/modular-field-z) once only the symplectic form is held rigid. The space and its parametrization are standard mathematics, and their algebraic identities pass a machine check.*

**Status:** Established — standard mathematics (#5 §C: "[D — structural; math facts standard]"); the parametrization identities are machine-checked [V] (battery test T2, at one sampled point; [the battery](/wiki/method/verification/battery)).

## Key facts

- **The parametrization.** #5 §C: "positive H compatible with ω alone form the **Siegel domain** Sp(2d,ℝ)/U(d), coordinatized by a complex symmetric matrix"

  ```text
  Z = X + iY,   Y > 0

  H_Z = [[ Y + XY⁻¹X ,  XY⁻¹ ],
         [ Y⁻¹X      ,  Y⁻¹  ]]
  ```

- **Its complex structure.** #7 §2 uses "the verified Siegel parametrization" of I = ω⁻¹H_Z:

  ```text
  I[Z] = [[ −Y⁻¹X     ,  −Y⁻¹  ],
          [ Y + XY⁻¹X ,  XY⁻¹  ]]
  ```

- **Battery test T2.** At d = 4, for one random symmetric X and positive-definite Y, the gate prints `PASS  T2 I[Z]^2 = -1`, `PASS  T2 H_Z symmetric`, `PASS  T2 det H_Z = 1  [det=1.000000000000]` and `PASS  T2 H_Z positive definite`. The handoff describes T2 as "(I[Z]² = −1, H ≻ 0, det H = 1 off-vacuum)" (`HANDOFF.md` §5). Round 3 found the same family compatible with ω but not with η when X ≠ 0: `omega residual <= 3e-14 but eta residual >= 0.52 (d=3), 1.87 (d=4)` (audit notes, Step 3).
- **Möbius maps.** "The Möbius action of the rigid Sp(2d,ℝ) contains the subgroup [[1, B], [0, 1]], B symmetric, acting as Z → Z + B" (#6 §1; [shift symmetry](/wiki/gravity/momentum-graviton/shift-symmetry)). Reciprocity acts as Z → −Z⁻¹ (#11 §6; [modular inversion](/wiki/phase-space/modular-field/modular-inversion)).
- **The target metric.** #5 §D: "the Siegel target metric Tr(Y⁻¹dZ Y⁻¹dZ̄) is positive-definite", one of the good signs for a healthy kinetic term. With Lorentzian g the invariant target metric becomes indefinite (#6 §3) — see [Lorentzian dressing](/wiki/phase-space/born-geometry/lorentzian-dressing).
- **d = 1 and the boundary.** In the coset toy model H(Z) = [[Y + X²/Y, X/Y], [X/Y, 1/Y]] for Z = X + iY in the upper half-plane (toy-model note §2; [model I: action and symmetries](/wiki/symmetry-breaking/toy-models/coset-model/action-and-symmetries)). The domain's Shilov boundary is [the Lagrangian Grassmannian](/wiki/phase-space/modular-field/lagrangian-grassmannian) [T] (#11 §6).

## Used by

- [The modular field Z = X + iY](/wiki/phase-space/modular-field/modular-field-z) — the program's field lives on this space.
- [Reciprocity as modular inversion Z → −Z⁻¹](/wiki/phase-space/modular-field/modular-inversion) — ρ as a Möbius map.
- [Shift symmetry: X is never auxiliary](/wiki/gravity/momentum-graviton/shift-symmetry) — the Möbius subgroup Z → Z + B.
- [The misalignment potential](/wiki/gravity/tuning-test/misalignment-potential) — built from I[Z].
- [Model I: action and symmetries](/wiki/symmetry-breaking/toy-models/coset-model/action-and-symmetries) — the d = 1 domain as the toy's H-sector.

## Sources

- `notes/debt1a-geometric-core.md` §C — the Siegel domain of ω-compatible metrics and H_Z.
- `notes/debt1a-geometric-core.md` §D — the positive target metric.
- `notes/debt1a-iii-tuning-test.md` §2 — I[Z] in the verified parametrization.
- `verify/battery.py` T2 — the parametrization identities at one sampled point.
- `HANDOFF.md` §5 — T2 described as an off-vacuum check.
- `notes/debt1a-ii-X-classification.md` §1, §3 — the Möbius subgroup Z → Z + B; the Lorentzian target metric.
- `papers/broken-born-checkpoint-v2.md` §6 — the modular field, ρ as Z → −Z⁻¹, the Shilov boundary.
- `papers/reciprocity-toy-models.md` §2 — the d = 1 case in model I.
- `review/round3/referee/audit-notes.md` Step 3 — the ω-only family checked numerically.
