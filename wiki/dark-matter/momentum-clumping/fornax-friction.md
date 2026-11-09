---
title: "Under review: Fornax friction suppression (old row 4)"
weight: 90
status: under-review
description: "Suppressed dynamical friction in condensed cores, which would have let Fornax's globular clusters stay put; withdrawn with the condensed cores that carried it, and under review."
sources:
  - "CLAUDE.md 'Since the handoff'"
  - "notes/ufd-endpoint.md 'Verdict and closure'"
  - "wiki/papers/broken-born-checkpoint-v2.md §13"
  - "wiki/papers/broken-born-checkpoint-v2.md §9"
  - "notes/stream-stability.md 'Consequences for the predictions table'"
  - "notes/wave-island.md 'What pins g? Two scenarios'"
  - "notes/broken-born-theory.md §9"
  - "notes/broken-born-theory.md §5.2"
  - "notes/broken-born-theory.md §10"
  - "notes/broken-born-theory.md 'Addendum (v0.2)'"
  - "notes/broken-born-program-v1.md §9"
---

*Fornax friction suppression was the [lab notebook](../../history/documents/lab-notebook.md)'s prediction that dark matter in the cores of dwarf galaxies condenses into a superfluid-like state in which dynamical friction, the drag that makes a massive body sink toward the centre of a galaxy, is suppressed. It would have explained why the globular star clusters of the Fornax dwarf galaxy have not sunk to its centre, the Fornax timing problem, and it was row 4 of the notebook's [prediction table](../../predictions/table-history.md). The condensed cores came from the same velocity-space condensation as the [founding image](founding-image.md) of velocity clumping, so when the tests of [the clumping problem](../../history/main-problems.md) went against that picture, the row was withdrawn, "permanently" in calc note [#4](../../../notes/ufd-endpoint.md)'s words. The founding image itself is P.R.'s open conjecture.*

**Status:** Under review — the evidence below weighs against it, and its final status awaits review. Withdrawn on the particle island in [`notes/stream-stability.md`](../../../notes/stream-stability.md) and on both islands in [`notes/ufd-endpoint.md`](../../../notes/ufd-endpoint.md) ("The Fornax mechanism goes with them"); [#11](../../history/documents/checkpoint.md) [§13](../../papers/broken-born-checkpoint-v2.md#13-predictions-and-kill-conditions) lists "Fornax friction suppression (§9)" among the rows withdrawn and under review. Untagged in the sources. It was withdrawn on the results of the clumping problem, which tested the founding image, P.R.'s open conjecture ([#11 §9](../../papers/broken-born-checkpoint-v2.md#9-momentum-clumping-the-founding-image-tested)); [the net theorem](net-theorem.md) summarizes those results. Home section: [momentum clumping](_index.md); listed in [claims under review](../../status/under-review.md).

## What was claimed

### The row as written

Row 4 of the lab notebook's prediction table ([`notes/broken-born-theory.md` §9](../../../notes/broken-born-theory.md#9-predictions)):

| Column | Row 4 |
|---|---|
| Observable | "Dynamical friction in dwarf cores" |
| Standard expectation | "GCs sink (cuspy CDM)" |
| Requirement of the framework | "Suppressed in condensed cores; Fornax GCs stay put" |
| Kill condition | "Demonstrated normal friction in cored dwarfs" |

GCs are globular clusters, and CDM is cold dark matter, whose halos have density cusps at their centres in simulations without self-interaction [T] ([dwarf galaxies](../halo-astrophysics/dwarf-galaxies.md)).

### The physics behind the row

**Dynamical friction** [T]. A massive body moving through a sea of lighter particles pulls them toward its path by gravity, and the overdense wake that forms behind it pulls the body back. The body loses orbital energy and spirals inward. The standard formula is Chandrasekhar's (1943)†. In a dwarf galaxy, a globular cluster orbiting inside the dark-matter halo should sink toward the centre by this drag ([halo-substructure probes](../halo-astrophysics/halo-substructure.md)).

**The Fornax timing problem** [T]. The Fornax dwarf spheroidal galaxy, a satellite of the Milky Way, has several globular clusters at large distances from its centre. Estimates of dynamical friction in a cuspy cold-dark-matter halo give sinking times shorter than the clusters' ages, so their present positions need an explanation. A cored halo, with a flat central density, slows the sinking, which is one of the standard responses [T].

**The notebook's mechanism.** §5.2, tagged "[D at mean-field level; O beyond]", read the gated attraction as a pairing interaction: "The BCS analogy is exact in structure: a momentum-gated attraction is precisely the pairing interaction, and below a critical velocity dispersion the core of a halo condenses — momentum-space clumping, realized. Consequences: superfluid-like cores in dwarfs and **suppressed dynamical friction** inside them (the Fornax globular-cluster timing problem is a feature, not a bug)." BCS is the Bardeen–Cooper–Schrieffer theory of superconductivity [T]. The analogy is with superfluids, in which a body moving slower than a critical speed experiences no drag [T]. The notebook did not derive the suppression; it listed it as a consequence of the condensed core.

### Its standing

The notebook's parameter count credits the two conjugate-matter parameters σ₀/m and v\* with "friction suppression" among the phenomena they cover (§10). Row 4 rested on the same condensation as [old row 3](velocity-granularity.md), velocity-space granularity: §5.2 derives both from the instability of a smooth velocity distribution under the gated attraction.

## How it was tested

The clumping problem tested the condensation itself, not the friction. Without a condensed core there is no superfluid-like medium and no suppression to compute. The test began with the notebook's open problem 3, the stream-instability growth rate against orbital phase mixing, and ran through three calc notes ([the founding image](founding-image.md#how-it-was-tested)).

## The evidence against it

### Particle island: no condensation

For dark-matter particles of MeV to GeV mass, [the mean-field criterion](instability-criterion.md) fails in a dwarf core by a ratio of about 10⁻²⁸ at the [scattering benchmark](../conjugate-matter/benchmark.md) ([#2](../../history/documents/clumping-notes.md)). Below threshold the velocity distribution is stable, so a halo core does not condense. [#2](../../../notes/stream-stability.md) withdrew the row on this island, together with the link to row 3: "Rows 3 (velocity granularity) and 4 (condensed cores / Fornax friction suppression) are **withdrawn**, and with them the mechanism-level linkage claimed between them." (#2, 'Consequences for the predictions table').

### Wave island: no placid condensate

Collective behaviour survives only for wave-like dark matter, on the [wave island](wave-island/_index.md) ([the classicality theorem](classicality-theorem.md)). There, under [Scenario A](wave-island/scenario-a.md), condensation is mandatory only in ultra-faint dwarfs; for a "Classical dwarf core" [#3](../../../notes/wave-island.md)'s table gives a ratio of [condensation rate](wave-island/condensation-rate.md) to orbital stirring of "~10⁻²", so condensation loses to stirring there. The notes do not apply this row to Fornax by name. Where condensation is mandatory, the endpoint is not a stable superfluid core: "Because the interaction is **attractive**, the endpoint is not a placid stream: a growing condensate with attractive self-interaction has a critical mass … above which it collapses (bosenova)" (#3; [attractive condensates](../wave-dark-matter/attractive-condensates.md)). #4 follows the collapses to a drain of the galaxy's dark matter, which observation excludes (Scenario A is under review). Under [Scenario B](wave-island/scenario-b.md) the coupling is free and condensation is optional, so it can carry no prediction.

### The withdrawal

#4 closed the clumping problem. In its words, rows 3 and 4 of the predictions table "are permanently withdrawn, on both islands. The Fornax mechanism goes with them." The notebook's addendum: "Rows 3–4 are struck from §9 permanently" ([`notes/broken-born-theory.md`](../../../notes/broken-born-theory.md), 'Addendum (v0.2)').

## What stands

The row is withdrawn and is under review. While it is withdrawn, the Fornax timing problem is an astrophysical question to which the program offers no answer. On the particle island, the program's dwarf-galaxy cores come from gated scattering, as in [self-interacting dark matter](../halo-astrophysics/self-interacting-dark-matter.md): the scattering benchmark is a fit of the cross-section to dwarf cores, and the [knee](../conjugate-matter/scattering-law.md) of that cross-section is [row 1](../../predictions/self-interaction-knee.md) of the current table. Whether a cored halo produced that way changes dynamical friction is not addressed in the sources.

## In the later tables

- [#9 §9](../../../notes/broken-born-program-v1.md#9-predictions-and-kill-conditions) lists the row, with velocity-space granularity in halos, as "Withdrawn with cause, permanently" (rows 3–4 of earlier versions; the cause is in [#9 §7](../../../notes/broken-born-program-v1.md#7-the-death-of-momentum-clumping-the-clumping-problem-closed-negative)).
- [#11 §13](../../papers/broken-born-checkpoint-v2.md#13-predictions-and-kill-conditions) lists the same two rows as withdrawn and under review. Its one withdrawal with cause is [#14's superheavy-soliton model](../candidates/soliton-candidate/obituary.md).

In #9 and #11, row 4 is [thawing dark energy](../../predictions/dark-energy-drift.md), so this wiki calls the notebook's row "old row 4" ([history of the predictions table](../../predictions/table-history.md)). Its companion is [old row 3](velocity-granularity.md).

## References

Added by the wiki from model memory (†):

- S. Chandrasekhar (1943)†: the dynamical-friction formula.

## Sources

- [`CLAUDE.md`](../../../CLAUDE.md) 'Since the handoff' — Fornax friction suppression under review
- [`notes/ufd-endpoint.md`](../../../notes/ufd-endpoint.md) 'Verdict and closure of the clumping problem' — the withdrawal, "permanently withdrawn" in its words: "The Fornax mechanism goes with them"
- [`wiki/papers/broken-born-checkpoint-v2.md` §13](../../papers/broken-born-checkpoint-v2.md#13-predictions-and-kill-conditions) — the row, withdrawn and under review; [§9](../../papers/broken-born-checkpoint-v2.md#9-momentum-clumping-the-founding-image-tested) — the founding image as P.R.'s open conjecture
- [`notes/stream-stability.md`](../../../notes/stream-stability.md) 'Consequences for the predictions table' — withdrawal on the particle island
- [`notes/wave-island.md`](../../../notes/wave-island.md) 'What pins g? Two scenarios' — the classical-dwarf ratio and the attractive endpoint
- [`notes/broken-born-theory.md` §9](../../../notes/broken-born-theory.md#9-predictions) — the row as written; [§5.2](../../../notes/broken-born-theory.md#52-collective-behavior-clumping-in-momentum-space-d-at-mean-field-level-o-beyond) — the condensed-core mechanism; [§10](../../../notes/broken-born-theory.md#10-parameter-count) — the parameter count; 'Addendum (v0.2)' — the strike
- [`notes/broken-born-program-v1.md` §9](../../../notes/broken-born-program-v1.md#9-predictions-and-kill-conditions) — the withdrawal in v1's renumbered table
