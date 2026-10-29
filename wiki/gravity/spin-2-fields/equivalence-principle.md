---
title: "The equivalence principle: free fall and local inertial frames"
weight: 15
status: established
description: "Gravity acts on every body alike: the weak form (universality of free fall), Einstein's form (local inertial frames; uniform acceleration indistinguishable from a uniform field) and the strong form; free-falling and Rindler frames; tidal effects as the limit of 'local'; how minimal coupling builds it in; the tests; and the program's uses: P4's universal coupling, χ on g, #13's dual reading and the chat-only dual equivalence principle."
provenance: [T]
sources:
  - "papers/broken-born-checkpoint-v2.md §4"
  - "papers/broken-born-checkpoint-v2.md §5"
  - "papers/broken-born-checkpoint-v2.md §6"
  - "papers/broken-born-checkpoint-v2.md §8"
  - "papers/broken-born-checkpoint-v2.md §11.1"
  - "papers/conjugate-special-relativity.md §5"
  - "papers/conjugate-special-relativity.md §6"
  - "HANDOFF.md §2"
  - "HANDOFF.md §4"
  - "notes/broken-born-theory.md §1"
  - "notes/broken-born-theory.md §3"
  - "notes/broken-born-theory.md §4"
  - "notes/stream-stability.md 'Setup'"
---

*The equivalence principle is the statement that gravity acts on every body in the same way. In its weak form, the universality of free fall, a body released at a given place with a given velocity follows the same path whatever it is made of. In Einstein's form, a small enough freely falling laboratory is an inertial frame, one in which a body on which no force acts moves in a straight line at constant speed, and the laws of [special relativity](/wiki/conjugate-relativity/special-relativity) hold in it. Equivalently, a laboratory accelerating uniformly through empty space cannot be told apart from one held at rest in a uniform gravitational field. [General relativity](/wiki/gravity/spin-2-fields/general-relativity) builds the principle in by coupling all matter and energy to one spacetime metric. The program postulates it for both of its kinds of matter: [postulate P4](/wiki/program/postulates/p4-polarized-matter) couples ordinary matter and [conjugate matter χ](/wiki/dark-matter/conjugate-matter) to the same geometry, so χ falls, orbits and bends light like any other dark matter. Separately, the paper on [conjugate special relativity](/wiki/conjugate-relativity) (#13) reads the principle as the relativity principle of the momentum [polarization](/wiki/phase-space/reciprocity/lagrangian-polarizations), the program's mirror description in which momentum plays the part of position. That reading is a claim of the program, alive but unreviewed, with its own page: [the equivalence principle as dual relativity](/wiki/conjugate-relativity/equivalence-principle).*

**Status:** Established — [T] — textbook physics, written here from general knowledge; the program's documents cite no source for the principle itself, and the references below are added from model memory (†). The program's uses carry their own tags: the universal coupling of postulate P4 [P] (#11 §4); conjugate matter that "falls, orbits, and lenses like ordinary dark matter" [D] ([the lab notebook](/wiki/history/documents/lab-notebook), #1 §4), restated in [checkpoint #11](/wiki/history/documents/checkpoint) §8; #13's reading of the principle as the dual relativity principle [D — structural] (#13 §5). Nothing on this page is machine-checked.

## The weak form: universality of free fall [T]

A test body is one small enough that its own gravity, and the change of the gravitational field across it, can be neglected, and on which no force other than gravity acts. The weak equivalence principle says that the path of a test body through spacetime is fixed by where it starts and with what velocity. It does not depend on the body's mass, composition or internal structure. Galileo argued from falling bodies and pendulums that bodies of different weight fall together (Galileo 1638†).

In Newton's theory the principle is the equality of two masses. A body's inertial mass m_inert measures its resistance to acceleration, in the second law of motion. Its passive gravitational mass m_grav measures how strongly a gravitational field acts on it, as electric charge measures how strongly an electric field acts. With Φ the Newtonian gravitational potential, a body at position x moves according to

```text
m_inert · d²x/dt² = −m_grav · ∇Φ(x)

d²x/dt² = −(m_grav/m_inert) · ∇Φ(x)
```

If the ratio m_grav/m_inert is the same for every body, every body at a given place falls with the same acceleration, and units can be chosen so that the ratio is 1. Nothing in Newton's laws requires this. It is a fact of observation, which Newton tested with pendulums of different materials (Newton 1687†). In an electric field the corresponding ratio, charge over inertial mass, differs from one body to another, and so do the accelerations.

## Einstein's form: local inertial frames [T]

Einstein took the equality of the two masses as a principle and extended it beyond the motion of bodies (Einstein 1907†). If every body near a freely falling observer falls with the observer, then relative to the observer nothing falls: a body released at rest stays at rest, and a body thrown moves in a straight line at constant speed. Over a small region, gravity then has no detectable effect on the motion of bodies relative to the observer, and the observer's laboratory is an inertial frame. Einstein's equivalence principle states that this holds for all of physics:

- in a freely falling laboratory small enough that the variation of the gravitational field across it can be neglected, every experiment that does not itself involve gravity gives the results of special relativity;
- a laboratory accelerating uniformly through a region without gravity cannot be told apart, by any experiment confined to it, from a laboratory held at rest in a uniform gravitational field.

The two statements are one statement. A laboratory held at rest in a gravitational field is accelerating upward relative to the freely falling laboratories around it, as a rocket accelerates relative to the inertial frames of empty space.

The standard modern statement divides the principle into three parts (Will 2014†): the weak form above; local Lorentz invariance, that the result of such an experiment does not depend on the velocity of the freely falling laboratory; and local position invariance, that it does not depend on where or when the experiment is done. Einstein used the principle as the step from special to general relativity. Since all bodies fall alike, their free-fall paths can be treated as a property of spacetime itself, the geodesics of its metric, which are the straightest paths the metric allows, rather than as the effect of a force ([minimal coupling and free fall](/wiki/gravity/spin-2-fields/general-relativity#minimal-coupling-and-free-fall-t)).

### The strong form [T]

The strong equivalence principle extends Einstein's form in two directions: to experiments that do involve gravity, such as a laboratory measurement of the attraction between two masses, and to bodies whose own gravity is not negligible, such as a planet or a star, part of whose mass-energy is gravitational binding energy. General relativity satisfies it. Theories that add a long-range field to gravity, such as scalar–tensor theories, generally do not, and in them a massive body's gravitational binding energy can fall at a different rate from the rest of its mass (Nordtvedt 1968†; Will 2014†). The program's documents do not discuss the strong form.

## Free fall and Rindler frames [T]

### Free fall

A freely falling frame is the frame of an observer on whom no force other than gravity acts, such as an astronaut in an orbiting spacecraft or a laboratory dropped down a shaft. Released objects float beside the observer, and an accelerometer reads zero. In general relativity the observer's worldline, its path through spacetime, is a geodesic, and the frame is locally inertial. An observer standing on the ground is the one who accelerates: the ground pushes the observer upward, off the geodesic, and an accelerometer held there reads an upward acceleration of the size that Newton's theory attributes to gravity.

### Rindler frames

**Uniform acceleration.** In special relativity, uniform acceleration means a constant proper acceleration a, the acceleration measured in the body's own momentary rest frame. A body that starts from rest at z = c²/a at time t = 0 and accelerates uniformly along z follows a hyperbola in spacetime,

```text
z² − c²t² = (c²/a)²
```

so that its speed approaches c without reaching it. A rigid laboratory built around this body, each point of which keeps a fixed distance from the body as measured in the laboratory, is a Rindler frame (Rindler 1966†). In coordinates attached to the frame, with the body as the reference point z′ = 0, t′ the time on its clock and z′ the height above it measured in the frame, the inertial coordinates are

```text
ct = (c²/a + z′) · sinh(at′/c)        z = (c²/a + z′) · cosh(at′/c)
```

and the metric of flat spacetime, with x and y the two transverse directions and time entering with the minus sign, becomes

```text
ds² = −(1 + az′/c²)² c² dt′² + dx² + dy² + dz′²
```

The reference point z′ = 0 has proper acceleration a. A point at height z′ has proper acceleration c²/(z′ + c²/a), smaller above the reference point and larger below it.

**A uniform field.** An object released in the frame moves at constant velocity in the inertial coordinates while the laboratory accelerates away from it. In the laboratory's description the object falls toward −z′, and every object released at the same place with the same velocity falls in the same way, whatever it is made of. For heights small compared with c²/a,

```text
g′₀₀ = −(1 + az′/c²)² ≈ −(1 + 2az′/c²)
```

which is the form the time component of the metric takes in a weak static gravitational field with Newtonian potential Φ, g₀₀ ≈ −(1 + 2Φ/c²), for Φ = az′: the potential of a uniform field of strength a, pointing toward −z′. Over heights small compared with c²/a the frame is therefore equivalent to a uniform gravitational field. For a real gravitational field the equivalence holds only locally, because a real field has tidal effects and a Rindler frame, which is flat spacetime, has none ([below](#why-the-principle-is-local-tidal-effects-t)).

**Clocks and light.** Since the metric does not change with t′, the proper time τ of a clock held at height z′, the time the clock itself reads, advances as dτ = (1 + az′/c²) dt′: the higher the clock, the faster it runs. Light sent upward from z′ = 0 to a receiver at height h arrives with its frequency lowered by the factor 1/(1 + ah/c²), a fractional shift of about −ah/c² for small heights. By the equivalence principle the same shift occurs for light climbing through a height h in a uniform gravitational field of strength a. In a weak static field the fractional shift is −ΔΦ/c², with ΔΦ the rise in potential: the gravitational redshift (Einstein 1911†), measured in the laboratory with gamma rays sent between the top and the bottom of a tower (Pound and Rebka 1960†).

**The horizon.** The proper acceleration c²/(z′ + c²/a) needed to stay at a fixed height grows without bound as z′ approaches −c²/a. That surface is a horizon of the frame: no signal from beyond it ever reaches the frame's observers. Over small distances the region just outside a black hole's horizon looks like a Rindler frame near its horizon, so a body held at fixed height there needs an acceleration that grows without bound as the horizon is approached [T]. The chat-only conjecture on [momentum-space black holes](/wiki/conjugate-relativity/momentum-space-black-holes) concerns the force such hovering requires.

## Why the principle is local: tidal effects [T]

A gravitational field that varies from place to place cannot be removed by a single choice of frame. Two bodies falling side by side toward the Earth move along lines that converge on its centre, so they draw together; two bodies falling one above the other draw apart, because the lower one is pulled more strongly. These relative accelerations are tidal effects. Instruments spread over enough distance in a freely falling laboratory, or watched for long enough, detect them. The equivalence principle holds only for regions small enough, and times short enough, that tidal effects fall below the precision of the experiment.

In Newton's theory, two nearby bodies whose positions differ by a small displacement δx have a relative acceleration set by the second derivatives of the potential. In general relativity the curvature plays that role: two neighbouring free-fall worldlines with four-velocity u^μ = dx^μ/ds and separation δx^μ obey the equation of geodesic deviation.

```text
Newton:                d²δxⁱ/dt² = −(∂ᵢ∂ⱼΦ) δxʲ

general relativity:    D²δx^μ/ds² = −R^μ_νρσ u^ν δx^ρ u^σ
```

Repeated indices are summed. D/ds is the covariant derivative along the worldline, s is the proper time along it, as in the geodesic equation, and R^μ_νρσ is the Riemann curvature tensor ([the metric and its curvature](/wiki/gravity/spin-2-fields/general-relativity#the-metric-and-its-curvature-t)). For slow motion in a weak field, in units with c = 1, the components R^i_0j0 reduce to ∂ᵢ∂ⱼΦ and the two equations agree. The uniform part of a gravitational field is the part a change of frame removes. The curvature is the part that remains, and it is what distinguishes a gravitational field from an accelerated frame in flat spacetime.

## How general relativity builds it in [T]

General relativity contains the principle through two properties of the theory ([minimal coupling and free fall](/wiki/gravity/spin-2-fields/general-relativity#minimal-coupling-and-free-fall-t)).

**Local inertial coordinates.** At any event P, coordinates can be chosen in which

```text
g_μν(P) = η_μν        ∂_λ g_μν(P) = 0        hence  Γ^λ_μν(P) = 0
```

Here η_μν is the Minkowski metric of special relativity, the textbook symbol, which is unrelated to the program's neutral metric η on phase space ([the structures ω, η, H](/wiki/phase-space/born-geometry/born-structures)), and Γ^λ_μν are the Christoffel symbols. At P the metric takes its special-relativistic form and the Christoffel symbols vanish, so the geodesic equation reduces there to d²x^μ/ds² = 0: a free body moves in a straight line at constant speed, as in an inertial frame. The second derivatives of the metric cannot all be removed in this way; they carry the curvature of the previous section. Such local inertial coordinates, of which Riemann normal coordinates are a standard construction, are the mathematical form of a small freely falling laboratory at the event P.

**Minimal coupling.** Matter enters general relativity through the matter action of special relativity, with the Minkowski metric replaced by g_μν, derivatives replaced by covariant derivatives, and no other gravitational field and no explicit curvature term. In local inertial coordinates at P the matter equations then take their special-relativistic form, which is Einstein's form of the principle. Every test body, whatever it is made of, follows a geodesic of the same metric, which is the weak form. Every form of energy, the binding energy of a nucleus and the energy of the electromagnetic field inside a body included, enters the stress-energy tensor T_μν and couples to the same g with the same strength ([stress-energy as the charge of gravity](/wiki/dark-matter/conjugate-matter/dual-stress#background-stress-energy-as-the-charge-of-gravity-t)).

**What would violate it.** A second long-range field that coupled to matter with a strength depending on composition, for example in proportion to the number of baryons (protons and neutrons) rather than to the energy, would give bodies of different materials different accelerations and violate the weak form ([fifth forces and how they are tested](/wiki/cosmology/dark-energy/tau-fifth-force#fifth-forces-and-how-they-are-tested-t)).

**Why one massless graviton forces it.** Read as a field theory on flat spacetime, general relativity is the theory of one massless spin-2 field coupled to itself and to matter, and the consistency of such a field's interactions at low energy forces its coupling to matter to be universal (Weinberg 1964†). In that reading the equivalence principle is a consequence rather than an assumption ([one massless graviton is general relativity](/wiki/gravity/spin-2-fields/general-relativity#one-massless-graviton-is-general-relativity-t)).

## Tests [T]

The weak form is tested by comparing the free fall of bodies of different composition. The other parts of Einstein's form are tested by comparing clocks and other instruments at different velocities and gravitational potentials (Will 2014†, a review).

- **Torsion balances.** Eötvös hung masses of two materials from the ends of a beam on a thin fibre. If the ratio of gravitational to inertial mass differed between the materials, the pull of the Earth and the centrifugal effect of the Earth's rotation would combine differently on them, and the fibre would twist (Eötvös, Pekár and Fekete 1922†). Later torsion balances compared the fall of two materials toward the Sun or toward the Earth (Roll, Krotkov and Dicke 1964†; Schlamminger et al. 2008†). The same instruments search for new long-range forces whose strength depends on composition ([fifth-force safety of the dark-energy field τ](/wiki/cosmology/dark-energy/tau-fifth-force)).
- **The Moon.** Laser pulses reflected from mirrors placed on the Moon measure the distance between the Earth and the Moon by their travel time. The two bodies fall together toward the Sun. If they fell at different rates, because of their different compositions or, under a violation of the strong form, their different gravitational binding energies, the Moon's orbit would be displaced along the direction of the Sun (Nordtvedt 1968†; Williams, Turyshev and Boggs 2004†).
- **In orbit.** A satellite carrying two test masses of different materials compared their free fall around the Earth (Touboul et al. 2017†, 2022†).
- **Clocks.** The gravitational redshift, measured in the laboratory by Pound and Rebka (1960†), tests local position invariance.

All of these find the principle satisfied within their precision. The program's documents cite none of them and quote no bound, so this page gives none.

## How the program uses it

**One gravity for both kinds of matter.** Postulate P4 [P] (#11 §4): "Matter comes in x-polarized (Standard Model) and p-polarized (χ) representations; both couple universally to H; gauge forces do not cross polarizations." H is the [generalized metric](/wiki/phase-space/born-geometry/born-structures) on phase space, parametrized by the [modular field](/wiki/phase-space/modular-field/modular-field-z) Z, whose real part X is the [momentum graviton](/wiki/gravity/momentum-graviton) and whose imaginary part is the spacetime metric g [D] (#11 §6). On the vacuum slice X = 0, H takes the block form H = diag(g, g⁻¹) (#11 §5, §6; [the compatibility theorem](/wiki/phase-space/born-geometry/compatibility-theorem)). Both kinds of matter therefore couple to the same g, as ordinary matter does through minimal coupling in general relativity. The lab notebook's form of the postulate names the principle: "Both couple universally to H — the equivalence principle holds across polarizations" [P] (#1 §1, transcribed from its LaTeX). Its action leaves ordinary matter as general relativity has it: "S_x is the Standard Model minimally coupled to g. Nothing is modified. [P4]" (#1 §3). The notebook is superseded as a reference ([one gravity for both](/wiki/program/postulates/p4-polarized-matter#one-gravity-for-both)).

**Conjugate matter falls, orbits and lenses.** The notebook draws the consequence [D]: "χ couples to g universally: it falls, orbits, and lenses like ordinary dark matter. Bullet Cluster lensing-centroid behavior is automatic (and see Prediction 1 for the scattering side)" (#1 §4). #11 keeps it in a clause of its section on conjugate matter: "χ propagates on g (equivalence principle; Bullet-Cluster-safe)" (#11 §8). By the weak form, χ follows the same free-fall paths as ordinary matter; and since its energy enters the stress-energy that curves the same g, it deflects passing light as any other mass does. In the Bullet Cluster, a collision of two galaxy clusters, the mass that gravitational lensing maps moved on with the galaxies, ahead of the hot gas [T] ([the Bullet Cluster](/wiki/dark-matter/halo-astrophysics/bullet-cluster)). For χ the lensing side of that observation is this coupling, and the scattering side is the [velocity gate](/wiki/dark-matter/conjugate-matter/velocity-gate), which for particle χ is closed at cluster collision speeds ([the χ-particle candidate](/wiki/dark-matter/candidates/chi-particles); [Row 1: the knee in σ_T(v)](/wiki/predictions/self-interaction-knee)).

**Gravity as the one link.** P4 lets no gauge force (such as the electromagnetic, weak or strong interaction) act across the two sectors, and its strict reading, in force since v2.1, excludes [kinetic mixing](/wiki/dark-matter/candidates/soliton-candidate/kinetic-mixing#what-kinetic-mixing-is) between them (a term in the action coupling the field strengths of the two sectors' photons) beyond what gravity induces (#11 §4). Conjugate matter then reaches ordinary matter through gravity alone, the basis of [Row 7: a permanent null in direct detection](/wiki/predictions/direct-detection-null). Anything built from conjugate matter gravitates, as #11 says of conjugate monopoles: "by P4, conjugate-sector solitons gravitate" (#11 §11.1; [conjugate monopoles as ontology](/wiki/electric-magnetic-duality/conjugate-monopoles)).

**Both polarizations fall alike.** #13 §6, on what the breaking of [reciprocity](/wiki/phase-space/reciprocity/born-reciprocity), the symmetry that exchanges position and momentum, leaves common to the two polarizations: "Shared: the time coordinate (in the 3+1 presentation used here) and the massless graviton, so both polarizations fall identically." The sentence carries no tag; in #11 the same consequence rests on a postulate, P4 ([what the two polarizations share](/wiki/conjugate-relativity/equivalence-principle#what-the-two-polarizations-share)).

**#13's dual reading.** Conjugate special relativity transcribes special relativity into the momentum polarization, with the rate of change of momentum dp/dt, a force, in place of velocity. Its dual-inertial frames are those of constant dp/dt: "rest (dp/dt = 0, i.e., force-free motion — our free fall) and uniform dual motion (constant force — our Rindler frames)" (#13 §5; [dual inertia: free fall as rest](/wiki/conjugate-relativity/dual-inertia)). In #13's reading, the two kinds of frame on this page are thus the rest state and the uniform motion of the momentum polarization, and #13 records [D — structural] that "the dual principle of relativity — equivalence of all force-free frames — is the equivalence principle", arrived at "from kinematics rather than gravitation" (#13 §5). The identification uses the general-relativistic reading of free fall, in which no force acts on a falling body ([which reading of free fall](/wiki/conjugate-relativity/dual-inertia#which-reading-of-free-fall)), and #13 does not say which of the forms above it means. The reading is a claim of the program, alive and unreviewed: `HANDOFF.md` §2 lists it among the alive results without the ✓ it uses for machine-verified items, no review round has covered #13, and #11 does not mention it. Its home is [the equivalence principle as dual relativity](/wiki/conjugate-relativity/equivalence-principle).

**A chat-only question: a dual equivalence principle.** The [handoff](/wiki/history/documents/handoff)'s list of results that exist only in the original chat gives gravity two charges, ordinary stress-energy as the source of the massless graviton and [dual stress](/wiki/dark-matter/conjugate-matter/dual-stress) as the source of the [momentum graviton X](/wiki/gravity/momentum-graviton), and ends: "equivalence principle intact; whether invariant length λ and dual charge lock together = 'dual equivalence principle' open question" (`HANDOFF.md` §4). In this wiki's reading, the name follows the Newtonian form of the weak principle, in which gravitational charge is locked to inertial mass. The question is whether the charge that sources X is locked in the same way to the invariant length λ_χ of a conjugate quantum ([the invariant-length shell](/wiki/conjugate-relativity/invariant-length-shell)), which #13 §5, in a statement it marks conjecture-tier, makes "the measure of resistance to force-*change*". No document goes further than posing the question, and its status is conjecture ([the open question: a dual equivalence principle](/wiki/gravity/momentum-graviton/chat-only-results#the-open-question-a-dual-equivalence-principle)).

## References

The program's documents cite no source for the equivalence principle. Added by the wiki from model memory (†):

- Galileo Galilei, *Two New Sciences* (1638)†: falling bodies and pendulums.
- I. Newton, *Principia* (1687)†: pendulums of different materials.
- A. Einstein (1907)†: the principle and its use toward general relativity; (1911)†: the gravitational redshift and the deflection of light derived from it.
- R. v. Eötvös, D. Pekár, E. Fekete (1922)†: the torsion-balance comparison of materials.
- R. V. Pound, G. A. Rebka (1960)†: the gravitational redshift measured in a tower.
- S. Weinberg (1964)†: a massless spin-2 field's couplings to matter must be universal.
- P. G. Roll, R. Krotkov, R. H. Dicke (1964)†; S. Schlamminger et al. (2008)†: torsion-balance tests.
- W. Rindler (1966)†: the uniformly accelerated frame.
- K. Nordtvedt (1968)†: the strong form and the free fall of gravitational binding energy.
- J. G. Williams, S. G. Turyshev, D. H. Boggs (2004)†: lunar laser ranging.
- P. Touboul et al. (2017, 2022)†: the satellite test.
- C. M. Will, "The confrontation between general relativity and experiment", *Living Reviews in Relativity* (2014)†: the forms of the principle and their tests, a review.
- C. W. Misner, K. S. Thorne, J. A. Wheeler, *Gravitation* (1973)†: local inertial frames, geodesic deviation and the uniformly accelerated observer.

## Used by

- [P4: polarized matter and strict sector separation](/wiki/program/postulates/p4-polarized-matter) — both kinds of matter couple universally to H, so the principle holds across polarizations.
- [The χ-particle candidate](/wiki/dark-matter/candidates/chi-particles) — χ falls, orbits and lenses like ordinary dark matter.
- [The velocity gate](/wiki/dark-matter/conjugate-matter/velocity-gate) — "χ propagates on g (equivalence principle; Bullet-Cluster-safe)", beside the gated self-interaction.
- [Row 1: the knee in σ_T(v)](/wiki/predictions/self-interaction-knee) — the gravitational side of cluster collisions.
- [Row 7: a permanent null in direct detection](/wiki/predictions/direct-detection-null) — dark matter that reaches ordinary matter through gravity alone.
- [Conjugate monopoles as ontology](/wiki/electric-magnetic-duality/conjugate-monopoles) — conjugate-sector objects gravitate.
- [Founding suppositions and their fates](/wiki/program/founding-suppositions) — supposition 4, dark matter as conjugate matter that "propagates on g".
- [Dual stress T̃](/wiki/dark-matter/conjugate-matter/dual-stress) — the universal coupling through stress-energy, beside which X's coupling through dual stress is set.
- [Dual inertia: free fall as rest](/wiki/conjugate-relativity/dual-inertia) — free fall and Rindler frames as the dual-inertial class.
- [The equivalence principle as dual relativity](/wiki/conjugate-relativity/equivalence-principle) — #13's reading of the principle.
- [Two gravitational charges and the conjugate field equations (chat-only)](/wiki/gravity/momentum-graviton/chat-only-results) — "equivalence principle intact", and the dual equivalence principle.
- [The invariant-length shell and Planck closure](/wiki/conjugate-relativity/invariant-length-shell) — λ_χ, the quantity a dual equivalence principle would lock to the dual charge.
- [The gated Vlasov model](/wiki/dark-matter/momentum-clumping/gated-vlasov-model) — ordinary gravity enters a dark-matter particle's energy as mΦ_grav(x), with the same m as its kinetic energy p²/2m; the model is the setup of the calculations that killed [velocity clumping](/wiki/dark-matter/momentum-clumping/founding-image).

## Sources

- `papers/broken-born-checkpoint-v2.md` §4 — P4, universal coupling to H, and its strict reading; §5, §6 — H = diag(g, g⁻¹) on the vacuum slice X = 0, with Im Z = g; §8 — "χ propagates on g (equivalence principle; Bullet-Cluster-safe)"; §11.1 — "by P4, conjugate-sector solitons gravitate".
- `papers/conjugate-special-relativity.md` §5 — the dual-inertial class of free fall and Rindler frames, the dual principle of relativity as the equivalence principle [D — structural], and λ_χ as the resistance to force-change (conjecture-tier); §6 — the shared massless graviton, "so both polarizations fall identically".
- `HANDOFF.md` §2 — #13's reading in the alive list, without a ✓; §4 — the chat-only two gravitational charges and the "dual equivalence principle" question.
- `notes/broken-born-theory.md` §1 — the notebook's P4, "the equivalence principle holds across polarizations"; §3 — the Standard Model minimally coupled to g; §4 — χ "falls, orbits, and lenses like ordinary dark matter" [D] (superseded as reference).
- `notes/stream-stability.md` 'Setup' — the gravitational term mΦ_grav(x) in the single-particle energy of the gated Vlasov model.
