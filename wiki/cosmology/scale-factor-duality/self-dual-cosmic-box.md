---
title: "The self-dual cosmic box"
weight: 90
status: alive
description: "The phase-space box [l_P, L] × [ħ/L, ħ/l_P], from the Planck length to the horizon, is mapped onto itself by Born reciprocity for one Born length, √(l_P L) = 47–84 μm: the Cohen–Kaplan–Nelson cutoff and the Born-geometry cell length, both prior art; its match to the dark-energy scale is the Friedmann equation, and de Sitter space is its self-dual state by construction."
provenance: [T, D, V]
sources:
  - "papers/phase-space-diameter.md §7"
  - "papers/phase-space-diameter.md §4"
  - "papers/phase-space-diameter.md §5"
  - "papers/phase-space-diameter.md §2"
  - "papers/phase-space-diameter.md §8"
  - "papers/phase-space-diameter.md §8.1"
  - "papers/phase-space-diameter.md §8.6"
  - "papers/phase-space-diameter.md §9"
  - "papers/phase-space-diameter.md 'References'"
  - "verify/phase_space_diameter.py 'Extent, resolution and the published answers (note §4)'"
  - "verify/phase_space_diameter.py 'The self-dual box (note §7)'"
  - "review/round5-adjudication.md 'Rulings' R6–R10, R15"
  - "review/round5-adjudication.md 'Pre-registration scored'"
  - "review/round5-preregistration.md 'Predictions'"
  - "notes/phase-space-diameter-worklog.md 'Status'"
  - "CLAUDE.md 'Since the handoff'"
  - "review/wiki-build-flags.md item 27"
  - "notes/closed-universe.md §2"
---

*The self-dual cosmic box is the range of scales of the universe drawn as a rectangle in [phase space](/wiki/phase-space), the space of positions and momenta taken together. In position it runs from the [Planck length](/wiki/gravity/spin-2-fields/planck-units) l_P to a cosmic length L, such as the radius of the Hubble sphere; in momentum it runs from ħ/L, the finest momentum a region of size L can resolve, to the Planck momentum ħ/l_P. A recorded waveform has the same two limits: its duration sets how finely its spectrum can be resolved, and its sampling interval sets how far the spectrum reaches. [Born reciprocity](/wiki/phase-space/reciprocity/born-reciprocity), the exchange of position and momentum, needs a reference length to turn a length into a momentum, the [Born length](/wiki/phase-space/reciprocity/born-length) λ, and it maps this box onto itself for exactly one value of λ: the geometric mean √(l_P L), between 47 and 84 micrometres depending on the cosmic length chosen. The length is already in the published literature, from a bound on field theory in a box the size of the universe to the Born-geometry papers this program builds on. It lies within a factor of two of the length scale of dark energy, an agreement that restates the Friedmann equation, and with it held fixed the box approaches exact symmetry as the universe approaches the empty [de Sitter space](/wiki/cosmology/dark-energy/de-sitter-space) of its far future, by construction. None of this predicts anything unless the Born length is fixed by other physics, and the program cannot use this length as a scale of its own ([obituary](/wiki/cosmology/scale-factor-duality/self-dual-length-obituary)).*

**Status:** Alive, as a restatement of published results — the self-dual length [T][V] and its prior art [T], with live-searched citations [S]; its equality with the Cohen–Kaplan–Nelson cutoff [T][V]; the dark-energy match, the aspect ratio A(t) = √Ω_Λ(t) and Λ = 3l_P²/λ⁴ [D][V] (`papers/phase-space-diameter.md` §7, §9) — every number is printed by `verify/phase_space_diameter.py` ([the phase-space-diameter script](/wiki/method/verification/phase-space-diameter-script)), and the note was graded B by both referees of [round 5](/wiki/method/review/round-5), with version 1.1 applying the revisions. In the note's words, "none of it predicts anything unless the reference length is fixed by something other than the cosmological constant itself" (§7).

## The box

### Its edges and its cells [T][V]

The phase-space-diameter note pairs a size in position with a size in momentum in four ways (§2). The box is the pairing of extent with resolution, and the note introduces it with a signal analogy: "A waveform of duration T can be resolved in frequency only to about 1/T, and a waveform sampled at intervals τ has a spectrum that reaches only to about 1/τ; the number of independent samples is the same in both descriptions" (§4, plain-language passage; [the Fourier transform](/wiki/phase-space/reciprocity/fourier-transform#the-timebandwidth-product)). For the universe the size L plays the duration and the Planck length the sampling interval:

```text
the Fourier box:    l_P ≤ x ≤ L,        ħ/L ≤ p ≤ ħ/l_P
```

"A region of position extent L resolved to a length ℓ has momentum extent ħ/ℓ resolved to ħ/L: L/ℓ cells of area ħ per axis in either description (L/2πℓ cells of area h)" (§4) [T]. With L = c/H₀ = 1.37×10²⁶ m, the Hubble radius of [Friedmann cosmology](/wiki/cosmology/scale-factor-duality/friedmann-cosmology), and ℓ = l_P = 1.616×10⁻³⁵ m, there are L/l_P = 8.49×10⁶⁰ cells per axis [V]. The box grows with L. Its area is therefore not conserved, unlike the area of the radiation rectangle in [the phase-space diameter relation](/wiki/cosmology/scale-factor-duality/phase-space-diameter), which stays fixed for a fixed comoving region (§2's table).

Gravity limits how many of these cells are independent [T][V]. The cube of the per-axis count, 6.12×10¹⁸², is not the number of independent states. A horizon of radius L carries the Gibbons–Hawking entropy πL²/l_P² [S: Gibbons–Hawking 1977; Bousso 2000]: 3.31×10¹²² for the de Sitter radius L_Λ = c/(H₀√Ω_Λ) = 1.66×10²⁶ m, and 3.0×10¹²² for today's cosmic event horizon, 16.7 Gly (billion light-years). Here Ω_Λ is the fraction of the critical density, the total density of a spatially flat universe, that is in dark energy. Bousso's N-bound states that "a universe with Λ > 0 cannot have entropy greater than N = 3π/Λ" in Planck units, which is the same horizon entropy [S: Bousso 2000] (§4).

### Reciprocity on the box [T][D][V]

With Born length λ, reciprocity in ordinary units is (§5):

```text
ρ_λ:   x′ = (λ²/ħ) p,     p′ = −(ħ/λ²) x
```

The map is symplectic for every λ. It sends a rectangle of extents (L, P) to one of extents (λ²P/ħ, ħL/λ²), so the area L·P is unchanged and the aspect ratio in units of λ, A = ħL/(λ²P), goes to 1/A. Every rectangle is self-dual, A = 1, for exactly one λ, the geometric mean of L and ħ/P [D][V]; "square" therefore has a meaning only once λ is fixed (§5).

For the box, ρ_λ sends the largest momentum, ħ/l_P, to the length λ²/l_P, and the smallest, ħ/L, to λ²/L. These are the box's own position limits, L and l_P, exactly when λ² = l_P L, and the position limits then go over to the momentum limits ħ/L and ħ/l_P, up to sign (the wiki's reading of the step). The note's statement:

> "By §5 the Fourier box [l_P, L] × [ħ/L, ħ/l_P] maps onto itself under ρ_λ exactly when λ² = l_P L." (§7)

The box's aspect ratio in units of λ is A = L l_P/λ² (§7's formula, with L in place of c/H). At the Planck value λ = l_P, which the program's paper on [conjugate special relativity](/wiki/conjugate-relativity), #13, adopts, the box is far from self-dual: "A = L/l_P = 8.5×10⁶⁰ for the Hubble radius" (§8.1).

## The self-dual length [T][V]

The length that makes the box self-dual, for three choices of L (§7):

| L | λ = √(l_P L) | ħc/λ |
| --- | --- | --- |
| Hubble radius c/H₀ = 1.37×10²⁶ m | 47.1 μm | 4.19 meV |
| de Sitter radius L_Λ = 1.66×10²⁶ m | 51.8 μm | 3.81 meV |
| particle horizon, 4.36×10²⁶ m | 84.0 μm | 2.35 meV |

The Hubble radius is set by today's expansion rate H₀; the de Sitter radius is the Hubble radius of a universe holding only the [cosmological constant](/wiki/cosmology/dark-energy/cosmological-constant); the particle horizon is the distance light can have travelled since the expansion began [T]. The last column is the energy that belongs to the length. `verify/phase_space_diameter.py` prints all six values.

## The length in the literature [T]

"This is the scale of §4's literature [S: CKN 1999; Bambi–Urban 2008; Padmanabhan 2006; FKGLM 2023; BHM 2023; implicitly Mignemi 2010]" (§7). Every citation below was retrieved by live search for the note [S]; the quotations are the note's.

### Born, 1938

Born set up the question of how the universe's size in position is related to its size in momentum (§4). In "A suggestion for unifying quantum theory and relativity" he notes that Einstein's static closed universe has "an upper limit for the distance between two points, given by the radius a of the universe", and writes: "Let us transfer this consideration to the p-space." Momentum space gets its own Einstein-type equations, with their own constants, and "for systems of some kind there is an upper limit for momenta, determined by the radius b of the hypersphere", so the number of states in a volume V is finite. He does not connect the two radii: "Whether these nuclear constants are connected with the corresponding molar constants λ, κ cannot be decided yet." (λ and κ are Born's symbols for the constants of the position-space equations; this λ is not the Born length.)

He fixes b from the classical electron radius r₀ by r₀ = h/(πb), so bc = 2ħc/r₀ ≈ 1.4×10⁸ eV [V], a particle scale, and leaves open "whether the constant b is universal, or characteristic for each energetically closed system". He opens by rejecting Eddington's attempt "to link the properties of the smallest particles to those of the whole universe". In 1949 he splits ħ = ab into a length and a momentum and fixes the length from particle masses. Neither paper uses the Planck length (§4). Both papers had been cited across the record from model memory (†); for this note they were retrieved and read (root `CLAUDE.md`, "Since the handoff", queue item 1; `notes/phase-space-diameter-worklog.md`, entry of 2026-10-26, 15:30; [the † literature battery](/wiki/method/literature-battery)).

### The Cohen–Kaplan–Nelson bound

The Cohen–Kaplan–Nelson (CKN) bound requires that an effective field theory in a box of size L, cut off at energy Λ_UV, hold no more energy than a black hole of the same size: "L³Λ⁴ ≲ L M_P²", so Λ_UV ≲ (M_P/L)^{1/2} in natural units, with M_P the unreduced Planck mass. For an infrared cutoff at the present horizon they find "Λ ∼ 10^{−2.5} eV"; with L = c/H₀ the bound is 4.19 meV [V]. In their formulas Λ is the ultraviolet cutoff, not the cosmological constant. They add: "This observation does not predict the cosmological constant's value" [S: CKN 1999] (§4). The bound and its place in the vacuum-energy problem are set out on [the cosmological-constant problem](/wiki/gravity/spin-2-fields/cosmological-constant-problem#ultraviolet-and-infrared-cutoffs-tied-by-gravity-t).

### The program's toy model II

In the Grosse–Wulkenhaar model, the program's [toy model II](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar), the strength Ω of the harmonic term sets the minimal momentum, and Grosse and Wulkenhaar "identify the parameter √Ω with the ratio of the Planck length to the size of the (finite!) universe" [S: Grosse–Wulkenhaar 2005]. The model is self-dual under the exchange of position and momentum at Ω = 1, a universe of Planck size; for L = c/H₀, Ω = (l_P/L)² = 1.4×10⁻¹²² [V] (§4).

### Born geometry

Freidel–Kowalski-Glikman–Leigh–Minic (FKGLM) work in the modular, or Born, geometry that this program builds on ([Born geometry](/wiki/phase-space/born-geometry)). They fix only the area of a phase-space cell: "λε = 2πℏ … the quantum area constraint. Whereas the area of the modular cell is fixed by this quantum constraint, its shape is not". They write the position and momentum cutoffs as L = N_q λ and M = N_p ε, and find

```text
LM/2πℏ = N^(1/4)
```

which they read as "the cutoffs on space and momentum are not separately arbitrary but are inversely related". Setting N equal to the horizon's gravitational entropy, they obtain ρ ≲ ħ/(ℓ²ℓ_P²), a momentum cutoff "M ∼ ℏ/√(ℓℓ_P)", and "the above geometric mean of the Hubble scale and the Planck length is λ ∼ (ℓℓ_P)^{1/2} ∼ 10^{−4} m, which corresponds to the observed vacuum energy scale of M ∼ 10^{−3} eV" [S: FKGLM 2023; also their essay "On the inevitable lightness of vacuum"]. Here ℓ is the Hubble scale and λ their cell length. They take λ to be "not universal but instead … chosen in the context of the system in question" (§4). Their regulated phase space is not the Fourier box, since their momentum cutoff is ħ/√(ℓℓ_P) itself, "though both carry the same length" (§4).

Berglund–Hübsch–Minic (BHM) write the same scale as l_Λ = √(l l_P) with λ_cc = l_P²/l_Λ⁴, and say that "the curvature of the dual spacetime is the cosmological constant of the observed spacetime, while the size of the dual spacetime is the gravitational constant" [S: BHM 2023] (§4).

### Padmanabhan and the extended uncertainty relations

Earlier versions of the geometric-mean length are Padmanabhan's L_DE = √(L_P L_Λ), under the heading "Geometrical Duality in our Universe" [S: Padmanabhan 2006], and the extended uncertainty relations, which carry both a minimal length and a de Sitter scale (§4). Bambi and Urban's relation is invariant under

```text
Δx → (α/β)^(1/2) (L_X L_Pl) Δp,      Δp → (β/α)^(1/2) (L_X L_Pl)⁻¹ Δx,      L_X = L_Λ  (ħ = 1)
```

which is ρ_λ with λ² ∝ l_P L_Λ [S: Bambi–Urban 2008]; α and β are their constants. Bolen and Cavaglià motivate the same form by "the symmetry of the symplectic space" [S: Bolen–Cavaglià 2005]. A count of modes crossing the Hubble radius has also been used to fix Λ [S: Padmanabhan and Padmanabhan, "CosMIn"] (§4).

### Snyder–de Sitter, implicitly

In the Snyder–de Sitter algebra, which deforms the commutation relations of positions and momenta with two scales [T], a duality exchanges position with momentum and Λ with the Planck area, and "connects the high-energy/short-distance regime, governed by the Planck area Ω, with the low-energy/long-distance regime, governed by the cosmological constant Λ" [S: Mignemi 2010]. Its self-dual length, λ⁴ ∝ Ω/Λ, "is implicit there" (§4). Mignemi writes no geometric-mean length and does not call the duality Born's (round-5 ruling R10).

## It is the Cohen–Kaplan–Nelson cutoff [T][V]

The energy that belongs to the self-dual length is the CKN bound (§7):

```text
ħc/√(l_P L) = √(E_P ħc/L)
```

which is the cutoff (M_P/L)^{1/2} of the previous section with E_P the unreduced Planck energy ([two conventions for the Planck mass](/wiki/gravity/spin-2-fields/planck-units#two-conventions-for-the-planck-mass-t)). Other conventions change it by a factor of order one [V]:

| Convention | Factor |
| --- | --- |
| the reduced Planck mass in place of the unreduced | 0.45 |
| an explicit black-hole mass for a sphere of size L (M_BH = Lc²/2G) | 0.59 |
| an explicit black-hole mass for a cube of size L (r_s = L) | 0.84 |
| the vacuum energy taken as one scalar field's zero-point energy Λ⁴/16π² | 2.08 |

The factors are printed by `verify/phase_space_diameter.py`; round-5 ruling R9 asked for the assumption behind the last one to be stated.

## The dark-energy match is the Friedmann equation [D][V]

The [dark-energy](/wiki/cosmology/dark-energy) density is ρ_Λ = 3Ω_Λ M̄_P² H₀² (natural units, M̄_P the reduced Planck mass), so (§7)

```text
ρ_Λ^(1/4) / (ħc/√(l_P c/H₀)) = (3Ω_Λ/8π)^(1/4) = 0.535
```

independently of H₀. The fourth power of the CKN energy for L = c/H₀ is M_P²H₀² in natural units, and the Friedmann equation gives ρ_Λ = (3Ω_Λ/8π) M_P²H₀², so the ratio depends on Ω_Λ alone (the wiki's reading of the step). The values: ρ_Λ^{1/4} = 2.24 meV, or 88.1 μm as a length [V; S: Particle Data Group], against 4.19 meV for the Hubble box. In the note's words, "The agreement within a factor of two is the statement that Ω_Λ is of order one today, and carries no further information." The closer agreement for the particle horizon, 2.35 meV against 2.24, "comes from χH₀/c = 3.18, a property of ΛCDM's expansion history", where χ is the particle horizon's comoving distance and ΛCDM the standard cosmological model of a cosmological constant plus cold dark matter (§7).

## De Sitter space as the self-dual state [D][V]

Fix λ² = l_P L_Λ and let the box follow the Hubble radius. Its aspect ratio in units of λ is (§7)

```text
A(t) = (c/H(t)) l_P / λ² = H_Λ/H(t) = √Ω_Λ(t)
```

exactly, in any Friedmann–Lemaître–Robertson–Walker universe, with H_Λ = c/L_Λ and Ω_Λ(t) = Λc²/3H². The aspect ratio is 0.83 today. It was far below one in the radiation and matter eras, and it tends to one as the universe approaches empty de Sitter space; at a turnaround of the expansion it diverges. In this language de Sitter space is the box's self-dual fixed point, and the coincidence that Ω_Λ ~ 1 today becomes the observation that the box is near self-duality now. "The statement holds by construction, because λ was built from L_Λ." `verify/phase_space_diameter.py` checks the identity at several epochs of the ΛCDM expansion history and finds it holding to rounding error.

The turnaround is the far-future event the program reads as [the conjugate bounce](/wiki/cosmology/scale-factor-duality/conjugate-bounce), whose premise the record leaves unresolved (flag 27 in `review/wiki-build-flags.md`). The flag's addendum (2026-10-27) finds that with τ's potential as written the turnaround needs a closed universe ([a closed Comatter universe](/wiki/cosmology/scale-factor-duality/closed-universe)).

Related models are in the literature [T] (§7). A box that instead follows c/H(t) with λ² = l_P c/H(t) gives a vacuum energy that tracks the matter density, which is excluded [S: Hsu 2004]; holographic dark energy with the event horizon as its infrared length is the variant that survives [S: Li 2004]. And "a dual-spacetime model with ultraviolet–infrared mixing, in the Born-geometry lineage, gives a dark energy that varies in time with w > −1, which its authors find compatible with DESI" [S: Hur, Jejjala, Kavic, Minic and Takeuchi 2025]. Here w is dark energy's [equation of state](/wiki/cosmology/dark-energy/quintessence), its pressure divided by its energy density, and DESI is the survey of the [Dark Energy Spectroscopic Instrument](/wiki/cosmology/dark-energy/desi).

## The cosmological constant as a reciprocity image [T][D]

Equivalently, L_Λ = λ²/l_P: the de Sitter radius is where ρ_λ sends the Planck momentum ħ/l_P. Then (§7)

```text
Λ = 3 l_P² / λ⁴,        λ/l_P = 3.2×10³⁰ = √(L_Λ/l_P)
```

[D][V], which is BHM's λ_cc = l_P²/l_Λ⁴ "up to the factor 3 they drop" [S]. The [cosmological-constant problem](/wiki/gravity/spin-2-fields/cosmological-constant-problem), Λl_P² ~ 10⁻¹²², becomes the hierarchy λ/l_P = 3.2×10³⁰. The script prints log₁₀(Λl_P²) = −121.5 against log₁₀(λ/l_P) = 30.5. The note's verdict: "This takes the fourth root of the problem and explains nothing while λ is defined through Λ. It would predict Λ only if λ were fixed by other physics." (§7)

## Numerology lies close at hand [V]

The note records three coincidences and gives none of them a mechanism (§7):

- **A TeV square.** In units of λ = √(l_P L_Λ), today's radiation rectangle would be square at k_BT ≈ 1.0 TeV, near the electroweak scale, counting the Standard Model's g_s, the effective number of species in the entropy ([the radiation era](/wiki/cosmology/early-universe/radiation-era)); for the photons alone it is 1.7 TeV.
- **Two geometric means.** That number is √(k_BT₀E_P) = 1.7 TeV up to the g_s factor, "a different geometric mean from the 5.2 TeV, √(ρ_Λ^{1/4}E_P), of Berglund, Hübsch and Minic's see-saw" [S].
- **A solar-system length.** The Born length that makes today's radiation rectangle itself square is √(ħD_x/D_p) = 3.7×10¹¹ m, about 2.5 au, the au (astronomical unit) being the mean Earth–Sun distance.

"Nothing here gives such coincidences a mechanism, and this note claims none." (§7) Round-5 ruling R6 corrected the first two items in version 1.1. The radiation rectangle is square, in Planck units, only before the radiation existed ([Obituary: the square rectangle at the bounce](/wiki/cosmology/scale-factor-duality/square-at-the-bounce)).

## Why the program cannot choose the length by context

FKGLM's length depends on the system. The note draws the contrast at the head of its consequences:

> "FKGLM let their reference length depend on the system under study. This program cannot: its reciprocity is one exact symmetry with one Born length. That length could enter in two places." (§8, plain-language passage)

Born left the same choice open in 1938, "whether the constant b is universal, or characteristic for each energetically closed system", which the note calls "the contextual choice that FKGLM make" (§4). Reciprocities with different Born lengths are different maps, which differ by a squeeze, ρ_{λ₁}ρ_{λ₂}⁻¹ = diag((λ₁/λ₂)², (λ₂/λ₁)²) [D][V] (§5).

The program's dynamics do not fix the length either [D] (§5). Its geometric action is invariant under the rigid Sp(2d, ℝ), which acts transitively on the [Siegel domain](/wiki/phase-space/modular-field/siegel-domain) and so moves the self-dual point Z = i anywhere, and "the action therefore singles out no Born length". A length enters only through reference structures: the reference axes of the [ρ-preserving potential](/wiki/symmetry-breaking/rho-preserving-potential), [matter's coupling to the polarization](/wiki/symmetry-breaking/matter-coupling), and #13, which sets λ = l_P "in one untagged sentence" (§5).

The two places one Born length would enter are the [maximum force](/wiki/conjugate-relativity/maximum-force) of #13 and the range of the [momentum graviton X](/wiki/gravity/momentum-graviton). The self-dual length is excluded in both: the maximum force would be 1.4×10⁻¹⁷ N, and in the program's aligned bimetric vacuum X's force would sit where torsion balances exclude a gravitational-strength force ([Obituary: the self-dual length as a program scale](/wiki/cosmology/scale-factor-duality/self-dual-length-obituary)). The second exclusion leaves a bound, [the laboratory bound on X's range](/wiki/gravity/momentum-graviton/range-bound).

## What would make it a prediction

The note: "§7's reformulation of Λ would become a prediction only if the program derived λ, or M_X, from its own dynamics." (§8.6) The record derives neither. The program's action singles out no Born length (§5), and the mass M_X of X has "no value in the record" (§8.2), only the lower bound M_X c² > 5.2 meV that holds in the aligned vacuum.

## History

- **The question.** Paul asked on 2026-10-26: "Investigate or explain if there is a relationship between the size of our universe in position space and momentum space. Speculate and work through the consequences if so." (`notes/phase-space-diameter-worklog.md`).
- **The literature sweep.** Run for the note before its first version, it found the length in FKGLM 2023 and in Berglund–Hübsch–Minic, Padmanabhan, the Snyder–de Sitter algebra and Cohen–Kaplan–Nelson, and Born 1938 was read in full, with its pairing of the two radii; the worklog records that the section "is now [T]" (entry of 2026-10-26, 15:30).
- **Round 5.** The pre-registration predicted "no prior art for the self-dual length beyond what §4 and §7 already cite". The referees found more: Bambi–Urban and Bolen–Cavaglià as explicit prior art, and Sundrum and Kapner et al. for the test at the dark-energy length. The adjudication scored the prediction a miss. Rulings R6 to R10 and R15 corrected the TeV numerology, replaced "halves the exponent" by the fourth root, recorded that BHM write the relation without the factor 3, spelled out the CKN conventions, made Mignemi implicit prior art, and added the omitted references ([round 5](/wiki/method/review/round-5)).
- **Version 1.1** (2026-10-26) applies the rulings.

## Sources

- `papers/phase-space-diameter.md` §7 — the box, the self-dual length and its table, the CKN identity and its conventions, the Friedmann identity 0.535, A(t) = √Ω_Λ(t), Λ = 3l_P²/λ⁴, the numerology, Hsu 2004, Li 2004 and Hur et al. 2025
- `papers/phase-space-diameter.md` §4 — the sampling count, holography, the CKN bound, Born 1938 and 1949, Grosse–Wulkenhaar, the Born-geometry literature and the extended uncertainty relations, with the quotations
- `papers/phase-space-diameter.md` §5 — ρ_λ on a rectangle; the squeeze between two Born lengths; the program fixes no λ
- `papers/phase-space-diameter.md` §2 — the four pairings of a size in position with a size in momentum
- `papers/phase-space-diameter.md` §8, §8.1, §8.6 — the contextual length against one exact reciprocity; A = L/l_P at λ = l_P; what would make the reformulation a prediction
- `papers/phase-space-diameter.md` §9, 'References' — the summary tags; the citations, all [S]
- `verify/phase_space_diameter.py` — sections "Extent, resolution and the published answers (note §4)" and "The self-dual box (note §7)"
- `review/round5-adjudication.md` 'Rulings' R6–R10, R15, 'Pre-registration scored' — the corrections and the novelty prediction
- `review/round5-preregistration.md` 'Predictions' — the novelty prediction
- `notes/phase-space-diameter-worklog.md` 'Status' — the question and the literature sweep
- `CLAUDE.md` 'Since the handoff' — the self-dual length as prior art; Born 1938 and 1949 retrieved for the note
- `review/wiki-build-flags.md` item 27 — the turnaround's premise, awaiting Paul's ruling; its addendum and `notes/closed-universe.md` §2 — the turnaround in a closed universe
