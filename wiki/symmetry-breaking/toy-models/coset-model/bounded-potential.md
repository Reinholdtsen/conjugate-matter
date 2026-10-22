---
title: "The bounded potential V_b"
weight: 50
status: alive
description: "The normalized form −μ[Tr(K K_ref)]²/(2 Tr KᵀK) is bounded by Cauchy–Schwarz, keeps ρ and the flip, and leaves the vacuum stable with H dynamical (Hessian 0, 0.764, 2, 5.236); its zero mode is not symmetry-protected, and its origin is not derived."
provenance: [D, V]
sources:
  - "papers/reciprocity-toy-models.md §4"
  - "papers/reciprocity-toy-models.md §6"
  - "papers/broken-born-checkpoint-v2.md §4"
  - "papers/broken-born-checkpoint-v2.md §10"
  - "papers/broken-born-checkpoint-v2.md §14 item 11"
  - "verify/toy_coset.py"
  - "verify/toy_s4.py"
  - "review/round4-adjudication.md 'Rulings' F2"
  - "review/round4-adjudication.md 'Revisions' 1"
  - "review/round4/adjudicator/arb.out"
  - "review/round4/referee/audit-notes.md Step 3"
  - "review/round4/referee/out_fix_potential.txt"
  - "review/round4/referee/ref_fix_potential.py"
  - "CLAUDE.md 'Since the handoff'"
---

*V_b is the repaired ρ-preserving potential of [model I](/wiki/symmetry-breaking/toy-models/coset-model): the [naive potential](/wiki/symmetry-breaking/toy-models/coset-model/naive-potential) divided by a normalizing factor, 2 Tr KᵀK, which keeps it between −μ and 0 for every real structure K. Like the naive form it is unchanged by [Born reciprocity](/wiki/phase-space/reciprocity/born-reciprocity) ρ and by the flip K → −K, and it reduces the circle of real structures to the pair ±K_ref. Unlike the naive form, it leaves the vacuum a stable minimum when the metric H is free to vary: the boosted configurations along which the naive form fell without limit now cost energy. The round-4 referee proposed it, version 2 of the toy-model note adopted it, and checkpoint #11 records [acceptance criterion 1](/wiki/symmetry-breaking/toy-models/acceptance-criterion) as met with it, in the referees' wording. One flat direction remains that no symmetry protects, and where such a potential comes from is not derived.*

**Status:** Alive; the potential itself is put in by hand, not derived — [D][V] ([#11](/wiki/history/documents/checkpoint) §10 tags its toy-model paragraph, which states the boundedness requirement, [D][V]) — boundedness, stability with H dynamical and the zero mode are checked in `verify/toy_coset.py` ([the toy-model scripts](/wiki/method/verification/toy-model-scripts)); upheld in [review round 4](/wiki/method/review/round-4) as "the repair". Its origin is [open](/wiki/symmetry-breaking/rho-preserving-potential).

## Definition

Version 2 of the [toy-model note](/wiki/symmetry-breaking/toy-models): "The normalized form V_b = −μ[Tr(K K_ref)]² / (2 Tr KᵀK) is bounded, −μ ≤ V_b ≤ 0 by Cauchy–Schwarz, since Tr K_refᵀK_ref = 2." (§4).

```text
V_b = −μ [Tr(K K_ref)]² / (2 Tr KᵀK),        K_ref = diag(1, −1)

−μ ≤ V_b ≤ 0
```

The numerator is the naive potential −μ[Tr(K K_ref)]². The denominator measures the size of K: Tr KᵀK is the sum of the squares of K's four entries [T]. μ sets the depth, and K_ref is the reference structure whose eigenlines are the x- and p-axes.

On the circle of vacua at H = 1, where K = K(φ), the potential depends on the polarization angle φ only through cos 2φ: "At H = 1, V_b = −(μ/2)(1 + cos 2φ)." (§4; [the gate](/wiki/method/verification/the-gate) passes "at H = 1, V_b(K(phi)) = -(1 + cos 2 phi)/2" at μ = 1, `verify/toy_coset.py`). The naive form there is −2μ(1 + cos 2φ). Both are lowest at φ = 0 and φ = π, the structures +K_ref and −K_ref, and at H = 1 they differ only in their overall factor ([model I vacua](/wiki/symmetry-breaking/toy-models/coset-model/vacua)).

## Why it is bounded

The bound is the Cauchy–Schwarz inequality for matrices [T]. Read a 2 × 2 matrix as a vector of its four entries; then Tr(AᵀB) is the dot product of A and B, and Tr AᵀA is the squared length of A. Because K_ref is symmetric, Tr(K K_ref) is the dot product of K and K_ref. The square of a dot product is at most the product of the squared lengths. The gate's own comment gives the step:

```text
[Tr(K K_ref)]²  ≤  Tr(KᵀK) · Tr(K_refᵀK_ref)  =  2 Tr(KᵀK),     so V_b ≥ −1   (μ = 1)
```

The upper bound needs nothing: V_b is minus a square divided by a positive number. Equality in Cauchy–Schwarz needs K to be a multiple of K_ref [T], which on K's hyperboloid means K = ±K_ref, so the floor −μ is reached exactly there.

Both bounds are also checked by sampling. The gate draws 20,000 points of the hyperboloid a² + bc = 1 and passes "sampled V_b stays in [-1, 0] on the hyperboloid", printing the lowest value −0.9770 (`verify/toy_coset.py`). The referee's larger sample: "min V'/mu = -0.99999913, max = -1.26e-05 over 141227 hyperboloid samples" (`review/round4/referee/audit-notes.md`, Step 3; `out_fix_potential.txt`).

## Symmetries

"It is ρ- and flip-invariant." (§4). The gate passes "V_b is rho-invariant" and "V_b is invariant under K -> -K"; the referee's samples gave "max |V'(rho K) - V'(K)| = 2.2e-16", zero to machine precision. The reason [T]: ρ is a rotation, so conjugating K by it leaves Tr KᵀK unchanged, and it only reverses the sign of Tr(K K_ref), which the square removes. The flip reverses the same sign and leaves the denominator alone.

What V_b does not keep matters as much. The naive form is invariant under a larger set of maps, which contains the stretches diag(a, 1/a) of the x- and p-axes, called squeezes in this wiki, and, among the rotations, ±1 and ±ρ ([the obituary](/wiki/symmetry-breaking/toy-models/coset-model/naive-potential#the-residual-symmetry)). The normalization changes that. The referee: "it uses the Euclidean Tr(K^T K), which breaks the residual boosts explicitly; the vacuum analysis with H dynamical would have to be redone." (Step 3, point C3). The referee's "residual boosts" are those squeezes (on the referee's two uses of the word boost, see flag 10 in `review/wiki-build-flags.md`). Tr KᵀK is the ordinary squared length of K's entries, and conjugating K by a map that is not a rotation can change it [T]. Version 2 states the result: "V_b breaks the squeeze away from K = ±K_ref" (§4).

## Stability with H dynamical

The redone analysis, at λ = μ = 1 in the coordinates of `verify/toy_coset.py`: "With H dynamical, (1, K_ref) is a stable minimum: Hessian eigenvalues 0, 0.764, 2, 5.236." (§4). The Hessian is the matrix of second derivatives of the full potential, compatibility term included, at the vacuum, with all four field directions free. No eigenvalue is negative, so the energy does not decrease in any direction away from the vacuum. The gate prints [−0., 0.7639, 2., 5.2361] and passes "with V_b, (1, K_ref) is stable: Hessian eigenvalues >= 0 with exactly one zero"; the adjudicator's run gives the same list (`review/round4/adjudicator/arb.out`). At the same point and in the same coordinates the naive form has the eigenvalue −6.47 ([the obituary](/wiki/symmetry-breaking/toy-models/coset-model/naive-potential#f2-the-intended-vacuum-is-a-saddle)).

Along the boost family on which the naive form fell without limit, V_b now rises. The family is H = SᵀS, K = S⁻¹K₀S with S(t) = [[cosh t, sinh t], [sinh t, cosh t]]:

- the referee's closed form: "V'(t)/mu = -1/2 - 1/(2*cosh(4*t)) ; t->oo limit: -1/2" (`out_fix_potential.txt`);
- the adjudicator: −1.0000, −0.5183, −0.5003 and −0.5000 at t = 0, 1, 2, 4 (`arb.out`);
- the gate: [−1, −0.6329, −0.5183, −0.5] at t = 0, 0.5, 1, 3, passing "boosts are penalized: V_b rises from -1 toward -1/2 along the boost family".

The adjudication's summary: "the boost family rises from −1 to −0.5" ('Rulings' F2). The normalization grows with K's entries as fast as the numerator does, so the ratio stays finite along the family, and the direction in which the naive form decreased is one in which V_b increases.

## The vacuum manifold and the zero mode

"Vacuum manifold: {diag(y, 1/y)} × {±K_ref}." (§4). The real structure is fixed up to sign, and the metric can still move along the line of diagonal metrics diag(y, 1/y), y > 0.

That line is the direction of the Hessian's one zero eigenvalue. Version 2: "The zero mode is the classical flat line H = diag(y, 1/y), K = K_ref. It is not symmetry-protected, because V_b breaks the squeeze away from K = ±K_ref. Boosts are penalized." (§4). The gate passes "the zero mode is the squeeze line H = diag(y, 1/y), K = K_ref: V = -1 all along it".

The squeeze S = diag(a, 1/a) carries the vacuum (1, K_ref) to (diag(a², 1/a²), K_ref), so the zero-mode line is the squeeze orbit of the vacuum [T]. The kinetic and compatibility terms are invariant under the squeeze; V_b is unchanged by it on the line, where K = K_ref, but not off the line. The line is therefore flat, but no symmetry of the full action keeps it flat. A flat direction enforced by a symmetry stays flat when quantum corrections are added; a flat direction that holds only classically has no such guarantee [T]. The note claims no more than "not symmetry-protected".

**The sources disagree here.** The adjudication's ruling on F2 called the zero mode "the residual diagonal squeeze, which is an exact symmetry", and its revision 1 asked for a "local minimum up to the exact residual squeeze". Version 2 says the opposite, "not symmetry-protected", and ranks above the adjudication in the wiki's source precedence, so this page follows version 2 ([conflicts between the documents](/wiki/history/documents/source-conflicts#postulates-and-the-toy-models); flag 12 in `review/wiki-build-flags.md`). Checkpoint #11 says only that "the vacuum is stable with H dynamical" (§14 item 11) and does not mention the zero mode.

## Where it came from

The round-4 referee proposed V_b during its conceptual audit, while reporting that the naive form ran away (Step 3, point C3):

> A bounded variant exists: V' = -mu[Tr(K K_ref)]^2/(2 Tr(K^T K)) gives min V'/mu = -0.99999913, max = -1.26e-05 over 141227 hyperboloid samples, max |V'(rho K) - V'(K)| = 2.2e-16, and on the runaway family V'/mu = -1/2 - 1/(2 cosh 4t) -> -1/2. But it uses the Euclidean Tr(K^T K), which breaks the residual boosts explicitly; the vacuum analysis with H dynamical would have to be redone.

The referee's script calls it a "candidate fix only" (`review/round4/referee/ref_fix_potential.py`). The adjudicator redid the Hessian with H dynamical and ruled: "The referee's bounded variant −μ[Tr(K K_ref)]²/(2Tr KᵀK) gives eigenvalues [0, 0.764, 2, 5.236]. ... **This is the repair.**" ('Rulings' F2). Revision 1 told version 2 to "Use the bounded potential. Show it is stable with H dynamical", and version 2, applied on 2026-10-20 in commit 6606734, adopted it; the gate's block "The bounded rho-preserving potential, with H dynamical (round-4 repair)" checks it.

## What rests on it

- **Acceptance criterion 1.** #11 §14 item 11: "Met in the referees' wording by the coset model of (H, K) with a bounded ρ-preserving potential", including "the vacuum is stable with H dynamical".
- **The cosmology's consistency claim.** #11 §10, "Toy-model support (v2.2) [D][V]": "A definite polarization requires the ρ-preserving potential this section posits. That potential must be bounded with all fields dynamical — the round-4 review found the naive form unbounded once H moves" ([τ as the Maslov phase](/wiki/phase-space/modular-field/maslov-phase)).
- **The refinement of P2′.** #11 §4: "A definite polarization needs a ρ-preserving potential on that angle — a rigid, unordered pair of axes, so more structure than ω alone, though less than a rigid η." ([P2′](/wiki/program/postulates/p2-prime)).
- **The lattice result.** The Monte Carlo simulates "model I's polarization angle at H = 1, with V_b up to a constant and normalization. H is not simulated." (§4; [the frozen-H reduction](/wiki/symmetry-breaking/toy-models/coset-model/frozen-h-reduction); [Monte Carlo: an ordered ℤ₂ phase](/wiki/symmetry-breaking/toy-models/coset-model/monte-carlo)). `verify/toy_s4.py` notes that its energy −h cos 2φ "equals the bounded V_b at H = 1 up to a constant and a factor".

## Open: where the potential comes from

V_b is put in, not derived. Version 2 lists among what is "Not shown": "a derivation of the ρ-preserving potential, which introduces a rigid, unordered pair of axes" (§6). #11 §14 item 11 keeps "a derivation of the potential" open [O], and the root `CLAUDE.md` names "a derivation of the ρ-preserving potential" among the toy work's open ends ('Since the handoff').

What it puts in by hand is K_ref up to sign: an unordered pair of axes. The referee's reading of what is left to the vacuum: "the potential fixes the unordered axis pair by hand, so the vacuum chooses only which of two pre-set axes is 'position'" (Step 3). The normalization 2 Tr KᵀK was chosen to make the potential bounded; the sources give it no other motivation. The question is treated in full at [Open: the origin of the ρ-preserving potential](/wiki/symmetry-breaking/rho-preserving-potential) and registered at [open problems](/wiki/status/open-problems).

## Sources

- `papers/reciprocity-toy-models.md` §4, §6 — the definition, bound, symmetries, Hessian, zero mode, vacuum manifold and H = 1 form, quoted above; the underived potential listed as not shown
- `papers/broken-born-checkpoint-v2.md` §4, §10, §14 item 11 — P2′'s price, the boundedness requirement [D][V], and the criterion met with V_b
- `verify/toy_coset.py` — the gated bound, invariances, stability, zero-mode and boost checks, and the Cauchy–Schwarz comment
- `verify/toy_s4.py` — the lattice energy as V_b at H = 1
- `review/round4-adjudication.md` 'Rulings' F2, 'Revisions' 1 — "This is the repair"; the boost-family summary; the adjudicator's reading of the zero mode
- `review/round4/adjudicator/arb.out` — the adjudicator's Hessian and boost-family values
- `review/round4/referee/audit-notes.md` Step 3 — the referee's proposal and its caveat about the residual boosts; the axis pair fixed by hand
- `review/round4/referee/out_fix_potential.txt`, `review/round4/referee/ref_fix_potential.py` — the referee's sampled bounds, invariance and closed form on the runaway family
- `CLAUDE.md` 'Since the handoff' — the derivation listed as an open end
