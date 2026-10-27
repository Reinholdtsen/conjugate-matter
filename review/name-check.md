# Name check: "comatter"

A check, run on 2026-10-26 before the program was renamed, that the new name is
not already in use in physics or elsewhere. Run by Claude at Paul's request; the
counts below are the printed outputs of the queries, not recalled.

## Queries and counts

Each search was run beside a control query for a term known to be in the
database, so that a zero means "not found" and not "the query is broken".

| Database | Query | Hits | Control | Control hits |
| --- | --- | --- | --- | --- |
| INSPIRE | title `comatter` | 0 | title `technicolor` | 694 |
| INSPIRE | `abstracts.value:comatter` | 0 | `abstracts.value:quintessence` | 3904 |
| INSPIRE | free text `comatter` | 0 | free text `quintessence` | 4968 |
| INSPIRE | fulltext `comatter` | 0 | fulltext `quintessence` | 17097 |
| INSPIRE | keywords `comatter` | 0 | — | — |
| INSPIRE | title, abstracts `"co-matter"` | 0 | — | — |
| INSPIRE | fulltext `"co-matter"` | 17 | — | — |
| arXiv API | `all:comatter`, `ti:comatter`, `abs:comatter` | 0 each | `abs:quintessence` | 2821 |
| arXiv API | `all:"co-matter"` | 0 | — | — |

A first INSPIRE query of the form `abstracts comatter` returned 0, and so did its
control, `abstracts quintessence`; that form is broken and its zero is not
evidence. The `abstracts.value:` form above replaces it. A first arXiv run with
`max_results=0` returned HTTP 500 for every query, the control included; the
counts above are from a rerun with `max_results=3`.

The 17 full-text hits for "co-matter" are astrophysics papers: 16 on white
dwarfs, novae, supernovae and accretion onto compact objects (for example
arXiv:1901.10007), and one on dark-matter
accretion and galaxy growth (arXiv:2005.08995). Their text was not inspected. In
the first group "CO matter" is presumably carbon–oxygen matter, which a full-text
index does not distinguish from "co-matter"; this reading is inferred from the
papers' subjects. Either way none uses the word as a name, and the one-word
spelling "comatter" has no hits.

Two general web searches, for `"comatter"` and for `"co-matter"` with physics,
company or software, found no exact use. The nearest results were a company
named COMAT and Matter, a smart-home connectivity standard; neither is the same
word.

## Limits

- arXiv's API searches titles, abstracts and metadata, not full text.
- INSPIRE's full text covers only the papers it has indexed.
- The web check was two searches on one engine.

A use inside the body of an unindexed paper would not have been found.

## Result

No prior use of "comatter" was found in INSPIRE, arXiv or on the web. The program
was renamed the Comatter program the same day (root `CLAUDE.md`, "Since the
handoff").

## Sources

- INSPIRE literature API, https://inspirehep.net/api/literature
- arXiv API, https://export.arxiv.org/api/query
