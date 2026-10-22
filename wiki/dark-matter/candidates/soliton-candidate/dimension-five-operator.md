---
title: "Obituary: Planck-suppressed adjoint mixing"
weight: 130
status: dead
description: "The operator Φ^a F^a B/M_* exists in the literature (Baumgart's footnote, ruling 8), but its O(1)-at-Planck coefficient is unsupported and its sources need bi-charged states that P4 excludes."
sources:
  - "review/round3-adjudication.md 'Rulings' 7–8"
  - "review/round3-adjudication.md 'Decisions' 1"
  - "review/round3-adjudication.md 'Pre-registration scored'"
  - "review/round3-adjudication.md 'What survives v3'"
  - "review/round3/referee/audit-notes.md Step 1"
  - "review/round3/referee/audit-notes.md Step 2"
  - "review/round3/referee/audit-notes.md Step 4(a)"
  - "review/round3/referee/audit-notes.md Step 4(b)"
  - "review/round3/referee/step2a.out"
  - "review/round3-preregistration.md 'Predictions'"
  - "review/v3-worklog.md 'Round-2 pending list'"
  - "notes/knot-dark-matter-standalone.md §2"
  - "notes/knot-dark-matter-standalone.md §4"
  - "notes/knot-dark-matter-standalone.md §5"
  - "notes/knot-dark-matter-standalone.md §6"
  - "papers/broken-born-checkpoint-v2.md §4"
  - "HANDOFF.md §6"
---

*Planck-suppressed adjoint mixing was #14 v3's estimate of how strongly its hidden photon would mix with ours. The hidden Higgs field Φ permits a gauge-invariant interaction Φ^a F^a_μν B^μν / M_\*, which links the hidden field strength to the field strength of our hypercharge; once Φ takes its vacuum value v, it produces a kinetic mixing ε ~ v/M_\*. v3 assumed the operator appears with a coefficient of order one at the Planck scale, which gives ε ~ 10⁻⁷–10⁻⁶. The [round-3 review](/wiki/method/review/round-3) found no source for that assumption: every paper that derives the operator obtains it at one loop from particles charged under both forces, which the manuscript's own sector separation excludes, and the estimate those papers give is three orders of magnitude smaller. The estimate is dead, and the program then took sector separation strictly.*

**Status:** Dead — round-3 ruling 7, upheld: the "O(1) coefficient at the Planck scale" is unsupported, and "the literature generates it at one loop from bi-charged states, which sector separation forbids" ([round-3 verdict and rulings](/wiki/method/review/round-3/rulings)). The operator itself exists: ruling 8 overturned the referee's claim that a cited paper lacked it. Decision 1 replaced the estimate with strict sector separation ([P4](/wiki/program/postulates/p4-polarized-matter); [round-3 decisions](/wiki/method/review/round-3/decisions)). Home: [the soliton candidate](/wiki/dark-matter/candidates/soliton-candidate); listed in [the graveyard](/wiki/status/graveyard).

## What was claimed

### The operator

The withdrawn manuscript [#14](/wiki/dark-matter/candidates/soliton-candidate) broke a hidden SU(2)_d to U(1)_d with a real scalar Φ in the adjoint representation ([Obituary: the hidden SU(2) → U(1) proposal](/wiki/dark-matter/candidates/soliton-candidate/hidden-sector)). A non-abelian group has no gauge-invariant field strength of its own to mix with ours, so the renormalizable [kinetic mixing](/wiki/dark-matter/candidates/soliton-candidate/kinetic-mixing) term does not exist for SU(2)_d [T]. #14 §2(b) gave the next possibility:

> (b) A dimension-5 operator. Phi^a F^a_mu-nu B^mu-nu / M_* is gauge invariant and gives epsilon ~ v/M_* once Phi condenses [10]. For an O(1) coefficient at the Planck or reduced Planck scale, epsilon ~ 1e-7 to 1e-6. The operator is odd under Phi -> -Phi, so a discrete symmetry acting as hidden charge conjugation forbids it - but only if that symmetry is gauged, since quantum gravity is believed to admit no exact global symmetries [11].

How the operator works [T]:

- **Gauge invariance.** Φ^a and the hidden field strength F^a_μν both transform in the adjoint of SU(2)_d, and the sum over a contracts them into an SU(2)_d singlet. B^μν, the field strength of our hypercharge, is invariant under hypercharge transformations. The product is invariant under both groups.
- **Dimension and suppression.** Φ has mass dimension 1 and each field strength dimension 2, so the product has dimension 5, and a Lagrangian term needs a factor 1/M_\* with M_\* a mass: the scale of whatever heavier physics produces the operator.
- **Mixing after condensation.** When Φ takes its vacuum value v along one direction in the adjoint, Φ^a F^a_μν becomes v times the field strength of the unbroken U(1)_d. The operator becomes (v/M_\*) times the product of the U(1)_d and hypercharge field strengths: kinetic mixing with ε ~ v/M_\*. The round-3 referee found the relation in the literature, "chi = v/M (their eq. 25)" in Brümmer–Jaeckel, with χ their name for ε (`review/round3/referee/audit-notes.md`, Step 1).
- **Symmetry.** The operator is linear in Φ, so it changes sign under Φ → −Φ; a symmetry that flips Φ forbids it.

### The size v3 gave it

The coefficient was the assumption: "an O(1) coefficient at the Planck or reduced Planck scale", that is, M_\* equal to the Planck or reduced Planck mass with nothing smaller in front. At v3's breaking scale, v ~ (0.8–1.4)×10¹² GeV (§3), that gives "epsilon ~ 1e-7 to 1e-6".

### What rested on it

The size of ε fixed the main test v3 offered.

- **Millicharged ψ.** #14 §4: "If hidden charge conjugation is not a gauged symmetry, psi carries visible electric charge ~ epsilon e, with epsilon ~ 1e-7 to 1e-6. Its mass lies between the MeV scale and ~0.1 TeV, and it is a subdominant relic. Bounds on millicharged particles in this mass and charge range have not been evaluated here. They are the most direct near-term test of the proposal (exclusion condition 3)." ψ is the light hidden fermion v3 added so that the hidden W′± could decay ([Obituary: the ψ relic window](/wiki/dark-matter/candidates/soliton-candidate/psi-relic-window)).
- **Exclusion condition 3.** "Exclusion of the millicharged psi window: m_psi from the MeV scale to ~0.1 TeV at visible charge ~ (1e-7 to 1e-6) e. This lapses if hidden charge conjugation is shown to be a gauged symmetry, which sets epsilon = 0" (§5).
- **Acceptance criterion (2).** "either a gauged hidden charge conjugation, or a demonstration that the millicharged psi window survives existing constraints" (§6), with "sector separation, and either its ultraviolet stability or a gauged hidden charge conjugation" among the claims v3 called conjectural.

The round-3 [pre-registration](/wiki/method/review/round-3/preregistration) expected the weakness to lie in the unevaluated bounds, its first runner-up weakest link: "The unevaluated millicharge bounds on ψ at ε ~ 10⁻⁷–10⁻⁶, MeV–0.1 TeV. They might already exclude part of the window." The review found the problem one step earlier, in ε itself.

## How it was tested

The round-3 referee checked the estimate three ways: the arithmetic in Python (Step 2), each reference against what it is cited for (Step 1, summarized in Step 4(b)), and the estimate against the rest of the manuscript (Step 4(a)).

## Why it failed

### The arithmetic was right

The referee's output (`review/round3/referee/step2a.out`):

```text
v=8.09e+11, M_*=MPl: v/M_* = 6.63e-08
v=8.09e+11, M_*=MPl_red: v/M_* = 3.32e-07
v=1.45e+12, M_*=MPl: v/M_* = 1.18e-07
v=1.45e+12, M_*=MPl_red: v/M_* = 5.94e-07
one-loop UV-completion factor g_d g' y/(16 pi^2) with y=1, g'=0.357: 1.37e-03 -> eps range 9.1e-11 - 8.1e-10 (Lambda=MPl..MPl_red)
```

The first four lines reproduce #14's range: "6.6e-8 - 5.9e-7", "CONFIRMED as arithmetic (order of magnitude)" (Step 2). The fifth line is the estimate the literature itself gives, below.

### The coefficient had no source

The referee read each paper of #14's reference [10] for where the operator comes from (Step 1):

- **Chen–Cline–Frey**, arXiv:0907.4746: the operator exists ("eq. 1: sum_i (1/Lambda_i) Y_mu-nu B^mu-nu_a Delta^a_i"), and "The dimension-5 operator (1) can be induced at one loop by a heavy particle X which carries both dark SU(2) charge and weak hypercharge" (p. 3).
- **Brümmer–Jaeckel**, arXiv:0902.3615: χ = v/M "(their eq. 25)", generated from a loop of a field charged under both groups, "1/M = e f h/(6 pi^2 m0) (eq. 28)".
- **Gherghetta et al.**, Sec. 3.2.3, for a non-abelian dark sector with an adjoint scalar: "eps ~ g_X g' y_Sigma/(16 pi^2) <Sigma>/Lambda".

The referee's conclusion: "[10] is cited for more than it says: all sources that derive the operator obtain it from bi-charged states with a one-loop factor ~ g g' y/(16 pi^2), not an O(1) coefficient at M_Pl; and bi-charged states are what the manuscript's sector-separation postulate excludes."

A particle that carries both the hidden and the visible charge, running in a loop, connects the two field strengths; the loop brings the factor 1/16π² and one coupling from each group, here the hidden g_d, the hypercharge g′ and a Yukawa coupling y [T]. With y = 1 and g′ = 0.357 the factor is "1.37e-03", and ε falls to "9.1e-11 - 8.1e-10" even with the heavy scale at the Planck mass (`step2a.out`). In the audit table: "eps with one-loop UV factor g_d g' y/16pi^2 | not considered | 1.37e-3 x -> 9e-11 - 8e-10 | the cited sources' own estimate is 3 orders smaller".

Ruling 7, upheld: "Consistent with the round-2 literature report: Chen–Cline–Frey "induced at one loop by a heavy particle X which carries both…". Sec. 2(a) and 2(b) of v3 are in tension."

### It contradicted the manuscript's own postulate

#14 had postulated sector separation in the same section: "No field carries charge under both U(1)_d and our hypercharge" (§2). Its point (a) took gravity-only mixing to be at most 10⁻¹³; its point (b) assumed an order-one coefficient. The referee (Step 4(a) item 6):

> Sec. 2(a) vs 2(b): (a) says gravity-only mixing is <~1e-13; (b) assumes an O(1) Planck-suppressed coefficient.

Every source that derives the operator gets it "at one loop from fields charged under" both groups (the referee capitalizes "both"), and "such fields are exactly what the sector-separation postulate excludes. The eps ~ 1e-7-1e-6 window therefore contradicts the manuscript's own postulate." Put the other way: with sector separation in force the operator has no known source, and with a source present the separation fails. The two halves of §2 could not both hold.

### Ruling 8: the operator itself exists

The referee also reported that the first paper of [10] does not contain the operator at all. Of Baumgart et al., arXiv:0901.0283, it wrote that the paper does not support the citation: "Its mixing is the renormalizable B_mu-nu b^mu-nu with a dark U(1) factor: "Since G_dark must contain a U(1) factor, the minimal choice is ... SU(2) x U(1)" (p.5). No adjoint dim-5 operator found (grep "dimension five/5", "non-renormalizable": no hits relevant)" (Step 1).

The adjudicator checked the paper and overturned the finding. Ruling 8:

> arXiv:0901.0283v2, p. 5, footnote 5, verbatim: "It is actually possible to achieve mixing without an abelian factor through an S parameter type operator Tr[Φw_μν]B^μν, where Φ is some operator that transforms as an adjoint of the non-abelian group." The referee missed the footnote.

The footnote's name for the operator refers to the electroweak S parameter, a precision observable to which the analogous operator built from our own Higgs field contributes [T]. The text search used words the footnote does not contain. The v3 worklog had cited the same footnote ("Baumgart et al. 2009 fn.", R4). The adjudication's scoring of the pre-registration records the outcome: "The referee's one misattribution claim (Baumgart) was itself wrong."

So the two rulings divide the claim. The operator, and the relation ε ~ v/M_\*, are in the literature (ruling 8). The size v3 gave it is not (ruling 7).

## The verdict

Decision 1 (2026-10-19) chose strict sector separation over the estimate:

> - The alternative rested on an unsupported coefficient. The dimension-5 "O(1) at the Planck scale" estimate (ruling 7) has no source. The sources generate that operator only from bi-charged states, which P4 forbids.
> - It costs nothing and closes three failure channels at once: ψ millicharge, the monopoles' Witten-effect charge (ruling 9), and re-thermalization of the hidden sector.

The decision's first line sets what remains: "ε ≲ 10⁻¹³ from gravity alone, and zero if hidden charge conjugation is a gauged symmetry." [Checkpoint #11](/wiki/history/documents/checkpoint) writes it into P4: "[P; taken strictly since v2.1: no kinetic mixing between the sectors beyond what gravity induces, which vanishes if hidden charge conjugation is exact and otherwise first appears at six loops, ε ≲ 10⁻¹³ [27S].]" (§4).

The adjudication counted the coefficient among the numerical indictments the pre-registration had not expected: "Three survive (p; the ψ window; ξ), plus the ε coefficient", with the comment "All are wrong inputs or model choices in my scripts, not arithmetic slips." The worklog had marked its own version of the estimate machine-verified, "Our estimate: ε ≈ 2.4×10⁻⁸ at M = M_Pl [V]" (R4). The check confirmed v/M, which round 3 also confirmed; the coefficient in front of it was an input the check did not test ([verification checks arithmetic, not the model](/wiki/method/verification/arithmetic-not-model)).

## What survives

- **The operator and the relation.** Φ^a F^a_μν B^μν/M_\* exists in the literature (Baumgart et al.'s footnote; Chen–Cline–Frey eq. 1; Brümmer–Jaeckel eq. 25), and gives ε ~ v/M_\*.
- **The rest of #14's mixing section.** The gravity-only bound and the absence of visible magnetic flux while U(1)_d is unbroken survive v3: "The kinetic-mixing literature points (a) and (c)" (adjudication, 'What survives v3'; [kinetic mixing between sectors](/wiki/dark-matter/candidates/soliton-candidate/kinetic-mixing)).
- **Nothing of the window.** The ε ~ 10⁻⁷–10⁻⁶ estimate, the millicharged-ψ window built on it and exclusion condition 3 are dead with the candidate ([Obituary: superheavy conjugate solitons](/wiki/dark-matter/candidates/soliton-candidate/obituary)).

## History

1. **[Round 2](/wiki/method/review/rounds-one-and-two)** disputed gravity-induced mixing (`HANDOFF.md` §6 records the dispute), and the literature report prepared for the v3 worklog found the dimension-5 operator. Worklog R4: "The dimension-5 adjoint operator is in the literature [Baumgart et al. 2009 fn.; Chen–Cline–Frey 2009; Brümmer–Jaeckel 2009, χ = v/M]. Our estimate: ε ≈ 2.4×10⁻⁸ at M = M_Pl [V]." Its planned wording for v3 gave the range as "≈ 10⁻⁸–10⁻⁷".
2. **v3** (§2(b)) printed "epsilon ~ 1e-7 to 1e-6". The worklog's range and #14's come from different stages of the benchmark and were never reconciled; both are moot ([conflicts between sources](/wiki/history/documents/source-conflicts)).
3. **Round 3** (2026-10-19): the arithmetic confirmed (Step 2), the coefficient found unsupported and in tension with sector separation (Step 4(a) item 6, Step 4(b)), and the Baumgart citation disputed. Rulings 7 (upheld) and 8 (overturned).
4. **Decision 1** (2026-10-19) and #11 v2.1: P4 taken strictly.

## Sources

- `review/round3-adjudication.md` 'Rulings' 7–8 — the unsupported coefficient and the Baumgart footnote; 'Decisions' 1 — strict sector separation; 'Pre-registration scored' — the ε coefficient among the indictments, and the referee's misattribution claim; 'What survives v3' — points (a) and (c)
- `review/round3/referee/audit-notes.md` Step 1 — the references of [10] read for the operator's origin; Step 2 — the arithmetic and the one-loop estimate; Step 4(a) item 6 — the contradiction with sector separation; Step 4(b) — the summary of the literature check
- `review/round3/referee/step2a.out` — the v/M_\* values and the one-loop factor
- `review/round3-preregistration.md` 'Predictions' — the millicharge runner-up
- `review/v3-worklog.md` 'Round-2 pending list' (R4) — the worklog's estimate and planned wording
- `notes/knot-dark-matter-standalone.md` §2 — sector separation and point (b); §4 — the millicharged ψ; §5 — exclusion condition 3; §6 — acceptance criterion (2) and the conjectural claims
- `papers/broken-born-checkpoint-v2.md` §4 — P4 taken strictly
- `HANDOFF.md` §6 — the round-2 dispute over gravity-induced mixing
