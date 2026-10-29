---
title: "Inflation, reheating and entropy dilution"
weight: 20
status: established
description: "How inflation dilutes relics, reheating sets the temperature (at most 5.7×10¹⁵ GeV for instantaneous reheating) and creates the radiation's entropy, and later entropy injection or early matter domination dilutes relics again — the survival routes the retired candidate would have needed."
provenance: [T]
sources:
  - "papers/broken-born-checkpoint-v2.md §11.1"
  - "papers/broken-born-checkpoint-v2.md §12"
  - "papers/broken-born-checkpoint-v2.md §13 row 8"
  - "papers/broken-born-checkpoint-v2.md §14 item 7"
  - "papers/broken-born-checkpoint-v2.md App. A item 5"
  - "papers/phase-space-diameter.md §3"
  - "papers/phase-space-diameter.md §6"
  - "papers/phase-space-diameter.md 'References'"
  - "verify/phase_space_diameter.py 'Where the radiation rectangle is square, lambda = l_P (note §6)'"
  - "review/round3-adjudication.md 'Rulings' 2"
  - "review/round3-adjudication.md 'Rulings' 3"
  - "review/round3-adjudication.md 'Rulings' (omitted constraints)"
  - "review/round3-adjudication.md 'Decisions' 1"
  - "review/round3-adjudication.md 'Decisions' 2"
  - "review/round3/referee/audit-notes.md Step 4(a) item 5"
  - "review/round3/referee/audit-notes.md Step 4(c) items 1, 7, 9"
  - "review/round3/referee/step4c.out"
  - "notes/knot-dark-matter-standalone.md §3"
  - "notes/knot-dark-matter-standalone.md §4"
  - "notes/knot-dark-matter-standalone.md §6"
  - "notes/broken-born-theory.md §8"
  - "HANDOFF.md §2"
  - "HANDOFF.md §4"
  - "review/wiki-build-flags.md item 59"
  - "review/wiki-build-flags.md item 62"
---

*Inflation is a proposed early period of extremely rapid, accelerating expansion, which thins any relics produced before it until essentially none remain in the observable universe; reheating is its end, when the energy that drove inflation turns into hot particles and sets the starting temperature of the [radiation era](/wiki/cosmology/early-universe/radiation-era). Relics made after reheating can still be thinned later if something releases a large amount of entropy into the plasma, for example the decay of heavy particles that dominated the universe for a time, a period called early matter domination. The program uses this physics in three places. Inflation is the standard account of why no [magnetic monopoles](/wiki/electric-magnetic-duality/monopoles) of our own sector are seen. It is one of several standard histories under which their absence is expected, and because the absence is expected anyway, it lends no support to the early claim that the conjugate sector explains it: one of the two reasons that claim is [dead](/wiki/electric-magnetic-duality/monopole-explanation). And late dilution was the only way the [retired soliton dark-matter candidate](/wiki/dark-matter/candidates/soliton-candidate/obituary) could have kept its heavy mass, a route the program rejected because it removes the mass prediction. And the note on the [phase-space diameter relation](/wiki/cosmology/scale-factor-duality/phase-space-diameter) dates the radiation's entropy, the count of quantum cells in that relation, from reheating, and uses the upper limit on the reheating temperature to show that the radiation's extents in position and in momentum, in Planck units, have been far from equal ever since: one of the grounds on which an early-chat claim that they were equal at a bounce is [withdrawn](/wiki/cosmology/scale-factor-duality/square-at-the-bounce).*

**Status:** Established — [T] — textbook early-universe physics, written here from general knowledge; references the wiki adds are from model memory (†). How the program used it is recorded in [checkpoint #11](/wiki/history/documents/checkpoint) §11.1 and §12 and in [round-3 Decision 2](/wiki/method/review/round-3/decisions). Most numbers on this page come from the retired soliton episode, and no script in `verify/` checks a dilution factor; the overproduction they rest on is [V] ([ruling 2](/wiki/method/review/round-3/rulings)). The limit on the energy scale of inflation that the phase-space-diameter note uses is literature [S]; the note's conversion of it into a reheating temperature, and the radiation's aspect ratio at that temperature, are [V] (`verify/phase_space_diameter.py`; [the phase-space-diameter script](/wiki/method/verification/phase-space-diameter-script)).

## Inflation [T]

### What it is

Inflation is a period in which the expansion of the universe accelerates, ä > 0. By the second Friedmann equation this requires a pressure below −ρ/3 ([Friedmann cosmology and minisuperspace](/wiki/cosmology/scale-factor-duality/friedmann-cosmology)). The standard source is a scalar field, the inflaton, whose energy is mostly potential energy: its equation of state is then close to w = −1, the Hubble rate H is nearly constant, and the scale factor grows nearly exponentially, a ∝ e^{Ht}. The amount of inflation is counted in e-folds, N = ln(a_end/a_start).

Inflation was proposed to explain why the universe is so nearly spatially flat, why regions that could never have exchanged signals in a standard hot Big Bang have the same temperature, and why no relic magnetic monopoles are seen (Guth 1981 †). The quantum fluctuations of the inflaton, stretched to cosmic size, seed the density perturbations seen in the [cosmic microwave background](/wiki/cosmology/early-universe/cosmic-microwave-background#where-they-come-from), and those of the metric leave a primordial background of gravitational waves ([gravitational waves from phase transitions](/wiki/cosmology/early-universe/phase-transition-gravitational-waves#primordial-backgrounds-t)) [T]. Once stretched beyond the Hubble radius, these fluctuations are left in strongly squeezed quantum states ([squeezed cosmological perturbations](/wiki/cosmology/early-universe/squeezed-perturbations)) [T]. Inflation is the standard account, though not a directly observed epoch; the program's documents use it as literature [T].

### How it dilutes relics

A relic present before or during inflation keeps its number of particles while the volume grows by e^{3N}, so its number density falls by that factor. The inflaton's energy density meanwhile stays nearly constant. When inflation ends, that energy is converted into a hot plasma with a large entropy, so the relic's yield, its number per unit entropy ([the radiation era](/wiki/cosmology/early-universe/radiation-era)), ends up suppressed by an enormous factor. For the number of e-folds inflation needs for its other purposes, fewer than one pre-inflationary relic remains in the observable universe [T].

This is the standard resolution of [the monopole problem](/wiki/electric-magnetic-duality/monopoles/monopole-problem): grand unified theories predict superheavy monopoles from a symmetry-breaking transition at very high temperature, too many of them if nothing intervenes (Preskill 1979), and inflation after that transition removes them [T].

## Reheating [T]

### The start of the radiation era

At the end of inflation the inflaton oscillates about the minimum of its potential and decays. Its decay products scatter, thermalize, and form a hot plasma whose temperature, the reheating temperature T_RH, is the starting point of [the radiation era](/wiki/cosmology/early-universe/radiation-era) [T]. Everything the hot early universe produces later, thermal relics and [defects](/wiki/symmetry-breaking/topological-defects) alike, is produced after reheating, and so is not diluted by inflation.

### How hot reheating can have been

Reheating cannot make the plasma hotter than the energy density of inflation allows, and the energy scale of inflation, E_inf, the fourth root of its energy density, is limited by the primordial gravitational waves [T]. Their amplitude is set by the Hubble rate during inflation, and so by E_inf; an upper limit on the tensor-to-scalar ratio, the power in primordial gravitational waves relative to that in density perturbations ([primordial backgrounds](/wiki/cosmology/early-universe/phase-transition-gravitational-waves#primordial-backgrounds-t)), is therefore an upper limit on E_inf [T]. The phase-space-diameter note takes the limit, a tensor-to-scalar ratio below 0.036, from BICEP/Keck 2021 [S] and the energy scale it allows, E_inf < 1.39×10¹⁶ GeV, from Soman et al. 2025 [S] (`papers/phase-space-diameter.md` §6). If the whole energy density of inflation became radiation at once, which is instantaneous reheating, the plasma would start at about 5.7×10¹⁵ GeV; any slower reheating starts it colder, because the energy density goes on falling while the inflaton decays [T]. The note therefore puts reheating "at a temperature no higher than about 5.7×10¹⁵ GeV" (§6). `verify/phase_space_diameter.py` gates the conversion, taking the radiation to be that of the Standard Model's particles ([the phase-space-diameter script](/wiki/method/verification/phase-space-diameter-script)):

```text
PASS  instant reheating at E_inf < 1.39e16 GeV: T_rh < 5.7e15 GeV; the rectangle then has A = 2.9e35  [5.710e+15 GeV, 2.920e+35]
```

The second number in that line belongs to [the program's use](#the-radiations-entropy-in-the-phase-space-diameter-relation) below.

### Ordering: which relics survive

Whether a symmetry-breaking transition at temperature T_c leaves defects depends on its place relative to inflation and reheating [T]:

- if T_c lies above the temperature the plasma reaches after reheating, the symmetry is never restored after inflation; defects formed before inflation are diluted away, and none form afterwards;
- if the plasma after reheating is hotter than T_c, the symmetry is restored and then breaks again as the plasma cools, and defects form after inflation with at least the count of [the Kibble mechanism](/wiki/electric-magnetic-duality/monopoles/kibble-mechanism), undiluted by it.

The withdrawn soliton manuscript [#14](/wiki/dark-matter/candidates/soliton-candidate) needed the second case, since its abundance was the Kibble count "at a post-inflationary transition with T_c ~ v", where v is the hidden symmetry-breaking scale. It stated the requirement: "Inflation must precede the hidden transition, and v must lie below the reheating temperature" (#14 §3).

### A hidden sector reheated colder

If the inflaton, or whatever reheats the universe, decays into two sectors that do not interact, each sector thermalizes separately, and they can start at different temperatures. Their ratio, the [hidden-to-visible temperature ratio](/wiki/cosmology/early-universe/hidden-sector-temperature#how-the-ratio-is-set-reheating-t) ξ, is then set by the decay, and it persists only while the two sectors stay out of contact [T]. #14 needed ξ below 1 to keep the contribution of its [hidden sector](/wiki/dark-matter/candidates/soliton-candidate/hidden-sector)'s massless photon to the radiation density within the measured bound: it required "the hidden sector to have been reheated to xi < 0.77 of our temperature, an assumption about reheating that the framework does not fix" (#14 §4), and its self-assessment listed "the colder reheating of the hidden sector" as conjectural (#14 §6). [Round 3](/wiki/method/review/round-3) corrected the bound to ξ < 0.760 [V] (ruling 5; [the hidden sector's thermal history](/wiki/dark-matter/candidates/soliton-candidate/hidden-thermal-history)).

These are requirements of the retired candidate, and the numbers below belong to the soliton episode. The round-3 referee listed what a colder start would demand of reheating (`review/round3/referee/audit-notes.md`, Step 4(c) item 9):

> Reheating: requires visible T_RH >~ v/xi = 1.06e12 - 1.90e12 GeV (step4c.out) and a two-field (or asymmetric) reheating mechanism for xi; a separately reheated hidden sector can carry dark-radiation isocurvature (conditional; not computed).

The two values are those of `step4c.out` for v = 8.092×10¹¹ and 1.446×10¹² GeV, the ends of v3's range for the symmetry-breaking scale, at ξ = 0.76. The division by ξ has a plain reading (the wiki's): a hidden plasma colder by the factor ξ reaches the temperature v only when the visible plasma is at v/ξ, so the visible plasma after reheating must be at least that hot for the hidden transition to happen after inflation.

A cold start also has to survive later contact between the sectors. The referee found two ways it could be lost. A Higgs-portal coupling between the two scalar sectors, allowed by every stated symmetry, would equilibrate them if large enough: "equilibration at T~v for lambda_p >~ 5e-2 (rough 2->2 estimate) would set xi=1 -> Delta N = 0.86 (excluded). Technically natural to set small, but unstated" (Step 4(c) item 7). And with a [kinetic-mixing](/wiki/dark-matter/candidates/soliton-candidate/kinetic-mixing) parameter in v3's range, ordinary matter would produce the hidden fermion [ψ](/wiki/dark-matter/candidates/soliton-candidate/psi-relic-window) fast enough that "The hidden sector is re-thermalised below v and the reheating ratio xi is no longer the operative variable" (Step 4(a) item 5). Decision 1 of the round-3 adjudication, strict sector separation under postulate [P4](/wiki/program/postulates/p4-polarized-matter), closes the second channel among others. The adjudication took the referee's list of omitted constraints, including "The reheating mechanism for ξ", "as a to-do; not individually re-checked"; it became moot when the candidate was retired.

### Isocurvature

Cosmological perturbations come in two kinds [T]. In adiabatic perturbations every component is compressed or rarefied together, so the ratios of number densities, such as n/s, are the same everywhere. In isocurvature perturbations those ratios vary from place to place while the total density does not. Single-field inflation produces adiabatic perturbations; a second field that sets the abundance of one component can add isocurvature, and the cosmic microwave background limits isocurvature to a small fraction of the total [T]. A hidden sector heated by a separate field, whose value fluctuated during inflation, would have a temperature ratio ξ that varies across the sky, which is the "dark-radiation isocurvature" of the referee's item 9 (the wiki's reading). The referee marked it "(conditional; not computed)" and added: "No CMB-scale monopole isocurvature expected from post-inflation production (inference, not computed)", where CMB is the cosmic microwave background.

## Entropy dilution after reheating [T]

### Early matter domination

A heavy, long-lived species, or a field oscillating about its minimum, behaves as matter, and if it lives long enough it dominates the universe for a time, a period of early matter domination. When it decays, its energy becomes radiation and the entropy in a comoving volume grows by some factor D [T]. Every yield Y = n/s fixed before the decays is divided by D, any baryon asymmetry made earlier included, while relics made afterwards are not affected; the decays must be over before [nucleosynthesis](/wiki/cosmology/early-universe/big-bang-nucleosynthesis#light-particles-decays-and-entropy-release) [T]. The mechanism, the size of D and its conditions are on [the relic yield Y = n/s and entropy dilution](/wiki/cosmology/early-universe/relic-yield-and-dilution#entropy-dilution-t).

### How much a relic needs

The dilution a relic needs is its overproduction factor. For monopoles counted by the Kibble mechanism it grows as (M/M\*)⁴, where M\* is the mass at which the undiluted abundance matches the [dark matter](/wiki/dark-matter) (#14 §3). At v3's benchmark of 3×10¹³ GeV the overproduction at minimum production is 2.1×10³–1.2×10⁴ [V] (ruling 2), which the adjudication reads as a dilution of "at least 10³–10⁴" (Decision 2). These figures belong to the retired soliton episode; the table of them, with the superseded figures for 10¹⁶ GeV, is on [how much dilution a relic needs](/wiki/cosmology/early-universe/relic-yield-and-dilution#how-much-dilution-a-relic-needs).

### The literature's version

Ruling 3 reads the 2026 paper of Liveoak, Maharana and Wells as finding that "hidden monopoles overclose for breaking scales ≳ 100 PeV unless diluted, e.g. by early matter domination", which #11 §12 cites as [29S] ([the literature's version](/wiki/cosmology/early-universe/relic-yield-and-dilution#the-literatures-version); [topological dark matter in the literature](/wiki/dark-matter/candidates/soliton-candidate/prior-art)).

## How the program uses it

### Inflation and our own monopoles

The program began with the supposition that monopoles live in conjugate space, which would explain why none of ours are seen ([founding suppositions](/wiki/program/founding-suppositions)). The [checkpoint](/wiki/history/documents/checkpoint) killed that explanation on two grounds (#11 §11.1, as v2.3 words it): "The relevant duality is electric–magnetic (E↔B, g → 1/g), not x↔p; only the shared-photon form of §11.4 contests this ground [O], and that form needs P4 restated" (the shared-photon form is the version of [P.R.'s magnetic-mirror conjecture](/wiki/electric-magnetic-duality/magnetic-identification#shared-photon) in which momentum-polarized partners of our charged particles carry magnetic charge of our own photon); and "the null result is expected under several standard histories, so it lends the program no support: inflation after a unification transition dilutes monopoles [T], and without grand unification there are none to dilute, since the Standard Model has no topologically stable monopoles [T]; flag 59 lists further histories (†). Inflation is the standard account, not an observed epoch (v2.3; flag 59)." This page's physics is the first of those histories. It applies only if a unification transition produced monopoles, inflation followed it and reheating stayed below it (flag 59; [ordering: which relics survive](#ordering-which-relics-survive)). #11's Appendix A records the split: "as explanation, dead (wrong duality, which only §11.4's shared-photon form contests, and that form needs P4 restated; the null result is expected under several standard histories, so it lends no support — v2.3, flag 59); as ontology, alive and consequence-bearing" (App. A item 5; [Obituary: conjugate monopoles explain the null result](/wiki/electric-magnetic-duality/monopole-explanation)). Whether the shared-photon form would reopen the explanation awaits Paul's ruling (flag 62 in `review/wiki-build-flags.md`, pending).

Until v2.3 the second ground was inflation alone: "inflationary dilution already accounts for absence [T]" (#11 v2.2 §11.1), and "wrong duality; inflation suffices" in #11 v2.2's Appendix A and in the [handoff](/wiki/history/documents/handoff)'s list of dead claims (`HANDOFF.md` §2). Flag 59 in `review/wiki-build-flags.md` found that this showed the explanation unnecessary, not false, and Paul accepted the restatement on 2026-10-29. The program still predicts a permanent null for monopoles of our sector, [row 8](/wiki/predictions/monopole-null).

### The soliton candidate's survival routes

The soliton candidate was retired after round 3 ([Obituary: superheavy conjugate solitons](/wiki/dark-matter/candidates/soliton-candidate/obituary)). Its manuscript had placed the monopole mass by the Kibble abundance "with no dilution required" (#14 abstract). Decision 2 of the round-3 adjudication explains why that mattered: "The row earned its place in the checkpoint's trilemma on two claims: topology makes it stable for free, and the mass came out of the abundance with no free dilution. Round 3 removed the second." The decision set out three routes ([round-3 decisions and lessons](/wiki/method/review/round-3/decisions)):

- **(a)** Claim the low-scale model: "Route (a), v ≲ 100 PeV, works", but the program does not claim it; the surviving version is noted as prior art, because it "is Murayama–Shu's and Liveoak–Maharana–Wells's model" and "claiming it would add no testable content and would misattribute it".
- **(b)** Keep a superheavy mass and name a dilution mechanism: rejected. "Route (b) restores the mass only by adding a free dilution factor of at least 10³–10⁴ (ruling 2), probably far more (ruling 3). The mass would then no longer be a prediction".
- **(c)** Retire the candidate: chosen.

With a dilution factor D left free, any mass above M\* fits the observed density by the choice of D, so the abundance no longer selects a mass. #11 §12: "Superheavy masses survive only with a free dilution factor. That removes the mass prediction, which was the candidate's reason to exist." The argument, and the superheavy alternative kept before round 3 that became route (b), are on [the relic yield Y = n/s and entropy dilution](/wiki/cosmology/early-universe/relic-yield-and-dilution#the-benchmark-overproduced-and-the-dilution-route-rejected).

### Reheating in polarization-genesis

[The lab notebook](/wiki/history/documents/lab-notebook)'s sketch of [polarization-genesis](/wiki/dark-matter/candidates/polarization-genesis), the open question of what sets the ratio of dark to ordinary matter, also places the decisive event at reheating: "at reheating, the heavy Grassmannian moduli (the nine non-Maslov directions) decay", and their branching into x- and p-polarized quanta is set by an angle of the vacuum's polarization (#1 §8, tagged "[O, sketched]"). As with a colder hidden sector, the relative amounts of the two kinds of matter would be fixed by how a decay at reheating divides its energy, a parallel the documents do not draw. The sketch is not a calculation, and the question is open (OP7).

### The radiation's entropy in the phase-space diameter relation

The [phase-space diameter relation](/wiki/cosmology/scale-factor-duality/phase-space-diameter), first stated in the early chat and written up in the phase-space-diameter note, multiplies the size of a region in position by the momentum spread of the radiation in it. For a fixed comoving region the product is constant, and it "counts the quantum cells the radiation occupies, which is about the number of photons" (`papers/phase-space-diameter.md` §3): "The relation's N is the radiation's photon count, or its entropy" (§3). The note dates that count from reheating: "before reheating at the end of inflation the region held no radiation. The area counts occupied cells; it was created at reheating and is not a constant of nature" (§3). From reheating on, the conserved quantity is the comoving entropy ([entropy and the yield](/wiki/cosmology/early-universe/radiation-era#entropy-and-the-yield-y--ns-t)) [T]. The program's constraint [a·ã = 1](/wiki/cosmology/scale-factor-duality/cosmological-constraint) fixes the area of one cell and not the number of cells, and in the note's words that number "is the radiation's entropy, set at reheating" (§3).

The note's §6 uses the reheating bound above to test the chat's claim that the radiation's rectangle in position and momentum was "square (D_x = D_p in Planck units) exactly at the bounce" (`HANDOFF.md` §4). Run back in time, the rectangle would be square only at about 4.4×10¹⁴ times the Planck temperature, before the radiation existed; at reheating, no hotter than about 5.7×10¹⁵ GeV, it was already long by a factor A = 2.9×10³⁵ [V], and "Since its creation the radiation rectangle has never been within 35 orders of magnitude of square" (§6). That is one of the grounds on which the claim is withdrawn ([Obituary: the square rectangle at the bounce](/wiki/cosmology/scale-factor-duality/square-at-the-bounce)).

## Standard references

- A. H. Guth, Phys. Rev. D 23, 347 (1981) †; A. D. Linde, Phys. Lett. B 108, 389 (1982) †; A. Albrecht, P. J. Steinhardt, Phys. Rev. Lett. 48, 1220 (1982) †: inflation and its slow-roll form.
- J. Preskill, Phys. Rev. Lett. 43, 1365 (1979): the monopole problem; #14's reference [19], checked at abstract level by the round-3 audit ([the monopole problem](/wiki/electric-magnetic-duality/monopoles/monopole-problem)).
- E. W. Kolb, M. S. Turner, *The Early Universe* (Addison-Wesley, 1990): #14's reference [17]; a standard treatment of inflation, reheating and entropy production.
- R. J. Scherrer, M. S. Turner, Phys. Rev. D 31, 681 (1985) †: entropy production by decaying particles.
- H. Murayama, J. Shu (2010), arXiv:0905.1720 [28S], and D. Liveoak, A. Maharana, J. D. Wells (2026), arXiv:2607.20843 [29S]: hidden-sector monopoles and the dilution they need, as #11 cites them.
- BICEP/Keck Collaboration, P. A. R. Ade et al., Phys. Rev. Lett. 127, 151301 (2021), arXiv:2110.00483 [S], and A. K. Soman, S. S. Mishra, M. Shafi, S. Basak, Phys. Rev. D 112, 103521 (2025), arXiv:2407.07956 [S]: the limit of a tensor-to-scalar ratio below 0.036 and the energy scale of inflation it allows, E_inf < 1.39×10¹⁶ GeV, as the phase-space-diameter note cites them.

The † entries are from model memory and unverified.

## Used by

- [Obituary: superheavy conjugate solitons](/wiki/dark-matter/candidates/soliton-candidate/obituary) — the free-dilution route, rejected.
- [Overproduction at the benchmark](/wiki/dark-matter/candidates/soliton-candidate/overproduction) — the dilution a mass above M\* would need.
- [Topological dark matter in the literature](/wiki/dark-matter/candidates/soliton-candidate/prior-art) — early matter domination as the escape above about 100 PeV.
- [The hidden sector's thermal history](/wiki/dark-matter/candidates/soliton-candidate/hidden-thermal-history) — a colder reheated hidden sector and the reheating it needs.
- [Obituary: conjugate monopoles explain the null result](/wiki/electric-magnetic-duality/monopole-explanation) — inflation as one of the standard histories under which the null result is expected (in v2.2, "inflationary dilution already accounts for absence").
- [Row 8: no monopoles of our sector](/wiki/predictions/monopole-null) — the permanent null for our sector, whose absence #11 §11.1 expects under several standard histories, inflation among them.
- [Open: polarization-genesis and the 5.4 : 1 ratio (OP7)](/wiki/dark-matter/candidates/polarization-genesis) — the lab notebook's sketch sets its decisive event at reheating.
- [The monopole problem](/wiki/electric-magnetic-duality/monopoles/monopole-problem) — inflation as the standard resolution.
- [Round-3 decisions and lessons](/wiki/method/review/round-3/decisions) — Decision 2 and its three routes.
- [The phase-space diameter relation](/wiki/cosmology/scale-factor-duality/phase-space-diameter) — the radiation's entropy, the relation's N, set at reheating.
- [Obituary: the square rectangle at the bounce](/wiki/cosmology/scale-factor-duality/square-at-the-bounce) — the reheating bound: elongated by at least 10³⁵ since reheating.

## Sources

- `papers/broken-born-checkpoint-v2.md` §11.1 — the dead monopole explanation, and the standard histories under which the null result is expected, inflation among them [T] (v2.3); App. A item 5 — the split fate of the supposition
- `papers/broken-born-checkpoint-v2.md` §12 — early matter domination [29S] and the free dilution factor in the soliton obituary; §13 row 8 — the permanent null for our monopoles; §14 item 7 — polarization-genesis open (OP7)
- `papers/phase-space-diameter.md` §3 — the radiation's entropy set at reheating, and a·ã = 1 as the area of one cell; §6 — the reheating bound [S] and the rectangle's aspect ratio at reheating [V]; 'References' — BICEP/Keck 2021 and Soman et al. 2025
- `verify/phase_space_diameter.py` 'Where the radiation rectangle is square, lambda = l_P (note §6)' — T_rh < 5.7×10¹⁵ GeV and A = 2.9×10³⁵
- `review/round3-adjudication.md` 'Decisions' 1, 2 — strict sector separation; the three routes and the rejected dilution route; 'Rulings' 2, 3 — the overproduction and the literature; the omitted-constraints list
- `review/round3/referee/audit-notes.md` Step 4(a) item 5 — re-thermalization by ψ; Step 4(c) items 1, 7, 9 — the literature, the Higgs portal, the reheating requirement and isocurvature
- `review/round3/referee/step4c.out` — the referee's printed reheating values
- `notes/knot-dark-matter-standalone.md` §3, §4, §6 — the withdrawn candidate's ordering requirement, its colder hidden sector and the dilution scaling (withdrawn)
- `notes/broken-born-theory.md` §8 — polarization-genesis at reheating [O, sketched]
- `HANDOFF.md` §2 — "wrong duality; inflation suffices"; §4 — the chat claim of a rectangle "square … exactly at the bounce"
- `review/wiki-build-flags.md` item 59 — the restated ground, and the conditions under which inflation accounts for the absence; item 62 — whether the shared-photon form reopens the explanation, pending
