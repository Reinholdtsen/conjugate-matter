---
title: "The net theorem: clumping is nowhere mandatory"
weight: 70
status: alive
description: "Velocity-space clumping is nowhere mandatory — in #11's words, 'forbidden (particles), fatal (committed wave), decorative (free wave)' — the summary result of the clumping problem."
provenance: [D]
sources:
  - "notes/ufd-endpoint.md 'Verdict and closure'"
  - "notes/ufd-endpoint.md 'The data'"
  - "notes/ufd-endpoint.md 'Sharpened input numbers'"
  - "notes/ufd-endpoint.md 'The attractive endpoint'"
  - "wiki/papers/broken-born-checkpoint-v2.md §9"
  - "wiki/papers/broken-born-checkpoint-v2.md §1"
  - "wiki/papers/broken-born-checkpoint-v2.md §12"
  - "wiki/papers/broken-born-checkpoint-v2.md §15"
  - "wiki/papers/broken-born-checkpoint-v2.md §8"
  - "wiki/papers/broken-born-checkpoint-v2.md §13"
  - "notes/stream-stability.md 'Corollary'"
  - "notes/wave-island.md 'What pins g? Two scenarios'"
  - "notes/wave-island.md 'Standing results'"
  - "notes/broken-born-program-v1.md §7"
  - "notes/broken-born-theory.md 'Addendum (v0.2)'"
  - "CLAUDE.md 'Since the handoff'"
  - "review/wiki-build-flags.md items 16, 19, 27, 55, 58"
  - "notes/velocity-gated-gravity.md §4"
  - "notes/velocity-gated-gravity.md §7"
  - "notes/gate-mechanism.md §5"
  - "verify/velocity_gated_gravity.py 'D. The obituary's scope'"
  - "notes/closed-universe.md §2"
---

*The net theorem is the summary result of [the clumping problem](../../history/main-problems.md): in every part of the program's parameter space that survives, dark matter clumping by velocity is never a required phenomenon. For particle dark matter the criterion for it fails under the program's [contact-range interaction](founding-image.md#the-scope-of-the-tests), which acts only over microscopic distances. For wave dark matter it was required only under one assumption about the coupling, [Scenario A](wave-island/scenario-a.md), whose prediction observation contradicts (Scenario A is under review); with the coupling left free, [Scenario B](wave-island/scenario-b.md), it is merely optional. The theorem closes the test of the program's [founding image](founding-image.md) with a [negative result](../../method/negative-results.md); the image itself is P.R.'s open conjecture. The theorem covers collective dynamics only, so whether a single topological object could be localized in momentum is a separate, untested question.*

**Status:** Alive — [D] in [#9 §7](../../../notes/broken-born-program-v1.md#7-the-death-of-momentum-clumping-the-clumping-problem-closed-negative) ("Three results [D]"); [#11](../../history/documents/checkpoint.md) [§9](../../papers/broken-born-checkpoint-v2.md#9-momentum-clumping-the-founding-image-tested) states it as result (iii) without a separate tag, resting on (i) [D] and (ii) [D + T]. [#11](../../papers/broken-born-checkpoint-v2.md) adds that "Results (i)–(iii) stand as results"; the founding image they tested is P.R.'s open conjecture, and Scenario A is under review ([#11 §9](../../papers/broken-born-checkpoint-v2.md#9-momentum-clumping-the-founding-image-tested)). Collective dynamics only, at the level of the calc notes' mean-field and wave-kinetic estimates. Machine-checked in part: since 2026-10-28 section D of [`verify/velocity_gated_gravity.py`](../../../verify/velocity_gated_gravity.py) has reproduced the particle leg's shortfall ratios (flag 16, addendum; [the velocity-gated-gravity script](../../method/verification/velocity-gated-gravity-script.md)); no `verify/` script covers the wave legs.

## Statement

As first stated, in [the note that closed the clumping problem](../../history/documents/clumping-notes.md), where BBT is Broken-Born theory, the program's earlier name ([`notes/ufd-endpoint.md`](../../../notes/ufd-endpoint.md), 'Verdict and closure of the clumping problem'):

> **Nowhere in the viable parameter space of BBT is velocity-space clumping a mandatory phenomenon.** It is forbidden for classical-particle χ, fatal where it would have been mandatory (Scenario A), and merely optional elsewhere (Scenario B, ten tunable orders of magnitude — a degeneration flag, not a prediction).

The checkpoint's form, [#11 §9](../../papers/broken-born-checkpoint-v2.md#9-momentum-clumping-the-founding-image-tested) (iii): "**Net theorem:** velocity-space clumping is nowhere mandatory — forbidden (particles), fatal (committed wave), decorative (free wave)." Its technical abstract: "collective momentum-space clumping is proven non-mandatory everywhere and falsified where it would have been mandatory" ([#11 §1](../../papers/broken-born-checkpoint-v2.md#1-two-abstracts)).

"Mandatory" is the operative word. A program's prediction counts only if the program requires it; a phenomenon the program merely permits, at a tunable strength, tests nothing. The theorem says that velocity clumping is never in the first class.

## The three legs

The parameter space divides first by mass, through [the classicality theorem](classicality-theorem.md), and then, on the wave side, by what fixes the coupling. Each part gets one verdict.

### "Forbidden": classical particles [D]

On the particle island, dark-matter particles with masses of MeV to GeV, the stream instability needs the attraction energy of co-moving particles to reach their kinetic energy. At the [scattering benchmark](../conjugate-matter/benchmark.md), where the coupling is fixed by dwarf-galaxy cores, [the mean-field criterion](instability-criterion.md) fails by 10²⁸–10³¹. Calc note [#2](../../../notes/stream-stability.md)'s narrow-gate form of the criterion overstates the Milky Way shortfall about 3×, and the verdict is unchanged (flag 58 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md); [the narrow-gate form, flagged](instability-criterion.md#the-narrow-gate-form-flagged)). Below threshold there is no growth, and collisions only drive the gas toward a Maxwellian. Meeting the criterion at fixed cross-section per mass would need m ≲ 0.1 meV, where about 10²⁰ quanta share each state and dark matter is a wave ([#11 §9](../../papers/broken-born-checkpoint-v2.md#9-momentum-clumping-the-founding-image-tested) (i); on the regime in which calc note #2 evaluates that mass, see flag 19 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md)). #2's summary: "Collective velocity-space dynamics and classical-particle dark matter are mutually exclusive within this framework."

### "Fatal": the committed wave [D + T]

On the [wave island](wave-island/_index.md), the gated attraction condenses the wave field at a rate [Γ_self](wave-island/condensation-rate.md). Streams need this rate to beat orbital stirring, Γ_self ≳ Ω = 1/t_dyn, with t_dyn the dynamical time of the system. Under [Scenario A](wave-island/scenario-a.md), the same gated channel makes the cores of classical dwarf galaxies, which fixes the coupling; "committed" in #11's phrase means this. Then streams lose to stirring "everywhere by 10²–10⁴ — *except ultra-faint dwarfs*" ([#3](../../../notes/wave-island.md)). In the [ultra-faint dwarf galaxies](../halo-astrophysics/dwarf-galaxies.md) condensation is mandatory: for Segue 1, "rate ratio ~660; condensation ~10⁴ yr" ([#11 §9](../../papers/broken-born-checkpoint-v2.md#9-momentum-clumping-the-founding-image-tested) (ii)). Because the interaction is attractive, the condensate collapses whenever it exceeds a [critical mass](../wave-dark-matter/attractive-condensates.md) and ejects part of its mass as fast waves, so the galaxy's dark matter is drained. Observed ultra-faint dwarfs are dense and old, so Scenario A is "**falsified** by observed UFD density and longevity", with UFD an ultra-faint dwarf, and "the light-mass escape is closed independently [15†, Lyman-α]" ([#11 §9](../../papers/broken-born-checkpoint-v2.md#9-momentum-clumping-the-founding-image-tested) (ii)). Scenario A is under review ([#11 §9](../../papers/broken-born-checkpoint-v2.md#9-momentum-clumping-the-founding-image-tested); [Under review: Scenario A and the ultra-faint-dwarf endpoint](wave-island/scenario-a.md)). [#4](../../../notes/ufd-endpoint.md)'s robustness check: "shrinking v\* makes it worse …; growing v\* leaves R unchanged; κ < 1 is by definition Scenario B. No parameter direction rescues it." (#4, 'The data').

### "Decorative": the free wave

Under [Scenario B](wave-island/scenario-b.md), dwarf cores come from something else, "fuzzy-end quantum pressure at m ~ 10⁻²² eV, or baryonic feedback", and the coupling is free (#3). The first option lies below the wave island's lower edge of 3×10⁻¹⁹ eV, which #4 draws from the fuzzy-dark-matter bounds; neither note addresses this, and the question is unresolved. The stream condition then holds over a window of the mean-field parameter X ≡ gn/(mσ²): "MW numbers, m = 0.1 meV: window X ∈ [5×10⁻¹¹, 1] — ten orders of magnitude. **Verdict B: streams are *tunable*, not mandatory.**" (#3, where MW is the Milky Way). Streams can be switched on or off by choosing the coupling, so their presence or absence tests nothing. #3, on the granularity prediction of [old row 3](velocity-granularity.md): "on this branch the granularity prediction is no longer a novel *requirement* of the program, only an option — a degeneration flag." [#11 §15](../../papers/broken-born-checkpoint-v2.md#15-assessment) lists the "tunable wave-island collective sector (quarantined)" among the program's [degeneration risks](../../program/assessment.md) ([Lakatosian methodology](../../method/lakatosian-methodology.md)).

### Why the legs cover the viable space

The mass split is the classicality theorem's: collective behaviour exists only where dark matter is a wave. On the wave island, the coupling is either fixed by the cores of classical dwarfs or it is not, and #4 closes the gap between the two cases by definition: "κ < 1 is by definition Scenario B", where κ is Scenario A's normalization of the condensation rate to dwarf cores. "Viable" excludes the light-mass branch of Scenario A, m ≲ 5×10⁻²¹ eV, which bounds on fuzzy dark matter already rule out (#4, 'The attractive endpoint'; [bounds on fuzzy dark matter](../wave-dark-matter/fuzzy-dark-matter-bounds.md)). The surviving wave island is "roughly 3×10⁻¹⁹ eV ≲ m ≲ 10⁻⁴ eV with Scenario-B couplings" (#4).

## What it withdrew

#4: "Rows 3 and 4 of the predictions table are permanently withdrawn, on both islands. The Fornax mechanism goes with them." These are the [lab notebook](../../history/documents/lab-notebook.md)'s rows, [old row 3](velocity-granularity.md), velocity-space granularity in halos, and [old row 4](fornax-friction.md), suppressed [dynamical friction](../halo-astrophysics/halo-substructure.md) in condensed dwarf cores. #3 had kept a "surviving descendant of old rows 3–4", a signature in ultra-faint dwarfs, which is Scenario A's own prediction; #4 follows it to an endpoint that the observed ultra-faint dwarfs contradict (Scenario A is under review). [#11 §13](../../papers/broken-born-checkpoint-v2.md#13-predictions-and-kill-conditions) lists both rows as withdrawn and under review ([history of the predictions table](../../predictions/table-history.md)).

## What survives

[#11 §9](../../papers/broken-born-checkpoint-v2.md#9-momentum-clumping-the-founding-image-tested): "Salvage: the **island discriminant** (knee shape: sharp cutoff ⇒ particle χ; (v\*/σ)⁴ ⇒ wave χ) and free relic abundance via misalignment on the wave island".

- [The island discriminant](../../predictions/island-discriminant.md), row 3 of the current [predictions table](../../predictions/_index.md). The self-interaction of particle dark matter switches off sharply above v\*, while on the wave island the condensation rate falls as (v\*/σ)⁴, a power law. The shape of the [knee](../conjugate-matter/scattering-law.md) would therefore tell the two islands apart. The particle side assumes the Gaussian tail of the notes, which [#11 §8](../../papers/broken-born-checkpoint-v2.md#8-conjugate-matter-and-the-gate) now leaves open.
- [Relic abundance by misalignment](wave-island/misalignment-relic.md) on the wave island.

#4's longer list of what "remains distinctively BBT's own" adds "the exponential cliff + in-gate isotropy (particle island)", which [#11 §8](../../papers/broken-born-checkpoint-v2.md#8-conjugate-matter-and-the-gate) has since turned into a knee with an open tail ([row 1](../../predictions/self-interaction-knee.md), [row 2](../../predictions/scattering-isotropy.md)); "the dark-energy sector (thawing, no-phantom, turnaround — live at DESI DR3)", with [DESI](../../cosmology/dark-energy/desi.md) the Dark Energy Spectroscopic Instrument and DR3 its Data Release 3 (whether the stated potential can turn negative, as [the turnaround](../../cosmology/dark-energy/potential-sign.md) needs, is flag 27 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md), whose addendum of 2026-10-27 finds the turnaround instead in [a closed universe](../../cosmology/scale-factor-duality/closed-universe.md)); and "the permanent nulls (direct detection, monopoles, linear dispersion)", which are rows [7](../../predictions/direct-detection-null.md), [8](../../predictions/monopole-null.md) and [9](../../predictions/photon-dispersion.md) of the current table. The dark-energy item has since come under pressure from DESI's Data Release 2 (DR2): the root [`CLAUDE.md`](../../../CLAUDE.md) records that "DESI DR2 favors a phantom crossing above z ≈ 0.4, against the framework's strict w ≥ −1", where w is dark energy's [equation of state](../../cosmology/dark-energy/quintessence.md#dark-energy-and-the-equation-of-state), its pressure divided by its energy density; z is the [redshift](../../cosmology/scale-factor-duality/redshift.md), the stretching of light by the expansion of the universe since the light was emitted (larger z means earlier); and −1 is the value of w for a cosmological constant. It also records that "The dark-energy sector is under real pressure ahead of DR3" ([the phantom crossing](../../cosmology/dark-energy/desi-dr2-phantom-crossing.md)).

## Scope

- **Collective dynamics only.** The theorem concerns the collective behaviour of many particles or of a wave field. "The clumping loophole — topological momentum-space localization of individual objects — remains untested; its candidate is P.R.'s conjecture of conjugate monopoles" ([#11 §12](../../papers/broken-born-checkpoint-v2.md#12-the-dark-sector-question-three-candidates-and-the-failure-of-one-model); [the topological loophole](topological-loophole.md); [Conjecture: magnetic monopoles abundant in momentum space](../candidates/momentum-space-monopoles.md)).
- **The level of the estimates.** The particle leg rests on a mean-field criterion bracketed by two limits. The wave legs rest on a condensation rate whose coefficients are "heuristic at O(1)–O(10) level" and await calibration against Levkov–Panin–Tkachev numerics (#3, header; [wave kinetics](../wave-dark-matter/wave-kinetics.md)); [#11 §9](../../papers/broken-born-checkpoint-v2.md#9-momentum-clumping-the-founding-image-tested) tags them "coefficients [O]". The notes argue that the verdicts survive these uncertainties: the particle side is "Robust to every dropped O(1)" (#2), and in Segue 1 "There is no timescale refuge" even after allowing for the slower growth seen in Levkov–Panin–Tkachev-type kinetics (#4, 'Sharpened input numbers').
- **A contact-range interaction.** The theorem concerns the program's own interaction, which acts on contact. It says that velocity clumping is required nowhere, not that clumping cannot happen. A long-range attraction among χ gated in relative velocity is a different model, which the clumping problem never tested; the momentum-gravity note of 2026-10-28 (computed, not reviewed) finds that any clumping it produced would be "decorative" "in the net theorem's own word" ([`notes/velocity-gated-gravity.md`](../../../notes/velocity-gated-gravity.md) §§4, 7; [the scope of the tests](founding-image.md#the-scope-of-the-tests); [Conjecture: a long-range velocity-gated attraction among χ](long-range-gated-attraction.md)).
- **The gate's mechanism.** Flag 55 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md) proposes that the gate's mechanism is not derived ([the gate mechanism](../conjugate-matter/gate-mechanism.md#exchanging-x-cannot-produce-the-gate)). The note behind it finds the clumping results unaffected and, if anything, strengthened: "a completion whose only velocity dependence is a knee in σ_T(v) leaves the forward amplitude, which drives collective behaviour, ungated" ([`notes/gate-mechanism.md` §5](../../../notes/gate-mechanism.md#5-what-follows-for-the-record)).
- **Machine-checked in part.** Section D of [`verify/velocity_gated_gravity.py`](../../../verify/velocity_gated_gravity.py) reproduces calc note #2's shortfall ratios, 3.9×10⁻²⁸ and 2.9×10⁻³¹; no `verify/` script covers a number of the wave legs ([the iron rule](../../method/verification/iron-rule.md)).

## Record

- #4 first stated the theorem and closed the clumping problem: "Verdict: Scenario A falsified; the clumping problem closed."
- The lab notebook's addendum v0.2 summarizes it: "**Net:** velocity-space clumping is nowhere a mandatory prediction of BBT." It adds that "open problems 3 and 5 close (5 via misalignment production on the wave island)"; #3 limits the relic-abundance closure to the wave island, and [#11 §12](../../papers/broken-born-checkpoint-v2.md#12-the-dark-sector-question-three-candidates-and-the-failure-of-one-model) keeps the ratio of dark to ordinary matter open for all three candidates.
- [#9 §7](../../../notes/broken-born-program-v1.md#7-the-death-of-momentum-clumping-the-clumping-problem-closed-negative) lists it as the third of "Three results [D]", in the form "forbidden (particles), fatal (wave, committed coupling), decorative (wave, free coupling)".
- [#11 §9](../../papers/broken-born-checkpoint-v2.md#9-momentum-clumping-the-founding-image-tested) (iii) carries it into the current checkpoint without a separate tag.

## Sources

- [`notes/ufd-endpoint.md`](../../../notes/ufd-endpoint.md) 'Verdict and closure of the clumping problem' — the theorem as first stated, the withdrawals, the salvage list and the final wave-island range; 'The data' — the robustness checks; 'The attractive endpoint' — the light-mass branch; 'Sharpened input numbers' — no timescale refuge
- [`wiki/papers/broken-born-checkpoint-v2.md` §9](../../papers/broken-born-checkpoint-v2.md#9-momentum-clumping-the-founding-image-tested) — the three results and the salvage, the results standing, the founding image as P.R.'s open conjecture, Scenario A under review; [§13](../../papers/broken-born-checkpoint-v2.md#13-predictions-and-kill-conditions) — the withdrawn rows under review; [§8](../../papers/broken-born-checkpoint-v2.md#8-conjugate-matter-and-the-gate) — the open tail; [§1](../../papers/broken-born-checkpoint-v2.md#1-two-abstracts) — the abstract's summary; [§12](../../papers/broken-born-checkpoint-v2.md#12-the-dark-sector-question-three-candidates-and-the-failure-of-one-model) — the loophole; [§15](../../papers/broken-born-checkpoint-v2.md#15-assessment) — the quarantined wave-island sector
- [`notes/stream-stability.md`](../../../notes/stream-stability.md) 'Corollary (the classicality theorem)' — the particle leg
- [`notes/wave-island.md`](../../../notes/wave-island.md) 'What pins g? Two scenarios' — Scenarios A and B and the degeneration flag; 'Standing results after Chunks A+B' — the interim standing
- [`notes/broken-born-program-v1.md` §7](../../../notes/broken-born-program-v1.md#7-the-death-of-momentum-clumping-the-clumping-problem-closed-negative) — the [D] tag on the three clumping results
- [`notes/broken-born-theory.md`](../../../notes/broken-born-theory.md) 'Addendum (v0.2)' — the notebook's "Net" summary
- [`CLAUDE.md`](../../../CLAUDE.md) 'Since the handoff' — the dark-energy sector "under real pressure" since the second data release
- [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md) items 19, 27 — the regime of the classicality corollary; the sign of the dark-energy potential, with its addendum; items 16 (addendum), 55, 58 — the shortfall now gated, the gate's mechanism, #2's narrow-gate criterion; all pending
- [`notes/velocity-gated-gravity.md` §4](../../../notes/velocity-gated-gravity.md#4-what-the-obituary-covers) — the scope of the tests; [§7](../../../notes/velocity-gated-gravity.md#7-what-clumping-needs-and-why-the-variant-is-decorative) — the long-range variant "decorative"
- [`notes/gate-mechanism.md` §5](../../../notes/gate-mechanism.md#5-what-follows-for-the-record) — the clumping results unaffected by the mechanism's status
- [`verify/velocity_gated_gravity.py`](../../../verify/velocity_gated_gravity.py) section D — calc note #2's shortfall ratios
- [`notes/closed-universe.md` §2](../../../notes/closed-universe.md#2-the-premise-and-the-turnaround-it-buys) — the turnaround in a closed universe
