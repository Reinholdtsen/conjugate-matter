---
title: "The hard core: spontaneously broken Born reciprocity"
weight: 20
status: alive
description: "The program's protected assumption: Born reciprocity is an exact symmetry of the laws, spontaneously broken by the vacuum, with only the symplectic form ω rigid and the neutral metric η emergent as the order parameter."
provenance: [P]
sources:
  - "wiki/papers/broken-born-checkpoint-v2.md §3"
  - "wiki/papers/broken-born-checkpoint-v2.md §4"
  - "wiki/papers/broken-born-checkpoint-v2.md §5"
  - "wiki/papers/broken-born-checkpoint-v2.md §10"
  - "wiki/papers/broken-born-checkpoint-v2.md §15"
  - "wiki/papers/broken-born-checkpoint-v2.md App. A item 1"
  - "HANDOFF.md §1"
  - "wiki/papers/reciprocity-toy-models.md §1"
  - "wiki/papers/reciprocity-toy-models.md §2"
  - "wiki/papers/reciprocity-toy-models.md §3"
  - "wiki/papers/reciprocity-toy-models.md §4"
  - "wiki/papers/reciprocity-toy-models.md §5"
  - "wiki/papers/reciprocity-toy-models.md §6"
  - "notes/geometric-core.md §B"
  - "notes/broken-born-theory.md §0–§3"
  - "notes/broken-born-program-v1.md §0–§1"
  - "notes/broken-born-program-v1.md §11"
  - "notes/toy-lagrangian.md 'Chunk 1 results'"
  - "notes/toy-lagrangian.md 'Chunk 2 results'"
  - "notes/toy-lagrangian.md 'Chunk 4'"
  - "review/round4-adjudication.md 'Rulings' F3"
  - "verify/toy_coset.py"
  - "verify/toy_s4.py"
  - "verify/toy_s5.py"
  - "popsci/universes-other-half.md 'What one assumption purchases'"
  - "notes/literature-check.md §6"
  - "review/wiki-build-flags.md item 66"
  - "notes/dual-sector.md §8"
  - "review/wiki-build-flags.md item 70"
---

*The hard core is the assumption the Comatter program keeps fixed while its other claims are tested and revised: [Born reciprocity](../phase-space/reciprocity/born-reciprocity.md), the quarter-turn (x, p) → (p, −x) of quantum phase space (the space of positions and momenta taken together), is an exact symmetry of the laws, and the vacuum, the universe's lowest-energy state, breaks it spontaneously. Only one structure of phase space is fixed in advance, the [symplectic form](../phase-space/reciprocity/symplectic-form.md) ω, which encodes the constancy of Planck's constant. The neutral metric η, the structure that marks which directions count as position, belongs to the vacuum state rather than to the laws, and it is the [order parameter](../symmetry-breaking/order-parameter.md) that distinguishes our vacuum from its mirror image. A cooled magnet is the standard picture: the laws governing its atoms single out no direction, but its magnetized state points in one. [Checkpoint #11](../history/documents/checkpoint.md) records the hard core as intact and sharpened twice by corrections that later derivations forced. The [toy models](../symmetry-breaking/toy-models/_index.md), two small field theories built to test the idea, added two qualifications: a definite polarization, that is, a definite choice of which directions count as position, needs an extra potential, and the breaking has physical effect only once matter couples to the sign of the order parameter.*

**Status:** Alive — [P]: it is the content of postulates P1–P5 ([#11 §4](../papers/broken-born-checkpoint-v2.md#4-postulates)). [#11 §15](../papers/broken-born-checkpoint-v2.md#15-assessment) finds it "intact, twice sharpened by forced corrections (P2′; the w-dictionary)" (w is a fluid's [equation of state](../cosmology/dark-energy/quintessence.md#dark-energy-and-the-equation-of-state), the ratio of its pressure to its energy density); the w-dictionary is, as a map of fluid variables, the scale-factor duality of string cosmology with sources (flag 66, pending). The v2.2 refinement from the toy models is [D][V], checked in [`verify/toy_coset.py`](../../verify/toy_coset.py), [`verify/toy_s4.py`](../../verify/toy_s4.py) and [`verify/toy_s5.py`](../../verify/toy_s5.py) ([the toy-model scripts](../method/verification/toy-model-scripts.md)).

## Statement

[The handoff](../history/documents/handoff.md) states the hard core in one sentence: "Born reciprocity — the (x,p) → (p,−x) symmetry of quantum kinematics — taken as exact and spontaneously broken, with only the symplectic form ω rigid (ℏ-rigidity) and the neutral metric η emergent as the order parameter" ([`HANDOFF.md` §1](../../HANDOFF.md#1-what-this-project-is)). [#11 §15](../papers/broken-born-checkpoint-v2.md#15-assessment) abbreviates it as "spontaneously broken reciprocity, ω-only rigidity".

"Hard core" is Imre Lakatos's term for the part of a research programme that is not given up when a prediction fails; the auxiliary claims around it are revised instead ([Lakatos's methodology](../method/lakatosian-methodology.md)). The sentence makes three claims:

1. [Born reciprocity](../phase-space/reciprocity/born-reciprocity.md), ρ: (x, p) → (p, −x), is an exact symmetry of the laws, not only of the kinematics, where it holds in ordinary quantum mechanics ([Born's question](borns-question.md)).
2. The vacuum breaks it: the laws are symmetric and the ground state is not ([spontaneous symmetry breaking](../symmetry-breaking/spontaneous-symmetry-breaking.md)).
3. Of the structures on phase space only ω is fixed by the laws; η is a property of the vacuum, its [order parameter](../symmetry-breaking/order-parameter.md).

The formal content is the five [postulates](postulates/_index.md) of [#11 §4](../papers/broken-born-checkpoint-v2.md#4-postulates), each tagged [P]:

| Postulate | Content ([#11 §4](../papers/broken-born-checkpoint-v2.md#4-postulates)) | Role in the hard core |
| --- | --- | --- |
| [P1](postulates/p1-arena.md) | Physics on phase space with symplectic form ω and positive generalized metric H | the arena |
| [P2′](postulates/p2-prime.md) | Only ω is rigid; η is emergent, the order parameter | claim 3 |
| [P3](postulates/p3-reciprocity.md) | The action is invariant under the Born rotation generated by I = ω⁻¹H | claim 1 |
| [P4](postulates/p4-polarized-matter.md) | Matter comes in x-polarized (Standard Model) and p-polarized (χ) representations; both couple universally to H; gauge forces do not cross polarizations | how matter sits in the broken vacuum |
| [P5](postulates/p5-spontaneous-selection.md) | The vacuum selects a polarization; ours is x-tilted; the mirror vacuum is equally lawful | claim 2 |

## The structures ω, η and H

Phase space for d degrees of freedom carries three structures ([#11 §5](../papers/broken-born-checkpoint-v2.md#5-the-kinematic-core-and-the-compatibility-theorem); the [lab notebook](../history/documents/lab-notebook.md)'s [§2](../../notes/broken-born-theory.md#2-kinematic-core) gives their standard form, with blocks of size d and units scaled out):

```text
ω = [[0, 1], [−1, 0]]        η = [[0, 1], [1, 0]]        H = [[1, 0], [0, 1]]

I = ω⁻¹H      J = η⁻¹H      K = η⁻¹ω          I² = −1,   J² = K² = +1,   IJ = K
```

- **ω**, the [symplectic form](../phase-space/reciprocity/symplectic-form.md), is antisymmetric. It pairs each position with its momentum and is the classical form of [the commutator](../phase-space/reciprocity/canonical-commutator.md) [x, p] = iℏ; P2′ reads its rigidity as the constancy of Planck's constant: "symplectic rigidity ≡ constancy of ℏ".
- **η**, the neutral metric, is symmetric with as many negative as positive directions, so it has null directions. For one degree of freedom (d = 1) its two null lines are the eigenlines L± of K, and both are Lagrangian, that is, possible choices of "position" axis: "Choosing K is choosing which line is 'position'" ([toy-model note §1](../papers/reciprocity-toy-models.md#1-setting-and-prior-work); [Lagrangian polarizations](../phase-space/reciprocity/lagrangian-polarizations.md)).
- **H**, the positive generalized metric, carries the geometry: in the vacuum it has the form diag(g, g⁻¹), with g the space-time metric ([the compatibility theorem](../phase-space/born-geometry/compatibility-theorem.md)).
- **I, J, K** satisfy "a split-quaternion algebra (Born geometry [3†]; a unique compatible connection exists [7†])" ([#11 §5](../papers/broken-born-checkpoint-v2.md#5-the-kinematic-core-and-the-compatibility-theorem); [the structures ω, η, H](../phase-space/born-geometry/born-structures.md)).

How ρ acts on them is what makes η the order parameter. The lab notebook computed it at the standard point: ρ "preserves ω (it is symplectic), preserves H (it is orthogonal), and flips the sign of η, hence flips J and K while preserving I" [D] ([#1 §2](../../notes/broken-born-theory.md#2-kinematic-core)). A vacuum that carries a definite η is therefore carried by ρ to a different vacuum, the one with −η. After the repair described below, the [field-equation note](../history/documents/field-equation-notes.md) put it as "the earlier observation that reciprocity flips η now reads correctly as the broken symmetry moving the order parameter" ([`notes/geometric-core.md` §B](../../notes/geometric-core.md#b-the-inconsistency-and-the-forced-repair-d--structural)).

The documents name the order parameter in two ways. #11 P2′ writes "η = HJ, with the real structure J chosen spontaneously"; the toy-model note writes η = ωK, "K a real structure, K² = 1". The two agree, since J = η⁻¹H and K = η⁻¹ω, but the documents differ on which of J and K they call "the real structure"; [the order parameter](../symmetry-breaking/order-parameter.md) records both conventions. This page follows the toy-model note and works with K.

## Why only ω is rigid: the first sharpening

The lab notebook's first rigidity postulate, the [original P2](postulates/original-p2.md), fixed both structures: "ω and η are non-dynamical; only H carries degrees of freedom" ([#1 §1](../../notes/broken-born-theory.md#1-postulates)). The [compatibility theorem](../phase-space/born-geometry/compatibility-theorem.md) [T][V] shows what that allows:

```text
H > 0,   (η⁻¹H)² = +1   and   (ω⁻¹H)² = −1     ⇔     H = diag(g, g⁻¹),   g ∈ Sym⁺(d)
```

The statement is Freidel, Leigh and Minic's Born-geometry result; the block proof and the machine check (battery test T1, [the verification battery](../method/verification/battery.md)) are the program's ([#11 §5](../papers/broken-born-checkpoint-v2.md#5-the-kinematic-core-and-the-compatibility-theorem)). With both structures rigid, the field-equation note found the program empty ([`notes/geometric-core.md` §B](../../notes/geometric-core.md#b-the-inconsistency-and-the-forced-repair-d--structural), "[D — structural]"):

- the polarizations compatible with both structures are, in the note's word, discrete, "the 2^d coordinate-type splittings" (on "discrete", see flag 1 in [`review/wiki-build-flags.md`](../../review/wiki-build-flags.md); the conclusion is not affected), so there is "No Lagrangian Grassmannian, no Maslov circle, no τ field", and no dark-energy sector;
- with H = diag(g, g⁻¹) the [geometric action](../gravity/tuning-test/geometric-action.md) "is a functional of g alone: a pure metric theory. No momentum graviton, hence no geometric origin for the χ gate either";
- the note's verdict on this branch: it "reduces to GR + one bespoke SIDM model, with w ≡ −1 and the gate unexplained", that is, [general relativity](../gravity/spin-2-fields/general-relativity.md) (GR) plus one model of [self-interacting dark matter](../dark-matter/halo-astrophysics/self-interacting-dark-matter.md) (SIDM).

The repair was to "Freeze ω only — that is genuinely ℏ — and let η be emergent: the order parameter itself". The space of real structures compatible with a given H is then the [Lagrangian Grassmannian](../phase-space/modular-field/lagrangian-grassmannian.md), "{J} ≅ U(d)/O(d) = Λ(d) … π₁ = ℤ, Maslov circle intact, τ restored" (same note). #11 records the result as the [nontriviality theorem](postulates/nontriviality-theorem.md): the theory has content beyond general relativity plus self-interacting dark matter if and only if η is emergent [D] ([#11 §4](../papers/broken-born-checkpoint-v2.md#4-postulates)–[§5](../papers/broken-born-checkpoint-v2.md#5-the-kinematic-core-and-the-compatibility-theorem)). That η should be dynamical "was argued independently in metastring theory [26S]; the reading of η as the order parameter of broken reciprocity is this program's" (#11 P2′).

## Why some breaking is said to be unavoidable

[#11 §3](../papers/broken-born-checkpoint-v2.md#3-the-question) argues that the symmetry cannot stay unbroken in a world like ours: "[x,p] = iℏ forbids joint locality, so any world with local physics must select a Lagrangian polarization. The magnet must point." A Lagrangian polarization is a choice of half of the phase-space directions as the variables wavefunctions depend on; locality means interactions confined in those variables, and the uncertainty principle rules out confinement in both halves at once. The argument is qualitative and untagged in [#11 §3](../papers/broken-born-checkpoint-v2.md#3-the-question). It requires some polarization, not a particular one; [P5](postulates/p5-spontaneous-selection.md) adds that ours is tilted toward position and that the mirror vacuum is equally lawful. The argument and its later qualifications are on [mandatory breaking](../symmetry-breaking/mandatory-breaking.md).

## What is the program's own

[#11 §3](../papers/broken-born-checkpoint-v2.md#3-the-question) credits the central idea to Freidel, Leigh and Minic: "the idea that a preferred polarization breaks Born duality is Freidel, Leigh and Minic's", quoting "if all probes agree on what we mean by space-time, then we have broken Born duality — there is a preferred choice of polarization, the space-time one" [26S, p. 3]. They "treat the breaking as kinematical and call the choice 'a dynamical question'. This program's addition is to read it as spontaneous breaking, with η as the order parameter" ([broken Born duality](../phase-space/reciprocity/broken-born-duality.md)). In the metastring paper [26S] ([arXiv:1502.08005](https://arxiv.org/abs/1502.08005)) and in [Freidel, Leigh and Minic 2014](https://arxiv.org/abs/1405.3949) (Int. J. Mod. Phys. D), "kinematical" is the word for general relativity's split of phase space, which they propose to make dynamical, and their papers, some with coauthors, also contain η = HJ, name U(d)/O(d) as the space of choices of η and place a symmetry breaking tied to the choice of polarization in the vacuum, for a dual Lorentz symmetry that is not ρ, none of them with a potential, an order parameter or a [Goldstone angle](../symmetry-breaking/goldstone-angle.md) ([further overlaps with the program](../dark-matter/conjugate-matter/dual-standard-model.md#further-overlaps-with-the-program); [`notes/dual-sector.md` §8](../../notes/dual-sector.md#8-the-vacuum-and-the-choice-of-polarization); flag 70, pending).

As the first step of its toy-model work ([criterion S0](../symmetry-breaking/toy-models/success-criteria.md)), the program searched the literature for that addition. The search, with every citation retrieved rather than recalled, covered INSPIRE full text and arXiv abstracts. It found "no existing action has Born reciprocity exactly symmetric and spontaneously broken with η or K as order parameter", and called the result "evidence of absence, not proof" because INSPIRE's coverage is incomplete (toy worklog, 'Chunk 1 results').

## The v2.2 refinement: a Goldstone angle and a twisted element

The [toy models](../symmetry-breaking/toy-models/_index.md) gave the hard core its first explicit realization, and with it two qualifications, which #11 now carries in P2′: "with only ω rigid, ρ sits inside a continuous U(1), and the polarization is a Goldstone angle rather than a discrete choice [D][V]. Two things follow. A definite polarization needs a ρ-preserving potential on that angle — a rigid, unordered pair of axes, so more structure than ω alone, though less than a rigid η. And the breaking of ρ is physical only once matter couples to the sign of K (P4): without such a coupling, a twisted element ρ∘(K → −K) leaves the vacuum invariant" ([#11 §4](../papers/broken-born-checkpoint-v2.md#4-postulates)). The steps, as the toy-model note gives them for its [model I](../symmetry-breaking/toy-models/coset-model/_index.md), a [coset sigma model](../symmetry-breaking/toy-models/coset-model/sigma-models.md) of the fields H and K on a 1+1-dimensional base:

1. **The symmetric action.** The action is invariant under the whole group Sp(2,ℝ), acting as H → SᵀHS and K → S⁻¹KS, so in particular under ρ, and separately under K → −K ([toy-model note §2](../papers/reciprocity-toy-models.md#2-model-i-a-coset-sigma-model-of-h-k); checked symbolically in [`verify/toy_coset.py`](../../verify/toy_coset.py)).
2. **The vacua form a circle.** At H = 1 the vacua are K(φ) = [[cos φ, sin φ], [sin φ, −cos φ]], and ρ maps K(φ) to K(φ + π) = −K(φ). No vacuum is ρ-invariant, and the operator O = K₁₁ changes sign under ρ, so it serves as the order parameter. The rotations of phase space that leave H = 1 unchanged move K around the circle, and ρ, the quarter turn, is one of them: in the worklog's words, ρ "is one element of a continuous U(1)", "the U(1) stabilizer of H that rotates K". The angle φ costs no energy to change, so it is a [Goldstone direction](../symmetry-breaking/goldstone-and-higgs.md), and it parametrizes Λ(1), "the checkpoint's Maslov circle (the τ field of §10)" (toy worklog, 'Chunk 1 results' and 'Chunk 2 results'; [the polarization as a Goldstone angle](../symmetry-breaking/goldstone-angle.md)). The complex [Grosse–Wulkenhaar model](../symmetry-breaking/toy-models/grosse-wulkenhaar/_index.md) shows the same structure, and the worklog calls the finding "model-level evidence from two toys, not a theorem".
3. **A potential is needed.** In 1+1 dimensions a compact continuous symmetry cannot break spontaneously ([the Mermin–Wagner–Coleman theorem](../symmetry-breaking/mermin-wagner-coleman.md)), so the note adds a potential that keeps ρ and K → −K and reduces the circle to two points. Its first form was unbounded below once H was allowed to move ([Under review: the naive ρ-preserving potential](../symmetry-breaking/toy-models/coset-model/naive-potential.md)). The bounded form V_b equals −(μ/2)(1 + cos 2φ) at H = 1, with minima at K = ±K_ref, which ρ exchanges; with H dynamical, (1, K_ref) is a stable minimum with Hessian eigenvalues "0, 0.764, 2, 5.236" ([toy-model note §4](../papers/reciprocity-toy-models.md#4-quantum-stability); [the bounded potential](../symmetry-breaking/toy-models/coset-model/bounded-potential.md)). With H held at 1, a lattice Monte Carlo at temperature T = 0.6 finds an ordered ℤ₂ phase: "⟨|m|⟩ = 0.954 ± 0.0001 at every size; Binder cumulant 0.667" at L = 16, 32 and 64 ([toy-model note §4](../papers/reciprocity-toy-models.md#4-quantum-stability), [`verify/toy_s4.py`](../../verify/toy_s4.py); on "at every size", see flag 13 in [`review/wiki-build-flags.md`](../../review/wiki-build-flags.md); [the Monte Carlo](../symmetry-breaking/toy-models/coset-model/monte-carlo.md)). That is a statement about the frozen-H reduction, not about model I with H dynamical ([the frozen-H reduction](../symmetry-breaking/toy-models/coset-model/frozen-h-reduction.md)). Where the potential would come from is [open](../symmetry-breaking/rho-preserving-potential.md).
4. **The twisted element.** Because the action is also invariant under K → −K, the combination of ρ with that flip "maps (1, K₀) to itself. So within the full symmetry group, the vacuum keeps an element that acts on H exactly as ρ does. Breaking ρ is physical only once a coupling odd in K is present" ([toy-model note §2](../papers/reciprocity-toy-models.md#2-model-i-a-coset-sigma-model-of-h-k)). The [round-4](../method/review/round-4.md) referee raised the point, and the adjudication upheld it as sharpening the matter-coupling result "rather than contradicting it" ([`review/round4-adjudication.md`](../../review/round4-adjudication.md), F3; [the twisted element](../symmetry-breaking/twisted-element.md)).
5. **Matter supplies the sign.** A matter interaction built from H and K, I[W] = ∫_{L+} du (∫_{L−} dv W)² of a state's [Wigner function](../phase-space/reciprocity/wigner-function.md) W, is "odd in K" ([toy-model note §5](../papers/reciprocity-toy-models.md#5-matter-and-locality); see flag 2 in [`review/wiki-build-flags.md`](../../review/wiki-build-flags.md)). At H = 1 it equals ∫|ψ(x)|⁴ dx, local in position, in the vacuum +K_ref, and ∫|ψ̃(p)|⁴ dp, local in momentum, in −K_ref; for the note's test state the two vacua give 0.4070 and 0.3600 ([toy-model note §5](../papers/reciprocity-toy-models.md#5-matter-and-locality), [`verify/toy_s5.py`](../../verify/toy_s5.py)). "Nothing here forces that coupling" (§5). The worklog names the coupling's role: "The lock is P4", so that in the toy, "our matter is the x-polarized species" ([locality from an (H, K)-built coupling](../symmetry-breaking/matter-coupling.md)).

[#11 §10](../papers/broken-born-checkpoint-v2.md#10-cosmology) limits what the toy models show for the rest of the program: "None of this tests the cosmology; it only shows the structure is consistent." The note's own list of what it did not show includes "anything beyond d = 1" ([toy-model note §6](../papers/reciprocity-toy-models.md#6-summary-and-limitations)).

## History of the statement

- **Lab notebook, v0.1 (#1).** Five postulates with both ω and η rigid, and a discrete breaking pattern ℤ₄ → ℤ₂ with J as the order parameter [D] ([#1 §2](../../notes/broken-born-theory.md#2-kinematic-core)). The rigid ω was also to supply the dark-energy potential by tilting the [Maslov circle](../phase-space/modular-field/maslov-phase.md), an item the notebook tagged [P/O] ([#1 §3](../../notes/broken-born-theory.md#3-action)). The discrete picture is on [the order parameter](../symmetry-breaking/order-parameter.md).
- **The P2 → P2′ repair** (field-equation note [#5](../../notes/geometric-core.md); notebook addendum v0.3), forced by the nontriviality theorem as described above.
- **v1 paper ([#9](../../notes/broken-born-program-v1.md)).** "hard core — spontaneously broken reciprocity with ω-only rigidity — intact and sharpened by the P2 → P2′ correction" ([#9 §11](../../notes/broken-born-program-v1.md#11-assessment)): one sharpening.
- **The checkpoint (#11).** "intact, twice sharpened by forced corrections (P2′; the w-dictionary)" ([#11 §15](../papers/broken-born-checkpoint-v2.md#15-assessment)). The second correction replaced an early heuristic translation rule for the conjugate cosmology, w_eff = −2 − w̃, by the derived [duality dictionary](../cosmology/scale-factor-duality/duality-dictionary.md) w_eff = −w̃ ([#11 §10](../papers/broken-born-checkpoint-v2.md#10-cosmology)), which as a map of fluid variables is the scale-factor duality of string cosmology with sources (flag 66, pending); the lab notebook had recorded that "The correction is what makes the dark-energy sector work" ([#1 §0](../../notes/broken-born-theory.md#0-epistemic-scope)). In v2.1 the compatibility theorem, presented in v2.0 as derived here, was re-attributed to Freidel, Leigh and Minic ([#11 §5](../papers/broken-born-checkpoint-v2.md#5-the-kinematic-core-and-the-compatibility-theorem)). In v2.2 they were also credited with the idea of broken Born duality, and P2′ gained the Goldstone-angle refinement above.
- **Round 3.** The [round-3](../method/review/round-3/_index.md) referees' objection that the framework did no work in the withdrawn soliton manuscript ([#14](../../notes/knot-dark-matter-standalone.md); [Obituary: #14's superheavy-soliton model](../dark-matter/candidates/soliton-candidate/obituary.md)) set the toy models as the next task; by the worklog's assessment the toy models make the hard core's structures "cohere (η as order parameter; τ as the polarization angle), but matter's x-locality still enters through the P4-type coupling" ([the 'framework does no work' critique](framework-does-no-work.md)).

The founding supposition behind all of this, P.R.'s "Symmetrize QM around conjugate variables" (QM: quantum mechanics), is recorded in [#11 Appendix A](../papers/broken-born-checkpoint-v2.md#appendix-a-audit-of-founding-suppositions-pr-with-fates) as "alive; the hard core (Born reciprocity, spontaneously broken, ω-only rigid)" ([founding suppositions](founding-suppositions.md)).

## What remains open

- **The potential.** A derivation of the ρ-preserving potential, which "introduces a rigid, unordered pair of axes" ([toy-model note §6](../papers/reciprocity-toy-models.md#6-summary-and-limitations); [Open: the origin of the ρ-preserving potential](../symmetry-breaking/rho-preserving-potential.md)).
- **The coupled model.** "whether ρ's SO(2) breaks in the coupled model without a potential" ([toy-model note §6](../papers/reciprocity-toy-models.md#6-summary-and-limitations); [Open: does ρ's SO(2) break in the coupled model?](../symmetry-breaking/toy-models/coset-model/so2-question.md)), and [a Monte Carlo with H dynamical](../symmetry-breaking/toy-models/coset-model/dynamical-h-monte-carlo.md) ([#11 §14 item 11](../papers/broken-born-checkpoint-v2.md#14-open-problems)).
- **Forced locality.** A mechanism that forces matter's coupling to the sign of K, rather than postulating it through P4 ([Open: forced locality and the P4 lock](../symmetry-breaking/strong-locality.md)). The worklog's literature search found the same gap in the field: "a mechanism that picks L over L̃" is open there too (toy worklog, 'Chunk 4').
- **Field-theory selection.** In the real Grosse–Wulkenhaar model the position-sharp vacuum is preferred at one loop. The toy-model note calls this "explicit, not spontaneous selection, because the real model is not duality-symmetric" ([§3](../papers/reciprocity-toy-models.md#3-model-ii-the-self-dual-grossewulkenhaar-model)), and it is recorded as a lead, not a result ([Open: the real model's one-loop preference](../symmetry-breaking/toy-models/grosse-wulkenhaar/real-model-lead.md)).
- **Lorentzian signature.** The geometric construction is a Euclidean skeleton; its Lorentzian dressing is [#11 §14 item 3](../papers/broken-born-checkpoint-v2.md#14-open-problems) ([Open: Lorentzian dressing](../phase-space/born-geometry/lorentzian-dressing.md)).

## Popsci-only: "a single assumption"

The popular article [#12](../../popsci/universes-other-half.md) says that "The framework rests on a single assumption — the position–momentum symmetry is exact and spontaneously broken". #11 formalizes the hard core as five postulates, and v2.2 added that a definite polarization needs a ρ-preserving potential and that the breaking has physical content only through a coupling odd in K. #12 has not been amended in substance since it was imported into the repository, before #11's later amendments. It presents the framework "as if it were confirmed"; it is never a source for a claim's status ([the popular articles](../history/documents/popular-articles.md)).

## Sources

- [`wiki/papers/broken-born-checkpoint-v2.md` §3](../papers/broken-born-checkpoint-v2.md#3-the-question) — the program, the mandatory-breaking argument and the Freidel–Leigh–Minic credit; [§4](../papers/broken-born-checkpoint-v2.md#4-postulates) — P1–P5 and the v2.2 refinement of P2′; [§5](../papers/broken-born-checkpoint-v2.md#5-the-kinematic-core-and-the-compatibility-theorem) — the structures, the compatibility theorem and the nontriviality theorem; [§10](../papers/broken-born-checkpoint-v2.md#10-cosmology) — the scope of the toy-model support; [§15](../papers/broken-born-checkpoint-v2.md#15-assessment) — "intact, twice sharpened"; [App. A item 1](../papers/broken-born-checkpoint-v2.md#appendix-a-audit-of-founding-suppositions-pr-with-fates) — the founding supposition
- [`HANDOFF.md` §1](../../HANDOFF.md#1-what-this-project-is) — the one-sentence statement of the hard core
- [`wiki/papers/reciprocity-toy-models.md` §1](../papers/reciprocity-toy-models.md#1-setting-and-prior-work), [§2](../papers/reciprocity-toy-models.md#2-model-i-a-coset-sigma-model-of-h-k), [§3](../papers/reciprocity-toy-models.md#3-model-ii-the-self-dual-grossewulkenhaar-model), [§4](../papers/reciprocity-toy-models.md#4-quantum-stability), [§5](../papers/reciprocity-toy-models.md#5-matter-and-locality), [§6](../papers/reciprocity-toy-models.md#6-summary-and-limitations) — η = ωK, model I, its vacua and the twisted element, the real model's explicit one-loop selection, the bounded potential and the Monte Carlo, the K-odd coupling, and what is not shown
- [`notes/geometric-core.md` §B](../../notes/geometric-core.md#b-the-inconsistency-and-the-forced-repair-d--structural) — the strict-P2 branch, the repair and the nontriviality theorem as first derived
- [`notes/broken-born-theory.md` §0](../../notes/broken-born-theory.md#0-epistemic-scope)–[§3](../../notes/broken-born-theory.md#3-action) — the original postulates, ρ's action on (ω, η, H), the discrete breaking pattern, the [P/O] origin of τ's potential, and the dictionary correction (superseded as reference)
- [`notes/broken-born-program-v1.md` §0](../../notes/broken-born-program-v1.md#0-two-abstracts)–[§1](../../notes/broken-born-program-v1.md#1-the-question), [§11](../../notes/broken-born-program-v1.md#11-assessment) — the v1 statement, "sharpened by the P2 → P2′ correction" (superseded by #11)
- [`notes/toy-lagrangian.md`](../../notes/toy-lagrangian.md) 'Chunk 1 results', 'Chunk 2 results', 'Chunk 4' — the prior-art search, the Goldstone spectrum, the U(1) containing ρ, and the P4 lock
- [`review/round4-adjudication.md`](../../review/round4-adjudication.md) 'Rulings' F3 — the twisted element upheld
- [`verify/toy_coset.py`](../../verify/toy_coset.py), [`verify/toy_s4.py`](../../verify/toy_s4.py), [`verify/toy_s5.py`](../../verify/toy_s5.py) — the machine checks of the refinement
- [`popsci/universes-other-half.md`](../../popsci/universes-other-half.md) 'What one assumption purchases' — the "single assumption" framing (popular article; not a status source)
- [`notes/literature-check.md` §6](../../notes/literature-check.md#6-conjugate-collapse-drives-our-acceleration-c5-partly-anticipated); [`review/wiki-build-flags.md`](../../review/wiki-build-flags.md) item 66 — the w-dictionary as scale-factor duality with sources, as a map of fluid variables; pending
- [`notes/dual-sector.md` §8](../../notes/dual-sector.md#8-the-vacuum-and-the-choice-of-polarization); [`review/wiki-build-flags.md`](../../review/wiki-build-flags.md) item 70 — what the papers of Freidel, Leigh, Minic and their coauthors hold of the choice of polarization, and what was not found there; pending
