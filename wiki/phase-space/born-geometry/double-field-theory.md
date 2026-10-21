---
title: "Double field theory and the generalized metric"
weight: 20
status: established
description: "String theory's doubled geometry: the O(d, d) generalized metric with its Kalb–Ramond B-field, and the section (strong) condition with its derivations — the contrast case for the program."
provenance: [T]
sources:
  - "papers/reciprocity-toy-models.md §1"
  - "papers/reciprocity-toy-models.md §5"
  - "papers/reciprocity-toy-models.md ref [11]"
  - "papers/reciprocity-toy-models.md ref [12]"
  - "notes/toy-lagrangian.md 'Chunk 4 (in progress, 2026-10-19): S5'"
  - "notes/toy-lagrangian.md 'Chunk 1 results'"
  - "review/round4-adjudication.md 'Rulings'"
  - "review/round4/referee/audit-notes.md Step 1"
  - "papers/broken-born-checkpoint-v2.md §5"
  - "papers/broken-born-checkpoint-v2.md §7.1"
  - "notes/debt1a-geometric-core.md §A"
  - "notes/debt1a-geometric-core.md §D"
  - "notes/debt1a-ii-X-classification.md §2"
  - "notes/broken-born-theory.md §1"
  - "notes/broken-born-theory.md §2"
  - "review/round3/referee/audit-notes.md Step 3"
  - "review/round3/referee/step3.py family (c)"
---

*Double field theory is a formulation of the low-energy fields of closed string theory (the metric, the antisymmetric Kalb–Ramond B-field and the dilaton) on a doubled space, in which each ordinary coordinate has a partner "dual" coordinate. Its central object, the generalized metric, packages the metric and the B-field into one matrix that preserves a neutral metric η, and its symmetry group O(d, d) is the group of transformations that preserve η. For the theory to be consistent, fields may depend on only half of the doubled coordinates: the section, or strong, condition. The known derivations of that condition leave open which half, and no mechanism that selects one is known. For the program, double field theory is the contrast case. Doubling geometry with η gives the metric an antisymmetric partner, the B-field; doubling it with the [symplectic form](/wiki/phase-space/reciprocity/symplectic-form) ω gives it a symmetric partner, a second graviton; and holding ω rigid as well as η removes the B-field altogether.*

**Status:** Established — literature [T]; the citations were retrieved by live search during the project [S] (the toy-model worklog, chunk 4; the toy-model note lists the same works unmarked) — not machine-checked as physics; round 3 checked numerically that generalized metrics with a B-field satisfy the η condition and fail the ω condition. A mechanism that selects one section is open, in the literature as in the program.

## The doubled space [T]

A closed string on a circle carries two kinds of conserved charge: momentum around the circle and the number of times it winds around it. T-duality exchanges the two and relates a circle to one of inverse radius in string units. Double field theory makes this symmetry manifest by giving each coordinate xⁱ a dual coordinate x̃ᵢ, conjugate to winding, and writing the massless closed-string fields as fields on the 2d-dimensional doubled space. The theory under this name is Hull and Zwiebach's (the toy-model note's ref. [11]).

The doubled space carries a neutral metric, the pairing of each coordinate with its dual. In the basis (x, x̃) it has the standard form [[0, 1], [1, 0]], the same form as the program's η ([the structures ω, η, H](/wiki/phase-space/born-geometry/born-structures)). The linear maps that preserve it form O(d, d). This group contains the T-duality transformations, the ordinary changes of coordinates and the constant shifts of the B-field [T].

## The generalized metric [T]

The generalized metric H combines the metric g and the antisymmetric B-field into one symmetric 2d × 2d matrix. In the program's block basis, the round-3 referee's script writes this family as (`review/round3/referee/step3.py`, family (c), B antisymmetric):

```text
H = [[ g − B g⁻¹ B ,  B g⁻¹ ],
     [ −g⁻¹ B      ,  g⁻¹   ]]
```

At B = 0 it reduces to diag(g, g⁻¹). The generalized metric is itself an element of O(d, d). For a symmetric H this is the statement (η⁻¹H)² = 1, the first of the two conditions in [the compatibility theorem](/wiki/phase-space/born-geometry/compatibility-theorem) [T].

The B-field is a 2-form gauge field: its gauge symmetry is δB = dλ, and calc note [#6](/wiki/history/documents/debt-1-notes) §2 calls it "a 2-form gauge theory — spin-wise harmless". With the dilaton, the metric and the B-field make up double field theory's massless sector, and that sector propagates without ghosts. Calc note #5 §D cites it ("graviton + B-field + dilaton, ghost-free") as evidence that "doubled-geometry kinetic operators can be healthy [T]".

## The section condition [T]

Fields on the doubled space cannot depend on all 2d coordinates. Closure of the theory's gauge transformations requires a constraint built from η:

- the **weak constraint**: η^{AB}∂_A∂_B annihilates every field and gauge parameter. On a torus it is the closed string's level-matching condition, and Hull and Zwiebach's 2009 paper uses it (round-4 referee, Step 1);
- the **strong constraint**, or section condition: η^{AB}∂_A∂_B also annihilates every product of fields. Hohm, Hull and Zwiebach show it is "equivalent to restriction ... to a maximally isotropic subspace" (quoted by the round-4 referee).

A maximally isotropic subspace has dimension d, the largest possible, and η vanishes on it. A section is such a subspace: all fields depend only on its coordinates. The standard choice, fields independent of x̃, gives back the ordinary metric, B-field and dilaton of string theory's low-energy limit [T]. In the toy-model note's notation for d = 1 the condition reads (§5):

```text
η^{AB} ∂_A f ∂_B g = 0,     η^{AB} ∂_A ∂_B f = 0
```

How many sections there are depends on the dimension. In d = 1 the doubled space is a plane with exactly two null lines, so there are two sections. For d > 1 there is a continuous family: the round-4 referee found that the maximal isotropic subspaces "split into two classes", each an SO(D, D) orbit, a continuum, citing a footnote of Hohm, Hull and Zwiebach. The worklog adds that "All sections are O(D,D)-equivalent."

## Where the condition comes from

The literature gives three routes (toy-model note §1; worklog chunk 4, "all citations retrieved [S]"):

- **Imposed** for closure of the gauge algebra (Hull–Zwiebach; Hohm–Hull–Zwiebach).
- **Derived from string consistency.** Betz, Blumenhagen, Lüst and Rennecke derive it "from modular invariance plus amplitude poles" (worklog); the round-4 referee confirmed the derivation from conformal field theory, "factorization of Virasoro-Shapiro amplitude".
- **Derived from worldsheet locality** in Freidel, Leigh and Minic's metastring paper, arXiv:1502.08005 §6 (worklog).

None of the derivations picks out one section. The toy-model note (v2, §1): "Those derivations leave the section undetermined within a family — a pair for d = 1, a continuous family for d > 1." Betz et al. find "w = 0 for M = 1 and p = 0 for M = −1" (worklog), where M is an O(d) matrix.

The wording has a correction history. The worklog first wrote "Every derivation selects only the pair {L, L̃}". The round-4 referee judged the claim overstated, and the adjudication upheld the finding "'Every derivation selects the pair' holds only for d = 1", with the evidence "For d > 1, Betz–Blumenhagen–Lüst–Rennecke's M ∈ O(d) gives a continuous family of sections." Version 2 of the note restricts the pair to d = 1 ([review round 4](/wiki/method/review/round-4)).

## Open: a mechanism that selects one section

That the choice of section is made dynamically has been said only in words (worklog chunk 4):

- Freidel, Rudolph and Svoboda (arXiv:1706.07089): the choice "might be subject to a dynamical selection rule". The round-4 referee found the phrase verbatim, with "the kinematical structure of spacetime itself" as its subject, and judged the paraphrase acceptable.
- Freidel, Leigh and Minic (arXiv:1502.08005): "a dynamical question".
- Bernardo, Brandenberger and Franzmann (arXiv:1901.01209), "whose support is a personal communication".
- Freidel, Leigh and Minic's linearized □_η H = 0 (arXiv:1405.3949) "is the weak constraint, and is solved along either null line".

The worklog's verdict: "Open: a mechanism that picks L over L̃. Each candidate in the literature either selects the pair only, or uses outside input: which modes are light, distance-dependent interactions, or a curved position space."

The program meets the same gap. Its toy section condition, built from the vacuum's η, "confines matter to one null line without telling the two apart" (toy-model note §5; [the section condition](/wiki/symmetry-breaking/section-condition)), and the stronger claim that locality is forced rather than chosen is "not achieved" (worklog, S5 conclusion). In the toy, matter's section is tied to the sign of the vacuum's real structure K only through a K-covariant coupling, and "The lock is P4" ([Open: forced locality and the P4 lock](/wiki/symmetry-breaking/strong-locality); [open problems](/wiki/status/open-problems)).

## Double field theory as the program's contrast case

**The partner's spin.** Calc note #6 §2 sets the two doublings side by side. Doubling with ω makes the partner of the metric the symmetric tensor X, whose dual diffeomorphisms δX_μν = ∂₍μλ_ν₎ are a second copy of linearized diffeomorphisms; in double field theory "there the doubled partner is the antisymmetric B-field, δB = dλ, a 2-form gauge theory — spin-wise harmless. The symmetry type of the rigid structure — η antisymmetric-pairing vs ω — dictates the symmetry type of the partner field. This is the structural reason string theory's η-doubling exists and naive ω-doubling is hard: the symplectic partner of the graviton is another graviton." (#6 §2; η itself is a symmetric pairing, #1 §1, and the phrase is quoted as #6 writes it.) Checkpoint [#11](/wiki/history/documents/checkpoint) §7.1 keeps the contrast: X is symmetric, "contrast [double field theory's] antisymmetric B-field: the symmetry type of the rigid pairing dictates the partner's spin". See [the symplectic partner of the graviton](/wiki/gravity/momentum-graviton/symplectic-partner) and [dual diffeomorphisms](/wiki/gravity/momentum-graviton/dual-diffeomorphisms).

**No B-field once ω is rigid too.** Generalized metrics built from a metric and a B-field satisfy the η condition, and satisfy the ω condition only when the B-field vanishes. #11 §5, crediting Freidel, Leigh and Minic: "writing the η-compatible H in terms of (G, B), H is related to ω through a complex structure exactly when B vanishes [26S, §2.1]." Calc note #5 §A states the same as corollary 2 of the compatibility theorem: "The off-diagonal block — [double field theory's] B-field — is frozen out by the extra symplectic compatibility. Born geometry with both structures rigid is *stiffer* than [double field theory]." Round 3 checked the family numerically at d = 3 and 4: "eta residual <= 7e-14 but omega residual >= 0.28 (d=3), 1.48 (d=4)" (audit notes, Step 3; [the corollaries](/wiki/phase-space/born-geometry/compatibility-corollaries)).

**A healthy precedent.** Double field theory's ghost-free massless sector is the program's evidence that a doubled geometry can have healthy kinetic terms (#5 §D), cited where the field content of the broken vacuum is still open ([Open: field content of the broken vacuum](/wiki/phase-space/modular-field/field-content)).

**The section condition, borrowed.** The lab notebook's geometric action used the same device: "Field dependence is restricted to a Lagrangian leaf by a section condition, as in double field theory; consistency of the section condition on general backgrounds is open there and open here. [O]" (#1 §2). That item left the program's open-problem list unresolved; [the section condition](/wiki/symmetry-breaking/section-condition) records its fate and the toy-model version.

**Broken O(D, D).** The worklog's prior-art survey lists double field theory with spontaneously broken O(D, D) (Angus, Kim and Park, arXiv:2111.07947) as related but not the same: "there H is the order parameter, with η fixed" [S] (worklog, 'Chunk 1 results'). In the program η itself is the order parameter ([broken Born duality](/wiki/phase-space/reciprocity/broken-born-duality)).

## References

As the documents give them; the toy-model note's list is unmarked, and the worklog marks every entry [S]:

- C. Hull, B. Zwiebach, "Double field theory," JHEP 09 (2009) 099, arXiv:0904.4664; O. Hohm, C. Hull, B. Zwiebach, "Background independent action for double field theory," JHEP 07 (2010) 016, arXiv:1003.5027 (toy-model note ref. [11]).
- A. Betz, R. Blumenhagen, D. Lüst, F. Rennecke, "A note on the [conformal field theory] origin of the strong constraint of [double field theory]," JHEP 05 (2014) 044, arXiv:1402.1686 (toy-model note ref. [12]).
- Reviews arXiv:1305.1907, arXiv:1306.2643 and arXiv:1309.2977 [S] (worklog only).
- L. Freidel, R. G. Leigh, D. Minic, "Metastring theory and modular space-time," JHEP 06 (2015) 006, arXiv:1502.08005 (#11 ref. [26][S]).
- L. Freidel, F. J. Rudolph, D. Svoboda, "Generalised kinematics for double field theory," JHEP 11 (2017) 175, arXiv:1706.07089 (toy-model note ref. [2]).
- Bernardo, Brandenberger and Franzmann, arXiv:1901.01209; Angus, Kim and Park, arXiv:2111.07947 [S] (worklog only).

## Used by

- [The section condition: what η fixes](/wiki/symmetry-breaking/section-condition) — the toy version of the condition, built from the vacuum's η.
- [The symplectic partner of the graviton is another graviton](/wiki/gravity/momentum-graviton/symplectic-partner) — the contrast between η-doubling and ω-doubling.
- [Open: field content of the broken vacuum](/wiki/phase-space/modular-field/field-content) — the precedent for healthy doubled kinetic terms.
- [Open: forced locality and the P4 lock](/wiki/symmetry-breaking/strong-locality) — no known mechanism picks one section.

## Sources

- `papers/reciprocity-toy-models.md` §1, §5 and refs. [11], [12] — the section condition, its derivations, the d = 1 pair and the d > 1 family; the toy condition built from η.
- `notes/toy-lagrangian.md` chunk 4 (S5) — the live-searched literature on deriving and selecting the section; 'Chunk 1 results' — broken O(D, D) with H as order parameter.
- `review/round4-adjudication.md` "Rulings" — the "pair" restricted to d = 1.
- `review/round4/referee/audit-notes.md` Step 1 — weak and strong constraints in the cited papers; the continuous family; the Freidel–Rudolph–Svoboda quotation.
- `papers/broken-born-checkpoint-v2.md` §5, §7.1 — the Freidel–Leigh–Minic statement in terms of (G, B); the partner's spin.
- `notes/debt1a-geometric-core.md` §A, §D — corollary 2 (no Kalb–Ramond analog); the healthy precedent.
- `notes/debt1a-ii-X-classification.md` §2 — the B-field as a spin-harmless partner.
- `notes/broken-born-theory.md` §1, §2 — η as a symmetric neutral metric; the v0.1 section condition, "open there and open here".
- `review/round3/referee/audit-notes.md` Step 3 and `review/round3/referee/step3.py` family (c) — the generalized metric with a B-field, checked numerically.
