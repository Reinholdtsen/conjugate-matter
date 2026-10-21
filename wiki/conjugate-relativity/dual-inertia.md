---
title: "Dual inertia: free fall as rest"
weight: 80
status: alive
description: "Trajectories of constant dp/dt are dual-inertial: free fall is rest and uniform force is uniform dual motion; the dual Newton's laws are conjecture-tier."
provenance: [D]
sources:
  - "papers/conjugate-special-relativity.md §5"
  - "papers/conjugate-special-relativity.md §1"
  - "papers/conjugate-special-relativity.md §2"
  - "papers/conjugate-special-relativity.md §4"
  - "papers/conjugate-special-relativity.md §6"
  - "papers/conjugate-special-relativity.md §7"
  - "HANDOFF.md §2"
  - "popsci/universes-other-half.md 'A second speed of light'"
---

*Dual inertia is #13's account of rest and uniform motion in the momentum polarization, the mirror description in which momentum plays the part that position plays for ordinary matter. An ordinary inertial body keeps its velocity constant. In #13's dual kinematics the rate of motion through momentum space, dp/dt, is a force, and it takes the place of velocity, so the dual-inertial motions are those of constant force: zero force, which in general relativity is free fall, and a constant nonzero force, which is a uniformly accelerated (Rindler) frame. In #13's words, "An astronaut coasting in orbit is, to the momentum polarization, at rest." The identification of dual-inertial frames with free fall is on #13's list of fixed results; the dual laws of motion built on it are marked conjecture-tier, and their formalization waits on dynamics that have not been written. Like the rest of #13, the material is unreviewed and unchecked by script, and the checkpoint #11 does not mention it.*

**Status:** Alive, unreviewed — the dual-inertial = free-fall identification is in #13 §7's fixed [D] list (it is untagged in §5); the dual Newton's laws are "conjecture-tier", #13's own label and not one of the house tags. The [D] is #13's own: no review round has covered #13, no `verify/` script checks it, and [#11](/wiki/history/documents/checkpoint) v2.2 does not mention it.

## Background: inertia, free fall and Rindler frames [T]

- **Inertial frames.** Newton's first law says that a body on which no force acts keeps a constant velocity; the frames in which this holds are the inertial frames. Special relativity keeps them and states its principle of relativity for them: the laws of physics take the same form in every inertial frame, and the frames are related by Lorentz boosts ([special relativity: the template](/wiki/conjugate-relativity/special-relativity)).
- **Two readings of free fall.** In Newtonian mechanics gravity is a force: a body falling near the Earth's surface has momentum changing at the rate mg. In [general relativity](/wiki/gravity/spin-2-fields/general-relativity) gravity is the curvature of spacetime, and a freely falling body follows a geodesic, the straightest path available, with no force acting on it; an accelerometer it carries reads zero. An astronaut in orbit is in free fall in this sense.
- **Rindler frames.** A frame accelerating uniformly through flat spacetime is a Rindler frame. An observer at rest in it carries a constant proper acceleration, so a constant force has to act on it, and by the equivalence principle it is locally indistinguishable from an observer held at rest in a uniform gravitational field.

## The dual-inertial class

#13 §1 gives momentum space its own light cone, which bounds the rate dp/dt of a trajectory p(t) by the maximum force c̃ ([two causal cones](/wiki/conjugate-relativity/two-causal-cones)). In that kinematics dp/dt plays the role that velocity dx/dt plays in ours. #13 §5 draws the consequence for inertia:

> "The dual-inertial class consists of trajectories with dp/dt constant: rest (dp/dt = 0, i.e., force-free motion — our free fall) and uniform dual motion (constant force — our Rindler frames)."

The transcription, term by term:

| Ordinary kinematics | Dual kinematics (#13 §5) |
| --- | --- |
| the rate of motion is the velocity dx/dt | the rate of motion is the force dp/dt |
| rest: dx/dt = 0 | rest: dp/dt = 0, "force-free motion — our free fall" |
| uniform motion: constant velocity | "uniform dual motion (constant force — our Rindler frames)" |
| inertial frames are related by Lorentz boosts | uniformly forced frames are related to force-free ones by force boosts |
| inertia resists changes of velocity | inertia resists changes of force (§5's plain passage) |

The fourth row comes from #13 §2: "A dual boost of parameter F carries the force-free frame to a uniformly forced one" ([force boosts and force composition](/wiki/conjugate-relativity/force-boosts)). As in special relativity, where all inertial frames are equivalent and a boost relates any two, the dual-inertial frames form one class: dual rest and uniform dual motion differ by a dual boost, as ordinary rest and uniform motion do.

#13 §5's plain-language passage gives the picture: "An astronaut coasting in orbit is, to the momentum polarization, at rest." It describes dual uniform motion as constant force, and dual inertia as resistance "not to acceleration but to *changes* in force" (the emphasis is #13's).

#13 §7 lists the "dual-inertial = free-fall identification" among the "Kinematic structure fixed [D]". In §5 itself the identification carries no tag.

### Which reading of free fall

The identification "force-free motion — our free fall" uses the general-relativistic reading of free fall, in which no force acts on a falling body. In the Newtonian reading the falling body's momentum changes, at a rate set by its weight [T]. #13 does not discuss the choice; its §6 states that "the massless graviton" is shared by both polarizations, "so both polarizations fall identically" ([the equivalence principle as dual relativity](/wiki/conjugate-relativity/equivalence-principle)).

### Which time

The rate dp/dt is taken with respect to a time t that both polarizations share. That is #13's 3+1 presentation, in which space and momentum trade places and time is left alone (§6). The fully four-dimensional version, in which time and energy also trade places, is open ([Open: the four-dimensional Born map and dual dynamics](/wiki/conjugate-relativity/four-dimensional-born-map)), and #13 uses two different dual cones in different sections ([Open: the two dual cones](/wiki/conjugate-relativity/two-cones-inconsistency)).

## Conjecture: the dual laws of motion

#13 §5 continues the transcription to Newton's first two laws:

> "The dual first law: an undisturbed system maintains its state of force. The dual second law, structurally, makes λ_χ the measure of resistance to force-*change* [conjecture-tier; the full dual dynamics awaits the formalization of §6]."

- **The first law.** Newton's first law says that an undisturbed body keeps its state of motion. The dual law says that an undisturbed system keeps its state of force: it stays in the dual-inertial class.
- **The second law.** In Newton's second law mass measures resistance to a change of velocity. The dual law gives that role to λ_χ, the invariant extent that #13 §4 assigns to conjugate quanta ([the invariant-length shell](/wiki/conjugate-relativity/invariant-length-shell)), as the resistance to a change of force. #13 writes no equation for it.
- **The tier.** "Conjecture-tier" is not one of the program's tags ([provenance tags and citation marks](/wiki/method/provenance-tags)); the tag text says why the laws are not derived: "the full dual dynamics awaits the formalization of §6". §6's open item is the four-dimensional Born map, "a required step before the dual dynamics (their Maxwell, their field theory) can be written". The dual laws are not on §7's fixed list.

The register of conjectures lists the dual second law among the conjecture-tier statements inside the record ([conjectures: chat-only and popsci-only claims](/wiki/status/conjectures)).

## What follows

The dual principle of relativity, in #13's words the "equivalence of all force-free frames", is then a statement about freely falling frames. #13 §5 records it as the equivalence principle reached from kinematics [D — structural] ([the equivalence principle as dual relativity](/wiki/conjugate-relativity/equivalence-principle)).

## The popular version

The popular article #12 ("A second speed of light") states the identification as settled: "To be at rest in the momentum description is to feel no force — which, in our description, is free fall." #12 presents the framework as if confirmed and is never a source for status ([the popular articles](/wiki/history/documents/popular-articles)).

## Basis of the status

`HANDOFF.md` §2 lists "dual inertial frames = free fall ⇒ equivalence principle as the dual relativity principle" among the alive results, without the ✓ it uses for machine-verified items. #13 has not been revised since its import on 2026-10-19 and has not been through a review round, and #11 v2.2 does not mention it ([conjugate special relativity](/wiki/conjugate-relativity)).

## Sources

- `papers/conjugate-special-relativity.md` §5 — the dual-inertial class, the astronaut, the dual first and second laws; §1 for the dual cone; §2 for the force boost to a uniformly forced frame; §4 for λ_χ; §6 for the shared time, the shared graviton and the open four-dimensional map; §7 for the fixed list.
- `HANDOFF.md` §2 — the alive listing.
- `popsci/universes-other-half.md` 'A second speed of light' — the popular statement (not a status source).
