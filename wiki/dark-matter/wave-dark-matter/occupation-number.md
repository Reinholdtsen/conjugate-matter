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
  - "papers/broken-born-checkpoint-v2.md §9"
  - "notes/broken-born-theory.md 'Addendum (v0.2, post Debt-3): resolution of open problem 3'"
---

*The occupation number is the average number of particles that share one quantum state, or mode, of a gas. When it is much smaller than one, the particles behave as separate particles; when it is much larger than one, so many quanta share each mode that the gas behaves as a classical wave, in the way that the enormous number of photons per mode in a radio broadcast behaves as an electromagnetic wave. For dark matter it is set by the particle mass, the halo's density and the spread of its velocities, and it equals the number of particles inside a cube whose side is the de Broglie wavelength. In the Broken-Born program it is the quantity that divides the dark-matter question into a [particle island](/wiki/dark-matter/momentum-clumping/classicality-theorem) and a [wave island](/wiki/dark-matter/momentum-clumping/wave-island).*

**Status:** Established — [T] — the standard definition, used in the [Debt-3 notes](/wiki/history/documents/debt-3-notes) without a citation and without a `verify/` script; Debt 3b writes it in two normalizations that no source reconciles.

## Definition [T]

Quantum statistics counts the states of a gas in phase space, the six-dimensional space of positions and momenta: one mode occupies a cell of volume (2πℏ)³. The occupation number is the number of particles per cell.

For dark matter in a halo, write m for the particle mass, ρ for the mass density, n = ρ/m for the number density and σ for the velocity dispersion. The particles' momenta are spread over a range of order mσ, and the de Broglie wavelength that belongs to that spread is λ_dB ~ ℏ/(mσ). The relation is the Fourier one between a waveform and its spectrum: a wave whose spectrum has width mσ stays coherent over a length of order ℏ/(mσ), and no further. A cube of side λ_dB is therefore one cell of phase space, and the occupation number is the number of particles it holds. In units with ℏ = c = 1, the units implicit in the Debt-3 notes' formulas (`notes/debt3a-stream-stability.md`, 'Corollary'):

```text
N_occ = n λ_dB³ = ρ/(m⁴σ³)
```

The second form is the first with n = ρ/m and λ_dB = 1/(mσ) substituted. At fixed density and dispersion the occupation grows as the fourth power of 1/m: light dark matter is crowded into few modes, heavy dark matter is spread thinly over many.

### Two normalizations in Debt 3b

Debt 3b writes the occupation twice. Its 'Setup' uses the "per-mode occupation" ρ/(m⁴σ³), as above. Its rate estimate uses the "peak occupation N_occ ≈ (2π)^{3/2}ρ/(m⁴σ³)" ('The rate'), the occupation at the maximum of the velocity distribution. The two differ by the factor (2π)^{3/2}, and no source reconciles them; [the record of conflicts between sources](/wiki/history/documents/source-conflicts) lists the difference as unresolved.

## Particles or waves [T]

**Few quanta per mode.** When N_occ ≪ 1, each mode holds at most one particle on average. The gas is then a collection of classical particles, described by a distribution f(x, p) over phase space that evolves by the collisionless Boltzmann (Vlasov) equation, with collisions added where the particles scatter ([Vlasov stability](/wiki/dark-matter/momentum-clumping/vlasov-stability)). This is the regime of the program's particle island.

**Many quanta per mode.** When N_occ ≫ 1, the amplitude of the field in each mode is large compared with its quantum uncertainty; the relative size of the quantum fluctuations falls as 1/√N_occ. The quantum field then behaves as a classical field, as the photons of a radio broadcast behave as a classical electromagnetic wave. In a virialized halo the modes have random phases, so the field is a superposition of waves of many momenta: Debt 3b calls it "an incoherent classical field" ('Setup'). Where such waves overlap they interfere, and the density shows granules of size about λ_dB that reshuffle on the time λ_dB/σ. Those granules are what bounds very light dark matter through the heating of stars ([bounds on fuzzy dark matter](/wiki/dark-matter/wave-dark-matter/fuzzy-dark-matter-bounds)).

**Bose enhancement.** For bosons, the rate of scattering into a mode that already holds N quanta is multiplied by 1 + N, the same stimulated-emission factor that operates in a laser. When N_occ ≫ 1 the relaxation of a wave halo is therefore faster than particle collisions alone would make it, by a factor of order N_occ. Debt 3b states this as the mechanism of the wave island: "relaxation proceeds by wave kinetics — the Boltzmann collision integral with Bose enhancement", with rate

```text
Γ ~ n σ_scat v × N_occ
```

(`notes/debt3b-wave-island.md`, 'Setup'). The first factor, n σ_scat v, is the ordinary two-body collision rate of one particle, with σ_scat the scattering cross-section and v the relative speed; the second is the Bose enhancement. How such relaxation builds a coherent core is on [wave kinetics and Bose-star formation](/wiki/dark-matter/wave-dark-matter/wave-kinetics).

## The divide in the program

### The classicality theorem

The program's [Debt 3](/wiki/history/debts) asked whether conjugate matter χ could clump by velocity rather than by position (the [founding image](/wiki/dark-matter/momentum-clumping/founding-image), now dead). Its first chunk found a mean-field [instability criterion](/wiki/dark-matter/momentum-clumping/instability-criterion) for such clumping and then asked at what mass the criterion can be met. Debt 3a holds the self-scattering strength fixed at S ≡ σ₀/m, the cross-section per unit mass that fits dwarf-galaxy cores ([the scattering benchmark](/wiki/dark-matter/conjugate-matter/benchmark)): "At fixed S ≡ σ₀/m and halo (ρ,σ), the criterion scales as √(πS)ρ/(m^{5/2}σ²)". Setting it to 1 gives

```text
m_crit = [√(πS)ρ/σ²]^{2/5} ≈ 10⁻¹³ GeV ~ 0.1 meV        (Milky Way conditions)
```

and at that mass "the per-mode occupation is N_occ = n λ_dB³ = ρ/(m⁴σ³) ~ 10²⁰ ≫ 1" (Debt 3a, 'Corollary'). The note's conclusion: "By the time the coupling is strong enough for collective behavior, the sector is deep in the wave regime." Collective velocity-space dynamics and classical-particle dark matter exclude each other, which Debt 3a calls "a theorem-grade statement at mean-field level, not a benchmark accident". [The checkpoint](/wiki/history/documents/checkpoint) states it as the classicality theorem, tagged [D]: "satisfying the criterion at fixed σ₀/m forces m ≲ 0.1 meV, where N_occ ~ 10²⁰" (#11 §9). [The lab notebook](/wiki/history/documents/lab-notebook)'s addendum v0.2 puts it in terms of this page: "collective momentum-space behavior requires N_occ≫1 — it exists only for wave dark matter". The derivation and its scope are on [the classicality theorem and the particle island](/wiki/dark-matter/momentum-clumping/classicality-theorem).

The symbol m_crit, a mass, is the threshold of this theorem. It is a different quantity from M_crit, the largest stable mass of an attractive condensate ([attractive condensates](/wiki/dark-matter/wave-dark-matter/attractive-condensates)).

### Two islands

Debt 3a splits the mass range of χ into a "**Particle island** (m_χ ~ MeV–GeV)", where χ is a gas of classical particles that scatters but cannot clump, and a "**Wave island** (m_χ ≲ meV, N_occ≫1)", where "the collective sector is reborn in field language" ('Consequences for the predictions table'). The wave island's upper edge is stated three ways in the record: ≲ meV in Debt 3a, "m ≲ 0.1 meV" in Debt 3b ('Setup'), and 10⁻⁴ eV in Debt 3c and the lab notebook's addendum v0.2. Debt 3c's final range is the one the wiki follows: "The surviving wave island is roughly 3×10⁻¹⁹ eV ≲ m ≲ 10⁻⁴ eV with Scenario-B couplings" ('Verdict and closure of Debt 3'). Its lower edge comes from the [bounds on fuzzy dark matter](/wiki/dark-matter/wave-dark-matter/fuzzy-dark-matter-bounds); the coupling condition is [Scenario B](/wiki/dark-matter/momentum-clumping/wave-island/scenario-b).

On the wave island the program's two-body scattering law is no longer the right observable: Debt 3a notes that "Rows 1–2 must be re-derived in wave language (two-body Born scattering is no longer the right observable)". That to-do is recorded on [the gated condensation rate](/wiki/dark-matter/momentum-clumping/wave-island/condensation-rate).

## References

The Debt-3 notes cite no source for the occupation number. Added by the wiki from model memory (†):

- W. Hu, R. Barkana, A. Gruzinov, "Fuzzy cold dark matter," Phys. Rev. Lett. (2000)†: dark matter as an ultralight wave field.
- L. Hui, J. P. Ostriker, S. Tremaine, E. Witten, "Ultralight scalars as cosmological dark matter," Phys. Rev. D (2017)†: the wave regime, granules and their dynamical effects.
- L. Hui, "Wave dark matter," Annu. Rev. Astron. Astrophys. (2021)†: a review.

## Used by

- [The classicality theorem and the particle island](/wiki/dark-matter/momentum-clumping/classicality-theorem) — collective behavior requires N_occ ≫ 1, so it exists only for wave dark matter.
- [The wave island](/wiki/dark-matter/momentum-clumping/wave-island) — defined by N_occ ≫ 1.
- [The gated condensation rate Γ_self](/wiki/dark-matter/momentum-clumping/wave-island/condensation-rate) — Bose enhancement by N_occ sets the rate.

## Sources

- `papers/broken-born-checkpoint-v2.md` §9 — the classicality theorem as the checkpoint states it
- `notes/debt3a-stream-stability.md` 'Corollary (the classicality theorem)', 'Consequences for the predictions table' — the definition, the scaling of the criterion, m_crit and the 10²⁰ occupation; the particle and wave islands; rows 1–2 in wave language
- `notes/debt3b-wave-island.md` 'Setup', 'The rate' — Bose-enhanced wave kinetics; the per-mode and peak normalizations
- `notes/debt3c-ufd-endpoint.md` 'Verdict and closure of Debt 3' — the final range of the wave island
- `notes/broken-born-theory.md` 'Addendum (v0.2, post Debt-3): resolution of open problem 3' — the theorem in terms of N_occ; the island range
