---
title: "Special relativity: the template"
weight: 10
status: established
description: "Boosts, γ and rapidity, the Minkowski interval and light cone, simultaneity, time dilation and length contraction, the mass shell and E = mc², the Galilean limit and the 3+1 split: the structure #13 transcribes."
provenance: [T]
sources:
  - "papers/conjugate-special-relativity.md §1"
  - "papers/conjugate-special-relativity.md §2"
  - "papers/conjugate-special-relativity.md §3"
  - "papers/conjugate-special-relativity.md §4"
  - "papers/conjugate-special-relativity.md §5"
  - "papers/conjugate-special-relativity.md §6"
---

*Special relativity is Einstein's 1905 theory of how measurements of length and time compare between observers moving at constant velocity relative to one another, built on one speed that all of them measure alike, the speed of light c. Its machinery (boosts, the light cone, time dilation, length contraction and the mass shell) is textbook physics. The program uses it as a template: the paper #13 copies each piece into the momentum polarization, with force in place of velocity and a maximum force c̃ in place of c. This page states the template; the copies are on the pages listed under Used by.*

**Status:** Established — [T] — textbook physics, written here from general knowledge; #13's transcriptions carry their own tags and are alive but unreviewed.

## Key facts

- **Boosts.** A boost with velocity v along x maps x′ = γ(x − vt), t′ = γ(t − vx/c²), with γ = (1 − v²/c²)^{−1/2} [T]. #13 §2's force boost replaces x by p, v by F and c by c̃ ([Force boosts and force composition](/wiki/conjugate-relativity/force-boosts)).
- **Rapidity and velocity addition.** Writing v = c tanh φ, rapidities add under successive boosts along one direction, so velocities compose as v₁ ⊕ v₂ = (v₁ + v₂)/(1 + v₁v₂/c²) and never exceed c [T]. #13 §2 copies this with F = c̃ tanh φ, so that forces "saturate at c̃".
- **Interval, light cone, Lorentz group.** The interval ds² = c²dt² − dx² is the same for all inertial observers; the transformations that preserve it form the Lorentz group, and its null cone separates the events a signal can reach from those it cannot [T]. #13 §1: "Ours bounds trajectories x(t): |dx/dt| ≤ c"; #13 §2 sets beside it the dual interval ds̃² = c̃²dt² − dp² ([Two causal cones](/wiki/conjugate-relativity/two-causal-cones)).
- **Simultaneity, time dilation, length contraction.** Events simultaneous for one observer are not simultaneous for another moving relative to it; a moving clock's proper time runs as dτ = dt√(1 − v²/c²); a moving body is shorter by the factor γ along its motion [T]. #13 transcribes all three: simultaneity across momentum (§2), force dilation and the contraction of momentum spread (§3) ([Force dilation](/wiki/conjugate-relativity/force-dilation)).
- **The mass shell and E = mc².** A free particle's four-momentum satisfies p_μp^μ = m²c² in every frame, and at rest its energy is E = mc² [T]. #13 §4: "Our invariant hypersurface is the mass shell, p_μp^μ = m²c²"; its Born image is the [invariant-length shell](/wiki/conjugate-relativity/invariant-length-shell), and "The dual E = mc² returns the right corner of physics."
- **The Galilean limit and inertia.** For v ≪ c, γ − 1 ≈ ½(v/c)², boosts reduce to Galilean transformations, velocities add, and passing to an accelerated frame introduces pseudo-forces; Newton's first law, that an undisturbed body keeps its velocity, picks out the inertial frames [T]. #13 §2: "Force *looks* exactly additive for the same reason velocity looked exactly additive before 1905"; #13 §5's dual first law: "an undisturbed system maintains its state of force" ([Dual inertia: free fall as rest](/wiki/conjugate-relativity/dual-inertia)).
- **The 3+1 split and energy–time conjugacy.** The 3+1 split separates spacetime into one time direction and three space directions, and in quantum mechanics energy is conjugate to time as momentum is to position [T]. #13 keeps time shared between the two polarizations ("the time coordinate (in the 3+1 presentation used here)", §6); the construction that would also exchange time and energy is [open](/wiki/conjugate-relativity/four-dimensional-born-map).

## Used by

- [Two causal cones](/wiki/conjugate-relativity/two-causal-cones) — the null cone of a metric, copied to momentum space.
- [The maximum force c̃ = c⁴/G](/wiki/conjugate-relativity/maximum-force) — the dual cone's invariant speed, in the role of c.
- [Force boosts and force composition](/wiki/conjugate-relativity/force-boosts) — boosts, rapidity, simultaneity and the Galilean limit, with F in place of v.
- [Force dilation](/wiki/conjugate-relativity/force-dilation) — time dilation and length contraction.
- [The invariant-length shell and Planck closure](/wiki/conjugate-relativity/invariant-length-shell) — the mass shell and E = mc².
- [Dual inertia: free fall as rest](/wiki/conjugate-relativity/dual-inertia) — inertial frames and Newton's first law.
- [Open: the four-dimensional Born map and dual dynamics](/wiki/conjugate-relativity/four-dimensional-born-map) — the 3+1 split it would replace.

## Sources

- `papers/conjugate-special-relativity.md` §1–§6 — the transcriptions named above: the two cones (§1); boosts, composition, simultaneity and the Galilean limit (§2); force dilation and momentum-spread contraction (§3); the mass shell (§4); the dual first law (§5); the 3+1 presentation (§6).
