---
title: "The velocity dispersion σ"
weight: 5
status: established
description: "The spread of velocities in a galaxy, halo or cluster: its definition and the Maxwellian, the virial relation between σ, size and mass, line-of-sight measurement in dwarf galaxies, stars against dark matter, the spread of pair speeds, the uncited values the program's notes use from 3 to 1000 km/s, and where σ enters the program: the gate's open and narrow regimes, the stream criterion, the occupation number, the wave-island condensation rate, Scenario A's dispersion ratio and row 3's (v*/σ)⁴."
provenance: [T]
sources:
  - "papers/broken-born-checkpoint-v2.md §8"
  - "papers/broken-born-checkpoint-v2.md §9"
  - "papers/broken-born-checkpoint-v2.md §13 rows 1, 3"
  - "notes/stream-stability.md 'Setup'"
  - "notes/stream-stability.md 'Limit 1 — broad gate'"
  - "notes/stream-stability.md 'Limit 2 — narrow gate'"
  - "notes/stream-stability.md 'Numbers at the scattering benchmark'"
  - "notes/stream-stability.md 'Corollary (the classicality theorem)'"
  - "notes/stream-stability.md 'Consequences for the predictions table'"
  - "notes/wave-island.md 'Setup'"
  - "notes/wave-island.md 'The rate'"
  - "notes/wave-island.md 'What pins g? Two scenarios'"
  - "notes/ufd-endpoint.md 'Sharpened input numbers'"
  - "notes/ufd-endpoint.md 'The data'"
  - "notes/broken-born-theory.md §5.1"
  - "notes/broken-born-theory.md §5.2"
  - "review/wiki-build-flags.md item 17"
  - "review/wiki-build-flags.md item 19"
  - "review/wiki-build-flags.md items 16, 58"
  - "notes/velocity-gated-gravity.md §4"
  - "verify/velocity_gated_gravity.py 'D. The obituary's scope'"
---

*The velocity dispersion σ of a galaxy, a [dark-matter halo](/wiki/dark-matter/halo-astrophysics) or a galaxy cluster is the spread of the velocities of its stars or particles about their mean: the standard deviation of their velocity distribution along one direction, quoted in km/s. It measures how hot a system is in the dynamical sense. For a system held together by its own gravity and in equilibrium, the dispersion is set by the mass and the size, which is how the dark matter of a [dwarf galaxy](/wiki/dark-matter/halo-astrophysics/dwarf-galaxies) is weighed from the speeds of its stars along the line of sight. The values used in the Comatter program's notes run from 3 km/s, for an [ultra-faint dwarf galaxy](/wiki/dark-matter/halo-astrophysics/dwarf-galaxies#ultra-faint-dwarfs-t), to 1000 km/s, for a galaxy cluster, and none of them is cited. In the program σ is the scale against which the [velocity gate](/wiki/dark-matter/conjugate-matter/velocity-gate) of [conjugate matter](/wiki/dark-matter/conjugate-matter) is measured: where σ is below the gate velocity v\*, as in dwarf galaxies, most pairs of dark-matter particles interact, and where it is above, as in the Milky Way and in clusters, only particles moving together do. σ also enters the [the clumping problem](/wiki/history/main-problems) calculation that killed [velocity clumping](/wiki/dark-matter/momentum-clumping/founding-image), the [occupation number](/wiki/dark-matter/wave-dark-matter/occupation-number) that divides particle from wave dark matter, and the power law (v\*/σ)⁴ of [row 3, the island discriminant](/wiki/predictions/island-discriminant). The quantity is standard physics; this page explains it and lists where the program uses it.*

**Status:** Established — [T] — standard stellar dynamics and kinetic theory, written here from general knowledge, with the literature it names marked † (Binney and Tremaine †; Simon and Geha 2007 †; Walker et al. 2009 †; Wolf et al. 2010 †; Simon 2019 †). The [clumping calc notes](/wiki/history/documents/clumping-notes) introduce σ as the dispersion of a Maxwellian, the thermal distribution of velocities, and give a value for each environment they consider, citing none; no `verify/` script checks those values, and of the numbers that depend on them only calc note #2's two shortfall ratios are reproduced, in section D of `verify/velocity_gated_gravity.py` ([the velocity-gated-gravity script](/wiki/method/verification/velocity-gated-gravity-script)). Flags 17, 19 and 58 in `review/wiki-build-flags.md`, on a convention for the gate, on the regime in which calc note #2 evaluates one result and on calc note #2's narrow-gate criterion, await Paul's ruling.

## What it is [T]

### The definition

The stars of a galaxy, or the particles of a dark-matter halo, move with velocities scattered about their mean, the velocity of the system as a whole. The velocity dispersion is the root-mean-square size of that scatter. Along one direction x,

```text
σ² = ⟨(vₓ − ⟨vₓ⟩)²⟩
```

where ⟨…⟩ is the average over the population. When the random motion is isotropic, the same in every direction, each direction has the same σ, and the mean square of the full random velocity is

```text
⟨|v − ⟨v⟩|²⟩ = 3σ²
```

Observers quote the one-dimensional dispersion along the line of sight, the only component a spectrum measures; some theoretical work quotes the three-dimensional value instead, so a value of σ needs its convention [T]. The clumping notes do not state one. On the wiki's reading their formulas use a one-dimensional σ: their density of co-movers, the particles inside one particle's velocity gate, n(v\*/σ)³/(2π)^{3/2}, contains the peak density in velocity space of a Maxwellian of one-dimensional dispersion σ ([the narrow-gate threshold](/wiki/dark-matter/momentum-clumping/instability-criterion#the-narrow-gate-threshold)).

### The Maxwellian and the dynamical temperature

A gas of particles of mass m in thermal equilibrium at temperature T has the Maxwell–Boltzmann distribution of velocities, which in terms of σ reads [T]

```text
f₀(v) ∝ exp(−v²/2σ²)        σ² = k_B T/m
```

with k_B Boltzmann's constant. Each component of the velocity is then Gaussian with standard deviation σ, and the momenta are spread over a range of order mσ.

A galaxy, or a halo of dark matter whose particles do not collide, is not a gas in thermal equilibrium, and its distribution need not be Maxwellian. σ² still plays the role of k_B T/m: a system with a large dispersion is called dynamically hot, one with a small dispersion cold [T]. Where collisions act, they drive the distribution toward the Maxwellian, whatever the dependence of the cross-section on speed ([the H-theorem](/wiki/dark-matter/momentum-clumping/vlasov-stability#collisions-and-the-h-theorem)).

[Calc note #2](/wiki/history/documents/clumping-notes), the first of the three clumping calc notes, takes the Maxwellian as the state of a halo. It linearizes "about a homogeneous Maxwellian f₀(p) of dispersion σ" (`notes/stream-stability.md`, 'Setup'; [the gated Vlasov model](/wiki/dark-matter/momentum-clumping/gated-vlasov-model#linear-response-an-eigenvalue-problem-on-momentum-space)), and it expects gated collisions to keep that state: "equilibrium is Maxwellian to one part in 10³⁰" ('Numbers at the scattering benchmark').

### A profile, not one number

σ varies with position in a system [T]. In a halo of collisionless cold dark matter, whose density keeps rising toward the center in a cusp, the dispersion is lowest near the center and rises outward through the inner halo ([what self-scattering does to a halo](/wiki/dark-matter/halo-astrophysics/self-interacting-dark-matter#what-self-scattering-does-to-a-halo-t)). If the dark matter scatters off itself, collisions carry heat down that gradient into the center, and the core they form has a nearly uniform dispersion, an isothermal core [T]. The dispersion can also differ between directions. A spherical system has a radial dispersion σ_r and a tangential one σ_t along each of the two tangential directions, and its anisotropy β ≡ 1 − σ_t²/σ_r² is zero for isotropic orbits, positive for orbits that are mostly radial and negative for mostly circular ones [T].

The program's notes describe each environment by one density and one dispersion, as in calc note #2's "Dwarf core (ρ ~ 1 GeV/cm³, σ ~ 30 km/s)" ('Numbers at the scattering benchmark'), without a profile or an anisotropy.

## Dispersion, mass and size [T]

### The virial theorem

A system held together by its own gravity, in a steady state, satisfies the virial theorem [T]:

```text
2K + W = 0
```

where K is the kinetic energy of its random motions and W its gravitational potential energy, which is negative. For a system of mass M and size R with isotropic dispersion σ, K = (3/2)Mσ², and W is of order −GM²/R, with G Newton's constant, so

```text
M ~ σ² R / G
```

with a coefficient of order one that depends on the density profile, on how R is defined and on the orbits [T]. The relation works in both directions. A deeper potential well holds faster random motions, so more massive systems have larger dispersions, from dwarf galaxies through large spirals to galaxy clusters; and a measured dispersion and size give a mass [T]. The page on [dwarf galaxies](/wiki/dark-matter/halo-astrophysics/dwarf-galaxies#what-dwarf-galaxies-are-t) uses the estimate in that second sense.

The dispersion also sets two scales of a system [T]. The dynamical time, the time an orbit takes to cross the system, is of order R/σ, and by the virial relation of order 1/√(Gρ) for a mean density ρ. The Jeans wavenumber k_J = √(4πGρ)/σ separates ripples in density that the random motion smooths out from longer ones that self-gravity makes grow into lumps ([the Jeans instability](/wiki/dark-matter/momentum-clumping/vlasov-stability#the-static-threshold-and-the-jeans-instability)).

### The Jeans equation

A more detailed estimate follows the dispersion with radius. For a spherical system in a steady state, a population of tracers, bodies whose motions are measured, with number density ν(r), radial dispersion σ_r(r) and anisotropy β obeys the spherical Jeans equation [T]:

```text
(1/ν) d(ν σ_r²)/dr + 2β σ_r²/r = −G M(r)/r²
```

where M(r) is the total mass inside radius r, dark matter included. The tracers need not carry the mass: the stars of a dwarf galaxy are a tracer population in a potential that its dark matter dominates (Binney and Tremaine †).

### Measuring σ in a dwarf galaxy

The spectrum of each member star gives its velocity along the line of sight through the Doppler shift. Subtracting the galaxy's mean velocity and allowing for the measurement errors leaves the spread, the line-of-sight dispersion [T]. It is one component of the motion, averaged through the depth of the galaxy, so a measured profile of it is consistent with different pairs of mass profile and anisotropy, the mass–anisotropy degeneracy. The mass inside about the half-light radius, the radius that holds half the light of the stars, depends little on the anisotropy, and it is the quantity such data fix best (Walker et al. 2009 †; Wolf et al. 2010 †). Dividing a mass by the light of the stars gives the mass-to-light ratio M/L, which in dwarf galaxies far exceeds what stars can supply ([what dwarf galaxies are](/wiki/dark-matter/halo-astrophysics/dwarf-galaxies#what-dwarf-galaxies-are-t)).

In the ultra-faint dwarfs, the faintest galaxies known, the dispersion is comparable to the measurement errors and to the orbital speeds of binary stars, whose motion adds to the measured spread. Their dispersions therefore rest on a model of the errors and on repeated spectra that identify the binaries (Simon and Geha 2007 †; Simon 2019 †).

### Stars and dark matter

A spectrograph measures the dispersion of the stars. The dark matter's own dispersion is not observed: it is inferred from a model in which both populations move in the same potential. In equilibrium that potential governs both, but the two dispersions need not be equal, since each also depends on its own density profile and orbits [T]. The formulas of the clumping notes need the dark matter's dispersion, the σ of its distribution f₀, and the notes do not say which kind of dispersion their environment values are. Calc note #4's value for [Segue 1](/wiki/dark-matter/halo-astrophysics/dwarf-galaxies#segue-1-the-test-case), "σ ≈ 3.7 km/s", stands beside a mass inside 38 pc and carries no citation (`notes/ufd-endpoint.md`, 'Sharpened input numbers').

## The spread of pair speeds [T]

Collisions, and any interaction between pairs, depend on the relative velocity of the two particles. For two particles drawn independently from a Maxwellian of one-dimensional dispersion σ, each component of the relative velocity is Gaussian with standard deviation √2σ [T]. The pairs of a halo therefore meet at speeds of order σ, spread over a range. A rate that depends on the speed of a collision, such as the scattering rate ρ(σ_T/m)v of [self-interacting dark matter](/wiki/dark-matter/halo-astrophysics/self-interacting-dark-matter), with σ_T the [transfer cross-section](/wiki/dark-matter/halo-astrophysics/transfer-cross-section), is an average over that spread, ρ⟨σ_T v⟩/m ([averaged over speeds](/wiki/dark-matter/halo-astrophysics/transfer-cross-section#averaged-over-speeds)). Through that average a halo's σ fixes the speeds at which it samples a cross-section that depends on speed.

The program states its regimes by comparing σ directly with the gate velocity v\*, which calc note #3 defines in relative velocity: "gate width v\* in relative velocity" (`notes/wave-island.md`, 'Setup'). The sources state no factor between a halo's dispersion and the collision speeds of its particles ([what the record leaves open](#what-the-record-leaves-open)).

## The values in the program's notes

The [clumping calc notes](/wiki/history/documents/clumping-notes) give one dispersion for each environment they consider:

| Environment | σ, as written | Where | Used for |
| --- | --- | --- | --- |
| Ultra-faint dwarf | 3 km/s | Calc note #3, environment table | [Scenario A](/wiki/dark-matter/momentum-clumping/wave-island/scenario-a)'s ratio R_X; replaced by Segue 1 |
| Segue 1 | σ ≈ 3.7 km/s | Calc note #4, 'Sharpened input numbers' | the test of Scenario A |
| Classical dwarf core | σ ~ 30 km/s; 30 km/s | Calc note #2, benchmark table; calc note #3, environment table | the stream criterion; Scenario A's normalization σ_d |
| Milky Way, inner 1 kpc | 120 km/s | Calc note #3, environment table | R_X |
| Milky Way halo near the Sun | σ ~ 155 km/s; 155 km/s | Calc note #2, benchmark table; calc note #3, environment table | the stream criterion; R_X |
| Galaxy cluster | 1000 km/s | Calc note #3, environment table | R_X |

Calc note #2 labels the Milky Way row near the Sun "MW halo, local" and calc note #3 "MW solar circle", MW being the Milky Way; calc note #3's inner row is "MW inner 1 kpc". Calc note #4 replaced calc note #3's ultra-faint-dwarf row with Segue 1's values ([the superseded row](/wiki/dark-matter/halo-astrophysics/dwarf-galaxies#superseded-calc-note-3s-ultra-faint-dwarf-row)). No source cites any of the values, and no `verify/` script checks them; like the program's other observational inputs, they are to be source-checked before external use ([what is unchecked in Scenario A](/wiki/dark-matter/momentum-clumping/wave-island/scenario-a#what-is-unchecked)).

For comparison, the gate velocity at the program's [scattering benchmark](/wiki/dark-matter/conjugate-matter/benchmark) is v\* = 120 km/s in calc note #2 ('Numbers at the scattering benchmark'), "v\* ≈ 120 km/s" in the [lab notebook](/wiki/history/documents/lab-notebook) (#1 §5.1) and "v\* ~ 10² km/s" in row 1 of [the checkpoint](/wiki/history/documents/checkpoint) (#11 §13). Calc note #2 assigns the classical dwarf core to the broad-gate "dwarf regime" and the Milky Way and clusters to the narrow-gate "MW/cluster regime" ('Limit 1 — broad gate', 'Limit 2 — narrow gate').

## How the program uses σ

The clumping notes describe each halo by its density ρ and its dispersion σ, and σ enters each of the results below.

### The gate's two regimes

[The velocity gate](/wiki/dark-matter/conjugate-matter/velocity-gate) lets two particles of conjugate matter χ interact only when their relative velocity is below about v\*. Whether that restriction matters in a halo depends on its dispersion:

- **Gate open, or broad** (σ ≲ v\*). Most pairs in the halo are inside the gate, which then drops out of the dynamics. Calc note #2 calls this the "dwarf regime".
- **Gate narrow** (σ > v\*). Only particles moving within about v\* of each other interact, the co-movers. Calc note #2 calls this the "MW/cluster regime", for the Milky Way and galaxy clusters.

Calc note #2 states the comparison in momentum, as the gate width μ against the spread of momenta mσ ("μ ≫ mσ; dwarf regime", "μ ≪ mσ; MW/cluster regime"); calc note #3 states it in velocity, "Gate-open (σ ≲ v\*)" ([gate open and gate narrow](/wiki/dark-matter/momentum-clumping/wave-island/condensation-rate#gate-open-and-gate-narrow)). The lab notebook relates the two widths as v\* ≡ √2μ/m_χ (#1 §5.1). A suspected factor of √2 between the sources' conventions for the gate is flag 17 in `review/wiki-build-flags.md`, which changes no stated number ([two conventions, not reconciled](/wiki/dark-matter/conjugate-matter/velocity-gate#two-conventions-not-reconciled)). The regime in between, σ comparable to v\*, is not solved: calc note #2 joins the two limits with min(σ, v\*) ([the unified criterion](/wiki/dark-matter/momentum-clumping/instability-criterion#the-unified-criterion)). The checkpoint's plain-language passage states the consequence for scattering: "self-interaction strong in cold dwarf galaxies, off in hot clusters" (#11 §8).

### Row 1: halos as a range of speeds

[Row 1](/wiki/predictions/self-interaction-knee) of [the predictions table](/wiki/predictions) requires a knee in the self-scattering cross-section, "σ_T(v) across halo masses", at "v\* ~ 10² km/s" (#11 §13). Because a halo's mass sets its dispersion, and its dispersion sets the speeds at which its particles collide, halos of different mass sample the cross-section at different speeds [T]. The lab notebook's core fit places the collisions of dwarf galaxies below the gate, "at v ≲ v\* ≈ 120 km/s" (#1 §5.1), and the row requires "zero cluster signal (particle χ)" in clusters, to which the notes give a dispersion of 1000 km/s. The notebook names the systems in between: "The discriminating band is v ~ 150–400 km/s (large spirals, small groups)" (#1 §5.1), a band in collision speed. No source converts a halo's σ into the collision speed v of the law σ_T(v) = σ₀F(v²/v\*²) (#11 §8; [the gated scattering law](/wiki/dark-matter/conjugate-matter/scattering-law)).

### The particle island: the stream criterion

[The clumping problem](/wiki/history/main-problems) asked whether the gated attraction makes a halo break up into streams of particles moving together. For classical particles the condition is the mean-field criterion, tagged [D] (#11 §9 (i); calc note #2, 'Limit 2 — narrow gate'):

```text
g · n_gate ≥ m · min(σ, v*)²        n_gate ≈ n (v*/σ)³/(2π)^{3/2}
```

with g the gated contact coupling, n the number density and m the particle mass. The right side is the kinetic energy of the random motion that the attraction has to overcome: mσ² with the gate open, and mv\*² with the gate narrow, where the spread inside the gate replaces σ. The co-mover density n_gate counts the particles inside one particle's gate; on the wiki's reading, its factor (v\*/σ)³ is the gate's share of the velocity space that a Maxwellian of dispersion σ fills ([the narrow-gate threshold](/wiki/dark-matter/momentum-clumping/instability-criterion#the-narrow-gate-threshold)). At the scattering benchmark calc note #2 evaluates the criterion for a "Dwarf core (ρ ~ 1 GeV/cm³, σ ~ 30 km/s)" and for the Milky Way's halo near the Sun, "ρ ~ 0.4, σ ~ 155 km/s", and finds ratios of the two sides of ~10⁻²⁸ and ~10⁻³¹ ([the mean-field criterion and its 10²⁸–10³¹ shortfall](/wiki/dark-matter/momentum-clumping/instability-criterion)). Since 2026-10-28 section D of `verify/velocity_gated_gravity.py` reproduces the two ratios, as 3.9×10⁻²⁸ and 2.9×10⁻³¹, from #2's inputs (flag 16, addendum; [verification record](/wiki/dark-matter/momentum-clumping/instability-criterion#verification-record)). The narrow-gate form is flagged: "Its substitution σ → v\* is the threshold of a cold stream that already exists, not of a smooth halo." Linearized, the halo's dispersion stays, g·n·Λ_g ≥ m·σ² with Λ_g the gate's top eigenvalue, and in the Milky Way #2's form overstates the shortfall about 3×; the verdict is unchanged (flag 58; `notes/velocity-gated-gravity.md` §4; [the narrow-gate form, flagged](/wiki/dark-matter/momentum-clumping/instability-criterion#the-narrow-gate-form-flagged)).

**The classicality theorem.** Holding the cross-section per unit mass S ≡ σ₀/m fixed, calc note #2 states that the criterion "scales as √(πS)ρ/(m^{5/2}σ²)" and sets it to 1, which gives m_crit = [√(πS)ρ/σ²]^{2/5} ≈ 10⁻¹³ GeV ~ 0.1 meV "for MW conditions" ('Corollary (the classicality theorem)'; [the classicality theorem and the particle island](/wiki/dark-matter/momentum-clumping/classicality-theorem)). That is the broad-gate form, with σ² in the denominator, evaluated at conditions that calc note #2's own table treats as narrow-gate. Flag 19 in `review/wiki-build-flags.md` records this, finds the conclusion unchanged and awaits Paul's ruling ([scope](/wiki/dark-matter/momentum-clumping/classicality-theorem#scope)).

### The wave island: occupation and condensation

**The occupation number.** At the masses where the criterion could be met, each quantum state of the halo holds many quanta: N_occ = ρ/(m⁴σ³) in the notes' natural units, "~ 10²⁰" at m_crit (calc note #2, 'Corollary (the classicality theorem)'; [the occupation number](/wiki/dark-matter/wave-dark-matter/occupation-number)). σ enters through the de Broglie wavelength λ_dB = 1/(mσ). The relation is the Fourier one between a waveform and its spectrum: a halo whose momenta are spread over mσ is coherent over a length of order 1/(mσ), so a colder halo has longer waves, and at the same density and mass more quanta share each cell of phase space [T]. Calc note #3 also writes a peak occupation, (2π)^{3/2}ρ/(m⁴σ³), and does not reconcile the two forms ([two normalizations in calc note #3](/wiki/dark-matter/wave-dark-matter/occupation-number#two-normalizations-in-calc-note-3)).

**The condensation rate.** On the [wave island](/wiki/dark-matter/momentum-clumping/wave-island), the range of χ masses so light that a halo behaves as a classical wave field, calc note #3 computes a gated condensation rate: the rate at which the halo's waves, scattering off one another, collect their power in a narrow range of relative momenta. Tagged [D, heuristic coefficients], it contains the dispersion twice, once through the gate and once through the halo:

```text
Γ_self ≈ c g²ρ² min(σ, v*)⁴ / (m³σ⁶),      c = O(5–15)
```

With the gate open the rate is "Γ ≈ c g²ρ²/(m³σ²)"; with the gate narrow it is "suppressed by (v\*/σ)⁴ — a power law, not an exponential" (calc note #3, 'The rate'; [the gated condensation rate Γ_self](/wiki/dark-matter/momentum-clumping/wave-island/condensation-rate)). The gravitational channel beside it, Γ_gr ≈ 8πG²ρ²Λ/(m³σ⁶), which calc note #3 tags [T: LPT], LPT being Levkov–Panin–Tkachev, and in which the note does not define Λ, falls as σ⁻⁶ at every dispersion ([the gravitational rate](/wiki/dark-matter/wave-dark-matter/wave-kinetics#the-gravitational-rate)).

**Scenario A.** If the gated channel also made the cores of classical dwarfs ([Scenario A](/wiki/dark-matter/momentum-clumping/wave-island/scenario-a), now dead), fitting them would fix the coupling. Calc note #3's ratio of the condensation rate to the orbital stirring rate in an environment X then follows with g²/m³ eliminated ('What pins g? Two scenarios'):

```text
R_X = κ (t_dyn,X/t_age) (ρ_X/ρ_d)² (σ_d/σ_X)² (min(σ_X, v*)/σ_X)⁴
```

Here ρ_d and σ_d are the density and dispersion of the classical dwarf core that normalizes the fit, which calc note #3's table enters as (1, 30) in GeV/cm³ and km/s; κ ~ 1 is the normalization of the core fit, t_age the age of the halo and t_dyn,X the dynamical time of the environment. Calc note #3's verdict names the leverage: "streams lose everywhere by 10²–10⁴ — except ultra-faint dwarfs, where ρ²/σ² leverage wins by ~40". Calc note #4 reran the ratio with Segue 1's "σ ≈ 3.7 km/s" and found "≈ 10⁻³ · 10⁴ · 66 ≈ 660"; on the wiki's reading, the factor 66 is the squared dispersion ratio (σ_d/σ)² ([Segue 1 and the condensation time](/wiki/dark-matter/momentum-clumping/wave-island/scenario-a#segue-1-and-the-condensation-time)). Its robustness check turns on the same dependence: "shrinking v\* makes it worse (σ⁻⁶ leverage boosts R to ~10⁵)" ('The data'). Segue 1's dense, intact halo falsified the scenario ([Obituary: Scenario A and the ultra-faint-dwarf endpoint](/wiki/dark-matter/momentum-clumping/wave-island/scenario-a)).

**Scenario B.** If the coupling is left free ([Scenario B](/wiki/dark-matter/momentum-clumping/wave-island/scenario-b), alive and quarantined), calc note #3 states the condition for streams through calc note #2's mean-field parameter X ≡ gn/(mσ²), the attraction energy of a particle divided by the kinetic energy of its random motion. X has to stay below 1, "so halos aren't modulationally unstable", that is, so that small ripples in a uniform halo do not grow on their own; streams need X ≥ √(Ωσ²/(c m v\*⁴)), with Ω = 1/t_dyn the stirring rate ([the mean-field parameter X](/wiki/dark-matter/momentum-clumping/wave-island/scenario-b#the-mean-field-parameter-x)).

### Row 3: the island discriminant

[Row 3](/wiki/predictions/island-discriminant) reads the shape of the knee's tail: "Knee tail: sharp ⇒ particle; (v\*/σ)⁴ ⇒ wave" (#11 §13). The wave law is the narrow-gate suppression of Γ_self and is written in the halo's dispersion; the particle law, e^{−v²/v\*²} for a Gaussian gate, is written in the collision speed v (calc note #3, 'The rate'). The sources do not convert one variable into the other ([caveats and open questions](/wiki/predictions/island-discriminant#caveats-and-open-questions)). Calc note #2's earlier estimate of the wave law, "(v\*/σ)³ suppression", is superseded by calc note #3's fourth power ([the cubic suppression of calc note #2](/wiki/dark-matter/momentum-clumping/wave-island/condensation-rate#superseded-the-cubic-suppression-of-calc-note-2)).

### The founding image

Before the clumping problem, the lab notebook expected the gated attraction to make the core of a halo condense in velocity "below a critical velocity dispersion" (#1 §5.2). In its analogy with the Bardeen–Cooper–Schrieffer theory of superconductivity, the dispersion took the place of the temperature below which electrons pair [T]. The clumping problem killed the picture. For particles the stream criterion falls short by 28–31 orders of magnitude at the benchmark, and on the wave island condensation is mandatory only under [Scenario A](/wiki/dark-matter/momentum-clumping/wave-island/scenario-a), which the ultra-faint dwarfs falsified ([Obituary: velocity clumping, the founding image](/wiki/dark-matter/momentum-clumping/founding-image); [the net theorem](/wiki/dark-matter/momentum-clumping/net-theorem)).

## What the record leaves open

- **Which dispersion.** The clumping notes do not state whether σ is one-dimensional or three-dimensional, or whether their values are dispersions of stars or of dark matter. Their formulas need the dark matter's, and on the wiki's reading they use a one-dimensional σ.
- **Citations.** No source cites any of the environment values, and no `verify/` script checks them ([the iron rule](/wiki/method/verification/iron-rule)).
- **From σ to a collision speed.** The sources compare σ with v\* directly and write the particle law in the collision speed v, without a factor between the two. For a Maxwellian, each component of a pair's relative velocity has the dispersion √2σ [T] ([the spread of pair speeds](#the-spread-of-pair-speeds-t)).
- **The regime between the limits.** For σ comparable to v\*, the mean-field problem is bracketed by the two limits, not solved ([what the bracket provides](/wiki/dark-matter/momentum-clumping/gated-vlasov-model#what-the-bracket-provides)).
- **Three rulings.** Flag 17, the √2 between the gate conventions, flag 19, the regime of the classicality corollary, and flag 58, calc note #2's substitution σ → v\* in the narrow-gate criterion, await Paul's ruling ([pending rulings](/wiki/status/open-problems#pending-rulings)).

## Symbol collisions

- σ on this page is a velocity dispersion. σ_d and σ_X are its values in the classical dwarf core and in an environment X (calc note #3), and σ_r and σ_t its radial and tangential parts.
- σ_T is the transfer cross-section, σ₀ its value below the gate, and σ_scat a generic scattering cross-section (calc note #3).
- R is a size on this page; R_X in [Scenario A](/wiki/dark-matter/momentum-clumping/wave-island/scenario-a) is a ratio of rates.
- X in R_X labels an environment, and X ≡ gn/(mσ²) is Scenario B's mean-field parameter; neither is the [momentum graviton X](/wiki/gravity/momentum-graviton).
- The other meanings of σ are listed on [notation](/wiki/notation#letters-with-several-meanings).

## References

The program's documents cite no source for the velocity dispersion or for the methods that measure it. Added by the wiki from model memory (†):

- J. Binney, S. Tremaine, *Galactic Dynamics* (Princeton University Press)†: the virial theorem, the Jeans equations and the dispersions of stellar systems.
- J. D. Simon, M. Geha, "The kinematics of the ultra-faint Milky Way satellites: solving the missing satellite problem," Astrophys. J. (2007)†: line-of-sight dispersions of ultra-faint dwarfs.
- M. G. Walker et al., "A universal mass profile for dwarf spheroidal galaxies?," Astrophys. J. (2009)†: dwarf masses within the half-light radius from line-of-sight dispersions.
- J. Wolf et al., "Accurate masses for dispersion-supported galaxies," Mon. Not. R. Astron. Soc. (2010)†: the mass inside the half-light radius, nearly independent of the anisotropy.
- J. D. Simon, "The faintest galaxies," Annu. Rev. Astron. Astrophys. (2019)†: a review of the ultra-faint dwarfs, including measurement errors and binary stars in their dispersions.

## Used by

- [The gated Vlasov model](/wiki/dark-matter/momentum-clumping/gated-vlasov-model) — the Maxwellian of dispersion σ about which calc note #2 linearizes; the gate width μ against the spread mσ.
- [The mean-field criterion and its 10²⁸–10³¹ shortfall](/wiki/dark-matter/momentum-clumping/instability-criterion) — g·n_gate ≥ m·min(σ, v\*)², evaluated at σ ~ 30 and σ ~ 155 km/s.
- [The classicality theorem and the particle island](/wiki/dark-matter/momentum-clumping/classicality-theorem) — m_crit and N_occ depend on the halo's ρ and σ.
- [The gated condensation rate Γ_self](/wiki/dark-matter/momentum-clumping/wave-island/condensation-rate) — min(σ, v\*)⁴/σ⁶, with the gate open or narrow.
- [Obituary: Scenario A and the ultra-faint-dwarf endpoint](/wiki/dark-matter/momentum-clumping/wave-island/scenario-a) — the dispersion ratio (σ_d/σ_X)² and Segue 1's σ ≈ 3.7 km/s.
- [Scenario B: tunable streams (quarantined)](/wiki/dark-matter/momentum-clumping/wave-island/scenario-b) — the mean-field parameter X ≡ gn/(mσ²).
- [Row 1: the knee in σ_T(v)](/wiki/predictions/self-interaction-knee) — halos of different dispersion sample σ_T at different speeds.
- [Row 3: the island discriminant](/wiki/predictions/island-discriminant) — the wave law (v\*/σ)⁴.
- [Obituary: velocity clumping, the founding image](/wiki/dark-matter/momentum-clumping/founding-image) — condensation "below a critical velocity dispersion".

## Sources

- `papers/broken-born-checkpoint-v2.md` §8 — "self-interaction strong in cold dwarf galaxies, off in hot clusters"; the law σ_T(v) = σ₀F(v²/v\*²); §9 (i) — the mean-field criterion g·n_gate ≥ m·min(σ,v\*)² and its tag [D]; §13 rows 1 and 3 — "σ_T(v) across halo masses", the knee at v\* ~ 10² km/s and the wave law (v\*/σ)⁴
- `notes/stream-stability.md` 'Setup' — the Maxwellian of dispersion σ; 'Limit 1 — broad gate' and 'Limit 2 — narrow gate' — μ against mσ, the dwarf and Milky Way–cluster regimes, n_gate and the unified criterion; 'Numbers at the scattering benchmark' — the dwarf-core and Milky Way dispersions, v\* = 120 km/s, the ratios and the Maxwellian equilibrium; 'Corollary (the classicality theorem)' — m_crit and N_occ = ρ/(m⁴σ³); 'Consequences for the predictions table' — the (v\*/σ)³ estimate
- `notes/wave-island.md` 'Setup' — "gate width v\* in relative velocity"; 'The rate' — Γ_self, gate open and gate narrow, the island discriminant, the gravitational rate; 'What pins g? Two scenarios' — the environment table, R_X with σ_d, the "ρ²/σ² leverage" and X ≡ gn/(mσ²)
- `notes/ufd-endpoint.md` 'Sharpened input numbers' — Segue 1's σ ≈ 3.7 km/s and the ratio of about 660; 'The data' — the "σ⁻⁶ leverage"
- `notes/broken-born-theory.md` §5.1 — v\* ≈ 120 km/s, v\* ≡ √2μ/m_χ and the 150–400 km/s band; §5.2 — "below a critical velocity dispersion"
- `review/wiki-build-flags.md` item 17 — the suspected √2 between the gate conventions; item 19 — the regime of the classicality corollary; item 58 — calc note #2's narrow-gate criterion; item 16, addendum — the shortfall now gated; all awaiting rulings
- `notes/velocity-gated-gravity.md` §4 — the narrow-gate criterion linearized, with the halo's dispersion
- `verify/velocity_gated_gravity.py` section D — calc note #2's shortfall ratios from the dwarf-core and Milky Way dispersions
