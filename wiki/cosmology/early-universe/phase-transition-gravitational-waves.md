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
  - "wiki/papers/broken-born-checkpoint-v2.md §13 row 10"
  - "review/wiki-build-flags.md item 32"
  - "notes/closed-universe.md §7"
  - "review/wiki-build-flags.md item 49"
---

*A first-order phase transition in the early universe proceeds by bubbles of the new phase forming, growing and colliding, much as water boils, and the collisions and the sound waves they leave in the plasma produce gravitational waves that arrive today from every direction as a random background. The waves' characteristic frequency is set at the transition by its temperature and duration and has been stretched by the expansion ever since, so a transition at a higher temperature leaves a higher frequency today. A related background, the primordial one, comes from [inflation](inflation-and-dilution.md), and its spectrum records how fast the universe expanded at each early epoch. The program met this physics in two places. One is the transition of the [hidden sector](../../dark-matter/candidates/soliton-candidate/hidden-sector.md) in [#14](../../../notes/knot-dark-matter-standalone.md)'s [model of its soliton dark-matter candidate](../../dark-matter/candidates/soliton-candidate/obituary.md), a model that failed; the transition's signal would have lain far above the frequencies of current detectors. The other is an early idea, since [dropped](../../predictions/early-universe-step.md), that the program's conjugate gravity sector would leave a step in the primordial gravitational-wave background.*

**Status:** Established — [T] — textbook physics, written here from general knowledge; references the wiki adds are from model memory (†). The frequency band of #14's model was recomputed by the referee of [review round 3](../../method/review/round-3/_index.md), and its corrected upper end, 3.2×10⁷ Hz, is a [V] check in [`verify/soliton_obituary.py`](../../../verify/soliton_obituary.py) ([the soliton-obituary script](../../method/verification/soliton-obituary-script.md)); the band itself died with the model. The program's own spectral step was dropped and is not machine-checked.

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

The number of bubbles that form in one Hubble volume grows as (β/H\*)³. Since each bubble picks its vacuum independently, this number also controls how many [topological defects](../../symmetry-breaking/topological-defects.md) a first-order transition leaves, on top of the minimum that [the Kibble mechanism](../../electric-magnetic-duality/monopoles/kibble-mechanism.md) guarantees. The round-3 referee's estimate, as coded: "first-order transition: bubbles per Hubble volume ~ (beta/H)^3 -> p ~ 104 (beta/H)^3" ([`review/round3/referee/step4.py`](../../../review/round3/referee/step4.py)), with `step4.out` printing p ~ 1.0e+02, 1.0e+05 and 1.0e+08 for β/H = 1, 10 and 100. Here p is the normalization of the defect [yield](relic-yield-and-dilution.md#the-kibble-yield-t) n/s = p (T_c/M_Pl)³ ([Under review: the Kibble normalization](../../dark-matter/candidates/soliton-candidate/kibble-normalization.md)).

## How the waves are made [T]

Gravitational radiation needs a source whose mass distribution is not spherically symmetric and changes in time, an anisotropic stress. A single expanding spherical bubble has none; the collisions between bubbles break the symmetry. Three sources contribute [T]:

- **Bubble-wall collisions.** The gradient energy of the field in the walls is released where walls meet.
- **Sound waves in the plasma.** The expanding walls push the surrounding plasma and set up compression waves, which keep sourcing gravitational waves long after the walls have collided. In a transition inside a thermal plasma this is usually the largest source.
- **Turbulence.** Part of the plasma motion becomes magnetohydrodynamic turbulence, which adds a smaller, broader component.

Each source produces a spectrum with one broad peak, near the inverse of the typical bubble size at the time of the transition. Because the bubble size is set by the duration, the peak frequency at emission, f\*, is of the order of β; in Hubble units, f\*/H\* is of the order of β/H\* [T]. The waves from many uncorrelated collisions add up to a stochastic background, random in phase and arriving from all directions.

A crossover has no bubbles and no latent heat, so it leaves no such signal [T]. [#14 §4](../../../notes/knot-dark-matter-standalone.md#4-observational-consistency): "A crossover transition leaves no such signal."

## Redshifting the peak to today [T]

After emission the waves travel freely, and their frequency falls as 1/a with the expansion, like the frequency of light. Today's peak frequency is the emitted one times the ratio of scale factors, f₀ = f\* · a\*/a₀. Two radiation-era relations fix that ratio ([the radiation era](radiation-era.md)):

- entropy conservation, g\*s T³ a³ = constant, gives a\*/a₀ in terms of today's temperature, the temperature T\* and the counts of relativistic degrees of freedom then and now;
- the expansion rate at the transition is H\* = 1.66√g\* T\*²/M_Pl, so writing f\* = (f\*/H\*)·H\* turns the emitted frequency into a multiple of a quantity fixed by T\*.

Combining the two, the T\*² of the expansion rate and the 1/T\* of the [redshift](../scale-factor-duality/redshift.md) leave one power of T\*, and the √g\* of the expansion rate and the g\*^{−1/3} of the redshift leave a weak g\*^{1/6} [T]. The round-3 referee's script ([`review/round3/referee/step2a.py`](../../../review/round3/referee/step2a.py)) and [`verify/soliton_obituary.py`](../../../verify/soliton_obituary.py) both code the standard numerical form:

```text
f₀ = 1.65×10⁻⁵ Hz × (f*/H*) × (T*/100 GeV) × (g*/100)^{1/6}
```

The coefficient is the frequency today of a wave emitted at one Hubble rate (f\*/H\* = 1) by a transition at T\* = 100 GeV with g\* = 100. The formula says three things. The frequency today is proportional to the transition temperature, so each factor of ten in T\* is a factor of ten in f₀. It is proportional to f\*/H\*, so a short transition with small bubbles peaks higher. And it hardly depends on the particle content.

## The amplitude [T]

The strength of the signal is usually quoted as Ω_gw, the energy density of the waves per logarithmic frequency interval as a fraction of the critical density. It grows with the square of the fraction of the total energy density that the transition puts into bulk motion of the plasma and the walls, and it falls as the transition gets shorter (larger β/H\*), because the source then acts for less time and on smaller scales [T]. After emission the waves dilute like radiation, so their share of the radiation density stays fixed apart from changes in the number of relativistic species [T].

A transition in a sector that holds only part of the energy density can put at most that part into motion. For a hidden sector colder than ours by the [temperature ratio](hidden-sector-temperature.md) ξ, that share falls roughly as ξ⁴ when it is small [T]. [#14 §4](../../../notes/knot-dark-matter-standalone.md#4-observational-consistency): "The amplitude is suppressed by the hidden sector's share of the energy density at the transition, which is small for xi < 0.77."

## Primordial backgrounds [T]

The primordial gravitational-wave background is the background left by the earliest epochs, above all by inflation [T]. During [inflation](inflation-and-dilution.md), quantum fluctuations of the metric are stretched to cosmic size, giving waves over an enormous range of wavelengths with nearly equal power in each decade. A wave longer than the Hubble length stays frozen; once the Hubble length grows past it, the wave re-enters, oscillates, and from then on redshifts like radiation. Each frequency observed today therefore corresponds to the epoch at which its wave re-entered, and the spectrum today maps the expansion history [T]. A change in the expansion rate at some epoch, from extra radiation, a change in the number of relativistic species, a stiff era or a change in the effective strength of gravity, shows up as a step or a change of slope at the frequencies whose waves re-entered at that time [T]. Phase transitions and cosmic strings add further stochastic backgrounds of their own.

This is the sense of the spectral step in the [lab notebook](../../history/documents/lab-notebook.md) ([the dropped spectral step](#the-dropped-spectral-step-row-10) below).

## Where the program met it

### The hidden transition of #14's model

The withdrawn manuscript [#14](../../dark-matter/candidates/soliton-candidate/_index.md) placed its superheavy [monopoles](../../electric-magnetic-duality/monopoles/thooft-polyakov-monopole.md) in a [hidden SU(2) sector broken to U(1)](../../dark-matter/candidates/soliton-candidate/hidden-sector.md) at a scale v, "v ~ (0.8-1.4)e12 GeV" at its benchmark ([#14 §3](../../../notes/knot-dark-matter-standalone.md#3-the-candidate)). If that symmetry breaking were first order, it would leave a background ([#14 §4](../../../notes/knot-dark-matter-standalone.md#4-observational-consistency)):

> If the hidden transition is first order, it sources a stochastic gravitational-wave background with a present-day peak frequency of ~1e5 to 1e7 Hz for f\*/H\* = 1-100. That is above the LIGO band, in the unconstrained ultra-high-frequency window targeted by proposed detectors.

LIGO is the Laser Interferometer Gravitational-Wave Observatory, a ground-based detector. #14's model failed, and this band died with it ([Obituary: #14's superheavy-soliton model](../../dark-matter/candidates/soliton-candidate/obituary.md)); the numbers below are kept as the model's record.

**The referee's recomputation.** The round-3 referee evaluated the formula above at T\* = v for the two ends of v3's range of v, 8.09×10¹¹ and 1.45×10¹² GeV, at f\*/H\* = 1 and 100, and at g\* = 106.75 and 122.75, the visible count without and with the hidden sector's 16 effective degrees of freedom added (`step2a.py`). The output runs from "f0 = 1.35e+05 Hz" to "f0 = 2.47e+07 Hz" (`step2a.out`), and the audit table records the band "1.35e5 - 2.47e7 Hz" against v3's "1e5 - 1e7 Hz" as "CONFIRMED" ([`review/round3/referee/audit-notes.md`](../../../review/round3/referee/audit-notes.md), Step 2).

**Ruling 5's knock-on.** Round 3 corrected the bound on the hidden temperature ratio from ξ < 0.77 to ξ < 0.760 ([the hidden sector's thermal history](../../dark-matter/candidates/soliton-candidate/hidden-thermal-history.md)). [Ruling 5](../../method/review/round-3/rulings.md) notes the knock-on for the upper end of the band, 3.2×10⁷ Hz, and the script checks it at the withdrawn benchmark, taking T\* = v/ξ with v at the top of v3's range and ξ at the bound, f\*/H\* = 100 and g\* = 106.75:

```text
== Dark radiation (ruling 5)
PASS  knock-on: GW upper end 3.2e7 Hz at the withdrawn benchmark  [3.17e+07]
```

The two upper ends, 2.47×10⁷ and 3.2×10⁷ Hz, differ in the transition temperature: the referee used T\* = v, and the script, which reproduces the adjudication's figure, T\* = v/ξ. They also differ slightly in g\*: the referee's 2.47×10⁷ is at g\* = 122.75, and at g\* = 106.75 the same T\* and f\*/H\* give "f0 = 2.41e+07 Hz" (`step2a.out`). The adjudication's value governs. The division by ξ has a plain reading (the wiki's): the hidden transition happens when the hidden plasma is at about v, and a hidden sector colder by ξ reaches that temperature when the visible plasma, which carries most of the energy and sets the redshift, is at v/ξ. The referee used the same relation for the reheating temperature #14's model needed ([inflation, reheating and entropy dilution](inflation-and-dilution.md)).

**The amplitude.** #14 noted that the signal is suppressed by the hidden sector's small share of the energy density at ξ < 0.77 (quoted above). #14 gave no amplitude, and the round-3 record contains none.

**A conflict with the manuscript's own abundance.** The first-order case also bears on the count of monopoles. The referee observed that [#14 §4](../../../notes/knot-dark-matter-standalone.md#4-observational-consistency) considers a first-order transition with f\*/H\* = 1–100, while bubble counting at such a transition "gives p ~ 104 (beta/H)^3 = 1e2-1e8" (Step 4(a) item 2). That is "flatly inconsistent" with [§3](../../../notes/knot-dark-matter-standalone.md#3-the-candidate)'s treatment of p = 1 as the upper end of the Kibble yield; a first-order hidden transition would have made far more monopoles than #14 assumed ([Under review: the Kibble normalization](../../dark-matter/candidates/soliton-candidate/kibble-normalization.md); [overproduction at the benchmark](../../dark-matter/candidates/soliton-candidate/overproduction.md)).

### The dropped spectral step (row 10)

The lab notebook's minisuperspace calculation adds the program's dual gravitational term to the Friedmann equation, 3H²(M_P² + M̃²a⁻⁶) = ρ, a term that grows toward the past as a⁻⁶ and so changes the effective strength of gravity only at early times ([Friedmann cosmology and minisuperspace](../scale-factor-duality/friedmann-cosmology.md)). The notebook drew two consequences: the term "predicts a step in" G_eff "before BBN and, conditionally on its one knob, a spectral step in the primordial gravitational-wave background. **[D]**" ([#1 §6](../../../notes/broken-born-theory.md#6-cosmology-i-the-constraint-and-the-corrected-dictionary)), where BBN is [Big Bang nucleosynthesis](big-bang-nucleosynthesis.md#row-10-a-step-in-g_eff-before-bbn). The notebook does not name the knob; the a⁻⁶ term has one free coefficient, the [dual Planck mass](../../gravity/spin-2-fields/planck-units.md#where-a-document-states-no-convention) M̃ (the wiki's reading). Its row 10 listed a conditional step in the primordial gravitational-wave spectrum among the requirements ([#1 §9](../../../notes/broken-born-theory.md#9-predictions)), and its parameter table counts a gravitational-wave step among the phenomena of the optional geometric parameters M̃ and k̃ ([#1 §10](../../../notes/broken-born-theory.md#10-parameter-count)).

The notebook states the step without deriving its size or position. The dual Einstein–Hilbert term behind the a⁻⁶ step is used in [#1 §6](../../../notes/broken-born-theory.md#6-cosmology-i-the-constraint-and-the-corrected-dictionary) under a [D] tag but derived from the geometric action in no document, so the step tests a postulate (flag 49 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md); [the dual frame](../scale-factor-duality/closed-universe.md#the-dual-frame-what-closure-fixes-and-what-it-does-not)). The mechanism it implies is the one above (the wiki's reading): waves that re-entered the Hubble length while the a⁻⁶ term changed the expansion rate would have re-entered under a different relation between the expansion rate and the energy density from those that re-entered later, and the spectrum today would change level between the two ranges of frequency.

Version 1 of the [checkpoint](../../history/documents/checkpoint.md) dropped the spectral step. Its dictionary calls the a⁻⁶ step "an optional early-universe fingerprint" ([#9 §8](../../../notes/broken-born-program-v1.md#8-cosmology)), and its row 10 lists only the G_eff step and the negative ΔN_eff ([#9 §9](../../../notes/broken-born-program-v1.md#9-predictions-and-kill-conditions)). [#11](../../papers/broken-born-checkpoint-v2.md) keeps that form: "Optional a⁻⁶ G_eff step; closed dual curvature ⇒ negative ΔN_eff", with "(Knob-bounded; CMB-S4 probes)" ([#11 §13 row 10](../../papers/broken-born-checkpoint-v2.md#13-predictions-and-kill-conditions)), where CMB-S4 is a proposed experiment on the [cosmic microwave background](cosmic-microwave-background.md#row-10s-probe-cmb-s4) (CMB); whether it is still going ahead is unchecked (flag 32 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md)). The documents give no reason for the drop. See [row 10: an early step in G_eff](../../predictions/early-universe-step.md) and [the history of the predictions table](../../predictions/table-history.md).

## Standard references

- M. Kamionkowski, A. Kosowsky, M. S. Turner, Phys. Rev. D 49, 2837 (1994) †: gravitational radiation from first-order transitions and the redshifted peak frequency in the form coded above.
- M. Hindmarsh, S. J. Huber, K. Rummukainen, D. J. Weir, Phys. Rev. Lett. 112, 041301 (2014) †: sound waves as the dominant source in a thermal plasma.
- C. Caprini et al., JCAP 04 (2016) 001 †: a review of the signal from first-order transitions and its detectability.
- A. A. Starobinsky, JETP Lett. 30, 682 (1979) †: the gravitational-wave background from an early [de Sitter](../dark-energy/de-sitter-space.md) stage, the primordial background.
- E. W. Kolb, M. S. Turner, *The Early Universe* (Addison-Wesley, 1990): #14's reference [17], for the radiation-era relations used in the redshift.

The † entries are from model memory and unverified; none is cited in the program's documents.

## Used by

- [The hidden sector's thermal history](../../dark-matter/candidates/soliton-candidate/hidden-thermal-history.md) — the band a first-order hidden transition would leave, and its corrected upper end.
- [Under review: the Kibble normalization](../../dark-matter/candidates/soliton-candidate/kibble-normalization.md) — bubble counting in a first-order transition.
- [Overproduction at the benchmark](../../dark-matter/candidates/soliton-candidate/overproduction.md) — a first-order hidden transition would raise the monopole yield further.
- [The duality dictionary w_eff = −w̃](../scale-factor-duality/duality-dictionary.md) — the lab notebook's spectral step in the primordial background, dropped in v1. Here w̃ is the ratio of pressure to energy density, or [equation of state](../dark-energy/quintessence.md#dark-energy-and-the-equation-of-state), of a fluid in the [conjugate universe](../../program/conjugate-universe.md), the momentum-space description of our universe; w_eff is the equation of state with which that fluid acts on our expansion.
- [Row 10: an early step in G_eff](../../predictions/early-universe-step.md) — the lab notebook's form of the row included the dropped spectral step.
- [Inflation, reheating and entropy dilution](inflation-and-dilution.md) — the primordial background from inflation.

## Sources

- [`review/round3-adjudication.md`](../../../review/round3-adjudication.md) 'Rulings' 5 — the corrected bound on ξ and the upper end of the band
- [`verify/soliton_obituary.py`](../../../verify/soliton_obituary.py) 'Dark radiation (ruling 5)' — the peak-frequency formula as coded and the executed upper end
- [`review/round3/referee/audit-notes.md`](../../../review/round3/referee/audit-notes.md) Step 2 — the recomputed band, confirmed; Step 4(a) item 2 — bubble counting against v3's p = 1
- [`review/round3/referee/step2a.py`](../../../review/round3/referee/step2a.py), [`review/round3/referee/step2a.out`](../../../review/round3/referee/step2a.out) — the referee's peak-frequency inputs and outputs
- [`review/round3/referee/step4.py`](../../../review/round3/referee/step4.py), [`review/round3/referee/step4.out`](../../../review/round3/referee/step4.out) — p ~ 104 (β/H)³ for a first-order transition
- [`notes/knot-dark-matter-standalone.md` §3](../../../notes/knot-dark-matter-standalone.md#3-the-candidate), [§4](../../../notes/knot-dark-matter-standalone.md#4-observational-consistency) — the p bracket, band, amplitude remark and crossover remark of #14's model (withdrawn manuscript)
- [`notes/broken-born-theory.md` §6](../../../notes/broken-born-theory.md#6-cosmology-i-the-constraint-and-the-corrected-dictionary), [§9 row 10](../../../notes/broken-born-theory.md#9-predictions), [§10](../../../notes/broken-born-theory.md#10-parameter-count) — the spectral step [D], the lab notebook's row 10 and its parameter table
- [`notes/broken-born-program-v1.md` §8](../../../notes/broken-born-program-v1.md#8-cosmology), [§9 row 10](../../../notes/broken-born-program-v1.md#9-predictions-and-kill-conditions) — the step dropped in v1
- [`wiki/papers/broken-born-checkpoint-v2.md` §13 row 10](../../papers/broken-born-checkpoint-v2.md#13-predictions-and-kill-conditions) — the current row, without it
- [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md) item 32 — CMB-S4's status, unchecked
- [`notes/closed-universe.md` §7](../../../notes/closed-universe.md#7-the-dual-frame-what-closure-fixes-and-what-it-does-not); [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md) item 49 — the dual Einstein–Hilbert term behind the a⁻⁶ step is not derived
