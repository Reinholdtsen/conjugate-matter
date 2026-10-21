---
title: "Documents"
weight: 30
status: hub
description: "The document map: artifacts #1–#15 and the later files, each with its status and where the wiki covers it, plus the precedence order that settles conflicts between them."
bookCollapseSection: true
---

*The program's record is a set of documents: a lab notebook and the calc notes that followed it, two paper-length checkpoints, two popular articles, a short paper on conjugate special relativity, a withdrawn manuscript with the console used to review it, a handoff note, and the files written since the move to this repository. `HANDOFF.md` numbers the artifacts carried over from claude.ai as #1–#15, and the wiki uses those numbers. Some documents are current references, some are kept only as an audit trail, and one was withdrawn; where two disagree, a fixed order of precedence decides which one the wiki follows.*

**Stands:** nothing in this section, which describes documents rather than claims ([claims that stand](/wiki/status/alive)) · **Died:** nothing in this section; the withdrawn manuscript #14 is described with [the retired soliton candidate](/wiki/dark-matter/candidates/soliton-candidate) · **Open:** nothing in this section ([open problems and the queue](/wiki/status/open-problems))

## Map

The pages start with the two files written to orient a new Claude Code session, follow the artifacts in their creation order (the lab notebook, the calc notes, the checkpoints), then take the popular articles, and end with the disagreements between all of them.

- [CLAUDE.md and the README](/wiki/history/documents/project-instructions) comes first because the root `CLAUDE.md` is the most current source: its section "Since the handoff" ranks first in the precedence order. The README is a one-line description from the first commit and is out of date.
- [The handoff document](/wiki/history/documents/handoff) is `HANDOFF.md`, written on 2026-10-19 to carry the project from claude.ai to Claude Code. It numbers the artifacts, keeps the results that exist only in the chat, and records the review history; its soliton candidate and work queue are superseded.
- [The lab notebook (#1) and its addenda](/wiki/history/documents/lab-notebook) is the first formalization, version 0.1 of September 2026, with addenda v0.2–v0.6 recording each settled debt and each correction. It is superseded as a reference and kept as the audit trail.
- [The Debt-3 calc notes (#2–#4)](/wiki/history/documents/debt-3-notes) are the three notes that tested momentum clumping and closed Debt 3 with a negative result. They are final for their scope.
- [The Debt-1 calc notes (#5–#8)](/wiki/history/documents/debt-1-notes) are the four notes that took Debt 1 from the compatibility theorem to the palindrome and found the gate's mechanism on the way. They are final for their scope.
- [The checkpoint: #9 to #11 v2.2](/wiki/history/documents/checkpoint) covers the paper-length consolidations: v1.0 (#9), now superseded, and #11, the current reference for the full program, through versions 2.0, 2.1 and 2.2.
- [The popular articles (#10, #12)](/wiki/history/documents/popular-articles) are a narrative of the first week and a tour of the framework written as if it were confirmed. Neither is ever a source for a claim's status.
- [Conflicts between sources](/wiki/history/documents/source-conflicts) closes the section: where the documents disagree, how the precedence order resolves each case, and which cases no document settles.

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

## The order of precedence

When documents disagree, the wiki follows the most current, in this order (`wiki/CLAUDE.md`):

1. the root `CLAUDE.md`, section "Since the handoff";
2. checkpoint #11 v2.2 and the toy-model note v2;
3. the review adjudications, `review/round4-adjudication.md` and `review/round3-adjudication.md`;
4. #13;
5. `HANDOFF.md`, whose §2 soliton candidate and §8 queue are superseded;
6. the notes: the calc notes #2–#8 are final for their own scope, #1 and #9 are superseded as reference, and #14 is withdrawn;
7. the popular articles. #12 presents the framework as if it were confirmed and is never a source for a claim's status.

Claims killed in `HANDOFF.md` §2, #11 §9 and §12, and the adjudications stay dead whatever a lower-ranked document says.

## Boundaries

- #13, #14 and the toy-model note are described on the index pages of their subjects: [Conjugate special relativity](/wiki/conjugate-relativity), [The soliton candidate (retired)](/wiki/dark-matter/candidates/soliton-candidate) and [Toy models of broken reciprocity](/wiki/symmetry-breaking/toy-models).
- The review records, including the skeptic console #15, are under [Blind review](/wiki/method/review), and the `verify/` scripts under [Verification](/wiki/method/verification).
- The dated sequence of the documents is the [Timeline](/wiki/history/timeline), elsewhere in [History](/wiki/history), and the current status of each claim they make is in [Status of the program's claims](/wiki/status).
