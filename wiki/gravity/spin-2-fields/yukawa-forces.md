---
title: "Yukawa forces and their range"
weight: 18
status: established
description: "The force carried by a field of mass M: the potential e^(−Mr)/(4πr) and its range ℏ/(Mc), the same law in momentum as 1/(q² + M²), the fifth-force form V = −(Gm₁m₂/r)(1 + α e^(−r/λ)), scattering through a Yukawa mediator in the contact and light-mediator limits, and the program's uses, from X's range 1/M_X to the gated amplitude; distinct from the Yukawa coupling."
provenance: [T]
sources:
  - "papers/broken-born-checkpoint-v2.md §7.5"
  - "papers/broken-born-checkpoint-v2.md §7.1"
  - "papers/broken-born-checkpoint-v2.md §8"
  - "papers/broken-born-checkpoint-v2.md §13 rows 1–2"
  - "papers/broken-born-checkpoint-v2.md §14 item 11"
  - "papers/reciprocity-toy-models.md Abstract"
  - "papers/reciprocity-toy-models.md §5"
  - "review/round4/referee/audit-notes.md Step 2(d)"
  - "papers/conjugate-special-relativity.md §1"
  - "papers/conjugate-special-relativity.md §6"
  - "HANDOFF.md §4"
  - "notes/debt1a-iv-beta-coefficients.md §3"
  - "notes/debt1a-ii-X-classification.md §4"
  - "notes/broken-born-theory.md §3"
  - "notes/broken-born-theory.md §4"
  - "notes/broken-born-theory.md §5.1"
  - "notes/broken-born-theory.md §9"
  - "notes/debt3a-stream-stability.md 'Setup'"
  - "notes/toy-lagrangian.md 'Success criteria (fixed 2026-10-19, before any construction)'"
  - "notes/toy-lagrangian.md 'Chunk 4 (in progress, 2026-10-19): S5'"
  - "review/round3/referee/audit-notes.md Step 1"
  - "review/round3/referee/audit-notes.md Step 2"
  - "review/wiki-build-flags.md items 5, 29"
  - "review/wiki-build-checks/audit/flag5_mass_scaling.out part D"
  - "review/wiki-build-checks/audit/c_yukawa_scaling.out"
  - "review/wiki-build-checks/audit/flag17_recompute.out part 3"
---

*A Yukawa force is the force carried by a field whose quanta have a mass M. Between two sources its potential falls as e^(−Mr)/r: at short distances it is the inverse-square force of a massless field, but beyond a distance of about ℏ/(Mc), the mediator's reduced Compton wavelength, it dies away exponentially, so the mass of the mediator sets the range of the force. In momentum the same law is the factor 1/(q² + M²), and that is the form in which such a force enters scattering. The program uses it in several places. Its [momentum graviton X](/wiki/gravity/momentum-graviton) is massive, so the force X exerts on ordinary matter is "Yukawa-cut at 1/M_X", which the program gives as the reason experiments see no sign of it ([safety by range](/wiki/gravity/momentum-graviton/fifth-force-safety)). The standard [self-interacting dark-matter](/wiki/dark-matter/halo-astrophysics/self-interacting-dark-matter) models that the program's scattering predictions are measured against scatter through a light Yukawa mediator, and the program's own amplitude for conjugate matter keeps the Yukawa factor in the momentum transfer and multiplies it by a [velocity gate](/wiki/dark-matter/conjugate-matter/velocity-gate). [Conjugate special relativity](/wiki/conjugate-relativity) reads X's short range as a range in momentum, which the checkpoint it cites does not state. The physics is textbook. The same name also covers a different object, the Yukawa coupling that gives particles their masses, which the program's toy models use as an analogy.*

**Status:** Established — [T] — textbook physics written here from general knowledge; the program's documents cite no source for it, and the literature named below is from model memory (†). The program's uses carry their own tags: "Yukawa-cut at 1/M_X" is [D + T] in [calc note #8](/wiki/history/documents/debt-1-notes) §3 and [D] in [checkpoint #11](/wiki/history/documents/checkpoint) §7.5; the gated amplitude is [D — mechanism; shape [O]] (#11 §8); [#13](/wiki/conjugate-relativity)'s range in momentum is tagged [D — checkpoint §7] there and is flag 29 in `review/wiki-build-flags.md`. No `verify/` script checks the physics on this page. Scripts written for the flags' audit, which are not part of the gate, check the relation between range and mass numerically and evaluate the Born cross-section in closed form (`review/wiki-build-checks/audit/flag5_mass_scaling.out` part D; `review/wiki-build-checks/audit/flag17_recompute.out` part 3).

## The potential of a massive mediator [T]

### The field of a point source

A static field φ produced by a point source obeys, in units where ℏ = c = 1,

```text
(∇² − M²) φ = −Q δ³(r)
```

where M is the mass of the field's quanta, Q is the source's charge under the field (its electric charge for electromagnetism; for gravity, a constant times its mass) and δ³(r) places the source at the origin. For M = 0 this is Poisson's equation, and the solution is the Coulomb profile Q/(4πr) of electrostatics and Newtonian gravity. For M > 0 the solution is the Yukawa profile:

```text
φ(r) = Q e^(−Mr) / (4πr)
```

The mass term in the field equation is what turns 1/r into e^(−Mr)/r. A second source of charge Q₂ at distance r has the potential energy

```text
V(r) = − Q₁Q₂ e^(−Mr) / (4πr)        field of spin 0 or 2: like charges attract
V(r) = + Q₁Q₂ e^(−Mr) / (4πr)        field of spin 1: like charges repel
```

and the force between them has the magnitude

```text
|F(r)| = |Q₁Q₂| (1 + Mr) e^(−Mr) / (4πr²)
```

### The range

At distances short compared with 1/M, e^(−Mr) is close to 1 and the force is an inverse-square force, indistinguishable from that of a massless field. At distances long compared with 1/M it is exponentially small, falling by nearly the same factor over each further distance 1/M. That distance is the range of the force. In ordinary units it is ℏ/(Mc), the reduced Compton wavelength of the mediator, so a heavier mediator gives a shorter range [T]. A standard heuristic gives the same scale: an exchanged quantum of mass M carries an energy Mc² that the static sources do not supply, so by the energy–time uncertainty relation it lasts for a time of about ℏ/(Mc²), in which it travels at most about ℏ/(Mc) [T].

Yukawa introduced the form for the force between nucleons, proposing that it is carried by a massive particle whose mass sets the short range of nuclear forces (Yukawa 1935 †); that particle is the pion [T]. The weak force is short-ranged for the same reason, being carried by the massive W and Z bosons [T]. The same form also describes screening: in a plasma or an electrolyte, the mobile charges around a test charge cancel its field at large distances, and the screened potential is a Yukawa potential whose range is the Debye length (Debye and Hückel 1923 †) [T].

### Attraction or repulsion

The sign depends on the spin of the field [T]. Exchange of a field of even spin, 0 or 2, attracts like charges; exchange of a field of spin 1 repels them, as electromagnetism does. A spin-2 field couples to energy and momentum, and every body's energy has the same sign, so the force it carries attracts all bodies to one another, as gravity does (Zee 2003 †).

## The same law in momentum [T]

The Yukawa profile and the factor 1/(q² + M²) are a Fourier pair:

```text
∫ d³r e^(−iq·r) · e^(−Mr)/(4πr) = 1/(q² + M²)
```

Here q is a wavevector, which in a scattering process is the momentum transfer. The two sides are a waveform and its spectrum ([the Fourier transform](/wiki/phase-space/reciprocity/fourier-transform)). The spectrum is nearly flat for q ≪ M and falls as 1/q² for q ≫ M: a short range in position is a broad spectrum in q, and a long range is a spectrum concentrated near q = 0. Two limits bracket the form:

- **The massless limit**, M → 0. The factor becomes 1/q², the transform of the Coulomb profile 1/(4πr), and the spectrum is concentrated at small q, the wavevectors of long distances.
- **The contact limit**, M large compared with every q of interest. The factor is close to the constant 1/M², the transform of a point interaction δ³(r)/M². Exchange of a heavy field then acts as a contact interaction, with a strength proportional to the square of the coupling divided by M². Replacing the heavy field by that contact term is called integrating it out ([integrating out a heavy carrier](/wiki/dark-matter/conjugate-matter/gate-mechanism#integrating-out-a-heavy-carrier)).

In field theory, 1/(q² + M²) is the field's propagator in the static case, in which the exchanged quantum carries momentum but no energy [T]. It is the form in which a Yukawa force enters the amplitudes below.

The scripts of the flags' audit check the relation between mass and range by evaluating the Fourier integral numerically rather than from the closed form. For the factor 1/(q² + c), where c stands in the place of M² (the script writes it k and calls it the quadratic coefficient), the fitted ranges are 1.0, 0.5 and 0.25 at c = 1, 4 and 16: "quadrupling the quadratic coefficient k halves the Yukawa range: the mass is sqrt(k)" (`review/wiki-build-checks/audit/flag5_mass_scaling.out` part D). The range is the inverse of the mass, not of its square, which is the point the audit needed for [flag 5](#the-momentum-graviton-x).

## Fifth forces: a Yukawa term beside gravity [T]

Searches for new forces between ordinary bodies describe a possible extra force by adding a Yukawa term to Newton's potential:

```text
V(r) = −(G m₁ m₂ / r) · (1 + α e^(−r/λ))
```

α is the strength of the extra force relative to gravity, positive for an extra attraction and negative for a repulsion, and λ = ℏ/(Mc) is its range. A force of "gravitational strength" has α of order one. This is the Yukawa potential of the previous sections with charges proportional to the masses of the two bodies, added to Newton's. The letters follow the experimental literature: λ here is not [the Born length](/wiki/phase-space/reciprocity/born-length) of conjugate relativity, and α is not a coupling of the program.

### How experiments test it

Two kinds of experiment look for such a term [T]:

- **Tests of the inverse-square law** measure the force between bodies as a function of their separation: torsion balances in the laboratory at short separations, the orbits of the Moon and the planets at long ones.
- **Tests of the universality of free fall** compare the accelerations of bodies of different composition. A field whose charge is not proportional to mass, for example one coupled to baryon number, makes the acceleration depend on what a body is made of. A field coupled alike to all energy, as a spin-2 field coupled to the stress-energy is, does not ([the universality of free fall](/wiki/gravity/spin-2-fields/equivalence-principle#the-weak-form-universality-of-free-fall-t)).

Each experiment is most sensitive to ranges comparable with the separations it probes. Where λ is much shorter than the separation of its test bodies, the factor e^(−r/λ) has removed the extra force before it reaches them, and the experiment's limit on α weakens exponentially as λ shrinks. The limits are drawn as an excluded region in the plane of λ and α, and toward short range that region ends: an extra force of gravitational strength is excluded only at ranges longer than about the shortest separations tested (Adelberger, Heckel and Nelson 2003 †; Fischbach and Talmadge 1999 †). The program's documents quote no limit of this kind, and the wiki adds none.

### A massive spin-2 mediator

The exchange of a massive spin-2 field between two slowly moving bodies adds an attractive Yukawa term [T]. Its coefficient is not the one a massless graviton with the same coupling to matter would give. The massive field has five polarizations ([the Fierz–Pauli mass term](/wiki/gravity/spin-2-fields/fierz-pauli)), and its helicity-zero polarization also couples to the trace of the source's stress-energy, which changes the coefficient by a fixed factor that does not approach one as M → 0: the van Dam–Veltman–Zakharov discontinuity (van Dam and Veltman 1970 †; Zakharov 1970 †) [T]. The factor is of order one, so the force is of gravitational strength in either case. The program's documents do not discuss it.

## Scattering through a Yukawa mediator [T]

### The Born amplitude

In the Born approximation, first order in the potential, the amplitude for two particles to scatter is proportional to the Fourier transform of their potential at the momentum transfer q ([what a position-local force depends on](/wiki/dark-matter/conjugate-matter/velocity-gate#background-what-a-position-local-force-depends-on-t)). For a Yukawa force it is therefore proportional to 1/(q² + M²). In the centre-of-mass frame each particle arrives with momentum k and leaves with a momentum of the same size, turned through an angle θ, so the transfer q = 2k sin(θ/2) runs from 0 in a grazing collision to 2k in a head-on rebound. The momentum is k = m_r v, with m_r the reduced mass and v the relative speed; for two particles of equal mass m it is k = mv/2, the [lab notebook](/wiki/history/documents/lab-notebook)'s k = m_χv_rel/2 (#1 §3). The angular distribution is

```text
dσ/dΩ ∝ (m_r Q₁Q₂)² / (q² + M²)²
```

The momentum-transfer cross-section σ_T weights each direction by the fraction of forward momentum the collision removes, 1 − cos θ ([the transfer cross-section σ_T](/wiki/dark-matter/halo-astrophysics/transfer-cross-section)). Written as an integral over the transfer, with 1 − cos θ = q²/(2k²) and dΩ = 2πq dq/k²,

```text
σ_T ∝ ((m_r Q₁Q₂)² / k⁴) · ∫₀^{2k} q³ dq / (q² + M²)²
```

This is the integral that the flag-17 audit evaluated in closed form (`review/wiki-build-checks/audit/flag17_recompute.out` part 3). How it behaves depends on how the largest transfer, 2k, compares with M.

### The contact limit: isotropic and independent of speed

When M is much larger than 2k, every collision samples the flat part of the spectrum. dσ/dΩ is then the same in every direction, so the scattering is isotropic. The integral grows as k⁴/M⁴, which cancels the k⁴ in front, and σ_T ∝ (m_r Q₁Q₂)²/M⁴ does not depend on the speed [T]. The audit's closed form has this limit, printed as "heavy-mediator limit k -> 0 of sigma_T*m_phi^4/A^2: 4*pi", a constant (m_φ there is the mediator's mass, M on this page, and A the numerator of the amplitude).

### The light-mediator limit: forward peaking and the Coulomb logarithm

When M is much smaller than 2k, the amplitude grows as 1/q² toward small q, the Rutherford form of an inverse-square force. Outside a narrow forward cone, where q ≲ M, dσ/dΩ falls as 1/q⁴, that is as 1/sin⁴(θ/2), so most collisions deflect the particles only slightly: the scattering is forward-peaked [T].

In σ_T the integrand falls as 1/q between M and 2k, so equal ratios of q contribute equally, and the integral is close to the logarithm ln(2k/M). With k = m_r v,

```text
σ_T ∝ (Q₁Q₂)² / (m_r² v⁴) · ln(2k/M)
```

which falls as v⁻⁴ multiplied by a logarithm [T]. For a massless mediator the integral diverges at small q: the transfer cross-section of an unscreened inverse-square force is infinite, because distant, grazing encounters are too numerous. In a plasma the divergence is cut off at the Debye length, beyond which charges are screened, and the logarithm that remains is the Coulomb logarithm of plasma physics [T]. For a Yukawa force the mediator's mass supplies the cut-off. This is the law that the program's documents call "power-law + Coulomb log".

### Between the limits, and beyond the Born approximation

With the full factor kept, σ_T is flat at low speed, where 2k is below M, and falls as v⁻⁴ with its logarithm at high speed, where 2k is above M; the turnover lies near the relative speed at which 2k reaches M [T]. Self-interaction through a light Yukawa mediator, falling with speed, was proposed as a way to make cores in dwarf galaxies while keeping scattering weak at the higher speeds in galaxy clusters (Loeb and Weiner 2011 †).

The Born approximation assumes that the potential is weak. For an attractive Yukawa force it needs, roughly, the coupling times the ratio of the particle's mass to the mediator's mass to be small [T]. Beyond it, an attractive force can hold quasi-bound states, and σ_T(v) shows resonances; and when the range is long compared with the particles' de Broglie wavelength and the force is strong, the scattering becomes classical. In both regimes σ_T(v) departs from the Born forms above (Tulin, Yu and Zurek 2013 †; [the Born regime and beyond](/wiki/dark-matter/halo-astrophysics/self-interacting-dark-matter#the-born-regime-and-beyond)).

## How the program uses it

### The momentum graviton X

X is a massive spin-2 field whose mass M_X is "the polarization-breaking scale" (#11 §7.1; [the gravitational Higgs mechanism](/wiki/gravity/momentum-graviton/gravitational-higgs)). Ordinary matter couples to the metric g, which contains X as well as the massless graviton; with the [equal Planck masses](/wiki/gravity/momentum-graviton/spectrum-and-parity#equal-planck-masses) that reciprocity forces, the two enter with comparable weight, so the force X carries between ordinary bodies is a Yukawa force of gravitational strength. Calc note #8 §3 [D + T] states the consequence, SM being the Standard Model:

> "safety is by **range**, not decoupling: X-mediated forces on the SM are Yukawa-cut at 1/M_X, and gravitational-strength short-range forces are experimentally unconstrained down to far below any plausible M_X."

#11 §7.5 [D] keeps it as "SM couplings gravitational-strength and Yukawa-cut at 1/M_X". In the fifth-force form above, X adds a term with α of order one and range λ = ℏ/(M_X c), and the argument is that experiments exclude such a term only at ranges far longer than that. The argument and its earlier forms are on [safety by range](/wiki/gravity/momentum-graviton/fifth-force-safety). No document gives M_X a value or quotes an experimental limit, so the range cannot be stated as a distance ([no value for M_X](/wiki/gravity/momentum-graviton/spectrum-and-parity#no-value-for-m_x)).

The range also settles what M_X denotes. A Yukawa range 1/M_X makes M_X the mass of X's quanta, not its square. The flags' audit uses this for flag 5, which says that #11 §7.5's "M_X ∝ 2(β₁+β₂)" should be M_X² ∝ 2(β₁+β₂), the form of its source, #8 §3 ([spectrum, parameters and reciprocity parity](/wiki/gravity/momentum-graviton/spectrum-and-parity)). The audit's script fits the decay of the static profile, finds the decay constant equal to M_X, and prints "d ln M_X / d ln(b1+b2) = 0.5" (`review/wiki-build-checks/audit/c_yukawa_scaling.out`). The flag is confirmed by the audit and is a question of notation only (item 5 in `review/wiki-build-flags.md`).

### The standard expectations of rows 1 and 2

[The checkpoint](/wiki/history/documents/checkpoint)'s predictions table sets the program's dark-matter scattering against self-interacting dark matter (SIDM) with a Yukawa mediator, whose behaviour is the light-mediator limit above (#11 §13):

```text
Row 1, σ_T(v) across halo masses:   "CDM none; Yukawa SIDM power-law + Coulomb log"
Row 2, scattering anisotropy:       "Forward-peaked (light mediators)"
```

Cold dark matter, CDM, does not scatter off itself at all. The [lab notebook](/wiki/history/documents/lab-notebook) states the two behaviours, "Yukawa SIDM falls as v⁻⁴ with a Coulomb-log correction" and "light-mediator Yukawa scattering is forward-peaked" (#1 §5.1), and its own table had "Constant (CDM: 0) or power-law v⁻⁴ln tail (Yukawa SIDM)" (#1 §9). It separates the program's law from "*every* x-local mediator model", x-local meaning local in position, by two signatures: the shape of the fall at high speed, "An exponential cliff, not a power-law tail", and "Isotropy inside the gate" (#1 §5.1). In the Born regime a Yukawa cross-section is itself flat at low speed, so the two laws differ in how they fall and in their angular distributions. The notebook places the separation in speed at "v ∼ 150–400 km/s (large spirals, small groups), where the two shapes diverge by orders of magnitude" (#1 §5.1). The exponential cliff has since been weakened to a knee whose tail is open ([the gated scattering law σ_T(v)](/wiki/dark-matter/conjugate-matter/scattering-law)). The tests are [Row 1: the knee in σ_T(v)](/wiki/predictions/self-interaction-knee) and [Row 2: isotropic scattering below the gate](/wiki/predictions/scattering-isotropy); the halo physics is on [self-interacting dark matter](/wiki/dark-matter/halo-astrophysics/self-interacting-dark-matter).

### The gated amplitude

The program's amplitude for the self-scattering of [conjugate matter](/wiki/dark-matter/conjugate-matter) χ keeps the Yukawa factor in the transfer q and multiplies it by a factor in the incoming relative momentum k:

```text
M(k, q) = 4πα̃m_χ / (q² + m_φ²) · F(k²/μ²)        (#11 §8)
```

M(k, q) is the amplitude, not a mass; m_χ is the χ mass, α̃ the coupling, m_φ the mass of the carrier of the transfer, F the gate and μ its width in momentum. #11 does not define α̃, m_φ or F, and the wiki takes them from the lab notebook ([the amplitude](/wiki/dark-matter/conjugate-matter/velocity-gate#the-amplitude)). The first factor is the Born amplitude of a Yukawa force of range 1/m_φ. The gate depends on k, "the variable no x-local mediator produces" (#11 §8). In the lab notebook's v0.1 form the gate is a Gaussian that tends to 1 as μ grows, and "An x-local Yukawa is the limit μ → ∞" (#1 §3).

The lab notebook puts the first factor in the contact limit: its scattering law assumes "a heavy transfer mediator (m_φ ≳ m_χ, contact-like in x)" (#1 §5.1). Two consequences follow from the contact limit described above.

- **Isotropy below the gate.** The first factor is flat in q, and the gate does not depend on the angle, so scattering below the gate is isotropic: "isotropic below the gate versus Yukawa forward-peaking" (#11 §8). The isotropy rests on the heavy-mediator assumption, which #11 does not restate ([the heavy-mediator assumption](/wiki/predictions/scattering-isotropy#the-heavy-mediator-assumption)).
- **The dependence on speed is the gate's.** In the contact limit the Yukawa factor adds no dependence on speed of its own. The flag-17 audit evaluated the transfer cross-section without the gate, with the full Yukawa factor, at the program's benchmark, m_φ = m_χ = 70 MeV and k = m v\*/2 with v\* the gate velocity. Its change relative to the zero-speed value is "2.13628772255849e-7 (negligible: the v-dependence of sigma_T is the gate's alone)" (`review/wiki-build-checks/audit/flag17_recompute.out` part 3; [the scattering benchmark](/wiki/dark-matter/conjugate-matter/benchmark)).

The lab notebook's low-speed cross-section, σ₀ = 16πα̃²m_χ²/m_φ⁴ (#1 §5.1), depends on the coupling and the masses as a contact cross-section does. [Debt 3](/wiki/history/documents/debt-3-notes)'s mean-field model takes the same limit for its coupling g ≡ 4πα̃/m_φ² (a coupling, not the metric), with "the x-range collapsed to contact (range 1/m_φ, microscopic)" (`notes/debt3a-stream-stability.md` 'Setup'; [the gated Vlasov model](/wiki/dark-matter/momentum-clumping/gated-vlasov-model)).

#11 §8 gives the gate's mechanism as X exchange, "delivered by X-exchange between dual-stress bilinears" [D — mechanism; shape [O]]. Calc note #6 §4 takes the contact limit of that exchange, "Integrating out massive X between χ bilinears gives the contact four-χ operator", and the dependence on k then enters through the width μ of a χ quantum in momentum ([the gate mechanism](/wiki/dark-matter/conjugate-matter/gate-mechanism)). No document relates m_φ to X's mass M_X.

### Conjugate special relativity: a range in momentum

#13 §6 names what the breaking of reciprocity makes different between the two polarizations: "the long-range/short-range asymmetry — our null structure is policed by massless gravity, the dual structure's dynamical part by the massive X, so dual-geometric effects are Yukawa-cut in momentum [D — checkpoint §7]". Its plain-language passage says "ours reaches across the universe and theirs is short-ranged" ([the equivalence principle as dual relativity](/wiki/conjugate-relativity/equivalence-principle#what-the-breaking-makes-different)). #13 §1 has X modify "the dual cone only at short range in momentum [D — §7 of the checkpoint]" ([two causal cones](/wiki/conjugate-relativity/two-causal-cones#the-slaved-dual-cone-and-x)).

A Yukawa range is a distance between sources, and the derived statement in #11 §7.5 is a range of that kind, for the forces between ordinary bodies. #11 §7 states no range in momentum. #13's citation of it for one is flag 29 in `review/wiki-build-flags.md`, confirmed by the flags' audit and awaiting Paul's ruling ([conflicts between sources](/wiki/history/documents/source-conflicts)). The reading in momentum appears elsewhere only among the results that exist in the old chat: "dual Newtonian limit = Yukawa in momentum = the gate" (`HANDOFF.md` §4). No document derives a Yukawa form in momentum. The documented counterpart is the gate's mechanism, X exchange, whose shape is open ([two gravitational charges and the conjugate field equations (chat-only)](/wiki/gravity/momentum-graviton/chat-only-results#the-dual-newtonian-limit-and-the-gate); [Open: the gate shape](/wiki/dark-matter/conjugate-matter/gate-shape)).

### The field τ: no coupling, so no Yukawa force

The program's dark-energy field [τ](/wiki/cosmology/dark-energy/tau-quintessence) is "ultralight" (#1 §4). A field still evolving on cosmological time scales must be so light that the range of a force it carried would be at least comparable to the observable universe, so range offers it no protection [T]. The lab notebook's argument concerns the coupling instead: "τ is a (pseudo-)Goldstone: derivatively coupled, no tree-level Yukawa to SM matter, safe from torsion-balance bounds despite being ultralight. [D]" (#1 §4). "Yukawa" there means a coupling of τ's value to matter, whose exchange would produce a Yukawa force of that long range; a field that couples only through its derivatives produces no static force between unpolarized bodies ([fifth-force safety of τ](/wiki/cosmology/dark-energy/tau-fifth-force)). X and τ are the two cases: X couples at gravitational strength over a short range, and τ has a cosmological range but no such coupling.

## A name collision: the Yukawa coupling

"Yukawa coupling" names a different object [T]. In particle physics it is an interaction term that joins a scalar field φ to a fermion field ψ, of the form y φ ψ̄ψ with y a dimensionless constant. Yukawa's theory coupled the meson field to nucleons in this way, and exchange of the meson through that coupling produces his potential, so the two uses share an origin. In the Standard Model the coupling has a second role: once the Higgs field takes its vacuum value, a Yukawa coupling between the Higgs field and a fermion becomes a mass term for the fermion, proportional to y times that value ([masses from a vacuum value](/wiki/symmetry-breaking/goldstone-and-higgs#masses-from-a-vacuum-value)).

The program's toy-model work uses the word in this second sense, as an analogy for the way a choice of vacuum can make the interactions of matter local. The analogy concerns no force and no range:

- The toy-model note's abstract: a coupling built from (H, K) "makes interactions local in one and nonlocal in the other — the analogue of Yukawa-generated masses. A mechanism forcing such a coupling is not given." Its §5: "as fermion masses follow from a Higgs vacuum value once Yukawa couplings are given. Nothing here forces that coupling." ([Locality from an (H, K)-built coupling](/wiki/symmetry-breaking/matter-coupling).)
- The worklog's criterion S5: "This is the analogue of a Yukawa coupling giving masses through a vacuum expectation value" ('Success criteria'); its result: "This works as a Yukawa coupling does" ('Chunk 4') ([success criteria S0–S5](/wiki/symmetry-breaking/toy-models/success-criteria)).
- #11 §14 item 11 keeps open "locality of matter beyond the weak (Yukawa-like) form, which in the toy reduces to P4" [O], P4 being the postulate of [polarized matter and strict sector separation](/wiki/program/postulates/p4-polarized-matter). "Weak" refers to locality that follows once the coupling is chosen; the worklog's strong form is "locality forced, not chosen" ('Chunk 4'). The word does not describe the strength of a force ([Open: forced locality and the P4 lock](/wiki/symmetry-breaking/strong-locality)).
- The round-4 referee: "the Yukawa analogy is heuristic" (`review/round4/referee/audit-notes.md` Step 2(d)).

The loop estimates of kinetic mixing for the retired soliton candidate ([Obituary: superheavy conjugate solitons](/wiki/dark-matter/candidates/soliton-candidate/obituary)) also contain Yukawa couplings in the particle-physics sense: a one-loop factor with "y" and an "O(1) hidden Yukawa" (`review/round3/referee/audit-notes.md` Steps 1 and 2; [Obituary: Planck-suppressed adjoint mixing](/wiki/dark-matter/candidates/soliton-candidate/dimension-five-operator); [kinetic mixing between sectors](/wiki/dark-matter/candidates/soliton-candidate/kinetic-mixing)).

In the wiki, "Yukawa force", "Yukawa potential", "Yukawa-cut", "Yukawa mediator" and "Yukawa SIDM" refer to the force on this page; "Yukawa coupling", "Yukawa-generated masses" and "the weak (Yukawa-like) form" refer to the coupling. τ's "no tree-level Yukawa" names the coupling whose exchange would produce the force.

## References

The program's documents cite no source for Yukawa forces. Added by the wiki from model memory (†):

- H. Yukawa, "On the interaction of elementary particles. I," Proc. Phys.-Math. Soc. Japan (1935)†: the nuclear force carried by a massive quantum, and its potential.
- P. Debye, E. Hückel (1923)†: the screened potential in electrolytes.
- E. G. Adelberger, B. R. Heckel, A. E. Nelson, "Tests of the gravitational inverse-square law," Annu. Rev. Nucl. Part. Sci. (2003)†; E. Fischbach, C. L. Talmadge, *The Search for Non-Newtonian Gravity* (1999)†: the Yukawa parametrization of fifth forces and the experiments that test it.
- H. van Dam, M. Veltman, Nucl. Phys. B (1970)†; V. I. Zakharov, JETP Lett. (1970)†: the discontinuity of massive spin-2 exchange.
- A. Zee, *Quantum Field Theory in a Nutshell* (2003)†: attraction by even-spin exchange and repulsion by spin-1 exchange.
- S. Tulin, H.-B. Yu, K. M. Zurek, "Beyond collisionless dark matter: particle physics dynamics for dark matter halo structure," Phys. Rev. D (2013)†: Yukawa scattering in the Born, resonant and classical regimes.
- A. Loeb, N. Weiner, "Cores in dwarf galaxies from dark matter with a Yukawa potential," Phys. Rev. Lett. (2011)†: velocity-dependent self-interaction through a light mediator.

## Used by

- [Safety by range: X and ordinary matter](/wiki/gravity/momentum-graviton/fifth-force-safety) — X's force on ordinary matter is cut off beyond 1/M_X.
- [The gravitational Higgs mechanism](/wiki/gravity/momentum-graviton/gravitational-higgs) — a massive X has a finite range.
- [Spectrum, parameters and reciprocity parity](/wiki/gravity/momentum-graviton/spectrum-and-parity) — M_X, whose inverse is X's range; flag 5.
- [The X-condensate candidate](/wiki/dark-matter/candidates/x-condensate) and [Open: the dual-stress enhancement (OP5)](/wiki/dark-matter/conjugate-matter/dual-stress-enhancement) — X's couplings to ordinary matter are of gravitational strength and Yukawa-cut.
- [The velocity gate](/wiki/dark-matter/conjugate-matter/velocity-gate) — the amplitude's first factor; a position-local Yukawa force is the limit μ → ∞.
- [The gate mechanism: X exchange over fiber overlap](/wiki/dark-matter/conjugate-matter/gate-mechanism) — the contact limit of X exchange.
- [The gated scattering law σ_T(v)](/wiki/dark-matter/conjugate-matter/scattering-law) — set against the Yukawa v⁻⁴ tail and forward peaking.
- [The scattering benchmark](/wiki/dark-matter/conjugate-matter/benchmark) and [the gated Vlasov model](/wiki/dark-matter/momentum-clumping/gated-vlasov-model) — the heavy mediator, contact-like in position.
- [Row 1: the knee in σ_T(v)](/wiki/predictions/self-interaction-knee) and [Row 2: isotropic scattering below the gate](/wiki/predictions/scattering-isotropy) — measured against Yukawa SIDM.
- [The equivalence principle as dual relativity](/wiki/conjugate-relativity/equivalence-principle) and [two causal cones](/wiki/conjugate-relativity/two-causal-cones) — #13's short range "in momentum".
- [Two gravitational charges and the conjugate field equations (chat-only)](/wiki/gravity/momentum-graviton/chat-only-results) — "Yukawa in momentum".
- [Fifth-force safety of τ](/wiki/cosmology/dark-energy/tau-fifth-force) — no Yukawa coupling, so no long-range Yukawa force.

## Sources

- `papers/broken-born-checkpoint-v2.md` §7.5 — "SM couplings gravitational-strength and Yukawa-cut at 1/M_X" [D]; §7.1 — M_X as the polarization-breaking scale; §8 — the gated amplitude, "the variable no x-local mediator produces", the mechanism [D — mechanism; shape [O]], "isotropic below the gate versus Yukawa forward-peaking"; §13 rows 1–2 — the standard expectations; §14 item 11 — "the weak (Yukawa-like) form" [O]
- `papers/reciprocity-toy-models.md` Abstract, §5 — the analogy with Yukawa-generated masses
- `review/round4/referee/audit-notes.md` Step 2(d) — "the Yukawa analogy is heuristic"
- `papers/conjugate-special-relativity.md` §1, §6 — "short range in momentum", "Yukawa-cut in momentum", the plain-language passage
- `HANDOFF.md` §4 — "dual Newtonian limit = Yukawa in momentum = the gate" (chat-only)
- `notes/debt1a-iv-beta-coefficients.md` §3 — safety by range, X-mediated forces "Yukawa-cut at 1/M_X" [D + T]
- `notes/debt1a-ii-X-classification.md` §4 — integrating out massive X gives the contact operator
- `notes/broken-born-theory.md` §3 — k = m_χv_rel/2; "An x-local Yukawa is the limit μ → ∞"; §4 — τ with "no tree-level Yukawa to SM matter"; §5.1 — the heavy transfer mediator, Yukawa SIDM's v⁻⁴ fall with a Coulomb log, forward peaking, the two signatures, the discriminating band, σ₀; §9 — the v0.1 row 1
- `notes/debt3a-stream-stability.md` 'Setup' — the contact coupling g ≡ 4πα̃/m_φ², range 1/m_φ collapsed to contact
- `notes/toy-lagrangian.md` 'Success criteria (fixed 2026-10-19, before any construction)', 'Chunk 4 (in progress, 2026-10-19): S5' — S5 as the analogue of a Yukawa coupling; the weak and strong forms
- `review/round3/referee/audit-notes.md` Steps 1 and 2 — the Yukawa couplings in the soliton candidate's kinetic-mixing estimates
- `review/wiki-build-flags.md` items 5, 29 — M_X or M_X², confirmed, notation only; #13's range in momentum, confirmed, awaiting Paul's ruling
- `review/wiki-build-checks/audit/flag5_mass_scaling.out` part D; `review/wiki-build-checks/audit/c_yukawa_scaling.out` — the range as the inverse of the mass, checked numerically
- `review/wiki-build-checks/audit/flag17_recompute.out` part 3 — the Born transfer cross-section with the full Yukawa factor: its constant heavy-mediator limit and its negligible change at the benchmark
