# The literature check of P.R.'s conjectures: record

*The record behind `notes/literature-check.md` and flags 64–69 in `review/wiki-build-flags.md`. It holds the
agents' brief, the pre-registration, every agent's findings, verdicts and query log, the citation screen, the merged
findings, the code checks, and the workflow scripts and tools. The gate runs `verify/literature_check.py`, which
checks the note against `findings.json`, `quotes.json`, `sources.json`, `recheck.json`, `screen/screen.json`, the
round-2 inputs, the workflow results and the pre-registration, and in its section G the algebra behind flag 66.
Nothing else here runs in the gate.*

Paul's request (2026-11-02): "Do a literature check of my conjectures". The seven conjectures, C1 to C7, are listed
with their sources in the note's §1. The check ran on 2026-11-02; the write-up followed on 2026-11-03.

## How it ran

1. **Round 1, search and verify** (`round1/`). Five searchers, one per theme, each followed by a verifier who
   reread every finding at its source and searched again: `g1-conjugate-matter` (C1), `g2-monopoles` (C2, C3),
   `g3-magnetic-mirror` (C4), `g4-collapse-acceleration` (C5), `g5-momentum-clumping` (C6, C7). Each has
   `<group>.search.json`, `<group>.verify.json` and its query logs.
2. **Round 2, the citation screen** (`screen/`, `round2/`). `tools/screen.py` collected every INSPIRE record citing
   one of ten anchors of the Born-reciprocity literature (`screen/screen.json`: 498 distinct records) and screened
   them by title, abstract and full text against each conjecture. Four readers read the 143 flagged records that no
   searcher had assessed (`round2/r*.input.json`, 171 reading assignments); verifiers checked the strong matches.
3. **Round 3, coverage** (`round3/`). Sweeps outside INSPIRE (OpenAlex, Crossref, DataCite, Zenodo, HAL, the web):
   `oa-c1-c6-c7`, `oa-c2-c3-c4`, `oa-c5`, and `lineages`, older lines of work. `known.json` lists the 195 papers
   already assessed, which the sweeps skipped. Verifiers checked the strong matches.
4. **Round 4, the verdict panel** (`panel/`). Seven judges, each given the evidence for its conjectures
   (`C*.evidence.json`): three for C1 (`c1-advocate`, asked to argue for novelty; `c1-scope`; `c1-content`), one
   each for C4, C5 and C6, and one for C2, C3 and C7. A reboot stopped the first launch before any judge returned;
   the workflow ran again from the start.
5. **Consolidation and code checks.** `tools/consolidate.py` merged the findings by paper and conjecture: a
   verifier's label replaces the finder's, the weaker label is kept where verifiers disagreed, a restatement is
   labeled no closer than its source (two findings for C5, lowered from partial to related), and the panel's label
   changes apply last: five of the six it proposed. The content judge's anticipates for 2202.06890 was not
   applied; the paper keeps its verifier's partial, which two other judges also gave it (`findings.json`, 287
   findings). `tools/recheck.py` looked up every identifier and compared the title, first author and year of each that resolved
   with the citation (eight of 287 did not resolve, none in a finding that carries a verdict). It found every
   quotation in a finding that carries a verdict again in the source's abstract or full text, except six from two
   sources it could not read (Henry-Couannier 2018 and Goldhaber 2017), which agents read through a web fetch. It
   flagged 23 of the 287 findings (`recheck.json`, `recheck.out`).

Scale of the check's four workflows, as the workflow tool reported it (`workflows/workflow1-result.json` to
`workflow4-result.json`): 31 agents, about 11.2 million tokens. The reviews of the write-up and round 5 (below) came
after; `workflow5-result.json` to `workflow9-result.json` record their workflows' agent and token counts. The
first review's two reviewers ran outside the workflow tool, and their counts are not in the record; the seven agents
of `workflow5-result.json` are its six verifiers and round 5's searcher.

## The pre-registration

`preregistration.md` was written by the main session before any search agent was launched, and kept outside every
folder an agent used until the check was done. It discloses the three papers seen while testing the tools, two by their abstracts and one by its title. Its
scoring, appended after the panel: four of seven verdicts right, all three misses underestimating the prior art;
the three misses are verdicts that rest on a reading of the conjecture, and under the other readings the judges state
each would have been a hit, and C5's hit a miss (note §2, §11); both overall predictions held. C3's hit, like its
verdict and the second overall prediction, is provisional until Khademi 2009's full text is read (note §4, §11).

## What came of it

- `notes/literature-check.md`: C1 anticipated (the identification, published by Minic and coauthors since 2020);
  C4, C5 and C6 partly anticipated; C2, C3 and C7 related only. No claim's status changed.
- Flags 64–69, pending: prior art #11 does not cite, the dictionary of §10 as scale-factor duality with sources (as
  a map of fluid variables), §11.3's bridge as a published remark, Brümmer et al. 2026 beside §12, and two fits
  bearing on row 1.
- `sources.json` and `quotes.json`, built for the write-up by `tools/make_sources.py` and `tools/make_quotes.py`:
  the metadata snapshot of every work the note cites (INSPIRE and arXiv metadata, CC0; Crossref bibliographic fields
  only; one OpenAlex record), and every quotation the note takes from the literature, with where code found it.
  Full texts are not stored; for a quotation from a full text, `quotes.json` keeps a short excerpt and a hash of the
  text as fetched. `verify/literature_check.py --online` fetches the sources again.
- A test of the gate script (2026-11-03): run against copies of the note with five planted errors (a changed
  quotation; a wrong coauthor, C.-H. Tze for T. Takeuchi in Jejjala et al. 2022, arXiv:2011.08852, the error the
  round-1 searcher for conjugate matter had made; a wrong verdict; a wrong count of findings; a wrong year), it
  failed on each.

## The reviews of the write-up, and round 5 (2026-11-03)

- **Two reviewers** read the first draft against this record: one the note, flags 64–69, the root `CLAUDE.md` entry
  and this README (findings F1–F20), one the wiki (W1–W20). **Six verifiers** each tried to refute a group of their
  findings, and one listed further stale statements in the wiki (X1–X10): none was refuted, and of the 56 verdicts
  (some findings were judged in parts) 41 were confirmed and 15 confirmed in part. Their verdicts, evidence and proposed edits are in `workflows/workflow5-result.json`, and the
  edits were applied to the note, the flags, `CLAUDE.md`, this README and the wiki; the workflow script is
  `workflows/litcheck-review-verify-wf_6aaa971f-b3e.js`.
- **Round 5** (`round5/`), run beside the verifiers, tried to rerun the queries that OpenAlex's quota had blocked in round 3.
  The quota had not renewed (it renews at 00:00 UTC); one query was refused, and the 26 OpenAlex queries, with four
  for Semantic Scholar, which also refused, are listed in `round5/not-run-queries.json`. Two arXiv queries ran and
  found nothing new. The round read the abstract of Khademi 2009, "Why magnetic monopoles are not seen?", from the
  Wayback Machine's capture of its repository page and from OpenAIRE's harvest (the item is CC0; the repository
  still refuses access, and the Wayback Machine never captured the PDF; CORE, BASE and Google Books refused
  automated requests, including one for a CORE download link of unknown content that a web search surfaced,
  core.ac.uk/download/287420038.pdf). Two judges, one asked to argue for the stronger label, each
  fetched the abstract again, found it by code, and labeled the item related to C3, with medium confidence
  (`workflows/workflow6-result.json`). It is not in `findings.json`, which holds rounds 1–4; its abstract is in
  `sources.json` and the quotation the note takes from it in `quotes.json`. A search during the round also surfaced
  arXiv:1709.10080, on a monopole background that coarse-grains momentum space, a possible collision for C2 and C3,
  not judged.
- **The second review** read the corrected write-up: one reviewer the note, flags 64–69, the root `CLAUDE.md`
  entries and this README (LC-01–LC-23), one the wiki (LC-1–LC-25), one what was missing or unverified
  (MU-01–MU-23). Each was followed by an agent that tried to refute its findings: none was refuted, 64 were
  confirmed and 7 confirmed in part (`workflows/workflow7-result.json`; script
  `workflows/litcheck-final-review-wf_bab37a40-2df.js`). The edits were applied, merged by hand where two touched the
  same passage. The largest: Berglund, Hübsch and Minic 2021 had been read as making the dark sector the
  electric–magnetic dual of the visible one (MU-01); C5's verdict also rests on a reading (MU-02); verified findings
  bearing on #11 had been left out of the note (MU-05 to MU-10, MU-12, MU-16, MU-18 and MU-19); and the algebra
  behind flag 66 was outside the gate (MU-14). `checks/` keeps the two agents' scripts for that algebra, and
  section G of `verify/literature_check.py` repeats the judge's checks. No verdict changed.
- **A check of the merges.** Four agents, each followed by a skeptic, checked the edits the main session wrote or
  merged by hand in applying the second review, the new section G and the note as a whole: 47 findings, none
  refuted, 43 confirmed and 4 confirmed in part (`workflows/workflow8-result.json`; script
  `workflows/litcheck-verify-merges-wf_5d58b04f-ddc.js`), applied, merged by hand where two touched the same passage.
- **A last sweep.** One agent, followed by a skeptic, checked the texts the main session wrote in applying the check
  of the merges and swept the repository for statements the edits had left stale: 14 findings, none refuted, 13
  confirmed and 1 confirmed in part (`workflows/workflow9-result.json`; script
  `workflows/litcheck-final-sweep-wf_2c828a96-7c1.js`), applied.

## Files

- `brief.md` — the brief every agent was given: the conjectures, the record's existing citations, the tools, the
  method and the labels.
- `preregistration.md` — the predicted verdicts, the weakest link, the scoring rule, and the scoring.
- `round1/`, `round2/`, `round3/`, `panel/` — each agent's output as returned, and its query log where it kept one.
- `screen/` — `screen.json` (anchors, citing records, flags), `screen.out`, `screen-fulltext.json` (full-text flags),
  `screen-gap.json` (flagged records no searcher had assessed).
- `findings.json` — the 287 merged findings, each with its labels, verdicts, quotations and the basis of its label.
  Its citations are the agents' strings, which `tools/recheck.py` checked only for title, first author and year; the
  round-1 verifier for C1 found two wrong coauthors there (2011.08852: T. Takeuchi, not C.-H. Tze; hep-th/0507199:
  T. Multamäki, not S. Watson). The note's references are built from `sources.json`.
- `recheck.json`, `recheck.out` — the code check of identifiers and quotations.
- `sources.json`, `quotes.json` — what the gate checks the note against.
- `round5/` — the attempted rerun of 2026-11-03: `round5.json` (queries and the Khademi finding), `notes.md`,
  `queries.tsv`, `not-run-queries.json`, `known-ids.json`, `out/` (raw outputs) and `scripts/`, the round's helpers
  and the runner for the queries still to run, `run_openalex.py`; their paths are relative to this record, so they
  use `tools/lit.py` and its cache here.
- `checks/` — the executed checks of the dictionary behind flag 66: the round-1 C5 verifier's `dg_exponents.py` and
  the C5 judge's `c5_dictionary_check.py`, with their outputs; section G of `verify/literature_check.py` repeats the
  judge's checks in the gate. Beside them, `planck_sigma.out` is the C5 judge's output, kept without its code, for
  how many standard deviations w = −2 and w = −1 lie from Planck 2018's w₀ (note §6, "Against the first version").
- `workflows/` — the workflow scripts of the check (four), of the first review's verification, of the Khademi
  judges, of the second review, of the check of the merges and of the last sweep, and the results the
  workflow tool returned (`workflow1-result.json` to `workflow9-result.json`, each with its workflow's
  agent and token counts).
- `tools/` — `lit.py` (INSPIRE, arXiv, Crossref and OpenAlex queries, full texts, quotation checks),
  `screen.py`, `consolidate.py`, `recheck.py`, `make_sources.py`, `make_quotes.py`, `assemble_record.py`. They ran
  from `work/literature-check/`, with a cache of fetched pages there that is not kept (copyrighted full texts); paths
  in them refer to that layout.
