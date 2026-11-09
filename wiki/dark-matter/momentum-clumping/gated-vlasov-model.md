---
title: "The gated Vlasov model"
weight: 30
status: method
description: "The mean-field setup the clumping problem used: a Gaussian gate on a contact interaction, with linear response as an eigenproblem on momentum space bracketed by two solvable limits; the superseded 'γ vs Ω' framing."
sources:
  - "notes/stream-stability.md 'Setup'"
  - "notes/stream-stability.md 'Limit 1 — broad gate'"
  - "notes/stream-stability.md 'Limit 2 — narrow gate'"
  - "notes/stream-stability.md 'Next chunk (3b)'"
  - "notes/wave-island.md 'Setup'"
  - "notes/wave-island.md 'What pins g? Two scenarios'"
  - "notes/broken-born-theory.md §5.1"
  - "notes/broken-born-theory.md §5.2"
  - "notes/broken-born-theory.md §11 item 3"
  - "wiki/papers/broken-born-checkpoint-v2.md §8"
  - "wiki/papers/broken-born-checkpoint-v2.md §14 item 4"
  - "wiki/papers/broken-born-checkpoint-v2.md §13"
  - "review/wiki-build-flags.md items 17, 55, 58"
  - "notes/velocity-gated-gravity.md §4"
  - "notes/gate-mechanism.md §5"
---

*The gated Vlasov model is the simplified description of dark matter that [the clumping problem](../../history/main-problems.md) used to test [velocity clumping](founding-image.md). Dark matter is treated as a smooth gas in position and momentum. Besides gravity, each particle feels an attraction only from neighbours whose momentum lies within a narrow window around its own, the [velocity gate](../conjugate-matter/velocity-gate.md), and the attraction's range in space is shrunk to a point. Whether a small ripple in this gas grows then becomes an eigenvalue problem on momentum space, which the calculation brackets between a broad-gate limit and a narrow-gate limit instead of solving in general. The model also superseded the earlier plan to race the growth of streams against orbital stirring, because below the threshold there is no growth to race.*

**Status:** Method — the setup of [`notes/stream-stability.md`](../../../notes/stream-stability.md), which carries no tag of its own; it rests on standard [Vlasov stability theory](vlasov-stability.md) [T]. Its Gaussian gate is an assumption, since [the gate's shape](../conjugate-matter/gate-shape.md) is open ([#11](../../history/documents/checkpoint.md) [§14 item 4](../../papers/broken-born-checkpoint-v2.md#14-open-problems)). The earlier "γ vs Ω" framing is superseded; see [the folded section below](#superseded-racing-stream-growth-against-orbital-stirring).

## What the model is

The clumping problem's first note, [#2](../../history/documents/clumping-notes.md), opens: "Nonrelativistic mean-field (Vlasov) limit of the gated interaction." The dark-matter particles χ, of mass m, are described by a phase-space distribution f(x, p), which evolves by the Vlasov equation. Every particle moves with the single-particle energy ([#2](../../../notes/stream-stability.md), Setup)

```text
ε(x, p) = p²/2m + mΦ_grav(x) − g ∫d³p′ G((p − p′)/μ) f(x, p′),
g ≡ 4πα̃/m_φ² = √(πσ₀/m²)
```

with "G the Gaussian gate, G(0)=1, attractive sign, and the x-range collapsed to contact (range 1/m_φ, microscopic)". Term by term:

- **p²/2m** is the kinetic energy.
- **mΦ_grav(x)** is ordinary gravity. The program's dark matter falls like everything else: χ "propagates on g (equivalence principle; Bullet-Cluster-safe)" ([#11 §8](../../papers/broken-born-checkpoint-v2.md#8-conjugate-matter-and-the-gate); [the equivalence principle](../../gravity/spin-2-fields/equivalence-principle.md); [the Bullet Cluster](../halo-astrophysics/bullet-cluster.md)), where g in that quotation is the spacetime metric.
- **The gated term** is the new physics. At the point x it adds up the particles present there, weighted by G((p − p′)/μ), which equals 1 when their momentum p′ matches the particle's own momentum p and falls off once the two differ by more than about μ. The minus sign makes the force attractive. Because the interaction's range 1/m_φ is microscopic, on the scale of a galaxy it acts only between particles at the same place: a contact interaction in position, with a window in momentum.

The window is the [velocity gate](../conjugate-matter/velocity-gate.md). Its width is μ in momentum; [#3](../../../notes/wave-island.md) restates it as "gate width v\* in relative velocity" (#3, Setup). The [lab notebook](../../history/documents/lab-notebook.md) relates the two as v\* ≡ √2μ/m_χ ([`notes/broken-born-theory.md` §5.1](../../../notes/broken-born-theory.md#51-the-scattering-law-d)), a relation that #11 does not restate. The notebook wrote it for its own gate, e^{−k²/μ²}; a suspected factor of √2 in μ between the sources' gate conventions is recorded in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md) item 17 ([two conventions](../conjugate-matter/velocity-gate.md#two-conventions-not-reconciled)).

**The coupling g.** Its first form uses the coupling α̃ and the mediator mass m_φ of the gated scattering amplitude ([#11 §8](../../papers/broken-born-checkpoint-v2.md#8-conjugate-matter-and-the-gate); [the scattering law](../conjugate-matter/scattering-law.md)). Its second form expresses it through σ₀, the [momentum-transfer cross-section](../halo-astrophysics/transfer-cross-section.md) at low velocity, which is what observations of dwarf-galaxy cores constrain. #3 restates the same relation as "σ₀ ≡ g²m²/π" (#3, Setup). Because the strength of a contact interaction is an energy times a volume, g carries the units GeV⁻² in the natural units of the notes, as in #3's "g ≳ … ~ 10⁻³¹ GeV⁻²" (#3, 'The rate'). At the [scattering benchmark](../conjugate-matter/benchmark.md), the fit to dwarf cores fixes σ₀/m and with it g; #2 says g is then "determined".

**What the gate does to motion.** Because the gated term depends on p, the particle velocity ẋ = ∇ₚε contains more than p/m. The lab notebook wrote the same structure as ε(p; f) = p²/2m_χ + ∫d³p′ U(p − p′) f̄(p′) with ẋ ⊃ ∇ₚε, "an anomalous velocity, the same structure as Berry-curvature transport in solids" ([`notes/broken-born-theory.md` §5.2](../../../notes/broken-born-theory.md#52-collective-behavior-clumping-in-momentum-space-d-at-mean-field-level-o-beyond)).

## Linear response: an eigenvalue problem on momentum space

The stability test follows the textbook route on the [Vlasov stability](vlasov-stability.md) page. #2 linearizes "about a homogeneous Maxwellian f₀(p) of dispersion σ; perturbations δf ∝ e^{i(k·x − ωt)}". The linearized Vlasov equation gives δf = −(k·∇ₚf₀) δε/(ω − k·v) [T]. The gated term turns this density change back into an energy change, δε(p) = −g ∫d³p′ G δf(p′), and the two together give (#2, Setup)

```text
δε(p) = g ∫d³p′ G(p − p′) [k·∇_{p′} f₀ / (ω − k·v′)] δε(p′)
```

#2 prints only this result; the substitution between the two steps is the standard one [T]. Here k is a wavevector and ω a frequency, v′ = p′/m, and the gate's width μ is left implicit in G.

#2's comment: "An eigenvalue problem (the "potential" lives on momentum space), not a scalar dispersion relation. Two solvable limits bracket it."

The difference from the textbook case is this. For gravity or a plain contact force, every particle at a point feels the same energy change, so δε is a single number for each plane wave and the self-consistency condition is one scalar equation. With the gate, each particle feels only its momentum neighbours, so δε(p) is a function on momentum space. The equation above is then a homogeneous linear integral equation for that function, and a mode exists at (k, ω) when the integral operator on the right has eigenvalue 1. Solving it in general would mean finding the spectrum of that operator for every (k, ω). #2 does not attempt this; it brackets the problem between two limits in which it can be solved.

## The two solvable limits

The limits compare the gate width μ with the thermal [momentum spread](../halo-astrophysics/velocity-dispersion.md#the-particle-island-the-stream-criterion) mσ of the gas.

### Broad gate: μ ≫ mσ (the dwarf regime)

The gate is much wider than the spread of momenta in the gas, so G ≈ 1 for every pair of particles that matter, and the gate drops out. In #2's words: "G → 1, δε constant, scalar relation." The eigenvalue problem collapses to the scalar dispersion relation of a contact attraction, whose threshold follows from "standard plasma-function algebra". #2 labels this the dwarf regime, where the velocity dispersion is small.

### Narrow gate: μ ≪ mσ (the Milky Way and cluster regime)

The gate is much narrower than the spread. #2: "Patch modes: δε supported on a momentum ball of radius ~μ." A mode then lives on a small patch of momentum space: only the "co-movers", the particles inside the patch, take part, and the spread that resists clumping is the patch's own internal spread v\*, not the halo's σ. #2 obtains this limit with the "Same algebra", substituting n → n_gate and σ → v\*. #2 labels it the "MW/cluster regime", the Milky Way and galaxy clusters, where velocity dispersions are large.

The second substitution is flagged. The momentum-gravity investigation of 2026-10-27 and 2026-10-28 found that σ → v\* "is the threshold of a cold stream that already exists, not of a smooth halo"; linearized about the halo, the threshold keeps the halo's dispersion, g·n·Λ_g ≥ m·σ², with Λ_g the gate's top eigenvalue. In the Milky Way #2's form overstates the shortfall about 3×, and the verdict is unchanged ([`notes/velocity-gated-gravity.md` §4](../../../notes/velocity-gated-gravity.md#4-what-the-obituary-covers); flag 58 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md); [the narrow-gate form, flagged](instability-criterion.md#the-narrow-gate-form-flagged)).

### What the bracket provides

Neither limit is the general case, and the intermediate regime μ ~ mσ is not solved. #2 merges the two limits into one criterion, "ε_gate ≳ m·min(σ, v\*)²", in which the smaller of the thermal spread and the gate width sets the kinetic-energy scale that the attraction has to overcome. The thresholds and their evaluation at the benchmark are on [the mean-field criterion](instability-criterion.md) page.

## Assumptions

- **Mean field, no collisions.** The Vlasov equation keeps only the averaged field. Collisions are treated separately, by the H-theorem argument on the criterion page.
- **Nonrelativistic** motion, as #2 states.
- **Classical particles.** f is a classical phase-space density, which describes the gas only while few particles share each quantum state. [The classicality theorem](classicality-theorem.md) shows that the model's own threshold can be met only far outside this regime.
- **A homogeneous Maxwellian background** of dispersion σ, as stated in the Setup.
- **A Gaussian gate.** [#11 §8](../../papers/broken-born-checkpoint-v2.md#8-conjugate-matter-and-the-gate) states the gate's mechanism, exchange of the [momentum graviton X](../../gravity/momentum-graviton/_index.md) between particles whose momentum-space wavepackets overlap, with μ "the χ quantum's intrinsic momentum-fiber width", and tags it "[D — mechanism; shape [O]]". [`notes/gate-mechanism.md`](../../../notes/gate-mechanism.md) (2026-10-28; two derivations, the second blind; not reviewed) finds that exchanging [#11 §7](../../papers/broken-born-checkpoint-v2.md#7-the-massive-momentum-graviton)'s X cannot produce the gate, and flag 55 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md) (pending) proposes [P] for the gate and μ and [O] for the mechanism ([the gate mechanism](../conjugate-matter/gate-mechanism.md#exchanging-x-cannot-produce-the-gate)). The model takes the gate G as given and does not use the mechanism (the wiki's reading). [#11 §14 item 4](../../papers/broken-born-checkpoint-v2.md#14-open-problems) keeps the shape open: "Gate shape (X propagator on momentum fibers; Gaussian vs rational — now observable) [O]" ([the gate mechanism](../conjugate-matter/gate-mechanism.md), [the gate shape](../conjugate-matter/gate-shape.md)).
- **Contact range** in position, from the microscopic mediator range 1/m_φ.

## Carried to the wave island

The second note, #3, keeps the conventions: "Same conventions as Chunk A: σ₀ ≡ g²m²/π, gate width v\* in relative velocity" (#3, Setup). On the [wave island](wave-island/_index.md) the classical Vlasov description is replaced by [wave kinetics](../wave-dark-matter/wave-kinetics.md), "the Boltzmann collision integral with Bose enhancement", and the stability threshold is replaced by a condensation rate, [Γ_self](wave-island/condensation-rate.md). #3 also reuses this page's mean-field parameter under the name X ≡ gn/(mσ²), "the Chunk-A mean-field parameter", in [Scenario B](wave-island/scenario-b.md).

## Superseded: racing stream growth against orbital stirring

**The old framing.** Before the clumping problem, the lab notebook took the instability for granted and asked only whether streams would grow faster than a galaxy's orbits could smear them out. [§5.2](../../../notes/broken-born-theory.md#52-collective-behavior-clumping-in-momentum-space-d-at-mean-field-level-o-beyond): "The growth rate γ versus orbital phase-mixing remains to be computed; it is the theory's most important undone calculation on the astrophysics side. **[O]**". Its open-problem list repeats it as item 3: "Stream-instability growth rate γ vs. orbital phase-mixing: determines whether Prediction 3's granularity survives in Milky-Way-like halos." ([`notes/broken-born-theory.md` §11](../../../notes/broken-born-theory.md#11-open-problems-in-order-of-severity); Prediction 3 is [velocity-space granularity](velocity-granularity.md), withdrawn and under review, [#11 §13](../../papers/broken-born-checkpoint-v2.md#13-predictions-and-kill-conditions)). Here γ is a growth rate and Ω an orbital stirring rate; orbital phase mixing is the spreading-out of structure as particles on orbits of slightly different period drift apart in phase [T].

**Why it is superseded.** #2 found that below the threshold there is no growth at all, so there is nothing to race: "Below threshold: Landau-damped, stable. There is no race with orbital stirring below threshold — the flocking never starts. The earlier "γ vs Ω" framing presumed growth exists; it exists only above this line." (#2, Limit 1). Since the threshold is missed by 28–31 orders of magnitude at the benchmark, the question the notebook ranked first on the astrophysics side was answered by the threshold alone.

**Where the comparison returned.** On the wave island the race reappears in a different form, as the condensation rate against the stirring rate: "Streams need the much harder Γ_self ≳ Ω = 1/t_dyn" (#3, 'What pins g? Two scenarios'), where t_dyn is the dynamical time. #2 had already set this up as the next task: "Γ_cond(m, g, v\*; ρ, σ), compared to orbital stirring Ω per environment" (#2, 'Next chunk (3b)').

## Symbol collisions

- g is the gated coupling, in GeV⁻²; elsewhere in the wiki g is the spacetime metric.
- G is the gate here; in #3's gravity formulas it is Newton's constant.
- ω and k are a frequency and a wavevector; elsewhere ω is the [symplectic form](../../phase-space/reciprocity/symplectic-form.md) and k the gate variable of the scattering law, the incoming relative momentum.
- σ is a velocity dispersion; σ₀ is a cross-section.
- X ≡ gn/(mσ²) in #3 is unrelated to the momentum graviton X, and Ω = 1/t_dyn is unrelated to a density parameter Ω_χ.
- See [notation](../../notation.md).

## Sources

- [`notes/stream-stability.md`](../../../notes/stream-stability.md) 'Setup' — the energy, the linearization and the eigenvalue problem
- [`notes/stream-stability.md`](../../../notes/stream-stability.md) 'Limit 1 — broad gate' and 'Limit 2 — narrow gate' — the bracketing limits and the unified criterion; why "γ vs Ω" is superseded
- [`notes/stream-stability.md`](../../../notes/stream-stability.md) 'Next chunk (3b)' — the rate-versus-stirring comparison handed to #3
- [`notes/wave-island.md`](../../../notes/wave-island.md) 'Setup' — the conventions carried to the wave island; 'What pins g? Two scenarios' — Γ_self ≳ Ω and the parameter X
- [`wiki/papers/broken-born-checkpoint-v2.md` §8](../../papers/broken-born-checkpoint-v2.md#8-conjugate-matter-and-the-gate) — the gate's mechanism and the equivalence principle; [§14 item 4](../../papers/broken-born-checkpoint-v2.md#14-open-problems) — the open gate shape; [§13](../../papers/broken-born-checkpoint-v2.md#13-predictions-and-kill-conditions) — the old row 3, withdrawn and under review
- [`notes/broken-born-theory.md` §5.1](../../../notes/broken-born-theory.md#51-the-scattering-law-d) — v\* ≡ √2μ/m_χ; [§5.2](../../../notes/broken-born-theory.md#52-collective-behavior-clumping-in-momentum-space-d-at-mean-field-level-o-beyond) — the anomalous velocity and the γ-versus-phase-mixing problem; [§11 item 3](../../../notes/broken-born-theory.md#11-open-problems-in-order-of-severity) — the original open problem
- [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md) item 17 — the suspected √2 in μ between the gate conventions; item 55 — the gate's mechanism not derived; item 58 — the narrow-gate substitution σ → v\*; all pending
- [`notes/velocity-gated-gravity.md` §4](../../../notes/velocity-gated-gravity.md#4-what-the-obituary-covers) — #2's narrow-gate criterion, linearized
- [`notes/gate-mechanism.md` §5](../../../notes/gate-mechanism.md#5-what-follows-for-the-record) — the proposed tags
