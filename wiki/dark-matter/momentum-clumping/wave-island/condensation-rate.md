---
title: "The gated condensation rate Γ_self"
weight: 10
status: alive
description: "Γ_self ≈ c g²ρ² min(σ, v*)⁴/(m³σ⁶), suppressed by a power law when the gate is narrow, raced against the gravitational floor and orbital stirring; its coefficient awaits calibration against Levkov–Panin–Tkachev."
provenance: [D, T, O]
sources:
  - "notes/debt3b-wave-island.md 'Setup'"
  - "notes/debt3b-wave-island.md 'The rate'"
  - "notes/debt3b-wave-island.md 'What pins g? Two scenarios'"
  - "notes/debt3b-wave-island.md 'Standing results'"
  - "papers/broken-born-checkpoint-v2.md §9"
  - "papers/broken-born-checkpoint-v2.md §8"
  - "papers/broken-born-checkpoint-v2.md §13"
  - "papers/broken-born-checkpoint-v2.md §14 item 10"
  - "papers/broken-born-checkpoint-v2.md ref [13]"
  - "notes/debt3a-stream-stability.md 'Setup'"
  - "notes/debt3a-stream-stability.md 'Limit 1 (broad gate)'"
  - "notes/debt3a-stream-stability.md 'Limit 2 (narrow gate)'"
  - "notes/debt3a-stream-stability.md 'Consequences for the predictions table'"
  - "notes/debt3a-stream-stability.md 'Next chunk (3b)'"
  - "notes/debt3c-ufd-endpoint.md 'Sharpened input numbers'"
  - "notes/broken-born-program-v1.md §7"
  - "notes/broken-born-program-v1.md §10"
  - "notes/broken-born-theory.md §11"
  - "notes/broken-born-theory.md 'Addendum (v0.2)'"
  - "HANDOFF.md §3"
---

*Γ_self is the rate at which the gated attraction of [conjugate matter](/wiki/dark-matter/conjugate-matter) makes a wave-like dark-matter halo condense: the rate at which the halo's waves, scattering off one another, move their power into a narrow range of low relative momenta. It applies on the [wave island](/wiki/dark-matter/momentum-clumping/wave-island), the range of very light χ masses in which each quantum state of the halo holds so many quanta that the halo is a classical wave field rather than a gas of particles. There every scattering rate is multiplied by that number of quanta. Levkov, Panin and Tkachev (LPT) worked out this kind of condensation for gravity; the gated attraction adds a second channel to it. When the halo's velocity spread is wider than the gate, the rate falls as the fourth power of their ratio, a power law rather than the exponential cutoff that particles show, and that difference became a test of whether dark matter is made of particles or waves. [Debt 3](/wiki/history/debts) compared the rate with the gravitational channel and with the stirring of the halo by its own orbits. Its form is derived; its numerical coefficient is a heuristic estimate that has not been calibrated.*

**Status:** Alive, with uncalibrated coefficients. [Debt 3b](/wiki/history/documents/debt-3-notes) tags the rate "[D, heuristic coefficients]" (`notes/debt3b-wave-island.md`); [checkpoint #11](/wiki/history/documents/checkpoint) §9 (ii) carries it inside the wave-island result tagged [D + T]: "Bose-enhanced, LPT-style [13†]; coefficients [O]". Not machine-checked; no `verify/` script covers any Debt-3 number ([the iron rule](/wiki/method/verification/iron-rule)). Two items on this page are open and not itemized in #11 §14: the [calibration of the coefficient c](#open-calibration-of-the-coefficient-c) and the [restatement of rows 1 and 2 in wave language](#open-rows-1-and-2-in-wave-language).

## What the rate measures

[Debt 3](/wiki/history/debts) asked whether conjugate matter χ, attracting itself only between particles of nearly equal velocity ([the velocity gate](/wiki/dark-matter/conjugate-matter/velocity-gate)), breaks a halo into velocity streams. For classical particles the answer was no: [the mean-field criterion](/wiki/dark-matter/momentum-clumping/instability-criterion) fails by 10²⁸–10³¹, and [the classicality theorem](/wiki/dark-matter/momentum-clumping/classicality-theorem) showed that the coupling needed for collective behavior is reached only at masses where χ is a wave. On that branch, `notes/debt3a-stream-stability.md` wrote, "the collective sector is reborn in field language. The halo is an incoherent wave field; the gated attraction drives condensation in k-space — power flowing into narrow-momentum streams — which is the original 'clumps in momentum space' intuition in its natural habitat" ('Consequences for the predictions table').

In the Fourier picture the halo is a superposition of waves of many momenta with random relative phases; its state is described by how much power each momentum carries. Condensation in k-space means that this spectrum narrows: power collects in a small range of momenta, and a narrow spectrum is a long, coherent waveform. Γ_self is the rate, per unit time, at which the gated attraction drives that narrowing. Debt 3a named the quantity still to be computed, Γ_cond(m, g, v\*; ρ, σ), and set the task: "Boltzmann collision integral for the field with Bose enhancement and the momentum gate", "compared to orbital stirring Ω per environment" ('Next chunk (3b)'). Debt 3b computed it under the name Γ_self.

## Background: wave kinetics with Bose enhancement [T]

When the [occupation number](/wiki/dark-matter/wave-dark-matter/occupation-number) N_occ, the number of quanta per quantum state, is much larger than one, a gas of bosons behaves as a classical field. Its waves scatter off one another through whatever interaction the field has, and a kinetic equation of Boltzmann type describes how the spectrum evolves. For bosons each scattering into an occupied state is enhanced by the occupation of that state, so the relaxation rate exceeds the particle collision rate by a factor of order N_occ [T]. Debt 3b ('Setup'):

> Wave island: m ≲ 0.1 meV, per-mode occupation N_occ = ρ/(m⁴σ³) ≫ 1. The halo is an incoherent classical field; relaxation proceeds by wave kinetics — the Boltzmann collision integral with Bose enhancement, rate Γ ~ n σ_scat v × N_occ.

Here n is the number density, σ_scat a scattering cross-section and v a relative speed: n σ_scat v is the ordinary collision rate of a particle gas, and N_occ is the Bose factor. Scatterings that conserve both the number of quanta and their energy move quanta toward the lowest-energy states, and the field condenses there into a coherent core [T] ([wave kinetics and Bose-star formation](/wiki/dark-matter/wave-dark-matter/wave-kinetics)). The note continues: "This is the mechanism LPT established for gravity (Bose condensation of virialized wave DM into solitons); here the gated contact attraction adds a channel", where DM is dark matter and a "soliton" is a Bose-star core, not the topological soliton of [the retired candidate](/wiki/dark-matter/candidates/soliton-candidate/obituary). The reference is the checkpoint's [13]†, Levkov, Panin and Tkachev's papers on gravitational Bose–Einstein condensation in the kinetic regime (2018) and on collapsing Bose stars (2017).

## The ingredients

### The gated coupling g

Debt 3b uses "Same conventions as Chunk A: σ₀ ≡ g²m²/π, gate width v\* in relative velocity" ('Setup'). In Chunk A ([the gated Vlasov model](/wiki/dark-matter/momentum-clumping/gated-vlasov-model)), g is the strength of a contact attraction whose momentum dependence is a Gaussian gate G of width μ in momentum, with "G(0)=1, attractive sign, and the x-range collapsed to contact (range 1/m_φ, microscopic)", and

```text
g ≡ 4πα̃/m_φ² = √(πσ₀/m²)
```

where α̃ is the coupling and m_φ the mediator mass of [the scattering law](/wiki/dark-matter/conjugate-matter/scattering-law), and σ₀ the low-velocity cross-section (`notes/debt3a-stream-stability.md`, 'Setup'). The gate width v\* is the same cutoff expressed in relative velocity: only pairs whose relative velocity is below about v\* interact.

### The halo

A halo region is described by its mass density ρ and its velocity dispersion σ, and χ has mass m. The occupation number N_occ = ρ/(m⁴σ³), in natural units (ℏ and the speed of light set to 1), is the number density times the cube of the de Broglie wavelength (Debt 3a, 'Corollary').

### Three substitutions

Debt 3b obtains the rate from the generic estimate by three choices ('The rate'): "With peak occupation N_occ ≈ (2π)^{3/2}ρ/(m⁴σ³), scatterer density restricted to the gate, and relative velocities min(σ, v\*)". The peak occupation is the occupation at the maximum of the velocity distribution. The note's 'Setup' writes the occupation without the factor (2π)^{3/2}, and the note does not reconcile the two forms ([occupation number](/wiki/dark-matter/wave-dark-matter/occupation-number)). "Scatterer density restricted to the gate" counts only the partners that can interact: in a halo wider than the gate, a given wave meets only the fraction of the halo moving within about v\* of it. Chunk A wrote the density of these co-movers, for its narrow-gate limit, as n_gate ≈ n(v\*/σ)³/(2π)^{3/2}, "(co-movers only)" ('Limit 2 (narrow gate)').

### Word collisions

Several symbols on this page mean something else elsewhere in the program. c is a numerical coefficient, not the speed of light. g is the gated coupling (in GeV⁻²), not the metric. ρ is a mass density, not the [Born rotation](/wiki/phase-space/reciprocity/born-reciprocity). σ is a velocity dispersion, distinct from the cross-sections σ₀ and σ_scat. G is Newton's constant here but the gate function in Debt 3a. Λ in the gravitational rate is undefined in the note and is not [the cosmological constant](/wiki/cosmology/dark-energy/cosmological-constant#the-letter-λ). Ω is the orbital stirring rate, not a density parameter Ω_χ. The [glossary](/wiki/glossary) and [notation](/wiki/notation) pages list the collisions.

## The rate

Debt 3b's result, tagged [D, heuristic coefficients] ('The rate'):

```text
Γ_self ≈ c g²ρ² min(σ, v*)⁴ / (m³σ⁶),      c = O(5–15)
```

The rate grows as the square of the coupling and the square of the density, and falls steeply with the dispersion. Its dependence on g and m runs only through the combination g²/m³, which matters when a scenario fixes the coupling ([Scenario A](/wiki/dark-matter/momentum-clumping/wave-island/scenario-a)).

### Gate open and gate narrow

The formula has two regimes, according to whether the halo's dispersion is smaller or larger than the gate (3b): "Gate-open (σ ≲ v\*): Γ ≈ c g²ρ²/(m³σ²). Gate-narrow: suppressed by (v\*/σ)⁴ — a power law, not an exponential."

- **Gate open.** When σ ≲ v\*, min(σ, v\*) = σ and most pairs in the halo are inside the gate; the rate is the full Bose-enhanced rate c g²ρ²/(m³σ²).
- **Gate narrow.** When σ > v\*, min(σ, v\*) = v\*, and the rate is the gate-open value multiplied by (v\*/σ)⁴. Debt 3a assigned the regimes by environment: the broad gate is the "dwarf regime", the narrow gate the "MW/cluster regime", where MW is the Milky Way ('Limit 1 (broad gate)', 'Limit 2 (narrow gate)').

### Where the powers come from

The note gives the result without the intermediate algebra. The following reading of the three substitutions accounts for the powers in the formula, but not for the coefficient c, and it is not written in the note. With the gate open, the generic estimate with n = ρ/m, σ_scat = σ₀ = g²m²/π, v = σ and N_occ ∝ ρ/(m⁴σ³) gives a rate proportional to g²ρ²/(m³σ²), the gate-open form. With the gate narrow, restricting the scatterers to the co-movers multiplies the rate by the factor (v\*/σ)³ of Chunk A's n_gate, up to a numerical factor, and taking the relative velocity as v\* instead of σ multiplies it by one further v\*/σ: four powers in all.

### A power law, not an exponential

For classical particles the gate acts on each two-body collision, and the self-interaction cross-section falls with the gate's tail above v\*. On the wave island, read through the substitutions above, the gate removes most partners from a hot halo but leaves the co-moving fraction, whose size falls as a power of v\*/σ. Debt 3a, before the rate was computed, put it this way: "the gate turns the effective coupling *off* in high-dispersion systems, so a cliff-analog survives as (v\*/σ)³ suppression rather than an exponential" ('Consequences for the predictions table'). Debt 3b's exponent is 4; see [the superseded estimate](#superseded-the-cubic-suppression-of-debt-3a) below.

## Corollary 1: the island discriminant

Debt 3b draws two corollaries "before any numbers". The first:

> Island discriminant. The velocity suppression of self-interaction effects is e^{−v²/v\*²} on the particle island but (v\*/σ)⁴ on the wave island. The cliff's sharpness distinguishes the islands observationally.

If the self-interaction of dark matter switches off sharply above the gate, χ is a particle ([the χ-particle candidate](/wiki/dark-matter/candidates/chi-particles)); if it fades as a power law, χ is a wave. #11 §9 lists it as salvage from Debt 3 ("knee shape: sharp cutoff ⇒ particle χ; (v\*/σ)⁴ ⇒ wave χ"), and it is [row 3 of the predictions table](/wiki/predictions/island-discriminant), a diagnostic rather than a kill condition: "Knee tail: sharp ⇒ particle; (v\*/σ)⁴ ⇒ wave" (#11 §13).

Two caveats belong to the row and are discussed there. The particle side, e^{−v²/v\*²}, is the tail of a Gaussian gate, while #11 §8 now treats the tail as open: "tail (Gaussian vs rational) diagnoses the vertex completion" ([Open: the gate shape](/wiki/dark-matter/conjugate-matter/gate-shape)). And the two laws are written in different variables, the relative velocity v of a collision on the particle side and the halo's dispersion σ on the wave side.

## Corollary 2: the gravity floor

The gated channel is not the only one. Gravity condenses a wave halo too, which is the process Levkov, Panin and Tkachev studied. Debt 3b:

> Gravity floor. The gravitational channel Γ_gr ≈ 8πG²ρ²Λ/(m³σ⁶) [T: LPT] always runs; the gated channel dominates iff g ≳ G√(8πΛ/c)/min(σ,v\*)² ~ 10⁻³¹ GeV⁻² (MW numbers) — an easy floor. For m ≫ 10⁻²⁰ eV the gravity channel is negligible on Hubble times; the gated channel is the only game.

The note does not write the step; on the wiki's reading, both rates carry the same factor ρ²/(m³σ⁶), so the comparison reduces to c g² min(σ, v\*)⁴ against 8πG²Λ, and the threshold on g follows by setting the two equal. The note does not define Λ ([wave kinetics and Bose-star formation](/wiki/dark-matter/wave-dark-matter/wave-kinetics) discusses a reading).

## The race against orbital stirring

A stream that forms in velocity space does not persist automatically. Stars and dark matter in a halo move on orbits whose periods differ, and that differential motion shears any structure in velocity space and mixes it away (phase mixing) on the dynamical time t_dyn, the time an orbit takes to cross the system, of order 1/√(Gρ) with G Newton's constant [T]. The stirring rate is Ω = 1/t_dyn.

The race has a history. [The lab notebook](/wiki/history/documents/lab-notebook) listed as its third open problem the "Stream-instability growth rate γ vs. orbital phase-mixing: determines whether Prediction 3's granularity survives in Milky-Way-like halos" (#1 §11; Prediction 3 is [velocity-space granularity](/wiki/dark-matter/momentum-clumping/velocity-granularity)). Debt 3a found that for classical particles the race never starts: "There is no race with orbital stirring below threshold — the flocking never starts. The earlier 'γ vs Ω' framing presumed growth exists; it exists only above this line." ('Limit 1 (broad gate)'; [the gated Vlasov model](/wiki/dark-matter/momentum-clumping/gated-vlasov-model)). On the wave island condensation does run at the rate Γ_self, and Debt 3b poses the race again with Γ_self in place of γ. It distinguishes two thresholds ('What pins g? Two scenarios'):

- Making [dwarf-galaxy cores](/wiki/dark-matter/halo-astrophysics/dwarf-galaxies), by analogy with [self-interacting dark matter](/wiki/dark-matter/halo-astrophysics/self-interacting-dark-matter) (SIDM), needs about one relaxation over the age of the halo: "Γ_self(dwarf) · t_age = κ ~ 1".
- Streams need condensation faster than stirring: "Streams need the much harder Γ_self ≳ Ω = 1/t_dyn."

The second condition is harder than the first by the ratio t_age/t_dyn. What fixes the coupling is Debt 3b's next question, "What pins g?", and it answers with two scenarios: [Scenario A](/wiki/dark-matter/momentum-clumping/wave-island/scenario-a), in which the gated channel makes the cores and the coupling is fixed (dead), and [Scenario B](/wiki/dark-matter/momentum-clumping/wave-island/scenario-b), in which the coupling is free (alive, quarantined).

Debt 3c, testing Scenario A, also allows for the slowdown of Bose-star growth seen in LPT-type kinetics, "t^{1/2} growth, factor ~10²–10³ in effective rate" ('Sharpened input numbers').

## Where the rate is carried

- **Debt 3b** (`notes/debt3b-wave-island.md`), header: "Status: rate derived, environments evaluated, verdict reached. Coefficients heuristic at O(1)–O(10) level". Its 'Standing results after Chunks A+B' summarize the wave island as "collective phenomena live but tunable, except Scenario A's mandatory UFD signature; cliff softens to (v\*/σ)⁴", where UFD stands for ultra-faint dwarf.
- **The lab notebook's addendum v0.2** (#1) states the rate in the same form for the wave island, 3×10⁻¹⁹ eV ≲ m ≲ 10⁻⁴ eV.
- **[Program v1](/wiki/history/documents/checkpoint)** (#9 §7 item 2): "The gated wave-kinetic condensation rate is Γ ≈ c·g²ρ²min(σ, v\*)⁴/(m³σ⁶) (Bose-enhanced, LPT-style [T]; coefficients to calibrate [O])."
- **Checkpoint #11** (§9 (ii), [D + T]): "Gated wave-kinetic rate Γ ≈ c·g²ρ²min(σ,v\*)⁴/(m³σ⁶) (Bose-enhanced, LPT-style [13†]; coefficients [O])."
- **[The handoff](/wiki/history/documents/handoff)** (`HANDOFF.md` §3, row 3) describes Debt 3b as the "Calc note: gated wave-kinetic condensation rate; island discriminant (exponential vs (v\*/σ)⁴)".

## Superseded: the cubic suppression of Debt 3a

Before the rate was computed, Debt 3a estimated the wave-island suppression as "(v\*/σ)³ suppression rather than an exponential" ('Consequences for the predictions table'). Debt 3b, Debt 3c and #11 use (v\*/σ)⁴, and the fourth power governs ([conflicts between sources](/wiki/history/documents/source-conflicts)). The cube is the same power of v\*/σ as Chunk A's co-mover density n_gate; the notes do not say whether that is where the estimate came from, and none of them comments on the change.

## Open: calibration of the coefficient c

The coefficient c = O(5–15) is a heuristic estimate. Debt 3a had asked for the check before the rate was computed: "Anchor scalings against LPT before trusting coefficients" ('Next chunk (3b)'). Debt 3b's header records it as undone: "Coefficients heuristic at O(1)–O(10) level; calibration against Levkov–Panin–Tkachev (LPT) numerics is a flagged to-do." Program v1 lists it among its open literature verifications: "Literature verifications: symmetric-bimetric Λ = 0; LPT coefficient calibration; Dalal–Kravtsov exact bound [O]" (#9 §10 item 8).

Checkpoint #11 marks the coefficients "[O]" in §9 but does not itemize the calibration in its [open problems](/wiki/status/open-problems), §14. Its item 10, "Literature battery completion; every † reference source-checked [O]" (OP10), covers checking the reference [13]† against the source, which is a different task from fitting c to the simulations ([the † literature battery](/wiki/method/literature-battery)). The calibration is recorded among the notes' open items on [open problems](/wiki/status/open-problems).

The coefficient enters the two scenarios differently, as their formulas show. In Scenario A the coupling is fixed by fitting dwarf cores with the same rate formula, and Debt 3b's stream-to-stirring ratio R_X contains no c. The [critical mass](/wiki/dark-matter/wave-dark-matter/attractive-condensates) M_crit = 3.6 M_P/(m√g) depends on g itself, so on the wiki's reading its Scenario-A normalization does inherit c through the core fit; Debt 3c does not state the value of c it used. In Scenario B, c appears under the square root of the stream condition X ≥ √(Ωσ²/(c m v\*⁴)). Neither note discusses the effect of a different c.

## Open: rows 1 and 2 in wave language

Rows 1 and 2 of the predictions table are [the self-interaction knee](/wiki/predictions/self-interaction-knee) and [isotropic scattering below the gate](/wiki/predictions/scattering-isotropy). Both were derived for particles, from two-body scattering. Debt 3a: "Rows 1–2 must be re-derived in wave language (two-body Born scattering is no longer the right observable)." ('Consequences for the predictions table'.) Debt 3b's suppression law supplies the wave-island form of the knee's tail, which is corollary 1 above. No document restates the isotropy of row 2 for a wave halo, and #11 §14 does not itemize the task.

## Sources

- `notes/debt3b-wave-island.md` 'Setup', 'The rate [D, heuristic coefficients]' — the mechanism, the conventions, the rate, both corollaries, the calibration flag in the header; 'What pins g? Two scenarios' — the core and stream thresholds; 'Standing results after Chunks A+B' — the summary
- `papers/broken-born-checkpoint-v2.md` §9 (ii) — the current statement, its tags and the reference [13]†; §8 — the open tail; §13 row 3 — the island discriminant; §14 item 10 — the literature battery
- `notes/debt3a-stream-stability.md` 'Setup' — the coupling g and the gate; 'Limit 1 (broad gate)' — the retired "γ vs Ω" framing; 'Limit 2 (narrow gate)' — the co-mover density n_gate; 'Consequences for the predictions table' — the wave island, the (v\*/σ)³ estimate and the rows 1–2 to-do; 'Next chunk (3b)' — the task and the anchoring instruction
- `notes/debt3c-ufd-endpoint.md` 'Sharpened input numbers' — the t^{1/2} slowdown allowed for in the test of Scenario A
- `notes/broken-born-program-v1.md` §7 item 2 — the v1 statement; §10 item 8 — the calibration as an open literature verification
- `notes/broken-born-theory.md` §11 item 3 — the original growth-rate problem; 'Addendum (v0.2)' — the notebook's record of the rate
- `HANDOFF.md` §3 row 3 — the inventory description of Debt 3b
