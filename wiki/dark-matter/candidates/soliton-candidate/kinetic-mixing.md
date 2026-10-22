---
title: "Kinetic mixing between sectors"
weight: 120
status: established
description: "Gravity alone mixes two photons only at six loops (ε ≲ 10⁻¹³) and not at all if hidden charge conjugation is exact; no visible flux while U(1)_d is unbroken; and the leakage channels mixing would open, closed by strict P4."
provenance: [T]
sources:
  - "papers/broken-born-checkpoint-v2.md §4"
  - "papers/broken-born-checkpoint-v2.md ref [27]"
  - "CLAUDE.md 'Since the handoff'"
  - "review/round3-adjudication.md 'Decisions' 1"
  - "review/round3-adjudication.md 'Rulings' 9"
  - "review/round3-adjudication.md 'Rulings' (omitted constraints)"
  - "review/round3-adjudication.md 'What survives v3'"
  - "review/round3/referee/audit-notes.md Step 1"
  - "review/round3/referee/audit-notes.md Step 4(a)"
  - "review/round3/referee/audit-notes.md Step 4(b)"
  - "review/round3/referee/audit-notes.md Step 4(c)"
  - "review/round3/referee/step2a.out"
  - "review/round3/referee/step4b.out"
  - "notes/knot-dark-matter-standalone.md §2"
  - "notes/knot-dark-matter-standalone.md §4"
  - "notes/knot-dark-matter-standalone.md §5"
  - "notes/knot-dark-matter-standalone.md refs [9]–[14]"
  - "review/v3-worklog.md 'Round-2 pending list'"
  - "review/v3-worklog.md 'Findings neither referee raised'"
  - "HANDOFF.md §2"
  - "HANDOFF.md §6"
---

*Kinetic mixing is a coupling between the field strengths of two U(1) gauge forces, such as our photon and a hidden photon, through a term proportional to ε times the product of the two field strengths. When ε is not zero, particles charged under the hidden force acquire a small electric charge under ours, so kinetic mixing is the standard route by which a hidden sector can leak into the visible one. Three literature results framed the soliton candidate's hidden sector: gravity alone produces mixing only at six loops or more, and none if hidden charge conjugation is an exact symmetry; while the hidden photon stays massless, mixing does not make hidden [monopoles](/wiki/electric-magnetic-duality/monopoles) magnetic under our electromagnetism; and what leakage remains would give the hidden fermion ψ, and through the Witten effect the monopoles, a small visible electric charge. The program closed these channels by taking its postulate [P4](/wiki/program/postulates/p4-polarized-matter) strictly.*

**Status:** Established — literature [T]: Gherghetta–Kersten–Olive–Pospelov [27S] on gravity-induced mixing, and Hiramatsu et al. (massless hidden photon) and Terning–Verhaaren (massive hidden photon) on visible magnetic flux, as read in the v3 worklog and checked by the [round-3](/wiki/method/review/round-3) referee. "The kinetic-mixing literature points (a) and (c)" survive v3 (round-3 adjudication). The Witten-effect finding was "Accepted, not re-checked" ([ruling 9](/wiki/method/review/round-3/rulings#ruling-9-the-witten-effect)). The general explanations below are from standard physics [T]; references the wiki adds are marked †.

## What kinetic mixing is

### The term [T]

The field strength of an abelian gauge field, F_μν = ∂_μA_ν − ∂_νA_μ, does not change under that field's gauge transformations. So when two U(1) gauge fields exist, nothing in gauge invariance forbids a term that multiplies one field strength by the other [T]:

```text
ℒ ⊃ −(ε/2) F′_μν B^μν
```

Here F′ is the hidden U(1)'s field strength and B our hypercharge field strength. Below electroweak breaking the hypercharge field is the combination cos θ_W A − sin θ_W Z of the photon A and the Z boson, θ_W being the weak mixing angle, so the photon inherits the mixing with a factor cos θ_W. The term has dimension four, so ε is a pure number, allowed at any size unless some symmetry or structure fixes it (Holdom 1986 †). The withdrawn manuscript [#14](/wiki/dark-matter/candidates/soliton-candidate) (§2) calls it "kinetic mixing epsilon between the two field strengths".

### What it does [T]

The term makes the two gauge fields' kinetic terms non-diagonal. Redefining the fields to undo this shifts the couplings: with the hidden photon massless, particles charged under the hidden U(1) acquire a small electric charge, of order ε times their hidden charge, under our photon. They become millicharged particles. The round-3 referee's code writes it for ψ as "psi visible charge = eps*cos(thetaW)*((g_d/2)/e) e; (g_d/2)/e = 1.000, cos thetaW=0.8815" (`review/round3/referee/step2a.out`), where (g_d/2)/e = 1 is the manuscript's coupling hypothesis H ([Obituary: the coupling α_d ≈ 34](/wiki/dark-matter/candidates/soliton-candidate/alpha-d-coupling)).

### Where ε comes from [T]

A loop of a particle that carries both charges generates ε, suppressed by the loop factor 1/16π² and by the two couplings. If no particle carries both charges, that source is gone, and ε can arise only from gravity or from operators of higher dimension. The round-3 referee found that all the sources that derive the soliton manuscript's dimension-5 version obtain it this way, "from bi-charged states with a one-loop factor ~ g g' y/(16 pi^2)" (audit notes, Step 1).

A non-abelian field strength F^a_μν changes under its gauge transformations, so a hidden group with no U(1) factor, such as [SU(2)_d](/wiki/dark-matter/candidates/soliton-candidate/hidden-sector) before it breaks, has no dimension-4 mixing term. Mixing then needs a field that breaks the group: the adjoint operator Φ^a F^a_μν B^μν/M_\*, which becomes ε ~ v/M_\* once Φ takes its vacuum value v ([Obituary: Planck-suppressed adjoint mixing](/wiki/dark-matter/candidates/soliton-candidate/dimension-five-operator)).

### Why it matters to the program

The program's postulate [P4](/wiki/program/postulates/p4-polarized-matter) puts the Standard Model and the [conjugate matter](/wiki/dark-matter/conjugate-matter) in separate [polarizations](/wiki/phase-space/reciprocity/lagrangian-polarizations) and says that "gauge forces do not cross polarizations" ([checkpoint #11](/wiki/history/documents/checkpoint) §4). Kinetic mixing is the standard way two otherwise separate gauge forces could cross. For the soliton candidate it decided whether the hidden sector stayed dark: #14 postulated "No field carries charge under both U(1)_d and our hypercharge" and then set out what mixing remains (§2).

## (a) Mixing from gravity alone

### The result

#14 §2(a):

> (a) Pure gravity. Kinetic mixing vanishes to all perturbative orders if hidden charge conjugation is an exact symmetry. If it is broken, gravity can induce mixing, but only at six loops or more, giving epsilon <~ 1e-13 [9].

Charge conjugation C reverses the sign of a U(1) gauge field [T]. The mixing term contains one field strength from each sector, so it changes sign under charge conjugation of the hidden sector alone; if that operation is an exact symmetry, no process can generate the term [T]. This is the condition #14 and #11 state, "if hidden charge conjugation is exact". The paper (#11's [27S], #14's [9]), as the round-3 referee quotes it (Step 1):

- p. 5: "If C_A and C_X are separately good symmetries ..., then kinetic mixing cannot be induced at any perturbative order";
- abstract: "kinetic mixing through gravity alone, requires at least six loops and could be as large as ~1e-13", conditional, in the referee's reading, "on C_X breaking and O(1) hidden Yukawa".

Gravity couples to both sectors, so it is the one interaction that P4 cannot switch off; the paper finds that it generates mixing only at a high loop order, and only if hidden charge conjugation is broken. The referee's verdict: "SUPPORTS both parts" (Step 1). In Step 4(b) it added a caveat: "the manuscript does not say whether hidden C is broken in its SU(2)+adjoint+doublet sector."

#11 adopts the result in P4 (§4):

> [P; taken strictly since v2.1: no kinetic mixing between the sectors beyond what gravity induces, which vanishes if hidden charge conjugation is exact and otherwise first appears at six loops, ε ≲ 10⁻¹³ [27S].]

### An unresolved reading: ceiling or floor

The referee notes that Gherghetta et al. present 10⁻¹³ as a floor (the referee's capitals), "minimum kinetic mixing in any theory with hidden gauge interactions and charge symmetry breaking", which is "consistent with "<~" only in the sense "up to"" (Step 1). #11's "ε ≲ 10⁻¹³" stands as written; the reading is flagged and not resolved ([conflicts between sources](/wiki/history/documents/source-conflicts)).

## (b) Gauged, not global

An exact hidden charge conjugation would remove even gravity's contribution, but only if gravity respects it. #14 §2(b) states the condition:

> The operator is odd under Phi -> -Phi, so a discrete symmetry acting as hidden charge conjugation forbids it - but only if that symmetry is gauged, since quantum gravity is believed to admit no exact global symmetries [11].

A global symmetry acts the same way everywhere and is not tied to a gauge field; a gauged symmetry is part of the gauge structure [T]. The expectation that quantum gravity breaks every global symmetry is argued in Banks–Seiberg 2011 and Harlow–Ooguri 2021 (#14's [11]); one standard argument is that a black hole can absorb a global charge and evaporate without returning it [T]. A gauged discrete symmetry is not affected. For a U(1) gauge group, the reflections of the group O(2) act on its rotations, SO(2) ≅ U(1), as charge conjugation, so gauging O(2) instead of SO(2) makes C part of the gauge group [T]. The v3 worklog (R4): "Quantum gravity forbids an exact global C [Banks–Seiberg 2011; Harlow–Ooguri 2021]; a gauged C (O(2)/O(3)-type) remains a loophole [Obied–Parikh, preprint]." The referee found the statement "consistent with [11]" (Step 4(b)).

This is the basis of the strict reading's second clause: mixing is "zero if hidden charge conjugation is a gauged symmetry" ([round-3 Decision 1](/wiki/method/review/round-3/decisions#decision-1-strict-sector-separation)).

## (c) No visible magnetic flux while U(1)_d is unbroken

The third point changed what the soliton manuscript had to worry about. The v3 worklog, finding L1:

> With an unbroken dual U(1), i.e. a massless dark photon, which is v2's setup, kinetic mixing gives the dark monopole **no QED magnetic flux**.

QED is quantum electrodynamics. The literature behind it, as the worklog and the referee read it:

- Hiramatsu–Ibe–Suzuki–Yamaguchi, arXiv:2109.12771 (#14's [12]), abstract, checked by the worklog's author and by the referee: "does not induce the QED magnetic flux in the U(1) symmetric phase, even in the presence of the kinetic mixing".
- Brümmer–Jaeckel 2009, p. 5: "hidden monopoles are invisible to ordinary electrically charged matter" (Step 4(b)).
- Terning–Verhaaren, arXiv:1808.09459 (#14's [13]), p. 11: with a massive dark photon, "dark magnetic charges get an eps e/4pi coupling to the massless photon", and the dark monopoles are confined by flux tubes (Step 1). The worklog: "Minicharged, confined monopoles need a *massive* dark photon", citing also Graesser et al., JHEP 03 (2022) 105.

So v2's premise, "mixing ε gives the solitons magnetic charge εg under our photon", "is wrong for its own setup." The worklog counted four places in v2 that rested on it: "§2's "It is not decorative" paragraph, §4's last sentence of the first paragraph, §5 exclusion 3, and §6 acceptance criterion (2)". v3 rewrote them (§2(c)):

> (c) Consequence. With U(1)_d unbroken, kinetic mixing does not give the monopoles magnetic charge under our photon: the hidden monopole induces no visible magnetic flux even with epsilon nonzero [12, 10]. Minicharged monopoles would require a massive hidden photon [13], which this proposal excludes.

The counterfactual magnetic flux of #14 §4 then serves only to show why the sectors must be separate ([benchmark-conditional arithmetic](/wiki/dark-matter/candidates/soliton-candidate/benchmark-arithmetic)). The referee's verdict on point (c): "SUPPORTED" (Step 4(b)).

## The leakage channels when ε ≠ 0

#14 §2(c) continued: "The visible-sector leakage is instead (i) psi acquires visible electric charge ~ epsilon e, and (ii) with CP violation the monopoles acquire a small visible electric charge [14]. The decisive constraints therefore act on psi, not on the dark matter itself (Sec. 4)." CP is the combined symmetry of charge conjugation and parity.

### (i) A millicharged ψ

ψ is the light hidden fermion v3 added so that the hidden W′± could decay ([W′ overclosure](/wiki/dark-matter/candidates/soliton-candidate/w-prime-overclosure)). With mixing it is millicharged. #14 §4 left the consequences open: "Bounds on millicharged particles in this mass and charge range have not been evaluated here." The referee listed them (Step 4(c) items 2–5): limits from supernova SN1987A cooling, from the cosmic microwave background and Big Bang nucleosynthesis, from charged subcomponents of the dark matter, and from dark acoustic oscillations; they are set out on [Obituary: the ψ relic window](/wiki/dark-matter/candidates/soliton-candidate/psi-relic-window).

A millicharge also reconnects the two plasmas. The referee (Step 4(a) item 5): "with eps = 1e-6 the SM freeze-in of psi reaches equilibrium for all m_psi <= 30 GeV", where SM is the Standard Model; the hidden sector is then "re-thermalised below v and the reheating ratio xi is no longer the operative variable", and a late decoupling, "T_d < 0.2 GeV -> Delta N >= 0.61 (excluded)", violates the bound on extra radiation ([the hidden sector's thermal history](/wiki/dark-matter/candidates/soliton-candidate/hidden-thermal-history)).

Before ψ existed, the worklog had placed the millicharge on the hidden W′± instead: "dark *electric* states (W′±) pick up a millicharge εe [Brümmer–Jaeckel]" (L1).

### (ii) The Witten effect

In a gauge theory with a θ term, a term proportional to θ times the product of the electric and magnetic fields, a magnetic monopole acquires an electric charge proportional to θ: it becomes a dyon (Witten 1979 †) [T]. The angle θ has physical effects only if it cannot be removed by redefining fermion fields, which a massive charged fermion prevents [T]. The referee (Step 4(a) item 7): "Hidden theta is physical (psi massive) and generically O(1): q_vis ~ chi theta_d/(2 pi)", by eq. 3.19 of Brümmer–Jaeckel–Khoze (#14's [14]), which gives "1.6e-8 e (chi=1e-7, theta=1) to 1.6e-7 e (chi=1e-6)". Here χ is ε and θ_d the hidden θ. The referee quotes the paper's abstract (Step 1): with CP violation, hidden monopoles acquire a hidden electric charge, and "quite generally they also acquire (small) electric charges under the visible electromagnetic gauge group"; also, "Both kinetic and magnetic mixing are naturally induced radiatively". Over χ from 1e-7 to 1e-6 and θ_d from 0.10 to 3.14, the referee's script gives charges from 1.59e-09 e to 5.00e-07 e (`step4b.out`).

Ruling 9, "Accepted, not re-checked": "With mixing and a physical hidden θ, the monopoles carry visible electric charge ~ εθ/2π · e (Witten effect)", which "contradicts v3's "constraints act on ψ, not the dark matter" whenever ε ≠ 0." The referee called the charge "Phenomenologically tiny at M=3e13 GeV, but it makes exclusion condition 1 self-triggering in the eps != 0 branch": #14's exclusion condition 1 counted "Any confirmed non-gravitational coupling between the dominant dark-matter component and the Standard Model" as fatal (§5).

## Strict sector separation

Round-3 Decision 1 (2026-10-19), in full:

> 1. **Kinetic mixing: strict sector separation.** ε ≲ 10⁻¹³ from gravity alone, and zero if hidden charge conjugation is a gauged symmetry.
>    - It is the program's own postulate P4 ("gauge forces do not cross polarizations") taken at face value.
>    - The alternative rested on an unsupported coefficient. The dimension-5 "O(1) at the Planck scale" estimate (ruling 7) has no source. The sources generate that operator only from bi-charged states, which P4 forbids.
>    - It costs nothing and closes three failure channels at once: ψ millicharge, the monopoles' Witten-effect charge (ruling 9), and re-thermalization of the hidden sector.

The [project instructions](/wiki/history/documents/project-instructions) record it among the changes since the handoff: "Strict sector separation (P4 at face value) is in force." It is a decision about the postulate, not a derivation: whether sector separation is stable against quantum corrections was never computed, and [the handoff](/wiki/history/documents/handoff)'s open item 3, "UV stability of sector separation / kinetic mixing (incl. the disputed gravity-induced mixing channel — see §6)" (§2), was settled by taking P4 strictly ([round-3 decisions](/wiki/method/review/round-3/decisions)). Under strict P4 neither dark-matter candidate couples to the Standard Model, which is [row 7, a permanent null in direct detection](/wiki/predictions/direct-detection-null).

## History

1. **Round 1** found "kinetic mixing unaddressed (postulate + ε ≲ 10⁻⁵ exclusion added)" (`HANDOFF.md` §6). That bound was #14 v2's added postulate, a different context from the gravity-only ε ≲ 10⁻¹³ ([rounds 1 and 2](/wiki/method/review/rounds-one-and-two)).
2. **Round 2** disputed gravity-induced mixing: the referee "claims a graviton-loop mixing mechanism needing no bi-charged matter; its formula was uncited and unverified — v2's "forbidden to all orders" is too strong either way; soften and resolve by literature" (`HANDOFF.md` §6).
3. **The v3 worklog** resolved it from the literature (R4): "The referee is right that it exists, and it is negligible", and planned v3's wording: "absent if dark C is a gauged symmetry; otherwise ε ~ ⟨Φ⟩/M (≈ 10⁻⁸–10⁻⁷) from dimension 5 and ≲ 10⁻¹³ from pure gravity". L1 added point (c).
4. **v3** (§2) stated points (a)–(c) as above, with the dimension-5 estimate at "epsilon ~ 1e-7 to 1e-6".
5. **Round 3** supported (a) and (c), found the dimension-5 coefficient unsupported (ruling 7) and the Witten-effect charge a contradiction (ruling 9) ([round-3 verdict and rulings](/wiki/method/review/round-3/rulings)).
6. **Decision 1** and #11 v2.1: P4 taken strictly, with Gherghetta et al. as [27S].

## Standard references

- B. Holdom, "Two U(1)'s and ε charge shifts," Phys. Lett. B 166, 196 (1986) † — the kinetic-mixing term.
- E. Witten, "Dyons of charge eθ/2π," Phys. Lett. B 86, 283 (1979) † — the Witten effect.
- T. Gherghetta, J. Kersten, K. Olive, M. Pospelov, Phys. Rev. D 100, 095001 (2019), arXiv:1909.00696 — #11's [27S], #14's [9]: gravity-induced mixing.
- M. Baumgart et al., arXiv:0901.0283; F. Chen, J. M. Cline, A. R. Frey, arXiv:0907.4746; F. Brümmer, J. Jaeckel, arXiv:0902.3615 — #14's [10]: non-abelian mixing and its loop origin.
- T. Banks, N. Seiberg, arXiv:1011.5120; D. Harlow, H. Ooguri, arXiv:1810.05338 — #14's [11]: no global symmetries in quantum gravity.
- T. Hiramatsu, M. Ibe, M. Suzuki, S. Yamaguchi, JHEP 12 (2021) 122, arXiv:2109.12771 — #14's [12]: no visible flux in the unbroken phase.
- J. Terning, C. B. Verhaaren, JHEP 12 (2018) 123, arXiv:1808.09459 — #14's [13]: minicharged monopoles need a massive dark photon.
- F. Brümmer, J. Jaeckel, V. V. Khoze, JHEP 06 (2009) 037, arXiv:0905.0633 — #14's [14]: magnetic mixing and the visible charge of hidden monopoles.
- Graesser et al., JHEP 03 (2022) 105; Obied–Parikh, preprint without identifier — cited in the v3 worklog only.

#14's references are untagged in #14 itself; the round-3 referee resolved all of them on INSPIRE and checked each against the claim it supports (Step 1). The two † entries are added here from memory and are unchecked.

## Used by

- [P4: polarized matter and strict sector separation](/wiki/program/postulates/p4-polarized-matter) — the literature behind the strict reading since v2.1.
- [Row 7: a permanent null in direct detection](/wiki/predictions/direct-detection-null) — no coupling of either candidate to the Standard Model.
- [Obituary: Planck-suppressed adjoint mixing](/wiki/dark-matter/candidates/soliton-candidate/dimension-five-operator) — the dimension-5 alternative that strict P4 replaced.
- [Obituary: superheavy conjugate solitons](/wiki/dark-matter/candidates/soliton-candidate/obituary) — "dark by sector separation".
- [Obituary: the ψ relic window](/wiki/dark-matter/candidates/soliton-candidate/psi-relic-window) — ψ's millicharge channels, closed by Decision 1.
- [The hidden sector's thermal history](/wiki/dark-matter/candidates/soliton-candidate/hidden-thermal-history) — re-thermalization through a millicharge.
- [Benchmark-conditional arithmetic](/wiki/dark-matter/candidates/soliton-candidate/benchmark-arithmetic) — why the counterfactual monopole flux does not arise.
- [Obituary: the hidden SU(2) → U(1) proposal](/wiki/dark-matter/candidates/soliton-candidate/hidden-sector) — how weakly the hidden photon mixes with ours, and points (a) and (c) among the survivors.
- [W′ overclosure: the minimal sector is excluded](/wiki/dark-matter/candidates/soliton-candidate/w-prime-overclosure) — the visible charge ψ would carry if the photons mix.
- [Conjugate monopoles as ontology](/wiki/electric-magnetic-duality/conjugate-monopoles) — under strict P4 a conjugate monopole carries no charge under our photon.
- [Obituary: the magnetic identification (popsci-only)](/wiki/electric-magnetic-duality/magnetic-identification) — strict sector separation, which the identification contradicts.
- [Round-3 decisions and lessons](/wiki/method/review/round-3/decisions) — Decision 1 rests on points (a) and (b).
- [Round-3 verdict, rulings and citation audit](/wiki/method/review/round-3/rulings) — ruling 9 and the surviving points (a) and (c).

## Sources

- `papers/broken-born-checkpoint-v2.md` §4 — P4 and its strict reading; ref [27] — Gherghetta–Kersten–Olive–Pospelov [S]
- `CLAUDE.md` 'Since the handoff' — strict sector separation in force
- `review/round3-adjudication.md` 'Decisions' 1 — strict sector separation; 'Rulings' 9 — the Witten effect; the omitted-constraints list; 'What survives v3' — points (a) and (c)
- `review/round3/referee/audit-notes.md` Step 1 — the literature checked, the floor reading; Step 4(a) items 5 and 7 — re-thermalization and the monopoles' visible charge; Step 4(b) — the kinetic-mixing claims against the literature; Step 4(c) — the omitted millicharge constraints
- `review/round3/referee/step2a.out` — ψ's visible charge with cos θ_W; `review/round3/referee/step4b.out` — the Witten-effect charges
- `review/v3-worklog.md` 'Round-2 pending list' (R4) and 'Findings neither referee raised' (L1) — the literature as read for v3
- `notes/knot-dark-matter-standalone.md` §2 — sector separation and points (a), (b) and (c); §4 — the unevaluated millicharge bounds; §5 — exclusion condition 1; refs [9]–[14]
- `HANDOFF.md` §2 — open item 3; §6 — rounds 1 and 2 on kinetic mixing
