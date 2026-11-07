# The dual-sector investigation: record

*The record behind `notes/dual-sector.md`, the addendum to flag 64 and flags 70–73 in `review/wiki-build-flags.md`,
and the wiki page `wiki/dark-matter/conjugate-matter/dual-standard-model.md`. It holds the agents' brief, the
program's statements as the agents were given them, the pre-registration, every reader's and verifier's output, the
evidence as the panel read it, the judges' and the critic's outputs, round 2, the metadata snapshots and quotations
the gate checks, the workflow scripts and the tools. The gate runs `verify/dual_sector.py`, which checks the note
against `quotes.json`, `sources.json`, `events.json`, `readers/`, `panel/`, `round2/`, `workflows/usage.json` and the
pre-registration. Nothing else here runs in the gate.*

Paul's request (2026-11-06), of the executive summary's sentence on C1, "Its core is published (Minic and coauthors,
2020), their sector correlated with ours; neither form was found.": "Please investigate the highlighted claim more
thoroughly. Create a page for it at the minimum, especially if the claim is true that there is overlap between our
conjectures and theirs. Also, whenever referenced include a link to the paper itself if possible."

## How it ran

1. **Workflow A, read and verify** (`readers/`; script `workflows/dual-sector-read-verify-wf_c9a159be-379.js`). Nine
   readers, each followed at once by a verifier who tried to refute it from the sources: r1 priority, r2 the dual
   Standard Model, r3 the restatements of 2022–2026, r4 phenomenology and dark energy, r5 Modified Dark Matter, r6 the
   foundations, r7 the choice of polarization, r8 outside the group, r9 a mechanical sweep of 41 full texts. Each has
   `rN-….json` (the reader) and `rN-…-verify.json` (the verifier). The agents read with a copy of
   `review/literature-check/tools/lit.py` (here `tools/lit.py`) from `work/dual-sector/`, whose cache of fetched pages
   (copyrighted full texts) and the agents' downloads are not kept.
2. **Workflow B, the panel** (`panel/`; script `workflows/dual-sector-panel-wf_37362a3d-f8b.js`). The evidence was
   assembled by code (`tools/split.py`, `tools/assemble.py`, `tools/by_question.py`) into `panel/by-question.md`
   (every answer of the readers with its verifier's verdict, and every point where the record was found contradicted
   or qualified), `panel/papers.md`, `panel/missed.md` and `panel/statements.json`. Four judges read it: `j-identity`
   (asked to argue that the group's proposal is C1), `j-difference` (asked to argue that it is not), `j-content` and
   `j-overlap`; a completeness critic (`critic.json`), working beside them, looked for what was missing and closed what
   it could. The judges did not see the critic's output.
3. **Round 2** (`round2/`; script `workflows/dual-sector-round2-wf_0eee439e-102.js`): an independent verifier of the
   critic's find outside the group (Winn), and a sweep of conference abstracts, each followed by a refuter.
4. **The paper links** (`links/`). Every paper identifier in the wiki was turned into a link to the paper by code
   (`links/retrofit.py`, after `links/survey.py` and `links/context_check.py`), and one agent linked author–year
   citations of verified papers at their first mention on each page (`links/author_year.py`, `links/decisions.tsv`,
   `links/author-year-links.tsv`, `links/author-year-skipped.tsv`, `links/verify_wrap.py`). The registry of linked
   papers is `scripts/wiki-papers.tsv`, built by `scripts/wiki-papers.py`; the gate's `paper` check in
   `scripts/check-wiki.py` keeps it.
5. **The propagation** (workflow D; script `workflows/dual-sector-propagate-wf_2cdea7d1-67a.js`): eight agents
   carried the findings into `notes/literature-check.md` and the wiki pages that held the claim.

Scale, as the tools reported it (`workflows/usage.json`): workflow A, 18 agents; workflow B, 5; round 2, 4; the
propagation, 8; the linking, 1; their tokens as listed there.

## The pre-registration

`preregistration.md` was written by the main session before any agent was launched, and kept outside the repository
and every folder an agent used until the agents were done. It discloses what the main session had seen while
scouting. Its score, appended after the panel: ten of fourteen predictions held, against 10.25 expected from the
stated probabilities; three of the four misses underestimated how close the group comes to the program. Round 2,
which finished after the scoring, changed no hit or miss.

## What came of it

- `notes/dual-sector.md`: P1 (core published) and P2 (correlated) hold with qualification, P3 (neither form) holds,
  P4 (overlap beyond C1) holds. No claim's status changed.
- Round 2: Winn's magnetically charged partner for every charged particle, outside the group, verified and labeled
  partial for the magnetic mirror's shared-photon form (flag 73); the conference sweep found the identification, in
  its phase-space sense, only in the group's talks, and neither form.
- The addendum to flag 64 and flags 70–73, pending.
- `sources.json` (built by `tools/make_sources.py`, adapted from the literature check's) and `quotes.json` (built by
  `tools/make_quotes.py`): the metadata snapshot of every work the note cites and every quotation it takes from the
  literature, with where code found it. Two snapshots are edited by hand, each marked `edited`. Full texts are not
  stored; for a quotation from a full text, `quotes.json` keeps an excerpt and a hash of the text as fetched.
  `events.json` holds the date of the Belgrade talk with the evidence for it.

## Files

- `brief.md` — the brief every agent was given; `program.md` — #11's statements, extracted verbatim by code;
  `propagation/facts.md` — the facts, wording and links the agents of the two propagation rounds were given.
- `preregistration.md` — the predictions, the weakest link, the scoring rule and the score.
- `readers/` — the nine readers' and nine verifiers' outputs as returned.
- `panel/` — the evidence as the panel read it, the four judges' outputs and the critic's.
- `round2/` — round 2's outputs.
- `propagation/results.json`, `finish/results.json` — workflows D and E: the editors' and checkers' reports of the two
  propagation rounds, and the three reviewers' findings with their refuters'.
- `workflows/` — the workflow scripts and `usage.json`.
- `sources.json`, `quotes.json`, `events.json` — what the gate checks the note against.
- `tools/` — `lit.py`, `make_sources.py`, `make_quotes.py`, `refs.py` (the note's reference list), `split.py`,
  `assemble.py`, `by_question.py`, `q.py`. They ran from `work/dual-sector/`; paths in them refer to that layout.
- `links/` — the scripts and tables of the paper-link retrofit.
