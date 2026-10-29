---
title: "The Fierz–Pauli mass term and the Boulware–Deser ghost"
weight: 20
status: established
description: "The unique healthy linear mass term for spin-2, why its weight is special, the ghost that generic nonlinear completions revive, and how the program's metric-built potential misses the Fierz–Pauli weight (battery test T4); the signature obstruction, which keeps its kinetic term gauge-invariant, in summary."
provenance: [T]
sources:
  - "notes/x-classification.md §2"
  - "notes/x-classification.md §3"
  - "notes/tuning-test.md §1"
  - "notes/tuning-test.md §2"
  - "notes/tuning-test.md §3"
  - "notes/tuning-test.md §5"
  - "notes/beta-coefficients.md §3"
  - "papers/broken-born-checkpoint-v2.md §2"
  - "papers/broken-born-checkpoint-v2.md §7.1"
  - "papers/broken-born-checkpoint-v2.md §7.2"
  - "papers/broken-born-checkpoint-v2.md §7.5"
  - "verify/battery.py T4"
  - "HANDOFF.md §2"
  - "HANDOFF.md §5"
  - "notes/broken-born-theory.md 'Addendum (v0.4)'"
  - "notes/broken-born-theory.md 'Addendum (v0.5)'"
  - "review/wiki-build-flags.md items 4, 5, 36"
  - "review/wiki-build-checks/s_expansion.out"
---

*The Fierz–Pauli mass term is the only mass term that gives a free spin-2 field a mass without a [ghost](/wiki/gravity/spin-2-fields/ghosts), a mode whose energy has the wrong sign. In matrix notation it is proportional to Tr(h²) − (Tr h)², where h is the field; any other relative weight of the two terms lets an extra mode propagate, and that mode is a ghost. When the theory is made nonlinear, a generic completion brings the extra mode back, the Boulware–Deser ghost, and keeping it out takes the special [de Rham–Gabadadze–Tolley (dRGT)](/wiki/gravity/spin-2-fields/drgt-massive-gravity) and [Hassan–Rosen](/wiki/gravity/spin-2-fields/hassan-rosen-bimetric) potentials. A related standard fact, [the signature obstruction](/wiki/gravity/spin-2-fields/signature-obstruction), says that a ghost-free two-derivative kinetic term for a symmetric tensor field must have the gauge symmetry of the massless graviton; the Fierz–Pauli theory keeps that kinetic term and breaks the symmetry only through its mass term. The program uses all three facts to decide what its second field, the [momentum graviton X](/wiki/gravity/momentum-graviton), can be. Its [tuning test](/wiki/gravity/tuning-test) checks X's mass term against the Fierz–Pauli form, and the version built from metrics fails that check.*

**Status:** Established — [T] — textbook massive-gravity theory, with the signature obstruction tagged "[T — standard]" in [#6](/wiki/history/documents/field-equation-notes) §2. The program's documents cite no source for the Fierz–Pauli term or the Boulware–Deser ghost; the references below are added from model memory (†). The program's comparison of its own mass term with the Fierz–Pauli form is machine-checked as battery test T4 [V], which passes in the current [gate run](/wiki/method/verification/the-gate) ([the verification battery](/wiki/method/verification/battery)).

## A mass for a spin-2 field [T]

The starting point is the free massless graviton of [general relativity](/wiki/gravity/spin-2-fields/general-relativity): a symmetric tensor field h_μν on flat spacetime, with the two-derivative Lagrangian L_kin[h] obtained by expanding the Einstein–Hilbert action to second order. L_kin is invariant under the linearized diffeomorphisms δh_μν = ∂_μξ_ν + ∂_νξ_μ, and that gauge symmetry is what keeps the theory free of ghosts.

A mass term is a term quadratic in h with no derivatives. Lorentz invariance allows only the scalars h_μν h^μν and h², where h = h^μ_μ is the trace. Treating h as a matrix (one index raised with the flat metric), these are Tr(h²) and (Tr h)². A general mass term is a combination of them with some relative weight. Any such term breaks the gauge symmetry, because it changes when a pure-gauge perturbation ∂_μξ_ν + ∂_νξ_μ is added to h.

## The Fierz–Pauli weight [T]

Fierz and Pauli (1939†) wrote down the Lagrangian of a free massive spin-2 field. Its mass term has one particular relative weight, and with any other weight the field carries a ghost (van Nieuwenhuizen 1973†):

```text
L_FP = L_kin[h] + L_mass,        L_mass ∝ −m² (h_μν h^μν − h²) = −m² (Tr(h²) − (Tr h)²)
```

**What the weight does.** With this weight, taking the divergence and then the trace of the source-free field equations yields the constraints ∂^μ h_μν = 0 and h = 0. The field is then transverse and traceless, and each component obeys the massive wave equation, the Klein–Gordon equation with mass m. What propagates is a massive spin-2 particle with five polarizations, the count calc note #6 §3 gives for X: "a **massive spin-2** with its five polarizations".

**Why only this weight.** The mechanism shows up in the time components. In h_μν h^μν and in h², the term quadratic in h₀₀ appears with the same coefficient, so with the Fierz–Pauli weight it cancels, and h₀₀ enters the action only linearly. A field that appears linearly and without time derivatives is a Lagrange multiplier: its equation is a constraint, and that constraint removes the extra mode a symmetric tensor would otherwise carry. With any other weight h₀₀ appears quadratically, the constraint is lost, and the extra mode propagates. It is a scalar with a wrong-sign kinetic term.

**What a ghost does.** A field whose kinetic term has the wrong sign carries negative energy. Coupled to ordinary fields, it leaves the energy unbounded below: the vacuum can decay by producing ghosts together with ordinary particles, and energy conservation does not stop it. In the quantum theory the choice is between negative-energy states and negative-norm states, an unstable vacuum or a loss of unitarity. A theory with a ghost coupled to ordinary matter is not considered physical.

## The signature obstruction

The Fierz–Pauli construction keeps the gauge-invariant kinetic term L_kin even though its mass term breaks the gauge symmetry. The reason is [the signature obstruction](/wiki/gravity/spin-2-fields/signature-obstruction), tagged "[T — standard]" in calc note #6 §2 and named in calc note #7 §5: without the gauge invariance, no two-derivative kinetic term for a Lorentz-covariant symmetric tensor is free of ghosts, because in Lorentzian signature the mixed time–space components h₀ᵢ enter with the wrong sign. L_kin contains no time derivatives of h₀₀ and h₀ᵢ, which are constrained rather than propagated ([general relativity and the graviton](/wiki/gravity/spin-2-fields/general-relativity#linearized-gravity-and-the-graviton-t)), and the Fierz–Pauli weight keeps h₀₀ a Lagrange multiplier when the mass term is added. The [checkpoint](/wiki/history/documents/checkpoint) states the program's use as "ungauged X by Lorentz signature" (#11 §7.1). Calc note #6 §3 adds that the chain beneath that use was derived for positive-definite metrics; its extension to spacetime signature is open ([Lorentzian dressing (OP3)](/wiki/phase-space/born-geometry/lorentzian-dressing)).

## Beyond quadratic order: the Boulware–Deser ghost [T]

The Fierz–Pauli term fixes a massive spin-2 theory only to quadratic order in h. Coupling the field to gravity, or giving it self-interactions, requires a nonlinear potential: a function of the full metric g_μν and a second, reference metric f_μν (a fixed background in massive gravity, a dynamical field in bimetric gravity) whose expansion about g = f begins with the Fierz–Pauli term. Boulware and Deser (1972†) showed that a generic completion of this kind propagates the extra mode after all, beyond quadratic order, and that the mode is a ghost: the Boulware–Deser ghost.

In the Hamiltonian formulation the mechanism is the one described above, at full nonlinear order [T]. In general relativity the lapse, which carries g₀₀, appears linearly and enforces the Hamiltonian constraint. A generic potential makes the lapse appear nonlinearly; the constraint disappears, and with it the condition that removed the extra mode. The linear constraint from h₀₀ in the Fierz–Pauli theory is the quadratic-order form of that Hamiltonian constraint. In the literature the name Boulware–Deser ghost usually refers to the extra mode as it reappears beyond quadratic order; at quadratic order the same extra mode is what any non-Fierz–Pauli weight lets propagate, and the program's notes use the name for both.

Avoiding the ghost at every order takes a special family of potentials, for which the constraint survives: [dRGT massive gravity](/wiki/gravity/spin-2-fields/drgt-massive-gravity) for one dynamical metric and [Hassan–Rosen bimetric gravity](/wiki/gravity/spin-2-fields/hassan-rosen-bimetric) for two. Calc note #6 §3 summarizes: "Massive spin-2 coupled to gravity has exactly one known consistent structure: the Fierz–Pauli tuning at quadratic order completed by a dRGT/Hassan–Rosen-class potential [T: HR 2011]", and "a generic potential reintroduces the Boulware–Deser ghost".

## Frame variables [T]

In the vielbein, or frame, formulation the ghost-free potentials are polynomials in two frames, and the Fierz–Pauli weight comes out of them without being imposed. Calc note #7 §3 calls these potentials "ghost-free by construction, Fierz–Pauli automatic, dRGT structure inherited rather than tuned" ([the vielbein formulation and wedge potentials](/wiki/gravity/spin-2-fields/vielbein-formulation)).

## How the program uses it

### The ungauged option is closed

X = Re Z is a symmetric tensor with its own gauge symmetry, the [dual diffeomorphisms](/wiki/gravity/momentum-graviton/dual-diffeomorphisms) δX_μν = ∂₍μλ_ν₎ (#6 §2). Two routes would avoid giving it a mass, and both are closed (#11 §7.1, [D + T]): "Massless X is excluded by the multi-graviton no-go [8†]; ungauged X by Lorentz signature." The second exclusion is [the signature obstruction](/wiki/gravity/spin-2-fields/signature-obstruction); the first is [the multi-graviton no-go theorem](/wiki/gravity/spin-2-fields/multi-graviton-no-go). What remains is a mass that respects the Fierz–Pauli structure, generated when the vacuum's choice of [polarization](/wiki/phase-space/reciprocity/lagrangian-polarizations) breaks the dual diffeomorphisms ([why X must be massive](/wiki/gravity/momentum-graviton/forcing-chain); [the gravitational Higgs mechanism](/wiki/gravity/momentum-graviton/gravitational-higgs)). The [lab notebook](/wiki/history/documents/lab-notebook)'s addendum v0.4 states the same pair: massless X "excluded by the multi-graviton no-go", and "the ghost-free no-gauge option is excluded by Lorentz signature".

### The metric tier misses the Fierz–Pauli weight

The [tuning test](/wiki/gravity/tuning-test) asks whether the potential that gives X its mass lands in the ghost-free family "or in the generic Boulware–Deser-ghost family" (#7 §1). Its object is the [misalignment potential](/wiki/gravity/tuning-test/misalignment-potential), built from the anticommutator {J₀, I[Z]} = [[S, A], [A, S]] with S = Y + XY⁻¹X − Y⁻¹ and A = [X, Y⁻¹], in the vacuum frame where the metric Y = Im Z of the [modular field](/wiki/phase-space/modular-field/modular-field-z) is the identity, on the Euclidean skeleton (#7 §2).

Calc note #7 §2 expands it about the vacuum [D — rigorous]: "With Y = 1 + h, X = x: S = 2h + x² + O(3), A = [h, x] + O(3). Any potential of the class Tr({J,I}²)-with-positive-norm gives, at quadratic order, m²Tr(h²) — a graviton mass **without** the −(Tr h)² companion. That violates Fierz–Pauli already at linear order: Boulware–Deser ghost, immediately." Flag 4 in `review/wiki-build-flags.md` records a suspected missing −h² term in this expansion of S, found by executed checks of two agents (`review/wiki-build-checks/s_expansion.py`), and notes that the quadratic-order test, battery test T4, is unaffected, because it uses only the leading term 2h. A second natural invariant, built from [J, I] + 2K, gives X a mass "as Tr(x²) with no trace subtraction. Same disease." #7's conclusion: "Every metric-tier (second-order, H-coupled) misalignment invariant tested lands off the tuning", a "theorem-grade negative". The [handoff](/wiki/history/documents/handoff) records the first failure with its machine-check mark ✓ (HANDOFF §2); the second invariant has no battery test, so its tag stays [D]. See [the metric tier fails twice](/wiki/gravity/tuning-test/metric-tier-failures).

### Battery test T4 [V]

T4 checks the first failure numerically. With the generator seeded at 0 and d = 4, `verify/battery.py` draws one random symmetric h and x, sets Y = 1 + εh and X = εx, computes S, and compares Tr(S²)/ε² with two forms: 4Tr(h²), and the Fierz–Pauli structure with the same normalization, 4(Tr(h²) − (Tr h)²). The normalization follows from the expansion: S begins with 2εh, the 2h of #7's expansion scaled by ε, so Tr(S²)/ε² tends to 4Tr(h²). The current gate run prints:

```text
      T4 eps=0.0001: 66.5772 vs 4Tr(h^2)=66.5770 vs FP=63.7221
      T4 eps=1e-05: 66.5770 vs 4Tr(h^2)=66.5770 vs FP=63.7221
PASS  T4 Tr(S^2)/eps^2 -> 4Tr(h^2) (rel 1e-5 at eps=1e-5)
PASS  T4 limit differs from Fierz-Pauli form (rel > 1%)
PASS  T4 parity: 66.58 vs 63.72 as quoted  [66.58 vs 63.72]
```

The limit is 4Tr(h²) = 66.5770, against the Fierz–Pauli form 63.7221. The checkpoint describes the test as "the linearized potential (Tr(S²)/ε² → 4Tr(h²) to six digits, visibly ≠ the Fierz–Pauli form)" (#11 §2) and quotes it in §7.2 as "the 66.58-vs-63.72 test of §2". Those figures are not in #11 §2, and the script's docstring repeats the pointer to §2; they are in the handoff, "66.58 vs 63.72 at seed 0" (HANDOFF §5), and in the script's output, whose parity check confirms that the environment still reproduces them ([conflicts between sources](/wiki/history/documents/source-conflicts); see flag 36 in `review/wiki-build-flags.md`).

The figures belong to one seeded random h; another draw gives other numbers. What T4 confirms is the arithmetic of the expansion. That the metric-tier potential is the right object to test, and that missing the trace term means a ghost, rest on #7's derivation and on the literature ([verification checks arithmetic, not the model](/wiki/method/verification/arithmetic-not-model)).

### The frame tier, and X's mass

Built from frames instead of metrics, the misalignment potential is a wedge polynomial of the symplectic vielbein E (H = EᵀE) and the polarization frame E₀[J]. That is the Hinterbichler–Rosen class, "ghost-free by construction, Fierz–Pauli automatic" (#7 §3) — a structural claim [D — structural, resting on T] with no machine check ([the frame tier](/wiki/gravity/tuning-test/frame-tier)). The verdict (#7 §3; #1 'Addendum (v0.5)') is that the theory fails in metric variables and passes in frame variables ([the verdict: a conditional pass](/wiki/gravity/tuning-test/conditional-pass)).

X's mass is then the Fierz–Pauli mass of the passing potential. Calc note #8 §3 [D + T] writes it after [reciprocity](/wiki/phase-space/reciprocity/born-reciprocity) has constrained the coefficients ([the palindrome βₙ = β₄₋ₙ](/wiki/gravity/palindromic-branch/palindrome)): "the Fierz–Pauli mass combination m_FP² ∝ β₁ + 2β₂ + β₃ = 2(β₁+β₂), i.e. **M_X**". The checkpoint writes "M_X ∝ 2(β₁+β₂)" [D] (#11 §7.5): #8 states the proportionality for the squared mass, #11 for M_X, and flag 5 in `review/wiki-build-flags.md` suspects that #11 means M_X², a question of notation only. No battery test covers it ([spectrum, parameters and reciprocity parity](/wiki/gravity/momentum-graviton/spectrum-and-parity)).

The lab notebook's v0.1 text had claimed a different route to ghost freedom, "no second independent metric", which addendum v0.4 reversed; that superseded argument is recorded with [the v0.1 action](/wiki/gravity/tuning-test/geometric-action).

## References

The program's documents cite no source for the Fierz–Pauli term, the Boulware–Deser ghost or the signature obstruction. Added by the wiki from model memory (†):

- M. Fierz, W. Pauli (1939)†: the mass term for free fields of spin 2 and higher.
- D. G. Boulware, S. Deser (1972)†: the ghost of generic nonlinear massive gravity.
- P. van Nieuwenhuizen (1973)†: ghost-free quadratic Lagrangians for a symmetric tensor.
- K. Hinterbichler, "Theoretical aspects of massive gravity," Rev. Mod. Phys. (2012)†; C. de Rham, "Massive gravity," Living Rev. Relativ. (2014)†: reviews.

## Used by

- [Why X must be massive](/wiki/gravity/momentum-graviton/forcing-chain) — the Fierz–Pauli structure is what the exclusions of a massless and an ungauged X leave; a generic potential reintroduces the Boulware–Deser ghost.
- [The gravitational Higgs mechanism](/wiki/gravity/momentum-graviton/gravitational-higgs) — the mass X acquires must have the Fierz–Pauli structure.
- [The misalignment potential](/wiki/gravity/tuning-test/misalignment-potential) — the potential tested against the Fierz–Pauli form.
- [The metric tier fails twice](/wiki/gravity/tuning-test/metric-tier-failures) — the missing Fierz–Pauli trace term (T4).
- [The frame tier: the symplectic vielbein](/wiki/gravity/tuning-test/frame-tier) — the Fierz–Pauli structure comes out automatically.
- [The verdict: a conditional pass](/wiki/gravity/tuning-test/conditional-pass) — the Boulware–Deser ghost in metric variables, none in frame variables.
- [Open: deriving the wedge sector from S_H (OP1)](/wiki/gravity/tuning-test/wedge-reduction) — the potential to be derived must lie in the ghost-free structure.
- [Spectrum, parameters and reciprocity parity](/wiki/gravity/momentum-graviton/spectrum-and-parity) — M_X as the Fierz–Pauli mass combination.
- [The geometric action S_H and the v0.1 action (superseded)](/wiki/gravity/tuning-test/geometric-action) — the v0.1 argument that no Boulware–Deser ghost arises.
- [Original P2: both structures rigid (superseded)](/wiki/program/postulates/original-p2) — P2's promise of no Boulware–Deser ghost.
- [Open: Lorentzian dressing of the Euclidean skeleton (OP3)](/wiki/phase-space/born-geometry/lorentzian-dressing) — the regime where the gauge and mass structure is the only path to health.
- [The verification battery T1–T7](/wiki/method/verification/battery) — test T4.

## Sources

- `notes/x-classification.md` §2, §3 — the signature obstruction; the five polarizations; the one known consistent structure and the Boulware–Deser criterion; the Lorentzian caveat.
- `notes/tuning-test.md` §1, §2, §3, §5 — the test's question; the missing trace term and the second invariant; Fierz–Pauli automatic in frame variables; the name "signature obstruction".
- `papers/broken-born-checkpoint-v2.md` §2, §7.1, §7.2, §7.5 — the T4 description; the exclusion of an ungauged X; the metric-tier failure and the "66.58-vs-63.72" pointer to §2, where the numbers do not appear; M_X.
- `verify/battery.py` T4 — the printed comparison, 66.5770 against 63.7221, and the parity check.
- `HANDOFF.md` §2, §5 — the failure marked ✓; "66.58 vs 63.72 at seed 0".
- `notes/beta-coefficients.md` §3 — the Fierz–Pauli mass combination after the palindrome.
- `notes/broken-born-theory.md` 'Addendum (v0.4)', 'Addendum (v0.5)' — the two exclusions; the tuning test's verdict as first recorded.
- `review/wiki-build-flags.md` item 4 — the suspected missing −h² in #7's expansion of S; item 5 — M_X versus M_X²; item 36 — where the figures 66.58 and 63.72 are printed. All await Paul's ruling.
- `review/wiki-build-checks/s_expansion.py` and `review/wiki-build-checks/s_expansion.out` — the expansion of S checked to second order.
