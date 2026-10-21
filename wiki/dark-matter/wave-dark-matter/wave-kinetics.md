---
title: "Wave kinetics and Bose-star formation"
weight: 20
status: established
description: "Levkov–Panin–Tkachev kinetic condensation: waves in a halo scatter into low-energy states and form Bose-star cores, with a t^{1/2} slowdown of growth."
provenance: [T]
sources:
  - "notes/debt3b-wave-island.md 'Setup'"
  - "notes/debt3b-wave-island.md 'The rate'"
  - "notes/debt3a-stream-stability.md 'Consequences for the predictions table'"
  - "notes/debt3c-ufd-endpoint.md 'Sharpened input numbers'"
  - "papers/broken-born-checkpoint-v2.md §9"
  - "papers/broken-born-checkpoint-v2.md ref [13]"
---

*Wave kinetics is the theory of how a field made of many waves with random phases relaxes when the waves scatter off one another. In a dark-matter halo made of a very light boson, the waves interact through gravity, and the scattering moves power into the lowest-energy modes faster the more those modes are already occupied; the result is a dense, coherent ground-state core, a Bose star, which forms at the halo's center and then grows. Levkov–Panin–Tkachev (LPT) worked out this kinetic condensation and followed it in simulations. The program's [Debt-3 calculation](/wiki/dark-matter/momentum-clumping) used it as the anchor for a gated version driven by conjugate matter's self-attraction.*

**Status:** Established — [T: LPT] in the [Debt-3 notes](/wiki/history/documents/debt-3-notes), cited as [13]† in [the checkpoint](/wiki/history/documents/checkpoint) — not machine-checked; calibrating the program's gated rate against Levkov–Panin–Tkachev numerics is an open to-do.

## Key facts

- **The mechanism.** For wave dark matter, "relaxation proceeds by wave kinetics — the Boltzmann collision integral with Bose enhancement, rate Γ ~ n σ_scat v × N_occ", where N_occ is the [occupation number](/wiki/dark-matter/wave-dark-matter/occupation-number). The note continues, with DM for dark matter: "This is the mechanism LPT established for gravity (Bose condensation of virialized wave DM into solitons); here the gated contact attraction adds a channel" (`notes/debt3b-wave-island.md`, 'Setup').
- **The anchor.** "The known anchor is Levkov–Panin–Tkachev gravitational Bose condensation (kinetic relaxation with Bose-enhancement factors ∝ N_occ)" (`notes/debt3a-stream-stability.md`).
- **The gravitational rate.** "The gravitational channel Γ_gr ≈ 8πG²ρ²Λ/(m³σ⁶) [T: LPT] always runs" (Debt 3b, 'The rate'); the note does not define Λ. How this floor compares with the gated channel is on [the gated condensation rate](/wiki/dark-matter/momentum-clumping/wave-island/condensation-rate).
- **Growth slows.** The Debt-3 notes cite "the soliton-growth slowdown seen in LPT-type kinetics (t^{1/2} growth, factor ~10²–10³ in effective rate)" (`notes/debt3c-ufd-endpoint.md`, 'Sharpened input numbers').
- **A word with two meanings.** In these notes a "soliton" is a Bose-star core. It is not the topological soliton of the program's retired candidate, for which see [the soliton obituary](/wiki/dark-matter/candidates/soliton-candidate/obituary).
- **The references.** The checkpoint's [13]†: D. G. Levkov, A. G. Panin, I. I. Tkachev, "Gravitational Bose–Einstein condensation in the kinetic regime," Phys. Rev. Lett. 121, 151301 (2018); "Relativistic axions from collapsing Bose stars," Phys. Rev. Lett. 118, 011301 (2017). Both are cited from model memory and await [the † literature battery](/wiki/method/literature-battery).
- **Calibration open.** Debt 3b's coefficients are "heuristic at O(1)–O(10) level; calibration against Levkov–Panin–Tkachev (LPT) numerics is a flagged to-do." [v1](/wiki/history/documents/checkpoint) lists "LPT coefficient calibration" among its literature verifications (`notes/broken-born-program-v1.md` §10 item 8); the checkpoint's open-problem list (#11 §14) does not itemize it.

## Used by

- [The gated condensation rate Γ_self](/wiki/dark-matter/momentum-clumping/wave-island/condensation-rate) — the gated channel added to this mechanism, and the gravitational floor it races.
- [The wave island](/wiki/dark-matter/momentum-clumping/wave-island) — on the island, relaxation is wave-kinetic.
- [Obituary: Scenario A and the ultra-faint-dwarf endpoint](/wiki/dark-matter/momentum-clumping/wave-island/scenario-a) — even with the t^{1/2} slowdown, "There is no timescale refuge."

## Sources

- `papers/broken-born-checkpoint-v2.md` §9, ref [13] — "LPT-style [13†]"; the reference
- `notes/debt3b-wave-island.md` 'Setup', 'The rate' — the wave-kinetic rate, the LPT mechanism, the gravitational channel, the calibration to-do
- `notes/debt3a-stream-stability.md` 'Consequences for the predictions table' — Levkov–Panin–Tkachev as the known anchor
- `notes/debt3c-ufd-endpoint.md` 'Sharpened input numbers' — the t^{1/2} growth slowdown
- `notes/broken-born-program-v1.md` §10 — the calibration listed among literature verifications
