---
title: "Row 1: the knee in σ_T(v)"
weight: 20
status: alive
description: "Strong self-scattering in slow dwarfs, none in fast clusters, with a knee at v* ~ 10² km/s; killed by robust self-interaction at v ≫ v* or a knee excluded in the 150–400 km/s band."
provenance: [D, O]
sources:
  - "papers/broken-born-checkpoint-v2.md §13 row 1"
  - "papers/broken-born-checkpoint-v2.md §8"
  - "papers/broken-born-checkpoint-v2.md §14 item 4"
  - "papers/broken-born-checkpoint-v2.md §15"
  - "notes/broken-born-program-v1.md §9"
  - "notes/broken-born-theory.md §5.1"
  - "notes/broken-born-theory.md §9"
  - "notes/broken-born-theory.md 'Addendum (v0.4)'"
  - "notes/debt1a-ii-X-classification.md §4"
---

*Row 1 of the predictions table tests how strongly dark matter scatters off itself as a function of the speed at which two particles collide. If dark matter is the program's [conjugate matter χ](/wiki/dark-matter/candidates/chi-particles) in particle form, its self-interaction acts only through [the velocity gate](/wiki/dark-matter/conjugate-matter/velocity-gate): it is strong in slow collisions, as in dwarf galaxies, and absent in fast ones, as in galaxy clusters, with a knee near the gate velocity v\* ~ 10² km/s between the two. Standard cold dark matter does not scatter at all, and the usual self-interacting models with a light force carrier weaken gradually, as a power law, rather than at a knee. Row 1 is one of the three rows that #11 lists as the program's near-term falsification exposure.*

**Status:** Alive, with near-term falsification exposure (#11 §15) — [D] for the gate mechanism, [O] for the knee's shape (#11 §8) — derived in the lab notebook and the Debt-1 calc notes and not machine-checked; the shape of the knee's tail is open problem 4 of #11 §14.

## Key facts

- **The row** ([checkpoint #11](/wiki/history/documents/checkpoint) §13). Observable: "σ_T(v) across halo masses". Standard expectation: "CDM none; Yukawa SIDM power-law + Coulomb log", that is, no self-scattering for cold dark matter (CDM), and a power-law tail with a Coulomb logarithm for Yukawa-mediated [self-interacting dark matter](/wiki/dark-matter/halo-astrophysics/self-interacting-dark-matter) (SIDM). Requirement: "Knee at v\* ~ 10² km/s; zero cluster signal (particle χ)". Killed by: "Robust self-interaction at v ≫ v\*; knee excluded in the 150–400 km/s band".
- **The law it tests** (#11 §8, [D — mechanism; shape [O]]): "σ_T(v) = σ₀F(v²/v\*²): robust knee at v\*; tail (Gaussian vs rational) diagnoses the vertex completion; isotropic below the gate versus Yukawa forward-peaking." The gate F comes from exchange of the massive [momentum graviton X](/wiki/gravity/momentum-graviton) between two χ quanta ([the gate mechanism](/wiki/dark-matter/conjugate-matter/gate-mechanism); [the gated scattering law](/wiki/dark-matter/conjugate-matter/scattering-law)).
- **Its strength.** The benchmark fitted to dwarf-galaxy cores is m_χ ≈ 70 MeV·α̃^{2/3}(σ₀/m ÷ 30 cm²g⁻¹)^{−1/3} (#11 §8; [the scattering benchmark](/wiki/dark-matter/conjugate-matter/benchmark)). How σ₀ can be nuclear-scale while the couplings to ordinary matter stay gravitational is open ([Open: the dual-stress enhancement](/wiki/dark-matter/conjugate-matter/dual-stress-enhancement)).
- **The band.** In the lab notebook's original version, "The discriminating band is v ~ 150–400 km/s (large spirals, small groups), where the two shapes diverge by orders of magnitude" (#1 §5.1). The systems at the slow end are described in [dwarf galaxies](/wiki/dark-matter/halo-astrophysics/dwarf-galaxies).
- **From cliff to knee.** v0.1 required a "cliff at v\* ~ 120 km/s; **exactly zero in clusters forever**", killed by "Robust nonzero self-interaction at v > 3v\*" (#1 §9). Once the gate's mechanism was derived, "the exponential cliff weakens to a sharp knee at v\* with tail shape (Gaussian vs rational) diagnosing the vertex completion; the knee's existence and location remain the robust prediction" (#1 'Addendum (v0.4)'). Calc note #6 §4 gives the reason: "tree-level exchange with generic vertices yields rational (power-law-tailed) gates; the Gaussian requires the Gaussian fiber profile". v1 (#9 §9) already carries the knee; see [the history of the table](/wiki/predictions/table-history).
- **What is open.** The gate shape, "Gaussian vs rational — now observable", is #11 §14 item 4 [O] ([Open: the gate shape](/wiki/dark-matter/conjugate-matter/gate-shape)). The definition v\* ≡ √2μ/m_χ, with μ the momentum width of a χ quantum, is the lab notebook's (#1 §5.1); #11 does not restate it. The tail is what [row 3, the island discriminant](/wiki/predictions/island-discriminant), reads, and rows 1–3 together are the discriminators of [row 11](/wiki/predictions/dark-sector-microstructure). Its companion signature is [row 2](/wiki/predictions/scattering-isotropy).
- **Exposure.** #11 §15: "**Falsification exposure:** genuine and near-term (rows 1, 4, 7)."

## Sources

- `papers/broken-born-checkpoint-v2.md` §13 row 1 — the row; §8 for the law, the mechanism tag and the benchmark; §14 item 4 for the open gate shape; §15 for the exposure
- `notes/broken-born-theory.md` 'Addendum (v0.4)' and `notes/debt1a-ii-X-classification.md` §4 — the amendment from cliff to knee and its reason
- `notes/broken-born-program-v1.md` §9 — v1's row 1, already a knee
- `notes/broken-born-theory.md` §5.1, §9 — the v0.1 cliff, the definition of v\*, the 150–400 km/s band and the v0.1 row
