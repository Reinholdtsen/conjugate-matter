---
title: "Reciprocity on a closed space"
weight: 110
status: alive
description: "On a closed position space the global Fourier exchange of position and momentum fails, since one spectrum is continuous and the other discrete, while the local exchange holds to (2/3)(σ/R)²; on T*S³ only the position polarization is integrable (the critic's single-agent result); no product of a closed position space and a closed momentum space is a phase space, and the non-product Gr̃(2,5) needs a momentum radius far above the Planck energy."
provenance: [D, V]
sources:
  - "notes/closed-universe.md §5"
  - "notes/closed-universe.md §2"
  - "notes/closed-universe.md §1"
  - "notes/closed-universe.md §9"
  - "notes/closed-universe.md §10"
  - "verify/closed_universe.py 'E. Momentum space and reciprocity'"
  - "verify/closed_universe.py 'Anchors (independent of the investigation)'"
  - "review/closed-universe/README.md"
  - "review/wiki-build-flags.md item 47"
  - "papers/broken-born-checkpoint-v2.md §3"
  - "papers/phase-space-diameter.md §8.1"
  - "papers/phase-space-diameter.md §8.2"
  - "notes/broken-born-theory.md §2"
---

*Born reciprocity exchanges position and momentum, and in flat space the [Fourier transform](/wiki/phase-space/reciprocity/fourier-transform) carries it out exactly, turning a waveform into its spectrum and back. On a closed space, finite in extent like the surface of a sphere, the two descriptions stop matching as wholes: position is still continuous, but momentum becomes discrete, as a waveform on a ring has a line spectrum, so no exact map exchanges them. The exchange still holds for any wave packet much smaller than the universe, with a relative error of order the square of the packet's size over the curvature radius. The closed-universe note of 2026-10-27 adds two results of geometry. On the phase space of a closed universe, only the program's position-like polarization fits together consistently across the whole space, so the mirror polarization has no global form if the program requires that fit. And a closed position space times a closed momentum space cannot be a phase space; one compact phase space that treats position and momentum symmetrically does exist, but it needs a momentum scale far above the Planck energy.*

**Status:** Alive — computed, not reviewed — [D][V] for the failure of the global exchange, the local accuracy and the compact phase spaces; [D][V] for integrability, from the note's critic alone and not independently verified, as the note marks it; Gr̃(2,5) [S][V], a construction of the critic alone (one agent); the prior art [S], found by a verifier. Every number is recomputed in section E of `verify/closed_universe.py` ([the closed-universe script](/wiki/method/verification/closed-universe-script)). The note's results were checked by independent verifiers and a completeness critic and have not been reviewed (`notes/closed-universe.md` header). The scope note on #11 §3 is flag 47 in `review/wiki-build-flags.md`, which awaits Paul's ruling.

## The setting

The [closed-universe note](/wiki/cosmology/scale-factor-duality/closed-universe) asks what follows if the universe's space is closed, curvature k = +1, so that position space is a three-sphere S³ of radius R, or a space with the same local geometry and a different topology (§1). Phase space is then the cotangent bundle T\*S³: over each point of S³ sits the [momentum fibre](/wiki/phase-space/reciprocity/momentum-fibers), the space of momenta available there [T]. The note's §5 asks what is left of [Born reciprocity](/wiki/phase-space/reciprocity/born-reciprocity), ρ: (x, p) → (p, −x), on that space.

## The global Fourier map fails [D][V]

**Why [T].** A waveform on an infinite line has a continuous spectrum, and the Fourier transform maps functions on the line to functions on a line of the same kind. A waveform on a ring, a periodic signal, has a line spectrum: only whole numbers of wavelengths fit around the ring, and the transform becomes a Fourier series, which maps functions on a circle to sequences.

**On a closed space.** On S³ or a torus, position has a continuous spectrum and momentum a discrete one, so no unitary operator exchanges them (§5). The momentum spectrum on S³ is √(ν² − 1)·ħ/R, with ν a whole number, so the allowed momenta are spaced by about ħ/R ([how small momentum space gets](/wiki/cosmology/scale-factor-duality/closed-universe#how-small-momentum-space-gets)). The script's anchors check the eigenvalues and their multiplicities on S³ against the textbook spectrum of the Laplacian.

**The record's sentence.** #11 §3 states: "Quantum kinematics is exactly invariant under ρ: (x,p) → (p,−x); the Fourier transform implements it unitarily [1†, 2†]." The sentence is true on ℝ^d, which #11's flat cosmology assumes; once closure is adopted it needs a scope (§5; flag 47). The flag's audit found the point to depend on a reading: "Not an error under the record's flat assumption; an error once k = +1."

## The local exchange survives [D][V]

A wave packet of width σ is exchanged by the flat transform to relative accuracy (2/3)(σ/R)². That is 3.5×10⁻⁵⁵ at σ = 1 m for |Ω_k| = 10⁻², a curvature larger than the data allow for a closed universe (§5). The script computes the mean squared momentum of a Gaussian packet of geodesic width σ on a sphere of radius R and finds the correction coefficient −2/3, both by quadrature and from the Gaussian moments. For any laboratory or astrophysical system, the flat statement of reciprocity holds.

## Only the position polarization is integrable [D][V]

The note marks this result "from the critic alone, not independently verified" (§5).

**Polarizations and integrability [T].** A [polarization](/wiki/phase-space/reciprocity/lagrangian-polarizations) is a choice, at each point of phase space, of a Lagrangian plane: half of the directions, on which the symplectic form vanishes. A field of planes is integrable when the planes fit together as the tangent planes of a family of surfaces that fill the space; by Frobenius's theorem this holds exactly when the bracket of any two vector fields lying in the planes lies in the planes again. The vertical plane at each point, tangent to the momentum fibre, is always integrable on a cotangent bundle, its surfaces being the fibres themselves.

**The program's family.** The program's U(1) family of polarizations is L_θ = e^{θI}(vertical): the vertical plane rotated by the angle θ, with I the quarter-turn of each tangent plane of phase space that the vacuum's metric defines (the wiki's reading). This assumes the Levi-Civita splitting in which H = diag(g, g⁻¹) (§5). θ = 0 is what the note calls the position polarization, and θ = π/2 the mirror momentum polarization of [P5](/wiki/program/postulates/p5-spontaneous-selection).

**The result** (§5):

- Every L_θ is Lagrangian.
- On T\*S³, the component of [L_θ, L_θ] outside L_θ is ℓ²p·sin³θ/R², the curvature of S³ times sin³θ, with ℓ the length scale of the rotation (the wiki's reading of the script's ell) and p the momentum.
- So only θ = 0, and θ = π, which is the same plane, is integrable. Every tilt, including the mirror polarization θ = π/2, fails the Frobenius condition.
- On the flat three-torus T³, every θ is integrable.
- The size of the effect is (L/R₀)² = 5.309×10⁻⁵⁵ at L = 1 m for |Ω_k| = 10⁻², R₀ being the curvature radius today.

**Consequences** (§5):

- Closure cuts the Born rotation's U(1) on integrable polarizations down to Z₂, the rotations by 0 and by π, which both return the position polarization.
- If the [section condition](/wiki/symmetry-breaking/section-condition) (#1 §2) requires integrability, P5's mirror vacuum has no global realization in a closed universe. The section condition's consistency on curved backgrounds was already open in the record ([Open: the section condition on curved backgrounds](/wiki/symmetry-breaking/section-condition#open-the-section-condition-on-curved-backgrounds)).
- The record does not state that requirement. If polarization fields that are not integrable are allowed, the energy cost of the mirror is not computed [O]. The note's open list includes the related energy splitting between the ±K_ref polarizations that closure induces (§9), ±K_ref being the two vacua of the toy models that ρ exchanges ([locality from an (H, K)-built coupling](/wiki/symmetry-breaking/matter-coupling)).

## Compact phase spaces [D][V]

**No product works.** No product X × M is symplectic when X is a k = +1 position space, S³ or any spherical space form, and M is any closed 3-manifold. In the product the second cohomology comes from M alone, so the cube of the symplectic form's class would be pulled back from the sixth cohomology of M, which vanishes; a symplectic form on a six-dimensional closed space needs that cube to be nonzero (§5). So Born's position sphere times a momentum sphere cannot be a phase space. Born 1938 had paired the radius of Einstein's closed universe with a momentum-space hypersphere of radius b fixed from the classical electron radius (§2; [Born's papers](/wiki/phase-space/reciprocity/born-reciprocity#borns-papers)).

**A non-product one exists [S][V; the critic's construction, one agent].** Gr̃(2,5) = SO(5)/(SO(2)×SO(3)), the Euclidean Snyder–de Sitter orbit, is a compact Kähler space, and Born reciprocity is the inner SO(5) automorphism that exchanges its position and momentum generators (Mignemi and Štrajn 2015, arXiv:1501.01447 [S]; §5). It belongs to the Snyder lineage of [curved momentum space](/wiki/phase-space/reciprocity/curved-momentum-space). The script checks that Gr̃(2,5) is the quadric Q₃ in CP⁴, on which the Fubini–Study form is non-degenerate, and that the automorphism maps X to P and P to −X. Its existence corrected an analyst's claim that "a doubly compact reciprocal phase space must be torus-like" (§10).

**Its reciprocity length.** λ = √(Rħ/κ), with κ the momentum-sphere radius. With κ = m_P·c this is √(R₀ l_P) = 1.489×10⁻⁴ m at |Ω_k| = 10⁻², which the diameter note's two tests exclude (§5): as the [Born length](/wiki/phase-space/reciprocity/born-length) it gives a [maximum force](/wiki/conjugate-relativity/maximum-force) that every atom exceeds, and as the range of [X](/wiki/gravity/momentum-graviton/range-bound) it is excluded by torsion balances ([Obituary: the self-dual length as a program scale](/wiki/cosmology/scale-factor-duality/self-dual-length-obituary)).

**The momentum radius it needs.** To meet the program's own Born-length bounds, the momentum-sphere radius κc must be at least (§5):

- 46.5 E_P today, from X's range of 37.7 μm, E_P being the Planck energy;
- 1.72×10¹¹ E_P today, from #13's maximum force, which the script evaluates as λ ≤ 6.195×10⁻¹⁰ m;
- 4.1×10⁴ and 1.5×10¹⁴ E_P respectively at the turnaround.

The script evaluates "today" at |Ω_k| = 1.13×10⁻³, the 95% bound given closure, and "at the turnaround" at R_max = 1.174×10⁵ Gpc ([how big position space gets](/wiki/cosmology/scale-factor-duality/closed-universe#how-big-position-space-gets-v)). A momentum space of this kind is therefore compact only on a scale above the Planck energy.

## Prior art [S]

Found by a verifier of the investigation (§5):

- Artigas, Mielczarek and Rovelli 2019 (arXiv:1904.11338): compactifying the minisuperspace phase space makes the universe recollapse. The paper cites Born reciprocity. The root `CLAUDE.md` lists it as a lead, not queued.
- Moffat 2004 (gr-qc/0401117) writes a closed momentum-space FRW metric following Born, FRW being Friedmann–Robertson–Walker.
- Tseytlin 1992 (hep-th/9112004) bounds the size of a toroidal universe by duality.

## Where it bears

- **#11 §3 and the pages that quote it.** "The Fourier transform implements it unitarily" holds on flat space and locally; on a closed space the exchange is local only (flag 47). The established statement is on [the Fourier transform as a phase-space rotation](/wiki/phase-space/reciprocity/fourier-transform) and the program's use on [P3](/wiki/program/postulates/p3-reciprocity).
- **P5's mirror vacuum.** In a closed universe it has a global form only if the section condition admits polarizations that are not integrable, and then its energy cost is not computed ([P5](/wiki/program/postulates/p5-spontaneous-selection)).
- **Row 10's closed dual space.** The momentum fibre stays flat in the record's geometry, so a closed momentum space would be a new postulate ([the symmetric reading](/wiki/cosmology/scale-factor-duality/closed-universe#the-symmetric-reading-dead-unless-postulated-dv); flag 48).

## Sources

- `notes/closed-universe.md` §5 — the global and local exchange, the integrability result and its consequences, the compact phase spaces, the momentum radius needed and the prior art; §2 — Born 1938's momentum hypersphere; §1 — the reading of "closed"; §9 — the ±K_ref splitting, open; §10 — the corrected torus-like claim
- `verify/closed_universe.py` section E — E2 (the grain), E3 (the local accuracy), E4 (integrability on T\*S³ and T³, and (L/R₀)²), E5 (the product obstruction, Gr̃(2,5), √(R₀ l_P) and the bounds on κc); the anchors — the S³ spectrum
- `review/closed-universe/README.md` — the investigation's analyses, verifiers and critic
- `review/wiki-build-flags.md` item 47 — the scope of #11 §3's sentence, with its audit; awaiting Paul's ruling
- `papers/broken-born-checkpoint-v2.md` §3 — "the Fourier transform implements it unitarily"
- `papers/phase-space-diameter.md` §8.1, §8.2 — the maximum force and X's range, the two tests that exclude √(R₀ l_P)
- `notes/broken-born-theory.md` §2 — the section condition
