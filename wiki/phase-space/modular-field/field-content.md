---
title: "Open: field content of the broken vacuum"
weight: 60
status: open
description: "The graviton, the momentum graviton X, the ten moduli of Λ(d) and matter: the field-equation notes resolved X as a massive spin-2 field, but whether inverse-Higgs constraints remove the nine non-Maslov moduli was never worked out."
provenance: [O]
sources:
  - "notes/geometric-core.md §D"
  - "notes/geometric-core.md §E"
  - "notes/geometric-core.md §F"
  - "notes/x-classification.md §1"
  - "notes/x-classification.md §2"
  - "notes/x-classification.md §3"
  - "notes/x-classification.md §4"
  - "notes/x-classification.md §5"
  - "notes/tuning-test.md §4"
  - "notes/beta-coefficients.md §3"
  - "notes/broken-born-theory.md §2"
  - "notes/broken-born-theory.md §8"
  - "wiki/papers/broken-born-checkpoint-v2.md §4"
  - "wiki/papers/broken-born-checkpoint-v2.md §7"
  - "wiki/papers/broken-born-checkpoint-v2.md §14"
  - "wiki/papers/reciprocity-toy-models.md §2"
  - "HANDOFF.md §2"
  - "HANDOFF.md §4"
  - "review/wiki-build-flags.md item 55"
  - "notes/gate-mechanism.md §2"
---

*The field content of the broken vacuum is the list of fields that the program's geometry leaves in play once the vacuum has chosen a polarization: the ordinary metric, [the momentum graviton X](../../gravity/momentum-graviton/_index.md), the ten moduli of [the Lagrangian Grassmannian](lagrangian-grassmannian.md) (the dark-energy field τ plus nine more), and matter. [Calc note #5](../../history/documents/field-equation-notes.md) wrote the list down and marked it partial. The later field-equation notes settled what X is: a massive spin-2 field. Whether the nine extra moduli survive as fields, or are removed by [inverse-Higgs constraints](../../symmetry-breaking/inverse-higgs-constraints.md) (relations that turn some Goldstone-type fields into derivatives of others), was never worked out. The question is open, and it is not on the [checkpoint](../../history/documents/checkpoint.md)'s numbered list of open problems.*

**Status:** Open [O] — calc note [#5 §D](../../../notes/geometric-core.md#d-quadratic-spectrum-and-the-ghost-question-partial) and [§F item 4](../../../notes/geometric-core.md#f-status-after-tonight); not carried into [#11 §14](../../papers/broken-born-checkpoint-v2.md#14-open-problems) or into [the handoff](../../history/documents/handoff.md)'s open list — the X part was resolved by calc note [#6](../../../notes/x-classification.md) (a massive spin-2 field); the count of surviving moduli has not been computed ([open problems and the queue](../../status/open-problems.md)).

## The list

Calc note #5, in its section "Quadratic spectrum and the ghost question [partial]" ([§D](../../../notes/geometric-core.md#d-quadratic-spectrum-and-the-ghost-question-partial)):

```text
h_μν (10, graviton) ⊕ X_μν (10, momentum graviton) ⊕ Λ(d) σ-modes (10: τ plus nine) ⊕ matter
```

The note attaches to the nine "of which inverse-Higgs constraints likely eliminate most [O]".

Entry by entry:

- **h_μν** is the fluctuation of the spacetime metric g = Im Z about the vacuum, a symmetric tensor with ten components in four dimensions: the graviton.
- **X_μν** is Re Z, the program's second symmetric tensor ([the modular field Z = X + iY](modular-field-z.md)).
- **The Λ(d) σ-modes.** The vacuum's polarization can vary from place to place, so it is a field with values in Λ(d), the target space of a nonlinear sigma model ([coset and hyperbolic sigma models](../../symmetry-breaking/toy-models/coset-model/sigma-models.md)). Its fluctuations along the ten directions of Λ(4) are the σ-modes. One direction is the Maslov circle, whose angle is τ ([τ as the Maslov phase](maslov-phase.md)); the other nine are, in the [lab notebook](../../history/documents/lab-notebook.md)'s words, "the nine non-Maslov directions" ([#1 §8](../../../notes/broken-born-theory.md#8-polarization-genesis-o-sketched)).
- **Matter** is the x-polarized and p-polarized matter of [postulate P4](../../program/postulates/p4-polarized-matter.md).

The tens count components, not propagating modes. A massive spin-2 field such as X carries five polarizations ([#6 §3](../../../notes/x-classification.md#3-the-mass-mechanism-and-the-endpoint-d--structural)).

## What happened to X

Calc note #6 resolved X by symmetry and consistency arguments. The translations Z → Z + B make it shift-symmetric, so it is never auxiliary ([§1](../../../notes/x-classification.md#1-the-shift-symmetry-d--rigorous)); its local shifts make it a second graviton, which the [multi-graviton no-go](../../gravity/spin-2-fields/multi-graviton-no-go.md) excludes as a massless field ([§2](../../../notes/x-classification.md#2-the-gauge-structure-and-the-no-go-d--t)); and the polarization choice breaks the local shifts, so that "the four would-be Goldstones π_μ of the broken λ-gauge are eaten; X becomes a **massive spin-2** with its five polarizations, mass M_X = the polarization-breaking scale" ([§3](../../../notes/x-classification.md#3-the-mass-mechanism-and-the-endpoint-d--structural)). Its closing summary: "**Resolved:** the three-way classification. Not healthy-by-default, not auxiliary, not necessarily ghost: *massive spin-2, conditionally healthy*" ([§5](../../../notes/x-classification.md#5-the-field-equation-problem-after-this-chunk)). See [why X must be massive](../../gravity/momentum-graviton/forcing-chain.md) and [the gravitational Higgs mechanism](../../gravity/momentum-graviton/gravitational-higgs.md).

After [the tuning test](../../gravity/tuning-test/_index.md) and the β coefficients, the spin-2 spectrum is one massless graviton, even under reciprocity, and one massive spin-2 field, X, odd under it ([#8 §3](../../../notes/beta-coefficients.md#3-spectrum-parameters-selection-structure-d--t); [#11 §7.5](../../papers/broken-born-checkpoint-v2.md#75-spectrum-d); [spectrum and parity](../../gravity/momentum-graviton/spectrum-and-parity.md); on the parities under [#11 §6](../../papers/broken-born-checkpoint-v2.md#6-the-modular-field)'s Z → −Z⁻¹, see flag 39 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md)).

The documents describe the absorbed modes in two ways. Calc note #6 says "the four would-be Goldstones π_μ" are eaten ([§3](../../../notes/x-classification.md#3-the-mass-mechanism-and-the-endpoint-d--structural)), and [#11 §7.1](../../papers/broken-born-checkpoint-v2.md#71-the-chain-d--t) follows it ("X eats the four Goldstones"). Calc note #8 says the Higgsing "eats the vector π_μ and the *longitudinal scalar of the λ-gradient sector*" ([§3](../../../notes/beta-coefficients.md#3-spectrum-parameters-selection-structure-d--t)). No document reconciles the two wordings ([source conflicts](../../history/documents/source-conflicts.md)).

## Superseded: the three-way classification of X

Calc note #5 had posed the X question as a calculation: "expand the generalized curvature scalar of (ω, H_Z) to quadratic order in X about X = 0 on the section, with ω-generalized diffeomorphisms as the gauge symmetry, and classify X as one of" three outcomes ([§D](../../../notes/geometric-core.md#d-quadratic-spectrum-and-the-ghost-question-partial)):

1. "**healthy propagating** → dynamical momentum-space gravity (Born's dream, linearized)";
2. "**auxiliary** (no derivatives at quadratic order) → integrate out → a *contact, momentum-structured* four-χ operator, i.e. the gate delivered directly";
3. "**ghost** → fatal to the geometric sector."

"Outcomes 1 and 2 both serve the program; only 3 kills." Calc note #6 replaced the question rather than answering it in these terms. Its shift symmetry rules out the second outcome: "'auxiliary X' (the soft outcome 2) is off the table at the fundamental level" ([§1](../../../notes/x-classification.md#1-the-shift-symmetry-d--rigorous); [shift symmetry](../../gravity/momentum-graviton/shift-symmetry.md)). Its no-go and Higgs arguments then give an answer the list did not offer in that form: "Not healthy-by-default, not auxiliary, not necessarily ghost: *massive spin-2, conditionally healthy*" ([§5](../../../notes/x-classification.md#5-the-field-equation-problem-after-this-chunk)). The curvature expansion itself is not reported in any document. Outcome 2 had been the cheapest route to the shape of the dark-matter gate ("outcome 2 gives it most cheaply", [#5 §E](../../../notes/geometric-core.md#e-the-gate-problem--the-mechanism-found-d--structural)); with it gone, the gate comes from integrating out the massive X between [conjugate-matter](../../dark-matter/conjugate-matter/_index.md) bilinears ([#6 §4](../../../notes/x-classification.md#4-consequences-downstream-d--structural-with-one-honest-downgrade); [the gate mechanism](../../dark-matter/conjugate-matter/gate-mechanism.md)). That route is disputed: [`notes/gate-mechanism.md`](../../../notes/gate-mechanism.md) (2026-10-28; two derivations, the second blind; not reviewed) finds that exchanging the massive X cannot produce the gate ([§2](../../../notes/gate-mechanism.md#2-exchanging-the-x-of-7-cannot-produce-the-gate)), and flag 55 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md), pending, proposes [P] for the gate and μ and [O] for the mechanism ([the gate mechanism](../../dark-matter/conjugate-matter/gate-mechanism.md#exchanging-x-cannot-produce-the-gate)).

## Chat-only: massive X waves

Among the results that exist only in the old claude.ai chat, the handoff lists a comparison of the program's field equations with [general relativity](../../gravity/spin-2-fields/general-relativity.md) that ends "X-waves massive, 5 polarizations, frequency floor" ([`HANDOFF.md` §4](../../../HANDOFF.md#4-results-that-exist-only-in-the-chat-not-in-any-artifact)). The massive spin-2 nature and the five polarizations are in calc note #6; the frequency floor appears nowhere outside that line of the handoff. See [two gravitational charges and the conjugate field equations (chat-only)](../../gravity/momentum-graviton/chat-only-results.md).

## The open question: the nine moduli

### Background: inverse-Higgs constraints [T]

When a symmetry breaks spontaneously, each broken generator usually brings one massless Goldstone field ([Goldstone modes and the Higgs mechanism](../../symmetry-breaking/goldstone-and-higgs.md)). For symmetries that act on spacetime itself this counting can fail, because one Goldstone field can turn out to be a derivative of another and need not be counted separately. The standard example is a membrane in a space of one more dimension. It breaks the translations perpendicular to itself and the rotations that would tilt it, but the local tilt of a membrane is the gradient of its displacement, so the rotation Goldstones are derivatives of the translation Goldstone and are not independent fields. In the algebra the constraint is available when the commutator of an unbroken translation with one broken generator contains another broken generator; the Goldstone field of the first can then be eliminated in favor of derivatives of the second (Ivanov–Ogievetsky 1975 †; Low–Manohar 2002 †).

### The program's expectation [O]

Calc note #5 expects such constraints to "likely eliminate most" of the nine ([§D](../../../notes/geometric-core.md#d-quadratic-spectrum-and-the-ghost-question-partial)), and lists among the items "Now precisely open": "(4) inverse-Higgs accounting of the nine heavy moduli" ([§F](../../../notes/geometric-core.md#f-status-after-tonight)). The note does not say which broken generators or which commutators would supply the constraints, and no later note returns to the question. The item is absent from [#11 §14](../../papers/broken-born-checkpoint-v2.md#14-open-problems) and from the handoff's open list ([`HANDOFF.md` §2](../../../HANDOFF.md#2-scientific-state-one-screen)), but no document closes it, so it is open.

### What the documents do say about the ten

- **Where the nine sit.** #1 calls them "the nine non-Maslov directions" ([§8](../../../notes/broken-born-theory.md#8-polarization-genesis-o-sketched)): the directions in which the polarization can move without changing det², the function whose angle is τ; the points with one value of det² form a copy of SU(d)/SO(d) [T] ([the Maslov class](lagrangian-grassmannian.md#the-maslov-class)).
- **Which one is light.** That τ is the lightest modulus, "with the other nine directions heavy, is assumed **[P]**" ([#1 §2](../../../notes/broken-born-theory.md#2-kinematic-core)). No document derives a mass for any of the nine, and the source of τ's own potential is open ("what explicitly breaks Λ(d) rotations", [#5 §F item 3](../../../notes/geometric-core.md#f-status-after-tonight)).
- **None is eaten by X.** "The Λ(d) moduli, τ included, are not the eaten modes — they carry the compact phase directions, which constant shifts do not generate" ([#6 §3](../../../notes/x-classification.md#3-the-mass-mechanism-and-the-endpoint-d--structural)); τ "survives as the light field" ([#8 §3](../../../notes/beta-coefficients.md#3-spectrum-parameters-selection-structure-d--t); [τ is not eaten](../../gravity/momentum-graviton/tau-not-eaten.md)).
- **They bound the second frame.** "J carries only the 10 compact moduli of U(d)/O(d) — not a full second metric" ([#7 §4](../../../notes/tuning-test.md#4-the-picture-that-emerges-constrained-bimetric-gravity-d--structural); [constrained bimetric gravity](../../gravity/tuning-test/constrained-bimetric.md)).
- **The toy model cannot help.** In the d = 1 [coset model](../../symmetry-breaking/toy-models/coset-model/_index.md) the compact [Goldstone angle](../../symmetry-breaking/goldstone-angle.md) "parametrizes the Lagrangian Grassmannian Λ(1)" ([toy-model note §2](../../papers/reciprocity-toy-models.md#2-model-i-a-coset-sigma-model-of-h-k)), a single circle, so the toy has no counterpart of the nine ([model I vacua](../../symmetry-breaking/toy-models/coset-model/vacua.md)).

### A sketch that depends on the answer

The lab notebook's polarization-genesis sketch, tagged "[O, sketched]", needs the nine to exist and to decay: "at reheating, the heavy Grassmannian moduli (the nine non-Maslov directions) decay; their branching into x- versus p-polarized quanta is set by the vacuum tilt angle, Ω_χ/Ω_x^(0) ~ tan²θ_pol, after which baryogenesis processes the x-side" ([#1 §8](../../../notes/broken-born-theory.md#8-polarization-genesis-o-sketched)). It calls itself "a shape, not a mechanism". Calc note #5, written later, expects inverse-Higgs constraints to eliminate most of the same nine. No document reconciles the two, and the abundance ratio Ω_χ : Ω_b = 5.4 : 1 that the sketch addresses is open item 7 ([Open: polarization-genesis (OP7)](../../dark-matter/candidates/polarization-genesis.md)).

## Signs of health

Calc note #5 recorded two encouraging signs for the kinetic terms of this field content ([§D](../../../notes/geometric-core.md#d-quadratic-spectrum-and-the-ghost-question-partial)). The first: "the Siegel target metric Tr(Y⁻¹dZ Y⁻¹dZ̄) is positive-definite", so a kinetic term for Z built on it has the healthy sign in every direction ([the target metric](siegel-domain.md#the-target-metric)). The second comes from double field theory (DFT), string theory's doubled geometry: "the DFT precedent (graviton + B-field + dilaton, ghost-free) shows doubled-geometry kinetic operators can be healthy [T]" ([double field theory](../born-geometry/double-field-theory.md)).

The first sign belongs to positive (Euclidean) metrics. With a Lorentzian metric "the invariant target metric" becomes "indefinite" ([#6 §3](../../../notes/x-classification.md#3-the-mass-mechanism-and-the-endpoint-d--structural)), and the extension to spacetime signature is open item 3 ([Open: Lorentzian dressing (OP3)](../born-geometry/lorentzian-dressing.md)).

## Sources

- [`notes/geometric-core.md` §D](../../../notes/geometric-core.md#d-quadratic-spectrum-and-the-ghost-question-partial) — the field content, the nine moduli, the three-way classification and the signs of health.
- [`notes/geometric-core.md` §E](../../../notes/geometric-core.md#e-the-gate-problem--the-mechanism-found-d--structural), [§F](../../../notes/geometric-core.md#f-status-after-tonight) — the gate's cheapest route through outcome 2; item 3, the origin of τ's potential; item 4, the inverse-Higgs accounting.
- [`notes/x-classification.md` §1](../../../notes/x-classification.md#1-the-shift-symmetry-d--rigorous), [§2](../../../notes/x-classification.md#2-the-gauge-structure-and-the-no-go-d--t), [§3](../../../notes/x-classification.md#3-the-mass-mechanism-and-the-endpoint-d--structural), [§4](../../../notes/x-classification.md#4-consequences-downstream-d--structural-with-one-honest-downgrade), [§5](../../../notes/x-classification.md#5-the-field-equation-problem-after-this-chunk) — the auxiliary outcome excluded; the massless option excluded by the no-go; X a massive spin-2 field with five polarizations; the moduli not eaten; the Lorentzian caveat; the gate from integrating out massive X; the resolved classification.
- [`notes/tuning-test.md` §4](../../../notes/tuning-test.md#4-the-picture-that-emerges-constrained-bimetric-gravity-d--structural) — the ten compact moduli carried by J.
- [`notes/beta-coefficients.md` §3](../../../notes/beta-coefficients.md#3-spectrum-parameters-selection-structure-d--t) — the eaten modes in #8's wording; τ survives; parity of the two tensors.
- [`notes/broken-born-theory.md` §2](../../../notes/broken-born-theory.md#2-kinematic-core), [§8](../../../notes/broken-born-theory.md#8-polarization-genesis-o-sketched) — τ the lightest modulus [P]; the polarization-genesis sketch.
- [`wiki/papers/broken-born-checkpoint-v2.md` §4](../../papers/broken-born-checkpoint-v2.md#4-postulates), [§7](../../papers/broken-born-checkpoint-v2.md#7-the-massive-momentum-graviton), [§14](../../papers/broken-born-checkpoint-v2.md#14-open-problems) — P4's polarized matter; X's chain and spectrum; the current open list, which does not carry this item.
- [`wiki/papers/reciprocity-toy-models.md` §2](../../papers/reciprocity-toy-models.md#2-model-i-a-coset-sigma-model-of-h-k) — Λ(1) in model I.
- [`HANDOFF.md` §2](../../../HANDOFF.md#2-scientific-state-one-screen), [§4](../../../HANDOFF.md#4-results-that-exist-only-in-the-chat-not-in-any-artifact) — the handoff's open list; the chat-only massive X waves.
- [`notes/gate-mechanism.md` §2](../../../notes/gate-mechanism.md#2-exchanging-the-x-of-7-cannot-produce-the-gate) and [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md) item 55 — exchanging the massive X gives no gate; the flag is pending.
