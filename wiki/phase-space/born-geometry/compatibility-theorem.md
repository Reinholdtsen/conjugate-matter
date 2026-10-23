---
title: "The compatibility theorem"
weight: 40
status: established
description: "Positive H compatible with both rigid ω and η are exactly diag(g, g⁻¹): Freidel–Leigh–Minic's statement, the program's block proof, battery test T1, and round 3's independent Gröbner re-derivation."
provenance: [T, V]
sources:
  - "CLAUDE.md 'Since the handoff'"
  - "papers/broken-born-checkpoint-v2.md §5"
  - "papers/broken-born-checkpoint-v2.md §2"
  - "papers/broken-born-checkpoint-v2.md §6"
  - "papers/broken-born-checkpoint-v2.md §15"
  - "papers/broken-born-checkpoint-v2.md ref [26]"
  - "review/round3-adjudication.md 'Rulings'"
  - "review/round3-adjudication.md 'What survives v3'"
  - "review/round3-adjudication.md 'Decisions'"
  - "review/round3/referee/audit-notes.md Step 1"
  - "review/round3/referee/audit-notes.md Step 3"
  - "review/round3/referee/audit-notes.md Step 4"
  - "review/round3/referee/step3.out d = 1–4"
  - "review/round3/referee/step3_diag.out d = 1–3"
  - "review/round3/referee/step3_groebner.out d = 2"
  - "review/round3/referee/step3.py residuals"
  - "notes/debt1a-geometric-core.md §A"
  - "notes/debt1a-geometric-core.md §C"
  - "notes/debt1a-ii-X-classification.md §3"
  - "notes/broken-born-theory.md 'Addendum (v0.3, overnight)'"
  - "notes/broken-born-program-v1.md §3"
  - "notes/knot-dark-matter-standalone.md §1"
  - "notes/knot-dark-matter-standalone.md §6"
  - "papers/conjugate-special-relativity.md §1"
  - "verify/battery.py T1"
  - "scripts/check.sh verify loop"
  - "HANDOFF.md §2"
  - "HANDOFF.md §6"
  - "review/wiki-build-flags.md items 1, 30"
---

*The compatibility theorem is a statement of linear algebra about metrics on phase space: if [the symplectic form](/wiki/phase-space/reciprocity/symplectic-form) ω and the neutral metric η are both held fixed in their standard forms, the only positive metrics H compatible with both are block-diagonal, H = diag(g, g⁻¹), with the momentum block equal to the inverse of the position block. "Compatible" means that H fits each structure in the way [Born geometry](/wiki/phase-space/born-geometry/born-structures) requires, (η⁻¹H)² = 1 and (ω⁻¹H)² = −1. The statement is [Freidel, Leigh and Minic](/wiki/phase-space/reciprocity/broken-born-duality)'s; the short block proof and its machine check are the program's, and an independent reviewer re-derived it in [round 3](/wiki/method/review/round-3) and found that one step of the proof is not needed. Its use in the program is that it forced a change of postulates: with both structures fixed, the program reduces to [general relativity](/wiki/gravity/spin-2-fields/general-relativity) plus one dark-matter model, so the program replaced its postulate [P2](/wiki/program/postulates/original-p2) with [P2′](/wiki/program/postulates/p2-prime) and let η vary.*

**Status:** Established — literature [T] (Freidel–Leigh–Minic, #11 ref. [26S, §2.1]), with the program's block proof machine-checked [V] (battery test T1; [the battery](/wiki/method/verification/battery)) — re-derived independently in round 3 by symbolic algebra, a Gröbner basis and numerical families; re-attributed from "derived here" to the literature in #11 v2.1.

## Statement

Checkpoint [#11](/wiki/history/documents/checkpoint) §5:

> **Compatibility theorem [T][V].** Positive H satisfying both (η⁻¹H)² = 1 and (ω⁻¹H)² = −1 are exactly H = diag(g, g⁻¹), g ∈ Sym⁺(d).

Sym⁺(d) is the set of real symmetric positive-definite d × d matrices [T]. The calc note that gave the program's proof, [#5](/wiki/history/documents/debt-1-notes) §A, states the setting: "On flat phase space with ω and η both in standard form", the positive generalized metrics "satisfying the full Born algebra — (η⁻¹H)² = +1 **and** (ω⁻¹H)² = −1" are exactly those block-diagonal matrices. In the notation of [the structures ω, η, H](/wiki/phase-space/born-geometry/born-structures), the two conditions are J² = 1 and I² = −1.

The theorem concerns one tangent space at a time. The withdrawn manuscript [#14](/wiki/dark-matter/candidates/soliton-candidate) calls it "pointwise, in a flat frame" (§1), and the round-3 referee "a pointwise linear-algebra fact" (audit notes, Step 3).

## What the two conditions mean [T]

For a symmetric H with ω and η in standard form, each condition says that H preserves one of the two structures:

- **(η⁻¹H)² = 1** says that H preserves η, so H is an element of O(d, d). Such matrices are the generalized metrics of [double field theory](/wiki/phase-space/born-geometry/double-field-theory), built from a metric g and an antisymmetric [B-field](/wiki/phase-space/born-geometry/kalb-ramond-field#in-double-field-theorys-generalized-metric-t).
- **(ω⁻¹H)² = −1** says that H preserves ω. The positive symplectic matrices form [the Siegel domain](/wiki/phase-space/modular-field/siegel-domain), parametrized by a complex symmetric matrix Z = X + iY with Y positive definite.

Each condition alone admits a large family, and round 3 sampled both: the family with a B-field satisfies the η condition and fails the ω condition, and the Siegel family with X ≠ 0 does the reverse (families (c) and (d) in the table below). The theorem says the two families meet only in diag(g, g⁻¹), where the B-field and X both vanish. In double field theory's terms this is Freidel, Leigh and Minic's statement that H "is related to ω through a complex structure exactly when B vanishes" (#11 §5). In the terms of [the modular field](/wiki/phase-space/modular-field/modular-field-z) it is the slice X = 0: "the η-compatible locus X = 0 is the vacuum slice of §5" (#11 §6).

## The proof

#11 §5 gives the proof in three lines, and #5 §A says how positivity enters. With H written in d × d blocks:

```text
H = [[A, C], [Cᵀ, B]]            A, B symmetric;  C a general d × d block

(2,1) block of (η⁻¹H)² − 1:      A Cᵀ + C A = 0
(2,1) block of (ω⁻¹H)² + 1:      C A − A Cᵀ = 0
hence                            A Cᵀ = 0
positivity:                      A invertible, so C = 0
diagonal blocks, with C = 0:     B A = A B = 1,  so B = A⁻¹        ∎
```

Step by step:

1. **Blocks.** Positivity of H makes its diagonal blocks positive definite. #5 §A: "positivity makes A invertible".
2. **The off-diagonal equations.** The lower-left block of each squared operator is linear in C. The two conditions require both blocks to vanish, and together they give A Cᵀ = 0. The round-3 referee notes that the sum of the two block expressions is 2CA and their difference 2ACᵀ (audit notes, Step 3).
3. **C = 0.** A is invertible, so A Cᵀ = 0 forces C = 0.
4. **The diagonal blocks.** With C = 0, H is block-diagonal and the remaining equations reduce to B·A = 1 and A·B = 1, as the round-3 referee confirmed (`With C=0 the remaining equations reduce to BA=1 and AB=1: True`, audit notes, Step 3). So B = A⁻¹, and writing g = A gives H = diag(g, g⁻¹).
5. **The converse.** H = diag(g, g⁻¹) satisfies both conditions for every g ∈ Sym⁺(d).

#11 §5 closes the proof with "(Both directions and the individual block identities machine-checked.)"

## Battery test T1 [V]

The gate runs `verify/battery.py`, whose first test checks the theorem at d = 4 ([the battery](/wiki/method/verification/battery)). The recorded run prints:

```text
PASS  T1a diag(g,g^-1) satisfies (eta^-1 H)^2=1 and (omega^-1 H)^2=-1
PASS  T1b generic H violates at least one condition
PASS  T1c proof block (J^2)_21 = A C^T + C A
PASS  T1c proof block (I^2)_21 = C A - A C^T
```

T1a draws one positive-definite g and checks the converse direction on H = diag(g, g⁻¹). T1b draws one H with positive-definite diagonal blocks and a nonzero off-diagonal block, and checks that it fails at least one condition. The two T1c lines check, on that same H, the block identities that steps 2 and 3 of the proof rest on. Each check runs on a single seeded random instance, so the battery confirms the identities numerically; the proof is the block argument.

## Round 3's independent re-derivation

The round-3 referee, a blind subagent with Python and web access reviewing the withdrawn manuscript #14, re-derived the theorem from scratch (audit notes, Step 3; scripts and outputs in `review/round3/referee/`). Its setup: "omega=[[0,1],[-1,0]], eta=[[0,1],[1,0]] (d x d blocks), H=[[A,C],[C^T,B]], A,B symmetric, C general." It writes E1 = (η⁻¹H)² − 1 and E2 = (ω⁻¹H)² + 1 for the two residual matrices.

### Symbolic checks at d = 1 and d = 2

Computer algebra confirmed the proof's block identities at d = 1 and d = 2 (`step3.out`):

```text
(2,1) block of (eta^-1 H)^2 - 1 == A C^T + C A : True
(2,1) block of (omega^-1 H)^2 + 1 == C A - A C^T : True
sum = 2 C A : True ; difference = 2 A C^T : True
```

At d = 1 the full solution of the equations, with no positivity imposed, has one branch, `C = [0] | A = [1/b0] | B = [b0]`. At d = 2 the general-purpose solver returned no branches, which the referee records as "sympy.solve returned 0 branches (solver failure, not a counterexample)", and settled the case with a Gröbner basis instead.

### The Gröbner basis at d = 2

A system of polynomial equations generates an *ideal*: every polynomial combination of the equations. A polynomial in the ideal vanishes at every solution of the system. A *Gröbner basis* is a generating set of the ideal for which reduction gives a unique remainder, the normal form, so a polynomial lies in the ideal exactly when its normal form is zero [T].

The referee's ideal is generated by the entries of (η⁻¹H)² − 1 and (ω⁻¹H)² + 1 together with t·det(A) − 1. The extra variable t, a standard device, admits only solutions with det A ≠ 0. The normal forms of all four entries of C, and of every entry of B·A − 1, came out zero (`step3_groebner.out`). The referee's conclusion: "algebraic proof C=0, B=A^-1". Without the equation for t, the entry c0 of C still lies in the ideal (`True`), and 1 does not (`False`), so the equations still have solutions (audit notes, Step 3).

### Positivity is not needed for C = 0

The diagonal blocks carry more information than the proof uses. For d = 1, 2 and 3 the referee found (`step3_diag.out`):

```text
(1,1)-blocks: E1+E2 == 2 (C^T)^2 : True ; E1-E2 == 2(BA-1): True
```

Its reading (audit notes, Step 3):

```text
Hence BA=1 follows from the diagonal blocks alone, A is automatically
invertible, and CA=0 then gives C=0. Positivity is NOT needed for C=0
(only for g>0).
```

Setting both residuals to zero in these identities gives B·A = 1 from the diagonal blocks alone, without assuming anything about A. Positivity is needed only for the solution g to be a positive metric. #11 §5 records the refinement ("the positivity step is not needed for C = 0") and keeps its proof as written, so the proof stands and the positivity step is redundant, not wrong ([conflicts between sources](/wiki/history/documents/source-conflicts)).

### Numerical families at d = 3 and d = 4

The referee drew 2000 random members of each of families (a) to (d), and one perturbation of each size for family (e), and measured the residuals, the matrix norms of E1 and E2 (`step3.py`). From `step3.out`:

| Family | d = 3 | d = 4 |
| --- | --- | --- |
| (a) diag(g, g⁻¹): largest residuals | η 4.71e-15, ω 4.71e-15 | η 8.37e-15, ω 8.37e-15 |
| (b) generic positive H with C ≠ 0: smallest, over trials, of the larger residual | 21.032 | 83.515 |
| (c) η only, a generalized metric with a B-field | η at most 4.97e-14; ω at least 0.282 | η at most 7.30e-14; ω at least 1.483 |
| (d) ω only, the Siegel family with X ≠ 0 | ω at most 2.30e-14; η at least 0.524 | ω at most 2.85e-14; η at least 1.873 |
| (e) diag(g, g⁻¹) plus C of size 1e-02 | η 9.23e-02, ω 6.15e-02 | η 4.56e-01, ω 3.72e-01 |
| (e) diag(g, g⁻¹) plus C of size 1e-04 | η 1.44e-03, ω 2.39e-04 | η 2.12e-03, ω 3.41e-03 |

In family (b) "every trial violates at least one" condition. Of family (e) the audit notes say "perturbing diag by C of size 1e-4 gives residuals ~1e-3: the solution set is isolated as claimed."

### The verdict

The referee's verdict on the theorem: `theorem TRUE; stated proof VALID (uses positivity where it is not needed; slightly weaker hypothesis suffices)`. It added: "It is essentially the known Freidel-Leigh-Minic 'Born geometry' statement (B-field vanishes <=> I = H^-1 omega compatible), uncited (1502.08005 p.11). It is a pointwise linear-algebra fact; it does not by itself establish any physics (the identification of a dynamical H, a rigid eta, and a second spin-2 field X is assumed, not derived)."

The adjudication agreed: "**The compatibility theorem is verified** (sympy, including a Groebner basis at d = 2; random tests at d = 3, 4)", and listed it among what survives the withdrawn manuscript, "as [T], pending the FLM comparison" (FLM is Freidel–Leigh–Minic; `review/round3-adjudication.md`; [the round-3 rulings](/wiki/method/review/round-3/rulings)). The referee's scripts are a review record and are not part of the gate: `scripts/check.sh` runs the scripts in `verify/` and the wiki check ([the gate](/wiki/method/verification/the-gate)).

## Attribution history

Until round 3 the program treated the theorem as its own result:

- calc note #5 heads its section "The compatibility theorem [D — rigorous]", and the [notebook](/wiki/history/documents/lab-notebook)'s v0.3 addendum reports that the [Debt-1](/wiki/history/debts) groundwork "produced a rigorous compatibility theorem";
- the v1 program paper tags it "Compatibility theorem [D]" (#9 §3);
- [#13](/wiki/conjugate-relativity) builds on it with the tag "[D — compatibility theorem]" (#13 §1; see flag 30 in `review/wiki-build-flags.md`);
- the withdrawn #14 lists it under "Derived within the framework or by standard methods" as "the compatibility theorem (elementary; machine-verified numerically in both directions)" (#14 §6);
- [the handoff](/wiki/history/documents/handoff) lists it among the alive results, "derived, machine-verified where marked ✓", with the ✓ (`HANDOFF.md` §2).

Round 1's referee "insinuated the compatibility theorem might be false (it is machine-verified)", one of the reviewer errors that the machine check settled (`HANDOFF.md` §6; [review rounds 1 and 2](/wiki/method/review/rounds-one-and-two)).

Round 3 found the prior art. Under "Uncited claims / prior art that should be cited" the referee wrote: "The compatibility theorem is the known 'Born geometry' structure of Freidel-Leigh-Minic: 1502.08005 (JHEP 06 (2015) 006), p.11", and quoted the passage that defines Born geometries (audit notes, Step 1). The adjudication: "Unless a comparison shows otherwise, the checkpoint's '[D] derived here' tag on it should become [T] with that citation." Decision 4 then scheduled the cleanup: "check the Freidel–Leigh–Minic prior art and re-tag the compatibility theorem if confirmed".

#11 v2.1 (2026-10-19) made the change: "*Attribution (v2.1):* v2.0 presented this as derived here. It is the Born-geometry compatibility statement of Freidel, Leigh and Minic: writing the η-compatible H in terms of (G, B), H is related to ω through a complex structure exactly when B vanishes [26S, §2.1]. The block proof and the machine check are this program's." The root `CLAUDE.md` records "compatibility theorem re-tagged [T] (Freidel–Leigh–Minic)". #11 §15 counts the re-attribution among the program's degeneration risks, "the novelty demotion of §7.4 as a standing caution, joined in v2.1 by the §12 soliton obituary and the §5 re-attribution of the compatibility theorem".

The older documents keep their old tags. #11 and the root `CLAUDE.md` govern, so the statement is [T] and the block proof and machine check are [V] ([conflicts between sources](/wiki/history/documents/source-conflicts)).

The reference: #11 [26][S] L. Freidel, R. G. Leigh, D. Minic, "Metastring theory and modular space-time," JHEP 06 (2015) 006, arXiv:1502.08005; §2.1 for the statement, p. 11 for the name "Born geometries".

## Scope

- **Euclidean only.** The theorem is proven for positive-definite H. Calc note #6 §3: "the compatibility theorem and Siegel parametrization were derived for positive H". The extension to spacetime signature is open problem 3 of #11 ([Open: Lorentzian dressing](/wiki/phase-space/born-geometry/lorentzian-dressing)).
- **Pointwise.** It is a statement about one tangent space, in a flat frame.
- **No physics by itself.** In the round-3 referee's words, "it does not by itself establish any physics". In #14 it did no further work: "The compatibility theorem (true) is never used after Sec. 1" (audit notes, Step 4(d)), part of [the 'framework does no work' critique](/wiki/program/framework-does-no-work).

## What follows

- **Three corollaries:** det H = 1, no analog of the Kalb–Ramond B-field, and a momentum metric slaved to the position metric, g̃ = g⁻¹ ([the corollaries](/wiki/phase-space/born-geometry/compatibility-corollaries)).
- **The postulate change.** Under the original P2, with ω and η both rigid, "the compatible polarizations are discrete, so no Grassmannian, no Maslov circle, no dark-energy field, and S_H is a functional of g alone: **nontriviality theorem** — the program has content iff η is emergent. Hence P2 → P2′." (#11 §5; on "discrete", see flag 1 in `review/wiki-build-flags.md`; [original P2](/wiki/program/postulates/original-p2), [the nontriviality theorem](/wiki/program/postulates/nontriviality-theorem), [P2′](/wiki/program/postulates/p2-prime).)
- **The vacuum slice.** Under P2′ only ω is rigid, H ranges over the Siegel domain, and the theorem's solutions become the slice X = 0 of [the modular field Z = X + iY](/wiki/phase-space/modular-field/modular-field-z): "At X = 0, H = diag(g, g⁻¹): the η-compatible locus of Theorem A is precisely the vacuum slice" (#5 §C).
- **Two light cones.** #13 reads the block form as two metrics, "position space carries the metric g and momentum space its inverse", each with its own null cone ([two causal cones](/wiki/conjugate-relativity/two-causal-cones)). Flag 30 in `review/wiki-build-flags.md` notes that the theorem's g is positive-definite and has no null cone, so the cones need the Lorentzian dressing, which is open ([OP3](/wiki/phase-space/born-geometry/lorentzian-dressing)). #13 tags the block form "[D — compatibility theorem]" and draws the cones from it in an untagged sentence; the flags' audit found the tag itself supported by the theorem and rated the flag as a question of tagging convention, turning on whether #13's inherited Euclidean/Lorentzian caveat covers the cones.

## Used by

- [The hard core: spontaneously broken Born reciprocity](/wiki/program/hard-core) — the theorem behind the first sharpening, P2 → P2′.
- [P1: the phase-space arena](/wiki/program/postulates/p1-arena) — what H can be with η fixed as well as ω.
- [Original P2: both structures rigid (superseded)](/wiki/program/postulates/original-p2) — the postulate the theorem showed to be too rigid.
- [The nontriviality theorem](/wiki/program/postulates/nontriviality-theorem) — content beyond general relativity requires η to be emergent.
- [P2′: only the symplectic form is rigid](/wiki/program/postulates/p2-prime) — the repair the theorem forced.
- [The modular field Z = X + iY](/wiki/phase-space/modular-field/modular-field-z) — the theorem's solutions are the vacuum slice X = 0.
- [Open: Lorentzian dressing of the Euclidean skeleton (OP3)](/wiki/phase-space/born-geometry/lorentzian-dressing) — the theorem is proven for positive-definite H only.
- [Born's answer: momentum space gravitates](/wiki/gravity/momentum-graviton/borns-answer) and [why X must be massive](/wiki/gravity/momentum-graviton/forcing-chain) — with both structures frozen, g̃ = g⁻¹ has no freedom of its own.
- [The symplectic partner of the graviton is another graviton](/wiki/gravity/momentum-graviton/symplectic-partner) — with both pairings rigid, no partner field survives.
- [The geometric action S_H and the v0.1 action (superseded)](/wiki/gravity/tuning-test/geometric-action) — strict P2 leaves S_H a functional of g alone.
- [The misalignment potential](/wiki/gravity/tuning-test/misalignment-potential) — #11's η-compatible locus X = 0, distinct from #7's compatible locus.
- [The cosmological constraint a·ã = 1](/wiki/cosmology/scale-factor-duality/cosmological-constraint) — the first corollary, det H = 1, as the same ℏ-rigidity.
- [Conjugate monopoles as ontology](/wiki/electric-magnetic-duality/conjugate-monopoles) — on the vacuum slice, universal coupling to H includes coupling to g.
- [Two causal cones](/wiki/conjugate-relativity/two-causal-cones) — #13 builds its two light cones on H = diag(g, g⁻¹) (see flag 30 in `review/wiki-build-flags.md`).
- [Two gravitational charges and the conjugate field equations (chat-only)](/wiki/gravity/momentum-graviton/chat-only-results) — corollary 3 as the documented counterpart of the slaved layer.
- [Obituary: superheavy conjugate solitons](/wiki/dark-matter/candidates/soliton-candidate/obituary) — the one framework result the withdrawn manuscript cited, re-derived by the round-3 referee.

## Sources

- `CLAUDE.md` "Since the handoff" — the re-tag to [T] with the Freidel–Leigh–Minic credit.
- `papers/broken-born-checkpoint-v2.md` §5 and ref. [26] — statement, proof, attribution and the positivity note; §2 — Tier 1, "both directions"; §6 — the vacuum slice; §15 — the re-attribution as a degeneration risk.
- `review/round3-adjudication.md` "Rulings", "What survives v3", "Decisions" — verified, identified as Freidel–Leigh–Minic's result, kept "as [T], pending the FLM comparison"; the cleanup decision.
- `review/round3/referee/audit-notes.md` Step 1, Step 3, Step 4(d) — the prior art; the symbolic, Gröbner and numerical re-derivation and the verdict; never used after Sec. 1.
- `review/round3/referee/step3.out`, `review/round3/referee/step3_diag.out`, `review/round3/referee/step3_groebner.out`, `review/round3/referee/step3.py` — the referee's outputs and the residual definitions.
- `papers/conjugate-special-relativity.md` §1 — the block form as two metrics with two cones.
- `HANDOFF.md` §2, §6 — the ✓ in the handoff; round 1's doubt, settled by the machine check.
- `notes/debt1a-geometric-core.md` §A, §C — the original proof, tagged "[D — rigorous]"; the vacuum slice.
- `notes/debt1a-ii-X-classification.md` §3 — proven for positive H only.
- `notes/broken-born-theory.md` 'Addendum (v0.3, overnight)'; `notes/broken-born-program-v1.md` §3 — the theorem as derived here, before the re-attribution.
- `notes/knot-dark-matter-standalone.md` §1, §6 — "pointwise, in a flat frame"; listed as derived.
- `verify/battery.py` T1 — both directions and the two proof-block identities.
- `scripts/check.sh` — the gate runs `verify/`, not the referee's scripts.
- `review/wiki-build-flags.md` items 1, 30 — the query on "discrete" in #11 §5's statement of the nontriviality theorem; #13's tag on its two cones.
