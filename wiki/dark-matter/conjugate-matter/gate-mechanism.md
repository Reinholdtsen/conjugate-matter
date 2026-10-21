---
title: "The gate mechanism: X exchange over fiber overlap"
weight: 30
status: alive
description: "χ couples to X through the dual stress; integrating X out gives a contact operator acting over the overlap of momentum-fiber wavepackets, with μ the χ quantum's fiber width."
provenance: [D]
sources:
  - "notes/debt1a-ii-X-classification.md §4"
  - "notes/debt1a-geometric-core.md §E"
  - "notes/broken-born-theory.md 'Addendum (v0.3, overnight)'"
  - "notes/broken-born-theory.md 'Addendum (v0.4)'"
  - "papers/broken-born-checkpoint-v2.md §8"
  - "notes/debt1a-iv-beta-coefficients.md §5"
  - "papers/conjugate-special-relativity.md §4"
---

*The gate mechanism is the program's derivation of [the velocity gate](/wiki/dark-matter/conjugate-matter/velocity-gate): two conjugate particles interact by exchanging the massive [momentum graviton X](/wiki/gravity/momentum-graviton), and they can do so only where their wavepackets overlap in momentum space. A conjugate quantum has a finite width μ along the momentum directions, as an atomic nucleus has a finite radius in space. A nucleus's size cuts off its scattering at large momentum transfer; the χ quantum's momentum width cuts off its interaction at large relative momentum, which is the same construction with position and momentum exchanged. Because X is heavy, its exchange acts as a contact interaction, and the overlap of the two wavepackets supplies the gate; the exact shape of the cutoff depends on details not yet computed.*

**Status:** Alive — [D — structural] (`notes/debt1a-geometric-core.md` §E; `notes/debt1a-ii-X-classification.md` §4, "with one honest downgrade"), and [D] for the mechanism with the shape [O] in the checkpoint (#11 §8) — no explicit X propagator exists, and no `verify/` script covers it.

## Key facts

- **Exchange of X.** "Exchange of X between two such bilinears yields a four-point amplitude that depends on the **incoming relative momenta** of the pair", the bilinears being [dual stresses](/wiki/dark-matter/conjugate-matter/dual-stress) (`notes/debt1a-geometric-core.md` §E). That note's first identification, "gate = momentum-graviton exchange, μ ↔ (M_X, M_B) parametrically", was replaced by the fiber width in the next note; M_B is the mass scale of [the lab notebook](/wiki/history/documents/lab-notebook)'s geometric action S_H (#1 §3).
- **Fiber overlap.** "Integrating out massive X between χ bilinears gives the contact four-χ operator. The relative-momentum dependence enters through the χ quanta's **intrinsic momentum-space extent**: p-polarized quanta are extended objects on the momentum fiber with width μ, and they exchange X only over their fiber overlap — the dual of how x-extended composites acquire form factors F(qR)" (`notes/debt1a-ii-X-classification.md` §4). The momentum fiber is the set of momentum directions attached to each point of spacetime. Integrating out a heavy carrier to leave a contact interaction is standard effective-field-theory practice [T].
- **The Gaussian case.** "Wavepacket overlap of Gaussian profiles gives exactly e^{−(p₁−p₂)²/2μ²} — the postulated gate, with **μ = the χ quantum's own p-width**, a physical identification the [effective field theory] lacked." The same note adds the downgrade: "tree-level exchange with generic vertices yields rational (power-law-tailed) gates; the Gaussian requires the Gaussian fiber profile" (§4). Which holds is [the gate-shape problem](/wiki/dark-matter/conjugate-matter/gate-shape).
- **The lab-notebook record.** The lab notebook's v0.3 addendum names the mechanism, "X-exchange between χ dual-stress bilinears, which produces dependence on incoming relative momenta — the defining property of the gate"; v0.4 adds that "μ is identified as the χ quantum's intrinsic momentum-fiber width, with a Gaussian gate iff the fiber profile is Gaussian" (#1).
- **What it paid.** "**Debt 2:** mechanism paid (X-exchange, μ = fiber width); shape completion open (Gaussian vs rational tail — now also an observable discriminant)" (`notes/debt1a-iv-beta-coefficients.md` §5); see [the three debts](/wiki/history/debts). The consequence for the observable is the knee of [the gated scattering law](/wiki/dark-matter/conjugate-matter/scattering-law), tested in [row 1](/wiki/predictions/self-interaction-knee).
- **Unreconciled exponents.** The overlap form e^{−(p₁−p₂)²/2μ²} and the lab notebook's postulated e^{−k²/μ²} with k = m_χv_rel/2 (#1 §3) are not reconciled in any source.
- **The reading in conjugate relativity.** The paper on [conjugate special relativity](/wiki/conjugate-relativity) (#13 §4) reads μ as fixed by the χ quantum's invariant extent: "μ ~ ℏ/λ_χ — which is precisely the gate scale of the dark-matter sector, v\* = √2 μ/m_χ" [D — structural]. #13 is unreviewed, and its use of λ_χ alongside m_χ is not reconciled with the checkpoint's ordinary kinematics for χ, which govern the χ candidate; see [the invariant-length shell](/wiki/conjugate-relativity/invariant-length-shell).

## Sources

- `papers/broken-born-checkpoint-v2.md` §8 — the checkpoint's statement and tags
- `notes/debt1a-ii-X-classification.md` §4 — integrating out X, fiber overlap, the Gaussian case, the rational-tail downgrade
- `notes/debt1a-geometric-core.md` §E — the four-point amplitude; the superseded μ ↔ (M_X, M_B) identification
- `notes/debt1a-iv-beta-coefficients.md` §5 — Debt 2's mechanism paid, shape open
- `notes/broken-born-theory.md` 'Addendum (v0.3, overnight)', 'Addendum (v0.4)' — the mechanism and the fiber width in the lab notebook
- `papers/conjugate-special-relativity.md` §4 — μ ~ ℏ/λ_χ as the gate scale
