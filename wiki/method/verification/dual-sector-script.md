---
title: "The dual-sector script"
weight: 150
status: method
description: "verify/dual_sector.py checks the note on the dual Standard Model of Minic and coauthors against its record: every quotation found again in a repository document or a stored source, every citation against a metadata snapshot, the dates of first publication, the counts and the judges' verdicts, the pre-registration's score, the quotations of the wiki page and of the flags the note proposes, and the doubled bracket behind one comparison; it checks that the note reports its record, not the agents' judgments."
provenance: [V]
sources:
  - "verify/dual_sector.py"
  - "notes/dual-sector.md §1"
  - "notes/dual-sector.md §13"
  - "review/dual-sector/README.md"
  - "review/wiki-build-flags.md items 64, 70, 71, 72, 73"
  - "scripts/check.sh"
---

*The dual-sector script, [`verify/dual_sector.py`](../../../verify/dual_sector.py), checks the note on [dark matter as the dual Standard Model](../../dark-matter/conjugate-matter/dual-standard-model.md), the proposal of Djordje Minic and coauthors, against the record the investigation left in [`review/dual-sector/`](../../../review/dual-sector/). The investigation's results are judgments by agents of how close a published paper comes to P.R.'s conjecture, and no script can recompute a judgment. What the script can do is confirm that the note reports the record faithfully: that each quotation is found again in its source, that each citation matches the bibliographic record of the paper it names and links to it, that the dates and counts it gives are those of the record, and that the wiki page and the flags quote nothing the record lacks.*

**Status:** Method, in force — twelfth in the list of scripts that [the gate](the-gate.md), [`scripts/check.sh`](../../../scripts/check.sh), runs. It runs offline against the stored record; `--online` also fetches the arXiv full texts again. The run recorded below printed 46 lines marked `PASS` and none marked `FAIL`.

## What it checks

- **A. Quotations.** Every passage of three or more words in double quotes in the note's body is found again, in a repository document other than the note and its record or among the quotations from the literature, [`review/dual-sector/quotes.json`](../../../review/dual-sector/quotes.json). A passage that one of the papers' verified statements holds is a quotation from the literature and must be in `quotes.json`, wherever else it is repeated. Each quotation there occurs in the note and in the excerpt stored when code found it in an abstract, an arXiv full text or a text extracted from a downloaded PDF. Four passages come from the handwritten slides of a talk, which code cannot read; they are counted, and the note must say they were read from the images.
- **B. Citations.** Every entry of the note's reference list with an identifier matches its metadata snapshot from INSPIRE, arXiv or Crossref: the authors' surnames, or the first author's and the count past four, the title and a year; and the entry links to that identifier.
- **C. Dates.** The first-public dates the note gives match the snapshots, and the date of the talk matches the record's evidence for it; the papers counted as prior art precede the program's [lab notebook](../../history/documents/lab-notebook.md) of September 2026, and the restatement of October 2026 follows it; the 173 days from the talk to the first written statement are recomputed.
- **D. Counts.** The statements, verdicts and added passages of the nine readers and their verifiers, the four judges' verdicts, the agents and tokens of each workflow, and the pre-registration's score and expected hits are recomputed from the record and found in the note as it states them. The counts of round 2's sweep of conference abstracts, and the number of Winn's quotations that round 2's refuter found again, are not recounted: each is found, as the note states it, in the report of the agent that made it.
- **E. Dependent texts.** Every quotation on the wiki page and in the flags the note proposes ([`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md), flag 64's addendum and flags 70–73) is found in the note, a repository document or `quotes.json`; for the flags, a repository document other than the flags file itself.
- **F. Algebra.** The commutators of the string's zero modes that the note relies on, [x, x̃] proportional to λ², [x, p] = [x̃, p̃] = iℏ and the others zero, form a non-degenerate bracket of four variables per dimension, against two for (x, p): a doubled phase space.

## What a pass means

A pass confirms that the note matches its record and that the record matches its stored sources. It does not confirm that a paper anticipates a conjecture: the verifiers and the panel judged that, and the script takes their verdicts as given. Full texts are not stored, being copyrighted, so offline the script compares a quotation from a full text with the short excerpt kept when code first found it; `--online` fetches the arXiv full texts again and finds each quotation in them.

## The recorded output

The run of 2026-11-06, after the review of the write-up, printed 46 lines marked `PASS` and 0 marked `FAIL` (a count of its output lines). Below, each section's `PASS` lines are replaced by their number; the other lines are as printed.

```text
A. Quotations
     (5 lines PASS)
      quotations by source: {'full text': 58, 'abstract': 8, 'image': 4, 'local text': 9}
B. Citations
     (1 line PASS)
C. Dates
     (10 lines PASS)
D. Counts
     (23 lines PASS)
E. Dependent texts
     (3 lines PASS)
F. Algebra
     (4 lines PASS)
dual_sector OK
```

## Used by

- [Dark matter as the dual Standard Model: the Minic precedent](../../dark-matter/conjugate-matter/dual-standard-model.md) — every quotation on the page.

## Sources

- [`verify/dual_sector.py`](../../../verify/dual_sector.py) — the checks and their docstring
- [`notes/dual-sector.md` §1](../../../notes/dual-sector.md#1-the-question-and-the-method) — the method; [§13](../../../notes/dual-sector.md#13-record) — the record and its scale
- [`review/dual-sector/README.md`](../../../review/dual-sector/README.md) — the record the script reads
- [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md) items 64 (addendum), 70–73 — the flags whose quotations it finds
- [`scripts/check.sh`](../../../scripts/check.sh) — the gate that runs it
