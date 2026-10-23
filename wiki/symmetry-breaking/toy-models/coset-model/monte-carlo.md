---
title: "Monte Carlo: an ordered ℤ₂ phase"
weight: 70
status: alive
description: "Checkerboard Metropolis of the frozen-H lattice model at L = 16, 32, 64 over four independent seeds: ⟨|m|⟩ = 0.954 with the potential, 1/L decay in the T = 3 control, slow spin-wave decay without the potential; hot-start trapping, the referee's independent run, and the superseded first-version control values."
provenance: [V]
sources:
  - "papers/reciprocity-toy-models.md §4"
  - "papers/reciprocity-toy-models.md ref [17]"
  - "papers/reciprocity-toy-models.md v1 (commit d9a06ac) §4"
  - "verify/toy_s4.py"
  - "review/round4-adjudication.md 'Rulings' (MC control, MC start)"
  - "review/round4-adjudication.md 'Pre-registration scored'"
  - "review/round4-adjudication.md 'Lessons'"
  - "review/round4-adjudication.md 'Revisions' 1"
  - "review/round4/adjudicator/ctrl.out"
  - "review/round4/adjudicator/ctrl.py"
  - "review/round4/referee/audit-notes.md Step 1"
  - "review/round4/referee/audit-notes.md Step 2(c)"
  - "review/round4/referee/out_xy_mc.txt"
  - "review/round4/referee/out_xy_trap.txt"
  - "review/round4/referee/out_sec4_extra.txt"
  - "review/round4/referee/ref_xy_mc.py"
  - "review/round4-preregistration.md 'Predictions'"
  - "notes/toy-lagrangian.md 'Chunk 3 results'"
  - "CLAUDE.md 'Method'"
---

*The Monte Carlo is a lattice simulation of the [frozen-H reduction](/wiki/symmetry-breaking/toy-models/coset-model/frozen-h-reduction) of model I: a square grid of angles φ, one per site, with an energy that is lowest when neighbouring angles agree and, when the [ρ-preserving potential](/wiki/symmetry-breaking/rho-preserving-potential) is switched on, lowest at the two angles 0 and π. Random local changes are accepted or rejected by the Metropolis rule at a fixed temperature, and the lattice average m of cos φ, which changes sign under ρ, shows whether one of the two vacua has been singled out. With the potential the mean of |m| stays at 0.954 on every lattice size, an ordered ℤ₂ phase. Without it the order decays slowly with size, as a continuous symmetry in two dimensions requires, and at high temperature it falls as the inverse of the lattice size. This is [criterion S4](/wiki/symmetry-breaking/toy-models/success-criteria) for the reduction, with error bars from four independent seeds, adopted after round 4 found the first control numbers under-sampled.*

**Status:** Alive, for the frozen-H reduction only — [V] (the worklog records "S4 passes only with the τ-type potential [V]", the [naive form](/wiki/symmetry-breaking/toy-models/coset-model/naive-potential), which at H = 1 gives the same lattice energy; `verify/toy_s4.py`, gated; [the toy-model scripts](/wiki/method/verification/toy-model-scripts)) — the ordered-phase values and the potential-free decay agree with the round-4 referee "to about 1%"; the control values were corrected in version 2 ([review round 4](/wiki/method/review/round-4)).

## The lattice model

The simulated energy is model I's polarization angle at H = 1 on a square lattice (toy-model note §4):

```text
E = −J Σ⟨ij⟩ cos(φ_i − φ_j) − h Σ_i cos 2φ_i
```

The first sum runs over neighbouring sites and is the lattice form of the angle's stiffness; the second is [the bounded potential V_b](/wiki/symmetry-breaking/toy-models/coset-model/bounded-potential) at H = 1, "up to a constant and normalization" (§4). The lattice has L × L sites with periodic boundaries: the neighbour shifts in `verify/toy_s4.py` wrap around the edges. The runs use J = 1, h = 1 with the potential and h = 0 without it, temperature T = 0.6, a control at T = 3.0, and L = 16, 32 and 64. The lattice coupling J is unrelated to the J of [#11](/wiki/history/documents/checkpoint)'s postulate [P2′](/wiki/program/postulates/p2-prime).

[Born reciprocity](/wiki/phase-space/reciprocity/born-reciprocity) acts on the lattice as φ → φ + π at every site. The order parameter is "m = ⟨cos φ⟩" (§4), the lattice average of cos φ in one configuration. Since cos φ is the entry K₁₁ of K(φ), m is the lattice average of model I's [order parameter](/wiki/symmetry-breaking/order-parameter) O = K₁₁, and it changes sign under ρ ([model I vacua](/wiki/symmetry-breaking/toy-models/coset-model/vacua)). The script records |m| and averages it over the run, ⟨|m|⟩, because in a finite lattice the sign of m can flip over a long run, which would average m itself to zero [T]. Without the potential the symmetry is the whole circle of shifts, and the script uses "the U(1) magnetization |mean exp(i phi)|" (`verify/toy_s4.py`), written ⟨|M|⟩ = |⟨e^{iφ}⟩| in the note.

## The algorithm

The Metropolis algorithm samples configurations with the Boltzmann weight e^{−E/T} [T] (Metropolis et al. 1953†). Each step proposes a random change; a change that lowers the energy is accepted, and one that raises it by ΔE is accepted with probability e^{−ΔE/T}. In `verify/toy_s4.py` each proposal shifts an angle by an amount drawn uniformly between −1 and 1. "Checkerboard" means the sites are split into two interleaved sublattices like the squares of a chessboard; every neighbour of a site lies on the other sublattice, so a whole sublattice can be updated at once [T]. One sweep updates both.

Version 2: "Checkerboard Metropolis, cold start (φ = 0), L = 16, 32, 64. Means ± standard errors over four independent seeds." (§4). In the script each run discards 1,500 sweeps for equilibration and then measures over 4,000 (its defaults "therm=1500, sweeps=4000"). Each quoted value is the mean of four runs with different random seeds, and its error bar is the standard error of that mean: the spread of the four results divided by √4. The seeds are fixed, so the whole computation, error bars included, is reproducible: "Fixed seeds, so the run is deterministic." (docstring; [the Monte Carlo error-bar rule](/wiki/method/verification/monte-carlo-error-bars)).

### What the diagnostics show [T]

- **Size dependence of ⟨|m|⟩.** In an ordered phase ⟨|m|⟩ approaches a nonzero constant as L grows. In a disordered phase m averages L² nearly independent angles, so its typical size falls as 1/√(L²) = 1/L.
- **The Binder cumulant.** The script computes U = 1 − ⟨m⁴⟩/(3⟨m²⟩²). If m takes only two opposite values ±m₀, then ⟨m⁴⟩ = ⟨m²⟩² and U = 2/3. If m is spread as a Gaussian about zero, as in a disordered phase, then ⟨m⁴⟩ = 3⟨m²⟩² and U = 0. The script's check reads a value "near 2/3" as "an ordered Z2 phase".
- **Spin waves without the potential.** In two dimensions the XY model at low temperature has no true long-range order, but its order decays only as a power of distance. In the Gaussian, or spin-wave, approximation the magnetization of an L × L lattice falls as L^{−T/4πJ}. Between L = 16 and L = 64 that predicts the ratio (64/16)^{−T/4πJ}, which the note evaluates as 0.936 at T = 0.6 and J = 1. The script computes the same estimate from η = T/2π at J = 1, the power with which correlations decay with distance.

## Results

Version 2's table (§4), reproduced by [the gate](/wiki/method/verification/the-gate):

| Run | Values at L = 16, 32, 64 | Reading |
|---|---|---|
| With the potential (J = h = 1), T = 0.6 | ⟨\|m\|⟩ = 0.954 ± 0.0001 at every size; Binder cumulant 0.667 | Ordered ℤ₂ phase |
| Control, T = 3.0 | ⟨\|m\|⟩ = 0.0653 ± 0.0043, 0.0338 ± 0.0013, 0.0155 ± 0.0004 | Scales as 1/L: disordered |
| No potential (h = 0), T = 0.6 | ⟨\|M\|⟩ = \|⟨e^{iφ}⟩\| = 0.8369 ± 0.0007, 0.8025 ± 0.0039, 0.7736 ± 0.0038; ratio 0.924 vs spin-wave (64/16)^{−T/4πJ} = 0.936 | No true order |

### With the potential: an ordered ℤ₂ phase

The gate prints ⟨|m|⟩ = 0.9543 ± 0.0001, 0.9542 ± 0.0001 and 0.9542 ± 0.0000, with Binder cumulants 0.6666, 0.6667 and 0.6667, at L = 16, 32 and 64 (`verify/toy_s4.py`). The note's "± 0.0001 at every size" is an upper bound at L = 64, where the printed error rounds to 0.0000 (flag 13 in `review/wiki-build-flags.md`); the gate accepts any standard error below 0.0002 for this row. The script passes four checks on this row: "ordered: <|m|> > 0.8 at every size"; "size-independent within errors (|m64 - m16| < 3 sigma + 0.002)", with the difference printed as −0.0001 and sigma as 0.0001; "Binder cumulant near 2/3 (an ordered Z2 phase)"; and the quoted values.

⟨|m|⟩ does not fall as the lattice grows fourfold, and the Binder cumulant sits at its ordered value: the shift by π is [spontaneously broken](/wiki/symmetry-breaking/spontaneous-symmetry-breaking), and the lattice stays near one of the two angles 0 and π instead of visiting both. Version 2 states the limit of the claim: "We call the first row an ordered ℤ₂ phase. We did not measure critical exponents. Symmetry-breaking fields in the planar model are treated generally in [17]; the ordered phase at these parameters is established by the simulation itself." (§4).

Reference [17] is J. V. José, L. P. Kadanoff, S. Kirkpatrick and D. R. Nelson, Phys. Rev. B 16, 1217 (1977), which version 2 keeps as "Background on symmetry-breaking fields in the planar model; the ordered phase used here is established by our own Monte Carlo, not by appeal to this reference." The first version had cited it, as [12], for "the two-fold anisotropic planar model, whose ordered phase is Ising-like" (v1 §4). The [pre-registration](/wiki/method/review/pre-registration) named it the likeliest reference "cited for more than it says" (`review/round4-preregistration.md`). The referee found that its abstract treats "hexagonal and cubic crystalline fields; no mention of the two-fold/Ising case", and with the full text paywalled the specific claim could not be checked (`review/round4/referee/audit-notes.md`, Step 1). The adjudication recorded "[12]'s specific claim is unverifiable".

### The control at T = 3: the sampler leaves the ordered start

Every run starts from the ordered configuration φ = 0. At T = 3.0 the values fall with size: the gate passes "disordered: <|m|> scales as 1/L (m16/m64 within [3.3, 4.8], expected 4)" with the ratio 4.209. A disordered phase gives 1/L, so the sampler does leave its ordered start when the temperature puts the system in a disordered state. The worklog: "The ordered start is a choice; the high-T control shows the sampler does leave it when the phase is disordered." ('Chunk 3 results'); the script's comment on its start reads "ordered start; equilibration tested by the high-T control".

### Without the potential: no true order

With h = 0 the magnetization falls with size, slowly: the gate passes "no true order: the U(1) magnetization falls with size by more than 3 sigma", printing the ratio 0.9243 against the spin-wave estimate 0.9360. This is the lattice form of [the Mermin–Wagner–Coleman theorem](/wiki/symmetry-breaking/mermin-wagner-coleman): a continuous compact symmetry in two dimensions does not order.

The referee checked the spin-wave formula on the lattice: "lattice Gaussian sum gives M(64)/M(16) = 0.9359 vs closed form (64/16)^(-T/4piJ) = 0.9360" (Step 2(c); `review/round4/referee/out_sec4_extra.txt`). The data fall below the estimate, which the referee read "as expected from stiffness renormalisation (referee fitted exponent -0.0628 vs bare -0.0477)". At nonzero temperature, fluctuations beyond the Gaussian approximation soften the effective stiffness, so the order decays faster than the bare spin-wave exponent says [T].

## Start conditions: hot starts trap

A hot start begins from random angles. The referee ran both starts. At L = 16 and 32 they agree: 0.9541 from both at L = 16, and 0.9542 (hot) against 0.9543 (cold) at L = 32, with Binder cumulants 0.6666 and 0.6667 (`review/round4/referee/out_xy_mc.txt`). At L = 64 the hot start "did not equilibrate in 6000 sweeps: <|m|> = 0.0593 (U=0.536)" (Step 2(c)). Diagnostic runs at L = 64 (`review/round4/referee/out_xy_trap.txt`):

| Start | Seed | Energy per site | ⟨\|m\|⟩ |
|---|---|---|---|
| hot | 1064 | −2.58524 | 0.0265 |
| hot | 77 | −2.61222 | 0.6052 |
| cold | 1065 | −2.67587 | 0.9541 |

The cold start ends at the lowest energy. The referee's reading: "Metastable domain stripes with higher energy; equilibrium is ordered." A random start in an ordered phase breaks up into domains of both signs, with angles near 0 in some and near π in others, separated by walls that cost energy [T]. The walls move slowly, and on a periodic lattice a wall that wraps all the way around the system can persist for a long time [T].

The referee also cautioned: "Manuscript does not state its start condition; results from a cold start alone would be partly by construction." The ruling on start conditions, "Hot starts at L = 64 trap in metastable domains; start conditions not stated", was accepted: "Cold starts are standard for ordered-phase measurements, but they must be stated." (`review/round4-adjudication.md`, 'Rulings', the row "MC start", MC standing for Monte Carlo). Version 2 states them: "Hot starts at L = 64 coarsen slowly through metastable domains, so ordered-phase values are reported from cold starts." (§4); the script's docstring: "All runs use a cold start (phi = 0)."

## The referee's independent simulation

The round-4 referee wrote its own checkerboard Metropolis, with its own seeds, longer runs and error bars from binning a single run (`review/round4/referee/ref_xy_mc.py`), and compared it with the first version of the note (Step 2(c)):

| Run | First version | Referee |
|---|---|---|
| h = 1, T = 0.6, ⟨\|m\|⟩ at L = 16 / 32 / 64 | 0.954 at all sizes; Binder 0.667 | cold: 0.9541 / 0.9543 / 0.9542; Binder 0.6666 / 0.6667 / 0.6667 |
| control, T = 3.0 | 0.078 → 0.033 → 0.014 | 0.0630 ± 0.0004 → 0.0318 ± 0.0004 → 0.0156 ± 0.0002 |
| h = 0, T = 0.6, ⟨\|M\|⟩ | 0.838 → 0.798 → 0.776, ratio 0.925 | 0.8371 → 0.8040 → 0.7673, ratio 0.9166 |

The adjudication: "The ordered-phase values (0.954) and the h = 0 decay agree with the referee to about 1%." ('Rulings', "MC control"). For h = 0 the referee noted: "Values agree at L=16; L=32/64 differ by ~0.006-0.009 (3-4 binned sigma, binned errors likely underestimated for Metropolis autocorrelation at L=64)." Successive Metropolis sweeps are correlated, so error bars computed from blocks of one run come out too small when the blocks are short compared with the correlation time [T]; independent runs avoid that. The values this wiki cites for h = 0 are version 2's four-seed ones in the table above.

## Superseded: the first version's control values

The first version (v1 §4, commit d9a06ac) and the worklog quoted the high-temperature control as "0.078 → 0.033 → 0.014", from fixed seeds and without error bars, and the run without the potential as "0.838 → 0.798 → 0.776, ratio 0.925" ('Chunk 3 results').

The referee confirmed the qualitative reading (disordered), but not the numbers: "the quoted sequence scales as L^-1.239 vs the 1/L expected and found (referee exponent -1.0069); quoted L=16 value is 1.238x the referee's (0.078 vs 0.0630+-0.0004). Minor: likely under-sampled" (Step 2(c)). The adjudicator reran the control with the script's own run function (`review/round4/adjudicator/ctrl.py`). At L = 16 and T = 3, seed 116 gave 0.0777, seeds 1, 2 and 3 gave 0.0687, 0.0639 and 0.0626, and a long run of 40,000 sweeps gave 0.0653; long runs at L = 32 and 64 gave 0.0325 and 0.0164 (`review/round4/adjudicator/ctrl.out`). The ruling, upheld:

> `ctrl.py`: my L = 16 value from seed 116 was a short-run fluctuation. Other seeds give 0.063–0.069, and long runs give 0.0653 / 0.0325 / 0.0164, clean 1/L. **Fixed seeds gave reproducibility, not accuracy; the numbers lacked error bars.**

The current values are version 2's four-seed means, 0.0653 ± 0.0043, 0.0338 ± 0.0013 and 0.0155 ± 0.0004, which the gate reproduces. The adjudicator's long runs differ from them at L = 32 and L = 64 (0.0325 against 0.0338, and 0.0164 against 0.0155); the sources do not reconcile the two sets, and this wiki cites version 2's ([conflicts between sources](/wiki/history/documents/source-conflicts#postulates-and-the-toy-models)). The values without the potential changed too: version 2's 0.8369, 0.8025, 0.7736 and ratio 0.924 replace the first version's. That first-version ratio appears as 0.925 (v1 and the worklog), 0.926 (the referee's notes) and 0.9260 (`out_sec4_extra.txt`); the last two were recomputed from the rounded values.

The pre-registration had predicted "at most one surviving numerical indictment", likeliest in "a normalization or convention: the spin-wave exponent, the 8π(m+n+1) coefficient, or the Δ sign convention". The outcome was scored "Hit on count, miss on location": "One: the MC control values, a statistical problem. Every normalization and sign I listed was confirmed" ('Pre-registration scored'). Revision 1 asked for "start conditions, equilibration checks, and error bars from independent seeds; rerun the control", and round-4 lesson 2 became a rule in the root `CLAUDE.md`: "Monte Carlo numbers need error bars from independent runs. A fixed seed makes a number reproducible, not accurate." ([the Monte Carlo error-bar rule](/wiki/method/verification/monte-carlo-error-bars)). The replacement is listed among the [superseded statements](/wiki/status/superseded).

## Scope

The simulation is of the reduction only: "H is not simulated" (§4). The worklog's run used the same lattice energy under the name "τ-type potential", the [naive form](/wiki/symmetry-breaking/toy-models/coset-model/naive-potential). At H = 1 the naive form and V_b differ only by an overall factor, and on the lattice either becomes −h cos 2φ up to a constant, so the lattice results stand for both; the naive form fails only once H is dynamical. A Monte Carlo of model I with H dynamical is open ([Open: a Monte Carlo with H dynamical](/wiki/symmetry-breaking/toy-models/coset-model/dynamical-h-monte-carlo)), and so is whether the coupled model orders ρ's SO(2) without a potential ([Open: does ρ's SO(2) break in the coupled model?](/wiki/symmetry-breaking/toy-models/coset-model/so2-question)). The result counts toward [acceptance criterion 1](/wiki/symmetry-breaking/toy-models/acceptance-criterion) as "an ordered ℤ₂ phase in 1+1 in the frozen-H reduction (Monte Carlo)" (#11 §14 item 11).

## Sources

- `papers/reciprocity-toy-models.md` §4, ref [17] — the method, the three runs and their readings, the start conditions, quoted above
- `papers/reciprocity-toy-models.md` v1 (commit d9a06ac) §4 — the first-version values and the Ising-like citation
- `verify/toy_s4.py` — the gated simulation, its parameters and checks, which reproduce every quoted value
- `review/round4-adjudication.md` 'Rulings' (MC control, MC start), 'Pre-registration scored', 'Revisions' 1, 'Lessons' — the rulings on the control values and on the start conditions; the scoring; the error-bar lesson
- `review/round4/adjudicator/ctrl.py`, `review/round4/adjudicator/ctrl.out` — the seed-116 value and the long runs
- `review/round4/referee/audit-notes.md` Step 1, Step 2(c) — the citation check of [17]; the referee's independent simulation, the hot-start trapping and the spin-wave check
- `review/round4/referee/out_xy_mc.txt`, `review/round4/referee/out_xy_trap.txt`, `review/round4/referee/out_sec4_extra.txt`, `review/round4/referee/ref_xy_mc.py` — the referee's runs, trap diagnostics, spin-wave sums and code
- `review/round4-preregistration.md` 'Predictions' — the predicted numerical indictment and the citation flag
- `notes/toy-lagrangian.md` 'Chunk 3 results' — the first-version values, now superseded, and the role of the control
- `CLAUDE.md` 'Method' — the error-bar rule
