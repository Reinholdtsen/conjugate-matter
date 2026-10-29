---
title: "The gate: scripts/check.sh"
weight: 60
status: method
description: "The definition of done: ten verify/ scripts and the wiki check, each check printing PASS or FAIL with its measured value; how it runs, what each script gates, what is not gated, how the script list grew, and a recorded run."
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
  - "verify/phase_space_diameter.py"
  - "verify/closed_universe.py"
  - "verify/velocity_gated_gravity.py"
  - "verify/gate_mechanism.py"
  - "notes/velocity-gated-gravity.md header"
  - "notes/gate-mechanism.md header"
  - "review/closed-universe/README.md"
  - "review/momentum-gravity/README.md"
  - "papers/broken-born-checkpoint-v2.md §12"
  - "papers/broken-born-checkpoint-v2.md §14 item 11"
  - "papers/reciprocity-toy-models.md §2–§5"
  - "review/round3-adjudication.md 'Rulings'"
  - "review/round3-adjudication.md 'Decisions'"
  - "review/round3-adjudication.md 'What survives v3'"
  - "review/round4-adjudication.md header"
  - "review/wiki-build-checks/README.md"
  - "review/wiki-build-flags.md items 16 (addendum), 33, 38"
  - "wiki/CLAUDE.md 'The gate'"
  - "site/CLAUDE.md 'The gate'"
  - "scripts/check-site.py"
  - "HANDOFF.md §2"
---

*The gate is the shell script `scripts/check.sh`, which runs the repository's ten verification scripts in `verify/` and then the wiki's own consistency check, and exits with a failure if any check fails. The project calls it "the definition of done": work is not finished until it passes, and a check may not be weakened to make it pass. Each verification script prints one line per check, a pass or a fail together with the measured value where there is one, so the record of a run shows what was tested as well as the verdict. What the gate tests is the arithmetic of the models the scripts encode and the form of the wiki; which claims it covers, and which it leaves to derivation, review or nothing, is listed below.*

**Status:** Method, in force — untagged — root `CLAUDE.md` ('The gate'); the results it checks carry [V] where the papers cite them. In the run of 2026-10-21 every check passed and the script ended "OK — all checks pass."

## The rule

Root `CLAUDE.md`, 'The gate': "`scripts/check.sh` is the definition of done. It runs every script in `verify/`, then `scripts/check-wiki.py` on the wiki, and exits non-zero on any failure. It must pass before work is called finished. Do not weaken a check to make it pass. New verification scripts get wired into it." The script's own header: "The definition of done for this repo. Exits non-zero if any verification script fails. New arbitration and audit scripts in verify/ get added here."

The gate is where [the iron rule](/wiki/method/verification/iron-rule) becomes enforceable. A number that a current document asserts gets a check in a script, and the script runs every time the gate runs, so a later edit to a script that changes a computed number, or a change of environment that changes the arithmetic, shows up as a failure. The scripts hold their own copies of the figures they compare against and do not read the documents, so an edit to a document's figure does not trip them.

## How it runs

- **Environment.** The scripts run in a Python virtual environment, `.venv`, built from `requirements.txt`, which pins numpy==2.5.4 and sympy==1.14.0. Without it the gate prints `check FAILED: no .venv. Create it with:` and the command to create it, and exits with status 1.
- **An explicit list.** The script runs `verify/battery.py`, `verify/soliton_obituary.py`, `verify/toy_coset.py`, `verify/toy_gw.py`, `verify/toy_s4.py`, `verify/toy_s5.py`, `verify/phase_space_diameter.py`, `verify/closed_universe.py`, `verify/velocity_gated_gravity.py` and `verify/gate_mechanism.py`, in that order, named one by one rather than matched by a pattern. "Runs every script in `verify/`" therefore holds as long as the list matches the folder, as it does now; a new script counts only once it is added to the list. When the wiki was built, root `CLAUDE.md`'s 'Layout' named only `battery.py` and `soliton_obituary.py` of the six scripts then in the list (flag 38 in `review/wiki-build-flags.md`); it now names all ten. The list in the script is the fact.
- **Every script runs.** The shell options are `set -uo pipefail`, without `-e`. A failing script prints its name followed by `FAILED` and sets a status variable; the loop continues, so one run reports every failure rather than the first.
- **Then the wiki.** After the ten scripts it runs `scripts/check-wiki.py` on the whole wiki, with the same failure handling.
- **The verdict.** If nothing failed it prints "OK — all checks pass." and exits 0; otherwise it exits 1.
- **Deterministic.** Every script that draws random numbers fixes its seeds, so a rerun in the pinned environment prints the same values. `verify/toy_s4.py` says so in its docstring: "Fixed seeds, so the run is deterministic."

## The check line

All ten verification scripts define the same helper, `check(name, ok, detail="")`. It prints `PASS` or `FAIL`, the check's name and, when a detail is given, the measured value in square brackets, and it records the failure. At the end a script with failures prints `FAILED`, the count and the names, and exits with status 1; a clean script prints a closing "OK" line of its own. Lines indented without a verdict print measured values for the reader (the T4 limits, the Monte Carlo rows, the truncation sweep) and gate nothing by themselves. `verify/battery.py` states the convention: "Every verdict is a boolean or a number against a tolerance, never a judgement."

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
| `verify/phase_space_diameter.py` | anchors (CODATA 2018 Planck units, Particle Data Group densities, two torsion-balance limits); the [phase-space diameter relation](/wiki/cosmology/scale-factor-duality/phase-space-diameter) and [the laboratory bound on X's range](/wiki/gravity/momentum-graviton/range-bound) | the numbers `papers/phase-space-diameter.md` computes, tagged [V] | [the phase-space-diameter script](/wiki/method/verification/phase-space-diameter-script) |
| `verify/closed_universe.py` | anchors (exact closed solutions, the three-sphere's spectrum, published curvature values); closed τ histories, data bounds, the bimetric sector, momentum space | the numbers of `notes/closed-universe.md` ([a closed Comatter universe](/wiki/cosmology/scale-factor-duality/closed-universe)) | [the closed-universe script](/wiki/method/verification/closed-universe-script) |
| `verify/velocity_gated_gravity.py` | anchors (two-body Lagrangians, spin-2 numerators, Planck 2018's age, exact growth modes); [X between ordinary bodies](/wiki/gravity/momentum-graviton/ordinary-bodies), calc note #2's shortfall, [a long-range gated attraction among χ](/wiki/dark-matter/momentum-clumping/long-range-gated-attraction), carriers; the N-body runs read from their logs | the numbers of `notes/velocity-gated-gravity.md` | [the velocity-gated-gravity script](/wiki/method/verification/velocity-gated-gravity-script) |
| `verify/gate_mechanism.py` | anchors (on-shell kinematics, the Fierz–Pauli numerator, Legendre and Chebyshev identities); exchange of X, the two readings of the fiber overlap, the polarization under boosts | the algebra and numbers of `notes/gate-mechanism.md` ([the gate mechanism](/wiki/dark-matter/conjugate-matter/gate-mechanism)) | [the gate-mechanism script](/wiki/method/verification/gate-mechanism-script) |
| `scripts/check-wiki.py` | the wiki's links, anchors, maps, sources and page shape | `wiki/CLAUDE.md`'s conventions | [below](#the-wiki-check) |

#11 tags the toy results [D][V] (§4, the [P2′](/wiki/program/postulates/p2-prime) refinement; §10, "Toy-model support") and records them in §14 item 11. #11 §12 ends: "The [V] numbers here are gated in `verify/soliton_obituary.py`." The four later scripts back the [V] tags of their notes: the phase-space-diameter note defines [V] as "machine-verified by `verify/phase_space_diameter.py`", and the closed-universe, velocity-gated-gravity and gate-mechanism notes say in their headers that their numbers are recomputed in their scripts, the velocity-gated-gravity note "except the N-body runs of §8, whose record is kept".

## What is not gated

The gate covers less than the record contains. These are outside it:

- **Round-3 numbers the adjudicator did not compute.** Rulings 3 and 6–13 have no checks, and neither has ruling 4's referee range: the adjudicator "did not re-run the referee's Kibble–Zurek integration", and rulings 6 and 9 were "Accepted, not re-checked" (`review/round3-adjudication.md`; [Review round 3](/wiki/method/review/round-3)). The soliton script's docstring nonetheless claims every number of that record (flag 33 in `review/wiki-build-flags.md`). The [withdrawn manuscript](/wiki/dark-matter/candidates/soliton-candidate/obituary)'s benchmark arithmetic ("flux, densities, σ_T/M"), which 'What survives v3' keeps, lost its checks when they were retired with the paper; of that list only the W′ overclosure is gated ([benchmark arithmetic](/wiki/dark-matter/candidates/soliton-candidate/benchmark-arithmetic)).
- **Round-4 numbers outside the toy note.** The adjudicator's F1 sequence and F2's eigenvalues at λ = 10 and 100 come from `review/round4/adjudicator/arb.py`, and its control re-runs from `review/round4/adjudicator/ctrl.py`; the gate checks the boost at t = 4 and the eigenvalues at λ = μ = 1.
- **Analytic arguments.** The toy note's argument that the complex model's breaking does not survive quantization is analytic (§4). The gate checks its premise, the exact continuous symmetry, not its conclusion ([quantum restoration](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/quantum-restoration)).
- **A check mark, backed late.** `HANDOFF.md` §2 marks the clumping figure "criterion fails by 10²⁸–10³¹" ✓, and #11 §9 tags it [D]; when the wiki was built no script in `verify/` computed it (flag 16 in `review/wiki-build-flags.md`; [the mean-field criterion](/wiki/dark-matter/momentum-clumping/instability-criterion)). A wiki-build recomputation, `review/wiki-build-checks/stream_stability_check.py`, reproduced it and "could be moved into `verify/`" (flag 16). Since 2026-10-28 block D of `verify/velocity_gated_gravity.py` ports that arithmetic and reproduces both ratios, 3.9×10⁻²⁸ and 2.9×10⁻³¹, with the linearized values beside them; flag 16's addendum: "The ✓ is now backed by a script; #11 §9's tag [D] is unchanged until Paul rules" ([the velocity-gated-gravity script](/wiki/method/verification/velocity-gated-gravity-script)).
- **Whole documents.** Apart from calc note #2's shortfall, `verify/` holds no script for the numbers of the clumping calc notes (the wave island of #3, the ultra-faint-dwarf endpoint of #4, the classicality corollary's mass and occupation number), nor for the numbers of #13 ([the clumping calc notes](/wiki/history/documents/clumping-notes); [conjugate special relativity](/wiki/conjugate-relativity)).
- **Review and wiki-build scripts.** The referees' and adjudicators' scripts stay in `review/` and are not run: `review/round3/adjudicator/round3_arb.py`, `review/round4/adjudicator/arb.py` and `review/round4/adjudicator/ctrl.py`, with the referees' scripts beside them. Root `CLAUDE.md`'s layout says of `verify/` that "arbitration and audit scripts go here", and the header of `scripts/check.sh` says the same; the sources do not settle the difference, so it stands as a gap (flag 38 in `review/wiki-build-flags.md`). The gate carries their corrected results instead, in `verify/soliton_obituary.py` and in checks labelled with round-4 findings (F3, F4, F6) in the toy scripts. The executed checks of the wiki build are likewise outside: "none is wired into `scripts/check.sh`" (`review/wiki-build-checks/README.md`), although `verify/velocity_gated_gravity.py` now ports the arithmetic of one of them, `stream_stability_check.py`. The records of the two later investigations say the same of their own scripts, "The gate does not run any of it" (`review/closed-universe/README.md`, `review/momentum-gravity/README.md`); their numbers are recomputed in `verify/closed_universe.py`, `verify/velocity_gated_gravity.py` and `verify/gate_mechanism.py` instead. The N-body runs of the momentum-gravity investigation cannot be rerun at all, because their snapshots were not kept; the gate reads their logs ([the velocity-gated-gravity script](/wiki/method/verification/velocity-gated-gravity-script#what-it-does-not-recompute)).

## The wiki check

`scripts/check-wiki.py` applies the conventions of `wiki/CLAUDE.md` to every page. Its docstring lists the checks in order of severity:

- **link** — an internal link points at a page that does not exist, or is not an absolute /wiki/ link;
- **anchor** — a link points at a heading that does not exist, with each heading's anchor computed the way Hugo computes it;
- **heading** — a heading holds a link, an image, a bare web address, emphasis or an attribute block such as `{#id}`, for which Hugo builds the anchor from only part of the heading's text or takes it from the block, so the script cannot compute it;
- **map** — a page is not linked from its parent section's index;
- **source** — a frontmatter source, or a repository path in inline code, names a missing file;
- **frontmatter**, **weight**, **section** — missing or invalid fields, siblings sharing a weight, a folder without an index, a file named claude.md, or two files that serve at one address;
- **gist**, **statusline** — the page's opening: the italic passage and the status line;
- **star** — an unescaped starred symbol such as v\*, whose asterisk can end an italic passage early;
- **h1**, **fence** — no top-level heading, and a language on every code fence;
- **acronym** — an acronym that is unregistered, or used without its expansion nearby or a link (registry: `scripts/wiki-acronyms.txt`).

Its reason for existing, from the docstring: "Hugo does not validate internal links: it renders /wiki/does-not-exist without complaint. This script catches a dead link in the Markdown, before any build." Two later checks belong to the gate of the site that publishes the wiki, `npm run check` in `site/` (`site/CLAUDE.md`): the build fails on a link to a missing page, and `scripts/check-site.py` checks the built pages, among other things that every heading got the anchor this script computes. Given file names, it reports only on those files while resolving links across the whole wiki; with `--stats` it also prints status counts and the pages with fewer than three inbound links from outside their parent's map.

It checks form, not content. It does not compare a page's numbers, quotations, tags or statuses with the source documents; that comparison was the work of the wiki build's verifiers, whose suspected source errors are in `review/wiki-build-flags.md` with executed checks in `review/wiki-build-checks/`.

## How the script list grew

The commit history records each change:

- **2026-10-19, commit 008c3ee.** The first gate ran `verify/battery.py` alone ("add battery gate").
- **2026-10-19, commit 678e48a.** knot_numbers.py was added ("Recompute every number in #14 v2"); it later checked every number of the soliton manuscript's third version.
- **2026-10-19, commits d15cd4a and 5dbaa82.** dark_sector.py joined the list for the worklog's items O1 and O2 ("Script O1/O2: minimal dark sector overcloses; needs a light doublet"); when v3 was cut it was "merged into" knot_numbers.py and left the list again.
- **2026-10-19, commit 96f58da.** After round 3, knot_numbers.py was given the corrected inputs and independent anchors, and the commit message records the consequence: "scripts/check.sh fails on v3's affected claims, by design, until v3 is revised or withdrawn."
- **2026-10-19, commit 5b6efaa.** The manuscript was withdrawn and knot_numbers.py replaced by `verify/soliton_obituary.py`. The adjudication's 'Decisions' explains why this is not a weakened check: "This retires the checks of a withdrawn paper. It does not loosen the gate: the gate verifies what current documents claim, and v3 no longer claims anything." The commit message: "the gate is green again because the withdrawn paper no longer claims anything."
- **2026-10-19, commits 0e0f51e to 56485d3.** The four toy-model scripts were added chunk by chunk as the models were built.
- **2026-10-20, commit 17e1338.** `scripts/check-wiki.py` was added ("Add the wiki gate: links, anchors, section maps, sources, page shape"); on 2026-10-21 it began checking starred symbols (commit b970e9d; [timeline](/wiki/history/timeline)). On 2026-10-22 it began computing heading anchors as Hugo does (commit b41f199), then rejecting headings whose anchors it cannot compute (commit 503d34d) and two files that serve at one address (commit 5540adc).
- **2026-10-26, commit 97934f2.** `verify/phase_space_diameter.py` was added with the phase-space-diameter note ("The phase-space-diameter note (v1.1), its gate script and worklog").
- **2026-10-28, commit b80e1a4.** `verify/closed_universe.py` was added with the closed-universe note ("The closed-universe investigation: note, script, record, flags, wiki").
- **2026-10-28.** `verify/velocity_gated_gravity.py` and `verify/gate_mechanism.py` were added with the two momentum-gravity notes, bringing the list to ten.

## A recorded run

The closing lines of the run of 2026-10-21, after the closing lines of the six scripts then in the list:

```text
OK — S5 (weak form) and the section-condition structure check out.

wiki OK — 278 pages, no problems

OK — all checks pass.
```

The output of each script is quoted on its page, in full except for parts A and B of `verify/toy_s5.py`: [the battery](/wiki/method/verification/battery#the-recorded-output), [the soliton-obituary script](/wiki/method/verification/soliton-obituary-script#the-recorded-output) and [the toy-model scripts](/wiki/method/verification/toy-model-scripts). The run predates the four later scripts; each of their pages quotes a run of its own: [the phase-space-diameter script](/wiki/method/verification/phase-space-diameter-script#the-recorded-output), [the closed-universe script](/wiki/method/verification/closed-universe-script#the-recorded-output), [the velocity-gated-gravity script](/wiki/method/verification/velocity-gated-gravity-script#the-recorded-output) and [the gate-mechanism script](/wiki/method/verification/gate-mechanism-script#the-recorded-output).

## A name shared

"The gate" in the physics pages is a different thing: [the velocity gate](/wiki/dark-matter/conjugate-matter/velocity-gate) that switches [conjugate matter](/wiki/dark-matter/conjugate-matter)'s self-interaction off at high relative velocity.

## Sources

- `scripts/check.sh` — the script list, the environment check, the failure handling, the final line
- `scripts/check-wiki.py` — the wiki checks, their order and their stated purpose
- Root `CLAUDE.md` 'The gate', 'Layout' — the definition of done; the scripts' folder
- `requirements.txt` — the pinned environment
- `verify/battery.py`, `verify/soliton_obituary.py`, `verify/toy_coset.py`, `verify/toy_gw.py`, `verify/toy_s4.py`, `verify/toy_s5.py`, `verify/phase_space_diameter.py`, `verify/closed_universe.py`, `verify/velocity_gated_gravity.py`, `verify/gate_mechanism.py` — the check helper, the parity convention, the seeds; block D of `verify/velocity_gated_gravity.py`, the ported calc note #2's arithmetic
- `notes/velocity-gated-gravity.md` header and `notes/gate-mechanism.md` header — what the two latest scripts recompute; `review/closed-universe/README.md` and `review/momentum-gravity/README.md` — the investigations' scripts, which the gate does not run, and the N-body snapshots not kept
- `papers/broken-born-checkpoint-v2.md` §12, §14 item 11, and `papers/reciprocity-toy-models.md` §2–§5 — the claims the scripts gate
- `review/round3-adjudication.md` 'Rulings', 'What survives v3', 'Decisions' — the unchecked rulings; the retired benchmark checks; the script replacement
- `review/round4-adjudication.md` header — the arbitration scripts in `review/`
- `review/wiki-build-checks/README.md` and `review/wiki-build-flags.md` items 16 (with its addendum), 33, 38 — the wiki build's checks, outside the gate; the clumping check mark and its later script; the soliton script's claimed coverage; the Layout's two scripts
- `HANDOFF.md` §2 — the ✓ on the clumping figure
- `wiki/CLAUDE.md` 'The gate' — how the wiki check is run
- `site/CLAUDE.md` 'The gate' and `scripts/check-site.py` — the site's later checks
- Git history: commits 008c3ee, 678e48a, d15cd4a, 5dbaa82, 96f58da, 5b6efaa, 0e0f51e, 56485d3, 17e1338, b970e9d, b41f199, 503d34d, 5540adc, 97934f2 and b80e1a4 — the growth of the script list and of the wiki check; `scripts/check.sh` as of 2026-10-28 for the last two scripts
