---
title: "Scenario B: tunable streams (quarantined)"
weight: 30
status: alive
description: "If cores come from elsewhere and the coupling is free, streams are tunable across about ten orders but never required — an option rather than a prediction, flagged by the checkpoint as a degeneration risk."
provenance: [D, T]
sources:
  - "notes/wave-island.md 'What pins g? Two scenarios'"
  - "notes/wave-island.md 'The rate'"
  - "notes/wave-island.md 'Setup'"
  - "notes/ufd-endpoint.md 'The data'"
  - "notes/ufd-endpoint.md 'Verdict and closure'"
  - "notes/stream-stability.md 'Limit 1 — broad gate'"
  - "wiki/papers/broken-born-checkpoint-v2.md §15"
  - "wiki/papers/broken-born-checkpoint-v2.md §9"
  - "notes/broken-born-program-v1.md §7"
  - "notes/broken-born-program-v1.md §11"
  - "notes/broken-born-theory.md 'Addendum (v0.2)'"
  - "HANDOFF.md §2"
  - "verify/velocity_gated_gravity.py 'D. The obituary's scope'"
---

*Scenario B is the alternative to [Scenario A](scenario-a.md) on the [wave island](_index.md). In it, the smooth cores of dwarf galaxies are made by something other than [conjugate matter](../../conjugate-matter/_index.md)'s gated attraction, such as the quantum pressure of extremely light wave dark matter or the feedback of ordinary matter, so nothing fixes the strength of that attraction. With the coupling free, it can be set anywhere in a window about ten orders of magnitude wide in which velocity streams form, or outside the window, where they do not. Streams are then possible but never required. That makes them an option the program can accommodate rather than a prediction it is committed to, which in [Lakatos's terms](../../../method/lakatosian-methodology.md) is a sign of a degenerating research programme. The checkpoint keeps the scenario alive but quarantined, among the program's listed degeneration risks.*

**Status:** Alive but quarantined. [Checkpoint #11](../../../history/documents/checkpoint.md) [§15](../../../papers/broken-born-checkpoint-v2.md#15-assessment) lists the "tunable wave-island collective sector (quarantined)" among its degeneration risks. The statement belongs to [#11 §9](../../../papers/broken-born-checkpoint-v2.md#9-momentum-clumping-the-founding-image-tested) (ii), which is tagged [D + T] as a whole; the window is computed in [`notes/wave-island.md`](../../../../notes/wave-island.md) (calc note [#3](../../../../notes/wave-island.md)) at a single mass. Not machine-checked; no `verify/` script covers a number of calc note #3 or [#4](../../../../notes/ufd-endpoint.md); the gate checks only calc note [#2](../../../../notes/stream-stability.md)'s shortfall ratios, in section D of [`verify/velocity_gated_gravity.py`](../../../../verify/velocity_gated_gravity.py) ([the velocity-gated-gravity script](../../../method/verification/velocity-gated-gravity-script.md)).

## The scenario

[The gated condensation rate Γ_self](condensation-rate.md) depends on the gated coupling g, and calc note #3, the second of [the clumping calc notes](../../../history/documents/clumping-notes.md), asked what fixes it ('What pins g? Two scenarios'). Scenario A answered that the gated channel makes the cores of classical dwarf galaxies, which fixes g; the ultra-faint dwarfs contradict it, and it is under review ([#11 §9](../../../papers/broken-born-checkpoint-v2.md#9-momentum-clumping-the-founding-image-tested)). Scenario B is the other answer:

> Scenario B — cores come from elsewhere (fuzzy-end quantum pressure at m ~ 10⁻²² eV, or baryonic feedback), leaving g free.

Both alternatives are established explanations of dwarf-galaxy cores [T] ([dwarf galaxies](../../halo-astrophysics/dwarf-galaxies.md)). In fuzzy dark matter, a boson so light that its de Broglie wavelength reaches the size of a galactic core cannot be confined more tightly than that wavelength, and the resulting quantum pressure supports a flat core ([bounds on fuzzy dark matter](../../wave-dark-matter/fuzzy-dark-matter-bounds.md)). In baryonic feedback, repeated outflows of gas driven by supernovae change the gravitational potential at the center of a galaxy fast enough to push dark matter outward and flatten the cusp [T]. Either way, the cores no longer fix the gated coupling.

## The stream condition

### The mean-field parameter X

Calc note #3 expresses the free coupling through a dimensionless parameter:

> Writing X ≡ gn/(mσ²) (the Chunk-A mean-field parameter, with X < 1 required so halos aren't modulationally unstable), the stream condition Γ_self ≥ Ω becomes X ≥ √(Ωσ²/(c m v\*⁴)).

Here n is the number density of χ, m its mass and σ the halo's [velocity dispersion](../../halo-astrophysics/velocity-dispersion.md); X is unrelated to [the momentum graviton](../../../gravity/momentum-graviton/_index.md) of the same letter. The numerator gn is the mean-field interaction energy of a particle, the ε_int of Chunk A ([the gated Vlasov model](../gated-vlasov-model.md)), the attraction exerted on it by its neighbors; the denominator mσ² is its kinetic energy; X compares the two. It is the quantity in Chunk A's broad-gate threshold, "g n/(m σ²) ≥ 1" ([`notes/stream-stability.md`](../../../../notes/stream-stability.md), 'Limit 1 — broad gate'; [the mean-field criterion](../instability-criterion.md)). Above that threshold the uniform halo itself is unstable.

### Why X stays below 1

A medium is modulationally unstable when small modulations of a uniform wave grow instead of dispersing. In a wave medium with attractive self-interaction this happens when the attraction outweighs the dispersion that smooths modulations out [T]; for a gas with velocity spread σ, the spread plays that role, and Chunk A's threshold X = 1 marks the balance. Calc note #3 requires X < 1 so that the halo as a whole stays stable, and that requirement is the upper edge of the window, X = 1.

### The lower edge

Ω = 1/t_dyn is the orbital stirring rate, with t_dyn the dynamical time, and Γ_self ≥ Ω is the condition that condensation outruns the stirring. The note gives the result without the step. On the wiki's reading, the rate formula Γ_self ≈ c g²ρ² min(σ, v\*)⁴/(m³σ⁶), with g = X mσ²/n and ρ = mn, becomes c X² m min(σ, v\*)⁴/σ², and setting it at least equal to Ω gives the bound on X. The note writes it with v\*⁴, the gate-narrow case, in which the halo's dispersion exceeds the width of [the velocity gate](../../conjugate-matter/velocity-gate.md).

## The window

With Milky Way (MW) numbers the window is ten orders of magnitude wide (calc note #3):

> MW numbers, m = 0.1 meV: window X ∈ [5×10⁻¹¹, 1] — ten orders of magnitude. Verdict B: streams are tunable, not mandatory.

Any coupling with X between about 5×10⁻¹¹ and 1 satisfies the stream condition in the Milky Way; a smaller coupling does not; and nothing in the scenario selects one value over another. Two limits of the calculation:

- **One mass.** The window is evaluated at m = 0.1 meV, the upper end of calc note #3's wave island ("m ≲ 0.1 meV", 'Setup'). The lower edge carries a factor 1/√m, and no source evaluates the window at other masses.
- **Uncited inputs.** The note does not say which Milky Way values of Ω, σ and v\* enter the window. Its environment table, given on [the page on Scenario A](scenario-a.md), lists densities, dispersions and dynamical times without references.

## Why it is a degeneration flag

In Imre Lakatos's account of research programmes ([Lakatos's methodology of research programmes](../../../method/lakatosian-methodology.md)), a programme is progressive while its changes predict new facts, some of which are then observed, and degenerating when its changes only accommodate facts already known [T]. A consequence that the program can switch on or off with a free parameter predicts nothing: it is consistent both with streams and with their absence. Calc note #3 states the conclusion:

> In Lakatos terms from the earlier discussion: on this branch the granularity prediction is no longer a novel requirement of the program, only an option — a degeneration flag.

"The granularity prediction" is [the lab notebook](../../../history/documents/lab-notebook.md)'s old row 3, [velocity-space granularity in halos](../velocity-granularity.md), withdrawn and under review; the "earlier discussion" is not identified in the note. The checkpoints carry the flag into their self-assessments:

- [Program v1](../../../history/documents/checkpoint.md) ([#9 §11](../../../../notes/broken-born-program-v1.md#11-assessment)): "Degeneration risks — the wave-island collective sector is tunable (flagged, quarantined); the gate's tail shape is not yet forced."
- Checkpoint [#11 §15](../../../papers/broken-born-checkpoint-v2.md#15-assessment): "Degeneration risks: tunable wave-island collective sector (quarantined); gate tail not yet forced", followed by the novelty demotion of [§7.4](../../../papers/broken-born-checkpoint-v2.md#74-literature-position-updated-by-this-sessions-search--honesty-upgrade), [the failure of #14's soliton model](../../candidates/soliton-candidate/obituary.md), the re-attribution of [the compatibility theorem](../../../phase-space/born-geometry/compatibility-theorem.md) and [the phantom crossing](../../../cosmology/dark-energy/desi-dr2-phantom-crossing.md) in the second data release of the Dark Energy Spectroscopic Instrument, against §10's [w ≥ −1](../../../cosmology/dark-energy/no-phantom-bound.md), where w is dark energy's [equation of state](../../../cosmology/dark-energy/quintessence.md#dark-energy-and-the-equation-of-state), its pressure divided by its energy density, and −1 is its value for a cosmological constant.

Neither document defines "quarantined". In practice the scenario stays in the program, but it appears among the risks in §15 and not among the predictions of [#11 §13](../../../papers/broken-born-checkpoint-v2.md#13-predictions-and-kill-conditions) ([the assessment](../../../program/assessment.md)).

## Its place in the verdict on the clumping problem

Calc note #4, after finding Scenario A contradicted by the ultra-faint dwarfs, closed [the clumping problem](../../../history/main-problems.md) with Scenario B as the only surviving form of collective behavior ('Verdict and closure of the clumping problem'):

> Nowhere in the viable parameter space of BBT is velocity-space clumping a mandatory phenomenon. It is forbidden for classical-particle χ, fatal where it would have been mandatory (Scenario A), and merely optional elsewhere (Scenario B, ten tunable orders of magnitude — a degeneration flag, not a prediction).

BBT is Broken-Born theory, the program's earlier name. Scenario B is the "decorative (free wave)" leg of [the net theorem](../net-theorem.md), in [#11 §9](../../../papers/broken-born-checkpoint-v2.md#9-momentum-clumping-the-founding-image-tested)'s words. It also defines what is left of the wave island: "The surviving wave island is roughly 3×10⁻¹⁹ eV ≲ m ≲ 10⁻⁴ eV with Scenario-B couplings." Calc note #4's robustness check makes the boundary between the scenarios explicit: a core normalization "κ < 1 is by definition Scenario B" ('The data'), that is, any coupling too weak to make the cores falls under Scenario B.

The later summaries state the verdict in the same terms:

- The lab notebook's addendum v0.2 ([#1](../../../../notes/broken-born-theory.md)): "With the coupling left free, streams are tunable across ~10 orders — optional, never required."
- Program v1 ([#9 §7 item 2](../../../../notes/broken-born-program-v1.md#7-the-death-of-momentum-clumping-the-clumping-problem-closed-negative)): "With the coupling left free instead, streams are merely tunable across ~10 orders — optional, never required."
- Checkpoint [#11 §9](../../../papers/broken-born-checkpoint-v2.md#9-momentum-clumping-the-founding-image-tested) (ii): "With coupling free, streams are tunable across ~10 orders: optional, never required."
- [The handoff](../../../history/documents/handoff.md) of 2026-10-19 ([`HANDOFF.md` §2](../../../../HANDOFF.md#2-scientific-state-one-screen)), in its list of failed claims, describes [momentum clumping](../founding-image.md) as "fatal where mandatory on the wave island (ultra-faint dwarfs would be drained; Segue 1 intact), tunable elsewhere." The founding image is P.R.'s open conjecture ([#11 §9](../../../papers/broken-born-checkpoint-v2.md#9-momentum-clumping-the-founding-image-tested)).

## An unresolved conflict: the fuzzy-end option

Scenario B's first named source of cores, "fuzzy-end quantum pressure at m ~ 10⁻²² eV", lies below the lower edge of the wave island that calc note #4 later set, 3×10⁻¹⁹ eV, at the bound from ultra-faint-dwarf kinematics and the Lyman-α forest that also closed Scenario A's light-mass branch ([bounds on fuzzy dark matter](../../wave-dark-matter/fuzzy-dark-matter-bounds.md)). Neither note addresses the mismatch, and [the record of conflicts between sources](../../../history/documents/source-conflicts.md) lists it as unresolved. Baryonic feedback, the other named option, is not affected by the mass bound.

## Sources

- [`notes/wave-island.md`](../../../../notes/wave-island.md) 'What pins g? Two scenarios' — the scenario, the stream condition, the window and the Lakatos reading; 'The rate [D, heuristic coefficients]' — the rate; 'Setup' — the island's upper edge
- [`notes/ufd-endpoint.md`](../../../../notes/ufd-endpoint.md) 'Verdict and closure of the clumping problem' — Scenario B in the net verdict and the surviving range; 'The data' — κ < 1 as Scenario B
- [`notes/stream-stability.md`](../../../../notes/stream-stability.md) 'Limit 1 — broad gate' — the mean-field threshold that defines X
- [`wiki/papers/broken-born-checkpoint-v2.md` §15](../../../papers/broken-born-checkpoint-v2.md#15-assessment) — the quarantine among the degeneration risks; [§9](../../../papers/broken-born-checkpoint-v2.md#9-momentum-clumping-the-founding-image-tested) (ii), (iii) — the current statement and the net theorem; [§9](../../../papers/broken-born-checkpoint-v2.md#9-momentum-clumping-the-founding-image-tested) — the founding image as P.R.'s open conjecture, Scenario A under review
- [`notes/broken-born-program-v1.md` §7 item 2](../../../../notes/broken-born-program-v1.md#7-the-death-of-momentum-clumping-the-clumping-problem-closed-negative) — the v1 statement; [§11](../../../../notes/broken-born-program-v1.md#11-assessment) — the v1 degeneration risks
- [`notes/broken-born-theory.md`](../../../../notes/broken-born-theory.md) 'Addendum (v0.2)' — the notebook's record
- [`HANDOFF.md` §2](../../../../HANDOFF.md#2-scientific-state-one-screen) — the handoff's list of failed claims
- [`verify/velocity_gated_gravity.py`](../../../../verify/velocity_gated_gravity.py) section D — calc note #2's shortfall ratios, the only clumping numbers the gate checks
