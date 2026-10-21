---
title: "Why X must be massive"
weight: 40
status: alive
description: "Shift symmetry, dual diffeomorphisms, the multi-graviton no-go and the signature obstruction leave one exit — mass; and the three-way healthy/auxiliary/ghost classification this chain resolved."
provenance: [D, T]
sources:
  - "papers/broken-born-checkpoint-v2.md §7.1"
  - "notes/debt1a-ii-X-classification.md §1–§3"
  - "notes/debt1a-ii-X-classification.md §5"
  - "notes/debt1a-geometric-core.md §D"
  - "notes/debt1a-geometric-core.md §C"
  - "notes/debt1a-geometric-core.md §E"
  - "notes/debt1a-geometric-core.md §F"
  - "notes/debt1a-iii-tuning-test.md §3"
  - "notes/debt1a-iii-tuning-test.md §5"
  - "notes/broken-born-theory.md 'Addendum (v0.4)'"
  - "notes/broken-born-theory.md 'Addendum (v0.3, overnight)'"
  - "notes/broken-born-theory.md §1"
  - "notes/broken-born-theory.md §4"
  - "papers/broken-born-checkpoint-v2.md §1"
  - "papers/broken-born-checkpoint-v2.md §7.2"
  - "papers/broken-born-checkpoint-v2.md §14"
  - "papers/broken-born-checkpoint-v2.md §15"
  - "papers/broken-born-checkpoint-v2.md ref [8]"
  - "review/round3/referee/audit-notes.md Step 1"
  - "review/round3/referee/audit-notes.md Step 3"
  - "notes/broken-born-program-v1.md §5"
  - "notes/knot-dark-matter-standalone.md §1"
  - "HANDOFF.md §2"
---

*The forcing chain is the sequence of arguments in [checkpoint #11](/wiki/history/documents/checkpoint) §7.1 that leaves the [momentum graviton X](/wiki/gravity/momentum-graviton) one consistent option: to be a massive spin-2 field. [Shift symmetry](/wiki/gravity/momentum-graviton/shift-symmetry) rules out an auxiliary X, a field with no motion of its own. The [dual diffeomorphisms](/wiki/gravity/momentum-graviton/dual-diffeomorphisms) make X a second graviton-like gauge field. If that gauge symmetry stays unbroken, X is a second massless graviton, and a theorem excludes two massless gravitons that interact; X has to interact, with the metric and with dark matter. If the gauge symmetry is dropped from the kinetic term, the time–space components of a symmetric tensor carry kinetic energy of the wrong sign in spacetime's signature, a ghost. Mass is the exit that remains, and it comes from the vacuum's choice of [polarization](/wiki/phase-space/reciprocity/lagrangian-polarizations). The chain replaced an earlier three-way question about X (healthy, auxiliary, or a ghost that would have killed the program's geometric sector) with the answer "massive spin-2, conditionally healthy", the condition being [the tuning test](/wiki/gravity/tuning-test). It is derived and rests on literature theorems [D + T]; no script checks it.*

**Status:** Alive — [D + T] in #11 §7.1 and [calc note #6](/wiki/history/documents/debt-1-notes) (`notes/debt1a-ii-X-classification.md` §2) — a chain of symmetry and no-go arguments, not machine-checked; the three-way classification it replaced is superseded (below).

## The chain as the checkpoint states it

#11 §7.1, headed "The chain [D + T]", where DFT is double field theory:

> (i) The rigid Sp(2d,ℝ) contains Z → Z + B (B symmetric): X is shift-symmetric — axion-like, never auxiliary. (ii) Locally, dual diffeomorphisms act as δX_μν = ∂₍μλ_ν₎ — a second linearized-diff gauge field, because X is *symmetric* (contrast DFT's antisymmetric B-field: the symmetry type of the rigid pairing dictates the partner's spin). Massless X is excluded by the multi-graviton no-go [8†]; ungauged X by Lorentz signature. (iii) The polarization choice spontaneously breaks the dual diffs; X eats the four Goldstones and emerges massive, M_X = the polarization-breaking scale. The unique consistent structure for massive spin-2 is Fierz–Pauli/dRGT/Hassan–Rosen [9†, 10†, 11†].

The † marks citations from model memory, not yet checked against the source, and dRGT is de Rham–Gabadadze–Tolley. X is the real part of [the modular field](/wiki/phase-space/modular-field/modular-field-z) Z = X + iY, whose imaginary part is the spacetime metric g. The derivation is calc note #6 §1–§3 ([the Debt-1 calc notes](/wiki/history/documents/debt-1-notes)), with these steps and tags:

| Step | What it establishes | Tag in #6 | Page |
| --- | --- | --- | --- |
| (i) | constant shifts Z → Z + B are exact symmetries: X is never auxiliary | [D — rigorous] (§1) | [shift symmetry](/wiki/gravity/momentum-graviton/shift-symmetry) |
| (ii) | local shifts δX_μν = ∂₍μλ_ν₎: X is a second graviton-like gauge field | [D + T] (§2) | [dual diffeomorphisms](/wiki/gravity/momentum-graviton/dual-diffeomorphisms) |
| massless excluded | massless multi-graviton cross-interactions are inconsistent | [T] (§2) | [the multi-graviton no-go](/wiki/gravity/spin-2-fields/multi-graviton-no-go) |
| ungauged excluded | no ghost-free two-derivative kinetic term without the gauge invariance | [T — standard] (§2) | [the Fierz–Pauli mass term](/wiki/gravity/spin-2-fields/fierz-pauli) |
| (iii) | the polarization choice breaks the dual diffeomorphisms; X becomes massive | [D — structural] (§3) | [the gravitational Higgs mechanism](/wiki/gravity/momentum-graviton/gravitational-higgs) |

## Steps (i) and (ii): what kind of field X is

The first two steps fix the type of field before any dynamics is written. The translations Z → Z + B belong to the symplectic group of the rigid form ω, so any geometric action built from ω and the phase-space metric H is unchanged by constant shifts of X. X can then appear only through its derivatives: it has no potential from geometry, it cannot be an auxiliary field that is solved for algebraically, and "it propagates or it doesn't exist" (#6 §1).

Locally the shifts become δX_μν = ∂₍μλ_ν₎ with an arbitrary vector field λ_μ(x). Because X is symmetric, this has the same form as the linearized coordinate changes of [general relativity](/wiki/gravity/spin-2-fields/general-relativity), δh_μν = ∂₍μξ_ν₎, and X is "a second graviton-like gauge field" (#6 §2). Calc note #6 then states: "Two consistency facts then close the door on the massless option". There are two cases, with the gauge invariance and without it.

## With the gauge invariance: the multi-graviton no-go [T]

### The theorem

> With the gauge invariance, X is a second **massless** spin-2 — and massless multi-graviton cross-interactions are inconsistent (Boulanger–Damour–Gualtieri–Henneaux). X must couple (to g through the Siegel structure, to χ through the gate), so decoupling is not available. [T]

(#6 §2.) The theorem is #11's reference [8†]: N. Boulanger, T. Damour, L. Gualtieri, M. Henneaux, "Inconsistency of interacting, multi-graviton theories," Nucl. Phys. B 597, 127 (2001), hep-th/0007220. The [round-3](/wiki/method/review/round-3) auditor read its abstract, "no consistent (ghost-free) coupling, with at most two derivatives ... that can mix the various gravitons", and judged that it supports the exclusion of a massless X coupled to gravity, with the caveats "2-derivative, local, ghost-free" (`review/round3/referee/audit-notes.md` Step 1). The theorem is described on [the multi-graviton no-go theorem](/wiki/gravity/spin-2-fields/multi-graviton-no-go).

### Why decoupling is not available

The theorem forbids couplings that mix massless gravitons. Copies that never interact with one another escape it [T], so a massless X would be consistent if it were sealed off from the metric and from matter. #6 rules that out with two couplings:

- **To g, through the Siegel structure.** X and the metric g = Y are the two halves of one field Z, and the phase-space metric contains them together: its upper-left block is Y + XY⁻¹X and its off-diagonal blocks are XY⁻¹ and Y⁻¹X (#5 §C; [the Siegel domain](/wiki/phase-space/modular-field/siegel-domain)).
- **To χ, through the gate.** [Conjugate matter](/wiki/dark-matter/conjugate-matter), the program's p-polarized matter χ, "couples to H universally (P4); its coupling to the X-block is through the **dual stress** T̃" (#5 §E; [P4: polarized matter](/wiki/program/postulates/p4-polarized-matter); [dual stress](/wiki/dark-matter/conjugate-matter/dual-stress)). Exchange of X between conjugate-matter particles is the program's mechanism for the [velocity gate](/wiki/dark-matter/conjugate-matter/velocity-gate) ([the gate mechanism](/wiki/dark-matter/conjugate-matter/gate-mechanism)).

A massless X would therefore be a second massless graviton that interacts, which the theorem excludes.

## Without the gauge invariance: the signature obstruction [T — standard]

### The fact

> Without the gauge invariance, no ghost-free two-derivative kinetic term for a Lorentz-covariant symmetric tensor exists (mixed time–space components enter with the wrong sign under any invariant contraction; this is why the Fierz–Pauli structure and its accidental gauge symmetry exist at all). [T — standard]

(#6 §2.) #11 states it as "ungauged X by Lorentz signature" (§7.1), and its abstract counts "a signature obstruction" among the structural results that force X to be massive (§1); calc note #7 uses the same name (§5).

### What it says [T]

A two-derivative kinetic term is the standard form of the energy of a field that propagates as a wave: quadratic in the field's first derivatives [T]. In a Lorentz-invariant theory the indices of a symmetric tensor are contracted with the spacetime metric, in which time has the opposite sign to space. In such a contraction the components with one time index and one space index come with the opposite sign from the rest, so if they propagated they would carry negative kinetic energy: a ghost, which makes the theory unstable [T]. The gauge invariance of linearized gravity is what keeps those components from propagating. A symmetric tensor whose kinetic term lacks it has no healthy kinetic term at all.

### What the two facts leave

Read together, the two facts leave one combination: a kinetic term that has the gauge invariance, so that the wrong-sign components do not propagate, and a mass that breaks the invariance, so that X is not a second massless graviton. That combination is the Fierz–Pauli structure for a massive spin-2 field [T], the structure #6's parenthesis names: "this is why the Fierz–Pauli structure and its accidental gauge symmetry exist at all".

This step uses the Lorentzian signature of spacetime directly. Calc note #6 nonetheless calls the chain of its §1–§3 "the Euclidean-rigorous skeleton", because the compatibility theorem and the Siegel parametrization beneath it were derived for positive-definite metrics; it adds that Lorentzian signature "is precisely the regime where the gauge+mass structure above is not a luxury but the only path to health" (§3; [Open: Lorentzian dressing of the Euclidean skeleton (OP3)](/wiki/phase-space/born-geometry/lorentzian-dressing)).

## The exit: mass

#6 §2 concludes: "**Therefore X must be massive.**"

The mass cannot be an explicit mass term in the geometric action, because the shift symmetry forbids it: "The mass cannot be written by hand (shift symmetry) — but it doesn't need to be" (#6 §3). It comes from the vacuum. The vacuum ⟨Z⟩ = i·g sits at X = 0 and is moved by the shifts, so the vacuum's selection of a polarization breaks the dual diffeomorphisms spontaneously, and X absorbs the [would-be Goldstone modes](/wiki/symmetry-breaking/goldstone-and-higgs) and becomes "a **massive spin-2** with its five polarizations" ([the gravitational Higgs mechanism](/wiki/gravity/momentum-graviton/gravitational-higgs)).

Which massive theory is consistent is the next question. #6 §3: "Massive spin-2 coupled to gravity has exactly one known consistent structure: the Fierz–Pauli tuning at quadratic order completed by a dRGT/Hassan–Rosen-class potential [T: HR 2011]", HR being Hassan–Rosen ([dRGT massive gravity](/wiki/gravity/spin-2-fields/drgt-massive-gravity); [Hassan–Rosen bimetric gravity](/wiki/gravity/spin-2-fields/hassan-rosen-bimetric)). #11 §7.1 words it without "known": "The unique consistent structure for massive spin-2 is Fierz–Pauli/dRGT/Hassan–Rosen".

## The answer: "massive spin-2, conditionally healthy"

Calc note #6 states where the classification lands (§3):

> **X is a massive spin-2 field. The geometric sector is healthy iff the potential generated by the η-selection lands in the Hassan–Rosen class; a generic potential reintroduces the Boulware–Deser ghost.**

The Boulware–Deser ghost is the extra negative-energy mode that a generic nonlinear mass term for a spin-2 field revives [T] ([the Fierz–Pauli mass term and the Boulware–Deser ghost](/wiki/gravity/spin-2-fields/fierz-pauli)). The note's closing summary (§5): "**Resolved:** the three-way classification. Not healthy-by-default, not auxiliary, not necessarily ghost: *massive spin-2, conditionally healthy*, with the massless branch excluded by theorem, the mass mechanism identified (Higgsed dual diffs), the eaten modes counted, and the unique consistent target structure named (HR class)."

The condition became a single computation, with the stakes stated in advance (#6 §5): "derive the X-potential from the η-selection (J–Z) sector and test it against the dRGT coefficient family. Pass ⇒ the geometric core stands and "theory" becomes the defensible word. Fail ⇒ the Boulware–Deser ghost kills the geometric sector, and BBT survives only as its phenomenological shell (gated SIDM + Maslov quintessence with the geometric story demoted to heuristics)." BBT is the Broken-Born program and SIDM [self-interacting dark matter](/wiki/dark-matter/halo-astrophysics/self-interacting-dark-matter).

The computation is [the tuning test](/wiki/gravity/tuning-test), tagged [D][V] in #11 §7.2. Its verdict (#7 §3): "the theory *fails* in second-order (metric) variables and *passes* in first-order (frame) variables. Since the first-order formulation is independently the natural one, this is a conditional pass with the condition being the formulation the geometry already prefers" ([the verdict: a conditional pass](/wiki/gravity/tuning-test/conditional-pass)). The passing class was selected, not derived: deriving it from the geometric action is open item 1 of #11 §14 ([Open: deriving the wedge sector from S_H (OP1)](/wiki/gravity/tuning-test/wedge-reduction)), one of the three items on which, in #11 §15's words, "the word 'theory' still waits".

## How many tests

Calc note #7, after the tuning test, counted "three structural tests in a row (multi-graviton no-go, signature obstruction, tuning test)" that "could each have killed the geometric sector outright; each instead forced it into the unique known consistent structure at that junction" (§5). #11 §15, which governs, counts "four consecutive consistency tests each forced the theory onto the unique consistent structure available", without naming them. The versions of the list in the documents are set out on [Assessment: a live research program](/wiki/program/assessment).

## Superseded: the three-way classification of X

Before the chain, the question of what X is had been posed as a computation with three possible outcomes. Calc note #5, in its section "Quadratic spectrum and the ghost question [partial]": "expand the generalized curvature scalar of (ω, H_Z) to quadratic order in X about X = 0 on the section, with ω-generalized diffeomorphisms as the gauge symmetry, and classify X as one of" (§D):

1. "**healthy propagating** → dynamical momentum-space gravity (Born's dream, linearized)";
2. "**auxiliary** (no derivatives at quadratic order) → integrate out → a *contact, momentum-structured* four-χ operator, i.e. the gate delivered directly";
3. "**ghost** → fatal to the geometric sector."

"Outcomes 1 and 2 both serve the program; only 3 kills. Not completed tonight; it is the single most important remaining calculation, and it is now a defined computation rather than a slogan." (§D.) It headed the note's list of what was "Now precisely open": "(1) the quadratic X classification of §D — *do this next*" (§F). The [lab notebook](/wiki/history/documents/lab-notebook)'s v0.3 addendum restated it as "a single decisive computation: the quadratic-order classification of X (healthy / auxiliary / ghost), where the first two outcomes serve the program and only the third kills the geometric sector."

Calc note #6 replaced the question instead of answering it in these terms. Its status line: "the three-way classification (healthy / auxiliary / ghost) is resolved into a sharper statement: X is forced to be a massive spin-2 field, with exactly one known consistent structure available, and the massless option excluded by theorem." Its answer matches none of the three outcomes as posed: "Not healthy-by-default, not auxiliary, not necessarily ghost: *massive spin-2, conditionally healthy*" (§5). The shift symmetry removed outcome 2 ("'auxiliary X' (the soft outcome 2) is off the table at the fundamental level", §1); the no-go and the signature obstruction showed that a propagating X cannot be massless; and whether X carries the ghost of outcome 3 became the condition that the tuning test examined. The curvature expansion itself is reported in no document. The same history is recorded, from the side of the field list, on [Open: field content of the broken vacuum](/wiki/phase-space/modular-field/field-content).

## Superseded: no second graviton under the original P2

The lab notebook's v0.1 had the opposite expectation. Its rigidity postulate, the [original P2](/wiki/program/postulates/original-p2), froze both ω and the neutral metric η, and the notebook said it "does triple duty below: it kills the would-be second graviton (no Boulware–Deser ghost, §6)" (#1 §1). The notebook's §6 finds the dual gravitational sector of minisuperspace "not a new fluid and not a ghost", since ã was never independent, and its §4, "Ghost accounting", states the claim:

> There is no second independent metric: g̃'s cosmological mode is eliminated by the P2 constraint (§7), so no Boulware–Deser sector arises in minisuperspace. **[D]** The statement for full inhomogeneous H is open. **[O]**

The P2 constraint, a·ã = 1, is derived in the notebook's §6 and used in its §7. With both structures frozen, [the compatibility theorem](/wiki/phase-space/born-geometry/compatibility-theorem) leaves only H = diag(g, g⁻¹), so the momentum metric g̃ = g⁻¹ has no freedom of its own. Under [P2′](/wiki/program/postulates/p2-prime), with η emergent, the metric can leave that slice, and its off-diagonal blocks carry the new field X (#5 §C). The v0.4 addendum reversed the claim: "Its local gauge structure δX_μν = ∂_(μλ_ν) makes it a *second graviton*", made massive by the polarization choice. Ghost-freedom now comes from the formulation, not from rigidity: the frame-tier couplings are the Hinterbichler–Rosen class, "ghost-free by construction" (#11 §7.2; [the frame tier](/wiki/gravity/tuning-test/frame-tier)). The fate of the rest of P2's "triple duty" is on the original-P2 page; the v0.1 action and its ghost accounting are on [the geometric action S_H and the v0.1 action](/wiki/gravity/tuning-test/geometric-action).

## Scope and caveats

- **Not machine-checked.** The seven battery tests check the compatibility theorem, the Siegel parametrization, the misalignment blocks, the linearized potential, the palindrome identity, the linearization coefficients and the p₄ exclusion ([the verification battery](/wiki/method/verification/battery)); none checks a step of this chain. `HANDOFF.md` §2 lists "X is forced massive" among the results that stand, without the check mark it gives machine-verified items.
- **Literature steps.** The no-go is a memory citation [8†], due a source check in [the literature battery](/wiki/method/literature-battery). Its exclusion holds within the theorem's assumptions as the round-3 auditor summarized them: at most two derivatives, local, ghost-free.
- **Positive metrics.** The compatibility theorem and the Siegel parametrization under the chain were derived for positive-definite metrics, and #6 calls its §1–§3 "the Euclidean-rigorous skeleton" (§3); the Lorentzian extension is open item 3.
- **The round-3 auditor's caution.** Reviewing the withdrawn soliton manuscript (#14; [the soliton candidate](/wiki/dark-matter/candidates/soliton-candidate)), whose §1 states the chain in a few sentences, the blind auditor wrote of the compatibility theorem: "It is a pointwise linear-algebra fact; it does not by itself establish any physics (the identification of a dynamical H, a rigid eta, and a second spin-2 field X is assumed, not derived)" (`review/round3/referee/audit-notes.md` Step 3). The round-3 adjudication did not rule on the remark. The broader critique is [the "framework does no work" critique](/wiki/program/framework-does-no-work).

## History

- **The question** was posed in calc note #5 §D and the v0.3 addendum (above).
- **The answer.** Calc note #6 §1–§3, summarized in the lab notebook's v0.4 addendum: "Massless X is then excluded by the multi-graviton no-go (Boulanger–Damour–Gualtieri–Henneaux), and the ghost-free no-gauge option is excluded by Lorentz signature. The only exit: the polarization selection (η-emergence) spontaneously breaks the dual diffeomorphisms, X eats the four Goldstones and becomes a **massive spin-2** with M_X = the polarization-breaking scale." Its result: "the geometric sector is bimetric gravity with structure dictated by modular symmetry — healthy **iff** the η-selection generates a Hassan–Rosen-class potential" ([the lab notebook](/wiki/history/documents/lab-notebook)).
- **The v1 paper.** #9 §5 gives "The chain, each link load-bearing", with the steps tagged "Shift symmetry [D]", "Gauge structure and no-go [D+T]" and "The mass [D]", and words the exclusions: "Massless: excluded by the multi-graviton no-go (Boulanger–Damour–Gualtieri–Henneaux) since X must couple. Ungauged: excluded by Lorentz signature (wrong-sign mixed components)."
- **The checkpoint.** #11 §7.1 is the current statement, and #11's abstract summarizes: "A chain of structural results (a compatibility theorem [T][V]; the multi-graviton no-go [8†]; a signature obstruction; an explicit tuning test [V]) forces X to be a **massive spin-2** field" (§1). The handoff: "X is forced massive: shift symmetry ⇒ never auxiliary; δX = ∂λ ⇒ second graviton; massless excluded (Boulanger–Damour–Gualtieri–Henneaux no-go); mass via Higgsed dual diffeomorphisms" (`HANDOFF.md` §2).
- **The withdrawn manuscript.** #14 §1 gives the no-go step and the Higgs step but not the signature obstruction: "a massless X coupled to gravity is excluded by the multi-graviton no-go [2]. The polarization choice spontaneously breaks the dual diffeomorphisms; X absorbs the Goldstones and acquires mass M_X (gravitational Higgs)".

## Sources

- `papers/broken-born-checkpoint-v2.md` §7.1 — the chain [D + T]; §1 — the abstract's list of structural results; §7.2 — the tuning test [D][V] and the frame tier; §14 — open items 1 and 3; §15 — "four consecutive consistency tests"; ref [8] — the no-go, marked †.
- `notes/debt1a-ii-X-classification.md` §1–§3 — the derivation, with its tags; §5 — the resolved classification and the remaining computation.
- `notes/debt1a-geometric-core.md` §D — the three-way classification as first posed; §C — H_Z, through which X couples to g; §E — the coupling of χ to X through the dual stress; §F — the classification as the next computation.
- `notes/debt1a-iii-tuning-test.md` §3 — the verdict of the tuning test; §5 — the "three structural tests" count.
- `notes/broken-born-theory.md` §1, §4 — the v0.1 claim of no second graviton; 'Addendum (v0.3, overnight)' — the classification restated; 'Addendum (v0.4)' — the chain and its result.
- `review/round3/referee/audit-notes.md` Step 1 — the no-go abstract and its caveats; Step 3 — the auditor's caution.
- `notes/broken-born-program-v1.md` §5 — the v1 statement of the chain.
- `notes/knot-dark-matter-standalone.md` §1 — the withdrawn manuscript's compressed version.
- `HANDOFF.md` §2 — the handoff's summary.
