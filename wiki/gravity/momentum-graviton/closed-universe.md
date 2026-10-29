---
title: "The momentum graviton in a closed universe"
weight: 105
status: alive
description: "With its second metric f dynamical at equal Planck masses, f closes with the same curvature as g and stays aligned, on a branch that needs β₁ > 0 and passes the turnaround smoothly; early on G_eff = 2G_N, the Higuchi bound holds through the dressed mass, and Könnig's gradient instability operates above about 1.3 TeV; a frozen f admits no closed expanding universe but contradicts the record's equal Planck masses."
provenance: [D, V]
sources:
  - "notes/closed-universe.md §6"
  - "notes/closed-universe.md §2"
  - "notes/closed-universe.md §8"
  - "notes/closed-universe.md §9"
  - "notes/closed-universe.md §10"
  - "verify/closed_universe.py 'D. Bimetric sector'"
  - "verify/closed_universe.py 'Anchors (independent of the investigation)'"
  - "review/wiki-build-flags.md items 5, 51, 52, 53"
  - "notes/beta-coefficients.md §3"
  - "papers/phase-space-diameter.md §8.2"
  - "review/round5-adjudication.md 'Rulings' R1"
  - "papers/broken-born-checkpoint-v2.md §7"
  - "papers/broken-born-checkpoint-v2.md §10"
  - "notes/knot-dark-matter-standalone.md §1"
---

*The program's [momentum graviton X](/wiki/gravity/momentum-graviton) is the massive spin-2 field of a two-metric theory: beside the ordinary spacetime metric g there is a second metric f, and X is the combination of their fluctuations that carries mass. The closed-universe note of 2026-10-27 asks what happens to f if the universe is closed. If f is a dynamical field with the same Planck mass as g, which is what the program's reciprocity requires, then f must be closed with the same curvature, it stays almost exactly aligned with g, and the expansion passes smoothly through its turnaround. In the early universe the second metric makes gravity up to twice as strong as today, a step that the checkpoint does not mention, and a known instability of two-metric cosmologies operates above temperatures of about 1.3 TeV, in energy units. If instead f were a fixed background, a closed expanding universe would be impossible, but that reading contradicts the record's equal Planck masses.*

**Status:** Alive — computed, not reviewed — [D][V], with the uniqueness of the closed reference metric [T] (Comelli, Crisostomi, Nesti and Pilo 2012) — every derivation and number is recomputed in section D of `verify/closed_universe.py` ([the closed-universe script](/wiki/method/verification/closed-universe-script)), two of them against published results; the note's results were checked by independent verifiers and a completeness critic and have not been reviewed (`notes/closed-universe.md` header). It bears on flags 5, 51, 52 and 53 in `review/wiki-build-flags.md`, which await Paul's ruling.

## The setting

The note takes the program's gravity sector as #11 §7 and the phase-space-diameter note give it (§1, §6): [Hassan–Rosen bimetric gravity](/wiki/gravity/spin-2-fields/hassan-rosen-bimetric) with both metrics dynamical, the [palindromic](/wiki/gravity/palindromic-branch/palindrome) coefficients βₙ = β₄₋ₙ, the zero-vacuum branch β₀ = −4β₁ − 3β₂ on which the flat aligned vacuum has no vacuum energy ([the vacuum-energy identity](/wiki/gravity/palindromic-branch/vacuum-energy-identity)), and equal Planck masses, M_f = M_g, which reciprocity forces ([equal Planck masses](/wiki/gravity/momentum-graviton/spectrum-and-parity#equal-planck-masses); `notes/beta-coefficients.md` §3).

Both metrics take the homogeneous form of [Friedmann cosmology](/wiki/cosmology/scale-factor-duality/friedmann-cosmology) [T]: g with lapse 1 and scale factor a, f with lapse X and scale factor Y. (This X, f's lapse, is the note's symbol and is distinct from the field X.) The ratio y = Y/a measures how far f has moved from g; y = 1 is the aligned vacuum of [the laboratory bound on X's range](/wiki/gravity/momentum-graviton/range-bound), background ratio u = 1. The general physics of such solutions, and their known instabilities, is on [bimetric cosmology and its instabilities](/wiki/gravity/spin-2-fields/bimetric-cosmology).

## f closes with g [D][V][T]

- **The algebra does not see k.** On the dynamical branch both Friedmann equations depend on the curvature k only through H² + k/a², so the algebraic equation for y, a quartic, does not depend on k (§6). The script checks the quartic against von Strauss et al. 2012's, a published anchor.
- **f is closed with the same k.** A metric on S³ that respects the symmetry of a closed universe must be a multiple of the round metric: the symmetric two-index tensors invariant under the rotations about a point form a one-dimensional space (§6) [D][V]. That unequal curvatures of the two metrics are inconsistent is [T: Comelli, Crisostomi, Nesti, Pilo 2012, arXiv:1111.1983].

## The branch relation [D][V]

On the branch the exact relation is (§6):

```text
3M̄²(H² + k/a²) = ρ + (M̄²M_X²/8)·(β₁/(β₁ + β₂))·(1 − y)⁴/y
```

with M̄² = 2M_g² (the script's statement) and ρ the matter density. The second term is the bimetric sector's contribution, which vanishes at y = 1 to fourth order.

- At leading order, 1 − y = 2(H² + k/a²)/M_X², which is 1.5×10⁻⁶¹ today at the smallest allowed M_X c² = 5.24 meV (§6). f is aligned with g today to that accuracy.
- M_X² = 4m²(β₁ + β₂), with m the interaction scale of the potential. This confirms flag 5, which reads #11 §7.5's "M_X ∝ 2(β₁+β₂)" as a statement about M_X² ([spectrum, parameters and reciprocity parity](/wiki/gravity/momentum-graviton/spectrum-and-parity)).
- The exact relation is also what guarantees that the bimetric sector contributes nothing that competes with τ's dark energy: flag 52 notes that #11 §10 attributes the guarantee to §7.3's aligned-point identity alone.

## β₁ > 0 is required [D][V]

Every broken vacuum, a proportional background f = u²g with u ≠ 1, has a vacuum energy Λ_g = −3m²(β₁ + β₂)(u − 1)² = 18m²u(β₁ + β₂)²/β₁ (§6). β₁ > 0 is required: for β₁ ≤ 0 the aligned branch is bounded, or ends at a broken vacuum with negative Λ_g and a Higuchi ghost (§6). No document of the record states the requirement (flag 51; its audit found it nowhere in the repository). The phase-space-diameter note had stated only when broken vacua exist ([why that vacuum and no other](/wiki/gravity/momentum-graviton/range-bound#why-that-vacuum-and-no-other-dv)). On the β₁ > 0 branch the ratio y stays in (0, 1] while Y grows with a, so the compactness of the polarization frame's moduli does not bound the universe (§2).

## A regular turnaround [D][V]

In a toy closed history, f's lapse passes smoothly through the turnaround ȧ = 0: a_max = 1.588667, with lapse 1.226664 there (§6). The script integrates the history and finds the lapse a function of a alone that never divides by ȧ, positive along the whole path, with both Friedmann equations satisfied along it. The turnaround of the [closed universe](/wiki/cosmology/scale-factor-duality/closed-universe) therefore raises no difficulty in the gravity sector.

## The early universe [D][V]

### Gravity up to twice as strong

For H ≫ M_X, G_eff = 2G_N: gravity acts twice as strongly as in the late universe (§6). The script's check finds H² + k/a² → ρ/(3M_g²) in that limit, against 3(2M_g²)(H² + k/a²) = ρ near alignment, an effective Planck mass squared of M_g² early and 2M_g² late. The halfway point is at T ≈ 1.55–1.58 TeV (H/M_X = 0.75–0.77) for the smallest M_X, scaling as √M_X. #11 §10 omits this step (flag 52). It is a different step from the a⁻⁶ step of [row 10](/wiki/predictions/early-universe-step), which comes from the lab notebook's dual gravity term.

### The Higuchi bound holds through the dressed mass

A massive spin-2 field on an expanding background must satisfy the Higuchi bound, m² ≥ 2H² in de Sitter space, or its helicity-0 mode is a ghost [T] ([the Higuchi bound](/wiki/gravity/spin-2-fields/bimetric-cosmology#the-higuchi-bound)). The withdrawn manuscript #14 and its worklog called the bound "trivially satisfied by a heavy X". The note finds that the conclusion holds and the reasoning does not (§6; flag 53): with a fixed mass the argument fails once 2(H² + k/a²) exceeds M_X², at TeV temperatures for the smallest M_X and during inflation unless M_X > √2·H_inf (flag 53). The bound holds through the dressed mass on the branch:

```text
m_FP²(y) − 2(H² + k/a²) = −yρ_y/(3M_g²) > 0
```

where m_FP(y) is the Fierz–Pauli mass at ratio y ([Fierz–Pauli theory](/wiki/gravity/spin-2-fields/fierz-pauli)) and ρ_y the derivative of the density with respect to y along the branch (the wiki's reading of the note's symbol).

### The gradient instability

Könnig's scalar gradient instability for w > −1/2 operates above about 1.3 TeV (H ≈ 0.5 M_X). It returns in the recollapse, and equal Planck masses close the usual escape from it (§6). The script checks Könnig 2015's eigenfrequency on the program's branch, a published anchor, and finds the instability above T = 1.31–1.38 TeV for radiation or dust. This is the live problem of the early universe; it bears directly on [Open: stability at equal Planck masses](/wiki/gravity/momentum-graviton/equal-planck-mass-stability), whose regime it is. The note's pre-registration had expected the Higuchi bound to be the difficulty; it is the gradient instability (§10).

## If f were frozen [D][V]

If f were a fixed background rather than a dynamical field (§6):

- a frozen flat f cannot be written in k = +1 Friedmann form: the curvature component (X² + Ẏ²)sin²χ/X² of f, χ being the angle on S³, never vanishes;
- a frozen scale, Ẏ = 0, makes the Bianchi constraint proportional to ȧ, so there is no expanding universe for any k;
- every frozen f is the M_f → ∞ limit, which the record's equal Planck masses (`notes/beta-coefficients.md` §3) exclude.

So the frozen reading contradicts the record. What remains unsettled is a definition: the record never defines E₀[J] beyond "the polarization frame" on compact moduli, and round-5 ruling R1 holds that question open (§6; [the premise: the aligned vacuum](/wiki/gravity/momentum-graviton/range-bound#the-premise-the-aligned-vacuum-u--1)).

## Modes on the sphere [D]

X's lowest tensor modes on S³ are the L = 2 modes, those of the Bianchi IX cosmologies (§8). How they and the other perturbations behave through the recollapse is open.

## What is open

From the note's §9 [O]:

- inflation and the bimetric sector together: G_eff = 2G_N during inflation, with two light gravitons;
- perturbations, and X's L = 2 modes, through the recollapse.

Both are on [open problems and the queue](/wiki/status/open-problems). The open stability question at equal Planck masses now has a concrete form, the gradient instability above about 1.3 TeV.

## Sources

- `notes/closed-universe.md` §6 — the branch and its k-independence, f closed with the same k, the exact relation, 1 − y today, M_X², the broken vacua and β₁ > 0, the regular turnaround, G_eff = 2G_N and its halfway point, the dressed Higuchi bound, the gradient instability, and f frozen; §2 — y in (0, 1] on the β₁ > 0 branch; §8 — the L = 2 modes; §9 — what is open; §10 — the pre-registration scored
- `verify/closed_universe.py` section D — D1 (the y-equation, with von Strauss et al. 2012 as anchor), D2 and D3 (the exact relation and leading order), D4 (M_X²), D5 (the broken vacua), D6 (G_eff, the halfway point, Könnig 2015's eigenfrequency and the crossover), D7 (SO(4)-invariant tensors), D8 (the frozen reference), D9 (the turnaround toy); the anchors — the interpolation that gives the smallest M_X
- `review/wiki-build-flags.md` items 5, 51, 52 and 53 — M_X², β₁ > 0, the omitted G_eff step and the Higuchi reasoning, with their audits; awaiting Paul's ruling
- `notes/beta-coefficients.md` §3 — equal effective Planck masses
- `papers/phase-space-diameter.md` §8.2 and `review/round5-adjudication.md` 'Rulings' R1 — the aligned vacuum, the smallest M_X, and the open definition of E₀[J]
- `papers/broken-born-checkpoint-v2.md` §7 — the gravity sector and "M_X ∝ 2(β₁+β₂)"; §10 — the guarantee that the wedge sector does not compete with τ
- `notes/knot-dark-matter-standalone.md` §1 — "satisfied trivially by the heavy field" (manuscript withdrawn for an unrelated error)
