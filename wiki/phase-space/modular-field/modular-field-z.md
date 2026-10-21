---
title: "The modular field Z = X + iY"
weight: 20
status: alive
description: "All the geometry fits one field: Im Z = g is the metric (X = 0 is the vacuum slice, ⟨Z⟩ = i·g) and Re Z = X is the local wobble of the polarization — the momentum graviton."
provenance: [D]
sources:
  - "papers/broken-born-checkpoint-v2.md §6"
  - "notes/debt1a-geometric-core.md §C"
  - "notes/debt1a-geometric-core.md §F"
  - "notes/debt1a-ii-X-classification.md §3"
  - "notes/broken-born-program-v1.md §4"
  - "papers/broken-born-checkpoint-v2.md §7"
  - "notes/broken-born-theory.md 'Addendum (v0.3, overnight): axiom correction and the modular core'"
  - "verify/battery.py T2"
  - "review/round3/referee/audit-notes.md Step 3"
---

*The modular field Z = X + iY is a complex symmetric matrix field that, in the program, carries the whole geometry of phase space at each point of spacetime once only the symplectic form is rigid: each value of Z is a point of [the Siegel domain](/wiki/phase-space/modular-field/siegel-domain) and names one compatible phase-space metric. The program identifies the imaginary part Y with the spacetime metric g, and the real part X with a new symmetric tensor field, the momentum graviton, which records how the split between position and momentum tilts from place to place. In the vacuum X = 0 and Z = i·g. These identifications are the program's derived claims; the algebra of the parametrization is machine-checked, and the field X is shown elsewhere to be forced to have a mass.*

**Status:** Alive — the identifications are derived [D] (#11 §6; #5 §C "[D — structural]") — only the parametrization identity I[Z]² = −1 is machine-checked [V] (battery test T2; [the battery](/wiki/method/verification/battery)).

## Key facts

- **The identifications.** #11 §6: "With only ω rigid, H ranges over Sp(2d,ℝ)/U(d): Z = X + iY (symmetric; Y > 0), H_Z the standard generalized metric (I[Z]² = −1 machine-verified [V]). Identifications [D]: **Im Z = g**; the η-compatible locus X = 0 is the vacuum slice of §5. **Re Z = X**, the momentum graviton — the fluctuation of the emergent polarization."
- **Im Z = g and the vacuum slice.** #5 §C: "At X = 0, H = diag(g, g⁻¹): the η-compatible locus of Theorem A is precisely the vacuum slice" — the solutions of [the compatibility theorem](/wiki/phase-space/born-geometry/compatibility-theorem). #6 §3: "The vacuum ⟨Z⟩ = i·g sits at X = 0".
- **Re Z = X.** #5 §C: X is "a *new symmetric tensor*: the momentum graviton. It is exactly the fluctuation that breaks η-compatibility — i.e., the local wobble of the emergent polarization, 'which way the x/p split points, here.'" Round 3's numerics agree that points with X ≠ 0 are compatible with ω but not with η (audit notes, Step 3).
- **One field for the geometric program [D — structural].** #5 §C: "One object now carries the whole geometric program: **metric (Im Z), momentum geometry and gate mediator (Re Z), scale-factor duality (|Z|), dark energy (boundary phase of Z).**" The pieces are [the gate mechanism](/wiki/dark-matter/conjugate-matter/gate-mechanism), [the cosmological constraint a·ã = 1](/wiki/cosmology/scale-factor-duality/cosmological-constraint) and [τ as the Maslov phase](/wiki/phase-space/modular-field/maslov-phase).
- **Born's debt, restated.** #5 §C: "the field equation for momentum-space geometry is the Re Z sector of S_H." The action S_H of the lab notebook is superseded ([the geometric action S_H](/wiki/gravity/tuning-test/geometric-action)); the program reached X's dynamics through its symmetries and the tuning test instead, and deriving them from S_H is still open ([deriving the wedge sector from S_H](/wiki/gravity/tuning-test/wedge-reduction)).
- **What X became.** The rigid group's shifts Z → Z + B make X "axion-like, never auxiliary"; dual diffeomorphisms make it a second graviton; the multi-graviton no-go excludes a massless X; the polarization choice gives it a mass (#11 §7.1). See [shift symmetry](/wiki/gravity/momentum-graviton/shift-symmetry), [why X must be massive](/wiki/gravity/momentum-graviton/forcing-chain) and [Born's answer](/wiki/gravity/momentum-graviton/borns-answer).
- **History.** Z entered with the P2 → P2′ correction in #1's v0.3 addendum ("a single **modular field** Z = X + iY on the Siegel domain"); #9 §4 restates it. See [P2′](/wiki/program/postulates/p2-prime).

## Sources

- `papers/broken-born-checkpoint-v2.md` §6 — the identifications [D] and the [V] on I[Z]² = −1.
- `papers/broken-born-checkpoint-v2.md` §7 — the chain that makes X a massive spin-2 field.
- `notes/debt1a-geometric-core.md` §C — Im Z = g, Re Z = X, the modular unification.
- `notes/debt1a-geometric-core.md` §F — the unification and Born's debt among the results paid.
- `notes/debt1a-ii-X-classification.md` §3 — the vacuum ⟨Z⟩ = i·g at X = 0.
- `notes/broken-born-theory.md` v0.3 addendum — the introduction of Z with P2′.
- `notes/broken-born-program-v1.md` §4 — the same identifications in #9.
- `verify/battery.py` T2 — I[Z]² = −1 at one sampled point.
- `review/round3/referee/audit-notes.md` Step 3 — X ≠ 0 breaks η-compatibility, numerically.
