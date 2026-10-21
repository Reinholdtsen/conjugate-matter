---
title: "Coset and hyperbolic sigma models"
weight: 10
status: established
description: "Fields valued in homogeneous spaces; why an indefinite target metric (de Sitter dS₂) means a ghost; and why non-compact hyperbolic models, unlike compact ones, can break symmetry in two dimensions."
provenance: [T]
sources:
  - "papers/reciprocity-toy-models.md §1"
  - "papers/reciprocity-toy-models.md §2"
  - "papers/reciprocity-toy-models.md §4"
  - "papers/reciprocity-toy-models.md ref [15]"
  - "notes/toy-lagrangian.md 'Chunk 1 results'"
  - "notes/toy-lagrangian.md 'Assessment against the predictions'"
  - "review/round4/referee/audit-notes.md Step 1"
  - "review/round4/referee/audit-notes.md Step 3"
  - "review/round4-adjudication.md 'Rulings'"
  - "verify/toy_coset.py"
---

*A sigma model is a field theory whose field takes values, at each point of spacetime, in a curved target space such as a sphere or a hyperbolic plane, with an energy cost when neighbouring points take distant values. In a coset sigma model the target is a group divided by a subgroup, so the group acts on the target as a symmetry, and with no potential every constant field is a lowest-energy state. Two results from this literature shape [model I](/wiki/symmetry-breaking/toy-models/coset-model): the target's metric must be positive, or the kinetic term contains a ghost (a mode of negative energy); and in two dimensions a compact continuous symmetry cannot break spontaneously, while non-compact hyperbolic models are an exception.*

**Status:** Established — literature [T]; the hyperbolic-model citations were retrieved [S] in the worklog's prior-art survey and checked against the sources in round 4, which corrected an author's initial (A. Duncan) and added an erratum.

## Key facts

- **Model I as a coset model.** The worklog calls model I "a coset model of Sp(2,R) → Z₂". Its metric field H takes values in "Sp(2)/U(1) (the upper half-plane, H = H(Z), Z = X + iY)" (`verify/toy_coset.py`; [the Siegel domain](/wiki/phase-space/modular-field/siegel-domain)), and its real structure K in the one-sheeted hyperboloid a² + bc = 1.
- **An indefinite target means a ghost.** K's target "is the one-sheeted hyperboloid a² + bc = 1, which is two-dimensional de Sitter space", and "K's own target space (de Sitter dS₂) has an indefinite metric, which would give a ghost." The naive kinetic term is indefinite on it, "2 db dc at K₀ = diag(1, −1)"; model I contracts K's kinetic term with H, which makes it positive definite ([action and symmetries](/wiki/symmetry-breaking/toy-models/coset-model/action-and-symmetries)).
- **No compact continuous breaking in two dimensions.** "Continuous compact symmetries cannot break spontaneously in two dimensions [13, 14]", the theorems of Mermin and Wagner and of Coleman ([the Mermin–Wagner–Coleman theorem](/wiki/symmetry-breaking/mermin-wagner-coleman)).
- **The hyperbolic exception.** "Non-compact hyperbolic models are an exception [15]": Niedermaier–Seiler, and Duncan–Niedermaier–Seiler, whose abstract states that the SO(1,N) symmetry is spontaneously broken and that for D = 2 "this shows that the systems evade the Mermin-Wagner theorem" (quoted in the round-4 audit notes). The worklog's summary: "SO(1,N) broken in D ≥ 2, evading Mermin–Wagner."
- **Model I's metric sector is such a model.** The round-4 referee identified model I's H-sector as "the SO(1,2)/SO(2) hyperbolic sigma model". The adjudication upheld this as a literature point and restricted the Mermin–Wagner statement to the compact SO(2) containing ρ ([the open SO(2) question](/wiki/symmetry-breaking/toy-models/coset-model/so2-question)).
- **The worklog's framing.** Before construction the worklog listed "a claimed exception for non-amenable groups, to be checked"; its assessment records the non-amenability route as "not needed, not tested".
- **Born sigma models.** Marotta and Szabo's Born sigma models treat the polarization as target structure and choose it "by gauging" (version 2, §1), rather than as a dynamical (H, K) field; the referee found no prior coset model of Born geometry with an order parameter.

## Used by

- [Model I: action and symmetries](/wiki/symmetry-breaking/toy-models/coset-model/action-and-symmetries) — a coset sigma model of (H, K) whose K kinetic term is contracted with H to avoid the dS₂ ghost.
- [Model I vacua, the order parameter and the Goldstone spectrum](/wiki/symmetry-breaking/toy-models/coset-model/vacua) — the vacuum manifold, the half-plane of metrics times a circle of real structures.
- [The frozen-H reduction](/wiki/symmetry-breaking/toy-models/coset-model/frozen-h-reduction) — at H = 1, a two-dimensional spin model of one angle.
- [Open: does ρ's SO(2) break in the coupled model?](/wiki/symmetry-breaking/toy-models/coset-model/so2-question) — the hyperbolic H-sector keeps the compact-symmetry theorem from settling the full model.

## Sources

- `papers/reciprocity-toy-models.md` §1, §2, §4, ref [15] — the literature statements and their use in model I
- `verify/toy_coset.py` — the target spaces of H and K, as the script defines them
- `review/round4-adjudication.md` 'Rulings' — "Mermin–Wagner vs [11]", upheld (literature); the citation corrections
- `review/round4/referee/audit-notes.md` Step 1, Step 3 — the abstract quotation, the H-sector identification, the novelty search
- `notes/toy-lagrangian.md` 'Chunk 1 results', 'Assessment against the predictions' — the citations, retrieved [S]; the dS₂ ghost; the non-amenability framing
