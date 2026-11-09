---
title: "Under review: Scenario A and the ultra-faint-dwarf endpoint"
weight: 20
status: under-review
description: "If the gated channel makes the cores, condensation is mandatory in ultra-faint dwarfs, whose condensates would cycle through bosenovas and drain the halo; Segue 1 is intact and the light-mass escape is closed, so no parameter direction rescues it."
provenance: [D, T]
sources:
  - "notes/ufd-endpoint.md 'The question'"
  - "notes/ufd-endpoint.md 'Sharpened input numbers'"
  - "notes/ufd-endpoint.md 'The attractive endpoint'"
  - "notes/ufd-endpoint.md 'The data'"
  - "notes/ufd-endpoint.md 'Verdict and closure'"
  - "notes/wave-island.md 'What pins g? Two scenarios'"
  - "notes/wave-island.md 'The rate'"
  - "notes/wave-island.md 'Standing results'"
  - "wiki/papers/broken-born-checkpoint-v2.md §9"
  - "wiki/papers/broken-born-checkpoint-v2.md §13"
  - "wiki/papers/broken-born-checkpoint-v2.md §14 item 10"
  - "wiki/papers/broken-born-checkpoint-v2.md refs [13]–[15]"
  - "HANDOFF.md §2"
  - "HANDOFF.md §3"
  - "notes/broken-born-theory.md 'Addendum (v0.2)'"
  - "notes/broken-born-program-v1.md §7"
  - "notes/broken-born-program-v1.md §10"
  - "verify/velocity_gated_gravity.py 'D. The obituary's scope'"
  - "review/momentum-gravity/scripts/corner/obs_corner.py part D"
  - "CLAUDE.md 'Since the handoff'"
---

*Scenario A is the assumption that, on the [wave island](_index.md), the gated attraction that condenses wave-like dark matter is also what gives ordinary dwarf galaxies their smooth, constant-density cores. Fitting those cores fixes the strength of the coupling, and with the coupling fixed, condensation is forced to happen, across the whole halo, in the ultra-faint dwarf galaxies, the faintest, densest and oldest galaxies known. Because the attraction makes a condensate collapse whenever it passes a critical mass, throwing off fast waves that escape the galaxy, these galaxies would by now have lost much of their dark matter. Instead they are among the most dark-matter-dominated systems observed: Segue 1 holds a dense, intact halo around stars about 13 billion years old. A much lighter mass, which would avoid the collapse, is excluded by other observations, and no other change of parameters rescues the scenario.*

**Status:** Under review — the evidence below weighs against it, and its final status awaits review. [Calc note #4](../../../history/documents/clumping-notes.md)'s verdict is "Scenario A is falsified by the existence of ultra-faint dwarfs" ([`notes/ufd-endpoint.md`](../../../../notes/ufd-endpoint.md)). In [checkpoint #11](../../../history/documents/checkpoint.md) [§9](../../../papers/broken-born-checkpoint-v2.md#9-momentum-clumping-the-founding-image-tested), Scenario A is the committed-wave case of result (ii), tagged [D + T], which records its endpoint as "falsified by observed UFD density and longevity", where UFD stands for ultra-faint dwarf. Not machine-checked: no `verify/` script covers a number of calc note [#3](../../../../notes/wave-island.md) or [#4](../../../../notes/ufd-endpoint.md); the gate checks only calc note [#2](../../../../notes/stream-stability.md)'s shortfall ratios, in section D of [`verify/velocity_gated_gravity.py`](../../../../verify/velocity_gated_gravity.py) ([the velocity-gated-gravity script](../../../method/verification/velocity-gated-gravity-script.md)), and calc note #4 gives no reference for its Segue 1 inputs. Home section: [the wave island](_index.md); listed in [claims under review](../../../status/under-review.md).

## What was claimed

### The gated channel as the core-maker

Dwarf galaxies show cores, regions of nearly constant dark-matter density at their centers, where collisionless cold dark matter predicts a density that keeps rising inward [T] ([dwarf galaxies](../../halo-astrophysics/dwarf-galaxies.md)). [Self-interacting dark matter](../../halo-astrophysics/self-interacting-dark-matter.md) (SIDM) explains them by scattering: collisions carry heat from the outer halo into the cold inner region and flatten it, and a core forms when a typical particle scatters about once over the age of the halo [T]. On the particle side of the program the same reasoning fixes [conjugate matter](../../conjugate-matter/_index.md)'s cross-section ([the scattering benchmark](../../conjugate-matter/benchmark.md)).

On the wave island the relaxation is wave-kinetic, at [the gated condensation rate Γ_self](condensation-rate.md). Scenario A assumes that this rate is what makes the cores. [`notes/wave-island.md`](../../../../notes/wave-island.md) (calc note #3), 'What pins g? Two scenarios':

> Scenario A — the gated channel is the core-maker. On the wave island, Γ_self is the analog of SIDM heat transport (kinetic relaxation redistributes energy through the halo). Fitting classical-dwarf cores means Γ_self(dwarf) · t_age = κ ~ 1, which spends g²/m³. Streams need the much harder Γ_self ≳ Ω = 1/t_dyn.

Here t_age is the age of the halo, κ the normalization of the core fit, and Ω = 1/t_dyn the rate at which orbits stir the halo, with t_dyn the dynamical time. The rate Γ_self ≈ c g²ρ² min(σ, v\*)⁴/(m³σ⁶), with v\* the width of [the velocity gate](../../conjugate-matter/velocity-gate.md), depends on the coupling g and the mass m only through g²/m³, so fitting the cores fixes that combination: the coupling is determined, and the rate in every other environment follows from it.

### The environment table

Calc note #3 then compares the stream condition with the core condition in each environment. It writes R_X for the ratio of the condensation rate to the stirring rate in an environment X, where X labels the environment and is not [the momentum graviton](../../../gravity/momentum-graviton/_index.md). "Eliminating g²/m³":

```text
R_X ≡ Γ_self(X)/Ω_X = κ (t_dyn,X/t_age) (ρ_X/ρ_d)² (σ_d/σ_X)² (min(σ_X, v*)/σ_X)⁴
```

with ρ_d and σ_d the density and [dispersion](../../halo-astrophysics/velocity-dispersion.md) of the classical dwarf core used for the fit. The note does not write the step out. On the wiki's reading, dividing Γ_self in environment X by Γ_self in the dwarf removes c, g and m, and multiplying by t_dyn,X and using Γ_self(dwarf) = κ/t_age gives the formula; the absence of a gate factor for the dwarf means the dwarf is taken to be gate-open (σ_d ≲ v\*). Streams form where R_X ≳ 1. Calc note #3's table, at κ = 1:

| Environment (ρ in GeV/cm³, σ in km/s) | t_dyn | R_X (κ = 1) |
|---|---|---|
| Classical dwarf core (1, 30) | 0.1 Gyr | ∼10⁻² |
| Ultra-faint dwarf (20, 3) | 0.01 Gyr | ∼40 |
| Milky Way inner 1 kpc (10, 120) | 0.02 Gyr | ∼10⁻² |
| Milky Way solar circle (0.4, 155) | 0.2 Gyr | ∼4×10⁻⁵ |
| Cluster (0.03, 1000) | 1 Gyr | ∼0 |

The inputs are not cited, and the ultra-faint-dwarf row was later replaced by Segue 1's numbers (below). The note's verdict, with UFD for ultra-faint dwarf:

> Verdict A: streams lose everywhere by 10²–10⁴ — except ultra-faint dwarfs, where ρ²/σ² leverage wins by ~40. In UFDs, condensation is then mandatory and halo-wide: power drains into the lowest relative momenta on sub-dynamical timescales.

The leverage is the factor (ρ_X/ρ_d)²(σ_d/σ_X)²: ultra-faint dwarfs are denser than the classical dwarf and colder, and both differences raise the rate. The Milky Way streams of [the program's founding image](../founding-image.md) do not form; condensation is forced only in the smallest galaxies.

### The first endpoint: a localized signature

Calc note #3 drew the consequence for the ultra-faint dwarfs at once:

> Because the interaction is attractive, the endpoint is not a placid stream: a growing condensate with attractive self-interaction has a critical mass, M_crit ≈ 3.6 M_P/(m√g) [T: dilute-boson-star bound, Chavanis-type], above which it collapses (bosenova). The surviving descendant of old rows 3–4 is therefore a sharply localized prediction: anomalous central objects, density spikes, or disruption signatures in ultra-faint dwarfs, absent in classical dwarfs and the MW.

MW is the Milky Way. Old rows 3 and 4 are the withdrawn predictions of [velocity-space granularity](../velocity-granularity.md) and [Fornax friction suppression](../fornax-friction.md). The note left the endpoint to the next calculation: "Quantifying the endpoint (soliton growth rate vs. M_crit; survival constraints from observed UFDs) is Chunk 3c." In calc note #3, then, Scenario A is the one place in the program where velocity-space condensation is a mandatory prediction ('Standing results after Chunks A+B': "except Scenario A's mandatory UFD signature").

## How it was tested

Calc note #4 ([`notes/ufd-endpoint.md`](../../../../notes/ufd-endpoint.md)) set the test ('The question'): "Chunk 3b left Scenario A (gated channel = the core-maker) with one mandatory prediction: halo-wide condensation in ultra-faint dwarfs (UFDs), R ≡ Γ_self·t_dyn ≫ 1. This chunk follows that condensation to its endpoint and tests it against real UFDs."

### Segue 1 and the condensation time

Segue 1 is an ultra-faint dwarf satellite of the Milky Way [T]. Calc note #4 takes its numbers as the test case ('Sharpened input numbers'):

> Segue 1: M(< 38 pc) ≈ 6×10⁵ M_⊙ ⇒ mean core density ρ ≈ 100 GeV/cm³ (not the conservative 20 used in 3b), σ ≈ 3.7 km/s, t_dyn ≈ 10 Myr.

Here M(< 38 pc) is the mass within 38 parsecs of the center and M_⊙ the mass of the Sun, and 3b is calc note #3. Rerunning calc note #3's ratio "with the dwarf-core normalization (κ = 1)":

```text
R_Segue1 = κ (t_dyn/t_age) (ρ/ρ_d)² (σ_d/σ)² ≈ 10⁻³ · 10⁴ · 66 ≈ 660
```

The note does not name the three numerical factors; on the wiki's reading they are, in order, the time ratio, the squared density ratio and the squared dispersion ratio, with calc note #3's classical dwarf core as the reference. Calc note #4's version omits #3's gate factor (min(σ, v\*)/σ)⁴, which equals 1 when the gate is open, σ ≲ v\*.

The condensation time follows: "Condensation time τ_cond = t_dyn/R ≈ 1.5×10⁴ yr. Over a 10 Gyr lifetime the system has ~6×10⁵ condensation times." (τ_cond is unrelated to the dark-energy field τ.) Bose-star growth in wave kinetics slows with time ([wave kinetics and Bose-star formation](../../wave-dark-matter/wave-kinetics.md)), and calc note #4 allows for it: "Even granting the soliton-growth slowdown seen in LPT-type kinetics (t^{1/2} growth, factor ~10²–10³ in effective rate), the core is processed through the condensate many times over. There is no timescale refuge." LPT is Levkov–Panin–Tkachev, the checkpoint's [13]†, and "soliton" here means a Bose-star core. [#11 §9](../../../papers/broken-born-checkpoint-v2.md#9-momentum-clumping-the-founding-image-tested) rounds the result to "Segue 1: rate ratio ~660; condensation ~10⁴ yr".

### The critical mass

For a condensate held together by gravity alone, a larger mass gives a smaller and denser equilibrium. An attractive self-interaction adds an energy that grows faster with compactness, and above a critical mass the gradient energy of the wave can no longer balance the combined attraction: no stable equilibrium exists, and the condensate collapses [T] ([attractive condensates](../../wave-dark-matter/attractive-condensates.md)). Calc note #3 took the bound from the literature, "[T: dilute-boson-star bound, Chavanis-type]"; #11 cites it as [14]†, P.-H. Chavanis, Phys. Rev. D 84, 043531 (2011). Calc note #4 evaluates it under Scenario A's normalization, "which pins g²/m³, hence pins M_crit as a function of m alone" ('The attractive endpoint: criticality and the drain'):

```text
M_crit = 3.6 M_P/(m√g) ≈ 2.9×10⁻³⁰ (m/eV)^(−7/4) M_⊙
```

M_P is the [Planck mass](../../../gravity/spin-2-fields/planck-units.md#where-a-document-states-no-convention). The exponent follows from the fixed combination, a step the note does not write: with g²/m³ fixed, g grows as m^{3/2}, so m√g grows as m^{7/4}. The −7/4 form therefore holds only under Scenario A. "This crosses the UFD core mass (~10⁶ M_⊙) at m ≈ 5×10⁻²¹ eV", and the wave island splits into two branches.

### Branch (i): the condensate as a mass drain

For "m ≳ 10⁻²⁰ eV (the bulk of the wave island): M_crit ≪ M_core — often absurdly so (10⁻⁷ M_⊙ at 10⁻¹³ eV)". The condensate reaches the critical mass almost at once and enters the collapse cycle known from attractive Bose stars, the bosenova (calc note #4):

> grow to M_crit → collapse → eject an O(0.1–1) fraction as fast/relativistic waves (bosenova; LPT 2017-type result [T]) → remnant regrows.

The 2017 paper is the second item of the checkpoint's [13]†, on relativistic [axions](../../../cosmology/dark-energy/axion-like-fields.md#as-dark-matter) from collapsing Bose stars. What decides the galaxy's fate is the speed of the ejected waves: "Ejecta velocities are set by the dense collapse stage and vastly exceed a UFD escape velocity of ~10 km/s: the condensate is a mass drain." Each cycle removes part of the galaxy's dark matter, and the remnant regrows from the remaining halo to be processed again. Calc note #4 bounds the outcome even under a slowed rate:

> The UFD converts its cold dark matter into escaping radiation at a rate bounded below by the self-regulated relaxation rate. Even if heating and expansion throttle Γ down to ~1/t_age (the gravothermal self-limit), an O(1) fraction of the core mass is processed and removed within the lifetime — unlike SIDM, where relaxation is elastic and mass stays.

The contrast with SIDM carries the argument. In SIDM the collisions are elastic: they move energy around and the halo's evolution is gravothermal, a slow redistribution of heat under gravity, but the mass stays in the halo [T]. In Scenario A the relaxation feeds a condensate that converts bound dark matter into unbound waves. "Prediction of Branch (i): UFDs today should be low-density, inflated, or gone."

### Branch (ii): excluded in advance

For "m ≲ 5×10⁻²¹ eV: M_crit ≳ M_core; the condensate grows as a stable soliton — ordinary fuzzy-DM phenomenology with an attractive perturbation", where DM is dark matter. Fuzzy dark matter is wave dark matter so light that its de Broglie wavelength reaches the size of galactic cores, where the quantum pressure of the wave supports a stable core [T]. This branch fails before the data on Segue 1 are consulted (calc note #4):

> But this mass range is independently excluded: UFD sizes and stellar kinematics (granule-heating arguments, Dalal & Kravtsov 2022 [T — bound ≈ 3×10⁻¹⁹ eV; verify exact figure before publication]) and Lyman-α forest limits already forbid wave DM this light.

In a wave halo, interference between waves makes density fluctuations of about the de Broglie size, granules, whose gravity heats the orbits of stars; the lighter the boson, the larger the granules and the stronger the heating, so compact stellar systems bound the mass from below [T]. The Lyman-α forest, absorption lines from intergalactic hydrogen, traces the matter distribution on small scales, which very light wave dark matter would smooth out [T]. The Dalal–Kravtsov reference is the checkpoint's [15]†, N. Dalal and A. Kravtsov, Phys. Rev. D 106, 063517 (2022). No source gives a reference for the Lyman-α limit. [#11 §9](../../../papers/broken-born-checkpoint-v2.md#9-momentum-clumping-the-founding-image-tested) states the closure without a number: "the light-mass escape is closed independently [15†, Lyman-α]". See [bounds on fuzzy dark matter](../../wave-dark-matter/fuzzy-dark-matter-bounds.md).

## The evidence against it

### The data

Calc note #4 compares the two branches with the observed ultra-faint dwarfs ('The data'):

> Observed UFDs are the densest, most DM-dominated, oldest systems known — Segue 1 has M/L ~ 10³ and a ~13 Gyr stellar population sitting in an intact, dense halo. Branch (i) predicts the opposite of what is observed; Branch (ii) is excluded before we arrive.

M/L is the mass-to-light ratio, in solar units [T]; a value of order a thousand means that the galaxy's mass is almost entirely dark matter. Branch (i) predicts galaxies that have lost their dark matter or puffed up; Segue 1 is dense and has kept a stellar population of about 13 billion years inside an intact halo. Branch (ii), the only escape, lies below the mass bounds.

### No parameter rescues it

Calc note #4 checks the remaining freedom:

> Robustness checks: shrinking v\* makes it worse (σ⁻⁶ leverage boosts R to ~10⁵); growing v\* leaves R unchanged; κ < 1 is by definition Scenario B. No parameter direction rescues it.

- **A narrower gate** (smaller v\*) makes the verdict stronger: the note attributes a rise of R to about 10⁵ to "σ⁻⁶ leverage". In the gate-narrow regime the rate falls as σ⁻⁶ rather than σ⁻² ([the rate](condensation-rate.md)).
- **A wider gate** (larger v\*) changes nothing; R stays as computed.
- **A smaller core normalization**, κ < 1, means that the gated channel does not make the cores. That is no longer Scenario A but [Scenario B](scenario-b.md).

## The finding

Calc note #4's verdict ('Verdict and closure of the clumping problem'): "Scenario A is falsified by the existence of ultra-faint dwarfs." The header of the note: "Status: complete. Verdict: Scenario A falsified; the clumping problem closed."

The verdict is carried in every later summary:

- [The lab notebook](../../../history/documents/lab-notebook.md)'s addendum v0.2 ([#1](../../../../notes/broken-born-theory.md)): "If the gated channel also makes dwarf cores, condensation is mandatory only in ultra-faint dwarfs, where the attractive endpoint (bosenova cycling above M_crit≈3.6M_P/(m√g)) drains their dark matter — falsified by the observed density and longevity of Segue 1-class systems."
- [Program v1](../../../history/documents/checkpoint.md) ([#9 §7 item 2](../../../../notes/broken-born-program-v1.md#7-the-death-of-momentum-clumping-the-clumping-problem-closed-negative)): "Observed UFDs are the densest, oldest, most DM-dominated systems known: falsified. The light-mass escape is independently excluded (UFD heating bounds ≈ 3×10⁻¹⁹ eV, Dalal & Kravtsov 2022 [T — verify figure]; Lyman-α)."
- Checkpoint [#11 §9](../../../papers/broken-born-checkpoint-v2.md#9-momentum-clumping-the-founding-image-tested) (ii), [D + T]: condensation is mandatory only in ultra-faint dwarfs, "whose attractive endpoint cycles above M_crit ≈ 2.9×10⁻³⁰(m/eV)^{−7/4} M_⊙ [14†] and drains the halo — falsified by observed UFD density and longevity".
- [The handoff](../../../history/documents/handoff.md) of 2026-10-19 ([`HANDOFF.md` §2](../../../../HANDOFF.md#2-scientific-state-one-screen)), in its list of failed claims: clumping was "fatal where mandatory on the wave island (ultra-faint dwarfs would be drained; Segue 1 intact)". Its inventory ([§3](../../../../HANDOFF.md#3-artifact-inventory-creation-order), row 4) summarizes calc note #4 as "Segue 1 endpoint; bosenova drain; Scenario A falsified".

The calculation behind the verdict is the third of [the clumping calc notes](../../../history/documents/clumping-notes.md). [#11 §9](../../../papers/broken-born-checkpoint-v2.md#9-momentum-clumping-the-founding-image-tested) adds that "Results (i)–(iii) stand as results", and lists Scenario A as under review.

## What rests on it

- **Old rows 3 and 4.** Calc note #4: "Rows 3 and 4 of the predictions table are permanently withdrawn, on both islands. The Fornax mechanism goes with them." Calc note #3's "surviving descendant" of those rows, the localized ultra-faint-dwarf signature, is Scenario A's own prediction, "Scenario A's mandatory UFD signature" ('Standing results after Chunks A+B'); calc note #4 follows it to its endpoint and finds that endpoint contradicted by the observed ultra-faint dwarfs ('The data'). [#11 §13](../../../papers/broken-born-checkpoint-v2.md#13-predictions-and-kill-conditions) lists both rows, velocity-space granularity in halos and Fornax friction suppression ([§9](../../../papers/broken-born-checkpoint-v2.md#9-momentum-clumping-the-founding-image-tested)), as withdrawn and under review ([Under review: velocity-space granularity in halos (old row 3)](../velocity-granularity.md), [Under review: Fornax friction suppression (old row 4)](../fornax-friction.md)).
- **The last mandatory form of clumping.** With Scenario A contradicted by the ultra-faint dwarfs, [velocity-space clumping](../_index.md) is nowhere a required phenomenon. Scenario A is the "fatal (committed wave)" case of [the net theorem](../net-theorem.md). The founding image that Scenario A tested on the wave island is P.R.'s open conjecture ([Conjecture: velocity clumping, the founding image](../founding-image.md)).

## What stands

- **The wave island, with a free coupling.** Calc note #4: "The surviving wave island is roughly 3×10⁻¹⁹ eV ≲ m ≲ 10⁻⁴ eV with Scenario-B couplings." Under [Scenario B](scenario-b.md) streams are possible but never required, and [#11 §15](../../../papers/broken-born-checkpoint-v2.md#15-assessment) lists that sector as a [degeneration risk](../../../program/assessment.md).
- **The rate and its corollary.** [The gated condensation rate](condensation-rate.md) stands, and its power-law suppression is the wave side of [the island discriminant](../../../predictions/island-discriminant.md), the diagnostic that [#11 §9](../../../papers/broken-born-checkpoint-v2.md#9-momentum-clumping-the-founding-image-tested) lists as salvage from the clumping problem.
- **Relic production.** [#11 §9](../../../papers/broken-born-checkpoint-v2.md#9-momentum-clumping-the-founding-image-tested) lists "free relic abundance via misalignment on the wave island" among the salvage, after recording the falsification ([misalignment on the wave island](misalignment-relic.md)).

## What is unchecked

- No `verify/` script covers the environment table, the Segue 1 ratio, the condensation time or the critical-mass normalization ([the iron rule](../../../method/verification/iron-rule.md)).
- The calc notes give no reference for the Segue 1 inputs or the environment table's inputs; they need a source check before any external use. The momentum-gravity investigation's scripts cite Simon et al. 2011 [S] for their own Segue 1 values ([`review/momentum-gravity/scripts/corner/obs_corner.py`](../../../../review/momentum-gravity/scripts/corner/obs_corner.py); [Segue 1, the test case](../../halo-astrophysics/dwarf-galaxies.md#segue-1-the-test-case)).
- The coefficient 3.6 and the convention for g in M_crit have not been checked against the cited paper. The normalization 2.9×10⁻³⁰ also rests on the core fit, which runs through the rate's coefficient c ([the open calibration](condensation-rate.md#open-calibration-of-the-coefficient-c)); calc note #4 does not state the value of c it used.
- The references [13]†, [14]† and [15]† are cited from model memory and await [the † literature battery](../../../method/literature-battery.md) ([#11 §14 item 10](../../../papers/broken-born-checkpoint-v2.md#14-open-problems), OP10). Program v1 lists the "Dalal–Kravtsov exact bound" among its open literature verifications ([#9 §10 item 8](../../../../notes/broken-born-program-v1.md#10-open-problems)), and #11 dropped the figure ≈ 3×10⁻¹⁹ eV that the notes and v1 quote.

## Sources

- [`notes/ufd-endpoint.md`](../../../../notes/ufd-endpoint.md) 'The question', 'Sharpened input numbers', 'The attractive endpoint: criticality and the drain', 'The data', 'Verdict and closure of the clumping problem' — the test, the Segue 1 numbers, the critical mass, both branches, the robustness checks and the verdict
- [`notes/wave-island.md`](../../../../notes/wave-island.md) 'What pins g? Two scenarios' — Scenario A, R_X, the environment table, Verdict A and the first endpoint; 'The rate [D, heuristic coefficients]' — the rate; 'Standing results after Chunks A+B' — the mandatory signature
- [`CLAUDE.md`](../../../../CLAUDE.md) 'Since the handoff' — Scenario A under review
- [`wiki/papers/broken-born-checkpoint-v2.md` §9](../../../papers/broken-born-checkpoint-v2.md#9-momentum-clumping-the-founding-image-tested) (ii) — the current statement and its tags; [§9](../../../papers/broken-born-checkpoint-v2.md#9-momentum-clumping-the-founding-image-tested) — Scenario A under review, with results (i)–(iii) standing; [§13](../../../papers/broken-born-checkpoint-v2.md#13-predictions-and-kill-conditions) — the withdrawn rows, under review; [§14 item 10](../../../papers/broken-born-checkpoint-v2.md#14-open-problems) — the literature battery; references [13]†, [14]†, [15]†
- [`HANDOFF.md` §2](../../../../HANDOFF.md#2-scientific-state-one-screen) — the handoff's list of failed claims; [§3 row 4](../../../../HANDOFF.md#3-artifact-inventory-creation-order) — the inventory description of calc note #4
- [`notes/broken-born-theory.md`](../../../../notes/broken-born-theory.md) 'Addendum (v0.2)' — the notebook's record of the verdict
- [`notes/broken-born-program-v1.md` §7 item 2](../../../../notes/broken-born-program-v1.md#7-the-death-of-momentum-clumping-the-clumping-problem-closed-negative) — the v1 record, with the Dalal–Kravtsov figure; [§10 item 8](../../../../notes/broken-born-program-v1.md#10-open-problems) — the exact bound as an open verification
- [`verify/velocity_gated_gravity.py`](../../../../verify/velocity_gated_gravity.py) section D — calc note #2's shortfall ratios, the only clumping numbers the gate checks
- [`review/momentum-gravity/scripts/corner/obs_corner.py`](../../../../review/momentum-gravity/scripts/corner/obs_corner.py) part D — Simon et al. 2011 [S] for that investigation's Segue 1 values, outside the calc notes
