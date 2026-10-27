# Referee A audit notes: "The Size of the Universe in Position and in Momentum" (v1.0, 2026-10-26)

Working directory: /tmp/claude-1000/-home-paul-git-reinholdtsen-conjugate-matter/8384be45-7ab6-4f04-95e6-8a6a977bced8/scratchpad/round5/referee-A
Isolation: only manuscript.md and files created here were read. Program documents [H1],[H2],[P1]-[P4] treated as premises.
Layout: scripts/ (my code), outputs/ (printed output of each script), downloads/<source>/ (untrusted downloaded files, read with python -I only).

## Step 1. Citations

Method: arXiv API metadata for all 33 arXiv IDs (scripts/parse_arxiv_meta.py -> outputs/arxiv_meta.txt); Crossref for
non-arXiv DOIs and missing journal data (scripts/fetch_crossref.sh, parse_crossref*.py -> outputs/crossref_1.txt,
outputs/crossref_2.txt); INSPIRE (outputs/inspire_1.txt). Full texts downloaded to downloads/arxiv/<id>/paper.pdf,
text extracted with `python -I scripts/pdf2txt.py`, searched with /usr/bin/grep. Lee thesis from UW ResearchWorks
(downloads/lee_thesis/). Born 1938/1949 (Royal Society, APS) blocked by a Cloudflare challenge; Gabor 1946 and
Slepian 1983 not found in open copies.

Bibliographic data: all 33 arXiv IDs resolve to the stated titles and authors; journal/volume/page/year agree with
arXiv journal_ref, Crossref or INSPIRE for every entry (Lueben et al. CQG 37 047001; FKGLM essay IJMPD 32 2342004;
Soman et al. PRD 112 103521; FLM JHEP06(2015)006; Born 1938 PRSA 165 291-303; Born 1949 RMP 21 463; Gabor 1946
J. IEE III 93(26) 429-441; GH 1977 PRD 15 2738; Shannon 1949 Proc IRE 37 10-21; Slepian 1983 SIAM Rev 25 379-393;
PDG 2024 PRD 110 030001). Only cosmetic: in-text "Bedroya-Vafa 2019" vs JHEP 2020 in the list.

Quotes and attributions checked against the source text:
- FKGLM 2023 (2212.00901): "lambda eps = 2 pi hbar ... quantum area constraint. Whereas the area of the modular cell is
  fixed by this quantum constraint, its shape is not" (eq. 11 + text) OK; L := N_q lambda, M := N_p eps (eq. 13) OK;
  LM/2 pi hbar = N^(1/4) (eq. 15) OK; "not separately arbitrary but are inversely related" OK; rho <~ hbar/(l^2 lP^2)
  (eq. 21) OK; M ~ hbar/sqrt(l lP) (eq. 23) OK; "the above geometric mean ... lambda ~ (l lP)^(1/2) ~ 1e-4 m ... M ~ 1e-3 eV" OK.
- "not universal but instead is to be chosen in the context of the system in question": in the essay 2303.17495 p. 6, OK
  (the citation names both papers).
- BHM (2212.06086): l_Lambda := sqrt(l lP) (eq. 4.74) OK; lambda_cc := rho l_P^2 = l_P^2/l_Lambda^4 (after 4.75) OK;
  "the curvature of the dual spacetime is the cosmological constant of the observed spacetime, while the size of the
  dual spacetime is the gravitational constant" (abstract) OK; TeV scale as seesaw/geometric mean (eqs. 4.50-4.51) OK.
- CKN (hep-th/9803132): "L^3 Lambda^4 <~ L M_P^2" (eq. 2) OK; "Lambda ~ 10^-2.5 eV" OK; "This observation does not predict
  the cosmological constant's value" OK verbatim. CKN's M_P is unreduced (S_BH = pi L^2 M_P^2) OK.
- Bousso (hep-th/0010252): "a universe with Lambda > 0 cannot have entropy greater than N = 3 pi/Lambda" OK verbatim.
- Egan-Lineweaver (0909.3983): photons 5.40e89 k and SMBHs 3.1e104 k are in Table 1 OK; the cosmic event horizon 2.6e122 k
  is in Table 2 (and eq. 46 / abstract), not Table 1 -> pinpoint error (minor). (E&L's own eq. 13 prints 2.03e89 for
  photons, inconsistent with their Table 1; s_gamma x V_obs = 5.41e89, so Table 1 is right.)
- Lee et al. PRL 2020 (2002.11761): "limiting with 95% confidence any gravitational-strength Yukawa interactions to
  ranges <38.6 um" (abstract) OK; "the dilaton[28] or heavy graviton[3] mass ... must be greater than 5.1 meV", ref [3] =
  Aoki-Mukohyama OK; "largest extra dimension ... toroidal radius less than 30 um" is the 30 um value OK.
- Lee thesis Table 11.4 (pp. 133-136): columns lambda, alpha*, +alpha95, -alpha95, |alpha95| exist OK; 37.7 um reproduced
  (Step 2, scripts/lee_interp.py).
- Grosse-Wulkenhaar (hep-th/0401128, p. 41): sqrt(4 Omega theta) is the minimal momentum; "We can thus identify the parameter
  sqrt(Omega) with the ratio of the Planck length to the size of the (finite!) universe" OK verbatim.
- Padmanabhan 2006 (astro-ph/0603114): section "3.1. Geometrical Duality in our Universe", "L_DE = sqrt(L_P L_Lambda)" OK.
- Mignemi (0802.1129, p. 16): "This duality connects the high-energy/short-distance regime, governed by the Planck area
  Omega, with the low-energy/long-distance regime, governed by the cosmological constant Lambda" OK verbatim. The paper
  states the duality; it does not write a geometric-mean length (the manuscript lists it among "earlier versions of the
  geometric-mean length": a stretch, minor).
- Shannon 1949 (copy at fab.cba.mit.edu, Proc IRE pages 10-21): "...can be specified by giving 2TW numbers" OK.
- Low 2006 (math-ph/0506031, Type-3 font decoded with scripts/decode_t3.py): "Forces have become relative and are bounded
  by b", "b is a universal constant with the dimensions of force", b = alpha_G c^4/G OK.
- FLM 2015 (1502.08005): "hbar = lambda eps, alpha' = lambda/eps. The Newton constant is proportional to the latter scale,
  G_N = rho alpha'" OK.
- Bambi-Urban (0709.1965): extended GUP invariant under Dx -> (alpha/beta)^(1/2) (L_X L_Pl) Dp, Dp -> ... (eq. 4), with
  L_X = L_Lambda in their ref. [4] OK. NB this map is rho_lambda with lambda^2 ~ L_Lambda L_Pl, i.e. the section 7 self-dual
  length itself; the manuscript cites B-U in section 5 but not as prior art for section 7 (omission, minor).
- Squeezing: Martin-Vennin "at the end of inflation, r_k ~ 50" OK; Kiefer-Polarski "r_k ~ 100 and even larger" OK;
  KPS "r ~ 100" OK; Grishchuk "r ~ 120 ... Hubble frequencies" OK. Grain-Vennin abstract (canonical-variable dependence) OK.
- Bhattacharyya et al. 2020 (2001.08664): computes circuit complexity, which grows linearly with e-folds during de Sitter
  but DEcreases in the radiation era ("de-complexification"); the word "clock" does not occur. "That growth has been read
  as a clock" overstates the source (minor).
- Soman et al. (2407.07956, eq. A.31): "E_inf < 1.39e16 GeV" OK. BICEP/Keck: r_0.05 < 0.036 (95%) OK. Fixsen: 2.72548 +- 0.00057 K OK.
  Planck 2018 abstract: H0 = 67.4 +- 0.5, Om = 0.315 +- 0.007 OK. Bedroya-Vafa TCC wording OK. Hsu: w = 0, "strongly
  disfavored" OK. CosMIn: counts modes crossing the Hubble radius OK. Ohsawa and de Gosson App. A (Siegel half-space,
  transitive Sp action on Gaussians) OK. Gibbons-Hawking 1977 abstract (horizon area as entropy) OK.
- Lueben et al. 2020 eq. (9): V = -(1/m_Pl^2)(1/r + (4 alpha^2 c^2/3) e^(-m r)/r), alpha = m_f/m_g, c the background ratio
  (f = c^2 g). Enander-Moertsell 2013 eq. (4.1): Phi = -(GM/r)(1 + (4c^2/3) e^(-m r)). The manuscript's
  "alpha = (4/3)(M_f/M_g)^2" drops the c^2 that both cited equations carry -> misquotation (see Step 4, MAJOR).

Unverifiable (no access to the source): Born 1938 quotes and "b c ~ 1.4e8 eV" (note: hbar c/r_e = 7.00e7 eV;
2 hbar c/r_e = 1.40e8 eV, outputs/num_check.txt, so the stated value needs Born's definition); Born 1949 (hbar = ab,
length from particle masses, "neither paper uses the Planck length"); Gabor 1946 quotes ("areas ... proportional to the
number of independent data", "replacing a co-ordinate x by t ... h by unity", "self-reciprocal"); Slepian 1983
"engineering folk theorem"; PDG 2025 update.

## Step 2. Numbers

Inputs chosen independently: CODATA 2018 (h, c, k_B, e exact; G = 6.67430e-11; a0, m_e, alpha), Planck 2018
(H0 = 67.4, Om = 0.315; sensitivity run with 67.36/0.3153), T0 = 2.7255 K, N_eff = 3.046, g_s0 = 3.909, SM g = 106.75.
Script: scripts/num_check.py -> outputs/num_check.txt (every manuscript number printed beside mine).

All of the following reproduce to the quoted precision:
kappa = 1.70812 and the alternatives 0.31618 / 0.85406 / 1.37674; particle horizon 46.13 Gly (46.14 for 67.36/0.3153),
4.3645e26 m, chi H0/c = 3.180; CEH 16.68 Gly; n_gamma = 410.7 cm^-3; N_gamma = 1.427e89; S = 1.005e90; s/n = 3.6016 and
7.039; D_x = 8.72e26 m (ms 8.73e26: R = 46.1 Gly gives 8.723e26; 46.13 Gly gives 8.729e26 - fine); D_p = 6.781e-31;
area 8.93e29 h; S^(1/3) = 1.002e30; (11/4)^(1/3) = 1.401; (106.75/3.909)^(1/3) = 3.011; c/H0 = 1.3725e26 m; L/lP = 8.492e60;
cube 6.12e182; L_Lambda = 1.658e26 m; S_dS = 3.308e122; CEH entropy 2.99e122 (3.00e122 at 16.7 Gly); Bousso N = S_dS;
CKN 4.190 meV; GW Omega = 1.39e-122; S_dS^(1/4) = 4.265e30; kT0 = 0.2349 meV; rho_L^(1/4) = 2.2403 meV = 88.08 um;
-1/Z = -0.51724 + 1.20690i; A0 = 5.193e92 (log10 92.715, ln 213.49, sqrt3 ln 369.77, 106.74 e-folds); square at
a/a0 = 4.388e-47, T = 4.384e14 T_P; with g_s: 2.529e-47, 2.526e14 T_P; sqrt(2 pi kappa) = 3.2760, T_sq coefficient 0.6064;
N^(1/6) = 7.23e14; A(T_P) = 6.38e28; T_rh = 5.71e15 GeV from E_inf = 1.39e16 (my own E_inf for A_s = 2.1e-9, r = 0.036:
1.41e16); A(T_rh) = 2.92e35; Hubble rectangle square at T = 0.2784 T_P, R_H = 0.752 lP, 0.447 quanta; N_H = 4.45e87;
A_H0 = 1.634e92; two regions: 1.24e30 lP, 5.6e89 patches, A = 8.2e29; lambda = 47.10 / 51.77 / 83.95 um and
4.190 / 3.811 / 2.351 meV; (3 OL/8pi)^(1/4) = 0.5347; sqrt(OL) = 0.828; lambda/lP = 3.203e30; Lambda lP^2 = 2.85e-122;
T_sq(lambda = sqrt(lP L_L)) = 1.671 TeV; sqrt(hbar Dx/Dp) = 3.68e11 m = 2.46 au; c^4/G = 1.2103e44 N; c~ = 1.425e-17 and
1.180e-17 N; Coulomb at a0 = 8.2387e-8 N; ratios 5.78e9 and 6.88e17; Vainshtein (r_s lambda^2)^(1/3) = 1.5e-12 m (1 kg,
50 um); hbar c/37.7 um = 5.234 meV; hbar c/38.6 um = 5.112 meV; 5.234/2.240 = 2.34; conjugate extents 1.04e-31 lP and
5.40e61 m_P c; lever arm 4.94e-60 m/rad and 41.9 m/rad; (M_X/H0)^2 = 1.31e61.

Torsion-balance bound: scripts/lee_interp.py -> outputs/lee_interp.txt, rows of thesis Table 11.4 transcribed from
downloads/lee_thesis/thesis.txt. Log-log interpolation gives |alpha95| = 1 at 38.63 um (published 38.6) and |alpha95| = 8/3
at 30.23 um (published R < 30 um), so the method is validated; the one-sided attractive column gives alpha = +4/3 at
37.68 um -> M_X c^2 > 5.237 meV. Verified (conditional on alpha = 4/3; see Step 4). For reference the two-sided |alpha95|
column would give 35.8 um / 5.51 meV, i.e. the manuscript's choice is the conservative one.

Number-level discrepancies (none changes a conclusion):
- Section 7 numerology: T ~ 1.7 TeV is the no-g_s value; with SM g_s = 106.75 (all relevant species are relativistic at a
  TeV) it is 0.96 TeV (outputs/num_check.txt). Section 6 gives both versions for the Planck-unit square; section 7 only the
  naive one. Minor. (Also: 1.67 TeV is numerically sqrt(kT0 E_P) = 1.69 TeV, the geometric mean of the CMB temperature and
  the Planck energy, not of the vacuum and Planck scales that BHM use; no mechanism is claimed, so this is cosmetic.)
- Section 7 "with the reduced Planck mass, or explicit factors for the black hole's mass, the two differ by factors between
  0.45 and 2.1": 0.447 = (8 pi)^(-1/4) reproduced; explicit black-hole-mass factors give 0.59-0.84; 2.08 needs an extra
  assumption such as rho = Lambda^4/16 pi^2 (scripts/misc_checks.py -> outputs/misc_checks.txt). Unstated convention; minor.
- Section 2 table, row "One cell": sides "one wavelength" and "hbar over that wavelength" give area hbar = 0.159 h, not
  "1" in the column's units of h (outputs/misc_checks.txt). Minor.
- Section 7 "This halves the exponent": Lambda lP^2 ~ 10^-121.5 becomes lambda/lP ~ 10^30.5, a quarter of the exponent;
  it is half of the exponent of L_Lambda/lP ~ 10^61 (outputs/misc_checks.txt). Wording; minor.
- Section 7 "the formula of Berglund, Huebsch and Minic": BHM write lambda_cc = lP^2/l_Lambda^4 with no factor 3 (their
  O(1) factors are dropped); Lambda = 3 lP^2/lambda^4 is the exact version. Minor attribution precision.

## Step 3. Independent re-derivations

Script: scripts/derivations.py -> outputs/derivations.txt (sympy + numpy/mpmath).
(a) kappa from Bose integrals Gamma(3)zeta(3), Gamma(4)zeta(4) (checked by quadrature): sphere/2<|p|> gives
    3^(1/3) pi^(10/3)/(30 zeta(3)^(4/3)) exactly (difference 0); kT/c, <|p|>, cube alternatives exact closed forms. OK.
(b) square: side sqrt(2 pi kappa) N^(1/6) = 3.276 N^(1/6); T_sq = 0.6064 N^(1/6) T_P. OK.
(c) rho_lambda: R^T J R = J (symplectic), area invariant, A' A = 1, lambda^2 = hbar L/P, rho_l1 rho_l2^-1 =
    diag((l1/l2)^2, (l2/l1)^2), Fourier box self-dual iff lambda = sqrt(L lP) (both endpoint conditions agree). OK.
(d) Gaussians: numerical FT of exp(i Z x^2/2), Z = 0.3+0.7i, gives exponent -0.51724+1.20690i = -1/Z at three momenta; Var x =
    1/2Y, Var p = |Z|^2/2Y, Dx/Dp = 1/|Z|; det G = 1 for the Wigner form; d(i,Z) - |ln|Z|| >= 0 on 20000 random Z (min 6e-12),
    equality on the slice; d = 2r for sigma_x = e^r/sqrt2; Fubini-Study metric computed symbolically: g_XX = g_YY = 1/(8Y^2),
    g_XY = 0, i.e. 1/8 of the Siegel metric, so Siegel length 2r <-> FS length r/sqrt2; |tanh s + i sech s| = 1 and
    d(i, Z(s)) = |s|. OK.
(e) A(t)^2 = Omega_L(t) identically for lambda^2 = lP L_Lambda; 3 lP^2/lambda^4 = Lambda; rho_lambda maps hbar/lP to L_Lambda. OK.
(f) 1/sqrt(lP L) = sqrt(M_P/L) (CKN, unreduced); rho_L/(H0 M_P)^2 = 3 OL/8pi. OK.
(g) Bimetric Yukawa strength from the mode decomposition (kinetic matrix diag(M_g^2, M_f^2 c^2), Fierz-Pauli mass term in
    (h_g - h_f), matter on g, static tensor weights 1/2 and 2/3): alpha = 4 M_f^2 c^2 / (3 M_g^2); = 4c^2/3 at M_f = M_g;
    = 4/3 only if also c = 1. Agrees with Lueben et al. eq. 9 and Enander-Moertsell eq. 4.1; disagrees with the manuscript's
    alpha = (4/3)(M_f/M_g)^2, which omits c^2.
(h) a^-6 term: K1 = M_P^2 a adot^2 and K2 = M~^2 C^3 adot^2/a^5 are exchanged by a -> C/a iff M~ = M_P; equal at a = sqrt(C);
    K2 is the kinetic term of M~^2 atilde atildedot^2 with atilde = C/a. OK.
Hubble-sphere and two-region readings: reproduced in num_check.py (above). Epoch dependence of the per-axis count
comparison: scripts/closeness.py -> outputs/closeness.txt (Step 4). Sections 8.2/8.4 normalisation:
scripts/c_consistency.py -> outputs/c_consistency.txt (Step 4).

## Step 4. Conceptual audit

### 4.1 MAJOR: the bimetric Yukawa strength (section 8.2) and its tension with section 8.4
- The manuscript writes alpha = (4/3)(M_f/M_g)^2 and cites Lueben et al. eq. 9 and Enander-Moertsell eq. 4.1. Both cited
  equations carry the background ratio c (fbar = c^2 gbar): alpha = (4/3)(M_f c/M_g)^2 (Lueben, with m_Pl^2 = m_g^2(1 + alpha^2
  c^2)) and alpha = 4c^2/3 (E-M). My mode decomposition gives the same: alpha = 4 M_f^2 c^2/(3 M_g^2)
  (scripts/derivations.py (g) -> outputs/derivations.txt). In Hassan-Rosen gravity only M_f c is invariant under f -> k^2 f,
  so "equal Planck masses" fixes alpha only once the normalisation of f (c = 1) is fixed. The note never states c.
- The program's own a . atilde = 1 makes the momentum frame's scale factor atilde = 1/a. If the f background tracks atilde,
  c = atilde/a. Section 8.4 places the self-dual point a = atilde = 1 at ~1e14 T_P (lambda = lP, today's observable
  universe), and that normalisation is what keeps its M~ = M_P a^-6 term harmless today. Then c0 = 1/A0 = 1.9e-93 and
  alpha = 4.9e-186: X's force is negligible and the torsion-balance bound does not apply. With c0 = 1 instead (a0 = atilde0 = 1)
  the M~ = M_P a^-6 term equals the GR term today and H/H_LCDM = 0.71 (z = 0), 0.12 (z = 1), 7.5e-10 (z = 1100)
  (scripts/c_consistency.py -> outputs/c_consistency.txt). So sections 8.2 and 8.4 need different normalisations of the
  same scale factors. The coupling may be fixed differently in [P1 section 7.5]/[P3 section 3] (unavailable to me), but
  as written the [D] "At equal Planck masses alpha = +4/3" is not established, and with it the note's one new number
  (lambda_X < 37.7 um, M_X c^2 > 5.2 meV) and "an X set by the self-dual length is excluded".
- Sensitivity (scripts/lee_interp.py): alpha = 1 (c^2 = 3/4) -> 40.7 um; c^2 = 0.5 -> 45.7 um; c^2 = 0.1 -> 80.7 um (then most
  of the 47-84 um self-dual range is no longer excluded).
- Related omitted constraint from the same source: Lueben et al. eqs. 16-19 show that with O(1) beta_n and m ~ H0, a spin-2 mass
  m_FP >> H0 requires M_f/M_g << 1 (weak coupling); equal Planck masses with M_X >~ 5 meV needs m ~ M_X and hence a bimetric
  vacuum energy ~ M_X^2 M_P^2 ~ 1e61 rho_Lambda to be tuned away. Lueben et al. also note the gradient instability of
  bimetric FLRW backgrounds for H > m_FP; for M_X = 5 meV that is T >~ TeV. Neither is mentioned.

### 4.2 Minor: "it holds at no other epoch" (section 4)
scripts/closeness.py -> outputs/closeness.txt. Today's ratio S^(1/3)/S_dS^(1/4) = 0.235 = 0.852 x (T0/rho_L^(1/4) = 0.105) x
(R/L_L = 2.63): the explanation via T0 ~ rho_L^(1/4)/10 omits the factor R/L_L. Under each reading of "another epoch":
(i) the fixed comoving region the note itself uses: 0.235 at every epoch since reheating (S conserved, S_dS constant);
(ii) radiation inside the particle horizon at epoch t: 0.18 (z = 1), 0.28 (a = 2), 0.32 as a -> infinity, i.e. it holds in the
whole future; (iii) Hubble sphere vs that sphere's horizon entropy: 0.83 throughout the radiation era, 0.58 at
recombination, 0.08 today, i.e. closer in the past than now. Reading (iii) is CKN's own eq. 3, S_max ~ S_BH^(3/4)
(radiation filling a Hubble volume in a radiation-dominated universe saturates it), which the note does not mention
although it cites CKN. The claim is false under every reading I could construct.

### 4.3 Tags, attribution, speculation
- [D] items actually derived: kappa identity, one-cell vs number-of-cells, no preferred lambda (transitivity of Sp(2d,R)
  on the Siegel domain), three loci, distance and clock, square epochs, Hubble and two-region readings, A(t), Lambda =
  3 lP^2/lambda^4, the c~ arithmetic, the a^-6 exchange symmetry: all re-derived (Step 3). Exception: alpha = 4/3 (4.1).
- Section 8.4: identifying a = sqrt(C) with "the 1e14 T_P of section 6" depends on which comoving scale is the unit cell
  (the note says so); it is a choice, and as 4.1 shows it conflicts with what 8.2 needs.
- Section 6 "At the turnaround": "V0[1 + cos(tau/f)] >= 0 ... produces no turnaround" holds for a spatially flat universe;
  with positive curvature a turnaround needs no negative energy. Flatness is unstated. Minor.
- [T] attributions: correct except the minor items in Step 1 (E&L Table 2 vs 1; Bhattacharyya et al. "clock"; Mignemi as a
  geometric-mean length; BHM's formula has no factor 3) and the c^2 misquotation (4.1).
- Speculation is labelled: section 6 "Where the claim probably came from [D, inference]" (and the record has no transcript),
  section 7 numerology explicitly disclaimed, section 8.5 [O]. Good.

### 4.4 The withdrawn claim, under every reading I could construct
Radiation rectangle of today's observable universe: square only at 4.4e14 T_P (2.5e14 with g_s), before reheating,
A >= 2.9e35 since reheating, A(T_P) = 6.4e28, so even a loop-quantum-cosmology bounce near T_P leaves it ~1e28
elongated. Hubble reading: A ~ 1 only near the Planck time (true also just after an LQC-type bounce, H_max ~ 0.9 t_P^-1),
and A -> infinity at any bounce or turnaround because H = 0 there. Two-region reading: different objects. |Z| = 1
reading: contradicts the measured aspect ratio. Program's turnaround (bounce of atilde): maximal elongation. A one-cell
reading with lambda = lP: a single photon's cell is square only when its wavelength ~ lP. The program's self-dual point
a = atilde (section 8.4): square by construction, but neither a nor atilde has an extremum there, so it is not a bounce, and it is
again at 1e14 T_P. A lambda other than lP: excluded by the chat's own "Planck units". The withdrawal holds under every
reading. The obituary's "What survives" is accurate.

### 4.5 Prior art for the [D] items (searched; INSPIRE records in downloads/inspire/)
- kappa identity: textbook blackbody statistics; the note says so. Area conservation: Liouville in FLRW (Ma-Bertschinger
  sec. 5.1; Tsagas et al. sec. 4.1, verified).
- Self-dual length sqrt(lP L_Lambda): FKGLM, BHM, Padmanabhan, CKN cited. Omitted: Bambi-Urban 2008 (already cited in
  section 5), whose extended-GUP symmetry Dx -> (alpha/beta)^(1/2) L_X L_Pl Dp with L_X = L_Lambda is rho_lambda with
  lambda^2 ~ L_Lambda L_Pl.
- Per-axis counts N^(1/3) vs N^(1/4): CKN eq. 3 / 't Hooft: S_max ~ S_BH^(3/4) (omitted; see 4.2).
- Gravity tests at the dark-energy length: Kapner et al., PRL 98, 021101 (2007), hep-ph/0611184 ("below the dark-energy
  length scale lambda_d ~ 85 um"); Sundrum, PRD 69, 044014 (2004), hep-th/0306106 (sub-mm "fat graviton" tied to Lambda).
  Omitted.
- Hubble-cutoff holographic dark energy: Hsu cited; Li, PLB 603, 1 (2004), hep-th/0403127 (event-horizon cutoff, the
  standard viable alternative) omitted.
- Maximal force: Low cited; Gibbons, Found. Phys. 32, 1891 (2002), hep-th/0210109 (maximum tension c^4/4G) and Caianiello's
  maximal acceleration omitted.
- The heavy-graviton bound itself is Lee et al.'s 5.1 meV (alpha = 1); the note's 5.2 meV is that bound redone at
  alpha = +4/3 with the one-sided column. The note says so.

(LQC aside in 4.4: scripts/misc_checks.py (5) -> outputs/misc_checks.txt: H_max = 0.93/t_P at rho_c/2, T = 0.28 T_P, A = 1.45;
A infinite at the bounce itself.)

## Step 5. Verdict

Verdict: B (flawed but salvageable). Confidence 0.75.

The arithmetic is clean: every number I recomputed agrees with the manuscript (Step 2). The identities re-derive
symbolically (Step 3). The literature is real, and quoted text matches its sources wherever I could read them (Step 1).
The withdrawal of "square exactly at the bounce" holds under every reading I could construct (4.4). The flaw sits in the
one result the note presents as new. The torsion-balance bound on X rests on alpha = 4/3 "at equal Planck masses". That
value drops the background-ratio factor c^2 that both cited sources carry, and the note's own section 8.4 normalisation
would make c ~ 1e-93 today (4.1). The rest is minor: one false side claim (4.2) and several citation and wording slips.

Weakest link: section 8.2, "At equal Planck masses alpha = +4/3". In Hassan-Rosen gravity the strength is
(4/3)(M_f c/M_g)^2. c is never fixed. With the section 8.4 normalisation (a = atilde at ~1e14 T_P) it is ~1/A0, and the
bound vanishes. With c = 1 (a = atilde today), the section 8.4 M~ = M_P a^-6 term equals the GR term today.
