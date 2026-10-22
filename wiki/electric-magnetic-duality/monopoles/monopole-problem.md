---
title: "The monopole problem"
weight: 40
status: established
description: "Superheavy monopoles from the early universe would be unacceptably abundant (Preskill); annihilation cannot lower n/T³ below about 10⁻¹⁰ at 10¹⁶ GeV, and inflation dilutes them — why our sector's null result needs no new explanation, and the hidden-sector version that bounds topological dark matter."
provenance: [T]
sources:
  - "papers/broken-born-checkpoint-v2.md §11.1"
  - "papers/broken-born-checkpoint-v2.md §12"
  - "papers/broken-born-checkpoint-v2.md refs [28]–[29]"
  - "notes/knot-dark-matter-standalone.md §3"
  - "notes/knot-dark-matter-standalone.md §5"
  - "notes/knot-dark-matter-standalone.md §6"
  - "notes/knot-dark-matter-standalone.md ref [19]"
  - "review/v3-worklog.md 'Findings neither referee raised'"
  - "review/round3-adjudication.md 'Rulings' 10"
  - "review/round3-adjudication.md 'Decisions' 2"
  - "review/round3-adjudication.md 'Decisions' 3"
  - "review/round3/referee/audit-notes.md Step 1"
  - "review/round3/referee/audit-notes.md Step 4(a)"
  - "review/round3/referee/audit-notes.md Step 4(c)"
  - "HANDOFF.md §2"
  - "HANDOFF.md §6"
---

*The monopole problem, in the form the program cites (John Preskill, 1979), is the finding that the hot early universe should have produced superheavy [magnetic monopoles](/wiki/electric-magnetic-duality/monopoles) in unacceptably large numbers, while none has ever been detected. Every grand unified theory contains such monopoles, the cooling universe makes at least about one per horizon volume when the unified symmetry breaks, and monopoles and antimonopoles annihilate one another too slowly to remove enough of them. The standard resolution is [inflation](/wiki/cosmology/early-universe/inflation-and-dilution), a period of rapid expansion after the monopoles form that dilutes them to an unobservable density. The program meets the problem twice: inflation is one of the two reasons its founding claim that [conjugate monopoles explain the null result](/wiki/electric-magnetic-duality/monopole-explanation) is dead, and [round 3](/wiki/method/review/round-3) ruled that the strong-coupling annihilation question of its [retired soliton candidate](/wiki/dark-matter/candidates/soliton-candidate/obituary) is Preskill's calculation, already done for hidden sectors.*

**Status:** Established — [T] — literature. Preskill 1979 is reference [19] of the withdrawn [#14](/wiki/dark-matter/candidates/soliton-candidate), cited without a tag; the worklog reports its key figure as "verified from the scan", and [the round-3 audit](/wiki/method/review/round-3/rulings) checked the abstract. The [checkpoint](/wiki/history/documents/checkpoint) uses inflationary dilution as established physics [T] (#11 §11.1), and its hidden-sector bound is live-searched literature [29S]. The explanations below are standard physics written from general knowledge [T]; references added from memory are marked †.

## Too many monopoles [T]

A grand unified theory embeds the strong, weak and electromagnetic forces in one simple gauge group, broken at a very high scale v to the Standard Model's groups. The breaking leaves the U(1) of electromagnetism unbroken inside a simply connected group, so the theory has ['t Hooft–Polyakov monopoles](/wiki/electric-magnetic-duality/monopoles/thooft-polyakov-monopole), with mass of order the heavy vector bosons' mass divided by the unified fine-structure constant: superheavy.

When the universe cooled through the unification transition at T_c ~ v, [the Kibble mechanism](/wiki/electric-magnetic-duality/monopoles/kibble-mechanism) produced at least about one monopole per horizon volume, a yield n/s ≳ p (T_c/M_Pl)³ with p of order 100. The yield stays fixed as the universe expands, so the present mass density of the monopoles is their mass times the yield times today's entropy density s₀:

```text
ρ_M = M · (n/s) · s₀,       n/s ≳ p (T_c/M_Pl)³,       T_c ~ v,   M ∝ v
```

The density grows as the fourth power of the scale: M and T_c are each proportional to v, and the yield carries T_c³. #14 §3 states the scaling for its own monopoles: "Heavier monopoles are over-produced as (M/M\*)^4", where M\* is the mass at which the monopoles would make up exactly the observed [dark matter](/wiki/dark-matter) ([overproduction at the benchmark](/wiki/dark-matter/candidates/soliton-candidate/overproduction)). At grand-unified scales the predicted density exceeds the critical density, the total density of a spatially flat universe, by many orders of magnitude. Preskill's abstract, as the round-3 audit quotes it: the "density of such monopoles in the early universe is estimated to be unacceptably large" (`review/round3/referee/audit-notes.md`, Step 1). Zel'dovich and Khlopov (1978†) reached the same conclusion independently.

## Annihilation is not enough [T]

A monopole can annihilate with an antimonopole, so the question is whether annihilation in the early universe removes the excess. It does so only slowly. A monopole and an antimonopole must first bind: in the hot plasma the pair loses energy by scattering on the charged particles around it (diffusive capture) and by radiation, and the bound pair then spirals in and annihilates. The rate per monopole is proportional to the monopole density, which expansion dilutes, so annihilation stops once the density has fallen to a level set by the capture rate and the expansion rate [T]. Annihilation therefore lowers a high initial abundance toward a fixed level and cannot go below it; an initial abundance already below that level is left as it was.

Preskill's calculation put that level far too high to help. The v3 worklog's reading of the paper: "Preskill (verified from the scan): annihilation cannot reduce n/T³ below ~10⁻¹⁰ at m ≈ 10¹⁶ GeV" (`review/v3-worklog.md`, finding F1), where n/T³ is the monopole density in units of the cube of the temperature. #14 §3 summarizes: "The classic relic analysis [19] found monopole-antimonopole annihilation inefficient for superheavy monopoles in our plasma."

**Strong coupling is the ordinary case.** Monopoles of the minimal Dirac charge interact strongly with one another, because [Dirac quantization](/wiki/electric-magnetic-duality/monopoles/dirac-quantization) makes the magnetic coupling the inverse of a weak electric one. Two effects of a strong attractive force enhance annihilation at low relative speed [T]: the attraction focuses the pair's wavefunction toward short distances (Sommerfeld enhancement), and the pair binds readily, radiating its binding energy (bound-state formation). Preskill's monopoles were Dirac monopoles, so his analysis already concerned this regime. The round-3 referee made the point against #14: "the "strong-coupling" regime alpha_m = 34 is exactly the Dirac-monopole case of Preskill 1979 (h = 2 pi/e)" (Step 4(a) item 3), with h the magnetic charge in the notation of the analysis it followed.

## Inflation as the remedy [T]

Inflation, a period of accelerated expansion in the very early universe, removes the problem if it happens after the monopoles form. The monopole number density falls as the cube of the expansion factor, so a sufficiently long inflation leaves of order one monopole or none in the observable universe. After inflation the universe reheats, and the monopoles stay diluted only if the reheating temperature is too low to make them again, below the transition temperature T_c. The monopole problem was one of the motivations for inflation (Guth, 1981†). See [inflation, reheating and entropy dilution](/wiki/cosmology/early-universe/inflation-and-dilution).

With inflation the expected monopole flux today is negligible, consistent with searches that have found none ([the monopole flux bounds](/wiki/electric-magnetic-duality/monopoles/monopole-searches)). #11 §11.1 states it for our sector: "inflationary dilution already accounts for absence [T]".

The same condition, read the other way, is a requirement on any scenario in which monopoles survive as a relic: the transition must come after inflation, below the reheating temperature, or the monopoles are diluted away. #14 §3 required exactly that for its hidden sector: "Inflation must precede the hidden transition, and v must lie below the reheating temperature."

## Hidden sectors [T]

A hidden gauge sector with its own symmetry breaking and its own plasma has the same problem, and the same literature applies. Two works the checkpoint cites, both live-searched:

- **Murayama and Shu** [28S] proposed hidden-sector monopoles as dark matter; the audit quotes their abstract: "Kibble mechanism drastically underestimates the production of topological defects ... dark matter of mass 1-10 PeV" (Step 4(c) item 1).
- **Liveoak–Maharana–Wells** (LMW) [29S] bound the scale: "for symmetry-breaking scales >~ 100 PeV, the monopole abundance is unacceptably high" (Step 4(c) item 1). Ruling 3 summarizes their abstract, without quotation marks, as "hidden monopoles overclose for breaking scales ≳ 100 PeV unless diluted, e.g. by early matter domination".

#11 §12 states the result in its own words: "Hidden-sector monopoles avoid overclosing the universe only for symmetry-breaking scales ≲ 100 PeV, or with a period of early matter domination [29S]", and "Below that scale, annihilation in the hidden plasma sets the abundance. That is the established topological-dark-matter scenario [28S, 29S], and nothing in it depends on Born reciprocity." See [topological dark matter in the literature](/wiki/dark-matter/candidates/soliton-candidate/prior-art).

## How the program uses it

### The absence of our sector's monopoles

The program began with the supposition that monopoles live in conjugate space, which would explain why none of ours are seen ([founding suppositions and their fates](/wiki/program/founding-suppositions)). #11 §11.1 killed that explanation on two grounds: "As an explanation of the null result: dead — the relevant duality is electric–magnetic (E↔B, g → 1/g), not x↔p, and inflationary dilution already accounts for absence [T]." The second ground is this page's physics: since inflation already removes our sector's monopoles, their absence needs no further explanation ([Obituary: conjugate monopoles explain the null result](/wiki/electric-magnetic-duality/monopole-explanation)). The program still predicts a permanent null for monopoles of our sector ([row 8](/wiki/predictions/monopole-null)).

### The soliton candidate's relic question

The retired soliton candidate was a population of hidden-sector monopoles, and the monopole problem followed it through every version ([Obituary: superheavy conjugate solitons](/wiki/dark-matter/candidates/soliton-candidate/obituary)):

- **Round 1.** The referee found that #14 v1 had cited Preskill backwards: "Preskill citation inverted (fixed)" (`HANDOFF.md` §6; [review rounds 1 and 2](/wiki/method/review/rounds-one-and-two)).
- **The open question.** The [handoff](/wiki/history/documents/handoff) listed as open item 2 the "Strong-coupling relic freeze-out at α_d ~ 34: Sommerfeld-enhanced annihilation vs. the √N topological-charge floor" (`HANDOFF.md` §2). The v3 worklog agreed that the hidden-sector rate "has to be recomputed (acceptance criterion 3), not carried over" (finding F1). #14 §3 left it open: annihilation "runs through the hidden plasma (psi and hidden photons) at alpha_m ~ 34, where Sommerfeld enhancement and rapid bound-state formation may matter", and its acceptance criterion 3 asked for "the strong-coupling relic freeze-out calculation of Sec. 3, in the hidden plasma" (§6); exclusion condition 4 was a relic calculation showing that annihilation "cannot leave the observed abundance" (§5). Here α_m ≈ 34 is the monopoles' magnetic coupling under #14's hypothesis H, a figure that depends on convention by a factor of 4 ([Obituary: the coupling α_d ≈ 34](/wiki/dark-matter/candidates/soliton-candidate/alpha-d-coupling)).
- **Round 3.** The referee closed it: "Acceptance criterion 3 is not open: the "strong-coupling" regime alpha_m = 34 is exactly the Dirac-monopole case of Preskill 1979 (h = 2 pi/e); its modern hidden-sector version (LMW 2026) excludes v >~ 100 PeV for hidden monopoles" (Step 4(a) item 3; LMW is Liveoak–Maharana–Wells). At the corrected Kibble minimum, the referee found the initial yield, "7e-20 - 1.4e-18", far below the level at which annihilation acts, "so annihilation is irrelevant in that case and overproduction 4.9e3 - 9.8e4 (xi=0.76..0.5) stands". Ruling 10, upheld at the level of the abstracts: "Annihilation at α_m ≈ 34 is Preskill's Dirac case, already done for hidden sectors", with "LMW 2026 as in #3" as evidence.
- **The √N floor.** The chat-only idea that a net topological charge would survive annihilation was dropped by Decision 3, because "Its premise, Kibble as a ceiling, is inverted (ruling 3)" and "Under decision 2 it has no candidate left to serve" ([Obituary: the √N topological floor (chat-only)](/wiki/dark-matter/candidates/soliton-candidate/sqrt-n-floor)).
- **Dilution as a survival route.** Inflation-style dilution could have saved a superheavy mass, but only as a free parameter. Decision 2 rejected that route: "Route (b) restores the mass only by adding a free dilution factor of at least 10³–10⁴ (ruling 2), probably far more (ruling 3). The mass would then no longer be a prediction" ([round-3 decisions](/wiki/method/review/round-3/decisions); [inflation, reheating and entropy dilution](/wiki/cosmology/early-universe/inflation-and-dilution)).

The production side of the problem is [the Kibble mechanism](/wiki/electric-magnetic-duality/monopoles/kibble-mechanism), and its observational side is [the monopole flux bounds](/wiki/electric-magnetic-duality/monopoles/monopole-searches).

## References

- J. Preskill, Phys. Rev. Lett. 43, 1365 (1979) — #14 [19], without a tag; read from a scan for the v3 worklog, and its abstract checked by the round-3 audit.
- H. Murayama, J. Shu, "Topological dark matter," Phys. Lett. B 686, 162 (2010), arXiv:0905.1720 — #11 [28S].
- D. Liveoak, A. Maharana, J. D. Wells, "Dark monopoles, bounds on hidden sectors, and cosmological implications," arXiv:2607.20843 (2026) — #11 [29S].
- E. W. Kolb, M. S. Turner, *The Early Universe* (Addison-Wesley, 1990) — #14 [17], cited there for freeze-out; a standard textbook account of the monopole problem.

Added by the wiki from model memory (†):

- Ya. B. Zel'dovich, M. Yu. Khlopov (1978)†: the overabundance of grand-unified monopoles.
- A. H. Guth (1981)†: inflation, proposed in part to solve the monopole problem.

## Used by

- [Obituary: conjugate monopoles explain the null result](/wiki/electric-magnetic-duality/monopole-explanation) — inflation already accounts for the absence of monopoles.
- [Row 8: no monopoles of our sector](/wiki/predictions/monopole-null) — the permanent null for our sector's monopoles, whose absence #11 §11.1 attributes to inflationary dilution.
- [Topological dark matter in the literature](/wiki/dark-matter/candidates/soliton-candidate/prior-art) — the hidden-sector version, where annihilation sets the abundance below about 100 PeV.
- [Obituary: the √N topological floor (chat-only)](/wiki/dark-matter/candidates/soliton-candidate/sqrt-n-floor) — the strong-coupling annihilation question that ruling 10 closed.
- [Inflation, reheating and entropy dilution](/wiki/cosmology/early-universe/inflation-and-dilution) — the remedy, and the dilution route the program rejected.
- [Overproduction at the benchmark](/wiki/dark-matter/candidates/soliton-candidate/overproduction) — Preskill's annihilation floor at the old benchmark.
- [Obituary: superheavy conjugate solitons](/wiki/dark-matter/candidates/soliton-candidate/obituary) — ruling 10: annihilation at α_m ≈ 34 is Preskill's Dirac case.

## Sources

- `papers/broken-born-checkpoint-v2.md` §11.1, §12, refs [28]–[29] — inflationary dilution [T]; the hidden-sector bound and the established scenario [28S, 29S].
- `review/v3-worklog.md` 'Findings neither referee raised' (F1) — the n/T³ floor from Preskill, and the hidden-sector rate to be recomputed.
- `review/round3-adjudication.md` 'Rulings' 10, 'Decisions' 2 and 3 — strong-coupling annihilation is Preskill's Dirac case; the rejected dilution route; the dropped √N floor.
- `review/round3/referee/audit-notes.md` Step 1, Step 4(a), Step 4(c) — the abstract check; the Dirac-monopole identification and the Kibble-minimum yield; Murayama–Shu and Liveoak–Maharana–Wells.
- `notes/knot-dark-matter-standalone.md` §3, §5, §6, ref [19] — the relic analysis as #14 used it, the scaling (M/M\*)⁴, acceptance criterion 3 and exclusion condition 4 (withdrawn manuscript).
- `HANDOFF.md` §2, §6 — open item 2 as it stood at the handoff; the round-1 citation fix.
