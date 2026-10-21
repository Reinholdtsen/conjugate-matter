---
title: "The vacuum-energy identity V(1) = 2T"
weight: 20
status: alive
description: "At the aligned point the integer identity [2,8,6] = 2·[1,4,3] gives V(1) = 2T, so a flat aligned vacuum forces T = 0 and V(1) = 0 (battery T5); it does not address matter-loop vacuum energy."
provenance: [D, V]
sources:
  - "papers/broken-born-checkpoint-v2.md §7.3"
  - "papers/broken-born-checkpoint-v2.md §7.4"
  - "papers/broken-born-checkpoint-v2.md §1"
  - "papers/broken-born-checkpoint-v2.md §2"
  - "papers/broken-born-checkpoint-v2.md §15"
  - "papers/broken-born-checkpoint-v2.md ref [22]"
  - "verify/battery.py T5"
  - "verify/battery.py T6"
  - "notes/debt1a-iv-beta-coefficients.md §2"
  - "notes/debt1a-iv-beta-coefficients.md §1"
  - "notes/debt1a-iv-beta-coefficients.md §3"
  - "notes/debt1a-iv-beta-coefficients.md §4"
  - "HANDOFF.md §2"
  - "HANDOFF.md §3"
  - "HANDOFF.md §5"
  - "notes/broken-born-theory.md 'Addendum (v0.6)'"
  - "notes/broken-born-theory.md §7"
  - "notes/broken-born-program-v1.md §0"
  - "notes/broken-born-program-v1.md §5"
  - "notes/broken-born-program-v1.md §8"
  - "notes/broken-born-program-v1.md §11"
  - "popsci/angle-of-the-mirror.md 'What refused to die'"
  - "popsci/universes-other-half.md 'The second geometry, and why it has never been seen'"
---

*The vacuum-energy identity is a short algebraic result about the program's [spin-2 interaction potential](/wiki/gravity/spin-2-fields/hassan-rosen-bimetric) once its coefficients obey [the palindrome](/wiki/gravity/palindromic-branch/palindrome) βₙ = β₄₋ₙ. At the aligned point, where the potential's two frames coincide, the value of the potential, V(1), is exactly twice its tadpole T, the coefficient of the term linear in a small departure from that point. A flat aligned vacuum separately requires V(1) = T, and the two equations together force T = 0 and V(1) = 0: the spin-2 interaction sector adds no vacuum energy there, by symmetry, with the one flatness condition doing the work of the two tunings that generic bimetric gravity needs. The integer arithmetic is machine-checked. The identity says nothing about the vacuum energy of matter loops, the "old" [cosmological-constant problem](/wiki/gravity/spin-2-fields/cosmological-constant-problem), and whether it is new is the subject of an open [literature comparison](/wiki/gravity/palindromic-branch/pm-comparison).*

**Status:** Alive — [D][V] (#11 §7.3); calc note #8 §2 tags the derivation "[D — rigorous, four lines]" — battery test T5 checks the integer identity in exact integers and T6 the linearization coefficients it uses, and both pass ([the verification battery](/wiki/method/verification/battery)). The palindrome it starts from and the flatness condition are derived, not machine-checked. The novelty claim was downgraded in #11 §7.4 and waits on [the partially-massless comparison (OP2)](/wiki/gravity/palindromic-branch/pm-comparison); the scope is the wedge sector at the aligned point (#11 §7.3).

## Statement

[Checkpoint #11](/wiki/history/documents/checkpoint) §7.3, after the palindrome: "Then V(1) = 2T exactly (integer identity: [2,8,6] = 2·[1,4,3]), so a flat aligned vacuum (V(1) = T) forces **T = 0 and V(1) = 0**: *the wedge sector contributes zero cosmological constant, by symmetry.*"

[Calc note #8](/wiki/history/documents/debt-1-notes) §2, where the result was first derived, states it as "**In the reciprocity-symmetric theory, the existence of a flat aligned vacuum forces the wedge sector's vacuum energy to be exactly zero** — one condition does the work that takes two tunings in generic bimetric gravity."

The "wedge sector" is the frame-tier potential of [the tuning test](/wiki/gravity/tuning-test): the [Hassan–Rosen](/wiki/gravity/spin-2-fields/hassan-rosen-bimetric) potential of two frames that gives the [momentum graviton X](/wiki/gravity/momentum-graviton) its mass ([the frame tier](/wiki/gravity/tuning-test/frame-tier)). #11 uses the symbol T without defining it; the definition is #8's.

## The ingredients

### The potential and the aligned point

#8 §1 writes the potential as V = 2m²M² Σₙ₌₀⁴ βₙ eₙ(𝕏), with 𝕏 = √(g⁻¹f) built from the metrics of the two frames and eₙ the [elementary symmetric polynomials](/wiki/gravity/spin-2-fields/elementary-symmetric-polynomials) of its eigenvalues; the palindrome page explains each piece. "At the aligned point 𝕏 = 1" (#8 §2) the two frames coincide, g⁻¹f is the unit matrix, and a small departure from that point is written 𝕏 = 1 + δ, with δ a small matrix. V(1) is the potential at 𝕏 = 1. #8 gives it only up to proportionality (the display under [the four lines](#the-four-lines)); the overall factor 2m²M² plays no role in what follows.

### The polynomials at and near the unit matrix [T]

At the unit matrix all four eigenvalues equal 1, so every product in eₙ equals 1 and eₙ counts the ways of choosing n eigenvalues out of four: the binomial coefficient C(4, n). Moving slightly away, each eigenvalue becomes 1 + δᵢ. To first order a product of n such eigenvalues picks up one δᵢ with the other factors equal to 1, and a given δᵢ appears in as many products as there are ways of choosing the other n − 1 eigenvalues from the remaining three, C(3, n − 1). Summing over i turns the δᵢ into the trace. #8 §2 states the result:

```text
eₙ(1) = C(4, n),        eₙ(1 + δ) = C(4, n) + C(3, n−1) Tr δ
```

Battery test T6 checks the linear coefficients numerically ([verification](#verification)).

### The value V(1) and the tadpole T

Substituting into the potential gives its value at the aligned point, V(1) ∝ Σₙ βₙ C(4, n), and the coefficient of its linear term, Σₙ βₙ C(3, n − 1). #8 §2: "linearizing eₙ(1+δ) = C(4,n) + C(3,n−1)Tr δ gives the tadpole combination T = β₁ + 3β₂ + 3β₃ + β₄." β₀ does not appear, because e₀ = 1 is constant.

In field theory a term linear in the fluctuations about a background is called a tadpole, after the shape of its Feynman diagram, and a background solves the field equations exactly when the action has no net term linear in those fluctuations [T]. The lab notebook glosses the identity as "vacuum energy = twice the tadpole" (#1, v0.6 addendum; [the lab notebook](/wiki/history/documents/lab-notebook)).

## The four lines

### V(1) = 2T under the palindrome

With β₄ = β₀ and β₃ = β₁, the outer terms of each sum merge. #8 §2:

```text
V(1) ∝ 2β₀ + 8β₁ + 6β₂,        T = β₀ + 4β₁ + 3β₂        ⟹        V(1) = 2T
```

Every coefficient of V(1) is twice the matching coefficient of T, which is what #11 §7.3 calls the "integer identity: [2,8,6] = 2·[1,4,3]". Battery test T5 builds the two coefficient vectors over (β₀, β₁, β₂) from binomial coefficients in exactly this way: the coefficient of β₀ in V(1) as C(4,0) + C(4,4), of β₁ as C(4,1) + C(4,3), of β₂ as C(4,2), and for T as C(3,3), C(3,0) + C(3,2) and C(3,1) (`verify/battery.py`).

### The flatness condition V(1) = T

#8 §2: "Flat aligned vacuum requires the g-equation's potential contribution to vanish: V(1) = T." The g-equation is the field equation of the metric g, obtained by varying the action with respect to g. At the aligned point the potential enters it as a term proportional to the metric, which acts as a cosmological constant, and a flat metric needs that term to vanish [T]. Varying the potential term with respect to g produces two contributions: one from the volume factor of g, proportional to the value V(1), and one from 𝕏 = √(g⁻¹f), which depends on g, proportional to the linear coefficient T. The condition V(1) = T says that the two cancel [T]. #8 states the condition without writing out the field equation, and #11 §7.3 repeats it as "a flat aligned vacuum (V(1) = T)".

### Both vanish

The flatness condition says V(1) = T and the identity says V(1) = 2T, so T = 0 and then V(1) = 0. #8 §2 boxes the conclusion:

```text
T = 0  and  V(1) = 0  exactly
```

Written out under the palindrome, T = 0 is the condition β₀ = −4β₁ − 3β₂. #11 §7.4 records that "our flat-aligned-vacuum identity selects a *different* point of the same branch (β₁ ≠ 0 generically, β₀ = −4β₁ − 3β₂)" from the partially massless point of the bimetric literature ([partially massless gravity](/wiki/gravity/spin-2-fields/partially-massless-gravity)).

## What it means

### One condition instead of two

In generic bimetric gravity the potential contributes a vacuum-energy term to each of the two metrics' field equations, so a vacuum in which the aligned metrics are flat needs both terms set to zero [T]. #8 §2: "one condition does the work that takes two tunings in generic bimetric gravity." The lab notebook's v0.6 addendum puts it as "the massive-gravity sector contributes zero cosmological constant, by symmetry rather than tuning".

### Dark energy is left to τ

#8 §2: "The massive-gravity sector contributes *nothing* to the cosmological constant; dark energy is left entirely to the τ sector, which is precisely the architecture the cosmology chapter had assumed. What was an assumption is now a theorem of the symmetry." In the lab notebook's cosmology, dark energy is the [Maslov modulus τ](/wiki/phase-space/modular-field/maslov-phase), an angle on the space of polarizations, sitting near the top of a cosine potential (#1 §7; [τ as hilltop quintessence](/wiki/cosmology/dark-energy/tau-quintessence); [dark energy](/wiki/cosmology/dark-energy)). [#9](/wiki/history/documents/checkpoint), the v1.0 consolidation, drew the same consequence for its own cosmology section: "§5's Λ theorem guarantees the massive-gravity sector contributes nothing to compete with τ" (#9 §8).

### One parameter fewer

T = 0 removes one more of the five βₙ: "five βₙ → palindrome (−2) → T = 0 (−1) → **two**" (#8 §3). The two that remain are the combination that sets X's mass and one shape parameter of its cubic interactions ([spectrum, parameters and reciprocity parity](/wiki/gravity/momentum-graviton/spectrum-and-parity)).

## Scope

#11 §7.3: "Scope, stated carefully: this cancels the spin-2 interaction potential's vacuum contribution at the aligned point — it does **not** by itself address matter-loop vacuum energy, the "old" cosmological-constant problem, on which bimetric theory is otherwise no better placed than GR [22S]." GR is [general relativity](/wiki/gravity/spin-2-fields/general-relativity). Matter-loop vacuum energy is the zero-point energy of quantum matter fields, which gravitates like a cosmological constant and is estimated far above the observed value [T]; that problem is on [the cosmological-constant problem](/wiki/gravity/spin-2-fields/cosmological-constant-problem). Reference [22][S] is A. Schmidt-May, M. von Strauss, "Recent developments in bimetric theory," J. Phys. A 49, 183001 (2016), arXiv:1512.00021.

The statement carries three limits:

- **The aligned point only.** It concerns 𝕏 = 1, where the two frames coincide (#11 §7.3, "at the aligned point").
- **The wedge sector only.** It is a property of the frame-tier potential, a class the program "selected, not derived" (#11 §14 item 1); deriving that sector from the geometric action is [open problem 1](/wiki/gravity/tuning-test/wedge-reduction).
- **Not a statement about τ.** It removes the spin-2 sector's contribution; the dark-energy field τ carries its own potential, treated in [dark energy](/wiki/cosmology/dark-energy).

## Verification

Two battery tests cover the arithmetic ([the verification battery](/wiki/method/verification/battery)). The recorded gate run prints:

```text
PASS  T5 V(1) - 2T = [0,0,0]  [V1=[2, 8, 6] T=[1, 4, 3]]
PASS  T6 e_n(1+delta) linear coefficients = C(3,n-1) = [0,1,3,3,1]  [[0.0, 1.0, 3.0, 3.0, 1.0]]
```

- **T5 [V]** computes the coefficient vectors of V(1) and T from `math.comb` in exact integers and checks that V(1) − 2T is the zero vector. #11 §2 lists it in Tier 1 as "the palindrome identity as exact integers"; the [handoff](/wiki/history/documents/handoff) as "T5 palindrome V(1) = 2T as exact integers" (HANDOFF §5).
- **T6 [V]** draws one random small symmetric δ (`randsym(1e-6)` in `verify/battery.py`), computes the eₙ of 1 + δ from its eigenvalues, and checks that the linear coefficients match C(3, n − 1) = [0, 1, 3, 3, 1] with absolute tolerance `atol=1e-3`. #11 §2 lists it as "the binomial linearization coefficients".

What the tests do not check: T5 takes the palindrome as input, with β₄ = β₀ and β₃ = β₁ built into its vectors, and neither test touches the flatness condition V(1) = T or the claim that reciprocity acts as the frame exchange. Those steps are derivations [D]. #11 §2's caution applies: "a verification script confirms arithmetic, not the model it encodes" ([verification checks arithmetic, not the model](/wiki/method/verification/arithmetic-not-model)).

## Names and history

The result has had several names:

- "The vacuum-energy theorem [D — rigorous, four lines]" (#8 §2) and "the palindrome theorem" (#8 §4).
- "A four-line theorem" (#1, v0.6 addendum; #9 §0).
- "The palindrome and the Λ theorem [D — rigorous]" (#9 §5 item 5), "the palindrome theorem" and "an unsolicited theorem (Λ_wedge = 0)" (#9 §11).
- "Palindrome/Λ theorem" (HANDOFF §2) and "V(1) = 2T ⇒ Λ_wedge = 0" (HANDOFF §3, row 8); Λ_wedge is the wedge sector's vacuum energy.
- "Palindrome and the vacuum-energy identity" (the heading of #11 §7.3), "A four-line identity [V]" (#11 §1) and "an unsolicited identity (§7.3)" (#11 §15).

Its novelty claim changed. #8 §2 flagged the literature check and wrote that, if the property had not been noticed before, "it is a standalone publishable observation"; #9 §11 counted it among "at least two results that stand on their own regardless of its fate". #11 §7.4 downgraded the claim "from 'likely standalone result' to 'requires detailed comparison with the PM and exchange-symmetric literature'", PM being partially massless, and #11 §15 now counts "one identity awaiting a novelty verdict". The earlier claim is recorded as [superseded](/wiki/gravity/palindromic-branch/pm-comparison#superseded-the-standalone-result-claim) on the comparison page.

The two popular articles ([#10 and #12](/wiki/history/documents/popular-articles)), which are never a source for a claim's status, describe the cancellation and leave its novelty open: "whether the cancellation is new or a rediscovery awaits a careful comparison" (#10, 'What refused to die'). #12 describes the cancellation in the same paragraph as the size of the cosmological-constant problem; by the scope statement above, the identity does not bear on that problem.

## What remains open

- **Novelty.** The convention-careful comparison with partially massless bimetric gravity [24S], with Hossenfelder's exchange-symmetric theory [25S] and with the Schmidt-May–von Strauss review [22S] is open problem 2: [Open: the partially-massless comparison (OP2)](/wiki/gravity/palindromic-branch/pm-comparison).
- **The potential it rests on.** The identity holds for the selected frame-tier class; its derivation from the geometric action is [open problem 1](/wiki/gravity/tuning-test/wedge-reduction).

## Sources

- `papers/broken-born-checkpoint-v2.md` §7.3, §7.4 — the identity as currently stated, its scope, the selected point β₀ = −4β₁ − 3β₂ and the novelty downgrade.
- `papers/broken-born-checkpoint-v2.md` §1, §2, §15, ref [22] — "A four-line identity [V]"; the Tier-1 listing of T5 and T6 and the caution on scripts; the self-assessment; the cited review, marked [S].
- `verify/battery.py` T5, T6 — the construction of the coefficient vectors and the printed checks.
- `notes/debt1a-iv-beta-coefficients.md` §2 — the four-line derivation, the definition of T, the flatness condition and the consequences for τ; §1, §3, §4 for the potential, the parameter count and "the palindrome theorem".
- `HANDOFF.md` §2, §3, §5 — the "Palindrome/Λ theorem" with its machine-check mark and novelty downgrade; Λ_wedge = 0; the description of T5 and T6.
- `notes/broken-born-theory.md` 'Addendum (v0.6)', §7 — the result as first recorded, "vacuum energy = twice the tadpole"; the cosmology chapter that assigns dark energy to τ.
- `notes/broken-born-program-v1.md` §0, §5, §8, §11 — v1's "four-line theorem", "Λ theorem" and "standalone" claim (superseded by #11).
- `popsci/angle-of-the-mirror.md` 'What refused to die'; `popsci/universes-other-half.md` 'The second geometry, and why it has never been seen' — the popular accounts (never a status source).
