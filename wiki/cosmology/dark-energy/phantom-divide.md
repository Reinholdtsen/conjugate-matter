---
title: "The phantom divide and the null energy condition"
weight: 20
status: established
description: "Why w = −1 is a divide: a canonical scalar obeys the null energy condition and cannot reach w < −1, and what a phantom crossing would require."
provenance: [T]
sources:
  - "notes/broken-born-theory.md §7"
  - "papers/broken-born-checkpoint-v2.md §10"
  - "review/round3/referee/audit-notes.md Step 4(c) item 11"
  - "popsci/universes-other-half.md 'Dark energy as the orientation of the split'"
---

*The phantom divide is the value w = −1 of the dark-energy equation of state, the value a cosmological constant has, and it separates two kinds of behaviour: above it, dark energy thins out as space expands; below it, in the regime called phantom, dark energy becomes denser as space expands. An ordinary scalar field cannot reach the phantom side, because the quantity that would have to become negative is the square of the field's rate of change. That fact is a case of the null energy condition, a standard requirement on physically reasonable matter. A measured w below −1 would therefore point to something unusual, such as a field with negative kinetic energy, several interacting fields or a change to gravity, and a robust intrinsic one would kill the program's framework outright.*

**Status:** Established — [T] — textbook physics, written here from general knowledge; the program's use of it is [D] in #1 §7 item 1 and is stated in #11 §10.

## Key facts

- **The condition [T].** The null energy condition requires T_μν k^μ k^ν ≥ 0 for every light-like vector k. For a perfect fluid it reads ρ + p ≥ 0, which for positive energy density means w ≥ −1.
- **A canonical scalar obeys it [T].** For a uniform canonical scalar, ρ + p = φ̇² ≥ 0. Since ρ̇ = −3H(ρ + p), its energy density can only fall or hold steady as the universe expands. The popular article #12 puts it as "a square of a real quantity cannot be negative".
- **Phantom [T].** With w < −1, ρ ∝ a^{−3(1+w)} grows as a grows. Reaching that regime needs a ghost (a field with negative kinetic energy), several fields, non-minimal couplings or modified gravity; a single canonical scalar cannot cross w = −1.
- **Intrinsic versus inferred.** The program's kill condition counts only w < −1 "as an intrinsic equation of state, not an artifact of an assumed ΛCDM background" (#1 §7 item 1), and #11 §10 notes that "w(z) is inferred from distances rather than observed".
- **The program's use.** #1 §7 item 1: "**w ≥ −1 always.** τ is a canonical scalar; the null energy condition holds; phantom crossing is impossible. **[D]**" See [the no-phantom bound w ≥ −1](/wiki/cosmology/dark-energy/no-phantom-bound), and for the field, [quintessence and the equation of state](/wiki/cosmology/dark-energy/quintessence).
- **Current data.** Data Release 2 of the Dark Energy Spectroscopic Instrument reports "a phantom crossing to w < −1 above redshifts z ≃ 0.4" [21S] (#11 §10); see [DESI DR2's phantom crossing](/wiki/cosmology/dark-energy/desi-dr2-phantom-crossing). The round-3 referee also quotes the release as finding that models respecting the null energy condition "can somewhat outperform" the cosmological-constant model, while noting that they are disfavoured relative to the w₀–wₐ fit (`review/round3/referee/audit-notes.md` Step 4(c) item 11).

## Used by

- [The no-phantom bound w ≥ −1](/wiki/cosmology/dark-energy/no-phantom-bound) — τ obeys the null energy condition.
- [DESI DR2's phantom crossing](/wiki/cosmology/dark-energy/desi-dr2-phantom-crossing) — the data that favour the other side of the divide.
- [Row 4: thawing dark energy, never phantom](/wiki/predictions/dark-energy-drift) — "robust intrinsic w < −1 (kills outright)".
- [Obituary: conjugate collapse powers our expansion](/wiki/cosmology/scale-factor-duality/collapse-powered-expansion) — its first version required w = −2.

## Sources

- `notes/broken-born-theory.md` §7 item 1 — the program's no-phantom statement and the intrinsic-versus-artifact qualification
- `papers/broken-born-checkpoint-v2.md` §10 — "strictly w ≥ −1", DESI DR2's crossing, and inference from distances
- `review/round3/referee/audit-notes.md` Step 4(c) item 11 — the referee's reading of DESI DR2 on models that respect the null energy condition
- `popsci/universes-other-half.md` 'Dark energy as the orientation of the split' — the plain-language gloss (popular article)
