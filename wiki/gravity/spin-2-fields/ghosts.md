---
title: "Ghosts and perturbative instabilities"
weight: 19
status: established
description: "A ghost is a mode whose kinetic term has the wrong sign: negative energy or negative norm, and a vacuum that decays once the mode interacts. How it differs from tachyons, gradient instabilities and strong coupling; how ghost freedom is checked, from constraints and the kinetic matrix to the Hamiltonian constraint; the Higuchi ghost and phantom fields; and the ghosts that bear on the program, from the signature obstruction and the tuning test to model I's de Sitter target."
provenance: [T]
sources:
  - "notes/debt1a-ii-X-classification.md §2"
  - "notes/debt1a-ii-X-classification.md §3"
  - "notes/debt1a-ii-X-classification.md §5"
  - "notes/debt1a-geometric-core.md §D"
  - "notes/debt1a-iii-tuning-test.md §2"
  - "notes/debt1a-iii-tuning-test.md §3"
  - "papers/broken-born-checkpoint-v2.md §7.1"
  - "papers/broken-born-checkpoint-v2.md §7.2"
  - "papers/broken-born-checkpoint-v2.md §10"
  - "papers/broken-born-checkpoint-v2.md §14 item 1"
  - "papers/broken-born-checkpoint-v2.md §14 item 3"
  - "verify/battery.py T4"
  - "verify/battery.py T7"
  - "papers/reciprocity-toy-models.md §2"
  - "papers/reciprocity-toy-models.md §4"
  - "notes/toy-lagrangian.md 'Chunk 1 results'"
  - "verify/toy_coset.py"
  - "review/round4-adjudication.md 'Rulings' F1–F2"
  - "notes/knot-dark-matter-standalone.md §1"
  - "notes/knot-dark-matter-standalone.md ref [6]"
  - "review/round3/referee/audit-notes.md Step 1"
  - "review/v3-worklog.md 'Round-2 pending list'"
  - "notes/broken-born-theory.md §4"
  - "notes/broken-born-theory.md §6"
  - "notes/broken-born-theory.md §7"
  - "notes/broken-born-theory.md 'Addendum (v0.4)'"
  - "notes/broken-born-theory.md 'Addendum (v0.5)'"
  - "CLAUDE.md 'Since the handoff'"
  - "review/wiki-build-flags.md item 25"
  - "notes/closed-universe.md §7"
  - "review/wiki-build-flags.md item 49"
  - "notes/closed-universe.md §6"
  - "review/wiki-build-flags.md item 53"
---

*A ghost is a mode of a field whose kinetic term, the part of its energy that comes from the field's rate of change, has the wrong sign, so that its excitations carry negative energy or, in the quantum theory, negative norm. On its own a ghost oscillates like any other field. Coupled to ordinary fields it leaves the energy with no lower bound, and the vacuum can decay into ghosts and ordinary particles without violating energy conservation, so a theory in which a ghost interacts with ordinary matter is not considered physical. The other instabilities of small perturbations about a solution are different: a tachyon, a mode of negative mass squared, grows at long wavelengths, and a gradient instability, a negative squared propagation speed, grows fastest at short wavelengths. Under strong coupling, which is not an instability, a mode's kinetic term is so small that linear perturbation theory cannot decide its fate. Whether a mode is a ghost is read from the signs of the kinetic terms that remain once constraints have removed the components that do not propagate. Ghost freedom decides what the program's [momentum graviton X](/wiki/gravity/momentum-graviton) can be: it excludes an X without its gauge symmetry, and [the tuning test](/wiki/gravity/tuning-test) asks whether the potential that gives X its mass carries the [Boulware–Deser ghost](/wiki/gravity/spin-2-fields/fierz-pauli#beyond-quadratic-order-the-boulwaredeser-ghost-t) of generic massive gravity. It also fixes the kinetic term of the real structure in [model I](/wiki/symmetry-breaking/toy-models/coset-model), the program's coset toy model, and a ghost field is one route to the [phantom side of the dark-energy divide](/wiki/cosmology/dark-energy/phantom-divide), which the program's dark-energy field, an ordinary scalar, cannot reach.*

**Status:** Established — [T] — textbook field theory, written here from general knowledge, with the literature it names marked †; no `verify/` script checks the general statements. The program's documents use the concept without defining it or citing a general source. Their statements about particular ghosts keep their own tags, given where they are quoted below: [the signature obstruction](/wiki/gravity/spin-2-fields/signature-obstruction) is [T — standard] in [calc note #6](/wiki/history/documents/debt-1-notes) §2; the Boulware–Deser ghost of the metric tier is [D — rigorous] in #7 §2 and [D][V] in [checkpoint #11](/wiki/history/documents/checkpoint) §7.2, checked by battery tests T4 and T7 ([the verification battery](/wiki/method/verification/battery)); the frame tier's ghost freedom is [D — structural, resting on T] in #7 §3, with no machine check; and the positive kinetic term of model I's real structure is checked by `verify/toy_coset.py` in [the gate](/wiki/method/verification/the-gate) ([the toy-model scripts](/wiki/method/verification/toy-model-scripts)).

## What a ghost is [T]

### A kinetic term of the wrong sign

The energy of an ordinary field is a sum of squares with positive coefficients: one from its rate of change in time, one from its variation in space and one from its mass. A ghost has the opposite sign. For a single scalar field, with L the Lagrangian density, E the energy density, a dot a time derivative and ∇ the spatial gradient:

```text
ordinary field:  L =  ½φ̇² − ½(∇φ)² − ½m²φ²       E =   ½φ̇² + ½(∇φ)² + ½m²φ²     ≥ 0
ghost:           L = −½χ̇² + ½(∇χ)² + ½m²χ²       E = −(½χ̇² + ½(∇χ)² + ½m²χ²)    ≤ 0
```

The ghost's Lagrangian is the ordinary one with its overall sign reversed. Reversing the sign of a whole Lagrangian leaves the field equation unchanged, so χ obeys the same wave equation as φ and oscillates at the same frequencies; what changes is the sign of the energy its motion carries. The sign that decides the matter is that of the time-derivative, or kinetic, term. A mode whose kinetic term is negative has an energy with no lower bound, since a large enough rate of change makes it as negative as one likes, whatever the signs of its other terms.

A ghost that interacts with nothing is harmless: its energy is conserved on its own, and the overall sign of an isolated system's energy has no observable effect. Gravity couples to every field, though, so in a theory with gravity a ghost always interacts.

### Why an interacting ghost is fatal

Once the ghost couples to ordinary fields, energy can pass between them. The total is conserved, but the ghost can give up energy without limit while the ordinary fields gain the same amount, so both can grow together, and there is no state of lowest energy. In the quantum theory the empty state can then decay into ghosts and ordinary particles, a process that conserves energy and momentum. If the theory is Lorentz invariant, the rate of that decay diverges, because the products can carry arbitrarily large momenta, and a ghost is tolerable only in an effective theory cut off at a low energy scale (Carroll, Hoffman and Trodden 2003 †; Cline, Jeon and Moore 2004 †).

The ghost can instead be quantized with positive energies. Its states then have negative norm, a negative squared length in the space of quantum states, and probabilities computed with them can be negative, so the theory loses unitarity, the conservation of total probability. The choice is between an unstable vacuum and a loss of unitarity, and either way a theory in which a ghost interacts with ordinary matter is not considered physical ([the Fierz–Pauli mass term and the Boulware–Deser ghost](/wiki/gravity/spin-2-fields/fierz-pauli#the-fierzpauli-weight-t)). Results are stated in whichever form suits the setting; the Higuchi ghost below is described by its negative norm.

### Ghosts from higher time derivatives

A Lagrangian that depends on second or higher time derivatives of a field, in a way that no integration by parts removes, also carries a ghost, unless the dependence is degenerate: the highest derivatives cannot all be solved for from the canonical momenta, and the constraints that result can remove the extra modes. Ostrogradsky showed that without such a degeneracy the energy is linear in one of the canonical momenta and so has no lower bound (Ostrogradsky 1850 †; Woodard 2015 †, a review). In a free theory the extra solutions form a second mode with the opposite sign of kinetic term. A field equation with four time derivatives, (□ + m₁²)(□ + m₂²)φ = 0, describes particles of masses m₁ and m₂, and its propagator splits into two terms of opposite sign:

```text
1/[(k² − m₁²)(k² − m₂²)]  =  [1/(k² − m₁²) − 1/(k² − m₂²)] / (m₁² − m₂²)
```

One of the two particles is a ghost (Pais and Uhlenbeck 1950 †). In the limit of massive gravity that de Rham and Gabadadze studied (2010 †), which isolates the helicity-0 polarization, the Boulware–Deser ghost appears in this form, as interactions with too many derivatives ([dRGT massive gravity](/wiki/gravity/spin-2-fields/drgt-massive-gravity#the-problem-drgt-solves-t)).

## Ghosts, tachyons, gradient instabilities and strong coupling [T]

A solution is tested for stability by writing each field as the solution plus a small fluctuation and expanding the action to second order in the fluctuation. For a single mode χ the quadratic Lagrangian has three coefficients, each set by the background:

```text
L₂ = ½A χ̇² − ½B (∇χ)² − ½C χ²          plane waves:   A ω² = B k² + C
```

A is the kinetic coefficient, B the gradient coefficient and C the mass coefficient; ω is the angular frequency, k the wavenumber, and c² = B/A the squared propagation speed. Their signs sort the possible instabilities, and a vanishing A marks strong coupling.

- **Ghost: A < 0.** The kinetic term has the wrong sign, as above. A ghost need not grow: a free one whose three coefficients all have the reversed sign oscillates. The damage is done through its interactions.
- **Gradient instability: B/A < 0.** The squared speed is negative, so ω² = c²k² + C/A is negative at large k, and the mode grows exponentially at a rate proportional to k: the shorter the wavelength, the faster. In a continuum theory the rate has no upper bound, and the evolution from given initial data is not well defined. The withdrawn manuscript [#14](/wiki/dark-matter/candidates/soliton-candidate) summarizes the published analyses of bimetric cosmological branches as finding "gradient or ghost instabilities" (#14 §1; [what the published analyses found](/wiki/gravity/spin-2-fields/bimetric-cosmology#what-the-published-analyses-found)).
- **Tachyon: C/A < 0, with B/A > 0.** The mode grows only at long wavelengths, k² < −C/B, and no faster than √(−C/A). A negative mass squared means that the background sits at a maximum or a saddle of the potential, and the instability is the field moving away from it, toward a lower state if one exists. It is a property of the background, not a defect of the theory: spontaneous symmetry breaking starts this way, and [hilltop quintessence](/wiki/cosmology/dark-energy/thawing-and-freezing#hilltop-models) is a slow version of it. Gravitational collapse is of the same long-wavelength kind: in a self-gravitating medium, ripples longer than the Jeans length grow ([the Jeans instability](/wiki/dark-matter/momentum-clumping/vlasov-stability#the-static-threshold-and-the-jeans-instability)), and the [round-3](/wiki/method/review/round-3) audit describes one of the bimetric results as an "exponential Jeans-like instability" (`review/round3/referee/audit-notes.md` Step 1). With several fields, C becomes the Hessian of the potential, the mass-squared matrix, and a negative eigenvalue marks a tachyonic direction ([counting with the Hessian](/wiki/symmetry-breaking/goldstone-and-higgs#counting-with-the-hessian)). Whether the theory itself is sick then turns on whether the potential is bounded below.
- **Strong coupling: A → 0.** Rescaling the mode so that its kinetic term has unit coefficient, χ_c = √A χ, multiplies its interaction terms by inverse powers of A, so they grow without limit as A goes to zero, and linear perturbation theory no longer decides what the mode does; the nonlinear theory has to. A kinetic coefficient that changes sign across a family of backgrounds passes through zero, so the boundary between a healthy mode and a ghost is a region of strong coupling. Among the limits of the heavy spin-2 result in bimetric cosmology, the worklog for the third version of the withdrawn manuscript #14 lists that "the strong-coupling era H > H⋆ is unresolved" (`review/v3-worklog.md`, item R7), with H the Hubble rate, not the program's phase-space metric, and H⋆ left undefined ([the heavy spin-2 regime](/wiki/gravity/spin-2-fields/bimetric-cosmology#the-heavy-spin-2-regime)).

## How ghost freedom is checked [T]

### Constraints first

A field with several components often has components that do not propagate, and only those that propagate can be ghosts. A component that enters the action linearly and without time derivatives is a Lagrange multiplier: its field equation is a constraint on the other components rather than an equation of motion, and each constraint, together with any gauge freedom, removes modes. In the Hamiltonian form of [general relativity](/wiki/gravity/spin-2-fields/general-relativity#the-einsteinhilbert-action-and-the-field-equations-t) the lapse and the shift, which carry g₀₀ and g₀ᵢ, play this role. Their constraints remove every component of the metric except the graviton's helicity ±2 polarizations, including components that would otherwise carry negative energy.

The [Fierz–Pauli mass term](/wiki/gravity/spin-2-fields/fierz-pauli) works the same way at quadratic order. Its special relative weight makes h₀₀ enter linearly, so h₀₀ stays a Lagrange multiplier and its constraint removes the extra mode that a symmetric tensor would otherwise carry; with any other weight that mode propagates with a wrong-sign kinetic term. Of the ten components of a symmetric tensor field (#5 §D), what then propagates is, in calc note #6's words, "a **massive spin-2** with its five polarizations" (#6 §3).

### A negative coefficient that is not a ghost

Constraints also explain why a wrong-sign term is not always a ghost. In minisuperspace, general relativity reduced to the scale factor a(t) and the lapse N(t), the gravitational Lagrangian's term in ȧ² has a negative coefficient ([Friedmann cosmology and minisuperspace](/wiki/cosmology/scale-factor-duality/friedmann-cosmology#minisuperspace-gravity-reduced-to-at-and-nt-t)). The scale factor is nevertheless not a ghost. The lapse enforces the Hamiltonian constraint, which fixes the expansion rate from the energy content, so a has no motion of its own to excite. In the Euclidean path integral of quantum gravity the same sign makes the action unbounded below, the conformal-factor problem (Gibbons, Hawking and Perry 1978 †).

### The kinetic matrix

Once the constraints are solved, the time-derivative terms of the remaining variables form a quadratic form, the kinetic matrix: the matrix of second derivatives of the Lagrangian with respect to the rates of change. The theory is free of ghosts about the background in question when the kinetic matrix is positive definite. Each negative eigenvalue is a ghost, and a zero eigenvalue marks a variable with no dynamics of its own, a constraint or an auxiliary field. A change of variables changes the eigenvalues but not how many are negative, by the law of inertia (Sylvester's) that also governs the Hessian of the potential. The two matrices test different things: the kinetic matrix finds ghosts, the Hessian of the potential finds tachyonic directions, and the program's [reduced-model stability rule](/wiki/method/verification/reduced-model-stability) asks for the Hessian with all fields dynamical.

For a sigma model, a field that takes values at each point in a curved target space, the kinetic matrix is the target space's metric, so the model is free of ghosts exactly when that metric is positive definite ([positive target metrics, and the de Sitter ghost](/wiki/symmetry-breaking/toy-models/coset-model/sigma-models#positive-target-metrics-and-the-de-sitter-ghost)). In Euclidean signature an indefinite target metric shows up instead as an action unbounded below.

### Beyond quadratic order: the Hamiltonian constraint

A quadratic expansion tests one background. A nonlinear theory can be free of ghosts about one background and carry one about another, or carry a mode that appears only beyond quadratic order. The general test is the Hamiltonian analysis of Arnowitt, Deser and Misner: write the action in terms of the lapse, the shift and the spatial metric, and count the constraints. In general relativity the lapse appears linearly. A generic potential for a massive graviton makes it appear nonlinearly, the Hamiltonian constraint is lost, and the extra mode returns as the Boulware–Deser ghost (Boulware and Deser 1972 †; [beyond quadratic order](/wiki/gravity/spin-2-fields/fierz-pauli#beyond-quadratic-order-the-boulwaredeser-ghost-t)). For the potentials of [dRGT massive gravity](/wiki/gravity/spin-2-fields/drgt-massive-gravity#the-potential-t) and [Hassan–Rosen bimetric gravity](/wiki/gravity/spin-2-fields/hassan-rosen-bimetric#ghost-freedom-t) the lapse can be made to appear linearly again after a redefinition of the shift; the constraint survives, with a secondary constraint that follows from it, and together they remove the extra mode. In frame variables the same potentials are wedge products of two frames, ghost-free by construction ([vielbein formulation and wedge potentials](/wiki/gravity/spin-2-fields/vielbein-formulation)).

Ghost freedom in this sense removes the extra mode on every background. The kinetic coefficients of the remaining modes still depend on the background, and about particular solutions of a ghost-free theory they can have the wrong sign.

### The Higuchi ghost

The standard example is a massive spin-2 field on [de Sitter space](/wiki/cosmology/dark-energy/de-sitter-space), the spacetime of a universe expanding at a constant Hubble rate H. The field is healthy when its mass m satisfies the Higuchi bound,

```text
m² ≥ 2H²
```

For masses between zero and the bound, its helicity-0 polarization has negative norm: it is a ghost. The manuscript [#14](/wiki/dark-matter/candidates/soliton-candidate), withdrawn after round 3 for an unrelated error, cites the bound as its reference [6], A. Higuchi, Nucl. Phys. B 282, 397 (1987), and the round-3 audit found that the reference supports it (`review/round3/referee/audit-notes.md` Step 1). At the edge, m² = 2H², a gauge symmetry removes the helicity-0 polarization ([partially massless gravity](/wiki/gravity/spin-2-fields/partially-massless-gravity)). A heavy field meets the bound trivially; in #14's words, the bound "is satisfied trivially by the heavy field" (#14 §1). Flag 53 in `review/wiki-build-flags.md` finds that the conclusion holds and the reasoning does not: with a fixed mass the argument fails once 2(H² + k/a²) > M_X², at TeV temperatures for the smallest M_X and during inflation unless M_X > √2·H_inf, while the bound holds through X's dressed mass on the program's branch ([the momentum graviton in a closed universe](/wiki/gravity/momentum-graviton/closed-universe#the-higuchi-bound-holds-through-the-dressed-mass)). The bound and its check are on [bimetric cosmology and its instabilities](/wiki/gravity/spin-2-fields/bimetric-cosmology#the-higuchi-bound).

## Phantom fields [T]

A scalar field with a wrong-sign kinetic term is the simplest model of phantom dark energy, dark energy whose equation of state w, its pressure p divided by its energy density ρ, lies below −1. For a uniform field, ρ + p is twice the kinetic term: φ̇² for an ordinary field, −φ̇² for a ghost. An ordinary scalar therefore keeps w ≥ −1 while its density is positive, and a ghost scalar with positive density has w < −1 whenever it moves (Caldwell 2002 †). Its vacuum decays as described above unless the theory is cut off at a low scale. A ghost is one route to a phantom phase, alone or paired with an ordinary field so that w can cross −1; couplings to curvature, modified gravity and energy exchange in the dark sector are others ([reaching the phantom side](/wiki/cosmology/dark-energy/phantom-divide#reaching-the-phantom-side-t)).

The program's dark-energy field, [τ](/wiki/cosmology/dark-energy/tau-quintessence), is an ordinary scalar. The [lab notebook](/wiki/history/documents/lab-notebook) states the consequence: "**w ≥ −1 always.** τ is a canonical scalar; the null energy condition holds; phantom crossing is impossible. **[D]**" (#1 §7 item 1, transcribed from its LaTeX). The checkpoint keeps "strictly w ≥ −1" in its dark-energy passage, tagged [D + T] (#11 §10; [the no-phantom bound w ≥ −1](/wiki/cosmology/dark-energy/no-phantom-bound)). The second data release of the Dark Energy Spectroscopic Instrument favours a phantom crossing above [redshift](/wiki/cosmology/scale-factor-duality/redshift) z ≈ 0.4, against that bound, and the root `CLAUDE.md` describes the dark-energy sector as "under real pressure" ('Since the handoff'; [DESI DR2's phantom crossing](/wiki/cosmology/dark-energy/desi-dr2-phantom-crossing)).

## Ghosts in the program

### What X can be

Calc note #5 posed the nature of the momentum graviton as a classification with three outcomes, "healthy propagating", "auxiliary" or "ghost", the last "fatal to the geometric sector" (#5 §D). Calc note #6 replaced the question with the answer "*massive spin-2, conditionally healthy*" (#6 §5; [the three-way classification, superseded](/wiki/gravity/momentum-graviton/forcing-chain#superseded-the-three-way-classification-of-x)). Two of its steps are statements about ghosts.

**The signature obstruction.** Calc note #6 §2 states it and tags it as standard literature:

> Without the gauge invariance, no ghost-free two-derivative kinetic term for a Lorentz-covariant symmetric tensor exists (mixed time–space components enter with the wrong sign under any invariant contraction; this is why the Fierz–Pauli structure and its accidental gauge symmetry exist at all). [T — standard]

Read literally, "the gauge invariance" overstates: a smaller gauge symmetry also gives a ghost-free term ([the signature obstruction](/wiki/gravity/spin-2-fields/signature-obstruction); flag 44 in `review/wiki-build-flags.md`, not yet audited).

In this page's terms, without its gauge symmetry the kinetic matrix of a symmetric tensor has negative directions, the mixed components, and only the constraints that come with the gauge symmetry keep them from propagating ([the signature obstruction](/wiki/gravity/spin-2-fields/signature-obstruction)). The checkpoint states the exclusion in one clause, "ungauged X by Lorentz signature" (#11 §7.1, [D + T]). With [the multi-graviton no-go theorem](/wiki/gravity/spin-2-fields/multi-graviton-no-go), which excludes a second massless graviton that interacts, it leaves X a mass as its one option ([why X must be massive](/wiki/gravity/momentum-graviton/forcing-chain)).

**The health criterion.** #6 §3, in a section tagged [D — structural]:

> **X is a massive spin-2 field. The geometric sector is healthy iff the potential generated by the η-selection lands in the Hassan–Rosen class; a generic potential reintroduces the Boulware–Deser ghost.**

Calc note #6 set the stakes before the test: "Fail ⇒ the Boulware–Deser ghost kills the geometric sector" (#6 §5).

### The tuning test

[The tuning test](/wiki/gravity/tuning-test) applied the criterion to the potential that gives X its mass, [the misalignment potential](/wiki/gravity/tuning-test/misalignment-potential). Built from metrics, the potential misses the Fierz–Pauli weight at quadratic order and lies outside the Hassan–Rosen family beyond it, so it carries the Boulware–Deser ghost by either route: "Boulware–Deser ghost, exhibited twice independently" (#1 'Addendum (v0.5)'). Calc note #7 calls this half of the test "a theorem-grade negative" [D — rigorous] (#7 §2); battery test T4 checks the first failure, and T7 the algebraic fact the second rests on [V] (#11 §7.2; [the metric tier fails twice](/wiki/gravity/tuning-test/metric-tier-failures)). Built from frames, the potential is a wedge polynomial of the kind described above, "ghost-free by construction" [D — structural, resting on T] (#7 §3), with no machine check ([the frame tier](/wiki/gravity/tuning-test/frame-tier)). The verdict is [a conditional pass](/wiki/gravity/tuning-test/conditional-pass), the condition being the choice of variables. The passing class was selected rather than derived, and deriving it is item 1 of #11 §14 ([Open: deriving the wedge sector from S_H (OP1)](/wiki/gravity/tuning-test/wedge-reduction)).

### The Lorentzian caveat

The chain of calc note #6 is what #6 §3 calls "the Euclidean-rigorous skeleton", and the tuning test is computed on the same Euclidean skeleton (#7 §2), where the metric is positive definite. There the [target metric](/wiki/phase-space/modular-field/siegel-domain#the-target-metric) of the [modular field Z](/wiki/phase-space/modular-field/modular-field-z) is positive definite, which calc note #5 counted as a good sign for its kinetic term, beside the precedent of [double field theory](/wiki/phase-space/born-geometry/double-field-theory), whose massless sector is free of ghosts (#5 §D). With a Lorentzian metric, #6 §3 records, the invariant target metric becomes "indefinite — which is precisely the regime where the gauge+mass structure above is not a luxury but the only path to health". By the criterion above, an indefinite target metric means a ghost unless something removes its negative directions. The extension to Lorentzian signature is open ([Open: Lorentzian dressing of the Euclidean skeleton (OP3)](/wiki/phase-space/born-geometry/lorentzian-dressing)).

### Model I: the de Sitter target of K

In model I, the program's coset sigma model of a phase-space metric H and a real structure K (here H is the phase-space metric, not a Hubble rate), the obvious kinetic term for K would carry a ghost. Version 2 of the [toy-model note](/wiki/symmetry-breaking/toy-models) places K on a curved target: "Its target is the one-sheeted hyperboloid a² + bc = 1, which is two-dimensional de Sitter space" (§2). The metric that space inherits is indefinite, and the worklog draws the consequence: "K's own target space (de Sitter dS₂) has an indefinite metric, which would give a ghost" (`notes/toy-lagrangian.md`, 'Chunk 1 results'). The note states the remedy: "The K kinetic term is contracted with H and is positive definite. The naive Tr(∂K ∂K) is indefinite on the hyperboloid (2 db dc at K₀ = diag(1, −1))." (§2). The contraction couples the two sectors of the model ([Model I: action and symmetries](/wiki/symmetry-breaking/toy-models/coset-model/action-and-symmetries#the-k-kinetic-term-and-the-ghost)). The metric H itself takes values in the upper half-plane, whose invariant metric is the positive metric of the hyperbolic plane [T], so by the criterion above its kinetic term is healthy as written ([coset and hyperbolic sigma models](/wiki/symmetry-breaking/toy-models/coset-model/sigma-models)). The gate checks both statements about K (`verify/toy_coset.py`):

```text
PASS  the K kinetic term Tr(H^-1 dK^T H dK) is positive for random H and dK (no ghost)
PASS  the naive Tr(dK dK) is indefinite on K's target space (de Sitter): 2 db dc
```

### An unbounded potential is not a ghost

[Round 4](/wiki/method/review/round-4) found a defect of another kind in the first potential added to model I to pin its polarization, −μ[Tr(K K_ref)]². Model I's kinetic terms are positive, so the defect lies in the potential. In the words of the toy-model note, the potential "is unbounded below once H is dynamical", and "The point (1, K_ref) is a saddle" (§4); the round-4 adjudication upheld both findings (F1, F2), and the gate confirms the saddle (`verify/toy_coset.py`). In this page's terms that is a tachyonic direction of a potential with no lower bound, not a ghost. The potential is dead ([Obituary: the naive ρ-preserving potential](/wiki/symmetry-breaking/toy-models/coset-model/naive-potential)). [The bounded potential V_b](/wiki/symmetry-breaking/toy-models/coset-model/bounded-potential) replaced it, and the episode produced [the reduced-model stability rule](/wiki/method/verification/reduced-model-stability).

### The lab notebook's minisuperspace argument

In its first version the lab notebook argued that no Boulware–Deser ghost arises. Under [the original P2](/wiki/program/postulates/original-p2), which froze both the symplectic form ω and the neutral metric η, its paragraph headed "Ghost accounting" reads: "There is no second independent metric: g̃'s cosmological mode is eliminated by the P2 constraint (§7), so no Boulware–Deser sector arises in minisuperspace. **[D]** The statement for full inhomogeneous H is open. **[O]**" (#1 §4; the constraint is derived in §6, see flag 25 in `review/wiki-build-flags.md`). Here g̃ is the momentum-space metric and H the phase-space metric. The minisuperspace calculation of #1 §6 finds the dual gravitational sector "**not** a new fluid and **not** a ghost — ã was never independent" [D]. In this page's terms, [the cosmological constraint a·ã = 1](/wiki/cosmology/scale-factor-duality/cosmological-constraint) ties the momentum-space scale factor ã to a, so, like the scale factor in the example above, it has no motion of its own to excite.

The argument is superseded. Once η became emergent, calc note #6 found X to be a second graviton, which the notebook's v0.4 addendum records as "a *second graviton*", reversing the claim of "no second independent metric"; ghost freedom now rests on the frame tier (#11 §7.2; [the v0.1 argument against a ghost](/wiki/gravity/tuning-test/geometric-action#the-v01-argument-against-a-ghost); [no second graviton under the original P2](/wiki/gravity/momentum-graviton/forcing-chain#superseded-no-second-graviton-under-the-original-p2)). The a⁻⁶ term of the same calculation survives in #11 §10: "the dual Einstein term is an a⁻⁶ step in G_eff" ([Row 10: an early step in G_eff](/wiki/predictions/early-universe-step)). The dual Einstein–Hilbert term behind the a⁻⁶ step is used in #1 §6 under a [D] tag but derived from the geometric action in no document, so the step tests a postulate (flag 49 in `review/wiki-build-flags.md`; [the dual frame](/wiki/cosmology/scale-factor-duality/closed-universe#the-dual-frame-what-closure-fixes-and-what-it-does-not)).

### X in an expanding universe

Whether a heavy X is stable in an expanding universe is open. #14 summarized the literature: "The published analyses of bimetric cosmological branches find gradient or ghost instabilities, but they assume a spin-2 mass of order the present Hubble rate and comparable Planck masses for the two metrics [4]", and a heavy spin-2 field is linearly stable at late times "in the regime where the second metric's Planck mass is much smaller than the first [5]" (#14 §1). The round-3 audit found reference [4] slightly over-generalized: one of its papers identifies a stable model, and another finds stable scalar perturbations for a particular parameter choice. The framework's reciprocity "sets the two Planck masses equal" (#14 §1), so the known stable regime is out of reach ([bimetric cosmology and its instabilities](/wiki/gravity/spin-2-fields/bimetric-cosmology); [Open: stability at equal Planck masses](/wiki/gravity/momentum-graviton/equal-planck-mass-stability)).

## Used by

- [The Fierz–Pauli mass term and the Boulware–Deser ghost](/wiki/gravity/spin-2-fields/fierz-pauli) — the extra mode of a non-Fierz–Pauli weight, and its return beyond quadratic order.
- [Bimetric cosmology and its instabilities](/wiki/gravity/spin-2-fields/bimetric-cosmology) — gradient and ghost instabilities of cosmological branches; the Higuchi ghost.
- [Why X must be massive](/wiki/gravity/momentum-graviton/forcing-chain) — the signature obstruction, and the healthy, auxiliary or ghost question the chain replaced.
- [The metric tier fails twice](/wiki/gravity/tuning-test/metric-tier-failures) — the Boulware–Deser ghost of metric-built potentials, battery tests T4 and T7.
- [The verdict: a conditional pass](/wiki/gravity/tuning-test/conditional-pass) — ghost-free in frame variables only.
- [Open: stability at equal Planck masses](/wiki/gravity/momentum-graviton/equal-planck-mass-stability) — the cosmological stability of a heavy X.
- [Open: Lorentzian dressing of the Euclidean skeleton (OP3)](/wiki/phase-space/born-geometry/lorentzian-dressing) — the indefinite target metric in Lorentzian signature.
- [Coset and hyperbolic sigma models](/wiki/symmetry-breaking/toy-models/coset-model/sigma-models) — a positive target metric, or a ghost.
- [Model I: action and symmetries](/wiki/symmetry-breaking/toy-models/coset-model/action-and-symmetries) — K's kinetic term contracted with H to avoid the de Sitter ghost.
- [The phantom divide and the null energy condition](/wiki/cosmology/dark-energy/phantom-divide) — a ghost scalar as one route to w < −1.
- [The geometric action S_H and the v0.1 action (superseded)](/wiki/gravity/tuning-test/geometric-action) — the notebook's minisuperspace argument against a ghost.

## References

The program's documents give no general reference for ghosts. For particular results they cite Higuchi (1987), #14's reference [6], and the analyses of bimetric cosmological branches, #14's references [4] and [5], all three checked by the round-3 audit ([bimetric cosmology and its instabilities](/wiki/gravity/spin-2-fields/bimetric-cosmology)); de Rham, Gabadadze and Tolley, #11's [9†] ([dRGT massive gravity](/wiki/gravity/spin-2-fields/drgt-massive-gravity)); Hassan and Rosen, #11's [10†] and [11†] ([Hassan–Rosen bimetric gravity](/wiki/gravity/spin-2-fields/hassan-rosen-bimetric)); Hinterbichler and Rosen, #11's [12†], for the frame-tier potentials ([vielbein formulation and wedge potentials](/wiki/gravity/spin-2-fields/vielbein-formulation)); and Boulanger, Damour, Gualtieri and Henneaux, #11's [8†] ([the multi-graviton no-go theorem](/wiki/gravity/spin-2-fields/multi-graviton-no-go)). Added by the wiki from model memory (†):

- M. Ostrogradsky (1850)†: the Hamiltonian of a higher-derivative Lagrangian, unbounded below.
- A. Pais, G. E. Uhlenbeck (1950)†: a field theory with four time derivatives, and its two modes of opposite sign.
- R. P. Woodard, "Ostrogradsky's theorem on Hamiltonian instability," Scholarpedia (2015)†: a review.
- D. G. Boulware, S. Deser (1972)†: the ghost of generic nonlinear massive gravity.
- C. de Rham, G. Gabadadze (2010)†: the limit that isolates the helicity-0 polarization, where the Boulware–Deser ghost appears as interactions with too many derivatives.
- G. W. Gibbons, S. W. Hawking, M. J. Perry (1978)†: the Euclidean gravitational action, unbounded below through the conformal factor.
- R. R. Caldwell (2002)†: phantom dark energy from a scalar with a wrong-sign kinetic term.
- S. M. Carroll, M. Hoffman, M. Trodden (2003)†; J. M. Cline, S. Jeon, G. D. Moore (2004)†: the decay of the vacuum with phantom ghosts, and the cutoff it needs.
- K. Hinterbichler, "Theoretical aspects of massive gravity," Rev. Mod. Phys. (2012)†; C. de Rham, "Massive gravity," Living Rev. Relativ. (2014)†: reviews, including the Hamiltonian analysis of massive gravity.

## Sources

- `notes/debt1a-ii-X-classification.md` §2 — the signature obstruction [T — standard]; §3 — the five polarizations, the health criterion [D — structural] and the Lorentzian caveat; §5 — "massive spin-2, conditionally healthy" and the stakes of the test.
- `notes/debt1a-geometric-core.md` §D — the ten components; the healthy, auxiliary or ghost classification; the positive target metric and the double-field-theory precedent.
- `notes/debt1a-iii-tuning-test.md` §2 — the metric tier's Boulware–Deser ghost, "a theorem-grade negative" [D — rigorous]; §3 — the frame tier, "ghost-free by construction" [D — structural, resting on T].
- `papers/broken-born-checkpoint-v2.md` §7.1 — "ungauged X by Lorentz signature" [D + T]; §7.2 — the tuning test [D][V]; §10 — "strictly w ≥ −1" and the dual Einstein term as an a⁻⁶ step; §14 item 1 — the class selected, not derived; item 3 — the Lorentzian dressing, open.
- `verify/battery.py` T4, T7 — the linearized potential's departure from the Fierz–Pauli form, and the power sum p₄ outside the linear span of the elementary symmetric polynomials.
- `papers/reciprocity-toy-models.md` §2 — K's target as two-dimensional de Sitter space and its two kinetic terms; §4 — the naive potential, unbounded below with H dynamical, its vacuum a saddle.
- `notes/toy-lagrangian.md` 'Chunk 1 results' — "which would give a ghost".
- `verify/toy_coset.py` — the gated checks of K's two kinetic terms and of the saddle.
- `review/round4-adjudication.md` 'Rulings' F1–F2 — the unbounded potential and the saddle, upheld.
- `notes/knot-dark-matter-standalone.md` §1, ref [6] — the instabilities of bimetric cosmological branches, the heavy spin-2 regime, equal Planck masses and the Higuchi bound (manuscript withdrawn for an unrelated error).
- `review/round3/referee/audit-notes.md` Step 1 — the "exponential Jeans-like instability"; the over-generalization of reference [4]; Higuchi's reference supports the bound.
- `review/v3-worklog.md` 'Round-2 pending list', item R7 — "the strong-coupling era H > H⋆ is unresolved".
- `notes/broken-born-theory.md` §4 — 'Ghost accounting' [D], with its open remainder [O]; §6 — "not a ghost — ã was never independent" [D]; §7 item 1 — w ≥ −1 [D]; 'Addendum (v0.4)' — X a second graviton; 'Addendum (v0.5)' — "exhibited twice independently".
- `CLAUDE.md` 'Since the handoff' — the dark-energy sector "under real pressure".
- `review/wiki-build-flags.md` item 25 — the notebook's "(§7)" for a constraint derived in §6; awaiting Paul's ruling.
- `notes/closed-universe.md` §7; `review/wiki-build-flags.md` item 49 — the dual Einstein–Hilbert term behind the a⁻⁶ step is not derived
- `notes/closed-universe.md` §6; `review/wiki-build-flags.md` item 53 — the Higuchi bound through the dressed mass
