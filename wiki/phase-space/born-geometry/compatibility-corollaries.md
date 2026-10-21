---
title: "Corollaries: unimodularity, no B-field, slaved momentum metric"
weight: 50
status: established
description: "det H = 1 (ℏ-rigidity as geometry), no Kalb–Ramond analog, and g̃ = g⁻¹ — the slaved momentum metric that collided with the theory as documented and forced the repair."
provenance: [D]
sources:
  - "notes/debt1a-geometric-core.md §A"
  - "notes/debt1a-geometric-core.md §B"
  - "notes/debt1a-geometric-core.md §C"
  - "papers/broken-born-checkpoint-v2.md §5"
  - "papers/broken-born-checkpoint-v2.md §2"
  - "verify/battery.py T2"
  - "review/round3/referee/audit-notes.md Step 3"
  - "notes/knot-dark-matter-standalone.md §1"
  - "papers/conjugate-special-relativity.md §1"
  - "HANDOFF.md §4"
---

*Three consequences follow from the [compatibility theorem](/wiki/phase-space/born-geometry/compatibility-theorem)'s answer H = diag(g, g⁻¹). The determinant of H is 1, so phase-space volume cannot change, which the program reads as the constancy of Planck's constant built into the geometry. The off-diagonal block, where [double field theory](/wiki/phase-space/born-geometry/double-field-theory) keeps its B-field, must vanish. And the momentum metric is fixed as the inverse of the position metric, g̃ = g⁻¹, so momentum space has no geometry of its own. That last corollary contradicted the program as it then stood — the dark-energy field and the geometric origin of the dark-matter gate both disappeared — and it forced the postulate change to P2′.*

**Status:** Established — derived in #5 as rigorous corollaries [D] of a theorem #11 v2.1 credits to Freidel–Leigh–Minic [T] — det H = 1 is machine-checked at one sampled point of the modular family (battery test T2), so its persistence across the whole family stays [D].

## Key facts

- **Corollary 1: det H = 1.** #5 §A: "**det H = 1 identically.** The generalized metric is unimodular: phase-space volume is not a dynamical field. ℏ-rigidity is manifest in the geometry, not imposed on it." Round 3 confirmed det H = 1 numerically on diag(g, g⁻¹) at d = 3, 4 (audit notes, Step 3).
- **The family-wide claim.** #11 §5 adds that det H = 1 "— machine-verified — persists across the whole modular family of §6" (#11 §2 says the same). Battery test T2 checks one random point of [the Siegel domain](/wiki/phase-space/modular-field/siegel-domain): `PASS  T2 det H_Z = 1  [det=1.000000000000]`. One sample does not verify a statement about the whole family, so this wiki tags the family-wide statement [D] ([conflicts between sources](/wiki/history/documents/source-conflicts); [the battery](/wiki/method/verification/battery)).
- **Corollary 2: no Kalb–Ramond analog.** #5 §A: the off-diagonal block, double field theory's B-field, "is frozen out by the extra symplectic compatibility. Born geometry with both structures rigid is *stiffer* than" double field theory.
- **Corollary 3: the slaved momentum metric.** #5 §A: "**The momentum metric is slaved: g̃ = g⁻¹ pointwise.** No independent momentum-space geometry survives." #13 builds its [two causal cones](/wiki/conjugate-relativity/two-causal-cones) on this block form: "position space carries the metric g and momentum space its inverse".
- **The collision [D — structural].** #5 §B: "Corollary 3 collides with the theory as documented." With ω and η both rigid the compatible polarizations are discrete, so there is no Lagrangian Grassmannian, no Maslov circle and no τ field, and S_H is a functional of g alone — "Branch R", in which the program reduces to general relativity plus one bespoke self-interacting dark-matter model "with w ≡ −1 and the gate unexplained". See [original P2](/wiki/program/postulates/original-p2), [the nontriviality theorem](/wiki/program/postulates/nontriviality-theorem) and [P2′](/wiki/program/postulates/p2-prime).
- **Under P2′.** g̃ = g⁻¹ survives only on the vacuum slice X = 0 of [the modular field](/wiki/phase-space/modular-field/modular-field-z) (#5 §C); "any independent momentum-space geometry resides in the fluctuation X" (#14 §1). The handoff's chat-only results add that the slaved layer "is algebraic (Einstein's equation does double duty)" (`HANDOFF.md` §4; [chat-only results](/wiki/gravity/momentum-graviton/chat-only-results)).

## Used by

- [Original P2: both structures rigid (superseded)](/wiki/program/postulates/original-p2) — corollary 3 is what made strict P2 untenable.
- [The nontriviality theorem](/wiki/program/postulates/nontriviality-theorem) — content beyond general relativity iff η is emergent.
- [P2′: only the symplectic form is rigid](/wiki/program/postulates/p2-prime) — the repair; det H = 1 as the geometric face of ℏ-rigidity.
- [Two causal cones](/wiki/conjugate-relativity/two-causal-cones) — the dual cone of the slaved momentum metric.
- [The cosmological constraint a·ã = 1](/wiki/cosmology/scale-factor-duality/cosmological-constraint) — another consequence of a fixed phase-space cell.

## Sources

- `notes/debt1a-geometric-core.md` §A — the three corollaries, "[D — rigorous]".
- `notes/debt1a-geometric-core.md` §B — "Corollary 3 collides with the theory as documented"; Branch R; the repair.
- `notes/debt1a-geometric-core.md` §C — the vacuum slice X = 0.
- `papers/broken-born-checkpoint-v2.md` §5, §2 — the corollaries in the current reference; the family-wide det H = 1 claim.
- `verify/battery.py` T2 — det H_Z = 1 at one sampled Siegel point.
- `review/round3/referee/audit-notes.md` Step 3 — det H = 1 on diag(g, g⁻¹) at d = 3, 4.
- `papers/conjugate-special-relativity.md` §1 — the block form as two metrics with two cones.
- `notes/knot-dark-matter-standalone.md` §1 — momentum-space geometry resides in X.
- `HANDOFF.md` §4 — the chat-only remark on the slaved layer.
