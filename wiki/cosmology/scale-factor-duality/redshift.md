---
title: "Redshift"
weight: 15
status: established
description: "1 + z = a₀/a_e: the expansion stretches every wavelength by the ratio of scale factors and lowers the momentum of every free particle as 1/a. The derivation and its conditions, redshift as a clock and a distance, other shifts, and the program's uses: w(z) and DESI DR2's crossing above z ≃ 0.4 (flag 43 on the crossing redshift), temperatures and gravitational-wave frequencies falling as 1/a, and #12's reading of redshift as a contracting momentum spectrum."
provenance: [T]
sources:
  - "papers/broken-born-checkpoint-v2.md §10"
  - "papers/broken-born-checkpoint-v2.md §13 row 4"
  - "CLAUDE.md 'Since the handoff'"
  - "review/round3-adjudication.md 'Rulings' 5"
  - "review/wiki-build-flags.md item 43"
  - "review/round3/referee/audit-notes.md Step 4(c) item 5"
  - "review/round3/referee/step4.py section 4"
  - "review/round3/referee/step2a.py 'peak frequency'"
  - "verify/soliton_obituary.py 'Dark radiation (ruling 5)'"
  - "notes/knot-dark-matter-standalone.md §4"
  - "popsci/universes-other-half.md 'Dark energy as the orientation of the split'"
---

*Redshift is the stretching of the wavelength of light between its emission and its observation. In cosmology it is written z and measures how much the universe expanded while the light was travelling: 1 + z = a₀/a_e, the [scale factor](/wiki/cosmology/scale-factor-duality/friedmann-cosmology) when the light arrives divided by the scale factor when it left, the scale factor being the number that multiplies the distances between distant galaxies. Every wavelength in a spectrum stretches by the same factor, the momentum of every freely moving particle falls in inverse proportion to the scale factor, and the frequency of [gravitational waves](/wiki/cosmology/early-universe/phase-transition-gravitational-waves) and the temperature of freely travelling radiation fall with it; in wave terms, stretching a waveform compresses its spectrum by the same factor. Because the scale factor has grown throughout the history of the universe, a measured redshift dates the emission, and surveys report the expansion history as a function of z, including the [equation of state](/wiki/cosmology/dark-energy/quintessence) w of dark energy, its pressure divided by its energy density. The program meets redshift there. The second data release of the [Dark Energy Spectroscopic Instrument](/wiki/cosmology/dark-energy/desi) (DESI) favours a w that lies below −1 at redshifts above about 0.4 and above −1 since; the program requires that [w never fall below −1](/wiki/cosmology/dark-energy/no-phantom-bound), so its dark-energy sector is under real pressure. The [popular article](/wiki/history/documents/popular-articles) #12 reads the redshift as the momentum spectrum of the universe contracting, which the wiki takes as a plain-language gloss on the program's constraint [a·ã = 1](/wiki/cosmology/scale-factor-duality/cosmological-constraint); the technical documents do not discuss the connection.*

**Status:** Established — [T] — textbook cosmology, written here from general knowledge, with the literature it names marked †. No `verify/` script tests the relation itself; `verify/soliton_obituary.py` codes the standard formula for a redshifted gravitational-wave frequency in one of its checks ([the soliton-obituary script](/wiki/method/verification/soliton-obituary-script)). The program states no result of its own about redshift. It uses z as the coordinate of the finding of DESI's Data Release 2 (DR2), a crossing "above redshifts z ≃ 0.4" [21S] ([#11](/wiki/history/documents/checkpoint) §10, §13 row 4), and the [round-3 review](/wiki/method/review/round-3) used the redshift of temperatures and frequencies in its checks. #12's reading of redshift in momentum variables is explanation, not a source for status.

## What redshift is [T]

Light from a distant galaxy arrives with its spectral lines at longer wavelengths than the same lines have in a laboratory. With λ_e a wavelength at emission and λ₀ the same wavelength as observed, the redshift z is defined by

```text
z = (λ₀ − λ_e) / λ_e          1 + z = λ₀ / λ_e
```

In a universe that is the same at every place and in every direction, whose geometry reduces to the scale factor a(t) ([Friedmann cosmology and minisuperspace](/wiki/cosmology/scale-factor-duality/friedmann-cosmology)), the stretching has a single cause, the growth of a while the light travels:

```text
1 + z = a₀ / a_e
```

where a_e is the scale factor at emission and a₀ its value at observation. With the usual normalization a₀ = 1 today this reads 1 + z = 1/a: z = 0 for light emitted now, and z grows without limit as a approaches 0.

The factor is the same at every wavelength, so the whole spectrum is rescaled and the pattern of an element's lines is kept. Identifying the pattern in an observed spectrum gives z. This is how a spectroscopic survey such as DESI measures the redshifts of galaxies and quasars ([DESI baryon acoustic oscillations](/wiki/cosmology/dark-energy/desi#the-survey-t)).

## Why wavelengths stretch [T]

### Successive crests

Written with cosmic time t (the [lapse](/wiki/cosmology/scale-factor-duality/friedmann-cosmology#the-homogeneous-universe-t) set to 1) and with the speed of light c shown, the metric of a flat homogeneous universe is ds² = −c²dt² + a(t)²dx², where x are comoving coordinates, labels that stay attached to galaxies moving with the expansion. Light travels on paths with ds = 0, so along a ray the comoving distance grows as dχ = c dt/a. The comoving distance χ between an emitter and an observer, both at rest in comoving coordinates, is fixed:

```text
χ = ∫ c dt / a(t)          (from t_e to t₀)
```

A crest emitted at t_e arrives at t₀. The next crest, emitted one period δt_e later, arrives δt₀ later and covers the same χ. Over one period a hardly changes, so subtracting the two integrals gives

```text
δt₀ / a₀ = δt_e / a_e
```

Periods grow in proportion to a, and with them wavelengths, λ = c·δt. That is 1 + z = a₀/a_e [T]. The argument holds in a curved universe too, with χ measured along the ray.

**Conditions.** The derivation uses only the form of the metric, not the Friedmann equation. Whatever sets the expansion rate, whether matter, radiation, dark energy or a change in the law of gravity, changes how a, and so z, depends on time, but not how z depends on a. The derivation also treats the wave as short: its period must be brief compared with the time over which a changes, the limit of geometric optics. For light from galaxies this holds by a wide margin. For gravitational waves from the early universe it holds once a wave is shorter than the Hubble length c/H; a longer wave does not yet oscillate, and its energy begins to fall like that of radiation only after the Hubble length has grown past it ([primordial backgrounds](/wiki/cosmology/early-universe/phase-transition-gravitational-waves#primordial-backgrounds-t)).

### Time dilation

The same relation stretches every interval between events at the source. A process that lasts δt_e there, such as the brightening and fading of a supernova, is seen to last (1 + z)·δt_e [T].

### The momentum of free particles

A photon of wavelength λ has momentum p = h/λ, with h Planck's constant, so the stretching of its wavelength is a fall of its momentum as 1/a. The same holds for any freely moving particle, with or without mass [T]. Momentum here is the physical momentum, the one measured by an observer at rest in comoving coordinates.

The short argument: a particle moving at speed v relative to these observers covers the distance v·dt in a time dt and reaches a comoving observer who recedes from the first at speed H·v·dt, where H = ȧ/a is the [Hubble rate](/wiki/cosmology/scale-factor-duality/friedmann-cosmology#the-homogeneous-universe-t). Measured by that observer, the particle's momentum is lower by the effect of the boost, (E/c²)·H·v·dt, with E the particle's energy. Since p = Ev/c² for any particle,

```text
dp = −(E/c²) · H v dt = −p H dt          so  p ∝ 1/a
```

Equivalently, the comoving momentum a·p is constant. (On this page H is always the Hubble rate, not the program's phase-space metric H of [Born geometry](/wiki/phase-space/born-geometry/born-structures).)

Two consequences follow. A slow particle's peculiar velocity, its velocity relative to the comoving observers, decays as 1/a when no force acts on it. And a particle that starts out relativistic becomes non-relativistic once its momentum has fallen well below its mass times c.

### Phase space and temperature

[Phase space](/wiki/phase-space) is the space of positions and momenta taken together. For a gas of free particles the momentum spread falls as 1/a in each direction while the physical size of a comoving region grows as a in each direction, so the gas keeps its phase-space volume and the number of particles per phase-space cell is carried along unchanged: [Liouville's theorem](/wiki/phase-space/reciprocity/symplectic-form#the-symplectic-group) applied to the expansion [T].

A thermal spectrum of massless particles therefore keeps its shape. Every momentum falls by the same factor, so a blackbody spectrum at temperature T_e, when the scale factor is a_e, is still a blackbody spectrum when the scale factor is a, at the lower temperature T_e·a_e/a. Radiation that travels freely stays thermal with T ∝ 1/a, which with a₀ = 1 reads T = T₀(1 + z), T₀ being the temperature today [T]. This is why the [cosmic microwave background](/wiki/cosmology/early-universe/cosmic-microwave-background#a-blackbody-spectrum) is still a blackbody. Radiation that stays in equilibrium with the plasma also cools as 1/a, except while a species is annihilating and passing its entropy to the particles that remain ([the radiation era](/wiki/cosmology/early-universe/radiation-era#entropy-and-the-yield-y--ns-t)).

For the energy density, the redshift supplies the factor that separates radiation from matter. The number of quanta per unit volume falls as a⁻³ and each quantum's energy falls as 1/a, so radiation thins as a⁻⁴ while cold matter thins as a⁻³ ([fluids and how they thin](/wiki/cosmology/scale-factor-duality/friedmann-cosmology#fluids-and-how-they-thin-t)).

### Waveform and spectrum

In Fourier terms the redshift is an instance of the scaling property of the [Fourier transform](/wiki/phase-space/reciprocity/fourier-transform#waveform-and-spectrum): stretching a waveform by a factor s compresses its spectrum by the same factor,

```text
f(x) → f(x/s)          f̂(k) → s · f̂(s k)
```

A pulse of light that crosses an expanding universe is stretched along its direction of travel by 1 + z, and its spectrum of wavenumbers is compressed by 1 + z. For a quantum particle the momentum is p = ℏk, so the compression of wavenumbers is the fall of momentum. The product of the pulse's length and its spread in wavenumber does not change, so the expansion leaves the pulse's [time–bandwidth product](/wiki/phase-space/reciprocity/fourier-transform#the-timebandwidth-product) as it was.

## Redshift as a clock and a distance [T]

Because a has grown steadily, z labels the epoch at which light was emitted: low redshift is the recent past and high redshift the early universe. Turning z into a time or a distance needs the expansion history H(z). From 1 + z = 1/a,

```text
dz/dt = −(1 + z) H(z)

D_M(z) = c ∫ dz′ / H(z′)          (from 0 to z; spatially flat universe)
```

where D_M is the transverse comoving distance, which in a flat universe equals the comoving distance to the source and is the quantity a survey's ruler measures across the line of sight ([from the ruler to distances](/wiki/cosmology/dark-energy/desi#from-the-ruler-to-distances-t)). Along the line of sight, a small redshift interval Δz spans the comoving distance c·Δz/H(z), which is how a survey measures H(z) itself.

The expansion rate comes from the [Friedmann equation](/wiki/cosmology/scale-factor-duality/friedmann-cosmology#minisuperspace-gravity-reduced-to-at-and-nt-t), in which each kind of content enters as a power of 1 + z: cold matter as (1 + z)³, radiation as (1 + z)⁴, a cosmological constant as (1 + z)⁰, and a fluid of constant equation of state w as (1 + z)^{3(1+w)}. The round-3 referee's script codes it for radiation and matter as H(z) = H₀√(Ω_r(1 + z)⁴ + Ω_m(1 + z)³), with H₀ the Hubble rate today and Ω_r and Ω_m the present densities of radiation and matter as fractions of the critical density, the total density of a spatially flat universe (`review/round3/referee/step4.py`, section 4). The dark-energy density enters H(z) through its equation of state w(z) ([expansion and the Friedmann equation](/wiki/cosmology/dark-energy/quintessence#expansion-and-the-friedmann-equation-t)), and distances are integrals over H(z), so w(z) is inferred from distances by fitting a model, not read off them ([from distances to w(z)](/wiki/cosmology/dark-energy/desi#from-distances-to-wz-t)).

**Hubble's law.** For z much smaller than 1 the distance integral reduces to D ≈ cz/H₀: distance proportional to redshift, the relation Lemaître (1927 †) derived from an expanding solution and Hubble (1929 †) found in the data. The product cz is often quoted as a recession velocity. At low redshift the cosmological redshift matches a Doppler shift with velocity v = cz; in general it is the ratio of scale factors, and cz is not a velocity: it exceeds c whenever z > 1.

## Other shifts [T]

The redshift observed for a single object combines the cosmological factor with two others, each multiplying 1 + z:

- **Doppler shifts** from peculiar motion, the velocities of the source and the observer relative to the comoving observers: 1 + z_obs = (1 + z_cos)(1 + z_pec), with z_cos the cosmological part and z_pec the Doppler part [T].
- **Gravitational redshift** from a difference in gravitational potential. Light that climbs out of a potential well loses frequency: in a weak static field the fractional shift is −ΔΦ/c², with ΔΦ the rise in potential ([the equivalence principle](/wiki/gravity/spin-2-fields/equivalence-principle#rindler-frames)). In the cosmic microwave background the same effect, for photons leaving the potential wells present at last scattering, is part of the temperature pattern ([where the anisotropies come from](/wiki/cosmology/early-universe/cosmic-microwave-background#where-they-come-from)).

These corrections differ from object to object. The cosmological factor is the same for all light emitted at one epoch and received today.

## How the program uses redshift

The technical documents state no result about redshift itself. They use z as a coordinate, chiefly for the dark-energy data, and the [round-3](/wiki/method/review/round-3) review used the redshift of temperatures and frequencies in its checks.

### The time coordinate of the dark-energy data

- **w(z) and w(a).** Surveys give the dark-energy equation of state as a function of redshift, w(z). The [Chevallier–Polarski–Linder (CPL) form](/wiki/cosmology/dark-energy/cpl-parametrization) and the program's [thawing](/wiki/cosmology/dark-energy/thawing-and-freezing) requirement are written in the scale factor, w(a). With a₀ = 1 the two describe one function in two variables related by a = 1/(1 + z): the CPL line w(a) = w₀ + wₐ(1 − a) reads w(z) = w₀ + wₐ·z/(1 + z) ([in redshift](/wiki/cosmology/dark-energy/cpl-parametrization#in-redshift)). Row 4 of #11's predictions table names its observable "Dark energy w(z)" (#11 §13; [row 4](/wiki/predictions/dark-energy-drift)).
- **DR2's crossing.** #11 §10 quotes the paper of DR2: in every dataset combination "the favored w(z) shows a phase of w > −1 at low redshifts and a phantom crossing to w < −1 above redshifts z ≃ 0.4" [21S]. Read as a history, the favoured w was below −1 at the epochs above z ≃ 0.4 and has been above −1 since. The program's requirement, w ≥ −1 at all times, excludes the earlier phase ([the no-phantom bound w ≥ −1](/wiki/cosmology/dark-energy/no-phantom-bound); [the phantom divide](/wiki/cosmology/dark-energy/phantom-divide)). #11 §13 row 4 carries the finding in its kill-condition column, "DR2 already favors a crossing above z ≈ 0.4 (§10)", and the root `CLAUDE.md` states the position: "DESI DR2 favors a phantom crossing above z ≈ 0.4, against the framework's strict w ≥ −1 (§10). The dark-energy sector is under real pressure ahead of DR3" ('Since the handoff'), DR3 being DESI's Data Release 3. Both write ≈ where #11's quotation of DR2 writes ≃. The record of the finding is [DESI DR2's phantom crossing](/wiki/cosmology/dark-energy/desi-dr2-phantom-crossing).
- **Inferred, not observed.** w enters the measured distances only through H(z). One of the two points on which #11 §10 says the framework survives is that "w(z) is inferred from distances rather than observed, as [21S] also notes" ([DESI baryon acoustic oscillations](/wiki/cosmology/dark-energy/desi)).
- **The crossing redshift (flag 43).** A CPL line that is not the constant −1 crosses −1 at most once, at a scale factor a_c and so at one redshift ([a phantom crossing in the w₀–wₐ plane](/wiki/cosmology/dark-energy/cpl-parametrization#a-phantom-crossing-in-the-wwₐ-plane-t)). Flag 43 in `review/wiki-build-flags.md` compares the crossing of the program's [thawing corridor](/wiki/cosmology/dark-energy/cpl-parametrization#thawing-models-in-the-wwₐ-plane), wₐ ≈ −1.5(1 + w₀) (#11 §10), with DR2's: "The corridor's line crosses at z = 2 for every w₀; DR2's fits cross at z ≈ 0.35–0.50". The corridor and DR2's fits both lie in the region w₀ > −1, w₀ + wₐ < −1 of the w₀–wₐ plane, which the flag calls a quadrant, and the flag concludes that the pressure on the program "rests on the crossing redshift (DR2 calls the preference 'rather independent of parametrization choices'), not on the quadrant". The flag awaits Paul's ruling ([the corridor and DR2's crossing](/wiki/cosmology/dark-energy/cpl-parametrization#the-corridor-and-dr2s-crossing); [pending rulings](/wiki/status/open-problems#pending-rulings)).

### Temperatures and frequencies in the early universe

**Temperature as the clock.** Early-universe physics usually labels epochs by the temperature of the radiation, which falls as 1/a apart from the steps at annihilations ([the radiation era](/wiki/cosmology/early-universe/radiation-era)). A hidden sector that has decoupled from ours keeps its own temperature. Once its radiation and ours both travel freely, both temperatures fall as 1/a and their ratio stays fixed ([a hidden sector at its own temperature](/wiki/cosmology/early-universe/hidden-sector-temperature#how-the-two-temperatures-evolve-t)).

**Gravitational waves.** Waves from a phase transition at temperature T\* travel freely afterwards, and their frequency falls as 1/a, so the peak frequency today is the emitted one times the ratio of scale factors, f₀ = f\*·a\*/a₀ ([redshifting the peak to today](/wiki/cosmology/early-universe/phase-transition-gravitational-waves#redshifting-the-peak-to-today-t)). Entropy conservation turns that ratio into temperatures, and both the round-3 referee's script (`review/round3/referee/step2a.py`) and `verify/soliton_obituary.py` code the standard result:

```text
f₀ = 1.65×10⁻⁵ Hz × (f*/H*) × (T*/100 GeV) × (g*/100)^{1/6}
```

Here f\*/H\* is the emitted peak frequency in units of the Hubble rate at the transition, and g\* is the number of relativistic degrees of freedom. The retired [soliton dark-matter candidate](/wiki/dark-matter/candidates/soliton-candidate/obituary) predicted a band of such waves if its hidden transition was first order (`notes/knot-dark-matter-standalone.md` §4). [The gate](/wiki/method/verification/the-gate) checks the band's upper end, 3.2×10⁷ Hz after round-3 ruling 5, which `verify/soliton_obituary.py` reproduces as `3.17e+07`. The band died with the candidate ([the gravitational-wave band](/wiki/dark-matter/candidates/soliton-candidate/hidden-thermal-history#the-gravitational-wave-band-died-with-the-candidate)).

**Decoupling dates in round 3.** The round-3 referee dated by redshift the end of the coupling between the withdrawn manuscript's hidden fermion ψ and its hidden photons: "psi kinetically coupled to the gamma' bath until z = 2.7e3 (30 MeV), 7.0e4 (0.3 GeV), 2.2e6 (3 GeV), 6.9e7 (30 GeV) for Delta N = 0.286 (step4.out)", the masses in parentheses being ψ's, and "For sub-GeV psi this approaches recombination" (`review/round3/referee/audit-notes.md` Step 4(c) item 5; [dark acoustic oscillations](/wiki/method/review/round-3/rulings#dark-acoustic-oscillations)). Recombination is the epoch at which electrons and nuclei formed neutral atoms and the cosmic microwave background was released, at the redshift z\* of [last scattering](/wiki/cosmology/early-universe/cosmic-microwave-background#last-scattering). The script takes the hidden photons' temperature at redshift z as today's value times 1 + z, and the expansion rate as the H(z) above (`review/round3/referee/step4.py`, section 4).

**The Lyman-α forest.** Each cloud of neutral hydrogen between a quasar and the observer absorbs at the Lyman-α wavelength stretched by the cloud's own 1 + z, so position in the quasar's spectrum maps to distance along the line of sight. The bounds on fuzzy dark matter read the small-scale distribution of matter from that map ([bounds from the Lyman-α forest](/wiki/dark-matter/wave-dark-matter/fuzzy-dark-matter-bounds#bounds-from-the-lyman-α-forest-t)).

### The momentum description: #12's reading

Standard cosmology contains a reciprocal scaling of its own: for every free particle the product a·p of the scale factor and the physical momentum is constant, and a free gas keeps its phase-space volume (above). The program's [cosmological constraint a·ã = 1](/wiki/cosmology/scale-factor-duality/cosmological-constraint) has the same reciprocal form for two scale factors: a multiplies position-space distances, and ã multiplies momentum-space distances in the momentum-space description of the same state, the [conjugate universe](/wiki/program/conjugate-universe). The constraint is derived from the rigidity of the [symplectic form](/wiki/phase-space/reciprocity/symplectic-form) ω, which fixes the volume of a comoving phase-space cell. #11 §10 states it as "ω-rigidity fixes the comoving phase-space cell: a·ã = 1 (ℏ does not run)", tagged [D].

The popular article #12 connects the two in plain language:

> Cosmic expansion stretches every wavelength — the redshift — which, read in the momentum description, means every momentum in the universe is shrinking: the spectrum of the cosmos has been contracting since the beginning. That is not a second process running alongside expansion; it is expansion, read in the other variable.

(#12, 'Dark energy as the orientation of the split'.) #12 does not name the constraint there; the wiki reads the passage as its gloss on a·ã = 1. The technical documents state the constraint from ω-rigidity and do not discuss its relation to redshift, and the passage is explanation, not a source for status. In this wiki's reading, the fall of momenta as 1/a follows from the expanding metric alone and holds in standard cosmology without a second description, so the redshift illustrates the constraint's reciprocal form but does not test it.

## Scope

- **No check of the relation.** No `verify/` script tests 1 + z = a₀/a_e or p ∝ 1/a; they are textbook results [T]. The one use of redshift in the gate is the gravitational-wave formula above, checked through a figure of the retired candidate.
- **Crossing redshifts.** No program document computes where the program's own corridor crosses −1. The figures in flag 43 come from the flag's executed checks, kept outside the gate in `review/wiki-build-checks/corridor/`, and from Table 5 of the DR2 paper, which one auditor fetched by live search [S].
- **The momentum reading.** The connection between redshift and a·ã = 1 is the popular article's, read by the wiki; the technical documents do not draw it (above).

## Standard references

- V. M. Slipher (1917) †: the spectral shifts of spiral nebulae.
- G. Lemaître (1927) †; E. Hubble (1929) †: the linear relation between redshift and distance, derived from an expanding solution and found in the data.
- S. Weinberg, *Cosmology* (Oxford University Press, 2008) †: redshift, the decay of free-particle momenta and the distance measures of a homogeneous universe.
- D. W. Hogg, "Distance measures in cosmology", arXiv:astro-ph/9905116 (1999) †: the conversions from redshift to distances and times.

None of these is cited in the program's documents; they are given here from memory and are unverified.

## Used by

- [The cosmological constraint a·ã = 1](/wiki/cosmology/scale-factor-duality/cosmological-constraint) — free-particle momenta falling as 1/a, set beside the constraint, and #12's gloss.
- [The conjugate universe: one state, two descriptions](/wiki/program/conjugate-universe) — #12's reading of the redshift in the momentum description.
- [Row 4: thawing dark energy, never phantom](/wiki/predictions/dark-energy-drift) — the observable w(z) and DR2's crossing above z ≈ 0.4.
- [The no-phantom bound w ≥ −1](/wiki/cosmology/dark-energy/no-phantom-bound) — the phantom phase DR2 favours above z ≃ 0.4.
- [τ: hilltop quintessence on the Maslov circle](/wiki/cosmology/dark-energy/tau-quintessence) — the corridor's crossing redshift against DR2's (flag 43).
- [DESI DR2's phantom crossing](/wiki/cosmology/dark-energy/desi-dr2-phantom-crossing) — the record of the finding and its crossing redshift.
- [The hidden sector's thermal history](/wiki/dark-matter/candidates/soliton-candidate/hidden-thermal-history) — the gravitational-wave band of the retired candidate, redshifted to today.
- [Round-3 verdict, rulings and citation audit](/wiki/method/review/round-3/rulings#dark-acoustic-oscillations) — the redshifts at which the hidden fermion decouples.

## Sources

- `papers/broken-born-checkpoint-v2.md` §10 — DR2's crossing "above redshifts z ≃ 0.4" [21S], w(z) "inferred from distances rather than observed", the thawing corridor, and the constraint a·ã = 1 [D]
- `papers/broken-born-checkpoint-v2.md` §13 row 4 — the observable w(z) and "DR2 already favors a crossing above z ≈ 0.4"
- `CLAUDE.md` 'Since the handoff' — the crossing above z ≈ 0.4 and the dark-energy sector "under real pressure ahead of DR3"
- `review/round3-adjudication.md` 'Rulings' 5 — the knock-on that moves the upper end of the gravitational-wave band to 3.2×10⁷ Hz
- `review/wiki-build-flags.md` item 43 — the crossing redshifts of the corridor's line and of DR2's fits, and where the pressure rests (pending ruling), with the checks in `review/wiki-build-checks/corridor/`
- `review/round3/referee/audit-notes.md` Step 4(c) item 5 — the decoupling redshifts of the hidden fermion
- `review/round3/referee/step4.py` section 4 — H(z) and the hidden temperature written in redshift
- `review/round3/referee/step2a.py` 'peak frequency' — the redshifted peak frequency of gravitational waves, as coded by the referee
- `verify/soliton_obituary.py` 'Dark radiation (ruling 5)' — the same formula in the gate's check of the band's upper end
- `notes/knot-dark-matter-standalone.md` §4 — the withdrawn candidate's band, conditional on a first-order hidden transition (withdrawn)
- `popsci/universes-other-half.md` 'Dark energy as the orientation of the split' — the redshift read as a contracting momentum spectrum (popular article; explanation only)
