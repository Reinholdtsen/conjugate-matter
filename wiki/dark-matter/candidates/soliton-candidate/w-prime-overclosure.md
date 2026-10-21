---
title: "W′ overclosure: the minimal sector is excluded"
weight: 80
status: alive
description: "Without a light charged fermion the thermal W′± would outweigh the observed dark matter 10¹⁶–10¹⁷ times, which forced the hidden doublet — a result that survives the candidate."
provenance: [V]
sources:
  - "papers/broken-born-checkpoint-v2.md §12"
  - "verify/soliton_obituary.py"
  - "notes/knot-dark-matter-standalone.md §3"
  - "review/round3-adjudication.md 'What survives v3'"
  - "review/round3/referee/audit-notes.md Step 2"
  - "review/round3/referee/audit-notes.md Step 4(a)"
  - "review/v3-worklog.md 'New open items'"
  - "review/v3-worklog.md 'v3 as drafted (2026-10-19)'"
---

*W′ overclosure is the result that the simplest version of the soliton candidate's hidden sector — SU(2)_d broken to U(1)_d by an adjoint Higgs field and nothing else — is excluded by its own heavy charged bosons, the W′±. With no lighter particle carrying hidden charge, the W′± cannot decay. The hot hidden plasma needed to form the monopoles also fills the universe with W′±, and after they freeze out their density would exceed the observed dark matter 10¹⁶ to 10¹⁷ times. #14 v3 therefore added a light hidden fermion ψ for the W′± to decay into. The calculation was done at the withdrawn benchmark, but the statement that the minimal sector is excluded survived the candidate's retirement and is machine-checked.*

**Status:** Alive — it survives the candidate, conditional on the benchmark. #11 §12 lists it under "What survives" with [V]; the round-3 adjudication lists "The statement that the minimal adjoint-only sector is excluded" among what survives v3. Gated in `verify/soliton_obituary.py` ([the soliton-obituary script](/wiki/method/verification/soliton-obituary-script)).

## Key facts

- **The result** (#11 §12): "The minimal adjoint-only SU(2) → U(1) hidden sector is excluded on its own terms: its stable W′± overclose the universe by 10¹⁶–10¹⁷ at the v3 benchmark [V]."
- **The argument** (#14 §3, "A negative result: the minimal model fails."): "With only the adjoint scalar, the W'+- are the lightest hidden-charged states and are stable by U(1)_d charge. Kibble production (below) requires a hidden plasma at temperature ~ v, so the W' are thermally populated and freeze out. At the benchmark mass below, m_W' ~ (5-9)e11 GeV. Standard freeze-out [17] then leaves them at 1e16 to 1e17 times the observed dark-matter density, bracketing the annihilation coefficient over a factor of ten. The adjoint-only sector is excluded." See [relic abundance mechanisms](/wiki/dark-matter/candidates/relic-abundance) and [the hidden SU(2) → U(1) proposal](/wiki/dark-matter/candidates/soliton-candidate/hidden-sector).
- **The gate's check.** The script takes the annihilation cross-section σv = κ π α_W′²/m_W′², with κ = 1 and 10, m_W′ = α_W′ M/f, f = 1 and 1.787, at M = 3×10¹³ GeV; its output `stable W'+- overclose by 1e16-1e17  [9.5e+15-2.0e+17]` passes.
- **The referee's check** (audit notes, Step 2): "c=1..10: 9.4e15-1.95e17; with c=6.67 (W+W- -> gg at threshold, own detailed balance of hep-ph/9405359 eq. 5.15; scalar check gives textbook 2.000): 1.3e16-4.0e16", verdict "CONFIRMED (bracket reasonable)". Here gg are hidden photon pairs, and the coefficient 6.67 comes from detailed balance, the annihilation rate inferred from the inverse process γγ → W⁺W⁻.
- **It holds for a colder hidden sector** (Step 4(a) item 4): "W' overclosure survives (xi=0.76: 9.9e15 - 2.9e16, step4b.out)" ([the hidden sector's thermal history](/wiki/dark-matter/candidates/soliton-candidate/hidden-thermal-history)).
- **What it forced** (#14 §3): "The fix is the Dirac doublet psi: W'+ can decay to a psi pair." This became requirement (i) of #14 §6, a light hidden doublet fermion, whose own relic window was later recounted ([Obituary: the ψ relic window](/wiki/dark-matter/candidates/soliton-candidate/psi-relic-window)).
- **How it was found.** The v3 worklog's item O1 was headed "dark W′± fate: fatal to the minimal model, not to the candidate". When v3 was drafted, the gated check corrected a planned figure: "the minimal model overcloses by 10¹⁶–10¹⁷ (not 10¹⁵–10¹⁷)". The worklog's own stage numbers ("Under F1 and F2, m_W′ = α M\*/f = 1.2–2.2×10¹¹ GeV"; a relic of "0.8–15×10¹⁶ × the observed density") belong to an earlier stage and were never reconciled with #14; the record cites #11, the adjudication and the gate.

## Sources

- `papers/broken-born-checkpoint-v2.md` §12 — the surviving statement, tagged [V]
- `review/round3-adjudication.md` 'What survives v3' — listed as surviving
- `verify/soliton_obituary.py` — the gated check and its inputs
- `review/round3/referee/audit-notes.md` Step 2 — the referee's coefficient by detailed balance; Step 4(a) — the colder-sector values
- `review/v3-worklog.md` 'New open items' (O1), 'v3 as drafted (2026-10-19)' — how it was found and corrected
- `notes/knot-dark-matter-standalone.md` §3 — the argument and the fix
