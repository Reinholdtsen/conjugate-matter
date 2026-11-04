---
title: "The literature check of P.R.'s conjectures"
weight: 90
status: record
description: "A search of the physics literature, made on 2026-11-02, for seven of P.R.'s conjectures: one is published in its core, three in part, and three were not found; how the search was made and checked, what it found, what it means for the checkpoint's citations, and its limits."
sources:
  - "notes/literature-check.md §1–§11"
  - "review/literature-check/README.md"
  - "review/wiki-build-flags.md items 64–69"
  - "verify/literature_check.py"
  - "CLAUDE.md 'Since the handoff'"
---

*The literature check is a search of the published physics literature, made on 2026-11-02, for seven of P.R.'s conjectures, to find which of them are already in print. Agents searched in three rounds, a second agent checked all but four of the findings that place a paper close to a conjecture or against it, a panel of judges reread those four with the rest of the evidence, and code found every quotation in the note again in its source. One conjecture, that dark matter is conjugate matter, is published in its core; three are published in part; three were not found. Prior art says who stated an idea first. It does not bear on whether the idea is right, and it changes no claim's status.*

**Status:** Record — a summary of `notes/literature-check.md`, searched and verified by independent agents, not through a blind review round. Its citations were retrieved by live search [S], and [the literature-check script](/wiki/method/verification/literature-check-script) checks its quotations, citations, verdicts and main counts against the stored record, and the algebra behind flag 66, on every run of the gate; it does not test the agents' judgments behind the verdicts.

## What was searched for

The seven conjectures, as the record states them:

| | Conjecture | Where the record states it |
| --- | --- | --- |
| C1 | [dark matter is conjugate matter](/wiki/program/founding-suppositions#4-dark-matter-is-conjugate-matter) | #11 App. A item 4 |
| C2 | [magnetic monopoles abundant in momentum space](/wiki/dark-matter/candidates/momentum-space-monopoles) | #11 §11.1, §12 |
| C3 | [that is why none has been found](/wiki/electric-magnetic-duality/monopole-explanation) | #11 App. A item 5 |
| C4 | [the momentum sector as the magnetic mirror](/wiki/electric-magnetic-duality/magnetic-identification) | #11 §11.4 |
| C5 | [conjugate collapse powers our expansion](/wiki/cosmology/scale-factor-duality/collapse-powered-expansion) | #11 §10, App. A item 9 |
| C6 | [velocity clumping, the founding image](/wiki/dark-matter/momentum-clumping/founding-image) | #11 §9, App. A item 3 |
| C7 | [a long-range velocity-gated attraction among χ](/wiki/dark-matter/momentum-clumping/long-range-gated-attraction) | `notes/velocity-gated-gravity.md` §5 |

## How it was done

- **Round 1.** Five searchers, one per theme, each followed by a verifier who reread every finding at its source and searched again.
- **Round 2.** A citation screen: every record in INSPIRE, the database of the high-energy physics literature, that cites one of ten works of the Born-reciprocity literature, 498 records. Four readers read the 143 flagged records that the first round had not assessed.
- **Round 3.** Sweeps outside INSPIRE, through OpenAlex, Crossref, DataCite, Zenodo, other open archives and the web, and through older lines of work.
- **Round 4.** A panel of seven judges reread the evidence for each verdict. One of the three judges for C1 was asked to argue for novelty.

Each finding relates one paper to one conjecture: *anticipates* (the paper states the conjecture in substance), *partial* (a close variant or a central part), *related* (the theme or mechanism), *evidence against*, or *collision* (the same words with another meaning). A conjecture's verdict is the strongest relation that survives verification, a rule written down before the search agents were launched, together with the expected verdicts ([pre-registration](/wiki/method/review/pre-registration)). Four of the seven expected verdicts held, C3's provisionally, and all three misses underestimated the prior art; each miss is a verdict that rests on a reading of the conjecture, and read the other way each would have held, while C5's hit, whose verdict also rests on a reading, would have become a miss. In its four workflows, 31 agents took part and produced 287 findings; in a fifth round, two further judges labeled the closest account of C3 found, Khademi 2009, from its abstract.

## What it found

| | Verdict | Closest published work | Not found |
| --- | --- | --- | --- |
| C1 | anticipated | Minic 2020; Berglund, Hübsch and Minić 2021; the same school to 2026 | the identification joined to a sector coupled to ours by gravity alone (mirror and twin matter couple by gravity, without reciprocity); the χ form with a velocity gate; the monopole form |
| C2 | related only | magnetic charge mapped to momentum space as a string background; Berry-curvature monopoles; monopole dark matter in position space | magnetically charged objects localized in momentum, as matter |
| C3 | related only | Khademi 2009, read in its abstract only (uncertainty in phase-space quantum mechanics; its full text could raise the verdict); other accounts of the null result: a second time dimension, neutral cores, superpositions of +g and −g, a dark sector, screening by a magnetic condensate | hiding by localization in momentum |
| C4 | partly anticipated | magnetic dark sectors: the magnetic half of one dual electrodynamics (Govaerts 2023); monopoles with a photon of their own (Vento 2025; García-Moreno and Vento 2026) | the analogs in the momentum polarization, one per charged particle |
| C5 | partly anticipated | a contracting partner universe that drives our acceleration (Henry-Couannier 2013, 2018); collapse in one frame as acceleration in another (Gasperini and Veneziano 1993; Mukherjee, Jassal and Lochan 2024) | the partner as the momentum description of our own universe |
| C6 | partly anticipated | Bose condensation of dark matter (Riotto and Tkachev 2000; Sikivie and Yang 2009; Levkov, Panin and Tkachev 2018) | velocity flocks formed by an attraction between similar velocities |
| C7 | related only | a Born-reciprocal partner of Newton's potential (Delbourgo and Lashmar 2008) | a long-range attraction among dark matter alone, gated in relative velocity |

**The first conjecture.** A group around Djordje Minic has proposed since 2020 that dark matter is the dual of the Standard Model in a Born-reciprocal formulation of string theory: in the words of Berglund, Hübsch and Minić 2021, dark matter "comes from the degrees of freedom dual to the visible matter" [S]. In the foundations of their work the dual coordinates are the momentum side of phase space; Freidel, Leigh and Minic 2014 (Phys. Lett. B) call them "coordinates in momentum space" [S]. In the model their dark-matter statements rest on, the dual coordinate belongs to a doubled phase space at the string scale, beside an ordinary momentum. Their dual sector is correlated with ours by construction. The program's [conjugate matter](/wiki/dark-matter/conjugate-matter) couples to ours by gravity alone under the strict reading of [postulate P4](/wiki/program/postulates/p4-polarized-matter), which the [shared-photon form](/wiki/electric-magnetic-duality/magnetic-identification#shared-photon) of the monopole candidate would need restated; its polarization is chosen by the vacuum ([P5](/wiki/program/postulates/p5-spontaneous-selection)); and neither of its two forms, [χ particles](/wiki/dark-matter/candidates/chi-particles) and [conjugate monopoles](/wiki/dark-matter/candidates/momentum-space-monopoles), was found in the literature.

Four verdicts rest on a reading of the conjecture that the judges state. C1's would be partly anticipated if strict P4 and ordinary momentum, rather than the dual coordinate at the string scale, belong to its substance, the reason one judge gave for medium confidence, or if its gloss, matter *organized around momentum*, is read as a clause about dynamics, dark matter that interacts or is localized in momentum, a dissent kept on record by the judge asked to argue for novelty. C4's would be related only if the placement in momentum alone is the conjecture. C5's counts the partner's identity, the momentum description of our own universe, as part of the conjecture; if that identity is counted as framework, Henry-Couannier's contracting partner could be called an anticipation of the conjecture's founding sentence, though never of the route that remains, a reading its judge does not adopt; the round-1 verifier for C5 finds an anticipation arguable only for the founding sentence read as a statement about how the two scale factors move, since in Dark Gravity the contraction of the conjugate side does not power our acceleration. C6's counts Bose condensation of dark matter as a form of the conjecture; restricted to the founding image of several velocity flocks, it would be related only.

The page of each conjecture linked above gives the details under "In the literature": a section, or for the first a paragraph of its audit entry.

## What it means for the checkpoint

No claim's status changes. The suggested changes concern what [checkpoint #11](/wiki/history/documents/checkpoint) cites, in six flags of `review/wiki-build-flags.md`, all pending:

- **Flag 64:** #11 cites none of the published work on C1's identification.
- **Flag 65:** the partial prior art for C4, C5 and C6 is uncited in #11 §11.4, §10 and App. A items 3 and 9.
- **Flag 66:** [the duality dictionary](/wiki/cosmology/scale-factor-duality/duality-dictionary#in-the-literature) is, as a map of fluid variables, the scale-factor duality of string cosmology with sources.
- **Flag 67:** the bridge between electric–magnetic duality and Born reciprocity behind [one enlarged modular structure](/wiki/electric-magnetic-duality/unified-modular-structure#in-the-literature) is a published remark.
- **Flag 68:** the exclusion of [the minimal hidden sector](/wiki/dark-matter/candidates/soliton-candidate/w-prime-overclosure#in-the-literature) was published first, independently, by Brümmer, Ferrante, Fischer and Frigerio (arXiv 2025, before #14 v3; Phys. Rev. D 2026).
- **Flag 69:** [row 1](/wiki/predictions/self-interaction-knee#the-data-situation)'s "zero cluster signal (particle χ)" meets two fits that mildly prefer a nonzero cross-section at cluster speeds.

The note also sets out published work that bears on #11 without changing a verdict: a third way to hide the magnetic analogs of the [shared-photon form](/wiki/electric-magnetic-duality/magnetic-identification#shared-photon), screening by a magnetic condensate; that where one kind of charge is the only one, which kind is called magnetic is a convention, which bears on the [separate-photon form](/wiki/electric-magnetic-duality/magnetic-identification#separate-photon); that the superseded rule of [the duality dictionary](/wiki/cosmology/scale-factor-duality/duality-dictionary#in-the-literature) is itself a published map, and that in a contracting universe anisotropy grows like a stiff fluid; a published measurement for the statement that the data exclude w = −2; a mechanism other than the gate for scattering that is strong in dwarfs and weak in clusters; published counterparts, without clumping, of [Fornax friction suppression](/wiki/dark-matter/momentum-clumping/fornax-friction) and [velocity-space granularity in halos](/wiki/dark-matter/momentum-clumping/velocity-granularity), two consequences the lab notebook drew from [clumping in momentum](/wiki/dark-matter/momentum-clumping/founding-image); and sources for two statements of #11 §11.3 that carry no citation (`notes/literature-check.md` §3–§7, §9).

For [the † literature battery](/wiki/method/literature-battery), the check found that the bibliographic data of #11's references [3]† (both papers), [13]† (its first paper) and [18]† (Montonen and Olive) match INSPIRE. Whether they support what #11 cites them for was not checked.

## Limits

A "not found" means not found by these searches.

- OpenAlex's free daily quota ran out during round 3, so the sweeps finished on the other indexes and the web, and the OpenAlex queries planned after that point did not run, among them four on explanations of the monopole null result. A rerun on 2026-11-03 found the quota not yet renewed, and Semantic Scholar refused too; the queries are listed in `review/literature-check/round5/not-run-queries.json`.
- The closest account of C3, Khademi 2009, "Why magnetic monopoles are not seen?", is read only in its abstract; its two pages, held in a repository that refuses access, could raise C3's verdict, which is provisional until they are read.
- Literature not in English was not searched.
- The large output of Carlos Castro Perelman on Born's reciprocal relativity was screened through INSPIRE and read only in part.
- The passages of two sources, Henry-Couannier 2018 and Goldhaber 2017, were read only through a web fetch, since the code checks cannot read them; the note paraphrases them.
- The labels are agents' judgments, tested by verifiers, a panel and code, not by a human expert.

## Sources

- `notes/literature-check.md` §1 — the conjectures, the request's date and the method; §2 — the verdicts and the findings behind them; §3–§8 — what is published and what is not, by conjecture; §9 — statuses and flags; §10 — limits; §11 — scale and the pre-registration's score
- `review/literature-check/README.md` — the rounds, the agents' outputs, the code checks and the files
- `review/wiki-build-flags.md` items 64–69 — the six flags, pending
- `verify/literature_check.py` — the machine check of the note against its record
- `CLAUDE.md` 'Since the handoff' — the check's date and results
