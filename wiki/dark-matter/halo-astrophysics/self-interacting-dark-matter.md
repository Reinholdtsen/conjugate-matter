---
title: "Self-interacting dark matter"
weight: 10
status: established
description: "Dark matter with non-gravitational self-scattering: the transfer cross-section per mass, Yukawa mediators and the Born regime, the Coulomb log and forward peaking, gravothermal evolution, and the Bullet Cluster limit."
provenance: [T]
sources:
  - "papers/broken-born-checkpoint-v2.md §8"
  - "papers/broken-born-checkpoint-v2.md §13 rows 1–2"
  - "notes/broken-born-theory.md §5.1"
  - "notes/broken-born-theory.md §4"
  - "notes/debt3c-ufd-endpoint.md 'The attractive endpoint: criticality and the drain'"
  - "notes/debt3b-wave-island.md 'What pins g? Two scenarios'"
---

*Self-interacting dark matter (SIDM) is dark matter whose particles scatter off one another through a force of their own, in addition to gravity. The scattering carries heat from the hot outer parts of a halo into its cold center, which turns the steep central density peak predicted for collisionless cold dark matter (CDM) into a flat core. How strongly the particles scatter, and how that strength changes with their relative speed, is the observable that the program's [velocity gate](/wiki/dark-matter/conjugate-matter/velocity-gate) modifies. This page is the established background; the program's own law is [the gated scattering law σ_T(v)](/wiki/dark-matter/conjugate-matter/scattering-law).*

**Status:** Established — [T], explained here from general knowledge — literature; the program's sources cite no paper for it, and it enters the program as the standard expectation of prediction rows 1 and 2.

## Key facts

- **The observable [T].** Self-scattering is measured by the momentum-transfer cross-section per unit mass, σ_T/m, as a function of the relative velocity v. The transfer cross-section weights each collision by the fraction of forward momentum it removes, so grazing collisions count for little.
- **The standard velocity dependence.** When the force is carried by a light (Yukawa) mediator, "Yukawa SIDM falls as v⁻⁴ with a Coulomb-log correction" ([the lab notebook](/wiki/history/documents/lab-notebook), #1 §5.1). [The checkpoint](/wiki/history/documents/checkpoint) (#11 §13) lists the standard expectation for [row 1](/wiki/predictions/self-interaction-knee) as "CDM none; Yukawa SIDM power-law + Coulomb log".
- **Forward peaking.** "light-mediator Yukawa scattering is forward-peaked" (#1 §5.1); the standard expectation for [row 2](/wiki/predictions/scattering-isotropy) is "Forward-peaked (light mediators)" (#11 §13). A heavy, contact-like mediator scatters equally in all directions [T].
- **The Born regime.** The program computes scattering in the Born approximation, which holds for weak coupling; at its benchmark, "At α̃ ~ 1 the Born approximation is marginal (expect O(1) corrections)" (#1 §5.1).
- **The core-fitting value the program used.** For the cores of dwarf galaxies, #1 §5.1 takes "σ₀/m_χ ≈ 30 cm²/g at v ≲ v\* ≈ 120 km/s", a value it states without a citation. It fixes [the scattering benchmark](/wiki/dark-matter/conjugate-matter/benchmark).
- **Gravothermal evolution [T].** Heat flow by scattering first builds the core; over longer times the same flow can make the core contract and heat up, because a self-gravitating system heats as it loses energy. The relaxation is elastic, so the halo keeps its mass: the [Debt-3 notes](/wiki/history/documents/debt-3-notes) contrast a draining condensate with SIDM, "where relaxation is elastic and mass stays", and call a rate throttled to ~1/t_age "the gravothermal self-limit" (`notes/debt3c-ufd-endpoint.md`).
- **The Bullet Cluster [T].** In this collision of two galaxy clusters, the hot gas that carries most of the ordinary mass was slowed between them, while the mass mapped by gravitational lensing moved on with the galaxies; dark matter therefore scatters off itself only weakly at cluster collision speeds. The program's χ is "Bullet-Cluster-safe" (#11 §8), and "Bullet Cluster lensing-centroid behavior is automatic" (#1 §4).

## Used by

- [The velocity gate](/wiki/dark-matter/conjugate-matter/velocity-gate) — an ordinary position-local Yukawa interaction is the gate's μ → ∞ limit.
- [The gated scattering law σ_T(v)](/wiki/dark-matter/conjugate-matter/scattering-law) — replaces the Yukawa power-law tail with a knee at v\*, isotropic below it.
- [The scattering benchmark](/wiki/dark-matter/conjugate-matter/benchmark) — takes σ₀/m from the dwarf-core fit.
- [The χ-particle candidate](/wiki/dark-matter/candidates/chi-particles) — on the particle island the program's dark sector is gated self-interacting dark matter.
- [The gated condensation rate Γ_self](/wiki/dark-matter/momentum-clumping/wave-island/condensation-rate) — on the wave island, Γ_self "*is* the analog of SIDM heat transport" (`notes/debt3b-wave-island.md`).
- [Obituary: Scenario A and the ultra-faint-dwarf endpoint](/wiki/dark-matter/momentum-clumping/wave-island/scenario-a) — the drain that SIDM's elastic relaxation does not produce.

## Sources

- `papers/broken-born-checkpoint-v2.md` §8, §13 rows 1–2 — χ as Bullet-Cluster-safe; the standard expectations for rows 1 and 2
- `notes/debt3c-ufd-endpoint.md` 'The attractive endpoint: criticality and the drain' — elastic relaxation keeps the mass; the gravothermal self-limit
- `notes/debt3b-wave-island.md` 'What pins g? Two scenarios' — the wave-island rate as the analog of SIDM heat transport
- `notes/broken-born-theory.md` §5.1 — Yukawa SIDM's v⁻⁴ fall with a Coulomb log, forward peaking, the dwarf-core value, the Born-approximation caveat
- `notes/broken-born-theory.md` §4 — Bullet Cluster lensing centroids for χ
