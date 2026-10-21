---
title: "The symplectic charge lattice"
weight: 70
status: alive
description: "The DSZ pairing makes charge space symplectic, mutually local charges form a Lagrangian sublattice, and choosing a duality frame is choosing a polarization — the same matrix [[0,1],[−1,0]] behind ρ, Z → −Z⁻¹ and S-duality."
provenance: [D, T]
sources:
  - "papers/broken-born-checkpoint-v2.md §11.3"
  - "papers/broken-born-checkpoint-v2.md §1"
  - "papers/broken-born-checkpoint-v2.md §4"
  - "papers/broken-born-checkpoint-v2.md §6"
  - "papers/broken-born-checkpoint-v2.md §15"
  - "papers/broken-born-checkpoint-v2.md App. A item 11"
  - "papers/broken-born-checkpoint-v2.md ref [17]"
  - "papers/reciprocity-toy-models.md §1"
  - "HANDOFF.md §2"
  - "HANDOFF.md §3"
  - "HANDOFF.md §6"
  - "notes/knot-dark-matter-standalone.md §2"
  - "notes/knot-dark-matter-standalone.md §6"
  - "review/round3-preregistration.md 'Predictions'"
  - "review/round3/referee/audit-notes.md Step 1"
  - "review/round3/referee/audit-notes.md Step 4(d)"
  - "review/round3-adjudication.md 'Rulings' 12"
  - "verify/toy_coset.py 'Anchors', 'S2: vacua'"
  - "popsci/universes-other-half.md 'Dark matter as the other polarization'"
---

*The symplectic charge lattice is the program's observation that the set of allowed electric and magnetic charges has the same geometry as phase space. The Dirac–Schwinger–Zwanziger (DSZ) pairing of two charges is an antisymmetric whole-number form, like the pairing of position with momentum; charges that can all be described together by one Lagrangian form a "Lagrangian" half of the lattice; and deciding which particles count as electric is therefore a choice of polarization, as the program's vacuum chooses which coordinates count as position. One quarter-turn matrix generates Born reciprocity, the program's modular inversion and S-duality. The checkpoint counts this as a structural unification [D — structural; math T]: the mathematics is established, the identification of the two choices is the program's, and no calculation depends on it. Whether the two polarizations are one physical structure is open problem 8.*

**Status:** Alive — [D — structural; math T] — #11 §11.3. No script checks the charge-lattice statements. The phase-space side of the shared matrix is machine-checked in d = 1: `verify/toy_coset.py` confirms that "rho is symplectic and is the quarter turn: rho^2 = -1" (section 'Anchors') and that "rho acts on Z as Z -> -1/Z with fixed point Z = i" (section 'S2: vacua') ([the toy-model scripts](/wiki/method/verification/toy-model-scripts)). The DSZ citation [17†] is from model memory and awaits [the † literature battery](/wiki/method/literature-battery).

## The charge lattice [T]

In a theory with one unbroken U(1) gauge field, such as electromagnetism, each particle carries an electric charge e and a magnetic charge g, written as a pair q = (e, g). A particle with both is a dyon. Quantum mechanics allows only a discrete set of charge pairs, and sums of allowed charges are allowed, so the allowed charges form a lattice in the (e, g) plane [T]. With r unbroken U(1) factors the lattice has 2r dimensions, one electric and one magnetic direction per factor.

## The DSZ pairing [T]

Dirac showed that a magnetic charge g and an electric charge e can coexist only if e·g is a whole multiple of a fixed constant ([Dirac quantization and the DSZ pairing](/wiki/electric-magnetic-duality/monopoles/dirac-quantization)). The reason is angular momentum: the combined field of an electric charge and a monopole carries angular momentum proportional to the product of their charges, and angular momentum is quantized [T]. Schwinger and Zwanziger extended the argument to two dyons, for which the field angular momentum depends on e₁g₂ − e₂g₁, and the condition becomes a condition on that combination [T].

[#11](/wiki/history/documents/checkpoint) §11.3:

> The Dirac–Schwinger–Zwanziger pairing ⟨q, q′⟩ = e₁g₂ − e₂g₁ ∈ 2πℤ is an antisymmetric integer form: **the charge lattice is a symplectic space** [17†].

The pairing is antisymmetric: exchanging the two charges reverses its sign, ⟨q′, q⟩ = −⟨q, q′⟩, so a charge paired with itself gives zero. In matrix form [T]:

```text
⟨q, q′⟩ = (e₁, g₁) [[0, 1], [−1, 0]] (e₂, g₂)ᵀ = e₁g₂ − e₂g₁
```

The normalization differs between sources. The round-3 referee, checking #14's citation of Dirac and Zwanziger, found that "Zwanziger's abstract states e_m g_n - g_m e_n in 4 pi Z; manuscript writes 2 pi Z (Dirac normalization). The 't Hooft-Polyakov monopole with doublets realises 2 pi, so the physics is fine; but [7] as cited states 4 pi. "Charge space is symplectic" is interpretation." The referee also noted that Schwinger was named but not cited (`review/round3/referee/audit-notes.md`, Step 1). Ruling 12 accepted these as minor citation issues ([round-3 rulings](/wiki/method/review/round-3/rulings)); #11 now cites Schwinger 1966 in [17]†.

## The same geometry as phase space

A symplectic form is an antisymmetric pairing that leaves no direction paired to zero with everything ([the symplectic form](/wiki/phase-space/reciprocity/symplectic-form)). Phase space carries one, ω, which pairs each position with its momentum. For one degree of freedom the toy-model note writes it as a matrix: "Phase space ℝ² with symplectic form ω = [[0, 1], [−1, 0]]. ρ = [[0, 1], [−1, 0]] is symplectic and squares to −1." (`papers/reciprocity-toy-models.md` §1). In the (e, g) basis the DSZ pairing has the same matrix. The comparison, side by side:

| | phase space | charge space |
| --- | --- | --- |
| elements | points (x, p) | charges q = (e, g) |
| pairing | ω, antisymmetric | ⟨q, q′⟩ = e₁g₂ − e₂g₁, antisymmetric |
| values | real numbers | integer multiples of 2π |
| a Lagrangian half | a subspace on which ω vanishes | a sublattice on which ⟨·,·⟩ vanishes |
| choosing one | a polarization: which coordinates are "position" | a duality frame: which charges are "electric" |
| transformations preserving the pairing [T] | Sp(2d,ℝ), continuous | integer symplectic matrices; for one U(1), SL(2,ℤ) |

The last row is standard mathematics [T]: a lattice is preserved only by matrices with integer entries, so the symmetries of charge space form a discrete group, while those of phase space form a continuous one. The checkpoint does not comment on the difference.

## Mutual locality and Lagrangian sublattices

#11 §11.3 continues: "Mutual locality (which charges can share one Lagrangian) is ⟨q,q′⟩ = 0: a **Lagrangian sublattice**."

Two charges with a vanishing pairing can be coupled to one set of gauge potentials in a single local Lagrangian [T]. All purely electric charges (g = 0) are mutually local, which is why ordinary electrodynamics has a local Lagrangian. An electron and a magnetic monopole are not: their pairing is not zero, and a description containing both needs a Dirac string or a second set of potentials [T]. A largest set of mutually local charges is a Lagrangian sublattice, the integer analogue of a [Lagrangian subspace](/wiki/phase-space/reciprocity/lagrangian-polarizations), half the dimension of the lattice. For a single U(1), the pairing of two charges vanishes exactly when they are proportional, so a Lagrangian sublattice consists of the lattice points on one line through the origin.

## A duality frame is a polarization

The step the program adds [D — structural], #11 §11.3:

> Choosing a duality frame — which particles are "electric" (fundamental) versus "magnetic" (solitonic) — is choosing a Lagrangian polarization of charge space, in the literature's own words.

In any one Lagrangian description of a gauge theory, the charges carried by the elementary quanta of its fields are the electric ones, and the charges that appear only on solitons, such as ['t Hooft–Polyakov monopoles](/wiki/electric-magnetic-duality/monopoles/thooft-polyakov-monopole), are the magnetic ones [T]. A duality transformation gives an equivalent description in which a different Lagrangian sublattice plays the electric role; S-duality exchanges the electric and magnetic sublattices ([S-duality and Montonen–Olive](/wiki/electric-magnetic-duality/s-duality)). Choosing a frame is choosing a Lagrangian sublattice, in the same sense that the program's postulate [P5](/wiki/program/postulates/p5-spontaneous-selection) has the vacuum choose a Lagrangian subspace of phase space as "position".

The phrase "in the literature's own words" carries no citation. It is flagged for the † literature battery ([conflicts between sources](/wiki/history/documents/source-conflicts)).

## One matrix, three appearances

#11 §11.3: "S-duality acts on the complexified coupling by τ_c → −1/τ_c, generated by the same [[0,1],[−1,0]] rotation as Born's ρ and our Z → −Z⁻¹: the third appearance of one matrix in this program."

```text
the matrix [[0, 1], [−1, 0]] generates
  Born reciprocity     ρ: (x, p) → (p, −x)          on phase space
  modular inversion    Z → −Z⁻¹                     on the modular field
  S-duality            τ_c → −1/τ_c                 on the complexified coupling
```

- **Born reciprocity** is the symmetry of quantum kinematics that the program takes as exact and spontaneously broken; the Fourier transform implements it ([Born reciprocity](/wiki/phase-space/reciprocity/born-reciprocity)).
- **The modular inversion** is ρ acting on the modular field Z = X + iY, the program's packaging of the phase-space metric; its fixed point Z = i is the vacuum (#11 §6; [reciprocity as modular inversion](/wiki/phase-space/modular-field/modular-inversion)). The d = 1 form is the gated check quoted in the status line.
- **S-duality** acts on τ_c, the complexified gauge coupling, not the dark-energy field τ ([notation](/wiki/notation)).

The matrix squares to −1 in each setting [T]. On phase space ρ² sends (x, p) to (−x, −p), and on charges S² sends (e, g) to (−e, −g), charge conjugation. Both leave the modular variable unchanged, since −1/(−1/τ) = τ.

## What kind of claim it is

The tag [D — structural; math T] divides the claim. The mathematics is literature: the antisymmetric DSZ pairing, mutual locality, the duality group acting on charges and couplings. The program's contribution is the identification of the electric–magnetic frame choice with the phase-space polarization choice as the same operation, with no dynamics behind it: no Lagrangian in the repository relates the two choices.

The checkpoint counts the identification in several places:

- the technical abstract: "The electric–magnetic charge lattice, with its Dirac–Schwinger–Zwanziger symplectic pairing [17†], furnishes a second arena in which the same polarization choice recurs" (#11 §1);
- the assessment: "one structural unification (polarization of phase space and of charge space as one move)", and among the progressive signs "the §11.3 unification generating new questions" (#11 §15; [the program's self-assessment](/wiki/program/assessment));
- founding supposition 11: "the polarization identification as the program-native addition" to the established [magnetic mirror-family](/wiki/electric-magnetic-duality/magnetic-mirror-family) (#11 App. A item 11);
- [the handoff](/wiki/history/documents/handoff), under "Alive": "Charge-lattice identification: DSZ pairing is symplectic; duality frame choice = Lagrangian polarization, same [[0,1],[−1,0]] generator as Born rotation and S-duality" (`HANDOFF.md` §2).

The section first appeared in the checkpoint's v2.0; the handoff lists "charge-lattice §11" among v2.0's additions (`HANDOFF.md` §3). The v2.1 and v2.2 change lists do not touch it.

## The critiques

The critiques on record come from the reviews of the soliton manuscript, which used the identification as motivation for its hidden sector.

- **Round 2.** The soliton manuscript's v2 used the shared matrix to fix its hidden coupling, conjecturing that reciprocity acts on gauge couplings as S. The referee graded the round "B near B/C / medium" with "weakest link = the α_d derivation ("matrix coincidence ≠ physical identity" / "numerology")" (`HANDOFF.md` §6; [review rounds 1 and 2](/wiki/method/review/rounds-one-and-two); [Obituary: the coupling α_d ≈ 34](/wiki/dark-matter/candidates/soliton-candidate/alpha-d-coupling)).
- **#14 v3** stepped back: "We use this only as motivation: it suggests that the vacuum event that polarizes phase space also fixes which description of a gauge sector is the electric one. No numerical result below depends on it." (#14 §2). Its acceptance criterion 1 asked for an action with η "selecting both the position polarization and the hidden sector's electric description" (#14 §6).
- **Round 3.** The pre-registration expected the weakest link to be that the framework does no work: "Nothing numerical depends on Born reciprocity, the compatibility theorem or the polarization identification" (`review/round3-preregistration.md`). The referee agreed. Its citation check called "Charge space is symplectic" "interpretation" (Step 1), and its conceptual audit concluded that the phase-space framework did no work in the proposal (Step 4(d); [the 'framework does no work' critique](/wiki/program/framework-does-no-work); [review round 3](/wiki/method/review/round-3)).

The withdrawn manuscript is [#14](/wiki/dark-matter/candidates/soliton-candidate). The checkpoint, amended after round 3, keeps §11.3 as a structural observation and makes no numerical use of it.

## What is open

Whether the phase-space and charge-space polarizations are components of one enlarged structure is a conjecture [O], #11's open problem 8 ([Open: one modular structure for both polarizations (OP8)](/wiki/electric-magnetic-duality/unified-modular-structure)). The demand that the order parameter also select the electric charges, part of the handoff's and #14's wording of the toy-model criterion, has not been addressed ([acceptance criterion 1](/wiki/symmetry-breaking/toy-models/acceptance-criterion)).

[The popular article #12](/wiki/history/documents/popular-articles) presents the unification without its open status, as "The framework's proposal is that the two divisions are one", and goes on to identify the momentum-polarized sector with the magnetic side of electromagnetism. That claim is found only in #12 and is dead ([Obituary: the magnetic identification (popsci-only)](/wiki/electric-magnetic-duality/magnetic-identification)).

## Sources

- `papers/broken-born-checkpoint-v2.md` §11.3 — the identification [D — structural; math T] and the recurring matrix; §1 — the technical abstract; §4 — P5; §6 — Z → −Z⁻¹ and its fixed point; §15 — the assessment; App. A item 11 — the program-native addition; ref [17]†.
- `papers/reciprocity-toy-models.md` §1 — ω and ρ as the matrix [[0, 1], [−1, 0]] in d = 1.
- `verify/toy_coset.py` 'Anchors', 'S2: vacua' — ρ as the quarter turn and its action Z → −1/Z.
- `HANDOFF.md` §2 — the identification listed as alive; §3 — §11 added in v2.0; §6 — round 2's "matrix coincidence ≠ physical identity".
- `notes/knot-dark-matter-standalone.md` §2, §6 — the identification used "only as motivation"; acceptance criterion 1 with the electric description (withdrawn manuscript).
- `review/round3-preregistration.md` 'Predictions' — the forecast that nothing numerical depends on the identification.
- `review/round3/referee/audit-notes.md` Step 1, Step 4(d) — the 2π versus 4π normalization and "interpretation"; the framework doing no work in #14.
- `review/round3-adjudication.md` 'Rulings' 12 — the normalization and Schwinger, accepted as minor.
- `popsci/universes-other-half.md` 'Dark matter as the other polarization' — the unification as "The framework's proposal" (not a status source).
