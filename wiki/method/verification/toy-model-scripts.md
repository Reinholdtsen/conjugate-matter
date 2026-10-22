---
title: "The toy-model scripts"
weight: 90
status: method
description: "toy_coset, toy_gw, toy_s4 and toy_s5: what each checks for the toy-model note and by what method, their anchors and tolerances, what they leave unchecked, and the vacuous checks caught before commit."
provenance: [D, V]
sources:
  - "verify/toy_coset.py"
  - "verify/toy_gw.py"
  - "verify/toy_s4.py"
  - "verify/toy_s5.py"
  - "papers/reciprocity-toy-models.md §2–§6"
  - "papers/broken-born-checkpoint-v2.md §4"
  - "papers/broken-born-checkpoint-v2.md §10"
  - "papers/broken-born-checkpoint-v2.md §14 item 11"
  - "notes/toy-lagrangian.md 'Success criteria (fixed 2026-10-19, before any construction)'"
  - "notes/toy-lagrangian.md 'Chunk 2 results (2026-10-19): the Grosse–Wulkenhaar route'"
  - "notes/toy-lagrangian.md 'Chunk 4 (in progress, 2026-10-19): S5'"
  - "notes/toy-lagrangian.md 'Write-up and review (2026-10-19/20)'"
  - "review/round4-adjudication.md 'Rulings'"
  - "review/wiki-build-flags.md items 2, 10, 11, 12, 13"
---

*The toy-model scripts are four programs in `verify/` that recompute the results of the toy-model note, which studies two explicit field theories in which the exchange of position and momentum is an exact symmetry that the vacuum breaks. `toy_coset.py` checks the coset sigma model (model I), `toy_gw.py` the self-dual Grosse–Wulkenhaar model (model II), `toy_s4.py` runs a lattice Monte Carlo of model I with the phase-space metric held fixed, and `toy_s5.py` checks how the vacuum's choice can make matter interactions local in position. They were written with the models on 2026-10-19, extended with the corrections of the round-4 review, and run in the gate. Their checks are exact symbolic identities, numerical tests against anchors taken from the cited literature, and seeded simulations with error bars; each confirms the arithmetic of the model as written, and several of the note's conclusions rest on arguments that no script checks.*

**Status:** Method, in force — #11 tags the toy results these scripts gate [D][V] (§4, the P2′ refinement; §10, "Toy-model support") — run in [the gate](/wiki/method/verification/the-gate); in the run of 2026-10-21 every check in all four passed.

## What they check, and for what

The toy-model note, `papers/reciprocity-toy-models.md`, answers [acceptance criterion 1](/wiki/symmetry-breaking/toy-models/acceptance-criterion): an action in which ρ, the exchange (x, p) → (p, −x), is a symmetry that the vacuum breaks, with η as order parameter ([the toy models](/wiki/symmetry-breaking/toy-models)). Before any construction the worklog fixed six [success criteria](/wiki/symmetry-breaking/toy-models/success-criteria): S0, a prior-art survey; S1, invariance of an explicit action, "verified symbolically"; S2, degenerate vacua that ρ permutes with no fixed point; S3, an order parameter built from η that is odd under ρ; S4, survival of the breaking under fluctuations in 1+1 dimensions, preferably shown by "a lattice simulation"; and S5, interactions local in the selected polarization, shown by "an explicit computation". The scripts check S1 to S5; S0 is literature work.

The note's §6 lists its results as "Shown (each by executed code)". #11 records them in §14 item 11 and tags them [D][V] in §4 and §10.

## `verify/toy_coset.py`: model I

[Model I](/wiki/symmetry-breaking/toy-models/coset-model) has two fields on a 1+1-dimensional base: a phase-space metric H, written through Z = X + iY in the upper half-plane, and a real structure K with K² = 1. The docstring gives its Euclidean Lagrangian:

```text
L = (f_H^2/8) Tr(H^-1 dH H^-1 dH) + (f_K^2/4) Tr(H^-1 dK^T H dK) + V,
V = (lam/8) Tr(H^-1 C^T H C),  C = K I + I K.
```

with Sp(2,ℝ) acting by H → SᵀHS, K → S⁻¹KS, and ρ = [[0, 1], [−1, 0]] one of its elements.

What it checks, in order:

- **Anchors.** H(Z) is symplectic with I = ω⁻¹H squaring to −1, and ρ is symplectic with ρ² = −1; both exact in sympy.
- **S1, symmetry.** Each of the three terms is invariant under a generic symplectic S with three symbolic parameters, hence under ρ, and under K → −K, all exactly. The K kinetic term is positive on 200 random samples of H and ∂K (no ghost), while the naive Tr(∂K ∂K) is indefinite on K's target space, equal to 2 db dc at K₀ ([action and symmetries](/wiki/symmetry-breaking/toy-models/coset-model/action-and-symmetries)).
- **S2, vacua.** At H = 1 the potential is a sum of squares, |C|² = 2(b − c)², vanishing on the circle K(φ); ρ maps K(φ) to K(φ + π); within that circle no vacuum is ρ-invariant (sympy finds no solution); ρ acts on Z as Z → −1/Z; and the stabilizer of the vacuum (1, K₀) in Sp(2,ℝ) is {+1, −1} ([vacua](/wiki/symmetry-breaking/toy-models/coset-model/vacua)).
- **S3 and the spectrum.** O = K₁₁ takes +1 in (1, K₀) and −1 in its ρ-image; the potential's Hessian at the vacuum has rank 1, leaving three flat (Goldstone) directions.
- **The round-4 repair, with H dynamical.** [The bounded potential V_b](/wiki/symmetry-breaking/toy-models/coset-model/bounded-potential) is invariant under ρ and under K → −K (exact); Tr(K_refᵀK_ref) = 2, the input to the Cauchy–Schwarz bound −1 ≤ V_b ≤ 0; V_b(K(φ)) = −(1 + cos 2φ)/2 at H = 1 (exact); and 20000 random points on the hyperboloid stay inside [−1, 0]. The Hessian of the full potential at (1, K_ref), over all four field coordinates, is computed by finite differences: with [the naive potential](/wiki/symmetry-breaking/toy-models/coset-model/naive-potential) it has a negative eigenvalue (a saddle), with V_b it has non-negative eigenvalues and exactly one zero. The script also checks the note's quoted figures, the unboundedness along a boost at t = 4, the flat squeeze line, the rise of V_b along the boost family, and round-4 finding F3, that the [twisted element](/wiki/symmetry-breaking/twisted-element) ρ∘(K → −K) fixes (1, K_ref).

What it does not check:

- V ≥ 0 is checked as a sum of squares at H = 1; the absence of a ρ-invariant vacuum is solved within the circle K(φ) at H = 1.
- V_b's bound is checked through its input Tr(K_refᵀK_ref) = 2 and by sampling; the Cauchy–Schwarz step itself is the note's argument.
- The Hessians are evaluated at one point, (1, K_ref), at λ = μ = 1 ("these coordinates"). The adjudicator's eigenvalues at λ = 10 and 100 are not in the script.
- The flat squeeze line is checked as flat; whether it is a symmetry is a separate question on which the sources disagree (flag 12 in `review/wiki-build-flags.md`; [the reduced-model stability rule](/wiki/method/verification/reduced-model-stability#the-zero-mode-where-the-sources-disagree)).

Its output, from the run of 2026-10-21:

```text
== Anchors
PASS  H(Z) is symplectic and I = w^-1 H squares to -1
PASS  rho is symplectic and is the quarter turn: rho^2 = -1

== S1: the action is invariant under Sp(2,R), hence under rho
PASS  generic S is symplectic
PASS  H kinetic term invariant under generic symplectic S
PASS  K kinetic term invariant under generic symplectic S
PASS  potential term invariant under generic symplectic S
PASS  all three terms invariant under rho
PASS  all three terms invariant under K -> -K
PASS  the K kinetic term Tr(H^-1 dK^T H dK) is positive for random H and dK (no ghost)
PASS  the naive Tr(dK dK) is indefinite on K's target space (de Sitter): 2 db dc

== S2: vacua
PASS  at H = 1, |C|^2 = 2 (b - c)^2: V = 0 exactly when K is symmetric  [2*(b - c)**2]
PASS  K(phi) is a compatible real structure for every phi
PASS  V vanishes on the circle K(phi) at H = 1
PASS  V >= 0: V = (lam/8)|C|^2_H is a sum of squares at H = 1
PASS  rho maps the vacuum (1, K(phi)) to (1, -K(phi)) = (1, K(phi + pi))
PASS  no vacuum is rho-invariant: at H = 1 a compatible K with rho^-1 K rho = K must vanish
PASS  rho acts on Z as Z -> -1/Z with fixed point Z = i
PASS  the stabilizer of the vacuum (1, K0) in Sp(2,R) is {+1, -1} (so the orbit is 3-dimensional)

== S3: order parameter
PASS  O = K_11 takes +1 in (1, K0) and -1 in its rho-image (1, -K0)

== Spectrum at the vacuum (1, K0): 4 fields, 3-dim vacuum manifold
PASS  potential Hessian has rank 1: three flat directions (Goldstones), one massive  [[0, 4, 0, 0]]

== The bounded rho-preserving potential, with H dynamical (round-4 repair)
PASS  V_b is rho-invariant
PASS  V_b is invariant under K -> -K
PASS  Tr(Kref^T Kref) = 2, so Cauchy-Schwarz gives -1 <= V_b <= 0
PASS  at H = 1, V_b(K(phi)) = -(1 + cos 2 phi)/2
PASS  sampled V_b stays in [-1, 0] on the hyperboloid  [min -0.9770]
PASS  the unnormalized potential makes (1, K_ref) a saddle (negative Hessian eigenvalue)  [[-6.472  0.     2.472  8.   ]]
PASS  with V_b, (1, K_ref) is stable: Hessian eigenvalues >= 0 with exactly one zero  [[-0.      0.7639  2.      5.2361]]
PASS  quoted: saddle eigenvalue -6.47; bounded-variant eigenvalues 0, 0.764, 2, 5.236 (lambda = mu = 1, these coordinates)
PASS  quoted: unbounded below - at boost t = 4 the compatibility term is ~0 and -[Tr(K K_ref)]^2 = -8.9e6  [-8.8861e+06]
PASS  the zero mode is the squeeze line H = diag(y, 1/y), K = K_ref: V = -1 all along it
PASS  boosts are penalized: V_b rises from -1 toward -1/2 along the boost family  [[-1.     -0.6329 -0.5183 -0.5   ]]
PASS  round-4 F3: the twisted rho (rho composed with K -> -K) fixes (1, K_ref)

OK — the coset baseline meets S1-S3 classically.
```

## `verify/toy_gw.py`: model II

[Model II](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar) is a scalar field on the noncommutative (Moyal) plane at the self-dual point Ω = 1, where the Langmann–Szabo duality exchanging position and momentum is exact ([noncommutative field theory](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/noncommutative-field-theory)). The script works with θ = 1 and states where its inputs come from: "Inputs taken from the sources, not from memory", namely the matrix base of de Goursac–Tanasa–Wallet (0709.3950, App. A) and the duality of Grosse–Wulkenhaar (hep-th/0402093, eq. 1).

What it checks, in order:

- **Anchors on the matrix base.** The explicit Laguerre form of the basis functions f_mn satisfies the two defining eigen-relations with H = ½x² exactly for m, n ≤ 2; f₀₀ = 2e^{−x²/θ} "as in 0709.3950 (A.2)"; and orthogonality and ∫f_mn = 2πθ δ_mn hold on a grid ([the matrix base](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/model-and-matrix-base)).
- **The duality lemma.** The transform D is computed by direct numerical integration with the Grosse–Wulkenhaar kernel. An anchor fixes its normalization, D f₀₀ = f₀₀; then D f_mn = (−1)^m f_mn is checked for all m, n < 4 at twelve random points, with a tolerance of 10⁻⁷ ([the duality on the matrix base](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/matrix-base-lemma)).
- **The kinetic form.** With exact derivatives, ∫|∂φ|² + x̃²|φ|² is diagonal in the matrix base and proportional to (m + n + 1). The script prints the ratio beside 8π; it asserts the proportionality, not the value.
- **S1, symmetry against covariance.** For the complex field the duality Π and every pair of diagonal unitaries leave the action unchanged, a continuous U(1)^N × U(1)^N; for the real field Πφ is not Hermitian and the quartic term is invariant only in the alternating form ([complex versus real fields](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/complex-and-real-fields)).
- **S2, the complex vacua.** At μ² = 4, λ = 1 and truncation N = 8, gradient descent from six random starts ends at diagonal minima with the stated occupations and S_min = −2.5; the relative phase β of levels 0 and 1 varies between minima and the action is constant around the β circle; the duality maps β to β + π ([complex-model vacua](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/complex-vacua)).
- **The polarization.** Δ(β), the difference between the vacuum's spread in x and its dual's, is nonzero, equals Δ(0) cos β, and changes sign at β = π, with Δ(0) = 10.8828.
- **The real model's one-loop split (round-4 F4).** For N = 6, 8 and 10, both sign-vacua have action −2.5 and positive-definite Hessians (by finite differences), and their one-loop Gaussian free energies, F = ½ Σ ln of the Hessian eigenvalues, differ by 2.634 in favour of diag(a₀, −a₁) ([Open: the real model's one-loop preference](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/real-model-lead)).
- **The tadpole (round-4 F6).** Σ_{k<N} 1/(k + 1) − ln N tends to Euler's constant, so a level-0 tadpole with that propagator grows as ln N.

What it does not check:

- **The restoration argument.** The note's conclusion that the complex model's breaking does not survive quantization is analytic (§4). The script checks its premise, `complex model: S[U phi V^dag] = S[phi] for any diagonal unitaries U, V (a continuous U(1)^N x U(1)^N)`, not its conclusion ([quantum restoration](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/quantum-restoration)).
- **One check is a premise.** "No vacuum is duality-invariant once level 1 condenses" asserts that level 1 condenses (|φ₁₁| > 0.1); the conclusion follows from the preceding check that the duality shifts β by π.
- **The vacuum identification in F4** ("diag(a0, -a1) is the beta = pi vacuum") checks the sign of Δ(π); that diag(a₀, −a₁) is the β = π configuration holds by construction.
- **The tadpole's coefficient.** The F6 check tests one harmonic series against Euler's constant. It does not compute the propagator, and it does not settle whether the tadpole grows as ln N (the note) or 2 ln N (the referee and the adjudication); flag 11 records the conflict.
- **Large N and renormalization.** The note lists "the large-N, renormalized fate of the real model's one-loop selection" as not shown (§6).

Its output:

```text
== Anchors: the explicit matrix base
PASS  H * f_mn = theta (m+1/2) f_mn for m, n <= 2 (exact)
PASS  f_mn * H = theta (n+1/2) f_mn for m, n <= 2 (exact)
PASS  f_00 = 2 exp(-x^2/theta) as in 0709.3950 (A.2)
PASS  orthogonality: int conj(f_kl) f_mn = 2 pi theta delta delta (grid)  [max dev 4.6e-14]
PASS  int f_mn = 2 pi theta delta_mn (grid)

== The duality on the matrix base
PASS  anchor: D f_00 = f_00 (the normalization pi sqrt|det theta|)
PASS  D f_mn = (-1)^m f_mn for all m, n < 4: the duality is left multiplication by parity  [max dev 1.4e-12]

== The Omega = 1 kinetic form in the matrix base
PASS  int |d phi|^2 + xtilde^2 |phi|^2 is diagonal in the matrix base  [max off-diag 1.7e-14]
PASS  and proportional to (m + n + 1)  [ratio 25.1327 (8 pi = 25.1327)]

== S1: is the duality a symmetry of the field space?
PASS  complex model: S[Pi phi] = S[phi] (duality is a field symmetry)
PASS  complex model: S[U phi V^dag] = S[phi] for any diagonal unitaries U, V (a continuous U(1)^N x U(1)^N)
PASS  real model: Pi phi is not Hermitian, so the duality leaves the real field space
PASS  real model: Tr((Pi phi)^4) != Tr(phi^4); the real action is only covariant (alternating legs)
PASS  real model: its quartic is invariant in the alternating form Tr((psi psi^dag)^2), psi = Pi phi

== S2: vacua of the complex model (mu2 = 4: levels 0 and 1 condense)
PASS  every minimum found is diagonal
PASS  with |phi_mm|^2 = q_m = max(0, -(2m+1-mu2)/(2 lam))  [q = [1.5 0.5 0. ]]
PASS  and S_min = -sum (2m+1-mu2)^2/(4 lam)  [-2.5]
PASS  the relative phase beta of levels 0 and 1 varies across minima (a flat direction)  [betas [-1.61  1.4  -0.52  2.06 -2.28  0.64]]
PASS  S is constant around the vacuum circle beta (Goldstone direction)
PASS  the duality maps vacuum beta to vacuum beta + pi
PASS  no vacuum is duality-invariant once level 1 condenses (|phi_11| > 0)
PASS  the duality is the beta -> beta + pi element of the left phase rotations exp(-i alpha N)

== S3/S5 start: x-versus-p polarization of the vacuum profile
PASS  dual of the vacuum profile computed two ways agrees (grid FT vs (-1)^m rule)
PASS  Delta(beta) = <x^2>_vacuum - <x^2>_dual is nonzero at beta = 0 and flips sign at beta = pi  [Delta(0) = 10.8828]
PASS  Delta(beta) = Delta(0) cos(beta): the polarization is an angle on the Goldstone circle
PASS  Delta(0) > 0: the beta = 0 vacuum is broader in x than in p (quoted +10.88)

== Real model: the two sign-vacua are classically degenerate but split at one loop (round-4 F4)
      N= 6: both S = -2.5000; min eig (+) 2.0000, (-) 1.0718; F(+) - F(-) = 2.634
      N= 8: both S = -2.5000; min eig (+) 2.0000, (-) 1.0718; F(+) - F(-) = 2.634
      N=10: both S = -2.5000; min eig (+) 2.0000, (-) 1.0718; F(+) - F(-) = 2.634
PASS  both sign-vacua have the same classical action (-2.5) and positive-definite Hessians  [min eig over all 1.0718]
PASS  F(+) - F(-) = 2.634 at N = 8 (matching the round-4 referee)
PASS  F(+) > F(-) at N = 6, 8, 10: the opposite-sign vacuum diag(a0, -a1) is preferred at one loop  [{6: np.float64(2.634), 8: np.float64(2.634), 10: np.float64(2.634)}]
PASS  diag(a0, -a1) is the beta = pi vacuum, i.e. the one sharper in x (Delta(pi) = -Delta(0) < 0)

== Mass renormalization: the tadpole grows logarithmically with the truncation (round-4 F6)
PASS  sum_{k<N} 1/(k+1) - ln N -> Euler's gamma (the level-0 tadpole with G_0k = 1/(k+1) is ~ ln N)  [[0.62638 0.57772 0.57722]]

OK — Grosse-Wulkenhaar route checks pass.
```

## `verify/toy_s4.py`: criterion S4

S4 asks whether the breaking survives thermal and quantum fluctuations in 1+1 dimensions. The script simulates model I's polarization angle φ on a square lattice with H held at 1:

```text
E = −J Σ⟨ij⟩ cos(φ_i − φ_j) − h Σ_i cos 2φ_i
```

The first term is the angle's kinetic term, an XY-model stiffness; the second is the ρ-preserving potential at H = 1, under which ρ acts as φ → φ + π. Model A has h = 1, model B has h = 0 (exactly self-dual). The docstring: `This is the FROZEN-H reduction of the coset toy (H = 1 held fixed); the unreduced model's stability with the bounded potential V_b is checked in toy_coset.py.` See [the frozen-H reduction](/wiki/symmetry-breaking/toy-models/coset-model/frozen-h-reduction).

The algorithm is checkerboard Metropolis: each sweep updates the two sublattices in turn, proposing a uniform shift of up to ±1 in φ at each site. Every run starts cold (φ = 0), discards 1500 sweeps and measures over 4000. Each value is the mean over four runs with different seeds, and its error bar the standard error, the sample standard deviation over √4. "All runs use a cold start (phi = 0). Error bars: standard error over 4 independent seeds." The order parameter for ρ is m = ⟨cos φ⟩; for model B the script also measures the U(1) magnetization |⟨e^{iφ}⟩|.

The checks and their thresholds:

- **Model A at T = 0.6.** Ordered, ⟨|m|⟩ > 0.8 at every size; size-independent, |m₆₄ − m₁₆| < 3σ + 0.002, with σ the two error bars combined; Binder cumulant above 0.6 (an ordered ℤ₂ phase has 2/3) ([Monte Carlo: an ordered ℤ₂ phase](/wiki/symmetry-breaking/toy-models/coset-model/monte-carlo)).
- **The control, model A at T = 3.** Disordered: m₁₆/m₆₄ within [3.3, 4.8], where 1/L scaling gives 4.
- **Model B at T = 0.6.** No true order: the U(1) magnetization falls from L = 16 to L = 64 by more than 3σ, as the Mermin–Wagner–Coleman theorem requires for a continuous symmetry in two dimensions ([Mermin–Wagner–Coleman](/wiki/symmetry-breaking/mermin-wagner-coleman)). The spin-wave estimate is printed beside the measured ratio; agreement between the two is not asserted.
- **Quoted values.** Three "quoted:" checks require the printed means and error bars to match the note's table to the stated decimals. Because the seeds are fixed, these are reproductions ([the Monte Carlo error-bar rule](/wiki/method/verification/monte-carlo-error-bars)).

Its output:

```text
== Model A: with the rho-preserving potential (h = 1), T = 0.6
      L= 16: <|m|> = 0.9543 +- 0.0001, Binder = 0.6666
      L= 32: <|m|> = 0.9542 +- 0.0001, Binder = 0.6667
      L= 64: <|m|> = 0.9542 +- 0.0000, Binder = 0.6667
PASS  ordered: <|m|> > 0.8 at every size
PASS  size-independent within errors (|m64 - m16| < 3 sigma + 0.002)  [diff -0.0001, sigma 0.0001]
PASS  Binder cumulant near 2/3 (an ordered Z2 phase)
PASS  quoted: <|m|> = 0.954 +- 0.0001 at every size, Binder 0.667

== Control: model A at high temperature, T = 3.0
      L= 16: <|m|> = 0.0653 +- 0.0043
      L= 32: <|m|> = 0.0338 +- 0.0013
      L= 64: <|m|> = 0.0155 +- 0.0004
PASS  disordered: <|m|> scales as 1/L (m16/m64 within [3.3, 4.8], expected 4)  [4.209]
PASS  quoted: 0.0653 +- 0.0043, 0.0338 +- 0.0013, 0.0155 +- 0.0004

== Model B: exactly symmetric (h = 0), T = 0.6
      L= 16: <|M|> = 0.8369 +- 0.0007
      L= 32: <|M|> = 0.8025 +- 0.0039
      L= 64: <|M|> = 0.7736 +- 0.0038
PASS  no true order: the U(1) magnetization falls with size by more than 3 sigma  [ratio 0.9243; spin-wave estimate 0.9360]
PASS  quoted: 0.8369 +- 0.0007, 0.8025 +- 0.0039, 0.7736 +- 0.0038; ratio 0.924 vs spin-wave 0.936

OK — S4: rho is spontaneously broken in 1+1 (frozen-H reduction) only with the rho-preserving potential.
```

What it does not check: the full model I with H dynamical, which the note lists as not shown; critical exponents ("We did not measure critical exponents", note §4); and hot starts, which "coarsen slowly through metastable domains" at L = 64, so ordered-phase values come from cold starts (note §4). The note's "0.954 ± 0.0001 at every size" is printed as ± 0.0000 at L = 64; flag 13 calls the note's figure a conservative bound. The docstring still calls the naive potential "The tau-type potential" and notes that the simulated energy "equals the bounded V_b at H = 1 up to a constant and a factor".

## `verify/toy_s5.py`: criterion S5

S5 asks whether the vacuum's choice of K makes matter interactions local in one polarization and nonlocal in the other. The script has three parts:

- **A, what the vacuum's η fixes** (exact, sympy). η = ωK is a symmetric neutral metric; K's eigenvectors e₊ and e₋ are null for η at every φ and are its only null lines; the two lines are Lagrangian and transverse; K → −K sends η to −η with the same null lines; and ρ maps K to −K and L₊ onto L₋ ([the section condition](/wiki/symmetry-breaking/section-condition)).
- **B, the section condition built from η** (exact). In null coordinates η⁻¹ is purely off-diagonal; fields on one null line pass, fields mixing the two fail, and the condition built from −η passes and fails the same fields, so "it cannot tell L+ from L-".
- **C, an interaction built from the vacuum** (numerical, ħ = 1). For a test state made of two displaced Gaussians, the script computes the Wigner function on a grid and checks Parseval's theorem and both marginals first. The interaction I[W] = ∫_{L₊} du (∫_{L₋} dv W)² equals ∫|ψ(x)|⁴ dx in the vacuum +K_ref and ∫|ψ̃(p)|⁴ dp in −K_ref, and the two values differ by more than 5% of the larger ([locality from an (H, K)-built coupling](/wiki/symmetry-breaking/matter-coupling)). Two further checks carry round-4 finding F5 and the covariance: rescaling the coordinate along L₊ by 2 doubles I, so I needs H as well as K; and the combined map (ψ → Fψ, K → −K) leaves I unchanged, while ∫W², which does not use K, shows no asymmetry.

Part C's output:

```text
== C: a rho-covariant interaction built from K (numerical, hbar = 1)
PASS  Fourier pair is consistent (Parseval)
PASS  Wigner marginal over p is |psi(x)|^2
PASS  Wigner marginal over x is |psi~(p)|^2
PASS  vacuum +K_ref: I = int |psi(x)|^4 dx (local in x)  [0.406972]
PASS  vacuum -K_ref: I = int |psi~(p)|^4 dp (local in p)  [0.360047]
PASS  the two vacua give different physics for the same state  [0.4070 vs 0.3600]
PASS  quoted: 0.4070 vs 0.3600
PASS  I_K is not K-covariant alone: rescaling the L+ coordinate by 2 doubles it (it needs H)  [0.4070 -> 0.8139]
PASS  rho-covariance: I_{-K}[W_{F psi}] = I_{+K}[W_psi]
PASS  a K-blind phase-space interaction int W^2 (= 1/(2 pi) for pure states) shows no asymmetry

OK — S5 (weak form) and the section-condition structure check out.
```

Parts A and B print their checks in the same form; the full output is in a run of `scripts/check.sh`.

What it does not check: the closing line says "weak form". The script evaluates I for one test state at the two vacua ±K_ref; it shows that such a coupling produces locality, not that anything forces matter to couple this way ("Nothing here forces that coupling", note §5; [Open: forced locality and the P4 lock](/wiki/symmetry-breaking/strong-locality)). Its section B treats d = 1; for d > 1 the note cites "a continuous family of sections". Two wording issues sit next to it: part C's header still says "built from K", where the note v2 says the coupling is built from (H, K) (flag 10), and the note's "I is odd in K" overstates what the values 0.4070 and 0.3600 show, which is that I is not invariant under K → −K (flag 2).

## Lessons from writing them

The worklog records three episodes in which a check was wrong before it was right:

- "Two checks were vacuous on the first draft (an always-true term; a condition multiplied by 0) and were replaced by real tests before commit." (chunk 4, `toy_s5.py`).
- "Two drafting errors were caught by gated checks along the way: a hard-coded `True`, and citation regexes matching matrix entries." ('Write-up and review').
- On the model II kinetic form: "A first check used finite-difference derivatives and failed at the 0.3% level. The fix was exact derivatives, not a looser tolerance." (chunk 2). The gate's rule against weakening a check applied to the script's own author.

## Tolerances against quoted precision

Some assertions are looser than the precision the note quotes. The note gives the duality lemma "to ≲ 10⁻¹¹" (§3); the script asserts a deviation below 10⁻⁷ and prints 1.4e-12. The split 2.634 is asserted to three decimals at N = 8; at N = 6 and 10 only its sign is asserted, and the run prints 2.634 at all three. The kinetic form's coefficient 8π(m + n + 1), which the note states, is printed but asserted only up to proportionality.

## What no script checks

The note's §6 lists as not shown: "a Monte Carlo of model I with H dynamical"; "whether ρ's SO(2) breaks in the coupled model without a potential"; "a derivation of the ρ-preserving potential, which introduces a rigid, unordered pair of axes"; "the large-N, renormalized fate of the real model's one-loop selection"; "a mechanism forcing the (H, K)-coupling of matter"; and "anything beyond d = 1". #11 §14 item 11: "Still open [O]: a Monte Carlo with H dynamical; a derivation of the potential; locality of matter beyond the weak (Yukawa-like) form, which in the toy reduces to P4." See [acceptance criterion 1](/wiki/symmetry-breaking/toy-models/acceptance-criterion) and [Open: does ρ's SO(2) break in the coupled model?](/wiki/symmetry-breaking/toy-models/coset-model/so2-question).

## Sources

- `verify/toy_coset.py`, `verify/toy_gw.py`, `verify/toy_s4.py`, `verify/toy_s5.py` — docstrings, checks, thresholds, final lines
- `papers/reciprocity-toy-models.md` §2–§5 — the results the scripts check; §6 — shown and not shown
- `papers/broken-born-checkpoint-v2.md` §4, §10 — the [D][V] tags on the toy results; §14 item 11 — the record and what stays open
- `notes/toy-lagrangian.md` 'Success criteria (fixed 2026-10-19, before any construction)' — S0–S5; 'Chunk 2 results' — the tolerance fix; 'Chunk 4 (in progress, 2026-10-19): S5' — the vacuous checks; 'Write-up and review (2026-10-19/20)' — the drafting errors
- `review/round4-adjudication.md` 'Rulings' — the round-4 findings (F3–F6, the control) that the scripts now carry
- `review/wiki-build-flags.md` items 2, 10, 11, 12, 13 — the wording and coefficient issues beside the scripts
