---
title: "The symplectic partner of the graviton is another graviton"
weight: 30
status: alive
description: "Doubling geometry with η pairs the metric with a harmless 2-form; doubling with ω pairs it with a second graviton — the program's account of why string theory's doubling works and Born's stalled."
provenance: [D, T]
sources:
  - "papers/broken-born-checkpoint-v2.md §7.1"
  - "papers/broken-born-checkpoint-v2.md §7"
  - "papers/broken-born-checkpoint-v2.md §15"
  - "papers/broken-born-checkpoint-v2.md §5"
  - "papers/broken-born-checkpoint-v2.md §7.4"
  - "notes/debt1a-ii-X-classification.md §2"
  - "notes/debt1a-ii-X-classification.md §3"
  - "notes/debt1a-geometric-core.md §A"
  - "notes/debt1a-geometric-core.md §C"
  - "notes/debt1a-geometric-core.md §D"
  - "review/round3/referee/audit-notes.md Step 3"
  - "review/round3/referee/step3.py"
  - "notes/broken-born-theory.md §1"
  - "notes/broken-born-theory.md 'Addendum (v0.4)'"
  - "notes/broken-born-program-v1.md §5"
  - "notes/broken-born-program-v1.md §11"
  - "HANDOFF.md §3"
  - "popsci/angle-of-the-mirror.md 'What refused to die'"
---

*This observation compares two ways of extending the geometry of spacetime to a doubled space, in which each coordinate has a partner. Each way holds one pairing of the doubled coordinates fixed, and the field that partners the metric is whatever that fixed pairing allows. [Double field theory](/wiki/phase-space/born-geometry/double-field-theory), the doubled geometry of string theory, fixes a symmetric pairing η, and the metric's partner is the antisymmetric B-field, a 2-form gauge field that is harmless as far as spin goes. The program's phase space fixes the antisymmetric [symplectic form](/wiki/phase-space/reciprocity/symplectic-form) ω, and the metric's partner is the momentum graviton X, which is symmetric and has its own [linearized diffeomorphisms](/wiki/gravity/momentum-graviton/dual-diffeomorphisms): a second graviton, and two interacting massless gravitons are inconsistent. [Checkpoint #11](/wiki/history/documents/checkpoint) offers this as the structural reason string theory's doubling works while Born's stalled, and its assessment lists it as the one observation that stands regardless of the program's fate. It is derived and rests on literature [D + T]; it is a structural argument, not a computation a script could check.*

**Status:** Alive — [D + T] in #11 §7.1 and calc note #6 (`notes/debt1a-ii-X-classification.md` §2) — structural, not machine-checked; #11 §15 lists it as the program's one observation that "stands regardless of its fate".

## The observation

Calc note #6 ([the Debt-1 calc notes](/wiki/history/documents/debt-1-notes)) states it as a parenthesis to the gauge structure of X, in a section tagged [D + T] (§2). DFT is double field theory:

> (Contrast DFT: there the doubled partner is the antisymmetric B-field, δB = dλ, a 2-form gauge theory — spin-wise harmless. The symmetry type of the rigid structure — η antisymmetric-pairing vs ω — dictates the symmetry type of the partner field. **This is the structural reason string theory's η-doubling exists and naive ω-doubling is hard: the symplectic partner of the graviton is another graviton.**)

The checkpoint keeps the contrast inside step (ii) of its chain (#11 §7.1): X is "a second linearized-diff gauge field, because X is *symmetric* (contrast DFT's antisymmetric B-field: the symmetry type of the rigid pairing dictates the partner's spin)". Its plain-language passage for §7: "This, we found, is the structural reason string theory's version of doubled geometry works while the symplectic version stalled since Born: string theory's partner field is a harmless different animal; the symplectic partner of the graviton is another graviton."

## Two doubled geometries

Both constructions double the arena and describe its geometry by a generalized metric H, a positive symmetric 2d × 2d matrix that contains the ordinary metric g together with one more field, the partner. They differ in which pairing of the doubled coordinates is held fixed.

| | Double field theory [T] | The program's phase space |
| --- | --- | --- |
| Doubled coordinates | each coordinate and its dual, conjugate to string winding | position x and momentum p |
| Fixed pairing | the neutral metric η, symmetric | the symplectic form ω, antisymmetric |
| Its symmetry group | O(d, d) | Sp(2d, ℝ) |
| The metric's partner | the B-field, antisymmetric | X = Re Z, symmetric |
| Local transformation of the partner | δB = dλ | δX_μν = ∂₍μλ_ν₎ |
| What the partner is | "a 2-form gauge theory — spin-wise harmless" (#6 §2) | "a second graviton-like gauge field" (#6 §2) |

In double field theory the generalized metric packages the metric and the Kalb–Ramond B-field of closed string theory, and it preserves η [T] ([double field theory](/wiki/phase-space/born-geometry/double-field-theory)). In the program, with only ω rigid ([P2′](/wiki/program/postulates/p2-prime)), the positive metrics compatible with ω are the points of [the Siegel domain](/wiki/phase-space/modular-field/siegel-domain), written in terms of Z = X + iY (#5 §C):

```text
H_Z = [[ Y + XY⁻¹X ,  XY⁻¹ ],
       [ Y⁻¹X      ,  Y⁻¹  ]]
```

with Y = g the metric and X the momentum graviton ([the modular field Z = X + iY](/wiki/phase-space/modular-field/modular-field-z)). The structures η and ω themselves are described on [the structures ω, η, H](/wiki/phase-space/born-geometry/born-structures).

## Why the partner's symmetry is opposite to the pairing's [T]

The documents state the rule without algebra. The standard algebra behind it is short. Both families of generalized metrics have the form

```text
H = Lᵀ · diag(g, g⁻¹) · L,        L = [[ 1 , 0 ],
                                       [ M , 1 ]]
```

with M = X for the program's H_Z (the factorization is set out on the Siegel-domain page) and M = −B for the B-field family in the form the round-3 referee's script uses (`review/round3/referee/step3.py`, family (c)). The block diag(g, g⁻¹) is compatible with both pairings. A matrix L of this form preserves each fixed pairing only for one symmetry type of M [T]:

```text
Lᵀ η L = [[ M + Mᵀ , 1 ],            Lᵀ ω L = [[ M − Mᵀ ,  1 ],
          [ 1      , 0 ]]                      [ −1     ,  0 ]]
```

with η = [[0, 1], [1, 0]] and ω = [[0, 1], [−1, 0]] in d × d blocks. L preserves η exactly when M is antisymmetric, and preserves ω exactly when M is symmetric, and a metric obtained from a compatible one by a map that preserves the pairing is again compatible [T]. So the off-diagonal field that a fixed symmetric pairing admits is antisymmetric, and the one a fixed antisymmetric pairing admits is symmetric: "The symmetry type of the rigid structure — η antisymmetric-pairing vs ω — dictates the symmetry type of the partner field" (#6 §2).

The round-3 blind audit checked both families numerically with its own code, 2000 random trials per family at d = 3 and d = 4 (`review/round3/referee/audit-notes.md` Step 3):

```text
eta-only family (O(d,d) generalized metric with B-field): eta residual <= 7e-14 but omega residual >= 0.28 (d=3), 1.48 (d=4).
omega-only family (Siegel, X != 0): omega residual <= 3e-14 but eta residual >= 0.52 (d=3), 1.87 (d=4).
```

Every B-field metric sampled is compatible with η to rounding error and misses compatibility with ω by a finite margin; every X metric is compatible with ω and misses η. The audit's scripts sit in `review/round3/referee/` and are not part of the gate.

## From symmetry type to spin

The symmetry type decides what kind of gauge field the partner is, once its constant shifts are made local.

- **The B-field.** An antisymmetric field shifted by the antisymmetrized derivative of a vector, δB = dλ, is a 2-form gauge field [T]. It is not a spin-2 field and does not compete with the graviton; with the metric and the dilaton it makes up double field theory's massless sector, which propagates without ghosts. Calc note #5 cites that sector ("graviton + B-field + dilaton, ghost-free") as evidence that "doubled-geometry kinetic operators can be healthy [T]" (§D).
- **X.** A symmetric field shifted by the symmetrized derivative, δX_μν = ∂₍μλ_ν₎, has the gauge structure of the graviton itself: "a *second copy of linearized diffeomorphisms*, making X a second graviton-like gauge field" (#6 §2; [dual diffeomorphisms](/wiki/gravity/momentum-graviton/dual-diffeomorphisms)). Two interacting massless gravitons are excluded by [the multi-graviton no-go theorem](/wiki/gravity/spin-2-fields/multi-graviton-no-go) [T], and X must couple to the metric and to matter, so X cannot stay massless.

Hence the observation as #6 words it: the symplectic partner of the graviton is another graviton. #11 says the pairing "dictates the partner's spin"; #6 says it dictates "the symmetry type of the partner field". The step from one to the other is the gauge structure above.

## The program's reading

The documents use the observation to explain a difference between two lines of work: "This is the structural reason string theory's η-doubling exists and naive ω-doubling is hard" (#6 §2), and "why string theory's doubling works and Born's stalled" (#11 §15). Doubling with η gives a partner that causes no difficulty; doubling with ω gives a second graviton, which a consistent theory can carry only if it is massive.

The program does not stop at the difficulty. #11 §7 continues that mass is the only exit, and that the vacuum's choice of polarization provides it: X absorbs the would-be Goldstone modes of the broken dual diffeomorphisms and becomes a massive spin-2 field ([why X must be massive](/wiki/gravity/momentum-graviton/forcing-chain); [the gravitational Higgs mechanism](/wiki/gravity/momentum-graviton/gravitational-higgs)). Whether that massive field is healthy was [the tuning test](/wiki/gravity/tuning-test).

The v1 paper's plain-language passage called the observation "the deep reason string theory's version of doubled geometry works" (#9 §5); #11's passage says "the structural reason".

## With both pairings rigid: no partner at all

If η and ω are both held fixed, neither partner survives. This is corollary 2 of [the compatibility theorem](/wiki/phase-space/born-geometry/compatibility-theorem), in calc note #5's words: "**No Kalb–Ramond analog.** The off-diagonal block — DFT's B-field — is frozen out by the extra symplectic compatibility. Born geometry with both structures rigid is *stiffer* than DFT." (§A; [the corollaries](/wiki/phase-space/born-geometry/compatibility-corollaries).) #11 credits the statement to Freidel, Leigh and Minic: "writing the η-compatible H in terms of (G, B), H is related to ω through a complex structure exactly when B vanishes [26S, §2.1]" (§5). The theorem leaves H = diag(g, g⁻¹), the slice X = 0, so the symmetric partner is absent too. That was the situation under the [original P2](/wiki/program/postulates/original-p2). Under P2′, η is emergent, and X is "exactly the fluctuation that breaks η-compatibility" (#5 §C).

## Standing

#11's assessment counts the program's output, and this observation comes first: "The program has produced one observation that stands regardless of its fate (the symplectic partner of the graviton is another graviton — why string theory's doubling works and Born's stalled), one identity awaiting a novelty verdict, one new experimental question (the knee-shape discriminant), one structural unification (polarization of phase space and of charge space as one move), and a two-way question about dark matter's nature with named discriminators" (§15; [Assessment: a live research program](/wiki/program/assessment)). The assessment gives no separate argument for why this item stands regardless of the program's fate.

## Superseded: the v1 count of two standalone results

The v1 paper counted two results that would outlast the program: "This one has produced at least two results that stand on their own regardless of its fate — the observation that the symplectic partner of the graviton is another graviton (explaining why string theory's doubling works and Born's stalled), and the palindrome theorem cancelling the symmetric-bimetric vacuum energy" (#9 §11). #11 §15 keeps only the first. The second, now [the vacuum-energy identity V(1) = 2T](/wiki/gravity/palindromic-branch/vacuum-energy-identity), was downgraded by #11 §7.4 after a literature search found the partially-massless parameter point inside the same branch: the novelty claim went from "likely standalone result" to "requires detailed comparison with the PM and exchange-symmetric literature", PM being partially massless ([the partially-massless comparison](/wiki/gravity/palindromic-branch/pm-comparison)). It is "one identity awaiting a novelty verdict" (#11 §15).

## Popsci-only: a forty-year asymmetry

The first popular article puts a date on the asymmetry: "(As a side effect, this explains a forty-year asymmetry in theoretical physics: string theory's version of doubled geometry thrived because *its* partner field is a harmless different species; Born's version stalled because his partner was gravity's identical twin.)" (#10, 'What refused to die'). No technical document dates the asymmetry: #11 §7 says that "the symplectic version stalled since Born", and #9 §5 that "ω-doubling stalled since Born". The popular articles are never a source for a claim's status ([the popular articles](/wiki/history/documents/popular-articles)), and the forty-year dating has no source in the record.

## Scope and caveats

- **A quoted ambiguity.** #6's phrase "η antisymmetric-pairing vs ω" is quoted unchanged and not paraphrased. η itself is a symmetric pairing, "a neutral (split-signature) metric" (lab notebook #1 §1, postulate P1), so the phrase is ambiguous as written. #11 §7.1's restatement, "the symmetry type of the rigid pairing dictates the partner's spin", does not use it.
- **Structural, not computed.** The program's part [D] is the identification of X as the partner and of its local gauge structure; the facts it is set against, double field theory's B-field and the no-go theorem, are literature [T]. No document writes an action for X, and no script checks the argument; the round-3 numbers above check only that the two families of metrics are compatible with different pairings.
- **Positive metrics.** The Siegel parametrization assumes a positive-definite H, and #6 calls the chain of its §1–§3 "the Euclidean-rigorous skeleton" (§3); the extension to spacetime signature is open item 3 ([Open: Lorentzian dressing of the Euclidean skeleton (OP3)](/wiki/phase-space/born-geometry/lorentzian-dressing)).

## History

- **First statement.** Calc note #6 §2, quoted above.
- **The lab notebook.** The v0.4 addendum: X's local gauge structure "makes it a *second graviton* — which is the structural reason η-doubling (string theory's B-field) is easy and ω-doubling is hard: the symplectic partner of the graviton is another graviton" ([the lab notebook](/wiki/history/documents/lab-notebook)).
- **The v1 paper.** #9 §5 item 2: "Contrast DFT, whose partner is the antisymmetric B-field — a 2-form, spin-harmless: *the symmetry type of the rigid pairing dictates the partner's spin, which is why η-doubling (strings) exists and ω-doubling stalled since Born.*" #9 §11 counted it among two standalone results (above).
- **The checkpoint.** #11 §7.1 and the plain-language passage of §7 state it; §15 makes it the one observation that stands regardless of the program's fate. The handoff's inventory describes calc note #6 with the phrase in quotation marks: "symplectic partner of the graviton is another graviton" (`HANDOFF.md` §3, row 6).

## Sources

- `papers/broken-born-checkpoint-v2.md` §7.1 — the current statement, inside step (ii) of the chain; §7 — the plain-language passage; §15 — its standing; §5 — the Freidel–Leigh–Minic statement on B; §7.4 — the downgrade of the identity.
- `notes/debt1a-ii-X-classification.md` §2 — the original statement [D + T]; §3 — the Euclidean-rigorous skeleton.
- `notes/debt1a-geometric-core.md` §A — corollary 2, no Kalb–Ramond analog; §C — H_Z and X as the fluctuation that breaks η-compatibility; §D — the healthy precedent of double field theory.
- `review/round3/referee/audit-notes.md` Step 3 and `review/round3/referee/step3.py` — the two families of metrics, checked by independent code.
- `notes/broken-born-theory.md` §1 — η as a neutral metric; 'Addendum (v0.4)' — the notebook's statement.
- `notes/broken-born-program-v1.md` §5, §11 — the v1 statement and its "two results" count.
- `HANDOFF.md` §3 — the inventory entry for calc note #6.
- `popsci/angle-of-the-mirror.md` 'What refused to die' — the popular article's "forty-year asymmetry".
