---
title: "Momentum fibers and the cotangent bundle"
weight: 75
status: established
description: "The momenta available at one point of space-time form a fiber, and phase space, made of these fibers, is the cotangent bundle of space-time; general relativity measures each fiber with the inverse metric g⁻¹ and leaves it flat, which #11 §3 calls an architectural assumption; in the program the compatibility theorem slaves the momentum metric to g⁻¹ on the vacuum, independent momentum-space geometry is assigned to X, and the gate acts through χ quanta of width μ along the fibers."
provenance: [T]
sources:
  - "papers/broken-born-checkpoint-v2.md §3"
  - "papers/broken-born-checkpoint-v2.md refs [4]–[6]"
  - "papers/broken-born-checkpoint-v2.md §5"
  - "papers/broken-born-checkpoint-v2.md §6"
  - "papers/broken-born-checkpoint-v2.md §7"
  - "papers/broken-born-checkpoint-v2.md §8"
  - "papers/broken-born-checkpoint-v2.md §14 item 4"
  - "papers/broken-born-checkpoint-v2.md App. A item 10"
  - "notes/debt1a-geometric-core.md §A"
  - "notes/debt1a-geometric-core.md §B"
  - "notes/debt1a-geometric-core.md §C"
  - "notes/debt1a-geometric-core.md §E"
  - "notes/debt1a-ii-X-classification.md §4"
  - "notes/debt1a-ii-X-classification.md §5"
  - "notes/debt1a-iv-beta-coefficients.md §5"
  - "notes/broken-born-theory.md §2"
  - "notes/broken-born-theory.md §3"
  - "notes/broken-born-theory.md §5.1"
  - "notes/broken-born-theory.md §11 item 6"
  - "notes/broken-born-theory.md 'Addendum (v0.4)'"
  - "notes/broken-born-program-v1.md §1"
  - "notes/knot-dark-matter-standalone.md §1"
  - "papers/conjugate-special-relativity.md §1"
  - "papers/conjugate-special-relativity.md §4"
  - "papers/conjugate-special-relativity.md §6"
  - "HANDOFF.md §2"
  - "HANDOFF.md §4"
  - "review/wiki-build-flags.md items 17, 29, 30"
  - "notes/closed-universe.md §4"
  - "notes/closed-universe.md §5"
  - "verify/closed_universe.py 'E. Momentum space and reciprocity'"
  - "review/wiki-build-flags.md item 48"
---

*A momentum fiber is the set of all momenta a particle can have at one point of space-time. [Phase space](/wiki/program/postulates/p1-arena#phase-space), the space of positions and momenta taken together, is made of these fibers, one attached to each point, much as a spectrogram attaches a whole frequency axis to each instant of a recording; geometers call the structure the cotangent bundle of space-time. In [general relativity](/wiki/gravity/spin-2-fields/general-relativity) every fiber is flat. Momenta at a point are measured with the inverse of the space-time metric, which is the same everywhere along the fiber, so the curvature of space-time changes how neighbouring fibers are joined but not the geometry inside any one of them. The program's [checkpoint](/wiki/history/documents/checkpoint) lists this flatness among the places where the laws treat position and momentum differently and calls it "an architectural assumption, not a measurement" ([Born's question](/wiki/program/borns-question)). In the program's own geometry the [compatibility theorem](/wiki/phase-space/born-geometry/compatibility-theorem) fixes the momentum metric as the inverse metric on the vacuum, any independent momentum-space geometry is assigned to the [momentum graviton X](/wiki/gravity/momentum-graviton), and the [dark-matter gate](/wiki/dark-matter/conjugate-matter/gate-mechanism) acts through the width of conjugate-matter quanta along the fibers. How X propagates along the fibers, which would fix the shape of that gate, has not been computed.*

**Status:** Established — [T] — textbook geometry and general relativity, written here from general knowledge; the references the wiki adds are marked †, and no `verify/` script checks this material. That the flat fibers are "an architectural assumption, not a measurement" is #11 §3's framing, untagged there; the v1 paper's version of the sentence carries [T] (#9 §1), and its counterexample, gravity in 2+1 dimensions [5†], awaits [the † literature battery](/wiki/method/literature-battery). The program's uses carry their own tags: the slaved momentum metric g̃ = g⁻¹, tagged [D — rigorous] in calc note #5 (§A) as a corollary of a theorem that #11 §5 tags [T][V] (Freidel–Leigh–Minic's statement, machine-checked in [battery test T1](/wiki/method/verification/battery)); μ as the χ quantum's fiber width, [D — mechanism; shape [O]] (#11 §8); and the X propagator on the fibers, open [O] as OP4.

## Phase space as a bundle [T]

### The fiber over a point

In classical mechanics the state of a particle is a position together with a momentum [T]. Fix the position and let the momentum vary: the momenta available at that one position form a space of their own, the fiber over that position. For a particle moving in ordinary space the fiber is three-dimensional. In relativity a position is an event x of space-time and a momentum p has an energy component as well, so the fiber is four-dimensional [T]. Phase space is the union of the fibers over all points, and the map that sends a phase-space point (x, p) to its position x carries each fiber onto the point it sits over [T]:

```text
phase space     T*M = { (x, p) : x a point of M, p a momentum at x }
projection      π: (x, p) ↦ x
fiber over x    π⁻¹(x) = T*ₓM, every momentum at the one point x
```

Here M is space-time, or the configuration space of a mechanical system. A space built this way, a base with a copy of one fixed space attached to each of its points, is a fiber bundle [T]. This one is the cotangent bundle T\*M. The name records what a momentum is in geometry: a cotangent vector, an object that pairs with a small displacement dx^μ to give a number, p_μ dx^μ, which has the units of action [T]. Directions in phase space that change the momentum at a fixed position run along a fiber, and geometers call them vertical [T].

The layout is the one signal analysis uses. A spectrogram attaches a whole frequency axis to each instant of a recording, and its time–frequency plane is the phase space of the signal [T]. For a wave in space the frequency axis at each position is a wavenumber axis k, which ℏ converts into momentum, p = ℏk [T]. The fiber over x is that axis. For a particle in flat space the [Fourier transform](/wiki/phase-space/reciprocity/fourier-transform#waveform-and-spectrum) relates a state's description along the base, ψ(x), to its description along a fiber, ψ̃(p).

### The structure a cotangent bundle carries

Every cotangent bundle carries a [symplectic form](/wiki/phase-space/reciprocity/symplectic-form), built from the pairing of momenta with displacements alone, with no metric or other choice needed [T]. In the coordinates (x, p) it takes the standard form ω(u, v) = u_x · v_p − u_p · v_x ([definition](/wiki/phase-space/reciprocity/symplectic-form#definition)), which pairs each position direction with its own momentum direction; texts differ on its overall sign [T].

Two vertical directions have no position components, so ω vanishes between them: each fiber is a [Lagrangian](/wiki/phase-space/reciprocity/lagrangian-polarizations) submanifold, of half the dimension of phase space, with ω zero on it [T]. So is the set of points with p = 0, a copy of the base [T]. Geometric quantization, the standard construction of quantum states from a classical phase space, calls the fibers the vertical polarization: the wavefunctions constant along every fiber are the ordinary ψ(x) [T]. In the program's usage, where a polarization names the Lagrangian directions that count as position ([which coordinates count as "position"](/wiki/phase-space/reciprocity/lagrangian-polarizations#polarizations-which-coordinates-are-position)), the same structure is the position polarization: the base supplies the positions and the fibers the conjugate momenta. Writing phase space as a cotangent bundle therefore builds that choice into the arena. On flat phase space [Born reciprocity](/wiki/phase-space/reciprocity/born-reciprocity), ρ: (x, p) → (p, −x), carries the fiber directions onto the position directions and back [T].

## The fibers of general relativity [T]

### The inverse metric on each fiber

In general relativity the fiber over an event x holds the four-momenta of particles at x. The space-time metric g_μν(x) measures them through its matrix inverse g^μν(x). A particle of mass m has its momentum on the mass shell, written here in the sign convention #13 §4 uses,

```text
g^μν(x) p_μ p_ν = m²c²
```

a hyperboloid inside the fiber over x ([the mass shell](/wiki/program/borns-question#the-mass-shell); [special relativity](/wiki/conjugate-relativity/special-relativity#four-momentum-the-mass-shell-and-e--mc-t)) [T]. Free fall uses the same inverse metric. With the function ½ g^μν(x) p_μ p_ν as the Hamiltonian, Hamilton's equations are

```text
dx^μ/ds = g^μν p_ν          dp_μ/ds = −½ (∂_μ g^αβ) p_α p_β
```

with s a parameter that advances with proper time, and together they are the geodesic equation ([minimal coupling and free fall](/wiki/gravity/spin-2-fields/general-relativity#minimal-coupling-and-free-fall-t)) [T]. A path of free fall is a curve in the cotangent bundle: its position runs along the base, and its momentum passes from each fiber to the next.

### Flat fibers on a curved base

The metric on the fiber over x, g^μν(x), depends on the point x and not on where in the fiber a momentum lies. A space with a constant metric has no curvature, so every fiber is flat: in a local inertial frame at x the fiber is the four-momentum space of special relativity [T]. The curvature of space-time appears elsewhere, in how the fibers over different points are joined. Momenta at two different events can be compared only by carrying one to the other along a path (parallel transport), and when space-time is curved the result depends on the path; that dependence is the Riemann curvature [T]. General relativity therefore curves the base and the way the fibers are joined, and leaves the geometry of each fiber flat. The v1 paper's summary: "general relativity curves x-space while leaving momentum fibers flat" (#9 §1).

The fiber metric is not a field of its own. It is fixed algebraically by g_μν, as its inverse, so Einstein's equations for g_μν determine it with no further equation [T].

### Curved fibers in the literature

If no choice of coordinates makes a fiber's metric constant, the fiber has curvature of its own, and the momentum space is curved. #11 §3 cites a line of quantum-gravity work in which momentum space is curved: Snyder's quantized space-time [4†], the momenta of a point particle in gravity with two space dimensions, which "live on a curved group manifold" [5†], and relative locality [6†]. The curvature has a scale, which the literature usually places near the Planck scale, and for momenta far below it such a space looks flat [T]. The lineage, and the soccer-ball problem it raises for the momenta of macroscopic bodies, are on [curved momentum space](/wiki/phase-space/reciprocity/curved-momentum-space).

## Flat fibers as an assumption

#11 §3 names three places where the dynamics departs from the symmetry of quantum kinematics, and the fibers are the third:

> "The asymmetry is dynamical: x-local interactions, the momentum-space mass shell, and general relativity's flat momentum fibers — the last an architectural assumption, not a measurement, and false in the one exactly solved quantum gravity (2+1d, where momenta live on a curved group manifold [5†]; curved momentum space has an independent lineage from Snyder [4†] through relative locality [6†])."

The v1 paper words it "an assumption of the formalism, not a measurement, and one that is *false* in the one exactly solved quantum gravity (2+1 dimensions, where momentum space is a curved group manifold) [T]" (#9 §1).

In this wiki's reading, on the bundle picture the assumption is the choice of fiber metric: general relativity measures every fiber with g⁻¹, so its fibers are flat by construction, and the 2+1-dimensional case is a gravitational theory in which they are curved. The point is negative, as [curved momentum space](/wiki/phase-space/reciprocity/curved-momentum-space#the-programs-framing) puts it: flat fibers are not forced by any measurement, and the statement does not say what geometry the fibers have. [Born's question](/wiki/program/borns-question#flat-momentum-fibers) counts the flat fibers beside the form of the Hamiltonian, the locality of interactions and the mass shell, and the program's reply is [Born's answer](/wiki/gravity/momentum-graviton/borns-answer), set out below.

## The fibers in the program's geometry

### Flat phase space and the momentum metric g̃

The program's kinematic core works on flat phase space. The [lab notebook](/wiki/history/documents/lab-notebook) sets up its kinematics "first on flat 𝒫 ≅ ℝ²ᵈ with coordinates (xᵃ, pₐ), d = 4" (#1 §2; the notebook's words on this page are transcribed from its LaTeX), so each fiber is a copy of ℝᵈ ([P1: the phase-space arena](/wiki/program/postulates/p1-arena)). Its [generalized metric](/wiki/phase-space/born-geometry/born-structures) H, a positive metric on the whole of phase space, splits along the two kinds of direction: "On the x-tilted vacuum, H decomposes into a spacetime metric g_μν(x) and a momentum-space metric g̃^μν" [D, schematic] (#1 §3). The split belongs to the vacuum, the x-tilted one that postulate [P5](/wiki/program/postulates/p5-spontaneous-selection) selects. In this wiki's terms g̃ is the metric of the fibers.

In the notebook's first version g̃ carried the dark-matter gate. The self-interaction of [conjugate matter](/wiki/dark-matter/conjugate-matter) was "routed through the g̃ block", and the gate's support was "set by a scale μ of the g̃ sector" [P] (#1 §3), a form since superseded ([the Gaussian gate of v0.1](/wiki/dark-matter/conjugate-matter/velocity-gate#superseded-the-gaussian-gate-of-v01)). The notebook's sixth open problem asked "why macroscopic momenta don't probe g̃ curvature" (#1 §11 item 6). That is the soccer-ball problem, which no later document takes up ([extensivity](/wiki/phase-space/reciprocity/curved-momentum-space#open-extensivity-the-soccer-ball-problem)).

### Slaved to the base: g̃ = g⁻¹

The [compatibility theorem](/wiki/phase-space/born-geometry/compatibility-theorem) fixes the fibers' metric when the symplectic form ω and the neutral metric η are both held rigid: the positive H compatible with both are exactly H = diag(g, g⁻¹). Calc note #5 draws the third corollary: "**The momentum metric is slaved: g̃ = g⁻¹ pointwise.** No independent momentum-space geometry survives." (§A; [corollary 3](/wiki/phase-space/born-geometry/compatibility-corollaries#corollary-3-the-slaved-momentum-metric)).

In this wiki's reading, g⁻¹ is the metric general relativity puts on its fibers, so with both structures rigid the program's fibers are those of general relativity and its momentum space has no geometry of its own. Calc note #5 states the consequence for the program: "With H = diag(g, g⁻¹), S_H is a functional of g alone: a pure metric theory. No momentum graviton, hence no geometric origin for the χ gate either." (§B; [the collision with the theory as documented](/wiki/phase-space/born-geometry/compatibility-corollaries#the-collision-with-the-theory-as-documented-d--structural)). The collision forced the change from [original P2](/wiki/program/postulates/original-p2) to [P2′](/wiki/program/postulates/p2-prime), under which only ω is rigid and the block form survives only on the vacuum slice: "At X = 0, H = diag(g, g⁻¹): the η-compatible locus of Theorem A is precisely the vacuum slice" (#5 §C).

[The handoff](/wiki/history/documents/handoff) records the comparison with general relativity among results that exist only in the original conversation: "slaved layer g̃ = g⁻¹ is algebraic (Einstein's equation does double duty)" (`HANDOFF.md` §4). No document derives it, and its status is conjecture ([chat-only: the slaved layer is algebraic](/wiki/phase-space/born-geometry/compatibility-corollaries#chat-only-the-slaved-layer-is-algebraic)).

The theorem is proven for a positive-definite g, while the fibers of general relativity carry the Lorentzian g⁻¹. The extension is open ([Open: Lorentzian dressing of the Euclidean skeleton (OP3)](/wiki/phase-space/born-geometry/lorentzian-dressing)).

### A closed base does not close the fibre

The closed-universe note of 2026-10-27 draws a further consequence of the block form [D][V]. In the record's generalized metric the momentum block is Y⁻¹, the same at every momentum p, for any X; so the fibre over each point is flat ℝ³, with dual curvature k̃ = 0, and a closed universe, k = +1, does not induce a closed momentum space (`notes/closed-universe.md` §4). What closure does to the fibres is make momenta discrete, with spacing of order ħ/R on a three-sphere of radius R. The lab notebook's "closed dual space ⇒ negative ΔN_eff" therefore needs a separate postulate of a curved, compact momentum space, which no document states (flag 48 in `review/wiki-build-flags.md`; [a closed Comatter universe](/wiki/cosmology/scale-factor-duality/closed-universe#how-small-momentum-space-gets)). On the closed universe's phase space T\*S³, the note also finds that only the polarization along the fibres is integrable ([reciprocity on a closed space](/wiki/phase-space/reciprocity/closed-space-reciprocity)).

### Independent momentum-space geometry: X

Under P2′ the generalized metric ranges over the values of the [modular field](/wiki/phase-space/modular-field/modular-field-z) Z = X + iY, whose imaginary part is the space-time metric, Im Z = g [D] (#11 §6), and the real part carries what is not slaved. Calc note #5 calls Re Z = X "the momentum graviton", "the local wobble of the emergent polarization, 'which way the x/p split points, here.'", and lists its roles as "momentum geometry and gate mediator (Re Z)" (§C). In this wiki's reading, X tilts the split between position directions and fiber directions from point to point. The withdrawn manuscript [#14](/wiki/dark-matter/candidates/soliton-candidate) states the division: "the baseline momentum-space geometry is slaved (g-tilde = g^-1, det H = 1), and any independent momentum-space geometry resides in the fluctuation X" (§1).

Calc note #5 restates the lab notebook's first open problem in these terms: "Born's debt, restated exactly: *the field equation for momentum-space geometry is the Re Z sector of S_H.*" (§C). #11 §7 gives the program's answer, [Born's answer](/wiki/gravity/momentum-graviton/borns-answer): "momentum-space geometry is dynamical — a reciprocity-odd massive spin-2, its mass born of the polarization choice". The [founding supposition](/wiki/program/founding-suppositions#10-momentum-space-has-its-own-gravity) "Momentum space has its own gravity" is recorded as "vindicated, transformed: dynamical, massive, reciprocity-odd (§7)" (#11 App. A item 10; bold dropped).

#13 adds that X "modifies the dual cone only at short range in momentum [D — §7 of the checkpoint]" (§1), and §6 that "dual-geometric effects are Yukawa-cut in momentum [D — checkpoint §7]". #11 §7 makes neither statement; flag 29 in `review/wiki-build-flags.md`, confirmed by the flags' audit, records that the momentum reading appears only among the chat-only results (`HANDOFF.md` §4). Beyond these one-line statements no document describes how X changes the geometry within one fiber, and none compares the program's momentum-space geometry in detail with Snyder's construction or with relative locality ([the program's own momentum-space geometry](/wiki/phase-space/reciprocity/curved-momentum-space#the-programs-own-momentum-space-geometry)).

### A second light cone

#13 builds its kinematics on the block form: "The broken vacuum equips phase space with H = diag(g, g⁻¹) [D — compatibility theorem]: position space carries the metric g and momentum space its inverse. Each metric defines a null cone." (§1; [two causal cones](/wiki/conjugate-relativity/two-causal-cones)). It calls the dual cone "the causal structure of the *slaved* geometry g⁻¹" (§1). Flag 30 in `review/wiki-build-flags.md` notes that the theorem's g is positive-definite and has no null cone, so the cones need the open Lorentzian dressing; its audit found the tag itself a question of tagging convention. Which momentum-space cone #13 means is also open ([Open: the two dual cones](/wiki/conjugate-relativity/two-cones-inconsistency)).

## Matter on the fibers: the gate

Conjugate matter χ, one of the program's dark-matter candidates, is the "p-polarized" matter of postulate [P4](/wiki/program/postulates/p4-polarized-matter), and the program's account of its self-interaction places its quanta on the fibers.

### Quanta with a width along the fiber

Calc note #6 derives the [velocity gate](/wiki/dark-matter/conjugate-matter/velocity-gate), the factor that switches off χ's self-interaction at large relative velocity, from exchange of the massive X ([the gate mechanism](/wiki/dark-matter/conjugate-matter/gate-mechanism)):

> "The relative-momentum dependence enters through the χ quanta's **intrinsic momentum-space extent**: p-polarized quanta are extended objects on the momentum fiber with width μ, and they exchange X only over their fiber overlap — the dual of how x-extended composites acquire form factors F(qR)." (`notes/debt1a-ii-X-classification.md` §4)

Integrating out the heavy X leaves a contact interaction, one that acts only where the particles meet, so the two quanta interact at one point of space-time. In this wiki's reading their overlap is then taken in the fiber over that point: a contact force acts where two waveforms overlap, and the gate acts only where their spectra overlap as well ([position and momentum exchanged](/wiki/dark-matter/conjugate-matter/gate-mechanism#position-and-momentum-exchanged)).

In the lab notebook the width became a property of the χ quantum itself with the v0.4 addendum, which records #6: "μ is identified as the χ quantum's intrinsic momentum-fiber width, with a Gaussian gate iff the fiber profile is Gaussian" (#1 'Addendum (v0.4)'). #11 §8 writes the gate as F(k²/μ²), with k the incoming relative momentum of the pair, "with μ the χ quantum's intrinsic momentum-fiber width [D — mechanism; shape [O]]". The handoff lists "μ = χ's momentum-fiber width" among the live results (`HANDOFF.md` §2), and calc note #8's close-out lists Debt 2 as "mechanism paid (X-exchange, μ = fiber width); shape completion open (Gaussian vs rational tail — now also an observable discriminant)" (`notes/debt1a-iv-beta-coefficients.md` §5).

The profile along the fiber decides the form of the gate. "Wavepacket overlap of Gaussian profiles gives exactly e^{−(p₁−p₂)²/2μ²} — the postulated gate", but "tree-level exchange with generic vertices yields rational (power-law-tailed) gates; the Gaussian requires the Gaussian fiber profile" (#6 §4). The overlap form and the lab notebook's postulated e^{−k²/μ²} are written in different variables, and no source converts one into the other. Flag 17 in `review/wiki-build-flags.md` records a factor of √2 in μ between them, which its audit found to depend on how #6's form is read, and notes that no stated number changes ([two conventions, not reconciled](/wiki/dark-matter/conjugate-matter/velocity-gate#two-conventions-not-reconciled)).

#13 §4 gives the width a kinematic origin: "The conjugate quantum's invariant extent fixes its intrinsic momentum-space width μ ~ ℏ/λ_χ — which is precisely the gate scale of the dark-matter sector, v\* = √2 μ/m_χ" [D — structural], with λ_χ the extent of a conjugate quantum in position ([the invariant-length shell](/wiki/conjugate-relativity/invariant-length-shell)). The relation between the width in momentum and the extent in position is reciprocal, as between the widths of a spectrum and its waveform ([the time–bandwidth product](/wiki/phase-space/reciprocity/fourier-transform#the-timebandwidth-product)). The relation v\* = √2 μ/m_χ is the lab notebook's (#1 §5.1), and #13's use of it with the fiber width is the combination flag 17 records ([what μ is](/wiki/dark-matter/conjugate-matter/gate-mechanism#what-μ-is)).

### The X propagator on the fibers (OP4)

The shape of the gate depends on how X propagates along the fibers. Calc note #5: "The gate *shape* is the X propagator's structure on the momentum fibers — open [O]" (§E). #11 keeps it as its fourth open problem: "Gate shape (X propagator on momentum fibers; Gaussian vs rational — now observable) [O]" (#11 §14 item 4; [Open: the gate shape (OP4)](/wiki/dark-matter/conjugate-matter/gate-shape)). Calc note #6's closing list ties the Gaussian case to the metastring of [Freidel, Leigh and Minic](/wiki/phase-space/reciprocity/broken-born-duality): "gate-shape completion (Gaussian fiber profile — ties to the metastring's modular vertex structure)" (§5). No document writes the X propagator on the fibers, the χ–X vertex or the profile of a χ quantum along the fiber.

### The dual stress: derivatives along the fiber

X couples to χ through the [dual stress T̃](/wiki/dark-matter/conjugate-matter/dual-stress): "Conjugate matter couples to H universally (P4); its coupling to the X-block is through the **dual stress** T̃ — moments involving momentum-derivatives of the χ bilinear" (#5 §E). Ordinary stress-energy is built from derivatives along space-time, the base [T]; derivatives with respect to momentum are taken along the fibers. No document writes T̃ out, and the strength of the coupling is open ([Open: the dual-stress enhancement (OP5)](/wiki/dark-matter/conjugate-matter/dual-stress-enhancement)).

## What is open

- **The propagator and the profile.** X's propagator on the fibers, the χ–X vertex and a χ quantum's profile along the fiber decide the gate's shape, and none of them is computed (OP4).
- **Geometry within a fiber.** No document works out how X changes the geometry of a single fiber or compares the program's momentum-space geometry with the curved momentum spaces of the literature.
- **Lorentzian signature.** The slaved metric g̃ = g⁻¹ is derived for a positive-definite g (OP3).
- **Extensivity.** The soccer-ball problem stays open on the lab notebook's authority and is absent from #11's list ([curved momentum space](/wiki/phase-space/reciprocity/curved-momentum-space#open-extensivity-the-soccer-ball-problem)).
- **The citations.** #11 §3's references [4]–[6], including the 2+1-dimensional result behind "false in the one exactly solved quantum gravity", are from model memory and await the † literature battery (OP10).

The registered items are listed in [open problems and the queue](/wiki/status/open-problems).

## Standard references

Added by the wiki from model memory (†); the program's documents do not cite them.

- V. I. Arnold, *Mathematical Methods of Classical Mechanics* (1978)†: the cotangent bundle, its symplectic form and Hamiltonian mechanics on it.
- R. Abraham and J. E. Marsden, *Foundations of Mechanics*, 2nd edition (1978)†: the same, with geodesic motion as a Hamiltonian flow on the cotangent bundle.
- C. W. Misner, K. S. Thorne and J. A. Wheeler, *Gravitation* (1973)†: the momentum space at an event and the mass hyperboloid, in kinetic theory on curved space-time.
- N. M. J. Woodhouse, *Geometric Quantization* (1980)†: the vertical polarization of a cotangent bundle.

## Used by

- [Born's question](/wiki/program/borns-question) — general relativity's flat momentum fibers as one source of the asymmetry between position and momentum.
- [Born's answer: momentum space gravitates](/wiki/gravity/momentum-graviton/borns-answer) — the program's reply: momentum-space geometry is dynamical and carried by X.
- [Corollaries: unimodularity, no B-field, slaved momentum metric](/wiki/phase-space/born-geometry/compatibility-corollaries) — g̃ = g⁻¹, the fiber metric fixed by g.
- [The modular field Z = X + iY](/wiki/phase-space/modular-field/modular-field-z) — X as the carrier of independent momentum-space geometry.
- [The gate mechanism: X exchange over fiber overlap](/wiki/dark-matter/conjugate-matter/gate-mechanism) — χ quanta of width μ along the fibers.
- [The velocity gate](/wiki/dark-matter/conjugate-matter/velocity-gate) — μ as "the χ quantum's intrinsic momentum-fiber width" in #11 §8.
- [Open: the gate shape (OP4)](/wiki/dark-matter/conjugate-matter/gate-shape) — the X propagator on the momentum fibers.
- [Dual stress T̃](/wiki/dark-matter/conjugate-matter/dual-stress) — momentum derivatives of the χ bilinear.
- [Two causal cones](/wiki/conjugate-relativity/two-causal-cones) — a second light cone on the momentum block g⁻¹.
- [The invariant-length shell and Planck closure](/wiki/conjugate-relativity/invariant-length-shell) — μ ~ ℏ/λ_χ read as the fiber width.
- [A closed Comatter universe](/wiki/cosmology/scale-factor-duality/closed-universe) — the fibre stays flat when the base is closed; closure makes momenta discrete.
- [Reciprocity on a closed space](/wiki/phase-space/reciprocity/closed-space-reciprocity) — the polarization along the fibres is the only integrable one on T\*S³.

## Sources

- `papers/broken-born-checkpoint-v2.md` §3 and refs [4]–[6] — the flat fibers as "an architectural assumption, not a measurement" and the curved-momentum lineage (all †); §5 — the compatibility theorem [T][V] and g̃ = g⁻¹ slaved; §6 — Im Z = g; §7 — Born's answer; §8 — μ as the fiber width; §14 item 4 — the X propagator on the fibers; App. A item 10 — "vindicated, transformed"
- `notes/debt1a-geometric-core.md` §A — corollary 3, the slaved momentum metric; §B — the collision with the documented theory; §C — the vacuum slice, X as momentum geometry, Born's debt as the Re Z sector; §E — the dual stress, the gate shape as the X propagator on the fibers
- `notes/debt1a-ii-X-classification.md` §4 — quanta extended on the fiber, exchange over the fiber overlap, Gaussian and rational gates; §5 — the Gaussian fiber profile and the metastring
- `notes/debt1a-iv-beta-coefficients.md` §5 — Debt 2's mechanism paid with "μ = fiber width", shape open
- `notes/broken-born-theory.md` §2 — flat phase space ℝ²ᵈ; §3 — H split into g and g̃, the v0.1 gate through g̃; §11 item 6 — "g̃ curvature"; 'Addendum (v0.4)' — μ as the fiber width; §5.1 — v\* ≡ √2μ/m_χ
- `notes/broken-born-program-v1.md` §1 — the flat fibers, tagged [T]
- `notes/knot-dark-matter-standalone.md` §1 — independent momentum-space geometry resides in X (withdrawn manuscript)
- `papers/conjugate-special-relativity.md` §1 — the block form, the dual cone of g⁻¹, X "at short range in momentum"; §4 — μ ~ ℏ/λ_χ; §6 — "Yukawa-cut in momentum"
- `HANDOFF.md` §2 — "μ = χ's momentum-fiber width"; §4 — the chat-only "slaved layer g̃ = g⁻¹ is algebraic"
- `review/wiki-build-flags.md` items 17, 29, 30 — the two gate conventions and the √2 in μ; #13's citation of #11 §7; #13's tag on its cones
- `notes/closed-universe.md` §4, §5 and `verify/closed_universe.py` section E (E1, E2, E4) — the flat fibre over a closed base, the discrete momenta and the integrable polarization; computed, not reviewed
- `review/wiki-build-flags.md` item 48 — a closed universe does not close momentum space; awaiting Paul's ruling
