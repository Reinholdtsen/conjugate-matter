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
  - "notes/broken-born-theory.md §3"
  - "notes/broken-born-theory.md §4"
  - "notes/broken-born-theory.md §9"
  - "notes/debt3a-stream-stability.md 'Numbers at the scattering benchmark'"
  - "notes/debt3a-stream-stability.md 'Consequences for the predictions table'"
  - "notes/debt3b-wave-island.md 'What pins g? Two scenarios'"
  - "notes/debt3c-ufd-endpoint.md 'The attractive endpoint: criticality and the drain'"
---

*Self-interacting dark matter (SIDM) is dark matter whose particles scatter off one another through a force of their own, in addition to gravity. The scattering carries heat from the outer parts of a halo into its colder center, which turns the steep central density peak predicted for collisionless cold dark matter (CDM) into a flat core. How strongly the particles scatter, and how that strength changes with their relative speed, is the observable that the Broken-Born program's [velocity gate](/wiki/dark-matter/conjugate-matter/velocity-gate) modifies. This page is the established background; the program's own law is [the gated scattering law σ_T(v)](/wiki/dark-matter/conjugate-matter/scattering-law).*

**Status:** Established — [T], explained here from general knowledge — literature; the program's sources cite no paper for it, and it enters the program as the standard expectation of prediction [rows 1](/wiki/predictions/self-interaction-knee) and [2](/wiki/predictions/scattering-isotropy).

## What self-scattering does to a halo [T]

In the [standard cosmological model](/wiki/cosmology), dark matter is cold and collisionless: its particles feel only gravity. Simulations of such dark matter give halos whose density keeps rising toward the center, a cusp. In a cuspy halo the velocity dispersion is lowest near the center and rises outward, so the inner halo is dynamically colder than the region around it.

If the particles scatter off one another, collisions conduct heat down that temperature gradient, into the center. The heated central particles move onto wider orbits, the central density falls, and the cusp becomes a core of nearly constant density. The effect needs only a modest rate: about one scattering per particle over the age of the halo. [Debt 3a](/wiki/history/documents/debt-3-notes) of the program contrasts this with collective effects: "scattering fits only need Γt ∼ 1 over Gyr, which is ~30 orders cheaper" (`notes/debt3a-stream-stability.md`, 'Numbers at the scattering benchmark'; see [the instability criterion](/wiki/dark-matter/momentum-clumping/instability-criterion)).

The rate at which one particle scatters is Γ = n σ_T v, with n the number density, σ_T the [transfer cross-section](/wiki/dark-matter/halo-astrophysics/transfer-cross-section) and v the relative speed. Since n = ρ/m for mass density ρ and particle mass m:

```text
Γ = ρ (σ_T/m) v
```

Gravitational dynamics measures ρ and v, not m, so what observations constrain is the cross-section per unit mass, σ_T/m, usually quoted in cm²/g.

## The transfer cross-section [T]

Not every collision moves heat equally. The momentum-transfer cross-section, σ_T = ∫ dΩ (1 − cos θ) dσ/dΩ, weights each scattering angle θ by the forward momentum the collision removes, so grazing collisions (θ near 0) count for little and head-on rebounds most. Its definition, its relation to the total cross-section, its quotation per unit mass and its dependence on speed and angle are on [the transfer cross-section σ_T](/wiki/dark-matter/halo-astrophysics/transfer-cross-section). How it depends on speed is set by the force that carries the scattering, as the next two subsections describe.

### Contact and Yukawa forces

A dark force carried by a mediator of mass m_φ has a [Yukawa potential](/wiki/gravity/spin-2-fields/yukawa-forces), an attraction or repulsion that dies off beyond the range 1/m_φ. In the Born approximation (first order in the coupling) the scattering amplitude is proportional to 1/(q² + m_φ²), where q is the momentum transfer. Two limits bracket the behavior:

- **Heavy mediator, contact interaction** (m_φ much larger than the momentum transfer). The amplitude does not depend on q, the scattering is isotropic, and σ_T does not depend on speed.
- **Light mediator** (m_φ much smaller than the momentum transfer). The amplitude goes as 1/q², the Rutherford form, and the scattering is concentrated at small angles: it is forward-peaked. The transfer cross-section then falls steeply with speed, as v⁻⁴, multiplied by a logarithm that comes from the small-angle cutoff the mediator mass supplies, the Coulomb logarithm familiar from plasma physics.

[The lab notebook](/wiki/history/documents/lab-notebook) states the second limit as the standard behavior: "Yukawa SIDM falls as v⁻⁴ with a Coulomb-log correction", and "light-mediator Yukawa scattering is forward-peaked" (#1 §5.1).

### The Born regime and beyond

The Born approximation holds when the coupling is weak compared with the ratio of mediator mass to particle mass; at stronger coupling the scattering enters resonant and classical regimes, where σ_T(v) has a more complicated shape [T]. The program computes its own scattering in the Born approximation and records the limit at its benchmark: "At α̃ ∼ 1 the Born approximation is marginal (expect O(1) corrections); the *shape* claims above survive because they follow from the k- vs q-dependence, not from the coupling strength" (#1 §5.1). Here α̃ is the conjugate sector's coupling.

## Why velocity dependence matters [T]

Halos span a wide range of internal speeds. The program's Debt-3 notes, for example, model a classical dwarf core with dispersion 30 km/s and a galaxy cluster with 1000 km/s (`notes/debt3b-wave-island.md`, 'What pins g? Two scenarios'). A cross-section large enough to make cores in slow dwarfs must, if it stayed the same, also scatter strongly in fast clusters. A cross-section that falls with speed separates the two, and the shape of the fall is the observable. The program's documents state the standard expectations against which their rows 1 and 2 are measured:

```text
Row 1, σ_T(v) across halo masses:  "CDM none; Yukawa SIDM power-law + Coulomb log"     (#11 §13)
                                   "Constant (CDM: 0) or power-law v⁻⁴ln tail (Yukawa SIDM)"   (#1 §9)
Row 2, scattering anisotropy:      "Forward-peaked (light mediators)"                   (#11 §13)
```

The lab notebook names where the shapes separate: "The discriminating band is v ∼ 150–400 km/s (large spirals, small groups), where the two shapes diverge by orders of magnitude" (#1 §5.1). [The checkpoint](/wiki/history/documents/checkpoint)'s row 1 keeps that band in its kill condition, "knee excluded in the 150–400 km/s band" (#11 §13). The tests are [row 1: the knee in σ_T(v)](/wiki/predictions/self-interaction-knee) and [row 2: isotropic scattering](/wiki/predictions/scattering-isotropy).

## Gravothermal evolution [T]

A self-gravitating system has negative heat capacity: when it loses energy, it contracts and its particles speed up. Scattering therefore has two phases in a halo. First, heat flows into the cold center and builds a core. Later, once the core is hotter than its surroundings, heat flows outward, the core loses energy, contracts and heats further, and the flow accelerates; this runaway is the gravothermal catastrophe, or core collapse. Throughout, the collisions are elastic: they move energy between particles but do not remove particles, so the halo keeps its mass.

The program uses that last property as a contrast. On the [wave island](/wiki/dark-matter/momentum-clumping/wave-island), the condensate of an attractive self-interaction would eject mass from the halo in repeated collapses ([attractive condensates](/wiki/dark-matter/wave-dark-matter/attractive-condensates)). Debt 3c: even if heating and expansion throttle the rate "down to ~1/t_age (the gravothermal self-limit), an O(1) fraction of the core mass is processed *and removed* within the lifetime — unlike SIDM, where relaxation is elastic and mass stays" (`notes/debt3c-ufd-endpoint.md`, 'The attractive endpoint: criticality and the drain').

## The Bullet Cluster [T]

[The Bullet Cluster](/wiki/dark-matter/halo-astrophysics/bullet-cluster) is a pair of galaxy clusters seen after one passed through the other. The hot gas, most of the ordinary mass, was slowed and left between them, while the mass mapped by gravitational lensing moved on with the galaxies. The dark matter therefore passed through with little scattering, which limits σ_T/m at cluster collision speeds; a cross-section large enough to make dwarf cores can meet the limit by falling with speed. The program's χ is "Bullet-Cluster-safe" (#11 §8) on two counts: it lenses like ordinary dark matter ([the lab notebook](/wiki/history/documents/lab-notebook), #1 §4), and its gate is closed at cluster speeds, so row 1 requires "zero cluster signal (particle χ)" (#11 §13). How little scattering remains above the knee depends on the gate's tail, which is open ([Open: the gate shape](/wiki/dark-matter/conjugate-matter/gate-shape)).

## How the program uses it

### Conjugate matter as gated SIDM

On the [particle island](/wiki/dark-matter/momentum-clumping/classicality-theorem), where [conjugate matter](/wiki/dark-matter/conjugate-matter) χ is a gas of classical particles of MeV–GeV mass, the program's dark sector is a form of SIDM. Debt 3a: "On this island BBT is cliff-shaped SIDM plus Maslov quintessence", BBT being the Broken-Born program ('Consequences for the predictions table'). The difference from a Yukawa model lies in what the interaction depends on. The program's amplitude has the Yukawa propagator in the momentum transfer q, multiplied by a gate factor in the incoming relative momentum k:

```text
M(k, q) = 4πα̃m_χ/(q² + m_φ²) · F(k²/μ²)                    (#11 §8)
```

k is "the variable no x-local mediator produces" (#11 §8), and "An x-local Yukawa is the limit μ → ∞" (#1 §3). The lab notebook's v0.1 form, with a Gaussian gate e^{−k²/μ²} and a heavy mediator (m_φ ≳ m_χ, contact-like in position), gave the transfer cross-section

```text
σ_T(v) = σ₀ e^{−v²/v*²},    v* ≡ √2 μ/m_χ,    σ₀ = 16πα̃²m_χ²/m_φ⁴        (#1 §5.1, v0.1)
```

with "Two structural signatures" that set it apart from "*every* x-local mediator model": "An exponential cliff, not a power-law tail", and "Isotropy inside the gate" — "Because the gate depends on k and the contact part is flat in q, scattering below v\* is isotropic" (#1 §5.1). The isotropy rests on the heavy-mediator assumption. The exponential cliff has since been weakened to a knee whose tail is open: "σ_T(v) = σ₀F(v²/v\*²): robust knee at v\*; tail (Gaussian vs rational) diagnoses the vertex completion; isotropic below the gate versus Yukawa forward-peaking" (#11 §8). The history and the current law are on [the gated scattering law σ_T(v)](/wiki/dark-matter/conjugate-matter/scattering-law).

### The core-fitting value

The program fixes its coupling from dwarf cores: "Fitting dwarf-scale cores wants σ₀/m_χ ≈ 30 cm²/g at v ≲ v\* ≈ 120 km/s" (#1 §5.1), a value stated without a citation. With it, Debt 3a says the coupling is "*spent* — no freedom remains" ('Numbers at the scattering benchmark'), and the checkpoint's benchmark mass is m_χ ≈ 70 MeV·α̃^{2/3}(σ₀/m ÷ 30 cm²g⁻¹)^{−1/3} (#11 §8). See [the scattering benchmark](/wiki/dark-matter/conjugate-matter/benchmark) and [dwarf galaxies](/wiki/dark-matter/halo-astrophysics/dwarf-galaxies).

### The wave-island analog

On the [wave island](/wiki/dark-matter/momentum-clumping/wave-island), where χ is a classical wave field, two-body scattering is no longer the observable, and the role of SIDM heat transport passes to [the gated condensation rate](/wiki/dark-matter/momentum-clumping/wave-island/condensation-rate): Γ_self "*is* the analog of SIDM heat transport (kinetic relaxation redistributes energy through the halo)" (`notes/debt3b-wave-island.md`, 'What pins g? Two scenarios'). [Scenario A](/wiki/dark-matter/momentum-clumping/wave-island/scenario-a), which made that channel the core-maker, is dead.

## References

The program's documents cite no source for SIDM, the transfer cross-section or the Bullet Cluster. Added by the wiki from model memory (†):

- D. N. Spergel, P. J. Steinhardt, "Observational evidence for self-interacting cold dark matter," Phys. Rev. Lett. (2000)†: the proposal.
- S. Tulin, H.-B. Yu, K. M. Zurek, "Beyond collisionless dark matter: particle physics dynamics for dark matter halo structure," Phys. Rev. D (2013)†: Yukawa scattering in the Born, resonant and classical regimes.
- S. Tulin, H.-B. Yu, "Dark matter self-interactions and small scale structure," Phys. Rep. (2018)†: a review.
- M. Markevitch et al., Astrophys. J. (2004)†; D. Clowe et al., "A direct empirical proof of the existence of dark matter," Astrophys. J. Lett. (2006)†: the Bullet Cluster.
- D. Lynden-Bell, R. Wood (1968)†: the gravothermal catastrophe; S. Balberg, S. L. Shapiro, S. Inagaki, "Self-interacting dark matter halos and the gravothermal catastrophe," Astrophys. J. (2002)†.

## Used by

- [The velocity gate](/wiki/dark-matter/conjugate-matter/velocity-gate) — an ordinary position-local Yukawa interaction is the gate's μ → ∞ limit.
- [The gated scattering law σ_T(v)](/wiki/dark-matter/conjugate-matter/scattering-law) — replaces the Yukawa power-law tail with a knee at v\*, isotropic below it.
- [The scattering benchmark](/wiki/dark-matter/conjugate-matter/benchmark) — takes σ₀/m from the dwarf-core fit.
- [The χ-particle candidate](/wiki/dark-matter/candidates/chi-particles) — on the particle island the program's dark sector is gated self-interacting dark matter.
- [The classicality theorem and the particle island](/wiki/dark-matter/momentum-clumping/classicality-theorem) — on the particle island the program is "cliff-shaped SIDM plus Maslov quintessence" (Debt 3a).
- [The mean-field criterion and its 10²⁸–10³¹ shortfall](/wiki/dark-matter/momentum-clumping/instability-criterion) — evaluated at the coupling fixed by the core fit above.
- [Open: the dual-stress enhancement (OP5)](/wiki/dark-matter/conjugate-matter/dual-stress-enhancement) — the nuclear-scale σ₀ it must explain is the core-fitting value.
- [The nontriviality theorem](/wiki/program/postulates/nontriviality-theorem) — without an emergent η the program has no content beyond general relativity plus one SIDM model.
- [The gated condensation rate Γ_self](/wiki/dark-matter/momentum-clumping/wave-island/condensation-rate) — on the wave island, Γ_self is the analog of SIDM heat transport.
- [Obituary: Scenario A and the ultra-faint-dwarf endpoint](/wiki/dark-matter/momentum-clumping/wave-island/scenario-a) — the drain that SIDM's elastic relaxation does not produce.
- [Row 1: the knee in σ_T(v)](/wiki/predictions/self-interaction-knee) and [Row 2: isotropic scattering](/wiki/predictions/scattering-isotropy) — measured against the standard expectations above.

## Sources

- `papers/broken-born-checkpoint-v2.md` §8, §13 rows 1–2 — the gated amplitude; χ as Bullet-Cluster-safe; the knee; the standard expectations for rows 1 and 2
- `notes/debt3a-stream-stability.md` 'Numbers at the scattering benchmark', 'Consequences for the predictions table' — scattering fits need Γt ∼ 1; the "spent" coupling; cliff-shaped SIDM on the particle island
- `notes/debt3b-wave-island.md` 'What pins g? Two scenarios' — the wave-island rate as the analog of SIDM heat transport; the environment dispersions
- `notes/debt3c-ufd-endpoint.md` 'The attractive endpoint: criticality and the drain' — elastic relaxation keeps the mass; the gravothermal self-limit
- `notes/broken-born-theory.md` §3, §4, §5.1, §9 — the x-local Yukawa as the μ → ∞ limit; Bullet Cluster lensing centroids; the v0.1 scattering law, Yukawa SIDM's v⁻⁴ fall with a Coulomb log, forward peaking, the discriminating band, the dwarf-core value, the Born-approximation caveat; v0.1 row 1
