---
title: "Model II: the matrix base and the action"
weight: 20
status: alive
description: "The matrix base f_mn of the Moyal plane with its anchors, the diagonal Ω = 1 kinetic form 8π(m + n + 1)|φ_mn|² computed with exact derivatives, and the action for complex and real fields."
provenance: [V]
sources:
  - "papers/reciprocity-toy-models.md §3"
  - "verify/toy_gw.py (anchors, kinetic form)"
  - "review/round4/referee/audit-notes.md Step 1"
  - "review/round4/referee/audit-notes.md Step 2(b)"
  - "review/round4/referee/out_model2_base.txt"
  - "review/round4-preregistration.md 'Predictions'"
  - "review/round4-adjudication.md 'Pre-registration scored'"
  - "notes/toy-lagrangian.md 'Chunk 1 results'"
  - "notes/toy-lagrangian.md 'Chunk 2 results'"
---

*Model II is the self-dual Grosse–Wulkenhaar model of a self-interacting scalar field on the noncommutative plane, rewritten as a model of matrices. The field is expanded in functions f_mn built from harmonic-oscillator states; in this basis the star product of two fields becomes the product of their matrices, and the integral over the plane becomes a trace. At the self-dual point Ω = 1 the quadratic part of the action is diagonal, 8π(m + n + 1)|φ_mn|², so each matrix entry carries an oscillator energy of its own, and the interaction is the trace of a fourth power of the matrix. A complex field is an arbitrary matrix and a real field a Hermitian one. Every formula was checked against an independent anchor before it was used, and the first check of the kinetic form, made with finite differences, failed until exact derivatives replaced them. The [duality lemma](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/matrix-base-lemma), the vacua and the restoration argument of [model II](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar) are all computed on this set-up.*

**Status:** Alive as a toy — [V]: the matrix-base anchors and the kinetic form are gated in `verify/toy_gw.py` ([the toy-model scripts](/wiki/method/verification/toy-model-scripts)), and the referee of [review round 4](/wiki/method/review/round-4) reproduced every formula with an independent construction. The route built on it fails criterion S4 ([success criteria](/wiki/symmetry-breaking/toy-models/success-criteria); [quantum restoration](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/quantum-restoration)).

## What model II is

Model II is the Grosse–Wulkenhaar model of [noncommutative field theory](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/noncommutative-field-theory), taken in two dimensions, on the Moyal plane [x₁, x₂] = iθ with θ = 1, at the self-dual point Ω = 1 where the Langmann–Szabo duality exchanges the field's position and momentum descriptions. The field has a quartic self-interaction and is either complex or real. The [toy-model note](/wiki/symmetry-breaking/toy-models) computes everything in the matrix base, truncated to the first N oscillator levels, at μ² = 4 and λ = 1 (§3). `verify/toy_gw.py` works at "theta = 1 throughout", with N = 8 for the complex model and N = 6, 8 and 10 for the real model's one-loop split.

Two symbols collide with other uses. H here is the oscillator function ½x², not [model I](/wiki/symmetry-breaking/toy-models/coset-model)'s phase-space metric. N is both the truncation and, in Π = e^{−iπN}, the matrix diag(0, 1, 2, …) that counts oscillator levels ([notation](/wiki/notation)).

## The matrix base

The note takes the basis "as in [9, App. A]", de Goursac, Tanasa and Wallet (§3):

```text
f₀₀ = 2e^{−x²/θ}
f_mn = (m! n! θ^{m+n})^{−1/2} ā^{⋆m} ⋆ f₀₀ ⋆ a^{⋆n}
f_mn ⋆ f_kl = δ_nk f_ml
H ⋆ f_mn = θ(m + ½) f_mn,        f_mn ⋆ H = θ(n + ½) f_mn,        H = ½x²
```

Here a = (x₁ + ix₂)/√2 and its conjugate ā are the ladder functions, as the round-4 referee transcribed the source's appendix (audit notes, Step 1), and a^{⋆n} is the n-fold star product. Star-multiplying by ā from the left raises the left index, and star-multiplying by a from the right raises the right index.

How to read the formulas [T]:

- f₀₀ is the Gaussian that represents the oscillator's ground state.
- f_mn is the [Weyl symbol](/wiki/phase-space/reciprocity/wigner-function) of the operator |m⟩⟨n|, so it has a left oscillator level m and a right level n. The eigen-relations say that star-multiplying by H from the left measures the left level, with energy θ(m + ½), and from the right measures the right level: θ plays ℏ.
- f_mn ⋆ f_kl = δ_nk f_ml is the operator rule |m⟩⟨n| · |k⟩⟨l| = δ_nk |m⟩⟨l|. A field φ = Σ φ_mn f_mn therefore star-multiplies like the matrix (φ_mn).
- ∫ f_mn = 2πθ δ_mn is the trace of |m⟩⟨n| times 2πθ, the area of phase space per quantum state. Integrals over the plane become traces.

The note works with the explicit form

```text
f_mn = 2(−1)^m √(m!/n!) (√(2/θ))^{n−m} (x₁ + i x₂)^{n−m} L_m^{n−m}(2r²/θ) e^{−r²/θ}        (n ≥ m)
```

where r² = x₁² + x₂² and L_m^{n−m} is a generalized Laguerre polynomial (§3). For n < m the function is the complex conjugate of f_nm; the gate script's docstring writes the rule as "f_mn^dagger = f_nm". On the diagonal, n = m, the form reduces to 2(−1)^m L_m(2r²/θ) e^{−r²/θ}: a real function of the radius alone. Diagonal matrices are therefore rotationally symmetric profiles on the plane, which is the form the vacua of model II take ([complex-model vacua](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/complex-vacua)).

## The anchors

An anchor is a check against something independent of the claim being checked: a textbook identity or a value from the literature ([independent anchors](/wiki/method/verification/independent-anchors)). The note: "The explicit Laguerre form … is checked exactly against the H-eigen-relations, and numerically for orthogonality and ∫ f_mn = 2πθ δ_mn." (§3). The script's docstring: "The explicit Laguerre form of f_mn used below is checked against the first two properties exactly (sympy), so it is not taken on trust."

**In the gate [V].** The section "Anchors: the explicit matrix base" of `verify/toy_gw.py` checks:

- "H * f_mn = theta (m+1/2) f_mn for m, n <= 2 (exact)" and the same from the right, computed symbolically with the exact star product of H (for a quadratic function the series stops at second order; see [the star product](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/noncommutative-field-theory#the-star-product));
- "f_00 = 2 exp(-x^2/theta) as in 0709.3950 (A.2)", the literature value;
- orthogonality on a numerical grid, "int conj(f_kl) f_mn = 2 pi theta delta delta", with "max dev 4.6e-14", and "int f_mn = 2 pi theta delta_mn".

The two grid checks assert deviations below 1e-8.

**By the referee.** The round-4 referee rebuilt the base from its own starting points: a differential Moyal product with [x₁, x₂]⋆ = i at θ = 1, an integral form of the star product whose sign was fixed against the derivative series, Weyl symbols built from Hermite functions, and Grosse and Wulkenhaar's eq. 1 read from the source (audit notes, Step 2(b)). Its results:

- the Laguerre form against the exact eigen-relations for m, n ≤ 3: "True";
- the kernel's sign, compared with the derivative series taken to tenth order, at θ = 1/5 on off-centre Gaussians: "sigma=+1: |diff| 3.34e-09; sigma=-1: 1.77e-02", so only one sign reproduces the product;
- f_mn ⋆ f_kl = δ_nk f_ml by exact Gaussian integrals over 20 index sets: "max error 2.97e-140";
- the Laguerre f_mn against "Weyl symbol of |m><n|" from Hermite functions: "max error 5.63e-14 (m,n<=3)";
- ∫ f_mn and orthogonality: "errors 0.0 (exact)".

## The kinetic form at Ω = 1

```text
∫ ( |∂φ|² + x̃²|φ|² ) d²x  =  8π Σ_mn (m + n + 1) |φ_mn|²        x̃ = 2θ⁻¹x
```

"The Ω = 1 quadratic form ∫ |∂φ|² + x̃²|φ|² equals 8π(m + n + 1)|φ_mn|², diagonal, computed with exact derivatives." (§3) [V].

**Why it is diagonal.** At Ω = 1 the operator −∂² + x̃² is proportional to the sum of left and right star-multiplication by H [T]; this follows from the exact products H ⋆ g and g ⋆ H that the script uses, whose middle terms cancel in the sum. Each f_mn is then an eigenfunction, with eigenvalue proportional to (m + ½) + (n + ½) = m + n + 1. The coefficient m + n + 1 is the sum of the two oscillator energies of the entry, in units of θ. Away from Ω = 1 the gradient and oscillator terms no longer combine this way. The note does not rely on the argument; it computed the form directly.

**The check [V].** The gate's section "The Omega = 1 kinetic form in the matrix base" builds the quadratic form for m, n < 4 from symbolic derivatives evaluated on the grid and prints "max off-diag 1.7e-14" and "ratio 25.1327 (8 pi = 25.1327)". The referee's exact computation: "off-diagonal max 0.0; diagonal/(8 pi) = m+n+1 for all m,n<=2 (exact)" (audit notes, Step 2(b)).

**The finite-difference episode.** The worklog: "A first check used finite-difference derivatives and failed at the 0.3% level. The fix was exact derivatives, not a looser tolerance." ('Chunk 2 results'). The check that failed was not loosened; the method was replaced, as the program's rule for its gate requires ([the gate](/wiki/method/verification/the-gate)).

**A predicted error site.** The round-4 pre-registration listed "the 8π(m+n+1) coefficient" among the likeliest places for a surviving numerical error ([pre-registration](/wiki/method/review/pre-registration); `review/round4-preregistration.md`). The adjudication scored the outcome: "Every normalization and sign I listed was confirmed" ('Pre-registration scored').

## The action

**Complex fields.** "In units where the kinetic coefficient is 1" (§3):

```text
S[φ] = Σ_mn (m + n + 1 − μ²) |φ_mn|² + λ Tr((φ†φ)²)
```

Here † is the Hermitian adjoint of the matrix, not the citation mark. The first term is the kinetic form above, with its 8π divided out, plus a mass term −μ²|φ_mn|². Its sign is negative for μ² > 0, so an entry whose oscillator energy m + n + 1 lies below μ² has a negative quadratic coefficient and lowers the action by growing, until the quartic term stops it; this is how the vacua condense ([complex-model vacua](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/complex-vacua)). The quartic term is the matrix form of the star-product interaction ∫ φ̄ ⋆ φ ⋆ φ̄ ⋆ φ, with φ̄ the complex-conjugate field, whose matrix is φ† [T]. The quadratic term depends only on the magnitudes |φ_mn|², and the quartic term is a trace, unchanged when φ†φ is conjugated by a unitary matrix, so the action is unchanged when the rows and columns of φ are multiplied by phases: "It satisfies S[UφV†] = S[φ] for all diagonal unitaries U, V." (§3). See [complex versus real fields](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/complex-and-real-fields).

**Real fields.** A field that is real on the plane has φ_nm equal to the complex conjugate of φ_mn, because f_mn and f_nm are complex conjugates; its matrix is Hermitian [T]. The quadratic term keeps its form, and the quartic term becomes Tr φ⁴, the matrix form of ∫ φ ⋆ φ ⋆ φ ⋆ φ. The worklog noted in chunk 1 what this implies for the vacua: "At Ω = 1 the matrix-base action depends on φ only through φ² (the kinetic term is 2 Tr(Eφ²) with E diagonal; checked against de Goursac–Tanasa–Wallet eqs. 3.16, 3.26). With distinct level energies, every minimum is then diagonal, φ = diag(±√q_m) over the condensed levels." ('Chunk 1 results'). Those are the sign-vacua of [the real model's one-loop preference](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/real-model-lead).

Whether the duality is a symmetry of these actions depends on the field: for a complex field it is, and for a real field "Πφ is not Hermitian, so the duality maps the real field space out of itself" (§3).

## The duality's normalization

The duality is taken from Grosse and Wulkenhaar's eq. 1, adapted to two dimensions: "the two-dimensional form of [6, eq. 1] — p = x̃ = 2θ⁻¹x and normalization π√|det θ| (the cited equation is the 4D form, with π²)" (§3). The gate fixes the normalization with an anchor, the Gaussian ground-state function mapped to itself: "anchor: D f_00 = f_00 (the normalization pi sqrt|det theta|)". The referee flagged that the first version of the note wrote π for π² without saying so ("(minor)", audit notes, Step 1); version 2 says so. The duality's action on the whole base is [the lemma](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/matrix-base-lemma).

## Where the inputs come from

The worklog records the sources of every input: "Inputs come from the sources: the matrix base from de Goursac–Tanasa–Wallet App. A; the duality from Grosse–Wulkenhaar hep-th/0402093 eq. 1" ('Chunk 2 results'); the script's docstring says "Inputs taken from the sources, not from memory". The rule followed from chunk 1, where conventions recalled from memory could not be reconciled with Grosse and Wulkenhaar's stated invariance: "So a recalled convention is wrong somewhere." ('Chunk 1 results'). The episode is told on [the duality on the matrix base](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/matrix-base-lemma#how-the-result-was-found).

## What is built on it

- [The duality on the matrix base](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/matrix-base-lemma): D f_mn = (−1)^m f_mn.
- [Complex versus real fields](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/complex-and-real-fields): symmetry for complex fields, covariance for real ones.
- [Complex-model vacua and the polarization Δ(β)](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/complex-vacua): the condensed vacua and their flat angle.
- [Quantum restoration in the complex model](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/quantum-restoration): why the classical breaking does not survive.
- [Open: the real model's one-loop preference](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/real-model-lead): the real model's sign-vacua, split at one loop.

## Sources

- `papers/reciprocity-toy-models.md` §3 — the matrix base, its Laguerre form and checks, the kinetic form, the actions, the duality's normalization
- `verify/toy_gw.py` — the docstring's inputs and the "Anchors" and "Omega = 1 kinetic form" sections, with their printed deviations and the normalization anchor
- `review/round4/referee/audit-notes.md` Step 1, Step 2(b) — the ladder functions as transcribed from the source; the π² adaptation; the referee's independent construction and its measured deviations
- `review/round4/referee/out_model2_base.txt` — the referee's printed anchors, including the kernel-sign test
- `review/round4-preregistration.md` 'Predictions'; `review/round4-adjudication.md` 'Pre-registration scored' — the 8π(m + n + 1) coefficient as a predicted error site, and its confirmation
- `notes/toy-lagrangian.md` 'Chunk 1 results', 'Chunk 2 results' — the real action's dependence on φ², the sources of the inputs, the finite-difference episode
