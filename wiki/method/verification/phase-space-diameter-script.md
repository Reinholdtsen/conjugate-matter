---
title: "The phase-space-diameter script"
weight: 100
status: method
description: "verify/phase_space_diameter.py recomputes every number the phase-space-diameter note computes, against anchors independent of it (CODATA 2018 Planck units, Particle Data Group densities and dark-energy scale, a Bose integral, a published horizon, two published torsion-balance limits): its blocks in order, the checks it labels as identities or arithmetic of quoted factors, the independent recomputations, the round-5 additions and the later tightening, and what it leaves unchecked."
provenance: [D, V]
sources:
  - "verify/phase_space_diameter.py"
  - "papers/phase-space-diameter.md header"
  - "papers/phase-space-diameter.md §3–§8"
  - "papers/phase-space-diameter.md 'References'"
  - "papers/phase-space-diameter.md provenance note"
  - "notes/phase-space-diameter-worklog.md 'Status'"
  - "review/round5-adjudication.md 'Rulings'"
  - "review/round5-adjudication.md 'Revisions for v1.1 (all accepted; applied 2026-10-26)'"
  - "review/round5-adjudication.md 'Pre-registration scored'"
  - "review/round5/referee-A/audit-notes.md Step 2, Step 3"
  - "review/round5/referee-B/audit-notes.md Step 2, Step 3, Step 5"
  - "review/round5/adjudicator/arb.out"
  - "scripts/check.sh"
  - "CLAUDE.md 'Layout'"
  - "CLAUDE.md 'Method (HANDOFF §5)'"
  - "review/wiki-build-flags.md item 38"
  - "review/wiki-build-flags.md items 49, 51"
---

*The phase-space-diameter script, `verify/phase_space_diameter.py`, recomputes every number computed in the note on [the phase-space diameter relation](/wiki/cosmology/scale-factor-duality/phase-space-diameter), the program's study of how the size of the universe in position is related to its size in momentum. Before it computes anything from the note, it reproduces published values that do not depend on the note: the Planck units of CODATA 2018, the photon and entropy densities and the dark-energy scale given by the Particle Data Group, a standard integral of blackbody radiation and the distance to the edge of the observable universe; in its last block, beside the bound that uses them, it reproduces two limits from a laboratory test of gravity at short range. Its checks follow the note section by section, from the blackbody identity to the consequences for the program, among them the bound on the range of the momentum graviton. Some are exact symbolic identities, most recompute a quoted number from stated inputs, and the script itself labels a few as an identity or as arithmetic of factors quoted from elsewhere. A separate agent and both referees of the round-5 review recomputed the numbers with their own code and inputs. What no script here checks is whether the cited sources say what the note quotes, and whether the program's vacuum has the background ratio u = 1 that the bound assumes.*

**Status:** Method, in force — the note defines [V] as "machine-verified by `verify/phase_space_diameter.py`" (note header), and the numbers it computes carry that tag — the last script in the list that [the gate](/wiki/method/verification/the-gate), `scripts/check.sh`, runs. In the run of 2026-10-26 all 85 checks passed and the script ended "OK — every number the phase-space-diameter note computes reproduces."

## What it checks, and for what

The note is `papers/phase-space-diameter.md`, version 1.1. It shows that the chat-only relation D_x·D_p = h·N^{1/3} is an identity of blackbody statistics, withdraws the claim that the universe's position–momentum rectangle was square at a bounce ([Obituary: the square rectangle at the bounce](/wiki/cosmology/scale-factor-duality/square-at-the-bounce)), sets out what [Born reciprocity](/wiki/phase-space/reciprocity/born-reciprocity) does to such rectangles, identifies a length at which a cosmic box is symmetric under the exchange ([the self-dual cosmic box](/wiki/cosmology/scale-factor-duality/self-dual-cosmic-box)), shows that the program cannot use that length ([Obituary: the self-dual length as a program scale](/wiki/cosmology/scale-factor-duality/self-dual-length-obituary)), and derives [a laboratory bound on the range of the momentum graviton X](/wiki/gravity/momentum-graviton/range-bound). The numbers the note computes carry [V], [D][V] or [T][V], and this script is the machine check behind the [V]; the figures it quotes from the literature carry [S].

The docstring states the scope, what it leaves out, and the inputs:

```text
phase_space_diameter.py — every number that papers/phase-space-diameter.md (the
phase-space-diameter note) computes, recomputed and checked. Figures the note
quotes from the literature (Egan and Lineweaver's entropies, the squeezing
values, FKGLM's estimates) are not recomputed, except where a check below
reproduces them; the torsion-balance limits are typed in from the source table.

    .venv/bin/python verify/phase_space_diameter.py

Exit code 1 if any check fails. Anchors come first and are independent of the
note: CODATA 2018's published Planck units, the PDG photon and entropy
densities and dark-energy scale, a Bose integral evaluated two ways, a
published comoving horizon, and the two published limits of Lee et al. 2020
that the exclusion-table interpolation must reproduce.

Inputs: CODATA 2018 constants; Planck 2018 cosmology (H0 = 67.4 km/s/Mpc,
Omega_m = 0.315), T_CMB = 2.7255 K, three massless neutrinos at
(4/11)^(1/3) T, flat, Omega_Lambda = 1 - Omega_m - Omega_r. Standard Model
g_s = 106.75 at high temperature. The radiation rectangle is a sphere of
blackbody photons: D_x its diameter, D_p twice the mean photon momentum.
```

PDG is the Particle Data Group, and FKGLM is Freidel–Kowalski-Glikman–Leigh–Minic, the four authors of the Born-geometry estimates the note quotes. Each check prints `PASS` or `FAIL`, its label and, where there is one, the computed value in brackets; the failures are collected, and the script lists them and exits with code 1. It uses three numerical libraries: mpmath for the integrals (the horizon distances and the Bose integrals), numpy for a numerical Fourier transform and the matrix work, and sympy for exact algebra.

Most checks compare by rounding: a check passes when the computed value, rounded to the digits the note quotes, equals those digits. The photon number of the observable universe, for example, passes when N_γ/10⁸⁷ rounds to 143. Some use a tolerance instead: a relative 2×10⁻⁶ for the CODATA anchors, and an absolute difference below 10⁻⁹ for the blackbody coefficient κ and below 10⁻⁶ for the numerical Fourier transform.

The script's labels write the bimetric background ratio as u, as version 1.1 of the note does ("written u here; c in the cited papers"), which keeps it apart from the speed of light, held in the code's constant `C`; one label adds "c in the cited papers". Inside the code the ratio's sympy symbol is still named `c`.

## The anchors

The rule behind them is root `CLAUDE.md`'s: "An anchor must be independent of the paper (a textbook identity, a published value). A check that reproduces the paper's own number is circular." ([independent anchors](/wiki/method/verification/independent-anchors)). The first block holds these:

- **The Planck units.** The script builds the Planck length, mass, temperature and time from h, c and k_B, which are exact in CODATA 2018, and from the measured G, and compares them with CODATA's published values to 2×10⁻⁶. Every number the note states "in Planck units" ([Planck units](/wiki/gravity/spin-2-fields/planck-units)) uses them.
- **The photon and entropy densities.** The blackbody photon number density at 2.7255 K must equal the Particle Data Group's 410.73 cm⁻³, and the entropy density of photons and three neutrino species its 2891.2 cm⁻³, each to 10⁻⁴. They test the formulas behind N_γ and S.
- **A Bose integral evaluated two ways.** The mean photon energy, by numerical quadrature of the Planck spectrum, must equal π⁴/(30ζ(3)) = 2.701 kT to 10⁻¹². The mean momentum built from it is the D_p of the rectangle and enters κ.
- **The comoving particle horizon.** The distance to the edge of the observable universe, integrated from the Friedmann equation with the docstring's inputs, must lie within 1% of "'about 46 Glyr' (Davis-Lineweaver 2004)", as the label gives it; it prints 46.14 Gly. The same integral gives the note's radius of 46.1 Gly and χH₀/c = 3.18, and the same expansion history, integrated forward, the event horizon ([Friedmann cosmology](/wiki/cosmology/scale-factor-duality/friedmann-cosmology)).
- **The dark-energy scale.** With the Particle Data Group's round values Ω_v = 0.68 and h = 0.67, the dark-energy density must come to "(2.2 meV)^4", the figure of its Big-Bang review; it prints 2.230 meV. The same formula, with the note's inputs, gives ρ_Λ^{1/4} = 2.24 meV.

The two published limits that the docstring also counts as anchors sit in the last block, beside the bound they protect. The bound comes from a table of the torsion-balance experiment of Lee et al. 2020, typed into the script from the thesis behind it (Table 11.4), and read by interpolating between rows. The anchor requires the interpolation to reproduce the experiment's published 38.6 μm at strength |α| = 1 and 30 μm at α = 8/3; it prints 38.63 and 30.23 μm. As round-5 ruling R12 notes, these two values come from the table's two-sided |α₉₅| column, while the bound uses its one-sided +α₉₅ column: "Both columns come from the same table, so the anchor checks the transcription and the method" ([Round 5](/wiki/method/review/round-5)).

Three later checks also compare with published values: the Cohen–Kaplan–Nelson (CKN) cutoff of the note's §4 against CKN's own estimate, "~10^-2.5 eV", to within 0.2 in the base-10 logarithm (it prints −2.378); the Coulomb force in the hydrogen ground state against CODATA's atomic unit of force, 8.2387234983×10⁻⁸ N, to 10⁻⁹; and Lee et al.'s 5.1 meV as ħc/(38.6 μm).

## The checks, block by block

The script prints one block per section of the note, in the note's order.

### The conserved area (note §3)

- **κ.** For a sphere of blackbody photons, D_x·D_p/(h N_γ^{1/3}) is evaluated at very different radii and temperatures (today's observable universe at 2.7255 K, 1 m at 10¹⁰ K, 10⁻³⁰ m at 10³² K) and must equal the closed form 3^{1/3}π^{10/3}/(30ζ(3)^{4/3}), computed exactly by sympy, to 10⁻⁹ each time; it prints κ = 1.708121. That the ratio does not change is the note's identity [D][V].
- **Other definitions.** κ = 0.316 with D_p = k_BT/c, 0.854 with D_p = ⟨|p|⟩, 1.377 for a cube.
- **Today's values.** The radius 46.1 Gly; D_x = 8.73×10²⁶ m and D_p = 6.78×10⁻³¹ kg m s⁻¹; N_γ = 1.43×10⁸⁹ and S = 1.01×10⁹⁰ k_B; S^{1/3} = 1.0×10³⁰ and the area 8.9×10²⁹ h; the entropy per photon, 3.60 for photons alone and 7.04 with neutrinos.
- **The thermal-history factors**, labelled as arithmetic (below): 11/4 at electron–positron annihilation, (11/4)^{1/3} = 1.40 and (106.75/3.909)^{1/3} = 3.01 ([the radiation era](/wiki/cosmology/early-universe/radiation-era)).

### Extent, resolution and the published answers (note §4)

- c/H₀ = 1.37×10²⁶ m, L/l_P = 8.49×10⁶⁰ cells per axis and the cube, 6.12×10¹⁸².
- The Gibbons–Hawking entropy πL²/l_P²: 3.31×10¹²² for the de Sitter radius L_Λ = 1.66×10²⁶ m and 3.0×10¹²² for the event horizon of 16.7 Gly ([de Sitter space](/wiki/cosmology/dark-energy/de-sitter-space)).
- The CKN cutoff, 4.19 meV for L = c/H₀, against CKN's estimate (above).
- Born 1938's momentum radius b, fixed by the classical electron radius through r₀ = h/(πb): bc = 2ħc/r₀ = 1.4×10⁸ eV.
- The Grosse–Wulkenhaar parameter Ω = (l_P/L)² = 1.4×10⁻¹²² ([the self-dual Grosse–Wulkenhaar model](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar)).
- The per-axis counts S^{1/3} = 1.0×10³⁰ and S_dS^{1/4} = 4.3×10³⁰, and their ratio, 0.235, the same at every epoch because both are conserved for the fixed region.
- **The CKN saturation.** For a Hubble sphere in the radiation era, in Planck units, sympy simplifies S^{1/3}/S_BH^{1/4} and S/S_BH^{3/4} and confirms that neither depends on the temperature, for g = 3.36 and g = 106.75 effective relativistic degrees of freedom; the first ratio is 0.79 and 1.05.

### Reciprocity on a rectangle, and wave packets (note §5)

- **Exact, in sympy.** The map ρ_λ: x′ = (λ²/ħ)p, p′ = −(ħ/λ²)x is symplectic for every Born length λ ([the Born length λ](/wiki/phase-space/reciprocity/born-length)); it keeps a rectangle's area; it sends the aspect ratio A to 1/A; A = 1 exactly when λ² = ħL/P; and two Born lengths differ by a squeeze, ρ_{λ₁}ρ_{λ₂}⁻¹ = diag((λ₁/λ₂)², (λ₂/λ₁)²).
- **The widths of a Gaussian.** For ψ_Z ∝ exp(iZx²/2) with Z = X + iY, Δx² = 1/(2Y) by exact integration, and Im(−1/Z) = Y/|Z|², so that Δp² = |Z|²/(2Y) and Δx/Δp = 1/|Z| ([Gaussian wave packets on the Siegel half-plane](/wiki/phase-space/modular-field/gaussian-states)).
- **A numerical Fourier transform.** The packet with Z = 0.3 + 0.7i is sampled on a grid of 2¹⁴ points and transformed; fitting the phase and the logarithm of the modulus of the result against p²/2 returns −0.5172 + 1.2069i, which equals −1/Z to 10⁻⁶. This is reciprocity's action [Z → −Z⁻¹](/wiki/phase-space/modular-field/modular-inversion) realized on a wave packet ([the Fourier transform as a phase-space rotation](/wiki/phase-space/reciprocity/fourier-transform)). The numerical width ratio of the same packet equals 1/|Z| to 10⁻⁶.
- **Distances.** On the upper half-plane with the metric (dX² + dY²)/Y², the distance from i to iY is |ln Y| (checked at Y = 3, 1/7 and 10⁵); off the imaginary axis |ln|Z|| is smaller than the distance from i, at sample points, with equality on the axis; for Z = iY the distance equals 2r in the convention σ_x = e^r/√2; the Fubini–Study metric of the packets, computed by finite differences on the grid in the X and the Y direction at three points, Z = 0.7i on the slice and 0.3 + 0.7i and −1.2 + 0.4i off it, is 1/8 of the half-plane metric to 10⁻⁶ in all six cases (it prints 0.125 six times); and in degree 3 the distance from i·1 to iy·1 is √3|ln y| ([the Siegel domain](/wiki/phase-space/modular-field/siegel-domain)).
- **det H_Z = 1** at every Z, exactly, and H = diag(Y, 1/Y) on X = 0, the slice on which the [cosmological constraint a·ã = 1](/wiki/cosmology/scale-factor-duality/cosmological-constraint) holds.
- **The clock.** ln A₀ = 213.5 per axis, 369.8 for the isotropic point in degree 3, and 106.7 e-folds.

### Where the radiation rectangle is square (note §6)

- The aspect ratio today in Planck units, A₀ = 5.2×10⁹² (log₁₀ A₀ = 92.72).
- The square, run back with D_x ∝ a and D_p ∝ 1/a, at a/a₀ = 4.4×10⁻⁴⁷ and T = 4.4×10¹⁴ T_P; in closed form, sides of 3.28 N_γ^{1/6} and T_sq = 0.61 N_γ^{1/6} T_P; counting the Standard Model's g_s = 106.75, 2.5×10⁻⁴⁷ and 2.5×10¹⁴ T_P; and at T = T_P an elongation of 6.4×10²⁸.
- Instantaneous reheating at the bound E_inf < 1.39×10¹⁶ GeV, a value typed into the script from Soman et al. 2025: T_rh < 5.7×10¹⁵ GeV and A = 2.9×10³⁵ then ([inflation and reheating](/wiki/cosmology/early-universe/inflation-and-dilution)).
- The Hubble rectangle: square at 0.28 T_P, with radius 0.75 l_P and about 0.45 quanta inside; today an aspect ratio of 1.6×10⁹² and N_H = 4.4×10⁸⁷ photons.
- The two-region reading: at that epoch the observable universe was 1.2×10³⁰ l_P across, made of 5.6×10⁸⁹ Hubble patches, and its own rectangle was long by 8×10²⁹.
- A squeezed mode with aspect ratio 10⁹² has r = 105.9 ([squeezed cosmological perturbations](/wiki/cosmology/early-universe/squeezed-perturbations)); the literature's range of 100–120 in the same label is quoted, not computed.
- At a string-scale bounce, k_BT = 10¹⁷ GeV, the rectangle is still long by A = 9.5×10³².
- A grows as a², so a turnaround, the maximum of a, is the maximum of A; the script labels this check an identity.
- The record's circle |Z| = 1, written Z = tanh s + i sech s: |Z| = 1 along it and Im Z peaks at s = 0, Z = i; on the circle the position and momentum entries of H are equal, H_xx = H_pp = 1/Y.
- (M_X/H₀)² = 1.3×10⁶¹ for M_X c² = 5.2 meV, the order of the factor by which an order-one X today would exceed the critical density. The mass is ħc over the interpolated one-sided bound at α = 4/3, computed with the same interpolation as the bound in the last block.

### The self-dual box (note §7)

- λ = √(l_P L) = 47.1, 51.8 and 84.0 μm, with ħc/λ = 4.19, 3.81 and 2.35 meV, for the Hubble radius, the de Sitter radius and the particle horizon; each equals the CKN cutoff with the unreduced Planck mass to 10⁻¹².
- The CKN cutoff in other conventions: factors 0.45, 0.59, 0.84 and 2.08, computed from four closed forms whose assignment to conventions is the label's (reduced Planck mass; a sphere with M_BH = Lc²/2G; a cube with r_s = L; one scalar field's zero-point energy Λ⁴/16π²).
- ρ_Λ^{1/4} = 2.24 meV, or 88.1 μm; its ratio to the Hubble box's ħc/λ equals (3Ω_Λ/8π)^{1/4} = 0.535 to 10⁻¹⁰ at each of H₀ = 60, 67.4 and 73 km s⁻¹ Mpc⁻¹, with Ω_Λ held fixed; and the particle horizon's closer agreement comes from χH₀/c = 3.18 ([the cosmological constant Λ](/wiki/cosmology/dark-energy/cosmological-constant)).
- With λ² = l_P L_Λ, the Hubble box's aspect ratio equals √Ω_Λ(t) at scale factors from 10⁻³ to 10, with a largest deviation of 3.3×10⁻¹⁶; 0.83 today.
- L_Λ = λ²/l_P, Λ = 3l_P²/λ⁴ and λ/l_P = 3.2×10³⁰ = √(L_Λ/l_P).
- The numerology: in units of √(l_P L_Λ) today's rectangle is square at k_BT = 1.0 TeV with the Standard Model's species, 1.7 TeV for photons alone; √(k_BT₀E_P) = 1.7 TeV; √(ρ_Λ^{1/4}E_P) = 5.2 TeV, the geometric mean of Berglund–Hübsch–Minic's see-saw.
- The fourth root: log₁₀(Λl_P²) = −121.5 against log₁₀(λ/l_P) = 30.5.
- The Born length that makes today's rectangle square, √(ħD_x/D_p) = 3.7×10¹¹ m, 2.5 au.

### Consequences (note §8)

- The maximum force of [conjugate special relativity](/wiki/conjugate-relativity/maximum-force), c̃ = ħc/λ²: c⁴/G = 1.21×10⁴⁴ N at λ = l_P, and 1.4×10⁻¹⁷ N (L = c/H₀) and 1.2×10⁻¹⁷ N (L_Λ) at the self-dual length, with c̃/(c⁴/G) = l_P/L; the hydrogen Coulomb force, 8.24×10⁻⁸ N, exceeds the value for L = c/H₀ by 5.8×10⁹, and the weight of a kilogram exceeds it by 6.9×10¹⁷.
- With the Born length at l_P the Hubble box is long by L/l_P = 8.5×10⁶⁰.
- **The torsion-balance bound.** The rows of the thesis table at ranges from 25 to 100 μm, each with its +α₉₅ and |α₉₅| limits, are typed into the script; a crossing is found by interpolating linearly in the logarithms of range and strength between the two rows that bracket it. After the anchor, the one-sided column at α = 4/3 gives λ_X < 37.7 μm and M_X c² > 5.2 meV (it prints 37.68 μm, 5.237 meV); Lee et al.'s 5.1 meV is ħc/(38.6 μm); the two-sided column at α = 4/3 gives 35.8 μm ([Yukawa forces and their range](/wiki/gravity/spin-2-fields/yukawa-forces)).
- **The background ratio.** At α = (4/3)u² the one-sided column gives 57.0 μm at u = 0.5, 42.5 μm at 0.8 and 30.8 μm at 1.5; reading the interpolated limit at the self-dual lengths, X at 47.1 μm survives only for u below 0.67, and at 84.0 μm only below 0.30 (it prints 0.6717 and 0.3017).
- **The vacua of the palindromic theory.** With βₙ = β₄₋ₙ ([the palindrome](/wiki/gravity/palindromic-branch/palindrome)), sympy confirms that the equation for proportional backgrounds factorizes as u(u − 1)(u + 1)(β₁u² + (3β₂ − β₀)u + β₁) = 0. On the flat branch β₀ = −4β₁ − 3β₂, the symmetry-breaking pair (u, 1/u) is looked for at sample points of the (β₁, β₂) plane: it appears at each sample inside β₁ < 0 < |β₁| < β₂, each root with a vacuum energy, in units of 2(β₁ + β₂), of size above 0.1, and at none of the samples outside. The label says "(sampled)". The closed-universe note later found that the aligned branch needs β₁ > 0, which no document had stated; for β₁ < 0 the hot branch ends at a broken vacuum with negative Λ_g (flag 51 in `review/wiki-build-flags.md`; [the momentum graviton in a closed universe](/wiki/gravity/momentum-graviton/closed-universe#β--0-is-required-dv)).
- X at the self-dual length, 47–84 μm, is excluded in the aligned vacuum, and M_X exceeds the dark-energy scale by a factor of 2.3.
- The 4/3 of the Yukawa strength, labelled as arithmetic of the cited propagators (below).
- The Vainshtein radius of a 1 kg test mass for a 50 μm range, about 10⁻¹² m, checked to its power of ten (it prints 1.95e-12 m).
- Under ρ at λ = l_P, today's rectangle maps to a region 1.0×10⁻³¹ l_P across with momenta spread over 5.4×10⁶¹ m_P c.
- **The a⁻⁶ term.** In sympy, a → C/a (with ȧ transformed with it) exchanges the minisuperspace kinetic terms M_P² aȧ² and M̃² C³ȧ²/a⁵; their sum is invariant for M̃ = M_P and not for M̃ = 2M_P; and at M̃ = M_P the two are equal at a = √C. The check takes the dual kinetic term as given; no document derives it from the program's geometric action (flag 49 in `review/wiki-build-flags.md`).
- The lever arm per radian at the Bohr momentum: 4.9×10⁻⁶⁰ m at λ = l_P and 42 m at λ = √(l_P c/H₀).

## Identities, quoted factors and reproductions

The checks confirm different things, and the script marks some of the difference itself.

- **Labelled by the script.** These labels carry a parenthesis. "(arithmetic of the quoted factors)": the factor 11/4 by which the photon number jumps at annihilation, its cube root 1.40, and (106.75/3.909)^{1/3} = 3.01. "(identity)": "A grows as a^2, so a turnaround (maximum of a) is the maximum of A", tested on sample pairs of scale factors. "(arithmetic of the cited propagators)": the 4/3 as the ratio of the massive tensor structure, 1 − 1/3, to the massless one, 1 − 1/2. These confirm how the quoted factors combine, not the physics that supplies them: the species counts are standard thermal history [T], and the 4/3 with its dependence on u is the result of the cited bimetric papers ([Hassan–Rosen bimetric gravity](/wiki/gravity/spin-2-fields/hassan-rosen-bimetric)).
- **Exact identities.** The sympy checks hold for all values of their symbols: ρ_λ on rectangles, the Gaussian widths, det H_Z = 1, the |Z| = 1 path, the CKN saturation's independence of temperature, the factorization of the background equation and the a → C/a exchange. They confirm algebra that the note tags [D][V] or [T][V].
- **Reproductions.** The rest recompute a number the note quotes from the docstring's inputs. They show that the note's numbers follow from those inputs, not that the inputs or the model are right ([verification checks arithmetic, not the model](/wiki/method/verification/arithmetic-not-model)). Some are identities, and the note says so: with λ² = l_P L_Λ, A(t) = √Ω_Λ(t) "holds by construction, because λ was built from L_Λ" (§7), and the match of the self-dual length to the dark-energy scale, the ratio 0.535, is "the Friedmann equation restated" (§1).

## Independent recomputation

Outside the script, the numbers were recomputed by agents that chose their own inputs and wrote their own code:

- **Before the draft was final.** The note's research workflow ran eight agents, among them "an independent recomputation of the numbers" and "an independent re-derivation" (note, provenance line). The worklog at 15:15 on 2026-10-26: "the independent numbers agent has returned and matches every number of my draft script". The agents' results were kept in the session's scratch files, outside the repository. The worklog records that a crash of the machine later wiped those files, after everything the record needs had been copied into the repository, and that the literature and review agents' full returns survive in the workflow journals.
- **In round 5.** Each referee received only a copy of the note's version 1.0 and recomputed every number with its own code. Referee A used CODATA 2018 and Planck 2018, with a sensitivity run at H₀ = 67.36 and Ω_m = 0.3153, and N_eff = 3.046: "All of the following reproduce to the quoted precision" (`review/round5/referee-A/audit-notes.md`, Step 2). Referee B used its own inputs, with N_eff = 3.046 and A_s = 2.1×10⁻⁹ and the horizons by quadrature: "every number in the manuscript reproduced from my own inputs …; none wrong beyond rounding" (`review/round5/referee-B/audit-notes.md`, Step 5). Both re-derived κ, the closed forms of the square, ρ_λ, the Gaussian statements and the Fubini–Study factor, A(t) and the a → C/a exchange symbolically, and both interpolated the thesis table themselves and found 37.68 μm at α = 4/3 in the one-sided column (Steps 2 and 3). The adjudication: "Every number reproduced under the referees' own constants and code".

While the note was drafted, the script caught errors of the author's own: at 15:55 the worklog records that "The script caught two of my own numbers (ln A₀ = 213.5, not 213.8; the two-region aspect 8×10²⁹, not 8×10²⁸) and one script bug before they reached the note."

Five minor numerical findings survived the round, "four of them in conventions listed" in the forecast (rulings R3, R6, R7, R9 and R12; [Round 5](/wiki/method/review/round-5)): the area of one cell, ħ rather than h; the TeV numerology without its species count and set beside the wrong geometric mean; "halves the exponent" for what is a fourth root; an unstated assumption behind one convention factor; and which column of the exclusion table the bound uses. The major finding, R1, came from the referees' reading of the cited equations and their own derivation of the coupling, while the note's arithmetic with its formula reproduced.

## The round-5 additions

Revision 10 of the adjudication reads: "References and `verify/phase_space_diameter.py`: every new number gated; every new citation retrieved." The worklog lists the extension made with version 1.1 as "c-dependent bound, broken vacua, CKN saturation, conventions". The rulings that changed a number of the note, and the checks that now carry them:

| Ruling | What version 1.1 states | The check |
| --- | --- | --- |
| R1, the background ratio | the bound as a function of u; the aligned vacuum as the only proportional vacuum compatible with the observed Λ | the bound at u = 0.5, 0.8 and 1.5; the thresholds 0.67 and 0.30; the factorization; the sampled symmetry-breaking pair |
| R2, the per-axis counts | the constant ratio 0.235 and the CKN saturation, in place of "holds at no other epoch" | the constant ratio; the CKN saturation |
| R6, the TeV numerology | 1.0 TeV with the Standard Model's species; 1.7 TeV as √(k_BT₀E_P) | the numerology line |
| R7, "halves the exponent" | a fourth root | the fourth-root line |
| R9, the CKN conventions | 0.45, 0.59, 0.84 and 2.08, each with its assumption | the conventions line |
| R12, the two columns | the one-sided column, and why | the two-sided 35.8 μm beside the one-sided 37.7 μm |
| R14, further readings | the squeezed mode; a string-scale bounce | r = 105.9; A = 9.5×10³² |

Later the same day, after the wiki's pages on the note were written, the script was tightened: the worklog's entry of 17:55 lists "the verify script's labels, its H₀ independence check, its interpolated M_X and its Fubini–Study check tightened". As it now stands, its docstring and closing line claim the numbers the note computes; the dark-energy ratio is evaluated at three values of H₀; the order-one-X check takes its mass from the interpolated bound; the Fubini–Study check covers both directions, on the slice and off it; and the labels write the background ratio as u. It runs 85 checks.

The adjudicator's arbitration, `review/round5/adjudicator/arb.py` with its output `arb.out`, computed the figures behind these rulings. Like the arbitration scripts of rounds 3 and 4 it sits in `review/` and the gate does not run it; root `CLAUDE.md` says arbitration scripts go in `verify/` (flag 38 in `review/wiki-build-flags.md`). The numbers of version 1.1 that came from it are gated here.

## What it does not check

- **The literature's own figures.** The docstring says so itself: "Figures the note quotes from the literature (Egan and Lineweaver's entropies, the squeezing values, FKGLM's estimates) are not recomputed, except where a check below reproduces them". Not computed are Egan and Lineweaver's entropy budget (5.40×10⁸⁹ k for the photons, about 3×10¹⁰⁴ k for the supermassive black holes, 2.6×10¹²² k for the event horizon, §3), the squeezing of about 50 at the end of inflation and 100–120 today (§5), and the estimates the note quotes from FKGLM (§4), among others. Where such a figure feeds a computation, the script types it in, as below.
- **Citations.** The script checks numbers, not sources. Whether each cited work says what the note quotes rests on retrieval, which the note's reference list marks [S] ("retrieved by live search for this note"), and on the referees' citation step ([Round 5](/wiki/method/review/round-5)). Several inputs from the literature are typed in: Planck 2018's H₀ and Ω_m, T₀ = 2.7255 K, the rows of the thesis table, E_inf < 1.39×10¹⁶ GeV, and the string scale of 10¹⁷ GeV. The anchors test some of them indirectly (the table rows through the published limits, the blackbody inputs through the densities); the reheating bound, and the squeezing range of 100–120 in a label, are quoted without a check.
- **The premise u = 1.** The bound of 37.7 μm is computed at α = 4/3, the value at equal Planck masses in the aligned vacuum, background ratio u = 1. The script shows that the palindromic background equation factorizes and that, at its sample points, the symmetry-breaking vacua carry a vacuum energy of the order of the spin-2 mass squared. That the program's vacuum is the aligned one, that reciprocity fixes equal Planck masses, and whether the aligned point persists as the universe expands, an open question [O], are premises and arguments of the note's §8.2 and the program's documents, not computations ([the vacuum-energy identity](/wiki/gravity/palindromic-branch/vacuum-energy-identity)). The bound also assumes that X adds the only Yukawa term (§8.2, caveats).
- **Statements wider than the code.** The symmetry-breaking pair is checked at sample points, as its label says. The CKN saturation's range, 0.79–1.05, is evaluated at its two ends, g = 3.36 and 106.75. The ratio 0.535 is independent of H₀ by algebra (note §7); the code evaluates it at three values, as its label says.
- **Loose checks.** Some checks are loose by design: the particle-horizon anchor (within 1% of "about 46 Glyr"), CKN's estimate (0.2 in the logarithm), N_γ^{1/6} near 10¹⁵ and the Vainshtein radius (its power of ten). For the Vainshtein radius the script prints 1.95e-12 m, and referee A, with its own formula, found 1.5×10⁻¹² m; the note says "about 10⁻¹² m".
- **The arguments.** Which event the chat meant by "the bounce", the paragraph on where the claim probably came from, which the note tags "[D, inference]" (§6), and the conditional consequences of §8.4 and §8.5 are arguments. The script checks the arithmetic inside them.

## The recorded output

The run of 2026-10-26:

```text
== Anchors (independent of the note)
PASS  CODATA 2018 Planck length 1.616255e-35 m  [1.616255e-35]
PASS  CODATA 2018 Planck mass 2.176434e-8 kg  [2.176434e-08]
PASS  CODATA 2018 Planck temperature 1.416784e32 K  [1.416784e+32]
PASS  CODATA 2018 Planck time 5.391247e-44 s  [5.391246e-44]
PASS  PDG: photon number density 410.73 cm^-3 at 2.7255 K  [410.73]
PASS  PDG: entropy density s/k = 2891.2 cm^-3  [2891.3]
PASS  blackbody mean photon energy: quadrature = pi^4/(30 zeta(3)) = 2.701 kT  [2.701178]
PASS  comoving particle horizon: 'about 46 Glyr' (Davis-Lineweaver 2004), within 1%  [46.14 Gly]
PASS  PDG Big-Bang review: dark energy ~ (2.2 meV)^4 for Omega_v = 0.68, h = 0.67  [2.230 meV]

== The conserved area (note §3)
PASS  D_x D_p = kappa h N^(1/3), kappa = 3^(1/3) pi^(10/3)/(30 zeta(3)^(4/3)) = 1.708, at any R and T  [kappa = 1.708121]
PASS  other definitions: kappa = 0.316 (D_p = kT/c), 0.854 (<p>), 1.377 (cube of side D_x)  [0.3162, 0.8541, 1.3767]
      D_x = 8.7295e+26 m, D_p = 6.7810e-31 kg m/s, N_gamma = 1.4306e+89, S = 1.0071e+90 k_B
PASS  observable universe: radius 46.1 Gly; D_x = 8.73e26 m, D_p = 6.78e-31 kg m/s
PASS  N_gamma = 1.43e89, S = 1.01e90 k_B (the chat's ~10^90 is S)  [1.431e+89, 1.007e+90]
PASS  S^(1/3) = 1.0e30; area D_x D_p = 8.9e29 h  [1.002e+30, 8.934e+29]
PASS  entropy per photon: 3.60 (photons alone), 7.04 (with neutrinos)  [7.0394]
PASS  (arithmetic of the quoted factors) photon number jumps by 11/4 at annihilation (before it: 4/11 of today's), aT by (11/4)^(1/3) = 1.40; (106.75/3.909)^(1/3) = 3.01

== Extent, resolution and the published answers (note §4)
PASS  c/H0 = 1.37e26 m; L/l_P = 8.49e60 cells per axis; the cube 6.12e182  [8.4918e+60]
PASS  Gibbons-Hawking pi L^2/l_P^2 = 3.31e122 for L_Lambda = 1.66e26 m; 3.0e122 for the event horizon, 16.7 Gly  [CEH 16.68 Gly]
PASS  CKN cutoff (M_P/L)^(1/2) = 4.19 meV for L = c/H0 (CKN's own estimate: ~10^-2.5 eV)  [-2.378]
PASS  Born 1938: b from the classical electron radius by r0 = h/(pi b), b c = 2 hbar c/r0 = 1.4e8 eV  [1.4005e+08 eV]
PASS  Grosse-Wulkenhaar: Omega = (l_P/L)^2 = 1.4e-122 for L = c/H0  [1.387e-122]
PASS  per-axis counts: radiation S^(1/3) = 1.0e30 against FKGLM's S_dS^(1/4) = 4.3e30  [4.265e+30]
PASS  both counts are conserved for the fixed region, so S^(1/3)/S_dS^(1/4) = 0.235 at every epoch  [0.2350]
PASS  CKN saturation: a radiation-era Hubble sphere has S^(1/3)/S_BH^(1/4) = 0.79-1.05 (g = 3.36-106.75) and S proportional to S_BH^(3/4), at every temperature  [[0.7899, 1.0537]]

== Reciprocity on a rectangle; wave packets (note §5)
PASS  rho_lambda is symplectic for every lambda (R^T w R = w)
PASS  the area L P is invariant for every lambda
PASS  the aspect ratio A = hbar L/(lambda^2 P) goes to 1/A
PASS  A = 1 iff lambda^2 = hbar L/P
PASS  two Born lengths differ by a squeeze: rho_l1 rho_l2^-1 = diag((l1/l2)^2, (l2/l1)^2)
PASS  Delta x^2 = 1/(2Y) for psi_Z
PASS  Fourier image has Im(-1/Z) = Y/|Z|^2, so Delta p^2 = |Z|^2/(2Y) and Delta x/Delta p = 1/|Z|
PASS  Fourier transform maps Z = 0.3 + 0.7i to -1/Z = -0.5172 + 1.2069i (numerical FFT)  [-0.517241+1.206897j]
PASS  numerically Delta x/Delta p = 1/|Z| for Z = 0.3 + 0.7i  [1.313064]
PASS  half-plane distance from i to iY is |ln Y| (Y = 3, 1/7, 1e5)
PASS  off the slice |ln(Delta x/Delta p)| = |ln|Z|| is smaller than d(i, Z); equal on the slice
PASS  for Z = iY, sigma_x/sigma_p = 1/Y and the distance |ln Y| = 2r (sigma_x = e^r/sqrt 2)
PASS  Fubini-Study metric on Gaussians is 1/8 of the Siegel metric (dX^2 + dY^2)/Y^2, in both directions, on and off the slice (so Siegel length 2r = FS length r/sqrt 2)  [[0.125, 0.125, 0.125, 0.125, 0.125, 0.125]]
PASS  Siegel degree 3: distance from i1 to iy1 is sqrt(3)|ln y|; rho maps iy1 to (i/y)1
PASS  det H_Z = 1 at every Z; on X = 0, H = diag(Y, 1/Y)
PASS  the clock: ln A0 = 213.5 per axis, 369.8 for the isotropic degree-3 point; 106.7 e-folds  [213.486]

== Where the radiation rectangle is square, lambda = l_P (note §6)
PASS  aspect ratio today (D_x/l_P)/(D_p/m_P c) = 5.2e92, log10 92.72  [5.1970e+92]
PASS  square at a/a0 = 4.4e-47, T = 4.4e14 T_P (free streaming back from today)  [4.387e-47, 4.386e+14]
PASS  closed form: sides sqrt(2 pi kappa) N^(1/6) = 3.28 N^(1/6); T_sq = 0.61 N^(1/6) T_P; N^(1/6) ~ 1e15
PASS  with the SM's g_s = 106.75: a/a0 = 2.5e-47, T = 2.5e14 T_P  [2.528e-47, 2.527e+14]
PASS  at T = T_P (SM counting) the rectangle is still long by 6.4e28  [6.387e+28]
PASS  instant reheating at E_inf < 1.39e16 GeV: T_rh < 5.7e15 GeV; the rectangle then has A = 2.9e35  [5.710e+15 GeV, 2.920e+35]
PASS  Hubble sphere (radiation era, SM): square at T = 0.28 T_P, radius 0.75 l_P, about 0.45 quanta inside  [T = 0.2784 T_P, R = 0.752, N = 0.447]
PASS  Hubble sphere today: aspect ratio 1.6e92, N_H = 4.4e87  [1.634e+92, 4.448e+87]
PASS  two regions: at that epoch the observable universe was 1.2e30 l_P across, 5.6e89 Hubble patches, its rectangle long by 8e29  [1.239e+30, 5.592e+89, 8.239e+29]
PASS  a squeezed mode with aspect 1e92 has r = 105.9, inside the literature's 100-120
PASS  at a string-scale bounce, kT = 1e17 GeV, the radiation rectangle is still long by A = 9.5e32  [9.520e+32]
PASS  (identity) A grows as a^2, so a turnaround (maximum of a) is the maximum of A
PASS  the record's |Z| = 1 path Z = tanh s + i sech s: |Z| = 1, Im Z peaks at s = 0 (Z = i)
PASS  on |Z| = 1, H_xx = H_pp = 1/Y: the position and momentum extents are equal at all times
PASS  an order-one X today: (M_X/H0)^2 = 1.3e61 for M_X c^2 = 5.2 meV  [1.327e+61]

== The self-dual box (note §7)
PASS  lambda = sqrt(l_P L) = 47.1 um, hbar c/lambda = 4.19 meV, equal to the CKN cutoff (unreduced)
PASS  lambda = sqrt(l_P L) = 51.8 um, hbar c/lambda = 3.81 meV, equal to the CKN cutoff (unreduced)
PASS  lambda = sqrt(l_P L) = 84.0 um, hbar c/lambda = 2.35 meV, equal to the CKN cutoff (unreduced)
PASS  CKN in other conventions: 0.45 (reduced M_P), 0.59 (sphere, M_BH = Lc^2/2G), 0.84 (cube, r_s = L), 2.08 (one scalar's zero-point energy Lambda^4/16 pi^2)  [[0.4466, 0.5878, 0.8409, 2.0837]]
PASS  rho_Lambda^(1/4) = 2.24 meV, 88.1 um
PASS  rho_Lambda^(1/4)/(hbar c/sqrt(l_P c/H0)) = (3 Omega_L/8 pi)^(1/4) = 0.535, at H0 = 60, 67.4 and 73  [0.53472]
PASS  the particle horizon's closer agreement comes from chi H0/c = 3.18
PASS  with lambda^2 = l_P L_Lambda the Hubble box has A(t) = sqrt(Omega_Lambda(t)); 0.83 today  [max deviation 3.3e-16]
PASS  L_Lambda = lambda^2/l_P, Lambda = 3 l_P^2/lambda^4, lambda/l_P = 3.2e30 = sqrt(L_Lambda/l_P)
PASS  numerology: in units of sqrt(l_P L_Lambda) the radiation rectangle is square at kT = 1.0 TeV with the SM g_s, 1.7 TeV for photons alone; sqrt(k T0 E_P) = 1.7 TeV; BHM-type sqrt(rho_L^(1/4) E_P) = 5.2 TeV  [0.963, 1.671, 1.693, 5.23 TeV]
PASS  the reformulation takes the fourth root: log10(Lambda l_P^2) = -121.5 against log10(lambda/l_P) = 30.5
PASS  the Born length that makes today's radiation rectangle square: sqrt(hbar D_x/D_p) = 3.7e11 m, 2.5 au

== Consequences (note §8)
PASS  c~ = c^4/G = 1.21e44 N at lambda = l_P
PASS  at the self-dual length c~ = 1.4e-17 N (c/H0), 1.2e-17 N (L_Lambda); c~/(c^4/G) = l_P/L
PASS  hydrogen Coulomb force 8.24e-8 N (CODATA atomic unit 8.2387234983e-8 N) exceeds it by 5.8e9; 1 kg weight by 6.9e17
PASS  with the Born length at l_P the Hubble box is long by L/l_P = 8.5e60
PASS  anchor: the interpolation reproduces Lee et al.'s published 38.6 um (|alpha| = 1) and 30 um (alpha = 8/3)  [38.63, 30.23 um]
PASS  attractive Yukawa with alpha = 4/3 (one-sided +alpha95): lambda_X < 37.7 um, M_X c^2 > 5.2 meV  [37.68 um, 5.237 meV]
PASS  Lee et al.'s 5.1 meV is hbar c/38.6 um
PASS  the two-sided |alpha95| column gives the stronger 35.8 um at alpha = 4/3  [35.79 um]
PASS  for background ratio u (alpha = 4u^2/3; c in the cited papers): 57.0 um at u = 0.5, 42.5 at 0.8, 30.8 at 1.5  [[56.98, 42.53, 30.83]]
PASS  X at the self-dual length survives only for u < 0.67 (47.1 um) or u < 0.30 (84.0 um)  [[0.6717, 0.3017]]
PASS  proportional backgrounds of the palindromic theory: u(u - 1)(u + 1)(beta1 u^2 + (3 beta2 - beta0) u + beta1) = 0
PASS  on the flat branch the symmetry-breaking pair (u, 1/u) exists only for beta1 < 0 < |beta1| < beta2 (sampled), with vacuum energy of order the spin-2 mass squared  [[[-1.143, -70.857], [-1.387, -934.613], [-0.632, -5.128]]]
PASS  so X at the self-dual length (47-84 um) is excluded, and M_X exceeds the dark-energy scale by 2.3x
PASS  (arithmetic of the cited propagators) the 4/3: massive (1 - 1/3) over massless (1 - 1/2) tensor structure
PASS  Vainshtein radius of a 1 kg test mass for a 50 um range: about 1e-12 m  [1.95e-12 m]
PASS  rho_(l_P) image of today's radiation rectangle: 1.0e-31 l_P across, momenta 5.4e61 m_P c
PASS  a -> C/a exchanges M_P^2 a adot^2 and M~^2 C^3 adot^2/a^5 iff M~ = M_P; then they are equal at a = sqrt(C)
PASS  lever arm per radian at the Bohr momentum: 4.9e-60 m (lambda = l_P), 42 m (lambda = sqrt(l_P c/H0))

OK — every number the phase-space-diameter note computes reproduces.
```

## Sources

- `verify/phase_space_diameter.py` — the docstring with its scope and what it leaves out, the inputs, the check helper and tolerances, every check and label, the typed-in table rows and the sampled couplings, the closing line; its output — the 85 checks of the recorded run
- `papers/phase-space-diameter.md` header — the [V] tag and the background ratio written u; §3–§8 — the numbers the script reproduces, "holds by construction" (§7) and the caveats of §8.2; 'References' — the [S] marks; the provenance note — the separate agents
- `notes/phase-space-diameter-worklog.md` 'Status' — the independent numbers agent (15:15), the errors the script caught (15:55), the extension with version 1.1 (17:00), the tightening (17:55), the agents' results kept in scratch files and their loss in the crash, with the 85 checks passing after it (18:25)
- `review/round5-adjudication.md` 'Rulings' (R1, R2, R6, R7, R9, R12, R14), 'Revisions for v1.1' (item 10) — the checks the review added; the verdict's "Every number reproduced"; 'Pre-registration scored' — the five minor numerical findings
- `review/round5/referee-A/audit-notes.md` and `review/round5/referee-B/audit-notes.md` Steps 2, 3 and 5 — the referees' inputs, recomputations and re-derivations
- `review/round5/adjudicator/arb.out` — the arbitration figures
- `scripts/check.sh` — the script's place in the gate
- `CLAUDE.md` 'Layout' — the script listed as "the diameter note"; where arbitration scripts go; 'Method (HANDOFF §5)' — the anchor rule
- `review/wiki-build-flags.md` item 38 — where arbitration scripts belong, awaiting Paul's ruling
- `review/wiki-build-flags.md` items 49 and 51 — the dual Einstein–Hilbert term not derived; β₁ > 0 required and never stated; from the closed-universe investigation, awaiting Paul's ruling
