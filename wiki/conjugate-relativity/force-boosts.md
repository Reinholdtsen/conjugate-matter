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
  - "papers/conjugate-special-relativity.md §1"
  - "papers/broken-born-checkpoint-v2.md §13"
  - "HANDOFF.md §2"
  - "popsci/universes-other-half.md 'A second speed of light'"
  - "review/wiki-build-flags.md item 56"
  - "notes/velocity-gated-gravity.md §2"
---

*A force boost is the momentum-space counterpart of a [Lorentz boost](/wiki/conjugate-relativity/special-relativity): where Einstein's boost relates observers moving at constant velocity, the force boost of [#13](/wiki/conjugate-relativity) relates an observer under no force to one under a constant force, with the [maximum force c̃](/wiki/conjugate-relativity/maximum-force) in the role of the speed of light. The same algebra then gives forces that combine like relativistic velocities, so that no composition of forces passes c̃, and observers under different forces who disagree about which events are simultaneous when the events differ in momentum. At what #13 calls the strongest sustained macroscopic force in nature, on a kilogram at a neutron-star surface, the correction is of order 10⁻⁶⁵, which #13 gives as the reason force looks exactly additive; only merging black holes approach the limit. The results are alive but unreviewed: #13 tags them as derived, but no review round or script has checked them, the [checkpoint #11](/wiki/history/documents/checkpoint) does not mention them, and no observable signature in merger data has been derived.*

**Status:** Alive, unreviewed — the dual Lorentz group [D — structural], the composition law [D], force boosts and γ̃ on §7's fixed [D] list, simultaneity untagged, the merger arena [O — flagged, not derived] — all as #13 tags them; no [blind review](/wiki/method/review) round has examined #13, no `verify/` script checks the formulas or the 10⁻⁶⁵ estimate ([the iron rule](/wiki/method/verification/iron-rule)), and #11 v2.3 does not mention them.

## The dual interval and the dual Lorentz group

The force boosts rest on an interval built from time and momentum. #13 §2:

> "The dual interval on (t, **p**) is ds̃² = c̃²dt² − d**p**², preserved by rotations in the (c̃t, p) planes — the dual Lorentz group [D — structural]."

It is the Minkowski interval ds² = c²dt² − dx² of [special relativity](/wiki/conjugate-relativity/special-relativity) with the position x replaced by the momentum p and c by the maximum force c̃ ([The maximum force c̃ = c⁴/G](/wiki/conjugate-relativity/maximum-force)). Its null directions are the dual cone of [Two causal cones](/wiki/conjugate-relativity/two-causal-cones), |dp/dt| = c̃. The "rotations in the (c̃t, p) planes" are rotations in the Lorentzian sense: as an ordinary boost is a hyperbolic rotation of the (ct, x) plane [T], each one mixes c̃t with one direction of momentum. Together with the ordinary rotations of the momentum directions among themselves they form the dual Lorentz group. "[D — structural]" is one of #13's qualified forms of the derived tag, which #13 does not define ([provenance tags](/wiki/method/provenance-tags)).

The interval is the 3+1 form: time is shared between [the two polarizations](/wiki/phase-space/reciprocity/lagrangian-polarizations) and only position and momentum trade places. #13 §6 uses a different dual cone, and which construction governs is open ([Open: the two dual cones](/wiki/conjugate-relativity/two-cones-inconsistency)).

## The force boost

#13 §2: "A dual boost of parameter F carries the force-free frame to a uniformly forced one:"

```text
p′ = γ̃(p − F t),    t′ = γ̃(t − F·p/c̃²),    γ̃ = (1 − F²/c̃²)^{−1/2}
```

The template is the Lorentz boost x′ = γ(x − vt), t′ = γ(t − vx/c²), and the dictionary is

| Lorentz boost [T] | Force boost (#13 §2) |
| --- | --- |
| position x | momentum p |
| velocity v = dx/dt | force F = dp/dt |
| speed of light c | maximum force c̃ |
| Lorentz factor γ | dual Lorentz factor γ̃ |
| frame moving at constant v | frame under constant force F |

In the template, a body at rest in the original frame is seen from the boosted frame to move at −v. In the transcription, a system on which no force acts, whose momentum is constant, is seen from the forced frame to be under the force −F; for small F this is the pseudo-force of an accelerated frame, as the Galilean limit below shows. The dual Lorentz factor γ̃ is 1 for F = 0 and grows without bound as F approaches c̃, so no force boost reaches the maximum force. #13 §7 lists "force boosts, γ̃" in its "Kinematic structure fixed [D]".

## Relativity of simultaneity across momentum

#13 §2, item 1, untagged:

> "Events at equal t but different p are non-simultaneous in a forced frame — simultaneity depends on momentum location as, for us, it depends on position."

The term F·p/c̃² in the transformation of t is the dual of vx/c² in the Lorentz boost. Reading it off the formula, two events at the same t but at momenta differing by Δp along F are separated in the forced frame by Δt′ = −γ̃FΔp/c̃², as two events at the same t but a distance Δx apart are separated by Δt′ = −γvΔx/c² in the template [T]. #13 states the consequence in words only. It is not on §7's fixed list.

## Force composition [D]

#13 §2, item 2:

> "With dual rapidity F = c̃ tanh φ and rapidities additive,"

```text
F₁ ⊕ F₂ = (F₁ + F₂)/(1 + F₁F₂/c̃²)
```

> "so forces saturate at c̃ rather than accumulate without bound [D]."

The steps are those of relativistic velocity addition [T]:

1. **Dual rapidity.** Each force boost is labelled by φ with F = c̃ tanh φ; then γ̃ = cosh φ, and the boost is a hyperbolic rotation of the (c̃t, p) plane through φ.
2. **Rapidities add.** Two force boosts along one direction compose into one with φ = φ₁ + φ₂, as two rotations about one axis compose by adding angles.
3. **The addition formula.** tanh(φ₁ + φ₂) = (tanh φ₁ + tanh φ₂)/(1 + tanh φ₁ tanh φ₂). Multiplying by c̃ and writing Fᵢ = c̃ tanh φᵢ gives the composition law.
4. **Saturation.** |tanh φ| < 1 for every finite φ, so any number of compositions of forces below c̃ stays below c̃, and composing any force with c̃ returns c̃. When both forces are small compared with c̃ the denominator is close to 1 and the forces add.

In the template, v₁ ⊕ v₂ is a body's velocity in the original frame when it moves at v₂ relative to a frame that itself moves at v₁. The transcribed meaning is the force on a system, seen from the force-free frame, when it is under F₂ relative to a frame that is itself under F₁; #13 states the law and its saturation and does not spell out the setting. It writes the law for forces along one line and gives no form for forces in different directions. The popular article #12 describes the law as "two forces applied together yield less than their arithmetic sum"; #12 is not a source for status ([The popular articles (#10, #12)](/wiki/history/documents/popular-articles)).

## The Galilean limit: why force looks additive

#13 §2, item 3, is titled "The Galilean limit is everything we know":

> "For F ≪ c̃ the transformation reduces to the ordinary passage to an accelerated frame, with its familiar pseudo-forces, and composition reduces to addition. The strongest sustained macroscopic force in nature — on a kilogram at a neutron-star surface, ~10¹² N — gives γ̃ − 1 ≈ ½(F/c̃)² ~ 10⁻⁶⁵. Force *looks* exactly additive for the same reason velocity looked exactly additive before 1905: no accessible process approaches the limit."

The reduction follows the template [T]. For F much smaller than c̃, γ̃ is close to 1, with γ̃ − 1 ≈ ½(F/c̃)², and the term F·p/c̃² is negligible, so the boost becomes p′ = p − Ft, t′ = t. Momenta shift at the steady rate F and time is common to both frames, as the Galilean x′ = x − vt, t′ = t shifts positions at the steady rate v. In an accelerated frame of Newtonian mechanics a body's momentum shifts in the same way, and the shift is what appears as a pseudo-force ([Special relativity: the template](/wiki/conjugate-relativity/special-relativity)). The composition law's denominator tends to 1 and forces add.

The size of the correction comes from the weight of one kilogram at a neutron-star surface, about 10¹² N in #13's figure, set against c̃ ≈ 1.2 × 10⁴⁴ N; #13 gives the result as γ̃ − 1 ~ 10⁻⁶⁵ and lists "γ̃ − 1 ~ 10⁻⁶⁵ at neutron-star forces" among the §7 numerical anchors. Neither the force nor the correction is reproduced by a `verify/` script, as the iron rule requires. The argument is the one that explains why Newtonian velocity addition went unchallenged until 1905: the corrections scale as the square of the ratio to the limit, and no accessible process comes near it. #12 repeats the numbers in popular form.

## Open: merger-band corrections

#13 §2, item 3, continues:

> "The single natural exception is a comparable-mass black-hole merger, which operates at F ~ c̃ by construction; if dual-kinematic corrections have any observable expression, merger and ringdown dynamics are where they would be order unity [O — flagged, not derived]."

A merger of two black holes of comparable mass runs through three stages [T]: the inspiral, in which the orbit shrinks as it radiates gravitational waves; the merger itself; and the ringdown, in which the single remnant settles into a stationary black hole with damped oscillations. Gravitational-wave detectors record all three. #13 §1 notes that the literature's companion luminosity bound c⁵/4G is "approached by binary black-hole mergers" ([Maximum force and maximal acceleration in the literature](/wiki/conjugate-relativity/maximum-force-conjectures)); #13 gives no estimate behind "F ~ c̃ by construction".

#13's own §5 gives a different answer for this arena. §2 says a black-hole merger "operates at F ~ c̃ by construction", using the gravitational force between the holes; §5 identifies dual rest with free fall, and merging black holes are in free fall, so under §5 their dual-kinematic correction is zero. For the Sun and Earth the two readings give (1/2)(F/c̃)² = 4.3×10⁻⁴⁴ and 0: "both are negligible, but the paper gives two answers" (flag 56 in `review/wiki-build-flags.md`, rated low; raised by 1 agent, the run-3 theory verifier of the momentum-gravity investigation, and upheld by its final critic; `notes/velocity-gated-gravity.md` §2; [X between ordinary bodies](/wiki/gravity/momentum-graviton/ordinary-bodies#two-other-readings-of-momentum-gravity)). It awaits Paul's ruling.

The tag says what is and is not claimed: the arena is flagged, and no correction has been derived. #13 §7 lists the question among its open items, "whether merger-band gravitational-wave data can bound dual-kinematic corrections", and the Abstract says the construction "locates the one natural arena where dual-kinematic corrections could be order unity". No signature has been computed, #11 §13's table of predictions has no row for dual kinematics ([Predictions and kill conditions](/wiki/predictions)), and the item is not among #11 §14's open problems or on the current queue in `CLAUDE.md`. It is listed in [Open problems and the queue](/wiki/status/open-problems).

## Standing

#13 tags the dual Lorentz group and the composition law as derived and lists the force boosts among its fixed results. Each is a transcription of special relativity under x → p, v → F, c → c̃, stated without further steps. No blind review round has examined #13, no `verify/` script checks its formulas or its numbers, and #11 v2.3 mentions neither force boosts nor the maximum force. `HANDOFF.md` §2 lists "force boosts" under dual special relativity among the alive results, without a machine-check mark. The results are alive and unreviewed ([Conjugate special relativity](/wiki/conjugate-relativity)).

## Sources

- `papers/conjugate-special-relativity.md` §2 — the dual interval, the force boost, simultaneity, composition, the Galilean limit and the merger arena; §7 for the fixed list, the anchor and the open item; Abstract for "short of black-hole mergers" and the arena; §1 for the companion luminosity.
- `papers/broken-born-checkpoint-v2.md` §13 — the predictions table, which has no dual-kinematic row.
- `HANDOFF.md` §2 — force boosts among the alive results, without a machine-check mark.
- `popsci/universes-other-half.md` 'A second speed of light' — the popular description of composition and of the numbers (not a status source).
- `review/wiki-build-flags.md` item 56 — #13 §2 against §5 on gravitating pairs (low), awaiting Paul's ruling; `notes/velocity-gated-gravity.md` §2 — the two answers for the Sun and Earth
