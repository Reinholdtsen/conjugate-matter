---
title: "The section condition: what η fixes"
weight: 90
status: alive
description: "η's null lines are K's eigenlines; a section condition built from η confines matter to one of them but cannot tell which (a clean pair only for d = 1); the lab notebook's original section condition and its curved-background question."
provenance: [V]
sources:
  - "papers/reciprocity-toy-models.md §5"
  - "papers/reciprocity-toy-models.md §1"
  - "papers/reciprocity-toy-models.md §2"
  - "papers/reciprocity-toy-models.md §6"
  - "papers/reciprocity-toy-models.md Abstract"
  - "notes/toy-lagrangian.md 'Chunk 3 results (2026-10-19): S4, quantum stability'"
  - "notes/toy-lagrangian.md 'Chunk 4 (in progress, 2026-10-19): S5'"
  - "verify/toy_s5.py parts A–B"
  - "review/round4/referee/audit-notes.md Step 1"
  - "review/round4/referee/audit-notes.md Step 2(d)"
  - "review/round4/referee/audit-notes.md Step 3"
  - "review/round4/referee/out_sec5.txt"
  - "review/round4-adjudication.md 'Rulings' (the double-field-theory 'pair')"
  - "review/round4-adjudication.md 'Pre-registration scored'"
  - "review/round4-adjudication.md 'Revisions' 5"
  - "notes/broken-born-theory.md §2"
  - "notes/broken-born-theory.md §3"
  - "notes/broken-born-theory.md §11 item 1"
  - "papers/broken-born-checkpoint-v2.md §14"
  - "notes/closed-universe.md §5"
---

*A section condition is a rule, taken from double field theory, that makes every field depend on only half of a doubled set of coordinates, so that physics lives on one "section" of the doubled space. In the program's coset toy model the [neutral metric](/wiki/phase-space/born-geometry/born-structures) η, the order parameter of broken reciprocity, singles out exactly two lines in the position–momentum plane: its null lines, which are the two eigenlines of the real structure K. A section condition built from η forces each matter field to depend on the coordinate along one of those lines only. It cannot say which of the two is position, because the same fields pass whether the condition is built from η or from −η. So the condition fixes the pair of candidate directions, and matter's choice within the pair has to come from somewhere else. The clean two-way choice holds only when phase space is a plane (one position and one momentum coordinate); with more dimensions the literature finds a continuous family of sections.*

**Status:** Alive, for d = 1 — [V] (the worklog's parts A and B; `verify/toy_s5.py`, [the toy-model scripts](/wiki/method/verification/toy-model-scripts)) — the section condition itself is literature [T] and is imposed, not derived, in the toy; the lab notebook's question about curved backgrounds stays open [O] and is not tracked in [#11](/wiki/history/documents/checkpoint) §14.

## What a section condition is

[Double field theory](/wiki/phase-space/born-geometry/double-field-theory) writes the low-energy fields of closed string theory on a doubled space, in which each coordinate has a dual partner, and equips that space with a neutral metric η, a symmetric pairing with as many positive as negative directions [T]. Consistency does not allow fields to depend on all the doubled coordinates. The [toy-model note](/wiki/symmetry-breaking/toy-models) (`papers/reciprocity-toy-models.md`, version 2; "toy note" below) summarizes the literature:

> The section condition confines fields to a maximally isotropic subspace. It is imposed for closure of the gauge algebra [11], or derived from string consistency [12]. Those derivations leave the section undetermined within a family — a pair for d = 1, a continuous family for d > 1. (toy note §1)

A maximally isotropic subspace is one of the largest dimension on which η vanishes; with d coordinates and d dual coordinates it has dimension d [T]. Here d counts position coordinates, so d = 1 means that phase space is the plane ℝ², and the maximally isotropic subspaces are lines: the null lines of η. Reference [11] is Hull–Zwiebach and Hohm–Hull–Zwiebach, [12] Betz, Blumenhagen, Lüst and Rennecke. How the literature derives the condition, and why no derivation picks out one section, is set out on the double-field-theory page.

## The toy setting

The program applies the device to phase space, with η the vacuum's [order parameter](/wiki/symmetry-breaking/order-parameter). In the toy (toy note §1):

> Phase space ℝ² with symplectic form ω = [[0, 1], [−1, 0]]. … A real structure K with K² = 1 and Kᵀ ω K = −ω defines a neutral metric η = ωK. Its null lines are the two eigenlines L± of K, which are Lagrangian. Choosing K is choosing which line is "position".

L+ is the eigenline of K with eigenvalue +1 and L− the one with eigenvalue −1. In [model I](/wiki/symmetry-breaking/toy-models/coset-model) the vacua at metric H = 1 are the real structures K(φ) = [[cos φ, sin φ], [sin φ, −cos φ]] (toy note §2), so the pair of lines turns with the [polarization angle](/wiki/symmetry-breaking/goldstone-angle) φ. In the vacuum K₀ = diag(1, −1), the point φ = 0, L+ is the x-axis and L− the p-axis. See [the order parameter](/wiki/symmetry-breaking/order-parameter) and [Lagrangian subspaces and polarizations](/wiki/phase-space/reciprocity/lagrangian-polarizations).

## What η fixes [V]

The note's statement (toy note §5; worklog part A [V]):

> - The null lines of η = ωK(φ) are exactly K's eigenlines L±, and the only ones.
> - K → −K sends η → −η with the same null lines. ρ exchanges L+ and L−.

[The gate](/wiki/method/verification/the-gate) checks it in steps (`verify/toy_s5.py`, part A), and the [round-4](/wiki/method/review/round-4) referee checked it independently (`review/round4/referee/audit-notes.md`, Step 2(d); "audit notes" below):

1. **η is a neutral metric.** "eta = w K is a symmetric neutral metric (det = -1)": a symmetric pairing with one positive and one negative direction.
2. **K's eigenvectors are null.** The script takes e+ = (cos φ/2, sin φ/2) and e− = (−sin φ/2, cos φ/2), with K e+ = e+ and K e− = −e−, and checks "e+ and e- are null for eta, for every phi". The reason is one line of algebra [T]: for an eigenvector, eᵀηe = eᵀωKe = ±eᵀωe, which vanishes because ω is antisymmetric.
3. **There are no other null lines.** The gate checks "they are the only null lines: eta(e+, e-) != 0": since e+ and e− are null and η pairs them nonzero, a combination of the two is null only if one coefficient vanishes [T]. The referee evaluated η on the unit vector at every angle t: "v(t)^T eta v(t) = sin(phi - 2t): zeros exactly at t = phi/2, phi/2+pi/2", the directions of e+ and e− (audit notes, Step 2(d)).
4. **The lines are Lagrangian and transverse.** In the plane ω vanishes on any single line, so both lines are Lagrangian trivially, and "w(e+, e-) != 0" (gate).
5. **K → −K keeps the lines.** "K -> -K sends eta -> -eta, with the same null lines" (gate): a vector is null for −η exactly when it is null for η.
6. **ρ exchanges them.** "rho maps K to -K, and maps L+ onto L- (rho^-1 e+ is a K-eigenvector with eigenvalue -1)" (gate); the referee: "rho^-1 e+ is parallel to e-".

So the null lines of η fix the unordered pair {L+, L−} and nothing more. Which line is L+, the eigenvalue +1 line that counts as position, is carried by the sign of K. Reversing that sign leaves η's null lines where they are and exchanges the labels; [Born reciprocity](/wiki/phase-space/reciprocity/born-reciprocity) ρ has the same effect, since it sends K to −K.

## The condition built from η [V]

For d = 1 the toy imposes on matter fields f and g the conditions (toy note §5):

```text
η^{AB} ∂_A f ∂_B g = 0,        η^{AB} ∂_A ∂_B f = 0
```

Here A and B run over the two phase-space coordinates and η^{AB} is the inverse of η. The first condition applies to every pair of fields, a field paired with itself included; the second to every field. They are the toy's form of double field theory's strong constraint, which asks that the wave operator η^{AB}∂_A∂_B annihilate products of fields as well as the fields themselves [T] ([double field theory](/wiki/phase-space/born-geometry/double-field-theory)).

**Null coordinates.** The computation becomes transparent in coordinates along the two null lines. Write a phase-space point as ξ = u e+ + v e− (the script's "xi = u e+ + v e-"), so u runs along L+ and v along L−. Because e+ and e− are null, η has no diagonal entries in this basis, and neither does its inverse: "in null coordinates eta^-1 is purely off-diagonal (box = c d_u d_v)" (gate), where c is a nonzero constant. The pairing of two gradients therefore always combines a u-derivative of one field with a v-derivative of the other. Then (worklog part B [V]; gate; audit notes, Step 2(d)):

- **Fields on one null line pass.** If f = F(u) and g = G(u), every v-derivative vanishes and both conditions hold. The same is true of fields that depend on v alone.
- **Mixed fields fail.** "Mixing the two lines fails: η(dF(u), dG(v)) = −F′G′." (worklog). The gate prints the pairing as "-Derivative(F(u), u)*Derivative(G(v), v)".
- **A field spread over both lines fails against itself.** F(u) + G(v) satisfies the second condition, since ∂_u∂_v of it vanishes, but its pairing with itself is "-2*Derivative(F(u), u)*Derivative(G(w), w)", with "box = 0" (`review/round4/referee/out_sec5.txt`, which names the second null coordinate w). The worklog: "So does F(u) + G(v) paired with itself."
- **Building the condition from −η changes nothing.** "With −η the pairing only changes sign" (worklog), so exactly the same fields pass and fail. The gate's check: "with -eta the pairing only changes sign, so the same fields pass and fail: it cannot tell L+ from L-".

The worklog's conclusion of part B: "**The section condition selects the unordered pair {L+, L−} and cannot tell position from momentum.**" The note: "So consistency confines matter to one null line without telling the two apart." (toy note §5). Its abstract adds the dimension: a section condition built from η "confines matter fields to one of η's two null lines (for d = 1) without telling them apart."

The information the condition carries is the same as that of the axis pair in the toy's ρ-preserving potential. When the worklog planned this step, it wrote that η and −η have the same null lines, "so the section condition is blind to the sign of K: it selects the unordered pair {L, L̃}, the same information as K_ref" ('Chunk 3 results', plan for S5), K_ref being the reference real structure of that potential, which fixes the pair up to sign ([Open: the origin of the ρ-preserving potential](/wiki/symmetry-breaking/rho-preserving-potential)).

## Imposed, not derived

In the literature the condition is imposed for the closure of gauge transformations, or derived from string consistency [T] (toy note §1). The toy imposes it. The round-4 referee listed the note's wording among its over-reaches in the matter section: "(iii) 'consistency confines matter' -- the section condition is imposed, not derived, in this paper." (audit notes, Step 3). The adjudication did not rule on this point and its revisions do not mention it, and version 2 keeps the sentence "So consistency confines matter to one null line without telling the two apart" (§5). The sources leave the wording unreconciled ([conflicts between sources](/wiki/history/documents/source-conflicts#gravity-and-symmetry-breaking)).

Whether a section can be selected dynamically is open in the literature as well. The worklog's live-searched survey [S] files the dynamical choice of a section under "Claimed only in words", and records as open "a mechanism that picks L over L̃" ('Chunk 4', 'S5 literature'). Its findings are on [the double-field-theory page](/wiki/phase-space/born-geometry/double-field-theory) and at [Open: forced locality and the P4 lock](/wiki/symmetry-breaking/strong-locality).

## Only for d = 1

The toy's phase space is the plane, d = 1, and there the section condition leaves exactly two choices, the two null lines. With more coordinates it does not: "For d > 1 the analogous statement leaves a continuous family of sections [12]." (toy note §5).

The round-4 referee read the derivation in [12], the paper of Betz, Blumenhagen, Lüst and Rennecke (cited as [8] in the version under review): "k_R = M k_L, M in O(d) -- a continuous family for d>=2; only for d=1, O(1)={+-1}, giving w=0 or p=0 (a pair)". So "'every derivation selects the pair' is true only in d=1, where it is just the statement that R^{1,1} has two null lines" (audit notes, Step 1). The referee also cites a footnote of Hohm, Hull and Zwiebach: the maximal isotropic subspaces "split into two classes", each an orbit of SO(D,D), a continuum. The adjudication upheld the finding, "'Every derivation selects the pair' holds only for d = 1", with the evidence "For d > 1, Betz–Blumenhagen–Lüst–Rennecke's M ∈ O(d) gives a continuous family of sections." Its scoring of the [pre-registered](/wiki/method/review/pre-registration) citation forecast lists the same reference as over-cited: "also [8] (d = 1 only)" (`review/round4-adjudication.md`; [review round 4](/wiki/method/review/round-4)).

The [V] results on this page therefore hold for d = 1. The toy-model note lists "anything beyond d = 1" among what it does not show (§6).

## Superseded: every derivation selects the pair

Before round 4 the statement carried no dimension restriction. The worklog's literature summary reads "**Every derivation selects only the pair {L, L̃}.**" ('Chunk 4', 'S5 literature'), and the version of the note sent to review said that the toy agrees with the double-field-theory literature, "where every derivation selects the pair [8]" (quoted by the referee, audit notes, Step 3, as an over-reach). The round-4 ruling above restricted it to d = 1, and revision 5 asked version 2 to "restrict the section 'pair' to d = 1". Version 2 does so in §1 and §5. The change is listed at [Superseded statements](/wiki/status/superseded).

## What η leaves to the coupling

The section condition fixes the pair of lines, not the member. In the toy, which member is position is the sign of K, the order parameter of the [spontaneously broken](/wiki/symmetry-breaking/spontaneous-symmetry-breaking) ρ, and matter's line is tied to that sign only by a coupling that can tell K from −K. The worklog's conclusion on locality: "matter's section is locked to K's sign only through the K-covariant coupling. Without that lock, matter's choice of section and K's sign are independent orders." ('Chunk 4', S5 conclusion). The coupling, which version 2 describes as built from H and K, is at [Locality from an (H, K)-built coupling](/wiki/symmetry-breaking/matter-coupling); why such a coupling is also what gives the breaking of ρ physical content is at [the twisted element](/wiki/symmetry-breaking/twisted-element); and the question of what forces matter to use it is [Open: forced locality and the P4 lock](/wiki/symmetry-breaking/strong-locality).

## Open: the section condition on curved backgrounds

[The lab notebook](/wiki/history/documents/lab-notebook) (#1, v0.1) had already borrowed the device for the program's geometric action. Its kinematic core: "Field dependence is restricted to a Lagrangian leaf by a section condition, as in double field theory; consistency of the section condition on general backgrounds is open there and open here. **[O]**" (#1 §2). The action it served is S_H = ½M_B² ∫_Σ √|H| R_B[H], built from the curvature of [the Born connection](/wiki/phase-space/born-geometry/born-connection) and integrated "over the section Σ, with ω,η frozen (P2)" (#1 §3; [the v0.1 action, superseded](/wiki/gravity/tuning-test/geometric-action)). The notebook's list of open problems kept the question under its first item, the field equation for H: "The action exists (Born connection **[T]**), but solutions, the section condition on curved backgrounds, and the full ghost analysis do not. **[O]**" (#1 §11, item 1).

The question has not been settled. It is not among the open problems of #11 §14, and no document before 2026-10-27 takes it up: it left the program's list of open problems without being resolved. The closed-universe note bears on one curved background, a closed universe, without settling the question: on its phase space T\*S³ only the position polarization is integrable, so if the section condition requires integrability, the mirror vacuum of P5 has no global realization there; the record does not state that requirement, and if polarizations that are not integrable are allowed, the mirror's energy cost is not computed [O] (`notes/closed-universe.md` §5, a result of the note's critic alone; [reciprocity on a closed space](/wiki/phase-space/reciprocity/closed-space-reciprocity)). The toy work, which uses flat phase space ℝ², does not reach it. It is registered at [Open problems and the queue](/wiki/status/open-problems); the notebook's record is at [the lab notebook](/wiki/history/documents/lab-notebook).

## Sources

- `papers/reciprocity-toy-models.md` §5 — what η fixes; the section condition, its behaviour in null coordinates, and the d > 1 family; §1 — η = ωK and its Lagrangian null lines, and the double-field-theory prior work; §2 — the vacua K(φ); Abstract, §6 — "for d = 1" and "anything beyond d = 1" not shown
- `notes/toy-lagrangian.md` 'Chunk 4' — parts A and B [V], "cannot tell position from momentum", the section-selection literature [S] and the K-covariant lock; 'Chunk 3 results' — the plan for S5 and "the same information as K_ref"
- `verify/toy_s5.py` parts A and B — the gated checks quoted above
- `review/round4/referee/audit-notes.md` Step 2(d) — the independent check of the null lines and the section condition; Step 1 — the reading of [12] and Hohm–Hull–Zwiebach, the pair only for d = 1; Step 3 — "imposed, not derived" and the v1 "pair" wording
- `review/round4/referee/out_sec5.txt` — the referee's printed pairings
- `review/round4-adjudication.md` 'Rulings' (the double-field-theory "pair"), 'Pre-registration scored', 'Revisions' 5 — the "pair" restricted to d = 1
- `notes/broken-born-theory.md` §2, §3, §11 item 1 — the v0.1 section condition, the action over the section, and the curved-background question [O]
- `papers/broken-born-checkpoint-v2.md` §14 — the current open problems, which do not include the curved-background question
- `notes/closed-universe.md` §5 — integrability of the polarizations on T\*S³ and its bearing on the section condition; the critic's result alone, not reviewed
