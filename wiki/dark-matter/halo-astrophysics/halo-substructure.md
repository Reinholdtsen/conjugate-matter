---
title: "Halo-substructure probes: streams and dynamical friction"
weight: 30
status: established
description: "Cold stellar streams (GD-1, Pal 5) as probes of substructure, and dynamical friction on Fornax's globular clusters: the probes behind the program's withdrawn rows 3 and 4, which are under review."
provenance: [T]
sources:
  - "wiki/papers/broken-born-checkpoint-v2.md §13"
  - "wiki/papers/broken-born-checkpoint-v2.md §9"
  - "CLAUDE.md 'Since the handoff'"
  - "notes/broken-born-theory.md §9"
  - "notes/broken-born-theory.md §5.2"
  - "notes/broken-born-theory.md §10"
  - "notes/broken-born-theory.md §11"
  - "notes/broken-born-theory.md 'Addendum (v0.2, after the clumping notes): resolution of open problem 3'"
  - "notes/stream-stability.md 'Limit 1 — broad gate (μ ≫ mσ; dwarf regime)'"
  - "notes/stream-stability.md 'Consequences for the predictions table'"
  - "notes/wave-island.md 'What pins g? Two scenarios'"
  - "notes/wave-island.md 'Standing results after Chunks A+B'"
  - "notes/ufd-endpoint.md 'Verdict and closure of the clumping problem'"
  - "notes/broken-born-program-v1.md §9"
  - "notes/broken-born-program-v1.md §7"
---

*Halo substructure is the small-scale lumpiness of a galaxy's dark-matter halo, and two kinds of observation probe it. Cold stellar streams — long, thin trails of stars pulled off globular clusters or small galaxies by the Milky Way's tides — are disturbed by any lump of dark matter that passes through them, which leaves gaps and kinks along the stream. Dynamical friction — the drag a massive body feels from the gravitational wake it raises in a sea of lighter particles — makes globular clusters sink toward the center of a dwarf galaxy, at a rate set by the dark matter's distribution. The Comatter program's [lab notebook](../../history/documents/lab-notebook.md) used both as tests of its [founding image](../momentum-clumping/founding-image.md) of dark matter clumping by velocity, P.R.'s open conjecture; both tests are withdrawn, because the calculations of [the clumping problem](../../history/main-problems.md) showed that velocity clumping is nowhere a required consequence of the program. The two withdrawn rows, [velocity-space granularity](../momentum-clumping/velocity-granularity.md) and [Fornax friction suppression](../momentum-clumping/fornax-friction.md), are under review.*

**Status:** Established — [T], explained here from general knowledge — the program used these probes for old rows 3 and 4 of the lab notebook's [predictions table](../../predictions/table-history.md), which calc note [#4](../../../notes/ufd-endpoint.md) calls "permanently withdrawn, on both islands" ([`notes/ufd-endpoint.md`](../../../notes/ufd-endpoint.md)); [#11 §13](../../papers/broken-born-checkpoint-v2.md#13-predictions-and-kill-conditions) lists them as withdrawn and under review.

## Substructure in cold dark matter [T]

In cold dark matter (CDM), structure forms hierarchically: small halos form first and merge into larger ones. Many of the small halos survive inside the larger ones as subhalos, down to masses far below those of the faintest galaxies. Subhalos too small to have formed stars can be detected only through their gravity, and stellar streams are one of the few probes sensitive to them inside the Milky Way.

## Cold stellar streams [T]

A globular cluster orbiting the Milky Way loses stars to the Galaxy's tides. The escaped stars spread along the cluster's orbit, ahead of it and behind it, into a pair of thin tidal tails that can stretch across a large part of the sky. Because the stars left the cluster with small relative velocities, the stream is dynamically cold: its internal [velocity spread](velocity-dispersion.md) is small, so it stays thin, and a small disturbance persists in it for a long time.

When a subhalo passes close to a stream, it gives the nearby stars a gravitational kick. The kicked stars drift apart from their neighbors along the stream, and a gap opens that grows with time. Over a stream's lifetime many such encounters leave a pattern of density fluctuations along it. The pattern is measured as a power spectrum of the stream's density along its length, which records how much fluctuation there is at each wavelength. Point-like subhalos produce localized gaps. A different small-scale structure of the halo would produce a different power spectrum.

GD-1 and Palomar 5 (Pal 5) are among the best-studied cold streams. The European Space Agency's Gaia mission measures the positions and motions of their stars, and the Rubin Observatory's deep imaging maps fainter members.

## Dynamical friction [T]

A massive body moving through a sea of lighter particles deflects them as it passes. They gather into a wake of enhanced density behind it, and the wake's gravity pulls the body back. Chandrasekhar's formula gives the drag: proportional to the square of the body's mass and to the density of the background, and, for a body moving fast compared with the background particles, inversely proportional to the square of its speed, with a Coulomb logarithm. A body orbiting inside a galaxy loses orbital energy this way and spirals inward.

In a dwarf galaxy the massive bodies are globular clusters (GCs), and the drag comes mainly from the dark matter. The Fornax dwarf spheroidal has several globular clusters orbiting well away from its center. In a cuspy halo, friction should have dragged them to the center within the galaxy's lifetime; their presence there is the Fornax timing problem. In the literature, simulations find that friction becomes inefficient inside a constant-density core, where an inspiraling cluster stalls, an effect known as core stalling, which is one reason the problem is cited as evidence for a core ([dwarf galaxies](dwarf-galaxies.md)).

## The program's old rows 3 and 4

### The founding image

The lab notebook's first version predicted that [conjugate matter](../conjugate-matter/_index.md)'s gated self-attraction would make a halo's velocity distribution unstable. In its words ([#1 §5.2](../../../notes/broken-born-theory.md#52-collective-behavior-clumping-in-momentum-space-d-at-mean-field-level-o-beyond), tagged [D at mean-field level; O beyond]): "the collisionless Boltzmann equation with this mean field is the Jeans problem *with the roles of x and v exchanged*: a smooth Maxwellian f(v) is unstable to fragmentation into **discrete velocity streams of width Δv ∼ v\***, each spatially delocalized and internally coherent across kiloparsecs." The gate width v\* is the relative speed below which conjugate particles interact ([the velocity gate](../conjugate-matter/velocity-gate.md)). The notebook drew two consequences for observation: "superfluid-like cores in dwarfs and **suppressed dynamical friction** inside them (the Fornax globular-cluster timing problem is a feature, not a bug)". It also named the calculation on which both rested: "The growth rate γ versus orbital phase-mixing remains to be computed; it is the theory's most important undone calculation on the astrophysics side. [O]" The founding image is P.R.'s open conjecture [O], and its page states the evidence against it in full ([Conjecture: velocity clumping, the founding image](../momentum-clumping/founding-image.md)).

### The two rows, verbatim

The lab notebook's predictions table ([#1 §9](../../../notes/broken-born-theory.md#9-predictions); columns: observable, standard expectation, requirement, kill condition):

```text
3 | DM velocity-space structure in relaxed halos | Smooth f(v) + sub-percent accretion streams
  | Fragmentation into O(10) macro-streams of width ~v*, coherent over kpc; long-wavelength
    correlated perturbations of cold stellar streams (GD-1, Pal 5) vs. ΛCDM's localized subhalo gaps
  | Gaia DR4/Rubin stream power spectra consistent with smooth-halo + point-subhalo model only
4 | Dynamical friction in dwarf cores | GCs sink (cuspy CDM)
  | Suppressed in condensed cores; Fornax GCs stay put
  | Demonstrated normal friction in cored dwarfs
```

Here DM is dark matter, DR4 is Gaia's Data Release 4, and ΛCDM is the [standard cosmological model](../../cosmology/_index.md), with a [cosmological constant](../../cosmology/dark-energy/cosmological-constant.md) and cold dark matter.

**Row 3** reads the founding image through the stream probe. A halo whose dark matter moved in a few broad velocity streams, each coherent across kiloparsecs, would pull on a stellar stream along its whole length, and the stream's density fluctuations would be correlated over long wavelengths, unlike the localized gaps of point-like subhalos. A stream power spectrum consistent with a smooth halo plus point subhalos would have killed the row. The notebook ranked it with its strongest tests: "Rows 1, 3, and 7 are the flagship discriminants: no mainstream framework predicts an exponential scattering cliff, gravitationally-detectable macro-granularity of the local velocity distribution, *and* a guaranteed-null direct-detection program" ([#1 §9](../../../notes/broken-born-theory.md#9-predictions)).

**Row 4** reads it through dynamical friction. A dwarf core condensed in velocity space would drag less on globular clusters, so the Fornax clusters would stay where they are; normal friction demonstrated in a cored dwarf would have killed the row. The notebook ties the suppression to the "superfluid-like" condensed core and gives no calculation of the friction itself.

Both rows drew on the same two parameters: the notebook's parameter count lists "stream granularity scale, friction suppression" among the phenomena covered by σ₀/m and v\* ([#1 §10](../../../notes/broken-born-theory.md#10-parameter-count)).

## How the rows were withdrawn

The open calculation was the notebook's open problem 3: "**Stream-instability growth rate** γ vs. orbital phase-mixing: determines whether Prediction 3's granularity survives in Milky-Way-like halos" ([#1 §11](../../../notes/broken-born-theory.md#11-open-problems-in-order-of-severity)). [The clumping problem](../../history/main-problems.md) carried it out in three chunks ([the clumping notes](../../history/documents/clumping-notes.md)).

- **Calc note [#2](../../../notes/stream-stability.md), [particle island](../momentum-clumping/classicality-theorem.md).** The mean-field [instability criterion](../momentum-clumping/instability-criterion.md) fails by 28–31 orders of magnitude at the [scattering benchmark](../conjugate-matter/benchmark.md), and below threshold there is no growth: "There is no race with orbital stirring below threshold — the flocking never starts" ('Limit 1'). Hence: "Rows 3 (velocity granularity) and 4 (condensed cores / Fornax friction suppression) are **withdrawn**, and with them the mechanism-level linkage claimed between them" ('Consequences for the predictions table').
- **Calc note [#3](../../../notes/wave-island.md), [wave island](../momentum-clumping/wave-island/_index.md).** Collective behavior is possible there but not required. "Row 3 as written (Gaia/GD-1 granularity in MW-like halos)" fails "on both islands as a *mandatory* signature" ('Standing results after Chunks A+B'), with MW for the Milky Way. Under [Scenario A](../momentum-clumping/wave-island/scenario-a.md), "The surviving descendant of old rows 3–4 is therefore a sharply localized prediction: **anomalous central objects, density spikes, or disruption signatures in ultra-faint dwarfs, absent in classical dwarfs and the MW.**" Under [Scenario B](../momentum-clumping/wave-island/scenario-b.md), "streams are *tunable*, not mandatory".
- **Calc note #4.** The ultra-faint dwarfs contradict Scenario A, which is under review, and with it its descendant prediction: "Rows 3 and 4 of the predictions table are permanently withdrawn, on both islands. The Fornax mechanism goes with them." ('Verdict and closure of the clumping problem'.)

The lab notebook's addendum v0.2 records the result: "Rows 3–4 are struck from §9 permanently". [Program v1](../../history/documents/checkpoint.md) lists both as "Withdrawn with cause, permanently" ([#9 §9](../../../notes/broken-born-program-v1.md#9-predictions-and-kill-conditions)), with the calculations in its §7. [The checkpoint](../../history/documents/checkpoint.md) lists both as withdrawn and under review ([#11 §13](../../papers/broken-born-checkpoint-v2.md#13-predictions-and-kill-conditions)). Their pages are [Under review: velocity-space granularity in halos (old row 3)](../momentum-clumping/velocity-granularity.md) and [Under review: Fornax friction suppression (old row 4)](../momentum-clumping/fornax-friction.md), both in [claims under review](../../status/under-review.md). The theorem that summarizes the clumping problem is [the net theorem](../momentum-clumping/net-theorem.md).

The probes themselves are unaffected: streams and friction remain standard tests of dark-matter substructure. What was withdrawn, and is under review, is the program's claim that they would show its signature.

## Numbering

These are the "old" rows 3 and 4 of the lab notebook's table. In the current table, row 3 is [the island discriminant](../../predictions/island-discriminant.md) and row 4 is [dark energy](../../predictions/dark-energy-drift.md); see [the history of the predictions table](../../predictions/table-history.md).

## References

The lab notebook and the clumping calc notes cite no source for streams, dynamical friction or the Fornax problem; the momentum-gravity note's citations on the Sagittarius stream and on fine-grained streams are in [the references](../../references.md#momentum-gravity-and-velocity-dependent-forces). Added by the wiki from model memory (†):

- S. Chandrasekhar, "Dynamical friction," Astrophys. J. (1943)†.
- S. D. Tremaine, Astrophys. J. (1976)†: globular clusters sinking in dwarf galaxies, the origin of the Fornax timing problem.
- T. Goerdt, B. Moore, J. I. Read, J. Stadel, M. Zemp, "Does the Fornax dwarf spheroidal have a central cusp or core?," Mon. Not. R. Astron. Soc. (2006)†; J. I. Read et al., "Dynamical friction in constant density cores," Mon. Not. R. Astron. Soc. (2006)†: core stalling.
- M. Odenkirchen et al., Astrophys. J. Lett. (2001)†: the tidal tails of Palomar 5; C. J. Grillmair, O. Dionatos, Astrophys. J. Lett. (2006)†: the discovery of GD-1.
- R. G. Carlberg, Astrophys. J. (2012)†; D. Erkal, V. Belokurov, Mon. Not. R. Astron. Soc. (2015)†: gaps in streams from subhalo encounters.

## Used by

- [Under review: velocity-space granularity in halos (old row 3)](../momentum-clumping/velocity-granularity.md) — the stream test of the founding image.
- [Under review: Fornax friction suppression (old row 4)](../momentum-clumping/fornax-friction.md) — the friction test.
- [Conjecture: velocity clumping, the founding image](../momentum-clumping/founding-image.md) — predicted the condensed cores and the suppressed friction.
- [The history of the predictions table](../../predictions/table-history.md) — the old rows 3 and 4 and their renumbering.

## Sources

- [`wiki/papers/broken-born-checkpoint-v2.md` §13](../../papers/broken-born-checkpoint-v2.md#13-predictions-and-kill-conditions) — the two rows withdrawn and under review; [§9](../../papers/broken-born-checkpoint-v2.md#9-momentum-clumping-the-founding-image-tested) — the founding image as P.R.'s open conjecture, Scenario A under review
- [`CLAUDE.md`](../../../CLAUDE.md) 'Since the handoff' — the two rows and Scenario A under review
- [`notes/stream-stability.md`](../../../notes/stream-stability.md) 'Limit 1 — broad gate (μ ≫ mσ; dwarf regime)', 'Consequences for the predictions table' — no growth below threshold; the withdrawal on the particle island
- [`notes/wave-island.md`](../../../notes/wave-island.md) 'What pins g? Two scenarios', 'Standing results after Chunks A+B' — row 3 fails on both islands as a *mandatory* signature; Scenario A's descendant prediction; tunable streams
- [`notes/ufd-endpoint.md`](../../../notes/ufd-endpoint.md) 'Verdict and closure of the clumping problem' — the withdrawal on both islands, "permanently withdrawn" in its words
- [`notes/broken-born-program-v1.md` §9](../../../notes/broken-born-program-v1.md#9-predictions-and-kill-conditions), [§7](../../../notes/broken-born-program-v1.md#7-the-death-of-momentum-clumping-the-clumping-problem-closed-negative) — "Withdrawn with cause, permanently"; the calculations behind it
- [`notes/broken-born-theory.md` §9](../../../notes/broken-born-theory.md#9-predictions) — old rows 3 and 4, verbatim; the flagship discriminants
- [`notes/broken-born-theory.md` §5.2](../../../notes/broken-born-theory.md#52-collective-behavior-clumping-in-momentum-space-d-at-mean-field-level-o-beyond), [§10](../../../notes/broken-born-theory.md#10-parameter-count), [§11](../../../notes/broken-born-theory.md#11-open-problems-in-order-of-severity), 'Addendum (v0.2, after the clumping notes): resolution of open problem 3' — the founding image, suppressed friction and the Fornax timing problem; the parameter count; open problem 3; the rows struck
