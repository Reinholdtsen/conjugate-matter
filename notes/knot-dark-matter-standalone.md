# Dark Matter as Superheavy Monopoles of a Hidden Gauge Sector Selected by a Spontaneously Broken Phase-Space Duality

> **Withdrawn (2026-10-19) after failing round-3 review (verdict C). Kept as the audit trail; not for circulation.** The Kibble normalization in Sec. 3 is wrong: one monopole per Hubble volume is p ≈ 104, not 0.023, and it is the minimum, not the upper end. So the mass band, the benchmark's "no dilution required" and the ψ relic window are wrong. The soliton candidate is retired as a program-native proposal. The corrected numbers are in [review/round3-adjudication.md](../review/round3-adjudication.md), checked by `verify/soliton_obituary.py`.

*Anonymous working manuscript submitted for adversarial review. The manuscript may contain errors or confabulations; the reviewer is asked to find them.*

## Abstract

We propose that dark matter consists of superheavy 't Hooft-Polyakov monopoles of a hidden SU(2) gauge sector broken to U(1). The hidden sector is identified with the momentum-polarized half of a spontaneously broken Born reciprocity. The proposal makes one coupling hypothesis: the smallest hidden charge equals the electron's. Given that, the hidden sector's own Dirac quantization makes the monopoles' mutual magnetic coupling 1/(4 alpha) ~ 34. A Kibble-mechanism abundance then places the monopole mass at about 1e13 to 4e13 GeV with no dilution required. The candidate is stable by topology, dark by sector separation, effectively collisionless, and inaccessible to direct detection. Consistency forces two additions to the minimal hidden sector, stated here as requirements. First, a light hidden-charged fermion: without it, stable hidden W bosons overclose the universe by a factor of 1e16 to 1e17. Second, a hidden sector reheated to at most 0.77 of our temperature, from the dark-radiation bound. We give the derivations and the arithmetic, name the mechanisms most likely to invalidate the proposal, and list explicit acceptance criteria and exclusion conditions.

## 1. Framework

Quantum kinematics is invariant under the Born rotation rho: (x, p) -> (p, -x); the Fourier transform implements it unitarily [1]. We note at the outset a distinction the proposal must eventually discharge: as usually encountered, rho is a unitary equivalence between representations of the canonical commutation relations, not a Noether symmetry of a specified action. The framework's claim is that rho is a genuine symmetry of an underlying action, spontaneously broken; the emergent structure eta below is the proposed order parameter, and the exhibition of a toy action realizing this is stated in Sec. 6 as the proposal's first acceptance criterion. The breaking, if the symmetry exists, is compulsory in one respect: the uncertainty principle forbids states symmetric between the variables, so some polarization must be selected; which one is the spontaneous datum. Ours is position-polarized.

Geometric setting. Let phase space carry a rigid symplectic form omega and a dynamical positive generalized metric H (rigidity of omega encodes the constancy of hbar). Compatibility theorem (pointwise, in a flat frame; both directions verified numerically by machine): if a neutral metric eta is also held rigid, the conditions (eta^-1 H)^2 = 1 and (omega^-1 H)^2 = -1 force H = diag(g, g^-1) with g positive symmetric. Proof: writing H in blocks (A, C; C^T, B), the (2,1) blocks of the two conditions give A C^T + C A = 0 and C A - A C^T = 0, hence A C^T = 0; positivity gives C = 0; the diagonal blocks give B = A^-1. QED. Consequently the baseline momentum-space geometry is slaved (g-tilde = g^-1, det H = 1), and any independent momentum-space geometry resides in the fluctuation X of the off-vacuum modular parameter Z = X + iY on Sp(2d,R)/U(d), with eta emergent as the order parameter.

Mass of the second tensor. X is symmetric and its local shift symmetry delta X_mu-nu = partial_(mu lambda_nu) is a second copy of linearized diffeomorphisms; a massless X coupled to gravity is excluded by the multi-graviton no-go [2]. The polarization choice spontaneously breaks the dual diffeomorphisms; X absorbs the Goldstones and acquires mass M_X (gravitational Higgs), with the consistent nonlinear structure taken to be of ghost-free bimetric type [3]. This renders the second geometry short-ranged and unobserved. That the symmetry-breaking sector lands on the ghost-free potential is argued from a first-order (vielbein) formulation and is a structural claim, not a line-by-line derivation. Cosmological stability is a further, open check. The published analyses of bimetric cosmological branches find gradient or ghost instabilities, but they assume a spin-2 mass of order the present Hubble rate and comparable Planck masses for the two metrics [4]. A heavy spin-2 field has been shown to be linearly stable at late times in the regime where the second metric's Planck mass is much smaller than the first [5]. The framework's reciprocity, acting as exchange of the two metrics, instead sets the two Planck masses equal, so the stability of a heavy spin-2 field at equal Planck masses is an open consistency condition (Sec. 5, item 7). The Higuchi bound m^2 >= 2H^2 [6] is satisfied trivially by the heavy field.

Kinematics. Throughout, the hidden sector is described by ordinary relativistic quantum field theory. Whether the parent framework requires a different kinematics for momentum-polarized matter is an open question that this proposal does not use.

## 2. The hidden sector and its coupling

Motivation. The Dirac-Schwinger-Zwanziger pairing <q, q'> = e1 g2 - e2 g1 in 2 pi Z equips the electric-magnetic charge lattice with an antisymmetric integer form: charge space is symplectic [7]. Mutual locality - the condition for a set of charges to admit a common Lagrangian description - is <q, q'> = 0: a Lagrangian sublattice. Choosing a duality frame (which states are "electric," fundamental and weakly coupled, versus "magnetic," solitonic and strongly coupled) is therefore choosing a Lagrangian polarization of charge space, formally the same operation as choosing a Lagrangian polarization of phase space; the S generator of electric-magnetic duality and the Born rotation are represented by the same matrix. We use this only as motivation: it suggests that the vacuum event that polarizes phase space also fixes which description of a gauge sector is the electric one. No numerical result below depends on it.

The sector (postulated). The momentum-polarized matter sector contains a gauge group SU(2)_d with a real adjoint scalar Phi whose expectation value v breaks it to U(1)_d. U(1)_d stays unbroken, so the hidden photon is massless. The charged vectors W'+- have mass g_d v. The sector also contains at least one Dirac fermion psi in the doublet, with U(1)_d charges +-g_d/2 (Sec. 3 shows it is required). An exact mirror copy of the Standard Model cannot serve: the electroweak vacuum manifold is S^3, whose pi_2 vanishes, so it has no stable monopoles. The hidden gauge structure must therefore differ from ours.

Coupling. The hidden sector is weakly coupled in its electric description, with alpha_W' = g_d^2/4pi. Its monopoles carry magnetic charge g_m = 4 pi/g_d, the Dirac minimum relative to psi's charge g_d/2, so their mutual coupling is alpha_m = g_m^2/4pi = 1/alpha_W' [7]. Any weakly coupled hidden sector therefore has strongly coupled monopoles: the strong magnetic coupling is generic, not a hypothesis.

The proposal's single coupling hypothesis (H): the smallest hidden charge equals ours, (g_d/2)^2/4pi = alpha. The motivation is that reciprocity exchanges the two polarizations; if it acts on gauge couplings at all, the minimal action is to equate the elementary charges of the two sectors. Under H, alpha_W' = 4 alpha ~ 1/34 and alpha_m = 1/(4 alpha) ~ 34. Two conventions move this number. Matching the W' charge to ours instead of psi's gives alpha_m ~ 137. Matching at 1e12 GeV instead of at low energy gives about 29, from one-loop Standard Model running of alpha. Without H, alpha_W' is a free weak coupling and alpha_m = 1/alpha_W' is free but necessarily strong; H only selects a point.

What is not asserted. These objects carry no charge under our photon. The Dirac quantization used above is the hidden sector's own, applied to its own charges; nothing is quantized against our gauge field. Exact electric-magnetic duality is also not assumed. It has been tested non-trivially only in N=4 super-Yang-Mills and certain finite N=2 theories, and there is no reason to expect it to survive quantum corrections in a non-supersymmetric theory [8]. Nothing here requires it: the monopole physics used is semiclassical, at alpha_W' ~ 1/34.

Sector separation (postulated). No field carries charge under both U(1)_d and our hypercharge. The status of kinetic mixing epsilon between the two field strengths is then as follows.

- (a) Pure gravity. Kinetic mixing vanishes to all perturbative orders if hidden charge conjugation is an exact symmetry. If it is broken, gravity can induce mixing, but only at six loops or more, giving epsilon <~ 1e-13 [9].
- (b) A dimension-5 operator. Phi^a F^a_mu-nu B^mu-nu / M_* is gauge invariant and gives epsilon ~ v/M_* once Phi condenses [10]. For an O(1) coefficient at the Planck or reduced Planck scale, epsilon ~ 1e-7 to 1e-6. The operator is odd under Phi -> -Phi, so a discrete symmetry acting as hidden charge conjugation forbids it - but only if that symmetry is gauged, since quantum gravity is believed to admit no exact global symmetries [11].
- (c) Consequence. With U(1)_d unbroken, kinetic mixing does not give the monopoles magnetic charge under our photon: the hidden monopole induces no visible magnetic flux even with epsilon nonzero [12, 10]. Minicharged monopoles would require a massive hidden photon [13], which this proposal excludes. The visible-sector leakage is instead (i) psi acquires visible electric charge ~ epsilon e, and (ii) with CP violation the monopoles acquire a small visible electric charge [14]. The decisive constraints therefore act on psi, not on the dark matter itself (Sec. 4).

## 3. The candidate

The monopoles. SU(2)_d -> U(1)_d has pi_2(SU(2)/U(1)) = pi_2(S^2) = Z and supports 't Hooft-Polyakov monopoles [15], stable by topological charge. Their mass is M = 4 pi f v/g_d. The factor f is 1 in the BPS limit [16] and rises to about 1.79 at large scalar self-coupling. Under H this gives M ~ (21-37) v.

A negative result: the minimal model fails. With only the adjoint scalar, the W'+- are the lightest hidden-charged states and are stable by U(1)_d charge. Kibble production (below) requires a hidden plasma at temperature ~ v, so the W' are thermally populated and freeze out. At the benchmark mass below, m_W' ~ (5-9)e11 GeV. Standard freeze-out [17] then leaves them at 1e16 to 1e17 times the observed dark-matter density, bracketing the annihilation coefficient over a factor of ten. The adjoint-only sector is excluded.

The fix is the Dirac doublet psi: W'+ can decay to a psi pair. psi is then itself stable by U(1)_d charge and freezes out by annihilating to hidden photons. Under H, psi makes up less than 10% of the dark matter for m_psi below 0.1-0.3 TeV, and all of it at 0.3-1 TeV. We take m_psi below about 0.1 TeV, so that the monopoles dominate, and above the MeV scale, so that psi has annihilated before nucleosynthesis. The psi plasma is also the medium through which monopole-antimonopole annihilation proceeds (below).

Abundance. The Kibble mechanism [18] at a post-inflationary transition with T_c ~ v yields n/s ~ p (v/M_Pl)^3. One monopole per horizon volume with g* = 100 gives p ~ 0.023; we take p = 1 as the upper end. We require Omega h^2 ~ 0.12, with mean rho_DM = 1.26 keV/cm^3, s_0 ~ 2.9e3 /cm^3 and M_Pl = 1.22e19 GeV, and M = (21-37) v. This gives a Kibble-consistent mass M* ~ (0.9-3.7)e13 GeV; the reduced-Planck convention lowers it by a factor of about 3. We adopt the benchmark M = 3e13 GeV, which corresponds to v ~ (0.8-1.4)e12 GeV.

This is a point, not a window. Heavier monopoles are over-produced as (M/M*)^4 and need that much entropy dilution - about 1e10 at M = 1e16 GeV. Lighter monopoles are under-produced.

The classic relic analysis [19] found monopole-antimonopole annihilation inefficient for superheavy monopoles in our plasma. Here annihilation runs through the hidden plasma (psi and hidden photons) at alpha_m ~ 34, where Sommerfeld enhancement and rapid bound-state formation may matter. Whether the Kibble abundance survives requires a dedicated strong-coupling freeze-out calculation in that plasma, not performed here (acceptance criterion 3). Inflation must precede the hidden transition, and v must lie below the reheating temperature.

Benchmark numbers (M = 3e13 GeV). The mean number density is n ~ 4.2e-20 /cm^3. At the local halo density (0.4 GeV/cm^3) there is one monopole per ~0.075 km^3, a mean spacing of about 420 m, drifting at ~1e-3 c.

## 4. Observational consistency

Not monopoles of our U(1). If these objects carried magnetic charge under our electromagnetism, they would be classic monopoles and excluded. The flux at dark-matter density would be F = n v/4 pi ~ 3e-8 /cm^2/s/sr. That exceeds the Parker bound (~1e-15 for M <~ 1e17 GeV) [20] by 7.5 orders of magnitude, the MACRO limit for m >~ 1e10 GeV (2.8e-16) [21] by eight, and the extended Parker bound 1e-16 (M/1e17 GeV) [22] by twelve. Sector separation is therefore mandatory. Sec. 2(c) shows it is not undone by kinetic mixing while U(1)_d is unbroken.

Millicharged hidden fermions. If hidden charge conjugation is not a gauged symmetry, psi carries visible electric charge ~ epsilon e, with epsilon ~ 1e-7 to 1e-6. Its mass lies between the MeV scale and ~0.1 TeV, and it is a subdominant relic. Bounds on millicharged particles in this mass and charge range have not been evaluated here. They are the most direct near-term test of the proposal (exclusion condition 3).

Dark radiation. The hidden photon is radiation. Suppose the two sectors shared a temperature above v. The hidden sector - the SU(2)_d gauge fields, the adjoint scalar and one psi doublet - then contributes Delta N_eff ~ 0.86 after its heavy states disappear. That is excluded by Planck 2018 (N_eff = 2.99 +- 0.34 at 95%) [23]. The proposal therefore requires the hidden sector to have been reheated to xi < 0.77 of our temperature, an assumption about reheating that the framework does not fix. A colder hidden sector lowers M* by xi^(3/4), a factor of 0.8 at the bound - smaller than the factor-of-four spread already in the band above.

Self-interaction. Monopole-monopole scattering through the hidden photon is Rutherford-like at alpha_m ~ 34 but suppressed by the mass: sigma_T/M ~ 8 pi alpha_m^2 ln(Lambda)/((M/2)^2 M v^4) ~ 1e-26 cm^2/g at v ~ 1e-3 c and M = 3e13 GeV, for ln(Lambda) = 10-30. That is some twenty-six orders below astrophysical sensitivity. The candidate is effectively collisionless cold dark matter, so observed dwarf-galaxy cores must be attributed to baryonic feedback.

Phase-transition signatures. If the hidden transition is first order, it sources a stochastic gravitational-wave background with a present-day peak frequency of ~1e5 to 1e7 Hz for f*/H* = 1-100. That is above the LIGO band, in the unconstrained ultra-high-frequency window targeted by proposed detectors. The amplitude is suppressed by the hidden sector's share of the energy density at the transition, which is small for xi < 0.77. A crossover transition leaves no such signal. The parent framework's cosmological sector separately predicts thawing, never-phantom dark energy, currently consistent with hints of weakening dark energy in recent baryon-acoustic-oscillation data.

## 5. Exclusion conditions

1. Any confirmed non-gravitational coupling between the dominant dark-matter component and the Standard Model.
2. Any confirmed magnetic-monopole flux of our U(1) at dark-matter abundance.
3. Exclusion of the millicharged psi window: m_psi from the MeV scale to ~0.1 TeV at visible charge ~ (1e-7 to 1e-6) e. This lapses if hidden charge conjugation is shown to be a gauged symmetry, which sets epsilon = 0.
4. A strong-coupling relic calculation showing that monopole annihilation in the hidden plasma at alpha_m ~ 34 cannot leave the observed abundance.
5. Demonstration that dwarf cores require dark-sector self-interaction (this candidate cannot supply it).
6. Robust dark-energy measurement of constant w = -1 or intrinsic w < -1 (kills the parent framework's cosmological sector).
7. Internal: failure of the ghost-free landing of Sec. 1; instability of a heavy spin-2 field at equal Planck masses; or proof that no hidden sector with SU(2)_d, an adjoint scalar and a doublet fermion is consistent with the polarization structure.

## 6. Status of claims and acceptance criteria

All numerical statements in Secs. 2-4 were computed by executed code rather than by hand.

Derived within the framework or by standard methods:

- the compatibility theorem (elementary; machine-verified numerically in both directions);
- the symplectic structure of the charge lattice (standard mathematics [7]);
- the relation alpha_m = 1/alpha_W' and its consequence that weakly coupled hidden sectors have strongly coupled monopoles (standard);
- the failure of the adjoint-only model and the psi relic window;
- the Kibble-consistent mass;
- the dark-radiation requirement;
- the counterfactual flux numbers and cross-section of Sec. 4.

Established results used: [1]-[23].

Conjectural:

- that rho is a genuine, spontaneously broken symmetry;
- hypothesis H;
- the identification of the SU(2)_d sector as the momentum-polarized matter sector;
- sector separation, and either its ultraviolet stability or a gauged hidden charge conjugation;
- the ghost-free landing of the mass mechanism and its cosmological stability at equal Planck masses;
- the colder reheating of the hidden sector.

Requirements forced by consistency (not optional):

- (i) at least one hidden doublet fermion with mass between the MeV scale and ~0.1 TeV;
- (ii) a hidden-to-visible temperature ratio xi < 0.77 after reheating;
- (iii) an unbroken U(1)_d.

Acceptance criteria, stated so that failure is checkable:

- (1) exhibition of an action - a toy model suffices - in which rho is a genuine Noether symmetry, spontaneously broken, with eta the order parameter selecting both the position polarization and the hidden sector's electric description; deriving hypothesis H from that action would make the coupling a prediction;
- (2) either a gauged hidden charge conjugation, or a demonstration that the millicharged psi window survives existing constraints;
- (3) the strong-coupling relic freeze-out calculation of Sec. 3, in the hidden plasma.

The manuscript's claim is not that the proposal is true, but that it is a self-consistent, maximally symmetric assignment of dark matter's identity whose failure modes are stated. The reviewer is asked to test that claim adversarially.

## References

[1] M. Born, Proc. R. Soc. Lond. A 165, 291 (1938); Rev. Mod. Phys. 21, 463 (1949).
[2] N. Boulanger, T. Damour, L. Gualtieri, M. Henneaux, Nucl. Phys. B 597, 127 (2001), hep-th/0007220.
[3] S. F. Hassan, R. A. Rosen, Phys. Rev. Lett. 108, 041101 (2012), arXiv:1106.3344; JHEP 02 (2012) 126, arXiv:1109.3515.
[4] D. Comelli, M. Crisostomi, L. Pilo, JHEP 06 (2012) 085, arXiv:1202.1986; F. Könnig, Y. Akrami, L. Amendola, M. Motta, A. R. Solomon, Phys. Rev. D 90, 124014 (2014), arXiv:1407.4331; M. Lagos, P. G. Ferreira, JCAP 12 (2014) 026, arXiv:1410.0207.
[5] Y. Akrami, S. F. Hassan, F. Könnig, A. Schmidt-May, A. R. Solomon, Phys. Lett. B 748, 37 (2015), arXiv:1503.07521.
[6] A. Higuchi, Nucl. Phys. B 282, 397 (1987).
[7] P. A. M. Dirac, Proc. R. Soc. Lond. A 133, 60 (1931); D. Zwanziger, Phys. Rev. 176, 1489 (1968).
[8] C. Montonen, D. Olive, Phys. Lett. B 72, 117 (1977); H. Osborn, Phys. Lett. B 83, 321 (1979); J. A. Harvey, "Magnetic monopoles, duality and supersymmetry," hep-th/9603086.
[9] T. Gherghetta, J. Kersten, K. Olive, M. Pospelov, Phys. Rev. D 100, 095001 (2019), arXiv:1909.00696.
[10] M. Baumgart, C. Cheung, J. T. Ruderman, L.-T. Wang, I. Yavin, JHEP 04 (2009) 014, arXiv:0901.0283; F. Chen, J. M. Cline, A. R. Frey, Phys. Rev. D 80, 083516 (2009), arXiv:0907.4746; F. Brümmer, J. Jaeckel, Phys. Lett. B 675, 360 (2009), arXiv:0902.3615.
[11] T. Banks, N. Seiberg, Phys. Rev. D 83, 084019 (2011), arXiv:1011.5120; D. Harlow, H. Ooguri, Commun. Math. Phys. 383, 1669 (2021), arXiv:1810.05338.
[12] T. Hiramatsu, M. Ibe, M. Suzuki, S. Yamaguchi, JHEP 12 (2021) 122, arXiv:2109.12771.
[13] J. Terning, C. B. Verhaaren, JHEP 12 (2018) 123, arXiv:1808.09459.
[14] F. Brümmer, J. Jaeckel, V. V. Khoze, JHEP 06 (2009) 037, arXiv:0905.0633.
[15] G. 't Hooft, Nucl. Phys. B 79, 276 (1974); A. M. Polyakov, JETP Lett. 20, 194 (1974).
[16] M. K. Prasad, C. M. Sommerfield, Phys. Rev. Lett. 35, 760 (1975); E. B. Bogomolny, Sov. J. Nucl. Phys. 24, 449 (1976).
[17] E. W. Kolb, M. S. Turner, The Early Universe (Addison-Wesley, 1990).
[18] T. W. B. Kibble, J. Phys. A 9, 1387 (1976).
[19] J. Preskill, Phys. Rev. Lett. 43, 1365 (1979).
[20] Particle Data Group, Review of Particle Physics (2024), "Magnetic Monopoles" review (D. Milstead, E. J. Weinberg); M. S. Turner, E. N. Parker, T. J. Bogdan, Phys. Rev. D 26, 1296 (1982); E. N. Parker, Astrophys. J. 160, 383 (1970).
[21] MACRO Collaboration (M. Ambrosio et al.), Eur. Phys. J. C 25, 511 (2002), hep-ex/0207020.
[22] F. C. Adams, M. Fatuzzo, K. Freese, G. Tarlé, R. Watkins, M. S. Turner, Phys. Rev. Lett. 70, 2511 (1993).
[23] Planck Collaboration, Astron. Astrophys. 641, A6 (2020), arXiv:1807.06209.
