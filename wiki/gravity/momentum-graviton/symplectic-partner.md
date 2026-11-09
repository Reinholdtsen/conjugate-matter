---
title: "The symplectic partner of the graviton is another graviton"
weight: 30
status: alive
description: "Doubling geometry with η pairs the metric with a harmless 2-form; doubling with ω pairs it with a second graviton — the program's account of why string theory's doubling works and Born's stalled."
provenance: [D, T]
sources:
  - "wiki/papers/broken-born-checkpoint-v2.md §7.1"
  - "wiki/papers/broken-born-checkpoint-v2.md §7"
  - "wiki/papers/broken-born-checkpoint-v2.md §15"
  - "wiki/papers/broken-born-checkpoint-v2.md §5"
  - "wiki/papers/broken-born-checkpoint-v2.md §7.4"
  - "notes/x-classification.md §2"
  - "notes/x-classification.md §3"
  - "notes/geometric-core.md §A"
  - "notes/geometric-core.md §C"
  - "notes/geometric-core.md §D"
  - "review/round3/referee/audit-notes.md Step 3"
  - "review/round3/referee/step3.py"
  - "notes/broken-born-theory.md §1"
  - "notes/broken-born-theory.md 'Addendum (v0.4)'"
  - "notes/broken-born-program-v1.md §5"
  - "notes/broken-born-program-v1.md §11"
  - "HANDOFF.md §3"
  - "popsci/angle-of-the-mirror.md 'What refused to die'"
  - "review/wiki-build-flags.md item 15"
---

*The observation that the symplectic partner of the graviton is another graviton compares two ways of extending the geometry of spacetime to a doubled space, in which each coordinate has a partner. Each way holds one pairing of the doubled coordinates fixed, and the field that partners the metric is whatever that fixed pairing allows. [Double field theory](../../phase-space/born-geometry/double-field-theory.md), the doubled geometry of string theory, fixes a symmetric pairing η, and the metric's partner is the antisymmetric [B-field](../../phase-space/born-geometry/kalb-ramond-field.md), a 2-form gauge field that is harmless as far as spin goes. The program's phase space fixes the antisymmetric [symplectic form](../../phase-space/reciprocity/symplectic-form.md) ω, and the metric's partner is the [momentum graviton X](_index.md), which is symmetric and has its own [linearized diffeomorphisms](dual-diffeomorphisms.md): a second graviton, and two interacting massless gravitons are inconsistent. [Checkpoint #11](../../history/documents/checkpoint.md) offers this as the structural reason string theory's doubling works while Born's stalled, and its assessment lists it as the one observation that stands regardless of the program's fate. It is derived and rests on literature [D + T]; it is a structural argument, and no script checks it.*

**Status:** Alive — [D + T] in [#11 §7.1](../../papers/broken-born-checkpoint-v2.md#71-the-chain-d--t) and [calc note #6](../../history/documents/field-equation-notes.md) ([`notes/x-classification.md` §2](../../../notes/x-classification.md#2-the-gauge-structure-and-the-no-go-d--t)) — structural, not machine-checked; [#11 §15](../../papers/broken-born-checkpoint-v2.md#15-assessment) lists it as the program's one observation that "stands regardless of its fate".

## The observation

Calc note [#6](../../../notes/x-classification.md) ([the field-equation calc notes](../../history/documents/field-equation-notes.md)) states it as a parenthesis to the gauge structure of X, in a section tagged [D + T] ([§2](../../../notes/x-classification.md#2-the-gauge-structure-and-the-no-go-d--t)). DFT is double field theory:

> (Contrast DFT: there the doubled partner is the antisymmetric B-field, δB = dλ, a 2-form gauge theory — spin-wise harmless. The symmetry type of the rigid structure — η antisymmetric-pairing vs ω — dictates the symmetry type of the partner field. **This is the structural reason string theory's η-doubling exists and naive ω-doubling is hard: the symplectic partner of the graviton is another graviton.**)

The checkpoint keeps the contrast inside step (ii) of its chain ([#11 §7.1](../../papers/broken-born-checkpoint-v2.md#71-the-chain-d--t)): X is "a second linearized-diff gauge field, because X is *symmetric* (contrast DFT's antisymmetric B-field: the symmetry type of the rigid pairing dictates the partner's spin)". Its plain-language passage for [§7](../../papers/broken-born-checkpoint-v2.md#7-the-massive-momentum-graviton): "This, we found, is the structural reason string theory's version of doubled geometry works while the symplectic version stalled since Born: string theory's partner field is a harmless different animal; the symplectic partner of the graviton is another graviton."

## Two doubled geometries

Both constructions double the arena and describe its geometry by a generalized metric H, a positive symmetric 2d × 2d matrix that contains the ordinary metric g together with one more field, the partner. They differ in which pairing of the doubled coordinates is held fixed.

| | Double field theory [T] | The program's phase space |
| --- | --- | --- |
| Doubled coordinates | each coordinate and its dual, conjugate to string winding | position x and momentum p |
| Fixed pairing | the neutral metric η, symmetric | the symplectic form ω, antisymmetric |
| Its symmetry group | O(d, d) | Sp(2d, ℝ) |
| The metric's partner | the B-field, antisymmetric | X = Re Z, symmetric |
| Local transformation of the partner | δB = dλ | δX_μν = ∂₍μλ_ν₎ |
| What the partner is | "a 2-form gauge theory — spin-wise harmless" ([#6 §2](../../../notes/x-classification.md#2-the-gauge-structure-and-the-no-go-d--t)) | "a second graviton-like gauge field" ([#6 §2](../../../notes/x-classification.md#2-the-gauge-structure-and-the-no-go-d--t)) |

In double field theory the generalized metric packages the metric and the Kalb–Ramond B-field of closed string theory, and it preserves η [T] ([double field theory](../../phase-space/born-geometry/double-field-theory.md)). In the program, with only ω rigid ([P2′](../../program/postulates/p2-prime.md)), the positive metrics compatible with ω are the points of [the Siegel domain](../../phase-space/modular-field/siegel-domain.md), written in terms of Z = X + iY ([#5 §C](../../../notes/geometric-core.md#c-the-modular-field-d--structural-math-facts-standard)):

```text
H_Z = [[ Y + XY⁻¹X ,  XY⁻¹ ],
       [ Y⁻¹X      ,  Y⁻¹  ]]
```

with Y = g the metric and X the momentum graviton ([the modular field Z = X + iY](../../phase-space/modular-field/modular-field-z.md)). The structures η and ω themselves are described on [the structures ω, η, H](../../phase-space/born-geometry/born-structures.md).

## Why the partner's symmetry is opposite to the pairing's [T]

The documents state the rule without algebra. The standard algebra behind it is short. Both families of generalized metrics have the form

```text
H = Lᵀ · diag(g, g⁻¹) · L,        L = [[ 1 , 0 ],
                                       [ M , 1 ]]
```

with M = X for the program's H_Z (the factorization is set out on the Siegel-domain page) and M = −B for the B-field family in the form the [round-3](../../method/review/round-3/_index.md) referee's script uses ([`review/round3/referee/step3.py`](../../../review/round3/referee/step3.py), family (c)). The block diag(g, g⁻¹) is compatible with both pairings. A matrix L of this form preserves each fixed pairing only for one symmetry type of M [T]:

```text
Lᵀ η L = [[ M + Mᵀ , 1 ],            Lᵀ ω L = [[ M − Mᵀ ,  1 ],
          [ 1      , 0 ]]                      [ −1     ,  0 ]]
```

with η = [[0, 1], [1, 0]] and ω = [[0, 1], [−1, 0]] in d × d blocks. L preserves η exactly when M is antisymmetric, and preserves ω exactly when M is symmetric, and a metric obtained from a compatible one by a map that preserves the pairing is again compatible [T]. So the off-diagonal field that a fixed symmetric pairing admits is antisymmetric, and the one a fixed antisymmetric pairing admits is symmetric: "The symmetry type of the rigid structure — η antisymmetric-pairing vs ω — dictates the symmetry type of the partner field" ([#6 §2](../../../notes/x-classification.md#2-the-gauge-structure-and-the-no-go-d--t)).

The round-3 blind audit checked both families numerically with its own code, 2000 random trials per family at d = 3 and d = 4 ([`review/round3/referee/audit-notes.md`](../../../review/round3/referee/audit-notes.md) Step 3):

```text
eta-only family (O(d,d) generalized metric with B-field): eta residual <= 7e-14 but omega residual >= 0.28 (d=3), 1.48 (d=4).
omega-only family (Siegel, X != 0): omega residual <= 3e-14 but eta residual >= 0.52 (d=3), 1.87 (d=4).
```

Every B-field metric sampled is compatible with η to rounding error and misses compatibility with ω by a finite margin; every X metric is compatible with ω and misses η. The audit's scripts sit in [`review/round3/referee/`](../../../review/round3/referee/) and are not part of [the gate](../../method/verification/the-gate.md).

## From symmetry type to spin

The symmetry type decides what kind of gauge field the partner is, once its constant shifts are made local.

- **The B-field.** An antisymmetric field shifted by the antisymmetrized derivative of a vector, δB = dλ, is a 2-form gauge field [T]. It is not a spin-2 field and does not compete with the graviton; with the metric and the dilaton it makes up double field theory's massless sector, which propagates without [ghosts](../spin-2-fields/ghosts.md). Calc note #5 cites that sector ("graviton + B-field + dilaton, ghost-free") as evidence that "doubled-geometry kinetic operators can be healthy [T]" ([§D](../../../notes/geometric-core.md#d-quadratic-spectrum-and-the-ghost-question-partial)).
- **X.** A symmetric field shifted by the symmetrized derivative, δX_μν = ∂₍μλ_ν₎, has the gauge structure of the graviton itself: "a *second copy of linearized diffeomorphisms*, making X a second graviton-like gauge field" ([#6 §2](../../../notes/x-classification.md#2-the-gauge-structure-and-the-no-go-d--t); [dual diffeomorphisms](dual-diffeomorphisms.md)). Two interacting massless gravitons are excluded by [the multi-graviton no-go theorem](../spin-2-fields/multi-graviton-no-go.md) [T], and X must couple to the metric and to [conjugate matter](../../dark-matter/conjugate-matter/_index.md) χ ([#6 §2](../../../notes/x-classification.md#2-the-gauge-structure-and-the-no-go-d--t)), so X cannot stay massless.

Hence the observation as #6 words it: the symplectic partner of the graviton is another graviton. #11 says the pairing "dictates the partner's spin"; #6 says it dictates "the symmetry type of the partner field". The step from one to the other is the gauge structure above.

## The program's reading

The documents use the observation to explain a difference between two lines of work: "This is the structural reason string theory's η-doubling exists and naive ω-doubling is hard" ([#6 §2](../../../notes/x-classification.md#2-the-gauge-structure-and-the-no-go-d--t)), and "why string theory's doubling works and Born's stalled" ([#11 §15](../../papers/broken-born-checkpoint-v2.md#15-assessment)). Doubling with η gives a partner that causes no difficulty; doubling with ω gives a second graviton, which a consistent theory can carry only if it is massive.

The program does not stop at the difficulty. [#11 §7](../../papers/broken-born-checkpoint-v2.md#7-the-massive-momentum-graviton) continues that mass is the only exit, and that the vacuum's choice of [polarization](../../phase-space/reciprocity/lagrangian-polarizations.md) provides it: X absorbs the [would-be Goldstone modes](../../symmetry-breaking/goldstone-and-higgs.md) of the broken dual diffeomorphisms and becomes a massive spin-2 field ([why X must be massive](forcing-chain.md); [the gravitational Higgs mechanism](gravitational-higgs.md)). Whether that massive field is healthy was [the tuning test](../tuning-test/_index.md).

The v1 paper's plain-language passage called the observation "the deep reason string theory's version of doubled geometry works" ([#9 §5](../../../notes/broken-born-program-v1.md#5-the-second-graviton-and-its-mass-the-field-equation-problem-solved)); #11's passage says "the structural reason".

## With both pairings rigid: no partner at all

If η and ω are both held fixed, neither partner survives. This is corollary 2 of [the compatibility theorem](../../phase-space/born-geometry/compatibility-theorem.md), in calc note #5's words: "**No Kalb–Ramond analog.** The off-diagonal block — DFT's B-field — is frozen out by the extra symplectic compatibility. Born geometry with both structures rigid is *stiffer* than DFT." ([§A](../../../notes/geometric-core.md#a-the-compatibility-theorem-d--rigorous); [the corollaries](../../phase-space/born-geometry/compatibility-corollaries.md).) #11 credits the statement to Freidel, Leigh and Minic: "writing the η-compatible H in terms of (G, B), H is related to ω through a complex structure exactly when B vanishes [26S, §2.1]" ([§5](../../papers/broken-born-checkpoint-v2.md#5-the-kinematic-core-and-the-compatibility-theorem)). The theorem leaves H = diag(g, g⁻¹), the slice X = 0, so the symmetric partner is absent too. That was the situation under the [original P2](../../program/postulates/original-p2.md). Under P2′, η is emergent, and X is "exactly the fluctuation that breaks η-compatibility" ([#5 §C](../../../notes/geometric-core.md#c-the-modular-field-d--structural-math-facts-standard)).

## Standing

#11's assessment counts the program's output, and this observation comes first: "The program has produced one observation that stands regardless of its fate (the symplectic partner of the graviton is another graviton — why string theory's doubling works and Born's stalled), one identity awaiting a novelty verdict, one new experimental question (the knee-shape discriminant), one structural unification (polarization of phase space and of charge space as one move), and a three-way question about dark matter's nature with named discriminators" ([§15](../../papers/broken-born-checkpoint-v2.md#15-assessment); [Assessment: a live research program](../../program/assessment.md); on the structural unification, flag 67 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md), pending). The assessment gives no separate argument for why this item stands regardless of the program's fate.

## Superseded: the v1 count of two standalone results

The v1 paper counted two results that would outlast the program: "This one has produced at least two results that stand on their own regardless of its fate — the observation that the symplectic partner of the graviton is another graviton (explaining why string theory's doubling works and Born's stalled), and the palindrome theorem cancelling the symmetric-bimetric vacuum energy" ([#9 §11](../../../notes/broken-born-program-v1.md#11-assessment)). [#11 §15](../../papers/broken-born-checkpoint-v2.md#15-assessment) keeps only the first. The second, now [the vacuum-energy identity V(1) = 2T](../palindromic-branch/vacuum-energy-identity.md), was downgraded by [#11 §7.4](../../papers/broken-born-checkpoint-v2.md#74-literature-position-updated-by-this-sessions-search--honesty-upgrade) after a literature search found the [partially-massless parameter point](../spin-2-fields/partially-massless-gravity.md) inside the same branch: the novelty claim went from "likely standalone result" to "requires detailed comparison with the PM and exchange-symmetric literature", PM being partially massless ([the partially-massless comparison](../palindromic-branch/pm-comparison.md)). It is "one identity awaiting a novelty verdict" ([#11 §15](../../papers/broken-born-checkpoint-v2.md#15-assessment)).

## Popsci-only: a forty-year asymmetry

The first popular article puts a date on the asymmetry: "(As a side effect, this explains a forty-year asymmetry in theoretical physics: string theory's version of doubled geometry thrived because *its* partner field is a harmless different species; Born's version stalled because his partner was gravity's identical twin.)" ([#10](../../../popsci/angle-of-the-mirror.md), 'What refused to die'). No technical document dates the asymmetry: [#11 §7](../../papers/broken-born-checkpoint-v2.md#7-the-massive-momentum-graviton) says that "the symplectic version stalled since Born", and [#9 §5](../../../notes/broken-born-program-v1.md#5-the-second-graviton-and-its-mass-the-field-equation-problem-solved) that "ω-doubling stalled since Born". The popular articles are never a source for a claim's status ([the popular articles](../../history/documents/popular-articles.md)), and the forty-year dating has no source in the record.

## Scope and caveats

- **A quoted ambiguity.** #6's phrase "η antisymmetric-pairing vs ω" is quoted unchanged and not paraphrased. η itself is a symmetric pairing, "a neutral (split-signature) metric" ([lab notebook](../../history/documents/lab-notebook.md) [#1 §1](../../../notes/broken-born-theory.md#1-postulates), postulate [P1](../../program/postulates/p1-arena.md)), so the phrase is ambiguous as written (see flag 15 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md)). [#11 §7.1](../../papers/broken-born-checkpoint-v2.md#71-the-chain-d--t)'s restatement, "the symmetry type of the rigid pairing dictates the partner's spin", does not use it.
- **Structural, not computed.** The program's part [D] is the identification of X as the partner and of its local gauge structure; the facts it is set against, double field theory's B-field and the no-go theorem, are literature [T]. No document writes an action for X, and no script checks the argument; the round-3 numbers above check only that the two families of metrics are compatible with different pairings.
- **Positive metrics.** The Siegel parametrization assumes a positive-definite H, and #6 calls the chain of its §1–§3 "the Euclidean-rigorous skeleton" ([§3](../../../notes/x-classification.md#3-the-mass-mechanism-and-the-endpoint-d--structural)); the extension to spacetime signature is open item 3 ([Open: Lorentzian dressing of the Euclidean skeleton (OP3)](../../phase-space/born-geometry/lorentzian-dressing.md)).

## History

- **First statement.** Calc note [#6 §2](../../../notes/x-classification.md#2-the-gauge-structure-and-the-no-go-d--t), quoted above.
- **The lab notebook.** The v0.4 addendum: X's local gauge structure "makes it a *second graviton* — which is the structural reason η-doubling (string theory's B-field) is easy and ω-doubling is hard: the symplectic partner of the graviton is another graviton" ([the lab notebook](../../history/documents/lab-notebook.md)).
- **The v1 paper.** [#9 §5 item 2](../../../notes/broken-born-program-v1.md#5-the-second-graviton-and-its-mass-the-field-equation-problem-solved): "Contrast DFT, whose partner is the antisymmetric B-field — a 2-form, spin-harmless: *the symmetry type of the rigid pairing dictates the partner's spin, which is why η-doubling (strings) exists and ω-doubling stalled since Born.*" [#9 §11](../../../notes/broken-born-program-v1.md#11-assessment) counted it among two standalone results (above).
- **The checkpoint.** [#11 §7.1](../../papers/broken-born-checkpoint-v2.md#71-the-chain-d--t) and the plain-language passage of [§7](../../papers/broken-born-checkpoint-v2.md#7-the-massive-momentum-graviton) state it; [§15](../../papers/broken-born-checkpoint-v2.md#15-assessment) makes it the one observation that stands regardless of the program's fate. [The handoff](../../history/documents/handoff.md)'s inventory describes calc note #6 with the phrase in quotation marks: "symplectic partner of the graviton is another graviton" ([`HANDOFF.md` §3](../../../HANDOFF.md#3-artifact-inventory-creation-order), row 6).

## Sources

- [`wiki/papers/broken-born-checkpoint-v2.md` §7.1](../../papers/broken-born-checkpoint-v2.md#71-the-chain-d--t) — the current statement, inside step (ii) of the chain; [§7](../../papers/broken-born-checkpoint-v2.md#7-the-massive-momentum-graviton) — the plain-language passage; [§15](../../papers/broken-born-checkpoint-v2.md#15-assessment) — its standing; [§5](../../papers/broken-born-checkpoint-v2.md#5-the-kinematic-core-and-the-compatibility-theorem) — the Freidel–Leigh–Minic statement on B; [§7.4](../../papers/broken-born-checkpoint-v2.md#74-literature-position-updated-by-this-sessions-search--honesty-upgrade) — the downgrade of the identity.
- [`notes/x-classification.md` §2](../../../notes/x-classification.md#2-the-gauge-structure-and-the-no-go-d--t) — the original statement [D + T]; [§3](../../../notes/x-classification.md#3-the-mass-mechanism-and-the-endpoint-d--structural) — the Euclidean-rigorous skeleton.
- [`notes/geometric-core.md` §A](../../../notes/geometric-core.md#a-the-compatibility-theorem-d--rigorous) — corollary 2, no Kalb–Ramond analog; [§C](../../../notes/geometric-core.md#c-the-modular-field-d--structural-math-facts-standard) — H_Z and X as the fluctuation that breaks η-compatibility; [§D](../../../notes/geometric-core.md#d-quadratic-spectrum-and-the-ghost-question-partial) — the healthy precedent of double field theory.
- [`review/round3/referee/audit-notes.md`](../../../review/round3/referee/audit-notes.md) Step 3 and [`review/round3/referee/step3.py`](../../../review/round3/referee/step3.py) — the two families of metrics, checked by independent code.
- [`notes/broken-born-theory.md` §1](../../../notes/broken-born-theory.md#1-postulates) — η as a neutral metric; 'Addendum (v0.4)' — the notebook's statement.
- [`notes/broken-born-program-v1.md` §5](../../../notes/broken-born-program-v1.md#5-the-second-graviton-and-its-mass-the-field-equation-problem-solved), [§11](../../../notes/broken-born-program-v1.md#11-assessment) — the v1 statement and its "two results" count.
- [`HANDOFF.md` §3](../../../HANDOFF.md#3-artifact-inventory-creation-order) — the inventory entry for calc note #6.
- [`popsci/angle-of-the-mirror.md`](../../../popsci/angle-of-the-mirror.md) 'What refused to die' — the popular article's "forty-year asymmetry".
- [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md) item 15 — [#6 §2](../../../notes/x-classification.md#2-the-gauge-structure-and-the-no-go-d--t)'s "η antisymmetric-pairing vs ω", which reads as calling η antisymmetric (pending).
