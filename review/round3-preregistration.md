# Round 3 — pre-registration

Written and committed **before** the round-3 audit was dispatched, so the
prediction cannot be fitted to the outcome. Rounds 1 and 2 were pre-registered
the same way and scored 2 for 2 on verdicts (HANDOFF §6).

- **Manuscript under review:** `papers/knot-dark-matter-standalone.md` v3, as
  of commit 5dbaa82.
- **Auditor:** a fresh subagent with shell, Python (numpy/sympy/scipy) and
  web search. It gets only a copy of the manuscript and the protocol below,
  with no repo, worklog or handoff context.
- **Limitation, stated up front:** the auditor is the same model family as
  the author. It removes the arithmetic failure mode of rounds 1–2, which had
  no code execution. It does not remove correlated blind spots.

## Protocol (HANDOFF §6, round 3)

1. Verify every citation against INSPIRE, arXiv or the publisher, including
   that each one supports what it is cited for.
2. Re-check every number in Secs. 2–4 in Python from independently chosen
   constants.
3. Re-derive the compatibility theorem independently, symbolically (sympy)
   and with random numerical tests.
4. Conceptual audit: internal consistency, omitted constraints (by literature
   search), and the kinetic-mixing claims.
5. Verdict A/B/C with a confidence, four lists (verified / failed /
   unverifiable / omitted constraints), and the single weakest link.

## Predictions

- **Verdict: B** ("flawed but salvageable"), confidence medium.
  - It is not A: the toy action (acceptance criterion 1) does not exist,
    and two of v3's own exclusion tests (the millicharged ψ window and the
    strong-coupling relic) are stated but not evaluated.
  - It is not C: v3 removes v2's known internal contradictions (§2 vs §3
    coupling; the ε·g premise; the "Kibble-only" window).
- **Weakest link: the framework does no work.**
  - The candidate in §2–§4 is a standard hidden-sector monopole model.
  - Nothing numerical depends on Born reciprocity, the compatibility
    theorem or the polarization identification. Hypothesis H's motivation
    ("the minimal action is to equate the elementary charges") is one
    sentence.
  - Expect the auditor to say the dark-matter proposal stands or falls
    independently of the phase-space framework.
- **Runner-up weakest links**, in order:
  1. The unevaluated millicharge bounds on ψ at ε ~ 10⁻⁷–10⁻⁶,
     MeV–0.1 TeV. They might already exclude part of the window.
  2. Thermal-history consistency. The W′ and ψ freeze-out are computed at
     ξ = 1, but dark radiation requires ξ < 0.77, and Kibble production with
     a colder hidden sector is treated only by the ξ^(3/4) scaling.
  3. The strong-coupling annihilation at α_m ≈ 34 (criterion 3).
- **Arithmetic:** zero surviving numerical indictments. Every number was
  computed by `verify/knot_numbers.py`. If one does land, the most likely
  place is the order-of-magnitude freeze-out or ΔN_eff estimates, where the
  inputs (κ, g*, f) are bracketed rather than derived.
- **Citations:** all 23 resolve. The likeliest problems are the two not
  live-checked (Kolb & Turner; Hiramatsu et al.'s journal reference), or a
  reference cited for slightly more than it says, such as [5] on
  heavy-spin-2 stability or [11] on global symmetries.
