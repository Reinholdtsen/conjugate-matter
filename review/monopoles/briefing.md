# Monopoles in the Comatter record: briefing for discussion

**Source key.** #11 = `papers/broken-born-checkpoint-v2.md` (v2.2) · #11v2.0 = `git show 8d588f6:import/broken-born-checkpoint-v2.md` · #14 = `notes/knot-dark-matter-standalone.md` (v3, withdrawn) · #14v2 = `git show 8d588f6:import/knot-dark-matter-standalone.md` · #1 = `notes/broken-born-theory.md` · #9 = `notes/broken-born-program-v1.md` · #10 = `popsci/angle-of-the-mirror.md` · #12 = `popsci/universes-other-half.md` · #13 = `papers/conjugate-special-relativity.md` · HO = `HANDOFF.md` · CL = root `CLAUDE.md` · WL = `review/v3-worklog.md` · ADJ = `review/round3-adjudication.md` · REF = `review/round3/referee/` · FL = `review/wiki-build-flags.md` · RW = `review/wiki-build-rulings.md` · OB = `verify/soliton_obituary.py` · CHK = `scripts/check.sh` · W/ = `wiki/`.

**Checked directly by the synthesizer, beyond the seven sweeps:**
- #11 and HO read in full; #14, #14v2 and #11v2.0 read at every cited line.
- ADJ's rulings, survivors and decisions.
- Flags 21, 22, 28, 33, 34 and 37, and the rulings worksheet: 44 ruling lines, none ticked.
- OB re-run: 16 PASS, exit 0.
- Grep results: no "Witten" in papers/, notes/, HO or popsci/; no document names SL(2,ℤ); only #11:120 mentions U-duality.

The readers agreed on every substantive point. Where their line numbers differed, I checked the file.

## a. The program's position

- **Dead [D]: monopoles in conjugate space as the reason none is seen.** #11:116: “As an explanation of the null result: dead — the relevant duality is electric–magnetic (E↔B, g → 1/g), not x↔p, and inflationary dilution already accounts for absence [T]”. The same verdict is in App. A item 5 (#11:217) and HO:31.
- **Dead, retired 2026-10-19: the monopole dark-matter candidate.** This was #14's proposal of superheavy 't Hooft–Polyakov monopoles of a hidden SU(2) → U(1) sector, placed in the p-polarized half (#11:141; #14:9).
  - Round 3 returned verdict C. One defect per Hubble volume gives p ≈ 104 [V], which is the causal minimum, so the 3×10¹³ GeV benchmark is overproduced 2.1×10³–1.2×10⁴ times [V] (#11:145-146).
  - The version that works, at breaking scales ≲ 100 PeV, is prior art [28S, 29S], and “nothing in it depends on Born reciprocity” (#11:147-150).
  - Also dead: α_d ≈ 34 via our photon (HO:32), hypothesis H (#14:29) and the √N floor (ADJ:132-134).
- **Alive but conditional [D]: conjugate monopoles as objects.** #11:116: “As ontology: alive and consequence-bearing — by P4, conjugate-sector solitons gravitate”. #11 names no consequence beyond gravitation and never specifies the gauge content of the p-polarized sector, so it does not say that any such objects exist (W/electric-magnetic-duality/conjugate-monopoles.md:41, :61).
- **Alive as structure [D — structural; math T]; the unification is [O].**
  - The DSZ pairing makes the charge lattice symplectic, and a duality frame is a Lagrangian polarization. S-duality shares the matrix [[0,1],[−1,0]] with Born's ρ and with Z → −Z⁻¹ (#11:120).
  - “One enlarged modular structure” joining the two choices is a conjecture [O] (#11:120, :192). It is not queued (CL:107-112).
  - There is no Lagrangian for it and no script, and #11 itself has never been reviewed (W/summary.md:37).
- **Established physics [T], absorbed into §11.**
  - The magnetic mirror family: Montonen–Olive, Seiberg, the dual superconductor (#11:118, :223).
  - “A weakly coupled hidden sector always has strongly coupled monopoles, by Dirac quantization [T]” (#11:152).
  - Our magnetic coupling ≈ 34 is the right number, but #11 writes the formula for 137 beside it. This is flag 28, confirmed by audit and not yet ruled on (FL:198-203).
- **Prediction row 8: untagged, with no mechanism from the program.** The row reads “Magnetic monopoles (ours) | Model-dependent | Permanent null; Berry-curvature monopoles in solids as the only shadow | Direct detection” (#11:172). Two open ends are not queued: the topological clumping loophole, which “remains untested, but has no candidate” (#11:154), and the electric-sublattice clause (HO:35).

## b. The threads

### b1. The founding conjecture and its split

- The idea is Paul's founding supposition 5: “Monopoles live in conjugate space, explaining non-detection” (#11:217).
- **#1 v0.1, September 2026** (#1:4). Row 8 reads “Permanent null (p-polarized solitons); Berry-curvature monopoles in solids as the only shadow | Direct monopole detection” (#1:232). #1's P4 already says “Gauge interactions do not connect the two representations” (#1:29).
- **#9 v1.0.** Drops “(p-polarized solitons)” and has no monopole section (#9:105).
- **#11 v2.0**, written on claude.ai before the 2026-10-19 import. It adds §11 and splits the supposition into a dead explanation and a live ontology (#11v2.0:110). P.R.'s correction is worded two ways: “'true but irrelevant' is the empty set” (#11:116) and “'true-but-irrelevant is measure zero'” (#11:217).
- **#11 v2.1** (commit e1c1f67, 2026-10-19) changes two things:
  - §11.1 adds “Their candidacy as the dark matter itself is retired in v2.1 (§12)” (#11:116).
  - App. A's “feeding the knot candidate” (#11v2.0:187) becomes “the knot candidate it fed is retired (§12)” (#11:217).
- **Current status.** The explanation is dead and the ontology is conditional. The wiki notes that the audit was done “By argument, not by calculation” and that “no script and no review round checked it” (W/electric-magnetic-duality/monopole-explanation.md:44).

### b2. Charge lattice, mirror family, electric sublattice

- **§11.3 [D — structural; math T]** (#11:120):
  - “⟨q, q′⟩ = e₁g₂ − e₂g₁ ∈ 2πℤ”, and “the charge lattice is a symplectic space [17†]”.
  - Mutual locality defines a Lagrangian sublattice.
  - Choosing a duality frame “is choosing a Lagrangian polarization of charge space, in the literature's own words”. That phrase has no citation.
  - S-duality, τ_c → −1/τ_c, is called “the third appearance of one matrix in this program”.
- **The [O] conjecture** (#11:120). The polarization P5 selects and the charge-lattice polarization “are components of one enlarged modular structure”, by analogy with T- and S-duality inside U-duality [T].
  - Open problem 8 (OP8) asks to “formalize §11.3's unification [O]” (#11:192).
  - No document names SL(2,ℤ) (W/electric-magnetic-duality/modular-group.md:158).
- **§11.2 [T]** (#11:118):
  - Montonen–Olive is cited as “[17†-adjacent; 18†], exact in maximally supersymmetric Yang–Mills”. Seiberg's magnetic quarks are cited [18†].
  - The dual superconductor is tagged “[T, 't Hooft–Mandelstam†]”, but the reference list has no such entry (#11:231-259).
  - “Non-observation is structural … the magnetic world is our strong-coupling mirror, heavy and bound.”
  - “Same explanatory shape as §7: the duality is genuine, and its structure hides its second half.”
- **App. A item 11.** The mirror family is “alive as established physics … with the polarization identification as the program-native addition” (#11:223).
- **How the shared matrix was used, then withdrawn:**
  - #14 v2 made it carry weight. Its conjecture: “the momentum-polarized matter sector is the S-dual image of the electric sector”, with the coupling fixed by “the reciprocity map, acting as the modular S transformation … alpha_d = 1/(4 alpha) ~ 34”. The manuscript called this its “load-bearing conjecture” (#14v2:21).
  - Round 2 named it the weakest link: “matrix coincidence ≠ physical identity” / “numerology” (HO:90).
  - Paul decided on 2026-10-19 (worklog F2, commit 2eb58de) that “S-duality is no longer what fixes α_d” (WL:63).
  - #14 v3: “We use this only as motivation … No numerical result below depends on it” (#14:23), and “Exact electric-magnetic duality is also not assumed” (#14:31).
  - The round-3 referee wrote “'Charge space is symplectic' is interpretation” and noted that Zwanziger writes 4πℤ where the documents write 2πℤ (REF/audit-notes.md:33-34). Ruling 12 accepted both points as minor (ADJ:41). #11 was not amended.
- **The electric-sublattice criterion was never delivered.**
  - Three wordings asked for it:
    - HO open item 1: “η the order parameter also selecting the electric sublattice” (HO:35).
    - #14 v2: “selecting simultaneously the position polarization and the electric sublattice” (#14v2:57).
    - #14 v3: “the hidden sector's electric description; deriving hypothesis H from that action would make the coupling a prediction” (#14:110).
  - The toy-model worklog took its criteria from “The referees' wording (rounds 1–2)”, which lacks the clause (notes/toy-lagrangian.md:6-9). #11 §14 item 11 says the criterion was “Met in the referees' wording” (#11:195).
  - The toy models contain no gauge field and no charge lattice. No document lists the clause as met or as open; only the wiki registers it as open (W/status/open-problems.md:145).

### b3. The soliton/knot candidate (#14)

- **Origin.**
  - #11 v2.0 §12 proposed “topological knots, the conjugate sector's monopoles” (#11v2.0:120), described as “topological solitons of a p-local gauge sector (§11)”.
  - Their localization in momentum rested on an unproven conjecture: “[O: 'solitons of p-local gauge theories are p-localized' is duality-plausible, underived]” (#11v2.0:128).
  - The current plain-language abstract still credits the charge-lattice observation: it “suggested a third, topological candidate” (#11:16).
- **v1** (claude.ai; its text is not in the repo). It took α_d ≈ 34 from Dirac quantization against our photon. Round 1 (verdict B, medium confidence) killed that step: you “can't use our DSZ lattice and then deny coupling to our photon” (HO:32). Round 1 also:
  - renamed “knots” to “π₂ monopole-class”;
  - added a kinetic-mixing postulate with an ε ≲ 10⁻⁵ exclusion;
  - made the toy Lagrangian acceptance criterion 1 (HO:88).
- **v2.**
  - “'Magnetic' refers throughout to the sector's duality-frame character - solitonic, strongly coupled - not to a charge visible to our electromagnetism” (#14v2:21).
  - The objects are “monopole-class defects classified by pi_2, not knot solitons” (#14v2:29).
  - Kinetic mixing was declared forbidden “to all orders in field theory”, and “gravitational loops … induce none” (#14v2:23).
  - Round 2 returned B near B/C (HO:90).
- **The worklog, 2026-10-19.**
  - L1: with the dark U(1) unbroken, a hidden monopole produces no visible magnetic flux, so v2's εg premise was wrong (WL:64-80).
  - R2: “1/(4α) = 34.26 (eg = 2πn) vs 1/α = 137.04 (eg = 4πn)”. Round 2's “toward ~6–8” is “not reproduced” (WL:28).
  - O3: #14's ordinary kinematics was never reconciled with #13 (WL:135-147).
- **v3** (commit 5dbaa82).
  - The sector is SU(2)_d → U(1)_d with an adjoint scalar and a Dirac doublet ψ. It is “identified with the momentum-polarized half”, and #14 lists that identification as Conjectural (#14:9, :97).
  - Hypothesis H, “(g_d/2)^2/4pi = alpha”, gives α_m ≈ 34 (#14:29).
  - “These objects carry no charge under our photon” (#14:31).
  - The abundance used “p ~ 0.023; we take p = 1 as the upper end” (#14:47), which led to the claim “no dilution required” (#14:9).
  - Kinetic mixing is treated in three parts:
    - (a) gravity alone gives ε ≲ 10⁻¹³ (#14:35);
    - (b) a dimension-5 operator with an O(1) coefficient at the Planck scale gives ε ~ 10⁻⁷–10⁻⁶ (#14:36);
    - (c) with U(1)_d unbroken, mixing produces no visible monopole flux (#14:37).
- **Round 3.** It was pre-registered as B, with the weakest link expected to be “the framework does no work”. The verdict was C.
  - Ruling 1: p = 104.31 with M_Pl and 0.828 with the reduced M_Pl. v3's 0.0228 had dropped a factor (1.66√g*)³ ≈ 4.6×10³. The adjudicator: “My error came from misremembering the formula” (ADJ:30).
  - Ruling 3: the Kibble count is a floor, not a ceiling. The adjudicator did not re-run the referee's Kibble–Zurek (KZ) integration (ADJ:32).
  - Ruling 7: the O(1) coefficient for the dimension-5 operator is unsupported (ADJ:36).
  - Ruling 9: the monopoles' Witten-effect charge was “Accepted, not re-checked” (ADJ:38).
  - Ruling 10: annihilation at α_m ≈ 34 “is Preskill's Dirac case” (ADJ:39).
  - Ruling 13: “The code checked the arithmetic of a wrong model” (ADJ:42).
  - The referee's summary: the proposal “stands or falls on that literature, independently of Born reciprocity”. Matching ψ's charge to e/3 instead gives α_m = 308, and “the framework gives no way to choose” (REF/audit-notes.md:241-247).
- **Decisions.** Paul delegated them, Claude made them, and Paul keeps the veto (ADJ:99-100).
  - Decision 1, strict sector separation. It closes “ψ millicharge, the monopoles' Witten-effect charge (ruling 9), and re-thermalization” (ADJ:102-112).
  - Decision 2, retire the candidate (route c). The ≲ 100 PeV model is noted as prior art. Superheavy masses rescued by dilution are rejected, because that needs “at least 10³–10⁴” and “the program does not trade falsifiability for survival” (ADJ:113-131).
  - Decision 3, drop the √N floor, an idea that existed only in the claude.ai chat (HO:36, :73). “Its premise, Kibble as a ceiling, is inverted” (ADJ:132-134).
- **What survives.**
  - #11 lists three survivors: the weak-to-strong statement [T], the exclusion of the adjoint-only sector [V], and the untested loophole (#11:151-154).
  - ADJ's list differs. It adds the arithmetic conditional on the benchmark (flux, densities, σ_T/M, W′) and kinetic-mixing points (a) and (c), and leaves out the weak-to-strong statement (ADJ:89-95).
- **The gate.** OB runs in CHK:21.
  - Its closing line says “every number the round-3 record quotes reproduces” (OB:114; docstring OB:2-5). That overclaims: α_m ≈ 34, ε, the KZ and Boltzmann ranges and ruling 6 are not recomputed (flag 33, FL:223-230).
  - #11 §12's own statement, “The [V] numbers here are gated”, is accurate (FL:230).

### b4. Observables and prior art

- **Row 8** (#11:172), untagged.
  - “(ours)” was added in v2.0 (#11v2.0:147). It leaves hidden-sector and conjugate monopoles outside the row (W/predictions/monopole-null.md:38).
  - #11 gives two reasons our monopoles are absent, both [T] and neither the program's own: inflation (#11:116), and strong coupling that keeps them “heavy and bound” (#11:118).
  - The wiki summary says “row 8's null already has the standard explanation” (W/summary.md:99).
  - #11 does not list row 8 among its near-term tests, which are rows 1, 4 and 7 (#11:207).
- **The Berry-curvature shadow.** Weyl semimetals [16†]: “right geometry, different flux” (#11:116). In #1 the same analogy described the p-local mean field of the dead clumping mechanism: “the same structure as Berry-curvature transport in solids” (#1:157).
- **Monopole searches and the Parker bound** appear only in #14's counterfactual. At 3×10¹³ GeV, monopoles of our U(1) would give a flux F = 3.18×10⁻⁸ cm⁻²s⁻¹sr⁻¹. That is 7.50 orders of magnitude above the Parker bound, 8.06 above the MACRO limit and 12.03 above the extended Parker bound (REF/step2a.out:46; #14:57). Hence “Sector separation is therefore mandatory” (#14:57). These numbers were gated until commit 5b6efaa and are not gated now.
- **The Witten effect** appears nowhere in #11, the notes, HO or the popsci articles (grep). It appears only in round 3: the monopoles would carry “visible electric charge ~ εθ/2π · e”, from 1.6×10⁻⁸ to 1.6×10⁻⁷ e for ε = 10⁻⁷–10⁻⁶ (ADJ:38; REF/step4b.out:9-14). Decision 1 closed this channel.
- **Kinetic mixing.**
  - Point (c) survives round 3 (ADJ:94): “With U(1)_d unbroken, kinetic mixing does not give the monopoles magnetic charge under our photon” (#14:37).
  - Strict P4 allows only gravity-induced mixing, ε ≲ 10⁻¹³ [27S] (#11:45). The referee reads 10⁻¹³ as a floor rather than a ceiling, and the question is unresolved (W/history/documents/source-conflicts.md:101).
- **The topological clumping loophole.**
  - It began as v2.0's unproven [O] conjecture (#11v2.0:128).
  - #11 now calls it “untested, but has no candidate” (#11:154), and also “closed by the §12 obituary” (#11:192).
  - App. A calls it “untested” (#11:215); HO:29 called it “untouched”.
- **Prior art.**
  - Murayama–Shu [28S] and Liveoak–Maharana–Wells [29S] were checked at the level of their abstracts (ADJ:32).
  - Baek–Ko–Park and Khoze–Ro were accepted as uncited prior art (ADJ:54) and are still not cited in #11 (#11:257-259).

## c. Monopoles and comatter

- **The record keeps the two sectors separate, in its own words.**
  - “the relevant duality is electric–magnetic (E↔B, g → 1/g), not x↔p” (#11:116).
  - P4: “gauge forces do not cross polarizations”, taken strictly since v2.1 (#11:45).
  - Row 8 covers only “Magnetic monopoles (ours)” (#11:172).
  - Our own magnetic sector is hidden by its strong coupling, “heavy and bound” (#11:118), not by being in the other polarization.
- **Conjugate monopoles are allowed, would gravitate, and are not monopoles of our photon.**
  - #11: “by P4, conjugate-sector solitons gravitate” (#11:116).
  - HO: “'dark by sector separation,' NOT magnetically charged under our photon” (HO:26).
  - #14 v3: “These objects carry no charge under our photon. The Dirac quantization used above is the hidden sector's own” (#14:31).
  - #11 does not say what gauge fields the p-polarized sector has (W/electric-magnetic-duality/conjugate-monopoles.md:41). #13 says the dual dynamics, “their Maxwell, their field theory”, cannot be written until the fully covariant construction with t ↔ E exists [O] (#13:85).
- **The strong identification was made twice, and neither survives.** It says the p-polarized sector is the magnetic, or S-dual, image of our electric sector.
  - #14 v2 conjectured it: “the S-dual image of the electric sector” (#14v2:7, :21). Paul's F2 decision superseded it (WL:63), v3 demoted it to “only as motivation” (#14:23), and it was withdrawn with #14.
  - #12 states it, presenting the framework “as if it were confirmed” (#12:5):
    - “The momentum-polarized sector is the magnetic side of electromagnetism … about 34, against our 1/137” (#12:41);
    - “A candidate identity for dark matter's charge: the magnetic half of electromagnetism's own duality” (#12:73).
  - #12's version conflicts with three things: the dead derivation of α_d via our photon (HO:32), strict P4 (#11:45), and row 7 (#11:171). The wiki records it as dead on its own reading of which source takes precedence (W/electric-magnetic-duality/magnetic-identification.md:4). No review or ruling addresses it.
- **What is left open: whether the two choices are one structure [O]** (#11:120). Even if so, that alone would not put magnetic states in momentum space.
  - The only dynamical test the record ever named, an order parameter η that also selects the electric frame, has not been attempted (HO:35; #14:110).
  - The plain-language text reads stronger than the tag: “Two intuitions, one operation” (#11:114); “one structural unification (polarization of phase space and of charge space as one move)” (#11:205).
- **Answer.** In #11 v2.2 the magnetic sector of our electromagnetism is not the conjugate sector. If the p-polarized sector has gauge fields that allow monopoles, its monopoles would be a separate population, coupled to us only through gravity. The dark sector now has no magnetic content: χ particles and the X-condensate (#11:128-133).

## d. Numbers

| Quantity | Value | Source | Provenance |
|---|---|---|---|
| Kibble p, one defect per Hubble volume (g* = 100) | 104.31 (M_Pl); 0.828 (reduced M_Pl) | #11:145; OB:62-63 | [V]; gated (CHK:21); anchors: Friedmann 1.66 and Gangui's n/s ~ 100(T_c/M_Pl)³ (OB:52, :55) |
| #14's earlier p | 1 (v2); 0.0228 (v3), which dropped (1.66√g*)³ = 4575.6 | #11:144; OB:64 | gated as an error decomposition; both values dead |
| M* at which minimum production closes | 2.873–4.441×10¹² GeV | #11:146; OB:73 | [V]; gated; model assumes H, f = 1–1.787, T_c ~ v (OB:16-19) |
| Overproduction of the 3×10¹³ GeV benchmark | 2.08×10³–1.19×10⁴ | #11:146; OB:78 | [V]; gated |
| KZ production plus annihilation | Ω/Ω_DM 1.14–2.22×10¹² (integration); 1.24×10⁹–2.16×10¹¹ (LMW analytic); ruling 3 says “1e9–1e12” | FL:154-158; ADJ:32 | REF/step4.out; not gated; adjudicator did not re-run it; flag 21 |
| Hidden-monopole overclosure scale | ≲ 100 PeV, or early matter domination | #11:147 | [29S], abstract level; not executed |
| W′± relic, adjoint-only sector | 9.5×10¹⁵–2.0×10¹⁷ (quoted as 10¹⁶–10¹⁷) | #11:153; OB:108 | [V]; gated; holds only at the withdrawn benchmark |
| ψ relic window (dead) | 10% of DM at 45.2–48.8 GeV; 100% at 146.4–158.0 GeV | OB:90-92; ADJ:33 | gated; referee's 28–46 / 96–153 GeV not gated |
| Dark radiation | ΔN_eff < 0.286; ξ < 0.7601 (v3: 0.77) | OB:98-99; #14:61 | gated |
| GW peak upper end (dead) | 3.17×10⁷ Hz | OB:102 | gated |
| Gravity-only kinetic mixing | ε ≲ 10⁻¹³; zero if hidden C exact | #11:45 | [27S]; not executed; ceiling or floor unresolved |
| Our magnetic coupling at e·g = 2π | g²/4π = π/e² = 1/(4α) = 34.259 | FL:198-203; review/wiki-build-checks/dirac_coupling_check.out:1, :4 | #11 writes “4π/e² ≈ 34” [T] (#11:118); check prints only, not gated; α⁻¹ typed in (†) |
| 4π/e² as written | 137.036 = 1/α: the e·g = 4π value, and S's α_D for e = electron | dirac_coupling_check.out:3; review/wiki-build-checks/audit/flag28_recompute.out:26, :39-41 | audit scripts; not gated |
| Hidden α_m under H (dead) | 34.259; 137.036 (W′ matched); 308.3 (ψ at e/3); 28.61–28.86 (run to 10¹² GeV) | REF/step2a.out:3-8; #14:29 | referee script; not gated; not recomputed by OB (flag 33) |
| Round 2's running claim | “toward ~6–8”; recomputed 29.0 / 28.8 / 27.3 at 10¹¹ / 3×10¹¹ / 10¹⁶ GeV | HO:90; WL:28 | “[V]” via the retired knot_numbers.py; not gated |
| Counterfactual flux if the monopoles were ours (3×10¹³ GeV) | 3.18×10⁻⁸ cm⁻²s⁻¹sr⁻¹; 7.50 / 8.06 / 12.03 orders over Parker / MACRO / extended Parker | REF/step2a.out:46; #14:57 | referee script; gated until 5b6efaa, not now |
| Flux limits used | Parker ~10⁻¹⁵ (M ≲ 10¹⁷ GeV); MACRO 2.8×10⁻¹⁶ (m ≳ 10¹⁰ GeV); extended Parker 10⁻¹⁶(M/10¹⁷ GeV) | #14:57 | literature (#14 refs [20]–[22]), checked by the round-3 referee; not executed |
| Witten-effect visible charge | ~εθ/2π·e = 1.59×10⁻⁹–5.00×10⁻⁷ e (ε = 10⁻⁷–10⁻⁶, θ_d = 0.1–π) | REF/step4b.out:9-14; ADJ:38 | referee script; “Accepted, not re-checked”; not gated; channel closed by strict P4 |
| σ_T/M at the benchmark | ~10⁻²⁶ cm²/g | #14:63 | referee-confirmed; not gated |
| Collective time 1/ω_p | 17.2 yr (local); 9.67×10³ yr (cosmic mean) | REF/step4.out:61-63 | referee script; “Unevaluated, not an indictment”; not gated |
| Dilution needed to rescue a superheavy mass | ≥ 10³–10⁴ | ADJ:119-120 | from ruling 2; not separately executed |
| HANDOFF-era mass window | ~10¹³–10¹⁷ GeV | HO:26 | chat-era; never gated; superseded |
| Reheating the hidden transition needs | T_RH ≳ 1.06–1.90×10¹² GeV | REF/step4c.out:1-2 | the script is not in the repo; not gated |

## e. Timeline

- **1931–1995, the literature as #11 cites it.** Dirac 1931, Schwinger 1966, Zwanziger 1968 [17]†; Montonen–Olive 1977 and Seiberg (hep-th/9411149) [18]† (#11:247-248). #11's plain text: “proposed in 1977, named in 1994” (#11:114).
- **September 2026.** #1 v0.1, with row 8's “(p-polarized solitons)” (#1:4, :232).
- **September–October 2026, on claude.ai; git cannot date these:**
  - #9 v1.0 (#9:105);
  - #11 v2.0, with §11, the knot trilemma and App. A items 5 and 11 (#11v2.0:106-130, :187);
  - #14 v1 and round 1 (B, medium confidence), then #14 v2 and round 2 (B near B/C) (HO:88-90);
  - #12, containing the magnetic identification, listed as “final” (HO:61).
- **2026-10-17.** The round-3 audit run on claude.ai dies on a rate limit (HO:94).
- **2026-10-18 23:07.** Initial commit, with the README tagline (6b8f599).
- **2026-10-19:**
  - 10:28: import of the claude.ai files (8d588f6);
  - 10:41: #14 v2's numbers recomputed (678e48a);
  - 10:59: L1, no visible flux with a massless dark photon (2b72da0);
  - 13:23: Paul's F1/F2 decisions: benchmark moved to 3×10¹³ GeV, and S-duality no longer fixes α_d (2eb58de; WL:63);
  - 13:25: W′ overclosure scripted (d15cd4a);
  - 14:42: #14 v3 (5dbaa82);
  - 14:48: round 3 pre-registered (cc05705);
  - 15:47: verdict C (96f58da);
  - 17:14: decisions: candidate retired, strict P4, √N floor dropped, OB added to the gate (5b6efaa);
  - 17:29: #11 v2.1 (e1c1f67);
  - same day: the toy-model criteria fixed without the electric-sublattice clause (notes/toy-lagrangian.md:6-9).
- **2026-10-20.** #11 v2.2: criterion 1 “Met in the referees' wording” (#11:4, :195).
- **2026-10-21:**
  - wiki breadth pass, including the electric–magnetic duality section (7b9438b);
  - flags 21, 22, 28, 33–34 and 37 recorded (5327429, 16bbacb, 293dcc3, 9dbcf3a, ce26397);
  - refuter audit committed (d89b457, 21:28 local time); the flags file dates the audit 2026-10-22 (FL:9).
- **2026-10-22.** Witten-effect wiki page (8b677d9). Rulings worksheet prepared, with all 44 entries unticked (RW:5-6). GitHub description read (RW:2605-2635).
- **2026-10-26.** Program renamed Comatter (da72ce2); the monopole text is untouched (#11:6).
- **2026-10-28.** Executive summary, with row 8 glossed as “The absence is already explained by inflation” (7151fc0; W/summary.md:110). “Debt-3 loophole” renamed “clumping loophole” (c12da1b).

## f. Tensions and inconsistencies

**Superseded text still in the repo (the document wins)**
- **README:2**, “Physics hypothesis explaining dark matter and missing magnetic monopoles”, contradicts #11:116, #11:217 and HO:31.
  - It is unchanged since 6b8f599 and is also the public GitHub description (RW:2605-2635).
  - Flag 37 is confirmed and unruled (FL:241-244).
- **HO keeps the candidate alive in several places:**
  - “Current best DM candidate” (HO:26);
  - “As ontology they're alive (the soliton candidate)” (HO:31);
  - the √N floor as open item 2 and queue item 3 (HO:36, :110);
  - the three-way question (HO:42);
  - #14 v2 as “CURRENT” (HO:63).
  #11:137-155 and CL:44-48 and :107 supersede all of these. HO's monopole text is unchanged since the import.
- **The popsci articles.**
  - #12's magnetic identification and mirror family (#12:41, :43, :73), its three-candidate framing (#12:39, :45), and #10's “topological knots — the conjugate sector's monopoles” (#10:37) are unchanged since the import (git log -S).
  - HO called #12 “final” (HO:61).
  - No flag and no queue item targets them.
- **Round 2's running claim.** “drags 34 toward ~6–8”, recorded as a valid hit (HO:90), is “not reproduced” for the electromagnetic coupling (WL:28).

**Inside #11**
- **Flag 28.** #11:118 writes “4π/e² ≈ 34”. But 4π/e² = 1/α = 137.036, and 34 = π/e² = 1/(4α) (FL:198-203; dirac_coupling_check.out:1-4).
  - The sentence has been verbatim since v2.0 (#11v2.0:112).
  - The flag is confirmed by two checks and unruled. Its check script prints only and sits outside the gate (FL:4-7).
- **The loophole.** “untested, but has no candidate” (#11:154) and “untested” (#11:215) stand against “closed by the §12 obituary” (#11:192).
- **P.R.'s wording.** “the empty set” (#11:116) against “measure zero” (#11:217).
- **Tag against prose.** §11.3 tags the identification [D — structural] and the unification [O] (#11:120, :192). But the abstract, the §11 plain-language passage and §15 say “the same mathematical move”, “Two intuitions, one operation” and “one structural unification” (#11:16, :114, :205).
- **The shadow.** §11.1 makes Weyl-semimetal monopoles the “laboratory shadow” of conjugate-sector solitons (#11:116). Row 8 makes them “the only shadow” of “Magnetic monopoles (ours)” (#11:172).
- **Row 8's footing.** The row sits under “Program requirement” (#11:163, :172), yet both of #11's reasons for the absence are [T] (#11:116, :118).
- **“Knots.”** Round 1 renamed the knots π₂ monopole-class (HO:88; #14v2:29). #11 still says knots (#11:98, :126, :205, :217), and so do #10:37 and #12:41, :43.
- **DSZ normalization.** #11 writes 2πℤ (#11:120); Zwanziger writes 4πℤ (REF/audit-notes.md:33-34). Ruling 12 accepted the point, but #11 was not amended (ADJ:41).
- **Citations in §11.**
  - The label “[17†-adjacent; 18†]” is unexplained.
  - “'t Hooft–Mandelstam†” has no reference entry (#11:118, :231-259).
  - “in the literature's own words” has no citation (#11:120).
- **Two survivor lists.** #11 §12 includes the weak-to-strong statement [T] (#11:152), which ADJ leaves out. ADJ's benchmark arithmetic and mixing point (c) (ADJ:89-95) are absent from #11 §12.

**The gate and the review record**
- **OB's self-description.**
  - Its docstring (OB:2-5) and closing line (OB:114) claim more than it checks: six quoted figures are not recomputed, including α_m ≈ 34 and ε (flag 33, FL:223-230). ADJ:12-13 makes the same claim.
  - Its constants are labelled “PDG and Planck 2018 values” (OB:20) but are typed in, and the model-memory caveat of the old script was dropped (flag 34, FL:231-234).
- **Ruling 3's range.** Ruling 3 attributes “1e9–1e12” to the referee's integration (ADJ:32). The integration gave 1.14e12–2.22e12; the 1e9 end comes from LMW's analytic estimate (flag 21, FL:154-158).
- **Missing scripts.** ADJ:9 says every one of the referee's 16 numerical findings “rests on executed code”. But REF/ holds step4c.out and step4d.out with no step4c.py or step4d.py.
- **Strict P4's bound.** #11:45 says “ε ≲ 10⁻¹³ [27S]” and that the mixing “vanishes if hidden charge conjugation is exact”. Decision 1 says “zero if hidden charge conjugation is a gauged symmetry” (ADJ:102-103). The referee reads 10⁻¹³ as a floor (W/history/documents/source-conflicts.md:101).

**The wiki against the documents (the document wins)**
- **A tag.** W/electric-magnetic-duality/magnetic-identification.md:94 tags “under strict P4 they carry no charge under our photon [D]”. In #11 the [D] tag (§11.1) covers the step to gravitation. The no-charge clause follows from P4, which is [P] (#11:45), and the record states it explicitly only for #14's hidden sector (HO:26; #14:31).
- **Row 8 in the summary.** W/summary.md:99, :110 frame row 8 as already explained by inflation. #11:172 says “Model-dependent”, and the summary omits §11.2's second, structural account (#11:118).
- **#12's identification.** The wiki records it as dead (W/electric-magnetic-duality/magnetic-identification.md:4; W/history/documents/source-conflicts.md:196). That verdict is the wiki's own reading of precedence, not a ruling.
- **Line numbers.** RW's line numbers are from commit 0990cc3 (RW:5-6). It places §11.2 at line 117 (RW:1321); it is now #11:118.

**Inside the withdrawn #14 (these died with it)**
- **Mixing.** §2(a) and §2(b) are “in tension” (ruling 7, ADJ:36).
- **The Kibble count.** “p = 1 as the upper end” (#14:47) conflicts with #14's own first-order transition, whose bubble counting gives p ~ 10²–10⁸ (REF/audit-notes.md:163-168).
- **Where the constraints act.** “The decisive constraints therefore act on psi, not on the dark matter itself” (#14:37) conflicts with ruling 9 (ADJ:38).
- **The code.** “All numerical statements … computed by executed code” (#14:79) conflicts with ruling 13 (ADJ:42).
- **ξ.** #14 has ξ < 0.77 (#14:61, :105); the gated value is 0.7601 (OB:99).

## g. Open items and leads

- **OP8**, formalize §11.3's unification [O] (#11:192). Not queued (CL:107-112).
- **The electric-sublattice clause** (HO:35; #14:110). Not queued, and listed by no document; only the wiki registers it (W/status/open-problems.md:145).
- **The topological clumping loophole** (#11:154). Not queued; it has no work item (W/history/documents/source-conflicts.md:85).
- **Checks of the † citations** behind §11: [16]†, [17]†, [18]†, 't Hooft–Mandelstam†, the label “17†-adjacent” and the phrase “in the literature's own words” (#11:118-120, :194, :263). Queued as queue item 1, the † literature battery (CL:108-110).
- **Gravity-induced kinetic mixing** (HO:113, part of HO §8 item 6). Nominally inside queue item 1. #11 already rests on [27S]; the ceiling-or-floor and exact-or-gauged questions are unresolved.
- **Flag 28** (RW:1316-1342). Accepting it would move dirac_coupling_check.py into verify/ and the gate, and bump #11 to v2.3. Awaiting Paul's ruling.
- **Flag 37**, the README and GitHub description (RW:2605-2635). Awaiting Paul's ruling.
- **Flags 33 and 34** (OB's docstring and constants), **21** (ruling 3's range) and **22** (#14's N_eff interval). Awaiting Paul's ruling.
- **The p-polarized sector's gauge content and dual dynamics**, “their Maxwell” [O] (#13:85). Not queued.
- **Dual kinematics for any p-polarized sector**, Paul's question O3 of 2026-10-19 (WL:135-150). Not queued.
- **Whether polarization selection in the early universe leaves defects** (W/symmetry-breaking/topological-defects.md:196). No document registers it; not queued.
- **Round-3 leftovers**, moot now that the candidate is retired. None is queued.
  - collective magnetic-plasma effects (ADJ:53);
  - the KZ integration, not re-run (ADJ:32);
  - rulings 6 and 9, not re-checked (ADJ:35, :38);
  - Baek–Ko–Park and Khoze–Ro, still uncited (ADJ:54).
- **Popsci #10 and #12** still present the candidate and the magnetic identification as live. No flag, no queue item.
- **Dropped:** the √N floor (ADJ:132-134), and the superheavy-plus-dilution rescue, route (b) (ADJ:113-122).

## Verifier corrections (adversarial pass, 2026-10-29)

60 key claims checked: 53 confirmed, 7 misstated (K14, K15, K18, K26, K56, K58, K59). None is a wrong citation or unsupported, and every path:line resolved within 3 lines.

The misstatements:
- K15 and the §b2 body: ruling 12 covered only the 4π-vs-2π citation point (plus [4] and Schwinger), not the referee's 'interpretation' remark. The referee also judged 2πℤ physically fine.
- K26: only the adjudicator checked LMW at abstract level. The referee used its Sec. III and eqs. 13–30.
- K18: the [O] conjecture is not the only statement joining the two polarizations (#11:16, :18, :114, :120, :205 all do).
- K56: its status should be dead (the wiki's reading), not superseded. 'No paper' needs a caveat for #14 v2's S-dual conjecture.
- K59: #11's [D] is the §11.1 section tag, and #11 never states the no-charge clause.
- K14: X is #11's momentum-space geometry, so 'neither hidden half is the conjugate sector' overreaches for X.
- K58: see the biggest gap below.

Numbers: all table values reproduce. OB re-run 2026-10-29 gives 16 PASS, exit 0, and it is gated at scripts/check.sh:21. knot_numbers.py left the gate in 5b6efaa; it had also gated α_m 34/137/29 and σ_T/M, which the table omits. Two mismatches:
- §b4's Witten range 1.6e-8–1.6e-7 e is only the θ_d = 1 subset; the table's 1.59e-9–5.00e-7 matches step4b.out:9-14.
- The LMW eq. 25 values are printed as Ω_M (step4.out:36-41), not Ω/Ω_DM.

Tensions: 24 of 27 hold. Three do not as framed: DSZ normalization, 'A tag', and 'Row 8 in the summary' ('Model-dependent' is the standard-expectation column).

Biggest gap: review/closed-universe/analyses/gravity-sector.json:250-253 and :480 compute π₂(Λ(4)) = Z₂ and register as open the fate of Z₂ point defects, textures and τ-strings from the polarization-breaking transition. The program's own order parameter therefore admits monopole-type defects, which contradicts K58 and §g.

Also missing from the briefing:
- v2.0's OP8 listed 'conjugate gauge sectors and their soliton spectrum' as open, and v2.1 closed it unanswered (e1c1f67, 8d588f6:...:167). This bears directly on the conditional ontology.
- The Witten-effect physics appears unnamed in #14:37(ii) and WL:79-80.
- #12:45's 'forty orders' has no record source.

- K14 (misstated): #11:118 does draw the §7 parallel and does not develop it. 'Neither hidden half is the conjugate sector' is the briefing's own gloss. It is clearly true for the magnetic half (§11.1, #11:116). For X it is contestable: #11 calls X 'momentum-space geometry' that 'gravitates, massively and invisibly to everything not polarized its way' (#11:84), and §8 makes X-exchange the χ gate. X is not the p-polarized matter χ, but it is the momentum side's geometry.

- K15 (misstated): Ruling 12 (ADJ:41) accepts only 'Minor citation issues: [4] over-generalized; Zwanziger's 4π vs 2π; Schwinger uncited'. The referee's '"Charge space is symplectic" is interpretation' (audit-notes.md:34) is not among them and was never ruled on, so the briefing body's 'Ruling 12 accepted both points as minor' is wrong. The referee also wrote 'The 't Hooft-Polyakov monopole with doublets realises 2 pi, so the physics is fine; but [7] as cited states 4 pi' (audit-notes.md:33-34). The problem is a citation mismatch in #14 v3's [7], not an error in 2πℤ. Round 3 reviewed #14, and no decision asked for #11 to be amended (ADJ:141-145).

- K18 (misstated): The [O] conjecture is the only tagged claim that the two choices form one structure. It is not the only statement joining them. Several other passages in #11 do so: §11.3 [D — structural] says both are generated by the same matrix (#11:120); the plain abstract says 'the same mathematical move' (#11:16); the technical abstract says 'the same polarization choice recurs' (#11:18); §11's plain passage says 'Two intuitions, one operation' (#11:114); §15 lists 'one structural unification (polarization of phase space and of charge space as one move)' (#11:205). The briefing's own K20 and K21 say this.

- K26 (misstated): 'Abstract level' describes the adjudicator's check only (ADJ:32; ruling 10, ADJ:39). The round-3 referee read LMW past the abstract: it cites LMW Sec. III and eqs. 13, 16, 18, 25 and 28–30 (audit-notes.md:133, :169-175) and evaluates them in step4.py (step4.out:21-41). The specific '≲ 100 PeV, or early matter domination' clause is quoted from the abstract by both.

- K56 (misstated): The quotes at #12:5 and :41 are exact, but two points need correcting. (1) The status 'superseded' is wrong. The wiki records the identification as dead (magnetic-identification.md:4; conjectures.md:87). Nothing replaced it with a corrected version, and no ruling exists. (2) 'No paper makes this claim' holds only for the strong form, magnetic charge visible to our electromagnetism. #14 v2, which sat in papers/ until v3, conjectured that the momentum-polarized sector is 'the S-dual image of the electric sector', while denying any charge under our photon (git 8d588f6:import/knot-dark-matter-standalone.md:7, :21). The briefing's own §c counts that as the same identification.

- K58 (misstated): The record does connect the order parameter's topology to defects. The closed-universe gravity-sector analysis computes π₂(U(4)/O(4)) = Z₂ and π₃ = Z₂, tagged [D][V][T] (review/closed-universe/analyses/gravity-sector.json:243-262, claims C35–C37). It lists as open 'Fate of Z2 textures and Z2 point defects of Λ(4), and of τ-strings, produced at the polarization-breaking transition' (gravity-sector.json:480). π₂ classifies point defects, the monopole type. Its script, grassmannian_homotopy.py, lives in a session directory outside the repo (gravity-sector.json:503-504) and is not gated. No paper or note makes the connection, and none ties it to monopoles by name or to the loophole.

- K59 (misstated): The wiki line is quoted correctly. But #11's [D] is §11.1's section tag (#11:116) and covers the whole audit, not 'only the step to gravitation'; the briefing's own K1 calls it the section tag. #11 never states the no-charge clause for conjugate monopoles; the wiki infers it from P4 (conjugate-monopoles.md:51). #11's own practice tags a one-step consequence of P4 as [D] ('by P4, conjugate-sector solitons gravitate' under §11.1 [D]), so [P] is not the better tag. The real problem is that the wiki states a consequence #11 does not, which conflicts with wiki/CLAUDE.md's rule that the wiki adds no results.

## Discussion hooks

- Synthesizer's note: P4 as written ('gauge forces do not cross polarizations', already in #1) forbids a monopole of our U(1) from being p-polarized. Supposition 5 therefore conflicts with the program's own postulate before inflation or the 'wrong duality' argument is needed, and the round-1 kill of v1 and #12's identification fail on the same point. Is that the cleaner obituary, and does the ontology half (monopoles of a gauge field in the p-sector) keep anything of Paul's original idea? (papers/broken-born-checkpoint-v2.md:45, :116, :217; notes/broken-born-theory.md:29; HANDOFF.md:32; popsci/universes-other-half.md:41)

- §11.1 kills the explanation because 'the relevant duality is electric–magnetic … not x↔p', while §11.3 calls the two frame choices one operation and conjectures one enlarged modular structure [O]. If OP8 succeeded, would the 'wrong duality' reason still stand, given that the second reason (inflation suffices) shows only that the explanation is unnecessary, not that it is false? (papers/broken-born-checkpoint-v2.md:114, :116, :120)

- Row 8 lists a permanent null as a 'Program requirement' with kill condition 'Direct detection', but the record supplies no mechanism of the program's own: the absence is due to inflation [T] and strong coupling [T]. Would a confirmed monopole of our U(1) contradict any postulate? If not, should the row become a consistency statement rather than a kill condition? (papers/broken-born-checkpoint-v2.md:116, :118, :172; wiki/predictions/monopole-null.md:63, :94)

- The 'only shadow' clause was written beside the dead '(p-polarized solitons)' rationale in #1 v0.1. #11 now attaches it to our monopoles in row 8 and to conjugate-sector solitons in §11.1. Synthesizer's note: the clause may be left over from the dead explanation, and 'right geometry, different flux' commits the program to no measurement. (notes/broken-born-theory.md:232; papers/broken-born-checkpoint-v2.md:116, :172)

- 'Alive and consequence-bearing' names no consequence beyond gravitation. The p-sector's gauge content is unspecified, and #13 says its 'Maxwell' cannot yet be written. Keep the ontology as a bare constraint (whatever is there gravitates), or tie it to a stated gauge structure for the p-sector? (papers/broken-born-checkpoint-v2.md:116; wiki/electric-magnetic-duality/conjugate-monopoles.md:41, :61; papers/conjugate-special-relativity.md:85)

- The plain-language text ('Two intuitions, one operation'; 'the same mathematical move'; §15's 'one structural unification') reads as a result, while §11.3 tags the unification [O]. #12 took the strong reading all the way to 'the magnetic side of electromagnetism'. Re-word the plain passages so they stop inviting that reading? (papers/broken-born-checkpoint-v2.md:16, :114, :120, :205; popsci/universes-other-half.md:41)

- The electric-sublattice clause is the only dynamical test of §11.3 the record ever specified ('deriving hypothesis H from that action would make the coupling a prediction'). The toy models met criterion 1 without it and contain no gauge field. Synthesizer's note: the smallest concrete version of OP8 would add a U(1) gauge field to the coset toy model and ask whether η's choice fixes its electric frame. (HANDOFF.md:35; notes/knot-dark-matter-standalone.md:110; notes/toy-lagrangian.md:6-9; papers/broken-born-checkpoint-v2.md:195; wiki/status/open-problems.md:145)

- The flag-28 audit shows that S (τ → −1/τ, θ = 0) maps our coupling to α_D = 4π/e² = 137.036, the e·g = 4π value, while 34 = 1/(4α) is the e·g = 2π Dirac minimum. §11.2 writes the S-dual expression beside the Dirac number, and #14 v2 needed 'the standard factor of four'. Flag 28 is a quick ruling; the same factor of 4 is the 'valid core' of round 2's objection about conventions. (review/wiki-build-checks/audit/flag28_recompute.out:26, :39-41; papers/broken-born-checkpoint-v2.md:118; git 8d588f6:import/knot-dark-matter-standalone.md:21; review/v3-worklog.md:28)

- ρ sits inside a continuous U(1) once only ω is rigid. S belongs to the discrete SL(2,ℤ), which no document names, and exact S-duality holds only with maximal supersymmetry. Synthesizer's note: [[0,1],[−1,0]] is the canonical swap for any two-dimensional symplectic pairing, so its recurrence may follow simply from both lattices being symplectic. What further fact would make it evidence of one structure? (papers/broken-born-checkpoint-v2.md:43, :118, :120; wiki/electric-magnetic-duality/modular-group.md:136, :158; notes/knot-dark-matter-standalone.md:31)

- v2.0 rested the topological clumping loophole on an unproven [O] ('solitons of p-local gauge theories are p-localized'). v2.1 calls it untested in §12 and closed in §14 item 8 of the same document. Paul could rule it either an open problem without a candidate or abandoned. (git 8d588f6:import/broken-born-checkpoint-v2.md:128; papers/broken-born-checkpoint-v2.md:154, :192, :215)

- The polarization order parameter has topology in the record: π₁(Λ(d)) = ℤ, ℤ₂ textures on a closed universe, and the toy model's two vacua ±K. Yet no document asks whether selecting the polarization in the early universe leaves defects. Synthesizer's note: this is the only route to a topological object that belongs to the program itself rather than to a borrowed hidden gauge sector, and so the only possible occupant of the loophole. (papers/broken-born-checkpoint-v2.md:66; notes/closed-universe.md:316; wiki/symmetry-breaking/topological-defects.md:196)

- Strict P4 was adopted by delegated decision on 2026-10-19, partly to close the monopoles' Witten-effect charge, on the same day the candidate was retired. It now carries row 7's permanent null for χ, and the reading of its ε ≲ 10⁻¹³ (ceiling or floor; hidden C exact or gauged) is unresolved. Worth an explicit ruling from Paul, who kept the veto? (review/round3-adjudication.md:99-112; papers/broken-born-checkpoint-v2.md:45, :171; wiki/history/documents/source-conflicts.md:101)

- Every referee across the three rounds on the monopole manuscript converged on 'the framework does no work'. After the obituary, every monopole statement in the program is dead, borrowed (row 8 rests on inflation), conditional (the ontology) or structural with an [O] (§11.3). Keep §11 as a structural remark, or invest in OP8 and the electric-sublattice clause? (review/round3-adjudication.md:135-137; review/round3/referee/audit-notes.md:241-247; papers/broken-born-checkpoint-v2.md:116-120, :172)

- The README line (also the public GitHub description), popsci #10's knots and #12's magnetic identification still present dead claims as live. Flag 37 needs only a tick, and no flag or queue item targets #10 or #12. (README.md:2; review/wiki-build-rulings.md:2605-2635; popsci/angle-of-the-mirror.md:37; popsci/universes-other-half.md:39-45, :73)

## Gaps

- The text of #14 v1 and the round-1 and round-2 referee reports are not in the repo: Paul holds the reports, and the arbitration code existed only in the chat. The v1 coupling argument and the referees' exact wording rest on HANDOFF's summary (HANDOFF.md:66, :77, :88-90).

- #11 §11, the v2.0 knot trilemma and App. A items 5 and 11 were all written on claude.ai before the 2026-10-19 import, so git cannot date them more finely (git 8d588f6; HANDOFF.md:60).

- Whether P.R.'s correction was 'the empty set' or 'measure zero' (papers/broken-born-checkpoint-v2.md:116 vs :217).

- What 'right geometry, different flux' commits the program to, and whether the Berry-curvature shadow belongs to our monopoles (row 8) or to conjugate-sector solitons (§11.1).

- What '17†-adjacent' means, which 't Hooft and Mandelstam papers are meant (no reference entry), and what source 'in the literature's own words' quotes. All wait on the queued † literature battery (papers/broken-born-checkpoint-v2.md:118, :120, :194).

- Whether strict P4's ε ≲ 10⁻¹³ is a ceiling or a floor, and whether hidden charge conjugation must be exact (#11:45) or gauged (review/round3-adjudication.md:102-103).

- Whether the p-polarized sector has gauge fields at all, and in which kinematics: #13's dual kinematics or ordinary relativistic QFT (papers/conjugate-special-relativity.md:85; review/v3-worklog.md:135-147; notes/knot-dark-matter-standalone.md:19).

- Whether §14 item 8's 'closed' abandons the topological loophole or only records that it has no candidate.

- HANDOFF.md:12 says 'Three blind AI reviews returned verdict B', but §6 records two completed rounds, both on the monopole manuscript #14, plus an incomplete third. The third B is unidentified.

- review/round3/referee/step4c.py and step4d.py are absent; only their .out files exist. The 0.828 figure is reproduced independently by verify/soliton_obituary.py:63; the reheating-temperature figure is not.

- Rulings 6 and 9 (the Witten-effect charge) were accepted without re-check, and the adjudicator did not re-run the Kibble–Zurek integration (review/round3-adjudication.md:32, :35, :38).

- Popsci #12's transparency figure ('some forty orders of magnitude below') has no executed check anywhere in verify/ or review/ (grep).

- None of the 44 entries in the rulings worksheet is ticked, so flags 21, 22, 28, 33, 34 and 37 stand confirmed but unruled. The GitHub description was last read on 2026-10-22.

- How #11 ranks its two accounts of our monopoles' absence, inflation (§11.1) and strong coupling (§11.2); the record does not say.

- The wiki's 'dead' verdict on #12's magnetic identification is the wiki's own reading of precedence; no review, ruling or program document addresses the claim.
