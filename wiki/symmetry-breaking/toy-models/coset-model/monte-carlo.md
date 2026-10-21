---
title: "Monte Carlo: an ordered ℤ₂ phase"
weight: 70
status: alive
description: "Checkerboard Metropolis at L = 16, 32, 64 over four seeds: ⟨|m|⟩ = 0.954 with the potential, slow 2D decay without it, a 1/L control at T = 3, and hot-start trapping."
provenance: [V]
sources:
  - "papers/reciprocity-toy-models.md §4"
  - "verify/toy_s4.py"
  - "review/round4-adjudication.md 'Rulings'"
  - "review/round4/adjudicator/ctrl.out"
  - "review/round4/referee/audit-notes.md Step 2(c)"
  - "notes/toy-lagrangian.md 'Chunk 3 results'"
  - "CLAUDE.md 'Method'"
---

*The Monte Carlo is a lattice simulation of the [frozen-H reduction](/wiki/symmetry-breaking/toy-models/coset-model/frozen-h-reduction) of model I: a square grid of angles φ, one per site, with an energy that is lowest when neighbouring angles agree and, when the ρ-preserving potential is switched on, lowest at the two angles 0 and π. Random local updates are accepted or rejected by the Metropolis rule at a fixed temperature, and the lattice average m of cos φ, which changes sign under ρ, shows whether one of the two vacua has been singled out. With the potential the mean of |m| stays at 0.954 on every lattice size, an ordered ℤ₂ phase; without it the order decays slowly with size, as a continuous symmetry in two dimensions requires. This is criterion S4 for the reduction, with error bars from four independent seeds, adopted after round 4 found the first control numbers under-sampled.*

**Status:** Alive, for the frozen-H reduction only — [V] (`verify/toy_s4.py`, gated; [the toy-model scripts](/wiki/method/verification/toy-model-scripts)) — the ordered-phase values and the potential-free decay agree with the round-4 referee "to about 1%"; the control values were corrected in version 2 ([review round 4](/wiki/method/review/round-4)).

## Key facts

- **Method.** "Checkerboard Metropolis, cold start (φ = 0), L = 16, 32, 64. Means ± standard errors over four independent seeds. Order parameter for ρ: m = ⟨cos φ⟩." The lattice energy is E = −J Σ cos(φ_i − φ_j) − h Σ cos 2φ_i, where J is the lattice coupling, unrelated to the J of #11's P2′.
- **With the potential** (J = h = 1, T = 0.6): ⟨|m|⟩ = 0.954 ± 0.0001 at every size; Binder cumulant 0.667. Reading: "Ordered ℤ₂ phase". "We did not measure critical exponents."
- **Control** (T = 3.0): ⟨|m|⟩ = 0.0653 ± 0.0043, 0.0338 ± 0.0013, 0.0155 ± 0.0004. Reading: "Scales as 1/L: disordered".
- **No potential** (h = 0, T = 0.6): ⟨|M|⟩ = |⟨e^{iφ}⟩| = 0.8369 ± 0.0007, 0.8025 ± 0.0039, 0.7736 ± 0.0038; ratio 0.924 vs spin-wave (64/16)^{−T/4πJ} = 0.936. Reading: "No true order", as [the Mermin–Wagner–Coleman theorem](/wiki/symmetry-breaking/mermin-wagner-coleman) requires of the continuous symmetry. The referee confirmed the spin-wave formula with a lattice Gaussian sum and found the data below it, "as expected from stiffness renormalisation".
- **The control: the one surviving numerical indictment.** The first version quoted 0.078 → 0.033 → 0.014 from fixed-seed runs. The adjudicator: "my L = 16 value from seed 116 was a short-run fluctuation", and "Fixed seeds gave reproducibility, not accuracy; the numbers lacked error bars." The adjudicator's long runs gave 0.0653 / 0.0325 / 0.0164 (`review/round4/adjudicator/ctrl.out`); the four-seed values above, from version 2 and the gate, are the ones cited. The lesson is now a rule ([the Monte Carlo error-bar rule](/wiki/method/verification/monte-carlo-error-bars)).
- **Hot starts trap.** At L = 64 a hot start "did not equilibrate in 6000 sweeps" (⟨|m|⟩ = 0.0593), held in "metastable domain stripes with higher energy; equilibrium is ordered" (referee). Version 2 reports ordered-phase values from cold starts and says so; the adjudication: "Cold starts are standard for ordered-phase measurements, but they must be stated."
- **Scope.** "H is not simulated"; the lattice energy is the [bounded potential V_b](/wiki/symmetry-breaking/toy-models/coset-model/bounded-potential) at H = 1, "up to a constant and normalization". The worklog's run used the same lattice energy under the name "τ-type potential", the [naive form](/wiki/symmetry-breaking/toy-models/coset-model/naive-potential); the two differ only once H is dynamical, where the naive form is unbounded. A simulation of model I with H dynamical is open ([acceptance criterion 1](/wiki/symmetry-breaking/toy-models/acceptance-criterion)).

## Sources

- `papers/reciprocity-toy-models.md` §4 — the method and the three runs, quoted above
- `verify/toy_s4.py` — the gated simulation, which reproduces every quoted value
- `review/round4-adjudication.md` 'Rulings' — the rulings on the Monte Carlo control values and on the start conditions
- `review/round4/adjudicator/ctrl.out` — the seed-116 value and the long runs
- `review/round4/referee/audit-notes.md` Step 2(c) — the referee's independent simulation, the hot-start trapping and the spin-wave check
- `notes/toy-lagrangian.md` 'Chunk 3 results' — the first-version values, now superseded
- `CLAUDE.md` 'Method' — the error-bar rule
