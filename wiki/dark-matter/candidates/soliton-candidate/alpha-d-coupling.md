---
title: "Obituary: the coupling α_d ≈ 34"
weight: 40
status: dead
description: "Three attempts to fix the hidden monopoles' coupling — Dirac quantization against our photon (round 1's valid kill), reciprocity acting as modular S (numerology), and hypothesis H — the F2 reframing, and the factor-of-four convention spread."
sources:
  - "HANDOFF.md §2"
  - "HANDOFF.md §6"
  - "review/skeptic-review-console.html"
  - "review/v3-worklog.md 'Round-2 pending list'"
  - "review/v3-worklog.md 'Findings neither referee raised'"
  - "review/v3-worklog.md 'v3 as drafted (2026-10-19)'"
  - "notes/knot-dark-matter-standalone.md Abstract"
  - "notes/knot-dark-matter-standalone.md §2"
  - "notes/knot-dark-matter-standalone.md §6"
  - "review/round3/referee/audit-notes.md Step 1"
  - "review/round3/referee/audit-notes.md Step 2"
  - "review/round3/referee/audit-notes.md Step 4(d)"
  - "review/round3/referee/step2a.out"
  - "review/round3-preregistration.md 'Predictions'"
  - "review/round3-adjudication.md 'Rulings' 12"
  - "review/round3-adjudication.md 'Decisions' 2"
  - "papers/broken-born-checkpoint-v2.md §11"
  - "papers/broken-born-checkpoint-v2.md §12"
  - "verify/soliton_obituary.py"
  - "popsci/universes-other-half.md 'Dark matter as the other polarization'"
  - "review/wiki-build-flags.md item 28"
---

*α_d ≈ 34 was the strength the soliton candidate assigned to the interaction between its hidden [monopoles](/wiki/electric-magnetic-duality/monopoles): 1/(4α), the reciprocal of four times the fine-structure constant α ≈ 1/137 of ordinary electromagnetism. The program tried three ways to fix that value. The first applied Dirac's charge-quantization condition using our photon's charge, which contradicted the claim that the monopoles do not couple to our photon. The second had [Born reciprocity](/wiki/phase-space/reciprocity/born-reciprocity) act on gauge couplings as the modular S transformation of [electric–magnetic duality](/wiki/electric-magnetic-duality); a referee called it numerology, and it was set aside. The third assumed that the smallest hidden charge equals the electron's; it was motivated but not derived, and it fell with the candidate. The number itself shifts by a factor of four with the convention used. What survives is a general fact: a weakly coupled force always has strongly coupled monopoles.*

**Status:** Dead in all three forms. The first was killed in round 1 ([the handoff](/wiki/history/documents/handoff) calls it the "round-1 reviewer's valid kill"); the second was set aside when Paul decided on 2026-10-19 that "S-duality is no longer what fixes α_d" (v3 worklog, F2), and is folded below as superseded; the third, hypothesis H, was part of #14 v3, which was withdrawn on 2026-10-19 (round-3 Decision 2; [round-3 decisions](/wiki/method/review/round-3/decisions)). The round-3 referee confirmed the arithmetic of hypothesis H with executed code; the convention spread is marked [V] in the v3 worklog, and the current gate, `verify/soliton_obituary.py`, does not re-check it. The surviving Dirac relation is [T]. Home: [the soliton candidate](/wiki/dark-matter/candidates/soliton-candidate); listed in [the graveyard](/wiki/status/graveyard).

## The couplings and Dirac's condition

### Electric and magnetic couplings [T]

A gauge force's strength is measured by a dimensionless coupling, α = q²/4π for a charge q in units with ħ = c = 1; for ordinary electromagnetism α ≈ 1/137, the fine-structure constant [T]. A magnetic charge g has a magnetic coupling g²/4π in the same way. Dirac showed that if a magnetic monopole and an electric charge exist in the same gauge theory, quantum mechanics requires their charges to satisfy q·g = 2πn for an integer n, in the normalization the program's documents use ([Dirac quantization and the DSZ pairing](/wiki/electric-magnetic-duality/monopoles/dirac-quantization)) [T]. The smallest electric charge therefore fixes the smallest magnetic charge, and a small electric charge forces a large magnetic one.

### The relation in #14

#14 v3 applied this inside the hidden sector (§2, "Coupling."):

> The hidden sector is weakly coupled in its electric description, with alpha_W' = g_d^2/4pi. Its monopoles carry magnetic charge g_m = 4 pi/g_d, the Dirac minimum relative to psi's charge g_d/2, so their mutual coupling is alpha_m = g_m^2/4pi = 1/alpha_W' [7]. Any weakly coupled hidden sector therefore has strongly coupled monopoles: the strong magnetic coupling is generic, not a hypothesis.

Here g_d is the gauge coupling of the hidden SU(2)_d, α_W′ the coupling of its heavy charged vector bosons W′±, and ψ the light hidden fermion, whose charge g_d/2 is the smallest hidden charge ([the hidden SU(2) → U(1) proposal](/wiki/dark-matter/candidates/soliton-candidate/hidden-sector)). With q = g_d/2 and n = 1, Dirac's condition gives g_m = 4π/g_d, and then α_m = (4π/g_d)²/4π = 4π/g_d² = 1/α_W′. The product α_m·α_W′ = 1 holds whatever g_d is; the referee's script checks it, "check alpha_m * alpha_W' = 1.000000 (should be 1)" (`review/round3/referee/step2a.out`). The question the three attempts below tried to answer is which value g_d takes.

The monopoles' coupling has carried several names: α_d in the handoff and v2, α_m in v3, and α_d again in the worklog's F2 (where α_e,d denotes the hidden electric coupling). On this page α_d ≈ 34 means the monopoles' mutual coupling.

## Attempt 1: Dirac quantization against our photon

The first version of #14 fixed the hidden monopoles' coupling with Dirac's condition applied to our electron's charge. The handoff lists the result among the dead claims (`HANDOFF.md` §2):

> α_d ≈ 34 via Dirac quantization against our photon (round-1 reviewer's valid kill: can't use our DSZ lattice and then deny coupling to our photon).

The DSZ (Dirac–Schwinger–Zwanziger) lattice is the lattice of electric and magnetic charges of one gauge theory, on which Dirac's condition holds pairwise ([the symplectic charge lattice](/wiki/electric-magnetic-duality/symplectic-charge-lattice)). Dirac's argument applies only to charges that couple to the same gauge field. Quantizing the monopoles' charge against the electron's therefore makes them magnetic charges of our electromagnetism, which contradicts the candidate's defining claim that they are dark because they do not couple to our photon. Round 1 found the contradiction and the handoff calls it valid (§6). v3 later stated the opposite explicitly: "nothing is quantized against our gauge field" (#14 §2, "What is not asserted.").

## Superseded: reciprocity acting as modular S

v2 replaced the Dirac argument with a conjecture. The handoff: "Restated in v2 as reciprocity-acts-as-modular-S on the coupling — explicitly the load-bearing conjecture; without it α_d is a free strong coupling" (§2).

### The conjecture as v2 stated it

Electric–magnetic duality exchanges a theory's electric and magnetic descriptions. Its generator S acts on the complexified coupling τ_c by τ_c → −1/τ_c, and [#11](/wiki/history/documents/checkpoint) §11.3 notes that S is generated by the same matrix [[0,1],[−1,0]] as Born's ρ and the program's [inversion Z → −Z⁻¹](/wiki/phase-space/modular-field/modular-inversion) [T] ([S-duality and Montonen–Olive](/wiki/electric-magnetic-duality/s-duality)). v2 conjectured that the two dualities are the same event. Its §2, embedded verbatim in `review/skeptic-review-console.html`:

> Conjecture (the identification). The two polarization choices are made by the same vacuum event, and the momentum-polarized matter sector is the S-dual image of the electric sector: a distinct gauge structure whose complexified coupling is fixed by the reciprocity map, acting as the modular S transformation, to the image of ours - alpha_d = 1/(4 alpha) ~ 34, quoted in the Dirac normalization (the Schwinger convention shifts this by the standard factor of four).

v2 stated the stakes: "This identification is the manuscript's load-bearing conjecture: if reciprocity does not act on gauge couplings as S, the value alpha_d ~ 34 loses its derivation and becomes a free parameter (the candidate survives, but loses predictivity)."

### Round 2's verdict

Round 2 graded v2 "B near B/C / medium" with "weakest link = the α_d derivation ("matrix coincidence ≠ physical identity" / "numerology")" (`HANDOFF.md` §6; [review rounds 1 and 2](/wiki/method/review/rounds-one-and-two)). That two dualities are represented by the same matrix does not show that one acts on the other's coupling. Round 2 also raised the exactness burden, which the worklog answered as item R1: "Exact S-duality has been tested only in N=4 SYM and special finite N=2 theories. For non-SUSY theories there is "no reason to think" it survives quantum corrections, and the bosonic spectrum mismatches (W spin 1, monopole spin 0). That is an expectation, not a no-go" (`review/v3-worklog.md`, 'Round-2 pending list'). SYM is super Yang–Mills, and SUSY is supersymmetry.

### Why it was set aside

The worklog's finding F2 (next section) showed that the S-duality reading was not needed to obtain a strong monopole coupling, and Paul decided on 2026-10-19 that "S-duality is no longer what fixes α_d". v3 kept the charge-lattice correspondence only "as motivation" and added that "Exact electric-magnetic duality is also not assumed" (#14 §2). No [round-3 ruling](/wiki/method/review/round-3/rulings) addresses the conjecture, and #11 v2.2 does not mention it; F2's decision is the operative record.

## Superseded: F2, which coupling sets the soliton mass

The worklog found an inconsistency in v2 that neither referee had raised (`review/v3-worklog.md`, 'Findings neither referee raised', F2, tagged [D, numbers V]):

> v2 writes M ~ (4π/e_d²) Λ_c ~ 100 Λ_c. That factor is ~137 only if e_d²/4π ≈ 1/137. With e_d²/4π = α_d = 34 it is 0.029, so the solitons would not be heavy. v2 uses the weak value in §3 and the strong value in §2 and §4.

A soliton's mass is the symmetry-breaking scale enhanced by the inverse of the elementary coupling [T] ([the 't Hooft–Polyakov monopole](/wiki/electric-magnetic-duality/monopoles/thooft-polyakov-monopole)), so a heavy soliton needs a weak elementary coupling. v2 had used one number for two different couplings. The worklog's resolution:

- "the dual sector's elementary coupling α_e,d is weak, its solitons are heavy (M ≈ Λ_c/α_e,d), and the solitons themselves are strongly coupled (α_m ≈ 1/(4α_e,d) or 1/α_e,d)";
- "Then α_d ≈ 34 follows from α_e,d ≈ α, a mirror-coupling equality, and does not need S acting on our coupling."

Paul adopted the reading on 2026-10-19: "the load-bearing conjecture becomes α_e,d = α (or α_e,d free and weak), and S-duality is no longer what fixes α_d." That equality became hypothesis H. F2's argument is not refuted; it is superseded because the hypothesis it led to died with the candidate.

## Attempt 3: hypothesis H

### The statement

#14 v3 §2:

> The proposal's single coupling hypothesis (H): the smallest hidden charge equals ours, (g_d/2)^2/4pi = alpha. The motivation is that reciprocity exchanges the two polarizations; if it acts on gauge couplings at all, the minimal action is to equate the elementary charges of the two sectors. Under H, alpha_W' = 4 alpha ~ 1/34 and alpha_m = 1/(4 alpha) ~ 34.

The arithmetic follows from the Dirac relation above: if (g_d/2)²/4π = α, then α_W′ = g_d²/4π = 4α, and α_m = 1/α_W′ = 1/(4α). The worklog explains why H matches ψ's charge rather than the W′ charge: the light doublet "makes ψ's charge g_d/2 the smallest dark charge. H matches *that* charge to ours, so α_W′ = 4α ≈ 1/34 and the monopoles' coupling is α_m = 1/α_W′ = 1/(4α) ≈ 34 exactly, by Dirac quantization relative to ψ" ('v3 as drafted (2026-10-19)'). It also records a limit on what H can mean: an exact mirror copy of the Standard Model has no stable monopoles, "so H relates couplings only, not gauge groups". (H here is unrelated to the [generalized metric](/wiki/phase-space/born-geometry/born-structures) H of phase space.)

H fixed g_d, and through it the monopole mass M = 4πf v/g_d ≈ (21–37) v, the W′ mass g_d v, the ψ annihilation cross-section and the monopoles' self-interaction; the gate script still states it as part of the model it checks ("Dirac doublet psi of dark charge g_d/2 = e (hypothesis H)").

### What round 3 found

The referee confirmed the arithmetic with executed code: "alpha_W' under H | 4 alpha ~ 1/34 | 1/34.259 | CONFIRMED" and "alpha_m | ~34 | 34.259 | CONFIRMED" (`review/round3/referee/audit-notes.md`, Step 2), with "gd = 0.60564" (`step2a.out`). It also found a variant the manuscript had not considered: matching ψ's charge to e/3, the smallest charge in the Standard Model, "gives alpha_m = 308 (step2a.out), and the framework gives no way to choose" (Step 4(d)).

The conceptual audit placed H at the centre of the referee's second finding, "the framework does no work": "hypothesis H is motivated, not derived (acceptance criterion 1 concedes this)", and "Even the one structural input H only sets M/v = 21-37 and alpha_m = 34" (Step 4(d); [the 'framework does no work' critique](/wiki/program/framework-does-no-work)). The [pre-registration](/wiki/method/review/round-3/preregistration) had expected this: "Hypothesis H's motivation ("the minimal action is to equate the elementary charges") is one sentence."

### How it died

#14 §6 listed "hypothesis H" as "Conjectural", and its [acceptance criterion 1](/wiki/symmetry-breaking/toy-models/acceptance-criterion) asked for an action from which H could be derived: "deriving hypothesis H from that action would make the coupling a prediction". No ruling addresses H by itself. It died as a component of v3 when the candidate was retired (round-3 Decision 2; [Obituary: superheavy conjugate solitons](/wiki/dark-matter/candidates/soliton-candidate/obituary)), and it is absent from both survivor lists.

## Superseded: the convention and running spread

Round 2 asked how much the number 34 depends on conventions. The worklog's item R2, "**adjudicated** [V]" (`review/v3-worklog.md`, 'Round-2 pending list'):

> Convention: 1/(4α) = 34.26 (eg = 2πn) vs 1/α = 137.04 (eg = 4πn). One-loop SM running of α_em gives 1/(4α_em) = 29.0 at 10¹¹, 28.8 at 3×10¹¹ and 27.3 at 10¹⁶ GeV. The referee's "toward ~6–8" is **not reproduced** for the electromagnetic coupling; 6–8 appears only for 1/(4α₃). The valid core stands: the number is convention-dependent by a factor of 4. v3: present α_d as free-but-strong.

SM is the Standard Model, and α₃ the strong-force coupling. The spread has two sources [T]. The first is normalization: whether Dirac's condition is written q·g = 2πn or 4πn changes the minimal magnetic charge by a factor of two and the coupling by four. The referee also flagged it in #14's citation of Zwanziger, whose abstract "states e_m g_n - g_m e_n in 4 pi Z; manuscript writes 2 pi Z (Dirac normalization). The 't Hooft-Polyakov monopole with doublets realises 2 pi, so the physics is fine" (Step 1; [ruling 12](/wiki/method/review/round-3/rulings#ruling-12-minor-citation-issues), accepted). The second is the energy scale: α grows slowly with energy, so matching the two sectors' charges at the transition scale rather than at low energy lowers 1/(4α).

v3 carried both into its text: "Matching the W' charge to ours instead of psi's gives alpha_m ~ 137. Matching at 1e12 GeV instead of at low energy gives about 29, from one-loop Standard Model running of alpha." The referee confirmed both: "137.036" for the W′-charge variant, and "28.61 (MSbar 127.930), 28.86 (128.95)" for running to 10¹² GeV (Step 2). The drafting check had corrected the second figure before v3 was written: "the coupling matched at 10¹² GeV is ≈ 29 (not 28)" (worklog, 'v3 as drafted (2026-10-19)').

The spread is the spread of a number that no longer has a role: with H dead, nothing in the program fixes α_d.

## What survives

The general relation survives the candidate. #11 §12, under "What survives": "A weakly coupled hidden sector always has strongly coupled monopoles, by Dirac quantization [T]." In #14's words, "the strong magnetic coupling is generic, not a hypothesis." What died is every attempt to pick the particular value 34 for a hidden sector.

For ordinary electromagnetism the same arithmetic is established physics and untouched. #11 §11.2 [T]: "Dirac's condition e·g ~ 2π pins the magnetic coupling near 4π/e² ≈ 34 — the magnetic world is our strong-coupling mirror, heavy and bound" ([the magnetic mirror-family](/wiki/electric-magnetic-duality/magnetic-mirror-family)). That value concerns the magnetic charges of our own electromagnetism, not a hidden sector. Flag 28 in `review/wiki-build-flags.md` finds the number right and the formula beside it suspect: with α = e²/4π, 4π/e² is 1/α, while a coupling near 34 is 1/(4α), as in the Dirac relation above.

The [popular article](/wiki/history/documents/popular-articles) #12 uses the same comparison, "about 34, against our 1/137", for the claim that the momentum-polarized sector is "the magnetic side of electromagnetism". That claim appears only in the popular article and is dead ([Obituary: the magnetic identification](/wiki/electric-magnetic-duality/magnetic-identification)).

## Sources

- `papers/broken-born-checkpoint-v2.md` §12 — what survives; §11.2 — the ordinary-electromagnetism statement; §11.3 — the shared matrix
- `HANDOFF.md` §2 — the first two attempts and their status; §6 — round 1's kill and round 2's verdict
- `review/v3-worklog.md` 'Round-2 pending list' (R1, R2), 'Findings neither referee raised' (F2), 'v3 as drafted (2026-10-19)' — the exactness burden, the convention spread, the mass argument and Paul's decision, and how H was matched
- `notes/knot-dark-matter-standalone.md` §2 — the Dirac relation, hypothesis H, "What is not asserted"; §6 — H as "Conjectural" and acceptance criterion 1; Abstract — the coupling as v3 states it
- `review/round3/referee/audit-notes.md` Step 1 — the 2π versus 4π normalization; Step 2 — the confirmed arithmetic and variants; Step 4(d) — the e/3 variant and "motivated, not derived"
- `review/round3/referee/step2a.out` — the referee's printed couplings
- `review/round3-preregistration.md` 'Predictions' — H's one-sentence motivation
- `review/round3-adjudication.md` 'Rulings' 12 — the normalization accepted; 'Decisions' 2 — the retirement
- `verify/soliton_obituary.py` — H as part of the checked model
- `review/skeptic-review-console.html` — #14 v2's modular-S conjecture, verbatim
- `popsci/universes-other-half.md` 'Dark matter as the other polarization' — the popular echo
- `review/wiki-build-flags.md` item 28 — the formula #11 §11.2 writes beside the value 34
