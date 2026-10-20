# Round 3 — adjudication

- **Manuscript:** `papers/knot-dark-matter-standalone.md` v3 (commit 5dbaa82).
- **Pre-registration:** [round3-preregistration.md](round3-preregistration.md)
  (commit cc05705, made before dispatch).
- **Referee:** a blind subagent with Python and web access.
  - Notes, verdict and scripts: [round3/referee/](round3/referee/). The
    verdict is in `audit-notes.md` §5.
  - Every one of its 16 numerical findings rests on executed code.
- **My arbitration:** [round3/adjudicator/round3_arb.py](round3/adjudicator/round3_arb.py)
  and its `.out`, plus direct checks of the sources named below.
  The corrected inputs now live in `verify/soliton_obituary.py`, which checks
  every number this record quotes.

## Verdict

**Referee: C (fundamentally flawed), medium confidence. I agree for v3 as
written.**

- The headline result ("1e13–4e13 GeV, no dilution required") rests on a
  wrong Kibble normalization.
- Correcting it leaves two routes: a superheavy monopole that needs a named
  dilution mechanism, or a model at v ≲ 100 PeV that already exists in the
  literature.

## Rulings

| # | Referee finding | Ruling | Evidence |
|---|---|---|---|
| 1 | Kibble normalization: one defect per Hubble volume is p ≈ 104, not 0.023 | **Upheld** | My code: p = 104.31 with M_Pl, 0.828 with the reduced M_Pl. v3's 0.0228 drops (1.66√g*)³ ≈ 4.6×10³. My error came from misremembering the formula. |
| 2 | The M* band and "no dilution" fail | **Upheld** | At minimum production M* = 2.9–4.4×10¹² GeV. The 3×10¹³ benchmark is overproduced 2.1×10³–1.2×10⁴ times. The "reduced-Planck factor of 3" was not a convention spread: consistently normalized, the two conventions agree. |
| 3 | Kibble is a floor, not a ceiling; Kibble–Zurek or bubble counting add more | **Upheld** | Murayama–Shu, arXiv:0905.1720, abstract: Kibble "drastically underestimates the production of topological defects". Liveoak–Maharana–Wells, arXiv:2607.20843 (July 2026), abstract: hidden monopoles overclose for breaking scales ≳ 100 PeV unless diluted, e.g. by early matter domination. I did not re-run the referee's Kibble–Zurek integration (1e9–1e12 overproduction). |
| 4 | ψ relic window too high | **Upheld** | v3 omitted ψ̄ and the second doublet member (a factor of 4), and bracketed an exactly known s-wave σv up to ×10. My recount: 10% of the DM at 45–49 GeV, 100% at 146–158 GeV. The referee's Boltzmann integration gives 28–46 / 96–153 GeV. We agree to within ×1.6, and v3's 0.1–0.3 TeV was wrong. |
| 5 | ξ bound 0.760, not 0.77 | **Upheld (minor)** | Using N_eff,SM = 3.044, the 95% bound is ΔN_eff < 0.286. Knock-on: the GW upper end becomes 3.2×10⁷ Hz. |
| 6 | MeV-scale ψ freezes out during BBN | **Accepted, not re-checked** | T_f ~ m/20, so the lower mass bound should be ≳ 20–30 MeV. |
| 7 | "O(1) coefficient at the Planck scale" for the dimension-5 operator is unsupported; the literature generates it at one loop from bi-charged states, which sector separation forbids | **Upheld** | Consistent with the round-2 literature report: Chen–Cline–Frey "induced at one loop by a heavy particle X which carries both…". Sec. 2(a) and 2(b) of v3 are in tension. |
| 8 | Baumgart et al. does not contain the adjoint operator | **Overturned** | arXiv:0901.0283v2, p. 5, footnote 5, verbatim: "It is actually possible to achieve mixing without an abelian factor through an S parameter type operator Tr[Φw_μν]B^μν, where Φ is some operator that transforms as an adjoint of the non-abelian group." The referee missed the footnote. |
| 9 | With mixing and a physical hidden θ, the monopoles carry visible electric charge ~ εθ/2π · e (Witten effect) | **Accepted, not re-checked** | Brümmer–Jaeckel–Khoze eq. 3.19, per the referee. This contradicts v3's "constraints act on ψ, not the dark matter" whenever ε ≠ 0. |
| 10 | Annihilation at α_m ≈ 34 is Preskill's Dirac case, already done for hidden sectors | **Upheld** (abstract level) | LMW 2026 as in #3. |
| 11 | DESI DR2's best fit crosses into phantom (w < −1) above z ≈ 0.4 | **Accepted** | The parent framework's "never phantom" needs the checkpoint's own nuance: non-phantom fits remain compatible at ~2σ. |
| 12 | Minor citation issues: [4] over-generalized; Zwanziger's 4π vs 2π; Schwinger uncited | **Accepted** | — |
| 13 | v3 §6 "all numbers computed by executed code" overstates | **Upheld in substance** | The code checked the arithmetic of a wrong model. See lesson 2. |

Omitted constraints (referee list, accepted as a to-do; not individually
re-checked):

- Re-thermalization by ψ at ε ~ 1e-7–1e-6
- SN1987A and BBN limits on millicharged particles
- Charged-subcomponent and CMB bounds
- Dark acoustic oscillations
- The Higgs portal
- The reheating mechanism for ξ
- Collective magnetic-plasma effects
- Uncited prior art: Murayama–Shu; LMW; Baek–Ko–Park; Khoze–Ro.

**The compatibility theorem is verified** (sympy, including a Groebner basis
at d = 2; random tests at d = 3, 4). But the referee identifies it as
essentially the Born-geometry result of Freidel–Leigh–Minic
(arXiv:1502.08005), which is uncited. Unless a comparison shows otherwise,
the checkpoint's "[D] derived here" tag on it should become [T] with that
citation.

## Pre-registration scored

| Prediction | Outcome | Score |
|---|---|---|
| Verdict B | C | **Miss**: the first after 2 for 2 |
| Weakest link: "the framework does no work" | The referee's #2; its #1 was the abundance normalization | **Miss on #1** (hit on #2) |
| Zero surviving numerical indictments | Three survive (p; the ψ window; ξ), plus the ε coefficient | **Miss**. All are wrong inputs or model choices in my scripts, not arithmetic slips |
| All 23 citations resolve | All exist | **Hit** |
| A misattribution most likely in [5] or [11] | The referee's one misattribution claim (Baumgart) was itself wrong; [4] was flagged as over-generalized | Miss |

Calibration: my confidence in v3 was too high. The failure mode has moved.
In rounds 1–2 it was the referee's unaided arithmetic. In round 3 it is that
**the author's verification checks the author's model**: a wrong physics
input passes a gate that tests only arithmetic.

## Lessons (now in CLAUDE.md)

1. Keep the prediction out of the pre-registration commit subject. The
   auditor's auto-attached git status showed it. The auditor says it did
   not use it, and its verdict differed from the prediction, which argues
   against anchoring. But the round was less blind than intended.
2. An anchor must be independent of the paper. v3's Kibble anchor
   reproduced v2's own number and so tested nothing. The replacement anchors
   are the Friedmann coefficient 1.66 and n/s ≈ 100 (T_c/M_Pl)³ for one
   defect per Hubble volume.

## What survives v3

- The compatibility theorem (as [T], pending the FLM comparison).
- The benchmark-conditional arithmetic: flux, densities, σ_T/M, W′
  overclosure.
- The kinetic-mixing literature points (a) and (c).
- The statement that the minimal adjoint-only sector is excluded.

## Decisions

Paul delegated these on 2026-10-19 ("You make the decisions for me and give
rational"). Claude made them. Paul keeps the veto.

1. **Kinetic mixing: strict sector separation.** ε ≲ 10⁻¹³ from gravity
   alone, and zero if hidden charge conjugation is a gauged symmetry.
   - It is the program's own postulate P4 ("gauge forces do not cross
     polarizations") taken at face value.
   - The alternative rested on an unsupported coefficient. The dimension-5
     "O(1) at the Planck scale" estimate (ruling 7) has no source. The
     sources generate that operator only from bi-charged states, which P4
     forbids.
   - It costs nothing and closes three failure channels at once: ψ
     millicharge, the monopoles' Witten-effect charge (ruling 9), and
     re-thermalization of the hidden sector.
2. **The soliton candidate: retired as a program-native proposal (route c).**
   The surviving version is noted as prior art (route a). Rejected route (b):
   superheavy plus a named dilution.
   - The row earned its place in the checkpoint's trilemma on two claims:
     topology makes it stable for free, and the mass came out of the
     abundance with no free dilution. Round 3 removed the second.
   - Route (b) restores the mass only by adding a free dilution factor of
     at least 10³–10⁴ (ruling 2), probably far more (ruling 3). The mass
     would then no longer be a prediction, and the program does not trade
     falsifiability for survival.
   - Route (a), v ≲ 100 PeV, works, but it is Murayama–Shu's and
     Liveoak–Maharana–Wells's model. Nothing in it depends on Born
     reciprocity (the referee and the pre-registration agree), so claiming
     it would add no testable content and would misattribute it.
   - The program's precedent is the Debt 3 obituary: a dead claim is
     reported prominently and stays dead.
   - Consequence: the trilemma becomes two program-native candidates (gated
     χ particles; the X-condensate), plus the remark that the framework is
     compatible with known PeV-scale topological dark matter.
3. **HANDOFF §8 queue item 3 (the "√N floor"): dropped.**
   - Its premise, Kibble as a ceiling, is inverted (ruling 3).
   - Under decision 2 it has no candidate left to serve.
4. **What comes next: the toy Lagrangian (HANDOFF §8 item 4), after one
   short cleanup.**
   - Every referee across three rounds converges on "the framework does no
     work". The toy action is the only item that can change that, and it is
     acceptance criterion 1 for anything the program proposes.
   - Candidate-level work is downstream of it.
   - The cleanup comes first so the current reference stops asserting what
     round 3 killed: amend checkpoint #11 with the soliton obituary
     (§11–§15), check the Freidel–Leigh–Minic prior art and re-tag the
     compatibility theorem if confirmed, and give §10 the DESI DR2
     phantom-crossing nuance (ruling 11).

Executed the same day:

- v3 moved to `notes/` with a withdrawal banner.
- `verify/knot_numbers.py` (v3's claims) was replaced by
  `verify/soliton_obituary.py`, which checks every number this record
  quotes, with independent anchors. The v3 checks are in history at
  96f58da.
  - This retires the checks of a withdrawn paper. It does not loosen the
    gate: the gate verifies what current documents claim, and v3 no longer
    claims anything.
