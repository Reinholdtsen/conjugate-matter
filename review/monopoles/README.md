# The monopole sweep: record

*The record behind flags 59–61 in `review/wiki-build-flags.md` and #11 v2.3's §11.1, §11.4 and §14 item 12.
It holds the readers' outputs, the briefing as the synthesizer returned it with the verifier's corrections
appended, and the verifier's verdicts. The gate does not run any of it. The one executed check that came of
it, the polarization manifold's homotopy, is in `verify/closed_universe.py` section F.*

Paul's request (2026-10-28): "scan this repo for all information about monopoles so we can discuss in a rapid
back and forth about how this program thinks about them and comatter." The discussion that followed, on
2026-10-28 and 2026-10-29, turned on three questions:

- whether inflation is the only account of the monopole null result, and whether inflation happened ("The
  whole dilution discussion seemed off somehow");
- whether conjugate monopoles, compact in momentum space, would escape searches made in position space;
- Paul's conjecture: "momentum matter is similar to position matter with electrically charged position
  particles having magnetically charged momentum particle analogs".

## How it ran

1. **Seven readers** (`readers.json`), each over one partition of the repository: the current references and
   the handoff; the soliton candidate (#14) and its three review rounds; the lab notebook, the calc notes, the
   later notes and git history; the wiki-build flags, rulings and checks; and three slices of the wiki. Each
   returned tagged claims with path:line and a verbatim quote, 425 claims in all.
2. **A synthesizer** (`briefing.md`) combined them. It re-read every cited line of #11, the handoff and #14
   (v2 and v3), and re-ran `verify/soliton_obituary.py` (16 PASS).
3. **An adversarial verifier** (`verdicts.json`) checked 60 key claims at source: 53 confirmed, 7 misstated,
   none with a wrong citation. It checked the briefing's numbers against the scripts' printed output (two
   mismatches in the briefing's text, none in the record) and its tensions (24 of 27 hold), and swept the
   repository for monopole content the readers had missed. Its corrections are appended to `briefing.md`.

The sweep was not pre-registered: it collected the record and tested no prediction.

## What came of it

- **Flag 59**, accepted: #11 §11.1's second ground for the dead monopole explanation is restated. The null
  result is expected under several standard histories, so it lends the program no support; inflation is one
  of them, not an observed epoch.
- **Flag 60**, accepted: the wiki's obituary of the magnetic identification is reversed. Paul's
  magnetic-mirror conjecture is #11 §11.4 [O]. Paul withdrew the worklog's decision F2 of 2026-10-19
  (`review/v3-worklog.md`) as a confusion.
- **Flag 61**, applied under Paul's instruction to update the repo: the polarization manifold has
  π₂(Λ(4)) = ℤ₂, so selecting the polarization can leave point defects where the order parameter ranges over
  the whole manifold (for d = 4 and a global U(4)). Section F of `verify/closed_universe.py` gates the maps
  behind π₁ and π₃; π₂ follows by exactness. The defects' fate is #11 §14 item 12.
- **Flag 62**, pending: whether the conjecture's shared-photon form would reopen the dead explanation of the
  null result. The update's source reviewer raised it.

The update itself was reviewed by three adversarial agents (fidelity, consistency, sources). The source
reviewer found, among other things, that §11.2's strong coupling is not a history under which the null result
is expected, so it is not among flag 59's histories.

The briefing predates these rulings. Where it calls the magnetic identification dead, quotes #11 v2.2, or
counts §11.2's strong coupling as a second account of the monopoles' absence, the flags and #11 v2.3 supersede
it.

## Files

- `readers.json` — the seven readers' outputs as returned: files read, claims, numbers, history, tensions and
  open items for each partition.
- `briefing.md` — the synthesizer's briefing, then the verifier's overall finding, its corrections to the
  seven misstated key claims, the fourteen discussion hooks and the gaps. Text marked "Synthesizer's note" is
  the synthesizer's own observation, not record.
- `verdicts.json` — the 60 key claims and the verifier's verdict on each, with its number checks, tension
  checks and the files it found uncovered.
- `update-review.json` — the review of the update itself. Round 1: three adversarial reviewers (fidelity,
  consistency, sources) of the first edits, 75 findings. Round 2: the verifier after the fixes, which ran the
  gate and found 11 more, all applied. The source reviewer's findings are behind flag 62 and
  the removal of §11.2's strong coupling from flag 59's histories.
