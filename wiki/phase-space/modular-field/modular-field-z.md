---
title: "The modular field Z = X + iY"
weight: 20
status: alive
description: "Once only ω is rigid, all of phase-space geometry fits one complex field: Im Z = g is the spacetime metric (the vacuum slice X = 0, ⟨Z⟩ = i·g) and Re Z = X is the local tilt of the position/momentum split, the momentum graviton."
provenance: [D]
sources:
  - "wiki/papers/broken-born-checkpoint-v2.md §6"
  - "notes/geometric-core.md §C"
  - "notes/geometric-core.md §B"
  - "notes/geometric-core.md §D"
  - "notes/geometric-core.md §F"
  - "notes/x-classification.md §1"
  - "notes/x-classification.md §3"
  - "notes/tuning-test.md §2"
  - "notes/beta-coefficients.md §4"
  - "wiki/papers/broken-born-checkpoint-v2.md §7"
  - "wiki/papers/broken-born-checkpoint-v2.md §8"
  - "wiki/papers/broken-born-checkpoint-v2.md §14"
  - "notes/broken-born-program-v1.md §4"
  - "notes/broken-born-theory.md 'Addendum (v0.3, overnight): axiom correction and the modular core'"
  - "notes/broken-born-theory.md §3"
  - "notes/broken-born-theory.md §11"
  - "verify/battery.py T2"
  - "review/round3/referee/audit-notes.md Step 3"
  - "HANDOFF.md §2"
  - "notes/geometric-core.md §E"
  - "notes/x-classification.md §2"
  - "notes/broken-born-theory.md §2"
  - "review/wiki-build-flags.md items 3, 23, 55"
  - "notes/gate-mechanism.md §2"
  - "notes/gate-mechanism.md §3"
---

*The modular field Z = X + iY is a complex symmetric matrix field that, in the program, carries the whole geometry of phase space at each point of spacetime once only the symplectic form is held rigid. Each value of Z is a point of [the Siegel domain](siegel-domain.md) and names one phase-space metric compatible with that form. The program reads the imaginary part Y as the spacetime metric g, and the real part X as a new symmetric tensor field, [the momentum graviton](../../gravity/momentum-graviton/_index.md), which records how far the split between position and momentum tilts from place to place. In the vacuum X = 0 and Z = i·g. These readings are the program's derived claims, tagged structural in the note that introduced them; the algebra of the parametrization is machine-checked, and later notes show that X must be a massive spin-2 field.*

**Status:** Alive — the identifications are derived [D] ([#11](../../history/documents/checkpoint.md) [§6](../../papers/broken-born-checkpoint-v2.md#6-the-modular-field); calc note [#5 §C](../../../notes/geometric-core.md#c-the-modular-field-d--structural-math-facts-standard) heads them "[D — structural; math facts standard]"); only the parametrization identities, such as I[Z]² = −1, are machine-checked [V] (battery test T2, at one sampled point; [the verification battery](../../method/verification/battery.md)).

## The claim

[#11 §6](../../papers/broken-born-checkpoint-v2.md#6-the-modular-field): "With only ω rigid, H ranges over Sp(2d,ℝ)/U(d): Z = X + iY (symmetric; Y > 0), H_Z the standard generalized metric (I[Z]² = −1 machine-verified [V]). Identifications [D]: **Im Z = g**; the η-compatible locus X = 0 is the vacuum slice of §5. **Re Z = X**, the momentum graviton — the fluctuation of the emergent polarization."

The same paragraph goes on to reciprocity acting as Z → −Z⁻¹ and to the dark-energy field on the domain's boundary. Those claims have their own pages: [reciprocity as modular inversion](modular-inversion.md) and [τ as the Maslov phase of the boundary](maslov-phase.md).

## How the field arises

### Step 1: the postulate repair frees the metric

The program's phase space carries three structures: the [symplectic form](../reciprocity/symplectic-form.md) ω, a neutral metric η, and a positive generalized metric H ([the structures ω, η, H](../born-geometry/born-structures.md)). When ω and η are both held rigid, [the compatibility theorem](../born-geometry/compatibility-theorem.md) leaves only H = diag(g, g⁻¹) with g positive definite: the momentum metric is the inverse of the position metric and nothing else can vary. Calc note #5 found that this rigid version has no [Lagrangian Grassmannian](lagrangian-grassmannian.md), no Maslov circle and no dark-energy field, and that the program then reduces to [general relativity](../../gravity/spin-2-fields/general-relativity.md) plus one bespoke model of [self-interacting dark matter](../../dark-matter/halo-astrophysics/self-interacting-dark-matter.md) ("Branch R", [§B](../../../notes/geometric-core.md#b-the-inconsistency-and-the-forced-repair-d--structural); [original P2](../../program/postulates/original-p2.md); [the nontriviality theorem](../../program/postulates/nontriviality-theorem.md)).

The repair, [P2′](../../program/postulates/p2-prime.md), keeps only ω rigid. [#5 §C](../../../notes/geometric-core.md#c-the-modular-field-d--structural-math-facts-standard): "With P2′, the dynamical space opens up: positive H compatible with ω alone form the **Siegel domain** Sp(2d,ℝ)/U(d), coordinatized by a complex symmetric matrix"

```text
Z = X + iY,   Y > 0

H_Z = [[ Y + XY⁻¹X ,  XY⁻¹ ],
       [ Y⁻¹X      ,  Y⁻¹  ]]
```

The space and its parametrization are standard mathematics, explained on [the Siegel domain](siegel-domain.md).

### Step 2: the coordinate becomes a field

H is a field, so its coordinate Z is one too: at each point of the section on which the fields live (the half of phase space the lab notebook calls a Lagrangian leaf, [#1 §2](../../../notes/broken-born-theory.md#2-kinematic-core); [the section condition](../../symmetry-breaking/section-condition.md)), Z is a complex symmetric d × d matrix. At d = 4, X and Y have ten real components each, the counts calc note #5 lists for the momentum graviton and the graviton ([§D](../../../notes/geometric-core.md#d-quadratic-spectrum-and-the-ghost-question-partial)). The rest of the page is about what the two halves mean.

### Step 3: Im Z = g, and the vacuum slice

[#5 §C](../../../notes/geometric-core.md#c-the-modular-field-d--structural-math-facts-standard): "**Im Z = Y = g**, the spacetime metric. At X = 0, H = diag(g, g⁻¹): the η-compatible locus of Theorem A is precisely the vacuum slice."

Setting X = 0 in H_Z leaves diag(Y, Y⁻¹), which is exactly the form the compatibility theorem allows, with g = Y. So the slice X = 0 is where η is again compatible with H, and on it Y plays the part of the metric that the lab notebook's action had split off as "a spacetime metric g_μν(x)" ([#1 §3](../../../notes/broken-born-theory.md#3-action), tagged [D, schematic]). Calc note [#6](../../../notes/x-classification.md) places the vacuum there: "The vacuum ⟨Z⟩ = i·g sits at X = 0" ([§3](../../../notes/x-classification.md#3-the-mass-mechanism-and-the-endpoint-d--structural)). The momentum metric on the slice is Y⁻¹ = g⁻¹, the slaved momentum metric of [the compatibility corollaries](../born-geometry/compatibility-corollaries.md).

### Step 4: Re Z = X, the new field

[#5 §C](../../../notes/geometric-core.md#c-the-modular-field-d--structural-math-facts-standard): "**Re Z = X**, a *new symmetric tensor*: the momentum graviton. It is exactly the fluctuation that breaks η-compatibility — i.e., the local wobble of the emergent polarization, 'which way the x/p split points, here.'"

The algebra behind the words: away from the slice, H_Z has off-diagonal blocks XY⁻¹ and Y⁻¹X that couple position directions to momentum directions. Such a metric is still compatible with ω but no longer with η. The [round-3](../../method/review/round-3/_index.md) audit tested this with its own code over 2000 random trials at each of d = 3 and d = 4: "omega-only family (Siegel, X != 0): omega residual <= 3e-14 but eta residual >= 0.52 (d=3), 1.87 (d=4)" ([`review/round3/referee/audit-notes.md`](../../../review/round3/referee/audit-notes.md) Step 3). X therefore measures, point by point, how far the metric departs from the position/momentum split that the vacuum's η defines: the "local wobble of the emergent polarization".

[The tuning test](../../gravity/tuning-test/_index.md) later made the misalignment explicit. It measures the mismatch between the vacuum polarization J₀ and I[Z] = ω⁻¹H_Z by their anticommutator, {J₀, I[Z]} = [[S, A], [A, S]], with S = Y + XY⁻¹X − Y⁻¹ and A = [X, Y⁻¹] ([#7 §2](../../../notes/tuning-test.md#2-explicit-computation-metric-tier-d--rigorous); battery test T3), and "The compatible locus is X = 0 *and* Y = Y⁻¹" (on that locus, see flag 3 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md)). The energy cost of that misalignment is what gives X its mass ([the misalignment potential](../../gravity/tuning-test/misalignment-potential.md)).

Calc note #5 also calls Re Z the "gate mediator": exchange of X between two [conjugate-matter](../../dark-matter/conjugate-matter/_index.md) particles produces the [velocity gate](../../dark-matter/conjugate-matter/velocity-gate.md) of the dark-matter sector ([§E](../../../notes/geometric-core.md#e-the-gate-problem--the-mechanism-found-d--structural); [the gate mechanism](../../dark-matter/conjugate-matter/gate-mechanism.md)). [`notes/gate-mechanism.md`](../../../notes/gate-mechanism.md) (2026-10-28; two derivations, the second blind; not reviewed) finds that exchanging X as [#11 §7](../../papers/broken-born-checkpoint-v2.md#7-the-massive-momentum-graviton) builds it cannot produce the gate: every on-shell vertex depends only on the momentum transfer, and the section condition makes X depend on position only (§§2–3). Flag 55 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md), pending, proposes [P] for the gate and μ and [O] for the mechanism; [#11 §8](../../papers/broken-born-checkpoint-v2.md#8-conjugate-matter-and-the-gate) tags the mechanism [D] and the shape [O] ([the gate mechanism](../../dark-matter/conjugate-matter/gate-mechanism.md#exchanging-x-cannot-produce-the-gate)).

### Step 5: one field for the geometric program [D — structural]

[#5 §C](../../../notes/geometric-core.md#c-the-modular-field-d--structural-math-facts-standard): "One object now carries the whole geometric program: **metric (Im Z), momentum geometry and gate mediator (Re Z), scale-factor duality (|Z|), dark energy (boundary phase of Z).**"

| Part of Z | Reading in the program | Where it is set out |
| --- | --- | --- |
| Im Z = Y | the spacetime metric g | this page |
| Re Z = X | [momentum-space geometry](../reciprocity/curved-momentum-space.md); the mediator of the dark-matter gate (disputed, flag 55) | this page; [the gate mechanism](../../dark-matter/conjugate-matter/gate-mechanism.md) |
| the circle \|Z\| = 1 | [scale-factor duality](../../cosmology/scale-factor-duality/_index.md), the constraint a·ã = 1 (queried in flag 23 of [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md)) | [modular inversion](modular-inversion.md); [the cosmological constraint](../../cosmology/scale-factor-duality/cosmological-constraint.md) |
| the phase of Z's boundary value | the dark-energy field τ | [τ as the Maslov phase](maslov-phase.md) |

The note's closing summary counts "the modular unification (reciprocity = Z → −Z⁻¹, cosmological duality = |Z| = 1)" among its results (§F). The identification of the |Z| = 1 circle with a·ã = 1 is queried in flag 23 of [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md). The unification is tagged structural: it says where each part sits in one parametrization, and the dynamics of each part are worked out separately, on the pages the table links.

## What X became

Calc note #5 left open whether X propagates healthily, is auxiliary, or is a [ghost](../../gravity/spin-2-fields/ghosts.md) ([§D](../../../notes/geometric-core.md#d-quadratic-spectrum-and-the-ghost-question-partial)). The next three notes settled it by symmetry and consistency arguments; the chain is set out under [the momentum graviton](../../gravity/momentum-graviton/_index.md).

1. **Shift symmetry.** The translations Z → Z + B of the Siegel domain shift X and leave Y alone, so "X has no potential and no non-derivative couplings from the geometric sector alone — it is axion-like — and 'auxiliary X' (the soft outcome 2) is off the table at the fundamental level" ([#6 §1](../../../notes/x-classification.md#1-the-shift-symmetry-d--rigorous); [shift symmetry](../../gravity/momentum-graviton/shift-symmetry.md)).
2. **A second graviton.** Locally the shifts become dual diffeomorphisms, δX_μν = ∂₍μλ_ν₎, "a second copy of linearized diffeomorphisms" because X is symmetric ([#6 §2](../../../notes/x-classification.md#2-the-gauge-structure-and-the-no-go-d--t); [dual diffeomorphisms](../../gravity/momentum-graviton/dual-diffeomorphisms.md)).
3. **No massless or ungauged X.** "Massless X is excluded by the multi-graviton no-go [8†]; ungauged X by Lorentz signature" ([#11 §7.1](../../papers/broken-born-checkpoint-v2.md#71-the-chain-d--t); [the multi-graviton no-go](../../gravity/spin-2-fields/multi-graviton-no-go.md); [the signature obstruction](../../gravity/spin-2-fields/signature-obstruction.md); [why X must be massive](../../gravity/momentum-graviton/forcing-chain.md)).
4. **Mass from the polarization.** "The vacuum ⟨Z⟩ = i·g sits at X = 0 and is *moved* by the shifts: the polarization selection (η-emergence) **spontaneously breaks the local dual diffeomorphisms**", and X becomes "a **massive spin-2** with its five polarizations" ([#6 §3](../../../notes/x-classification.md#3-the-mass-mechanism-and-the-endpoint-d--structural); [the gravitational Higgs mechanism](../../gravity/momentum-graviton/gravitational-higgs.md)).
5. **Its dynamics.** The tuning test passes on a condition, in first-order (frame) variables, and the picture that emerges is [Hassan–Rosen bimetric gravity](../../gravity/spin-2-fields/hassan-rosen-bimetric.md) with the second frame confined to the compact Λ(d) ([constrained bimetric gravity](../../gravity/tuning-test/constrained-bimetric.md)). Reciprocity makes X odd: "Momentum-space geometry is carried by X = Re Z, the reciprocity-odd partner of the metric. It is a **massive spin-2 field**" ([#8 §4](../../../notes/beta-coefficients.md#4-the-field-equation-problem-the-answer-to-born); [spectrum and parity](../../gravity/momentum-graviton/spectrum-and-parity.md); [Born's answer](../../gravity/momentum-graviton/borns-answer.md)).

## Open: the Re Z sector of the geometric action (OP1)

Calc note #5 restated the lab notebook's first main problem in terms of Z: "The field-equation problem, restated exactly: *the field equation for momentum-space geometry is the Re Z sector of S_H.*" (§C). The problem is the lab notebook's first open problem, "The field equation for H beyond minisuperspace — the question Born left open in 1938" ([#1 §11](../../../notes/broken-born-theory.md#11-open-problems-in-order-of-severity); [the three main problems](../../history/main-problems.md)). S_H is the notebook's geometric action, written with ω and η both frozen ([the geometric action S_H](../../gravity/tuning-test/geometric-action.md), superseded).

Calc note #5 also defined the direct route ([§D](../../../notes/geometric-core.md#d-quadratic-spectrum-and-the-ghost-question-partial)): "expand the generalized curvature scalar of (ω, H_Z) to quadratic order in X about X = 0 on the section, with ω-generalized diffeomorphisms as the gauge symmetry". No document reports that expansion; calc note #6 classified X by symmetry and no-go arguments instead, and the tuning test selected the ghost-free class by minimality and consistency. [#11 §14](../../papers/broken-born-checkpoint-v2.md#14-open-problems) keeps the gap open as item 1: "First-principles reduction of the frame-tier wedge sector from S_H (class selected, not derived) [O]" ([Open: deriving the wedge sector from S_H](../../gravity/tuning-test/wedge-reduction.md)). S_H also presupposes the Born connection, whose uniqueness is proved for the full triple (ω, η, H) but not for the (ω, H)-only structure of P2′ ([#5 §F item 5](../../../notes/geometric-core.md#f-status-after-tonight); [the Born connection](../born-geometry/born-connection.md)). Both appear on [open problems and the queue](../../status/open-problems.md).

## Scope and caveats

- **Positive metrics only.** Calc note #6: "the compatibility theorem and Siegel parametrization were derived for positive H. Lorentzian g makes the stabilizer U(1, d−1) and the invariant target metric indefinite" ([#6 §3](../../../notes/x-classification.md#3-the-mass-mechanism-and-the-endpoint-d--structural)). The extension to spacetime signature is open item 3 ([Open: Lorentzian dressing](../born-geometry/lorentzian-dressing.md)).
- **What the machine checks.** Battery test T2 checks I[Z]² = −1, the symmetry and positivity of H_Z and det H_Z = 1 at one sampled point at d = 4; [`verify/toy_coset.py`](../../../verify/toy_coset.py) checks the d = 1 parametrization symbolically ([the toy-model scripts](../../method/verification/toy-model-scripts.md)). The identifications are readings, "each checkable against everything derived so far" ([#5 §C](../../../notes/geometric-core.md#c-the-modular-field-d--structural-math-facts-standard)) and "each cross-checked against the independent derivations elsewhere in the arc [D]" ([#9 §4](../../../notes/broken-born-program-v1.md#4-the-modular-field)). A script confirms the algebra, not the reading ([verification confirms arithmetic, not the model](../../method/verification/arithmetic-not-model.md)).
- **The round-3 auditor's caution.** Of the compatibility theorem, the blind auditor wrote: "It is a pointwise linear-algebra fact; it does not by itself establish any physics (the identification of a dynamical H, a rigid eta, and a second spin-2 field X is assumed, not derived)" ([`review/round3/referee/audit-notes.md`](../../../review/round3/referee/audit-notes.md) Step 3). Two of the steps it names, a dynamical H and X as a second spin-2 field, are the ones this page records. The round-3 adjudication did not rule on the remark; the broader critique is [the "framework does no work" critique](../../program/framework-does-no-work.md).

## History

- **Lab notebook, v0.3 addendum.** Z entered with the P2 → P2′ correction: τ and the Grassmannian are "restored, now as the boundary phase of a single **modular field** Z = X + iY on the Siegel domain Sp(2d,ℝ)/U(d): Im Z = g (the metric), Re Z = X (the momentum graviton — the local fluctuation of the emergent polarization)" ([the lab notebook](../../history/documents/lab-notebook.md)).
- **Calc note #5** (an overnight working note) gives the argument above in [§C](../../../notes/geometric-core.md#c-the-modular-field-d--structural-math-facts-standard) and lists "The field-equation problem reframed from slogan to a specific sector of a specific field (Re Z)" among its results ([§F](../../../notes/geometric-core.md#f-status-after-tonight); [the field-equation notes](../../history/documents/field-equation-notes.md)).
- **[#9 §4](../../../notes/broken-born-program-v1.md#4-the-modular-field)** restates the identifications, with the parametrization "verified explicitly: I[Z]² = −1".
- **[#11 §6](../../papers/broken-born-checkpoint-v2.md#6-the-modular-field)** is the current statement. [`HANDOFF.md` §2](../../../HANDOFF.md#2-scientific-state-one-screen) lists the modular field among the results that stand, marked "✓ (parametrization identities)": the check mark covers the algebra, not the readings.

## Sources

- [`wiki/papers/broken-born-checkpoint-v2.md` §6](../../papers/broken-born-checkpoint-v2.md#6-the-modular-field) — the identifications [D] and the [V] on I[Z]² = −1.
- [`notes/geometric-core.md` §C](../../../notes/geometric-core.md#c-the-modular-field-d--structural-math-facts-standard) — the Siegel domain under P2′, Im Z = g, Re Z = X, the modular unification, the field-equation problem restated.
- [`notes/geometric-core.md` §B](../../../notes/geometric-core.md#b-the-inconsistency-and-the-forced-repair-d--structural), [§D](../../../notes/geometric-core.md#d-quadratic-spectrum-and-the-ghost-question-partial), [§E](../../../notes/geometric-core.md#e-the-gate-problem--the-mechanism-found-d--structural), [§F](../../../notes/geometric-core.md#f-status-after-tonight) — Branch R; the unperformed curvature expansion and the field counts; Re Z as the gate mediator; the night's closing summary and open item 5.
- [`notes/x-classification.md` §1](../../../notes/x-classification.md#1-the-shift-symmetry-d--rigorous), [§2](../../../notes/x-classification.md#2-the-gauge-structure-and-the-no-go-d--t), [§3](../../../notes/x-classification.md#3-the-mass-mechanism-and-the-endpoint-d--structural) — the shift symmetry; the dual diffeomorphisms; the vacuum ⟨Z⟩ = i·g at X = 0, the Higgs mechanism and the positive-H caveat.
- [`notes/tuning-test.md` §2](../../../notes/tuning-test.md#2-explicit-computation-metric-tier-d--rigorous) — {J₀, I[Z]} = [[S, A], [A, S]] and the compatible locus.
- [`notes/beta-coefficients.md` §4](../../../notes/beta-coefficients.md#4-the-field-equation-problem-the-answer-to-born) — "X = Re Z, the reciprocity-odd partner of the metric".
- [`wiki/papers/broken-born-checkpoint-v2.md` §7](../../papers/broken-born-checkpoint-v2.md#7-the-massive-momentum-graviton), [§8](../../papers/broken-born-checkpoint-v2.md#8-conjugate-matter-and-the-gate), [§14](../../papers/broken-born-checkpoint-v2.md#14-open-problems) — the chain that makes X massive; the tags on the gate's mechanism and shape; open item 1.
- [`notes/broken-born-program-v1.md` §4](../../../notes/broken-born-program-v1.md#4-the-modular-field) — the same identifications in #9.
- [`notes/broken-born-theory.md`](../../../notes/broken-born-theory.md) v0.3 addendum, [§2](../../../notes/broken-born-theory.md#2-kinematic-core), [§3](../../../notes/broken-born-theory.md#3-action), [§11](../../../notes/broken-born-theory.md#11-open-problems-in-order-of-severity) — the introduction of Z with P2′; fields on a Lagrangian leaf; the v0.1 metric split; the field-equation problem.
- [`verify/battery.py`](../../../verify/battery.py) T2 — the parametrization identities at one sampled point.
- [`review/round3/referee/audit-notes.md`](../../../review/round3/referee/audit-notes.md) Step 3 — X ≠ 0 breaks η-compatibility numerically; the auditor's caution.
- [`HANDOFF.md` §2](../../../HANDOFF.md#2-scientific-state-one-screen) — the handoff's one-screen state, with the check mark on the parametrization identities.
- [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md) items 3, 23 — the query on #7's compatible locus; the query on the identification of |Z| = 1 with a·ã = 1, with its executed check [`review/wiki-build-checks/self_dual_locus.py`](../../../review/wiki-build-checks/self_dual_locus.py); item 55 — the gate's mechanism not derived, pending.
- [`notes/gate-mechanism.md` §2](../../../notes/gate-mechanism.md#2-exchanging-the-x-of-7-cannot-produce-the-gate), [§3](../../../notes/gate-mechanism.md#3-the-fiber-overlap-read-two-ways) — exchanging X gives no gate; X depends on position only under the section condition.
