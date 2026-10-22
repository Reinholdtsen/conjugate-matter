---
title: "The scattering benchmark"
weight: 50
status: alive
description: "Dwarf cores fix σ₀/m at the gate, giving m_χ ≈ 70 MeV·α̃^{2/3}(σ₀/m ÷ 30 cm²g⁻¹)^{−1/3}; the other benchmark numbers exist only in the lab notebook and are unverified."
provenance: [D]
sources:
  - "papers/broken-born-checkpoint-v2.md §8"
  - "papers/broken-born-checkpoint-v2.md §9"
  - "papers/broken-born-checkpoint-v2.md §13 row 1"
  - "notes/broken-born-program-v1.md §6"
  - "notes/broken-born-theory.md §5.1"
  - "notes/broken-born-theory.md §10"
  - "notes/broken-born-theory.md §3"
  - "notes/broken-born-theory.md 'Addendum (v0.3, overnight)'"
  - "notes/debt3a-stream-stability.md 'Setup'"
  - "notes/debt3a-stream-stability.md 'Numbers at the scattering benchmark'"
  - "notes/debt3a-stream-stability.md 'Corollary (the classicality theorem)'"
  - "papers/conjugate-special-relativity.md §4"
  - "review/wiki-build-flags.md items 17, 19"
---

*The scattering benchmark is the set of numbers obtained by requiring the self-scattering of [conjugate matter](/wiki/dark-matter/conjugate-matter) to produce the flat central cores observed in dwarf galaxies. Fitting the cores fixes the cross-section per unit mass at low velocity; with an assumed mass for the carrier of the momentum transfer, that fixes the mass of a χ particle at about 70 MeV for a coupling of order one. [The checkpoint](/wiki/history/documents/checkpoint) keeps only this mass relation. The other benchmark numbers, among them the prediction that galaxy clusters show no self-interaction at any sensitivity, appear only in [the lab notebook](/wiki/history/documents/lab-notebook), rest on a Gaussian gate tail that is now an open question, and have never been checked by machine. The benchmark also fixes the coupling that the program's Debt-3 calculation used to rule out [collective clumping of χ particles](/wiki/dark-matter/momentum-clumping/founding-image).*

**Status:** Alive — [D] (`notes/broken-born-theory.md` §5.1) — the mass relation is carried by #11 §8, and v1 (#9 §6) states it for particle χ; no benchmark number has a `verify/` script, and the numbers found only in the lab notebook still lack the executed check that [the iron rule](/wiki/method/verification/iron-rule) requires. The lab notebook's predictions above the gate are superseded.

## The relation

The checkpoint, #11, gives the benchmark in one line of §8:

> "Benchmark: m_χ ≈ 70 MeV·α̃^{2/3}(σ₀/m ÷ 30 cm²g⁻¹)^{−1/3}."

```text
m_χ ≈ 70 MeV · α̃^{2/3} · (σ₀/m ÷ 30 cm²g⁻¹)^{−1/3}
```

Here m_χ is the mass of a χ particle, α̃ the coupling of its self-interaction amplitude, and σ₀/m the low-velocity [cross-section per unit mass](/wiki/dark-matter/halo-astrophysics/transfer-cross-section#per-unit-mass-t) of [the gated scattering law](/wiki/dark-matter/conjugate-matter/scattering-law), σ_T(v) = σ₀F(v²/v\*²). The relation is scaled to a reference value of σ₀/m of 30 cm²/g: at that value and α̃ = 1 it gives 70 MeV, and other values scale by the powers shown. v1 (#9 §6) gives the same relation "for particle-χ, with the wave-χ alternative in §7".

## Where the input comes from

Dark matter that does not scatter off itself, cold dark matter, is predicted to pile up in a steep central density peak, a cusp, while many dwarf galaxies show a flat core instead ([dwarf galaxies](/wiki/dark-matter/halo-astrophysics/dwarf-galaxies)) [T]. Self-scattering carries heat into the cold center of a halo and turns a cusp into a core, provided the cross-section per unit mass is large enough at the velocities found in dwarfs ([self-interacting dark matter](/wiki/dark-matter/halo-astrophysics/self-interacting-dark-matter)) [T].

The lab notebook takes the value from that requirement: "Fitting dwarf-scale cores wants σ₀/m_χ ≈ 30 cm²/g at v ≲ v\* ≈ 120 km/s" (#1 §5.1). It cites no source for the value. The gate velocity v\* is where the cross-section turns down, so dwarfs, at lower velocities, see the full σ₀. The checkpoint's row 1 places the knee at "v\* ~ 10² km/s" (#11 §13), less precisely than the notebook's 120 km/s.

## How the relation follows

The lab notebook derives the relation in §5.1, tagged [D], from its v0.1 scattering law:

```text
σ_T(v) = σ₀ e^{−v²/v*²},   v* ≡ √2 μ/m_χ,   σ₀ = 16πα̃²m_χ²/m_φ⁴
```

Here m_φ is the mass of the carrier of the momentum transfer and μ the gate's momentum width. "With m_φ ~ m_χ this fixes" the mass relation together with

```text
μ = m_χ v*/√2 ≈ 20 keV   (α̃ ≈ 1)
```

(#1 §5.1). The notebook does not show the algebra. The form of the relation can be read from σ₀ [T]: with m_φ set equal to m_χ, σ₀/m_χ is proportional to α̃²/m_χ³, so fixing σ₀/m fixes m_χ³ in proportion to α̃², which gives the powers 2/3 and −1/3. The prefactor of 70 MeV is the notebook's number and is not machine-checked. The value of μ follows from the definition of v\* at that mass and v\* ≈ 120 km/s.

The notebook attaches a caveat to the coupling: "At α̃ ~ 1 the Born approximation is marginal (expect O(1) corrections); the *shape* claims above survive because they follow from the k- vs q-dependence, not from the coupling strength" (#1 §5.1). The Born approximation is the first-order treatment of scattering, reliable when the interaction is weak [T]; at α̃ ~ 1 the absolute cross-section can be off by a factor of order one, and the notebook's argument is that the velocity dependence set by the gate survives because it does not depend on the coupling's size.

## The coupling is "spent"

The benchmark leaves no free strength in the [χ-particle](/wiki/dark-matter/candidates/chi-particles) sector, and the Debt-3 calculation used that. Calc note #2, the first of [the Debt-3 calc notes](/wiki/history/documents/debt-3-notes), writes the self-interaction strength as a single coupling,

```text
g ≡ 4πα̃/m_φ² = √(πσ₀/m²)
```

('Setup'), and then evaluates the mean-field criterion for collective clumping at the benchmark:

> "The dwarf-core fit fixes σ₀/m = 30 cm²/g, hence g is *spent* — no freedom remains. With m_χ = 70 MeV, v\* = 120 km/s:" (`notes/debt3a-stream-stability.md`, 'Numbers at the scattering benchmark')

The ratio of interaction energy to the threshold comes out "∼ 10⁻²⁸" in a dwarf core and "∼ 10⁻³¹" in the local halo of the Milky Way: "**Fails by 28–31 orders of magnitude.**" #11 §9 carries it as "fails by 10²⁸–10³¹ at the scattering benchmark". See [the mean-field criterion and its 10²⁸–10³¹ shortfall](/wiki/dark-matter/momentum-clumping/instability-criterion). The same calculation, run the other way, gives [the classicality theorem](/wiki/dark-matter/momentum-clumping/classicality-theorem): "satisfying the criterion at fixed σ₀/m forces m ≲ 0.1 meV, where N_occ ~ 10²⁰" (#11 §9): "collective momentum-space behavior and classical particles are mutually exclusive". On the regime in which Debt 3a evaluates that mass, see flag 19 in `review/wiki-build-flags.md`.

The benchmark is therefore the particle-island benchmark. On the [wave island](/wiki/dark-matter/momentum-clumping/wave-island), where χ is light enough to act as a classical wave, the dwarf-core fit is imposed on a different quantity, [the gated condensation rate](/wiki/dark-matter/momentum-clumping/wave-island/condensation-rate), and the combination it fixes is g²/m³ ([Obituary: Scenario A and the ultra-faint-dwarf endpoint](/wiki/dark-matter/momentum-clumping/wave-island/scenario-a)).

## Assumptions and caveats

- **An assumption from before the mechanism.** The choice m_φ ~ m_χ was made in v0.1, when the gate was a postulate. The v0.3 addendum later identified the carrier as exchange of the [momentum graviton X](/wiki/gravity/momentum-graviton) (#1 'Addendum (v0.3, overnight)'; [the gate mechanism](/wiki/dark-matter/conjugate-matter/gate-mechanism)). No later document revisits m_φ or relates it to the mass M_X of X ([conflicts between sources](/wiki/history/documents/source-conflicts)).
- **An uncited input.** The 30 cm²/g that fixes the scale is stated without a reference (#1 §5.1).
- **The Born approximation** is marginal at α̃ ~ 1, as the notebook says.
- **Numbers found only in the lab notebook.** μ ≈ 20 keV and the predictions above the gate (below) appear only in #1. The formulas for v\* and σ₀ come from #1 and are not restated in #11; [#13](/wiki/conjugate-relativity) §4 uses the definition of v\* with μ read as the χ quantum's fiber width ([the invariant-length shell](/wiki/conjugate-relativity/invariant-length-shell)), and a suspected factor of √2 in μ between the two gate conventions is recorded for a ruling in `review/wiki-build-flags.md` item 17 ([two conventions](/wiki/dark-matter/conjugate-matter/velocity-gate#two-conventions-not-reconciled)). The project's rule is that every asserted number gets executed code; for these, no `verify/` script exists ([the iron rule](/wiki/method/verification/iron-rule)).

## Why the strength needs explaining

The checkpoint calls this σ₀ "nuclear-scale", comparable to the cross-sections of nuclear physics [T]. In the same sentence it lists reconciling that value with the gravitational-strength couplings of ordinary matter to X as the "Main open quantitative item" (#11 §8). The benchmark fits σ₀; it does not explain how X exchange produces a cross-section that large. See [Open: the dual-stress enhancement (OP5)](/wiki/dark-matter/conjugate-matter/dual-stress-enhancement).

## Superseded: the v0.1 predictions from the benchmark

In v0.1 the benchmark fed predictions that the checkpoint no longer makes.

- **Cross-sections above the gate.** "Then the theory *predicts*, with zero remaining freedom: σ_T/m (300 km/s) ≈ 6×10⁻² cm²/g, σ_T/m (1500 km/s) ≈ 30 e^{−156} ≈ 0." (#1 §5.1)
- **Clusters.** "Cluster self-interaction is *identically zero at any future sensitivity* — a sharper statement than any Yukawa model can make, and a standing kill condition." (#1 §5.1; [scattering through a Yukawa mediator](/wiki/gravity/spin-2-fields/yukawa-forces#scattering-through-a-yukawa-mediator-t))
- **What two parameters covered.** The notebook's parameter count gave the conjugate sector two parameters, "σ₀/m, v\* (2)", covering "Dwarf cores, LSB/group knee, cluster nulls, stream granularity scale, friction suppression (≥5)" (#1 §10), LSB meaning low surface brightness galaxies.

The cross-section numbers come from the exponential cliff e^{−v²/v\*²}, which the v0.4 addendum weakened to a knee whose tail may be Gaussian or rational ([the gated scattering law](/wiki/dark-matter/conjugate-matter/scattering-law)). They hold only if the tail is Gaussian, which is now [Open: the gate shape (OP4)](/wiki/dark-matter/conjugate-matter/gate-shape), and none is machine-checked. The checkpoint keeps the qualitative statement, "zero cluster signal (particle χ)", in [row 1](/wiki/predictions/self-interaction-knee) (#11 §13), with no number attached. Of the five phenomena, two have died: velocity-space granularity ([obituary](/wiki/dark-matter/momentum-clumping/velocity-granularity)) and the suppression of [dynamical friction](/wiki/dark-matter/halo-astrophysics/halo-substructure) in dwarf cores ([obituary](/wiki/dark-matter/momentum-clumping/fornax-friction)).

## Sources

- `papers/broken-born-checkpoint-v2.md` §8 — the mass relation; σ₀ as nuclear-scale; the main open quantitative item; §9 — the 10²⁸–10³¹ shortfall at the benchmark and the classicality theorem; §13 row 1 — v\* ~ 10² km/s, zero cluster signal for particle χ
- `notes/broken-born-program-v1.md` §6 — the relation for particle χ
- `notes/debt3a-stream-stability.md` 'Setup' — the coupling g; 'Numbers at the scattering benchmark' — "spent" at the benchmark, the 28–31 orders; 'Corollary (the classicality theorem)'
- `notes/broken-born-theory.md` §5.1 — the core-fit input, σ₀ and v\*, m_φ ~ m_χ, μ ≈ 20 keV, the Born caveat, the 300 and 1500 km/s numbers, the cluster statement; §10 — the v0.1 parameter count; §3 — the v0.1 amplitude
- `notes/broken-born-theory.md` 'Addendum (v0.3, overnight)' — the gate's carrier identified as X exchange
- `papers/conjugate-special-relativity.md` §4 — the definition of v\* reused
- `review/wiki-build-flags.md` items 17, 19 — the suspected √2 in μ between the two gate conventions; the regime of the classicality corollary; both awaiting a ruling
