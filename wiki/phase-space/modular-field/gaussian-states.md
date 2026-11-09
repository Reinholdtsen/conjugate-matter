---
title: "Gaussian wave packets on the Siegel half-plane"
weight: 15
status: established
description: "A Gaussian wave packet ψ_Z ∝ exp(iZx²/2) is labelled by a point Z = X + iY of the upper half-plane; the Fourier transform sends Z to −1/Z, Δx/Δp = 1/|Z|, the loci |Z| = 1, Z = i and det H_Z = 1 are distinct, and on the slice X = 0 the log of the aspect ratio is the distance from Z = i."
provenance: [T, V]
sources:
  - "wiki/papers/phase-space-diameter.md §5"
  - "wiki/papers/phase-space-diameter.md §6"
  - "wiki/papers/phase-space-diameter.md References"
  - "verify/phase_space_diameter.py"
  - "review/round5-adjudication.md 'Rulings' R13, R14"
  - "review/round5-adjudication.md 'Author-found items' 2"
  - "review/round5-adjudication.md 'Recommendations to Paul'"
  - "review/round5-adjudication.md 'Verdict'"
  - "wiki/papers/broken-born-checkpoint-v2.md §6"
  - "wiki/papers/broken-born-checkpoint-v2.md §10"
  - "review/wiki-build-flags.md item 23"
---

*A Gaussian wave packet is the bell-shaped quantum state ψ(x) ∝ exp(iZx²/2), whose whole shape is set by one complex number Z = X + iY with Y > 0: Y fixes the width in position, and X adds a chirp, a phase that ties momentum to position. The labels fill the upper half of the complex plane, the one-coordinate case of [the Siegel domain](siegel-domain.md), and the linear maps of phase space that preserve its [symplectic form](../reciprocity/symplectic-form.md) move them by Möbius maps. The [Fourier transform](../reciprocity/fourier-transform.md), which turns a waveform into its spectrum, sends the packet labelled Z to the one labelled −1/Z; on wave packets it is the inversion by which [Born reciprocity](../reciprocity/born-reciprocity.md) acts on the program's [modular field](modular-inversion.md). Three sets of labels that the program's record mentions in connection with self-duality then come apart: the packets with |Z| = 1 are as wide in position as in momentum, Z = i is the one packet the transform leaves unchanged, and the condition det H = 1 holds for every Z. For a packet without a chirp, the logarithm of its width ratio is its distance from Z = i in the geometry of the half-plane, which is how the phase-space-diameter note measures how far the universe's radiation is from a self-dual shape. The mathematics is standard, and the note's script checks the formulas the note uses.*

**Status:** Established — literature [T]: the labelling of Gaussian states by the Siegel upper half-space and the Möbius action of the symplectic group on them are cited by the phase-space-diameter note ([`wiki/papers/phase-space-diameter.md` §5](../../papers/phase-space-diameter.md#5-what-reciprocity-adds-invariant-area-inverted-shape)) to [Ohsawa 2015](https://arxiv.org/abs/1504.03963) and [de Gosson 2013](https://arxiv.org/abs/1305.1025) [S]. The widths, the Fourier action on one sampled packet, the half-plane distances, the Fubini–Study factor and det H_Z = 1 are machine-checked [V] in [`verify/phase_space_diameter.py`](../../../verify/phase_space_diameter.py) ([the phase-space-diameter script](../../method/verification/phase-space-diameter-script.md)); the separation of the three loci is the note's own result [D][V]. The note went through [round 5](../../method/review/round-5.md) of blind review (verdict B); for the reviewed version, v1.0, the adjudication records that every number reproduced under the referees' own constants and code and that every literature citation resolves.

## The packets and their labels [T]

The note works in units ℏ = λ = 1, with positions counted in a reference length λ ([the Born length](../reciprocity/born-length.md)) and momenta in ℏ/λ. A Gaussian pure state is then (§5)

```text
ψ_Z(x) ∝ exp(i Z x²/2),        Z = X + iY,   Y > 0
```

Its probability density is |ψ_Z(x)|² ∝ exp(−Yx²), so the packet can be normalized only when Y > 0, which is why the labels fill the upper half-plane [T]. The real part X enters only the phase, exp(iXx²/2). The local wavenumber of that phase is Xx, proportional to x: a chirp, in the language of signal analysis, whose frequency sweeps linearly across the pulse, so that in the packet momentum is correlated with position [T]. With d coordinates, x is a vector, the exponent is i xᵀZx/2, and Z is a complex symmetric d × d matrix with positive-definite imaginary part, a point of the Siegel upper half-space [T].

In the note's words, "in d dimensions Z lies in the Siegel upper half-space, on which Sp(2d, ℝ) acts on such states by Möbius maps [S: Ohsawa 2015; de Gosson 2013]" (§5). The unitary operators that carry out linear symplectic maps on states, which form the metaplectic representation ([unitary equivalence versus Noether symmetry](../reciprocity/unitary-equivalence.md)), send Gaussian packets to Gaussian packets, and the label moves by the corresponding fractional-linear map [T]. The same half-plane, under the same group, is the space of positive phase-space metrics compatible with ω through the parametrization H_Z of [the Siegel domain](siegel-domain.md). The note uses both readings of a label: as a packet's shape, and as the metric H_Z when it speaks of det H_Z.

## The Fourier transform as Z → −1/Z [T][V]

The transform of ψ_Z is a Gaussian integral, and completing the square in the exponent gives [T]

```text
ψ̃(p) = (2π)^(−1/2) ∫ exp(i Z x²/2) e^(−ipx) dx   ∝   exp(i (−1/Z) p²/2)
```

So the transform of the packet labelled Z is the packet labelled −1/Z, written in the momentum variable. The note: "The Fourier transform sends ψ_Z to ψ_{−1/Z} [V: for Z = 0.3 + 0.7i a numerical transform returns −0.5172 + 1.2069i = −1/Z]. This is the program's reciprocity Z → −Z⁻¹ on its modular field …, realized on wave packets" (§5; the omitted citation is [#11 §6](../../papers/broken-born-checkpoint-v2.md#6-the-modular-field)). The script samples the packet on a grid, takes a discrete Fourier transform, and reads the new label off the phase and the magnitude of the result. [The gate](../../method/verification/the-gate.md) prints:

```text
PASS  Fourier transform maps Z = 0.3 + 0.7i to -1/Z = -0.5172 + 1.2069i (numerical FFT)  [-0.517241+1.206897j]
```

The check covers one packet with one coordinate. The same map acting on the metric H(Z), for symbolic X and Y, is checked in [`verify/toy_coset.py`](../../../verify/toy_coset.py) ([reciprocity as modular inversion](modular-inversion.md#the-machine-check-d--1)).

**The fixed point.** −1/Z = Z requires Z² = −1, and the one solution in the upper half-plane is Z = i [T]. The packet ψ_i ∝ exp(−x²/2) is, in the note's words, "the one Gaussian the transform leaves unchanged, the ground state of an oscillator of length λ" (§5). The note gives Gabor's term for such pulses this way: "Gabor called Gaussian pulses "self-reciprocal" because the transform of one is a Gaussian of reciprocal sharpness [S: Gabor 1946]; Z = i is the one whose sharpness is its own reciprocal" (§5). A round-5 referee checked Gabor's text, which applies the term to Gaussian pulses of any sharpness and not to the fixed point alone, and the adjudication upheld that reading (ruling R13).

## Widths and three loci [D][V]

The note's "Three loci" paragraph starts from the widths. |ψ_Z|² ∝ exp(−Yx²) is a normal distribution of variance 1/(2Y). The transformed label −1/Z has imaginary part Y/|Z|², so the same formula gives the momentum variance [T]:

```text
Δx² = 1/(2Y)        Δp² = |Z|²/(2Y)        Δx/Δp = 1/|Z|
```

Multiplying the two widths gives Δx·Δp = |Z|/(2Y), which reaches the uncertainty bound ½ only where |Z| = Y, on the slice X = 0: the packets without a chirp are the minimum-uncertainty states [T] ([the canonical commutator and the uncertainty principle](../reciprocity/canonical-commutator.md)). The gate prints the note's checks, the first two symbolic and the third numerical, on the grid of the transform above:

```text
PASS  Delta x^2 = 1/(2Y) for psi_Z
PASS  Fourier image has Im(-1/Z) = Y/|Z|^2, so Delta p^2 = |Z|^2/(2Y) and Delta x/Delta p = 1/|Z|
PASS  numerically Delta x/Delta p = 1/|Z| for Z = 0.3 + 0.7i  [1.313064]
```

From the widths the note separates "three sets that appear in the record's statements about self-duality" (§5):

- **|Z| = 1** "is the set of states whose rectangle is square, Δx = Δp, including tilted ellipses with X ≠ 0";
- **Z = i** "is the one round state, unchanged by reciprocity";
- **det H_Z = 1** "holds at every Z, so the constraint a·ã = 1 holds everywhere on the slice X = 0, where H = diag(Y, Y⁻¹)".

The rectangle is the box Δx × Δp around the packet's [Wigner function](../reciprocity/wigner-function.md), the picture of the state on phase space, whose level curves for a Gaussian are ellipses [T]. On the circle |Z| = 1 the box is square while the ellipse inside it may be tilted; only at Z = i, where X = 0 as well, is the ellipse a circle. det H_Z = 1 is the unimodularity of the Siegel parametrization ([why the identities hold](siegel-domain.md#why-the-identities-hold-t)), which the script checks symbolically with one coordinate: `PASS  det H_Z = 1 at every Z; on X = 0, H = diag(Y, 1/Y)`. det H = 1 is not one of the record's self-duality loci: the list collects the sets that appear in the record's statements about self-duality (round-5 adjudication, author-found item 2).

**Where the record differs.** [#11](../../history/documents/checkpoint.md) identifies [the cosmological constraint a·ã = 1](../../cosmology/scale-factor-duality/cosmological-constraint.md) with the circle |Z| = 1 ([§6](../../papers/broken-born-checkpoint-v2.md#6-the-modular-field), [§10](../../papers/broken-born-checkpoint-v2.md#10-cosmology)). The note: "But a·ã = 1 holds along the whole slice, and the circle meets the slice only at Z = i; an internal audit of the record queries the identification on this ground [H2]. This note uses the slice: cosmic expansion moves along X = 0, and "self-duality" means Z = i" ([§5](../../papers/broken-born-checkpoint-v2.md#5-the-kinematic-core-and-the-compatibility-theorem)). The audit is flag 23 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md), pending; the round-5 adjudication recommends accepting it ('Recommendations to Paul'). The record's identification and the note's reading of it are on [reciprocity as modular inversion](modular-inversion.md#the-circle-z--1-and-the-constraint-aã--1).

## Distance from the self-dual packet [T][D][V]

The half-plane carries the metric ds² = (dX² + dY²)/Y², the degree-1 case of the Siegel domain's invariant metric ([the target metric](siegel-domain.md#the-target-metric)). The note states, with the tags [T][D][V] (§5):

- the distance from i to iY is |ln Y| = |ln(Δx/Δp)|, so on the slice X = 0 the logarithm of a packet's aspect ratio is its distance from the self-dual packet;
- off the slice |ln(Δx/Δp)| is smaller than the distance d(i, Z), with equality only on the slice;
- "In the convention σ_x = e^r/√2 for a squeezed vacuum, d = 2r", twice the squeezing parameter r;
- in degree d, the Siegel distance from i·1 to iy·1 is √d |ln y|.

The number also depends on which metric measures it. In the note's words, "the Fubini–Study metric that Hilbert space induces is 1/8 of the Siegel metric, so a path of Siegel length 2r has Fubini–Study length r/√2 [V]. A "distance from self-duality" is defined only once its metric and its λ are named." (§5). The Fubini–Study metric measures the distance between two nearby quantum states by how far their overlap falls below one [T].

The gate prints:

```text
PASS  half-plane distance from i to iY is |ln Y| (Y = 3, 1/7, 1e5)
PASS  off the slice |ln(Delta x/Delta p)| = |ln|Z|| is smaller than d(i, Z); equal on the slice
PASS  for Z = iY, sigma_x/sigma_p = 1/Y and the distance |ln Y| = 2r (sigma_x = e^r/sqrt 2)
PASS  Fubini-Study metric on Gaussians is 1/8 of the Siegel metric (dX^2 + dY^2)/Y^2, in both directions, on and off the slice (so Siegel length 2r = FS length r/sqrt 2)  [[0.125, 0.125, 0.125, 0.125, 0.125, 0.125]]
PASS  Siegel degree 3: distance from i1 to iy1 is sqrt(3)|ln y|; rho maps iy1 to (i/y)1
```

What the checks cover: the distances use the closed-form distance of the half-plane at sampled points; the factor 1/8 is computed numerically, from finite differences of the normalized packets on the grid, at one point on the slice and two off it, along both the X and the Y direction at each, and all six values print as 0.125; the degree-3 statement is checked at one sampled y.

## Which way the imaginary part runs

The packet label and the program's field read Im Z in opposite directions. For a packet, a larger width in position means a smaller Y, since Δx² = 1/(2Y). The program reads Im Z = g as the spacetime metric ([the modular field Z = X + iY](modular-field-z.md)), which grows as a² when the universe expands. The note meets the difference in §6: "With §5's wave-packet convention, in which Im Z falls as a⁻²", the top of the circle |Z| = 1 is a minimum of the scale factor a, while with the record's a² = Im Z it is a maximum. The round-5 adjudication records this convention dependence and finds that it does not change the withdrawal of the claim "square exactly at the bounce" ([under review](../../cosmology/scale-factor-duality/square-at-the-bounce.md)), since the |Z| = 1 geometry is excluded under either convention (ruling R14).

## What follows

- **The clock.** A comoving cell of the expanding universe grows as a in position and shrinks as 1/a in momentum, so its point moves along the imaginary axis away from Z = i: "distance 2 ln(a/a_sd) per axis, where a_sd is the scale factor at which the cell was square, advancing at the rate 2H" [D][V]. For the radiation of today's observable universe in Planck units the distance is 213.5 per axis (369.8 for the isotropic point in degree 3), which is 106.7 e-folds since the square. In the note's words, the clock "reparametrizes ln a and adds no dynamics" (§5). See [the phase-space diameter relation](../../cosmology/scale-factor-duality/phase-space-diameter.md).
- **Squeezed perturbations.** After a quantum fluctuation's wavelength leaves the Hubble radius during inflation, its state is squeezed, with the squeezing growing as the number of e-folds since then: about 50 at the end of inflation and about 100–120 today on the largest observed scales [T][S] (§5). Read as one mode's Wigner ellipse, an aspect ratio of 10⁹² is a squeezing of r = 105.9 [D][V] (§6). Squeezing values depend on the choice of canonical variables ([Grain–Vennin 2020](https://arxiv.org/abs/1910.01916) [S]). See [squeezed cosmological perturbations](../../cosmology/early-universe/squeezed-perturbations.md).
- **The square at the bounce.** The record's |Z| = 1 geometry would make the early-chat claim of a rectangle "square exactly at the bounce" exact, but on |Z| = 1 the position and momentum extents are equal at all times, which the measured aspect ratio of 10⁹² contradicts [V] (§6; [Under review: the square rectangle at the bounce](../../cosmology/scale-factor-duality/square-at-the-bounce.md)).

## Standard references

All three are cited by the phase-space-diameter note and were retrieved by live search for it [S]; the wiki adds none.

- T. Ohsawa, "The Siegel upper half space is a Marsden–Weinstein quotient: symplectic reduction and Gaussian wave packets," Lett. Math. Phys. (2015), [arXiv:1504.03963](https://arxiv.org/abs/1504.03963) [S] — Gaussian packets as points of the Siegel upper half-space.
- M. A. de Gosson, "Symplectic and Hamiltonian deformations of Gabor frames" (2013), [arXiv:1305.1025](https://arxiv.org/abs/1305.1025), Appendix A [S] — the action of the symplectic group on Gaussians.
- D. Gabor, "Theory of communication. Part 1: The analysis of information" (1946) [S] — Gaussian pulses as "self-reciprocal".

## Used by

- [The phase-space diameter relation](../../cosmology/scale-factor-duality/phase-space-diameter.md) — the aspect ratio of the universe's radiation as a distance from Z = i, and the clock.
- [Reciprocity as modular inversion Z → −Z⁻¹](modular-inversion.md) — the inversion realized on wave packets; the three loci beside the record's |Z| = 1 identification.
- [Squeezed cosmological perturbations](../../cosmology/early-universe/squeezed-perturbations.md) — a mode's squeezing as a distance from the round packet.
- [Under review: the square rectangle at the bounce](../../cosmology/scale-factor-duality/square-at-the-bounce.md) — the |Z| = 1 geometry that would make the chat claim exact, and why it fails.
- [The Born length λ](../reciprocity/born-length.md) — the unit in which Z = i is the self-dual packet; reciprocity maps with two Born lengths differ by a squeeze.

## Sources

- [`wiki/papers/phase-space-diameter.md` §5](../../papers/phase-space-diameter.md#5-what-reciprocity-adds-invariant-area-inverted-shape) — the packets ψ_Z and the Möbius action [S]; the Fourier transform as Z → −1/Z [V]; the fixed point and Gabor's "self-reciprocal"; the widths and the three loci [D][V]; the slice as the note's reading; the distance and its dependence on the metric [T][D][V]; the clock [D][V]; squeezed perturbations [T][S].
- [`wiki/papers/phase-space-diameter.md` §6](../../papers/phase-space-diameter.md#6-where-the-rectangle-is-square) — the squeezed-mode reading (r = 105.9), the convention in which Im Z falls as a⁻², and the failure of the |Z| = 1 geometry.
- [`wiki/papers/phase-space-diameter.md`](../../papers/phase-space-diameter.md) References — Ohsawa 2015, de Gosson 2013, Gabor 1946, Grain–Vennin 2020 [S].
- [`verify/phase_space_diameter.py`](../../../verify/phase_space_diameter.py) — the checks of the [note's §5](../../papers/phase-space-diameter.md#5-what-reciprocity-adds-invariant-area-inverted-shape), printed as quoted above.
- [`review/round5-adjudication.md`](../../../review/round5-adjudication.md) 'Verdict', 'Rulings' R13 and R14, author-found item 2, 'Recommendations to Paul' — every number of v1.0 reproduced and every citation resolved; Gabor's term; the convention of the apex; the framing of the loci; the recommendation on flag 23.
- [`wiki/papers/broken-born-checkpoint-v2.md` §6](../../papers/broken-born-checkpoint-v2.md#6-the-modular-field), [§10](../../papers/broken-born-checkpoint-v2.md#10-cosmology) — Z → −Z⁻¹ on the modular field; a·ã = 1 identified with the |Z| = 1 locus.
- [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md) item 23 — the audit's query on that identification, pending.
