---
title: "The gate: scripts/check.sh"
weight: 60
status: method
description: "The definition of done: six verify/ scripts and the wiki check, each check printing PASS or FAIL with its measured value; how it runs, what each script gates, what is not gated, how the script list grew, and a recorded run."
sources:
  - "scripts/check.sh"
  - "scripts/check-wiki.py"
  - "CLAUDE.md 'The gate'"
  - "CLAUDE.md 'Layout'"
  - "requirements.txt"
  - "verify/battery.py"
  - "verify/soliton_obituary.py"
  - "verify/toy_coset.py"
  - "verify/toy_gw.py"
  - "verify/toy_s4.py"
  - "verify/toy_s5.py"
  - "papers/broken-born-checkpoint-v2.md §12"
  - "papers/broken-born-checkpoint-v2.md §14 item 11"
  - "papers/reciprocity-toy-models.md §2–§5"
  - "review/round3-adjudication.md 'Rulings'"
  - "review/round3-adjudication.md 'Decisions'"
  - "review/round3-adjudication.md 'What survives v3'"
  - "review/round4-adjudication.md header"
  - "review/wiki-build-checks/README.md"
  - "review/wiki-build-flags.md items 16, 33, 38"
  - "wiki/CLAUDE.md 'The gate'"
  - "HANDOFF.md §2"
---

*The gate is the shell script `scripts/check.sh`, which runs the repository's six verification scripts in `verify/` and then the wiki's own consistency check, and exits with a failure if any check fails. The project calls it "the definition of done": work is not finished until it passes, and a check may not be weakened to make it pass. Each verification script prints one line per check, a pass or a fail together with the measured value where there is one, so the record of a run shows what was tested as well as the verdict. What the gate tests is the arithmetic of the models the scripts encode and the form of the wiki; which claims it covers, and which it leaves to derivation, review or nothing, is listed below.*

**Status:** Method, in force — untagged — root `CLAUDE.md` ('The gate'); the results it checks carry [V] where the papers cite them. In the run of 2026-10-21 every check passed and the script ended "OK — all checks pass."

## The rule

Root `CLAUDE.md`, 'The gate': "`scripts/check.sh` is the definition of done. It runs every script in `verify/`, then `scripts/check-wiki.py` on the wiki, and exits non-zero on any failure. It must pass before work is called finished. Do not weaken a check to make it pass. New verification scripts get wired into it." The script's own header: "The definition of done for this repo. Exits non-zero if any verification script fails. New arbitration and audit scripts in verify/ get added here."

The gate is where [the iron rule](/wiki/method/verification/iron-rule) becomes enforceable. A number that a current document asserts gets a check in a script, and the script runs every time the gate runs, so a later edit to a script that changes a computed number, or a change of environment that changes the arithmetic, shows up as a failure. The scripts hold their own copies of the figures they compare against and do not read the documents, so an edit to a document's figure does not trip them.

## How it runs

- **Environment.** The scripts run in a Python virtual environment, `.venv`, built from `requirements.txt`, which pins numpy==2.5.4 and sympy==1.14.0. Without it the gate prints `check FAILED: no .venv. Create it with:` and the command to create it, and exits with status 1.
- **An explicit list.** The script runs `verify/battery.py`, `verify/soliton_obituary.py`, `verify/toy_coset.py`, `verify/toy_gw.py`, `verify/toy_s4.py` and `verify/toy_s5.py`, in that order, named one by one rather than matched by a pattern. "Runs every script in `verify/`" therefore holds as long as the list matches the folder, as it does now; a new script counts only once it is added to the list. Root `CLAUDE.md`'s 'Layout' names only `battery.py` and `soliton_obituary.py` (flag 38 in `review/wiki-build-flags.md`); the list in the script is the fact.
- **Every script runs.** The shell options are `set -uo pipefail`, without `-e`. A failing script prints its name followed by `FAILED` and sets a status variable; the loop continues, so one run reports every failure rather than the first.
- **Then the wiki.** After the six scripts it runs `scripts/check-wiki.py` on the whole wiki, with the same failure handling.
- **The verdict.** If nothing failed it prints "OK — all checks pass." and exits 0; otherwise it exits 1.
- **Deterministic.** Every script that draws random numbers fixes its seeds, so a rerun in the pinned environment prints the same values. `verify/toy_s4.py` says so in its docstring: "Fixed seeds, so the run is deterministic."

## The check line

All six verification scripts define the same helper, `check(name, ok, detail="")`. It prints `PASS` or `FAIL`, the check's name and, when a detail is given, the measured value in square brackets, and it records the failure. At the end a script with failures prints `FAILED`, the count and the names, and exits with status 1; a clean script prints a closing "OK" line of its own. Lines indented without a verdict print measured values for the reader (the T4 limits, the Monte Carlo rows, the truncation sweep) and gate nothing by themselves. `verify/battery.py` states the convention: "Every verdict is a boolean or a number against a tolerance, never a judgement."

Two kinds of check need distinguishing:

- a check against something known independently of the documents, an [independent anchor](/wiki/method/verification/independent-anchors), or a property the derivation predicts (a symmetry, a sign, a scaling);
- a check labelled "parity" or "quoted:", which compares the output with the figure a document prints. It confirms that the document prints what the code computes and that the environment still reproduces it. It is a reproduction, and by itself it tests nothing about whether the figure is right.

## What each script gates

| Script | What it checks | Claims it gates | Page |
| --- | --- | --- | --- |
| `verify/battery.py` | tests T1–T7 and two parity checks | #11 §2's [Tier 1](/wiki/method/claim-tiers#tier-1-explicit-algebra): §5, §6, §7.2, §7.3 | [the battery](/wiki/method/verification/battery) |
| `verify/soliton_obituary.py` | four anchors; round-3 rulings 1, 2, 4, 5; the [W′ overclosure](/wiki/dark-matter/candidates/soliton-candidate/w-prime-overclosure) | every number #11 §12 tags [V] | [the soliton-obituary script](/wiki/method/verification/soliton-obituary-script) |
| `verify/toy_coset.py` | [model I](/wiki/symmetry-breaking/toy-models/coset-model)'s action, vacua, [order parameter](/wiki/symmetry-breaking/order-parameter), spectrum; the [bounded potential](/wiki/symmetry-breaking/toy-models/coset-model/bounded-potential) with H dynamical | toy note §2; §4's potential | [the toy-model scripts](/wiki/method/verification/toy-model-scripts) |
| `verify/toy_gw.py` | the [matrix base](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/model-and-matrix-base); the [duality lemma](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/matrix-base-lemma); complex and real [model II](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar); the [one-loop split](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/real-model-lead); the tadpole series | toy note §3; §4's restoration premise | same |
| `verify/toy_s4.py` | the frozen-H [Monte Carlo](/wiki/symmetry-breaking/toy-models/coset-model/monte-carlo), four seeds with error bars | toy note §4's table | same |
| `verify/toy_s5.py` | η's null lines; the [section condition](/wiki/symmetry-breaking/section-condition); the [(H, K)-built coupling](/wiki/symmetry-breaking/matter-coupling) | toy note §5 | same |
| `scripts/check-wiki.py` | the wiki's links, anchors, maps, sources and page shape | `wiki/CLAUDE.md`'s conventions | [below](#the-wiki-check) |

#11 tags the toy results [D][V] (§4, the [P2′](/wiki/program/postulates/p2-prime) refinement; §10, "Toy-model support") and records them in §14 item 11. #11 §12 ends: "The [V] numbers here are gated in `verify/soliton_obituary.py`."

## What is not gated

The gate covers less than the record contains. These are outside it:

- **Round-3 numbers the adjudicator did not compute.** Rulings 3 and 6–13 have no checks, and neither has ruling 4's referee range: the adjudicator "did not re-run the referee's Kibble–Zurek integration", and rulings 6 and 9 were "Accepted, not re-checked" (`review/round3-adjudication.md`; [Review round 3](/wiki/method/review/round-3)). The soliton script's docstring nonetheless claims every number of that record (flag 33 in `review/wiki-build-flags.md`). The [withdrawn manuscript](/wiki/dark-matter/candidates/soliton-candidate/obituary)'s benchmark arithmetic ("flux, densities, σ_T/M"), which 'What survives v3' keeps, lost its checks when they were retired with the paper; of that list only the W′ overclosure is gated ([benchmark arithmetic](/wiki/dark-matter/candidates/soliton-candidate/benchmark-arithmetic)).
- **Round-4 numbers outside the toy note.** The adjudicator's F1 sequence and F2's eigenvalues at λ = 10 and 100 come from `review/round4/adjudicator/arb.py`, and its control re-runs from `review/round4/adjudicator/ctrl.py`; the gate checks the boost at t = 4 and the eigenvalues at λ = μ = 1.
- **Analytic arguments.** The toy note's argument that the complex model's breaking does not survive quantization is analytic (§4). The gate checks its premise, the exact continuous symmetry, not its conclusion ([quantum restoration](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/quantum-restoration)).
- **A check mark without a script.** `HANDOFF.md` §2 marks the Debt-3 figure "criterion fails by 10²⁸–10³¹" ✓, but no script in `verify/` computes it, and #11 §9 tags it [D] (flag 16 in `review/wiki-build-flags.md`; [the mean-field criterion](/wiki/dark-matter/momentum-clumping/instability-criterion)). A wiki-build recomputation, `review/wiki-build-checks/debt3a_check.py`, reproduces it and "could be moved into `verify/`" (flag 16).
- **Whole documents.** `verify/` holds no script for the numbers of the Debt-3 calc notes or of #13 ([the Debt-3 calc notes](/wiki/history/documents/debt-3-notes); [conjugate special relativity](/wiki/conjugate-relativity)).
- **Review and wiki-build scripts.** The referees' and adjudicators' scripts stay in `review/` and are not run: `review/round3/adjudicator/round3_arb.py`, `review/round4/adjudicator/arb.py` and `review/round4/adjudicator/ctrl.py`, with the referees' scripts beside them. Root `CLAUDE.md`'s layout says of `verify/` that "arbitration and audit scripts go here"; the sources do not settle the difference, so it stands as a gap. The gate carries their corrected results instead, in `verify/soliton_obituary.py` and in checks labelled with round-4 findings (F3, F4, F6) in the toy scripts. The executed checks of the wiki build are likewise outside: "none is wired into `scripts/check.sh`" (`review/wiki-build-checks/README.md`).

## The wiki check

`scripts/check-wiki.py` applies the conventions of `wiki/CLAUDE.md` to every page. Its docstring lists the checks in order of severity:

- **link** — an internal link points at a page that does not exist, or is not an absolute /wiki/ link;
- **anchor** — a link points at a heading that does not exist;
- **map** — a page is not linked from its parent section's index;
- **source** — a frontmatter source, or a repository path in inline code, names a missing file;
- **frontmatter**, **weight**, **section** — missing or invalid fields, siblings sharing a weight, a folder without an index or a file named claude.md;
- **gist**, **statusline** — the page's opening: the italic passage and the status line;
- **star** — an unescaped starred symbol such as v\*, whose asterisk can end an italic passage early;
- **h1**, **fence** — no top-level heading, and a language on every code fence;
- **acronym** — an acronym that is unregistered, or used without its expansion nearby or a link (registry: `scripts/wiki-acronyms.txt`).

Its reason for existing, from the docstring: "Hugo does not validate internal links: it renders /wiki/does-not-exist without complaint. This script is the only thing standing between a renamed page and a silent 404." Given file names, it reports only on those files while resolving links across the whole wiki; with `--stats` it also prints status counts and the pages with fewer than three inbound links from outside their parent's map.

It checks form, not content. It does not compare a page's numbers, quotations, tags or statuses with the source documents; that comparison was the work of the wiki build's verifiers, whose suspected source errors are in `review/wiki-build-flags.md` with executed checks in `review/wiki-build-checks/`.

## How the script list grew

The commit history records each change:

- **2026-10-19, commit 008c3ee.** The first gate ran `verify/battery.py` alone ("add battery gate").
- **2026-10-19, commit 678e48a.** knot_numbers.py was added ("Recompute every number in #14 v2"); it later checked every number of the soliton manuscript's third version.
- **2026-10-19, commits d15cd4a and 5dbaa82.** dark_sector.py joined the list for the worklog's items O1 and O2 ("Script O1/O2: minimal dark sector overcloses; needs a light doublet"); when v3 was cut it was "merged into" knot_numbers.py and left the list again.
- **2026-10-19, commit 96f58da.** After round 3, knot_numbers.py was given the corrected inputs and independent anchors, and the commit message records the consequence: "scripts/check.sh fails on v3's affected claims, by design, until v3 is revised or withdrawn."
- **2026-10-19, commit 5b6efaa.** The manuscript was withdrawn and knot_numbers.py replaced by `verify/soliton_obituary.py`. The adjudication's 'Decisions' explains why this is not a weakened check: "This retires the checks of a withdrawn paper. It does not loosen the gate: the gate verifies what current documents claim, and v3 no longer claims anything." The commit message: "the gate is green again because the withdrawn paper no longer claims anything."
- **2026-10-19, commits 0e0f51e to 56485d3.** The four toy-model scripts were added chunk by chunk as the models were built.
- **2026-10-20, commit 17e1338.** `scripts/check-wiki.py` was added ("Add the wiki gate: links, anchors, section maps, sources, page shape"); on 2026-10-21 it began checking starred symbols (`wiki/CLAUDE.md`, 'Build state').

## A recorded run

The closing lines of the run of 2026-10-21, after the six scripts' own closing lines:

```text
OK — S5 (weak form) and the section-condition structure check out.

wiki OK — 278 pages, no problems

OK — all checks pass.
```

The output of each script is quoted on its page, in full except for parts A and B of `verify/toy_s5.py`: [the battery](/wiki/method/verification/battery#the-recorded-output), [the soliton-obituary script](/wiki/method/verification/soliton-obituary-script#the-recorded-output) and [the toy-model scripts](/wiki/method/verification/toy-model-scripts).

## A name shared

"The gate" in the physics pages is a different thing: [the velocity gate](/wiki/dark-matter/conjugate-matter/velocity-gate) that switches [conjugate matter](/wiki/dark-matter/conjugate-matter)'s self-interaction off at high relative velocity.

## Sources

- `scripts/check.sh` — the script list, the environment check, the failure handling, the final line
- `scripts/check-wiki.py` — the wiki checks, their order and their stated purpose
- Root `CLAUDE.md` 'The gate', 'Layout' — the definition of done; the scripts' folder
- `requirements.txt` — the pinned environment
- `verify/battery.py`, `verify/soliton_obituary.py`, `verify/toy_coset.py`, `verify/toy_gw.py`, `verify/toy_s4.py`, `verify/toy_s5.py` — the check helper, the parity convention, the seeds
- `papers/broken-born-checkpoint-v2.md` §12, §14 item 11, and `papers/reciprocity-toy-models.md` §2–§5 — the claims the scripts gate
- `review/round3-adjudication.md` 'Rulings', 'What survives v3', 'Decisions' — the unchecked rulings; the retired benchmark checks; the script replacement
- `review/round4-adjudication.md` header — the arbitration scripts in `review/`
- `review/wiki-build-checks/README.md` and `review/wiki-build-flags.md` items 16, 33, 38 — the wiki build's checks, outside the gate; the Debt-3 check mark; the soliton script's claimed coverage; the Layout's two scripts
- `HANDOFF.md` §2 — the ✓ on the Debt-3 figure
- `wiki/CLAUDE.md` 'The gate', 'Build state' — how the wiki check is run; when it was extended
- Git history: commits 008c3ee, 678e48a, d15cd4a, 5dbaa82, 96f58da, 5b6efaa, 0e0f51e, 56485d3 and 17e1338 — the growth of the script list
