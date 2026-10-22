---
title: "The 't Hooft–Polyakov monopole"
weight: 20
status: established
description: "The topological monopole of SU(2) → U(1) breaking by an adjoint scalar: π₂(S²) = ℤ (none for a mirror Standard Model, whose π₂ vanishes), magnetic charge 4π/g_d, and mass M = 4πf v/g_d, with f = 1 in the Bogomolny–Prasad–Sommerfield limit rising to about 1.79."
provenance: [T]
sources:
  - "notes/knot-dark-matter-standalone.md §2"
  - "notes/knot-dark-matter-standalone.md §3"
  - "notes/knot-dark-matter-standalone.md refs [15]–[16]"
  - "review/round3/referee/audit-notes.md Step 1"
  - "review/round3/referee/audit-notes.md Step 2"
  - "review/round3/referee/audit-notes.md Step 4(c)"
  - "review/round3/referee/audit-notes.md Step 4(d)"
  - "review/round3/referee/step2b.py (docstring)"
  - "review/round3/referee/step2b.out"
  - "review/round3/referee/step2b_inf.out (L = 30, 40, 60)"
  - "review/round3/referee/step2a.out 'MONOPOLE MASS RELATION'"
  - "review/round3/referee/step2a.py (f_inf)"
  - "review/v3-worklog.md 'Round-2 pending list'"
  - "review/v3-worklog.md 'v3 as drafted (2026-10-19)'"
  - "verify/soliton_obituary.py (docstring)"
  - "papers/broken-born-checkpoint-v2.md §12"
---

*The 't Hooft–Polyakov monopole is a stable, particle-like configuration of fields in a gauge theory whose SU(2) symmetry is broken to U(1) by a Higgs field in the adjoint representation; far from its core it looks like a [magnetic monopole](/wiki/electric-magnetic-duality/monopoles) of the surviving U(1). It cannot decay, because its Higgs field winds once around the space of possible vacua, a sphere, and no smooth change of the fields can undo the winding. Its mass is the symmetry-breaking scale v times 4π/g_d, with g_d the gauge coupling, times a factor f between 1 and about 1.79 set by the strength of the Higgs field's self-interaction relative to the gauge coupling. In the program it was the object of the withdrawn manuscript #14, which proposed superheavy monopoles of this kind as [dark matter](/wiki/dark-matter); that proposal is retired, and the physics on this page is textbook.*

**Status:** Established — [T] — textbook physics, cited in the withdrawn [#14](/wiki/dark-matter/candidates/soliton-candidate) without [provenance tags](/wiki/method/provenance-tags) as [15] ('t Hooft 1974; Polyakov 1974) and [16] (Prasad–Sommerfield 1975; Bogomolny 1976). [The round-3 audit](/wiki/method/review/round-3/rulings) found that both references resolve and support their use, except that the value f ≈ 1.79 is not in [16]; the referee confirmed that value by solving the field equations itself (`review/round3/referee/step2b_inf.out`). The use of this monopole as dark matter is dead ([Obituary: superheavy conjugate solitons](/wiki/dark-matter/candidates/soliton-candidate/obituary)). The explanations below are standard physics written from general knowledge [T]; references added from memory are marked †.

## The model: SU(2) broken to U(1) [T]

The simplest theory with a 't Hooft–Polyakov monopole is an SU(2) gauge theory with a real scalar field Φ in the adjoint representation, a three-component vector Φᵃ (a = 1, 2, 3) that the gauge group rotates (the Georgi–Glashow model, 1972†). The scalar potential has its minimum on a sphere:

```text
V(Φ) = (λ/4) (ΦᵃΦᵃ − v²)²          vacua: |Φ| = v,  a 2-sphere
```

The vacuum lies at one point of that sphere, say Φ = (0, 0, v); this is [spontaneous symmetry breaking](/wiki/symmetry-breaking/spontaneous-symmetry-breaking). Rotations about the third axis leave the chosen point fixed, so a U(1) subgroup survives, and its gauge field stays massless: it is the photon of the unbroken U(1). The other two gauge fields combine into charged vector bosons W± that absorb the would-be Goldstone modes and acquire a mass, as in [the Higgs mechanism](/wiki/symmetry-breaking/goldstone-and-higgs). #14 §2 describes the hidden sector it postulated in these terms: "a gauge group SU(2)_d with a real adjoint scalar Phi whose expectation value v breaks it to U(1)_d. U(1)_d stays unbroken, so the hidden photon is massless. The charged vectors W'+- have mass g_d v." In such a theory the vector bosons carry U(1) charge g_d; a fermion in the doublet of SU(2), such as #14's ψ, carries charge ±g_d/2.

The space of vacua is the coset SU(2)/U(1), which is the 2-sphere S² [T].

## Why it is stable: winding [T]

A configuration of finite energy must approach a vacuum far from its centre, so at large distance r the direction of Φ defines a map from the sphere at infinity to the sphere of vacua. Such maps fall into classes labelled by an integer, the number of times the first sphere wraps the second, and two maps of different class cannot be deformed into each other. The classes form the homotopy group π₂(S²) = ℤ. Time evolution is continuous, so the integer is conserved: a configuration with winding number one cannot decay to the vacuum, whatever its energy. The simplest such configuration is the hedgehog, in which Φ at each point of the sphere at infinity points radially outward, Φᵃ → v r̂ᵃ.

#14 §3 states it in this form: "SU(2)_d -> U(1)_d has pi_2(SU(2)/U(1)) = pi_2(S^2) = Z and supports 't Hooft-Polyakov monopoles [15], stable by topological charge."

**The general rule.** For a simply connected group G broken to a subgroup H, the second homotopy group of the vacuum manifold equals the first homotopy group of the unbroken group, π₂(G/H) = π₁(H) [T]. Since π₁(U(1)) = ℤ, any breaking of a simply connected group that leaves an unbroken U(1) produces monopoles. The integer is the same one that labels the Dirac quantization condition on the two-patch construction ([Dirac quantization](/wiki/electric-magnetic-duality/monopoles/dirac-quantization#diracs-argument-t)). Every grand unified theory, which breaks a simple group to a subgroup containing the U(1) of electromagnetism, therefore predicts monopoles, superheavy because the breaking scale is high ([the monopole problem](/wiki/electric-magnetic-duality/monopoles/monopole-problem)).

**No monopoles in the electroweak theory.** The Standard Model's electroweak breaking, SU(2) × U(1) → U(1) of electromagnetism, has a Higgs doublet whose vacuum manifold is the 3-sphere, and π₂(S³) = 0 [T]; the group SU(2) × U(1) is not simply connected, so the rule above does not apply. #14 §2 used this to constrain its hidden sector: "An exact mirror copy of the Standard Model cannot serve: the electroweak vacuum manifold is S^3, whose pi_2 vanishes, so it has no stable monopoles. The hidden gauge structure must therefore differ from ours."

## The magnetic charge [T]

Outside a core of radius about 1/m_W, where m_W = g_d v is the vector-boson mass, the massive fields have decayed and only the unbroken U(1) field remains. That field is the field of a magnetic monopole of charge

```text
g_m = 4π/g_d     (per unit winding)
```

with no Dirac string: the string of the pure U(1) description is resolved inside the core, where the full SU(2) gauge field is smooth. Against the vector bosons' charge g_d the product is 4π; against a doublet charge g_d/2 it is 2π, the minimum Dirac quantization allows. The round-3 audit put it as "The 't Hooft-Polyakov monopole with doublets realises 2 pi" (Step 1), and #14 §2 calls g_m "the Dirac minimum relative to psi's charge g_d/2" ([Dirac quantization: which charge counts](/wiki/electric-magnetic-duality/monopoles/dirac-quantization#which-charge-counts-2π-or-4π)). A weakly coupled theory, g_d small, thus has monopoles of large magnetic charge and strong mutual coupling, α_m = g_m²/4π = 1/α_W′ with α_W′ = g_d²/4π (#14 §2).

The monopole can also carry U(1) electric charge, making it a dyon (Julia and Zee, 1975†).

## The mass [T]

### The energy functional

The static solution is found from the hedgehog ansatz. The round-3 referee wrote it, with the dimensionless radius ξ = g v r, as (`review/round3/referee/step2b.py`, docstring):

```text
Φᵃ = v H(ξ) r̂ᵃ,     Aᵃᵢ = εₐᵢⱼ r̂ⱼ (1 − K(ξ))/(g r)

E = ∫₀^∞ dξ [ K′² + (K² − 1)²/(2ξ²) + ξ²H′²/2 + K²H² + μ ξ²(H² − 1)² ]    in units of 4πv/g
μ ∝ λ/g²
```

The profile functions run from K = 1, H = 0 at the centre, where the fields are regular, to K = 0, H = 1 at infinity, where the configuration is the hedgehog vacuum. The mass of the monopole is its energy, so in these units it is the number f:

```text
M = 4π f v / g_d          (#14 §3)
```

### The Bogomolny–Prasad–Sommerfield limit: f = 1

Bogomolny (1976) showed that the energy is bounded below by the magnetic charge times v [T]. Writing the energy density as a perfect square plus a total derivative, the square is non-negative and the total derivative integrates to the flux of the magnetic field weighted by Φ through the sphere at infinity, which is v times the magnetic charge 4π/g. In the units above the bound is E ≥ 1 per unit winding. It is reached only when the potential term vanishes, the limit λ → 0 at fixed v, and when the fields obey first-order equations, the Bogomolny equations. Prasad and Sommerfield (1975) had found the solution in closed form; the referee's docstring gives it as "BPS (mu=0): K = xi/sinh xi, H = coth xi - 1/xi, E = 1", where BPS stands for Bogomolny–Prasad–Sommerfield. The monopole is then exactly f = 1, M = 4πv/g_d.

### Larger self-coupling: f rises to about 1.79

For λ > 0 the potential term μξ²(H² − 1)² is non-negative and grows with μ, so the minimum energy can only rise as μ grows [T]. In the opposite limit, λ → ∞, the potential forces |Φ| = v everywhere outside the centre, H = 1, and the gauge profile K alone is varied; that value of f is the upper end. #14 §3: "The factor f is 1 in the BPS limit [16] and rises to about 1.79 at large scalar self-coupling."

The audit found that 1.79 "is not in [16] and is uncited" (Step 1, in lower case), and checked it numerically instead. The referee's solver first reproduced the closed-form solution's energy over its integration range, "BPS analytic solution energy (units 4 pi v/g): 0.983333  (expect 1)", a check the audit records as "BPS check E=1 with tail" (Step 2). It then scanned μ (`review/round3/referee/step2b.out`):

```text
mu=0.0001  status=0 f = E = 1.0039
mu=0.01    status=0 f = E = 1.0849
mu=0.1     status=0 f = E = 1.2091
mu=0.5     status=0 f = E = 1.3385
mu=1       status=0 f = E = 1.4005
mu=3       status=0 f = E = 1.4975
mu=10      status=0 f = E = 1.5901
mu=30      status=0 f = E = 1.6547
mu=100     status=0 f = E = 1.7033
mu=300     status=0 f = E = 1.7314
mu=1000    status=0 f = E = 1.7500
mu=3000    status=0 f = E = 1.7598
```

The scan integrates over a finite range of ξ and adds nothing for the field energy beyond it. Its first attempt at λ → ∞ reported "solve_bvp status=1, f_inf = E = 1.7741", where status 1 means the solver had not converged. A dedicated run with H = 1, integrating to L = 30, 40 and 60 and adding the analytic tail 1/(2L) beyond L, gave the same value each time (`review/round3/referee/step2b_inf.out`):

```text
L= 30.0 ... E(0..L)=1.76899  +tail 1/(2L)=0.01667 -> f_inf=1.7857
L= 40.0 ... E(0..L)=1.77316  +tail 1/(2L)=0.01250 -> f_inf=1.7857
L= 60.0 ... E(0..L)=1.77734  +tail 1/(2L)=0.00833 -> f_inf=1.7857
```

(The middle of each line, the solver's status message, is elided.) The run starts at ξ = 10⁻³, and the referee's `step2a.py` adds 10⁻³ for the interval from 0 to 10⁻³ that it omits: "f_inf = 1.7867   # step2b_inf.py: 1.7857 on [1e-3,L] + 1e-3 from [0,1e-3] (K~1-a xi^2)" (`review/round3/referee/step2a.py`). The audit's table lists 1.7867 as the referee's value, from its own boundary-value solver, and marks #14's value of about 1.79 as confirmed. It judges the range "f in [1, 1.79] - correct physical range (BPS to lambda->inf)" (Step 2).

### The order of magnitude

With m_W = g_d v, the mass relation reads M = f m_W/α_W′, where α_W′ = g_d²/4π: the monopole is heavier than the vector bosons by the inverse of the gauge coupling's fine-structure constant. 't Hooft's paper made this estimate for a coupling of electromagnetic strength; the audit summarizes his abstract as giving a "monopole mass of order 137 M_W" (Step 1). In a grand unified theory the same relation puts the monopole far above the breaking scale.

## How the program used it

### The soliton candidate

#14 proposed superheavy monopoles of a hidden SU(2) → U(1) sector as dark matter. The proposal was retired after round 3 ([Obituary: superheavy conjugate solitons](/wiki/dark-matter/candidates/soliton-candidate/obituary)); [#11](/wiki/history/documents/checkpoint) §12 names the candidate "superheavy 't Hooft–Polyakov monopoles of a hidden SU(2) → U(1) sector". The page's textbook physics is not what failed. The program's uses of it were these:

- **The sector.** [Round 2](/wiki/method/review/rounds-one-and-two) asked #14 to name an explicit gauge group (item R6), and the worklog's answer was this model: "SU(2) → U(1) by an adjoint Higgs; π₂(SU(2)/U(1)) = ℤ ['t Hooft 1974; Polyakov 1974]" (`review/v3-worklog.md`, 'Round-2 pending list'). As a program proposal the sector is dead ([Obituary: the hidden SU(2) → U(1) proposal](/wiki/dark-matter/candidates/soliton-candidate/hidden-sector)), and its minimal adjoint-only form is excluded on its own terms because its stable W′± overclose the universe ([W′ overclosure](/wiki/dark-matter/candidates/soliton-candidate/w-prime-overclosure)).
- **The mass relation.** v3 replaced v2's estimate: "v2's "M ~ 100 Λ_c" is replaced by M = 4π f v/g_d ≈ (21–37) v [f: Prasad–Sommerfield, Bogomolny, verified on INSPIRE]" (worklog, 'v3 as drafted (2026-10-19)'). Under #14's coupling hypothesis H the relation became "M ~ (21-37) v" (#14 §3), which the referee reproduced as "M = (20.7 - 37.1) v" (`review/round3/referee/step2a.out`, from 4π/g_d = 20.749 and 4πf_inf/g_d = 37.072). Hypothesis H and the benchmark mass died with the candidate ([Obituary: the coupling α_d ≈ 34](/wiki/dark-matter/candidates/soliton-candidate/alpha-d-coupling); [overproduction at the benchmark](/wiki/dark-matter/candidates/soliton-candidate/overproduction)).
- **The gate's model input.** `verify/soliton_obituary.py` takes "M = 4 pi f v / g_d, f = 1 (BPS) to 1.787" in its docstring, the range over which it brackets the closing mass ([the soliton-obituary script](/wiki/method/verification/soliton-obituary-script)).
- **Prior art.** The referee found the scenario already in the literature: "The DM proposal is the standard hidden 't Hooft-Polyakov-monopole scenario (Baek-Ko-Park 2013; Khoze-Ro 2014; Murayama-Shu 2009; LMW 2026)" (Step 4(d)), where DM is dark matter and LMW is Liveoak–Maharana–Wells; Baek–Ko–Park and Khoze–Ro study hidden SU(2) → U(1) monopoles together with the W′ and a dark photon (Step 4(c) item 10). See [topological dark matter in the literature](/wiki/dark-matter/candidates/soliton-candidate/prior-art).

## References

As #14 cites them (without tags; the round-3 audit found both items resolving and supporting their use, apart from f ≈ 1.79):

- [15] G. 't Hooft, Nucl. Phys. B 79, 276 (1974); A. M. Polyakov, JETP Lett. 20, 194 (1974).
- [16] M. K. Prasad, C. M. Sommerfield, Phys. Rev. Lett. 35, 760 (1975); E. B. Bogomolny, Sov. J. Nucl. Phys. 24, 449 (1976).

Added by the wiki from model memory (†):

- H. Georgi, S. L. Glashow (1972)†: the SU(2) model with an adjoint scalar.
- B. Julia, A. Zee (1975)†: dyons in the same model.
- E. J. Weinberg, *Classical Solutions in Quantum Field Theory* (Cambridge University Press)†: textbook treatment of monopoles, the Bogomolny bound and the homotopy classification.

## Used by

- [Dirac quantization and the DSZ pairing](/wiki/electric-magnetic-duality/monopoles/dirac-quantization) — the monopole's charge 4π/g_d realizes the 2π normalization relative to a doublet.
- [The Kibble mechanism](/wiki/electric-magnetic-duality/monopoles/kibble-mechanism) — how a cooling universe makes these monopoles.
- [Obituary: the hidden SU(2) → U(1) proposal](/wiki/dark-matter/candidates/soliton-candidate/hidden-sector) — the hidden sector whose monopoles were the candidate.
- [Overproduction at the benchmark](/wiki/dark-matter/candidates/soliton-candidate/overproduction) — the mass relation enters the closing mass M\*.
- [Obituary: superheavy conjugate solitons](/wiki/dark-matter/candidates/soliton-candidate/obituary) — the candidate itself.
- [The soliton-obituary script](/wiki/method/verification/soliton-obituary-script) — the model input f = 1 to 1.787.
- [W′ overclosure: the minimal sector is excluded](/wiki/dark-matter/candidates/soliton-candidate/w-prime-overclosure) — the charged vector bosons that the same breaking leaves.
- [Obituary: the coupling α_d ≈ 34](/wiki/dark-matter/candidates/soliton-candidate/alpha-d-coupling) — a soliton's mass enhanced by the inverse of the elementary coupling.
- [Open: the topological loophole](/wiki/dark-matter/momentum-clumping/topological-loophole) — the retired candidate that was to fill it.
- [Conjugate monopoles as ontology](/wiki/electric-magnetic-duality/conjugate-monopoles) — the standard example of a topological soliton.
- [The symplectic charge lattice](/wiki/electric-magnetic-duality/symplectic-charge-lattice) — magnetic charges that appear only on solitons.
- [The 'framework does no work' critique](/wiki/program/framework-does-no-work) — #14's hidden monopoles as the standard scenario of the literature.
- [Row 8: no monopoles of our sector](/wiki/predictions/monopole-null) — grand unified monopoles as solitons with masses set by the unification scale.

## Sources

- `notes/knot-dark-matter-standalone.md` §2, §3, refs [15]–[16] — the sector, the topology, the mirror-Standard-Model obstruction, the mass relation and the references (withdrawn manuscript; the textbook statements are not what failed).
- `review/round3/referee/audit-notes.md` Step 1, Step 2, Step 4(c), Step 4(d) — the citation check and "realises 2 pi"; the confirmation of f; the prior art.
- `review/round3/referee/step2b.py`, `review/round3/referee/step2b.out`, `review/round3/referee/step2b_inf.out` — the hedgehog ansatz, the energy functional, the closed-form solution, the μ scan and f_inf = 1.7857.
- `review/round3/referee/step2a.py`, `review/round3/referee/step2a.out` — f_inf = 1.7867 and the reproduced mass relation.
- `review/v3-worklog.md` 'Round-2 pending list' (R6), 'v3 as drafted (2026-10-19)' — the named group and the mass relation that replaced v2's.
- `verify/soliton_obituary.py` — the range f = 1 to 1.787 used in the gate.
- `papers/broken-born-checkpoint-v2.md` §12 — the candidate named as 't Hooft–Polyakov monopoles.
