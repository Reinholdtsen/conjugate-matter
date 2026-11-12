---
title: "The symplectic charge lattice"
weight: 70
status: alive
description: "The DSZ pairing makes charge space symplectic, mutually local charges form a Lagrangian sublattice, and choosing a duality frame is choosing a polarization — the same matrix [[0,1],[−1,0]] behind ρ, Z → −Z⁻¹ and S-duality."
provenance: [D, T]
sources:
  - "wiki/papers/broken-born-checkpoint-v2.md §11.3"
  - "wiki/papers/broken-born-checkpoint-v2.md §11.4"
  - "wiki/papers/broken-born-checkpoint-v2.md §11.1"
  - "wiki/papers/broken-born-checkpoint-v2.md §12"
  - "wiki/papers/broken-born-checkpoint-v2.md App. A item 5"
  - "wiki/papers/broken-born-checkpoint-v2.md §1"
  - "wiki/papers/broken-born-checkpoint-v2.md §4"
  - "wiki/papers/broken-born-checkpoint-v2.md §6"
  - "wiki/papers/broken-born-checkpoint-v2.md §15"
  - "wiki/papers/broken-born-checkpoint-v2.md App. A item 11"
  - "wiki/papers/broken-born-checkpoint-v2.md ref [17]"
  - "wiki/papers/reciprocity-toy-models.md §1"
  - "HANDOFF.md §2"
  - "HANDOFF.md §3"
  - "HANDOFF.md §6"
  - "notes/knot-dark-matter-standalone.md §2"
  - "notes/knot-dark-matter-standalone.md §6"
  - "review/round3-preregistration.md 'Predictions'"
  - "review/round3/referee/audit-notes.md Step 1"
  - "review/round3/referee/audit-notes.md Step 4(d)"
  - "review/round3/referee/audit-notes.md Step 5"
  - "review/round3-adjudication.md 'Rulings' 12"
  - "verify/toy_coset.py 'Anchors', 'S2: vacua'"
  - "review/wiki-build-flags.md flag 60"
  - "review/wiki-build-flags.md flag 62"
  - "review/wiki-build-flags.md flag 67"
  - "notes/literature-check.md §5"
  - "popsci/universes-other-half.md 'Dark matter as the other polarization'"
---

*The symplectic charge lattice is the program's observation that the set of allowed electric and magnetic charges has the same geometry as phase space. The Dirac–Schwinger–Zwanziger (DSZ) pairing of two charges is an antisymmetric whole-number form, like the pairing of position with momentum; charges that can all be described together by one Lagrangian form a "Lagrangian" half of the lattice; and deciding which particles count as electric is therefore a choice of polarization, as the program's vacuum chooses which coordinates count as position. One quarter-turn matrix generates [Born reciprocity](../phase-space/reciprocity/born-reciprocity.md), the program's [modular inversion](../phase-space/modular-field/modular-inversion.md) and [S-duality](s-duality.md). [The checkpoint](../history/documents/checkpoint.md) counts this as a structural unification [D — structural; math T]: the mathematics is established, the identification of the two choices is the program's, and no calculation depends on it. Whether the two polarizations are one physical structure is [open problem 8](unified-modular-structure.md).*

**Status:** Alive — [D — structural; math T] — [#11 §11.3](../papers/broken-born-checkpoint-v2.md#113-the-identification-d--structural-math-t). No script checks the charge-lattice statements. The phase-space side of the shared matrix is machine-checked in d = 1: [`verify/toy_coset.py`](../../verify/toy_coset.py) confirms that "rho is symplectic and is the quarter turn: rho^2 = -1" (section 'Anchors') and that "rho acts on Z as Z -> -1/Z with fixed point Z = i" (section 'S2: vacua') ([the toy-model scripts](../method/verification/toy-model-scripts.md)). The DSZ citation [17†] is from model memory and awaits [the † literature battery](../method/literature-battery.md).

## The charge lattice [T]

In a theory with one unbroken U(1) gauge field, such as electromagnetism, each particle carries an electric charge e and a magnetic charge g, written as a pair q = (e, g). A particle with both is a dyon. Quantum mechanics allows only a discrete set of charge pairs, and sums of allowed charges are allowed, so the allowed charges form a lattice in the (e, g) plane [T]. With r unbroken U(1) factors the lattice has 2r dimensions, one electric and one magnetic direction per factor.

## The DSZ pairing [T]

Dirac showed that a magnetic charge g and an electric charge e can coexist only if e·g is a whole multiple of a fixed constant ([Dirac quantization and the DSZ pairing](monopoles/dirac-quantization.md)). One way to see the reason is angular momentum: the combined field of an electric charge and a monopole carries angular momentum proportional to the product of their charges, and angular momentum is quantized [T]. Schwinger and Zwanziger extended the argument to two dyons, for which the field angular momentum depends on e₁g₂ − e₂g₁, and the condition becomes a condition on that combination [T].

[#11](../history/documents/checkpoint.md) [§11.3](../papers/broken-born-checkpoint-v2.md#113-the-identification-d--structural-math-t):

> The Dirac–Schwinger–Zwanziger pairing ⟨q, q′⟩ = e₁g₂ − e₂g₁ ∈ 2πℤ is an antisymmetric integer form: **the charge lattice is a symplectic space** [17†].

The pairing is antisymmetric: exchanging the two charges reverses its sign, ⟨q′, q⟩ = −⟨q, q′⟩, so a charge paired with itself gives zero. In matrix form [T]:

```text
⟨q, q′⟩ = (e₁, g₁) [[0, 1], [−1, 0]] (e₂, g₂)ᵀ = e₁g₂ − e₂g₁
```

The normalization differs between sources. [The round-3 referee](../method/review/round-3/_index.md), checking [#14](../dark-matter/candidates/soliton-candidate/_index.md)'s citation of Dirac and Zwanziger, found that "Zwanziger's abstract states e_m g_n - g_m e_n in 4 pi Z; manuscript writes 2 pi Z (Dirac normalization). The 't Hooft-Polyakov monopole with doublets realises 2 pi, so the physics is fine; but [7] as cited states 4 pi. "Charge space is symplectic" is interpretation." The referee also noted that Schwinger was named but not cited ([`review/round3/referee/audit-notes.md`](../../review/round3/referee/audit-notes.md), Step 1). Ruling 12 accepted these as minor citation issues ([round-3 rulings](../method/review/round-3/rulings.md)); #11's reference [17]† includes Schwinger 1966.

## The same geometry as phase space

A symplectic form is an antisymmetric pairing that leaves no direction paired to zero with everything ([the symplectic form](../phase-space/reciprocity/symplectic-form.md)). Phase space carries one, ω, which pairs each position with its momentum. For one degree of freedom the toy-model note writes it as a matrix: "Phase space ℝ² with symplectic form ω = [[0, 1], [−1, 0]]. ρ = [[0, 1], [−1, 0]] is symplectic and squares to −1." ([`wiki/papers/reciprocity-toy-models.md` §1](../papers/reciprocity-toy-models.md#1-setting-and-prior-work)). In the (e, g) basis the DSZ pairing has the same matrix. The comparison, side by side:

| | phase space | charge space |
| --- | --- | --- |
| elements | points (x, p) | charges q = (e, g) |
| pairing | ω, antisymmetric | ⟨q, q′⟩ = e₁g₂ − e₂g₁, antisymmetric |
| values | real numbers | integer multiples of 2π |
| a Lagrangian half | a subspace on which ω vanishes | a sublattice on which ⟨·,·⟩ vanishes |
| choosing one | a polarization: which coordinates are "position" | a duality frame: which charges are "electric" |
| transformations preserving the pairing [T] | Sp(2d,ℝ), continuous | integer symplectic matrices; for one U(1), [SL(2,ℤ)](modular-group.md#charge-lattices-t) |

The last row is standard mathematics [T]: a lattice is preserved only by matrices with integer entries, so the symmetries of charge space form a discrete group, while those of phase space form a continuous one. The checkpoint does not comment on the difference.

## Mutual locality and Lagrangian sublattices

[#11 §11.3](../papers/broken-born-checkpoint-v2.md#113-the-identification-d--structural-math-t) continues: "Mutual locality (which charges can share one Lagrangian) is ⟨q,q′⟩ = 0: a **Lagrangian sublattice**."

Two charges with a vanishing pairing can be coupled to one set of gauge potentials in a single local Lagrangian [T]. All purely electric charges (g = 0) are mutually local, which is why ordinary electrodynamics has a local Lagrangian. An electron and a [magnetic monopole](monopoles/_index.md) are not: their pairing is not zero, and a description containing both needs a Dirac string or a second set of potentials [T]. A largest set of mutually local charges is a Lagrangian sublattice, the integer analogue of a [Lagrangian subspace](../phase-space/reciprocity/lagrangian-polarizations.md), half the dimension of the lattice. For a single U(1), the pairing of two charges vanishes exactly when they are proportional, so a Lagrangian sublattice consists of the lattice points on one line through the origin.

## A duality frame is a polarization

[#11 §11.3](../papers/broken-born-checkpoint-v2.md#113-the-identification-d--structural-math-t) then states the identification, attributing its wording to the literature:

> Choosing a duality frame — which particles are "electric" (fundamental) versus "magnetic" (solitonic) — is choosing a Lagrangian polarization of charge space, in the literature's own words.

In any one Lagrangian description of a gauge theory, the charges carried by the elementary quanta of its fields are the electric ones, and the charges that appear only on solitons, such as ['t Hooft–Polyakov monopoles](monopoles/thooft-polyakov-monopole.md), are the magnetic ones [T]. A duality transformation gives an equivalent description in which a different Lagrangian sublattice plays the electric role; S-duality exchanges the electric and magnetic sublattices ([S-duality and Montonen–Olive](s-duality.md)). Choosing a frame is choosing a Lagrangian sublattice, in the same sense that the program's postulate [P5](../program/postulates/p5-spontaneous-selection.md) has the vacuum choose a Lagrangian subspace of phase space as "position".

The phrase "in the literature's own words" carries no citation. It is listed as an unreferenced phrase on the page of [the † literature battery](../method/literature-battery.md).

## One matrix, three appearances

[#11 §11.3](../papers/broken-born-checkpoint-v2.md#113-the-identification-d--structural-math-t): "S-duality acts on the complexified coupling by τ_c → −1/τ_c, generated by the same [[0,1],[−1,0]] rotation as Born's ρ and our Z → −Z⁻¹: the third appearance of one matrix in this program."

```text
the matrix [[0, 1], [−1, 0]] generates
  Born reciprocity     ρ: (x, p) → (p, −x)          on phase space
  modular inversion    Z → −Z⁻¹                     on the modular field
  S-duality            τ_c → −1/τ_c                 on the complexified coupling
```

- **Born reciprocity** is the symmetry of quantum kinematics that the program takes as exact and [spontaneously broken](../symmetry-breaking/spontaneous-symmetry-breaking.md); the [Fourier transform](../phase-space/reciprocity/fourier-transform.md) implements it ([Born reciprocity](../phase-space/reciprocity/born-reciprocity.md)).
- **The modular inversion** is ρ acting on the [modular field](../phase-space/modular-field/modular-field-z.md) Z = X + iY, the program's packaging of the phase-space metric; its fixed point Z = i is the vacuum ([#11 §6](../papers/broken-born-checkpoint-v2.md#6-the-modular-field); [reciprocity as modular inversion](../phase-space/modular-field/modular-inversion.md)). The d = 1 form is the gated check quoted in the status line.
- **S-duality** acts on τ_c, the complexified gauge coupling, not the dark-energy field τ ([notation](../notation.md)).

The matrix squares to −1 in each setting [T]. On phase space ρ² sends (x, p) to (−x, −p), and on charges S² sends (e, g) to (−e, −g), charge conjugation. Both leave the modular variable unchanged, since −1/(−1/τ_c) = τ_c, and likewise for Z.

## What kind of claim it is

The tag [D — structural; math T] divides the claim. The mathematics is literature: the antisymmetric DSZ pairing, mutual locality, the duality group acting on charges and couplings. The program's contribution is the identification of the electric–magnetic frame choice with the phase-space polarization choice as the same operation, with no dynamics behind it: no Lagrangian in the repository relates the two choices. The bridge between the two dualities is a published remark: "electric-magnetic duality is a special case of Born-Reciprocity", "a transformation which acts as a rotation in phase space" ([Gibbons and Herdeiro 2001](https://arxiv.org/abs/hep-th/0008052) [S]). The phase space they name is the electromagnetic field's, whose conjugate pair is the magnetic field B and the electric displacement D, not the position and momentum of matter, so the remark does not show that ρ, acting on position and momentum, exchanges electric and magnetic charge ([`notes/literature-check.md` §5](../../notes/literature-check.md#5-the-magnetic-mirror-c4-partly-anticipated)). One vacuum event that selects both polarizations was not found ([one enlarged modular structure](unified-modular-structure.md#in-the-literature); flag 67, pending).

The checkpoint counts the identification in several places:

- the technical abstract: "The electric–magnetic charge lattice, with its Dirac–Schwinger–Zwanziger symplectic pairing [17†], furnishes a second arena in which the same polarization choice recurs" ([#11 §1](../papers/broken-born-checkpoint-v2.md#1-two-abstracts));
- the assessment: "one structural unification (polarization of phase space and of charge space as one move)", and among the progressive signs "the §11.3 unification generating new questions" ([#11 §15](../papers/broken-born-checkpoint-v2.md#15-assessment); [the program's self-assessment](../program/assessment.md); flag 67, pending);
- [founding supposition 11](../program/founding-suppositions.md): "the polarization identification as the program-native addition" to the established [magnetic mirror-family](magnetic-mirror-family.md) ([#11 App. A item 11](../papers/broken-born-checkpoint-v2.md#appendix-a-audit-of-founding-suppositions-pr-with-fates));
- [the handoff](../history/documents/handoff.md), under "Alive": "Charge-lattice identification: DSZ pairing is symplectic; duality frame choice = Lagrangian polarization, same [[0,1],[−1,0]] generator as Born rotation and S-duality" ([`HANDOFF.md` §2](../../HANDOFF.md#2-scientific-state-one-screen)).

The section first appeared in the checkpoint's v2.0; the handoff lists "charge-lattice §11" among v2.0's additions ([`HANDOFF.md` §3](../../HANDOFF.md#3-artifact-inventory-creation-order)). §11.1 gives two grounds against the explanation of the monopole null result, and of the first, wrong duality, it says that "only the shared-photon form of §11.4 contests this ground, and that form needs P4 restated"; §11.4 is P.R.'s magnetic-mirror conjecture [O]. The explanation (§11.1, App. A item 5; flag 62) and conjugate monopoles abundant in momentum space as a third dark-matter candidate (§12) are P.R.'s open conjectures ([Conjecture: conjugate monopoles explain the null result](monopole-explanation.md); [Conjecture: magnetic monopoles abundant in momentum space](../dark-matter/candidates/momentum-space-monopoles.md)).

## The critiques

The critiques on record come from the reviews of the soliton manuscript, which used the identification as motivation for its [hidden sector](../dark-matter/candidates/soliton-candidate/hidden-sector.md).

- **Round 2.** The soliton manuscript's v2 used the shared matrix to fix its hidden coupling, conjecturing that reciprocity acts on gauge couplings as S. The round-2 referee graded v2 "B near B/C / medium" with "weakest link = the α_d derivation ("matrix coincidence ≠ physical identity" / "numerology")" ([`HANDOFF.md` §6](../../HANDOFF.md#6-review-history-and-the-measured-failure-mode); [review rounds 1 and 2](../method/review/rounds-one-and-two.md); [Under review: the coupling α_d ≈ 34](../dark-matter/candidates/soliton-candidate/alpha-d-coupling.md)).
- **[#14](../../notes/knot-dark-matter-standalone.md) v3** kept the identification as motivation only: "We use this only as motivation: it suggests that the vacuum event that polarizes phase space also fixes which description of a gauge sector is the electric one. No numerical result below depends on it." ([#14 §2](../../notes/knot-dark-matter-standalone.md#2-the-hidden-sector-and-its-coupling)). Its [acceptance criterion 1](../symmetry-breaking/toy-models/acceptance-criterion.md) asked for an action with η "selecting both the position polarization and the hidden sector's electric description" ([#14 §6](../../notes/knot-dark-matter-standalone.md#6-status-of-claims-and-acceptance-criteria)).
- **Round 3.** The [pre-registration](../method/review/round-3/preregistration.md) expected the weakest link to be that the framework does no work: "Nothing numerical depends on Born reciprocity, the compatibility theorem or the polarization identification" ([`review/round3-preregistration.md`](../../review/round3-preregistration.md)). The referee named it as the second weakest link, after "the Kibble abundance / mass determination" (Step 5). Its citation check called "Charge space is symplectic" "interpretation" (Step 1), and its conceptual audit concluded that the phase-space framework did no work in the proposal (Step 4(d); [the 'framework does no work' critique](../program/framework-does-no-work.md); [review round 3](../method/review/round-3/_index.md)).

The withdrawn manuscript is [#14](../dark-matter/candidates/soliton-candidate/_index.md). The checkpoint, amended after round 3, keeps [§11.3](../papers/broken-born-checkpoint-v2.md#113-the-identification-d--structural-math-t) as a structural observation and makes no numerical use of it.

## What is open

Whether the phase-space and charge-space polarizations are components of one enlarged structure is a conjecture [O], #11's open problem 8 ([Open: one modular structure for both polarizations (OP8)](unified-modular-structure.md)). The demand that the [order parameter](../symmetry-breaking/order-parameter.md) also select the electric charges, part of the handoff's and #14's wording of the toy-model criterion, has not been addressed ([acceptance criterion 1](../symmetry-breaking/toy-models/acceptance-criterion.md)).

[The popular article #12](../history/documents/popular-articles.md) presents the unification without its open status, as "The framework's proposal is that the two divisions are one", and goes on to identify the momentum-polarized sector with the magnetic side of electromagnetism. The checkpoint records P.R.'s magnetic-mirror conjecture, open, and says that the conjecture "is what §11.3's conjecture would give if one vacuum event selected both the position polarization and the electric sublattice" ([#11 §11.4](../papers/broken-born-checkpoint-v2.md#114-the-magnetic-mirror-conjecture-o-pr-v23)). [#12](../../popsci/universes-other-half.md)'s version, magnetic charge of our own photon, is the conjecture's shared-photon form ([Conjecture: the momentum sector as the magnetic mirror](magnetic-identification.md)).

## Sources

- [`wiki/papers/broken-born-checkpoint-v2.md` §11.3](../papers/broken-born-checkpoint-v2.md#113-the-identification-d--structural-math-t) — the identification [D — structural; math T] and the recurring matrix; [§11.4](../papers/broken-born-checkpoint-v2.md#114-the-magnetic-mirror-conjecture-o-pr-v23) — P.R.'s magnetic-mirror conjecture, what [§11.3](../papers/broken-born-checkpoint-v2.md#113-the-identification-d--structural-math-t)'s conjecture would give [O]; [§11.1](../papers/broken-born-checkpoint-v2.md#111-the-monopole-audit-revised-d) and [App. A item 5](../papers/broken-born-checkpoint-v2.md#appendix-a-audit-of-founding-suppositions-pr-with-fates) — the grounds against the explanation of the null result, P.R.'s open conjecture; [§12](../papers/broken-born-checkpoint-v2.md#12-the-dark-sector-question-three-candidates) — the third candidate, P.R.'s open conjecture; [§1](../papers/broken-born-checkpoint-v2.md#1-two-abstracts) — the technical abstract; [§4](../papers/broken-born-checkpoint-v2.md#4-postulates) — P5; [§6](../papers/broken-born-checkpoint-v2.md#6-the-modular-field) — Z → −Z⁻¹ and its fixed point; [§15](../papers/broken-born-checkpoint-v2.md#15-assessment) — the assessment; [App. A item 11](../papers/broken-born-checkpoint-v2.md#appendix-a-audit-of-founding-suppositions-pr-with-fates) — the program-native addition; ref [17]†.
- [`wiki/papers/reciprocity-toy-models.md` §1](../papers/reciprocity-toy-models.md#1-setting-and-prior-work) — ω and ρ as the matrix [[0, 1], [−1, 0]] in d = 1.
- [`verify/toy_coset.py`](../../verify/toy_coset.py) 'Anchors', 'S2: vacua' — ρ as the quarter turn and its action Z → −1/Z.
- [`HANDOFF.md` §2](../../HANDOFF.md#2-scientific-state-one-screen) — the identification listed as alive; [§3](../../HANDOFF.md#3-artifact-inventory-creation-order) — §11 added in v2.0; [§6](../../HANDOFF.md#6-review-history-and-the-measured-failure-mode) — round 2's "matrix coincidence ≠ physical identity".
- [`notes/knot-dark-matter-standalone.md` §2](../../notes/knot-dark-matter-standalone.md#2-the-hidden-sector-and-its-coupling), [§6](../../notes/knot-dark-matter-standalone.md#6-status-of-claims-and-acceptance-criteria) — the identification used "only as motivation"; acceptance criterion 1 with the electric description (withdrawn manuscript).
- [`review/round3-preregistration.md`](../../review/round3-preregistration.md) 'Predictions' — the forecast that nothing numerical depends on the identification.
- [`review/round3/referee/audit-notes.md`](../../review/round3/referee/audit-notes.md) Step 1, Step 4(d), Step 5 — the 2π versus 4π normalization and "interpretation"; the framework doing no work in #14; the order of the weakest links.
- [`review/round3-adjudication.md`](../../review/round3-adjudication.md) 'Rulings' 12 — the normalization and Schwinger, accepted as minor.
- [`review/wiki-build-flags.md`](../../review/wiki-build-flags.md) flag 60 — #12's identification as the conjecture's shared-photon form; flag 62 — the explanation of the null result open, in that form's setting.
- [`notes/literature-check.md` §5](../../notes/literature-check.md#5-the-magnetic-mirror-c4-partly-anticipated); [`review/wiki-build-flags.md`](../../review/wiki-build-flags.md) flag 67 — the bridge between the two dualities as a published remark; pending.
- [`popsci/universes-other-half.md`](../../popsci/universes-other-half.md) 'Dark matter as the other polarization' — the unification as "The framework's proposal" (not a status source).
