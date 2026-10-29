---
title: "The net theorem: clumping is nowhere mandatory"
weight: 70
status: alive
description: "Velocity-space clumping is forbidden for particles, fatal where mandatory for waves, and decorative elsewhere — the summary result of the clumping problem."
provenance: [D]
sources:
  - "notes/ufd-endpoint.md 'Verdict and closure'"
  - "notes/ufd-endpoint.md 'The data'"
  - "notes/ufd-endpoint.md 'Sharpened input numbers'"
  - "notes/ufd-endpoint.md 'The attractive endpoint'"
  - "papers/broken-born-checkpoint-v2.md §9"
  - "papers/broken-born-checkpoint-v2.md §1"
  - "papers/broken-born-checkpoint-v2.md §12"
  - "papers/broken-born-checkpoint-v2.md §15"
  - "papers/broken-born-checkpoint-v2.md §8"
  - "notes/stream-stability.md 'Corollary'"
  - "notes/wave-island.md 'What pins g? Two scenarios'"
  - "notes/wave-island.md 'Standing results'"
  - "notes/broken-born-program-v1.md §7"
  - "notes/broken-born-theory.md 'Addendum (v0.2)'"
  - "review/round3-adjudication.md 'Decisions'"
  - "CLAUDE.md 'Since the handoff'"
  - "review/wiki-build-flags.md items 16, 19, 27, 55, 58"
  - "notes/velocity-gated-gravity.md §4"
  - "notes/velocity-gated-gravity.md §7"
  - "notes/gate-mechanism.md §5"
  - "verify/velocity_gated_gravity.py 'D. The obituary's scope'"
  - "notes/closed-universe.md §2"
---

*The net theorem is the summary result of [the clumping problem](/wiki/history/main-problems): in every part of the program's parameter space that survives, dark matter clumping by velocity is never a required phenomenon. For particle dark matter it cannot happen. For wave dark matter it was required only under one assumption about the coupling, [Scenario A](/wiki/dark-matter/momentum-clumping/wave-island/scenario-a), which observation rules out; with the coupling left free, [Scenario B](/wiki/dark-matter/momentum-clumping/wave-island/scenario-b), it is merely optional. The theorem closes the test of the program's [founding image](/wiki/dark-matter/momentum-clumping/founding-image) with a [negative result](/wiki/method/negative-results). It covers collective dynamics only, so whether a single topological object could be localized in momentum is a separate, untested question.*

**Status:** Alive — [D] in #9 §7 ("Three results [D]"); [#11](/wiki/history/documents/checkpoint) §9 states it as result (iii) without a separate tag, resting on (i) [D] and (ii) [D + T]. Collective dynamics only, at the level of the calc notes' mean-field and wave-kinetic estimates. Machine-checked in part: since 2026-10-28 section D of `verify/velocity_gated_gravity.py` reproduces the particle leg's shortfall ratios (flag 16, addendum; [the velocity-gated-gravity script](/wiki/method/verification/velocity-gated-gravity-script)); no `verify/` script covers the wave legs.

## Statement

As first stated, in [the note that closed the clumping problem](/wiki/history/documents/clumping-notes), where BBT is Broken-Born theory, the program's earlier name (`notes/ufd-endpoint.md`, 'Verdict and closure of the clumping problem'):

> **Nowhere in the viable parameter space of BBT is velocity-space clumping a mandatory phenomenon.** It is forbidden for classical-particle χ, fatal where it would have been mandatory (Scenario A), and merely optional elsewhere (Scenario B, ten tunable orders of magnitude — a degeneration flag, not a prediction).

The checkpoint's form, #11 §9 (iii): "**Net theorem:** velocity-space clumping is nowhere mandatory — forbidden (particles), fatal (committed wave), decorative (free wave)." Its technical abstract: "collective momentum-space clumping is proven non-mandatory everywhere and falsified where it would have been mandatory" (#11 §1).

"Mandatory" is the operative word. A program's prediction counts only if the program requires it; a phenomenon the program merely permits, at a tunable strength, tests nothing. The theorem says that velocity clumping is never in the first class.

## The three legs

The parameter space divides first by mass, through [the classicality theorem](/wiki/dark-matter/momentum-clumping/classicality-theorem), and then, on the wave side, by what fixes the coupling. Each part gets one verdict.

### Forbidden: classical particles [D]

On the particle island, dark-matter particles with masses of MeV to GeV, the stream instability needs the attraction energy of co-moving particles to reach their kinetic energy. At the [scattering benchmark](/wiki/dark-matter/conjugate-matter/benchmark), where the coupling is fixed by dwarf-galaxy cores, [the mean-field criterion](/wiki/dark-matter/momentum-clumping/instability-criterion) fails by 10²⁸–10³¹. Calc note #2's narrow-gate form of the criterion overstates the Milky Way shortfall about 3×, and the verdict is unchanged (flag 58 in `review/wiki-build-flags.md`; [the narrow-gate form, flagged](/wiki/dark-matter/momentum-clumping/instability-criterion#the-narrow-gate-form-flagged)). Below threshold there is no growth, and collisions only drive the gas toward a Maxwellian. Meeting the criterion at fixed cross-section per mass would need m ≲ 0.1 meV, where about 10²⁰ quanta share each state and dark matter is a wave (#11 §9 (i); on the regime in which calc note #2 evaluates that mass, see flag 19 in `review/wiki-build-flags.md`). #2's summary: "Collective velocity-space dynamics and classical-particle dark matter are mutually exclusive within this framework."

### Fatal: the committed wave [D + T]

On the [wave island](/wiki/dark-matter/momentum-clumping/wave-island), the gated attraction condenses the wave field at a rate [Γ_self](/wiki/dark-matter/momentum-clumping/wave-island/condensation-rate). Streams need this rate to beat orbital stirring, Γ_self ≳ Ω = 1/t_dyn, with t_dyn the dynamical time of the system. Under [Scenario A](/wiki/dark-matter/momentum-clumping/wave-island/scenario-a), the same gated channel makes the cores of classical dwarf galaxies, which fixes the coupling; "committed" in #11's phrase means this. Then streams lose to stirring "everywhere by 10²–10⁴ — *except ultra-faint dwarfs*" (#3). In the [ultra-faint dwarf galaxies](/wiki/dark-matter/halo-astrophysics/dwarf-galaxies) condensation is mandatory: for Segue 1, "rate ratio ~660; condensation ~10⁴ yr" (#11 §9 (ii)). Because the interaction is attractive, the condensate collapses whenever it exceeds a [critical mass](/wiki/dark-matter/wave-dark-matter/attractive-condensates) and ejects part of its mass as fast waves, so the galaxy's dark matter is drained. Observed ultra-faint dwarfs are dense and old, so Scenario A is "**falsified** by observed UFD density and longevity", with UFD an ultra-faint dwarf, and "the light-mass escape is closed independently [15†, Lyman-α]" (#11 §9 (ii)). #4's robustness check: "shrinking v\* makes it worse …; growing v\* leaves R unchanged; κ < 1 is by definition Scenario B. No parameter direction rescues it." (#4, 'The data').

### Decorative: the free wave

Under [Scenario B](/wiki/dark-matter/momentum-clumping/wave-island/scenario-b), dwarf cores come from something else, "fuzzy-end quantum pressure at m ~ 10⁻²² eV, or baryonic feedback", and the coupling is free (#3). The first option lies below the wave island's lower edge of 3×10⁻¹⁹ eV, which #4 draws from the fuzzy-dark-matter bounds; neither note addresses this, and the question is unresolved. The stream condition then holds over a window of the mean-field parameter X ≡ gn/(mσ²): "MW numbers, m = 0.1 meV: window X ∈ [5×10⁻¹¹, 1] — ten orders of magnitude. **Verdict B: streams are *tunable*, not mandatory.**" (#3, where MW is the Milky Way). Streams can be switched on or off by choosing the coupling, so their presence or absence tests nothing. #3: "on this branch the granularity prediction is no longer a novel *requirement* of the program, only an option — a degeneration flag." #11 §15 lists the "tunable wave-island collective sector (quarantined)" among the program's [degeneration risks](/wiki/program/assessment) ([Lakatosian methodology](/wiki/method/lakatosian-methodology)).

### Why the legs cover the viable space

The mass split is the classicality theorem's: collective behaviour exists only where dark matter is a wave. On the wave island, the coupling is either fixed by the cores of classical dwarfs or it is not, and #4 closes the gap between the two cases by definition: "κ < 1 is by definition Scenario B", where κ is Scenario A's normalization of the condensation rate to dwarf cores. "Viable" excludes the light-mass branch of Scenario A, m ≲ 5×10⁻²¹ eV, which bounds on fuzzy dark matter already rule out (#4, 'The attractive endpoint'; [bounds on fuzzy dark matter](/wiki/dark-matter/wave-dark-matter/fuzzy-dark-matter-bounds)). The surviving wave island is "roughly 3×10⁻¹⁹ eV ≲ m ≲ 10⁻⁴ eV with Scenario-B couplings" (#4).

## What it withdrew

#4: "Rows 3 and 4 of the predictions table are permanently withdrawn, on both islands. The Fornax mechanism goes with them." These are the [lab notebook](/wiki/history/documents/lab-notebook)'s rows, [old row 3](/wiki/dark-matter/momentum-clumping/velocity-granularity), velocity-space granularity in halos, and [old row 4](/wiki/dark-matter/momentum-clumping/fornax-friction), suppressed [dynamical friction](/wiki/dark-matter/halo-astrophysics/halo-substructure) in condensed dwarf cores. #3 had kept a "surviving descendant of old rows 3–4", a signature in ultra-faint dwarfs; it died with Scenario A. #11 §13 lists both rows under "Withdrawn with cause" ([history of the predictions table](/wiki/predictions/table-history)).

## What survives

#11 §9: "Salvage: the **island discriminant** (knee shape: sharp cutoff ⇒ particle χ; (v\*/σ)⁴ ⇒ wave χ) and free relic abundance via misalignment on the wave island".

- [The island discriminant](/wiki/predictions/island-discriminant), row 3 of the current [predictions table](/wiki/predictions). The self-interaction of particle dark matter switches off sharply above v\*, while on the wave island the condensation rate falls as (v\*/σ)⁴, a power law. The shape of the [knee](/wiki/dark-matter/conjugate-matter/scattering-law) would therefore tell the two islands apart. The particle side assumes the Gaussian tail of the notes, which #11 §8 now leaves open.
- [Relic abundance by misalignment](/wiki/dark-matter/momentum-clumping/wave-island/misalignment-relic) on the wave island.

#4's longer list of what "remains distinctively BBT's own" adds "the exponential cliff + in-gate isotropy (particle island)", which #11 §8 has since turned into a knee with an open tail ([row 1](/wiki/predictions/self-interaction-knee), [row 2](/wiki/predictions/scattering-isotropy)); "the dark-energy sector (thawing, no-phantom, turnaround — live at DESI DR3)", with [DESI](/wiki/cosmology/dark-energy/desi) the Dark Energy Spectroscopic Instrument and DR3 its Data Release 3 (whether the stated potential can turn negative, as [the turnaround](/wiki/cosmology/dark-energy/potential-sign) needs, is flag 27 in `review/wiki-build-flags.md`, whose addendum of 2026-10-27 finds the turnaround instead in [a closed universe](/wiki/cosmology/scale-factor-duality/closed-universe)); and "the permanent nulls (direct detection, monopoles, linear dispersion)", which are rows [7](/wiki/predictions/direct-detection-null), [8](/wiki/predictions/monopole-null) and [9](/wiki/predictions/photon-dispersion) of the current table. The dark-energy item has since come under pressure from DESI's Data Release 2 (DR2): the root `CLAUDE.md` records that "DESI DR2 favors a phantom crossing above z ≈ 0.4, against the framework's strict w ≥ −1" and that "The dark-energy sector is under real pressure ahead of DR3" ([the phantom crossing](/wiki/cosmology/dark-energy/desi-dr2-phantom-crossing)).

## Scope

- **Collective dynamics only.** The theorem concerns the collective behaviour of many particles or of a wave field. "The clumping loophole — topological momentum-space localization of individual objects — remains untested, but has no candidate" (#11 §12; [the topological loophole](/wiki/dark-matter/momentum-clumping/topological-loophole)).
- **The level of the estimates.** The particle leg rests on a mean-field criterion bracketed by two limits. The wave legs rest on a condensation rate whose coefficients are "heuristic at O(1)–O(10) level" and await calibration against Levkov–Panin–Tkachev numerics (#3, header; [wave kinetics](/wiki/dark-matter/wave-dark-matter/wave-kinetics)); #11 §9 tags them "coefficients [O]". The notes argue that the verdicts survive these uncertainties: the particle side is "Robust to every dropped O(1)" (#2), and in Segue 1 "There is no timescale refuge" even after allowing for the slower growth seen in Levkov–Panin–Tkachev-type kinetics (#4, 'Sharpened input numbers').
- **A contact-range interaction.** The theorem concerns the program's own interaction, which acts on contact. It says that velocity clumping is required nowhere, not that clumping cannot happen. A long-range attraction among χ gated in relative velocity is a different model, which the clumping problem never tested; the momentum-gravity note of 2026-10-28 (computed, not reviewed) finds that any clumping it produced would be "decorative" "in the net theorem's own word" (`notes/velocity-gated-gravity.md` §§4, 7; [what the obituary covers](/wiki/dark-matter/momentum-clumping/founding-image#what-the-obituary-covers); [Conjecture: a long-range velocity-gated attraction among χ](/wiki/dark-matter/momentum-clumping/long-range-gated-attraction)).
- **The gate's mechanism.** Flag 55 in `review/wiki-build-flags.md` proposes that the gate's mechanism is not derived ([the gate mechanism](/wiki/dark-matter/conjugate-matter/gate-mechanism#exchanging-x-cannot-produce-the-gate)). The note behind it: "The velocity-clumping obituary is unaffected. If anything it is strengthened: a completion whose only velocity dependence is a knee in σ_T(v) leaves the forward amplitude, which drives collective behaviour, ungated" (`notes/gate-mechanism.md` §5).
- **Machine-checked in part.** Section D of `verify/velocity_gated_gravity.py` reproduces calc note #2's shortfall ratios, 3.9×10⁻²⁸ and 2.9×10⁻³¹; no `verify/` script covers a number of the wave legs ([the iron rule](/wiki/method/verification/iron-rule)).

## Later use

[The round-3 adjudication](/wiki/method/review/round-3/decisions) cited the clumping obituary as a precedent for retiring [the soliton candidate](/wiki/dark-matter/candidates/soliton-candidate) (`review/round3-adjudication.md`, 'Decisions').

## Record

- #4 first stated the theorem and closed the clumping problem: "Verdict: Scenario A falsified; the clumping problem closed."
- The lab notebook's addendum v0.2 summarizes it: "**Net:** velocity-space clumping is nowhere a mandatory prediction of BBT." It adds that "open problems 3 and 5 close (5 via misalignment production on the wave island)"; #3 limits the relic-abundance closure to the wave island, and #11 §12 keeps the ratio of dark to ordinary matter open for both candidates.
- #9 §7 lists it as the third of "Three results [D]", in the form "forbidden (particles), fatal (wave, committed coupling), decorative (wave, free coupling)".
- #11 §9 (iii) carries it into the current checkpoint without a separate tag.

## Sources

- `notes/ufd-endpoint.md` 'Verdict and closure of the clumping problem' — the theorem as first stated, the withdrawals, the salvage list and the final wave-island range; 'The data' — the robustness checks; 'The attractive endpoint' — the light-mass branch; 'Sharpened input numbers' — no timescale refuge
- `papers/broken-born-checkpoint-v2.md` §9 — the three results and the salvage; §8 — the open tail; §1 — the abstract's summary; §12 — the loophole; §15 — the quarantined wave-island sector
- `notes/stream-stability.md` 'Corollary (the classicality theorem)' — the particle leg
- `notes/wave-island.md` 'What pins g? Two scenarios' — Scenarios A and B and the degeneration flag; 'Standing results after Chunks A+B' — the interim standing
- `notes/broken-born-program-v1.md` §7 — the [D] tag on the three clumping results
- `notes/broken-born-theory.md` 'Addendum (v0.2)' — the notebook's "Net" summary
- `review/round3-adjudication.md` 'Decisions' — the clumping obituary as precedent
- `CLAUDE.md` 'Since the handoff' — the dark-energy sector "under real pressure" since the second data release
- `review/wiki-build-flags.md` items 19, 27 — the regime of the classicality corollary; the sign of the dark-energy potential, with its addendum; items 16 (addendum), 55, 58 — the shortfall now gated, the gate's mechanism, #2's narrow-gate criterion; all awaiting a ruling
- `notes/velocity-gated-gravity.md` §4 — what the obituary covers; §7 — the long-range variant "decorative"
- `notes/gate-mechanism.md` §5 — the obituary unaffected by the mechanism's status
- `verify/velocity_gated_gravity.py` section D — calc note #2's shortfall ratios
- `notes/closed-universe.md` §2 — the turnaround in a closed universe
