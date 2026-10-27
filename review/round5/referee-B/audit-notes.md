# Referee B — audit notes

Manuscript: `manuscript.md` (copy in this directory), "The Size of the Universe in Position and in Momentum", v1.0, 2026-10-26.

Working directory: /tmp/claude-1000/-home-paul-git-reinholdtsen-conjugate-matter/8384be45-7ab6-4f04-95e6-8a6a977bced8/scratchpad/round5/referee-B

- `scripts/` — my scripts (all numbers below rest on these)
- `outputs/` — their printed output
- `downloads/` — untrusted downloaded literature (never executed; read with `python -I` or /usr/bin/grep)
- `venv/` — local venv (pypdf, scipy) for reading PDFs

Isolation: I read only the manuscript copy and my own files. Program documents [H1], [H2], [P1]–[P4] are treated as premises.

Weighting for this referee: §4, §7, §8, prior art for every [D]; steelman of the withdrawn claim (§6); premises of the §8.2 bound.

---

## Step 2 — Numbers (first pass)

Script: `scripts/recompute_numbers.py` → `outputs/recompute_numbers.txt`. Inputs are mine: CODATA 2018; Planck 2018 H0 = 67.4, Ωm = 0.315; T0 = 2.7255 K; N_eff = 3.046 (so Ω_r = 9.21e-5, Ω_Λ = 0.6849); A_s = 2.1e-9. Comoving particle horizon and today's event horizon by quadrature of the full ΛCDM+radiation H(a).

Reproduced (manuscript value → mine): κ 1.708 → 1.708; alternatives 0.316/0.854/1.377 → 0.3162/0.8541/1.377; R_obs 46.1 Gly → 46.13; N_γ 1.43e89 → 1.430e89; S 1.01e90 → 1.007e90; s/n 7.04/3.60 → 7.039/3.602; D_x 8.73e26 → 8.729e26 m; D_p 6.78e-31 → 6.781e-31; area 8.9e29 h → 8.933e29; S^{1/3} 1.0e30 → 1.002e30; (11/4)^{1/3} 1.40; (106.75/3.909)^{1/3} 3.01; c/H0 1.372e26; L/l_P 8.49e60; cube 6.12e182; L_Λ 1.66e26; S_GH 3.31e122 → 3.308e122; event horizon 16.7 Gly → 16.68, S 3.0e122 → 2.995e122; CKN 4.19 meV; Ω_GW 1.4e-122 → 1.387e-122; S_dS^{1/4} 4.3e30 → 4.265e30; k_BT0 0.235 meV; ρ_Λ^{1/4} 2.24 meV; A0 5.2e92 (log 92.72, ln 213.5, √3·ln 369.8, 106.7 e-folds); a_sq 4.4e-47/T 4.4e14 T_P; with g_s 2.5e-47/2.5e14; √(2πκ) 3.28; 0.61; A(T_P) 6.4e28; T_reh 5.7e15 GeV; A(reh) 2.9e35; Hubble square 0.28 T_P, 0.75 l_P, 0.45 quanta; N_H 4.4e87; A_H 1.6e92; two-region 1.24e30 l_P, 5.6e89 patches, 8.2e29; λ table 47.1/51.8/84.0 μm, 4.19/3.81/2.35 meV; 0.535; 88.1 μm; χH0/c 3.18; √Ω_Λ 0.83; λ/l_P 3.2e30; 3.7e11 m = 2.46 au; c⁴/G 1.21e44 N; 1.4e-17 / 1.2e-17 N; Coulomb 8.24e-8 N; ratios 5.8e9, 6.9e17; Vainshtein radius 1.5e-12 m (1 kg, cubic form; 1.6e-9 m for the quintic Fierz–Pauli form); 5.23 meV; 5.11 meV ↔ 38.6 μm; 2.34×; conjugate extents 1.04e-31 l_P, 5.40e61 m_Pc; lever arm 4.9e-60 m, 41.9 m (50.7 m for L_Λ).

Discrepancies or notes from this pass (all from the same script/output):
- **Born's b c ≈ 1.4×10⁸ eV "from the classical electron radius"**: ħc/r_e = 7.00e7 eV; 2ħc/r_e = 1.40e8 eV. The quoted value corresponds to ħc/(r_e/2), not ħc/r_e. Must check how Born defined b (citation step).
- **E_inf < 1.39e16 GeV**: the standard single-field formula V^{1/4} = (3π²A_s r/2)^{1/4} M̄_P with r = 0.036, A_s = 2.1e-9 gives 1.409e16 GeV (1.4% higher); only affects T_reh at the 0.4% level. Check Soman et al. (citation step). Not material.
- **"In units of λ = √(l_P L_Λ) ... square at T ≈ 1.7 TeV"**: 1.67 TeV with no g_s; 0.96 TeV with g_s = 106.75. §6 states the g_s-corrected value as well; §7 gives only the uncorrected one. Minor.
- **"This halves the exponent"** (§7): log10(Λ l_P²) = −121.5, log10(λ/l_P) = 30.5. Relative to the 10⁻¹²² the sentence just quoted, the exponent is quartered; it is halved only relative to L_Λ/l_P = 10^61.0. Minor wording error.
- (M_X/H0)² = 1.3e61 (M_X² /3H0² = 4.4e60): "of order 10⁶¹" fine.

## Step 3 — Re-derivations (first pass)

Script: `scripts/derivations.py` → `outputs/derivations.txt` (sympy + numpy + mpmath).

1. κ: from the Bose–Einstein integrals (2ζ(3), π⁴/15, checked by quadrature) κ = 3^{1/3}π^{10/3}/(30ζ(3)^{4/3}) = 1.70812 exactly, T- and R-independent; alternatives 0.316181, 0.854061, 1.37674 (= 2^{2/3}π^{11/3}/(60ζ(3)^{4/3})). Confirmed.
2. Square closed forms: side √(2πκ)N^{1/6} = 3.2760 N^{1/6}; T_sq = 0.60641 N^{1/6} T_P. Confirmed.
3. Fourier transform of exp(iZx²/2) analytically gives exp(i(−1/Z)p²/2); numerical transform of Z = 0.3+0.7i gives −0.5172+1.2069i. Δx² = 1/(2Y), Δp² = |Z|²/(2Y), Δx/Δp = 1/|Z|. Confirmed.
4. Fubini–Study metric of normalized ψ_Z: g = |dZ|²/(8Y²), i.e. 1/8 of the Siegel/Poincaré metric (both by the Var(x²) formula and by direct integration). Siegel length 2r → FS length r/√2. Confirmed.
5. d(i,Z) − |ln|Z|| ≥ 0 over 20 000 random Z (minimum 2.4e-9, at X ≈ 0); equality on X = 0; σ_x = e^r/√2 → d = 2r; degree d: √d |ln y|. Confirmed (geometric reason: |Z| = const are geodesics with common perpendicular the imaginary axis).
6. ρ_λ symplectic; ρ_{λ1}ρ_{λ2}⁻¹ = diag((λ1/λ2)², (λ2/λ1)²); A·A' = 1; self-dual λ = √(ħL/P). Confirmed.
7. Fourier box self-dual iff λ² = l_P L; with λ² = l_P L_Λ and L = c/H(t), A = H_Λ/H = √Ω_Λ(t); Λ = 3l_P²/λ⁴; ρ_Λ^{1/4}/√(M_P H0) = (3Ω_Λ/8π)^{1/4}; ħc/√(l_P L) = √(E_P ħc/L). Confirmed.
8. Minisuperspace: dual kinetic term M̃²C³ȧ²/a⁵; a → C/a exchanges the two iff M̃ = M_P; equal at a = √C; Friedmann 3H²(M_P² + M̃²C³a⁻⁶) = ρ. Confirmed.
9. Bimetric mass-eigenstate decomposition: matter on g couples to massless mode with 1/M_eff and to massive mode with (M_f/M_g)/M_eff; static-source tensor factors 1/2 (massless) vs 2/3 (massive) give α = (4/3)(M_f/M_g)², = 4/3 at equal Planck masses. Confirmed at the level of the linear theory around proportional backgrounds with ratio 1 (see premises, Step 4).

## Step 1 — Citations

Bibliographic records: every arXiv-numbered reference checked against INSPIRE (`scripts/parse_inspire.py` on `downloads/inspire/*.json` → `outputs/inspire_records.txt`); the non-arXiv ones against Crossref (`scripts/parse_crossref.py` → `outputs/crossref_records.txt`). All 37 entries match title, authors, journal, volume, page/article and year as given. (Gabor's Crossref page range is 429–441 for Part 1; the scan runs to 457 because Parts 2–3 follow.)

Content and quotations (sources downloaded to `downloads/`, LaTeX sources extracted with `scripts/extract_eprints.py`, PDFs read with `scripts/pdf2txt.py`/`scripts/pdf_images.py` under `python -I`; searched with /usr/bin/grep):

| Reference | What it is cited for | Result |
|---|---|---|
| CKN 1999 | "L³Λ⁴ ≲ L M_P²"; "Λ ∼ 10^{−2.5} eV"; "This observation does not predict the cosmological constant's value" | all three verbatim (hep-th/9803132, lines 200, 262, 265); M_P unreduced (S_BH = πL²M_P²) |
| Bousso 2000 | "a universe with Λ > 0 cannot have entropy greater than N = 3π/Λ" | verbatim (lines 125–126) |
| Gibbons–Hawking 1977 | horizon entropy | abstract: "area can be interpreted as the entropy"; coefficient supplied by Bousso. OK |
| Grosse–Wulkenhaar 2005 | "identify the parameter √Ω with the ratio of the Planck length to the size of the (finite!) universe"; self-dual at Ω = 1 | both verbatim (lines 4252–4254; "self-dual case Ω=1") |
| FKGLM 2023 (PRD) + essay | quantum area constraint, shape not fixed; L = N_qλ, M = N_pε; "LM/2πℏ = N^{1/4}"; "inversely related"; ρ ≲ ħ/(ℓ²ℓ_P²); M ∼ ℏ/√(ℓℓ_P); "λ ∼ (ℓℓ_P)^{1/2} ∼ 10^{−4} m ... M ∼ 10^{−3} eV"; "not universal but instead … chosen in the context of the system in question" | all verbatim; the last is in the essay (2303.17495 line 470) |
| BHM 2023 | l_Λ = √(l l_P), λ_cc = l_P²/l_Λ⁴; dual-curvature quote; TeV as geometric mean | verbatim (lines 2290, 2298; abstract line 317; μ_vac ~ TeV, lines 2014–2019). Note BHM also use l_Λ for the de Sitter radius (line 438) — harmless |
| Padmanabhan 2006 | L_DE = √(L_P L_Λ), heading "Geometrical Duality in our Universe" | verbatim (lines 305, 316) |
| Mignemi 2010 | Snyder–de Sitter duality quote | quote verbatim (lines 768–770), but Mignemi calls it a duality for X↔P with Λ↔Ω, not "Born duality", and states no geometric-mean length. Citing it as an "earlier version of the geometric-mean length" overreaches (minor) |
| CosMIn 2013 | mode count fixing Λ | verified (abstract) |
| Egan–Lineweaver 2010 | photons 5.40e89 k, SMBH ~3e104 k, CEH 2.6e122 k "Table 1" | photons and SMBH in Table 1; the CEH value is in the abstract and Table 2 (Scheme 2), not Table 1 (minor) |
| Lee et al. 2020 PRL | "any gravitational-strength Yukawa interactions to ranges <38.6 μm"; heavy graviton citing Aoki–Mukohyama; "must be greater than 5.1 meV" | all verbatim (2002.11761 lines 33, 38, 151–152) |
| Lee 2020 thesis Table 11.4 | α = 4/3 one-sided limit 37.7 μm | table found (thesis pp. 133–136, `downloads/thesis/thesis.txt`). `scripts/torsion_interp.py` → `outputs/torsion_interp.txt`: log-log interpolation of the +α95 column gives 37.68 μm at α = 4/3. The "published 38.6 and 30 μm" are reproduced only by the |α95| column (38.63, 30.23 μm); the +α95 column gives 40.66 μm at α = 1. So the check validates the method on one column and the result uses the other; the +α95 choice is the conservative one (|α95| column gives 35.8 μm, 5.5 meV). Minor transparency point |
| Aoki–Mukohyama 2016 | heavy graviton in bigravity | verified; their eq. has α = (4/3)M_pl²/M_G² (same structure) |
| Lüben–Mörtsell–Schmidt-May 2020 eq. 9 | V(r) with α = (4/3)(M_f/M_g)² | equation number verified (eq. 9 by count, `scripts/count_eqs.py`), but the source reads V = −(1/m_Pl²)(1/r + (4α²c²/3)e^{−m r}/r) with c the background ratio f̄ = c²ḡ. The manuscript drops c² (see Step 4) |
| Enander–Mörtsell 2013 eq. 4.1 | same | first equation of §4: Φ = −(GM/r)(1 + (4c²/3)e^{−m_g r}), with their c defined after rescaling f by M_g²/M_f² (so c² ⊃ (M_f/M_g)² × background ratio²) |
| Low 2006 | maximal force b | verified ("bounded by a universal constant b") |
| FLM 2015 | G_N tied to λ/ε | verified: ħ = λε, α' = λ/ε, "G_N = ρα'" |
| Hsu 2004 | Hubble-tracking vacuum energy excluded | verified (w = 0, strongly disfavoured) |
| Bambi–Urban 2008 | reciprocity map on uncertainty extents | verified (eq. symm). Note: with L_X = L_Λ (their choice, after Bolen–Cavaglià 2005) the map's scale is (L_X L_Pl)^{1/2} — i.e. the geometric-mean self-dual length. This is earlier prior art for §7 that the manuscript does not credit there (minor) |
| Ohsawa 2015; de Gosson 2013 App. A | Siegel half-space, Möbius action on Gaussians | verified (App. A: (S,M) ↦ (C+DM)(A+BM)^{-1}) |
| Gabor 1946 | three quotes | from the scan (`downloads/gabor/img/p01, p07`): "areas … proportional to the number of independent data which they can convey" (p. 429) ✓; "could have been formally obtained by replacing a co-ordinate x by t, the momentum p by f, and Planck's constant h by unity" (p. 435) ✓; "Because of its self-reciprocal character, the probability signal…" (p. 435) — Gabor applies "self-reciprocal" to the Gaussian pulse family (any sharpness α), not to the single Fourier-invariant member Z = i (minor misattribution) |
| Shannon 1949 | "can be specified by giving 2TW numbers" | sentence frame verbatim in the 1998 reprint text layer (math glyphs not machine-readable; "2TW" is standard) ✓ |
| Slepian 1983 | "engineering folk theorem", rigorous version | abstract (via a downloaded bibliography record): "a rigorous version of an engineering folk theorem called the 2WT-Theorem" ✓ |
| Born 1938 | Eddington quote; "upper limit for the distance … radius a"; "Let us transfer this consideration to the p-space"; "upper limit for momenta … radius b"; finite number of states; "Whether these nuclear constants are connected with the corresponding molar constants … cannot be decided yet"; b from r_e; bc ≈ 1.4e8 eV | all verified in the Internet Archive OCR of Proc. R. Soc. A 165 (`downloads/born/prsa165_27020.txt`, lines 18178–18990). Born fixes b = h/(πr_0) = 7.43e-15 g cm/s (eq. 26) and gives bc = 1.41e8 eV (eq. 37). `scripts/steelman_and_premises.py` §F: h c/(π r_e) = 1.401e8 eV ✓. Born also asks whether b is universal or system-specific — not mentioned in the manuscript |
| Born 1949 | "splits ħ = ab … fixes the length from particle masses" | full text not accessible (APS paywall; no open copy found). Secondary sources confirm constants a, b with x → ap, p → −bx and the Born–Green mass determination, but not "ħ = ab". Unverifiable |
| Martin–Vennin 2016 | r ~ 50 at end of inflation | verbatim ("r_k ∼ 50", line 799) |
| Kiefer–Polarski 2009; KPS 1998; Grishchuk 1993 | r ~ 100–120 today | "r_k ∼ 100 and even larger" (KP09; note r_k ≡ ln(a_f/a_k)); "r ≈ 100" (KPS98); "r ≈ 120" (Gr93) ✓ |
| Bhattacharyya et al. 2020 | squeezing growth "read as a clock" | the paper never uses "clock"; it reads complexity as growing linearly with e-folds in de Sitter and *decreasing* in the radiation era while squeezing continues. Overstated (minor) |
| Grain–Vennin 2020 | squeezing depends on canonical variables | verified (abstract) |
| BICEP/Keck 2021 | r < 0.036 | verified (r_0.05 < 0.036, 95%) |
| Soman et al. 2025 | E_inf < 1.39e16 GeV | verbatim (eq. inf_Energy_scale_inflation) |
| Bedroya–Vafa 2019 | TCC | verified |
| Ma–Bertschinger; Tsagas et al.; Fixsen; Planck 2018; PDG | standard inputs | verified (Fixsen 2.72548 K) |

## Step 3 — Re-derivations (additions)

- Bimetric α: `scripts/derivations.py` §9 reproduces α = (4/3)(M_f/M_g)² for proportional backgrounds with unit ratio; the general linear result (Lüben et al. eq. 9) is (4/3)(M_f/M_g)²c².
- Torsion-balance bound: `scripts/torsion_interp.py` → 37.68 μm (α = 4/3, +α95, log-log), 5.23 meV.
- Born b: `scripts/steelman_and_premises.py` §F → bc = 1.401e8 eV.

## Step 4 — Conceptual audit

Script for all numbers in this step: `scripts/steelman_and_premises.py` → `outputs/steelman_and_premises.txt` (and `scripts/torsion_interp.py` → `outputs/torsion_interp.txt`).

### 4.1 Premises behind the §8.2 bound

Stated: X massive spin-2 with M_X = polarization-breaking scale [P1 §7]; equal Planck masses forced by reciprocity [P1 §7.5, P3 §3]; matter on g only; linear Hassan–Rosen potential with α = (4/3)(M_f/M_g)²; no Vainshtein screening at 50 μm (checked: r_V ≈ 1.5e-12 m for 1 kg, 1.6e-9 m even in the quintic Fierz–Pauli form; `outputs/recompute_numbers.txt`).

Unstated, and load-bearing:
1. **Background ratio c = 1.** The cited formula (Lüben et al. eq. 9; Enander–Mörtsell eq. 4.1) is α_Y = (4/3)(M_f/M_g)²c² with f̄ = c²ḡ. The manuscript drops c². With M_f = M_g and the g↔f-symmetric couplings β_n = β_{4−n} that an exact exchange symmetry requires, the background equation factorises as (c−1)(c+1)(β1c² + (3β2−β0)c + β1) = 0 (sympy, §E): c = 1 is the symmetric vacuum; the other roots come as a (c, 1/c) pair — the vacua in which the exchange symmetry is spontaneously broken. In those, α_Y = (4/3)c². Using Table 11.4 (+α95, log-log): c = 0.5 → λ_X < 57.0 μm (M_X > 3.46 meV); c = 0.8 → 42.5 μm; c = 1 → 37.7 μm; c = 1.5 → 30.8 μm. The self-dual length 47.1 μm is allowed for c < 0.672; 84.0 μm for c < 0.302. So "M_X c² > 5.2 meV, whatever sets it" and "an X set by the self-dual length is excluded" hold only for c = 1 (unbroken exchange in the background) or c ≳ 0.67. In a program whose central premise is spontaneously broken reciprocity this needs to be stated and argued. → **major (fixable)**.
2. Single Yukawa: the limit assumes one new Yukawa; other light fields of the program (the coset model's flat directions [P4]) could add attractive or repulsive terms. Not discussed. → minor.
3. M_f = M_g with matter on g only is not protected against matter loops, but δM_g²/M_P² ~ N Λ_UV²/(16π² M_P²) is negligible unless the cutoff is near M_P. → not a finding.
4. The +α95 column is defined by Δχ² = 6.17 (thesis p. 133), more conservative than a one-parameter 95% limit; 37.7 μm is therefore conservative. → fine.

### 4.2 §4 statement "it holds at no other epoch"

Per-axis counts (chat S_rad^{1/3} vs FKGLM N^{1/4}):
- Reading A, the manuscript's own definitions (fixed comoving region; S_dS with fixed Λ): ratio 0.235, the same at every epoch, because both numbers are constants.
- Reading B, epoch-dependent (radiation entropy inside the then-particle horizon vs π(c/H l_P)²): ratio 0.26 today, 0.78 at z = 1100, 0.83 throughout the radiation era (z ≥ 1e4). The match is better at early times, because in radiation domination kT ~ √(M_P H) (ratio 0.57 vs 0.056 today).
- Reading C (chat region fixed, FKGLM N at then-Hubble scale): ratio 0.26 today, 1.2 at z = 10, 40 at z = 1100 — holds for z ≲ 30.
Only the auxiliary statement "k_BT ~ ρ_Λ^{1/4} within ×10" is specific to now (z ≲ 9). The sentence conflates it with the count comparison, which under the manuscript's own definitions is epoch-independent. → minor error in a [D][V] claim.

### 4.3 The withdrawn claim (§6): constructed readings

- **S1, squeezed perturbation modes.** Rectangle = Wigner ellipse of the largest-scale curvature mode; round (Z = i in the mode's own variables) at Hubble exit; aspect ratio today e^{2r}; Siegel distance 2r (the manuscript's own §5 result). Literature r ≈ 100–120 gives e^{2r} = 10^86.9–10^104.2; 10^92 needs r = 105.9 (the radiation rectangle's ln A0 = 213.5 corresponds to r = 106.75). This reading gives the chat's "~10^92" and "clock measuring distance from self-duality" physical content independent of λ. It does not give "square in Planck units exactly at the bounce": the mode is round only in its own units, at Hubble exit, which is not a bounce (in bouncing models modes are already squeezed at the bounce). The manuscript introduces squeezing in §5 but never tests it as a reading in §6, and §2's "Its numbers fit the radiation rectangle" overlooks that 10^92 also fits this reading. → minor omission; withdrawal unaffected.
- **S2, scale-factor duality (the program's own §8.4).** With M̃ = M_P the a ↔ C/a symmetry is exact in the kinetic terms and the step sits at a = ã = √C. For C equal to the observable-universe rectangle's area per axis in Planck units (5.61e30, √C = 2.37e15 = 3.28 N^{1/6}) the step is exactly the §6 square epoch; for C = 1 and one thermal cell it is at T ≈ 0.46 T_P. Is the step a bounce? H² = ρ/(3M_P²(1 + C³a⁻⁶)) > 0 for every a (also with dual radiation), so a and ã are monotonic; only max(a, ã) has a minimum at √C — a pre-big-bang-style "dominant-frame" bounce. Under that reading the claim is true by construction, but only by tuning C to one particular region (a global event cannot depend on which comoving region is chosen), at a super-Planckian temperature. The manuscript's obituary ("No reading puts a square rectangle of 10⁹⁰ cells at any bounce") is defensible only if "bounce" is defined as an extremum of a or ã; it should say so and reconcile §6 with §8.4, which itself places the step at the §6 square epoch. → minor (fairness/completeness), withdrawal stands.
- **S3, Hubble sphere at an actual bounce.** At any bounce H = 0, so the Hubble rectangle is infinitely elongated — a stronger refutation than "dimensional analysis", which the manuscript uses only for the turnaround. → minor.
- **S4, the |Z| = 1 inference.** The manuscript takes the record's a² = Im Z, making Z = i a maximum of a (turnaround). Its own slice convention (Δx/Δp = 1/Y ∝ a², so Im Z ∝ a⁻²) would make Z = i a *minimum* of a — a literal bounce (§D: cosh s minimal at s = 0). The circle reading then reproduces "square exactly at the bounce" even more directly; it still fails for the reasons given (Δx = Δp on the whole circle; X ≈ 1 energy density). Convention-dependent wording. → minor.
- "Before the radiation existed" presupposes inflation and reheating; in a bounce-instead-of-inflation scenario radiation can exist at the bounce, leaving only the super-Planckian-temperature objection (still decisive). → minor.
Judgement: withdrawn under every reading I could construct; the treatment is fair in its conclusion but incomplete in its coverage (S1, S2) and in one convention (S4).

### 4.4 Other consistency points
- §7 "This halves the exponent": quartered relative to Λl_P² ~ 10⁻¹²² (log10 λ/l_P = 30.5); halved only relative to L_Λ/l_P. Minor.
- §7 "square at T ≈ 1.7 TeV": no g_s; 0.96 TeV with g_s = 106.75, unlike §6 which gives both. Minor.
- §4 closing sentence "the cell's own length is their geometric mean" (of the UV momentum extent and IR position extent) is dimensionally muddled; in FKGLM the momentum extent is M ~ ħ/√(ℓℓ_P) ~ meV (N_p ~ 1), not ħ/l_P, so FKGLM's regulated phase space differs from the §7 Fourier box even though both have cell length √(ℓℓ_P). Minor wording.
- §6 uses "X" both for Re Z and for the momentum graviton, and the 10⁶¹ estimate assumes the record's identification of Re Z with the graviton amplitude. Premise; cannot check.
- Tags: speculation labelled ([O], "inference", "numerology"); [T] attributions mostly correct (exceptions in Step 1).

### 4.5 Prior art for [D] results (searches: INSPIRE fulltext/title queries in `downloads/inspire_q/`, arXiv sources)
- κ identity / constant comoving area: textbook blackbody counting plus Liouville; no specific prior statement of κ found; [D] fine.
- Reciprocity on rectangles, squeeze relation, "self-dual for one λ": Born 1949 (constants a, b), Bambi–Urban 2008 (explicit map with λ² ∝ L_X L_Pl).
- Distance/clock: Kiefer–Polarski 2009 define r_k ≡ ln(a_f/a_k), i.e. squeezing as e-fold count; FS = 1/8 Siegel is the standard Gaussian-state geometry.
- Self-dual length √(l_P L_Λ): additionally Bambi–Urban 2008 / Bolen–Cavaglià 2005 (extended GUP with L_Λ); Beane 1997 (sub-mm forces at the critical-density Compton wavelength); Sundrum 2004 (fat graviton at the dark-energy length); Kapner et al. 2007 (torsion-balance tests "below the dark-energy length scale", λ_d ≈ 85 μm). These also anticipate §8.2's conclusion that a gravitational-strength force at that length is excluded. Not cited.
- "Dark-energy scale by Friedmann": holographic dark energy, Li 2004 (ρ = 3c²M_P²L⁻²), alongside CKN/Hsu. Not cited.
- de Sitter as the box's self-dual state (A = √Ω_Λ(t)): no direct prior statement found; closest is Padmanabhan 2006 (ρ_DE = √(ρ_UV ρ_IR)) and BHM's dual-curvature picture. Born-geometry dark energy that is dynamical: Jejjala–Kavic–Minic–Takeuchi 2022 and Hur et al. 2025 (JCAP 11, 054). Not cited.
- Maximal force: Jarvis–Morgan 2008 (J. Phys. A 41, 465203; arXiv:0806.4794) already equate the Born force scale with c⁴/G ≈ 10⁴⁴ N at the Planck scale; the 10⁻¹⁷ N value at the meV scale appears new and is trivial.
- §8.2 bound: Lee et al. 2020 give the heavy-graviton bound for |α| = 1 (5.1 meV); the α = 4/3 number is new but follows from their table. A 2026 review (arXiv:2605.18212) confirms UW 2020/HUST 2020 are still the tightest limits at these ranges, so no stronger omitted constraint.
- §8.4 a ↔ C/a symmetry and self-dual point: scale-factor duality (Veneziano 1991, PLB 265, 287), pre-big bang (Gasperini–Veneziano 1993), string-gas/T-duality cosmology (Brandenberger–Vafa 1989), thermal-duality bounces at the self-dual point (Kounnas–Partouche–Toumbas 2011). Not cited; also relevant to the §6 readings.

## Step 5 — Verdict

**B (flawed but salvageable), confidence 0.75.**

Basis:
- Numbers: every number in the manuscript reproduced from my own inputs (`outputs/recompute_numbers.txt`); none wrong beyond rounding. Wording/convention slips: "halves the exponent" (quartered), 1.7 TeV without g_s.
- Derivations: all symbolic and numerical claims re-derived and confirmed (`outputs/derivations.txt`).
- Citations: all bibliographic records correct; quotes verbatim in 30+ sources including Born 1938 (Internet Archive OCR), Gabor 1946 (scan) and the Lee thesis table. Minor misattributions: Egan–Lineweaver CEH value is Table 2, not Table 1; Gabor's "self-reciprocal" refers to the Gaussian family, not the single fixed point; Mignemi states no geometric-mean length and does not call the duality Born's; Bhattacharyya et al. never read complexity as a clock (and find it decreasing in the radiation era). Born 1949's "ħ = ab" could not be checked.
- Major: §8.2 derives α = 4/3 from equal Planck masses alone, dropping the background-ratio factor c² that is in both cited formulas. In a g↔f-symmetric bimetric theory the symmetry-broken vacua have c ≠ 1, so the headline bound λ_X < 37.7 μm / M_X > 5.2 meV ("whatever sets it") and the exclusion of X at the self-dual length hold only for c = 1 (exclusion of 47.1 μm needs c > 0.67). Fixable by stating c = 1 and giving the bound as a function of c.
- Minor: §4 "it holds at no other epoch" is false under the manuscript's own definitions (ratio constant) and under the epoch-dependent reading (ratio 0.83 in the radiation era); §6's survey of readings omits the squeezed-mode reading (which matches 10^92 with r ≈ 106) and the scale-factor-duality reading that §8.4's own step points to, and the |Z| = 1 inference depends on a convention opposite to §5's. The withdrawal itself stands under every reading constructed.
- Prior art omitted: Bambi–Urban 2008/Bolen–Cavaglià 2005 (EGUP reciprocity at √(L_Λ l_P)); Beane 1997, Sundrum 2004, Kapner et al. 2007 (forces at the dark-energy length and their torsion-balance exclusion); Li 2004; scale-factor/T/thermal-duality cosmology (Veneziano 1991, Gasperini–Veneziano 1993, Brandenberger–Vafa 1989, Kounnas–Partouche–Toumbas 2012); Jarvis–Morgan 2008; Jejjala–Kavic–Minic–Takeuchi 2022 / Hur et al. 2025.

Weakest link: the premise α = 4/3 in §8.2 (equal Planck masses ⇒ α = 4/3 only for proportional backgrounds with ratio c = 1), which carries the manuscript's only new number.
