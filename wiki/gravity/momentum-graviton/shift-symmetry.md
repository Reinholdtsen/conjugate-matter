---
title: "Shift symmetry: X is never auxiliary"
weight: 10
status: alive
description: "The rigid Sp(2d, ℝ) contains Z → Z + B, so constant shifts of X are exact symmetries: geometry gives X no potential, and it propagates or it does not exist."
provenance: [D]
sources:
  - "notes/debt1a-ii-X-classification.md §1"
  - "notes/debt1a-ii-X-classification.md §2"
  - "notes/debt1a-ii-X-classification.md §3"
  - "notes/debt1a-ii-X-classification.md §4"
  - "papers/broken-born-checkpoint-v2.md §7.1"
  - "papers/broken-born-checkpoint-v2.md §4"
  - "papers/broken-born-checkpoint-v2.md §6"
  - "papers/broken-born-checkpoint-v2.md §14 item 1"
  - "notes/debt1a-geometric-core.md §C"
  - "notes/debt1a-geometric-core.md §D"
  - "notes/debt1a-geometric-core.md §E"
  - "notes/debt1a-geometric-core.md §F"
  - "notes/debt1a-iii-tuning-test.md §1"
  - "notes/broken-born-theory.md §3"
  - "notes/broken-born-theory.md 'Addendum (v0.3, overnight)'"
  - "notes/broken-born-theory.md 'Addendum (v0.4)'"
  - "notes/broken-born-program-v1.md §5"
  - "HANDOFF.md §2"
  - "verify/battery.py T2"
---

*The shift symmetry is the statement that adding a constant symmetric matrix B to the momentum graviton X leaves every geometric action of the program unchanged. X is the real part of the [modular field](/wiki/phase-space/modular-field/modular-field-z) Z = X + iY, and the shift Z → Z + B is one of the maps of the group Sp(2d, ℝ) that preserves the rigid [symplectic form](/wiki/phase-space/reciprocity/symplectic-form) ω. Any geometric action built from ω and the phase-space metric H therefore takes the same value before and after the shift. Such an action cannot give X a potential energy, a mass, or any coupling without derivatives: X is axion-like, a field that enters only through how it varies from place to place. That rules out one of the three outcomes the program had defined for X, an auxiliary field with no motion of its own: X either propagates or does not exist. The calc note that found the result rates it rigorous; it is the first step of the argument that X must be a massive spin-2 field, and no script checks it.*

**Status:** Alive — [D — rigorous] in calc note #6 (`notes/debt1a-ii-X-classification.md` §1); step (i) of [checkpoint #11](/wiki/history/documents/checkpoint) §7.1's chain, which is tagged [D + T] as a whole — a symmetry argument, not machine-checked: none of the seven tests of [the verification battery](/wiki/method/verification/battery) covers it.

## The statement

Calc note #6 ([the Debt-1 calc notes](/wiki/history/documents/debt-1-notes)), in its section headed "The shift symmetry [D — rigorous]":

> The Möbius action of the rigid Sp(2d,ℝ) contains the subgroup [[1, B], [0, 1]], B symmetric, acting as

```text
Z → Z + B:    X → X + B,    Y → Y.
```

> Constant shifts of X are **exact symmetries** of any S_H built from (ω, H). Consequences: X has no potential and no non-derivative couplings from the geometric sector alone — it is axion-like — and "auxiliary X" (the soft outcome 2) is off the table at the fundamental level: X appears only through derivatives, so it propagates or it doesn't exist.

The checkpoint keeps it as the first step of the chain that makes X massive (#11 §7.1): "(i) The rigid Sp(2d,ℝ) contains Z → Z + B (B symmetric): X is shift-symmetric — axion-like, never auxiliary."

## What is being shifted

Under the corrected postulate [P2′](/wiki/program/postulates/p2-prime), only ω is rigid: "Only ω is rigid (symplectic rigidity ≡ constancy of ℏ)" [P] (#11 §4). The positive phase-space metrics H compatible with ω alone then form [the Siegel domain](/wiki/phase-space/modular-field/siegel-domain) Sp(2d, ℝ)/U(d), whose points are complex symmetric matrices Z = X + iY with Y positive definite. Calc note #5 writes the metric belonging to each point as (§C)

```text
H_Z = [[ Y + XY⁻¹X ,  XY⁻¹ ],
       [ Y⁻¹X      ,  Y⁻¹  ]]
```

The program reads Y = Im Z as the spacetime metric g and X = Re Z as a new symmetric tensor field, the momentum graviton (#11 §6, tagged [D]; [the modular field Z = X + iY](/wiki/phase-space/modular-field/modular-field-z)). At X = 0 the metric is diag(Y, Y⁻¹), with no blocks that mix position and momentum directions; X ≠ 0 mixes them. The vacuum sits on that slice: "The vacuum ⟨Z⟩ = i·g sits at X = 0" (#6 §3).

A shift by a constant B changes X at every point by the same symmetric matrix and leaves Y, the metric, unchanged.

## Why the shift is a symmetry

### The group of the rigid structure [T]

The linear maps of phase space that preserve ω form the symplectic group Sp(2d, ℝ). A symplectic matrix written in d × d blocks, S = [[A, B], [C, D]], moves points of the Siegel domain by the matrix form of a fractional-linear map [T] (Siegel 1943 †):

```text
Z → (A Z + B)(C Z + D)⁻¹
```

With A = D = 1 and C = 0 the map is Z → Z + B, and a matrix [[1, B], [0, 1]] is symplectic exactly when B is symmetric [T]. Those are the translations #6 §1 names. In the convention in which a symplectic map acts on a metric by congruence, H → SᵀHS, the same shift comes from the transposed matrix [[1, 0], [B, 1]], the shear that adds Bx to each momentum and leaves the position unchanged [T]; the Siegel-domain page sets out the two conventions. Either way the shift is a symplectic map: it leaves ω exactly as it was.

### From a symmetry of ω to a symmetry of the action

"Rigid" means that ω is the same fixed structure in every configuration of the fields. An action built from ω and H alone takes the same value on a configuration and on its image under a map that preserves ω [T], and the shift is such a map. #6 states this step in one line: constant shifts are "exact symmetries of any S_H built from (ω, H)".

S_H is the program's geometric action, the dynamics of the metric H ([the geometric action S_H](/wiki/gravity/tuning-test/geometric-action)). The [lab notebook](/wiki/history/documents/lab-notebook) wrote it as an Einstein-like curvature action, "S_H = ½M_B² ∫_Σ √|H| R_B[H] over the section Σ, with ω, η frozen (P2)" (#1 §3), under [the original postulate](/wiki/program/postulates/original-p2) that froze the neutral metric η as well. No document writes S_H out with ω alone rigid, and its first-principles relation to the potential that gives X its mass is open item 1 of #11 §14 ([Open: deriving the wedge sector from S_H (OP1)](/wiki/gravity/tuning-test/wedge-reduction)). The symmetry argument does not need an explicit form: it constrains every action built from ω and H at once.

### What a shift symmetry forbids [T]

If an action is unchanged by X → X + B for every constant B, no term in it can depend on the value of X itself. Derivatives are unaffected, since ∂(X + B) = ∂X, so X can appear only through its derivatives [T]. In Fourier terms, a constant shift adds only to the zero-wavenumber component of X, and every term built from derivatives weights each component by its wavenumber, so that component drops out. The elastic energy of a solid behaves the same way: it depends on how the displacement varies from point to point, not on a uniform displacement of the whole body.

Three kinds of term are therefore excluded from the geometric action: a potential V(X), which includes a mass term; self-interactions of X without derivatives; and couplings of X to other fields without derivatives. A field with this property is called axion-like, after the axion of particle physics, whose shift symmetry a → a + c keeps it light [T]. This is the content of "X has no potential and no non-derivative couplings from the geometric sector alone — it is axion-like".

## What it rules out: an auxiliary X

### The outcome it removes

Calc note #5 had posed the question of what X is as a choice among three outcomes. The computation it defined to decide between them was to "expand the generalized curvature scalar of (ω, H_Z) to quadratic order in X about X = 0 on the section, with ω-generalized diffeomorphisms as the gauge symmetry, and classify X as one of" (#5 §D):

1. "**healthy propagating** → dynamical momentum-space gravity (Born's dream, linearized)";
2. "**auxiliary** (no derivatives at quadratic order) → integrate out → a *contact, momentum-structured* four-χ operator, i.e. the gate delivered directly";
3. "**ghost** → fatal to the geometric sector."

An auxiliary field, in the standard sense [T], is one that enters the action without derivatives. Its field equation is then algebraic rather than a wave equation: it can be solved for the field and substituted back, which is what integrating the field out means, and this leaves contact interactions among the fields it couples to and no particle of its own. Outcome 2 would have made X such a field, with the four-χ contact operator acting between particles χ of [conjugate matter](/wiki/dark-matter/conjugate-matter), one of the program's two dark-matter candidates.

### Why the shift excludes it

An auxiliary X would enter the action at quadratic order through terms with no derivatives of X, and the shift symmetry forbids every such term. If X appears in the geometric action at all, it appears through its derivatives, and then it carries a kinetic term and propagates: "X appears only through derivatives, so it propagates or it doesn't exist" (#6 §1). The note calls outcome 2 "the soft outcome" and removes it "at the fundamental level". The other two outcomes were settled by the rest of the chain, set out on [why X must be massive](/wiki/gravity/momentum-graviton/forcing-chain).

### What replaced the auxiliary route to the gate

Outcome 2 would have delivered the [velocity gate](/wiki/dark-matter/conjugate-matter/velocity-gate), the dependence of dark matter's self-interaction on relative momentum, directly as a contact operator, and #5 counted it the cheapest route to the gate's shape: "outcome 2 gives it most cheaply" (§E). With the outcome excluded, the contact operator comes instead from exchange of a massive, propagating X: "Integrating out massive X between χ bilinears gives the contact four-χ operator" (#6 §4; [the gate mechanism](/wiki/dark-matter/conjugate-matter/gate-mechanism)). Exchange of a heavy propagating field looks like a contact interaction at distances longer than its range, that is, at momentum transfers small compared with its mass [T]; an auxiliary X would have given the contact interaction exactly.

## What it implies for the mass

A mass term for X is a term without derivatives, so the exact shift symmetry forbids it in the geometric action. #6 §3: "The mass cannot be written by hand (shift symmetry) — but it doesn't need to be."

The qualifier "from the geometric sector alone" matters here. The tuning-test note places the mass outside the action built from ω and H: "The X mass must come from the η-selection (Higgs) sector: a misalignment potential penalizing incompatibility between the polarization J and the modular field Z" (#7 §1; [the misalignment potential](/wiki/gravity/tuning-test/misalignment-potential)). J, the real structure that the vacuum chooses spontaneously (η = HJ, #11 §4), is not fixed by ω and H. The vacuum breaks the symmetry: "The vacuum ⟨Z⟩ = i·g sits at X = 0 and is *moved* by the shifts" (#6 §3), and the local version of the shifts is broken spontaneously when the vacuum selects its polarization. That is [the gravitational Higgs mechanism](/wiki/gravity/momentum-graviton/gravitational-higgs).

## The local version

The constant shift is a global symmetry: the same B everywhere. Calc note #6 §2 next replaces B by the symmetrized derivative of a vector field λ_μ(x) that varies from point to point, δX_μν = ∂₍μλ_ν₎. A constant shift is the special case of a λ_μ that grows linearly with position, whose symmetrized derivative is constant [T]. Because X is symmetric, the local shifts have the same form as the linearized coordinate changes of [general relativity](/wiki/gravity/spin-2-fields/general-relativity), and X becomes a second graviton-like gauge field: [dual diffeomorphisms: a second graviton](/wiki/gravity/momentum-graviton/dual-diffeomorphisms).

## Scope and caveats

- **Level of rigor.** Of the three steps of calc note #6's chain this is the one marked rigorous; the gauge structure and no-go step is [D + T] and the mass mechanism [D — structural] (#6 §2, §3). The v1 paper tags the step [D] (#9 §5 item 1), and #11 §7.1 folds it into a chain tagged [D + T].
- **Not machine-checked.** Battery test T2 checks the Siegel parametrization H_Z (I[Z]² = −1, symmetry, positivity, det H_Z = 1) at one sampled point ([the Siegel domain](/wiki/phase-space/modular-field/siegel-domain)); no test checks the shift or its consequences.
- **The geometric sector only.** The result constrains the action built from ω and H. It says nothing against a potential for X from the η-selection sector, and that sector is where the mass comes from.
- **Positive metrics.** The Siegel parametrization assumes positive H, and #6 calls its §1–§3 "the Euclidean-rigorous skeleton" (§3). The extension to the Lorentzian signature of spacetime is open item 3 ([Open: Lorentzian dressing of the Euclidean skeleton (OP3)](/wiki/phase-space/born-geometry/lorentzian-dressing)).

## History

- **The question.** Calc note #5 defined the three outcomes and called the curvature expansion "the single most important remaining calculation" (§D), the first item "Now precisely open" (§F). The lab notebook's v0.3 addendum restated it as "the quadratic-order classification of X (healthy / auxiliary / ghost), where the first two outcomes serve the program and only the third kills the geometric sector" ([the lab notebook](/wiki/history/documents/lab-notebook)).
- **The answer.** Calc note #6 §1 removed the auxiliary outcome by symmetry; the curvature expansion itself is reported in no document. The notebook's v0.4 addendum: "The rigid Sp(2d,ℝ) shift symmetry Z → Z + B makes X axion-like (no potential from geometry; "auxiliary" is off the table)."
- **The papers.** #9 §5 item 1: "**Shift symmetry [D].** The rigid Sp(2d,ℝ) contains Z → Z + B (B symmetric): X is axion-like — no potential from geometry, "auxiliary" excluded." #11 §7.1 (i) is the current statement, and [the handoff](/wiki/history/documents/handoff)'s summary reads "shift symmetry ⇒ never auxiliary" (`HANDOFF.md` §2).

## Sources

- `notes/debt1a-ii-X-classification.md` §1 — the shift and its consequences [D — rigorous]; §2 — the local version; §3 — the vacuum at X = 0, "The mass cannot be written by hand", the Euclidean-rigorous skeleton; §4 — the gate from integrating out massive X.
- `papers/broken-born-checkpoint-v2.md` §7.1 — the current statement, step (i) of the chain [D + T]; §4 — P2′; §6 — Im Z = g and Re Z = X; §14 item 1 — the open derivation from S_H.
- `notes/debt1a-geometric-core.md` §C — the Siegel domain and H_Z; §D — the three outcomes; §E — "outcome 2 gives it most cheaply"; §F — the classification as the next computation.
- `notes/debt1a-iii-tuning-test.md` §1 — the mass from the η-selection (Higgs) sector.
- `notes/broken-born-theory.md` §3 — the v0.1 form of S_H; 'Addendum (v0.3, overnight)' and 'Addendum (v0.4)' — the question and its answer in the lab notebook.
- `notes/broken-born-program-v1.md` §5 — the v1 statement, tagged [D].
- `HANDOFF.md` §2 — the handoff's summary of the chain.
- `verify/battery.py` T2 — the Siegel parametrization at one sampled point.
