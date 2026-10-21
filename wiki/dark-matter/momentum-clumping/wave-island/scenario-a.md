---
title: "Obituary: Scenario A and the ultra-faint-dwarf endpoint"
weight: 20
status: dead
description: "If the gated channel makes the cores, condensation is mandatory in ultra-faint dwarfs, whose condensates would cycle through bosenovas and drain the halo; Segue 1 is intact and the light-mass escape is closed, so no parameter direction rescues it."
provenance: [D, T]
sources:
  - "notes/debt3b-wave-island.md 'What pins g? Two scenarios'"
  - "notes/debt3c-ufd-endpoint.md 'The question'"
  - "notes/debt3c-ufd-endpoint.md 'Sharpened input numbers'"
  - "notes/debt3c-ufd-endpoint.md 'The attractive endpoint'"
  - "notes/debt3c-ufd-endpoint.md 'The data'"
  - "notes/debt3c-ufd-endpoint.md 'Verdict and closure'"
  - "papers/broken-born-checkpoint-v2.md §9"
  - "HANDOFF.md §2"
  - "notes/broken-born-theory.md 'Addendum (v0.2)'"
---

*Scenario A was the assumption that, on the [wave island](/wiki/dark-matter/momentum-clumping/wave-island), the gated attraction that condenses dark matter is also what smooths the cores of ordinary dwarf galaxies. Fitting those cores fixes the coupling, and with the coupling fixed, condensation becomes mandatory and halo-wide in ultra-faint dwarf galaxies, the faintest and densest galaxies known. Because the attraction makes a condensate collapse each time it passes a critical mass, throwing off fast waves that escape, these galaxies would by now have lost much of their dark matter; instead they are the most dark-matter-dominated systems observed, and Segue 1 holds a dense, intact halo around stars about 13 billion years old. The escape to a much lighter mass is excluded by other observations, and no other change of parameters rescues the scenario, so Scenario A is dead.*

**Status:** Dead — "Scenario A is falsified by the existence of ultra-faint dwarfs" (`notes/debt3c-ufd-endpoint.md`); #11 §9 (ii), tagged [D + T], records its endpoint as "falsified by observed UFD density and longevity". Not machine-checked, and the Segue 1 inputs carry no reference in any source document. Listed in [the graveyard](/wiki/status/graveyard).

## Key facts

- **The assumption** (3b), by analogy with [self-interacting dark matter](/wiki/dark-matter/halo-astrophysics/self-interacting-dark-matter) (SIDM). "On the wave island, Γ_self is the analog of SIDM heat transport (kinetic relaxation redistributes energy through the halo). Fitting classical-dwarf cores means Γ_self(dwarf) · t_age = κ ~ 1, which spends g²/m³. Streams need the much harder Γ_self ≳ Ω = 1/t_dyn." ([The gated condensation rate](/wiki/dark-matter/momentum-clumping/wave-island/condensation-rate).)
- **Where it bites** (3b). Eliminating g²/m³ gives the stream-to-stirring ratio, where X labels an environment, not the momentum graviton:

  ```text
  R_X ≡ Γ_self(X)/Ω_X = κ (t_dyn,X/t_age) (ρ_X/ρ_d)² (σ_d/σ_X)² (min(σ_X, v*)/σ_X)⁴
  ```

  "Verdict A: streams lose everywhere by 10²–10⁴ — except ultra-faint dwarfs, where ρ²/σ² leverage wins by ~40." The predicted signature was "anomalous central objects, density spikes, or disruption signatures in ultra-faint dwarfs", which 3b called "the surviving descendant of old rows 3–4".
- **Segue 1** (3c; [dwarf galaxies](/wiki/dark-matter/halo-astrophysics/dwarf-galaxies)). "M(< 38 pc) ≈ 6×10⁵ M_⊙ ⇒ mean core density ρ ≈ 100 GeV/cm³ (not the conservative 20 used in 3b), σ ≈ 3.7 km/s, t_dyn ≈ 10 Myr", so R_Segue 1 ≈ 10⁻³·10⁴·66 ≈ 660 and "Condensation time τ_cond = t_dyn/R ≈ 1.5×10⁴ yr. Over a 10 Gyr lifetime the system has ~6×10⁵ condensation times." Even granting the t^{1/2} growth slowdown of Levkov–Panin–Tkachev (LPT) kinetics, "There is no timescale refuge." #11 rounds the time to "~10⁴ yr".
- **The critical mass** (3c; [attractive condensates](/wiki/dark-matter/wave-dark-matter/attractive-condensates)). Under the Scenario-A normalization, which "pins M_crit as a function of m alone",

  ```text
  M_crit = 3.6 M_P/(m√g) ≈ 2.9×10⁻³⁰ (m/eV)^(−7/4) M_⊙
  ```

  The bound is "[T: dilute-boson-star bound, Chavanis-type]" (3b; #11 cites [14†]). "This crosses the UFD core mass (~10⁶ M_⊙) at m ≈ 5×10⁻²¹ eV."
- **Branch (i), m ≳ 10⁻²⁰ eV, "the bulk of the wave island"** (3c). M_crit ≪ M_core, "often absurdly so (10⁻⁷ M_⊙ at 10⁻¹³ eV)". The condensate cycles "grow to M_crit → collapse → eject an O(0.1–1) fraction as fast/relativistic waves (bosenova; LPT 2017-type result [T]) → remnant regrows", and the ejecta far exceed "a UFD escape velocity of ~10 km/s: the condensate is a mass drain", "unlike SIDM, where relaxation is elastic and mass stays." "Prediction of Branch (i): UFDs today should be low-density, inflated, or gone."
- **Branch (ii), m ≲ 5×10⁻²¹ eV** (3c). M_crit ≳ M_core and "the condensate grows as a stable soliton", as in ordinary fuzzy dark matter, but ultra-faint-dwarf sizes and stellar kinematics ("Dalal & Kravtsov 2022 [T — bound ≈ 3×10⁻¹⁹ eV; verify exact figure before publication]") and Lyman-α forest limits already exclude wave dark matter this light. #11: "the light-mass escape is closed independently [15†, Lyman-α]"; no source gives a reference for the Lyman-α limit ([bounds on fuzzy dark matter](/wiki/dark-matter/wave-dark-matter/fuzzy-dark-matter-bounds)).
- **The data and the verdict** (3c). Segue 1 "has M/L ~ 10³ and a ~13 Gyr stellar population sitting in an intact, dense halo. Branch (i) predicts the opposite of what is observed; Branch (ii) is excluded before we arrive. Robustness checks: shrinking v\* makes it worse (σ⁻⁶ leverage boosts R to ~10⁵); growing v\* leaves R unchanged; κ < 1 is by definition Scenario B. No parameter direction rescues it." The handoff's summary: "ultra-faint dwarfs would be drained; Segue 1 intact".
- **What it took with it.** With Scenario A dead, the old rows 3 and 4 are "permanently withdrawn, on both islands" (3c; [old row 3](/wiki/dark-matter/momentum-clumping/velocity-granularity), [old row 4](/wiki/dark-matter/momentum-clumping/fornax-friction)), and the wave island keeps only [Scenario B](/wiki/dark-matter/momentum-clumping/wave-island/scenario-b), which completes the [net theorem](/wiki/dark-matter/momentum-clumping/net-theorem).

## Sources

- `notes/debt3c-ufd-endpoint.md` 'The question', 'Sharpened input numbers', 'The attractive endpoint: criticality and the drain', 'The data', 'Verdict and closure of Debt 3' — the falsification
- `notes/debt3b-wave-island.md` 'What pins g? Two scenarios' — Scenario A, R_X and the ultra-faint-dwarf signature
- `papers/broken-born-checkpoint-v2.md` §9 (ii) — the current statement, its tags and the references [14†], [15†]
- `HANDOFF.md` §2 — the handoff's summary of the kill
- `notes/broken-born-theory.md` 'Addendum (v0.2)' — the notebook's record
