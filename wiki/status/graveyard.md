---
title: "The graveyard: dead claims"
weight: 10
status: record
description: "Every dead claim with what killed it and when, linked to its obituary: momentum clumping, collapse-powered expansion, the monopole explanation, α_d ≈ 34, the soliton candidate and its components, the naive toy potential, and the popsci-only magnetic identification."
sources:
  - "CLAUDE.md 'Since the handoff'"
  - "papers/broken-born-checkpoint-v2.md §9"
  - "papers/broken-born-checkpoint-v2.md §11.1"
  - "papers/broken-born-checkpoint-v2.md §12"
  - "papers/broken-born-checkpoint-v2.md §13"
  - "papers/broken-born-checkpoint-v2.md App. A"
  - "papers/reciprocity-toy-models.md §4"
  - "review/round4-adjudication.md 'Rulings'"
  - "review/round3-adjudication.md 'Rulings'"
  - "review/round3-adjudication.md 'Decisions'"
  - "HANDOFF.md §2"
  - "notes/broken-born-theory.md §6"
  - "notes/debt3c-ufd-endpoint.md 'Verdict and closure of Debt 3'"
  - "popsci/universes-other-half.md 'Dark matter as the other polarization'"
---

*The graveyard is the register of the program's dead claims: ideas that were proposed, tested by calculation, by review or against observations, and failed. Each line links to an obituary page that says what was claimed, how it was tested, why it failed and what survived it. The program reports these deaths prominently, because its own incentives ran against them and they are therefore among its most reliable findings, and a claim recorded here is not revived.*

**Status:** Record, a register current to 2026-10-20 — no tags of its own — each death was decided by the calculation, review ruling or recorded decision named on its line, and the root `CLAUDE.md` rule applies: claims listed as dead stay dead.

## Key facts

- `HANDOFF.md` §2 lists as "Dead (killed by own calculations — keep dead)": clumping of dark matter in momentum space as dynamics; "conjugate collapse powers our expansion"; conjugate monopoles as the explanation of our monopole non-detection; and α_d ≈ 34 via Dirac quantization against our photon. The root `CLAUDE.md` adds the superheavy soliton candidate, now "**dead** as a program-native proposal".
- [Momentum clumping](/wiki/dark-matter/momentum-clumping) died three ways (#11 §9). For particles the mean-field criterion fails by 10²⁸–10³¹ at the scattering benchmark [D]; where clumping would be mandatory for wave dark matter, it would drain ultra-faint dwarf galaxies, which are observed intact; elsewhere it is tunable and never required. `HANDOFF.md` §2 marks the 10²⁸–10³¹ figure ✓, but no script in `verify/` checks it, and #11 tags it [D].
- "Conjugate collapse powers our expansion" died twice (#11 App. A item 9): the chat-era dictionary w_eff = −2 − w̃ gave w = −2, which is falsified, and the corrected dictionary w_eff = −w̃ removed the mechanism, since dual dust maps to dust.
- The soliton candidate was retired on 2026-10-19 (#11 §12). One defect per Hubble volume gives a Kibble yield p ≈ 104 [V], not the p ≈ 0.023 of #14 v3, and at minimum production the v3 benchmark of 3×10¹³ GeV is overproduced by 2.1×10³–1.2×10⁴ [V]. The round-3 review returned verdict C, and round-3 Decision 2 retired the candidate; the numbers are gated in `verify/soliton_obituary.py`.
- #11 §13 lists as "withdrawn with cause": velocity-space granularity in halos, Fornax friction suppression, and superheavy-soliton dark matter.
- The naive ρ-preserving potential −μ[Tr(K K_ref)]² of toy model I is unbounded below once H is dynamical, reaching −8.9 × 10⁶ μ at boost parameter 4 (`papers/reciprocity-toy-models.md` §4). Round 4 upheld findings F1–F2, and the note's v2 replaced it with a bounded form.
- Several deaths left something standing: the [island discriminant](/wiki/predictions/island-discriminant) from Debt 3, [conjugate monopoles as ontology](/wiki/electric-magnetic-duality/conjugate-monopoles), the exclusion of the minimal hidden sector by [W′ overclosure](/wiki/dark-matter/candidates/soliton-candidate/w-prime-overclosure), and the [bounded potential V_b](/wiki/symmetry-breaking/toy-models/coset-model/bounded-potential).

## Dead claims by section

### Spontaneous breaking of reciprocity

- [Obituary: the naive ρ-preserving potential](/wiki/symmetry-breaking/toy-models/coset-model/naive-potential) — the potential the toy-model note's v1 added to model I to pin the polarization; unbounded below with H dynamical, so its vacuum is a saddle. Killed by round-4 findings F1–F2; the repair was applied in the note's v2 on 2026-10-20 (`review/round4-adjudication.md`).

### Dark matter

- [Obituary: velocity clumping, the founding image](/wiki/dark-matter/momentum-clumping/founding-image) — dark matter fragmenting into discrete velocity streams, founding supposition 3 of #11 App. A; tested three ways in Debt 3 and failed all three (#11 §9). "Dead as dynamics" (#11 App. A).
- [Obituary: Scenario A and the ultra-faint-dwarf endpoint](/wiki/dark-matter/momentum-clumping/wave-island/scenario-a) — if the gated channel also makes dwarf cores, condensation becomes mandatory in ultra-faint dwarfs and drains their dark matter; falsified by their observed density and longevity (calc note #4, `notes/debt3c-ufd-endpoint.md`; #11 §9).
- [Obituary: velocity-space granularity in halos (old row 3)](/wiki/dark-matter/momentum-clumping/velocity-granularity) — the lab notebook's flagship prediction of "fragmentation into O(10) macro-streams" (#1 §9); withdrawn permanently on both islands after Debt 3 (calc note #4; #11 §13).
- [Obituary: Fornax friction suppression (old row 4)](/wiki/dark-matter/momentum-clumping/fornax-friction) — suppressed dynamical friction in condensed dwarf cores, which would have kept Fornax's globular clusters in place; withdrawn with the condensed cores that carried it (calc note #4; #11 §13).
- [Obituary: superheavy conjugate solitons](/wiki/dark-matter/candidates/soliton-candidate/obituary) — the third dark-matter candidate of #11 v2.0, superheavy monopoles of a hidden gauge sector written up as #14; retired 2026-10-19 after the round-3 review (verdict C) found its abundance estimate misnormalized (#11 §12; round-3 Decision 2).
- [Obituary: the hidden SU(2) → U(1) proposal](/wiki/dark-matter/candidates/soliton-candidate/hidden-sector) — the hidden gauge sector #14 was built on; dead as a program-native proposal with the candidate. Its low-scale version is prior art (Murayama–Shu; Liveoak–Maharana–Wells) that owes nothing to Born reciprocity (round-3 Decision 2).
- [Obituary: the coupling α_d ≈ 34](/wiki/dark-matter/candidates/soliton-candidate/alpha-d-coupling) — fixing the hidden coupling by Dirac quantization against our photon (round 1's valid kill, `HANDOFF.md` §2), then by reciprocity acting as modular S on the coupling (round 2's weakest link, "numerology", `HANDOFF.md` §6); without that conjecture α_d is a free strong coupling.
- [Obituary: the Kibble normalization](/wiki/dark-matter/candidates/soliton-candidate/kibble-normalization) — #14 v3's yield n/s = p (T_c/M_Pl)³ with p ≈ 0.023 dropped a factor (1.66√g*)³; one defect per Hubble volume gives p ≈ 104, the causal minimum. Round-3 ruling 1, upheld [V].
- [Obituary: the √N topological floor (chat-only)](/wiki/dark-matter/candidates/soliton-candidate/sqrt-n-floor) — a chat-only bound on the relic abundance; its premise, Kibble production as a ceiling, is inverted (ruling 3), and with no candidate left to serve it was dropped (round-3 Decision 3).
- [Obituary: the ψ relic window](/wiki/dark-matter/candidates/soliton-candidate/psi-relic-window) — #14 v3's mass window for the light hidden fermion ψ was too high: the recount puts 10% of the dark matter at 45–49 GeV and all of it at 146–158 GeV (ruling 4, upheld); MeV-scale ψ would freeze out during nucleosynthesis (ruling 6, accepted, not re-checked).
- [Obituary: Planck-suppressed adjoint mixing](/wiki/dark-matter/candidates/soliton-candidate/dimension-five-operator) — the "O(1) coefficient at the Planck scale" for the dimension-5 mixing operator has no source; the literature generates the operator only from states charged under both sectors, which sector separation excludes (ruling 7). The program then took P4 strictly (round-3 Decision 1).

### Cosmology

- [Obituary: conjugate collapse powers our expansion](/wiki/cosmology/scale-factor-duality/collapse-powered-expansion) — founding supposition 9; the chat-era heuristic w_eff = −2 − w̃ gave w = −2, which is falsified, and the corrected [duality dictionary](/wiki/cosmology/scale-factor-duality/duality-dictionary) removed the mechanism: "dead twice" (#11 App. A item 9). The correction is already in the lab notebook's version 0.1 (`notes/broken-born-theory.md` §0, §6).

### Electric–magnetic duality

- [Obituary: conjugate monopoles explain the null result](/wiki/electric-magnetic-duality/monopole-explanation) — the explanatory half of founding supposition 5: the relevant duality is electric–magnetic, not x ↔ p, and inflationary dilution already accounts for the absence of monopoles (#11 §11.1). The ontology half stands.
- [Obituary: the magnetic identification (popsci-only)](/wiki/electric-magnetic-duality/magnetic-identification) — the popular article's statement that "the momentum-polarized sector is the magnetic side of electromagnetism", with a magnetic coupling "about 34, against our 1/137" (#12); never a program claim, and in conflict with the dead α_d ≈ 34 claim, with strict P4 and with prediction [row 7](/wiki/predictions/direct-detection-null).

### Predictions

The predictions section holds no obituaries of its own. The predictions #11 §13 withdraws with cause are recorded above: velocity-space granularity and Fornax friction suppression (Debt 3) and superheavy-soliton dark matter (the soliton candidate). The table's earlier rows are traced on [History of the predictions table](/wiki/predictions/table-history).

## Sources

- `CLAUDE.md` "Since the handoff" — the soliton candidate dead as a program-native proposal; strict sector separation in force.
- `papers/broken-born-checkpoint-v2.md` §9, §11.1, §12, §13, App. A — the Debt-3 obituary, the monopole audit, the soliton obituary, the withdrawn predictions, and the fates of the founding suppositions.
- `papers/reciprocity-toy-models.md` §4 — the naive potential's runaway and the bounded replacement.
- `review/round4-adjudication.md` "Rulings" — findings F1–F2 on the naive potential, upheld.
- `review/round3-adjudication.md` "Rulings", "Decisions" — rulings 1–13 on #14 v3; Decisions 1–3 (strict P4, retirement of the candidate, the √N floor dropped).
- `HANDOFF.md` §2, §6 — the dead list at the move from claude.ai; the round-1 and round-2 verdicts on α_d.
- `notes/broken-born-theory.md` §0, §6, §9 — the corrected dictionary; the original rows 3 and 4.
- `notes/debt3c-ufd-endpoint.md` "Verdict and closure of Debt 3" — Scenario A falsified; rows 3 and 4 withdrawn on both islands.
- `popsci/universes-other-half.md` "Dark matter as the other polarization" — the magnetic identification.
