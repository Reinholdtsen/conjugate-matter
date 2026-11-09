---
title: "τ: hilltop quintessence on the Maslov circle"
weight: 40
status: alive
description: "S_τ with V = V₀[1 + cos(τ/f)]: τ sits near the hilltop and thaws (w₀ > −1, wₐ < 0) along the corridor wₐ ≈ −1.5(1 + w₀) — 'the angle of the mirror'; under real pressure from DESI DR2, and the toy models show consistency only."
provenance: [D, T]
sources:
  - "wiki/papers/broken-born-checkpoint-v2.md §10"
  - "CLAUDE.md 'Since the handoff'"
  - "wiki/papers/broken-born-checkpoint-v2.md §4"
  - "wiki/papers/broken-born-checkpoint-v2.md §6"
  - "wiki/papers/broken-born-checkpoint-v2.md §7.3"
  - "wiki/papers/broken-born-checkpoint-v2.md §7.5"
  - "wiki/papers/broken-born-checkpoint-v2.md §13 rows 4–5"
  - "wiki/papers/broken-born-checkpoint-v2.md §15"
  - "wiki/papers/reciprocity-toy-models.md §2"
  - "wiki/papers/reciprocity-toy-models.md §4"
  - "wiki/papers/reciprocity-toy-models.md §6"
  - "verify/toy_coset.py"
  - "HANDOFF.md §2"
  - "notes/broken-born-theory.md §1"
  - "notes/broken-born-theory.md §2"
  - "notes/broken-born-theory.md §3"
  - "notes/broken-born-theory.md §7"
  - "notes/broken-born-theory.md §12"
  - "notes/broken-born-theory.md 'Addendum (v0.3, overnight): axiom correction and the modular core'"
  - "notes/broken-born-program-v1.md §8"
  - "notes/geometric-core.md §B"
  - "notes/geometric-core.md §F"
  - "notes/beta-coefficients.md §2"
  - "notes/toy-lagrangian.md 'Chunk 1 results'"
  - "notes/toy-lagrangian.md 'Chunk 2 results'"
  - "notes/toy-lagrangian.md 'Chunk 3 results'"
  - "review/wiki-build-flags.md items 1, 10, 27, 43"
  - "review/wiki-build-flags.md items 27 (addendum), 45, 46, 52"
  - "notes/closed-universe.md §2"
  - "notes/closed-universe.md §6"
  - "popsci/angle-of-the-mirror.md 'The referee is already on the field'"
  - "popsci/universes-other-half.md 'Dark energy as the orientation of the split'"
---

*The program identifies dark energy with τ, the angle that sets how the vacuum divides phase space into position and momentum. Because τ is an angle, its potential energy must repeat when τ goes once around its circle, and the program writes it as a cosine, V = V₀[1 + cos(τ/f)]. Today τ is taken to sit near the top of that potential, where its energy is almost all potential energy and it acts almost like a [cosmological constant](cosmological-constant.md), while drifting slowly away from the top, so that dark energy weakens over time and its [equation of state](quintessence.md#dark-energy-and-the-equation-of-state) w, the ratio of its pressure to its energy density, never falls below −1, the value for a cosmological constant. [Thawing](thawing-and-freezing.md) hilltop [quintessence](quintessence.md) of this kind is an established class of models; the program's contribution is the identification of the field, which the [popular article](../../history/documents/popular-articles.md) calls "the angle of the mirror". The claim stands under real pressure: the second data release of the [Dark Energy Spectroscopic Instrument](desi.md) (DESI) favours a phase with w below −1, which τ cannot produce, and the next release is the decisive test.*

**Status:** Alive, under pressure — [D + T] ([checkpoint #11](../../history/documents/checkpoint.md) [§10](../../papers/broken-born-checkpoint-v2.md#10-cosmology)): the identification is the program's, the quintessence physics is literature — the cited fits are live-searched [S]; the toy-model support is [D][V] and shows consistency only, and no `verify/` script tests these claims; [`verify/closed_universe.py`](../../../verify/closed_universe.py) checks the separate arithmetic of [a closed Comatter universe](../scale-factor-duality/closed-universe.md). The pressure comes from Data Release 2 (DR2) of [DESI](desi.md), per the root [`CLAUDE.md`](../../../CLAUDE.md): "The dark-energy sector is under real pressure ahead of DR3."

## The claim

[#11 §10](../../papers/broken-born-checkpoint-v2.md#10-cosmology), inside the paragraph tagged **Dark energy [D + T]** (w₀ is the value of w today, and wₐ measures how fast w has changed as the universe expanded, a negative wₐ meaning that w has been rising; [what w₀ and wₐ mean](cpl-parametrization.md#what-w-and-wₐ-mean)):

> τ is hilltop quintessence on the Maslov circle, V = V₀[1 + cos(τ/f)], periodicity by topology; strictly w ≥ −1; thawing corridor wₐ ≈ −1.5(1 + w₀); two parameters (f, τᵢ) for three observables (w₀, wₐ, t_turn) — one over-constraint.

The sentence joins two kinds of statement. That the dark-energy field is τ, the Maslov phase of the vacuum's polarization, and that its potential is periodic by topology, are the program's own [D]. That a canonical scalar field near the top of a cosine potential behaves as thawing quintessence, with w ≥ −1 and a drift along a known corridor, is established cosmology [T]; applied to τ, [#1 §7](../../../notes/broken-born-theory.md#7-cosmology-ii-dark-energy-its-drift-and-the-turnaround) tags the bound w ≥ −1 [D] ([quintessence and the equation of state](quintessence.md)). The remaining clauses have their own pages: [the no-phantom bound w ≥ −1](no-phantom-bound.md) and [the dark-energy over-constraint](over-constraint.md).

## The field τ

### An angle on the space of polarizations

Under the program's postulates the vacuum selects a polarization, a division of phase space into a position half and a momentum half ([P5: the vacuum selects a polarization](../../program/postulates/p5-spontaneous-selection.md)). The possible divisions form [the Lagrangian Grassmannian](../../phase-space/modular-field/lagrangian-grassmannian.md) Λ(d), a compact space whose loops that cannot be shrunk to a point are all built from one, the [Maslov circle](../../phase-space/modular-field/maslov-phase.md). The [lab notebook](../../history/documents/lab-notebook.md) defines τ as the angle around that circle ([#1 §2](../../../notes/broken-born-theory.md#2-kinematic-core), transcribed from its LaTeX):

```text
τ ≡ f · arg det²(·)
```

"a compact, 2πf-periodic modulus of the vacuum. This field is promoted below to the dark-energy field. Periodicity is topology **[D]**; that τ is the *lightest* modulus, with the other nine directions heavy, is assumed **[P]**." The constant f converts the angle into a field with units; τ and τ + 2πf are the same vacuum.

[#11 §6](../../papers/broken-born-checkpoint-v2.md#6-the-modular-field) places τ on the boundary of the space where the program's [modular field](../../phase-space/modular-field/modular-field-z.md) takes its values: "**Λ(d) is the Shilov boundary** of the Siegel domain [T]; the dark-energy field τ is the Maslov phase of the boundary variable, its periodicity a fact of topology (π₁(U(d)/O(d)) = ℤ)." The construction is on [τ as the Maslov phase of the boundary](../../phase-space/modular-field/maslov-phase.md).

### Light, and not absorbed by X

τ's lightness among the moduli of Λ(d) is a postulate [P] ([#1 §2](../../../notes/broken-born-theory.md#2-kinematic-core)). The program's [momentum graviton X](../../gravity/momentum-graviton/_index.md) becomes massive by absorbing modes of a different sector, and τ survives: "τ un-eaten (compact J-sector, not the Stückelberg sector)" ([#11 §7.5](../../papers/broken-born-checkpoint-v2.md#75-spectrum-d), [D]; [τ is not eaten](../../gravity/momentum-graviton/tau-not-eaten.md); [the Stückelberg sector](../../symmetry-breaking/stuckelberg-fields.md#τ-is-outside-the-stückelberg-sector)). The residual mixing of τ with the absorbed modes is open item 6 of [#11 §14](../../papers/broken-born-checkpoint-v2.md#14-open-problems) ([Open: τ–Stückelberg mixing (OP6)](../../gravity/momentum-graviton/tau-stuckelberg-mixing.md)).

### Why τ needs the corrected postulate

The field exists only because the program's postulate on rigid structures was corrected. Under the [original P2](../../program/postulates/original-p2.md), with both the [symplectic form](../../phase-space/reciprocity/symplectic-form.md) ω and the [neutral metric](../../phase-space/born-geometry/born-structures.md) η rigid, the notebook's v0.3 addendum records that "strict P2 makes the polarization choice discrete, eliminating the Lagrangian Grassmannian, the Maslov circle, and hence the entire τ/dark-energy sector". (The word "discrete" is flagged as a suspected error in the source: for d ≥ 2 the doubly compatible polarizations form continuous families, though the conclusion that there is no Maslov circle survives; [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md) item 1.) [Calc note #5](../../history/documents/field-equation-notes.md) named the rigid branch: "BBT reduces to GR + one bespoke SIDM model, with w ≡ −1 and the gate unexplained" ([§B](../../../notes/geometric-core.md#b-the-inconsistency-and-the-forced-repair-d--structural)), BBT being Broken-Born theory (the program's earlier name), GR [general relativity](../../gravity/spin-2-fields/general-relativity.md) and SIDM [self-interacting dark matter](../../dark-matter/halo-astrophysics/self-interacting-dark-matter.md). Under [P2′](../../program/postulates/p2-prime.md), only ω is rigid, and "The Grassmannian, the Maslov circle, and τ are restored" (#1 'Addendum (v0.3)'). The argument is on [the nontriviality theorem](../../program/postulates/nontriviality-theorem.md).

## The action and its potential

### S_τ

The lab notebook gives τ a canonical scalar action ([#1 §3](../../../notes/broken-born-theory.md#3-action), transcribed from its LaTeX):

```text
S_τ = ∫ √−g [ ½(∂τ)² − V(τ) ]
V(τ) = V₀ [1 + cos(τ/f)]
```

and tags its parts separately: "The potential's *periodicity* is forced by the Maslov topology **[D]**; its *existence* comes from the explicit breaking of Grassmannian rotations by the rigid ω (P2) — the rigidity is the 'instanton' that tilts the circle. Its *magnitude* V₀ is a free parameter here. **[P/O]**" The account of the potential's existence is superseded (below, [Superseded: the potential's origin in the rigid ω](#superseded-the-potentials-origin-in-the-rigid-ω)).

The kinetic term is the standard one, which is why τ obeys the null energy condition and keeps w ≥ −1 while its energy density is positive ([the phantom divide and the null energy condition](phantom-divide.md)).

### Why a cosine

The topology fixes only the period: V must be unchanged under τ → τ + 2πf. In this wiki's reading, any such function can be written as a Fourier series in τ/f, and V₀[1 + cos(τ/f)] keeps the constant term and the first harmonic, the standard form for an [axion-like field](axion-like-fields.md#the-periodic-potential) [T]. The documents do not discuss higher harmonics or the size of the constant term. As written, V ≥ 0 whenever V₀ > 0, while the documents' account of the program's [turnaround](../scale-factor-duality/conjugate-bounce.md) needs V < 0; they do not reconcile the two ([Open: the sign of V(τ) and the turnaround](potential-sign.md); flag 27 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md)). The flag's addendum (2026-10-27) finds that a closed universe turns around with V ≥ 0 throughout, τ passing its minimum and oscillating as dust while curvature reverses the expansion, and that a flat or open universe never does ([a closed Comatter universe](../scale-factor-duality/closed-universe.md#the-turnaround-needs-k--1-dv)).

### Its magnitude

V₀ is fixed by the observed dark-energy density: [#9 §8](../../../notes/broken-born-program-v1.md#8-cosmology) writes the potential with "V₀ fixed by Ω_DE", and [#1 §7 item 4](../../../notes/broken-born-theory.md#7-cosmology-ii-dark-energy-its-drift-and-the-turnaround) states "V₀ is fixed by Ω_DE". That leaves f and the initial value τᵢ as the sector's free numbers ([the dark-energy over-constraint](over-constraint.md)).

### Its origin: open

Where the potential comes from is an open problem. Version 2.2 of #11 refines P2′ with the [toy-model](../../symmetry-breaking/toy-models/_index.md) result that the polarization is a [Goldstone angle](../../symmetry-breaking/goldstone-angle.md): "A definite polarization needs a ρ-preserving potential on that angle — a rigid, unordered pair of axes, so more structure than ω alone, though less than a rigid η" ([#11 §4](../../papers/broken-born-checkpoint-v2.md#4-postulates)). The root [`CLAUDE.md`](../../../CLAUDE.md) lists "a derivation of the ρ-preserving potential" among the open ends of the toy-model work. See [Open: the origin of the ρ-preserving potential](../../symmetry-breaking/rho-preserving-potential.md).

## How τ behaves: thawing from the hilltop

A field near the maximum of its potential has almost no kinetic energy and w close to −1. While the expansion rate is large, the expansion damps the field's motion and holds it nearly fixed; as the expansion slows, the field moves away from the maximum, its kinetic energy grows, and w rises above −1. This is the thawing behaviour of hilltop quintessence [T] ([thawing and freezing quintessence](thawing-and-freezing.md#hilltop-models)).

The lab notebook applies it to τ ([#1 §7](../../../notes/broken-born-theory.md#7-cosmology-ii-dark-energy-its-drift-and-the-turnaround), introduction and item 2, transcribed from its LaTeX):

> Identify dark energy with the Maslov modulus τ sitting near the top of its cosine potential (hilltop axion quintessence). [...] **Thawing shape.** Hilltop initial conditions give w ≈ −1 in the past, rising now: w₀ > −1, wₐ < 0, on the standard thawing corridor wₐ ≈ −1.5(1 + w₀). [...] **[T]**

Here w₀ and wₐ are the present value and the drift of w in the Chevallier–Polarski–Linder (CPL) form w(a) = w₀ + wₐ(1 − a) ([the CPL parametrization](cpl-parametrization.md)). #1 tags item 2 [T]: the thawing shape is a property of hilltop fields, not something the program derives. [#11 §10](../../papers/broken-born-checkpoint-v2.md#10-cosmology) keeps the corridor, and the requirement of row 4 of the [prediction table](../../predictions/_index.md) is "Thawing, w₀ > −1, wₐ < 0, never phantom; drift persists in DESI DR3" ([#11 §13](../../papers/broken-born-checkpoint-v2.md#13-predictions-and-kill-conditions); [row 4: thawing dark energy, never phantom](../../predictions/dark-energy-drift.md)).

In the toy-model worklog this drift has a geometric reading: "the present-day thawing of τ would be a slow drift of the polarization angle. That is a claim about the program, not verified here" ([`notes/toy-lagrangian.md`](../../../notes/toy-lagrangian.md), 'Chunk 2 results'; [the polarization as a Goldstone angle](../../symmetry-breaking/goldstone-angle.md)).

## Nothing else supplies vacuum energy

[#11 §10](../../papers/broken-born-checkpoint-v2.md#10-cosmology): "§7.3 guarantees the wedge sector contributes nothing that competes with τ." The reference is to the program's [vacuum-energy identity](../../gravity/palindromic-branch/vacuum-energy-identity.md): with reciprocity forcing [the palindrome βₙ = β₄₋ₙ](../../gravity/palindromic-branch/palindrome.md) on the momentum graviton's potential, a flat aligned vacuum forces that potential's vacuum energy to vanish ([#11 §7.3](../../papers/broken-born-checkpoint-v2.md#73-palindrome-and-the-vacuum-energy-identity-dv), [D][V]). [Calc note #8](../../history/documents/field-equation-notes.md) drew the consequence for cosmology: "The massive-gravity sector contributes *nothing* to the cosmological constant; dark energy is left entirely to the τ sector, which is precisely the architecture the cosmology chapter had assumed" ([`notes/beta-coefficients.md` §2](../../../notes/beta-coefficients.md#2-the-vacuum-energy-theorem-d--rigorous-four-lines)). Flag 52 notes that the guarantee holds for the dark-energy density but follows from the exact (1 − y)⁴/y relation on the bimetric branch, not from §7.3's aligned-point identity alone, and that #11 omits a step in the strength of gravity, G_eff = 2G_N while the expansion rate far exceeds X's mass ([the momentum graviton in a closed universe](../../gravity/momentum-graviton/closed-universe.md#the-branch-relation-dv)).

The scope is limited. The identity "does **not** by itself address matter-loop vacuum energy, the 'old' cosmological-constant problem" ([#11 §7.3](../../papers/broken-born-checkpoint-v2.md#73-palindrome-and-the-vacuum-energy-identity-dv); [the cosmological-constant problem](../../gravity/spin-2-fields/cosmological-constant-problem.md)). The identity leaves the vacuum energy of matter loops where general relativity leaves it, and #11 does not claim otherwise.

## The fits [S]

[#11 §10](../../papers/broken-born-checkpoint-v2.md#10-cosmology) summarizes the fits: "compelling evidence for weakening dark energy with phantom behavior less significant (non-phantom compatible at ~2σ) and high posterior preference for a future anti-de Sitter transition and collapse in negative-minimum quintessence fits [19S, 20S, 21S]" ([anti-de Sitter space](de-sitter-space.md#anti-de-sitter-space-t)). Flag 45 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md) finds that only [19] supports the second clause: [20] fits V₀[1 + cos] with null spatial curvature and mentions no anti-de Sitter phase or collapse, and neither paper bears on the program's V ≥ 0 potential. The two fits are Gialamas et al., "Quintessence and phantoms in light of DESI 2025," [arXiv:2506.21542](https://arxiv.org/abs/2506.21542) [19S], and Ureña-López et al. (DESI), an axion-quintessence analysis of DESI data, [arXiv:2503.20178](https://arxiv.org/abs/2503.20178) [20S]. The lab notebook says that "Hilltop/axion potentials of exactly this class have been fit directly to DESI DR1/DR2 by the collaboration and others" ([#1 §7 item 2](../../../notes/broken-born-theory.md#7-cosmology-ii-dark-energy-its-drift-and-the-turnaround)), DR1 being Data Release 1. The fits concern the class of models, not the program's identification of the field.

## Under pressure from DESI DR2

The second DESI data release reports, in every combination of datasets, "a phase of w > −1 at low redshifts and a phantom crossing to w < −1 above redshifts z ≃ 0.4" ([#11 §10](../../papers/broken-born-checkpoint-v2.md#10-cosmology), quoting [21S]), where [redshift](../scale-factor-duality/redshift.md) z is the stretching of light by the expansion of the universe since the light was emitted, and larger z means earlier. τ is a canonical scalar and cannot produce the phantom phase, so, in #11's words, "The framework's strict w ≥ −1 therefore stands against the direct reading of the data." It survives on two points: "non-phantom quintessence fits remain compatible [19S], and w(z) is inferred from distances rather than observed" ([#11 §10](../../papers/broken-born-checkpoint-v2.md#10-cosmology)). Data Release 3 (DR3) "is the decisive test (§13, row 4)".

The root [`CLAUDE.md`](../../../CLAUDE.md) states the position: "DESI DR2 favors a phantom crossing above z ≈ 0.4, against the framework's strict w ≥ −1 (§10). The dark-energy sector is under real pressure ahead of DR3." [#11 §15](../../papers/broken-born-checkpoint-v2.md#15-assessment) lists the crossing among the program's degeneration risks. The measurement, its route into the program through the [round-3](../../method/review/round-3/_index.md) review, and the three outcomes of DR3 are on [DESI DR2's phantom crossing](desi-dr2-phantom-crossing.md); the italic passage of [#11 §10](../../papers/broken-born-checkpoint-v2.md#10-cosmology), which calls DESI's hints "exactly the required drift", is recorded there as [an unreconciled sentence](desi-dr2-phantom-crossing.md#an-unreconciled-sentence-in-11-10).

[#11 §10](../../papers/broken-born-checkpoint-v2.md#10-cosmology) states the corridor quoted above and DR2's crossing in one paragraph without relating them. Flag 43 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md) relates them: every point of the corridor has w₀ > −1 and w₀ + wₐ < −1, the region of the CPL plane in which DR2's fits lie and in which, in the flag's audit, fields with τ's potential that never fall below −1 also give fits. In the flag's account, what separates the corridor from DR2's crossing is the slope (a crossing at z = 2 for every point of the corridor against z ≈ 0.35–0.50 for DR2's fits), not the region; the pressure stands, and it rests on the crossing [redshift](../scale-factor-duality/redshift.md). The audit confirmed the flag by two independent checks ([the corridor and DR2's crossing](cpl-parametrization.md#the-corridor-and-dr2s-crossing)).

## Toy-model support: consistency only

### What the toy models show

Version 2.2 of #11 adds a paragraph to [§10](../../papers/broken-born-checkpoint-v2.md#10-cosmology), tagged [D][V]:

> in an explicit ρ-symmetric coset model of (H, K), and in the complex self-dual Grosse–Wulkenhaar model, ρ sits inside a continuous U(1), so the polarization is a Goldstone angle. In the coset model that angle parametrizes Λ(1): it is τ's circle. A definite polarization requires the ρ-preserving potential this section posits.

In [model I, the coset sigma model](../../symmetry-breaking/toy-models/coset-model/_index.md), the potential's Hessian at the vacuum has rank 1, leaving three Goldstone directions: "the two non-compact half-plane directions, and the compact angle φ, which parametrizes the Lagrangian Grassmannian Λ(1)" ([toy note §2](../../papers/reciprocity-toy-models.md#2-model-i-a-coset-sigma-model-of-h-k)). [`verify/toy_coset.py`](../../../verify/toy_coset.py) checks the rank: "potential Hessian has rank 1: three flat directions (Goldstones), one massive" ([the toy-model scripts](../../method/verification/toy-model-scripts.md)). The worklog draws the connection: the compact Goldstone is "the Lagrangian Grassmannian Λ(1), which is the checkpoint's Maslov circle (the τ field of §10)" ([`notes/toy-lagrangian.md`](../../../notes/toy-lagrangian.md), 'Chunk 1 results').

### The potential the toys need

Without a potential the angle does not order in 1+1 dimensions, by the [Mermin–Wagner–Coleman theorem](../../symmetry-breaking/mermin-wagner-coleman.md), so the toy adds a ρ-preserving potential on it. [#11 §10](../../papers/broken-born-checkpoint-v2.md#10-cosmology) continues: "That potential must be bounded with all fields dynamical — the round-4 review found the naive form unbounded once H moves" ([Under review: the naive ρ-preserving potential](../../symmetry-breaking/toy-models/coset-model/naive-potential.md)). Its bounded replacement V_b reduces at H = 1 to "V_b = −(μ/2)(1 + cos 2φ)" ([toy note §4](../../papers/reciprocity-toy-models.md#4-quantum-stability); [the bounded potential V_b](../../symmetry-breaking/toy-models/coset-model/bounded-potential.md)), which [`verify/toy_coset.py`](../../../verify/toy_coset.py) also checks. It is a cosine on the same circle, invariant under ρ, which acts as φ → φ + π. No document relates the toy's μ and φ quantitatively to τ's V₀ and f.

The worklog's chunk 3 states what this means for the program: "In 3+1, the program's actual dimension, Coleman–Mermin–Wagner does not apply. There the self-dual coset model can break the continuous U(1) itself, with τ an exactly massless Goldstone. §10's τ has a potential, so the explicit breaking is in the program anyway." Its revised conclusion is that the toy supports broken reciprocity in the form "a pseudo-Goldstone polarization angle with a ρ-symmetric potential" ([`notes/toy-lagrangian.md`](../../../notes/toy-lagrangian.md), 'Chunk 3 results'; [the polarization as a Goldstone angle](../../symmetry-breaking/goldstone-angle.md)).

### What they do not show

[#11 §10](../../papers/broken-born-checkpoint-v2.md#10-cosmology) ends the paragraph: "None of this tests the cosmology; it only shows the structure is consistent." The toy note says the same in its limitations: "**Motivation, not result.** In a parent framework the polarization angle is identified with a dark-energy field. The Goldstone structure here is consistent with that, but untested by it." ([toy note §6](../../papers/reciprocity-toy-models.md#6-summary-and-limitations)). Both toys are field theories at d = 1 without gravity or an expanding background, so they say nothing about w.

## Parameters and tests

- **Free numbers.** V₀, fixed by Ω_DE; f; and τᵢ, the initial value. Two remain for three observables, w₀, wₐ and the turnaround time t_turn ([the dark-energy over-constraint](over-constraint.md)). With V ≥ 0 a turnaround needs a closed universe, where t_turn ∝ |Ω_k|^{−3/2} at fixed (w₀, wₐ), so the curvature is a third input and the over-constraint moves to (f, τᵢ, Ω_k) rather than vanishing (flag 46; [a closed Comatter universe](../scale-factor-duality/closed-universe.md#the-over-constraint-moves-dv)).
- **Near-term test.** [Row 4](../../predictions/dark-energy-drift.md): "DR3+ constant −1 (kills τ-sector); robust intrinsic w < −1 (kills outright) — DR2 already favors a crossing above z ≈ 0.4 (§10)" ([#11 §13](../../papers/broken-born-checkpoint-v2.md#13-predictions-and-kill-conditions)).
- **Long-horizon consequence.** [Row 5: the fate of the expansion](../../predictions/fate-of-expansion.md), "Turnaround = conjugate bounce" ([#11 §13](../../papers/broken-born-checkpoint-v2.md#13-predictions-and-kill-conditions)), which in the documents' account needs V(τ) < 0 ([the turnaround as the conjugate bounce](../scale-factor-duality/conjugate-bounce.md); see flag 27 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md)) and, by the flag's addendum, with V ≥ 0 needs a closed universe.
- **Safety.** τ is extremely light; the lab notebook argues that as a [pseudo-Goldstone field](../../symmetry-breaking/goldstone-and-higgs.md) it produces no detectable [fifth force](../../gravity/spin-2-fields/yukawa-forces.md#fifth-forces-a-yukawa-term-beside-gravity-t) ([fifth-force safety of τ](tau-fifth-force.md)).

## What is open

- **The origin of the potential.** [Open: the origin of the ρ-preserving potential](../../symmetry-breaking/rho-preserving-potential.md); "a derivation of the ρ-preserving potential" is an open end in the root [`CLAUDE.md`](../../../CLAUDE.md).
- **The sign of the potential.** V₀[1 + cos(τ/f)] is never negative for V₀ > 0, yet the documents' turnaround needs V < 0; none of them reconciles the two ([Open: the sign of V(τ) and the turnaround](potential-sign.md); flag 27 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md)). The flag's addendum finds the turnaround with V ≥ 0 in a closed universe, and the data in the program's model class disfavour closure at about 2σ.
- **Mixing with the absorbed modes.** [Open: τ–Stückelberg mixing (OP6)](../../gravity/momentum-graviton/tau-stuckelberg-mixing.md).
- **Kinetic or potential energy.** The lab notebook motivates near-constant dark energy as kinetic energy in the dual frame and then implements it as τ's potential energy; no document derives the link ([Open: dual kinetic energy versus τ's potential](../scale-factor-duality/dual-kinetic-link.md)). [#11 §10](../../papers/broken-born-checkpoint-v2.md#10-cosmology) lists how the dual-frame route "relates to τ's potential" as an open question of P.R.'s conjecture that the conjugate universe's collapse drives our acceleration [O] ([Conjecture: conjugate collapse powers our expansion](../scale-factor-duality/collapse-powered-expansion.md)).
- **τ's lightness** among the ten moduli of Λ(d) at d = 4 is a postulate [P] ([#1 §2](../../../notes/broken-born-theory.md#2-kinematic-core)), and the fate of the other nine is open ([Open: field content of the broken vacuum](../../phase-space/modular-field/field-content.md)).

## History

- **v0.1, the lab notebook (September 2026).** [#1 §3](../../../notes/broken-born-theory.md#3-action) writes the action and potential; [§4](../../../notes/broken-born-theory.md#4-consistency-with-everything-already-measured) argues fifth-force safety; [§7](../../../notes/broken-born-theory.md#7-cosmology-ii-dark-energy-its-drift-and-the-turnaround) identifies dark energy with τ (thawing, w ≥ −1, the turnaround, the over-constraint); [§9 row 5](../../../notes/broken-born-theory.md#9-predictions) sets the test against DESI DR3; the [§12](../../../notes/broken-born-theory.md#12-one-paragraph-summary) summary calls τ "a dark energy field that is literally the Maslov angle of the vacuum, forced by topology to a periodic potential, hence thawing, never phantom, and destined to go negative" (see flag 27 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md), whose addendum finds that the turnaround's cause, with this potential, is a closed universe's curvature and not a negative V).
- **v0.2.** After [the clumping problem](../../history/main-problems.md), the notebook lists "row 5 (thawing, no-phantom, DESI DR3)" among the program's distinctive, still-live content.
- **v0.3.** Strict P2 is found to erase τ, and P2′ restores it (above).
- **The field-equation problem.** Calc note [#8](../../../notes/beta-coefficients.md) shows that the momentum graviton's sector adds no vacuum energy, "leaving dark energy entirely to τ as the cosmology chapter had assumed" (#1 'Addendum (v0.6)'), and that τ is not absorbed by X at leading order ([§3](../../../notes/broken-born-theory.md#3-action)).
- **v1 ([#9 §8](../../../notes/broken-born-program-v1.md#8-cosmology)).** The sector as a numbered section, with "V₀ fixed by Ω_DE" and the fits marked "[T — refresh citations before publication]".
- **#11 v2.0.** [§10](../../papers/broken-born-checkpoint-v2.md#10-cosmology) states the sector in its present form, before the DR2 paragraph. The [handoff](../../history/documents/handoff.md) lists τ among the live results: "τ = hilltop/axion quintessence on the Maslov circle; thawing, w ≥ −1 always, eventual negative V ⇒ turnaround = conjugate bounce" ([`HANDOFF.md` §2](../../../HANDOFF.md#2-scientific-state-one-screen)).
- **#11 v2.1 (2026-10-19).** After round 3, [§10](../../papers/broken-born-checkpoint-v2.md#10-cosmology) gains the "Under pressure (v2.1)" paragraph on DESI DR2.
- **#11 v2.2 (2026-10-20).** [§10](../../papers/broken-born-checkpoint-v2.md#10-cosmology) gains the toy-model support, and P2′ its refinement: the polarization is a Goldstone angle that needs a ρ-preserving potential.
- **The popular articles.** The journey article [#10](../../../popsci/angle-of-the-mirror.md) gives the program's slogan: dark energy is "not a substance but a *position*", and "dark matter is the mirror-world's stuff; dark energy is the angle of the mirror" ('The referee is already on the field'). The other article, [#12](../../../popsci/universes-other-half.md), describes dark energy as "the energy stored in that orientation's displacement from its resting value" ('Dark energy as the orientation of the split'). Both are explanation only, not sources for status ([the popular articles](../../history/documents/popular-articles.md)).

## Superseded: the potential's origin in the rigid ω

The lab notebook's v0.1 attributed the existence of τ's potential to the rigidity of ω. In [#1 §3](../../../notes/broken-born-theory.md#3-action) the potential's "*existence* comes from the explicit breaking of Grassmannian rotations by the rigid ω (P2) — the rigidity is the 'instanton' that tilts the circle", tagged [P/O]. [#1 §1](../../../notes/broken-born-theory.md#1-postulates) lists this as one of the "triple duty" roles of P2, which "supplies the explicit breaking that gives the dark-energy field its potential (§5)"; the potential is in fact in [#1 §3](../../../notes/broken-born-theory.md#3-action), not [§5](../../../notes/broken-born-theory.md#5-conjugate-sector-phenomenology) ([`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md) item 10). The §12 summary repeats it: reciprocity is broken "with a rigid symplectic form as its explicit tilt".

The later documents replace this account step by step.

1. Calc note [#5](../../../notes/geometric-core.md), writing the repair P2′, lists "the origin of τ's potential under P2′ (what explicitly breaks Λ(d) rotations — candidate: the section choice itself, or matter loops)" among the problems now open ([`notes/geometric-core.md` §F](../../../notes/geometric-core.md#f-status-after-tonight)).
2. The toy models show that with only ω rigid, ρ sits inside a continuous U(1) and the polarization is a Goldstone angle [D][V]; a definite polarization needs a potential that brings "more structure than ω alone" ([#11 §4](../../papers/broken-born-checkpoint-v2.md#4-postulates), v2.2).
3. The root [`CLAUDE.md`](../../../CLAUDE.md) lists the derivation of that potential as open.

So rigidity of ω alone does not tilt the circle; the potential's periodicity [D] stands, and its origin is [Open: the origin of the ρ-preserving potential](../../symmetry-breaking/rho-preserving-potential.md). The superseded statement is listed on [superseded statements](../../status/superseded.md).

## Sources

- [`wiki/papers/broken-born-checkpoint-v2.md` §10](../../papers/broken-born-checkpoint-v2.md#10-cosmology) — the identification and its tag, the fits, the "Under pressure (v2.1)" paragraph, the toy-model support and its limit; founding supposition 9 [O] and its open question on τ's potential
- [`CLAUDE.md`](../../../CLAUDE.md) 'Since the handoff' — "under real pressure ahead of DR3"; the derivation of the ρ-preserving potential as an open end; the naive potential under review
- [`wiki/papers/broken-born-checkpoint-v2.md` §4](../../papers/broken-born-checkpoint-v2.md#4-postulates) — P2′ and its v2.2 refinement; [§6](../../papers/broken-born-checkpoint-v2.md#6-the-modular-field) — τ as the Maslov phase of the Shilov boundary; [§7.3](../../papers/broken-born-checkpoint-v2.md#73-palindrome-and-the-vacuum-energy-identity-dv) — the wedge sector's zero vacuum energy and its scope; [§7.5](../../papers/broken-born-checkpoint-v2.md#75-spectrum-d) — τ un-eaten; [§13 rows 4–5](../../papers/broken-born-checkpoint-v2.md#13-predictions-and-kill-conditions) — the tests; [§15](../../papers/broken-born-checkpoint-v2.md#15-assessment) — the degeneration risk
- [`wiki/papers/reciprocity-toy-models.md` §2](../../papers/reciprocity-toy-models.md#2-model-i-a-coset-sigma-model-of-h-k), [§4](../../papers/reciprocity-toy-models.md#4-quantum-stability), [§6](../../papers/reciprocity-toy-models.md#6-summary-and-limitations) — the compact Goldstone angle, the bounded potential V_b at H = 1, "Motivation, not result"
- [`verify/toy_coset.py`](../../../verify/toy_coset.py) — the Hessian rank and V_b at H = 1 (current output in [`scripts/check.sh`](../../../scripts/check.sh))
- [`HANDOFF.md` §2](../../../HANDOFF.md#2-scientific-state-one-screen) — τ among the live results
- [`notes/broken-born-theory.md` §1](../../../notes/broken-born-theory.md#1-postulates)–[§3](../../../notes/broken-born-theory.md#3-action) — P2's "triple duty", τ ≡ f·arg det² and its tags, the action and potential; [§7](../../../notes/broken-born-theory.md#7-cosmology-ii-dark-energy-its-drift-and-the-turnaround) — hilltop thawing and the corridor; [§12](../../../notes/broken-born-theory.md#12-one-paragraph-summary) — the summary; 'Addendum (v0.3)' — strict P2 erases τ, P2′ restores it
- [`notes/broken-born-program-v1.md` §8](../../../notes/broken-born-program-v1.md#8-cosmology) — V₀ fixed by Ω_DE
- [`notes/geometric-core.md` §B](../../../notes/geometric-core.md#b-the-inconsistency-and-the-forced-repair-d--structural) — the rigid branch without τ; [§F](../../../notes/geometric-core.md#f-status-after-tonight) — the origin of τ's potential under P2′, open
- [`notes/beta-coefficients.md` §2](../../../notes/beta-coefficients.md#2-the-vacuum-energy-theorem-d--rigorous-four-lines) — dark energy left entirely to the τ sector
- [`notes/toy-lagrangian.md`](../../../notes/toy-lagrangian.md) 'Chunk 1 results', 'Chunk 2 results', 'Chunk 3 results' — the Goldstone angle as τ's circle, the thawing reading, the pseudo-Goldstone conclusion
- [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md) item 43 — the corridor in the region of DR2's fits, and the slope that separates it from DR2's crossing; items 1, 10 and 27 — the suspected source errors quoted on this page; item 27's addendum and items 45, 46 and 52 — the closed turnaround, the compound citation for the anti-de Sitter fits, the over-constraint moved to Ω_k, and the wedge sector's guarantee
- [`notes/closed-universe.md` §2](../../../notes/closed-universe.md#2-the-premise-and-the-turnaround-it-buys) — the turnaround in a closed universe with V ≥ 0, the over-constraint and the data; [§6](../../../notes/closed-universe.md#6-the-momentum-graviton-x-in-a-closed-universe) — the bimetric branch relation and G_eff = 2G_N; [`verify/closed_universe.py`](../../../verify/closed_universe.py) — the separate arithmetic of a closed universe
- [`popsci/angle-of-the-mirror.md`](../../../popsci/angle-of-the-mirror.md) 'The referee is already on the field', [`popsci/universes-other-half.md`](../../../popsci/universes-other-half.md) 'Dark energy as the orientation of the split' — the popular framing
