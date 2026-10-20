# Round 4 — pre-registration

Written and committed **before** the round-4 audit is dispatched. Per the
round-3 lesson, the commit subject does not state the prediction.

- **Manuscript:** `papers/reciprocity-toy-models.md` (the toy-Lagrangian
  note), as committed with this file.
- **Auditor:** a fresh subagent with shell, Python (numpy/sympy/scipy) and
  web. It gets only a copy of the manuscript, no repo context, and the same
  five-step protocol as round 3: citations, numbers, an independent
  re-derivation, a conceptual audit, and a verdict with four lists.
- **Limitation:** same model family as the author.

## Predictions

- **Verdict: B** (flawed but salvageable), confidence medium.
  - It is not C: every number was computed by gated code with independent
    anchors, and the claims are narrowly scoped, with limitations stated.
  - It is not A: the significance is thin, and at least one argument is
    explicitly incomplete.
- **Weakest link: in 1+1, the "spontaneous" breaking of ρ rests on an
  explicit, rigid background.** The ρ-preserving potential needs a fixed
  unordered pair of axes K_ref. A referee can reasonably call model I's
  1+1 result an ordinary Z₂ breaking of an explicitly chosen axis pair.
  Model I without it is a coset construction by definition.
- **Runner-up weakest links**, in order:
  1. Model II's quantum-restoration argument. The tunnelling step is argued,
     not proven, and a referee may raise large-N matrix-model transitions or
     noncommutative nonlocality as ways around "nothing couples β across
     space".
  2. The real-versus-complex distinction. Grosse–Wulkenhaar call the real
     model invariant, and a referee may read their alternating convention
     as a symmetry of the real model after all.
  3. The weak form of matter locality is close to true by construction.
- **Arithmetic:** at most one surviving numerical indictment. The likeliest
  places are a normalization or convention: the spin-wave exponent, the
  8π(m+n+1) coefficient, or the Δ sign convention, which I reversed once
  myself while drafting.
- **Citations:** all 12 resolve. The likeliest "cited for more than it says"
  is [12] (José et al.) for the Ising-like ordered phase of the two-fold
  anisotropic planar model.
