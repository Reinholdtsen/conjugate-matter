---
title: "The scattering benchmark"
weight: 50
status: alive
description: "Dwarf cores fix σ₀/m at the gate, giving m_χ ≈ 70 MeV·α̃^{2/3}(σ₀/m ÷ 30 cm²g⁻¹)^{−1/3}; the other benchmark numbers exist only in the lab notebook and are unverified."
provenance: [D]
sources:
  - "papers/broken-born-checkpoint-v2.md §8"
  - "notes/broken-born-theory.md §5.1"
  - "notes/debt3a-stream-stability.md 'Setup'"
  - "notes/debt3a-stream-stability.md 'Numbers at the scattering benchmark'"
  - "notes/broken-born-theory.md 'Addendum (v0.3, overnight)'"
---

*The scattering benchmark is the set of numbers obtained by requiring conjugate matter's self-scattering to produce the observed flat cores of dwarf galaxies. Fitting the cores fixes the cross-section per unit mass at low velocity, and with an assumed mediator mass that fixes the χ particle's mass at about 70 MeV for a coupling of order one. The checkpoint keeps only this mass relation. The other benchmark numbers, including the prediction that galaxy clusters show no self-interaction at all, appear only in the lab notebook, rest on a Gaussian gate tail that is now an open question, and have never been checked by machine.*

**Status:** Alive — [D] (`notes/broken-born-theory.md` §5.1) — only the mass relation survives into the checkpoint (#11 §8); no benchmark number has a `verify/` script, and for those that appear only in the lab notebook [the iron rule](/wiki/method/verification/iron-rule) is still owed.

## Key facts

- **The mass relation.** [The checkpoint](/wiki/history/documents/checkpoint) (#11 §8): "Benchmark: m_χ ≈ 70 MeV·α̃^{2/3}(σ₀/m ÷ 30 cm²g⁻¹)^{−1/3}."
- **Its inputs.** "Fitting dwarf-scale cores wants σ₀/m_χ ≈ 30 cm²/g at v ≲ v\* ≈ 120 km/s. With m_φ ~ m_χ this fixes" the relation above and "μ = m_χv\*/√2 ≈ 20 keV (α̃ ≈ 1)" ([the lab notebook](/wiki/history/documents/lab-notebook), #1 §5.1). The input is the observed cores of [dwarf galaxies](/wiki/dark-matter/halo-astrophysics/dwarf-galaxies), read as in [self-interacting dark matter](/wiki/dark-matter/halo-astrophysics/self-interacting-dark-matter); the gate velocity v\* is the knee location that [row 1](/wiki/predictions/self-interaction-knee) tests, written there as "v\* ~ 10² km/s" (#11 §13).
- **The coupling's caveat.** "At α̃ ~ 1 the Born approximation is marginal (expect O(1) corrections); the *shape* claims above survive because they follow from the k- vs q-dependence, not from the coupling strength" (#1 §5.1).
- **Numbers found only in the lab notebook.** "σ_T/m (300 km/s) ≈ 6×10⁻² cm²/g, σ_T/m (1500 km/s) ≈ 30 e^{−156} ≈ 0", and "Cluster self-interaction is *identically zero at any future sensitivity*" (#1 §5.1). They come from the v0.1 exponential cliff, so they hold only if the gate's tail is Gaussian, which is now [an open problem](/wiki/dark-matter/conjugate-matter/gate-shape); together with μ ≈ 20 keV they are unverified.
- **The coupling is spent.** "The dwarf-core fit fixes σ₀/m = 30 cm²/g, hence g is *spent* — no freedom remains. With m_χ = 70 MeV, v\* = 120 km/s", the momentum-clumping criterion fails by 28–31 orders of magnitude (`notes/debt3a-stream-stability.md`); see [the mean-field criterion](/wiki/dark-matter/momentum-clumping/instability-criterion). Debt 3a's coupling is "g ≡ 4πα̃/m_φ² = √(πσ₀/m²)" ('Setup').
- **An assumption from before the mechanism.** The choice m_φ ~ m_χ was made in v0.1, before the v0.3 addendum identified the gate's carrier as X exchange (#1); no later document revisits it. See [the gate mechanism](/wiki/dark-matter/conjugate-matter/gate-mechanism).
- **Why the strength needs explaining.** The checkpoint calls this σ₀ "nuclear-scale" and lists reconciling it with gravitational couplings of ordinary matter to X as its "Main open quantitative item" (#11 §8); see [the dual-stress enhancement](/wiki/dark-matter/conjugate-matter/dual-stress-enhancement).

## Sources

- `papers/broken-born-checkpoint-v2.md` §8 — the surviving mass relation; σ₀ as nuclear-scale
- `notes/debt3a-stream-stability.md` 'Setup', 'Numbers at the scattering benchmark' — the coupling g, "spent" at the benchmark
- `notes/broken-born-theory.md` §5.1 — the core-fit inputs, μ ≈ 20 keV, the Born caveat, the 300 and 1500 km/s numbers
- `notes/broken-born-theory.md` 'Addendum (v0.3, overnight)' — the gate's carrier identified as X exchange
