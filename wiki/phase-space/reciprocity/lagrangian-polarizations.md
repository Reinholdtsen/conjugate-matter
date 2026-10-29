---
title: "Lagrangian subspaces and polarizations"
weight: 60
status: established
description: "Maximal subspaces on which ω vanishes; choosing one is choosing which coordinates count as 'position', the choice the program says the vacuum makes."
provenance: [T]
sources:
  - "papers/broken-born-checkpoint-v2.md §3"
  - "papers/broken-born-checkpoint-v2.md §4"
  - "papers/broken-born-checkpoint-v2.md §11"
  - "papers/reciprocity-toy-models.md §1"
  - "papers/reciprocity-toy-models.md §2"
  - "papers/reciprocity-toy-models.md §5"
  - "notes/broken-born-theory.md §1"
  - "notes/broken-born-theory.md §2"
  - "notes/broken-born-theory.md 'Addendum (v0.3, overnight)'"
  - "notes/geometric-core.md §B"
  - "notes/toy-lagrangian.md 'Chunk 1 results'"
  - "verify/toy_s5.py"
  - "review/wiki-build-flags.md item 1"
  - "review/wiki-build-checks/verifier_null_lagrangians.py"
---

*A Lagrangian subspace of phase space is a set of directions, half the dimension of phase space, on which the [symplectic form](/wiki/phase-space/reciprocity/symplectic-form) vanishes: no two of its directions form a position–momentum pair. Choosing one, a polarization, is choosing which coordinates count as "position". The ordinary position axis is one Lagrangian subspace, the momentum axis is another, and a continuous family of tilted ones lies in between. A quantum state can be written as a wavefunction over any of them, and the different descriptions are related by unitary transforms such as the Fourier transform. The program's postulates say that the vacuum carries one such choice, and that ours is tilted toward position.*

**Status:** Established — standard symplectic geometry [T] — the d = 1 statements the toy models rely on are machine-checked [V] in `verify/toy_s5.py` (see [the toy-model scripts](/wiki/method/verification/toy-model-scripts)). What the program does with the choice is its own claim: the postulate [P5](/wiki/program/postulates/p5-spontaneous-selection) [P] and the argument of [mandatory breaking](/wiki/symmetry-breaking/mandatory-breaking).

## Definition

A subspace L of phase space ℝ^{2d} is isotropic when the symplectic form vanishes on it, ω(u, v) = 0 for all u and v in L, and Lagrangian when it is isotropic and as large as an isotropic subspace can be, of dimension d [T]. Since ω pairs each direction with a conjugate partner, an isotropic subspace never contains both members of a pair.

Examples [T]:

- **The coordinate subspaces.** The position subspace {p = 0} and the momentum subspace {x = 0} are Lagrangian. In quantum mechanics the positions x¹, …, x^d commute with one another, as do the momenta; these two complete sets of commuting coordinates go with the two coordinate subspaces.
- **Tilted subspaces.** The graph {(x, Ax)} of a d × d matrix A is Lagrangian exactly when A is symmetric, since ω((x, Ax), (y, Ay)) = xᵀ(A − Aᵀ)y. The symmetric matrices thus give coordinates on the set of Lagrangian subspaces near the position subspace, with d(d+1)/2 independent entries.
- **One degree of freedom.** For d = 1 phase space is a plane, ω is the signed area, and every line through the origin is Lagrangian. The gate's check reads "L+ and L- are Lagrangian (w vanishes on each line trivially in d = 1) and transverse: w(e+, e-) != 0" (`verify/toy_s5.py`).

## Polarizations: which coordinates are "position"

In the program's usage, a polarization is a choice of which Lagrangian subspace counts as position. States are then written as wavefunctions of the coordinates along it, and a transverse Lagrangian subspace supplies the conjugate momenta [T]. (Geometric quantization uses the word for the closely related choice of directions along which wavefunctions are constant [T].)

The ordinary choice writes a state as ψ(x); the opposite choice writes it as ψ̃(p). The two are related by the [Fourier transform](/wiki/phase-space/reciprocity/fourier-transform), and any two choices are related by some unitary operator (the metaplectic representation) [T]. Within quantum kinematics, then, the choice is a convention: the same state written in other coordinates ([unitary equivalence versus Noether symmetry](/wiki/phase-space/reciprocity/unitary-equivalence)). The program's claim is that it is not a convention but a property of the vacuum.

## The program's use

[#11](/wiki/history/documents/checkpoint) §3 makes some choice compulsory: "[x,p] = iℏ forbids joint locality, so any world with local physics must select a Lagrangian polarization." See [the canonical commutator](/wiki/phase-space/reciprocity/canonical-commutator) and [mandatory breaking](/wiki/symmetry-breaking/mandatory-breaking).

The postulate P5 says which: "The vacuum selects a polarization; ours is x-tilted; the mirror vacuum is equally lawful." [P] (#11 §4; [P5](/wiki/program/postulates/p5-spontaneous-selection)). The [lab notebook](/wiki/history/documents/lab-notebook)'s version names the Lagrangian explicitly: "The vacuum selects a Lagrangian polarization of 𝒫; ours is x-tilted. The choice is spontaneous: the mirror vacuum is an equally good solution." (#1 §1).

Since v2.2 the choice is a continuous angle rather than a discrete pick. With only ω rigid, the reciprocity map ρ ([Born reciprocity](/wiki/phase-space/reciprocity/born-reciprocity)) "sits inside a continuous U(1), and the polarization is a Goldstone angle rather than a discrete choice [D][V]" (#11 §4; [the polarization as a Goldstone angle](/wiki/symmetry-breaking/goldstone-angle)).

## A polarization from a real structure

The [toy-model note](/wiki/symmetry-breaking/toy-models) builds the choice out of a matrix: "A real structure K with K² = 1 and Kᵀ ω K = −ω defines a neutral metric η = ωK. Its null lines are the two eigenlines L± of K, which are Lagrangian. Choosing K is choosing which line is 'position'." (§1). A [neutral metric](/wiki/phase-space/born-geometry/born-structures) is a symmetric pairing with as many positive as negative directions; its null lines are the directions of zero length.

The steps are checked symbolically in `verify/toy_s5.py`, part A [V]:

1. η = ωK is a symmetric neutral metric (det = −1).
2. K's eigenvectors e± (eigenvalues +1 and −1) are null for η, for every angle φ, and they span the only null lines.
3. L+ and L− are Lagrangian and transverse.
4. K → −K sends η → −η with the same null lines.
5. ρ maps K to −K, and L+ onto L−.

In [model I](/wiki/symmetry-breaking/toy-models/coset-model) the real structures compatible with the metric H = 1 form a circle, K(φ) = [[cos φ, sin φ], [sin φ, −cos φ]] (toy-model note §2), and the script takes e+ = (cos φ/2, sin φ/2): the line L+ sits at angle φ/2. Advancing φ by π turns L+ through a quarter-turn onto the line where L− began; that is the map K(φ) → K(φ + π) = −K(φ) by which ρ acts (§2). A full circuit of φ turns L+ through a half-turn, which brings every line through the origin back to itself, so each Lagrangian line corresponds to one value of φ. The angle φ therefore parametrizes the choice of polarization; the note says the compact angle φ "parametrizes the Lagrangian Grassmannian Λ(1)" (§2). See [the order parameter](/wiki/symmetry-breaking/order-parameter) and [the section condition](/wiki/symmetry-breaking/section-condition).

For any d the same construction works [T]. If Ku = u and Kv = v, then ω(u, v) = ω(Ku, Kv) = −ω(u, v), so ω vanishes on each eigenspace of K. The two eigenspaces together span phase space, and each is isotropic, so each has dimension d: K splits phase space into a transverse pair of Lagrangian subspaces. Freidel, Leigh and Minic ([broken Born duality](/wiki/phase-space/reciprocity/broken-born-duality)) label the solutions of their theory by such pairs: "The solutions are labelled by bi-Lagrangians and spacetime is a derived dynamical concept" (arXiv:1307.7080, as the worklog quotes it, "Chunk 1 results").

The documents name the real structure differently. #11's [P2′](/wiki/program/postulates/p2-prime) writes "η = HJ, with the real structure J chosen spontaneously"; the toy-model note writes η = ωK with K the real structure, and #11 §14 item 11 uses the same η = ωK. The sources do not reconcile the two notations; this page follows the toy note.

## The space of all choices

"The space of Lagrangian polarizations of ℝ^{2d} is the Lagrangian Grassmannian Λ(d) ≅ U(d)/O(d), compact, of dimension d(d+1)/2 = 10 for d=4." [T] (#1 §2). The dimension matches the symmetric-matrix coordinates above, one for each independent entry. For d = 1, Λ(1) is a circle, the toy's angle φ. The fundamental group of Λ(d) is ℤ, "generated by the **Maslov circle**" [T] (#1 §2), which the program makes the home of the dark-energy field τ ([τ as hilltop quintessence](/wiki/cosmology/dark-energy/tau-quintessence)). See [the Lagrangian Grassmannian Λ(d)](/wiki/phase-space/modular-field/lagrangian-grassmannian) and [τ as the Maslov phase of the boundary](/wiki/phase-space/modular-field/maslov-phase).

## When too much is frozen

If the neutral metric η is held rigid as well as ω, a polarization must be Lagrangian for ω and null for η at once. Calc note [#5](/wiki/history/documents/field-equation-notes) finds the compatible polarizations "**discrete** — the 2^d coordinate-type splittings, GL(d)-rigid. No Lagrangian Grassmannian, no Maslov circle, **no τ field**." (§B). Flag 1 in `review/wiki-build-flags.md` queries the word "discrete". For d ≥ 2, any subspace V of the position directions, taken together with its orthogonal complement V^⊥ placed in the momentum directions, gives a polarization V ⊕ V^⊥ that is Lagrangian for ω and null for η, so the compatible polarizations form continuous Grassmannian families Gr(k, d). The Maslov phase det² is constant (±1) on each family, so no family winds around the Maslov circle, and the conclusion, no Maslov circle and no τ, stands. The flag's executed check, at d = 2 and 3, is `review/wiki-build-checks/verifier_null_lagrangians.py`; the flag awaits Paul's ruling. The same note's second consequence is that the [geometric action](/wiki/gravity/tuning-test/geometric-action) becomes a functional of the metric g alone, with no [momentum graviton](/wiki/gravity/momentum-graviton). The two together are why the [original P2](/wiki/program/postulates/original-p2), which froze η, was replaced by [P2′](/wiki/program/postulates/p2-prime). Under P2′, η is emergent, "the order parameter itself, η = HJ, with the real structure J chosen spontaneously from U(d)/O(d) = Λ(d)" (#1, addendum v0.3).

## Prior art and a second arena

Freidel, Leigh and Minic "make η dynamical and describe spacetime as a choice of Lagrangian [1]" (toy-model note §1; [broken Born duality](/wiki/phase-space/reciprocity/broken-born-duality)).

The same structure recurs in charge space. "Mutual locality (which charges can share one Lagrangian) is ⟨q,q′⟩ = 0: a **Lagrangian sublattice**. Choosing a duality frame — which particles are 'electric' (fundamental) versus 'magnetic' (solitonic) — is choosing a Lagrangian polarization of charge space, in the literature's own words." [D — structural; math T] (#11 §11.3; [the symplectic charge lattice](/wiki/electric-magnetic-duality/symplectic-charge-lattice)). #11 attaches no reference to the phrase "in the literature's own words", which leaves it to [the † literature battery](/wiki/method/literature-battery).

## Standard references

Added by the wiki from model memory (†); the program's documents do not cite them.

- V. I. Arnold (1967)†: the Maslov index and the topology of the Lagrangian Grassmannian.
- V. Guillemin and S. Sternberg, *Symplectic Techniques in Physics* (1984)†: Lagrangian subspaces and their uses.
- N. M. J. Woodhouse, *Geometric Quantization* (1980)†: polarizations in quantization.

## Used by

- [Mandatory breaking: the uncertainty argument](/wiki/symmetry-breaking/mandatory-breaking) — any world with local physics must select a polarization.
- [The hard core: spontaneously broken Born reciprocity](/wiki/program/hard-core) — η's null lines as the possible "position" axes.
- [P1: the phase-space arena](/wiki/program/postulates/p1-arena) — P5's choice is a Lagrangian subspace of P1's phase space.
- [P2′: only the symplectic form is rigid](/wiki/program/postulates/p2-prime) — the vacuum's real structure ranges over all Lagrangian subspaces.
- [P4: polarized matter and strict sector separation](/wiki/program/postulates/p4-polarized-matter) — x-polarized and p-polarized matter.
- [P5: the vacuum selects a polarization](/wiki/program/postulates/p5-spontaneous-selection) — ours is x-tilted, the mirror vacuum equally lawful.
- [Original P2 (superseded)](/wiki/program/postulates/original-p2) and [the nontriviality theorem](/wiki/program/postulates/nontriviality-theorem) — with η rigid as well, the compatible polarizations include no Maslov circle (on #5's word "discrete" for them, see flag 1 in `review/wiki-build-flags.md`).
- [The order parameter: J, η and K](/wiki/symmetry-breaking/order-parameter) — choosing K is choosing which line is "position".
- [The polarization as a Goldstone angle](/wiki/symmetry-breaking/goldstone-angle) and [Open: the origin of the ρ-preserving potential](/wiki/symmetry-breaking/rho-preserving-potential) — the choice as an angle on Λ(1).
- [The section condition: what η fixes](/wiki/symmetry-breaking/section-condition) — matter confined to one Lagrangian null line.
- [Acceptance criterion 1](/wiki/symmetry-breaking/toy-models/acceptance-criterion) and [model I: action and symmetries](/wiki/symmetry-breaking/toy-models/coset-model/action-and-symmetries) — η fixes which Lagrangian line of the toy counts as position.
- [Why X must be massive](/wiki/gravity/momentum-graviton/forcing-chain), [the gravitational Higgs mechanism](/wiki/gravity/momentum-graviton/gravitational-higgs) and [shift symmetry](/wiki/gravity/momentum-graviton/shift-symmetry) — the vacuum's choice of polarization breaks the dual diffeomorphisms.
- [The palindrome βₙ = β₄₋ₙ](/wiki/gravity/palindromic-branch/palindrome) — one of the potential's two frames is set by the polarization.
- [The χ-particle candidate](/wiki/dark-matter/candidates/chi-particles) — χ is matter of the momentum polarization.
- [Two causal cones](/wiki/conjugate-relativity/two-causal-cones), [dual inertia](/wiki/conjugate-relativity/dual-inertia), [force dilation](/wiki/conjugate-relativity/force-dilation), [the invariant-length shell](/wiki/conjugate-relativity/invariant-length-shell) and [the equivalence principle as dual relativity](/wiki/conjugate-relativity/equivalence-principle) — #13's kinematics of the momentum polarization.
- [The symplectic charge lattice](/wiki/electric-magnetic-duality/symplectic-charge-lattice) and [Open: one modular structure for both polarizations (OP8)](/wiki/electric-magnetic-duality/unified-modular-structure) — a duality frame as a Lagrangian polarization of charge space.
- [Conjecture: the momentum sector as the magnetic mirror](/wiki/electric-magnetic-duality/magnetic-identification) — P.R.'s conjecture of a magnetically charged momentum-polarized analog for each electrically charged particle, which is what #11 §11.3's conjecture would give if one vacuum event selected both the position polarization and the electric sublattice (#11 §11.4).

## Sources

- `papers/broken-born-checkpoint-v2.md` §3 — the mandatory selection of a Lagrangian polarization.
- `papers/broken-born-checkpoint-v2.md` §4 — P5; the v2.2 refinement; P2′'s notation η = HJ.
- `papers/broken-born-checkpoint-v2.md` §11 — Lagrangian sublattices and duality frames in charge space; §11.4 — the magnetic-mirror conjecture, what §11.3's conjecture would give if one vacuum event made both choices [O].
- `papers/reciprocity-toy-models.md` §1, §2, §5 — K's eigenlines as η's Lagrangian null lines; the circle K(φ) and Λ(1); Freidel–Leigh–Minic's "choice of Lagrangian".
- `verify/toy_s5.py` — the d = 1 Lagrangian-line checks (part A).
- `notes/geometric-core.md` §B — the splittings compatible with a rigid η, which the note calls discrete.
- `review/wiki-build-flags.md` item 1 and `review/wiki-build-checks/verifier_null_lagrangians.py` — the query on "discrete": continuous families V ⊕ V^⊥ for d ≥ 2, with det² constant on each; awaiting Paul's ruling.
- `notes/broken-born-theory.md` §1, §2, addendum v0.3 — P5; Λ(d) ≅ U(d)/O(d), its dimension and the Maslov circle; J chosen from Λ(d).
- `notes/toy-lagrangian.md` "Chunk 1 results" — the bi-Lagrangian quotation from arXiv:1307.7080.
