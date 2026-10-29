---
title: "The closed-universe script"
weight: 110
status: method
description: "verify/closed_universe.py recomputes every number of the closed-universe note in one self-contained file: anchors independent of the investigation (CODATA Planck units, a PDG density, exact closed solutions, elliptic averages, the S³ spectrum, a dodecahedral mode, published curvature values, torsion-balance ranges, a calibrated fit), then regression checks in five blocks — τ histories, data bounds, the bimetric sector, momentum space and, since 2026-10-29, the polarization manifold's homotopy with two winding-number anchors of its own — and what it does not recompute: the 96-history grid, more than one crunch phase, the two curvature reductions it takes as input."
provenance: [D, V]
sources:
  - "verify/closed_universe.py"
  - "notes/closed-universe.md header"
  - "notes/closed-universe.md §1–§8"
  - "notes/closed-universe.md §9"
  - "notes/closed-universe.md §10"
  - "review/closed-universe/README.md"
  - "review/closed-universe/critic/d_light_travel.out"
  - "review/closed-universe/analyses/gravity-sector.json"
  - "scripts/check.sh"
  - "CLAUDE.md 'Layout'"
  - "CLAUDE.md 'Method (HANDOFF §5)'"
  - "CLAUDE.md 'Since the handoff'"
  - "review/wiki-build-flags.md items 27 (addendum), 45–54"
  - "review/wiki-build-flags.md item 61"
  - "papers/broken-born-checkpoint-v2.md §14 item 12"
---

*The closed-universe script, `verify/closed_universe.py`, recomputes every number of the note on [a closed Comatter universe](/wiki/cosmology/scale-factor-duality/closed-universe), the program's study of what follows if space is finite and positively curved. The investigation itself ran in scripts outside the repository; this file ports them into one self-contained check that the gate runs. Before it computes anything from the investigation, it reproduces values that do not depend on it: the Planck units of CODATA 2018, the photon density of the Particle Data Group, the exact solutions of a closed universe filled with dust or with dust and radiation, a textbook average over an oscillating field, the vibration spectrum of a three-sphere, the lowest mode of the Poincaré dodecahedral space, two published measurements of the universe's curvature, two published torsion-balance ranges and two published fits of the second data release of the Dark Energy Spectroscopic Instrument. Everything after the anchors is, in the script's own words, a regression check: it shows that the investigation's numbers follow from its inputs, not that the inputs or the model are right. What it does not recompute is the full grid of 96 histories, more than one phase of the field's oscillation at the crunch, and the two curvature terms of the gravity sector, which it takes as input. A last block, added on 2026-10-29, derives the homotopy groups of the space of polarizations, which decide what defects the program's choice of polarization could leave. It computes the maps behind two of the three groups, calibrating its winding integral on two winding numbers from the literature, and matches all three to the standard table; the group behind the point defects follows from standard inputs, one of which the block confirms rather than tests, and the count of textures on a closed universe is argued, not computed.*

**Status:** Method, in force — the note says that "Every number is recomputed in `verify/closed_universe.py`" (note header), and its [V] tags rest on the script — eighth in the list of scripts that [the gate](/wiki/method/verification/the-gate), `scripts/check.sh`, runs. In the run of 2026-10-27 recorded below, all 92 checks passed and the script ended "OK — every number of the closed-universe investigation reproduces." Section F, added on 2026-10-29 under flag 61 in `review/wiki-build-flags.md`, brings the count to 100; in the run of 2026-10-29, also recorded below, all 100 passed and the script ended with the same line. The note itself has not been reviewed.

## What it checks, and for what

The note is `notes/closed-universe.md`, of 2026-10-27, which answers Paul's question of that day on a closed universe. Its results are on three pages: [a closed Comatter universe](/wiki/cosmology/scale-factor-duality/closed-universe) (the premise, the turnaround, the data, how big position space and how small momentum space get, the dual frame, light and counts), [the momentum graviton in a closed universe](/wiki/gravity/momentum-graviton/closed-universe) (the bimetric sector) and [reciprocity on a closed space](/wiki/phase-space/reciprocity/closed-space-reciprocity). The topology that section F checks is also on [Open: point defects of the polarization](/wiki/symmetry-breaking/topological-defects#open-point-defects-of-the-polarization-op12), #11 §14 item 12. The numbers the note computes carry [V] or [D][V], and this script is the machine check behind the [V]; the published figures it quotes carry [S].

The docstring states the scope, the anchors and the inputs:

```text
closed_universe.py — every number of the closed-universe investigation
(notes/closed-universe.md), recomputed and checked. The work was done outside
the repository in executed scripts; this file ports them (it imports none of
them) and is self-contained. The ported sources are named at each section.
Paths such as closed/dynamics/cc.py name scripts in the investigation's work
folder, which is not in the repository; its record (the analyses, the
verdicts, the critic's scripts and grid.csv) is in review/closed-universe/.

Exit code 1 if any check fails. Anchors come first and are independent of the
investigation: [...] Everything else after the anchors is a regression check:
it reproduces the investigation's own numbers and derivations, and is not
independent of them.

Inputs: CODATA 2018 constants; H0 = 67.4 km/s/Mpc, Omega_m = 0.315,
T_CMB = 2.7255 K, three massless neutrinos at (4/11)^(1/3) T; closed means
Omega_k < 0, curvature radius today R0 = c/(H0 sqrt|Omega_k|). Dark energy is
the field tau with V = V0 [1 + cos(tau/f)], f in units of the reduced Planck
mass, thawing from rest at theta_i (measured from the hilltop), V0 shot so that
H(a = 1) = H0 and theta_i shot to a target w0 = w(a = 1). Bimetric sector:
Hassan-Rosen, palindromic beta_n = beta_(4-n), beta0 = -4 beta1 - 3 beta2,
M_f = M_g. Other inputs are typed in with their sources where they are used.
```

The docstring's lines are rewrapped here, and the bracket stands for its list of anchors, set out below. Each check prints `PASS` or `FAIL`, its label and, where there is one, the computed value in brackets; lines that begin with spaces print intermediate values without a check. The failures are collected, and the script lists them and exits with code 1. It imports mpmath, numpy and sympy, the last for the exact algebra.

The closed histories are integrated with an adaptive Dormand–Prince method with event location, in three forms: with ln a as the clock while H² is not small, with time as the clock through H = 0, and, once the field's oscillation is fast compared with the expansion, with the exact average of the oscillation over a period, whose equation of state comes from complete elliptic integrals. The crunch is integrated with the full field (the script's comments). Units are the reduced Planck mass, c = 1 and H₀ = 1.

## The anchors

The rule behind them is root `CLAUDE.md`'s: "An anchor must be independent of the paper (a textbook identity, a published value). A check that reproduces the paper's own number is circular." ([independent anchors](/wiki/method/verification/independent-anchors)). The first block, headed "Anchors (independent of the investigation)", holds 22 checks:

- **Units and densities.** The Planck length, mass, temperature and time against CODATA 2018, to 2×10⁻⁶; ħc against CODATA; the blackbody photon density at 2.7255 K against the Particle Data Group's 410.73 cm⁻³; the reduced Planck energy against its 2.435×10¹⁸ GeV.
- **The integrator against exact solutions.** A closed universe of dust and curvature has the cycloid as its exact solution, and one of dust, radiation and curvature an exact solution in conformal time (textbook: Weinberg 1972 §15.3; Misner, Thorne and Wheeler §27.10, as the code cites them). The integrator must reproduce a_max, t_turn, t_crunch = 2t_turn and a conformal angle of π at the turnaround to 10⁻⁸, at |Ω_k| = 10⁻² and 10⁻³; sympy confirms that the radiation solution solves its equation. The flat ΛCDM age without radiation is checked against its textbook closed form.
- **The oscillating field's average.** The mean equation of state of an oscillating field, which the integrator uses once the oscillation is fast, comes from complete elliptic integrals; the script checks its own arithmetic-geometric-mean evaluation against mpmath's elliptic integrals, and the period and mean w against a direct integration of the pendulum.
- **The three-sphere.** The zonal harmonics have Laplacian eigenvalue ν² − 1 for unit radius; the harmonic polynomials of degree l on ℝ⁴ number (l + 1)² = ν²; the same spectrum follows from S³ = SU(2) with spin l = (ν − 1)/2; and the unit S³ has Ricci scalar 6. These support the momentum spectrum √(ν² − 1)·ħ/R ([how small momentum space gets](/wiki/cosmology/scale-factor-duality/closed-universe#how-small-momentum-space-gets)).
- **The Poincaré dodecahedral space.** From the characters of the binary icosahedral group, whose class sizes must sum to 120, the lowest nontrivial scalar mode is ν = 13, the published value of Aurich, Lustig and Steiner 2005 (astro-ph/0412569).
- **Published curvature.** DESI DR2 with the CMB, Ω_K = 0.0023 ± 0.0011, and Akrami, Alestas and Nesseris, Ω_K = 0.003 ± 0.001, are typed in. DESI is the Dark Energy Spectroscopic Instrument, DR2 its Data Release 2, and CMB the cosmic microwave background.
- **X's range.** The torsion-balance table of Lee et al. 2020, typed in as in [the phase-space-diameter script](/wiki/method/verification/phase-space-diameter-script), must reproduce the experiment's published 38.6 μm and 30 μm; at strength 4/3 it gives λ_X < 37.7 μm and M_X c² > 5.24 meV ([the laboratory bound on X's range](/wiki/gravity/momentum-graviton/range-bound)).
- **The fit's calibration.** The background fit, described under block C, must reproduce two published DR2 results: the flat w₀wₐ fit, w₀ = −0.43 ± 0.22 and wₐ = −1.72 ± 0.64, within one standard deviation, and ΛCDM with free curvature, 0.0023 ± 0.0011, within 0.2 standard deviations and 5% in width; it prints +0.00242 ± 0.00114.

Two literature anchors sit inside block D, where the derivation they test is made: von Strauss et al. 2012's quartic for the bimetric ratio and Könnig 2015's gradient-instability frequency. Block F has two of its own, the winding numbers of SU(2)'s fundamental representation (|W| = 1) and of SO(3) in SO(4) acting on ℝ⁴ (|W| = 4), "with Bott periodicity's stable values for U/O as the table its homotopy groups must match" (docstring), the stable values being those the homotopy groups of U(d)/O(d) take when d is large [T].

## The checks, block by block

The later blocks are labelled B to F and name the investigation's scripts they port. Their check labels carry the note's item numbers, such as B1 or E5; block F's labels, F1 to F4, cite the gravity-sector analysis's claims C35–C38 instead.

### B. Closed τ histories (21 checks)

The block runs four histories in full, from the big bang through the turnaround to the crunch: the representative one (|Ω_k| = 10⁻³, f = 1, w₀ = −0.8), the grid's two extremes (smallest R_max at |Ω_k| = 10⁻², f = 0.2, w₀ = −0.7; largest at 10⁻⁵, 2, −0.95), and the over-constraint partner at |Ω_k| = 10⁻⁴ with the representative's (w₀, wₐ). It regresses them against the investigation's `grid.csv` and outputs ([a closed Comatter universe](/wiki/cosmology/scale-factor-duality/closed-universe)):

- the representative history: a_max = 1726, t_turn = 1.24×10⁶ Gyr, R₀ = 140.7 Gpc, R_max = 2.43×10⁵ Gpc = 7.49×10³⁰ m, and 1.58 mK at the turnaround;
- the grid's ranges, R_max from 4.54×10³ to 1.91×10¹⁰ Gpc and t_turn from about 2.3×10⁴ to 9.8×10¹⁰ Gyr, from the two extremes;
- every history has V₀ > 0 and turns around; a_max = (Ω_m + Ω_d)/|Ω_k|, t_turn = (π/2)(Ω_m + Ω_d)|Ω_k|^{−3/2}/H₀ and t_crunch = 2t_turn; the crunch is kinetic, w → 1; τ's first minimum lies in a = 1.34–18.9 over the grid; |⟨w⟩| ≤ 1.1×10⁻⁷ at the turnaround; Ω_d/Ω_DE,0 ≥ 1.0149;
- the contrasts: τ frozen at the hilltop never turns around, with H/H₀ tending to √Ω_Λ, and sympy shows that with V ≥ 0, H² > 0 whenever k ≤ 0 (flag 27 addendum);
- the over-constraint: at fixed (w₀, wₐ), d ln t_turn/d ln|Ω_k| = −1.5 from the pair at 10⁻³ and 10⁻⁴ (flag 46; [the over-constraint](/wiki/cosmology/dark-energy/over-constraint));
- light: the conformal time from today to the turnaround is π + c√|Ω_k|, and sympy confirms that a closed de Sitter phase adds π/2 from its throat.

### C. Data bounds given closure (11 checks)

- **The bounds.** From the DESI DR2 + CMB value, treated as a Gaussian truncated to Ω_K < 0, the probability of closure is 0.018 and the 95% bound |Ω_k| < 0.00113, from which follow R₀, a_max, R_max, t_turn, 1/a_max, the grain ħc/R_max and the CMB temperature at the turnaround; the same for the cosmic-variance floor |Ω_k| = 10⁻⁴.
- **The fit.** The background fit uses DESI DR2's baryon-acoustic-oscillation table, typed in by the investigation's critic, and DESI's compressed CMB prior; the sound horizon comes from DESI's fitting formula. It has no supernovae. The script replaces the original's Nelder–Mead minimizer with a Levenberg–Marquardt one and reproduces the original's printed χ² profile in Ω_K. It gives Ω_K = 0.00252 ± 0.00119 for the corridor with s = 1.5 (quoted as 0.0025 ± 0.0012), 0.00245 ± 0.00119 for s = 2.0, a probability of closure of 0.017–0.020, and 0.00071 ± 0.00151 with probability 0.32 for w₀wₐ+Ω_K ([what the data say](/wiki/cosmology/scale-factor-duality/closed-universe#what-the-data-say)).

### D. The bimetric sector (19 checks)

In sympy, from the reduced action of the two metrics ([the momentum graviton in a closed universe](/wiki/gravity/momentum-graviton/closed-universe)):

- the potential of the bidiagonal ansatz, the Bianchi constraint with no k, and the y-equation, a quartic that does not depend on k, anchored to von Strauss et al. 2012 (D1);
- the exact relation 2P_g + 3ρ\* = β₁(1 − y)⁴/y, with M̄² = 2M_g², and its leading order, 1 − y = 2(H² + k/a²)/M_X², which is 1.5×10⁻⁶¹ today at the smallest M_X (D2, D3);
- M_X² = 4m²(β₁ + β₂) from the shear mode (D4, flag 5); the broken vacua and their Λ_g (D5, flag 51);
- G_eff → 2G_N as y → 0, the halfway point at 1.55–1.58 TeV, Könnig 2015's eigenfrequency, and the gradient instability above 1.31–1.38 TeV (D6, flags 52 and 53);
- SO(4)-invariant tensors on S³ form a one-dimensional space (D7); a frozen flat reference cannot take k = +1 form, and a fixed scale makes the Bianchi constraint proportional to ȧ (D8);
- the turnaround toy, a_max = 1.588667 with f's lapse 1.226664, regular along the integrated path (D9).

### E. Momentum space and reciprocity (19 checks)

- the fibre: the momentum block of H_Z is Y⁻¹ for any X, so the fibre is flat (E1, flag 48); the grain ħ/R and the lowest momentum √3ħ/R (E2);
- the local exchange: the coefficient −2/3 by quadrature and from the Gaussian moments, and (2/3)(σ/R₀)² = 3.5×10⁻⁵⁵ (E3);
- integrability on T\*S³: every L_θ is Lagrangian, the Frobenius obstruction is ℓ²p sin³θ/R², only θ = 0 is integrable, every θ on T³, and (L/R₀)² = 5.309×10⁻⁵⁵ (E4);
- compact phase spaces: the Künneth argument, Gr̃(2,5) as a Kähler quadric with its reciprocity automorphism, √(R₀ l_P) = 1.489×10⁻⁴ m and the bounds on κc (E5) ([reciprocity on a closed space](/wiki/phase-space/reciprocity/closed-space-reciprocity));
- the photon count of the whole sphere (E6); the symmetric dual-curvature reading and its bounds, with the LHC (Large Hadron Collider) cap (E7, flag 48); the inflationary throat, 2.67×10⁵ l_P, typed in from E_inf < 1.39×10¹⁶ GeV (E8); the a⁻⁶ term below 10⁻¹⁹⁸ after inflation (E9, flag 49); the radius–mass pairing and its aspect ratios (E10).

### F. Topology of the polarization manifold (8 checks)

The block was added on 2026-10-29, when flag 61 was applied. It ports the gravity-sector analysis's `grassmannian_homotopy.py`, which had run only in the investigation's work folder and was not gated, and covers that analysis's claims C35–C38 (`review/closed-universe/analyses/gravity-sector.json`), the last of them argued in a label rather than computed. Λ(4) = U(4)/O(4) is the space of polarizations ([the Lagrangian Grassmannian](/wiki/phase-space/modular-field/lagrangian-grassmannian)). The code's comments give the method: the homotopy follows from the fibration O(4) → U(4) → U(4)/O(4) and standard inputs [T], the homotopy groups of O(4) and U(4), among them π₃(O(4)) = ℤ + ℤ, from left and right multiplication by unit quaternions, and π₃(U(4)) = ℤ, counted by the winding number W[g] = (1/24π²)∫Tr(g⁻¹dg)³ over S³. The script computes the two maps π₁(O(4)) → π₁(U(4)) and π₃(SO(4)) → π₃(U(4)), evaluating W as a sum over a grid on S³.

- **Anchors** [T]: left and right quaternion multiplication by a unit quaternion are orthogonal with determinant 1; SU(2)'s fundamental representation has |W| = 1, unchanged when SU(2) is embedded in U(4); SO(3) in SO(4) acting on ℝ⁴, spin 1 plus spin 0, has |W| = 4, its Dynkin index.
- **F1** (C37): the generators x → qx and x → xq of π₃(SO(4)) have W = −2 and +2 in π₃(U(4)) = ℤ; the image is 2ℤ, and with π₂(O(4)) = 0, π₃(Λ(4)) = ℤ₂.
- **F2** (C35): det² winds once on a loop that closes in Λ(4) and twice on the generator of π₁(U(4)), so π₁(Λ(4)) = ℤ, the Maslov class.
- **F3** (C36): the generator of π₁(SO(4)) = ℤ₂ has determinant winding 0 in U(4). The determinant is 1 on SO(4), so in the label's words the check "confirms an input rather than testing one". π₁(O(4)) → π₁(U(4)) is therefore zero, and with π₂(U(4)) = 0, π₂(Λ(4)) = ℤ₂ "follows by exactness": "the polarization manifold admits point defects". The note tags π₂ [T], and π₁ and π₃ [T][V] (`notes/closed-universe.md` §8).
- **F4** (C38): the three groups match Bott periodicity's stable values for U/O, ℤ, ℤ₂ and ℤ₂ [T]. The label adds the count of textures: maps of S³ into Λ(4), with no base point fixed, fall into the classes of π₃ up to the action of π₁, which is trivial on ℤ₂ because the automorphism group of ℤ₂ is trivial, so [S³, Λ(4)] = Z₂, "two texture classes on a closed universe". The label marks the count "argued, not computed", and the note tags it [D].

The block's comment carries the caveat of the note and of flag 61: on the light Maslov circle alone π₂(S¹) = π₃(S¹) = 0, so the point defects and textures belong to the regime in which the order parameter ranges over all of Λ(4); the strings of τ that π₁ allows exist on the circle too (#11 §14 item 12). The classification also assumes d = 4 and that the U(4) acting on the polarization is global, the closed-universe verifiers' caveats (flag 61). The results are on [a closed Comatter universe](/wiki/cosmology/scale-factor-duality/closed-universe#light-horizons-and-counts) and [Open: point defects of the polarization](/wiki/symmetry-breaking/topological-defects#open-point-defects-of-the-polarization-op12).

## What it does not recompute

The docstring and the code say what was trimmed to keep the run short:

- **Four histories, not the grid.** "The closed histories run only the representative case, the two grid extremes and the over-constraint pair" (docstring). The investigation's dynamics analysis computed 96 histories, kept in `review/closed-universe/grid.csv` (`review/closed-universe/README.md`); the script checks the two extremes against it, so the grid's ranges rest on the grid's extremes being where the investigation found them. The B6 label adds that, grid-wide, c runs from −1.991 to +0.628; the four histories print −1.983955 to +0.615044, which the note gives as −1.98 to +0.62. The critic's output gives −1.984 to +0.628 at |Ω_k| = 10⁻² (`review/closed-universe/critic/d_light_travel.out`).
- **One crunch phase.** The history function is "a port of cc.history, one oscillation phase at the crunch". The note's light-travel result depends on the phase of τ's oscillation, and one of the investigation's two refuted claims came from sampling too few phases (§10); the script does not sample phases.
- **Two curvature reductions taken as input.** In block D the reduced Einstein–Hilbert terms of the two metrics, √−g R(g) with curvature k and the same for f, are written into the code as input ("sqrt(-g) R(g) reduced, curvature k"), not derived there from the metrics. The checks downstream confirm the algebra that follows from them.
- **Rounded inputs.** Some of the quoted numbers were computed from rounded inputs, and block E5 checks them with those inputs; it prints the unrounded values too, which change the third digit of one figure (46.4 against 46.5 E_P). The note quotes 46.5. Block C checks the corridor bounds at the unrounded bound |Ω_k| < 0.001207, which the note's table quotes; the critic had rounded it to 0.00121 first.
- **The literature and the inputs.** Published values are typed in: the DESI tables and fits, the two curvature values, Lee et al.'s table, the inflation bound and the cosmic-variance floor. Whether the cited works say what the note quotes rests on retrieval ([S]), not on the script, and the 10⁻⁴ floor and the exclusion of eternal inflation are not computed.
- **The models.** The fit is a background fit without supernovae, and the corridor approximates τ's histories; a fit of V₀[1 + cos(τ/f)] with full likelihoods is open. The dual Einstein–Hilbert term behind E7 and E9 is a postulate of the record (flag 49). The script checks arithmetic, not the model ([verification checks arithmetic, not the model](/wiki/method/verification/arithmetic-not-model)).
- **Single-agent results.** Four results came from the note's critic alone and were not independently verified (note header): the corridor fit (C2), the integrability result (E4), the Gr̃(2,5) construction (E5) and inflation's π/2 (B6). The script ports the critic's scripts and so reproduces these results rather than verifying them.
- **Block F's inputs and the defects' fate.** The homotopy groups of O(4) and U(4) are standard inputs [T], stated in the code's comments; the script computes the maps between them and compares the result with Bott periodicity's table. The map of F3 is zero because the determinant is 1 on SO(4), so that check confirms an input, and π₂(Λ(4)) = ℤ₂ rests on exactness [T]; the count of texture classes on S³ is argued in F4's label, not computed [D]. Whether a transition produced the point defects and τ-strings, and what became of them, it does not compute: that is open (#11 §14 item 12; `notes/closed-universe.md` §9 item 4).

## The recorded output

The run of 2026-10-27, made while this page was written (about 10 seconds):

```text
== Anchors (independent of the investigation)
PASS  CODATA 2018 Planck length 1.616255e-35 m  [1.616255e-35]
PASS  CODATA 2018 Planck mass 2.176434e-8 kg  [2.176434e-08]
PASS  CODATA 2018 Planck temperature 1.416784e32 K  [1.416784e+32]
PASS  CODATA 2018 Planck time 5.391247e-44 s  [5.391246e-44]
PASS  CODATA 2018 hbar c = 197.3269804 MeV fm  [1.9732698046e-07 eV m]
PASS  PDG: photon number density 410.73 cm^-3 at 2.7255 K  [410.73]
PASS  PDG: reduced Planck energy 2.435e18 GeV  [2.4353e+18 GeV]
PASS  closed dust + curvature, |Omega_k| = 0.01, Omega_m = 1 + |Omega_k|: integrator reproduces the cycloid's a_max = Omega_m/(Omega_m - 1), t_turn = (pi/2) Omega_m/(H0 (Omega_m - 1)^1.5), t_crunch = 2 t_turn and chi_turn = pi to 1e-8  [-1.6e-10, -1.4e-10, -1.6e-10, -1.8e-10]
PASS  closed dust + curvature, |Omega_k| = 0.001, Omega_m = 1 + |Omega_k|: integrator reproduces the cycloid's a_max = Omega_m/(Omega_m - 1), t_turn = (pi/2) Omega_m/(H0 (Omega_m - 1)^1.5), t_crunch = 2 t_turn and chi_turn = pi to 1e-8  [-1.7e-10, -1.3e-10, -1.7e-10, -1.6e-10]
PASS  closed dust + radiation + curvature (|Omega_k| = 1e-3): a_max, t_turn and chi_turn of the exact solution a = A(1 - cos eta) + sqrt(Omega_r/|Omega_k|) sin eta, to 1e-8  [-1.7e-10, -1.3e-10, -1.6e-10]
PASS  sympy: that a(eta) solves (da/deta)^2 = (Omega_r + Omega_m a - |Omega_k| a^2)/|Omega_k|
PASS  flat LCDM without radiation: age H0 t0 = 2/(3 sqrt(Omega_L)) asinh(sqrt(Omega_L/Omega_m)) (textbook)  [0.950985489925]
PASS  averaged field: AGM K(m), E(m) and <w>(m) = 2(E/K - 1 + m)/m - 1 against mpmath's elliptic integrals  [4.4e-16, 7.2e-10]
PASS  pendulum V0(1 - cos(x/f)) integrated directly: period 4K(m)/mass and period-averaged w equal the formulas  [T = 4.4822975018, <w> = -0.0777062554]
PASS  S^3: the zonal harmonic sin(nu chi)/sin(chi) has -Laplacian eigenvalue nu^2 - 1 (unit radius), any nu
PASS  S^3: harmonic polynomials of degree l on R^4 number C(l+3,3) - C(l+1,3) = (l+1)^2 = nu^2 (l = 0..20)
PASS  S^3 = SU(2): -Laplacian = sum (2 J_a)^2 on spin l = (nu - 1)/2 gives nu^2 - 1, (2l+1) x (2l+1) = nu^2 states
PASS  unit S^3 in hyperspherical coordinates has Ricci scalar 6 (textbook)
PASS  Poincare dodecahedral space: the class sizes sum to 120; the lowest nontrivial scalar mode is nu = 13, i.e. k = 12 with eigenvalue k(k + 2) = 168 (Aurich et al. 2005)  [first invariant at j = 6, nu = 13]
      typed in: DESI DR2 + CMB LCDM + Omega_K = 0.0023 +- 0.0011; Akrami-Alestas-Nesseris Omega_K = 0.003 +- 0.001
PASS  the range interpolation reproduces Lee et al.'s published 38.6 um (|alpha| = 1) and 30 um (alpha = 8/3); at alpha = 4/3 it gives lambda_X < 37.7 um, M_X c^2 > 5.24 meV  [37.680 um, 5.2369 meV]
      flat LCDM: chi2 = 15.65, Omega_m = 0.3007, H0 = 68.33 (DR2 DESI+CMB: 0.3027, 68.17); flat w0wa: chi2 = 7.15, w0 = -0.444, wa = -1.661
PASS  fit calibration: flat w0wa best fit within 1 sigma of DR2's DESI + (theta_*, omega_b, omega_bc) result w0 = -0.43 +- 0.22, wa = -1.72 +- 0.64  [w0 = -0.444, wa = -1.661]
PASS  fit calibration: LCDM + Omega_K gives 0.00242 +- 0.00114, within 0.2 sigma and 5% in width of DR2's DESI + CMB 0.0023 +- 0.0011  [+0.00242 +- 0.00114]

== B. Closed tau histories (regression: closed/dynamics/grid.csv, overconstraint.out, contrasts.out, critic/d_light_travel.out)
      representative: |Omega_k| = 1e-3, f = 1, w0 = -0.8: theta_i = 1.4993693881, V0 = 2.4773014872, w0 = -0.8000000000, waT = -0.414626398; a_max = 1726.1267002, t_turn = 1.2438868e+06 Gyr, t_crunch = 2.4877614e+06 Gyr
PASS  representative history reproduces grid.csv: theta_i = 1.4993693881, V0 = 2.4773014872, a_max = 1726.12670, t_turn = 1.24388683e6 Gyr
PASS  B1: a_max = 1726, t_turn = 1.24e6 Gyr, R0 = 140.7 Gpc  [R0 = 140.657 Gpc]
PASS  B1: R_max = 2.43e5 Gpc = 7.49e30 m  [2.4279e+05 Gpc, 7.4918e+30 m]
PASS  B1: T_CMB at the turnaround = T0/a_max = 1.58 mK; atilde_min = 1/a_max = 5.8e-4  [1.5790 mK, 5.7933e-04]
PASS  grid extremes reproduce grid.csv: a_max = 102.052198 (1e-2, 0.2, -0.7) and 1.35935492e7 (1e-5, 2, -0.95)  [102.052198, 1.35935492e+07]
PASS  B3: R_max runs from 4.54e3 to 1.91e10 Gpc and t_turn from about 2.3e4 to 9.8e10 Gyr over the grid  [R_max 4.5392e+03 .. 1.9120e+10 Gpc, t_turn 2.3260e+04 .. 9.7958e+10 Gyr]
      |Omega_k| = 1e-4 at the representative's (w0, wa) = (-0.8, -0.414626398): f = 1.000731895, theta_i = 1.501224780, w0 = -0.8000000000, wa = -0.414626398; a_max = 1.724243e+04, t_turn = 3.929208553e+07 Gyr
PASS  over-constraint pair reproduces overconstraint.out: f = 1.000731895, theta_i = 1.501224780, t_turn = 3.9292086e7 Gyr
PASS  B5: at fixed (w0, wa), d ln t_turn/d ln|Omega_k| = -1.5 (two-point, |Omega_k| = 1e-3 and 1e-4)  [-1.49952]
      representative: |Omega_k| = 0.001, f = 1: Omega_d = 1.4111266, first minimum at a = 2.7362, <w>(turn) = -2.077e-11, t_crunch/t_turn = 1.99999017, w_eff(crunch) = 1.000000, c = -1.5514
      smallest R_max: |Omega_k| = 0.01, f = 0.2: Omega_d = 0.7055211, first minimum at a = 1.3367, <w>(turn) = -1.054e-07, t_crunch/t_turn = 1.99985190, w_eff(crunch) = 1.000000, c = -1.9840
      largest R_max: |Omega_k| = 1e-05, f = 2: Omega_d = 135.6204917, first minimum at a = 18.5013, <w>(turn) = -4.162e-21, t_crunch/t_turn = 2.00000000, w_eff(crunch) = 1.000000, c = +0.6150
      over-constraint 1e-4: |Omega_k| = 0.0001, f = 1.001: Omega_d = 1.4092430, first minimum at a = 2.7367, <w>(turn) = -2.080e-14, t_crunch/t_turn = 1.99999972, w_eff(crunch) = 1.000000, c = -1.5522
PASS  B2: every history has V0 > 0 (so V = 2 V0 sin^2(delta/2f) >= 0 throughout) and turns around
PASS  B2: a_max = (Omega_m + Omega_d)/|Omega_k| to <= 1e-5, Omega_d = rho_tau a^3/3 at the turnaround (Friedmann constraint there < 1e-8)  [-3.1e-08, -8.8e-07, 1.6e-10, -2.9e-09]
PASS  B2: t_turn = (pi/2)(Omega_m + Omega_d)|Omega_k|^-1.5/H0 to 1e-3  [3.8e-06, 1.8e-04, 2.1e-10, 1.2e-07]
PASS  B2: t_crunch = 2 t_turn to 1e-3
PASS  B2: the crunch is kinetic: w_eff -> 1 and the kinetic fraction -> 1 at a = 1e-10
PASS  B2: tau's first minimum lies in a = 1.34-18.9 (grid range 1.3367-18.939)
PASS  B2: |<w>| <= 1.1e-7 at the turnaround  [largest 1.054e-07]
PASS  B2: Omega_d/Omega_DE,0 >= 1.0149, Omega_DE,0 = 1 - Omega_m - Omega_r + |Omega_k|  [2.05731, 1.01527, 198.00969, 2.05726]
PASS  B4: tau frozen at the hilltop (theta_i = 0, V = 2 V0 = Lambda), |Omega_k| = 1e-2: H > 0 all the way to a = 1e8, H/H0 -> sqrt(Omega_Lambda) (contrasts.out: 0.833611704)  [H/H0 = 0.833611704]
PASS  B4: and H^2 = 0 has no positive root for that history (quartic in a)
PASS  B4 (sympy): with V >= 0, H^2 = rho/3 - k/a^2 > 0 whenever k <= 0, so flat and open universes never turn around
PASS  B6: conformal time from today to the turnaround = pi + c sqrt|Omega_k|, with c = -1.98 to +0.62 in the four histories (grid-wide, critic/d_light_travel.out: -1.991 to +0.628)  [-1.551434, -1.983955, +0.615044, -1.552160]
PASS  B6 (sympy): closed de Sitter R = cosh(Ht)/H from its throat: eta = 2 arctan(tanh(Ht/2)) solves d eta/dt = 1/R and tends to pi/2

== C. Data bounds given closure (port of critic/g_answer_numbers.py and f_corridor_curvature_fit.py)
      DESI DR2 + CMB: |Omega_k| < 0.001129: R0 > 132.39 Gpc, a_max > 886.9, R_max > 1.1741e+05 Gpc = 2.2416e+65 l_P, t_turn > 6.0154e+05 Gyr, 1/a_max < 1.1276e-03, hbar c/R_max < 5.4465e-38 eV, T_CMB(turn) < 3.0732 mK
PASS  C1: DESI DR2 + CMB truncated to Omega_K < 0: P(closed) = 0.018, |Omega_k| < 0.00113
PASS  C1: R0 > 132.4 Gpc, a_max > 887, R_max > 1.174e5 Gpc = 2.242e65 l_P, t_turn > 6.015e5 Gyr
PASS  C1: 1/a_max < 1.128e-3, hbar c/R_max < 5.446e-38 eV, T_CMB(turnaround) < 3.073 mK
      LCDM   : chi2 min 11.31; dchi2 -0.002:14.873 -0.001:8.832 +0.000:4.344 +0.001:1.402 +0.002:0.000 +0.003:0.130 +0.004:1.784 +0.005:4.956 +0.006:9.638 +0.007:15.821  -> Omega_K = +0.00242 +- 0.00114, P(closed) = 0.0172, |Omega_k| < 0.001166
      corr1.5: chi2 min 11.27; dchi2 -0.002:14.906 -0.001:8.871 +0.000:4.383 +0.001:1.436 +0.002:0.000 +0.003:0.024 +0.004:1.438 +0.005:4.161 +0.006:8.105 +0.007:13.177  -> Omega_K = +0.00252 +- 0.00119, P(closed) = 0.0168, |Omega_k| < 0.001207
      corr2.0: chi2 min 10.83; dchi2 -0.002:13.688 -0.001:8.231 +0.000:4.095 +0.001:1.339 +0.002:0.000 +0.003:0.088 +0.004:1.584 +0.005:4.440 +0.006:8.585 +0.007:13.933  -> Omega_K = +0.00245 +- 0.00119, P(closed) = 0.0200, |Omega_k| < 0.001236
      w0wa   : chi2 min 6.90; dchi2 -0.005:13.277 -0.004:9.330 -0.003:5.979 -0.002:3.300 -0.001:1.365 +0.000:0.245 +0.001:0.000 +0.002:0.673 +0.003:2.286 +0.004:4.831 +0.005:8.262 +0.006:12.469  -> Omega_K = +0.00071 +- 0.00151, P(closed) = 0.3191, |Omega_k| < 0.002526
PASS  C2: corridor (w_a = -s(1 + w0), w0 >= -1) + Omega_K: s = 1.5 gives 0.00252 +- 0.00119 (= 0.0025 +- 0.0012), s = 2.0 gives 0.00245 +- 0.00119
PASS  C2: P(closed) = 0.017-0.020 (s = 1.5, 2.0); 95% bound given closure |Omega_k| < 0.001207 (s = 1.5)  [0.0168, 0.0200; s = 2.0 bound 0.00124]
PASS  C2: the corridor result lies within 1 sigma of both published values (DESI DR2 0.0023 +- 0.0011; Akrami et al. 0.003 +- 0.001)
      corridor + Omega_K (s = 1.5): |Omega_k| < 0.001207: R0 > 128.03 Gpc, a_max > 829.5, R_max > 1.0620e+05 Gpc = 2.0275e+65 l_P, t_turn > 5.4408e+05 Gyr, 1/a_max < 1.2056e-03, hbar c/R_max < 6.0218e-38 eV, T_CMB(turn) < 3.2859 mK
PASS  C2: at the corridor bound: R0 > 128.0 Gpc, a_max > 829.5, R_max > 1.062e5 Gpc, t_turn > 5.441e5 Gyr
PASS  C2: 1/a_max < 1.206e-3, grain < 6.022e-38 eV, T < 3.286 mK
PASS  C2: in the same fit w0wa + Omega_K gives +0.00071 +- 0.00151, P(closed) = 0.32  [dchi2 at -0.003: 5.979 (selection edge 6)]
      cosmic-variance floor: |Omega_k| < 0.000100: R0 > 444.80 Gpc, a_max > 10000.1, R_max > 4.4480e+06 Gpc = 8.4919e+66 l_P, t_turn > 2.2788e+07 Gyr, 1/a_max < 9.9999e-05, hbar c/R_max < 1.4377e-39 eV, T_CMB(turn) < 0.2725 mK
PASS  C3: floor |Omega_k| = 1e-4: R0 > 444.8 Gpc, a_max > 1e4, R_max > 4.448e6 Gpc, t_turn > 2.279e7 Gyr
PASS  C3: grain < 1.438e-39 eV, T < 0.273 mK
      [9.1 s]

== D. Bimetric sector (ports of gravity-sector/bimetric_flrw.py, proportional_closed.py, y_epochs.py, higuchi_gradient.py, s3_harmonics.py, turnaround_toy.py and critic/c_second_frame.py)
      minimal M_X (anchors): lambda_X < 37.680 um, M_X c^2 > 5.2369 meV
PASS  potential of the bidiagonal ansatz: N a^3 sum beta_n e_n(sqrt(g^-1 f)) = N U_N + X U_X
PASS  Bianchi constraint: adot EL_a - N dE_N/dt = 3 m^2 M_g^2 (beta1 a^2 + 2 beta2 a Y + beta3 Y^2)(N Ydot - X adot) (up to sign), with no k
PASS  D1: on the dynamical branch (Ydot = X adot, y = Y/a) both Friedmann equations depend on k only through H^2 + k/a^2, so the algebraic y-equation (a quartic) does not depend on k
PASS  anchor: that quartic is von Strauss et al. 2012's (arXiv:1111.1655) with M_* = M_f/M_g, times m^2/y^2
PASS  program branch: rho_*(y) = (1 - y^2)(beta1 y^2 + (4 beta1 + 6 beta2) y + beta1)/(3y); H^2 + k/a^2 = m^2 (P_g(y)/3 + rho_*), P_g(1) = 0
PASS  D2: exact, all y: 2 P_g + 3 rho_* = beta1 (1 - y)^4/y, i.e. 3 Mbar^2 (H^2 + k/a^2) = rho + (Mbar^2 M_X^2/8)(beta1/(beta1 + beta2))(1 - y)^4/y with Mbar^2 = 2 M_g^2
PASS  D3: y = 1 - rho_*/(4(beta1 + beta2)) + O(rho_*^2) and (H^2 + k/a^2)/m^2 = rho_*/2 + 0 rho_*^2, so 1 - y = 2(H^2 + k/a^2)/M_X^2 at leading order (and 3(2 M_g^2)(H^2 + k/a^2) = rho)
PASS  D3: today, at the minimal M_X: 1 - y = 1.5e-61 (1.507e-61 flat limit; 1.522e-61 at Omega_k = -0.01; exact branch = leading order 2 H0^2/M_X^2)  [1.507e-61, 1.522e-61]
PASS  D4: potential at O(shear^2) = (1/2)(c beta1 + 2c^2 beta2 + c^3 beta3) sum d_i^2; the massive shear mode has m_FP^2 = m^2 K (1 + M_g^2/(M_f^2 c^2)), which at c = 1, M_f = M_g, beta3 = beta1 is M_X^2 = 4 m^2 (beta1 + beta2)
PASS  proportional backgrounds f = u^2 g (palindrome): P_g(u) = u^2 P_f(u) iff u(u - 1)(u + 1)(beta1 u^2 + (3 beta2 - beta0) u + beta1) = 0, for any k
PASS  D5: every broken vacuum (u != 1) has Lambda_g = m^2 P_g(u) = -3 m^2 (beta1 + beta2)(u - 1)^2 = 18 m^2 u (beta1 + beta2)^2/beta1
      e.g. beta1 = -1, beta2 = 2: u = 0.12702, 7.87298, Lambda_g/m^2 = [-2.2863, -141.7137] (bimetric_flrw.out: -2.2863, -141.7137)
PASS  D6: as y -> 0 (rho_* ~ beta1/(3y)), (H^2 + k/a^2)/(m^2 rho_*) -> 1, i.e. H^2 + k/a^2 -> rho/(3 M_g^2): G_eff -> 2 G_N
      G_eff halfway (M_eff^2 = 1.5 M_g^2) at the minimal M_X, g* = 106.75: s = 0: y = 0.1482, H/M_X = 0.7694, T = 1.5760 TeV; s = 1: y = 0.0988, H/M_X = 0.7457, T = 1.5515 TeV
PASS  D6: G_eff is halfway between G_N and 2 G_N at T = 1.55-1.58 TeV (s = 1, 0; quoted as ~1.5 TeV)
PASS  D6: Konnig 2015 eq. (eigenfreq) on the program branch: omega^2/(k/calH)^2 -> 2w + 1 at high density (r -> 0), so the scalar gradient instability needs w > -1/2
      gradient-instability crossover (unstable above): w = 0.33, s = -0.5: r_c = 0.5159, T = 1309 GeV, H/M_X = 0.469; w = 0.33, s = 0: r_c = 0.4062, T = 1350 GeV, H/M_X = 0.502; w = 0.33, s = 1: r_c = 0.3141, T = 1370 GeV, H/M_X = 0.518; w = 0.33, s = 10: r_c = 0.1665, T = 1377 GeV, H/M_X = 0.519; w = 0, s = -0.5: r_c = 0.4841, T = 1332 GeV, H/M_X = 0.489; w = 0, s = 0: r_c = 0.3855, T = 1362 GeV, H/M_X = 0.513; w = 0, s = 1: r_c = 0.3022, T = 1376 GeV, H/M_X = 0.523; w = 0, s = 10: r_c = 0.1640, T = 1377 GeV, H/M_X = 0.520
PASS  D6: the gradient instability (radiation or dust) operates above T = 1.31-1.38 TeV, i.e. H/M_X = 0.47-0.52 (~1.3 TeV, H ~ 0.5 M_X)
PASS  D7: SO(3)-invariant symmetric 2-tensors at a point of S^3 (the isotropy of SO(4)) form a space of dimension 1 (the round metric), with no invariant vectors: an SO(4)-invariant f is -X^2 dt^2 + Y^2 gamma_(k=+1)  [dim 1, vectors 0]
PASS  D8: f = -X^2 dt^2 + Y^2 gamma_(k=+1) has R^chi_(theta chi theta) = (X^2 + Ydot^2) sin^2(chi)/X^2, never zero: a flat reference cannot be put in k = +1 form
PASS  D8: with a fixed scale (Ydot = 0) the Bianchi constraint is -3 m^2 M_g^2 (beta1 a^2 + 2 beta2 a Y0 + beta3 Y0^2) adot: proportional to adot
      toy: a_max = 1.588667 (integrated 1.588667), y = 0.895602, X = 1.226664, dY/da = 1.226664; max relative residuals of the g and f Friedmann equations 4.4e-15, 3.9e-15; min X on the path 1.22666
PASS  D9: through adot = 0 the f lapse is regular: a_max = 1.588667, X = dY/da = 1.226664 at the turnaround, X > 0 on the path, both Friedmann constraints hold along the integrated path
      [13.0 s]

== E. Momentum space and reciprocity (ports of verify-minisuperspace-derivation/d5_fibre_and_measure.py, momentum-space/compact_reciprocity.py, critic/e_polarization_integrability.py, b_compact_phase_space.py, a_dualcurv_conventions.py, h_misc.py, minisuperspace/closure_epochs.py, radius_mass_pairing.py, dynamics/context.py)
PASS  E1: the generalized metric H_Z = [[Y + X Y^-1 X, X Y^-1], [Y^-1 X, Y^-1]] has p-p block Y^-1 = g^-1 for any X (d = 2, det H_Z = 1): the fibre metric over a point does not depend on p, so the fibre is flat (k~ = 0; Ricci scalar of the S^3 fibre metric at a point = 0)
PASS  E2: S^3 momentum spectrum p = hbar sqrt(nu^2 - 1)/R (from the anchor's eigenvalues): lowest sqrt(3) hbar/R, spacing -> hbar/R (the grain; hbar c/R as an energy)
PASS  E3: <p^2> of a Gaussian of geodesic width sigma on S^3_R = (3 hbar^2/4 sigma^2)(1 - (2/3)(sigma/R)^2 + ...): coefficient -2/3 by quadrature and from the Gaussian moments; (2/3)(sigma/R0)^2 = 3.5e-55 at sigma = 1 m, |Omega_k| = 1e-2  [c = -0.666644 (sigma/R = 0.01), -0.666665 (0.003); 3.539e-55]
      [L_1, L_2] outside L_theta on T*S^3: [ell**2*p2*sin(theta)**3/R**2, -ell**2*p1*sin(theta)**3/R**2, 0]
PASS  E4: on T*S^3 every L_theta = span{cos(theta) d/dp_a + sin(theta) ell H_a} is Lagrangian; the Frobenius obstruction is ell^2 p sin^3(theta)/R^2
PASS  E4: L_theta is integrable at theta = 0 and not at pi/4 or pi/2 (the mirror) on T*S^3; on T^3 every theta is
PASS  E4: the curvature measure (L/R0)^2 at L = 1 m, |Omega_k| = 1e-2 is 5.309e-55  [5.3086e-55]
PASS  E5: Kunneth: for X a rational homology 3-sphere, H^2(X x M) = H^2(M) for every closed 3-manifold M, so every class [omega] is pulled back from M and [omega]^3 = 0: X x M is not symplectic (S^3 x S^3 has b2 = 0)
PASS  E5: Gr~(2,5) = SO(5)/(SO(2) x SO(3)) is the quadric Q3 in CP^4 (z = u + i v), where the Fubini-Study form is non-degenerate (Kahler); the SO(5) reciprocity automorphism (pi/2 in the (4,5) plane: X -> P, P -> -X, M_45 fixed) has residual ~1e-16  [1.1e-15, residual 8.7e-17]
PASS  E5: its Born length sqrt(R0 l_P) = 1.489e-4 m at |Omega_k| = 1e-2  [1.4894e-04 m]
PASS  E5: kappa c >= 46.4 E_P (X range 37.7 um) and >= 1.72e11 E_P (#13's maximum force, lambda <= 6.195e-10 m) today (|Omega_k| = 1.13e-3); 4.1e4 and 1.5e14 E_P at the turnaround floor R_max = 1.174e5 Gpc  [4.6430e+01, 1.7197e+11, 4.1195e+04, 1.5258e+14]
      with unrounded inputs (|Omega_k| < 0.0011287, R_max = 1.17415e+05 Gpc): 46.46 E_P (37.7 um), 46.51 E_P (lambda_X = 37.68 um), 1.7206e+11; floor 4.1200e+04, 1.5260e+14 E_P
PASS  E5: with unrounded inputs the X-range figure is 46.5 E_P, the others unchanged at their quoted digits
PASS  E6: photons in the whole S^3, n_gamma 2 pi^2 R0^3 = 2.1e91 (|Omega_k| = 1e-2) to 6.6e95 (1e-5) (context.out: 2.0961e91, 6.6285e95)  [2.0961e+91, 6.6285e+95]
PASS  E7 (sympy): with a atilde = C, the a^-6 term over M_P^2 is (R_sd/R)^6 and dual over our curvature is (R_sd/R)^2, R_sd = sqrt(C) ell, in either normalization (ell = lambda or R0)
      |Omega_k| = 1e-2: Omega_nu1 = 1.23632e-05, a_BBN = 1.6764e-10, a_end = 1.3659e-29; R_sd <= 1.5675e+17 m (BBN), 3.0292e+25 m (N_eff); lambda <= 1.2775e-06 m (LHC cap + N_eff + BBN), 1.9856e-49 m (+ inflation)
PASS  E7: at |Omega_k| = 1e-2: BBN bound R_sd <= 1.568e17 m, N_eff bound 3.029e25 m; the LHC 6.8 TeV cap plus N_eff plus BBN needs lambda <= 1.278e-6 m, adding standard inflation (N* = 55) lambda <= 1.986e-49 m
PASS  E7: for lambda = sqrt(l_P c/H0) the window is empty: the LHC cap needs R_sd >= 5.779e18 m > 1.568e17 m  [5.7790e+18 m]
PASS  E8: with E_inf < 1.39e16 GeV (Soman et al. 2025, r < 0.036) and H_inf^2 = 8 pi G E_inf^4/(3 (hbar c)^3 c^2): c/H_inf = sqrt(3/8pi)(E_P/E_inf)^2 l_P = 2.67e5 l_P, and atilde = l_P H_inf/c <= 3.75e-6 there (lambda = l_P)  [c/H_inf = 4.3080e-30 m = 2.6654e+05 l_P; atilde = 3.7518e-06]
PASS  E9: the a^-6 term after inflation is largest at its end and below 1e-198 for |Omega_k| <= 1e-2 (log10 = -198.39 at 1e-2; later epochs smaller as (l_P/R)^6)  [log10 = [-207.39, -204.39, -201.39, -198.39]]
      (the bound is on the a^-6 term, the only dual term at k~ = 0; under the symmetric reading k~ = k the dual curvature over ours is (l_P/R)^2 = 10^-66.13 at the end of inflation)
PASS  E10: (D_x/l_P)/(D_p/(m_P c)) = f R c^2/(G M) = f (4/3pi)/(1 + (HR/c)^2), hbar-free; at H = 0, G M/c^2 = (3 pi/4) R (the cycloid's R_max = 4 G M/(3 pi c^2))
PASS  E10: the aspect ratio at a turnaround spans 4/(3 pi) = 0.4244 (D_x = R) to 8/3 (D_x = 2 pi R) across conventions  [[0.4244, 0.8488, 1.3333, 2.6667]]

wall time 16.0 s

OK — every number of the closed-universe investigation reproduces.
```

The run of 2026-10-29, made after the labels of F3 and F4 were revised (wall time 10.9 s), printed every line of the anchors and of blocks B to E as above except two timings, 4.8 s and 7.1 s in place of 9.1 s and 13.0 s, and then section F:

```text
== F. Topology of the polarization manifold (port of gravity-sector/grassmannian_homotopy.py; gravity-sector C35-C38; flag 61)
PASS  F anchor: x -> q x and x -> x q are quaternion multiplication by a unit quaternion, orthogonal with det 1
PASS  F anchor: SU(2)'s fundamental representation has |W| = 1 [T]  [W = -1.000179]
PASS  F anchor: embedding SU(2) in U(4) leaves W unchanged  [W = -1.000179]
PASS  F anchor: SO(3) in SO(4) acting on R^4 (spin 1 plus spin 0) has |W| = 4, its Dynkin index [T]  [W = -4.000714]
PASS  F1: the generators x -> q x and x -> x q of pi_3(SO(4)) = Z + Z have W = -2 and +2 in pi_3(U(4)) = Z; the image is 2Z and pi_2(O(4)) = 0, so pi_3(Lambda(4)) = Z2 (C37)  [W = -2.000357, +2.000357]
PASS  F2: det^2 winds once on the loop t -> diag(e^(i pi t), 1, 1, 1), which closes in Lambda(4) because diag(-1, 1, 1, 1) is in O(4), and twice on the generator of pi_1(U(4)): pi_1(Lambda(4)) = Z, the Maslov class (C35)  [+1.000000, +2.000000]
PASS  F3: the generator of pi_1(SO(4)) = Z2 has det winding 0 in U(4) (det = 1 on SO(4), so this confirms an input rather than testing one); pi_1(O(4)) -> pi_1(U(4)) is therefore zero and, with pi_2(U(4)) = 0, pi_2(Lambda(4)) = Z2 follows by exactness (C36): the polarization manifold admits point defects  [+0.000000]
PASS  F4: pi_1, pi_2, pi_3 of Lambda(4) as derived in F1-F3 match Bott periodicity's stable values for U/O, Z, Z2, Z2 [T]; free classes of maps S^3 -> Lambda(4) are pi_3 modulo the pi_1 action, trivial on Z2 since Aut(Z2) is trivial, so [S^3, Lambda(4)] = Z2, two texture classes on a closed universe (C38; argued, not computed)  [('Z', 'Z2', 'Z2')]

wall time 10.9 s

OK — every number of the closed-universe investigation reproduces.
```

An earlier run the same day, made when section F was first described here, printed the same values under earlier labels of F3 and F4. They did not say that F3 confirms an input or that F4's count of textures is argued, not computed, and F4 gave the count from S³'s being simply connected rather than from the action of π₁.

## Sources

- `verify/closed_universe.py` — the docstring with its scope, anchors and inputs; the integrator and its three forms; every check and label; the typed-in tables and values; the trims named in the docstring and the code ("one oscillation phase at the crunch"; the reduced √−g R terms); its output — the 92 checks of the run of 2026-10-27 and the 100 of the run of 2026-10-29 recorded above; section F's docstring sentence, comments and labels
- `notes/closed-universe.md` header — "Every number is recomputed in `verify/closed_universe.py`" and the note's status; §1–§8 — the numbers the script reproduces, §8 the topology and its tags (π₁ and π₃ [T][V], π₂ [T], the texture count [D]); §9 item 4 — the defects' fate, open; §10 — the refuted claim about light travel and the phases of τ's oscillation
- `review/closed-universe/README.md` — the investigation's record and the 96 histories of `review/closed-universe/grid.csv`; `review/closed-universe/critic/d_light_travel.out` — the critic's light-travel ranges; `review/closed-universe/analyses/gravity-sector.json` — claims C35–C38, which section F checks
- `scripts/check.sh` — the script's place in the gate
- `CLAUDE.md` 'Layout' — the script listed as "the closed-universe note"; 'Method (HANDOFF §5)' — the anchor rule; 'Since the handoff' (2026-10-29) — section F gates the homotopy
- `review/wiki-build-flags.md` items 27 (addendum) and 45–54 — "Arithmetic is checked in `verify/closed_universe.py`"; item 61 — the point defects, the ungated script, and section F as its fix
- `papers/broken-born-checkpoint-v2.md` §14 item 12 — the polarization's defects, the open problem the section's groups bear on, "with the maps behind them gated" and the caveats d = 4 and a global U(4)
