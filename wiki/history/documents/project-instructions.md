---
title: "CLAUDE.md and the README"
weight: 10
status: record
description: "The repository's standing instructions, whose 'Since the handoff' section is the top status source, with their history commit by commit, and the README's stale one-line description."
sources:
  - "CLAUDE.md 'Since the handoff'"
  - "CLAUDE.md 'Layout'"
  - "CLAUDE.md 'The gate'"
  - "CLAUDE.md 'Method (HANDOFF §5)'"
  - "CLAUDE.md 'Working with Paul'"
  - "README.md"
  - "wiki/CLAUDE.md 'The wiki is derivative'"
  - "scripts/check.sh"
  - "review/round3-adjudication.md 'Lessons (now in CLAUDE.md)'"
  - "review/round3-adjudication.md 'Decisions'"
  - "review/round4-adjudication.md 'Lessons (into CLAUDE.md)'"
  - "HANDOFF.md §5"
  - "HANDOFF.md §9"
  - "papers/broken-born-checkpoint-v2.md §14"
  - "review/wiki-build-flags.md items 37, 38, 40, 42"
---

*The root `CLAUDE.md` is the repository's file of standing instructions for Claude Code sessions. It says what the program is, maps the documents to their folders, records what has changed since the program moved from claude.ai, defines [the gate](/wiki/method/verification/the-gate) that must pass before work is called finished, and sets the method and the working arrangement with Paul. Its section "Since the handoff" is the most current statement of the program's status, and it ranks first when the documents disagree. The README is the repository's one-line description from its first commit, and what it says about the project is out of date.*

**Status:** Record — untagged (the file defines the provenance tags but applies none) — its section "Since the handoff" is rank 1 in the wiki's precedence order (`wiki/CLAUDE.md`). The file was created at the move in commit 008c3ee (2026-10-19) and revised after each decision since, most recently in 3243cdc (2026-10-21); the README has not changed since the initial commit, 6b8f599 (2026-10-18).

## What the file is

When the chat's files were restructured into this repository, the root `CLAUDE.md` was written beside them as the starting point for a fresh session. The commit that created it describes its job: "CLAUDE.md points fresh sessions at HANDOFF.md and carries the method and conventions" (008c3ee). [The handoff document](/wiki/history/documents/handoff) had asked for this arrangement in its suggested layout: "HANDOFF.md (this file; point CLAUDE.md at it)" (`HANDOFF.md` §9).

The file's parts, in order, are a statement of what the program is; the instruction to read `HANDOFF.md` first; the layout of the folders, with the read order and the section "Since the handoff"; the gate; the method; and the conventions for working with Paul. The method and the conventions were carried over from the handoff's §5 and §7. "Since the handoff" and the method's later bullets are what the repository added.

The file is a working document, not a paper, and it carries no provenance tags of its own. Its authority in the wiki comes from its currency: it has been revised after each decision since the move, so where it states a status, that status is the current one.

## The program statement and the first instruction

The file opens: "The Broken-Born program (BBT): a speculative physics research program built on spontaneously broken Born reciprocity. It was developed with Claude on claude.ai in September–October 2026 and continues here. Status: a Lakatosian research program, not a theory." BBT stands for Broken-Born theory, the name the lab notebook used. The program, its [hard core](/wiki/program/hard-core) and its claim to be a research program in Lakatos's sense are described under [the research program](/wiki/program) and [Lakatos's methodology of research programmes](/wiki/method/lakatosian-methodology).

The next paragraph says (the file's links are shown here as file names): "**Read `HANDOFF.md` first.** It is the project's state at the move from claude.ai: what is alive, dead and open (§2), results that exist only in the old chat (§4), review history and the referees' measured failure mode (§6), and the ranked next-actions queue (§8). Its §3 numbers the artifacts; the map below gives their paths." The paragraph has not changed since the file was created, although the handoff's §2 and §8 have since been superseded in part (below, and on [the handoff document](/wiki/history/documents/handoff)).

## Layout and read order

The layout section maps the documents to folders:

- **`papers/`**, "current references only": #11 `broken-born-checkpoint-v2.md`, "**the current reference for the full program.**"; #13 `conjugate-special-relativity.md`; and, since commit 6606734, `reciprocity-toy-models.md`, "the toy-Lagrangian note: two models of spontaneously broken ρ. Blind-review format. Round 4: B; v2 applies the revisions. The worklog is `notes/toy-lagrangian.md`." Version 2 itself says that the comparison with an exactly solved model, asked for in revision 4, was not carried out (flag 42 in `review/wiki-build-flags.md`; [review round 4](/wiki/method/review/round-4#the-revisions-and-version-2)). Until commit 5b6efaa the folder also held #14, "**the current blind-review manuscript** (v2; v3 pending, see HANDOFF §6)".
- **`popsci/`**: #10 and #12, [the popular articles](/wiki/history/documents/popular-articles).
- **`notes/`**, "the audit trail, superseded as reference but kept": #1, [the lab notebook](/wiki/history/documents/lab-notebook); #2–#8, [the Debt-3 calc notes](/wiki/history/documents/debt-3-notes) and [the Debt-1 calc notes](/wiki/history/documents/debt-1-notes); #9, "superseded by #11" ([the checkpoint](/wiki/history/documents/checkpoint)); and, since 5b6efaa, #14, "v3, **withdrawn** after failing round-3 review" ([the soliton candidate (retired)](/wiki/dark-matter/candidates/soliton-candidate)).
- **`review/`**: #15, [the skeptic review console](/wiki/method/review/skeptic-console); "referee reports and adjudications go here" ([blind review](/wiki/method/review)).
- **`verify/`**: "`battery.py` (HANDOFF Appendix A); `soliton_obituary.py` (the round-3 record); arbitration and audit scripts go here" ([verification](/wiki/method/verification)).
- **`wiki/`**, added in commit 3243cdc: "the program's wiki: one page per topic, explaining and indexing everything above, with each page's status and sources in its frontmatter. It is derivative: when it and a document disagree, the document wins. Its conventions are in `wiki/CLAUDE.md`."

The arrangement follows the handoff's suggested repository (`HANDOFF.md` §9), which assigned #1–#8 to `notes/` and did not place #9. The restructuring put the superseded v1 paper there too: "papers/ holds only current references (#11, #13, #14); the superseded v1 paper (#9) joins the lab notebook and calc notes in notes/" (commit 008c3ee). The full table of artifacts, with each one's standing, is on [Documents](/wiki/history/documents).

The read order "for a fresh session" is now "#11 → HANDOFF §6 → `review/round3-adjudication.md` → calc notes only as a task needs them", with the adjudication linked in the file. Until commit 5b6efaa it was "#11 → #14 → HANDOFF §6 → calc notes only as a task needs them", which followed the handoff's own "#11 → #14 → §6 of this handoff → calc notes (#2–#8) only as needed per task" (`HANDOFF.md` §3). The withdrawn #14 left the list and [the round-3 adjudication](/wiki/method/review/round-3) took its place. The file thus asks for the handoff to be read first, as orientation, and then gives an order for the documents that starts with #11.

## "Since the handoff": the status record

The section "Since the handoff (2026-10-19)" lists what changed after `HANDOFF.md` was written. It is the first source in the wiki's order of precedence (`wiki/CLAUDE.md`). Its bullets, in the file's order:

- **The soliton candidate.** "#14 went to v3, failed round-3 review (verdict C) and was withdrawn. The superheavy soliton candidate in HANDOFF §2 is **dead** as a program-native proposal. The framework is merely compatible with known PeV-scale topological dark matter (prior art)." See [Obituary: superheavy conjugate solitons](/wiki/dark-matter/candidates/soliton-candidate/obituary) and [topological dark matter in the literature](/wiki/dark-matter/candidates/soliton-candidate/prior-art).
- **Sector separation.** "Strict sector separation (P4 at face value) is in force." See [P4: polarized matter and strict sector separation](/wiki/program/postulates/p4-polarized-matter).
- **#11 v2.1.** "#11 is now v2.1: soliton obituary (§12); compatibility theorem re-tagged [T] (Freidel–Leigh–Minic); P4 strict (§4); DESI DR2 favors a phantom crossing above z ≈ 0.4, against the framework's strict w ≥ −1 (§10). The dark-energy sector is under real pressure ahead of DR3." DESI is the [Dark Energy Spectroscopic Instrument](/wiki/cosmology/dark-energy/desi), and DR2 and DR3 are its Data Release 2 and Data Release 3. See [the compatibility theorem](/wiki/phase-space/born-geometry/compatibility-theorem), [DESI DR2's phantom crossing](/wiki/cosmology/dark-energy/desi-dr2-phantom-crossing) and [row 4](/wiki/predictions/dark-energy-drift). The version the bullet names is out of date ([below](#where-the-file-and-the-repository-disagree); flag 38 in `review/wiki-build-flags.md`).
- **The toy Lagrangian.** "The toy Lagrangian (HANDOFF §8 item 4) is done to the referees' wording; see `papers/reciprocity-toy-models.md` and #11 v2.2 §14 item 11." Its open ends are listed as "a Monte Carlo with H dynamical", "a derivation of the ρ-preserving potential", "the strong form of matter locality" and "the real Grosse–Wulkenhaar model's one-loop preference for the position-sharp vacuum, a lead". See [acceptance criterion 1](/wiki/symmetry-breaking/toy-models/acceptance-criterion), [Open: a Monte Carlo with H dynamical](/wiki/symmetry-breaking/toy-models/coset-model/dynamical-h-monte-carlo), [Open: the origin of the ρ-preserving potential](/wiki/symmetry-breaking/rho-preserving-potential), [Open: forced locality and the P4 lock](/wiki/symmetry-breaking/strong-locality) and [Open: the real model's one-loop preference](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/real-model-lead). #11 §14 item 11 lists all but the last as open and does not mention the real-model lead.
- **The queue**, below.
- **The reasons.** "Reasons are in the adjudication's 'Decisions' section" ([round-3 decisions and lessons](/wiki/method/review/round-3/decisions)).

The section grew step by step. Commit 96f58da (2026-10-19), the round-3 adjudication, added a first paragraph: "#14 went to v3 and failed round-3 review (verdict C). HANDOFF §2's 'current best DM candidate' (superheavy solitons) is superseded by `review/round3-adjudication.md`. Read that before relying on §2 or on queue item 3 of §8", with the adjudication linked and DM being dark matter. Commit 5b6efaa, the round-3 decisions, replaced it with the dated list: the bullets on the soliton candidate and on sector separation, the queue and the reasons. Commit e1c1f67 added the bullet on #11 v2.1, and 6606734 (2026-10-20) the bullet on the toy Lagrangian.

## The queue and how it changed

The current queue reads: "HANDOFF §8 queue item 3 is dropped. The current queue, in order: 1. HANDOFF §8 items 5–7: the partially-massless comparison, the † literature battery, the phase-space-diameter note. 2. Optional: a round-5 review of the toy note, but only before any external use." The three items are [Open: the partially-massless comparison](/wiki/gravity/palindromic-branch/pm-comparison), [Open: the † literature battery](/wiki/method/literature-battery) and [the phase-space diameter relation](/wiki/cosmology/scale-factor-duality/phase-space-diameter), a chat-only conjecture. The round-5 review would follow [review round 4](/wiki/method/review/round-4). The register of open items is [Open problems and the queue](/wiki/status/open-problems).

| Commit | The queue as written |
| --- | --- |
| `HANDOFF.md` §8 (2026-10-19) | ranked items 1–7: cut #14 v3; re-run the blind audit; the √N-floor estimate; the toy Lagrangian; the partially-massless comparison; the literature battery; optional write-ups |
| 5b6efaa | item 3 dropped; "1. Amend #11 with the soliton obituary, the Freidel–Leigh–Minic prior-art check on the compatibility theorem, and the DESI DR2 phantom nuance. 2. The toy Lagrangian (HANDOFF §8 item 4). 3. HANDOFF §8 items 5–7, unchanged." |
| e1c1f67 | "1. The toy Lagrangian (HANDOFF §8 item 4). 2. HANDOFF §8 items 5–7, unchanged." |
| 6606734 | the current queue, above |

The √N floor of handoff item 3 was dropped by round-3 Decision 3 because "Its premise, Kibble as a ceiling, is inverted (ruling 3)" and it had no candidate left to serve ([Obituary: the √N topological floor](/wiki/dark-matter/candidates/soliton-candidate/sqrt-n-floor)). Handoff items 1 and 2 were done on 2026-10-19 ([review round 3](/wiki/method/review/round-3)).

## The gate

The section reads, with its link shown as a file name: "`scripts/check.sh` is the definition of done. It runs every script in `verify/`, then `scripts/check-wiki.py` on the wiki, and exits non-zero on any failure. It must pass before work is called finished. Do not weaken a check to make it pass. New verification scripts get wired into it." A first-time setup line follows: "python3 -m venv .venv && .venv/bin/pip install -r requirements.txt".

The wording "then `scripts/check-wiki.py` on the wiki" dates from commit 3243cdc (2026-10-21); the script itself had begun running the wiki check in commit 17e1338 (2026-10-20), and before that it ran the `verify/` scripts only. `scripts/check.sh` now runs `verify/battery.py`, `verify/soliton_obituary.py`, `verify/toy_coset.py`, `verify/toy_gw.py`, `verify/toy_s4.py` and `verify/toy_s5.py`, then the wiki check. See [the gate](/wiki/method/verification/the-gate), [the verification battery](/wiki/method/verification/battery), [the soliton-obituary script](/wiki/method/verification/soliton-obituary-script) and [the toy-model scripts](/wiki/method/verification/toy-model-scripts).

## The method

The section is headed "Method (HANDOFF §5)" and began as a condensed copy of the handoff's verification protocol ([Method](/wiki/method) in this wiki). Its bullets now read, with the commit that added each:

- **Tags and marks** (commit 008c3ee): "Tag every claim: **[D]** derived here, **[T]** literature, **[P]** postulate, **[O]** open, **[V]** machine-verified. Citations: **†** from model memory (verify against the source before any external use), **[S]** live-searched." See [provenance tags and citation marks](/wiki/method/provenance-tags).
- **The iron rule** (008c3ee): "no arithmetic by eyeball. Every asserted or disputed number gets executed code with printed output, kept in `verify/`." See [the iron rule](/wiki/method/verification/iron-rule).
- **Pre-registration** (008c3ee), with a lesson of round 3 added in 96f58da: "Keep the prediction out of the commit subject: subagents see recent commit subjects in their git-status context, and round 3's auditor saw it." See [pre-registration and its calibration record](/wiki/method/review/pre-registration).
- **Independent anchors** (96f58da): "A verification check confirms arithmetic, not the model. An anchor must be independent of the paper (a textbook identity, a published value). A check that reproduces the paper's own number is circular. Round 3 caught a wrong Kibble normalization that a circular anchor had passed." See [independent anchors](/wiki/method/verification/independent-anchors) and [verification checks arithmetic, not the model](/wiki/method/verification/arithmetic-not-model).
- **Reduced models** (e3ce9eb, round 4): "When numerics run on a reduced model (fields frozen), check the unreduced model's stability — boundedness, and the Hessian with all fields dynamical — and say in the text that it is a reduction. Round 4 found a potential that was bounded only at frozen H." See [the reduced-model stability rule](/wiki/method/verification/reduced-model-stability). The last sentence holds for the toy-model note's frozen-H reduction, in which the real structure K also stays on its circle, and not if only H is held fixed (flag 40 in `review/wiki-build-flags.md`, rated by its audit as depending on that reading; [the frozen-H reduction](/wiki/symmetry-breaking/toy-models/coset-model/frozen-h-reduction#the-rule-it-produced)).
- **Monte Carlo error bars** (e3ce9eb): "Monte Carlo numbers need error bars from independent runs. A fixed seed makes a number reproducible, not accurate." See [the Monte Carlo error-bar rule](/wiki/method/verification/monte-carlo-error-bars).
- **Negative results** (008c3ee): "Report negative results prominently. Claims listed as dead in HANDOFF §2 stay dead." See [negative results and dead claims](/wiki/method/negative-results) and [the graveyard](/wiki/status/graveyard).

The adjudications record the lessons at their source: round 3's "Lessons (now in CLAUDE.md)" and round 4's "Lessons (into CLAUDE.md)" (`review/round3-adjudication.md`; `review/round4-adjudication.md`).

## Working with Paul

The last section has not changed since the file was created. It fixes the roles, "Paul — conjecture, direction, veto. Claude — derivations, counterexamples, drafting, verification", and the attribution line for papers, "conjecture and direction, P.R.; derivations, counterexamples, verification, drafting, Claude (Anthropic)." It states that "Paul is an independent developer (Stanford Ginzton Lab background in scanning acoustic microscopy, which is where the Fourier-domain intuition comes from). Never describe Paul as retired." It records that Paul "cannot independently verify most of the technical physics and relies on the tags, the machine checks and pre-registration to tell sound results from confabulation", and asks that this calibration be kept explicit. The remaining bullets set the working pattern (chunks, saved state, "go"), the style of working communication ("simple bullets"), the register of science prose ("a serious scientist explaining abstract material in plain language. No anthropomorphizing, no moralizing, no detective-story reveals. Wave/Fourier analogies work; ball-rolling and ledger/bookkeeping metaphors don't") and the shape of papers ("every section opens with an italic plain-language passage, then the tagged technical record").

The wiki's voice rules are taken from this section. The roles, the calibration and the record of decisions taken and delegated are on [the collaboration](/wiki/method/collaboration).

## Where the file and the repository disagree

- **The version of #11.** The bullet on #11 in "Since the handoff" still says "#11 is now v2.1", while the bullet on the toy Lagrangian refers to "#11 v2.2 §14 item 11", and the checkpoint's header reads "Version 2.2 (checkpoint), amended 2026-10-20". Commit 6606734 made #11 v2.2 and added the toy-Lagrangian bullet without editing the other. The changes the bullet on #11 lists are the v2.1 changes and remain in v2.2; the version is 2.2 ([the checkpoint](/wiki/history/documents/checkpoint); flag 38 in `review/wiki-build-flags.md`).
- **The scripts in `verify/`.** The layout names `battery.py` and `soliton_obituary.py`. `scripts/check.sh` also runs the toy-model scripts `toy_coset.py`, `toy_gw.py`, `toy_s4.py` and `toy_s5.py`, which the layout does not list (flag 38).
- **Where arbitration scripts go.** The layout says "arbitration and audit scripts go here", in `verify/`, and the header of `scripts/check.sh` says "New arbitration and audit scripts in verify/ get added here". The arbitration scripts of rounds 3 and 4 sit in `review/round3/adjudicator/` and `review/round4/adjudicator/`, and the gate does not run them; the numbers they arbitrated are gated through `verify/soliton_obituary.py` and the toy-model scripts. No document says whether the instruction or the practice governs, and the wiki lists the point as unresolved ([conflicts between sources](/wiki/history/documents/source-conflicts#method-and-records); flag 38).

## The README

`README.md` is the repository's initial commit (6b8f599, 2026-10-18), and it has not been edited since. Its whole text is the heading "conjugate-matter" and one line:

> Physics hypothesis explaining dark matter and missing magnetic monopoles

Against the current record, the line is out of date in each part (its monopole clause is flag 37 in `review/wiki-build-flags.md`):

- **The missing monopoles.** The program's explanation of our failure to find magnetic monopoles is dead: the relevant duality is electric–magnetic, not position–momentum, and [inflation](/wiki/cosmology/early-universe/inflation-and-dilution) already accounts for the absence (#11 §11.1; `HANDOFF.md` §2; [Obituary: conjugate monopoles explain the null result](/wiki/electric-magnetic-duality/monopole-explanation)).
- **Dark matter.** The program offers two candidates, [χ particles](/wiki/dark-matter/candidates/chi-particles) and [an X-condensate](/wiki/dark-matter/candidates/x-condensate), and discriminating between them is open (#11 §12 and §14 item 9 [O]; [dark-sector candidates](/wiki/dark-matter/candidates)).
- **"Hypothesis".** The root `CLAUDE.md` calls the work "a Lakatosian research program, not a theory", and #11 §15 says the word "theory" "still waits on items 1–3" of its open problems ([assessment](/wiki/program/assessment)).

The wiki does not use the README as a source for anything but its own text.

## How the wiki uses the file

The wiki's conventions file, `wiki/CLAUDE.md`, places "the root `CLAUDE.md`, section 'Since the handoff'" first in its order of precedence, above checkpoint #11 v2.2 and the [toy-model note](/wiki/symmetry-breaking/toy-models), the adjudications, #13, the handoff, the notes and the popular articles ([Documents](/wiki/history/documents#the-order-of-precedence)). The other sections of the root file are instructions rather than statements about the physics, and the wiki follows them as working rules: its gate is part of `scripts/check.sh`, and its register follows "Working with Paul". The wiki mounts into a Hugo site configured to ignore files named `CLAUDE.md` (`ignoreFiles = ['CLAUDE\.md$']`, `wiki/CLAUDE.md`), so its conventions file never renders as a page.

## Sources

- `CLAUDE.md` — the opening statement; 'Layout' with the read order and "Since the handoff (2026-10-19)"; 'The gate'; 'Method (HANDOFF §5)'; 'Working with Paul'. Its history is in `git log -- CLAUDE.md`: 008c3ee, 96f58da, 5b6efaa, e1c1f67, e3ce9eb, 6606734, 3243cdc.
- `wiki/CLAUDE.md` 'The wiki is derivative' — the precedence order that puts "Since the handoff" first
- `scripts/check.sh` — the scripts the gate runs
- `review/round3-adjudication.md` 'Lessons (now in CLAUDE.md)' and 'Decisions' — the round-3 additions and the queue decisions; `review/round4-adjudication.md` 'Lessons (into CLAUDE.md)' — the round-4 additions
- `HANDOFF.md` §5 — the method the file condenses; §8 — the queue it replaced; §9 — the suggested layout
- `papers/broken-born-checkpoint-v2.md` header — the version the file's bullet lags; §11.1, §12, §14 and §15 — the points on which the README is out of date
- `README.md` — the one-line description
- `review/wiki-build-flags.md` items 37 and 38 — the README's monopole clause; the root `CLAUDE.md`'s stale version of #11, its two-script layout and where it says arbitration scripts go; item 40 — the method's "bounded only at frozen H"; item 42 — the layout's "v2 applies the revisions" beside the comparison v2 did not carry out
