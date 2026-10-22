---
title: "Round-3 arbitration and the referee's constants"
weight: 40
status: record
description: "The adjudicator's recomputation from an independent anchor (p = 104.31; M* = 2.9–4.4×10¹² GeV; the ψ recount), the referee's numbers check and its externally sourced constants, where the two calculations differ, and how the numbers reached the gate."
provenance: [V]
sources:
  - "review/round3/adjudicator/round3_arb.py"
  - "review/round3/adjudicator/round3_arb.out"
  - "review/round3-adjudication.md header"
  - "review/round3-adjudication.md 'Rulings'"
  - "review/round3/referee/audit-notes.md Step 2"
  - "review/round3/referee/audit-notes.md Step 4(a)"
  - "review/round3/referee/audit-notes.md Step 5"
  - "review/round3/referee/step2a.py"
  - "review/round3/referee/step2a.out"
  - "review/round3/referee/step2b.out"
  - "review/round3/referee/step2b_inf.out"
  - "review/round3/referee/step2c.out"
  - "review/round3/referee/step2c_psi.out"
  - "review/round3/referee/step2c_thr.out"
  - "review/round3/referee/step4b.out"
  - "review/round3/referee/step4d.out"
  - "verify/soliton_obituary.py"
  - "papers/broken-born-checkpoint-v2.md §12"
  - "notes/knot-dark-matter-standalone.md §2–§3"
  - "scripts/check.sh"
  - "CLAUDE.md 'Layout'"
  - "review/wiki-build-flags.md items 21, 33–34"
---

*The round-3 arbitration is the adjudicator's own recomputation of the central numbers the referee disputed, run before ruling on them: a short script, `review/round3/adjudicator/round3_arb.py`, that rebuilds [the Kibble normalization](/wiki/dark-matter/candidates/soliton-candidate/kibble-normalization) from the expansion rate of the radiation-dominated universe, finds the monopole mass at which the abundance matches the dark matter, and recounts the relic density of the light hidden fermion ψ. It confirmed the referee's central finding: one monopole per Hubble volume gives p = 104.31, where v3 had used 0.0228, so the mass that closes the abundance falls to 2.9–4.4×10¹² GeV and v3's benchmark of 3×10¹³ GeV is overproduced. The referee had done the same work independently, taking every physical constant from outside sources, chiefly the Particle Data Group's 2024 review and Planck 2018, rather than from the manuscript. The two calculations agree on the Kibble numbers and, on ψ, "to within ×1.6", and the adjudicator's numbers were carried into the gate.*

**Status:** Record. The numbers it settled carry [V] in #11 §12 (p, the closing mass and the overproduction), because `verify/soliton_obituary.py` recomputes them in the gate along with the ψ recount ([the soliton-obituary script](/wiki/method/verification/soliton-obituary-script)); the arbitration script itself sits in `review/` and the gate does not run it. The root `CLAUDE.md` 'Layout' says arbitration scripts go in `verify/`; no document resolves the difference ([conflicts between sources](/wiki/history/documents/source-conflicts#method-and-records)).

## What the arbitration is

An adjudication does not take the referee's numbers on trust without saying so. Where a ruling rests on a number, the adjudicator writes a script of its own and rules on what it prints, or states that it did not re-check the number ([adjudication](/wiki/method/review/review-protocol#after-the-referee-adjudication)). The round-3 adjudication's header: "My arbitration: `round3/adjudicator/round3_arb.py` and its `.out`, plus direct checks of the sources named below." The script covers rulings 1, 2 and 4 ([round-3 verdict and rulings](/wiki/method/review/round-3/rulings)). The direct checks are the passages the adjudication quotes as evidence, such as the two abstracts of ruling 3 and the footnote of ruling 8. The adjudicator did not re-run the referee's Kibble–Zurek integration ([the Kibble mechanism](/wiki/electric-magnetic-duality/monopoles/kibble-mechanism)), and rulings 6 and 9 were "Accepted, not re-checked".

The adjudicator was also the author, who had written v3 and the scripts that gated it. The arbitration script starts from an anchor fixed outside the manuscript, the coefficient of the expansion rate, rather than from v3's numbers ([independent anchors](/wiki/method/verification/independent-anchors)).

## The script

### The expansion rate and the Kibble normalization

The script's constants and its first calculation:

```python
M_PL=1.22089e19; M_PL_RED=2.43536e18; S0=2891.2; RHO_DM=0.120*1.05371e-5
gs=100.0
# H = 1.66 sqrt(g*) T^2 / M_Pl  (radiation era, non-reduced Planck mass)
print("1.66 check: sqrt(8 pi^3/90) =", round(sqrt(8*pi**3/90),4))
def p_one_per_hubble(mpl_reduced=False):
    pref = sqrt(pi**2*gs/90) if mpl_reduced else sqrt(8*pi**3*gs/90)
    return pref**3 * 45/(2*pi**2*gs)
```

M_PL is the Planck mass in GeV, M_PL_RED the reduced Planck mass, S0 the present entropy density in cm⁻³, and RHO_DM the mean dark-matter density, Ω h² = 0.120 times the critical density over h², in GeV cm⁻³. gs is g\*, the number of relativistic degrees of freedom at the transition.

The wiki's reading of the code, from textbook cosmology [T] ([Friedmann cosmology](/wiki/cosmology/scale-factor-duality/friedmann-cosmology); [the radiation era](/wiki/cosmology/early-universe/radiation-era)):

```text
radiation era:          H² = (8π/3) ρ/M_Pl²,   ρ = (π²/30) g* T⁴
so                      H  = √(8π³ g*/90) · T²/M_Pl  ≈ 1.66 √g* T²/M_Pl
entropy density:        s  = (2π²/45) g* T³
one defect per H⁻³:     n/s = H³/s = (√(8π³ g*/90))³ · 45/(2π² g*) · (T/M_Pl)³
```

The coefficient of (T/M_Pl)³ is p, which the function returns. In the reduced convention, M̄_Pl = M_Pl/√(8π), the prefactor becomes √(π² g\*/90), and the function returns the same physical count expressed against M̄_Pl. The first print is the script's anchor: the coefficient √(8π³/90) of the expansion rate, printed for comparison with the textbook 1.66 before it is used. Lesson 2 of the round names it as one of the two replacement anchors ([round-3 decisions and lessons](/wiki/method/review/round-3/decisions#lesson-2-anchors-independent-of-the-paper)).

### The closing mass

```python
g_d = 2*sqrt(4*pi/137.035999)
for f in (1.0, 1.787):
    r = 4*pi*f/g_d
    v = (RHO_DM*M_PL**3/(r*p_one_per_hubble()*S0))**0.25
    print(f"f={f}: M* (Kibble minimum production) = {r*v:.2e} GeV; v = {v:.2e}; 3e13 overproduced x{(3e13/(r*v))**4:.1e}")
```

The model is #14 v3's. Hypothesis H sets the smallest hidden charge equal to the electron's, (g_d/2)²/4π = α, which fixes the hidden gauge coupling g_d ([hypothesis H](/wiki/dark-matter/candidates/soliton-candidate/alpha-d-coupling#attempt-3-hypothesis-h)). The monopole mass is M = 4πf v/g_d, with v the symmetry-breaking scale and f between 1 in the Bogomolny–Prasad–Sommerfield (BPS) limit and 1.787 at large scalar self-coupling ([the 't Hooft–Polyakov monopole](/wiki/electric-magnetic-duality/monopoles/thooft-polyakov-monopole)). In the code r = M/v.

The wiki's reading of the solve [T]: monopoles formed at T_c ~ v with yield p (v/M_Pl)³ have today the number density p (v/M_Pl)³ s₀ and the mass density

```text
ρ = M · n = r v · p (v/M_Pl)³ s₀ = r p s₀ v⁴ / M_Pl³
```

Setting ρ equal to the observed dark-matter density gives v⁴ = ρ_DM M_Pl³/(r p s₀), the line in the code, and M\* = r v. At fixed p the density grows as v⁴, and so as M⁴, so a benchmark mass M is overproduced by (M/M\*)⁴, the factor printed last. #14 §3 had stated the same scaling: "Heavier monopoles are over-produced as (M/M\*)^4".

### The ψ recount

```python
def omega(m, gstar):
    sig=pi*(1/137.036)**2/m**2
    xf=20.0
    for _ in range(100): xf=log(0.038*2*M_PL*m*sig/sqrt(gstar))-0.5*log(xf)
    return 1.07e9*xf/(sqrt(gstar)*M_PL*sig)
```

ψ is the Dirac fermion v3 added to the hidden sector ([Obituary: the ψ relic window](/wiki/dark-matter/candidates/soliton-candidate/psi-relic-window)). The function is the standard approximate solution for the relic density of a species that freezes out with an s-wave cross-section [T] ([relic abundance mechanisms](/wiki/dark-matter/candidates/relic-abundance)): the freeze-out point x_f = m/T_f is found by iterating its defining equation, and Ω h² is proportional to x_f/(√g\* M_Pl σ). The gate's version of the same function cites "Kolb & Turner eqs. 5.43-5.45". The cross-section is σv = πα²/m², exact at low velocity for a fermion pair annihilating into two massless gauge bosons, as an electron and positron do into two photons [T]. The script's comment: "Dirac fermion, sigma v = pi alpha^2/m^2 exact s-wave; count psi+psibar and both doublet members". It then multiplies the relic of one species by 1 ("v3 counting") or by 4 ("psi+psibar, two doublet members") and finds, by bisection, the masses at which ψ is 100% and 10% of the dark matter, for g\* = 80 and 106.75.

## The output

`review/round3/adjudicator/round3_arb.out`, in full:

```text
1.66 check: sqrt(8 pi^3/90) = 1.6602
p, one defect per H^-3, non-reduced M_Pl: 104.31
p, one defect per H^-3, reduced M_Pl:     0.828
p used in v3 (45/(2 pi^2 g*)):             0.0228
f=1.0: M* (Kibble minimum production) = 2.87e+12 GeV; v = 1.38e+11; 3e13 overproduced x1.2e+04
f=1.787: M* (Kibble minimum production) = 4.44e+12 GeV; v = 1.20e+11; 3e13 overproduced x2.1e+03
g*= 80.00 v3 counting                      : 100% at    297 GeV, 10% at    92 GeV
g*= 80.00 psi+psibar, two doublet members  : 100% at    146 GeV, 10% at    45 GeV
g*=106.75 v3 counting                      : 100% at    321 GeV, 10% at    99 GeV
g*=106.75 psi+psibar, two doublet members  : 100% at    158 GeV, 10% at    49 GeV
```

### What each line settled

- **Ruling 1.** Lines 2–4. One defect per Hubble volume gives p = 104.31 with the Planck mass and 0.828 with the reduced Planck mass; v3's 0.0228 is 45/(2π² g\*), the formula with the expansion-rate prefactor left out. The ruling: "v3's 0.0228 drops (1.66√g\*)³ ≈ 4.6×10³. My error came from misremembering the formula." ([Obituary: the Kibble normalization](/wiki/dark-matter/candidates/soliton-candidate/kibble-normalization))
- **Ruling 2.** Lines 5–6. At minimum production the abundance closes at M\* = 2.87e+12 GeV (f = 1) to 4.44e+12 GeV (f = 1.787), and the 3×10¹³ GeV benchmark is overproduced ×1.2e+04 to ×2.1e+03. The ruling rounds these to "M\* = 2.9–4.4×10¹² GeV" and "2.1×10³–1.2×10⁴ times" ([overproduction at the benchmark](/wiki/dark-matter/candidates/soliton-candidate/overproduction)). Line 3 bears on the ruling's other point, that the "reduced-Planck factor of 3" was not a spread: p is a different number in the reduced convention, and "consistently normalized, the two conventions agree".
- **Ruling 4.** Lines 7–10. With v3's counting the exact cross-section puts all of the dark matter in ψ at 297–321 GeV and 10% at 92–99 GeV, near the lower ends of v3's own ranges; counting ψ, ψ̄ and both doublet members moves them to 146–158 GeV and 45–49 GeV, the ruling's "10% of the DM at 45–49 GeV, 100% at 146–158 GeV" (DM is dark matter).

## The referee's numbers check

The referee had recomputed every number of #14 v3's Sections 2–4 before the arbitration, and set its own value beside each with a verdict (audit notes, Step 2):

- **Confirmed.** The couplings under hypothesis H (α_W′ "1/34.259", α_m "34.259", the variant "137.036", and "28.61" or "28.86" with the coupling run to 10¹² GeV); the mass factor at large self-coupling, "1.7867", and the mass relation M = "20.75 - 37.07" v; the breaking scale and the W′ mass at the benchmark; the overclosure by the stable W′±; the factor ξ^(3/4); the benchmark densities, the counterfactual monopole flux and its excess over the three [flux limits](/wiki/electric-magnetic-duality/monopoles/monopole-searches), "7.50 / 8.06 / 12.03" orders of magnitude; ε ~ v/M_\* "as arithmetic (order of magnitude)"; ΔN_eff = "0.8567" for a hidden sector at our temperature; σ_T/M "(factor-2 convention)"; and the [gravitational-wave](/wiki/cosmology/early-universe/phase-transition-gravitational-waves) peak, "1.35e5 - 2.47e7 Hz".
- **Discrepant.** The Kibble normalization p, "(factor ~1e3-5e3)"; the mass band M\* with the correct p; the benchmark's "no dilution"; the masses at which ψ would make up 10% and all of the dark matter, "(factor 3-10 in mass)"; and the bound on the temperature ratio ξ, a "minor DISCREPANCY (should be 0.76)".
- **Arithmetic right, input wrong.** The mass band recomputed from #14's own inputs ("arithmetic reproduces, but rests on wrong p"), the reduced-Planck factor "3.350" ("a convention artefact, not a physical spread") and the [entropy dilution](/wiki/cosmology/early-universe/inflation-and-dilution) needed at 10¹⁶ GeV ("input M\* wrong").
- **Beyond the manuscript.** The cited sources' own estimate of ε, "3 orders smaller"; a "missing variant" in which ψ's charge is matched to e/3, the smallest charge of the Standard Model, giving α_m = "308.3"; and the galactic acceleration of monopoles in the Particle Data Group's (PDG) review, eq. 95.8, which v3 had not used: "conclusion strengthened".

Among the confirmed numbers are the [benchmark-conditional arithmetic](/wiki/dark-matter/candidates/soliton-candidate/benchmark-arithmetic) and the [W′ overclosure](/wiki/dark-matter/candidates/soliton-candidate/w-prime-overclosure) that survive v3. The discrepant ones became rulings 1, 2, 4 and 5, and the ε estimate ruling 7 ([Obituary: Planck-suppressed adjoint mixing](/wiki/dark-matter/candidates/soliton-candidate/dimension-five-operator)).

The referee also checked its own codes against known answers before using them, the discipline the program wrote down as lesson 2 (the wiki's reading):

- the monopole-mass solver against the exact BPS solution, "BPS analytic solution energy (units 4 pi v/g): 0.983333  (expect 1)" (`step2b.out`), which the audit notes record as "BPS check E=1 with tail", that is, once the energy beyond the integration range is added; then the large-coupling limit, "f_inf=1.7857" with the energy beyond the grid added (`step2b_inf.out`), to which `step2a.py` adds the innermost interval to reach 1.7867;
- the annihilation calculation against scalar electrodynamics, "sigma v(S+S- -> gg) = 2.0000 pi a^2/m^2 (textbook: 2)" (`step2c.out`);
- the relic code against a standard weakly interacting massive particle (WIMP): "[validation] visible Majorana WIMP 100 GeV, <sv>=2.2e-26: Omega h^2 = 0.1145 (expect ~0.10-0.12)" (`step2c_psi.out`).

## The referee's constants

The protocol asks for every number to be re-checked "from independently chosen constants", so that the check does not inherit the manuscript's inputs. The referee's notes list its constants and its check of the manuscript's inputs (Step 2, verbatim):

```text
Own constants: alpha^-1=137.035999; alpha_hat(MZ)^-1 = 127.930 (PDG 2024 EW review); MPl=1.220890e19 (PDG 2024 astro);
rho_c/h^2=1.053672e-5 GeV/cm^3; s0=2891.2/cm^3 (PDG 2024 astro); Omega_c h^2 = 0.120 (Planck 2018); N_eff 95% from Planck eq. 67b.
Manuscript inputs checked: rho_DM = 1.264 keV/cm^3 (OK), s0 ~2.9e3 (OK), MPl 1.22e19 (OK); local 0.4 GeV/cm^3 (PDG canonical 0.3, x2-3).
```

The docstring of `step2a.py` gives the source of each, naming for two the document it was read from in the referee's `dl/` download folder, which the repository does not keep (an excerpt; the unit conversions are omitted):

```text
  alpha(0)^-1 = 137.035999     CODATA 2018 / PDG 2024 physical constants
  alpha_hat^(5)(MZ)^-1 = 127.930 (MSbar)   PDG 2024 "Electroweak model" review, p.4 (dl/pdgew)
  MZ = 91.1876 GeV             PDG
  M_Pl = 1.220890e19 GeV       PDG 2024 astrophysical constants (dl/pdgastro)
  reduced M_Pl = M_Pl/sqrt(8 pi)
  rho_crit/h^2 = 1.053672e-5 GeV cm^-3   PDG 2024 astrophysical constants
  Omega_c h^2 = 0.120          Planck 2018 VI abstract
  s0 = 2891.2 cm^-3            PDG 2024 astrophysical constants
  local DM density: manuscript uses 0.4 GeV/cm^3; PDG canonical 0.3 "within factor 2-3" -> also report 0.3
  Planck 2018 eq. (67b): N_eff = 2.99 +0.34 -0.33 (95%); N_eff,SM = 3.044 (Bennett et al 2021) or 3.046 (Planck's value)
```

The one input the referee flagged is the local dark-matter density: #14 used 0.4 GeV/cm³ against the PDG's canonical 0.3, so the referee reported the local spacing for both values ([benchmark-conditional arithmetic](/wiki/dark-matter/candidates/soliton-candidate/benchmark-arithmetic)). The arbitration script uses its own set: the same Planck mass and entropy density, and the critical density as 1.05371e-5 against the referee's 1.053672e-5.

## Where referee and adjudicator differ

- **The ψ window.** The referee integrated the Boltzmann equations with the hidden sector's own temperature, starting from a ratio ξ₀ to ours, and found ψ at 10% and 100% of the dark matter at 28.3 and 96.3 GeV for ξ₀ = 1, 34.9 and 117.8 GeV for ξ₀ = 0.76, and 45.9 and 153.4 GeV for ξ₀ = 0.5 (`step2c_thr.out`). The adjudicator's formula gives 45–49 and 146–158 GeV. Ruling 4: "The referee's Boltzmann integration gives 28–46 / 96–153 GeV. We agree to within ×1.6, and v3's 0.1–0.3 TeV was wrong." The gate checks the adjudicator's numbers. Both calculations put v3's window too high.
- **The count per Hubble volume.** The referee also gave the mass for one defect per (4π/3)H⁻³ rather than per H⁻³, "4.11e12 - 6.35e12" GeV with p = 24.90 (Step 2). The adjudication and the gate use one per H⁻³ ([the count per Hubble volume](/wiki/dark-matter/candidates/soliton-candidate/overproduction#the-count-per-hubble-volume-a-convention)).
- **The colder hidden sector.** At ξ = 0.76, the corrected bound on the temperature ratio, the referee's minimum-production mass is "2.34e12-3.61e12 GeV", and the benchmark is "overproduced by 2.1e3-2.7e4 (step4b.out)" over both temperature ratios (Step 4(a) item 1). The adjudication quotes the values at ξ = 1.
- **What was not re-run.** "I did not re-run the referee's Kibble–Zurek integration (1e9–1e12 overproduction)" (ruling 3). Flag 21 in `review/wiki-build-flags.md` notes that the integration itself gave 1.1e12–2.2e12 and that the 1e9 lower end is the referee's analytic estimate from Liveoak–Maharana–Wells, 1.2e9–2.2e11; the verdict is the same either way. Rulings 6 and 9 rest on the referee's evidence alone.

## From the arbitration to the gate

The adjudication's header: "The corrected inputs now live in `verify/soliton_obituary.py`, which checks every number this record quotes." The gate script re-implements the arbitration's three calculations with the same formulas and the arbitration's values of M_Pl, s₀ and the dark-matter density, and adds anchors that run first: the Friedmann coefficient, the published normalization of one defect per Hubble volume (Gangui, astro-ph/0110285), a standard freeze-out relic, and ΔN_eff = 1 for one extra neutrino species. Its lines for rulings 1, 2 and 4, from the current run:

```text
== Kibble normalization (ruling 1)
PASS  p = 104.31 with M_Pl  [104.3106]
PASS  p = 0.828 with reduced M_Pl  [0.8279]
PASS  v3's 0.0228 drops (1.66 sqrt(g*))^3 ~ 4.6e3  [4575.6]

== Mass and overproduction (ruling 2)
PASS  M* at minimum production = 2.9-4.4e12 GeV  [2.873e+12-4.441e+12]
PASS  the two Planck conventions agree when p is normalized consistently
PASS  the 3e13 benchmark is overproduced 2.1e3-1.2e4 times  [2.08e+03-1.19e+04]

== psi relic window (ruling 4): psi, psi-bar, both doublet members; sigma v = pi alpha^2/m^2
PASS  10% of the dark matter at 45-49 GeV  [45.2-48.8]
PASS  100% at 146-158 GeV  [146.4-158.0]
```

#11 §12 tags p ≈ 104, the closing mass and the overproduction [V] on the strength of these checks. Two flags in `review/wiki-build-flags.md` qualify the script's description of itself. Flag 33: it does not check every number the record quotes; the referee's numbers in rulings 3 and 4, ruling 6's figure and the surviving benchmark arithmetic are not among its checks. Flag 34: its docstring calls its constants "PDG and Planck 2018 values", but they are typed into the script, not retrieved ([the soliton-obituary script](/wiki/method/verification/soliton-obituary-script)).

The arbitration script itself stays in `review/round3/adjudicator/`. The gate, `scripts/check.sh`, runs a fixed list of `verify/` scripts and then the wiki check, and its header says "New arbitration and audit scripts in verify/ get added here"; the root `CLAUDE.md` 'Layout' says the same of `verify/`: "arbitration and audit scripts go here". Round 4's arbitration scripts also stayed in `review/`. No document reconciles the stated layout with where the scripts are ([the gate](/wiki/method/verification/the-gate); flag 38 in `review/wiki-build-flags.md`).

## Sources

- `review/round3/adjudicator/round3_arb.py` — the constants, the anchor, the Kibble normalization, the closing mass and the ψ counting
- `review/round3/adjudicator/round3_arb.out` — the printed numbers
- `review/round3-adjudication.md` header — "My arbitration" and the move to `verify/`; 'Rulings' 1–4 — how the arbitration fed the rulings, and what was not re-run
- `review/round3/referee/audit-notes.md` Step 2 — the numbers table, the constants and the manuscript inputs checked; Step 4(a) item 1 — the colder-sector mass; Step 5 — the grade the numbers supported
- `review/round3/referee/step2a.py` — the sources of the referee's constants; `review/round3/referee/step2b.out`, `review/round3/referee/step2b_inf.out`, `review/round3/referee/step2c.out`, `review/round3/referee/step2c_psi.out` — the referee's validations; `review/round3/referee/step2c_thr.out` — its ψ window; `review/round3/referee/step2a.out`, `review/round3/referee/step4b.out`, `review/round3/referee/step4d.out` — its masses and conventions
- `verify/soliton_obituary.py` — the gated recomputation and its anchors
- `papers/broken-born-checkpoint-v2.md` §12 — the corrected numbers as [V]
- `notes/knot-dark-matter-standalone.md` §2 — hypothesis H; §3 — the mass relation and the (M/M\*)⁴ scaling
- `scripts/check.sh` — the scripts the gate runs; `CLAUDE.md` 'Layout' — where arbitration scripts belong
- `review/wiki-build-flags.md` items 21, 33 and 34 — ruling 3's lower figure; the script's coverage and constants
