---
title: "Conjecture: velocity clumping, the founding image"
weight: 10
status: conjecture
description: "P.R.'s founding picture of dark matter fragmenting into discrete velocity streams — 'the Jeans problem with the roles of x and v exchanged' — his open conjecture again since #11 v2.5: as collective dynamics it fails for particles by 10²⁸–10³¹, where mandatory for waves it predicts drained ultra-faint dwarfs, which the data contradict, and with a free coupling it is optional; an obituary from v2.0 to v2.4."
provenance: [O]
sources:
  - "papers/broken-born-checkpoint-v2.md §9"
  - "papers/broken-born-checkpoint-v2.md App. A item 3"
  - "papers/broken-born-checkpoint-v2.md header"
  - "papers/broken-born-checkpoint-v2.md §15"
  - "papers/broken-born-checkpoint-v2.md §12"
  - "papers/broken-born-checkpoint-v2.md §1"
  - "papers/broken-born-checkpoint-v2.md §8"
  - "papers/broken-born-checkpoint-v2.md §13"
  - "CLAUDE.md 'Since the handoff'"
  - "CLAUDE.md 'Method'"
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
  - "notes/stream-stability.md 'Status note'"
  - "notes/wave-island.md 'Status note'"
  - "notes/ufd-endpoint.md 'Status note'"
  - "notes/broken-born-program-v1.md §7"
  - "HANDOFF.md §2"
  - "popsci/angle-of-the-mirror.md 'The wager'"
  - "popsci/angle-of-the-mirror.md 'The killing fields'"
  - "review/wiki-build-flags.md items 16, 19, 58"
  - "notes/velocity-gated-gravity.md §4"
  - "notes/velocity-gated-gravity.md 'Status note'"
  - "notes/velocity-gated-gravity.md §1"
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

*Velocity clumping is the program's founding picture of dark matter and P.R.'s conjecture: a smooth dark-matter halo would break up into a few streams, each made of particles moving with nearly the same velocity, so that dark matter clumps in velocity instead of in position. The [lab notebook](/wiki/history/documents/lab-notebook) described it as the [Jeans problem](/wiki/dark-matter/momentum-clumping/vlasov-stability), the gravitational instability that makes lumps in space, with the roles of position and velocity exchanged. The clumping calculation tested it as collective dynamics. For particle dark matter the attraction falls short of the threshold by 28 to 31 orders of magnitude. For wave dark matter, the one case in which clumping would be mandatory predicts that the faintest galaxies have lost their dark matter, and they are, in the checkpoint's words, "the most dark-matter-rich objects known". With the coupling left free, clumping is possible but never required. These results stand. The checkpoint recorded the image as dead from version 2.0 to 2.4; on 2026-10-29 P.R. did not concur in that death, and since version 2.5 it has been his open conjecture again.*

**Status:** Conjecture — [O] — P.R.'s founding supposition 3, "Matter clumps in momentum space", open since [#11](/wiki/history/documents/checkpoint) v2.5 (§9, 'Status (v2.5)'; App. A item 3): on 2026-10-29 Paul did not concur in recording it dead (root `CLAUDE.md`, 'Since the handoff'). As collective dynamics it fails for particle dark matter by 10²⁸–10³¹ (theory), fails the test of the faintest dwarf galaxies where it is mandatory for wave dark matter (data), and is optional for a wave with a free coupling (#11 App. A item 3); the one form the tests did not cover, a single topological object localized in momentum, is untested ([the topological loophole](/wiki/dark-matter/momentum-clumping/topological-loophole)). The tests' results stand, tagged [D] on the particle island and [D + T] on the [wave island](/wiki/dark-matter/momentum-clumping/wave-island) (#11 §9 (i)–(iii); [the evidence](#the-evidence)). Since 2026-10-28 `verify/velocity_gated_gravity.py` (section D) has reproduced calc note #2's two shortfall ratios in the gate; #11 §9's tag stays [D] until Paul rules, and no script covers the other clumping numbers (flag 16 in `review/wiki-build-flags.md`, addendum; [the velocity-gated-gravity script](/wiki/method/verification/velocity-gated-gravity-script)). [Scenario A](/wiki/dark-matter/momentum-clumping/wave-island/scenario-a), the committed-wave case, is under review, not dead. The tests cover the program's contact-range interaction; a long-range attraction gated in relative velocity is a different model ([the scope of the tests](#the-scope-of-the-tests)). From the wiki's first build until 2026-10-29 this page was an obituary ([history](#history)). Home section: [momentum clumping](/wiki/dark-matter/momentum-clumping); listed with the [conjectures](/wiki/status/conjectures).

## The conjecture

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

### Open again since v2.5

On 2026-10-29 Paul answered whether he concurred in recording the founding image dead. The root `CLAUDE.md` records the answer: "the founding image, matter clumping in momentum space (App. A item 3): not concurred. It is his open conjecture again, with the evidence of §9 stated in full" ('Since the handoff', "2026-10-29, Paul's answers to the concurrence questions"). His rule of the same day is that a claim is dead only when theory and data kill it and he explicitly concurs, and that "A failed model or version of an idea is not the death of the idea" ('Method').

#11 v2.5 retitles §9 "Momentum clumping: the founding image, tested" and closes its technical record:

> **Status (v2.5).** Matter clumping in momentum space is P.R.'s open conjecture [O] (App. A item 3): he does not concur in recording it dead (2026-10-29). Results (i)–(iii) stand as results. Scenario A, the committed-wave case of (ii), is under review, not dead, until P.R. reviews it.

Its plain-language passage: "These results stand. P.R. does not concur that they kill the founding image, which is his open conjecture (v2.5)." The audit of founding suppositions now reads, for item 3:

> Matter clumps in momentum space — **open**, P.R.'s conjecture [O] (v2.5): as collective dynamics it fails for particle dark matter by 10²⁸–10³¹ (theory) and, where mandatory for wave dark matter (Scenario A, under review), against the faintest dwarfs (data), and it is optional for a free-coupling wave; P.R. does not concur in its death (2026-10-29) (§9); **loophole**: topological p-localization of individual solitons untested; its candidate, p-localized conjugate monopoles, is P.R.'s open conjecture (§12; v2.4).

#11 §15's plain-language passage agrees: "The founding image failed the program's own calculations for particle dark matter and, where it would have been mandatory for wave dark matter, the test of the faintest dwarf galaxies; P.R. holds it open as his conjecture (v2.5)." The image is one of four founding ideas of his restored as open conjectures in v2.4 and v2.5, with [magnetic monopoles abundant in momentum space](/wiki/dark-matter/candidates/momentum-space-monopoles), [their explanation of the monopole null result](/wiki/electric-magnetic-duality/monopole-explanation) and [conjugate collapse powering our expansion](/wiki/cosmology/scale-factor-duality/collapse-powered-expansion) (#11 header, v2.4 and v2.5 change notes).

## How it was tested

The notebook left one step undone and said so: "The growth rate γ versus orbital phase-mixing remains to be computed; it is the theory's most important undone calculation on the astrophysics side. **[O]**" (§5.2). Its open-problem list carries it as item 3, the stream-instability growth rate, which "determines whether Prediction 3's granularity survives in Milky-Way-like halos" (§11).

That calculation became the clumping problem, one of the program's [three main problems](/wiki/history/main-problems), and three short calc notes carried it out ([the clumping calc notes](/wiki/history/documents/clumping-notes)):

1. `notes/stream-stability.md` built [the gated Vlasov model](/wiki/dark-matter/momentum-clumping/gated-vlasov-model), the notebook's mean-field picture made explicit with a Gaussian gate and a contact interaction, and computed its stability threshold with standard [Vlasov stability theory](/wiki/dark-matter/momentum-clumping/vlasov-stability). Result: "negative on the particle island, with a structural corollary."
2. `notes/wave-island.md` followed the corollary to very light, wave-like dark matter and computed the gated [condensation rate](/wiki/dark-matter/momentum-clumping/wave-island/condensation-rate) there. Result: "rate derived, environments evaluated, verdict reached."
3. `notes/ufd-endpoint.md` followed the one case in which clumping was mandatory, [Scenario A](/wiki/dark-matter/momentum-clumping/wave-island/scenario-a), to its endpoint in the faintest galaxies. Result: "Scenario A falsified; the clumping problem closed."

Each of the three notes now opens with the same status note:

> Status note, 2026-10-29: none of the deaths that calc notes #2–#4 record has Paul's concurrence, which his rule of that day requires. The founding image, matter clumping in momentum space, is his open conjecture again (#11 v2.5 §9). Old rows 3 and 4 and Scenario A are under his review, not dead, until he reviews them with Claude. The calculations stand as results (root `CLAUDE.md`, 'Since the handoff').

## The evidence

#11 v2.5 sums up the evidence in App. A item 3: as collective dynamics the image "fails for particle dark matter by 10²⁸–10³¹ (theory) and, where mandatory for wave dark matter (Scenario A, under review), against the faintest dwarfs (data), and it is optional for a free-coupling wave". The sections below give #11 §9's results (i)–(iii) in full; they stand.

### Particles: the attraction falls short by 28–31 orders of magnitude [D]

The threshold for streams is the [mean-field criterion](/wiki/dark-matter/momentum-clumping/instability-criterion): the attraction energy among co-moving particles must reach the kinetic energy of their random motion, g·n_gate ≥ m·min(σ, v\*)². At the [scattering benchmark](/wiki/dark-matter/conjugate-matter/benchmark), the coupling is already fixed by fitting dwarf-galaxy cores, and the criterion fails: the ratio is about 10⁻²⁸ in a dwarf core and 10⁻³¹ in the Milky Way's halo near the Sun (#2). Below threshold there is no growth: a ripple in the velocity distribution is Landau-damped, so the race against orbital mixing that the notebook planned never begins. Collisions do not help: "The H-theorem closes the collisional back door: gated collisions still maximize entropy; equilibrium is Maxwellian to one part in 10³⁰" (#2).

The checkpoint's summary: "Mean-field criterion g·n_gate ≥ m·min(σ,v\*)² fails by 10²⁸–10³¹ at the scattering benchmark; below threshold there is no growth; the H-theorem closes the collisional route" (#11 §9 (i)).

### The corollary: collective behaviour requires a wave [D]

Meeting the criterion at fixed cross-section per mass "forces m ≲ 0.1 meV, where N_occ ~ 10²⁰" (#11 §9 (i); on the regime in which calc note #2 evaluates that mass, see flag 19 in `review/wiki-build-flags.md`): at such masses about 10²⁰ quanta share each quantum state, and dark matter is a classical wave, not a gas of particles. This is [the classicality theorem](/wiki/dark-matter/momentum-clumping/classicality-theorem), in #11's words: "collective momentum-space behavior and classical particles are mutually exclusive". The notebook's χ was a classical particle, at a benchmark mass of about 70 MeV (`notes/broken-born-theory.md` §5.1); for classical particles the instability does not occur.

### Waves: drained dwarfs where mandatory, optional where free [D + T]

On the [wave island](/wiki/dark-matter/momentum-clumping/wave-island), the gated attraction can condense the wave field into narrow ranges of momentum, at a rate [Γ_self](/wiki/dark-matter/momentum-clumping/wave-island/condensation-rate). Whether that makes streams depends on what fixes the coupling (#3, 'What pins g? Two scenarios'):

- **Scenario A**, the gated channel also makes the dwarf cores. Then the coupling is fixed, and condensation outruns orbital stirring only in [ultra-faint dwarf galaxies](/wiki/dark-matter/halo-astrophysics/dwarf-galaxies), where it is mandatory. Because the attraction makes the condensate collapse above a [critical mass](/wiki/dark-matter/wave-dark-matter/attractive-condensates), the endpoint is a cycle of collapses that ejects dark matter from the galaxy. #11 §9 (ii): "If the gated channel also makes dwarf cores, condensation is mandatory only in ultra-faint dwarfs (Segue 1: rate ratio ~660; condensation ~10⁴ yr), whose attractive endpoint cycles above M_crit ≈ 2.9×10⁻³⁰(m/eV)^{−7/4} M_⊙ [14†] and drains the halo — **falsified** by observed UFD density and longevity; the light-mass escape is closed independently [15†, Lyman-α]", where UFD stands for ultra-faint dwarf. Segue 1, the test case, is dense and old. Scenario A is under review, not dead ([Under review: Scenario A and the ultra-faint-dwarf endpoint](/wiki/dark-matter/momentum-clumping/wave-island/scenario-a)).
- **Scenario B**, the cores come from elsewhere and the coupling is free. Then "streams are tunable across ~10 orders: optional, never required" (#11 §9 (ii); [Scenario B](/wiki/dark-matter/momentum-clumping/wave-island/scenario-b)).

### The net theorem

[The net theorem](/wiki/dark-matter/momentum-clumping/net-theorem): "velocity-space clumping is nowhere mandatory — forbidden (particles), fatal (committed wave), decorative (free wave)" (#11 §9 (iii)). The notebook's addendum v0.2 opens: "The clumping problem is settled, and the answer went against the theory." Calc note #4 withdrew the two predictions the image carried: "Rows 3 and 4 of the predictions table are permanently withdrawn, on both islands. The Fornax mechanism goes with them." (#4). #11 v2.5 §13 lists both rows as "Withdrawn and under P.R.'s review, not dead (v2.5)" ([Under review: velocity-space granularity in halos (old row 3)](/wiki/dark-matter/momentum-clumping/velocity-granularity); [Under review: Fornax friction suppression (old row 4)](/wiki/dark-matter/momentum-clumping/fornax-friction)).

### The scope of the tests

The tests used the program's own interaction, and that interaction acts on contact. Calc note #2 says "the x-range collapsed to contact (range 1/m_φ, microscopic)" and names "the force is contact-range" as one reason its verdict is robust (`notes/velocity-gated-gravity.md` §4). The results cover all three branches of that model: particle χ, wave χ whose coupling also makes the dwarf cores, and wave χ with a free coupling. On those branches, in turn, the net theorem finds clumping "forbidden (particles), fatal (committed wave), decorative (free wave)". For particle χ the record's "10²⁸–10³¹" quotes the exponents of the two shortfall ratios; the shortfall factors themselves are 2.6×10²⁷ and 3.5×10³⁰ (§4; flag 16, addendum). The results say that velocity clumping is required nowhere. They do not say that clumping cannot happen.

`notes/velocity-gated-gravity.md` (2026-10-28, not reviewed) took up the question of scope when it answered P.R.'s question of 2026-10-26 ([what the obituary covers](#what-the-obituary-covers)). Its status note of 2026-10-29 reads "the obituary" as #11 §9's record as it stood on 2026-10-28, and says: "The note's results stand as evidence about that record's scope; none of them is a death." The results:

- **Between ordinary bodies**, the [momentum graviton X](/wiki/gravity/momentum-graviton) adds a Yukawa term of range below 37.7 μm in the aligned vacuum (u = 1), unscreened. Its dependence on relative velocity is the O(v²/c²) spin-2 factor, 1 + 2.40×10⁻⁷ at 120 km/s, against 1 + 3.20×10⁻⁷ for ordinary gravity, not a gate [D][V] (§2). A relative-velocity gate acting between all bodies is bounded to |ε| < 8.7×10⁻⁹ for a Gaussian gate of width 0.3–3000 km/s in the e^{−v²/v_a²} convention, which is v\* = 0.2–2100 km/s in the record's [D; data S] (§3), where ε is the gated term's strength relative to gravity ([X between ordinary bodies](/wiki/gravity/momentum-graviton/ordinary-bodies)).
- **A long-range attraction among χ, gated in relative velocity,** is a different model. The record does not contain it, and the clumping problem never tested it. No field in the record could carry it (§5). At the record's gate width the Lyman-α forest allows ε < 0.057–0.106 in the record's reading, an estimate from compressed data, while velocity-selected clumping needs ε > 1 at every gate width (§§6–7). The force could not make dwarf cores, which would need G̃/G ≈ 3.6×10³¹, so any clumping it produced would be decorative (§7; [Conjecture: a long-range velocity-gated attraction among χ](/wiki/dark-matter/momentum-clumping/long-range-gated-attraction); [what could carry a relative-velocity gate](/wiki/dark-matter/conjugate-matter/gate-carriers)).
- **Narrow gates**, below about 30 km/s: N-body runs (one agent) found no velocity-selected structure up to ε = 10; one statistic shows a small offset the record does not adjudicate (§8). Corrected estimates, not likelihoods and rerun by one agent, exclude ε ≈ 2 from 10 km/s up, and ε ≈ 3 at 5–30 km/s in one of the two readings (§8).

Calc note #2's threshold for narrow gates is itself flagged: its form overstates the Milky Way shortfall about 3×, and the verdict is unchanged (flag 58 in `review/wiki-build-flags.md`; [the narrow-gate form, flagged](/wiki/dark-matter/momentum-clumping/instability-criterion#the-narrow-gate-form-flagged)). The gate-mechanism note of the same date, which finds that exchanging X cannot produce the program's gate (flag 55), leaves the tests' results unaffected. Of the obituary, as §9 then was, it says: "If anything it is strengthened: a completion whose only velocity dependence is a knee in σ_T(v) leaves the forward amplitude, which drives collective behaviour, ungated". The same bullet goes on: "Since 2026-10-29 that record has counted as evidence, not as a death: Paul did not concur, and the founding image is his open conjecture again (#11 v2.5 §9)" (`notes/gate-mechanism.md` §5; [the gate mechanism](/wiki/dark-matter/conjugate-matter/gate-mechanism#what-flag-55-proposes)).

## What the tests yielded

#11 §9's plain-language passage: "The tests yielded one new experimental question — the knee's sharpness distinguishes particle dark matter from wave dark matter — and one loophole for individual knots, whose candidate, conjugate monopoles localized in momentum, is P.R.'s open conjecture (§12)." Its technical record: "Salvage: the **island discriminant** (knee shape: sharp cutoff ⇒ particle χ; (v\*/σ)⁴ ⇒ wave χ) and free relic abundance via misalignment on the wave island".

- **[The island discriminant](/wiki/predictions/island-discriminant)**, now row 3 of [the predictions table](/wiki/predictions). The sharpness of the [knee](/wiki/dark-matter/conjugate-matter/scattering-law) in the self-interaction cross-section would tell particle dark matter from wave dark matter. #11 §13 lists it as "(not previously posed)".
- **[Relic abundance by misalignment](/wiki/dark-matter/momentum-clumping/wave-island/misalignment-relic)** on the wave island, which removes the notebook's relic-abundance problem there.
- **The loophole.** The clumping problem tested collective dynamics only. #11 App. A item 3 records: "**loophole**: topological p-localization of individual solitons untested; its candidate, p-localized conjugate monopoles, is P.R.'s open conjecture (§12; v2.4)". The loophole "remains untested; its candidate is P.R.'s conjecture of conjugate monopoles" (#11 §12; [the topological loophole](/wiki/dark-matter/momentum-clumping/topological-loophole); [Conjecture: magnetic monopoles abundant in momentum space](/wiki/dark-matter/candidates/momentum-space-monopoles)). #14's model of that candidate, superheavy solitons described with ordinary kinematics, failed, and its [obituary](/wiki/dark-matter/candidates/soliton-candidate/obituary) is in the candidates section; from v2.1 to v2.3 App. A item 3 read "its candidate is retired (§12)".

## What is open

- **The loophole.** Whether topology localizes a single object in momentum, the one form the tests did not cover, is untested. The root `CLAUDE.md` lists, among the items open and not queued, "for the restored candidate and the explanation: p-localization, and the kinematics of momentum-polarized matter, never modeled (#14 §1 assumed ordinary kinematics)" ('Since the handoff').
- **Scenario A's review.** [Scenario A](/wiki/dark-matter/momentum-clumping/wave-island/scenario-a), the committed-wave case, is one of the claims under review with Paul; "each stays not dead until he reviews it, and a death needs his explicit concurrence, in a change of its own" (root `CLAUDE.md`, 'Since the handoff'; [claims under review](/wiki/status/under-review)).
- **Long range and narrow gates.** For [a long-range attraction among χ gated in relative velocity](/wiki/dark-matter/momentum-clumping/long-range-gated-attraction), a model outside the record, the root `CLAUDE.md` lists as open and not queued "a full Lyman-α likelihood and a nonlinear simulation of narrow gates, if the long-range variant is pursued" and "whether the Hamiltonian reading is the right classical limit for a long-range gate" ('Since the handoff'). The note behind them leaves open "whether 'premature' rests on a particular observation" (`notes/velocity-gated-gravity.md` §10, citing §4).

## History

### An obituary, v2.0 to v2.4

- **The checkpoint.** From v2.0 to v2.4 #11 §9 was titled "Obituary: the death of momentum clumping", and App. A item 3 read "**dead as dynamics** (§9)". In v2.5 §9 became "Momentum clumping: the founding image, tested", with results (i)–(iii) unchanged, and item 3 "**open**, P.R.'s conjecture [O] (v2.5)" (#11 header, v2.5 change note).
- **The handoff.** On 2026-10-19 the handoff listed the image under "Dead (killed by own calculations — keep dead)": "DM clumping in momentum space as dynamics: impossible for particle DM (criterion fails by 10²⁸–10³¹ ✓), fatal where mandatory on the wave island (ultra-faint dwarfs would be drained; Segue 1 intact), tunable elsewhere" (`HANDOFF.md` §2), where DM is dark matter. The list now opens with a note: "Overtaken, 2026-10-29: none of the four below is dead now. Paul's rule of that day: a claim is dead only when theory and data kill it and he explicitly concurs. The first three are his open conjectures again (#11 v2.5 §9, §10, §11.1)".
- **The wiki.** From the wiki's first build (2026-10-20 to 2026-10-22) until 2026-10-29 this page was "Obituary: velocity clumping, the founding image", with status dead, and [the graveyard](/wiki/status/graveyard) listed it. On 2026-10-29, under Paul's rule on deaths, he was asked whether he concurred in the image's death, and he answered the same day that he did not (root `CLAUDE.md`, 'Since the handoff' and 'Method').
- **A precedent.** [The round-3 adjudication](/wiki/method/review/round-3/decisions) cited the clumping obituary as a precedent for retiring the soliton candidate, a decision Paul narrowed on 2026-10-29 to #14's model. Decision 2's note now ends: "The clumping obituary cited above as precedent is no longer a death: he did not concur, and the founding image is his open conjecture again (#11 v2.5 §9)" (`review/round3-adjudication.md`, 'Decisions').

### What the obituary covers

On 2026-10-26, while #11 §9 was still an obituary, P.R. asked whether the obituary is premature, and whether momentum gravity would look like a perturbation of gravity that depends on two bodies' relative velocity. The note that answered, `notes/velocity-gated-gravity.md` (2026-10-28, not reviewed), titles its §4 "What the obituary covers", the title this section keeps. Its answer is no to both: the obituary was "not premature" (root `CLAUDE.md`, 'Since the handoff', which adds "on 2026-10-29 Paul did not concur in the death: the founding image is his open conjecture, #11 v2.5 §9"), and momentum gravity is no such perturbation. The note opens with a status note:

> Status note, 2026-10-29: Paul did not concur in recording the founding image dead, and matter clumping in momentum space is his open conjecture again (#11 v2.5 §9). "The obituary" in this note is #11 §9's record as it stood on 2026-10-28. The note's results stand as evidence about that record's scope; none of them is a death.

Those results are given above, in [the scope of the tests](#the-scope-of-the-tests).

## Where the records differ

- **The handoff's check mark.** The handoff writes "impossible for particle DM (criterion fails by 10²⁸–10³¹ ✓)" (`HANDOFF.md` §2), where ✓ marks a machine-verified claim. When the wiki was built no `verify/` script covered any clumping number, and #11 §9 tags the result [D]. The checkpoint governs ([the mean-field criterion](/wiki/dark-matter/momentum-clumping/instability-criterion#verification-record)); the unbacked mark is flag 16 in `review/wiki-build-flags.md`. A recomputation made while building the wiki, `review/wiki-build-checks/stream_stability_check.py`, reproduces the shortfall from #2's inputs, printing `ratio = 3.9e-28` for the dwarf core and `ratio = 2.9e-31` for the Milky Way halo near the Sun (`review/wiki-build-checks/stream_stability_check.out`). It is evidence for a ruling, not part of [the project's gate](/wiki/method/verification/the-gate), `scripts/check.sh`; the flag noted that it "could be moved into `verify/`". Its addendum of 2026-10-28 records the move: `verify/velocity_gated_gravity.py` (section D) "now ports 3a's arithmetic into the gate and reproduces both ratios, with the linearized values beside them (flag 58). The ✓ is now backed by a script; #11 §9's tag [D] is unchanged until Paul rules. "10²⁸–10³¹" quotes the ratios' exponents; the shortfall factors are 2.6×10²⁷ and 3.5×10³⁰" ([the velocity-gated-gravity script](/wiki/method/verification/velocity-gated-gravity-script)).
- **The notebook's body.** The lab notebook's §5.2 and its prediction table were never edited and still read the instability and rows 3–4 as live; the addendum v0.2 strikes the rows ([the lab notebook](/wiki/history/documents/lab-notebook)). The tag "[D at mean-field level; O beyond]" on §5.2 asserted the instability; #2 found its threshold missed by 28–31 orders of magnitude.
- **The plain-language passages** of #9 §7 and #11 §9 describe the image as "dark matter flocking by velocity" and round the shortfall to "a factor of a million trillion trillion" (#9) and "thirty orders of magnitude" (#11). The popular article #10 presents the tests as a death, in 'The killing fields', rounding the shortfall to "a factor of ten to the thirtieth"; it is never a status source ([the popular articles](/wiki/history/documents/popular-articles)).
- **#11 §1, until 2026-10-30.** From v2.0 until a correction of 2026-10-30, #11 §1's plain abstract said that following the idea "killed its most cherished consequence — dark matter clumping in velocity instead of space — but forced the survivors into a tight structure". Version 2.5 at first kept the sentence beside §9's 'Status (v2.5)' and App. A item 3, which record the image as P.R.'s open conjecture. The correction, "Correction to v2.5 (2026-10-30)" in #11's header, says that §1 "now matches §9 and §15". §1's plain abstract now says that following the idea "put its most cherished consequence — dark matter clumping in velocity instead of space — to the program's own tests, which it failed for particle dark matter and, where it would be mandatory for wave dark matter, at the faintest dwarf galaxies; P.R. holds it open as his conjecture (§9)" ([inconsistencies inside #11](/wiki/history/documents/checkpoint#inconsistencies-inside-11)).

## Sources

- `papers/broken-born-checkpoint-v2.md` §9 — the tests, their tags and the salvage; 'Status (v2.5)' — P.R.'s open conjecture, results (i)–(iii) standing, Scenario A under review; the v2.5 plain-language passage; App. A item 3 — founding supposition 3, open since v2.5 ("dead as dynamics" from v2.0 to v2.4), the evidence in one line, and the loophole; header — the v2.4 and v2.5 change notes and the correction to v2.5 (2026-10-30); §15 — the v2.5 plain-language passage; §12 — the loophole's current wording; §1 — "most cherished consequence", and the plain abstract before and after the correction; §8 — the gate in plain language; §13 — the island discriminant as row 3, and the withdrawn rows under review
- `CLAUDE.md` 'Since the handoff' (2026-10-29, Paul's answers to the concurrence questions) — the founding image: he did not concur in its death, and it is his open conjecture again; the items open and not queued; the 2026-10-28 entry, "not premature", with his non-concurrence in the death, 2026-10-29; 'Method' — the rule on deaths
- `review/round3-adjudication.md` 'Decisions' — the clumping obituary as precedent; Paul's narrowing of Decision 2 to #14's model, and the note's last sentence: the precedent no longer a death
- `notes/stream-stability.md` 'Numbers at the scattering benchmark', 'Corollary (the classicality theorem)' — the particle-island test
- `notes/wave-island.md` 'What pins g? Two scenarios' — the wave-island scenarios
- `notes/ufd-endpoint.md` 'Verdict and closure of the clumping problem' — the note's verdicts on Scenario A, "falsified", and on rows 3–4, "permanently withdrawn"
- `notes/stream-stability.md`, `notes/wave-island.md`, `notes/ufd-endpoint.md` 'Status note, 2026-10-29' — none of the deaths the three notes record has Paul's concurrence; the calculations stand as results
- `notes/broken-born-theory.md` §5.2 — the original claim; §5.1 — the benchmark mass; §9 — rows 3–4 and the flagship discriminants; §10 — the parameter count; §11 item 3 — the open problem; 'Addendum (v0.2)' — the notebook's record of the result
- `notes/broken-born-program-v1.md` §7 — the first consolidation's record
- `HANDOFF.md` §2 — "keep dead", the unbacked ✓, and the note "Overtaken, 2026-10-29" over the dead list
- `popsci/angle-of-the-mirror.md` 'The wager', 'The killing fields' — the popular image and retelling (not a status source)
- `review/wiki-build-flags.md` items 16, 19, 58 — the ✓ without a script, and its addendum of 2026-10-28; the regime of the classicality corollary; calc note #2's narrow-gate criterion; all awaiting a ruling
- `notes/velocity-gated-gravity.md` (2026-10-28, not reviewed) 'Status note, 2026-10-29' — "the obituary" as #11 §9 stood on 2026-10-28, and the results as evidence about its scope; §4 — what the obituary covers; §§2–3 — X between ordinary bodies and the universal gate; §§5–8 — the long-range variant and the narrow-gate corner; §1 and §10 — the question and what is open
- `verify/velocity_gated_gravity.py` section D — calc note #2's shortfall ratios in the gate
- `notes/gate-mechanism.md` §5 — the tests' results unaffected by flag 55, and the record as evidence, not a death, since 2026-10-29
- `review/wiki-build-checks/stream_stability_check.py` and `review/wiki-build-checks/stream_stability_check.out` — the wiki build's recomputation of the shortfall (outside `verify/`)
