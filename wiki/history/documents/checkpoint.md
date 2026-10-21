---
title: "The checkpoint: #9 to #11 v2.2"
weight: 60
status: record
description: "The first consolidation (v1.0, #9) and the current reference (#11) through v2.0, v2.1 and v2.2: what each version changed, and the section map between them."
sources:
  - "papers/broken-born-checkpoint-v2.md header"
  - "papers/broken-born-checkpoint-v2.md footer"
  - "papers/broken-born-checkpoint-v2.md §1"
  - "papers/broken-born-checkpoint-v2.md §10"
  - "notes/broken-born-program-v1.md"
  - "HANDOFF.md §3"
  - "CLAUDE.md 'Layout'"
  - "CLAUDE.md 'Since the handoff'"
---

*The checkpoint is the program's paper-length statement of everything it has derived, predicted, retracted and left open, with every claim tagged by where it came from. Its first version, #9 ("The Broken-Born Program" v1.0), consolidated the lab notebook and the calc notes into one document with a plain-language passage opening every section. Its successor, #11, is the current reference for the full program. Version 2.0 added a methodological preface with a machine-verification battery, sections on charge lattices and on the dark-sector candidates, and a reference list; version 2.1 recorded the outcome of review round 3; version 2.2 recorded the toy-model results. #11 is a working checkpoint, not to be submitted until its citations from memory have been checked against their sources.*

**Status:** Record — #11 v2.2 is rank 2 in the wiki's precedence order and "the current reference for the full program" (root `CLAUDE.md`); #9 is superseded by #11 and kept as the audit trail (`HANDOFF.md` §3: "v1.0 — superseded by #11"; #11 header: "Supersedes v2.1, v2.0 and v1.0").

## Key facts

- **#9, "The Broken-Born Program" v1.0.** "Version 1.0 — consolidation of the full development arc. Each section opens with a plain-language passage, then the technical record. Provenance tags: [D] derived here, [T] established literature, [P] postulate, [O] open." It is undated and sits between #8 and #10 in `HANDOFF.md` §3's creation order. Its section headings label the debts "(Debt 1: paid)", "(Debt 2: mechanism paid)" and "(Debt 3: closed, negative)" ([the three debts](/wiki/history/debts)).
- **#11 v2.0** (`HANDOFF.md` §3). "Supersedes #1 and #9. Adds: methodological preface + 7-test machine-verification battery; charge-lattice §11; dark-sector trilemma §12; 25 references flagged † (memory — verify) vs [S] (live-searched); PM/Hossenfelder novelty downgrade; Appendix A supposition audit (11 items with fates)" (PM: partially massless). See [the verification battery](/wiki/method/verification/battery), [the symplectic charge lattice](/wiki/electric-magnetic-duality/symplectic-charge-lattice), [Dark-sector candidates](/wiki/dark-matter/candidates), [the partially-massless comparison](/wiki/gravity/palindromic-branch/pm-comparison) and [Founding suppositions and their fates](/wiki/program/founding-suppositions).
- **v2.1** ("2026-10-19, after the round-3 review"; commit e1c1f67). "the soliton candidate is retired (§12); the compatibility theorem is re-attributed to the Born-geometry literature (§5); P4 is taken strictly (§4); §10 records DESI DR2's phantom crossing." The footer adds: "v2.1 amendments: decisions delegated by P. R. to Claude; record in `review/round3-adjudication.md`." See [the soliton obituary](/wiki/dark-matter/candidates/soliton-candidate/obituary), [the compatibility theorem](/wiki/phase-space/born-geometry/compatibility-theorem), [P4](/wiki/program/postulates/p4-polarized-matter) and [the phantom crossing](/wiki/cosmology/dark-energy/desi-dr2-phantom-crossing) in Data Release 2 of the Dark Energy Spectroscopic Instrument (DESI DR2).
- **v2.2** ("amended 2026-10-20"; commits 6ee74d0 and 6606734). "§3 credits Freidel–Leigh–Minic for "broken Born duality"; P2′ (§4), §10 and §14 item 11 record the toy-model results." See [broken Born duality](/wiki/phase-space/reciprocity/broken-born-duality), [the polarization as a Goldstone angle](/wiki/symmetry-breaking/goldstone-angle) and [acceptance criterion 1](/wiki/symmetry-breaking/toy-models/acceptance-criterion). The reference list now runs to [29] ([References](/wiki/references)).
- **Section map, #9 → #11.** §0 → §1, §1 → §3, §2 → §4, §3 → §5, §4 → §6, §5 → §7, §6 → §8, §7 → §9, §8 → §10, §9 → §13, §10 → §14, §11 → §15. #11's §2 (the methodological preface), §7.4 (the literature position), §11 (charge lattices), §12 (the dark-sector question) and Appendix A (the founding suppositions) have no counterpart in #9. The history of the predictions table across these versions is on [History of the predictions table](/wiki/predictions/table-history).
- **Not for submission yet.** The footer: "Working checkpoint — not for submission until the † audit (open item 10) completes" ([Open: the † literature battery](/wiki/method/literature-battery)). The provenance line reads "conjecture and direction, P. R.; derivations, counterexamples, verification battery, and drafting, Claude (Anthropic)"; #9's lacks "verification battery" ([The collaboration](/wiki/method/collaboration)).
- **What the wiki does not copy from #11.** §10's plain-language opener still says "DESI's hints of weakening dark energy are exactly the required drift", against the same section's "Under pressure (v2.1)" paragraph, which the wiki follows. Some plain passages use phrasing the house register excludes, such as "plays favorites" (§1) and "one state, two ledgers" (Appendix A); the wiki writes "two descriptions". And §10 writes τ's potential as V = V₀[1 + cos(τ/f)], which is non-negative for V₀ > 0, while the turnaround it predicts needs V < 0; no document settles this ([Open: the sign of V(τ) and the turnaround](/wiki/cosmology/dark-energy/potential-sign); [Conflicts between sources](/wiki/history/documents/source-conflicts)).

## Sources

- `papers/broken-born-checkpoint-v2.md` header — the version line and the v2.1 and v2.2 change lists; footer — the provenance line and the submission condition; §1 and §10 — the passages the wiki does not copy; References — the list through [29]
- `CLAUDE.md` 'Layout' — #11 as "the current reference for the full program" and #9 "superseded by #11"; 'Since the handoff' — the v2.1 changes
- `HANDOFF.md` §3 rows 9 and 11 — v1.0's standing and what v2.0 added
- `notes/broken-born-program-v1.md` — #9's header, section headings and provenance note
