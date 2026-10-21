---
title: "The velocity gate"
weight: 10
status: alive
description: "The self-interaction amplitude depends on the incoming relative momentum through a gate F(k²/μ²), a variable no position-local mediator produces; from the v0.1 Gaussian postulate to the current form."
provenance: [D, O]
sources:
  - "papers/broken-born-checkpoint-v2.md §8"
  - "notes/broken-born-program-v1.md §6"
  - "notes/debt1a-geometric-core.md §E"
  - "notes/debt1a-geometric-core.md §B"
  - "notes/debt1a-ii-X-classification.md §4"
  - "notes/debt1a-iv-beta-coefficients.md §5"
  - "notes/broken-born-theory.md §3"
  - "notes/broken-born-theory.md §5.1"
  - "notes/broken-born-theory.md §5.2"
  - "notes/broken-born-theory.md §11 item 2"
  - "notes/broken-born-theory.md 'Addendum (v0.3, overnight)'"
  - "notes/broken-born-theory.md 'Addendum (v0.4)'"
  - "papers/broken-born-checkpoint-v2.md Appendix A item 4"
  - "HANDOFF.md §2"
---

*The velocity gate is a factor in the self-interaction of [conjugate matter](/wiki/dark-matter/conjugate-matter) χ that turns the interaction off between two particles that approach each other with a large relative velocity. For an ordinary force carried through position space, the scattering amplitude depends on how much momentum the two particles exchange; the gate makes it depend also on the momentum with which they approach, a variable that, according to [the checkpoint](/wiki/history/documents/checkpoint), no carrier local in position produces. In signal terms, an ordinary contact force acts where two waveforms overlap, and the gate acts only where their spectra overlap as well. The program first postulated the gate as a Gaussian, then derived its mechanism from exchange of the [momentum graviton X](/wiki/gravity/momentum-graviton) between conjugate particles. The mechanism stands as a structural derivation; the exact shape of the cutoff is open. The gate is what lets conjugate matter scatter off itself in dwarf galaxies, where dark matter moves slowly, and not in galaxy clusters, where it moves fast.*

**Status:** Alive — [D — mechanism; shape [O]] (`papers/broken-born-checkpoint-v2.md` §8) — the mechanism is derived structurally in [the Debt-1 calc notes](/wiki/history/documents/debt-1-notes); the shape is [Open: the gate shape (OP4)](/wiki/dark-matter/conjugate-matter/gate-shape); no `verify/` script covers either. The v0.1 Gaussian postulate is superseded.

## The amplitude

The checkpoint, #11, states the gate in its section on conjugate matter (§8):

> "χ propagates on g (equivalence principle; Bullet-Cluster-safe) with nonrelativistic amplitude M(k,q) = 4πα̃m_χ/(q² + m_φ²)·F(k²/μ²), k the incoming *relative* momentum — the variable no x-local mediator produces, delivered by X-exchange between dual-stress bilinears, with μ the χ quantum's intrinsic momentum-fiber width [D — mechanism; shape [O]]."

```text
M(k, q) = 4πα̃ m_χ / (q² + m_φ²) · F(k²/μ²)
```

Here "x-local" means local in position. The first factor is an ordinary scattering amplitude; the second, F, is the gate. #11 does not define α̃, m_φ or F, so the wiki takes them from [the lab notebook](/wiki/history/documents/lab-notebook) (#1 §3) and the first consolidation, v1 (#9 §6), as [conflicts between sources](/wiki/history/documents/source-conflicts) records:

- **m_χ** is the mass of a χ particle.
- **q** is the momentum transfer, the momentum one particle hands to the other in the collision: "q is the momentum **transfer**" (#1 §3); "where q is transfer and k the incoming *relative* momentum" (#9 §6).
- **k** is the incoming relative momentum. The lab notebook fixes it as "k = m_χv_rel/2", with v_rel the relative velocity of the pair (#1 §3).
- **α̃** is the coupling constant and **m_φ** the mass of the carrier of the momentum transfer. Both enter the lab notebook's boxed amplitude without further definition; its scattering law then assumes "a heavy transfer mediator (m_φ ≳ m_χ, contact-like in x)" (#1 §5.1).
- **μ** is the momentum scale of the gate. In v0.1 it was "a scale μ of the g̃ sector" (#1 §3), g̃ being the momentum-space metric; since the v0.4 addendum it is the χ quantum's own width in momentum (below).
- **F** is the gate function. The lab notebook's Gaussian, e^{−k²/μ²}, tends to 1 as μ grows, and the notebook states the limit: "An x-local Yukawa is the limit μ → ∞" (#1 §3). Without the gate, the amplitude is that of ordinary [self-interacting dark matter](/wiki/dark-matter/halo-astrophysics/self-interacting-dark-matter) with a Yukawa mediator.

The checkpoint's other clause, that χ propagates on the metric g, is [postulate P4](/wiki/program/postulates/p4-polarized-matter): conjugate matter falls, orbits and bends light exactly as ordinary matter does. That side of χ is on [the χ-particle candidate](/wiki/dark-matter/candidates/chi-particles). The gate concerns only its self-interaction.

## Background: what a position-local force depends on [T]

Two particles of equal mass m_χ that collide elastically can be described in their centre-of-mass frame, where they approach with equal and opposite momenta of size k and leave with momenta of the same size in a new direction. The incoming relative momentum k fixes the energy of the collision. The transfer q measures how far the direction turns: for a scattering angle θ, q = 2k sin(θ/2), so q runs from zero for a grazing collision to 2k for a head-on rebound [T].

In the Born approximation, the first-order treatment in which the lab notebook derives its scattering law (#1 §5.1), the amplitude for scattering off a static potential V(r) is proportional to the Fourier transform of V evaluated at the transfer q [T]. The potential's profile in position and the amplitude's dependence on q are a waveform and its spectrum. The Yukawa potential −α e^{−m_φ r}/r, the potential of a force carried by a field of mass m_φ, transforms to a constant times 1/(q² + m_φ²) [T], which is the first factor of M(k, q). However the force varies with distance, an interaction that acts at points of position space produces, at this order, an amplitude that depends on q alone.

A cross-section can still depend on velocity without a gate. For a light Yukawa mediator, the transfer cross-section falls with velocity because faster collisions reach larger q and the amplitude weakens there: "Yukawa SIDM falls as v⁻⁴ with a Coulomb-log correction" (#1 §5.1). That dependence comes from the range of q a collision can reach. The gate is a dependence on k at fixed q, which the lab notebook singles out: "The Gaussian *gate* e^{−k²/μ²} is the new object: it is the imprint of momentum-space locality, and it depends on k, not q" (#1 §3). The sources state that no position-local carrier produces it; the Born-level reason is the one above.

## The mechanism in brief

Calc note #5 found the gate's origin in the [modular field](/wiki/phase-space/modular-field/modular-field-z), whose real part is the momentum graviton X [D — structural]:

> "Conjugate matter couples to H universally (P4); its coupling to the X-block is through the **dual stress** T̃ — moments involving momentum-derivatives of the χ bilinear. Exchange of X between two such bilinears yields a four-point amplitude that depends on the **incoming relative momenta** of the pair — the variable no x-local mediator can produce, and exactly the variable the gate was postulated in." (`notes/debt1a-geometric-core.md` §E)

Calc note #6 completed it: integrating out the massive X leaves a contact interaction, and the dependence on relative momentum enters because a χ quantum has a finite width μ along the momentum directions, so two quanta exchange X only where their momentum-space wavepackets overlap (`notes/debt1a-ii-X-classification.md` §4). The coupling is on [dual stress T̃](/wiki/dark-matter/conjugate-matter/dual-stress) and the derivation step by step on [the gate mechanism](/wiki/dark-matter/conjugate-matter/gate-mechanism). Calc note #8 records the outcome for the program's debts: "**Debt 2:** mechanism paid (X-exchange, μ = fiber width); shape completion open (Gaussian vs rational tail — now also an observable discriminant)" (`notes/debt1a-iv-beta-coefficients.md` §5).

The mechanism needs X. Under the original postulate that both the symplectic form ω and the neutral metric η are rigid ([original P2](/wiki/program/postulates/original-p2)), the generalized metric reduces to H = diag(g, g⁻¹) and calc note #5 finds "No momentum graviton, hence no geometric origin for the χ gate either"; in that branch the program "reduces to GR + one bespoke SIDM model, with w ≡ −1 and the gate unexplained" (`notes/debt1a-geometric-core.md` §B), GR being general relativity and SIDM self-interacting dark matter. This is part of what [the nontriviality theorem](/wiki/program/postulates/nontriviality-theorem) records, and it is why the gate's derivation depends on [P2′](/wiki/program/postulates/p2-prime), under which η is emergent.

## Two conventions, not reconciled

The sources write the Gaussian gate in two ways:

```text
#1 §3 (v0.1):   e^{−k²/μ²},   k = m_χ v_rel / 2
#6 §4:          e^{−(p₁−p₂)²/2μ²}
```

The first is a postulate in the incoming relative momentum. The second is the result of the overlap calculation, written in the momenta p₁ and p₂ of the two quanta. No source relates the two exponents, and μ meant a scale of the momentum-space metric in the first and the χ quantum's own momentum width in the second. #11 §8 writes the general F(k²/μ²) and fixes neither. The conflict is recorded as unreconciled on [conflicts between sources](/wiki/history/documents/source-conflicts).

## What the gate does

- **The scattering law.** The gate turns into a velocity dependence of the cross-section, "σ_T(v) = σ₀F(v²/v\*²): robust knee at v\*; tail (Gaussian vs rational) diagnoses the vertex completion; isotropic below the gate versus Yukawa forward-peaking" (#11 §8). Self-scattering is strong below the gate velocity v\* and suppressed above it: [the gated scattering law σ_T(v)](/wiki/dark-matter/conjugate-matter/scattering-law). Its strength, fitted to the cores of dwarf galaxies, is [the scattering benchmark](/wiki/dark-matter/conjugate-matter/benchmark).
- **The predictions.** The knee is [row 1](/wiki/predictions/self-interaction-knee) of the predictions table, the isotropy below the gate is [row 2](/wiki/predictions/scattering-isotropy), and the shape of the knee's tail is read by [row 3, the island discriminant](/wiki/predictions/island-discriminant).
- **The collective image it did not deliver.** The lab notebook expected the gated attraction to act collectively: "a momentum-gated attraction is precisely the pairing interaction, and below a critical velocity dispersion the core of a halo condenses — momentum-space clumping, realized" (#1 §5.2). The program's own Debt-3 calculation killed this ([Obituary: velocity clumping, the founding image](/wiki/dark-matter/momentum-clumping/founding-image)); for particles, the mean-field criterion fails by 10²⁸–10³¹ at the benchmark ([the mean-field criterion](/wiki/dark-matter/momentum-clumping/instability-criterion)).
- **The founding supposition it keeps.** #11's audit of the [founding suppositions](/wiki/program/founding-suppositions) records item 4, "Dark matter is conjugate matter", as "**alive, modified**: x-clumping, gated self-force; now one of two remaining candidates (§12)" (#11 Appendix A). Conjugate matter clusters in position like ordinary dark matter; the gate is its distinctive self-force.

[The handoff](/wiki/history/documents/handoff) lists the gate among the live results: "Dark matter sector: gated self-interaction (gate = X-exchange; gate variable = incoming relative momentum; μ = χ's momentum-fiber width); knee at v\*; knee-tail shape = particle-vs-wave 'island discriminant' (new observable)" (`HANDOFF.md` §2).

## Superseded: the Gaussian gate of v0.1

The lab notebook's v0.1 action routes χ's self-interaction "through the g̃ block" and writes "The leading nonrelativistic effective amplitude consistent with the residual ℤ₂ and with p-polarization" as a boxed formula (#1 §3):

```text
M(k, q) = 4πα̃ m_χ / (q² + m_φ²) · e^{−k²/μ²}
```

Its tags split the claim. That a gate exists was a postulate: "that the gate exists, with support set by a scale μ of the g̃ sector, is the EFT-level content of 'conjugate matter interacts in momentum space.' **[P]**", EFT being effective field theory. Its Gaussian form was not derived: "Deriving the precise gate shape from S_H + S_mix is open **[O]**" (#1 §3), where S_H is the geometric action and S_mix a mixing term the notebook names without writing out. #1 §11 lists the derivation as its second open problem: "obtain e^{−k²/μ²} (or its true form) from S_H + S_mix rather than postulating it. The σ(v) *cliff* is robust to the exact shape; the sub-v\* profile is not. **[O]**"

Three steps replaced the postulate:

1. **v0.3 addendum.** Strict P2 was found to remove "any geometric origin for the χ gate"; with P2′ in its place, "the *mechanism* is X-exchange between χ dual-stress bilinears, which produces dependence on incoming relative momenta — the defining property of the gate; the shape awaits the X propagator" (#1 'Addendum (v0.3, overnight)'). From then on the gate's existence rested on a structural derivation rather than a postulate.
2. **v0.4 addendum.** "μ is identified as the χ quantum's intrinsic momentum-fiber width, with a Gaussian gate iff the fiber profile is Gaussian" (#1 'Addendum (v0.4)'). The Gaussian became one possibility among others, and the scattering law's exponential cliff weakened to a knee ([the gated scattering law](/wiki/dark-matter/conjugate-matter/scattering-law)).
3. **v1 and the checkpoint.** v1 (#9 §6) and #11 §8 replace e^{−k²/μ²} by the unspecified F(k²/μ²) and tag the claim [D — mechanism; shape [O]].

The lab notebook's numbers that assume a Gaussian tail, such as "σ_T/m (1500 km/s) ≈ 30 e^{−156} ≈ 0" (#1 §5.1), hold only if the tail turns out Gaussian; they are on [the scattering benchmark](/wiki/dark-matter/conjugate-matter/benchmark).

## What is open

Two questions remain, each with its own page.

- **The shape.** Whether F falls off as a Gaussian or with a power-law (rational) tail depends on the X propagator on the momentum fibers and on the χ quantum's profile there: [Open: the gate shape (OP4)](/wiki/dark-matter/conjugate-matter/gate-shape), item 4 of #11 §14.
- **The strength.** The mechanism explains why the interaction depends on relative momentum, not why it is strong. Fitting dwarf cores needs a cross-section #11 §8 calls nuclear-scale, while ordinary matter couples to the same X only at gravitational strength: [Open: the dual-stress enhancement (OP5)](/wiki/dark-matter/conjugate-matter/dual-stress-enhancement), item 5 of #11 §14.

Neither is on the current work queue (root `CLAUDE.md`, "Since the handoff"). Both are listed in [open problems](/wiki/status/open-problems).

## A name collision

"The gate" also names the build check `scripts/check.sh`, which every change to the project must pass. That is a different subject, on [the gate](/wiki/method/verification/the-gate).

## Sources

- `papers/broken-born-checkpoint-v2.md` §8 — the current amplitude, the gate variable, the tags, the scattering law; Appendix A item 4 — "Dark matter is conjugate matter", alive, modified
- `notes/broken-born-program-v1.md` §6 — v1's statement, with q the transfer and F in place of the Gaussian
- `HANDOFF.md` §2 — the gate among the live results
- `notes/debt1a-geometric-core.md` §E — the mechanism: X exchange between dual-stress bilinears; §B — no geometric origin for the gate under strict P2, Branch R
- `notes/debt1a-ii-X-classification.md` §4 — the fiber overlap and the form e^{−(p₁−p₂)²/2μ²}
- `notes/debt1a-iv-beta-coefficients.md` §5 — Debt 2's mechanism paid, shape open
- `notes/broken-born-theory.md` §3 — the v0.1 Gaussian gate, k = m_χv_rel/2, the μ → ∞ Yukawa limit, the [P] and [O] tags; §5.1 — the heavy transfer mediator, the Born approximation, the Yukawa v⁻⁴ tail; §5.2 — the gated attraction in the founding image; §11 item 2 — the gate-shape derivation listed as open
- `notes/broken-born-theory.md` 'Addendum (v0.3, overnight)' — strict P2 removes the gate's geometric origin; the mechanism identified as X exchange
- `notes/broken-born-theory.md` 'Addendum (v0.4)' — μ as the fiber width; Gaussian iff the fiber profile is Gaussian
