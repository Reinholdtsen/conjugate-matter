---
title: "The gated Vlasov model"
weight: 30
status: method
description: "The mean-field setup the clumping problem used: a Gaussian gate on a contact interaction, with linear response as an eigenproblem on momentum space bracketed by two solvable limits; the retired 'γ vs Ω' framing."
sources:
  - "notes/stream-stability.md 'Setup'"
  - "notes/stream-stability.md 'Limit 1 (broad gate)'"
  - "notes/stream-stability.md 'Limit 2 (narrow gate)'"
  - "notes/stream-stability.md 'Next chunk (3b)'"
  - "notes/wave-island.md 'Setup'"
  - "notes/wave-island.md 'What pins g? Two scenarios'"
  - "notes/broken-born-theory.md §5.1"
  - "notes/broken-born-theory.md §5.2"
  - "notes/broken-born-theory.md §11 item 3"
  - "papers/broken-born-checkpoint-v2.md §8"
  - "papers/broken-born-checkpoint-v2.md §14 item 4"
  - "review/wiki-build-flags.md items 17, 55, 58"
  - "notes/velocity-gated-gravity.md §4"
  - "notes/gate-mechanism.md §5"
---

*The gated Vlasov model is the simplified description of dark matter that [the clumping problem](/wiki/history/main-problems) used to test [velocity clumping](/wiki/dark-matter/momentum-clumping/founding-image). Dark matter is treated as a smooth gas in position and momentum. Besides gravity, each particle feels an attraction only from neighbours whose momentum lies within a narrow window around its own, the [velocity gate](/wiki/dark-matter/conjugate-matter/velocity-gate), and the attraction's range in space is shrunk to a point. Whether a small ripple in this gas grows then becomes an eigenvalue problem on momentum space, which the calculation brackets between a broad-gate limit and a narrow-gate limit instead of solving in general. The model also retired the earlier plan to race the growth of streams against orbital stirring, because below the threshold there is no growth to race.*

**Status:** Method — the setup of `notes/stream-stability.md`, which carries no tag of its own; it rests on standard [Vlasov stability theory](/wiki/dark-matter/momentum-clumping/vlasov-stability) [T]. Its Gaussian gate is an assumption, since [the gate's shape](/wiki/dark-matter/conjugate-matter/gate-shape) is open ([#11](/wiki/history/documents/checkpoint) §14 item 4). The earlier "γ vs Ω" framing that it retired is superseded; see [the folded section below](#superseded-racing-stream-growth-against-orbital-stirring).

## What the model is

The clumping problem's first note, [#2](/wiki/history/documents/clumping-notes), opens: "Nonrelativistic mean-field (Vlasov) limit of the gated interaction." The dark-matter particles χ, of mass m, are described by a phase-space distribution f(x, p), which evolves by the Vlasov equation. Every particle moves with the single-particle energy (#2, Setup)

```text
ε(x, p) = p²/2m + mΦ_grav(x) − g ∫d³p′ G((p − p′)/μ) f(x, p′),
g ≡ 4πα̃/m_φ² = √(πσ₀/m²)
```

with "G the Gaussian gate, G(0)=1, attractive sign, and the x-range collapsed to contact (range 1/m_φ, microscopic)". Term by term:

- **p²/2m** is the kinetic energy.
- **mΦ_grav(x)** is ordinary gravity. The program's dark matter falls like everything else: χ "propagates on g (equivalence principle; Bullet-Cluster-safe)" (#11 §8; [the equivalence principle](/wiki/gravity/spin-2-fields/equivalence-principle); [the Bullet Cluster](/wiki/dark-matter/halo-astrophysics/bullet-cluster)), where g in that quotation is the spacetime metric.
- **The gated term** is the new physics. At the point x it adds up the particles present there, weighted by G((p − p′)/μ), which equals 1 when their momentum p′ matches the particle's own momentum p and falls off once the two differ by more than about μ. The minus sign makes the force attractive. Because the interaction's range 1/m_φ is microscopic, on the scale of a galaxy it acts only between particles at the same place: a contact interaction in position, with a window in momentum.

The window is the [velocity gate](/wiki/dark-matter/conjugate-matter/velocity-gate). Its width is μ in momentum; #3 restates it as "gate width v\* in relative velocity" (#3, Setup). The [lab notebook](/wiki/history/documents/lab-notebook) relates the two as v\* ≡ √2μ/m_χ (`notes/broken-born-theory.md` §5.1), a relation that #11 does not restate. The notebook wrote it for its own gate, e^{−k²/μ²}; a suspected factor of √2 in μ between the sources' gate conventions is recorded for a ruling in `review/wiki-build-flags.md` item 17 ([two conventions](/wiki/dark-matter/conjugate-matter/velocity-gate#two-conventions-not-reconciled)).

**The coupling g.** Its first form uses the coupling α̃ and the mediator mass m_φ of the gated scattering amplitude (#11 §8; [the scattering law](/wiki/dark-matter/conjugate-matter/scattering-law)). Its second form expresses it through σ₀, the [momentum-transfer cross-section](/wiki/dark-matter/halo-astrophysics/transfer-cross-section) at low velocity, which is what observations of dwarf-galaxy cores constrain. #3 restates the same relation as "σ₀ ≡ g²m²/π" (#3, Setup). Because the strength of a contact interaction is an energy times a volume, g carries the units GeV⁻² in the natural units of the notes, as in #3's "g ≳ … ~ 10⁻³¹ GeV⁻²" (#3, 'The rate'). At the [scattering benchmark](/wiki/dark-matter/conjugate-matter/benchmark), the fit to dwarf cores fixes σ₀/m and with it g; #2 says g is then "determined".

**What the gate does to motion.** Because the gated term depends on p, the particle velocity ẋ = ∇ₚε contains more than p/m. The lab notebook wrote the same structure as ε(p; f) = p²/2m_χ + ∫d³p′ U(p − p′) f̄(p′) with ẋ ⊃ ∇ₚε, "an anomalous velocity, the same structure as Berry-curvature transport in solids" (`notes/broken-born-theory.md` §5.2).

## Linear response: an eigenvalue problem on momentum space

The stability test follows the textbook route on the [Vlasov stability](/wiki/dark-matter/momentum-clumping/vlasov-stability) page. #2 linearizes "about a homogeneous Maxwellian f₀(p) of dispersion σ; perturbations δf ∝ e^{i(k·x − ωt)}". The linearized Vlasov equation gives δf = −(k·∇ₚf₀) δε/(ω − k·v) [T]. The gated term turns this density change back into an energy change, δε(p) = −g ∫d³p′ G δf(p′), and the two together give (#2, Setup)

```text
δε(p) = g ∫d³p′ G(p − p′) [k·∇_{p′} f₀ / (ω − k·v′)] δε(p′)
```

#2 prints only this result; the substitution between the two steps is the standard one [T]. Here k is a wavevector and ω a frequency, v′ = p′/m, and the gate's width μ is left implicit in G.

#2's comment: "An eigenvalue problem (the "potential" lives on momentum space), not a scalar dispersion relation. Two solvable limits bracket it."

The difference from the textbook case is this. For gravity or a plain contact force, every particle at a point feels the same energy change, so δε is a single number for each plane wave and the self-consistency condition is one scalar equation. With the gate, each particle feels only its momentum neighbours, so δε(p) is a function on momentum space. The equation above is then a homogeneous linear integral equation for that function, and a mode exists at (k, ω) when the integral operator on the right has eigenvalue 1. Solving it in general would mean finding the spectrum of that operator for every (k, ω). #2 does not attempt this; it brackets the problem between two limits in which it can be solved.

## The two solvable limits

The limits compare the gate width μ with the thermal [momentum spread](/wiki/dark-matter/halo-astrophysics/velocity-dispersion#the-particle-island-the-stream-criterion) mσ of the gas.

### Broad gate: μ ≫ mσ (the dwarf regime)

The gate is much wider than the spread of momenta in the gas, so G ≈ 1 for every pair of particles that matter, and the gate drops out. In #2's words: "G → 1, δε constant, scalar relation." The eigenvalue problem collapses to the scalar dispersion relation of a contact attraction, whose threshold follows from "standard plasma-function algebra". #2 labels this the dwarf regime, where the velocity dispersion is small.

### Narrow gate: μ ≪ mσ (the Milky Way and cluster regime)

The gate is much narrower than the spread. #2: "Patch modes: δε supported on a momentum ball of radius ~μ." A mode then lives on a small patch of momentum space: only the "co-movers", the particles inside the patch, take part, and the spread that resists clumping is the patch's own internal spread v\*, not the halo's σ. #2 obtains this limit with the "Same algebra", substituting n → n_gate and σ → v\*. #2 labels it the "MW/cluster regime", the Milky Way and galaxy clusters, where velocity dispersions are large.

The second substitution is flagged. The momentum-gravity investigation of 2026-10-27 and 2026-10-28 found that σ → v\* "is the threshold of a cold stream that already exists, not of a smooth halo"; linearized about the halo, the threshold keeps the halo's dispersion, g·n·Λ_g ≥ m·σ², with Λ_g the gate's top eigenvalue. In the Milky Way #2's form overstates the shortfall about 3×, and the verdict is unchanged (`notes/velocity-gated-gravity.md` §4; flag 58 in `review/wiki-build-flags.md`; [the narrow-gate form, flagged](/wiki/dark-matter/momentum-clumping/instability-criterion#the-narrow-gate-form-flagged)).

### What the bracket provides

Neither limit is the general case, and the intermediate regime μ ~ mσ is not solved. #2 merges the two limits into one criterion, "ε_gate ≳ m·min(σ, v\*)²", in which the smaller of the thermal spread and the gate width sets the kinetic-energy scale that the attraction has to overcome. The thresholds and their evaluation at the benchmark are on [the mean-field criterion](/wiki/dark-matter/momentum-clumping/instability-criterion) page.

## Assumptions

- **Mean field, no collisions.** The Vlasov equation keeps only the averaged field. Collisions are treated separately, by the H-theorem argument on the criterion page.
- **Nonrelativistic** motion, as #2 states.
- **Classical particles.** f is a classical phase-space density, which describes the gas only while few particles share each quantum state. [The classicality theorem](/wiki/dark-matter/momentum-clumping/classicality-theorem) shows that the model's own threshold can be met only far outside this regime.
- **A homogeneous Maxwellian background** of dispersion σ, as stated in the Setup.
- **A Gaussian gate.** #11 §8 derives the gate's mechanism, exchange of the [momentum graviton X](/wiki/gravity/momentum-graviton) between particles whose momentum-space wavepackets overlap, with μ "the χ quantum's intrinsic momentum-fiber width", and tags it "[D — mechanism; shape [O]]". `notes/gate-mechanism.md` (2026-10-28; two derivations, the second blind; not reviewed) finds that exchanging #11 §7's X cannot produce the gate, and flag 55 in `review/wiki-build-flags.md` proposes [P] for the gate and μ and [O] for the mechanism, pending Paul's ruling; #11 is unchanged ([the gate mechanism](/wiki/dark-matter/conjugate-matter/gate-mechanism#exchanging-x-cannot-produce-the-gate)). The model takes the gate G as given and does not use the mechanism (the wiki's reading). #11 §14 item 4 keeps the shape open: "Gate shape (X propagator on momentum fibers; Gaussian vs rational — now observable) [O]" ([the gate mechanism](/wiki/dark-matter/conjugate-matter/gate-mechanism), [the gate shape](/wiki/dark-matter/conjugate-matter/gate-shape)).
- **Contact range** in position, from the microscopic mediator range 1/m_φ.

## Carried to the wave island

The second note, #3, keeps the conventions: "Same conventions as Chunk A: σ₀ ≡ g²m²/π, gate width v\* in relative velocity" (#3, Setup). On the [wave island](/wiki/dark-matter/momentum-clumping/wave-island) the classical Vlasov description is replaced by [wave kinetics](/wiki/dark-matter/wave-dark-matter/wave-kinetics), "the Boltzmann collision integral with Bose enhancement", and the stability threshold is replaced by a condensation rate, [Γ_self](/wiki/dark-matter/momentum-clumping/wave-island/condensation-rate). #3 also reuses this page's mean-field parameter under the name X ≡ gn/(mσ²), "the Chunk-A mean-field parameter", in [Scenario B](/wiki/dark-matter/momentum-clumping/wave-island/scenario-b).

## Superseded: racing stream growth against orbital stirring

**The old framing.** Before the clumping problem, the lab notebook took the instability for granted and asked only whether streams would grow faster than a galaxy's orbits could smear them out. §5.2: "The growth rate γ versus orbital phase-mixing remains to be computed; it is the theory's most important undone calculation on the astrophysics side. **[O]**". Its open-problem list repeats it as item 3: "Stream-instability growth rate γ vs. orbital phase-mixing: determines whether Prediction 3's granularity survives in Milky-Way-like halos." (`notes/broken-born-theory.md` §11; Prediction 3 is [velocity-space granularity](/wiki/dark-matter/momentum-clumping/velocity-granularity), now dead). Here γ is a growth rate and Ω an orbital stirring rate; orbital phase mixing is the spreading-out of structure as particles on orbits of slightly different period drift apart in phase [T].

**Why it was retired.** #2 found that below the threshold there is no growth at all, so there is nothing to race: "Below threshold: Landau-damped, stable. There is no race with orbital stirring below threshold — the flocking never starts. The earlier "γ vs Ω" framing presumed growth exists; it exists only above this line." (#2, Limit 1). Since the threshold is missed by 28–31 orders of magnitude at the benchmark, the question the notebook ranked first on the astrophysics side was answered by the threshold alone.

**Where the comparison returned.** On the wave island the race reappears in a different form, as the condensation rate against the stirring rate: "Streams need the much harder Γ_self ≳ Ω = 1/t_dyn" (#3, 'What pins g? Two scenarios'), where t_dyn is the dynamical time. #2 had already set this up as the next task: "Γ_cond(m, g, v\*; ρ, σ), compared to orbital stirring Ω per environment" (#2, 'Next chunk (#3)').

## Symbol collisions

- g is the gated coupling, in GeV⁻²; elsewhere in the wiki g is the spacetime metric.
- G is the gate here; in #3's gravity formulas it is Newton's constant.
- ω and k are a frequency and a wavevector; elsewhere ω is the [symplectic form](/wiki/phase-space/reciprocity/symplectic-form) and k the gate variable of the scattering law, the incoming relative momentum.
- σ is a velocity dispersion; σ₀ is a cross-section.
- X ≡ gn/(mσ²) in #3 is unrelated to the momentum graviton X, and Ω = 1/t_dyn is unrelated to a density parameter Ω_χ.
- See [notation](/wiki/notation).

## Sources

- `notes/stream-stability.md` 'Setup' — the energy, the linearization and the eigenvalue problem
- `notes/stream-stability.md` 'Limit 1 — broad gate' and 'Limit 2 — narrow gate' — the bracketing limits and the unified criterion; the retirement of "γ vs Ω"
- `notes/stream-stability.md` 'Next chunk (#3)' — the rate-versus-stirring comparison handed to #3
- `notes/wave-island.md` 'Setup' — the conventions carried to the wave island; 'What pins g? Two scenarios' — Γ_self ≳ Ω and the parameter X
- `papers/broken-born-checkpoint-v2.md` §8 — the gate's mechanism and the equivalence principle; §14 item 4 — the open gate shape
- `notes/broken-born-theory.md` §5.1 — v\* ≡ √2μ/m_χ; §5.2 — the anomalous velocity and the γ-versus-phase-mixing problem; §11 item 3 — the original open problem
- `review/wiki-build-flags.md` item 17 — the suspected √2 in μ between the gate conventions; item 55 — the gate's mechanism not derived; item 58 — the narrow-gate substitution σ → v\*; all awaiting a ruling
- `notes/velocity-gated-gravity.md` §4 — #2's narrow-gate criterion, linearized
- `notes/gate-mechanism.md` §5 — the proposed tags
