---
title: "The 't Hooft–Polyakov monopole"
weight: 20
status: established
description: "The topological monopole of SU(2) → U(1) breaking (π₂(S²) = ℤ; none for a mirror Standard Model, whose π₂ vanishes) and its mass M = 4πf v/g_d, with f = 1 in the Bogomolny–Prasad–Sommerfield limit rising to about 1.79."
provenance: [T]
sources:
  - "notes/knot-dark-matter-standalone.md §2"
  - "notes/knot-dark-matter-standalone.md §3"
  - "notes/knot-dark-matter-standalone.md refs [15]–[16]"
  - "review/round3/referee/audit-notes.md Step 1"
  - "review/round3/referee/audit-notes.md Step 2"
  - "review/round3/referee/step2b_inf.out (L = 30, 40, 60)"
  - "review/round3/referee/step2a.out 'MONOPOLE MASS RELATION'"
  - "verify/soliton_obituary.py (docstring)"
  - "papers/broken-born-checkpoint-v2.md §12"
---

*The 't Hooft–Polyakov monopole is a stable, particle-like configuration of fields in a gauge theory whose SU(2) symmetry is broken to U(1) by a Higgs field in the adjoint representation; far from its core it looks like a magnetic monopole of the surviving U(1). It cannot decay, because its Higgs field winds once around the space of possible vacua, a sphere, and no smooth change can undo the winding. Its mass is the symmetry-breaking scale v times 4π/g_d, times a factor f between 1 and about 1.79 set by the strength of the Higgs field's self-interaction. In the program it was the object of the withdrawn manuscript #14, which proposed superheavy monopoles of this kind as dark matter; that proposal is retired, and the physics on this page is textbook.*

**Status:** Established — [T] — textbook physics, cited in the withdrawn [#14](/wiki/dark-matter/candidates/soliton-candidate) without provenance tags as [15] ('t Hooft 1974; Polyakov 1974) and [16] (Prasad–Sommerfield 1975; Bogomolny 1976). [The round-3 audit](/wiki/method/review/round-3/rulings) found that both references resolve and support their use, except that the value f ≈ 1.79 is not in [16]; the referee confirmed that value by solving the field equations itself (`review/round3/referee/step2b_inf.out`). The use of this monopole as dark matter is dead ([Obituary: superheavy conjugate solitons](/wiki/dark-matter/candidates/soliton-candidate/obituary)).

## Key facts

- **Topology** (#14 §3): "SU(2)_d -> U(1)_d has pi_2(SU(2)/U(1)) = pi_2(S^2) = Z and supports 't Hooft-Polyakov monopoles [15], stable by topological charge." In the checkpoint's notation, π₂(SU(2)/U(1)) = π₂(S²) = ℤ.
- **None in a mirror Standard Model** (#14 §2): "An exact mirror copy of the Standard Model cannot serve: the electroweak vacuum manifold is S^3, whose pi_2 vanishes, so it has no stable monopoles. The hidden gauge structure must therefore differ from ours." That is, π₂(S³) = 0.
- **The field content** (#14 §2): an adjoint scalar Φ whose expectation value v breaks SU(2) to U(1); "U(1)_d stays unbroken, so the hidden photon is massless. The charged vectors W'+- have mass g_d v." As a program proposal this sector is dead ([Obituary: the hidden SU(2) → U(1) proposal](/wiki/dark-matter/candidates/soliton-candidate/hidden-sector)).
- **Mass** (#14 §3): "Their mass is M = 4 pi f v/g_d." The factor f is 1 in the Bogomolny–Prasad–Sommerfield limit [16] and "rises to about 1.79 at large scalar self-coupling."

```text
M = 4π f v / g_d
f = 1      Bogomolny–Prasad–Sommerfield limit (vanishing scalar self-coupling)
f ≈ 1.79   large scalar self-coupling
```

- **The factor f, checked** (round-3 audit, Step 2). The referee's own boundary-value solver, checked against the Bogomolny–Prasad–Sommerfield energy E = 1, gave f = 1.7867 at infinite self-coupling and marked #14's "~1.79" as confirmed; the audit called the range from 1 to 1.79 the correct physical range. The solver output reads "f_inf=1.7857" at L = 30, 40 and 60 (`review/round3/referee/step2b_inf.out`); `review/round3/referee/step2a.py` adds 10⁻³ for the innermost interval to reach 1.7867. Step 1 notes that the 1.79 value is not in [16] and has no citation. `verify/soliton_obituary.py` takes f = 1 to 1.787 ([the soliton-obituary script](/wiki/method/verification/soliton-obituary-script)).
- **'t Hooft's estimate** (round-3 audit, Step 1, on [15]): the audit summarizes the abstract as giving a "monopole mass of order 137 M_W", where M_W is the mass of the charged vector boson.
- **How #14 used it.** Under its coupling hypothesis H, the relation became "M ~ (21-37) v" (#14 §3), which the referee reproduced as M = (20.7 – 37.1) v (`review/round3/referee/step2a.out`). Hypothesis H and the benchmark mass died with the candidate ([Obituary: the coupling α_d ≈ 34](/wiki/dark-matter/candidates/soliton-candidate/alpha-d-coupling); [overproduction at the benchmark](/wiki/dark-matter/candidates/soliton-candidate/overproduction)). #11 §12 names the candidate "superheavy 't Hooft–Polyakov monopoles of a hidden SU(2) → U(1) sector".
- **References** (#14 [15]–[16]): G. 't Hooft, Nucl. Phys. B 79, 276 (1974); A. M. Polyakov (1974); M. K. Prasad, C. M. Sommerfield, Phys. Rev. Lett. 35, 760 (1975); E. B. Bogomolny, Sov. J. Nucl. Phys. 24, 449 (1976).

## Used by

- [Obituary: the hidden SU(2) → U(1) proposal](/wiki/dark-matter/candidates/soliton-candidate/hidden-sector) — the hidden sector whose monopoles were the candidate.
- [Overproduction at the benchmark](/wiki/dark-matter/candidates/soliton-candidate/overproduction) — the mass relation enters the closing mass M\*.
- [Obituary: superheavy conjugate solitons](/wiki/dark-matter/candidates/soliton-candidate/obituary) — the candidate itself.
- [The soliton-obituary script](/wiki/method/verification/soliton-obituary-script) — the model input f = 1 to 1.787.

## Sources

- `notes/knot-dark-matter-standalone.md` §2, §3, refs [15]–[16] — the topology, the mirror-Standard-Model obstruction, the mass relation and the references (withdrawn manuscript; the textbook statements are not what failed).
- `review/round3/referee/audit-notes.md` Step 1, Step 2 — the citation check, and the confirmation of f.
- `review/round3/referee/step2b_inf.out`, `review/round3/referee/step2a.out` — the solver's f and the reproduced mass relation.
- `verify/soliton_obituary.py` — the range f = 1 to 1.787 used in the gate.
- `papers/broken-born-checkpoint-v2.md` §12 — the candidate named as 't Hooft–Polyakov monopoles.
