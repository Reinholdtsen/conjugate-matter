---
title: "Coset and hyperbolic sigma models"
weight: 10
status: established
description: "Fields valued in a curved target space; coset targets G/H and their Goldstone directions; why an indefinite target metric (de Sitter dS₂) means a ghost; and why non-compact hyperbolic models, unlike compact ones, can break symmetry in two dimensions."
provenance: [T]
sources:
  - "papers/reciprocity-toy-models.md §1"
  - "papers/reciprocity-toy-models.md §2"
  - "papers/reciprocity-toy-models.md §4"
  - "papers/reciprocity-toy-models.md refs [3], [13]–[15]"
  - "review/round4/referee/audit-notes.md Step 1"
  - "review/round4/referee/audit-notes.md Step 2(a)"
  - "review/round4/referee/audit-notes.md Step 2(c)"
  - "review/round4/referee/audit-notes.md Step 3"
  - "review/round4/referee/out_model1.txt"
  - "review/round4-adjudication.md 'Rulings'"
  - "notes/toy-lagrangian.md 'Success criteria'"
  - "notes/toy-lagrangian.md 'Chunk 1 results'"
  - "notes/toy-lagrangian.md 'Assessment against the predictions'"
  - "verify/toy_coset.py"
---

*A sigma model is a field theory whose field takes values, at each point of spacetime, in a curved space called the target, such as a circle, a sphere or a hyperbolic plane; the action charges a cost whenever neighbouring points take distant values in the target. In a coset sigma model the target is a group divided by a subgroup, so the group acts on the target as a symmetry and every constant field is a lowest-energy state. Two results from this literature shape [model I](/wiki/symmetry-breaking/toy-models/coset-model), the program's coset model of phase-space structures. The target's metric must be positive, or the kinetic term carries a ghost, a mode of negative energy. And in two dimensions a compact continuous symmetry cannot break spontaneously, while the non-compact symmetry of a hyperbolic target can.*

**Status:** Established — literature [T]; the hyperbolic-model citations were retrieved [S] in the worklog's prior-art survey and checked against the sources in round 4, which corrected an author's initial (A. Duncan) and added an erratum.

## What a sigma model is

A sigma model has one field n(x) that maps each point x of the base, the spacetime on which the theory lives, to a point of a target manifold M [T]. The target carries a metric g, which measures how far apart two of its points are. The Euclidean action charges for variation of the field from point to point:

```text
S[n] = (f²/2) ∫ d^D x  g_ab(n) ∂_μ n^a ∂_μ n^b
```

Here D is the dimension of the base, the n^a are coordinates on the target, and f sets the stiffness [T]. The model is nonlinear because the target is curved: the field cannot be rescaled freely, only moved within M. With no potential, any constant field has zero action, so every point of the target is a vacuum [T].

Three examples fix the idea [T]:

- **The circle.** n is an angle φ and the action is (f²/2) ∫ (∂φ)². This is the continuum form of the XY model of statistical mechanics, a lattice of planar spins. The frozen-H form of model I is of this kind ([the frozen-H reduction](/wiki/symmetry-breaking/toy-models/coset-model/frozen-h-reduction)).
- **The sphere.** n is a unit vector in ℝ^N, the O(N) model; for N = 3 it is the long-wavelength theory of a Heisenberg magnet.
- **The hyperbolic plane.** The target is a surface of constant negative curvature, the non-compact counterpart of the sphere (below).

The name comes from the σ field of Gell-Mann and Lévy's 1960 model of pions (†).

## Coset targets

Many targets are homogeneous: a group G moves any point of M to any other [T]. Fix one point and let G₀ ⊂ G be the subgroup that leaves it in place, its stabilizer. Each point of M then corresponds to a group element taken up to the stabilizer, and M is the coset space G/G₀ [T]. The sphere S² is SO(3)/SO(2), and the upper half-plane is SL(2, ℝ)/SO(2), since the rotations are the maps that fix the point i ([the Siegel domain](/wiki/phase-space/modular-field/siegel-domain)). If the target metric is unchanged by G, the action is too, and G is a symmetry of the model [T].

A constant field picks one point of the target and is left unchanged only by that point's stabilizer, so a vacuum breaks G down to the stabilizer ([spontaneous symmetry breaking](/wiki/symmetry-breaking/spontaneous-symmetry-breaking)). Moving the vacuum along the target costs nothing, so the target directions are flat: there are dim G − dim G₀ [Goldstone directions](/wiki/symmetry-breaking/goldstone-and-higgs) [T].

Model I is built this way. The worklog calls it "a coset model of Sp(2,R) → Z₂" (`notes/toy-lagrangian.md`, 'Chunk 1 results'). Its metric field H takes values in "Sp(2)/U(1) (the upper half-plane, H = H(Z), Z = X + iY)" (`verify/toy_coset.py`), and its real structure K, the field that marks which line of the phase plane is position, takes values in the one-sheeted hyperboloid a² + bc = 1 ([toy-model note](/wiki/symmetry-breaking/toy-models) §2; [Model I: action and symmetries](/wiki/symmetry-breaking/toy-models/coset-model/action-and-symmetries)). Its vacuum is left fixed only by ±1, so the whole three-dimensional group is broken and there are three flat directions ([Model I vacua](/wiki/symmetry-breaking/toy-models/coset-model/vacua)). The round-4 referee's novelty search judged that "Model I appears new as a field theory, but it is a simple coset", whose vacuum manifold is the group divided by {±1} (`review/round4/referee/audit-notes.md`, Step 3).

## Positive target metrics, and the de Sitter ghost

The kinetic term in each target direction carries the sign of the target metric in that direction [T]. A positive-definite metric makes every way of varying the field cost action. An indefinite metric gives some direction a kinetic term of the wrong sign. In real time that mode carries negative energy, or negative norm once quantized: it is a ghost, and the theory is sick. In Euclidean signature the same defect makes the action unbounded below [T].

Two-dimensional de Sitter space, dS₂, is a target of this second kind [T]. As a surface it is the one-sheeted hyperboloid in a three-dimensional space with one negative direction, and its natural metric has one positive and one negative direction. That is what makes it a spacetime; as a target space it means a ghost.

Model I meets this through K. Version 2 of the toy-model note: "K, traceless with det K = −1. Its target is the one-sheeted hyperboloid a² + bc = 1, which is two-dimensional de Sitter space" (§2). The worklog: "K's own target space (de Sitter dS₂) has an indefinite metric, which would give a ghost" ('Chunk 1 results'). The naive kinetic term Tr(∂K ∂K) is that indefinite metric. At K₀ = diag(1, −1) it is "2 db dc" (note §2; confirmed by the referee's sympy run, `review/round4/referee/out_model1.txt`), which is positive when db and dc have the same sign and negative when they differ.

A picture shows why the metric field is healthy where K is not [T]. Sp(2, ℝ) acts on both fields by conjugation (on K directly, and on H through I = ω⁻¹H), and both K and I are traceless 2 × 2 matrices. On that three-dimensional space the trace form Tr(XY) is an invariant inner product with two positive directions and one negative. The condition I² = −1 cuts out a two-sheeted hyperboloid, on which the form is positive: each sheet is a hyperbolic plane. The condition K² = 1 cuts out the one-sheeted hyperboloid, on which the form is indefinite: de Sitter space. So one group and one invariant form give the metric a target on which the kinetic term is positive, and the real structure one on which it is indefinite.

Model I avoids the ghost by contracting K's kinetic term with H, Tr(H⁻¹ ∂Kᵀ H ∂K), which "is positive definite" (note §2). The referee found it equal to "db**2 + dc**2" at H = 1, and positive on random samples (`out_model1.txt`); the gate checks the same positivity on random H and ∂K (`verify/toy_coset.py`). The price is that K's kinetic term now depends on H, so the two sectors of the model are coupled ([Model I: action and symmetries](/wiki/symmetry-breaking/toy-models/coset-model/action-and-symmetries#the-k-kinetic-term-and-the-ghost)).

## Two dimensions: compact symmetries do not break

"Continuous compact symmetries cannot break spontaneously in two dimensions [13, 14]" (toy-model note §1). The references are Mermin and Wagner (1966) and Coleman (1973): [the Mermin–Wagner–Coleman theorem](/wiki/symmetry-breaking/mermin-wagner-coleman) [T]. In two dimensions the long-wavelength fluctuations of a would-be Goldstone mode grow without limit, because the integral ∫ d²k/k² over their wavenumbers diverges logarithmically at small k, and they wash out any order in a compact direction [T]. For the circle model this shows up as an order parameter that decays slowly, as a power of the system size, instead of approaching a constant. The [Monte Carlo of model I's frozen-H reduction](/wiki/symmetry-breaking/toy-models/coset-model/monte-carlo) sees that decay in its run without a potential.

Discrete symmetries are not covered: "In 1+1, a discrete symmetry can break (as in the 2D Ising model). A continuous compact one cannot (Coleman–Mermin–Wagner)" (worklog, 'Success criteria', criterion S4). Model I's lattice result uses exactly this: a potential reduces the compact angle's symmetry to a discrete one, which then orders.

## Hyperbolic sigma models: the non-compact exception

"Non-compact hyperbolic models are an exception [15]" (toy-model note §1). A hyperbolic sigma model takes as target the hyperbolic space SO(1, N)/SO(N), which is one sheet of a two-sheeted hyperboloid with the positive metric described above, and whose symmetry group SO(1, N) is non-compact [T]. Reference [15] is two papers: M. Niedermaier and E. Seiler, Ann. Henri Poincaré 6, 1025 (2005), hep-th/0312293; and A. Duncan, M. Niedermaier and E. Seiler, "Vacuum orbit and spontaneous symmetry breaking in hyperbolic sigma models", Nucl. Phys. B 720, 235 (2005), with an erratum in Nucl. Phys. B 758, 330 (2006), hep-th/0405163.

The second paper's abstract, as the round-4 referee retrieved it: "(ii) the SO(1,N) symmetry is spontaneously broken. For D=2 this shows that the systems evade the Mermin-Wagner theorem." (`review/round4/referee/audit-notes.md`, Step 1). The worklog's summary of the same pair: "SO(1,N) broken in D ≥ 2, evading Mermin–Wagner" ('Chunk 1 results', citations retrieved [S]).

The program's documents give the result by citation only, not its mechanism. The worklog first framed the exception as one for "non-amenable groups" ('Success criteria'). A group is amenable when an invariant average over it exists [T]. Compact groups and abelian groups are amenable; Sp(2, ℝ) and SO(1, N) with N ≥ 2 are not [T]. The referee kept that framing for model I ("Model I's group Sp(2,R) is non-amenable", Step 3), while version 2 of the note states the exception for hyperbolic models.

Round 4 checked the citation: "first author of the second is A. Duncan (INSPIRE), not 'N. Duncan'", and the erratum was added (audit notes Step 1). The adjudication accepted both corrections (`review/round4-adjudication.md`, 'Rulings', "Citations").

## How model I uses these results

The theorem and its exception apply to different parts of model I.

- **The metric sector is a hyperbolic model.** The referee: "its H-sector is the SO(1,2)/SO(2) hyperbolic sigma model" (Step 3, point C2). The upper half-plane with its invariant metric is the hyperbolic plane, which is also SO(1, 2)/SO(2) [T]. The adjudication upheld the point from the literature (ruling "Mermin–Wagner vs [11]"; [11] is the first version's number for reference [15]).
- **The polarization angle is compact.** At H = 1 the vacua form a circle of real structures K(φ), and moving along it is a rotation, an element of the compact SO(2) that contains ρ. Held at H = 1, model I is a circle-valued sigma model, the kind of model the theorem covers when no potential is added ([the frozen-H reduction](/wiki/symmetry-breaking/toy-models/coset-model/frozen-h-reduction)).
- **The restriction.** The ruling: "The Mermin–Wagner statement must be restricted to the compact SO(2) containing ρ. Whether that SO(2) is broken in the coupled model is open." Version 2: "In 1+1 the compact angle φ cannot order: Mermin–Wagner [13, 14] applies to the compact SO(2) containing ρ." and "The non-compact half-plane sector is a hyperbolic model, where symmetry breaking in 2D does occur [15]. Whether ρ's SO(2) stays unbroken in the full coupled model is open." (§4). See [Open: does ρ's SO(2) break in the coupled model?](/wiki/symmetry-breaking/toy-models/coset-model/so2-question)

The worklog had listed the hyperbolic route as one way to pass criterion S4, "Or the non-amenability route (Duncan–Niedermaier–Seiler), whose applicability to this target is unchecked" ('Chunk 1 results'). Its final assessment, which scores the coset model as passing "only with a ρ-preserving τ-type potential", adds "Non-amenability not needed, not tested" ('Assessment against the predictions').

## Related models in the literature

The worklog's prior-art survey, with every citation retrieved [S], found related models but "no existing action has Born reciprocity exactly symmetric and spontaneously broken with η or K as order parameter" ('Chunk 1 results'). The two closest:

- **Born sigma models.** "Born sigma models choose the polarization by gauging [3]" (note §1; V. E. Marotta and R. J. Szabo, Rev. Math. Phys. 33, 2150031 (2021), arXiv:1910.09997). The referee: they "treat Born geometry as target structure, not as dynamical (H,K) fields", and an INSPIRE search for "Born geometry", coset and "order parameter" "returned 0" (Step 3).
- **Broken O(D,D) in [double field theory](/wiki/phase-space/born-geometry/double-field-theory).** Angus, Kim and Park (arXiv:2111.07947): "there H is the order parameter, with η fixed" (worklog, 'Chunk 1 results'). In model I, by contrast, the neutral metric η = ωK is the order parameter ([the order parameter](/wiki/symmetry-breaking/order-parameter)).

## Standard references

The program's documents cite these:

- N. D. Mermin, H. Wagner, Phys. Rev. Lett. 17, 1133 (1966) — the note's [13].
- S. Coleman, "There are no Goldstone bosons in two dimensions", Commun. Math. Phys. 31, 259 (1973) — the note's [14].
- M. Niedermaier, E. Seiler (2005), and A. Duncan, M. Niedermaier, E. Seiler (2005, erratum 2006), as above — the note's [15], retrieved [S].
- V. E. Marotta, R. J. Szabo (2021), as above — the note's [3].

Added by the wiki from model memory (†); the program's documents do not cite them:

- M. Gell-Mann, M. Lévy, "The axial vector current in beta decay", Nuovo Cimento 16, 705 (1960)† — the σ field that gave the model its name.
- A. M. Polyakov, *Gauge Fields and Strings* (1987)† — sigma models in two dimensions.

## Used by

- [Model I: action and symmetries](/wiki/symmetry-breaking/toy-models/coset-model/action-and-symmetries) — a coset sigma model of (H, K) whose K kinetic term is contracted with H to avoid the dS₂ ghost.
- [Model I vacua, the order parameter and the Goldstone spectrum](/wiki/symmetry-breaking/toy-models/coset-model/vacua) — the vacuum manifold, the upper half-plane of metrics times a circle of real structures, and its three flat directions.
- [The frozen-H reduction](/wiki/symmetry-breaking/toy-models/coset-model/frozen-h-reduction) — at H = 1, a circle-valued sigma model of one angle.
- [Monte Carlo: an ordered ℤ₂ phase](/wiki/symmetry-breaking/toy-models/coset-model/monte-carlo) — the lattice XY model with a two-fold field, and the slow decay of order without it.
- [Open: does ρ's SO(2) break in the coupled model?](/wiki/symmetry-breaking/toy-models/coset-model/so2-question) — the hyperbolic H-sector keeps the compact-symmetry theorem from settling the full model.
- [The polarization as a Goldstone angle](/wiki/symmetry-breaking/goldstone-angle) — the compact flat direction of the coset model.

## Sources

- `papers/reciprocity-toy-models.md` §1, §2, §4, refs [3], [13]–[15] — the literature statements and their use in model I
- `review/round4/referee/audit-notes.md` Step 1 — the abstract quotation, the citation corrections and the H-sector identification
- `review/round4/referee/audit-notes.md` Step 2(a), Step 3 — the kinetic-term checks; non-amenability; the novelty search and the "simple coset" remark
- `review/round4/referee/out_model1.txt` — "2*db*dc" and "db**2 + dc**2"
- `review/round4-adjudication.md` 'Rulings' — "Mermin–Wagner vs [11]", upheld (literature); the citation corrections
- `notes/toy-lagrangian.md` 'Success criteria', 'Chunk 1 results', 'Assessment against the predictions' — criterion S4; the citations, retrieved [S]; the dS₂ ghost; the non-amenability framing and its outcome
- `verify/toy_coset.py` — the target spaces of H and K as the script defines them; the positivity and indefiniteness checks
