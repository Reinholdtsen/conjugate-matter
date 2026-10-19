# v3 of #14 — worklog

Cutting v3 of [papers/knot-dark-matter-standalone.md](../papers/knot-dark-matter-standalone.md)
from the round-2 pending list (HANDOFF §6). State is saved here after each
chunk so any session can resume cold.

Evidence used so far:

- HANDOFF §6 summary of round 2. The round-2 referee report itself is not in
  the repo. Paul holds it.
- [verify/knot_numbers.py](../verify/knot_numbers.py): every number v2 quotes,
  recomputed. All reproduce (gated in `scripts/check.sh`). NOTE lines are
  adjudication inputs not yet quoted by the manuscript.
- Literature report, 2026-10-19: a subagent with web access pulled each
  record from INSPIRE, arXiv, the PDG 2024 monopole review and the scanned
  Preskill 1979 paper, with no citations from memory. Summarized per item
  below.
  - I spot-checked the load-bearing claim (L1) against the Hiramatsu et al.
    abstract myself.
  - Not re-checked: Adams et al. 1993 full text (paywalled; abstract only);
    Terning–Verhaaren body text.

## Round-2 pending list

| # | Item | Status | Evidence / decision |
|---|------|--------|---------------------|
| R1 | SUSY-exactness burden for Montonen–Olive | **ready** | Exact S-duality has been tested only in N=4 SYM and special finite N=2 theories. For non-SUSY theories there is "no reason to think" it survives quantum corrections, and the bosonic spectrum mismatches (W spin 1, monopole spin 0). That is an expectation, not a no-go [Harvey hep-th/9603086; Osborn 1979]. v3 must state it. If F2 is adopted, S no longer carries α_d, and the burden shrinks to the §2 "full mirror spectrum" remark. |
| R2 | Coupling convention and running spread | **adjudicated** [V] | Convention: 1/(4α) = 34.26 (eg = 2πn) vs 1/α = 137.04 (eg = 4πn). One-loop SM running of α_em gives 1/(4α_em) = 29.0 at 10¹¹, 28.8 at 3×10¹¹ and 27.3 at 10¹⁶ GeV. The referee's "toward ~6–8" is **not reproduced** for the electromagnetic coupling; 6–8 appears only for 1/(4α₃). The valid core stands: the number is convention-dependent by a factor of 4. v3: present α_d as free-but-strong. |
| R3 | Extended Parker bound | **ready** (counterfactual only, see L1) | Adams, Fatuzzo, Freese, Tarlé, Watkins, Turner, PRL 70, 2511 (1993). Abstract: ℱ ≤ 10⁻¹⁶ (m/10¹⁷ GeV) cm⁻² s⁻¹ sr⁻¹. Others quote a 1.2×10⁻¹⁶ prefactor, and PDG 2024 Eq. 95.10 adds a low-mass floor. Excess at the 10¹⁶ benchmark: 6.98 orders [V]. Charge scaling: (g/g_D)⁻² at high mass, (g/g_D)⁻¹ at low mass [Kobayashi–Perri 2023, arXiv:2307.07553]. |
| R4 | Gravity-induced kinetic mixing | **ready**; the question changes, see L1 | Pure gravity: ε = 0 if dark charge conjugation C is exact. Otherwise it needs at least 6 loops and gives ≲10⁻¹³ [Gherghetta–Kersten–Olive–Pospelov, PRD 100, 095001 (2019)]. The referee is right that it exists, and it is negligible. The dimension-5 adjoint operator is in the literature [Baumgart et al. 2009 fn.; Chen–Cline–Frey 2009; Brümmer–Jaeckel 2009, χ = v/M]. Our estimate: ε ≈ 2.4×10⁻⁸ at M = M_Pl [V]. Quantum gravity forbids an exact global C [Banks–Seiberg 2011; Harlow–Ooguri 2021]; a gauged C (O(2)/O(3)-type) remains a loophole [Obied–Parikh, preprint]. v3: replace "forbidden to all orders" with "absent if dark C is a gauged symmetry; otherwise ε ~ ⟨Φ⟩/M (≈ 10⁻⁸–10⁻⁷) from dimension 5 and ≲ 10⁻¹³ from pure gravity". |
| R5 | Entropy-dilution caveat | **adjudicated** [V], stronger than the referee said | See F1. |
| R6 | Name an explicit candidate group | **ready** | SU(2) → U(1) by an adjoint Higgs; π₂(SU(2)/U(1)) = ℤ ['t Hooft 1974; Polyakov 1974]. Hiramatsu et al. (JHEP 12 (2021) 122) study exactly this case with kinetic mixing. |
| R7 | Bimetric cosmological-branch instability | **ready, with a tension** | The instability analyses assume a spin-2 mass m ~ H₀ and M_f ~ M_g [Comelli–Crisostomi–Pilo, JHEP 06 (2012) 085; Könnig et al., PRD 90, 124014 (2014); Lagos–Ferreira, JCAP 12 (2014) 026]. A heavy spin-2 is linearly stable at late times [Akrami–Hassan–Könnig–Schmidt-May–Solomon, PLB 748, 37 (2015)]. Three limits on that: their viable regime takes **M_f ≪ M_g**; it holds at linear order only, with tuned βₙ; and the strong-coupling era H > H⋆ is unresolved. Higuchi bound m² ≥ 2H² [Higuchi, NPB 282, 397 (1987)]: trivially satisfied by a heavy X. **Tension:** [notes/debt1a-iv §3](../notes/debt1a-iv-beta-coefficients.md) says reciprocity forces equal effective Planck masses (M_f = M_g), which rules out the M_f ≪ M_g escape. Whether a large mass alone is enough at M_f = M_g is open (De Felice et al. 2014, cited in Akrami et al.: "the instability becomes negligible for large values of m"; not yet read). v3: state this as an open consistency item, not as evaded. |

## Findings neither referee raised

- **F1 — the mass window is not "Kibble-only"** [V]. Kibble with p = 1 closes
  at a single point, M* ≈ 3.0×10¹³ GeV. Below it, solitons are
  under-produced (×0.013 at 10¹³). Above it, the abundance scales as
  (M/M*)⁴, so the observed density needs entropy dilution of 1.3×10⁶ at
  10¹⁵, **1.3×10¹⁰ at the 10¹⁶ benchmark**, and 1.3×10¹⁴ at 10¹⁷.
  - The horizon-counting p is ≈ 0.023, which moves M* to ≈ 7.7×10¹³. Same
    conclusion.
  - Preskill (verified from the scan): annihilation cannot reduce n/T³ below
    ~10⁻¹⁰ at m ≈ 10¹⁶ GeV. For a hidden sector the rate runs through the
    dark plasma, so it has to be recomputed (acceptance criterion 3), not
    carried over.
  - **Decided (Paul, 2026-10-19):** move the benchmark to M ≈ 3×10¹³, and
    keep 10¹⁶ with its ~10¹⁰ dilution as a stated alternative. At 3×10¹³, the
    counterfactual MACRO limit is ≤ 2.8×10⁻¹⁶ (m ≳ 10¹⁰ GeV row), not
    1.4×10⁻¹⁶ (m ≳ 10¹⁶ GeV row).
- **F2 — which coupling sets the soliton mass** [D, numbers V]. v2 writes
  M ~ (4π/e_d²) Λ_c ~ 100 Λ_c. That factor is ~137 only if e_d²/4π ≈ 1/137.
  With e_d²/4π = α_d = 34 it is 0.029, so the solitons would not be heavy.
  v2 uses the weak value in §3 and the strong value in §2 and §4.
  - The self-consistent reading: the dual sector's elementary coupling α_e,d
    is weak, its solitons are heavy (M ≈ Λ_c/α_e,d), and the solitons
    themselves are strongly coupled (α_m ≈ 1/(4α_e,d) or 1/α_e,d).
  - Then α_d ≈ 34 follows from α_e,d ≈ α, a mirror-coupling equality, and
    does not need S acting on our coupling.
  - **Decided (Paul, 2026-10-19):** adopt this reading. v3 §2 is reframed:
    the load-bearing conjecture becomes α_e,d = α (or α_e,d free and weak),
    and S-duality is no longer what fixes α_d.
- **L1 — mixing does not give the monopoles a visible charge** (from the
  literature). With an unbroken dual U(1), i.e. a massless dark photon, which
  is v2's setup, kinetic mixing gives the dark monopole **no QED magnetic
  flux**.
  - Hiramatsu–Ibe–Suzuki–Yamaguchi, arXiv:2109.12771, abstract, checked:
    "does not induce the QED magnetic flux in the U(1) symmetric phase, even
    in the presence of the kinetic mixing". Also Brümmer–Jaeckel 2009.
  - Minicharged, confined monopoles need a *massive* dark photon
    [Terning–Verhaaren, JHEP 12 (2018) 123; Graesser et al., JHEP 03 (2022) 105].
  - So v2's premise "mixing ε gives the solitons magnetic charge εg under our
    photon" is wrong for its own setup. Four places rest on it: §2's "It is
    not decorative" paragraph, §4's last sentence of the first paragraph,
    §5 exclusion 3, and §6 acceptance criterion (2).
  - The real leakage channels:
    - dark *electric* states (W′±) pick up a millicharge εe [Brümmer–Jaeckel];
    - CP violation gives the monopoles a small visible *electric* charge
      ("magnetic mixing", Brümmer–Jaeckel–Khoze, JHEP 06 (2009) 037);
    - a massive dark photon would make minicharged monopoles.
  - Net effect: the candidate survives mixing more easily than v2 says, and
    the constraint moves to the dark W′±, which ties into F2's open items.
  - Parker and MACRO stay in v3 only as the reason sector separation is
    needed: they show what would happen if these objects were monopoles of
    our U(1).

## New open items (to compute before v3 states anything about them)

- **O1 — dark W′± fate: fatal to the minimal model, not to the candidate**
  [computed in [verify/knot_numbers.py](../verify/knot_numbers.py); `dark_sector.py` was merged into it]. The script
  checks its freeze-out formula on a standard relic first: 100 GeV with
  σv = 2.2×10⁻²⁶ cm³/s gives Ω h² = 0.108.
  - Minimal model: SU(2)_d → U(1)_d with only the adjoint Higgs.
    - Under F1 and F2, m_W′ = α M*/f = 1.2–2.2×10¹¹ GeV.
    - W′± is the lightest dark-charged state, so it is stable.
    - Its thermal relic is **0.8–15×10¹⁶ × the observed density**, bracketing
      the annihilation coefficient κ = 1–10 and f = 1–1.787.
    - Kibble production needs a hot dark plasma at T ~ Λ_c, so the W′± were
      thermal. The minimal model is excluded.
  - The fix: at least one light dark-charged fermion (a dark doublet) for W′±
    to decay into.
    - That fermion is itself a thermal relic. With α_e,d = α it would be all
      of the dark matter at 0.3–1.0 TeV, and 10% of it at 0.1–0.3 TeV.
    - So it must be lighter than roughly 100–300 GeV to stay subdominant.
      Otherwise the minimal consistent dark sector contains a second
      dark-matter candidate besides the monopoles.
  - Consequences for v3:
    - R6 becomes "SU(2)_d → U(1)_d with at least one light dark doublet".
    - The light dark fermions carry millicharge εe unless dark C is gauged
      (R4, L1). Their constraint at ε ~ 10⁻⁸–10⁻⁷ is not yet checked [O].
    - Their plasma is what runs Preskill-type monopole annihilation in the
      dark sector, which feeds acceptance criterion 3.
    - If they are lighter than ~MeV they add ΔN_eff at BBN as well (not yet
      scripted).
  - Computed at ξ = 1 only. The effect of a colder dark sector on the W′
    freeze-out is not scripted.
- **O2 — dark radiation: not fatal; it needs a cooler dark sector**
  [NOTE-tier]. The script checks its formula first: one extra neutrino
  species at T_ν gives ΔN_eff = 1.000.
  - Setup: the two sectors at temperature ratio ξ at high T, then separately
    entropy-conserving, ending with only the dark photon relativistic.
  - Results:

    | Dark sector content | ΔN_eff at ξ = 1 | ξ needed for ΔN_eff < 0.3 |
    |---|---|---|
    | Minimal | 0.40 | < 0.93 |
    | One light doublet | 0.86 | < 0.77 |
    | Two light doublets | 1.39 | < 0.68 |

  - The 0.3 bound is an approximate Planck 2018 value, from memory †.
  - v3 requirement: the dark sector reheated ~25–30% colder than ours. ξ is
    a free parameter of the framework. A colder dark sector also moves the
    Kibble point M* by ξ^(3/4) (×0.82 at ξ = 0.77), which is minor.
- **O3 — the dark sector in dual kinematics.** #14 describes the dark sector
  entirely in our kinematics: GeV masses, 10⁻³ c drift, an ordinary massless
  dark photon moving at c. #13 §4 labels conjugate quanta by an invariant
  length λ instead of a mass, and a λ = 0 quantum would sit on the dual null
  cone with |dp/dt| = c̃. The papers were never reconciled.
  - #13 also has two different dual cones. §1 uses the 3+1 version (shared
    time): the cone lives in (t, p) with slope c̃. §6 says "our massless
    dispersion E = c|p| *is* the dual null cone", which belongs to the 4D
    Born map (t ↔ E): a cone in (E, p) with slope c. Under the 4D map,
    anything on our light cone is automatically dual-null.
  - Whether the dark photon is m = 0, λ = 0, or both is part of #13's open
    "dual dynamics" item.
  - v3 decision: keep the dark sector in ordinary kinematics and say so
    explicitly. L1 and O2 both rest on that.
  - Before any paper claims more: fix #13's two cones and settle which
    construction governs (raised by Paul, 2026-10-19).

## Verified references for v3

All checked against INSPIRE/arXiv/PDG by the literature report unless noted.
v2's [1]–[10] are all correct as cited. Corrections:

- Kibble's title is "Topology of Cosmic Domains and Strings".
- For the 10⁻¹⁵ Parker value, cite PDG 2024 or Turner–Parker–Bogdan, PRD 26,
  1296 (1982), not Parker 1970 alone. That value holds for M ≲ 10¹⁷ GeV.
- Harvey's lectures are conference proceedings, not a journal article.

New references for v3:

- Adams et al., PRL 70, 2511 (1993).
- Kobayashi–Perri, PRD 108, 083005 (2023), arXiv:2307.07553.
- Gherghetta–Kersten–Olive–Pospelov, PRD 100, 095001 (2019), arXiv:1909.00696.
- Hiramatsu et al., arXiv:2109.12771.
- Brümmer–Jaeckel, PLB 675, 360 (2009), arXiv:0902.3615.
- Brümmer–Jaeckel–Khoze, arXiv:0905.0633.
- Terning–Verhaaren, arXiv:1808.09459.
- Harvey, hep-th/9603086.
- Akrami et al., arXiv:1503.07521.
- Higuchi, NPB 282, 397 (1987).
- Banks–Seiberg, arXiv:1011.5120.

## Next chunks

1. ~~Paul's call on F1 and F2~~ — done 2026-10-19 (both accepted).
2. ~~Script O1 and O2~~ — done: the minimal model is dead; the fix is a
   light dark doublet plus ξ ≲ 0.77.
3. ~~Draft v3~~ — done 2026-10-19 (see "v3 as drafted" below).
   `verify/knot_numbers.py` now checks every number v3 quotes, and the v2
   checks are retired (still in history at d15cd4a).
4. Pre-register the expected verdict and weakest link, then run the round-3
   audit on v3 (HANDOFF §8 item 2).

## v3 as drafted (2026-10-19)

[papers/knot-dark-matter-standalone.md](../papers/knot-dark-matter-standalone.md)
now holds v3; v2 is in git history. Every number it quotes is a gated check
in `verify/knot_numbers.py`. Two planned figures were corrected by that
check before the text was written: the coupling matched at 10¹² GeV is
≈ 29 (not 28), and the minimal model overcloses by 10¹⁶–10¹⁷ (not
10¹⁵–10¹⁷).

Where drafting refined the plan above:

- **Which charge hypothesis H matches.** The light doublet (O1) makes ψ's
  charge g_d/2 the smallest dark charge. H matches *that* charge to ours, so
  α_W′ = 4α ≈ 1/34 and the monopoles' coupling is α_m = 1/α_W′ = 1/(4α) ≈ 34
  exactly, by Dirac quantization relative to ψ. Matching the W′ charge
  instead gives 137; matching at 10¹² GeV gives ≈ 29. This is F2 made
  precise.
- **The mass relation.** v2's "M ~ 100 Λ_c" is replaced by
  M = 4π f v/g_d ≈ (21–37) v [f: Prasad–Sommerfield, Bogomolny, verified on
  INSPIRE]. The Kibble-consistent band becomes M* ≈ (0.9–3.7)×10¹³ GeV over
  f and p. The F1 benchmark of 3×10¹³ sits inside it, with
  v ≈ (0.8–1.4)×10¹² and m_W′ ≈ (5–9)×10¹¹ GeV.
- **Benchmark numbers** move with it. One soliton per 0.075 km³ locally;
  σ_T/M ~ 10⁻²⁶ cm²/g; GW peak 10⁵–10⁷ Hz; the counterfactual flux exceeds
  Parker by 7.5 orders, MACRO (2.8×10⁻¹⁶) by 8 and extended Parker by 12.
- **The mirror-SM tension.** An exact mirror copy of the SM has no stable
  monopoles (π₂(S³) = 0), so H relates couplings only, not gauge groups.
  v3 says so in §2.
- **Requirements section.** v3 §6 lists three conditions forced by
  consistency: a light doublet (MeV to ~0.1 TeV), ξ < 0.77, and an unbroken
  U(1)_d.
- **Exclusion conditions.** v2's ε·g condition is replaced by the
  millicharged ψ window (item 3). The bimetric instability at equal Planck
  masses is added to item 7.

Not live-checked in v3's reference list: Kolb & Turner, *The Early Universe*
(a textbook, cited for the freeze-out formula); the JHEP reference for
Hiramatsu et al., which was taken from its DOI. Round 3 should confirm both.

[review/skeptic-review-console.html](skeptic-review-console.html) embeds v2
verbatim. It is kept as the record of rounds 1–2. Round 3 runs as a subagent
here, not through the console.
