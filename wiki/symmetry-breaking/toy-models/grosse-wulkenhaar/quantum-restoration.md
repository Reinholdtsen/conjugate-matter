---
title: "Quantum restoration in the complex model"
weight: 60
status: alive
description: "Every condensate phase is an exact flat direction and the condensate is a localized lump with no volume factor, so ⟨Δ⟩ = 0 and the classical breaking does not survive; the tadpole grows with the truncation."
provenance: [D]
sources:
  - "papers/reciprocity-toy-models.md §4"
  - "papers/reciprocity-toy-models.md §6"
  - "verify/toy_gw.py 'Tadpole'"
  - "review/round4-adjudication.md 'Rulings' F6"
  - "review/round4-adjudication.md 'Revisions' 4"
  - "review/round4/referee/audit-notes.md Step 2(c)"
  - "review/round4/referee/audit-notes.md Step 3"
  - "notes/toy-lagrangian.md 'Chunk 3 results'"
---

*Quantum restoration is the result that the classical breaking found in the complex [model II](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar) disappears once the model is quantized. The relative phase β of the condensed levels costs no action, so the quantum state spreads evenly over all its values. And because the condensate occupies only finitely many oscillator levels, it is a localized lump rather than an order extending over a large volume, so nothing suppresses the fluctuations of β. The quantum average of the polarization is therefore zero, and criterion S4 fails for this route. It is a negative result, reached by an exact argument and restated in version 2 after round 4.*

**Status:** Alive, a negative result — [D] ("S4 fails, by an exact argument [D]", worklog) — confirmed "in substance" by the round-4 referee, who found the phase decoupling "stronger than stated"; the tadpole check is in `verify/toy_gw.py` ([the toy-model scripts](/wiki/method/verification/toy-model-scripts)).

## Key facts

- **Exact flat directions.** "Every condensate phase is an exact flat direction, by the U(1)^N × U(1)^N symmetry" ([complex versus real fields](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/complex-and-real-fields)). The referee found this stronger than stated: every condensed level's phase is an independent exact flat direction, so no β-dependence can arise at any loop order.
- **No volume factor.** "At fixed μ² the condensate occupies finitely many levels: it is a localized lump, not an extended order. Nothing supplies a volume factor that could suppress fluctuations of β." Hence "the quantum measure is uniform in β at every truncation, and ⟨Δ⟩ = 0. The classical breaking of §3 does not survive quantization." ([complex-model vacua](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/complex-vacua))
- **Why the argument was restated.** The referee noted that ⟨Δ⟩ = 0 at finite truncation holds for any symmetric finite system and is not by itself an argument against breaking; the operative point is that β is one compact collective coordinate with an action of order one, with no volume factor. Revision 4 asked for the restatement on that basis ([review round 4](/wiki/method/review/round-4)).
- **Tadpole caveat (finding F6).** "The bare μ² is itself renormalized. The level-0 tadpole grows as ln N (it is a harmonic sum), so fixed bare μ² is not a consistent large-N limit." The adjudication accepted F6 without re-checking it: "The no-breaking conclusion is unaffected." The worklog's "Raising N adds only massive levels" is superseded.
- **Unresolved: ln N or 2 ln N.** Version 2, the worklog and the gate (which checks that Σ_{k<N} 1/(k+1) − ln N approaches Euler's γ) write ln N. The referee and the adjudication's revision 4 write 2 ln N, from a sum of G₀ₖ + Gₖ₀. The two use different definitions, and no document reconciles them; version 2 is the higher-ranked statement.
- **Argued, not proven.** "Whether a potential on β could be stabilized by the massive tower is argued against, not proven." The worklog's version of this step: "integrating out the massive tower is assumed not to make the barrier grow with N."
- **The check not done.** "The exact solution of the related model [8] is the natural independent check. We have not carried it out." Revision 4 had asked for this comparison with Langmann–Szabo–Zarembo; it remains undone ([noncommutative field theory](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/noncommutative-field-theory)).

## Sources

- `papers/reciprocity-toy-models.md` §4, §6 — the restoration argument and its two caveats, quoted above
- `verify/toy_gw.py` 'Tadpole' — the gated ln N check
- `review/round4-adjudication.md` 'Rulings' F6, 'Revisions' 4 — F6 accepted, not re-checked; the requested restatement and comparison
- `review/round4/referee/audit-notes.md` Step 2(c), Step 3 — "stronger than stated", the logical gap, and the 2 ln N tadpole
- `notes/toy-lagrangian.md` 'Chunk 3 results' — the original argument [D] and its superseded "only massive levels" step
