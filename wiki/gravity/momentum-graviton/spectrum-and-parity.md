---
title: "Spectrum, parameters and reciprocity parity"
weight: 80
status: alive
description: "Five βₙ reduce to two (the Fierz–Pauli mass and one cubic shape); the massless graviton is the reciprocity-even combination and X the odd one, with equal Planck masses forced and reciprocity a vertex selection rule."
provenance: [D]
sources:
  - "notes/beta-coefficients.md §3"
  - "notes/beta-coefficients.md §1"
  - "notes/beta-coefficients.md §2"
  - "wiki/papers/broken-born-checkpoint-v2.md §7.5"
  - "wiki/papers/broken-born-checkpoint-v2.md §7.3"
  - "wiki/papers/broken-born-checkpoint-v2.md §6"
  - "wiki/papers/broken-born-checkpoint-v2.md §7.4"
  - "wiki/papers/broken-born-checkpoint-v2.md §13"
  - "wiki/papers/broken-born-checkpoint-v2.md §15"
  - "verify/battery.py T5"
  - "verify/battery.py T6"
  - "notes/tuning-test.md §3"
  - "notes/tuning-test.md §4"
  - "notes/tuning-test.md §5"
  - "notes/x-classification.md §3"
  - "notes/broken-born-theory.md 'Addendum (v0.5)'"
  - "notes/broken-born-theory.md 'Addendum (v0.6)'"
  - "notes/broken-born-program-v1.md §5"
  - "notes/broken-born-program-v1.md §9"
  - "notes/broken-born-program-v1.md §11"
  - "review/v3-worklog.md 'Round-2 pending list'"
  - "popsci/universes-other-half.md 'The second geometry, and why it has never been seen'"
  - "review/wiki-build-flags.md items 5, 8, 39"
  - "review/wiki-build-checks/rho_parity.py"
  - "wiki/papers/phase-space-diameter.md §8.2"
  - "wiki/papers/phase-space-diameter.md §9"
  - "verify/phase_space_diameter.py 'Consequences (note §8)'"
---

*The potential that gives the [momentum graviton X](_index.md) its mass is a bimetric potential with five coefficients, and this page covers what is left of it once [reciprocity](../../phase-space/reciprocity/born-reciprocity.md) has acted, and how the program's two spin-2 fields sort under reciprocity. The [palindrome](../palindromic-branch/palindrome.md) removes two coefficients and the requirement of a flat vacuum removes a third, leaving two numbers: one sets X's mass M_X, the other shapes its cubic interactions. Reciprocity exchanges the two spin-2 frames of the theory, so the fields of definite mass are their sum, which the exchange leaves unchanged and which is the ordinary massless graviton, and their difference, which changes sign and is the massive X. The same symmetry forces the two frames to have [equal Planck masses](../spin-2-fields/planck-units.md#equal-planck-masses-in-the-bimetric-sector), a statement of calc note [#8 §3](../../../notes/beta-coefficients.md#3-spectrum-parameters-selection-structure-d--t) that [#11](../../papers/broken-born-checkpoint-v2.md) does not repeat. The count and the parities are derivations [D] in [checkpoint #11](../../history/documents/checkpoint.md) [§7.5](../../papers/broken-born-checkpoint-v2.md#75-spectrum-d), not machine-checked, and the masslessness of the even combination is prediction [row 6](../../predictions/massless-graviton.md).*

**Status:** Alive — [D] in [#11 §7.5](../../papers/broken-born-checkpoint-v2.md#75-spectrum-d); [D + T] in [calc note #8](../../history/documents/field-equation-notes.md) ([`notes/beta-coefficients.md` §3](../../../notes/beta-coefficients.md#3-spectrum-parameters-selection-structure-d--t)) — derivations only: no battery test covers the parameter count, the m_FP² combination or the parities. The machine-checked inputs are [the identity V(1) = 2T](../palindromic-branch/vacuum-energy-identity.md) used in the second reduction step and the coefficients that define T (battery tests T5 and T6, [the verification battery](../../method/verification/battery.md)). Tested observationally by [Row 6: the exactly massless graviton](../../predictions/massless-graviton.md).

## The potential and its five coefficients

After [the tuning test](../tuning-test/_index.md), the program's spin-2 sector is a [Hassan–Rosen bimetric](../spin-2-fields/hassan-rosen-bimetric.md) potential written in frame variables. Its two frames are e and f = E₀[J], the second built from the vacuum's [polarization J](../../symmetry-breaking/order-parameter.md) ([the frame tier](../tuning-test/frame-tier.md)); g and f in the formula below are the corresponding metrics. Calc note [#8 §1](../../../notes/beta-coefficients.md#1-what-reciprocity-does-to-the-wedge-potential-d) writes it as

```text
V = 2m²M² Σₙ₌₀⁴ βₙ eₙ(𝕏),        𝕏 = √(g⁻¹f)
exchange identity:  Sₙ(g, f) = S₄₋ₙ(f, g)
```

The eₙ are the [elementary symmetric polynomials](../spin-2-fields/elementary-symmetric-polynomials.md) of the four eigenvalues of 𝕏: e₀ = 1, e₁ is their sum, e₂ the sum of their pairwise products, e₃ the sum of triple products and e₄ their product [T]. The note does not define m, M or Sₙ. The point where the two frames coincide, 𝕏 = 1, is the aligned point; there eₙ(1) = C(4, n), the binomial coefficients ([#8 §2](../../../notes/beta-coefficients.md#2-the-vacuum-energy-theorem-d--rigorous-four-lines)).

In general bimetric gravity the five coefficients β₀ to β₄ are free [T]. In the program's account they are what remained undetermined after the tuning test: "What a pass does **not** yet deliver: the βₙ coefficients" (calc note [#7 §3](../../../notes/tuning-test.md#3-the-frame-tier-d--structural-resting-on-t)).

## From five coefficients to two

Calc note [#8 §3](../../../notes/beta-coefficients.md#3-spectrum-parameters-selection-structure-d--t) [D + T] states the count in one line:

```text
five βₙ  →  palindrome (−2)  →  T = 0 (−1)  →  two
```

### Step 1: the palindrome removes two

Reciprocity acts on the broken vacuum as the exchange of the two frames, "𝕏 → 𝕏⁻¹ in the aligned frame" ([#8 §1](../../../notes/beta-coefficients.md#1-what-reciprocity-does-to-the-wedge-potential-d)). By the exchange identity, swapping the frames reverses the order of the potential's terms, so a potential that reciprocity leaves invariant must read the same in both directions: βₙ = β₄₋ₙ, that is β₀ = β₄ and β₁ = β₃, with β₂ free ([#8 §1](../../../notes/beta-coefficients.md#1-what-reciprocity-does-to-the-wedge-potential-d); [#11 §7.3](../../papers/broken-born-checkpoint-v2.md#73-palindrome-and-the-vacuum-energy-identity-dv)). Two conditions remove two coefficients. The derivation is on [the palindrome βₙ = β₄₋ₙ](../palindromic-branch/palindrome.md) [D].

### Step 2: a flat aligned vacuum removes one

Moving slightly away from the aligned point, 𝕏 = 1 + δ, changes the potential at first order by an amount proportional to Tr δ. Its coefficient is the tadpole T: "linearizing eₙ(1+δ) = C(4,n) + C(3,n−1)Tr δ gives the tadpole combination T = β₁ + 3β₂ + 3β₃ + β₄" ([#8 §2](../../../notes/beta-coefficients.md#2-the-vacuum-energy-theorem-d--rigorous-four-lines)). Under the palindrome the value of the potential at the aligned point and the tadpole satisfy an identity:

```text
V(1) ∝ 2β₀ + 8β₁ + 6β₂,     T = β₀ + 4β₁ + 3β₂     ⟹     V(1) = 2T
flat aligned vacuum:  V(1) = T     ⟹     T = 0  and  V(1) = 0
```

A flat aligned vacuum requires "the g-equation's potential contribution to vanish: V(1) = T" ([#8 §2](../../../notes/beta-coefficients.md#2-the-vacuum-energy-theorem-d--rigorous-four-lines)), and with the identity this forces T = 0. One condition removes one coefficient: it fixes β₀ = −4β₁ − 3β₂, which [#11 §7.4](../../papers/broken-born-checkpoint-v2.md#74-literature-position-updated-by-this-sessions-search--honesty-upgrade) notes is "a *different* point of the same branch" from the [partially massless](../spin-2-fields/partially-massless-gravity.md) one. The identity, its scope and its novelty status are on [the vacuum-energy identity V(1) = 2T](../palindromic-branch/vacuum-energy-identity.md).

### What remains

After both steps β₁ and β₂ are free, and the other three follow: β₃ = β₁ and β₀ = β₄ = −4β₁ − 3β₂ ([#8 §1](../../../notes/beta-coefficients.md#1-what-reciprocity-does-to-the-wedge-potential-d); [#11 §7.4](../../papers/broken-born-checkpoint-v2.md#74-literature-position-updated-by-this-sessions-search--honesty-upgrade)). Calc note [#8 §3](../../../notes/beta-coefficients.md#3-spectrum-parameters-selection-structure-d--t) names the two surviving numbers:

> "the Fierz–Pauli mass combination m_FP² ∝ β₁ + 2β₂ + β₃ = 2(β₁+β₂), i.e. **M_X**, and one orthogonal shape parameter controlling cubic interactions."

The [Fierz–Pauli](../spin-2-fields/fierz-pauli.md) mass term is the only [ghost-free](../spin-2-fields/ghosts.md) quadratic mass term of a spin-2 field. Expanded to second order about the aligned point, a bimetric potential produces it with a coefficient proportional to β₁ + 2β₂ + β₃ [T]. With the palindrome's β₃ = β₁ this combination is 2(β₁ + β₂). Neither β₀ nor β₄ enters it, so the vacuum condition of step 2 fixes them without fixing the mass. #8 says nothing further about the second parameter beyond its role in the cubic interactions.

[#11 §7.5](../../papers/broken-born-checkpoint-v2.md#75-spectrum-d) [D] restates the count as "Five βₙ → two parameters (M_X ∝ 2(β₁+β₂); one cubic shape)." #8 states the proportionality for the squared mass m_FP², and #11 writes it for M_X. Flag 5 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md), raised independently by three agents, notes that the β-combination fixes the squared Fierz–Pauli mass [T] and suspects that [#11 §7.5](../../papers/broken-born-checkpoint-v2.md#75-spectrum-d) and [#9 §5 item 6](../../../notes/broken-born-program-v1.md#5-the-second-graviton-and-its-mass-the-field-equation-problem-solved) mean M_X². It is a question of notation only, and the flag is pending; this page quotes both documents as written.

### No value for M_X

No document fixes a value for M_X. Calc note [#6 §3](../../../notes/x-classification.md#3-the-mass-mechanism-and-the-endpoint-d--structural) identifies it as "the polarization-breaking scale", and [#8 §3](../../../notes/beta-coefficients.md#3-spectrum-parameters-selection-structure-d--t) argues safety "down to far below any plausible M_X" without saying what is plausible ([safety by range](fifth-force-safety.md)).

The one number in the record is a lower bound, and it is conditional. The [phase-space-diameter note](../../cosmology/scale-factor-duality/phase-space-diameter.md), which also says M_X has "no value in the record" ([§8.2](../../papers/phase-space-diameter.md#82-not-the-range-of-the-momentum-graviton-and-a-bound-on-it-dvs)), takes the program's aligned vacuum, in which the ratio of the two frames' backgrounds is u = 1. There, with the equal Planck masses below, X's force on ordinary matter has Yukawa strength α = 4/3 relative to gravity, and torsion balances require λ_X < 37.7 μm, M_X c² > 5.2 meV, with λ_X = ħ/(M_X c) the range of the force ([§8.2](../../papers/phase-space-diameter.md#82-not-the-range-of-the-momentum-graviton-and-a-bound-on-it-dvs); tagged [V][S] in the note's summary, [§9](../../papers/phase-space-diameter.md#9-summary); recomputed by [`verify/phase_space_diameter.py`](../../../verify/phase_space_diameter.py), [the phase-space-diameter script](../../method/verification/phase-space-diameter-script.md)). Whether the aligned vacuum persists as the universe expands is open [O]. The bound, its premise and its dependence on u are on [the laboratory bound on X's range](range-bound.md).

The popular article [#12](../../../popsci/universes-other-half.md) says the second field "acquired a large mass"; #12 presents the framework as if confirmed and is not a source for status ([the popular articles](../../history/documents/popular-articles.md)).

### What is checked

Two machine checks enter the reduction. Battery test T5 confirms V(1) − 2T = [0, 0, 0] in exact integers, printing `T5 V(1) - 2T = [0,0,0]  [V1=[2, 8, 6] T=[1, 4, 3]]`, and T6 confirms the linearization coefficients C(3, n−1) that define T. The palindrome derivation, the count of two, the m_FP² combination and the parity assignments below have no test; the wiki tags them [D], as [#11 §7.5](../../papers/broken-born-checkpoint-v2.md#75-spectrum-d) does.

## The two spin-2 fields and their parity

### Even and odd combinations

A bimetric theory has two spin-2 fields, and about a common background one combination of them is massless and the other massive. Calc note [#7 §4](../../../notes/tuning-test.md#4-the-picture-that-emerges-constrained-bimetric-gravity-d--structural) records this for the program: "Standard bimetric facts then slot in [T]: one massless combination (our graviton, coupling to SM stress) and one massive (X)", where SM is the Standard Model. Calc note [#8 §3](../../../notes/beta-coefficients.md#3-spectrum-parameters-selection-structure-d--t) [D + T] says which combination is which:

> "the massless graviton is the reciprocity-**even** combination (e + f); X is reciprocity-**odd** (e − f)."

That the fields of definite mass are a sum and a difference is a general property of an exchange symmetry [T]. If an exchange of two fields leaves the quadratic part of the action unchanged, the action's mass matrix commutes with the exchange, and its eigenstates can be taken to be the sum, which the exchange leaves unchanged, and the difference, which changes sign. #8 does not spell this step out; which of the two is the massless one is its assignment:

```text
reciprocity:   e ↔ f
e + f   →   e + f          even    the massless graviton
e − f   →   −(e − f)       odd     X, mass M_X
```

[#11 §7.5](../../papers/broken-born-checkpoint-v2.md#75-spectrum-d) [D] carries the result as "Massless graviton = reciprocity-even" and "X = reciprocity-odd".

### Two actions of reciprocity

The assignment uses reciprocity in the form the documents give for the spin-2 sector, the exchange of the two frames, e ↔ f ([#8 §1](../../../notes/beta-coefficients.md#1-what-reciprocity-does-to-the-wedge-potential-d); [#11 §7.3](../../papers/broken-born-checkpoint-v2.md#73-palindrome-and-the-vacuum-energy-identity-dv)), which [the palindrome](../palindromic-branch/palindrome.md#how-reciprocity-acts-the-frame-exchange) also needs. [#11 §6](../../papers/broken-born-checkpoint-v2.md#6-the-modular-field) gives a second action, on the modular field: ρ: Z → −Z⁻¹, with fixed point Z = i ([reciprocity as modular inversion](../../phase-space/modular-field/modular-inversion.md)). Flag 39 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md) notes that the two give the massless graviton opposite parities. Linearized at Z = i, the inversion sends a small fluctuation x + ih, with x the fluctuation of X and h that of the metric, to −(x + ih) for every d, so h changes sign together with X (the flag's check prints this for d = 1, 2 and 3, [`review/wiki-build-checks/rho_parity.py`](../../../review/wiki-build-checks/rho_parity.py)). The documents state both actions and do not show how one becomes the other for the massless mode. The flag's audit (2026-10-22) found the parities right under the frame exchange and wrong under §6's map if the graviton is read as the fluctuation of Im Z; X is odd under either. It rated the flag as depending on which action is meant, and the flag is pending.

### Equal Planck masses

In bimetric gravity each metric has its own [Einstein–Hilbert term](../spin-2-fields/general-relativity.md), and the coefficient of that term, the metric's Planck mass, sets how strongly the metric responds to sources [T]; the v3 worklog ([`review/v3-worklog.md`](../../../review/v3-worklog.md), item R7) writes the two as M_g and M_f. An exchange of the two metrics is a symmetry of the whole action only if it maps the two kinetic terms onto each other, which requires the two Planck masses to be equal [T]. Calc note [#8 §3](../../../notes/beta-coefficients.md#3-spectrum-parameters-selection-structure-d--t) states the result for the program's frames as "With equal effective Planck masses (forced by the same symmetry)", with no separate derivation.

Two consequences are worked out elsewhere. Matter coupled to g "sees both eigenstates with comparable strength" ([#8 §3](../../../notes/beta-coefficients.md#3-spectrum-parameters-selection-structure-d--t)), so ordinary matter feels X at gravitational strength, and its safety rests on X's short range ([safety by range](fifth-force-safety.md)). Equal Planck masses fix that strength only together with the ratio u of the two frames' backgrounds: "Only the product M_f u is fixed by the theory, so equal Planck masses give α = 4/3 only if u = 1", the program's aligned vacuum ([phase-space-diameter note §8.2](../../papers/phase-space-diameter.md#82-not-the-range-of-the-momentum-graviton-and-a-bound-on-it-dvs); [the laboratory bound on X's range](range-bound.md)). And equal Planck masses rule out the regime in which a heavy spin-2 field has been shown to be linearly stable at late times in an expanding universe ([Open: stability at equal Planck masses](equal-planck-mass-stability.md)).

### A selection rule on vertices

[#8 §3](../../../notes/beta-coefficients.md#3-spectrum-parameters-selection-structure-d--t) adds: "Reciprocity is a selection rule on vertices." A selection rule is a restriction, following from a symmetry, on which interaction vertices can occur. With a two-valued parity, a vertex is allowed only if the parities of the fields meeting at it multiply to +1 [T]. #8 does not list the vertices the rule allows or forbids, and no other document works them out.

## What follows

- **Row 6.** Bounds on the graviton mass from gravitational-wave observations constrain the massless eigenstate. In [#8 §3](../../../notes/beta-coefficients.md#3-spectrum-parameters-selection-structure-d--t)'s words, these bounds "apply to the even eigenstate, which is exactly massless", and [#11 §7.5](../../papers/broken-born-checkpoint-v2.md#75-spectrum-d) calls them satisfied identically. [#11 §13 row 6](../../papers/broken-born-checkpoint-v2.md#13-predictions-and-kill-conditions): standard expectation "m_g = 0"; program requirement "Massless eigenstate exactly massless (reciprocity-even)"; killed by "Nonzero mass attributed to the even eigenstate" ([Row 6: the exactly massless graviton](../../predictions/massless-graviton.md)).
- **The predictive truncation, counted.** Calc note [#7 §4](../../../notes/tuning-test.md#4-the-picture-that-emerges-constrained-bimetric-gravity-d--structural) had called the program's gravity sector "a *predictive truncation* of bimetric theory" ([constrained bimetric gravity](../tuning-test/constrained-bimetric.md)). [#8 §3](../../../notes/beta-coefficients.md#3-spectrum-parameters-selection-structure-d--t) quantifies it: the "five-function freedom" of Hassan–Rosen bimetric gravity, its five constant coefficients, "collapses to two numbers". Flag 8 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md) notes that the βₙ are constants ([#7 §2](../../../notes/tuning-test.md#2-explicit-computation-metric-tier-d--rigorous)), so the freedom is five parameters rather than five functions.
- **Born's answer.** The "two free parameters" in the program's summary of its gravity results are these two ([Born's answer: momentum space gravitates](borns-answer.md)).

## Superseded: the graviton-mass bound as a mixing-angle check

Before the coefficients were known, calc note [#7 §4](../../../notes/tuning-test.md#4-the-picture-that-emerges-constrained-bimetric-gravity-d--structural) treated the graviton-mass bound as a check on how the two spin-2 fields mix. It required "the massless combination to dominate SM couplings — a parametric check to log, alongside graviton-mass bounds" from gravitational-wave observations, quoted as "m_g ≲ 10⁻²³ eV territory", "for the mixing angle". The note's list of remaining items included "(iv) SM-coupling/graviton-mass parametrics" ([§5](../../../notes/tuning-test.md#5-status-of-the-field-equation-problem)), and [the lab notebook](../../history/documents/lab-notebook.md)'s v0.5 addendum logged graviton-mass and mixing parametrics against the gravitational-wave bounds as one of three checks.

Calc note [#8 §3](../../../notes/beta-coefficients.md#3-spectrum-parameters-selection-structure-d--t) replaced that reading. With the eigenstates fixed by parity, the bounds "apply to the even eigenstate, which is exactly massless", and [#11 §7.5](../../papers/broken-born-checkpoint-v2.md#75-spectrum-d) states them as satisfied identically. #8 and #11 row 6 are the current form ([conflicts between sources](../../history/documents/source-conflicts.md)). The other half of #7's check, the requirement that the massless combination dominate the couplings of ordinary matter, was also replaced in #8, by safety through range ([safety by range](fifth-force-safety.md)).

## History

- **Calc note [#7 §3](../../../notes/tuning-test.md#3-the-frame-tier-d--structural-resting-on-t)** expected the coefficients to settle three things: "they determine M_X, the X–h mixing, and a vacuum-energy contribution". Calc note #8 answered with the mass combination, the parity eigenstates and a vanishing vacuum energy of the wedge sector.
- **The lab notebook's v0.6 addendum** summarized: "Parameter count: five → two (M_X and one cubic-shape parameter). Spectrum: massless graviton = reciprocity-even, X = reciprocity-odd" ([the lab notebook](../../history/documents/lab-notebook.md)).
- **The v1 paper (#9)** [§5 item 6](../../../notes/broken-born-program-v1.md#5-the-second-graviton-and-its-mass-the-field-equation-problem-solved) has nearly the same wording as [#11 §7.5](../../papers/broken-born-checkpoint-v2.md#75-spectrum-d). Its row 6 ([§9](../../papers/broken-born-checkpoint-v2.md#9-momentum-clumping-the-founding-image-tested)) also required "massive X short-range", and its assessment ([§11](../../papers/broken-born-checkpoint-v2.md#11-polarized-charge-lattices-monopoles-duality-frames-and-the-recurring-matrix)) counted "even-eigenstate masslessness as a bimetric-parity statement" among "novel predictions not previously posed". [#11 §15](../../papers/broken-born-checkpoint-v2.md#15-assessment) names only rows 3 and 11 as predictions not previously posed ([history of the predictions table](../../predictions/table-history.md)).
- **[#11 §7.5](../../papers/broken-born-checkpoint-v2.md#75-spectrum-d)** is the current statement [D].

## Sources

- [`notes/beta-coefficients.md` §3](../../../notes/beta-coefficients.md#3-spectrum-parameters-selection-structure-d--t) — the count, the parities, the equal Planck masses and the selection rule [D + T]; [§1](../../../notes/beta-coefficients.md#1-what-reciprocity-does-to-the-wedge-potential-d) — the potential, the frames e and f and the palindrome; [§2](../../../notes/beta-coefficients.md#2-the-vacuum-energy-theorem-d--rigorous-four-lines) — the tadpole and the identity V(1) = 2T
- [`wiki/papers/broken-born-checkpoint-v2.md` §7.5](../../papers/broken-born-checkpoint-v2.md#75-spectrum-d) — the current statement [D]; [§7.3](../../papers/broken-born-checkpoint-v2.md#73-palindrome-and-the-vacuum-energy-identity-dv) — the palindrome and the identity; [§6](../../papers/broken-born-checkpoint-v2.md#6-the-modular-field) — reciprocity as Z → −Z⁻¹; [§7.4](../../papers/broken-born-checkpoint-v2.md#74-literature-position-updated-by-this-sessions-search--honesty-upgrade) — the point β₀ = −4β₁ − 3β₂; [§13](../../papers/broken-born-checkpoint-v2.md#13-predictions-and-kill-conditions) — row 6; [§15](../../papers/broken-born-checkpoint-v2.md#15-assessment) — the predictions counted as not previously posed
- [`verify/battery.py`](../../../verify/battery.py) T5 — the identity V(1) = 2T in exact integers; T6 — the linearization coefficients C(3, n−1)
- [`notes/tuning-test.md` §3](../../../notes/tuning-test.md#3-the-frame-tier-d--structural-resting-on-t) — the coefficients left open by the tuning test; [§4](../../../notes/tuning-test.md#4-the-picture-that-emerges-constrained-bimetric-gravity-d--structural) — the standard bimetric facts and the mixing-angle reading; [§5](../../../notes/tuning-test.md#5-status-of-the-field-equation-problem) — the graviton-mass parametrics as a remaining check
- [`notes/x-classification.md` §3](../../../notes/x-classification.md#3-the-mass-mechanism-and-the-endpoint-d--structural) — M_X as the polarization-breaking scale
- [`notes/broken-born-theory.md`](../../../notes/broken-born-theory.md) 'Addendum (v0.5)' — the logged checks; 'Addendum (v0.6)' — the lab notebook's summary of the spectrum
- [`notes/broken-born-program-v1.md` §5](../../../notes/broken-born-program-v1.md#5-the-second-graviton-and-its-mass-the-field-equation-problem-solved), [§9](../../../notes/broken-born-program-v1.md#9-predictions-and-kill-conditions), [§11](../../../notes/broken-born-program-v1.md#11-assessment) — the superseded v1 statement, its row 6 and its assessment
- [`review/v3-worklog.md`](../../../review/v3-worklog.md) 'Round-2 pending list' — item R7: the Planck masses written M_g and M_f, and the stable heavy-spin-2 regime at M_f ≪ M_g
- [`popsci/universes-other-half.md`](../../../popsci/universes-other-half.md) 'The second geometry, and why it has never been seen' — "acquired a large mass" (popular article; not a status source)
- [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md) item 5 — M_X versus M_X² in [#11 §7.5](../../papers/broken-born-checkpoint-v2.md#75-spectrum-d) and [#9 §5](../../../notes/broken-born-program-v1.md#5-the-second-graviton-and-its-mass-the-field-equation-problem-solved); item 8 — "five-function" for five constant coefficients; item 39 — the two actions of reciprocity on the spin-2 sector and the parities they give, with its audit verdict; all pending
- [`review/wiki-build-checks/rho_parity.py`](../../../review/wiki-build-checks/rho_parity.py) — the linearization of Z → −Z⁻¹ at Z = i, for flag 39
- [`wiki/papers/phase-space-diameter.md` §8.2](../../papers/phase-space-diameter.md#82-not-the-range-of-the-momentum-graviton-and-a-bound-on-it-dvs) — M_X with "no value in the record"; the background ratio u in X's strength; the conditional bound λ_X < 37.7 μm, M_X c² > 5.2 meV [D][V][S]; [§9](../../papers/phase-space-diameter.md#9-summary) — the bound tagged [V][S]
- [`verify/phase_space_diameter.py`](../../../verify/phase_space_diameter.py) 'Consequences (note §8)' — the bound recomputed [V]
