---
title: "Independent anchors"
weight: 30
status: method
description: "An anchor must come from outside the paper — a textbook identity or a published value; a check that reproduces the paper's own number is circular, as the soliton manuscript's Kibble anchor was."
sources:
  - "CLAUDE.md 'Method'"
  - "review/round3-adjudication.md 'Lessons (now in CLAUDE.md)'"
  - "review/round3-adjudication.md 'Rulings'"
  - "review/round3/referee/audit-notes.md Step 4(a)"
  - "review/round4-preregistration.md 'Predictions'"
  - "review/round4-adjudication.md 'Pre-registration scored'"
  - "verify/soliton_obituary.py"
  - "verify/toy_coset.py"
  - "verify/toy_gw.py"
  - "verify/toy_s4.py"
  - "verify/toy_s5.py"
  - "verify/battery.py"
  - "verify/literature_check.py"
  - "verify/dual_sector.py"
  - "review/v3-worklog.md 'New open items (to compute before v3 states anything about them)'"
  - "review/v3-worklog.md 'Findings neither referee raised'"
  - "review/wiki-build-checks/README.md"
  - "review/wiki-build-flags.md items 11, 14, 16, 28"
  - "verify/velocity_gated_gravity.py 'D. The obituary's scope'"
  - "review/wiki-build-flags.md item 16"
  - "verify/phase_space_diameter.py"
  - "verify/closed_universe.py"
  - "verify/velocity_gated_gravity.py"
  - "verify/gate_mechanism.py"
  - "review/round5-adjudication.md 'Rulings' R12"
---

*An anchor is a check that a verification script must pass against something known independently of the paper being checked, such as a textbook identity or a published value, before its own numbers are trusted. A check that only reproduces the paper's own figure is circular: if the paper's formula is wrong, the check repeats the error and passes. Review round 3 found such a case in the soliton manuscript, whose script anchored the monopole count to the previous draft's own figure and computed [the Kibble normalization](/wiki/dark-matter/candidates/soliton-candidate/kibble-normalization) too small by a factor of about 4.6×10³ without failing. The rule has been in the program's method since, and seven of the twelve current scripts open with anchor checks taken from textbooks or from the cited literature.*

**Status:** Method, in force (round-3 lesson 2, now in root `CLAUDE.md`) — untagged — applied in `verify/soliton_obituary.py`, `verify/toy_coset.py`, `verify/toy_gw.py`, `verify/phase_space_diameter.py`, `verify/closed_universe.py`, `verify/velocity_gated_gravity.py` and `verify/gate_mechanism.py`, which print their anchor checks first, and in identity checks in `verify/toy_s5.py`.

## The rule

Root `CLAUDE.md`, 'Method': "A verification check confirms arithmetic, not the model. An anchor must be independent of the paper (a textbook identity, a published value). A check that reproduces the paper's own number is circular. Round 3 caught a wrong Kibble normalization that a circular anchor had passed."

The rule is round-3 lesson 2: "An anchor must be independent of the paper. v3's Kibble anchor reproduced v2's own number and so tested nothing. The replacement anchors are the Friedmann coefficient 1.66 and n/s ≈ 100 (T_c/M_Pl)³ for one defect per Hubble volume." (`review/round3-adjudication.md`). It is the repair for the limit stated on [Verification checks arithmetic, not the model](/wiki/method/verification/arithmetic-not-model).

## What an anchor does

This section is the wiki's reading.

A script that recomputes a paper's numbers encodes the paper's formulas and inputs. If it is checked only against the paper's figures, a wrong formula yields a wrong figure that the check confirms. An anchor tests the encoded formula first on a case whose answer is known from outside the paper, the way an instrument is calibrated on a reference sample before it measures an unknown one. If the formula carries a wrong factor, the reference case fails.

Two consequences follow from this:

- **The anchor must exercise the same code.** An anchor tests something only if the later checks reuse the function or constant it tested.
- **The anchor's tolerance sets what it can catch.** A window anchor that accepts a factor of two catches a dropped factor of thousands, not a 10% slip; the precision of the later figures then rests on the arithmetic alone.

## The circular anchor of round 3

The [soliton manuscript](/wiki/dark-matter/candidates/soliton-candidate/obituary) (#14 v3) was checked by knot_numbers.py, a script that recomputed every number the manuscript quoted ([the soliton-obituary script](/wiki/method/verification/soliton-obituary-script)). At v3 (commit 5dbaa82) its anchor section held four checks: a standard [freeze-out relic](/wiki/dark-matter/candidates/thermal-freeze-out#the-anchor), one extra neutrino species, the running of the electromagnetic coupling, and this one:

```text
check("Kibble: v2 point M = 100 Lambda_c, p = 1 reproduces 3e13 GeV",
      sig(100*(RHO_DM*M_PL**3/(100*S0))**0.25)==3e13)
```

It confirmed that the previous draft's formula, at the previous draft's normalization p = 1, gives the previous draft's own abundance-closure mass, 3×10¹³ GeV, which v3 then adopted as its benchmark (`review/v3-worklog.md`, F1). Whatever p should be, that check passes. Further down, the script defined the normalization of one [defect](/wiki/symmetry-breaking/topological-defects) per horizon volume as 45/(2π²·100) and checked "one defect per horizon volume: p ~ 0.023", which also passed, because the code computed what the formula said.

The round-3 referee recomputed it from independently chosen constants and found "p = 0.023 is the H^3 abundance with the 1.66 sqrt(g\*) factor dropped" (`review/round3/referee/audit-notes.md`, Step 4(a)). Ruling 1, upheld: "one defect per Hubble volume is p ≈ 104, not 0.023", with "v3's 0.0228 drops (1.66√g\*)³ ≈ 4.6×10³". The adjudicator's account: "My error came from misremembering the formula." See [Under review: the Kibble normalization](/wiki/dark-matter/candidates/soliton-candidate/kibble-normalization).

The script's freeze-out and ΔN_eff anchors were sound: the worklog records that the script "checks its freeze-out formula on a standard relic first: 100 GeV with σv = 2.2×10⁻²⁶ cm³/s gives Ω h² = 0.108" (`review/v3-worklog.md`, item O1). The circular one was the anchor for the normalization on which the manuscript's mass band rested. After the adjudication the script's docstring recorded the repair: "An earlier Kibble "anchor" that reproduced v2's own number was circular and has been replaced with independent ones." (knot_numbers.py at commit 96f58da).

## The anchors in the gate now

### The soliton-obituary script

`verify/soliton_obituary.py`: "Anchors come first and are independent of the manuscript (a textbook identity; a published value)."

```text
== Anchors
PASS  Friedmann: H = 1.66 sqrt(g*) T^2/M_Pl
PASS  one defect per Hubble volume gives n/s ~ 100 (T_c/M_Pl)^3 (Gangui, astro-ph/0110285)  [p = 104.31]
PASS  freeze-out: 100 GeV, sigma v = 2.2e-26 cm^3/s gives Omega h^2 ~ 0.12 (within x2)
PASS  Delta N_eff: one extra neutrino species at T_nu gives 1
```

The first two are lesson 2's replacements. The [Friedmann](/wiki/cosmology/scale-factor-duality/friedmann-cosmology) check is a textbook identity, √(8π³/90) to two decimals [T]; the Hubble-volume check holds the script's p inside a window of 50 to 200 around Gangui's published "~ 100". Both test the code from which the ruling-1 and ruling-2 numbers are built. The freeze-out anchor tests the relic function (window 0.06 to 0.24) and prints no value; the ΔN_eff anchor tests the dark-radiation function to 10⁻¹². The mass formula M\* and the gravitational-wave frequency formula have no separate anchor ([the soliton-obituary script](/wiki/method/verification/soliton-obituary-script#the-anchors)).

### The toy-model scripts

- **`verify/toy_coset.py`** opens with two textbook identities [T]: `H(Z) is symplectic and I = w^-1 H squares to -1` and `rho is symplectic and is the quarter turn: rho^2 = -1`, both exact in sympy.
- **`verify/toy_gw.py`** takes its inputs "from the sources, not from memory": the [matrix base](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/model-and-matrix-base) of de Goursac–Tanasa–Wallet ([arXiv:0709.3950](https://arxiv.org/abs/0709.3950), App. A) and the duality of [Grosse–Wulkenhaar](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar) ([hep-th/0402093](https://arxiv.org/abs/hep-th/0402093), eq. 1). Its docstring: "The explicit Laguerre form of f_mn used below is checked against the first two properties exactly (sympy), so it is not taken on trust." Its anchors print `f_00 = 2 exp(-x^2/theta) as in 0709.3950 (A.2)`, the two eigen-relations, orthogonality and normalization on a grid, and `anchor: D f_00 = f_00 (the normalization pi sqrt|det theta|)`, which checks the normalization of the duality transform before [the lemma](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/matrix-base-lemma) D f_mn = (−1)^m f_mn is tested. Its last check, for round-4 finding F6, tests a harmonic series against Euler's constant; flag 11 in `review/wiki-build-flags.md` notes that it checks only one harmonic series and does not settle whether [the tadpole](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/quantum-restoration#the-coefficient-ln-n-or-2-ln-n) grows as ln N or 2 ln N.
- **`verify/toy_s5.py`** checks textbook identities on its test state: `Fourier pair is consistent (Parseval)` and the two marginals of the [Wigner function](/wiki/phase-space/reciprocity/wigner-function) before it computes the interaction values, and ∫W² = 1/(2π) for a pure state in its last check.
- **`verify/toy_s4.py`** has no anchor section. It checks its Monte Carlo against the expectations for each phase: a Binder cumulant above 0.6 for an [ordered ℤ₂ phase](/wiki/symmetry-breaking/toy-models/coset-model/monte-carlo) (whose ideal value is 2/3), and 1/L scaling of the magnetization in the disordered control. It prints a spin-wave estimate beside the measured ratio for the symmetric model, without asserting agreement.

See [the toy-model scripts](/wiki/method/verification/toy-model-scripts).

### The four later scripts

Each docstring says "Anchors come first", independent of the document the script checks. The full lists are on the scripts' pages.

- **`verify/phase_space_diameter.py`** prints nine anchor checks first: CODATA 2018's Planck units, the Particle Data Group's photon and entropy densities and dark-energy scale, a Bose integral evaluated two ways and a published comoving horizon. The two published limits of [Lee et al. 2020](https://arxiv.org/abs/2002.11761), which the docstring also counts, sit in the last block, beside the bound they protect. Round-5 ruling R12 notes that they come from the column of the exclusion table the bound does not use: "Both columns come from the same table, so the anchor checks the transcription and the method" ([the anchors](/wiki/method/verification/phase-space-diameter-script#the-anchors)).
- **`verify/closed_universe.py`** prints 22: units and densities, the exact closed solutions its integrator must reproduce, the pendulum average, the spectrum of the three-sphere, a published mode of the dodecahedral space, published curvature values, Lee et al.'s ranges and a fit calibrated against two published results. Two literature anchors sit inside its section D, and section F has two winding-number anchors of its own ([the anchors](/wiki/method/verification/closed-universe-script#the-anchors)).
- **`verify/velocity_gated_gravity.py`** prints 14: CODATA 2018 constants, the Einstein–Infeld–Hoffmann and Darwin Lagrangians, textbook spin-2 numerators, [Planck 2018](https://arxiv.org/abs/1807.06209)'s age and matter–radiation equality, exact growing modes, the closed form of the gate's Fourier kernel, Lee et al.'s ranges, Mercury's perihelion advance and the Plummer sphere's free-fall time ([the anchors](/wiki/method/verification/velocity-gated-gravity-script#the-anchors)).
- **`verify/gate_mechanism.py`** prints 12: CODATA 2018 constants, the on-shell identity, the Fierz–Pauli numerator with its helicity sum, Legendre and Chebyshev identities and the zero-range s-wave ([the anchors](/wiki/method/verification/gate-mechanism-script#the-anchors)).

The last three docstrings call everything after the anchors a regression check, which reproduces the work's own numbers and is not independent of them.

### The battery

`verify/battery.py` has no anchors. Its tests are algebraic identities evaluated on random matrices, which do not depend on any figure in the papers, and exact integer arithmetic ([the verification battery](/wiki/method/verification/battery)).

### The literature-check script

`verify/literature_check.py` has no anchors in its sections A–F, which recompute no physics: they check the literature-check note against the record the check left, finding each quotation again in a stored abstract or excerpt and each citation in a metadata snapshot from INSPIRE, arXiv, Crossref or OpenAlex ([the literature-check script](/wiki/method/verification/literature-check-script)). Its section G, the algebra behind flag 66, is anchored in published equations, not in the program's results: Gasperini and Veneziano's [scale-factor duality](/wiki/cosmology/scale-factor-duality/cosmological-constraint#the-name-scale-factor-duality-t) with sources (2003, §2.2), the Friedmann equation of Einstein gravity with the inversions of the scale factor published for it, and a solution of Brans–Dicke gravity, a theory in which a scalar field sets the strength of gravity, by Mukherjee, Jassal and Lochan (2024, §6) ([section G](/wiki/method/verification/literature-check-script#section-g-the-algebra-behind-flag-66)).

### The dual-sector script

`verify/dual_sector.py` has no anchors either. Its sections A–E recompute no physics: they check the dual-sector note against its record, finding each quotation again in a repository document or a stored excerpt and each citation in a metadata snapshot from INSPIRE, arXiv or Crossref ([the dual-sector script](/wiki/method/verification/dual-sector-script)). Its section F takes its input from a published equation, the zero-mode commutators of [Minic 2020](https://arxiv.org/abs/2003.00318) (eq. 27), and checks that they form a non-degenerate 4 × 4 bracket per dimension, against 2 × 2 for (x, p) at ℏ.

## Reproductions are not anchors

The checks labelled "quoted:" in the toy scripts, and the "parity" checks of the battery, compare the output with the figures the documents print. The battery's docstring states their purpose: "a parity failure means this environment no longer reproduces the numbers the papers cite." Such checks show that the documents print what the code computes and that the environment still reproduces it. They are reproductions by design. The soliton-obituary script's ruling checks are of the same kind (for example `p = 104.31 with M_Pl`), and that is acceptable there because the anchors above them test the code from outside.

## How the rule has been applied since

- **Round 4.** The [pre-registration](/wiki/method/review/pre-registration#round-4) gave as a reason the verdict would not be C: "every number was computed by gated code with independent anchors". The one numerical indictment that survived was "the MC control values, a statistical problem" (MC is Monte Carlo); "Every normalization and sign I listed was confirmed" (`review/round4-adjudication.md`, 'Pre-registration scored'). An anchor tests a formula, not the statistics of a simulation, and the error-bar rule came out of that round ([the Monte Carlo error-bar rule](/wiki/method/verification/monte-carlo-error-bars)).
- **The wiki build.** The verifiers of the wiki's depth pass wrote executed checks for every suspected source error that rests on arithmetic, kept in `review/wiki-build-checks/`. Several test a document's statement against a textbook identity rather than against the document's own figures: `dirac_coupling_check.py` derives the [magnetic coupling](/wiki/electric-magnetic-duality/monopoles/dirac-quantization) from α = e²/4π and prints `4π/e² = 137.036   (= 1/alpha)` against #11 §11.2's "4π/e² ≈ 34" (flag 28), and `sqrt_eig_check.py` prints `Newton p4 identity: True` beside the trace it tests (flag 14). Others reproduce a note's figures from its own inputs, such as `stream_stability_check.py` for the [clumping shortfall](/wiki/dark-matter/momentum-clumping/instability-criterion) (flag 16). Since 2026-10-28 its arithmetic has been in the gate, as section D of `verify/velocity_gated_gravity.py`, whose docstring calls everything after its anchors a regression check: "it reproduces the investigation's own numbers and is not independent of them" ([the velocity-gated-gravity script](/wiki/method/verification/velocity-gated-gravity-script)); flag 16's addendum records the move, and the flag is pending. The README sets the condition for moving any of them into the gate: "A ruling that accepts a flag should move the relevant check into `verify/`, with an anchor independent of the paper."

## Sources

- Root `CLAUDE.md` 'Method' — the rule
- `review/round3-adjudication.md` 'Lessons (now in CLAUDE.md)' (lesson 2) and 'Rulings' (ruling 1) — the circular anchor, its replacement, the corrected normalization
- `review/round3/referee/audit-notes.md` Step 4(a) item 1 — how the dropped factor was found
- `review/v3-worklog.md` 'New open items (to compute before v3 states anything about them)' (O1, O2) — the predecessor's sound anchors; 'Findings neither referee raised' (F1) — the p = 1 closure at 3×10¹³ GeV and the move of the benchmark there
- `verify/soliton_obituary.py` — the current anchors
- `verify/toy_coset.py`, `verify/toy_gw.py`, `verify/toy_s5.py`, `verify/toy_s4.py` — the toy-model anchors, identity checks and phase expectations
- `verify/phase_space_diameter.py`, `verify/closed_universe.py`, `verify/velocity_gated_gravity.py`, `verify/gate_mechanism.py` — the later scripts' docstrings and anchor blocks; `review/round5-adjudication.md` 'Rulings' R12 — the column the table's anchor checks
- `verify/battery.py` — the parity checks, which are reproductions
- `verify/literature_check.py` — sections A–F, without anchors, check a note against its stored record; section G is anchored in published equations
- `verify/dual_sector.py` — sections A–E, without anchors, check a note against its stored record; section F's bracket is built from Minic 2020's commutators
- `review/round4-preregistration.md` 'Predictions' and `review/round4-adjudication.md` 'Pre-registration scored' — the rule in round 4
- `review/wiki-build-checks/README.md`, `dirac_coupling_check.out`, `sqrt_eig_check.out`; `review/wiki-build-flags.md` items 11, 14, 16, 28 — the wiki build's checks and the condition for promoting them
- Git history: knot_numbers.py at commits 5dbaa82 (the circular anchor) and 96f58da (the repaired docstring)
- `verify/velocity_gated_gravity.py` docstring and section D — the port of `stream_stability_check.py` into the gate, a regression check
- `review/wiki-build-flags.md` item 16 — the ✓ without a script, and its addendum of 2026-10-28
