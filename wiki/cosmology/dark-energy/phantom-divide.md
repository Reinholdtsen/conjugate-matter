---
title: "The phantom divide and the null energy condition"
weight: 20
status: established
description: "Why w = −1 is a divide: a canonical scalar obeys the null energy condition and cannot reach w < −1, what a phantom phase or a crossing would require, and how the program uses the divide."
provenance: [T]
sources:
  - "notes/broken-born-theory.md §7"
  - "papers/broken-born-checkpoint-v2.md §10"
  - "papers/broken-born-checkpoint-v2.md §13 row 4"
  - "review/round3/referee/audit-notes.md Step 4(c) item 11"
  - "popsci/universes-other-half.md 'Dark energy as the orientation of the split'"
---

*The phantom divide is the value w = −1 of the dark-energy equation of state, the value a cosmological constant has, and it separates two kinds of behaviour: above it, dark energy thins out as space expands; below it, in the regime called phantom, dark energy becomes denser as space expands. An ordinary scalar field cannot reach the phantom side, because the quantity that would have to become negative is the square of the field's rate of change. That fact is a case of the null energy condition, a standard requirement on physically reasonable matter. A measured w below −1 would therefore point to something unusual, such as a field with negative kinetic energy, several interacting fields or a change to gravity. The program's [dark-energy field](/wiki/cosmology/dark-energy/tau-quintessence) is an ordinary scalar, so a robust intrinsic w < −1 would kill the program's framework outright.*

**Status:** Established — [T] — textbook physics, written here from general knowledge, with the literature it names marked †; the program's use of it is [D] in #1 §7 item 1 and is stated in [checkpoint #11](/wiki/history/documents/checkpoint) §10.

## Why w = −1 is a divide [T]

The energy density of each component of the universe obeys the continuity equation ρ̇ = −3H(ρ + p), with H the expansion rate and p the pressure ([quintessence and the equation of state](/wiki/cosmology/dark-energy/quintessence)). With p = wρ this reads

```text
ρ̇ = −3Hρ(1 + w)
```

In an expanding universe (H > 0) with positive energy density, the sign of 1 + w decides the direction of change:

- w > −1: ρ falls as space expands, like every ordinary form of matter and radiation;
- w = −1: ρ stays constant, the cosmological constant;
- w < −1: ρ grows as space expands. This is the phantom regime (Caldwell †).

For constant w the solution is ρ ∝ a^{−3(1+w)}, and a phantom exponent is positive. The value −1 is therefore a dividing line between dark energy that weakens and dark energy that strengthens, and a w(z) that passes through it is said to cross the phantom divide.

## The null energy condition [T]

### The condition

[General relativity](/wiki/gravity/spin-2-fields/general-relativity) allows any stress-energy tensor T_μν as a source, so physicists impose energy conditions to separate reasonable matter from unreasonable (Hawking and Ellis †). The weakest of the standard set is the null energy condition (NEC): for every light-like vector k,

```text
T_μν k^μ k^ν ≥ 0
```

It says that an observer moving at nearly the speed of light never measures a negative energy density.

### For a perfect fluid

A homogeneous cosmic fluid has the perfect-fluid form T_μν = (ρ + p)u_μu_ν + p g_μν (signature mostly plus), with u its four-velocity. For a light-like k the term p g_μν k^μ k^ν vanishes, leaving (ρ + p)(u·k)², and (u·k)² > 0. The condition is therefore

```text
ρ + p ≥ 0,   that is,   w ≥ −1 when ρ > 0
```

A phantom fluid violates the null energy condition, and a cosmological constant saturates it, ρ + p = 0.

### Not the strong energy condition

A different condition, the strong energy condition, requires ρ + 3p ≥ 0. Accelerated expansion needs ρ + 3p < 0 ([quintessence and the equation of state](/wiki/cosmology/dark-energy/quintessence)), so every form of dark energy violates the strong condition. Only phantom dark energy violates the null one. The divide at w = −1 is the null condition; the threshold of acceleration at w = −1/3 is the strong one.

## A canonical scalar obeys it [T]

A canonical scalar field has a kinetic term of the standard sign, ½(∂φ)² in the program's convention, plus a potential. Its stress-energy tensor is the product ∂_μφ ∂_νφ plus a term proportional to the metric. Contracted with a light-like k, the metric term drops out and what remains is a square:

```text
T_μν k^μ k^ν = (k^μ ∂_μφ)² ≥ 0
```

For a uniform field this is the statement ρ + p = φ̇², with ρ = ½φ̇² + V and p = ½φ̇² − V. The potential cancels from the sum, so no choice of potential can make it negative. A canonical scalar, alone and minimally coupled to gravity, therefore keeps w ≥ −1 whenever its energy density is positive, and its energy density never grows as the universe expands.

The popular article #12 states the same point in words: phantom behaviour "would require the orientation's kinetic energy to be negative, and kinetic energy is the square of a rate of change; a square of a real quantity cannot be negative" ('Dark energy as the orientation of the split'; [the popular articles](/wiki/history/documents/popular-articles)). The article is a gloss on the physics, not a source for any claim's status.

## Reaching the phantom side [T]

Since a single canonical scalar cannot cross w = −1, a measured phantom phase needs one of a small set of ingredients:

- **A ghost.** A scalar with the wrong sign of kinetic term has ρ + p = −φ̇² < 0 and is phantom (Caldwell †). Its quanta carry negative energy, and in an interacting theory the vacuum can decay into ghosts and ordinary particles; avoiding that needs the theory to be cut off at a low scale (Carroll, Hoffman and Trodden †; Cline, Jeon and Moore †).
- **Several fields.** A single field, canonical or ghost, cannot pass smoothly through w = −1 (Vikman †). Models with one field of each kind can, and are called quintom models (Feng, Wang and Zhang †).
- **Non-minimal couplings or modified gravity.** If the field couples to curvature, or gravity itself is modified, the effective w inferred from the expansion can fall below −1 without any component violating the null energy condition (Boisseau, Esposito-Farèse, Polarski and Starobinsky †).
- **Interactions in the dark sector.** If dark energy exchanges energy with [dark matter](/wiki/dark-matter), a fit that treats them as separate, non-interacting fluids can return an apparent w < −1 (Das, Corasaniti and Khoury †).

A constant w < −1 would make the energy density grow without limit, and the scale factor would diverge in finite time, the "big rip" (Caldwell, Kamionkowski and Weinberg †). A crossing that lasts only part of cosmic history does not need that outcome.

## Intrinsic against inferred

The last two items above produce a phantom phase in the fitted w without any component that violates the null energy condition. An equation of state is a parameter of a fitted model, not a measured property of a substance, and the program's kill condition is written with that in mind. It counts only a w < −1 "as an intrinsic equation of state, not an artifact of an assumed ΛCDM background" (#1 §7 item 1), ΛCDM being the standard model of a cosmological constant plus cold dark matter. #11 §10 makes the matching point about the current data: "w(z) is inferred from distances rather than observed". How the survey turns distances into w(z) is on [DESI baryon acoustic oscillations](/wiki/cosmology/dark-energy/desi).

## How the program uses the divide

The program's dark-energy field [τ](/wiki/cosmology/dark-energy/tau-quintessence) is a canonical scalar, S_τ = ∫√−g[½(∂τ)² − V(τ)] (#1 §3, transcribed from its LaTeX). The lab notebook applies the argument above to it ([the lab notebook](/wiki/history/documents/lab-notebook), #1 §7 item 1):

> **w ≥ −1 always.** τ is a canonical scalar; the null energy condition holds; phantom crossing is impossible. **[D]**

#11 §10 keeps the statement as "strictly w ≥ −1", inside a paragraph tagged [D + T]. The bound, its kill condition and its history are on [the no-phantom bound w ≥ −1](/wiki/cosmology/dark-energy/no-phantom-bound); the field is [τ: hilltop quintessence on the Maslov circle](/wiki/cosmology/dark-energy/tau-quintessence). The test card is [row 4: thawing dark energy, never phantom](/wiki/predictions/dark-energy-drift), whose kill condition includes a "robust intrinsic w < −1 (kills outright)" (#11 §13 row 4).

## What the current data say

The second data release (DR2) of the Dark Energy Spectroscopic Instrument (DESI) reports, in #11's quotation, "a phantom crossing to w < −1 above redshifts z ≃ 0.4" [21S] (#11 §10). At those redshifts the data favour the side of the divide that the program excludes, and the program's dark-energy sector is under real pressure (root `CLAUDE.md`, 'Since the handoff'). The finding and the program's response are on [DESI DR2's phantom crossing](/wiki/cosmology/dark-energy/desi-dr2-phantom-crossing).

The [round-3](/wiki/method/review/round-3) referee, who raised the point, also notes, quoting the release, that models respecting the null energy condition "can somewhat outperform" the cosmological-constant model, and adds that they are disfavoured relative to the w₀–wₐ fit ([the CPL parametrization](/wiki/cosmology/dark-energy/cpl-parametrization)) (`review/round3/referee/audit-notes.md` Step 4(c) item 11).

## Used by

- [The no-phantom bound w ≥ −1](/wiki/cosmology/dark-energy/no-phantom-bound) — τ obeys the null energy condition.
- [τ: hilltop quintessence on the Maslov circle](/wiki/cosmology/dark-energy/tau-quintessence) — τ is a canonical scalar.
- [DESI DR2's phantom crossing](/wiki/cosmology/dark-energy/desi-dr2-phantom-crossing) — the data that favour the other side of the divide.
- [Row 4: thawing dark energy, never phantom](/wiki/predictions/dark-energy-drift) — "robust intrinsic w < −1 (kills outright)".
- [Obituary: conjugate collapse powers our expansion](/wiki/cosmology/scale-factor-duality/collapse-powered-expansion) — its first version required w = −2, a phantom value.

## Sources

- `notes/broken-born-theory.md` §7 item 1 — the program's no-phantom statement [D] and the intrinsic-versus-artifact qualification; §3 for the canonical action
- `papers/broken-born-checkpoint-v2.md` §10 — "strictly w ≥ −1", DESI DR2's crossing and inference from distances; §13 row 4 for the kill condition
- `review/round3/referee/audit-notes.md` Step 4(c) item 11 — the referee's reading of DESI DR2 on models that respect the null energy condition
- `popsci/universes-other-half.md` 'Dark energy as the orientation of the split' — the plain-language gloss (popular article)
