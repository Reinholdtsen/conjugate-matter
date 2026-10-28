---
title: "The geometric action S_H and the v0.1 action (superseded)"
weight: 60
status: superseded
description: "The lab notebook's action S = S_H + S_τ + S_x + S_p + S_mix, its Einstein-like S_H with ω and η frozen, and its argument against a ghost — superseded by P2′, and the starting point of open problem 1."
provenance: [D]
sources:
  - "notes/broken-born-theory.md §3"
  - "notes/broken-born-theory.md §4"
  - "notes/broken-born-theory.md §1"
  - "notes/broken-born-theory.md §2"
  - "notes/broken-born-theory.md §6"
  - "notes/broken-born-theory.md §11"
  - "notes/broken-born-theory.md 'Addendum (v0.3, overnight)'"
  - "notes/broken-born-theory.md 'Addendum (v0.4)'"
  - "notes/broken-born-theory.md 'Addendum (v0.5)'"
  - "papers/broken-born-checkpoint-v2.md §4"
  - "papers/broken-born-checkpoint-v2.md §5"
  - "papers/broken-born-checkpoint-v2.md §7.2"
  - "papers/broken-born-checkpoint-v2.md §8"
  - "papers/broken-born-checkpoint-v2.md §10"
  - "papers/broken-born-checkpoint-v2.md §14 item 1"
  - "notes/debt1a-geometric-core.md §B"
  - "notes/debt1a-geometric-core.md §C"
  - "notes/debt1a-geometric-core.md §D"
  - "notes/debt1a-geometric-core.md §F"
  - "notes/debt1a-ii-X-classification.md §1"
  - "notes/debt3b-wave-island.md 'Next'"
  - "notes/debt3c-ufd-endpoint.md 'Next: Debt 1, Chunk 1a'"
  - "review/wiki-build-flags.md items 1, 25, 27"
  - "review/wiki-build-flags.md items 27 (addendum), 49"
  - "notes/closed-universe.md §2"
  - "notes/closed-universe.md §7"
---

*The v0.1 action is the complete action written in the program's [lab notebook](/wiki/history/documents/lab-notebook) in September 2026: a sum of five terms, for the phase-space geometry, the [dark-energy angle τ](/wiki/phase-space/modular-field/maslov-phase), the Standard Model, [conjugate matter](/wiki/dark-matter/conjugate-matter), and an unspecified mixing term. Its geometric term S_H is an Einstein-like action for the phase-space metric H, built from the curvature of [the Born connection](/wiki/phase-space/born-geometry/born-connection) and written with both the [symplectic form](/wiki/phase-space/reciprocity/symplectic-form) ω and the [neutral metric η](/wiki/phase-space/born-geometry/born-structures) frozen, as [the original P2](/wiki/program/postulates/original-p2) required. From that rigidity the notebook argued that no second independent metric, and so no [Boulware–Deser ghost](/wiki/gravity/spin-2-fields/fierz-pauli), could arise. Both points were later overturned: [postulate P2′](/wiki/program/postulates/p2-prime) made η emergent, the [momentum graviton X](/wiki/gravity/momentum-graviton) was found to be a [second graviton](/wiki/gravity/momentum-graviton/dual-diffeomorphisms), and [ghost freedom](/wiki/gravity/spin-2-fields/ghosts) now comes from [the frame tier](/wiki/gravity/tuning-test/frame-tier). This form of the action is therefore superseded, and [checkpoint #11](/wiki/history/documents/checkpoint) writes no full action. The name S_H survives as the action from which [open problem 1](/wiki/gravity/tuning-test/wedge-reduction) asks for the ghost-free potential to be derived.*

**Status:** Superseded — S_H is [D, schematic] and the argument against a ghost is [D] with an [O] remainder, in `notes/broken-born-theory.md` §3–§4 — superseded by P2′ (the notebook's v0.3 addendum; #11 §4–§5) and by [calc notes #5–#8](/wiki/history/documents/debt-1-notes). Listed in [superseded statements](/wiki/status/superseded).

## The action as written (v0.1)

### The five terms

The lab notebook's §3 ("Action") writes the whole theory as one action:

```text
S = S_H + S_τ + S_x[SM; g] + S_p[χ; g, g̃] + S_mix          (#1 §3)
```

Here g is the spacetime metric, g̃ the momentum-space metric and χ conjugate matter. The terms, in the notebook's words and tags:

- **S_H, the geometric sector**, an action for the phase-space metric H [D, schematic]; set out below.
- **S_τ, the polarization sector**: "S_τ = ∫ √(−g) [½(∂τ)² − V(τ)]" with "V(τ) = V₀[1 + cos(τ/f)]". "The potential's *periodicity* is forced by the Maslov topology **[D]**; its *existence* comes from the explicit breaking of Grassmannian rotations by the rigid ω (P2) — the rigidity is the 'instanton' that tilts the circle. Its *magnitude* V₀ is a free parameter here. **[P/O]**" τ is the dark-energy field, the angle on the Maslov circle ([τ as the Maslov phase](/wiki/phase-space/modular-field/maslov-phase)).
- **S_x, the ordinary sector**: "S_x is the Standard Model minimally coupled to g. Nothing is modified. **[P4]**" ([P4](/wiki/program/postulates/p4-polarized-matter)).
- **S_p, the conjugate sector**: χ "propagates on g — it gravitates exactly like ordinary matter — but its self-interaction is routed through the g̃ block", with a postulated gate in the incoming relative momentum of a colliding pair ([the velocity gate](/wiki/dark-matter/conjugate-matter/velocity-gate)). "Deriving the precise gate shape from S_H + S_mix is open **[O]**".
- **S_mix, a mixing term**, which the notebook names but never writes down. It appears again only where the notebook asks for the gate shape to come "from S_H + S_mix" (#1 §3, §11 item 2).

### The geometric term S_H [D, schematic]

```text
S_H = ½ M_B² ∫_Σ √|H| R_B[H]        over the section Σ, with ω, η frozen (P2)
```

The ingredients:

- **R_B[H]** is the curvature of the Born connection, the unique connection compatible with all three structures (ω, η, H), whose existence and uniqueness the notebook takes from Freidel, Rudolph and Svoboda [T] (#1 §2; [the Born connection](/wiki/phase-space/born-geometry/born-connection)). "Its curvature R_B[H] is therefore well-defined, and a diffeomorphism-style invariant action for H can be written" (#1 §2).
- **Σ, the section.** "Field dependence is restricted to a Lagrangian leaf by a section condition, as in double field theory; consistency of the section condition on general backgrounds is open there and open here. **[O]**" (#1 §2; [the section condition](/wiki/symmetry-breaking/section-condition)).
- **M_B** is the mass scale of the geometric sector.
- **"ω, η frozen (P2)."** Only H carries degrees of freedom, as [the original P2](/wiki/program/postulates/original-p2) states.

The form copies general relativity, whose Einstein–Hilbert action is the integral of √|g| R over spacetime [T] ([general relativity and the graviton](/wiki/gravity/spin-2-fields/general-relativity)), with the phase-space metric and its Born curvature in place of g and R. The notebook's claim about its content: "On the x-tilted vacuum, H decomposes into a spacetime metric g_μν(x) and a momentum-space metric g̃^μν; the g-block reproduces the Einstein–Hilbert action with M_P fixed by M_B and the section volume. **[D, schematic]**" (#1 §3). The tag marks the reduction as sketched rather than carried out. The notebook's first open problem records how far it went: "The action exists (Born connection **[T]**), but solutions, the section condition on curved backgrounds, and the full ghost analysis do not. **[O]**" (#1 §11 item 1).

## The v0.1 argument against a ghost

A second dynamical metric beside g raises the question of the Boulware–Deser ghost, the extra negative-energy mode that generic theories of two metrics, or of a massive graviton, carry [T] ([the Fierz–Pauli mass term and the Boulware–Deser ghost](/wiki/gravity/spin-2-fields/fierz-pauli)). The notebook's answer, under the heading "Ghost accounting" (#1 §4):

> There is no second independent metric: g̃'s cosmological mode is eliminated by the P2 constraint (§7), so no Boulware–Deser sector arises in minisuperspace. **[D]** The statement for full inhomogeneous H is open. **[O]**

The constraint is [a·ã = 1](/wiki/cosmology/scale-factor-duality/cosmological-constraint) between the scale factors of position and momentum space, which the notebook derives from the rigidity of ω: "This is not an extra assumption; it is the statement that ℏ does not run" (#1 §6, "Cosmology I"). In [minisuperspace](/wiki/cosmology/scale-factor-duality/friedmann-cosmology), the homogeneous cosmological sector, substituting ã = 1/a into the dual Einstein–Hilbert term makes the dual gravitational sector "not a new fluid and not a ghost — ã was never independent — but a stiff-like (a⁻⁶) modification of the effective Planck mass" (#1 §6; [an effective Planck mass](/wiki/gravity/spin-2-fields/planck-units#an-effective-planck-mass)). #1 §3 reduces S_H only for the g-block, "[D, schematic]", and no document derives the dual Einstein–Hilbert term from S_H, so the a⁻⁶ step it gives tests a postulate (flag 49; [the dual frame](/wiki/cosmology/scale-factor-duality/closed-universe#the-dual-frame-what-closure-fixes-and-what-it-does-not)). The postulate itself had promised this: P2 "kills the would-be second graviton (no Boulware–Deser ghost, §6)" (#1 §1).

Two of the notebook's section pointers bear on this argument. The "(§7)" of the passage quoted above points to the constraint, which the notebook derives in §6 (see flag 25 in `review/wiki-build-flags.md`). P2's "§6", given for "no Boulware–Deser ghost", is a fair pointer: §6 is where the minisuperspace result quoted above finds the dual sector "not a ghost", while the argument itself is the "Ghost accounting" of §4. This wiki cites the notebook by heading ([the original P2](/wiki/program/postulates/original-p2); [conflicts between the documents](/wiki/history/documents/source-conflicts)).

## Why the form is superseded

### Strict P2 empties S_H

The first Debt-1 calculation found that freezing both ω and η leaves H no freedom beyond the spacetime metric. By [the compatibility theorem](/wiki/phase-space/born-geometry/compatibility-theorem), the only positive H compatible with both are H = diag(g, g⁻¹), so "S_H is a functional of g alone: a pure metric theory. No momentum graviton, hence no geometric origin for the χ gate either" (calc note #5 §B; [the Debt-1 calc notes](/wiki/history/documents/debt-1-notes)). #11 states the consequence as [the nontriviality theorem](/wiki/program/postulates/nontriviality-theorem): "Under strict P2 the compatible polarizations are discrete, so no Grassmannian, no Maslov circle, no dark-energy field, and S_H is a functional of g alone: **nontriviality theorem** — the program has content iff η is emergent. Hence P2 → P2′" (#11 §5; on "discrete", see flag 1 in `review/wiki-build-flags.md`).

P2′ keeps only ω rigid: "The neutral metric η is emergent — the order parameter" (#11 §4). An action written "with ω, η frozen (P2)" is written under the postulate that P2′ replaced. The notebook's v0.3 addendum records the replacement; the body of the notebook was never edited, so §3 still reads as if strict P2 were in force ([the lab notebook](/wiki/history/documents/lab-notebook)).

### The second graviton

With η emergent, the real part X of [the modular field](/wiki/phase-space/modular-field/modular-field-z) Z = X + iY carries momentum-space geometry, and the v0.4 addendum found that "Its local gauge structure δX_μν = ∂_(μλ_ν) makes it a *second graviton*". Two interacting massless gravitons are inconsistent, so X must be massive ([why X must be massive](/wiki/gravity/momentum-graviton/forcing-chain)). The "no second independent metric" of #1 §4 is reversed. Ghost freedom no longer follows from rigidity; it follows from writing X's mass term in frame variables, where the frame-tier couplings are "the Hinterbichler–Rosen class [12†], ghost-free by construction" (#11 §7.2; notebook 'Addendum (v0.5)'; [the verdict: a conditional pass](/wiki/gravity/tuning-test/conditional-pass)).

### The route that was planned, and the one taken

At the end of Debt 3 the next step was to be a linearization of S_H. Calc note #3: "**Then Chunk 1a** (large): linearize S_H on the broken vacuum; leaning on the known linearized-DFT spectrum, identify propagating modes and check quadratic-order ghost freedom. Born's debt, first installment." (`notes/debt3b-wave-island.md` 'Next'). DFT is double field theory ([double field theory](/wiki/phase-space/born-geometry/double-field-theory)). Calc note #4 sub-planned it:

> Linearize S_H on the broken vacuum. Sub-plan: (1a-i) mode content at quadratic order on flat background, importing the known linearized-DFT spectrum [T: graviton + two-form + dilaton]; (1a-ii) ghost check of the quadratic action with ω, η frozen; (1a-iii) extract the dynamical equation for the g̃-block — Born's debt, first direct installment. This is the heaviest chunk; expect subdivision.

(`notes/debt3c-ufd-endpoint.md` 'Next: Debt 1, Chunk 1a'.) The notes that carried out Debt 1 are titled Chunk A to Chunk A-iv (calc notes #5 to #8), and they did not follow this plan. The first of them found the inconsistency of the frozen-η setting and made η emergent (#5 §B). It then defined a different decisive computation, "expand the generalized curvature scalar of (ω, H_Z) to quadratic order in X about X = 0 on the section, with ω-generalized diffeomorphisms as the gauge symmetry", and marked it "Not completed tonight" (#5 §D). No later document reports that expansion. Calc notes #6 to #8 settled the character of X by symmetry and consistency arguments and by [the tuning test](/wiki/gravity/tuning-test) instead.

## What survives

- **S_H, as the named starting point of open problem 1.** After P2′ the notes keep the symbol for an action built from ω and H alone: "Constant shifts of X are **exact symmetries** of any S_H built from (ω, H)" (#6 §1), and "Born's debt, restated exactly: *the field equation for momentum-space geometry is the Re Z sector of S_H*" (#5 §C). No document writes such an action out. #11 §14 item 1 asks for the ghost-free potential to be derived from it: "First-principles reduction of the frame-tier wedge sector from S_H (class selected, not derived) [O]" ([Open: deriving the wedge sector from S_H (OP1)](/wiki/gravity/tuning-test/wedge-reduction)). Whether the Born connection, on which the v0.1 form rests, is still unique when only ω and H are fundamental is also open (#5 §F item 5; [the Born connection](/wiki/phase-space/born-geometry/born-connection)).
- **S_τ's potential, with a new origin question.** #11 §10 keeps "V = V₀[1 + cos(τ/f)], periodicity by topology" ([τ as quintessence](/wiki/cosmology/dark-energy/tau-quintessence)). The v0.1 origin of the potential, the rigid ω tilting the circle, has not survived. Calc note #5 reopened it as "what explicitly breaks Λ(d) rotations" (#5 §F item 3), and [the toy models](/wiki/symmetry-breaking/toy-models) showed that with only ω rigid the polarization is a [Goldstone angle](/wiki/symmetry-breaking/goldstone-angle), so that "A definite polarization needs a ρ-preserving potential on that angle" (#11 §4; [Open: the origin of the ρ-preserving potential](/wiki/symmetry-breaking/rho-preserving-potential)). The documents also disagree, without resolution, on the sign this potential must take for the turnaround ([Open: the sign of V(τ) and the turnaround](/wiki/cosmology/dark-energy/potential-sign); see flag 27 in `review/wiki-build-flags.md`, whose addendum finds that in a closed universe the turnaround happens with V ≥ 0, [a closed Comatter universe](/wiki/cosmology/scale-factor-duality/closed-universe)).
- **S_x, as postulate P4**, taken strictly since #11 v2.1 ([P4](/wiki/program/postulates/p4-polarized-matter)).
- **S_p's gate, with a mechanism.** The gate is now delivered "by X-exchange between dual-stress bilinears", "[D — mechanism; shape [O]]" (#11 §8; [the gate mechanism](/wiki/dark-matter/conjugate-matter/gate-mechanism)). Its shape, which the notebook hoped to derive "from S_H + S_mix", is open problem 4 ([Open: the gate shape (OP4)](/wiki/dark-matter/conjugate-matter/gate-shape)).
- **S_mix** was never written, and no later document uses it.

## Sources

- `notes/broken-born-theory.md` §3 — the v0.1 action, S_H [D, schematic], S_τ, S_x and S_p; §4 — "Ghost accounting"; §1 — P2 and its promise of no second graviton; §2 — the Born connection, R_B[H] and the section condition; §6 — the constraint a·ã = 1 and minisuperspace; §11 — the field equation for H as the first open problem, and the gate shape from S_H + S_mix.
- `notes/broken-born-theory.md` 'Addendum (v0.3, overnight)', 'Addendum (v0.4)', 'Addendum (v0.5)' — the replacement of P2, the second graviton, the frame tier.
- `papers/broken-born-checkpoint-v2.md` §4, §5 — P2′ and the nontriviality theorem; §7.2 — frame-tier ghost freedom; §8 — the gate mechanism; §10 — the τ potential; §14 item 1 — the open derivation from S_H.
- `notes/debt1a-geometric-core.md` §B — S_H reduced to g under strict P2; §C — Born's debt as the Re Z sector of S_H; §D — the decisive computation, not completed; §F — the origin of τ's potential reopened, and connection uniqueness for (ω, H).
- `notes/debt1a-ii-X-classification.md` §1 — S_H built from (ω, H) and the shift symmetry.
- `notes/debt3b-wave-island.md` 'Next' — the planned Chunk 1a.
- `notes/debt3c-ufd-endpoint.md` 'Next: Debt 1, Chunk 1a' — its sub-plan with ω and η frozen.
- `review/wiki-build-flags.md` items 1, 25, 27 — item 1: the η-null polarizations called "discrete"; item 25: #1's pointer to its §7 for the cosmological constraint; item 27: the sign of V(τ) that the turnaround needs, with its addendum on the closed turnaround; awaiting Paul's ruling. Item 49: the dual Einstein–Hilbert term, derived from S_H in no document.
- `notes/closed-universe.md` §2 — the turnaround in a closed universe with V ≥ 0; §7 — the dual term underived
