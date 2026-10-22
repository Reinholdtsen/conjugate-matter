---
title: "Gravitational waves from phase transitions"
weight: 30
status: established
description: "Stochastic gravitational waves from first-order phase transitions and their redshifted peak frequency, and the primordial background the lab notebook's dropped spectral step referred to."
provenance: [T]
sources:
  - "review/round3-adjudication.md 'Rulings' 5"
  - "verify/soliton_obituary.py 'Dark radiation (ruling 5)'"
  - "review/round3/referee/audit-notes.md Step 2"
  - "review/round3/referee/audit-notes.md Step 4(a) item 2"
  - "review/round3/referee/step2a.py 'peak frequency'"
  - "review/round3/referee/step2a.out 'peak frequency'"
  - "review/round3/referee/step4.py 'first-order transition'"
  - "review/round3/referee/step4.out 'first-order'"
  - "notes/knot-dark-matter-standalone.md §3"
  - "notes/knot-dark-matter-standalone.md §4"
  - "notes/broken-born-theory.md §6"
  - "notes/broken-born-theory.md §9"
  - "notes/broken-born-theory.md §10"
  - "notes/broken-born-program-v1.md §8"
  - "notes/broken-born-program-v1.md §9"
  - "papers/broken-born-checkpoint-v2.md §13 row 10"
  - "review/wiki-build-flags.md item 32"
---

*A first-order phase transition in the early universe proceeds by bubbles of the new phase forming, growing and colliding, much as water boils, and the collisions and the sound waves they leave in the plasma produce gravitational waves that arrive today from every direction as a random background. The waves' characteristic frequency is set at the transition by its temperature and duration and has been stretched by the expansion ever since, so a transition at a higher temperature leaves a higher frequency today. A related background, the primordial one, comes from [inflation](/wiki/cosmology/early-universe/inflation-and-dilution), and its spectrum records how fast the universe expanded at each early epoch. The program met this physics in two places: the hidden-sector transition of its [retired soliton dark-matter candidate](/wiki/dark-matter/candidates/soliton-candidate/obituary), whose signal would have lain far above the frequencies of current detectors, and an early idea, since [dropped](/wiki/predictions/early-universe-step), that its conjugate gravity sector would leave a step in the primordial gravitational-wave background.*

**Status:** Established — [T] — textbook physics, written here from general knowledge; references the wiki adds are from model memory (†). The retired candidate's frequency band was recomputed by the referee of [review round 3](/wiki/method/review/round-3), and its corrected upper end, 3.2×10⁷ Hz, is a [V] check in `verify/soliton_obituary.py` ([the soliton-obituary script](/wiki/method/verification/soliton-obituary-script)); the band itself died with the candidate. The program's own spectral step was dropped and is not machine-checked.

## First-order transitions [T]

### Crossover, continuous and first order

As the early universe cools, the equilibrium state of a field can change, for example when a symmetry breaks and the field acquires a nonzero value. How it changes matters here [T]:

- In a **crossover** or a **continuous** transition, the field moves smoothly from one state to the other everywhere at once. No latent heat is released, and the plasma is not stirred.
- In a **first-order** transition, the old and new states are separated by a barrier. Below the critical temperature the old state survives as a metastable phase, and the new phase appears only where a bubble nucleates, by thermal activation over the barrier or quantum tunnelling through it. Bubbles expand, collide and merge until the new phase fills space, and the latent heat goes into the plasma and into the motion of the bubble walls.

The Standard Model's own transitions, the electroweak and the strong-interaction ones, are crossovers according to lattice calculations [T]. A first-order transition in the early universe therefore needs physics beyond the Standard Model, such as a hidden sector.

### The parameters

Four quantities describe a first-order transition for this purpose [T]:

- **T\***, the temperature of the plasma when the transition takes place;
- **β**, the rate at which the bubble-nucleation rate grows, so that 1/β is the duration of the transition. It is quoted in units of the Hubble rate at the time, β/H\*: a large value means a short transition with many small bubbles;
- **the strength**, the energy the transition releases compared with the radiation energy density;
- **the wall speed**, how fast the bubbles expand.

The number of bubbles that form in one Hubble volume grows as (β/H\*)³. Since each bubble picks its vacuum independently, this number also controls how many topological defects a first-order transition leaves, on top of the minimum that [the Kibble mechanism](/wiki/electric-magnetic-duality/monopoles/kibble-mechanism) guarantees. The round-3 referee's estimate, as coded: "first-order transition: bubbles per Hubble volume ~ (beta/H)^3 -> p ~ 104 (beta/H)^3" (`review/round3/referee/step4.py`), with `step4.out` printing p ~ 1.0e+02, 1.0e+05 and 1.0e+08 for β/H = 1, 10 and 100. Here p is the normalization of the defect yield n/s = p (T_c/M_Pl)³ ([Obituary: the Kibble normalization](/wiki/dark-matter/candidates/soliton-candidate/kibble-normalization)).

## How the waves are made [T]

Gravitational radiation needs a source whose mass distribution is not spherically symmetric and changes in time, an anisotropic stress. A single expanding spherical bubble has none; the collisions between bubbles break the symmetry. Three sources contribute [T]:

- **Bubble-wall collisions.** The gradient energy of the field in the walls is released where walls meet.
- **Sound waves in the plasma.** The expanding walls push the surrounding plasma and set up compression waves, which keep sourcing gravitational waves long after the walls have collided. In a transition inside a thermal plasma this is usually the largest source.
- **Turbulence.** Part of the plasma motion becomes magnetohydrodynamic turbulence, which adds a smaller, broader component.

Each source produces a spectrum with one broad peak, near the inverse of the typical bubble size at the time of the transition. Because the bubble size is set by the duration, the peak frequency at emission, f\*, is of the order of β; in Hubble units, f\*/H\* is of the order of β/H\* [T]. The waves from many uncorrelated collisions add up to a stochastic background, random in phase and arriving from all directions.

A crossover has no bubbles and no latent heat, so it leaves no such signal [T]. #14 §4: "A crossover transition leaves no such signal."

## Redshifting the peak to today [T]

After emission the waves travel freely, and their frequency falls as 1/a with the expansion, like the frequency of light. Today's peak frequency is the emitted one times the ratio of scale factors, f₀ = f\* · a\*/a₀. Two radiation-era relations fix that ratio ([the radiation era](/wiki/cosmology/early-universe/radiation-era)):

- entropy conservation, g\*s T³ a³ = constant, gives a\*/a₀ in terms of today's temperature, the temperature T\* and the counts of relativistic degrees of freedom then and now;
- the expansion rate at the transition is H\* = 1.66√g\* T\*²/M_Pl, so writing f\* = (f\*/H\*)·H\* turns the emitted frequency into a multiple of a quantity fixed by T\*.

Combining the two, the T\*² of the expansion rate and the 1/T\* of the redshift leave one power of T\*, and the √g\* of the expansion rate and the g\*^{−1/3} of the redshift leave a weak g\*^{1/6} [T]. The round-3 referee's script (`review/round3/referee/step2a.py`) and `verify/soliton_obituary.py` both code the standard numerical form:

```text
f₀ = 1.65×10⁻⁵ Hz × (f*/H*) × (T*/100 GeV) × (g*/100)^{1/6}
```

The coefficient is the frequency today of a wave emitted at one Hubble rate (f\*/H\* = 1) by a transition at T\* = 100 GeV with g\* = 100. The formula says three things. The frequency today is proportional to the transition temperature, so each factor of ten in T\* is a factor of ten in f₀. It is proportional to f\*/H\*, so a short transition with small bubbles peaks higher. And it hardly depends on the particle content.

## The amplitude [T]

The strength of the signal is usually quoted as Ω_gw, the energy density of the waves per logarithmic frequency interval as a fraction of the critical density. It grows with the square of the fraction of the total energy density that the transition puts into bulk motion of the plasma and the walls, and it falls as the transition gets shorter (larger β/H\*), because the source then acts for less time and on smaller scales [T]. After emission the waves dilute like radiation, so their share of the radiation density stays fixed apart from changes in the number of relativistic species [T].

A transition in a sector that holds only part of the energy density can put at most that part into motion. For a hidden sector colder than ours by the temperature ratio ξ, that share falls roughly as ξ⁴ when it is small [T]. #14 §4: "The amplitude is suppressed by the hidden sector's share of the energy density at the transition, which is small for xi < 0.77."

## Primordial backgrounds [T]

The primordial gravitational-wave background is the background left by the earliest epochs, above all by inflation [T]. During [inflation](/wiki/cosmology/early-universe/inflation-and-dilution), quantum fluctuations of the metric are stretched to cosmic size, giving waves over an enormous range of wavelengths with nearly equal power in each decade. A wave longer than the Hubble length stays frozen; once the Hubble length grows past it, the wave re-enters, oscillates, and from then on redshifts like radiation. Each frequency observed today therefore corresponds to the epoch at which its wave re-entered, and the spectrum today maps the expansion history [T]. A change in the expansion rate at some epoch, from extra radiation, a change in the number of relativistic species, a stiff era or a change in the effective strength of gravity, shows up as a step or a change of slope at the frequencies whose waves re-entered at that time [T]. Phase transitions and cosmic strings add further stochastic backgrounds of their own.

This is the sense of the spectral step in the [lab notebook](/wiki/history/documents/lab-notebook) ([the dropped spectral step](#the-dropped-spectral-step-row-10) below).

## Where the program met it

### The retired candidate's hidden transition

The withdrawn manuscript [#14](/wiki/dark-matter/candidates/soliton-candidate) placed its superheavy [monopoles](/wiki/electric-magnetic-duality/monopoles/thooft-polyakov-monopole) in a [hidden SU(2) sector broken to U(1)](/wiki/dark-matter/candidates/soliton-candidate/hidden-sector) at a scale v, "v ~ (0.8-1.4)e12 GeV" at its benchmark (#14 §3). If that symmetry breaking were first order, it would leave a background (#14 §4):

> If the hidden transition is first order, it sources a stochastic gravitational-wave background with a present-day peak frequency of ~1e5 to 1e7 Hz for f\*/H\* = 1-100. That is above the LIGO band, in the unconstrained ultra-high-frequency window targeted by proposed detectors.

LIGO is the Laser Interferometer Gravitational-Wave Observatory, a ground-based detector. The candidate, and with it this band, is dead ([Obituary: superheavy conjugate solitons](/wiki/dark-matter/candidates/soliton-candidate/obituary)); the numbers below are kept as the record of the soliton episode.

**The referee's recomputation.** The round-3 referee evaluated the formula above at T\* = v for the two ends of v3's range of v, 8.09×10¹¹ and 1.45×10¹² GeV, at f\*/H\* = 1 and 100, and at g\* = 106.75 and 122.75, the visible count without and with the hidden sector's 16 effective degrees of freedom added (`step2a.py`). The output runs from "f0 = 1.35e+05 Hz" to "f0 = 2.47e+07 Hz" (`step2a.out`), and the audit table records the band "1.35e5 - 2.47e7 Hz" against v3's "1e5 - 1e7 Hz" as "CONFIRMED" (`review/round3/referee/audit-notes.md`, Step 2).

**Ruling 5's knock-on.** Round 3 corrected the bound on the hidden temperature ratio from ξ < 0.77 to ξ < 0.760 ([the hidden sector's thermal history](/wiki/dark-matter/candidates/soliton-candidate/hidden-thermal-history)). [Ruling 5](/wiki/method/review/round-3/rulings) notes the knock-on for the upper end of the band, 3.2×10⁷ Hz, and the script checks it at the withdrawn benchmark, taking T\* = v/ξ with v at the top of v3's range and ξ at the bound, f\*/H\* = 100 and g\* = 106.75:

```text
== Dark radiation (ruling 5)
PASS  knock-on: GW upper end 3.2e7 Hz at the withdrawn benchmark  [3.17e+07]
```

The two upper ends, 2.47×10⁷ and 3.2×10⁷ Hz, differ in the transition temperature: the referee used T\* = v, and the script, which reproduces the adjudication's figure, T\* = v/ξ. They also differ slightly in g\*: the referee's 2.47×10⁷ is at g\* = 122.75, and at g\* = 106.75 the same T\* and f\*/H\* give "f0 = 2.41e+07 Hz" (`step2a.out`). The adjudication's value governs. The division by ξ has a plain reading (the wiki's): the hidden transition happens when the hidden plasma is at about v, and a hidden sector colder by ξ reaches that temperature when the visible plasma, which carries most of the energy and sets the redshift, is at v/ξ. The referee used the same relation for the reheating temperature the candidate needed ([inflation, reheating and entropy dilution](/wiki/cosmology/early-universe/inflation-and-dilution)).

**The amplitude.** #14 noted that the signal is suppressed by the hidden sector's small share of the energy density at ξ < 0.77 (quoted above). #14 gave no amplitude, and the round-3 record contains none.

**A conflict with the manuscript's own abundance.** The first-order case also bears on the count of monopoles. The referee observed that #14 §4 considers a first-order transition with f\*/H\* = 1–100, while bubble counting at such a transition "gives p ~ 104 (beta/H)^3 = 1e2-1e8" (Step 4(a) item 2). That is "flatly inconsistent" with §3's treatment of p = 1 as the upper end of the Kibble yield; a first-order hidden transition would have made far more monopoles than #14 assumed ([Obituary: the Kibble normalization](/wiki/dark-matter/candidates/soliton-candidate/kibble-normalization); [overproduction at the benchmark](/wiki/dark-matter/candidates/soliton-candidate/overproduction)).

### The dropped spectral step (row 10)

The lab notebook's minisuperspace calculation adds the program's dual gravitational term to the Friedmann equation, 3H²(M_P² + M̃²a⁻⁶) = ρ, a term that grows toward the past as a⁻⁶ and so changes the effective strength of gravity only at early times ([Friedmann cosmology and minisuperspace](/wiki/cosmology/scale-factor-duality/friedmann-cosmology)). The notebook drew two consequences: the term "predicts a step in" G_eff "before BBN and, conditionally on its one knob, a spectral step in the primordial gravitational-wave background. **[D]**" (#1 §6), where BBN is [Big Bang nucleosynthesis](/wiki/cosmology/early-universe/big-bang-nucleosynthesis#row-10-a-step-in-g_eff-before-bbn). The notebook does not name the knob; the a⁻⁶ term has one free coefficient, the [dual Planck mass](/wiki/gravity/spin-2-fields/planck-units#where-a-document-states-no-convention) M̃ (the wiki's reading). Its row 10 listed a conditional step in the primordial gravitational-wave spectrum among the requirements (#1 §9), and its parameter table counts a gravitational-wave step among the phenomena of the optional geometric parameters M̃ and k̃ (#1 §10).

The notebook states the step without deriving its size or position. The mechanism it implies is the one above (the wiki's reading): waves that re-entered the Hubble length while the a⁻⁶ term changed the expansion rate would have re-entered under a different relation between the expansion rate and the energy density from those that re-entered later, and the spectrum today would change level between the two ranges of frequency.

Version 1 of the [checkpoint](/wiki/history/documents/checkpoint) dropped the spectral step. Its dictionary calls the a⁻⁶ step "an optional early-universe fingerprint" (#9 §8), and its row 10 lists only the G_eff step and the negative ΔN_eff (#9 §9). #11 keeps that form: "Optional a⁻⁶ G_eff step; closed dual curvature ⇒ negative ΔN_eff", with "(Knob-bounded; CMB-S4 probes)" (#11 §13 row 10), where CMB-S4 is a proposed experiment on the [cosmic microwave background](/wiki/cosmology/early-universe/cosmic-microwave-background#row-10s-probe-cmb-s4) (CMB); whether it is still going ahead is unchecked (flag 32 in `review/wiki-build-flags.md`). The documents give no reason for the drop. See [row 10: an early step in G_eff](/wiki/predictions/early-universe-step) and [the history of the predictions table](/wiki/predictions/table-history).

## Standard references

- M. Kamionkowski, A. Kosowsky, M. S. Turner, Phys. Rev. D 49, 2837 (1994) †: gravitational radiation from first-order transitions and the redshifted peak frequency in the form coded above.
- M. Hindmarsh, S. J. Huber, K. Rummukainen, D. J. Weir, Phys. Rev. Lett. 112, 041301 (2014) †: sound waves as the dominant source in a thermal plasma.
- C. Caprini et al., JCAP 04 (2016) 001 †: a review of the signal from first-order transitions and its detectability.
- A. A. Starobinsky, JETP Lett. 30, 682 (1979) †: the gravitational-wave background from an early [de Sitter](/wiki/cosmology/dark-energy/de-sitter-space) stage, the primordial background.
- E. W. Kolb, M. S. Turner, *The Early Universe* (Addison-Wesley, 1990): #14's reference [17], for the radiation-era relations used in the redshift.

The † entries are from model memory and unverified; none is cited in the program's documents.

## Used by

- [The hidden sector's thermal history](/wiki/dark-matter/candidates/soliton-candidate/hidden-thermal-history) — the band a first-order hidden transition would leave, and its corrected upper end.
- [Obituary: the Kibble normalization](/wiki/dark-matter/candidates/soliton-candidate/kibble-normalization) — bubble counting in a first-order transition.
- [Overproduction at the benchmark](/wiki/dark-matter/candidates/soliton-candidate/overproduction) — a first-order hidden transition would raise the monopole yield further.
- [The duality dictionary w_eff = −w̃](/wiki/cosmology/scale-factor-duality/duality-dictionary) — the lab notebook's spectral step in the primordial background, dropped in v1.
- [Row 10: an early step in G_eff](/wiki/predictions/early-universe-step) — the lab notebook's form of the row included the dropped spectral step.
- [Inflation, reheating and entropy dilution](/wiki/cosmology/early-universe/inflation-and-dilution) — the primordial background from inflation.

## Sources

- `review/round3-adjudication.md` 'Rulings' 5 — the corrected bound on ξ and the upper end of the band
- `verify/soliton_obituary.py` 'Dark radiation (ruling 5)' — the peak-frequency formula as coded and the executed upper end
- `review/round3/referee/audit-notes.md` Step 2 — the recomputed band, confirmed; Step 4(a) item 2 — bubble counting against v3's p = 1
- `review/round3/referee/step2a.py`, `review/round3/referee/step2a.out` — the referee's peak-frequency inputs and outputs
- `review/round3/referee/step4.py`, `review/round3/referee/step4.out` — p ~ 104 (β/H)³ for a first-order transition
- `notes/knot-dark-matter-standalone.md` §3, §4 — the withdrawn candidate's p bracket, band, amplitude remark and crossover remark (withdrawn)
- `notes/broken-born-theory.md` §6, §9 row 10, §10 — the spectral step [D], the lab notebook's row 10 and its parameter table
- `notes/broken-born-program-v1.md` §8, §9 row 10 — the step dropped in v1
- `papers/broken-born-checkpoint-v2.md` §13 row 10 — the current row, without it
- `review/wiki-build-flags.md` item 32 — CMB-S4's status, unchecked
