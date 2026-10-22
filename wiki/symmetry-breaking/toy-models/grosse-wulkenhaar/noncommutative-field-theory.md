---
title: "Noncommutative field theory and the Langmann–Szabo duality"
weight: 10
status: established
description: "The Moyal plane, its star product and matrix base; the Grosse–Wulkenhaar model and the Langmann–Szabo duality, which exchanges a field's position and momentum descriptions; the self-dual point Ω = 1, with its all-orders vanishing β-function in four dimensions."
provenance: [T]
sources:
  - "papers/reciprocity-toy-models.md §1"
  - "papers/reciprocity-toy-models.md §3"
  - "papers/reciprocity-toy-models.md §4"
  - "papers/reciprocity-toy-models.md refs [5]–[10]"
  - "review/round4/referee/audit-notes.md Step 1"
  - "review/round4/referee/audit-notes.md Step 2(c)"
  - "review/round4/referee/audit-notes.md Step 3"
  - "review/round4-adjudication.md 'Rulings'"
  - "verify/toy_gw.py"
  - "notes/toy-lagrangian.md 'Chunk 1 results'"
  - "notes/toy-lagrangian.md 'Chunk 2 results'"
---

*Noncommutative field theory places fields on a plane whose two coordinates do not commute, [x₁, x₂] = iθ: the plane behaves like the phase space of a quantum particle, with θ in the role of Planck's constant. Fields on it are multiplied with the Moyal star product, which builds that relation in. On this plane Langmann and Szabo found a duality that exchanges a field's description in position with its description in momentum. It is a [Fourier transform](/wiki/phase-space/reciprocity/fourier-transform) of the field, relating the two descriptions as a waveform is related to its spectrum. Grosse and Wulkenhaar's renormalizable model of a self-interacting scalar field is carried into itself by the duality at one value of its oscillator parameter, Ω = 1, and there its β-function vanishes to all orders in four dimensions. This literature supplied [model II](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar) of the program's toy models: an interacting field theory with an exact exchange of position and momentum, used to test whether a vacuum alone could break that exchange.*

**Status:** Established — literature [T]. The [toy-model note](/wiki/symmetry-breaking/toy-models) cites it as refs. [5]–[10] and marks none of them; the worklog's prior-art survey retrieved [5], [6a], [7] and [9] by live search [S], [8] and [10] are among the five references version 2 added ("all retrieved"), and [6b] has been cited since version 1. The referee of [review round 4](/wiki/method/review/round-4) resolved the version-1 references against INSPIRE records and arXiv sources and found [8] and [10] as omitted prior work. Explanations below that do not come from these papers are general knowledge [T], and any reference they add is marked †.

## The Moyal plane

The Moyal plane is the ordinary plane with coordinates (x₁, x₂) made noncommutative [T]:

```text
[x₁, x₂] = iθ
```

This is the [canonical commutator](/wiki/phase-space/reciprocity/canonical-commutator) [x, p] = iℏ with x₁ and x₂ in the roles of position and momentum and θ in the role of ℏ. The plane is therefore a quantum [phase space](/wiki/phase-space) treated as a space on which fields live. The toy-model note works on "the Moyal plane [x₁, x₂] = iθ (θ = 1)" (§3).

### The star product

Functions on the plane are multiplied with the Moyal star product ⋆ (Groenewold 1946†, Moyal 1949†), the product of [Weyl symbols](/wiki/phase-space/reciprocity/wigner-function) that represents the product of the operators they stand for [T]. To first order in θ,

```text
f ⋆ g = f g + (iθ/2)(∂₁f ∂₂g − ∂₂f ∂₁g) + (terms with more derivatives, each with a further power of θ)
```

The full series is an exponential of the derivative operator in the second term [T]. It is associative but not commutative, and its antisymmetric part gives back the commutator, x₁ ⋆ x₂ − x₂ ⋆ x₁ = iθ [T]. For a quadratic function the series ends after the second-order term. [The gate](/wiki/method/verification/the-gate) script `verify/toy_gw.py` ([the toy-model scripts](/wiki/method/verification/toy-model-scripts)) uses the exact product of the oscillator function H = ½x² with any g, "exact (the series stops at second order)":

```text
H ⋆ g = ½x² g + (iθ/2)(x₁∂₂g − x₂∂₁g) − (θ²/8)(∂₁² + ∂₂²) g
```

with the sign of the middle term reversed for g ⋆ H. Integrated over the plane, a star product of two functions equals the ordinary product, ∫ f ⋆ g = ∫ f g [T], so noncommutativity first shows in products of three or more fields, as in a quartic interaction. Such an interaction is nonlocal on the scale √θ: the star product spreads a product of fields over a cell of area of order θ [T].

### The matrix base

Because the plane is a phase space, it carries the harmonic oscillator, and the oscillator's states give a basis of functions f_mn in which the star product becomes multiplication of matrices [T]. The toy note takes the construction "as in [9, App. A]" (de Goursac, Tanasa and Wallet): f₀₀ = 2e^{−x²/θ}, f_mn built from it with ladder functions, and

```text
f_mn ⋆ f_kl = δ_nk f_ml        H ⋆ f_mn = θ(m + ½) f_mn        f_mn ⋆ H = θ(n + ½) f_mn
```

(§3). Each f_mn is the Weyl symbol of the oscillator operator |m⟩⟨n| [T]. The first relation says that a field φ = Σ φ_mn f_mn star-multiplies like the matrix (φ_mn), and because ∫ f_mn = 2πθ δ_mn (§3), the integral of a star product of fields is 2πθ times the trace of the product of their matrices [T]. A field theory on the Moyal plane is therefore a matrix model, and keeping the first N oscillator levels makes it a model of N × N matrices. The explicit functions, their checks and model II's action in this basis are on [Model II: the matrix base and the action](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/model-and-matrix-base).

## The Grosse–Wulkenhaar model

A self-interacting scalar field on the Moyal plane, with a gradient term, a mass term and a star-product quartic interaction, is not renormalizable as it stands in four dimensions [T]. The nonlocality of the star product feeds the ultraviolet divergences of loop diagrams back into singular behaviour at long wavelengths, an effect called UV/IR mixing (Minwalla, Van Raamsdonk and Seiberg 2000†). Grosse and Wulkenhaar added a harmonic-oscillator term to the kinetic term [T], so that the quadratic part of the action reads

```text
∫ ( |∂φ|² + Ω² x̃² |φ|² )  + mass term,        x̃ = 2θ⁻¹x
```

where Ω is the oscillator frequency and x̃ is the position rescaled by the noncommutativity, the "p = x̃ = 2θ⁻¹x" of the toy note (§3). With this term the model is renormalizable to all orders of perturbation theory in four dimensions [T]; the paper that proves it is, by its title, the note's ref. [6b], "Renormalisation of φ⁴-theory on noncommutative ℝ⁴ in the matrix base". The oscillator term confines the field around the origin and breaks translation invariance [T]. At Ω = 1 the toy note's quadratic form is "∫ |∂φ|² + x̃²|φ|²" (§3).

## The Langmann–Szabo duality

A Fourier transform turns a gradient into multiplication by momentum, and multiplication by position into a gradient [T] (see [the Fourier transform as a phase-space rotation](/wiki/phase-space/reciprocity/fourier-transform)). On the Moyal plane momenta can be identified with positions through θ, p = x̃ = 2θ⁻¹x. Replacing a field by its Fourier transform, read at that identification, therefore carries the gradient term ∫|∂φ|² into an oscillator term and the oscillator term into a gradient term [T]. Langmann and Szabo showed that the star-product interaction keeps its form under the same exchange, so the whole theory is mapped into a theory of the same type [T]. In the toy note's words: "Langmann and Szabo found a duality of noncommutative scalar field theory that exchanges positions and momenta, formulated for complex fields [5]." (§1).

The round-4 referee read the original paper (audit notes, Step 1). Langmann and Szabo formulate the duality "for a complex field in a magnetic field" (capitals lowered here), keep both quartic vertices of a complex field, the orderings Φ†ΦΦ†Φ and Φ†Φ†ΦΦ with separate couplings α and β (here † is the Hermitian adjoint, not the citation mark), and write the duality "as a single Fourier map" (their Prop. 1), under which the noncommutativity θ goes over to −B⁻¹θ⁻¹B⁻¹, with B the magnetic field. The referee's conclusion: "The complex-field framing is [Langmann and Szabo's] original".

### The self-dual point

In the standard presentation the duality relates the model at oscillator frequency Ω to the model at 1/Ω, with rescaled mass and coupling [T] (general knowledge; the program's documents do not state it). This is why Grosse and Wulkenhaar call their theory "duality-covariant", in the title of [6a], "The β-function in duality-covariant noncommutative φ⁴-theory". At Ω = 1 the gradient and oscillator terms carry equal weight, and the model is carried into itself: "The Grosse–Wulkenhaar model is invariant under it at Ω = 1 [6]" (toy note §1). Two details of Grosse and Wulkenhaar's convention matter for the program, both confirmed in their paper by the round-4 referee (audit notes, Step 1):

- **The normalization.** Their eq. 1 relates φ̂(p) to π²√|det θ| φ(x), the four-dimensional form; the note uses "the two-dimensional form of [6, eq. 1] — p = x̃ = 2θ⁻¹x and normalization π√|det θ| (the cited equation is the 4D form, with π²)" (§3).
- **The alternating sign.** The sign of the Fourier exponent alternates from one field of the quartic vertex to the next: "phi^(p_a)=int e^{(-1)^a i p_a x_a} phi(x_a), 'a refers to the cyclic order in the star-product' -- CONFIRMED". In the matrix base this becomes parity acting on the left index of one factor and the right index of the next; see [the duality on the matrix base](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/matrix-base-lemma).

Grosse and Wulkenhaar state that the real Ω = 1 action "is invariant under the duality". The toy note reads the same algebra differently, as a covariance of the real model and a symmetry of the complex one; the referee called that reading "its own reinterpretation" (audit notes, Step 1). See [complex versus real fields](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/complex-and-real-fields).

### A vanishing β-function

A β-function gives the rate at which a coupling changes with the energy scale at which it is measured [T]. In ordinary φ⁴ theory in four dimensions the quartic coupling grows at short distances [T]. At the self-dual point of the Grosse–Wulkenhaar model it does not change, to all orders of perturbation theory: the model has "an all-orders vanishing β-function in 4D [7]" (toy note §1). The round-4 referee found the statement in the source, Disertori, Gurau, Magnen and Rivasseau: "we compute the flow at the special [Langmann–Szabo] dual point Omega=1, and check that the beta function vanishes at all orders" (audit notes, Step 1, with the referee's abbreviation written out). The worklog's reason for choosing the model rests on this pedigree: "an interacting, renormalizable field whose own vacuum might select x or p, with no K put in by hand" ('Chunk 1 results').

## What the literature had studied

The note's survey of prior work: "A closely related model is exactly solvable [8]. Non-constant vacua at Ω = 1 [9], and minima of the complex self-dual planar model [10], have been studied, but not their behaviour under the duality." (§1).

- **Non-constant vacua** (de Goursac, Tanasa and Wallet [9]). The worklog: they "find non-constant vacua at Ω = 1 for μ² ≥ 4/θ" ('Chunk 1 results'). The referee recorded their forms: for the complex model "a f_{m0 n0}", for the real model "sum_k a_k f_kk, a_k^2=(mu^2 theta/4-2k-1)/(lambda theta)", and found that "'duality' appears only in the set-up (l.359-364): breaking not examined -- CONFIRMED" (audit notes, Step 1). They describe the vacuum as one that "decays at infinity", a "finite linear combination of Schwartz functions" (as the referee quotes them, Step 2(c)): a localized lump, which matters for [quantum restoration](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/quantum-restoration).
- **One-loop effects around the minima** (Fosco and Moreno [10]). The referee: the complex self-dual model, "quantum effects around non-trivial (U(1)-breaking) minima; does not examine duality breaking (grep)" (audit notes, Step 1).
- **An exact solution** (Langmann, Szabo and Zarembo [8]). The referee: an "exact solution of the complex model at a special self-dual point (U(infty) degeneracies); [Grosse and Wulkenhaar] themselves cite it as 'closely related' to the Omega=1 model. Directly relevant to Sec. 4 restoration claim." (audit notes, Step 1). Version 2 calls it "the natural independent check" of its restoration argument and has not carried it out (§4).
- **Stripes.** "Stripe phases in this literature break translations, not x ↔ p." (worklog, 'Chunk 1 results').

The referee's own searches of INSPIRE full text "found no prior explicit model with [Langmann–Szabo] duality spontaneously broken by vacua" (audit notes, Step 1).

## Locality in this literature

The program's question is why physical interactions are local in position and not in momentum ([Born's question](/wiki/program/borns-question)). The worklog's survey quotes Langmann and Szabo on that point: at θ = 0 the position vertex is "fully local" and the momentum vertex non-local; "for non-singular θ, both vertex functions have the same non-local form". Its reading: "In that literature, locality in x arises only at the singular θ → 0 limit, not from a vacuum." ('Chunk 1 results').

## Four dimensions and two

The literature results above are four-dimensional: Grosse and Wulkenhaar's eq. 1 carries π², the vanishing β-function is for the four-dimensional model, and the referee noted of the Disertori–Gurau–Magnen–Rivasseau result that "This is the 4D model; model II is 2D" (audit notes, Step 1). Model II is the two-dimensional version, on a Moyal plane with θ = 1, so these results are its pedigree, not properties it inherits. The round-4 adjudication accepted the citation fixes, including "GW eq. 1 is the 4D form (π²)" and "[5] is about 4D" ('Rulings', Citations; there GW means Grosse–Wulkenhaar, and [5] is the version-1 number of the Disertori–Gurau–Magnen–Rivasseau paper).

## How the program uses it

The worklog's route decision, made by Claude under Paul's delegation ([the collaboration](/wiki/method/collaboration)), tried this model first: "It is the one place where the toy could be both new and non-trivial: an interacting, renormalizable field whose own vacuum might select x or p, with no K put in by hand." ('Chunk 1 results'). Model II takes the two-dimensional self-dual model, writes it on the matrix base, computes the duality there, and asks whether the vacua break it. For complex fields they do, classically, and quantization restores the symmetry; for real fields the duality is only a covariance, and one loop prefers the vacuum that is sharper in position. The section index, [Model II: the self-dual Grosse–Wulkenhaar model](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar), maps the results.

## Standard references

The toy note's references, as it lists them (marks as described in the status line):

- [5] E. Langmann, R. J. Szabo, "Duality in scalar field theory on noncommutative phase spaces," Phys. Lett. B 533, 168 (2002), hep-th/0202039.
- [6] H. Grosse, R. Wulkenhaar: (a) "The β-function in duality-covariant noncommutative φ⁴-theory," Eur. Phys. J. C 35, 277 (2004), hep-th/0402093; (b) "Renormalisation of φ⁴-theory on noncommutative ℝ⁴ in the matrix base," Commun. Math. Phys. 256, 305 (2005), hep-th/0401128.
- [7] M. Disertori, R. Gurau, J. Magnen, V. Rivasseau, "Vanishing of beta function of non-commutative φ⁴₄ theory to all orders," Phys. Lett. B 649, 95 (2007), hep-th/0612251.
- [8] E. Langmann, R. J. Szabo, K. Zarembo, "Exact solution of quantum field theory on noncommutative phase spaces," JHEP 01 (2004) 017, hep-th/0308043.
- [9] A. de Goursac, A. Tanasa, J.-C. Wallet, "Vacuum configurations for renormalizable non-commutative scalar models," Eur. Phys. J. C 53, 459 (2008), arXiv:0709.3950.
- [10] C. D. Fosco, G. A. Moreno, "One-loop effects in a self-dual planar noncommutative theory," JHEP 11 (2007) 046, arXiv:0710.0818.

Added by the wiki from model memory (†); the program's documents do not cite them:

- H. J. Groenewold (1946)† and J. E. Moyal (1949)†: the star product.
- S. Minwalla, M. Van Raamsdonk, N. Seiberg (2000)†: UV/IR mixing in noncommutative field theory.
- M. R. Douglas, N. A. Nekrasov (2001)† and R. J. Szabo (2003)†: reviews of noncommutative field theory.

## Used by

- [Model II: the matrix base and the action](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/model-and-matrix-base) — the matrix base and the Ω = 1 kinetic form.
- [The duality on the matrix base](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/matrix-base-lemma) — the duality's explicit action on f_mn, and the alternating sign.
- [Complex versus real fields](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/complex-and-real-fields) — symmetry for complex fields, covariance for real ones.
- [Complex-model vacua and the polarization Δ(β)](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/complex-vacua) — the condensed vacua and their cos β polarization.
- [Quantum restoration in the complex model](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/quantum-restoration) — why the classical breaking does not survive; the exact solution not yet compared.
- [Open: the real model's one-loop preference](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/real-model-lead) — the real model's one-loop split.
- [Open: forced locality and the P4 lock](/wiki/symmetry-breaking/strong-locality) — Langmann and Szabo on where locality in x comes from.
- [Success criteria S0–S5](/wiki/symmetry-breaking/toy-models/success-criteria) — the route forecast for S5 and the prior-art survey that found this literature.

## Sources

- `papers/reciprocity-toy-models.md` §1, §3, §4, refs. [5]–[10] — the literature as version 2 states it; the Moyal plane, the matrix base and the duality's normalization; the uncompleted exact-solution check
- `review/round4/referee/audit-notes.md` Step 1 — the citation audit: Langmann and Szabo's complex formulation, the four-dimensional form of eq. 1, "invariant under the duality", the alternating sign, the vanishing β-function, the vacua of de Goursac–Tanasa–Wallet, the omitted Fosco–Moreno and Langmann–Szabo–Zarembo papers, the novelty searches
- `review/round4/referee/audit-notes.md` Step 2(c), Step 3 — the vacuum as a localized lump; "its own reinterpretation" assessed
- `review/round4-adjudication.md` 'Rulings' — the accepted citation fixes and omitted prior work
- `verify/toy_gw.py` — the exact star product H ⋆ g used in the matrix-base anchors
- `notes/toy-lagrangian.md` 'Chunk 1 results', 'Chunk 2 results' — the prior-art survey [S], the vacua at μ² ≥ 4/θ, the locality quotation, the route decision and the sources of the matrix base and the duality
