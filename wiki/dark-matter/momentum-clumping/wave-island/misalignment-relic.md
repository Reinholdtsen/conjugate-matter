---
title: "Relic abundance by misalignment on the wave island"
weight: 40
status: alive
description: "A field this light with only gravitational and self couplings is produced by misalignment, which makes the lab notebook's cannibalism-safe relic-abundance problem moot — on the wave island only; the 5.4 : 1 ratio stays open."
sources:
  - "notes/wave-island.md 'Bonus'"
  - "notes/wave-island.md 'Standing results'"
  - "wiki/papers/broken-born-checkpoint-v2.md §9"
  - "wiki/papers/broken-born-checkpoint-v2.md §12"
  - "wiki/papers/broken-born-checkpoint-v2.md §14 item 7"
  - "wiki/papers/broken-born-checkpoint-v2.md §14 item 5"
  - "notes/broken-born-theory.md §5.3"
  - "notes/broken-born-theory.md §8"
  - "notes/broken-born-theory.md §11"
  - "notes/broken-born-theory.md 'Addendum (v0.2)'"
  - "notes/broken-born-program-v1.md §7"
  - "notes/broken-born-program-v1.md §10"
  - "notes/ufd-endpoint.md 'Verdict and closure'"
  - "HANDOFF.md §3"
---

*[Misalignment](../../wave-dark-matter/misalignment-mechanism.md) is a way for a very light field to acquire its relic density in the [early universe](../../../cosmology/early-universe/_index.md): the field starts away from the minimum of its potential, stays there while the universe expands quickly, and later oscillates coherently about the minimum; the oscillation then behaves as cold dark matter. It is the standard production route for [axions](../../../cosmology/dark-energy/axion-like-fields.md#as-dark-matter). [The clumping problem](../../../history/main-problems.md) noted that [conjugate matter](../../conjugate-matter/_index.md) χ on the [wave island](_index.md), a field this light, coupled only through gravity and its own self-interaction, would be produced the same way. On the wave island only, that removes a difficulty [the lab notebook](../../../history/documents/lab-notebook.md) had recorded: a light, strongly self-coupled sector connected to ordinary matter only through gravity cannot get its density by ordinary [thermal freeze-out](../../candidates/thermal-freeze-out.md#particle-χ-the-route-the-notebook-closes). It does not explain why dark matter outweighs ordinary matter by 5.4 to 1, a question that stays open for all three dark-matter candidates.*

**Status:** Alive, on the wave island only. It is part of the clumping problem's salvage in [checkpoint #11](../../../history/documents/checkpoint.md) [§9](../../../papers/broken-born-checkpoint-v2.md#9-momentum-clumping-the-founding-image-tested) ("free relic abundance via misalignment on the wave island"), with no tag of its own. Not machine-checked; the claim contains no number. The 5.4 : 1 question "applies to all three" dark-matter candidates ([#11 §12](../../../papers/broken-born-checkpoint-v2.md#12-the-dark-sector-question-three-candidates-and-the-failure-of-one-model)) and is item 7 of [#11 §14](../../../papers/broken-born-checkpoint-v2.md#14-open-problems), OP7 ([Open: polarization-genesis](../../candidates/polarization-genesis.md)).

## The statement

[`notes/wave-island.md`](../../../../notes/wave-island.md) ([calc note #3](../../../history/documents/clumping-notes.md)), in a closing section titled 'Bonus: the relic-abundance problem solves itself':

> A field this light with only gravitational + self couplings is produced by misalignment, like an axion. Open problem [#5](../../../../notes/geometric-core.md) (cannibalism-safe relic abundance) is moot on the wave island: misalignment is the mechanism, and Ω_χ trades against (m, χ_i) in the standard way. The 5.4:1 question remains (polarization-genesis), but the production channel is no longer exotic.

Ω_χ is the present density of χ as a fraction of the critical density, and m is its mass. The note does not define χ_i; in the standard treatment the relic density depends on the field's initial value [T], which is the natural reading. The note's summary of the wave island ends "the relic-abundance problem resolved by misalignment" ('Standing results after Chunks A+B').

The claim has three parts: χ on the wave island is the kind of field misalignment produces; for that field the notebook's relic-abundance problem no longer arises; and the ratio of dark to ordinary matter is still unexplained.

## Background: the misalignment mechanism [T]

A homogeneous scalar field φ of mass m in an expanding universe obeys the equation of a damped oscillator [T]:

```text
φ̈ + 3Hφ̇ + m²φ = 0
```

where H is the [Hubble rate](../../../cosmology/scale-factor-duality/friedmann-cosmology.md). While H ≫ m the friction term holds the field at its initial value. When H falls to about m, the field starts to oscillate about the minimum of its potential, and from then on the energy of the oscillation dilutes with the volume of the universe, as the density of cold, pressureless matter does [T]. The relic density is set by two inputs: the mass, which fixes when the oscillation starts, and the initial displacement, which fixes its amplitude. That is the sense of "Ω_χ trades against (m, χ_i)": for a given mass, the observed density fixes the initial value, and conversely.

Two features fit the wave island. The oscillation is a single, nearly uniform mode of enormous amplitude, so the dark matter it produces is cold and has a huge [occupation number](../../wave-dark-matter/occupation-number.md): a classical wave from the start. And the mechanism needs no contact with the thermal bath of ordinary particles, so a field coupled only through gravity and its own self-interaction can use it. The mechanism is described on [the misalignment mechanism](../../wave-dark-matter/misalignment-mechanism.md).

The word has a second meaning in the program. The "misalignment potential" of the field-equation problem [tuning test](../../../gravity/tuning-test/_index.md) is the Higgs-sector potential penalizing incompatibility between the polarization and the [modular field](../../../phase-space/modular-field/modular-field-z.md) ([the misalignment potential](../../../gravity/tuning-test/misalignment-potential.md)); it is unrelated to relic production.

## The problem it removes

[The lab notebook](../../../history/documents/lab-notebook.md) ([#1](../../../../notes/broken-born-theory.md), v0.1) had left the relic abundance of conjugate matter open ([§5.3](../../../../notes/broken-born-theory.md#53-relic-abundance-o), tagged [O]):

> A sub-GeV, strongly self-coupled, gravitationally-only-connected sector cannot freeze out thermally without cannibalism problems; the abundance must be set asymmetrically — by polarization-genesis (§8). The observed Ω_χ/Ω_b = 5.4 is an input awaiting a mechanism, exactly as η_B awaited baryogenesis.

Here Ω_b is the baryon density and η_B the baryon asymmetry of the universe. The background is standard [T] ([relic abundance mechanisms](../../candidates/relic-abundance.md)). A thermal relic gets its density by freeze-out: it annihilates while in equilibrium, and its abundance freezes when annihilation becomes too slow to keep up with the expansion. A sector that couples to ordinary matter only through gravity cannot annihilate into Standard Model particles, so its freeze-out happens within the sector itself. If its strong self-interactions change particle number, for instance three particles going to two, the annihilations convert rest mass into kinetic energy, and the sector cools more slowly than an ordinary relic as the universe expands; this is called cannibalism, and it changes the relic's abundance and temperature. The notebook concluded that the abundance had to be set some other way, by an asymmetry, and listed the item fifth among its open problems: "Relic abundance without cannibalism: needs the asymmetric mechanism of (4)" ([#1 §11](../../../../notes/broken-born-theory.md#11-open-problems-in-order-of-severity)), where item 4 is polarization-genesis.

Misalignment bypasses the issue on the wave island. A field that is never in thermal equilibrium does not freeze out, and its density comes from its initial condition rather than from annihilation [T]. In calc note [#3](../../../../notes/wave-island.md)'s words, the production channel "is no longer exotic".

## On the wave island only

The argument uses two properties of the field: it is light, and its only couplings are gravity and self-interaction. The second is what the notebook already assumed for its sub-GeV sector, a "gravitationally-only-connected sector" ([#1 §5.3](../../../../notes/broken-born-theory.md#53-relic-abundance-o)); the first holds only on the wave island, which calc note [#4](../../../../notes/ufd-endpoint.md) left at "roughly 3×10⁻¹⁹ eV ≲ m ≲ 10⁻⁴ eV with Scenario-B couplings" ('Verdict and closure of the clumping problem'). The salvage is stated for that branch alone:

- Calc note #3: the problem "is moot on the wave island".
- [#11 §9](../../../papers/broken-born-checkpoint-v2.md#9-momentum-clumping-the-founding-image-tested), listing what the clumping problem left standing: "free relic abundance via misalignment on the wave island".

For particle χ, the MeV–GeV branch of [the classicality theorem](../classicality-theorem.md) and the first of the three [dark-matter candidates](../../candidates/_index.md) ([the χ-particle candidate](../../candidates/chi-particles.md)), the sources offer only the notebook's own answer, an asymmetry set by polarization-genesis, which is still a sketch; the problem stands there.

The wave island itself survives only with [Scenario B](scenario-b.md) couplings, after calc note #4 found [Scenario A](scenario-a.md) contradicted by the ultra-faint dwarfs; Scenario A is under review ([#11 §9](../../../papers/broken-born-checkpoint-v2.md#9-momentum-clumping-the-founding-image-tested)). [#11 §9](../../../papers/broken-born-checkpoint-v2.md#9-momentum-clumping-the-founding-image-tested) lists the misalignment salvage after recording that result.

## What remains open: the 5.4 : 1 ratio

Misalignment supplies a channel, not an amount. Its output depends on (m, χ_i), and nothing in it explains why the result is 5.4 times the density of baryons. Calc note #3 keeps the question with polarization-genesis: "The 5.4:1 question remains (polarization-genesis), but the production channel is no longer exotic."

The checkpoint keeps it open for all three dark-sector candidates, χ particles, [the X-condensate](../../candidates/x-condensate.md) and P.R.'s conjecture of [magnetic monopoles abundant in momentum space](../../candidates/momentum-space-monopoles.md): "The 5.4 : 1 abundance question (polarization-genesis) applies to all three." ([#11 §12](../../../papers/broken-born-checkpoint-v2.md#12-the-dark-sector-question-three-candidates-and-the-failure-of-one-model).) It is item 7 of [#11 §14](../../../papers/broken-born-checkpoint-v2.md#14-open-problems): "Polarization-genesis: Ω_χ : Ω_b = 5.4 : 1 [O]." The lab notebook's sketch of polarization-genesis ([#1 §8](../../../../notes/broken-born-theory.md#8-polarization-genesis-o-sketched), "[O, sketched]") has heavy moduli decaying at reheating, with their branching into x- and p-polarized quanta set by a vacuum tilt angle, and calls itself "a shape, not a mechanism". See [Open: polarization-genesis](../../candidates/polarization-genesis.md).

## The record, and which open problem 5

The closure appears in four documents, with slightly different reach:

- [The lab notebook](../../../history/documents/lab-notebook.md)'s addendum v0.2 (#1): "open problems 3 and 5 close (5 via misalignment production on the wave island)".
- Program v1 ([#9 §7 item 3](../../../../notes/broken-born-program-v1.md#7-the-death-of-momentum-clumping-the-clumping-problem-closed-negative)): "the wave island gets its relic abundance from misalignment for free, closing a separate open problem". Its list of open problems ([#9 §10](../../../../notes/broken-born-program-v1.md#10-open-problems)) keeps polarization-genesis, the 5.4 : 1 ratio, as item 6.
- Checkpoint [#11 §9](../../../papers/broken-born-checkpoint-v2.md#9-momentum-clumping-the-founding-image-tested): "free relic abundance via misalignment on the wave island".
- [The handoff](../../../history/documents/handoff.md) ([`HANDOFF.md` §3](../../../../HANDOFF.md#3-artifact-inventory-creation-order), row 3) describes calc note #3 as ending with "misalignment fixes the relic abundance".

Calc note #3's "Open problem #5" uses the lab notebook's numbering: it is item 5 of [#1 §11](../../../../notes/broken-born-theory.md#11-open-problems-in-order-of-severity), relic abundance without cannibalism. Item 5 of [#11 §14](../../../papers/broken-born-checkpoint-v2.md#14-open-problems) is a different problem, [the dual-stress enhancement](../../conjugate-matter/dual-stress-enhancement.md) (OP5). The notebook's addendum says the problem closes, with the wave-island qualifier in parentheses, and calc note #3 and [#11 §9](../../../papers/broken-born-checkpoint-v2.md#9-momentum-clumping-the-founding-image-tested) state the closure for the wave island only; [#11 §12](../../../papers/broken-born-checkpoint-v2.md#12-the-dark-sector-question-three-candidates-and-the-failure-of-one-model) keeps the 5.4 : 1 ratio open for all three candidates. The wiki follows #11 ([conflicts between sources](../../../history/documents/source-conflicts.md)).

## Sources

- [`notes/wave-island.md`](../../../../notes/wave-island.md) 'Bonus: the relic-abundance problem solves itself' — the statement and what remains; 'Standing results after Chunks A+B' — the summary line
- [`wiki/papers/broken-born-checkpoint-v2.md` §9](../../../papers/broken-born-checkpoint-v2.md#9-momentum-clumping-the-founding-image-tested) — the salvage line, and Scenario A under review; [§12](../../../papers/broken-born-checkpoint-v2.md#12-the-dark-sector-question-three-candidates-and-the-failure-of-one-model) — the candidates table and the 5.4 : 1 question for all three; [§14 item 7](../../../papers/broken-born-checkpoint-v2.md#14-open-problems) — polarization-genesis as an open item; [§14 item 5](../../../papers/broken-born-checkpoint-v2.md#14-open-problems) — the different open problem 5
- [`notes/broken-born-theory.md` §5.3](../../../../notes/broken-born-theory.md#53-relic-abundance-o) — the original relic-abundance problem [O]; [§8](../../../../notes/broken-born-theory.md#8-polarization-genesis-o-sketched) — the polarization-genesis sketch; [§11 item 5](../../../../notes/broken-born-theory.md#11-open-problems-in-order-of-severity) — its place in the notebook's list; 'Addendum (v0.2)' — the notebook's record of the closure
- [`notes/broken-born-program-v1.md` §7 item 3](../../../../notes/broken-born-program-v1.md#7-the-death-of-momentum-clumping-the-clumping-problem-closed-negative) — the v1 statement; [§10 item 6](../../../../notes/broken-born-program-v1.md#10-open-problems) — polarization-genesis still open
- [`notes/ufd-endpoint.md`](../../../../notes/ufd-endpoint.md) 'Verdict and closure of the clumping problem' — the surviving wave island
- [`HANDOFF.md` §3 row 3](../../../../HANDOFF.md#3-artifact-inventory-creation-order) — the inventory description of calc note #3
