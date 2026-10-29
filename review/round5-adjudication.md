# Round 5 — adjudication

- **Manuscript:** `papers/phase-space-diameter.md` v1.0 (the
  phase-space-diameter note), SHA-256
  `2ed53d537d03c26273564cb4ed81b70117cc67853b08239a28149e927f3425a4`.
- **Pre-registration:** [round5-preregistration.md](round5-preregistration.md),
  written before dispatch and kept outside the repository until both referees
  had returned. Its SHA-256,
  `b5094b65cf969c8106353059e14bc8f66497076dfa3ae3ef262bda3a0fe3033b`, was
  recorded in `notes/phase-space-diameter-worklog.md` before dispatch and
  matches the file. Neither the pre-registration nor the manuscript was
  committed before the review: the session had no commit authorization
  until afterwards. Both were committed at Paul's request after the
  adjudication (97934f2, v1.1; f40e250, this record); the hash recorded
  before dispatch is the evidence that the forecast predates the reports.
- **Referees:** two blind subagents with Python and web, each given only a
  copy of the manuscript. Referee A followed the five-step protocol; referee
  B followed it with extra weight on §4, §7–§8 and prior art. Their notes,
  scripts and outputs are in [round5/referee-A/](round5/referee-A/) and
  [round5/referee-B/](round5/referee-B/). Every numerical indictment rests
  on executed code. Referee A could open neither Born paper. Referee B
  verified the Born 1938 quotations in the Internet Archive's scan of the
  volume and could not open Born 1949. Both papers were retrieved for the note
  (Born 1938 from the publisher's PDF in the Wayback Machine, Born 1949 from
  the American Physical Society's open copy); the copies' hashes are in the
  worklog.
- **The reviewed text:** v1.0 is kept as
  [round5/manuscript-v1.0.md](round5/manuscript-v1.0.md), the copy sent to
  the referees; its SHA-256 matches the one above.
- **My arbitration:** [round5/adjudicator/](round5/adjudicator/): `arb.py`,
  run from the repo root, with its output in `arb.out`.

## Verdict

**Both referees: B (flawed but salvageable), confidence 0.75. I agree.**

- Every number reproduced under the referees' own constants and code, and
  every literature citation resolves.
- Both referees found the same major gap: the note's one new number, the
  bound on the momentum graviton's range, uses a bimetric coupling formula
  without one of its parameters.
- It is repairable, and the repair (R1) makes the bound's premise explicit
  instead of removing it.

## Rulings

| # | Finding | Ruling | Evidence |
|---|---|---|---|
| R1 | §8.2: the Yukawa strength in Hassan–Rosen bigravity is α = (4/3)(M_f c/M_g)², with c the ratio of the two frames' backgrounds (f̄ = c²ḡ). The note's "α = 4/3 at equal Planck masses" drops c, so the bound λ_X < 37.7 μm holds only for c = 1, which the note never states (A, B) | **Upheld in substance**; referee A's value of c **not upheld** | Both cited equations carry c (Lüben et al. eq. 9; Enander–Mörtsell eq. 4.1). `arb.py`: with the palindromic couplings the proportional-background equation factorizes as c(c − 1)(c + 1)(β₁c² + (3β₂ − β₀)c + β₁), as referee B found. The program's vacuum is the aligned point 𝕏 = √(g⁻¹f) = 1, i.e. c = 1, where its vacuum-energy identity is derived (`notes/beta-coefficients.md` §1–§2). That is also the argument B asked for: on the program's flat branch (β₀ = −4β₁ − 3β₂) the symmetry-breaking pairs (c, 1/c) exist only for β₁ < 0 < \|β₁\| < β₂, and there Λ_g is of the order of the spin-2 mass squared (Λ_g/2(β₁ + β₂) = −1.14 and −70.9 at β₁ = −1, β₂ = 2), which is (M_X/H₀)² = 1.3×10⁶¹ times H₀² for M_X c² ≥ 5.24 meV. So the aligned vacuum is the only one compatible with the observed Λ. What stays open is whether the aligned point persists as the universe expands, since the second frame f = E₀[J] lies on a compact moduli space (`notes/tuning-test.md` §4) and so, on the note's reading, has no scale of its own. The bound as a function of c: 57.0 μm (c = 0.5), 47.2 (0.67), 42.5 (0.8), 37.7 (1), 30.8 (1.5); X at 47.1 μm is allowed only for c < 0.672, at 84.0 μm only for c < 0.302. Referee A set c₀ = ã₀/a₀ from a·ã = 1, which gave α ~ 10⁻¹⁸⁶. The record's second frame is the polarization frame, not the slaved momentum block g̃ = g⁻¹ that carries ã, so that value does not follow. The record also leaves open how reciprocity's action as frame exchange relates to its action as Z → −Z⁻¹ (audit item 39 in `review/wiki-build-flags.md`), so v1.1 states that relation as open rather than ruling out referee A's identification on that ground. |
| R2 | §4: the closeness of the radiation's per-axis count (1.0×10³⁰) to FKGLM's per-dimension count (4.3×10³⁰) "holds at no other epoch" (A, B) | **Upheld** | `arb.py`: for the note's fixed comoving region both counts are conserved, so their ratio, 0.235, is constant. For a Hubble sphere in the radiation era, S^{1/3}/S_BH^{1/4} = 0.79–1.05 (g = 3.36 to 106.75) at every temperature, because the radiation nearly saturates CKN's S_max ≃ S_BH^{3/4} (their eq. 3; S/S_BH^{3/4} = 0.49–1.17). The sentence is replaced by the CKN explanation. |
| R3 | §2 table: the "one cell" row, with momentum ħ/w, has area ħ, not h (A) | **Upheld** | `arb.py`: ħ = 0.159 h. The momentum side becomes h/w, the de Broglie momentum. |
| R4 | §3: the cosmic event horizon's 2.6×10¹²² k is in Egan–Lineweaver's Table 2, not Table 1 (A, B) | **Upheld** | Both referees, from the arXiv source. |
| R5 | §5: Bhattacharyya et al. do not call complexity a "clock"; it grows linearly with e-folds during inflation and decreases in the radiation era (A, B) | **Upheld** | Both referees, from the arXiv source. The "clock" reading is credited to the squeezing literature itself (Albrecht et al. 1994: R_k ≃ ln a/a₁ₓ). |
| R6 | §7: the TeV square omits the g_s correction that §6 applies, and 1.7 TeV is √(k_BT₀E_P), not Berglund–Hübsch–Minic's geometric mean (A, B) | **Upheld** | `arb.py`: 1.671 TeV for photons alone, 0.963 TeV with g_s; √(k_BT₀E_P) = 1.693 TeV; √(ρ_Λ^{1/4}E_P) = 5.23 TeV. |
| R7 | §7: "halves the exponent" (A, B) | **Upheld** | `arb.py`: log₁₀(Λl_P²) = −121.55, log₁₀(λ/l_P) = 30.51: a fourth root. |
| R8 | §7: Λ = 3l_P²/λ⁴ is attributed to BHM, who write λ_cc = l_P²/l_Λ⁴ without the 3 (A) | **Upheld** | Referee A, from the arXiv source. |
| R9 | §7: the CKN conventions "between 0.45 and 2.1" need the 2.1's assumption stated (A) | **Upheld** | `arb.py`: 0.4466 (reduced Planck mass), 0.5878 (sphere), 0.8409 (cube), 2.0837 (one scalar's zero-point energy Λ⁴/16π²). |
| R10 | §4, §7: Mignemi 2010 writes no geometric-mean length and does not call the duality Born's (A, B) | **Upheld** | Both referees, from the arXiv source. The explicit prior art is Bambi–Urban 2008, whose map of the extended uncertainty relation has scale (α/β)^{1/2}L_X L_Pl with L_X = L_Λ, and Bolen–Cavaglià 2005, which motivates the same relation by "the symmetry of the symplectic space". |
| R11 | §6: "no turnaround as written" assumes spatial flatness (A) | **Upheld** | A closed universe can turn around with V ≥ 0. The program's cosmology is flat (`papers/broken-born-checkpoint-v2.md` §10); v1.1 says so. |
| R12 | §8.2: the interpolation's anchors validate the \|α₉₅\| column, while 37.7 μm comes from the +α₉₅ column (B) | **Upheld (wording)** | `arb.py`: the \|α₉₅\| column gives 38.63 μm (α = 1) and 30.23 μm (α = 8/3), the published values; at α = 4/3 it gives 35.79 μm, the +α₉₅ column 37.68 μm. Both columns come from the same table, so the anchor checks the transcription and the method; the note now says which column it uses and why (the attractive, one-sided limit, which is the more conservative). |
| R13 | §5: Gabor's "self-reciprocal" refers to Gaussian pulses of any sharpness, not to the one fixed point (B) | **Upheld** | Referee B, from the scan (p. 435). |
| R14 | §6: the survey of readings misses the squeezed-mode reading (r = 105.9 gives 10⁹²), the convention dependence of the \|Z\| = 1 apex, §8.4's step at the §6 epoch, and the infinite Hubble-sphere elongation at a true bounce (B) | **Accepted** | `arb.py`: e^{2r} = 10^{86.9}–10^{104.2} for r = 100–120 and 10^{92.0} at r = 105.9; with Im Z ∝ a⁻² the apex of \|Z\| = 1 is a minimum of a, with a² = Im Z a maximum. None of these changes the withdrawal: the squeezed mode was round before it left the Hubble radius during inflation, not at a bounce, and the \|Z\| = 1 geometry is excluded under either convention. |
| R15 | Omitted prior art (A, B): Bambi–Urban and Bolen–Cavaglià for the self-dual length; Sundrum 2004 and Kapner et al. 2007 for a gravitational-strength modification at the dark-energy length, tested by torsion balances; Li 2004 for holographic dark energy; Kiefer–Polarski's reading of squeezing as an e-fold count (B), for which v1.1 cites Albrecht et al. 1994, where the e-fold law is derived; Veneziano 1991, Gasperini–Veneziano 1993 and Brandenberger–Vafa 1989 for self-dual bounces; Hur et al. 2025 for dual-spacetime dark energy; CKN's eq. 3 | **Accepted** | All retrieved for this note in chunk 1 except where marked; added with [S]. Not added: Beane 1997, Jarvis–Morgan 2008 and Kounnas–Partouche–Toumbas 2012, which were not retrieved. |
| R16 | Omitted constraints (A, B): in bigravity a heavy spin-2 at equal Planck masses needs the potential's vacuum energy, of order M_X²M_P², cancelled; bimetric cosmologies have gradient instabilities while H exceeds the spin-2 mass; the bound assumes a single Yukawa term | **Accepted, as caveats** | In the program the cancellation is the palindrome identity at the aligned point; the early-universe stability is open in the record (`review/v3-worklog.md` item R7); other light fields could add Yukawa terms. |

**Minor items accepted without separate rulings:** the rounding of 5.2×10⁹² in
the plain abstract; "the length scale of dark energy" for 47–52 μm, which is
within a factor of two of it; §8.4's normalization being a choice; the year
of Bedroya–Vafa (JHEP 2020); Born 1938's own question whether b is universal
or set by the system, which anticipates FKGLM's contextual λ; §4's last
sentence, which conflated FKGLM's momentum cutoff (ħ/√(ℓℓ_P)) with the
Planck momentum.

**Author-found items (my reread during the review, before the reports):**

1. §5: "the circle meets a·ã = 1 only at Z = i" should say that a·ã = 1 holds
   along the slice and the circle meets the slice only at Z = i.
2. §5: det H = 1 is not one of the record's "self-duality" loci; the list is
   of the sets that appear in the record's statements about self-duality.
3. §3: "before that" read as "before annihilation"; the comoving entropy is
   conserved throughout, from reheating on.
4. §6: the |Z| = 1 paragraph's second failure needs to say that 10⁹² is
   there read as the squeeze of H along the circle.
5. §8.1: the metastring sentence is sharpened to its source: ħ = λε and
   G_N = ρλ/ε, so λ² = ħG_N/ρ.

## Pre-registration scored

| Prediction | Outcome | Score |
|---|---|---|
| Verdict B from both | B and B, confidence 0.75 each | **Hit** |
| Weakest link: the bound in §8.2 inherits the unreviewed coupling premise (equal Planck masses, α = 4/3) | Both referees: §8.2's α = 4/3 omits the background ratio c | **Hit** on location and premise; the mechanism, a dropped parameter of the cited formula, was not foreseen |
| Runner-up 1: the obituary — a surviving reading, or the \|Z\| = 1 origin paragraph read as speculation | B: the survey of readings is incomplete and the apex is convention-dependent; none changes the withdrawal | **Partial** |
| Runner-up 2: "the program fixes no λ" rests on unavailable documents | Not raised | Miss |
| Runner-up 3: §8.4 and §8.5 conditional to the point of carrying no content | A: §8.4 in tension with §8.2 (through the value of c, not upheld); B: §8.4's step sits at the §6 epoch; §8.5 not attacked | **Partial** |
| Arithmetic: zero surviving numerical indictments; if one, a convention (κ, CKN factor, ±α₉₅ column, g_* at T_P, ħ against h cells) | Five minor ones survive (R3, R6, R7, R9, R12), four of them in conventions listed | **Miss on count; hit on kind** |
| Citations: all resolve; likeliest over-cited Ohsawa or de Gosson, Slepian, Egan–Lineweaver, the Mignemi sentence, the Lee interpolation | All resolve. Over-cited: Egan–Lineweaver (table), Mignemi, the Lee interpolation column; also Bhattacharyya et al. and Gabor, not foreseen | **Hit** on resolution; three of five predicted, two not |
| Novelty: no prior art for the self-dual length beyond what the note cites | Bambi–Urban and Bolen–Cavaglià (explicit), Sundrum and Kapner et al. (the test at the dark-energy length), Albrecht et al. (the e-fold clock), string cosmology (self-dual bounces) | **Miss** |

Calibration across rounds:

- Verdicts: 2/2 (rounds 1–2), miss (round 3), hit (round 4), hit (round 5).
- Weakest-link location: hit in rounds 4 and 5.
- Still underestimated: the number of small errors in a long text, and the
  extent of prior art.

## Lessons (into CLAUDE.md)

1. When a result rests on a formula from the literature, carry every
   parameter the cited formula has, and state what fixes each one. Round 5
   found a dropped background ratio in a bimetric coupling.
2. A claim about how a quantity behaves over time ("holds at no other
   epoch") needs executed code like any number. Round 5 found one that a
   two-line calculation refutes.

## Revisions for v1.1 (all accepted; applied 2026-10-26)

v1.1 writes the background ratio as u (c in the cited papers and in the
referees' reports), to keep it apart from the speed of light.


1. **§8.2:** write α = (4/3)(M_f c/M_g)²; state the program's vacuum, c = 1,
   and the argument for it (R1); give the bound as a function of c and the
   values of c below which X at the self-dual length survives; say which
   column of the exclusion table is used and why; state that whether the
   aligned point persists in an expanding universe is open, that the second
   frame is not the slaved momentum block, and that how reciprocity's two
   actions relate is open in the record; add the caveats of R16. Carry the
   condition c = 1 into the abstracts, §8's opening and §9.
2. **§4:** replace "holds at no other epoch" by the CKN explanation (R2);
   fix the last sentence (FKGLM's momentum cutoff); add Born's question
   whether b is universal.
3. **§2:** the one-cell row's momentum side is h/w (R3).
4. **§3:** Egan–Lineweaver's Table 2 for the horizon (R4); the entropy
   sentence (author item 3).
5. **§5:** Gabor's "self-reciprocal" (R13); credit the e-fold count of
   squeezing to Albrecht et al. and drop "clock" for complexity (R5); fix
   author items 1 and 2.
6. **§6:** add the squeezed-mode reading, the convention dependence of the
   |Z| = 1 apex, the infinite Hubble-sphere elongation at a true bounce and
   the string-cosmology bounces (R14, R15); state flatness (R11); fix author
   item 4.
7. **§7:** Bambi–Urban and Bolen–Cavaglià as the explicit prior art, Mignemi
   as an implicit one (R10); the CKN conventions spelled out (R9); the
   fourth root (R7); BHM's form without the 3 (R8); the TeV numerology
   corrected (R6); Sundrum, Kapner et al. and Li (R15).
8. **§8.1:** the metastring sentence (author item 5); Gibbons and Caianiello
   beside Low.
9. **§8.4:** the step's epoch must lie before nucleosynthesis; it coincides
   with the §6 square for the region-scale unit, which is not a bounce (R14).
10. **References** and `verify/phase_space_diameter.py`: every new number
    gated; every new citation retrieved.

## Recommendations to Paul

- **Flags 23 and 24** (`review/wiki-build-flags.md`), still awaiting a
  ruling: the note's §5 and §6 support accepting both. a·ã = 1 is
  det H = 1 on the whole slice X = 0; |Z| = 1 is the locus of square
  rectangles; Z = i is the self-dual point; and the diameter relation's
  square is not at the turnaround.
- **Leads found by the literature sweep, outside this note:** Low 2006 is
  prior art for #13's maximum force. Lukierski, Meljanac, Mignemi and Pachoł
  (PLB 847, 138261, 2023) break an algebra containing a continuous Born
  rotation spontaneously in the Yang model, which bears on the toy note's
  "no explicit model of ρ itself being spontaneously broken". Shlivko and
  Steinhardt 2024 and Hur et al. 2025 bear on reading DESI's CPL quadrant
  against #11 §10's strict w ≥ −1.
