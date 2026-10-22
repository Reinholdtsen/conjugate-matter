---
title: "The three debts"
weight: 20
status: record
description: "Debt 1 (the field equation for H, settled in structure by calc notes #5–#8), Debt 2 (the gate: mechanism found in #5 §E, shape open) and Debt 3 (the stream instability, closed negative by #2–#4): what each asked, how it was settled, and what it left open."
sources:
  - "papers/broken-born-checkpoint-v2.md §7–§9"
  - "papers/broken-born-checkpoint-v2.md §2"
  - "papers/broken-born-checkpoint-v2.md §5"
  - "papers/broken-born-checkpoint-v2.md §12"
  - "papers/broken-born-checkpoint-v2.md §14"
  - "papers/broken-born-checkpoint-v2.md §15"
  - "review/round3-adjudication.md 'Decisions'"
  - "HANDOFF.md §2"
  - "HANDOFF.md §3"
  - "notes/debt3a-stream-stability.md"
  - "notes/debt3b-wave-island.md"
  - "notes/debt3c-ufd-endpoint.md"
  - "notes/debt1a-geometric-core.md §A–§F"
  - "notes/debt1a-ii-X-classification.md §1–§5"
  - "notes/debt1a-iii-tuning-test.md §1–§5"
  - "notes/debt1a-iv-beta-coefficients.md §1–§5"
  - "notes/broken-born-theory.md §0"
  - "notes/broken-born-theory.md §3"
  - "notes/broken-born-theory.md §5.2"
  - "notes/broken-born-theory.md §11"
  - "notes/broken-born-theory.md §12"
  - "notes/broken-born-theory.md 'Addendum (v0.2)' to 'Addendum (v0.6)'"
  - "notes/broken-born-program-v1.md §5–§7"
  - "verify/battery.py"
  - "review/v3-worklog.md 'Round-2 pending list'"
  - "review/wiki-build-flags.md items 1, 3–8, 14–17, 19, 23"
---

*The three debts are the three open problems that the program's first write-up, the lab notebook #1, ranked most severe and called its "three named debts"; the calc notes #2 to #8, written to settle them, call them Debt 1, Debt 2 and Debt 3. Debt 1 asked for the field equation of momentum-space geometry, the question left open since Born's paper of 1938. Debt 2 asked where the velocity gate comes from, the factor that confines the self-interaction of conjugate matter to particles of nearly equal velocity. Debt 3 asked whether that interaction makes dark matter gather into streams of shared velocity, the program's founding image. Debt 3 was settled first, against the program: such clumping is nowhere required. Debt 1 was settled in structure: momentum-space geometry is carried by a massive spin-2 field of a known class of bimetric gravity, though the class was selected rather than derived from the program's action. Debt 2's mechanism, exchange of that field, came out of the first Debt-1 note; the gate's exact shape is still open.*

**Status:** Record — untagged; the debts entered #1 §11 as open problems tagged [O]. Debt 3 closed negative in calc note #4 (`HANDOFF.md` §3: "closes Debt 3 (negative)"); Debt 1 closed in structure in calc note #8 ("closes Debt 1 (structural)"); Debt 2's mechanism was found in calc note #5 §E ("pays Debt 2's mechanism"), and its shape is #11 §14 item 4 [O]. The Tier-1 algebra of the Debt-1 notes is machine-checked by [the battery T1–T7](/wiki/method/verification/battery); no `verify/` script covers Debt 2 or Debt 3.

## The debts at a glance

| | Debt 1 | Debt 2 | Debt 3 |
| --- | --- | --- | --- |
| Open problem of #1 §11 | 1: the field equation for H | 2: a derivation of the gate | 3: the stream instability against orbital mixing |
| Settled in | calc notes #5–#8 | #5 §E (mechanism), #6 §4 (the width μ) | calc notes #2–#4 |
| Outcome | in structure: X is a massive spin-2 field in the [reciprocity-symmetric branch](/wiki/gravity/palindromic-branch) of [Hassan–Rosen bimetric gravity](/wiki/gravity/spin-2-fields/hassan-rosen-bimetric) | mechanism found, exchange of X; shape open | negative: velocity clumping is nowhere mandatory |
| Left open | [OP1](/wiki/gravity/tuning-test/wedge-reduction), [OP2](/wiki/gravity/palindromic-branch/pm-comparison), [OP3](/wiki/phase-space/born-geometry/lorentzian-dressing), [OP6](/wiki/gravity/momentum-graviton/tau-stuckelberg-mixing) | [OP4](/wiki/dark-matter/conjugate-matter/gate-shape), [OP5](/wiki/dark-matter/conjugate-matter/dual-stress-enhancement) | [the topological loophole](/wiki/dark-matter/momentum-clumping/topological-loophole), with no candidate |
| Label in #11 | §7, "The massive momentum graviton (Debt 1)" | §8, "Conjugate matter and the gate (Debt 2)" | §9, "Obituary: the death of momentum clumping (Debt 3)" |

OPn is item n of #11 §14, the checkpoint's list of open problems ([open problems and the queue](/wiki/status/open-problems)).

## What the debts were

The lab notebook, #1 ("Version 0.1, September 2026"), set the program out as postulates, an action and a table of predictions ([the lab notebook](/wiki/history/documents/lab-notebook)). Its summary ends with "three named debts standing between this document and a paper" (#1 §12): the first three entries of its §11, "Open problems, in order of severity". Quotations from #1 and from the Debt-3 notes on this page are transcribed from their LaTeX.

1. "The field equation for H beyond minisuperspace — Born's 88-year debt. The action exists (Born connection [T]), but solutions, the section condition on curved backgrounds, and the full ghost analysis do not. [O]" H is the positive generalized metric of postulate [P1](/wiki/program/postulates/p1-arena), which carries the spacetime metric g and a momentum-space metric g̃ ([the structures ω, η, H](/wiki/phase-space/born-geometry/born-structures)). Its action, built from the curvature of [the Born connection](/wiki/phase-space/born-geometry/born-connection), had been used only in minisuperspace, the reduction of cosmology to a few homogeneous modes ([the v0.1 action](/wiki/gravity/tuning-test/geometric-action); [minisuperspace](/wiki/cosmology/scale-factor-duality/friedmann-cosmology)). The missing equation would answer what calc note #8 calls "the 88-year question 'what is the dynamics of momentum-space geometry?'" (§4), the years counted from Born's paper of 1938 (#11 §3; [Born's question](/wiki/program/borns-question)).
2. "Gate-shape derivation: obtain e^{−k²/μ²} (or its true form) from S_H + S_mix rather than postulating it. The σ(v) cliff is robust to the exact shape; the sub-v\* profile is not. [O]" In v0.1 the self-interaction of [conjugate matter](/wiki/dark-matter/conjugate-matter) χ carries a Gaussian factor in the incoming relative momentum k, where an ordinary force depends on the momentum transfer q; the gate's existence was a postulate [P] (#1 §3; [the velocity gate](/wiki/dark-matter/conjugate-matter/velocity-gate)). On the two forms the gate's exponent takes in #1 and calc note #6, see flag 17 in `review/wiki-build-flags.md`.
3. "Stream-instability growth rate γ vs. orbital phase-mixing: determines whether Prediction 3's granularity survives in Milky-Way-like halos. [O]" The notebook expected the gated attraction to break a halo's velocity distribution into "discrete velocity streams of width Δv ~ v\*" (#1 §5.2), the founding image of dark matter clumping in velocity rather than in space, behind rows 3 and 4 of its predictions table ([Obituary: velocity clumping, the founding image](/wiki/dark-matter/momentum-clumping/founding-image)). It called the growth rate "the theory's most important undone calculation on the astrophysics side".

The other three entries, [polarization-genesis](/wiki/dark-matter/candidates/polarization-genesis), the relic abundance and extensivity, were not named debts. The notebook's list of tags glosses its open tag as "[O] open — a debt the program owes" (#1 §0), and the debts keep the numbers of their open problems: the heading of addendum v0.2 reads "Addendum (v0.2, post Debt-3): resolution of open problem 3".

## The order of the work

Debt 3 was settled first, by calc notes #2–#4, and Debt 1 next, by #5–#8; Debt 2's mechanism came out of the first Debt-1 note. This is the creation order of `HANDOFF.md` §3, and the notes' closing plans record it: #3 plans "Chunk 3c (small)" and "Then Chunk 1a (large)", and #4 ends with "Next: Debt 1, Chunk 1a". The lab notebook recorded each step in an addendum naming its working note, v0.2 after #4 and v0.3 to v0.6 with #5 to #8. No document dates these steps; [the timeline](/wiki/history/timeline) places them in creation order. This page follows the order of the work.

## Debt 3: the stream instability

### The particle island: no growth to race

Calc note #2 (`notes/debt3a-stream-stability.md`) took the mean-field, or Vlasov, limit of the gated interaction and asked whether a smooth Maxwellian distribution of velocities is linearly unstable ([Vlasov stability and Landau damping](/wiki/dark-matter/momentum-clumping/vlasov-stability); [the gated Vlasov model](/wiki/dark-matter/momentum-clumping/gated-vlasov-model)). It found a threshold, which #11 §9 writes as g·n_gate ≥ m·min(σ, v\*)²: the attraction among co-moving neighbours must be comparable to the kinetic energy of the velocity spread. Below it, perturbations are damped, which changed the question the notebook had posed: "There is no race with orbital stirring below threshold — the flocking never starts. The earlier 'γ vs Ω' framing presumed growth exists; it exists only above this line."

At [the scattering benchmark](/wiki/dark-matter/conjugate-matter/benchmark) the fit to [dwarf-galaxy](/wiki/dark-matter/halo-astrophysics/dwarf-galaxies) cores fixes σ₀/m = 30 cm²/g, "hence g is *spent*", and the criterion falls short by 28–31 orders of magnitude (#2; 10²⁸–10³¹ in #11 §9); "the H-theorem closes the collisional route" ([the mean-field criterion and its shortfall](/wiki/dark-matter/momentum-clumping/instability-criterion)). The corollary, [the classicality theorem](/wiki/dark-matter/momentum-clumping/classicality-theorem): meeting the criterion at fixed σ₀/m "forces m ≲ 0.1 meV, where N_occ ~ 10²⁰ — collective momentum-space behavior and classical particles are mutually exclusive" (#11 §9; on the regime in which #2 evaluates it, see flag 19 in `review/wiki-build-flags.md`). With so many quanta per state, dark matter behaves as a classical wave ([occupation number](/wiki/dark-matter/wave-dark-matter/occupation-number)).

### The wave island: the race, and where it was required

Calc note #3 (`notes/debt3b-wave-island.md`) took that branch, [the wave island](/wiki/dark-matter/momentum-clumping/wave-island). A wave halo relaxes by Bose-enhanced wave kinetics, the mechanism that the Levkov–Panin–Tkachev (LPT) papers established for gravity ([wave kinetics and Bose-star formation](/wiki/dark-matter/wave-dark-matter/wave-kinetics)), and the gate adds a channel:

```text
Γ ≈ c·g²ρ²min(σ, v*)⁴/(m³σ⁶)
```

("Bose-enhanced, LPT-style [13†]; coefficients [O]", #11 §9; [the gated condensation rate](/wiki/dark-matter/momentum-clumping/wave-island/condensation-rate)). Here the race is real: streams form where Γ exceeds the orbital rate Ω = 1/t_dyn. In [Scenario A](/wiki/dark-matter/momentum-clumping/wave-island/scenario-a) the gated channel also makes the cores of classical dwarf galaxies, and "streams lose everywhere by 10²–10⁴ — *except ultra-faint dwarfs*", where condensation becomes mandatory. In Scenario B the cores come from elsewhere, the coupling is free, and "streams are *tunable*, not mandatory" across "ten orders of magnitude", which #3 calls "a degeneration flag" ([Scenario B](/wiki/dark-matter/momentum-clumping/wave-island/scenario-b)).

Calc note #4 (`notes/debt3c-ufd-endpoint.md`) followed Scenario A into the ultra-faint dwarf galaxies (UFDs). In Segue 1 the rate ratio is ~660 and condensation takes ~10⁴ yr (#11 §9). Because the gated interaction is attractive, the condensate collapses in a bosenova whenever it passes a critical mass, M_crit ≈ 2.9×10⁻³⁰(m/eV)^{−7/4} M_⊙ (#11 §9), ejecting fast waves that leave the galaxy, so the halo is drained ([attractive condensates](/wiki/dark-matter/wave-dark-matter/attractive-condensates)). The observed ultra-faint dwarfs are dense and old: "Scenario A is falsified by the existence of ultra-faint dwarfs." The light-mass branch that escapes the collapse is excluded independently ([bounds on fuzzy dark matter](/wiki/dark-matter/wave-dark-matter/fuzzy-dark-matter-bounds); [Obituary: Scenario A](/wiki/dark-matter/momentum-clumping/wave-island/scenario-a)).

### The verdict

Calc note #4 closed the debt with [the net theorem](/wiki/dark-matter/momentum-clumping/net-theorem):

> "Nowhere in the viable parameter space of BBT is velocity-space clumping a mandatory phenomenon. It is forbidden for classical-particle χ, fatal where it would have been mandatory (Scenario A), and merely optional elsewhere (Scenario B, ten tunable orders of magnitude — a degeneration flag, not a prediction)."

(`notes/debt3c-ufd-endpoint.md`, 'Verdict and closure of Debt 3'; BBT is the Broken-Born framework.) Addendum v0.2 of the notebook reports it as "Debt 3 is paid, and the answer went against the theory" and strikes rows 3 and 4 permanently; each has its obituary, [velocity-space granularity in halos (old row 3)](/wiki/dark-matter/momentum-clumping/velocity-granularity) and [Fornax friction suppression (old row 4)](/wiki/dark-matter/momentum-clumping/fornax-friction). #11 reports the result as an obituary in §9, and the handoff lists it under "Dead (killed by own calculations — keep dead)" (`HANDOFF.md` §2). After review round 3 it served as precedent: "The program's precedent is the Debt 3 obituary: a dead claim is reported prominently and stays dead" (`review/round3-adjudication.md`, 'Decisions', on retiring the [superheavy soliton candidate](/wiki/dark-matter/candidates/soliton-candidate/obituary)).

### What survived, and what remains

- **The island discriminant.** The self-interaction is cut off as a sharp knee for particle χ and as (v\*/σ)⁴ for wave χ, so the knee's shape identifies the branch (#11 §9). It is now [row 3 of the predictions table](/wiki/predictions/island-discriminant).
- **A relic abundance on the wave island**, by misalignment, like an axion (#3); the 5.4 : 1 ratio of dark to ordinary matter stays open ([relic abundance by misalignment](/wiki/dark-matter/momentum-clumping/wave-island/misalignment-relic); [Open: polarization-genesis (OP7)](/wiki/dark-matter/candidates/polarization-genesis)).
- **A quarantined sector.** #11 §15 counts the "tunable wave-island collective sector (quarantined)" among its [degeneration risks](/wiki/program/assessment).
- **The topological loophole.** Debt 3 tested collective dynamics only; a single topological object localized in momentum "remains untested, but has no candidate" (#11 §12).
- **Coefficients and checks.** The rate's coefficients are "heuristic at O(1)–O(10) level", their calibration against LPT "a flagged to-do" (#3). No `verify/` script checks any Debt-3 number, although the handoff marks the shortfall as machine-verified, "criterion fails by 10²⁸–10³¹ ✓" (`HANDOFF.md` §2); see flag 16 in `review/wiki-build-flags.md`, which points to a recomputation, `review/wiki-build-checks/debt3a_check.py`.

## Debt 1: the field equation for H

### From the plan to a restatement

Calc note #4 ends with a plan: linearize S_H on the broken vacuum, import the known spectrum of linearized [double field theory](/wiki/phase-space/born-geometry/double-field-theory), run a ghost check "with ω, η frozen", and extract the equation for the momentum-space block g̃. The plan kept the notebook's postulate P2, under which both the symplectic form ω and the neutral metric η are fixed ([Original P2](/wiki/program/postulates/original-p2)).

Calc note #5 (`notes/debt1a-geometric-core.md`, an "Overnight working note") changed the plan. Its first result, [the compatibility theorem](/wiki/phase-space/born-geometry/compatibility-theorem), showed that under P2 there was no independent momentum-space geometry for the plan to find: with ω and η both rigid, H = diag(g, g⁻¹), so g̃ = g⁻¹ ([the corollaries](/wiki/phase-space/born-geometry/compatibility-corollaries)), and "S_H is a functional of g alone: a pure metric theory. No momentum graviton, hence no geometric origin for the χ gate either" (#5 §B). The note made only ω rigid and η emergent, the [order parameter](/wiki/symmetry-breaking/order-parameter) ([P2′](/wiki/program/postulates/p2-prime)), a repair forced by [the nontriviality theorem](/wiki/program/postulates/nontriviality-theorem): "BBT has content beyond GR + SIDM iff η is emergent", GR being [general relativity](/wiki/gravity/spin-2-fields/general-relativity) and SIDM [self-interacting dark matter](/wiki/dark-matter/halo-astrophysics/self-interacting-dark-matter). With only ω rigid, H is described by [the modular field Z = X + iY](/wiki/phase-space/modular-field/modular-field-z), with Im Z the spacetime metric and Re Z = X a new symmetric tensor, the [momentum graviton](/wiki/gravity/momentum-graviton), and the debt became one sector of one field: "Born's debt, restated exactly: the field equation for momentum-space geometry is the Re Z sector of S_H" (#5 §C). The decisive computation, a classification of X at quadratic order as healthy, auxiliary or ghost, was defined and "Not completed tonight" (§D). #5 tagged the compatibility theorem "[D — rigorous]"; after review round 3 attributed it to Freidel, Leigh and Minic, #11 v2.1 re-tagged it [T][V] (#11 §5).

### X is a massive spin-2 field

Calc note #6 (`notes/debt1a-ii-X-classification.md`) found a sharper answer than any of the three outcomes. A constant shift of X is a symmetry, so X is never auxiliary ([shift symmetry](/wiki/gravity/momentum-graviton/shift-symmetry)). Locally the shifts act as δX_μν = ∂₍μλ_ν₎, so X is a second graviton ([dual diffeomorphisms](/wiki/gravity/momentum-graviton/dual-diffeomorphisms); [the symplectic partner of the graviton](/wiki/gravity/momentum-graviton/symplectic-partner)). Massless, it is excluded by [the multi-graviton no-go theorem](/wiki/gravity/spin-2-fields/multi-graviton-no-go) [T], and ungauged by the Lorentz signature. The vacuum's choice of [polarization](/wiki/phase-space/reciprocity/lagrangian-polarizations) breaks the dual diffeomorphisms, X absorbs the four would-be Goldstone modes ([Goldstone modes and the Higgs mechanism](/wiki/symmetry-breaking/goldstone-and-higgs)), and it becomes massive, with "mass M_X = the polarization-breaking scale" (§3; [why X must be massive](/wiki/gravity/momentum-graviton/forcing-chain); [the gravitational Higgs mechanism](/wiki/gravity/momentum-graviton/gravitational-higgs)). Calc note #8 §3 words the eaten modes differently, as the vector π_μ and a longitudinal scalar, and no document reconciles the two wordings ([conflicts between sources](/wiki/history/documents/source-conflicts#gravity-and-symmetry-breaking)). Massive spin-2 coupled to gravity "has exactly one known consistent structure: the Fierz–Pauli tuning at quadratic order completed by a dRGT/Hassan–Rosen-class potential" (§3), dRGT being de Rham–Gabadadze–Tolley ([dRGT massive gravity](/wiki/gravity/spin-2-fields/drgt-massive-gravity); [Hassan–Rosen bimetric gravity](/wiki/gravity/spin-2-fields/hassan-rosen-bimetric)). The verdict, "massive spin-2, conditionally healthy", came with the stakes:

> "The single remaining computation of Debt 1: derive the X-potential from the η-selection (J–Z) sector and test it against the dRGT coefficient family. Pass ⇒ the geometric core stands and 'theory' becomes the defensible word. Fail ⇒ the Boulware–Deser ghost kills the geometric sector, and BBT survives only as its phenomenological shell (gated SIDM + Maslov quintessence with the geometric story demoted to heuristics)." (#6 §5)

### The tuning test

Calc note #7 (`notes/debt1a-iii-tuning-test.md`) built the mass from a potential that penalizes misalignment between the polarization J and the modular field, through the anticommutator {J, I[Z]} ([the tuning test](/wiki/gravity/tuning-test); [the misalignment potential](/wiki/gravity/tuning-test/misalignment-potential)). Built from the metric, it fails twice: at linear order the graviton mass lacks the −(Tr h)² term of the Fierz–Pauli form, and the nonlinear structure lies outside the Hassan–Rosen family; "Every metric-tier (second-order, H-coupled) misalignment invariant tested lands off the tuning" (§2; [the metric tier fails twice](/wiki/gravity/tuning-test/metric-tier-failures); [the Fierz–Pauli mass term and the Boulware–Deser ghost](/wiki/gravity/spin-2-fields/fierz-pauli)). Built from frames, as [wedge polynomials](/wiki/gravity/spin-2-fields/vielbein-formulation) of the symplectic vielbein, it falls in the Hinterbichler–Rosen class, "ghost-free by construction" (§3; [the frame tier](/wiki/gravity/tuning-test/frame-tier)). The verdict: "the theory *fails* in second-order (metric) variables and *passes* in first-order (frame) variables", a pass conditional on the formulation the note argues the geometry prefers ([the verdict](/wiki/gravity/tuning-test/conditional-pass)), giving "Hassan–Rosen bimetric gravity with the second frame constrained to a compact moduli space Λ(d)" ([constrained bimetric gravity](/wiki/gravity/tuning-test/constrained-bimetric)).

### The palindrome and the answer

Calc note #8 (`notes/debt1a-iv-beta-coefficients.md`) computed the coefficients βₙ of the wedge potential. [Reciprocity](/wiki/phase-space/reciprocity/born-reciprocity) acts on it as the exchange of the two frames, which forces [the palindrome βₙ = β₄₋ₙ](/wiki/gravity/palindromic-branch/palindrome). Under it the potential at the aligned point is twice the tadpole, V(1) = 2T, while a flat aligned vacuum requires V(1) = T, so T = 0 and V(1) = 0: the wedge sector contributes no vacuum energy ([the vacuum-energy identity](/wiki/gravity/palindromic-branch/vacuum-energy-identity)). The five βₙ reduce to two parameters, the massless graviton is the reciprocity-even mode and X the odd one, and τ, the [dark-energy field](/wiki/cosmology/dark-energy/tau-quintessence), is not absorbed by X at leading order ([spectrum, parameters and reciprocity parity](/wiki/gravity/momentum-graviton/spectrum-and-parity); [τ is not eaten](/wiki/gravity/momentum-graviton/tau-not-eaten)). The note's §4, "Debt 1: the answer to Born", gives the answer:

> "Momentum-space geometry is carried by X = Re Z, the reciprocity-odd partner of the metric. It is a massive spin-2 field — massless is forbidden by the multi-graviton no-go, and the mass is generated by the Higgsing of dual diffeomorphisms when the vacuum selects a polarization."

([Born's answer](/wiki/gravity/momentum-graviton/borns-answer) sets it out clause by clause.) The note's status line reads "Debt 1 is structurally paid"; addendum v0.6 is headed "the β coefficients — Debt 1 closed". The algebra of #5, #7 and #8 is [Tier 1](/wiki/method/claim-tiers) in #11 §2 and machine-checked [V]: the compatibility theorem (T1), the [Siegel](/wiki/phase-space/modular-field/siegel-domain) parametrization (T2), the blocks of the misalignment potential (T3), the non-Fierz–Pauli mass (T4), the palindrome identity in exact integers (T5) and two facts about symmetric polynomials (T6, T7). In the gate's run of 2026-10-21 every check passed, T5 printing "V(1) - 2T = [0,0,0]" (`verify/battery.py`, run by `scripts/check.sh`).

### What "structurally" covers

#8 does not define the qualifier; the first item of its residue comes closest: the wedge sector's class "was selected by minimality + consistency, not derived line-by-line" (§5). The chain that forces X to be massive is "the Euclidean-rigorous skeleton" (#6 §3), derived for a positive-definite metric; its extension to the Lorentzian signature of spacetime is a separate step. #11 tags the chain [D + T] (§7.1), the tuning test and the palindrome identity [D][V] (§7.2, §7.3) and the spectrum [D] (§7.5). Debt 1 was settled as a class of dynamics, fixed by consistency and by the symmetry, rather than as a field equation derived from S_H.

Of the other pieces named in the notebook's statement of the debt, the ghost analysis was settled for the class: the frame-tier potentials are ghost-free by construction, on the Euclidean skeleton and pending the Lorentzian dressing. The section condition on curved backgrounds is in neither #8's residue nor #11 §14, and no later document settles it ([the section condition](/wiki/symmetry-breaking/section-condition#open-the-section-condition-on-curved-backgrounds)).

### What remains

#8 §5 calls its residue "none of it existential"; its five items became items of #11 §14:

| #8 §5 | Residue | #11 §14 |
| --- | --- | --- |
| (i) | first-principles reduction of the wedge sector from S_H | [OP1](/wiki/gravity/tuning-test/wedge-reduction) |
| (ii) | Lorentzian dressing of the Euclidean skeleton | [OP3](/wiki/phase-space/born-geometry/lorentzian-dressing) |
| (iii) | τ–Stückelberg mixing matrix | [OP6](/wiki/gravity/momentum-graviton/tau-stuckelberg-mixing) |
| (iv) | dual-stress enhancement parametrics | [OP5](/wiki/dark-matter/conjugate-matter/dual-stress-enhancement) |
| (v) | literature check on the Λ = 0 palindrome observation | [OP2](/wiki/gravity/palindromic-branch/pm-comparison) |

Item (v) gained weight in #11 v2.0, whose literature search found the partially massless (PM) point of bimetric gravity inside the palindromic branch (at α = 1) and downgraded the identity's novelty to "requires detailed comparison with the PM and exchange-symmetric literature" (#11 §7.4; [partially massless gravity](/wiki/gravity/spin-2-fields/partially-massless-gravity)). The word "theory" "still waits on items 1–3 above", OP1 to OP3 (#11 §15; [Assessment](/wiki/program/assessment)), and the partially-massless comparison heads the current queue (root `CLAUDE.md`, 'Since the handoff').

Two consequences lie outside that list. Reciprocity makes the two effective Planck masses equal (#8 §3), and the cosmological stability of a heavy X at equal Planck masses is open (`review/v3-worklog.md`, item R7; [Open: stability at equal Planck masses](/wiki/gravity/momentum-graviton/equal-planck-mass-stability)). And #6 §4 noted, as "A new door, deliberately left closed today", that oscillations of a massive X are themselves a dark-matter candidate, now one of the checkpoint's two ([the X-condensate candidate](/wiki/dark-matter/candidates/x-condensate)).

## Debt 2: the gate

### The mechanism

Debt 2's mechanism came out of the first Debt-1 note, subtitled "(plus an unplanned payment on Debt 2)". Its §E, "Debt 2 — the mechanism, found [D — structural]", traces the gate to the modular field. Conjugate matter couples to H universally (postulate [P4](/wiki/program/postulates/p4-polarized-matter)), and to the X block through its [dual stress T̃](/wiki/dark-matter/conjugate-matter/dual-stress); "Exchange of X between two such bilinears yields a four-point amplitude that depends on the incoming relative momenta of the pair — the variable no x-local mediator can produce, and exactly the variable the gate was postulated in." The note's summary:

```text
gate = momentum-graviton exchange,    μ ↔ (M_X, M_B) parametrically
```

The shape it left open: "The gate shape is the X propagator's structure on the momentum fibers — open [O]" (#5 §E). Addendum v0.3 records the step as an upgrade of open problem 2: "the mechanism is X-exchange between χ dual-stress bilinears, which produces dependence on incoming relative momenta — the defining property of the gate; the shape awaits the X propagator."

Calc note #6 completed the identification (§4; [the gate mechanism](/wiki/dark-matter/conjugate-matter/gate-mechanism)). Integrating out the massive X between χ bilinears gives a contact interaction, and the χ quanta are "extended objects on the momentum fiber with width μ, and they exchange X only over their fiber overlap", which the note calls "the dual of how x-extended composites acquire form factors F(qR)": a contact force acts where two waveforms overlap, and the gate acts only where their spectra overlap as well. Gaussian profiles reproduce the postulated Gaussian gate, with μ the quantum's own momentum width in place of #5's relation to M_X and M_B; generic vertices give power-law tails. The notebook's lead prediction was downgraded accordingly: "row 1's 'exponential cliff' weakens to 'sharp knee at v\*, with the tail shape (Gaussian vs rational) a diagnostic of the vertex completion.'" (the note writes v_\* for v\*; [row 1](/wiki/predictions/self-interaction-knee); [the cliff, superseded](/wiki/predictions/self-interaction-knee#superseded-the-exponential-cliff-of-v01)). #8 §5 records the debt as "Debt 2: mechanism paid (X-exchange, μ = fiber width); shape completion open (Gaussian vs rational tail — now also an observable discriminant)", and #11 §8 tags it "[D — mechanism; shape [O]]".

### What remains

- **The shape** ([Open: the gate shape (OP4)](/wiki/dark-matter/conjugate-matter/gate-shape)). Gaussian or rational depends on the X propagator on the momentum fibers and on the profile of a χ quantum, and no document computes either. The tail is observable, since in σ_T(v) the "tail (Gaussian vs rational) diagnoses the vertex completion" (#11 §8); #11 §15 lists "gate tail not yet forced" among the degeneration risks.
- **The strength** ([Open: the dual-stress enhancement (OP5)](/wiki/dark-matter/conjugate-matter/dual-stress-enhancement)). The mechanism explains the gate's variable, not its strength: "the dual-stress enhancement (nuclear-scale σ₀ with gravitational SM couplings)" is #11 §8's "Main open quantitative item", SM being the Standard Model. #8 §5 files it under Debt 1, as "(gate strength vs gravitational SM coupling)".
- **A convention.** #6 writes the Gaussian gate as e^{−(p₁−p₂)²/2μ²}, the notebook as e^{−k²/μ²}; a suspected factor of √2 in μ between them is flag 17 in `review/wiki-build-flags.md` ([two conventions, not reconciled](/wiki/dark-matter/conjugate-matter/velocity-gate#two-conventions-not-reconciled)).
- **No computation, no check.** No source writes the χ–X vertex, the propagator or the overlap integral, and no `verify/` script covers the mechanism ([scope and caveats](/wiki/dark-matter/conjugate-matter/gate-mechanism#scope-and-caveats)).

## The names across the documents

| Document | Debt 1 | Debt 2 | Debt 3 |
| --- | --- | --- | --- |
| #1 §11, v0.1 | open problem 1, "Born's 88-year debt" | open problem 2 | open problem 3 |
| Titles of the calc notes | "Debt 1, Chunk A" to "Chunk A-iv" (#5–#8) | the subtitle of #5 | "Debt 3, Chunk A" to "Chunk C" (#2–#4) |
| Addenda of #1 | v0.3 to v0.6, the last headed "Debt 1 closed" | v0.3 and v0.4 | v0.2, "post Debt-3" |
| #9, v1.0 | §5, "(Debt 1: paid)" | §6, "(Debt 2: mechanism paid)" | §7, "(Debt 3: closed, negative)" |
| #11 | §7, "(Debt 1)" | §8, "(Debt 2)" | §9, "(Debt 3)", an obituary |
| `HANDOFF.md` §3 | #8 "closes Debt 1 (structural)" | #5 "pays Debt 2's mechanism" | #4 "closes Debt 3 (negative)" |

The labels for Debt 1 differ in strength: the notebook's v0.6 heading says "Debt 1 closed" and #9 "(Debt 1: paid)", while #8 and the handoff qualify the result as structural and #11 keeps its residue open in §14. By the order of precedence #11's reading stands ([what "structurally" covers](#what-structurally-covers); [conflicts between sources](/wiki/history/documents/source-conflicts#gravity)).

Documents written after the move to this repository use the names only for this finished work, as in "the Debt-3 loophole" (#11 §12); new work is tracked as #11 §14's open problems and the queue of the root `CLAUDE.md` ([open problems and the queue](/wiki/status/open-problems)). In this wiki the results of Debt 1 are under [gravity and the momentum graviton](/wiki/gravity), of Debt 2 under [conjugate matter and the velocity gate](/wiki/dark-matter/conjugate-matter), and of Debt 3 under [momentum clumping (Debt 3)](/wiki/dark-matter/momentum-clumping). The notes as documents are described on [the Debt-3 calc notes](/wiki/history/documents/debt-3-notes) and [the Debt-1 calc notes](/wiki/history/documents/debt-1-notes), and the renumbering of the predictions after Debt 3 on [the history of the predictions table](/wiki/predictions/table-history).

## Statements awaiting a ruling

The wiki's verifiers flagged suspected errors in the documents of all three debts; the wiki quotes the documents as written, and each item of `review/wiki-build-flags.md` awaits Paul's ruling:

- **Debt 1.** Item 1, the η-null polarizations that #5 §B calls discrete (the conclusion survives, per the flag); items 3, 4 and 14, the zero set of the misalignment potential, a term missing from the expansion of S and a notational point (#7 §2); item 15, a wording about η (#6 §2); item 5, "M_X ∝ 2(β₁+β₂)" (#11 §7.5 and #9, from #8 §3); item 7, #11 §7.1's "The unique consistent structure", which drops #6 §3's "known"; item 8, #8 §3's "five-function freedom"; item 6, "by symmetry rather than tuning" (#1 v0.6, #10); item 23, the identification of the constraint a·ã = 1 with the |Z| = 1 locus, flagged in #11 §6 and §10 and also made in #5 §C, in the notebook's addendum v0.3 and in `HANDOFF.md` §2.
- **Debt 2.** Item 17, the √2 in μ between the two gate conventions.
- **Debt 3.** Item 16, the handoff's ✓ on a number no script checks; item 19, the regime in which #2 evaluates the classicality corollary.

## Sources

- `papers/broken-born-checkpoint-v2.md` §7–§9 — the current statements under the three labels, their tags, the rate and the numbers of Debt 3; §2 — Tier 1; §5 — the compatibility theorem re-tagged in v2.1; §12 — the loophole without a candidate; §14 — the open items the debts left; §15 — what the word "theory" waits on, and the degeneration risks
- `review/round3-adjudication.md` 'Decisions' — the Debt-3 obituary as precedent
- `HANDOFF.md` §3 — each calc note's outcome for its debt; §2 — the dead list and the ✓ without a script
- `notes/debt3a-stream-stability.md`, `notes/debt3b-wave-island.md`, `notes/debt3c-ufd-endpoint.md` — Debt 3 step by step: the threshold, the shortfall and the classicality corollary; the wave island and its two scenarios; the ultra-faint-dwarf endpoint, the verdict, and the plan for Debt 1
- `notes/debt1a-geometric-core.md` §A–§F — the compatibility theorem, the repair of P2, the restatement of Born's debt, the defined computation, and Debt 2's mechanism (§E)
- `notes/debt1a-ii-X-classification.md` §1–§5 — the classification of X, the stakes of the tuning test, the width μ and the downgrade of row 1 (§4)
- `notes/debt1a-iii-tuning-test.md` §1–§5 — the tuning test and its verdict
- `notes/debt1a-iv-beta-coefficients.md` §1–§5 — the palindrome, the vacuum-energy identity, the answer to Born, and the state of all three debts at the close (§5)
- `notes/broken-born-theory.md` §0, §3, §5.2, §11, §12 — the gloss of [O], the postulated gate, the stream picture, the debts as open problems 1–3; 'Addendum (v0.2)' to 'Addendum (v0.6)' — each step as the notebook recorded it
- `notes/broken-born-program-v1.md` §5–§7 — v1.0's section labels
- `verify/battery.py` — tests T1–T7 of the Debt-1 algebra
- `review/v3-worklog.md` 'Round-2 pending list', item R7 — stability at equal Planck masses left open
- `review/wiki-build-flags.md` items 1, 3–8, 14–17, 19, 23 — suspected errors in the debts' documents, awaiting a ruling
