---
title: "The mean-field criterion and its 10²⁸–10³¹ shortfall"
weight: 40
status: alive
description: "Streams need g·n_gate ≳ m·min(σ, v*)²; at the scattering benchmark the interaction falls short by 10²⁸ in dwarf cores and 10³¹ in the Milky Way, and the H-theorem closes the collisional route."
provenance: [D]
sources:
  - "notes/debt3a-stream-stability.md 'Limit 1 (broad gate)'"
  - "notes/debt3a-stream-stability.md 'Limit 2 (narrow gate)'"
  - "notes/debt3a-stream-stability.md 'Numbers at the scattering benchmark'"
  - "notes/debt3a-stream-stability.md 'Consequences for the predictions table'"
  - "papers/broken-born-checkpoint-v2.md §9"
  - "papers/broken-born-checkpoint-v2.md §8"
  - "notes/broken-born-theory.md §5.1"
  - "notes/broken-born-program-v1.md §7"
  - "HANDOFF.md §2"
  - "notes/broken-born-theory.md 'Addendum (v0.2)'"
  - "popsci/angle-of-the-mirror.md 'The killing fields'"
---

*The mean-field criterion is the condition under which a gas of dark-matter particles with the gated attraction would break up into velocity streams on its own: the attraction energy among particles that share a velocity has to match the kinetic energy of their random motion. Debt 3 derived it in two limits of the [gated Vlasov model](/wiki/dark-matter/momentum-clumping/gated-vlasov-model) and evaluated it at the [scattering benchmark](/wiki/dark-matter/conjugate-matter/benchmark), where the coupling is already fixed by fitting the cores of dwarf galaxies. There the attraction falls short by a factor of about 10²⁸ in dwarf-galaxy cores and 10³¹ in the Milky Way's halo near the Sun. Collisions cannot make up the difference, because they only drive the gas toward a smooth thermal distribution. The result rules out [velocity clumping](/wiki/dark-matter/momentum-clumping/founding-image) for particle dark matter, and the result itself stands.*

**Status:** Alive — [D] (#11 §9 (i)), derived in `notes/debt3a-stream-stability.md`. Mean-field only: the general eigenvalue problem is bracketed by two limits, not solved, and the threshold algebra is named but not printed. Not machine-checked: no `verify/` script covers any Debt-3 number, although the handoff marks the shortfall ✓ (see [the verification record](#verification-record)).

## Statement

#11 §9 (i), "Particle island [D]":

> Mean-field criterion g·n_gate ≥ m·min(σ,v\*)² fails by 10²⁸–10³¹ at the scattering benchmark; below threshold there is no growth; the H-theorem closes the collisional route.

Here g is the gated contact coupling, n_gate the number density of particles inside one particle's velocity gate, m the dark-matter particle mass, σ the halo's velocity dispersion and v\* the width of the [velocity gate](/wiki/dark-matter/conjugate-matter/velocity-gate) in relative velocity. The left side is the attraction energy a particle gains from its co-moving neighbours; the right side is the kinetic-energy scale of the random motion that the attraction must overcome. The note writes the same criterion as "ε_gate ≳ m·min(σ, v\*)²" (3a, Limit 2).

The criterion is the threshold for a collective instability. Above it, a smooth velocity distribution would fragment into streams; below it, a perturbation dies away. It is derived in the mean-field (Vlasov) description, in which each particle feels the averaged field of the others ([Vlasov stability](/wiki/dark-matter/momentum-clumping/vlasov-stability)).

## The broad-gate threshold

When the gate is much wider than the gas's momentum spread (μ ≫ mσ, "dwarf regime"), every particle attracts every other at the same point, and the linear-stability problem reduces to a single dispersion relation. 3a, Limit 1: "Static threshold (standard plasma-function algebra)":

```text
g n/(m σ²) ≥ 1,   i.e.   ε_int ≡ g n ≥ mσ²
```

g n is the attraction energy per particle in a gas of number density n, and mσ² is the kinetic energy of the random motion per particle, up to a factor of order one. The note does not print the algebra. In the textbook treatment of a Maxwellian gas with a momentum-independent attraction, the stability boundary is the static mode ω = 0, at which the attraction energy per particle equals mσ²; for gravity this gives the Jeans criterion, and for a contact attraction it gives the form above [T] ([the static threshold](/wiki/dark-matter/momentum-clumping/vlasov-stability#the-static-threshold-and-the-jeans-instability)).

Below threshold: "Landau-damped, stable." A ripple in the velocity distribution decays by phase mixing, without collisions. 3a adds: "There is no race with orbital stirring below threshold — the flocking never starts." That sentence retired the [lab notebook](/wiki/history/documents/lab-notebook)'s plan to compare the growth rate of streams with orbital phase mixing ([the gated Vlasov model](/wiki/dark-matter/momentum-clumping/gated-vlasov-model#superseded-racing-stream-growth-against-orbital-stirring)).

## The narrow-gate threshold

When the gate is much narrower than the spread (μ ≪ mσ, the "MW/cluster regime", that is the Milky Way and galaxy clusters), a mode lives on a small patch of momentum space of radius about μ. Only the co-movers inside the patch take part, and the spread inside the patch is v\*, not σ. 3a, Limit 2, applies the "Same algebra" with two substitutions,

```text
n → n_gate ≈ n (v*/σ)³/(2π)^{3/2}   (co-movers only)
σ → v*                               (internal spread of the patch)
```

giving

```text
g n_gate/(m v*²) ≥ O(1)
```

The co-mover density is a small fraction of n when v\* ≪ σ. As a reading, not the note's derivation: n/((2π)^{3/2}σ³) is the peak density in velocity space of a Maxwellian of dispersion σ [T], and multiplying it by a velocity-space volume v\*³, the size of the gate, gives the expression above. The factor (v\*/σ)³ is then the gate's share of the velocity space that the halo's particles fill.

## The unified criterion

3a merges the two limits: "Unified criterion: ε_gate ≳ m·min(σ, v\*)²". The smaller of σ and v\* sets the kinetic-energy scale. When σ is well below v\*, the whole velocity distribution lies inside the gate, as in the broad-gate limit; when σ is well above v\*, only co-movers count, as in the narrow-gate limit. The minimum joins the two cases; the intermediate regime is not solved. #11 §9 writes the criterion with n_gate, g·n_gate ≥ m·min(σ,v\*)², and #9 §7 does the same.

## Numbers at the scattering benchmark

**The coupling is fixed.** 3a: "The dwarf-core fit fixes σ₀/m = 30 cm²/g, hence g is spent — no freedom remains. With m_χ = 70 MeV, v\* = 120 km/s". The benchmark comes from the lab notebook's fit of [self-interacting dark matter](/wiki/dark-matter/halo-astrophysics/self-interacting-dark-matter) to dwarf-galaxy cores: "Fitting dwarf-scale cores wants σ₀/m_χ ≈ 30 cm²/g at v ≲ v\* ≈ 120 km/s" (`notes/broken-born-theory.md` §5.1). The checkpoint carries it as "m_χ ≈ 70 MeV·α̃^{2/3}(σ₀/m ÷ 30 cm²g⁻¹)^{−1/3}" (#11 §8; [the scattering benchmark](/wiki/dark-matter/conjugate-matter/benchmark)). Since g = √(πσ₀/m²) ([the gated Vlasov model](/wiki/dark-matter/momentum-clumping/gated-vlasov-model)), fixing σ₀/m and m fixes g. The criterion therefore has no free parameter left at the benchmark.

**The comparison** (3a, 'Numbers at the scattering benchmark'):

| System | ε_gate (GeV) | m·min(σ, v\*)² (GeV) | Ratio |
|---|---|---|---|
| Dwarf core (ρ ~ 1 GeV/cm³, σ ~ 30 km/s) | ~3×10⁻³⁷ | ~7×10⁻¹⁰ | ~10⁻²⁸ |
| MW halo, local (ρ ~ 0.4, σ ~ 155 km/s) | ~3×10⁻³⁹ | ~10⁻⁸ | ~10⁻³¹ |

The second row is the Milky Way's (MW's) halo near the Sun; the note gives its density without a unit, and the column is the same as in the first row. In the dwarf core σ is below v\*, so the right-hand side is mσ²; in the Milky Way σ is above v\*, so it is mv\*². The ratio is the left-hand side divided by the right-hand side; the criterion needs it to reach about 1.

3a's verdict: "**Fails by 28–31 orders of magnitude.**" #11 §9 (i) and #9 §7 repeat "10²⁸–10³¹"; #9 adds "in every environment".

## Why the shortfall is so large

3a: "Robust to every dropped O(1): halos are dilute, the force is contact-range, and a mean-field instability needs interaction energy density competitive with kinetic — scattering fits only need Γt ~ 1 over Gyr, which is ~30 orders cheaper."

Three reasons are named:

- **Halos are dilute.** The attraction energy per particle grows with the number density, and a galactic halo holds few particles per unit volume.
- **The force is contact-range.** A particle interacts only with neighbours at its own position, not with the whole halo, as it does through gravity's long range.
- **Scattering and instability ask for different things.** The benchmark coupling was fitted to make dwarf cores through scattering, and scattering accumulates: it needs each particle to scatter about once over billions of years, Γt ~ 1. A mean-field instability needs the attraction energy to compete with the kinetic energy at every instant. The second demand is "~30 orders" stronger than the first, so a coupling chosen to satisfy the first falls short of the second by about that much.

Because the factor is so large, the factors of order one dropped in the two limits cannot change the verdict.

## The collisional route: the H-theorem

If the mean field cannot make streams, collisions might. 3a closes this in one sentence: "The H-theorem closes the collisional back door: gated collisions still maximize entropy; equilibrium is Maxwellian to one part in 10³⁰." The textbook basis [T] is Boltzmann's H-theorem: collisions that conserve number, momentum and energy drive a gas toward the Maxwellian, whatever the cross-section's dependence on velocity, so a gate on the cross-section changes the relaxation rate and not the end state ([the H-theorem](/wiki/dark-matter/momentum-clumping/vlasov-stability#collisions-and-the-h-theorem)). The note states the conclusion without a separate derivation.

## What follows

- **The classicality theorem.** Meeting the criterion at fixed σ₀/m requires a mass so small that dark matter is a wave, not a gas of particles ([the classicality theorem](/wiki/dark-matter/momentum-clumping/classicality-theorem)).
- **The particle island.** For dark-matter particles with masses of MeV to GeV, clumping is forbidden. 3a withdraws the lab notebook's two clumping predictions on this island: "Rows 3 (velocity granularity) and 4 (condensed cores / Fornax friction suppression) are **withdrawn**" ([old row 3](/wiki/dark-matter/momentum-clumping/velocity-granularity), [old row 4](/wiki/dark-matter/momentum-clumping/fornax-friction)). The scattering predictions survive: "Rows 1–2 (exponential cliff, isotropy) **survive** — they are collisional."
- **The net theorem** records the particle case as "forbidden (particles)" ([the net theorem](/wiki/dark-matter/momentum-clumping/net-theorem)).

## Scope

- **Mean-field level.** The criterion comes from the linear stability of the Vlasov equation. The general eigenvalue problem on momentum space is bracketed by the broad- and narrow-gate limits, not solved.
- **A Gaussian gate** is assumed; the gate's shape is open (#11 §14 item 4; [the gate shape](/wiki/dark-matter/conjugate-matter/gate-shape)).
- **The benchmark.** The numbers hold at the benchmark coupling, which is fixed by the dwarf-core fit. The notebook's numbers behind that fit come from `notes/broken-born-theory.md` §5.1.
- **Classical particles.** The model treats dark matter as a classical gas, which [the classicality theorem](/wiki/dark-matter/momentum-clumping/classicality-theorem) shows is consistent on the particle island and not where the criterion could be met.

## Verification record

The handoff lists the result under "Dead (killed by own calculations — keep dead)" with a check mark: "impossible for particle DM (criterion fails by 10²⁸–10³¹ ✓)" (`HANDOFF.md` §2), where ✓ marks a machine-verified claim and DM is dark matter. No `verify/` script covers any Debt-3 number, and #11 §9 tags the result [D]. The checkpoint governs: the result is derived, not machine-verified, and any check behind the ✓ exists only in the old chat. Under [the iron rule](/wiki/method/verification/iron-rule) these numbers still owe an executed check.

The plain-language passages round the shortfall: #11 §9's italic passage says "thirty orders of magnitude", #9 §7's says "a factor of a million trillion trillion", and the popular article #10 says "a factor of ten to the thirtieth" (`popsci/angle-of-the-mirror.md`, 'The killing fields'). The notebook's addendum records "fails by 28–31 orders of magnitude at the scattering benchmark" (`notes/broken-born-theory.md`, 'Addendum (v0.2)'). The calc note's table is the record.

## Sources

- `notes/debt3a-stream-stability.md` 'Limit 1 — broad gate', 'Limit 2 — narrow gate' — the two thresholds and the unified criterion
- `notes/debt3a-stream-stability.md` 'Numbers at the scattering benchmark' — the benchmark, the shortfall table, robustness, the H-theorem
- `notes/debt3a-stream-stability.md` 'Consequences for the predictions table' — the particle island and the withdrawals
- `papers/broken-born-checkpoint-v2.md` §9 (i) — the current statement and its tag; §8 — the benchmark
- `notes/broken-born-theory.md` §5.1 — the dwarf-core fit behind the benchmark; 'Addendum (v0.2)' — the notebook's summary of the result
- `notes/broken-born-program-v1.md` §7 — the same result in the first consolidation
- `HANDOFF.md` §2 — the ✓ with no script behind it
- `popsci/angle-of-the-mirror.md` 'The killing fields' — the popular rounding (not a status source)
