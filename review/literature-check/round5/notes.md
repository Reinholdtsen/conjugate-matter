# Round 5 of the literature check: the queries round 3 could not run (2026-11-03)

Task (workflow, 2026-11-03): run every query recorded as not run in round 1 and round 3 with the check's own tool,
screen the hits against `review/literature-check/findings.json` and `round3/known.json`, read and label anything
new, and try once more to read Khademi 2009 (C3). Nothing outside this folder was edited. The one side effect
outside it: `lit.py` writes its cache under `work/literature-check/cache/` (new arXiv API entries; lock-file
timestamps). The gate does not read that cache (`verify/literature_check.py` points `lit.CACHE` at a temp dir).

Files: `not-run-queries.json` (the collected list, with sources), `queries.tsv` (every request sent today),
`out/` (raw outputs), `khademi/` (downloads, untrusted, not kept in the record; `../sources.json` has the abstract),
`scripts/` (`q.sh` logs lit.py runs; `s2.sh`; `known.py` builds `known-ids.json` and screens; `qlocal.py` checks a
quotation in a local copy with lit.py's `norm()`; `html2text.py`; `run_openalex.py`, see below), `round5.json`
(the structured result).

## 1. What was collected

26 OpenAlex queries (Q01–Q26), 4 Semantic Scholar queries (S1–S4) and 2 arXiv API queries (A1, A2); five more
entries were checked and need no rerun (`not-run-queries.json`, `not_rerun`). Sources:

- `round3/oa-c1-c6-c7`: Q01–Q03 (C6), S1–S2 (C1); the curl probe of the budget is not a search.
- `round3/oa-c2-c3-c4`: Q04–Q07 (oa07-1..4, C3; full strings from `queries.log`, since the JSON abbreviates them),
  Q08–Q13 (the six re-run queries named in the JSON notes; C2, C3, C4), S3 (C2). The Crossref posted-content
  queries cp01–cp03 (ERROR 400) were rerun at once in round 3.
- `round3/oa-c5`: Q14–Q15 (bh_parent, negmass_contr), S4, and five topics recorded without query strings
  (Janus/Sakharov, isodual, Reciprocal System, time-reversed universe, extra-dimension contraction): Q16–Q20 are
  my formulations, marked `formulated`.
- `round3/lineages`: Q21 (Assis Weber), Q22 ("Born reciprocity", --size 100 recorded), and the phrase sweeps named
  in its unverified leads: Q23–Q25 (formulated from the phrase list).
- `round3/oa-c1-c6-c7` notes: "The C7 OpenAlex set (Weber, relational mechanics, velocity-dependent gravity)
  therefore ran on DataCite": Weber and relational mechanics did run on OpenAlex in the lineage sweep; Q26 covers
  velocity-dependent gravity (formulated).
- Round 1: A1 (g5, C7) never ran; A2 (g2) was a title lookup resolved through INSPIRE and Crossref; g1's
  `abs:"dark matter" AND abs:"momentum-space" AND abs:"localized"` and g4's `abs:reciprocity AND abs:"scale factor"`
  are recorded as errors but ran later in round 1 (10 and 16 hits).

## 2. What ran

- **OpenAlex: not reset.** The quota had not reset when this round ran. A free single-work lookup at 20:49 UTC
  returned `x-ratelimit-remaining-usd: 0` of `0.1`, `x-ratelimit-reset: 11441` s, i.e. the free daily budget for
  this IP renews at 2026-11-04 00:00 UTC (16:00 PST on 2026-11-03). Round 3 exhausted it at about 01:04 UTC on
  2026-11-03, the same UTC day. Q01 was sent once through lit.py at 20:52 UTC: "OpenAlex error 429" (lit.py's own
  six attempts over 61 s). Per the task, the OpenAlex part stopped there: Q02–Q26 were not sent.
- **Semantic Scholar:** S1 answered HTTP 429 (no Retry-After). Same rule: S2–S4 not sent.
- **arXiv API (lit.py arxiv):** A1, 0 hits. Control `abs:Weber AND abs:gravitational`: 59 hits, 50 screened by
  title: Weber-bar gravitational-wave papers and other uses of the name; the only two on Weber-type forces are
  Bunchaft–Carneiro 1997 (cited by the record) and Devasia 2008 (read and set aside in round 3; C7 panel evidence).
  So A1's zero is not a parsing failure. A2: 1 hit, Brouder et al. 2007, already in the record.

## 3. Khademi 2009 (C3): abstract read, full text still unread

- Handle server API: `20.500.12415/6128` → `https://openaccess.maltepe.edu.tr/handle/20.500.12415/6128`.
- Repository: landing page, OAI-PMH GetRecord, DSpace REST and the PDF bitstream all answer a plain nginx 403.
- **Wayback Machine:** the repository's own item page was captured on 2021-05-10 (DSpace 6.2, HTTP 200). It gives
  the metadata and the abstract: conference object, "Why magnetic monopoles are not seen?", Khademi, Siamak; source
  "International Conference of Mathematical Sciences"; publisher Maltepe Üniversitesi; 2009; pp. 365–366; ISBN
  9786052124154; CC0 1.0; full text `371.pdf` (97.93 KB). The PDF was never captured (CDX: no bitstream URL under
  either path).
- **OpenAIRE** (api.openaire.eu, no key): the same record, harvested from the repository (collected 2026-08-19),
  same abstract, now under handle 20.500.12415/2255 (the repository renumbered its items; in 2021 handle 2255 was an
  unrelated article), instance "nonPeerReviewed", licence CC0, its only web resource the handle.
- OpenAlex W3153563614 (fresh): one location (the repository landing page), no PDF, no abstract, "closed".
- CORE: API 429, web page a bot check. BASE: JavaScript proof-of-work page. Google Books API (ISBN): 429 daily quota.
  Semantic Scholar title match: 429. Not worked around.
- WebSearch (one extended, one standard) and Maltepe's ICMS proceedings page: no copy of the item and no 2009
  volume (the page lists AIP proceedings from 2018 on).

Abstract, checked with `scripts/qlocal.py` (lit.py's `norm()`) in both copies (FOUND in each; the negative control
"monopoles live in momentum space" NOT FOUND in either):

> Dual symmetry of Maxwell’s equations predicts the existence of magnetic monopoles which are not detected until
> now. As an important consequence of this prediction, the quantization of electric charge is obtained by P.A.M.
> Dirac. In this paper I show the uncertainty in the phase space quantum mechanics could be the responsible of the
> non-visibility of magnetic monopoles.

Reading against C3: it explains the null result by "the uncertainty in the phase space quantum mechanics", the
position–momentum uncertainty that C3's own page invokes (an object compact in momentum is spread in position by
about ħ/Δp). It does not say where the monopoles live: no momentum space, conjugate sector, polarization, dark
matter or abundance. Label: **related**, conservatively; the two-page text could make it partial if it places the
monopoles in momentum, and that text is still unread. Inference, not read: its "phase space quantum mechanics" is
probably the Kirkwood phase-space picture of Khademi and Nasiri 2008 (J. Phys. Conf. Ser. 128, 012016; C4 related in
`findings.json`), which gets charge quantization without monopoles.

Venue: a conference contribution of two pages in the ICMS 2009 book (Maltepe Üniversitesi); OpenAIRE's record marks
it "nonPeerReviewed". Authorship: the repository lists Khademi alone; round 3's Zanjan faculty listing gives "S.
Khademi, S. Nasiri" for a talk of the same title at the Multiphysics conference, Lille, December 2009: probably a
second presentation, not checked.

## 4. To finish after the reset (2026-11-04 00:00 UTC = 16:00 PST)

`python3 review/literature-check/round5/scripts/run_openalex.py` checks the budget with a free lookup and sends
nothing if it is zero; otherwise it sends each of Q01–Q26 once through lit.py (`--size 200`, Q21 `--size 25`),
stops at the first 429, and writes `out/<ID>.txt` and `out/<ID>.screen.tsv` (KNOWN/new against
`known-ids.json`). `--dry-run` prints the commands. S2–S4 need a Semantic Scholar pool that answers; nothing here
retries them.
