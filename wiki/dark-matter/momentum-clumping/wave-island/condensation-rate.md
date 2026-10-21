---
title: "The gated condensation rate Γ_self"
weight: 10
status: alive
description: "Γ_self ≈ c g²ρ² min(σ, v*)⁴/(m³σ⁶), suppressed by a power law when the gate is narrow, raced against the gravitational floor and orbital stirring; its coefficient awaits calibration against Levkov–Panin–Tkachev."
provenance: [D, T, O]
sources:
  - "notes/debt3b-wave-island.md 'The rate'"
  - "notes/debt3b-wave-island.md 'Setup'"
  - "notes/debt3b-wave-island.md 'What pins g? Two scenarios'"
  - "papers/broken-born-checkpoint-v2.md §9"
  - "notes/debt3a-stream-stability.md 'Consequences for the predictions table'"
  - "notes/broken-born-program-v1.md §7"
  - "notes/broken-born-program-v1.md §10"
---

*Γ_self is the rate at which the gated attraction makes a wave-like dark-matter halo condense, moving its waves' power into a narrow range of low relative momenta. On the [wave island](/wiki/dark-matter/momentum-clumping/wave-island) the halo is an incoherent classical field whose waves scatter off one another, with every rate multiplied by the large number of quanta per mode; Levkov, Panin and Tkachev established this condensation mechanism for gravity, and the gated attraction adds a second channel to it. Once the halo's velocity spread exceeds the gate width, the rate falls off as a power of their ratio rather than exponentially, and Debt 3 races it against the gravitational channel and against orbital stirring. Its form is derived; its numerical coefficient is a heuristic estimate still to be calibrated against Levkov–Panin–Tkachev (LPT) simulations.*

**Status:** Alive, with uncalibrated coefficients — "[D, heuristic coefficients]" in `notes/debt3b-wave-island.md`; in #11 §9 (ii) it is part of the [D + T] wave-island result, "Bose-enhanced, LPT-style [13†]; coefficients [O]". Not machine-checked. The calibration is open (3b; #9 §10 item 8) but not itemized in #11 §14.

## Key facts

- **Mechanism** (3b, Setup; [wave kinetics](/wiki/dark-matter/wave-dark-matter/wave-kinetics)). The halo is an incoherent classical field, and "relaxation proceeds by wave kinetics — the Boltzmann collision integral with Bose enhancement, rate Γ ~ n σ_scat v × N_occ." The gravitational version is the mechanism LPT established, Bose condensation of virialized wave dark matter into "solitons", meaning Bose-star cores here; "the gated contact attraction adds a channel."
- **The rate** (3b, "The rate [D, heuristic coefficients]"), "with peak occupation N_occ ≈ (2π)^{3/2}ρ/(m⁴σ³), scatterer density restricted to the gate, and relative velocities min(σ, v\*)":

  ```text
  Γ_self ≈ c g²ρ² min(σ, v*)⁴ / (m³σ⁶),   c = O(5–15)
  ```

  3b's Setup writes the occupation without the factor (2π)^{3/2}, and the note does not reconcile the two forms ([occupation number](/wiki/dark-matter/wave-dark-matter/occupation-number)).
- **Gate-open and gate-narrow** (3b). "Gate-open (σ ≲ v\*): Γ ≈ c g²ρ²/(m³σ²). Gate-narrow: suppressed by (v\*/σ)⁴ — a power law, not an exponential." 3a's first estimate had (v\*/σ)³; 3b, 3c and #11 use (v\*/σ)⁴, which governs.
- **Corollary 1, the island discriminant** (3b). "The velocity suppression of self-interaction effects is e^{−v²/v\*²} on the particle island but (v\*/σ)⁴ on the wave island. The cliff's sharpness distinguishes the islands observationally." It became [row 3 of the predictions table](/wiki/predictions/island-discriminant).
- **Corollary 2, the gravity floor** (3b, with Milky Way numbers). "The gravitational channel Γ_gr ≈ 8πG²ρ²Λ/(m³σ⁶) [T: LPT] always runs; the gated channel dominates iff g ≳ G√(8πΛ/c)/min(σ,v\*)² ~ 10⁻³¹ GeV⁻²" — "an easy floor". "For m ≫ 10⁻²⁰ eV the gravity channel is negligible on Hubble times." The note does not define Λ.
- **The race** (3b). The rate is compared with orbital stirring, Ω = 1/t_dyn: streams need "Γ_self ≳ Ω", the comparison that replaced the retired "γ vs Ω" framing of [the gated Vlasov model](/wiki/dark-matter/momentum-clumping/gated-vlasov-model). What fixes g has two answers, [Scenario A](/wiki/dark-matter/momentum-clumping/wave-island/scenario-a) and [Scenario B](/wiki/dark-matter/momentum-clumping/wave-island/scenario-b).
- **Open: the calibration.** 3b's header: "Coefficients heuristic at O(1)–O(10) level; calibration against Levkov–Panin–Tkachev (LPT) numerics is a flagged to-do." #9 §10 item 8 lists "LPT coefficient calibration" among its open literature verifications [O]; #11 §14 does not itemize it ([open problems](/wiki/status/open-problems)).
- **Open: rows 1–2 in wave language.** 3a: "Rows 1–2 must be re-derived in wave language (two-body Born scattering is no longer the right observable)." #11 §14 does not itemize this either ([the knee](/wiki/predictions/self-interaction-knee), [isotropy](/wiki/predictions/scattering-isotropy)).

## Sources

- `notes/debt3b-wave-island.md` 'Setup', 'The rate [D, heuristic coefficients]' — the mechanism, the rate, both corollaries, the calibration flag
- `notes/debt3b-wave-island.md` 'What pins g? Two scenarios' — the comparison with Ω = 1/t_dyn
- `papers/broken-born-checkpoint-v2.md` §9 (ii) — the current statement and its tags
- `notes/debt3a-stream-stability.md` 'Consequences for the predictions table' — the first (v\*/σ)³ estimate and the rows 1–2 to-do
- `notes/broken-born-program-v1.md` §7, §10 item 8 — the v1 summary and the calibration as an open item
