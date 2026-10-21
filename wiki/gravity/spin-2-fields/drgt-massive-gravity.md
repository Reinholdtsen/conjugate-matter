---
title: "dRGT massive gravity"
weight: 40
status: established
description: "de Rham–Gabadadze–Tolley's ghost-free nonlinear completion of Fierz–Pauli, and the program's criterion that X's sector is healthy iff its potential lands in the dRGT/Hassan–Rosen class."
provenance: [T]
sources:
  - "papers/broken-born-checkpoint-v2.md §7.1"
  - "papers/broken-born-checkpoint-v2.md §7.2"
  - "papers/broken-born-checkpoint-v2.md §14"
  - "papers/broken-born-checkpoint-v2.md §15"
  - "papers/broken-born-checkpoint-v2.md ref [9]"
  - "notes/debt1a-ii-X-classification.md §3"
  - "notes/debt1a-ii-X-classification.md §5"
  - "notes/debt1a-iii-tuning-test.md §1"
  - "notes/debt1a-iii-tuning-test.md §2"
  - "notes/debt1a-iii-tuning-test.md §3"
  - "notes/debt1a-iv-beta-coefficients.md §1"
  - "notes/debt1a-iv-beta-coefficients.md §5"
  - "notes/broken-born-theory.md 'Addendum (v0.4)'"
  - "notes/broken-born-theory.md 'Addendum (v0.5)'"
---

*dRGT massive gravity, after de Rham, Gabadadze and Tolley, is a theory of a single massive graviton whose nonlinear potential is built so that the Boulware–Deser ghost never appears; it completes the Fierz–Pauli mass term to all orders. Its potential is a linear combination, with constant coefficients, of the elementary symmetric polynomials of the matrix square root √(g⁻¹f), where g is the dynamical metric and f a fixed reference metric. With its two-metric extension by Hassan and Rosen, it is the one known consistent structure for a massive spin-2 field coupled to gravity. The program adopted this class as the health test for its [momentum graviton X](/wiki/gravity/momentum-graviton): X's sector is healthy if and only if the potential that gives X its mass lands in it. Built from metrics, X's potential misses the class; built from frames, it lands in it.*

**Status:** Established — [T] — cited in the [checkpoint](/wiki/history/documents/checkpoint) as [9†], from model memory, and not yet checked against the source: it is not among the references the round-3 audit checked, and its check belongs to [the † literature battery](/wiki/method/literature-battery) (OP10). In [#6](/wiki/history/documents/debt-1-notes) §3 the literature statement the program builds on carries the tag "[T: HR 2011]", and the health criterion drawn from it sits in a section tagged [D — structural]; the criterion was applied in [the tuning test](/wiki/gravity/tuning-test), which X's potential passed conditionally. Nothing on this page is machine-checked; the tuning test's checks are on [the verification battery](/wiki/method/verification/battery).

## The problem dRGT solves [T]

The [Fierz–Pauli mass term](/wiki/gravity/spin-2-fields/fierz-pauli) gives a healthy massive spin-2 field, but only at quadratic order. A massive graviton that interacts, with the metric of general relativity or with itself, needs a nonlinear potential, and Boulware and Deser showed that a generic one brings back an extra mode, a ghost ([beyond quadratic order](/wiki/gravity/spin-2-fields/fierz-pauli#beyond-quadratic-order-the-boulwaredeser-ghost-t)). Their result left open whether any nonlinear potential avoids it.

De Rham and Gabadadze (2010†) worked in a limit that isolates the helicity-0 polarization of the massive graviton, where the ghost shows up as self-interactions with too many derivatives, and chose the coefficients of the potential order by order so that those interactions cancel. De Rham, Gabadadze and Tolley then resummed the series into a closed form, the paper the checkpoint cites as [9†], "Resummation of massive gravity".

## The potential [T]

The theory has one dynamical metric g_μν and one fixed reference metric f_μν; in the original construction f is the flat metric. The building block is the matrix g⁻¹f, with components g^μρ f_ρν, and its square root, the matrix 𝕏 whose square is g⁻¹f. The program's calc note #8 §1 writes it as 𝕏 = √(g⁻¹f).

The potential is built from the [elementary symmetric polynomials](/wiki/gravity/spin-2-fields/elementary-symmetric-polynomials) eₙ of the eigenvalues of 𝕏: e₀ = 1, e₁ is their sum (Tr 𝕏), e₂ the sum of their pairwise products, and so on up to e₄, their product (det 𝕏), in four dimensions. The action is the Einstein–Hilbert action of g plus a potential linear in the eₙ:

```text
S = S_EH[g] − ∫ d⁴x √−g V(g, f)
V ∝ m² Σₙ₌₀⁴ βₙ eₙ(𝕏),        𝕏 = √(g⁻¹f),        βₙ constants
```

Here m sets the graviton's mass scale and the βₙ are constant coefficients. Calc note #7 §2 states the defining feature for the family as a whole: "The Hassan–Rosen ghost-free family is *linear* combinations Σβₙeₙ(√(g⁻¹f)) (constants βₙ)." A potential that is a nonlinear function of the eₙ lies outside the family, which is the second way the program's metric-built potential failed ([the metric tier fails twice](/wiki/gravity/tuning-test/metric-tier-failures)).

**Expanded about g = f.** There 𝕏 is the identity. The coefficients are chosen so that g = f solves the field equations, with no term linear in the fluctuation (a vanishing tadpole). The term quadratic in the fluctuation is then the Fierz–Pauli mass term, with its relative weight −1 between Tr(h²) and (Tr h)², and once the βₙ are chosen the structure of the eₙ fixes every higher order.

**Why the ghost stays out.** In the Hamiltonian formulation of Arnowitt, Deser and Misner, the lapse of general relativity appears linearly and enforces the Hamiltonian constraint, which, with the gauge freedom, removes every mode that is not a physical polarization. A generic potential spoils that linearity, and the constraint that would remove the extra mode of a massive graviton is lost. With the dRGT potential the lapse can be made to appear linearly again, after a redefinition of the shift, so the constraint, and a secondary constraint that follows from it, survive and remove the extra mode. Hassan and Rosen gave the proof, in the paper the checkpoint cites as [10†], "Resolving the ghost problem in non-linear massive gravity". What propagates is a massive spin-2 field with the five polarizations that calc note #6 §3 counts for X.

## From massive gravity to bimetric gravity [T]

In dRGT massive gravity the reference metric f is fixed in advance and has no field equation. Hassan and Rosen showed that f can be given its own Einstein–Hilbert term without bringing the ghost back. The result, [Hassan–Rosen bimetric gravity](/wiki/gravity/spin-2-fields/hassan-rosen-bimetric) ([11†]), has two dynamical metrics coupled through the same potential, and its spectrum about proportional backgrounds holds one massless and one massive spin-2 field. In frame variables the same potentials are the wedge polynomials of Hinterbichler and Rosen ([12†]; [the vielbein formulation](/wiki/gravity/spin-2-fields/vielbein-formulation)).

The program treats these as one class. Calc note #6 §3: "Massive spin-2 coupled to gravity has exactly one known consistent structure: the Fierz–Pauli tuning at quadratic order completed by a dRGT/Hassan–Rosen-class potential [T: HR 2011]." The checkpoint: "The unique consistent structure for massive spin-2 is Fierz–Pauli/dRGT/Hassan–Rosen [9†, 10†, 11†]" (#11 §7.1). #6 states the uniqueness as a fact about what is known; #11 states it without the qualifier. In the program's vocabulary the "tuning" is this coefficient structure: the relative weights that keep the ghost out.

## The program's health criterion

### The criterion

Once the chain of #6 §1–§3 has made X a massive spin-2 field ([why X must be massive](/wiki/gravity/momentum-graviton/forcing-chain)), the question is whether its mass term is healthy. Calc note #6 §3, a section tagged [D — structural], states the criterion right after the literature statement quoted above:

> **X is a massive spin-2 field. The geometric sector is healthy iff the potential generated by the η-selection lands in the Hassan–Rosen class; a generic potential reintroduces the Boulware–Deser ghost.**

The η-selection sector is the coupling through which the vacuum selects its polarization: the coupling between the polarization J and the modular field Z, which the program calls its Higgs sector ([the misalignment potential](/wiki/gravity/tuning-test/misalignment-potential)). Its potential is what gives X its mass ([the gravitational Higgs mechanism](/wiki/gravity/momentum-graviton/gravitational-higgs)). #6 restates the criterion as a "selling line": the geometric sector "is bimetric gravity with the second metric's kinetic structure and couplings dictated by modular (Siegel-domain) symmetry rather than chosen by hand", provided "the dRGT tuning emerges from the symmetry". The [lab notebook](/wiki/history/documents/lab-notebook)'s addendum v0.4 records the same reduction: the sector is "healthy **iff** the η-selection generates a Hassan–Rosen-class potential", and "Debt 1 has been reduced to that single tuning computation" ([the three debts](/wiki/history/debts)).

### What depended on it

#6 §5 named the computation that would decide it: "derive the X-potential from the η-selection (J–Z) sector and test it against the dRGT coefficient family." It set out both outcomes. "Pass ⇒ the geometric core stands and 'theory' becomes the defensible word. Fail ⇒ the Boulware–Deser ghost kills the geometric sector", and the program "survives only as its phenomenological shell": gated self-interacting dark matter ([conjugate matter](/wiki/dark-matter/conjugate-matter)) plus Maslov quintessence ([τ](/wiki/cosmology/dark-energy/tau-quintessence)), "with the geometric story demoted to heuristics".

### The test and its outcome

Calc note #7 §1 poses the test: "does the resulting potential land in the ghost-free (Fierz–Pauli / dRGT / Hassan–Rosen) family, or in the generic Boulware–Deser-ghost family?" The lab notebook calls it "The dRGT tuning test" (#1 'Addendum (v0.5)').

- **Metric tier: fails twice** [D — rigorous] (#7 §2). Built from the metric H, the potential gives a graviton mass "**without** the −(Tr h)² companion", which misses the Fierz–Pauli weight (battery test T4), and its nonlinear structure Tr(g²) = p₄ is "a *nonlinear* polynomial in the eₙ, hence outside the family" (battery test T7 checks p₄ numerically). See [the metric tier fails twice](/wiki/gravity/tuning-test/metric-tier-failures).
- **Frame tier: passes** [D — structural, resting on T] (#7 §3). Built from the symplectic vielbein E (H = EᵀE) and the polarization frame E₀[J], the potential is a wedge polynomial, "*precisely* the Hinterbichler–Rosen class: ghost-free by construction, Fierz–Pauli automatic, dRGT structure inherited rather than tuned". This half has no machine check ([the frame tier](/wiki/gravity/tuning-test/frame-tier)).

The verdict, in the notebook's words: "the theory passes iff formulated in first-order variables, which is the formulation the geometry prefers anyway" (#1 'Addendum (v0.5)'). #7 §3 calls it "a conditional pass with the condition being the formulation the geometry already prefers", and the checkpoint tags the test [D][V] (#11 §7.2). See [the verdict: a conditional pass](/wiki/gravity/tuning-test/conditional-pass).

### What the pass does not settle

A pass does not fix the coefficients. #7 §3: "What a pass does **not** yet deliver: the βₙ coefficients. Those follow from expanding the E–J wedge sector, and they determine M_X, the X–h mixing, and a vacuum-energy contribution." Calc note #8 then found that reciprocity constrains them to βₙ = β₄₋ₙ ([the palindrome](/wiki/gravity/palindromic-branch/palindrome)).

The passing class was chosen rather than derived. #8 §5: "the class was selected by minimality + consistency, not derived line-by-line". Deriving it from the geometric action is open, item 1 of #11 §14: "First-principles reduction of the frame-tier wedge sector from S_H (class selected, not derived) [O]" ([Open: deriving the wedge sector from S_H](/wiki/gravity/tuning-test/wedge-reduction)).

#6 §5 expected a pass to make "theory" the defensible word. The checkpoint, which outranks it, says instead that "the word 'theory' still waits on items 1–3" of its open problems (#11 §15; [the assessment](/wiki/program/assessment)).

## References

As the documents give them:

- [9]† C. de Rham, G. Gabadadze, A. J. Tolley, "Resummation of massive gravity," Phys. Rev. Lett. 106, 231101 (2011), arXiv:1011.1232 (#11).
- [10]† and [11]† Hassan–Rosen, [12]† Hinterbichler–Rosen (#11); see [Hassan–Rosen bimetric gravity](/wiki/gravity/spin-2-fields/hassan-rosen-bimetric) and [the vielbein formulation](/wiki/gravity/spin-2-fields/vielbein-formulation).

Added by the wiki from model memory (†):

- C. de Rham, G. Gabadadze (2010)†: the potential constructed order by order in the helicity-0 limit.
- K. Hinterbichler, "Theoretical aspects of massive gravity," Rev. Mod. Phys. (2012)†; C. de Rham, "Massive gravity," Living Rev. Relativ. (2014)†: reviews.

## Used by

- [Why X must be massive](/wiki/gravity/momentum-graviton/forcing-chain) — names the unique consistent structure for a massive X.
- [The gravitational Higgs mechanism](/wiki/gravity/momentum-graviton/gravitational-higgs) — the structure the Higgsed X must land in.
- [The misalignment potential](/wiki/gravity/tuning-test/misalignment-potential) — the potential tested against this class.
- [The metric tier fails twice](/wiki/gravity/tuning-test/metric-tier-failures) — misses the Fierz–Pauli weight and the linear-in-eₙ structure.
- [The frame tier: the symplectic vielbein](/wiki/gravity/tuning-test/frame-tier) — the passing potentials inherit the dRGT structure.
- [The verdict: a conditional pass](/wiki/gravity/tuning-test/conditional-pass) — the test's outcome.
- [Constrained bimetric gravity](/wiki/gravity/tuning-test/constrained-bimetric) — the picture that results.
- [Open: deriving the wedge sector from S_H (OP1)](/wiki/gravity/tuning-test/wedge-reduction) — the class was selected, not derived.

## Sources

- `papers/broken-born-checkpoint-v2.md` §7.1, §7.2, §14 item 1, §15, ref [9] — the unique consistent structure; the tuning test's tags; the open derivation; "theory" waits on items 1–3; the citation, marked †.
- `notes/debt1a-ii-X-classification.md` §3, §5 — the health criterion, the selling line, and what depended on it.
- `notes/debt1a-iii-tuning-test.md` §1, §2, §3 — the test; linearity in the eₙ and the metric-tier failures; the frame tier, "dRGT structure inherited rather than tuned"; what a pass does not deliver.
- `notes/debt1a-iv-beta-coefficients.md` §1, §5 — the potential in the program's notation; the class selected, not derived.
- `notes/broken-born-theory.md` 'Addendum (v0.4)', 'Addendum (v0.5)' — the reduction to one tuning computation; the verdict as first recorded.
