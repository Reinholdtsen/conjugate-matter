---
title: "The classicality theorem and the particle island"
weight: 50
status: alive
description: "Meeting the criterion forces m ≲ 0.1 meV, where N_occ ~ 10²⁰: collective velocity dynamics and classical-particle dark matter exclude each other, so MeV–GeV χ scatters but cannot clump."
provenance: [D]
sources:
  - "notes/debt3a-stream-stability.md 'Corollary'"
  - "notes/debt3a-stream-stability.md 'Consequences for the predictions table'"
  - "notes/debt3a-stream-stability.md 'Setup'"
  - "papers/broken-born-checkpoint-v2.md §9"
  - "papers/broken-born-checkpoint-v2.md §12"
  - "papers/broken-born-checkpoint-v2.md §8"
  - "notes/debt3b-wave-island.md 'Setup'"
  - "notes/debt3b-wave-island.md 'The rate'"
  - "notes/debt3b-wave-island.md 'Standing results'"
  - "notes/debt3c-ufd-endpoint.md 'Verdict and closure'"
  - "notes/broken-born-program-v1.md §7"
  - "HANDOFF.md §3 row 2"
  - "notes/broken-born-theory.md 'Addendum (v0.2)'"
  - "notes/broken-born-theory.md §5.3"
  - "review/wiki-build-flags.md item 19"
---

*The classicality theorem says that dark matter coupled strongly enough to clump in velocity must be so light that it behaves as a wave, not as a collection of separate particles. It follows from the [mean-field criterion](/wiki/dark-matter/momentum-clumping/instability-criterion): at the scattering strength that fits dwarf-galaxy cores, the criterion can be met only for masses below about 0.1 meV, and at such masses about 10²⁰ quanta share each quantum state, which is the regime of a classical wave. The program therefore splits dark matter into two regimes: a particle island, with χ masses of MeV to GeV, where dark matter scatters but cannot clump, and a [wave island](/wiki/dark-matter/momentum-clumping/wave-island) of far lighter masses. The theorem is derived at mean-field level and stands.*

**Status:** Alive — [D] ([#11](/wiki/history/documents/checkpoint) §9 (i)), derived in `notes/debt3a-stream-stability.md` ("Corollary (the classicality theorem)"). Mean-field level, at fixed σ₀/m. Not machine-checked: no `verify/` script covers any [Debt-3](/wiki/history/debts) number.

## Statement

[3a](/wiki/history/documents/debt-3-notes), 'Corollary (the classicality theorem)':

> By the time the coupling is strong enough for collective behavior, the sector is deep in the wave regime. Collective velocity-space dynamics and classical-particle dark matter are mutually exclusive within this framework. This is a theorem-grade statement at mean-field level, not a benchmark accident.

#11 §9 (i), tagged [D]: "**Classicality theorem:** satisfying the criterion at fixed σ₀/m forces m ≲ 0.1 meV, where N_occ ~ 10²⁰ — collective momentum-space behavior and classical particles are mutually exclusive." The [lab notebook](/wiki/history/documents/lab-notebook)'s addendum puts it in one line: "collective momentum-space behavior requires N_occ ≫ 1 — it exists only for wave dark matter" (`notes/broken-born-theory.md`, 'Addendum (v0.2)').

"Theorem" and "theorem-grade" are the sources' words. The argument is a scaling argument at mean-field level, and its premises are listed under [Scope](#scope).

## The argument

The argument has three steps: how the stream criterion depends on the particle mass when the scattering strength is held fixed; the mass at which the criterion is met; and the [occupation number](/wiki/dark-matter/wave-dark-matter/occupation-number) at that mass.

### Step 1: the criterion grows as the mass falls

Write S ≡ σ₀/m for the cross-section per unit mass, the quantity that dwarf-core fits constrain ([the scattering benchmark](/wiki/dark-matter/conjugate-matter/benchmark)). 3a: "At fixed S ≡ σ₀/m and halo (ρ,σ), the criterion scales as √(πS) ρ/(m^{5/2}σ²)."

The note states the scaling without the intermediate line. The substitution below is the wiki's reading, not printed in the note. It starts from the broad-gate form of the criterion, g n/(mσ²), takes the model's definition g = √(πσ₀/m²) ([the gated Vlasov model](/wiki/dark-matter/momentum-clumping/gated-vlasov-model)), and writes σ₀ = Sm and n = ρ/m:

```text
g = √(πS m)/m = √(πS) m^{−1/2},    n = ρ/m
g n/(mσ²) = √(πS) ρ/(m^{5/2} σ²)
```

At fixed S and fixed halo density ρ and dispersion σ, a lighter particle helps the criterion in two ways: the coupling per particle g grows as m^{−1/2}, and the number of particles in a given mass density grows as 1/m. Together with the m in the kinetic energy mσ², the criterion grows as m^{−5/2}.

### Step 2: the critical mass

Setting the criterion equal to 1 gives the mass below which streams could form (3a):

```text
m_crit = [√(πS) ρ/σ²]^{2/5} ≈ 10⁻¹³ GeV ~ 0.1 meV      (Milky Way conditions)
```

The scaling is the broad-gate form of the criterion, evaluated at Milky Way conditions; see [Scope](#scope) and flag 19 in `review/wiki-build-flags.md`. At the benchmark mass m_χ = 70 MeV the criterion falls short by 10²⁸–10³¹ ([the mean-field criterion](/wiki/dark-matter/momentum-clumping/instability-criterion)); lowering the mass at fixed S closes the gap only at m_crit.

### Step 3: the occupation number at that mass

The occupation number counts how many particles share one quantum state: the number of particles in a cube one de Broglie wavelength on a side. 3a: "At that mass the per-mode occupation is"

```text
N_occ = n λ_dB³ = ρ/(m⁴σ³) ~ 10²⁰ ≫ 1
```

In the natural units of the notes (ħ = 1), the notes take λ_dB = 1/(mσ), the de Broglie wavelength ħ/(mσ) of a particle moving at speed σ up to factors of 2π, and the number density is n = ρ/m, which gives the second form [T]. The occupation grows as m⁻⁴: a lighter particle means both more particles in a given mass density and a longer wavelength for each.

When N_occ ≫ 1, the particles are described as a classical wave field, in the way that a radio wave is a classical field although it consists of photons: the field's amplitude and phase are well defined, and individual quanta play no role [T]. A classical phase-space gas, the description in which the criterion was derived, does not apply.

### The conclusion

At fixed S and in a given halo, the criterion can be met only by lowering m, and lowering m drives N_occ up as m⁻⁴, faster than the criterion's m^{−5/2}. By the time the criterion reaches 1, the dark matter is a wave with about 10²⁰ quanta per state (3a). The particle picture and collective velocity-space dynamics therefore never meet within the framework at mean-field level. The note does not spell out "not a benchmark accident". On the wiki's reading, it refers to m_crit depending on S and on the halo's ρ and σ but not on the benchmark mass of 70 MeV, so the conclusion does not hinge on the choice of χ mass. The faster growth of N_occ does not by itself guarantee N_occ ≫ 1 at m_crit; the margin, N_occ ~ 10²⁰, is computed for Milky Way conditions at the benchmark value of S.

## The particle island

The theorem splits the mass range in two. The particle island is the classical side. 3a, 'Consequences for the predictions table':

> **Particle island** (m_χ ~ MeV–GeV): Rows 1–2 (exponential cliff, isotropy) **survive** — they are collisional. Rows 3 (velocity granularity) and 4 (condensed cores / Fornax friction suppression) are **withdrawn**, and with them the mechanism-level linkage claimed between them. On this island BBT is cliff-shaped SIDM plus Maslov quintessence.

Here BBT is the Broken-Born framework and SIDM is [self-interacting dark matter](/wiki/dark-matter/halo-astrophysics/self-interacting-dark-matter). The rows are those of the lab notebook's [prediction table](/wiki/predictions/table-history). Rows 1 and 2, the velocity dependence of the scattering cross-section and the isotropy of scattering inside the [velocity gate](/wiki/dark-matter/conjugate-matter/velocity-gate), are about two-body collisions, which need no collective instability; that is the sense of "they are collisional". Rows 3 and 4 needed the instability and are withdrawn: [old row 3](/wiki/dark-matter/momentum-clumping/velocity-granularity), velocity-space granularity, and [old row 4](/wiki/dark-matter/momentum-clumping/fornax-friction), condensed cores and Fornax friction suppression. "Maslov quintessence" is the program's dark-energy field ([τ quintessence](/wiki/cosmology/dark-energy/tau-quintessence)).

3b's standing result after the first two notes: "Particle island: cliff (exponential) + isotropy live; no collective phenomena. Fully classical, fully collisional." (3b, 'Standing results after Chunks A+B'). 3c lists the same pair among the survivors: "the exponential cliff + in-gate isotropy (particle island)".

**Since then.** The "cliff" of the notes, a Gaussian cut-off e^{−v²/v\*²} of the cross-section above v\*, has become a knee whose tail is open (#11 §8; [the scattering law](/wiki/dark-matter/conjugate-matter/scattering-law)). The surviving rows are now [row 1, the knee](/wiki/predictions/self-interaction-knee), and [row 2, isotropy](/wiki/predictions/scattering-isotropy). The particle island is the home of the [χ-particle candidate](/wiki/dark-matter/candidates/chi-particles); #11 §12 lists its handles as "knee at v\*, sharp tail; isotropic scattering; permanent direct-detection null". The particle side of [the island discriminant](/wiki/predictions/island-discriminant), the sharp knee, is this island's signature.

## The wave island

The other side of the theorem is the range of very light masses, where N_occ ≫ 1 and dark matter is a wave. 3a: "**Wave island** (m_χ ≲ meV, N_occ ≫ 1): the collective sector is reborn in field language. The halo is an incoherent wave field; the gated attraction drives condensation in k-space — power flowing into narrow-momentum streams". Its treatment needs [wave kinetics](/wiki/dark-matter/wave-dark-matter/wave-kinetics) rather than [the Vlasov equation](/wiki/dark-matter/momentum-clumping/vlasov-stability), and it has its own section: [the wave island](/wiki/dark-matter/momentum-clumping/wave-island).

The island's upper edge is written differently in the three notes: "m_χ ≲ meV" (3a), "m ≲ 0.1 meV" (3b, Setup), and 10⁻⁴ eV in 3c's final range, "roughly 3×10⁻¹⁹ eV ≲ m ≲ 10⁻⁴ eV with Scenario-B couplings". 3c's range closed Debt 3 and is the one this wiki uses.

## Scope

- **Mean-field level.** The theorem rests on the mean-field criterion, which is itself bracketed by two limits rather than solved in general ([the gated Vlasov model](/wiki/dark-matter/momentum-clumping/gated-vlasov-model)).
- **Fixed σ₀/m.** The scaling holds the cross-section per unit mass at its dwarf-core value; #11 §9 states the premise as "at fixed σ₀/m". On the wave island the question becomes a [condensation rate](/wiki/dark-matter/momentum-clumping/wave-island/condensation-rate) instead of this criterion, and under [Scenario B](/wiki/dark-matter/momentum-clumping/wave-island/scenario-b) the coupling is free instead of fixed.
- **Milky Way conditions** for the number m_crit ≈ 10⁻¹³ GeV. The scaling has the broad-gate form, with σ² in the denominator, while 3a's Limit 2 places the Milky Way in the narrow-gate regime and its benchmark table evaluates the Milky Way row with v\*; the note does not discuss the difference. Flag 19 in `review/wiki-build-flags.md` records it and notes that N_occ ≫ 1 either way, so the conclusion is unchanged.
- **Two normalizations of N_occ.** 3a writes N_occ = ρ/(m⁴σ³), and 3b's Setup does the same, but 3b's rate formula uses a "peak occupation N_occ ≈ (2π)^{3/2}ρ/(m⁴σ³)". The notes do not reconcile the two; at 10²⁰ ≫ 1 the factor does not affect the conclusion.

## What stays open

- **The [relic abundance](/wiki/dark-matter/candidates/relic-abundance)** on the particle island. The wave island obtains its abundance from [misalignment](/wiki/dark-matter/momentum-clumping/wave-island/misalignment-relic). The particle island has no such route: the lab notebook states that this sector "cannot freeze out thermally without cannibalism problems" and assigns the abundance to [polarization-genesis](/wiki/dark-matter/candidates/polarization-genesis) [O] (`notes/broken-born-theory.md` §5.3). The ratio of dark to ordinary matter stays open for both candidates: "The 5.4 : 1 abundance question (polarization-genesis) applies to both" (#11 §12).
- **Which island is realized** is an observational question, posed by [the island discriminant](/wiki/predictions/island-discriminant).

## Record

The theorem appears in every later summary in the same form: #9 §7 item 1 ("collective momentum-space behavior and classical-particle dark matter are mutually exclusive"), #11 §9 (i), and [the handoff](/wiki/history/documents/handoff)'s artifact table, which describes 3a as giving the "classicality theorem (collective behavior ⇒ wave DM, m ≲ 0.1 meV)" (`HANDOFF.md` §3, row 2), where DM is dark matter.

**A word collision.** "Island" here names a mass regime of Debt 3. It is unrelated to the "consistency islands" of the gravity sector ([glossary](/wiki/glossary)).

## Sources

- `notes/debt3a-stream-stability.md` 'Corollary (the classicality theorem)' — the scaling, m_crit, N_occ and the theorem; 'Consequences for the predictions table' — the particle and wave islands; 'Setup' — the definition of g
- `papers/broken-born-checkpoint-v2.md` §9 (i) — the current statement and its tag; §8 — the knee; §12 — the χ-particle candidate and the shared abundance question
- `notes/debt3b-wave-island.md` 'Setup', 'The rate' — the wave island's upper edge and the second N_occ normalization; 'Standing results after Chunks A+B' — the particle island's standing
- `notes/debt3c-ufd-endpoint.md` 'Verdict and closure of Debt 3' — the survivors and the final wave-island range
- `notes/broken-born-program-v1.md` §7 — the theorem in the first consolidation
- `HANDOFF.md` §3 row 2 — the artifact summary of 3a
- `notes/broken-born-theory.md` 'Addendum (v0.2)' — the notebook's summary; §5.3 — the particle-side relic problem
- `review/wiki-build-flags.md` item 19 — the regime in which 3a evaluates the corollary, awaiting a ruling
