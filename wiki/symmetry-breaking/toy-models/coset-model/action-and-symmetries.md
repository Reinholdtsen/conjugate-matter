---
title: "Model I: action and symmetries"
weight: 20
status: alive
description: "The Euclidean Lagrangian of a phase-space metric H and a real structure K: a hyperbolic kinetic term for H, an H-contracted kinetic term for K that avoids a ghost, and a compatibility potential; invariant under Sp(2, ℝ) ∋ ρ and a separate ℤ₂ K → −K (criterion S1, verify/toy_coset.py)."
provenance: [V]
sources:
  - "papers/reciprocity-toy-models.md §1"
  - "papers/reciprocity-toy-models.md §2"
  - "verify/toy_coset.py S1"
  - "verify/toy_coset.py S2"
  - "verify/toy_s4.py"
  - "review/round4/referee/audit-notes.md Step 2(a)"
  - "review/round4/referee/audit-notes.md Step 3"
  - "review/round4/referee/out_model1.txt"
  - "review/round4-adjudication.md 'Verdict'"
  - "notes/toy-lagrangian.md 'Success criteria'"
  - "notes/toy-lagrangian.md 'Predictions'"
  - "notes/toy-lagrangian.md 'Chunk 1 results'"
  - "notes/toy-lagrangian.md 'Assessment against the predictions'"
  - "papers/broken-born-checkpoint-v2.md §4"
  - "papers/broken-born-checkpoint-v2.md §5"
  - "papers/broken-born-checkpoint-v2.md §14 item 11"
---

*Model I's action is the integral, over a flat two-dimensional base, of a Lagrangian with three terms: two kinetic terms, which cost action when the fields vary from point to point, and a potential that vanishes exactly when the two fields are compatible. The fields are geometric structures on the phase plane of one particle moving in one dimension: a metric H, parametrized by a point of the upper half-plane, and a real structure K, whose two eigenlines are the candidate position and momentum axes. The action is unchanged by every symplectic (area-preserving) linear map of the phase plane, which includes [Born reciprocity](/wiki/phase-space/reciprocity/born-reciprocity) ρ, and by the separate flip K → −K. That invariance is criterion S1, checked symbolically, and it supplies the "genuine Noether symmetry" that [acceptance criterion 1](/wiki/symmetry-breaking/toy-models/acceptance-criterion) asks for.*

**Status:** Alive — [V] (the worklog records "S1 pass [V]"; criterion S1 in `verify/toy_coset.py`; [the toy-model scripts](/wiki/method/verification/toy-model-scripts)) — confirmed independently with sympy by the [round-4](/wiki/method/review/round-4) referee ("all three terms Sp(2,R)-invariant").

## The setting: one position and one momentum

Model I lives on the phase plane of a single degree of freedom, d = 1. Version 2 of the [toy-model note](/wiki/symmetry-breaking/toy-models) sets it up in five sentences (§1):

> Phase space ℝ² with symplectic form ω = [[0, 1], [−1, 0]]. ρ = [[0, 1], [−1, 0]] is symplectic and squares to −1. A real structure K with K² = 1 and Kᵀ ω K = −ω defines a neutral metric η = ωK. Its null lines are the two eigenlines L± of K, which are Lagrangian. Choosing K is choosing which line is "position".

Each object has a plain meaning [T]:

- **ω** is the [symplectic form](/wiki/phase-space/reciprocity/symplectic-form): it measures signed area in the (x, p) plane. The linear maps that preserve it form Sp(2, ℝ).
- **ρ** is the quarter-turn (x, p) → (p, −x). As a matrix it equals ω, and ρ² = −1 is the half-turn (x, p) → (−x, −p).
- **K** squares to 1 and, for d = 1, has determinant −1, so its eigenvalues are +1 and −1 and it has two eigenlines, L+ and L−. The condition Kᵀ ω K = −ω says that K reverses the sign of areas. In d = 1 every line through the origin is Lagrangian, a line on which ω vanishes ([Lagrangian subspaces and polarizations](/wiki/phase-space/reciprocity/lagrangian-polarizations)).
- **η = ωK** is a symmetric metric with one positive and one negative direction, a neutral metric, whose null lines are L+ and L− ([the structures ω, η, H](/wiki/phase-space/born-geometry/born-structures)). The program reads η, equivalently K, as [the order parameter](/wiki/symmetry-breaking/order-parameter) of broken reciprocity.

For the reference structure K₀ = diag(1, −1), L+ is the x-axis and L− the p-axis. Its ρ-image −K₀ swaps them, because "ρ exchanges L+ and L−" (note §5). Choosing K therefore chooses which line plays the role of position, the choice the program calls a polarization.

## The fields

On a Euclidean 1+1-dimensional base the model has two fields (note §2):

```text
H(Z) = [[Y + X²/Y, X/Y], [X/Y, 1/Y]],   Z = X + iY,  Y > 0        I ≡ ω⁻¹H,  I² = −1
K    = [[a, b], [c, −a]],                a² + bc = 1               (traceless, det K = −1)
```

- **H**, "a positive symmetric symplectic matrix", is a metric on the phase plane: a way of measuring lengths that can mix x and p. Each such H corresponds to one point Z of the upper half-plane, the d = 1 case of [the Siegel domain](/wiki/phase-space/modular-field/siegel-domain). I = ω⁻¹H squares to −1, so it is a quarter-turn adapted to H, a complex structure [T]. At Z = i the metric is H = 1.
- **K** is the real structure. For a traceless 2 × 2 matrix, K² = (a² + bc)·1 and Kᵀ ω K = (det K) ω, so "traceless with det K = −1" is the d = 1 form of K² = 1 and Kᵀ ω K = −ω (both identities are printed in the referee's check, `review/round4/referee/out_model1.txt`). "Its target is the one-sheeted hyperboloid a² + bc = 1, which is two-dimensional de Sitter space" (note §2; [coset and hyperbolic sigma models](/wiki/symmetry-breaking/toy-models/coset-model/sigma-models)).

**Compatibility.** The two fields fit together when K anticommutes with I. The worklog writes the potential as the squared size of that anticommutator, "(λ/8)|{K, ω⁻¹H}|²_H" ('Chunk 1 results'), and version 2 states that the potential "vanishes exactly when K is compatible with H" (§2). At H = 1 the condition is simple: "|C|^2 = 2 (b - c)^2: V = 0 exactly when K is symmetric" (`verify/toy_coset.py`; the referee: "C at H=1: [b - c, 0, 0, b - c] -> zero iff b=c").

## The Euclidean Lagrangian

```text
L = (f_H²/8) Tr(H⁻¹∂H H⁻¹∂H) + (f_K²/4) Tr(H⁻¹ ∂Kᵀ H ∂K) + (λ/8) Tr(H⁻¹ Cᵀ H C)

C = KI + IK,   I = ω⁻¹H
```

The couplings f_H and f_K set the stiffness of the two fields, and λ the strength of the compatibility potential [T]. ∂ stands for a derivative along the base, summed over its two directions. The Lagrangian is Euclidean, so a constant field has only its potential energy.

### The H kinetic term

Tr(H⁻¹∂H H⁻¹∂H) is the standard invariant metric on positive matrices [T]. Under H → SᵀHS with a constant S, the product H⁻¹∂H becomes S⁻¹(H⁻¹∂H)S, and the trace of its square does not change. On the upper half-plane this metric is, up to a constant factor, the hyperbolic metric [T]. The metric sector on its own is therefore a sigma model on the hyperbolic plane, which the round-4 referee identified as "the SO(1,2)/SO(2) hyperbolic sigma model" (`review/round4/referee/audit-notes.md`, Step 3). That identification matters for whether the model can order in two dimensions ([Open: does ρ's SO(2) break in the coupled model?](/wiki/symmetry-breaking/toy-models/coset-model/so2-question)).

### The K kinetic term and the ghost

The obvious kinetic term for K, Tr(∂K ∂K), would carry a ghost. Version 2: "The K kinetic term is contracted with H and is positive definite. The naive Tr(∂K ∂K) is indefinite on the hyperboloid (2 db dc at K₀ = diag(1, −1))." (§2). The worklog gives the reason: "K's own target space (de Sitter dS₂) has an indefinite metric, which would give a ghost" ('Chunk 1 results'). A kinetic term of indefinite sign gives one direction of fluctuation negative energy ([coset and hyperbolic sigma models](/wiki/symmetry-breaking/toy-models/coset-model/sigma-models#positive-target-metrics-and-the-de-sitter-ghost)).

The contracted term Tr(H⁻¹ ∂Kᵀ H ∂K) is positive for every nonzero ∂K [T]: it equals the sum of the squares of the entries of H^{1/2} ∂K H^{−1/2}, since H is symmetric and positive. The sources state the positivity and check it numerically:

- the referee, with sympy: "naive Tr(dK dK) at K0 = '2*db*dc' (indefinite); H-contracted at H=1 = 'db**2 + dc**2'"; and over random samples of H and ∂K, the smallest ratio of the term to the sum of the squared entries of ∂K was 0.0598 (`out_model1.txt`; audit notes Step 2(a));
- the gate: "the K kinetic term Tr(H^-1 dK^T H dK) is positive for random H and dK (no ghost)" and "the naive Tr(dK dK) is indefinite on K's target space (de Sitter): 2 db dc" (`verify/toy_coset.py`).

The contraction keeps the symmetry. Under S, ∂K → S⁻¹∂K S and H → SᵀHS, so H⁻¹ ∂Kᵀ H ∂K becomes S⁻¹(H⁻¹ ∂Kᵀ H ∂K)S and its trace is unchanged [T]. It also couples the two sectors: K's kinetic energy now depends on H.

On the circle of vacua at H = 1, K = K(φ), this term reduces to the stiffness of one angle: "(f_K^2/4)Tr(dK^T dK) = (1/2) f_K^2 (dphi)^2" (referee, Step 2(a)), "an XY stiffness" (`verify/toy_s4.py`). That is the starting point of [the frozen-H reduction](/wiki/symmetry-breaking/toy-models/coset-model/frozen-h-reduction).

### The compatibility potential

The third term is the squared size of C = KI + IK, measured with H, so it is never negative [T]; the gate checks that "V = (lam/8)|C|^2_H is a sum of squares at H = 1" (`verify/toy_coset.py`). It vanishes exactly on the compatible pairs, which are therefore the vacua ([Model I vacua](/wiki/symmetry-breaking/toy-models/coset-model/vacua)). It shares the symmetry [T]: a symplectic S preserves ω, so I = ω⁻¹H becomes S⁻¹IS, C transforms like K, and the same algebra as for the K kinetic term applies.

## The symmetries (criterion S1)

"Sp(2,ℝ) acts by H → SᵀHS, K → S⁻¹KS, and the action is invariant (checked for generic symplectic S, so for ρ). There is a separate ℤ₂, K → −K." (note §2). The same S acts at every point of the base, so this is a global symmetry [T]. The referee wrote the full group as "Sp(2,R) x Z2(K->-K)" (Step 2(a), finding F3).

The flip K → −K is a symmetry because the two terms that involve K are quadratic, one in ∂K and the other in C, and C changes sign with K. ρ belongs to Sp(2, ℝ), so invariance under a generic symplectic S includes invariance under ρ; the gate also checks ρ by itself.

**The checks [V].** `verify/toy_coset.py` takes a symbolic S = [[s₁, s₂], [s₃, (1 + s₂s₃)/s₁]], whose determinant is 1 by construction, and symbolic H, ∂H, K, ∂K. Its S1 block passes these checks:

- "generic S is symplectic";
- "H kinetic term invariant under generic symplectic S", and the same for the K kinetic term and the potential term;
- "all three terms invariant under rho";
- "all three terms invariant under K -> -K".

The worklog records the result as "S1 pass [V]: all three terms are invariant under a generic symplectic S (H → SᵀHS, K → S⁻¹KS), under ρ, and under K → −K." ('Chunk 1 results'). The round-4 referee repeated the computation in its own conventions and found "transformed - original = 0" for each term, and invariance under K → −K (`out_model1.txt`; audit notes Step 2(a)).

**What S1 asks for.** Criterion S1 demands "An explicit action S[fields] on which ρ acts as a symmetry: S is invariant, not merely related to its image by a unitary equivalence. Invariance is verified symbolically." (worklog, 'Success criteria'; [success criteria S0–S5](/wiki/symmetry-breaking/toy-models/success-criteria)). In quantum mechanics ρ is carried out by the Fourier transform, a unitary change of description that any theory admits; that does not make ρ a symmetry of the dynamics ([unitary equivalence versus Noether symmetry](/wiki/phase-space/reciprocity/unitary-equivalence)). In model I, ρ acts on the fields H and K, and the action is unchanged. [Checkpoint #11](/wiki/history/documents/checkpoint) §14 item 11 counts this as the first part of acceptance criterion 1: "ρ is a symmetry of an explicit action, and η = ωK is the order parameter".

## What the symmetries imply

- **The vacua break them.** The vacua are the compatible constant pairs, and ρ carries each one to a different one ([Model I vacua, the order parameter and the Goldstone spectrum](/wiki/symmetry-breaking/toy-models/coset-model/vacua)).
- **The flip qualifies the breaking.** K → −K is also a symmetry, so the composite ρ∘(K → −K), the twisted element, is one too, and it maps the vacuum (1, K₀) to itself. Hence the note's qualification: "Breaking ρ is physical only once a coupling odd in K is present" (note §2; [the twisted element](/wiki/symmetry-breaking/twisted-element); [locality from an (H, K)-built coupling](/wiki/symmetry-breaking/matter-coupling)).
- **The action alone does not fix a polarization.** With only these three terms the vacua form a continuous family, and the polarization is a flat angle on it ([the polarization as a Goldstone angle](/wiki/symmetry-breaking/goldstone-angle)). A definite polarization needs an added ρ-preserving potential: first the [naive form](/wiki/symmetry-breaking/toy-models/coset-model/naive-potential), now dead, then [the bounded potential V_b](/wiki/symmetry-breaking/toy-models/coset-model/bounded-potential).

## History

The worklog fixed the success criteria on 2026-10-19 before building anything, and predicted this part would be easy: "S1–S3 will pass easily. A coset sigma model on the space of compatible (H, K) pairs does it classically, which is close to a construction by definition." ('Predictions'). Model I was built first as "A baseline ... It is cheap, and it fixes what the minimal construction gives" ('Plan'), and passed: "As predicted, S1–S3 come almost by construction. This is a coset model of Sp(2,R) → Z₂." ('Chunk 1 results'). The assessment scored the prediction "Hit".

The prior-art survey found that "no existing action has Born reciprocity exactly symmetric and spontaneously broken with η or K as order parameter", while crediting the idea to Freidel–Leigh–Minic ('Chunk 1 results'; [broken Born duality](/wiki/phase-space/reciprocity/broken-born-duality)). The round-4 referee agreed with qualification: "Model I appears new as a field theory, but it is a simple coset" (Step 3). The adjudication's verdict: "The algebra and numerics of §§2, 3 and 5 reproduced under the referee's own conventions and code." (`review/round4-adjudication.md`, 'Verdict'; [review round 4](/wiki/method/review/round-4)).

## Notation

These pages follow the toy-model note: K is the real structure and η = ωK, as in #11 §14 item 11. Checkpoint #11's postulate P2′ writes the real structure as J and the order parameter as η = HJ (§4). These are not two names for one operator: #11 §5 defines both, J = η⁻¹H and K = η⁻¹ω, and the documents differ in which one they call the structure chosen spontaneously. The sources do not reconcile the two ([the order parameter](/wiki/symmetry-breaking/order-parameter); [notation](/wiki/notation); [P2′](/wiki/program/postulates/p2-prime)).

## Sources

- `papers/reciprocity-toy-models.md` §1, §2 — the setting, the fields, the Lagrangian and the symmetries, quoted above; §5 for ρ exchanging L+ and L−
- `verify/toy_coset.py` S1, S2 — the gated invariance, positivity and compatibility checks
- `verify/toy_s4.py` — the docstring's XY stiffness at H = 1
- `review/round4/referee/audit-notes.md` Step 2(a), Step 3 — the referee's independent symbolic confirmation; the full symmetry group; the hyperbolic H-sector; the novelty remark
- `review/round4/referee/out_model1.txt` — the referee's printed identities and kinetic-term checks
- `review/round4-adjudication.md` 'Verdict' — the algebra reproduced
- `notes/toy-lagrangian.md` 'Success criteria', 'Predictions', 'Chunk 1 results', 'Assessment against the predictions' — criterion S1, the prediction, the S1 pass [V], the reason for the H-contracted kinetic term, the prior-art survey
- `papers/broken-born-checkpoint-v2.md` §4, §5, §14 item 11 — P2′'s J notation; the definitions J = η⁻¹H and K = η⁻¹ω; the criterion as met
