---
title: "The frame tier: the symplectic vielbein"
weight: 30
status: alive
description: "Wedge polynomials of the symplectic vielbein E (H = EᵀE) and the polarization frame E₀[J] are exactly the Hinterbichler–Rosen class: ghost-free by construction, Fierz–Pauli automatic — selected, not derived."
provenance: [D, T]
sources:
  - "wiki/papers/broken-born-checkpoint-v2.md §7.2"
  - "wiki/papers/broken-born-checkpoint-v2.md ref [12]"
  - "wiki/papers/broken-born-checkpoint-v2.md §14 item 1"
  - "wiki/papers/broken-born-checkpoint-v2.md §6"
  - "notes/tuning-test.md §3"
  - "notes/tuning-test.md §4"
  - "notes/tuning-test.md §5"
  - "notes/beta-coefficients.md §1"
  - "notes/beta-coefficients.md §5"
  - "notes/x-classification.md §3"
  - "notes/broken-born-theory.md §2"
  - "notes/broken-born-theory.md 'Addendum (v0.5)'"
  - "notes/broken-born-program-v1.md §5"
  - "notes/knot-dark-matter-standalone.md §1"
  - "HANDOFF.md §2"
---

*The frame tier is the reformulation that rescued [the tuning test](_index.md): the mass term of the [momentum graviton X](../momentum-graviton/_index.md) is built from frames, or vielbeins, instead of from metrics. A frame is a set of local reference axes from which a metric is assembled quadratically, as H = EᵀE, so the program calls frames first-order variables and metrics second-order ones. In frame variables the [ghost-free](../spin-2-fields/ghosts.md) potentials for two spin-2 fields are plain polynomials, wedge products of the two frames in the form found by Hinterbichler and Rosen ([the vielbein formulation](../spin-2-fields/vielbein-formulation.md)), with no matrix square roots and no ratio of coefficients to get wrong. The program has a frame of this kind, the symplectic vielbein E, which sits on the same first-order footing as the [polarization J](../../symmetry-breaking/order-parameter.md). [Calc note #7](../../history/documents/field-equation-notes.md) argues that the minimal coupling of the polarization to the geometry is therefore a wedge polynomial of E and a polarization frame E₀[J], and such a polynomial lies in the ghost-free class by construction, with the [Fierz–Pauli](../spin-2-fields/fierz-pauli.md) structure automatic. The argument is structural and rests on the literature. The class was selected by minimality and consistency rather than derived from the program's [geometric action](geometric-action.md), and no machine check covers it.*

**Status:** Alive — [D — structural, resting on T] in calc note [#7 §3](../../../notes/tuning-test.md#3-the-frame-tier-d--structural-resting-on-t); part of [checkpoint #11](../../history/documents/checkpoint.md) [§7.2](../../papers/broken-born-checkpoint-v2.md#72-the-tuning-test-dv), which is tagged [D][V] as a whole, but no test of [the verification battery](../../method/verification/battery.md) covers the frame tier, and the Hinterbichler–Rosen class is cited from model memory [12†] — the class was selected, not derived ([Open: deriving the wedge sector from S_H (OP1)](wedge-reduction.md)).

## The claim

Calc note #7 ([the field-equation calc notes](../../history/documents/field-equation-notes.md)) heads its §3 "The frame tier [D — structural, resting on T]" and makes the argument in one paragraph:

> The rescue is not a tuning but a *tier change*. In vielbein variables the ghost-free potentials are polynomial — wedge products ε(e ∧ … ∧ f ∧ …) of two frames (Hinterbichler–Rosen) [T] — with no square roots and no tuning to miss. And BBT possesses a natural frame-tier object: the symplectic vielbein E, the coset representative with H = EᵀE. Crucially, **J and E live on the same geometric tier** (first-order structures on the tangent, like the Born connection), while H = EᵀE is second-order. The geometrically minimal coupling of the polarization to the modular sector is therefore E-linear — wedge polynomials of (E, E₀[J]) — which is *precisely* the Hinterbichler–Rosen class: ghost-free by construction, Fierz–Pauli automatic, dRGT structure inherited rather than tuned.

BBT is Broken-Born theory, the program's earlier name, and dRGT is de Rham–Gabadadze–Tolley. Checkpoint [#11](../../papers/broken-born-checkpoint-v2.md) carries the claim in one sentence ([#11 §7.2](../../papers/broken-born-checkpoint-v2.md#72-the-tuning-test-dv)): "*Frame-tier* couplings — wedge polynomials of the symplectic vielbein E (H = EᵀE) with the polarization frame E₀[J] — are the Hinterbichler–Rosen class [12†], ghost-free by construction; J, E, and the Born connection share the first-order tier, so this is the geometrically minimal formulation."

## Frames and metrics [T]

A vielbein, or frame, is a set of local reference axes at each point, d of them in d dimensions, orthonormal in the metric. Written as a matrix e of components, it gives back the metric as g = eᵀe in Euclidean signature (in Lorentzian signature the Minkowski metric sits between the two factors), so the metric is quadratic in the frame, and the frame is fixed by the metric only up to a local rotation of the axes. In [general relativity](../spin-2-fields/general-relativity.md) the two descriptions are equivalent.

With two spin-2 fields the choice of variables changes what the healthy potentials look like. In metric variables, the ghost-free potentials of [dRGT massive gravity](../spin-2-fields/drgt-massive-gravity.md) and Hassan–Rosen bimetric gravity are linear combinations of the elementary symmetric polynomials eₙ of the matrix square root √(g⁻¹f), where f is the second metric ([Hassan–Rosen bimetric gravity](../spin-2-fields/hassan-rosen-bimetric.md); [elementary symmetric polynomials](../spin-2-fields/elementary-symmetric-polynomials.md)). In frame variables the square root disappears: when the two frames satisfy a symmetry condition, the square root is the ratio of the two frames. Each frame then supplies d one-forms. A wedge product of d one-forms, contracted with the totally antisymmetric symbol ε, is a volume element, and taking n of the d factors from the second frame and the rest from the first gives one term for each n. These are the wedge polynomials ε(e ∧ … ∧ f ∧ …) of [#7 §3](../../../notes/tuning-test.md#3-the-frame-tier-d--structural-resting-on-t), and term by term, up to normalization, they reproduce the eₙ terms of the metric potential [T] ([the vielbein formulation and wedge potentials](../spin-2-fields/vielbein-formulation.md)).

The two failures of the metric tier are failures to hit special coefficient relations: the Fierz–Pauli ratio at quadratic order and the linear span of the eₙ beyond it ([the metric tier fails twice](metric-tier-failures.md)). In frame variables every wedge polynomial of two frames is in the ghost-free class, so a coupling of that form has no ratio to get wrong. That is the sense of "no tuning to miss" and of "dRGT structure inherited rather than tuned".

## The program's frames

### The symplectic vielbein E

Once only the [symplectic form](../../phase-space/reciprocity/symplectic-form.md) is rigid, the phase-space metric H ranges over the Siegel domain Sp(2d, ℝ)/U(d) ([#11 §6](../../papers/broken-born-checkpoint-v2.md#6-the-modular-field); [the Siegel domain](../../phase-space/modular-field/siegel-domain.md)). [#7 §3](../../../notes/tuning-test.md#3-the-frame-tier-d--structural-resting-on-t) defines the symplectic vielbein as "the coset representative with H = EᵀE": for each H, a symplectic matrix E that produces H as EᵀE. Any other choice differs from E by a rotation in U(d) acting from the left, which leaves EᵀE unchanged [T]. E therefore stands to H as an ordinary frame stands to a metric.

### The polarization frame E₀[J]

The second frame is built from the polarization J, the real structure that the vacuum selects ([the order parameter: J, η and K](../../symmetry-breaking/order-parameter.md)). [#11 §7.2](../../papers/broken-born-checkpoint-v2.md#72-the-tuning-test-dv) calls it "the polarization frame E₀[J]", and [#7 §4](../../../notes/tuning-test.md#4-the-picture-that-emerges-constrained-bimetric-gravity-d--structural) calls it "the 'second vielbein'" and says what it can range over: "J carries only the 10 compact moduli of U(d)/O(d) — not a full second metric. So the 'second vielbein' E₀[J] is confined to a compact 10-dimensional moduli space" ([constrained bimetric gravity](constrained-bimetric.md)). No document writes E₀[J] out as a matrix. In calc note [#8](../../../notes/beta-coefficients.md) the two frames of the wedge sector are "(e, f = E₀[J])" ([#8 §1](../../../notes/beta-coefficients.md#1-what-reciprocity-does-to-the-wedge-potential-d)).

### The first-order tier

[#7 §3](../../../notes/tuning-test.md#3-the-frame-tier-d--structural-resting-on-t) sorts the program's objects by tier: "J and E live on the same geometric tier (first-order structures on the tangent, like the Born connection), while H = EᵀE is second-order." J acts linearly on tangent vectors, as one of the endomorphisms the lab notebook defines ([#1 §2](../../../notes/broken-born-theory.md#2-kinematic-core)); E is a frame for those vectors; and [the Born connection](../../phase-space/born-geometry/born-connection.md) is the rule for differentiating them. H, by contrast, is quadratic in E. The metric tier coupled the polarization to H; the frame tier couples it to E.

## The argument, step by step [D — structural, resting on T]

1. **The literature input [T].** In vielbein variables the ghost-free potentials for two spin-2 fields are the wedge polynomials of the two frames (Hinterbichler–Rosen, cited in #11 as [12†]).
2. **A frame in the program.** The program has a natural frame-tier object, the symplectic vielbein E with H = EᵀE.
3. **The shared tier.** J and E are both first-order objects; H is second-order.
4. **Minimality.** "The geometrically minimal coupling of the polarization to the modular sector is therefore E-linear — wedge polynomials of (E, E₀[J])". "E-linear" is set against the metric tier's couplings through H = EᵀE.
5. **The landing.** Such couplings are "*precisely* the Hinterbichler–Rosen class: ghost-free by construction, Fierz–Pauli automatic, dRGT structure inherited rather than tuned."

Step 4 is where the argument is structural. #7 gives a reason to prefer the frame-level coupling, the shared tier, and no derivation from an action showing that the theory contains it. Calc note #8 says so in its close-out: "the class was selected by minimality + consistency, not derived line-by-line" ([#8 §5](../../../notes/beta-coefficients.md#5-what-remains-honest-close-out)). Step 5 rests on the literature result, which #11 cites from model memory and which has not yet been checked against the source ([Open: the † literature battery (OP10)](../../method/literature-battery.md)). The reference is #11 [12]†: K. Hinterbichler, R. A. Rosen, "Interacting spin-2 fields," JHEP 1207, 047 (2012), [arXiv:1203.5783](https://arxiv.org/abs/1203.5783).

## What the frame tier yields

Calc note #8 writes the passing potential under its §1 heading "What reciprocity does to the wedge potential [D]":

```text
V = 2m²M² Σₙ₌₀⁴ βₙ eₙ(𝕏),      𝕏 = √(g⁻¹f)

exchange identity:  Sₙ(g, f) = S₄₋ₙ(f, g)                     (#8 §1)
```

"The Hinterbichler–Rosen sector for (e, f = E₀[J])" is the [Hassan–Rosen potential](../spin-2-fields/hassan-rosen-bimetric.md): a linear combination of the eₙ with constant coefficients βₙ, the form the metric tier missed. #8 does not define Sₙ, m or M, and it uses f both for the second frame and for the metric built from it.

The tier change fixes the form of the potential and not its coefficients. [#7 §3](../../../notes/tuning-test.md#3-the-frame-tier-d--structural-resting-on-t): "What a pass does **not** yet deliver: the βₙ coefficients. Those follow from expanding the E–J wedge sector, and they determine M_X, the X–h mixing, and a vacuum-energy contribution." Calc note #8 then restricted them by [reciprocity](../../phase-space/reciprocity/born-reciprocity.md) ([the palindrome βₙ = β₄₋ₙ](../palindromic-branch/palindrome.md)) and by the existence of a flat vacuum ([the vacuum-energy identity](../palindromic-branch/vacuum-energy-identity.md)). The picture the frame tier leaves is [constrained bimetric gravity](constrained-bimetric.md), and its place in the outcome of the test is [the verdict: a conditional pass](conditional-pass.md).

## Verification and scope

- **No machine check.** [#11 §7.2](../../papers/broken-born-checkpoint-v2.md#72-the-tuning-test-dv) tags the tuning test [D][V] as a whole. The [V] belongs to the blocks of the misalignment potential (battery test T3) and the two metric-tier failures (T4, T7); no test of [`verify/battery.py`](../../../verify/battery.py) touches the frame tier, which stays [D — structural, resting on T] ([the verification battery](../../method/verification/battery.md)).
- **Selected, not derived.** [#11 §14 item 1](../../papers/broken-born-checkpoint-v2.md#14-open-problems) keeps the derivation open: "First-principles reduction of the frame-tier wedge sector from S_H (class selected, not derived) [O]" ([Open: deriving the wedge sector from S_H (OP1)](wedge-reduction.md)). [#11 §2](../../papers/broken-born-checkpoint-v2.md#2-methodological-preface-provenance-and-verification) names this kind of risk, "the selection-versus-derivation bias" ([claim tiers and selection bias](../../method/claim-tiers.md)).
- **Euclidean skeleton.** The tuning test is computed for a positive-definite metric ([#7 §2](../../../notes/tuning-test.md#2-explicit-computation-metric-tier-d--rigorous)); extending the program's Euclidean results to spacetime signature is open problem 3 ([Open: Lorentzian dressing (OP3)](../../phase-space/born-geometry/lorentzian-dressing.md)).

## History

- **Calc note [#6](../../../notes/x-classification.md)** set the condition: the geometric sector "is healthy iff the potential generated by the η-selection lands in the Hassan–Rosen class" ([#6 §3](../../../notes/x-classification.md#3-the-mass-mechanism-and-the-endpoint-d--structural)).
- **Calc note #7** found the frame tier after the metric tier failed, and its §5 records "the consistent branch is identified and class-certified (frame tier)" ([#7 §5](../../../notes/tuning-test.md#5-status-of-the-field-equation-problem)).
- **The lab notebook**, v0.5 addendum: frame-tier couplings "land in the Hinterbichler–Rosen polynomial class, ghost-free by construction. Since J, E, and the Born connection all live on the first-order tier, the frame formulation is the geometrically minimal one" ([the lab notebook](../../history/documents/lab-notebook.md)).
- **The v1 program paper** ([#9 §5 item 4](../../../notes/broken-born-program-v1.md#5-the-second-graviton-and-its-mass-the-field-equation-problem-solved), superseded by #11) tagged the Hinterbichler–Rosen class [T]; [#11 §7.2](../../papers/broken-born-checkpoint-v2.md#72-the-tuning-test-dv) cites it as [12†] ([the checkpoint](../../history/documents/checkpoint.md)). [The handoff](../../history/documents/handoff.md) lists "frame-tier (vielbein wedge, Hinterbichler–Rosen class) passes" among the results that stand ([`HANDOFF.md` §2](../../../HANDOFF.md#2-scientific-state-one-screen)).
- **The standalone manuscript [#14](../../../notes/knot-dark-matter-standalone.md)**, since withdrawn after its [round-3](../../method/review/round-3/_index.md) review for reasons unrelated to this section ([Obituary: #14's superheavy-soliton model](../../dark-matter/candidates/soliton-candidate/obituary.md)), put the caveat to its referees in these words: "That the symmetry-breaking sector lands on the ghost-free potential is argued from a first-order (vielbein) formulation and is a structural claim, not a line-by-line derivation" ([#14 §1](../../../notes/knot-dark-matter-standalone.md#1-framework)).

## Sources

- [`notes/tuning-test.md` §3](../../../notes/tuning-test.md#3-the-frame-tier-d--structural-resting-on-t) — the frame tier [D — structural, resting on T] and what a pass does not deliver; [§4](../../../notes/tuning-test.md#4-the-picture-that-emerges-constrained-bimetric-gravity-d--structural) — E₀[J] as the "second vielbein" on a compact moduli space; [§5](../../../notes/tuning-test.md#5-status-of-the-field-equation-problem) — "class-certified".
- [`wiki/papers/broken-born-checkpoint-v2.md` §7.2](../../papers/broken-born-checkpoint-v2.md#72-the-tuning-test-dv) and ref. [12] — the current statement and the Hinterbichler–Rosen citation, marked †; [§14 item 1](../../papers/broken-born-checkpoint-v2.md#14-open-problems) — the open derivation; [§6](../../papers/broken-born-checkpoint-v2.md#6-the-modular-field) — the Siegel domain.
- [`notes/beta-coefficients.md` §1](../../../notes/beta-coefficients.md#1-what-reciprocity-does-to-the-wedge-potential-d) — the wedge potential for (e, f = E₀[J]); [§5](../../../notes/beta-coefficients.md#5-what-remains-honest-close-out) — "selected by minimality + consistency".
- [`notes/x-classification.md` §3](../../../notes/x-classification.md#3-the-mass-mechanism-and-the-endpoint-d--structural) — the health criterion.
- [`notes/broken-born-theory.md` §2](../../../notes/broken-born-theory.md#2-kinematic-core) — I, J and K as endomorphisms; 'Addendum (v0.5)' — the notebook's statement.
- [`notes/broken-born-program-v1.md` §5](../../../notes/broken-born-program-v1.md#5-the-second-graviton-and-its-mass-the-field-equation-problem-solved) — the v1 statement, tagged [T].
- [`notes/knot-dark-matter-standalone.md` §1](../../../notes/knot-dark-matter-standalone.md#1-framework) — the caveat as stated in the withdrawn manuscript.
- [`HANDOFF.md` §2](../../../HANDOFF.md#2-scientific-state-one-screen) — the handoff's summary.
