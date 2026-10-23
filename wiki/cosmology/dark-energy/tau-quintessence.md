---
title: "τ: hilltop quintessence on the Maslov circle"
weight: 40
status: alive
description: "S_τ with V = V₀[1 + cos(τ/f)]: τ sits near the hilltop and thaws (w₀ > −1, wₐ < 0) along the corridor wₐ ≈ −1.5(1 + w₀) — 'the angle of the mirror'; under real pressure from DESI DR2, and the toy models show consistency only."
provenance: [D, T]
sources:
  - "papers/broken-born-checkpoint-v2.md §10"
  - "CLAUDE.md 'Since the handoff'"
  - "papers/broken-born-checkpoint-v2.md §4"
  - "papers/broken-born-checkpoint-v2.md §6"
  - "papers/broken-born-checkpoint-v2.md §7.3"
  - "papers/broken-born-checkpoint-v2.md §7.5"
  - "papers/broken-born-checkpoint-v2.md §13 rows 4–5"
  - "papers/broken-born-checkpoint-v2.md §15"
  - "papers/reciprocity-toy-models.md §2"
  - "papers/reciprocity-toy-models.md §4"
  - "papers/reciprocity-toy-models.md §6"
  - "verify/toy_coset.py"
  - "HANDOFF.md §2"
  - "notes/broken-born-theory.md §1"
  - "notes/broken-born-theory.md §2"
  - "notes/broken-born-theory.md §3"
  - "notes/broken-born-theory.md §7"
  - "notes/broken-born-theory.md §12"
  - "notes/broken-born-theory.md 'Addendum (v0.3, overnight): axiom correction and the modular core'"
  - "notes/broken-born-program-v1.md §8"
  - "notes/debt1a-geometric-core.md §B"
  - "notes/debt1a-geometric-core.md §F"
  - "notes/debt1a-iv-beta-coefficients.md §2"
  - "notes/toy-lagrangian.md 'Chunk 1 results'"
  - "notes/toy-lagrangian.md 'Chunk 2 results'"
  - "notes/toy-lagrangian.md 'Chunk 3 results'"
  - "review/wiki-build-flags.md items 1, 10, 27, 43"
  - "popsci/angle-of-the-mirror.md 'The referee is already on the field'"
  - "popsci/universes-other-half.md 'Dark energy as the orientation of the split'"
---

*The program identifies dark energy with τ, the angle that sets how the vacuum divides phase space into position and momentum. Because τ is an angle, its potential energy must repeat when τ goes once around its circle, and the program writes it as a cosine, V = V₀[1 + cos(τ/f)]. Today τ is taken to sit near the top of that potential, where its energy is almost all potential energy and it acts almost like a [cosmological constant](/wiki/cosmology/dark-energy/cosmological-constant), while drifting slowly away from the top, so that dark energy weakens over time and its equation of state w never falls below −1. [Thawing](/wiki/cosmology/dark-energy/thawing-and-freezing) hilltop [quintessence](/wiki/cosmology/dark-energy/quintessence) of this kind is an established class of models; the program's contribution is the identification of the field, which the [popular article](/wiki/history/documents/popular-articles) calls "the angle of the mirror". The claim stands under real pressure: the second data release of the [Dark Energy Spectroscopic Instrument](/wiki/cosmology/dark-energy/desi) (DESI) favours a phase with w below −1, which τ cannot produce, and the next release is the decisive test.*

**Status:** Alive, under pressure — [D + T] ([checkpoint #11](/wiki/history/documents/checkpoint) §10): the identification is the program's, the quintessence physics is literature — the cited fits are live-searched [S]; the toy-model support is [D][V] and shows consistency only, and no `verify/` script tests [the cosmology](/wiki/cosmology). The pressure comes from Data Release 2 (DR2) of [DESI](/wiki/cosmology/dark-energy/desi), per the root `CLAUDE.md`: "The dark-energy sector is under real pressure ahead of DR3."

## The claim

#11 §10, inside the paragraph tagged **Dark energy [D + T]**:

> τ is hilltop quintessence on the Maslov circle, V = V₀[1 + cos(τ/f)], periodicity by topology; strictly w ≥ −1; thawing corridor wₐ ≈ −1.5(1 + w₀); two parameters (f, τᵢ) for three observables (w₀, wₐ, t_turn) — one over-constraint.

The sentence joins two kinds of statement. That the dark-energy field is τ, the Maslov phase of the vacuum's polarization, and that its potential is periodic by topology, are the program's own [D]. That a canonical scalar field near the top of a cosine potential behaves as thawing quintessence, with w ≥ −1 and a drift along a known corridor, is established cosmology [T]; applied to τ, #1 §7 tags the bound w ≥ −1 [D] ([quintessence and the equation of state](/wiki/cosmology/dark-energy/quintessence)). The remaining clauses have their own pages: [the no-phantom bound w ≥ −1](/wiki/cosmology/dark-energy/no-phantom-bound) and [the dark-energy over-constraint](/wiki/cosmology/dark-energy/over-constraint).

## The field τ

### An angle on the space of polarizations

Under the program's postulates the vacuum selects a polarization, a division of phase space into a position half and a momentum half ([P5: the vacuum selects a polarization](/wiki/program/postulates/p5-spontaneous-selection)). The possible divisions form [the Lagrangian Grassmannian](/wiki/phase-space/modular-field/lagrangian-grassmannian) Λ(d), a compact space whose loops that cannot be shrunk to a point are all built from one, the [Maslov circle](/wiki/phase-space/modular-field/maslov-phase). The [lab notebook](/wiki/history/documents/lab-notebook) defines τ as the angle around that circle (#1 §2, transcribed from its LaTeX):

```text
τ ≡ f · arg det²(·)
```

"a compact, 2πf-periodic modulus of the vacuum. This field is promoted below to the dark-energy field. Periodicity is topology **[D]**; that τ is the *lightest* modulus, with the other nine directions heavy, is assumed **[P]**." The constant f converts the angle into a field with units; τ and τ + 2πf are the same vacuum.

#11 §6 places τ on the boundary of the space where the program's [modular field](/wiki/phase-space/modular-field/modular-field-z) takes its values: "**Λ(d) is the Shilov boundary** of the Siegel domain [T]; the dark-energy field τ is the Maslov phase of the boundary variable, its periodicity a fact of topology (π₁(U(d)/O(d)) = ℤ)." The construction is on [τ as the Maslov phase of the boundary](/wiki/phase-space/modular-field/maslov-phase).

### Light, and not absorbed by X

τ's lightness among the moduli of Λ(d) is a postulate [P] (#1 §2). The program's [momentum graviton X](/wiki/gravity/momentum-graviton) becomes massive by absorbing modes of a different sector, and τ survives: "τ un-eaten (compact J-sector, not the Stückelberg sector)" (#11 §7.5, [D]; [τ is not eaten](/wiki/gravity/momentum-graviton/tau-not-eaten); [the Stückelberg sector](/wiki/symmetry-breaking/stuckelberg-fields#τ-is-outside-the-stückelberg-sector)). The residual mixing of τ with the absorbed modes is open item 6 of #11 §14 ([Open: τ–Stückelberg mixing (OP6)](/wiki/gravity/momentum-graviton/tau-stuckelberg-mixing)).

### Why τ needs the corrected postulate

The field exists only because the program's postulate on rigid structures was corrected. Under the [original P2](/wiki/program/postulates/original-p2), with both the [symplectic form](/wiki/phase-space/reciprocity/symplectic-form) ω and the [neutral metric](/wiki/phase-space/born-geometry/born-structures) η rigid, the notebook's v0.3 addendum records that "strict P2 makes the polarization choice discrete, eliminating the Lagrangian Grassmannian, the Maslov circle, and hence the entire τ/dark-energy sector". (The word "discrete" is flagged as a suspected error in the source: for d ≥ 2 the doubly compatible polarizations form continuous families, though the conclusion that there is no Maslov circle survives; `review/wiki-build-flags.md` item 1.) [Calc note #5](/wiki/history/documents/debt-1-notes) named the rigid branch: "BBT reduces to GR + one bespoke SIDM model, with w ≡ −1 and the gate unexplained" (§B), BBT being the Broken-Born theory, GR [general relativity](/wiki/gravity/spin-2-fields/general-relativity) and SIDM [self-interacting dark matter](/wiki/dark-matter/halo-astrophysics/self-interacting-dark-matter). Under [P2′](/wiki/program/postulates/p2-prime), only ω is rigid, and "The Grassmannian, the Maslov circle, and τ are restored" (#1 'Addendum (v0.3)'). The argument is on [the nontriviality theorem](/wiki/program/postulates/nontriviality-theorem).

## The action and its potential

### S_τ

The lab notebook gives τ a canonical scalar action (#1 §3, transcribed from its LaTeX):

```text
S_τ = ∫ √−g [ ½(∂τ)² − V(τ) ]
V(τ) = V₀ [1 + cos(τ/f)]
```

and tags its parts separately: "The potential's *periodicity* is forced by the Maslov topology **[D]**; its *existence* comes from the explicit breaking of Grassmannian rotations by the rigid ω (P2) — the rigidity is the 'instanton' that tilts the circle. Its *magnitude* V₀ is a free parameter here. **[P/O]**" The account of the potential's existence is superseded (below, [Superseded: the potential's origin in the rigid ω](#superseded-the-potentials-origin-in-the-rigid-ω)).

The kinetic term is the standard one, which is why τ obeys the null energy condition and keeps w ≥ −1 while its energy density is positive ([the phantom divide and the null energy condition](/wiki/cosmology/dark-energy/phantom-divide)).

### Why a cosine

The topology fixes only the period: V must be unchanged under τ → τ + 2πf. In this wiki's reading, any such function can be written as a Fourier series in τ/f, and V₀[1 + cos(τ/f)] keeps the constant term and the first harmonic, the standard form for an [axion-like field](/wiki/cosmology/dark-energy/axion-like-fields#the-periodic-potential) [T]. The documents do not discuss higher harmonics or the size of the constant term. As written, V ≥ 0 whenever V₀ > 0, while the program's [turnaround](/wiki/cosmology/scale-factor-duality/conjugate-bounce) needs V < 0; the documents do not reconcile the two ([Open: the sign of V(τ) and the turnaround](/wiki/cosmology/dark-energy/potential-sign); flag 27 in `review/wiki-build-flags.md`).

### Its magnitude

V₀ is fixed by the observed dark-energy density: #9 §8 writes the potential with "V₀ fixed by Ω_DE", and #1 §7 item 4 states "V₀ is fixed by Ω_DE". That leaves f and the initial value τᵢ as the sector's free numbers ([the dark-energy over-constraint](/wiki/cosmology/dark-energy/over-constraint)).

### Its origin: open

Where the potential comes from is now an open problem. Version 2.2 of #11 refines P2′ with the [toy-model](/wiki/symmetry-breaking/toy-models) result that the polarization is a [Goldstone angle](/wiki/symmetry-breaking/goldstone-angle): "A definite polarization needs a ρ-preserving potential on that angle — a rigid, unordered pair of axes, so more structure than ω alone, though less than a rigid η" (#11 §4). The root `CLAUDE.md` lists "a derivation of the ρ-preserving potential" among the open ends of the toy-model work. See [Open: the origin of the ρ-preserving potential](/wiki/symmetry-breaking/rho-preserving-potential).

## How τ behaves: thawing from the hilltop

A field near the maximum of its potential has almost no kinetic energy and w close to −1. While the expansion rate is large, the expansion damps the field's motion and holds it nearly fixed; as the expansion slows, the field moves away from the maximum, its kinetic energy grows, and w rises above −1. This is the thawing behaviour of hilltop quintessence [T] ([thawing and freezing quintessence](/wiki/cosmology/dark-energy/thawing-and-freezing#hilltop-models)).

The lab notebook applies it to τ (#1 §7, introduction and item 2, transcribed from its LaTeX):

> Identify dark energy with the Maslov modulus τ sitting near the top of its cosine potential (hilltop axion quintessence). [...] **Thawing shape.** Hilltop initial conditions give w ≈ −1 in the past, rising now: w₀ > −1, wₐ < 0, on the standard thawing corridor wₐ ≈ −1.5(1 + w₀). [...] **[T]**

Here w₀ and wₐ are the present value and the drift of w in the Chevallier–Polarski–Linder (CPL) form w(a) = w₀ + wₐ(1 − a) ([the CPL parametrization](/wiki/cosmology/dark-energy/cpl-parametrization)). #1 tags item 2 [T]: the thawing shape is a property of hilltop fields, not something the program derives. #11 §10 keeps the corridor, and the requirement of row 4 of the [prediction table](/wiki/predictions) is "Thawing, w₀ > −1, wₐ < 0, never phantom; drift persists in DESI DR3" (#11 §13; [row 4: thawing dark energy, never phantom](/wiki/predictions/dark-energy-drift)).

In the toy-model worklog this drift has a geometric reading: "the present-day thawing of τ would be a slow drift of the polarization angle. That is a claim about the program, not verified here" (`notes/toy-lagrangian.md`, 'Chunk 2 results'; [the polarization as a Goldstone angle](/wiki/symmetry-breaking/goldstone-angle)).

## Nothing else supplies vacuum energy

#11 §10: "§7.3 guarantees the wedge sector contributes nothing that competes with τ." The reference is to the program's [vacuum-energy identity](/wiki/gravity/palindromic-branch/vacuum-energy-identity): with reciprocity forcing [the palindrome βₙ = β₄₋ₙ](/wiki/gravity/palindromic-branch/palindrome) on the momentum graviton's potential, a flat aligned vacuum forces that potential's vacuum energy to vanish (#11 §7.3, [D][V]). [Calc note #8](/wiki/history/documents/debt-1-notes) drew the consequence for cosmology: "The massive-gravity sector contributes *nothing* to the cosmological constant; dark energy is left entirely to the τ sector, which is precisely the architecture the cosmology chapter had assumed" (`notes/debt1a-iv-beta-coefficients.md` §2).

The scope is limited. The identity "does **not** by itself address matter-loop vacuum energy, the 'old' cosmological-constant problem" (#11 §7.3; [the cosmological-constant problem](/wiki/gravity/spin-2-fields/cosmological-constant-problem)). The identity leaves the vacuum energy of matter loops where general relativity leaves it, and #11 does not claim otherwise.

## The fits [S]

#11 §10 summarizes the fits in a sentence written for v2.0 and kept unchanged since: "compelling evidence for weakening dark energy with phantom behavior less significant (non-phantom compatible at ~2σ) and high posterior preference for a future anti-de Sitter transition and collapse in negative-minimum quintessence fits [19S, 20S, 21S]" ([anti-de Sitter space](/wiki/cosmology/dark-energy/de-sitter-space#anti-de-sitter-space-t)). The two fits are Gialamas et al., "Quintessence and phantoms in light of DESI 2025," arXiv:2506.21542 [19S], and Ureña-López et al. (DESI), an axion-quintessence analysis of DESI data, arXiv:2503.20178 [20S]. The lab notebook says that "Hilltop/axion potentials of exactly this class have been fit directly to DESI DR1/DR2 by the collaboration and others" (#1 §7 item 2), DR1 being Data Release 1. The fits concern the class of models, not the program's identification of the field.

## Under pressure from DESI DR2

The second DESI data release reports, in every combination of datasets, "a phase of w > −1 at low redshifts and a phantom crossing to w < −1 above redshifts z ≃ 0.4" (#11 §10, quoting [21S]). τ is a canonical scalar and cannot produce the phantom phase, so, in #11's words, "The framework's strict w ≥ −1 therefore stands against the direct reading of the data." It survives on two points: "non-phantom quintessence fits remain compatible [19S], and w(z) is inferred from distances rather than observed" (#11 §10). Data Release 3 (DR3) "is the decisive test (§13, row 4)".

The root `CLAUDE.md` states the position: "DESI DR2 favors a phantom crossing above z ≈ 0.4, against the framework's strict w ≥ −1 (§10). The dark-energy sector is under real pressure ahead of DR3." #11 §15 lists the crossing among the program's degeneration risks. The measurement, its route into the program through the [round-3](/wiki/method/review/round-3) review, and the three outcomes of DR3 are on [DESI DR2's phantom crossing](/wiki/cosmology/dark-energy/desi-dr2-phantom-crossing); the italic passage of #11 §10, which still calls DESI's hints "exactly the required drift", is recorded there as [an unreconciled sentence](/wiki/cosmology/dark-energy/desi-dr2-phantom-crossing#an-unreconciled-sentence-in-11-10).

#11 §10 states the corridor quoted above and DR2's crossing in one paragraph without relating them. Flag 43 in `review/wiki-build-flags.md` relates them: every point of the corridor has w₀ > −1 and w₀ + wₐ < −1, the region of the CPL plane in which DR2's fits lie and in which, in the flag's audit, fields with τ's potential that never fall below −1 also give fits. In the flag's account, what separates the corridor from DR2's crossing is the slope (a crossing at z = 2 against z ≈ 0.4), not the region; the pressure stands, and it rests on the crossing [redshift](/wiki/cosmology/scale-factor-duality/redshift). The audit confirmed the flag by two independent checks ([the corridor and DR2's crossing](/wiki/cosmology/dark-energy/cpl-parametrization#the-corridor-and-dr2s-crossing)).

## Toy-model support: consistency only

### What the toy models show

Version 2.2 of #11 adds a paragraph to §10, tagged [D][V]:

> in an explicit ρ-symmetric coset model of (H, K), and in the complex self-dual Grosse–Wulkenhaar model, ρ sits inside a continuous U(1), so the polarization is a Goldstone angle. In the coset model that angle parametrizes Λ(1): it is τ's circle. A definite polarization requires the ρ-preserving potential this section posits.

In [model I, the coset sigma model](/wiki/symmetry-breaking/toy-models/coset-model), the potential's Hessian at the vacuum has rank 1, leaving three Goldstone directions: "the two non-compact half-plane directions, and the compact angle φ, which parametrizes the Lagrangian Grassmannian Λ(1)" (toy note §2). `verify/toy_coset.py` checks the rank: "potential Hessian has rank 1: three flat directions (Goldstones), one massive" ([the toy-model scripts](/wiki/method/verification/toy-model-scripts)). The worklog draws the connection: the compact Goldstone is "the Lagrangian Grassmannian Λ(1), which is the checkpoint's Maslov circle (the τ field of §10)" (`notes/toy-lagrangian.md`, 'Chunk 1 results').

### The potential the toys need

Without a potential the angle does not order in 1+1 dimensions, by the [Mermin–Wagner–Coleman theorem](/wiki/symmetry-breaking/mermin-wagner-coleman), so the toy adds a ρ-preserving potential on it. #11 §10 continues: "That potential must be bounded with all fields dynamical — the round-4 review found the naive form unbounded once H moves". The naive form is dead ([Obituary: the naive ρ-preserving potential](/wiki/symmetry-breaking/toy-models/coset-model/naive-potential)); its bounded replacement V_b reduces at H = 1 to "V_b = −(μ/2)(1 + cos 2φ)" (toy note §4; [the bounded potential V_b](/wiki/symmetry-breaking/toy-models/coset-model/bounded-potential)), which `verify/toy_coset.py` also checks. It is a cosine on the same circle, invariant under ρ, which acts as φ → φ + π. No document relates the toy's μ and φ quantitatively to τ's V₀ and f.

The worklog's chunk 3 states what this means for the program: "In 3+1, the program's actual dimension, Coleman–Mermin–Wagner does not apply. There the self-dual coset model can break the continuous U(1) itself, with τ an exactly massless Goldstone. §10's τ has a potential, so the explicit breaking is in the program anyway." Its revised conclusion is that the toy supports broken reciprocity in the form "a pseudo-Goldstone polarization angle with a ρ-symmetric potential" (`notes/toy-lagrangian.md`, 'Chunk 3 results'; [the polarization as a Goldstone angle](/wiki/symmetry-breaking/goldstone-angle)).

### What they do not show

#11 §10 ends the paragraph: "None of this tests the cosmology; it only shows the structure is consistent." The toy note says the same in its limitations: "**Motivation, not result.** In a parent framework the polarization angle is identified with a dark-energy field. The Goldstone structure here is consistent with that, but untested by it." (toy note §6). Both toys are field theories at d = 1 without gravity or an expanding background, so they say nothing about w.

## Parameters and tests

- **Free numbers.** V₀, fixed by Ω_DE; f; and τᵢ, the initial value. Two remain for three observables, w₀, wₐ and the turnaround time t_turn ([the dark-energy over-constraint](/wiki/cosmology/dark-energy/over-constraint)).
- **Near-term test.** [Row 4](/wiki/predictions/dark-energy-drift): "DR3+ constant −1 (kills τ-sector); robust intrinsic w < −1 (kills outright) — DR2 already favors a crossing above z ≈ 0.4 (§10)" (#11 §13).
- **Long-horizon consequence.** [Row 5: the fate of the expansion](/wiki/predictions/fate-of-expansion), "Turnaround = conjugate bounce" (#11 §13), which needs V(τ) < 0 ([the turnaround as the conjugate bounce](/wiki/cosmology/scale-factor-duality/conjugate-bounce); see flag 27 in `review/wiki-build-flags.md`).
- **Safety.** τ is extremely light; the lab notebook argues that as a [pseudo-Goldstone field](/wiki/symmetry-breaking/goldstone-and-higgs) it produces no detectable [fifth force](/wiki/gravity/spin-2-fields/yukawa-forces#fifth-forces-a-yukawa-term-beside-gravity-t) ([fifth-force safety of τ](/wiki/cosmology/dark-energy/tau-fifth-force)).

## What is open

- **The origin of the potential.** [Open: the origin of the ρ-preserving potential](/wiki/symmetry-breaking/rho-preserving-potential); "a derivation of the ρ-preserving potential" is an open end in the root `CLAUDE.md`.
- **The sign of the potential.** V₀[1 + cos(τ/f)] is never negative for V₀ > 0, yet the turnaround needs V < 0; no document reconciles the two ([Open: the sign of V(τ) and the turnaround](/wiki/cosmology/dark-energy/potential-sign); flag 27 in `review/wiki-build-flags.md`).
- **Mixing with the absorbed modes.** [Open: τ–Stückelberg mixing (OP6)](/wiki/gravity/momentum-graviton/tau-stuckelberg-mixing).
- **Kinetic or potential energy.** The lab notebook motivates near-constant dark energy as kinetic energy in the dual frame and then implements it as τ's potential energy; no document derives the link ([Open: dual kinetic energy versus τ's potential](/wiki/cosmology/scale-factor-duality/dual-kinetic-link)).
- **τ's lightness** among the ten moduli of Λ(d) at d = 4 is a postulate [P] (#1 §2), and the fate of the other nine is open ([Open: field content of the broken vacuum](/wiki/phase-space/modular-field/field-content)).

## History

- **v0.1, the lab notebook (September 2026).** #1 §3 writes the action and potential; §4 argues fifth-force safety; §7 identifies dark energy with τ (thawing, w ≥ −1, the turnaround, the over-constraint); §9 row 5 sets the test against DESI DR3; the §12 summary calls τ "a dark energy field that is literally the Maslov angle of the vacuum, forced by topology to a periodic potential, hence thawing, never phantom, and destined to go negative" (see flag 27 in `review/wiki-build-flags.md`).
- **v0.2.** After [Debt 3](/wiki/history/debts), the notebook lists "row 5 (thawing, no-phantom, DESI DR3)" among the program's distinctive, still-live content.
- **v0.3.** Strict P2 is found to erase τ, and P2′ restores it (above).
- **Debt 1.** Calc note #8 shows that the momentum graviton's sector adds no vacuum energy, "leaving dark energy entirely to τ as the cosmology chapter had assumed" (#1 'Addendum (v0.6)'), and that τ is not absorbed by X at leading order (§3).
- **v1 (#9 §8).** The sector as a numbered section, with "V₀ fixed by Ω_DE" and the fits marked "[T — refresh citations before publication]".
- **#11 v2.0.** §10 states the sector in its present form, before the DR2 paragraph. The [handoff](/wiki/history/documents/handoff) lists τ among the live results: "τ = hilltop/axion quintessence on the Maslov circle; thawing, w ≥ −1 always, eventual negative V ⇒ turnaround = conjugate bounce" (`HANDOFF.md` §2).
- **#11 v2.1 (2026-10-19).** After round 3, §10 gains the "Under pressure (v2.1)" paragraph on DESI DR2.
- **#11 v2.2 (2026-10-20).** §10 gains the toy-model support, and P2′ its refinement: the polarization is a Goldstone angle that needs a ρ-preserving potential.
- **The popular articles.** The journey article #10 gives the program's slogan: dark energy is "not a substance but a *position*", and "dark matter is the mirror-world's stuff; dark energy is the angle of the mirror" ('The referee is already on the field'). The other article, #12, describes dark energy as "the energy stored in that orientation's displacement from its resting value" ('Dark energy as the orientation of the split'). Both are explanation only, not sources for status ([the popular articles](/wiki/history/documents/popular-articles)).

## Superseded: the potential's origin in the rigid ω

The lab notebook's v0.1 attributed the existence of τ's potential to the rigidity of ω. In #1 §3 the potential's "*existence* comes from the explicit breaking of Grassmannian rotations by the rigid ω (P2) — the rigidity is the 'instanton' that tilts the circle", tagged [P/O]. #1 §1 lists this as one of the "triple duty" roles of P2, which "supplies the explicit breaking that gives the dark-energy field its potential (§5)"; the potential is in fact in #1 §3, not §5 (`review/wiki-build-flags.md` item 10). The §12 summary repeats it: reciprocity is broken "with a rigid symplectic form as its explicit tilt".

The later documents replace this account step by step.

1. Calc note #5, writing the repair P2′, lists "the origin of τ's potential under P2′ (what explicitly breaks Λ(d) rotations — candidate: the section choice itself, or matter loops)" among the problems now open (`notes/debt1a-geometric-core.md` §F).
2. The toy models show that with only ω rigid, ρ sits inside a continuous U(1) and the polarization is a Goldstone angle [D][V]; a definite polarization needs a potential that brings "more structure than ω alone" (#11 §4, v2.2).
3. The root `CLAUDE.md` lists the derivation of that potential as open.

So rigidity of ω alone does not tilt the circle; the potential's periodicity [D] stands, and its origin is [Open: the origin of the ρ-preserving potential](/wiki/symmetry-breaking/rho-preserving-potential). The superseded statement is listed on [superseded statements](/wiki/status/superseded).

## Sources

- `papers/broken-born-checkpoint-v2.md` §10 — the identification and its tag, the fits, the "Under pressure (v2.1)" paragraph, the toy-model support and its limit
- `CLAUDE.md` 'Since the handoff' — "under real pressure ahead of DR3"; the derivation of the ρ-preserving potential as an open end
- `papers/broken-born-checkpoint-v2.md` §4 — P2′ and its v2.2 refinement; §6 — τ as the Maslov phase of the Shilov boundary; §7.3 — the wedge sector's zero vacuum energy and its scope; §7.5 — τ un-eaten; §13 rows 4–5 — the tests; §15 — the degeneration risk
- `papers/reciprocity-toy-models.md` §2, §4, §6 — the compact Goldstone angle, the bounded potential V_b at H = 1, "Motivation, not result"
- `verify/toy_coset.py` — the Hessian rank and V_b at H = 1 (current output in `scripts/check.sh`)
- `HANDOFF.md` §2 — τ among the live results
- `notes/broken-born-theory.md` §1–§3 — P2's "triple duty", τ ≡ f·arg det² and its tags, the action and potential; §7 — hilltop thawing and the corridor; §12 — the summary; 'Addendum (v0.3)' — strict P2 erases τ, P2′ restores it
- `notes/broken-born-program-v1.md` §8 — V₀ fixed by Ω_DE
- `notes/debt1a-geometric-core.md` §B — the rigid branch without τ; §F — the origin of τ's potential under P2′, open
- `notes/debt1a-iv-beta-coefficients.md` §2 — dark energy left entirely to the τ sector
- `notes/toy-lagrangian.md` 'Chunk 1 results', 'Chunk 2 results', 'Chunk 3 results' — the Goldstone angle as τ's circle, the thawing reading, the pseudo-Goldstone conclusion
- `review/wiki-build-flags.md` item 43 — the corridor in the region of DR2's fits, and the slope that separates it from DR2's crossing; items 1, 10 and 27 — the suspected source errors quoted on this page
- `popsci/angle-of-the-mirror.md` 'The referee is already on the field', `popsci/universes-other-half.md` 'Dark energy as the orientation of the split' — the popular framing
