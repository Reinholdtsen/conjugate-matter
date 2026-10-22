---
title: "Inflation, reheating and entropy dilution"
weight: 20
status: established
description: "How inflation dilutes relics, reheating sets the temperature, and later entropy injection or early matter domination dilutes them again — the survival routes the retired candidate would have needed."
provenance: [T]
sources:
  - "papers/broken-born-checkpoint-v2.md §11.1"
  - "papers/broken-born-checkpoint-v2.md §12"
  - "papers/broken-born-checkpoint-v2.md §13 row 8"
  - "papers/broken-born-checkpoint-v2.md §14 item 7"
  - "papers/broken-born-checkpoint-v2.md App. A item 5"
  - "review/round3-adjudication.md 'Rulings' 2"
  - "review/round3-adjudication.md 'Rulings' 3"
  - "review/round3-adjudication.md 'Rulings' (omitted constraints)"
  - "review/round3-adjudication.md 'Decisions' 1"
  - "review/round3-adjudication.md 'Decisions' 2"
  - "review/round3/referee/audit-notes.md Step 2"
  - "review/round3/referee/audit-notes.md Step 4(a) item 5"
  - "review/round3/referee/audit-notes.md Step 4(c) items 1, 7, 9"
  - "review/round3/referee/step2a.out 'Kibble'"
  - "review/round3/referee/step4c.out"
  - "review/v3-worklog.md 'Findings neither referee raised'"
  - "notes/knot-dark-matter-standalone.md §3"
  - "notes/knot-dark-matter-standalone.md §4"
  - "notes/knot-dark-matter-standalone.md §6"
  - "notes/broken-born-theory.md §8"
  - "HANDOFF.md §2"
---

*Inflation is a proposed early period of extremely rapid, accelerating expansion, which thins any relics produced before it until essentially none remain in the observable universe; reheating is its end, when the energy that drove inflation turns into hot particles and sets the starting temperature of the [radiation era](/wiki/cosmology/early-universe/radiation-era). Relics made after reheating can still be thinned later if something releases a large amount of entropy into the plasma, for example the decay of heavy particles that dominated the universe for a time, a period called early matter domination. The program uses this physics in two places. Inflation is the standard reason no [magnetic monopoles](/wiki/electric-magnetic-duality/monopoles) of our own sector are seen, which is one of the two reasons the early claim that the conjugate sector explains their absence is [dead](/wiki/electric-magnetic-duality/monopole-explanation). And late dilution was the only way the [retired soliton dark-matter candidate](/wiki/dark-matter/candidates/soliton-candidate/obituary) could have kept its heavy mass, a route the program rejected because it removes the mass prediction.*

**Status:** Established — [T] — textbook early-universe physics, written here from general knowledge; references the wiki adds are from model memory (†). How the program used it is recorded in [checkpoint #11](/wiki/history/documents/checkpoint) §11.1 and §12 and in [round-3 Decision 2](/wiki/method/review/round-3/decisions). The numbers on this page come from the retired soliton episode, and no script in `verify/` checks a dilution factor; the overproduction they rest on is [V] ([ruling 2](/wiki/method/review/round-3/rulings)).

## Inflation [T]

### What it is

Inflation is a period in which the expansion of the universe accelerates, ä > 0. By the second Friedmann equation this requires a pressure below −ρ/3 ([Friedmann cosmology and minisuperspace](/wiki/cosmology/scale-factor-duality/friedmann-cosmology)). The standard source is a scalar field, the inflaton, whose energy is mostly potential energy: its equation of state is then close to w = −1, the Hubble rate H is nearly constant, and the scale factor grows nearly exponentially, a ∝ e^{Ht}. The amount of inflation is counted in e-folds, N = ln(a_end/a_start).

Inflation was proposed to explain why the universe is so nearly spatially flat, why regions that could never have exchanged signals in a standard hot Big Bang have the same temperature, and why no relic magnetic monopoles are seen (Guth 1981 †). The quantum fluctuations of the inflaton, stretched to cosmic size, seed the density perturbations seen in the cosmic microwave background, and those of the metric leave a primordial background of gravitational waves ([gravitational waves from phase transitions](/wiki/cosmology/early-universe/phase-transition-gravitational-waves#primordial-backgrounds-t)) [T]. Inflation is the standard account, though not a directly observed epoch; the program's documents use it as literature [T].

### How it dilutes relics

A relic present before or during inflation keeps its number of particles while the volume grows by e^{3N}, so its number density falls by that factor. The inflaton's energy density meanwhile stays nearly constant. When inflation ends, that energy is converted into a hot plasma with a large entropy, so the relic's yield, its number per unit entropy ([the radiation era](/wiki/cosmology/early-universe/radiation-era)), ends up suppressed by an enormous factor. For the number of e-folds inflation needs for its other purposes, fewer than one pre-inflationary relic remains in the observable universe [T].

This is the standard resolution of [the monopole problem](/wiki/electric-magnetic-duality/monopoles/monopole-problem): grand unified theories predict superheavy monopoles from a symmetry-breaking transition at very high temperature, too many of them if nothing intervenes (Preskill 1979), and inflation after that transition removes them [T].

## Reheating [T]

### The start of the radiation era

At the end of inflation the inflaton oscillates about the minimum of its potential and decays. Its decay products scatter, thermalize, and form a hot plasma whose temperature, the reheating temperature T_RH, is the starting point of [the radiation era](/wiki/cosmology/early-universe/radiation-era) [T]. Everything the hot early universe produces later, thermal relics and defects alike, is produced after reheating, and so is not diluted by inflation.

### Ordering: which relics survive

Whether a symmetry-breaking transition at temperature T_c leaves defects depends on its place relative to inflation and reheating [T]:

- if T_c lies above the temperature the plasma reaches after reheating, the symmetry is never restored after inflation; defects formed before inflation are diluted away, and none form afterwards;
- if the plasma after reheating is hotter than T_c, the symmetry is restored and then breaks again as the plasma cools, and defects form after inflation with at least the count of [the Kibble mechanism](/wiki/electric-magnetic-duality/monopoles/kibble-mechanism), undiluted by it.

The withdrawn soliton manuscript [#14](/wiki/dark-matter/candidates/soliton-candidate) needed the second case, since its abundance was the Kibble count "at a post-inflationary transition with T_c ~ v", where v is the hidden symmetry-breaking scale. It stated the requirement: "Inflation must precede the hidden transition, and v must lie below the reheating temperature" (#14 §3).

### A hidden sector reheated colder

If the inflaton, or whatever reheats the universe, decays into two sectors that do not interact, each sector thermalizes separately, and they can start at different temperatures. Their ratio, the hidden-to-visible temperature ratio ξ, is then set by the decay, and it persists only while the two sectors stay out of contact [T]. #14 needed ξ below 1 to keep the contribution of its [hidden sector](/wiki/dark-matter/candidates/soliton-candidate/hidden-sector)'s massless photon to the radiation density within the measured bound: it required "the hidden sector to have been reheated to xi < 0.77 of our temperature, an assumption about reheating that the framework does not fix" (#14 §4), and its self-assessment listed "the colder reheating of the hidden sector" as conjectural (#14 §6). [Round 3](/wiki/method/review/round-3) corrected the bound to ξ < 0.760 [V] (ruling 5; [the hidden sector's thermal history](/wiki/dark-matter/candidates/soliton-candidate/hidden-thermal-history)).

These are requirements of the retired candidate, and the numbers below belong to the soliton episode. The round-3 referee listed what a colder start would demand of reheating (`review/round3/referee/audit-notes.md`, Step 4(c) item 9):

> Reheating: requires visible T_RH >~ v/xi = 1.06e12 - 1.90e12 GeV (step4c.out) and a two-field (or asymmetric) reheating mechanism for xi; a separately reheated hidden sector can carry dark-radiation isocurvature (conditional; not computed).

The two values are those of `step4c.out` for v = 8.092×10¹¹ and 1.446×10¹² GeV, the ends of v3's range for the symmetry-breaking scale, at ξ = 0.76. The division by ξ has a plain reading (the wiki's): a hidden plasma colder by the factor ξ reaches the temperature v only when the visible plasma is at v/ξ, so the visible plasma after reheating must be at least that hot for the hidden transition to happen after inflation.

A cold start also has to survive later contact between the sectors. The referee found two ways it could be lost. A Higgs-portal coupling between the two scalar sectors, allowed by every stated symmetry, would equilibrate them if large enough: "equilibration at T~v for lambda_p >~ 5e-2 (rough 2->2 estimate) would set xi=1 -> Delta N = 0.86 (excluded). Technically natural to set small, but unstated" (Step 4(c) item 7). And with a [kinetic-mixing](/wiki/dark-matter/candidates/soliton-candidate/kinetic-mixing) parameter in v3's range, ordinary matter would produce the hidden fermion [ψ](/wiki/dark-matter/candidates/soliton-candidate/psi-relic-window) fast enough that "The hidden sector is re-thermalised below v and the reheating ratio xi is no longer the operative variable" (Step 4(a) item 5). Decision 1 of the round-3 adjudication, strict sector separation under postulate [P4](/wiki/program/postulates/p4-polarized-matter), closes the second channel among others. The adjudication took the referee's list of omitted constraints, including "The reheating mechanism for ξ", "as a to-do; not individually re-checked"; it became moot when the candidate was retired.

### Isocurvature

Cosmological perturbations come in two kinds [T]. In adiabatic perturbations every component is compressed or rarefied together, so the ratios of number densities, such as n/s, are the same everywhere. In isocurvature perturbations those ratios vary from place to place while the total density does not. Single-field inflation produces adiabatic perturbations; a second field that sets the abundance of one component can add isocurvature, and the cosmic microwave background limits isocurvature to a small fraction of the total [T]. A hidden sector heated by a separate field, whose value fluctuated during inflation, would have a temperature ratio ξ that varies across the sky, which is the "dark-radiation isocurvature" of the referee's item 9 (the wiki's reading). The referee marked it "(conditional; not computed)" and added: "No CMB-scale monopole isocurvature expected from post-inflation production (inference, not computed)", where CMB is the cosmic microwave background.

## Entropy dilution after reheating [T]

### Early matter domination

A heavy, long-lived species, or a field oscillating about its minimum, behaves as matter: its energy density falls as a⁻³ while that of radiation falls as a⁻⁴. If it lives long enough, it overtakes the radiation and the universe passes through a period of early matter domination. When it finally decays, its energy becomes radiation and the entropy in a comoving volume grows by some factor D [T]. Every yield Y = n/s fixed before the decays is divided by D; relics made afterwards are not affected. The dilution is indiscriminate: it also dilutes any baryon asymmetry made earlier ([relic abundance mechanisms](/wiki/dark-matter/candidates/relic-abundance)), and the decays must be over before nucleosynthesis, which needs the standard radiation-dominated expansion [T].

### How much a relic needs

The dilution a relic needs is its overproduction factor: the ratio of the density it would have to the density observed. For monopoles counted by the Kibble mechanism the factor grows steeply with mass. #14 §3: "Heavier monopoles are over-produced as (M/M\*)^4 and need that much entropy dilution - about 1e10 at M = 1e16 GeV", where M\* is the mass at which the undiluted abundance matches the [dark matter](/wiki/dark-matter). The fourth power comes from the yield growing as the cube of the transition temperature, which scales with M, times one more power of M in the mass density ([overproduction at the benchmark](/wiki/dark-matter/candidates/soliton-candidate/overproduction)).

These figures belong to the retired soliton episode, and they moved when round 3 corrected the count ([Obituary: the Kibble normalization](/wiki/dark-matter/candidates/soliton-candidate/kibble-normalization)):

| Case | Dilution needed | Source |
|---|---|---|
| M = 10¹⁶ GeV against M\* = 3×10¹³ GeV, as v3 took it | "1.24e10" | audit notes Step 2; `step2a.out` |
| M = 10¹⁶ GeV against the corrected M\* | "2.6e13" | audit notes Step 2 ("input M\* wrong") |
| v3's benchmark, 3×10¹³ GeV, at minimum production | 2.1×10³–1.2×10⁴ [V] | ruling 2; #11 §12 |

The last row is gated in `verify/soliton_obituary.py` as an overproduction factor ([the soliton-obituary script](/wiki/method/verification/soliton-obituary-script)); the dilution it implies is the adjudication's reading of it ("at least 10³–10⁴", Decision 2). Realistic production makes more monopoles than the minimum, so the required dilution is larger again: "probably far more (ruling 3)".

### The literature's version

The published analysis of hidden-sector monopoles reaches the same structure. Ruling 3 reads the 2026 paper of Liveoak–Maharana–Wells (LMW) as finding that "hidden monopoles overclose for breaking scales ≳ 100 PeV unless diluted, e.g. by early matter domination", and #11 §12 states it as "Hidden-sector monopoles avoid overclosing the universe only for symmetry-breaking scales ≲ 100 PeV, or with a period of early matter domination [29S]" ([topological dark matter in the literature](/wiki/dark-matter/candidates/soliton-candidate/prior-art)).

## How the program uses it

### Inflation and our own monopoles

The program began with the supposition that monopoles live in conjugate space, which would explain why none of ours are seen ([founding suppositions](/wiki/program/founding-suppositions)). The [checkpoint](/wiki/history/documents/checkpoint) killed that explanation on two grounds (#11 §11.1): "As an explanation of the null result: dead — the relevant duality is electric–magnetic (E↔B, g → 1/g), not x↔p, and inflationary dilution already accounts for absence [T]." The [handoff](/wiki/history/documents/handoff) lists it among the dead claims as "wrong duality; inflation suffices" (`HANDOFF.md` §2), and #11's Appendix A records the split: "as explanation, dead (wrong duality; inflation suffices); as ontology, alive and consequence-bearing" (App. A item 5). The second ground is this page's physics: since inflation already removes our sector's monopoles, their absence needs no further explanation ([Obituary: conjugate monopoles explain the null result](/wiki/electric-magnetic-duality/monopole-explanation)). The program still predicts a permanent null for monopoles of our sector, [row 8](/wiki/predictions/monopole-null).

### The soliton candidate's survival routes

The soliton candidate was retired after round 3 ([Obituary: superheavy conjugate solitons](/wiki/dark-matter/candidates/soliton-candidate/obituary)). Its manuscript had placed the monopole mass by the Kibble abundance "with no dilution required" (#14 abstract). Decision 2 of the round-3 adjudication explains why that mattered: "The row earned its place in the checkpoint's trilemma on two claims: topology makes it stable for free, and the mass came out of the abundance with no free dilution. Round 3 removed the second." The decision set out three routes ([round-3 decisions and lessons](/wiki/method/review/round-3/decisions)):

- **(a)** Claim the low-scale model: "Route (a), v ≲ 100 PeV, works", but the program does not claim it; the surviving version is noted as prior art, because it "is Murayama–Shu's and Liveoak–Maharana–Wells's model" and "claiming it would add no testable content and would misattribute it".
- **(b)** Keep a superheavy mass and name a dilution mechanism: rejected. "Route (b) restores the mass only by adding a free dilution factor of at least 10³–10⁴ (ruling 2), probably far more (ruling 3). The mass would then no longer be a prediction".
- **(c)** Retire the candidate: chosen.

Why a free dilution factor removes the prediction follows from the scaling above. Without dilution, the requirement that the monopoles make up exactly the observed dark matter fixes one mass, M\*. With a dilution factor D left free, any heavier mass fits by choosing D in proportion to (M/M\*)⁴, so the abundance no longer selects a mass. #11 §12: "Superheavy masses survive only with a free dilution factor. That removes the mass prediction, which was the candidate's reason to exist."

The superheavy alternative had been kept open before round 3. On 2026-10-19 Paul decided to "move the benchmark to M ≈ 3×10¹³, and keep 10¹⁶ with its ~10¹⁰ dilution as a stated alternative" (`review/v3-worklog.md`, finding F1). That dilution figure rested on the uncorrected count and is superseded ([overproduction at the benchmark](/wiki/dark-matter/candidates/soliton-candidate/overproduction)); the alternative itself became route (b).

### Reheating in polarization-genesis

[The lab notebook](/wiki/history/documents/lab-notebook)'s sketch of [polarization-genesis](/wiki/dark-matter/candidates/polarization-genesis), the open question of what sets the ratio of dark to ordinary matter, also places the decisive event at reheating: "at reheating, the heavy Grassmannian moduli (the nine non-Maslov directions) decay", and their branching into x- and p-polarized quanta is set by an angle of the vacuum's polarization (#1 §8, tagged "[O, sketched]"). As with a colder hidden sector, the relative amounts of the two kinds of matter would be fixed by how a decay at reheating divides its energy, a parallel the documents do not draw. The sketch is not a calculation, and the question is open (OP7).

## Standard references

- A. H. Guth, Phys. Rev. D 23, 347 (1981) †; A. D. Linde, Phys. Lett. B 108, 389 (1982) †; A. Albrecht, P. J. Steinhardt, Phys. Rev. Lett. 48, 1220 (1982) †: inflation and its slow-roll form.
- J. Preskill, Phys. Rev. Lett. 43, 1365 (1979): the monopole problem; #14's reference [19], checked at abstract level by the round-3 audit ([the monopole problem](/wiki/electric-magnetic-duality/monopoles/monopole-problem)).
- E. W. Kolb, M. S. Turner, *The Early Universe* (Addison-Wesley, 1990): #14's reference [17]; a standard treatment of inflation, reheating and entropy production.
- R. J. Scherrer, M. S. Turner, Phys. Rev. D 31, 681 (1985) †: entropy production by decaying particles.
- H. Murayama, J. Shu (2010), arXiv:0905.1720 [28S], and D. Liveoak, A. Maharana, J. D. Wells (2026), arXiv:2607.20843 [29S]: hidden-sector monopoles and the dilution they need, as #11 cites them.

The † entries are from model memory and unverified.

## Used by

- [Obituary: superheavy conjugate solitons](/wiki/dark-matter/candidates/soliton-candidate/obituary) — the free-dilution route, rejected.
- [Overproduction at the benchmark](/wiki/dark-matter/candidates/soliton-candidate/overproduction) — the dilution a mass above M\* would need.
- [Topological dark matter in the literature](/wiki/dark-matter/candidates/soliton-candidate/prior-art) — early matter domination as the escape above about 100 PeV.
- [The hidden sector's thermal history](/wiki/dark-matter/candidates/soliton-candidate/hidden-thermal-history) — a colder reheated hidden sector and the reheating it needs.
- [Obituary: conjugate monopoles explain the null result](/wiki/electric-magnetic-duality/monopole-explanation) — "inflationary dilution already accounts for absence".
- [Row 8: no monopoles of our sector](/wiki/predictions/monopole-null) — the permanent null for our sector, whose absence #11 §11.1 attributes to inflationary dilution.
- [Open: polarization-genesis and the 5.4 : 1 ratio (OP7)](/wiki/dark-matter/candidates/polarization-genesis) — the lab notebook's sketch sets its decisive event at reheating.
- [The monopole problem](/wiki/electric-magnetic-duality/monopoles/monopole-problem) — inflation as the standard resolution.
- [Round-3 decisions and lessons](/wiki/method/review/round-3/decisions) — Decision 2 and its three routes.

## Sources

- `papers/broken-born-checkpoint-v2.md` §11.1 — inflationary dilution [T] and the dead monopole explanation; App. A item 5 — the split fate of the supposition
- `papers/broken-born-checkpoint-v2.md` §12 — early matter domination [29S] and the free dilution factor in the soliton obituary; §13 row 8 — the permanent null for our monopoles; §14 item 7 — polarization-genesis open (OP7)
- `review/round3-adjudication.md` 'Decisions' 1, 2 — strict sector separation; the three routes and the rejected dilution route; 'Rulings' 2, 3 — the overproduction and the literature; the omitted-constraints list
- `review/round3/referee/audit-notes.md` Step 2 — the dilution at 10¹⁶ GeV; Step 4(a) item 5 — re-thermalization by ψ; Step 4(c) items 1, 7, 9 — the literature, the Higgs portal, the reheating requirement and isocurvature
- `review/round3/referee/step2a.out` 'Kibble', `review/round3/referee/step4c.out` — the referee's printed dilution and reheating values
- `review/v3-worklog.md` 'Findings neither referee raised' (F1) — the superheavy alternative kept before round 3 (superseded)
- `notes/knot-dark-matter-standalone.md` §3, §4, §6 — the withdrawn candidate's ordering requirement, its colder hidden sector and the dilution scaling (withdrawn)
- `notes/broken-born-theory.md` §8 — polarization-genesis at reheating [O, sketched]
- `HANDOFF.md` §2 — "wrong duality; inflation suffices"
