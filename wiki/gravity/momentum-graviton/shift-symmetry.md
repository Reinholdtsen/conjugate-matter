---
title: "Shift symmetry: X is never auxiliary"
weight: 10
status: alive
description: "The rigid Sp(2d, ℝ) contains Z → Z + B, so constant shifts of X are exact symmetries: geometry gives X no potential, and it propagates or it does not exist."
provenance: [D]
sources:
  - "notes/debt1a-ii-X-classification.md §1"
  - "notes/debt1a-ii-X-classification.md §3"
  - "papers/broken-born-checkpoint-v2.md §7.1"
  - "notes/debt1a-geometric-core.md §D"
  - "notes/broken-born-theory.md 'Addendum (v0.4)'"
---

*The shift symmetry is the statement that adding a constant symmetric matrix B to the momentum graviton X, written Z → Z + B for the [modular field](/wiki/phase-space/modular-field/modular-field-z) Z = X + iY, leaves the program's geometry unchanged. The shift belongs to the symplectic group Sp(2d, ℝ), the symmetry group of the rigid [symplectic form](/wiki/phase-space/reciprocity/symplectic-form) ω, so any geometric action built from ω and the generalized metric H is unchanged by it. The geometry can therefore give X no potential energy and no coupling without derivatives: X is axion-like, a field that enters the dynamics only through its derivatives. This settles one of the three outcomes the program had defined for X, the auxiliary field with no motion of its own: X either propagates or does not exist. The result is derived [D — rigorous] and is the first link of the chain in [checkpoint #11](/wiki/history/documents/checkpoint) §7.1.*

**Status:** Alive — [D — rigorous] in calc note #6 (`notes/debt1a-ii-X-classification.md` §1); step (i) of #11 §7.1's chain, which is tagged [D + T] — a symmetry argument, not machine-checked.

## Key facts

- The shift, from calc note #6 §1 [D — rigorous] (see [The Debt-1 calc notes](/wiki/history/documents/debt-1-notes)): "The Möbius action of the rigid Sp(2d,ℝ) contains the subgroup [[1, B],[0, 1]], B symmetric, acting as"

  ```text
  Z → Z + B:    X → X + B,    Y → Y.
  ```

- "Constant shifts of X are exact symmetries of any S_H built from (ω, H). Consequences: X has no potential and no non-derivative couplings from the geometric sector alone — it is axion-like" (#6 §1). S_H is the [geometric action](/wiki/gravity/tuning-test/geometric-action); the Möbius action is that of Sp(2d, ℝ) on the [Siegel domain](/wiki/phase-space/modular-field/siegel-domain).
- What it excludes (#6 §1): "'auxiliary X' (the soft outcome 2) is off the table at the fundamental level: X appears only through derivatives, so it propagates or it doesn't exist." Outcome 2 of calc note #5's classification would have delivered the velocity gate directly as a contact four-χ operator (`notes/debt1a-geometric-core.md` §D); the gate is instead produced by X exchange ([The gate mechanism](/wiki/dark-matter/conjugate-matter/gate-mechanism)). The classification is described on [Why X must be massive](/wiki/gravity/momentum-graviton/forcing-chain).
- #11 §7.1, step (i): "The rigid Sp(2d,ℝ) contains Z → Z + B (B symmetric): X is shift-symmetric — axion-like, never auxiliary."
- Consequence for the mass (#6 §3): "The mass cannot be written by hand (shift symmetry) — but it doesn't need to be." It comes from [the gravitational Higgs mechanism](/wiki/gravity/momentum-graviton/gravitational-higgs) instead.
- The local version of these shifts is the [dual diffeomorphisms](/wiki/gravity/momentum-graviton/dual-diffeomorphisms), which make X a second graviton.

## Sources

- `notes/debt1a-ii-X-classification.md` §1 — the derivation [D — rigorous]; §3 for the consequence for the mass
- `papers/broken-born-checkpoint-v2.md` §7.1 — the current statement, step (i) of the chain
- `notes/debt1a-geometric-core.md` §D — the three-way classification and its auxiliary outcome
- `notes/broken-born-theory.md` 'Addendum (v0.4)' — the lab notebook's record of the result
