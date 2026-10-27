---
title: "Corollaries: unimodularity, no B-field, slaved momentum metric"
weight: 50
status: established
description: "det H = 1 (ℏ-rigidity as geometry), no Kalb–Ramond analog, and g̃ = g⁻¹ — the slaved momentum metric that collided with the theory as documented and forced the repair."
provenance: [D]
sources:
  - "notes/debt1a-geometric-core.md §A"
  - "notes/debt1a-geometric-core.md §B"
  - "notes/debt1a-geometric-core.md §C"
  - "notes/debt1a-geometric-core.md §F"
  - "papers/broken-born-checkpoint-v2.md §5"
  - "papers/broken-born-checkpoint-v2.md §2"
  - "papers/broken-born-checkpoint-v2.md §7.1"
  - "verify/battery.py T2"
  - "review/round3/referee/audit-notes.md Step 3"
  - "review/round3/referee/step3.out (a)"
  - "review/round3/referee/step3.py (a)"
  - "notes/broken-born-theory.md §3"
  - "notes/broken-born-theory.md 'Addendum (v0.3, overnight)'"
  - "notes/knot-dark-matter-standalone.md §1"
  - "papers/conjugate-special-relativity.md §1"
  - "HANDOFF.md §2"
  - "HANDOFF.md §4"
  - "HANDOFF.md §5"
---

*Three consequences follow from the [compatibility theorem](/wiki/phase-space/born-geometry/compatibility-theorem)'s answer H = diag(g, g⁻¹). The determinant of H is 1, so the phase-space volume that H measures cannot change, which the program reads as the constancy of Planck's constant built into the geometry. The off-diagonal block, where [double field theory](/wiki/phase-space/born-geometry/double-field-theory) keeps its antisymmetric [B-field](/wiki/phase-space/born-geometry/kalb-ramond-field), must vanish. And the momentum metric is fixed as the inverse of the position metric, g̃ = g⁻¹, so momentum space has no geometry of its own. That last corollary contradicted the program as it then stood: the dark-energy field and the geometric origin of [the dark-matter gate](/wiki/dark-matter/conjugate-matter/velocity-gate) both disappeared. It forced the postulate change to P2′, under which the block form, and with it the slaved momentum metric, holds only on the vacuum slice of the modular field.*

**Status:** Established — derived in #5 as rigorous corollaries ("[D — rigorous]") of a theorem that #11 v2.1 credits to [Freidel–Leigh–Minic](/wiki/phase-space/reciprocity/broken-born-duality) [T]; the reading of det H = 1 as ℏ-rigidity is the program's — det H = 1 off the vacuum slice is machine-checked at one sampled point of the modular family (battery test T2, [the battery](/wiki/method/verification/battery)), so #11's statement that it persists across the whole family stays [D] here.

## From the theorem to the corollaries

The compatibility theorem fixes H completely once g is given: with ω and η both rigid, the positive H compatible with both are exactly H = diag(g, g⁻¹), g ∈ Sym⁺(d). Calc note [#5](/wiki/history/documents/debt-1-notes) §A reads off three consequences, under the heading "[D — rigorous]":

1. "**det H = 1 identically.** The generalized metric is unimodular: phase-space volume is not a dynamical field. ℏ-rigidity is manifest in the geometry, not imposed on it."
2. "**No Kalb–Ramond analog.** The off-diagonal block — [double field theory's] B-field — is frozen out by the extra symplectic compatibility. Born geometry with both structures rigid is *stiffer* than [double field theory]."
3. "**The momentum metric is slaved: g̃ = g⁻¹ pointwise.** No independent momentum-space geometry survives."

Checkpoint [#11](/wiki/history/documents/checkpoint) §5 lists them in one line: "Corollaries: det H = 1 identically (ℏ-rigidity is *geometric*, and — machine-verified — persists across the whole modular family of §6); no Kalb–Ramond analog; g̃ = g⁻¹ slaved." [The handoff](/wiki/history/documents/handoff) carries the theorem and the first and third corollaries on one line with a machine-check mark: "Compatibility theorem: ω,η both rigid ⇒ H = diag(g,g⁻¹), det H = 1, momentum metric slaved g̃ = g⁻¹ ✓" (`HANDOFF.md` §2).

## Corollary 1: det H = 1

**The statement.** The determinant of a block-diagonal matrix is the product of the blocks' determinants, and det g⁻¹ = 1/det g, so det diag(g, g⁻¹) = 1 for every g [T]. The volume element that H defines on phase space is therefore the same everywhere, whatever g does: "phase-space volume is not a dynamical field" (#5 §A).

**The reading.** In quantum mechanics ℏ sets the size of the phase-space cell occupied by one state [T], and the program reads the rigid symplectic form ω as the constancy of ℏ ([the symplectic form](/wiki/phase-space/reciprocity/symplectic-form); [the canonical commutator](/wiki/phase-space/reciprocity/canonical-commutator)). It reads det H = 1 as the same rigidity seen in the metric: "ℏ-rigidity is manifest in the geometry, not imposed on it" (#5 §A), "unimodularity of H (det H = 1) as the geometric face of ℏ-rigidity" (#5 §F). The mathematics is elementary; the reading is the program's.

**Across the modular family.** Under P2′ only ω is rigid, and H ranges over the Siegel family H_Z ([the Siegel domain](/wiki/phase-space/modular-field/siegel-domain)), with the parametrization of #5 §C:

```text
Z = X + iY,   Y > 0

H_Z = [[ Y + XY⁻¹X ,  XY⁻¹ ],
       [ Y⁻¹X      ,  Y⁻¹  ]]
```

#11 claims det H = 1 for all of it, in §5 ("— machine-verified — persists across the whole modular family of §6") and in the Tier-1 list of §2 ("det H = 1 across the whole family"). The handoff describes the test as "det H = 1 off-vacuum" (`HANDOFF.md` §5). Battery test T2 draws one random symmetric X and one positive-definite Y at d = 4 and prints `PASS  T2 det H_Z = 1  [det=1.000000000000]` (`verify/battery.py`). One sample does not verify a statement about the whole family, so this wiki tags the family-wide statement [D], not [V] ([conflicts between sources](/wiki/history/documents/source-conflicts)).

**On the vacuum slice.** The [round-3](/wiki/method/review/round-3) referee's audit notes summarize the diag(g, g⁻¹) family as "max residuals 4.7e-15 (d=3), 8.4e-15 (d=4); det H = 1." The script prints `det H = 1 check: 2.2e-16` at d = 3 and at d = 4, and computes that line on one fixed member of the family, with g equal to twice the identity, not on the 2000 random samples (`review/round3/referee/step3.py`, family (a)).

## Corollary 2: no Kalb–Ramond analog

The off-diagonal block C of H is where double field theory's generalized metric carries its B-field, the antisymmetric Kalb–Ramond 2-form, alongside the metric g ([double field theory](/wiki/phase-space/born-geometry/double-field-theory)). Such metrics satisfy the η condition of the theorem. The ω condition forces C = 0, and with it B = 0. In Freidel, Leigh and Minic's form, quoted in #11 §5: "writing the η-compatible H in terms of (G, B), H is related to ω through a complex structure exactly when B vanishes [26S, §2.1]."

Round 3 checked this numerically on 2000 generalized metrics with a B-field at each of d = 3 and d = 4: "eta residual <= 7e-14 but omega residual >= 0.28 (d=3), 1.48 (d=4)" (audit notes, Step 3). Every sampled metric with a B-field fits η and misses ω.

"Stiffer" here means that the [generalized metric](/wiki/phase-space/born-geometry/born-structures) has fewer free components: double field theory's carries g and B, and with ω and η both rigid only g remains.

Under P2′ the off-diagonal block of H_Z is XY⁻¹ (#5 §C), built from the symmetric field X rather than from an antisymmetric one. #11 §7.1 makes the contrast: X is symmetric, "contrast [double field theory's] antisymmetric B-field: the symmetry type of the rigid pairing dictates the partner's spin" ([the symplectic partner of the graviton](/wiki/gravity/momentum-graviton/symplectic-partner)).

## Corollary 3: the slaved momentum metric

The lower-right block of H is the momentum-space metric. The [lab notebook](/wiki/history/documents/lab-notebook) describes the split: "On the x-tilted vacuum, H decomposes into a spacetime metric g_μν(x) and a momentum-space metric g̃^μν" (#1 §3). The theorem fixes that block as the inverse of the position block at every point, g̃ = g⁻¹: momentum-space geometry is determined by spacetime geometry and carries no degrees of freedom of its own.

[#13](/wiki/conjugate-relativity) builds its kinematics on this form: "The broken vacuum equips phase space with H = diag(g, g⁻¹) [D — compatibility theorem]: position space carries the metric g and momentum space its inverse. Each metric defines a null cone." (#13 §1; on the tag, see flag 30 in `review/wiki-build-flags.md`; [two causal cones](/wiki/conjugate-relativity/two-causal-cones)). It adds a refinement from the main program: "the dual cone is the causal structure of the *slaved* geometry g⁻¹; the independently dynamical part of momentum-space geometry is the massive field X, which modifies the dual cone only at short range in momentum [D — §7 of the checkpoint]." (#13 §1; on its citation of #11 §7, see flag 29 in `review/wiki-build-flags.md`.)

## The collision with the theory as documented [D — structural]

Corollary 3 contradicted the program as the lab notebook had built it. Calc note #5 §B, tagged "[D — structural]":

> Corollary 3 collides with the theory as documented. Under strict P2 (ω **and** η rigid):
>
> - The space of polarizations compatible with both structures (ω-Lagrangian *and* η-null) is **discrete** — the 2^d coordinate-type splittings, GL(d)-rigid. No Lagrangian Grassmannian, no Maslov circle, **no τ field**. The dark-energy sector as constructed contradicts P2.
> - With H = diag(g, g⁻¹), S_H is a functional of g alone: a pure metric theory. No momentum graviton, hence no geometric origin for the χ gate either.

The note's "discrete" is queried in flag 1 of `review/wiki-build-flags.md`. The note names the result Branch R, for rigid: "BBT reduces to GR + one bespoke SIDM model, with w ≡ −1 and the gate unexplained. On Branch R the program has no content of its own — and it is *already disfavored* if DESI's drift is real." Here BBT is Broken-Born theory (the program's earlier name), GR [general relativity](/wiki/gravity/spin-2-fields/general-relativity), SIDM [self-interacting dark matter](/wiki/dark-matter/halo-astrophysics/self-interacting-dark-matter), and DESI the [Dark Energy Spectroscopic Instrument](/wiki/cosmology/dark-energy/desi). The notebook's v0.3 addendum records the same finding: strict P2 eliminates "the Lagrangian Grassmannian, the Maslov circle, and hence the entire τ/dark-energy sector, while also slaving g̃ = g⁻¹ and removing any geometric origin for the χ gate. A theory with strict P2 is GR plus one bespoke SIDM model."

The way out was to stop fixing η. The [nontriviality theorem](/wiki/program/postulates/nontriviality-theorem) states that the program has content beyond Branch R if and only if η is emergent, and [P2′](/wiki/program/postulates/p2-prime) makes it so; the superseded postulate and Branch R are on [original P2](/wiki/program/postulates/original-p2). The dark-energy field τ that strict P2 removed lives on [the Lagrangian Grassmannian](/wiki/phase-space/modular-field/lagrangian-grassmannian) as [the Maslov phase](/wiki/phase-space/modular-field/maslov-phase).

## Under P2′: the vacuum slice

With only ω rigid, H can leave the block-diagonal form, and the theorem's solutions become one slice of the modular field. Calc note #5 §C: "At X = 0, H = diag(g, g⁻¹): the η-compatible locus of Theorem A is precisely the vacuum slice", and Re Z = X "is exactly the fluctuation that breaks η-compatibility" ([the modular field Z = X + iY](/wiki/phase-space/modular-field/modular-field-z)).

The three corollaries fare differently there:

- **det H = 1** is claimed for the whole family (#11 §5), checked at one point (T2), and tagged [D] here, as above.
- **The off-diagonal block** is XY⁻¹, the place where the momentum graviton enters ([the momentum graviton X](/wiki/gravity/momentum-graviton)).
- **g̃ = g⁻¹** holds on the slice X = 0. The withdrawn manuscript #14 puts it this way: "Consequently the baseline momentum-space geometry is slaved (g-tilde = g^-1, det H = 1), and any independent momentum-space geometry resides in the fluctuation X of the off-vacuum modular parameter Z = X + iY on Sp(2d,R)/U(d)" (#14 §1).

## Chat-only: the slaved layer is algebraic

The handoff lists among the results that exist only in the claude.ai conversation, not in any document: "**GR-vs-conjugate equation comparison:** slaved layer g̃ = g⁻¹ is algebraic (Einstein's equation does double duty); dual Newtonian limit = Yukawa in momentum = the gate; X-waves massive, 5 polarizations, frequency floor." (`HANDOFF.md` §4; GR is general relativity; [a range in momentum](/wiki/gravity/spin-2-fields/yukawa-forces#conjugate-special-relativity-a-range-in-momentum).) An algebraic relation gives g̃ no field equation of its own, so the equation that determines g determines g̃ as well. No document derives the comparison, and its status is conjecture ([two gravitational charges and the conjugate field equations (chat-only)](/wiki/gravity/momentum-graviton/chat-only-results); [conjectures](/wiki/status/conjectures)).

## Used by

- [P1: the phase-space arena](/wiki/program/postulates/p1-arena) — with η fixed as well, the momentum metric is slaved.
- [Original P2: both structures rigid (superseded)](/wiki/program/postulates/original-p2) — corollary 3 is what made strict P2 untenable.
- [The nontriviality theorem](/wiki/program/postulates/nontriviality-theorem) — content beyond general relativity iff η is emergent.
- [P2′: only the symplectic form is rigid](/wiki/program/postulates/p2-prime) — the repair; det H = 1 as the geometric face of ℏ-rigidity.
- [The modular field Z = X + iY](/wiki/phase-space/modular-field/modular-field-z) — on the vacuum slice the momentum metric is the slaved Y⁻¹ = g⁻¹.
- [The symplectic partner of the graviton is another graviton](/wiki/gravity/momentum-graviton/symplectic-partner) — corollary 2: with both pairings rigid, no B-field.
- [Two gravitational charges and the conjugate field equations (chat-only)](/wiki/gravity/momentum-graviton/chat-only-results) — the slaved layer g̃ = g⁻¹ as the documented counterpart.
- [Two causal cones](/wiki/conjugate-relativity/two-causal-cones) — the dual cone of the slaved momentum metric (see flag 30 in `review/wiki-build-flags.md`).
- [The cosmological constraint a·ã = 1](/wiki/cosmology/scale-factor-duality/cosmological-constraint) — another consequence of a fixed phase-space cell.

## Sources

- `papers/broken-born-checkpoint-v2.md` §5, §2, §7.1 — the corollaries in the current reference; the family-wide det H = 1 claim; X against the antisymmetric B-field.
- `review/round3/referee/audit-notes.md` Step 3, `review/round3/referee/step3.out` and `review/round3/referee/step3.py` family (a) — det H = 1 on the diag(g, g⁻¹) family, and the matrix the check uses; the B-field family.
- `papers/conjugate-special-relativity.md` §1 — the block form as two metrics with two cones.
- `HANDOFF.md` §2, §4, §5 — the ✓ on the theorem line; the chat-only remark on the slaved layer; T2 as "det H = 1 off-vacuum".
- `notes/debt1a-geometric-core.md` §A — the three corollaries, "[D — rigorous]".
- `notes/debt1a-geometric-core.md` §B — "Corollary 3 collides with the theory as documented"; Branch R; the repair.
- `notes/debt1a-geometric-core.md` §C, §F — H_Z and the vacuum slice X = 0; unimodularity as "the geometric face of ℏ-rigidity".
- `notes/broken-born-theory.md` §3, 'Addendum (v0.3, overnight)' — g and g̃ as the blocks of H; strict P2 as "GR plus one bespoke SIDM model".
- `notes/knot-dark-matter-standalone.md` §1 — momentum-space geometry resides in X.
- `verify/battery.py` T2 — det H_Z = 1 at one sampled Siegel point.
