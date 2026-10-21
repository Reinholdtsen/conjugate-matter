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
  - "papers/broken-born-checkpoint-v2.md §2"
  - "review/round3-adjudication.md 'Decisions'"
  - "notes/broken-born-theory.md §5.2"
  - "notes/broken-born-theory.md §5.1"
  - "notes/broken-born-theory.md §9"
  - "notes/broken-born-theory.md §10"
  - "notes/broken-born-theory.md §11 item 3"
  - "notes/broken-born-theory.md 'Addendum (v0.2)'"
  - "notes/debt3a-stream-stability.md 'Numbers at the scattering benchmark'"
  - "notes/debt3a-stream-stability.md 'Corollary'"
  - "notes/debt3b-wave-island.md 'What pins g? Two scenarios'"
  - "notes/debt3c-ufd-endpoint.md 'Verdict and closure'"
  - "notes/broken-born-program-v1.md §7"
  - "HANDOFF.md §2"
  - "popsci/angle-of-the-mirror.md 'The wager'"
  - "popsci/angle-of-the-mirror.md 'The killing fields'"
---

*Velocity clumping was the program's founding picture of dark matter: a smooth dark-matter halo would break up into a few streams, each made of particles moving with nearly the same velocity, so that dark matter clumps in velocity instead of in position. The [lab notebook](/wiki/history/documents/lab-notebook) described it as the [Jeans problem](/wiki/dark-matter/momentum-clumping/vlasov-stability), the gravitational instability that makes lumps in space, with the roles of position and velocity exchanged. The program's own Debt-3 calculation tested it and found it impossible for particle dark matter, fatal where it would be mandatory for wave dark matter, and merely optional elsewhere. The claim is dead as dynamics and stays dead.*

**Status:** Dead — killed by [Debt 3](/wiki/history/debts): [D] on the particle island and [D + T] on the [wave island](/wiki/dark-matter/momentum-clumping/wave-island) (#11 §9). Founding supposition 3, "Matter clumps in momentum space", is "dead as dynamics" (#11 App. A item 3; [founding suppositions](/wiki/program/founding-suppositions)), and the handoff lists it under "Dead (killed by own calculations — keep dead)". No `verify/` script checks any Debt-3 number. Home section: [momentum clumping](/wiki/dark-matter/momentum-clumping); listed in [the graveyard](/wiki/status/graveyard).

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

The notebook continued: "The BCS analogy is exact in structure: a momentum-gated attraction is precisely the pairing interaction, and below a critical velocity dispersion the core of a halo condenses — momentum-space clumping, realized." BCS is the Bardeen–Cooper–Schrieffer theory of superconductivity, in which an attraction acting only between electrons within a thin shell of momentum near the Fermi surface makes the electron gas unstable to pairing below a critical temperature [T]. In the notebook's analogy, the halo's velocity dispersion plays the role of the temperature.

### What it was meant to explain

The notebook drew two consequences: "superfluid-like cores in dwarfs and **suppressed dynamical friction** inside them (the Fornax globular-cluster timing problem is a feature, not a bug)". In its [prediction table](/wiki/predictions/table-history) (`notes/broken-born-theory.md` §9) these became two rows:

- **Row 3**, velocity-space granularity: "Fragmentation into O(10) macro-streams of width ~v\*, coherent over kpc", visible in the perturbations of cold [stellar streams](/wiki/dark-matter/halo-astrophysics/halo-substructure) ([old row 3](/wiki/dark-matter/momentum-clumping/velocity-granularity));
- **Row 4**, friction in dwarf cores: "Suppressed in condensed cores; Fornax GCs stay put", with GCs the globular clusters ([old row 4](/wiki/dark-matter/momentum-clumping/fornax-friction)).

Row 3 was one of the notebook's three "flagship discriminants". Its parameter count credited the two conjugate-matter parameters with "stream granularity scale, friction suppression" among the phenomena covered (§10). The checkpoint's abstract calls velocity clumping the program's "most cherished consequence" (#11 §1).

## How it was tested

The notebook left one step undone and said so: "The growth rate γ versus orbital phase-mixing remains to be computed; it is the theory's most important undone calculation on the astrophysics side. **[O]**" (§5.2). Its open-problem list carries it as item 3, the stream-instability growth rate, which "determines whether Prediction 3's granularity survives in Milky-Way-like halos" (§11).

That calculation became Debt 3, one of the [three debts](/wiki/history/debts) the program owed, and three short calc notes paid it ([the Debt-3 calc notes](/wiki/history/documents/debt-3-notes)):

1. `notes/debt3a-stream-stability.md` built [the gated Vlasov model](/wiki/dark-matter/momentum-clumping/gated-vlasov-model), the notebook's mean-field picture made explicit with a Gaussian gate and a contact interaction, and computed its stability threshold with standard [Vlasov stability theory](/wiki/dark-matter/momentum-clumping/vlasov-stability). Result: "negative on the particle island, with a structural corollary."
2. `notes/debt3b-wave-island.md` followed the corollary to very light, wave-like dark matter and computed the gated [condensation rate](/wiki/dark-matter/momentum-clumping/wave-island/condensation-rate) there. Result: "rate derived, environments evaluated, verdict reached."
3. `notes/debt3c-ufd-endpoint.md` followed the one case in which clumping was mandatory, [Scenario A](/wiki/dark-matter/momentum-clumping/wave-island/scenario-a), to its endpoint in the faintest galaxies. Result: "Scenario A falsified; Debt 3 closed."

## Why it failed

### Particles: the attraction falls short by 28–31 orders of magnitude [D]

The threshold for streams is the [mean-field criterion](/wiki/dark-matter/momentum-clumping/instability-criterion): the attraction energy among co-moving particles must reach the kinetic energy of their random motion, g·n_gate ≥ m·min(σ, v\*)². At the [scattering benchmark](/wiki/dark-matter/conjugate-matter/benchmark), the coupling is already fixed by fitting dwarf-galaxy cores, and the criterion fails: the ratio is about 10⁻²⁸ in a dwarf core and 10⁻³¹ in the Milky Way's halo near the Sun (3a). Below threshold there is no growth: a ripple in the velocity distribution is Landau-damped, so the race against orbital mixing that the notebook planned never begins. Collisions do not help: "The H-theorem closes the collisional back door: gated collisions still maximize entropy; equilibrium is Maxwellian to one part in 10³⁰" (3a).

The checkpoint's summary: "Mean-field criterion g·n_gate ≥ m·min(σ,v\*)² fails by 10²⁸–10³¹ at the scattering benchmark; below threshold there is no growth; the H-theorem closes the collisional route" (#11 §9 (i)).

### The corollary: collective behaviour requires a wave [D]

Meeting the criterion at fixed cross-section per mass "forces m ≲ 0.1 meV, where N_occ ~ 10²⁰" (#11 §9 (i)): at such masses about 10²⁰ quanta share each quantum state, and dark matter is a classical wave, not a gas of particles. This is [the classicality theorem](/wiki/dark-matter/momentum-clumping/classicality-theorem). The notebook's χ was a classical particle, at a benchmark mass of about 70 MeV (`notes/broken-born-theory.md` §5.1); for classical particles the instability does not occur.

### Waves: fatal where mandatory [D + T]

On the [wave island](/wiki/dark-matter/momentum-clumping/wave-island), the gated attraction can condense the wave field into narrow ranges of momentum, at a rate [Γ_self](/wiki/dark-matter/momentum-clumping/wave-island/condensation-rate). Whether that makes streams depends on what fixes the coupling (3b, 'What pins g? Two scenarios'):

- **Scenario A**, the gated channel also makes the dwarf cores. Then the coupling is fixed, and condensation outruns orbital stirring only in [ultra-faint dwarf galaxies](/wiki/dark-matter/halo-astrophysics/dwarf-galaxies), where it is mandatory. Because the attraction makes the condensate collapse above a [critical mass](/wiki/dark-matter/wave-dark-matter/attractive-condensates), the endpoint is a cycle of collapses that ejects dark matter from the galaxy. #11 §9 (ii): the endpoint "drains the halo — **falsified** by observed UFD density and longevity", where UFD stands for ultra-faint dwarf. Segue 1, the test case, is dense and old ([Scenario A](/wiki/dark-matter/momentum-clumping/wave-island/scenario-a)).
- **Scenario B**, the cores come from elsewhere and the coupling is free. Then "streams are tunable across ~10 orders: optional, never required" (#11 §9 (ii); [Scenario B](/wiki/dark-matter/momentum-clumping/wave-island/scenario-b)).

### The verdict

[The net theorem](/wiki/dark-matter/momentum-clumping/net-theorem): "velocity-space clumping is nowhere mandatory — forbidden (particles), fatal (committed wave), decorative (free wave)" (#11 §9 (iii)). The notebook's addendum v0.2 opens: "Debt 3 is paid, and the answer went against the theory." Rows 3 and 4 were withdrawn permanently on both islands: "Rows 3 and 4 of the predictions table are permanently withdrawn, on both islands. The Fornax mechanism goes with them." (3c).

## What survives

#11 §9: "Salvage: the **island discriminant** (knee shape: sharp cutoff ⇒ particle χ; (v\*/σ)⁴ ⇒ wave χ) and free relic abundance via misalignment on the wave island".

- **[The island discriminant](/wiki/predictions/island-discriminant)**, now row 3 of the predictions table. The sharpness of the [knee](/wiki/dark-matter/conjugate-matter/scattering-law) in the self-interaction cross-section would tell particle dark matter from wave dark matter. #11 §13 lists it as "(not previously posed)".
- **[Relic abundance by misalignment](/wiki/dark-matter/momentum-clumping/wave-island/misalignment-relic)** on the wave island, which removes the notebook's relic-abundance problem there.
- **The loophole.** Debt 3 tested collective dynamics only. #11 App. A item 3 records: "**loophole**: topological p-localization of individual solitons untested, and its candidate is retired (§12)". The candidate was the superheavy soliton, whose [obituary](/wiki/dark-matter/candidates/soliton-candidate/obituary) is in the candidates section; the loophole now "remains untested, but has no candidate" (#11 §12; [the topological loophole](/wiki/dark-matter/momentum-clumping/topological-loophole)).

The program kept the result prominent. The round-3 adjudication cites it as the precedent for retiring the soliton candidate: "The program's precedent is the Debt 3 obituary: a dead claim is reported prominently and stays dead." (`review/round3-adjudication.md`, 'Decisions'). The checkpoint counts such results as the most reliable of its novel, Tier-3 claims: "Negative results (§9, §7.1, and the §12 obituary) are the most reliable Tier-3 items, since the program's incentive gradient ran against them" (#11 §2; [negative results](/wiki/method/negative-results)).

## Where the records differ

- **The handoff's check mark.** The handoff writes "impossible for particle DM (criterion fails by 10²⁸–10³¹ ✓)" (`HANDOFF.md` §2), where ✓ marks a machine-verified claim and DM is dark matter. No `verify/` script covers any Debt-3 number, and #11 §9 tags the result [D]. The checkpoint governs ([the mean-field criterion](/wiki/dark-matter/momentum-clumping/instability-criterion#verification-record)).
- **The notebook's body.** The lab notebook's §5.2 and its prediction table were never edited and still read the instability and rows 3–4 as live; the addendum v0.2 records their death ([the lab notebook](/wiki/history/documents/lab-notebook)). The tag "[D at mean-field level; O beyond]" on §5.2 asserted the instability; 3a found its threshold missed by 28–31 orders of magnitude.
- **The plain-language passages** of #9 §7 and #11 §9 describe the image as "dark matter flocking by velocity" and round the shortfall to "a factor of a million trillion trillion" (#9) and "thirty orders of magnitude" (#11). The popular article #10 retells the death in 'The killing fields', rounding the shortfall to "a factor of ten to the thirtieth"; it is never a status source ([the popular articles](/wiki/history/documents/popular-articles)).

## Sources

- `papers/broken-born-checkpoint-v2.md` §9 — the obituary, its tags and the salvage; App. A item 3 — founding supposition 3, "dead as dynamics", and the loophole; §12 — the loophole's current wording; §1 — "most cherished consequence"; §2 — negative results as the most reliable Tier-3 items; §8 — the gate in plain language; §13 — the island discriminant as row 3
- `review/round3-adjudication.md` 'Decisions' — the Debt-3 obituary as precedent
- `notes/debt3a-stream-stability.md` 'Numbers at the scattering benchmark', 'Corollary (the classicality theorem)' — the particle-island test
- `notes/debt3b-wave-island.md` 'What pins g? Two scenarios' — the wave-island scenarios
- `notes/debt3c-ufd-endpoint.md` 'Verdict and closure of Debt 3' — the falsification and the permanent withdrawal of rows 3–4
- `notes/broken-born-theory.md` §5.2 — the original claim; §5.1 — the benchmark mass; §9 — rows 3–4 and the flagship discriminants; §10 — the parameter count; §11 item 3 — the open problem; 'Addendum (v0.2)' — the notebook's record of the death
- `notes/broken-born-program-v1.md` §7 — the first consolidation's obituary
- `HANDOFF.md` §2 — "keep dead", and the unbacked ✓
- `popsci/angle-of-the-mirror.md` 'The wager', 'The killing fields' — the popular image and retelling (not a status source)
