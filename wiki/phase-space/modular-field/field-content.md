---
title: "Open: field content of the broken vacuum"
weight: 60
status: open
description: "The graviton, the momentum graviton X, the ten moduli of Λ(d) and matter: the Debt-1 notes resolved X as a massive spin-2 field, but whether inverse-Higgs constraints remove the nine non-Maslov moduli was never worked out."
provenance: [O]
sources:
  - "notes/debt1a-geometric-core.md §D"
  - "notes/debt1a-geometric-core.md §E"
  - "notes/debt1a-geometric-core.md §F"
  - "notes/debt1a-ii-X-classification.md §1"
  - "notes/debt1a-ii-X-classification.md §3"
  - "notes/debt1a-ii-X-classification.md §4"
  - "notes/debt1a-ii-X-classification.md §5"
  - "notes/debt1a-iii-tuning-test.md §4"
  - "notes/debt1a-iv-beta-coefficients.md §3"
  - "notes/broken-born-theory.md §2"
  - "notes/broken-born-theory.md §8"
  - "papers/broken-born-checkpoint-v2.md §4"
  - "papers/broken-born-checkpoint-v2.md §7"
  - "papers/broken-born-checkpoint-v2.md §14"
  - "papers/reciprocity-toy-models.md §2"
  - "HANDOFF.md §2"
  - "HANDOFF.md §4"
---

*The field content of the broken vacuum is the list of fields that the program's geometry leaves in play once the vacuum has chosen a polarization: the ordinary metric, the momentum graviton X, the ten moduli of [the Lagrangian Grassmannian](/wiki/phase-space/modular-field/lagrangian-grassmannian) (the dark-energy field τ plus nine more), and matter. Calc note #5 wrote the list down and marked it partial. The later Debt-1 notes settled what X is: a massive spin-2 field. Whether the nine extra moduli survive as fields, or are removed by inverse-Higgs constraints (relations that turn some Goldstone-type fields into derivatives of others), was never worked out. The question is open, and it is not on the checkpoint's numbered list of open problems.*

**Status:** Open [O] — calc note #5 §D and §F item 4; not carried into #11 §14 or into the handoff's open list — the X part was resolved by calc note #6 (a massive spin-2 field); the count of surviving moduli has not been computed ([open problems and the queue](/wiki/status/open-problems)).

## The list

Calc note #5, in its section "Quadratic spectrum and the ghost question [partial]" (§D):

```text
h_μν (10, graviton) ⊕ X_μν (10, momentum graviton) ⊕ Λ(d) σ-modes (10: τ plus nine) ⊕ matter
```

The note attaches to the nine "of which inverse-Higgs constraints likely eliminate most [O]".

Entry by entry:

- **h_μν** is the fluctuation of the spacetime metric g = Im Z about the vacuum, a symmetric tensor with ten components in four dimensions: the graviton.
- **X_μν** is Re Z, the program's second symmetric tensor ([the modular field Z = X + iY](/wiki/phase-space/modular-field/modular-field-z)).
- **The Λ(d) σ-modes.** The vacuum's polarization can vary from place to place, so it is a field with values in Λ(d), the target space of a nonlinear sigma model ([coset and hyperbolic sigma models](/wiki/symmetry-breaking/toy-models/coset-model/sigma-models)). Its fluctuations along the ten directions of Λ(4) are the σ-modes. One direction is the Maslov circle, whose angle is τ ([τ as the Maslov phase](/wiki/phase-space/modular-field/maslov-phase)); the other nine are, in the lab notebook's words, "the nine non-Maslov directions" (#1 §8).
- **Matter** is the x-polarized and p-polarized matter of [postulate P4](/wiki/program/postulates/p4-polarized-matter).

The tens count components, not propagating modes. A massive spin-2 field such as X carries five polarizations (#6 §3).

## What happened to X

Calc note #6 resolved X by symmetry and consistency arguments. The translations Z → Z + B make it shift-symmetric, so it is never auxiliary (§1); its local shifts make it a second graviton, which the multi-graviton no-go excludes as a massless field (§2); and the polarization choice breaks the local shifts, so that "the four would-be Goldstones π_μ of the broken λ-gauge are eaten; X becomes a **massive spin-2** with its five polarizations, mass M_X = the polarization-breaking scale" (§3). Its closing summary: "**Resolved:** the three-way classification. Not healthy-by-default, not auxiliary, not necessarily ghost: *massive spin-2, conditionally healthy*" (§5). See [why X must be massive](/wiki/gravity/momentum-graviton/forcing-chain) and [the gravitational Higgs mechanism](/wiki/gravity/momentum-graviton/gravitational-higgs).

After the tuning test and the β coefficients, the spin-2 spectrum is one massless graviton, even under reciprocity, and one massive spin-2 field, X, odd under it (#8 §3; #11 §7.5; [spectrum and parity](/wiki/gravity/momentum-graviton/spectrum-and-parity)).

The documents describe the absorbed modes in two ways. Calc note #6 says "the four would-be Goldstones π_μ" are eaten (§3), and #11 §7.1 follows it ("X eats the four Goldstones"). Calc note #8 says the Higgsing "eats the vector π_μ and the *longitudinal scalar of the λ-gradient sector*" (§3). No document reconciles the two wordings ([source conflicts](/wiki/history/documents/source-conflicts)).

## Superseded: the three-way classification of X

Calc note #5 had posed the X question as a calculation: "expand the generalized curvature scalar of (ω, H_Z) to quadratic order in X about X = 0 on the section, with ω-generalized diffeomorphisms as the gauge symmetry, and classify X as one of" three outcomes (§D):

1. "**healthy propagating** → dynamical momentum-space gravity (Born's dream, linearized)";
2. "**auxiliary** (no derivatives at quadratic order) → integrate out → a *contact, momentum-structured* four-χ operator, i.e. the gate delivered directly";
3. "**ghost** → fatal to the geometric sector."

"Outcomes 1 and 2 both serve the program; only 3 kills." Calc note #6 replaced the question rather than answering it in these terms. Its shift symmetry rules out the second outcome: "'auxiliary X' (the soft outcome 2) is off the table at the fundamental level" (§1; [shift symmetry](/wiki/gravity/momentum-graviton/shift-symmetry)). Its no-go and Higgs arguments then give an answer the list did not offer in that form: "Not healthy-by-default, not auxiliary, not necessarily ghost: *massive spin-2, conditionally healthy*" (§5). The curvature expansion itself is not reported in any document. Outcome 2 had been the cheapest route to the dark-matter gate ("outcome 2 gives it most cheaply", #5 §E); with it gone, the gate comes from integrating out the massive X between conjugate-matter bilinears (#6 §4; [the gate mechanism](/wiki/dark-matter/conjugate-matter/gate-mechanism)).

## Chat-only: massive X waves

Among the results that exist only in the old claude.ai chat, the handoff lists a comparison of the program's field equations with general relativity that ends "X-waves massive, 5 polarizations, frequency floor" (`HANDOFF.md` §4). The massive spin-2 nature and the five polarizations are in calc note #6; the frequency floor appears nowhere outside that line of the handoff. See [two gravitational charges and the conjugate field equations (chat-only)](/wiki/gravity/momentum-graviton/chat-only-results).

## The open question: the nine moduli

### Background: inverse-Higgs constraints [T]

When a symmetry breaks spontaneously, each broken generator usually brings one massless Goldstone field ([Goldstone modes and the Higgs mechanism](/wiki/symmetry-breaking/goldstone-and-higgs)). For symmetries that act on spacetime itself this counting can fail, because one Goldstone field can turn out to be a derivative of another and need not be counted separately. The standard example is a membrane in a space of one more dimension. It breaks the translations perpendicular to itself and the rotations that would tilt it, but the local tilt of a membrane is the gradient of its displacement, so the rotation Goldstones are derivatives of the translation Goldstone and are not independent fields. In the algebra the constraint is available when the commutator of an unbroken translation with one broken generator contains another broken generator; the Goldstone field of the first can then be eliminated in favor of derivatives of the second (Ivanov–Ogievetsky 1975 †; Low–Manohar 2002 †).

### The program's expectation [O]

Calc note #5 expects such constraints to "likely eliminate most" of the nine (§D), and lists among the items "Now precisely open": "(4) inverse-Higgs accounting of the nine heavy moduli" (§F). The note does not say which broken generators or which commutators would supply the constraints, and no later note returns to the question. The item is absent from #11 §14 and from the handoff's open list (`HANDOFF.md` §2), but no document closes it, so this wiki keeps it open.

### What the documents do say about the ten

- **Where the nine sit.** They are the directions in which the polarization can move without changing det², the function whose angle is τ; the points with one value of det² form a copy of SU(d)/SO(d) [T] ([the Maslov class](/wiki/phase-space/modular-field/lagrangian-grassmannian#the-maslov-class)).
- **Which one is light.** That τ is the lightest modulus, "with the other nine directions heavy, is assumed **[P]**" (#1 §2). No document derives a mass for any of the nine, and the source of τ's own potential is open ("what explicitly breaks Λ(d) rotations", #5 §F item 3).
- **None is eaten by X.** "The Λ(d) moduli, τ included, are not the eaten modes — they carry the compact phase directions, which constant shifts do not generate" (#6 §3); τ "survives as the light field" (#8 §3; [τ is not eaten](/wiki/gravity/momentum-graviton/tau-not-eaten)).
- **They bound the second frame.** "J carries only the 10 compact moduli of U(d)/O(d) — not a full second metric" (#7 §4; [constrained bimetric gravity](/wiki/gravity/tuning-test/constrained-bimetric)).
- **The toy model cannot help.** In the d = 1 coset model the compact Goldstone angle "parametrizes the Lagrangian Grassmannian Λ(1)" (toy-model note §2), a single circle, so the toy has no counterpart of the nine ([model I vacua](/wiki/symmetry-breaking/toy-models/coset-model/vacua)).

### A sketch that depends on the answer

The lab notebook's polarization-genesis sketch, tagged "[O, sketched]", needs the nine to exist and to decay: "at reheating, the heavy Grassmannian moduli (the nine non-Maslov directions) decay; their branching into x- versus p-polarized quanta is set by the vacuum tilt angle, Ω_χ/Ω_x^(0) ~ tan²θ_pol, after which baryogenesis processes the x-side" (#1 §8). It calls itself "a shape, not a mechanism". Calc note #5, written later, expects inverse-Higgs constraints to eliminate most of the same nine. No document reconciles the two, and the abundance ratio Ω_χ : Ω_b = 5.4 : 1 that the sketch addresses is open item 7 ([Open: polarization-genesis (OP7)](/wiki/dark-matter/candidates/polarization-genesis)).

## Signs of health

Calc note #5 recorded two encouraging signs for the kinetic terms of this field content (§D). The first: "the Siegel target metric Tr(Y⁻¹dZ Y⁻¹dZ̄) is positive-definite", so a kinetic term for Z built on it has the healthy sign in every direction ([the target metric](/wiki/phase-space/modular-field/siegel-domain#the-target-metric)). The second comes from double field theory (DFT), string theory's doubled geometry: "the DFT precedent (graviton + B-field + dilaton, ghost-free) shows doubled-geometry kinetic operators can be healthy [T]" ([double field theory](/wiki/phase-space/born-geometry/double-field-theory)).

Both signs belong to positive (Euclidean) metrics. With a Lorentzian metric "the invariant target metric" becomes "indefinite" (#6 §3), and the extension to spacetime signature is open item 3 ([Open: Lorentzian dressing (OP3)](/wiki/phase-space/born-geometry/lorentzian-dressing)).

## Sources

- `notes/debt1a-geometric-core.md` §D — the field content, the nine moduli, the three-way classification and the signs of health.
- `notes/debt1a-geometric-core.md` §E, §F — the gate's cheapest route through outcome 2; item 3, the origin of τ's potential; item 4, the inverse-Higgs accounting.
- `notes/debt1a-ii-X-classification.md` §1, §3, §4, §5 — the auxiliary outcome excluded; X a massive spin-2 field with five polarizations; the moduli not eaten; the Lorentzian caveat; the gate from integrating out massive X; the resolved classification.
- `notes/debt1a-iii-tuning-test.md` §4 — the ten compact moduli carried by J.
- `notes/debt1a-iv-beta-coefficients.md` §3 — the eaten modes in #8's wording; τ survives; parity of the two tensors.
- `notes/broken-born-theory.md` §2, §8 — τ the lightest modulus [P]; the polarization-genesis sketch.
- `papers/broken-born-checkpoint-v2.md` §4, §7, §14 — P4's polarized matter; X's chain and spectrum; the current open list, which does not carry this item.
- `papers/reciprocity-toy-models.md` §2 — Λ(1) in model I.
- `HANDOFF.md` §2, §4 — the handoff's open list; the chat-only massive X waves.
