---
title: "The phase-space diameter relation"
weight: 70
status: alive
description: "For blackbody radiation filling a fixed comoving region, diameter times momentum spread is D_x·D_p = κ h N_γ^{1/3} with κ = 1.708: an identity of blackbody statistics, constant since reheating up to entropy steps; the chat's ~10⁹⁰ is the radiation entropy; a·ã = 1 is its one-cell form, and it holds in standard cosmology, so it cannot test the program; the aspect ratio, 5.2×10⁹² in Planck units today, is a clock and a distance from self-duality."
provenance: [T, D, V]
sources:
  - "papers/phase-space-diameter.md §3"
  - "papers/phase-space-diameter.md §2"
  - "papers/phase-space-diameter.md §5"
  - "papers/phase-space-diameter.md §6"
  - "papers/phase-space-diameter.md §4"
  - "papers/phase-space-diameter.md §8.6"
  - "papers/phase-space-diameter.md §9"
  - "verify/phase_space_diameter.py 'The conserved area (note §3)'"
  - "verify/phase_space_diameter.py 'Extent, resolution and the published answers (note §4)'"
  - "verify/phase_space_diameter.py 'Reciprocity on a rectangle; wave packets (note §5)'"
  - "verify/phase_space_diameter.py 'Where the radiation rectangle is square, lambda = l_P (note §6)'"
  - "review/round5-adjudication.md 'Verdict'"
  - "review/round5-adjudication.md 'Rulings' R2–R4"
  - "review/round5-adjudication.md 'Recommendations to Paul'"
  - "review/round5/manuscript-v1.0.md §2–§4"
  - "CLAUDE.md 'Since the handoff'"
  - "HANDOFF.md §4"
  - "HANDOFF.md §8 item 7"
  - "review/wiki-build-flags.md items 23, 24"
---

*The phase-space diameter relation states that the radiation filling a region of the expanding universe occupies an area of [phase space](/wiki/phase-space) that does not change: along each of the three axes, the region's diameter D_x times the spread of the radiation's momenta D_p equals Planck's constant h times the cube root of the number of photons, up to a coefficient of order one. The [expansion](/wiki/cosmology/scale-factor-duality/friedmann-cosmology) stretches every light wave by the same factor, and a stretched wave has a proportionally narrower spectrum, so D_x grows with the scale factor while D_p falls by the same factor; the relation is the cosmological form of the [time–bandwidth product](/wiki/phase-space/reciprocity/fourier-transform#the-timebandwidth-product) of signal analysis. It entered the program as a conjecture from the early chat sessions. The phase-space-diameter note of 2026-10-26 showed it to be an identity of blackbody statistics that holds in standard cosmology with or without the program's reciprocity, so it cannot test the program. What changes with time is the ratio of the two sizes, which grows as the square of the scale factor and, once a reference length is chosen, measures how far the radiation is from the square shape that [Born reciprocity](/wiki/phase-space/reciprocity/born-reciprocity) leaves unchanged. The original conjecture's claim that the rectangle was square at a bounce [is dead](/wiki/cosmology/scale-factor-duality/square-at-the-bounce).*

**Status:** Alive, as standard physics — the identity and its coefficient [D][V], the constancy of the area for a fixed comoving region [T], today's values [V] (`papers/phase-space-diameter.md` §3, §9) — every number the note computes is checked by `verify/phase_space_diameter.py` ([the phase-space-diameter script](/wiki/method/verification/phase-space-diameter-script)), and the note went through [round 5](/wiki/method/review/round-5) of blind review, verdict B from both referees, with version 1.1 applying the revisions. The relation holds in standard cosmology, with or without the program's reciprocity, so it can neither confirm nor refute the program (note §3, §8.6). Its chat-only clause "square exactly at the bounce" is withdrawn: [Obituary: the square rectangle at the bounce](/wiki/cosmology/scale-factor-duality/square-at-the-bounce).

## Statement

The note's form of the relation, for blackbody photons at temperature T filling a sphere (`papers/phase-space-diameter.md` §3) [D][V]:

```text
D_x · D_p = κ · h · N_γ^(1/3),     κ = 3^(1/3) π^(10/3) / (30 ζ(3)^(4/3)) = 1.708
```

- **D_x** is the diameter of the sphere.
- **D_p** = 2⟨|p|⟩ = 2(π⁴/30ζ(3)) k_BT/c is twice the mean photon momentum, with k_B Boltzmann's constant and ζ the Riemann zeta function.
- **N_γ** = (2ζ(3)/π²)(k_BT/ħc)³ · (π/6)D_x³ is the photon count: the blackbody number density times the volume of the sphere.

The identity holds "for every T and every radius" (note §3). With these definitions D_p is proportional to T and N_γ^{1/3} to the product T·D_x, so both sides are proportional to D_x·T and their ratio is the fixed number κ (the wiki's reading of the definitions). In the note's words, "It is the blackbody number density rewritten, not a separate law." [The phase-space-diameter script](/wiki/method/verification/phase-space-diameter-script) checks the identity and the value of κ.

**The coefficient depends on the definitions [V].** With D_p = k_BT/c in place of twice the mean momentum, κ = 0.316; with D_p = ⟨|p|⟩, κ = 0.854; for a cube of side D_x in place of the sphere, κ = 1.377. The chat's D_x·D_p = h·N^{1/3} "is therefore exact for radiation once the diameters are defined, with a coefficient of order one in place of 1" (note §3).

**Per axis.** The rectangle lies in one position–momentum plane, and the relation holds in each of the three: the area per axis, in units of h, is κ N_γ^{1/3} (note §2). This is the chat's "per dimension".

## Which sizes are paired

A size in position has one obvious meaning; a size in momentum has three. It can be the spread of momenta that the universe's contents carry, the finest difference in momentum that a universe of finite size can resolve, or the largest momentum available, set by the smallest meaningful length. Each pairs with a different size in position, and the pairs behave differently as the universe expands (note §2, plain-language passage). The note's table [D]:

| Pairing | Size in position | Size in momentum | Area per axis, in units of h | As the universe expands |
| --- | --- | --- | --- | --- |
| Radiation rectangle | D_x, the diameter of a fixed comoving region (here today's observable universe) | D_p, the momentum spread of the radiation in it | κ N_γ^{1/3} | area fixed; aspect ratio grows as a² |
| Hubble rectangle | 2c/H, the diameter of the Hubble sphere | the radiation's momentum spread | κ N_H^{1/3}, N_H the photons inside the Hubble sphere | area grows as N_H^{1/3} |
| Fourier box | from the Planck length l_P to a large length L | from ħ/L to ħ/l_P | L/(2π l_P) | grows with L |
| One cell | one wavelength w | h/w, the de Broglie momentum | 1 | area fixed; this is a·ã = 1 |

Here a is the scale factor and H the Hubble rate, so the Hubble sphere has radius c/H. The chat's numbers fit the radiation rectangle of today's observable universe (note §2–§3), and that pairing is the relation on this page. The Hubble rectangle is one of the readings tested on [the obituary of the square](/wiki/cosmology/scale-factor-duality/square-at-the-bounce); the Fourier box is [the self-dual cosmic box](/wiki/cosmology/scale-factor-duality/self-dual-cosmic-box); the one-cell row is [the cosmological constraint a·ã = 1](/wiki/cosmology/scale-factor-duality/cosmological-constraint). Version 1.0 of the note gave the one-cell row the momentum "ħ over that wavelength", whose cell has area ħ rather than h; round-5 ruling R3 corrected it to the de Broglie momentum h/w (`review/round5/manuscript-v1.0.md` §2).

## Background: the time–bandwidth product [T]

A waveform stretched in time has its spectrum compressed by the same factor, so the product of its duration and its bandwidth is unchanged ([waveform and spectrum](/wiki/phase-space/reciprocity/fourier-transform#waveform-and-spectrum)). The product also counts how much a signal can carry. The note quotes the sources (§3): a signal limited to a duration T and a bandwidth W "can be specified by giving 2TW numbers" [S: Shannon 1949], an "engineering folk theorem" whose rigorous version Slepian reviews [S: Slepian 1983]. Gabor drew signals in a time–frequency plane whose "areas … are proportional to the number of independent data which they can convey", and noted that his results "could have been formally obtained by replacing a co-ordinate x by t, the momentum p by f, and Planck's constant h by unity" [S: Gabor 1946].

The position–momentum version is the [uncertainty principle](/wiki/phase-space/reciprocity/canonical-commutator). In phase space a cell has area h per position–momentum pair (Weyl's law), and radiation at occupation number of order one holds about one quantum per cell (note §3) [T]. The rectangle's area therefore counts the quantum cells the radiation occupies, about 10³⁰ along each axis for the observable universe (note §3, plain-language passage).

## Why the area is conserved [T]

**Liouville's theorem in an expanding universe.** In a Friedmann–Lemaître–Robertson–Walker universe, the uniform expanding universe of standard cosmology, a freely moving particle's momentum, measured by observers at rest in comoving coordinates, falls as 1/a, and the distribution of free-streaming particles in phase space is conserved along their paths, which is [Liouville's theorem](/wiki/phase-space/reciprocity/symplectic-form#the-symplectic-group) [S: Ma and Bertschinger 1995; Tsagas, Challinor and Maartens 2008]. A blackbody spectrum stays Planckian with T ∝ 1/a (note §3). The fall of momentum as 1/a is derived on [redshift](/wiki/cosmology/scale-factor-duality/redshift#the-momentum-of-free-particles).

**Which region [T][D].** The area is constant for "a fixed comoving region of a homogeneous radiation bath": D_x ∝ a and D_p ∝ 1/a. It is not the bounding box of a fixed set of photons, which spreads as they stream, and it is not the area of a region that grows in comoving size, such as the particle horizon or the Hubble sphere (note §3). The Hubble rectangle's area grows as N_H^{1/3} (note §6).

**Since when.** For a fixed comoving region (note §3):

- the photon number is conserved once electron–positron annihilation is over (k_BT ≪ m_e c²); before it, the region held 4/11 of today's comoving photon number [T][V];
- throughout, from reheating on, the conserved quantity is the comoving entropy, S ∝ g_s(T)(aT)³, with g_s the effective number of relativistic degrees of freedom counted for entropy ([the radiation era](/wiki/cosmology/early-universe/radiation-era#entropy-and-the-yield-y--ns-t)). The area scales as aT, so it changes as g_s^{−1/3}: by (11/4)^{1/3} = 1.40 for the photons across annihilation, and by (106.75/3.909)^{1/3} = 3.01 across all the Standard Model's thresholds [V];
- before [reheating](/wiki/cosmology/early-universe/inflation-and-dilution#reheating-t) at the end of inflation the region held no radiation. "The area counts occupied cells; it was created at reheating and is not a constant of nature."

The same conservation laws are set out as established physics on [redshift](/wiki/cosmology/scale-factor-duality/redshift#conserved-counts-in-a-comoving-region-t).

## Today's values [V]

The note evaluates the relation for the comoving region that is today's observable universe, of radius 46.1 Gly (billion light-years) for the Planck 2018 parameters H₀ = 67.4 km s⁻¹ Mpc⁻¹ and Ω_m = 0.315 [S], with the temperature of the [cosmic microwave background](/wiki/cosmology/early-universe/cosmic-microwave-background#a-blackbody-spectrum) T₀ = 2.7255 K [S: Fixsen 2009; Particle Data Group] (note §3):

- the rectangle's sides are D_x = 8.73×10²⁶ m and D_p = 6.78×10⁻³¹ kg m s⁻¹, and its area is D_x D_p = 8.9×10²⁹ h;
- the photon number is N_γ = 1.43×10⁸⁹, and the entropy of photons and neutrinos is S = 1.01×10⁹⁰ k_B;
- the entropy per photon is 7.04 with neutrinos counted, 3.60 for photons alone.

The chat's "~10⁹⁰" is S, not N_γ. Its "~10³⁰ h per dimension" fits both the area, 8.9×10²⁹ h, and S^{1/3} = 1.0×10³⁰ (note §3).

## What N counts [T]

"The relation's N is the radiation's photon count, or its entropy. It is not 'the universe's entropy'" (note §3). Egan and Lineweaver's budget for the observable universe puts the photons at 5.40×10⁸⁹ k and the supermassive black holes at about 3×10¹⁰⁴ k [S: Egan–Lineweaver 2010, Table 1], and the cosmic event horizon at 2.6×10¹²² k [S: Egan–Lineweaver 2010, Table 2], k being Boltzmann's constant. Black holes and the [horizon](/wiki/cosmology/dark-energy/de-sitter-space#the-horizon) dominate the universe's entropy (note §1, §9). Black-hole and horizon entropies are not counts of phase-space cells occupied by free quanta, and they do not enter the relation. Version 1.0 of the note cited Table 1 for the horizon's figure; both round-5 referees found it in Table 2, and ruling R4 upheld the correction.

## The program's reading [D]

The program's [cosmological constraint a·ã = 1](/wiki/cosmology/scale-factor-duality/cosmological-constraint) states that the rigidity of the [symplectic form](/wiki/phase-space/reciprocity/symplectic-form) ω, the statement that Planck's constant does not run, keeps the volume of every comoving phase-space cell fixed, so the scale factor ã of the momentum description, the [conjugate universe](/wiki/program/conjugate-universe), is the reciprocal of a ([#11](/wiki/history/documents/checkpoint) §10). The note reads this as the area statement for one cell (§3):

> The rectangle's area is the number of occupied cells times the area of one; a·ã = 1 fixes only the second factor, and the first is the radiation's entropy, set at reheating. In general relativity the one-cell statement already holds, because a free particle's comoving momentum is conserved [T]. The diameter relation therefore holds in standard ΛCDM cosmology, with or without reciprocity, and cannot test the program.

ΛCDM is the standard cosmological model of a [cosmological constant](/wiki/cosmology/dark-energy/cosmological-constant) plus cold dark matter. The note's closing assessment is the same: "Nothing in §3–§6 goes beyond ΛCDM, so none of it can confirm or refute the program" (§8.6).

## The aspect ratio: a clock and a distance from self-duality

**Reciprocity keeps the area and inverts the shape [T][V].** Born reciprocity exchanges position and momentum, and to exchange a length with a momentum it needs a reference length, the [Born length](/wiki/phase-space/reciprocity/born-length) λ, with ħ/λ as the matching momentum. In ordinary units (note §5):

```text
ρ_λ:   x′ = (λ²/ħ) p,     p′ = −(ħ/λ²) x
```

The map is symplectic for every λ. It sends a rectangle of extents (L, P) to one of extents (λ²P/ħ, ħL/λ²), so the area L·P is invariant; the aspect ratio in units of λ, A = (L/λ)/(P/(ħ/λ)) = ħL/(λ²P), goes to 1/A; and the rectangle is self-dual, A = 1, exactly when λ² = ħL/P. Every rectangle is therefore self-dual for exactly one λ, the geometric mean of L and ħ/P [D][V].

**The program fixes no Born length [D].** The program's geometric action is invariant under the rigid symplectic group Sp(2d, ℝ), which acts transitively on the [Siegel domain](/wiki/phase-space/modular-field/siegel-domain) and so moves the [self-dual point Z = i](/wiki/phase-space/modular-field/modular-inversion#the-fixed-point-the-self-dual-vacuum-z--i) anywhere; the action singles out no Born length (note §5). "Planck units" means λ = l_P, the choice that #13, the program's [dual special relativity](/wiki/conjugate-relativity), makes in one untagged sentence (#13 §1; note §5, §6). "Square" has a meaning only once λ is fixed.

**Wave packets [T][D][V].** In units with ħ = λ = 1, a Gaussian wave packet ψ_Z(x) ∝ exp(iZx²/2) is labelled by a point Z = X + iY of the upper half-plane, and the Fourier transform sends Z to −1/Z, which is the program's reciprocity Z → −Z⁻¹ on its [modular field](/wiki/phase-space/modular-field/modular-field-z) realized on wave packets. A packet's position and momentum widths satisfy Δx/Δp = 1/|Z|, so three sets that appear in the record's statements about self-duality are distinct: |Z| = 1 is the set of square rectangles, Z = i is the one round state, and det H_Z = 1, for the generalized metric H_Z, holds at every Z, so that a·ã = 1 holds along the whole slice X = 0 (note §5). With the half-plane metric ds² = (dX² + dY²)/Y², the distance from i to iY is |ln Y| = |ln(Δx/Δp)|, and in the convention σ_x = e^r/√2 for a squeezed vacuum it is 2r. The note adds that "A 'distance from self-duality' is defined only once its metric and its λ are named." The construction is set out on [Gaussian wave packets on the Siegel half-plane](/wiki/phase-space/modular-field/gaussian-states).

**The clock [D][V].** A comoving cell's extents scale as a and 1/a, so its aspect ratio in units of λ grows as a², and its point moves along the imaginary axis away from Z = i: a distance of 2 ln(a/a_sd) per axis, where a_sd is the scale factor at which the cell was square, advancing at twice the Hubble rate (note §5). For the radiation of today's observable universe in Planck units:

- the aspect ratio is A₀ = 5.2×10⁹² (log₁₀ A₀ = 92.72), matching the chat's "~10⁹²" (note §6);
- the distance is ln A₀ = 213.5 per axis, or 369.8 for the isotropic point in degree 3, which is 106.7 e-folds of expansion since the square (note §5).

"This is the content of the chat's 'aspect ratio … = a clock measuring distance from self-duality'. It reparametrizes ln a and adds no dynamics" (note §5). In wave terms, the clock reads how far the radiation's waveform has been stretched, and its spectrum compressed, since the two had equal extents in units of λ.

**A physical version [T][S].** The aspect ratio in units of λ depends on the choice of λ. The squeezing of cosmological perturbations is an aspect ratio that does not depend on it and is observed: after a quantum fluctuation's wavelength leaves the Hubble radius during inflation, its state is squeezed relative to its own vacuum, with the squeezing parameter growing as r_k ≃ ln(a/a_k) (R_k in Albrecht et al.), the number of e-folds since the mode left the Hubble radius [S: Albrecht, Ferreira, Joyce and Prokopec 1994]: about 50 at the end of inflation [S: Martin–Vennin 2016], and about 100–120 today on the largest observed scales [S: Kiefer–Polarski 2009; Kiefer, Polarski and Starobinsky 1998; Grishchuk 1993] (note §5). Squeezing values depend on the choice of canonical variables [S: Grain–Vennin 2020], and modes stop squeezing once they re-enter the Hubble radius. See [squeezed cosmological perturbations](/wiki/cosmology/early-universe/squeezed-perturbations).

## Where the rectangle is square

Run back in time with D_x ∝ a and D_p ∝ 1/a, the radiation rectangle in Planck units would be square at a/a₀ = 4.4×10⁻⁴⁷, where T = 4.4×10¹⁴ T_P (T_P the Planck temperature): above the Planck temperature, where no physics is tested, and before reheating created the radiation; since reheating the rectangle has been elongated by at least 10³⁵. At a far-future turnaround, which the program reads as the [conjugate universe's bounce](/wiki/cosmology/scale-factor-duality/conjugate-bounce), the aspect ratio is at its largest. Drawn around the Hubble sphere instead, the rectangle is square at 0.28 T_P, which is dimensional analysis at the Planck time rather than a result. No reading the note tested puts a square rectangle at a bounce for one region, and the chat's "square exactly at the bounce" is withdrawn [D][V] (note §6). The readings, their numbers and the probable origin of the claim are on [Obituary: the square rectangle at the bounce](/wiki/cosmology/scale-factor-duality/square-at-the-bounce).

## Beside the published relations

**Freidel–Kowalski-Glikman–Leigh–Minic (FKGLM).** Working in the Born geometry this program builds on, FKGLM fix only the area of a phase-space cell and find that the position and momentum cutoffs L and M of a regulated phase space satisfy L·M/2πℏ = N^{1/4}, which they read as "the cutoffs on space and momentum are not separately arbitrary but are inversely related" [S: FKGLM 2023] (note §4). The note compares the two relations [D][V]:

> Both relations multiply a position extent by a momentum extent and equal a power of a count N. They count different things: the chat's N is the radiation entropy, 10⁹⁰, taken per spatial axis (N^{1/3}); FKGLM's is the horizon entropy, 10¹²², taken per spacetime dimension (N^{1/4}). Their per-axis counts are 1.0×10³⁰ and S_dS^{1/4} = 4.3×10³⁰; both are conserved for a fixed comoving region, so their ratio, 0.235, does not change [V].

Here S_dS is the entropy of the de Sitter horizon, π L_Λ²/l_P² for the de Sitter radius L_Λ (note §4).

**The Cohen–Kaplan–Nelson saturation.** The two kinds of count are linked by the maximal entropy of Cohen–Kaplan–Nelson (CKN): when their bound is near saturation, "the entropy is S_max ≃ S_BH^{3/4}" [S: CKN 1999, eq. 3], S_BH being the entropy of a black hole the size of the region. Radiation filling a Hubble sphere in the radiation era nearly saturates the bound, so its per-axis count S^{1/3} equals the horizon's per-dimension count S_BH^{1/4} within a factor of 0.79–1.05, at every temperature [V] (note §4). Version 1.0 of the note said that the closeness of the two counts "holds at no other epoch". Round-5 ruling R2 upheld the referees' objection: for the fixed comoving region both counts are conserved, so their ratio is the same at every epoch, and version 1.1 gives the CKN explanation instead.

FKGLM's cell length, the geometric mean of the Planck length and the horizon radius, is also the length for which the Fourier box of the table above is self-dual, although their regulated phase space is not that box (note §4): see [the self-dual cosmic box](/wiki/cosmology/scale-factor-duality/self-dual-cosmic-box).

## Scope and caveats

- **It tests nothing in the program.** The relation, its conservation and its clock are standard cosmology (note §3, §8.6).
- **The coefficient is a convention.** κ depends on how D_x and D_p are defined, from 0.316 to 1.708 for the definitions above.
- **A fixed comoving region.** The area is conserved for a fixed comoving region of a homogeneous bath, not for a fixed set of photons or for a region that grows in comoving size.
- **Not the universe's entropy.** N is the radiation's photon count or entropy; black holes and the horizon carry far more entropy and do not enter.
- **Square and distance need choices.** Every rectangle is self-dual for one λ, the program's action fixes none, and a distance needs a named metric (note §5).

## Chat-only: the original statement

The relation was first recorded in one bullet of the [handoff document](/wiki/history/documents/handoff), `HANDOFF.md` §4, "Results that exist only in the chat (not in any artifact)" (the heading's "only" is set in capitals in the source):

> Phase-space diameter relation: D_x · D_p = h · N^(1/3) per dimension (cosmic time–bandwidth theorem); the constant = the universe's photon count/entropy (~10⁹⁰, i.e. ~10³⁰ h per dimension); rectangle square (D_x = D_p in Planck units) exactly at the bounce; aspect ratio today ~10⁹² = a clock measuring distance from self-duality. Conjecture-tier; candidate for a future note.

The bullet "defines none of D_x, D_p, N or 'the bounce'" (note §2). Its four claims, and what the note found:

1. **The product**, D_x·D_p = h·N^{1/3} per dimension: exact for radiation once the diameters are defined, with κ = 1.708 in place of 1 [D][V] (above).
2. **The constant**, "the universe's photon count/entropy (~10⁹⁰, i.e. ~10³⁰ h per dimension)": ~10⁹⁰ is the radiation entropy S = 1.01×10⁹⁰ k_B, the photon count being 1.43×10⁸⁹, and ~10³⁰ fits both the area and S^{1/3} [V]. It is not the universe's entropy [T][S].
3. **The square**, "square (D_x = D_p in Planck units) exactly at the bounce": withdrawn [D][V] ([obituary](/wiki/cosmology/scale-factor-duality/square-at-the-bounce)). Flag 24 in `review/wiki-build-flags.md` recorded that the bullet names no bounce; the round-5 adjudication recommends that Paul accept the flag ('Recommendations to Paul'), and it awaits his ruling.
4. **The clock**, "aspect ratio today ~10⁹² = a clock measuring distance from self-duality": 5.2×10⁹² in Planck units [V]; the clock reparametrizes ln a, and the distance is the Siegel distance from Z = i on the slice X = 0 [T][D][V]. The note takes "self-duality" to mean Z = i on that slice (§5). The record identifies a·ã = 1 with the circle |Z| = 1 instead, an identification that flag 23 in `review/wiki-build-flags.md` queries and that awaits Paul's ruling ([the cosmological constraint](/wiki/cosmology/scale-factor-duality/cosmological-constraint#the-geometry-the-z--1-locus)).

The handoff's queue listed "Optional write-ups: phase-space diameter relation note (§4)" (`HANDOFF.md` §8 item 7). The root `CLAUDE.md` records it as done ('Since the handoff'): "the chat-only relation is standard physics: D_x·D_p = κ h N^{1/3} is an identity of blackbody statistics, constant for a fixed comoving region; a·ã = 1 is its one-cell form, and none of it tests the program".

## History

- **Chat era, before 2026-10-19.** The relation and its four claims, with no definitions or derivation.
- **`HANDOFF.md` §4 and §8 item 7 (2026-10-19).** Recorded among the results that exist only in the chat, "Conjecture-tier; candidate for a future note".
- **Wiki build (2026-10-21 to 2026-10-22).** This page carried the relation as a chat-only conjecture; flags 23 and 24 were raised and audited.
- **The note, version 1.0 (2026-10-26).** The identity, the conserved area, the program's reading, the aspect ratio as a distance, the comparison with the published relations and the [obituary of the square](/wiki/cosmology/scale-factor-duality/square-at-the-bounce). [Round 5](/wiki/method/review/round-5) of blind review returned verdict B from both referees; for this page's material its rulings R2, R3 and R4 were upheld (above).
- **Version 1.1 (2026-10-26)** applies the accepted revisions, and the root `CLAUDE.md` records the note as done.

## Sources

- `papers/phase-space-diameter.md` §3 — the identity, κ and its dependence on the definitions, the conserved area and its region, today's values, what N counts, and the program's reading
- `papers/phase-space-diameter.md` §2 — the four pairings, and the chat bullet's missing definitions
- `papers/phase-space-diameter.md` §5 — reciprocity on a rectangle, the program's free Born length, wave packets on the half-plane, the distance and the clock, squeezed perturbations
- `papers/phase-space-diameter.md` §6 — where the rectangle is square (summarized here; details on the obituary)
- `papers/phase-space-diameter.md` §4 — the comparison with FKGLM's relation and the CKN saturation
- `papers/phase-space-diameter.md` §8.6, §9 — what would test the note's results; the summary table and its tags
- `verify/phase_space_diameter.py` — the note's computed numbers, in the sections 'The conserved area (note §3)', 'Extent, resolution and the published answers (note §4)', 'Reciprocity on a rectangle; wave packets (note §5)' and 'Where the radiation rectangle is square, lambda = l_P (note §6)'
- `review/round5-adjudication.md` 'Verdict', 'Rulings' R2–R4, 'Recommendations to Paul' — verdict B; the corrections to this page's material; the recommendation on flags 23 and 24
- `review/round5/manuscript-v1.0.md` §2–§4 — the reviewed version 1.0: the one-cell row, Egan and Lineweaver's Table 1, and "holds at no other epoch", before the corrections
- `CLAUDE.md` 'Since the handoff' — the note done, and its results
- `HANDOFF.md` §4 — the original chat-only bullet
- `HANDOFF.md` §8 item 7 — the optional write-up in the handoff's queue
- `review/wiki-build-flags.md` items 23, 24 — the |Z| = 1 identification, and the bounce the bullet names; both await Paul's ruling
