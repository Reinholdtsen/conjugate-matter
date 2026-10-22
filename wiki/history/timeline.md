---
title: "Timeline"
weight: 10
status: record
description: "Dated events from Born's 1938 paper to the pending DESI DR3 release: the claude.ai era in creation order, the move to the repository, rounds 3 and 4, the checkpoint's versions, and the wiki's build with its flags file."
sources:
  - "CLAUDE.md 'Since the handoff'"
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
  - "wiki/CLAUDE.md 'Build state'"
  - "review/wiki-build-flags.md"
---

*The timeline lists the program's events in date order, from Max Born's paper of 1938 to the third data release of the Dark Energy Spectroscopic Instrument (DESI), which the handoff names the program's external clock, since its data can kill the dark-energy sector or the whole framework. The work done on claude.ai in September and October 2026 is almost entirely undated, so those events follow the creation order of the artifacts in `HANDOFF.md` §3. From the move to this repository on 2026-10-19, the commit history dates each step to the minute: review round 3 and the retirement of the soliton candidate, the toy models and review round 4, the checkpoint's versions 2.1 and 2.2, and the building of this wiki, with the file of suspected source errors its verifiers keep.*

**Status:** Record, current to the afternoon of 2026-10-21 — untagged — dates come from the documents' own headers and dated entries and from `git log` (commit times are local, −0700). Before the handoff the record gives two dates, "September 2026" for #1 v0.1 and 2026-10-17 for the first attempt at round 3; the other claude.ai events follow `HANDOFF.md` §3's creation order, and where review rounds 1 and 2 fall in that order is inferred, not recorded.

## How the record is dated

The record has two layers.

- **Before the move.** Artifacts #1–#15 were written in one conversation on claude.ai and carry almost no dates. #1's header reads "Version 0.1, September 2026". The handoff says the program was "developed September–October 2026" (`HANDOFF.md` §1) and dates two events, the first attempt at round 3 (§6) and its own preparation (footer). Everything else is ordered by the handoff's inventory, headed "Artifact inventory (creation order)" (§3), and by the version headers and addenda of the documents. The first popular article, #10, describes the work it narrates as "a week" of stress-testing (its subtitle).
- **From the move.** The repository's commits date every later step. Each row gives the time of the commit that recorded the event (local time, −0700) and its hash, so `git show` with the hash displays the change. The time is when the record was committed: an event such as a blind audit ran between the commits that bracket it, and its own time is given only where a document records it.

## Before the program

The literature the program starts from, builds on or is measured against has its own dates. Bracketed numbers are #11's reference list, with its marks: † cited from model memory, [S] retrieved by live search ([References](/wiki/references)).

| Year | Work | In the program |
| --- | --- | --- |
| 1938 | M. Born, "A suggestion for unifying quantum theory and relativity," Proc. R. Soc. Lond. A 165, 291 [1†] | the origin of [Born's question](/wiki/program/borns-question) |
| 1947 | H. S. Snyder, "Quantized space-time," Phys. Rev. 71, 38 [4†] | the start of the lineage of [curved momentum space](/wiki/phase-space/reciprocity/curved-momentum-space) (#11 §3) |
| 1949 | M. Born, "Reciprocity theory of elementary particles," Rev. Mod. Phys. 21, 463 [2†] | [Born reciprocity](/wiki/phase-space/reciprocity/born-reciprocity) |
| 2001 | N. Boulanger, T. Damour, L. Gualtieri, M. Henneaux, "Inconsistency of interacting, multi-graviton theories," Nucl. Phys. B 597, 127 [8†] | [the multi-graviton no-go](/wiki/gravity/spin-2-fields/multi-graviton-no-go), which excludes a massless [momentum graviton](/wiki/gravity/momentum-graviton) |
| 2014 | L. Freidel, R. G. Leigh, D. Minic, "Born reciprocity in string theory and the nature of spacetime," Phys. Lett. B 730, 302 [3†] | Born geometry ([the structures ω, η, H](/wiki/phase-space/born-geometry/born-structures)) |
| 2015 | Freidel, Leigh, Minic, "Metastring theory and modular space-time," JHEP 06 (2015) 006, arXiv:1502.08005 [26S] | [broken Born duality](/wiki/phase-space/reciprocity/broken-born-duality), and since #11 v2.1 the attribution of [the compatibility theorem](/wiki/phase-space/born-geometry/compatibility-theorem) |
| 2025 | DESI Collaboration (M. Abdul-Karim et al.), "DESI DR2 Results II: Measurements of Baryon Acoustic Oscillations and Cosmological Constraints," arXiv:2503.14738 [21S] | Data Release 2 (DR2) and its phantom crossing ([DESI DR2's phantom crossing](/wiki/cosmology/dark-energy/desi-dr2-phantom-crossing)) |
| 2026, July | D. Liveoak, A. Maharana, J. D. Wells, "Dark monopoles, bounds on hidden sectors, and cosmological implications," arXiv:2607.20843 [29S] | prior art for the [retired soliton candidate](/wiki/dark-matter/candidates/soliton-candidate/obituary) ([topological dark matter in the literature](/wiki/dark-matter/candidates/soliton-candidate/prior-art)); the month is from round-3 ruling 3 |

## The claude.ai era

The numbers in the first column are the artifact numbers of `HANDOFF.md` §3, in its creation order.

| # | Date | Event | Record |
| --- | --- | --- | --- |
| — | not recorded; before #1 | The development discussion: Paul's founding suppositions, eleven ideas later audited in #11 Appendix A ([founding suppositions](/wiki/program/founding-suppositions)); a heuristic duality dictionary, w_eff = −2 − w̃, which #1 corrected ([Obituary: conjugate collapse powers our expansion](/wiki/cosmology/scale-factor-duality/collapse-powered-expansion)); and bimetric gravity, raised in "the second turn of this whole conversation" | #1 §0, §6; #6 §3; #11 Appendix A |
| 1 | September 2026 | The lab notebook, "Version 0.1": postulates P1–P5 with the [original P2](/wiki/program/postulates/original-p2), an action, a predictions table of ten rows, six open problems and "three named debts standing between this document and a paper" ([the lab notebook](/wiki/history/documents/lab-notebook); [the three debts](/wiki/history/debts); [the predictions table](/wiki/predictions/table-history)) | #1 header, §9, §11, §12 |
| 2 | not recorded | Calc note debt3a: the particle island; the clumping criterion fails by 10²⁸–10³¹ ([the Debt-3 calc notes](/wiki/history/documents/debt-3-notes)) | `HANDOFF.md` §3 |
| 3 | not recorded | Calc note debt3b: the wave island and its two scenarios | `HANDOFF.md` §3 |
| 4 | not recorded | Calc note debt3c, which "closes Debt 3 (negative)"; the notebook's addendum v0.2 withdraws rows 3 and 4 of its table ([Obituary: velocity clumping, the founding image](/wiki/dark-matter/momentum-clumping/founding-image)) | `HANDOFF.md` §3; #1 'Addendum (v0.2)' |
| 5 | not recorded; written "overnight" | Calc note debt1a, an "Overnight working note": the compatibility theorem, the repair of P2 to [P2′](/wiki/program/postulates/p2-prime), [the modular field](/wiki/phase-space/modular-field/modular-field-z) and [the gate mechanism](/wiki/dark-matter/conjugate-matter/gate-mechanism); addendum v0.3, also headed "overnight" ([the Debt-1 calc notes](/wiki/history/documents/debt-1-notes)) | #5 header; #1 'Addendum (v0.3, overnight)' |
| 6 | not recorded | Calc note debt1a-ii: X classified as a massive spin-2 field; addendum v0.4 | `HANDOFF.md` §3; #1 'Addendum (v0.4)' |
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
| 2026-10-18 23:07 | 6b8f599 | Initial commit: a README describing the repository as "Physics hypothesis explaining dark matter and missing magnetic monopoles" ([CLAUDE.md and the README](/wiki/history/documents/project-instructions)); the monopole explanation is dead ([Obituary: conjugate monopoles explain the null result](/wiki/electric-magnetic-duality/monopole-explanation)) |
| 2026-10-19 10:28 | 8d588f6 | "Import session from regular Claude.": `HANDOFF.md` and artifacts #1–#15 copied into the repository |
| 10:35 | 008c3ee | The import arranged into `papers/`, `notes/`, `popsci/`, `review/` and `verify/` as `HANDOFF.md` §9 suggests; the root `CLAUDE.md` written; `verify/battery.py`, the handoff's Appendix A turned into assertions, and `scripts/check.sh`, "the definition of done": the first [gate](/wiki/method/verification/the-gate). #1–#10, #12, #13, #15 and `HANDOFF.md` have not changed since |

## Round 3 and the retirement of the soliton candidate: 2026-10-19

The handoff's queue began with cutting v3 of #14 and re-running the blind audit on it (`HANDOFF.md` §8, items 1 and 2).

| Time | Commit | Event |
| --- | --- | --- |
| 2026-10-19 10:41 | 678e48a | Every number of #14 v2 recomputed by a new script, `knot_numbers.py` in `verify/` (since replaced); the v3 worklog begun |
| 10:59 | 2b72da0 | The literature check of the worklog, done by a subagent with web access "with no citations from memory" |
| 13:23 | 2eb58de | Paul's decisions on F1 and F2, "Decided (Paul, 2026-10-19)": the benchmark mass moves to M ≈ 3×10¹³ GeV, and the hidden sector's elementary coupling is read as weak, its solitons as strongly coupled ([Obituary: the coupling α_d ≈ 34](/wiki/dark-matter/candidates/soliton-candidate/alpha-d-coupling#superseded-f2-which-coupling-sets-the-soliton-mass)). The same commit logs item O3: #13's two dual cones are to be fixed before any paper claims more, "raised by Paul, 2026-10-19" ([Open: the two dual cones](/wiki/conjugate-relativity/two-cones-inconsistency)) |
| 13:25 | d15cd4a | The minimal hidden sector scripted: its stable W′ bosons overclose the universe, so v3 needs a light dark doublet ([W′ overclosure](/wiki/dark-matter/candidates/soliton-candidate/w-prime-overclosure)) |
| 14:42 | 5dbaa82 | #14 v3 cut from the round-2 pending list and the two decisions |
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
| 18:59 | d112dd4 | The prior-art survey S0, with no existing action found that breaks Born reciprocity spontaneously with η as the order parameter; the Grosse–Wulkenhaar (GW) route chosen for chunk 2 |
| 20:45 | 4923112 | Chunk 2: the vacua of the complex self-dual GW model break the duality classically; `verify/toy_gw.py` ([model II](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar)) |
| 21:02 | 4f989e6 | Chunk 3: S4 passes in the coset model only with a τ-type potential, the one round 4 later found unbounded below ([Obituary: the naive ρ-preserving potential](/wiki/symmetry-breaking/toy-models/coset-model/naive-potential)), and the classical breaking of the GW model does not survive quantization; `verify/toy_s4.py` |
| 21:52 | 56485d3 | Chunk 4: the S5 computation on the locality of matter; `verify/toy_s5.py` |
| 22:16 | bed9306 | Chunk 4 concluded after a literature check by a subagent: S5 passes in its weak form only, the pre-registered predictions score four hits, and acceptance criterion 1 is met in the referees' wording ([acceptance criterion 1](/wiki/symmetry-breaking/toy-models/acceptance-criterion)) |
| 22:26 | d9a06ac | Round 4 pre-registered under a neutral commit subject, with the toy-model note v1 as the manuscript ([review round 4](/wiki/method/review/round-4)); the same commit corrects a sign reversed in the worklog's chunk-2 results, marked "Corrected 2026-10-19" |
| 22:29 | 6ee74d0 | #11 §3 credits Freidel–Leigh–Minic for "broken Born duality", a change of v2.2 committed ahead of the version |
| 2026-10-19, time not recorded | — | The round-4 blind audit, "Started 2026-10-19"; it "was interrupted once by a rate limit and resumed from its own transcript" |
| 2026-10-20 11:13 | e3ce9eb | The adjudication: verdict B; the potential of the note's §4 is unbounded below once H is dynamical ([Obituary: the naive ρ-preserving potential](/wiki/symmetry-breaking/toy-models/coset-model/naive-potential)). Two lessons enter the root `CLAUDE.md`: check the stability of the unreduced model, and give Monte Carlo numbers error bars from independent runs ([the reduced-model stability rule](/wiki/method/verification/reduced-model-stability); [the Monte Carlo error-bar rule](/wiki/method/verification/monte-carlo-error-bars)) |
| 18:54 | 6606734 | The toy-model note v2 and #11 v2.2, "amended 2026-10-20"; the root `CLAUDE.md` records the toy Lagrangian as done and sets the current queue |
| 18:54 | 5ca7d81 | The adjudication marks the revisions applied |

## The wiki and its flags file: 2026-10-20 and 21

The build is recorded in the section 'Build state' of `wiki/CLAUDE.md` and in the commits. The build state labels the fourth depth wave "2026-10-21/22"; its commits carry the date 2026-10-21.

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

### The flags file

`review/wiki-build-flags.md` lists the suspected errors in the source documents that the wiki's verifiers found. The wiki quotes the sources as written and corrects none of them; each item awaits Paul's ruling, and a topic page that quotes a flagged statement is to point to its item (the build state lists a sweep that adds the pointers still missing). Items were added as they were found; the table runs to item 34, and later items are in the file itself:

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

## Pending

- **The queue.** Since 2026-10-20 (commit 6606734) the root `CLAUDE.md` gives it as "HANDOFF §8 items 5–7: the partially-massless comparison, the † literature battery, the phase-space-diameter note", then an optional round-5 review of the toy note, "but only before any external use" ([the partially-massless comparison](/wiki/gravity/palindromic-branch/pm-comparison); [the † literature battery](/wiki/method/literature-battery); [the phase-space diameter relation (chat-only)](/wiki/cosmology/scale-factor-duality/phase-space-diameter)). How the queue changed since the handoff is set out on [CLAUDE.md and the README](/wiki/history/documents/project-instructions) and [open problems and the queue](/wiki/status/open-problems).
- **Submission.** #11 is "not for submission until the † audit (open item 10) completes" (#11, closing provenance note).
- **DESI Data Release 3 (DR3)**, "expected late 2026" (`HANDOFF.md` §2). The handoff's kill conditions: a robust constant w = −1 kills the τ sector, a robust intrinsic w < −1 kills the framework outright, and continued thawing keeps it alive ([row 4](/wiki/predictions/dark-energy-drift)).

## What the record does not date

- The addenda v0.2–v0.6 of #1 and the artifacts #2–#15; only their order is recorded.
- Review rounds 1 and 2 and their pre-registrations.
- The runs of the round-3 and round-4 referees, beyond the commits that bracket them and the round-4 notes' "Started 2026-10-19".
- The wiki's design round, recorded only as 2026-10-20, and the reboot recorded in the build state of 16:31.

## Sources

- `CLAUDE.md` 'Since the handoff' — the post-handoff decisions, the lessons added in 96f58da and e3ce9eb, and the current queue
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
- `wiki/CLAUDE.md` 'Build state' — the wiki's design round, breadth pass and depth waves
- `review/wiki-build-flags.md` — the flags file, items 1–34
- `git log` — commit hashes, subjects and times (local, −0700); the messages of 96f58da and 5b6efaa — the gate failing by design after round 3 and passing again
