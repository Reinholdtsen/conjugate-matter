---
title: "The radiation era: thermal history and N_eff"
weight: 10
status: established
description: "The expansion rate H = 1.66√g* T²/M_Pl, entropy density and yields Y = n/s, and the effective number of relativistic species with its nucleosynthesis and cosmic-microwave-background bounds."
provenance: [T]
sources:
  - "verify/soliton_obituary.py 'Anchors'"
  - "verify/soliton_obituary.py 'Kibble normalization (ruling 1)'"
  - "verify/soliton_obituary.py 'Dark radiation (ruling 5)'"
  - "review/round3-adjudication.md 'Rulings' 1"
  - "review/round3-adjudication.md 'Rulings' 5"
  - "review/round3-adjudication.md 'Rulings' 6"
  - "review/round3-adjudication.md 'Lessons (now in CLAUDE.md)'"
  - "review/round3/adjudicator/round3_arb.out"
  - "review/round3/referee/audit-notes.md Step 1"
  - "review/round3/referee/audit-notes.md Step 2"
  - "review/round3/referee/audit-notes.md Step 4(a)"
  - "review/round3/referee/step2a.py 'Delta N_eff'"
  - "review/round3/referee/step2a.out 'dark radiation'"
  - "review/v3-worklog.md 'New open items'"
  - "papers/broken-born-checkpoint-v2.md §10"
  - "papers/broken-born-checkpoint-v2.md §12"
  - "papers/broken-born-checkpoint-v2.md §13 row 10"
  - "notes/broken-born-theory.md §6"
  - "notes/broken-born-theory.md §9"
  - "notes/broken-born-theory.md §10"
  - "notes/broken-born-program-v1.md §9"
  - "notes/knot-dark-matter-standalone.md §3"
  - "notes/knot-dark-matter-standalone.md §4"
  - "review/wiki-build-flags.md items 22, 32"
---

*The radiation era is the early period in which the universe's energy was dominated by radiation and by particles moving at nearly the speed of light, so that the temperature alone set how fast the universe expanded. Three standard quantities describe it. The first is the expansion rate as a function of temperature, H = 1.66√g\* T²/M_Pl. The second is the entropy density: it falls as the volume grows, so the ratio of a relic's number density to it, the yield, stays fixed once the relic is no longer made or destroyed. The third is N_eff, the effective number of light neutrino-like species, which nucleosynthesis and the cosmic microwave background both measure. The program uses these quantities twice: in its [optional prediction](/wiki/predictions/early-universe-step) of fewer effective species from the [conjugate universe](/wiki/program/conjugate-universe), and in the [review](/wiki/method/review/round-3) that retired its [soliton dark-matter candidate](/wiki/dark-matter/candidates/soliton-candidate/obituary), whose central error was a dropped factor of the radiation-era expansion rate.*

**Status:** Established — [T] — textbook thermal history, written here from general knowledge. `verify/soliton_obituary.py` checks the Friedmann coefficient 1.66 and the one-species normalization of ΔN_eff as anchors independent of any program document, and gates the dark-radiation bound ΔN_eff < 0.286 of [review round 3](/wiki/method/review/round-3) [V] ([the soliton-obituary script](/wiki/method/verification/soliton-obituary-script)). The program's own use, negative ΔN_eff in [row 10](/wiki/predictions/early-universe-step), is [D] and not machine-checked.

## What the radiation era is [T]

In the [Friedmann cosmology](/wiki/cosmology/scale-factor-duality/friedmann-cosmology) of a homogeneous universe, each kind of content thins at its own rate as the scale factor a grows: matter as a⁻³, radiation as a⁻⁴. Radiation loses the extra factor because each quantum's energy is redshifted as well as diluted. Running the expansion backwards, radiation therefore grows faster than matter, and before matter–radiation equality it dominates the energy density. That early stretch, which runs from reheating at the end of [inflation](/wiki/cosmology/early-universe/inflation-and-dilution) through nucleosynthesis to matter–radiation equality, is the radiation era.

In this era the plasma is close to thermal equilibrium at a temperature T, and the temperature falls as 1/a, up to the small corrections described under entropy below. The energy density of everything relativistic is

```text
ρ = (π²/30) g* T⁴
```

where g\* is the effective number of relativistic degrees of freedom: each bosonic spin or particle state counts 1 and each fermionic state counts 7/8, the factor that the Fermi–Dirac distribution gives relative to the Bose–Einstein one, with species at their own temperature weighted by (T_i/T)⁴ [T]. As the temperature drops below a particle's mass, that particle annihilates away and stops counting, so g\* falls in steps. The values that appear in the program's scripts are g\* = 106.75 with every Standard Model (SM) particle relativistic, 10.75 when the neutrinos decouple (photons, electrons and positrons, and three neutrino species), and the round value g\* = 100 used for the [Kibble](/wiki/electric-magnetic-duality/monopoles/kibble-mechanism) anchor (`verify/soliton_obituary.py`).

## The expansion rate [T]

### Derivation

The Friedmann equation for a spatially flat universe is H² = 8πGρ/3, with H = ȧ/a the Hubble rate. (On this page H is always the Hubble rate, not the program's phase-space metric H of [Born geometry](/wiki/phase-space/born-geometry/born-structures).) Writing Newton's constant through the Planck mass, G = 1/M_Pl², and inserting the radiation energy density gives [T]

```text
H² = (8π/3) ρ / M_Pl² = (8π³/90) g* T⁴ / M_Pl²
H  = √(8π³/90) √g* T² / M_Pl = 1.66 √g* T² / M_Pl
```

The arbitration script of round 3 prints the coefficient: "1.66 check: sqrt(8 pi^3/90) = 1.6602" (`review/round3/adjudicator/round3_arb.out`). The expansion rate grows as T², and its prefactor carries √g\*: more light species means more energy at the same temperature and so a faster expansion.

### Two Planck masses

Two conventions for the Planck mass are in common use [T]. The one above is M_Pl = G^{−1/2}; `verify/soliton_obituary.py` takes M_Pl = 1.22089×10¹⁹ GeV, the Particle Data Group (PDG) 2024 value the round-3 referee also used. The reduced Planck mass is M̄_Pl = M_Pl/√(8π), for which the script takes 2.43536×10¹⁸ GeV. With the reduced mass the Friedmann equation reads 3M̄_Pl²H² = ρ, the form [Friedmann cosmology and minisuperspace](/wiki/cosmology/scale-factor-duality/friedmann-cosmology) uses, and the same expansion rate is written H = √(π²g\*/90) T²/M̄_Pl, as the script codes it. The physics is the same; only the prefactor moves. Any formula that combines H with a power of the Planck mass has to keep the two consistent, which is what the soliton candidate's mass estimate failed to do (below).

### The anchor

The coefficient is the first anchor of the program's soliton-obituary script, chosen because it is a textbook identity, independent of every program document (round-3 lesson 2: "An anchor must be independent of the paper"; [independent anchors](/wiki/method/verification/independent-anchors)). The check rounds √(8π³/90) to two decimals and compares it with 1.66:

```text
== Anchors
PASS  Friedmann: H = 1.66 sqrt(g*) T^2/M_Pl
```

## Entropy and the yield Y = n/s [T]

While the plasma stays in equilibrium, the entropy in a comoving volume is conserved. The entropy density is

```text
s = (2π²/45) g*s T³
```

with g\*s counted like g\* but with a third power of each species' temperature ratio; the two counts agree while all species share one temperature [T]. Conservation of s·a³ means that T falls as 1/a except when g\*s drops: when a species annihilates, its entropy passes to the particles that remain, and the temperature falls more slowly for a while [T].

Because s and a number density n both scale as a⁻³ when nothing is created or destroyed, their ratio, the yield

```text
Y = n/s
```

is constant once a relic has stopped interacting. The yield is how relic abundances are carried from the early universe to today: the present density of a relic of mass m is m·Y·s₀, with s₀ the entropy density today [T] ([relic abundance mechanisms](/wiki/dark-matter/candidates/relic-abundance)). `verify/soliton_obituary.py` takes s₀ = 2891.2 cm⁻³, the value the round-3 referee took from the PDG's 2024 astrophysical constants (`review/round3/referee/audit-notes.md` Step 2), and builds the dark-matter density from Ωh² = 0.120. The withdrawn manuscript [#14](/wiki/dark-matter/candidates/soliton-candidate) used "s_0 ~ 2.9e3 /cm^3" and "mean rho_DM = 1.26 keV/cm^3" (#14 §3), which the referee checked as "OK".

### The Kibble yield as a radiation-era formula

The count of [monopoles](/wiki/electric-magnetic-duality/monopoles) a cooling universe forms is a yield, and computing it uses both formulas above. [The Kibble mechanism](/wiki/electric-magnetic-duality/monopoles/kibble-mechanism) gives at least about one defect per Hubble volume, n ≈ H³ at the transition temperature T_c. Dividing by s gives the form [checkpoint #11](/wiki/history/documents/checkpoint) writes in §12, "n/s = p (T_c/M_Pl)³", with [T]

```text
p = (1.66 √g*)³ · 45/(2π² g*)
```

These numbers belong to the retired soliton episode. At g\* = 100 the script prints `p = 104.31 with M_Pl` and, with M̄_Pl in place of M_Pl, `p = 0.828 with reduced M_Pl`. Version 3 of #14 had used p ≈ 0.023, which is the same formula with the Friedmann prefactor 1.66√g\* set to one. Ruling 1 of round 3: "v3's 0.0228 drops (1.66√g\*)³ ≈ 4.6×10³. My error came from misremembering the formula." The script prints the dropped factor as `[4575.6]`. This was the central error of the candidate ([Obituary: the Kibble normalization](/wiki/dark-matter/candidates/soliton-candidate/kibble-normalization); [Obituary: superheavy conjugate solitons](/wiki/dark-matter/candidates/soliton-candidate/obituary)). The second anchor of the script is the same normalization taken from the literature, "one defect per Hubble volume gives n/s ~ 100 (T_c/M_Pl)^3 (Gangui, astro-ph/0110285)".

## N_eff: counting light species [T]

### Definition

After electrons and positrons annihilate, the radiation of the universe is photons and the three species of neutrinos. The neutrinos had already decoupled, so the entropy of the annihilations heated only the photons, and the neutrino temperature ends below the photon temperature, T_ν = (4/11)^{1/3} T_γ [T]. The effective number of neutrino species, N_eff, is defined by writing the total radiation density as

```text
ρ_rad = ρ_γ [1 + (7/8)(4/11)^{4/3} N_eff]
```

so that N_eff measures the energy density of all light species other than photons, in units of one neutrino species at T_ν [T]. Three neutrinos that decoupled instantly would give exactly 3. They were still slightly coupled when electrons and positrons annihilated and received a little of that energy, and with that and smaller corrections the SM value is a little above 3. The round-3 record uses 3.044 ([ruling 5](/wiki/method/review/round-3/rulings)); the referee also gave results for 3.046, the value Planck's analysis uses ("Planck uses N_eff,SM = 3.046", audit notes Step 1). The referee's script attributes 3.044 to "Bennett et al 2021" (`review/round3/referee/step2a.py`).

### Extra species: ΔN_eff

Any other light species adds to N_eff. Its contribution is its energy density divided by that of one neutrino species, (π²/30)(7/4)T_ν⁴, and the script codes it as [T]

```text
ΔN_eff = (4/7) g (T_x/T_ν)⁴
```

for g bosonic degrees of freedom at temperature T_x (fermionic ones weighted by 7/8). The anchor is the defining case: one neutrino species, g = 7/4, at T_x = T_ν gives exactly 1.

```text
PASS  Delta N_eff: one extra neutrino species at T_nu gives 1
```

### A sector at its own temperature

A hidden sector that shares no interactions with ours keeps its own temperature, and the ratio fixes its ΔN_eff. The v3 worklog describes the setup it scripted: "the two sectors at temperature ratio ξ at high T, then separately entropy-conserving, ending with only the dark photon relativistic" (`review/v3-worklog.md`, item O2). Each sector conserves its own entropy, so when its heavy states annihilate, their entropy heats only the light states of that sector. For a hidden sector that starts with g_h(high) degrees of freedom and ends with g_h(late), the result is [T]

```text
T_h/T_ν = ξ · [(g_h(high)/g_h(late)) / (g_vis(high)/g_ν,dec)]^{1/3}
```

with g_vis(high) = 106.75 and g_ν,dec = 10.75 on the visible side. The round-3 referee's script codes the bracket, the shared-temperature case ξ = 1, and brings in ξ afterwards through ΔN_eff ∝ ξ⁴ (`review/round3/referee/step2a.py`). Once both the hidden photon and the neutrinos are free and relativistic, both temperatures fall as 1/a, and the ratio stays fixed.

## How N_eff is measured [T]

**Nucleosynthesis.** In the first minutes, the ratio of neutrons to protons freezes when the weak interactions that convert them become slower than the expansion. A larger expansion rate, from more radiation and hence a larger N_eff, makes that happen earlier and at a higher temperature, which leaves more neutrons and so more helium. The primordial helium abundance therefore measures H during Big Bang nucleosynthesis (BBN), and through H = 1.66√g\* T²/M_Pl it measures the radiation content [T]. A change in G at that time would act on H in the same way, which is why a step in the effective strength of gravity is constrained by the same physics (the wiki's reading of why [the lab notebook](/wiki/history/documents/lab-notebook) places the G_eff step of [row 10](/wiki/predictions/early-universe-step) "before BBN", #1 §6).

**The cosmic microwave background (CMB).** Extra radiation changes the expansion history before recombination, which shifts the scale of the acoustic peaks relative to the damping of small-scale anisotropies, and free-streaming light particles leave a characteristic phase shift in the peaks [T]. The value the program's documents use is from Planck 2018: "excluded by Planck 2018 (N_eff = 2.99 +- 0.34 at 95%) [23]" (#14 §4). The referee checked the reference, Planck 2018 VI eq. (67b), and recorded the interval as "N_eff = 2.99 +0.34 -0.33" at 95%, from the combination of Planck data with baryon-acoustic-oscillation measurements (audit notes, Step 1). #14's symmetric interval against the source's asymmetric one is flag 22 in `review/wiki-build-flags.md`; the bound below uses only the +0.34 side.

**The bound used in round 3.** For the retired soliton candidate (below), the script takes the upper end of that interval, 2.99 + 0.34, and subtracts the SM value 3.044 (`bound = 2.99 + 0.34 - 3.044`):

```text
== Dark radiation (ruling 5)
PASS  95% bound Delta N_eff < 0.286  [0.286]
```

**The next step.** CMB-S4, a proposed ground-based CMB experiment [T], is the probe #11 names for the program's own N_eff prediction; whether it is still going ahead is unchecked (flag 32 in `review/wiki-build-flags.md`).

## How the program uses it

### Row 10: negative ΔN_eff from a closed dual space

The program's [duality dictionary](/wiki/cosmology/scale-factor-duality/duality-dictionary) translates content of the momentum-space (dual) frame into its effect on our expansion. Spatial curvature of the dual frame, w̃ = −1/3, appears on our side as "Dark radiation (w = +1/3; closed dual space ⇒ *negative* ΔN_eff)" ([the lab notebook](/wiki/history/documents/lab-notebook) #1 §6, [D]). The sign follows from the Friedmann equation: the curvature of a closed space enters with the opposite sign to an energy density, so read as a fluid it has negative energy density [T], and the dictionary carries that sign across as negative dark radiation. #11 §10 keeps it as "dual curvature ↦ negative dark radiation".

[Row 10](/wiki/predictions/early-universe-step) states the prediction (#11 §13): standard expectation "Standard G, N_eff"; requirement "Optional a⁻⁶ G_eff step; closed dual curvature ⇒ negative ΔN_eff"; and "(Knob-bounded; CMB-S4 probes)". It is [D] and not machine-checked. Knob-bounded means that a null result bounds free parameters rather than killing the program; the lab notebook lists the parameters of this dual geometric sector as M̃ and k̃ and calls them optional (#1 §10). The lab notebook's row 10 had been more specific, saying that CMB-S4 measuring N_eff "at ±0.03 probes the curvature term" (#1 §9). Version 1 of the checkpoint dropped the figure, writing "(Bounds constrain knobs; CMB-S4 probes)" (#9 §9), and #11 keeps only "CMB-S4 probes" ([history of the predictions table](/wiki/predictions/table-history)).

### The retired soliton candidate

The review that retired the soliton candidate turned on radiation-era physics in three places. The candidate is dead, and the numbers below are kept as its record ([Obituary: superheavy conjugate solitons](/wiki/dark-matter/candidates/soliton-candidate/obituary)).

- **The Kibble yield.** The dropped factor (1.66√g\*)³ above, ruling 1 ([Obituary: the Kibble normalization](/wiki/dark-matter/candidates/soliton-candidate/kibble-normalization)). Corrected, the yield fixes the mass at which the monopoles would be all of the [dark matter](/wiki/dark-matter), and the benchmark of v3 is overproduced ([overproduction at the benchmark](/wiki/dark-matter/candidates/soliton-candidate/overproduction)). v3 also reported a "factor of about 3" spread from the choice of Planck mass; ruling 2 found that "consistently normalized, the two conventions agree", which is the point made under the two Planck masses above.
- **Dark radiation and the hidden temperature.** The massless hidden photon of #14's [hidden SU(2) → U(1) sector](/wiki/dark-matter/candidates/soliton-candidate/hidden-sector) is radiation. "Suppose the two sectors shared a temperature above v. The hidden sector - the SU(2)_d gauge fields, the adjoint scalar and one psi doublet - then contributes Delta N_eff ~ 0.86 after its heavy states disappear" (#14 §4), where v is the hidden symmetry-breaking scale. The referee's script counts that sector as "SU(2) gauge (3x2) + real adjoint (3) + Dirac doublet (2x4 x 7/8)" (`step2a.py`) and prints "g_h(high)=16.0, g_h(late)=2.0, g_vis(high)=106.75: T_h/T_nu = 0.9305, DeltaN_eff = 0.8567" (`step2a.out`). Since ΔN_eff scales as ξ⁴, the bound 0.286 caps ξ, the ratio of hidden to visible temperature, and the script checks `xi < 0.760  [0.7601]`. #14 had required "xi < 0.77". The v3 worklog had tabulated that figure for the bound ΔN_eff < 0.3 and noted "The 0.3 bound is an approximate Planck 2018 value, from memory †" (item O2); the referee's script gives "xi needed for DeltaN<0.30: 0.7693". Ruling 5 upheld the correction as minor: "ξ bound 0.760, not 0.77". The referee's value with N_eff,SM = 3.046 is 0.759. The full record is [the hidden sector's thermal history](/wiki/dark-matter/candidates/soliton-candidate/hidden-thermal-history).
- **Freeze-out during nucleosynthesis.** A hidden particle freezes out at hidden temperature T_h ~ m/20, which corresponds to a different visible temperature from the one at which the same mass would freeze out in our plasma. The referee converted the hidden freeze-out of #14's fermion ψ to visible temperatures, found that at MeV masses it falls "during BBN", and concluded that ψ "Needs m_psi >~ 20-30 MeV" (Step 4(a) item 8); ruling 6 accepted this without re-checking it ([Obituary: the ψ relic window](/wiki/dark-matter/candidates/soliton-candidate/psi-relic-window)).

## Standard references

- E. W. Kolb, M. S. Turner, *The Early Universe* (Addison-Wesley, 1990): #14's reference [17], which the round-3 audit resolved as "Front. Phys. 69 (1990), Addison-Wesley" (Step 1); `verify/soliton_obituary.py` takes its freeze-out formulas from "Kolb & Turner eqs. 5.43-5.45". A standard treatment of the thermal history on this page.
- Planck Collaboration, Astron. Astrophys. 641, A6 (2020), arXiv:1807.06209: #14's reference [23], "Planck 2018 VI" in the round-3 audit, which checked its eq. (67b) for N_eff.
- Particle Data Group, *Review of Particle Physics* (2024), astrophysical constants: the source of M_Pl and s₀ in the referee's script and in `verify/soliton_obituary.py`.
- A. Gangui, astro-ph/0110285: the normalization "n/s ~ 100 (T_c/M_Pl)^3" used as the script's second anchor; not cited in #11.
- J. J. Bennett et al. (2021) †: the source the referee's script names for 3.044, a precision calculation of neutrino decoupling in the SM. G. Mangano et al. (2005) †: the earlier calculation behind 3.046. The details of both entries are from model memory and unverified.

## Used by

- [Row 10: an early step in G_eff](/wiki/predictions/early-universe-step) — negative ΔN_eff from closed dual curvature.
- [The duality dictionary w_eff = −w̃](/wiki/cosmology/scale-factor-duality/duality-dictionary) — dual curvature acts as dark radiation, measured by ΔN_eff.
- [Independent anchors](/wiki/method/verification/independent-anchors) — the Friedmann coefficient 1.66 as a textbook anchor.
- [The soliton-obituary script](/wiki/method/verification/soliton-obituary-script) — the anchors, the yield normalization and the dark-radiation bound, executed.
- [Obituary: the Kibble normalization](/wiki/dark-matter/candidates/soliton-candidate/kibble-normalization) — the dropped (1.66√g\*)³.
- [Overproduction at the benchmark](/wiki/dark-matter/candidates/soliton-candidate/overproduction) — the yield at minimum production.
- [The hidden sector's thermal history](/wiki/dark-matter/candidates/soliton-candidate/hidden-thermal-history) — the dark-radiation bound and ξ < 0.760.
- [Obituary: the ψ relic window](/wiki/dark-matter/candidates/soliton-candidate/psi-relic-window) — freeze-out timed against nucleosynthesis.
- [Relic abundance mechanisms](/wiki/dark-matter/candidates/relic-abundance) — the expansion rate and the yield in freeze-out.
- [Gravitational waves from phase transitions](/wiki/cosmology/early-universe/phase-transition-gravitational-waves) — the Hubble rate and entropy conservation in the redshift of the peak frequency.

## Sources

- `verify/soliton_obituary.py` 'Anchors', 'Kibble normalization (ruling 1)', 'Dark radiation (ruling 5)' — the Friedmann coefficient, the one-species anchor, the constants, p, the ΔN_eff bound and ξ, all executed
- `review/round3-adjudication.md` 'Rulings' 1, 5, 6 — the dropped factor; ΔN_eff < 0.286 with N_eff,SM = 3.044 and ξ < 0.760; freeze-out during nucleosynthesis; 'Lessons (now in CLAUDE.md)' — the Friedmann coefficient as an independent anchor
- `review/round3/adjudicator/round3_arb.out` — "sqrt(8 pi^3/90) = 1.6602"
- `review/round3/referee/audit-notes.md` Step 1 — the Planck and Kolb–Turner references, Planck's 3.046; Step 2 — the constants and the dark-radiation recomputation; Step 4(a) item 8 — ψ freeze-out during nucleosynthesis
- `review/round3/referee/step2a.py` 'Delta N_eff' and `review/round3/referee/step2a.out` 'dark radiation' — the degrees-of-freedom count, the temperature ratio and the two SM values
- `review/v3-worklog.md` 'New open items' (O2) — the two-sector setup and the approximate 0.3 bound
- `papers/broken-born-checkpoint-v2.md` §10, §12, §13 row 10 — the dictionary entry; the Kibble yield in the soliton obituary; the program's ΔN_eff prediction
- `notes/broken-born-theory.md` §6, §9 row 10, §10 — the dictionary table [D]; the dropped ±0.03 target; the optional geometric knobs
- `notes/broken-born-program-v1.md` §9 row 10 — the row without the figure
- `notes/knot-dark-matter-standalone.md` §3, §4 — the withdrawn candidate's yield inputs and dark radiation (withdrawn; its body numbers are superseded)
- `review/wiki-build-flags.md` item 22 — #14's symmetric N_eff interval against the source's asymmetric one; item 32 — CMB-S4's status, unchecked
