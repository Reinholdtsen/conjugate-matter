---
title: "The duality on the matrix base"
weight: 30
status: alive
description: "By direct numerical Fourier integration the Langmann–Szabo duality is left multiplication by parity, D f_mn = (−1)^m f_mn, recorded as a lemma crediting Grosse–Wulkenhaar, Royer and Langmann–Szabo."
provenance: [V]
sources:
  - "papers/reciprocity-toy-models.md §3 'Lemma'"
  - "verify/toy_gw.py"
  - "review/round4-adjudication.md 'Revisions' 3"
  - "review/round4/referee/audit-notes.md Step 1"
  - "review/round4/referee/audit-notes.md Step 2(b)"
  - "review/round4/referee/audit-notes.md Step 3"
  - "review/round4/referee/out_model2_base.txt"
  - "notes/toy-lagrangian.md 'Chunk 1 results'"
  - "notes/toy-lagrangian.md 'Chunk 2 results'"
---

*The lemma states how the Langmann–Szabo duality acts on the matrix-base functions f_mn of [model II](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar): it multiplies each one by (−1)^m, a sign fixed by its left index alone. The duality is a Fourier transform of the field, which exchanges its position profile with its momentum profile, and on this basis it reduces to parity, the reflection that leaves the even oscillator levels unchanged and reverses the sign of the odd ones, applied to the left index of the field's matrix. Because Grosse and Wulkenhaar alternate the sign of the Fourier exponent from one factor of the interaction to the next, parity acts on the left index of one factor and on the right index of the next. The result came from a direct numerical Fourier integration, which settled a clash between conventions recalled from memory. The round-4 referee confirmed it and judged it correct but not new, and the note's second version presents it as a lemma credited to the work it follows from. The rest of model II turns on it.*

**Status:** Alive — [V]: `verify/toy_gw.py` checks "D f_mn = (-1)^m f_mn for all m, n < 4: the duality is left multiplication by parity" ([the toy-model scripts](/wiki/method/verification/toy-model-scripts)). The referee of [review round 4](/wiki/method/review/round-4) confirmed it with exact integrals at θ = 1, 1/2 and 3 and called it "Correct, but not a new structural fact"; version 2 credits Grosse–Wulkenhaar, Royer and Langmann–Szabo.

## Statement

```text
D f(x) = (πθ)⁻¹ ∫ d²y e^{−i x̃·y} f(y),        x̃ = 2θ⁻¹x

D f_mn = (−1)^m f_mn        for m, n < 4, to ≲ 10⁻¹¹
with the opposite sign of the exponent:   f_mn → (−1)^n f_mn
```

The [toy-model note](/wiki/symmetry-breaking/toy-models), §3: "**Result:** D f_mn = (−1)^m f_mn for m, n < 4, to ≲ 10⁻¹¹. The opposite sign of the exponent gives (−1)^n." Here f_mn are the functions of [the matrix base](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/model-and-matrix-base) of the Moyal plane [x₁, x₂] = iθ, the Weyl symbols of the oscillator operators |m⟩⟨n|.

## The map

The note takes the duality from Grosse and Wulkenhaar: "With the two-dimensional form of [6, eq. 1] — p = x̃ = 2θ⁻¹x and normalization π√|det θ| (the cited equation is the 4D form, with π²) — we implement D f(x) = (πθ)⁻¹ ∫ d²y e^{−i x̃·y} f(y) by direct numerical integration." (§3). D is a [Fourier transform](/wiki/phase-space/reciprocity/fourier-transform) of the field over the whole plane. It takes the field's profile in position to its profile in momentum, and reads the momentum at the point x̃ = 2θ⁻¹x, which is how the Langmann–Szabo duality identifies momenta with positions ([noncommutative field theory](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/noncommutative-field-theory#the-langmannszabo-duality)).

In `verify/toy_gw.py`, with θ the antisymmetric matrix whose off-diagonal entry is θ₁₂ = θ = 1 (the code's comment: "xtilde = 2 theta^-1 x, theta_12 = theta"), the dual coordinate is x̃ = (−2x₂, 2x₁). The exponent is then −2i(x₁y₂ − x₂y₁): the kernel is built from the [symplectic product](/wiki/phase-space/reciprocity/symplectic-form) of the two points, x₁y₂ − x₂y₁, rather than from the ordinary dot product.

The normalization is fixed by an anchor: D leaves the Gaussian f₀₀, the oscillator ground state, unchanged. The gate prints the check as "anchor: D f_00 = f_00 (the normalization pi sqrt|det theta|)".

## Precision

The deviation is quoted three ways, two measured values and the looser tolerance the gate asserts, and the three are consistent:

- version 2 of the note: "to ≲ 10⁻¹¹" (§3);
- the worklog: "to 1.4×10⁻¹²" ('Chunk 2 results'), which is also what the gate prints, "max dev 1.4e-12";
- the gate's assertion: a maximum deviation below 1e-7.

The gate computes D by direct summation on a grid and compares it with (−1)^m f_mn at sample points, for every pair m, n < 4. The round-4 referee computed the transform with exact Gaussian integrals instead and found "D_minus f_mn / f_mn == (-1)^m for all m,n<=3: True" for θ = 1, 1/2 and 3; its D₋ is the note's D, with the minus sign in the exponent. "The opposite sign of the exponent gives '(-1)^n: True'" (audit notes, Step 2(b)). The referee's printed ratios at θ = 1 show the pattern directly: +1 for every f₀ₙ and −1 for every f₁ₙ under D₋, and an alternation along each row under the opposite sign (`review/round4/referee/out_model2_base.txt`).

## What "left multiplication by parity" means

**On matrices.** A field φ = Σ φ_mn f_mn has the matrix (φ_mn). The lemma multiplies its m-th row by (−1)^m:

```text
Dφ = Πφ,        Π = diag(1, −1, 1, −1, …) = e^{−iπN},        N = diag(0, 1, 2, …)
```

The worklog: "It is left multiplication by parity, Π = e^{−iπN}." ('Chunk 2 results'). The opposite sign of the exponent multiplies the n-th column by (−1)^n instead, φ → φΠ: right multiplication.

**On operators** [T]. Since f_mn is the [Weyl symbol](/wiki/phase-space/reciprocity/wigner-function) of |m⟩⟨n|, the lemma says that D turns the symbol of an operator A into the symbol of the product P·A, where P is the parity operator of the oscillator, the reflection (x₁, x₂) → (−x₁, −x₂) of the plane, and P|m⟩ = (−1)^m|m⟩ because the m-th oscillator state has parity (−1)^m [T]. The opposite sign gives A·P. The round-4 referee: "the explicit parity form follows from the classical parity-operator representation of Weyl symbols", Royer's 1977 result that the Wigner function at a point is the expectation value of parity about that point (audit notes, Step 2(b); the note's ref. [16]; see [Royer's parity form](/wiki/phase-space/reciprocity/wigner-function)).

**Not a rotation.** D is a Fourier transform, but on this basis it does not act as a rotation of the plane. A rotation of the plane multiplies f_mn by a phase u_m ū_n and leaves the rotationally symmetric diagonal functions f_mm unchanged ([the matrix base](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/model-and-matrix-base#the-matrix-base)) [T]. D reverses the sign of every f_mm with odd m. The difference decided the question chunk 1 had left open (below): a duality of rotation type would leave the diagonal vacua of the model invariant, and parity does not.

## The alternation of Grosse and Wulkenhaar

Grosse and Wulkenhaar's duality does not use one sign of the exponent throughout. The round-4 referee found the convention in their paper: "phi^(p_a)=int e^{(-1)^a i p_a x_a} phi(x_a), 'a refers to the cyclic order in the star-product' -- CONFIRMED" (audit notes, Step 1). Successive fields of the interaction vertex get opposite signs. With the lemma, the note reads this off directly: "The duality is therefore parity acting on the left index for one factor and on the right for the next. That is the alternation of [6], and is consistent with the parity-operator form of Weyl symbols [16]." (§3).

The alternation is what makes the quartic interaction come back to itself. For any four matrices M₁, M₂, M₃, M₄, transforming them alternately on the left and on the right gives Tr((ΠM₁)(M₂Π)(ΠM₃)(M₄Π)) = Tr(M₁M₂M₃M₄), since Π² = 1 and the trace is cyclic. Grosse and Wulkenhaar's statement that the Ω = 1 action is invariant and the lemma agree. What the alternation means for a field that must stay real is the subject of [complex versus real fields](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/complex-and-real-fields).

## Credit and novelty

The note's first version presented the matrix-base form as its own computation. The round-4 referee: correct, "but GW (hep-th/0401128) already say the duality is 'manifest' in the matrix base; the explicit parity form follows from the classical parity-operator representation of Weyl symbols … Correct, but not a new structural fact." (audit notes, Step 2(b); GW is Grosse–Wulkenhaar). Its conceptual audit asked for the result to be presented "as a lemma" (Step 3). The adjudication's revision 3: "Present the matrix-base duality as a lemma, crediting Grosse–Wulkenhaar (manifest in the matrix base), Royer (the parity form) and Langmann–Szabo (the complex formulation)." ([review round 4](/wiki/method/review/round-4)).

Version 2 does so: "Grosse and Wulkenhaar already note that the duality is manifest in the matrix base [6b]; we record the explicit form because the rest of the analysis turns on it." (§3). Royer's paper is ref. [16], added in version 2 and, with the other four new references, "all retrieved" (worklog, 'Write-up and review').

## How the result was found

**Chunk 1: the question.** The worklog's route decision tested the Grosse–Wulkenhaar model first and found that everything hinged on how the duality acts on the matrix base ('Chunk 1 results'):

- "**If** the duality multiplies the diagonal functions f_mm by (−1)^m, no ground state is duality-invariant once two levels condense (μ²θ > 12). That would be spontaneous breaking of x ↔ p, with the vacuum sharp in x for one sign pattern and sharp in p for its image."
- "**If** it acts as a diagonal phase rotation (u_m ū_n), the diagonal vacua are invariant, and this route gives no classical breaking."

The condition μ²θ > 12 is stated in Grosse and Wulkenhaar's units (worklog, 'Chunk 2 results'); the note's computations, in its own units, take μ² = 4, where levels 0 and 1 are condensed.

**Chunk 1: the clash.** "My recalled Fourier eigenvalues ((−i)^{m+n}, or (−1)^m with the B rotation) are not of rotation type. But with them I cannot make the quartic term invariant, which contradicts Grosse–Wulkenhaar's stated invariance. So a recalled convention is wrong somewhere." The worklog marked it "**Unresolved, not a finding.**" and planned the next step: "Compute numerically the Langmann–Szabo map on the f_mn functions (2D Fourier transform plus rescaling, projected back onto f_kl)."

**Chunk 2: the computation.** "The duality acts as D f_mn = (−1)^m f_mn [V], to 1.4×10⁻¹². This is a direct numerical 2D Fourier integral with Grosse–Wulkenhaar's kernel, not a recalled eigenvalue." The inputs came from the sources, the matrix base from de Goursac–Tanasa–Wallet and the duality from Grosse–Wulkenhaar's eq. 1 ('Chunk 2 results'). The apparent contradiction had a different cause from the eigenvalue: "Why it looked contradictory: Grosse–Wulkenhaar's duality alternates the sign of the Fourier exponent around the ⋆-vertex." A convention disputed from memory was settled by executed code, as the program's [iron rule](/wiki/method/verification/iron-rule) requires for disputed numbers.

## What turns on it

- **The vacua.** In the complex model the vacua are diagonal, with levels 0 and 1 condensed and a free relative phase β. Π multiplies the level-1 entry by −1 = e^{iπ}, so the duality shifts β by π, and no vacuum is invariant once level 1 condenses ([complex-model vacua](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/complex-vacua)). This is the first case of chunk 1.
- **Complex versus real.** For a complex field Πφ is another allowed field, and the duality is a symmetry; for a real field, a Hermitian matrix, Πφ is in general not Hermitian, and the duality leads out of the field space ([complex versus real fields](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/complex-and-real-fields)).
- **A continuous family.** Π = e^{−iπN} is the α = π member of the left phase rotations e^{−iαN}, all of which leave the complex action unchanged. The duality is therefore one point on a circle of symmetries, and the vacuum's polarization is an angle on that circle ([the polarization as a Goldstone angle](/wiki/symmetry-breaking/goldstone-angle)). The gate checks "the duality is the beta -> beta + pi element of the left phase rotations exp(-i alpha N)".

## Sources

- `papers/reciprocity-toy-models.md` §3 'Lemma' — the statement, the map, the parity reading, the alternation and the credit, quoted above
- `verify/toy_gw.py` — the gated lemma, its tolerance, the normalization anchor and the kernel as implemented
- `review/round4-adjudication.md` 'Revisions' 3 — the required lemma form and credits
- `review/round4/referee/audit-notes.md` Step 1, Step 2(b), Step 3 — the alternating sign found in the source; the exact confirmation at three values of θ; the novelty judgement and the request for a lemma
- `review/round4/referee/out_model2_base.txt` — the referee's printed ratios
- `notes/toy-lagrangian.md` 'Chunk 1 results', 'Chunk 2 results', 'Write-up and review' — the two cases, the convention clash and its resolution [V]; the v2 references "all retrieved"
