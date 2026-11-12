---
title: "The classicality theorem and the particle island"
weight: 50
status: alive
description: "Meeting the criterion forces m ≲ 0.1 meV, where N_occ ~ 10²⁰: collective velocity dynamics and classical-particle dark matter exclude each other, so, under the program's contact-range interaction, MeV–GeV χ scatters but cannot clump."
provenance: [D]
sources:
  - "notes/stream-stability.md 'Corollary'"
  - "notes/stream-stability.md 'Consequences for the predictions table'"
  - "notes/stream-stability.md 'Setup'"
  - "wiki/papers/broken-born-checkpoint-v2.md §9"
  - "wiki/papers/broken-born-checkpoint-v2.md §12"
  - "wiki/papers/broken-born-checkpoint-v2.md §8"
  - "wiki/papers/broken-born-checkpoint-v2.md §13"
  - "notes/wave-island.md 'Setup'"
  - "notes/wave-island.md 'The rate'"
  - "notes/wave-island.md 'Standing results'"
  - "notes/ufd-endpoint.md 'Verdict and closure'"
  - "notes/broken-born-program-v1.md §7"
  - "HANDOFF.md §3 row 2"
  - "notes/broken-born-theory.md 'Addendum (v0.2)'"
  - "notes/broken-born-theory.md §5.3"
  - "review/wiki-build-flags.md items 16, 19"
  - "notes/velocity-gated-gravity.md §4"
  - "verify/velocity_gated_gravity.py 'D. The obituary's scope'"
  - "review/wiki-build-checks/stream_stability_check.py"
  - "review/wiki-build-checks/stream_stability_check.out"
---

*The classicality theorem says that dark matter coupled strongly enough to clump in velocity must be so light that it behaves as a wave, not as a collection of separate particles. It follows from the [mean-field criterion](instability-criterion.md): at the scattering strength that fits dwarf-galaxy cores, the criterion can be met only for masses below about 0.1 meV, and at such masses about 10²⁰ quanta share each quantum state, which is the regime of a classical wave. The program therefore splits dark matter into two regimes: a particle island, with χ masses of MeV to GeV, where, under the program's [contact-range interaction](founding-image.md#the-scope-of-the-tests), which acts only over microscopic distances, dark matter scatters but cannot clump, and a [wave island](wave-island/_index.md) of far lighter masses. The theorem is derived at mean-field level and stands.*

**Status:** Alive — [D] ([#11](../../history/documents/checkpoint.md) [§9](../../papers/broken-born-checkpoint-v2.md#9-momentum-clumping-the-founding-image-tested) (i)), derived in [`notes/stream-stability.md`](../../../notes/stream-stability.md) ("Corollary (the classicality theorem)"). Mean-field level, at fixed σ₀/m. Not machine-checked: no `verify/` script computes m_crit or N_occ. Of the numbers of [the clumping problem](../../history/main-problems.md), the gate checks only the shortfall of the [mean-field criterion](instability-criterion.md) the theorem starts from, in section D of [`verify/velocity_gated_gravity.py`](../../../verify/velocity_gated_gravity.py) (flag 16, addendum of 2026-10-28; [the velocity-gated-gravity script](../../method/verification/velocity-gated-gravity-script.md)). A recomputation made while building the wiki, outside `verify/`, prints m_crit and N_occ in both gate limits (flag 19; see [Scope](#scope)).

## Statement

[#2](../../history/documents/clumping-notes.md), 'Corollary (the classicality theorem)':

> By the time the coupling is strong enough for collective behavior, the sector is deep in the wave regime. Collective velocity-space dynamics and classical-particle dark matter are mutually exclusive within this framework. This is a theorem-grade statement at mean-field level, not a benchmark accident.

[#11 §9](../../papers/broken-born-checkpoint-v2.md#9-momentum-clumping-the-founding-image-tested) (i), tagged [D]: "**Classicality theorem:** satisfying the criterion at fixed σ₀/m forces m ≲ 0.1 meV, where N_occ ~ 10²⁰ — collective momentum-space behavior and classical particles are mutually exclusive." The [lab notebook](../../history/documents/lab-notebook.md)'s addendum puts it in one line: "collective momentum-space behavior requires N_occ ≫ 1 — it exists only for wave dark matter" ([`notes/broken-born-theory.md`](../../../notes/broken-born-theory.md), 'Addendum (v0.2)').

"Theorem" and "theorem-grade" are the sources' words. The argument is a scaling argument at mean-field level, and its premises are listed under [Scope](#scope).

## The argument

The argument has three steps: how the stream criterion depends on the particle mass when the scattering strength is held fixed; the mass at which the criterion is met; and the [occupation number](../wave-dark-matter/occupation-number.md) at that mass.

### Step 1: the criterion grows as the mass falls

Write S ≡ σ₀/m for the cross-section per unit mass, the quantity that dwarf-core fits constrain ([the scattering benchmark](../conjugate-matter/benchmark.md)). [#2](../../../notes/stream-stability.md): "At fixed S ≡ σ₀/m and halo (ρ,σ), the criterion scales as √(πS) ρ/(m^{5/2}σ²)."

The note states the scaling without the intermediate line. The substitution below is the wiki's reading, not printed in the note. It starts from the broad-gate form of the criterion, g n/(mσ²), takes the model's definition g = √(πσ₀/m²) ([the gated Vlasov model](gated-vlasov-model.md)), and writes σ₀ = Sm and n = ρ/m:

```text
g = √(πS m)/m = √(πS) m^{−1/2},    n = ρ/m
g n/(mσ²) = √(πS) ρ/(m^{5/2} σ²)
```

At fixed S and fixed halo density ρ and [dispersion σ](../halo-astrophysics/velocity-dispersion.md), a lighter particle helps the criterion in two ways: the coupling per particle g grows as m^{−1/2}, and the number of particles in a given mass density grows as 1/m. Together with the m in the kinetic energy mσ², the criterion grows as m^{−5/2}.

### Step 2: the critical mass

Setting the criterion equal to 1 gives the mass below which streams could form (#2):

```text
m_crit = [√(πS) ρ/σ²]^{2/5} ≈ 10⁻¹³ GeV ~ 0.1 meV      (Milky Way conditions)
```

The scaling is the broad-gate form of the criterion, evaluated at Milky Way conditions; see [Scope](#scope) and flag 19 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md). At the benchmark mass m_χ = 70 MeV the criterion falls short by 10²⁸–10³¹ ([the mean-field criterion](instability-criterion.md)); lowering the mass at fixed S closes the gap only at m_crit.

### Step 3: the occupation number at that mass

The occupation number counts how many particles share one quantum state: the number of particles in a cube one de Broglie wavelength on a side. #2: "At that mass the per-mode occupation is"

```text
N_occ = n λ_dB³ = ρ/(m⁴σ³) ~ 10²⁰ ≫ 1
```

In the natural units of the notes (ħ = 1), the notes take λ_dB = 1/(mσ), the de Broglie wavelength ħ/(mσ) of a particle moving at speed σ up to factors of 2π, and the number density is n = ρ/m, which gives the second form [T]. The occupation grows as m⁻⁴: a lighter particle means both more particles in a given mass density and a longer wavelength for each.

When N_occ ≫ 1, the particles are described as a classical wave field, in the way that a radio wave is a classical field although it consists of photons: the field's amplitude and phase are well defined, and individual quanta play no role [T]. A classical phase-space gas, the description in which the criterion was derived, does not apply.

### The conclusion

At fixed S and in a given halo, the criterion can be met only by lowering m, and lowering m drives N_occ up as m⁻⁴, faster than the criterion's m^{−5/2}. By the time the criterion reaches 1, the dark matter is a wave with about 10²⁰ quanta per state (#2). The particle picture and collective velocity-space dynamics therefore never meet within the framework at mean-field level. The note does not spell out "not a benchmark accident". On the wiki's reading, it refers to m_crit depending on S and on the halo's ρ and σ but not on the benchmark mass of 70 MeV, so the conclusion does not hinge on the choice of χ mass. The faster growth of N_occ does not by itself guarantee N_occ ≫ 1 at m_crit; the margin, N_occ ~ 10²⁰, is computed for Milky Way conditions at the benchmark value of S.

## The particle island

The theorem splits the mass range in two. The particle island is the classical side. #2, 'Consequences for the predictions table':

> **Particle island** (m_χ ~ MeV–GeV): Rows 1–2 (exponential cliff, isotropy) **survive** — they are collisional. Rows 3 (velocity granularity) and 4 (condensed cores / Fornax friction suppression) are **withdrawn**, and with them the mechanism-level linkage claimed between them. On this island BBT is cliff-shaped SIDM plus Maslov quintessence.

Here BBT is Broken-Born theory, the program's earlier name, and SIDM is [self-interacting dark matter](../halo-astrophysics/self-interacting-dark-matter.md). The rows are those of the lab notebook's [prediction table](../../predictions/table-history.md). Rows 1 and 2, the velocity dependence of the scattering cross-section and the isotropy of scattering inside the [velocity gate](../conjugate-matter/velocity-gate.md), are about two-body collisions, which need no collective instability; that is the sense of "they are collisional". Rows 3 and 4 needed the instability; they are withdrawn and under review ([#11 §13](../../papers/broken-born-checkpoint-v2.md#13-predictions-and-kill-conditions)): [old row 3](velocity-granularity.md), velocity-space granularity, and [old row 4](fornax-friction.md), condensed cores and Fornax friction suppression. "Maslov quintessence" is the program's dark-energy field ([τ quintessence](../../cosmology/dark-energy/tau-quintessence.md)).

[#3](../../../notes/wave-island.md)'s standing result after the first two notes: "Particle island: cliff (exponential) + isotropy live; no collective phenomena. Fully classical, fully collisional." (#3, 'Standing results after Chunks A+B'). [#4](../../../notes/ufd-endpoint.md) lists the same pair among the survivors: "the exponential cliff + in-gate isotropy (particle island)".

**Since then.** The "cliff" of the notes, a Gaussian cut-off e^{−v²/v\*²} of the cross-section above v\*, has become a knee whose tail is open ([#11 §8](../../papers/broken-born-checkpoint-v2.md#8-conjugate-matter-and-the-gate); [the scattering law](../conjugate-matter/scattering-law.md)). The surviving rows are now [row 1, the knee](../../predictions/self-interaction-knee.md), and [row 2, isotropy](../../predictions/scattering-isotropy.md). The particle island is the home of the [χ-particle candidate](../candidates/chi-particles.md); [#11 §12](../../papers/broken-born-checkpoint-v2.md#12-the-dark-sector-question-three-candidates) lists its handles as "knee at v\*, sharp tail; isotropic scattering; permanent direct-detection null". The particle side of [the island discriminant](../../predictions/island-discriminant.md), the sharp knee, is this island's signature.

## The wave island

The other side of the theorem is the range of very light masses, where N_occ ≫ 1 and dark matter is a wave. #2: "**Wave island** (m_χ ≲ meV, N_occ ≫ 1): the collective sector is reborn in field language. The halo is an incoherent wave field; the gated attraction drives condensation in k-space — power flowing into narrow-momentum streams". Its treatment needs [wave kinetics](../wave-dark-matter/wave-kinetics.md) rather than [the Vlasov equation](vlasov-stability.md), and it has its own section: [the wave island](wave-island/_index.md).

The island's upper edge is written differently in the three notes: "m_χ ≲ meV" (#2), "m ≲ 0.1 meV" (#3, Setup), and 10⁻⁴ eV in #4's final range, "roughly 3×10⁻¹⁹ eV ≲ m ≲ 10⁻⁴ eV with Scenario-B couplings". #4's range closed the clumping problem and is the one this wiki uses.

## Scope

- **Mean-field level.** The theorem rests on the mean-field criterion, which is itself bracketed by two limits rather than solved in general ([the gated Vlasov model](gated-vlasov-model.md)).
- **Fixed σ₀/m.** The scaling holds the cross-section per unit mass at its dwarf-core value; [#11 §9](../../papers/broken-born-checkpoint-v2.md#9-momentum-clumping-the-founding-image-tested) states the premise as "at fixed σ₀/m". On the wave island the question becomes a [condensation rate](wave-island/condensation-rate.md) instead of this criterion, and under [Scenario B](wave-island/scenario-b.md) the coupling is free instead of fixed.
- **Milky Way conditions** for the number m_crit ≈ 10⁻¹³ GeV. The scaling has the broad-gate form, with σ² in the denominator, while #2's Limit 2 places the Milky Way in the narrow-gate regime and its benchmark table evaluates the Milky Way row with v\*; the note does not discuss the difference. Flag 19 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md) records it, with an executed check made while building the wiki, [`review/wiki-build-checks/stream_stability_check.py`](../../../review/wiki-build-checks/stream_stability_check.py). With #2's inputs, the check prints `m_crit = 1.4e-13 GeV = 0.14 meV` and `N_occ(m_crit) = 5.5e+19` for the broad form, and `m_crit (narrow-gate form) = 4.2e-14 GeV` and `N_occ at narrow-gate m_crit = 6.8e+21` for the narrow form with v\* fixed ([`review/wiki-build-checks/stream_stability_check.out`](../../../review/wiki-build-checks/stream_stability_check.out)). In the flag's words, "N_occ ≫ 1 either way, so the conclusion (collective behaviour needs wave dark matter) is unchanged". The check is not part of [the project's gate](../../method/verification/the-gate.md), [`scripts/check.sh`](../../../scripts/check.sh), and the flag is pending. The flags' audit rated it as depending on how the corollary is read. Read as a ceiling on m, it is right: #2's narrow form is at most 0.064× the broad one, so 1.4e-13 GeV caps m, which is how [#11 §9](../../papers/broken-born-checkpoint-v2.md#9-momentum-clumping-the-founding-image-tested) uses it ("forces m ≲ 0.1 meV"). Read as the Milky Way's threshold, it is about 3× high (4.2e-14 GeV).
- **Two normalizations of N_occ.** #2 writes N_occ = ρ/(m⁴σ³), and #3's Setup does the same, but #3's rate formula uses a "peak occupation N_occ ≈ (2π)^{3/2}ρ/(m⁴σ³)". The notes do not reconcile the two; at 10²⁰ ≫ 1 the factor does not affect the conclusion.

## What stays open

- **The [relic abundance](../candidates/relic-abundance.md)** on the particle island. The wave island obtains its abundance from [misalignment](wave-island/misalignment-relic.md). The particle island has no such route: the lab notebook states that this sector "cannot freeze out thermally without cannibalism problems" ([thermal freeze-out](../candidates/thermal-freeze-out.md#particle-χ-the-route-the-notebook-closes)) and assigns the abundance to [polarization-genesis](../candidates/polarization-genesis.md) [O] ([`notes/broken-born-theory.md` §5.3](../../../notes/broken-born-theory.md#53-relic-abundance-o)). The ratio of dark to ordinary matter stays open for all three candidates: "The 5.4 : 1 abundance question (polarization-genesis) applies to all three" ([#11 §12](../../papers/broken-born-checkpoint-v2.md#12-the-dark-sector-question-three-candidates)).
- **Which island is realized** is an observational question, posed by [the island discriminant](../../predictions/island-discriminant.md).

## Record

The theorem appears in every later summary in the same form: [#9 §7 item 1](../../../notes/broken-born-program-v1.md#7-the-death-of-momentum-clumping-the-clumping-problem-closed-negative) ("collective momentum-space behavior and classical-particle dark matter are mutually exclusive"), [#11 §9](../../papers/broken-born-checkpoint-v2.md#9-momentum-clumping-the-founding-image-tested) (i), and [the handoff](../../history/documents/handoff.md)'s artifact table, which describes #2 as giving the "classicality theorem (collective behavior ⇒ wave DM, m ≲ 0.1 meV)" ([`HANDOFF.md` §3](../../../HANDOFF.md#3-artifact-inventory-creation-order), row 2), where DM is dark matter.

**A word collision.** "Island" here names a mass regime of the clumping problem. It is unrelated to the "consistency islands" of the gravity sector ([glossary](../../glossary.md)).

## Sources

- [`notes/stream-stability.md`](../../../notes/stream-stability.md) 'Corollary (the classicality theorem)' — the scaling, m_crit, N_occ and the theorem; 'Consequences for the predictions table' — the particle and wave islands; 'Setup' — the definition of g
- [`wiki/papers/broken-born-checkpoint-v2.md` §9](../../papers/broken-born-checkpoint-v2.md#9-momentum-clumping-the-founding-image-tested) (i) — the current statement and its tag; [§8](../../papers/broken-born-checkpoint-v2.md#8-conjugate-matter-and-the-gate) — the knee; [§12](../../papers/broken-born-checkpoint-v2.md#12-the-dark-sector-question-three-candidates) — the χ-particle candidate and the shared abundance question; [§13](../../papers/broken-born-checkpoint-v2.md#13-predictions-and-kill-conditions) — the old rows 3 and 4, withdrawn and under review
- [`notes/wave-island.md`](../../../notes/wave-island.md) 'Setup', 'The rate' — the wave island's upper edge and the second N_occ normalization; 'Standing results after Chunks A+B' — the particle island's standing
- [`notes/ufd-endpoint.md`](../../../notes/ufd-endpoint.md) 'Verdict and closure of the clumping problem' — the survivors and the final wave-island range
- [`notes/broken-born-program-v1.md` §7](../../../notes/broken-born-program-v1.md#7-the-death-of-momentum-clumping-the-clumping-problem-closed-negative) — the theorem in the first consolidation
- [`HANDOFF.md` §3 row 2](../../../HANDOFF.md#3-artifact-inventory-creation-order) — the artifact summary of #2
- [`notes/broken-born-theory.md`](../../../notes/broken-born-theory.md) 'Addendum (v0.2)' — the notebook's summary; [§5.3](../../../notes/broken-born-theory.md#53-relic-abundance-o) — the particle-side relic problem
- [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md) item 19 — the regime in which #2 evaluates the corollary (pending); item 16, addendum — what the gate now checks of the clumping problem
- [`notes/velocity-gated-gravity.md` §4](../../../notes/velocity-gated-gravity.md#4-what-the-obituary-covers) — the scope of the tests, the program's contact-range interaction
- [`verify/velocity_gated_gravity.py`](../../../verify/velocity_gated_gravity.py) section D — the shortfall ratios of the criterion, not m_crit or N_occ
- [`review/wiki-build-checks/stream_stability_check.py`](../../../review/wiki-build-checks/stream_stability_check.py) and [`review/wiki-build-checks/stream_stability_check.out`](../../../review/wiki-build-checks/stream_stability_check.out) — the flag's executed check: m_crit and N_occ in the broad- and narrow-gate forms (outside `verify/`)
