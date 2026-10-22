---
title: "Round-3 verdict, rulings and citation audit"
weight: 20
status: record
description: "Grade C with medium confidence and the adjudicator's agreement; rulings 1–13 with their evidence; the compatibility theorem verified and re-attributed; the omitted constraints accepted as a to-do; all 23 references resolving."
sources:
  - "review/round3-adjudication.md 'Verdict'"
  - "review/round3-adjudication.md 'Rulings'"
  - "review/round3-adjudication.md 'What survives v3'"
  - "review/round3/referee/audit-notes.md Step 1"
  - "review/round3/referee/audit-notes.md Step 2"
  - "review/round3/referee/audit-notes.md Step 3"
  - "review/round3/referee/audit-notes.md Step 4(a)"
  - "review/round3/referee/audit-notes.md Step 4(b)"
  - "review/round3/referee/audit-notes.md Step 4(c)"
  - "review/round3/referee/audit-notes.md Step 4(d)"
  - "review/round3/referee/audit-notes.md Step 5"
  - "review/round3/referee/step4.out"
  - "review/round3/referee/step4b.out"
  - "review/round3/referee/step4c.out"
  - "review/round3/referee/cite_fetch.py"
  - "review/round3/referee/pdfgrep.py"
  - "review/v3-worklog.md 'Verified references for v3'"
  - "review/v3-worklog.md 'v3 as drafted (2026-10-19)'"
  - "notes/knot-dark-matter-standalone.md §1–§6"
  - "notes/knot-dark-matter-standalone.md 'References'"
  - "papers/broken-born-checkpoint-v2.md §5"
  - "papers/broken-born-checkpoint-v2.md §10"
  - "papers/broken-born-checkpoint-v2.md §12"
  - "papers/broken-born-checkpoint-v2.md 'References'"
  - "verify/soliton_obituary.py"
  - "review/skeptic-review-console.html SYSTEM"
  - "review/wiki-build-flags.md items 21, 22 and 33"
---

*The round-3 verdict and rulings are the outcome of the third blind review of #14, the manuscript proposing that dark matter consists of [superheavy magnetic monopoles of a hidden gauge sector](/wiki/dark-matter/candidates/soliton-candidate/obituary): the referee's grade and findings, and the adjudicator's ruling on each finding. The referee graded version 3 C, fundamentally flawed, with medium confidence. The predicted monopole mass rested on a count of monopoles formed in the early universe that was normalized too low, by a factor of about 4.6×10³, and every number derived from that mass carried the error. The adjudicator agreed for v3 as written. Of the thirteen numbered findings it upheld most, accepted others, some without re-checking them, and overturned one, the claim that a cited paper lacked the operator it was cited for. The audit also found every one of #14's 23 references real, identified the manuscript's one theorem as a known result of Born geometry, and listed constraints the manuscript had not evaluated, which the adjudication accepted as a to-do.*

**Status:** Record — untagged; #11 §12 tags the corrected numbers [V]. The verdict, the table of rulings, the list of omitted constraints and the survivors are in `review/round3-adjudication.md`; the referee's evidence is `review/round3/referee/audit-notes.md`, with its scripts and printed outputs beside it. The numbers of rulings 1, 2, 4 and 5 are gated in `verify/soliton_obituary.py` ([the soliton-obituary script](/wiki/method/verification/soliton-obituary-script)), apart from the referee's figures that ruling 4 quotes (flag 33 in `review/wiki-build-flags.md`); the other rulings, the omitted constraints and the citation audit are not gated. A figure quoted in ruling 3 is the subject of flag 21 in `review/wiki-build-flags.md`.

## The audit

[Review round 3](/wiki/method/review/round-3) sent #14 v3, the standalone manuscript of [the soliton candidate](/wiki/dark-matter/candidates/soliton-candidate), to "a blind subagent with Python and web access". The subagent received only the manuscript and [the five-step protocol](/wiki/method/review/review-protocol): check every citation, re-check every number from independently chosen constants, re-derive the [compatibility theorem](/wiki/phase-space/born-geometry/compatibility-theorem), audit the argument and its omitted constraints, and grade the whole ([the round-3 pre-registration](/wiki/method/review/round-3/preregistration)). It kept notes organized by those steps, `review/round3/referee/audit-notes.md`, and the scripts and printed outputs of its calculations. `cite_fetch.py` queried INSPIRE, the literature database of high-energy physics, for each reference; `pdfgrep.py` searched the papers' full texts for the claims they were cited for; the `step2` scripts recomputed #14's numbers, the `step3` scripts re-derived the theorem, and the `step4` scripts supported the conceptual audit. The adjudication counts the result: "Every one of its 16 numerical findings rests on executed code."

The referee's table of #14's numbers, its own values and its verdicts, with the constants it chose, is summarized on [the arbitration page](/wiki/method/review/round-3/arbitration#the-referees-numbers-check). Most of #14's arithmetic was confirmed; the discrepancies became rulings 1, 2, 4 and 5, and the referee's estimate of ε ruling 7.

## The verdict

The referee's grade line (Step 5):

```text
GRADE: C (fundamentally flawed), confidence MEDIUM (high confidence in each individual finding; medium on the B/C boundary).
```

Its reason: the headline result, a monopole mass of "M ~ 1e13-4e13 GeV" with "no dilution required", "is wrong on two independent counts":

- [the Kibble normalization](/wiki/dark-matter/candidates/soliton-candidate/kibble-normalization) ("Kibble normalisation, step2a.out"), and
- the "neglect of Kibble-Zurek / bubble overproduction with hidden-plasma annihilation", with the evidence in `step4.out` and in the papers of Liveoak–Maharana–Wells (LMW) and of Murayama and Shu.

Every downstream number, from the breaking scale v and the [W′](/wiki/dark-matter/candidates/soliton-candidate/w-prime-overclosure) mass to [the ψ window](/wiki/dark-matter/candidates/soliton-candidate/psi-relic-window), [the gravitational-wave band](/wiki/dark-matter/candidates/soliton-candidate/hidden-thermal-history#the-gravitational-wave-band-died-with-the-candidate) and ε, "hangs on it, and the "selected by phase-space duality" claim does no work." The referee's single weakest link was "the Kibble abundance / mass determination (p=0.023 instead of >= 25-104; Kibble treated as an upper end when it is the causal minimum; KZ production and alpha_m=34 Preskill-type annihilation not computed although the literature already has it)", where KZ is Kibble–Zurek. Second came "the framework does no work" ([the 'framework does no work' critique](/wiki/program/framework-does-no-work)). Its salvage: "Salvage = a different model (v <~ 1e8 GeV, or explicit dilution), which already exists in the literature."

The adjudication opens with its agreement: "**Referee: C (fundamentally flawed), medium confidence. I agree for v3 as written.**" It adds two points:

- "The headline result ("1e13–4e13 GeV, no dilution required") rests on a wrong Kibble normalization."
- "Correcting it leaves two routes: a superheavy monopole that needs a named dilution mechanism, or a model at v ≲ 100 PeV that already exists in the literature."

Those two routes, and a third, retirement, became Decision 2 ([round-3 decisions and lessons](/wiki/method/review/round-3/decisions)). On the program's scale a C is the lowest grade; the console's prompt glosses it as "confabulation" and the referee as "fundamentally flawed" ([the verdict scale](/wiki/method/review/review-protocol#the-verdict-scale)). The referee's medium confidence was about where the line between B and C falls, not about any single finding.

## The rulings

The adjudication answers the referee in a table, one row per finding, each with a ruling and the adjudicator's evidence. "Upheld" carries the qualifiers "(minor)", "(abstract level)" and "in substance"; "Accepted, not re-checked" marks a finding that rests on the referee's evidence alone; "Overturned" marks one the adjudicator found wrong ([adjudication](/wiki/method/review/review-protocol#after-the-referee-adjudication)). The physics of each finding is on the page named in the last column.

| # | Finding (the adjudication's wording, shortened) | Ruling | Where the physics is |
| --- | --- | --- | --- |
| 1 | one defect per Hubble volume is p ≈ 104, not 0.023 | Upheld | [the Kibble normalization](/wiki/dark-matter/candidates/soliton-candidate/kibble-normalization) |
| 2 | the M\* band and "no dilution" fail | Upheld | [overproduction at the benchmark](/wiki/dark-matter/candidates/soliton-candidate/overproduction) |
| 3 | Kibble is a floor, not a ceiling | Upheld | [the Kibble mechanism](/wiki/electric-magnetic-duality/monopoles/kibble-mechanism) |
| 4 | the ψ relic window is too high | Upheld | [the ψ relic window](/wiki/dark-matter/candidates/soliton-candidate/psi-relic-window) |
| 5 | the ξ bound is 0.760, not 0.77 | Upheld (minor) | [the hidden sector's thermal history](/wiki/dark-matter/candidates/soliton-candidate/hidden-thermal-history) |
| 6 | MeV-scale ψ freezes out during nucleosynthesis | Accepted, not re-checked | [the ψ relic window](/wiki/dark-matter/candidates/soliton-candidate/psi-relic-window#the-lower-edge-freeze-out-during-nucleosynthesis) |
| 7 | the dimension-5 operator's "O(1) coefficient at the Planck scale" is unsupported | Upheld | [Planck-suppressed adjoint mixing](/wiki/dark-matter/candidates/soliton-candidate/dimension-five-operator) |
| 8 | Baumgart et al. lack the adjoint operator | Overturned | [Planck-suppressed adjoint mixing](/wiki/dark-matter/candidates/soliton-candidate/dimension-five-operator#ruling-8-the-operator-itself-exists) |
| 9 | the monopoles carry a visible electric charge (Witten effect) | Accepted, not re-checked | [kinetic mixing between sectors](/wiki/dark-matter/candidates/soliton-candidate/kinetic-mixing#ii-the-witten-effect) |
| 10 | annihilation at α_m ≈ 34 is Preskill's Dirac case | Upheld (abstract level) | [topological dark matter in the literature](/wiki/dark-matter/candidates/soliton-candidate/prior-art#strong-coupling-annihilation-is-a-solved-case) |
| 11 | the dark-energy data's best fit crosses into phantom above z ≈ 0.4 | Accepted | [the DR2 phantom crossing](/wiki/cosmology/dark-energy/desi-dr2-phantom-crossing) |
| 12 | minor citation issues | Accepted | [the citation audit](#the-citation-audit) below |
| 13 | v3 §6's "all numbers computed by executed code" overstates | Upheld in substance | [verification checks arithmetic, not the model](/wiki/method/verification/arithmetic-not-model) |

### Rulings 1 to 3: how many monopoles form

The manuscript counted monopoles by their yield, the number per unit entropy, n/s = p (T_c/M_Pl)³, where T_c is the temperature of the hidden symmetry-breaking transition and M_Pl the Planck mass. [The Kibble mechanism](/wiki/electric-magnetic-duality/monopoles/kibble-mechanism) fixes the least the transition can produce, about one monopole per Hubble volume, because the field cannot align its vacuum over regions that have never been in causal contact [T]. The first three rulings concern the size of p and its direction.

**Ruling 1, upheld.** The finding: "Kibble normalization: one defect per Hubble volume is p ≈ 104, not 0.023". The evidence: "My code: p = 104.31 with M_Pl, 0.828 with the reduced M_Pl. v3's 0.0228 drops (1.66√g\*)³ ≈ 4.6×10³. My error came from misremembering the formula." The code is the arbitration script ([round-3 arbitration](/wiki/method/review/round-3/arbitration)), and the last sentence is the author's, since the adjudicator had written v3 and its scripts. 1.66√g\* is the prefactor of the radiation-era expansion rate, H = 1.66 √g\* T²/M_Pl, with g\* the number of relativistic degrees of freedom [T] ([the dropped factor](/wiki/dark-matter/candidates/soliton-candidate/kibble-normalization#the-dropped-factor)).

**Ruling 2, upheld.** The finding: "The M\* band and "no dilution" fail". M\* is the mass at which the monopoles' relic density equals the observed dark-matter density. The evidence: "At minimum production M\* = 2.9–4.4×10¹² GeV. The 3×10¹³ benchmark is overproduced 2.1×10³–1.2×10⁴ times. The "reduced-Planck factor of 3" was not a convention spread: consistently normalized, the two conventions agree." v3 had read a factor of about 3 between the two normalizations of the Planck mass as a spread in its prediction; with p normalized in the same convention as M_Pl it disappears ([overproduction at the benchmark](/wiki/dark-matter/candidates/soliton-candidate/overproduction); [the reduced-Planck artefact](/wiki/dark-matter/candidates/soliton-candidate/kibble-normalization#the-reduced-planck-factor-of-3-was-an-artefact)).

**Ruling 3, upheld.** The finding: "Kibble is a floor, not a ceiling; Kibble–Zurek or bubble counting add more". The evidence:

> Murayama–Shu, arXiv:0905.1720, abstract: Kibble "drastically underestimates the production of topological defects". Liveoak–Maharana–Wells, arXiv:2607.20843 (July 2026), abstract: hidden monopoles overclose for breaking scales ≳ 100 PeV unless diluted, e.g. by early matter domination. I did not re-run the referee's Kibble–Zurek integration (1e9–1e12 overproduction).

The referee's own estimates (Step 4(a)): at a first-order transition, where defects form as bubbles of the new phase meet, "bubble counting gives p ~ 104 (beta/H)^3 = 1e2-1e8 (step4.out)", with β/H the rate of the transition relative to the expansion rate (item 2); Kibble–Zurek production at a continuous transition, followed by capture of monopole pairs in the hidden plasma, leaves "Omega/Omega_DM = 1.1e12 - 2.2e12 (step4.out). LMW analytic eq. (25) at these parameters: 1.2e9 - 2.2e11. Either way the annihilation does not rescue it" (item 3). The ruling's "1e9–1e12" spans both: flag 21 in `review/wiki-build-flags.md` notes that the integration itself gave 1.1e12–2.2e12 and that the 1e9 lower end is the analytic estimate's. Both figures mean overproduction, so the verdict is unaffected; the wiki quotes the ruling as written ([A floor, not a ceiling](/wiki/electric-magnetic-duality/monopoles/kibble-mechanism#a-floor-not-a-ceiling-t); [topological dark matter in the literature](/wiki/dark-matter/candidates/soliton-candidate/prior-art)).

### Ruling 4: the ψ relic window

ψ is the light hidden fermion v3 added so that the heavy W′± could decay; it is itself a stable relic, and v3 chose its mass window to keep it a minor part of the dark matter ([Obituary: the ψ relic window](/wiki/dark-matter/candidates/soliton-candidate/psi-relic-window)). The finding: "ψ relic window too high". Upheld, with the evidence:

> v3 omitted ψ̄ and the second doublet member (a factor of 4), and bracketed an exactly known s-wave σv up to ×10. My recount: 10% of the DM at 45–49 GeV, 100% at 146–158 GeV. The referee's Boltzmann integration gives 28–46 / 96–153 GeV. We agree to within ×1.6, and v3's 0.1–0.3 TeV was wrong.

DM is dark matter. The recount is in the arbitration run, and the two calculations are compared on [the arbitration page](/wiki/method/review/round-3/arbitration#where-referee-and-adjudicator-differ).

### Rulings 5 and 6: the colder hidden sector and nucleosynthesis

The hidden photon is massless, so the hidden sector adds radiation, which measurements of the cosmic microwave background (CMB) limit through N_eff, the effective number of neutrino species ([the radiation era](/wiki/cosmology/early-universe/radiation-era)). v3 therefore required the hidden sector to be colder than ours by a temperature ratio ξ ([the hidden sector's thermal history](/wiki/dark-matter/candidates/soliton-candidate/hidden-thermal-history)).

**Ruling 5, upheld (minor).** The finding: "ξ bound 0.760, not 0.77". The evidence: "Using N_eff,SM = 3.044, the 95% bound is ΔN_eff < 0.286." N_eff,SM is the Standard Model value. Its knock-on, which the adjudication writes with an abbreviation: the upper end of the gravitational-wave band becomes 3.2×10⁷ Hz ([gravitational waves from phase transitions](/wiki/cosmology/early-universe/phase-transition-gravitational-waves)). The referee had given the spread over conventions: "0.760 (N_SM=3.044), 0.759 (3.046); 0.769 only if DeltaN<0.30" (Step 2). v3's 0.77 came from a bound of 0.3 that the v3 worklog had taken "from memory †" ([the corrected bound](/wiki/dark-matter/candidates/soliton-candidate/hidden-thermal-history#the-worklogs-table-and-the-corrected-bound)).

**Ruling 6, accepted, not re-checked.** The finding: "MeV-scale ψ freezes out during BBN", Big Bang nucleosynthesis. The evidence: "T_f ~ m/20, so the lower mass bound should be ≳ 20–30 MeV." In a colder hidden sector a particle freezes out while the visible plasma is still hotter; the referee found the hidden freeze-out of a 1, 3 or 10 MeV ψ at visible temperatures of "0.08 MeV", "0.24 MeV" and "0.71 MeV", "i.e. during BBN. Needs m_psi >~ 20-30 MeV. (Moot: excluded anyway, below.)" (Step 4(a) item 8). The exclusion it points to is, in the wiki's reading, the supernova and nucleosynthesis limits of Step 4(c) [below](#supernova-sn1987a-and-nucleosynthesis-limits).

### Rulings 7 and 8: the mixing operator

[Kinetic mixing](/wiki/dark-matter/candidates/soliton-candidate/kinetic-mixing) couples the hidden photon's field strength to our hypercharge's with a strength ε, and gives hidden particles small charges under our electromagnetism [T]. For its [hidden SU(2)](/wiki/dark-matter/candidates/soliton-candidate/hidden-sector), v3 used a dimension-5 operator, Φ^a F^a_μν B^μν/M_\*, which gives ε ~ v/M_\* once the hidden Higgs field Φ takes its vacuum value v, with an "O(1) coefficient at the Planck or reduced Planck scale" (#14 §2(b)).

**Ruling 7, upheld.** The finding: "'O(1) coefficient at the Planck scale' for the dimension-5 operator is unsupported; the literature generates it at one loop from bi-charged states, which sector separation forbids". The evidence: "Consistent with the round-2 literature report: Chen–Cline–Frey "induced at one loop by a heavy particle X which carries both…". Sec. 2(a) and 2(b) of v3 are in tension." Every source that derives the operator needs particles charged under both groups, which v3's sector separation excludes, and their one-loop factor "1.37e-03" lowers ε to "9.1e-11 - 8.1e-10" (`step2a.out`; [the coefficient had no source](/wiki/dark-matter/candidates/soliton-candidate/dimension-five-operator#the-coefficient-had-no-source)).

**Ruling 8, overturned.** The referee had marked the first paper of #14's reference [10] `DOES NOT SUPPORT`: Baumgart et al. use a renormalizable mixing with a hidden U(1) factor, and a text search found "No adjoint dim-5 operator" (Step 1). The finding: "Baumgart et al. does not contain the adjoint operator". The adjudicator checked the paper:

> arXiv:0901.0283v2, p. 5, footnote 5, verbatim: "It is actually possible to achieve mixing without an abelian factor through an S parameter type operator Tr[Φw_μν]B^μν, where Φ is some operator that transforms as an adjoint of the non-abelian group." The referee missed the footnote.

The two rulings divide the claim: the operator and the relation ε ~ v/M_\* are in the literature, and the size v3 gave the coefficient is not ([ruling 8](/wiki/dark-matter/candidates/soliton-candidate/dimension-five-operator#ruling-8-the-operator-itself-exists)).

### Ruling 9: the Witten effect

A θ term, proportional to the product of electric and magnetic fields, gives a magnetic monopole an electric charge proportional to θ (the Witten effect) [T]. The finding: "With mixing and a physical hidden θ, the monopoles carry visible electric charge ~ εθ/2π · e (Witten effect)". Accepted, not re-checked, with the evidence: "Brümmer–Jaeckel–Khoze eq. 3.19, per the referee. This contradicts v3's "constraints act on ψ, not the dark matter" whenever ε ≠ 0." The referee put the charge at "1.6e-8 e (chi=1e-7, theta=1) to 1.6e-7 e (chi=1e-6)", with χ standing for ε: "Phenomenologically tiny at M=3e13 GeV, but it makes exclusion condition 1 self-triggering in the eps != 0 branch" (Step 4(a) item 7). #14's first exclusion condition was any confirmed non-gravitational coupling of the dark matter to the Standard Model ([the Witten effect](/wiki/dark-matter/candidates/soliton-candidate/kinetic-mixing#ii-the-witten-effect)).

### Ruling 10: annihilation at strong coupling

#14's acceptance criterion 3 asked for "the strong-coupling relic freeze-out calculation of Sec. 3, in the hidden plasma", because the monopoles' mutual coupling α_m ≈ 34 is strong (§6). The finding: "Annihilation at α_m ≈ 34 is Preskill's Dirac case, already done for hidden sectors". Upheld (abstract level), with the evidence "LMW 2026 as in #3". The referee: "Acceptance criterion 3 is not open: the "strong-coupling" regime alpha_m = 34 is exactly the Dirac-monopole case of Preskill 1979 (h = 2 pi/e); its modern hidden-sector version (LMW 2026) excludes v >~ 100 PeV for hidden monopoles" (Step 4(a) item 3). A monopole with the minimal Dirac charge relative to a weak electric charge is strongly coupled [T], so Preskill's monopoles were already in this regime ([strong-coupling annihilation](/wiki/dark-matter/candidates/soliton-candidate/prior-art#strong-coupling-annihilation-is-a-solved-case); [the monopole problem](/wiki/electric-magnetic-duality/monopoles/monopole-problem)). The handoff had queued a strong-coupling estimate of its own, the "√N floor", which Decision 3 dropped ([Obituary: the √N topological floor](/wiki/dark-matter/candidates/soliton-candidate/sqrt-n-floor)).

### Ruling 11: the phantom crossing

#14 §4 ended with an aside on the parent framework, which "predicts thawing, never-phantom dark energy, currently consistent with hints of weakening dark energy in recent baryon-acoustic-oscillation data". The referee checked it against Data Release 2 (DR2) of the Dark Energy Spectroscopic Instrument (DESI), which reports that "the favored w(z) shows a phase of w > -1 at low redshifts and a phantom crossing to w < -1 above redshifts z ~ 0.4", and judged the aside "at best partially true; the DESI-preferred solution is phantom-crossing, which exclusion condition 6 says would kill the framework" (Step 4(c) item 11). The finding: "DESI DR2's best fit crosses into phantom (w < −1) above z ≈ 0.4". Accepted, with the evidence: "The parent framework's "never phantom" needs the checkpoint's own nuance: non-phantom fits remain compatible at ~2σ." #11 v2.1 added the "Under pressure" paragraph to §10 ([DESI DR2's phantom crossing](/wiki/cosmology/dark-energy/desi-dr2-phantom-crossing); [the no-phantom bound](/wiki/cosmology/dark-energy/no-phantom-bound)).

### Ruling 12: minor citation issues

The finding: "Minor citation issues: [4] over-generalized; Zwanziger's 4π vs 2π; Schwinger uncited". Accepted, without further evidence. All three come from Step 1 of the audit and are set out in [the citation audit](#support-reference-by-reference) below.

### Ruling 13: the claim of executed code

#14 §6 opened: "All numerical statements in Secs. 2-4 were computed by executed code rather than by hand." The referee: "the p error (a dropped prefactor of 4576) and the psi window (factor 3-10 in mass) indicate otherwise or a coding error" (Step 4(a) item 9). The finding: "v3 §6 "all numbers computed by executed code" overstates". Upheld in substance: "The code checked the arithmetic of a wrong model. See lesson 2." The numbers had been computed by code, the script that gated v3; the code encoded wrong inputs, and its anchor for the Kibble normalization reproduced v2's own number. Lesson 2 made the response a rule: an anchor must be independent of the paper ([verification checks arithmetic, not the model](/wiki/method/verification/arithmetic-not-model); [independent anchors](/wiki/method/verification/independent-anchors); [the lessons](/wiki/method/review/round-3/decisions#the-lessons)).

## The compatibility theorem: verified and re-attributed

Step 3 of the protocol asked the referee to re-derive the one theorem #14 states, the [compatibility theorem](/wiki/phase-space/born-geometry/compatibility-theorem): a positive metric H on phase space that satisfies both (η⁻¹H)² = 1 and (ω⁻¹H)² = −1 has the form H = diag(g, g⁻¹). The referee confirmed the proof's block identities symbolically for d = 1 and 2, proved the case d = 2 with a Gröbner basis, and tested d = 3 and 4 numerically on random matrices (Step 3). Its verdict: `theorem TRUE; stated proof VALID (uses positivity where it is not needed; slightly weaker hypothesis suffices)`. The diagonal blocks alone give B·A = 1, so positivity is needed only for g to be a positive metric, not for the off-diagonal block C to vanish ([the re-derivation](/wiki/phase-space/born-geometry/compatibility-theorem#round-3s-independent-re-derivation)).

The referee also found the theorem in the literature of [Born geometry](/wiki/phase-space/born-geometry): "essentially the known Freidel-Leigh-Minic "Born geometry" statement (B-field vanishes <=> I = H^-1 omega compatible), uncited (1502.08005 p.11)". It added a limit on what the theorem shows: "It is a pointwise linear-algebra fact; it does not by itself establish any physics (the identification of a dynamical H, a rigid eta, and a second spin-2 field X is assumed, not derived)."

The adjudication: "**The compatibility theorem is verified** (sympy, including a Groebner basis at d = 2; random tests at d = 3, 4). But the referee identifies it as essentially the Born-geometry result of Freidel–Leigh–Minic (arXiv:1502.08005), which is uncited. Unless a comparison shows otherwise, the checkpoint's "[D] derived here" tag on it should become [T] with that citation." #11 v2.1 made the change: §5 now tags the theorem [T][V], credits the statement to Freidel–Leigh–Minic (FLM) [26S], keeps "The block proof and the machine check" as the program's, and records that "the positivity step is not needed for C = 0" ([attribution history](/wiki/phase-space/born-geometry/compatibility-theorem#attribution-history); [how a tag changes](/wiki/method/provenance-tags#how-a-tag-changes)).

## Omitted constraints

Step 4(c) of the audit lists constraints #14 had not evaluated, each with its literature "verified on INSPIRE/arXiv", and in several cases with the referee's own estimate in code. Three of its eleven items became rulings: Kibble–Zurek and first-order overproduction (ruling 3), the hidden θ and the Witten effect (ruling 9), and the dark-energy aside (ruling 11). The adjudication accepted the rest as a list, "accepted as a to-do; not individually re-checked":

| The adjudication's item | The referee's item (Step 4(c)) |
| --- | --- |
| "Re-thermalization by ψ at ε ~ 1e-7–1e-6" | 2, with Step 4(a) item 5 |
| "SN1987A and BBN limits on millicharged particles" | 3, and the nucleosynthesis limits in 2 |
| "Charged-subcomponent and CMB bounds" | 4 |
| "Dark acoustic oscillations" | 5 |
| "The Higgs portal" | 7 |
| "The reheating mechanism for ξ" | 9 |
| "Collective magnetic-plasma effects" | 6 |
| "Uncited prior art: Murayama–Shu; LMW; Baek–Ko–Park; Khoze–Ro." | 10 |

The first four items concern ψ, which carries a small visible charge, about ε times the electron's, if the photons mix kinetically: a millicharged particle (MCP) [T]. The numbers below are the referee's and were not re-checked by the adjudicator.

### Re-thermalization through a millicharge

A millicharged ψ can be produced by the Standard Model plasma through its visible charge. If production is fast enough, ψ comes into equilibrium with our plasma and drags the hidden sector with it, undoing the colder hidden temperature that v3 required [T]. The referee computed this freeze-in (Step 4(a) item 5): "with eps = 1e-6 the SM freeze-in of psi reaches equilibrium for all m_psi <= 30 GeV (Y_FI/Y_eq = 4.9e3 (3 MeV) ... 1.1 (30 GeV)); with eps=1e-7 for m_psi <~ 0.3 GeV", from s-channel production only, which it calls "conservative". SM is the Standard Model. Then "The hidden sector is re-thermalised below v and the reheating ratio xi is no longer the operative variable", and the extra radiation is set by when the hidden photon decouples: "T_d < 0.2 GeV -> Delta N >= 0.61 (excluded); T_d = 0.2-30 GeV -> 0.065-0.11 (gamma' only) up to 0.48-0.83 if the psi entropy is dumped after decoupling (step4.out)". The literature it cites (item 2): Vogel and Redondo, JCAP 02 (2014) 029, arXiv:1311.2600, a Planck-2013-era analysis that "disfavors MCPs with masses between 14 MeV < m_f < 390 MeV for a wide range of minicharges eps > 1e-7", and Adshead, Ralegankar and Shelton, arXiv:2206.13530, for the threshold of thermalization ([no portal that re-equilibrates the sectors](/wiki/dark-matter/candidates/soliton-candidate/hidden-thermal-history#no-portal-that-re-equilibrates-the-sectors)).

### Supernova SN1987A and nucleosynthesis limits

Light particles produced in the hot core of a supernova and escaping from it would carry energy away and shorten the neutrino burst observed from supernova SN1987A; particles that interact too strongly stay trapped and carry little energy out, so the excluded region is a band in charge [T]. The referee (item 3): Chang, Essig and McDermott, arXiv:1803.00993, "For a millicharged particle, we exclude charges between 1e-9 - few x 1e-6 ... for masses <~ 200 MeV" — a band that "covers the whole stated charge range for m_psi = 1-200 MeV". v3's window for ψ ran from the MeV scale to about 0.1 TeV "at visible charge ~ (1e-7 to 1e-6) e" (#14 §5, exclusion condition 3). Nucleosynthesis adds a limit at low mass: Vogel and Redondo "exclude MCPs with m_f < 16 MeV for eps > 1.4e-8" (item 2) ([channels that became moot](/wiki/dark-matter/candidates/soliton-candidate/psi-relic-window#channels-that-became-moot)).

### Charged-subcomponent and cosmic-microwave-background bounds

v3 allowed ψ to be up to 10% of the dark matter: a charged subcomponent. The referee listed the bounds on such a component (item 4): Stebbins and Krnjaic, JCAP 12 (2019) 003, "q/e <~ 1e-13+-1 m/GeV, weakened by f^-1/2 for f >~ 0.13", with f the fraction of the dark matter; McDermott, Yu and Zurek, PRD 83 (2011) 063509, from recombination, "eps < 1e-6 at 1 GeV for all DM"; the competing effects of evacuation from the galactic disk (Chuzhoy and Kolb, JCAP 07 (2009) 014) and of acceleration by supernova shocks (Dunsky, Hall and Harigaya, JCAP 07 (2019) 015), so that "terrestrial direct detection of psi is non-trivial and unevaluated"; and limits from the cosmic microwave background on dark matter that scatters off baryons, which "vanish below 0.4% interacting fraction (Boddy et al. 1808.00001); psi up to 10% is not automatically safe."

### Dark acoustic oscillations

A component of the dark matter that stays coupled to a bath of dark radiation behaves as a fluid with pressure: sound waves travel through it, as through the photon–baryon plasma before recombination, and leave oscillations in its density on the scales that were inside the horizon while the coupling lasted [T]. ψ is coupled to the hidden photons by Thomson-like scattering, and the referee's script computed when that coupling ends (item 5): "psi kinetically coupled to the gamma' bath until z = 2.7e3 (30 MeV), 7.0e4 (0.3 GeV), 2.2e6 (3 GeV), 6.9e7 (30 GeV) for Delta N = 0.286 (step4.out)", the largest hidden radiation the bound of ruling 5 allows. "For sub-GeV psi this approaches recombination", and Cyr-Racine et al., arXiv:1310.3278, allow "at most ~5% of all DM" to interact very strongly with dark radiation. The referee's verdict: "Not addressed."

### Collective magnetic-plasma effects

v3 called its monopoles "effectively collisionless" on the strength of their two-body scattering cross-section, σ_T/M ~ 1e-26 cm²/g ([self-interaction](/wiki/dark-matter/candidates/soliton-candidate/benchmark-arithmetic#self-interaction)). A population of charges also responds collectively. Its plasma frequency ω_p, set by the density, charge and mass of the carriers, gives the time 1/ω_p on which collective oscillations and instabilities develop [T]; here the charges are the monopoles' magnetic charges, coupled through the massless hidden photon. The referee's script (`step4.out`, section 5):

```text
local 0.4 GeV/cm3: omega_p = 1.84e-09 s^-1, 1/omega_p = 1.72e+01 yr
cluster ~1e-2 GeV/cm3: omega_p = 2.91e-10 s^-1, 1/omega_p = 1.09e+02 yr
cosmic mean: omega_p = 3.28e-12 s^-1, 1/omega_p = 9.67e+03 yr
```

These times are "far shorter than dynamical times", and Lasenby, arXiv:2007.00667, "shows such instabilities can matter "many orders of magnitude below" two-body bounds (he gives no constraint)". The referee's conclusion (item 6): ""Effectively collisionless" rests on two-body sigma_T only. Unevaluated, not an indictment."

### The Higgs portal

The combination |H|² of our Higgs doublet H (here the Higgs field, not the program's phase-space metric) is gauge invariant, so any scalar of a hidden sector can couple to it at renormalizable order; this coupling is called the Higgs portal [T]. For #14's adjoint scalar the operator is λ_p |H|² Tr Φ², "allowed by every stated symmetry". When Φ takes its vacuum value v the operator adds λ_p v² to the Higgs mass term, which would have to be cancelled if it exceeded the square of the Higgs mass [T]. The referee's script (`step4.out`, section 6):

```text
v=8.09e+11: lambda_p v^2 <= m_h^2 (125 GeV)^2 needs lambda_p <= 2.4e-20
v=1.45e+12: lambda_p v^2 <= m_h^2 (125 GeV)^2 needs lambda_p <= 7.5e-21
portal equilibrates sectors at T=1e+12 if lambda_p >~ 5.3e-02
```

A portal strong enough to bring the two sectors into equilibrium at T ~ v "would set xi=1 -> Delta N = 0.86 (excluded). Technically natural to set small, but unstated" (item 7). #14 had not mentioned the portal ([the hidden sector's thermal history](/wiki/dark-matter/candidates/soliton-candidate/hidden-thermal-history#no-portal-that-re-equilibrates-the-sectors)).

### Reheating

A colder hidden sector is an assumption about how the universe was reheated after inflation, which "the framework does not fix" (#14 §4). The referee's item 9:

> Reheating: requires visible T_RH >~ v/xi = 1.06e12 - 1.90e12 GeV (step4c.out) and a two-field (or asymmetric) reheating mechanism for xi; a separately reheated hidden sector can carry dark-radiation isocurvature (conditional; not computed). No CMB-scale monopole isocurvature expected from post-inflation production (inference, not computed).

The hidden plasma must reach the breaking scale v for the monopoles to form after inflation, and at temperature ratio ξ that needs a visible reheating temperature T_RH of at least about v/ξ [T]. A single inflaton decaying equally into both sectors would give them the same temperature, hence the need for two fields or an asymmetric decay [T]. Isocurvature here means a fluctuation in the ratio of hidden to visible radiation rather than in the total density [T] ([a reheating mechanism](/wiki/dark-matter/candidates/soliton-candidate/hidden-thermal-history#a-reheating-mechanism); [inflation, reheating and entropy dilution](/wiki/cosmology/early-universe/inflation-and-dilution)).

### Uncited prior art

The referee's item 10 named prior work that #14 did not cite: "Baek, Ko & Park JCAP 10 (2014) 067 [1311.1035]; Khoze & Ro JHEP 10 (2014) 061 [1406.2291] (both: hidden SU(2)->U(1) monopoles + W' + dark photon); Murayama-Shu; LMW; Freidel-Leigh-Minic (Born geometry, for Sec. 1)." Its conceptual audit concluded that the proposal "is the standard hidden 't Hooft-Polyakov-monopole scenario (Baek-Ko-Park 2013; Khoze-Ro 2014; Murayama-Shu 2009; LMW 2026) with one coupling choice (alpha_d = alpha), and it stands or falls on that literature, independently of Born reciprocity" (Step 4(d)). Step 1 adds three further uncited items: the mass factor f ~ 1.79 at large self-coupling, which the referee checked numerically instead; the dark-energy sentence of §4; and the normalization of one monopole per Hubble volume, for which it used Gangui, astro-ph/0110285, "n_monop/s ~ 100 (T_c/m_P)^3".

#11 now cites Freidel–Leigh–Minic [26S], Murayama–Shu [28S] and Liveoak–Maharana–Wells [29S]. It does not cite Baek–Ko–Park or Khoze–Ro, and Gangui serves as an anchor in the gate rather than as a reference ([other prior art](/wiki/dark-matter/candidates/soliton-candidate/prior-art#other-prior-art); [the Kibble normalization in the gate](/wiki/dark-matter/candidates/soliton-candidate/kibble-normalization#the-corrected-value-in-the-gate)).

### What became of the list

Decision 1, strict sector separation, names the three channels it closes: it "closes three failure channels at once: ψ millicharge, the monopoles' Witten-effect charge (ruling 9), and re-thermalization of the hidden sector" ([Decision 1](/wiki/method/review/round-3/decisions#decision-1-strict-sector-separation)). Decision 2 then retired the candidate the list had been written against. No later document returns to the list, which stands as the adjudication wrote it.

## The citation audit

### Method

Step 1 of the protocol asks for two checks of each reference: that it exists as cited, and that it supports what it is cited for. The referee queried INSPIRE for each item of #14's reference list with `cite_fetch.py`, which retrieves titles, authors, journal, volume, page, year, arXiv identifier and DOI; read the arXiv abstracts; and searched the full texts with `pdfgrep.py` "for the specific claim each reference is cited for" (Step 1). The Particle Data Group's 2024 monopole review was confirmed on the PDG's own site.

### Every reference exists

The result, with the referee's capitals lowered: "all 23 references (37 individual items) resolve on INSPIRE with matching authors / journal / volume / page / year / arXiv id. No fabricated or mis-numbered reference found." The pre-registration had forecast exactly this, "all 23 resolve", and expected the likeliest problems in the two references not checked live before the round: Kolb and Turner's textbook, which "resolves as Front. Phys. 69 (1990), Addison-Wesley", and the journal reference of Hiramatsu et al., which also resolved ([how the forecast scored](/wiki/method/review/round-3/preregistration#how-it-scored)).

### Support, reference by reference

Existence is the weaker test: a real paper cited for something it does not say passes it. The referee's findings on support (Step 1), with the claim #14 cites each reference for:

| Ref. | Work | Cited in #14 for | The audit's finding |
| --- | --- | --- | --- |
| [1] | Born 1938, 1949 | the rotation (x, p) → (p, −x) ([Born reciprocity](/wiki/phase-space/reciprocity/born-reciprocity)) | metadata correct; the 1938 abstract does not state the rule and the primary text was paywalled: `PARTIALLY VERIFIED (primary text not read)` |
| [2] | Boulanger, Damour, Gualtieri, Henneaux 2001 | the exclusion of a massless X coupled to gravity ([the multi-graviton no-go](/wiki/gravity/spin-2-fields/multi-graviton-no-go)) | supports, with the caveats "2-derivative, local, ghost-free" |
| [3] | Hassan, Rosen (two papers) | the ghost-free bimetric structure ([Hassan–Rosen bimetric gravity](/wiki/gravity/spin-2-fields/hassan-rosen-bimetric)) | supports |
| [4] | Comelli et al.; Könnig et al.; Lagos, Ferreira | instabilities of bimetric cosmologies ([bimetric cosmology](/wiki/gravity/spin-2-fields/bimetric-cosmology)) | supports, with a "slight over-generalisation": Könnig et al. identify a stable model, and Lagos and Ferreira find stable scalar perturbations for one parameter choice (ruling 12) |
| [5] | Akrami et al. | late-time stability of a heavy spin-2 field ([stability at equal Planck masses](/wiki/gravity/momentum-graviton/equal-planck-mass-stability)) | supports |
| [6] | Higuchi 1987 | the bound m² ≥ 2H² ([partially massless gravity](/wiki/gravity/spin-2-fields/partially-massless-gravity)) | supports: the abstract's bound with Λ = 3H² "is m^2 >= 2H^2" |
| [7] | Dirac 1931; Zwanziger 1968 | the antisymmetric charge pairing ([Dirac quantization](/wiki/electric-magnetic-duality/monopoles/dirac-quantization); [the symplectic charge lattice](/wiki/electric-magnetic-duality/symplectic-charge-lattice)) | supports; Zwanziger's abstract states the pairing in 4π ℤ where #14 writes 2π ℤ, though the monopole with doublets "realises 2 pi, so the physics is fine"; "Charge space is symplectic" is "interpretation"; and Schwinger, named in the text, is not cited (ruling 12) |
| [8] | Montonen, Olive; Osborn; Harvey | exact duality tested only with supersymmetry ([S-duality](/wiki/electric-magnetic-duality/s-duality)) | supports |
| [9] | Gherghetta, Kersten, Olive, Pospelov 2019 | mixing from gravity alone ([kinetic mixing between sectors](/wiki/dark-matter/candidates/soliton-candidate/kinetic-mixing#an-unresolved-reading-ceiling-or-floor)) | supports both parts; the paper presents 1e-13 as a floor, "consistent with "<~" only in the sense "up to"" |
| [10] | Baumgart et al.; Chen, Cline, Frey; Brümmer, Jaeckel | the dimension-5 operator and ε ~ v/M_\* | "cited for more than it says" (ruling 7); the claim that Baumgart et al. lack the operator was overturned (ruling 8) |
| [11] | Banks, Seiberg; Harlow, Ooguri | no exact global symmetries in quantum gravity | supports |
| [12] | Hiramatsu, Ibe, Suzuki, Yamaguchi 2021 | no visible magnetic flux while U(1)_d is unbroken | supports (abstract) |
| [13] | Terning, Verhaaren 2018 | minicharged monopoles need a massive hidden photon | supports (p. 11) |
| [14] | Brümmer, Jaeckel, Khoze 2009 | a small visible electric charge under charge-conjugation and parity (CP) violation | supports (abstract) |
| [15] | 't Hooft; Polyakov 1974 | the monopole ([the 't Hooft–Polyakov monopole](/wiki/electric-magnetic-duality/monopoles/thooft-polyakov-monopole)) | supports ("monopole mass of order 137 M_W") |
| [16] | Prasad, Sommerfield; Bogomolny | f = 1 in the Bogomolny–Prasad–Sommerfield (BPS) limit | supports f = 1; the value f ~ 1.79 at large self-coupling is not in [16] and is uncited |
| [17] | Kolb, Turner 1990 | the freeze-out formula ([relic abundance mechanisms](/wiki/dark-matter/candidates/relic-abundance)) | "standard; not checked page-level" |
| [18] | Kibble 1976 | the Kibble mechanism | supports (abstract) |
| [19] | Preskill 1979 | inefficient annihilation of superheavy monopoles ([the monopole problem](/wiki/electric-magnetic-duality/monopoles/monopole-problem)) | supports (abstract level) |
| [20] | PDG 2024 review (Milstead, Weinberg); Turner, Parker, Bogdan 1982; Parker 1970 | the Parker bound, "~1e-15 for M <~ 1e17 GeV" ([monopole flux bounds](/wiki/electric-magnetic-duality/monopoles/monopole-searches)) | supports, by the review's eq. (95.9); Turner–Parker–Bogdan's abstract quotes "F <~ 1e-16" as the Parker limit, but "the manuscript follows PDG; fine." |
| [21] | MACRO final result, 2002 | the limit 2.8e-16 "for m >~ 1e10 GeV" | supports "the 2.8e-16 figure exactly" |
| [22] | Adams et al. 1993 | the extended Parker bound | supports exactly; the PDG form adds a term "negligible here" |
| [23] | Planck 2018 VI | the bound on N_eff | supports: eq. (67b) gives `N_eff = 2.99 +0.34 -0.33 (95%, TT,TE,EE+lowE+lensing+BAO)` |

MACRO is the Monopole, Astrophysics and Cosmic Ray Observatory. For [23], #14 §4 writes the interval as "2.99 +- 0.34"; flag 22 in `review/wiki-build-flags.md` notes the difference from Planck's +0.34/−0.33, which changes nothing, since the bound uses only the upper side.

### Before and after the round

The v3 worklog had already checked the earlier version's list: "v2's [1]–[10] are all correct as cited", with three corrections, among them "Kibble's title is "Topology of Cosmic Domains and Strings"" and "Harvey's lectures are conference proceedings, not a journal article" (`review/v3-worklog.md`, 'Verified references for v3'). The round-3 audit checked #14's list only. #11's own reference list, whose memory-cited entries carry †, is a separate list, and its check is still open ([Open: the † literature battery](/wiki/method/literature-battery)).

## What survives v3

The adjudication's list:

- "The compatibility theorem (as [T], pending the FLM comparison)" — the re-tag was made in #11 v2.1 ([the compatibility theorem](/wiki/phase-space/born-geometry/compatibility-theorem));
- "The benchmark-conditional arithmetic: flux, densities, σ_T/M, W′ overclosure" ([benchmark-conditional arithmetic](/wiki/dark-matter/candidates/soliton-candidate/benchmark-arithmetic); [W′ overclosure](/wiki/dark-matter/candidates/soliton-candidate/w-prime-overclosure));
- "The kinetic-mixing literature points (a) and (c)": mixing from gravity alone, and no visible magnetic flux while U(1)_d is unbroken ([kinetic mixing between sectors](/wiki/dark-matter/candidates/soliton-candidate/kinetic-mixing));
- "The statement that the minimal adjoint-only sector is excluded."

#11 §12 gives its own list of survivors, which overlaps this one; the two are compared on [the obituary](/wiki/dark-matter/candidates/soliton-candidate/obituary#what-survives). The candidate itself is dead ([the graveyard](/wiki/status/graveyard)).

## Sources

- `review/round3-adjudication.md` 'Verdict' — the agreement and the two routes; 'Rulings' — the table of rulings 1–13, the omitted-constraints list and the compatibility theorem; 'What survives v3' — the survivors
- `review/round3/referee/audit-notes.md` Step 1 — the citation audit, the uncited claims and the Gangui normalization; Step 2 — the numbers table; Step 3 — the theorem; Step 4(a) — internal consistency, items 1–9; Step 4(b) — the mixing claims; Step 4(c) — the omitted constraints, items 1–11; Step 4(d) — the framework does no work; Step 5 — the grade, the reason and the weakest links
- `review/round3/referee/step4.out` — sections 4–6, the decoupling redshifts, plasma frequencies and the Higgs portal; `review/round3/referee/step4b.out` — the Witten-effect charges; `review/round3/referee/step4c.out` — the reheating temperatures
- `review/round3/referee/cite_fetch.py`, `review/round3/referee/pdfgrep.py` — the citation method
- `notes/knot-dark-matter-standalone.md` §2 — the dimension-5 operator; §4 — dark radiation and the dark-energy aside; §5 — the exclusion conditions; §6 — the claim of executed code and acceptance criterion 3; 'References' — the cited list
- `review/v3-worklog.md` 'Verified references for v3', 'v3 as drafted (2026-10-19)' — the earlier reference check and the references not checked live
- `papers/broken-born-checkpoint-v2.md` §5 — the re-tag; §10 — "Under pressure"; §12 — the corrected numbers as [V]; 'References' — [26S]–[29S]
- `verify/soliton_obituary.py` — the gated numbers of rulings 1, 2, 4 and 5
- `review/skeptic-review-console.html` — the referee prompt's gloss of grade C
- `review/wiki-build-flags.md` items 21–22 — ruling 3's lower figure; Planck's interval; item 33 — the referee's figures the soliton script does not check
