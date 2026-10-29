---
title: "Obituary: Fornax friction suppression (old row 4)"
weight: 90
status: dead
description: "Suppressed dynamical friction in condensed cores, which would have let Fornax's globular clusters stay put; withdrawn with the condensed cores that carried it."
sources:
  - "notes/ufd-endpoint.md 'Verdict and closure'"
  - "papers/broken-born-checkpoint-v2.md §13"
  - "notes/stream-stability.md 'Consequences for the predictions table'"
  - "notes/wave-island.md 'What pins g? Two scenarios'"
  - "notes/broken-born-theory.md §9"
  - "notes/broken-born-theory.md §5.2"
  - "notes/broken-born-theory.md §10"
  - "notes/broken-born-theory.md 'Addendum (v0.2)'"
  - "notes/broken-born-program-v1.md §9"
---

*Fornax friction suppression was the [lab notebook](/wiki/history/documents/lab-notebook)'s prediction that dark matter in the cores of dwarf galaxies condenses into a superfluid-like state in which dynamical friction, the drag that makes a massive body sink toward the centre of a galaxy, is suppressed. It would have explained why the globular star clusters of the Fornax dwarf galaxy have not sunk to its centre, the Fornax timing problem, and it was row 4 of the notebook's [prediction table](/wiki/predictions/table-history). The condensed cores came from the same velocity-space condensation as the [founding image](/wiki/dark-matter/momentum-clumping/founding-image) of velocity clumping, so when [the clumping problem](/wiki/history/main-problems) killed that picture the row was withdrawn with it, permanently.*

**Status:** Dead — withdrawn on the particle island in `notes/stream-stability.md` and on both islands in `notes/ufd-endpoint.md` ("The Fornax mechanism goes with them"); [#11](/wiki/history/documents/checkpoint) §13 lists "Fornax friction suppression (obituary §9)" under "Withdrawn with cause". Untagged in the sources. Killed with the founding image by the clumping problem, whose summary is [the net theorem](/wiki/dark-matter/momentum-clumping/net-theorem). Home section: [momentum clumping](/wiki/dark-matter/momentum-clumping); listed in [the graveyard](/wiki/status/graveyard).

## What was claimed

### The row as written

Row 4 of the lab notebook's prediction table (`notes/broken-born-theory.md` §9):

| Column | Row 4 |
|---|---|
| Observable | "Dynamical friction in dwarf cores" |
| Standard expectation | "GCs sink (cuspy CDM)" |
| Requirement of the framework | "Suppressed in condensed cores; Fornax GCs stay put" |
| Kill condition | "Demonstrated normal friction in cored dwarfs" |

GCs are globular clusters, and CDM is cold dark matter, whose halos have density cusps at their centres in simulations without self-interaction [T] ([dwarf galaxies](/wiki/dark-matter/halo-astrophysics/dwarf-galaxies)).

### The physics behind the row

**Dynamical friction** [T]. A massive body moving through a sea of lighter particles pulls them toward its path by gravity, and the overdense wake that forms behind it pulls the body back. The body loses orbital energy and spirals inward. The standard formula is Chandrasekhar's (1943)†. In a dwarf galaxy, a globular cluster orbiting inside the dark-matter halo should sink toward the centre by this drag ([halo-substructure probes](/wiki/dark-matter/halo-astrophysics/halo-substructure)).

**The Fornax timing problem** [T]. The Fornax dwarf spheroidal galaxy, a satellite of the Milky Way, has several globular clusters at large distances from its centre. Estimates of dynamical friction in a cuspy cold-dark-matter halo give sinking times shorter than the clusters' ages, so their present positions need an explanation. A cored halo, with a flat central density, slows the sinking, which is one of the standard responses [T].

**The notebook's mechanism.** §5.2, tagged "[D at mean-field level; O beyond]", read the gated attraction as a pairing interaction: "The BCS analogy is exact in structure: a momentum-gated attraction is precisely the pairing interaction, and below a critical velocity dispersion the core of a halo condenses — momentum-space clumping, realized. Consequences: superfluid-like cores in dwarfs and **suppressed dynamical friction** inside them (the Fornax globular-cluster timing problem is a feature, not a bug)." BCS is the Bardeen–Cooper–Schrieffer theory of superconductivity [T]. The analogy is with superfluids, in which a body moving slower than a critical speed experiences no drag [T]. The notebook did not derive the suppression; it listed it as a consequence of the condensed core.

### Its standing

The notebook's parameter count credits the two conjugate-matter parameters σ₀/m and v\* with "friction suppression" among the phenomena they cover (§10). Row 4 rested on the same condensation as [old row 3](/wiki/dark-matter/momentum-clumping/velocity-granularity), velocity-space granularity: §5.2 derives both from the instability of a smooth velocity distribution under the gated attraction.

## How it was tested

The clumping problem tested the condensation itself, not the friction. Without a condensed core there is no superfluid-like medium and no suppression to compute. The test began with the notebook's open problem 3, the stream-instability growth rate against orbital phase mixing, and ran through three calc notes ([the founding image](/wiki/dark-matter/momentum-clumping/founding-image#how-it-was-tested)).

## Why it failed

### Particle island: no condensation

For dark-matter particles of MeV to GeV mass, [the mean-field criterion](/wiki/dark-matter/momentum-clumping/instability-criterion) fails in a dwarf core by a ratio of about 10⁻²⁸ at the [scattering benchmark](/wiki/dark-matter/conjugate-matter/benchmark) ([#2](/wiki/history/documents/clumping-notes)). Below threshold the velocity distribution is stable, so a halo core does not condense. #2 withdrew the row on this island, together with the link to row 3: "Rows 3 (velocity granularity) and 4 (condensed cores / Fornax friction suppression) are **withdrawn**, and with them the mechanism-level linkage claimed between them." (#2, 'Consequences for the predictions table').

### Wave island: no placid condensate

Collective behaviour survives only for wave-like dark matter, on the [wave island](/wiki/dark-matter/momentum-clumping/wave-island) ([the classicality theorem](/wiki/dark-matter/momentum-clumping/classicality-theorem)). There, under [Scenario A](/wiki/dark-matter/momentum-clumping/wave-island/scenario-a), condensation is mandatory only in ultra-faint dwarfs; for a "Classical dwarf core" #3's table gives a ratio of [condensation rate](/wiki/dark-matter/momentum-clumping/wave-island/condensation-rate) to orbital stirring of "~10⁻²", so condensation loses to stirring there. The notes do not apply this row to Fornax by name. Where condensation is mandatory, the endpoint is not a stable superfluid core: "Because the interaction is **attractive**, the endpoint is not a placid stream: a growing condensate with attractive self-interaction has a critical mass … above which it collapses (bosenova)" (#3; [attractive condensates](/wiki/dark-matter/wave-dark-matter/attractive-condensates)). #4 follows the collapses to a drain of the galaxy's dark matter, which observation excludes. Under [Scenario B](/wiki/dark-matter/momentum-clumping/wave-island/scenario-b) the coupling is free and condensation is optional, so it can carry no prediction.

### The permanent withdrawal

#4, closing the clumping problem: "Rows 3 and 4 of the predictions table are permanently withdrawn, on both islands. The Fornax mechanism goes with them." The notebook's addendum: "Rows 3–4 are struck from §9 permanently" (`notes/broken-born-theory.md`, 'Addendum (v0.2)').

## What survives

Nothing of the row. The Fornax timing problem stays an astrophysical question to which the program no longer offers an answer. On the particle island, the program's dwarf-galaxy cores come from gated scattering, as in [self-interacting dark matter](/wiki/dark-matter/halo-astrophysics/self-interacting-dark-matter): the scattering benchmark is a fit of the cross-section to dwarf cores, and the [knee](/wiki/dark-matter/conjugate-matter/scattering-law) of that cross-section is [row 1](/wiki/predictions/self-interaction-knee) of the current table. Whether a cored halo produced that way changes dynamical friction is not addressed in the sources.

## In the later tables

- #9 §9: "Withdrawn with cause, permanently: velocity-space granularity in halos; Fornax friction suppression (rows 3–4 of earlier versions; obituary in §7)."
- #11 §13: "Withdrawn with cause: velocity-space granularity in halos; Fornax friction suppression (obituary §9); superheavy-soliton dark matter (obituary §12)." The last item is [the soliton candidate](/wiki/dark-matter/candidates/soliton-candidate/obituary).

In #9 and #11, row 4 is [thawing dark energy](/wiki/predictions/dark-energy-drift), so this wiki calls the notebook's row "old row 4" ([history of the predictions table](/wiki/predictions/table-history)). Its companion is [old row 3](/wiki/dark-matter/momentum-clumping/velocity-granularity).

## References

Added by the wiki from model memory (†):

- S. Chandrasekhar (1943)†: the dynamical-friction formula.

## Sources

- `notes/ufd-endpoint.md` 'Verdict and closure of the clumping problem' — the permanent withdrawal: "The Fornax mechanism goes with them"
- `papers/broken-born-checkpoint-v2.md` §13 — "Withdrawn with cause"
- `notes/stream-stability.md` 'Consequences for the predictions table' — withdrawal on the particle island
- `notes/wave-island.md` 'What pins g? Two scenarios' — the classical-dwarf ratio and the attractive endpoint
- `notes/broken-born-theory.md` §9 — the row as written; §5.2 — the condensed-core mechanism; §10 — the parameter count; 'Addendum (v0.2)' — the strike
- `notes/broken-born-program-v1.md` §9 — the withdrawal in v1's renumbered table
