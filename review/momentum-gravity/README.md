# The momentum-gravity investigation: record

*The record behind `notes/velocity-gated-gravity.md` and `notes/gate-mechanism.md`. It holds the analyses, the
verifiers' verdicts, the critics' rulings, the scripts with their printed output, the pre-registrations and the
answer as given to Paul. The gate does not run any of it. The numbers the notes use are recomputed in
`verify/velocity_gated_gravity.py` and `verify/gate_mechanism.py`.*

Paul's question (2026-10-26): "I think the obituary is premature. Would momentum gravity look like a perturbation
to regular gravity that depends on the relative velocity of two massive bodies?" The obituary is
`wiki/dark-matter/momentum-clumping/founding-image.md` (#11 §9, the clumping problem).

## How it ran

1. **Run 1** (wf_589ec39d-e20) was lost when the machine ran out of memory. No agent had finished.
2. **Run 2** (wf_65ea65ce-bbd, 2026-10-26/27). Pre-registration: `preregistration-run2.md`.
   - Four analyses (`run2/analyses/*.json`): the program's momentum gravity, velocity clumping, tests with
     ordinary matter, tests in the dark sector.
   - Two verifiers per analysis (`run2/verdicts/<analysis>-<lens>.json`), each working from the extracted
     claims. Three were lost to a network error: both dark-tests verifiers and the ordinary-tests numbers
     verifier. Run 3 redid them.
   - A critic (`run2/critic.json`).
   - Tally of the five verifiers that returned: 107 claim checks, 72 confirmed, 32 corrected, 1 refuted,
     2 unverifiable.
3. **Run 3** (wf_91faf08e-d5e). Pre-registration: `preregistration-run3.md`.
   - The three lost verifications (`run3/verify-dark-tests-*.json`, `run3/verify-ordinary-tests-numbers.json`).
   - Two checks of the run-2 critic's own claims (`run3/verify-critic-theory.json`,
     `run3/verify-critic-numbers.json`).
   - The low-gate-width corner (`run3/corner.json`): 29 N-body runs and linear proxies.
   - A final critic (`run3/critic.json`, scripts in `scripts/critic3/`), which reran the corner's proxies and
     the Lyman-α bound with corrected formulas.
   - Tally of the five verifiers: 71 claim checks, 35 confirmed, 33 corrected, 2 refuted, 1 unverifiable.
4. **Run 4** (wf_bc695139-ab4). Pre-registration: `preregistration-run4.md`.
   - Two checks of the draft answer: every number against the printed outputs
     (`run4/answer-check-numbers.json`) and every claim's scope against the critics' rulings
     (`run4/answer-check-scope.json`). Their fixes were applied before the answer was sent.
   - A blind second derivation of whether X-exchange produces #11 §8's gate (`run4/gate-derivation.json`,
     scripts in `scripts/derivation-gate-mechanism/`).
5. **The answer** (`answer.md`): the answer as given to Paul on 2026-10-27, with the pre-registrations scored
   and the flags proposed.

## Blindness

- The run-2 pre-registration sat in the session's state file, beside the agents' folders. Three agents opened
  it: the program analyst, the clumping derivation verifier and the dark-tests analyst. Their judgment-level
  text was therefore not blind. Their executed numbers were unaffected.
- The run-3 and run-4 pre-registrations were kept outside every agent folder and named in no prompt.
- SHA-256 of the pre-registrations as committed:
  - run 2: `a3298f032a57a0dd541451ae59b1107f22cf3a9bf937dd7ead2dd1d6480fc3cb`
  - run 3: `63645c05452375a31fe0085f2a63953497d32a590caa7a726ed25c4bbea6eb05`
  - run 4: `d3217ad8544193c5ad1fc26a43a604779bfb655b2ca9a6ad91e159e19dc12463`

## Scripts

`scripts/` is the session's working folder, one subfolder per agent; each `.py` sits beside its printed
`.out`. Paths inside the scripts and the JSON name the session folder they ran in (`.../mg/<agent>/`), which
is `scripts/<agent>/` here. Some scripts import a sibling module or read a sibling output, so run them from
their own folder.

## Not kept

- The N-body snapshots and diagnostic caches (`corner/runs/*.npz`, `*.pkl`, about 90 MB). The run logs and
  `corner/diagnostics_final.out` are kept.
- The compiled kernel `corner/libgated.so`; its source `corner/gated_kernel.c` is kept.
- The downloaded DE430 lunar-coordinate document and its extracted text (copyrighted).
- The run-3 input copies (duplicates of `run2/`), the session state file and the memory log.
