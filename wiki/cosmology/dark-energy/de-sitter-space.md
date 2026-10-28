---
title: "De Sitter space"
weight: 5
status: established
description: "The maximally symmetric spacetime of a positive cosmological constant: constant Hubble rate, exponential expansion, Λ = 3H², the hyperboloid and the horizon; anti-de Sitter space as its negative-Λ counterpart; and the program's uses: row 5's standard expectation, the background of the Higuchi bound and the partially massless point, bimetric gravity's proportional backgrounds, and dS₂, the target space of K in model I."
provenance: [T]
sources:
  - "papers/broken-born-checkpoint-v2.md §13 row 5"
  - "papers/broken-born-checkpoint-v2.md §10"
  - "papers/broken-born-checkpoint-v2.md §7.4"
  - "papers/broken-born-checkpoint-v2.md §14 item 2"
  - "review/round3/referee/audit-notes.md Step 1"
  - "notes/knot-dark-matter-standalone.md §1"
  - "notes/knot-dark-matter-standalone.md ref [6]"
  - "notes/debt1a-ii-X-classification.md §3"
  - "papers/reciprocity-toy-models.md §2"
  - "notes/toy-lagrangian.md 'Chunk 1 results'"
  - "verify/toy_coset.py S1"
  - "review/round4/referee/out_model1.txt"
  - "notes/broken-born-theory.md §9 row 6"
  - "notes/broken-born-program-v1.md §9 row 5"
  - "review/wiki-build-flags.md item 27"
  - "review/wiki-build-flags.md items 27 (addendum), 45, 53"
  - "notes/closed-universe.md §2"
  - "notes/closed-universe.md §6"
---

*De Sitter space is the spacetime of a universe that contains nothing but a positive [cosmological constant Λ](/wiki/cosmology/dark-energy/cosmological-constant), an energy density of empty space that stays the same as space expands. Its expansion rate, the Hubble rate H, never changes, so the distances between distant galaxies grow exponentially, and every observer is surrounded by a horizon beyond which events can never be seen. Its curvature is the same at every point and in every direction; anti-de Sitter space is the counterpart for a negative cosmological constant. With a positive cosmological constant as its [dark energy](/wiki/cosmology/dark-energy), standard cosmology expects our universe to approach de Sitter space as matter thins: "Eternal de Sitter" is the standard expectation of the program's [row 5](/wiki/predictions/fate-of-expansion), where the program requires instead a far-future turnaround whose premise is unresolved. De Sitter space is also the background on which a massive spin-2 field, a graviton with mass, must satisfy the [Higuchi bound](/wiki/gravity/spin-2-fields/bimetric-cosmology#the-higuchi-bound), the setting of [partially massless gravity](/wiki/gravity/spin-2-fields/partially-massless-gravity), and, in two dimensions, the space of values of the field K in the program's first [toy model](/wiki/symmetry-breaking/toy-models/coset-model), where its metric, positive in one direction and negative in the other, would give a [ghost](/wiki/gravity/spin-2-fields/ghosts): a mode with negative energy.*

**Status:** Established — [T] — textbook general relativity and cosmology, written here from general knowledge, with the literature it names marked † (de Sitter 1917 †; Hawking and Ellis 1973 †; Gibbons and Hawking 1977 †; Starobinsky 1979 †); no `verify/` script checks the spacetime itself. The relation Λ = 3H² is the one the [round-3](/wiki/method/review/round-3) audit used to convert Higuchi's bound (`review/round3/referee/audit-notes.md` Step 1). The program's uses are stated in [checkpoint #11](/wiki/history/documents/checkpoint) §13 row 5 and §7.4, in the withdrawn manuscript [#14](/wiki/dark-matter/candidates/soliton-candidate) §1, and in the [toy-model note](/wiki/symmetry-breaking/toy-models) §2. [The gate](/wiki/method/verification/the-gate) checks the note's statement that the naive kinetic term on K's de Sitter target is indefinite (`verify/toy_coset.py`; [the toy-model scripts](/wiki/method/verification/toy-model-scripts)).

On this page H is the Hubble rate, not the program's phase-space metric H, except in the section on model I, which uses H for that model's metric field.

## The spacetime [T]

### A universe with only a cosmological constant

[General relativity](/wiki/gravity/spin-2-fields/general-relativity) with a cosmological constant has the field equations

```text
G_μν + Λ g_μν = T_μν / M_P²
```

where g_μν is the metric, G_μν the Einstein tensor built from its curvature, T_μν the stress-energy tensor of matter, and M_P the [reduced Planck mass](/wiki/gravity/spin-2-fields/planck-units#two-conventions-for-the-planck-mass-t). Moved to the right-hand side, the Λ term is the stress-energy of a fluid with energy density ρ_Λ = M_P²Λ and pressure −ρ_Λ, so its equation of state is w = −1: it is the [cosmological constant](/wiki/cosmology/dark-energy/cosmological-constant) of dark-energy physics. The vacuum energy of quantum fields has the same form and adds to Λ ([the cosmological-constant problem](/wiki/gravity/spin-2-fields/cosmological-constant-problem)).

For a homogeneous, spatially flat universe with scale factor a(t), the factor by which distances between distant galaxies have grown, the Friedmann equation reads 3M_P²H² = ρ, with H = ȧ/a the [Hubble rate](/wiki/cosmology/scale-factor-duality/friedmann-cosmology) and ρ the total energy density. With ρ_Λ as the only content:

```text
3M_P²H² = M_P²Λ                ⇒   Λ = 3H²
ȧ = H a,  with H constant      ⇒   a(t) ∝ e^{Ht}
ds² = −dt² + e^{2Ht} dx²            (units with c = 1; mostly-plus sign convention)
```

The expansion rate stays constant because the energy density does: matter thins as space grows, and a cosmological constant does not. Each interval 1/H of time multiplies every distance between galaxies at rest in the comoving coordinates x by the same factor. The expansion accelerates: with p = −ρ, the second Friedmann equation gives ä/a = H², which is positive ([acceleration](/wiki/cosmology/dark-energy/quintessence#acceleration-t)).

### Maximal symmetry and the hyperboloid

The exponential form above does not show how symmetric the spacetime is. De Sitter space, the solution found by W. de Sitter (1917 †), is the hyperboloid

```text
−X₀² + X₁² + X₂² + X₃² + X₄² = 1/H²
```

in a flat spacetime with one time direction, X₀, and one space direction more than ours (Hawking and Ellis 1973 †). The rotations and boosts of that larger flat spacetime map the hyperboloid to itself and act on it as symmetries. They move any point of de Sitter space to any other, and at each point they include the rotations and boosts of [special relativity](/wiki/conjugate-relativity/special-relativity). A spacetime with as many independent symmetries as flat spacetime has is called maximally symmetric, and its curvature is the same everywhere:

```text
R_μνρσ = H² (g_μρ g_νσ − g_μσ g_νρ)        (R_μνρσ the Riemann tensor; mostly-plus sign convention)
```

Flat Minkowski spacetime, de Sitter space and anti-de Sitter space are the maximally symmetric spacetimes, with Λ zero, positive and negative [T].

The exponentially expanding form covers half of the hyperboloid. Other choices of time cut the same spacetime into different slices [T]. In global coordinates the spatial slices are spheres whose radius, cosh(Ht)/H, shrinks to a smallest value 1/H at t = 0 and then grows without limit: the whole hyperboloid is a closed universe that contracts and re-expands. In static coordinates, centred on one observer, the metric does not depend on time; they are the natural description of the horizon.

### The horizon

A light signal emitted at time t toward an observer covers, however long it travels, at most the comoving distance

```text
∫ₜ^∞ dt′ / a(t′) = 1 / (H a(t))
```

which is finite. An event that lies farther from the observer than the proper distance 1/H (c/H in ordinary units) at the moment it happens therefore never becomes visible: 1/H is the radius of the observer's event horizon [T]. A galaxy at fixed comoving distance recedes faster as the scale factor grows and in time passes beyond the horizon. Light it emitted earlier keeps arriving, later and more [redshifted](/wiki/cosmology/scale-factor-duality/redshift); light it emits afterwards never arrives. In static coordinates,

```text
ds² = −(1 − H²r²) dt² + dr² / (1 − H²r²) + r² dΩ²        (dΩ² the metric of a unit sphere)
```

the horizon is the sphere r = 1/H around the observer at r = 0, where the coefficient of dt² vanishes. Gibbons and Hawking (1977 †) showed that a freely falling detector in de Sitter space registers thermal radiation from its horizon, at a temperature proportional to H.

### The far future of an expanding universe

With matter and a positive cosmological constant, the Friedmann equation reads 3M_P²H² = ρ_m + M_P²Λ, with ρ_m the matter density. The matter density falls as a⁻³ while the vacuum term stays constant, so H² approaches Λ/3 and the spacetime approaches de Sitter space: the expansion never stops [T]. In the standard cosmological model, whose dark energy is a cosmological constant, this is the far future of our universe.

[Inflation](/wiki/cosmology/early-universe/inflation-and-dilution) is an approximate de Sitter stage at the other end of the history. A field whose energy is almost all potential energy keeps H nearly constant, and the scale factor grows nearly exponentially [T]. The primordial gravitational-wave background is, above all, the one left by such an early de Sitter stage [T] (Starobinsky 1979 †; [primordial backgrounds](/wiki/cosmology/early-universe/phase-transition-gravitational-waves#primordial-backgrounds-t)).

## Anti-de Sitter space [T]

Anti-de Sitter space is the maximally symmetric spacetime with Λ < 0. It is also a hyperboloid, but in a flat space with two time directions instead of one, and its curvature has the opposite sign to that of de Sitter space [T].

A negative cosmological constant cannot drive an expansion on its own: for a flat universe the Friedmann equation 3M_P²H² = ρ has no solution when the total density ρ is negative. With matter present, a flat universe with Λ < 0 expands while the matter density exceeds −ρ_Λ, halts when the two cancel and H = 0, and then contracts toward a collapse [T]. The spacetime of a negative vacuum energy alone is anti-de Sitter, so this sequence is described as a transition to anti-de Sitter space followed by collapse. A field that settles where its potential is negative acts as a negative cosmological constant and produces the same sequence ([recollapse](/wiki/cosmology/dark-energy/quintessence#recollapse-t)).

The program cites fits of this kind: #11 §10 reports "high posterior preference for a future anti-de Sitter transition and collapse in negative-minimum quintessence fits [19S, 20S, 21S]"; flag 45 in `review/wiki-build-flags.md` finds that only [19] supports the clause, [20] fitting V₀[1 + cos] with null spatial curvature and mentioning no anti-de Sitter phase or collapse. Its own [turnaround](/wiki/cosmology/scale-factor-duality/conjugate-bounce) needs the vacuum energy to become negative, but the potential the documents write for the dark-energy field [τ](/wiki/cosmology/dark-energy/tau-quintessence), V₀[1 + cos(τ/f)], is never negative for V₀ > 0. The conflict is unresolved ([Open: the sign of V(τ) and the turnaround](/wiki/cosmology/dark-energy/potential-sign); flag 27 in `review/wiki-build-flags.md`). The flag's addendum (2026-10-27) finds that a closed universe turns around with that potential, curvature reversing the expansion while V ≥ 0, so the turnaround needs a closed universe rather than an anti-de Sitter phase ([a closed Comatter universe](/wiki/cosmology/scale-factor-duality/closed-universe#the-turnaround-needs-k--1-dv)).

## How the program uses de Sitter space

### Row 5: "Eternal de Sitter"

Row 5 of the [predictions table](/wiki/predictions), #11 §13:

| Observable | Standard expectation | Program requirement | Killed by |
| --- | --- | --- | --- |
| Fate of expansion | Eternal de Sitter | Turnaround = conjugate bounce | (Long horizon; near-term test is row 4) |

"Eternal de Sitter" is the far future described above: with a positive cosmological constant, the universe approaches de Sitter space and expands forever. The program requires instead that the expansion halt and reverse, and through the [cosmological constraint](/wiki/cosmology/scale-factor-duality/cosmological-constraint) a·ã = 1 it reads that event as [the conjugate universe's bounce](/wiki/cosmology/scale-factor-duality/conjugate-bounce). The turnaround needs a negative vacuum energy, the anti-de Sitter sign, which τ's potential as written does not reach (flag 27, above), unless the universe is closed, in which case curvature supplies the reversal (flag 27 addendum).

The standard-expectation column reads "Eternal de Sitter" in all three versions of the table (#1 §9 row 6; #9 §9 row 5; #11 §13 row 5). The [lab notebook](/wiki/history/documents/lab-notebook)'s requirement named the anti-de Sitter transition directly: "Turnaround after V(τ)<0; AdS transition preferred by current quintessence fits" (#1 §9 row 6, transcribed from its LaTeX), AdS being anti-de Sitter ([history of the predictions table](/wiki/predictions/table-history)).

### The background of a massive spin-2 field

A massive spin-2 field has five polarizations [T]: [calc note #6](/wiki/history/documents/debt-1-notes) counts "its five polarizations" for the [momentum graviton X](/wiki/gravity/momentum-graviton) (#6 §3). In flat spacetime any positive mass is allowed. On de Sitter space the curvature sets a second scale, H, and the mass must satisfy the Higuchi bound [T]:

```text
m² ≥ 2H²
```

For masses between zero and the bound, the helicity-0 polarization has negative norm: it is a ghost, and the theory is not unitary [T]. #14 cites the bound as its reference [6], A. Higuchi, Nucl. Phys. B 282, 397 (1987). The round-3 audit read it from Higuchi's abstract, "M^2 cannot be between 0 and 2/3 x (cosmological constant)", converted it with "Lambda = 3H^2" to "m^2 >= 2H^2", and found that the reference supports the statement (`review/round3/referee/audit-notes.md`, Step 1). The conversion is the relation Λ = 3H² of the first section.

At the edge of the bound, m² = 2H², a scalar gauge symmetry removes the helicity-0 polarization, and the field is partially massless [T] ([the partially massless value](/wiki/gravity/spin-2-fields/partially-massless-gravity#the-partially-massless-value)). The edge exists only because de Sitter space has a curvature scale: at H = 0 it is m = 0, the ordinary massless graviton.

A field much heavier than H meets the bound trivially. #14 §1: "The Higuchi bound m^2 >= 2H^2 [6] is satisfied trivially by the heavy field", the heavy field being X. Flag 53 finds that the conclusion holds and the reasoning does not: with a fixed mass the argument fails once 2(H² + k/a²) > M_X², at TeV temperatures for the smallest M_X and during inflation unless M_X > √2·H_inf, while the bound still holds through X's dressed mass on the program's branch ([the momentum graviton in a closed universe](/wiki/gravity/momentum-graviton/closed-universe#the-higuchi-bound-holds-through-the-dressed-mass)). The open question about X is a different one, its cosmological stability at equal Planck masses ([Open: stability at equal Planck masses](/wiki/gravity/momentum-graviton/equal-planck-mass-stability)).

### Proportional de Sitter backgrounds in bimetric gravity

[Hassan–Rosen bimetric gravity](/wiki/gravity/spin-2-fields/hassan-rosen-bimetric) has two dynamical metrics, g and f. Among its simplest solutions are proportional backgrounds, f = c²g with c a constant, in which each metric solves Einstein's equations with an effective cosmological constant; when that constant is positive, both metrics are de Sitter [T]. Around such a background the fluctuations separate into a massless spin-2 mode and a massive one, and the massive mode is a spin-2 field on de Sitter space of the kind just described, subject to the Higuchi bound [T] ([proportional de Sitter backgrounds](/wiki/gravity/spin-2-fields/partially-massless-gravity#proportional-de-sitter-backgrounds)).

The partially massless point of bimetric gravity is defined on such backgrounds. #11 §7.4: "the PM point β₀ = 3α⁻²β₂, β₁ = β₃ = 0, β₄ = 3α²β₂ makes the potential g↔f symmetric, with proportional de Sitter solutions of undetermined ratio [24S]", PM standing for partially massless; the undetermined ratio is c, which #11 does not define (the wiki reads it as the c of f = c²g). The same paragraph separates the point from the program's own result: "Note the PM point sits at Λ ≠ 0 with c undetermined; our flat-aligned-vacuum identity selects a *different* point of the same branch (β₁ ≠ 0 generically, β₀ = −4β₁ − 3β₂)". The partially massless point lives on de Sitter backgrounds, while the program's [vacuum-energy identity](/wiki/gravity/palindromic-branch/vacuum-energy-identity) concerns a flat vacuum at the aligned point, where the two frames coincide. The detailed comparison of the two is open problem 2 of #11 §14 ([Open: the partially-massless comparison (OP2)](/wiki/gravity/palindromic-branch/pm-comparison)).

### Two-dimensional de Sitter space as the target of K

In this section H is model I's phase-space metric field, not the Hubble rate.

[Model I](/wiki/symmetry-breaking/toy-models/coset-model/action-and-symmetries) of the toy-model note is a [sigma model](/wiki/symmetry-breaking/toy-models/coset-model/sigma-models): its fields take values in curved spaces, called target spaces. One field is the real structure K, which marks which line of the phase plane is position. Version 2 of the note: "K, traceless with det K = −1. Its target is the one-sheeted hyperboloid a² + bc = 1, which is two-dimensional de Sitter space" (§2). For K = [[a, b], [c, −a]], K² = (a² + bc)·1, so det K = −1 is the condition K² = 1. Writing b = u + v and c = u − v turns a² + bc into a² + u² − v², so the target is the hyperboloid −v² + a² + u² = 1 in the flat space with coordinates (a, u, v), in which v is a time direction: the two-dimensional version of the hyperboloid above, with radius 1 [T].

The metric that the hyperboloid inherits from that flat space has one positive and one negative direction, which is what makes de Sitter space a spacetime. As the target of a field, it gives a ghost [T] ([positive target metrics, and the de Sitter ghost](/wiki/symmetry-breaking/toy-models/coset-model/sigma-models#positive-target-metrics-and-the-de-sitter-ghost)). The worklog: "K's own target space (de Sitter dS₂) has an indefinite metric, which would give a ghost" (`notes/toy-lagrangian.md`, 'Chunk 1 results'). The naive kinetic term Tr(∂K ∂K) is, up to a constant factor, that indefinite metric [T]. At K₀ = diag(1, −1) it is "2 db dc" (note §2), which is positive when db and dc have the same sign and negative when they differ. Model I avoids the ghost by contracting K's kinetic term with H, Tr(H⁻¹ ∂Kᵀ H ∂K), which "is positive definite" (note §2). [The gate](/wiki/method/verification/the-gate) checks both statements, the first on random samples (`verify/toy_coset.py`; [the toy-model scripts](/wiki/method/verification/toy-model-scripts)):

```text
PASS  the K kinetic term Tr(H^-1 dK^T H dK) is positive for random H and dK (no ghost)
PASS  the naive Tr(dK dK) is indefinite on K's target space (de Sitter): 2 db dc
```

The hyperboloid is non-compact: K can move along it without limit while K² = 1 continues to hold. The [round-4](/wiki/method/review/round-4) referee's counterexample runs along such a path. On a family of compatible pairs (H, K) moved by boosts of the phase plane, the entries of K grow without limit while K² = 1 holds, and the naive ρ-preserving potential falls without bound (`review/round4/referee/out_model1.txt`; [Obituary: the naive ρ-preserving potential](/wiki/symmetry-breaking/toy-models/coset-model/naive-potential)).

At H = 1 the vacua of model I form a circle on the hyperboloid, K(φ) = [[cos φ, sin φ], [sin φ, −cos φ]], and the angle φ parametrizes the [Lagrangian Grassmannian](/wiki/phase-space/modular-field/lagrangian-grassmannian) Λ(1) (note §2), a Λ unrelated to the cosmological constant. #11 §10: "In the coset model that angle parametrizes Λ(1): it is τ's circle" ([the polarization as a Goldstone angle](/wiki/symmetry-breaking/goldstone-angle)). Here de Sitter space is a space of field values, not a spacetime. Model I's fields live on a "1+1 dimensional base" (note §2), and nothing in the model is an expanding universe.

## Standard references

- A. Higuchi, Nucl. Phys. B 282, 397 (1987): the bound m² ≥ 2H². It is #14's reference [6], unmarked there; the round-3 audit found that it supports the statement.
- Added by the wiki from model memory (†): W. de Sitter (1917)†, the solution with a positive cosmological constant; S. W. Hawking and G. F. R. Ellis, *The Large Scale Structure of Space-Time* (Cambridge University Press, 1973)†, the hyperboloid, its coordinate patches and its horizons; G. W. Gibbons and S. W. Hawking (1977)†, the temperature of the de Sitter horizon; A. A. Starobinsky (1979)†, the gravitational-wave background from an early de Sitter stage. None of these is cited in the program's documents, and none has been checked against the source.

## Used by

- [Row 5: the fate of the expansion](/wiki/predictions/fate-of-expansion) — "Eternal de Sitter", the standard expectation the program's turnaround departs from.
- [The turnaround as the conjugate bounce](/wiki/cosmology/scale-factor-duality/conjugate-bounce) — the transition to anti-de Sitter space that a turnaround needs.
- [Open: the sign of V(τ) and the turnaround](/wiki/cosmology/dark-energy/potential-sign) — the negative vacuum energy that τ's potential as written does not reach.
- [Partially massless gravity](/wiki/gravity/spin-2-fields/partially-massless-gravity) — a spin-2 field on de Sitter space at the edge of the Higuchi bound, and the bimetric point with proportional de Sitter solutions.
- [Open: the partially-massless comparison (OP2)](/wiki/gravity/palindromic-branch/pm-comparison) — the partially massless point at Λ ≠ 0, set against the flat vacuum of the identity.
- [Open: stability at equal Planck masses](/wiki/gravity/momentum-graviton/equal-planck-mass-stability) — the Higuchi bound, met trivially by a heavy X.
- [The momentum graviton in a closed universe](/wiki/gravity/momentum-graviton/closed-universe) — the Higuchi bound through the dressed mass (flag 53).
- [Model I: action and symmetries](/wiki/symmetry-breaking/toy-models/coset-model/action-and-symmetries) — K's target, dS₂, and the H-contracted kinetic term that avoids its ghost.
- [Obituary: the naive ρ-preserving potential](/wiki/symmetry-breaking/toy-models/coset-model/naive-potential) — the non-compact hyperboloid along which the potential falls without bound.

## Sources

- `papers/broken-born-checkpoint-v2.md` §13 row 5 — "Eternal de Sitter" against "Turnaround = conjugate bounce"
- `papers/broken-born-checkpoint-v2.md` §10 — the anti-de Sitter transition in negative-minimum quintessence fits; τ's potential; the coset model's angle as Λ(1), τ's circle
- `papers/broken-born-checkpoint-v2.md` §7.4, §14 item 2 — proportional de Sitter solutions at the partially massless point, which sits at Λ ≠ 0, and the different point selected by the flat-vacuum identity; the open comparison
- `review/round3/referee/audit-notes.md` Step 1 — Higuchi's abstract and the conversion with Λ = 3H²
- `notes/knot-dark-matter-standalone.md` §1, ref [6] — the Higuchi bound, met trivially by the heavy field; the citation (manuscript withdrawn for an unrelated error: its Kibble estimate of the relic abundance had been normalized too low)
- `notes/debt1a-ii-X-classification.md` §3 — the five polarizations of a massive spin-2 field
- `papers/reciprocity-toy-models.md` §2 — K's target, the one-sheeted hyperboloid a² + bc = 1, as two-dimensional de Sitter space; the naive and the H-contracted kinetic terms; the 1+1 dimensional base; the vacua K(φ) and Λ(1)
- `notes/toy-lagrangian.md` 'Chunk 1 results' — the indefinite metric of dS₂ "would give a ghost"
- `verify/toy_coset.py` S1 — the two kinetic-term checks
- `review/round4/referee/out_model1.txt` — the boost family on which K grows without limit with K² = 1, and the naive potential falls
- `notes/broken-born-theory.md` §9 row 6; `notes/broken-born-program-v1.md` §9 row 5 — "Eternal de Sitter" in the earlier tables, and the first version's "AdS transition"
- `review/wiki-build-flags.md` item 27 — the potential as written cannot turn negative; its addendum — the turnaround in a closed universe; item 45 — the compound citation for the anti-de Sitter fits; item 53 — the Higuchi bound's reasoning
- `notes/closed-universe.md` §2 — the closed turnaround with V ≥ 0; §6 — the dressed Higuchi bound
