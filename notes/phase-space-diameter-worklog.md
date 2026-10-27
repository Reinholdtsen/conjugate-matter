# Worklog: the size of the universe in position and momentum space

The phase-space-diameter note (root `CLAUDE.md` queue item 1, third part;
`HANDOFF.md` §8 item 7). Paul's question, 2026-10-26: "Investigate or explain
if there is a relationship between the size of our universe in position space
and momentum space. Speculate and work through the consequences if so."

Deliverables:

- `papers/phase-space-diameter.md`: the note, house format.
- `verify/phase_space_diameter.py`: every number in the note, with anchors
  independent of the note, wired into `scripts/check.sh`.
- A blind review round, pre-registered before dispatch, then an adjudication.
- Wiki updates once the note is final.

## Starting point (what the record says)

- `HANDOFF.md` §4 (chat-only): "D_x · D_p = h · N^(1/3) per dimension (cosmic
  time–bandwidth theorem); the constant = the universe's photon count/entropy
  (~10⁹⁰, i.e. ~10³⁰ h per dimension); rectangle square (D_x = D_p in Planck
  units) exactly at the bounce; aspect ratio today ~10⁹² = a clock measuring
  distance from self-duality."
- #11 §10: a·ã = 1 from ω-rigidity [D], identified with the |Z| = 1 locus.
  Flag 23 (audited, confirmed) says a·ã = 1 is the whole X = 0 slice (it is
  det H = 1), and |Z| = 1 meets that slice only at Z = i, the self-dual point
  a = ã.
- Flag 24 (audited, confirmed): "square exactly at the bounce" names no bounce.
  With D_x·D_p fixed, the aspect ratio grows as a², so the square is near
  a ~ 10⁻⁴⁶ a₀ and the turnaround is where the rectangle is most elongated.
- Flag 27 (audited, confirmed): V = V₀[1 + cos(τ/f)] ≥ 0, so the turnaround
  the "conjugate bounce" needs does not happen as written.
- #13 §1: the Born length λ = l_P, untagged; c̃ = ħc/λ² = c⁴/G.
- `wiki/cosmology/scale-factor-duality/phase-space-diameter.md`: no
  definitions, no derivation, no checked numbers.

## Chunks

1. Research workflow: literature with live retrieval and a novelty audit, an
   independent re-derivation that tries to refute the candidate results, an
   independent recomputation of the numbers, a steelman of the chat claim, a
   sweep of the record.
2. Draft the note and the verify script; run the gate.
3. Pre-register; blind review; adjudicate with arbitration scripts.
4. Revise the note.
5. Wiki: the diameter page, an obituary for any dead sub-claim, registers.
6. Root `CLAUDE.md` ("Since the handoff", layout); final gate.

## Status

- 2026-10-26: chunk 0 done. Record read; `.venv` created on this machine;
  baseline `scripts/check.sh` passes (306 wiki pages). Chunk 1 starting.
- 2026-10-26 15:15: chunk 1 running (workflow `wf_796856c9-3a9`, 8 agents;
  the independent numbers agent has returned and matches every number of my
  draft script). Drafts, outside the repo until final, in this session's
  scratchpad `draft/`: the note, the verify script (all checks pass), the
  wiki plan and the round-5 protocol. The round-5 pre-registration draft is
  kept in the scratchpad `prereg/` so the referees cannot read it.
- Findings so far, all from executed code:
  - For blackbody photons in a sphere, D_x·D_p = κ h N_γ^{1/3} exactly,
    κ = 3^{1/3}π^{10/3}/(30ζ(3)^{4/3}) = 1.708 (D_x the diameter, D_p twice
    the mean momentum). Observable universe: N_γ = 1.43×10⁸⁹, S = 1.01×10⁹⁰,
    area 8.9×10²⁹ h. The chat's ~10⁹⁰ is the radiation entropy.
  - Aspect ratio in Planck units 5.2×10⁹² today; square at a/a₀ = 4.4×10⁻⁴⁷,
    T = 4.4×10¹⁴ T_P = 0.61 N^{1/6} T_P; at reheating (≤ 6.6×10¹⁵ GeV) it was
    already 2.2×10³⁵ [draft; superseded: v1.1 uses the BICEP/Keck 2021 bound, ≤ 5.7×10¹⁵ GeV and
    A = 2.9×10³⁵]. Hubble-sphere reading: square at 0.28 T_P with about
    0.45 quanta inside. "Square at the bounce" fails in every reading tried.
  - The box [l_P, L] × [ħ/L, ħ/l_P] is ρ_λ-self-dual iff λ = √(l_P L):
    47–84 μm, 2.3–4.2 meV, equal to the CKN cutoff; the dark-energy match is
    the identity (3Ω_Λ/8π)^{1/4} = 0.535. With λ² = l_P L_Λ, A = √Ω_Λ(t).
  - At that λ, #13's maximum force would be 1.4×10⁻¹⁷ N (excluded), and X
    at 47–84 μm with α = 4/3 is excluded by torsion balances (bound to be
    confirmed by the data agent), giving M_X c² > 5.1 meV [draft; superseded: v1.1 gives
    λ_X < 37.7 μm, M_X c² > 5.2 meV for α = 4/3, conditional on the background ratio u = 1].
- 2026-10-26 15:30: chunk 1 done (8 of 8 agents; results in the scratchpad
  `wf1_results.json`). What changed the plan:
  - Prior art for the self-dual length, in the Born-geometry lineage the
    program cites: Freidel, Kowalski-Glikman, Leigh, Minic, PRD 107, 126016
    (2023), with LM/2πħ = N^{1/4} and λ ~ √(ℓℓ_P) ~ 10⁻⁴ m tied to the vacuum
    energy; also Berglund–Hübsch–Minic 2023, Padmanabhan 2006, Snyder–de
    Sitter (Mignemi 2010), CKN 1999. §7 is now [T].
  - Born 1938 and 1949, retrieved by the reciprocity agent: Born 1938 as the
    Royal Society's own PDF in the Wayback Machine (SHA-256
    `556753a7c670d7d55bc17e2ecb3eb92e8a8684a81873061ee9785dc0f70f95b5`),
    Born 1949 as the American Physical Society's open copy (SHA-256
    `9e25ee5122844f467e65676fb42b3c10dc573a097c21ffae15233d5840b9ba23`);
    both have no usable text layer, so the quotations were transcribed from
    the page images. Born 1938, read in full: Born pairs the
    radius of Einstein's closed universe with a momentum-space radius b and
    declines to connect them; b is fixed from the classical electron radius.
  - Grosse–Wulkenhaar 2005 (toy model II's source) identify √Ω with
    l_P/(size of the universe).
  - Lee et al. 2020 bound a heavy graviton above 5.1 meV; with X's α = +4/3
    the thesis table gives λ_X < 37.7 μm, M_X c² > 5.2 meV.
  - The steelman found no reading that makes the chat claim true for one
    region; the record's |Z| = 1 identification (flag 23) reproduces the
    claim exactly and is excluded by the measured aspect ratio.
  - For Gaussian states |Z| = 1 is Δx = Δp; Z = i is the round state;
    det H = 1 holds everywhere. The three "self-dual" referents separate.
  - Leads outside this note, for Paul: Low 2006 is prior art for #13's
    maximum force; Lukierski–Meljanac–Mignemi–Pachoł 2023 (PLB 847, 138261)
    break an o(5,1) containing a continuous Born rotation spontaneously in
    the Yang model, which bears on the toy note's "no model breaks ρ
    itself"; Shlivko–Steinhardt 2024 and Hur et al. 2025 bear on reading
    DESI's CPL quadrant against strict w ≥ −1.
- 2026-10-26 15:55: chunk 2 done. `papers/phase-space-diameter.md` v1.0
  written; `verify/phase_space_diameter.py` written and wired into
  `scripts/check.sh`; full gate passes. The script caught two of my own
  numbers (ln A₀ = 213.5, not 213.8; the two-region aspect 8×10²⁹, not
  8×10²⁸) and one script bug before they reached the note.
- Round 5 dispatch (chunk 3), recorded before dispatch:
  - pre-registration (kept in the scratchpad until the referees return):
    SHA-256 `b5094b65cf969c8106353059e14bc8f66497076dfa3ae3ef262bda3a0fe3033b`
  - manuscript copy sent to both referees:
    SHA-256 `2ed53d537d03c26273564cb4ed81b70117cc67853b08239a28149e927f3425a4`
  - dispatched 2026-10-26T15:55-07:00.
- 2026-10-26 16:45: chunk 3 done. Both referees: B (0.75). The shared
  weakest link: §8.2's α = 4/3 dropped the bimetric background ratio c of
  the cited formula, α = (4/3)(M_f c/M_g)². Upheld in substance (the
  program's vacuum is the aligned point, c = 1; the symmetry-breaking
  (c, 1/c) vacua carry vacuum energy ~10⁶¹ H₀²), with referee A's
  c = ã/a rejected (the second frame is E₀[J], not the slaved block).
  R2–R13 upheld, R14–R16 accepted (fifteen further findings). Pre-registration: verdict hit, weakest-link
  location hit, arithmetic count missed, novelty missed. Records:
  `review/round5-preregistration.md` (hash verified),
  `review/round5-adjudication.md`, `review/round5/`.
- 2026-10-26 17:00: chunk 4 done. Note v1.1 with every accepted revision;
  verify script extended (c-dependent bound, broken vacua, CKN saturation,
  conventions); root `CLAUDE.md` updated (layout, "Since the handoff",
  queue, leads, two method lessons). Acronyms CKN, FKGLM, BHM, HUST, BICEP,
  TCC, NIST, CQG and IJMPD added to `scripts/wiki-acronyms.txt`.
- Next: chunk 5, the wiki (plan in the scratchpad `draft/wiki-plan.md`).
- 2026-10-26 17:55: chunk 5 written. Nine writer agents updated 61 wiki
  files (eight new pages); `scripts/check-wiki.py` passes on 314 pages. The
  writers' source findings fixed afterwards: Hur et al. 2025 added to note §7
  (ruling R15 had claimed it); the adjudication's statement on the referees'
  access to Born corrected; the reviewed v1.0 kept as
  `review/round5/manuscript-v1.0.md` (hash verified); this log's superseded
  draft numbers marked; the verify script's labels, its H₀ independence check,
  its interpolated M_X and its Fubini–Study check tightened.
- 2026-10-26 18:25: the machine (WSL) crashed during the wiki verification
  pass (workflow `wf_d7e5c309-d32`). No verifier edit had reached disk (every
  changed file predates the launch). The session scratchpad in /tmp was wiped;
  everything the record needs had already been copied into the repo
  (pre-registration, referee notes, scripts and outputs, the reviewed v1.0,
  source hashes in this log). The literature and review agents' full returns
  survive in the workflow journals under ~/.claude/projects/. Gate state after
  the crash: the verify script's 85 checks pass, `scripts/check-wiki.py`
  passes on 314 pages. Verification relaunched at 18:26.
- Still to do: the verification pass's fixes; the full `scripts/check.sh`;
  `npm run check` in `site/` (Hugo build and HTML check; the theme submodule
  and `npm ci` were set up this session, no deploy); the summary for Paul.
- 2026-10-26 18:55: verification pass done (five agents, 98 fixes across the
  new and changed wiki pages; wiki/CLAUDE.md's source precedence now ranks the
  note and the round-5 adjudication; the conflicts register records the note's
  reading of |Z| = 1 against #11's, flag 23). Follow-ups applied afterwards:
  the documents index's precedence list, three register deep links to folded
  sections, the planck-units heading (no longer "chat-only"), a
  machine-dependent residual dropped from a wiki page, four wordings in the
  round-5 adjudication (the uncommitted files, the "no scale" attribution, the
  reading of A's identification, the credit for the e-fold clock), and PDF and
  SHA registered as names.
- 2026-10-26 19:00: chunk 5 done. `npm run check` in `site/` passes: every
  verify script (the diameter script's 85 checks), the wiki gate on 314 pages,
  the Hugo build, and the HTML check (316 pages, 141,360 links, 3,633 heading
  IDs). Nothing deployed, nothing committed.
