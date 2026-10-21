---
title: "Original P2: both structures rigid (superseded)"
weight: 20
status: superseded
description: "The first rigidity postulate froze both ω and η: only discrete polarizations, no Maslov circle, no τ, and a theory collapsed to Branch R (general relativity plus one self-interacting dark-matter model)."
provenance: [P]
sources:
  - "notes/broken-born-theory.md §1"
  - "notes/debt1a-geometric-core.md §A"
  - "notes/debt1a-geometric-core.md §B"
  - "papers/broken-born-checkpoint-v2.md §4"
  - "papers/broken-born-checkpoint-v2.md §5"
  - "notes/broken-born-theory.md 'Addendum (v0.3)'"
  - "notes/broken-born-theory.md 'Addendum (v0.4)'"
---

*The original P2 was the lab notebook's second axiom: both the symplectic form ω and the neutral metric η are fixed background structures, and only the generalized metric H carries degrees of freedom. It was meant to express the constancy of Planck's constant. The program's own geometry showed that it fixed too much: with both structures fixed, the vacuum can pick among only a discrete set of position–momentum splittings, there is no circle of polarizations for a dark-energy field to live on, and the theory reduces to general relativity plus one bespoke model of self-interacting dark matter. It was replaced by [P2′](/wiki/program/postulates/p2-prime), which fixes ω alone.*

**Status:** Superseded by P2′ — [P] as stated; its reduction to "Branch R" is [D — structural] (`notes/debt1a-geometric-core.md` §B) — the replacement was forced by [the nontriviality theorem](/wiki/program/postulates/nontriviality-theorem) (#11 §4–§5; lab notebook addendum v0.3). Listed in [superseded statements](/wiki/status/superseded).

## Key facts

- Statement (#1 §1, v0.1):

  ```text
  P2 (Rigidity of ℏ). ω and η are non-dynamical; only H carries degrees
  of freedom. Physically: the symplectic structure is the constancy of
  ℏ — phase-space cells do not stretch.                              [P]
  ```

- With both structures fixed, the [compatibility theorem](/wiki/phase-space/born-geometry/compatibility-theorem) [T][V] (battery test T1, [the verification battery](/wiki/method/verification/battery)) leaves only H = diag(g, g⁻¹), with det H = 1, no Kalb–Ramond analog and a slaved momentum metric g̃ = g⁻¹ ([the corollaries](/wiki/phase-space/born-geometry/compatibility-corollaries)). The note that derived them: "Corollary 3 collides with the theory as documented" (#5 §B).
- #5 §B: "The space of polarizations compatible with both structures (ω-Lagrangian *and* η-null) is **discrete** — the 2^d coordinate-type splittings, GL(d)-rigid. No Lagrangian Grassmannian, no Maslov circle, **no τ field**." See [the Lagrangian Grassmannian](/wiki/phase-space/modular-field/lagrangian-grassmannian) and [τ as the Maslov phase](/wiki/phase-space/modular-field/maslov-phase).
- #5 §B: "With H = diag(g, g⁻¹), S_H is a functional of g alone: a pure metric theory. No momentum graviton, hence no geometric origin for the χ gate either." See [the momentum graviton](/wiki/gravity/momentum-graviton) and [the velocity gate](/wiki/dark-matter/conjugate-matter/velocity-gate).
- Branch R (#5 §B): the theory "reduces to GR + one bespoke SIDM model, with w ≡ −1 and the gate unexplained. On Branch R the program has no content of its own — and it is *already disfavored* if DESI's drift is real." Here GR is general relativity, SIDM is self-interacting dark matter, and DESI is the Dark Energy Spectroscopic Instrument survey.
- The lab notebook said P2 "does triple duty": it kills the would-be second graviton (no Boulware–Deser ghost), enforces the cosmological constraint aã = const, and supplies the explicit breaking that gives the dark-energy field its potential (#1 §1, paraphrased; its section pointers there are wrong). The three fared differently. Addendum v0.4 found that X is a second graviton after all, made massive ([why X must be massive](/wiki/gravity/momentum-graviton/forcing-chain)); the constraint survives from ω alone as a·ã = 1 ([the cosmological constraint](/wiki/cosmology/scale-factor-duality/cosmological-constraint)); and the origin of the potential became [an open problem](/wiki/symmetry-breaking/rho-preserving-potential).
- The body of the lab notebook was never edited, so strict P2 still reads as in force there; its v0.3 addendum records the replacement, and #9 and #11 state only P2′.

## Sources

- `notes/broken-born-theory.md` §1 — the statement and its "triple duty"; 'Addendum (v0.3)' — the replacement; 'Addendum (v0.4)' — the second graviton
- `notes/debt1a-geometric-core.md` §A–§B — the compatibility theorem, the inconsistency, Branch R and the repair
- `papers/broken-born-checkpoint-v2.md` §4–§5 — the current record of the forced correction
