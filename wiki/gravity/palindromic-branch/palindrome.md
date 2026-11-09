---
title: "The palindrome βₙ = β₄₋ₙ"
weight: 10
status: alive
description: "On the broken vacuum reciprocity acts as the exchange of the wedge potential's two frames, 𝕏 → 𝕏⁻¹, which reverses the order of its five terms and forces β₀ = β₄ and β₁ = β₃: the interchange-symmetric branch of bimetric gravity, its ℤ₂ read as Born reciprocity."
provenance: [D]
sources:
  - "wiki/papers/broken-born-checkpoint-v2.md §7.3"
  - "wiki/papers/broken-born-checkpoint-v2.md §7.4"
  - "wiki/papers/broken-born-checkpoint-v2.md §1"
  - "wiki/papers/broken-born-checkpoint-v2.md §4"
  - "wiki/papers/broken-born-checkpoint-v2.md §6"
  - "wiki/papers/broken-born-checkpoint-v2.md §7.2"
  - "wiki/papers/broken-born-checkpoint-v2.md §7.5"
  - "wiki/papers/broken-born-checkpoint-v2.md §7 'Born's answer'"
  - "wiki/papers/broken-born-checkpoint-v2.md §15"
  - "notes/beta-coefficients.md §1"
  - "notes/beta-coefficients.md §2"
  - "notes/beta-coefficients.md §3"
  - "notes/tuning-test.md §2"
  - "notes/tuning-test.md §3"
  - "HANDOFF.md §2"
  - "verify/battery.py T5"
  - "review/v3-worklog.md item R7"
  - "notes/broken-born-theory.md 'Addendum (v0.6)'"
  - "notes/broken-born-program-v1.md §5"
  - "notes/broken-born-program-v1.md §11"
  - "review/wiki-build-flags.md item 39"
---

*The palindrome is the constraint βₙ = β₄₋ₙ on the five coefficients β₀ to β₄ of the potential that gives [the program's second spin-2 field](../momentum-graviton/_index.md) its mass: β₀ = β₄ and β₁ = β₃, with β₂ free, so the list of coefficients reads the same forwards and backwards. The potential couples two [frames](../spin-2-fields/vielbein-formulation.md), one built from the dynamical geometry and one determined by the [polarization](../../phase-space/reciprocity/lagrangian-polarizations.md) that the vacuum selects, and exchanging the two frames reverses the order of its five terms. The program's claim is that [Born reciprocity](../../phase-space/reciprocity/born-reciprocity.md), on the [broken vacuum](../../symmetry-breaking/_index.md), acts as exactly this exchange, so a potential invariant under reciprocity must be a palindrome. The constraint places the program's gravity sector in the interchange-symmetric branch of [bimetric gravity](../spin-2-fields/hassan-rosen-bimetric.md) and reads that branch's two-element exchange symmetry as Born reciprocity. It is a derivation of the program [D] with no machine check, and the branch itself is known in the literature, where it contains the [partially massless point](../spin-2-fields/partially-massless-gravity.md).*

**Status:** Alive — [D] — derived in [calc note #8](../../history/documents/field-equation-notes.md) [§1](../../../notes/beta-coefficients.md#1-what-reciprocity-does-to-the-wedge-potential-d) and restated in [checkpoint #11](../../history/documents/checkpoint.md) [§7.3](../../papers/broken-born-checkpoint-v2.md#73-palindrome-and-the-vacuum-energy-identity-dv). [#11](../../papers/broken-born-checkpoint-v2.md) tags [§7.3](../../papers/broken-born-checkpoint-v2.md#73-palindrome-and-the-vacuum-energy-identity-dv) as a whole [D][V], but the [V] belongs to the integer identity of [the vacuum-energy identity](vacuum-energy-identity.md) ([battery test T5](../../method/verification/battery.md)), which takes the palindrome as its input; no script checks the palindrome derivation itself. [#8](../../../notes/beta-coefficients.md)'s early description of the branch as an "ad hoc simplification" in the literature is superseded by the literature position of [#11 §7.4](../../papers/broken-born-checkpoint-v2.md#74-literature-position-updated-by-this-sessions-search--honesty-upgrade) ([below](#superseded-an-ad-hoc-branch-given-a-reason-to-exist)).

## Statement

[#11 §7.3](../../papers/broken-born-checkpoint-v2.md#73-palindrome-and-the-vacuum-energy-identity-dv): "Reciprocity acts on the wedge sector as frame exchange, forcing **βₙ = β₄₋ₙ**." Calc note [#8 §1](../../../notes/beta-coefficients.md#1-what-reciprocity-does-to-the-wedge-potential-d), under a heading tagged [D], boxes the constraint:

```text
βₙ = β₄₋ₙ          (β₀ = β₄,   β₁ = β₃,   β₂ free)
```

The five coefficients βₙ multiply the five terms of the potential. The constraint ties the last two to the first two and leaves the middle one free, so the list (β₀, β₁, β₂, β₁, β₀) reads the same in both directions; it removes two of the five free coefficients ([#8 §3](../../../notes/beta-coefficients.md#3-spectrum-parameters-selection-structure-d--t)). In the bimetric literature this is the "interchange-symmetric branch" ([#8 §1](../../../notes/beta-coefficients.md#1-what-reciprocity-does-to-the-wedge-potential-d)), and #11's technical abstract places the program's massive spin-2 field X, [the momentum graviton](../momentum-graviton/_index.md), "in the interchange-symmetric branch of Hassan–Rosen bimetric gravity [10†, 11†] with the second frame confined to Λ(4)" ([#11 §1](../../papers/broken-born-checkpoint-v2.md#1-two-abstracts)). [Hassan–Rosen bimetric gravity](../spin-2-fields/hassan-rosen-bimetric.md) is the [ghost-free](../spin-2-fields/ghosts.md) theory of two interacting metrics, and Λ(4) is [the Lagrangian Grassmannian](../../phase-space/modular-field/lagrangian-grassmannian.md), the compact space of polarizations.

## The potential it acts on

### Where the potential comes from

The program's [momentum graviton X](../momentum-graviton/_index.md) is a second spin-2 field that has to be massive ([why X must be massive](../momentum-graviton/forcing-chain.md)), and its mass comes from a potential that penalizes misalignment between the vacuum's polarization and the geometry. [The tuning test](../tuning-test/_index.md) asked whether that potential avoids the Boulware–Deser ghost, an extra mode with negative kinetic energy that generic nonlinear massive spin-2 theories carry [T] ([Fierz–Pauli and the Boulware–Deser ghost](../spin-2-fields/fierz-pauli.md)). Built from metrics, the potential fails; built from frames, it passes. The passing couplings are "wedge polynomials of the symplectic vielbein E (H = EᵀE) with the polarization frame E₀[J]", which "are the Hinterbichler–Rosen class [12†], ghost-free by construction" ([#11 §7.2](../../papers/broken-born-checkpoint-v2.md#72-the-tuning-test-dv); [the frame tier](../tuning-test/frame-tier.md); [the vielbein formulation](../spin-2-fields/vielbein-formulation.md)).

The pass fixed the form of the potential but not its coefficients. Calc note [#7](../../../notes/tuning-test.md): "What a pass does **not** yet deliver: the βₙ coefficients. Those follow from expanding the E–J wedge sector, and they determine M_X, the X–h mixing, and a vacuum-energy contribution. That coefficient computation is the closing stone of the field-equation problem." ([§3](../../../notes/tuning-test.md#3-the-frame-tier-d--structural-resting-on-t); [the conditional pass](../tuning-test/conditional-pass.md); [the three main problems](../../history/main-problems.md)). Calc note #8 is that closing note, and [the lab notebook](../../history/documents/lab-notebook.md) records it as "The coefficient computation is done" ([#1](../../../notes/broken-born-theory.md), v0.6 addendum). #8 constrains the βₙ instead of computing them from the wedge sector: reciprocity fixes two of them, the flat-vacuum condition of the next page fixes a third, and two remain free ([#8 §3](../../../notes/beta-coefficients.md#3-spectrum-parameters-selection-structure-d--t)).

### The potential

[#8 §1](../../../notes/beta-coefficients.md#1-what-reciprocity-does-to-the-wedge-potential-d) writes the sector in the form of [Hassan–Rosen bimetric gravity](../spin-2-fields/hassan-rosen-bimetric.md): "The Hinterbichler–Rosen sector for (e, f = E₀[J]) is"

```text
V = 2m²M² Σₙ₌₀⁴ βₙ eₙ(𝕏),        𝕏 = √(g⁻¹f)
exchange identity:   Sₙ(g, f) = S₄₋ₙ(f, g)
```

The two frames are e and f = E₀[J], the frame fixed by the polarization J; in 𝕏 the letters g and f stand for the metrics the two frames define, so the note uses f for both a frame and its metric. (The frame e is not one of the polynomials eₙ.) 𝕏 is the matrix square root of g⁻¹f [T]. The eₙ are the [elementary symmetric polynomials](../spin-2-fields/elementary-symmetric-polynomials.md) of the eigenvalues of 𝕏 [T]: e₀ = 1, e₁ is the sum of the four eigenvalues, e₂ the sum of their pairwise products, e₃ the sum of their triple products, and e₄ their product, the determinant of 𝕏. The βₙ are constants: "The Hassan–Rosen ghost-free family is *linear* combinations Σβₙeₙ(√(g⁻¹f)) (constants βₙ)" ([#7 §2](../../../notes/tuning-test.md#2-explicit-computation-metric-tier-d--rigorous)). The note defines neither the mass scales m and M nor the symbol Sₙ.

### Why exchanging the frames reverses the terms [T]

The sources state the exchange identity without its derivation, which is standard algebra [T]. Exchanging the two metrics replaces √(g⁻¹f) by √(f⁻¹g), which is 𝕏⁻¹. For a 4 × 4 matrix, the elementary symmetric polynomials of the inverse are those of the matrix in reverse order, divided by the determinant:

```text
eₙ(𝕏⁻¹) = e₄₋ₙ(𝕏) / det 𝕏
```

The identity holds because a product of n inverse eigenvalues equals the product of the other 4 − n eigenvalues divided by the product of all four. In the action each term of the potential carries the volume factor of g, √(−g), and the volume factor of f is √(−f) = √(−g)·det 𝕏 [T]. Under the exchange the determinant therefore cancels, and the n-th term of the potential density becomes the (4 − n)-th. Reading Sₙ(g, f) as the n-th term of the density, √(−g) eₙ(√(g⁻¹f)), this is the exchange identity, and a whole potential transforms as

```text
Σₙ βₙ Sₙ(g, f)   →   Σₙ βₙ Sₙ(f, g)  =  Σₙ β₄₋ₙ Sₙ(g, f)
```

The exchange acts on the coefficient list by reversing it. A polynomial whose coefficients read the same in both directions is called palindromic, or self-reciprocal: inverting its variable and multiplying by the top power returns the same polynomial [T]. Signal processing uses the same symmetry: a finite filter whose coefficients form a palindrome has linear phase, a frequency response that is real apart from a pure delay [T].

## How reciprocity acts: the frame exchange

[#8 §1](../../../notes/beta-coefficients.md#1-what-reciprocity-does-to-the-wedge-potential-d) states the step in one sentence: "Born reciprocity acts on the broken vacuum as the frame exchange (𝕏 → 𝕏⁻¹ in the aligned frame; the duality between the 'e-dynamical' and 'f-dynamical' presentations of the same physics). Invariance of the potential therefore forces the **palindromic constraint**".

The argument has two parts.

1. **Reciprocity is the frame exchange [D].** The broken vacuum is the state in which a polarization has been selected and reciprocity is no longer manifest ([the hard core](../../program/hard-core.md)). There, according to #8, reciprocity does not leave the two frames in place; it exchanges them. The note's support is the parenthesis: in the aligned frame the exchange is the inversion 𝕏 → 𝕏⁻¹, and it relates the presentation of the physics in which e is the dynamical frame to the one in which f is. The aligned point is 𝕏 = 1, where the two frames coincide ([#8 §2](../../../notes/beta-coefficients.md#2-the-vacuum-energy-theorem-d--rigorous-four-lines)). [#11 §7.3](../../papers/broken-born-checkpoint-v2.md#73-palindrome-and-the-vacuum-energy-identity-dv) restates the identification without further argument.
2. **Invariance forces the palindrome.** The invariance is that of postulate [P3](../../program/postulates/p3-reciprocity.md), "The action is invariant under the Born rotation generated by I = ω⁻¹H. [P]" ([#11 §4](../../papers/broken-born-checkpoint-v2.md#4-postulates)), so the potential must be unchanged by the exchange. By the display above, the exchange reverses the coefficient list, and matching the five terms gives βₙ = β₄₋ₙ; this step is the standard algebra of the previous section [T].

The physics is in part 1. How part 1 relates to the action of reciprocity on the [modular field Z](../../phase-space/modular-field/modular-field-z.md) is not written out. On Z reciprocity acts as "**ρ: Z → −Z⁻¹** (Möbius; d = 1 check), fixed point Z = i; at X = 0 it is scale-factor duality g → g⁻¹" ([#11 §6](../../papers/broken-born-checkpoint-v2.md#6-the-modular-field); [reciprocity as modular inversion](../../phase-space/modular-field/modular-inversion.md); [scale-factor duality](../../cosmology/scale-factor-duality/_index.md)). Neither #8 nor #11 derives the frame exchange from that inversion, so the identification in part 1 rests on the note's one-sentence argument.

The two actions also differ on the spin-2 fields. Linearized at Z = i, the inversion changes the sign of the metric's fluctuation together with that of X, while the frame exchange leaves the sum of the two frames unchanged. Flag 39 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md) records the difference, which decides the parity of the massless graviton; its audit found the parity the documents give right under the frame exchange that the palindrome uses, and rated the flag as depending on which action is meant ([two actions of reciprocity](../momentum-graviton/spectrum-and-parity.md#two-actions-of-reciprocity)).

## What follows

### The gravity sector is the interchange-symmetric branch

With the palindrome, the program's gravity sector is the interchange-symmetric branch of Hassan–Rosen bimetric gravity, with the second frame confined to the compact space Λ(4) of polarizations ([constrained bimetric gravity](../tuning-test/constrained-bimetric.md)). The [handoff](../../history/documents/handoff.md) puts it as "Geometric sector = interchange-symmetric (palindromic βₙ = β₄₋ₙ) Hassan–Rosen bimetric, second frame confined to compact Λ(4)" ([HANDOFF §2](../../../HANDOFF.md#2-scientific-state-one-screen)). #11's statement of [Born's answer](../momentum-graviton/borns-answer.md) gives X "its dynamics the reciprocity-symmetric branch of bimetric gravity with the second frame confined to compact Λ(4), its wedge vacuum energy zero by identity" ([#11 §7](../../papers/broken-born-checkpoint-v2.md#7-the-massive-momentum-graviton)).

### The vacuum-energy identity

At the aligned point the palindrome makes the value of the potential exactly twice its tadpole, V(1) = 2T, and a flat aligned vacuum then forces both to vanish. That result, [the vacuum-energy identity](vacuum-energy-identity.md), is the next page.

### Two parameters left

[#8 §3](../../../notes/beta-coefficients.md#3-spectrum-parameters-selection-structure-d--t) counts what remains: "five βₙ → palindrome (−2) → T = 0 (−1) → **two**: the Fierz–Pauli mass combination m_FP² ∝ β₁ + 2β₂ + β₃ = 2(β₁+β₂), i.e. **M_X**, and one orthogonal shape parameter controlling cubic interactions." The palindrome supplies the first step and the flat-vacuum condition T = 0 the second. [#11 §7.5](../../papers/broken-born-checkpoint-v2.md#75-spectrum-d) tags the count [D], and no script checks it ([spectrum, parameters and reciprocity parity](../momentum-graviton/spectrum-and-parity.md)).

### Parity and equal Planck masses

The same exchange sorts the two spin-2 fields. [#8 §3](../../../notes/beta-coefficients.md#3-spectrum-parameters-selection-structure-d--t): "the massless graviton is the reciprocity-**even** combination (e + f); X is reciprocity-**odd** (e − f). Reciprocity is a selection rule on vertices." (On the parities under [#11 §6](../../papers/broken-born-checkpoint-v2.md#6-the-modular-field)'s Z → −Z⁻¹, see flag 39, above.) For the exchange to be a symmetry of the whole action, the two metrics' kinetic terms must be exchanged as well, which requires equal [Planck masses](../spin-2-fields/planck-units.md#two-metrics-two-planck-masses) [T]; [#8 §3](../../../notes/beta-coefficients.md#3-spectrum-parameters-selection-structure-d--t) records "equal effective Planck masses (forced by the same symmetry)". The masslessness of the even combination is prediction [row 6](../../predictions/massless-graviton.md). Equal Planck masses also close one route to cosmological stability for a heavy spin-2 field. The worklog of manuscript [#14](../../../notes/knot-dark-matter-standalone.md), whose model, built with ordinary kinematics, failed on its recomputed abundance ([Obituary: #14's superheavy-soliton model](../../dark-matter/candidates/soliton-candidate/obituary.md)), notes that [#8 §3](../../../notes/beta-coefficients.md#3-spectrum-parameters-selection-structure-d--t)'s condition, M_f = M_g for the Planck masses of the two metrics, "rules out the M_f ≪ M_g escape", the regime in which the late-time stability result it cites holds, and records whether a large mass alone suffices at M_f = M_g as open ([`review/v3-worklog.md`](../../../review/v3-worklog.md), item R7; [Open: stability at equal Planck masses](../momentum-graviton/equal-planck-mass-stability.md)).

### The last link in a chain

[#9](../../history/documents/checkpoint.md), the first consolidated paper, illustrates its "forced convergence onto consistency islands" with a sequence of structural steps: the [multi-graviton no-go](../spin-2-fields/multi-graviton-no-go.md), then the [gravitational Higgs mechanism](../momentum-graviton/gravitational-higgs.md), then the Hassan–Rosen class, then the palindrome ([#9 §11](../../../notes/broken-born-program-v1.md#11-assessment)). #11 keeps "forced convergence onto consistency islands" among the program's progressive signs ([§15](../../papers/broken-born-checkpoint-v2.md#15-assessment); [the assessment](../../program/assessment.md); [Lakatosian methodology](../../method/lakatosian-methodology.md)).

## The literature position

The branch is not new, and #8's first presentation of it as an ad hoc simplification that the program gave a reason to exist is superseded ([below](#superseded-an-ad-hoc-branch-given-a-reason-to-exist)). The live literature search recorded in [#11 §7.4](../../papers/broken-born-checkpoint-v2.md#74-literature-position-updated-by-this-sessions-search--honesty-upgrade) (the [S] marks denote live-searched references) found:

> Exchange-symmetric bimetric potentials are *not* unexplored territory. (a) The interchange-symmetric parameter choice appears in the partially-massless (PM) bimetric literature: the PM point β₀ = 3α⁻²β₂, β₁ = β₃ = 0, β₄ = 3α²β₂ makes the potential g↔f symmetric, with proportional de Sitter solutions of undetermined ratio [24S]. At α = 1 the PM point lies **inside** our palindromic branch — so partially massless gravity, with its celebrated extra gauge symmetry, is a special point of the reciprocity-symmetric family, raising the open question of whether reciprocity is the origin of the PM symmetry [O]. ([#11 §7.4](../../papers/broken-born-checkpoint-v2.md#74-literature-position-updated-by-this-sessions-search--honesty-upgrade))

The partially massless point and its gauge symmetry are described on [partially massless gravity](../spin-2-fields/partially-massless-gravity.md), and its proportional de Sitter solutions on [de Sitter space](../../cosmology/dark-energy/de-sitter-space.md#proportional-de-sitter-backgrounds-in-bimetric-gravity). What remains the program's is the derivation: reciprocity, acting as the frame exchange, forces the branch [D]. Whether that also accounts for the extra gauge symmetry of the partially massless point is part of open problem 2, [the partially-massless comparison (OP2)](pm-comparison.md), which also asks whether the vacuum-energy identity is new.

## Superseded: an ad hoc branch given a reason to exist

The early documents presented the palindrome as the first motivation for a corner of bimetric gravity that had lacked one:

- [#8 §1](../../../notes/beta-coefficients.md#1-what-reciprocity-does-to-the-wedge-potential-d): the branch "has floated in the bimetric literature as an ad hoc simplification — it now has a reason to exist: **its ℤ₂ is Born reciprocity.**"
- The lab notebook's v0.6 addendum: "giving that previously ad hoc branch its reason to exist".
- #9, the v1.0 consolidation, [§5 item 5](../../../notes/broken-born-program-v1.md#5-the-second-graviton-and-its-mass-the-field-equation-problem-solved): "identifying the theory as the interchange-symmetric branch of bimetric gravity and supplying that branch's previously missing raison d'être."

[#11 §7.4](../../papers/broken-born-checkpoint-v2.md#74-literature-position-updated-by-this-sessions-search--honesty-upgrade) replaced this with the literature position above: the interchange-symmetric choice "appears in the partially-massless (PM) bimetric literature", and whether reciprocity is the origin of the PM symmetry is open [O]. The handoff records the same correction: the partially massless point "is g↔f symmetric and sits inside the palindromic branch" ([HANDOFF §2](../../../HANDOFF.md#2-scientific-state-one-screen)). The derivation of the palindrome from reciprocity was not affected. What #11 superseded is the description of the branch as an ad hoc simplification to which the program first gave a reason to exist; #11 does not repeat that claim and does not retract it in words.

## Tags and verification

- [#8 §1](../../../notes/beta-coefficients.md#1-what-reciprocity-does-to-the-wedge-potential-d) tags the derivation [D]. [#9 §5 item 5](../../../notes/broken-born-program-v1.md#5-the-second-graviton-and-its-mass-the-field-equation-problem-solved) tagged "The palindrome and the Λ theorem" together as "[D — rigorous]", and [#11 §7.3](../../papers/broken-born-checkpoint-v2.md#73-palindrome-and-the-vacuum-energy-identity-dv) tags "Palindrome and the vacuum-energy identity" together as [D][V].
- The [V] is battery test T5 ([the verification battery](../../method/verification/battery.md)). T5 builds the coefficients of V(1) and T with β₄ = β₀ and β₃ = β₁ already imposed ([`verify/battery.py`](../../../verify/battery.py)), so it checks what follows from the palindrome, not the palindrome. Like the parameter count of [#8 §3](../../../notes/beta-coefficients.md#3-spectrum-parameters-selection-structure-d--t), the derivation of the palindrome is [D] without a machine check.

## Sources

- [`wiki/papers/broken-born-checkpoint-v2.md` §7.3](../../papers/broken-born-checkpoint-v2.md#73-palindrome-and-the-vacuum-energy-identity-dv), [§7.4](../../papers/broken-born-checkpoint-v2.md#74-literature-position-updated-by-this-sessions-search--honesty-upgrade) — the constraint as currently stated; the literature position and the open question of the PM origin.
- [`wiki/papers/broken-born-checkpoint-v2.md` §1](../../papers/broken-born-checkpoint-v2.md#1-two-abstracts), [§7](../../papers/broken-born-checkpoint-v2.md#7-the-massive-momentum-graviton) 'Born's answer', [§7.2](../../papers/broken-born-checkpoint-v2.md#72-the-tuning-test-dv), [§7.5](../../papers/broken-born-checkpoint-v2.md#75-spectrum-d), [§15](../../papers/broken-born-checkpoint-v2.md#15-assessment) — the interchange-symmetric branch in the abstract and in Born's answer; the frame-tier class; the parameter count [D]; forced convergence among the progressive signs.
- [`wiki/papers/broken-born-checkpoint-v2.md` §4](../../papers/broken-born-checkpoint-v2.md#4-postulates), [§6](../../papers/broken-born-checkpoint-v2.md#6-the-modular-field) — postulate P3; reciprocity as Z → −Z⁻¹ and g → g⁻¹ at X = 0.
- [`notes/beta-coefficients.md` §1](../../../notes/beta-coefficients.md#1-what-reciprocity-does-to-the-wedge-potential-d), [§2](../../../notes/beta-coefficients.md#2-the-vacuum-energy-theorem-d--rigorous-four-lines), [§3](../../../notes/beta-coefficients.md#3-spectrum-parameters-selection-structure-d--t) — the potential, the exchange identity and the derivation [D]; the aligned point; the parameter count, the parities and the equal Planck masses.
- [`notes/tuning-test.md` §2](../../../notes/tuning-test.md#2-explicit-computation-metric-tier-d--rigorous), [§3](../../../notes/tuning-test.md#3-the-frame-tier-d--structural-resting-on-t) — linearity of the Hassan–Rosen family in the eₙ; what the tuning test's pass left to compute.
- [`HANDOFF.md` §2](../../../HANDOFF.md#2-scientific-state-one-screen) — the geometric sector as the palindromic branch; the partially massless point inside it.
- [`verify/battery.py`](../../../verify/battery.py) T5 — the test's input, with the palindrome already imposed.
- [`review/v3-worklog.md`](../../../review/v3-worklog.md) item R7 — equal Planck masses and the open stability question for a heavy spin-2 field.
- [`notes/broken-born-theory.md`](../../../notes/broken-born-theory.md) 'Addendum (v0.6)' — the result as first recorded, with the "previously ad hoc branch" wording that [#11 §7.4](../../papers/broken-born-checkpoint-v2.md#74-literature-position-updated-by-this-sessions-search--honesty-upgrade) replaced.
- [`notes/broken-born-program-v1.md` §5](../../../notes/broken-born-program-v1.md#5-the-second-graviton-and-its-mass-the-field-equation-problem-solved), [§11](../../../notes/broken-born-program-v1.md#11-assessment) — v1's "raison d'être" and its "[D — rigorous]" tag; the chain of forced convergence (superseded by #11).
- [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md) item 39 — the frame exchange against §6's Z → −Z⁻¹, and the parity of the massless graviton (pending).
