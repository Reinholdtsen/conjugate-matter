---
title: "The Witten effect"
weight: 25
status: established
description: "A magnetic monopole in a gauge theory with vacuum angle θ carries an electric charge shifted by θ/2π of the unit charge per unit of magnetic charge (Witten 1979†): the θ term and Gauss's law, when θ is physical, charge conjugation and parity, the dyon lattice and the shift T of SL(2, ℤ), and the visible charge round-3 ruling 9 gave the soliton candidate's hidden monopoles, a channel strict P4 closes."
provenance: [T]
sources:
  - "review/round3-adjudication.md 'Rulings' 9"
  - "review/round3-adjudication.md 'Decisions' 1"
  - "review/round3-adjudication.md 'Decisions' 2"
  - "review/round3/referee/audit-notes.md Step 1"
  - "review/round3/referee/audit-notes.md Step 4(a)"
  - "review/round3/referee/audit-notes.md Step 4(b)"
  - "review/round3/referee/audit-notes.md Step 4(c)"
  - "review/round3/referee/step4b.py"
  - "review/round3/referee/step4b.out"
  - "review/round3/referee/step2a.out"
  - "notes/knot-dark-matter-standalone.md §2"
  - "notes/knot-dark-matter-standalone.md §5"
  - "notes/knot-dark-matter-standalone.md ref [14]"
  - "review/v3-worklog.md 'Findings neither referee raised'"
  - "papers/broken-born-checkpoint-v2.md §4"
  - "papers/broken-born-checkpoint-v2.md §11.3"
  - "CLAUDE.md 'Since the handoff'"
---

*The Witten effect is the electric charge that a [magnetic monopole](/wiki/electric-magnetic-duality/monopoles) carries in a gauge theory with a nonzero vacuum angle θ, the coefficient of a term in the Lagrangian proportional to the product E·B of the electric and magnetic fields. In such a theory a monopole's electric charge is not a whole multiple of the unit of charge e: it is shifted by θ/2π of e for each unit of magnetic charge, so the monopole is a [dyon](/wiki/electric-magnetic-duality/monopoles/dirac-quantization#dyons-and-the-dsz-pairing-t), a particle carrying both kinds of charge. Edward Witten derived the result in 1979. Increasing θ by 2π gives back the same set of charges with the dyons relabelled, which is the shift T of the [duality group SL(2, ℤ)](/wiki/electric-magnetic-duality/s-duality#the-coupling-and-the-generator-s-t). The effect entered the program once, through the [retired soliton candidate](/wiki/dark-matter/candidates/soliton-candidate/obituary). The round-3 review accepted, without re-checking it, that a hidden vacuum angle together with [kinetic mixing](/wiki/dark-matter/candidates/soliton-candidate/kinetic-mixing) between the hidden photon and ours would give the candidate's hidden monopoles a small electric charge under our photon, contradicting the manuscript's statement that the decisive constraints act on its hidden fermion, not on the dark matter itself. Strict sector separation, the program's reading of postulate [P4](/wiki/program/postulates/p4-polarized-matter), closes that channel.*

**Status:** Established — [T] — literature (Witten 1979 †), explained here from general knowledge; no `verify/` script checks it. Its one use in the program, [ruling 9](/wiki/method/review/round-3/rulings#ruling-9-the-witten-effect) of the [round-3 review](/wiki/method/review/round-3) on the soliton candidate's monopoles, was "Accepted, not re-checked", and the charges quoted for it come from the referee's own script and its output (`review/round3/referee/step4b.out`), which the gate does not run. The candidate is retired, and strict sector separation is in force (root `CLAUDE.md`, 'Since the handoff'). References the wiki adds from memory are marked †.

## The θ term [T]

### One more gauge-invariant term

The Lagrangian density of electromagnetism is built from the field strength, which gauge transformations leave unchanged. For a single U(1) gauge field there are two independent Lorentz-invariant terms quadratic in the field strength: the familiar ½(E² − B²) and the product E·B [T]. Ordinary electrodynamics usually omits the second, because it has no effect on the classical field equations unless magnetic charge is present. Its coefficient is written with an angle θ, the vacuum angle. For a U(1) theory whose smallest electric charge is e, in natural rationalized units (ħ = c = 1, α = e²/4π, as on [Dirac quantization and the DSZ pairing](/wiki/electric-magnetic-duality/monopoles/dirac-quantization)):

```text
ℒ = ½(E² − B²) − (θe²/4π²) E·B − ρ_e φ + j_e·A
```

Here ρ_e and j_e are the electric charge and current densities, and φ and A the scalar and vector potentials, with E = −∇φ − ∂A/∂t and B = ∇×A. The factor e²/4π² makes the physics periodic in θ with period 2π, as the charges below show; the overall sign of the term is a convention [T].

### Why it acts only where there is magnetic charge

Wherever the fields derive from potentials, E·B is a total derivative: it can be written as the divergence of a current in space and time, so adding it to the Lagrangian adds only a boundary term to the action and changes no equation of motion [T]. Varying the action with respect to φ shows where this fails. Gauss's law acquires an extra term:

```text
∇·E = ρ_e + (θe²/4π²) ∇·B
```

Without magnetic charge, ∇·B = 0 and the extra term vanishes. With a magnetic charge density ρ_m = ∇·B, it acts as an electric charge density (θe²/4π²)ρ_m attached to the magnetic charge: a monopole is also a source of electric flux, in proportion to θ and to its magnetic charge [T].

In a non-abelian theory the corresponding term is also a total derivative, but configurations whose gauge field at infinity winds around the gauge group, instantons, give it physical effects even without monopoles [T].

## The charge of a monopole [T]

### Witten's result

By the modified Gauss law, a monopole of magnetic charge g carries an electric charge θe²g/4π² in addition to any ordinary charge. Dirac's condition allows the magnetic charges g = m·2π/e, with m an integer ([Dirac's argument](/wiki/electric-magnetic-duality/monopoles/dirac-quantization#diracs-argument-t)), and for them the extra charge is mθe/2π. Witten showed that the ordinary part is a whole multiple of e (Witten 1979 †), so the state with labels (n, m) carries

```text
magnetic charge    g = m · 2π/e
electric charge    q = e (n + mθ/2π)          n, m integers
```

The opposite sign convention for the θ term gives q = e(n − mθ/2π) [T].

Witten's argument is quantum mechanical, and he made it for the ['t Hooft–Polyakov monopole](/wiki/electric-magnetic-duality/monopoles/thooft-polyakov-monopole) of an SU(2) gauge theory broken to U(1) by a Higgs field. A rotation by a full turn about the direction of the Higgs field is the identity transformation, so it must act trivially on every physical state. With the θ term present, the operator that generates such rotations contains θ times the magnetic charge besides the electric charge, and requiring a full turn to act trivially quantizes that combination rather than the electric charge alone [T]. Classical dyons of the same theory, monopoles carrying an electric charge, had been found by Julia and Zee (1975 †); the θ term changes the values that the quantized charge can take.

In Witten's paper the unit of electric charge is the charge of the W bosons, relative to which the 't Hooft–Polyakov monopole carries twice the Dirac minimum, and θ is normalized for the SU(2) group. The result has the same form, a shift by θ/2π of the W bosons' charge, which the paper's title writes as "Dyons of charge eθ/2π" †. Factors of 2 in such formulas move with the choice of unit and of normalization, as they do in Dirac's condition itself ([which charge counts: 2π or 4π](/wiki/electric-magnetic-duality/monopoles/dirac-quantization#which-charge-counts-2π-or-4π)) [T].

### When θ is physical

An angle that a change of variables can remove has no physical effect. A massless fermion that carries the gauge charge provides such a change: rotating the phases of its left- and right-handed components in opposite directions, a chiral rotation, shifts θ by an amount fixed by the anomaly of that rotation, so θ can be rotated to zero [T]. If every charged fermion has a mass, the same rotation moves the phase into the mass terms instead, and one combination of θ with the phases of the masses stays physical [T].

### Charge conjugation and parity

Under a reflection of space, parity, E reverses and B does not; under time reversal, B reverses and E does not. The product E·B is therefore odd under both, while charge conjugation C, which reverses both fields, leaves it unchanged. A θ term with θ ≠ 0 violates parity and time reversal, and it violates the combination CP of charge conjugation and parity [T]. CP reverses the sign of θ, and θ matters only modulo 2π, so θ = 0 and θ = π are the two values that conserve CP [T].

The charge formula shows the same thing. CP reverses electric charges and leaves magnetic charges unchanged. For each magnetic charge m, the electric charges e(n + mθ/2π) form a set symmetric under that reversal at θ = 0 and at θ = π, where for odd m they are the odd multiples of e/2, and at no other θ [T]. In the strong interactions the corresponding angle is measured to be very small, the puzzle known as the strong CP problem [T]. The paper #14 cites for hidden monopoles states the effect in these terms, as a consequence of CP violation ([below](/wiki/electric-magnetic-duality/monopoles/witten-effect#in-the-literature-as-the-round-3-referee-read-it)).

## The dyon lattice and the shift T [T]

### The pairing does not depend on θ

The charges of a theory with monopoles form a lattice in the plane of electric and magnetic charge, and two dyons are mutually consistent only if their Dirac–Schwinger–Zwanziger (DSZ) pairing, written e₁g₂ − e₂g₁ on [dyons and the DSZ pairing](/wiki/electric-magnetic-duality/monopoles/dirac-quantization#dyons-and-the-dsz-pairing-t), is a whole multiple of 2π. For dyons (n₁, m₁) and (n₂, m₂) with the shifted charges of the Witten effect:

```text
q₁g₂ − q₂g₁ = e(n₁ + m₁θ/2π)·m₂(2π/e) − e(n₂ + m₂θ/2π)·m₁(2π/e)
            = 2π (n₁m₂ − n₂m₁)
```

The θ-dependent parts cancel, so the pairing takes the same integer values at every θ, and dyons with fractional electric charges remain consistent with Dirac's condition [T].

### Shifting θ by 2π relabels the dyons

Increasing θ by 2π raises the electric charge of each dyon (n, m) by m·e, to the value that the dyon (n + m, m) had before:

```text
q(n, m; θ + 2π) = e(n + m + mθ/2π) = q(n + m, m; θ)

(n, m) → (n + m, m):    the matrix [[1, 1], [0, 1]] acting on (n, m)
```

As θ grows from 0 to 2π, each row of the lattice with fixed magnetic charge slides along the electric axis, by m units of e over the full turn, and at θ = 2π the lattice coincides with the one at θ = 0. The set of charges is the same; only the labels move. This is why θ is an angle [T].

The relabelling is an integer matrix of determinant 1, so it belongs to SL(2, ℤ), the group of linear maps that carry the lattice to itself and preserve its pairing. It is the generator T. On the complexified coupling τ_c = θ/2π + 4πi/g², with g there the gauge coupling, T acts as τ_c → τ_c + 1, the shift of θ by 2π; the other generator, S, exchanges electric and magnetic charges ([the coupling and the generator S](/wiki/electric-magnetic-duality/s-duality#the-coupling-and-the-generator-s-t)) [T]. The Witten effect is the physical content of T: shifting θ by 2π changes every dyon's charge and leaves the spectrum as a whole unchanged. With the opposite sign convention for θ, the relabelling is the inverse of T.

#11 §11.3 builds the program's [symplectic charge lattice](/wiki/electric-magnetic-duality/symplectic-charge-lattice) on the DSZ pairing and on S, "generated by the same [[0,1],[−1,0]] rotation as Born's ρ and our Z → −Z⁻¹". The [checkpoint](/wiki/history/documents/checkpoint) does not mention the vacuum angle or the Witten effect.

## Hidden monopoles and our photon

### A hidden sector's own angle [T]

A hidden sector with an unbroken U(1) of its own has its own photon and can have its own vacuum angle, written θ_d (d for dark). Its monopoles are then hidden dyons: by the Witten effect each carries a hidden electric charge, θ_d/2π of the hidden unit of charge for each unit of magnetic charge, under the hidden photon [T]. Two couplings between the hidden photon and ours could make such a monopole electrically charged under our photon as well.

- **Kinetic mixing**, a term proportional to ε times the product of the two field strengths, gives particles charged under the hidden U(1) a small electric charge under ours, of order ε times their hidden charge, while the hidden photon is massless ([what kinetic mixing does](/wiki/dark-matter/candidates/soliton-candidate/kinetic-mixing#what-it-does-t)) [T]. It does not make a hidden monopole magnetic under our electromagnetism while the hidden U(1) is unbroken ([point (c)](/wiki/dark-matter/candidates/soliton-candidate/kinetic-mixing#c-no-visible-magnetic-flux-while-u1d-is-unbroken)).
- **A mixed angle.** A θ-type term that multiplies our E by the hidden B enters our Gauss law as the θ term does above, with the hidden magnetic charge as the source. A hidden monopole then carries an electric charge under our photon in proportion to that mixed angle [T].

### In the literature, as the round-3 referee read it

#14 cites F. Brümmer, J. Jaeckel and V. V. Khoze (2009) for this channel, as its reference [14]. The round-3 referee checked the paper against its abstract and found support (`review/round3/referee/audit-notes.md`, Step 1): with CP violation, hidden monopoles acquire a hidden electric charge through the Witten effect, and "quite generally they also acquire (small) electric charges under the visible electromagnetic gauge group"; also, "Both kinetic and magnetic mixing are naturally induced radiatively". The referee's notes cite two of the paper's equations:

- eq. 2.7, for what the referee calls "CP-violating magnetic mixing": "hidden monopole gets visible electric charge -theta_12/2pi" (Step 4(b)); the notes do not define θ₁₂;
- eq. 3.19, for kinetic mixing together with the hidden angle: "q_vis ~ chi theta_d/(2 pi)" (Step 4(a) item 7).

Here χ is the referee's symbol for the kinetic mixing ε, as in Brümmer and Jaeckel's χ = v/M (Step 1), and is unrelated to the program's conjugate matter χ ([notation](/wiki/notation)); q_vis is the monopole's electric charge under our photon. In this wiki's reading, the formula is the product of the two effects above: the hidden Witten charge θ_d/2π, in hidden units, and the factor χ by which mixing passes a hidden electric charge to our photon. The adjudication cites eq. 3.19 "per the referee" and does not mention eq. 2.7 (ruling 9).

## The soliton candidate's monopoles

### The channel #14 named

The withdrawn manuscript [#14](/wiki/dark-matter/candidates/soliton-candidate) proposed superheavy 't Hooft–Polyakov monopoles of a hidden gauge group SU(2)_d, broken to U(1)_d, as the dark matter ([Obituary: superheavy conjugate solitons](/wiki/dark-matter/candidates/soliton-candidate/obituary)). U(1)_d stayed unbroken, so the hidden photon was massless. The hidden W′± carried charge g_d, a doublet fermion ψ carried ±g_d/2, and the monopoles carried magnetic charge g_m = 4π/g_d, "the Dirac minimum relative to psi's charge g_d/2" (#14 §2; [Obituary: the hidden SU(2) → U(1) proposal](/wiki/dark-matter/candidates/soliton-candidate/hidden-sector)). For the mixing, v3 gave "epsilon ~ 1e-7 to 1e-6" from a Planck-suppressed operator (#14 §2(b)), an estimate round 3 found unsupported ([Obituary: Planck-suppressed adjoint mixing](/wiki/dark-matter/candidates/soliton-candidate/dimension-five-operator)).

The v3 worklog had found from the literature that mixing gives the hidden monopoles no magnetic flux of ours, and it listed what leaks instead (`review/v3-worklog.md`, item L1):

> - dark *electric* states (W′±) pick up a millicharge εe [Brümmer–Jaeckel];
> - CP violation gives the monopoles a small visible *electric* charge ("magnetic mixing", Brümmer–Jaeckel–Khoze, JHEP 06 (2009) 037);
> - a massive dark photon would make minicharged monopoles.

Its assessment: "the candidate survives mixing more easily than v2 says, and the constraint moves to the dark W′±". v3, which had added ψ so that the W′± could decay ([W′ overclosure](/wiki/dark-matter/candidates/soliton-candidate/w-prime-overclosure)), wrote the second channel into §2(c):

> The visible-sector leakage is instead (i) psi acquires visible electric charge ~ epsilon e, and (ii) with CP violation the monopoles acquire a small visible electric charge [14]. The decisive constraints therefore act on psi, not on the dark matter itself (Sec. 4).

#14's first exclusion condition was "Any confirmed non-gravitational coupling between the dominant dark-matter component and the Standard Model" (§5).

### What round 3 found

The referee found #14's citation supported but noted that v3 addressed neither the size of the monopoles' visible charge nor its consequence for the dark matter (Step 4(b)). Its own estimate (Step 4(a) item 7): "Hidden theta is physical (psi massive) and generically O(1): q_vis ~ chi theta_d/(2 pi)", by eq. 3.19 of Brümmer–Jaeckel–Khoze, which gives "1.6e-8 e (chi=1e-7, theta=1) to 1.6e-7 e (chi=1e-6)". The same item states the contradiction: §2(c)(ii) gives the dark matter itself a visible electric charge, yet §2(c) concludes that "the decisive constraints act on psi, not on the dark matter itself", and exclusion condition 1 treats any coupling of the dark matter to the Standard Model as fatal. The referee's judgement of the size: "Phenomenologically tiny at M=3e13 GeV, but it makes exclusion condition 1 self-triggering in the eps != 0 branch", M being the benchmark monopole mass. Among the constraints #14 had not evaluated, it listed the same point (Step 4(c) item 8): "monopoles are hidden dyons; visible charge ~1e-8-1e-7 e for eps~1e-7-1e-6".

The referee's script evaluates the formula on a grid (`review/round3/referee/step4b.py`, part (3)). It sets the ratio of the hidden unit of charge to ours to (g_d/2)/e, which is 1 under the manuscript's coupling hypothesis H (`review/round3/referee/step2a.out`: "(g_d/2)/e = 1.000"; [Obituary: the coupling α_d ≈ 34](/wiki/dark-matter/candidates/soliton-candidate/alpha-d-coupling)). Its output (`review/round3/referee/step4b.out`), where 3.14 is the script's `pi`:

```text
chi=1e-07, theta_d=0.10: monopole visible charge ~ 1.59e-09 e
chi=1e-07, theta_d=1.00: monopole visible charge ~ 1.59e-08 e
chi=1e-07, theta_d=3.14: monopole visible charge ~ 5.00e-08 e
chi=1e-06, theta_d=0.10: monopole visible charge ~ 1.59e-08 e
chi=1e-06, theta_d=1.00: monopole visible charge ~ 1.59e-07 e
chi=1e-06, theta_d=3.14: monopole visible charge ~ 5.00e-07 e
```

### Ruling 9 and the claim it contradicted

The adjudication ruled on the finding as ruling 9 (`review/round3-adjudication.md`, 'Rulings'):

| Referee finding | Ruling | Evidence |
| --- | --- | --- |
| With mixing and a physical hidden θ, the monopoles carry visible electric charge ~ εθ/2π · e (Witten effect) | Accepted, not re-checked | Brümmer–Jaeckel–Khoze eq. 3.19, per the referee. This contradicts v3's "constraints act on ψ, not the dark matter" whenever ε ≠ 0. |

The statement the ruling contradicts, #14's "The decisive constraints therefore act on psi, not on the dark matter itself", is registered as dead in [the graveyard](/wiki/status/graveyard#parts-of-the-soliton-candidate), with the candidate's [obituary](/wiki/dark-matter/candidates/soliton-candidate/obituary#the-other-rulings): whenever ε ≠ 0, the dark matter itself carries a visible charge. The Witten effect itself was not in question; the ruling concerns its consequence in #14's sector.

### Closed by strict sector separation

Decision 1 of the same adjudication took the program's postulate P4 strictly ([Decision 1](/wiki/method/review/round-3/decisions#decision-1-strict-sector-separation)):

> **Kinetic mixing: strict sector separation.** ε ≲ 10⁻¹³ from gravity alone, and zero if hidden charge conjugation is a gauged symmetry.

Among its reasons, it "closes three failure channels at once: ψ millicharge, the monopoles' Witten-effect charge (ruling 9), and re-thermalization of the hidden sector." #11 v2.1 wrote the strict reading into P4 (§4): "no kinetic mixing between the sectors beyond what gravity induces, which vanishes if hidden charge conjugation is exact and otherwise first appears at six loops, ε ≲ 10⁻¹³ [27S]" ([strict sector separation](/wiki/dark-matter/candidates/soliton-candidate/kinetic-mixing#strict-sector-separation)). Decision 2 retired the soliton candidate the same day ([Decision 2](/wiki/method/review/round-3/decisions#decision-2-the-soliton-candidate-retired)), so the channel no longer bears on a live candidate. The [project instructions](/wiki/history/documents/project-instructions) record that "Strict sector separation (P4 at face value) is in force." Under strict P4 neither of the program's remaining dark-matter candidates couples to the Standard Model, which is [row 7, a permanent null in direct detection](/wiki/predictions/direct-detection-null).

## What the record leaves open

- **Accepted, not re-checked.** Ruling 9 rests on the referee's reading of Brümmer–Jaeckel–Khoze: the adjudication cites eq. 3.19 "per the referee" and accepted the finding without re-checking it. A finding accepted this way rests on the referee alone ([the protocol's limits](/wiki/method/review/review-protocol#limits)).
- **Outside the gate.** The charges come from `review/round3/referee/step4b.py`, which `scripts/check.sh` does not run, and no `verify/` script reproduces them.
- **The residual mixing.** Decision 1 closes the channel by bounding ε. The mixing is zero only if hidden charge conjugation is exact (#11) or gauged (Decision 1), and whether #11's ε ≲ 10⁻¹³ is a ceiling or a floor is unresolved ([how to read the bound and the zero](/wiki/program/postulates/p4-polarized-matter#how-to-read-the-bound-and-the-zero)). No document evaluates the monopoles' visible charge at that level. After Decision 2 retired the candidate, no document returns to the channel.

## References

As the program's documents cite them:

- F. Brümmer, J. Jaeckel, V. V. Khoze, JHEP 06 (2009) 037, arXiv:0905.0633 — #14's [14], untagged in #14 itself; the v3 worklog names it in item L1. The round-3 referee found support in its abstract (Step 1) and took the visible charge from its eqs. 2.7 and 3.19 (Steps 4(a) and 4(b)).

Added by the wiki from model memory (†):

- E. Witten, "Dyons of charge eθ/2π," Phys. Lett. B 86, 283 (1979) † — the effect.
- B. Julia, A. Zee (1975) † — classical dyons of the SU(2) theory with an adjoint Higgs field.

## Used by

- [Kinetic mixing between sectors](/wiki/dark-matter/candidates/soliton-candidate/kinetic-mixing) — leakage channel (ii): with ε ≠ 0 and a hidden θ, the soliton candidate's monopoles carry a visible charge.
- [P4: polarized matter and strict sector separation](/wiki/program/postulates/p4-polarized-matter) — the monopoles' Witten-effect charge, one of the three channels Decision 1 closed.
- [Row 7: a permanent null in direct detection](/wiki/predictions/direct-detection-null) — the same three channels, closed by strict P4.
- [Round-3 verdict, rulings and citation audit](/wiki/method/review/round-3/rulings) — ruling 9.
- [Round-3 decisions and lessons](/wiki/method/review/round-3/decisions) — Decision 1 and the channels it closes.
- [Obituary: superheavy conjugate solitons](/wiki/dark-matter/candidates/soliton-candidate/obituary) — ruling 9 among the rulings on the hidden sector.
- [Obituary: Planck-suppressed adjoint mixing](/wiki/dark-matter/candidates/soliton-candidate/dimension-five-operator) — the mixing whose range sets the referee's charges.
- [Obituary: the ψ relic window](/wiki/dark-matter/candidates/soliton-candidate/psi-relic-window) — the channels Decision 1 closed, ψ's millicharge among them.
- [The graveyard: dead claims](/wiki/status/graveyard) — #14's statement that the decisive constraints act on ψ, not on the dark matter.
- [The blind-review protocol and verdict scale](/wiki/method/review/review-protocol) — ruling 9 as a finding accepted without re-checking.
- [Dirac quantization and the DSZ pairing](/wiki/electric-magnetic-duality/monopoles/dirac-quantization) — the shift T of the charge lattice.

## Sources

- `review/round3-adjudication.md` 'Rulings' 9 — the finding, "Accepted, not re-checked", and its evidence; 'Decisions' 1 — strict sector separation and the three channels it closes; 'Decisions' 2 — the candidate retired
- `review/round3/referee/audit-notes.md` Step 1 — reference [14] against its abstract; Step 4(a) item 7 — the hidden θ, the formula, the size of the charge and the contradiction with exclusion condition 1; Step 4(b) — magnetic mixing and eq. 2.7; Step 4(c) item 8 — "monopoles are hidden dyons"
- `review/round3/referee/step4b.py` part (3) — the formula as coded; `review/round3/referee/step4b.out` — the charges; `review/round3/referee/step2a.out` — (g_d/2)/e = 1.000
- `notes/knot-dark-matter-standalone.md` §2 — the hidden sector, the mixing estimate and leakage channel (ii); §5 — exclusion condition 1; ref [14] (withdrawn manuscript)
- `review/v3-worklog.md` 'Findings neither referee raised' (L1) — the channel as first named, "magnetic mixing"
- `papers/broken-born-checkpoint-v2.md` §4 — P4 taken strictly; §11.3 — the DSZ pairing and S, without the vacuum angle
- `CLAUDE.md` 'Since the handoff' — strict sector separation in force
