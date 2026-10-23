---
title: "The frame tier: the symplectic vielbein"
weight: 30
status: alive
description: "Wedge polynomials of the symplectic vielbein E (H = EᵀE) and the polarization frame E₀[J] are exactly the Hinterbichler–Rosen class: ghost-free by construction, Fierz–Pauli automatic — selected, not derived."
provenance: [D, T]
sources:
  - "papers/broken-born-checkpoint-v2.md §7.2"
  - "papers/broken-born-checkpoint-v2.md ref [12]"
  - "papers/broken-born-checkpoint-v2.md §14 item 1"
  - "papers/broken-born-checkpoint-v2.md §6"
  - "notes/debt1a-iii-tuning-test.md §3"
  - "notes/debt1a-iii-tuning-test.md §4"
  - "notes/debt1a-iii-tuning-test.md §5"
  - "notes/debt1a-iv-beta-coefficients.md §1"
  - "notes/debt1a-iv-beta-coefficients.md §5"
  - "notes/debt1a-ii-X-classification.md §3"
  - "notes/broken-born-theory.md §2"
  - "notes/broken-born-theory.md 'Addendum (v0.5)'"
  - "notes/broken-born-program-v1.md §5"
  - "notes/knot-dark-matter-standalone.md §1"
  - "HANDOFF.md §2"
---

*The frame tier is the reformulation that rescued [the tuning test](/wiki/gravity/tuning-test): the mass term of the [momentum graviton X](/wiki/gravity/momentum-graviton) is built from frames, or vielbeins, instead of from metrics. A frame is a set of local reference axes from which a metric is assembled quadratically, as H = EᵀE, so the program calls frames first-order variables and metrics second-order ones. In frame variables the [ghost-free](/wiki/gravity/spin-2-fields/ghosts) potentials for two spin-2 fields are plain polynomials, wedge products of the two frames in the form found by Hinterbichler and Rosen ([the vielbein formulation](/wiki/gravity/spin-2-fields/vielbein-formulation)), with no matrix square roots and no ratio of coefficients to get wrong. The program has a frame of this kind, the symplectic vielbein E, which sits on the same first-order footing as the [polarization J](/wiki/symmetry-breaking/order-parameter). [Calc note #7](/wiki/history/documents/debt-1-notes) argues that the minimal coupling of the polarization to the geometry is therefore a wedge polynomial of E and a polarization frame E₀[J], and such a polynomial lies in the ghost-free class by construction, with the [Fierz–Pauli](/wiki/gravity/spin-2-fields/fierz-pauli) structure automatic. The argument is structural and rests on the literature. The class was selected by minimality and consistency rather than derived from the program's [geometric action](/wiki/gravity/tuning-test/geometric-action), and no machine check covers it.*

**Status:** Alive — [D — structural, resting on T] in calc note #7 §3; part of [checkpoint #11](/wiki/history/documents/checkpoint) §7.2, which is tagged [D][V] as a whole, but no test of [the verification battery](/wiki/method/verification/battery) covers the frame tier, and the Hinterbichler–Rosen class is cited from model memory [12†] — the class was selected, not derived ([Open: deriving the wedge sector from S_H (OP1)](/wiki/gravity/tuning-test/wedge-reduction)).

## The claim

Calc note #7 ([the Debt-1 calc notes](/wiki/history/documents/debt-1-notes)) heads its §3 "The frame tier [D — structural, resting on T]" and makes the argument in one paragraph:

> The rescue is not a tuning but a *tier change*. In vielbein variables the ghost-free potentials are polynomial — wedge products ε(e ∧ … ∧ f ∧ …) of two frames (Hinterbichler–Rosen) [T] — with no square roots and no tuning to miss. And BBT possesses a natural frame-tier object: the symplectic vielbein E, the coset representative with H = EᵀE. Crucially, **J and E live on the same geometric tier** (first-order structures on the tangent, like the Born connection), while H = EᵀE is second-order. The geometrically minimal coupling of the polarization to the modular sector is therefore E-linear — wedge polynomials of (E, E₀[J]) — which is *precisely* the Hinterbichler–Rosen class: ghost-free by construction, Fierz–Pauli automatic, dRGT structure inherited rather than tuned.

BBT is the Broken-Born program, and dRGT is de Rham–Gabadadze–Tolley. Checkpoint #11 carries the claim in one sentence (#11 §7.2): "*Frame-tier* couplings — wedge polynomials of the symplectic vielbein E (H = EᵀE) with the polarization frame E₀[J] — are the Hinterbichler–Rosen class [12†], ghost-free by construction; J, E, and the Born connection share the first-order tier, so this is the geometrically minimal formulation."

## Frames and metrics [T]

A vielbein, or frame, is a set of local reference axes at each point, d of them in d dimensions, orthonormal in the metric. Written as a matrix e of components, it gives back the metric as g = eᵀe in Euclidean signature (in Lorentzian signature the Minkowski metric sits between the two factors), so the metric is quadratic in the frame, and the frame is fixed by the metric only up to a local rotation of the axes. In [general relativity](/wiki/gravity/spin-2-fields/general-relativity) the two descriptions are equivalent.

With two spin-2 fields the choice of variables changes what the healthy potentials look like. In metric variables, the ghost-free potentials of [dRGT massive gravity](/wiki/gravity/spin-2-fields/drgt-massive-gravity) and Hassan–Rosen bimetric gravity are linear combinations of the elementary symmetric polynomials eₙ of the matrix square root √(g⁻¹f), where f is the second metric ([Hassan–Rosen bimetric gravity](/wiki/gravity/spin-2-fields/hassan-rosen-bimetric); [elementary symmetric polynomials](/wiki/gravity/spin-2-fields/elementary-symmetric-polynomials)). In frame variables the square root disappears: when the two frames satisfy a symmetry condition, the square root is the ratio of the two frames. Each frame then supplies d one-forms. A wedge product of d one-forms, contracted with the totally antisymmetric symbol ε, is a volume element, and taking n of the d factors from the second frame and the rest from the first gives one term for each n. These are the wedge polynomials ε(e ∧ … ∧ f ∧ …) of #7 §3, and term by term, up to normalization, they reproduce the eₙ terms of the metric potential [T] ([the vielbein formulation and wedge potentials](/wiki/gravity/spin-2-fields/vielbein-formulation)).

The two failures of the metric tier are failures to hit special coefficient relations: the Fierz–Pauli ratio at quadratic order and the linear span of the eₙ beyond it ([the metric tier fails twice](/wiki/gravity/tuning-test/metric-tier-failures)). In frame variables every wedge polynomial of two frames is in the ghost-free class, so a coupling of that form has no ratio to get wrong. That is the sense of "no tuning to miss" and of "dRGT structure inherited rather than tuned".

## The program's frames

### The symplectic vielbein E

Once only the [symplectic form](/wiki/phase-space/reciprocity/symplectic-form) is rigid, the phase-space metric H ranges over the Siegel domain Sp(2d, ℝ)/U(d) (#11 §6; [the Siegel domain](/wiki/phase-space/modular-field/siegel-domain)). #7 §3 defines the symplectic vielbein as "the coset representative with H = EᵀE": for each H, a symplectic matrix E that produces H as EᵀE. Any other choice differs from E by a rotation in U(d) acting from the left, which leaves EᵀE unchanged [T]. E therefore stands to H as an ordinary frame stands to a metric.

### The polarization frame E₀[J]

The second frame is built from the polarization J, the real structure that the vacuum selects ([the order parameter: J, η and K](/wiki/symmetry-breaking/order-parameter)). #11 §7.2 calls it "the polarization frame E₀[J]", and #7 §4 calls it "the 'second vielbein'" and says what it can range over: "J carries only the 10 compact moduli of U(d)/O(d) — not a full second metric. So the 'second vielbein' E₀[J] is confined to a compact 10-dimensional moduli space" ([constrained bimetric gravity](/wiki/gravity/tuning-test/constrained-bimetric)). No document writes E₀[J] out as a matrix. In calc note #8 the two frames of the wedge sector are "(e, f = E₀[J])" (#8 §1).

### The first-order tier

#7 §3 sorts the program's objects by tier: "J and E live on the same geometric tier (first-order structures on the tangent, like the Born connection), while H = EᵀE is second-order." J acts linearly on tangent vectors, as one of the endomorphisms the lab notebook defines (#1 §2); E is a frame for those vectors; and [the Born connection](/wiki/phase-space/born-geometry/born-connection) is the rule for differentiating them. H, by contrast, is quadratic in E. The metric tier coupled the polarization to H; the frame tier couples it to E.

## The argument, step by step [D — structural, resting on T]

1. **The literature input [T].** In vielbein variables the ghost-free potentials for two spin-2 fields are the wedge polynomials of the two frames (Hinterbichler–Rosen, cited in #11 as [12†]).
2. **A frame in the program.** The program has a natural frame-tier object, the symplectic vielbein E with H = EᵀE.
3. **The shared tier.** J and E are both first-order objects; H is second-order.
4. **Minimality.** "The geometrically minimal coupling of the polarization to the modular sector is therefore E-linear — wedge polynomials of (E, E₀[J])". "E-linear" is set against the metric tier's couplings through H = EᵀE.
5. **The landing.** Such couplings are "*precisely* the Hinterbichler–Rosen class: ghost-free by construction, Fierz–Pauli automatic, dRGT structure inherited rather than tuned."

Step 4 is where the argument is structural. #7 gives a reason to prefer the frame-level coupling, the shared tier, and no derivation from an action showing that the theory contains it. Calc note #8 says so in its close-out: "the class was selected by minimality + consistency, not derived line-by-line" (#8 §5). Step 5 rests on the literature result, which #11 cites from model memory and which has not yet been checked against the source ([Open: the † literature battery (OP10)](/wiki/method/literature-battery)). The reference is #11 [12]†: K. Hinterbichler, R. A. Rosen, "Interacting spin-2 fields," JHEP 1207, 047 (2012), arXiv:1203.5783.

## What the frame tier yields

Calc note #8 writes the passing potential under its §1 heading "What reciprocity does to the wedge potential [D]":

```text
V = 2m²M² Σₙ₌₀⁴ βₙ eₙ(𝕏),      𝕏 = √(g⁻¹f)

exchange identity:  Sₙ(g, f) = S₄₋ₙ(f, g)                     (#8 §1)
```

"The Hinterbichler–Rosen sector for (e, f = E₀[J])" is the [Hassan–Rosen potential](/wiki/gravity/spin-2-fields/hassan-rosen-bimetric): a linear combination of the eₙ with constant coefficients βₙ, the form the metric tier missed. #8 does not define Sₙ, m or M, and it uses f both for the second frame and for the metric built from it.

The tier change fixes the form of the potential and not its coefficients. #7 §3: "What a pass does **not** yet deliver: the βₙ coefficients. Those follow from expanding the E–J wedge sector, and they determine M_X, the X–h mixing, and a vacuum-energy contribution." Calc note #8 then restricted them by [reciprocity](/wiki/phase-space/reciprocity/born-reciprocity) ([the palindrome βₙ = β₄₋ₙ](/wiki/gravity/palindromic-branch/palindrome)) and by the existence of a flat vacuum ([the vacuum-energy identity](/wiki/gravity/palindromic-branch/vacuum-energy-identity)). The picture the frame tier leaves is [constrained bimetric gravity](/wiki/gravity/tuning-test/constrained-bimetric), and its place in the outcome of the test is [the verdict: a conditional pass](/wiki/gravity/tuning-test/conditional-pass).

## Verification and scope

- **No machine check.** #11 §7.2 tags the tuning test [D][V] as a whole. The [V] belongs to the blocks of the misalignment potential (battery test T3) and the two metric-tier failures (T4, T7); no test of `verify/battery.py` touches the frame tier, which stays [D — structural, resting on T] ([the verification battery](/wiki/method/verification/battery)).
- **Selected, not derived.** #11 §14 item 1 keeps the derivation open: "First-principles reduction of the frame-tier wedge sector from S_H (class selected, not derived) [O]" ([Open: deriving the wedge sector from S_H (OP1)](/wiki/gravity/tuning-test/wedge-reduction)). #11 §2 names this kind of risk, "the selection-versus-derivation bias" ([claim tiers and selection bias](/wiki/method/claim-tiers)).
- **Euclidean skeleton.** The tuning test is computed for a positive-definite metric (#7 §2); extending the program's Euclidean results to spacetime signature is open problem 3 ([Open: Lorentzian dressing (OP3)](/wiki/phase-space/born-geometry/lorentzian-dressing)).

## History

- **Calc note #6** set the condition: the geometric sector "is healthy iff the potential generated by the η-selection lands in the Hassan–Rosen class" (#6 §3).
- **Calc note #7** found the frame tier after the metric tier failed, and its §5 records "the consistent branch is identified and class-certified (frame tier)" (#7 §5).
- **The lab notebook**, v0.5 addendum: frame-tier couplings "land in the Hinterbichler–Rosen polynomial class, ghost-free by construction. Since J, E, and the Born connection all live on the first-order tier, the frame formulation is the geometrically minimal one" ([the lab notebook](/wiki/history/documents/lab-notebook)).
- **The v1 program paper** (#9 §5 item 4, superseded by #11) tagged the Hinterbichler–Rosen class [T]; #11 §7.2 cites it as [12†] ([the checkpoint](/wiki/history/documents/checkpoint)). [The handoff](/wiki/history/documents/handoff) lists "frame-tier (vielbein wedge, Hinterbichler–Rosen class) passes" among the results that stand (`HANDOFF.md` §2).
- **The standalone manuscript #14**, since withdrawn after its [round-3](/wiki/method/review/round-3) review for reasons unrelated to this section ([Obituary: superheavy conjugate solitons](/wiki/dark-matter/candidates/soliton-candidate/obituary)), put the caveat to its referees in these words: "That the symmetry-breaking sector lands on the ghost-free potential is argued from a first-order (vielbein) formulation and is a structural claim, not a line-by-line derivation" (#14 §1).

## Sources

- `notes/debt1a-iii-tuning-test.md` §3 — the frame tier [D — structural, resting on T] and what a pass does not deliver; §4 — E₀[J] as the "second vielbein" on a compact moduli space; §5 — "class-certified".
- `papers/broken-born-checkpoint-v2.md` §7.2 and ref. [12] — the current statement and the Hinterbichler–Rosen citation, marked †; §14 item 1 — the open derivation; §6 — the Siegel domain.
- `notes/debt1a-iv-beta-coefficients.md` §1 — the wedge potential for (e, f = E₀[J]); §5 — "selected by minimality + consistency".
- `notes/debt1a-ii-X-classification.md` §3 — the health criterion.
- `notes/broken-born-theory.md` §2 — I, J and K as endomorphisms; 'Addendum (v0.5)' — the notebook's statement.
- `notes/broken-born-program-v1.md` §5 — the v1 statement, tagged [T].
- `notes/knot-dark-matter-standalone.md` §1 — the caveat as stated in the withdrawn manuscript.
- `HANDOFF.md` §2 — the handoff's summary.
