---
title: "The Kalb–Ramond B-field"
weight: 25
status: established
description: "The antisymmetric 2-form gauge field of closed string theory: gauge symmetry δB = dλ, a 3-form field strength, strings as its charges, mixed with the metric by T-duality and paired with it in double field theory's generalized metric. The program uses it three ways: frozen out once ω is rigid as well as η (corollary 2), set against the symmetric momentum graviton, and cited as a precedent for healthy doubled kinetic terms."
provenance: [T]
sources:
  - "papers/broken-born-checkpoint-v2.md §5"
  - "papers/broken-born-checkpoint-v2.md §7.1"
  - "papers/broken-born-checkpoint-v2.md ref [26]"
  - "review/round3/referee/audit-notes.md Step 1"
  - "review/round3/referee/audit-notes.md Step 3"
  - "review/round3/referee/step3.py family (c)"
  - "review/round3/referee/step3.out family (c)"
  - "notes/debt1a-geometric-core.md §A"
  - "notes/debt1a-geometric-core.md §C"
  - "notes/debt1a-geometric-core.md §D"
  - "notes/debt1a-ii-X-classification.md §1"
  - "notes/debt1a-ii-X-classification.md §2"
  - "notes/debt3b-wave-island.md 'Next'"
  - "notes/debt3c-ufd-endpoint.md 'Next: Debt 1, Chunk 1a'"
  - "notes/broken-born-theory.md 'Addendum (v0.4)'"
  - "notes/broken-born-program-v1.md §3"
  - "notes/broken-born-program-v1.md §5"
  - "review/wiki-build-flags.md item 15"
---

*The Kalb–Ramond B-field is an antisymmetric tensor field, B_μν = −B_νμ, that does for a string what the electromagnetic potential does for a charged particle: a particle's quantum phase changes by the potential summed along its path, and a string's by the B-field summed over the surface the string sweeps out. Like the electromagnetic potential it is a gauge field, so it can be changed by a gauge transformation without changing anything measurable, and what is measurable locally is its field strength, built from its derivatives. It is one of the massless fields of closed string theory, with the metric and a scalar, the dilaton. T-duality, the symmetry of strings on a circle that exchanges momentum around the circle with winding around it, turns parts of the metric into parts of the B-field, and for that reason [double field theory](/wiki/phase-space/born-geometry/double-field-theory) puts the two in one matrix, the generalized metric, which preserves a [neutral metric η](/wiki/phase-space/born-geometry/born-structures). The program uses the B-field as established physics in three ways. Holding the [symplectic form](/wiki/phase-space/reciprocity/symplectic-form) ω rigid as well as η removes it ([corollary 2](/wiki/phase-space/born-geometry/compatibility-corollaries#corollary-2-no-kalbramond-analog) of the compatibility theorem). It is the antisymmetric counterpart of the program's own partner of the metric, the symmetric [momentum graviton X](/wiki/gravity/momentum-graviton): X is a second graviton, and the B-field is not. And its healthy propagation alongside the metric and the dilaton is the program's precedent for a doubled geometry whose kinetic terms have no [ghosts](/wiki/gravity/spin-2-fields/ghosts), modes that carry negative energy.*

**Status:** Established — [T] — textbook string theory and double field theory, written here from general knowledge, with the works it names marked † (Kalb and Ramond 1974 †; Buscher 1987 †) and the double-field-theory papers as [double field theory](/wiki/phase-space/born-geometry/double-field-theory#references) lists them. The program's statements that involve the B-field are corollary 2 of the compatibility theorem, "[D — rigorous]" in calc note [#5](/wiki/history/documents/debt-1-notes) §A, which [checkpoint #11](/wiki/history/documents/checkpoint) §5 credits to Freidel, Leigh and Minic [26S]; and calc note #6's contrast with the momentum graviton, [D + T] (#6 §2; #11 §7.1). No `verify/` script checks either. The [round-3](/wiki/method/review/round-3) audit sampled generalized metrics with a B-field and found each compatible with η and not with ω, in scripts kept outside [the gate](/wiki/method/verification/the-gate).

## What the field is [T]

### A gauge field one rank above electromagnetism

The electromagnetic potential A_μ has one index. Its gauge symmetry adds a gradient, δA = dφ with φ any function, and the field strength F = dA, which holds the electric and magnetic fields, does not change under it. The B-field has two indices and is antisymmetric, so it is a 2-form: where A assigns a number to each small step along a path, B assigns one to each small oriented patch of surface. Its gauge symmetry adds the antisymmetrized derivative of a field λ_μ with one index, a 1-form, and its field strength is the 3-form dB [T]:

```text
δB_μν = ∂_μλ_ν − ∂_νλ_μ            in form notation:  δB = dλ

(dB)_μνρ = ∂_μB_νρ + ∂_νB_ρμ + ∂_ρB_μν
```

The field strength does not change under the gauge symmetry, because applying d twice gives zero, d(dλ) = 0, in the same way that F = dA does not change because d(dφ) = 0 [T]. The gauge parameter carries a redundancy of its own: λ and λ + dφ give the same δB. The string literature writes the field strength as H; in this wiki H is the generalized metric, so the field strength is written dB ([letters with several meanings](/wiki/notation#letters-with-several-meanings)).

| | Electromagnetism | The B-field |
| --- | --- | --- |
| Potential | A_μ, a 1-form | B_μν, a 2-form |
| Gauge symmetry | δA = dφ, φ a function | δB = dλ, λ a 1-form |
| Field strength | F = dA, a 2-form | dB, a 3-form |
| What carries its charge | a point particle | a string |
| The coupling is summed over | the particle's path | the surface the string sweeps out |

### The field that strings carry

A charged particle's quantum phase changes along its path by its charge times the potential summed along the path. Two paths that enclose a region of magnetic flux end with a phase difference set by the flux, even where the field strength on the paths themselves is zero: the Aharonov–Bohm effect [T]. A string is extended in one dimension, and as it moves it sweeps out a surface, its worldsheet. The B-field enters the string's phase in the same way one dimension up, summed over the worldsheet, so a string is to the B-field what a charged particle is to the electromagnetic potential [T]. Kalb and Ramond introduced the antisymmetric tensor potential in this role, as the field through which strings act on one another (1974 †), and the field carries their names.

When the closed string is quantized, its massless states include a symmetric tensor, the graviton; an antisymmetric tensor, the B-field; and a scalar, the dilaton, whose value sets the strength with which strings interact [T]. In the type II superstring theories these three make up the Neveu–Schwarz–Neveu–Schwarz sector, and the B-field is often called the Neveu–Schwarz B-field. At low energies they are described by a field theory whose action is built from the curvature of the metric, the square of the field strength dB and the derivatives of the dilaton, with an overall factor that depends on the dilaton [T]. Double field theory rewrites that action on a doubled space ([the doubled space](/wiki/phase-space/born-geometry/double-field-theory#the-doubled-space-t)).

### Why it is not a second graviton

The B-field and the fluctuation of the metric are both two-index fields, and their symmetry decides what kind of field each is. A symmetric two-index field whose gauge symmetry is the symmetrized derivative of a vector, δh_μν = ∂₍μξ_ν₎, is a massless spin-2 field, a graviton ([linearized diffeomorphisms](/wiki/gravity/momentum-graviton/dual-diffeomorphisms#background-linearized-diffeomorphisms-and-the-graviton-t)). The B-field is antisymmetric, so it has no spin-2 component, and its gauge symmetry δB = dλ is not a copy of the coordinate changes of [general relativity](/wiki/gravity/spin-2-fields/general-relativity) [T]. It couples to a conserved current carried by strings, not to energy and momentum as the metric does. The [multi-graviton no-go theorem](/wiki/gravity/spin-2-fields/multi-graviton-no-go), which rules out two interacting massless spin-2 fields, does not apply to it.

Its kinetic term is the square of its field strength dB, as Maxwell's is the square of F, and the gauge symmetry removes the components that would otherwise propagate with negative energy, the [ghosts](/wiki/gravity/spin-2-fields/ghosts) [T]. In four spacetime dimensions a massless 2-form field is equivalent to a massless scalar field: its field strength can be rewritten as the dual of the gradient of a scalar [T].

Calc note [#6](/wiki/history/documents/debt-1-notes) §2 summarizes the field as "a 2-form gauge theory — spin-wise harmless".

## The B-field and T-duality [T]

A closed string on a circle carries two conserved charges: its momentum around the circle and the number of times it winds around it ([the doubled space](/wiki/phase-space/born-geometry/double-field-theory#the-doubled-space-t)). In the dimensions that remain, each is the charge of a gauge field. The metric's components with one index along the circle form a gauge field whose charge is momentum, as in Kaluza and Klein's unification of gravity and electromagnetism. The B-field's components with one index along the circle form a gauge field whose charge is winding, because a wound string's worldsheet extends along the circle and picks up those components [T].

T-duality relates a string on a circle to a string on a circle of inverse radius in string units, and it exchanges momentum with winding. It exchanges the two gauge fields with them: the metric's components with one index on the circle become, divided by the circle's own metric component, the B-field's, and the reverse (Buscher 1987 †). The metric and the B-field are therefore not separately invariant under T-duality, and a formulation in which T-duality is a manifest symmetry has to combine them in one object. Double field theory's generalized metric is that object.

## In double field theory's generalized metric [T]

The generalized metric H is a symmetric 2d × 2d matrix on the doubled space that preserves the neutral metric η, the pairing of each coordinate with its dual ([the generalized metric](/wiki/phase-space/born-geometry/double-field-theory#the-generalized-metric-t)). In the program's block basis, the round-3 referee's script writes it in terms of g and B (`review/round3/referee/step3.py`, family (c), B antisymmetric):

```text
H = [[ g − B g⁻¹ B ,  B g⁻¹ ],
     [ −g⁻¹ B      ,  g⁻¹   ]]
```

At B = 0 it is diag(g, g⁻¹). The B-field enters through a shear of the doubled space [T]:

```text
H = Lᵀ · diag(g, g⁻¹) · L,        L = [[ 1  , 0 ],
                                       [ −B , 1 ]]
```

L preserves η because B is antisymmetric, so H preserves η whenever diag(g, g⁻¹) does. A shear by a symmetric block would preserve the symplectic form ω instead; the short computation is on [the symplectic partner of the graviton](/wiki/gravity/momentum-graviton/symplectic-partner#why-the-partners-symmetry-is-opposite-to-the-pairings-t). Since L is invertible, H is positive definite exactly when g is [T], and the round-3 script asserts positivity for every matrix of this family it samples.

Three standard properties [T]:

- **Constant shifts are O(d, d) transformations.** Shifting B by a constant antisymmetric matrix b multiplies L by a shear of the same form, L_b = [[1, 0], [−b, 1]], so it acts on the generalized metric as H → L_bᵀ H L_b, an element of O(d, d), the group that preserves η. On a torus, the shifts by antisymmetric integer matrices, in string units, are among the T-duality symmetries.
- **Gauge transformations are dual changes of coordinates.** The gauge parameters of double field theory form one doubled vector. Its components along the ordinary coordinates generate changes of coordinates, and its components along the dual coordinates, λ_μ, generate the B-field's gauge transformations δB = dλ; together they are the generalized diffeomorphisms (Hull and Zwiebach; Hohm, Hull and Zwiebach). A constant shift of B is the special case of a λ that grows linearly with position, whose dλ is constant.
- **On a section the ordinary fields return.** With fields independent of the dual coordinates, the standard solution of [the section condition](/wiki/phase-space/born-geometry/double-field-theory#the-section-condition-t), double field theory reduces to the low-energy action of the metric, the B-field and the dilaton.

## Frozen out when both pairings are rigid

[Born geometry](/wiki/phase-space/born-geometry/born-structures) asks H to be compatible with the symplectic form ω as well as with η. Generalized metrics with a B-field satisfy the η condition (η⁻¹H)² = 1. [The compatibility theorem](/wiki/phase-space/born-geometry/compatibility-theorem) adds the ω condition (ω⁻¹H)² = −1 and finds that the positive H satisfying both are exactly H = diag(g, g⁻¹): the B-field must vanish. Calc note #5 §A draws this as the second of three corollaries, under the heading "[D — rigorous]":

> **No Kalb–Ramond analog.** The off-diagonal block — DFT's B-field — is frozen out by the extra symplectic compatibility. Born geometry with both structures rigid is *stiffer* than DFT.

DFT there is double field theory. "Stiffer" means that the generalized metric has fewer free components: double field theory's carries g and B, and with ω and η both rigid only g remains ([the corollaries](/wiki/phase-space/born-geometry/compatibility-corollaries#corollary-2-no-kalbramond-analog)).

#11 §5 lists "no Kalb–Ramond analog" among the theorem's corollaries and, since version 2.1, credits the theorem to [Freidel, Leigh and Minic](/wiki/phase-space/reciprocity/broken-born-duality): "writing the η-compatible H in terms of (G, B), H is related to ω through a complex structure exactly when B vanishes [26S, §2.1]." There G is the metric and B the Kalb–Ramond field. The round-3 referee located the passage in their metastring paper, arXiv:1502.08005, p. 11, and quoted it (audit notes, Step 1):

```text
"If, in addition, we assume that B vanishes we have that I is a complex
structure and that JK = -KJ. Phase space geometries that have I,J,K
satisfying these conditions were referred to as Born geometries"
```

In the quoted passage, the conditions that define a Born geometry are the ones that hold when B vanishes. The referee summarizes the theorem as "B-field vanishes <=> I = H^-1 omega compatible" (audit notes, Step 3), writing the complex structure as H⁻¹ω where #11 writes I = ω⁻¹H; this wiki follows #11 ([conflicts between sources](/wiki/history/documents/source-conflicts#tags-attribution-and-what-the-checks-cover)).

Round 3 checked the exclusion numerically with its own code: 2000 random generalized metrics with a B-field at each of d = 3 and d = 4, built as above with g positive definite and B antisymmetric (`review/round3/referee/step3.py`, family (c)). Among other lines, the script prints, in `review/round3/referee/step3.out`:

```text
===== d = 3 (numerical, 2000 trials per family) =====
(c) eta-only family (B-field): eta residual max 4.97e-14; omega residual min 0.282
===== d = 4 (numerical, 2000 trials per family) =====
(c) eta-only family (B-field): eta residual max 7.30e-14; omega residual min 1.483
```

The residuals are the norms of (η⁻¹H)² − 1 and (ω⁻¹H)² + 1. Every sampled metric with a B-field satisfies the η condition to rounding error and misses the ω condition by at least the printed margin. The audit notes summarize the family as "eta residual <= 7e-14 but omega residual >= 0.28 (d=3), 1.48 (d=4)" (Step 3). The check confirms the linear algebra on samples; it is not part of the gate ([numerical families at d = 3 and d = 4](/wiki/phase-space/born-geometry/compatibility-theorem#numerical-families-at-d--3-and-d--4)).

Under the original postulate P2, which held ω and η both rigid, the generalized metric is therefore diag(g, g⁻¹), with no partner for the metric at all ([original P2](/wiki/program/postulates/original-p2); [the nontriviality theorem](/wiki/program/postulates/nontriviality-theorem)). Under [P2′](/wiki/program/postulates/p2-prime) only ω is rigid. The positive metrics compatible with ω form [the Siegel domain](/wiki/phase-space/modular-field/siegel-domain), and their off-diagonal block is XY⁻¹, built from the symmetric field X (#5 §C; [the modular field Z = X + iY](/wiki/phase-space/modular-field/modular-field-z)). The program's generalized metric then has a partner for the metric again, but a symmetric one.

## Set against the momentum graviton

Calc note #6 traces what the symmetric partner implies and sets it against the B-field. The rigid symplectic group contains the constant shifts Z → Z + B, with B a constant symmetric matrix, not the Kalb–Ramond field, which shift X and leave the metric alone (#6 §1; [shift symmetry](/wiki/gravity/momentum-graviton/shift-symmetry)). Their local version acts on X as δX_μν = ∂₍μλ_ν₎, a second copy of the gauge symmetry of the graviton ([dual diffeomorphisms](/wiki/gravity/momentum-graviton/dual-diffeomorphisms)). #6 §2 then writes:

> (Contrast DFT: there the doubled partner is the antisymmetric B-field, δB = dλ, a 2-form gauge theory — spin-wise harmless. The symmetry type of the rigid structure — η antisymmetric-pairing vs ω — dictates the symmetry type of the partner field. **This is the structural reason string theory's η-doubling exists and naive ω-doubling is hard: the symplectic partner of the graviton is another graviton.**)

The phrase "η antisymmetric-pairing vs ω" reads as calling η antisymmetric, although η is a symmetric pairing; it is quoted as #6 writes it (flag 15 in `review/wiki-build-flags.md`). Checkpoint #11 §7.1 restates the point without the phrase: X is "a second linearized-diff gauge field, because X is *symmetric* (contrast DFT's antisymmetric B-field: the symmetry type of the rigid pairing dictates the partner's spin)".

| | Double field theory [T] | The program under P2′ |
| --- | --- | --- |
| Fixed pairing | η, symmetric | ω, antisymmetric |
| The metric's partner | the B-field, antisymmetric | X = Re Z, symmetric |
| Its local transformation | δB = dλ | δX_μν = ∂₍μλ_ν₎ |
| What it is | a 2-form gauge field, not spin 2 | a second graviton-like gauge field |

With this gauge symmetry intact X would be a second massless graviton, so the multi-graviton no-go theorem applies to it, and X must become massive ([why X must be massive](/wiki/gravity/momentum-graviton/forcing-chain)). The B-field, being antisymmetric, meets no such obstruction. The argument in full, with the algebra that ties the partner's symmetry to the pairing's, is on [the symplectic partner of the graviton is another graviton](/wiki/gravity/momentum-graviton/symplectic-partner). The wiki's page on #11 §11.3's conjecture of one modular structure for both polarizations sets the contrast beside its comparison with string theory's dualities ([Open: one modular structure for both polarizations (OP8)](/wiki/electric-magnetic-duality/unified-modular-structure)).

## A precedent for healthy doubled kinetic terms

Calc note #5 §D lists the field content of the broken vacuum and two signs that its kinetic terms can be healthy. The second: "the DFT precedent (graviton + B-field + dilaton, ghost-free) shows doubled-geometry kinetic operators can be healthy [T]". The precedent is the massless sector of double field theory, in which the metric, the B-field and the dilaton propagate without ghosts. The question it is cited for is open ([Open: field content of the broken vacuum](/wiki/phase-space/modular-field/field-content#signs-of-health)).

#5 wrote this before #6 classified X. In this wiki's reading, the precedent concerns an antisymmetric partner; #6 then found the program's partner to be symmetric, a second graviton, whose health became the question of [the tuning test](/wiki/gravity/tuning-test).

Earlier, at the close of Debt 3, the next step was to linearize the lab notebook's geometric action "leaning on the known linearized-DFT spectrum" (#3 'Next'), which #4 tags "[T: graviton + two-form + dilaton]" ('Next: Debt 1, Chunk 1a'). The Debt-1 notes did not follow that plan ([the route that was planned, and the one taken](/wiki/gravity/tuning-test/geometric-action#the-route-that-was-planned-and-the-one-taken)).

## Three meanings of the letter B

The documents use B for three different things:

- **The Kalb–Ramond field** of this page: "DFT's B-field" (#5 §A), "graviton + B-field + dilaton" (#5 §D), "the antisymmetric B-field, δB = dλ" (#6 §2), "(G, B)" and "exactly when B vanishes" (#11 §5), "DFT's antisymmetric B-field" (#11 §7.1).
- **A block of H in the compatibility proof.** #5 §A writes H in blocks [[A, C], [Cᵀ, B]], and #11 §5's proof uses the same blocks: "the diagonal blocks give B = A⁻¹". This B is symmetric: it is the momentum-space block of H. #11 §5 uses this B and the Kalb–Ramond B in the same paragraph.
- **The shift Z → Z + B**, with B a constant symmetric matrix (#6 §1; #11 §7.1). Its local version is X's gauge transformation, the counterpart of the B-field's δB = dλ in #6 §2.

The [notation page](/wiki/notation#letters-with-several-meanings) lists the collision.

## Scope and what is open

- **The field itself.** The B-field is literature, and no program document derives anything new about it.
- **Positive metrics.** The compatibility theorem and its corollary 2 are proven for positive-definite H, the Euclidean case, though #11 §5 records the round-3 finding that "the positivity step is not needed for C = 0", the vanishing of the block that carries the B-field ([positivity is not needed for C = 0](/wiki/phase-space/born-geometry/compatibility-theorem#positivity-is-not-needed-for-c--0)). Their extension to spacetime signature is open item 3 of #11 §14 ([Open: Lorentzian dressing of the Euclidean skeleton (OP3)](/wiki/phase-space/born-geometry/lorentzian-dressing)).
- **Pointwise linear algebra.** The exclusion concerns one tangent space at a time. The round-3 referee: "It is a pointwise linear-algebra fact; it does not by itself establish any physics (the identification of a dynamical H, a rigid eta, and a second spin-2 field X is assumed, not derived)" (audit notes, Step 3).
- **Structural, not computed.** The contrast with X is an argument from symmetry type. No document writes an action for X, and no script checks the argument ([scope and caveats](/wiki/gravity/momentum-graviton/symplectic-partner#scope-and-caveats)).
- **A precedent for an open question.** The healthy massless sector of double field theory is cited for the field content of the broken vacuum, which is open.

## Where the documents use it

In order of writing:

- **Calc notes #3 and #4** ('Next'; 'Next: Debt 1, Chunk 1a'): the planned import of "the known linearized-DFT spectrum", "[T: graviton + two-form + dilaton]".
- **Calc note #5** §A: corollary 2, "No Kalb–Ramond analog"; §D: the precedent, "graviton + B-field + dilaton, ghost-free".
- **Calc note #6** §1: the symmetric shift Z → Z + B; §2: the B-field as "a 2-form gauge theory — spin-wise harmless", set against X.
- **The [lab notebook](/wiki/history/documents/lab-notebook)**, v0.4 addendum: X's local gauge structure makes it "a *second graviton* — which is the structural reason η-doubling (string theory's B-field) is easy and ω-doubling is hard".
- **The v1 paper #9**, §3: "no Kalb–Ramond analog"; §5 item 2: "Contrast DFT, whose partner is the antisymmetric B-field — a 2-form, spin-harmless".
- **The round-3 audit**, Step 1: the passage of Freidel, Leigh and Minic on vanishing B; Step 3: family (c), the generalized metrics with a B-field.
- **Checkpoint #11**, §5: "no Kalb–Ramond analog" and, since v2.1, the attribution to Freidel, Leigh and Minic in terms of (G, B); §7.1: the contrast with "DFT's antisymmetric B-field".

## References

- M. Kalb, P. Ramond, "Classical direct interstring action," Phys. Rev. D 9, 2273 (1974) †: the antisymmetric tensor potential coupled to strings. Added by the wiki; no document cites it.
- T. H. Buscher, "A symmetry of the background equations of sigma models," Phys. Lett. B 194, 59 (1987) †: T-duality of a string background with metric and B-field. Added by the wiki.
- C. Hull, B. Zwiebach, "Double field theory," JHEP 09 (2009) 099, arXiv:0904.4664; O. Hohm, C. Hull, B. Zwiebach, "Background independent action for double field theory," JHEP 07 (2010) 016, arXiv:1003.5027: the toy-model note's ref. [11], as [double field theory](/wiki/phase-space/born-geometry/double-field-theory#references) lists it.
- L. Freidel, R. G. Leigh, D. Minic, "Metastring theory and modular space-time," JHEP 06 (2015) 006, arXiv:1502.08005: #11 ref. [26][S].

## Used by

- [Corollaries: unimodularity, no B-field, slaved momentum metric](/wiki/phase-space/born-geometry/compatibility-corollaries#corollary-2-no-kalbramond-analog) — corollary 2: with ω rigid as well as η, the B-field is frozen out.
- [The compatibility theorem](/wiki/phase-space/born-geometry/compatibility-theorem) — the η-only family with a B-field, and Freidel, Leigh and Minic's "exactly when B vanishes".
- [Original P2: both structures rigid (superseded)](/wiki/program/postulates/original-p2) and [the nontriviality theorem](/wiki/program/postulates/nontriviality-theorem) — corollary 2 among the consequences of holding both structures rigid.
- [P1: the phase-space arena](/wiki/program/postulates/p1-arena) — the name "generalized metric", from double field theory, where it combines the metric with the B-field.
- [The symplectic partner of the graviton is another graviton](/wiki/gravity/momentum-graviton/symplectic-partner) — the B-field as the partner that η-doubling gives the metric.
- [Dual diffeomorphisms: a second graviton](/wiki/gravity/momentum-graviton/dual-diffeomorphisms) — X's δX_μν = ∂₍μλ_ν₎ set against δB = dλ.
- [Why X must be massive](/wiki/gravity/momentum-graviton/forcing-chain) — step (ii) of #11 §7.1 contrasts X with the antisymmetric B-field.
- [Open: field content of the broken vacuum](/wiki/phase-space/modular-field/field-content#signs-of-health) — the healthy precedent.
- [Open: one modular structure for both polarizations (OP8)](/wiki/electric-magnetic-duality/unified-modular-structure) — the symmetric X set against string theory's antisymmetric B-field.

## Sources

- `papers/broken-born-checkpoint-v2.md` §5 — "no Kalb–Ramond analog" among the corollaries; Freidel, Leigh and Minic's statement in terms of (G, B); the proof's block B; the positivity note; §7.1 — X against "DFT's antisymmetric B-field", and the symmetric B of Z → Z + B; ref. [26] — the metastring paper.
- `review/round3/referee/audit-notes.md` Step 1 — the passage on p. 11 of arXiv:1502.08005; Step 3 — the B-field family's residuals, "B-field vanishes <=> I = H^-1 omega compatible", "a pointwise linear-algebra fact".
- `review/round3/referee/step3.py` family (c) and `review/round3/referee/step3.out` — the generalized metric with a B-field as the script builds it, the positivity assertion, and the printed residuals.
- `notes/debt1a-geometric-core.md` §A — corollary 2, "[D — rigorous]", and the proof's blocks; §C — H_Z and its off-diagonal block XY⁻¹; §D — the precedent "graviton + B-field + dilaton, ghost-free".
- `notes/debt1a-ii-X-classification.md` §1 — the symmetric B of Z → Z + B; §2 — the contrast, "a 2-form gauge theory — spin-wise harmless".
- `notes/debt3b-wave-island.md` 'Next' and `notes/debt3c-ufd-endpoint.md` 'Next: Debt 1, Chunk 1a' — the planned use of the linearized double-field-theory spectrum, "[T: graviton + two-form + dilaton]".
- `notes/broken-born-theory.md` 'Addendum (v0.4)' — "η-doubling (string theory's B-field) is easy and ω-doubling is hard".
- `notes/broken-born-program-v1.md` §3, §5 — the corollary and the contrast in the v1 paper.
- `review/wiki-build-flags.md` item 15 — #6 §2's "η antisymmetric-pairing vs ω", which reads as calling η antisymmetric.
