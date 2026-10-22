---
title: "General relativity and the graviton"
weight: 10
status: established
description: "The metric, the Einstein–Hilbert action and minimal coupling; the equivalence principle, free fall and Rindler frames; linearized diffeomorphisms, the massless spin-2 graviton and its uniqueness — the template for the program's second field X."
provenance: [T]
sources:
  - "papers/broken-born-checkpoint-v2.md §3"
  - "papers/broken-born-checkpoint-v2.md §4"
  - "papers/broken-born-checkpoint-v2.md §5"
  - "papers/broken-born-checkpoint-v2.md §6"
  - "papers/broken-born-checkpoint-v2.md §7.1"
  - "papers/broken-born-checkpoint-v2.md §7.5"
  - "papers/broken-born-checkpoint-v2.md §13"
  - "papers/conjugate-special-relativity.md §5"
  - "papers/conjugate-special-relativity.md §6"
  - "notes/debt1a-geometric-core.md §B"
  - "notes/debt1a-geometric-core.md §D"
  - "notes/debt1a-ii-X-classification.md §2"
  - "notes/debt1a-iii-tuning-test.md §4"
  - "notes/debt1a-iv-beta-coefficients.md §3"
  - "notes/broken-born-theory.md §1"
  - "notes/broken-born-theory.md §3"
  - "notes/broken-born-theory.md §4"
  - "HANDOFF.md §4"
---

*General relativity is Einstein's theory of gravity. A single field, the spacetime metric g_μν, fixes distances and durations; its curvature is gravity; and a freely falling body follows the straightest path the metric allows, feeling no force. Small ripples of the metric about flat spacetime are the graviton, a massless spin-2 field whose gauge symmetry is the linearized form of a change of coordinates (a diffeomorphism), and a single such field that couples consistently to itself and to matter rebuilds general relativity. The program keeps general relativity as the long-range gravity of ordinary matter; its second, massive spin-2 field reaches ordinary matter only at gravitational strength and over a short range. It uses the graviton as the template for that second field, the [momentum graviton X](/wiki/gravity/momentum-graviton), whose local symmetry is a second copy of the same linearized diffeomorphisms, and its [conjugate special relativity](/wiki/conjugate-relativity) [reads the equivalence principle as the relativity principle of the momentum polarization](/wiki/conjugate-relativity/equivalence-principle).*

**Status:** Established — [T] — textbook physics, written here from general knowledge; the program's documents cite no general-relativity source, and the references below are added from model memory (†). The program's uses of it carry their own tags: X's [dual diffeomorphisms](/wiki/gravity/momentum-graviton/dual-diffeomorphisms) [D + T] ([#11](/wiki/history/documents/checkpoint) §7.1), the universal coupling of postulate [P4](/wiki/program/postulates/p4-polarized-matter) [P] (#11 §4), and the equivalence principle as a dual relativity principle [D — structural] (#13 §5). Nothing on this page is machine-checked.

## The metric and its curvature [T]

General relativity describes spacetime as a four-dimensional manifold carrying a metric g_μν(x), a symmetric tensor field. The line element

```text
ds² = g_μν(x) dx^μ dx^ν
```

gives the interval between two neighbouring events: the proper time read by a clock that passes through both, or the proper distance between them when they are simultaneous. The signature is Lorentzian. One direction, time, enters with the opposite sign to the three space directions, and that sign is what gives every event a light cone separating its possible causes and effects from the events it cannot influence ([special relativity](/wiki/conjugate-relativity/special-relativity)).

In flat spacetime and inertial coordinates the metric takes a constant form, the Minkowski metric. A gravitational field is a departure of g_μν from that form which no change of coordinates removes; that coordinate-independent content is the curvature. From the metric comes the one connection that preserves it and has no torsion, the Levi-Civita connection, whose components are the Christoffel symbols Γ^λ_μν. From the connection come the Riemann curvature tensor, its contraction the Ricci tensor R_μν, and the curvature scalar R. ([The Born connection](/wiki/phase-space/born-geometry/born-connection) is the analogous object for the program's phase-space structures.)

## The Einstein–Hilbert action and the field equations [T]

The dynamics of the metric come from the Einstein–Hilbert action, to which the action of the matter fields ψ is added:

```text
S = S_EH[g] + S_matter[ψ; g],        S_EH ∝ M_P² ∫ d⁴x √−g R
```

Here √−g is the square root of minus the determinant of g_μν, the factor that turns d⁴x into an invariant volume, and M_P is the Planck mass, which sets the strength of gravity through Newton's constant G. Varying S with respect to g_μν gives Einstein's field equations, G_μν ∝ T_μν: the Einstein tensor G_μν, built from R_μν and R, is proportional to the stress-energy tensor T_μν of the matter, with the constant fixed by G.

Three properties of this action matter for the rest of the section:

- **General covariance.** The action is unchanged by diffeomorphisms, the smooth changes of coordinates x^μ → x′^μ(x). Two metrics related by such a change describe the same physics.
- **Two derivatives.** The field equations contain at most second derivatives of the metric. The [multi-graviton no-go theorem](/wiki/gravity/spin-2-fields/multi-graviton-no-go) is stated for theories of this kind.
- **Constrained components.** Not every component of g_μν propagates. In the Hamiltonian formulation of Arnowitt, Deser and Misner, g₀₀ and g₀ᵢ enter through the lapse and the shift, which appear in the action without time derivatives and act as Lagrange multipliers. Their constraints, together with the freedom to choose coordinates, remove every component except the physical polarizations, including the components that would otherwise carry negative energy. This is the property that a mass term for a spin-2 field must not destroy ([the Fierz–Pauli mass term and the Boulware–Deser ghost](/wiki/gravity/spin-2-fields/fierz-pauli)).

## Minimal coupling and free fall [T]

Matter enters through S_matter[ψ; g], the matter action of special relativity with the Minkowski metric replaced by g_μν and partial derivatives replaced by covariant derivatives built from g. No other gravitational field appears in it, and no explicit curvature term. This is minimal coupling. Its consequence is universality: every form of matter and energy couples to the same field g, through its stress-energy tensor, with the same strength.

A small test body in free fall then follows a geodesic of g, the straightest worldline available,

```text
d²x^μ/ds² + Γ^μ_νρ (dx^ν/ds)(dx^ρ/ds) = 0
```

with s the proper time along the path. No force term appears and the body's composition does not enter: in general relativity gravity is not a force, and an accelerometer carried by a freely falling body reads zero.

## The equivalence principle and Rindler frames [T]

The equivalence principle says that within a small enough region of spacetime the effects of gravity cannot be told apart from those of acceleration. It has a weak form, the universality of free fall (a test body's trajectory depends only on where it starts and how fast it moves, not on what it is made of), and Einstein's form, that in a freely falling frame local physics is the physics of special relativity.

Two kinds of frame make it concrete:

- **Free fall.** A freely falling frame, such as an orbiting spacecraft, is locally inertial. Nothing in it feels a gravitational force.
- **Rindler frames.** A frame accelerating uniformly through flat spacetime, a Rindler frame, is locally equivalent to a frame at rest in a uniform gravitational field: objects released in it fall together, with a common acceleration.

The program's conjugate special relativity reads these two frames as the rest state and the uniform motion of the momentum [polarization](/wiki/phase-space/reciprocity/lagrangian-polarizations); see [below](#how-the-program-uses-general-relativity).

## Linearized gravity and the graviton [T]

Far from strong sources the metric is close to flat:

```text
g_μν = η_μν + h_μν,        |h_μν| ≪ 1
```

Here η_μν is the Minkowski metric, the textbook symbol, which is unrelated to the program's neutral metric η on phase space ([the structures ω, η, H](/wiki/phase-space/born-geometry/born-structures)). The perturbation h_μν is a symmetric tensor field on flat spacetime. Calc note [#5](/wiki/history/documents/debt-1-notes) §D counts its components when it lists [the field content of the program's broken vacuum](/wiki/phase-space/modular-field/field-content): "h_μν (10, graviton)".

**Linearized diffeomorphisms.** An infinitesimal change of coordinates generated by a vector field ξ^μ(x) changes h_μν, to first order, by

```text
δh_μν = ∂_μ ξ_ν + ∂_ν ξ_μ
```

Since a change of coordinates does not change the physics, two perturbations that differ by such a transformation describe the same geometry. The transformation is therefore a gauge symmetry, the linear form of diffeomorphism invariance, in the way A_μ → A_μ + ∂_μα is the gauge symmetry of electromagnetism. The program's documents write the same symmetrized derivative as ∂₍μλ_ν₎ for the shifts of X.

**The kinetic term.** Expanding the Einstein–Hilbert action to second order in h gives a Lagrangian that is quadratic in h and has two derivatives. Up to normalization and total derivatives it is the only such Lagrangian invariant under δh_μν = ∂_μξ_ν + ∂_νξ_μ; it is often called the massless Fierz–Pauli Lagrangian.

**What propagates.** The gauge symmetry, and the constraints that come with it, remove most of the ten components. In a suitable gauge the vacuum field equations become wave equations, □h_μν = 0, so a disturbance of the metric travels at the speed of light. The components that survive are transverse to the direction of travel and traceless, and under rotations about that direction they carry helicity ±2. The field is massless and has spin 2, and its quanta are gravitons. A passing gravitational wave stretches distances along one transverse direction while squeezing them along another, alternately.

**Why the gauge symmetry is needed.** In Lorentzian signature, raising a time index changes a sign, so the mixed components h₀ᵢ enter a contraction such as h_μν h^μν, and the kinetic term built from it, with the opposite sign to h₀₀ and hᵢⱼ. If all ten components propagated, the mixed ones would carry negative kinetic energy. The gauge-invariant Lagrangian contains no time derivatives of h₀₀ and h₀ᵢ, which are constrained rather than propagated. Calc note [#6](/wiki/history/documents/debt-1-notes) §2 states the general fact as the signature obstruction [T — standard], on [the Fierz–Pauli page](/wiki/gravity/spin-2-fields/fierz-pauli).

## One massless graviton is general relativity [T]

The linear theory is incomplete once matter is present. Its source is the stress-energy tensor, and the gravitational field itself carries energy, so a massless spin-2 field coupled consistently to all stress-energy must also couple to itself. Completing the theory order by order, with the gauge symmetry kept at every order, rebuilds general relativity, up to terms with more derivatives (Gupta 1954†; Weinberg 1965†; Deser 1970†). Along the way the linear gauge symmetry becomes full diffeomorphism invariance, and the field's coupling to matter is forced to be universal, which is the equivalence principle (Weinberg 1964†).

This uniqueness holds for one massless spin-2 field. For several, the [multi-graviton no-go theorem](/wiki/gravity/spin-2-fields/multi-graviton-no-go) shows that no consistent interaction can mix them.

## The graviton's mass [T]

General relativity's graviton is exactly massless. The predictions table of the [checkpoint](/wiki/history/documents/checkpoint) gives "m_g = 0" as the standard expectation for gravitational waves (#11 §13, row 6). A graviton mass would make gravitational waves disperse, low frequencies travelling more slowly than light, and would change the phase of the signals from merging compact binaries; observations of those signals bound it. Calc note #7 §4 places the bound from gravitational-wave observations in the "m_g ≲ 10⁻²³ eV territory". The program's prediction that one of its two spin-2 eigenstates is exactly massless is tested against such bounds on [row 6](/wiki/predictions/massless-graviton).

## How the program uses general relativity

**Ordinary matter.** In the [lab notebook](/wiki/history/documents/lab-notebook)'s v0.1 action, ordinary matter was left alone: "S_x is the Standard Model minimally coupled to g. Nothing is modified. [P4]" (#1 §3). Its consistency section reads, for general relativity (GR) and the Standard Model (SM): "GR and the SM. Exact at tree level in the x-sector by construction (P4, P5). [D]" (#1 §4). In the same action the g-block of the phase-space metric H "reproduces the Einstein–Hilbert action with M_P fixed by M_B and the section volume" [D, schematic] (#1 §3). That action is superseded as reference ([the geometric action S_H and the v0.1 action](/wiki/gravity/tuning-test/geometric-action)). In the current picture ordinary matter still couples to g, and therefore feels both of the program's spin-2 eigenstates: the massless graviton at long range, and X at gravitational strength within its range 1/M_X. The checkpoint states it as "SM couplings gravitational-strength and Yukawa-cut at 1/M_X" [D] (#11 §7.5), and calc note #8 §3 as "safety is by **range**, not decoupling" ([safety by range](/wiki/gravity/momentum-graviton/fifth-force-safety)).

**Universal coupling.** In the current postulate [P4](/wiki/program/postulates/p4-polarized-matter), x-polarized matter (the Standard Model) and p-polarized matter (χ, [conjugate matter](/wiki/dark-matter/conjugate-matter)) "both couple universally to H" [P] (#11 §4). The notebook's version of P4 adds "the equivalence principle holds across polarizations" (#1 §1). [Conjugate special relativity](/wiki/conjugate-relativity) (#13 §6) lists what the two polarizations share: "the time coordinate (in the 3+1 presentation used here) and the massless graviton, so both polarizations fall identically."

**The metric inside the modular field.** In the [modular field](/wiki/phase-space/modular-field/modular-field-z) Z = X + iY, the program identifies Im Z = g, the spacetime metric, and the slice X = 0 as the vacuum [D] (#11 §6).

**General relativity as Branch R.** With both phase-space structures ω and η held rigid (the [original P2](/wiki/program/postulates/original-p2)), the program has no content of its own: calc note #5 §B calls this Branch R and finds that it "reduces to GR + one bespoke SIDM model", that is, general relativity plus one model of [self-interacting dark matter](/wiki/dark-matter/halo-astrophysics/self-interacting-dark-matter) (SIDM). This is the [nontriviality theorem](/wiki/program/postulates/nontriviality-theorem) [D] (#11 §4, §5), which forced the change to [P2′](/wiki/program/postulates/p2-prime).

**The template for X.** The program's second symmetric tensor, X = Re Z, has local shifts δX_μν = ∂₍μλ_ν₎, which form "a second copy of linearized diffeomorphisms" because X is symmetric (#6 §2; #11 §7.1, [D + T]). That makes X a second graviton-like gauge field ([dual diffeomorphisms](/wiki/gravity/momentum-graviton/dual-diffeomorphisms)). Since a second interacting massless graviton is excluded, and so is a symmetric tensor without gauge symmetry, X must be massive ([why X must be massive](/wiki/gravity/momentum-graviton/forcing-chain)).

**Which graviton is massless.** In the program's bimetric sector ([Hassan–Rosen bimetric gravity](/wiki/gravity/spin-2-fields/hassan-rosen-bimetric)) the massless graviton is the combination (e + f) of the two frames, which is even under [Born reciprocity](/wiki/phase-space/reciprocity/born-reciprocity), and X is the odd combination (e − f) (#8 §3, [D + T]; #11 §7.5, [D]). Calc note #8 §3 adds that graviton-mass bounds from gravitational waves "apply to the even eigenstate, which is exactly massless"; #11 §7.5 calls them "satisfied identically". The kill condition of row 6 is a "Nonzero mass attributed to the even eigenstate" (#11 §13). See [spectrum, parameters and reciprocity parity](/wiki/gravity/momentum-graviton/spectrum-and-parity).

**Flat momentum space.** General relativity curves spacetime and leaves momentum space flat. The checkpoint counts "general relativity's flat momentum fibers" among the sources of the asymmetry between position and momentum and calls them "an architectural assumption, not a measurement, and false in the one exactly solved quantum gravity (2+1d, where momenta live on a curved group manifold [5†])" (#11 §3). See [Born's question](/wiki/program/borns-question) and [curved momentum space](/wiki/phase-space/reciprocity/curved-momentum-space).

**Free fall as rest.** #13 §5 reads the two frames of the equivalence principle as the inertial states of the momentum polarization: "The dual-inertial class consists of trajectories with dp/dt constant: rest (dp/dt = 0, i.e., force-free motion — our free fall) and uniform dual motion (constant force — our Rindler frames)." It then records [D — structural]: "the dual principle of relativity — equivalence of all force-free frames — is the equivalence principle". See [dual inertia](/wiki/conjugate-relativity/dual-inertia) and [the equivalence principle as dual relativity](/wiki/conjugate-relativity/equivalence-principle).

**A chat-only comparison.** The [handoff](/wiki/history/documents/handoff) records, among results that exist only in the original chat, a comparison of the program's field equations with Einstein's: "slaved layer g̃ = g⁻¹ is algebraic (Einstein's equation does double duty)" (HANDOFF §4). No document derives it, and its status is conjecture ([two gravitational charges and the conjugate field equations](/wiki/gravity/momentum-graviton/chat-only-results)).

## References

The program's documents cite no source for general relativity itself. Added by the wiki from model memory (†):

- A. Einstein (1915)†; D. Hilbert (1915)†: the field equations and the action.
- S. N. Gupta (1954)†; S. Weinberg (1964, 1965)†; S. Deser (1970)†: a massless spin-2 field coupled consistently to matter and to itself is general relativity, and its coupling to matter is universal.
- W. Rindler (1966)†: the uniformly accelerated frame.
- C. W. Misner, K. S. Thorne, J. A. Wheeler, *Gravitation* (1973)†; R. M. Wald, *General Relativity* (1984)†; S. M. Carroll, *Spacetime and Geometry* (2004)†: textbooks.

## Used by

- [Dual diffeomorphisms: a second graviton](/wiki/gravity/momentum-graviton/dual-diffeomorphisms) — X's local shifts copy the graviton's gauge symmetry.
- [Why X must be massive](/wiki/gravity/momentum-graviton/forcing-chain) — the graviton's gauge symmetry, doubled, is what excludes a massless X.
- [The gravitational Higgs mechanism](/wiki/gravity/momentum-graviton/gravitational-higgs) — a mass breaks the graviton's linearized diffeomorphisms, which the Stückelberg fields restore.
- [Spectrum, parameters and reciprocity parity](/wiki/gravity/momentum-graviton/spectrum-and-parity) — the massless graviton is the reciprocity-even combination.
- [Row 6: the exactly massless graviton](/wiki/predictions/massless-graviton) — the observational test of that statement.
- [Row 9: no linear photon dispersion](/wiki/predictions/photon-dispersion) — general relativity's expectation, no dispersion, is the row's standard.
- [P4: polarized matter and strict sector separation](/wiki/program/postulates/p4-polarized-matter) — both matter sectors couple universally to H.
- [The modular field Z = X + iY](/wiki/phase-space/modular-field/modular-field-z) — Im Z is the spacetime metric.
- [The nontriviality theorem](/wiki/program/postulates/nontriviality-theorem) — with η rigid the program reduces to general relativity plus one dark-matter model.
- [Dual inertia: free fall as rest](/wiki/conjugate-relativity/dual-inertia) and [the equivalence principle as dual relativity](/wiki/conjugate-relativity/equivalence-principle) — #13's reading of free fall and Rindler frames.
- [Momentum-space black holes (chat-only)](/wiki/conjugate-relativity/momentum-space-black-holes) — the event horizon and the force needed to hover near it.
- [Born's question](/wiki/program/borns-question) — general relativity's flat momentum fibers.
- [Born's answer: momentum space gravitates](/wiki/gravity/momentum-graviton/borns-answer) — the program's answer makes general relativity's flat momentum space dynamical.
- [The geometric action S_H and the v0.1 action (superseded)](/wiki/gravity/tuning-test/geometric-action) — the v0.1 action's Einstein–Hilbert g-block.
- [Two gravitational charges and the conjugate field equations (chat-only)](/wiki/gravity/momentum-graviton/chat-only-results) — the chat-only comparison of the program's field equations with Einstein's.

## Sources

- `papers/broken-born-checkpoint-v2.md` §3, §4 (P4), §5, §6, §7.1, §7.5, §13 row 6 — the flat momentum fibers; universal coupling; the nontriviality theorem; Im Z = g; X's dual diffeomorphisms; the even eigenstate, graviton-mass bounds and the short-range coupling of X to ordinary matter; the massless-graviton row.
- `papers/conjugate-special-relativity.md` §5, §6 — free fall and Rindler frames as the dual-inertial frames; the equivalence principle as the dual relativity principle; the massless graviton shared by both polarizations.
- `notes/debt1a-ii-X-classification.md` §2 — the local shifts of X as a second copy of linearized diffeomorphisms.
- `notes/debt1a-iv-beta-coefficients.md` §3 — the reciprocity-even massless graviton; graviton-mass bounds apply to it; safety by range, not decoupling.
- `notes/debt1a-iii-tuning-test.md` §4 — the gravitational-wave bound, "m_g ≲ 10⁻²³ eV territory".
- `notes/debt1a-geometric-core.md` §B, §D — Branch R as general relativity plus one dark-matter model; the ten components of h_μν.
- `notes/broken-born-theory.md` §1, §3, §4 — P4 with the equivalence principle across polarizations; the v0.1 action, Einstein–Hilbert from the g-block, the Standard Model minimally coupled; general relativity and the Standard Model exact at tree level (superseded as reference).
- `HANDOFF.md` §4 — the chat-only comparison with Einstein's equation.
