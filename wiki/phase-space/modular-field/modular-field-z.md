---
title: "The modular field Z = X + iY"
weight: 20
status: alive
description: "Once only ω is rigid, all of phase-space geometry fits one complex field: Im Z = g is the spacetime metric (the vacuum slice X = 0, ⟨Z⟩ = i·g) and Re Z = X is the local tilt of the position/momentum split, the momentum graviton."
provenance: [D]
sources:
  - "papers/broken-born-checkpoint-v2.md §6"
  - "notes/debt1a-geometric-core.md §C"
  - "notes/debt1a-geometric-core.md §B"
  - "notes/debt1a-geometric-core.md §D"
  - "notes/debt1a-geometric-core.md §F"
  - "notes/debt1a-ii-X-classification.md §1"
  - "notes/debt1a-ii-X-classification.md §3"
  - "notes/debt1a-iii-tuning-test.md §2"
  - "notes/debt1a-iv-beta-coefficients.md §4"
  - "papers/broken-born-checkpoint-v2.md §7"
  - "papers/broken-born-checkpoint-v2.md §14"
  - "notes/broken-born-program-v1.md §4"
  - "notes/broken-born-theory.md 'Addendum (v0.3, overnight): axiom correction and the modular core'"
  - "notes/broken-born-theory.md §3"
  - "notes/broken-born-theory.md §11"
  - "verify/battery.py T2"
  - "review/round3/referee/audit-notes.md Step 3"
  - "HANDOFF.md §2"
---

*The modular field Z = X + iY is a complex symmetric matrix field that, in the program, carries the whole geometry of phase space at each point of spacetime once only the symplectic form is held rigid. Each value of Z is a point of [the Siegel domain](/wiki/phase-space/modular-field/siegel-domain) and names one phase-space metric compatible with that form. The program reads the imaginary part Y as the spacetime metric g, and the real part X as a new symmetric tensor field, the momentum graviton, which records how far the split between position and momentum tilts from place to place. In the vacuum X = 0 and Z = i·g. These readings are the program's derived claims, tagged structural in the note that introduced them; the algebra of the parametrization is machine-checked, and later notes show that X must be a massive spin-2 field.*

**Status:** Alive — the identifications are derived [D] (#11 §6; calc note #5 §C heads them "[D — structural; math facts standard]"); only the parametrization identities, such as I[Z]² = −1, are machine-checked [V] (battery test T2, at one sampled point; [the verification battery](/wiki/method/verification/battery)).

## The claim

#11 §6: "With only ω rigid, H ranges over Sp(2d,ℝ)/U(d): Z = X + iY (symmetric; Y > 0), H_Z the standard generalized metric (I[Z]² = −1 machine-verified [V]). Identifications [D]: **Im Z = g**; the η-compatible locus X = 0 is the vacuum slice of §5. **Re Z = X**, the momentum graviton — the fluctuation of the emergent polarization."

The same paragraph goes on to reciprocity acting as Z → −Z⁻¹ and to the dark-energy field on the domain's boundary. Those claims have their own pages: [reciprocity as modular inversion](/wiki/phase-space/modular-field/modular-inversion) and [τ as the Maslov phase of the boundary](/wiki/phase-space/modular-field/maslov-phase).

## How the field arises

### Step 1: the postulate repair frees the metric

The program's phase space carries three structures: the [symplectic form](/wiki/phase-space/reciprocity/symplectic-form) ω, a neutral metric η, and a positive generalized metric H ([the structures ω, η, H](/wiki/phase-space/born-geometry/born-structures)). When ω and η are both held rigid, [the compatibility theorem](/wiki/phase-space/born-geometry/compatibility-theorem) leaves only H = diag(g, g⁻¹) with g positive definite: the momentum metric is the inverse of the position metric and nothing else can vary. Calc note #5 found that this rigid version has no Lagrangian Grassmannian, no Maslov circle and no dark-energy field, and that the program then reduces to general relativity plus one bespoke model of self-interacting dark matter ("Branch R", §B; [original P2](/wiki/program/postulates/original-p2); [the nontriviality theorem](/wiki/program/postulates/nontriviality-theorem)).

The repair, [P2′](/wiki/program/postulates/p2-prime), keeps only ω rigid. #5 §C: "With P2′, the dynamical space opens up: positive H compatible with ω alone form the **Siegel domain** Sp(2d,ℝ)/U(d), coordinatized by a complex symmetric matrix"

```text
Z = X + iY,   Y > 0

H_Z = [[ Y + XY⁻¹X ,  XY⁻¹ ],
       [ Y⁻¹X      ,  Y⁻¹  ]]
```

The space and its parametrization are standard mathematics, explained on [the Siegel domain](/wiki/phase-space/modular-field/siegel-domain).

### Step 2: the coordinate becomes a field

H is a field, so its coordinate Z is one too: at each point of the section on which the fields live (the half of phase space the lab notebook calls a Lagrangian leaf, #1 §2), Z is a complex symmetric d × d matrix. At d = 4, X and Y have ten real components each, the counts calc note #5 lists for the momentum graviton and the graviton (§D). The rest of the page is about what the two halves mean.

### Step 3: Im Z = g, and the vacuum slice

#5 §C: "**Im Z = Y = g**, the spacetime metric. At X = 0, H = diag(g, g⁻¹): the η-compatible locus of Theorem A is precisely the vacuum slice."

Setting X = 0 in H_Z leaves diag(Y, Y⁻¹), which is exactly the form the compatibility theorem allows, with g = Y. So the slice X = 0 is where η is again compatible with H, and on it Y plays the part of the metric that the lab notebook's action had split off as "a spacetime metric g_μν(x)" (#1 §3, tagged [D, schematic]). Calc note #6 places the vacuum there: "The vacuum ⟨Z⟩ = i·g sits at X = 0" (§3). The momentum metric on the slice is Y⁻¹ = g⁻¹, the slaved momentum metric of [the compatibility corollaries](/wiki/phase-space/born-geometry/compatibility-corollaries).

### Step 4: Re Z = X, the new field

#5 §C: "**Re Z = X**, a *new symmetric tensor*: the momentum graviton. It is exactly the fluctuation that breaks η-compatibility — i.e., the local wobble of the emergent polarization, 'which way the x/p split points, here.'"

The algebra behind the words: away from the slice, H_Z has off-diagonal blocks XY⁻¹ and Y⁻¹X that couple position directions to momentum directions. Such a metric is still compatible with ω but no longer with η. The round-3 audit tested this with its own code over 2000 random trials at each of d = 3 and d = 4: "omega-only family (Siegel, X != 0): omega residual <= 3e-14 but eta residual >= 0.52 (d=3), 1.87 (d=4)" (`review/round3/referee/audit-notes.md` Step 3). X therefore measures, point by point, how far the metric departs from the position/momentum split that the vacuum's η defines: the "local wobble of the emergent polarization".

The tuning test later made the misalignment explicit. It measures the mismatch between the vacuum polarization J₀ and I[Z] = ω⁻¹H_Z by their anticommutator, {J₀, I[Z]} = [[S, A], [A, S]], with S = Y + XY⁻¹X − Y⁻¹ and A = [X, Y⁻¹] (#7 §2; battery test T3), and "The compatible locus is X = 0 *and* Y = Y⁻¹". The energy cost of that misalignment is what gives X its mass ([the misalignment potential](/wiki/gravity/tuning-test/misalignment-potential)).

Calc note #5 also calls Re Z the "gate mediator": exchange of X between two conjugate-matter particles produces the velocity gate of the dark-matter sector (§E; [the gate mechanism](/wiki/dark-matter/conjugate-matter/gate-mechanism)).

### Step 5: one field for the geometric program [D — structural]

#5 §C: "One object now carries the whole geometric program: **metric (Im Z), momentum geometry and gate mediator (Re Z), scale-factor duality (|Z|), dark energy (boundary phase of Z).**"

| Part of Z | Reading in the program | Where it is set out |
| --- | --- | --- |
| Im Z = Y | the spacetime metric g | this page |
| Re Z = X | momentum-space geometry; the mediator of the dark-matter gate | this page; [the gate mechanism](/wiki/dark-matter/conjugate-matter/gate-mechanism) |
| the circle \|Z\| = 1 | scale-factor duality, the constraint a·ã = 1 | [modular inversion](/wiki/phase-space/modular-field/modular-inversion); [the cosmological constraint](/wiki/cosmology/scale-factor-duality/cosmological-constraint) |
| the phase of Z's boundary value | the dark-energy field τ | [τ as the Maslov phase](/wiki/phase-space/modular-field/maslov-phase) |

The note's closing summary counts "the modular unification (reciprocity = Z → −Z⁻¹, cosmological duality = |Z| = 1)" among that night's results (§F). The unification is tagged structural: it says where each part sits in one parametrization, and the dynamics of each part are worked out separately, on the pages the table links.

## What X became

Calc note #5 left open whether X propagates healthily, is auxiliary, or is a ghost (§D). The next three notes settled it by symmetry and consistency arguments; the chain is set out under [the momentum graviton](/wiki/gravity/momentum-graviton).

1. **Shift symmetry.** The translations Z → Z + B of the Siegel domain shift X and leave Y alone, so "X has no potential and no non-derivative couplings from the geometric sector alone — it is axion-like — and 'auxiliary X' (the soft outcome 2) is off the table" (#6 §1; [shift symmetry](/wiki/gravity/momentum-graviton/shift-symmetry)).
2. **A second graviton.** Locally the shifts become dual diffeomorphisms, δX_μν = ∂₍μλ_ν₎, "a second copy of linearized diffeomorphisms" because X is symmetric (#6 §2; [dual diffeomorphisms](/wiki/gravity/momentum-graviton/dual-diffeomorphisms)).
3. **No massless or ungauged X.** "Massless X is excluded by the multi-graviton no-go [8†]; ungauged X by Lorentz signature" (#11 §7.1; [the multi-graviton no-go](/wiki/gravity/spin-2-fields/multi-graviton-no-go); [why X must be massive](/wiki/gravity/momentum-graviton/forcing-chain)).
4. **Mass from the polarization.** "The vacuum ⟨Z⟩ = i·g sits at X = 0 and is *moved* by the shifts: the polarization selection (η-emergence) **spontaneously breaks the local dual diffeomorphisms**", and X becomes "a **massive spin-2** with its five polarizations" (#6 §3; [the gravitational Higgs mechanism](/wiki/gravity/momentum-graviton/gravitational-higgs)).
5. **Its dynamics.** The tuning test passes on a condition, in first-order (frame) variables, and the picture that emerges is Hassan–Rosen bimetric gravity with the second frame confined to the compact Λ(d) ([constrained bimetric gravity](/wiki/gravity/tuning-test/constrained-bimetric)). Reciprocity makes X odd: "Momentum-space geometry is carried by X = Re Z, the reciprocity-odd partner of the metric. It is a **massive spin-2 field**" (#8 §4; [spectrum and parity](/wiki/gravity/momentum-graviton/spectrum-and-parity); [Born's answer](/wiki/gravity/momentum-graviton/borns-answer)).

## Open: the Re Z sector of the geometric action (OP1)

Calc note #5 restated the lab notebook's first debt in terms of Z: "Born's debt, restated exactly: *the field equation for momentum-space geometry is the Re Z sector of S_H.*" (§C). The debt is the lab notebook's first open problem, "The field equation for H beyond minisuperspace — Born's 88-year debt" (#1 §11; [the three debts](/wiki/history/debts)). S_H is the notebook's geometric action, written with ω and η both frozen ([the geometric action S_H](/wiki/gravity/tuning-test/geometric-action), superseded).

Calc note #5 also defined the direct route (§D): "expand the generalized curvature scalar of (ω, H_Z) to quadratic order in X about X = 0 on the section, with ω-generalized diffeomorphisms as the gauge symmetry". No document reports that expansion; calc note #6 classified X by symmetry and no-go arguments instead, and the tuning test selected the ghost-free class by minimality and consistency. #11 §14 keeps the gap open as item 1: "First-principles reduction of the frame-tier wedge sector from S_H (class selected, not derived) [O]" ([Open: deriving the wedge sector from S_H](/wiki/gravity/tuning-test/wedge-reduction)). S_H also presupposes the Born connection, whose uniqueness is proved for the full triple (ω, η, H) but not for the (ω, H)-only structure of P2′ (#5 §F item 5; [the Born connection](/wiki/phase-space/born-geometry/born-connection)). Both appear on [open problems and the queue](/wiki/status/open-problems).

## Scope and caveats

- **Positive metrics only.** Calc note #6: "the compatibility theorem and Siegel parametrization were derived for positive H. Lorentzian g makes the stabilizer U(1, d−1) and the invariant target metric indefinite" (#6 §3). The extension to spacetime signature is open item 3 ([Open: Lorentzian dressing](/wiki/phase-space/born-geometry/lorentzian-dressing)).
- **What the machine checks.** Battery test T2 checks I[Z]² = −1, the symmetry and positivity of H_Z and det H_Z = 1 at one sampled point at d = 4; `verify/toy_coset.py` checks the d = 1 parametrization symbolically. The identifications are readings, "each checkable against everything derived so far" (#5 §C) and "each cross-checked against the independent derivations elsewhere in the arc [D]" (#9 §4). A script confirms the algebra, not the reading ([verification confirms arithmetic, not the model](/wiki/method/verification/arithmetic-not-model)).
- **The round-3 auditor's caution.** Of the compatibility theorem, the blind auditor wrote: "It is a pointwise linear-algebra fact; it does not by itself establish any physics (the identification of a dynamical H, a rigid eta, and a second spin-2 field X is assumed, not derived)" (`review/round3/referee/audit-notes.md` Step 3). Two of the steps it names, a dynamical H and X as a second spin-2 field, are the ones this page records. The round-3 adjudication did not rule on the remark; the broader critique is [the "framework does no work" critique](/wiki/program/framework-does-no-work).

## History

- **Lab notebook, v0.3 addendum.** Z entered with the P2 → P2′ correction: τ and the Grassmannian are "restored, now as the boundary phase of a single **modular field** Z = X + iY on the Siegel domain Sp(2d,ℝ)/U(d): Im Z = g (the metric), Re Z = X (the momentum graviton — the local fluctuation of the emergent polarization)" ([the lab notebook](/wiki/history/documents/lab-notebook)).
- **Calc note #5** (an overnight working note) gives the argument above in §C and books "Born's debt reframed from slogan to a specific sector of a specific field (Re Z)" among its results (§F; [the Debt-1 notes](/wiki/history/documents/debt-1-notes)).
- **#9 §4** restates the identifications, with the parametrization "verified explicitly: I[Z]² = −1".
- **#11 §6** is the current statement. `HANDOFF.md` §2 lists the modular field among the results that stand, marked "✓ (parametrization identities)": the check mark covers the algebra, not the readings.

## Sources

- `papers/broken-born-checkpoint-v2.md` §6 — the identifications [D] and the [V] on I[Z]² = −1.
- `notes/debt1a-geometric-core.md` §C — the Siegel domain under P2′, Im Z = g, Re Z = X, the modular unification, Born's debt restated.
- `notes/debt1a-geometric-core.md` §B, §D, §F — Branch R; the unperformed curvature expansion and the field counts; the night's closing summary and open item 5.
- `notes/debt1a-ii-X-classification.md` §1, §3 — the shift symmetry; the vacuum ⟨Z⟩ = i·g at X = 0, the Higgs mechanism and the positive-H caveat.
- `notes/debt1a-iii-tuning-test.md` §2 — {J₀, I[Z]} = [[S, A], [A, S]] and the compatible locus.
- `notes/debt1a-iv-beta-coefficients.md` §4 — "X = Re Z, the reciprocity-odd partner of the metric".
- `papers/broken-born-checkpoint-v2.md` §7, §14 — the chain that makes X massive; open item 1.
- `notes/broken-born-program-v1.md` §4 — the same identifications in #9.
- `notes/broken-born-theory.md` v0.3 addendum, §3, §11 — the introduction of Z with P2′; the v0.1 metric split; Born's debt.
- `verify/battery.py` T2 — the parametrization identities at one sampled point.
- `review/round3/referee/audit-notes.md` Step 3 — X ≠ 0 breaks η-compatibility numerically; the auditor's caution.
- `HANDOFF.md` §2 — the handoff's one-screen state, with the check mark on the parametrization identities.
