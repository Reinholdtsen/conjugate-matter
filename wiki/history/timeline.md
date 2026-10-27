---
title: "Timeline"
weight: 10
status: record
description: "Dated events from Born's 1938 paper to the pending DESI DR3 release: the claude.ai era in creation order, the move to the repository, rounds 3 and 4, the checkpoint's versions, the wiki's build with its flags file and the flags' audit, the next day's revisions, new pages, flags 43 and 44, the rulings worksheet, a second round of new pages and the Hugo site built from the wiki, and on 2026-10-26 the phase-space-diameter note, its gate script, review round 5, the note's version 1.1, the wiki update, the fixes to the sources that followed it, and the crash that interrupted the update's verification."
sources:
  - "CLAUDE.md 'Since the handoff'"
  - "notes/phase-space-diameter-worklog.md"
  - "papers/phase-space-diameter.md header"
  - "papers/phase-space-diameter.md §4"
  - "papers/phase-space-diameter.md §5"
  - "review/round5-preregistration.md"
  - "review/round5-adjudication.md"
  - "verify/phase_space_diameter.py"
  - "scripts/check.sh"
  - "papers/broken-born-checkpoint-v2.md header"
  - "papers/broken-born-checkpoint-v2.md §3"
  - "papers/broken-born-checkpoint-v2.md §12"
  - "papers/broken-born-checkpoint-v2.md References"
  - "papers/broken-born-checkpoint-v2.md footer"
  - "papers/reciprocity-toy-models.md"
  - "review/round4-adjudication.md"
  - "review/round4-preregistration.md"
  - "review/round4/referee/audit-notes.md"
  - "review/round3-adjudication.md"
  - "review/round3-preregistration.md"
  - "review/v3-worklog.md"
  - "HANDOFF.md §1"
  - "HANDOFF.md §2"
  - "HANDOFF.md §3"
  - "HANDOFF.md §5"
  - "HANDOFF.md §6"
  - "HANDOFF.md §8"
  - "HANDOFF.md footer"
  - "notes/toy-lagrangian.md"
  - "notes/knot-dark-matter-standalone.md banner"
  - "notes/broken-born-theory.md header"
  - "notes/broken-born-theory.md §0"
  - "notes/broken-born-theory.md 'Addendum (v0.2)' to 'Addendum (v0.6)'"
  - "notes/debt1a-geometric-core.md header"
  - "notes/debt1a-ii-X-classification.md §3"
  - "notes/broken-born-program-v1.md header"
  - "popsci/angle-of-the-mirror.md subtitle"
  - "README.md"
  - "wiki/CLAUDE.md 'Build state' (retired at b03903c)"
  - "wiki/CLAUDE.md 'Keeping it current'"
  - "wiki/CLAUDE.md 'Voice'"
  - "wiki/CLAUDE.md 'Links'"
  - "wiki/CLAUDE.md 'Publishing'"
  - "site/CLAUDE.md 'The gate'"
  - "site/CLAUDE.md 'Deploying (manual)'"
  - "review/wiki-build-rulings.md"
  - "review/wiki-build-flags.md"
  - "review/wiki-build-checks/flag-audit.json"
  - "review/wiki-build-checks/README.md"
---

*The timeline lists the program's events in date order, from Max Born's paper of 1938 to the third data release of the [Dark Energy Spectroscopic Instrument](/wiki/cosmology/dark-energy/desi) (DESI), which the handoff names the program's external clock, since its data can kill the [dark-energy sector](/wiki/cosmology/dark-energy) or the whole framework. The work done on claude.ai in September and October 2026 is almost entirely undated, so those events follow the creation order of the artifacts in `HANDOFF.md` §3. From the move to this repository on 2026-10-19, the commit history dates each step to the minute: review round 3 and the retirement of the [soliton candidate](/wiki/dark-matter/candidates/soliton-candidate/obituary), the [toy models](/wiki/symmetry-breaking/toy-models) and review round 4, the checkpoint's versions 2.1 and 2.2, and the building of this wiki, with the file of suspected source errors its verifiers kept and the audit that re-checked every item; then, on the next day, a rule on how the wiki states negative results, new pages of established physics, two further flags, a worksheet for ruling on the flags, a second round of new pages, and a static site built from the wiki; and on 2026-10-26 the note on [the phase-space diameter relation](/wiki/cosmology/scale-factor-duality/phase-space-diameter), its gate script, [review round 5](/wiki/method/review/round-5), the note's version 1.1, the wiki's update from it, the fixes to the sources that followed, and the verification of the update.*

**Status:** Record, current to the verification of the wiki's update from the phase-space-diameter note (2026-10-26), after round 5, the note's version 1.1 and the fixes to the sources that followed — untagged — dates come from the documents' own headers and dated entries, from `git log` (commit times are local, −0700) and, for 2026-10-26, from the times in the note's worklog, since the day's work had not been committed when its rows were written. Before the handoff the record gives two dates, "September 2026" for #1 v0.1 and 2026-10-17 for the first attempt at round 3; the other claude.ai events follow `HANDOFF.md` §3's creation order, and where review rounds 1 and 2 fall in that order is inferred, not recorded.

## How the record is dated

The record has two layers, and the most recent day is dated differently.

- **Before the move.** Artifacts #1–#15 were written in one conversation on claude.ai and carry almost no dates. #1's header reads "Version 0.1, September 2026". The handoff says the program was "developed September–October 2026" (`HANDOFF.md` §1) and dates two events, the first attempt at round 3 (§6) and its own preparation (footer). Everything else is ordered by the handoff's inventory, headed "Artifact inventory (creation order)" (§3), and by the version headers and addenda of the documents. The first popular article, #10, describes the work it narrates as "a week" of stress-testing (its subtitle).
- **From the move.** The repository's commits date every later step. Each row gives the time of the commit that recorded the event (local time, −0700) and its hash, so `git show` with the hash displays the change. The time is when the record was committed: an event such as a blind audit ran between the commits that bracket it, and its own time is given only where a document records it.
- **2026-10-26.** The work on the phase-space-diameter note had not been committed when its rows were written: the round-5 pre-registration records that it was not committed, the adjudication gives the reason, "this session had no commit authorization", and the note, its script, the review records and the edits to `scripts/check.sh` and the root `CLAUDE.md` stood uncommitted in the working tree. Those rows give the times of the entries in `notes/phase-space-diameter-worklog.md`, local time like the commits (the dispatch is recorded as "2026-10-26T15:55-07:00"), and their commit column is empty.

## Before the program

The literature the program starts from, builds on or is measured against has its own dates. Bracketed numbers are #11's reference list, with its marks: † cited from model memory, [S] retrieved by live search ([References](/wiki/references)).

| Year | Work | In the program |
| --- | --- | --- |
| 1938 | M. Born, "A suggestion for unifying quantum theory and relativity," Proc. R. Soc. Lond. A 165, 291 [1†] | the origin of [Born's question](/wiki/program/borns-question); read in full for the phase-space-diameter note, whose §4 records its pairing of a largest distance with a largest momentum |
| 1947 | H. S. Snyder, "Quantized space-time," Phys. Rev. 71, 38 [4†] | the start of the lineage of [curved momentum space](/wiki/phase-space/reciprocity/curved-momentum-space) (#11 §3) |
| 1949 | M. Born, "Reciprocity theory of elementary particles," Rev. Mod. Phys. 21, 463 [2†] | [Born reciprocity](/wiki/phase-space/reciprocity/born-reciprocity); retrieved for the phase-space-diameter note, which cites its split ħ = ab (§4, §5) |
| 2001 | N. Boulanger, T. Damour, L. Gualtieri, M. Henneaux, "Inconsistency of interacting, multi-graviton theories," Nucl. Phys. B 597, 127 [8†] | [the multi-graviton no-go](/wiki/gravity/spin-2-fields/multi-graviton-no-go), which excludes a massless [momentum graviton](/wiki/gravity/momentum-graviton) |
| 2014 | L. Freidel, R. G. Leigh, D. Minic, "Born reciprocity in string theory and the nature of spacetime," Phys. Lett. B 730, 302 [3†] | Born geometry ([the structures ω, η, H](/wiki/phase-space/born-geometry/born-structures)) |
| 2015 | Freidel, Leigh, Minic, "Metastring theory and modular space-time," JHEP 06 (2015) 006, arXiv:1502.08005 [26S] | [broken Born duality](/wiki/phase-space/reciprocity/broken-born-duality), and since #11 v2.1 the attribution of [the compatibility theorem](/wiki/phase-space/born-geometry/compatibility-theorem) |
| 2025 | DESI Collaboration (M. Abdul-Karim et al.), "DESI DR2 Results II: Measurements of Baryon Acoustic Oscillations and Cosmological Constraints," arXiv:2503.14738 [21S] | Data Release 2 (DR2) and its phantom crossing ([DESI DR2's phantom crossing](/wiki/cosmology/dark-energy/desi-dr2-phantom-crossing)) |
| 2026, July | D. Liveoak, A. Maharana, J. D. Wells, "Dark monopoles, bounds on hidden sectors, and cosmological implications," arXiv:2607.20843 [29S] | prior art for the [retired soliton candidate](/wiki/dark-matter/candidates/soliton-candidate/obituary) ([topological dark matter in the literature](/wiki/dark-matter/candidates/soliton-candidate/prior-art)); the month is from round-3 ruling 3 |

## The claude.ai era

The numbers in the first column are the artifact numbers of `HANDOFF.md` §3, in its creation order.

| # | Date | Event | Record |
| --- | --- | --- | --- |
| — | not recorded; before #1 | The development discussion: Paul's founding suppositions, eleven ideas later audited in #11 Appendix A ([founding suppositions](/wiki/program/founding-suppositions)); a heuristic [duality dictionary](/wiki/cosmology/scale-factor-duality/duality-dictionary), w_eff = −2 − w̃, which #1 corrected ([Obituary: conjugate collapse powers our expansion](/wiki/cosmology/scale-factor-duality/collapse-powered-expansion)); and [bimetric gravity](/wiki/gravity/spin-2-fields/hassan-rosen-bimetric), raised in "the second turn of this whole conversation" | #1 §0, §6; #6 §3; #11 Appendix A |
| 1 | September 2026 | The lab notebook, "Version 0.1": [postulates P1–P5](/wiki/program/postulates) with the [original P2](/wiki/program/postulates/original-p2), an action, a predictions table of ten rows, six open problems and "three named debts standing between this document and a paper" ([the lab notebook](/wiki/history/documents/lab-notebook); [the three debts](/wiki/history/debts); [the predictions table](/wiki/predictions/table-history)) | #1 header, §9, §11, §12 |
| 2 | not recorded | Calc note debt3a: [the particle island](/wiki/dark-matter/momentum-clumping/classicality-theorem); the [clumping criterion](/wiki/dark-matter/momentum-clumping/instability-criterion) fails by 10²⁸–10³¹ ([the Debt-3 calc notes](/wiki/history/documents/debt-3-notes)) | `HANDOFF.md` §3 |
| 3 | not recorded | Calc note debt3b: [the wave island](/wiki/dark-matter/momentum-clumping/wave-island) and its two scenarios | `HANDOFF.md` §3 |
| 4 | not recorded | Calc note debt3c, which "closes Debt 3 (negative)"; the notebook's addendum v0.2 withdraws rows 3 and 4 of its table ([Obituary: velocity clumping, the founding image](/wiki/dark-matter/momentum-clumping/founding-image)) | `HANDOFF.md` §3; #1 'Addendum (v0.2)' |
| 5 | not recorded; written "overnight" | Calc note debt1a, an "Overnight working note": the compatibility theorem, the repair of P2 to [P2′](/wiki/program/postulates/p2-prime), [the modular field](/wiki/phase-space/modular-field/modular-field-z) and [the gate mechanism](/wiki/dark-matter/conjugate-matter/gate-mechanism); addendum v0.3, also headed "overnight" ([the Debt-1 calc notes](/wiki/history/documents/debt-1-notes)) | #5 header; #1 'Addendum (v0.3, overnight)' |
| 6 | not recorded | Calc note debt1a-ii: X classified as a [massive spin-2 field](/wiki/gravity/momentum-graviton/forcing-chain); addendum v0.4 | `HANDOFF.md` §3; #1 'Addendum (v0.4)' |
| 7 | not recorded | Calc note debt1a-iii: [the tuning test](/wiki/gravity/tuning-test), a conditional pass; addendum v0.5 | `HANDOFF.md` §3; #1 'Addendum (v0.5)' |
| 8 | not recorded | Calc note debt1a-iv, which "closes Debt 1 (structural)": [the palindrome](/wiki/gravity/palindromic-branch/palindrome) and [Born's answer](/wiki/gravity/momentum-graviton/borns-answer); addendum v0.6 | `HANDOFF.md` §3; #1 'Addendum (v0.6)' |
| 9 | not recorded | The program v1.0, "consolidation of the full development arc", with a plain-language passage opening each section and the tags [D], [T], [P], [O] ([the checkpoint](/wiki/history/documents/checkpoint)) | #9 header; `HANDOFF.md` §3 |
| 10 | not recorded | "The Angle of the Mirror", the first popular article, a narrative "including the deaths" ([the popular articles](/wiki/history/documents/popular-articles)) | `HANDOFF.md` §3 |
| 11 | not recorded | Checkpoint v2.0, the reference for the full program: the methodological preface and the seven-test battery ([the battery](/wiki/method/verification/battery)), [the charge lattice](/wiki/electric-magnetic-duality/symplectic-charge-lattice), the dark-sector trilemma with the soliton candidate ([dark-sector candidates](/wiki/dark-matter/candidates)), references marked † or [S], the novelty downgrade of [the vacuum-energy identity](/wiki/gravity/palindromic-branch/vacuum-energy-identity), and the audit of the founding suppositions | `HANDOFF.md` §3 |
| 12 | not recorded | "The Universe's Other Half", the second popular article, "the framework presented as if confirmed" | `HANDOFF.md` §3 |
| 13 | not recorded | The short paper on [conjugate special relativity](/wiki/conjugate-relativity) | `HANDOFF.md` §3 |
| 14 | not recorded | The soliton manuscript, v1, written for context-free blind review ([the soliton candidate (retired)](/wiki/dark-matter/candidates/soliton-candidate)) | `HANDOFF.md` §3 |
| 15 | not recorded | [The skeptic review console](/wiki/method/review/skeptic-console), a browser page that sends #14 to a fresh referee with web search | `HANDOFF.md` §3 |
| — | not recorded; position inferred | Review round 1 on #14 v1, verdict "B / medium"; v2 takes in its valid findings; round 2 on v2, "B near B/C / medium". Both used #15 and were pre-registered ([review rounds 1 and 2](/wiki/method/review/rounds-one-and-two); [pre-registration](/wiki/method/review/pre-registration)) | `HANDOFF.md` §3, §5, §6 |
| — | 2026-10-17 | A first attempt at round 3, an execution-verified blind audit of #14, "dispatched 2026-10-17 and died partway on a rate limit"; the handoff asks for it to be re-run "natively" in Claude Code | `HANDOFF.md` §6 |
| — | 2026-10-19 | The handoff document, "prepared 2026-10-19 from the originating claude.ai session" ([the handoff document](/wiki/history/documents/handoff)) | `HANDOFF.md` footer |

The position of rounds 1 and 2 is inferred from what the handoff does record: round 1 reviewed #14 v1, v2 "incorporates all valid round-1 findings", round 2 reviewed v2, and #15 was "Used for review rounds 1–2". The rounds therefore follow #14 v1 and #15, but no document dates them. Nor does the handoff reconcile its count: §1 says "Three blind AI reviews returned verdict B", while §6 records two completed rounds and an incomplete third ([how many reviews returned B](/wiki/method/review/rounds-one-and-two#unresolved-how-many-reviews-returned-b); [conflicts between sources](/wiki/history/documents/source-conflicts#method-and-records)).

## The move to the repository: 2026-10-18 and 19

| Time | Commit | Event |
| --- | --- | --- |
| 2026-10-18 23:07 | 6b8f599 | Initial commit: a README describing the repository as "Physics hypothesis explaining dark matter and missing magnetic monopoles" ([CLAUDE.md and the README](/wiki/history/documents/project-instructions)); the monopole explanation is dead ([Obituary: conjugate monopoles explain the null result](/wiki/electric-magnetic-duality/monopole-explanation)), and the README's monopole clause is flag 37 in `review/wiki-build-flags.md` |
| 2026-10-19 10:28 | 8d588f6 | "Import session from regular Claude.": `HANDOFF.md` and artifacts #1–#15 copied into the repository |
| 10:35 | 008c3ee | The import arranged into `papers/`, `notes/`, `popsci/`, `review/` and `verify/` as `HANDOFF.md` §9 suggests; the root `CLAUDE.md` written; `verify/battery.py`, the handoff's Appendix A turned into assertions, and `scripts/check.sh`, "the definition of done": the first [gate](/wiki/method/verification/the-gate). #1–#10, #12, #13, #15 and `HANDOFF.md` have not changed since |

## Round 3 and the retirement of the soliton candidate: 2026-10-19

The handoff's queue began with cutting v3 of #14 and re-running the blind audit on it (`HANDOFF.md` §8, items 1 and 2).

| Time | Commit | Event |
| --- | --- | --- |
| 2026-10-19 10:41 | 678e48a | Every number of #14 v2 recomputed by a new script, `knot_numbers.py` in `verify/` (since replaced); the v3 worklog begun |
| 10:59 | 2b72da0 | The literature report, dated 2026-10-19, folded into the worklog: a subagent with web access pulled each record "with no citations from memory" |
| 13:23 | 2eb58de | Paul's decisions on F1 and F2, "Decided (Paul, 2026-10-19)": the benchmark mass moves to M ≈ 3×10¹³ GeV, and the hidden sector's elementary coupling is read as weak, its solitons as strongly coupled ([Obituary: the coupling α_d ≈ 34](/wiki/dark-matter/candidates/soliton-candidate/alpha-d-coupling#superseded-f2-which-coupling-sets-the-soliton-mass)). The same commit logs item O3: #13's two dual cones are to be fixed before any paper claims more, "raised by Paul, 2026-10-19" ([Open: the two dual cones](/wiki/conjugate-relativity/two-cones-inconsistency)) |
| 13:25 | d15cd4a | The minimal hidden sector scripted: its stable W′ bosons overclose the universe, so v3 needs a light dark doublet ([W′ overclosure](/wiki/dark-matter/candidates/soliton-candidate/w-prime-overclosure)) |
| 14:42 | 5dbaa82 | #14 v3 cut from the [round-2 pending list](/wiki/method/review/rounds-one-and-two) and the two decisions |
| 14:48 | cc05705 | Round 3 pre-registered: predicted verdict B, weakest link "the framework does no work". The prediction stood in the commit subject, which the auditor's git status showed ([round-3 pre-registration](/wiki/method/review/round-3/preregistration)) |
| not recorded | — | The blind audit: a fresh subagent with shell, Python and web search, given only the manuscript and the five-step protocol ([review round 3](/wiki/method/review/round-3)) |
| 15:47 | 96f58da | The adjudication: verdict C on the Kibble normalization, one monopole per Hubble volume being p ≈ 104, not 0.023 ([Obituary: the Kibble normalization](/wiki/dark-matter/candidates/soliton-candidate/kibble-normalization); [round-3 rulings](/wiki/method/review/round-3/rulings)). Two lessons enter the root `CLAUDE.md`: keep the prediction out of the commit subject, and use only anchors independent of the paper ([independent anchors](/wiki/method/verification/independent-anchors)). #14 gets a banner, "Status (2026-10-19): v3 failed round-3 review (verdict C)", and the gate now fails on its affected claims by design ([the gate](/wiki/method/verification/the-gate)) |
| 17:14 | 5b6efaa | The decisions Paul delegated: strict sector separation ([P4](/wiki/program/postulates/p4-polarized-matter)); the soliton candidate retired as a program-native proposal ([Obituary: superheavy conjugate solitons](/wiki/dark-matter/candidates/soliton-candidate/obituary)); the handoff's queue item 3, the √N floor, dropped ([Obituary: the √N topological floor](/wiki/dark-matter/candidates/soliton-candidate/sqrt-n-floor)); [the toy Lagrangian](/wiki/symmetry-breaking/toy-models) next, after amending #11. #14 moved to `notes/` with the banner "Withdrawn (2026-10-19)", and `verify/soliton_obituary.py` replaces the v3 checks, so the gate passes again ([round-3 decisions](/wiki/method/review/round-3/decisions); [the soliton-obituary script](/wiki/method/verification/soliton-obituary-script)) |
| 17:29 | e1c1f67 | #11 v2.1: the soliton obituary in §12, "retired 2026-10-19"; the compatibility theorem re-tagged [T][V] and attributed to Freidel–Leigh–Minic (§5); [P4](/wiki/program/postulates/p4-polarized-matter) strict (§4); DR2's phantom crossing (§10); references [26]–[29] added |

## The toy models and round 4: 2026-10-19 and 20

| Time | Commit | Event |
| --- | --- | --- |
| 2026-10-19 18:37 | d9e61f0 | Success criteria S0–S5 and the predictions for the toy Lagrangian, "fixed 2026-10-19, before any construction" ([success criteria](/wiki/symmetry-breaking/toy-models/success-criteria)) |
| 18:40 | 0e0f51e | Chunk 1: the coset model meets S1–S3 classically; `verify/toy_coset.py` joins the gate ([model I](/wiki/symmetry-breaking/toy-models/coset-model); [the toy-model scripts](/wiki/method/verification/toy-model-scripts)) |
| 18:59 | d112dd4 | The prior-art survey S0, with no existing action found that breaks Born reciprocity spontaneously with η as the [order parameter](/wiki/symmetry-breaking/order-parameter); the Grosse–Wulkenhaar (GW) route chosen for chunk 2 |
| 20:45 | 4923112 | Chunk 2: the vacua of the complex self-dual GW model break the duality classically; `verify/toy_gw.py` ([model II](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar)) |
| 21:02 | 4f989e6 | Chunk 3: S4 passes in the coset model only with a τ-type potential, the one round 4 later found unbounded below ([Obituary: the naive ρ-preserving potential](/wiki/symmetry-breaking/toy-models/coset-model/naive-potential)), and the classical breaking of the GW model does not survive quantization; `verify/toy_s4.py` |
| 21:52 | 56485d3 | Chunk 4: the S5 computation on the [locality of matter](/wiki/symmetry-breaking/matter-coupling); `verify/toy_s5.py` |
| 22:16 | bed9306 | Chunk 4 concluded after a literature check by a subagent: S5 passes in its weak form only, the pre-registered predictions score four hits, and acceptance criterion 1 is met in the referees' wording ([acceptance criterion 1](/wiki/symmetry-breaking/toy-models/acceptance-criterion)) |
| 22:26 | d9a06ac | Round 4 pre-registered under a neutral commit subject, with the toy-model note v1 as the manuscript ([review round 4](/wiki/method/review/round-4)); the same commit corrects a sign reversed in the worklog's chunk-2 results, marked "Corrected 2026-10-19" |
| 22:29 | 6ee74d0 | #11 §3 credits Freidel–Leigh–Minic for "broken Born duality", a change of v2.2 committed ahead of the version |
| 2026-10-19, time not recorded | — | The round-4 blind audit, "Started 2026-10-19"; it "was interrupted once by a rate limit and resumed from its own transcript" |
| 2026-10-20 11:13 | e3ce9eb | The adjudication: verdict B; the potential of the note's §4 is unbounded below once H is dynamical ([Obituary: the naive ρ-preserving potential](/wiki/symmetry-breaking/toy-models/coset-model/naive-potential)). Two lessons enter the root `CLAUDE.md`: check the stability of the unreduced model, and give Monte Carlo numbers error bars from independent runs ([the reduced-model stability rule](/wiki/method/verification/reduced-model-stability); [the Monte Carlo error-bar rule](/wiki/method/verification/monte-carlo-error-bars)) |
| 18:54 | 6606734 | The toy-model note v2 and #11 v2.2, "amended 2026-10-20"; the root `CLAUDE.md` records the toy Lagrangian as done and sets the current queue |
| 18:54 | 5ca7d81 | The adjudication marks the revisions applied |

## The wiki and its flags file: 2026-10-20 and 21

The build was recorded in the commits and in the section 'Build state' of `wiki/CLAUDE.md`, from the breadth pass (7b9438b) until b03903c retired it; its last version is at 51ede3e. From then on it is recorded on this page. The build state labels depth waves 4–6 "2026-10-21/22" and the final pass "running as of 2026-10-22", and the flags file dates its audit 2026-10-22; all their commits carry the date 2026-10-21.

| Time | Commit | Event |
| --- | --- | --- |
| 2026-10-20, time not recorded | — | The design round: "Thirteen inventories, a master topic list (371 topics, 115 background concepts, 151 resolved source conflicts) and taxonomy proposals B and C" in the session's scratch files; B adopted, with 278 entries |
| 2026-10-20 23:39 | 17e1338 | The wiki gate, `scripts/check-wiki.py`, joins `scripts/check.sh`: links, anchors, section maps, sources and page shape |
| 2026-10-21 09:53 | 7b9438b | The breadth pass: "all 278 pages, averaging about 800 words each", with the conventions in `wiki/CLAUDE.md` |
| 09:55 | b970e9d | Starred symbols escaped and checked by the gate; acronyms registered |
| 09:56 | 3243cdc | The root `CLAUDE.md` lists the wiki in its layout and its gate |
| 10:11 | 6e30305 | Depth wave 1 begins: the program and phase-space sections |
| 11:09 | c6f9a3f | Build state after wave 1: "52 files, committed page by page. The verifiers checked 1,882 claims and fixed 104 of 107 findings"; two suspected errors in the sources await Paul's ruling |
| 11:20 | 7f34fb5 | Depth wave 2 begins: gravity, then the breaking of reciprocity (85a8fc7, 11:28) |
| 14:05 | 900b6cc | Partial verifier fixes "from agents cut off by the usage limit" |
| 14:06 | 2b43d4d | The flags file, `review/wiki-build-flags.md`, begun (see below) |
| 14:30 | ab24319 | Build state after wave 2: "The usage limit cut the workflow off midway"; "15 in all" source flags |
| 14:31 | 0796b9c | Depth wave 3 begins: dark matter |
| 14:46 | ae94e66 | The verifiers' executed checks kept beside the flags, in `review/wiki-build-checks/` |
| 15:11 | e772eb6 | Depth wave 4 begins: cosmology, then electric–magnetic duality (e0a903c, 15:44) and conjugate relativity (1a29314, 15:48) |
| 15:44 | e58f7d5 | Build state after wave 3: dark matter "at full depth and verified: 54 files"; the flags file "now holds 26 items" |
| 16:15 | 8fa2f0b | The depth pass reaches the predictions, with row 1 |
| 16:31 | d34dbf5 | Build state "after the reboot": "A reboot cleared the session scratchpad, so the inventories and the taxonomy file are gone; the committed tree now carries the plan" |
| 17:10 | fe96131 | The depth pass reaches the method section, with [Lakatos's methodology](/wiki/method/lakatosian-methodology) |
| 17:25 | 9a5b7c1 | The depth pass reaches this section, with the document pages; then [the three debts](/wiki/history/debts) (45b782e, 17:44), this page and the section index |
| 18:15 | 51ede3e | Build state at the final pass: depth waves 4–6 "at full depth and verified"; "Two reboots interrupted agents"; "The flags file holds 38 items". The plan for the final pass: verify the last four batches; sweep each partition (flag pointers, known cross-page fixes, "Used by" lists, first-mention links); run six read-only critics, "four for source coverage, a casual reader, a navigation check", and apply their fixes; rebuild the registers from the finished pages; run the full gate |
| 18:28 | 91bd36f | The final pass's verification: verifier fixes for the last batches of the depth pass, the method pages, rows 6–11 of the predictions, the blind-review pages and the verification pages, committed page by page to 3a195c2 (18:35) |
| 18:49 | 6874af7 | The sweeps, committed by section as "Wiki sweep" to d01f133 (19:11): flag pointers where flagged statements are quoted, "Used by" lists completed from inbound links, first-mention links, and payment and bookkeeping wording taken out of the wiki's own prose |
| 19:23 | 791b455 | The critics' fixes, committed by section as "Wiki final pass" to 795e5f5 (19:33): among them section strips completed with their folded open, superseded, chat-only and popsci-only items, plain-language openings added or glossed, and the executed checks of flags 16 and 19 placed beside the statements they concern |
| 19:51 | 7d19a4b | The registers rebuilt from the finished pages: the home page; the graveyard and alive registers (d4334ca, 20:01); [open problems](/wiki/status/open-problems), conjectures and superseded (aa03f99, 20:03), with pending rulings 1–38; the [glossary](/wiki/glossary), "372 entries" (4c1ea08, 20:11); the [notation](/wiki/notation) (d60e623, 20:12); the [references](/wiki/references) (c1ed53c, 20:12) |
| 20:20 | e56651e | The final check, committed as one fix: [the status index](/wiki/status) lists the "Conjecture:" folded heading beside "Open:", "Superseded:", "Chat-only:" and "Popsci-only:" |
| 20:22 | 2c6f857 | [The gate](/wiki/method/verification/the-gate) keeps in-word underscores in heading anchors, as the Hugo site generator does. It had dropped every underscore, so a link to `#no-value-for-mx` passed while Hugo serves the heading as `#no-value-for-m_x`; "Eight links that the old rule let through are corrected" |
| 20:23 | 6d714e9 | Flags 39–42 from the final pass, with executed checks for flags 39 and 40; flags 6, 7 and 38 extended ([the flags file](#the-flags-file)) |
| 20:24 | b03903c | `wiki/CLAUDE.md` retires its build-state section, which was to be deleted "when the build is complete"; from then on the build is recorded on this page. The same commit adds "Conjecture:" to the folded headings and says how to act on a flag ruling |
| 21:28 | d89b457 | The flags audited by independent agents told to refute them ([the flags file](#the-flags-file)) |
| 21:44 | 239becd | Post-audit pointers: flag 39 where the graviton's reciprocity parity is stated, with [two actions of reciprocity](/wiki/gravity/momentum-graviton/spectrum-and-parity#two-actions-of-reciprocity) set out on the spectrum page and pointers on row 6, the palindrome, modular inversion, the vacuum-energy identity and other pages; then (5ff7b17, 21:53) pointers for flags 35, 36, 38, 40, 41 and 42, and the pages citing flags 11, 14, 17, 18, 19, 30, 31 and 32 state the audit's verdict instead of a confirmed error; then (670a71d, 23:24) the flag-42 pointer on the review protocol and the [pending rulings](/wiki/status/open-problems#pending-rulings) rewritten to list all 42 flags with their verdicts |
| 23:29 | fc073bb | The post-audit work completed: the open-problems register made consistent with its pending rulings, and the home page's reading guide gives the 42 flags and the audit's result. The rows of this table from 18:15 on, and the later rows under the flags file, follow in the next commit |
| 23:35 | f44963a | This table's rows from 18:15 on and the later rows under the flags file, with this page's status line, opening, pending list and sources brought to the end of the build; the row for 6d714e9 under the flags file corrected (44e31d2, 23:53) to describe flag 39 as that commit recorded it |
| 23:58 | ffac01a | References to the retired build-state section replaced on the conflicts register and the gate's page; the home page's reading guide adds "Conjecture:" to the folded headings |

### The flags file

`review/wiki-build-flags.md` lists the suspected errors in the source documents that the wiki's verifiers found. The wiki quotes the sources as written and corrects none of them; each item awaits Paul's ruling, and a topic page that quotes a flagged statement points to its item: the final pass's sweeps added the pointers then missing, the post-audit commits added those for the later flags, the commits after flag 43 added its own, and flag 44's stands where [the signature obstruction](/wiki/gravity/spin-2-fields/signature-obstruction#what-it-assumes-t) states the exception ([after the initial build](#after-the-initial-build-2026-10-22)). Items were added as they were found, and the audits then gave items 1–43 their verdicts:

| Time | Commit | Items | Subject |
| --- | --- | --- | --- |
| 2026-10-21 14:06 | 2b43d4d | 1–10 | the first record, from waves 1 and 2: among them the null polarizations of #5, the misalignment potential of #7, the mass formula and wording of the Debt-1 results, and smaller pointers |
| 14:14 | 27a92a7 | 11 | the tadpole coefficient of model II |
| 14:18 | 2e7fc5d | 12–13 | the zero mode of V_b; a Monte Carlo error figure |
| 14:24 | fe3b759 | 14 | the square-root eigenvalue convention in #7 |
| 14:30 | ab24319 | 15 | a wording about η in #6 |
| 14:46 | ae94e66 | 16 | the handoff's machine-verification mark on the Debt-3 shortfall, with no script behind it |
| 14:48 | 6d0e156 | 17 | two conventions for the gate, a √2 in μ |
| 14:50 | f6a9830 | 18 | the date #1 gives for baryogenesis |
| 14:55 | d1ee3fa | 19 | the regime of the classicality corollary |
| 15:03 | e3ab86f | 20 | #11's reference [23] |
| 15:23 | 5327429 | 21 | the Kibble–Zurek range in round-3 ruling 3 |
| 15:25 | 16bbacb | 22 | the N_eff interval in #14 |
| 15:27 | e0eb18c | 23–25 | the locus a·ã = 1; two minor items |
| 15:36 | dde537c | 26 | the handoff's description of Data Release 3 |
| 15:58 | 5078f50 | 27 | the sign of the dark-energy potential |
| 16:15 | 293dcc3 | 28 | the formula for the magnetic coupling in #11 §11.2 |
| 16:47 | aca97b2 | 29–30 | two items in #13 |
| 17:26 | 36bdacb | 31–32 | two leads from the prediction pages |
| 17:28 | 9dbcf3a | 33–34 | the coverage and constants of `verify/soliton_obituary.py` |
| 18:15 | ce26397 | 35–38 | a section pointer in the round-3 pre-registration; where #11 places the figures "66.58 vs 63.72"; the README's monopole clause; stale details of the root `CLAUDE.md`. Flags 7 and 23 extended |
| 20:23 | 6d714e9 | 39–42 | from the final pass: the reciprocity parity of the metric fluctuation under #11 §6's Z → −Z⁻¹; the naive toy potential at frozen H; a toy-note result listed as shown by executed code; a round-4 revision recorded as applied that was not. Flags 6, 7 and 38 extended |
| 21:28 | d89b457 | 1–42 | the audit: every flag re-checked by independent agents told to refute it, two for each of the eleven mathematical flags (one defending the source, one recomputing from scratch) and one for each of the rest. Result: 32 confirmed, 8 depend on a convention or a reading the documents support, 2 unclear because they rest on model memory, none refuted. Flag 39 reworded: the documents state two actions of ρ on the spin-2 sector, not none |
| 2026-10-22 13:20 | 153b482 | 43 | "the thawing corridor in the CPL crossing quadrant", CPL being the [Chevallier–Polarski–Linder parametrization](/wiki/cosmology/dark-energy/cpl-parametrization) of the dark-energy equation of state: the program's corridor lies in the region of the w₀–wₐ plane where the fits of DESI's Data Release 2 lie, and the slope, not the region, separates the two. The flag came with its own audit, two independent checks, one defending the documents and one recomputing from scratch, and both confirmed it |
| 18:08 | 91c5ac9 | 44 | "#6 §2 without the gauge invariance", minor: a kinetic term invariant only under the transverse diffeomorphisms and the Weyl rescalings, that of linearized unimodular gravity, is also free of ghosts, so "the gauge invariance" overstates while the conclusion stands. Raised after the audit by the verifier of the signature obstruction, with two references from model memory; not yet audited |

The flags file dates the audit 2026-10-22, and its commit carries 2026-10-21. The verdicts on flags 1–42 are in `review/wiki-build-checks/flag-audit.json`, and the auditors' scripts and outputs in `review/wiki-build-checks/audit/`. Flag 43's audit, also dated 2026-10-22, is recorded under the flag, with its scripts and outputs in `review/wiki-build-checks/corridor/`. Flag 44 is marked not yet audited; the file records one check, the page verifier's, and no independent refuters. Each flag is listed with its verdict, or flag 44 with its audit status, and the page that discusses it under [pending rulings](/wiki/status/open-problems#pending-rulings).

## After the initial build: 2026-10-22

The day after the initial build brought a rule on how the wiki states negative results and a pass that applied it, pages of their own for topics of established physics until then treated inside other pages, a further flag, a worksheet for Paul's rulings on the flags, a second round of pages of their own and a flag raised by one of their verifiers, a correction to how the gate computes heading anchors, and a static site built from the wiki.

| Time | Commit | Event |
| --- | --- | --- |
| 2026-10-22 09:50 | 458cfc3 | `wiki/CLAUDE.md` adds to its rules on wording: "Negative results are stated, not celebrated." A dead or rejected claim is reported as "what was claimed, what killed it, what survives", with no lessons drawn about the program's honesty, rigor or skepticism; where a source says such things, it is quoted only on the page that reports that document's self-assessment |
| 09:53 | 1ee727c | The tone pass, committed by section as "Wiki tone" to 3e4d52c (09:56): negative results stated plainly on the pages of gravity, the dark-matter candidates, cosmology and duality, relativity and the predictions, symmetry breaking, the home page and registers, the program and phase space, dark matter, and method and history |
| 10:01 | 0139bf5 | The tone pass's last commit: three gravity pages and the glossary give calc note #7's count of structural tests without its "could each have killed" framing; the clumping obituaries drop #11 §2's ranking of negative results as the most reliable, which the method pages keep; the predictions index's description, the notation page's flag count and the collaboration page's sentence on the build state brought up to date |
| 11:12 | ea66c70 | [The CPL parametrization](/wiki/cosmology/dark-energy/cpl-parametrization) gets its own page: the Chevallier–Polarski–Linder (CPL) form w(a) = w₀ + wₐ(1 − a), in which surveys report a changing w and the program states [row 4](/wiki/predictions/dark-energy-drift), with a summary left on [quintessence and the equation of state](/wiki/cosmology/dark-energy/quintessence). Verifier fixes follow: "w₁ notation clash, positive-density qualifier, early-time and extrapolation wording" (aa6a76b, 11:16), and more at d5e82b1 (11:31) |
| 12:07 | f11f4b9 | Topics of established physics until then treated inside other pages get pages of their own, in commits to e246113 (12:17): [Inverse-Higgs constraints](/wiki/symmetry-breaking/inverse-higgs-constraints), [the cosmological constant Λ](/wiki/cosmology/dark-energy/cosmological-constant), [the equivalence principle](/wiki/gravity/spin-2-fields/equivalence-principle), [Planck units and the two Planck masses](/wiki/gravity/spin-2-fields/planck-units), [Yukawa forces and their range](/wiki/gravity/spin-2-fields/yukawa-forces), [Big Bang nucleosynthesis](/wiki/cosmology/early-universe/big-bang-nucleosynthesis) and [the cosmic microwave background](/wiki/cosmology/early-universe/cosmic-microwave-background), [the Witten effect](/wiki/electric-magnetic-duality/monopoles/witten-effect), [the transfer cross-section σ_T](/wiki/dark-matter/halo-astrophysics/transfer-cross-section) and [the Bullet Cluster](/wiki/dark-matter/halo-astrophysics/bullet-cluster), [thermal freeze-out](/wiki/dark-matter/candidates/thermal-freeze-out), and [de Sitter space](/wiki/cosmology/dark-energy/de-sitter-space) |
| 12:56 | 4229637 | "Wiki: link the newly promoted pages": the new pages linked from the pages that mention them across the wiki, with the [glossary](/wiki/glossary), the [notation](/wiki/notation) and the [references](/wiki/references) updated |
| 13:06 | 3aa68a8 | Verifier fixes for the promoted pages, one commit per page as "Wiki: verifier fixes", to 27056f5 (13:16) |
| 13:20 | 153b482 | Flag 43 added to `review/wiki-build-flags.md` with its own audit, second in its "Where to start" list, after flag 27: the program's [thawing corridor](/wiki/cosmology/dark-energy/thawing-and-freezing#where-the-classes-lie-in-the-wwₐ-plane) lies in the region of the w₀–wₐ plane where the fits of DESI's Data Release 2 lie, and what separates the two is the slope ([the flags file](#the-flags-file)) |
| 13:33 | 9777140 | Flag 43 in the wiki: the CPL page's opening rests the pressure on the release's crossing, and a new section, [the corridor and DR2's crossing](/wiki/cosmology/dark-energy/cpl-parametrization#the-corridor-and-dr2s-crossing), reports the flag; pointers follow where other pages state the corridor beside the crossing (92c695b, 13:37), then the registers (06aea0c, 13:38). This page's rows from 23:35 on follow in the next commit |
| 13:58 | b9a0ea5 | "Wiki: flag-43 follow-up check": the CPL page attributes the crossing redshifts and its rough Gaussian approximation to the flag, the pending rulings link the corridor and the release's crossing, and the flag-43 row of [the flags file](#the-flags-file) spells out CPL |
| 15:29 | 0990cc3 | `wiki/CLAUDE.md` records the /wiki/ prefix of the wiki's links as "a settled choice (Paul, 2026-10-22)", with how such links behave: they do not resolve when the raw Markdown is browsed, they work as written at the domain root of a Hugo site, and under a subpath they work once a link render hook is enabled in the site's configuration |
| 16:22 | 7ca0d7b | The rulings worksheet, `review/wiki-build-rulings.md`: for each of the 43 flags, the text as it stands, a proposed correction and what would follow from accepting it, with a line for Paul's ruling. An accepted ruling corrects the source, moves any executed check into `verify/` and updates the wiki's pointers; nothing in the sources changes until Paul rules |
| 16:37 | 35c1353 | A second round of pages of their own, in commits to 1adaff6 (16:57): [Open: a Monte Carlo with H dynamical](/wiki/symmetry-breaking/toy-models/coset-model/dynamical-h-monte-carlo), the first of the toy work's open ends, until then a folded section of [the frozen-H reduction](/wiki/symmetry-breaking/toy-models/coset-model/frozen-h-reduction); thirteen topics of established physics until then treated inside other pages, [redshift](/wiki/cosmology/scale-factor-duality/redshift), [Stückelberg fields](/wiki/symmetry-breaking/stuckelberg-fields), [the relic yield Y = n/s and entropy dilution](/wiki/cosmology/early-universe/relic-yield-and-dilution), [momentum fibers and the cotangent bundle](/wiki/phase-space/reciprocity/momentum-fibers), [a hidden sector at its own temperature](/wiki/cosmology/early-universe/hidden-sector-temperature), [ghosts and perturbative instabilities](/wiki/gravity/spin-2-fields/ghosts), [the signature obstruction](/wiki/gravity/spin-2-fields/signature-obstruction), [thawing and freezing quintessence](/wiki/cosmology/dark-energy/thawing-and-freezing), [axion-like fields and pseudo-Goldstone bosons](/wiki/cosmology/dark-energy/axion-like-fields), [topological defects and the vacuum manifold](/wiki/symmetry-breaking/topological-defects), [the Kalb–Ramond B-field](/wiki/phase-space/born-geometry/kalb-ramond-field), [the velocity dispersion σ](/wiki/dark-matter/halo-astrophysics/velocity-dispersion) and [the modular group SL(2, ℤ)](/wiki/electric-magnetic-duality/modular-group); and [the Born length λ](/wiki/phase-space/reciprocity/born-length), #13's name for the length behind its maximum force, alive and unreviewed. Most of the pages they came from keep short summaries that link them. The links to them from the rest of the wiki, with the section maps, the glossary, the notation, the references and this page's rows, follow in the next commit |
| 17:43 | 75ad541 | "Wiki: link the second round of promoted pages": the new pages linked from the pages that mention them across the wiki, with the section maps, the [glossary](/wiki/glossary), the [notation](/wiki/notation), the [references](/wiki/references) and this page's rows from 13:58 to 16:37 |
| 17:51 | d3e5891 | Verifier fixes for the second round's pages, one commit per page as "Wiki: verifier fixes", to 039a390 (18:04). The fix to [the signature obstruction](/wiki/gravity/spin-2-fields/signature-obstruction) (c9f347e, 17:58) adds the case of a kinetic term with only part of the gauge symmetry, that of linearized unimodular gravity, with two references from model memory |
| 18:08 | 91c5ac9 | Flag 44 added to `review/wiki-build-flags.md`, minor and not yet audited: calc note #6 §2's "Without the gauge invariance" overstates, since the case above is still a gauge symmetry, and the conclusion that [the momentum graviton X](/wiki/gravity/momentum-graviton) must be gauged is unaffected. The same commit adds the flag's entry to the rulings worksheet, and its index row follows (29162e1, 18:08) ([the flags file](#the-flags-file)) |
| 18:30 | b41f199 | [The gate](/wiki/method/verification/the-gate) computes heading anchors as Hugo does. Its rule had kept subscript and superscript digits, which Hugo drops, and dropped an unpaired underscore after punctuation, which Hugo keeps, so "27 wiki links passed the gate with anchors that do not exist on the built site"; those links, on 15 pages, now name the headings' real anchors. The new rule matched the anchors that Hugo 0.159 and 0.168 wrote for all 3478 wiki headings and 45 edge cases, and the gate now also checks a link whose text holds brackets, which it had skipped |
| 18:34 | 60d2f65 | `site/`, a Hugo site that builds the wiki into static pages "on the stack of Paul's other Hugo sites": the hugo-book theme as a git submodule and a Cloudflare Workers static-assets Worker, to be deployed by hand. It mounts `wiki/` as its content rather than copying it, its build fails on a link to a missing page, and a new script, `scripts/check-site.py`, checks every internal link and anchor in the built HTML. The site's gate, `npm run check` in `site/`, runs `scripts/check.sh`, the build and that script; the commit records it passing, with "site OK, 308 pages, 119927 links", and "Nothing has been deployed." The site's instructions, `site/CLAUDE.md`, follow (8d467a6, 18:34), with `site/` in the root `CLAUDE.md`'s layout and a section on publishing in `wiki/CLAUDE.md`, whose sentence on links under a subpath now names the site's mechanism: the render-hook setting recorded at 0990cc3 has no effect while the theme supplies its own link hook |
| 18:50 | 140dac5 | Flag 44 in the wiki: the [pending rulings](/wiki/status/open-problems#pending-rulings), the home page's reading guide and the notation's flag range, and a pointer where [the signature obstruction](/wiki/gravity/spin-2-fields/signature-obstruction#what-it-assumes-t) states the exception |
| 18:52 | ee8a001 | The [references](/wiki/references) completed for both rounds of promoted pages: the works their pages cite from model memory that the register lacked, among them the two behind flag 44, and the pages missing from the lists of where a work is cited. This page's rows from 17:43 on follow in the next commit |
| 18:58 | ed0ca68 | Timeline rows from 17:43 to 18:52, and flag 44 under the flags file. |
| 19:49 | 503d34d | The wiki gate learns the heading-identifier rules Hugo applies that it had missed; links, emphasis and `{#id}` are no longer allowed inside a heading ([the gate](/wiki/method/verification/the-gate)). |
| 19:50 | 5540adc | The site gate checks every href and src in the built pages, that each wiki page is built once and no `CLAUDE.md` is, and that Hugo's heading identifiers equal the ones the wiki gate computes. |
| 19:50 | aa046dc | The site's `/wiki/` page gets a browser title without the repeated site name. |
| 19:53 | b636936 | Docs: the heading rule, the site gate's checks, how to publish by hand and how to add a domain (`site/CLAUDE.md`, the root and wiki `CLAUDE.md`). |

## The phase-space-diameter note and round 5: 2026-10-26

Paul's question of the day: "Investigate or explain if there is a relationship between the size of our universe in position space and momentum space. Speculate and work through the consequences if so." The worklog treats it as the third part of the queue's item 1, the write-up of the chat-only diameter relation (`HANDOFF.md` §8 item 7), and plans the work in chunks: a research workflow, the note and its script, a pre-registered blind review, the revision, the wiki, and the root `CLAUDE.md`. The times below are the worklog's, in local time; nothing in this section had been committed when it was written (above, [how the record is dated](#how-the-record-is-dated)).

| Time | Commit | Event |
| --- | --- | --- |
| 2026-10-26, time not recorded | — | Chunk 0: the record read, the Python environment created on this machine, and the baseline `scripts/check.sh` passing, "306 wiki pages" |
| 15:15 | — | Chunk 1 running: a research workflow of "8 agents" covering the literature with live retrieval and a novelty audit, an independent re-derivation, an independent recomputation of the numbers, a steelman of the chat claim and a sweep of the record; "the independent numbers agent has returned and matches every number of my draft script". The drafts are kept outside the repository, and the draft of the round-5 pre-registration where the referees cannot read it |
| 15:30 | — | Chunk 1 done, with what changed the plan: prior art for the self-dual length in the Born-geometry papers the program cites, by Freidel, Kowalski-Glikman, Leigh and Minic among others, so that the note's §7 is tagged [T] ([the self-dual cosmic box](/wiki/cosmology/scale-factor-duality/self-dual-cosmic-box)); Born 1938 "read in full", in which Born pairs the radius of Einstein's closed universe with a momentum-space radius and declines to connect them ([the † literature battery](/wiki/method/literature-battery)); Grosse and Wulkenhaar's reading of √Ω as the ratio of the Planck length to the size of the universe; Lee et al. 2020's bound on a heavy graviton; no reading that makes the chat's claim of a square at the bounce true for one region; and leads outside the note |
| 15:55 | — | Chunk 2: the note's version 1.0, `papers/phase-space-diameter.md`, and its script, `verify/phase_space_diameter.py`, wired into `scripts/check.sh`; the full gate passes. "The script caught two of my own numbers (ln A₀ = 213.5, not 213.8; the two-region aspect 8×10²⁹, not 8×10²⁸) and one script bug before they reached the note" ([the phase-space-diameter script](/wiki/method/verification/phase-space-diameter-script)) |
| 15:55 | — | Round 5 dispatched to two blind referees, "dispatched 2026-10-26T15:55-07:00", with two hashes (`SHA-256`) recorded before dispatch: the pre-registration, `b5094b65cf969c8106353059e14bc8f66497076dfa3ae3ef262bda3a0fe3033b`, kept outside the repository until both referees had returned, and the manuscript copy sent to both, `2ed53d537d03c26273564cb4ed81b70117cc67853b08239a28149e927f3425a4` ([pre-registration](/wiki/method/review/pre-registration)) |
| 16:45 | — | Chunk 3: both referees grade the note B, confidence 0.75, with the same weakest link, the bound on X's range, whose coupling formula had dropped the ratio of the two metrics' backgrounds. The adjudication upholds the finding in substance and does not uphold referee A's value for the ratio (R1), upholds R2–R13 and accepts R14–R16; the forecast scores a hit on the verdict and on the weakest link's location and premise, and misses on the number of arithmetic findings and on novelty. The records: `review/round5-preregistration.md` (its hash verified), `review/round5-adjudication.md` and `review/round5/` ([Round 5](/wiki/method/review/round-5)) |
| 17:00 | — | Chunk 4: the note's version 1.1 with the accepted revisions, of which one, the citation of Hur et al. 2025 that ruling R15 lists, reached the note only with the fixes of 17:55 ([Round 5](/wiki/method/review/round-5)); the script extended ("c-dependent bound, broken vacua, CKN saturation, conventions", CKN being Cohen–Kaplan–Nelson); the root `CLAUDE.md` updated: the note in the layout and in "Since the handoff", the queue reduced to `HANDOFF.md` §8 items 5–6 with an optional round-6 review of the toy note, the leads, and two rules added to its method; the acronyms the note's pages need added to `scripts/wiki-acronyms.txt` |
| 17:55 | — | Chunk 5 written: "Nine writer agents updated 61 wiki files (eight new pages)", and `scripts/check-wiki.py` passes on 314 pages. The worklog had planned the chunk as "the diameter page, an obituary for any dead sub-claim, registers": [the phase-space diameter relation](/wiki/cosmology/scale-factor-duality/phase-space-diameter) rewritten from the note, no longer a chat-only page; new pages for [Obituary: the square rectangle at the bounce](/wiki/cosmology/scale-factor-duality/square-at-the-bounce), [the self-dual cosmic box](/wiki/cosmology/scale-factor-duality/self-dual-cosmic-box), [Obituary: the self-dual length as a program scale](/wiki/cosmology/scale-factor-duality/self-dual-length-obituary), [the laboratory bound on X's range](/wiki/gravity/momentum-graviton/range-bound), [Gaussian wave packets on the Siegel half-plane](/wiki/phase-space/modular-field/gaussian-states), [squeezed cosmological perturbations](/wiki/cosmology/early-universe/squeezed-perturbations), [the phase-space-diameter script](/wiki/method/verification/phase-space-diameter-script) and [Round 5](/wiki/method/review/round-5); and updates to the registers and to pages that described the relation as chat-only or queued, this one among them |
| 17:55 | — | The writers' findings in the sources, fixed after chunk 5: Hur et al. 2025 added to the note's §7, as ruling R15 had claimed; the adjudication's statement on the referees' access to Born's papers corrected; the reviewed version 1.0 kept as `review/round5/manuscript-v1.0.md`, its hash verified; the worklog's superseded draft numbers marked; and the script's labels, its check that the dark-energy ratio does not depend on H₀, its interpolated M_X and its Fubini–Study check tightened ([Round 5](/wiki/method/review/round-5); [the phase-space-diameter script](/wiki/method/verification/phase-space-diameter-script)) |
| 18:25 | — | The machine crashes during the verification pass over the wiki's update. No verifier edit had reached disk. The session's scratch files are lost, after everything the record needs had been copied into the repository (the pre-registration, the referees' notes, scripts and outputs, the reviewed version 1.0 and the source hashes in the worklog); the literature and review agents' full returns survive in the workflow journals. After the crash the script's 85 checks pass, and `scripts/check-wiki.py` passes on 314 pages. The verification is relaunched at 18:26, with its fixes, the full `scripts/check.sh`, `npm run check` in `site/` and the summary for Paul still to do |
| 18:55 | — | The verification pass done: "five agents, 98 fixes across the new and changed wiki pages"; the wiki's rulebook now ranks the note and the round-5 adjudication among its sources, and [the conflicts register](/wiki/history/documents/source-conflicts) records the note's reading of the \|Z\| = 1 locus against #11's (flag 23). Follow-ups applied afterwards, among them three register links to folded sections and four wordings in the round-5 adjudication |
| 19:00 | — | Chunk 5 done: `npm run check` in `site/` passes, covering "every verify script (the diameter script's 85 checks), the wiki gate on 314 pages, the Hugo build, and the HTML check", which found 316 pages, 141,360 links and 3,633 heading identifiers in order. "Nothing deployed, nothing committed" |
| 19:10 | 97934f2, f40e250, bda03e3, 7d609b0 | The day's work committed at Paul's request, in four commits: the note with its script and worklog, the round-5 record, the root `CLAUDE.md`, and the wiki. Not pushed. The pre-registration's commit comes after the review; the hash recorded before dispatch is what dates it ([Round 5](/wiki/method/review/round-5)) |

The worklog's entry for chunk 3 counts the rulings as the adjudication's table does: "R2–R13 upheld, R14–R16 accepted (fifteen further findings)". Its entry for chunk 4, "Note v1.1 with every accepted revision", holds since the fixes of 17:55, which added the one citation that ruling R15 had claimed and the note lacked.

## Pending

- **The queue.** Since 2026-10-26 the root `CLAUDE.md` gives it as "HANDOFF §8 items 5–6: the partially-massless comparison and the † literature battery (Born 1938 and 1949 were retrieved for the diameter note; see its §4)", then an optional round-6 review of the toy note, "but only before any external use" ([the partially-massless comparison](/wiki/gravity/palindromic-branch/pm-comparison); [the † literature battery](/wiki/method/literature-battery)). From 2026-10-20 (commit 6606734) it had read "HANDOFF §8 items 5–7: the partially-massless comparison, the † literature battery, the phase-space-diameter note", then an optional round-5 review of the toy note; the note was written and reviewed in round 5 on 2026-10-26 ([the phase-space diameter relation](/wiki/cosmology/scale-factor-duality/phase-space-diameter)). How the queue changed since the handoff is set out on [CLAUDE.md and the README](/wiki/history/documents/project-instructions) and [open problems and the queue](/wiki/status/open-problems).
- **Submission.** #11 is "not for submission until the † audit (open item 10) completes" (#11, closing provenance note).
- **Rulings on the flags.** All 44 items of `review/wiki-build-flags.md` await Paul's rulings, items 1–43 with their audits' verdicts beside them and item 44 not yet audited ([pending rulings](/wiki/status/open-problems#pending-rulings)); `review/wiki-build-rulings.md` proposes a correction for each and gives a line for the ruling. The round-5 adjudication recommends accepting flags 23 and 24, on the locus a·ã = 1 and on "square exactly at the bounce".
- **DESI Data Release 3 (DR3)**, "expected late 2026" (`HANDOFF.md` §2). The handoff's kill conditions: a robust constant w = −1 kills the [τ sector](/wiki/cosmology/dark-energy/tau-quintessence), a robust intrinsic w < −1 kills the framework outright, and continued thawing keeps it alive ([row 4](/wiki/predictions/dark-energy-drift)).

## What the record does not date

- The addenda v0.2–v0.6 of #1 and the artifacts #2–#15; only their order is recorded.
- Review rounds 1 and 2 and their pre-registrations.
- The runs of the round-3 and round-4 referees, beyond the commits that bracket them and the round-4 notes' "Started 2026-10-19".
- The wiki's design round, recorded only as 2026-10-20, and the reboot recorded in the build state of 16:31.
- The runs of the flags' auditors, beyond the commit that records them (d89b457); the flags file dates the audit 2026-10-22, and the commit carries 2026-10-21. The runs of flag 43's two auditors, beyond the commit that records them (153b482).
- On 2026-10-26: the start of the work (chunk 0), which the worklog records without a time; the start of the wiki update (chunk 5), which it records only as written at 17:55; and the runs of the round-5 referees, beyond the dispatch at 15:55 and the worklog's entry of 16:45 that records the adjudication.

## Sources

- `CLAUDE.md` 'Since the handoff' — the post-handoff decisions, the lessons added in 96f58da and e3ce9eb, the diameter note done, and the current queue
- `notes/phase-space-diameter-worklog.md` — Paul's question of 2026-10-26, the chunks, the times of the day's entries, the hashes recorded before dispatch and the dispatch time, the count of the rulings, the writers' source findings fixed at 17:55, and the crash of 18:25 with the gate state after it
- `papers/phase-space-diameter.md` header — version 1.1 after round 5; §4, §5 — what the note records of Born 1938 and 1949
- `review/round5-preregistration.md`, `review/round5-adjudication.md` — round 5: the forecast kept outside the repository, "no commit authorization", the reviewed version 1.0 kept as `review/round5/manuscript-v1.0.md`, the verdicts, rulings R1–R16, the scoring, the revisions and the recommendation on flags 23 and 24
- `verify/phase_space_diameter.py`, `scripts/check.sh` — the note's script and its place in the gate
- `papers/broken-born-checkpoint-v2.md` header — the v2.1 (2026-10-19) and v2.2 (2026-10-20) changes; §3 — Snyder's lineage and the credit to Freidel–Leigh–Minic; §12 — the soliton candidate "retired 2026-10-19"; References — the literature entries with their marks; closing provenance note — "not for submission until the † audit"
- `review/round4-adjudication.md`, `review/round4-preregistration.md`, `review/round4/referee/audit-notes.md` — round 4: the neutral subject, the referee's start date and interruption, the verdict and the revisions "applied 2026-10-20 in commit 6606734"
- `review/round3-adjudication.md`, `review/round3-preregistration.md` — round 3: the verdict, the decisions Paul delegated on 2026-10-19, the commit-subject lesson, and the month of arXiv:2607.20843 (ruling 3)
- `papers/reciprocity-toy-models.md` — the toy-model note, v1 at d9a06ac and v2 at 6606734
- `HANDOFF.md` §1 — "developed September–October 2026" and the unreconciled count of reviews; §3 — the creation order of #1–#15 and the rounds' use of #15; §5, §6 — rounds 1 and 2 and the first attempt at round 3 on 2026-10-17; §8 — the queue at the handoff; §2 — DESI DR3 and the kill conditions; footer — the handoff's date
- `review/v3-worklog.md` — the recomputation of #14 v2, the literature report, Paul's decisions on F1 and F2, item O3, and v3 (2026-10-19)
- `notes/toy-lagrangian.md` — the dated criteria and chunks (2026-10-19), the corrected chunk-2 sign, the S5 literature check, and the write-up and review (2026-10-19/20)
- `notes/knot-dark-matter-standalone.md` banner — "Withdrawn (2026-10-19)"; the earlier banner, "Status (2026-10-19)", is in the file as committed at 96f58da, when it was still in `papers/`
- `notes/broken-born-theory.md` header — "Version 0.1, September 2026"; §0, §6 — the corrected heuristic of the development discussion; 'Addendum (v0.2)' to 'Addendum (v0.6)' — the order of the Debt-3 and Debt-1 results
- `notes/debt1a-geometric-core.md` header — "Overnight working note"; `notes/debt1a-ii-X-classification.md` §3 — "the second turn of this whole conversation"
- `notes/broken-born-program-v1.md` header — v1.0
- `popsci/angle-of-the-mirror.md` subtitle — "a week"
- `README.md` — the initial commit's description
- `wiki/CLAUDE.md` 'Build state', retired at b03903c (its last version is at 51ede3e) — the wiki's design round, breadth pass, depth waves and the plan of the final pass; 'Keeping it current' — the build recorded on this page; 'Voice' — the rule on negative results added at 458cfc3; 'Links' — the /wiki/ prefix recorded as a settled choice at 0990cc3, and the sentence on subpaths and the slug rule revised at 8d467a6; 'Publishing' — the site, added at 8d467a6
- `site/CLAUDE.md` 'The gate', 'Deploying (manual)' — the site's gate and its three layers of link checks; deployment by hand
- `review/wiki-build-flags.md` — the flags file, items 1–44, the audit's date, method and result, flag 43's own audit and flag 44's audit status
- `review/wiki-build-rulings.md` — the rulings worksheet: one entry per flag, with a proposed correction and what an accepted ruling does; flag 44's entry and index row, added at 91c5ac9 and 29162e1
- `review/wiki-build-checks/flag-audit.json` — the audit's verdicts on flags 1–42; `review/wiki-build-checks/README.md` — the executed checks and the auditors' folders, `review/wiki-build-checks/audit/` and, for flag 43, `review/wiki-build-checks/corridor/`
- `git log` — commit hashes, subjects and times (local, −0700); the messages of 96f58da and 5b6efaa — the gate failing by design after round 3 and passing again; of 2c6f857 — the underscore rule and the eight corrected links; of d89b457 — the audit's result and the rewording of flag 39; of 0139bf5 — the last details of the tone pass; of 153b482 — flag 43's two audits; of b41f199 — the anchor rule, the 27 links corrected on 15 pages and the comparison with the anchors Hugo writes; of 60d2f65 and 8d467a6 — the site, its check and its documentation, and why the sentence on subpaths changed
