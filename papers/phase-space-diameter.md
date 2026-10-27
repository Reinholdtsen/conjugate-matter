# The Size of the Universe in Position and in Momentum
### The phase-space diameter relation, what Born reciprocity adds, and a self-dual length

*Version 1.1, 2026-10-26, after the round-5 blind review (verdict B; `review/round5-adjudication.md`). A note of the Comatter program (until 2026-10-26, the Broken-Born program). It writes up the "phase-space diameter relation", a conjecture recorded only in the summary of the program's early chat sessions, tests it, sets it beside the published answers to the same question, and works through what Born reciprocity adds. Every section opens with a plain-language passage (italic), followed by the technical record. Provenance tags: **[D]** derived in this note, **[T]** established literature, **[P]** postulate of the program, **[O]** open, **[V]** machine-verified by `verify/phase_space_diameter.py`. References carry **[S]** (retrieved by live search for this note) or **†** (cited from memory; to be checked against the source before any external use). Program documents are cited as [H1]–[H2] and [P1]–[P6].*

- *v1.1 changes:* §8.2 states the bimetric background ratio (written u here; c in the cited papers) that the coupling to X carries, gives the program's argument for u = 1 and the bound as a function of u; §4 explains the per-axis agreement by the Cohen–Kaplan–Nelson bound instead of a coincidence; §5–§7 add prior art (Bambi–Urban, Bolen–Cavaglià, Albrecht et al., Sundrum, Kapner et al., Li, string cosmology); §6 adds the squeezed-mode and string-cosmology readings. Smaller corrections are listed in the adjudication.

---

## 1. Two abstracts

*In plain terms: For the radiation that fills the universe, its size in position and its size in momentum are tied together exactly. Expansion stretches every light wave by the same factor, and a stretched wave has a proportionally narrower spectrum, so every photon's momentum falls as the universe grows. The radiation's extent in position times its extent in momentum therefore stays fixed, at a value set by the number of photons: about 10⁸⁹ of them, which is about 10³⁰ quantum cells along each axis. This is the cosmic form of the time–bandwidth product of signal analysis, and it is standard cosmology. It holds whether or not position and momentum are symmetric, so it cannot test this program; the program's constraint a·ã = 1 is the same statement for a single cell. What changes with time is the ratio of the two extents, which grows as the square of the scale factor. Born reciprocity, the exchange of position and momentum, leaves the product alone and inverts the ratio, so the ratio is the quantity that says how far the universe's state is from symmetric under the exchange. In Planck units the radiation is about 5×10⁹² times longer in position than in momentum. An early-chat claim that the two extents were equal "at the bounce" fails: the radiation could have been square only at about 10¹⁴ times the Planck temperature, before the radiation existed, and at the program's far-future turnaround it would be at its most elongated. A different pair of sizes, the horizon and the Planck scale, is exactly symmetric under the exchange for one reference length of about 50 micrometres, within a factor of two of the length scale of dark energy. That is already in the literature, including the Born-geometry papers this program builds on, and its match to dark energy is the Friedmann equation restated. The program cannot use that length in either of the two places it could go: it would make the program's maximum force 10⁻¹⁷ newtons, and it would give the program's massive momentum graviton a range that laboratory gravity tests exclude. What survives the second failure is a bound: if the program's vacuum is the one its own equations assume, that graviton's range must be shorter than about 38 micrometres.*

**Technical abstract.** The chat-only relation D_x·D_p = h·N^{1/3} per dimension [H1] is, for blackbody radiation filling a sphere, an identity of blackbody statistics: D_x·D_p = κ h N_γ^{1/3} with κ = 3^{1/3}π^{10/3}/(30ζ(3)^{4/3}) = 1.708 for D_x the diameter and D_p twice the mean momentum [D][V]. Its constancy for a fixed comoving region is Liouville's theorem with photon-number conservation (since electron–positron annihilation) or entropy conservation (since reheating, up to g_s^{−1/3} steps) [T]. For today's observable universe N_γ = 1.43×10⁸⁹ and S = 1.01×10⁹⁰ k_B, so D_x D_p = 8.9×10²⁹ h [V]; the chat's "~10⁹⁰" is the radiation entropy, not the entropy of the universe, which black holes and the horizon dominate [T]. The program's a·ã = 1 fixes the area of one cell, not the number of occupied cells [D]. Born reciprocity ρ_λ preserves the area of a rectangle and inverts its aspect ratio; on Gaussian states it acts as Z → −Z⁻¹ on the Siegel half-plane, where |Z| = 1 is the locus Δx = Δp, Z = i the one Fourier-invariant state, and det H = 1 holds everywhere [T][D][V]. In Planck units the radiation rectangle's aspect ratio is 5.2×10⁹² today and grows as a²; it would be square at T = 0.61 N_γ^{1/6} T_P = 4.4×10¹⁴ T_P, outside any physical epoch, and is greatest at a turnaround. No reading of the chat claim makes it square at a bounce for one region; the claim "square exactly at the bounce" is withdrawn [D][V]. The Fourier box [l_P, L] × [ħ/L, ħ/l_P] is ρ_λ-self-dual exactly when λ = √(l_P L), 47–84 μm for L between c/H₀ and the particle horizon: the Cohen–Kaplan–Nelson length, and the Born-geometry cell length of Freidel, Kowalski-Glikman, Leigh and Minic, who tie it to the vacuum energy [T][S]. Its relation to the dark-energy scale is the identity ρ_Λ^{1/4} = (3Ω_Λ/8π)^{1/4} ħc/√(l_P c/H₀) [D][V], and with λ² = l_P L_Λ the Hubble box's aspect ratio is √Ω_Λ(t) [D][V]. Used as the Born length of the program's dual special relativity, λ = √(l_P L) gives a maximum force of 1.4×10⁻¹⁷ N, which every atom exceeds; used as the range of the momentum graviton X, which in the program's aligned vacuum (background ratio u = 1) couples to ordinary matter with Yukawa strength α = (4/3)u² = 4/3, it is excluded by torsion balances, which then bound X's range below 37.7 μm, M_X c² > 5.2 meV; for u < 0.67 the 47.1 μm end of the self-dual range would be allowed, and the 84.0 μm end needs u < 0.30 [D][V][S].

---

## 2. Three meanings of "size in momentum space"

*In plain terms: A size in position has an obvious meaning. A size in momentum has three. It can be the spread of momenta that the universe's contents actually carry. It can be the finest difference in momentum that a universe of finite size can resolve. Or it can be the largest momentum available, which is set by the smallest meaningful length. Each pairs naturally with a different size in position, and the pairs behave differently as the universe expands. Much of what follows depends on saying which pair is meant.*

The question "is the universe's size in position related to its size in momentum?" has a different answer for each pairing [D]:

| Pairing | Size in position | Size in momentum | Area per axis, in units of h | As the universe expands |
|---|---|---|---|---|
| Radiation rectangle | D_x, the diameter of a fixed comoving region (here: today's observable universe) | D_p, the momentum spread of the radiation in it | κ N_γ^{1/3} | area fixed; aspect ratio grows as a² (§3, §6) |
| Hubble rectangle | 2c/H, the diameter of the Hubble sphere | the radiation's momentum spread | κ N_H^{1/3}, N_H the photons inside the Hubble sphere | area grows as N_H^{1/3} (§6) |
| Fourier box | from the Planck length l_P to a large length L | from ħ/L to ħ/l_P | L/(2π l_P) | grows with L (§4, §7) |
| One cell | one wavelength w | h/w, the de Broglie momentum | 1 | area fixed; this is a·ã = 1 (§3) |

The early-chat relation, whose whole record is one bullet of the program's handoff document [H1],

> "Phase-space diameter relation: D_x · D_p = h · N^(1/3) per dimension (cosmic time–bandwidth theorem); the constant = the universe's photon count/entropy (~10⁹⁰, i.e. ~10³⁰ h per dimension); rectangle square (D_x = D_p in Planck units) exactly at the bounce; aspect ratio today ~10⁹² = a clock measuring distance from self-duality."

defines none of D_x, D_p, N or "the bounce". Its numbers fit the radiation rectangle of today's observable universe (§3). §6 also tests every other reading that has been proposed.

---

## 3. The conserved area: a cosmological time–bandwidth relation

*In plain terms: Expansion stretches every light wave in the universe by the same factor, and a wave stretched in length is compressed in spectrum by that factor. The radiation filling a region that expands with the universe therefore occupies a patch of phase space that grows in position and shrinks in momentum, and the area of that patch does not change. The area counts the quantum cells the radiation occupies, which is about the number of photons. For the observable universe it is about 10³⁰ cells along each axis. The relation holds for radiation in any expanding universe. It involves no symmetry between position and momentum and makes no prediction beyond standard cosmology.*

**Liouville in an expanding universe [T].** In a Friedmann–Lemaître–Robertson–Walker (FLRW) universe a freely moving particle's momentum, measured by comoving observers, falls as 1/a, and the distribution of free-streaming particles in phase space is conserved along their paths (Liouville's theorem) [S: Ma and Bertschinger 1995; Tsagas, Challinor and Maartens 2008]. A blackbody spectrum stays Planckian with T ∝ 1/a.

**Counting cells [T].** A signal limited to a time T and a bandwidth W "can be specified by giving 2TW numbers" [S: Shannon 1949], an "engineering folk theorem" whose rigorous version Slepian reviews [S: Slepian 1983]. Gabor drew signals in a time–frequency plane whose "areas … are proportional to the number of independent data which they can convey", and noted that his results "could have been formally obtained by replacing a co-ordinate x by t, the momentum p by f, and Planck's constant h by unity" [S: Gabor 1946]. In phase space the cell has area h per position–momentum pair (Weyl's law), and radiation at occupation number of order one holds about one quantum per cell.

**The area as an identity [D][V].** Take blackbody photons at temperature T filling a sphere. Let D_x be the sphere's diameter, D_p = 2⟨|p|⟩ = 2(π⁴/30ζ(3)) k_BT/c twice the mean photon momentum, and N_γ = (2ζ(3)/π²)(k_BT/ħc)³ · (π/6)D_x³ the photon count. Then

```text
D_x · D_p = κ · h · N_γ^(1/3),     κ = 3^(1/3) π^(10/3) / (30 ζ(3)^(4/3)) = 1.708
```

for every T and every radius. The coefficient depends on how the two diameters are defined: with D_p = k_BT/c it is 0.316, with D_p = ⟨|p|⟩ it is 0.854, and for a cube of side D_x it is 1.377 [V]. The chat's D_x·D_p = h·N^{1/3} is therefore exact for radiation once the diameters are defined, with a coefficient of order one in place of 1. It is the blackbody number density rewritten, not a separate law.

**Today's values [V].** For the comoving region that is today's observable universe (radius 46.1 Gly for the Planck 2018 parameters H₀ = 67.4 km s⁻¹ Mpc⁻¹ and Ω_m = 0.315 [S]; T₀ = 2.7255 K [S: Fixsen 2009; PDG]), the photon number is N_γ = 1.43×10⁸⁹ and the entropy of photons and neutrinos is S = 1.01×10⁹⁰ k_B. The rectangle's sides are D_x = 8.73×10²⁶ m and D_p = 6.78×10⁻³¹ kg m s⁻¹, and its area is D_x D_p = 8.9×10²⁹ h.

- The chat's "~10⁹⁰" is S, not N_γ; the entropy per photon is 7.04 with neutrinos counted, 3.60 for photons alone [V].
- Its "~10³⁰ h per dimension" fits both the area, 8.9×10²⁹ h, and S^{1/3} = 1.0×10³⁰ [V].

**Which region, and since when [T][D].** The area is constant for a *fixed comoving region of a homogeneous radiation bath*: D_x ∝ a and D_p ∝ 1/a. It is not the bounding box of a fixed set of photons, which spreads as they stream, and it is not the area of a region that grows in comoving size, such as the particle horizon or the Hubble sphere (§6). For a fixed comoving region:

- the photon number is conserved once electron–positron annihilation is over (k_BT ≪ m_e c²); before it, the region held 4/11 of today's comoving photon number [T][V];
- throughout, from reheating on, the conserved quantity is the comoving entropy, S ∝ g_s(T)(aT)³, so the area, which scales as aT, changes as g_s^{−1/3}: by (11/4)^{1/3} = 1.40 for the photons across annihilation, and by (106.75/3.909)^{1/3} = 3.01 across all the Standard Model's thresholds [V];
- before reheating at the end of inflation the region held no radiation. The area counts occupied cells; it was created at reheating and is not a constant of nature.

**What N counts [T].** The relation's N is the radiation's photon count, or its entropy. It is not "the universe's entropy". Egan and Lineweaver's budget for the observable universe puts the photons at 5.40×10⁸⁹ k and the supermassive black holes at about 3×10¹⁰⁴ k [S: Egan–Lineweaver 2010, Table 1], and the cosmic event horizon at 2.6×10¹²² k [ibid., Table 2]. Black-hole and horizon entropies are not counts of phase-space cells occupied by free quanta, and they do not enter the relation.

**The program's reading [D].** The program's cosmological constraint a·ã = 1 [P1, §10] states that rigidity of the symplectic form ω (Planck's constant does not run) keeps the volume of every comoving phase-space cell fixed, so the scale factor ã of the momentum description is the reciprocal of a. That is the area statement for one cell. The rectangle's area is the number of occupied cells times the area of one; a·ã = 1 fixes only the second factor, and the first is the radiation's entropy, set at reheating. In general relativity the one-cell statement already holds, because a free particle's comoving momentum is conserved [T]. The diameter relation therefore holds in standard ΛCDM cosmology, with or without reciprocity, and cannot test the program.

---

## 4. Extent and resolution, and the published answers

*In plain terms: A waveform of duration T can be resolved in frequency only to about 1/T, and a waveform sampled at intervals τ has a spectrum that reaches only to about 1/τ; the number of independent samples is the same in both descriptions. Applied to the universe, its size sets the finest momentum it can resolve, and the smallest meaningful length sets the largest momentum. Counted this way, the visible universe has about 10⁶¹ cells along each axis. Gravity cuts the number of independent states far below the cube of that number, and it ties the largest usable momentum to the size of the universe. That tie has been written down several times, beginning with Born in 1938, and most recently by the authors whose geometry of position and momentum this program uses.*

**The sampling count [T][V].** A region of position extent L resolved to a length ℓ has momentum extent ħ/ℓ resolved to ħ/L: L/ℓ cells of area ħ per axis in either description (L/2πℓ cells of area h). With L = c/H₀ = 1.37×10²⁶ m and ℓ = l_P = 1.616×10⁻³⁵ m there are L/l_P = 8.49×10⁶⁰ cells per axis.

**Holography [T][V].** The cube, 6.12×10¹⁸², is not the number of independent states. A horizon of radius L carries the Gibbons–Hawking entropy π L²/l_P² [S: Gibbons–Hawking 1977, abstract; Bousso 2000]: 3.31×10¹²² for the de Sitter radius L_Λ = c/(H₀√Ω_Λ) = 1.66×10²⁶ m, and 3.0×10¹²² for today's cosmic event horizon, 16.7 Gly [V]. Bousso's N-bound states that "a universe with Λ > 0 cannot have entropy greater than N = 3π/Λ" in Planck units, which is the same horizon entropy [S: Bousso 2000].

**Ultraviolet and infrared are tied [T][S].** Cohen, Kaplan and Nelson require that an effective field theory in a box of size L, cut off at energy Λ_UV, hold no more energy than a black hole of the same size: "L³Λ⁴ ≲ L M_P²", so Λ_UV ≲ (M_P/L)^{1/2} in natural units, with M_P the unreduced Planck mass. For an infrared cutoff at the present horizon they find "Λ ∼ 10^{−2.5} eV"; with L = c/H₀ the bound is 4.19 meV [V]. They add: "This observation does not predict the cosmological constant's value" [S: CKN 1999].

**Born, 1938 [T][S].** Born set up this question. In "A suggestion for unifying quantum theory and relativity" he notes that Einstein's static closed universe has "an upper limit for the distance between two points, given by the radius a of the universe", and writes: "Let us transfer this consideration to the p-space." Momentum space gets its own Einstein-type equations, with their own constants, and "for systems of some kind there is an upper limit for momenta, determined by the radius b of the hypersphere"; the number of states in a volume V is then finite. He declines to connect the two radii: "Whether these nuclear constants are connected with the corresponding molar constants λ, κ cannot be decided yet." He fixes b from the classical electron radius r₀ by r₀ = h/(πb), so b c = 2ħc/r₀ ≈ 1.4×10⁸ eV [V], a particle scale, and leaves open "whether the constant b is universal, or characteristic for each energetically closed system", the contextual choice that FKGLM make below. He opens by rejecting Eddington's attempt "to link the properties of the smallest particles to those of the whole universe" [S: Born 1938]. In 1949 he splits ħ = ab into a length and a momentum and fixes the length from particle masses [S: Born 1949]. Neither paper uses the Planck length.

**The program's own toy model [T][S].** In the Grosse–Wulkenhaar model, the program's toy model II [P4], the harmonic term's strength Ω sets the minimal momentum, and Grosse and Wulkenhaar "identify the parameter √Ω with the ratio of the Planck length to the size of the (finite!) universe" [S: Grosse–Wulkenhaar 2005]. The model is self-dual under the exchange of position and momentum at Ω = 1, a universe of Planck size; for L = c/H₀, Ω = (l_P/L)² = 1.4×10⁻¹²² [V].

**Born geometry [T][S].** Freidel, Kowalski-Glikman, Leigh and Minic (FKGLM) work in the modular, or Born, geometry this program builds on [P1, §3]. They fix only the area of a phase-space cell, "λε = 2πℏ … the quantum area constraint. Whereas the area of the modular cell is fixed by this quantum constraint, its shape is not"; write the position and momentum cutoffs as L = N_q λ and M = N_p ε; and find "LM/2πℏ = N^{1/4}", which they read as "the cutoffs on space and momentum are not separately arbitrary but are inversely related". Setting N equal to the horizon's gravitational entropy, they obtain ρ ≲ ħ/(ℓ²ℓ_P²), a momentum cutoff "M ∼ ℏ/√(ℓℓ_P)", and "the above geometric mean of the Hubble scale and the Planck length is λ ∼ (ℓℓ_P)^{1/2} ∼ 10^{−4} m, which corresponds to the observed vacuum energy scale of M ∼ 10^{−3} eV" [S: FKGLM 2023; also their essay "On the inevitable lightness of vacuum"]. They take λ to be "not universal but instead … chosen in the context of the system in question". Berglund, Hübsch and Minic write the same scale as l_Λ = √(l l_P) with λ_cc = l_P²/l_Λ⁴, and say that "the curvature of the dual spacetime is the cosmological constant of the observed spacetime, while the size of the dual spacetime is the gravitational constant" [S: BHM 2023]. Earlier versions of the geometric-mean length are Padmanabhan's L_DE = √(L_P L_Λ), under the heading "Geometrical Duality in our Universe" [S: Padmanabhan 2006], and the extended uncertainty relations with both a minimal length and a de Sitter scale. Bambi and Urban's is invariant under Δx → (α/β)^{1/2}(L_X L_Pl)Δp, Δp → (β/α)^{1/2}(L_X L_Pl)⁻¹Δx with L_X = L_Λ (ħ = 1), which is ρ_λ with λ² ∝ l_P L_Λ [S: Bambi–Urban 2008]; Bolen and Cavaglià motivate the same form by "the symmetry of the symplectic space" [S: Bolen–Cavaglià 2005]. In the Snyder–de Sitter algebra a duality exchanges position with momentum and Λ with the Planck area, and "connects the high-energy/short-distance regime, governed by the Planck area Ω, with the low-energy/long-distance regime, governed by the cosmological constant Λ" [S: Mignemi 2010]; its self-dual length, λ⁴ ∝ Ω/Λ, is implicit there. A count of modes crossing the Hubble radius has also been used to fix Λ [S: Padmanabhan and Padmanabhan, "CosMIn"].

**The chat relation beside FKGLM's [D][V].** Both relations multiply a position extent by a momentum extent and equal a power of a count N. They count different things: the chat's N is the radiation entropy, 10⁹⁰, taken per spatial axis (N^{1/3}); FKGLM's is the horizon entropy, 10¹²², taken per spacetime dimension (N^{1/4}). Their per-axis counts are 1.0×10³⁰ and S_dS^{1/4} = 4.3×10³⁰; both are conserved for a fixed comoving region, so their ratio, 0.235, does not change [V]. The two kinds of count are linked by Cohen, Kaplan and Nelson's maximal entropy: when their bound is near saturation, "the entropy is S_max ≃ S_BH^{3/4}" [S: CKN 1999, eq. 3]. Radiation filling a Hubble sphere in the radiation era nearly saturates it, so its per-axis count S^{1/3} equals the horizon's per-dimension count S_BH^{1/4} within a factor of 0.79–1.05, at every temperature [V].

So the question in this note's title has a published answer: in Born geometry, at a fixed count of cells, the momentum cutoff and the position cutoff are inversely related, and for a phase space the size of the horizon the cell length is the geometric mean of the Planck and horizon lengths. (FKGLM's momentum cutoff is itself ħ/√(ℓℓ_P), so their regulated phase space is not the Fourier box of §7, though both carry the same length.) What follows asks what the program's version of reciprocity adds, and whether it can use that length.

---

## 5. What reciprocity adds: invariant area, inverted shape

*In plain terms: Born reciprocity exchanges position and momentum. To exchange a length with a momentum it needs a reference length, the Born length λ, with ħ/λ as the matching momentum. Applied to a rectangle of phase space, the exchange keeps the area and turns the shape around: a rectangle long in position becomes one long in momentum by the same factor. So the area is what reciprocity cannot change, and the aspect ratio is what it reverses. Every rectangle is unchanged by the exchange for exactly one choice of λ, so "square" means something only once λ is fixed by physics. For quantum wave packets the statement is exact and familiar: the Fourier transform turns a Gaussian packet with shape parameter Z into one with −1/Z, which is the form the program's reciprocity takes on its modular field, and the logarithm of a packet's aspect ratio is its distance from the one shape the transform leaves unchanged. The universe's radiation sits about 213 units of that distance from the self-dual shape, and moves two units further with each e-fold of expansion.*

**Reciprocity on a rectangle [T][V].** With Born length λ, reciprocity in ordinary units is

```text
ρ_λ:   x′ = (λ²/ħ) p,     p′ = −(ħ/λ²) x
```

which is symplectic for every λ. It maps a rectangle of extents (L, P) to one of extents (λ²P/ħ, ħL/λ²). Hence the area LP is invariant for every λ; the aspect ratio in units of λ, A = (L/λ)/(P/(ħ/λ)) = ħL/(λ²P), goes to 1/A; and the rectangle is self-dual, A = 1, exactly when λ² = ħL/P. These are elementary and published: Born's own split ħ = ab is this choice of units [S: Born 1949], and the same map acts on uncertainty extents in Bambi and Urban's generalized uncertainty relation [S]. Two consequences matter here [D][V]:

- every rectangle is self-dual for exactly one λ, the geometric mean of L and ħ/P;
- reciprocity maps with two Born lengths differ by a squeeze: ρ_{λ₁}ρ_{λ₂}⁻¹ = diag((λ₁/λ₂)², (λ₂/λ₁)²).

**The program fixes no λ [D].** The program's geometric action, built from ω and H, is invariant under the rigid Sp(2d, ℝ) [P1, §7.1; P6, §1], which acts transitively on the Siegel domain and so moves the self-dual point Z = i anywhere; the action therefore singles out no Born length. A length enters only through reference structures: the reference axes of the ρ-preserving potential, matter's coupling to the polarization [P4], and the program's dual special relativity, which sets λ = l_P in one untagged sentence [P2, §1]. Born's own reciprocity length was a particle scale (§4).

**Wave packets and the Siegel half-plane [T][V].** In units ħ = λ = 1, a Gaussian pure state ψ_Z(x) ∝ exp(iZx²/2) is labelled by a point Z = X + iY of the upper half-plane; in d dimensions Z lies in the Siegel upper half-space, on which Sp(2d, ℝ) acts on such states by Möbius maps [S: Ohsawa 2015; de Gosson 2013]. The Fourier transform sends ψ_Z to ψ_{−1/Z} [V: for Z = 0.3 + 0.7i a numerical transform returns −0.5172 + 1.2069i = −1/Z]. This is the program's reciprocity Z → −Z⁻¹ on its modular field [P1, §6], realized on wave packets. Its fixed point Z = i is the one Gaussian the transform leaves unchanged, the ground state of an oscillator of length λ. Gabor called Gaussian pulses "self-reciprocal" because the transform of one is a Gaussian of reciprocal sharpness [S: Gabor 1946]; Z = i is the one whose sharpness is its own reciprocal.

**Three loci [D][V].** For ψ_Z the position and momentum widths are Δx² = 1/(2Y) and Δp² = |Z|²/(2Y), so Δx/Δp = 1/|Z|. Three sets that appear in the record's statements about self-duality are therefore distinct:

- **|Z| = 1** is the set of states whose rectangle is square, Δx = Δp, including tilted ellipses with X ≠ 0;
- **Z = i** is the one round state, unchanged by reciprocity;
- **det H_Z = 1** holds at every Z, so the constraint a·ã = 1 holds everywhere on the slice X = 0, where H = diag(Y, Y⁻¹).

The program's checkpoint identifies a·ã = 1 with the circle |Z| = 1 [P1, §6, §10]. But a·ã = 1 holds along the whole slice, and the circle meets the slice only at Z = i; an internal audit of the record queries the identification on this ground [H2]. This note uses the slice: cosmic expansion moves along X = 0, and "self-duality" means Z = i.

**The distance [T][D][V].** With the half-plane metric ds² = (dX² + dY²)/Y² (the degree-1 Siegel metric), the distance from i to iY is |ln Y| = |ln(Δx/Δp)|. Off the slice |ln(Δx/Δp)| is smaller than the distance d(i, Z), with equality only on the slice. In the convention σ_x = e^r/√2 for a squeezed vacuum, d = 2r. The number depends on the metric: the Fubini–Study metric that Hilbert space induces is 1/8 of the Siegel metric, so a path of Siegel length 2r has Fubini–Study length r/√2 [V]. A "distance from self-duality" is defined only once its metric and its λ are named. In degree d the Siegel distance from i·1 to iy·1 is √d |ln y| [V].

**The clock [D][V].** A comoving cell's extents scale as a and 1/a (§3), so its aspect ratio in units of λ grows as a², and its point moves along the imaginary axis away from Z = i: distance 2 ln(a/a_sd) per axis, where a_sd is the scale factor at which the cell was square, advancing at the rate 2H. For the radiation of today's observable universe in Planck units the distance is ln A₀ = 213.5 per axis (369.8 for the isotropic point in degree 3), which is 106.7 e-folds since the square (§6). This is the content of the chat's "aspect ratio … = a clock measuring distance from self-duality". It reparametrizes ln a and adds no dynamics.

**A physical version: squeezed perturbations [T][S].** The aspect ratio in units of λ depends on λ. A version that does not exists and is observed. After a quantum fluctuation's wavelength leaves the Hubble radius during inflation, its state is squeezed relative to its own vacuum, with the squeezing parameter growing as r_k ≃ ln(a/a_k) (R_k in Albrecht et al.), the number of e-folds since the mode left the Hubble radius [S: Albrecht, Ferreira, Joyce and Prokopec 1994]: about 50 at the end of inflation [S: Martin–Vennin 2016], and about 100–120 today on the largest observed scales [S: Kiefer–Polarski 2009; Kiefer, Polarski and Starobinsky 1998; Grishchuk 1993]. A circuit complexity built from the squeezing grows linearly with the number of e-folds during inflation and falls in the radiation era [S: Bhattacharyya, Das, Haque and Underwood 2020]. Squeezing values depend on the choice of canonical variables [S: Grain–Vennin 2020], and modes stop squeezing once they re-enter the Hubble radius.

---

## 6. Where the rectangle is square

*In plain terms: In Planck units the radiation's rectangle is long in position by a factor of about 10⁹³ today, and going back in time the factor shrinks as the square of the scale factor. Run back far enough, it would reach one. That would happen at about 10¹⁴ times the Planck temperature, in a state no known physics describes, and long before the radiation existed: it was made when inflation ended, and the rectangle was then already long by a factor of 10³⁵. At the program's far-future turnaround of the expansion, which its conjugate description reads as a bounce, the rectangle would be at its most elongated. Drawn around the Hubble sphere instead, the rectangle is square at the Planck time, when the sphere holds less than one quantum; that says only that everything is Planckian at the Planck time. No reading puts a square rectangle of 10⁹⁰ cells at any bounce, so the early-chat claim is withdrawn.*

**The radiation rectangle in Planck units [V].** "Planck units" means λ = l_P, the Born length of the program's dual special relativity [P2, §1]; then A = (D_x/l_P)/(D_p/m_Pc).

- Today A₀ = 5.2×10⁹² (log₁₀ A₀ = 92.72), matching the chat's "~10⁹²"; ln A₀ = 213.5, so the radiation is 106.7 e-folds of expansion past the moment it would have been square.
- Run back with D_x ∝ a and D_p ∝ 1/a, the rectangle is square at a/a₀ = 4.4×10⁻⁴⁷, where T = 4.4×10¹⁴ T_P. Counting the Standard Model's g_s = 106.75 moves this to a/a₀ = 2.5×10⁻⁴⁷ and T = 2.5×10¹⁴ T_P.
- In closed form [D][V]: at the square both sides equal √(2πκ) N_γ^{1/6} = 3.28 N_γ^{1/6} in Planck units, and T_sq = 0.61 N_γ^{1/6} T_P. A region of N cells can be square only when its quanta carry about N^{1/6} ≈ 10¹⁵ Planck momenta.
- At T = T_P the rectangle is still long by A = 6.4×10²⁸ (Standard Model counting).

**That epoch is not a physical one [T][V].** Above the Planck temperature there is no tested physics. And in inflationary cosmology the radiation did not exist then: it was created at reheating, at a temperature no higher than about 5.7×10¹⁵ GeV (instantaneous reheating at the energy scale of inflation allowed by a tensor-to-scalar ratio below 0.036 [S: BICEP/Keck 2021], E_inf < 1.39×10¹⁶ GeV [S: Soman et al. 2025]), when A = 2.9×10³⁵. Since its creation the radiation rectangle has never been within 35 orders of magnitude of square. The trans-Planckian censorship conjecture, which forbids modes from being stretched from below the Planck length to beyond the Hubble radius [S: Bedroya–Vafa 2020], is a separate constraint of the same kind on how far a mode's cell can move from the self-dual point during accelerated expansion.

**The Hubble rectangle [D][V].** Drawn around the Hubble sphere instead (D_x = 2c/H), the rectangle is square in the radiation era at T = 0.28 T_P, when the Hubble radius is 0.75 l_P and the sphere holds about 0.45 quanta of all Standard Model species. At the Planck time every scale is Planckian, so this is dimensional analysis rather than a result. In this reading the area is not conserved: it grows as N_H^{1/3}, from below one to N_H = 4.4×10⁸⁷ photons today, when the aspect ratio is 1.6×10⁹². At a true bounce, where H = 0, the Hubble rectangle is infinitely elongated.

**Two regions [D][V].** The chat's four statements can each be made true by reading the first two (the area, N ~ 10⁹⁰) as statements about today's observable universe and the last two (the square, the clock) as statements about one Hubble patch. They then describe different objects: when a Hubble patch was square, at T = 0.28 T_P, today's observable universe was a region about 10³⁰ l_P across made of about 6×10⁸⁹ such patches, and its own rectangle was long by about 8×10²⁹.

**A squeezed mode [D][V].** Read as one perturbation mode's Wigner ellipse (§5), an aspect ratio of 10⁹² is a squeezing of r = 105.9, inside the literature's 100–120 for today's largest scales, and the chat's clock is then the mode's squeezing. That reading fits the fourth part of the claim and not the third: the mode was round before it left the Hubble radius during inflation, which is not a bounce.

**Self-dual bounces in string cosmology [T][V].** String cosmology has bounces at self-dual points, the most natural source of the phrase. Scale-factor duality maps a(t) to a⁻¹(−t), and the big bang becomes "an instant of maximal curvature" between the two branches [S: Veneziano 1991; Gasperini–Veneziano 1993]; in string-gas cosmology the temperature is symmetric under R → 1/R about the self-dual radius [S: Brandenberger–Vafa 1989; Brandenberger 2008]. There the self-dual point is in string units, for a compact radius or for the scale factor itself, not for the radiation rectangle in Planck units: at a string-scale bounce, k_BT = 10¹⁷ GeV, the observable universe's radiation rectangle would still be long by A = 9.5×10³² [V].

**At the turnaround [D].** A ∝ a² is largest where a is. If the expansion turns around, the turnaround is the moment of greatest elongation, not a square; for the Hubble box H → 0 there, and A → ∞. The program reads that turnaround, through ã = 1/a, as the conjugate description's bounce [P1, §10]. The potential the program writes for its dark-energy field, V₀[1 + cos(τ/f)], is never negative for V₀ > 0, and so, in the spatially flat universe the program's cosmology assumes, produces no turnaround as written (a closed universe can turn around without negative energy); the record leaves this unresolved [H2].

**Where the claim probably came from [D, inference].** The record holds no transcript of the chat. One reading reproduces the claim exactly: the record's own identification of a·ã = 1 with the circle |Z| = 1 [P1, §6, §10]. Along that circle, written Z = tanh s + i sech s, Im Z peaks at Z = i; with the record's a² = Im Z, the peak is the maximum of a, the turnaround, and H is round there. (With §5's wave-packet convention, in which Im Z falls as a⁻², the same point is a minimum of a, a literal bounce.) Under that identification "square exactly at the bounce" and "a clock measuring distance from self-duality" both follow, with the bounce at the turnaround. The identification fails in two ways [V]. On |Z| = 1 the position and momentum extents are equal at all times (H_xx = H_pp = 1/Y), which contradicts the measured aspect ratio of 10⁹². And if the 10⁹² is read instead as the squeeze of H along the circle, it requires X ≈ 1 today, a homogeneous momentum graviton whose energy density, of order M̄_P² M_X² X², exceeds the critical density by a factor of order (M_X/H₀)² ≈ 10⁶¹ for the smallest M_X allowed by §8.2.

### Obituary: the square rectangle at the bounce

- **What was claimed.** That the universe's position–momentum rectangle is "square (D_x = D_p in Planck units) exactly at the bounce" [H1].
- **How it was tested.** By computing the aspect ratio's history for the reading the chat's own numbers fit (the radiation of today's observable universe), for the Hubble-sphere reading, for a two-region reading, for a squeezed mode, and for the record's |Z| = 1 geometry, at every event the record or the literature could mean by "the bounce", including the self-dual bounces of string cosmology (this section; `verify/phase_space_diameter.py`; round-5 review).
- **Why it failed.** In the reading the numbers fit, the rectangle is square only at about 10¹⁴ T_P, before the radiation existed; since reheating it has been elongated by at least 10³⁵. At the program's turnaround it is at its most elongated. In the Hubble reading it is square at the Planck time, a statement about the Planck time, not about any bounce. A squeezed mode matches the number 10⁹² but was round before it left the Hubble radius, not at a bounce. At a string-scale bounce the rectangle is still long by 10³³. The record's |Z| = 1 geometry, which would make the claim exact, contradicts the measured aspect ratio.
- **What survives.** The area relation, as standard physics (§3); the aspect ratio as a clock of e-folds and as a distance on the Siegel half-plane (§5).

---

## 7. A self-dual cosmic box

*In plain terms: One pair of sizes can be exactly symmetric under reciprocity. Take the universe's horizon as its largest length and the Planck length as its smallest; in momentum the matching range runs from the horizon's resolution to the Planck momentum. This box maps onto itself under the exchange for exactly one Born length, the geometric mean of the Planck length and the horizon radius, about 50 micrometres. It is the same length at which field theory in a box the size of the universe stops being trustworthy, and it is the cell length of the Born-geometry argument in §4. Within a factor of two it is the length scale of dark energy, an agreement that is the Friedmann equation restated. With that length held fixed, the box approaches exact symmetry as the universe approaches the pure dark-energy state of its far future. None of this is new except the phrasing, and none of it predicts anything unless the reference length is fixed by something other than the cosmological constant itself.*

**The self-dual length [T][V].** By §5 the Fourier box [l_P, L] × [ħ/L, ħ/l_P] maps onto itself under ρ_λ exactly when λ² = l_P L. This is the scale of §4's literature [S: CKN 1999; Bambi–Urban 2008; Padmanabhan 2006; FKGLM 2023; BHM 2023; implicitly Mignemi 2010]. Its value:

| L | λ = √(l_P L) | ħc/λ |
|---|---|---|
| Hubble radius c/H₀ = 1.37×10²⁶ m | 47.1 μm | 4.19 meV |
| de Sitter radius L_Λ = 1.66×10²⁶ m | 51.8 μm | 3.81 meV |
| particle horizon, 4.36×10²⁶ m | 84.0 μm | 2.35 meV |

**It is the CKN cutoff [T][V].** ħc/√(l_P L) = √(E_P ħc/L), which is the Cohen–Kaplan–Nelson cutoff (M_P/L)^{1/2} of §4 with the unreduced Planck energy E_P. Other conventions change it by a factor of order one: 0.45 with the reduced Planck mass, 0.59 or 0.84 with an explicit black-hole mass for a sphere or a cube of size L, and 2.08 if the vacuum energy is taken as one scalar field's zero-point energy Λ⁴/16π² [V].

**It is the dark-energy scale, by the Friedmann equation [D][V].** The dark-energy density is ρ_Λ = 3Ω_Λ M̄_P² H₀² (natural units, M̄_P the reduced Planck mass), so

```text
ρ_Λ^(1/4) / (ħc/√(l_P c/H₀)) = (3Ω_Λ/8π)^(1/4) = 0.535
```

independently of H₀: ρ_Λ^{1/4} = 2.24 meV, or 88.1 μm as a length [V; S: PDG], against 4.19 meV for the Hubble box. The agreement within a factor of two is the statement that Ω_Λ is of order one today, and carries no further information. The closer agreement for the particle horizon (2.35 meV against 2.24) comes from χH₀/c = 3.18, a property of ΛCDM's expansion history.

**De Sitter space as the self-dual state [D][V].** Fix λ² = l_P L_Λ and let the box follow the Hubble radius. Its aspect ratio in units of λ is

```text
A(t) = (c/H(t)) l_P / λ² = H_Λ/H(t) = √Ω_Λ(t)
```

exactly, in any FLRW universe (H_Λ = c/L_Λ, Ω_Λ(t) = Λc²/3H²). It is 0.83 today, was far below one in the radiation and matter eras, and tends to one as the universe approaches empty de Sitter space; at a turnaround it diverges. In this language de Sitter space is the box's self-dual fixed point, and the coincidence that Ω_Λ ~ 1 today becomes the observation that the box is near self-duality now. The statement holds by construction, because λ was built from L_Λ. A box that instead follows c/H(t) with λ² = l_P c/H(t) gives a vacuum energy that tracks the matter density, which is excluded [S: Hsu 2004]; holographic dark energy with the event horizon as its infrared length is the variant that survives [S: Li 2004]. A dual-spacetime model with ultraviolet–infrared mixing, in the Born-geometry lineage, gives a dark energy that varies in time with w > −1, which its authors find compatible with DESI [S: Hur, Jejjala, Kavic, Minic and Takeuchi 2025].

**The cosmological constant as a reciprocity image [T][D].** Equivalently, L_Λ = λ²/l_P: the de Sitter radius is where ρ_λ sends the Planck momentum ħ/l_P. Then Λ = 3l_P²/λ⁴ [D][V], which is Berglund, Hübsch and Minic's λ_cc = l_P²/l_Λ⁴ up to the factor 3 they drop [S]. The cosmological-constant problem, Λl_P² ~ 10⁻¹²², becomes the hierarchy λ/l_P = 3.2×10³⁰ = √(L_Λ/l_P). This takes the fourth root of the problem and explains nothing while λ is defined through Λ. It would predict Λ only if λ were fixed by other physics.

**Numerology lies close at hand [V].** In units of λ = √(l_P L_Λ), today's radiation rectangle would be square at k_BT ≈ 1.0 TeV, near the electroweak scale (1.7 TeV for the photons alone, without the Standard Model's g_s). The number is √(k_BT₀E_P) = 1.7 TeV up to that factor, a different geometric mean from the 5.2 TeV, √(ρ_Λ^{1/4}E_P), of Berglund, Hübsch and Minic's see-saw [S]. The Born length that makes today's radiation rectangle itself square is √(ħD_x/D_p) = 3.7×10¹¹ m, about 2.5 au. Nothing here gives such coincidences a mechanism, and this note claims none.

---

## 8. Consequences for the program

*In plain terms: FKGLM let their reference length depend on the system under study. This program cannot: its reciprocity is one exact symmetry with one Born length. That length could enter in two places. One is the program's dual special relativity, which sets a maximum force; the other is the range of the program's massive momentum graviton, whose force acts on ordinary matter at the strength of gravity. A 50-micrometre Born length would make the maximum force 10⁻¹⁷ newtons, below the force that holds a hydrogen atom together. A 50-micrometre range would put a gravitational-strength force where laboratory torsion balances have looked for one and found none. Both uses fail. The second failure leaves a number: if the program's vacuum is the one its own equations assume, the momentum graviton's range must be below about 38 micrometres, whatever sets its mass. Two smaller consequences follow, one about the conjugate description of today's universe and one about the early-universe term the program keeps as an option.*

**8.1 Not the Born length of the dual special relativity [D][V].** The program's dual special relativity bounds every rate of change of momentum by c̃ = ħc/λ² [P2, §1]. At λ = l_P this is c⁴/G = 1.21×10⁴⁴ N. At λ = √(l_P L) it is (c⁴/G)(l_P/L): 1.4×10⁻¹⁷ N for L = c/H₀, 1.2×10⁻¹⁷ N for L_Λ. The Coulomb force in the hydrogen ground state, 8.24×10⁻⁸ N, exceeds it by 5.8×10⁹, and the weight of a kilogram by 6.9×10¹⁷; the dual composition law F₁ ⊕ F₂ = (F₁ + F₂)/(1 + F₁F₂/c̃²) [P2, §2] would cap every force near 10⁻¹⁷ N. The self-dual length cannot be that Born length. In Freidel, Leigh and Minic's metastring, ħ = λε and Newton's constant is G_N = ρα′ = ρλ/ε, with ρ set by the dimension and the compactification, so λ² = ħG_N/ρ is the Planck length squared up to ρ [S: FLM 2015]. A maximal force from Born reciprocity is itself in the literature: Low's reciprocal relativity bounds forces by a constant b [S: Low 2006]; the program's own paper cites Gibbons's maximum-tension conjecture and Caianiello's maximal acceleration for the idea [P2, §1, †]. With the Born length at l_P, the cosmic Fourier box is far from self-dual, A = L/l_P = 8.5×10⁶⁰ for the Hubble radius, and the cosmological-constant problem is the size of that number squared.

**8.2 Not the range of the momentum graviton, and a bound on it [D][V][S].** The momentum graviton X is a massive spin-2 field whose mass M_X is the program's polarization-breaking scale, with no value in the record [P1, §7]. Reciprocity forces the two spin-2 frames to have equal Planck masses, so ordinary matter, coupled to the metric g, feels X at gravitational strength, and is safe only because X's force is cut off beyond ħ/(M_X c) [P1, §7.5; P3, §3].

*The coupling and its premise.* In Hassan–Rosen bimetric gravity with matter on g, the linearized potential between two masses is V(r) = −(Gm₁m₂/r)(1 + α e^{−r/λ_X}) with

```text
α = (4/3) (M_f u / M_g)²
```

where u is the ratio of the two frames' backgrounds, f̄ = u²ḡ (the cited papers write it c), and the 4/3 comes from the massive field's extra polarizations [S: Lüben, Mörtsell and Schmidt-May 2020, eq. 9; Enander–Mörtsell 2013, eq. 4.1; V]. Only the product M_f u is fixed by the theory, so equal Planck masses give α = 4/3 only if u = 1. The program's vacuum has u = 1: its second frame is the polarization frame f = E₀[J], and its vacuum is the aligned point 𝕏 = √(g⁻¹f) = 1, where its vacuum-energy identity holds [P3, §1–§2]. The program's couplings also say why that vacuum and no other [D][V]. With the palindromic couplings the proportional backgrounds solve u(u − 1)(u + 1)(β₁u² + (3β₂ − β₀)u + β₁) = 0. On the program's flat branch, β₀ = −4β₁ − 3β₂, the other solutions are a pair (u, 1/u) that breaks the frame exchange; they exist only for β₁ < 0 < |β₁| < β₂, and there the bimetric vacuum energy is of the order of the spin-2 mass squared, some 10⁶¹ times H₀² for M_X c² ≥ 5 meV. Only the aligned vacuum is compatible with the observed Λ. Two points stay open [O]. Whether the aligned point persists as the universe expands is not settled, since E₀[J] lies on a compact moduli space [P5, §4] and so, on this note's reading, carries no scale of its own. And how reciprocity's action as this frame exchange relates to its action Z → −Z⁻¹ on the modular field is open in the record [H2]. The second frame is not the slaved momentum block g̃ = g⁻¹ that carries ã (§5), so a·ã = 1 does not fix u. For a range of order 50 μm, laboratory test masses are far outside their Vainshtein radii (about 10⁻¹² m for a kilogram), so the force is unscreened [D][V].

*The bound.* Torsion-balance tests of the inverse-square law limit "any gravitational-strength Yukawa interactions to ranges <38.6 μm" at 95% confidence, and their authors draw the conclusion for a "heavy graviton", citing bigravity [S: Aoki–Mukohyama 2016]: its mass "must be greater than 5.1 meV" [S: Lee et al. 2020]. X's Yukawa force is attractive, so the relevant limit is the one-sided +α₉₅ column of the experiment's exclusion table, which at α = 4/3 gives λ_X < 37.7 μm. The two-sided |α₉₅| column, which reproduces the published 38.6 μm and 30 μm limits and so checks the transcription and the interpolation, gives the stronger 35.8 μm [S: Lee 2020 thesis, Table 11.4; V]. Hence, in the aligned vacuum,

```text
λ_X < 37.7 μm,     M_X c² > ħc/(37.7 μm) = 5.2 meV
```

[V]. For another background ratio the limit is the table's value at α = (4/3)u²: 57.0 μm at u = 0.5, 42.5 μm at u = 0.8, 30.8 μm at u = 1.5 [V].

*What follows.* In the aligned vacuum an X set by the self-dual length, at 47–84 μm, is excluded; it would survive only for u < 0.67 (47.1 μm) or u < 0.30 (84.0 μm) [V]. The polarization-breaking scale lies at least 2.3 times above the dark-energy scale of 2.24 meV. The test is an old one: a gravitational-strength modification of gravity at the dark-energy length was proposed to address the cosmological-constant problem [S: Sundrum 2004], and torsion balances were aimed "below the dark-energy length scale" to look for it [S: Kapner et al. 2007]. The record's statement that gravitational-strength short-range forces are "experimentally unconstrained down to far below any plausible M_X" [P3, §3] is consistent with the bound but gave no number.

*Caveats [T][O].* In bigravity a spin-2 field far heavier than H₀ at equal Planck masses needs the potential's vacuum energy, of order M_X²M_P², cancelled; in the program the cancellation is the palindrome identity at the aligned point [P3, §2]. Bimetric cosmologies are unstable while H exceeds the spin-2 mass [S: Lüben et al. 2020], so the early universe is a separate question, open in the record. And the bound assumes that X adds the only Yukawa term; other light fields of the program could add attractive or repulsive ones.

**8.3 The conjugate description of today's universe [D][V].** Under ρ_{l_P}, today's radiation rectangle maps to a region 1.0×10⁻³¹ l_P across whose momenta spread over 5.4×10⁶¹ m_P c. The program's "conjugate universe", read as the same state in exchanged variables [P1, App. A, item 2], is therefore not a place with ordinary physics: its extents lie beyond the Planck scale in both variables. The program does not require otherwise, since it treats the two as one state with two descriptions.

**8.4 The early-universe term sits at the self-dual point [D][V].** The program keeps an optional a⁻⁶ correction to the Friedmann equation, from a dual Einstein term with its own Planck mass M̃: 3H²(M_P² + M̃² a⁻⁶) = ρ, written with a·ã = C and C = 1 [P1, §10, §13 row 10]. With general C the minisuperspace kinetic terms M_P² aȧ² and M̃² C³ ȧ²/a⁵ are exchanged by a → C/a exactly when M̃ = M_P, and the two are then equal at the fixed point a = √C, where a = ã [V: sympy]. If reciprocity fixes M̃ = M_P, as it fixes the two bimetric Planck masses [P3, §3], the step therefore sits at the self-dual epoch. That epoch depends on λ and on the comoving scale reciprocity treats as unit, which is a choice: for λ = l_P and the radiation of today's observable universe it is the 10¹⁴ T_P of §6, the square, which is not a bounce (H² > 0 throughout). Whatever the unit, the dual term must be negligible by nucleosynthesis, so the self-dual epoch must lie before it. The normalization C here belongs to the slaved block that carries ã; it is not the bimetric background ratio of §8.2. The step's free parameter becomes the question of the Born length.

**8.5 A lever arm (open) [O].** The program identifies its dark-energy field τ with the angle of the vacuum's polarization [P1, §6, §10], and in its coset toy model the polarization angle and the squeeze along the slice are separate flat directions [P4]. Whether matter's polarization follows the vacuum's as τ drifts is not settled. If it does, a rotation of the polarization by θ displaces a particle of momentum p by θλ²p/ħ: 4.9×10⁻⁶⁰ m per radian for an electron with the Bohr momentum at λ = l_P, and 42 m per radian at the self-dual length [V]. A cosmological drift of τ would then be harmless only for a Born length near the Planck length.

**8.6 What would test this.** Nothing in §3–§6 goes beyond ΛCDM, so none of it can confirm or refute the program. The bound of §8.2 tightens with every improvement in short-range gravity tests. §7's reformulation of Λ would become a prediction only if the program derived λ, or M_X, from its own dynamics.

---

## 9. Summary

| Claim | Status | Tag |
|---|---|---|
| D_x D_p = κ h N_γ^{1/3}, κ = 1.708 (sphere, twice the mean momentum) | identity of blackbody statistics | [D][V] |
| The area is conserved | for a fixed comoving region: photon number since annihilation; entropy since reheating, up to g_s^{−1/3} | [T] |
| N ~ 10⁹⁰ | the radiation entropy, 1.01×10⁹⁰ k_B; photon count 1.43×10⁸⁹ | [V] |
| N is "the universe's entropy" | corrected: black holes and the horizon dominate the universe's entropy | [T][S] |
| a·ã = 1 underlies the relation | it fixes one cell's area, not the number of cells | [D] |
| Reciprocity keeps areas and inverts aspect ratios | elementary; every rectangle is self-dual for one λ | [T][V] |
| The program fixes a Born length | no: its action singles out none; #13's λ = l_P is an untagged choice | [D] |
| \|Z\| = 1, Z = i and det H = 1 | three different loci: square rectangles, the round state, everywhere | [D][V] |
| Radiation per-axis count ≈ horizon per-dimension count | the Cohen–Kaplan–Nelson saturation S ≃ S_BH^{3/4}, at every radiation-era temperature | [T][V] |
| Aspect ratio = distance from self-duality | the Siegel distance from Z = i on the slice; 2r in a stated convention | [T][D][V] |
| Aspect ratio today ~10⁹² | 5.2×10⁹² (observable universe), 1.6×10⁹² (Hubble sphere) | [V] |
| Square "exactly at the bounce" | **withdrawn**: square only at ~10¹⁴ T_P; greatest elongation at a turnaround | [D][V] |
| Size in position and in momentum inversely related, cell length √(l_P L) | published (FKGLM 2023; BHM 2023; Padmanabhan; Snyder–de Sitter; CKN) | [T][S] |
| Its match to dark energy | the Friedmann equation with Ω_Λ ~ 1 | [D][V] |
| De Sitter space as the box's self-dual state, A = √Ω_Λ(t) | identity, by construction | [D][V] |
| λ = √(l_P L) as the dual-relativity Born length | **excluded**: c̃ = 10⁻¹⁷ N | [D][V] |
| λ = √(l_P L) as X's range | **excluded** by torsion balances in the aligned vacuum; allowed only for background ratio u < 0.67 | [D][V][S] |
| X's range < 37.7 μm, M_X c² > 5.2 meV | bound in the aligned vacuum (u = 1, α = 4/3); 57.0 μm at u = 0.5 | [V][S] |
| The program's vacuum has u = 1 | the only proportional vacuum with zero wedge vacuum energy; persistence under expansion open | [D][V][O] |
| The a⁻⁶ step at the self-dual point if M̃ = M_P | conditional | [D][V] |
| Polarization drift as a lever arm | open | [O] |

The answer to the title's question is yes, in two senses. For the universe's radiation the two sizes are reciprocal, with a fixed product set by the number of photons, and their ratio is a clock; that is standard cosmology. For the universe's range of scales, the size of position space and the extent of momentum space are inversely tied through the black-hole bound, with the geometric mean of the Planck and horizon lengths, about 50 micrometres, as the cell length; that is published, in the Born-geometry literature among others. Born reciprocity adds a way to measure the ratio, as a distance from a self-dual point. The program cannot use the self-dual length, and the attempt yields one number it did not have: in the vacuum its own equations assume, the momentum graviton's range is below 37.7 micrometres.

---

## References

*[S] = retrieved by live search for this note; † = cited from memory, verify before external use.*

**Program documents.**
- [H1] Comatter program, handoff document (2026-10-19), §4 (`HANDOFF.md`).
- [H2] Comatter program, internal audit of the record, items 23, 24, 27 and 39 (`review/wiki-build-flags.md`).
- [P1] Comatter program, working checkpoint v2.2 (`papers/broken-born-checkpoint-v2.md`).
- [P2] Comatter program, special relativity of the momentum polarization (`papers/conjugate-special-relativity.md`).
- [P3] Comatter program, calc note on the β coefficients (`notes/debt1a-iv-beta-coefficients.md`).
- [P4] Comatter program, two toy models of spontaneously broken reciprocity (`papers/reciprocity-toy-models.md`).
- [P5] Comatter program, calc note on the tuning test (`notes/debt1a-iii-tuning-test.md`).
- [P6] Comatter program, calc note on the classification of X (`notes/debt1a-ii-X-classification.md`).

**Literature.**
- [S] A. Albrecht, P. Ferreira, M. Joyce, T. Prokopec, "Inflation and squeezed quantum states," Phys. Rev. D 50, 4807 (1994), arXiv:astro-ph/9303001.
- [S] K. Aoki, S. Mukohyama, "Massive gravitons as dark matter and gravitational waves," Phys. Rev. D 94, 024001 (2016), arXiv:1604.06704.
- [S] C. Bambi, F. R. Urban, "Natural extension of the generalised uncertainty principle," Class. Quantum Grav. 25, 095006 (2008), arXiv:0709.1965.
- [S] A. Bedroya, C. Vafa, "Trans-Planckian censorship and the swampland," JHEP 09 (2020) 123, arXiv:1909.11063.
- [S] P. Berglund, T. Hübsch, D. Minic, "On de Sitter spacetime and string theory," Int. J. Mod. Phys. D 32, 2330002 (2023), arXiv:2212.06086.
- [S] A. Bhattacharyya, S. Das, S. S. Haque, B. Underwood, "Cosmological complexity," Phys. Rev. D 101, 106020 (2020), arXiv:2001.08664.
- [S] BICEP/Keck Collaboration, P. A. R. Ade et al., "Improved constraints on primordial gravitational waves using Planck, WMAP, and BICEP/Keck observations through the 2018 observing season," Phys. Rev. Lett. 127, 151301 (2021), arXiv:2110.00483.
- [S] B. Bolen, M. Cavaglià, "(Anti-)de Sitter black hole thermodynamics and the generalized uncertainty principle," Gen. Rel. Grav. 37, 1255 (2005), arXiv:gr-qc/0411086.
- [S] M. Born, "A suggestion for unifying quantum theory and relativity," Proc. R. Soc. Lond. A 165, 291 (1938).
- [S] M. Born, "Reciprocity theory of elementary particles," Rev. Mod. Phys. 21, 463 (1949).
- [S] R. Bousso, "Positive vacuum energy and the N-bound," JHEP 11 (2000) 038, arXiv:hep-th/0010252.
- [S] R. H. Brandenberger, C. Vafa, "Superstrings in the early universe," Nucl. Phys. B 316, 391 (1989); R. H. Brandenberger, "String gas cosmology," arXiv:0808.0746 (2008).
- [S] A. G. Cohen, D. B. Kaplan, A. E. Nelson, "Effective field theory, black holes, and the cosmological constant," Phys. Rev. Lett. 82, 4971 (1999), arXiv:hep-th/9803132.
- [S] C. A. Egan, C. H. Lineweaver, "A larger estimate of the entropy of the universe," Astrophys. J. 710, 1825 (2010), arXiv:0909.3983.
- [S] J. Enander, E. Mörtsell, "Strong lensing constraints on bimetric massive gravity," JHEP 10 (2013) 031, arXiv:1306.1086.
- [S] D. J. Fixsen, "The temperature of the cosmic microwave background," Astrophys. J. 707, 916 (2009), arXiv:0911.1955.
- [S] L. Freidel, J. Kowalski-Glikman, R. G. Leigh, D. Minic, "Vacuum energy density and gravitational entropy," Phys. Rev. D 107, 126016 (2023), arXiv:2212.00901; "On the inevitable lightness of vacuum," Int. J. Mod. Phys. D 32, 2342004 (2023), arXiv:2303.17495.
- [S] L. Freidel, R. G. Leigh, D. Minic, "Metastring theory and modular space-time," JHEP 06 (2015) 006, arXiv:1502.08005.
- [S] D. Gabor, "Theory of communication. Part 1: The analysis of information," J. IEE Part III 93, no. 26, 429–441 (1946).
- [S] M. Gasperini, G. Veneziano, "Pre-big-bang in string cosmology," Astropart. Phys. 1, 317 (1993), arXiv:hep-th/9211021.
- [S] G. W. Gibbons, S. W. Hawking, "Cosmological event horizons, thermodynamics, and particle creation," Phys. Rev. D 15, 2738 (1977).
- [S] M. A. de Gosson, "Symplectic and Hamiltonian deformations of Gabor frames" (2013), arXiv:1305.1025, Appendix A.
- [S] J. Grain, V. Vennin, "Canonical transformations and squeezing formalism in cosmology," JCAP 02 (2020) 022, arXiv:1910.01916.
- [S] L. P. Grishchuk, "Quantum effects in cosmology," Class. Quantum Grav. 10, 2449 (1993), arXiv:gr-qc/9302036.
- [S] H. Grosse, R. Wulkenhaar, "Renormalisation of φ⁴-theory on noncommutative ℝ⁴ in the matrix base," Commun. Math. Phys. 256, 305 (2005), arXiv:hep-th/0401128.
- [S] S. D. H. Hsu, "Entropy bounds and dark energy," Phys. Lett. B 594, 13 (2004), arXiv:hep-th/0403052.
- [S] S. Hur, V. Jejjala, M. J. Kavic, D. Minic, T. Takeuchi, "Dynamical dark energy, dual spacetime, and DESI," JCAP 11 (2025) 054, arXiv:2503.20854.
- [S] D. J. Kapner, T. S. Cook, E. G. Adelberger, J. H. Gundlach, B. R. Heckel, C. D. Hoyle, H. E. Swanson, "Tests of the gravitational inverse-square law below the dark-energy length scale," Phys. Rev. Lett. 98, 021101 (2007), arXiv:hep-ph/0611184.
- [S] C. Kiefer, D. Polarski, "Why do cosmological perturbations look classical to us?," Adv. Sci. Lett. 2, 164 (2009), arXiv:0810.0087; C. Kiefer, D. Polarski, A. A. Starobinsky, "Quantum-to-classical transition for fluctuations in the early universe," Int. J. Mod. Phys. D 7, 455 (1998), arXiv:gr-qc/9802003.
- [S] J. G. Lee, E. G. Adelberger, T. S. Cook, S. M. Fleischer, B. R. Heckel, "New test of the gravitational 1/r² law at separations down to 52 μm," Phys. Rev. Lett. 124, 101101 (2020), arXiv:2002.11761; J. G. Lee, "A Fourier–Bessel test of the gravitational inverse-square law," PhD thesis, University of Washington (2020), Table 11.4 (ResearchWorks handle 1773/45542).
- [S] M. Li, "A model of holographic dark energy," Phys. Lett. B 603, 1 (2004), arXiv:hep-th/0403127.
- [S] S. G. Low, "Reciprocal relativity of noninertial frames and the quaplectic group," Found. Phys. 36, 1036 (2006), arXiv:math-ph/0506031.
- [S] M. Lüben, E. Mörtsell, A. Schmidt-May, "Bimetric cosmology is compatible with local tests of gravity," Class. Quantum Grav. 37, 047001 (2020), arXiv:1812.08686.
- [S] C.-P. Ma, E. Bertschinger, "Cosmological perturbation theory in the synchronous and conformal Newtonian gauges," Astrophys. J. 455, 7 (1995), arXiv:astro-ph/9506072.
- [S] J. Martin, V. Vennin, "Quantum discord of cosmic inflation: can we show that CMB anisotropies are of quantum-mechanical origin?," Phys. Rev. D 93, 023505 (2016), arXiv:1510.04038.
- [S] S. Mignemi, "Doubly special relativity in de Sitter spacetime," Annalen Phys. 522, 924 (2010), arXiv:0802.1129.
- [S] T. Ohsawa, "The Siegel upper half space is a Marsden–Weinstein quotient: symplectic reduction and Gaussian wave packets," Lett. Math. Phys. (2015), doi:10.1007/s11005-015-0780-z, arXiv:1504.03963.
- [S] T. Padmanabhan, "Dark energy: mystery of the millennium," AIP Conf. Proc. 861, 179 (2006), arXiv:astro-ph/0603114; H. Padmanabhan, T. Padmanabhan, "CosMIn: the solution to the cosmological constant problem," Int. J. Mod. Phys. D 22, 1342001 (2013), arXiv:1302.3226.
- [S] Particle Data Group, S. Navas et al., Phys. Rev. D 110, 030001 (2024) and 2025 update: "Astrophysical constants and parameters"; "Big-Bang cosmology".
- [S] Planck Collaboration, N. Aghanim et al., "Planck 2018 results. VI. Cosmological parameters," Astron. Astrophys. 641, A6 (2020), arXiv:1807.06209.
- [S] C. E. Shannon, "Communication in the presence of noise," Proc. IRE 37, 10–21 (1949).
- [S] D. Slepian, "Some comments on Fourier analysis, uncertainty and modeling," SIAM Review 25, 379–393 (1983).
- [S] A. K. Soman, S. S. Mishra, M. Shafi, S. Basak, "Inflationary gravitational waves as a probe of the unknown postinflationary primordial Universe," Phys. Rev. D 112, 103521 (2025), arXiv:2407.07956.
- [S] R. Sundrum, "Fat gravitons, the cosmological constant and submillimeter tests," Phys. Rev. D 69, 044014 (2004), arXiv:hep-th/0306106.
- [S] C. G. Tsagas, A. Challinor, R. Maartens, "Relativistic cosmology and large-scale structure," Phys. Rep. 465, 61 (2008), arXiv:0705.4397.
- [S] G. Veneziano, "Scale factor duality for classical and quantum strings," Phys. Lett. B 265, 287 (1991).
---

*Provenance: conjecture and direction, P. R.; derivations, counterexamples, verification and drafting, Claude (Anthropic). The literature sweep, an independent re-derivation, an independent recomputation of the numbers, a steelman of the chat claim and a sweep of the program's record were run by separate agents; their files are listed in `notes/phase-space-diameter-worklog.md`. Round-5 blind review: verdict B from both referees; v1.1 applies the accepted revisions (`review/round5-adjudication.md`).*
