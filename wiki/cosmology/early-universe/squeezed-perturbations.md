---
title: "Squeezed cosmological perturbations"
weight: 25
status: established
description: "Once a perturbation mode's wavelength leaves the Hubble radius during inflation, its quantum state is squeezed by about the number of e-folds since then, r_k ≃ ln(a/a_k): about 50 at the end of inflation and 100–120 today on the largest scales. On the Siegel half-plane a squeezed state lies at distance 2r from the round vacuum, and the phase-space-diameter note reads an early-chat aspect ratio of 10⁹² as a squeezing of 105.9."
provenance: [T]
sources:
  - "papers/phase-space-diameter.md §5"
  - "papers/phase-space-diameter.md §6"
  - "papers/phase-space-diameter.md §9"
  - "papers/phase-space-diameter.md 'References'"
  - "verify/phase_space_diameter.py 'Reciprocity on a rectangle; wave packets (note §5)'"
  - "verify/phase_space_diameter.py 'Where the radiation rectangle is square, lambda = l_P (note §6)'"
  - "review/round5-adjudication.md 'Rulings' R5"
  - "review/round5-adjudication.md 'Rulings' R14"
  - "review/round5-adjudication.md 'Rulings' R15"
  - "review/round5/adjudicator/arb.out 'B10'"
  - "review/round5/manuscript-v1.0.md §5"
  - "review/round5/referee-A/audit-notes.md Step 1"
  - "review/round5/referee-B/audit-notes.md Step 4.3"
  - "HANDOFF.md §4"
---

*Squeezed cosmological perturbations are the quantum states in which [inflation](/wiki/cosmology/early-universe/inflation-and-dilution) leaves the primordial fluctuations of density and of the metric. Each Fourier component of a fluctuation, a mode, behaves as an oscillator. While its wavelength is shorter than the Hubble radius, the distance at which the expansion carries matter away at the speed of light, the mode oscillates in its ground state, with its spreads in field value and in momentum balanced. Once the expansion has stretched the wavelength beyond that radius, the oscillation stops, and the state is stretched along one direction of the mode's phase space and compressed along the other, at a fixed product of the two spreads: a squeezed state, the kind of state that quantum optics makes in light. During inflation the squeezing is about the number of e-folds of expansion since the mode left the Hubble radius, an e-fold being a growth of the universe by the factor e; it reaches about 50 by the end of inflation and is about 100–120 today on the largest observed scales. The note on the program's [phase-space diameter relation](/wiki/cosmology/scale-factor-duality/phase-space-diameter) uses this physics as the observed form of a "distance from self-duality": on the half-plane that labels [Gaussian wave packets](/wiki/phase-space/modular-field/gaussian-states), a squeezed state lies at twice its squeezing from the round ground state. The note also reads an early-chat aspect ratio of 10⁹² as a squeezing of 105.9, a reading that fits the chat's "clock" but not its withdrawn claim of a [square rectangle at a bounce](/wiki/cosmology/scale-factor-duality/square-at-the-bounce).*

**Status:** Established — [T] — the squeezing of inflationary perturbations is literature, and the values on this page are those that the phase-space-diameter note retrieved by live search [S] (`papers/phase-space-diameter.md` §5); round 5's referee A checked them against the papers (`review/round5/referee-A/audit-notes.md`, Step 1). The general explanation is written from general knowledge, with the references it adds from model memory (†). Two steps are the note's own and machine-checked [V]: a squeezed vacuum lies at Siegel distance 2r from the round state, and an aspect ratio of 10⁹² is a squeezing of r = 105.9 (`verify/phase_space_diameter.py`; [the phase-space-diameter script](/wiki/method/verification/phase-space-diameter-script)). The reading of the chat's clock as a mode's squeezing is the note's [D][V] (§6), added after [round 5](/wiki/method/review/round-5) (ruling R14).

## What a squeezed state is [T]

### One oscillator

The ground state of a quantum harmonic oscillator is a Gaussian wave packet. In the units the oscillator sets, its spreads in position and in momentum are equal, Δx = Δp, and their product is the least the uncertainty principle allows, ℏ/2 [T]. Its [Wigner function](/wiki/phase-space/reciprocity/wigner-function), the state drawn on the plane of position and momentum, is a round Gaussian hill. A squeezed state is the same hill stretched by a factor e^r along one direction of that plane and compressed by e^{−r} along the perpendicular one, so its area, and the product of its spreads along the two axes, are unchanged [T]. The number r is the squeeze parameter, and the ratio of the long axis to the short one is e^{2r}. The map that does this is a squeeze of the phase plane, diag(a, 1/a) with a = e^r in axes along the ellipse ([rotations, boosts and squeezes](/wiki/phase-space/reciprocity/symplectic-form#rotations-boosts-and-squeezes)); in quantum mechanics a unitary operator carries it out [T].

In signal terms, a squeezed Gaussian with its axes along x and p is a Gaussian pulse made longer and correspondingly narrower in bandwidth, or shorter and broader, at the same minimal product of duration and bandwidth ([the time–bandwidth product](/wiki/phase-space/reciprocity/fourier-transform#the-timebandwidth-product)) [T]. Quantum optics uses the word for light whose noise in one quadrature, the part of the field that oscillates in phase with a reference wave, is pushed below the vacuum level at the cost of the other quadrature, a quarter-period out of phase (Walls 1983 †) [T].

### A pair of modes

A field in an expanding universe is a sum of Fourier modes, one for each wavevector k, and each mode is an oscillator whose parameters change as the universe expands [T]. The change creates quanta in pairs with opposite wavevectors k and −k, and the state of each pair is a two-mode squeezed state with squeeze parameter r_k [T] (Grishchuk and Sidorov 1990 †). The mechanism is parametric amplification, the one that makes squeezed light in an optical parametric amplifier: a change in an oscillator's parameters, driven there by a pump wave and here by the expansion, amplifies one quadrature and de-amplifies the other [T]. Each mode then holds on average sinh² r_k quanta [T], so a strongly squeezed mode is very highly occupied, the regime in which a quantum field behaves as a classical wave ([particles or waves](/wiki/dark-matter/wave-dark-matter/occupation-number#particles-or-waves-t)).

## How the expansion squeezes the perturbations [T]

### Inside and outside the Hubble radius

Each mode's physical wavelength grows with the scale factor a ([Friedmann cosmology and minisuperspace](/wiki/cosmology/scale-factor-duality/friedmann-cosmology)) [T]. While the wavelength is shorter than the Hubble radius c/H, with H the Hubble rate, the mode oscillates many times in one expansion time; its frequency changes slowly by comparison, and the mode stays in its instantaneous ground state, the vacuum [T]. During [inflation](/wiki/cosmology/early-universe/inflation-and-dilution#inflation-t) H is nearly constant while the wavelengths grow nearly exponentially, so every mode in turn becomes longer than the Hubble radius; this is called leaving the Hubble radius, or crossing the horizon [T]. Outside it the mode no longer oscillates. Its amplitude freezes, while the expansion goes on changing the mode's parameters and squeezes its state further [T].

In the phase-space-diameter note's statement, after a fluctuation's wavelength leaves the Hubble radius during inflation "its state is squeezed relative to its own vacuum", with the squeeze parameter growing as the number of e-folds since the mode left [S] (§5, citing Albrecht, Ferreira, Joyce and Prokopec 1994):

```text
r_k ≃ ln(a/a_k)        a_k: the scale factor at which mode k left the Hubble radius
                       (R_k in Albrecht et al., as the note records)
```

An e-fold is a growth of a by the factor e, so ln(a/a_k) counts the e-folds since the mode left ([what inflation is](/wiki/cosmology/early-universe/inflation-and-dilution#what-it-is)).

### How large the squeezing is

The note gives the squeezing as about 50 at the end of inflation [S] (Martin and Vennin 2016) and about 100–120 today on the largest observed scales [S] (Kiefer and Polarski 2009; Kiefer, Polarski and Starobinsky 1998; Grishchuk 1993) (§5). Round 5's referee A checked each value against its paper (audit notes, Step 1).

Modes "stop squeezing once they re-enter the Hubble radius" (§5). After inflation the Hubble radius grows faster than the wavelengths, so modes re-enter it, the shortest first; a mode that has re-entered oscillates again [T]. The largest scales observed today are the ones that have spent longest outside the Hubble radius [T].

### The classical limit

Strong squeezing, together with decoherence by interaction with other degrees of freedom, is the usual account of why the perturbations, quantum in origin, can be treated as a classical random field [T] (Polarski and Starobinsky 1996 †). In a strongly squeezed state the Wigner ellipse is so elongated that, for measurements of the field amplitude, the state cannot in practice be told apart from a classical spread of field values, each paired with its momentum; the quantum spread across the ellipse is negligible beside the spread along it [T]. Two of the papers the note cites for the values carry the question in their titles: Kiefer and Polarski's "Why do cosmological perturbations look classical to us?" and Kiefer, Polarski and Starobinsky's "Quantum-to-classical transition for fluctuations in the early universe". Martin and Vennin ask whether the anisotropies of the [cosmic microwave background](/wiki/cosmology/early-universe/cosmic-microwave-background) can be shown to be of quantum-mechanical origin (titles from the note's reference list).

### Dependence on the canonical variables

The value of the squeezing is not unique. "Squeezing values depend on the choice of canonical variables" (§5, citing Grain and Vennin 2020 [S]): the squeeze is measured from the mode's vacuum, and a time-dependent change to another pair of field and momentum variables changes which state counts as the reference, while the physical state and its predictions for observations stay the same [T].

### Circuit complexity

A circuit complexity is the length of the shortest sequence of elementary operations that prepares a state from a chosen reference state [T]. For cosmological perturbations one can be built from the squeezing, and in the note's statement "A circuit complexity built from the squeezing grows linearly with the number of e-folds during inflation and falls in the radiation era" [S] (§5, citing Bhattacharyya, Das, Haque and Underwood 2020).

## On the Siegel half-plane [T][D][V]

A one-dimensional Gaussian wave packet ψ_Z(x) ∝ exp(iZx²/2) is labelled by a point Z = X + iY of the upper half-plane, the one-dimensional case of [the Siegel domain](/wiki/phase-space/modular-field/siegel-domain); the program's documents use that domain as the arena of [the modular field](/wiki/phase-space/modular-field/modular-field-z). In units with ℏ = 1 and the round state at Z = i, the note's §5 gives the packet's spreads and its distance from the round state:

```text
Δx² = 1/(2Y),   Δp² = |Z|²/(2Y),   Δx/Δp = 1/|Z|
ds² = (dX² + dY²)/Y²            the half-plane (degree-1 Siegel) metric
d(i, iY) = |ln Y| = |ln(Δx/Δp)|  the distance from i along the imaginary axis
σ_x = e^r/√2  ⇒  d = 2r          a squeezed vacuum in the note's convention
```

On the imaginary axis X = 0 the ellipse has its axes along x and p, and moving along the axis is a squeeze [T]; for X ≠ 0 the ellipse is tilted (§5). A squeezed state with its axes along x and p therefore lies at Siegel distance 2r from the round state, and the aspect ratio of its ellipse is e^{2r} [T][D][V] (`verify/phase_space_diameter.py`: "for Z = iY, sigma_x/sigma_p = 1/Y and the distance |ln Y| = 2r (sigma_x = e^r/sqrt 2)").

Two cautions come with the number (§5). Off the axis, |ln(Δx/Δp)| is smaller than the distance d(i, Z), with equality only on the axis. And the number depends on the metric: the Fubini–Study metric, which measures the distance between quantum states by their overlap [T], is 1/8 of the Siegel metric on Gaussian states, so a path of Siegel length 2r has Fubini–Study length r/√2 [V]. In the note's words, 'A "distance from self-duality" is defined only once its metric and its λ are named.'

The point Z = i is the self-dual point of [Born reciprocity](/wiki/phase-space/reciprocity/born-reciprocity) on these packets. The Fourier transform sends ψ_Z to ψ_{−1/Z}, which is the program's reciprocity Z → −Z⁻¹ on its modular field ([reciprocity as modular inversion](/wiki/phase-space/modular-field/modular-inversion)), and its fixed point Z = i "is the one Gaussian the transform leaves unchanged, the ground state of an oscillator of length λ" (§5). The note's summary table records the distance as "the Siegel distance from Z = i on the slice; 2r in a stated convention" [T][D][V] (§9).

## How the program uses it

### A distance from self-duality without a Born length

The handoff's record of the relation, as the early chat stated it, ends with "aspect ratio today ~10⁹² = a clock measuring distance from self-duality" (`HANDOFF.md` §4). For the radiation of today's observable universe, the note gives that clock a definite form [D][V] (§5). A comoving cell's position extent grows as a and its momentum extent falls as 1/a, so its aspect ratio grows as a², and its point on the half-plane moves away from Z = i by 2 ln(a/a_sd) per axis, where a_sd is the scale factor at which the cell was square. In [Planck units](/wiki/gravity/spin-2-fields/planck-units) the distance today is ln A₀ = 213.5 per axis. The note's assessment: "It reparametrizes ln a and adds no dynamics" (§5).

That aspect ratio is measured in units of a [Born length](/wiki/phase-space/reciprocity/born-length) λ, here the Planck length, and a different λ gives a different ratio. A mode's squeezing has no such dependence, because its reference is the mode's own vacuum: "The aspect ratio in units of λ depends on λ. A version that does not exists and is observed" (§5). It depends instead on the choice of canonical variables ([above](#dependence-on-the-canonical-variables)).

### The squeezed-mode reading of the chat claim

Version 1.0 of the note did not test this reading against the chat claim. Round 5's referee B proposed it (`review/round5/referee-B/audit-notes.md`, Step 4.3), the adjudication accepted it (ruling R14), and version 1.1 adds it to §6 [D][V]: "Read as one perturbation mode's Wigner ellipse (§5), an aspect ratio of 10⁹² is a squeezing of r = 105.9, inside the literature's 100–120 for today's largest scales, and the chat's clock is then the mode's squeezing." The 10⁹² is the chat's round figure; the radiation rectangle's computed aspect ratio is 5.2×10⁹² (§6). The adjudicator's code prints the span of the literature's range (`review/round5/adjudicator/arb.out`, B10):

```text
  squeezed mode, r = 100.0: aspect e^(2r) = 10^86.9
  squeezed mode, r = 105.9: aspect e^(2r) = 10^92.0
  squeezed mode, r = 120.0: aspect e^(2r) = 10^104.2
```

`verify/phase_space_diameter.py` gates the conversion ("a squeezed mode with aspect 1e92 has r = 105.9, inside the literature's 100-120"; [the phase-space-diameter script](/wiki/method/verification/phase-space-diameter-script)).

The reading fits the fourth part of the chat claim, the clock, and not the third, the square rectangle at the bounce: "the mode was round before it left the Hubble radius during inflation, which is not a bounce" (§6). It is one of the readings tested on [Obituary: the square rectangle at the bounce](/wiki/cosmology/scale-factor-duality/square-at-the-bounce), whose record of it reads "A squeezed mode matches the number 10⁹² but was round before it left the Hubble radius, not at a bounce" (§6). The adjudication found that none of the readings added in round 5 changes the withdrawal (ruling R14).

### The complexity sentence

Version 1.0 of the note said of the squeezing's growth, "That growth has been read as a clock", citing Bhattacharyya et al.'s "cosmological complexity" (`review/round5/manuscript-v1.0.md` §5; quoted in referee A's audit notes, Step 1). Both referees found that Bhattacharyya et al. do not use the word "clock", and that the complexity they build from the squeezing falls in the radiation era; ruling R5 upheld them. Version 1.1 credits the reading of squeezing as a count of e-folds to the squeezing literature itself, Albrecht et al. 1994, which the referees had listed among omitted prior art (rulings R5 and R15).

## Standard references

- A. Albrecht, P. Ferreira, M. Joyce, T. Prokopec, "Inflation and squeezed quantum states," Phys. Rev. D 50, 4807 (1994), arXiv:astro-ph/9303001 [S]: the squeezing grows as the number of e-folds since the mode left the Hubble radius.
- J. Martin, V. Vennin, Phys. Rev. D 93, 023505 (2016), arXiv:1510.04038 [S]: about 50 at the end of inflation.
- C. Kiefer, D. Polarski, Adv. Sci. Lett. 2, 164 (2009), arXiv:0810.0087 [S]; C. Kiefer, D. Polarski, A. A. Starobinsky, Int. J. Mod. Phys. D 7, 455 (1998), arXiv:gr-qc/9802003 [S]; L. P. Grishchuk, "Quantum effects in cosmology," Class. Quantum Grav. 10, 2449 (1993), arXiv:gr-qc/9302036 [S]: about 100–120 today on the largest scales.
- J. Grain, V. Vennin, "Canonical transformations and squeezing formalism in cosmology," JCAP 02 (2020) 022, arXiv:1910.01916 [S]: the dependence on the canonical variables.
- A. Bhattacharyya, S. Das, S. S. Haque, B. Underwood, "Cosmological complexity," Phys. Rev. D 101, 106020 (2020), arXiv:2001.08664 [S]: circuit complexity of the squeezed perturbations.
- L. P. Grishchuk, Yu. V. Sidorov, Phys. Rev. D 42, 3413 (1990) †: squeezed states of relic gravitational waves and density perturbations.
- D. Polarski, A. A. Starobinsky, Class. Quantum Grav. 13, 377 (1996) †: semiclassicality and decoherence of cosmological perturbations.
- D. F. Walls, "Squeezed states of light," Nature 306, 141 (1983) †: squeezing in quantum optics.

The [S] entries are the note's, retrieved by live search for it. The † entries are from model memory and unverified.

## Used by

- [The phase-space diameter relation](/wiki/cosmology/scale-factor-duality/phase-space-diameter) — the chat's clock read as a mode's squeezing.
- [Obituary: the square rectangle at the bounce](/wiki/cosmology/scale-factor-duality/square-at-the-bounce) — the squeezed-mode reading, which matches 10⁹² but puts the round state at Hubble exit, not at a bounce.
- [Gaussian wave packets on the Siegel half-plane](/wiki/phase-space/modular-field/gaussian-states) — the distance 2r of a squeezed vacuum from Z = i, and its observed version.
- [Round 5](/wiki/method/review/round-5) — rulings R5, R14 and R15.
- [The phase-space-diameter script](/wiki/method/verification/phase-space-diameter-script) — the check r = 105.9.

## Sources

- `papers/phase-space-diameter.md` §5 — 'A physical version: squeezed perturbations' (the values and their sources), 'Wave packets and the Siegel half-plane', 'Three loci', 'The distance' (d = 2r, the Fubini–Study factor) and 'The clock'; §6 — 'A squeezed mode' and the obituary; §9 — the summary row; 'References' — the cited papers
- `verify/phase_space_diameter.py` 'Reciprocity on a rectangle; wave packets (note §5)' — the distance 2r, the Fubini–Study factor 1/8, ln A₀ = 213.5; 'Where the radiation rectangle is square, lambda = l_P (note §6)' — r = 105.9
- `review/round5-adjudication.md` 'Rulings' R5 — the complexity sentence; R14 — the squeezed-mode reading added; R15 — Albrecht et al. 1994 as omitted prior art
- `review/round5/adjudicator/arb.out` B10 — e^{2r} at r = 100, 105.9 and 120
- `review/round5/manuscript-v1.0.md` §5 — the reviewed text's sentence on the squeezing's growth "read as a clock"
- `review/round5/referee-A/audit-notes.md` Step 1 — the squeezing values checked against their papers; version 1.0's "clock" sentence
- `review/round5/referee-B/audit-notes.md` Step 4.3 — the squeezed-mode reading proposed
- `HANDOFF.md` §4 — the chat claim
