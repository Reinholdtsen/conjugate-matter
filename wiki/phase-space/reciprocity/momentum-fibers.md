---
title: "Momentum fibers and the cotangent bundle"
weight: 75
status: established
description: "The momenta available at one point of space-time form a fiber, and phase space, made of these fibers, is the cotangent bundle of space-time; general relativity measures each fiber with the inverse metric g⁻¹ and leaves it flat, which #11 §3 calls an architectural assumption; in the program the compatibility theorem slaves the momentum metric to g⁻¹ on the vacuum, independent momentum-space geometry is assigned to X, and the gate acts through χ quanta of width μ along the fibers."
provenance: [T]
sources:
  - "wiki/papers/broken-born-checkpoint-v2.md §3"
  - "wiki/papers/broken-born-checkpoint-v2.md refs [4]–[6]"
  - "wiki/papers/broken-born-checkpoint-v2.md §5"
  - "wiki/papers/broken-born-checkpoint-v2.md §6"
  - "wiki/papers/broken-born-checkpoint-v2.md §7"
  - "wiki/papers/broken-born-checkpoint-v2.md §8"
  - "wiki/papers/broken-born-checkpoint-v2.md §14 item 4"
  - "wiki/papers/broken-born-checkpoint-v2.md App. A item 10"
  - "notes/geometric-core.md §A"
  - "notes/geometric-core.md §B"
  - "notes/geometric-core.md §C"
  - "notes/geometric-core.md §E"
  - "notes/x-classification.md §4"
  - "notes/x-classification.md §5"
  - "notes/beta-coefficients.md §5"
  - "notes/broken-born-theory.md §2"
  - "notes/broken-born-theory.md §3"
  - "notes/broken-born-theory.md §5.1"
  - "notes/broken-born-theory.md §11 item 6"
  - "notes/broken-born-theory.md 'Addendum (v0.4)'"
  - "notes/broken-born-program-v1.md §1"
  - "notes/knot-dark-matter-standalone.md §1"
  - "wiki/papers/conjugate-special-relativity.md §1"
  - "wiki/papers/conjugate-special-relativity.md §4"
  - "wiki/papers/conjugate-special-relativity.md §6"
  - "HANDOFF.md §2"
  - "HANDOFF.md §4"
  - "review/wiki-build-flags.md items 17, 29, 30"
  - "notes/closed-universe.md §4"
  - "notes/closed-universe.md §5"
  - "verify/closed_universe.py 'E. Momentum space and reciprocity'"
  - "review/wiki-build-flags.md item 48"
  - "review/wiki-build-flags.md item 55"
  - "notes/gate-mechanism.md §3"
  - "notes/gate-mechanism.md §5"
  - "notes/dual-sector.md §9"
  - "review/wiki-build-flags.md item 72"
---

*A momentum fiber is the set of all momenta a particle can have at one point of space-time. [Phase space](../../program/postulates/p1-arena.md#phase-space), the space of positions and momenta taken together, is made of these fibers, one attached to each point, much as a spectrogram attaches a whole frequency axis to each instant of a recording; geometers call the structure the cotangent bundle of space-time. In [general relativity](../../gravity/spin-2-fields/general-relativity.md) every fiber is flat. Momenta at a point are measured with the inverse of the space-time metric, which is the same everywhere along the fiber, so the curvature of space-time changes how neighbouring fibers are joined but not the geometry inside any one of them. The program's [checkpoint](../../history/documents/checkpoint.md) lists this flatness among the places where the laws treat position and momentum differently and calls it "an architectural assumption, not a measurement" ([Born's question](../../program/borns-question.md)). In the program's own geometry the [compatibility theorem](../born-geometry/compatibility-theorem.md) fixes the momentum metric as the inverse metric on the vacuum, any independent momentum-space geometry is assigned to the [momentum graviton X](../../gravity/momentum-graviton/_index.md), and the [dark-matter gate](../../dark-matter/conjugate-matter/gate-mechanism.md) acts through the width of conjugate-matter quanta along the fibers, a mechanism that a note of 2026-10-28 finds not derived (flag 55, pending). How X propagates along the fibers, which in the record would fix the shape of that gate, has not been computed.*

**Status:** Established — [T] — textbook geometry and general relativity, written here from general knowledge; the references the wiki adds are marked †, and no `verify/` script checks this material. That the flat fibers are "an architectural assumption, not a measurement" is [#11 §3](../../papers/broken-born-checkpoint-v2.md#3-the-question)'s framing, untagged there; the v1 paper's version of the sentence carries [T] ([#9 §1](../../../notes/broken-born-program-v1.md#1-the-question)), and its counterexample, gravity in 2+1 dimensions [5†], awaits [the † literature battery](../../method/literature-battery.md). The program's uses carry their own tags: the slaved momentum metric g̃ = g⁻¹, tagged [D — rigorous] in calc note [#5](../../../notes/geometric-core.md) ([§A](../../../notes/geometric-core.md#a-the-compatibility-theorem-d--rigorous)) as a corollary of a theorem that [#11 §5](../../papers/broken-born-checkpoint-v2.md#5-the-kinematic-core-and-the-compatibility-theorem) tags [T][V] (Freidel–Leigh–Minic's statement, machine-checked in [battery test T1](../../method/verification/battery.md)); μ as the χ quantum's fiber width, [D — mechanism; shape [O]] ([#11 §8](../../papers/broken-born-checkpoint-v2.md#8-conjugate-matter-and-the-gate)), for which flag 55, pending, proposes [P]; and the X propagator on the fibers, open [O] as OP4.

## Phase space as a bundle [T]

### The fiber over a point

In classical mechanics the state of a particle is a position together with a momentum [T]. Fix the position and let the momentum vary: the momenta available at that one position form a space of their own, the fiber over that position. For a particle moving in ordinary space the fiber is three-dimensional. In relativity a position is an event x of space-time and a momentum p has an energy component as well, so the fiber is four-dimensional [T]. Phase space is the union of the fibers over all points, and the map that sends a phase-space point (x, p) to its position x carries each fiber onto the point it sits over [T]:

```text
phase space     T*M = { (x, p) : x a point of M, p a momentum at x }
projection      π: (x, p) ↦ x
fiber over x    π⁻¹(x) = T*ₓM, every momentum at the one point x
```

Here M is space-time, or the configuration space of a mechanical system. A space built this way, a base with a copy of one fixed space attached to each of its points, is a fiber bundle [T]. This one is the cotangent bundle T\*M. The name records what a momentum is in geometry: a cotangent vector, an object that pairs with a small displacement dx^μ to give a number, p_μ dx^μ, which has the units of action [T]. Directions in phase space that change the momentum at a fixed position run along a fiber, and geometers call them vertical [T].

The layout is the one signal analysis uses. A spectrogram attaches a whole frequency axis to each instant of a recording, and its time–frequency plane is the phase space of the signal [T]. For a wave in space the frequency axis at each position is a wavenumber axis k, which ℏ converts into momentum, p = ℏk [T]. The fiber over x is that axis. For a particle in flat space the [Fourier transform](fourier-transform.md#waveform-and-spectrum) relates a state's description along the base, ψ(x), to its description along a fiber, ψ̃(p).

### The structure a cotangent bundle carries

Every cotangent bundle carries a [symplectic form](symplectic-form.md), built from the pairing of momenta with displacements alone, with no metric or other choice needed [T]. In the coordinates (x, p) it takes the standard form ω(u, v) = u_x · v_p − u_p · v_x ([definition](symplectic-form.md#definition)), which pairs each position direction with its own momentum direction; texts differ on its overall sign [T].

Two vertical directions have no position components, so ω vanishes between them: each fiber is a [Lagrangian](lagrangian-polarizations.md) submanifold, of half the dimension of phase space, with ω zero on it [T]. So is the set of points with p = 0, a copy of the base [T]. Geometric quantization, the standard construction of quantum states from a classical phase space, calls the fibers the vertical polarization: the wavefunctions constant along every fiber are the ordinary ψ(x) [T]. In the program's usage, where a polarization names the Lagrangian directions that count as position ([which coordinates count as "position"](lagrangian-polarizations.md#polarizations-which-coordinates-are-position)), the same structure is the position polarization: the base supplies the positions and the fibers the conjugate momenta. Writing phase space as a cotangent bundle therefore builds that choice into the arena. On flat phase space [Born reciprocity](born-reciprocity.md), ρ: (x, p) → (p, −x), carries the fiber directions onto the position directions and back [T].

## The fibers of general relativity [T]

### The inverse metric on each fiber

In general relativity the fiber over an event x holds the four-momenta of particles at x. The space-time metric g_μν(x) measures them through its matrix inverse g^μν(x). A particle of mass m has its momentum on the mass shell, written here in the sign convention [#13 §4](../../papers/conjugate-special-relativity.md#4-invariants-the-mass-shell-and-the-length-shell) uses,

```text
g^μν(x) p_μ p_ν = m²c²
```

a hyperboloid inside the fiber over x ([the mass shell](../../program/borns-question.md#the-mass-shell); [special relativity](../../conjugate-relativity/special-relativity.md#four-momentum-the-mass-shell-and-e--mc-t)) [T]. Free fall uses the same inverse metric. With the function ½ g^μν(x) p_μ p_ν as the Hamiltonian, Hamilton's equations are

```text
dx^μ/ds = g^μν p_ν          dp_μ/ds = −½ (∂_μ g^αβ) p_α p_β
```

with s a parameter that advances with proper time, and together they are the geodesic equation ([minimal coupling and free fall](../../gravity/spin-2-fields/general-relativity.md#minimal-coupling-and-free-fall-t)) [T]. A path of free fall is a curve in the cotangent bundle: its position runs along the base, and its momentum passes from each fiber to the next.

### Flat fibers on a curved base

The metric on the fiber over x, g^μν(x), depends on the point x and not on where in the fiber a momentum lies. A space with a constant metric has no curvature, so every fiber is flat: in a local inertial frame at x the fiber is the four-momentum space of special relativity [T]. The curvature of space-time appears elsewhere, in how the fibers over different points are joined. Momenta at two different events can be compared only by carrying one to the other along a path (parallel transport), and when space-time is curved the result depends on the path; that dependence is the Riemann curvature [T]. General relativity therefore curves the base and the way the fibers are joined, and leaves the geometry of each fiber flat. The v1 paper's summary: "general relativity curves x-space while leaving momentum fibers flat" ([#9 §1](../../../notes/broken-born-program-v1.md#1-the-question)).

The fiber metric is not a field of its own. It is fixed algebraically by g_μν, as its inverse, so Einstein's equations for g_μν determine it with no further equation [T].

### Curved fibers in the literature

If no choice of coordinates makes a fiber's metric constant, the fiber has curvature of its own, and the momentum space is curved. [#11 §3](../../papers/broken-born-checkpoint-v2.md#3-the-question) cites a line of quantum-gravity work in which momentum space is curved: Snyder's quantized space-time [4†], the momenta of a point particle in gravity with two space dimensions, which "live on a curved group manifold" [5†], and relative locality [6†]. The [Born-geometry papers](broken-born-duality.md) on which the program builds state the same of momentum space: "not only will space-time become curved, but momentum space as well" ([Freidel, Leigh and Minic 2014](https://arxiv.org/abs/1307.7080), Phys. Lett. B [S]), an idea they trace to Born ([Freidel, Leigh and Minic 2015](https://arxiv.org/abs/1502.08005), §1 [S]); neither [#11 §3](../../papers/broken-born-checkpoint-v2.md#3-the-question)'s lineage nor the [founding supposition](../../program/founding-suppositions.md#10-momentum-space-has-its-own-gravity) "Momentum space has its own gravity" ([#11 App. A item 10](../../papers/broken-born-checkpoint-v2.md#appendix-a-audit-of-founding-suppositions-pr-with-fates)) cites them ([`notes/dual-sector.md` §9](../../../notes/dual-sector.md#9-other-overlaps); flag 72, pending). The curvature has a scale, which the literature usually places near the Planck scale, and for momenta far below it such a space looks flat [T]. The lineage, and the soccer-ball problem it raises for the momenta of macroscopic bodies, are on [curved momentum space](curved-momentum-space.md).

## Flat fibers as an assumption

[#11 §3](../../papers/broken-born-checkpoint-v2.md#3-the-question) names three places where the dynamics departs from the symmetry of quantum kinematics, and the fibers are the third:

> "The asymmetry is dynamical: x-local interactions, the momentum-space mass shell, and general relativity's flat momentum fibers — the last an architectural assumption, not a measurement, and false in the one exactly solved quantum gravity (2+1d, where momenta live on a curved group manifold [5†]; curved momentum space has an independent lineage from Snyder [4†] through relative locality [6†])."

The v1 paper words it "an assumption of the formalism, not a measurement, and one that is *false* in the one exactly solved quantum gravity (2+1 dimensions, where momentum space is a curved group manifold) [T]" ([#9 §1](../../../notes/broken-born-program-v1.md#1-the-question)).

In this wiki's reading, on the bundle picture the assumption is the choice of fiber metric: general relativity measures every fiber with g⁻¹, so its fibers are flat by construction, and the 2+1-dimensional case is a gravitational theory in which they are curved. The point is negative, as [curved momentum space](curved-momentum-space.md#the-programs-framing) puts it: flat fibers are not forced by any measurement, and the statement does not say what geometry the fibers have. [Born's question](../../program/borns-question.md#flat-momentum-fibers) counts the flat fibers beside the form of the Hamiltonian, the locality of interactions and the mass shell, and the program's reply is [Born's answer](../../gravity/momentum-graviton/borns-answer.md), set out below.

## The fibers in the program's geometry

### Flat phase space and the momentum metric g̃

The program's kinematic core works on flat phase space. The [lab notebook](../../history/documents/lab-notebook.md) sets up its kinematics "first on flat 𝒫 ≅ ℝ²ᵈ with coordinates (xᵃ, pₐ), d = 4" ([#1 §2](../../../notes/broken-born-theory.md#2-kinematic-core); the notebook's words on this page are transcribed from its LaTeX), so each fiber is a copy of ℝᵈ ([P1: the phase-space arena](../../program/postulates/p1-arena.md)). Its [generalized metric](../born-geometry/born-structures.md) H, a positive metric on the whole of phase space, splits along the two kinds of direction: "On the x-tilted vacuum, H decomposes into a spacetime metric g_μν(x) and a momentum-space metric g̃^μν" [D, schematic] ([#1 §3](../../../notes/broken-born-theory.md#3-action)). The split belongs to the vacuum, the x-tilted one that postulate [P5](../../program/postulates/p5-spontaneous-selection.md) selects. In this wiki's terms g̃ is the metric of the fibers.

In the notebook's first version g̃ carried the dark-matter gate. The self-interaction of [conjugate matter](../../dark-matter/conjugate-matter/_index.md) was "routed through the g̃ block", and the gate's support was "set by a scale μ of the g̃ sector" [P] ([#1 §3](../../../notes/broken-born-theory.md#3-action)), a form since superseded ([the Gaussian gate of v0.1](../../dark-matter/conjugate-matter/velocity-gate.md#superseded-the-gaussian-gate-of-v01)). The notebook's sixth open problem asked "why macroscopic momenta don't probe g̃ curvature" ([#1 §11 item 6](../../../notes/broken-born-theory.md#11-open-problems-in-order-of-severity)). That is the soccer-ball problem, which no later document takes up ([extensivity](curved-momentum-space.md#open-extensivity-the-soccer-ball-problem)).

### Slaved to the base: g̃ = g⁻¹

The [compatibility theorem](../born-geometry/compatibility-theorem.md) fixes the fibers' metric when the symplectic form ω and the neutral metric η are both held rigid: the positive H compatible with both are exactly H = diag(g, g⁻¹). Calc note #5 draws the third corollary: "**The momentum metric is slaved: g̃ = g⁻¹ pointwise.** No independent momentum-space geometry survives." ([§A](../../../notes/geometric-core.md#a-the-compatibility-theorem-d--rigorous); [corollary 3](../born-geometry/compatibility-corollaries.md#corollary-3-the-slaved-momentum-metric)).

In this wiki's reading, g⁻¹ is the metric general relativity puts on its fibers, so with both structures rigid the program's fibers are those of general relativity and its momentum space has no geometry of its own. Calc note #5 states the consequence for the program: "With H = diag(g, g⁻¹), S_H is a functional of g alone: a pure metric theory. No momentum graviton, hence no geometric origin for the χ gate either." ([§B](../../../notes/geometric-core.md#b-the-inconsistency-and-the-forced-repair-d--structural); [the collision with the theory as documented](../born-geometry/compatibility-corollaries.md#the-collision-with-the-theory-as-documented-d--structural)). The collision forced the change from [original P2](../../program/postulates/original-p2.md) to [P2′](../../program/postulates/p2-prime.md), under which only ω is rigid and the block form survives only on the vacuum slice: "At X = 0, H = diag(g, g⁻¹): the η-compatible locus of Theorem A is precisely the vacuum slice" ([#5 §C](../../../notes/geometric-core.md#c-the-modular-field-d--structural-math-facts-standard)).

[The handoff](../../history/documents/handoff.md) records the comparison with general relativity among results that exist only in the original conversation: "slaved layer g̃ = g⁻¹ is algebraic (Einstein's equation does double duty)" ([`HANDOFF.md` §4](../../../HANDOFF.md#4-results-that-exist-only-in-the-chat-not-in-any-artifact)). No document derives it, and its status is conjecture ([chat-only: the slaved layer is algebraic](../born-geometry/compatibility-corollaries.md#chat-only-the-slaved-layer-is-algebraic)).

The theorem is proven for a positive-definite g, while the fibers of general relativity carry the Lorentzian g⁻¹. The extension is open ([Open: Lorentzian dressing of the Euclidean skeleton (OP3)](../born-geometry/lorentzian-dressing.md)).

### A closed base does not close the fibre

The closed-universe note of 2026-10-27 draws a further consequence of the block form [D][V]. In the record's generalized metric the momentum block is Y⁻¹, the same at every momentum p, for any X; so the fibre over each point is flat ℝ³, with dual curvature k̃ = 0, and a closed universe, k = +1, does not induce a closed momentum space ([`notes/closed-universe.md` §4](../../../notes/closed-universe.md#4-how-small-momentum-space-gets)). What closure does to the fibres is make momenta discrete, with spacing of order ħ/R on a three-sphere of radius R. The lab notebook's "closed dual space ⇒ negative ΔN_eff" therefore needs a separate postulate of a curved, compact momentum space, which no document states (flag 48 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md); [a closed Comatter universe](../../cosmology/scale-factor-duality/closed-universe.md#how-small-momentum-space-gets)). On the closed universe's phase space T\*S³, the note also finds that only the polarization along the fibres is integrable ([reciprocity on a closed space](closed-space-reciprocity.md)).

### Independent momentum-space geometry: X

Under P2′ the generalized metric ranges over the values of the [modular field](../modular-field/modular-field-z.md) Z = X + iY, whose imaginary part is the space-time metric, Im Z = g [D] ([#11 §6](../../papers/broken-born-checkpoint-v2.md#6-the-modular-field)), and the real part carries what is not slaved. Calc note #5 calls Re Z = X "the momentum graviton", "the local wobble of the emergent polarization, 'which way the x/p split points, here.'", and lists its roles as "momentum geometry and gate mediator (Re Z)" ([§C](../../../notes/geometric-core.md#c-the-modular-field-d--structural-math-facts-standard)). In this wiki's reading, X tilts the split between position directions and fiber directions from point to point. A withdrawn paper on monopole dark matter states the division: "the baseline momentum-space geometry is slaved (g-tilde = g^-1, det H = 1), and any independent momentum-space geometry resides in the fluctuation X" ([its §1](../../../notes/knot-dark-matter-standalone.md#1-framework)).

Calc note #5 restates the lab notebook's first open problem in these terms: "The field-equation problem, restated exactly: *the field equation for momentum-space geometry is the Re Z sector of S_H.*" (§C). [#11 §7](../../papers/broken-born-checkpoint-v2.md#7-the-massive-momentum-graviton) gives the program's answer, [Born's answer](../../gravity/momentum-graviton/borns-answer.md): "momentum-space geometry is dynamical — a reciprocity-odd massive spin-2, its mass born of the polarization choice". The [founding supposition](../../program/founding-suppositions.md#10-momentum-space-has-its-own-gravity) "Momentum space has its own gravity" is recorded as "vindicated, transformed: dynamical, massive, reciprocity-odd (§7)" ([#11 App. A item 10](../../papers/broken-born-checkpoint-v2.md#appendix-a-audit-of-founding-suppositions-pr-with-fates); bold dropped).

#13 adds that X "modifies the dual cone only at short range in momentum [D — [§7](../../papers/broken-born-checkpoint-v2.md#7-the-massive-momentum-graviton) of the checkpoint]" (§1), and §6 that "dual-geometric effects are Yukawa-cut in momentum [D — [checkpoint §7](../../papers/broken-born-checkpoint-v2.md#7-the-massive-momentum-graviton)]". [#11 §7](../../papers/broken-born-checkpoint-v2.md#7-the-massive-momentum-graviton) makes neither statement; flag 29 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md), confirmed by the flags' audit, records that the momentum reading appears only among the chat-only results ([`HANDOFF.md` §4](../../../HANDOFF.md#4-results-that-exist-only-in-the-chat-not-in-any-artifact)). Beyond these one-line statements no document describes how X changes the geometry within one fiber, and none compares the program's momentum-space geometry in detail with Snyder's construction or with relative locality ([the program's own momentum-space geometry](curved-momentum-space.md#the-programs-own-momentum-space-geometry)).

### A second light cone

#13 builds its kinematics on the block form: "The broken vacuum equips phase space with H = diag(g, g⁻¹) [D — compatibility theorem]: position space carries the metric g and momentum space its inverse. Each metric defines a null cone." ([§1](../../papers/conjugate-special-relativity.md#1-two-causal-cones); [two causal cones](../../conjugate-relativity/two-causal-cones.md)). It calls the dual cone "the causal structure of the *slaved* geometry g⁻¹" ([§1](../../papers/conjugate-special-relativity.md#1-two-causal-cones)). Flag 30 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md) notes that the theorem's g is positive-definite and has no null cone, so the cones need the open Lorentzian dressing; its audit found the tag itself a question of tagging convention. Which momentum-space cone #13 means is also open ([Open: the two dual cones](../../conjugate-relativity/two-cones-inconsistency.md)).

## Matter on the fibers: the gate

Conjugate matter χ, one of the program's dark-matter candidates, is the "p-polarized" matter of postulate [P4](../../program/postulates/p4-polarized-matter.md), and the program's account of its self-interaction places its quanta on the fibers.

### Quanta with a width along the fiber

Calc note [#6](../../../notes/x-classification.md) derives the [velocity gate](../../dark-matter/conjugate-matter/velocity-gate.md), the factor that switches off χ's self-interaction at large relative velocity, from exchange of the massive X ([the gate mechanism](../../dark-matter/conjugate-matter/gate-mechanism.md); not derived, according to flag 55 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md), pending):

> "The relative-momentum dependence enters through the χ quanta's **intrinsic momentum-space extent**: p-polarized quanta are extended objects on the momentum fiber with width μ, and they exchange X only over their fiber overlap — the dual of how x-extended composites acquire form factors F(qR)." ([`notes/x-classification.md` §4](../../../notes/x-classification.md#4-consequences-downstream-d--structural-with-one-honest-downgrade))

Integrating out the heavy X leaves a contact interaction, one that acts only where the particles meet, so the two quanta interact at one point of space-time. In this wiki's reading their overlap is then taken in the fiber over that point: a contact force acts where two waveforms overlap, and the gate acts only where their spectra overlap as well ([position and momentum exchanged](../../dark-matter/conjugate-matter/gate-mechanism.md#position-and-momentum-exchanged)).

In the lab notebook the width became a property of the χ quantum itself with the v0.4 addendum, which records #6: "μ is identified as the χ quantum's intrinsic momentum-fiber width, with a Gaussian gate iff the fiber profile is Gaussian" (#1 'Addendum (v0.4)'). [#11 §8](../../papers/broken-born-checkpoint-v2.md#8-conjugate-matter-and-the-gate) writes the gate as F(k²/μ²), with k the incoming relative momentum of the pair, "with μ the χ quantum's intrinsic momentum-fiber width [D — mechanism; shape [O]]". The handoff lists "μ = χ's momentum-fiber width" among the live results ([`HANDOFF.md` §2](../../../HANDOFF.md#2-scientific-state-one-screen)), and calc note [#8](../../../notes/beta-coefficients.md)'s close-out lists the gate problem as "mechanism found (X-exchange, μ = fiber width); shape completion open (Gaussian vs rational tail — now also an observable discriminant)" ([`notes/beta-coefficients.md` §5](../../../notes/beta-coefficients.md#5-what-remains-honest-close-out)).

The profile along the fiber decides the form of the gate. "Wavepacket overlap of Gaussian profiles gives exactly e^{−(p₁−p₂)²/2μ²} — the postulated gate", but "tree-level exchange with generic vertices yields rational (power-law-tailed) gates; the Gaussian requires the Gaussian fiber profile" ([#6 §4](../../../notes/x-classification.md#4-consequences-downstream-d--structural-with-one-honest-downgrade)). The overlap form and the lab notebook's postulated e^{−k²/μ²} are written in different variables, and no source converts one into the other. Flag 17 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md) records a factor of √2 in μ between them, which its audit found to depend on how #6's form is read, and notes that no stated number changes ([two conventions, not reconciled](../../dark-matter/conjugate-matter/velocity-gate.md#two-conventions-not-reconciled)).

[#13 §4](../../papers/conjugate-special-relativity.md#4-invariants-the-mass-shell-and-the-length-shell) gives the width a kinematic origin: "The conjugate quantum's invariant extent fixes its intrinsic momentum-space width μ ~ ℏ/λ_χ — which is precisely the gate scale of the dark-matter sector, v\* = √2 μ/m_χ" [D — structural], with λ_χ the extent of a conjugate quantum in position ([the invariant-length shell](../../conjugate-relativity/invariant-length-shell.md)). The relation between the width in momentum and the extent in position is reciprocal, as between the widths of a spectrum and its waveform ([the time–bandwidth product](fourier-transform.md#the-timebandwidth-product)). The relation v\* = √2 μ/m_χ is the lab notebook's ([#1 §5.1](../../../notes/broken-born-theory.md#51-the-scattering-law-d)), and #13's use of it with the fiber width is the combination flag 17 records ([what μ is](../../dark-matter/conjugate-matter/gate-mechanism.md#what-μ-is)).

[`notes/gate-mechanism.md`](../../../notes/gate-mechanism.md) (2026-10-28; two derivations, the second blind; not reviewed) finds that this picture is not derived. The record never writes the overlap down, and written down in the two natural ways, which are the note's reconstruction, it gives either an ordinary position-local potential of range ħ/μ, about ten picometres (reading R1), or a pair-channel interaction that produces the gate but contains no X (reading R2) ([§3](../../../notes/gate-mechanism.md#3-the-fiber-overlap-read-two-ways); [the fiber overlap, read two ways](../../dark-matter/conjugate-matter/gate-mechanism.md#the-fiber-overlap-read-two-ways)). On #13's reading the note adds: "[#13 §4](../../papers/conjugate-special-relativity.md#4-invariants-the-mass-shell-and-the-length-shell) identifies μ with ħ/λ_χ, an extent in position. Standard form-factor physics turns that into a form factor in the transfer q at scale μ, not a gate in k [T]" (§3). Flag 55 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md) (pending) proposes [P] for the gate and μ and [O] for the mechanism; [#11 §8](../../papers/broken-born-checkpoint-v2.md#8-conjugate-matter-and-the-gate)'s tag is [D — mechanism; shape [O]].

### The X propagator on the fibers (OP4)

In the record, the shape of the gate depends on how X propagates along the fibers. Calc note #5: "The gate *shape* is the X propagator's structure on the momentum fibers — open [O]" ([§E](../../../notes/geometric-core.md#e-the-gate-problem--the-mechanism-found-d--structural)). #11 keeps it as its fourth open problem: "Gate shape (X propagator on momentum fibers; Gaussian vs rational — now observable) [O]" ([#11 §14 item 4](../../papers/broken-born-checkpoint-v2.md#14-open-problems); [Open: the gate shape (OP4)](../../dark-matter/conjugate-matter/gate-shape.md)). Calc note #6's closing list ties the Gaussian case to the metastring of [Freidel, Leigh and Minic](broken-born-duality.md): "gate-shape completion (Gaussian fiber profile — ties to the metastring's modular vertex structure)" ([§5](../../../notes/x-classification.md#5-the-field-equation-problem-after-this-chunk)). No document writes the X propagator on the fibers, the χ–X vertex or the profile of a χ quantum along the fiber. [`notes/gate-mechanism.md`](../../../notes/gate-mechanism.md) finds that within [#11 §7](../../papers/broken-born-checkpoint-v2.md#7-the-massive-momentum-graviton) there is nothing to write: "The section condition ([#1 §2](../../../notes/broken-born-theory.md#2-kinematic-core); [#5 §D](../../../notes/geometric-core.md#d-quadratic-spectrum-and-the-ghost-question-partial)) makes H_Z, and with it X, depend on x only. The fiber metric is constant along each fiber, so 'X propagator on momentum fibers' has no meaning within §7" (§3) [D, record audit]. Flag 55 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md) (pending) records the point ([the section condition](../../symmetry-breaking/section-condition.md)).

### The dual stress: derivatives along the fiber

X couples to χ through the [dual stress T̃](../../dark-matter/conjugate-matter/dual-stress.md): "Conjugate matter couples to H universally (P4); its coupling to the X-block is through the **dual stress** T̃ — moments involving momentum-derivatives of the χ bilinear" ([#5 §E](../../../notes/geometric-core.md#e-the-gate-problem--the-mechanism-found-d--structural)). Ordinary stress-energy is built from derivatives along space-time, the base [T]; derivatives with respect to momentum are taken along the fibers. No document writes T̃ out, and the strength of the coupling is open ([Open: the dual-stress enhancement (OP5)](../../dark-matter/conjugate-matter/dual-stress-enhancement.md)).

## What is open

- **The propagator and the profile.** X's propagator on the fibers, the χ–X vertex and a χ quantum's profile along the fiber decide the gate's shape, and none of them is computed (OP4). The gate-mechanism note finds that the section condition gives the propagator no meaning within [#11 §7](../../papers/broken-born-checkpoint-v2.md#7-the-massive-momentum-graviton), and proposes the mechanism itself as open [O] (flag 55, pending). Among its open questions is "Whether a doubled, phase-space field theory for χ that drops the section condition could define a relative momentum consistent with momentum conservation" ([`notes/gate-mechanism.md` §5](../../../notes/gate-mechanism.md#5-what-follows-for-the-record)).
- **Geometry within a fiber.** No document works out how X changes the geometry of a single fiber or compares the program's momentum-space geometry with the curved momentum spaces of the literature.
- **Lorentzian signature.** The slaved metric g̃ = g⁻¹ is derived for a positive-definite g (OP3).
- **Extensivity.** The soccer-ball problem stays open on the lab notebook's authority and is absent from #11's list ([curved momentum space](curved-momentum-space.md#open-extensivity-the-soccer-ball-problem)).
- **The citations.** [#11 §3](../../papers/broken-born-checkpoint-v2.md#3-the-question)'s references [4]–[6], including the 2+1-dimensional result behind "false in the one exactly solved quantum gravity", are from model memory and await the † literature battery (OP10).

The registered items are listed in [open problems and the queue](../../status/open-problems.md).

## Standard references

Added by the wiki from model memory (†); the program's documents do not cite them.

- V. I. Arnold, *Mathematical Methods of Classical Mechanics* (1978)†: the cotangent bundle, its symplectic form and Hamiltonian mechanics on it.
- R. Abraham and J. E. Marsden, *Foundations of Mechanics*, 2nd edition (1978)†: the same, with geodesic motion as a Hamiltonian flow on the cotangent bundle.
- C. W. Misner, K. S. Thorne and J. A. Wheeler, *Gravitation* (1973)†: the momentum space at an event and the mass hyperboloid, in kinetic theory on curved space-time.
- N. M. J. Woodhouse, *Geometric Quantization* (1980)†: the vertical polarization of a cotangent bundle.

## Used by

- [Born's question](../../program/borns-question.md) — general relativity's flat momentum fibers as one source of the asymmetry between position and momentum.
- [Born's answer: momentum space gravitates](../../gravity/momentum-graviton/borns-answer.md) — the program's reply: momentum-space geometry is dynamical and carried by X.
- [Corollaries: unimodularity, no B-field, slaved momentum metric](../born-geometry/compatibility-corollaries.md) — g̃ = g⁻¹, the fiber metric fixed by g.
- [The modular field Z = X + iY](../modular-field/modular-field-z.md) — X as the carrier of independent momentum-space geometry.
- [The gate mechanism: X exchange over fiber overlap](../../dark-matter/conjugate-matter/gate-mechanism.md) — χ quanta of width μ along the fibers.
- [The velocity gate](../../dark-matter/conjugate-matter/velocity-gate.md) — μ as "the χ quantum's intrinsic momentum-fiber width" in [#11 §8](../../papers/broken-born-checkpoint-v2.md#8-conjugate-matter-and-the-gate).
- [Open: the gate shape (OP4)](../../dark-matter/conjugate-matter/gate-shape.md) — the X propagator on the momentum fibers.
- [Dual stress T̃](../../dark-matter/conjugate-matter/dual-stress.md) — momentum derivatives of the χ bilinear.
- [Two causal cones](../../conjugate-relativity/two-causal-cones.md) — a second light cone on the momentum block g⁻¹.
- [The invariant-length shell and Planck closure](../../conjugate-relativity/invariant-length-shell.md) — μ ~ ℏ/λ_χ read as the fiber width.
- [A closed Comatter universe](../../cosmology/scale-factor-duality/closed-universe.md) — the fibre stays flat when the base is closed; closure makes momenta discrete.
- [Reciprocity on a closed space](closed-space-reciprocity.md) — the polarization along the fibres is the only integrable one on T\*S³.

## Sources

- [`wiki/papers/broken-born-checkpoint-v2.md` §3](../../papers/broken-born-checkpoint-v2.md#3-the-question) and refs [4]–[6] — the flat fibers as "an architectural assumption, not a measurement" and the curved-momentum lineage (all †); [§5](../../papers/broken-born-checkpoint-v2.md#5-the-kinematic-core-and-the-compatibility-theorem) — the compatibility theorem [T][V] and g̃ = g⁻¹ slaved; [§6](../../papers/broken-born-checkpoint-v2.md#6-the-modular-field) — Im Z = g; [§7](../../papers/broken-born-checkpoint-v2.md#7-the-massive-momentum-graviton) — Born's answer; [§8](../../papers/broken-born-checkpoint-v2.md#8-conjugate-matter-and-the-gate) — μ as the fiber width; [§14 item 4](../../papers/broken-born-checkpoint-v2.md#14-open-problems) — the X propagator on the fibers; [App. A item 10](../../papers/broken-born-checkpoint-v2.md#appendix-a-audit-of-founding-suppositions-pr-with-fates) — "vindicated, transformed"
- [`notes/geometric-core.md` §A](../../../notes/geometric-core.md#a-the-compatibility-theorem-d--rigorous) — corollary 3, the slaved momentum metric; [§B](../../../notes/geometric-core.md#b-the-inconsistency-and-the-forced-repair-d--structural) — the collision with the documented theory; [§C](../../../notes/geometric-core.md#c-the-modular-field-d--structural-math-facts-standard) — the vacuum slice, X as momentum geometry, the field-equation problem as the Re Z sector; [§E](../../../notes/geometric-core.md#e-the-gate-problem--the-mechanism-found-d--structural) — the dual stress, the gate shape as the X propagator on the fibers
- [`notes/x-classification.md` §4](../../../notes/x-classification.md#4-consequences-downstream-d--structural-with-one-honest-downgrade) — quanta extended on the fiber, exchange over the fiber overlap, Gaussian and rational gates; [§5](../../../notes/x-classification.md#5-the-field-equation-problem-after-this-chunk) — the Gaussian fiber profile and the metastring
- [`notes/beta-coefficients.md` §5](../../../notes/beta-coefficients.md#5-what-remains-honest-close-out) — the gate's mechanism found with "μ = fiber width", shape open
- [`notes/broken-born-theory.md` §2](../../../notes/broken-born-theory.md#2-kinematic-core) — flat phase space ℝ²ᵈ; [§3](../../../notes/broken-born-theory.md#3-action) — H split into g and g̃, the v0.1 gate through g̃; [§11 item 6](../../../notes/broken-born-theory.md#11-open-problems-in-order-of-severity) — "g̃ curvature"; 'Addendum (v0.4)' — μ as the fiber width; [§5.1](../../../notes/broken-born-theory.md#51-the-scattering-law-d) — v\* ≡ √2μ/m_χ
- [`notes/broken-born-program-v1.md` §1](../../../notes/broken-born-program-v1.md#1-the-question) — the flat fibers, tagged [T]
- [`notes/knot-dark-matter-standalone.md` §1](../../../notes/knot-dark-matter-standalone.md#1-framework) — independent momentum-space geometry resides in X (withdrawn manuscript)
- [`wiki/papers/conjugate-special-relativity.md` §1](../../papers/conjugate-special-relativity.md#1-two-causal-cones) — the block form, the dual cone of g⁻¹, X "at short range in momentum"; [§4](../../papers/conjugate-special-relativity.md#4-invariants-the-mass-shell-and-the-length-shell) — μ ~ ℏ/λ_χ; [§6](../../papers/conjugate-special-relativity.md#6-what-is-shared-what-is-broken-what-is-open) — "Yukawa-cut in momentum"
- [`HANDOFF.md` §2](../../../HANDOFF.md#2-scientific-state-one-screen) — "μ = χ's momentum-fiber width"; [§4](../../../HANDOFF.md#4-results-that-exist-only-in-the-chat-not-in-any-artifact) — the chat-only "slaved layer g̃ = g⁻¹ is algebraic"
- [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md) items 17, 29, 30 — the two gate conventions and the √2 in μ; #13's citation of [#11 §7](../../papers/broken-born-checkpoint-v2.md#7-the-massive-momentum-graviton); #13's tag on its cones
- [`notes/closed-universe.md` §4](../../../notes/closed-universe.md#4-how-small-momentum-space-gets), [§5](../../../notes/closed-universe.md#5-reciprocity-on-a-closed-space) and [`verify/closed_universe.py`](../../../verify/closed_universe.py) section E (E1, E2, E4) — the flat fibre over a closed base, the discrete momenta and the integrable polarization; computed, not reviewed
- [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md) item 48 — a closed universe does not close momentum space (pending); item 55 — the gate's mechanism not derived (pending)
- [`notes/gate-mechanism.md` §3](../../../notes/gate-mechanism.md#3-the-fiber-overlap-read-two-ways) — the fiber overlap read two ways; no X propagator on the fibers within [#11 §7](../../papers/broken-born-checkpoint-v2.md#7-the-massive-momentum-graviton); #13's μ ~ ℏ/λ_χ as a form factor in q; [§5](../../papers/conjugate-special-relativity.md#5-inertia-dualized) — a phase-space field theory for χ without the section condition, open
- [`notes/dual-sector.md` §9](../../../notes/dual-sector.md#9-other-overlaps) and [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md) item 72 — curved momentum space in Freidel, Leigh and Minic 2014 (Phys. Lett. B), traced by them to Born, uncited in [#11 §3](../../papers/broken-born-checkpoint-v2.md#3-the-question)'s lineage and at [App. A item 10](../../papers/broken-born-checkpoint-v2.md#appendix-a-audit-of-founding-suppositions-pr-with-fates); searched and verified by independent agents, not reviewed; the flag pending
