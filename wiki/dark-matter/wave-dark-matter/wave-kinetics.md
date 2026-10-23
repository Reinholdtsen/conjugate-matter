---
title: "Wave kinetics and Bose-star formation"
weight: 20
status: established
description: "Levkov–Panin–Tkachev kinetic condensation: waves in a halo scatter into low-energy states and form Bose-star cores, with a t^{1/2} slowdown of growth."
provenance: [T]
sources:
  - "notes/debt3b-wave-island.md 'Setup'"
  - "notes/debt3b-wave-island.md 'The rate'"
  - "notes/debt3a-stream-stability.md 'Consequences for the predictions table'"
  - "notes/debt3a-stream-stability.md 'Next chunk (3b)'"
  - "notes/debt3c-ufd-endpoint.md 'Sharpened input numbers'"
  - "papers/broken-born-checkpoint-v2.md §9"
  - "papers/broken-born-checkpoint-v2.md ref [13]"
  - "notes/broken-born-program-v1.md §7"
  - "notes/broken-born-program-v1.md §10"
---

*Wave kinetics is the theory of how a field made of many waves with random phases relaxes when the waves scatter off one another. In a dark-matter halo made of a very light boson, the waves interact through gravity, and each scattering moves power toward the lowest-energy modes at a rate that grows with how many quanta those modes already hold. The result is a dense, coherent ground-state core, a Bose star, which forms at the halo's center and then grows. Levkov, Panin and Tkachev (LPT) worked out this kinetic condensation and followed it in simulations. The Broken-Born program's [Debt-3 calculation](/wiki/dark-matter/momentum-clumping) used it as the anchor for a gated version driven by [conjugate matter](/wiki/dark-matter/conjugate-matter)'s self-attraction.*

**Status:** Established — [T: LPT] in the [Debt-3 notes](/wiki/history/documents/debt-3-notes), cited as [13]† in [the checkpoint](/wiki/history/documents/checkpoint) — not machine-checked; calibrating the program's gated rate against Levkov–Panin–Tkachev numerics is an open to-do.

## What wave kinetics describes [T]

When the [occupation number](/wiki/dark-matter/wave-dark-matter/occupation-number) N_occ is large, a halo of light bosons is a classical field: a superposition of waves of many momenta with random relative phases. Its state is summarized by the occupation of each momentum, its spectrum. Weak interactions between the waves make that spectrum evolve. The equation that governs it is a kinetic equation of the Boltzmann type: a collision integral sums over two-wave scatterings, each weighted by the occupations of the modes involved. For bosons those weights carry the Bose factors 1 + N, so when N_occ ≫ 1 the rate is larger than the particle collision rate by a factor of order N_occ. The Debt-3 notes write the estimate as Γ ~ n σ_scat v × N_occ: "relaxation proceeds by wave kinetics — the Boltzmann collision integral with Bose enhancement" (`notes/debt3b-wave-island.md`, 'Setup').

Why scattering condenses the field follows from two conservation laws [T]. A two-wave scattering conserves both the number of quanta and their total energy. A spectrum that relaxes under both constraints sends energy toward high momenta and quanta toward low momenta. Quanta pile up in the lowest modes, and the spectrum develops a narrow peak at the bottom. In the Fourier picture a narrow spectrum is a long, coherent waveform: concentrated in momentum, the field becomes one coherent object in position. Debt 3a describes the gated version of the process as "power flowing into narrow-momentum streams" ('Consequences for the predictions table').

## Gravitational Bose condensation [T]

Levkov, Panin and Tkachev studied the case where gravity is the only interaction. A virialized wave halo, left to relax kinetically, nucleates a Bose star after one relaxation time and then feeds it from the surrounding gas. The Debt-3 notes treat this as the known mechanism. Debt 3a: "The known anchor is Levkov–Panin–Tkachev gravitational Bose condensation (kinetic relaxation with Bose-enhancement factors ∝ N_occ)". Debt 3b, with DM for dark matter: "This is the mechanism LPT established for gravity (Bose condensation of virialized wave DM into solitons); here the gated contact attraction adds a channel" ('Setup').

### The gravitational rate

Debt 3b quotes the gravitational condensation rate as a literature result ('The rate'):

```text
Γ_gr ≈ 8πG²ρ²Λ/(m³σ⁶)        [T: LPT]
```

Here G is Newton's constant, ρ the density, m the boson mass and σ the [velocity dispersion](/wiki/dark-matter/halo-astrophysics/velocity-dispersion); the note does not define Λ. The form of the expression follows from the generic estimate Γ ~ n σ_scat v × N_occ, a reading given here and not in the note [T]. Gravitational scattering of two particles of mass m has the Rutherford form, with a cross-section that scales as (Gm/σ²)² times a Coulomb logarithm, and N_occ = ρ/(m⁴σ³). Multiplying n = ρ/m, that cross-section, the speed σ and N_occ gives G²ρ²/(m³σ⁶) times the logarithm, which suggests that Λ is the Coulomb logarithm of gravitational scattering; the note does not say so. The steep σ⁻⁶ dependence collects three effects: slow particles are deflected more strongly, slow halos crowd their particles into fewer modes, and a slower gas collides less often per unit time, which takes one power back.

### Bose stars [T]

A Bose star is the ground state of a self-gravitating boson field: a coherent lump in which gravity is balanced by the gradient energy of the wave, the "quantum pressure" that resists squeezing a wave into a small region. The balance gives a mass–radius relation in which the radius shrinks as the mass grows, R ∝ ℏ²/(G M m²). In simulations of [fuzzy dark matter](/wiki/dark-matter/wave-dark-matter/fuzzy-dark-matter-bounds) the same objects appear as the solitonic cores at the centers of halos. Once formed, a Bose star grows by absorbing quanta from the surrounding gas, and the growth slows with time. The Debt-3 notes cite "the soliton-growth slowdown seen in LPT-type kinetics (t^{1/2} growth, factor ~10²–10³ in effective rate)" (`notes/debt3c-ufd-endpoint.md`, 'Sharpened input numbers').

If the bosons also attract one another through a self-interaction, a Bose star has a maximum mass, and above it the cycle of collapse and regrowth described on [attractive condensates](/wiki/dark-matter/wave-dark-matter/attractive-condensates) takes over.

### A word with two meanings

In these notes a "soliton" is a Bose-star core, as in the fuzzy-dark-matter literature. It is not the [topological soliton](/wiki/symmetry-breaking/topological-defects#two-meanings-of-soliton-and-the-name-knots) of the program's retired dark-matter candidate, for which see [the soliton obituary](/wiki/dark-matter/candidates/soliton-candidate/obituary).

## How the program uses it

### A gated channel beside gravity

On the program's [wave island](/wiki/dark-matter/momentum-clumping/wave-island), the light end of the conjugate-matter mass range, the waves of χ interact through gravity and through their own gated contact attraction ([the velocity gate](/wiki/dark-matter/conjugate-matter/velocity-gate)). Debt 3b adds the second interaction as a second channel of the same kinetic mechanism and derives its rate, tagged [D, heuristic coefficients]:

```text
Γ_self ≈ c g²ρ² min(σ, v*)⁴/(m³σ⁶),        c = O(5–15)
```

where g is the gated contact coupling (in GeV⁻²) and v\* the gate width in relative velocity. With the gate open (σ ≲ v\*) it is "Γ ≈ c g²ρ²/(m³σ²)". The same generic estimate reproduces that form when gravity's speed-dependent cross-section is replaced by the speed-independent contact cross-section of Debt 3b's conventions, "σ₀ ≡ g²m²/π" ('Setup'); again this is a reading, not a step the note writes out. When the gate is narrow the rate is suppressed by the power law (v\*/σ)⁴. [The checkpoint](/wiki/history/documents/checkpoint) states the rate as "Bose-enhanced, LPT-style [13†]; coefficients [O]" (#11 §9). The derivation, the comparison with orbital stirring and the gravitational floor are on [the gated condensation rate Γ_self](/wiki/dark-matter/momentum-clumping/wave-island/condensation-rate). In brief, Γ_gr "always runs", the gated channel dominates above a coupling of order 10⁻³¹ GeV⁻² for Milky Way numbers, "an easy floor", and "For m ≫ 10⁻²⁰ eV the gravity channel is negligible on Hubble times; the gated channel is the only game" (Debt 3b).

### No timescale refuge

The growth slowdown entered the falsification of [Scenario A](/wiki/dark-matter/momentum-clumping/wave-island/scenario-a). In the [ultra-faint dwarf galaxy](/wiki/dark-matter/halo-astrophysics/dwarf-galaxies) Segue 1, Debt 3c finds a condensation time of about 1.5×10⁴ yr, so that "Over a 10 Gyr lifetime the system has ~6×10⁵ condensation times". Allowing for the slowdown does not change the verdict: "Even granting the soliton-growth slowdown seen in LPT-type kinetics (t^{1/2} growth, factor ~10²–10³ in effective rate), the core is processed through the condensate many times over. There is no timescale refuge." ('Sharpened input numbers'.) The checkpoint rounds the condensation time to "~10⁴ yr" (#11 §9).

## Calibration against the anchor

The numerical coefficients of the gated rate have not been calibrated against Levkov–Panin–Tkachev's numerics. Debt 3a set the condition before the rate was computed: "Anchor scalings against LPT before trusting coefficients" ('Next chunk (3b)'). Debt 3b's header records the result: coefficients "heuristic at O(1)–O(10) level; calibration against Levkov–Panin–Tkachev (LPT) numerics is a flagged to-do." [Program v1](/wiki/history/documents/checkpoint) lists "LPT coefficient calibration" among its literature verifications (`notes/broken-born-program-v1.md` §10 item 8) and calls the coefficients "to calibrate [O]" (§7). The checkpoint marks them "[O]" in §9, but its open-problem list (#11 §14) does not itemize the calibration. The item is kept open on [the gated condensation rate](/wiki/dark-matter/momentum-clumping/wave-island/condensation-rate) and in [open problems](/wiki/status/open-problems).

## References

- The checkpoint's [13]†: D. G. Levkov, A. G. Panin, I. I. Tkachev, "Gravitational Bose–Einstein condensation in the kinetic regime," Phys. Rev. Lett. 121, 151301 (2018); "Relativistic axions from collapsing Bose stars," Phys. Rev. Lett. 118, 011301 (2017). Both are cited from model memory and await [the † literature battery](/wiki/method/literature-battery) (OP10).

Added by the wiki from model memory (†):

- V. E. Zakharov, V. S. L'vov, G. Falkovich, *Kolmogorov Spectra of Turbulence I: Wave Turbulence* (1992)†: kinetic equations for interacting waves.
- H.-Y. Schive, T. Chiueh, T. Broadhurst, "Cosmic structure as the quantum interference of a coherent dark wave," Nature Physics (2014)†: solitonic cores in simulations of fuzzy dark matter.

## Used by

- [The gated condensation rate Γ_self](/wiki/dark-matter/momentum-clumping/wave-island/condensation-rate) — the gated channel added to this mechanism, and the gravitational floor it races.
- [The wave island](/wiki/dark-matter/momentum-clumping/wave-island) — on the island, relaxation is wave-kinetic.
- [Obituary: Scenario A and the ultra-faint-dwarf endpoint](/wiki/dark-matter/momentum-clumping/wave-island/scenario-a) — even with the t^{1/2} slowdown, "There is no timescale refuge."
- [The net theorem](/wiki/dark-matter/momentum-clumping/net-theorem) — its wave legs rest on the gated rate, whose coefficients await calibration against Levkov–Panin–Tkachev numerics.
- [Row 3: the island discriminant](/wiki/predictions/island-discriminant) — its wave side, the (v\*/σ)⁴ law, is the narrow-gate suppression of the wave-kinetic rate.

## Sources

- `papers/broken-born-checkpoint-v2.md` §9, ref [13] — "LPT-style [13†]"; coefficients [O]; the reference
- `notes/debt3b-wave-island.md` 'Setup', 'The rate' — the wave-kinetic rate, the mechanism, the gated rate, the gravitational channel, the calibration to-do
- `notes/debt3a-stream-stability.md` 'Consequences for the predictions table', 'Next chunk (3b)' — Levkov–Panin–Tkachev as the known anchor; power flowing into narrow-momentum streams; anchoring the coefficients
- `notes/debt3c-ufd-endpoint.md` 'Sharpened input numbers' — the t^{1/2} growth slowdown; no timescale refuge in Segue 1
- `notes/broken-born-program-v1.md` §7, §10 — coefficients to calibrate; the calibration listed among literature verifications
