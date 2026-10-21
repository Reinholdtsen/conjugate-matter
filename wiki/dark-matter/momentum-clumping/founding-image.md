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
  - "notes/broken-born-theory.md §5.2"
  - "notes/broken-born-theory.md 'Addendum (v0.2)'"
  - "notes/debt3a-stream-stability.md 'Numbers at the scattering benchmark'"
  - "notes/debt3b-wave-island.md 'What pins g? Two scenarios'"
  - "notes/debt3c-ufd-endpoint.md 'Verdict and closure'"
  - "HANDOFF.md §2"
  - "popsci/angle-of-the-mirror.md 'The killing fields'"
---

*Velocity clumping was the program's founding picture of dark matter: a smooth dark-matter halo would break up into a few streams, each made of particles moving with nearly the same velocity, so that dark matter clumps in velocity rather than in position. The lab notebook described it as the Jeans problem, the gravitational instability that makes lumps in space, with the roles of position and velocity exchanged. The program's own Debt-3 calculation then tested it and found it impossible for particle dark matter, fatal where it would be mandatory for wave dark matter, and merely optional elsewhere. The claim is dead as dynamics and stays dead.*

**Status:** Dead — killed by Debt 3: [D] on the particle island and [D + T] on the wave island (#11 §9). Founding supposition 3, "Matter clumps in momentum space", is "dead as dynamics" (#11 App. A item 3; [founding suppositions](/wiki/program/founding-suppositions)), and the handoff's instruction is "keep dead". No `verify/` script checks any Debt-3 number. Home section: [momentum clumping](/wiki/dark-matter/momentum-clumping); listed in [the graveyard](/wiki/status/graveyard).

## Key facts

- **What was claimed** (`notes/broken-born-theory.md` §5.2, tagged "[D at mean-field level; O beyond]"). "The genuinely p-local part of the interaction shifts a particle's energy by the phase-space density of co-moving neighbors", giving "an anomalous velocity, the same structure as Berry-curvature transport in solids". With an attractive [gate](/wiki/dark-matter/conjugate-matter/velocity-gate), "the collisionless Boltzmann equation with this mean field is the Jeans problem with the roles of x and v exchanged: a smooth Maxwellian f(v) is unstable to fragmentation into discrete velocity streams of width Δv ~ v\*, each spatially delocalized and internally coherent across kiloparsecs."
- **What it was meant to explain.** The notebook called the analogy with Bardeen–Cooper–Schrieffer pairing in superconductors "exact in structure" and drew two consequences: "superfluid-like cores in dwarfs and suppressed dynamical friction inside them". In its prediction table the stream fragmentation became [old row 3](/wiki/dark-matter/momentum-clumping/velocity-granularity), and the condensed cores with suppressed friction became [old row 4](/wiki/dark-matter/momentum-clumping/fornax-friction).
- **How it was tested.** The notebook called the growth rate "the theory's most important undone calculation on the astrophysics side" [O]. Debt 3 carried out the test with a [gated Vlasov model](/wiki/dark-matter/momentum-clumping/gated-vlasov-model), built on standard [Vlasov stability theory](/wiki/dark-matter/momentum-clumping/vlasov-stability).
- **Why it failed: particles** [D]. "Mean-field criterion g·n_gate ≥ m·min(σ,v\*)² fails by 10²⁸–10³¹ at the scattering benchmark; below threshold there is no growth; the H-theorem closes the collisional route" (#11 §9 (i); [the mean-field criterion](/wiki/dark-matter/momentum-clumping/instability-criterion)). Meeting the criterion "forces m ≲ 0.1 meV, where N_occ ~ 10²⁰" ([the classicality theorem](/wiki/dark-matter/momentum-clumping/classicality-theorem)).
- **Why it failed: waves** [D + T]. If the gated channel also makes dwarf cores, condensation is mandatory only in ultra-faint dwarf galaxies, and its endpoint "drains the halo — falsified by observed UFD density and longevity" (#11 §9 (ii); [Scenario A](/wiki/dark-matter/momentum-clumping/wave-island/scenario-a)). With the coupling free, "streams are tunable across ~10 orders: optional, never required" ([Scenario B](/wiki/dark-matter/momentum-clumping/wave-island/scenario-b)).
- **The verdict.** [The net theorem](/wiki/dark-matter/momentum-clumping/net-theorem): "velocity-space clumping is nowhere mandatory — forbidden (particles), fatal (committed wave), decorative (free wave)" (#11 §9 (iii)). The notebook's addendum v0.2 opens: "Debt 3 is paid, and the answer went against the theory."
- **What survives.** "Salvage: the island discriminant (knee shape: sharp cutoff ⇒ particle χ; (v\*/σ)⁴ ⇒ wave χ) and free relic abundance via misalignment on the wave island" (#11 §9; [row 3](/wiki/predictions/island-discriminant), [misalignment](/wiki/dark-matter/momentum-clumping/wave-island/misalignment-relic)). Momentum localization of single topological objects "remains untested, but has no candidate" (#11 §12; [the topological loophole](/wiki/dark-matter/momentum-clumping/topological-loophole)).
- **Where the records differ.** The handoff marks the 10²⁸–10³¹ failure ✓ (machine-verified), but no script exists for it; #11 §9's [D] governs. The notebook's body was never edited and still reads the clumping as live ([the lab notebook](/wiki/history/documents/lab-notebook)). The popular article #10 retells the death in "The killing fields" and is never a status source ([the popular articles](/wiki/history/documents/popular-articles)).

## Sources

- `papers/broken-born-checkpoint-v2.md` §9 — the obituary and its tags; §12 — the loophole's current wording; App. A item 3 — founding supposition 3, "dead as dynamics"
- `notes/debt3a-stream-stability.md`, `notes/debt3b-wave-island.md`, `notes/debt3c-ufd-endpoint.md` — the calculation (Debt 3)
- `notes/broken-born-theory.md` §5.2 — the original claim; 'Addendum (v0.2)' — the notebook's record of its death
- `HANDOFF.md` §2 — "keep dead", and the unbacked ✓
- `popsci/angle-of-the-mirror.md` 'The killing fields' — the popular retelling (not a status source)
