---
title: "Obituary: velocity clumping, the founding image"
weight: 10
status: dead
description: "The founding picture of dark matter fragmenting into discrete velocity streams — 'the Jeans problem with the roles of x and v exchanged' — how it was tested, and why it died."
provenance: [D, T]
sources:
  - "papers/broken-born-checkpoint-v2.md §9"
  - "papers/broken-born-checkpoint-v2.md App. A item 3"
  - "papers/broken-born-checkpoint-v2.md §12"
  - "papers/broken-born-checkpoint-v2.md §1"
  - "papers/broken-born-checkpoint-v2.md §8"
  - "papers/broken-born-checkpoint-v2.md §13"
  - "review/round3-adjudication.md 'Decisions'"
  - "notes/broken-born-theory.md §5.2"
  - "notes/broken-born-theory.md §5.1"
  - "notes/broken-born-theory.md §9"
  - "notes/broken-born-theory.md §10"
  - "notes/broken-born-theory.md §11 item 3"
  - "notes/broken-born-theory.md 'Addendum (v0.2)'"
  - "notes/stream-stability.md 'Numbers at the scattering benchmark'"
  - "notes/stream-stability.md 'Corollary'"
  - "notes/wave-island.md 'What pins g? Two scenarios'"
  - "notes/ufd-endpoint.md 'Verdict and closure'"
  - "notes/broken-born-program-v1.md §7"
  - "HANDOFF.md §2"
  - "popsci/angle-of-the-mirror.md 'The wager'"
  - "popsci/angle-of-the-mirror.md 'The killing fields'"
  - "review/wiki-build-flags.md items 16, 19, 58"
  - "notes/velocity-gated-gravity.md §4"
  - "notes/velocity-gated-gravity.md §2"
  - "notes/velocity-gated-gravity.md §3"
  - "notes/velocity-gated-gravity.md §5"
  - "notes/velocity-gated-gravity.md §6"
  - "notes/velocity-gated-gravity.md §7"
  - "notes/velocity-gated-gravity.md §8"
  - "review/wiki-build-checks/stream_stability_check.out"
  - "verify/velocity_gated_gravity.py 'D. The obituary's scope'"
  - "notes/gate-mechanism.md §5"
---

*Velocity clumping was the program's founding picture of dark matter: a smooth dark-matter halo would break up into a few streams, each made of particles moving with nearly the same velocity, so that dark matter clumps in velocity instead of in position. The [lab notebook](/wiki/history/documents/lab-notebook) described it as the [Jeans problem](/wiki/dark-matter/momentum-clumping/vlasov-stability), the gravitational instability that makes lumps in space, with the roles of position and velocity exchanged. The clumping calculation tested it and found it impossible for particle dark matter, fatal where it would be mandatory for wave dark matter, and merely optional elsewhere. The claim is dead as dynamics and stays dead.*

**Status:** Dead — killed by [the clumping problem](/wiki/history/main-problems): [D] on the particle island and [D + T] on the [wave island](/wiki/dark-matter/momentum-clumping/wave-island) ([#11](/wiki/history/documents/checkpoint) §9). Founding supposition 3, "Matter clumps in momentum space", is "dead as dynamics" (#11 App. A item 3; [founding suppositions](/wiki/program/founding-suppositions)), and [the handoff](/wiki/history/documents/handoff) lists it among its dead claims, to be kept dead (`HANDOFF.md` §2). Since 2026-10-28 `verify/velocity_gated_gravity.py` (section D) reproduces calc note #2's two shortfall ratios in the gate; #11 §9's tag stays [D] until Paul rules, and no script covers the other clumping numbers (flag 16 in `review/wiki-build-flags.md`, addendum; [the velocity-gated-gravity script](/wiki/method/verification/velocity-gated-gravity-script)). The obituary covers the program's contact-range interaction; a long-range attraction gated in relative velocity is a different model ([what the obituary covers](#what-the-obituary-covers)). Home section: [momentum clumping](/wiki/dark-matter/momentum-clumping); listed in [the graveyard](/wiki/status/graveyard).

## What was claimed

### The picture

The program began from P.R.'s supposition that "Matter clumps in momentum space" (#11 App. A, item 3). In the program's terms, dark matter is [conjugate matter](/wiki/dark-matter/conjugate-matter), matter polarized toward momentum, and its own force "operates only between particles moving at nearly the same velocity — a gate in relative speed" (#11 §8, plain-language passage). With an attraction that acts only between particles of similar velocity, the expectation was that dark matter would gather in velocity rather than in position. The popular article #10 states the image as "dark matter as invisible flocks, clumping not in space but in *speed*" (`popsci/angle-of-the-mirror.md`, 'The wager').

The lab notebook made this a mean-field claim in §5.2, titled "Collective behavior: clumping in momentum space" and tagged "[D at mean-field level; O beyond]". Its starting point is the energy of one particle in the gas:

```text
ε(p; f) = p²/2m_χ + ∫d³p′ U(p − p′) f̄(p′),     ẋ ⊃ ∇ₚε
```

"The genuinely p-local part of the interaction shifts a particle's energy by the phase-space density of *co-moving* neighbors". Here U is an interaction that depends on the momentum difference p − p′ and f̄ the averaged phase-space density. Because the energy depends on momentum through the neighbours, the velocity ẋ = ∇ₚε acquires a term beyond p/m_χ: "an anomalous velocity, the same structure as Berry-curvature transport in solids". In a crystal, the Berry curvature of an electron band adds an anomalous term to the electron's velocity, proportional to the applied force crossed with the curvature [T]; the notebook asserts the structural analogy without working out the correspondence.

### The instability

The claim proper:

> For attractive U with momentum range μ, the collisionless Boltzmann equation with this mean field is the Jeans problem *with the roles of x and v exchanged*: a smooth Maxwellian f(v) is unstable to fragmentation into **discrete velocity streams of width Δv ~ v\***, each spatially delocalized and internally coherent across kiloparsecs.

In the ordinary Jeans problem, self-gravity depends on the particles' separation in position, and in a uniform gas, perturbations longer than the Jeans length grow into lumps in space ([the Jeans instability](/wiki/dark-matter/momentum-clumping/vlasov-stability#the-static-threshold-and-the-jeans-instability)) [T]. The notebook's exchanged problem has the attraction acting between particles close in velocity, within the [velocity gate](/wiki/dark-matter/conjugate-matter/velocity-gate) of width v\*, and expects lumps in velocity: streams spread through space, each with a narrow spread of velocities around its own mean.

### The analogy with superconductivity

The notebook continued: "The BCS analogy is exact in structure: a momentum-gated attraction is precisely the pairing interaction, and below a critical velocity dispersion the core of a halo condenses — momentum-space clumping, realized." BCS is the Bardeen–Cooper–Schrieffer theory of superconductivity, in which an attraction acting only between electrons within a thin shell of momentum near the Fermi surface makes the electron gas unstable to pairing below a critical temperature [T]. In the notebook's analogy, the halo's [velocity dispersion](/wiki/dark-matter/halo-astrophysics/velocity-dispersion#the-maxwellian-and-the-dynamical-temperature) plays the role of the temperature.

### What it was meant to explain

The notebook drew two consequences: "superfluid-like cores in dwarfs and **suppressed dynamical friction** inside them (the Fornax globular-cluster timing problem is a feature, not a bug)". In its [prediction table](/wiki/predictions/table-history) (`notes/broken-born-theory.md` §9) these became two rows:

- **Row 3**, velocity-space granularity: "Fragmentation into O(10) macro-streams of width ~v\*, coherent over kpc", visible in the perturbations of cold [stellar streams](/wiki/dark-matter/halo-astrophysics/halo-substructure) ([old row 3](/wiki/dark-matter/momentum-clumping/velocity-granularity));
- **Row 4**, friction in dwarf cores: "Suppressed in condensed cores; Fornax GCs stay put", with GCs the globular clusters ([old row 4](/wiki/dark-matter/momentum-clumping/fornax-friction)).

Row 3 was one of the notebook's three "flagship discriminants". Its parameter count credited the two conjugate-matter parameters with "stream granularity scale, friction suppression" among the phenomena covered (§10). The checkpoint's abstract calls velocity clumping the program's "most cherished consequence" (#11 §1).

## How it was tested

The notebook left one step undone and said so: "The growth rate γ versus orbital phase-mixing remains to be computed; it is the theory's most important undone calculation on the astrophysics side. **[O]**" (§5.2). Its open-problem list carries it as item 3, the stream-instability growth rate, which "determines whether Prediction 3's granularity survives in Milky-Way-like halos" (§11).

That calculation became the clumping problem, one of the program's [three main problems](/wiki/history/main-problems), and three short calc notes carried it out ([the clumping calc notes](/wiki/history/documents/clumping-notes)):

1. `notes/stream-stability.md` built [the gated Vlasov model](/wiki/dark-matter/momentum-clumping/gated-vlasov-model), the notebook's mean-field picture made explicit with a Gaussian gate and a contact interaction, and computed its stability threshold with standard [Vlasov stability theory](/wiki/dark-matter/momentum-clumping/vlasov-stability). Result: "negative on the particle island, with a structural corollary."
2. `notes/wave-island.md` followed the corollary to very light, wave-like dark matter and computed the gated [condensation rate](/wiki/dark-matter/momentum-clumping/wave-island/condensation-rate) there. Result: "rate derived, environments evaluated, verdict reached."
3. `notes/ufd-endpoint.md` followed the one case in which clumping was mandatory, [Scenario A](/wiki/dark-matter/momentum-clumping/wave-island/scenario-a), to its endpoint in the faintest galaxies. Result: "Scenario A falsified; the clumping problem closed."

## Why it failed

### Particles: the attraction falls short by 28–31 orders of magnitude [D]

The threshold for streams is the [mean-field criterion](/wiki/dark-matter/momentum-clumping/instability-criterion): the attraction energy among co-moving particles must reach the kinetic energy of their random motion, g·n_gate ≥ m·min(σ, v\*)². At the [scattering benchmark](/wiki/dark-matter/conjugate-matter/benchmark), the coupling is already fixed by fitting dwarf-galaxy cores, and the criterion fails: the ratio is about 10⁻²⁸ in a dwarf core and 10⁻³¹ in the Milky Way's halo near the Sun (#2). Below threshold there is no growth: a ripple in the velocity distribution is Landau-damped, so the race against orbital mixing that the notebook planned never begins. Collisions do not help: "The H-theorem closes the collisional back door: gated collisions still maximize entropy; equilibrium is Maxwellian to one part in 10³⁰" (#2).

The checkpoint's summary: "Mean-field criterion g·n_gate ≥ m·min(σ,v\*)² fails by 10²⁸–10³¹ at the scattering benchmark; below threshold there is no growth; the H-theorem closes the collisional route" (#11 §9 (i)).

### The corollary: collective behaviour requires a wave [D]

Meeting the criterion at fixed cross-section per mass "forces m ≲ 0.1 meV, where N_occ ~ 10²⁰" (#11 §9 (i); on the regime in which calc note #2 evaluates that mass, see flag 19 in `review/wiki-build-flags.md`): at such masses about 10²⁰ quanta share each quantum state, and dark matter is a classical wave, not a gas of particles. This is [the classicality theorem](/wiki/dark-matter/momentum-clumping/classicality-theorem). The notebook's χ was a classical particle, at a benchmark mass of about 70 MeV (`notes/broken-born-theory.md` §5.1); for classical particles the instability does not occur.

### Waves: fatal where mandatory [D + T]

On the [wave island](/wiki/dark-matter/momentum-clumping/wave-island), the gated attraction can condense the wave field into narrow ranges of momentum, at a rate [Γ_self](/wiki/dark-matter/momentum-clumping/wave-island/condensation-rate). Whether that makes streams depends on what fixes the coupling (#3, 'What pins g? Two scenarios'):

- **Scenario A**, the gated channel also makes the dwarf cores. Then the coupling is fixed, and condensation outruns orbital stirring only in [ultra-faint dwarf galaxies](/wiki/dark-matter/halo-astrophysics/dwarf-galaxies), where it is mandatory. Because the attraction makes the condensate collapse above a [critical mass](/wiki/dark-matter/wave-dark-matter/attractive-condensates), the endpoint is a cycle of collapses that ejects dark matter from the galaxy. #11 §9 (ii): the endpoint "drains the halo — **falsified** by observed UFD density and longevity", where UFD stands for ultra-faint dwarf. Segue 1, the test case, is dense and old ([Scenario A](/wiki/dark-matter/momentum-clumping/wave-island/scenario-a)).
- **Scenario B**, the cores come from elsewhere and the coupling is free. Then "streams are tunable across ~10 orders: optional, never required" (#11 §9 (ii); [Scenario B](/wiki/dark-matter/momentum-clumping/wave-island/scenario-b)).

### The verdict

[The net theorem](/wiki/dark-matter/momentum-clumping/net-theorem): "velocity-space clumping is nowhere mandatory — forbidden (particles), fatal (committed wave), decorative (free wave)" (#11 §9 (iii)). The notebook's addendum v0.2 opens: "The clumping problem is settled, and the answer went against the theory." Rows 3 and 4 were withdrawn permanently on both islands: "Rows 3 and 4 of the predictions table are permanently withdrawn, on both islands. The Fornax mechanism goes with them." (#4).

### What the obituary covers

The obituary tested the program's own interaction, and that interaction acts on contact. Calc note #2 says "the x-range collapsed to contact (range 1/m_φ, microscopic)" and names "the force is contact-range" as one reason its verdict is robust (`notes/velocity-gated-gravity.md` §4). The verdict covers all three branches of that model: forbidden for particle χ, fatal for wave χ whose coupling also makes the dwarf cores, decorative for wave χ with a free coupling. For particle χ the record's "10²⁸–10³¹" quotes the exponents of the two shortfall ratios; the shortfall factors themselves are 2.6×10²⁷ and 3.5×10³⁰ (§4; flag 16, addendum). It says that velocity clumping is required nowhere. It does not say that clumping cannot happen.

On 2026-10-26 P.R. asked whether the obituary is premature, and whether momentum gravity would look like a perturbation of gravity that depends on two bodies' relative velocity. The answer, in `notes/velocity-gated-gravity.md` (2026-10-28, not reviewed), is no to both:

- **Between ordinary bodies**, the [momentum graviton X](/wiki/gravity/momentum-graviton) adds a Yukawa term of range below 37.7 μm in the aligned vacuum (u = 1), unscreened. Its dependence on relative velocity is the O(v²/c²) spin-2 factor, 1 + 2.40×10⁻⁷ at 120 km/s, against 1 + 3.20×10⁻⁷ for ordinary gravity, not a gate [D][V] (§2). A relative-velocity gate acting between all bodies is bounded to |ε| < 8.7×10⁻⁹ for a Gaussian gate of width 0.3–3000 km/s in the e^{−v²/v_a²} convention, which is v\* = 0.2–2100 km/s in the record's [D; data S] (§3), where ε is the gated term's strength relative to gravity ([X between ordinary bodies](/wiki/gravity/momentum-graviton/ordinary-bodies)).
- **A long-range attraction among χ, gated in relative velocity,** is a different model. The record does not contain it, and the clumping problem never tested it. No field in the record could carry it (§5). At the record's gate width the Lyman-α forest allows ε < 0.057–0.106 in the record's reading, an estimate from compressed data, while velocity-selected clumping needs ε > 1 at every gate width (§§6–7). The force could not make dwarf cores, which would need G̃/G ≈ 3.6×10³¹, so any clumping it produced would be decorative (§7; [Conjecture: a long-range velocity-gated attraction among χ](/wiki/dark-matter/momentum-clumping/long-range-gated-attraction); [what could carry a relative-velocity gate](/wiki/dark-matter/conjugate-matter/gate-carriers)).
- **Narrow gates**, below about 30 km/s: N-body runs (one agent) found no velocity-selected structure up to ε = 10; one statistic shows a small offset the record does not adjudicate (§8). Corrected estimates, not likelihoods and rerun by one agent, exclude ε ≈ 2 from 10 km/s up, and ε ≈ 3 at 5–30 km/s in one of the two readings (§8).

Calc note #2's threshold for narrow gates is itself flagged: its form overstates the Milky Way shortfall about 3×, and the verdict is unchanged (flag 58 in `review/wiki-build-flags.md`; [the narrow-gate form, flagged](/wiki/dark-matter/momentum-clumping/instability-criterion#the-narrow-gate-form-flagged)). The gate-mechanism note of the same date, which finds that exchanging X cannot produce the program's gate (flag 55), leaves the obituary unaffected: "If anything it is strengthened: a completion whose only velocity dependence is a knee in σ_T(v) leaves the forward amplitude, which drives collective behaviour, ungated" (`notes/gate-mechanism.md` §5; [the gate mechanism](/wiki/dark-matter/conjugate-matter/gate-mechanism#what-flag-55-proposes)).

## What survives

#11 §9: "Salvage: the **island discriminant** (knee shape: sharp cutoff ⇒ particle χ; (v\*/σ)⁴ ⇒ wave χ) and free relic abundance via misalignment on the wave island".

- **[The island discriminant](/wiki/predictions/island-discriminant)**, now row 3 of [the predictions table](/wiki/predictions). The sharpness of the [knee](/wiki/dark-matter/conjugate-matter/scattering-law) in the self-interaction cross-section would tell particle dark matter from wave dark matter. #11 §13 lists it as "(not previously posed)".
- **[Relic abundance by misalignment](/wiki/dark-matter/momentum-clumping/wave-island/misalignment-relic)** on the wave island, which removes the notebook's relic-abundance problem there.
- **The loophole.** The clumping problem tested collective dynamics only. #11 App. A item 3 records: "**loophole**: topological p-localization of individual solitons untested, and its candidate is retired (§12)". The candidate was the superheavy soliton, whose [obituary](/wiki/dark-matter/candidates/soliton-candidate/obituary) is in the candidates section; the loophole now "remains untested, but has no candidate" (#11 §12; [the topological loophole](/wiki/dark-matter/momentum-clumping/topological-loophole)).

[The round-3 adjudication](/wiki/method/review/round-3/decisions) cites this obituary as a precedent for retiring the soliton candidate (`review/round3-adjudication.md`, 'Decisions').

## Where the records differ

- **The handoff's check mark.** The handoff writes "impossible for particle DM (criterion fails by 10²⁸–10³¹ ✓)" (`HANDOFF.md` §2), where ✓ marks a machine-verified claim and DM is dark matter. When the wiki was built no `verify/` script covered any clumping number, and #11 §9 tags the result [D]. The checkpoint governs ([the mean-field criterion](/wiki/dark-matter/momentum-clumping/instability-criterion#verification-record)); the unbacked mark is flag 16 in `review/wiki-build-flags.md`. A recomputation made while building the wiki, `review/wiki-build-checks/stream_stability_check.py`, reproduces the shortfall from #2's inputs, printing `ratio = 3.9e-28` for the dwarf core and `ratio = 2.9e-31` for the Milky Way halo near the Sun (`review/wiki-build-checks/stream_stability_check.out`). It is evidence for a ruling, not part of [the project's gate](/wiki/method/verification/the-gate), `scripts/check.sh`; the flag noted that it "could be moved into `verify/`". Its addendum of 2026-10-28 records the move: `verify/velocity_gated_gravity.py` (section D) "now ports 3a's arithmetic into the gate and reproduces both ratios, with the linearized values beside them (flag 58). The ✓ is now backed by a script; #11 §9's tag [D] is unchanged until Paul rules. "10²⁸–10³¹" quotes the ratios' exponents; the shortfall factors are 2.6×10²⁷ and 3.5×10³⁰" ([the velocity-gated-gravity script](/wiki/method/verification/velocity-gated-gravity-script)).
- **The notebook's body.** The lab notebook's §5.2 and its prediction table were never edited and still read the instability and rows 3–4 as live; the addendum v0.2 records their death ([the lab notebook](/wiki/history/documents/lab-notebook)). The tag "[D at mean-field level; O beyond]" on §5.2 asserted the instability; #2 found its threshold missed by 28–31 orders of magnitude.
- **The plain-language passages** of #9 §7 and #11 §9 describe the image as "dark matter flocking by velocity" and round the shortfall to "a factor of a million trillion trillion" (#9) and "thirty orders of magnitude" (#11). The popular article #10 retells the death in 'The killing fields', rounding the shortfall to "a factor of ten to the thirtieth"; it is never a status source ([the popular articles](/wiki/history/documents/popular-articles)).

## Sources

- `papers/broken-born-checkpoint-v2.md` §9 — the obituary, its tags and the salvage; App. A item 3 — founding supposition 3, "dead as dynamics", and the loophole; §12 — the loophole's current wording; §1 — "most cherished consequence"; §2 — negative results as the most reliable Tier-3 items; §8 — the gate in plain language; §13 — the island discriminant as row 3
- `review/round3-adjudication.md` 'Decisions' — the clumping obituary as precedent
- `notes/stream-stability.md` 'Numbers at the scattering benchmark', 'Corollary (the classicality theorem)' — the particle-island test
- `notes/wave-island.md` 'What pins g? Two scenarios' — the wave-island scenarios
- `notes/ufd-endpoint.md` 'Verdict and closure of the clumping problem' — the falsification and the permanent withdrawal of rows 3–4
- `notes/broken-born-theory.md` §5.2 — the original claim; §5.1 — the benchmark mass; §9 — rows 3–4 and the flagship discriminants; §10 — the parameter count; §11 item 3 — the open problem; 'Addendum (v0.2)' — the notebook's record of the death
- `notes/broken-born-program-v1.md` §7 — the first consolidation's obituary
- `HANDOFF.md` §2 — "keep dead", and the unbacked ✓
- `popsci/angle-of-the-mirror.md` 'The wager', 'The killing fields' — the popular image and retelling (not a status source)
- `review/wiki-build-flags.md` items 16, 19, 58 — the ✓ without a script, and its addendum of 2026-10-28; the regime of the classicality corollary; calc note #2's narrow-gate criterion; all awaiting a ruling
- `notes/velocity-gated-gravity.md` (2026-10-28, not reviewed) §4 — what the obituary covers; §§2–3 — X between ordinary bodies and the universal gate; §§5–8 — the long-range variant and the narrow-gate corner
- `verify/velocity_gated_gravity.py` section D — calc note #2's shortfall ratios in the gate
- `notes/gate-mechanism.md` §5 — the obituary unaffected by flag 55
- `review/wiki-build-checks/stream_stability_check.py` and `review/wiki-build-checks/stream_stability_check.out` — the wiki build's recomputation of the shortfall (outside `verify/`)
