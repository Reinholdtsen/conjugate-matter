---
title: "The multi-graviton no-go theorem"
weight: 30
status: established
description: "Boulanger–Damour–Gualtieri–Henneaux: several massless gravitons cannot interact with one another consistently — the theorem that excludes a massless X."
provenance: [T]
sources:
  - "papers/broken-born-checkpoint-v2.md §1"
  - "papers/broken-born-checkpoint-v2.md §7"
  - "papers/broken-born-checkpoint-v2.md §7.1"
  - "papers/broken-born-checkpoint-v2.md ref [8]"
  - "review/round3/referee/audit-notes.md Step 1"
  - "notes/x-classification.md §2"
  - "notes/tuning-test.md §5"
  - "notes/beta-coefficients.md §4"
  - "notes/geometric-core.md §C"
  - "notes/broken-born-theory.md 'Addendum (v0.4)'"
  - "notes/broken-born-program-v1.md §5"
  - "notes/knot-dark-matter-standalone.md §1"
  - "notes/knot-dark-matter-standalone.md ref [2]"
  - "HANDOFF.md §2"
  - "popsci/universes-other-half.md 'The second geometry, and why it has never been seen'"
  - "popsci/angle-of-the-mirror.md 'What refused to die'"
  - "review/wiki-build-flags.md item 55"
  - "notes/gate-mechanism.md §2"
---

*The multi-graviton no-go theorem, proved by Boulanger, Damour, Gualtieri and Henneaux, states that several massless spin-2 fields cannot interact with one another consistently. Under its assumptions (local couplings, at most two derivatives, no [ghosts](/wiki/gravity/spin-2-fields/ghosts)) no coupling can mix them. Each massless graviton can be made consistent on its own, as [general relativity](/wiki/gravity/spin-2-fields/general-relativity) is, but a theory in which two of them couple to each other cannot. Massive spin-2 fields fall outside the theorem, which is how [bimetric gravity](/wiki/gravity/spin-2-fields/hassan-rosen-bimetric), with one massless and one massive spin-2 field, avoids it. In the program the theorem closes one route for the [momentum graviton X](/wiki/gravity/momentum-graviton): X has the gauge symmetry of a second massless graviton and must couple to the metric and to [conjugate matter](/wiki/dark-matter/conjugate-matter), so it cannot stay massless. Together with the [signature obstruction](/wiki/gravity/spin-2-fields/signature-obstruction), this leaves a mass as the only consistent option for X.*

**Status:** Established — [T] — a literature result, cited in the [checkpoint](/wiki/history/documents/checkpoint) as [8†], from model memory; the checkpoint's reference list still awaits its source check in [the † literature battery](/wiki/method/literature-battery) (OP10). The same paper, as reference [2] of the withdrawn manuscript [#14](/wiki/dark-matter/candidates/soliton-candidate), was resolved on INSPIRE in the [round-3 audit](/wiki/method/review/round-3/rulings), which read its abstract and found that it supports the program's use, with the caveats "2-derivative, local, ghost-free" (`review/round3/referee/audit-notes.md` Step 1). Nothing here is machine-checked.

## Statement [T]

**The setting.** Take a collection of massless spin-2 fields h⁽ᵃ⁾_μν, labelled by a, on flat spacetime. In the free limit each is a copy of the linearized graviton of [general relativity](/wiki/gravity/spin-2-fields/general-relativity), with the gauge-invariant kinetic term, positive energy, and its own gauge symmetry

```text
δh⁽ᵃ⁾_μν = ∂_μ ξ⁽ᵃ⁾_ν + ∂_ν ξ⁽ᵃ⁾_μ
```

**The question.** Can the fields be made to interact? An interacting theory has to deform the free action and its gauge symmetries together, order by order in the coupling, and keep as many gauge symmetries as the free theory has. If a symmetry were lost, the components it removed would propagate again, and for a symmetric tensor some of those components carry negative energy ([the signature obstruction](/wiki/gravity/spin-2-fields/signature-obstruction)). For a single massless graviton the deformation exists and is essentially unique: the linear gauge symmetry becomes full diffeomorphism invariance, and the theory becomes general relativity ([one massless graviton is general relativity](/wiki/gravity/spin-2-fields/general-relativity#one-massless-graviton-is-general-relativity-t)).

**The answer.** For several gravitons the abstract, as the round-3 audit quotes it, finds "no consistent (ghost-free) coupling, with at most two derivatives ... that can mix the various gravitons". What remains allowed keeps the gravitons apart. The paper's summary, given here from model memory (†), is that the only consistent deformations are sums of separate Einstein–Hilbert actions, one for each graviton, each invariant under its own diffeomorphisms.

**The assumptions.** The audit lists the theorem's caveats as "2-derivative, local, ghost-free". The fields are also massless: the theorem concerns the deformations of a theory of free massless gravitons.

**The method, in outline (from model memory †).** The proof uses the systematic method of consistent deformations of gauge theories. At first order the possible cubic couplings among the gravitons are described by an algebra on the space of graviton labels. Closure of the deformed gauge transformations at second order forces that algebra to be commutative and associative, and positivity of energy then forces it to split into independent pieces, one for each graviton, so no coupling connects two of them.

## What the theorem does not cover [T]

The assumptions mark out what the theorem does not cover:

- **Gravitons that never interact.** Several massless gravitons are consistent if each forms a separate copy of general relativity with no coupling to the others. Such sectors do not see one another.
- **Massive spin-2 fields.** A mass term breaks the gauge symmetry, so a massive spin-2 field has no gauge symmetry to preserve, and the theorem says nothing about it. A massive spin-2 field can interact with a massless graviton provided its potential keeps the [Boulware–Deser ghost](/wiki/gravity/spin-2-fields/fierz-pauli) out. [dRGT massive gravity](/wiki/gravity/spin-2-fields/drgt-massive-gravity) and [Hassan–Rosen bimetric gravity](/wiki/gravity/spin-2-fields/hassan-rosen-bimetric) are such theories. Bimetric gravity has two interacting metrics, but about proportional backgrounds (f a constant multiple of g) only one combination of their fluctuations is a massless spin-2 field; the other is massive.
- **Couplings with more derivatives, nonlocal couplings, or ghosts.** These lie outside the theorem's hypotheses, which is what the audit's caveats record.

The program takes the second exit.

## How the program uses it

### X cannot decouple

The program's second symmetric tensor X = Re Z has local shifts δX_μν = ∂₍μλ_ν₎, a second copy of linearized diffeomorphisms ([dual diffeomorphisms](/wiki/gravity/momentum-graviton/dual-diffeomorphisms)). Calc note [#6](/wiki/history/documents/field-equation-notes) §2 then applies the theorem [T]:

> With the gauge invariance, X is a second **massless** spin-2 — and massless multi-graviton cross-interactions are inconsistent (Boulanger–Damour–Gualtieri–Henneaux). X must couple (to g through the Siegel structure, to χ through the gate), so decoupling is not available.

Both couplings come from the program's own structure:

- **To g through the Siegel structure.** X and the metric g are the real and imaginary parts of one field, the [modular field](/wiki/phase-space/modular-field/modular-field-z) Z = X + iY with Y = g, on [the Siegel domain](/wiki/phase-space/modular-field/siegel-domain). The generalized metric H_Z built from Z contains both, in blocks such as Y + XY⁻¹X and XY⁻¹ (calc note #5 §C), so a geometric action built from H_Z contains couplings between them.
- **To χ through the gate.** The [velocity gate](/wiki/dark-matter/conjugate-matter/velocity-gate) in the self-interaction of conjugate matter χ is produced by X exchange between χ particles ([the gate mechanism](/wiki/dark-matter/conjugate-matter/gate-mechanism)), according to #11 §8 (not derived, according to flag 55 in `review/wiki-build-flags.md`, pending Paul's ruling; [the gate mechanism](/wiki/dark-matter/conjugate-matter/gate-mechanism#exchanging-x-cannot-produce-the-gate)).

The gravitons that the theorem allows are decoupled ones, and X cannot be decoupled, so a massless X is excluded. #6 §2 states this exclusion together with the signature obstruction, which excludes an X without gauge symmetry, and concludes from the pair: "**Therefore X must be massive.**"

### The forcing chain

The checkpoint states the step inside its chain [D + T] (#11 §7.1): "Massless X is excluded by the multi-graviton no-go [8†]; ungauged X by Lorentz signature." Its technical abstract lists the theorem among the structural results that force X's form: "A chain of structural results (a compatibility theorem [T][V]; the multi-graviton no-go [8†]; a signature obstruction; an explicit tuning test [V]) forces X to be a **massive spin-2** field" (#11 §1; [the compatibility theorem](/wiki/phase-space/born-geometry/compatibility-theorem), [the tuning test](/wiki/gravity/tuning-test)). The mass then comes from the [polarization](/wiki/phase-space/reciprocity/lagrangian-polarizations) choice ([why X must be massive](/wiki/gravity/momentum-graviton/forcing-chain); [the gravitational Higgs mechanism](/wiki/gravity/momentum-graviton/gravitational-higgs)).

The same step appears in every document of the chain:

- the [lab notebook](/wiki/history/documents/lab-notebook)'s addendum v0.4: "Massless X is then excluded by the multi-graviton no-go (Boulanger–Damour–Gualtieri–Henneaux), and the ghost-free no-gauge option is excluded by Lorentz signature";
- the superseded program v1 (#9 §5, item 2): "Massless: excluded by the multi-graviton no-go (Boulanger–Damour–Gualtieri–Henneaux) since X must couple";
- the [handoff](/wiki/history/documents/handoff) (HANDOFF §2): "massless excluded (Boulanger–Damour–Gualtieri–Henneaux no-go)";
- calc note #8 §4, the program's answer to Born: X "is a **massive spin-2 field** — massless is forbidden by the multi-graviton no-go, and the mass is generated by the Higgsing of dual diffeomorphisms when the vacuum selects a polarization" ([Born's answer](/wiki/gravity/momentum-graviton/borns-answer)).

Calc note #7 §5 lists the no-go as the first of three structural tests (the multi-graviton no-go, the signature obstruction, the tuning test), at each of which the geometric sector was restricted to "the unique known consistent structure at that junction"; #11 §15 counts four ([the assessment](/wiki/program/assessment)).

### The partner of the graviton

The checkpoint's plain-language passage for §7 states the theorem as "two interacting massless gravities are mathematically inconsistent", and sets it beside the contrast with string theory: in [double field theory](/wiki/phase-space/born-geometry/double-field-theory) the partner of the metric is the antisymmetric [B-field](/wiki/phase-space/born-geometry/kalb-ramond-field#set-against-the-momentum-graviton) (#11 §7.1), while "the symplectic partner of the graviton is another graviton" (#11 §7). Because the partner is a graviton, the theorem applies to it. See [the symplectic partner of the graviton is another graviton](/wiki/gravity/momentum-graviton/symplectic-partner).

### In the withdrawn manuscript and the popular articles

The withdrawn soliton manuscript #14 states the exclusion in its §1: "a massless X coupled to gravity is excluded by the multi-graviton no-go [2]". The round-3 audit checked that reference and found that it supports this statement, with the caveats above. #14 was withdrawn after round 3 for its dark-matter abundance arithmetic, not for this statement ([obituary: superheavy conjugate solitons](/wiki/dark-matter/candidates/soliton-candidate/obituary)).

The [popular articles](/wiki/history/documents/popular-articles) give the same sentence: #10 ("physics has a theorem for that: two interacting massless gravities are mathematically inconsistent") and #12 ("a theorem of field theory, proved in 2000, establishes that two interacting massless gravities are mathematically inconsistent"). The popular articles are not a source for status.

## The citation and its checks

The checkpoint cites the theorem as [8†], from model memory, so #11's own entry has not been checked against the source; that check belongs to the open literature battery. The same paper is reference [2] of #14, with the same journal, volume, page, year and arXiv identifier. The round-3 audit resolved all 23 of #14's references (37 individual items) on INSPIRE "with matching authors / journal / volume / page / year / arXiv id", read the abstract of this one, and marked it as supporting "massless X coupled to gravity is excluded" ([round-3 rulings and citation audit](/wiki/method/review/round-3/rulings)).

The date differs between documents: #12 says the theorem was "proved in 2000", while #11 cites the 2001 journal paper. The arXiv identifier, hep-th/0007220, is the preprint; the two years are the preprint year and the journal year of the same work, not a disagreement of substance ([conflicts between sources](/wiki/history/documents/source-conflicts)).

## References

As the documents give them:

- [8]† N. Boulanger, T. Damour, L. Gualtieri, M. Henneaux, "Inconsistency of interacting, multi-graviton theories," Nucl. Phys. B 597, 127 (2001), hep-th/0007220 (#11). #14 lists the same paper, unmarked, as [2].
- For the massive escape: [9]† de Rham–Gabadadze–Tolley, [10]† and [11]† Hassan–Rosen, [12]† Hinterbichler–Rosen (#11); see [dRGT massive gravity](/wiki/gravity/spin-2-fields/drgt-massive-gravity), [Hassan–Rosen bimetric gravity](/wiki/gravity/spin-2-fields/hassan-rosen-bimetric) and [the vielbein formulation](/wiki/gravity/spin-2-fields/vielbein-formulation).

## Used by

- [Why X must be massive](/wiki/gravity/momentum-graviton/forcing-chain) — excludes the massless option.
- [Dual diffeomorphisms: a second graviton](/wiki/gravity/momentum-graviton/dual-diffeomorphisms) — the gauge symmetry that would make X a second massless graviton.
- [The symplectic partner of the graviton is another graviton](/wiki/gravity/momentum-graviton/symplectic-partner) — the partner is a graviton, so the theorem applies.
- [Born's answer: momentum space gravitates](/wiki/gravity/momentum-graviton/borns-answer) — the massless option excluded in the program's answer.
- [The X-condensate candidate](/wiki/dark-matter/candidates/x-condensate) — the candidate is a massive X, the massless option being excluded.
- [Row 6: the exactly massless graviton](/wiki/predictions/massless-graviton) — the chain behind the row's massless and massive eigenstates includes the no-go.
- [The modular field Z = X + iY](/wiki/phase-space/modular-field/modular-field-z) — the coupling of X to g that rules out decoupling.
- [Open: field content of the broken vacuum](/wiki/phase-space/modular-field/field-content) — the no-go settles X's place in the field list as a massive field.
- [Open: Lorentzian dressing of the Euclidean skeleton (OP3)](/wiki/phase-space/born-geometry/lorentzian-dressing) — the no-go is a step of the chain whose Lorentzian extension is open.
- [Original P2: both structures rigid (superseded)](/wiki/program/postulates/original-p2) — the v0.4 reversal of P2's claim that it "kills the would-be second graviton" (#1 §1).
- [Founding suppositions and their fates](/wiki/program/founding-suppositions) — supposition 10, momentum space has its own gravity.

## Sources

- `papers/broken-born-checkpoint-v2.md` §1, §7, §7.1, ref [8] — the technical abstract's chain; the plain-language statement; the theorem's place in the chain; the citation, marked †.
- `review/round3/referee/audit-notes.md` Step 1 — the INSPIRE resolution of #14's references, the abstract of #14's reference [2] and its caveats.
- `notes/x-classification.md` §2 — the exclusion, and why X must couple, so that decoupling is unavailable.
- `notes/geometric-core.md` §C — the generalized metric H_Z, whose blocks mix X and Y.
- `notes/tuning-test.md` §5 — the no-go as the first of three structural tests.
- `notes/beta-coefficients.md` §4 — the exclusion in the answer to Born.
- `notes/broken-born-theory.md` 'Addendum (v0.4)' — the exclusion as first recorded in the notebook.
- `notes/broken-born-program-v1.md` §5 — "since X must couple" (superseded as reference).
- `notes/knot-dark-matter-standalone.md` §1, ref [2] — #14's statement of the exclusion and its citation (the manuscript was withdrawn for its abundance arithmetic, not for this statement).
- `HANDOFF.md` §2 — the exclusion in the handoff's scientific state.
- `popsci/angle-of-the-mirror.md` 'What refused to die'; `popsci/universes-other-half.md` 'The second geometry, and why it has never been seen' — the popular statements and the date "proved in 2000".
- `notes/gate-mechanism.md` §2 and `review/wiki-build-flags.md` item 55 — exchanging #11 §7's X cannot produce the gate; awaiting Paul's ruling
