---
title: "CLAUDE.md and the README"
weight: 10
status: record
description: "The repository's standing instructions, whose 'Since the handoff' section is the top status source, and the README's stale one-line description."
sources:
  - "CLAUDE.md"
  - "README.md"
  - "wiki/CLAUDE.md 'The wiki is derivative'"
  - "scripts/check.sh"
  - "papers/broken-born-checkpoint-v2.md §14"
---

*The root `CLAUDE.md` is the repository's file of standing instructions for Claude Code sessions. It says what the program is, maps the documents to their folders, records what has changed since the handoff from claude.ai, defines the gate that must pass before work is called finished, and sets the method and the working arrangement with Paul. Its section "Since the handoff" is the most current statement of the program's status, and it ranks first when sources disagree. The README is the repository's one-line description from its first commit, and what it says about the project is out of date.*

**Status:** Record — untagged — `CLAUDE.md` "Since the handoff" is rank 1 in the wiki's precedence order (`wiki/CLAUDE.md`). The file was written at the move (commit 008c3ee) and revised with each decision since, most recently in 6606734; the README has not changed since the initial commit, 6b8f599.

## Key facts

- **What it says the program is.** "The Broken-Born program (BBT): a speculative physics research program built on spontaneously broken Born reciprocity. It was developed with Claude on claude.ai in September–October 2026 and continues here. Status: a Lakatosian research program, not a theory." See [The research program](/wiki/program) and [the hard core](/wiki/program/hard-core).
- **Layout and read order.** It maps the documents to `papers/` ("current references only"), `popsci/`, `notes/` ("the audit trail, superseded as reference but kept"), `review/` and `verify/` ([Documents](/wiki/history/documents)), and sets the read order "for a fresh session: #11 → HANDOFF §6 → `review/round3-adjudication.md` → calc notes only as a task needs them", which replaces the handoff's "#11 → #14 → §6 of this handoff → calc notes" ([The handoff document](/wiki/history/documents/handoff)).
- **"Since the handoff (2026-10-19)": the status changes.** #14 v3 failed round-3 review (verdict C) and was withdrawn, and "The superheavy soliton candidate in HANDOFF §2 is **dead** as a program-native proposal" ([obituary](/wiki/dark-matter/candidates/soliton-candidate/obituary)). "Strict sector separation (P4 at face value) is in force" ([P4](/wiki/program/postulates/p4-polarized-matter)). #11's v2.1 changes are listed, including that the Dark Energy Spectroscopic Instrument's Data Release 2 "favors a phantom crossing above z ≈ 0.4, against the framework's strict w ≥ −1 (§10). The dark-energy sector is under real pressure ahead of DR3" (Data Release 3; [DESI DR2's phantom crossing](/wiki/cosmology/dark-energy/desi-dr2-phantom-crossing)). The toy Lagrangian "is done to the referees' wording" ([acceptance criterion 1](/wiki/symmetry-breaking/toy-models/acceptance-criterion)), with open ends: "a Monte Carlo with H dynamical; a derivation of the ρ-preserving potential; the strong form of matter locality; the real Grosse–Wulkenhaar model's one-loop preference for the position-sharp vacuum, a lead."
- **"Since the handoff": the queue.** "HANDOFF §8 queue item 3 is dropped. The current queue, in order: 1. HANDOFF §8 items 5–7: the partially-massless comparison, the † literature battery, the phase-space-diameter note. 2. Optional: a round-5 review of the toy note, but only before any external use." See [the partially-massless comparison](/wiki/gravity/palindromic-branch/pm-comparison), [the † literature battery](/wiki/method/literature-battery), [the phase-space diameter relation](/wiki/cosmology/scale-factor-duality/phase-space-diameter) and [Open problems and the queue](/wiki/status/open-problems).
- **The gate and the method.** "scripts/check.sh is the definition of done. It runs every script in `verify/` and exits non-zero on any failure. It must pass before work is called finished. Do not weaken a check to make it pass." ([The gate](/wiki/method/verification/the-gate).) The section "Method (HANDOFF §5)" carries the [provenance tags](/wiki/method/provenance-tags) and [the iron rule](/wiki/method/verification/iron-rule), and adds the lessons of rounds 3 and 4: keep the prediction out of the [pre-registration](/wiki/method/review/pre-registration) commit subject, use [independent anchors](/wiki/method/verification/independent-anchors), check [the unreduced model's stability](/wiki/method/verification/reduced-model-stability), and give [Monte Carlo numbers error bars](/wiki/method/verification/monte-carlo-error-bars) from independent runs.
- **Working with Paul.** It fixes the roles and the attribution line ("conjecture and direction, P.R.; derivations, counterexamples, verification, drafting, Claude (Anthropic)"), states that "Paul is an independent developer (Stanford Ginzton Lab background in scanning acoustic microscopy, which is where the Fourier-domain intuition comes from)", and sets the prose register the wiki follows ([The collaboration](/wiki/method/collaboration)).
- **Where it disagrees with itself.** It says "#11 is now v2.1" and later refers to "#11 v2.2"; the file is v2.2. Its Layout names two `verify/` scripts, while `scripts/check.sh` runs `verify/battery.py`, `verify/soliton_obituary.py`, `verify/toy_coset.py`, `verify/toy_gw.py`, `verify/toy_s4.py` and `verify/toy_s5.py`, and then the wiki check. It says arbitration scripts go in `verify/`, but the round-3 and round-4 arbitration scripts sit in `review/` and the gate does not run them; no document settles this ([Conflicts between sources](/wiki/history/documents/source-conflicts)).
- **The README.** Its whole text is the heading "conjugate-matter" and the line "Physics hypothesis explaining dark matter and missing magnetic monopoles". The line is stale: the monopole explanation of the missing monopoles is [dead](/wiki/electric-magnetic-duality/monopole-explanation), the two remaining dark-matter candidates are not yet discriminated (#11 §14 item 9, [O]), and the root `CLAUDE.md` calls the program "not a theory".

## Sources

- `CLAUDE.md` — the program statement; 'Layout' with "Since the handoff (2026-10-19)"; 'The gate'; 'Method (HANDOFF §5)'; 'Working with Paul'
- `README.md` — the one-line description
- `wiki/CLAUDE.md` 'The wiki is derivative' — the precedence order that puts "Since the handoff" first
- `scripts/check.sh` — the `verify/` scripts and the wiki check that the gate runs
- `papers/broken-born-checkpoint-v2.md` §14 item 9 — the open discrimination between the two candidates
