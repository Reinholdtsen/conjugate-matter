---
title: "The cosmic microwave background"
weight: 16
status: established
description: "The radiation released at recombination: its blackbody spectrum, the acoustic peaks and damping tail of its anisotropies, and what they measure (the baryon and dark-matter densities that calibrate the baryon-acoustic-oscillation ruler, and N_eff through the damping and the neutrinos' phase shift); the program's uses: Planck 2018's N_eff interval behind the round-3 bound ΔN_eff < 0.286, the dark-matter density Ω_c h² = 0.120, limits on the retired candidate's millicharged ψ, and CMB-S4 as row 10's named probe."
provenance: [T]
sources:
  - "notes/knot-dark-matter-standalone.md §3"
  - "notes/knot-dark-matter-standalone.md §4"
  - "notes/knot-dark-matter-standalone.md 'References' [23]"
  - "review/round3/referee/audit-notes.md Step 1"
  - "review/round3/referee/audit-notes.md Step 2"
  - "review/round3/referee/audit-notes.md Step 4(c) items 2, 4, 5, 9"
  - "review/round3/referee/step2a.py 'constants'"
  - "review/round3/referee/step2a.out 'dark radiation'"
  - "review/round3-adjudication.md 'Rulings' 5"
  - "review/round3-adjudication.md 'Rulings' (omitted constraints)"
  - "review/round3-adjudication.md 'Decisions' 1"
  - "verify/soliton_obituary.py 'Dark radiation (ruling 5)'"
  - "review/v3-worklog.md 'New open items'"
  - "papers/broken-born-checkpoint-v2.md §13 row 10"
  - "notes/broken-born-theory.md §9"
  - "notes/broken-born-program-v1.md §9"
  - "review/wiki-build-flags.md items 22, 32, 34"
---

*The cosmic microwave background (CMB) is the thermal radiation left over from the hot early universe, released when the universe became transparent. Until then electrons and nuclei formed a plasma in which light scattered constantly; once the plasma had cooled enough for them to combine into neutral atoms, an event called recombination, the light travelled freely, and the expansion has since stretched it to microwave wavelengths. Small differences in its temperature across the sky preserve the sound waves that ran through the plasma until that moment. Their pattern measures the densities of ordinary and dark matter, the length of the ruler that galaxy surveys use, and the amount of radiation in the early universe, counted as the effective number of light species N_eff. The program has used the CMB in the [round-3 review](/wiki/method/review/round-3) of its retired [soliton dark-matter candidate](/wiki/dark-matter/candidates/soliton-candidate/obituary): Planck 2018's measurement of N_eff bounded the candidate's extra radiation, and Planck's dark-matter density is the target of the review's abundance calculations. [Row 10](/wiki/predictions/early-universe-step), the program's optional early-universe prediction, names a planned CMB experiment, CMB-S4, as its probe.*

**Status:** Established — [T] — textbook cosmology, written here from general knowledge, with the references it adds from model memory (†). The round-3 referee checked the Planck 2018 interval for N_eff against its source (`review/round3/referee/audit-notes.md`, Step 1); the bound drawn from it, ΔN_eff < 0.286, and the hidden temperature ratio ξ < 0.760 are [V], gated in `verify/soliton_obituary.py` ([the soliton-obituary script](/wiki/method/verification/soliton-obituary-script)). Row 10, which names CMB-S4 as its probe, is [D] and not machine-checked.

## Recombination and the released radiation [T]

### Last scattering

In the early universe ordinary matter is an ionized plasma of electrons, protons and the light nuclei made in [Big Bang nucleosynthesis](/wiki/cosmology/early-universe/big-bang-nucleosynthesis) (BBN). Photons scatter off the free electrons, which is Thomson scattering, so often that photons and baryons move together as one fluid [T]. As the universe expands and cools, the electrons combine with nuclei into neutral atoms. Photons outnumber baryons so heavily that this happens only when the temperature is far below the binding energy of hydrogen, for the same reason that deuterium forms late ([the deuterium bottleneck](/wiki/cosmology/early-universe/big-bang-nucleosynthesis#neutron-decay-and-the-deuterium-bottleneck)) [T]. Once the free electrons are gone, the photons stop scattering and travel freely. The sphere around us from which they last scattered is the last-scattering surface, at a redshift written z\* [T].

### A blackbody spectrum

Before last scattering the photons were in thermal equilibrium with the plasma, so their spectrum was that of a blackbody. Free travel through an expanding universe keeps that shape: every wavelength is stretched by the same factor, and the spectrum stays a blackbody whose temperature falls as 1/a, a being the scale factor ([Friedmann cosmology and minisuperspace](/wiki/cosmology/scale-factor-duality/friedmann-cosmology)) [T]. Today the radiation arrives at microwave wavelengths from every direction, nearly uniform across the sky, with a blackbody spectrum to high precision [T].

## The anisotropies [T]

### Where they come from

The temperature differs slightly from one direction to another. In the standard account the differences trace density perturbations present before recombination, seeded by quantum fluctuations during [inflation](/wiki/cosmology/early-universe/inflation-and-dilution#inflation-t) [T]. Plasma that was denser at last scattering was hotter, but it also sat deeper in a gravitational potential well that its photons had to climb out of; the observed temperature combines the two effects [T].

### The angular power spectrum

The temperature map is expanded in spherical harmonics Y_ℓm, the counterpart on a sphere of a Fourier decomposition, and the mean squared amplitude at each multipole ℓ is the angular power spectrum C_ℓ [T]. Multipole ℓ corresponds to an angular scale of about π/ℓ radians: low ℓ are large angles, high ℓ small ones. Because the fluctuations are close to Gaussian, this one function of ℓ carries most of the information in the map [T].

### Acoustic peaks

Before recombination, gravity pulls the photon–baryon fluid into denser regions and the pressure of the photons pushes it back out, so each perturbation oscillates as a sound wave [T]. The sound speed is

```text
c_s = c / √(3(1 + 3ρ_b/(4ρ_γ)))
```

with ρ_b and ρ_γ the baryon and photon densities: photons alone would carry sound at c/√3, and the inertia of the baryons slows it [T]. In Fourier terms, each mode of wavenumber k oscillates in time with a phase equal to k times the comoving distance that sound has travelled, ∫c_s dt/a. Recombination stops the oscillation. The distance travelled by then is the sound horizon r\*, and the modes caught at the extremes of compression or rarefaction give the peaks of C_ℓ [T]:

```text
r*  = ∫ c_s dt/a           up to recombination: the comoving sound horizon
k_n r* = nπ                n = 1, 2, 3, …   odd n compressions, even n rarefactions
θ*  = r*/D_M(z*)           the angle r* subtends today
ℓ_n ≈ nπ/θ*                approximately; the driving and free-streaming radiation shift it
```

D_M is the transverse comoving distance to the last-scattering surface, as in the distance measurements of baryon acoustic oscillations ([from the ruler to distances](/wiki/cosmology/dark-energy/desi#from-the-ruler-to-distances-t)) [T]. The peaks are nearly evenly spaced in ℓ, a fundamental and its overtones, all set by the one length r\*, as the resonances of an organ pipe are set by its length [T].

The same sound waves left the baryon acoustic oscillations (BAO) that galaxy surveys use as a ruler ([the ruler](/wiki/cosmology/dark-energy/desi#the-ruler-baryon-acoustic-oscillations-t)). The survey ruler r_d is the sound horizon at the moment the baryons are released from the photons' drag, slightly later than the photons' last scattering, so r_d is slightly larger than r\* [T].

### Damping

The coupling between photons and baryons is not perfect. Between scatterings a photon travels a mean free path, and by random walk it diffuses a distance r_D that grows as the square root of the elapsed time [T]. Perturbations smaller than r_D are smoothed out, and C_ℓ falls off steeply at high ℓ: the damping tail (Silk 1968 †) [T].

### Polarization and lensing

Thomson scattering of radiation that is brighter along one axis than another, a quadrupole anisotropy, produces linear polarization, so the last-scattering surface also emits a polarization pattern [T]. The pattern is split into E-modes, which have no handedness, and B-modes, which do. Density perturbations produce only E-modes at linear order; primordial gravitational waves would produce both ([primordial backgrounds](/wiki/cosmology/early-universe/phase-transition-gravitational-waves#primordial-backgrounds-t)) [T]. On the way to us the photons are deflected by the gravity of intervening matter. This gravitational lensing slightly smooths the peaks and can be reconstructed from the maps [T].

The Planck data combination behind the program's N_eff interval is labelled `TT,TE,EE+lowE+lensing+BAO`. In the wiki's reading of these labels, `TT`, `TE` and `EE` are the temperature spectrum, its correlation with the E-mode polarization and the E-mode spectrum; `lowE` is the E-mode data at the largest angular scales; `lensing` is the reconstructed lensing; and `BAO` the added distances from baryon acoustic oscillations.

## What the pattern measures [T]

### Densities and the ruler

The peak pattern fixes the parameters of the standard cosmological model, ΛCDM, a [cosmological constant](/wiki/cosmology/dark-energy/cosmological-constant) plus cold dark matter [T]:

- **The baryon density Ω_b h².** Baryons add inertia to the oscillating fluid, which deepens the compressions relative to the rarefactions, so the odd-numbered peaks rise relative to the even-numbered ones [T].
- **The dark-matter density Ω_c h².** Dark matter does not oscillate with the plasma, but it sets when matter began to dominate over radiation. While radiation dominates, the gravitational potentials decay as the plasma oscillates, which drives the oscillations harder, so the heights of the first peaks measure the matter density [T]. Here Ω_c is the density of cold dark matter as a fraction of the critical density, and h is the present Hubble rate in a conventional unit ([what is being set](/wiki/dark-matter/candidates/relic-abundance#what-is-being-set)).
- **The angle θ\*.** The spacing of the peaks gives θ\*, which is measured with high precision [T].
- **The initial perturbations and reionization.** The amplitude and tilt of the primordial spectrum, and the scattering of the radiation by electrons freed when the first stars reionized the universe [T].

The baryon and matter densities fix the sound speed and the time of recombination, and so the lengths r\* and r_d. That is how the CMB calibrates the ruler of baryon-acoustic-oscillation surveys ([calibration](/wiki/cosmology/dark-energy/desi#calibration)) [T]. In the fits of the Dark Energy Spectroscopic Instrument (DESI) that bear on [row 4](/wiki/predictions/dark-energy-drift), the CMB usually enters as the data that fix the early universe and r_d ([from distances to w(z)](/wiki/cosmology/dark-energy/desi#from-distances-to-wz-t)).

### N_eff

Extra radiation, a larger N_eff, raises the expansion rate before recombination ([N_eff: counting light species](/wiki/cosmology/early-universe/radiation-era#n_eff-counting-light-species-t)). The CMB detects it in two ways [T].

- **The damping tail.** A faster expansion shortens the time to recombination. The sound horizon is a distance travelled at the sound speed and scales as 1/H; the diffusion length is a random walk and scales as 1/√H. Their ratio therefore grows with H. The peak positions fix θ\*, so at the observed peak scale a larger N_eff means stronger damping of the small-scale anisotropies (Hou et al. 2013 †) [T].

  ```text
  r* ∝ 1/H        r_D ∝ 1/√H        r_D/r* ∝ √H
  ```

- **The phase shift.** Free-streaming particles such as neutrinos travel at nearly the speed of light, faster than sound in the plasma, and their gravity pulls on the perturbations ahead of the sound waves. This shifts the acoustic peaks toward larger angular scales, lower ℓ, by an amount set by the free-streaming fraction of the radiation; radiation that does not free-stream does not cause it (Bashinsky and Seljak 2004 †; detected in the data by Follin et al. 2015 †) [T].

In a fit, N_eff is correlated with the helium fraction, which sets the number of free electrons and so also the damping, and with the present expansion rate H₀. Adding baryon-acoustic-oscillation distances reduces the correlations, and analyses commonly take the helium fraction that [nucleosynthesis](/wiki/cosmology/early-universe/big-bang-nucleosynthesis#nucleosynthesis-and-the-microwave-background-t) predicts for the fitted baryon density [T].

In the Standard Model (SM), with three neutrino species, N_eff is a little above 3 ([definition](/wiki/cosmology/early-universe/radiation-era#definition)). The round-3 record uses 3.044 for it, and the referee noted that "Planck uses N_eff,SM = 3.046" (audit notes, Step 1).

### Two epochs

Nucleosynthesis measures N_eff in the first minutes and the CMB at recombination. Agreement between the two values, and between the two baryon densities, limits radiation or entropy added in between [T] ([nucleosynthesis and the microwave background](/wiki/cosmology/early-universe/big-bang-nucleosynthesis#nucleosynthesis-and-the-microwave-background-t)).

## How the program uses it

### Planck 2018 and the dark-radiation bound

The massless hidden photon of the [hidden SU(2) → U(1) sector](/wiki/dark-matter/candidates/soliton-candidate/hidden-sector) proposed in the withdrawn manuscript [#14](/wiki/dark-matter/candidates/soliton-candidate) is radiation, so the CMB's N_eff limits the hidden sector's temperature ([dark radiation](/wiki/dark-matter/candidates/soliton-candidate/hidden-thermal-history#dark-radiation)). #14 §4 found that a hidden sector as hot as ours "contributes Delta N_eff ~ 0.86 after its heavy states disappear. That is excluded by Planck 2018 (N_eff = 2.99 +- 0.34 at 95%) [23]." Reference [23] is Planck Collaboration, Astron. Astrophys. 641, A6 (2020), arXiv:1807.06209. The referee located the value as eq. (67b), `N_eff = 2.99 +0.34 -0.33 (95%, TT,TE,EE+lowE+lensing+BAO)` (audit notes, Step 1). The interval is asymmetric where #14 wrote it symmetric; flag 22 in `review/wiki-build-flags.md` records the difference and that nothing changes, since the bound uses only the upper side.

[Ruling 5](/wiki/method/review/round-3/rulings#rulings-5-and-6-the-colder-hidden-sector-and-nucleosynthesis), "Upheld (minor)": "ξ bound 0.760, not 0.77", because "Using N_eff,SM = 3.044, the 95% bound is ΔN_eff < 0.286", ξ being the ratio of the hidden temperature to ours. The script takes the upper end of the interval and subtracts the Standard Model value, `bound = 2.99 + 0.34 - 3.044`, and gates both numbers:

```text
== Dark radiation (ruling 5)
PASS  95% bound Delta N_eff < 0.286  [0.286]
PASS  xi < 0.760  [0.7601]
```

With Planck's 3.046 instead, the referee's code gives "N_eff,SM=3.046: DeltaN_max(95%) = 0.284 -> xi_max = 0.7588" (`review/round3/referee/step2a.out`). v3's 0.77 had come from a bound of 0.3 that the v3 worklog called "an approximate Planck 2018 value, from memory †" ([the worklog's table and the corrected bound](/wiki/dark-matter/candidates/soliton-candidate/hidden-thermal-history#the-worklogs-table-and-the-corrected-bound)). The candidate is dead, and these numbers are kept as its record ([Obituary: superheavy conjugate solitons](/wiki/dark-matter/candidates/soliton-candidate/obituary)).

### The dark-matter density

The round-3 record takes the mean density of [dark matter](/wiki/dark-matter) from Planck. Among the referee's independently sourced constants is Ω_c h² = 0.120, attributed to the "Planck 2018 VI abstract" (`review/round3/referee/step2a.py`), from which its code gives "rho_DM mean = 1.2644e-06 GeV/cm^3 = 1.264 keV/cm^3" (`step2a.out`); #14 had used "Omega h^2 ~ 0.12, with mean rho_DM = 1.26 keV/cm^3" (§3). `verify/soliton_obituary.py` codes the same density, `RHO_DM = 0.120*1.05371e-5` in GeV cm⁻³, and describes its constants as "PDG and Planck 2018 values", PDG being the Particle Data Group; flag 34 in `review/wiki-build-flags.md` records that they are typed in, not retrieved. The density is the target of the review's abundance calculations: the monopole yield at which the monopoles would be all of the dark matter ([overproduction at the benchmark](/wiki/dark-matter/candidates/soliton-candidate/overproduction)), and the freeze-out of ψ and of the W′ bosons ([thermal freeze-out](/wiki/dark-matter/candidates/thermal-freeze-out#the-retired-candidates-hidden-sector)).

### Row 10's probe: CMB-S4

[Row 10](/wiki/predictions/early-universe-step) states two optional imprints of the program's dual gravitational sector, "Optional a⁻⁶ G_eff step; closed dual curvature ⇒ negative ΔN_eff", and its kill column reads "(Knob-bounded; CMB-S4 probes)" (#11 §13). A closed dual space would act on our expansion as negative dark radiation ([row 10 on the radiation-era page](/wiki/cosmology/early-universe/radiation-era#row-10-negative-δn_eff-from-a-closed-dual-space)). CMB-S4 is a proposed ground-based CMB experiment [T]; whether it is still going ahead is unchecked (flag 32 in `review/wiki-build-flags.md`, a lead from model memory that the flags' audit left unclear).

[Checkpoint #11](/wiki/history/documents/checkpoint) gives no sensitivity. The [lab notebook](/wiki/history/documents/lab-notebook)'s row had one: "(Bounds constrain knobs; CMB-S4 N_eff at ±0.03 probes the curvature term)" (#1 §9, transcribed from its LaTeX). Version 1 of the checkpoint dropped the figure, writing "(Bounds constrain knobs; CMB-S4 probes)" (#9 §9), and no document says why ([Superseded: the spectral step and the ±0.03 target](/wiki/predictions/early-universe-step#superseded-the-spectral-step-and-the-003-target)). No document compares row 10 with CMB data or computes the size of its negative ΔN_eff ([the data situation](/wiki/predictions/early-universe-step#the-data-situation)).

### Limits on the retired candidate's light fermion

If the hidden and visible photons mix kinetically, #14's light hidden fermion ψ carries a visible charge of about ε times the electron's and is a millicharged particle (MCP) ([a millicharged ψ](/wiki/dark-matter/candidates/soliton-candidate/kinetic-mixing#i-a-millicharged-ψ)). Among the constraints #14 had not evaluated, the referee listed several that rest on the CMB or on recombination (Step 4(c)):

- Vogel and Redondo, arXiv:1311.2600, a Planck-2013-era analysis that "disfavors MCPs with masses between 14 MeV < m_f < 390 MeV for a wide range of minicharges eps > 1e-7" (item 2);
- McDermott, Yu and Zurek, PRD 83 (2011) 063509, from recombination: "eps < 1e-6 at 1 GeV for all DM", DM being dark matter (item 4);
- limits on dark matter that scatters off baryons, which for a charged subcomponent "vanish below 0.4% interacting fraction (Boddy et al. 1808.00001); psi up to 10% is not automatically safe" (item 4);
- dark acoustic oscillations: ψ would stay coupled to the bath of hidden photons until late, and "For sub-GeV psi this approaches recombination" (item 5; [dark acoustic oscillations](/wiki/method/review/round-3/rulings#dark-acoustic-oscillations)).

The adjudication accepted "Charged-subcomponent and CMB bounds" and "Dark acoustic oscillations" as a to-do, "not individually re-checked" ([charged-subcomponent and microwave-background bounds](/wiki/method/review/round-3/rulings#charged-subcomponent-and-cosmic-microwave-background-bounds)). [Decision 1](/wiki/method/review/round-3/decisions#decision-1-strict-sector-separation), [strict sector separation](/wiki/program/postulates/p4-polarized-matter), then closed the millicharge channel. The ψ window was already dead on its counting, and the candidate's retirement left the remaining items moot ([channels that became moot](/wiki/dark-matter/candidates/soliton-candidate/psi-relic-window#channels-that-became-moot)).

### Isocurvature

The CMB limits isocurvature perturbations, in which the ratios of the components vary from place to place while the total density does not, to a small fraction of the total [T] ([isocurvature](/wiki/cosmology/early-universe/inflation-and-dilution#isocurvature)). For #14 the referee noted two possibilities and computed neither (Step 4(c) item 9): "a separately reheated hidden sector can carry dark-radiation isocurvature (conditional; not computed). No CMB-scale monopole isocurvature expected from post-inflation production (inference, not computed)." The adjudication accepted "The reheating mechanism for ξ" as a to-do without re-checking it ([reheating](/wiki/method/review/round-3/rulings#reheating)).

## Standard references

- A. A. Penzias and R. W. Wilson (1965) †; R. H. Dicke, P. J. E. Peebles, P. G. Roll and D. T. Wilkinson (1965) †: the detection of the radiation and its interpretation as the relic of a hot early universe.
- J. Silk (1968) †: the damping of small-scale perturbations by photon diffusion.
- R. A. Sunyaev and Ya. B. Zeldovich (1970) †; P. J. E. Peebles and J. T. Yu (1970) †: the acoustic oscillations of the photon–baryon plasma, also cited on [DESI baryon acoustic oscillations](/wiki/cosmology/dark-energy/desi).
- W. Hu and S. Dodelson, "Cosmic microwave background anisotropies", Annual Review of Astronomy and Astrophysics (2002) †: a review of the physics on this page.
- S. Bashinsky and U. Seljak (2004) †: the phase shift from free-streaming neutrinos; B. Follin, L. Knox, M. Millea and Z. Pan (2015) †: its detection.
- Z. Hou, R. Keisler, L. Knox, M. Millea and C. Reichardt (2013) †: how N_eff acts on the damping tail at fixed θ\*.
- Planck Collaboration, Astron. Astrophys. 641, A6 (2020), arXiv:1807.06209: #14's reference [23], "Planck 2018 VI" in the round-3 audit, which checked its eq. (67b) for N_eff; the referee also took Ω_c h² = 0.120 from its abstract.
- The referee's literature on millicharged and charged dark matter (Vogel and Redondo; McDermott, Yu and Zurek; Boddy et al.) and on dark acoustic oscillations (Cyr-Racine et al.), listed with [the omitted constraints](/wiki/method/review/round-3/rulings#omitted-constraints).

None of the † entries is cited in the program's documents; they are given from model memory and are unverified.

## Used by

- [The hidden sector's thermal history](/wiki/dark-matter/candidates/soliton-candidate/hidden-thermal-history) — Planck's N_eff interval, ΔN_eff < 0.286 and ξ < 0.760.
- [Row 10: an early step in G_eff](/wiki/predictions/early-universe-step) — CMB-S4 as the named probe of a negative ΔN_eff.
- [Round-3 verdict, rulings and citation audit](/wiki/method/review/round-3/rulings) — ruling 5, and the CMB bounds among the omitted constraints.
- [Obituary: the ψ relic window](/wiki/dark-matter/candidates/soliton-candidate/psi-relic-window) — CMB and recombination limits on a millicharged ψ.
- [Relic abundance mechanisms](/wiki/dark-matter/candidates/relic-abundance) — the target density Ω h² = 0.120.
- [Round-3 arbitration and the referee's constants](/wiki/method/review/round-3/arbitration) — Ω_c h² = 0.120 from the Planck 2018 abstract.
- [DESI baryon acoustic oscillations](/wiki/cosmology/dark-energy/desi) — the CMB's calibration of the ruler r_d.
- [Inflation, reheating and entropy dilution](/wiki/cosmology/early-universe/inflation-and-dilution) — the seed perturbations and the limit on isocurvature.
- [The radiation era: thermal history and N_eff](/wiki/cosmology/early-universe/radiation-era) — N_eff before recombination.

## Sources

- `notes/knot-dark-matter-standalone.md` §4 — the dark radiation and Planck 2018 as #14 cites it; §3 — "Omega h^2 ~ 0.12"; 'References' [23] (withdrawn manuscript)
- `review/round3/referee/audit-notes.md` Step 1 — Planck 2018 VI eq. (67b) and Planck's 3.046; Step 2 — the referee's constants; Step 4(c) items 2, 4, 5 and 9 — the CMB-based limits on ψ, dark acoustic oscillations and isocurvature
- `review/round3/referee/step2a.py` — Ω_c h² = 0.120 from the Planck 2018 abstract; `review/round3/referee/step2a.out` 'dark radiation' — the bound and ξ with 3.044 and 3.046, and the mean dark-matter density
- `review/round3-adjudication.md` 'Rulings' 5 — ΔN_eff < 0.286 and ξ < 0.760; the omitted-constraints list — "Charged-subcomponent and CMB bounds", "Dark acoustic oscillations", the reheating mechanism; 'Decisions' 1 — the millicharge channel closed
- `verify/soliton_obituary.py` 'Dark radiation (ruling 5)' — the gated bound and ξ; its constant `RHO_DM`
- `review/v3-worklog.md` 'New open items' (O2) — the earlier 0.3 bound, "from memory †"
- `papers/broken-born-checkpoint-v2.md` §13 row 10 — "(Knob-bounded; CMB-S4 probes)"
- `notes/broken-born-theory.md` §9 row 10 — the dropped ±0.03 target; `notes/broken-born-program-v1.md` §9 row 10 — the row without the figure
- `review/wiki-build-flags.md` item 22 — #14's symmetric interval; item 32 — CMB-S4's status, unchecked; item 34 — the gate's constants typed in
