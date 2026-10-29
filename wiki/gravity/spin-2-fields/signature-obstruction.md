---
title: "The signature obstruction"
weight: 25
status: established
description: "Without the gauge symmetry of the massless graviton, no two-derivative kinetic term for a symmetric tensor field in spacetime is free of ghosts, because the mixed time–space components enter with the wrong sign; how the gauge-invariant kinetic term escapes, why this leaves the Fierz–Pauli structure for a massive field, and how the program uses it to exclude an ungauged X."
provenance: [T]
sources:
  - "papers/broken-born-checkpoint-v2.md §7.1"
  - "papers/broken-born-checkpoint-v2.md §1"
  - "papers/broken-born-checkpoint-v2.md §2"
  - "papers/broken-born-checkpoint-v2.md §14 item 3"
  - "papers/broken-born-checkpoint-v2.md §15"
  - "notes/x-classification.md §2"
  - "notes/x-classification.md §3"
  - "notes/tuning-test.md §5"
  - "HANDOFF.md §2"
  - "HANDOFF.md §3"
  - "notes/broken-born-theory.md 'Addendum (v0.4)'"
  - "notes/broken-born-program-v1.md §0"
  - "notes/broken-born-program-v1.md §5"
  - "notes/broken-born-program-v1.md §11"
  - "notes/knot-dark-matter-standalone.md §1"
  - "review/wiki-build-flags.md item 44"
---

*The signature obstruction is the standard result that a symmetric tensor field in spacetime, such as the perturbation h_μν of the metric, has no [ghost-free](/wiki/gravity/spin-2-fields/ghosts) kinetic term with two derivatives unless that kinetic term has the gauge symmetry of the massless graviton. A ghost is a mode whose energy has the wrong sign. The obstruction comes from the signature of spacetime, in which time enters with the opposite sign to space: in a contraction such as h_μν h^μν the components h₀ᵢ, with one time index and one space index, enter with the opposite sign to the others, and in the simplest kinetic term built from such contractions that sign becomes the sign of their kinetic energy. The gauge symmetry avoids the problem by keeping those components from propagating: the kinetic term of linearized [general relativity](/wiki/gravity/spin-2-fields/general-relativity) contains no time derivatives of h₀₀ and h₀ᵢ, which are constrained rather than propagated. The [Fierz–Pauli](/wiki/gravity/spin-2-fields/fierz-pauli) theory of a massive spin-2 field keeps that kinetic term and breaks the symmetry only through its mass term. The program uses the result to close one option for its second symmetric tensor, the [momentum graviton X](/wiki/gravity/momentum-graviton): without its gauge symmetry X would carry a ghost, and with the symmetry unbroken X would be a second massless graviton interacting with the metric, which [the multi-graviton no-go theorem](/wiki/gravity/spin-2-fields/multi-graviton-no-go) excludes, so X must have a mass. [Calc note #6](/wiki/history/documents/field-equation-notes) tags the statement as standard literature without citing a source, and no script checks it.*

**Status:** Established — [T — standard], the tag of calc note #6 §2, which cites no source. The explanation on this page is written from general knowledge [T], and the references it adds are from model memory (†). No `verify/` script checks the statement. The program applies it to X in a chain tagged [D + T] in [checkpoint #11](/wiki/history/documents/checkpoint) §7.1, and no test of [the verification battery](/wiki/method/verification/battery) covers that chain.

## The statement

Calc note #6 §2 states it and tags it as standard literature:

> Without the gauge invariance, no ghost-free two-derivative kinetic term for a Lorentz-covariant symmetric tensor exists (mixed time–space components enter with the wrong sign under any invariant contraction; this is why the Fierz–Pauli structure and its accidental gauge symmetry exist at all). [T — standard]

Its terms [T]:

- **A Lorentz-covariant symmetric tensor** is a field h_μν = h_νμ whose components mix under Lorentz transformations as the components of the metric do. Its components are h₀₀, whose indices are both time indices; the mixed components h₀ᵢ, with one time index and one space index; and the spatial components hᵢⱼ.
- **A two-derivative kinetic term** is a part of the Lagrangian that is quadratic in the field and built from its first derivatives. It is the standard form for a field that propagates as a wave, and its terms in time derivatives are the field's kinetic energy.
- **Ghost-free** means that no propagating mode has negative kinetic energy. A ghost coupled to ordinary fields leaves the energy unbounded below; the consequences are set out with [the Fierz–Pauli weight](/wiki/gravity/spin-2-fields/fierz-pauli#the-fierzpauli-weight-t).
- **The gauge invariance** is the symmetry of the massless graviton, the linearized diffeomorphisms δh_μν = ∂_μξ_ν + ∂_νξ_μ, with ξ_μ an arbitrary vector field ([linearized gravity and the graviton](/wiki/gravity/spin-2-fields/general-relativity#linearized-gravity-and-the-graviton-t)).

The name "signature obstruction" is calc note #7's (§5). Checkpoint #11 counts "a signature obstruction" among the structural results of its technical abstract (§1) and states the program's use of it in one clause: "ungauged X by Lorentz signature" (§7.1).

## Where the wrong sign comes from [T]

**Signature.** The metric of flat spacetime, the Minkowski metric η_μν, gives the time direction the opposite sign to the space directions. (This is the textbook symbol, unrelated to the program's neutral metric η on phase space; see [the structures ω, η, H](/wiki/phase-space/born-geometry/born-structures).) Indices are raised with its inverse η^μν, which is diagonal with the same pattern of signs.

**In a contraction.** Raising both indices of a component of h_μν multiplies it by two diagonal entries of η^μν. For h₀₀ and for hᵢⱼ the two factors have the same sign; for the mixed components h₀ᵢ they have opposite signs. In either sign convention for the metric, therefore,

```text
h_μν h^μν = h₀₀h₀₀ − Σᵢ (h₀ᵢh₀ᵢ + hᵢ₀hᵢ₀) + Σᵢⱼ hᵢⱼhᵢⱼ
```

with the sums running over the space indices; hᵢ₀ and h₀ᵢ are the same component, since the tensor is symmetric.

**In a kinetic term.** The simplest two-derivative kinetic term contracts the first derivatives of the field in the same way, ∂_λh_μν ∂^λh^μν. Its part in time derivatives has the same pattern of signs, applied to the time derivatives ∂₀h_μν: those of the mixed components enter with the opposite sign to those of h₀₀ and hᵢⱼ. If the overall sign is chosen so that the spatial components hᵢⱼ carry positive kinetic energy, the mixed components carry negative kinetic energy: they are ghosts. This is the sign that #6's parenthesis refers to.

## How the gauge-invariant kinetic term escapes it [T]

**The other contractions.** Up to total derivatives, every Lorentz-invariant term that is quadratic in h_μν and has two derivatives is a combination of

```text
L_kin = c₁ ∂_λh_μν ∂^λh^μν + c₂ ∂_μh^μλ ∂^νh_νλ + c₃ ∂_μh^μν ∂_νh + c₄ ∂_λh ∂^λh
```

where h = h^μ_μ is the trace and c₁ to c₄ are constants. The terms built from the divergence ∂_μh^μν and from the trace also contain time derivatives of h₀ᵢ and h₀₀, so with suitable coefficients they can cancel the wrong-sign terms of the first.

**The gauge-invariant combination.** Expanding the [Einstein–Hilbert action](/wiki/gravity/spin-2-fields/general-relativity#the-einsteinhilbert-action-and-the-field-equations-t) of general relativity to second order gives one such combination. It is invariant under δh_μν = ∂_μξ_ν + ∂_νξ_μ, and up to normalization and total derivatives it is the only combination that is. In it the cancellation is complete: once total derivatives are dropped, it contains no time derivatives of h₀₀ or h₀ᵢ at all. Components that appear without time derivatives do not propagate. Their field equations are constraints, conditions that the other components must satisfy at each instant, and h₀₀ appears only linearly, as a Lagrange multiplier. In the full theory these are the constraints of general relativity carried by the lapse and the shift, the parts of the metric that h₀₀ and h₀ᵢ perturb. The gauge symmetry and the constraints leave only the transverse, traceless components to propagate, which carry the graviton's helicity ±2.

**Without the gauge symmetry.** #6's statement is that no other choice of the coefficients is free of ghosts: unless the gauge symmetry keeps them from propagating, some modes of the field carry negative kinetic energy. The classification of the quadratic Lagrangians of a symmetric tensor by whether they are ghost-free is due to van Nieuwenhuizen (1973†); the program's documents give no reference.

**The same sign in a vector field.** The vector potential A_μ of electromagnetism shows the mechanism with one index. In A_μA^μ the time component A₀ enters with the opposite sign to the space components, and a kinetic term built only from ∂_μA_ν ∂^μA^ν would give A₀ negative kinetic energy. Maxwell's kinetic term, proportional to F_μνF^μν with F_μν = ∂_μA_ν − ∂_νA_μ, is invariant under A_μ → A_μ + ∂_μα and contains no time derivative of A₀, because F₀ᵢ = ∂₀Aᵢ − ∂ᵢA₀. The field equation of A₀ is Gauss's law, a constraint. A mass term proportional to A_μA^μ, as in the Proca theory of a massive vector field, breaks the gauge symmetry but contains no derivatives, so A₀ still does not propagate: its equation fixes it in terms of the other components. The Fierz–Pauli theory has the same structure for spin 2.

## What it leaves: the Fierz–Pauli structure [T]

The obstruction concerns the kinetic term. By the obstruction, a symmetric tensor that propagates without a ghost keeps the gauge-invariant kinetic term, so a mass, which breaks the gauge symmetry, has to enter through a term without derivatives. The Fierz–Pauli theory does this. Its Lagrangian is the gauge-invariant kinetic term plus a mass term proportional to h_μν h^μν − h² (Fierz and Pauli 1939†). The mass term contains no time derivatives, so h₀₀ and h₀ᵢ still do not propagate. The h₀ᵢ appear in it squared and without derivatives, and their own equations fix them. With the Fierz–Pauli weight the terms quadratic in h₀₀ cancel between h_μν h^μν and h², so h₀₀ still appears only linearly, and its constraint removes the extra mode that a massive symmetric tensor would otherwise carry, a ghost ([the Fierz–Pauli weight](/wiki/gravity/spin-2-fields/fierz-pauli#the-fierzpauli-weight-t)). What propagates is a massive spin-2 particle with five polarizations, the count calc note #6 §3 gives for X.

#6 reads the obstruction this way in its parenthesis: "this is why the Fierz–Pauli structure and its accidental gauge symmetry exist at all". In this wiki's reading, the gauge symmetry meant is that of the Fierz–Pauli kinetic term, which the mass term breaks.

Beyond quadratic order a further question arises. A generic nonlinear completion of the Fierz–Pauli term brings the extra mode back, the [Boulware–Deser ghost](/wiki/gravity/spin-2-fields/fierz-pauli#beyond-quadratic-order-the-boulwaredeser-ghost-t), and the known potentials that keep it out are those of [de Rham–Gabadadze–Tolley massive gravity](/wiki/gravity/spin-2-fields/drgt-massive-gravity) and [Hassan–Rosen bimetric gravity](/wiki/gravity/spin-2-fields/hassan-rosen-bimetric).

## What it assumes [T]

The statement has the scope its wording gives it:

- **A free field.** It concerns the quadratic part of the action of one symmetric tensor on flat spacetime. Interactions and nonlinear completions raise separate questions: for one massive field, the Boulware–Deser ghost above; for several massless fields, the multi-graviton no-go theorem.
- **Lorentz covariance.** The kinetic term is built from contractions with the spacetime metric, which is where the signs come from.
- **Two derivatives.** Kinetic terms with more derivatives lie outside the statement.
- **Lorentzian signature.** The sign that causes the obstruction is that of time relative to space, which gives the obstruction its name; #11 §7.1 words the exclusion as "by Lorentz signature".
- **The full gauge symmetry against none.** The statement contrasts a kinetic term with the gauge symmetry and one without it. A kinetic term with part of the symmetry is a separate case in the literature: one invariant only under the transverse diffeomorphisms, those with ∂^μξ_μ = 0, and under the Weyl rescalings δh_μν = φη_μν, with φ an arbitrary function, is also free of ghosts and propagates the same two helicity states as linearized general relativity. It is the linearized form of unimodular gravity, the version of general relativity in which the determinant of the spacetime metric is held fixed (van der Bij, van Dam and Ng 1982†; Álvarez, Blas, Garriga and Verdaguer 2006†). No program document discusses this case. Flag 44 in `review/wiki-build-flags.md` (minor, not yet audited) notes that on this reading #6's "the gauge invariance" overstates: the smaller symmetry is still a gauge symmetry, so the conclusion that X must be gauged is unaffected.

## How the program uses it

### Excluding an ungauged X

X = Re Z is the real part of [the modular field](/wiki/phase-space/modular-field/modular-field-z) Z = X + iY, whose imaginary part Y is the spacetime metric g. X is a symmetric tensor, and its local shifts, the [dual diffeomorphisms](/wiki/gravity/momentum-graviton/dual-diffeomorphisms) δX_μν = ∂₍μλ_ν₎, have the form of the graviton's gauge symmetry: "a *second copy of linearized diffeomorphisms*" (#6 §2). #6 §2 then takes the two cases, without that gauge invariance and with it, introducing them as "Two consistency facts then close the door on the massless option". The first is the statement quoted above. The second is the multi-graviton no-go:

> With the gauge invariance, X is a second **massless** spin-2 — and massless multi-graviton cross-interactions are inconsistent (Boulanger–Damour–Gualtieri–Henneaux). X must couple (to g through the Siegel structure, to χ through the gate), so decoupling is not available. [T]

Its conclusion: "**Therefore X must be massive.**" #11 states the pair inside its chain, tagged [D + T]: "Massless X is excluded by the multi-graviton no-go [8†]; ungauged X by Lorentz signature" (§7.1). The [lab notebook](/wiki/history/documents/lab-notebook)'s addendum v0.4 words the second exclusion as "the ghost-free no-gauge option is excluded by Lorentz signature".

In this wiki's reading, an ungauged X is an X whose kinetic term lacks the dual-diffeomorphism invariance; by the obstruction, such an X would carry a ghost. What remains is the structure of the previous sections: a kinetic term with the gauge symmetry, and a mass that breaks it. The program cannot write that mass into the action, because constant shifts of X are exact symmetries ([shift symmetry](/wiki/gravity/momentum-graviton/shift-symmetry)): "The mass cannot be written by hand (shift symmetry) — but it doesn't need to be" (#6 §3). It comes from the vacuum's choice of [polarization](/wiki/phase-space/reciprocity/lagrangian-polarizations), which breaks the dual diffeomorphisms spontaneously, and X becomes "a **massive spin-2** with its five polarizations" (#6 §3; [the gravitational Higgs mechanism](/wiki/gravity/momentum-graviton/gravitational-higgs)). The whole chain is set out on [why X must be massive](/wiki/gravity/momentum-graviton/forcing-chain).

### Tags and checks

- **The obstruction** is literature, tagged [T — standard] in #6 §2, with no reference in any program document.
- **Its application to X** is a step of the chain tagged [D + T] in #11 §7.1 (the gauge structure and the no-go, [D + T], in #6 §2). #11 §2 counts the exclusions of §7.1 among its negative results, in Tier 3 of its [claim tiers](/wiki/method/claim-tiers#negative-results-the-most-reliable-tier-3-items), the tier of novel structural physics.
- **No machine check.** No battery test checks a step of the chain. The [handoff](/wiki/history/documents/handoff) lists "X is forced massive" among the results that stand without the ✓ it gives machine-verified items (`HANDOFF.md` §2).

### Where the documents state it

- **Calc note #6 §2**: the statement, tagged [T — standard], quoted above.
- **The lab notebook, addendum v0.4**: "the ghost-free no-gauge option is excluded by Lorentz signature".
- **Calc note #7 §5**: the name, in its list of "three structural tests in a row (multi-graviton no-go, signature obstruction, tuning test)".
- **The v1 paper, #9** (superseded as reference; [the checkpoint](/wiki/history/documents/checkpoint) covers #9 to #11): "a signature obstruction" in its technical abstract's "chain of structural theorems" (§0), and "Ungauged: excluded by Lorentz signature (wrong-sign mixed components)" (§5 item 2).
- **Checkpoint #11**: "a signature obstruction" in the technical abstract's "chain of structural results" (§1), and "ungauged X by Lorentz signature" (§7.1).
- **The handoff**: its inventory describes #6 with "massless/ungauged excluded" (`HANDOFF.md` §3, artifact 6); its summary of the scientific state names the massless exclusion and not this one (§2).
- **The withdrawn soliton manuscript, #14 §1**: gives the no-go step and the Higgs step, not this one ([the soliton candidate](/wiki/dark-matter/candidates/soliton-candidate)).

### The count of structural tests

Calc note #7 §5, written after [the tuning test](/wiki/gravity/tuning-test), lists the obstruction second of its "three structural tests in a row (multi-graviton no-go, signature obstruction, tuning test)". #11 §15 counts "four consecutive consistency tests" without naming them, and #11's technical abstract includes "a signature obstruction" in its chain (§1). The v1 paper's technical abstract has it in its "chain of structural theorems" (#9 §0), but the v1 assessment's four, "no-go → Higgs → HR class → palindrome" (#9 §11), HR being Hassan–Rosen, do not include it. #11 governs the count. The versions are compared on [Assessment: a live research program](/wiki/program/assessment#forced-convergence-onto-consistency-islands) and [conflicts between sources](/wiki/history/documents/source-conflicts).

## What is open

**The Lorentzian setting of the chain.** The obstruction is a statement about Lorentzian signature, and it is the step at which the program's chain already uses that signature ([where signature already enters](/wiki/phase-space/born-geometry/lorentzian-dressing#where-signature-already-enters)). The geometric results beneath the chain were derived for a positive-definite metric. Calc note #6 §3:

> the compatibility theorem and Siegel parametrization were derived for positive H. Lorentzian g makes the stabilizer U(1, d−1) and the invariant target metric indefinite — which is precisely the regime where the gauge+mass structure above is not a luxury but the only path to health. The chain of §1–§3 is the Euclidean-rigorous skeleton; the Lorentzian dressing rides on the same FP/HR machinery it lands on.

FP is Fierz–Pauli and HR is Hassan–Rosen. In this wiki's reading, the "gauge+mass structure" is the structure described above: a kinetic term with the gauge symmetry, and a mass that breaks it. Carrying [the compatibility theorem](/wiki/phase-space/born-geometry/compatibility-theorem), the parametrization of [the Siegel domain](/wiki/phase-space/modular-field/siegel-domain) and the chain over to spacetime signature is open item 3 of #11 §14, "Lorentzian dressing of the Euclidean-rigorous skeleton [O]" ([Open: Lorentzian dressing of the Euclidean skeleton (OP3)](/wiki/phase-space/born-geometry/lorentzian-dressing); [open problems and the queue](/wiki/status/open-problems)). No document reports or spells out that computation; what it would have to cover is listed on [the OP3 page](/wiki/phase-space/born-geometry/lorentzian-dressing#what-the-extension-would-have-to-cover).

**The citation.** No program document cites a source for the obstruction: #6 tags it as standard, and #11 states its use without a reference. It is therefore not among the † references that [the literature battery (OP10)](/wiki/method/literature-battery) is to check. The references below are the wiki's, from model memory (†).

## References

The program's documents cite no source for the statement. Added by the wiki from model memory (†):

- P. van Nieuwenhuizen, "On ghost-free tensor Lagrangians and linearized gravitation" (1973)†: the ghost-free quadratic Lagrangians of a symmetric tensor.
- M. Fierz, W. Pauli (1939)†: the free massive spin-2 field, whose kinetic term is the gauge-invariant one.
- J. J. van der Bij, H. van Dam, Y. J. Ng, "The exchange of massless spin-two particles," Physica A (1982)†; E. Álvarez, D. Blas, J. Garriga, E. Verdaguer, "Transverse Fierz–Pauli symmetry," Nucl. Phys. B (2006)†: kinetic terms invariant only under the transverse diffeomorphisms, among them the Weyl-invariant one of linearized unimodular gravity.
- K. Hinterbichler, "Theoretical aspects of massive gravity," Rev. Mod. Phys. (2012)†; C. de Rham, "Massive gravity," Living Rev. Relativ. (2014)†: reviews of massive gravity.

## Used by

- [Why X must be massive](/wiki/gravity/momentum-graviton/forcing-chain) — the obstruction excludes an ungauged X.
- [Dual diffeomorphisms: a second graviton](/wiki/gravity/momentum-graviton/dual-diffeomorphisms) — it closes the way out of dropping X's gauge symmetry.
- [The modular field Z = X + iY](/wiki/phase-space/modular-field/modular-field-z) — "no massless or ungauged X", in what X became.
- [Born's answer: momentum space gravitates](/wiki/gravity/momentum-graviton/borns-answer) — one of the steps that leave mass as the only exit.
- [The verdict: a conditional pass](/wiki/gravity/tuning-test/conditional-pass) — the second of calc note #7's three structural tests.
- [Assessment: a live research program](/wiki/program/assessment) — "a signature obstruction" in #11's chain of structural results.
- [Open: Lorentzian dressing of the Euclidean skeleton (OP3)](/wiki/phase-space/born-geometry/lorentzian-dressing) — the step of the chain that already uses Lorentzian signature.

## Sources

- `papers/broken-born-checkpoint-v2.md` §7.1 — "ungauged X by Lorentz signature", in the chain [D + T]; §1 — "a signature obstruction" in the technical abstract; §2 — the exclusions of §7.1 among the Tier-3 negative results; §14 item 3 — the Lorentzian dressing [O]; §15 — "four consecutive consistency tests".
- `notes/x-classification.md` §2 — the statement [T — standard], the second copy of linearized diffeomorphisms, the two facts and "Therefore X must be massive"; §3 — the mass that cannot be written by hand, the five polarizations, and the signature caveat.
- `notes/tuning-test.md` §5 — the name, in the three structural tests.
- `HANDOFF.md` §2 — "X is forced massive", without a ✓ and without this step; §3 — "massless/ungauged excluded" in the inventory entry for #6.
- `notes/broken-born-theory.md` 'Addendum (v0.4)' — "the ghost-free no-gauge option is excluded by Lorentz signature".
- `notes/broken-born-program-v1.md` §0 — "a signature obstruction" in the abstract's chain of structural theorems; §5 — "Ungauged: excluded by Lorentz signature (wrong-sign mixed components)"; §11 — the four tests of v1, without this one (superseded as reference).
- `notes/knot-dark-matter-standalone.md` §1 — the withdrawn manuscript's chain, without this step.
- `review/wiki-build-flags.md` item 44 — #6 §2's "the gauge invariance", read literally, overstates, since the transverse-diffeomorphism and Weyl case is still a gauge symmetry; minor, not yet audited, awaiting Paul's ruling.
