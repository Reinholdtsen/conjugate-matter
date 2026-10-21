---
title: "The gate: scripts/check.sh"
weight: 60
status: method
description: "The definition of done: the verify/ scripts and the wiki check, each check printing PASS or FAIL with its measured value where it has one; what is gated, what is not, and the last recorded run."
sources:
  - "scripts/check.sh"
  - "scripts/check-wiki.py"
  - "CLAUDE.md 'The gate'"
  - "CLAUDE.md 'Layout'"
  - "requirements.txt"
  - "verify/battery.py"
  - "verify/soliton_obituary.py"
  - "papers/broken-born-checkpoint-v2.md §12"
  - "papers/reciprocity-toy-models.md §2–§5"
  - "review/round3-adjudication.md 'Rulings'"
  - "review/round3-adjudication.md 'Decisions'"
  - "review/round4-adjudication.md header"
  - "HANDOFF.md §2"
---

*The gate is the shell script `scripts/check.sh`, which runs every verification script in the repository's `verify/` folder and then the wiki's own consistency check, and exits with a failure if any check fails. The project calls it "the definition of done": work is not finished until it passes, and a check may not be weakened to make it pass. Each script prints one line per check, a pass or a fail together with the measured value where there is one, so the record of a run shows what was tested as well as the verdict. What the gate tests is the arithmetic of the models the scripts encode; which claims of the papers it covers, and which it does not, is listed below.*

**Status:** Method, in force — untagged — root `CLAUDE.md` ('The gate'); the scripts' results carry [V] where the papers cite them. The last recorded run of the verification scripts passed every check and ended "OK — all checks pass."; it was made before the wiki check was added, so it records nothing about the wiki.

## Key facts

- **The definition.** "scripts/check.sh is the definition of done. It runs every script in `verify/` and exits non-zero on any failure. It must pass before work is called finished. Do not weaken a check to make it pass. New verification scripts get wired into it." (root `CLAUDE.md`, 'The gate'). The script's header: "The definition of done for this repo. Exits non-zero if any verification script fails." When the withdrawn manuscript's checks were replaced by `verify/soliton_obituary.py`, the round-3 adjudication recorded why replacing a script is not weakening a check: "This retires the checks of a withdrawn paper. It does not loosen the gate: the gate verifies what current documents claim, and v3 no longer claims anything." (`review/round3-adjudication.md`, 'Decisions').
- **What it runs.** An explicit list, not a pattern: `verify/battery.py`, `verify/soliton_obituary.py`, `verify/toy_coset.py`, `verify/toy_gw.py`, `verify/toy_s4.py` and `verify/toy_s5.py`, then `scripts/check-wiki.py`. It sets `set -uo pipefail` without `-e` and records failures in a status variable, so every script runs even after an earlier one fails. The statement that the gate "runs every script in `verify/`" therefore holds while the list matches the folder, as it does now. Root `CLAUDE.md`'s 'Layout' names only `battery.py` and `soliton_obituary.py`; the script list is the fact. The pages: [the battery](/wiki/method/verification/battery), [the soliton-obituary script](/wiki/method/verification/soliton-obituary-script), [the toy-model scripts](/wiki/method/verification/toy-model-scripts). The scripts run in a Python virtual environment built from `requirements.txt` (numpy==2.5.4, sympy==1.14.0); without it the gate prints `check FAILED: no .venv.` and exits with a failure.
- **The check line.** Each script defines `check(name, ok, detail="")`, prints `PASS` or `FAIL`, the check's name and, where one is given, the measured value in brackets, and exits 1 if any check failed. `verify/battery.py`: "Every verdict is a boolean or a number against a tolerance, never a judgement." Checks labelled "parity" or "quoted:" compare the output with the figures the documents print; they confirm that the documents print what the code computes ([Independent anchors](/wiki/method/verification/independent-anchors)).
- **The wiki check.** `scripts/check-wiki.py` checks links, anchors, section maps, source paths, frontmatter, weights, sections, the italic opening, the status line, body headings, code fences and acronyms. Its docstring: "Hugo does not validate internal links: it renders /wiki/does-not-exist without complaint. This script is the only thing standing between a renamed page and a silent 404."
- **What is gated.** `verify/battery.py` covers the Tier-1 algebra of #11 (§2, §5, §6, §7.2, §7.3). `verify/soliton_obituary.py` covers round-3 rulings 1, 2, 4 and 5 and the W′ overclosure, which #11 §12 cites: "The [V] numbers here are gated in `verify/soliton_obituary.py`." `verify/toy_coset.py` covers the toy-model note's §2 and the model I potential of §4; `verify/toy_gw.py` its §3 and the tadpole of §4; `verify/toy_s4.py` its §4 Monte Carlo table; `verify/toy_s5.py` its §5. #11 cites the toy results as [D][V] (§4, §10) and records them in §14 item 11.
- **What is not gated.** Round-3 rulings 3 and 6–13 (the adjudicator "did not re-run the referee's Kibble–Zurek integration", and rulings 6 and 9 were "Accepted, not re-checked"); the toy-model note's analytic argument that the complex model's breaking does not survive quantization (the gate checks its premise, the exact continuous symmetry, not its conclusion); the Debt-3 figure "criterion fails by 10²⁸–10³¹", which `HANDOFF.md` §2 marks ✓ although no script in `verify/` computes it ([The mean-field criterion and its 10²⁸–10³¹ shortfall](/wiki/dark-matter/momentum-clumping/instability-criterion)); and, more generally, the numbers of the Debt-3 calc notes and of #13, for which `verify/` holds no script ([The Debt-3 calc notes](/wiki/history/documents/debt-3-notes); [Conjugate special relativity](/wiki/conjugate-relativity)).
- **Review scripts stay outside.** The referees' and adjudicators' scripts sit in `review/` and are not run: `review/round3/adjudicator/round3_arb.py`, `review/round4/adjudicator/arb.py` and `review/round4/adjudicator/ctrl.py`. Root `CLAUDE.md` says "arbitration and audit scripts go here", meaning `verify/`; the sources do not settle the difference, so it stands as a gap. The gate carries their corrected results instead: the soliton numbers in `verify/soliton_obituary.py`, and checks labelled as round-4 findings (F3, F4, F6) in the toy scripts. See [Blind review](/wiki/method/review).
- **A name shared.** "The gate" in the physics pages is a different thing: [the velocity gate](/wiki/dark-matter/conjugate-matter/velocity-gate) that switches conjugate matter's self-interaction off at high relative velocity.

## Sources

- `scripts/check.sh` — the script list, the failure handling, the final line
- `scripts/check-wiki.py` — the wiki checks and their purpose
- Root `CLAUDE.md` 'The gate', 'Layout' — the definition of done; the scripts' folder
- `requirements.txt` — the pinned environment
- `verify/battery.py`, `verify/soliton_obituary.py` — the check helper and the parity convention
- `papers/broken-born-checkpoint-v2.md` §12 and `papers/reciprocity-toy-models.md` §2–§5 — the claims the scripts gate
- `review/round3-adjudication.md` 'Rulings', 'Decisions' — the unchecked rulings; the script replacement
- `review/round4-adjudication.md` header — the arbitration scripts in `review/`
- `HANDOFF.md` §2 — the ✓ on the Debt-3 figure
