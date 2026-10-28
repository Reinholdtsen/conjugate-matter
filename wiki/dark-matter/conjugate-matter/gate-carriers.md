---
title: "What could carry a relative-velocity gate"
weight: 35
status: alive
description: "No field of finite spin can carry a force that switches off above a relative speed like 120 km/s: exchange gives a polynomial in the relative Lorentz factor that grows with speed on the scale c; a tower of every spin needs cancellations of 10^5421169; a medium gates velocity through the medium, not relative velocity; a continuous-spin particle has the right shape but a threshold that falls with distance."
provenance: [D, V, T]
sources:
  - "notes/velocity-gated-gravity.md §9"
  - "notes/velocity-gated-gravity.md §5"
  - "notes/gate-mechanism.md §2"
  - "notes/gate-mechanism.md §4"
  - "verify/velocity_gated_gravity.py 'I. Carriers'"
  - "verify/gate_mechanism.py 'G. Run 3's theory verifier'"
  - "verify/gate_mechanism.py 'A. Anchors (independent of both derivations)'"
  - "review/momentum-gravity/README.md"
  - "papers/broken-born-checkpoint-v2.md §8"
---

*A force carried by a field depends on how fast the two bodies move relative to each other only in a limited way. When the field has a definite spin, the dependence is a polynomial in the bodies' relative velocity that grows with speed, and its natural scale is the speed of light. The program's dark-matter gate, and the long-range attraction P.R. asked about, both need the opposite: an interaction that switches off once the relative speed passes about 120 km/s. A working note of 2026-10-28 asks whether any field could carry such a gate. No single spin can. Fields of every spin together could build one only through cancellations between enormous terms. A medium can switch a force off with speed, but then the force depends on each body's motion through the medium, not on the bodies' relative velocity. One known exotic framework, a massless particle with infinitely many helicities, gives a correction with the right shape, but its threshold velocity falls with distance, so it does not give a fixed gate.*

**Status:** Alive — computed, not reviewed — as `notes/velocity-gated-gravity.md` §9 tags its parts: finite spin [D][V; two derivations]; the no-go theorems [T][S]; the spin tower [D][V; one derivation]; the medium [D][V; one derivation]; continuous spin [T][S, read twice: by the run-3 theory verifier and by the drafting session, whose fetch is in the session transcript, not the record; numbers D]. The numbers are recomputed in section I of `verify/velocity_gated_gravity.py` ([the velocity-gated-gravity script](/wiki/method/verification/velocity-gated-gravity-script)) and, for the spin-2 case and the medium, in section G of `verify/gate_mechanism.py` ([the gate-mechanism script](/wiki/method/verification/gate-mechanism-script)). The note has not been through a blind review round.

## The question

Two models need a carrier that switches an interaction off above a relative speed of order v\* ≈ 120 km/s:

- the program's own [velocity gate](/wiki/dark-matter/conjugate-matter/velocity-gate) on χ–χ scattering, which the record derives from exchange of the [momentum graviton X](/wiki/gravity/momentum-graviton) ([the gate mechanism](/wiki/dark-matter/conjugate-matter/gate-mechanism));
- [a long-range velocity-gated attraction among χ](/wiki/dark-matter/momentum-clumping/long-range-gated-attraction), P.R.'s model, for which the record supplies no carrier: X is massive, and #11 §8's m_φ is a free scale with no field behind it (`notes/velocity-gated-gravity.md` §5).

The velocity-gated-gravity note takes up the general question in its §9, "Could any field carry a relative-velocity gate?"; the gate-mechanism note answers it for the record's own X (`notes/gate-mechanism.md` §2), where flag 55 in `review/wiki-build-flags.md` proposes that the mechanism is not derived ([exchanging X cannot produce the gate](/wiki/dark-matter/conjugate-matter/gate-mechanism#exchanging-x-cannot-produce-the-gate)).

## Finite spin

[D][V; two derivations] (§9).

- **The residue is a polynomial.** At tree level, exchange of a spin-J field between spinless point sources has a pole residue that is a degree-J polynomial in γ, the relative Lorentz factor of the two sources: P_J(γ), the Legendre polynomial, if the field is massive, and T_J(γ), the Chebyshev polynomial, if it is massless. The (v/c)² coefficients are J(J + 1)/4 and J²/2. The script checks this for J = 0–4, and the coefficients for J = 0–8 (check I1). The polynomial form is standard: the residue at a spin-J pole is proportional to the Legendre polynomial of the scattering angle [T] (`verify/gate_mechanism.py`, anchors).
- **It grows with speed.** All the roots of these polynomials lie in [−1, 1], so every residue increases for γ > 1 (check I1): no single spin gives a gate. For spin 2 this is the factor (3γ² − 1)/2 of X, 1 + 2.40×10⁻⁷ at 120 km/s ([X between ordinary bodies](/wiki/gravity/momentum-graviton/ordinary-bodies#its-velocity-dependence-is-relativistic)).
- **The spin it would take.** An order-one rise at 120 km/s needs J ≈ 3533 (massless) to 4996 (massive).
- **Nothing else helps.** Derivative couplings, form factors of composite sources, loops, nonlocal form factors in the transfer, and the record's spin-0 fields (τ and the other moduli of [the field content](/wiki/phase-space/modular-field/field-content)) add no gate. Loops bring other functions of γ, all with velocity scale c (§9). For gravitational-strength exchange between 70 MeV χ the coupling α_G = Gm²/(ħc) is 3.287×10⁻⁴¹ and the Bohr-type velocity α_G c is 9.855×10⁻³³ m/s: loops bring no scale near v\* either (`verify/gate_mechanism.py`, check T3).
- **The record's X.** The gate-mechanism note gives the same result for X, with a general vertex: at fixed transfer the amplitude is a polynomial of degree at most two in k², whose velocity scale is c (`notes/gate-mechanism.md` §2).

## No-go theorems

[T][S] (§9). Two literature results close the obvious escapes ([the multi-graviton no-go theorem](/wiki/gravity/spin-2-fields/multi-graviton-no-go) is a related result for several massless spin-2 fields):

- Massless fields of spin 3 or more give no macroscopic force (Weinberg 1964, abstract read; Porrati 2008).
- Finitely many massive fields of spin above 2 cannot couple causally to gravitons (Afkhami-Jeddi, Kundu and Tajdini 2019).

## A tower of spins

[D][V; one derivation] (§9).

- A tower of fields of every spin can build only gates that are entire functions of γ, and only through cancelling terms.
- For the Gaussian gate at v\* = 120 km/s the largest single-spin term is about 10^5421169 times the net (x = c²/v\*² = 6.24×10⁶). The script checks the expansion of e^{−x(γ − 1)} into Legendre polynomials and the size of its largest term (check I3).
- Rational gates are impossible.

The gate-mechanism note reaches the same point from the amplitude: #11 §8's form h(t)F(k²/μ²), read as an exact amplitude, has a residue F(s) that is not a polynomial, and the Gaussian and rational F have nonzero Legendre coefficients at every order computed (l = 0–6), so the form would need exchanged particles of every spin at one mass (`notes/gate-mechanism.md` §2).

## A medium

[D][V; one derivation] (§9).

- A mediator propagating through a medium at speed c_s gives dependence on each body's velocity relative to the medium.
- Two co-moving bodies side by side feel 1/√(1 − V²/c_s²) times the static force: 1.155 at V/c_s = 0.5. In line, the force is unchanged below c_s (`verify/gate_mechanism.py`, check T6).
- Above c_s the trailing body feels twice the static force while the side-by-side and leading bodies, outside the Mach cone, feel none, so action and reaction are unequal (check T6).
- This is a preferred-frame effect, not dependence on relative velocity. Two bodies at zero relative velocity feel a force that depends on how fast they move together.

The gate-mechanism note finds the same for a preferred frame in the program's own vacuum: a per-leg profile gives the record's gate times a suppression e^{−m²V²/μ²} in the pair's velocity V through the frame, 0.26, 4.7×10⁻⁶ and 4.9×10⁻²² at V = 100, 300 and 600 km/s (`notes/gate-mechanism.md` §4; [the vacuum polarization supplies no velocity](/wiki/dark-matter/conjugate-matter/gate-mechanism#the-vacuum-polarization-supplies-no-velocity-dv-one-derivation)).

## Continuous spin

[T][S, read twice: by the run-3 theory verifier, and by the drafting session on 2026-10-27, whose fetch is in the session transcript, not the record; numbers D] (§9).

- A massless continuous-spin particle has infinitely many helicities and lies outside the theorems above. Its scale ρ, an energy, is unrelated to the program's Born rotation ρ.
- Schuster, Toro and Zhou (JHEP 04 (2023) 010, eq. 129) give, for a scalar current:

  ```text
  L_int ≈ (g²/4πr)[1 − (ρ²r²/32)(|v_ij| − v_ij·r̂)² + …]
  ```

  The correction depends only on the relative velocity, and vanishes for co-moving bodies and for motion along the line joining them: "the shape of Paul's question".
- But it matters when ρvr ~ ħc, so its threshold velocity falls with distance; it is not a fixed v\*. A 120 km/s threshold at 1 kpc needs ρ = 1.6×10⁻²³ eV, and one ten times smaller at 10 kpc (check I4).
- It is worked out only for a scalar current. No gravitational (tensor) version exists, and the record has no such field.

The investigation's run-3 pre-registration missed this framework (`notes/velocity-gated-gravity.md` §11).

## What follows

- **For the record's contact gate:** tree-level exchange of the X of #11 §7 is excluded as its mechanism, and both derivations of the gate-mechanism note conclude that no local carrier of finite spin delivers the gate (`notes/gate-mechanism.md` §3). Flag 55 awaits Paul's ruling.
- **For the long-range conjecture:** no field of the record, and no field of finite spin, carries it; the conjecture is tested as a hypothesis in its own right ([Conjecture: a long-range velocity-gated attraction among χ](/wiki/dark-matter/momentum-clumping/long-range-gated-attraction)).

## Sources

- `notes/velocity-gated-gravity.md` (2026-10-28, not reviewed) §9 — finite spin, the no-go theorems, the tower, the medium and continuous spin; §5 — no carrier in the record; §11 — the run-3 pre-registration's miss
- `notes/gate-mechanism.md` (2026-10-28, not reviewed) §2 — the record's X, the exact form needing every spin; §3 — no local carrier of finite spin; §4 — a preferred frame
- `verify/velocity_gated_gravity.py` section I — the spin-J residues, the spin needed, the tower and continuous spin ([the velocity-gated-gravity script](/wiki/method/verification/velocity-gated-gravity-script))
- `verify/gate_mechanism.py` section G — the spin-2 residue, T3 (loops) and T6 (the medium); the anchors — the Legendre and addition-theorem identities ([the gate-mechanism script](/wiki/method/verification/gate-mechanism-script))
- `review/momentum-gravity/README.md` — the investigation's runs
- `papers/broken-born-checkpoint-v2.md` §8 — the gate and the free scale m_φ
