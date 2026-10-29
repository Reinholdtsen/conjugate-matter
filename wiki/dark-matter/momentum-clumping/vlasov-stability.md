---
title: "Vlasov stability and Landau damping"
weight: 20
status: established
description: "Collisionless kinetic theory: the Vlasov equation, linear response about a Maxwellian, Landau damping, the Jeans instability and the Boltzmann H-theorem."
provenance: [T]
sources:
  - "notes/stream-stability.md 'Setup'"
  - "notes/stream-stability.md 'Limit 1 (broad gate)'"
  - "notes/stream-stability.md 'Numbers at the scattering benchmark'"
  - "notes/broken-born-theory.md §5.2"
---

*The Vlasov equation describes a gas whose particles interact only through a smooth, averaged force field, so that the gas is fully specified by how densely it fills each region of position and velocity. Its stability theory asks whether a small ripple in that density grows or dies away. In a plasma a ripple usually decays even without collisions (Landau damping), while in a self-gravitating gas a ripple longer than a critical length grows into a lump (the Jeans instability). Where collisions do act, they drive any distribution toward the smooth thermal shape (Boltzmann's H-theorem). The program used this textbook machinery in [the clumping problem](/wiki/history/main-problems) to test whether dark matter could [clump in velocity](/wiki/dark-matter/momentum-clumping/founding-image).*

**Status:** Established physics [T], summarized here from general knowledge; the references below are added by the wiki from model memory (†). The program's use of it is in `notes/stream-stability.md`, which names the method but does not print its steps.

## The Vlasov equation

A gas of many identical particles of mass m can be described by a distribution function f(x, p, t), the number of particles per unit volume of phase space, the six-dimensional space of positions and momenta. Integrating over momentum gives the ordinary number density, n(x, t) = ∫d³p f [T].

When each particle feels a force made up of small contributions from very many others, that force is well approximated by the average field of the whole gas, and close encounters between pairs can be neglected over the times of interest. Each particle then moves under a single-particle energy ε(x, p), which includes this mean field, by Hamilton's equations ẋ = ∇ₚε and ṗ = −∇ₓε. The phase-space density is carried unchanged along these trajectories, which gives the Vlasov equation, also called the collisionless Boltzmann equation [T]:

```text
∂f/∂t + ∇ₚε · ∇ₓf − ∇ₓε · ∇ₚf = 0
```

For a gas held together by its own gravity, ε = p²/2m + mΦ(x), with Φ fixed by Poisson's equation ∇²Φ = 4πGρ, and the equation takes its familiar stellar-dynamics form ∂f/∂t + v·∇ₓf − m∇ₓΦ·∇ₚf = 0 [T]. The equation is nonlinear, because the mean field inside ε is itself computed from f.

In the usual cases, gravity and electrostatics, the mean field depends only on position, so ∇ₚε = p/m is the ordinary velocity. The clumping problem works in the "Nonrelativistic mean-field (Vlasov) limit of the gated interaction" (`notes/stream-stability.md`, Setup), where the mean field also depends on momentum: a particle is attracted only by neighbours moving at nearly its own velocity. Then ∇ₚε contains an extra term, the "anomalous velocity" of the [lab notebook](/wiki/history/documents/lab-notebook) (`notes/broken-born-theory.md` §5.2). That model is on [the gated Vlasov model](/wiki/dark-matter/momentum-clumping/gated-vlasov-model) page.

## Linear response about a homogeneous equilibrium

When the mean field is uniform in space, any distribution f₀(p) that depends on momentum alone is a stationary solution. Stability theory perturbs it, f = f₀ + δf, keeps terms of first order in the perturbation, and decomposes the perturbation into plane waves e^{i(k·x − ωt)}, with k a wavevector and ω a frequency [T]. This is a Fourier analysis in space and time: each plane wave evolves independently at linear order, so it is enough to ask, wave by wave, whether ω has a positive imaginary part (growth) or a negative one (decay).

For each plane wave the linearized Vlasov equation gives the response of the distribution to a change δε in the single-particle energy [T]:

```text
δf(p) = − (k·∇ₚf₀) δε(p) / (ω − k·v)
```

The loop then closes. The perturbation δf changes the mean field, which changes δε, which acts back on the particles. A self-sustaining mode exists at (k, ω) when the loop reproduces the δε it started from.

When the pair interaction does not depend on momentum, as for gravity, the Coulomb force or a plain contact force, δε is the same for every particle at a given point: δε = Ũ(k) δn, where Ũ(k) is the [Fourier transform](/wiki/phase-space/reciprocity/fourier-transform) of the pair interaction energy and δn = ∫d³p δf. The loop then reduces to one scalar condition, the dispersion relation [T]:

```text
1 + Ũ(k) ∫d³p (k·∇ₚf₀)/(ω − k·v) = 0
```

For a Maxwellian f₀ the integral is written with the plasma dispersion function of Fried and Conte (1961)†, a tabulated function of the wave's phase velocity ω/k measured in units of the thermal speed [T]. [Calc note #2](/wiki/history/documents/clumping-notes) reaches its broad-gate threshold by what it calls "standard plasma-function algebra" (#2, Limit 1) and does not show the steps.

The integral has a singularity where ω = k·v, at the particles that move with the wave's phase velocity. These resonant particles are where Landau damping comes from.

## Landau damping

Landau (1946)† solved the linear problem as an initial-value problem: start a perturbation at t = 0 and follow it forward. The long-time response is then governed by the solutions of the dispersion relation with the velocity integral continued analytically from Im ω > 0 into Im ω < 0 [T]. When every such solution has Im ω < 0, the density and the field of the perturbation decay, although no particle ever collides with another. This is Landau damping [T].

Two complementary pictures describe it [T]:

- **Phase mixing.** The perturbation of f is a superposition of free-streaming components, each moving with its own velocity v. The density is an integral over v, and as the components move apart in phase, their sum decays, much as a chord of many slightly detuned oscillators fades although each oscillator keeps ringing. The fine structure is not lost; it moves to ever finer scales in velocity.
- **Resonant exchange.** Particles slightly slower than the wave take energy from it, and particles slightly faster give energy to it. Where the distribution falls with speed at the phase velocity, as it does everywhere for a Maxwellian, the slower particles are the more numerous, and the wave loses energy.

The clumping problem's verdict below its threshold is this case: "Below threshold: Landau-damped, stable." (#2, Limit 1).

## The static threshold and the Jeans instability

For an attractive interaction acting on a Maxwellian gas, an instability first appears through a non-oscillating mode, ω = 0, so the threshold can be found from the static limit of the dispersion relation [T]. For a Maxwellian with one-dimensional [velocity dispersion](/wiki/dark-matter/halo-astrophysics/velocity-dispersion#the-maxwellian-and-the-dynamical-temperature) σ, f₀ ∝ exp(−v²/2σ²), one has k·∇ₚf₀ = −(k·v) f₀/(mσ²), and at ω = 0 the integral equals n/(mσ²) [T]. The threshold is then

```text
−Ũ(k) n = mσ²
```

The interaction must be attractive (Ũ < 0), and the attraction energy per particle, |Ũ| n, must reach the kinetic-energy scale of the random motion, mσ². A repulsive interaction, as in an electron plasma, gives no static instability [T].

**Gravity.** For self-gravity Ũ(k) = −4πGm²/k², and the threshold becomes k² = 4πGρ/σ² with ρ = mn. Perturbations with wavenumber below the Jeans wavenumber k_J = √(4πGρ)/σ, that is with wavelength above the Jeans length 2π/k_J, grow: on those scales self-gravity outweighs the restoring effect of the velocity dispersion. This is the Jeans instability, Jeans (1902)†, which seeds lumps in space [T].

**A contact attraction.** For a contact attraction of strength g that acts equally on all momenta, Ũ = −g at every k, and the threshold reads g n = mσ². This is the form of the broad-gate threshold in the clumping problem, g n/(mσ²) ≥ 1 (#2, Limit 1; [the mean-field criterion](/wiki/dark-matter/momentum-clumping/instability-criterion)). The derivation in this section, from the static limit to this form, is the wiki's textbook reading of "standard plasma-function algebra" [T]; the note states only the result.

The lab notebook framed velocity clumping as "the Jeans problem with the roles of x and v exchanged" (`notes/broken-born-theory.md` §5.2). In the ordinary Jeans problem the attraction depends on the particles' separation in position, and the instability makes lumps in position. In the exchanged problem the attraction acts between particles that are close in velocity, through the [velocity gate](/wiki/dark-matter/conjugate-matter/velocity-gate), and the notebook expected lumps in velocity: streams. The clumping problem computed the threshold for that exchanged problem and found it far out of reach ([the founding image](/wiki/dark-matter/momentum-clumping/founding-image)).

## Collisions and the H-theorem

Collisions add a term C[f] to the right-hand side of the Vlasov equation, which makes it the Boltzmann equation. Boltzmann (1872)† showed that the functional H = ∫d³x d³p f ln f never increases under the collision term, and that it stops changing only when ln f is a combination of the quantities each collision conserves: particle number, momentum and kinetic energy. For a uniform gas that is the Maxwellian [T]. Since the entropy is proportional to −H, collisions never decrease it, and the state they drive the gas to is the distribution of maximum entropy for the conserved totals, the Maxwellian.

The proof uses only those conservation laws and the symmetry of the scattering rate under exchange of initial and final states. It does not depend on how the cross-section varies with velocity [T]. A velocity-dependent cross-section changes how fast a gas relaxes, not the state it relaxes to.

The clumping problem applies this to the gated collisions: "The H-theorem closes the collisional back door: gated collisions still maximize entropy; equilibrium is Maxwellian to one part in 10³⁰" (`notes/stream-stability.md`, 'Numbers at the scattering benchmark'). The note states this in one sentence and does not derive it.

## Notation

In the clumping problem, ω and k are a frequency and a wavevector. They are not the [symplectic form](/wiki/phase-space/reciprocity/symplectic-form) ω of the phase-space pages, and k is not the gate variable of [the scattering law](/wiki/dark-matter/conjugate-matter/scattering-law), the incoming relative momentum. G denotes the gate in the clumping notes, not Newton's constant, except where gravity is meant ([notation](/wiki/notation)).

## References

Added by the wiki from model memory (†); the program's documents cite none of them for the general theory.

- A. A. Vlasov (1938)†: the collisionless kinetic equation for a plasma.
- L. D. Landau (1946)†: the initial-value treatment and collisionless damping.
- J. H. Jeans (1902)†: the gravitational instability of a uniform medium.
- L. Boltzmann (1872)†: the kinetic equation with collisions and the H-theorem.
- B. D. Fried and S. D. Conte, *The Plasma Dispersion Function* (1961)†.
- J. Binney and S. Tremaine, *Galactic Dynamics*†: the collisionless Boltzmann equation, phase mixing and the Jeans instability for stellar systems.

## Used by

- [The gated Vlasov model](/wiki/dark-matter/momentum-clumping/gated-vlasov-model) — the mean-field setup of the clumping calculation, with a mean field that depends on momentum.
- [The mean-field criterion and its 10²⁸–10³¹ shortfall](/wiki/dark-matter/momentum-clumping/instability-criterion) — the stream threshold, Landau damping below it, and the H-theorem closure of the collisional route.
- [The classicality theorem](/wiki/dark-matter/momentum-clumping/classicality-theorem) — the corollary of that threshold.
- [Obituary: velocity clumping, the founding image](/wiki/dark-matter/momentum-clumping/founding-image) — "the Jeans problem with the roles of x and v exchanged".

## Sources

- `notes/stream-stability.md` 'Setup' — the Vlasov limit and the linearization the clumping problem performs
- `notes/stream-stability.md` 'Limit 1 — broad gate' — Landau damping below threshold; the plasma-function algebra
- `notes/stream-stability.md` 'Numbers at the scattering benchmark' — the H-theorem statement
- `notes/broken-born-theory.md` §5.2 — the Jeans framing of velocity clumping and the anomalous velocity
