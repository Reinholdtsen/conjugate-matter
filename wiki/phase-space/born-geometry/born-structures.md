---
title: "The structures ω, η, H and the split-quaternion algebra"
weight: 10
status: established
description: "I = ω⁻¹H, J = η⁻¹H, K = η⁻¹ω with I² = −1, J² = K² = +1, IJ = K: Freidel–Leigh–Minic's Born geometry, para-Hermitian geometry, and how ρ acts on the triple (it preserves ω and H and flips η)."
provenance: [T, D]
sources:
  - "papers/broken-born-checkpoint-v2.md §5"
  - "papers/broken-born-checkpoint-v2.md ref [3]"
  - "papers/broken-born-checkpoint-v2.md §4"
  - "papers/broken-born-checkpoint-v2.md §6"
  - "notes/broken-born-theory.md §1"
  - "notes/broken-born-theory.md §2"
  - "notes/broken-born-program-v1.md §3"
  - "notes/geometric-core.md §A"
  - "notes/geometric-core.md §B"
  - "notes/geometric-core.md §F"
  - "notes/tuning-test.md §1"
  - "notes/tuning-test.md §2"
  - "papers/reciprocity-toy-models.md §1"
  - "papers/reciprocity-toy-models.md §2"
  - "papers/reciprocity-toy-models.md §5"
  - "papers/reciprocity-toy-models.md ref [1]"
  - "papers/reciprocity-toy-models.md ref [3]"
  - "review/round3/referee/audit-notes.md Step 1"
  - "review/round3/referee/audit-notes.md Step 3"
  - "review/round4/referee/audit-notes.md Step 1"
  - "notes/toy-lagrangian.md 'Chunk 1 results'"
  - "verify/battery.py T1"
  - "verify/toy_s5.py A"
---

*Born geometry equips phase space, the space of positions and momenta taken together, with three structures: the [symplectic form](/wiki/phase-space/reciprocity/symplectic-form) ω, the antisymmetric pairing behind the quantum commutator; a neutral metric η, a symmetric pairing with as many positive as negative directions, whose null directions mark out which coordinates count as position and which as momentum; and a positive generalized metric H, a ruler that measures lengths in phase space. Combined in pairs, the three give operators I, J and K that multiply like the split quaternions: I squares to −1, J and K square to +1, and IJ = K. Freidel, Leigh and Minic named phase spaces carrying such a compatible triple Born geometries. The quarter-turn [ρ](/wiki/phase-space/reciprocity/born-reciprocity), which [the Fourier transform](/wiki/phase-space/reciprocity/fourier-transform) implements, preserves ω and H in their standard forms and reverses the sign of η. Under the program's corrected postulate η is the order parameter of the breaking, so ρ changes the order parameter's sign.*

**Status:** Established — the structures and their algebra are literature [T] (Freidel–Leigh–Minic; #11 ref. [3]†, not yet checked against the source); the action of ρ on the triple is derived here [D] (#1 §2) — battery test T1 checks J² = 1 and I² = −1 on one sampled compatible metric at d = 4 ([the battery](/wiki/method/verification/battery)), and the battery does not test the rest of the algebra; the d = 1 analogue of ρ's action, K → −K, is checked by the toy-model script `verify/toy_s5.py` ([the toy-model scripts](/wiki/method/verification/toy-model-scripts)).

## Phase space and its three structures

The arena is flat phase space 𝒫 ≅ ℝ^{2d} with coordinates (xᵃ, pₐ); the lab notebook ([#1](/wiki/history/documents/lab-notebook) §2) works at d = 4, with "units chosen so a reference length λ and momentum ε = ℏ/λ are scaled out" ([the Born length λ](/wiki/phase-space/reciprocity/born-length)). A bilinear form assigns a number to each pair of phase-space vectors. Three of them carry the geometry, and in the (x, p) block basis their standard forms are (#1 §2):

```text
ω = [[0, 1], [−1, 0]]      antisymmetric       the symplectic form
η = [[0, 1], [1, 0]]       symmetric, neutral   the neutral metric
H = [[1, 0], [0, 1]]       symmetric, positive  the generalized metric
```

Each entry is a d × d block. In words [T]:

- **ω** pairs each position component with its own momentum component, antisymmetrically. It measures oriented area in each (xᵃ, pₐ) plane, it is the classical counterpart of the [canonical commutator](/wiki/phase-space/reciprocity/canonical-commutator) [x, p] = iℏ, and the linear maps that preserve it form the symplectic group Sp(2d, ℝ) ([the symplectic form](/wiki/phase-space/reciprocity/symplectic-form)). The program reads its rigidity as the constancy of ℏ (#11 §4).
- **η** also pairs each position component with its momentum component, but symmetrically. It is "a neutral (split-signature) metric" (#1 §1, P1): d of its directions have positive length and d negative. In the standard form a vector of pure position, or of pure momentum, has zero η-length, so the position subspace and the momentum subspace are both null. This is the sense in which η marks out the split into position and momentum.
- **H** is positive definite, an ordinary ruler on phase space that measures position and momentum together. It is the structure that carries the geometry's dynamics: under [the original P2](/wiki/program/postulates/original-p2) "only H carries degrees of freedom" (#1 §1), and under [P2′](/wiki/program/postulates/p2-prime) it is fundamental together with ω (#5 §B).

The three are not independent. The conditions that tie H to the other two, (η⁻¹H)² = +1 and (ω⁻¹H)² = −1, are what calc note [#5](/wiki/history/documents/field-equation-notes) §A calls "the full Born algebra"; which H satisfy both is the subject of [the compatibility theorem](/wiki/phase-space/born-geometry/compatibility-theorem).

## The operators I, J, K and the split-quaternion algebra

Composing one form with the inverse of another gives a linear map of phase space to itself [T]. Checkpoint [#11](/wiki/history/documents/checkpoint) §5 defines three such maps and states their products:

```text
I = ω⁻¹H        J = η⁻¹H        K = η⁻¹ω

I² = −1         J² = K² = +1        IJ = K
```

"With ω, η standard", these satisfy the relations above, "a split-quaternion algebra (Born geometry [3†]; a unique compatible connection exists [7†])" (#11 §5). The lab notebook obtains the same relations by direct matrix computation with all three structures in standard form, and calls the result "a split-quaternion (para-quaternionic) algebra" (#1 §2).

What the relations mean [T]:

- **I² = −1.** Applying I twice reverses every vector, as multiplying by i twice does. I is a *complex structure*: it makes phase space a complex vector space. The notebook's postulate P3 calls it "the complex structure I" (#1 §1).
- **J² = +1.** J is an involution. Its +1 and −1 eigenspaces split phase space into two halves, which makes it a *real* (or para-complex) structure. Calc note #5 §B describes the J the vacuum selects as "a real structure J (an involution anticommuting with I)". In the vacuum frame of [the tuning test](/wiki/gravity/tuning-test) it is J₀ = [[0, 1], [1, 0]] (calc note #7 §2).
- **K² = +1 and IJ = K.** The identity and I, J, K span a four-dimensional algebra in which one generator squares to −1 and two square to +1: the split quaternions, also called coquaternions or para-quaternions. In Hamilton's quaternions all three generators square to −1; in both algebras the generators anticommute in pairs [T].

The relations J² = 1 and I² = −1 are conditions on H, since ω and η are held in standard form. They say that H is compatible with η and with ω respectively; [the compatibility theorem](/wiki/phase-space/born-geometry/compatibility-theorem) finds that the positive H satisfying both are exactly H = diag(g, g⁻¹). Battery test T1 checks the two relations on one randomly drawn metric of that form at d = 4, and the run prints `PASS  T1a diag(g,g^-1) satisfies (eta^-1 H)^2=1 and (omega^-1 H)^2=-1` (`verify/battery.py`; [the battery](/wiki/method/verification/battery)). The battery has no test of K² = 1 or IJ = K.

## Born geometry in the literature

The name is Freidel, Leigh and Minic's. The lab notebook: "A compatible triple (ω, η, H) realizing this algebra is precisely a Born geometry in the sense of Freidel, Leigh & Minic. [T]" (#1 §2). The v1 program paper repeats the attribution as "Born geometry in the sense of Freidel–Leigh–Minic [T]" (#9 §3), and #11 §5 cites it as ref. [3]†.

The [round-3](/wiki/method/review/round-3) referee located the term in the metastring paper, arXiv:1502.08005, p. 11, and quoted it (audit notes, Step 1):

```text
"If, in addition, we assume that B vanishes we have that I is a complex
structure and that JK = -KJ. Phase space geometries that have I,J,K
satisfying these conditions were referred to as Born geometries"
```

The condition "B vanishes" is the content of the compatibility theorem: the referee summarizes the theorem as "B-field vanishes <=> I = H^-1 omega compatible" (audit notes, Step 3). The referee writes FLM's complex structure as I = H⁻¹ω (FLM is Freidel–Leigh–Minic); this wiki follows #11's I = ω⁻¹H ([conflicts between sources](/wiki/history/documents/source-conflicts)).

In Freidel, Leigh and Minic's own work η is dynamical rather than fixed. The [round-4](/wiki/method/review/round-4) referee found "we have to make eta dynamical" in arXiv:1405.3949, and the toy-model worklog quotes arXiv:1307.7080: "both elements (η, J) of the chiral structure are dynamical. The solutions are labelled by bi-Lagrangians and spacetime is a derived dynamical concept" [S] (worklog, 'Chunk 1 results'). #11 §4 credits that literature for the point: "That η should be dynamical rather than fixed was argued independently in metastring theory [26S]; the reading of η as the order parameter of broken reciprocity is this program's." The history of the idea is on [broken Born duality](/wiki/phase-space/reciprocity/broken-born-duality).

References, with the marks the documents give them:

- #11 [3]† L. Freidel, R. G. Leigh, D. Minic, "Born reciprocity in string theory and the nature of spacetime," Phys. Lett. B 730, 302 (2014); "Quantum gravity, dynamical phase space and string theory," Int. J. Mod. Phys. D 23, 1442006 (2014). The [toy-model note](/wiki/symmetry-breaking/toy-models) lists the same two papers as its ref. [1], parts (a), arXiv:1307.7080, and (b), arXiv:1405.3949, retrieved during the project.
- #11 [26][S] L. Freidel, R. G. Leigh, D. Minic, "Metastring theory and modular space-time," JHEP 06 (2015) 006, arXiv:1502.08005 (the toy-model note's ref. [1], part (c)).

**Para-Hermitian geometry.** A real structure whose two eigenspaces are null for a neutral metric is the setting of para-Hermitian geometry, the mathematics of a doubled space split into two halves [T]. Calc note #5 points to this literature for an open question about the structure P2′ keeps, ω and H without a fixed η: whether a compatible connection is still unique there, for which "the para-Hermitian literature — Svoboda, Marotta–Szabo — is the nearest neighbor" (#5 §F; [the Born connection](/wiki/phase-space/born-geometry/born-connection)). The toy-model note cites V. E. Marotta, R. J. Szabo, "Born sigma-models for para-Hermitian manifolds and generalized T-duality," Rev. Math. Phys. 33, 2150031 (2021), arXiv:1910.09997 (ref. [3]), in which "Born sigma models choose the polarization by gauging" (toy-model note §1). The round-4 referee describes them as "sigma models of Born geometry (polarization as target structure, not a field)".

## How ρ acts on the triple [D]

The Born rotation ρ: (x, p) → (p, −x) acts on phase-space vectors by the matrix R = [[0, 1], [−1, 0]] (#1 §2), the same matrix as ω's standard form; the toy-model note states that ρ "is symplectic and squares to −1" (§1). The lab notebook's result, tagged [D]: "One checks directly: R preserves ω (it is symplectic), preserves H (it is orthogonal), and flips the sign of η, hence flips J and K while preserving I." (#1 §2).

The reason is visible in the standard forms. R turns each (xᵃ, pₐ) plane by a quarter turn. A rotation preserves oriented area, so it preserves ω, and it preserves lengths measured by H = 1. It exchanges the position and momentum axes and reverses the direction of one of them. The exchange alone reverses the sign of the antisymmetric ω and leaves the symmetric pairing η of position with momentum unchanged; the reversal alone reverses the sign of both. Together they leave ω unchanged and reverse the sign of η. J and K each contain η once, so both change sign; I = ω⁻¹H contains no η and is unchanged.

The statement "preserves H" refers to the standard H = 1. On a general ω-compatible metric H_Z, ρ acts as the modular inversion Z → −Z⁻¹, which at X = 0 is the [scale-factor duality](/wiki/cosmology/scale-factor-duality) g → g⁻¹ (#11 §6, an identification tagged [D] with a d = 1 check; [reciprocity as modular inversion](/wiki/phase-space/modular-field/modular-inversion)).

What the result was taken to mean changed with the postulates:

- **v0.1.** "The order parameter of the theory is J = η⁻¹H — equivalently, the choice of which Lagrangian splitting H aligns with. Reciprocity is broken iff ⟨J⟩ ≠ 0 in the vacuum." (#1 §2.)
- **P2′.** With η emergent, "the earlier observation that reciprocity flips η now reads correctly as the broken symmetry moving the order parameter" (#5 §B; [P2′](/wiki/program/postulates/p2-prime)).

The square ρ²: (x, p) → (−x, −p) preserves all three structures, and the notebook derived from this a discrete breaking pattern ℤ₄ → ℤ₂ = {1, ρ²} [D] (#1 §2). That pattern assumed a rigid η. Since #11 v2.2 the polarization is a Goldstone angle instead: "with only ω rigid, ρ sits inside a continuous U(1), and the polarization is a Goldstone angle rather than a discrete choice [D][V]" (#11 §4). The old pattern and its fate are recorded on [the order parameter](/wiki/symmetry-breaking/order-parameter); the current picture is [the polarization as a Goldstone angle](/wiki/symmetry-breaking/goldstone-angle).

In the one-dimensional toy model the corresponding statement for K is machine-checked: `PASS  rho maps K to -K, and maps L+ onto L- (rho^-1 e+ is a K-eigenvector with eigenvalue -1)` (`verify/toy_s5.py`, part A). The toy-model note writes the same action as K(φ) → K(φ + π) = −K(φ) (§2).

## η's null lines and the choice of polarization

The toy-model note builds η from ω and a real structure K: "A real structure K with K² = 1 and Kᵀ ω K = −ω defines a neutral metric η = ωK. Its null lines are the two eigenlines L± of K, which are Lagrangian. Choosing K is choosing which line is "position"." (§1). A Lagrangian subspace is one of maximal dimension on which ω vanishes; choosing one as the position coordinates is choosing a polarization ([Lagrangian subspaces and polarizations](/wiki/phase-space/reciprocity/lagrangian-polarizations)).

Two facts fix what η determines (toy-model note §5): "The null lines of η = ωK(φ) are exactly K's eigenlines L±, and the only ones", and "K → −K sends η → −η with the same null lines. ρ exchanges L+ and L−." The S5 script checks each piece at d = 1 (`verify/toy_s5.py`, part A). One of its lines carries a caveat: `PASS  L+ and L- are Lagrangian (w vanishes on each line trivially in d = 1) and transverse: w(e+, e-) != 0`. Every line is Lagrangian when d = 1, so the Lagrangian property is automatic there. What η's null lines imply for matter fields is on [the section condition](/wiki/symmetry-breaking/section-condition).

The choices of K form a manifold. At H = 1 the toy model's compatible real structures, which are its vacua, form the circle K(φ) = [[cos φ, sin φ], [sin φ, −cos φ]] (toy-model note §2), whose angle parametrizes the Lagrangian Grassmannian Λ(1). In general dimension, under P2′, "The space of H-compatible real structures on (ℝ^{2d}, I) is {J} ≅ U(d)/O(d) = Λ(d)" (#5 §B; [the Lagrangian Grassmannian](/wiki/phase-space/modular-field/lagrangian-grassmannian)).

The Fourier picture is literal here. A state's position description and its momentum description are related as a waveform and its spectrum, the two null lines of η are the position line and the momentum line, and ρ, which the Fourier transform implements, exchanges them.

## Which operator is "the real structure" (unreconciled)

The documents give the name to different operators, and none reconciles the two conventions:

```text
#11 P2′ (§4):                        η = HJ    "the real structure J"
toy-model note §1; #11 §14 item 11:  η = ωK    K the real structure, K² = 1
```

#11 §5 defines both J = η⁻¹H and K = η⁻¹ω, and the lab notebook calls J = η⁻¹H the order parameter. This page uses #11 §5's definitions. [The order parameter](/wiki/symmetry-breaking/order-parameter) records both conventions and the history of the order parameter's notation.

## How the program uses the structures

- **The arena.** P1: "Physics on phase space with symplectic form ω and positive generalized metric H. [P]" (#11 §4). The notebook's P1 listed all three structures, "a symplectic form ω, a neutral (split-signature) metric η, and a positive generalized metric H, mutually compatible" (#1 §1). See [P1: the phase-space arena](/wiki/program/postulates/p1-arena).
- **Which structures are rigid.** The original P2 fixed both ω and η ([original P2](/wiki/program/postulates/original-p2)); the compatibility theorem and its corollaries showed that this leaves the program no content of its own (#5 §B), and P2′ keeps only ω rigid, with η = HJ emergent (#11 §4; [P2′](/wiki/program/postulates/p2-prime)). Calc note #5 §B: "the fundamental pair is (ω, H); the derived complex structure is I = ω⁻¹H; the vacuum spontaneously selects a real structure J (an involution anticommuting with I), and η ≡ HJ."
- **The symmetry.** P3: "The action is invariant under the Born rotation generated by I = ω⁻¹H. [P]" (#11 §4; [P3](/wiki/program/postulates/p3-reciprocity)).
- **The misalignment measure.** The tuning test penalizes a mismatch between the vacuum's J and the [modular field](/wiki/phase-space/modular-field/modular-field-z)'s complex structure I[Z]: "The natural incompatibility measure is the anticommutator {J, I[Z]} (zero exactly on the compatible locus)" (#7 §1; on what that locus contains, see flag 3 in `review/wiki-build-flags.md`; [the misalignment potential](/wiki/gravity/tuning-test/misalignment-potential)).
- **Differentiation.** A unique connection compatible with all three structures exists ([the Born connection](/wiki/phase-space/born-geometry/born-connection)).

## Used by

- [The hard core: spontaneously broken Born reciprocity](/wiki/program/hard-core) — ω rigid, η emergent.
- [P1: the phase-space arena](/wiki/program/postulates/p1-arena) — physics on phase space with ω and a positive generalized metric H.
- [P2′: only the symplectic form is rigid](/wiki/program/postulates/p2-prime) — η = HJ emergent, J chosen by the vacuum.
- [P3: a reciprocity-invariant action](/wiki/program/postulates/p3-reciprocity) — the Born rotation generated by I = ω⁻¹H.
- [The nontriviality theorem](/wiki/program/postulates/nontriviality-theorem) — the three structures and their algebra are its starting point.
- [The modular field Z = X + iY](/wiki/phase-space/modular-field/modular-field-z) and [reciprocity as modular inversion](/wiki/phase-space/modular-field/modular-inversion) — the triple with only ω kept rigid, and ρ's action on it.
- [The order parameter: J, η and K](/wiki/symmetry-breaking/order-parameter) — η, J and K as the quantities ρ moves.
- [The section condition: what η fixes](/wiki/symmetry-breaking/section-condition) — η's null lines as the candidate sections.
- [Model I: action and symmetries](/wiki/symmetry-breaking/toy-models/coset-model/action-and-symmetries) — η = ωK as a neutral metric whose null lines are L±.
- [The misalignment potential](/wiki/gravity/tuning-test/misalignment-potential) — the anticommutator of J with I[Z] measures misalignment.
- [The metric tier fails twice](/wiki/gravity/tuning-test/metric-tier-failures) — an invariant built from K = η⁻¹ω gives X a mass without the trace term.
- [The symplectic partner of the graviton is another graviton](/wiki/gravity/momentum-graviton/symplectic-partner) — the two pairings η and ω and the partners they give the metric.
- [The velocity gate](/wiki/dark-matter/conjugate-matter/velocity-gate), [the gate mechanism](/wiki/dark-matter/conjugate-matter/gate-mechanism) and [dual stress T̃](/wiki/dark-matter/conjugate-matter/dual-stress) — conjugate matter couples universally to the generalized metric H.
- [The cosmological constraint a·ã = 1](/wiki/cosmology/scale-factor-duality/cosmological-constraint) — first derived under the postulate that froze ω and η.
- [Two causal cones](/wiki/conjugate-relativity/two-causal-cones) — #13 reads its cones off the block form of H (see flag 30 in `review/wiki-build-flags.md`).

## Sources

- `papers/broken-born-checkpoint-v2.md` §5 and ref. [3] — the definitions, the algebra and its attribution.
- `papers/broken-born-checkpoint-v2.md` §4 — P1, P2′ and P3 in terms of ω, H, J and I; the metastring credit; the Goldstone-angle refinement.
- `papers/broken-born-checkpoint-v2.md` §6 — ρ as Z → −Z⁻¹ and g → g⁻¹ at X = 0.
- `papers/reciprocity-toy-models.md` §1, §2, §5 and refs. [1], [3] — K as the real structure, η = ωK, its null lines, the circle K(φ), Marotta–Szabo.
- `review/round3/referee/audit-notes.md` Step 1, Step 3 — the Born-geometry passage in arXiv:1502.08005 and the referee's I = H⁻¹ω.
- `review/round4/referee/audit-notes.md` Step 1 — "we have to make eta dynamical"; Born sigma models.
- `notes/geometric-core.md` §A, §B, §F — "the full Born algebra"; ρ moving the order parameter; {J} ≅ Λ(d); the para-Hermitian neighbour.
- `notes/tuning-test.md` §1, §2 — the incompatibility measure {J, I[Z]}; J₀ in the vacuum frame.
- `notes/toy-lagrangian.md` 'Chunk 1 results' — Freidel–Leigh–Minic on (η, J) as dynamical [S].
- `notes/broken-born-theory.md` §1, §2 — the standard forms, the algebra tagged [T], ρ's action on the triple [D], the v0.1 order parameter and the ℤ₄ → ℤ₂ pattern.
- `notes/broken-born-program-v1.md` §3 — the same algebra as "Born geometry in the sense of Freidel–Leigh–Minic [T]".
- `verify/battery.py` T1 — J² = 1 and I² = −1 on one sampled H = diag(g, g⁻¹).
- `verify/toy_s5.py` part A — η = ωK, its null lines, and ρ mapping K to −K at d = 1.
