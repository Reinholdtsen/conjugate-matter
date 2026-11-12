---
title: "The misalignment mechanism"
weight: 40
status: established
description: "Coherent production of a light field displaced from its minimum in the early universe, as for axions — the relic route the wave island borrows."
provenance: [T]
sources:
  - "notes/wave-island.md 'Bonus: the relic-abundance problem solves itself'"
  - "notes/wave-island.md 'Standing results after Chunks A+B'"
  - "wiki/papers/broken-born-checkpoint-v2.md §9"
  - "wiki/papers/broken-born-checkpoint-v2.md §12"
  - "wiki/papers/broken-born-checkpoint-v2.md §14"
  - "wiki/papers/broken-born-checkpoint-v2.md §15"
  - "notes/broken-born-theory.md §5.3"
  - "notes/broken-born-theory.md §11"
  - "notes/broken-born-theory.md 'Addendum (v0.2, after the clumping notes): resolution of open problem 3'"
  - "notes/broken-born-program-v1.md §7"
---

*The misalignment mechanism is a way of producing dark matter as a coherent field rather than as a thermal gas of particles. In the [early universe](../../cosmology/early-universe/_index.md) a very light scalar field starts at some value away from the minimum of its potential and stays frozen there while the universe expands faster than the field can oscillate; once the expansion rate falls below the field's mass, the field oscillates about its minimum, and the energy of the oscillation then thins out with the expansion as cold matter does. It is the standard production route for [axions](../../cosmology/dark-energy/axion-like-fields.md#as-dark-matter). The Comatter program borrows it as the production channel for [the wave branch](../momentum-clumping/wave-island/_index.md) of [conjugate matter](../conjugate-matter/_index.md), a channel the particle branch still lacks; [the ratio of dark to ordinary matter](../candidates/polarization-genesis.md) stays unexplained on both.*

**Status:** Established — [T], explained here from general knowledge — the program applies it only on the wave island ([`notes/wave-island.md`](../../../notes/wave-island.md)); the abundance ratio Ω_χ : Ω_b = 5.4 : 1 stays open for all three [dark-sector candidates](../candidates/_index.md) ([`wiki/papers/broken-born-checkpoint-v2.md` §12](../../papers/broken-born-checkpoint-v2.md#12-the-dark-sector-question-three-candidates)).

## The mechanism [T]

Consider a scalar field φ of mass m that is the same everywhere in the observable universe, in a universe expanding at the Hubble rate H ([Friedmann cosmology](../../cosmology/scale-factor-duality/friedmann-cosmology.md)). Its equation of motion is that of a damped oscillator:

```text
φ̈ + 3Hφ̇ + m²φ = 0
```

The expansion supplies the friction term. Early on, when H ≫ m, the friction dominates and the field cannot move: it stays at its initial value φ_i, and its potential energy acts as a [cosmological constant](../../cosmology/dark-energy/cosmological-constant.md). As the universe expands, H falls. When H drops to about m, the field begins to oscillate about the minimum of its potential, at frequency m. From then on the oscillation's pressure averages to zero over a cycle, and its energy density falls in inverse proportion to the volume of the universe, as the density of cold, pressureless matter does. Equivalently, the number of quanta per comoving volume stays fixed.

Two quantities set the relic density: the mass, which fixes when the oscillation starts, and the initial displacement φ_i, which fixes its amplitude. At a given mass, a larger displacement gives more dark matter.

The name comes from the axion. There the field is an angle, and its initial value in the patch that became the observable universe is not aligned with the minimum that strong-interaction effects create later; the misalignment is the initial displacement. The field's quanta are produced at essentially zero momentum, because the field starts out uniform across the horizon. In Fourier terms the oscillation is a single mode of enormous amplitude: the dark matter is born cold and with a huge [occupation number](occupation-number.md), a classical wave from the start.

**No thermal contact.** Nothing in the mechanism requires the field to have been in equilibrium with ordinary matter. The abundance is set by the field's mass and initial value, not by any interaction with the Standard Model. That makes it the natural route for a field whose only couplings are gravity and its own self-interaction.

## How the program uses it

### The wave island's production channel

[Calc note #3](../../history/documents/clumping-notes.md) found that the light branch of conjugate matter, the [wave island](../momentum-clumping/wave-island/_index.md), is such a field, and drew the consequence ('Bonus: the relic-abundance problem solves itself'):

> A field this light with only gravitational + self couplings is produced by misalignment, like an axion. Open problem [#5](../../../notes/geometric-core.md) (cannibalism-safe relic abundance) is moot on the wave island: misalignment is the mechanism, and Ω_χ trades against (m, χ_i) in the standard way.

The note does not define χ_i; in the standard treatment the relic density depends on the field's initial value [T], which is the natural reading of χ_i. Calc note [#3](../../../notes/wave-island.md)'s summary: "the relic-abundance problem resolved by misalignment" ('Standing results after Chunks A+B'). [Program v1](../../history/documents/checkpoint.md) states the same as salvage from the clumping problem: "the wave island gets its relic abundance from misalignment for free, closing a separate open problem" ([#9 §7](../../../notes/broken-born-program-v1.md#7-the-death-of-momentum-clumping-the-clumping-problem-closed-negative)). [The checkpoint](../../history/documents/checkpoint.md) lists among the clumping salvage "free relic abundance via misalignment on the wave island" ([#11 §9](../../papers/broken-born-checkpoint-v2.md#9-momentum-clumping-the-founding-image-tested)). The program's page for the application is [relic abundance by misalignment on the wave island](../momentum-clumping/wave-island/misalignment-relic.md).

The wave island itself survives only with [Scenario B](../momentum-clumping/wave-island/scenario-b.md) couplings, and the checkpoint counts its tunable collective sector among the program's [degeneration risks](../../program/assessment.md): "tunable wave-island collective sector (quarantined)" ([#11 §15](../../papers/broken-born-checkpoint-v2.md#15-assessment)).

### The particle side, still open

For particle χ, on the MeV–GeV [particle island](../momentum-clumping/classicality-theorem.md), the record does not apply the mechanism, and [the lab notebook](../../history/documents/lab-notebook.md)'s problem stands: "A sub-GeV, strongly self-coupled, gravitationally-only-connected sector cannot freeze out thermally without cannibalism problems; the abundance must be set asymmetrically" ([#1 §5.3](../../../notes/broken-born-theory.md#53-relic-abundance-o); [thermal freeze-out](../candidates/thermal-freeze-out.md#particle-χ-the-route-the-notebook-closes)). A sector that interacts with ordinary matter only through gravity cannot annihilate into Standard Model particles, so a thermal relic of it must be settled within the sector itself; in a strongly self-coupled sector, number-changing self-interactions then convert rest mass into heat, the behavior called cannibalism [T]. The notebook's remedy is an asymmetric mechanism, polarization-genesis. The mechanisms are explained on [relic abundance mechanisms](../candidates/relic-abundance.md).

### What it leaves open

Misalignment supplies a production channel; it does not explain the amount. Calc note #3: "The 5.4:1 question remains (polarization-genesis), but the *production channel* is no longer exotic." The checkpoint keeps the ratio open for all three dark-sector candidates, [χ particles](../candidates/chi-particles.md), [the X-condensate](../candidates/x-condensate.md) and P.R.'s conjecture of [magnetic monopoles abundant in momentum space](../candidates/momentum-space-monopoles.md): "The 5.4 : 1 abundance question (polarization-genesis) applies to all three" ([#11 §12](../../papers/broken-born-checkpoint-v2.md#12-the-dark-sector-question-three-candidates)), listed as item 7 of its [open problems](../../status/open-problems.md), "Polarization-genesis: Ω_χ : Ω_b = 5.4 : 1 [O]" ([#11 §14](../../papers/broken-born-checkpoint-v2.md#14-open-problems), OP7). See [Open: polarization-genesis](../candidates/polarization-genesis.md).

### A numbering note

Calc note #3's "Open problem #5" is item 5 of the lab notebook's open problems, "**Relic abundance** without cannibalism: needs the asymmetric mechanism of (4)" ([#1 §11](../../../notes/broken-born-theory.md#11-open-problems-in-order-of-severity)), not item 5 of the checkpoint's list, which is [the dual-stress enhancement](../conjugate-matter/dual-stress-enhancement.md). The lab notebook's addendum v0.2 states the closure more broadly than calc note #3 does — "open problems 3 and 5 close (5 via misalignment production on the wave island)" — while calc note #3 confines it to the wave island. The wiki follows the checkpoint: the channel exists on the wave island, and the ratio stays open for all three candidates.

## References

The program's documents cite no source for the misalignment mechanism. Added by the wiki from model memory (†):

- J. Preskill, M. B. Wise, F. Wilczek, "Cosmology of the invisible axion," Phys. Lett. B (1983)†.
- L. F. Abbott, P. Sikivie, "A cosmological bound on the invisible axion," Phys. Lett. B (1983)†.
- M. Dine, W. Fischler, "The not-so-harmless axion," Phys. Lett. B (1983)†.
- D. J. E. Marsh, "Axion cosmology," Phys. Rep. (2016)†: a review, including ultralight axion-like fields.

## Used by

- [Relic abundance by misalignment on the wave island](../momentum-clumping/wave-island/misalignment-relic.md) — the program's application of the mechanism.
- [The wave island](../momentum-clumping/wave-island/_index.md) — its relic abundance.
- [Open: polarization-genesis and the 5.4 : 1 ratio](../candidates/polarization-genesis.md) — the ratio that misalignment does not explain.
- [The X-condensate candidate](../candidates/x-condensate.md) — a uniform oscillation behaves as cold matter, which for a light scalar is this mechanism; the spin-2 case is on [bigravity dark matter](../candidates/bigravity-dark-matter.md).

## Sources

- [`wiki/papers/broken-born-checkpoint-v2.md` §9](../../papers/broken-born-checkpoint-v2.md#9-momentum-clumping-the-founding-image-tested), [§12](../../papers/broken-born-checkpoint-v2.md#12-the-dark-sector-question-three-candidates), [§14](../../papers/broken-born-checkpoint-v2.md#14-open-problems), [§15](../../papers/broken-born-checkpoint-v2.md#15-assessment) — the salvage item; the 5.4 : 1 question for all three candidates; open problem 7; the quarantined wave-island sector
- [`notes/wave-island.md`](../../../notes/wave-island.md) 'Bonus: the relic-abundance problem solves itself', 'Standing results after Chunks A+B' — the program's use of misalignment and its limits
- [`notes/broken-born-theory.md` §5.3](../../../notes/broken-born-theory.md#53-relic-abundance-o), [§11](../../../notes/broken-born-theory.md#11-open-problems-in-order-of-severity), 'Addendum (v0.2, after the clumping notes): resolution of open problem 3' — the particle-side relic problem; the v0.1 open-problem numbering; the broader closure claim
- [`notes/broken-born-program-v1.md` §7](../../../notes/broken-born-program-v1.md#7-the-death-of-momentum-clumping-the-clumping-problem-closed-negative) — misalignment as clumping salvage in v1
