---
title: "Kinetic mixing between sectors"
weight: 120
status: established
description: "Gravity alone mixes two photons only at six loops (ε ≲ 10⁻¹³) and not at all if hidden charge conjugation is exact; no visible flux while U(1)_d is unbroken; and the leakage channels mixing would open, closed by strict P4."
provenance: [T]
sources:
  - "papers/broken-born-checkpoint-v2.md §4"
  - "papers/broken-born-checkpoint-v2.md ref [27]"
  - "notes/knot-dark-matter-standalone.md §2"
  - "review/v3-worklog.md 'Round-2 pending list'"
  - "review/v3-worklog.md 'Findings neither referee raised'"
  - "review/round3-adjudication.md 'Rulings' 9"
  - "review/round3-adjudication.md 'What survives v3'"
  - "review/round3-adjudication.md 'Decisions' 1"
  - "review/round3/referee/audit-notes.md Step 1"
  - "review/round3/referee/audit-notes.md Step 4(a)"
  - "review/round3/referee/audit-notes.md Step 4(b)"
  - "HANDOFF.md §6"
---

*Kinetic mixing is a coupling between the field strengths of two U(1) gauge forces, such as our photon and a hidden photon, through a term proportional to ε F_μν B^μν. When ε is not zero, particles charged under the hidden force acquire a small electric charge under ours, so kinetic mixing is a standard route by which a hidden sector can leak into the visible one. Three literature results framed the soliton candidate's hidden sector: gravity alone produces mixing only at six loops or more, and none if hidden charge conjugation is an exact symmetry; while the hidden photon stays massless, mixing does not make hidden monopoles magnetic under our electromagnetism; and what leakage remains would give the hidden fermion ψ, and through the Witten effect the monopoles, a small visible electric charge. The program closed these channels by taking its postulate P4 strictly.*

**Status:** Established — literature [T]: Gherghetta–Kersten–Olive–Pospelov [27S] on gravity-induced mixing, and Hiramatsu et al. and Terning–Verhaaren on the massless-photon case, as read in the v3 worklog and checked in round 3. "The kinetic-mixing literature points (a) and (c)" survive v3 (round-3 adjudication). The Witten-effect finding was "Accepted, not re-checked" (ruling 9).

## Key facts

- **(a) Gravity alone** (#14 §2(a)): "Kinetic mixing vanishes to all perturbative orders if hidden charge conjugation is an exact symmetry. If it is broken, gravity can induce mixing, but only at six loops or more, giving epsilon <~ 1e-13 [9]." #11 adopts it in [P4](/wiki/program/postulates/p4-polarized-matter): "[P; taken strictly since v2.1: no kinetic mixing between the sectors beyond what gravity induces, which vanishes if hidden charge conjugation is exact and otherwise first appears at six loops, ε ≲ 10⁻¹³ [27S].]"
- **An unresolved reading.** The round-3 referee quotes Gherghetta et al.'s abstract, "requires at least six loops and could be as large as ~1e-13", and notes that the paper presents 10⁻¹³ as a floor, "minimum kinetic mixing in any theory with hidden gauge interactions and charge symmetry breaking", which is consistent with "≲" only in the sense "up to" (audit notes, Step 1). #11's wording stands; the reading is flagged, not resolved ([conflicts between sources](/wiki/history/documents/source-conflicts)).
- **Gauged, not global** (#14 §2(b)): a discrete symmetry acting as hidden charge conjugation protects "only if that symmetry is gauged, since quantum gravity is believed to admit no exact global symmetries [11]". The v3 worklog (R4): "Quantum gravity forbids an exact global C [Banks–Seiberg 2011; Harlow–Ooguri 2021]; a gauged C (O(2)/O(3)-type) remains a loophole [Obied–Parikh, preprint]."
- **(c) No visible magnetic flux** (v3 worklog, L1): "With an unbroken dual U(1), i.e. a massless dark photon, which is v2's setup, kinetic mixing gives the dark monopole **no QED magnetic flux**" — no magnetic flux of quantum electrodynamics. Hiramatsu–Ibe–Suzuki–Yamaguchi, arXiv:2109.12771, abstract, checked: "does not induce the QED magnetic flux in the U(1) symmetric phase, even in the presence of the kinetic mixing". "Minicharged, confined monopoles need a *massive* dark photon" (Terning–Verhaaren). So v2's premise, "mixing ε gives the solitons magnetic charge εg under our photon", "is wrong for its own setup."
- **The leakage channels** (#14 §2(c)): "(i) psi acquires visible electric charge ~ epsilon e, and (ii) with CP violation the monopoles acquire a small visible electric charge [14]", CP being charge conjugation and parity. Ruling 9: "With mixing and a physical hidden θ, the monopoles carry visible electric charge ~ εθ/2π · e (Witten effect)", which "contradicts v3's "constraints act on ψ, not the dark matter" whenever ε ≠ 0." The referee put the charge at "1.6e-8 e (chi=1e-7, theta=1) to 1.6e-7 e (chi=1e-6)" (Step 4(a) item 7). A millicharged ψ would also re-thermalize the hidden sector: at ε = 10⁻⁶, freeze-in from the Standard Model plasma brings ψ to equilibrium for all masses up to 30 GeV, and decoupling below 0.2 GeV then gives "Delta N >= 0.61 (excluded)" (item 5).
- **Decision 1** (2026-10-19): "**Kinetic mixing: strict sector separation.** ε ≲ 10⁻¹³ from gravity alone, and zero if hidden charge conjugation is a gauged symmetry." "It is the program's own postulate P4 ("gauge forces do not cross polarizations") taken at face value." "It costs nothing and closes three failure channels at once: ψ millicharge, the monopoles' Witten-effect charge (ruling 9), and re-thermalization of the hidden sector." The alternative, a Planck-suppressed operator, died ([Obituary: Planck-suppressed adjoint mixing](/wiki/dark-matter/candidates/soliton-candidate/dimension-five-operator)).
- **History** (`HANDOFF.md` §6). Round 1 found "kinetic mixing unaddressed (postulate + ε ≲ 10⁻⁵ exclusion added)"; that bound was #14 v2's added postulate, a different context from the gravity-only ε ≲ 10⁻¹³. In round 2 the referee claimed "a graviton-loop mixing mechanism needing no bi-charged matter; its formula was uncited and unverified", and v2's "forbidden to all orders" was judged "too strong either way".

## Used by

- [P4: polarized matter and strict sector separation](/wiki/program/postulates/p4-polarized-matter) — the literature behind the strict reading since v2.1.
- [Row 7: a permanent null in direct detection](/wiki/predictions/direct-detection-null) — no coupling of either candidate to the Standard Model.
- [Obituary: Planck-suppressed adjoint mixing](/wiki/dark-matter/candidates/soliton-candidate/dimension-five-operator) — the dimension-5 alternative that strict P4 replaced.
- [Obituary: superheavy conjugate solitons](/wiki/dark-matter/candidates/soliton-candidate/obituary) — "dark by sector separation".
- [Obituary: the ψ relic window](/wiki/dark-matter/candidates/soliton-candidate/psi-relic-window) — ψ's millicharge channels, closed by Decision 1.
- [Benchmark-conditional arithmetic](/wiki/dark-matter/candidates/soliton-candidate/benchmark-arithmetic) — why the counterfactual monopole flux does not arise.

## Sources

- `papers/broken-born-checkpoint-v2.md` §4 — P4 and its strict reading; ref [27] — Gherghetta–Kersten–Olive–Pospelov [S]
- `review/round3-adjudication.md` 'Rulings' 9, 'What survives v3', 'Decisions' 1 — the Witten effect, the survivors, strict sector separation
- `HANDOFF.md` §6 — rounds 1 and 2 on kinetic mixing
- `review/round3/referee/audit-notes.md` Step 1, Step 4(a), Step 4(b) — the floor reading, the leakage magnitudes, the literature check
- `review/v3-worklog.md` 'Round-2 pending list' (R4) and 'Findings neither referee raised' (L1) — the literature as read for v3
- `notes/knot-dark-matter-standalone.md` §2 — points (a), (b) and (c)
