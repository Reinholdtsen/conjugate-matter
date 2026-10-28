# The closed-universe investigation: record

*The record behind `notes/closed-universe.md`. It holds the analyses, the verifiers' verdicts, the critic's
rulings and scripts, the pre-registration and the answer as first given to Paul. The gate does not run any of
it. The numbers the note uses are recomputed in `verify/closed_universe.py`.*

Paul's question (2026-10-27): "Presumably a comatter universe is closed. Work out the cosmological consequences
wrt generalized general relativity. How small does momentum space get? How big does position space get?
Anything else of interest."

## How it ran

1. **Pre-registration** (`preregistration.md`). Written before any agent was dispatched and kept outside every
   agent's folder. SHA-256 `5b1fb2334c316d2780fd47f8aca49a26663b9214f5d2ac86b31ecb9a0fd3f564`, unchanged
   since it was sealed.
2. **Five analyses** (`analyses/*.json`): observations, dynamics, gravity sector, minisuperspace and momentum
   space. Each analyst ran its own scripts and returned tagged, numbered claims.
3. **Ten verifiers** (`verdicts/<analysis>-<lens>.json`), two per analysis. Each lens worked from the extracted
   claims only, not from the other agents' conclusions:
   - derivation and numbers for the four theory analyses;
   - sources and applicability for the observations.

   Tally: 469 claim checks, 403 confirmed, 48 corrected, 2 refuted (dynamics C23, momentum space C37),
   16 not reached (arXiv rate limits).
4. **A completeness critic** (`verdicts/critic.json`, scripts in `critic/`). It ruled on seven tensions between
   the analyses and listed the gaps.
5. **The answer** (`answer.md`): the answer as given to Paul, with the pre-registration scored.

`grid.csv` holds the 96 closed τ histories of the dynamics analysis. `critic/d_light_travel.py` and
`critic/g_answer_numbers.py` read it from the session folder they ran in.

## Not kept

The downloaded sources (arXiv TeX, page images): about 360 MB, and copyrighted.
