---
title: "Open: the † literature battery (OP10)"
weight: 50
status: open
description: "Every memory-cited (†) reference in #11 and #13 must be checked against its source before external use: what is to be checked, what a check involves, the citation errors found so far, partial progress, and its place in the queue."
provenance: [O]
sources:
  - "papers/broken-born-checkpoint-v2.md §14 item 10"
  - "papers/broken-born-checkpoint-v2.md footer"
  - "papers/broken-born-checkpoint-v2.md 'References'"
  - "papers/broken-born-checkpoint-v2.md §2"
  - "papers/broken-born-checkpoint-v2.md §11.3"
  - "papers/conjugate-special-relativity.md 'References'"
  - "CLAUDE.md 'Since the handoff'"
  - "CLAUDE.md 'Method'"
  - "HANDOFF.md §1"
  - "HANDOFF.md §3"
  - "HANDOFF.md §6"
  - "HANDOFF.md §7"
  - "HANDOFF.md §8"
  - "review/round3-preregistration.md 'Protocol'"
  - "review/round3-adjudication.md 'Rulings'"
  - "review/round3-adjudication.md 'Decisions'"
  - "review/round3-adjudication.md 'Pre-registration scored'"
  - "review/round3/referee/audit-notes.md Step 1"
  - "review/round4-adjudication.md 'Rulings'"
  - "review/round4-adjudication.md 'Pre-registration scored'"
  - "review/round4-adjudication.md 'Revisions for v2 of the note'"
  - "review/round4/referee/audit-notes.md Step 1"
  - "review/v3-worklog.md preamble"
  - "review/wiki-build-flags.md items 9, 20, 26"
  - "notes/toy-lagrangian.md 'Chunk 1 results', 'Chunk 2 results', 'Write-up and review'"
  - "notes/knot-dark-matter-standalone.md 'References'"
  - "papers/reciprocity-toy-models.md 'References'"
  - "notes/broken-born-program-v1.md §8, §10, §11"
---

*The literature battery is the planned check of every reference that the program's papers cite from model memory, marked †, against the published source. A † citation was recalled by Claude rather than retrieved, so its authors, title, journal reference, or the statement it is cited for may be wrong. Checkpoint #11 lists the battery as open problem 10 of its §14 and calls itself "not for submission until the † audit (open item 10) completes". Some of the works involved have been checked in other contexts, and one suspected error in #11's list has been flagged, but no complete battery is on record. It is part of the first item of the current work queue.*

**Status:** Open — [O] (#11 §14 item 10) — no completed battery is recorded in the repository; it gates any submission (#11 footer) and sits in item 1 of the current queue (root `CLAUDE.md`). It qualifies the † mark defined on [Provenance tags and citation marks](/wiki/method/provenance-tags) and is listed in [Open problems and the queue](/wiki/status/open-problems).

## The open item

"Literature battery completion; every † reference source-checked [O]." (#11 §14 item 10). In #11's legend, [S] marks a reference "retrieved by live search during this project" and † one "cited from model memory — verify against the source before external use" (#11, 'References'). The battery turns each † into a checked reference, or finds what is wrong with it.

It matters for Tier 2 of #11's [claim tiers](/wiki/method/claim-tiers): literature results are "correct at the level of well-worn results; exact numbers, conventions, and attributions are flagged † pending source checks" (#11 §2). A memory citation can be right about the physics and wrong about where it was published, who proved it, or what exactly the paper says.

## Why it gates external use

#11's footer: "Working checkpoint — not for submission until the † audit (open item 10) completes." `HANDOFF.md` §7: "All †-flagged citations must be source-verified before anything goes external." The root `CLAUDE.md` gives † the same condition: "from model memory (verify against the source before any external use)".

## What is to be checked

- **#11.** Entries [1]–[18] and [23] carry †; [19]–[22] and [24]–[29] carry [S]. By subject, the † entries are: Born's two reciprocity papers ([1], [2]); Freidel–Leigh–Minic on Born reciprocity in string theory ([3]); curved momentum space, from Snyder to relative locality ([4]–[6]); the Born connection ([7]); spin-2 theory, from the multi-graviton no-go to Hinterbichler–Rosen ([8]–[12]); wave dark matter ([13]–[15]); Weyl semimetals ([16]); the Dirac–Schwinger–Zwanziger (DSZ) quantization and the electric–magnetic dualities ([17], [18]); and bigravity dark matter ([23]). The entries are collected on [References](/wiki/references); the document is [the checkpoint](/wiki/history/documents/checkpoint).
- **#13.** All four references of [conjugate special relativity](/wiki/conjugate-relativity) carry †: Gibbons and Schiller on maximum force, Caianiello on maximal acceleration, and Born's two papers, which are #11's [1] and [2] ([maximum-force conjectures](/wiki/conjugate-relativity/maximum-force-conjectures)).
- **An unreferenced phrase.** #11 §11.3 says that choosing a duality frame "is choosing a Lagrangian polarization of charge space, in the literature's own words", without naming the source of the words ([The symplectic charge lattice](/wiki/electric-magnetic-duality/symplectic-charge-lattice)).

## What a check involves

The blind referees of rounds 3 and 4 used a protocol that shows what a source check is. Its first step: "Verify every citation against INSPIRE, arXiv or the publisher, including that each one supports what it is cited for." (`review/round3-preregistration.md`, 'Protocol'). There are two parts. The reference must exist with the stated authors, title, journal, volume, page, year and preprint number; and the paper must say what the citing sentence uses it for. The round-3 referee did the second by searching the full text for each cited statement (`review/round3/referee/audit-notes.md`, Step 1).

## Citation errors found so far

The program's reviews and audits have found errors of each kind the battery targets. All but the last were in other manuscripts; no review has audited #11's list.

- **A citation inverted.** Round 1, on [the soliton manuscript #14](/wiki/dark-matter/candidates/soliton-candidate): "Preskill citation inverted (fixed)" (`HANDOFF.md` §6).
- **Cited for more than it says.** Round 3 found #14's reference [4] "over-generalized", Zwanziger's quantization stated with 4π where the manuscript wrote 2π, and Schwinger named but uncited (ruling 12). The referee also claimed that Baumgart et al. do not contain an operator #14 cited them for; the adjudicator overturned this from a footnote, quoted verbatim, that the referee had missed (ruling 8). A check has to read the paper, not only its abstract ([Round-3 verdict, rulings and citation audit](/wiki/method/review/round-3/rulings)).
- **Wrong details.** Round 4, on the [toy-model note](/wiki/symmetry-breaking/toy-models): "A. Duncan, not N."; a missing erratum; one reference's specific claim "cannot be checked (paywalled)" (`review/round4-adjudication.md`, 'Rulings', Citations; [Review round 4](/wiki/method/review/round-4)).
- **One entry pairing two papers.** #11's [23]† gives the title and journal of "Bigravitational origin of dark matter" (Phys. Rev. D 94, 084055, which is arXiv:1604.08564) with arXiv:1607.03497, the number of the companion paper "Heavy spin-2 Dark Matter". A verifier of the wiki build found this by live search; it is flag 20 in `review/wiki-build-flags.md`, a suspected error awaiting Paul's ruling, recorded "For the † battery (OP10)" ([bigravity dark matter](/wiki/dark-matter/candidates/bigravity-dark-matter)).

A related case concerned a convention rather than a citation. Working on the toy models, Claude found that its recalled Fourier eigenvalues contradicted Grosse–Wulkenhaar's stated invariance: "So a recalled convention is wrong somewhere." A direct numerical integral settled it, "not a recalled eigenvalue" (`notes/toy-lagrangian.md`, 'Chunk 1 results', 'Chunk 2 results').

`HANDOFF.md` §1 summarized the record at the handoff as "Zero fabricated citations across all checks", and the round-3 referee found all 23 of #14 v3's references, "37 individual items", resolving with matching metadata. The errors above are errors of detail and of support, not invented papers.

## Progress so far

The battery is open; what follows is partial progress, none of which closes it.

- **One † upgraded.** #11 v2.0 marked reference [21], the second data release of the [Dark Energy Spectroscopic Instrument](/wiki/cosmology/dark-energy/desi) (DESI), with †. v2.1 retrieved it and marked it [S], and added references [26]–[29], "all INSPIRE-checked" (repository history, commit e1c1f67, the v2.1 amendment).
- **Works checked through other manuscripts.** Several works that #11 cites with † were also cited by #14 v3 or by the toy-model note, and the referees of rounds 3 and 4 resolved them there: Born 1938 and 1949 (#11's [1], [2]; metadata confirmed, the primary text not read), Boulanger–Damour–Gualtieri–Henneaux ([8]), Hassan–Rosen ([10], [11]), Dirac 1931 and Zwanziger 1968 (two of the three works in [17]), Montonen–Olive (one of the two in [18]), and the two 2014 papers of Freidel, Leigh and Minic ([3]) (`review/round3/referee/audit-notes.md` and `review/round4/referee/audit-notes.md`, Step 1, matched against `notes/knot-dark-matter-standalone.md` and `papers/reciprocity-toy-models.md`, 'References'). Those checks confirmed the bibliographic data and, except for Born's papers, the support for what the other manuscripts cited each work for. Whether each supports what #11 cites it for remains part of the battery.
- **The wiki build.** The verifiers of this wiki checked pages against their sources, and at least one † reference was checked by live search, which produced flag 20. Two further flags concern [S] references, outside the battery: [24][S] has no authors and possibly a descriptive title (flag 9), and a live search found that the release #11 cites as [21][S] already covers three years of operations, which bears on the handoff's label "three-year data" for the next release (flag 26).

## Scope and place in the queue

`HANDOFF.md` §8 item 6 defined the task: "Literature battery completion: every † reference in #11 and #13 source-checked; resolve the gravity-induced kinetic mixing question." The second half was settled by round-3 Decision 1, "Kinetic mixing: strict sector separation", now part of postulate [P4](/wiki/program/postulates/p4-polarized-matter) ([Round-3 decisions and lessons](/wiki/method/review/round-3/decisions); [kinetic mixing](/wiki/dark-matter/candidates/soliton-candidate/kinetic-mixing)).

The root `CLAUDE.md` places the rest in the first item of the current queue: "1. HANDOFF §8 items 5–7: the partially-massless comparison, the † literature battery, the phase-space-diameter note." See [Open: the partially-massless comparison](/wiki/gravity/palindromic-branch/pm-comparison) and [the phase-space diameter relation](/wiki/cosmology/scale-factor-duality/phase-space-diameter). The references of the partially-massless comparison carry [S] and are outside the battery.

## History

- **v1.** The v1 paper's open problems ended with "Literature verifications: symmetric-bimetric Λ = 0; LPT coefficient calibration; Dalal–Kravtsov exact bound [O]" (#9 §10 item 8; LPT is Levkov–Panin–Tkachev), and its provenance note asked that "All citations flagged [T — verify] should be checked against sources before any submission" (#9 §11). The Λ = 0 comparison is now #11's open problem 2. The quintessence fits #9 tagged "[T — refresh citations before publication]" (§8) are [S] in #11.
- **v2.0.** #11 introduced the two marks: the handoff summarizes it as having "25 references flagged † (memory — verify) vs [S] (live-searched)" (`HANDOFF.md` §3).
- **Since the move.** New citations are retrieved, not recalled. The literature report for #14 v3 pulled each record "with no citations from memory" (`review/v3-worklog.md`). The toy-model work's prior-art searches retrieved every citation by live search, and round 4's revisions required that "Every new citation is to be retrieved, not recalled", which version 2 applied ("five new references, all retrieved", `notes/toy-lagrangian.md`). The pre-registered citation forecasts both scored hits: "All 23 citations resolve" in round 3 and "All 12 citations resolve" in round 4 ([pre-registration](/wiki/method/review/pre-registration)). Neither round covered #11 or #13 ([Review round 3](/wiki/method/review/round-3)).

## Sources

- `papers/broken-born-checkpoint-v2.md` §14 item 10, footer, 'References', §2, §11.3 — the open item, the submission gate, the † and [S] entries, Tier 2, the unreferenced phrase
- `papers/conjugate-special-relativity.md` 'References' — #13's † entries
- Root `CLAUDE.md` 'Since the handoff', 'Method' — the current queue; the meaning of †
- `HANDOFF.md` §7, §8 item 6 — the rule for external use; the battery's original scope; §1 — the record at the handoff; §3 — v2.0's marks; §6 — the inverted Preskill citation
- `review/round3-preregistration.md` 'Protocol' — what a citation check involves
- `review/round3-adjudication.md` 'Rulings' 8 and 12, 'Decisions', 'Pre-registration scored' — citation findings, Decision 1, the round-3 forecast
- `review/round4-adjudication.md` 'Rulings', 'Pre-registration scored', 'Revisions for v2 of the note' — citation findings, the round-4 forecast, "retrieved, not recalled"
- `review/round3/referee/audit-notes.md` and `review/round4/referee/audit-notes.md` Step 1 — the referees' citation audits
- `notes/knot-dark-matter-standalone.md` and `papers/reciprocity-toy-models.md` 'References' — the reference lists those audits covered
- Repository history, commit e1c1f67 — reference [21] upgraded to [S]
- `review/wiki-build-flags.md` items 9, 20, 26 — the wiki build's citation findings
- `review/v3-worklog.md` preamble and `notes/toy-lagrangian.md` — retrieval since the move; the recalled convention
- `notes/broken-born-program-v1.md` §8, §10 item 8, §11 — the v1 form of the item
