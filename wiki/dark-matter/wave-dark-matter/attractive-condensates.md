---
title: "Attractive condensates: critical mass and the bosenova"
weight: 30
status: established
description: "Above a critical mass M_crit ≈ 3.6M_P/(m√g) an attractive condensate collapses, ejects fast waves and regrows: the bosenova cycle."
provenance: [T]
sources:
  - "notes/debt3b-wave-island.md 'What pins g? Two scenarios'"
  - "notes/debt3c-ufd-endpoint.md 'The attractive endpoint: criticality and the drain'"
  - "papers/broken-born-checkpoint-v2.md §9"
  - "papers/broken-born-checkpoint-v2.md ref [14]"
  - "papers/broken-born-checkpoint-v2.md ref [13]"
---

*An attractive condensate is a Bose star — a self-gravitating clump of a light boson field, all in one coherent state — whose particles also attract one another through a self-interaction. Gravity and the self-attraction both pull inward against the outward pressure that comes from the field's wave nature, and the self-attraction grows faster with density, so such a condensate has a maximum stable mass. Above it the condensate collapses, throws off part of its mass as fast waves in a burst called a bosenova, and the remnant grows again. In the program this cycle is the endpoint that, in [Scenario A](/wiki/dark-matter/momentum-clumping/wave-island/scenario-a) of the wave island, would have drained the dark matter out of the ultra-faint dwarf galaxies.*

**Status:** Established — [T] — the critical mass is a "dilute-boson-star bound, Chavanis-type" (Debt 3b; [the checkpoint](/wiki/history/documents/checkpoint)'s [14]†) and the collapse cycle an "LPT 2017-type result" (Debt 3c; [13]†) — not machine-checked; the coefficient 3.6 and both citations are unchecked.

## Key facts

- **The bound.** "Because the interaction is **attractive**, the endpoint is not a placid stream: a growing condensate with attractive self-interaction has a critical mass, M_crit ≈ 3.6 M_P/(m√g) [T: dilute-boson-star bound, Chavanis-type], above which it collapses (bosenova)" (`notes/debt3b-wave-island.md`). Here m is the boson mass and g the gated contact coupling of the [Debt-3 notes](/wiki/history/documents/debt-3-notes), in GeV⁻².
- **The cycle.** "grow to M_crit → collapse → eject an O(0.1–1) fraction as fast/relativistic waves (bosenova; LPT 2017-type result [T]) → remnant regrows" (`notes/debt3c-ufd-endpoint.md`), where LPT is Levkov–Panin–Tkachev. "Ejecta velocities are set by the dense collapse stage and vastly exceed a UFD escape velocity of ~10 km/s", for an ultra-faint dwarf (UFD) galaxy.
- **Under Scenario A.** When the core-fitting normalization of [Scenario A](/wiki/dark-matter/momentum-clumping/wave-island/scenario-a) "pins g²/m³, hence pins M_crit as a function of m alone", Debt 3c gives the formula below. "This crosses the UFD core mass (~10⁶ M_⊙) at m ≈ 5×10⁻²¹ eV." The −7/4 form holds only under Scenario A. The checkpoint quotes the same scaling with [14]† (#11 §9).

```text
M_crit = 3.6 M_P/(m√g) ≈ 2.9×10⁻³⁰ (m/eV)^{−7/4} M_⊙
```

- **Two branches.** For "m ≳ 10⁻²⁰ eV (the bulk of the wave island): M_crit ≪ M_core — often absurdly so (10⁻⁷ M_⊙ at 10⁻¹³ eV)", and "**the condensate is a mass drain**". For "m ≲ 5×10⁻²¹ eV: M_crit ≳ M_core; the condensate grows as a stable soliton", ordinary fuzzy dark matter with an attractive perturbation, a mass range that [the fuzzy-dark-matter bounds](/wiki/dark-matter/wave-dark-matter/fuzzy-dark-matter-bounds) exclude (Debt 3c).
- **The references.** [14]†: P.-H. Chavanis, "Mass–radius relation of self-gravitating Bose–Einstein condensates with attractive self-interaction," Phys. Rev. D 84, 043531 (2011), arXiv:1103.2050. [13]† includes D. G. Levkov, A. G. Panin, I. I. Tkachev, "Relativistic axions from collapsing Bose stars," Phys. Rev. Lett. 118, 011301 (2017). Both are cited from model memory and await [the † literature battery](/wiki/method/literature-battery).

## Used by

- [Obituary: Scenario A and the ultra-faint-dwarf endpoint](/wiki/dark-matter/momentum-clumping/wave-island/scenario-a) — the bosenova cycle drains the ultra-faint dwarfs.
- [The wave island](/wiki/dark-matter/momentum-clumping/wave-island) — the attractive endpoint of gated condensation.
- [The net theorem](/wiki/dark-matter/momentum-clumping/net-theorem) — "fatal (committed wave)" rests on this endpoint.

## Sources

- `papers/broken-born-checkpoint-v2.md` §9, refs [13]–[14] — the checkpoint's statement and the references
- `notes/debt3b-wave-island.md` 'What pins g? Two scenarios' — the critical mass and its tag
- `notes/debt3c-ufd-endpoint.md` 'The attractive endpoint: criticality and the drain' — the Scenario-A scaling, the bosenova cycle, the two branches
