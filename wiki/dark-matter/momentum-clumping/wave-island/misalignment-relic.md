---
title: "Relic abundance by misalignment on the wave island"
weight: 40
status: alive
description: "A field this light with only gravitational and self couplings is produced by misalignment, which makes the lab notebook's cannibalism-safe relic-abundance problem moot — on the wave island only; the 5.4 : 1 ratio stays open."
sources:
  - "notes/debt3b-wave-island.md 'Bonus'"
  - "notes/debt3b-wave-island.md 'Standing results'"
  - "papers/broken-born-checkpoint-v2.md §9"
  - "papers/broken-born-checkpoint-v2.md §12"
  - "papers/broken-born-checkpoint-v2.md §14 item 7"
  - "papers/broken-born-checkpoint-v2.md §14 item 5"
  - "notes/broken-born-theory.md §5.3"
  - "notes/broken-born-theory.md §8"
  - "notes/broken-born-theory.md §11"
  - "notes/broken-born-theory.md 'Addendum (v0.2)'"
  - "notes/broken-born-program-v1.md §7"
  - "notes/broken-born-program-v1.md §10"
  - "notes/debt3c-ufd-endpoint.md 'Verdict and closure'"
  - "HANDOFF.md §3"
---

*[Misalignment](/wiki/dark-matter/wave-dark-matter/misalignment-mechanism) is a way for a very light field to acquire its relic density in the [early universe](/wiki/cosmology/early-universe): the field starts away from the minimum of its potential, stays there while the universe expands quickly, and later oscillates coherently about the minimum; the oscillation then behaves as cold dark matter. It is the standard production route for [axions](/wiki/cosmology/dark-energy/axion-like-fields#as-dark-matter). [Debt 3](/wiki/history/debts) noted that [conjugate matter](/wiki/dark-matter/conjugate-matter) χ on the [wave island](/wiki/dark-matter/momentum-clumping/wave-island), a field this light, coupled only through gravity and its own self-interaction, would be produced the same way. On the wave island only, that removes a difficulty [the lab notebook](/wiki/history/documents/lab-notebook) had recorded: a light, strongly self-coupled sector connected to ordinary matter only through gravity cannot get its density by ordinary [thermal freeze-out](/wiki/dark-matter/candidates/thermal-freeze-out#particle-χ-the-route-the-notebook-closes). It does not explain why dark matter outweighs ordinary matter by 5.4 to 1, a question that stays open for both remaining dark-matter candidates.*

**Status:** Alive, on the wave island only. It is part of Debt 3's salvage in [checkpoint #11](/wiki/history/documents/checkpoint) §9 ("free relic abundance via misalignment on the wave island"), with no tag of its own. Not machine-checked; the claim contains no number. The 5.4 : 1 question "applies to both" candidates (#11 §12) and is item 7 of #11 §14, OP7 ([Open: polarization-genesis](/wiki/dark-matter/candidates/polarization-genesis)).

## The statement

`notes/debt3b-wave-island.md` ([calc note #3](/wiki/history/documents/debt-3-notes)), in a closing section titled 'Bonus: the relic debt closes itself':

> A field this light with only gravitational + self couplings is produced by misalignment, like an axion. Open problem #5 (cannibalism-safe relic abundance) is moot on the wave island: misalignment is the mechanism, and Ω_χ trades against (m, χ_i) in the standard way. The 5.4:1 question remains (polarization-genesis), but the production channel is no longer exotic.

Ω_χ is the present density of χ as a fraction of the critical density, and m is its mass. The note does not define χ_i; in the standard treatment the relic density depends on the field's initial value [T], which is the natural reading. The note's summary of the wave island ends "relic debt resolved by misalignment" ('Standing results after Chunks A+B').

The claim has three parts: χ on the wave island is the kind of field misalignment produces; for that field the notebook's relic-abundance problem no longer arises; and the ratio of dark to ordinary matter is still unexplained.

## Background: the misalignment mechanism [T]

A homogeneous scalar field φ of mass m in an expanding universe obeys the equation of a damped oscillator [T]:

```text
φ̈ + 3Hφ̇ + m²φ = 0
```

where H is the [Hubble rate](/wiki/cosmology/scale-factor-duality/friedmann-cosmology). While H ≫ m the friction term holds the field at its initial value. When H falls to about m, the field starts to oscillate about the minimum of its potential, and from then on the energy of the oscillation dilutes with the volume of the universe, as the density of cold, pressureless matter does [T]. The relic density is set by two inputs: the mass, which fixes when the oscillation starts, and the initial displacement, which fixes its amplitude. That is the sense of "Ω_χ trades against (m, χ_i)": for a given mass, the observed density fixes the initial value, and conversely.

Two features fit the wave island. The oscillation is a single, nearly uniform mode of enormous amplitude, so the dark matter it produces is cold and has a huge [occupation number](/wiki/dark-matter/wave-dark-matter/occupation-number): a classical wave from the start. And the mechanism needs no contact with the thermal bath of ordinary particles, so a field coupled only through gravity and its own self-interaction can use it. The mechanism is described on [the misalignment mechanism](/wiki/dark-matter/wave-dark-matter/misalignment-mechanism).

The word has a second meaning in the program. The "misalignment potential" of the Debt-1 [tuning test](/wiki/gravity/tuning-test) is the Higgs-sector potential penalizing incompatibility between the polarization and the [modular field](/wiki/phase-space/modular-field/modular-field-z) ([the misalignment potential](/wiki/gravity/tuning-test/misalignment-potential)); it is unrelated to relic production.

## The problem it removes

[The lab notebook](/wiki/history/documents/lab-notebook) (#1, v0.1) had left the relic abundance of conjugate matter open (§5.3, tagged [O]):

> A sub-GeV, strongly self-coupled, gravitationally-only-connected sector cannot freeze out thermally without cannibalism problems; the abundance must be set asymmetrically — by polarization-genesis (§8). The observed Ω_χ/Ω_b = 5.4 is an input awaiting a mechanism, exactly as η_B awaited baryogenesis.

Here Ω_b is the baryon density and η_B the baryon asymmetry of the universe. The background is standard [T] ([relic abundance mechanisms](/wiki/dark-matter/candidates/relic-abundance)). A thermal relic gets its density by freeze-out: it annihilates while in equilibrium, and its abundance freezes when annihilation becomes too slow to keep up with the expansion. A sector that couples to ordinary matter only through gravity cannot annihilate into Standard Model particles, so its freeze-out happens within the sector itself. If its strong self-interactions change particle number, for instance three particles going to two, the annihilations convert rest mass into kinetic energy, and the sector cools more slowly than an ordinary relic as the universe expands; this is called cannibalism, and it changes the relic's abundance and temperature. The notebook concluded that the abundance had to be set some other way, by an asymmetry, and listed the item fifth among its open problems: "Relic abundance without cannibalism: needs the asymmetric mechanism of (4)" (#1 §11), where item 4 is polarization-genesis.

Misalignment bypasses the issue on the wave island. A field that is never in thermal equilibrium does not freeze out, and its density comes from its initial condition rather than from annihilation [T]. In Debt 3b's words, the production channel "is no longer exotic".

## On the wave island only

The argument uses two properties of the field: it is light, and its only couplings are gravity and self-interaction. The second is what the notebook already assumed for its sub-GeV sector, a "gravitationally-only-connected sector" (#1 §5.3); the first holds only on the wave island, which Debt 3c left at "roughly 3×10⁻¹⁹ eV ≲ m ≲ 10⁻⁴ eV with Scenario-B couplings" ('Verdict and closure of Debt 3'). The salvage is stated for that branch alone:

- Debt 3b: the problem "is moot on the wave island".
- #11 §9, listing what Debt 3 left standing: "free relic abundance via misalignment on the wave island".

For particle χ, the MeV–GeV branch of [the classicality theorem](/wiki/dark-matter/momentum-clumping/classicality-theorem) and the first of the two [remaining candidates](/wiki/dark-matter/candidates) ([the χ-particle candidate](/wiki/dark-matter/candidates/chi-particles)), the sources offer only the notebook's own answer, an asymmetry set by polarization-genesis, which is still a sketch; the problem stands there.

The wave island itself survives only with [Scenario B](/wiki/dark-matter/momentum-clumping/wave-island/scenario-b) couplings, after [Scenario A](/wiki/dark-matter/momentum-clumping/wave-island/scenario-a) was falsified. #11 §9 lists the misalignment salvage after recording that falsification.

## What remains open: the 5.4 : 1 ratio

Misalignment supplies a channel, not an amount. Its output depends on (m, χ_i), and nothing in it explains why the result is 5.4 times the density of baryons. Debt 3b keeps the question with polarization-genesis: "The 5.4:1 question remains (polarization-genesis), but the production channel is no longer exotic."

The checkpoint keeps it open for both dark-sector candidates, χ particles and [the X-condensate](/wiki/dark-matter/candidates/x-condensate): "The 5.4 : 1 abundance question (polarization-genesis) applies to both." (#11 §12.) It is item 7 of #11 §14: "Polarization-genesis: Ω_χ : Ω_b = 5.4 : 1 [O]." The lab notebook's sketch of polarization-genesis (#1 §8, "[O, sketched]") has heavy moduli decaying at reheating, with their branching into x- and p-polarized quanta set by a vacuum tilt angle, and calls itself "a shape, not a mechanism". See [Open: polarization-genesis](/wiki/dark-matter/candidates/polarization-genesis).

## The record, and which open problem 5

The closure appears in four documents, with slightly different reach:

- [The lab notebook](/wiki/history/documents/lab-notebook)'s addendum v0.2 (#1): "open problems 3 and 5 close (5 via misalignment production on the wave island)".
- Program v1 (#9 §7 item 3): "the wave island gets its relic abundance from misalignment for free, closing a separate open problem". Its list of open problems (#9 §10) keeps polarization-genesis, the 5.4 : 1 ratio, as item 6.
- Checkpoint #11 §9: "free relic abundance via misalignment on the wave island".
- [The handoff](/wiki/history/documents/handoff) (`HANDOFF.md` §3, row 3) describes Debt 3b as ending with "misalignment fixes relic debt".

Debt 3b's "Open problem #5" uses the lab notebook's numbering: it is item 5 of #1 §11, relic abundance without cannibalism. Item 5 of #11 §14 is a different problem, [the dual-stress enhancement](/wiki/dark-matter/conjugate-matter/dual-stress-enhancement) (OP5). The notebook's addendum says the problem closes, with the wave-island qualifier in parentheses, and Debt 3b and #11 §9 state the closure for the wave island only; #11 §12 keeps the 5.4 : 1 ratio open for both candidates. The wiki follows #11 ([conflicts between sources](/wiki/history/documents/source-conflicts)).

## Sources

- `notes/debt3b-wave-island.md` 'Bonus: the relic debt closes itself' — the statement and what remains; 'Standing results after Chunks A+B' — the summary line
- `papers/broken-born-checkpoint-v2.md` §9 — the salvage line; §12 — the candidates table and the 5.4 : 1 question for both; §14 item 7 — polarization-genesis as an open item; §14 item 5 — the different open problem 5
- `notes/broken-born-theory.md` §5.3 — the original relic-abundance problem [O]; §8 — the polarization-genesis sketch; §11 item 5 — its place in the notebook's list; 'Addendum (v0.2)' — the notebook's record of the closure
- `notes/broken-born-program-v1.md` §7 item 3 — the v1 statement; §10 item 6 — polarization-genesis still open
- `notes/debt3c-ufd-endpoint.md` 'Verdict and closure of Debt 3' — the surviving wave island
- `HANDOFF.md` §3 row 3 — the inventory description of Debt 3b
