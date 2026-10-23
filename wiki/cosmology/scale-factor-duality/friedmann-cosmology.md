---
title: "Friedmann cosmology and minisuperspace"
weight: 10
status: established
description: "The FLRW metric, the Friedmann equation written with a lapse, fluids with ρ ∝ a^{−3(1+w)} including the stiff fluid, and cosmological redshift."
provenance: [T]
sources:
  - "notes/broken-born-theory.md §6"
  - "notes/broken-born-theory.md §4"
  - "papers/broken-born-checkpoint-v2.md §10"
  - "verify/soliton_obituary.py anchors"
  - "popsci/universes-other-half.md 'Dark energy as the orientation of the split'"
---

*Friedmann cosmology is the description of a universe that looks the same at every place and in every direction, so that its entire geometry reduces to one function of time, the scale factor a(t), which multiplies the distance between any two distant galaxies. The Friedmann equation ties the expansion rate to the energy density, and each kind of content, whether matter, radiation or a [cosmological constant](/wiki/cosmology/dark-energy/cosmological-constant), thins out at its own rate as a grows. Minisuperspace is the name for gravity reduced to this one function, with the freedom to choose the time coordinate kept as a single function called the lapse. The program writes its [cosmology](/wiki/cosmology) in this reduced form and adds a second scale factor for the [conjugate universe](/wiki/program/conjugate-universe), the momentum-space description of the same state.*

**Status:** Established — [T] — textbook cosmology, written here from general knowledge; the program's extension of it, the dual gravity term, is derived in `notes/broken-born-theory.md` §6 [D], summarized in [#11](/wiki/history/documents/checkpoint) §10, and not machine-checked.

## The homogeneous universe [T]

On the largest scales the universe is, to good approximation, homogeneous (the same at every place) and isotropic (the same in every direction). A spacetime with those two properties is described by the Friedmann–Lemaître–Robertson–Walker (FLRW) metric. For a spatially flat universe, written with a lapse function N(t), its line element is

```text
ds² = −N(t)² dt² + a(t)² dx²
```

Here x are comoving coordinates: labels that stay attached to galaxies moving with the expansion. The physical distance between two such galaxies is a(t) times their comoving separation, so the scale factor a carries the whole expansion. The lapse N sets how coordinate time t relates to the time a clock at rest measures; choosing N = 1 makes t cosmic time. The expansion rate is the Hubble rate

```text
H = ȧ / (N a)          (H = ȧ/a for N = 1)
```

A spatially curved universe replaces dx² by the metric of a sphere (closed, curvature k > 0) or of a hyperbolic space (open, k < 0). The curvature then enters the equations below as a term proportional to k/a².

## Minisuperspace: gravity reduced to a(t) and N(t) [T]

Superspace is the space of all spatial geometries, the configuration space of [general relativity](/wiki/gravity/spin-2-fields/general-relativity) in its Hamiltonian form. Restricting it to the FLRW family leaves one geometric variable, a(t), plus the lapse; that drastic reduction is called minisuperspace (DeWitt 1967 †; Misner 1969 †). Substituting the FLRW metric into the Einstein–Hilbert action and integrating the second time derivative by parts gives, per unit comoving volume and with M_P the [reduced Planck mass](/wiki/gravity/spin-2-fields/planck-units#two-conventions-for-the-planck-mass-t) (M_P² = 1/(8πG)), a gravitational Lagrangian of the form

```text
L = −3 M_P² a ȧ² / N  −  N a³ ρ(a)
```

where the second term is the contribution of matter with energy density ρ. Two features of this Lagrangian matter for the program.

- **The lapse is a Lagrange multiplier.** N appears without time derivatives. Varying it does not give an equation of motion but a condition that must hold at every instant, the Hamiltonian constraint. Setting N = 1 after the variation gives the Friedmann equation in the form the program uses, 3M_P²H² = ρ, which is the familiar H² = 8πGρ/3. It is called a constraint because it fixes the expansion rate from the energy content rather than evolving it.
- **Energy enters per comoving volume.** The matter term is N a³ ρ: the energy in a comoving volume, a³ρ. Anything that contributes energy to this one constraint, whatever its origin, enters it in this form. The program's [duality dictionary](/wiki/cosmology/scale-factor-duality/duality-dictionary) relies on this: the [lab notebook](/wiki/history/documents/lab-notebook) adds conjugate-side fluids by "Entering our Hamiltonian constraint" (#1 §6).

The second Friedmann equation follows from the first and from energy conservation. It gives the acceleration,

```text
ä/a = −(4πG/3)(ρ + 3p)
```

so the expansion accelerates only if the pressure p is below −ρ/3. Ordinary matter and radiation decelerate it [T].

## Fluids and how they thin [T]

Cosmological content is modelled as a perfect fluid with energy density ρ and pressure p = wρ; the constant w is its equation of state. Energy conservation in an expanding universe, ρ̇ + 3H(ρ + p) = 0, then gives

```text
ρ ∝ a^{−3(1+w)}
```

Each case has a simple physical reading:

| Content | w | ρ ∝ | Why |
| --- | --- | --- | --- |
| dust (cold matter) | 0 | a⁻³ | a fixed number of particles spread over a volume growing as a³ |
| radiation | +1/3 | a⁻⁴ | the dilution of dust, times one more factor 1/a from the [redshift](/wiki/cosmology/scale-factor-duality/redshift) of each quantum's energy |
| spatial curvature | −1/3 | a⁻² | the k/a² term of the Friedmann equation, written as if it were a fluid |
| cosmological constant | −1 | a⁰ | an energy density of empty space, which does not thin at all |
| stiff fluid | +1 | a⁻⁶ | the fastest dilution compatible with causality; see below |

These are the values the program's notebook uses (#1 §6). Its table states that the stiff fluid "dies as a⁻⁶".

**The stiff fluid and scalar fields.** A uniform scalar field φ with potential V has energy density ½φ̇² + V and pressure ½φ̇² − V, so its equation of state is

```text
w = (½φ̇² − V) / (½φ̇² + V)
```

If the field's energy is all kinetic (V negligible), w = +1: a stiff fluid. Its field equation then makes φ̇ fall as a⁻³, so its energy density falls as a⁻⁶. If instead the field sits nearly still on its potential, w is close to −1 and it behaves like a cosmological constant. This is why #1 §6 labels the w̃ = +1 entry of its table "Kinetic/stiff energy", and it is the distinction behind [Open: dual kinetic energy versus τ's potential](/wiki/cosmology/scale-factor-duality/dual-kinetic-link). Dark energy built from a slowly evolving field is [quintessence](/wiki/cosmology/dark-energy/quintessence).

**Negative curvature energy.** For a closed universe (k > 0) the curvature term enters the Friedmann equation with the opposite sign to an ordinary energy density, as H² = 8πGρ/3 − k/a². Read as a fluid, closed curvature has negative energy density. The dictionary's entry "closed dual space ⇒ *negative* ΔN_eff" (#1 §6) carries this sign across to the conjugate side; N_eff, the effective number of neutrino species, is on [the radiation era](/wiki/cosmology/early-universe/radiation-era).

## Redshift and momentum [T]

Light emitted when the scale factor was a_e arrives when it is a₀ with every wavelength stretched by the same factor, 1 + z = a₀/a_e, where z is the redshift; the energy of each quantum and the physical momentum of any freely moving particle fall as 1/a. [Redshift](/wiki/cosmology/scale-factor-duality/redshift) derives the relation and its consequences and records the program's uses of z, among them the [popular article](/wiki/history/documents/popular-articles) #12's reading of the redshift as a contracting momentum spectrum, which the wiki takes as a gloss on [the cosmological constraint a·ã = 1](/wiki/cosmology/scale-factor-duality/cosmological-constraint) (explanation, not a source for status).

## The program's extension: a second scale factor

The program describes the universe with two scale factors: a for position space and ã for the momentum-space description, the [conjugate universe](/wiki/program/conjugate-universe). Rigidity of the [symplectic form](/wiki/phase-space/reciprocity/symplectic-form) fixes their product, a·ã = 1 ([the cosmological constraint](/wiki/cosmology/scale-factor-duality/cosmological-constraint)). The lab notebook then adds a dual gravitational term to minisuperspace (#1 §6, [D]): "With one shared lapse N and dual Planck mass M̃, substituting ã = 1/a into the dual Einstein–Hilbert kinetic term" — the term ã(dã/dt)², which the substitution turns into ȧ²/a⁵ — "gives"

```text
3H²(M_P² + M̃²a⁻⁶) = ρ
```

The notebook gives the substitution and the result, not the steps between. Written out in the minisuperspace form above (the wiki's reading), the dual kinetic term −3M̃² ã(dã/dt)²/N becomes −3M̃² ȧ²/(N a⁵) once ã = 1/a; it adds to our own term −3M_P² a ȧ²/N, and varying the shared lapse N gives the equation above. The notebook does not state its Planck-mass convention; 3H²M_P² = ρ is the ordinary Friedmann equation when M_P is the reduced Planck mass (the wiki's reading).

What the term means, in #1 §6's words: "The dual gravitational sector is **not** a new fluid and **not** a ghost — ã was never independent — but a stiff-like (a⁻⁶) modification of the effective Planck mass, relevant only at early times." The extra term multiplies H² alongside M_P², so it acts as an addition to the effective Planck mass, and with it a change in the effective strength of gravity G_eff. Because it grows as a⁻⁶ toward the past, it matters only when a was small; today the ordinary Friedmann equation is recovered. #11 §10 keeps the result in one clause, "the dual Einstein term is an a⁻⁶ step in G_eff", and its test is [row 10](/wiki/predictions/early-universe-step), which #11 calls optional.

**Caveats.** The equation appears only in the lab notebook and has not been machine-checked. Its claim that there is no [ghost](/wiki/gravity/spin-2-fields/ghosts#the-lab-notebooks-minisuperspace-argument) is a minisuperspace statement: #1 §4 records that "no Boulware–Deser sector arises in minisuperspace" [D] (the [Boulware–Deser ghost](/wiki/gravity/spin-2-fields/fierz-pauli) is the negative-energy sixth mode that a generic massive-gravity or two-metric theory carries [T]) and that "The statement for full inhomogeneous H is open" [O]. That analysis predates the v0.4 addendum, after which the momentum-space partner of the metric is a [massive spin-2 field](/wiki/gravity/momentum-graviton) and, from the v0.5 addendum on, ghost freedom rests on [the frame-tier potential](/wiki/gravity/tuning-test/frame-tier). The cosmological solutions of the full two-metric theory are [bimetric cosmology](/wiki/gravity/spin-2-fields/bimetric-cosmology).

## The radiation era, briefly

Early on, radiation dominates and the Friedmann equation fixes the expansion rate as a function of temperature. That form, H = 1.66√g\* T²/M_Pl with M_Pl the non-reduced Planck mass, is one of the [textbook anchors](/wiki/method/verification/independent-anchors) of `verify/soliton_obituary.py`, which prints `PASS  Friedmann: H = 1.66 sqrt(g*) T^2/M_Pl` ([the soliton-obituary script](/wiki/method/verification/soliton-obituary-script)). Its derivation and uses are on [the radiation era](/wiki/cosmology/early-universe/radiation-era).

## Standard references

- A. Friedmann (1922) †; G. Lemaître (1927) †; H. P. Robertson (1935) †; A. G. Walker (1937) †: the homogeneous, isotropic solutions and their metric.
- B. S. DeWitt, "Quantum theory of gravity. I. The canonical theory", Physical Review (1967) †; C. W. Misner, "Quantum cosmology. I", Physical Review (1969) †: superspace and minisuperspace.
- S. Weinberg, *Cosmology* (Oxford University Press, 2008) †: a standard textbook treatment of all of the above.

None of these is cited in the program's documents; they are given here from memory and are unverified.

## Used by

- [The cosmological constraint a·ã = 1](/wiki/cosmology/scale-factor-duality/cosmological-constraint) — the second scale factor and its reciprocal relation to ours.
- [The duality dictionary w_eff = −w̃](/wiki/cosmology/scale-factor-duality/duality-dictionary) — the shared lapse, the Hamiltonian constraint and ρ ∝ a^{−3(1+w)}.
- [Obituary: conjugate collapse powers our expansion](/wiki/cosmology/scale-factor-duality/collapse-powered-expansion) — dust decelerates the expansion.
- [The turnaround as the conjugate bounce](/wiki/cosmology/scale-factor-duality/conjugate-bounce) — a halt and reversal of a(t), read through a·ã = 1.
- [Open: dual kinetic energy versus τ's potential](/wiki/cosmology/scale-factor-duality/dual-kinetic-link) — kinetic versus potential energy of a scalar field.
- [Row 10: an early step in G_eff](/wiki/predictions/early-universe-step) — the a⁻⁶ term in the Friedmann equation.
- [Row 5: the fate of the expansion](/wiki/predictions/fate-of-expansion) — the expansion halts when the total energy density reaches zero.
- [The conjugate universe: one state, two descriptions](/wiki/program/conjugate-universe) — ρ ∝ a^{−3(1+w)} applied to a fluid in the momentum-space description.

## Sources

- `notes/broken-born-theory.md` §6 — the shared lapse, "our Hamiltonian constraint", the fluid table and the Friedmann equation with the dual term
- `notes/broken-born-theory.md` §4 — the minisuperspace ghost accounting and its open extension to inhomogeneous H
- `papers/broken-born-checkpoint-v2.md` §10 — the current statement of the cosmology built on this reduction
- `verify/soliton_obituary.py` — the radiation-era Friedmann coefficient, checked as an anchor
- `popsci/universes-other-half.md` 'Dark energy as the orientation of the split' — redshift read as a contracting momentum spectrum (popular article; explanation only)
