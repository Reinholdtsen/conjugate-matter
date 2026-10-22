---
title: "Documents"
weight: 30
status: hub
description: "The document map: artifacts #1–#15 and the later files, each with its standing and where the wiki covers it, the precedence order that settles conflicts between them, and a page per document group."
bookCollapseSection: true
---

*The program's record is a set of documents: a lab notebook and the calc notes that followed it, two paper-length checkpoints, two popular articles, a short paper on [conjugate special relativity](/wiki/conjugate-relativity), a [withdrawn manuscript](/wiki/dark-matter/candidates/soliton-candidate/obituary) with the console used to review it, a handoff note, and the files written since the move to this repository. `HANDOFF.md` numbers the artifacts carried over from claude.ai as #1–#15, and the wiki uses those numbers. Some documents are current references, some are kept only as the audit trail, and one was withdrawn; where two disagree, a fixed order of precedence decides which one the wiki follows.*

**Record pages only:** this section describes documents and the disagreements between them, and makes no physics claims of its own. What stands, what died and what is open is registered in [claims that stand](/wiki/status/alive), [the graveyard](/wiki/status/graveyard), [open problems and the queue](/wiki/status/open-problems), [conjectures](/wiki/status/conjectures) and [superseded statements](/wiki/status/superseded). The withdrawn manuscript #14 is described with [the retired soliton candidate](/wiki/dark-matter/candidates/soliton-candidate).

## Map

The pages start with the two files written to orient a new Claude Code session, follow the artifacts in their creation order (the lab notebook, the calc notes, the checkpoints), then take the popular articles, and end with the disagreements between all of them. Each page says what its document is, its versions and dates, its standing in the precedence order, what it covers section by section with links to the pages that draw on each part, and what in it is superseded or flagged.

- [CLAUDE.md and the README](/wiki/history/documents/project-instructions) comes first because the root `CLAUDE.md` is the most current source: its section "Since the handoff" ranks first in the precedence order. The page follows the file's parts and their history from its creation at the move (commit 008c3ee) through each later decision, with the queue as it changed, the method's rules with the round that added each, and the points where the file and the repository disagree. The README is a one-line description from the first commit and is out of date in each of its claims.
- [The handoff document](/wiki/history/documents/handoff) is `HANDOFF.md`, written on 2026-10-19 to carry the project from claude.ai to Claude Code. The page goes through its sections and records what became of every alive, dead and open item of its §2 and every entry of its §8 queue; its soliton candidate and queue are superseded, while its list of dead claims stays binding.
- [The lab notebook (#1) and its addenda](/wiki/history/documents/lab-notebook) is the first formalization, version 0.1 of September 2026. The page takes v0.1 section by section, then the addenda v0.2–v0.6 that recorded each resolved debt and correction, and lists what the unedited body still states as live. It is superseded as a reference and kept as the audit trail.
- [The Debt-3 calc notes (#2–#4)](/wiki/history/documents/debt-3-notes) are the three notes that tested momentum clumping and closed Debt 3 with a negative result: the particle island, the [wave island](/wiki/dark-matter/momentum-clumping/wave-island) and the [ultra-faint-dwarf](/wiki/dark-matter/halo-astrophysics/dwarf-galaxies) endpoint, with their numbers, where the results went and where the notes differ. They are final for their scope.
- [The Debt-1 calc notes (#5–#8)](/wiki/history/documents/debt-1-notes) are the four notes that took Debt 1 from the [compatibility theorem](/wiki/phase-space/born-geometry/compatibility-theorem) to the [palindrome](/wiki/gravity/palindromic-branch/palindrome) and found the gate's mechanism on the way. The page maps the [battery](/wiki/method/verification/battery) tests T1–T7 onto the notes and records what has changed in them since. They are final for their scope.
- [The checkpoint: #9 to #11 v2.2](/wiki/history/documents/checkpoint) covers the paper-length consolidations: v1.0 (#9), now superseded, and #11, the current reference for the full program, through versions 2.0, 2.1 and 2.2 commit by commit, with #11 section by section, the inconsistencies inside it and the flags that concern it.
- [The popular articles (#10, #12)](/wiki/history/documents/popular-articles) are a narrative of the first week and a tour of the framework written as if it were confirmed. The page goes through both section by section, links the claims only they make, and sets #12's closing list against the record. Neither is ever a source for a claim's status.
- [Conflicts between sources](/wiki/history/documents/source-conflicts) closes the section: where the documents disagree, how the precedence order resolves each case, and which cases no document settles, stated as unresolved. Suspected errors inside single statements are kept apart, in `review/wiki-build-flags.md`.

## The artifacts and later files

| # | File | Standing | Where the wiki covers it |
| --- | --- | --- | --- |
| 1 | `notes/broken-born-theory.md` | v0.1 with addenda v0.2–v0.6; superseded as reference, kept as the audit trail | [The lab notebook](/wiki/history/documents/lab-notebook) |
| 2–4 | `notes/debt3a-stream-stability.md`, `notes/debt3b-wave-island.md`, `notes/debt3c-ufd-endpoint.md` | final; #4 "closes Debt 3 (negative)" | [The Debt-3 calc notes](/wiki/history/documents/debt-3-notes) |
| 5–8 | `notes/debt1a-geometric-core.md`, `notes/debt1a-ii-X-classification.md`, `notes/debt1a-iii-tuning-test.md`, `notes/debt1a-iv-beta-coefficients.md` | final; #8 "closes Debt 1 (structural)" | [The Debt-1 calc notes](/wiki/history/documents/debt-1-notes) |
| 9 | `notes/broken-born-program-v1.md` | v1.0, superseded by #11 | [The checkpoint](/wiki/history/documents/checkpoint) |
| 10 | `popsci/angle-of-the-mirror.md` | final (journey article); never a status source | [The popular articles](/wiki/history/documents/popular-articles) |
| 11 | `papers/broken-born-checkpoint-v2.md` | v2.2, the current reference for the full program | [The checkpoint](/wiki/history/documents/checkpoint) |
| 12 | `popsci/universes-other-half.md` | final (destination article); written as if confirmed; never a status source | [The popular articles](/wiki/history/documents/popular-articles) |
| 13 | `papers/conjugate-special-relativity.md` | a current reference (root `CLAUDE.md`); never blind-reviewed | [Conjugate special relativity](/wiki/conjugate-relativity) |
| 14 | `notes/knot-dark-matter-standalone.md` | v3, withdrawn 2026-10-19 after failing round-3 review; kept as the audit trail | [The soliton candidate (retired)](/wiki/dark-matter/candidates/soliton-candidate) |
| 15 | `review/skeptic-review-console.html` | the tool of review rounds 1–2; embeds #14 v2 | [The skeptic review console](/wiki/method/review/skeptic-console) |
| — | `HANDOFF.md` | 2026-10-19; superseded in part | [The handoff document](/wiki/history/documents/handoff) |
| — | `CLAUDE.md`, `README.md` | the standing instructions, top status source; a stale one-line description | [CLAUDE.md and the README](/wiki/history/documents/project-instructions) |
| — | `papers/reciprocity-toy-models.md`, `notes/toy-lagrangian.md` | the toy-model note v2, a current reference, and its worklog | [Toy models of broken reciprocity](/wiki/symmetry-breaking/toy-models) |
| — | `review/v3-worklog.md` | the closed worklog of #14 v3 | [The soliton candidate (retired)](/wiki/dark-matter/candidates/soliton-candidate) |
| — | `review/round3-preregistration.md`, `review/round3-adjudication.md`, `review/round3/` | the round-3 record | [Review round 3](/wiki/method/review/round-3) |
| — | `review/round4-preregistration.md`, `review/round4-adjudication.md`, `review/round4/` | the round-4 record | [Review round 4](/wiki/method/review/round-4) |
| — | `verify/battery.py` and the other `verify/` scripts, `scripts/check.sh` | the gate | [Verification](/wiki/method/verification) |
| — | `review/wiki-build-flags.md`, `review/wiki-build-checks/` | suspected errors in the sources found while the wiki was built, with executed checks; awaiting Paul's ruling | [Conflicts between sources](/wiki/history/documents/source-conflicts#what-this-page-does-not-list) |

## The order of precedence

When documents disagree, the wiki follows the most current, in this order (`wiki/CLAUDE.md`):

1. the root `CLAUDE.md`, section "Since the handoff";
2. checkpoint #11 v2.2 and the toy-model note v2;
3. the review adjudications, `review/round4-adjudication.md` and `review/round3-adjudication.md`;
4. #13;
5. `HANDOFF.md`, whose §2 soliton candidate and §8 queue are superseded;
6. the notes: the calc notes #2–#8 are final for their own scope, #1 and #9 are superseded as reference, and #14 is withdrawn;
7. the popular articles. #12 presents the framework as if it were confirmed and is never a source for a claim's status.

Claims killed in `HANDOFF.md` §2, #11 §9 and §12, and the adjudications stay dead whatever a lower-ranked document says. The cases the order settles, and those it does not, are on [Conflicts between sources](/wiki/history/documents/source-conflicts).

## Boundaries

- #13, #14 and the toy-model note are described on the index pages of their subjects: [Conjugate special relativity](/wiki/conjugate-relativity), [The soliton candidate (retired)](/wiki/dark-matter/candidates/soliton-candidate) and [Toy models of broken reciprocity](/wiki/symmetry-breaking/toy-models).
- The review records, including the skeptic console #15, are under [Blind review](/wiki/method/review), and the `verify/` scripts under [Verification](/wiki/method/verification).
- The dated sequence of the documents is the [Timeline](/wiki/history/timeline), elsewhere in [History](/wiki/history); the three debts that the notebook named and the calc notes took up are on [The three debts](/wiki/history/debts); and the current status of each claim the documents make is in [Status of the program's claims](/wiki/status).
