---
title: "Reciprocity as modular inversion Z → −Z⁻¹"
weight: 30
status: alive
description: "Born reciprocity acts on the modular field by the Möbius inversion Z → −Z⁻¹ with fixed point Z = i; on the vacuum slice it is scale-factor duality g → g⁻¹, and the circle |Z| = 1 is identified with the cosmological constraint a·ã = 1. On Gaussian wave packets the Fourier transform acts the same way, and there |Z| = 1 is the set of square rectangles."
provenance: [D]
sources:
  - "papers/broken-born-checkpoint-v2.md §6"
  - "notes/geometric-core.md §C"
  - "notes/geometric-core.md §F"
  - "notes/broken-born-program-v1.md §4"
  - "notes/broken-born-theory.md 'Addendum (v0.3, overnight): axiom correction and the modular core'"
  - "notes/broken-born-theory.md §2"
  - "notes/broken-born-theory.md §6"
  - "papers/broken-born-checkpoint-v2.md §4"
  - "papers/broken-born-checkpoint-v2.md §10"
  - "papers/broken-born-checkpoint-v2.md §11"
  - "papers/broken-born-checkpoint-v2.md App. A item 6"
  - "papers/reciprocity-toy-models.md §2"
  - "notes/toy-lagrangian.md 'Chunk 1 results'"
  - "notes/toy-lagrangian.md 'Chunk 2 results'"
  - "notes/x-classification.md §3"
  - "verify/toy_coset.py"
  - "review/wiki-build-flags.md items 23, 39"
  - "review/wiki-build-checks/self_dual_locus.py"
  - "review/wiki-build-checks/rho_parity.py"
  - "notes/beta-coefficients.md §1"
  - "papers/broken-born-checkpoint-v2.md §7.3"
  - "papers/phase-space-diameter.md §5"
  - "papers/phase-space-diameter.md §6"
  - "verify/phase_space_diameter.py"
  - "review/round5-adjudication.md 'Rulings' R14"
  - "review/round5-adjudication.md 'Recommendations to Paul'"
---

*Modular inversion is the map Z → −Z⁻¹, "take minus the reciprocal", applied to [the modular field Z](/wiki/phase-space/modular-field/modular-field-z). The program shows that [Born reciprocity](/wiki/phase-space/reciprocity/born-reciprocity), the quarter-turn of the position–momentum plane that the Fourier transform performs on a wavefunction, acts on Z in exactly this way. The map leaves the point Z = i unchanged, and that point is the program's self-dual vacuum. On the vacuum slice the map sends the metric g to its inverse, which for a uniformly scaled metric turns the scale factor a into 1/a; the circle |Z| = 1 is identified with the program's relation a·ã = 1 between our scale factor and that of the [conjugate description](/wiki/program/conjugate-universe), an identification queried in flag 23 of `review/wiki-build-flags.md`. On [Gaussian wave packets](/wiki/phase-space/modular-field/gaussian-states) the Fourier transform acts on the packet's shape parameter by the same map; there the circle |Z| = 1 holds the packets as wide in position as in momentum, while a·ã = 1 holds on the whole slice X = 0, the reading that the phase-space-diameter note adopts. The same quarter-turn matrix generates the S-duality of electric and magnetic charges. The claim is derived; for one coordinate (d = 1) a script checks it symbolically, and no script checks the general case.*

**Status:** Alive — derived [D] ([#11](/wiki/history/documents/checkpoint) §6; [calc note #5](/wiki/history/documents/field-equation-notes) §C, "[D — structural]") — the d = 1 case is machine-checked symbolically in `verify/toy_coset.py` ([the toy-model scripts](/wiki/method/verification/toy-model-scripts)); general d rests on the argument alone, and the cosmological reading is structural. The realization on Gaussian wave packets is literature [T], checked numerically for one packet [V] in `verify/phase_space_diameter.py` ([the phase-space-diameter script](/wiki/method/verification/phase-space-diameter-script)).

## The claim

#11 §6: "**ρ: Z → −Z⁻¹** (Möbius; d = 1 check), fixed point Z = i; at X = 0 it is scale-factor duality g → g⁻¹, and the cosmological constraint a·ã = 1 (§10) is the |Z| = 1 locus." (On the |Z| = 1 locus, see flag 23 in `review/wiki-build-flags.md`.)

## Background: inversion of the half-plane [T]

For d = 1 [the Siegel domain](/wiki/phase-space/modular-field/siegel-domain) is the upper half-plane, on which the group SL(2, ℝ) acts by z → (αz + β)/(γz + δ). The matrix [[0, 1], [−1, 0]] gives z → 1/(−z) = −1/z. In polar form z = r e^{iθ} goes to (1/r) e^{i(π − θ)}: the distance from the origin is inverted and the point is reflected across the imaginary axis. The map therefore exchanges the inside and the outside of the unit semicircle |z| = 1, carries that semicircle onto itself, and leaves the single point z = i fixed. In the theory of modular forms the same map is the generator usually called S of the [modular group SL(2, ℤ)](/wiki/electric-magnetic-duality/modular-group#reciprocity-as-s-on-the-half-plane).

For general d the same matrix with unit blocks acts on complex symmetric matrices as Z → −Z⁻¹, and Z = i·1, i times the unit matrix, is again a fixed point, since −(i·1)⁻¹ = i·1.

## How reciprocity acts on Z

### The quarter-turn

Born reciprocity is the map ρ: (x, p) → (p, −x), the matrix [[0, 1], [−1, 0]]; the Fourier transform implements it on wavefunctions ([the Fourier transform](/wiki/phase-space/reciprocity/fourier-transform)). The lab notebook records its action on the three structures of [Born geometry](/wiki/phase-space/born-geometry/born-structures): "R preserves ω (it is symplectic), preserves H (it is orthogonal), and **flips the sign of η**, hence flips J and K while preserving I" (#1 §2, [D]; there H is the unit metric). Postulate [P3](/wiki/program/postulates/p3-reciprocity) makes the action invariant under "the Born rotation generated by I = ω⁻¹H" (#11 §4). Being symplectic, ρ maps ω-compatible metrics to ω-compatible metrics, so it moves the points of the Siegel domain by one of the domain's Möbius maps.

### The derivation as the sources give it

Calc note #5: "**Born reciprocity acts as Z → −Z⁻¹** (Möbius action of the I-rotation; d = 1 check: matrix [[0,1],[−1,0]] gives Z → −1/Z). Fixed point Z = i: the self-dual vacuum of the earlier turns, now as modular geometry." (§C)

The argument has two steps. ρ is the element [[0, 1], [−1, 0]] of the [symplectic group](/wiki/phase-space/reciprocity/symplectic-form), and the symplectic group acts on the domain by Möbius maps; so ρ acts by the Möbius map of that matrix, which is the inversion. The note works the d = 1 case explicitly. It does not say which "earlier turns" it means; calc note #6 uses "turn" for an exchange of the development conversation on claude.ai (§3), and no earlier document uses the phrase "self-dual vacuum".

### The machine check (d = 1)

`verify/toy_coset.py` takes the d = 1 parametrization H(Z) = [[Y + X²/Y, X/Y], [X/Y, 1/Y]] and checks symbolically, for symbolic X and Y, that ρᵀH(Z)ρ equals H(Z′), where Z′ = −1/Z is written out in components, X′ = −X/(X² + Y²) and Y′ = Y/(X² + Y²). [The gate](/wiki/method/verification/the-gate) prints:

```text
PASS  rho acts on Z as Z -> -1/Z with fixed point Z = i
```

The script's comment adds that "A rho-fixed vacuum needs rho^T H rho = H (only Z = i, i.e. H = 1)". The [toy-model note](/wiki/symmetry-breaking/toy-models) states the result as "ρ acts as Z → −1/Z and K(φ) → K(φ + π) = −K(φ)" (§2), and the worklog as "ρ acts as Z → −1/Z on H and as K → −K at H = 1" ('Chunk 1 results'). See [model I vacua](/wiki/symmetry-breaking/toy-models/coset-model/vacua).

For d > 1 no document writes the map out and no script checks it. Battery test T2 checks the parametrization H_Z at d = 4 but not the action of ρ ([the verification battery](/wiki/method/verification/battery)). `verify/phase_space_diameter.py` evaluates −Z⁻¹ at one isotropic point of degree 3, sending iy·1 to (i/y)·1; that checks the inversion's arithmetic there, not that ρ acts by it ([Gaussian wave packets on the Siegel half-plane](/wiki/phase-space/modular-field/gaussian-states#distance-from-the-self-dual-packet-tdv)). The general statement rests on the Möbius-action argument [D].

### On wave packets: the Fourier transform

The phase-space-diameter note (`papers/phase-space-diameter.md` v1.1) realizes the map on quantum states (§5, [T][V]). In units ℏ = λ = 1, a Gaussian wave packet ψ_Z(x) ∝ exp(iZx²/2) is labelled by a point Z = X + iY of the upper half-plane, and the Fourier transform, which carries out ρ on wavefunctions ([the Fourier transform as a phase-space rotation](/wiki/phase-space/reciprocity/fourier-transform)), sends ψ_Z to ψ_{−1/Z}. The note: "This is the program's reciprocity Z → −Z⁻¹ on its modular field …, realized on wave packets" (the omitted citation is #11 §6). Its script transforms one packet numerically:

```text
PASS  Fourier transform maps Z = 0.3 + 0.7i to -1/Z = -0.5172 + 1.2069i (numerical FFT)  [-0.517241+1.206897j]
```

The labelling of Gaussian states by the Siegel upper half-space, with the symplectic group acting by Möbius maps in any number of dimensions, is literature (Ohsawa 2015; de Gosson 2013 [S], cited by the note), and the script's check covers one packet with one coordinate. The packets and the program's field read the imaginary part in opposite directions: a packet that widens in position has a smaller Y, while the program reads Im Z = g as a metric that grows with the scale factor (round-5 ruling R14). The labelling, the widths, the three loci and the distance from Z = i are on [Gaussian wave packets on the Siegel half-plane](/wiki/phase-space/modular-field/gaussian-states).

## What follows

### The fixed point: the self-dual vacuum Z = i

At Z = i the metric is H = 1, the unit metric of the lab notebook's units, in which a [reference length λ](/wiki/phase-space/reciprocity/born-length) and momentum ε = ℏ/λ are scaled out (#1 §2). Position and momentum directions are measured alike there, and ρ leaves the metric unchanged. On wave packets the same point labels the ground state of an oscillator of length λ, "the one Gaussian the transform leaves unchanged" (phase-space-diameter note §5). According to the note, the program's action is invariant under the rigid Sp(2d, ℝ), which moves the self-dual point Z = i anywhere, so the action singles out no Born length (§5 [D]; [the Born length λ](/wiki/phase-space/reciprocity/born-length#the-programs-action-fixes-no-λ)).

The metric is not the whole vacuum, though. In the toy model the vacuum also carries a real structure K, the order parameter, and ρ sends K to −K: "No vacuum is ρ-invariant" (worklog, 'Chunk 1 results'), and the gate prints `PASS  no vacuum is rho-invariant: at H = 1 a compatible K with rho^-1 K rho = K must vanish`. In the toy model, then, reciprocity is broken at the self-dual point of the metric by [the order parameter](/wiki/symmetry-breaking/order-parameter), not by the metric. Even that breaking has physical content only once matter couples to the sign of K, because the twisted element ρ∘(K → −K) maps the reference vacuum to itself (toy-model note §2; [the twisted element](/wiki/symmetry-breaking/twisted-element)).

At the self-dual point ρ is also one element of a continuous symmetry. In the Siegel domain the maps fixing Z = i form U(d), U(1) at d = 1, and ρ is the quarter-turn among them [T]. The worklog found the same in its models: "At the self-dual point, Born reciprocity is never the whole symmetry. It is one element of a continuous U(1): the coset model: the U(1) stabilizer of H that rotates K" ('Chunk 2 results'). #11 draws the consequence in its [P2′](/wiki/program/postulates/p2-prime) refinement: "with only ω rigid, ρ sits inside a continuous U(1), and the polarization is a Goldstone angle rather than a discrete choice [D][V]" (§4; [the polarization as a Goldstone angle](/wiki/symmetry-breaking/goldstone-angle)).

### On the vacuum slice: g → g⁻¹

On the slice X = 0 the field is Z = iY, and −Z⁻¹ = −(iY)⁻¹ = iY⁻¹: the map sends Y = g to its inverse. This is #11's "at X = 0 it is scale-factor duality g → g⁻¹". If g is the unit metric scaled by a², g = a²·1, its inverse is a⁻²·1, so the scale factor a goes to 1/a: the a → 1/a symmetry that string cosmology calls scale-factor duality [T] ([scale-factor duality](/wiki/cosmology/scale-factor-duality)).

The same algebra shows which vacua the map fixes. A vacuum ⟨Z⟩ = i·g (#6 §3) goes to i·g⁻¹, so it is left unchanged only if g = g⁻¹, which for a positive-definite metric means g = 1: the fixed point Z = i.

### The circle |Z| = 1 and the constraint a·ã = 1

Calc note #5: "The cosmological constraint a·ã = 1 is the |Z| = 1 self-dual circle — the minisuperspace duality was the shadow of this modular action." (§C)

The constraint itself comes from the rigidity of ω. #11 §10: "**Constraint [D]:** ω-rigidity fixes the comoving phase-space cell: a·ã = 1 (ℏ does not run) — the |Z| = 1 self-dual locus." The lab notebook derives it: each mode occupies "(aã)³ × (comoving cell) = ℏ³. Hence a ã = const ≡ 1" (#1 §6). See [the cosmological constraint a·ã = 1](/wiki/cosmology/scale-factor-duality/cosmological-constraint).

At d = 1 the inversion carries the unit semicircle onto itself, each point reflected across the imaginary axis, with Z = i the one point left in place [T]. The documents identify a·ã = 1 with this circle without writing out how the two scale factors a and ã sit inside Z; the identification is a structural reading ([D — structural] in #5 §C, [D] in #11 §10). #11's audit of founding suppositions records the outcome for supposition 6, "Conjugate universe shrinks as ours expands — **promoted to theorem** (a·ã = 1 from ℏ-rigidity; the |Z| = 1 locus)" (App. A item 6; [founding suppositions](/wiki/program/founding-suppositions)). Flag 23 in `review/wiki-build-flags.md` queries the identification of a·ã = 1 with the |Z| = 1 locus. On the slice X = 0 the metric is H_Z = diag(Y, Y⁻¹). The flag reads the position block as g = a² = Y and the momentum block as ã² = Y⁻¹; with that reading a·ã = 1 is the statement det H = 1 and holds along the whole imaginary axis, while the circle |Z| = 1 meets that axis only at Z = i. The flag's executed check prints `a*a~ = 1 for every Y > 0; |Z| = 1 only at Y = 1` (`review/wiki-build-checks/self_dual_locus.py`). Either the identification needs a different reading of a and ã, or it is a slip. The flag asks for one ruling covering #11 §6 and §10, calc note #5 §C, the lab notebook's v0.3 addendum and `HANDOFF.md` §2, and it awaits Paul's ruling.

**The phase-space-diameter note's reading.** The note takes up the identification from the side of wave packets (§5, [D][V]). For a Gaussian packet the widths satisfy Δx/Δp = 1/|Z|, so three sets that appear in the record's statements about self-duality are distinct: |Z| = 1 is the set of square rectangles, Δx = Δp, including tilted ellipses with X ≠ 0; Z = i is the one round state, unchanged by reciprocity; and det H_Z = 1 holds at every Z, so that a·ã = 1 holds on the whole slice X = 0, where H = diag(Y, Y⁻¹) ([Gaussian wave packets on the Siegel half-plane](/wiki/phase-space/modular-field/gaussian-states)). The note: "But a·ã = 1 holds along the whole slice, and the circle meets the slice only at Z = i; an internal audit of the record queries the identification on this ground [H2]. This note uses the slice: cosmic expansion moves along X = 0, and "self-duality" means Z = i." Its [H2] is the flags file.

In §6 the note returns to the identification as the likeliest origin of the early-chat claim that the universe's position–momentum rectangle is "square exactly at the bounce", a reading it labels [D, inference]. Along the circle, written Z = tanh s + i sech s, Im Z peaks at Z = i. With the record's a² = Im Z the peak is the maximum of a, the turnaround, and H is round there (with the wave-packet convention, in which Im Z falls as a⁻², the same point is a minimum of a, a literal bounce). Under the identification, "square exactly at the bounce" and "a clock measuring distance from self-duality" both follow, with the bounce at the turnaround. The note finds that it fails in two ways [V]:

- on |Z| = 1 the position and momentum extents are equal at all times (H_xx = H_pp = 1/Y), which contradicts the measured aspect ratio of 10⁹²;
- read instead as the squeeze of H along the circle, the 10⁹² requires X ≈ 1 today, a homogeneous [momentum graviton](/wiki/gravity/momentum-graviton) whose energy density exceeds the critical density by a factor of order (M_X/H₀)² ≈ 10⁶¹ for the smallest mass that [the laboratory bound on X's range](/wiki/gravity/momentum-graviton/range-bound) allows.

The gate prints the corresponding checks:

```text
PASS  the record's |Z| = 1 path Z = tanh s + i sech s: |Z| = 1, Im Z peaks at s = 0 (Z = i)
PASS  on |Z| = 1, H_xx = H_pp = 1/Y: the position and momentum extents are equal at all times
PASS  an order-one X today: (M_X/H0)^2 = 1.3e61 for M_X c^2 = 5.2 meV  [1.327e+61]
```

The claim is withdrawn ([Obituary: the square rectangle at the bounce](/wiki/cosmology/scale-factor-duality/square-at-the-bounce)). On flags 23 and 24 the round-5 adjudication tells Paul that "the note's §5 and §6 support accepting both" ('Recommendations to Paul'). The wiki records that recommendation and does not rule on either flag; both await Paul's ruling.

### The same matrix in charge space

#11 §11.3, a section tagged "[D — structural; math T]": "S-duality acts on the complexified coupling by τ_c → −1/τ_c, generated by the same [[0,1],[−1,0]] rotation as Born's ρ and our Z → −Z⁻¹: the third appearance of one matrix in this program." The charge lattice of electric and magnetic charges is itself a symplectic space, and choosing which charges count as electric is choosing a [Lagrangian polarization](/wiki/phase-space/reciprocity/lagrangian-polarizations) of it ([the symplectic charge lattice](/wiki/electric-magnetic-duality/symplectic-charge-lattice); [S-duality](/wiki/electric-magnetic-duality/s-duality)).

Whether the two polarizations belong together is a conjecture [O], open item 8: #11 asks whether the phase-space polarization and the charge-lattice polarization "are components of one enlarged modular structure", the program's analogue of T- and S-duality sitting together inside U-duality in string theory ([Open: one modular structure for both polarizations (OP8)](/wiki/electric-magnetic-duality/unified-modular-structure)).

## Scope and caveats

- **Explicit only at d = 1.** The physical case is d = 4; there the map follows from the general Möbius action, which no script checks.
- **Positive metrics only.** Like the Siegel parametrization itself, the statement concerns positive (Euclidean) H; Lorentzian signature is open item 3 ([Open: Lorentzian dressing](/wiki/phase-space/born-geometry/lorentzian-dressing)).
- **A second action on the spin-2 sector.** For the program's two spin-2 [frames](/wiki/gravity/spin-2-fields/vielbein-formulation), [calc note #8](/wiki/history/documents/field-equation-notes) §1 and #11 §7.3 state reciprocity as their exchange, e ↔ f, the form [the palindrome](/wiki/gravity/palindromic-branch/palindrome#how-reciprocity-acts-the-frame-exchange) uses. Linearized at the fixed point Z = i, the inversion sends a fluctuation x + ih of Z to −(x + ih), so the metric's fluctuation h changes sign together with X's, while the frame exchange leaves the massless combination of the frames unchanged. The documents state both actions and do not show how one becomes the other for the massless mode (flag 39 in `review/wiki-build-flags.md`; `review/wiki-build-checks/rho_parity.py`). The flag's audit found the graviton's parity right under the frame exchange and rated the flag as depending on which action is meant ([two actions of reciprocity](/wiki/gravity/momentum-graviton/spectrum-and-parity#two-actions-of-reciprocity)).
- **A structural cosmology.** The |Z| = 1 reading of a·ã = 1 is stated, not derived through an explicit map from the scale factors to Z. Read with g = a² = Y and ã² = Y⁻¹ on the slice X = 0, the two loci differ: flag 23 in `review/wiki-build-flags.md` finds a·ã = 1 on the whole imaginary axis and |Z| = 1 only at Z = i (`review/wiki-build-checks/self_dual_locus.py`). The phase-space-diameter note uses the slice, and finds that the |Z| = 1 geometry contradicts the measured aspect ratio of the universe's radiation (§5, §6). The flag awaits Paul's ruling.

## History

- **Lab notebook, v0.3 addendum.** The modular field arrives with "Born reciprocity = Z → −Z⁻¹ with self-dual point Z = i, and the cosmological constraint a·ã = 1 as the |Z| = 1 locus" ([the lab notebook](/wiki/history/documents/lab-notebook); see flag 23 in `review/wiki-build-flags.md`).
- **Calc note #5** gives the derivation (§C) and lists "the modular unification (reciprocity = Z → −Z⁻¹, cosmological duality = |Z| = 1)" among the night's results (§F; see flag 23 in `review/wiki-build-flags.md`).
- **#9 §4**: "Reciprocity = Z → −Z⁻¹ (Möbius action; d = 1 matrix check), fixed point Z = i. At X = 0 it sends g → g⁻¹: scale-factor duality."
- **#11 §6** is the current statement.
- **The toy model** (2026-10-19) put the d = 1 case into the gate through `verify/toy_coset.py`.
- **The phase-space-diameter note** (v1.1, 2026-10-26) realized the map on Gaussian wave packets, separated |Z| = 1, Z = i and det H = 1, and found the |Z| = 1 geometry excluded as a reading of the early-chat rectangle (§5, §6); `verify/phase_space_diameter.py` checks the Fourier action for one packet.

## Sources

- `papers/broken-born-checkpoint-v2.md` §6 — the claim, among the identifications tagged [D].
- `notes/geometric-core.md` §C, §F — the derivation, the d = 1 matrix check and the |Z| = 1 circle; the modular unification in the closing summary.
- `papers/broken-born-checkpoint-v2.md` §4, §10 — P3 and the P2′ refinement; a·ã = 1 as the |Z| = 1 locus [D].
- `papers/broken-born-checkpoint-v2.md` §11 — the same matrix generating S-duality; the OP8 conjecture.
- `papers/broken-born-checkpoint-v2.md` App. A item 6 — supposition 6 "promoted to theorem".
- `notes/broken-born-theory.md` §2, §6, v0.3 addendum — ρ on (ω, η, H) and the units; the derivation of a·ã = 1; the introduction of Z → −Z⁻¹.
- `notes/broken-born-program-v1.md` §4 — the same statement in #9.
- `notes/x-classification.md` §3 — the vacuum ⟨Z⟩ = i·g; "turn" for an exchange of the development conversation.
- `papers/reciprocity-toy-models.md` §2 — ρ on Z and on K in model I; the twisted element.
- `notes/toy-lagrangian.md` 'Chunk 1 results', 'Chunk 2 results' — no ρ-invariant vacuum; ρ inside the U(1) stabilizer at the self-dual point.
- `verify/toy_coset.py` — the symbolic check of Z → −1/Z with fixed point Z = i, and of the absence of a ρ-invariant vacuum.
- `review/wiki-build-flags.md` item 23 and `review/wiki-build-checks/self_dual_locus.py` — the query on the identification of a·ã = 1 with |Z| = 1, with its executed check; awaiting Paul's ruling.
- `review/wiki-build-flags.md` item 39 and `review/wiki-build-checks/rho_parity.py` — the inversion against the frame exchange on the spin-2 sector (`notes/beta-coefficients.md` §1; #11 §7.3), with its executed check and audit verdict; awaiting Paul's ruling.
- `papers/phase-space-diameter.md` §5 — the inversion realized on Gaussian wave packets [T][V]; the three loci [D][V]; the slice X = 0 as the note's reading; the program's action fixes no λ [D].
- `papers/phase-space-diameter.md` §6 — the |Z| = 1 identification as the likeliest origin of "square exactly at the bounce" [D, inference], and its two failures [V].
- `verify/phase_space_diameter.py` — the numerical Fourier check for one packet; the |Z| = 1 path, H_xx = H_pp on it, and the energy factor of an order-one X.
- `review/round5-adjudication.md` 'Rulings' R14 — the convention dependence of the apex of |Z| = 1; 'Recommendations to Paul' — the note's §5 and §6 support accepting flags 23 and 24.
