---
title: "Elementary symmetric polynomials"
weight: 60
status: established
description: "eₙ of the eigenvalues of √(g⁻¹f), power sums and Newton's identities: the building blocks of the bimetric potential, its linearization coefficients C(3, n−1) (battery T6) and the span test T7."
provenance: [T, V]
sources:
  - "papers/broken-born-checkpoint-v2.md §2"
  - "papers/broken-born-checkpoint-v2.md §7.2"
  - "papers/broken-born-checkpoint-v2.md §7.3"
  - "verify/battery.py T6"
  - "verify/battery.py T7"
  - "notes/debt1a-iv-beta-coefficients.md §1"
  - "notes/debt1a-iv-beta-coefficients.md §2"
  - "notes/debt1a-iv-beta-coefficients.md §3"
  - "notes/debt1a-iii-tuning-test.md §2"
  - "notes/debt1a-ii-X-classification.md §3"
  - "HANDOFF.md §5"
  - "HANDOFF.md Appendix A"
---

*The elementary symmetric polynomials of a list of numbers are the sums of all products of distinct entries taken n at a time: e₁ is the sum, e₂ the sum of all pairwise products, and so on up to the product of all the entries, with e₀ = 1. Applied to the eigenvalues of the matrix √(g⁻¹f), built from the two metrics of [bimetric gravity](/wiki/gravity/spin-2-fields/hassan-rosen-bimetric), they are the building blocks of the ghost-free bimetric potential, which is a linear combination of them with constant coefficients. Power sums beyond the first, such as p₄, the sum of fourth powers, can be written in terms of the eₙ by Newton's identities, but only as nonlinear polynomials, so they lie outside that family. The program's [verification battery](/wiki/method/verification/battery) checks two facts of this algebra: the linear coefficients of the eₙ near the identity matrix, which give the tadpole of the program's potential (test T6), and that p₄ is not a linear combination of the eₙ (test T7).*

**Status:** Established — [T] for the algebra; [V] for battery tests T6 and T7, which pass in the last recorded gate run ([the verification battery](/wiki/method/verification/battery)). T7 tests the power sum p₄ alone, numerically. The statement that the [metric-tier](/wiki/gravity/tuning-test/metric-tier-failures) structure Tr(g²) + Tr(g⁻²) lies outside the family rests on the derivation [D] of [calc note #7](/wiki/history/documents/debt-1-notes), not on the test.

## Definition

For d numbers λ₁, …, λ_d, the n-th elementary symmetric polynomial eₙ is the sum of all products of n of them with distinct indices [T]:

```text
e₀ = 1
e₁ = λ₁ + λ₂ + … + λ_d
e₂ = Σ_{i<j} λᵢ λⱼ
eₙ = Σ_{i₁<i₂<…<iₙ} λ_{i₁} λ_{i₂} ⋯ λ_{iₙ}
e_d = λ₁ λ₂ ⋯ λ_d          (and eₙ = 0 for n > d)
```

One generating function holds all of them [T]:

```text
(1 + tλ₁)(1 + tλ₂) ⋯ (1 + tλ_d) = e₀ + e₁t + e₂t² + … + e_d t^d
```

When the left side is multiplied out, the coefficient of tⁿ collects one product for each choice of n factors whose tλ term is taken, which is the definition of eₙ.

Each eₙ is unchanged by any reordering of the λᵢ, which is what "symmetric" means. The fundamental theorem of symmetric polynomials says more: every symmetric polynomial in λ₁, …, λ_d can be written as a polynomial in e₁, …, e_d, and in only one way, because the eₙ are algebraically independent [T]. The eₙ are the basic symmetric functions from which every other one is assembled.

### Of a matrix

For a d × d matrix M, eₙ(M) means eₙ of the eigenvalues of M. With the eigenvalues in the generating function it becomes a determinant [T]:

```text
det(1 + tM) = Σₙ eₙ(M) tⁿ          e₁(M) = Tr M,    e_d(M) = det M
```

So the eₙ(M) are, up to sign, the coefficients of the characteristic polynomial of M. They can be computed from the entries of M without finding its eigenvalues, and they do not change when M is replaced by a similar matrix S·M·S⁻¹ [T].

The program works in four spacetime dimensions, so the matrix 𝕏 of the bimetric potential (below) is 4 × 4 and there are five polynomials, e₀ to e₄, one for each of the five coefficients β₀ to β₄ of the bimetric potential ([#8](/wiki/history/documents/debt-1-notes) §1, §3). The function `en` in `verify/battery.py` computes eₙ of a list of eigenvalues as defined above: a sum over all n-element combinations, with e₀ = 1.

### Binomial coefficients

The binomial coefficient C(d, n) counts the ways to choose n items from d [T]. If every λᵢ equals 1, each product in eₙ equals 1, and there are C(d, n) of them, so eₙ(1, …, 1) = C(d, n). For the 4 × 4 identity matrix this is the first line of the program's vacuum-energy calculation: "At the aligned point 𝕏 = 1: eₙ(1) = C(4,n)" (#8 §2).

## Power sums and Newton's identities

The k-th power sum is pₖ = λ₁ᵏ + λ₂ᵏ + … + λ_dᵏ; for a matrix, pₖ(M) = Tr(Mᵏ) [T]. Power sums are symmetric, so by the fundamental theorem each one is a polynomial in the eₙ. Newton's identities produce that polynomial step by step [T]:

```text
pₖ − e₁pₖ₋₁ + e₂pₖ₋₂ − … + (−1)^(k−1) eₖ₋₁p₁ + (−1)^k k eₖ = 0          (k ≥ 1)
```

The first identity gives p₁ = e₁. Each later one gives pₖ in terms of e₁, …, eₖ and the lower power sums, and substituting the lower ones back in writes pₖ as a polynomial in the eₙ alone. From k = 2 on, that polynomial contains the power e₁ᵏ, a product of eₙ. Because the representation is unique, pₖ for k ≥ 2 has no other form that is a linear combination of the eₙ with constant coefficients [T].

This is the algebra behind a statement of [calc note #7](/wiki/history/documents/debt-1-notes): "Tr(g²) = p₄ of the square-root eigenvalues is a *nonlinear* polynomial in the eₙ, hence outside the family" (#7 §2).

## The ghost-free bimetric potential is linear in the eₙ

### The matrix √(g⁻¹f)

[Hassan–Rosen bimetric gravity](/wiki/gravity/spin-2-fields/hassan-rosen-bimetric) has two dynamical metrics, g and f. Its potential is built from the matrix 𝕏 = √(g⁻¹f), a square root of g⁻¹f, so that 𝕏² = g⁻¹f [T]. When g and f are positive definite, g⁻¹f has positive eigenvalues and exactly one square root with positive eigenvalues [T]. #7 §2 speaks of "the square-root eigenvalues" without saying which of the two metrics is held fixed, so it leaves open whether the root is √(g⁻¹f) or its inverse, √(f⁻¹g) (see below). Calc note #7 works in this Euclidean setting ("in the vacuum frame (g₀ = 1), Euclidean skeleton", §2). The extension of the program's results to Lorentzian signature is [Open: Lorentzian dressing of the Euclidean skeleton (OP3)](/wiki/phase-space/born-geometry/lorentzian-dressing).

### The potential

Calc note #8 writes the potential for the program's two frames, e and f = E₀[J] (#8 §1; see [the frame tier](/wiki/gravity/tuning-test/frame-tier) and [the vielbein formulation](/wiki/gravity/spin-2-fields/vielbein-formulation)):

```text
V = 2m²M² Σₙ₌₀⁴ βₙ eₙ(𝕏),        𝕏 = √(g⁻¹f)
```

The note does not define m or M. The five coefficients βₙ are constants, so V is a linear combination of the eₙ(𝕏). Linearity with constant coefficients is the defining feature of the family: "The Hassan–Rosen ghost-free family is *linear* combinations Σβₙeₙ(√(g⁻¹f)) (constants βₙ)" (#7 §2). Other functions of the eigenvalues of 𝕏 fall outside it, and "a generic potential reintroduces the Boulware–Deser ghost" (#6 §3), an extra mode whose energy has the wrong sign ([the Fierz–Pauli mass term and the Boulware–Deser ghost](/wiki/gravity/spin-2-fields/fierz-pauli)). The single-metric form of the same potential, with f a fixed reference metric, is [de Rham–Gabadadze–Tolley (dRGT) massive gravity](/wiki/gravity/spin-2-fields/drgt-massive-gravity).

### Inversion reverses the order

Replacing each λᵢ by 1/λᵢ in the generating function and clearing denominators gives a standard identity [T]. For an invertible 4 × 4 matrix:

```text
eₙ(𝕏⁻¹) = e₄₋ₙ(𝕏) / e₄(𝕏)
```

Inverting the matrix reverses the order of the eₙ, up to one overall factor. In the action the potential multiplies the volume factor √|g|, with |g| the absolute value of det g. Since e₄(𝕏) = det 𝕏 = √(det f / det g), that factor absorbs the overall factor [T]:

```text
√|g| eₙ(√(g⁻¹f)) = √|f| e₄₋ₙ(√(f⁻¹g))
```

So the same potential, written with f's volume factor and the inverse square root √(f⁻¹g), has its coefficients in reverse order: the term with βₙ becomes the term with β₄₋ₙ [T]. Calc note #8 records an exchange identity, Sₙ(g, f) = S₄₋ₙ(f, g), without defining Sₙ (#8 §1); the wiki reads it as this identity.

Calc note #8 then takes [Born reciprocity](/wiki/phase-space/reciprocity/born-reciprocity) to act on the broken vacuum "as the frame exchange (𝕏 → 𝕏⁻¹ in the aligned frame …)" and concludes that invariance of the potential forces βₙ = β₄₋ₙ [D] (#8 §1). That is [the palindrome βₙ = β₄₋ₙ](/wiki/gravity/palindromic-branch/palindrome).

## Linearization at the identity (battery T6)

### The formula

At the aligned point the two frames coincide and 𝕏 = 1. Calc note #8 expands the eₙ around it: "linearizing eₙ(1+δ) = C(4,n) + C(3,n−1)Tr δ" (#8 §2). The note states the result without derivation.

The coefficient C(3, n−1) comes from counting [T]. For a small symmetric matrix δ, the eigenvalues of 1 + δ are 1 + δ₁, …, 1 + δ₄, where δᵢ are the eigenvalues of δ. A product of n of the factors (1 + δᵢ) equals 1, plus the sum of its n values δᵢ, plus terms of second order in δ. A given index i appears in every n-element subset of the four indices that contains it, and there are C(3, n−1) such subsets, since the other n − 1 indices are chosen from the remaining three. Summing over all subsets:

```text
eₙ(1 + δ) = C(4, n) + C(3, n−1) (δ₁ + δ₂ + δ₃ + δ₄) + O(δ²)
          = C(4, n) + C(3, n−1) Tr δ + O(δ²)
```

For n = 0 the linear coefficient is zero, since e₀ = 1 does not depend on δ.

### The tadpole

Weighting these linear coefficients by the βₙ gives the linear term of the potential. A term linear in the departure from a point is a tadpole: unless it vanishes or is balanced by another term, the point is not a solution of the field equations [T]. Calc note #8: linearizing "gives the tadpole combination T = β₁ + 3β₂ + 3β₃ + β₄" (#8 §2). Under the palindrome this T enters [the vacuum-energy identity V(1) = 2T](/wiki/gravity/palindromic-branch/vacuum-energy-identity), whose integer arithmetic is battery test T5. The [checkpoint](/wiki/history/documents/checkpoint) uses T without defining it (#11 §7.3); the definition is #8's.

### Battery test T6

T6 checks the coefficients numerically [V]. It draws one random symmetric 4 × 4 matrix δ with small entries (`randsym(1e-6)` in `verify/battery.py`), takes the eigenvalues of 1 + δ, and computes (eₙ − C(4, n)) / Tr δ for n = 0 to 4. The check passes when the five ratios agree with [0, 1, 3, 3, 1] to within `atol=1e-3` (numpy's `allclose`). The last recorded gate run prints:

```text
PASS  T6 e_n(1+delta) linear coefficients = C(3,n-1) = [0,1,3,3,1]  [[0.0, 1.0, 3.0, 3.0, 1.0]]
```

The test evaluates one random matrix, so it confirms the formula on one instance; the general statement rests on the counting argument above. It is one of the seven battery tests with which the checkpoint verifies its [Tier-1](/wiki/method/claim-tiers) (explicit-algebra) claims, "the binomial linearization coefficients" (#11 §2). `HANDOFF.md` §5 lists it as "T6 eₙ(1+δ) linear coefficients = C(3,n−1)", and [the handoff](/wiki/history/documents/handoff)'s Appendix A, from which the script was copied, expects "T6 = [0,1,3,3,1]".

## The span test (battery T7)

### What is being tested

The program's first candidate potentials for the mass of the [momentum graviton X](/wiki/gravity/momentum-graviton) were built from metrics. On the slice X = 0, calc note #7 finds "Tr(S²) = Tr(g²) + Tr(g⁻²) − 2d" (§2), with d the dimension and S the diagonal block of the [misalignment measure](/wiki/gravity/tuning-test/misalignment-potential) from which those potentials are built. Calc note #7 argues that this structure lies outside the ghost-free family, because "Tr(g²) = p₄ of the square-root eigenvalues is a *nonlinear* polynomial in the eₙ, hence outside the family. Fail again, independently of the linearized check" (#7 §2, tagged [D — rigorous]). It is the second of [the metric tier's two failures](/wiki/gravity/tuning-test/metric-tier-failures).

### How T7 tests it

T7 checks the central algebraic fact, that p₄ is not a linear combination of e₀, …, e₄, numerically [V]. It draws 300 lists of four numbers, each uniform between 0.5 and 2.0, so all are positive, as square-root eigenvalues of positive-definite metrics are. For each list it computes e₀ to e₄ and p₄. A least-squares fit then finds the five constant coefficients that best reproduce p₄ as a combination of e₀ to e₄ over all 300 lists. If p₄ were in the span of the eₙ, the fit would be exact and the residual zero up to rounding. The last recorded gate run prints:

```text
PASS  T7 p4 outside span of e_n (rms residual nonzero)  [rms=3.2853]
PASS  T7 parity: rms 3.29 as quoted  [rms=3.2853]
```

The first check passes when the root-mean-square residual exceeds `1e-6`. The size of the residual depends on the sampled range; the test uses only the fact that it is not zero. The second line is a parity check: it confirms that this environment still reproduces the figure the documents quote, "rms residual 3.29" (#11 §2). `HANDOFF.md` gives the same figure as "lstsq rms ≈ 3.29" (§5) and "T7 rms ≈ 3.3" (Appendix A). A parity check reproduces the program's own number, so it is not an [independent anchor](/wiki/method/verification/independent-anchors).

### What T7 does not show

The checkpoint states the metric-tier failure as "nonlinear structure Tr(g²) + Tr(g⁻²) provably outside the linear-in-eₙ span (T7)" (#11 §7.2). T7 tests p₄ alone, on samples. The [V] tag covers that numerical statement. The exclusion of Tr(g²) + Tr(g⁻²), and the word "provably", rest on the derivation in #7 §2, so the wiki tags that exclusion [D], not [V] ([conflicts between sources](/wiki/history/documents/source-conflicts)).

## Standard references

- I. G. Macdonald, *Symmetric Functions and Hall Polynomials* (1979; second edition 1995)†: elementary symmetric polynomials, power sums and Newton's identities. Added by the wiki from model memory; the program's documents cite no reference for this algebra.
- For the bimetric potential, the checkpoint cites S. F. Hassan and R. A. Rosen [10†, 11†] and, for its single-metric form, C. de Rham, G. Gabadadze and A. J. Tolley [9†]; see [Hassan–Rosen bimetric gravity](/wiki/gravity/spin-2-fields/hassan-rosen-bimetric) and [dRGT massive gravity](/wiki/gravity/spin-2-fields/drgt-massive-gravity).

## Used by

- [The vacuum-energy identity V(1) = 2T](/wiki/gravity/palindromic-branch/vacuum-energy-identity) — eₙ(1) = C(4, n) and the tadpole coefficients (T6).
- [The metric tier fails twice](/wiki/gravity/tuning-test/metric-tier-failures) — p₄ lies outside the span of the eₙ (T7).
- [The palindrome βₙ = β₄₋ₙ](/wiki/gravity/palindromic-branch/palindrome) — inversion reverses the order of the eₙ.
- [Hassan–Rosen bimetric gravity](/wiki/gravity/spin-2-fields/hassan-rosen-bimetric) — the potential is linear in the eₙ.
- [The verification battery T1–T7](/wiki/method/verification/battery) — tests T6 and T7.

## Sources

- `papers/broken-born-checkpoint-v2.md` §2 — the battery's Tier-1 list: "the binomial linearization coefficients" and "rms residual 3.29".
- `papers/broken-born-checkpoint-v2.md` §7.2, §7.3 — Tr(g²) + Tr(g⁻²) "provably outside the linear-in-eₙ span (T7)"; T used without a definition.
- `verify/battery.py` T6, T7 — the function `en`, the two tests, their tolerances and the printed output.
- `notes/debt1a-iv-beta-coefficients.md` §1, §2, §3 — the potential and its exchange identity; eₙ(1) = C(4, n), the linearization and the tadpole; the five βₙ.
- `notes/debt1a-iii-tuning-test.md` §2 — linearity of the ghost-free family; p₄ as a nonlinear polynomial in the eₙ; the Euclidean skeleton.
- `notes/debt1a-ii-X-classification.md` §3 — a generic potential reintroduces the Boulware–Deser ghost.
- `HANDOFF.md` §5, Appendix A — the descriptions of T6 and T7 and their expected output.
