---
title: "Gravitational waves from phase transitions"
weight: 30
status: established
description: "Stochastic gravitational waves from first-order phase transitions and their redshifted peak frequency, and the primordial background the lab notebook's dropped spectral step referred to."
provenance: [T]
sources:
  - "review/round3-adjudication.md 'Rulings' 5"
  - "verify/soliton_obituary.py 'Dark radiation (ruling 5)'"
  - "review/round3/referee/audit-notes.md Step 2"
  - "notes/knot-dark-matter-standalone.md §4"
  - "notes/broken-born-theory.md §6"
  - "notes/broken-born-theory.md §9"
  - "papers/broken-born-checkpoint-v2.md §13 row 10"
---

*A first-order phase transition in the early universe proceeds by bubbles of the new phase forming, growing and colliding, much as water boils, and the collisions and the sound waves they leave in the plasma produce gravitational waves that arrive today from every direction as a random background. The waves' characteristic frequency is set at the transition by its temperature and duration and has been stretched by the expansion ever since, so a transition at a higher temperature leaves a higher frequency today. The program met this physics in two places: the hidden-sector transition of its retired soliton dark-matter candidate, whose signal would lie far above the frequencies of current detectors, and an early idea, since dropped, that its conjugate gravity sector would leave a step in the primordial gravitational-wave background.*

**Status:** Established — [T] — textbook physics, written here from general knowledge; the retired candidate's frequency band was recomputed by the round-3 referee, and its corrected upper end is a [V] check in `verify/soliton_obituary.py` ([the soliton-obituary script](/wiki/method/verification/soliton-obituary-script)).

## Key facts

- **Sources of the signal [T].** Collisions of bubble walls, sound waves in the plasma and turbulence. A transition that is a smooth crossover rather than first order leaves no such signal, as #14 §4 also notes.
- **Peak frequency [T].** Redshifted to today, the peak frequency grows in proportion to the transition temperature T\* and to f\*/H\*, the peak frequency at the transition in units of the Hubble rate, and weakly with g\*. The script evaluates it in the standard form 1.65×10⁻⁵ Hz × (f\*/H\*) × (T\*/100 GeV) × (g\*/100)^{1/6}.
- **The retired candidate's band.** The withdrawn #14 §4 put the present-day peak at "~1e5 to 1e7 Hz for f\*/H\* = 1-100", above the band of ground-based detectors, "in the unconstrained ultra-high-frequency window targeted by proposed detectors". The round-3 referee recomputed "1.35e5 - 2.47e7 Hz" and marked it confirmed (`review/round3/referee/audit-notes.md` Step 2). With the corrected bound ξ < 0.760, ruling 5 moves the upper end to 3.2×10⁷ Hz, and the script checks that value at the withdrawn benchmark [V]. The two upper ends differ in taking the transition temperature as v or as v/ξ; the adjudication's value governs. See [the hidden sector's thermal history](/wiki/dark-matter/candidates/soliton-candidate/hidden-thermal-history).
- **Amplitude [T].** The strength of the signal grows with the transitioning sector's share of the total energy density at the transition. For the retired candidate, #14 §4: "The amplitude is suppressed by the hidden sector's share of the energy density at the transition".
- **The dropped spectral step.** The lab notebook said the conjugate gravity term predicts a step in G_eff before nucleosynthesis "and, conditionally on its one knob, a spectral step in the primordial gravitational-wave background. **[D]**" (#1 §6), and listed the step in its row 10 (#1 §9). #11's row 10 keeps only the "Optional a⁻⁶ G_eff step" and the negative ΔN_eff of closed dual curvature (#11 §13 row 10). A primordial background is the gravitational-wave background left by the earliest epochs, for example by inflation [T]. See [row 10: an early step in G_eff](/wiki/predictions/early-universe-step).

## Used by

- [The hidden sector's thermal history](/wiki/dark-matter/candidates/soliton-candidate/hidden-thermal-history) — the band a first-order hidden transition would leave.
- [Row 10: an early step in G_eff](/wiki/predictions/early-universe-step) — the earlier form of the row included the dropped spectral step.

## Sources

- `review/round3-adjudication.md` 'Rulings' 5 — the corrected upper end
- `verify/soliton_obituary.py` 'Dark radiation (ruling 5)' — the executed upper end and the peak-frequency formula
- `review/round3/referee/audit-notes.md` Step 2 — the referee's recomputed band
- `notes/knot-dark-matter-standalone.md` §4 — the withdrawn candidate's band and amplitude remarks (withdrawn)
- `notes/broken-born-theory.md` §6, §9 row 10 — the dropped spectral step
- `papers/broken-born-checkpoint-v2.md` §13 row 10 — the current row, without it
