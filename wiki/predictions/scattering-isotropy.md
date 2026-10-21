---
title: "Row 2: isotropic scattering below the gate"
weight: 30
status: alive
description: "Below the gate velocity, gated scattering through a heavy mediator is isotropic, unlike the forward-peaked scattering of light-mediator models; killed by halo morphology that demands forward peaking."
provenance: [D]
sources:
  - "papers/broken-born-checkpoint-v2.md §13 row 2"
  - "papers/broken-born-checkpoint-v2.md §8"
  - "papers/broken-born-checkpoint-v2.md §12"
  - "notes/broken-born-theory.md §5.1"
  - "notes/broken-born-theory.md §9"
  - "notes/broken-born-program-v1.md §9"
  - "notes/debt3a-stream-stability.md 'Consequences for the predictions table'"
---

*Row 2 of the predictions table concerns the directions into which colliding dark-matter particles scatter. In the usual self-interacting models, where a light particle carries the force, most collisions deflect the particles only slightly, so the scattering is forward-peaked; in the program's gated model, collisions slower than the gate velocity scatter equally in all directions. The two patterns carry energy and momentum through a halo with different efficiencies, so in principle they leave different imprints on the shapes of relaxed halos. The row stands, with one stated assumption: the particle that carries the gated force is heavy.*

**Status:** Alive — [D] in the lab notebook (#1 §5.1), restated in #11 §8, whose mechanism is [D] and shape [O] — it follows from the gate's dependence on the relative momentum of the colliding pair rather than on the momentum transferred; it assumes a heavy mediator and is not machine-checked.

## Key facts

- **The row** ([checkpoint #11](/wiki/history/documents/checkpoint) §13). Observable: "Scattering anisotropy". Standard expectation: "Forward-peaked (light mediators)". Requirement: "Isotropic below the gate". Killed by: "Morphology demanding forward peaking".
- **Why it is isotropic** ([the lab notebook](/wiki/history/documents/lab-notebook), #1 §5.1, [D]): "Because the gate depends on k and the contact part is flat in q, scattering below v\* is isotropic; light-mediator Yukawa scattering is forward-peaked. Energy- vs momentum-transport efficiencies differ, which feeds into halo relaxation morphology." Here k is the incoming relative momentum and q the momentum transfer; the dependence on k is what defines [the velocity gate](/wiki/dark-matter/conjugate-matter/velocity-gate).
- **The assumption.** The derivation is made "In Born approximation with a heavy transfer mediator (m_φ ≳ m_χ, contact-like in x)" (#1 §5.1). The current amplitude is M(k,q) = 4πα̃m_χ/(q² + m_φ²)·F(k²/μ²) (#11 §8; [the gated scattering law](/wiki/dark-matter/conjugate-matter/scattering-law)), with the gate delivered by [X exchange](/wiki/dark-matter/conjugate-matter/gate-mechanism).
- **The contrast.** #11 §8 states the signature as "isotropic below the gate versus Yukawa forward-peaking". Forward peaking in light-mediator models is established physics, covered in [self-interacting dark matter](/wiki/dark-matter/halo-astrophysics/self-interacting-dark-matter).
- **Wording across versions.** v0.1's observable was "Scattering anisotropy (via halo relaxation morphology)", killed by "Morphology fits demanding forward-peaked kernels" (#1 §9); v1's kill condition was "Morphology demanding forward-peaked kernels" (#9 §9). #11 shortens both ([history of the table](/wiki/predictions/table-history)).
- **Particles only, so far.** For wave-like χ, calc note #2 concluded that "Rows 1–2 must be re-derived in wave language (two-body Born scattering is no longer the right observable)" (`notes/debt3a-stream-stability.md`). No later document restates isotropy for [the wave island](/wiki/dark-matter/momentum-clumping/wave-island).
- **Use.** #11 §12 lists "isotropic scattering" among the distinctive handles of [the χ-particle candidate](/wiki/dark-matter/candidates/chi-particles), and rows 1–3 are the discriminators of [row 11](/wiki/predictions/dark-sector-microstructure). The neighbouring rows are [row 1](/wiki/predictions/self-interaction-knee), the knee, and [row 3](/wiki/predictions/island-discriminant), the island discriminant.

## Sources

- `papers/broken-born-checkpoint-v2.md` §13 row 2 — the row; §8 for the amplitude and the current statement; §12 for the candidate's handles
- `notes/broken-born-theory.md` §5.1 — the derivation of isotropy [D] and its heavy-mediator assumption
- `notes/broken-born-theory.md` §9 and `notes/broken-born-program-v1.md` §9 — the v0.1 and v1 wording of the row
- `notes/debt3a-stream-stability.md` 'Consequences for the predictions table' — rows 1–2 to be re-derived for wave dark matter
