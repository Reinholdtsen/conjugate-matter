---
title: "The scattering benchmark"
weight: 50
status: alive
description: "Dwarf cores fix σ₀/m at the gate, giving m_χ ≈ 70 MeV·α̃^{2/3}(σ₀/m ÷ 30 cm²g⁻¹)^{−1/3}, contact Born arithmetic that needs no gate mechanism; the predictions above the gate exist only in the lab notebook and are unverified."
provenance: [D]
sources:
  - "wiki/papers/broken-born-checkpoint-v2.md §8"
  - "wiki/papers/broken-born-checkpoint-v2.md §9"
  - "wiki/papers/broken-born-checkpoint-v2.md §13 row 1"
  - "wiki/papers/broken-born-checkpoint-v2.md §13"
  - "notes/broken-born-program-v1.md §6"
  - "notes/broken-born-theory.md §5.1"
  - "notes/broken-born-theory.md §10"
  - "notes/broken-born-theory.md §3"
  - "notes/broken-born-theory.md 'Addendum (v0.3, overnight)'"
  - "notes/stream-stability.md 'Setup'"
  - "notes/stream-stability.md 'Numbers at the scattering benchmark'"
  - "notes/stream-stability.md 'Corollary (the classicality theorem)'"
  - "wiki/papers/conjugate-special-relativity.md §4"
  - "review/wiki-build-flags.md items 16, 17, 19, 55"
  - "notes/gate-mechanism.md §1"
  - "notes/gate-mechanism.md §5"
  - "verify/gate_mechanism.py 'D. Numbers in run 4's convention'"
  - "verify/velocity_gated_gravity.py 'D. The obituary's scope'"
---

*The scattering benchmark is the set of numbers obtained by requiring the self-scattering of [conjugate matter](_index.md) to produce the flat central cores observed in dwarf galaxies. Fitting the cores fixes the cross-section per unit mass at low velocity; with an assumed mass for the carrier of the momentum transfer, that fixes the mass of a χ particle at about 70 MeV for a coupling of order one. [The checkpoint](../../history/documents/checkpoint.md) keeps only this mass relation, whose arithmetic is contact scattering in the Born approximation and does not depend on how the gate arises. The benchmark's predictions above the gate, among them the prediction that galaxy clusters show no self-interaction at any sensitivity, appear only in [the lab notebook](../../history/documents/lab-notebook.md), rest on a Gaussian gate tail that is an open question, and have never been checked by machine. The benchmark also fixes the coupling at which, in the clumping calculation, [collective clumping of χ particles](../momentum-clumping/founding-image.md) fails under the program's contact-range interaction, which acts only over microscopic distances.*

**Status:** Alive — [D] ([`notes/broken-born-theory.md` §5.1](../../../notes/broken-born-theory.md#51-the-scattering-law-d)) — the mass relation is carried by [#11 §8](../../papers/broken-born-checkpoint-v2.md#8-conjugate-matter-and-the-gate), and v1 ([#9 §6](../../../notes/broken-born-program-v1.md#6-conjugate-matter-and-the-gate-the-gate-problem-mechanism-found)) states it for particle χ. Some benchmark numbers have a `verify/` script, and the tag is [D]: [`verify/gate_mechanism.py`](../../../verify/gate_mechanism.py) section D recomputes σ₀/m = 32.0 cm²/g at 70 MeV, or m = 71.5 MeV for 30 cm²/g, and the conventions for μ and v\* ([the gate-mechanism script](../../method/verification/gate-mechanism-script.md)), and [`verify/velocity_gated_gravity.py`](../../../verify/velocity_gated_gravity.py) section D reproduces calc note [#2](../../../notes/stream-stability.md)'s coupling and its shortfall ratios (flag 16 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md), addendum; [the velocity-gated-gravity script](../../method/verification/velocity-gated-gravity-script.md)). The lab notebook's predictions above the gate still lack the executed check that [the iron rule](../../method/verification/iron-rule.md) requires, and they are superseded. The gate-mechanism note of 2026-10-28, which disputes the gate's derivation (flag 55), leaves the benchmark unchanged: "The benchmark arithmetic is contact Born physics and needs no mechanism" ([`notes/gate-mechanism.md` §5](../../../notes/gate-mechanism.md#5-what-follows-for-the-record)).

## The relation

The checkpoint, #11, gives the benchmark in one line of [§8](../../papers/broken-born-checkpoint-v2.md#8-conjugate-matter-and-the-gate):

> "Benchmark: m_χ ≈ 70 MeV·α̃^{2/3}(σ₀/m ÷ 30 cm²g⁻¹)^{−1/3}."

```text
m_χ ≈ 70 MeV · α̃^{2/3} · (σ₀/m ÷ 30 cm²g⁻¹)^{−1/3}
```

Here m_χ is the mass of a χ particle, α̃ the coupling of its self-interaction amplitude, and σ₀/m the low-velocity [cross-section per unit mass](../halo-astrophysics/transfer-cross-section.md#per-unit-mass-t) of [the gated scattering law](scattering-law.md), σ_T(v) = σ₀F(v²/v\*²). The relation is scaled to a reference value of σ₀/m of 30 cm²/g: at that value and α̃ = 1 it gives 70 MeV, and other values scale by the powers shown. v1 ([#9 §6](../../../notes/broken-born-program-v1.md#6-conjugate-matter-and-the-gate-the-gate-problem-mechanism-found)) gives the same relation "for particle-χ, with the wave-χ alternative in §7".

## Where the input comes from

Dark matter that does not scatter off itself, cold dark matter, is predicted to pile up in a steep central density peak, a cusp, while many dwarf galaxies show a flat core instead ([dwarf galaxies](../halo-astrophysics/dwarf-galaxies.md)) [T]. Self-scattering carries heat into the cold center of a halo and turns a cusp into a core, provided the cross-section per unit mass is large enough at the velocities found in dwarfs ([self-interacting dark matter](../halo-astrophysics/self-interacting-dark-matter.md)) [T].

The lab notebook takes the value from that requirement: "Fitting dwarf-scale cores wants σ₀/m_χ ≈ 30 cm²/g at v ≲ v\* ≈ 120 km/s" ([#1 §5.1](../../../notes/broken-born-theory.md#51-the-scattering-law-d)). It cites no source for the value. The gate velocity v\* is where the cross-section turns down, so dwarfs, at lower velocities, see the full σ₀. The checkpoint's row 1 places the knee at "v\* ~ 10² km/s" ([#11 §13](../../papers/broken-born-checkpoint-v2.md#13-predictions-and-kill-conditions)), less precisely than the notebook's 120 km/s.

## How the relation follows

The lab notebook derives the relation in [§5.1](../../../notes/broken-born-theory.md#51-the-scattering-law-d), tagged [D], from its v0.1 scattering law:

```text
σ_T(v) = σ₀ e^{−v²/v*²},   v* ≡ √2 μ/m_χ,   σ₀ = 16πα̃²m_χ²/m_φ⁴
```

Here m_φ is the mass of the carrier of the momentum transfer and μ the gate's momentum width. "With m_φ ~ m_χ this fixes" the mass relation together with

```text
μ = m_χ v*/√2 ≈ 20 keV   (α̃ ≈ 1)
```

([#1 §5.1](../../../notes/broken-born-theory.md#51-the-scattering-law-d)). The notebook does not show the algebra. The form of the relation can be read from σ₀ [T]: with m_φ set equal to m_χ, σ₀/m_χ is proportional to α̃²/m_χ³, so fixing σ₀/m fixes m_χ³ in proportion to α̃², which gives the powers 2/3 and −1/3. The prefactor of 70 MeV is the notebook's number. [`notes/gate-mechanism.md` §5](../../../notes/gate-mechanism.md#5-what-follows-for-the-record) recomputes it [V]: σ₀ = 16πα̃²m²/m_φ⁴ with α̃ = 1 and m_φ = m_χ "gives σ₀/m = 32.0 cm²/g at 70 MeV, or m = 71.5 MeV for 30 cm²/g" ([`verify/gate_mechanism.py`](../../../verify/gate_mechanism.py) section D). The value of μ follows from the definition of v\* at that mass and v\* ≈ 120 km/s. The same note finds the two not exactly consistent: "The second takes μc = 20 keV at m = 70 MeV, so v\* = 121.1 km/s and ħ/μ = 9.87 pm", while "The first takes v\* = 120 km/s, so μc = 19.81 keV and ħ/μ = 9.96 pm. They differ by 0.95%" (§1), where "the first" and "the second" are the note's two derivations. In the note's conventions μ/m = 2.857×10⁻⁴, v\* = 121.1 km/s and v_a = 171.3 km/s (§5), with v_a = √2 v\* the width of the amplitude gate e^{−v²/v_a²}.

The notebook attaches a caveat to the coupling: "At α̃ ~ 1 the Born approximation is marginal (expect O(1) corrections); the *shape* claims above survive because they follow from the k- vs q-dependence, not from the coupling strength" ([#1 §5.1](../../../notes/broken-born-theory.md#51-the-scattering-law-d)). The Born approximation is the first-order treatment of scattering, reliable when the interaction is weak [T]; at α̃ ~ 1 the absolute cross-section can be off by a factor of order one, and the notebook's argument is that the velocity dependence set by the gate survives because it does not depend on the coupling's size.

## The coupling is determined

The benchmark leaves no free strength in the [χ-particle](../candidates/chi-particles.md) sector, and the clumping calculation used that. Calc note #2, the first of [the clumping calc notes](../../history/documents/clumping-notes.md), writes the self-interaction strength as a single coupling,

```text
g ≡ 4πα̃/m_φ² = √(πσ₀/m²)
```

('Setup'), and then evaluates the mean-field criterion for collective clumping at the benchmark:

> "The dwarf-core fit fixes σ₀/m = 30 cm²/g, hence g is *determined* — no freedom remains. With m_χ = 70 MeV, v\* = 120 km/s:" ([`notes/stream-stability.md`](../../../notes/stream-stability.md), 'Numbers at the scattering benchmark')

The ratio of interaction energy to the threshold comes out "∼ 10⁻²⁸" in a dwarf core and "∼ 10⁻³¹" in the local halo of the Milky Way: "**Fails by 28–31 orders of magnitude.**" [#11 §9](../../papers/broken-born-checkpoint-v2.md#9-momentum-clumping-the-founding-image-tested) carries it as "fails by 10²⁸–10³¹ at the scattering benchmark". See [the mean-field criterion and its 10²⁸–10³¹ shortfall](../momentum-clumping/instability-criterion.md). The same calculation, run the other way, gives [the classicality theorem](../momentum-clumping/classicality-theorem.md): "satisfying the criterion at fixed σ₀/m forces m ≲ 0.1 meV, where N_occ ~ 10²⁰" ([#11 §9](../../papers/broken-born-checkpoint-v2.md#9-momentum-clumping-the-founding-image-tested)): "collective momentum-space behavior and classical particles are mutually exclusive". On the regime in which calc note #2 evaluates that mass, see flag 19 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md).

The benchmark is therefore the particle-island benchmark. On the [wave island](../momentum-clumping/wave-island/_index.md), where χ is light enough to act as a classical wave, the dwarf-core fit is imposed on a different quantity, [the gated condensation rate](../momentum-clumping/wave-island/condensation-rate.md), and the combination it fixes is g²/m³ ([Under review: Scenario A and the ultra-faint-dwarf endpoint](../momentum-clumping/wave-island/scenario-a.md)).

## Assumptions and caveats

- **An assumption from before the mechanism.** The choice m_φ ~ m_χ was made in v0.1, when the gate was a postulate. The v0.3 addendum later identified the carrier as exchange of the [momentum graviton X](../../gravity/momentum-graviton/_index.md) (#1 'Addendum (v0.3, overnight)'; [the gate mechanism](gate-mechanism.md)). No later document revisits m_φ or relates it to the mass M_X of X ([conflicts between sources](../../history/documents/source-conflicts.md)). [`notes/gate-mechanism.md`](../../../notes/gate-mechanism.md) (2026-10-28; two derivations, the second blind; not reviewed) finds that exchanging [#11 §7](../../papers/broken-born-checkpoint-v2.md#7-the-massive-momentum-graviton)'s X cannot produce the gate, and flag 55 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md), pending, proposes [P] for the gate and μ and [O] for the mechanism; [#11 §8](../../papers/broken-born-checkpoint-v2.md#8-conjugate-matter-and-the-gate) tags the mechanism [D] ([the gate mechanism](gate-mechanism.md#exchanging-x-cannot-produce-the-gate)). The benchmark does not depend on the outcome, since its arithmetic needs no mechanism ([§5](../../papers/broken-born-checkpoint-v2.md#5-the-kinematic-core-and-the-compatibility-theorem)).
- **An uncited input.** The 30 cm²/g that fixes the scale is stated without a reference ([#1 §5.1](../../../notes/broken-born-theory.md#51-the-scattering-law-d)).
- **The Born approximation** is marginal at α̃ ~ 1, as the notebook says.
- **Numbers found only in the lab notebook.** μ ≈ 20 keV and the predictions above the gate (below) appear only in #1; μ and the 70 MeV prefactor are recomputed in [`verify/gate_mechanism.py`](../../../verify/gate_mechanism.py), the predictions above the gate are not. The formulas for v\* and σ₀ come from #1 and are not restated in #11; [#13](../../conjugate-relativity/_index.md) [§4](../../papers/conjugate-special-relativity.md#4-invariants-the-mass-shell-and-the-length-shell) uses the definition of v\* with μ read as the χ quantum's [fiber width](../../phase-space/reciprocity/momentum-fibers.md#quanta-with-a-width-along-the-fiber) ([the invariant-length shell](../../conjugate-relativity/invariant-length-shell.md)), and a suspected factor of √2 in μ between the two gate conventions is recorded in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md) item 17, pending ([two conventions](velocity-gate.md#two-conventions-not-reconciled)). The project's rule is that every asserted number gets executed code; for the predictions above the gate, no `verify/` script exists ([the iron rule](../../method/verification/iron-rule.md)).

## Why the strength needs explaining

The checkpoint calls this σ₀ "nuclear-scale", comparable to the cross-sections of nuclear physics [T]. In the same sentence it lists reconciling that value with the gravitational-strength couplings of ordinary matter to X as the "Main open quantitative item" ([#11 §8](../../papers/broken-born-checkpoint-v2.md#8-conjugate-matter-and-the-gate)). The benchmark fits σ₀; it does not explain how X exchange produces a cross-section that large, and whether X exchange produces the gate at all is disputed (flag 55). The gate-mechanism note keeps the strength apart: "The coupling's strength (OP5, the dual-stress enhancement) stays open whatever the mechanism" ([`notes/gate-mechanism.md` §5](../../../notes/gate-mechanism.md#5-what-follows-for-the-record)). See [Open: the dual-stress enhancement (OP5)](dual-stress-enhancement.md).

## Superseded: the v0.1 predictions from the benchmark

In v0.1 the benchmark fed predictions that the checkpoint no longer makes.

- **Cross-sections above the gate.** "Then the theory *predicts*, with zero remaining freedom: σ_T/m (300 km/s) ≈ 6×10⁻² cm²/g, σ_T/m (1500 km/s) ≈ 30 e^{−156} ≈ 0." ([#1 §5.1](../../../notes/broken-born-theory.md#51-the-scattering-law-d))
- **Clusters.** "Cluster self-interaction is *identically zero at any future sensitivity* — a sharper statement than any Yukawa model can make, and a standing kill condition." ([#1 §5.1](../../../notes/broken-born-theory.md#51-the-scattering-law-d); [scattering through a Yukawa mediator](../../gravity/spin-2-fields/yukawa-forces.md#scattering-through-a-yukawa-mediator-t))
- **What two parameters covered.** The notebook's parameter count gave the conjugate sector two parameters, "σ₀/m, v\* (2)", covering "Dwarf cores, LSB/group knee, cluster nulls, stream granularity scale, friction suppression (≥5)" ([#1 §10](../../../notes/broken-born-theory.md#10-parameter-count)), LSB meaning low surface brightness galaxies.

The cross-section numbers come from the exponential cliff e^{−v²/v\*²}, which the v0.4 addendum weakened to a knee whose tail may be Gaussian or rational ([the gated scattering law](scattering-law.md)). They hold only if the tail is Gaussian, which is now [Open: the gate shape (OP4)](gate-shape.md), and none is machine-checked. The checkpoint keeps the qualitative statement, "zero cluster signal (particle χ)", in [row 1](../../predictions/self-interaction-knee.md) ([#11 §13](../../papers/broken-born-checkpoint-v2.md#13-predictions-and-kill-conditions)), with no number attached; two published fits mildly prefer a nonzero cross-section at cluster speeds, short of the row's kill condition ([the data situation](../../predictions/self-interaction-knee.md#the-data-situation); flag 69 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md), pending). Of the five phenomena, two were withdrawn on the results of the clumping problem and are under review: velocity-space granularity ([under review](../momentum-clumping/velocity-granularity.md)) and the suppression of [dynamical friction](../halo-astrophysics/halo-substructure.md) in dwarf cores ([under review](../momentum-clumping/fornax-friction.md)).

## Sources

- [`wiki/papers/broken-born-checkpoint-v2.md` §8](../../papers/broken-born-checkpoint-v2.md#8-conjugate-matter-and-the-gate) — the mass relation; σ₀ as nuclear-scale; the main open quantitative item; [§9](../../papers/broken-born-checkpoint-v2.md#9-momentum-clumping-the-founding-image-tested) — the 10²⁸–10³¹ shortfall at the benchmark and the classicality theorem; [§13 row 1](../../papers/broken-born-checkpoint-v2.md#13-predictions-and-kill-conditions) — v\* ~ 10² km/s, zero cluster signal for particle χ; [§13](../../papers/broken-born-checkpoint-v2.md#13-predictions-and-kill-conditions), below the table — the two withdrawn rows, under review
- [`notes/broken-born-program-v1.md` §6](../../../notes/broken-born-program-v1.md#6-conjugate-matter-and-the-gate-the-gate-problem-mechanism-found) — the relation for particle χ
- [`notes/stream-stability.md`](../../../notes/stream-stability.md) 'Setup' — the coupling g; 'Numbers at the scattering benchmark' — the coupling determined at the benchmark, the 28–31 orders; 'Corollary (the classicality theorem)'
- [`notes/broken-born-theory.md` §5.1](../../../notes/broken-born-theory.md#51-the-scattering-law-d) — the core-fit input, σ₀ and v\*, m_φ ~ m_χ, μ ≈ 20 keV, the Born caveat, the 300 and 1500 km/s numbers, the cluster statement; [§10](../../../notes/broken-born-theory.md#10-parameter-count) — the v0.1 parameter count; [§3](../../../notes/broken-born-theory.md#3-action) — the v0.1 amplitude
- [`notes/broken-born-theory.md`](../../../notes/broken-born-theory.md) 'Addendum (v0.3, overnight)' — the gate's carrier identified as X exchange
- [`wiki/papers/conjugate-special-relativity.md` §4](../../papers/conjugate-special-relativity.md#4-invariants-the-mass-shell-and-the-length-shell) — the definition of v\* reused
- [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md) items 17, 19 — the suspected √2 in μ between the two gate conventions; the regime of the classicality corollary; both pending; item 16 — the addendum that puts calc note #2's arithmetic in `verify/`; item 55 — the gate's mechanism not derived, pending
- [`notes/gate-mechanism.md` §5](../../../notes/gate-mechanism.md#5-what-follows-for-the-record) — the benchmark arithmetic needs no mechanism: σ₀/m = 32.0 cm²/g at 70 MeV, m = 71.5 MeV for 30 cm²/g, μ/m = 2.857×10⁻⁴, v\* = 121.1 km/s, v_a = 171.3 km/s; the strength open whatever the mechanism; [§1](../../../notes/gate-mechanism.md#1-the-question-and-what-the-record-says) — the two readings of μ ≈ 20 keV and v\* ≈ 120 km/s
- [`verify/gate_mechanism.py`](../../../verify/gate_mechanism.py) section D — the contact Born benchmark and the conventions; [`verify/velocity_gated_gravity.py`](../../../verify/velocity_gated_gravity.py) section D — calc note #2's coupling and shortfall ratios
