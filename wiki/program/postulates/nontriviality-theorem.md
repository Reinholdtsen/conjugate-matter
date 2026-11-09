---
title: "The nontriviality theorem"
weight: 30
status: alive
description: "The program has content beyond general relativity plus self-interacting dark matter if and only if η is emergent: under strict P2 the action S_H depends on g alone and the dark-energy sector disappears."
provenance: [D]
sources:
  - "wiki/papers/broken-born-checkpoint-v2.md §4"
  - "wiki/papers/broken-born-checkpoint-v2.md §5"
  - "wiki/papers/broken-born-checkpoint-v2.md §6"
  - "wiki/papers/broken-born-checkpoint-v2.md §15"
  - "notes/geometric-core.md §A"
  - "notes/geometric-core.md §B"
  - "notes/geometric-core.md §C"
  - "notes/geometric-core.md §E"
  - "notes/geometric-core.md §F"
  - "notes/broken-born-theory.md §2"
  - "notes/broken-born-theory.md 'Addendum (v0.3)'"
  - "notes/broken-born-program-v1.md §2–§3"
  - "HANDOFF.md §2"
  - "review/round3-adjudication.md 'Rulings'"
  - "verify/battery.py T1"
  - "review/wiki-build-flags.md item 1"
  - "review/wiki-build-checks/verifier_null_lagrangians.py"
  - "review/wiki-build-flags.md item 55"
  - "notes/gate-mechanism.md §2"
---

*The nontriviality theorem states that the Comatter program predicts anything beyond [general relativity](../../gravity/spin-2-fields/general-relativity.md) plus one model of self-interacting dark matter only if the neutral metric η, the structure that marks which directions count as position, is a property of the vacuum rather than a fixed part of the background. It is the argument that forced the program to change its second axiom. With η fixed, the position–momentum splittings compatible with both fixed structures include no [Maslov circle](../../phase-space/modular-field/maslov-phase.md), the loop of splittings on which the program's dark-energy field lives, and the [geometric action](../../gravity/tuning-test/geometric-action.md) depends only on the ordinary spacetime metric, which leaves no second, momentum-space graviton. With η a property of the vacuum, all of these return. The result is a structural argument of the program, tagged derived [D]; the compatibility theorem it starts from is a known result of Born geometry and is machine-checked.*

**Status:** Alive — [D] in [#11](../../history/documents/checkpoint.md) [§4](../../papers/broken-born-checkpoint-v2.md#4-postulates); the note that derived it tags its section "[D — structural]" — not machine-checked as a whole; its input, [the compatibility theorem](../../phase-space/born-geometry/compatibility-theorem.md), is [T][V] (battery test T1, [the verification battery](../../method/verification/battery.md)).

## Statement

The checkpoint states the result twice. In the postulate list, under [P2′](p2-prime.md): "the correction from the original P2 is *forced*: a nontriviality theorem (§5) shows the theory has content beyond GR + SIDM iff η is emergent. [D]" ([#11 §4](../../papers/broken-born-checkpoint-v2.md#4-postulates)). In the kinematic core: "Under strict P2 the compatible polarizations are discrete, so no Grassmannian, no Maslov circle, no dark-energy field, and S_H is a functional of g alone: **nontriviality theorem** — the program has content iff η is emergent. Hence P2 → P2′." ([#11 §5](../../papers/broken-born-checkpoint-v2.md#5-the-kinematic-core-and-the-compatibility-theorem); on "discrete", see flag 1 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md)). The [field-equation note](../../history/documents/field-equation-notes.md), where it was derived, puts it as:

> **Program-nontriviality theorem:** BBT has content beyond GR + SIDM **iff** η is emergent. P2 → P2′ is not optional. ([#5 §B](../../../notes/geometric-core.md#b-the-inconsistency-and-the-forced-repair-d--structural))

GR is general relativity, SIDM [self-interacting dark matter](../../dark-matter/halo-astrophysics/self-interacting-dark-matter.md), and BBT Broken-Born theory, the program's earlier name.

Two terms need unpacking.

- **"Content beyond GR + SIDM."** Under strict P2, [#5 §B](../../../notes/geometric-core.md#b-the-inconsistency-and-the-forced-repair-d--structural) finds no dark-energy field τ, no momentum graviton X, and no geometric origin for the velocity gate of [conjugate matter](../../dark-matter/conjugate-matter/_index.md), and without them "the program has no content of its own". What remains is general relativity, dark energy as a constant with w ≡ −1 (w is dark energy's [equation of state](../../cosmology/dark-energy/quintessence.md#dark-energy-and-the-equation-of-state), its pressure divided by its energy density), and one self-interacting dark-matter model whose gate is "unexplained" (Branch R, [#5 §B](../../../notes/geometric-core.md#b-the-inconsistency-and-the-forced-repair-d--structural)).
- **"η is emergent."** The neutral metric η is not a background structure but a property of the vacuum state: the [order parameter](../../symmetry-breaking/order-parameter.md) η = HJ of P2′, with the real structure J "chosen spontaneously" ([#11 §4](../../papers/broken-born-checkpoint-v2.md#4-postulates)). The alternative, η fixed in advance alongside ω, is the [original P2](original-p2.md), called "strict P2" in the record.

## The ingredients

### Three structures and their algebra [T]

Born geometry puts three structures on phase space ([the structures ω, η, H](../../phase-space/born-geometry/born-structures.md)): the [symplectic form](../../phase-space/reciprocity/symplectic-form.md) ω, the neutral metric η, and the positive generalized metric H. "With ω, η standard, I = ω⁻¹H, J = η⁻¹H, K = η⁻¹ω satisfy I² = −1, J² = K² = +1, IJ = K — a split-quaternion algebra (Born geometry [3†]; a unique compatible connection exists [7†])" ([#11 §5](../../papers/broken-born-checkpoint-v2.md#5-the-kinematic-core-and-the-compatibility-theorem)). I is a complex structure, a quarter-turn of phase space; J and K are real structures, maps that square to the identity.

### The compatibility theorem [T][V]

Holding both ω and η in standard form leaves almost no freedom in H:

```text
Positive H satisfying both (η⁻¹H)² = 1 and (ω⁻¹H)² = −1 are exactly
H = diag(g, g⁻¹),  g ∈ Sym⁺(d).                                     (#11 §5)

Proof (#11 §5; #5 §A), writing H = [[A, C], [Cᵀ, B]]:
  (2,1) blocks of the two conditions:  ACᵀ + CA = 0  and  CA − ACᵀ = 0   ⇒  ACᵀ = 0
  positivity                                                           ⇒  C = 0
  diagonal blocks                                                      ⇒  B = A⁻¹
```

The battery's test T1 checks the theorem by machine: a matrix diag(g, g⁻¹) satisfies both conditions, a randomly drawn H violates at least one, and the two (2,1) block identities used in the proof hold ([`verify/battery.py`](../../../verify/battery.py); [the verification battery](../../method/verification/battery.md)). The [round-3](../../method/review/round-3/_index.md) audit re-derived the theorem independently, with sympy and a Gröbner basis at d = 2, and "reports that the positivity step is not needed for C = 0" ([#11 §5](../../papers/broken-born-checkpoint-v2.md#5-the-kinematic-core-and-the-compatibility-theorem)). The statement is credited to [Freidel, Leigh and Minic](../../phase-space/reciprocity/broken-born-duality.md) [26S, §2.1]; the block proof and the machine check are the program's ([#11 §5](../../papers/broken-born-checkpoint-v2.md#5-the-kinematic-core-and-the-compatibility-theorem); [the compatibility theorem](../../phase-space/born-geometry/compatibility-theorem.md)).

Its corollaries ([#5 §A](../../../notes/geometric-core.md#a-the-compatibility-theorem-d--rigorous); [the corollaries](../../phase-space/born-geometry/compatibility-corollaries.md)) are det H = 1 identically; no [Kalb–Ramond](../../phase-space/born-geometry/kalb-ramond-field.md#frozen-out-when-both-pairings-are-rigid) analog, since "The off-diagonal block — DFT's B-field — is frozen out by the extra symplectic compatibility" (DFT: [double field theory](../../phase-space/born-geometry/double-field-theory.md)); and "The momentum metric is slaved: g̃ = g⁻¹ pointwise. No independent momentum-space geometry survives." The nontriviality argument starts from the third.

## The argument

### With η fixed: what strict P2 removes [D — structural]

"Corollary 3 collides with the theory as documented" ([#5 §B](../../../notes/geometric-core.md#b-the-inconsistency-and-the-forced-repair-d--structural)). The note draws two consequences.

1. **No Maslov circle.** A polarization is a choice of Lagrangian subspace, the directions that count as position ([Lagrangian polarizations](../../phase-space/reciprocity/lagrangian-polarizations.md)). Under strict P2 it must respect both fixed structures: "The space of polarizations compatible with both structures (ω-Lagrangian *and* η-null) is **discrete** — the 2^d coordinate-type splittings, GL(d)-rigid. No Lagrangian Grassmannian, no Maslov circle, **no τ field**." The program's dark-energy field τ is the angle around the Maslov circle, the [non-contractible loop](../../symmetry-breaking/topological-defects.md#the-polarizations-vacuum-manifold-and-its-maslov-loop) of [the Lagrangian Grassmannian](../../phase-space/modular-field/lagrangian-grassmannian.md) Λ(d), whose fundamental group is π₁ = ℤ ([#1 §2](../../../notes/broken-born-theory.md#2-kinematic-core) [T]; [τ as the Maslov phase](../../phase-space/modular-field/maslov-phase.md)). In #5's reading the compatible polarizations form a discrete set, which has no such loop, so τ cannot be defined: "The dark-energy sector as constructed contradicts P2." Flag 1 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md) queries the word "discrete". For d ≥ 2, any subspace V of the position directions, taken together with its orthogonal complement V^⊥ placed in the momentum directions, gives a polarization V ⊕ V^⊥ that is Lagrangian for ω and null for η, so the compatible polarizations form continuous Grassmannian families Gr(k, d). The Maslov phase det² is constant (±1) on each family, so no family winds around the Maslov circle, the x-polarization (V the whole of position space) is isolated, and the conclusion stands. The flag's executed check, at d = 2 and 3, is [`review/wiki-build-checks/verifier_null_lagrangians.py`](../../../review/wiki-build-checks/verifier_null_lagrangians.py). The flag, pending, suggests the wording "no continuous family through the x-polarization; det² is constant, so no Maslov circle".
2. **A pure metric theory.** "With H = diag(g, g⁻¹), S_H is a functional of g alone: a pure metric theory. No momentum graviton, hence no geometric origin for the χ gate either." S_H is the geometric action of H. If the spacetime metric g is the only free field in H, there is no second tensor to serve as the [momentum graviton](../../gravity/momentum-graviton/_index.md) X. The mechanism that the same note finds for the [velocity gate](../../dark-matter/conjugate-matter/velocity-gate.md) of conjugate matter χ is exchange of X ([#5 §E](../../../notes/geometric-core.md#e-the-gate-problem--the-mechanism-found-d--structural); [the gate mechanism](../../dark-matter/conjugate-matter/gate-mechanism.md)), so it has nothing to exchange. That mechanism is itself disputed (not derived, according to flag 55 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md), pending; [the gate mechanism](../../dark-matter/conjugate-matter/gate-mechanism.md#exchanging-x-cannot-produce-the-gate)).

The note calls what is left Branch R: "BBT reduces to GR + one bespoke SIDM model, with w ≡ −1 and the gate unexplained. On Branch R the program has no content of its own" ([#5 §B](../../../notes/geometric-core.md#b-the-inconsistency-and-the-forced-repair-d--structural)). The v0.3 addendum of the [lab notebook](../../history/documents/lab-notebook.md) condenses it: "A theory with strict P2 is GR plus one bespoke SIDM model."

### With η emergent: what the repair restores

The repair holds ω alone fixed: "the fundamental pair is (ω, H); the derived complex structure is I = ω⁻¹H; the vacuum spontaneously selects a real structure J (an involution anticommuting with I), and η ≡ HJ" ([#5 §B](../../../notes/geometric-core.md#b-the-inconsistency-and-the-forced-repair-d--structural)). The possible choices form the full Grassmannian:

```text
{J} ≅ U(d)/O(d) = Λ(d)                                              (#5 §B)
```

"the Lagrangian Grassmannian — π₁ = ℤ, Maslov circle intact, τ restored". The metric opens up in the same step. The positive H compatible with ω alone form [the Siegel domain](../../phase-space/modular-field/siegel-domain.md) Sp(2d, ℝ)/U(d), coordinatized by Z = X + iY with Y > 0 ([#5 §C](../../../notes/geometric-core.md#c-the-modular-field-d--structural-math-facts-standard)). Im Z = Y = g is the spacetime metric, and Re Z = X is "a *new symmetric tensor*: the momentum graviton. It is exactly the fluctuation that breaks η-compatibility" ([#5 §C](../../../notes/geometric-core.md#c-the-modular-field-d--structural-math-facts-standard); [the modular field Z = X + iY](../../phase-space/modular-field/modular-field-z.md)). The rigid case survives inside the emergent one as a slice: "At X = 0, H = diag(g, g⁻¹): the η-compatible locus of Theorem A is precisely the vacuum slice" ([#5 §C](../../../notes/geometric-core.md#c-the-modular-field-d--structural-math-facts-standard)).

So each item that strict P2 removes is present under P2′. The polarization ranges over Λ(d), τ lives on its Maslov circle, and X exists as Re Z. With X present, the gate has a mediator again ([#5 §E](../../../notes/geometric-core.md#e-the-gate-problem--the-mechanism-found-d--structural)).

### The two halves of "iff"

The "only if" half is the first subsection: with η fixed, the program reduces to Branch R. The "if" half rests on what the repair restores: with η emergent, the structures that carry the program's own content exist. The field-equation note tags both §B and the modular-field section §C as structural ("[D — structural]"; §C adds "math facts standard"). Neither half is a line-by-line derivation, and neither is machine-checked as a whole. The machine check covers the compatibility theorem underneath.

## Scope and caveats

- **A theorem in a structural section.** The note calls the result a theorem inside a section tagged "[D — structural]", and #11 carries it as [D]. It is an argument from the structure of the constructions, not a formal proof.
- **What "content" covers.** The result concerns the program's own sectors: what it lists as lost under strict P2 are τ, X and the gate's geometric origin ([#5 §B](../../../notes/geometric-core.md#b-the-inconsistency-and-the-forced-repair-d--structural)).
- **Circular pointers in v1.** The program paper v1 ([#9](../../../notes/broken-born-program-v1.md)) states the result in two places that point at each other: its §2 says the correction is "forced by the theorems of §3 and §5", and its §3 ends "Hence the nontriviality theorem of §2". #11 places the theorem in [§5](../../papers/broken-born-checkpoint-v2.md#5-the-kinematic-core-and-the-compatibility-theorem). #9 is superseded by #11.
- **The v2.2 refinement.** The [toy models](../../symmetry-breaking/toy-models/_index.md) later added structure between the two cases the theorem compares. With only ω rigid the polarization is a Goldstone angle, and "A definite polarization needs a ρ-preserving potential on that angle — a rigid, unordered pair of axes, so more structure than ω alone, though less than a rigid η" ([#11 §4](../../papers/broken-born-checkpoint-v2.md#4-postulates)). #11 states the refinement beside the theorem; no source revisits the theorem in its light. See [P2′](p2-prime.md) and [the polarization as a Goldstone angle](../../symmetry-breaking/goldstone-angle.md).

## Consequences for the program

- **P2 → P2′.** The theorem is why the program's second axiom changed. [#5 §B](../../../notes/geometric-core.md#b-the-inconsistency-and-the-forced-repair-d--structural): "P2 → P2′ is not optional." The replaced axiom is kept as [the original P2](original-p2.md).
- **The modular field.** The Siegel-domain geometry of [#11 §6](../../papers/broken-born-checkpoint-v2.md#6-the-modular-field), with its momentum graviton and the dark-energy field on the domain's boundary, exists only under P2′: "With only ω rigid, H ranges over Sp(2d,ℝ)/U(d)" ([#11 §6](../../papers/broken-born-checkpoint-v2.md#6-the-modular-field)).
- **The next computation.** The v0.3 addendum records that, with X restored, "Open problem 1 sharpens to a single decisive computation: the quadratic-order classification of X (healthy / auxiliary / ghost)". That computation found X to be a second graviton that must be massive ([why X must be massive](../../gravity/momentum-graviton/forcing-chain.md)).
- **The hard core.** [#11 §15](../../papers/broken-born-checkpoint-v2.md#15-assessment) lists the program's [hard core](../hard-core.md) as "spontaneously broken reciprocity, ω-only rigidity" and calls it "intact, twice sharpened by forced corrections (P2′; the w-dictionary)". P2′, which the theorem forced, is the first of those two sharpenings ([Lakatos's methodology](../../method/lakatosian-methodology.md)); the second, the w-dictionary, is as a map of fluid variables the scale-factor duality of string cosmology with sources (flag 66 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md), pending).

## History

- **Derived** in the overnight field-equation note, Chunk A (#5), whose header reads "Status: two rigorous results, one axiom correction forced, one mechanism identified, one decisive computation defined but not completed." Its closing tally, headed "Done", includes "discovery and repair of an axiom-level inconsistency (P2 → P2′, with a nontriviality theorem making the repair mandatory)" ([#5 §F](../../../notes/geometric-core.md#f-status-after-tonight)).
- **Recorded** in the lab notebook's v0.3 addendum, which found "with it an axiom-level inconsistency: strict P2 makes the polarization choice discrete, eliminating the Lagrangian Grassmannian, the Maslov circle, and hence the entire τ/dark-energy sector, while also slaving g̃ = g⁻¹ and removing any geometric origin for the χ gate" (on "discrete", see flag 1 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md)).
- **Carried forward** in the program paper v1 ([#9 §2](../../../notes/broken-born-program-v1.md#2-postulates--including-the-one-the-mathematics-rejected)–[§3](../../../notes/broken-born-program-v1.md#3-the-kinematic-core-and-the-compatibility-theorem), tagged [D], with the circular pointers above) and in [the handoff](../../history/documents/handoff.md), which lists among the alive results "P2′ correction: strict rigidity trivializes the theory (nontriviality theorem); η must be emergent" ([`HANDOFF.md` §2](../../../HANDOFF.md#2-scientific-state-one-screen)).
- **Current form** in [#11 §4](../../papers/broken-born-checkpoint-v2.md#4-postulates)–[§5](../../papers/broken-born-checkpoint-v2.md#5-the-kinematic-core-and-the-compatibility-theorem), tagged [D]. In v2.1 the compatibility theorem underneath was re-tagged from derived to [T][V] and credited to Freidel, Leigh and Minic after the round-3 review flagged it ([`review/round3-adjudication.md`](../../../review/round3-adjudication.md)); the nontriviality theorem kept its [D].

## Sources

- [`wiki/papers/broken-born-checkpoint-v2.md` §4](../../papers/broken-born-checkpoint-v2.md#4-postulates)–[§5](../../papers/broken-born-checkpoint-v2.md#5-the-kinematic-core-and-the-compatibility-theorem) — the current statement, tagged [D], and the compatibility theorem with its attribution; [§6](../../papers/broken-born-checkpoint-v2.md#6-the-modular-field) — the modular field that exists only under P2′; [§15](../../papers/broken-born-checkpoint-v2.md#15-assessment) — the hard core
- [`notes/geometric-core.md` §A](../../../notes/geometric-core.md#a-the-compatibility-theorem-d--rigorous) — the compatibility theorem and its corollaries; [§B](../../../notes/geometric-core.md#b-the-inconsistency-and-the-forced-repair-d--structural) — the derivation ("[D — structural]"), Branch R and the repair; [§C](../../../notes/geometric-core.md#c-the-modular-field-d--structural-math-facts-standard) — the Siegel domain and X; [§E](../../../notes/geometric-core.md#e-the-gate-problem--the-mechanism-found-d--structural) — the gate as X exchange; [§F](../../../notes/geometric-core.md#f-status-after-tonight) — the closing tally
- [`notes/broken-born-theory.md` §2](../../../notes/broken-born-theory.md#2-kinematic-core) — the Grassmannian and its Maslov circle; 'Addendum (v0.3)' — the axiom correction as first recorded
- [`notes/broken-born-program-v1.md` §2](../../../notes/broken-born-program-v1.md#2-postulates--including-the-one-the-mathematics-rejected)–[§3](../../../notes/broken-born-program-v1.md#3-the-kinematic-core-and-the-compatibility-theorem) — the v1 statement and its circular pointers (superseded by #11)
- [`HANDOFF.md` §2](../../../HANDOFF.md#2-scientific-state-one-screen) — the result as listed at the handoff
- [`review/round3-adjudication.md`](../../../review/round3-adjudication.md) 'Rulings' — the referee's identification of the compatibility theorem with Freidel–Leigh–Minic's result
- [`verify/battery.py`](../../../verify/battery.py) T1 — the compatibility-theorem checks
- [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md) item 1 and [`review/wiki-build-checks/verifier_null_lagrangians.py`](../../../review/wiki-build-checks/verifier_null_lagrangians.py) — the query on "discrete": continuous families V ⊕ V^⊥ for d ≥ 2, with det² constant on each, so the conclusion stands; pending
- [`notes/gate-mechanism.md` §2](../../../notes/gate-mechanism.md#2-exchanging-the-x-of-7-cannot-produce-the-gate) and [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md) item 55 — exchanging [#11 §7](../../papers/broken-born-checkpoint-v2.md#7-the-massive-momentum-graviton)'s X cannot produce the gate; the proposed tags [P] for the gate and μ, [O] for the mechanism; pending
