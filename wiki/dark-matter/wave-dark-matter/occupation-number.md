---
title: "Occupation number: particles or waves"
weight: 10
status: established
description: "N_occ = ρ/(m⁴σ³), the number of quanta per mode: N_occ ≫ 1 means a classical wave and Bose-enhanced rates; the de Broglie wavelength sets the divide."
provenance: [T]
sources:
  - "notes/debt3a-stream-stability.md 'Corollary (the classicality theorem)'"
  - "notes/debt3a-stream-stability.md 'Consequences for the predictions table'"
  - "notes/debt3b-wave-island.md 'Setup'"
  - "notes/debt3b-wave-island.md 'The rate'"
  - "notes/debt3c-ufd-endpoint.md 'Verdict and closure of Debt 3'"
---

*The occupation number is the average number of particles that share one quantum state, or mode, of a gas. When it is much smaller than one, the particles behave as separate particles; when it is much larger than one, so many quanta share each mode that the gas behaves as a classical wave, in the way that the enormous number of photons per mode in a radio broadcast behaves as an electromagnetic wave. For dark matter it depends on the particle mass, the halo's density and the spread of its velocities. In the program it is the quantity that divides the dark-matter question into a [particle island](/wiki/dark-matter/momentum-clumping/classicality-theorem) and a [wave island](/wiki/dark-matter/momentum-clumping/wave-island).*

**Status:** Established — [T] — the standard definition, used in the [Debt-3 notes](/wiki/history/documents/debt-3-notes) without a citation and without a `verify/` script; Debt 3b writes it in two normalizations that no source reconciles.

## Key facts

- **Definition.** For particle mass m, mass density ρ, number density n and velocity dispersion σ, with λ_dB the de Broglie wavelength (`notes/debt3a-stream-stability.md`, 'Corollary'):

```text
N_occ = n λ_dB³ = ρ/(m⁴σ³)
```

- **A second normalization.** Debt 3b also writes the "peak occupation N_occ ≈ (2π)^{3/2}ρ/(m⁴σ³)" ('The rate'). The two forms differ by the factor (2π)^{3/2}, and no source reconciles them.
- **Waves and Bose enhancement.** "Wave island: m ≲ 0.1 meV, per-mode occupation N_occ = ρ/(m⁴σ³) ≫ 1. The halo is an incoherent classical field; relaxation proceeds by wave kinetics — the Boltzmann collision integral with Bose enhancement, rate Γ ~ n σ_scat v × N_occ" (Debt 3b, 'Setup'). Scattering into a mode that already holds N_occ quanta is faster by that factor [T]; see [wave kinetics](/wiki/dark-matter/wave-dark-matter/wave-kinetics).
- **The classicality theorem's number.** At fixed S ≡ σ₀/m, collective velocity-space behavior needs masses below "m_crit = [√(πS)ρ/σ²]^{2/5} ≈ 10⁻¹³ GeV ~ 0.1 meV" for Milky Way conditions, where the occupation is "N_occ … ~ 10²⁰ ≫ 1": "By the time the coupling is strong enough for collective behavior, the sector is deep in the wave regime" (Debt 3a). See [the classicality theorem](/wiki/dark-matter/momentum-clumping/classicality-theorem).
- **The divide in the program.** Debt 3a splits the χ mass range into a "**Particle island** (m_χ ~ MeV–GeV)" and a "**Wave island** (m_χ ≲ meV, N_occ ≫ 1)". The wave island's upper edge differs between the notes (≲ meV in 3a, ≲ 0.1 meV in 3b); Debt 3c's final range is "roughly 3×10⁻¹⁹ eV ≲ m ≲ 10⁻⁴ eV with Scenario-B couplings".

## Used by

- [The classicality theorem and the particle island](/wiki/dark-matter/momentum-clumping/classicality-theorem) — collective behavior requires N_occ ≫ 1, so it exists only for wave dark matter.
- [The wave island](/wiki/dark-matter/momentum-clumping/wave-island) — defined by N_occ ≫ 1.
- [The gated condensation rate Γ_self](/wiki/dark-matter/momentum-clumping/wave-island/condensation-rate) — Bose enhancement by N_occ sets the rate.

## Sources

- `notes/debt3a-stream-stability.md` 'Corollary (the classicality theorem)', 'Consequences for the predictions table' — the definition, the 10²⁰ occupation at m_crit, the particle and wave islands
- `notes/debt3b-wave-island.md` 'Setup', 'The rate' — Bose-enhanced wave kinetics; the second normalization
- `notes/debt3c-ufd-endpoint.md` 'Verdict and closure of Debt 3' — the final range of the wave island
