---
title: "The literature-check script"
weight: 140
status: method
description: "verify/literature_check.py checks the note on the literature check of P.R.'s conjectures against the record the check left: verdicts recomputed from the merged findings, the counts, every quotation found again in a repository document or a stored source, every citation against a metadata snapshot, the pre-registration's score, and the quotations of flags 64–69, and in section G the algebra behind flag 66; it checks that the note reports its record, not the agents' judgments."
provenance: [V]
sources:
  - "verify/literature_check.py"
  - "notes/literature-check.md header"
  - "notes/literature-check.md §1"
  - "notes/literature-check.md §2"
  - "notes/literature-check.md §6"
  - "notes/literature-check.md §11"
  - "review/literature-check/README.md"
  - "review/literature-check/checks/c5_dictionary_check.py"
  - "review/wiki-build-flags.md items 64–69"
  - "scripts/check.sh"
---

*The literature-check script, `verify/literature_check.py`, checks [the note on the literature check](/wiki/method/literature-check) of P.R.'s conjectures against the record that the check left in `review/literature-check/`. The check's results are judgments by agents of how close a published paper comes to a conjecture, and no script can recompute a judgment. What the script can do is confirm that the note reports the record faithfully: that each verdict follows from the stored findings by the rule fixed in advance, that the counts it holds are right, that each quotation is found again in its source, and that each citation matches the bibliographic record of the paper it names. Its section G is a calculation instead: the algebra behind flag 66, which finds the program's [duality dictionary](/wiki/cosmology/scale-factor-duality/duality-dictionary) to be, as a map of fluid variables, the scale-factor duality of string cosmology with sources.*

**Status:** Method, in force — eleventh and last in the list of scripts that [the gate](/wiki/method/verification/the-gate), `scripts/check.sh`, runs. It runs offline against the stored record; `--online` also fetches every source again. The run recorded below printed 534 lines marked `PASS` and none marked `FAIL`, and ended "OK — the literature-check note matches its record: verdicts, counts, quotations and citations; the algebra behind flag 66 holds.".

## What it checks

- **A. Verdicts.** Each conjecture's verdict is recomputed from the 287 merged findings by the pre-registered rule, the strongest relation that survives verification, and compared with the note's table of verdicts and its table of findings by relation. Each verdict must rest on at least one finding that a second agent confirmed, and the findings that carry a verdict without a verifier's check must be the four the note names.
- **B. Counts.** The 498 records citing the citation screen's ten anchors, the 143 records read in round 2, the five labels the verdict panel changed, the code check's unresolved identifiers, flagged findings and quotations read only by web fetch, the agents and tokens the workflow tool reported, and the tallies of the two reviews of the write-up and of the check of the merges and the last sweep that followed them. Each count is recomputed from the record and must also appear in the note's prose as the note states it, in one phrase for each, so that a count changed in that phrase alone fails the check; where the note states the same count again elsewhere, as it does the 31 agents in §11, the script does not check the second statement.
- **C. Quotations.** Every passage of three or more words in double quotes in the note's body must be found again, either in a document of the repository or among the quotations taken from the literature. Each of those must appear in the note and in its source: the stored abstract (INSPIRE and arXiv release their metadata into the public domain) or, for a quotation from a full text, the excerpt stored when code found it.
- **D. Citations.** Every reference with an identifier must match its metadata snapshot from INSPIRE, arXiv, Crossref or OpenAlex: each author's surname and the number of authors, the title, the year, and the volume and page.
- **E. The pre-registration.** The verdicts predicted before the search agents were launched are scored against the recomputed ones: four of seven.
- **F. The flags.** Every quotation in flags 64–69 of `review/wiki-build-flags.md` must be found again in a repository document or among the note's quotations from the literature.
- **G. The algebra behind flag 66.** The checks that the panel judge for conjugate collapse ran on the [duality dictionary](/wiki/cosmology/scale-factor-duality/duality-dictionary), repeated in the gate ([below](#section-g-the-algebra-behind-flag-66)).

## Section G: the algebra behind flag 66

Flag 66 finds that #11 §10's corrected dictionary, w_eff = −w̃, is as a map of fluid variables the scale-factor duality of string cosmology with sources, where w̃ is the ratio of pressure to energy density, or [equation of state](/wiki/cosmology/dark-energy/quintessence#dark-energy-and-the-equation-of-state), of a fluid in the conjugate frame, and w_eff the equation of state with which that fluid acts on our expansion. Two agents of the literature check computed this in executed scripts, the round-1 verifier for conjugate collapse and the panel judge for it; both scripts are kept in `review/literature-check/checks/`. Section G repeats the judge's checks with the symbolic-algebra library sympy, each as a `PASS` or `FAIL` line:

- **The program's rule.** With the conjugate fluid's energy E = ρ̃ã³ entering our constraint as E/a³ and ã = 1/a, our own continuity equation gives the fluid's pressure, and w_eff = −w̃ follows; no reflection of the pressure is assumed (the lab notebook, #1 §6).
- **The published map.** Gasperini and Veneziano's duality with sources (2003, §2.2, eqs. 2.30–2.32: ρ̄ = ρa³ and p̄ = pa³ for three spatial dimensions, a → 1/a and p̄ → −p̄ at fixed ρ̄) keeps their continuity equation and gives the same density and pressure as the program's rule. The density agrees by construction, since both keep ρ̃ã³ = ρa³; the pressure agrees without a shared step: one computation never reflects a pressure, the other never uses our continuity equation.
- **The partner of a stiff source.** The duality turns a stiff source, p = ρ, into one with p = −ρ, and no de Sitter universe solves their field equations, eqs. 2.27–2.29, with such a source, whatever the sign of its energy density. Their string-frame power-law solutions, which match their closed form, eq. 2.37, satisfy the same equations, and the duality sends the one with a stiff source, a ∝ t^(1/2), to a ∝ t^(−1/2) with a running dilaton; for three spatial dimensions eq. 2.27 gives both a negative energy density.
- **Einstein gravity.** Without a dilaton the same map takes no flat Friedmann solution to another. Inverting the scale factor between single-fluid Friedmann solutions at a shared cosmic time gives w → −2 − w, the phantom duality and the program's superseded heuristic, and at a shared conformal time w → −2/3 − w.
- **Another pairing.** In the Brans–Dicke solution of Mukherjee, Jassal and Lochan (2024, §6), a theory in which a scalar field sets the strength of gravity, the contracting description's scale factor goes as a^(−1/2) of the expanding one's at the same event, not as 1/a, and its contents are stiff.
- **What acts as Λ.** Under the program's map the conjugate content that acts on ours as a cosmological constant is stiff, under the phantom duality it is a cosmological constant itself, and at a shared conformal time it is radiation.

The anchors are published equations, not the program's results, so the comparison is not circular. Like every check in the gate, section G confirms the arithmetic, not the model: it does not test the program's step of entering the conjugate energy in our Einstein-gravity constraint, which scale-factor duality, a symmetry of string-frame gravity with a dilaton, does not supply ([the duality dictionary](/wiki/cosmology/scale-factor-duality/duality-dictionary#in-the-literature)).

## What a pass means

A pass confirms that the note matches its record and that the record matches its stored sources, and, in section G, the algebra behind flag 66. It does not confirm that a paper anticipates a conjecture: the verifiers and the panel judged that, and the script takes their labels as given. Full texts are not stored, being copyrighted, so offline the script compares a quotation from a full text with the short excerpt kept when code first found it; the option `--online` fetches every abstract and full text again and finds each quotation in it. The passages of two sources, Henry-Couannier 2018 and Goldhaber 2017, were read only through a web fetch, since the code cannot read them, and the note paraphrases them instead of quoting.

The script was tested against copies of the note with five planted errors, a changed quotation, a wrong coauthor, a wrong verdict, a wrong count and a wrong year, and failed on each (`review/literature-check/README.md`). The wrong coauthor is the error one agent made during the check.

## The recorded output

The run of 2026-11-03, after the write-up, printed 534 lines marked `PASS` and none marked `FAIL` (a count of its output lines). Below, each section's `PASS` lines are replaced by their number; the other lines are as printed.

```text
A. Verdicts recomputed from findings.json
     C1: anticipated          53 findings; anticipates 9, partial 4, related 31, evidence-against 2, collision 7
     C2: related only         34 findings; related 23, evidence-against 3, collision 8
     C3: related only         30 findings; related 26, evidence-against 1, collision 3
     C4: partly anticipated   59 findings; partial 3, related 48, evidence-against 1, collision 7
     C5: partly anticipated   75 findings; partial 6, related 61, evidence-against 1, collision 7
     C6: partly anticipated   25 findings; partial 4, related 18, evidence-against 1, collision 2
     C7: related only         11 findings; related 9, evidence-against 1, collision 1
[22 lines marked PASS]
B. Counts
     workflow 1: 10 agents, 4,617,454 tokens
     workflow 2: 7 agents, 1,822,684 tokens
     workflow 3: 7 agents, 2,616,235 tokens
     workflow 4: 7 agents, 2,107,543 tokens
[32 lines marked PASS]
C. Quotations
     76 quoted passages: 60 from the literature, 16 from repository documents
[113 lines marked PASS]
D. Citations against their metadata snapshots
     86 references checked against INSPIRE, arXiv, Crossref or OpenAlex snapshots
[328 lines marked PASS]
E. The pre-registration, scored
     C1: predicted 'partly anticipated', found 'anticipated': miss
     C2: predicted 'related only', found 'related only': hit
     C3: predicted 'related only or nothing', found 'related only': hit
     C4: predicted 'related only', found 'partly anticipated': miss
     C5: predicted 'partly anticipated', found 'partly anticipated': hit
     C6: predicted 'related only', found 'partly anticipated': miss
     C7: predicted 'related only', found 'related only': hit
[1 line marked PASS]
F. Quotations in flags 64–69 (review/wiki-build-flags.md)
     22 quoted passages
[22 lines marked PASS]
G. The algebra behind flag 66: the duality dictionary as scale-factor duality with sources
[16 lines marked PASS]

OK — the literature-check note matches its record: verdicts, counts, quotations and citations; the algebra behind flag 66 holds.
```

## Sources

- `verify/literature_check.py` — the script and its docstring
- `notes/literature-check.md` header — the note's statement of what the script checks; §1 — the method and the verdict rule; §2 — the tables the script recomputes; §11 — the scale and the pre-registration's score
- `review/literature-check/README.md` — the stored record, how `sources.json` and `quotes.json` were built, and the test with planted errors
- `review/wiki-build-flags.md` items 64–69 — the flags whose quotations the script checks
- `notes/literature-check.md` §6 — the dictionary as scale-factor duality with sources, which section G checks
- `review/literature-check/checks/` — the two agents' scripts; section G repeats the judge's
- `scripts/check.sh` — the gate that runs it
