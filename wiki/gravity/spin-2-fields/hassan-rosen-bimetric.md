---
title: "Hassan–Rosen bimetric gravity"
weight: 50
status: established
description: "Two dynamical metrics with the ghost-free potential V = 2m²M² Σ βₙ eₙ(√(g⁻¹f)) and its exchange identity Sₙ(g, f) = S₄₋ₙ(f, g)."
provenance: [T]
sources:
  - "papers/broken-born-checkpoint-v2.md §1"
  - "papers/broken-born-checkpoint-v2.md §7"
  - "papers/broken-born-checkpoint-v2.md §7.1"
  - "papers/broken-born-checkpoint-v2.md §7.3"
  - "papers/broken-born-checkpoint-v2.md §7.4"
  - "papers/broken-born-checkpoint-v2.md §7.5"
  - "papers/broken-born-checkpoint-v2.md refs [10]–[12], [22], [24], [25]"
  - "review/round3/referee/audit-notes.md Step 1"
  - "notes/debt1a-iv-beta-coefficients.md §1"
  - "notes/debt1a-iv-beta-coefficients.md §3"
  - "notes/debt1a-iii-tuning-test.md §2"
  - "notes/debt1a-iii-tuning-test.md §4"
  - "notes/knot-dark-matter-standalone.md §1"
  - "notes/knot-dark-matter-standalone.md ref [3]"
  - "HANDOFF.md §2"
  - "review/wiki-build-flags.md items 8, 9"
---

*Hassan–Rosen bimetric gravity is a theory of two dynamical metrics, g and f, each with its own Einstein–Hilbert term, coupled through a potential that keeps the [Boulware–Deser ghost](/wiki/gravity/spin-2-fields/fierz-pauli#beyond-quadratic-order-the-boulwaredeser-ghost-t) out. The potential is a sum of five terms with constant coefficients β₀ to β₄, the n-th term built from the [elementary symmetric polynomial](/wiki/gravity/spin-2-fields/elementary-symmetric-polynomials) eₙ of the matrix √(g⁻¹f). An identity of these polynomials makes the exchange of the two metrics reverse the order of the terms, so the list of coefficients is read backwards. About proportional backgrounds the theory has one massless and one massive spin-2 field. The program's geometric sector, the home of its [momentum graviton X](/wiki/gravity/momentum-graviton), lands in this theory with the second frame confined to a compact space, and [Born reciprocity](/wiki/phase-space/reciprocity/born-reciprocity), acting as the exchange of the two frames, then forces the list of coefficients to read the same in both directions, [the palindrome βₙ = β₄₋ₙ](/wiki/gravity/palindromic-branch/palindrome).*

**Status:** Established — [T] — cited in the [checkpoint](/wiki/history/documents/checkpoint) as [10†, 11†], from model memory. The same two papers, as reference [3] of the withdrawn manuscript [#14](/wiki/dark-matter/candidates/soliton-candidate), were resolved on INSPIRE in the [round-3 audit](/wiki/method/review/round-3/rulings), which found that they support "ghost-free (bi)metric structure" (`review/round3/referee/audit-notes.md` Step 1). Calc note [#8](/wiki/history/documents/debt-1-notes) §1 writes the potential and the exchange identity under its [D] heading; both are literature, and what the note derives from them is the palindrome. Nothing on this page is machine-checked; battery test T7, which checks numerically that the power sum p₄ lies outside the linear span of the eₙ, is on [the verification battery](/wiki/method/verification/battery).

## From one dynamical metric to two [T]

In [dRGT massive gravity](/wiki/gravity/spin-2-fields/drgt-massive-gravity) the second metric f is fixed in advance. Hassan and Rosen showed that f can be made dynamical, with its own Einstein–Hilbert term and its own [Planck mass](/wiki/gravity/spin-2-fields/planck-units#two-metrics-two-planck-masses), without bringing back the [Boulware–Deser ghost](/wiki/gravity/spin-2-fields/fierz-pauli) (the paper the checkpoint cites as [11†], "Bimetric gravity from ghost-free massive gravity"). Theories with two interacting dynamical metrics are older (Isham, Salam and Strathdee 1971†). What is new in Hassan and Rosen's theory is that the interaction is the [ghost-free](/wiki/gravity/spin-2-fields/ghosts) potential of massive gravity, and that giving f its own dynamics keeps it ghost-free. The action has the form

```text
S = S_EH[g; M_g] + S_EH[f; M_f] − ∫ d⁴x √−g V(g, f) + S_matter[ψ; g]
V = 2m²M² Σₙ₌₀⁴ βₙ eₙ(𝕏),        𝕏 = √(g⁻¹f)
```

M_g and M_f are the Planck masses of the two metrics, and in the standard theory matter couples to g alone [T]. The second line is the potential as calc note #8 §1 writes it for the program's two frames (e, f = E₀[J]). #8 defines neither m nor M; the same prefactor appears in Hassan and Rosen's papers, where m sets the mass scale and M is a Planck-mass scale built from M_g and M_f (from model memory †). The eₙ are the [elementary symmetric polynomials](/wiki/gravity/spin-2-fields/elementary-symmetric-polynomials) of the eigenvalues of 𝕏.

**What each term does** [T]. Since e₀ = 1, the β₀ term is β₀√−g, a [cosmological constant](/wiki/cosmology/dark-energy/cosmological-constant#cosmological-constants-in-the-bimetric-potential) for g. Since e₄ = det 𝕏 and √−g det 𝕏 = √−f, the β₄ term is β₄√−f, a cosmological constant for f. The terms β₁, β₂ and β₃ are the interactions between the two metrics.

**Linear in the eₙ.** The coefficients are constants and the potential is linear in the eₙ. Calc note #7 §2: "The Hassan–Rosen ghost-free family is *linear* combinations Σβₙeₙ(√(g⁻¹f)) (constants βₙ)". A potential that is a nonlinear function of the eₙ lies outside the family, which is the second failure of the program's metric-built potential ([the metric tier fails twice](/wiki/gravity/tuning-test/metric-tier-failures)).

## The exchange identity [T]

Calc note #8 §1 states it as "the exchange identity Sₙ(g,f) = S₄₋ₙ(f,g)" and does not define Sₙ. The identity in the literature reads

```text
√−g eₙ(√(g⁻¹f)) = √−f e₄₋ₙ(√(f⁻¹g))
```

Reading Sₙ(g, f) as the n-th term of the potential, √−g eₙ(√(g⁻¹f)), gives #8's form; the note itself does not say so.

**Why it holds** [T]. Let λ₁, …, λ₄ be the eigenvalues of 𝕏. A product of n of them equals the product of all four divided by the product of the remaining 4 − n, so eₙ of the λ's equals λ₁λ₂λ₃λ₄ times e₄₋ₙ of their reciprocals. The product of all four is det 𝕏, and √−g det 𝕏 = √−f. The reciprocals are the eigenvalues of 𝕏⁻¹ = √(f⁻¹g). Together these give the identity.

**What it does to the potential** [T]. Exchanging g and f turns the potential term √−g Σ βₙ eₙ(√(g⁻¹f)) into √−f Σ βₙ eₙ(√(f⁻¹g)), which by the identity is √−g Σ βₙ e₄₋ₙ(√(g⁻¹f)). The coefficient of eₙ is now β₄₋ₙ: the exchange reads the list of coefficients backwards.

```text
(β₀, β₁, β₂, β₃, β₄)   →   (β₄, β₃, β₂, β₁, β₀)        under g ↔ f
```

If the two Planck masses are exchanged as well, the two Einstein–Hilbert terms trade places. In terms of the roles above, the exchange swaps the two cosmological constants β₀ and β₄ and swaps β₁ with β₃.

**What the program derives from it.** Born reciprocity acts on the program's broken vacuum as the exchange of its two frames, "𝕏 → 𝕏⁻¹ in the aligned frame" (#8 §1). Invariance of the potential under that exchange "therefore forces the **palindromic constraint**" βₙ = β₄₋ₙ, that is "β₀=β₄, β₁=β₃, β₂ free" [D] (#8 §1). The checkpoint tags the section that states it [D][V] (#11 §7.3); the battery checks the vacuum-energy identity that follows from the palindrome (test T5), not the palindrome's derivation. See [the palindrome βₙ = β₄₋ₙ](/wiki/gravity/palindromic-branch/palindrome) and [the vacuum-energy identity V(1) = 2T](/wiki/gravity/palindromic-branch/vacuum-energy-identity).

## Ghost freedom [T]

Hassan and Rosen showed that the bimetric theory with this potential is free of the Boulware–Deser ghost, by the same mechanism as dRGT massive gravity: in the Hamiltonian formulation a constraint survives that removes the extra mode ([10†], "Resolving the ghost problem in non-linear massive gravity"; [11†]). The theory propagates one massless and one massive spin-2 field and nothing else. In frame variables the same potentials are the wedge polynomials of Hinterbichler and Rosen ([12†]; [the vielbein formulation and wedge potentials](/wiki/gravity/spin-2-fields/vielbein-formulation)).

## The spectrum [T]

The simplest backgrounds have the two metrics proportional, f = c²g with c a constant. Linearizing about such a background, the fluctuations of g and f combine into one massless spin-2 mode and one massive spin-2 mode. The massless mode is a graviton with the gauge symmetry of [general relativity](/wiki/gravity/spin-2-fields/general-relativity); the massive one has a [Fierz–Pauli](/wiki/gravity/spin-2-fields/fierz-pauli) mass set by m and a combination of the βₙ. Matter coupled to g feels both modes in proportions set by the two Planck masses.

Calc note #7 §4 applies these "Standard bimetric facts" [T] to the program, for Standard Model (SM) matter: "one massless combination (our graviton, coupling to SM stress) and one massive (X); safety requires the massless combination to dominate SM couplings — a parametric check to log". It logged graviton-mass bounds from gravitational-wave observations ("m_g ≲ 10⁻²³ eV territory") as a check on the mixing angle.

Calc note #8 §3 replaced that framing [D + T]. In the program's vacuum the two frames are aligned (𝕏 = 1), and the two effective Planck masses are equal, "forced by the same symmetry". The massless graviton is "the reciprocity-**even** combination (e + f)" and X "is reciprocity-**odd** (e − f)" (on the parities under #11 §6's Z → −Z⁻¹, see flag 39 in `review/wiki-build-flags.md`). Standard Model matter, coupled to g, "sees both eigenstates with comparable strength; safety is by **range**, not decoupling", and graviton-mass bounds from gravitational waves "apply to the even eigenstate, which is exactly massless". The Fierz–Pauli mass at the aligned point is "m_FP² ∝ β₁ + 2β₂ + β₃", which the palindrome reduces to 2(β₁+β₂); neither β₀ nor β₄ enters it. See [spectrum, parameters and reciprocity parity](/wiki/gravity/momentum-graviton/spectrum-and-parity), [safety by range](/wiki/gravity/momentum-graviton/fifth-force-safety) and [row 6: the exactly massless graviton](/wiki/predictions/massless-graviton).

## The interchange-symmetric choice in the literature [T]

The branch βₙ = β₄₋ₙ was not new to the literature. The checkpoint's literature position (#11 §7.4):

- **[Partially massless gravity](/wiki/gravity/spin-2-fields/partially-massless-gravity).** "The interchange-symmetric parameter choice appears in the partially-massless (PM) bimetric literature: the PM point β₀ = 3α⁻²β₂, β₁ = β₃ = 0, β₄ = 3α²β₂ makes the potential g↔f symmetric, with proportional de Sitter solutions of undetermined ratio [24S]. At α = 1 the PM point lies **inside** our palindromic branch". Whether reciprocity is the origin of the partially massless symmetry is open [O]. #11 does not define α or c; in the bimetric literature's usual notation α is the ratio of the two metrics' Planck masses and c the constant of proportionality in f = c²g [T]. The PM point "sits at Λ ≠ 0 with c undetermined", while the program's flat-aligned-vacuum identity "selects a *different* point of the same branch (β₁ ≠ 0 generically, β₀ = −4β₁ − 3β₂)".
- **Hossenfelder's exchange-symmetric bimetric theory.** The theme of exchange symmetry cancelling vacuum energy in a two-metric theory has a precedent "in a different mechanism: Hossenfelder's exchange-symmetric bimetric, where twin-sector source terms cancel identically [25S]". The program's identity "is sector-internal (no twin matter required)".

Calc note #8 §1 had described the branch as the "'interchange-symmetric branch' that has floated in the bimetric literature as an ad hoc simplification", which "now has a reason to exist: **its ℤ₂ is Born reciprocity.**" After the literature search, #11 §7.4 downgraded the novelty of the resulting identity to "requires detailed comparison with the PM and exchange-symmetric literature". That comparison is open problem 2 ([Open: the partially-massless comparison (OP2)](/wiki/gravity/palindromic-branch/pm-comparison)).

## Cosmological branches [T]

Expanding-universe solutions of bimetric gravity have known instabilities. The withdrawn manuscript #14 summarizes the literature (§1): "The published analyses of bimetric cosmological branches find gradient or ghost instabilities, but they assume a spin-2 mass of order the present Hubble rate and comparable Planck masses for the two metrics [4]. A heavy spin-2 field has been shown to be linearly stable at late times in the regime where the second metric's Planck mass is much smaller than the first [5]." Since reciprocity "sets the two Planck masses equal", #14 calls the stability of a heavy spin-2 field at equal Planck masses "an open consistency condition". The round-3 audit found #14's reference [4] slightly over-generalized. See [bimetric cosmology and its instabilities](/wiki/gravity/spin-2-fields/bimetric-cosmology) and [Open: stability at equal Planck masses](/wiki/gravity/momentum-graviton/equal-planck-mass-stability). #14 was withdrawn for its abundance arithmetic, not for this summary ([obituary: superheavy conjugate solitons](/wiki/dark-matter/candidates/soliton-candidate/obituary)).

## The program's version: constrained bimetric gravity [D — structural]

The program's geometric sector passed [the tuning test](/wiki/gravity/tuning-test) in frame variables, with the second frame E₀[J] built from the [polarization J](/wiki/symmetry-breaking/order-parameter). Calc note #7 §4 observes that "J carries only the 10 compact moduli of U(d)/O(d) — not a full second metric", so the "second vielbein" E₀[J] "is confined to a compact 10-dimensional moduli space". Its conclusion:

> **Hassan–Rosen bimetric gravity with the second frame constrained to a compact moduli space Λ(d)** — a *predictive truncation* of bimetric theory: fewer free functions, with the light direction of the compact space being τ (the dark-energy field) and the massive spin-2 being X.

After the palindrome, #8 §3 quantifies the truncation: "HR bimetric's five-function freedom collapses to two numbers" (HR being Hassan–Rosen; on "five-function", see flag 8 in `review/wiki-build-flags.md`). The checkpoint's technical abstract places X "in the interchange-symmetric branch of Hassan–Rosen bimetric gravity [10†, 11†] with the second frame confined to Λ(4)" (#11 §1), and the [handoff](/wiki/history/documents/handoff) records the same identification (HANDOFF §2). The notes write Λ(d); #11 writes Λ(4) for the confined second frame (§1, §7). The two agree for four dimensions. #8 §1 calls the sector "The Hinterbichler–Rosen sector for (e, f = E₀[J])", the frame form of the same potential ([the frame tier](/wiki/gravity/tuning-test/frame-tier)). See [constrained bimetric gravity](/wiki/gravity/tuning-test/constrained-bimetric), [the Lagrangian Grassmannian Λ(d)](/wiki/phase-space/modular-field/lagrangian-grassmannian) and [τ: hilltop quintessence on the Maslov circle](/wiki/cosmology/dark-energy/tau-quintessence).

## References

As the documents give them:

- [10]† S. F. Hassan, R. A. Rosen, "Resolving the ghost problem in non-linear massive gravity," Phys. Rev. Lett. 108, 041101 (2012), arXiv:1106.3344 (#11).
- [11]† S. F. Hassan, R. A. Rosen, "Bimetric gravity from ghost-free massive gravity," JHEP 1202, 126 (2012), arXiv:1109.3515 (#11). #14 lists both papers, unmarked, as its [3].
- [12]† K. Hinterbichler, R. A. Rosen, "Interacting spin-2 fields," JHEP 1207, 047 (2012), arXiv:1203.5783 (#11).
- [22][S] A. Schmidt-May, M. von Strauss, "Recent developments in bimetric theory," J. Phys. A 49, 183001 (2016), arXiv:1512.00021 (#11): a review of the theory, which #11 cites for its §7.3 statement on the cosmological-constant problem.
- [24][S] "Partially massless bimetric gravity and its exchange-symmetric parameter point, arXiv:1609.09515" (#11, which gives no authors; see flag 9 in `review/wiki-build-flags.md`).
- [25][S] S. Hossenfelder, "A bi-metric theory with exchange symmetry," Phys. Rev. D 78, 044015 (2008), arXiv:0807.2838 (#11).

Added by the wiki from model memory (†):

- C. J. Isham, A. Salam, J. Strathdee (1971)†: an early theory of two interacting dynamical metrics.

## Used by

- [Why X must be massive](/wiki/gravity/momentum-graviton/forcing-chain) — names the Hassan–Rosen class as the consistent structure for a massive X.
- [The gravitational Higgs mechanism](/wiki/gravity/momentum-graviton/gravitational-higgs) — the βₙ that set M_X are this potential's coefficients.
- [The misalignment potential](/wiki/gravity/tuning-test/misalignment-potential) — the potential must land in the Hassan–Rosen class.
- [The metric tier fails twice](/wiki/gravity/tuning-test/metric-tier-failures) — battery T7 checks that p₄ lies outside the span of the eₙ; #7's derivation places the metric-built potential outside the family.
- [The frame tier: the symplectic vielbein](/wiki/gravity/tuning-test/frame-tier) — the passing potential, in frame form.
- [The verdict: a conditional pass](/wiki/gravity/tuning-test/conditional-pass) — the frame-tier potential lands in the ghost-free family.
- [Constrained bimetric gravity](/wiki/gravity/tuning-test/constrained-bimetric) — the program's truncation of the theory.
- [Open: deriving the wedge sector from S_H (OP1)](/wiki/gravity/tuning-test/wedge-reduction) — the potential to be derived must lie in the Hassan–Rosen class.
- [The palindrome βₙ = β₄₋ₙ](/wiki/gravity/palindromic-branch/palindrome) — reciprocity acting through the exchange identity.
- [The vacuum-energy identity V(1) = 2T](/wiki/gravity/palindromic-branch/vacuum-energy-identity) — the potential evaluated at the aligned point.
- [Open: the partially-massless comparison (OP2)](/wiki/gravity/palindromic-branch/pm-comparison) — the interchange-symmetric literature.
- [Spectrum, parameters and reciprocity parity](/wiki/gravity/momentum-graviton/spectrum-and-parity) — the five βₙ reduced to two; the even and odd eigenstates.
- [Open: τ–Stückelberg mixing (OP6)](/wiki/gravity/momentum-graviton/tau-stuckelberg-mixing) — the mixing would arise through this potential.
- [Safety by range: X and ordinary matter](/wiki/gravity/momentum-graviton/fifth-force-safety) — matter coupled to g feels both eigenstates.
- [Open: stability at equal Planck masses](/wiki/gravity/momentum-graviton/equal-planck-mass-stability) — the cosmological branches at equal Planck masses.
- [Row 6: the exactly massless graviton](/wiki/predictions/massless-graviton) — the even eigenstate.
- [Born's answer: momentum space gravitates](/wiki/gravity/momentum-graviton/borns-answer) — X's dynamics as the reciprocity-symmetric branch.
- [The modular field Z = X + iY](/wiki/phase-space/modular-field/modular-field-z) — X's dynamics are this theory with the second frame confined.
- [Open: Lorentzian dressing of the Euclidean skeleton (OP3)](/wiki/phase-space/born-geometry/lorentzian-dressing) — the dressing rests on the same Fierz–Pauli and Hassan–Rosen structure as the chain (#6 §3).
- [The X-condensate candidate](/wiki/dark-matter/candidates/x-condensate) — the candidate field is governed by this theory on the palindromic branch.

## Sources

- `papers/broken-born-checkpoint-v2.md` §1, §7, §7.1, §7.3, §7.4, §7.5, refs [10]–[12], [22], [24], [25] — the abstract's identification; the consistent structure for massive spin-2; the palindrome's tags; the interchange-symmetric choice in the literature; the spectrum; the citations, marked † or [S].
- `review/round3/referee/audit-notes.md` Step 1 — the audit of #14's reference [3], the same two Hassan–Rosen papers, and of its reference [4].
- `notes/debt1a-iv-beta-coefficients.md` §1, §3 — the potential, the exchange identity, reciprocity as frame exchange and the palindrome; the parameter count and the even and odd eigenstates.
- `notes/debt1a-iii-tuning-test.md` §2, §4 — linearity in the eₙ; the standard bimetric facts; the constrained picture.
- `notes/knot-dark-matter-standalone.md` §1, ref [3] — the instabilities of bimetric cosmological branches and the equal-Planck-mass condition; #14's citation of the two papers (manuscript withdrawn for unrelated arithmetic).
- `HANDOFF.md` §2 — the geometric sector as interchange-symmetric Hassan–Rosen bimetric gravity with the second frame confined to Λ(4).
- `review/wiki-build-flags.md` items 8, 9 — item 8: "five-function" for five constant coefficients; item 9: reference [24][S], with no authors and a title that may be descriptive; awaiting Paul's ruling.
