---
title: "Thawing and freezing quintessence"
weight: 12
status: established
description: "The two classes of scalar-field dark energy: a thawing field is held at w ≈ −1 by the expansion and departs late, a freezing field moves early and slows toward −1. Why a thawing field's initial velocity drops out, hilltop models as thawing, where each class lies in the w₀–wₐ plane, the program's corridor wₐ ≈ −1.5(1 + w₀), for which no document gives a reference, and its place relative to DESI DR2's fits (flag 43), DESI DR2 against the class, and the thawing drift of τ that row 4 requires."
provenance: [T]
sources:
  - "papers/broken-born-checkpoint-v2.md §10"
  - "papers/broken-born-checkpoint-v2.md §13 row 4"
  - "CLAUDE.md 'Since the handoff'"
  - "notes/broken-born-theory.md §7"
  - "notes/broken-born-theory.md §9"
  - "notes/broken-born-program-v1.md §8"
  - "notes/broken-born-program-v1.md §9"
  - "HANDOFF.md §2"
  - "notes/toy-lagrangian.md 'Chunk 2 results'"
  - "review/round3/referee/audit-notes.md Step 4(c) item 11"
  - "review/wiki-build-flags.md items 27, 43"
---

*Thawing and freezing are the two classes into which [quintessence](/wiki/cosmology/dark-energy/quintessence), dark energy made of a slowly changing scalar field, divides according to how its equation of state w, the ratio of its pressure to its energy density, changes with time. A thawing field is held almost still by the expansion of the universe at early times, so w stays close to −1, the value of a [cosmological constant](/wiki/cosmology/dark-energy/cosmological-constant); the field starts to change only late, and w rises above −1 toward the present. A freezing field is already changing at early times and slows down, so w falls toward −1. A field that starts near the maximum of its potential, a hilltop model, thaws. The program's dark-energy field [τ](/wiki/cosmology/dark-energy/tau-quintessence) is taken to be such a field, and [row 4](/wiki/predictions/dark-energy-drift) of its predictions requires a thawing drift that never takes w below −1. The second data release of the [Dark Energy Spectroscopic Instrument](/wiki/cosmology/dark-energy/desi) (DESI) favours a w that was below −1 earlier in cosmic history, a phase that a field of this kind, with the standard kinetic energy, cannot produce, so the requirement is under real pressure.*

**Status:** Established — [T] — textbook cosmology, written here from general knowledge, with the literature it names marked † (Caldwell and Linder †; Dutta and Scherrer †; Scherrer and Sen †; Ratra and Peebles †); no `verify/` script checks it. The program's uses are stated in [checkpoint #11](/wiki/history/documents/checkpoint) §10, in its entries "Dark energy [D + T]" and "Under pressure (v2.1)", and in §13 row 4; the [lab notebook](/wiki/history/documents/lab-notebook) tags τ's thawing shape [T] (#1 §7 item 2). No document gives a reference for the thawing corridor that #11 §10 states, and where the corridor lies relative to DESI's second data release is flag 43 in `review/wiki-build-flags.md`, confirmed by two independent checks kept outside [the gate](/wiki/method/verification/the-gate).

## The field equation and expansion damping [T]

A scalar field φ that is uniform in space obeys ([the field equation](/wiki/cosmology/dark-energy/quintessence#the-field-equation-t))

```text
φ̈ + 3Hφ̇ + V′(φ) = 0
```

where H is the expansion rate and V the field's potential energy density. It has the form of a damped oscillator's equation: −V′ is the force, and 3Hφ̇ is a damping set by the expansion, often called Hubble friction. The equation of state follows from the field's kinetic and potential energy densities ([energy density and pressure](/wiki/cosmology/dark-energy/quintessence#energy-density-and-pressure-t)):

```text
w = (½φ̇² − V) / (½φ̇² + V)
```

so w is close to −1 whenever the kinetic energy ½φ̇² is small compared with V, and w rises as the kinetic energy grows.

Two rates compete: the expansion rate H and the rate set by the curvature of the field's potential, of order √|V″|. While H is the larger, the damping holds the field nearly still; once H has fallen below it, the field responds to the slope of its potential [T]. Whether a field is held still at early times or is already changing decides its class (Caldwell and Linder †).

| Class | Early times | Late times | Present value w₀ and drift wₐ |
| --- | --- | --- | --- |
| Thawing | field held still, w ≈ −1 | w rises above −1 | w₀ > −1, wₐ < 0 |
| Freezing | field changing, w > −1 | w falls toward −1 | w₀ > −1, wₐ > 0 |

The last column anticipates the two-number description of w set out below ([where the classes lie in the w₀–wₐ plane](#where-the-classes-lie-in-the-wwₐ-plane)).

## Thawing [T]

A thawing field starts out held by the damping at some initial value φᵢ, with φ̇ ≈ 0 and w ≈ −1. As the expansion rate H falls, the damping weakens, the field begins to move toward lower potential energy, its kinetic energy grows, and w rises above −1. The departure from −1 comes late: w stays close to −1 for most of the expansion history and changes mainly at low [redshift](/wiki/cosmology/scale-factor-duality/redshift), in the recent past.

### The initial velocity drops out

While the slope V′ is negligible, the field equation reduces to φ̈ + 3Hφ̇ = 0, which says that a³φ̇ is constant, with a the [scale factor](/wiki/cosmology/scale-factor-duality/friedmann-cosmology), the factor by which cosmic distances have grown:

```text
d(a³φ̇)/dt = a³(φ̈ + 3Hφ̇) = 0        so        φ̇ ∝ a⁻³
```

An initial velocity therefore dies away as the universe expands, and it has no effect by the time the field starts to move [T]. A thawing history is fixed by the potential and the initial value φᵢ, with no separate initial velocity. In this wiki's reading, this is why [the dark-energy over-constraint](/wiki/cosmology/dark-energy/over-constraint) counts the initial value τᵢ of the program's field and no velocity.

### Hilltop models

A hilltop model starts near a maximum of its potential, where V′ ≈ 0 and V″ < 0 (Dutta and Scherrer †). Near the maximum the potential is an inverted parabola in the displacement from the top, and the force −V′ points away from the top, so a small displacement grows once the damping weakens. Starting closer to the top keeps w near −1 for longer; how fast w then rises depends on |V″| at the top compared with the expansion rate. Hilltop models are thawing models [T].

The periodic potential of an [axion-like field](/wiki/cosmology/dark-energy/axion-like-fields), V₀[1 + cos(φ/f)], has its maximum where cos(φ/f) = 1, with V″ = −V₀/f² there, so a field that starts near that maximum is a hilltop model. The program's τ is of this kind ([how τ behaves](/wiki/cosmology/dark-energy/tau-quintessence#how-τ-behaves-thawing-from-the-hilltop)).

### Nearly common histories

When w stays close to −1, the late rise of w has a similar shape for many potentials. Scherrer and Sen † found that for thawing fields with nearly flat potentials the history w(a) depends little on the shape of the potential, and Dutta and Scherrer † found the same for hilltop models, with the curvature at the maximum as a further parameter [T]. Thawing models therefore do not spread over the whole region of their signs, w₀ > −1 and wₐ < 0, but fall in a narrow band within it ([below](#where-the-classes-lie-in-the-wwₐ-plane)).

## Freezing [T]

A freezing field is already changing at early times, with w > −1. Its motion slows as its potential flattens, and w decreases toward −1 at late times. Potentials that fall off as an inverse power of the field, the form Ratra and Peebles † studied, are the standard example. A freezing field's dark energy departed most from a cosmological constant in the past and approaches it today, the reverse of a thawing field.

Both classes stay at or above −1. For a field with the standard kinetic energy, ρ + p = φ̇², with ρ the energy density and p the pressure, so ρ + p is never negative and w ≥ −1 while ρ is positive ([a canonical scalar obeys the null energy condition](/wiki/cosmology/dark-energy/phantom-divide#a-canonical-scalar-obeys-it-t)). A cosmological constant is the common limit of both classes, a field that never moves.

## Where the classes lie in the w₀–wₐ plane

Surveys report a changing w by two numbers in the Chevallier–Polarski–Linder (CPL) form w(a) = w₀ + wₐ(1 − a), with a = 1 today: w₀ is the present value, and a negative wₐ means that w has been rising as the universe expands ([the CPL parametrization](/wiki/cosmology/dark-energy/cpl-parametrization)). A thawing field's CPL point has w₀ > −1 and wₐ < 0; a freezing field's has w₀ > −1 and wₐ > 0 [T] ([thawing models in the w₀–wₐ plane](/wiki/cosmology/dark-energy/cpl-parametrization#thawing-models-in-the-wwₐ-plane)).

Thawing models fall in a narrow band through the cosmological-constant point (w₀, wₐ) = (−1, 0) [T]. The program writes the band as a line, the "thawing corridor wₐ ≈ −1.5(1 + w₀)" (#11 §10). The lab notebook calls it "the standard thawing corridor" (#1 §7 item 2, transcribed from its LaTeX), and [the v1 paper](/wiki/history/documents/checkpoint) gives the same form (#9 §8). No document gives a reference for the corridor or its slope, and the wiki has not checked the slope against the literature.

The CPL form is a straight line in a, while a thawing field's w is curved: close to −1 for most of the history and rising late. A line fitted to such a history can pass below −1 in the past although the field never does ([what two numbers cannot represent](/wiki/cosmology/dark-energy/cpl-parametrization#what-two-numbers-cannot-represent-t)). Flag 43 in `review/wiki-build-flags.md` applies this to the corridor. On it, "w₀ + wₐ + 1 = −(1 + w₀)/2, which is negative for every w₀ > −1", so every corridor point has w₀ > −1 and w₀ + wₐ < −1: the region in which a CPL line crosses −1 in the past, and the region in which the fits of DESI's Data Release 2 (DR2) lie. In the flag's audit, fields with τ's potential that never fall below −1 also give fits in that region. In the flag's account, what separates the corridor from DR2's fits is the slope, which sets where the line crosses −1, at a redshift z: "The corridor's line crosses at z = 2 for every w₀; DR2's fits cross at z ≈ 0.35–0.50". The flag awaits Paul's ruling ([pending rulings](/wiki/status/open-problems#pending-rulings)); its account and its audit are on [the corridor and DR2's crossing](/wiki/cosmology/dark-energy/cpl-parametrization#the-corridor-and-dr2s-crossing).

## The second DESI data release and the thawing class

#11 §10 quotes the release: in every dataset combination "the favored w(z) shows a phase of w > −1 at low redshifts and a phantom crossing to w < −1 above redshifts z ≃ 0.4", and this preference "is thus rather independent of parametrization choices made in the analysis" [21S]. The low-redshift phase, w above −1 with dark energy weakening, has the sign of a thawing drift. The phase above z ≃ 0.4, w below −1, lies outside both classes, since neither a thawing nor a freezing field with the standard kinetic energy reaches w < −1 ([the phantom divide](/wiki/cosmology/dark-energy/phantom-divide)). In CPL terms the favoured shape has w₀ > −1 with w₀ + wₐ < −1: the signs of a thawing fit, w₀ > −1 and wₐ < 0, together with a crossing ([a phantom crossing in the w₀–wₐ plane](/wiki/cosmology/dark-energy/cpl-parametrization#a-phantom-crossing-in-the-wwₐ-plane-t)). The signs of w₀ and wₐ alone therefore do not separate a thawing drift from a crossing.

The [round-3](/wiki/method/review/round-3) referee, quoting the release, notes that models respecting the null energy condition, a class that includes thawing quintessence, "can somewhat outperform" the cosmological-constant model but are disfavoured relative to the w₀–wₐ fit (`review/round3/referee/audit-notes.md` Step 4(c) item 11). #11 §10 states the consequence for the program:

> The framework's strict w ≥ −1 therefore stands against the direct reading of the data. It survives on two points: non-phantom quintessence fits remain compatible [19S], and w(z) is inferred from distances rather than observed, as [21S] also notes. DR3 is the decisive test (§13, row 4).

DR3 is DESI's Data Release 3. The measurement and its route into the program are on [DESI DR2's phantom crossing](/wiki/cosmology/dark-energy/desi-dr2-phantom-crossing).

Before the round-3 review, the lab notebook read DESI's results by their signs alone, as flag 43 notes: the thawing shape "is the *sign pattern DESI reports*" (#1 §7 item 2). That reading is superseded ([the earlier readings of DESI](/wiki/cosmology/dark-energy/desi-dr2-phantom-crossing#superseded-the-earlier-readings-of-desi)).

## How the program uses the classification

- **τ is a thawing hilltop field.** #11 §10: "τ is hilltop quintessence on the Maslov circle, V = V₀[1 + cos(τ/f)], periodicity by topology; strictly w ≥ −1; thawing corridor wₐ ≈ −1.5(1 + w₀)". The lab notebook applies the class to τ: "Hilltop initial conditions give w ≈ −1 in the past, rising now: w₀ > −1, wₐ < 0, on the standard thawing corridor wₐ ≈ −1.5(1 + w₀)" (#1 §7 item 2, transcribed from its LaTeX), tagged [T], since thawing is a property of hilltop fields in general, not a result of the program. The [handoff](/wiki/history/documents/handoff) lists τ as "thawing, w ≥ −1 always" among the live results (`HANDOFF.md` §2). Where the corridor lies relative to DR2's fits is flag 43 ([above](#where-the-classes-lie-in-the-wwₐ-plane)). The program's account is on [τ: hilltop quintessence on the Maslov circle](/wiki/cosmology/dark-energy/tau-quintessence).
- **Row 4.** The requirement of #11 §13 row 4 is "Thawing, w₀ > −1, wₐ < 0, never phantom; drift persists in DESI DR3", with the kill conditions "DR3+ constant −1 (kills τ-sector); robust intrinsic w < −1 (kills outright) — DR2 already favors a crossing above z ≈ 0.4 (§10)". In this wiki's reading, the first kill condition is data that show no thawing drift at all, and the second is a phase that neither class can reach. The earlier tables placed the requirement "on the thawing corridor" (#1 §9 row 5; #9 §9 row 4); #11 keeps only the signs ([history of the predictions table](/wiki/predictions/table-history)).
- **Not specific to τ.** The handoff gives the outcome that keeps the sector alive as "continued thawing drift keeps it alive (shared with other dynamical-DE models)" (`HANDOFF.md` §2), DE being dark energy. A thawing drift in the data does not single out τ among thawing models.
- **The over-constraint.** With the initial velocity dropping out and V₀ "fixed by Ω_DE" (#1 §7 item 4; #9 §8), Ω_DE being the fraction of the universe's energy density in dark energy today, two of τ's numbers remain free: "two parameters (f, τᵢ) for three observables (w₀, wₐ, t_turn) — one over-constraint" (#11 §10), t_turn being the time of the far-future turnaround. That turnaround needs V(τ) < 0, and the potential as written is never negative for V₀ > 0, so t_turn is not defined for it (flag 27 in `review/wiki-build-flags.md`; [Open: the sign of V(τ) and the turnaround](/wiki/cosmology/dark-energy/potential-sign)). No document computes (w₀, wₐ) from (f, τᵢ) ([the dark-energy over-constraint](/wiki/cosmology/dark-energy/over-constraint)).
- **A conjecture: the thawing as a drifting angle.** The toy-model worklog reads τ's thawing geometrically: "It also means the present-day thawing of τ would be a slow drift of the polarization angle. That is a claim about the program, not verified here." (`notes/toy-lagrangian.md`, 'Chunk 2 results'). No document computes the drift ([Conjecture: the thawing of dark energy as a drifting polarization angle](/wiki/symmetry-breaking/goldstone-angle#conjecture-the-thawing-of-dark-energy-as-a-drifting-polarization-angle)).

## What the record leaves open

- **The corridor's source.** No document gives a reference for wₐ ≈ −1.5(1 + w₀) or for its slope, and the wiki has not checked the slope against the literature.
- **Flag 43.** Where the corridor lies relative to DR2's crossing awaits Paul's ruling ([pending rulings](/wiki/status/open-problems#pending-rulings)).
- **τ's own history.** No program document integrates τ's field equation or computes its (w₀, wₐ). Flag 43's audit integrated fields with τ's potential numerically, outside the gate (`review/wiki-build-checks/corridor/`).
- **The data.** Whether DESI's Data Release 3 shows a persisting thawing drift is the test of row 4. The root `CLAUDE.md`: "The dark-energy sector is under real pressure ahead of DR3."

## Standard references

Added by the wiki from model memory (†); the program's documents cite none of them.

- R. R. Caldwell and E. V. Linder †: the thawing and freezing classes of quintessence.
- S. Dutta and R. J. Scherrer †: hilltop quintessence and its histories of w.
- R. J. Scherrer and A. A. Sen †: thawing fields with nearly flat potentials share nearly one history of w.
- B. Ratra and P. J. E. Peebles †: a scalar field with an inverse-power potential as dark energy, a freezing example.

## Used by

- [Row 4: thawing dark energy, never phantom](/wiki/predictions/dark-energy-drift) — the requirement "Thawing, w₀ > −1, wₐ < 0, never phantom".
- [τ: hilltop quintessence on the Maslov circle](/wiki/cosmology/dark-energy/tau-quintessence) — τ thaws from near the maximum of its potential.
- [The dark-energy over-constraint](/wiki/cosmology/dark-energy/over-constraint) — the initial velocity drops out, leaving f and τᵢ.
- [The no-phantom bound w ≥ −1](/wiki/cosmology/dark-energy/no-phantom-bound) — row 4's second kill condition; the first tests the thawing drift.
- [DESI DR2's phantom crossing](/wiki/cosmology/dark-energy/desi-dr2-phantom-crossing) — a low-redshift phase with the sign of a thawing drift, and a phase below −1 that neither class reaches.
- [Row 5: the fate of the expansion](/wiki/predictions/fate-of-expansion) — the turnaround would come later in the same motion that row 4 tests, once V(τ) has fallen below zero, which the potential as written never does (flag 27).
- [The polarization as a Goldstone angle](/wiki/symmetry-breaking/goldstone-angle) — the conjecture that τ's thawing is a drift of the polarization angle.

## Sources

- `papers/broken-born-checkpoint-v2.md` §10 — τ as hilltop quintessence, the thawing corridor, the over-constraint, DR2's crossing and the two points on which the sector survives; §13 row 4 — the requirement and the kill conditions
- `CLAUDE.md` 'Since the handoff' — "under real pressure ahead of DR3"
- `notes/broken-born-theory.md` §7 items 2 and 4 — τ's thawing shape [T], "the standard thawing corridor", "the sign pattern DESI reports", V₀ fixed by Ω_DE; §9 row 5 — "on the thawing corridor"
- `notes/broken-born-program-v1.md` §8 — the corridor and V₀ fixed by Ω_DE; §9 row 4 — "on the thawing corridor"
- `HANDOFF.md` §2 — "thawing, w ≥ −1 always"; continued thawing drift "shared with other dynamical-DE models"
- `notes/toy-lagrangian.md` 'Chunk 2 results' — the thawing of τ as a drift of the polarization angle, unverified
- `review/round3/referee/audit-notes.md` Step 4(c) item 11 — models respecting the null energy condition against the w₀–wₐ fit
- `review/wiki-build-flags.md` item 43 — the corridor in the region of DR2's fits, the fits of fields that never cross, and the slope that separates the corridor from DR2's crossing, with the auditors' scripts and outputs in `review/wiki-build-checks/corridor/`; item 27 — the potential as written is never negative, which bears on t_turn and row 5
