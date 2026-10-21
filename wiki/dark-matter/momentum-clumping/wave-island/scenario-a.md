---
title: "Obituary: Scenario A and the ultra-faint-dwarf endpoint"
weight: 20
status: dead
description: "If the gated channel makes the cores, condensation is mandatory in ultra-faint dwarfs, whose condensates would cycle through bosenovas and drain the halo; Segue 1 is intact and the light-mass escape is closed, so no parameter direction rescues it."
provenance: [D, T]
sources:
  - "notes/debt3c-ufd-endpoint.md 'The question'"
  - "notes/debt3c-ufd-endpoint.md 'Sharpened input numbers'"
  - "notes/debt3c-ufd-endpoint.md 'The attractive endpoint'"
  - "notes/debt3c-ufd-endpoint.md 'The data'"
  - "notes/debt3c-ufd-endpoint.md 'Verdict and closure'"
  - "notes/debt3b-wave-island.md 'What pins g? Two scenarios'"
  - "notes/debt3b-wave-island.md 'The rate'"
  - "notes/debt3b-wave-island.md 'Standing results'"
  - "papers/broken-born-checkpoint-v2.md §9"
  - "papers/broken-born-checkpoint-v2.md §13"
  - "papers/broken-born-checkpoint-v2.md §14 item 10"
  - "papers/broken-born-checkpoint-v2.md refs [13]–[15]"
  - "HANDOFF.md §2"
  - "HANDOFF.md §3"
  - "notes/broken-born-theory.md 'Addendum (v0.2)'"
  - "notes/broken-born-program-v1.md §7"
  - "notes/broken-born-program-v1.md §10"
---

*Scenario A was the assumption that, on the [wave island](/wiki/dark-matter/momentum-clumping/wave-island), the gated attraction that condenses wave-like dark matter is also what gives ordinary dwarf galaxies their smooth, constant-density cores. Fitting those cores fixes the strength of the coupling, and with the coupling fixed, condensation is forced to happen, across the whole halo, in the ultra-faint dwarf galaxies, the faintest, densest and oldest galaxies known. Because the attraction makes a condensate collapse whenever it passes a critical mass, throwing off fast waves that escape the galaxy, these galaxies would by now have lost much of their dark matter. Instead they are among the most dark-matter-dominated systems observed: Segue 1 holds a dense, intact halo around stars about 13 billion years old. A much lighter mass, which would avoid the collapse, is excluded by other observations, and no other change of parameters rescues the scenario. Scenario A is dead.*

**Status:** Dead. "Scenario A is falsified by the existence of ultra-faint dwarfs" (`notes/debt3c-ufd-endpoint.md`, calc note #4); [checkpoint #11](/wiki/history/documents/checkpoint) §9 (ii), tagged [D + T], records its endpoint as "falsified by observed UFD density and longevity". Not machine-checked: no `verify/` script covers any Debt-3 number, and the Segue 1 inputs carry no reference in any source document. Listed in [the graveyard](/wiki/status/graveyard).

## What was claimed

### The gated channel as the core-maker

Dwarf galaxies show cores, regions of nearly constant dark-matter density at their centers, where collisionless cold dark matter predicts a density that keeps rising inward [T] ([dwarf galaxies](/wiki/dark-matter/halo-astrophysics/dwarf-galaxies)). [Self-interacting dark matter](/wiki/dark-matter/halo-astrophysics/self-interacting-dark-matter) (SIDM) explains them by scattering: collisions carry heat from the outer halo into the cold inner region and flatten it, and a core forms when a typical particle scatters about once over the age of the halo [T]. On the particle side of the program the same reasoning fixes conjugate matter's cross-section ([the scattering benchmark](/wiki/dark-matter/conjugate-matter/benchmark)).

On the wave island the relaxation is wave-kinetic, at [the gated condensation rate Γ_self](/wiki/dark-matter/momentum-clumping/wave-island/condensation-rate). Scenario A assumes that this rate is what makes the cores. `notes/debt3b-wave-island.md` (calc note #3), 'What pins g? Two scenarios':

> Scenario A — the gated channel is the core-maker. On the wave island, Γ_self is the analog of SIDM heat transport (kinetic relaxation redistributes energy through the halo). Fitting classical-dwarf cores means Γ_self(dwarf) · t_age = κ ~ 1, which spends g²/m³. Streams need the much harder Γ_self ≳ Ω = 1/t_dyn.

Here t_age is the age of the halo, κ the normalization of the core fit, and Ω = 1/t_dyn the rate at which orbits stir the halo, with t_dyn the dynamical time. The rate Γ_self ≈ c g²ρ² min(σ, v\*)⁴/(m³σ⁶) depends on the coupling g and the mass m only through g²/m³, so fitting the cores fixes that combination: the coupling is "spent", and the rate in every other environment follows from it.

### The environment table

Debt 3b then compares the stream condition with the core condition in each environment. It writes R_X for the ratio of the condensation rate to the stirring rate in an environment X, where X labels the environment and is not [the momentum graviton](/wiki/gravity/momentum-graviton). "Eliminating g²/m³":

```text
R_X ≡ Γ_self(X)/Ω_X = κ (t_dyn,X/t_age) (ρ_X/ρ_d)² (σ_d/σ_X)² (min(σ_X, v*)/σ_X)⁴
```

with ρ_d and σ_d the density and dispersion of the classical dwarf core used for the fit. The note does not write the step out. Dividing Γ_self in environment X by Γ_self in the dwarf removes c, g and m, and multiplying by t_dyn,X and using Γ_self(dwarf) = κ/t_age gives the formula; the absence of a gate factor for the dwarf means the dwarf is taken to be gate-open (σ_d ≲ v\*). Streams form where R_X ≳ 1. Debt 3b's table, at κ = 1:

| Environment (ρ in GeV/cm³, σ in km/s) | t_dyn | R_X (κ = 1) |
|---|---|---|
| Classical dwarf core (1, 30) | 0.1 Gyr | ∼10⁻² |
| Ultra-faint dwarf (20, 3) | 0.01 Gyr | ∼40 |
| Milky Way inner 1 kpc (10, 120) | 0.02 Gyr | ∼10⁻² |
| Milky Way solar circle (0.4, 155) | 0.2 Gyr | ∼4×10⁻⁵ |
| Cluster (0.03, 1000) | 1 Gyr | ∼0 |

The inputs are not cited, and the ultra-faint-dwarf row was later replaced by Segue 1's numbers (below). The note's verdict, with UFD for ultra-faint dwarf:

> Verdict A: streams lose everywhere by 10²–10⁴ — except ultra-faint dwarfs, where ρ²/σ² leverage wins by ~40. In UFDs, condensation is then mandatory and halo-wide: power drains into the lowest relative momenta on sub-dynamical timescales.

The leverage is the factor (ρ_X/ρ_d)²(σ_d/σ_X)²: ultra-faint dwarfs are denser than the classical dwarf and colder, and both differences raise the rate. The Milky Way streams of the program's founding image do not form; condensation is forced only in the smallest galaxies.

### The first endpoint: a localized signature

Debt 3b drew the consequence for the ultra-faint dwarfs at once:

> Because the interaction is attractive, the endpoint is not a placid stream: a growing condensate with attractive self-interaction has a critical mass, M_crit ≈ 3.6 M_P/(m√g) [T: dilute-boson-star bound, Chavanis-type], above which it collapses (bosenova). The surviving descendant of old rows 3–4 is therefore a sharply localized prediction: anomalous central objects, density spikes, or disruption signatures in ultra-faint dwarfs, absent in classical dwarfs and the MW.

MW is the Milky Way. Old rows 3 and 4 are the withdrawn predictions of [velocity-space granularity](/wiki/dark-matter/momentum-clumping/velocity-granularity) and [Fornax friction suppression](/wiki/dark-matter/momentum-clumping/fornax-friction). The note left the endpoint to the next calculation: "Quantifying the endpoint (soliton growth rate vs. M_crit; survival constraints from observed UFDs) is Chunk 3c." For a while, then, Scenario A was the one place in the program where velocity-space condensation was a mandatory prediction ('Standing results after Chunks A+B': "except Scenario A's mandatory UFD signature").

## How it was tested

Debt 3c (`notes/debt3c-ufd-endpoint.md`, calc note #4) set the test ('The question'): "Chunk 3b left Scenario A (gated channel = the core-maker) with one mandatory prediction: halo-wide condensation in ultra-faint dwarfs (UFDs), R ≡ Γ_self·t_dyn ≫ 1. This chunk follows that condensation to its endpoint and tests it against real UFDs."

### Segue 1 and the condensation time

Segue 1 is an ultra-faint dwarf satellite of the Milky Way [T]. Debt 3c takes its numbers as the test case ('Sharpened input numbers'):

> Segue 1: M(< 38 pc) ≈ 6×10⁵ M_⊙ ⇒ mean core density ρ ≈ 100 GeV/cm³ (not the conservative 20 used in 3b), σ ≈ 3.7 km/s, t_dyn ≈ 10 Myr.

Here M(< 38 pc) is the mass within 38 parsecs of the center and M_⊙ the mass of the Sun. Rerunning Debt 3b's ratio "with the dwarf-core normalization (κ = 1)":

```text
R_Segue1 = κ (t_dyn/t_age) (ρ/ρ_d)² (σ_d/σ)² ≈ 10⁻³ · 10⁴ · 66 ≈ 660
```

The three numerical factors stand, in order, for the time ratio, the squared density ratio and the squared dispersion ratio, with Debt 3b's classical dwarf core as the reference. Debt 3c's version omits 3b's gate factor (min(σ, v\*)/σ)⁴, which equals 1 when the gate is open, σ ≲ v\*.

The condensation time follows: "Condensation time τ_cond = t_dyn/R ≈ 1.5×10⁴ yr. Over a 10 Gyr lifetime the system has ~6×10⁵ condensation times." (τ_cond is unrelated to the dark-energy field τ.) Bose-star growth in wave kinetics slows with time ([wave kinetics and Bose-star formation](/wiki/dark-matter/wave-dark-matter/wave-kinetics)), and Debt 3c allows for it: "Even granting the soliton-growth slowdown seen in LPT-type kinetics (t^{1/2} growth, factor ~10²–10³ in effective rate), the core is processed through the condensate many times over. There is no timescale refuge." LPT is Levkov–Panin–Tkachev, the checkpoint's [13]†, and "soliton" here means a Bose-star core. #11 §9 rounds the result to "Segue 1: rate ratio ~660; condensation ~10⁴ yr".

### The critical mass

For a condensate held together by gravity alone, a larger mass gives a smaller and denser equilibrium. An attractive self-interaction adds an energy that grows faster with compactness, and above a critical mass the gradient energy of the wave can no longer balance the combined attraction: no stable equilibrium exists, and the condensate collapses [T] ([attractive condensates](/wiki/dark-matter/wave-dark-matter/attractive-condensates)). Debt 3b took the bound from the literature, "[T: dilute-boson-star bound, Chavanis-type]"; #11 cites it as [14]†, P.-H. Chavanis, Phys. Rev. D 84, 043531 (2011). Debt 3c evaluates it under Scenario A's normalization, "which pins g²/m³, hence pins M_crit as a function of m alone" ('The attractive endpoint: criticality and the drain'):

```text
M_crit = 3.6 M_P/(m√g) ≈ 2.9×10⁻³⁰ (m/eV)^(−7/4) M_⊙
```

M_P is the Planck mass. The exponent follows from the fixed combination, a step the note does not write: with g²/m³ fixed, g grows as m^{3/2}, so m√g grows as m^{7/4}. The −7/4 form therefore holds only under Scenario A. "This crosses the UFD core mass (~10⁶ M_⊙) at m ≈ 5×10⁻²¹ eV", and the wave island splits into two branches.

### Branch (i): the condensate as a mass drain

For "m ≳ 10⁻²⁰ eV (the bulk of the wave island): M_crit ≪ M_core — often absurdly so (10⁻⁷ M_⊙ at 10⁻¹³ eV)". The condensate reaches the critical mass almost at once and enters the collapse cycle known from attractive Bose stars, the bosenova (Debt 3c):

> grow to M_crit → collapse → eject an O(0.1–1) fraction as fast/relativistic waves (bosenova; LPT 2017-type result [T]) → remnant regrows.

The 2017 paper is the second item of the checkpoint's [13]†, on relativistic axions from collapsing Bose stars. What decides the galaxy's fate is the speed of the ejected waves: "Ejecta velocities are set by the dense collapse stage and vastly exceed a UFD escape velocity of ~10 km/s: the condensate is a mass drain." Each cycle removes part of the galaxy's dark matter, and the remnant regrows from the remaining halo to be processed again. Debt 3c bounds the outcome even under a slowed rate:

> The UFD converts its cold dark matter into escaping radiation at a rate bounded below by the self-regulated relaxation rate. Even if heating and expansion throttle Γ down to ~1/t_age (the gravothermal self-limit), an O(1) fraction of the core mass is processed and removed within the lifetime — unlike SIDM, where relaxation is elastic and mass stays.

The contrast with SIDM carries the argument. In SIDM the collisions are elastic: they move energy around and the halo's evolution is gravothermal, a slow redistribution of heat under gravity, but every particle stays bound [T]. In Scenario A the relaxation feeds a condensate that converts bound dark matter into unbound waves. "Prediction of Branch (i): UFDs today should be low-density, inflated, or gone."

### Branch (ii): excluded in advance

For "m ≲ 5×10⁻²¹ eV: M_crit ≳ M_core; the condensate grows as a stable soliton — ordinary fuzzy-DM phenomenology with an attractive perturbation", where DM is dark matter. Fuzzy dark matter is wave dark matter so light that its de Broglie wavelength reaches the size of galactic cores, where the quantum pressure of the wave supports a stable core [T]. This branch fails before the data on Segue 1 are consulted (Debt 3c):

> But this mass range is independently excluded: UFD sizes and stellar kinematics (granule-heating arguments, Dalal & Kravtsov 2022 [T — bound ≈ 3×10⁻¹⁹ eV; verify exact figure before publication]) and Lyman-α forest limits already forbid wave DM this light.

In a wave halo, interference between waves makes density fluctuations of about the de Broglie size, granules, whose gravity heats the orbits of stars; the lighter the boson, the larger the granules and the stronger the heating, so compact stellar systems bound the mass from below [T]. The Lyman-α forest, absorption lines from intergalactic hydrogen, traces the matter distribution on small scales, which very light wave dark matter would smooth out [T]. The Dalal–Kravtsov reference is the checkpoint's [15]†, N. Dalal and A. Kravtsov, Phys. Rev. D 106, 063517 (2022). No source gives a reference for the Lyman-α limit. #11 §9 states the closure without a number: "the light-mass escape is closed independently [15†, Lyman-α]". See [bounds on fuzzy dark matter](/wiki/dark-matter/wave-dark-matter/fuzzy-dark-matter-bounds).

## Why it failed

### The data

Debt 3c compares the two branches with the observed ultra-faint dwarfs ('The data'):

> Observed UFDs are the densest, most DM-dominated, oldest systems known — Segue 1 has M/L ~ 10³ and a ~13 Gyr stellar population sitting in an intact, dense halo. Branch (i) predicts the opposite of what is observed; Branch (ii) is excluded before we arrive.

M/L is the mass-to-light ratio, in solar units [T]; a value of order a thousand means that the galaxy's mass is almost entirely dark matter. Branch (i) predicts galaxies that have lost their dark matter or puffed up; Segue 1 is dense and has kept a stellar population of about 13 billion years inside an intact halo. Branch (ii), the only escape, lies below the mass bounds.

### No parameter rescues it

Debt 3c checks the remaining freedom:

> Robustness checks: shrinking v\* makes it worse (σ⁻⁶ leverage boosts R to ~10⁵); growing v\* leaves R unchanged; κ < 1 is by definition Scenario B. No parameter direction rescues it.

- **A narrower gate** (smaller v\*) makes the verdict stronger. In the gate-narrow regime the rate falls as σ⁻⁶ instead of σ⁻² ([the rate](/wiki/dark-matter/momentum-clumping/wave-island/condensation-rate)), which the note calls "σ⁻⁶ leverage", and it raises R to about 10⁵.
- **A wider gate** (larger v\*) changes nothing; R stays as computed.
- **A smaller core normalization**, κ < 1, means that the gated channel does not make the cores. That is no longer Scenario A but [Scenario B](/wiki/dark-matter/momentum-clumping/wave-island/scenario-b).

## The verdict and its record

Debt 3c's verdict ('Verdict and closure of Debt 3'): "Scenario A is falsified by the existence of ultra-faint dwarfs." The header of the note: "Status: complete. Verdict: Scenario A falsified; Debt 3 closed."

The kill is carried in every later summary:

- [The lab notebook](/wiki/history/documents/lab-notebook)'s addendum v0.2 (#1): "If the gated channel also makes dwarf cores, condensation is mandatory only in ultra-faint dwarfs, where the attractive endpoint (bosenova cycling above M_crit≈3.6M_P/(m√g)) drains their dark matter — falsified by the observed density and longevity of Segue 1-class systems."
- [Program v1](/wiki/history/documents/checkpoint) (#9 §7 item 2): "Observed UFDs are the densest, oldest, most DM-dominated systems known: falsified. The light-mass escape is independently excluded (UFD heating bounds ≈ 3×10⁻¹⁹ eV, Dalal & Kravtsov 2022 [T — verify figure]; Lyman-α)."
- Checkpoint #11 §9 (ii), [D + T]: condensation is mandatory only in ultra-faint dwarfs, "whose attractive endpoint cycles above M_crit ≈ 2.9×10⁻³⁰(m/eV)^{−7/4} M_⊙ [14†] and drains the halo — falsified by observed UFD density and longevity".
- [The handoff](/wiki/history/documents/handoff) (`HANDOFF.md` §2), under "Dead (killed by own calculations — keep dead)": clumping was "fatal where mandatory on the wave island (ultra-faint dwarfs would be drained; Segue 1 intact)". Its inventory (§3, row 4) summarizes Debt 3c as "Segue 1 endpoint; bosenova drain; Scenario A falsified".

The calculation that killed it is the third of [the Debt-3 calc notes](/wiki/history/documents/debt-3-notes).

## What it took with it

- **Old rows 3 and 4.** Debt 3c: "Rows 3 and 4 of the predictions table are permanently withdrawn, on both islands. The Fornax mechanism goes with them." Debt 3b's "surviving descendant" of those rows, the localized ultra-faint-dwarf signature, died with Scenario A. #11 §13 lists the rows as "Withdrawn with cause: velocity-space granularity in halos; Fornax friction suppression (obituary §9)" ([velocity-space granularity](/wiki/dark-matter/momentum-clumping/velocity-granularity), [Fornax friction](/wiki/dark-matter/momentum-clumping/fornax-friction)).
- **The last mandatory form of clumping.** With Scenario A dead, velocity-space clumping is nowhere a required phenomenon. Scenario A is the "fatal (committed wave)" case of [the net theorem](/wiki/dark-matter/momentum-clumping/net-theorem), and its death completes the obituary of [the founding image](/wiki/dark-matter/momentum-clumping/founding-image).

## What survives

- **The wave island, with a free coupling.** Debt 3c: "The surviving wave island is roughly 3×10⁻¹⁹ eV ≲ m ≲ 10⁻⁴ eV with Scenario-B couplings." Under [Scenario B](/wiki/dark-matter/momentum-clumping/wave-island/scenario-b) streams are possible but never required, and #11 §15 lists that sector as a degeneration risk.
- **The rate and its corollary.** [The gated condensation rate](/wiki/dark-matter/momentum-clumping/wave-island/condensation-rate) stands, and its power-law suppression is the wave side of [the island discriminant](/wiki/predictions/island-discriminant), the diagnostic that #11 §9 lists as salvage from Debt 3.
- **Relic production.** [Misalignment on the wave island](/wiki/dark-matter/momentum-clumping/wave-island/misalignment-relic) does not depend on what fixes the coupling.

## What is unchecked

- No `verify/` script covers the environment table, the Segue 1 ratio, the condensation time or the critical-mass normalization ([the iron rule](/wiki/method/verification/iron-rule)).
- The Segue 1 inputs and the environment table's inputs carry no reference in any source document; they need a source check before any external use.
- The coefficient 3.6 and the convention for g in M_crit have not been checked against the cited paper.
- The references [13]†, [14]† and [15]† are cited from model memory and await [the † literature battery](/wiki/method/literature-battery) (#11 §14 item 10, OP10). Program v1 lists the "Dalal–Kravtsov exact bound" among its open literature verifications (#9 §10 item 8), and #11 dropped the figure ≈ 3×10⁻¹⁹ eV that the notes and v1 quote.

## Sources

- `notes/debt3c-ufd-endpoint.md` 'The question', 'Sharpened input numbers', 'The attractive endpoint: criticality and the drain', 'The data', 'Verdict and closure of Debt 3' — the test, the Segue 1 numbers, the critical mass, both branches, the robustness checks and the verdict
- `notes/debt3b-wave-island.md` 'What pins g? Two scenarios' — Scenario A, R_X, the environment table, Verdict A and the first endpoint; 'The rate [D, heuristic coefficients]' — the rate; 'Standing results after Chunks A+B' — the mandatory signature
- `papers/broken-born-checkpoint-v2.md` §9 (ii) — the current statement and its tags; §13 — the withdrawn rows; §14 item 10 — the literature battery; references [13]†, [14]†, [15]†
- `HANDOFF.md` §2 — the handoff's dead list; §3 row 4 — the inventory description of Debt 3c
- `notes/broken-born-theory.md` 'Addendum (v0.2)' — the notebook's record of the kill
- `notes/broken-born-program-v1.md` §7 item 2 — the v1 record, with the Dalal–Kravtsov figure; §10 item 8 — the exact bound as an open verification
