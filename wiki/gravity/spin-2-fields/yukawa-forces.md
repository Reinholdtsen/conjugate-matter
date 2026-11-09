---
title: "Yukawa forces and their range"
weight: 18
status: established
description: "The force carried by a field of mass M: the potential e^(−Mr)/(4πr) and its range ℏ/(Mc), the same law in momentum as 1/(q² + M²), the fifth-force form V = −(Gm₁m₂/r)(1 + α e^(−r/λ)) with its torsion-balance limits and the bimetric strength α = (4/3)(M_f u/M_g)², scattering through a Yukawa mediator in the contact and light-mediator limits, and the program's uses, from X's range 1/M_X and its laboratory bound to the gated amplitude; distinct from the Yukawa coupling."
provenance: [T]
sources:
  - "wiki/papers/broken-born-checkpoint-v2.md §7.5"
  - "wiki/papers/broken-born-checkpoint-v2.md §7.1"
  - "wiki/papers/broken-born-checkpoint-v2.md §8"
  - "wiki/papers/broken-born-checkpoint-v2.md §13 rows 1–2"
  - "wiki/papers/broken-born-checkpoint-v2.md §14 item 11"
  - "wiki/papers/reciprocity-toy-models.md Abstract"
  - "wiki/papers/reciprocity-toy-models.md §5"
  - "review/round4/referee/audit-notes.md Step 2(d)"
  - "wiki/papers/phase-space-diameter.md §8.2"
  - "wiki/papers/phase-space-diameter.md §7"
  - "wiki/papers/phase-space-diameter.md 'References'"
  - "verify/phase_space_diameter.py 'Consequences (note §8)'"
  - "review/round5-adjudication.md 'Rulings' R1, R12"
  - "review/round5/adjudicator/arb.out B9"
  - "review/round5/referee-A/scripts/lee_interp.py"
  - "review/round5/referee-A/audit-notes.md §4.5"
  - "review/round5/referee-B/audit-notes.md §4.5"
  - "wiki/papers/conjugate-special-relativity.md §1"
  - "wiki/papers/conjugate-special-relativity.md §6"
  - "HANDOFF.md §4"
  - "notes/beta-coefficients.md §3"
  - "notes/x-classification.md §4"
  - "notes/broken-born-theory.md §3"
  - "notes/broken-born-theory.md §4"
  - "notes/broken-born-theory.md §5.1"
  - "notes/broken-born-theory.md §9"
  - "notes/stream-stability.md 'Setup'"
  - "notes/toy-lagrangian.md 'Success criteria (fixed 2026-10-19, before any construction)'"
  - "notes/toy-lagrangian.md 'Chunk 4 (in progress, 2026-10-19): S5'"
  - "review/round3/referee/audit-notes.md Step 1"
  - "review/round3/referee/audit-notes.md Step 2"
  - "review/wiki-build-flags.md items 5, 29"
  - "review/wiki-build-checks/audit/flag5_mass_scaling.out part D"
  - "review/wiki-build-checks/audit/c_yukawa_scaling.out"
  - "review/wiki-build-checks/audit/flag17_recompute.out part 3"
  - "review/wiki-build-flags.md item 55"
  - "notes/gate-mechanism.md §2"
  - "notes/gate-mechanism.md §3"
---

*A Yukawa force is the force carried by a field whose quanta have a mass M. Between two sources its potential falls as e^(−Mr)/r: at short distances it is the inverse-square force of a massless field, but beyond a distance of about ℏ/(Mc), the mediator's reduced Compton wavelength, it dies away exponentially, so the mass of the mediator sets the range of the force. In momentum the same law is the factor 1/(q² + M²), and that is the form in which such a force enters scattering. The program uses it in several places. Its [momentum graviton X](../momentum-graviton/_index.md) is massive, so the force X exerts on ordinary matter is "Yukawa-cut at 1/M_X", which the program gives as the reason experiments see no sign of it ([safety by range](../momentum-graviton/fifth-force-safety.md)). Torsion-balance limits on such forces, applied with the strength that the program's aligned vacuum gives X, keep X's range below 37.7 micrometres ([the laboratory bound on X's range](../momentum-graviton/range-bound.md)). The standard [self-interacting dark-matter](../../dark-matter/halo-astrophysics/self-interacting-dark-matter.md) models that the program's scattering predictions are measured against scatter through a light Yukawa mediator, and the program's own amplitude for conjugate matter keeps the Yukawa factor in the momentum transfer and multiplies it by a [velocity gate](../../dark-matter/conjugate-matter/velocity-gate.md). [Conjugate special relativity](../../conjugate-relativity/_index.md) reads X's short range as a range in momentum, which the checkpoint it cites does not state. The physics is textbook. The same name also covers a different object, the Yukawa coupling that gives particles their masses, which the program's toy models use as an analogy.*

**Status:** Established — [T] — textbook physics written here from general knowledge, with the literature it adds from model memory (†); the torsion-balance limits and the bimetric strength are cited from live-searched sources [S] by the [phase-space-diameter note](../../cosmology/scale-factor-duality/phase-space-diameter.md) ([§8.2](../../papers/phase-space-diameter.md#82-not-the-range-of-the-momentum-graviton-and-a-bound-on-it-dvs)). The program's uses carry their own tags: "Yukawa-cut at 1/M_X" is [D + T] in [calc note #8](../../history/documents/field-equation-notes.md) [§3](../../../notes/beta-coefficients.md#3-spectrum-parameters-selection-structure-d--t) and [D] in [checkpoint #11](../../history/documents/checkpoint.md) [§7.5](../../papers/broken-born-checkpoint-v2.md#75-spectrum-d); the gated amplitude is [D — mechanism; shape [O]] ([#11 §8](../../papers/broken-born-checkpoint-v2.md#8-conjugate-matter-and-the-gate)), whose mechanism flag 55 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md) finds not derived (pending); [#13](../../conjugate-relativity/_index.md)'s range in momentum is tagged [D — [checkpoint §7](../../papers/broken-born-checkpoint-v2.md#7-the-massive-momentum-graviton)] there and is flag 29 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md). [`verify/phase_space_diameter.py`](../../../verify/phase_space_diameter.py) checks the arithmetic of the 4/3 and reproduces the published torsion-balance limits from the experiment's exclusion table [V] ([the phase-space-diameter script](../../method/verification/phase-space-diameter-script.md)); no `verify/` script checks the rest of the physics on this page. Scripts written for the flags' audit, which are not part of the gate, check the relation between range and mass numerically and evaluate the Born cross-section in closed form ([`review/wiki-build-checks/audit/flag5_mass_scaling.out`](../../../review/wiki-build-checks/audit/flag5_mass_scaling.out) part D; [`review/wiki-build-checks/audit/flag17_recompute.out`](../../../review/wiki-build-checks/audit/flag17_recompute.out) part 3).

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

Here q is a wavevector, which in a scattering process is the momentum transfer. The two sides are a waveform and its spectrum ([the Fourier transform](../../phase-space/reciprocity/fourier-transform.md)). The spectrum is nearly flat for q ≪ M and falls as 1/q² for q ≫ M: a short range in position is a broad spectrum in q, and a long range is a spectrum concentrated near q = 0. Two limits bracket the form:

- **The massless limit**, M → 0. The factor becomes 1/q², the transform of the Coulomb profile 1/(4πr), and the spectrum is concentrated at small q, the wavevectors of long distances.
- **The contact limit**, M large compared with every q of interest. The factor is close to the constant 1/M², the transform of a point interaction δ³(r)/M². Exchange of a heavy field then acts as a contact interaction, with a strength proportional to the square of the coupling divided by M². Replacing the heavy field by that contact term is called integrating it out ([integrating out a heavy carrier](../../dark-matter/conjugate-matter/gate-mechanism.md#integrating-out-a-heavy-carrier)).

In field theory, 1/(q² + M²) is the field's propagator in the static case, in which the exchanged quantum carries momentum but no energy [T]. It is the form in which a Yukawa force enters the amplitudes below.

The scripts of the flags' audit check the relation between mass and range by evaluating the Fourier integral numerically rather than from the closed form. For the factor 1/(q² + c), where c stands in the place of M² (the script writes it k and calls it the quadratic coefficient), the fitted ranges are 1.0, 0.5 and 0.25 at c = 1, 4 and 16: "quadrupling the quadratic coefficient k halves the Yukawa range: the mass is sqrt(k)" ([`review/wiki-build-checks/audit/flag5_mass_scaling.out`](../../../review/wiki-build-checks/audit/flag5_mass_scaling.out) part D). The range is the inverse of the mass, not of its square, which is the point the audit needed for [flag 5](#the-momentum-graviton-x).

## Fifth forces: a Yukawa term beside gravity [T]

Searches for new forces between ordinary bodies describe a possible extra force by adding a Yukawa term to Newton's potential:

```text
V(r) = −(G m₁ m₂ / r) · (1 + α e^(−r/λ))
```

α is the strength of the extra force relative to gravity, positive for an extra attraction and negative for a repulsion, and λ = ℏ/(Mc) is its range. A force of "gravitational strength" has α of order one. This is the Yukawa potential of the previous sections with charges proportional to the masses of the two bodies, added to Newton's. The letters follow the experimental literature: λ here is not [the Born length](../../phase-space/reciprocity/born-length.md) of conjugate relativity, and α is not the program's gate coupling α̃.

### How experiments test it

Two kinds of experiment look for such a term [T]:

- **Tests of the inverse-square law** measure the force between bodies as a function of their separation: torsion balances in the laboratory at short separations, the orbits of the Moon and the planets at long ones.
- **Tests of the universality of free fall** compare the accelerations of bodies of different composition. A field whose charge is not proportional to mass, for example one coupled to baryon number, makes the acceleration depend on what a body is made of. A field coupled alike to all energy, as a spin-2 field coupled to the stress-energy is, does not ([the universality of free fall](equivalence-principle.md#the-weak-form-universality-of-free-fall-t)).

Each experiment is most sensitive to ranges comparable with the separations it probes. Where λ is much shorter than the separation of its test bodies, the factor e^(−r/λ) has removed the extra force before it reaches them, and the experiment's limit on α weakens exponentially as λ shrinks. The limits are drawn as an excluded region in the plane of λ and α, and toward short range that region ends: an extra force of gravitational strength is excluded only at ranges longer than about the shortest separations tested (Adelberger, Heckel and Nelson 2003 †; Fischbach and Talmadge 1999 †). The phase-space-diameter note quotes the limits at the shortest ranges, set out in the next subsection.

### Laboratory bounds at short range

At ranges of tens of micrometres the limits come from torsion balances, which measure the tiny torque that nearby masses exert on a pendulum hung from a thin fibre [T]. The phase-space-diameter note (§8.2) cites the experiment of Lee, Adelberger, Cook, Fleischer and Heckel, "New test of the gravitational 1/r² law at separations down to 52 μm" (2020) [S]. It limits "any gravitational-strength Yukawa interactions to ranges <38.6 μm" at 95% confidence: a term with |α| = 1 must have a range below 38.6 μm. For α = 8/3 the published limit is 30 μm. The authors draw the consequence for a "heavy graviton" of bimetric gravity, citing [Aoki and Mukohyama 2016](https://arxiv.org/abs/1604.06704) [S]: its mass "must be greater than 5.1 meV", which is ħc/(38.6 μm) ([`verify/phase_space_diameter.py`](../../../verify/phase_space_diameter.py)).

The limit depends on the sign of α. The experiment's exclusion table, in Lee's thesis (Table 11.4) [S], gives at each range the largest strength the data allow at 95% confidence, in a one-sided column for an attractive term, +α₉₅, and a two-sided column for a term of either sign, |α₉₅|. Referee A of [review round 5](../../method/review/round-5.md) also transcribed the repulsive column, −α₉₅ ([`review/round5/referee-A/scripts/lee_interp.py`](../../../review/round5/referee-A/scripts/lee_interp.py)). For a force known to be attractive, as the exchange of a spin-2 field is, the note uses the one-sided column, which is the more conservative of the two here (note §8.2; round-5 ruling R12). The two columns at three strengths, from the round-5 arbitration ([`review/round5/adjudicator/arb.out`](../../../review/round5/adjudicator/arb.out), B9):

| α | one-sided +α₉₅ | two-sided \|α₉₅\| |
| --- | --- | --- |
| 1 | 40.66 μm | 38.63 μm |
| 4/3 | 37.68 μm | 35.79 μm |
| 8/3 | 31.69 μm | 30.23 μm |

The two-sided values 38.63 and 30.23 μm reproduce the published 38.6 and 30 μm, which checks the transcription of the table and the interpolation between its rows. The row at α = 4/3 is the one the program uses ([the momentum graviton X](#the-momentum-graviton-x)).

An earlier experiment by several of the same authors was aimed at the dark-energy length. [Sundrum 2004](https://arxiv.org/abs/hep-th/0306106) [S] had proposed a gravitational-strength modification of gravity at that length to address [the cosmological-constant problem](cosmological-constant-problem.md), and [Kapner et al. 2007](https://arxiv.org/abs/hep-ph/0611184) [S] tested the inverse-square law "below the dark-energy length scale" (note §8.2). Both round-5 referees quote that length from Kapner et al. as λ_d ≈ 85 μm ([`review/round5/referee-A/audit-notes.md`](../../../review/round5/referee-A/audit-notes.md) and [`review/round5/referee-B/audit-notes.md`, §4.5](../../../review/round5/referee-B/audit-notes.md#45-prior-art-for-d-results-searches-inspire-fulltexttitle-queries-in-downloadsinspire_q-arxiv-sources)); the note expresses its dark-energy scale, ρ_Λ^{1/4} = 2.24 meV with ρ_Λ the dark-energy density, as the length 88.1 μm (§7). Torsion-pendulum experiments at the Huazhong University of Science and Technology (HUST) test the same range (Tan et al. 2016 †, 2020 †). Referee B of round 5 reports a 2026 review ([arXiv:2605.18212](https://arxiv.org/abs/2605.18212)) that names the 2020 results of the University of Washington, where Lee et al. worked, and of HUST as still the tightest limits at these ranges ([`review/round5/referee-B/audit-notes.md` §4.5](../../../review/round5/referee-B/audit-notes.md#45-prior-art-for-d-results-searches-inspire-fulltexttitle-queries-in-downloadsinspire_q-arxiv-sources)).

### A massive spin-2 mediator

The exchange of a massive spin-2 field between two slowly moving bodies adds an attractive Yukawa term [T]. Its coefficient is not the one a massless graviton with the same coupling to matter would give. The massive field has five polarizations ([the Fierz–Pauli mass term](fierz-pauli.md)), and its helicity-zero polarization also couples to the trace of the source's stress-energy, which changes the coefficient by a fixed factor that does not approach one as M → 0: the van Dam–Veltman–Zakharov discontinuity (van Dam and Veltman 1970 †; Zakharov 1970 †) [T]. The factor is of order one, so the force is of gravitational strength in either case. For static sources it is 4/3: the massless graviton's exchange between two bodies carries the tensor factor 1 − 1/2, and a massive spin-2 field's carries 1 − 1/3 [T]; [`verify/phase_space_diameter.py`](../../../verify/phase_space_diameter.py) checks the ratio. In [Hassan–Rosen bimetric gravity](hassan-rosen-bimetric.md), with matter coupled to the metric g, the phase-space-diameter note writes the massive field's strength relative to gravity as

```text
α = (4/3) (M_f u / M_g)²
```

with M_g and M_f the Planck masses of the two metrics and u the ratio of their backgrounds, f̄ = u²ḡ (§8.2, citing [Lüben, Mörtsell and Schmidt-May 2020](https://arxiv.org/abs/1812.08686), eq. 9 [S], and [Enander and Mörtsell 2013](https://arxiv.org/abs/1306.1086), eq. 4.1 [S]). The cited papers write the ratio c, as does [the Hassan–Rosen page](hassan-rosen-bimetric.md#the-spectrum-t); the note writes u to keep it apart from the speed of light. "Only the product M_f u is fixed by the theory, so equal Planck masses give α = 4/3 only if u = 1" (§8.2).

## Scattering through a Yukawa mediator [T]

### The Born amplitude

In the Born approximation, first order in the potential, the amplitude for two particles to scatter is proportional to the Fourier transform of their potential at the momentum transfer q ([what a position-local force depends on](../../dark-matter/conjugate-matter/velocity-gate.md#background-what-a-position-local-force-depends-on-t)). For a Yukawa force it is therefore proportional to 1/(q² + M²). In the centre-of-mass frame each particle arrives with momentum k and leaves with a momentum of the same size, turned through an angle θ, so the transfer q = 2k sin(θ/2) runs from 0 in a grazing collision to 2k in a head-on rebound. The momentum is k = m_r v, with m_r the reduced mass and v the relative speed; for two particles of equal mass m it is k = mv/2, the [lab notebook](../../history/documents/lab-notebook.md)'s k = m_χv_rel/2 ([#1 §3](../../../notes/broken-born-theory.md#3-action)). The angular distribution is

```text
dσ/dΩ ∝ (m_r Q₁Q₂)² / (q² + M²)²
```

The momentum-transfer cross-section σ_T weights each direction by the fraction of forward momentum the collision removes, 1 − cos θ ([the transfer cross-section σ_T](../../dark-matter/halo-astrophysics/transfer-cross-section.md)). Written as an integral over the transfer, with 1 − cos θ = q²/(2k²) and dΩ = 2πq dq/k²,

```text
σ_T ∝ ((m_r Q₁Q₂)² / k⁴) · ∫₀^{2k} q³ dq / (q² + M²)²
```

This is the integral that the flag-17 audit evaluated in closed form ([`review/wiki-build-checks/audit/flag17_recompute.out`](../../../review/wiki-build-checks/audit/flag17_recompute.out) part 3). How it behaves depends on how the largest transfer, 2k, compares with M.

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

The Born approximation assumes that the potential is weak. For an attractive Yukawa force it needs, roughly, the coupling times the ratio of the particle's mass to the mediator's mass to be small [T]. Beyond it, an attractive force can hold quasi-bound states, and σ_T(v) shows resonances; and when the range is long compared with the particles' de Broglie wavelength and the force is strong, the scattering becomes classical. In both regimes σ_T(v) departs from the Born forms above (Tulin, Yu and Zurek 2013 †; [the Born regime and beyond](../../dark-matter/halo-astrophysics/self-interacting-dark-matter.md#the-born-regime-and-beyond)).

## How the program uses it

### The momentum graviton X

X is a massive spin-2 field whose mass M_X is "the polarization-breaking scale" ([#11 §7.1](../../papers/broken-born-checkpoint-v2.md#71-the-chain-d--t); [the gravitational Higgs mechanism](../momentum-graviton/gravitational-higgs.md)). Ordinary matter couples to the metric g, which contains X as well as the massless graviton; with the [equal Planck masses](../momentum-graviton/spectrum-and-parity.md#equal-planck-masses) that reciprocity forces, the two enter with comparable weight, so the force X carries between ordinary bodies is a Yukawa force of gravitational strength. Calc note [#8 §3](../../../notes/beta-coefficients.md#3-spectrum-parameters-selection-structure-d--t) [D + T] states the consequence, SM being the Standard Model:

> "safety is by **range**, not decoupling: X-mediated forces on the SM are Yukawa-cut at 1/M_X, and gravitational-strength short-range forces are experimentally unconstrained down to far below any plausible M_X."

[#11 §7.5](../../papers/broken-born-checkpoint-v2.md#75-spectrum-d) [D] keeps it as "SM couplings gravitational-strength and Yukawa-cut at 1/M_X". In the fifth-force form above, X adds a term with range λ = ℏ/(M_X c) and the bimetric strength α = (4/3)(M_f u/M_g)²; reciprocity makes the two Planck masses equal, and in the program's aligned vacuum the background ratio is u = 1, so α = 4/3 ([phase-space-diameter note §8.2](../../papers/phase-space-diameter.md#82-not-the-range-of-the-momentum-graviton-and-a-bound-on-it-dvs)). The argument of #8 is that experiments exclude such a term only at ranges far longer than ℏ/(M_X c); it and its earlier forms are on [safety by range](../momentum-graviton/fifth-force-safety.md). No document before the phase-space-diameter note quoted an experimental limit or bounded M_X, and none gives M_X a value ([no value for M_X](../momentum-graviton/spectrum-and-parity.md#no-value-for-m_x)). The note (§8.2) reads the one-sided column of the torsion-balance table above at α = 4/3 and obtains λ_X < 37.7 μm and M_X c² > 5.2 meV [V], conditional on u = 1; at u = 0.5 the limit is 57.0 μm [V] ([the laboratory bound on X's range](../momentum-graviton/range-bound.md)).

The range also settles what M_X denotes. A Yukawa range 1/M_X makes M_X the mass of X's quanta, not its square. The flags' audit uses this for flag 5, which says that [#11 §7.5](../../papers/broken-born-checkpoint-v2.md#75-spectrum-d)'s "M_X ∝ 2(β₁+β₂)" should be M_X² ∝ 2(β₁+β₂), the form of its source, [#8 §3](../../../notes/beta-coefficients.md#3-spectrum-parameters-selection-structure-d--t) ([spectrum, parameters and reciprocity parity](../momentum-graviton/spectrum-and-parity.md)). The audit's script fits the decay of the static profile, finds the decay constant equal to M_X, and prints "d ln M_X / d ln(b1+b2) = 0.5" ([`review/wiki-build-checks/audit/c_yukawa_scaling.out`](../../../review/wiki-build-checks/audit/c_yukawa_scaling.out)). The flag is confirmed by the audit and is a question of notation only (item 5 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md)).

### The standard expectations of rows 1 and 2

[The checkpoint](../../history/documents/checkpoint.md)'s predictions table sets the program's dark-matter scattering against self-interacting dark matter (SIDM) with a Yukawa mediator, whose behaviour is the light-mediator limit above ([#11 §13](../../papers/broken-born-checkpoint-v2.md#13-predictions-and-kill-conditions)):

```text
Row 1, σ_T(v) across halo masses:   "CDM none; Yukawa SIDM power-law + Coulomb log"
Row 2, scattering anisotropy:       "Forward-peaked (light mediators)"
```

Cold dark matter, CDM, does not scatter off itself at all. The [lab notebook](../../history/documents/lab-notebook.md) states the two behaviours, "Yukawa SIDM falls as v⁻⁴ with a Coulomb-log correction" and "light-mediator Yukawa scattering is forward-peaked" ([#1 §5.1](../../../notes/broken-born-theory.md#51-the-scattering-law-d)), and its own table had "Constant (CDM: 0) or power-law v⁻⁴ln tail (Yukawa SIDM)" ([#1 §9](../../../notes/broken-born-theory.md#9-predictions)). It separates the program's law from "*every* x-local mediator model", x-local meaning local in position, by two signatures: the shape of the fall at high speed, "An exponential cliff, not a power-law tail", and "Isotropy inside the gate" ([#1 §5.1](../../../notes/broken-born-theory.md#51-the-scattering-law-d)). In the Born regime a Yukawa cross-section is itself flat at low speed, so the two laws differ in how they fall and in their angular distributions. The notebook places the separation in speed at "v ∼ 150–400 km/s (large spirals, small groups), where the two shapes diverge by orders of magnitude" ([#1 §5.1](../../../notes/broken-born-theory.md#51-the-scattering-law-d)). The exponential cliff has since been weakened to a knee whose tail is open ([the gated scattering law σ_T(v)](../../dark-matter/conjugate-matter/scattering-law.md)). The tests are [Row 1: the knee in σ_T(v)](../../predictions/self-interaction-knee.md) and [Row 2: isotropic scattering below the gate](../../predictions/scattering-isotropy.md); the halo physics is on [self-interacting dark matter](../../dark-matter/halo-astrophysics/self-interacting-dark-matter.md).

### The gated amplitude

The program's amplitude for the self-scattering of [conjugate matter](../../dark-matter/conjugate-matter/_index.md) χ keeps the Yukawa factor in the transfer q and multiplies it by a factor in the incoming relative momentum k:

```text
M(k, q) = 4πα̃m_χ / (q² + m_φ²) · F(k²/μ²)        (#11 §8)
```

M(k, q) is the amplitude, not a mass; m_χ is the χ mass, α̃ the coupling, m_φ the mass of the carrier of the transfer, F the gate and μ its width in momentum. #11 does not define α̃, m_φ or F, and the wiki takes them from the lab notebook ([the amplitude](../../dark-matter/conjugate-matter/velocity-gate.md#the-amplitude)). The first factor is the Born amplitude of a Yukawa force of range 1/m_φ. The gate depends on k, "the variable no x-local mediator produces" ([#11 §8](../../papers/broken-born-checkpoint-v2.md#8-conjugate-matter-and-the-gate)). [`notes/gate-mechanism.md`](../../../notes/gate-mechanism.md) (2026-10-28, not reviewed) qualifies the phrase: it "holds only for the direct Born term. Exchange terms and near-threshold states of x-local forces do depend on k at fixed q" ([§3](../../../notes/gate-mechanism.md#3-the-fiber-overlap-read-two-ways)). In the lab notebook's v0.1 form the gate is a Gaussian that tends to 1 as μ grows, and "An x-local Yukawa is the limit μ → ∞" ([#1 §3](../../../notes/broken-born-theory.md#3-action)).

The lab notebook puts the first factor in the contact limit: its scattering law assumes "a heavy transfer mediator (m_φ ≳ m_χ, contact-like in x)" ([#1 §5.1](../../../notes/broken-born-theory.md#51-the-scattering-law-d)). Two consequences follow from the contact limit described above.

- **Isotropy below the gate.** The first factor is flat in q, and the gate does not depend on the angle, so scattering below the gate is isotropic: "isotropic below the gate versus Yukawa forward-peaking" ([#11 §8](../../papers/broken-born-checkpoint-v2.md#8-conjugate-matter-and-the-gate)). The isotropy rests on the heavy-mediator assumption, which #11 does not restate ([the heavy-mediator assumption](../../predictions/scattering-isotropy.md#the-heavy-mediator-assumption)).
- **The dependence on speed is the gate's.** In the contact limit the Yukawa factor adds no dependence on speed of its own. The flag-17 audit evaluated the transfer cross-section without the gate, with the full Yukawa factor, at the program's benchmark, m_φ = m_χ = 70 MeV and k = m v\*/2 with v\* the gate velocity. Its change relative to the zero-speed value is "2.13628772255849e-7 (negligible: the v-dependence of sigma_T is the gate's alone)" ([`review/wiki-build-checks/audit/flag17_recompute.out`](../../../review/wiki-build-checks/audit/flag17_recompute.out) part 3; [the scattering benchmark](../../dark-matter/conjugate-matter/benchmark.md)).

The lab notebook's low-speed cross-section, σ₀ = 16πα̃²m_χ²/m_φ⁴ ([#1 §5.1](../../../notes/broken-born-theory.md#51-the-scattering-law-d)), depends on the coupling and the masses as a contact cross-section does. [The clumping problem](../../history/documents/clumping-notes.md)'s mean-field model takes the same limit for its coupling g ≡ 4πα̃/m_φ² (a coupling, not the metric), with "the x-range collapsed to contact (range 1/m_φ, microscopic)" ([`notes/stream-stability.md`](../../../notes/stream-stability.md) 'Setup'; [the gated Vlasov model](../../dark-matter/momentum-clumping/gated-vlasov-model.md)).

[#11 §8](../../papers/broken-born-checkpoint-v2.md#8-conjugate-matter-and-the-gate) gives the gate's mechanism as X exchange, "delivered by X-exchange between dual-stress bilinears" [D — mechanism; shape [O]]. Calc note [#6 §4](../../../notes/x-classification.md#4-consequences-downstream-d--structural-with-one-honest-downgrade) takes the contact limit of that exchange, "Integrating out massive X between χ bilinears gives the contact four-χ operator", and the dependence on k then enters through the width μ of a χ quantum in momentum ([the gate mechanism](../../dark-matter/conjugate-matter/gate-mechanism.md)) (not derived, according to flag 55 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md), pending; [the gate mechanism](../../dark-matter/conjugate-matter/gate-mechanism.md#exchanging-x-cannot-produce-the-gate)). [`notes/gate-mechanism.md`](../../../notes/gate-mechanism.md) (2026-10-28; two derivations, the second blind) finds that single exchange of the massive spin-2 X gives an amplitude whose rational structure sits in the transfer, the propagator 1/(q² + M_X²), with a k-dependence that is a polynomial with the speed of light as its velocity scale (§§2–3); for identical χ the exchange term adds "the same Yukawa force seen at backward angles" ([§2](../../../notes/gate-mechanism.md#2-exchanging-the-x-of-7-cannot-produce-the-gate); one derivation). No document relates m_φ to X's mass M_X.

### Conjugate special relativity: a range in momentum

[#13 §6](../../papers/conjugate-special-relativity.md#6-what-is-shared-what-is-broken-what-is-open) names what the breaking of reciprocity makes different between the two polarizations: "the long-range/short-range asymmetry — our null structure is policed by massless gravity, the dual structure's dynamical part by the massive X, so dual-geometric effects are Yukawa-cut in momentum [D — [checkpoint §7](../../papers/broken-born-checkpoint-v2.md#7-the-massive-momentum-graviton)]". Its plain-language passage says "ours reaches across the universe and theirs is short-ranged" ([the equivalence principle as dual relativity](../../conjugate-relativity/equivalence-principle.md#what-the-breaking-makes-different)). [#13 §1](../../papers/conjugate-special-relativity.md#1-two-causal-cones) has X modify "the dual cone only at short range in momentum [D — [§7](../../papers/broken-born-checkpoint-v2.md#7-the-massive-momentum-graviton) of the checkpoint]" ([two causal cones](../../conjugate-relativity/two-causal-cones.md#the-slaved-dual-cone-and-x)).

A Yukawa range is a distance between sources, and the derived statement in [#11 §7.5](../../papers/broken-born-checkpoint-v2.md#75-spectrum-d) is a range of that kind, for the forces between ordinary bodies. [#11 §7](../../papers/broken-born-checkpoint-v2.md#7-the-massive-momentum-graviton) states no range in momentum. #13's citation of it for one is flag 29 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md), confirmed by the flags' audit, pending ([conflicts between sources](../../history/documents/source-conflicts.md)). The reading in momentum appears elsewhere only among the results that exist in the old chat: "dual Newtonian limit = Yukawa in momentum = the gate" ([`HANDOFF.md` §4](../../../HANDOFF.md#4-results-that-exist-only-in-the-chat-not-in-any-artifact)). No document derives a Yukawa form in momentum. The documented counterpart is the gate's mechanism, X exchange, whose shape is open ([two gravitational charges and the conjugate field equations (chat-only)](../momentum-graviton/chat-only-results.md#the-dual-newtonian-limit-and-the-gate); [Open: the gate shape](../../dark-matter/conjugate-matter/gate-shape.md)).

### The field τ: no coupling, so no Yukawa force

The program's dark-energy field [τ](../../cosmology/dark-energy/tau-quintessence.md) is "ultralight" ([#1 §4](../../../notes/broken-born-theory.md#4-consistency-with-everything-already-measured)). A field still evolving on cosmological time scales must be so light that the range of a force it carried would be at least comparable to the observable universe, so range offers it no protection [T]. The lab notebook's argument concerns the coupling instead: "τ is a (pseudo-)Goldstone: derivatively coupled, no tree-level Yukawa to SM matter, safe from torsion-balance bounds despite being ultralight. [D]" ([#1 §4](../../../notes/broken-born-theory.md#4-consistency-with-everything-already-measured)). "Yukawa" there means a coupling of τ's value to matter, whose exchange would produce a Yukawa force of that long range; a field that couples only through its derivatives produces no static force between unpolarized bodies ([fifth-force safety of τ](../../cosmology/dark-energy/tau-fifth-force.md)). X and τ are the two cases: X couples at gravitational strength over a short range, and τ has a cosmological range but no such coupling.

## A name collision: the Yukawa coupling

"Yukawa coupling" names a different object [T]. In particle physics it is an interaction term that joins a scalar field φ to a fermion field ψ, of the form y φ ψ̄ψ with y a dimensionless constant. Yukawa's theory coupled the meson field to nucleons in this way, and exchange of the meson through that coupling produces his potential, so the two uses share an origin. In the Standard Model the coupling has a second role: once the Higgs field takes its vacuum value, a Yukawa coupling between the Higgs field and a fermion becomes a mass term for the fermion, proportional to y times that value ([masses from a vacuum value](../../symmetry-breaking/goldstone-and-higgs.md#masses-from-a-vacuum-value)).

The program's toy-model work uses the word in this second sense, as an analogy for the way a choice of vacuum can make the interactions of matter local. The analogy concerns no force and no range:

- The toy-model note's abstract: a coupling built from (H, K) "makes interactions local in one and nonlocal in the other — the analogue of Yukawa-generated masses. A mechanism forcing such a coupling is not given." Its §5: "as fermion masses follow from a Higgs vacuum value once Yukawa couplings are given. Nothing here forces that coupling." ([Locality from an (H, K)-built coupling](../../symmetry-breaking/matter-coupling.md).)
- The worklog's criterion S5: "This is the analogue of a Yukawa coupling giving masses through a vacuum expectation value" ('Success criteria'); its result: "This works as a Yukawa coupling does" ('Chunk 4') ([success criteria S0–S5](../../symmetry-breaking/toy-models/success-criteria.md)).
- [#11 §14 item 11](../../papers/broken-born-checkpoint-v2.md#14-open-problems) keeps open "locality of matter beyond the weak (Yukawa-like) form, which in the toy reduces to P4" [O], P4 being the postulate of [polarized matter and strict sector separation](../../program/postulates/p4-polarized-matter.md). "Weak" refers to locality that follows once the coupling is chosen; the worklog's strong form is "locality forced, not chosen" ('Chunk 4'). The word does not describe the strength of a force ([Open: forced locality and the P4 lock](../../symmetry-breaking/strong-locality.md)).
- The round-4 referee: "the Yukawa analogy is heuristic" ([`review/round4/referee/audit-notes.md`](../../../review/round4/referee/audit-notes.md) Step 2(d)).

The loop estimates of kinetic mixing for [#14](../../../notes/knot-dark-matter-standalone.md)'s soliton model ([Obituary: #14's superheavy-soliton model](../../dark-matter/candidates/soliton-candidate/obituary.md)) also contain Yukawa couplings in the particle-physics sense: a one-loop factor with "y" and an "O(1) hidden Yukawa" ([`review/round3/referee/audit-notes.md`](../../../review/round3/referee/audit-notes.md) Steps 1 and 2; [Under review: Planck-suppressed adjoint mixing](../../dark-matter/candidates/soliton-candidate/dimension-five-operator.md); [kinetic mixing between sectors](../../dark-matter/candidates/soliton-candidate/kinetic-mixing.md)).

In the wiki, "Yukawa force", "Yukawa potential", "Yukawa-cut", "Yukawa mediator" and "Yukawa SIDM" refer to the force on this page; "Yukawa coupling", "Yukawa-generated masses" and "the weak (Yukawa-like) form" refer to the coupling. τ's "no tree-level Yukawa" names the coupling whose exchange would produce the force.

## References

Cited by the phase-space-diameter note, retrieved by live search [S] ([`wiki/papers/phase-space-diameter.md`](../../papers/phase-space-diameter.md) 'References'):

- J. G. Lee, E. G. Adelberger, T. S. Cook, S. M. Fleischer, B. R. Heckel, "New test of the gravitational 1/r² law at separations down to 52 μm," Phys. Rev. Lett. 124, 101101 (2020), [arXiv:2002.11761](https://arxiv.org/abs/2002.11761); J. G. Lee, "A Fourier–Bessel test of the gravitational inverse-square law," PhD thesis, University of Washington (2020), Table 11.4 [S]: the limits and the exclusion table.
- D. J. Kapner, T. S. Cook, E. G. Adelberger, J. H. Gundlach, B. R. Heckel, C. D. Hoyle, H. E. Swanson, "Tests of the gravitational inverse-square law below the dark-energy length scale," Phys. Rev. Lett. 98, 021101 (2007), [arXiv:hep-ph/0611184](https://arxiv.org/abs/hep-ph/0611184) [S].
- R. Sundrum, "Fat gravitons, the cosmological constant and submillimeter tests," Phys. Rev. D 69, 044014 (2004), [arXiv:hep-th/0306106](https://arxiv.org/abs/hep-th/0306106) [S].
- K. Aoki, S. Mukohyama, "Massive gravitons as dark matter and gravitational waves," Phys. Rev. D 94, 024001 (2016), [arXiv:1604.06704](https://arxiv.org/abs/1604.06704) [S]: the heavy graviton of bigravity that Lee et al. bound.
- M. Lüben, E. Mörtsell, A. Schmidt-May, "Bimetric cosmology is compatible with local tests of gravity," Class. Quantum Grav. 37, 047001 (2020), [arXiv:1812.08686](https://arxiv.org/abs/1812.08686) [S]; J. Enander, E. Mörtsell, "Strong lensing constraints on bimetric massive gravity," JHEP 10 (2013) 031, [arXiv:1306.1086](https://arxiv.org/abs/1306.1086) [S]: the bimetric strength α = (4/3)(M_f c/M_g)², in their notation.

The program's documents cite no other source for Yukawa forces. Added by the wiki from model memory (†):

- H. Yukawa, "On the interaction of elementary particles. I," Proc. Phys.-Math. Soc. Japan (1935)†: the nuclear force carried by a massive quantum, and its potential.
- P. Debye, E. Hückel (1923)†: the screened potential in electrolytes.
- E. G. Adelberger, B. R. Heckel, A. E. Nelson, "Tests of the gravitational inverse-square law," Annu. Rev. Nucl. Part. Sci. (2003)†; E. Fischbach, C. L. Talmadge, *The Search for Non-Newtonian Gravity* (1999)†: the Yukawa parametrization of fifth forces and the experiments that test it.
- H. van Dam, M. Veltman, Nucl. Phys. B (1970)†; V. I. Zakharov, JETP Lett. (1970)†: the discontinuity of massive spin-2 exchange.
- W.-H. Tan et al., Phys. Rev. Lett. (2016)† and (2020)†: torsion-pendulum tests of the inverse-square law at submillimetre ranges, at the Huazhong University of Science and Technology. The record gives no values from them.
- A. Zee, *Quantum Field Theory in a Nutshell* (2003)†: attraction by even-spin exchange and repulsion by spin-1 exchange.
- S. Tulin, H.-B. Yu, K. M. Zurek, "Beyond collisionless dark matter: particle physics dynamics for dark matter halo structure," Phys. Rev. D (2013)†: Yukawa scattering in the Born, resonant and classical regimes.
- A. Loeb, N. Weiner, "Cores in dwarf galaxies from dark matter with a Yukawa potential," Phys. Rev. Lett. (2011)†: velocity-dependent self-interaction through a light mediator.

## Used by

- [Safety by range: X and ordinary matter](../momentum-graviton/fifth-force-safety.md) — X's force on ordinary matter is cut off beyond 1/M_X.
- [The laboratory bound on X's range](../momentum-graviton/range-bound.md) — the bimetric strength α = (4/3)(M_f u/M_g)² and the torsion-balance limits, read at α = 4/3.
- [The gravitational Higgs mechanism](../momentum-graviton/gravitational-higgs.md) — a massive X has a finite range.
- [Spectrum, parameters and reciprocity parity](../momentum-graviton/spectrum-and-parity.md) — M_X, whose inverse is X's range; flag 5.
- [The X-condensate candidate](../../dark-matter/candidates/x-condensate.md) and [Open: the dual-stress enhancement (OP5)](../../dark-matter/conjugate-matter/dual-stress-enhancement.md) — X's couplings to ordinary matter are of gravitational strength and Yukawa-cut.
- [The velocity gate](../../dark-matter/conjugate-matter/velocity-gate.md) — the amplitude's first factor; a position-local Yukawa force is the limit μ → ∞.
- [The gate mechanism: X exchange over fiber overlap](../../dark-matter/conjugate-matter/gate-mechanism.md) — the contact limit of X exchange.
- [The gated scattering law σ_T(v)](../../dark-matter/conjugate-matter/scattering-law.md) — set against the Yukawa v⁻⁴ tail and forward peaking.
- [The scattering benchmark](../../dark-matter/conjugate-matter/benchmark.md) and [the gated Vlasov model](../../dark-matter/momentum-clumping/gated-vlasov-model.md) — the heavy mediator, contact-like in position.
- [Row 1: the knee in σ_T(v)](../../predictions/self-interaction-knee.md) and [Row 2: isotropic scattering below the gate](../../predictions/scattering-isotropy.md) — measured against Yukawa SIDM.
- [The equivalence principle as dual relativity](../../conjugate-relativity/equivalence-principle.md) and [two causal cones](../../conjugate-relativity/two-causal-cones.md) — #13's short range "in momentum".
- [Two gravitational charges and the conjugate field equations (chat-only)](../momentum-graviton/chat-only-results.md) — "Yukawa in momentum".
- [Fifth-force safety of τ](../../cosmology/dark-energy/tau-fifth-force.md) — no Yukawa coupling, so no long-range Yukawa force.

## Sources

- [`wiki/papers/broken-born-checkpoint-v2.md` §7.5](../../papers/broken-born-checkpoint-v2.md#75-spectrum-d) — "SM couplings gravitational-strength and Yukawa-cut at 1/M_X" [D]; [§7.1](../../papers/broken-born-checkpoint-v2.md#71-the-chain-d--t) — M_X as the polarization-breaking scale; [§8](../../papers/broken-born-checkpoint-v2.md#8-conjugate-matter-and-the-gate) — the gated amplitude, "the variable no x-local mediator produces", the mechanism [D — mechanism; shape [O]], "isotropic below the gate versus Yukawa forward-peaking"; [§13 rows 1–2](../../papers/broken-born-checkpoint-v2.md#13-predictions-and-kill-conditions) — the standard expectations; [§14 item 11](../../papers/broken-born-checkpoint-v2.md#14-open-problems) — "the weak (Yukawa-like) form" [O]
- [`wiki/papers/reciprocity-toy-models.md`](../../papers/reciprocity-toy-models.md) Abstract, [§5](../../papers/reciprocity-toy-models.md#5-matter-and-locality) — the analogy with Yukawa-generated masses
- [`review/round4/referee/audit-notes.md`](../../../review/round4/referee/audit-notes.md) Step 2(d) — "the Yukawa analogy is heuristic"
- [`wiki/papers/phase-space-diameter.md` §8.2](../../papers/phase-space-diameter.md#82-not-the-range-of-the-momentum-graviton-and-a-bound-on-it-dvs) — the bimetric strength α = (4/3)(M_f u/M_g)² and its 4/3, the torsion-balance limits of Lee et al. 2020 and the choice of column, Sundrum and Kapner et al., the bound on X's range [D][V][S]; §7 — the dark-energy length 88.1 μm; 'References' — the [S] sources
- [`verify/phase_space_diameter.py`](../../../verify/phase_space_diameter.py) 'Consequences (note §8)' — the 4/3, the published limits reproduced, Lee et al.'s 5.1 meV as ħc/(38.6 μm), the bound at α = 4/3 [V]
- [`review/round5-adjudication.md`](../../../review/round5-adjudication.md) 'Rulings' R1, R12 — the background ratio; the two columns and why the one-sided one is used
- [`review/round5/adjudicator/arb.out`](../../../review/round5/adjudicator/arb.out) B9 — the two columns at three strengths
- [`review/round5/referee-A/scripts/lee_interp.py`](../../../review/round5/referee-A/scripts/lee_interp.py) — the repulsive column of the thesis table
- [`review/round5/referee-A/audit-notes.md` §4.5](../../../review/round5/referee-A/audit-notes.md#45-prior-art-for-the-d-items-searched-inspire-records-in-downloadsinspire); [`review/round5/referee-B/audit-notes.md` §4.5](../../../review/round5/referee-B/audit-notes.md#45-prior-art-for-d-results-searches-inspire-fulltexttitle-queries-in-downloadsinspire_q-arxiv-sources) — Kapner et al.'s λ_d ≈ 85 μm; the 2026 review naming the 2020 limits as the tightest
- [`wiki/papers/conjugate-special-relativity.md` §1](../../papers/conjugate-special-relativity.md#1-two-causal-cones), [§6](../../papers/conjugate-special-relativity.md#6-what-is-shared-what-is-broken-what-is-open) — "short range in momentum", "Yukawa-cut in momentum", the plain-language passage
- [`HANDOFF.md` §4](../../../HANDOFF.md#4-results-that-exist-only-in-the-chat-not-in-any-artifact) — "dual Newtonian limit = Yukawa in momentum = the gate" (chat-only)
- [`notes/beta-coefficients.md` §3](../../../notes/beta-coefficients.md#3-spectrum-parameters-selection-structure-d--t) — safety by range, X-mediated forces "Yukawa-cut at 1/M_X" [D + T]
- [`notes/x-classification.md` §4](../../../notes/x-classification.md#4-consequences-downstream-d--structural-with-one-honest-downgrade) — integrating out massive X gives the contact operator
- [`notes/broken-born-theory.md` §3](../../../notes/broken-born-theory.md#3-action) — k = m_χv_rel/2; "An x-local Yukawa is the limit μ → ∞"; [§4](../../../notes/broken-born-theory.md#4-consistency-with-everything-already-measured) — τ with "no tree-level Yukawa to SM matter"; [§5.1](../../../notes/broken-born-theory.md#51-the-scattering-law-d) — the heavy transfer mediator, Yukawa SIDM's v⁻⁴ fall with a Coulomb log, forward peaking, the two signatures, the discriminating band, σ₀; [§9](../../../notes/broken-born-theory.md#9-predictions) — the v0.1 row 1
- [`notes/stream-stability.md`](../../../notes/stream-stability.md) 'Setup' — the contact coupling g ≡ 4πα̃/m_φ², range 1/m_φ collapsed to contact
- [`notes/toy-lagrangian.md`](../../../notes/toy-lagrangian.md) 'Success criteria (fixed 2026-10-19, before any construction)', 'Chunk 4 (in progress, 2026-10-19): S5' — S5 as the analogue of a Yukawa coupling; the weak and strong forms
- [`review/round3/referee/audit-notes.md`](../../../review/round3/referee/audit-notes.md) Steps 1 and 2 — the Yukawa couplings in the kinetic-mixing estimates for #14's soliton model
- [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md) items 5, 29 — M_X or M_X², confirmed, notation only; #13's range in momentum, confirmed, pending; item 55 — the gate's mechanism not derived, pending
- [`notes/gate-mechanism.md` §2](../../../notes/gate-mechanism.md#2-exchanging-the-x-of-7-cannot-produce-the-gate) — X exchange polynomial in k with velocity scale c, the u channel as the Yukawa force at backward angles; [§3](../../../notes/gate-mechanism.md#3-the-fiber-overlap-read-two-ways) — "the variable no x-local mediator produces" holds only for the direct Born term; the rationality sits in the transfer
- [`review/wiki-build-checks/audit/flag5_mass_scaling.out`](../../../review/wiki-build-checks/audit/flag5_mass_scaling.out) part D; [`review/wiki-build-checks/audit/c_yukawa_scaling.out`](../../../review/wiki-build-checks/audit/c_yukawa_scaling.out) — the range as the inverse of the mass, checked numerically
- [`review/wiki-build-checks/audit/flag17_recompute.out`](../../../review/wiki-build-checks/audit/flag17_recompute.out) part 3 — the Born transfer cross-section with the full Yukawa factor: its constant heavy-mediator limit and its negligible change at the benchmark
