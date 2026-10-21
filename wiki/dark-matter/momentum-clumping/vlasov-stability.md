---
title: "Vlasov stability and Landau damping"
weight: 20
status: established
description: "Collisionless kinetic theory: the Vlasov equation, linear response about a Maxwellian, Landau damping, the Jeans instability and the Boltzmann H-theorem."
provenance: [T]
sources:
  - "notes/debt3a-stream-stability.md 'Setup'"
  - "notes/debt3a-stream-stability.md 'Limit 1 (broad gate)'"
  - "notes/debt3a-stream-stability.md 'Numbers at the scattering benchmark'"
  - "notes/broken-born-theory.md §5.2"
---

*The Vlasov equation describes a gas whose particles interact only through a smooth, averaged force field, so that the gas is fully specified by how densely it fills each region of position and velocity. Its stability theory asks whether a small ripple in that density grows or dies away. In a plasma a ripple usually decays even without collisions (Landau damping), while in a self-gravitating gas a ripple longer than a critical length grows into a lump (the Jeans instability); where collisions do act, they drive any distribution toward the smooth thermal shape (Boltzmann's H-theorem). The program used this textbook machinery in Debt 3 to test whether dark matter could [clump in velocity](/wiki/dark-matter/momentum-clumping/founding-image).*

**Status:** Established physics [T], summarized here from general knowledge; the program's use of it is in `notes/debt3a-stream-stability.md`.

## Key facts

- **The Vlasov equation** [T]. A distribution f(x, p, t) whose particles move with a single-particle energy ε(x, p), which includes the mean field of all the other particles, obeys the collisionless Boltzmann equation

  ```text
  ∂f/∂t + ∇ₚε · ∇ₓf − ∇ₓε · ∇ₚf = 0
  ```

  Debt 3 works in the "Nonrelativistic mean-field (Vlasov) limit of the gated interaction" (`notes/debt3a-stream-stability.md`, Setup), where the mean field depends on momentum as well as position ([the gated Vlasov model](/wiki/dark-matter/momentum-clumping/gated-vlasov-model)).
- **Linear response about a Maxwellian** [T]. One linearizes about a homogeneous equilibrium and asks whether plane-wave perturbations grow or decay. Debt 3 linearizes "about a homogeneous Maxwellian f₀(p) of dispersion σ; perturbations δf ∝ e^{i(k·x − ωt)}". When the interaction does not depend on momentum, the result is a scalar dispersion relation, and its threshold follows from "standard plasma-function algebra" (3a, Limit 1).
- **Landau damping** [T]. Below an instability threshold, a collisionless perturbation decays through its resonant exchange of energy with particles moving near its phase velocity. Debt 3's verdict below its threshold is "Landau-damped, stable" (3a, Limit 1).
- **The Jeans instability** [T]. In a self-gravitating gas, perturbations longer than the Jeans length grow, because self-gravity outweighs the restoring effect of the velocity dispersion. The lab notebook framed velocity clumping as "the Jeans problem with the roles of x and v exchanged" (`notes/broken-born-theory.md` §5.2).
- **The H-theorem** [T]. Collisions never decrease the entropy, so a collisional gas relaxes to a Maxwellian. Debt 3: "The H-theorem closes the collisional back door: gated collisions still maximize entropy; equilibrium is Maxwellian to one part in 10³⁰" (3a).
- **Notation.** In Debt 3, ω and k are a frequency and a wavevector, not the symplectic form or the gate variable ([notation](/wiki/notation)).

## Used by

- [The gated Vlasov model](/wiki/dark-matter/momentum-clumping/gated-vlasov-model) — the mean-field setup of the Debt-3 calculation.
- [The mean-field criterion and its 10²⁸–10³¹ shortfall](/wiki/dark-matter/momentum-clumping/instability-criterion) — the stream threshold, Landau damping below it, and the H-theorem closure of the collisional route.
- [The classicality theorem](/wiki/dark-matter/momentum-clumping/classicality-theorem) — the corollary of that threshold.
- [Obituary: velocity clumping, the founding image](/wiki/dark-matter/momentum-clumping/founding-image) — "the Jeans problem with the roles of x and v exchanged".

## Sources

- `notes/debt3a-stream-stability.md` 'Setup' — the Vlasov limit and the linearization Debt 3 performs
- `notes/debt3a-stream-stability.md` 'Limit 1 — broad gate' — Landau damping below threshold; the plasma-function algebra
- `notes/debt3a-stream-stability.md` 'Numbers at the scattering benchmark' — the H-theorem statement
- `notes/broken-born-theory.md` §5.2 — the Jeans framing of velocity clumping
