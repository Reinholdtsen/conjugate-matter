---
title: "P5: the vacuum selects a polarization"
weight: 70
status: alive
description: "Our vacuum is x-tilted and the mirror vacuum is equally lawful; Freidel–Leigh–Minic stated the preferred-polarization idea, and the toy models add that selection needs a potential."
provenance: [P]
sources:
  - "wiki/papers/broken-born-checkpoint-v2.md §3"
  - "wiki/papers/broken-born-checkpoint-v2.md §4"
  - "wiki/papers/broken-born-checkpoint-v2.md §10"
  - "wiki/papers/broken-born-checkpoint-v2.md §14 item 11"
  - "notes/broken-born-theory.md §1"
  - "notes/broken-born-theory.md §2"
  - "notes/broken-born-theory.md §8"
  - "notes/broken-born-program-v1.md §2"
  - "notes/geometric-core.md §B"
  - "wiki/papers/reciprocity-toy-models.md §1"
  - "wiki/papers/reciprocity-toy-models.md §2"
  - "wiki/papers/reciprocity-toy-models.md §3"
  - "wiki/papers/reciprocity-toy-models.md §4"
  - "wiki/papers/reciprocity-toy-models.md §6"
  - "notes/toy-lagrangian.md 'Chunk 2 results (2026-10-19): the Grosse–Wulkenhaar route'"
  - "notes/toy-lagrangian.md 'Chunk 3 results (2026-10-19): S4, quantum stability'"
  - "review/round4-adjudication.md 'Rulings' F4"
  - "verify/toy_coset.py S2"
  - "verify/toy_s4.py"
  - "verify/toy_gw.py"
  - "CLAUDE.md 'Since the handoff'"
  - "popsci/universes-other-half.md 'An asymmetry that cannot be avoided'"
  - "notes/closed-universe.md §5"
  - "notes/dual-sector.md §8"
  - "review/wiki-build-flags.md item 70"
---

*P5 is the program's axiom of spontaneous breaking: the vacuum of the universe selects a polarization, a choice of which half of the phase-space directions count as position, and ours is the one organized around position in the ordinary sense ("x-tilted"). The mirror choice, a vacuum organized around momentum, satisfies the same laws equally well, because the [reciprocity symmetry](../../phase-space/reciprocity/born-reciprocity.md) of P3 carries one onto the other. Which one occurs is a property of the state, not of the laws, as the axes of an ice crystal belong to the crystal rather than to the laws governing water. Freidel, Leigh and Minic had already described a preferred polarization as breaking Born's symmetry, and a later paper of theirs places a breaking tied to that choice in the vacuum, though for another symmetry; the program's addition is to treat the choice as the spontaneous breaking of Born's symmetry itself, with an order parameter. The toy models qualify the axiom: with only the symplectic form fixed, the choice is a continuous angle, like an ice axis that could point anywhere, and a definite polarization needs an additional potential on that angle.*

**Status:** Alive — [P] — a postulate of [#11](../../history/documents/checkpoint.md) [§4](../../papers/broken-born-checkpoint-v2.md#4-postulates). The toy models show a consistent realization, not a test: in model I with a bounded ρ-preserving potential, the frozen-H reduction has an ordered ℤ₂ phase in 1+1 dimensions (Monte Carlo, [`verify/toy_s4.py`](../../../verify/toy_s4.py), [the toy-model scripts](../../method/verification/toy-model-scripts.md)). That ours is the x-tilted vacuum is postulated, not derived.

## Statement

```text
P5  The vacuum selects a polarization; ours is x-tilted; the mirror
    vacuum is equally lawful.                                      [P]
```

This is [#11 §4](../../papers/broken-born-checkpoint-v2.md#4-postulates)'s text, the same as the program paper v1's "P5 (Spontaneous breaking)" ([#9 §2](../../../notes/broken-born-program-v1.md#2-postulates--including-the-one-the-mathematics-rejected)). The [lab notebook](../../history/documents/lab-notebook.md)'s first version reads:

> **P5 (Spontaneous breaking).** The vacuum selects a Lagrangian polarization of 𝒫; ours is x-tilted. The choice is spontaneous: the mirror vacuum is an equally good solution. **[P]** ([#1 §1](../../../notes/broken-born-theory.md#1-postulates))

The axiom makes three claims: the vacuum selects a polarization; ours is the x-tilted one; and the mirror vacuum is equally lawful. The first has an argument behind it, the third follows from [P3](p3-reciprocity.md), and the second is a statement of fact about our universe that the program assumes.

## What is selected: a Lagrangian polarization

A Lagrangian subspace of phase space is a subspace of half the dimension on which the [symplectic form](../../phase-space/reciprocity/symplectic-form.md) ω vanishes; the pure-position directions (p = 0) and the pure-momentum directions (x = 0) are the standard examples [T]. A polarization takes one such subspace as the "position" directions, the variables in which states are written [T] ([Lagrangian polarizations](../../phase-space/reciprocity/lagrangian-polarizations.md)); in the program they are also the variables in which interactions are local ([#11 §3](../../papers/broken-born-checkpoint-v2.md#3-the-question)). The x-polarization writes a quantum state as a waveform ψ(x); the p-polarization writes the same state as its spectrum ψ̃(p), and the [Fourier transform](../../phase-space/reciprocity/fourier-transform.md) converts one into the other.

The possible choices form [the Lagrangian Grassmannian](../../phase-space/modular-field/lagrangian-grassmannian.md): "The space of Lagrangian polarizations of ℝ²ᵈ is the Lagrangian Grassmannian Λ(d) ≅ U(d)/O(d), compact, of dimension d(d+1)/2 = 10 for d = 4. **[T]** Its fundamental group is π₁(Λ(d)) = ℤ, generated by the **Maslov circle**" ([#1 §2](../../../notes/broken-born-theory.md#2-kinematic-core)). Under [P2′](p2-prime.md) the vacuum's choice ranges over all of it: the vacuum selects a real structure J, and "{J} ≅ U(d)/O(d) = Λ(d)" ([#5 §B](../../../notes/geometric-core.md#b-the-inconsistency-and-the-forced-repair-d--structural)). In the one-dimensional [toy models](../../symmetry-breaking/toy-models/_index.md) (d = 1) the choice is a real structure K, which defines the [neutral metric](../../phase-space/born-geometry/born-structures.md) η = ωK: "Its null lines are the two eigenlines L± of K, which are Lagrangian. Choosing K is choosing which line is 'position'" ([toy note §1](../../papers/reciprocity-toy-models.md#1-setting-and-prior-work)).

## Why a choice is made at all

[#11 §3](../../papers/broken-born-checkpoint-v2.md#3-the-question) argues that some polarization must be selected: "The breaking is *mandatory*: [x,p] = iℏ forbids joint locality, so any world with local physics must select a Lagrangian polarization. The magnet must point." Because nothing can be sharp in both position and momentum ([the canonical commutator](../../phase-space/reciprocity/canonical-commutator.md)), a world whose interactions are local must be local in one variable at the cost of the other. The argument requires some polarization, not a particular one ([mandatory breaking](../../symmetry-breaking/mandatory-breaking.md)).

The [popular article](../../history/documents/popular-articles.md) [#12](../../../popsci/universes-other-half.md) illustrates the point with freezing water: the laws governing water single out no direction, yet a crystal has definite axes, so "The settling was compulsory, since the uncertainty principle allows no symmetric option; the particular outcome was not" (#12, 'An asymmetry that cannot be avoided'). That passage predates the v2.2 qualifications below, and the popular articles are not a source for a claim's status.

## Why the mirror vacuum is equally lawful

A symmetry of the action maps solutions of the field equations to solutions with the same action [T], so whatever ρ does to one vacuum yields another vacuum. P3 makes ρ such a symmetry. ρ also reverses the [order parameter](../../symmetry-breaking/order-parameter.md): at the standard forms it "preserves ω (it is symplectic), preserves H (it is orthogonal), and **flips the sign of η**" [D] ([#1 §2](../../../notes/broken-born-theory.md#2-kinematic-core)). So the image of the x-tilted vacuum is a different vacuum, organized around momentum, with exactly the same standing in the laws. This is what [spontaneous symmetry breaking](../../symmetry-breaking/spontaneous-symmetry-breaking.md) means: the laws keep the symmetry, and each ground state breaks it [T].

The [coset toy model](../../symmetry-breaking/toy-models/coset-model/_index.md) shows the structure explicitly. Its vacua at H = 1 are the real structures K(φ), and "ρ acts as Z → −1/Z and K(φ) → K(φ + π) = −K(φ)" ([toy note §2](../../papers/reciprocity-toy-models.md#2-model-i-a-coset-sigma-model-of-h-k)). [The gate](../../method/verification/the-gate.md) checks that ρ maps each vacuum (1, K(φ)) to the vacuum (1, −K(φ)), that no vacuum is ρ-invariant, and that the order parameter O = K₁₁ takes +1 in one vacuum and −1 in its image ([`verify/toy_coset.py`](../../../verify/toy_coset.py), parts S2–S3; [model I vacua](../../symmetry-breaking/toy-models/coset-model/vacua.md)).

What the axiom adds by hand is "ours is x-tilted". No source defines "x-tilted" beyond its use for our vacuum, the one organized around position. The lab notebook's sketch of polarization-genesis, which it tags [O, sketched], uses a "vacuum tilt angle" θ_pol, with Ω_χ/Ω_x^(0) ~ tan²θ_pol ([#1 §8](../../../notes/broken-born-theory.md#8-polarization-genesis-o-sketched)); the relation appears only in #1 and is unverified ([Open: polarization-genesis](../../dark-matter/candidates/polarization-genesis.md)).

**In a closed universe.** The closed-universe note of 2026-10-27 qualifies the mirror vacuum's standing if space is closed ([`notes/closed-universe.md` §5](../../../notes/closed-universe.md#5-reciprocity-on-a-closed-space); [reciprocity on a closed space](../../phase-space/reciprocity/closed-space-reciprocity.md)). On the phase space T\*S³ of a closed universe, only the position polarization is integrable; every tilt, the mirror momentum polarization θ = π/2 included, fails the Frobenius condition, while on a flat torus every tilt passes [D][V]. If the [section condition](../../symmetry-breaking/section-condition.md) requires integrability, the mirror vacuum has no global realization in a closed universe; the record does not state that requirement, and if polarizations that are not integrable are allowed, the mirror's energy cost is not computed [O]. The note marks the result as its critic's alone, not independently verified, and the note has not been reviewed.

## Credit: a preferred polarization

The idea that choosing a polarization breaks Born's symmetry is not the program's. [#11 §3](../../papers/broken-born-checkpoint-v2.md#3-the-question) says so: "the idea that a preferred polarization breaks Born duality is Freidel, Leigh and Minic's — 'if all probes agree on what we mean by space-time, then we have broken Born duality — there is a preferred choice of polarization, the space-time one' [26S, p. 3]. They treat the breaking as kinematical and call the choice 'a dynamical question'. This program's addition is to read it as *spontaneous* breaking, with η as the order parameter". The toy-model note's survey adds two neighbours: Freidel, Rudolph and Svoboda suggest the choice "might be subject to a dynamical selection rule" [2], and Born sigma models "choose the polarization by gauging [3]" ([toy note §1](../../papers/reciprocity-toy-models.md#1-setting-and-prior-work)). See [broken Born duality](../../phase-space/reciprocity/broken-born-duality.md).

In the metastring paper [26S] ([arXiv:1502.08005](https://arxiv.org/abs/1502.08005)) and in [Freidel, Leigh and Minic 2014](https://arxiv.org/abs/1405.3949) (Int. J. Mod. Phys. D), "kinematical" is their word for general relativity's split of phase space into space and momentum space, which they propose to make dynamical, and a later paper of theirs ([Freidel, Kowalski-Glikman, Leigh and Minic 2021](https://arxiv.org/abs/2104.00802)) places a symmetry breaking tied to the choice of polarization "at the level of the vacuum sector", for a dual Lorentz symmetry of their doubled phase space that is not ρ, with no potential or order parameter ([neighbours of broken Born duality](../../phase-space/reciprocity/broken-born-duality.md#neighbours-in-the-literature); [`notes/dual-sector.md` §8](../../../notes/dual-sector.md#8-the-vacuum-and-the-choice-of-polarization); flag 70, pending).

The equal standing of the other polarization, P5's third clause, is stated as well, as a symmetry of the theory, in papers by Minic and coauthors: "there is nothing special about the" x^μ, the ordinary space-time coordinates, and "we could have taken any linear subspace", such as (x̃, p), with x̃ the dual coordinates ([Freidel, Kowalski-Glikman, Leigh and Minic 2018](https://arxiv.org/abs/1812.10821), §2); and "we could have picked the dual" polarization ([Berglund, Hübsch and Minic 2023](https://arxiv.org/abs/2212.06086), §4.4). Calling the choice a vacuum is the program's ([`notes/dual-sector.md` §8](../../../notes/dual-sector.md#8-the-vacuum-and-the-choice-of-polarization); flag 70, pending).

## What the toy models add: an angle, and a potential to fix it

### The choice is a continuous angle

#11 v2.2 refines P2′: "with only ω rigid, ρ sits inside a continuous U(1), and the polarization is a Goldstone angle rather than a discrete choice [D][V]" ([#11 §4](../../papers/broken-born-checkpoint-v2.md#4-postulates); [the polarization as a Goldstone angle](../../symmetry-breaking/goldstone-angle.md)). In the coset model the vacua at fixed H form a circle, K(φ), and ρ moves each by π along it. The worklog drew the consequence for P5 when it found this: "P5's 'the vacuum selects a polarization; ours is x-tilted' needs explicit breaking of that U(1) — a potential on the circle — to make the selection definite" ('Chunk 2 results'). In the coset model the angle "parametrizes Λ(1): it is τ's circle", the circle of the program's dark-energy field, and #11 adds that "None of this tests the cosmology; it only shows the structure is consistent" ([#11 §10](../../papers/broken-born-checkpoint-v2.md#10-cosmology); [τ: hilltop quintessence on the Maslov circle](../../cosmology/dark-energy/tau-quintessence.md)).

### In 1+1 dimensions the angle cannot order by itself

The [Mermin–Wagner–Coleman theorem](../../symmetry-breaking/mermin-wagner-coleman.md) rules out the spontaneous breaking of a continuous compact symmetry in two dimensions [T]. The toy note applies it to the polarization angle: "In 1+1 the compact angle φ cannot order: Mermin–Wagner [13, 14] applies to the compact SO(2) containing ρ" ([toy note §4](../../papers/reciprocity-toy-models.md#4-quantum-stability)). Its references are Mermin and Wagner (1966) and Coleman (1973). The rest of model I is different: "The non-compact half-plane sector is a hyperbolic model, where symmetry breaking in 2D does occur [15]. Whether ρ's SO(2) stays unbroken in the full coupled model is open" ([toy note §4](../../papers/reciprocity-toy-models.md#4-quantum-stability)).

### With a ρ-preserving potential: an ordered ℤ₂ phase

To obtain a definite polarization the toy adds "a potential that is invariant under ρ and under K → −K, and reduces the U(1) to a discrete group". The bounded form V_b = −μ[Tr(K K_ref)]² / (2 Tr KᵀK) is stable with H dynamical, and at H = 1 it is V_b = −(μ/2)(1 + cos 2φ), with minima at K = ±K_ref, which ρ exchanges ([toy note §4](../../papers/reciprocity-toy-models.md#4-quantum-stability); [the bounded potential V_b](../../symmetry-breaking/toy-models/coset-model/bounded-potential.md)). The first form tried had been unbounded below once H moves ([Under review: the naive ρ-preserving potential](../../symmetry-breaking/toy-models/coset-model/naive-potential.md)).

The note then simulates "the lattice model E = −J Σ cos(φ_i − φ_j) − h Σ cos 2φ_i: model I's polarization angle at H = 1, with V_b up to a constant and normalization. H is not simulated." Here J is a lattice coupling, not the real structure. The sampler is checkerboard Metropolis from a cold start (φ = 0) on L × L lattices with L = 16, 32, 64, and each value is a mean with its standard error over four independent seeds. The order parameter for ρ is m = ⟨cos φ⟩, which changes sign under φ → φ + π ([toy note §4](../../papers/reciprocity-toy-models.md#4-quantum-stability); [the frozen-H reduction](../../symmetry-breaking/toy-models/coset-model/frozen-h-reduction.md); [Monte Carlo: an ordered ℤ₂ phase](../../symmetry-breaking/toy-models/coset-model/monte-carlo.md)):

| Run | Values at L = 16, 32, 64 | Reading |
|---|---|---|
| With the potential (J = h = 1), T = 0.6 | ⟨\|m\|⟩ = 0.954 ± 0.0001 at every size; Binder cumulant 0.667 | Ordered ℤ₂ phase |
| Control, T = 3.0 | ⟨\|m\|⟩ = 0.0653 ± 0.0043, 0.0338 ± 0.0013, 0.0155 ± 0.0004 | Scales as 1/L: disordered |
| No potential (h = 0), T = 0.6 | ⟨\|M\|⟩ = \|⟨e^{iφ}⟩\| = 0.8369 ± 0.0007, 0.8025 ± 0.0039, 0.7736 ± 0.0038; ratio 0.924 vs spin-wave (64/16)^{−T/4πJ} = 0.936 | No true order |

(Toy note §4, reproduced by [`verify/toy_s4.py`](../../../verify/toy_s4.py); on the first row's "at every size", see flag 13 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md).)

How to read the three rows:

- **With the potential** the order parameter does not shrink as the lattice grows, which is the mark of long-range order [T]. The Binder cumulant, a ratio of the fourth and second moments of m, is near 2/3 for an ordered phase with two vacua [T]; the gate checks "Binder cumulant near 2/3 (an ordered Z2 phase)".
- **The high-temperature control** falls as 1/L, the behaviour of a disordered system; it "shows the sampler does leave" the ordered start "when the phase is disordered" (worklog, 'Chunk 3 results').
- **Without the potential** the magnetization of the full U(1) decays with size, at a rate the note sets beside the spin-wave estimate (ratio 0.924 against 0.936). A two-dimensional system with a continuous symmetry shows such a decay when it has no true order [T]; the worklog reads it as "no true order, as Coleman–Mermin–Wagner requires" ('Chunk 3 results').

The note states the limits: "We call the first row an ordered ℤ₂ phase. We did not measure critical exponents", and "Hot starts at L = 64 coarsen slowly through metastable domains, so ordered-phase values are reported from cold starts" ([toy note §4](../../papers/reciprocity-toy-models.md#4-quantum-stability)). The model simulated is a reduction with H frozen. The program's rule for such cases is to check the unreduced model's stability as well, which V_b passes with H dynamical ([the reduced-model stability rule](../../method/verification/reduced-model-stability.md)), and to give Monte Carlo numbers error bars from independent runs ([the Monte Carlo error-bar rule](../../method/verification/monte-carlo-error-bars.md)).

### In the other toy, quantization undoes the selection

In the complex self-dual [Grosse–Wulkenhaar model](../../symmetry-breaking/toy-models/grosse-wulkenhaar/_index.md) (model II), the classical vacua do break the position–momentum duality: the relative phase β of two condensed levels is a flat direction, and the vacuum's position-versus-momentum polarization varies as Δ(β) = Δ(0) cos β ([toy note §3](../../papers/reciprocity-toy-models.md#3-model-ii-the-self-dual-grossewulkenhaar-model); [complex-model vacua](../../symmetry-breaking/toy-models/grosse-wulkenhaar/complex-vacua.md)). Quantum fluctuations restore the symmetry: "the quantum measure is uniform in β at every truncation, and ⟨Δ⟩ = 0. The classical breaking of §3 does not survive quantization" ([toy note §4](../../papers/reciprocity-toy-models.md#4-quantum-stability); [quantum restoration](../../symmetry-breaking/toy-models/grosse-wulkenhaar/quantum-restoration.md)). So in neither toy does P5's selection come for free from a duality-symmetric action: model I needs the added potential, and model II's classical selection does not survive quantization (worklog, 'Chunk 3 results', scorecard).

## Open: why position rather than momentum

P5 postulates that ours is the x-tilted vacuum. One computation in the toy models bears on that choice, and the record calls it a lead. In the real Grosse–Wulkenhaar model, where the duality is only a covariance, "The vacua are diag(±√q₀, ±√q₁). Up to the global sign, the two relative signs are classically degenerate (S = −2.5) but have different fluctuation spectra" ([toy note §3](../../papers/reciprocity-toy-models.md#3-model-ii-the-self-dual-grossewulkenhaar-model)). Their one-loop free energies differ:

```text
F(+) − F(−) = 2.634        the same at truncations N = 6, 8, 10        (toy note §3; verify/toy_gw.py)
```

"**The preferred vacuum, diag(a₀, −a₁), is the β = π configuration, the one sharper in position.**" The note qualifies it at once: "This is explicit, not spontaneous selection, because the real model is not duality-symmetric: its field is real in position. It holds at fixed bare μ², and is not followed through renormalization" ([toy note §3](../../papers/reciprocity-toy-models.md#3-model-ii-the-self-dual-grossewulkenhaar-model)). [Round-4](../../method/review/round-4.md) ruling F4 recorded it "as a lead, not a result", with its truncation dependence then unchecked ([`review/round4-adjudication.md`](../../../review/round4-adjudication.md)); version 2 of the note reports the same value at N = 6, 8, 10. [`CLAUDE.md`](../../../CLAUDE.md) lists "the real Grosse–Wulkenhaar model's one-loop preference for the position-sharp vacuum" as "a lead", and "the large-N, renormalized fate of the real model's one-loop selection" is listed under "Not shown" ([toy note §6](../../papers/reciprocity-toy-models.md#6-summary-and-limitations)). See [Open: the real model's one-loop preference](../../symmetry-breaking/toy-models/grosse-wulkenhaar/real-model-lead.md) and [open problems](../../status/open-problems.md).

## Open: what a derived selection still lacks

- **The potential's origin.** "a derivation of the ρ-preserving potential, which introduces a rigid, unordered pair of axes" is not shown ([toy note §6](../../papers/reciprocity-toy-models.md#6-summary-and-limitations)); [#11 §14 item 11](../../papers/broken-born-checkpoint-v2.md#14-open-problems) lists "a derivation of the potential" as open [O] ([Open: the origin of the ρ-preserving potential](../../symmetry-breaking/rho-preserving-potential.md)).
- **The unreduced model.** "a Monte Carlo with H dynamical" is open ([#11 §14 item 11](../../papers/broken-born-checkpoint-v2.md#14-open-problems); [Open: a Monte Carlo with H dynamical](../../symmetry-breaking/toy-models/coset-model/dynamical-h-monte-carlo.md)), and so is "whether ρ's SO(2) breaks in the coupled model without a potential" ([toy note §6](../../papers/reciprocity-toy-models.md#6-summary-and-limitations); [Open: does ρ's SO(2) break in the coupled model?](../../symmetry-breaking/toy-models/coset-model/so2-question.md)).
- **Higher dimension.** The toy work covers d = 1 in 1+1 dimensions; "anything beyond d = 1" is not shown ([toy note §6](../../papers/reciprocity-toy-models.md#6-summary-and-limitations)). The worklog adds a remark it did not compute: "In 3+1, the program's actual dimension, Coleman–Mermin–Wagner does not apply. There the self-dual coset model can break the continuous U(1) itself, with τ an exactly massless Goldstone", and "§10's τ has a potential, so the explicit breaking is in the program anyway" ('Chunk 3 results'). That remark is a conjecture of the worklog, not a result.

## Sources

- [`wiki/papers/broken-born-checkpoint-v2.md` §4](../../papers/broken-born-checkpoint-v2.md#4-postulates) — the statement and the Goldstone-angle refinement; [§3](../../papers/broken-born-checkpoint-v2.md#3-the-question) — mandatory breaking and the Freidel–Leigh–Minic credit; [§10](../../papers/broken-born-checkpoint-v2.md#10-cosmology) — the angle as τ's circle, consistency only; [§14 item 11](../../papers/broken-born-checkpoint-v2.md#14-open-problems) — what is open
- [`notes/broken-born-theory.md` §1](../../../notes/broken-born-theory.md#1-postulates) — the v0.1 statement; [§2](../../../notes/broken-born-theory.md#2-kinematic-core) — Λ(d) and how ρ acts on the structures; [§8](../../../notes/broken-born-theory.md#8-polarization-genesis-o-sketched) — the tilt angle in the polarization-genesis sketch
- [`notes/broken-born-program-v1.md` §2](../../../notes/broken-born-program-v1.md#2-postulates--including-the-one-the-mathematics-rejected) — the v1 statement
- [`notes/geometric-core.md` §B](../../../notes/geometric-core.md#b-the-inconsistency-and-the-forced-repair-d--structural) — the space of choices Λ(d) under P2′
- [`wiki/papers/reciprocity-toy-models.md` §1](../../papers/reciprocity-toy-models.md#1-setting-and-prior-work) — K and its eigenlines, prior work; [§2](../../papers/reciprocity-toy-models.md#2-model-i-a-coset-sigma-model-of-h-k) — model I's vacua and ρ; [§3](../../papers/reciprocity-toy-models.md#3-model-ii-the-self-dual-grossewulkenhaar-model) — model II's vacua and the real-model lead; [§4](../../papers/reciprocity-toy-models.md#4-quantum-stability) — Mermin–Wagner, the potential, the Monte Carlo and quantum restoration; [§6](../../papers/reciprocity-toy-models.md#6-summary-and-limitations) — what is not shown
- [`notes/toy-lagrangian.md`](../../../notes/toy-lagrangian.md) 'Chunk 2 results' — the consequence for P5; 'Chunk 3 results' — the 3+1 remark
- [`review/round4-adjudication.md`](../../../review/round4-adjudication.md) 'Rulings' F4 — the real-model preference recorded as a lead
- [`verify/toy_coset.py`](../../../verify/toy_coset.py) S2 — the vacua and their ρ-images; [`verify/toy_s4.py`](../../../verify/toy_s4.py) — the Monte Carlo numbers, gated; [`verify/toy_gw.py`](../../../verify/toy_gw.py) — F(+) − F(−) = 2.634 at N = 6, 8, 10
- [`CLAUDE.md`](../../../CLAUDE.md) 'Since the handoff' — the real-model preference listed as a lead
- [`popsci/universes-other-half.md`](../../../popsci/universes-other-half.md) 'An asymmetry that cannot be avoided' — the ice-crystal picture (popular article; not a status source)
- [`notes/closed-universe.md` §5](../../../notes/closed-universe.md#5-reciprocity-on-a-closed-space) — on T\*S³ only the position polarization is integrable, and what that means for the mirror vacuum; the critic's result alone, not reviewed
- [`notes/dual-sector.md` §8](../../../notes/dual-sector.md#8-the-vacuum-and-the-choice-of-polarization); [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md) item 70 — "kinematical" as their word for general relativity's split; a breaking tied to the polarization in the vacuum, for another symmetry; the other polarization's equal standing as a symmetry of the theory; pending
