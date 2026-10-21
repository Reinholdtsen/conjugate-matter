---
title: "Force boosts and force composition"
weight: 50
status: alive
description: "The dual Lorentz group on (t, p) carries force-free frames to uniformly forced ones: simultaneity across momentum, forces composing to saturate at c̃, the Galilean limit (γ̃ − 1 ~ 10⁻⁶⁵ at neutron-star forces), and black-hole mergers as the one arena."
provenance: [D]
sources:
  - "papers/conjugate-special-relativity.md §2"
  - "papers/conjugate-special-relativity.md §7"
  - "papers/conjugate-special-relativity.md Abstract"
  - "papers/broken-born-checkpoint-v2.md §13"
---

*A force boost is the momentum-space counterpart of a Lorentz boost: where Einstein's boost relates observers moving at constant velocity, the force boost of #13 relates an observer under no force to one under a constant force, with the maximum force c̃ in the role of the speed of light. The same algebra then gives forces that combine like relativistic velocities, so that no sum of forces passes c̃, and observers under different forces who disagree about which events are simultaneous when the events differ in momentum. At what #13 calls the strongest sustained macroscopic force in nature, on a kilogram at a neutron-star surface, the correction is of order 10⁻⁶⁵, which #13 gives as the reason force looks exactly additive; only merging black holes approach the limit. The results are alive and unreviewed, and no observable signature in merger data has been derived.*

**Status:** Alive, unreviewed — the dual Lorentz group [D — structural], the composition law [D], the merger arena [O — flagged, not derived] — no `verify/` script; the 10⁻⁶⁵ estimate is unscripted ([the iron rule](/wiki/method/verification/iron-rule)).

## Key facts

- **The dual interval.** #13 §2: "The dual interval on (t, p) is ds̃² = c̃²dt² − dp², preserved by rotations in the (c̃t, p) planes — the dual Lorentz group [D — structural]." This is the 3+1 form, with time shared between the polarizations ([Two causal cones](/wiki/conjugate-relativity/two-causal-cones); for the competing four-dimensional cone, [Open: the two dual cones](/wiki/conjugate-relativity/two-cones-inconsistency)).
- **The force boost.** #13 §2: "A dual boost of parameter F carries the force-free frame to a uniformly forced one:"

  ```text
  p′ = γ̃(p − F t),    t′ = γ̃(t − F·p/c̃²),    γ̃ = (1 − F²/c̃²)^{−1/2}
  ```

  This is the Lorentz boost of [special relativity](/wiki/conjugate-relativity/special-relativity) with x → p, v → F and c → c̃.
- **Simultaneity across momentum** (untagged). #13 §2 item 1: "Events at equal t but different p are non-simultaneous in a forced frame — simultaneity depends on momentum location as, for us, it depends on position."
- **Force composition [D].** #13 §2 item 2: "With dual rapidity F = c̃ tanh φ and rapidities additive,"

  ```text
  F₁ ⊕ F₂ = (F₁ + F₂)/(1 + F₁F₂/c̃²)
  ```

  "so forces saturate at c̃ rather than accumulate without bound [D]."
- **The Galilean limit.** #13 §2 item 3: "For F ≪ c̃ the transformation reduces to the ordinary passage to an accelerated frame, with its familiar pseudo-forces, and composition reduces to addition. The strongest sustained macroscopic force in nature — on a kilogram at a neutron-star surface, ~10¹² N — gives γ̃ − 1 ≈ ½(F/c̃)² ~ 10⁻⁶⁵. Force *looks* exactly additive for the same reason velocity looked exactly additive before 1905: no accessible process approaches the limit." §7 lists "γ̃ − 1 ~ 10⁻⁶⁵ at neutron-star forces" among its numerical anchors; no script reproduces it.
- **Black-hole mergers [O — flagged, not derived].** #13 §2 item 3: "The single natural exception is a comparable-mass black-hole merger, which operates at F ~ c̃ by construction; if dual-kinematic corrections have any observable expression, merger and ringdown dynamics are where they would be order unity." §7's open list adds "whether merger-band gravitational-wave data can bound dual-kinematic corrections" ([Open problems and the queue](/wiki/status/open-problems)). The literature's companion maximum luminosity is approached by the same mergers ([Maximum force and maximal acceleration in the literature](/wiki/conjugate-relativity/maximum-force-conjectures)).
- **Not a prediction yet.** No signature is derived, and #11 §13's table has no row for dual kinematics ([Predictions and kill conditions](/wiki/predictions)).

## Sources

- `papers/conjugate-special-relativity.md` §2 — the dual interval, the force boost, simultaneity, composition, the Galilean limit and the merger arena; §7 for the fixed list, the anchor and the open item; Abstract for "short of black-hole mergers".
- `papers/broken-born-checkpoint-v2.md` §13 — the predictions table, which has no dual-kinematic row.
