---
title: "τ: hilltop quintessence on the Maslov circle"
weight: 40
status: alive
description: "S_τ with V = V₀[1 + cos(τ/f)]: τ sits near the hilltop and thaws (w₀ > −1, wₐ < 0) along the corridor wₐ ≈ −1.5(1 + w₀); the toy models show consistency only."
provenance: [D, T]
sources:
  - "papers/broken-born-checkpoint-v2.md §10"
  - "papers/broken-born-checkpoint-v2.md §6"
  - "papers/broken-born-checkpoint-v2.md §7.3"
  - "papers/broken-born-checkpoint-v2.md §7.5"
  - "notes/broken-born-theory.md §3"
  - "notes/broken-born-theory.md §7"
  - "notes/broken-born-program-v1.md §8"
  - "notes/debt1a-iv-beta-coefficients.md §2"
  - "papers/reciprocity-toy-models.md §6"
  - "HANDOFF.md §2"
  - "CLAUDE.md 'Since the handoff'"
---

*The program identifies dark energy with τ, the angle that sets how the vacuum divides phase space into position and momentum. Because τ is an angle, its potential energy must repeat when τ goes once around its circle, and the program writes it as a cosine, V = V₀[1 + cos(τ/f)]. Today τ is taken to sit near the top of that potential, where its energy is almost all potential energy and it acts almost like a cosmological constant, while drifting slowly away from the top, so that dark energy weakens over time. Thawing hilltop quintessence of this kind is an established class of models; the program's contribution is the identification of the field, which the popular article calls "the angle of the mirror", and the claim stands under pressure from the latest survey data.*

**Status:** Alive, under pressure — [D + T] (#11 §10); the toy-model support is [D][V] and shows consistency only — no `verify/` script tests the cosmology; the pressure comes from Data Release 2 (DR2) of the Dark Energy Spectroscopic Instrument (DESI), per the root `CLAUDE.md`.

## Key facts

- **The action.** #1 §3 writes S_τ = ∫√−g[½(∂τ)² − V(τ)] with V(τ) = V₀[1 + cos(τ/f)]. "The potential's *periodicity* is forced by the Maslov topology **[D]**"; its existence was attributed to explicit breaking by the rigid ω of the original P2, and "Its *magnitude* V₀ is a free parameter here. **[P/O]**" #9 §8 fixes V₀ by Ω_DE. Where the potential comes from is now open: [Open: the origin of the ρ-preserving potential](/wiki/symmetry-breaking/rho-preserving-potential).
- **The identification.** #11 §10: "τ is hilltop quintessence on the Maslov circle, V = V₀[1 + cos(τ/f)], periodicity by topology". τ is the Maslov phase of the boundary of the Siegel domain (#11 §6; [τ as the Maslov phase of the boundary](/wiki/phase-space/modular-field/maslov-phase)), and it survives the momentum graviton's Higgs mechanism: "τ un-eaten (compact J-sector, not the Stückelberg sector)" (#11 §7.5; [τ is not eaten](/wiki/gravity/momentum-graviton/tau-not-eaten)).
- **Thawing [T].** #1 §7 item 2: "Hilltop initial conditions give w ≈ −1 in the past, rising now: w₀ > −1, wₐ < 0, on the standard thawing corridor wₐ ≈ −1.5(1 + w₀)." The general physics is on [quintessence and the equation of state](/wiki/cosmology/dark-energy/quintessence).
- **No competing vacuum energy.** "§7.3 guarantees the wedge sector contributes nothing that competes with τ" (#11 §10). Calc note #8: "The massive-gravity sector contributes *nothing* to the cosmological constant; dark energy is left entirely to the τ sector" (§2). The scope is limited, since the identity "does **not** by itself address matter-loop vacuum energy" (#11 §7.3). See [the vacuum-energy identity](/wiki/gravity/palindromic-branch/vacuum-energy-identity) and [the cosmological-constant problem](/wiki/gravity/spin-2-fields/cosmological-constant-problem).
- **The fits.** #11 §10: "compelling evidence for weakening dark energy with phantom behavior less significant (non-phantom compatible at ~2σ) and high posterior preference for a future anti-de Sitter transition and collapse in negative-minimum quintessence fits [19S, 20S, 21S]".
- **The pressure.** DESI DR2 favours a crossing below w = −1 above z ≈ 0.4, against the strict w ≥ −1 that τ requires; "The dark-energy sector is under real pressure ahead of DR3" (root `CLAUDE.md`), DR3 being Data Release 3. See [DESI DR2's phantom crossing](/wiki/cosmology/dark-energy/desi-dr2-phantom-crossing) and [the no-phantom bound w ≥ −1](/wiki/cosmology/dark-energy/no-phantom-bound).
- **Toy models: consistency only.** #11 §10 (v2.2) [D][V]: in the coset model ρ sits inside a continuous U(1), and "In the coset model that angle parametrizes Λ(1): it is τ's circle." Then: "None of this tests the cosmology; it only shows the structure is consistent." The toy-model note agrees: "Motivation, not result" (`papers/reciprocity-toy-models.md` §6). The checks are [the toy-model scripts](/wiki/method/verification/toy-model-scripts); see [the polarization as a Goldstone angle](/wiki/symmetry-breaking/goldstone-angle).
- **Tests and loose ends.** The test is [row 4: thawing dark energy, never phantom](/wiki/predictions/dark-energy-drift); the parameter count is [the dark-energy over-constraint](/wiki/cosmology/dark-energy/over-constraint); safety from extra forces is [fifth-force safety of τ](/wiki/cosmology/dark-energy/tau-fifth-force). Open: τ's mixing with the momentum graviton's eaten modes ([τ–Stückelberg mixing, open problem 6](/wiki/gravity/momentum-graviton/tau-stuckelberg-mixing)); whether its potential can go negative ([the sign of V(τ)](/wiki/cosmology/dark-energy/potential-sign)); and how the dictionary's motivation leads to τ ([dual kinetic energy versus τ's potential](/wiki/cosmology/scale-factor-duality/dual-kinetic-link)).

## Sources

- `papers/broken-born-checkpoint-v2.md` §10 — the identification, its tag, the fits, the pressure from DR2, the toy-model support and its limit
- `papers/broken-born-checkpoint-v2.md` §6, §7.3, §7.5 — τ as the Maslov phase; the wedge sector's zero vacuum energy and its scope; τ un-eaten
- `notes/broken-born-theory.md` §3 — the action S_τ, the potential and its v0.1 tags
- `notes/broken-born-theory.md` §7 item 2 — hilltop thawing and the corridor
- `notes/broken-born-program-v1.md` §8 — V₀ fixed by Ω_DE
- `notes/debt1a-iv-beta-coefficients.md` §2 — dark energy left entirely to the τ sector
- `papers/reciprocity-toy-models.md` §6 — "Motivation, not result"
- `HANDOFF.md` §2 — τ among the live results
- `CLAUDE.md` 'Since the handoff' — "under real pressure ahead of DR3"
