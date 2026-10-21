---
title: "The Monte Carlo error-bar rule"
weight: 50
status: method
description: "Monte Carlo numbers need error bars from independent runs: a fixed seed makes a number reproducible, not accurate — round 4's second lesson."
sources:
  - "CLAUDE.md 'Method'"
  - "review/round4-adjudication.md 'Lessons (into CLAUDE.md)'"
  - "review/round4-adjudication.md 'Rulings'"
  - "verify/toy_s4.py"
  - "papers/reciprocity-toy-models.md §4"
  - "notes/toy-lagrangian.md 'Chunk 3 results (2026-10-19): S4, quantum stability'"
---

*The Monte Carlo error-bar rule says that a number produced by a random simulation must come with an error bar estimated from several independent runs. A simulation started from a fixed random seed gives the same output every time it is run, which makes the number reproducible but says nothing about how far it might lie from the true average. Review round 4 found the case that prompted the rule: control values in the toy-model note came from fixed seeds without error bars, and one of them was a short-run fluctuation. The lattice script now reports means and standard errors over four independent seeds.*

**Status:** Method, in force (a round-4 lesson, now in root `CLAUDE.md`) — untagged — applied in `verify/toy_s4.py`.

## Key facts

- **The rule.** "Monte Carlo numbers need error bars from independent runs. A fixed seed makes a number reproducible, not accurate." (root `CLAUDE.md`; round-4 lesson 2 in the same words).
- **The statistics [T].** Independent runs, each started from a different seed, give independent estimates of the same average; the spread of those estimates measures the random error, and the standard error of their mean is the sample standard deviation divided by the square root of the number of runs. A single seeded run, however long, gives no such measure.
- **The case.** The ruling headed "MC control" (the Monte Carlo control run): "Quoted 0.078 / 0.033 / 0.014 at T = 3 do not match the referee's 0.0630 / 0.0318 / 0.0156" — upheld: "`ctrl.py`: my L = 16 value from seed 116 was a short-run fluctuation. Other seeds give 0.063–0.069, and long runs give 0.0653 / 0.0325 / 0.0164, clean 1/L. Fixed seeds gave reproducibility, not accuracy; the numbers lacked error bars." The ordered-phase values (0.954) and the h = 0 decay agreed with the referee "to about 1%". (`review/round4-adjudication.md`; [Review round 4](/wiki/method/review/round-4)).
- **Start conditions too.** The ruling headed "MC start" (Monte Carlo start conditions): "Hot starts at L = 64 trap in metastable domains; start conditions not stated" — accepted: "Cold starts are standard for ordered-phase measurements, but they must be stated."
- **The practice now.** `verify/toy_s4.py`: "All runs use a cold start (phi = 0). Error bars: standard error over 4 independent seeds." Its docstring also says "Fixed seeds, so the run is deterministic": the four seeds are fixed, so the error bars are themselves reproducible. The note v2: "Checkerboard Metropolis, cold start (φ = 0), L = 16, 32, 64. Means ± standard errors over four independent seeds." See [The toy-model scripts](/wiki/method/verification/toy-model-scripts).
- **The values now gated.** Control at T = 3.0: ⟨|m|⟩ = 0.0653 ± 0.0043, 0.0338 ± 0.0013, 0.0155 ± 0.0004 at L = 16, 32, 64, "Scales as 1/L: disordered"; with the potential at T = 0.6: "⟨|m|⟩ = 0.954 ± 0.0001 at every size; Binder cumulant 0.667", an "Ordered ℤ₂ phase" (note v2 §4). The gate's size test uses the error bars: `size-independent within errors (|m64 - m16| < 3 sigma + 0.002)  [diff -0.0001, sigma 0.0001]`. See [Monte Carlo: an ordered ℤ₂ phase](/wiki/symmetry-breaking/toy-models/coset-model/monte-carlo).
- **Which control values to cite.** The worklog's fixed-seed "0.078 → 0.033 → 0.014", the referee's values, the adjudicator's long runs and the note v2 all differ. The note v2 governs, and its values are the ones the gate checks. The note's "± 0.0001 at every size" is printed by the script as `+- 0.0000` at L = 64, a difference of displayed precision only.

## Sources

- Root `CLAUDE.md` 'Method' — the rule
- `review/round4-adjudication.md` 'Lessons (into CLAUDE.md)' (lesson 2) and 'Rulings' (MC control, MC start) — the case
- `verify/toy_s4.py` — cold starts, four seeds, standard errors, the gated values
- `papers/reciprocity-toy-models.md` §4 — the method and the table as now stated
- `notes/toy-lagrangian.md` 'Chunk 3 results (2026-10-19): S4, quantum stability' — the superseded single-seed values
