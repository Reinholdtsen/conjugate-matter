---
title: "Vielbein formulation and wedge potentials"
weight: 70
status: established
description: "Frames (vielbeins) as the first-order variables of gravity, and Hinterbichler–Rosen's interacting spin-2 potentials written as wedge products of two frames, ghost-free by construction — the form in which the program's tuning test passed."
provenance: [T]
sources:
  - "papers/broken-born-checkpoint-v2.md §7.2"
  - "papers/broken-born-checkpoint-v2.md §14 item 1"
  - "papers/broken-born-checkpoint-v2.md ref [12]"
  - "notes/debt1a-iii-tuning-test.md §2"
  - "notes/debt1a-iii-tuning-test.md §3"
  - "notes/debt1a-iii-tuning-test.md §4"
  - "notes/debt1a-iv-beta-coefficients.md §1"
  - "notes/debt1a-iv-beta-coefficients.md §5"
  - "notes/debt1a-ii-X-classification.md §3"
  - "notes/broken-born-theory.md 'Addendum (v0.5)'"
  - "HANDOFF.md §2"
---

*In the vielbein, or frame, formulation of gravity the basic variable is a frame field e: at each point of spacetime, a set of reference axes that are orthonormal by definition, from which the metric is built as a quadratic expression, g = eᵀηe. The program calls frames first-order variables and metrics, being quadratic in frames, second-order. Hinterbichler and Rosen showed that the [ghost-free](/wiki/gravity/spin-2-fields/ghosts) potentials coupling two spin-2 fields can be written as wedge products of the two frames: polynomials, with none of the matrix square roots that the same potentials need when written with metrics. The program's [tuning test](/wiki/gravity/tuning-test) passed only in this form: candidate mass potentials for the [momentum graviton X](/wiki/gravity/momentum-graviton) built from metrics [fail the ghost test](/wiki/gravity/tuning-test/metric-tier-failures), while the frame-built one lands in the ghost-free class. That the program's potential takes the frame form was selected for minimality and consistency rather than derived, which is [an open problem](/wiki/gravity/tuning-test/wedge-reduction).*

**Status:** Established — [T] — the Hinterbichler–Rosen construction is cited in the [checkpoint](/wiki/history/documents/checkpoint) as [12†], from model memory and not yet source-checked. The program's use of it, [the frame tier](/wiki/gravity/tuning-test/frame-tier), is tagged "[D — structural, resting on T]" in [#7](/wiki/history/documents/debt-1-notes) §3. No test of [the verification battery](/wiki/method/verification/battery) covers the frame tier, and the class was selected rather than derived: [Open: deriving the wedge sector from S_H (OP1)](/wiki/gravity/tuning-test/wedge-reduction).

## Frames and metrics

### The frame field

A frame, or vielbein, assigns to each point of spacetime d basis vectors, labelled by an index a, that are orthonormal with respect to a fixed constant matrix η_ab: the Minkowski metric in Lorentzian signature, the identity matrix in Euclidean signature [T]. This η_ab is the textbook symbol, unrelated to the program's neutral metric η on phase space. In four dimensions the frame is also called a vierbein or tetrad; the German words mean "many legs" and "four legs". Writing the frame components as a matrix e^a_μ, with a labelling the axes and μ the coordinates, the metric is

```text
g_μν = e^a_μ η_ab e^b_ν          in matrix form:   g = eᵀ η e
```

The metric is quadratic in the frame. The frame carries more than the metric. Rotating the axes at each point, e → Λe with Λ a local Lorentz transformation (a local rotation in Euclidean signature), leaves g unchanged, so a frame is a metric together with a choice of axes, and that choice is a gauge freedom [T].

### First-order and second-order, in the program's usage

Calc note #7 sorts the program's geometric objects into tiers by this degree. The frame is first-order; the metric, quadratic in frames, is second-order: "**J and E live on the same geometric tier** (first-order structures on the tangent, like the Born connection), while H = EᵀE is second-order" (#7 §3). Here J is [the polarization](/wiki/symmetry-breaking/order-parameter), E the frame of the [phase-space metric H](/wiki/phase-space/born-geometry/born-structures) (see below), and the connection is [the Born connection](/wiki/phase-space/born-geometry/born-connection). The two halves of the tuning test follow the same split: "metric-tier (second-order, H-coupled)" potentials (#7 §2) against frame-tier ones.

In [general relativity](/wiki/gravity/spin-2-fields/general-relativity) the phrase "first-order formalism" more often names actions in which the connection is varied independently of the frame or metric, as in the Palatini and Einstein–Cartan forms [T]. The program's documents use "first-order" for the degree of a variable in the frame, not for the order of derivatives.

## Massive and bimetric gravity in frame variables

### The square root in the metric form

The ghost-free potentials of massive and bimetric gravity, in metric variables, are built from the matrix square root √(g⁻¹f) of the two metrics g and f: the potential is a linear combination, with constant coefficients βₙ, of the [elementary symmetric polynomials](/wiki/gravity/spin-2-fields/elementary-symmetric-polynomials) eₙ of that matrix [T]. These are [de Rham–Gabadadze–Tolley (dRGT) massive gravity](/wiki/gravity/spin-2-fields/drgt-massive-gravity), with f fixed, and [Hassan–Rosen bimetric gravity](/wiki/gravity/spin-2-fields/hassan-rosen-bimetric), with f dynamical. The square root makes the metric form awkward: it is defined through the eigenvalues of g⁻¹f, and for Lorentzian metrics a real square root need not exist [T].

### Frames remove the square root

Give each metric a frame: e for g and, following calc note #8's notation, f for the second metric (#8 §1 uses the letter f for both the second frame and its metric):

```text
g_μν = e^a_μ η_ab e^b_ν           f_μν = f^a_μ η_ab f^b_ν
```

If the frames satisfy the symmetry condition that e^a_μ η_ab f^b_ν is symmetric in μ and ν, then g⁻¹f = (e⁻¹f)², with e⁻¹f the matrix product of the inverse first frame and the second frame [T]. The square root is then a product of frames:

```text
√(g⁻¹f) = e⁻¹f          (when e^a_μ η_ab f^b_ν is symmetric in μν)
```

### Wedge products

With the frames written as one-forms, e^a = e^a_μ dx^μ, the potential can be written as a sum of wedge products. In four dimensions the n-th term contracts 4 − n copies of e and n copies of f with the totally antisymmetric symbol ε_abcd [T]:

```text
ε_abcd e^a ∧ e^b ∧ e^c ∧ e^d,    ε_abcd e^a ∧ e^b ∧ e^c ∧ f^d,    …,    ε_abcd f^a ∧ f^b ∧ f^c ∧ f^d
```

Each wedge product equals a constant times det(e) eₙ(e⁻¹f) d⁴x. Under the symmetry condition, det(e) is ±√|g| and e⁻¹f = √(g⁻¹f), so the n-th wedge product is, up to a constant, the n-th term √|g| eₙ(√(g⁻¹f)) of the metric potential [T]. The wedge products are polynomials in the components of the two frames. Calc note #7: "In vielbein variables the ghost-free potentials are polynomial — wedge products ε(e ∧ … ∧ f ∧ …) of two frames (Hinterbichler–Rosen) [T] — with no square roots and no tuning to miss" (#7 §3).

### Ghost-free by construction

Hinterbichler and Rosen built interacting spin-2 theories from such wedge products of frames [12†]; for two frames they are the frame form of the dRGT and Hassan–Rosen potentials [T]. Every wedge term is admissible, so no coefficient has to be tuned to keep the Boulware–Deser ghost, a mode whose energy has the wrong sign, out of the theory ([the Fierz–Pauli mass term and the Boulware–Deser ghost](/wiki/gravity/spin-2-fields/fierz-pauli)). Calc note #7 summarizes the class as "ghost-free by construction, Fierz–Pauli automatic, dRGT structure inherited rather than tuned" (#7 §3). The metric-language counterpart is calc note #6's criterion: "Massive spin-2 coupled to gravity has exactly one known consistent structure: the Fierz–Pauli tuning at quadratic order completed by a dRGT/Hassan–Rosen-class potential [T: HR 2011]" (#6 §3).

The checkpoint's entry for the work (#11, reference list):

- [12]† K. Hinterbichler, R. A. Rosen, "Interacting spin-2 fields," JHEP 1207, 047 (2012), arXiv:1203.5783.

Calc note #7 cites the construction as [T] and #8 names it, neither with a reference entry; #11 supplies the entry and marks it †, cited from model memory. Checking every † reference against its source is open problem 10 of #11 §14, [the † literature battery (OP10)](/wiki/method/literature-battery).

## The program's frame tier

### The symplectic vielbein and the polarization frame

The program's phase-space metric H, a point of [the Siegel domain](/wiki/phase-space/modular-field/siegel-domain) Sp(2d, ℝ)/U(d), has a frame of its own: "the symplectic vielbein E, the coset representative with H = EᵀE" (#7 §3). It is the Euclidean form of g = eᵀηe, with the identity in place of η. The polarization J, the real structure (an involution, J² = 1) that the vacuum selects ([the order parameter: J, η and K](/wiki/symmetry-breaking/order-parameter); [the structures ω, η, H](/wiki/phase-space/born-geometry/born-structures)), supplies a second frame, the polarization frame E₀[J] (#11 §7.2). The documents name E₀[J] without writing out its form.

### The tier argument

Calc note #7 argues from the tiers to the coupling:

> **J and E live on the same geometric tier** (first-order structures on the tangent, like the Born connection), while H = EᵀE is second-order. The geometrically minimal coupling of the polarization to the modular sector is therefore E-linear — wedge polynomials of (E, E₀[J]) — which is *precisely* the Hinterbichler–Rosen class: ghost-free by construction, Fierz–Pauli automatic, dRGT structure inherited rather than tuned. (#7 §3)

The checkpoint restates it: "*Frame-tier* couplings — wedge polynomials of the symplectic vielbein E (H = EᵀE) with the polarization frame E₀[J] — are the Hinterbichler–Rosen class [12†], ghost-free by construction; J, E, and the Born connection share the first-order tier, so this is the geometrically minimal formulation" (#11 §7.2). The argument classifies the objects by tier and then takes the minimal coupling at the frame tier. That the program's potential is this minimal coupling is a choice, made for minimality and consistency (#8 §5).

### The verdict of the tuning test

Potentials built at the metric tier failed twice ([the metric tier fails twice](/wiki/gravity/tuning-test/metric-tier-failures)): at quadratic order they give the graviton a mass with no Fierz–Pauli trace term (battery test T4), and their nonlinear structure lies outside the linear-in-eₙ family (#7 §2; battery test T7 checks the power sum p₄). The frame tier passes. Calc note #7: "The rescue is not a tuning but a *tier change*" (#7 §3). The [lab notebook](/wiki/history/documents/lab-notebook) states the verdict as "**the theory passes iff formulated in first-order variables, which is the formulation the geometry prefers anyway.**" (#1 'Addendum (v0.5)'), and the [handoff](/wiki/history/documents/handoff) repeats it (HANDOFF §2). See [the verdict: a conditional pass](/wiki/gravity/tuning-test/conditional-pass).

### What the pass delivers

A pass did not yet fix the potential's coefficients: "What a pass does **not** yet deliver: the βₙ coefficients" (#7 §3). Calc note #8 writes the frame-tier sector as a Hassan–Rosen potential for the two frames, "The Hinterbichler–Rosen sector for (e, f = E₀[J]) is V = 2m²M² Σₙ₌₀⁴ βₙ eₙ(𝕏), 𝕏 = √(g⁻¹f), with the exchange identity Sₙ(g,f) = S₄₋ₙ(f,g)" (#8 §1), and takes [Born reciprocity](/wiki/phase-space/reciprocity/born-reciprocity) to act on it as an exchange of the two frames, which forces [the palindrome βₙ = β₄₋ₙ](/wiki/gravity/palindromic-branch/palindrome). Because J carries only compact moduli, the second frame cannot range over all metrics: the result is "**Hassan–Rosen bimetric gravity with the second frame constrained to a compact moduli space Λ(d)**" (#7 §4), with Λ(d) [the Lagrangian Grassmannian](/wiki/phase-space/modular-field/lagrangian-grassmannian); this is [constrained bimetric gravity](/wiki/gravity/tuning-test/constrained-bimetric).

### Status of the program's use

- **Tag.** The frame tier is "[D — structural, resting on T]" (#7 §3). The checkpoint tags its §7.2 [D][V], but the machine checks there are the block algebra (battery T3) and the metric-tier failures (T4, T7); no test covers the frame tier, so the wiki tags it [D] ([conflicts between sources](/wiki/history/documents/source-conflicts); [the verification battery](/wiki/method/verification/battery)).
- **Selected, not derived.** Calc note #8 lists among [Debt 1](/wiki/history/debts)'s open residue "(i) first-principles reduction of the symplectic-vielbein wedge sector from S_H (the class was selected by minimality + consistency, not derived line-by-line)" (#8 §5). It is item 1 of the checkpoint's open problems: "First-principles reduction of the frame-tier wedge sector from S_H (class selected, not derived) [O]" (#11 §14). Here S_H is the program's geometric action ([the geometric action S_H](/wiki/gravity/tuning-test/geometric-action)). The open problem has its own page: [Open: deriving the wedge sector from S_H (OP1)](/wiki/gravity/tuning-test/wedge-reduction).

## Standard references

- [12]† K. Hinterbichler, R. A. Rosen, "Interacting spin-2 fields," JHEP 1207, 047 (2012), arXiv:1203.5783 — cited by #11.
- C. W. Misner, K. S. Thorne, J. A. Wheeler, *Gravitation* (1973)†: orthonormal frames (tetrads) in general relativity. Added by the wiki from model memory.

## Used by

- [The frame tier: the symplectic vielbein](/wiki/gravity/tuning-test/frame-tier) — the formulation in which the potential passes.
- [The verdict: a conditional pass](/wiki/gravity/tuning-test/conditional-pass) — the theory passes iff written in first-order variables.
- [Open: deriving the wedge sector from S_H (OP1)](/wiki/gravity/tuning-test/wedge-reduction) — the class was selected, not derived.
- [Constrained bimetric gravity](/wiki/gravity/tuning-test/constrained-bimetric) — the second frame confined to the compact space Λ(d).
- [Open: τ–Stückelberg mixing (OP6)](/wiki/gravity/momentum-graviton/tau-stuckelberg-mixing) — the mixing would arise through the wedge potential of the two frames.
- [The palindrome βₙ = β₄₋ₙ](/wiki/gravity/palindromic-branch/palindrome) — reciprocity acting on the wedge sector as frame exchange.

## Sources

- `papers/broken-born-checkpoint-v2.md` §7.2, §14 item 1, ref [12] — the frame-tier couplings as the Hinterbichler–Rosen class; the open derivation; the citation, marked †.
- `notes/debt1a-iii-tuning-test.md` §2, §3, §4 — the metric tier; wedge potentials, the symplectic vielbein, the tier argument and the verdict; the constrained bimetric picture.
- `notes/debt1a-iv-beta-coefficients.md` §1, §5 — the wedge sector as a Hassan–Rosen potential; the class selected, not derived.
- `notes/debt1a-ii-X-classification.md` §3 — the one known consistent structure for a massive spin-2 field.
- `notes/broken-born-theory.md` 'Addendum (v0.5)' — the verdict as first recorded.
- `HANDOFF.md` §2 — the verdict in the one-screen state.
