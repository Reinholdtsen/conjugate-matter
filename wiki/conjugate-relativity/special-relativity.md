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
  - "papers/conjugate-special-relativity.md §7"
  - "review/wiki-build-flags.md item 30"
---

*Special relativity is Einstein's 1905 theory of how measurements of length and time compare between observers moving at constant velocity relative to one another, built on one speed that all of them measure alike, the speed of light c. Its machinery (boosts, the light cone, the relativity of simultaneity, time dilation, length contraction and the mass shell) is textbook physics. The program uses it as a template: the paper [#13](/wiki/conjugate-relativity) copies each piece into the [momentum polarization](/wiki/phase-space/reciprocity/lagrangian-polarizations), the program's mirror description in which momentum plays the role of position, with force in place of velocity and a [maximum force c̃](/wiki/conjugate-relativity/maximum-force) in place of c. This page states the template and lists the copies; #13 tags most of its copies as derived, but no review round or script has checked them, and the [checkpoint #11](/wiki/history/documents/checkpoint) does not mention them.*

**Status:** Established — [T] — textbook physics, written here from general knowledge; #13 cites no source for it, and the references below are added from model memory (†). #13's transcriptions carry the tags #13 itself assigns ([D — structural], [D], or none); #13 has never been through a [blind review](/wiki/method/review) round, no `verify/` script checks any of its formulas or numbers, and #11 v2.3 does not mention it.

## Two postulates [T]

Special relativity rests on two postulates (Einstein 1905†). The first is the principle of relativity: the laws of physics take the same form in every inertial frame, a frame in which a body acted on by no force moves in a straight line at constant speed. The second is the invariance of the speed of light: light in vacuum moves at the same speed c in every inertial frame, whatever the motion of its source. The rest of the theory follows from asking which transformations between inertial frames respect both postulates.

## Boosts and the Lorentz factor [T]

Let a frame S′ move at velocity v along the x axis of a frame S, with the origins coinciding at t = t′ = 0. The coordinates of one event in the two frames are related by the Lorentz boost

```text
x′ = γ(x − vt),    t′ = γ(t − vx/c²),    γ = (1 − v²/c²)^{−1/2}
```

with the transverse coordinates unchanged. The Lorentz factor γ equals 1 at v = 0 and grows without bound as v approaches c, so no boost reaches c. The term vx/c² in the second equation mixes position into time; it is the origin of the relativity of simultaneity below.

#13 §2's force boost is this formula with x replaced by the momentum p, v by a force F and c by the maximum force c̃: p′ = γ̃(p − Ft), t′ = γ̃(t − F·p/c̃²) ([Force boosts and force composition](/wiki/conjugate-relativity/force-boosts)).

## Rapidity and the composition of velocities [T]

Writing v = c tanh φ defines the rapidity φ. Then γ = cosh φ and γv/c = sinh φ, and the boost takes the form

```text
ct′ = ct cosh φ − x sinh φ,    x′ = x cosh φ − ct sinh φ
```

which is a hyperbolic rotation of the (ct, x) plane through φ. Two successive boosts along one axis compose by adding their rapidities, φ = φ₁ + φ₂, as two rotations about one axis compose by adding their angles. The addition formula of the hyperbolic tangent,

```text
tanh(φ₁ + φ₂) = (tanh φ₁ + tanh φ₂)/(1 + tanh φ₁ tanh φ₂)
```

then gives the composition of velocities:

```text
v₁ ⊕ v₂ = (v₁ + v₂)/(1 + v₁v₂/c²)
```

Here v₂ is a body's velocity measured in a frame that itself moves at v₁, and v₁ ⊕ v₂ is the body's velocity in the original frame. Because |tanh φ| < 1 for every finite φ, any number of compositions of speeds below c stays below c, and composing any velocity with c returns c. When both speeds are small compared with c the denominator is close to 1 and the velocities add.

#13 §2 copies this with "dual rapidity F = c̃ tanh φ": forces compose by the same law, "so forces saturate at c̃ rather than accumulate without bound [D]".

## The interval and the light cone [T]

The quantity

```text
ds² = c²dt² − dx²
```

where dx² is the squared length of the spatial displacement, takes the same value in every inertial frame. The linear transformations that preserve it form the Lorentz group; the boosts and the rotations of space generate its connected part, and the reflections of space and time make up the rest. The sign of ds² sorts the separations between events:

- **timelike** (ds² > 0): a body moving slower than light can be present at both events;
- **spacelike** (ds² < 0): no signal can connect them;
- **null** (ds² = 0): a light ray connects them.

The null directions from an event form its light cone, the boundary between the events it can influence and those it cannot. For a trajectory x(t), staying inside the cone is the condition |dx/dt| ≤ c, so the speed limit is a property of the cone. The interval is the Minkowski metric. Its signature is Lorentzian: time enters with the opposite sign to space. A positive-definite (Euclidean) metric has no null directions and therefore no cone.

#13 §1 begins from this: "Ours bounds trajectories x(t): |dx/dt| ≤ c." Its dual interval is ds̃² = c̃²dt² − dp² (§2), and its dual cone bounds |dp/dt| by c̃ ([Two causal cones](/wiki/conjugate-relativity/two-causal-cones)).

## Simultaneity, proper time and length contraction [T]

Three effects follow from the boost.

- **The relativity of simultaneity.** Two events with Δt = 0 in S, a distance Δx apart along the boost, are separated in S′ by Δt′ = −γvΔx/c². Whether two events are simultaneous depends on the frame, and the disagreement grows with their separation in position.
- **Proper time and time dilation.** A clock carried along a trajectory x(t) reads its proper time,

  ```text
  dτ = ds/c = dt √(1 − v²/c²),    v = |dx/dt|
  ```

  so a moving clock runs slow by the factor γ relative to the coordinate time of the frame. The rate depends on the clock's speed, not on its acceleration.
- **Length contraction.** A rod of length L₀ in its rest frame, measured in a frame in which it moves at v along its length, has length L₀/γ; its transverse dimensions are unchanged.

#13 transcribes all three: simultaneity that depends on momentum (§2), force dilation and the contraction of a forced system's momentum spread (§3) ([Force dilation](/wiki/conjugate-relativity/force-dilation)).

## Four-momentum, the mass shell and E = mc² [T]

A particle's energy E and momentum p combine into the four-momentum p^μ = (E/c, p), whose invariant square is

```text
p_μ p^μ = E²/c² − p² = m²c²
```

The value is the same in every frame. The four-momenta it allows form a hyperboloid in energy–momentum space, the mass shell, labelled by the invariant mass m. At rest, p = 0 and the energy is E = mc². For a massless particle such as the photon the hyperboloid degenerates to the cone E = c|p|, the light cone drawn in energy–momentum space.

#13 §4: "Our invariant hypersurface is the mass shell, p_μp^μ = m²c²". Its Born image, a hyperboloid in position space, is the [invariant-length shell](/wiki/conjugate-relativity/invariant-length-shell), and the dual rest-energy relation E = λc̃ is #13's counterpart of E = mc²: "The dual E = mc² returns the right corner of physics." #13 §6 calls the massless cone E = c|p| "the dual null cone", which is one of two different dual cones in the paper ([Open: the two dual cones](/wiki/conjugate-relativity/two-cones-inconsistency)).

## The Galilean limit, accelerated frames and inertia [T]

For v much smaller than c, γ − 1 ≈ ½(v/c)², and the boost reduces to the Galilean transformation x′ = x − vt, t′ = t. Time is then common to all frames and velocities add. These are the kinematics of Newton's mechanics, and they described every velocity measurement until the speeds involved approached c.

Newton's first law, that a body on which no force acts keeps its velocity, picks out the inertial frames. In a frame accelerating uniformly at a relative to an inertial one, x′ = x − ½at², and a body of mass m on which no force acts appears to feel a pseudo-force −ma: its momentum in the accelerated frame changes as p′ = p − mat. A frame accelerating uniformly in special relativity, with constant acceleration as measured in its own instantaneous rest frame, is a Rindler frame ([Rindler frames](/wiki/gravity/spin-2-fields/equivalence-principle#rindler-frames)).

#13 §2 transcribes the limit: "For F ≪ c̃ the transformation reduces to the ordinary passage to an accelerated frame, with its familiar pseudo-forces, and composition reduces to addition", and "Force *looks* exactly additive for the same reason velocity looked exactly additive before 1905". #13 §5 transcribes the first law, "The dual first law: an undisturbed system maintains its state of force", and reads uniform dual motion as "constant force — our Rindler frames" ([Dual inertia: free fall as rest](/wiki/conjugate-relativity/dual-inertia)).

## The 3+1 split and energy–time conjugacy [T]

Writing spacetime as one time direction and three space directions is the 3+1 split. It belongs to a choice of frame, not to the theory, since boosts mix t with x. In quantum mechanics energy is conjugate to time as momentum is to position: a state's dependence on time and its spread of energies are Fourier partners, as a signal and its frequency spectrum are, just as a wavefunction in position and its momentum spectrum are ([the Fourier transform as a phase-space rotation](/wiki/phase-space/reciprocity/fourier-transform)). The four-momentum (E/c, p) is conjugate in this sense to the four-position (ct, x).

[Born reciprocity](/wiki/phase-space/reciprocity/born-reciprocity), as the program uses it, exchanges position and momentum and leaves time alone. #13 works in that setting and says so: the two polarizations share "the time coordinate (in the 3+1 presentation used here)" (§6). The construction that would also exchange time and energy, which #13 calls "the natural home of this paper's kinematics", is open ([Open: the four-dimensional Born map and dual dynamics](/wiki/conjugate-relativity/four-dimensional-born-map)).

## How #13 transcribes the template

#13 builds each piece of its dual kinematics by the substitutions x → p, v = dx/dt → F = dp/dt and c → c̃. The table pairs each piece of special relativity with its transcription and gives the tag #13 attaches.

| Special relativity [T] | #13's transcription | Where | Tag in #13 |
| --- | --- | --- | --- |
| light cone, \|dx/dt\| ≤ c | dual cone, \|dp/dt\| ≤ c̃ | §1 | [D — compatibility theorem], on the block form H = diag(g, g⁻¹) it starts from; queried in flag 30 of `review/wiki-build-flags.md` |
| the speed c | the maximum force c̃ = c⁴/G | §1 | none on the boxed value; a "numerical anchor" in §7 |
| interval c²dt² − dx², Lorentz group | dual interval c̃²dt² − dp², dual Lorentz group | §2 | [D — structural] |
| Lorentz boost and γ | force boost and γ̃ | §2 | on §7's fixed [D] list |
| velocity composition | force composition | §2 | [D] |
| simultaneity across position | simultaneity across momentum | §2 | none |
| Galilean limit | ordinary passage to an accelerated frame | §2 | none; γ̃ − 1 ~ 10⁻⁶⁵ is a §7 anchor |
| time dilation | force dilation | §3 | [D — structural; which physical clocks respond is polarization-dependent, O] |
| length contraction | contraction of momentum spread | §3 | none |
| mass shell, invariant mass m | invariant-length shell, invariant length λ_χ | §4 | [D — structural] |
| E = mc² | E = λc̃, [the Planck energy](/wiki/gravity/spin-2-fields/planck-units) at λ = l_P | §4 | [D] |
| inertial frames | dual-inertial frames: free fall and Rindler frames | §5 | on §7's fixed [D] list |
| the principle of relativity | [the equivalence principle](/wiki/conjugate-relativity/equivalence-principle) | §5 | [D — structural] |

The template is established; the transcriptions are not. #13 states each one without intermediate steps beyond the substitution, and §7 lists the kinematic structure as "fixed [D]". No blind review round has examined #13, no `verify/` script reproduces any of its formulas or numbers ([the iron rule](/wiki/method/verification/iron-rule)), and #11 v2.3 does not mention the maximum force or the dual kinematics. The section's status, alive and unreviewed, rests on `HANDOFF.md` §2 and on `CLAUDE.md`'s listing of #13 as a current reference ([Conjugate special relativity](/wiki/conjugate-relativity)).

## References

#13 cites no source for special relativity. Added by the wiki from model memory (†):

- A. Einstein (1905)†: the two postulates, the boost, time dilation and length contraction; E = mc² followed in a second paper the same year.
- H. Minkowski†: the interval, and spacetime as a four-dimensional geometry.
- E. F. Taylor and J. A. Wheeler, *Spacetime Physics*†; W. Rindler, *Relativity: Special, General, and Cosmological*†: textbooks covering rapidity, the light cone and uniformly accelerated frames.

## Used by

- [Two causal cones](/wiki/conjugate-relativity/two-causal-cones) — the null cone of a metric, copied to momentum space.
- [The maximum force c̃ = c⁴/G](/wiki/conjugate-relativity/maximum-force) — the dual cone's invariant speed, in the role of c.
- [Force boosts and force composition](/wiki/conjugate-relativity/force-boosts) — boosts, rapidity, simultaneity and the Galilean limit, with F in place of v.
- [Force dilation](/wiki/conjugate-relativity/force-dilation) — time dilation and length contraction.
- [The invariant-length shell and Planck closure](/wiki/conjugate-relativity/invariant-length-shell) — the mass shell and E = mc².
- [Dual inertia: free fall as rest](/wiki/conjugate-relativity/dual-inertia) — inertial frames, Newton's first law and Rindler frames.
- [The equivalence principle as dual relativity](/wiki/conjugate-relativity/equivalence-principle) — the principle of relativity.
- [Open: the two dual cones](/wiki/conjugate-relativity/two-cones-inconsistency) — the massless shell E = c|p|, which #13 §6 calls the dual null cone.
- [Open: the four-dimensional Born map and dual dynamics](/wiki/conjugate-relativity/four-dimensional-born-map) — the 3+1 split it would replace.
- [Row 6: the exactly massless graviton](/wiki/predictions/massless-graviton) — the energy–momentum relation of a massive particle, behind the graviton-mass bounds.
- [Row 9: no linear photon dispersion](/wiki/predictions/photon-dispersion) — exact Lorentz invariance and the vacuum relation E = c|p|, behind the row's standard expectation.

## Sources

- `papers/conjugate-special-relativity.md` §1–§6 — the transcriptions named above: the two cones (§1); boosts, composition, simultaneity and the Galilean limit (§2); force dilation and momentum-spread contraction (§3); the mass shell and E = λc̃ (§4); the dual first law and Rindler frames (§5); the 3+1 presentation and the dual null cone E = c|p| (§6).
- `papers/conjugate-special-relativity.md` §7 — the fixed [D] list, the numerical anchors and the open items.
- `review/wiki-build-flags.md` item 30 — #13 §1's tag [D — compatibility theorem] on the block form from which it reads cones that the theorem's positive-definite g cannot have; a question of tagging convention in the flags' audit.
