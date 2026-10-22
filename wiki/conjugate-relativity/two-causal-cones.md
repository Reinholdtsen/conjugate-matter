---
title: "Two causal cones"
weight: 30
status: alive
description: "With H = diag(g, g⁻¹) each block defines a null cone: ours bounds |dx/dt| by c and the dual bounds |dp/dt| by c̃ — motion through momentum space is force; the dual cone belongs to the slaved geometry, modified by X at short range in momentum."
provenance: [D]
sources:
  - "papers/conjugate-special-relativity.md §1"
  - "papers/conjugate-special-relativity.md Abstract"
  - "papers/conjugate-special-relativity.md preamble"
  - "papers/conjugate-special-relativity.md §6"
  - "papers/broken-born-checkpoint-v2.md §5"
  - "papers/broken-born-checkpoint-v2.md §6"
  - "papers/broken-born-checkpoint-v2.md §7.5"
  - "papers/broken-born-checkpoint-v2.md §8"
  - "papers/broken-born-checkpoint-v2.md §14 item 3"
  - "notes/broken-born-theory.md §2"
  - "review/v3-worklog.md 'New open items'"
  - "HANDOFF.md §2"
  - "HANDOFF.md §4"
  - "review/wiki-build-flags.md items 29, 30"
---

*The two causal cones are the light cones of position space and of momentum space. In the program's broken vacuum the metric on [phase space](/wiki/phase-space) has one block for position and the inverse of that block for momentum, and each block defines its own cone of allowed motion: the familiar cone limits speed, |dx/dt| ≤ c, and its twin limits the rate of change of momentum, |dp/dt| ≤ c̃. A rate of change of momentum is a force, so the twin of the speed of light is a [maximum force](/wiki/conjugate-relativity/maximum-force). This is the starting point of [#13](/wiki/conjugate-relativity), the program's paper on the special relativity of the [momentum polarization](/wiki/phase-space/reciprocity/lagrangian-polarizations). It is alive but unreviewed: #13 tags its starting point as derived, no script checks the cones, and the [checkpoint #11](/wiki/history/documents/checkpoint) does not mention them. #13 also uses two different versions of the momentum cone in different sections, an inconsistency that is open.*

**Status:** Alive, unreviewed — #13 §1 tags the block form it starts from [D — compatibility theorem] and the role of X [D — §7 of the checkpoint], both queried in `review/wiki-build-flags.md` (flags 30 and 29); the cones themselves carry no further tag — no `verify/` script checks the cones or the value of c̃, no [blind review](/wiki/method/review) round has examined #13, and #11 v2.2 does not mention them. The block form is [the compatibility theorem](/wiki/phase-space/born-geometry/compatibility-theorem), which #11 v2.1 and later tag [T][V] ([Freidel–Leigh–Minic](/wiki/phase-space/reciprocity/broken-born-duality); machine-checked in [the battery](/wiki/method/verification/battery), test T1), and #11 governs. Which momentum cone governs is [open](/wiki/conjugate-relativity/two-cones-inconsistency).

## The statement

#13 §1, after its plain-language passage:

> "The broken vacuum equips phase space with H = diag(g, g⁻¹) [D — compatibility theorem]: position space carries the metric g and momentum space its inverse. Each metric defines a null cone. Ours bounds trajectories x(t): |dx/dt| ≤ c. The dual cone bounds trajectories p(t):"

```text
|dp/dt| ≤ c̃ = ε/(λ/c) = ℏc/λ²
```

> "where λ is the Born length and ε = ℏ/λ its conjugate momentum scale."

The Abstract states the same result: "If Born reciprocity is exact and spontaneously broken, phase space carries two causal structures: the familiar light cone of position space and its image in momentum space. The momentum-space cone bounds the rate of momentum change". The value of c̃ is on [The maximum force c̃ = c⁴/G](/wiki/conjugate-relativity/maximum-force).

## What the cones are made of: the block form

The phase-space metric H is one of the three structures of [Born geometry](/wiki/phase-space/born-geometry/born-structures), with [the symplectic form ω](/wiki/phase-space/reciprocity/symplectic-form) and the neutral metric η. #11 §5 states the compatibility theorem: "Positive H satisfying both (η⁻¹H)² = 1 and (ω⁻¹H)² = −1 are exactly H = diag(g, g⁻¹), g ∈ Sym⁺(d)." In words, a metric on phase space that is compatible with both ω and η has a block g on positions, the inverse block g⁻¹ on momenta, and nothing mixing the two.

**The tag.** #13 tags the block form "[D — compatibility theorem]", as derived in the program. #11 since v2.1 tags the theorem [T][V]: the statement is the Born-geometry compatibility result of Freidel, Leigh and Minic, and the block proof and its machine check are the program's. #13 has not been revised since its import on 2026-10-19, so #11's re-attribution never reached it; #11 governs ([conflicts between sources](/wiki/history/documents/source-conflicts)).

**Where the block form holds.** Under the current postulate [P2′](/wiki/program/postulates/p2-prime), only ω is rigid and H ranges over the [modular field](/wiki/phase-space/modular-field/modular-field-z) Z = X + iY. #11 §6: "**Im Z = g**; the η-compatible locus X = 0 is the vacuum slice of §5. **Re Z = X**, the momentum graviton — the fluctuation of the emergent polarization." #13 does not cite §6, but in #11's terms the block form that #13 attributes to "the broken vacuum" is this slice, X = 0. One of the theorem's corollaries is the slaved momentum metric, g̃ = g⁻¹: on the vacuum slice momentum space has no metric of its own, only the inverse of the position metric ([corollaries of the compatibility theorem](/wiki/phase-space/born-geometry/compatibility-corollaries)).

## From a metric to a cone [T]

A metric of Lorentzian signature, in which time enters with the opposite sign to space, divides the directions at each point into timelike, spacelike and null ones; the null directions form a cone ([Special relativity: the template](/wiki/conjugate-relativity/special-relativity)). A trajectory that stays inside the cone of the spacetime metric g moves no faster than light, |dx/dt| ≤ c [T]. #13's step is to apply the same construction to the momentum block: "Each metric defines a null cone", and the cone of g⁻¹ bounds trajectories p(t) in momentum space.

**The scale c̃.** A bound on |dp/dt| needs a conversion between momentum and time, and #13 supplies it as c̃ = ε/(λ/c). The expression reads as one unit of momentum, ε, per light-crossing time of the length λ, which is λ/c; with ε = ℏ/λ it becomes ℏc/λ². #13 gives the bound without further derivation from H. The symbols match #1 §2, which writes the standard forms of ω, η and H in "units chosen so a reference length λ and momentum ε = ℏ/λ are scaled out"; #13 calls the same λ the Born length, and neither document cross-refers to the other.

## Force: motion through momentum space

#13 §1's plain passage gives the physical reading: "Motion through momentum space is what we call force." The rate of change of a body's momentum is the force acting on it, F = dp/dt (Newton's second law [T]), and a momentum per time has the units of force. The dual cone's bound |dp/dt| ≤ c̃ is therefore a bound on force, and F plays the part in the dual kinematics that velocity plays in ours. The same holds for waves [T]: a constant force translates a wavepacket's momentum spectrum at the steady rate F, as a constant velocity translates the packet itself in position. The two descriptions, waveform and spectrum, are related by the Fourier transform ([the Fourier transform as a phase-space rotation](/wiki/phase-space/reciprocity/fourier-transform)).

From this starting point #13 builds the dual interval, the force boosts and the composition law ([Force boosts and force composition](/wiki/conjugate-relativity/force-boosts)), force dilation ([Force dilation](/wiki/conjugate-relativity/force-dilation)), and the remaining pages of [the section](/wiki/conjugate-relativity).

## The slaved dual cone and X

#13 §1 ends with a refinement:

> "the dual cone is the causal structure of the *slaved* geometry g⁻¹; the independently dynamical part of momentum-space geometry is the massive field X, which modifies the dual cone only at short range in momentum [D — §7 of the checkpoint]."

The cone of g⁻¹ is fixed by g and has no dynamics of its own. What can vary independently in momentum-space geometry is X = Re Z, the departure from the vacuum slice, which is [the momentum graviton](/wiki/gravity/momentum-graviton). X is a massive spin-2 field ([why X must be massive](/wiki/gravity/momentum-graviton/forcing-chain)), so its influence is cut off beyond a range set by its mass.

**What #11 §7 says.** #13 cites "§7 of the checkpoint" for the claim, and #11 §7 does not discuss a dual cone. It states X's couplings to Standard Model matter as "gravitational-strength and Yukawa-cut at 1/M_X" (§7.5), a cut-off in the distance between ordinary bodies ([Safety by range](/wiki/gravity/momentum-graviton/fifth-force-safety)). #13 reads the cut-off as acting "at short range in momentum" here and as "Yukawa-cut in momentum [D — checkpoint §7]" in §6. The reading in momentum appears otherwise only among the results that exist in the original chat: "dual Newtonian limit = Yukawa in momentum = the gate" (`HANDOFF.md` §4; [two gravitational charges and the conjugate field equations](/wiki/gravity/momentum-graviton/chat-only-results#the-dual-newtonian-limit-and-the-gate)). #11 §8 says the dark-matter gate, a factor in the incoming relative momentum, is "delivered by X-exchange between dual-stress bilinears"; it states that mechanism, not a Yukawa form in momentum, and does not mention a dual cone. The wiki takes #11 §7.5's wording as the derived statement. The mismatch between #13's citation and #11 §7 is flag 29 in `review/wiki-build-flags.md`.

## Scope and caveats

- **Signature.** The compatibility theorem is proven for positive-definite H, with g ∈ Sym⁺(d), and a positive-definite metric has no null cone. #13's preamble: "The Euclidean/Lorentzian caveat of the main checkpoint is inherited throughout." Carrying the results to Lorentzian signature is #11 §14 item 3, "Lorentzian dressing of the Euclidean-rigorous skeleton [O]" ([Open: Lorentzian dressing of the Euclidean skeleton (OP3)](/wiki/phase-space/born-geometry/lorentzian-dressing)). #13 does not say which of its statements depend on the caveat. Flag 30 in `review/wiki-build-flags.md` makes the same point against §1's tag [D — compatibility theorem]: the theorem's g has no null cone, so the cones need the Lorentzian dressing, which is open.
- **Which dual cone.** The cone of §1 belongs to a 3+1 construction: it lives in (t, p), with time shared between the polarizations and slope c̃. #13 §6 instead says "our massless dispersion E = c|p| *is* the dual null cone", a cone in (E, p) with slope c that belongs to the four-dimensional Born map, which also exchanges time and energy. §6 uses that identification to read the bounds that the Fermi Large Area Telescope (Fermi-LAT) places on linear photon dispersion as a test of both cones: they "constrain both cones at once" ([Row 9: no linear photon dispersion](/wiki/predictions/photon-dispersion#13s-joint-reading)). The v3 worklog records the clash as item O3 and asks, before any paper claims more, to "fix #13's two cones and settle which construction governs (raised by Paul, 2026-10-19)" ([Open: the two dual cones](/wiki/conjugate-relativity/two-cones-inconsistency); [Open: the four-dimensional Born map and dual dynamics](/wiki/conjugate-relativity/four-dimensional-born-map)). The same item notes that a conjugate quantum of zero [invariant length](/wiki/conjugate-relativity/invariant-length-shell) "would sit on the dual null cone with |dp/dt| = c̃", while the withdrawn manuscript #14 described the dark sector in ordinary kinematics: "The papers were never reconciled."
- **No numbers.** Nothing on this page depends on a computed number; the value of c̃ comes with the Planck identification on the next page.

## Standing

`HANDOFF.md` §2 lists "Maximum force c̃ = c⁴/G as the momentum-space light speed" and "dual special relativity" among the alive results, under a heading that reads "derived, machine-verified where marked ✓"; neither item carries the ✓. `CLAUDE.md` lists #13 among the current references. #13 tags its starting point as derived, but no blind review round has covered #13, no `verify/` script checks the cones, and #11 v2.2 does not mention them. The section index gives the full basis of the status ([Conjugate special relativity](/wiki/conjugate-relativity)).

## Sources

- `papers/conjugate-special-relativity.md` §1 — the block form, the two cones, force as motion through momentum space, the slaved dual cone; Abstract for the two causal structures; preamble for the inherited caveat; §6 for the second cone, the Fermi-LAT bounds read as constraining both cones, and "Yukawa-cut in momentum".
- `papers/broken-born-checkpoint-v2.md` §5 — the compatibility theorem as [T][V] and its attribution; §6 for the vacuum slice X = 0 and Re Z = X; §7.5 for the range of X; §8 for the gate's mechanism; §14 item 3 for the Lorentzian dressing.
- `notes/broken-born-theory.md` §2 — the reference length λ and momentum ε = ℏ/λ.
- `review/v3-worklog.md` 'New open items' — item O3, the two dual cones.
- `HANDOFF.md` §2 — the alive listing; §4 for the chat-only "Yukawa in momentum".
- `review/wiki-build-flags.md` items 29 and 30 — #13's citation of #11 §7 for a reading #11 does not make; the tag [D — compatibility theorem] on cones that the theorem's positive-definite g cannot have. Both await Paul's ruling.
