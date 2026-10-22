---
title: "The Monte Carlo error-bar rule"
weight: 50
status: method
description: "Monte Carlo numbers need error bars from independent runs: a fixed seed makes a number reproducible, not accurate — round 4's second lesson, from a control value that was a single short-run fluctuation."
sources:
  - "CLAUDE.md 'Method'"
  - "review/round4-adjudication.md 'Lessons (into CLAUDE.md)'"
  - "review/round4-adjudication.md 'Rulings'"
  - "review/round4-adjudication.md 'Pre-registration scored'"
  - "review/round4-adjudication.md 'Revisions for v2 of the note (all accepted; applied 2026-10-20 in commit 6606734)'"
  - "review/round4/adjudicator/ctrl.out"
  - "review/round4/referee/audit-notes.md"
  - "review/round4-preregistration.md 'Predictions'"
  - "verify/toy_s4.py"
  - "papers/reciprocity-toy-models.md §4"
  - "notes/toy-lagrangian.md 'Chunk 3 results (2026-10-19): S4, quantum stability'"
  - "review/wiki-build-flags.md item 13"
---

*The Monte Carlo error-bar rule says that a number produced by a random simulation must come with an error bar estimated from several independent runs. A simulation started from a fixed random seed gives the same output every time it is run, which makes the number reproducible but says nothing about how far it lies from the average the simulation is estimating. Review round 4 found the case that prompted the rule: the high-temperature control values in the [toy-model note](/wiki/symmetry-breaking/toy-models) came from single fixed-seed runs without error bars, and the smallest lattice's value was a short-run fluctuation. The lattice script now reports means and standard errors over four independent seeds, and its checks use those error bars.*

**Status:** Method, in force (round-4 lesson 2, now in root `CLAUDE.md`) — untagged — applied in `verify/toy_s4.py`, the program's only Monte Carlo.

## The rule

Root `CLAUDE.md`, 'Method': "Monte Carlo numbers need error bars from independent runs. A fixed seed makes a number reproducible, not accurate." Round-4 lesson 2 is the same two sentences (`review/round4-adjudication.md`).

## The statistics [T]

This section is the wiki's reading of standard material [T].

A Monte Carlo simulation estimates an average, such as the mean magnetization of a lattice model, from a finite sequence of random configurations. The estimate differs from the true average by a random amount that shrinks as the run grows. A run from a fixed seed repeats exactly the same sequence, so rerunning it reproduces the same estimate and the same random error; it gives no measure of that error.

Runs started from different seeds are independent, and each gives an independent estimate of the same average. The spread of those estimates measures the random error, and the standard error of their mean is the sample standard deviation divided by the square root of the number of runs. In a Markov-chain simulation such as Metropolis, successive configurations within one run are correlated, so the configurations of one run cannot be treated as independent samples; separate runs avoid that problem. An error bar of this kind measures statistical error only. A systematic effect common to all runs, such as incomplete equilibration from the same starting state, is not in it.

## The episode: round 4

### The values as first written

The worklog's first lattice results for the [coset toy](/wiki/symmetry-breaking/toy-models/coset-model)'s [frozen-H reduction](/wiki/symmetry-breaking/toy-models/coset-model/frozen-h-reduction) gave the high-temperature control as "⟨|m|⟩ 0.078 → 0.033 → 0.014 — disordered" at L = 16, 32 and 64, and the run without the potential as "0.838 → 0.798 → 0.776 (ratio 0.925, spin-wave estimate 0.936)" ('Chunk 3 results'), from "fixed seeds" and without error bars. The first version of the note quoted them the same way ([Monte Carlo: an ordered ℤ₂ phase](/wiki/symmetry-breaking/toy-models/coset-model/monte-carlo#superseded-the-first-versions-control-values)).

### What the referee found

The round-4 referee wrote its own checkerboard Metropolis code with its own seeds and reported its values with error bars. For the control it found "0.0630+-0.0004 -> 0.0318+-0.0004 -> 0.0156+-0.0002", and noted that "the quoted sequence scales as L^-1.239 vs the 1/L expected and found (referee exponent -1.0069); quoted L=16 value is 1.238x the referee's (0.078 vs 0.0630+-0.0004). Minor: likely under-sampled; not reproduced to the stated precision." (`review/round4/referee/audit-notes.md`, capitals lowered). It also found that hot starts at L = 64 "did not equilibrate in 6000 sweeps", and that the manuscript did not state its start condition.

### The ruling

The adjudicator reran the control with the script's own run function (`review/round4/adjudicator/ctrl.py`) and printed:

```text
L=16 T=3 seed=116: <|m|> = 0.0777
L=16 T=3 seed=1: <|m|> = 0.0687
L=16 T=3 seed=2: <|m|> = 0.0639
L=16 T=3 seed=3: <|m|> = 0.0626
L=16 T=3 long run (40000 sweeps): <|m|> = 0.0653
L=32 T=3 long run: <|m|> = 0.0325
L=64 T=3 long run: <|m|> = 0.0164
```

The ruling headed "MC control" (the Monte Carlo control run), upheld: "`ctrl.py`: my L = 16 value from seed 116 was a short-run fluctuation. Other seeds give 0.063–0.069, and long runs give 0.0653 / 0.0325 / 0.0164, clean 1/L. **Fixed seeds gave reproducibility, not accuracy; the numbers lacked error bars.** The ordered-phase values (0.954) and the h = 0 decay agree with the referee to about 1%." The ruling headed "MC start", accepted: "Cold starts are standard for ordered-phase measurements, but they must be stated." (`review/round4-adjudication.md`; [Review round 4](/wiki/method/review/round-4)).

The four single-seed values at L = 16 show the point of the rule directly: the seed that had been quoted gave the largest of them, and nothing in a single run could have shown that.

### How the pre-registration scored it

The pre-registration had predicted "at most one surviving numerical indictment", likeliest in "a normalization or convention", and had given as a reason against verdict C that "every number was computed by gated code with independent anchors". The outcome: "One: the MC control values, a statistical problem. Every normalization and sign I listed was confirmed", scored "**Hit on count, miss on location**". The prediction had looked for errors of the kind anchors catch; the surviving one was of a kind they do not ([independent anchors](/wiki/method/verification/independent-anchors); [Pre-registration and its calibration record](/wiki/method/review/pre-registration)).

## The practice now

Revision 1 of the note asked for "start conditions, equilibration checks, and error bars from independent seeds; rerun the control". The note v2, §4: "Checkerboard Metropolis, cold start (φ = 0), L = 16, 32, 64. Means ± standard errors over four independent seeds."

`verify/toy_s4.py` implements it. Its docstring: "All runs use a cold start (phi = 0). Error bars: standard error over 4 independent seeds." Each of the four runs discards 1500 sweeps and measures over 4000, and the standard error is the sample standard deviation over √4. Two of its checks use the error bars as the measure of agreement:

- model A, with the potential: `size-independent within errors (|m64 - m16| < 3 sigma + 0.002)`, with σ the two error bars combined;
- model B, without it: `no true order: the U(1) magnetization falls with size by more than 3 sigma`.

Its docstring also says "Fixed seeds, so the run is deterministic." The four seeds are themselves fixed, so the gate reproduces the error bars along with the means. The rule asks for independence between the runs, not for unrepeatable runs, and the two properties coexist. The "quoted:" checks then compare the printed means and errors with the note's table, which makes them reproductions ([the toy-model scripts](/wiki/method/verification/toy-model-scripts)).

The values as the gate prints them, in the run of 2026-10-21:

```text
== Model A: with the rho-preserving potential (h = 1), T = 0.6
      L= 16: <|m|> = 0.9543 +- 0.0001, Binder = 0.6666
      L= 32: <|m|> = 0.9542 +- 0.0001, Binder = 0.6667
      L= 64: <|m|> = 0.9542 +- 0.0000, Binder = 0.6667
PASS  size-independent within errors (|m64 - m16| < 3 sigma + 0.002)  [diff -0.0001, sigma 0.0001]

== Control: model A at high temperature, T = 3.0
      L= 16: <|m|> = 0.0653 +- 0.0043
      L= 32: <|m|> = 0.0338 +- 0.0013
      L= 64: <|m|> = 0.0155 +- 0.0004
PASS  disordered: <|m|> scales as 1/L (m16/m64 within [3.3, 4.8], expected 4)  [4.209]

== Model B: exactly symmetric (h = 0), T = 0.6
      L= 16: <|M|> = 0.8369 +- 0.0007
      L= 32: <|M|> = 0.8025 +- 0.0039
      L= 64: <|M|> = 0.7736 +- 0.0038
PASS  no true order: the U(1) magnetization falls with size by more than 3 sigma  [ratio 0.9243; spin-wave estimate 0.9360]
```

## Which values to cite

Four sets of control values exist: the worklog's fixed-seed "0.078 → 0.033 → 0.014", the referee's, the adjudicator's long runs (0.0653 / 0.0325 / 0.0164), and the note v2's four-seed means (0.0653 ± 0.0043, 0.0338 ± 0.0013, 0.0155 ± 0.0004). The note v2 governs, and its values are the ones the gate reproduces. The adjudicator's long runs differ from them at L = 32 and 64; the sources do not reconcile the two sets. The note's "⟨|m|⟩ = 0.954 ± 0.0001 at every size" is printed by the script as `+- 0.0000` at L = 64; flag 13 in `review/wiki-build-flags.md` reads the note's figure as a conservative bound rather than the printed value.

## What the error bars do not cover

- **Systematic effects.** Every run starts cold, so incomplete equilibration from that start would be common to all four seeds and absent from the error bar. The guard is the control, in the worklog's words: "The ordered start is a choice; the high-T control shows the sampler does leave it when the phase is disordered". The note adds that hot-start runs at L = 64 "coarsen slowly through metastable domains" (§4).
- **The model.** The error bars measure the simulation of the frozen-H reduction. The Monte Carlo of model I with H dynamical has not been done ([the reduced-model stability rule](/wiki/method/verification/reduced-model-stability)).

## Applied since

The rule has had one application, the rerun of `verify/toy_s4.py` for the note v2. The program has run no other Monte Carlo since. None of the wiki build's executed checks in `review/wiki-build-checks/` is a simulation; its one Monte Carlo item, flag 13, compares the note's quoted error bar with the script's printed output.

## Sources

- Root `CLAUDE.md` 'Method' — the rule
- `review/round4-adjudication.md` 'Lessons (into CLAUDE.md)' (lesson 2), 'Rulings' (MC control, MC start), 'Pre-registration scored', 'Revisions for v2 of the note' (revision 1) — the case, its scoring, the rerun asked for
- `review/round4/adjudicator/ctrl.out` — the four single-seed values and the long runs
- `review/round4/referee/audit-notes.md` — the referee's independent simulation, its error bars, the hot-start trapping
- `review/round4-preregistration.md` 'Predictions' — the expected indictment
- `verify/toy_s4.py` — cold starts, four seeds, standard errors, the checks that use them
- `papers/reciprocity-toy-models.md` §4 — the method and the table as now stated
- `notes/toy-lagrangian.md` 'Chunk 3 results (2026-10-19): S4, quantum stability' — the superseded single-seed values
- `review/wiki-build-flags.md` item 13 — the quoted error bar at L = 64
