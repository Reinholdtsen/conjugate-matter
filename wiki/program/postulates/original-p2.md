---
title: "Original P2: both structures rigid (superseded)"
weight: 20
status: superseded
description: "The first rigidity postulate froze both ω and η: no Maslov circle, no τ, and a theory collapsed to Branch R (general relativity plus one self-interacting dark-matter model)."
provenance: [P]
sources:
  - "notes/broken-born-theory.md §1"
  - "notes/broken-born-theory.md §2"
  - "notes/broken-born-theory.md §3"
  - "notes/broken-born-theory.md §4"
  - "notes/broken-born-theory.md §6"
  - "notes/broken-born-theory.md §11"
  - "notes/debt1a-geometric-core.md §A"
  - "notes/debt1a-geometric-core.md §B"
  - "notes/debt1a-geometric-core.md §E"
  - "notes/debt1a-geometric-core.md §F"
  - "papers/broken-born-checkpoint-v2.md §4"
  - "papers/broken-born-checkpoint-v2.md §5"
  - "papers/broken-born-checkpoint-v2.md §7.2"
  - "papers/broken-born-checkpoint-v2.md §10"
  - "papers/broken-born-checkpoint-v2.md §13 row 9"
  - "notes/broken-born-theory.md 'Addendum (v0.3)'"
  - "notes/broken-born-theory.md 'Addendum (v0.4)'"
  - "CLAUDE.md 'Since the handoff'"
  - "verify/battery.py T1"
  - "review/wiki-build-flags.md items 1, 10, 23, 25"
  - "review/wiki-build-checks/verifier_null_lagrangians.py"
---

*The original P2 was the lab notebook's second axiom: of the three structures on phase space, the [symplectic form](/wiki/phase-space/reciprocity/symplectic-form) ω and the [neutral metric](/wiki/phase-space/born-geometry/born-structures) η are fixed background, and only the generalized metric H carries degrees of freedom. It was meant to express the constancy of Planck's constant, and the notebook gave it three further jobs: removing a would-be second graviton, fixing the relation between the two cosmological scale factors, and supplying the dark-energy field's potential. The program's geometry showed that it fixed too much. With both structures fixed, H is forced into a rigid block form, the [polarizations](/wiki/phase-space/reciprocity/lagrangian-polarizations) (position–momentum splittings) compatible with both include no circle for the dark-energy field to live on, and the theory reduces to [general relativity](/wiki/gravity/spin-2-fields/general-relativity) plus one bespoke model of self-interacting dark matter. It was replaced by [P2′](/wiki/program/postulates/p2-prime), which fixes ω alone. Of its three jobs, one was reversed, one survives from ω alone, and one became an open problem.*

**Status:** Superseded by P2′ — [P] as stated; its reduction to "Branch R" is [D — structural] (`notes/debt1a-geometric-core.md` §B) — the replacement was forced by [the nontriviality theorem](/wiki/program/postulates/nontriviality-theorem) ([#11](/wiki/history/documents/checkpoint) §4–§5; lab notebook addendum v0.3). Listed in [superseded statements](/wiki/status/superseded).

## The statement

```text
P2 (Rigidity of ℏ). ω and η are non-dynamical; only H carries degrees
of freedom. Physically: the symplectic structure is the constancy of
ℏ — phase-space cells do not stretch.                              [P]
```

This is the lab notebook's v0.1 text (#1 §1, September 2026). A non-dynamical structure is fixed background: it has no equation of motion and takes the same value in every state of the theory, as the Minkowski metric does in [special relativity](/wiki/conjugate-relativity/special-relativity) [T]. Of the three structures in the notebook's arena ([P1](/wiki/program/postulates/p1-arena) in its v0.1 form), P2 left only H free to vary. Its physical reading tied ω to Planck's constant. In the notebook's cosmology section, "Rigidity of ω means the comoving phase-space cell has fixed volume" (#1 §6), so holding ω fixed is the statement that ℏ does not change. The physical reading concerns ω; the axiom held η fixed as well.

## The triple duty

The notebook gave P2 three further roles: "This single postulate does triple duty below: it kills the would-be second graviton (no Boulware–Deser ghost, §6), it enforces the cosmological constraint aã = const (§7), and it supplies the explicit breaking that gives the dark-energy field its potential (§5)." (#1 §1). Two of the section numbers in that sentence do not match the notebook (see flags 10 and 25 in `review/wiki-build-flags.md`; [conflicts between sources](/wiki/history/documents/source-conflicts#pointers-inside-the-lab-notebook), entry C21): the constraint is derived in §6, not §7, and the potential's origin is stated in §3, not §5. The ghost claim's "§6" can stand, since §6 says the dual sector is "not a ghost — ã was never independent", but the claim itself is made in §4, 'Ghost accounting'. All three are cited here by heading.

1. **No second graviton** (#1 §4, 'Ghost accounting'): "There is no second independent metric: g̃'s cosmological mode is eliminated by the P2 constraint (§7), so no Boulware–Deser sector arises in minisuperspace. **[D]** The statement for full inhomogeneous H is open. **[O]**" Here g̃ is the momentum-space metric, and the notebook's "(§7)" is again its §6 (see flag 25 in `review/wiki-build-flags.md`). A Boulware–Deser ghost is the extra, negative-energy mode that generic theories of a massive or second metric carry ([the Fierz–Pauli mass term and the Boulware–Deser ghost](/wiki/gravity/spin-2-fields/fierz-pauli)) [T].
2. **The cosmological constraint** (#1 §6, 'The constraint from P2'): with x-space scale factor a and p-space scale factor ã, "each mode occupies (aã)³ × (comoving cell) = ℏ³. Hence aã = const ≡ 1. This is not an extra assumption; it is the statement that ℏ does not run."
3. **The dark-energy potential** (#1 §3, 'Polarization sector'): the potential V(τ) = V₀[1 + cos(τ/f)] of the dark-energy field τ has a periodicity "forced by the Maslov topology **[D]**; its *existence* comes from the explicit breaking of Grassmannian rotations by the rigid ω (P2) — the rigidity is the 'instanton' that tilts the circle. Its *magnitude* V₀ is a free parameter here. **[P/O]**"

## How the program's geometry rejected it

### The compatibility theorem

Groundwork on [Debt 1](/wiki/history/debts), the field equation for H (#1 §11, open problem 1), produced the result that settled P2 (#1 'Addendum (v0.3)'; the overnight [Debt-1 note](/wiki/history/documents/debt-1-notes), #5). With ω and η both in standard form, "the positive generalized metrics H satisfying the full Born algebra — (η⁻¹H)² = +1 **and** (ω⁻¹H)² = −1 — are exactly"

```text
H = diag(g, g⁻¹),     g ∈ Sym⁺(d)                                    (#5 §A)
```

The proof is three lines of block algebra (#5 §A; #11 §5):

```text
write H = [[A, C], [Cᵀ, B]]
(2,1) blocks of the two conditions:   ACᵀ + CA = 0   and   CA − ACᵀ = 0   ⇒   ACᵀ = 0
positivity makes A invertible         ⇒   C = 0
diagonal blocks:                      BA = AB = 1   ⇒   B = A⁻¹
```

This is [the compatibility theorem](/wiki/phase-space/born-geometry/compatibility-theorem), [T][V] since v2.1: the statement is credited to [Freidel, Leigh and Minic](/wiki/phase-space/reciprocity/broken-born-duality) [26S, §2.1], and the block proof and its machine check (battery test T1, [the verification battery](/wiki/method/verification/battery)) are the program's (#11 §5).

Its corollaries (#5 §A; [the corollaries](/wiki/phase-space/born-geometry/compatibility-corollaries)):

- "**det H = 1 identically.** The generalized metric is unimodular: phase-space volume is not a dynamical field."
- "**No Kalb–Ramond analog.** The off-diagonal block — DFT's B-field — is frozen out by the extra symplectic compatibility. Born geometry with both structures rigid is *stiffer* than DFT." (DFT: [double field theory](/wiki/phase-space/born-geometry/double-field-theory).)
- "**The momentum metric is slaved: g̃ = g⁻¹ pointwise.** No independent momentum-space geometry survives."

### The collision: Branch R

"Corollary 3 collides with the theory as documented" (#5 §B). The v0.1 notebook had a dark-energy field and a momentum-space gate for dark matter; under strict P2 the first cannot exist and the second has no geometric origin. #5 §B finds:

- "The space of polarizations compatible with both structures (ω-Lagrangian *and* η-null) is **discrete** — the 2^d coordinate-type splittings, GL(d)-rigid. No Lagrangian Grassmannian, no Maslov circle, **no τ field**. The dark-energy sector as constructed contradicts P2." (On "discrete", see flag 1 in `review/wiki-build-flags.md`.) The program's dark-energy field τ is the angle around the Maslov circle of [the Lagrangian Grassmannian](/wiki/phase-space/modular-field/lagrangian-grassmannian), the continuous space of all polarizations ([τ as the Maslov phase](/wiki/phase-space/modular-field/maslov-phase)). In #5's reading the compatible polarizations form a discrete set, which has no such circle. Flag 1 finds that for d ≥ 2 they form continuous families V ⊕ V^⊥ instead (V a subspace of the position directions, V^⊥ its orthogonal complement placed in the momentum directions), but the Maslov phase det² is constant on each family, so none of them winds around the Maslov circle and the conclusion stands (check: `review/wiki-build-checks/verifier_null_lagrangians.py`; awaiting Paul's ruling).
- "With H = diag(g, g⁻¹), S_H is a functional of g alone: a pure metric theory. No momentum graviton, hence no geometric origin for the χ gate either." S_H is the geometric action of H. If g is the only free field in H, there is no second tensor to act as the [momentum graviton](/wiki/gravity/momentum-graviton), and the mechanism the same note finds for the dark-matter [velocity gate](/wiki/dark-matter/conjugate-matter/velocity-gate), exchange of that graviton (#5 §E), has nothing to exchange.

The note names the result:

> Call this **Branch R** (rigid): BBT reduces to GR + one bespoke SIDM model, with w ≡ −1 and the gate unexplained. On Branch R the program has no content of its own — and it is *already disfavored* if DESI's drift is real. (#5 §B)

BBT is the Broken-Born program, GR general relativity, and SIDM [self-interacting dark matter](/wiki/dark-matter/halo-astrophysics/self-interacting-dark-matter). w ≡ −1 is the equation of state of a [cosmological constant](/wiki/cosmology/dark-energy/cosmological-constant) [T], all that remains of dark energy without τ. The dark-matter model is "bespoke" in that its velocity gate would be postulated for that one model and "unexplained" by any geometry. DESI is the Dark Energy Spectroscopic Instrument ([DESI](/wiki/cosmology/dark-energy/desi)), whose hints of evolving dark energy are the "drift". Since v2.1, #11 §10 records that DESI's second data release favours a crossing below w = −1 above redshift z ≃ 0.4, a reading that is against the program's own dark-energy sector as well ([DESI DR2's phantom crossing](/wiki/cosmology/dark-energy/desi-dr2-phantom-crossing)).

## The replacement

The repair keeps ω fixed and lets η vary: "Freeze ω only — that is genuinely ℏ — and let **η be emergent: the order parameter itself.**" (#5 §B). The lab notebook's v0.3 addendum records it: "**P2 is therefore replaced by P2′:** only ω is rigid (that is ℏ); **η is emergent — the order parameter itself**, η = HJ, with the real structure J chosen spontaneously from U(d)/O(d) = Λ(d)." The same addendum sums up the strict version: "A theory with strict P2 is GR plus one bespoke SIDM model."

The note presents the step as forced, under the name "Program-nontriviality theorem: BBT has content beyond GR + SIDM **iff** η is emergent. P2 → P2′ is not optional." #11 §4 carries the same verdict into the current postulate list: "the correction from the original P2 is *forced*". The argument is on [the nontriviality theorem](/wiki/program/postulates/nontriviality-theorem) page, and the corrected axiom is [P2′](/wiki/program/postulates/p2-prime). The program paper v1 (#9) and the checkpoint (#11) state only P2′.

## What became of the triple duty

1. **No second graviton — reversed.** With η emergent, the real part X of [the modular field Z = X + iY](/wiki/phase-space/modular-field/modular-field-z) carries its own gauge symmetry, and the v0.4 addendum found that "Its local gauge structure δX_μν = ∂_(μλ_ν) makes it a *second graviton*". Two interacting massless gravitons are excluded by a no-go theorem ([the multi-graviton no-go](/wiki/gravity/spin-2-fields/multi-graviton-no-go)), so "The only exit: the polarization selection (η-emergence) spontaneously breaks the dual diffeomorphisms, X eats the four Goldstones and becomes a **massive spin-2**" (#1 'Addendum (v0.4)'; [why X must be massive](/wiki/gravity/momentum-graviton/forcing-chain)). Ghost freedom now comes from the formulation, not from rigidity: the frame-tier couplings are "the Hinterbichler–Rosen class [12†], ghost-free by construction" (#11 §7.2; [the frame tier](/wiki/gravity/tuning-test/frame-tier)).
2. **The cosmological constraint — survives from ω alone.** #11 §10: "ω-rigidity fixes the comoving phase-space cell: a·ã = 1 (ℏ does not run) — the |Z| = 1 self-dual locus." (On the |Z| = 1 locus, see flag 23 in `review/wiki-build-flags.md`.) The notebook's own derivation in §6, quoted above, already used only the rigidity of ω. See [the cosmological constraint a·ã = 1](/wiki/cosmology/scale-factor-duality/cosmological-constraint).
3. **The dark-energy potential — open.** The Debt-1 note lists among its open items "the origin of τ's potential under P2′ (what explicitly breaks Λ(d) rotations — candidate: the section choice itself, or matter loops)" (#5 §F, item 3). The [toy models](/wiki/symmetry-breaking/toy-models) of v2.2 found that ω alone leaves the polarization as a free angle: "A definite polarization needs a ρ-preserving potential on that angle — a rigid, unordered pair of axes, so more structure than ω alone, though less than a rigid η" (#11 §4). A derivation of that potential is one of the open ends listed in `CLAUDE.md`. See [the origin of the ρ-preserving potential](/wiki/symmetry-breaking/rho-preserving-potential).

## Where the old axiom still reads as live

- The body of the lab notebook was never edited. Strict P2 still reads as in force in its §1, and its §3 writes the geometric action "with ω, η frozen (P2)" ([the v0.1 action](/wiki/gravity/tuning-test/geometric-action)). The v0.3 addendum records the replacement; #9 and #11 supersede the body ([the lab notebook](/wiki/history/documents/lab-notebook)).
- The notebook's §2 breaking pattern, ℤ₄ → ℤ₂ with ℤ₂ = {1, ρ²}, assumed strict P2. #11 v2.2 replaces the discrete picture with a [Goldstone angle](/wiki/symmetry-breaking/goldstone-angle), but #11 §13 row 9 still rests its photon-dispersion prediction on ρ², a rationale written out only in #1 ([the order parameter](/wiki/symmetry-breaking/order-parameter); [row 9](/wiki/predictions/photon-dispersion)).

## Sources

- `notes/broken-born-theory.md` §1 — the statement and its "triple duty"; §2 — the ℤ₄ → ℤ₂ breaking pattern; §3 — the potential attributed to the rigid ω, and the action with ω, η frozen; §4 — 'Ghost accounting'; §6 — the constraint from the rigidity of ω; §11 — Debt 1 as open problem 1
- `notes/broken-born-theory.md` 'Addendum (v0.3)' — the replacement; 'Addendum (v0.4)' — X as a second graviton, made massive
- `notes/debt1a-geometric-core.md` §A — the compatibility theorem and its corollaries; §B — the inconsistency, Branch R, the repair and the nontriviality theorem; §E — the gate as X exchange; §F — the potential's origin under P2′ as an open item
- `papers/broken-born-checkpoint-v2.md` §4–§5 — the current record of the forced correction and the theorem's attribution; §7.2 — frame-tier ghost freedom; §10 — the constraint from ω-rigidity and DESI's second data release; §13 row 9 — the remaining reliance on ρ²
- `CLAUDE.md` 'Since the handoff' — the derivation of the ρ-preserving potential as an open end
- `verify/battery.py` T1 — the compatibility-theorem checks
- `review/wiki-build-flags.md` items 1, 10, 23, 25 — the query on "discrete" (check: `review/wiki-build-checks/verifier_null_lagrangians.py`); the notebook's section pointers for the potential and the constraint; the identification of a·ã = 1 with the |Z| = 1 locus
