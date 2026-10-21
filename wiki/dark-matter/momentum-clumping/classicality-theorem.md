---
title: "The classicality theorem and the particle island"
weight: 50
status: alive
description: "Meeting the criterion forces m ≲ 0.1 meV, where N_occ ~ 10²⁰: collective velocity dynamics and classical-particle dark matter exclude each other, so MeV–GeV χ scatters but cannot clump."
provenance: [D]
sources:
  - "notes/debt3a-stream-stability.md 'Corollary'"
  - "notes/debt3a-stream-stability.md 'Consequences for the predictions table'"
  - "papers/broken-born-checkpoint-v2.md §9"
  - "papers/broken-born-checkpoint-v2.md §12"
  - "notes/debt3b-wave-island.md 'Standing results'"
  - "HANDOFF.md §3 row 2"
  - "notes/broken-born-theory.md 'Addendum (v0.2)'"
---

*The classicality theorem says that dark matter coupled strongly enough to clump in velocity must be so light that it behaves as a wave rather than as a collection of separate particles. It follows from the [mean-field criterion](/wiki/dark-matter/momentum-clumping/instability-criterion): at the scattering strength that fits dwarf-galaxy cores, the criterion can be met only for masses below about 0.1 meV, and at such masses about 10²⁰ quanta share each quantum state, which is the regime of a classical wave. The program therefore splits dark matter into two regimes: a particle island, with χ masses of MeV to GeV, where dark matter scatters but cannot clump, and a [wave island](/wiki/dark-matter/momentum-clumping/wave-island) of far lighter masses. The theorem is derived at mean-field level and stands.*

**Status:** Alive — [D] (#11 §9 (i)), derived in `notes/debt3a-stream-stability.md` ("Corollary (the classicality theorem)"). Mean-field level, at fixed σ₀/m. Not machine-checked.

## Key facts

- **Scaling** (3a). "At fixed S ≡ σ₀/m and halo (ρ,σ), the criterion scales as √(πS) ρ/(m^{5/2}σ²)." Setting it to 1 gives, for Milky Way conditions,

  ```text
  m_crit = [√(πS) ρ/σ²]^{2/5} ≈ 10⁻¹³ GeV ~ 0.1 meV
  ```

- **Occupation** (3a; [occupation number](/wiki/dark-matter/wave-dark-matter/occupation-number)). "At that mass the per-mode occupation is N_occ = n λ_dB³ = ρ/(m⁴σ³) ~ 10²⁰ ≫ 1."
- **The theorem** (3a). "By the time the coupling is strong enough for collective behavior, the sector is deep in the wave regime. Collective velocity-space dynamics and classical-particle dark matter are mutually exclusive within this framework. This is a theorem-grade statement at mean-field level, not a benchmark accident." #11 §9: satisfying the criterion "forces m ≲ 0.1 meV, where N_occ ~ 10²⁰ — collective momentum-space behavior and classical particles are mutually exclusive."
- **The particle island** (3a, m_χ ~ MeV–GeV). "Rows 1–2 (exponential cliff, isotropy) survive — they are collisional. Rows 3 (velocity granularity) and 4 (condensed cores / Fornax friction suppression) are withdrawn." 3a sums up the island as cliff-shaped self-interacting dark matter plus Maslov quintessence ([τ quintessence](/wiki/cosmology/dark-energy/tau-quintessence)). Since then the cliff has become a knee (#11 §8; [the scattering law](/wiki/dark-matter/conjugate-matter/scattering-law)); the surviving rows are [the knee](/wiki/predictions/self-interaction-knee) and [isotropy](/wiki/predictions/scattering-isotropy), and the withdrawn ones are [old row 3](/wiki/dark-matter/momentum-clumping/velocity-granularity) and [old row 4](/wiki/dark-matter/momentum-clumping/fornax-friction).
- **Standing result** (3b). "Particle island: cliff (exponential) + isotropy live; no collective phenomena. Fully classical, fully collisional." #11 §12 lists the [χ-particle candidate](/wiki/dark-matter/candidates/chi-particles) with the particle side's handles: "knee at v\*, sharp tail; isotropic scattering".
- **What stays open.** The relic abundance: "The 5.4 : 1 abundance question (polarization-genesis) applies to both" candidates (#11 §12; [polarization-genesis](/wiki/dark-matter/candidates/polarization-genesis)).
- **A word collision.** "Island" here names a mass regime of Debt 3; it is unrelated to the "consistency islands" of the gravity sector ([glossary](/wiki/glossary)).

## Sources

- `notes/debt3a-stream-stability.md` 'Corollary (the classicality theorem)' — the scaling, m_crit, N_occ and the theorem
- `notes/debt3a-stream-stability.md` 'Consequences for the predictions table' — the particle island
- `papers/broken-born-checkpoint-v2.md` §9 (i) — the current statement and its tag; §12 — the χ-particle candidate and the shared abundance question
- `notes/debt3b-wave-island.md` 'Standing results after Chunks A+B' — the particle island's standing
- `HANDOFF.md` §3 row 2 — the artifact summary of 3a
- `notes/broken-born-theory.md` 'Addendum (v0.2)' — the notebook's summary
