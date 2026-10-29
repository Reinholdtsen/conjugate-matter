---
title: "Round 5"
weight: 80
status: record
description: "The blind review of the phase-space-diameter note on 2026-10-26: two referees, the forecast kept outside the repository and hashed, verdicts B and B, the major ruling on the dropped background ratio (upheld in substance; referee A's value not upheld), the other rulings, the forecast scored, two lessons, and version 1.1, which carries out every accepted revision."
sources:
  - "review/round5-adjudication.md"
  - "review/round5-preregistration.md"
  - "review/round5/referee-A/audit-notes.md Step 1–Step 5"
  - "review/round5/referee-B/audit-notes.md Step 1–Step 5"
  - "review/round5/adjudicator/arb.out"
  - "papers/phase-space-diameter.md header"
  - "papers/phase-space-diameter.md §1"
  - "papers/phase-space-diameter.md §4"
  - "papers/phase-space-diameter.md §6"
  - "papers/phase-space-diameter.md §7"
  - "papers/phase-space-diameter.md §8.2"
  - "papers/phase-space-diameter.md 'References'"
  - "review/round5/manuscript-v1.0.md"
  - "notes/phase-space-diameter-worklog.md"
  - "verify/phase_space_diameter.py"
  - "CLAUDE.md 'Since the handoff (2026-10-19)'"
  - "CLAUDE.md 'Method (HANDOFF §5)'"
  - "HANDOFF.md §4"
  - "HANDOFF.md §8"
  - "notes/beta-coefficients.md §1–§2"
  - "notes/tuning-test.md §4"
  - "review/v3-worklog.md"
  - "review/wiki-build-flags.md items 23, 24, 38, 39"
  - "notes/closed-universe.md §2"
  - "notes/closed-universe.md §6"
  - "review/wiki-build-flags.md items 50, 51"
---

*Round 5 was the blind review of the phase-space-diameter note, `papers/phase-space-diameter.md`, which tests a relation recorded only in the program's early chat between the size of the universe in position and its size in momentum, and works through what Born reciprocity adds to it. Two fresh referees that could execute code each received only a copy of the note's version 1.0. Both reproduced every number, and both graded the note B, flawed but salvageable. Both found the same major gap: the note's one new number, a laboratory bound on the range of the program's momentum graviton, rested on a formula from bimetric gravity quoted without one of its parameters, the ratio of the two metrics' backgrounds. The author upheld the finding in substance, repaired the bound by stating that ratio, the program's argument for its value and the bound at other values, and did not uphold one referee's value for it. The forecast, written before dispatch and kept outside the repository with its hash recorded, had named the verdict and the place of the weakest link. Version 1.1 of the note applied the accepted revisions the same day, and the round added two rules to the project's method.*

**Status:** Record — untagged. The record is `review/round5-adjudication.md` and `review/round5-preregistration.md`, with each referee's notes, scripts and outputs in `review/round5/referee-A/` and `review/round5/referee-B/` and the arbitration in `review/round5/adjudicator/`. The text the referees reviewed is kept as `review/round5/manuscript-v1.0.md`. The revisions were applied on 2026-10-26 in the note's version 1.1 ([below](#the-revisions-and-version-11)). The pre-registration records that it was not committed, and the adjudication gives the same reason: "this session had no commit authorization".

## The manuscript under review

The note answers a question Paul put on 2026-10-26: "Investigate or explain if there is a relationship between the size of our universe in position space and momentum space. Speculate and work through the consequences if so." (`notes/phase-space-diameter-worklog.md`). It writes up [the phase-space diameter relation](/wiki/cosmology/scale-factor-duality/phase-space-diameter), one bullet of `HANDOFF.md` §4, the results that existed only in the chat, which the handoff had listed among its "Optional write-ups" (§8 item 7) and the root `CLAUDE.md` had queued as the third part of its first item.

The text sent to the referees was version 1.0. The adjudication identifies it by its hash (`SHA-256`), `2ed53d537d03c26273564cb4ed81b70117cc67853b08239a28149e927f3425a4`, which the worklog recorded before dispatch, and it keeps that text as `review/round5/manuscript-v1.0.md`, "the copy sent to the referees", whose hash matches the recorded one. The file in `papers/` is version 1.1; the referees' notes quote version 1.0 where they cite it. Its claims, as its technical abstract summarizes them and as version 1.1 keeps them:

- the chat's D_x·D_p = h·N^{1/3} is, for blackbody radiation in a sphere, an identity, D_x·D_p = κ h N_γ^{1/3} with κ = 1.708 [D][V], constant for a fixed comoving region [T], and the program's constraint a·ã = 1 fixes the area of one cell, not the number of cells, so the relation cannot test the program;
- [Born reciprocity](/wiki/phase-space/reciprocity/born-reciprocity) keeps a rectangle's area and inverts its aspect ratio, and on Gaussian states it acts as Z → −Z⁻¹ ([Gaussian wave packets on the Siegel half-plane](/wiki/phase-space/modular-field/gaussian-states));
- the claim "square exactly at the bounce" is withdrawn ([Obituary: the square rectangle at the bounce](/wiki/cosmology/scale-factor-duality/square-at-the-bounce));
- the box from the Planck length to a length L, with the matching momenta, is self-dual for the Born length √(l_P L), 47–84 μm, a length already in the literature ([the self-dual cosmic box](/wiki/cosmology/scale-factor-duality/self-dual-cosmic-box));
- that length can be neither the Born length of #13 nor the range of [the momentum graviton X](/wiki/gravity/momentum-graviton) ([Obituary: the self-dual length as a program scale](/wiki/cosmology/scale-factor-duality/self-dual-length-obituary));
- torsion balances bound X's range below 37.7 μm, M_X c² > 5.2 meV ([the laboratory bound on X's range](/wiki/gravity/momentum-graviton/range-bound)).

Version 1.0 stated the last claim as following from equal Planck masses alone. The referees quote it: "At equal Planck masses alpha = +4/3" (referee A, Step 4) and "M_X c² > 5.2 meV, whatever sets it" (referee B, Step 4). The program documents the note cites as premises ([H1], [H2] and [P1]–[P4] in its list) were not available to the referees.

## The forecast

The pre-registration was written before dispatch and "kept outside the repository, in the session scratchpad, until both referees had returned, so that neither could read it. It is not committed: this session has no commit authorization." Its hash, `b5094b65cf969c8106353059e14bc8f66497076dfa3ae3ef262bda3a0fe3033b`, and that of the manuscript copy were written into the worklog "and into the session transcript before dispatch". The worklog's entry, "recorded before dispatch", ends "dispatched 2026-10-26T15:55-07:00", and the adjudication confirms that the recorded hash "matches the file" ([pre-registration and its calibration record](/wiki/method/review/pre-registration#round-5)).

It forecast (`review/round5-preregistration.md`, 'Predictions'):

- **Verdict B from both referees**, confidence medium. "Not C: every number is gated by a script and matched by an independent recomputation; most claims are standard physics tagged [T] with retrieved sources; the speculative identifications are tested and rejected in the text." "Not A: the program-specific content is thin, and a note this long will have attribution or wording errors that a referee counts as flaws."
- **Weakest link: the bound on X in §8.2.** "It inherits the program's own, unreviewed premise that X couples to ordinary matter at gravitational strength (equal Planck masses, α = 4/3), which the referee cannot check. A referee may also call the bound vacuous for any plausible M_X."
- **Runners-up**, in order: the obituary of §6, where "A referee proposes a reading of 'the bounce' or of N under which the claim survives, or calls the |Z| = 1 'origin' paragraph speculation presented as diagnosis"; "'The program fixes no λ' (§5) rests on documents the referee cannot see"; and that §8.4 and §8.5 "are conditional to the point of carrying no content".
- **Arithmetic:** "zero surviving numerical indictments. If one survives, a convention: κ's definition, the CKN factor, the one-sided against two-sided α₉₅ column, `g_*` at the Planck temperature, or the 2π between cells of area ħ and h." CKN is the Cohen–Kaplan–Nelson bound.
- **Citations:** "all literature citations resolve", with the likeliest cited for more than they say "Ohsawa or de Gosson for the Fourier transform as Z → −1/Z; Slepian 1983; the Egan–Lineweaver numbers; the location of the quoted Mignemi sentence; the Lee thesis interpolation."
- **Novelty**, a part the earlier forecasts did not have: "no prior art for the self-dual length beyond what §4 and §7 already cite; possibly prior art for |Z| = 1 ⟺ Δx = Δp, or for de Sitter space as a self-dual state."

Its stated limitation: "same model family as the author. The program documents the note cites ([H1], [H2], [P1]–[P4]) are unavailable to the referees, so the premises taken from them can be checked for consistent use only."

## What the referees did

The referees were "two fresh subagents with shell, Python (numpy, sympy, mpmath) and web", each given "only a copy of the manuscript and the protocol" and "told to read nothing else on the machine" (pre-registration). Referee A followed "the five-step protocol of rounds 3 and 4"; referee B followed it "weighted towards §4 and §7–§8 and towards prior art" ([the blind-review protocol](/wiki/method/review/review-protocol)). Each states its isolation in its notes: referee A, "only manuscript.md and files created here were read"; referee B, "I read only the manuscript copy and my own files." Both treated the program documents as premises, and both kept downloaded literature in a folder of its own, read as untrusted data. The notes, scripts and outputs are in the repository; the downloads are not.

### Citations

Referee A checked the bibliographic data of every reference through arXiv's metadata for all 33 arXiv numbers, Crossref and INSPIRE, and searched the full texts for each quoted statement (Step 1). Referee B checked every record against INSPIRE or Crossref: "All 37 entries match title, authors, journal, volume, page/article and year as given." Between them they found the quoted sentences of Freidel–Kowalski-Glikman–Leigh–Minic (FKGLM), Berglund–Hübsch–Minic (BHM), Cohen–Kaplan–Nelson (CKN), Bousso, Lee et al., Grosse–Wulkenhaar, Padmanabhan and others verbatim in their sources.

Access differed. Referee A could not open Born 1938 or Born 1949, both "blocked by a Cloudflare challenge", and found no open copies of Gabor 1946 or Slepian 1983. Referee B read Gabor from a scan and Born 1938 from the Internet Archive's scanned text of the volume, and verified the note's Born quotations there, including Born's definition of b through the classical electron radius; for Born 1949 it found no accessible full text, so "Born 1949's 'ħ = ab' could not be checked." The adjudication's header records the same: "Referee A could open neither Born paper. Referee B verified the Born 1938 quotations in the Internet Archive's scan of the volume and could not open Born 1949." Both papers had been retrieved for the note, Born 1938 as the publisher's file archived in the Wayback Machine and Born 1949 as the American Physical Society's open copy, and the copies' hashes are in the worklog ([the † literature battery](/wiki/method/literature-battery)). The worklog's entry of 17:55 lists this statement among the source findings of the wiki's writers that were fixed after the wiki was written: "the adjudication's statement on the referees' access to Born corrected".

The citation step produced these findings, taken up under [the rulings](#the-rulings):

- both cited bimetric formulas carry a parameter the note dropped (both referees);
- the event horizon's entropy is in Egan and Lineweaver's Table 2, not Table 1 (both);
- Bhattacharyya et al. never call circuit complexity a clock (both);
- Mignemi writes no geometric-mean length and does not call the duality Born's (both);
- Gabor's "self-reciprocal" refers to the family of Gaussian pulses, not to its one Fourier-invariant member (B);
- Bambi and Urban's extended uncertainty relation already contains the self-dual length, uncredited in §7 (both);
- Born 1938 asks whether b is universal or set by each system, which the note did not mention (B).

### Numbers and re-derivations

Each referee recomputed every number of the note with constants it chose and code it wrote; [the phase-space-diameter script](/wiki/method/verification/phase-space-diameter-script) gives their inputs. Referee A: "All of the following reproduce to the quoted precision" (Step 2). Referee B: "every number in the manuscript reproduced from my own inputs …; none wrong beyond rounding" (Step 5). The discrepancies they reported were of convention and wording: the TeV numerology of §7 without the Standard Model's species count (both); "This halves the exponent", where the exponent is quartered (both); the CKN conventions' upper factor, 2.1, which needs an unstated assumption (A); the area of the "one cell" row of §2, ħ rather than h (A); and an anchor that validates one column of the exclusion table while the bound uses the other (B).

Both re-derived the note's identities symbolically and numerically (Step 3): the coefficient κ from the Bose integrals, the closed forms of the square, ρ_λ on rectangles, the Fourier statement Z → −1/Z on Gaussians with the Fubini–Study factor of 1/8, the box's aspect ratio √Ω_Λ(t) and the exchange a → C/a. Both also derived the Yukawa strength of [Hassan–Rosen bimetric gravity](/wiki/gravity/spin-2-fields/hassan-rosen-bimetric) by splitting the two metrics into a massless and a massive mode. Referee A: "alpha = 4 M_f^2 c^2 / (3 M_g^2); = 4c^2/3 at M_f = M_g; = 4/3 only if also c = 1. Agrees with Lueben et al. eq. 9 and Enander-Moertsell eq. 4.1; disagrees with the manuscript's alpha = (4/3)(M_f/M_g)^2, which omits c^2." Referee B found the manuscript's form "for proportional backgrounds with unit ratio", with the general linear result "(4/3)(M_f/M_g)²c²".

In these quotations c is the ratio of the two metrics' backgrounds, f̄ = c²ḡ, the letter of the cited papers. Version 1.1 writes it u, to keep it apart from the speed of light, and this page writes u outside quotations.

### Conceptual audit

Referee A (Step 4) marked the Yukawa strength as its one major finding and added two constraints from the same bimetric literature: that a spin-2 field far heavier than H₀ at equal Planck masses needs a vacuum energy of order M_X²M_P² tuned away, and that bimetric cosmologies are unstable while H exceeds the spin-2 mass. It found the §4 sentence "it holds at no other epoch" false "under every reading I could construct". On the withdrawn claim: "The withdrawal holds under every reading. The obituary's 'What survives' is accurate." It listed omitted prior art: Bambi–Urban, CKN's eq. 3, the torsion-balance tests of Kapner et al. "below the dark-energy length scale", Sundrum's "fat graviton", Li's holographic dark energy, and Gibbons and Caianiello beside Low on a maximal force.

Referee B (Step 4) called the background ratio "Unstated, and load-bearing" and rated it "major (fixable)": "In a program whose central premise is spontaneously broken reciprocity this needs to be stated and argued." It noted that the bound assumes a single Yukawa term. It constructed four readings of the withdrawn claim (a squeezed perturbation mode; the scale-factor duality of §8.4; the Hubble sphere at an actual bounce; the |Z| = 1 geometry under the opposite convention) and judged: "withdrawn under every reading I could construct; the treatment is fair in its conclusion but incomplete in its coverage (S1, S2) and in one convention (S4)." Its prior-art list added string cosmology's self-dual bounces and the dynamical Born-geometry dark energy of Hur et al. 2025, among others.

### Verdicts

- **Referee A:** "Verdict: B (flawed but salvageable). Confidence 0.75." Weakest link: "section 8.2, 'At equal Planck masses alpha = +4/3'. In Hassan-Rosen gravity the strength is (4/3)(M_f c/M_g)^2. c is never fixed."
- **Referee B:** "B (flawed but salvageable), confidence 0.75." Weakest link: "the premise α = 4/3 in §8.2 (equal Planck masses ⇒ α = 4/3 only for proportional backgrounds with ratio c = 1), which carries the manuscript's only new number."

## The rulings

The adjudication: "**Both referees: B (flawed but salvageable), confidence 0.75. I agree.**" It adds: "Every number reproduced under the referees' own constants and code, and every literature citation resolves", "Both referees found the same major gap: the note's one new number, the bound on the momentum graviton's range, uses a bimetric coupling formula without one of its parameters", and "It is repairable, and the repair (R1) makes the bound's premise explicit instead of removing it." The arbitration script is `review/round5/adjudicator/arb.py`, with its output in `arb.out`.

### R1: the background ratio

The finding, from both referees: "§8.2: the Yukawa strength in Hassan–Rosen bigravity is α = (4/3)(M_f c/M_g)², with c the ratio of the two frames' backgrounds (f̄ = c²ḡ). The note's 'α = 4/3 at equal Planck masses' drops c, so the bound λ_X < 37.7 μm holds only for c = 1, which the note never states". The ruling: "**Upheld in substance**; referee A's value of c **not upheld**".

The evidence, in the adjudication's order:

1. **The formula.** "Both cited equations carry c (Lüben et al. eq. 9; Enander–Mörtsell eq. 4.1)."
2. **The program's vacua.** With the palindromic couplings βₙ = β₄₋ₙ ([the palindrome](/wiki/gravity/palindromic-branch/palindrome)), the equation for proportional backgrounds factorizes as u(u − 1)(u + 1)(β₁u² + (3β₂ − β₀)u + β₁), "as referee B found". "The program's vacuum is the aligned point 𝕏 = √(g⁻¹f) = 1, i.e. c = 1, where its vacuum-energy identity is derived" (calc note #8, `notes/beta-coefficients.md` §1–§2; [the vacuum-energy identity](/wiki/gravity/palindromic-branch/vacuum-energy-identity)).
3. **Why that vacuum and no other**, "the argument B asked for". On the program's flat branch, β₀ = −4β₁ − 3β₂, the symmetry-breaking pairs (u, 1/u) "exist only for β₁ < 0 < |β₁| < β₂, and there Λ_g is of the order of the spin-2 mass squared (Λ_g/2(β₁ + β₂) = −1.14 and −70.9 at β₁ = −1, β₂ = 2), which is (M_X/H₀)² = 1.3×10⁶¹ times H₀² for M_X c² ≥ 5.24 meV. So the aligned vacuum is the only one compatible with the observed Λ." Flag 51 in `review/wiki-build-flags.md` adds that the branch also needs β₁ > 0, which no document states: for β₁ = 0 the aligned branch is bounded, and for β₁ < 0 it ends at a broken vacuum with negative Λ_g and a Higuchi ghost ([the momentum graviton in a closed universe](/wiki/gravity/momentum-graviton/closed-universe#β--0-is-required-dv)).
4. **What stays open.** "whether the aligned point persists as the universe expands, since the second frame f = E₀[J] lies on a compact moduli space with no scale of its own" (citing calc note #7, `notes/tuning-test.md` §4). The calc note places E₀[J] on the compact moduli space; version 1.1 of the note marks the rest as its own reading: E₀[J] "lies on a compact moduli space [P5, §4] and so, on this note's reading, carries no scale of its own" (§8.2).
5. **The bound at other ratios.** "57.0 μm (c = 0.5), 47.2 (0.67), 42.5 (0.8), 37.7 (1), 30.8 (1.5); X at 47.1 μm is allowed only for c < 0.672, at 84.0 μm only for c < 0.302."
6. **Referee A's value, not upheld.** Referee A had taken the second frame's background to follow the momentum scale factor ã of a·ã = 1, normalized as in the note's §8.4, which made the ratio of order 1/A₀ today, A₀ being the radiation rectangle's aspect ratio, and X's force negligible. The ruling: "Referee A set c₀ = ã₀/a₀ from a·ã = 1, which gave α ~ 10⁻¹⁸⁶. The record's second frame is the polarization frame, not the slaved momentum block g̃ = g⁻¹ that carries ã, so that value does not follow."
7. **A related open point.** "The record also leaves open how reciprocity's action as frame exchange relates to its action as Z → −Z⁻¹ (audit item 39 in `review/wiki-build-flags.md`), so v1.1 says so rather than ruling the identification out." ([two actions of reciprocity](/wiki/gravity/momentum-graviton/spectrum-and-parity#two-actions-of-reciprocity)).

Version 1.1 states the coupling as α = (4/3)(M_f u/M_g)², notes that "Only the product M_f u is fixed by the theory, so equal Planck masses give α = 4/3 only if u = 1", gives the argument for u = 1 and the bound at other values, and says that the second frame "is not the slaved momentum block g̃ = g⁻¹ that carries ã (§5), so a·ã = 1 does not fix u" (§8.2). The condition is carried into both abstracts, §8's opening and §9, where the bound holds "in the aligned vacuum (u = 1, α = 4/3)" ([the laboratory bound on X's range](/wiki/gravity/momentum-graviton/range-bound)). The arbitration's figures that version 1.1 states are gated in `verify/phase_space_diameter.py`.

### R2: the per-axis counts

The finding (A, B): the closeness of the radiation's per-axis count, 1.0×10³⁰, to FKGLM's per-dimension count, 4.3×10³⁰, "holds at no other epoch". The ruling, "**Upheld**": for the note's fixed comoving region "both counts are conserved, so their ratio, 0.235, is constant. For a Hubble sphere in the radiation era, S^{1/3}/S_BH^{1/4} = 0.79–1.05 (g = 3.36 to 106.75) at every temperature, because the radiation nearly saturates CKN's S_max ≃ S_BH^{3/4} (their eq. 3; S/S_BH^{3/4} = 0.49–1.17). The sentence is replaced by the CKN explanation." This finding produced the round's second lesson.

### The other rulings

Every finding was upheld or accepted, R1 with referee A's value of u not upheld. The qualifiers in the ruling column are the adjudication's.

| # | Finding | Ruling | In version 1.1 |
| --- | --- | --- | --- |
| R3 | the "one cell" row of §2 has area ħ, not h (A) | Upheld | the momentum side is h/w, the de Broglie momentum |
| R4 | the horizon's 2.6×10¹²² k is in Egan–Lineweaver's Table 2 (A, B) | Upheld | Table 2 |
| R5 | Bhattacharyya et al. do not call complexity a "clock"; it grows during inflation and decreases in the radiation era (A, B) | Upheld | the e-fold reading of squeezing credited to Albrecht et al. 1994 |
| R6 | the TeV square omits the species count that §6 applies, and 1.7 TeV is √(k_BT₀E_P), not BHM's geometric mean (A, B) | Upheld | 1.0 TeV with the Standard Model's species; the two geometric means kept apart |
| R7 | "halves the exponent" (A, B) | Upheld | "takes the fourth root" |
| R8 | Λ = 3l_P²/λ⁴ attributed to BHM, who write λ_cc = l_P²/l_Λ⁴ without the 3 (A) | Upheld | "up to the factor 3 they drop" |
| R9 | the CKN conventions "between 0.45 and 2.1" need the 2.1's assumption stated (A) | Upheld | 0.45, 0.59, 0.84 and 2.08, each with its convention |
| R10 | Mignemi writes no geometric-mean length and does not call the duality Born's (A, B) | Upheld | Bambi–Urban 2008 and Bolen–Cavaglià 2005 as the explicit prior art, Mignemi as implicit |
| R11 | "no turnaround as written" assumes spatial flatness (A) | Upheld | the flatness of the program's cosmology stated; flag 50 later adds the closed turnaround's two conditions and its prior art |
| R12 | the anchors validate the two-sided column, the bound uses the one-sided one (B) | Upheld (wording) | which column, and why: the attractive, one-sided limit, the more conservative |
| R13 | Gabor's "self-reciprocal" means Gaussian pulses of any sharpness (B) | Upheld | corrected |
| R14 | the survey of readings misses the squeezed mode, the convention dependence of the \|Z\| = 1 apex, §8.4's step at the §6 epoch and the Hubble sphere's infinite elongation at a true bounce (B) | Accepted | added; "None of these changes the withdrawal" |
| R15 | omitted prior art (A, B) | Accepted | added with [S], except the works not retrieved; Hur et al. 2025 in §7 (below) |
| R16 | omitted constraints: the vacuum energy to be cancelled, early-universe instability, a single Yukawa term (A, B) | Accepted, as caveats | a "Caveats [T][O]" paragraph in §8.2 |

On R14 the adjudication explains why none of the added readings changes the withdrawal: "the squeezed mode was round before it left the Hubble radius during inflation, not at a bounce, and the |Z| = 1 geometry is excluded under either convention" ([squeezed cosmological perturbations](/wiki/cosmology/early-universe/squeezed-perturbations)). On R15: "Not added: Beane 1997, Jarvis–Morgan 2008 and Kounnas–Partouche–Toumbas 2012, which were not retrieved." On R16: "In the program the cancellation is the palindrome identity at the aligned point; the early-universe stability is open in the record (`review/v3-worklog.md` item R7); other light fields could add Yukawa terms" ([bimetric cosmology and its instabilities](/wiki/gravity/spin-2-fields/bimetric-cosmology)).

The adjudication also accepted minor items without separate rulings: the rounding of 5.2×10⁹² in the plain abstract; "the length scale of dark energy" for 47–52 μm, "which is within a factor of two of it"; §8.4's normalization being a choice; the year of Bedroya–Vafa (2020); Born 1938's own question whether b is universal or set by the system, "which anticipates FKGLM's contextual λ"; and §4's last sentence, "which conflated FKGLM's momentum cutoff (ħ/√(ℓℓ_P)) with the Planck momentum".

The author's own items, numbered 1 to 5 in the adjudication, were found on a reread "during the review, before the reports": that a·ã = 1 holds along the whole slice X = 0, which the circle |Z| = 1 meets only at Z = i (§5); that det H = 1 is not one of the record's "self-duality" loci (§5); that the comoving entropy is conserved "throughout, from reheating on" (§3); that the |Z| = 1 paragraph's second failure reads 10⁹² "as the squeeze of H along the circle" (§6); and the metastring sentence of §8.1, sharpened to "ħ = λε and G_N = ρλ/ε, so λ² = ħG_N/ρ".

## The forecast scored

The adjudication's table (`review/round5-adjudication.md`, 'Pre-registration scored'):

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

The adjudication's calibration across rounds:

- "Verdicts: 2/2 (rounds 1–2), miss (round 3), hit (round 4), hit (round 5)."
- "Weakest-link location: hit in rounds 4 and 5."
- "Still underestimated: the number of small errors in a long text, and the extent of prior art."

The record across all rounds is on [pre-registration and its calibration record](/wiki/method/review/pre-registration).

## The lessons

Both went into root `CLAUDE.md` ('Method (HANDOFF §5)'), which words them:

1. "When a result rests on a formula from the literature, carry every parameter the cited formula has and state what fixes each one. Round 5 found a dropped background ratio in a bimetric coupling."
2. "A claim about how a quantity behaves over time ("holds at no other epoch") needs executed code like any number." The adjudication's form adds: "Round 5 found one that a two-line calculation refutes."

Neither has a page of its own; the second extends [the iron rule](/wiki/method/verification/iron-rule) from numbers to claims about how a number changes. Both concern the author's text: a parameter dropped from a cited formula, and a claim about other epochs made without code ([the measured referee failure mode](/wiki/method/review/referee-failure-mode)).

## The revisions and version 1.1

The adjudication's revisions are "all accepted; applied 2026-10-26", and it adds: "v1.1 writes the background ratio as u (c in the cited papers and in the referees' reports), to keep it apart from the speed of light." In brief:

1. **§8.2:** the formula with the background ratio; the program's vacuum, u = 1, and the argument for it; the bound as a function of u and the values below which X at the self-dual length survives; which column of the table is used and why; that persistence in an expanding universe is open, that the second frame is not the slaved block, and that how reciprocity's two actions relate is open in the record; the caveats of R16; and the condition u = 1 carried into the abstracts, §8's opening and §9.
2. **§4:** the CKN explanation in place of "holds at no other epoch"; FKGLM's momentum cutoff; Born's question whether b is universal.
3. **§2:** the one-cell row's momentum side h/w.
4. **§3:** Egan–Lineweaver's Table 2; the entropy sentence.
5. **§5:** Gabor's "self-reciprocal"; the e-fold count of squeezing credited to Albrecht et al., with "clock" dropped for complexity; author items 1 and 2.
6. **§6:** the squeezed-mode reading, the convention dependence of the |Z| = 1 apex, the infinite Hubble-sphere elongation at a true bounce and the string-cosmology bounces; flatness stated; author item 4.
7. **§7:** Bambi–Urban and Bolen–Cavaglià as explicit prior art, Mignemi as implicit; the CKN conventions; the fourth root; BHM's form without the 3; the TeV numerology; Sundrum, Kapner et al. and Li.
8. **§8.1:** the metastring sentence; "Gibbons and Caianiello beside Low".
9. **§8.4:** the step's epoch must lie before nucleosynthesis, and coincides with the §6 square for the region-scale unit, which is not a bounce.
10. **References and `verify/phase_space_diameter.py`:** "every new number gated; every new citation retrieved."

The note's header summarizes version 1.1: "§8.2 states the bimetric background ratio (written u here; c in the cited papers) that the coupling to X carries, gives the program's argument for u = 1 and the bound as a function of u; §4 explains the per-axis agreement by the Cohen–Kaplan–Nelson bound instead of a coincidence; §5–§7 add prior art (Bambi–Urban, Bolen–Cavaglià, Albrecht et al., Sundrum, Kapner et al., Li, string cosmology); §6 adds the squeezed-mode and string-cosmology readings. Smaller corrections are listed in the adjudication."

Every accepted revision is carried out in version 1.1's text. The last to reach it was R15's "Hur et al. 2025 for dual-spacetime dark energy": the note's §7 now cites the paper [S], for "a dual-spacetime model with ultraviolet–infrared mixing, in the Born-geometry lineage", which "gives a dark energy that varies in time with w > −1, which its authors find compatible with DESI", the Dark Energy Spectroscopic Instrument ([DESI](/wiki/cosmology/dark-energy/desi)). The worklog's entry of 17:55 records the citation as added after the wiki was written ("ruling R15 had claimed it"). The adjudication's 'Recommendations to Paul' and the root `CLAUDE.md` also list the paper as a lead outside the note, bearing on how DESI's data are read against the program's w ≥ −1.

## The round's files and the gate

The record is `review/round5-preregistration.md`, `review/round5-adjudication.md`, the reviewed text `review/round5/manuscript-v1.0.md`, each referee's `audit-notes.md`, scripts and printed outputs in `review/round5/referee-A/` and `review/round5/referee-B/`, and the adjudicator's `arb.py` and `arb.out` in `review/round5/adjudicator/`. As in rounds 3 and 4, the arbitration script sits in `review/` and the gate does not run it, while root `CLAUDE.md` says arbitration scripts go in `verify/`; no document resolves the difference (flag 38 in `review/wiki-build-flags.md`; [conflicts between sources](/wiki/history/documents/source-conflicts#method-and-records)). The numbers the rulings changed are gated through the note's script, which the gate runs: R1's bound at other values of u and the sampled vacua, R2's constant ratio and the CKN saturation, and the figures of R6, R7, R9, R12 and R14 ([the phase-space-diameter script](/wiki/method/verification/phase-space-diameter-script); [the gate](/wiki/method/verification/the-gate)).

## What remains open

- **Whether the aligned vacuum persists** as the universe expands, on which the bound's premise u = 1 rests [O] (note §8.2; root `CLAUDE.md`, 'Since the handoff').
- **How reciprocity's two actions relate**, as frame exchange on the spin-2 sector and as Z → −Z⁻¹ on the modular field (flag 39).
- **Flags 23 and 24.** The adjudication recommends accepting both: "a·ã = 1 is det H = 1 on the whole slice X = 0; |Z| = 1 is the locus of square rectangles; Z = i is the self-dual point; and the diameter relation's square is not at the turnaround." Both await Paul's ruling ([pending rulings](/wiki/status/open-problems#pending-rulings)).
- **Leads found by the literature sweep**, outside the note and "not queued" (root `CLAUDE.md`): Low 2006 as prior art for #13's [maximum force](/wiki/conjugate-relativity/maximum-force); Lukierski, Meljanac, Mignemi and Pachoł 2023, who break an algebra containing a continuous Born rotation spontaneously in the Yang model, which bears on the toy note's "no explicit model"; and Shlivko and Steinhardt 2024 and Hur et al. 2025, on reading DESI's fits against w ≥ −1. Hur et al. 2025 is also cited in the note's §7, for dual-spacetime dark energy.
- **The next review.** An optional round 6, of the [toy-model note](/wiki/symmetry-breaking/toy-models), "but only before any external use" (root `CLAUDE.md`). Round 4 was that note's last review ([review round 4](/wiki/method/review/round-4)).

## Sources

- `review/round5-adjudication.md` — the manuscript's hash and the copy kept of it, the referees and their access to Born's papers, the verdict, rulings R1–R16, the minor and author-found items, the scoring and calibration, the lessons, the revisions, the recommendations
- `review/round5-preregistration.md` — the set-up, the limitation, the forecast and its storage outside the repository
- `review/round5/manuscript-v1.0.md` — the reviewed text, version 1.0, whose hash matches the recorded one
- `review/round5/referee-A/audit-notes.md` and `review/round5/referee-B/audit-notes.md` Steps 1–5 — isolation, citation access and findings, recomputation, re-derivations, conceptual audits, verdicts and weakest links
- `review/round5/adjudicator/arb.out` — the arbitration figures
- `papers/phase-space-diameter.md` header — the v1.1 change line and the background ratio written u; §1 — the claims; §4, §6, §8.2 — the revised passages, and in §8.2 the reading that E₀[J] carries no scale of its own; §7 — Hur et al. 2025; 'References' — its entry
- `notes/phase-space-diameter-worklog.md` — Paul's question, the hashes recorded before dispatch, the dispatch time; the source fixes after the wiki was written (17:55)
- `verify/phase_space_diameter.py` — the gated figures of the rulings
- `CLAUDE.md` 'Since the handoff (2026-10-19)' — the note done, the leads, the optional round 6; 'Method (HANDOFF §5)' — the two lessons
- `HANDOFF.md` §4 — the chat-only relation; §8 item 7 — the optional write-up
- `notes/beta-coefficients.md` §1–§2 and `notes/tuning-test.md` §4 — the aligned vacuum and the open persistence, cited by R1
- `review/v3-worklog.md` item R7 — the early-universe stability cited by R16
- `review/wiki-build-flags.md` items 23, 24, 38, 39 — the flags the round bears on, all awaiting Paul's ruling
- `notes/closed-universe.md` §2, §6; `review/wiki-build-flags.md` items 50 and 51 — the conditions and prior art of a closed turnaround with V ≥ 0, which R11's statement omits, and β₁ > 0 on the branch of R1
