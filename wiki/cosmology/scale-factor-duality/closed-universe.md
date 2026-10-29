---
title: "A closed Comatter universe"
weight: 110
status: alive
description: "What spatial closure, k = +1, implies for the program: nothing derives it, but with V₀[1 + cos(τ/f)] ≥ 0 the turnaround of row 5 needs it, and the data disfavour it at about 2σ in the program's model class; position space has only lower bounds on its largest size, momentum space stays flat and only becomes discrete, and a compact momentum space would be a new postulate."
provenance: [D, V]
sources:
  - "notes/closed-universe.md §1"
  - "notes/closed-universe.md §2"
  - "notes/closed-universe.md §3"
  - "notes/closed-universe.md §4"
  - "notes/closed-universe.md §7"
  - "notes/closed-universe.md §8"
  - "notes/closed-universe.md §9"
  - "notes/closed-universe.md §10"
  - "verify/closed_universe.py 'Anchors (independent of the investigation)'"
  - "verify/closed_universe.py 'B. Closed tau histories'"
  - "verify/closed_universe.py 'C. Data bounds given closure'"
  - "verify/closed_universe.py 'E. Momentum space and reciprocity'"
  - "verify/closed_universe.py 'F. Topology of the polarization manifold'"
  - "review/closed-universe/README.md"
  - "review/closed-universe/preregistration.md"
  - "review/wiki-build-flags.md items 27 (addendum), 43, 46, 48, 49, 50, 54"
  - "review/wiki-build-flags.md item 61"
  - "review/round5-adjudication.md 'Rulings' R11"
  - "papers/phase-space-diameter.md §6"
  - "papers/broken-born-checkpoint-v2.md §10"
  - "papers/broken-born-checkpoint-v2.md §13 row 5"
  - "papers/broken-born-checkpoint-v2.md §14 item 12"
  - "CLAUDE.md 'Since the handoff'"
---

*A closed universe is one whose space is finite in volume and curved like the surface of a sphere, one dimension up: the spatial curvature is positive, k = +1, and a traveller going straight ahead would in principle return to the start. The closed-universe note of 2026-10-27 works out what closure would mean for the Comatter program. Nothing in the program derives closure, but the program's dark-energy potential never goes negative, and with such a potential only a closed universe stops expanding and falls back; the turnaround that the program identifies with the [conjugate bounce](/wiki/cosmology/scale-factor-duality/conjugate-bounce) therefore needs a closed universe. Current data, fitted with the program's own class of dark-energy models, disfavour closure at about two standard deviations. If the universe is closed, the data set only a minimum on its largest size, not a maximum. Momentum space does not close with it: the allowed momenta become discrete, as a string of fixed length holds only certain wavelengths, and their spacing is finest at the turnaround.*

**Status:** Alive — computed, not reviewed. The note's results carry [D][V], its data [S], its prior art [T] and [S]; every number is recomputed by `verify/closed_universe.py` ([the closed-universe script](/wiki/method/verification/closed-universe-script)), and the note states that its results were checked by independent verifiers and a completeness critic and have not been through a blind review round (`notes/closed-universe.md` header). The reading of Paul's question is an assumption the note states. The note bears on flags 27 (addendum), 43, 46, 48, 49, 50 and 54 in `review/wiki-build-flags.md`, which await Paul's ruling, and on flag 61, applied on 2026-10-29, which added the polarization's point defects and gated the maps behind its homotopy groups.

## The question and the reading

Paul asked on 2026-10-27: "Presumably a comatter universe is closed. Work out the cosmological consequences wrt generalized general relativity. How small does momentum space get? How big does position space get? Anything else of interest." (note §1).

The note reads the question as follows, and marks the reading as an assumption (§1):

- "Generalized general relativity" is the program's gravity on its generalized metric H: H = diag(g, g⁻¹) in the vacuum, with [a·ã = 1](/wiki/cosmology/scale-factor-duality/cosmological-constraint) (#11 §5, §10); the massive [momentum graviton X](/wiki/gravity/momentum-graviton) in the palindromic Hassan–Rosen branch at background ratio u = 1 ([the laboratory bound on X's range](/wiki/gravity/momentum-graviton/range-bound)); the dark-energy field [τ](/wiki/cosmology/dark-energy/tau-quintessence) with V = V₀[1 + cos(τ/f)]; and the lab notebook's dual-frame minisuperspace ([Friedmann cosmology and minisuperspace](/wiki/cosmology/scale-factor-duality/friedmann-cosmology#the-programs-extension-a-second-scale-factor)).
- "Closed" means spatial curvature k = +1, so the curvature density parameter Ω_k is negative. The note writes Ω_K, with a capital, for the values the survey fits quote.
- Born's reciprocal relativity with a momentum space of fixed curvature radius is not explored; one result bears on it ([reciprocity on a closed space](/wiki/phase-space/reciprocity/closed-space-reciprocity)).

Its conventions are H₀ = 67.4 km/s/Mpc and Ω_m = 0.315, and the curvature radius today is R₀ = c/(H₀√|Ω_k|) (§1). In a closed [Friedmann universe](/wiki/cosmology/scale-factor-duality/friedmann-cosmology#the-homogeneous-universe-t) the curvature term enters the expansion equation with the sign opposite to an energy density, H² = 8πGρ/3 − k/a² [T], so a closed universe can reach H = 0 with a positive total density.

## Nothing derives closure [S][D][V]

- **No source derives it.** Two independent searches of arXiv, INSPIRE and the web found no derivation of a closed universe from [Born reciprocity](/wiki/phase-space/reciprocity/born-reciprocity) (§2).
- **Born went the other way.** Born 1938 starts from Einstein's closed universe and gives momentum space a hypersphere to match, with its radius b fixed from the classical electron radius (§2; [Born's papers](/wiki/phase-space/reciprocity/born-reciprocity#borns-papers)).
- **The compact moduli do not bound the universe.** The space of polarization frames is compact, but this does not bound the universe's size: on the branch β₁ > 0 of the bimetric sector, the ratio y = Y/a of the two metrics' scale factors stays in (0, 1] while Y grows with a [V] ([the momentum graviton in a closed universe](/wiki/gravity/momentum-graviton/closed-universe)).

The note's pre-registration had expected closure to be "natural for the program". It is not: nothing derives it (§10).

## The turnaround needs k = +1 [D][V]

**Flat and open universes never turn around.** With V ≥ 0, H² > 0 at every epoch when k ≤ 0, so a flat or an open universe expands forever (§2). The potential V₀[1 + cos(τ/f)] has minimum zero for V₀ > 0, which is the conflict recorded on [Open: the sign of V(τ) and the turnaround](/wiki/cosmology/dark-energy/potential-sign) (flag 27 in `review/wiki-build-flags.md`).

**In a closed universe the turnaround happens with V ≥ 0 throughout** (§2):

1. τ thaws from near the hilltop and passes its potential minimum, at a = 1.34–18.5 in the histories recomputed;
2. it then oscillates about the minimum, and an oscillating field averages to the pressure-free behaviour of dust: |⟨w⟩| ≤ 1.1×10⁻⁷ at the turnaround;
3. curvature then reverses the expansion.

With τ frozen at the hilltop there is no turnaround (§2). The flag's addendum of 2026-10-27 draws the consequence for the record: #11 §10's "eventually goes negative" and the handoff's "eventual negative V ⇒ turnaround" name the wrong cause, and [row 5](/wiki/predictions/fate-of-expansion), the identification of the turnaround with the conjugate bounce, exists only if k = +1 (flag 27 addendum; note §2). [Round 5](/wiki/method/review/round-5)'s ruling R11 had already noted that a closed universe can turn around without negative energy (`review/round5-adjudication.md`; `papers/phase-space-diameter.md` §6).

### Size and timing [D][V]

```text
a_max    = (Ω_m + Ω_d)/|Ω_k|
t_turn   = (π/2)(Ω_m + Ω_d)|Ω_k|^(−3/2)/H₀
t_crunch = 2 t_turn
```

Here a_max is the largest scale factor, with a = 1 today; t_turn the time of the turnaround and t_crunch that of the final collapse. Ω_d is τ's dust-like density, referred to today; it satisfies Ω_d ≥ Ω_DE,0, the dark-energy fraction today, so a_max ≳ 1/|Ω_k| (§2). The crunch is driven by τ's kinetic energy, with w → 1; it is not the time-reverse of the bang (§2). The script recomputes four histories and checks each formula against them ([the closed-universe script](/wiki/method/verification/closed-universe-script)).

### The conditions [D][V]

The turnaround needs (§2):

- a_max ≥ Ω_m/|Ω_k|;
- at H = 0, ρ_m + 2ρ_r + 4K − 2V ≥ 0, where K is τ's kinetic energy density.

The second is the condition that the acceleration is not positive at the maximum of a. Round-5 ruling R11 states that a closed turnaround exists but does not state these conditions (flag 50).

### Prior art [T]

Recollapse of a closed universe with oscillating quintessence is published: Barrow 1987 †; Tipler et al., gr-qc/0003082, §7 [S] (§2; flag 50). The τ potential itself is the pseudo-Nambu–Goldstone potential of Frieman, Hill, Stebbins and Waga 1995 (astro-ph/9505060) [S], which neither #1 nor #11 cites (flag 54; [axion-like fields](/wiki/cosmology/dark-energy/axion-like-fields)).

### The over-constraint moves [D][V]

The [dark-energy over-constraint](/wiki/cosmology/dark-energy/over-constraint) counts three observables, (w₀, wₐ, t_turn), against two parameters, (f, τᵢ). At fixed (w₀, wₐ), t_turn ∝ |Ω_k|^{−3/2}, so Ω_k is a third input (§2; flag 46). Ω_k is measurable, so the over-constraint moves to (f, τᵢ, Ω_k) rather than vanishing; but the data bound t_turn only from below (next section), so the turnaround time cannot test the count (§2).

## What the data say

**Published values [S]** (§2):

- DESI DR2 with the cosmic microwave background (CMB), in ΛCDM with free curvature: Ω_K = 0.0023 ± 0.0011 (arXiv:2503.14738, Table 5). DESI is the [Dark Energy Spectroscopic Instrument](/wiki/cosmology/dark-energy/desi), DR2 its Data Release 2, and ΛCDM the standard model of a cosmological constant plus cold dark matter.
- Exponential quintessence with free curvature: Ω_K = 0.003 ± 0.001 (Akrami, Alestas and Nesseris, arXiv:2504.04226, abstract).

A positive Ω_K is the open side; closure is Ω_K < 0.

**The program's own model class [V; the critic's fit, one agent].** The note approximates τ's histories by the [thawing corridor](/wiki/cosmology/dark-energy/thawing-and-freezing) wₐ = −s(1 + w₀) with w₀ ≥ −1 and fits it, with Ω_K free, to DESI DR2's distances plus DESI's compressed CMB prior (§2):

- The fit uses the background only, with no supernovae. It reproduces DR2's published flat w₀wₐ fit and its ΛCDM+Ω_K value.
- Ω_K = +0.0025 ± 0.0012 for s = 1.5 and +0.00245 ± 0.00119 for s = 2.0.
- The probability of closure is 0.017–0.020.

**The wrong proxy.** The family w₀wₐ+Ω_K, with the [CPL](/wiki/cosmology/dark-energy/cpl-parametrization) form w(a) = w₀ + wₐ(1 − a), gives Ω_K = +0.00071 ± 0.00151 in the same fit, with probability of closure 0.32. Its looser bound comes from the phantom crossing, w₀ + wₐ < −1 at w₀ > −1. The program's w ≥ −1 forbids that crossing (flag 43; [the no-phantom bound](/wiki/cosmology/dark-energy/no-phantom-bound)), so w₀wₐ+Ω_K is not a proxy for the program's model (§2).

**Limits of measurement [S].** Curvature below |Ω_k| ≈ 10⁻⁴ is not measurable against cosmic variance (Leonard, Bull and Allison 2016, arXiv:1604.01410). A measured closed curvature with |Ω_k| > 10⁻⁴ would exclude eternal inflation in our past (Kleban and Schillo 2012, arXiv:1202.5037; Guth and Nomura 2012, arXiv:1203.6876) (§2).

**Result.** "Closure is a requirement of the turnaround story, not a consequence of the program. In the program's model class the data disfavour it at about 2σ." (§2). The fit is a background fit without supernovae; a fit of the actual potential against full likelihoods is open (below).

## How big position space gets [V]

A closed universe reaches a largest size and recollapses. The flat limit is |Ω_k| → 0, so the data, which only bound the curvature's size, set lower bounds on the largest size and no upper bound: the flatter the universe, the larger it grows before turning around (§3). The bounds below are the 95% bound on |Ω_k| given closure, with the posterior treated as a Gaussian truncated to Ω_K < 0 and a_max ≥ (Ω_m + Ω_DE,0)/|Ω_k|:

| Input | \|Ω_k\| | R₀ today | a_max | R_max | t_turn |
| --- | --- | --- | --- | --- | --- |
| DESI DR2 + CMB, ΛCDM+Ω_K | < 0.00113 | > 132.4 Gpc | > 886.9 | > 1.174×10⁵ Gpc = 2.242×10⁶⁵ l_P | > 6.015×10⁵ Gyr |
| Corridor + Ω_K fit (s = 1.5) | < 0.001207 | > 128.0 Gpc | > 829.5 | > 1.062×10⁵ Gpc | > 5.441×10⁵ Gyr |
| Cosmic-variance floor | = 10⁻⁴ | > 444.8 Gpc | > 10⁴ | > 4.448×10⁶ Gpc | > 2.279×10⁷ Gyr |

R_max is the curvature radius at the turnaround, l_P the Planck length and a Gyr a billion years.

**A representative history** (|Ω_k| = 10⁻³, f = M̄_P, w₀ = −0.8), with M̄_P the reduced Planck mass (§3):

- a_max = 1726 and t_turn = 1.24×10⁶ Gyr;
- R₀ = 140.7 Gpc and R_max = 2.43×10⁵ Gpc = 7.49×10³⁰ m;
- the temperature of the [cosmic microwave background](/wiki/cosmology/early-universe/cosmic-microwave-background) at the turnaround is 1.58 mK.

Across |Ω_k| = 10⁻⁵–10⁻², f = 0.2–2 M̄_P and w₀ = −0.95 to −0.7, R_max runs from 4.54×10³ to 1.91×10¹⁰ Gpc and t_turn from about 2.3×10⁴ to 9.8×10¹⁰ Gyr (§3).

**The smallest size [D][V].** The closed universe's smallest radius is set before the hot big bang. An inflationary de Sitter throat, the narrowest point of a closed [de Sitter](/wiki/cosmology/dark-energy/de-sitter-space) phase, has radius c/H_inf = 2.67×10⁵ l_P for an inflation scale at the bound the diameter note uses, E_inf < 1.39×10¹⁶ GeV (from a tensor-to-scalar ratio r < 0.036) (§3; [inflation and reheating](/wiki/cosmology/early-universe/inflation-and-dilution)).

## How small momentum space gets

The note distinguishes three readings of the question, of which only the second gives physical numbers (§4).

### Shape: the momentum fibre stays flat [D][V]

In the record's geometry the momentum block of H is Y⁻¹, the same at every momentum p, for any X. So the [momentum fibre](/wiki/phase-space/reciprocity/momentum-fibers#flat-fibers-on-a-curved-base) over each point is flat ℝ³, with dual curvature k̃ = 0, and k = +1 does not induce k̃ = +1 (§4). The dictionary's "closed dual space ⇒ negative ΔN_eff" is therefore not a consequence of closure (flag 48; [row 10](/wiki/predictions/early-universe-step)).

What closure does to momentum is make it discrete. A wave on a finite space must fit it, as a string of fixed length holds only certain wavelengths. On the three-sphere S³ of radius R the momentum spectrum is √(ν² − 1)·ħ/R, with ν a whole number, so the spacing of allowed momenta is of order ħ/R (§4). On the Poincaré dodecahedral space, a closed space with the local geometry of S³ and a different topology, the lowest nontrivial scalar mode is ν = 13 [V; anchor: Aurich et al. 2005].

### Scale: smallest at the turnaround [V]

The momentum-space scale factor ã = 1/a is smallest when a is largest: ã(turnaround)/ã(today) = 1/a_max (§4). At the 95% bounds given closure:

| Input | 1/a_max | grain ħc/R_max | T_CMB at the turnaround |
| --- | --- | --- | --- |
| DESI DR2 + CMB, ΛCDM+Ω_K | < 1.128×10⁻³ | < 5.446×10⁻³⁸ eV | < 3.073 mK |
| Corridor + Ω_K fit | < 1.206×10⁻³ | < 6.022×10⁻³⁸ eV | < 3.286 mK |
| Cosmic-variance floor | 10⁻⁴ | 1.438×10⁻³⁹ eV | 0.273 mK |

There is no lower bound: after the turnaround ã grows without bound into the crunch. Absolute values of ã are a normalization: with k̃ = 0 the comoving unit C is a gauge choice (§4).

### The conjugate picture [D][V]

Read through [reciprocity](/wiki/phase-space/reciprocity/born-reciprocity) with a [Born length](/wiki/phase-space/reciprocity/born-length) λ, ρ_λ, our position S³ of radius R becomes a momentum S³ of radius ħR/λ², which is largest at the turnaround. Our discrete momenta become an unbounded position lattice of spacing λ²/R (§4). In wave terms: a waveform confined to a ring has a comb for its spectrum, and the exchange carries the ring into momentum space and the comb into position space.

## The symmetric reading: dead unless postulated [D][V]

A compact momentum space would be a new postulate (§4). Its symmetric reading sets the dual curvature equal to ours, k̃ = k, with vM̃² = M_P², M̃ being the dual Planck mass of the [lab notebook's dual gravity term](/wiki/cosmology/scale-factor-duality/duality-dictionary#the-dual-gravity-term). Both the a⁻⁶ term and the dual curvature are then fixed by a single self-dual radius R_sd. At |Ω_k| = 10⁻² (§4):

- [Big Bang nucleosynthesis](/wiki/cosmology/early-universe/big-bang-nucleosynthesis) (BBN) requires R_sd ≤ 1.568×10¹⁷ m, and N_eff, the effective number of neutrino species, requires R_sd ≤ 3.029×10²⁵ m;
- the observed momentum range sets a minimum on R_sd; the 6.8 TeV protons of the Large Hadron Collider (LHC), together with N_eff and BBN, then need λ ≤ 1.278×10⁻⁶ m;
- adding standard slow-roll inflation needs λ ≤ 1.986×10⁻⁴⁹ m;
- for λ = √(l_P c/H₀) the window is empty.

The reading also contradicts the record's k̃ = 0, and it rests on the underived dual Einstein–Hilbert term (below). The note's verdict: "It is dead unless Paul adds a compact momentum space deliberately." (§4). No program document ever asserted the symmetric reading; the record keeps k̃ as an optional knob of row 10 (flag 48, audit), so the wiki records the reading's failure here and not on an obituary page.

## The dual frame: what closure fixes and what it does not

**The term is underived [O].** The dual Einstein–Hilbert term in ã, with its mass M̃, is used in #1 §6 under a [D] tag, but no document derives it from the geometric action S_H. The a⁻⁶ step in G_eff of #11 §10 and row 10 rests on it (§7; flag 49). Until it is derived, every bound on the dual frame tests a postulate.

**Only two combinations are physical [D][V].** Under the record's dictionary only vM̃²C³, the coefficient of the a⁻⁶ term, and vM̃²k̃C, the dual curvature, are physical, so "M̃ = M_P" constrains nothing unless the comoving unit C is fixed. Closure fixes the normalization a = R/λ, but not the a⁻⁶ coefficient (§7).

**With the record's normalization** (C = 1, M̃ = M_P, λ = l_P) [D][V] (§7):

- the a⁻⁶ term is below 10⁻¹⁹⁸ of the total after inflation, for |Ω_k| ≤ 10⁻²; at k̃ = 0 it is the only dual term;
- an inflationary throat has c/H_inf = 2.67×10⁵ l_P, so ã ≤ 3.75×10⁻⁶ there; the self-dual point a = ã is never reached after inflation begins.

**The radius–mass pairing [D][V].** Pairing the radius R with the total mass M = ρ·2π²R³/c² gives G·M/c² = (3π/4)R at H = 0, and the aspect ratio at a turnaround spans 4/(3π) to 8/3 across conventions. This is the closed Friedmann equation at H = 0, with ħ cancelling, and the obituary of "square exactly at the bounce" stands (§7; [Obituary: the square rectangle at the bounce](/wiki/cosmology/scale-factor-duality/square-at-the-bounce); [the phase-space diameter relation](/wiki/cosmology/scale-factor-duality/phase-space-diameter)).

## Light, horizons and counts

A closed universe can be crossed (§8).

- **Light [V].** The conformal time from today to the turnaround is π + c·√|Ω_k|, with c = −1.98 to +0.62 in the four histories recomputed. Conformal time measures the angle light travels on the three-sphere, and π is the angle to the antipode, so light emitted today reaches our antipode near the turnaround.
- **Inflation [D][V; the critic's, one agent].** A closed de Sitter phase starting at a throat adds π/2 of conformal time. With it the whole S³ is in causal contact by about a_max/2, and light circles the universe in every history.
- **Entropy bounds [D][V, review record].** The Fischler–Susskind bound fails as the particle horizon reaches the antipode, at a ≈ a_max. Bousso's covariant bound holds.
- **Photons [V].** The number of CMB photons in the whole universe is finite: n_γ·2π²R₀³ = 2.1×10⁹¹ at |Ω_k| = 10⁻² to 6.6×10⁹⁵ at 10⁻⁵. It is conserved after electron–positron annihilation.
- **Topology [D].** S³ carries two homotopy classes of polarization texture, [S³, Λ(4)] = Z₂, Λ(4) being the space of polarizations ([the Lagrangian Grassmannian](/wiki/phase-space/modular-field/lagrangian-grassmannian)); the count follows from π₃(Λ(4)) = ℤ₂ [T][V] and is argued, not computed. The same manifold has π₁(Λ(4)) = ℤ [T][V] and π₂(Λ(4)) = ℤ₂ [T], the second following by exactness. Selecting the polarization can therefore leave strings of the Maslov phase τ, which exist on the light Maslov circle too, and, where the order parameter ranges over the whole manifold, point defects, the monopole type ([topological defects](/wiki/symmetry-breaking/topological-defects#open-point-defects-of-the-polarization-op12)). On the light circle alone π₂ = π₃ = 0, and neither the point defects nor the textures exist there. All of this assumes d = 4 and that the U(4) acting on the polarization is global, the verifiers' caveats (flag 61). `verify/closed_universe.py` section F gates the maps behind the groups: its check F3 confirms an input rather than testing one, and F4 matches the groups to Bott periodicity's table and states the texture count as "argued, not computed" ([the closed-universe script](/wiki/method/verification/closed-universe-script#f-topology-of-the-polarization-manifold-8-checks)). X's lowest tensor modes on S³ are the L = 2 modes, those of Bianchi IX [D].

## The gravity sector and reciprocity

Two further parts of the note have their own pages:

- [The momentum graviton in a closed universe](/wiki/gravity/momentum-graviton/closed-universe) (note §6): with its second metric dynamical, X's reference metric closes with the same k and stays aligned, the turnaround is regular, the effective strength of gravity doubles in the early universe, passing the halfway point at T ≈ 1.55–1.58 TeV, and a scalar gradient instability operates above about 1.3 TeV.
- [Reciprocity on a closed space](/wiki/phase-space/reciprocity/closed-space-reciprocity) (note §5): the global exchange of position and momentum fails on a closed space while the local one holds, only the position polarization is integrable, and no product of a closed position space and a closed momentum space is a phase space.

## What is open

The note's §9 lists [O]:

1. **Derive the dual Einstein–Hilbert term from S_H.** Every bound on the dual frame, including #11 §10's a⁻⁶ step and row 10, currently tests a postulate (flag 49).
2. **Fit the program's model properly.** V₀[1 + cos(τ/f)] plus Ω_K against full CMB, baryon-acoustic-oscillation and supernova likelihoods, with the Cobaya and CAMB codes. It decides the premise: the background fit above has no supernovae.
3. **The remaining calculations:** inflation and the bimetric sector together (G_eff = 2G_N during inflation, two light gravitons); the energy splitting between the ±K_ref polarizations that closure induces; perturbations, and X's L = 2 modes, through the recollapse.
4. **Defects of the polarization** (added 2026-10-29, flag 61). If a transition in the early universe selected the polarization, the ℤ₂ point defects and the τ-strings above could form at it; the gravity-sector analysis lists their fate as open. Whether such a transition happened, what it left, and whether the point defects would pose a monopole problem of the program's own are not computed. They are defects of the program's own order parameter, unlike conjugate-sector solitons, whose existence depends on gauge content the record does not specify. #11 v2.3 lists the question as §14 item 12 ([Open: point defects of the polarization](/wiki/symmetry-breaking/topological-defects#open-point-defects-of-the-polarization-op12)).

The root `CLAUDE.md` lists the first two, and Artigas, Mielczarek and Rovelli 2019 as a lead, as "Open from the closed-universe note, not queued", and the fourth among those "Open from the monopole discussion, not queued". All four are on [open problems and the queue](/wiki/status/open-problems).

## Record of the investigation

**Method** (§1; `review/closed-universe/README.md`). A pre-registration was sealed before any agent was dispatched (`review/closed-universe/preregistration.md`, SHA-256 5b1fb233…). Five analyses followed (observations, dynamics, gravity sector, minisuperspace, momentum space), each with two verifiers working from the extracted claims only, and a critic ruled on the tensions between them. Tally: 469 claim checks, 403 confirmed, 48 corrected, 2 refuted, 16 not reached. The analyses, verdicts and scripts are in `review/closed-universe/`.

**Refuted along the way** (§10). Two intermediate claims of the analysts were refuted before the note was written; neither was ever a claim of the record, so neither has an obituary page:

- that light from the big bang never circles the universe in six histories: the grid had sampled only two independent phases of τ's oscillation, and with eight phases every history completes the circuit in some phase; the point is moot once inflation is included;
- that the Fischler–Susskind bound fails at a ≈ 4×10⁻¹⁷ during the collapse: the estimate assumed a horizon of 1 radian, while the horizon reaches the antipode at the turnaround.

**Corrected** (§10). "A doubly compact reciprocal phase space must be torus-like" is wrong: Gr̃(2,5) is a counterexample ([reciprocity on a closed space](/wiki/phase-space/reciprocity/closed-space-reciprocity)). The bounds first quoted for "how big" used the w₀wₐ+Ω_K family and central rather than closure-conditional bounds.

**The pre-registration scored** (§10). Confirmed: turnaround if and only if k = +1, the size and timing (8 of 8 matching histories), the radius–mass pairing, no over-constraint without Ω_k, and the Z₂ textures. Confirmed and strengthened: that reciprocity breaks globally and that nothing observable follows from the finite volume. The data numbers were confirmed, without the forecast anticipating that w₀wₐ+Ω_K is the wrong proxy. Partly wrong: the pre-registered weakest link, since the normalization is a gauge choice and row 10's knob survives as a postulate; and the expected problem in the gravity sector, since the Higuchi bound holds during inflation and the gradient instability is the problem. The expected overall answer called closure "natural for the program", which it is not. The method of sealed forecasts is on [pre-registration and its calibration record](/wiki/method/review/pre-registration).

## Sources

- `notes/closed-universe.md` §1 — the question, the reading [assumption], the method and the conventions; §2 — closure underived, the turnaround needing k = +1, size and timing, the conditions, the prior art, the over-constraint and the data; §3 — the bounds on the largest size, the representative history and the throat; §4 — the three readings of momentum space and the symmetric reading; §7 — the dual frame and the radius–mass pairing; §8 — light, horizons and counts, and the topology of the polarization (the textures [D], π₁ and π₃ [T][V], π₂ [T], and the caveats d = 4 and a global U(4)); §9 — what is open, item 4 the polarization's defects; §10 — the record and the pre-registration scored
- `verify/closed_universe.py` — every number above: the anchors (the S³ spectrum, the dodecahedral mode, the published curvature values, the fit's calibration), section B (the τ histories, size and timing, the contrasts, light), section C (the bounds given closure and the corridor fit), section E (the fibre, the grain, the symmetric reading, the throat, the dual terms, the radius–mass pairing, the photon count) and section F (the maps behind the homotopy of Λ(4), and the two texture classes, argued)
- `review/closed-universe/README.md` — how the investigation ran, its tally and the 96 histories of `review/closed-universe/grid.csv`; `review/closed-universe/preregistration.md` — the sealed forecast
- `review/wiki-build-flags.md` items 27 (addendum), 43, 46, 48, 49, 50 and 54 — the flags this page bears on, with their audits; awaiting Paul's ruling; item 61 — the polarization's point defects and τ-strings, applied on 2026-10-29
- `papers/broken-born-checkpoint-v2.md` §14 item 12 — the homotopy groups behind the polarization's defects [T], with the maps gated in section F, and their fate [O]
- `review/round5-adjudication.md` 'Rulings' R11 and `papers/phase-space-diameter.md` §6 — a closed universe can turn around without negative energy
- `papers/broken-born-checkpoint-v2.md` §10, §13 row 5 — "eventually goes negative" and the row the turnaround tests
- `CLAUDE.md` 'Since the handoff' — the note's results and its open items, not queued; the polarization's defects among the monopole discussion's open items (2026-10-29)
