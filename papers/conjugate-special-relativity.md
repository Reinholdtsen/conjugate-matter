# Special Relativity in the Comatter Framework
### The kinematics of the momentum polarization: a second light cone, force boosts, and the invariant length

*Working paper of the Comatter program (until 2026-10-26, the Broken-Born program). House conventions apply: each section opens with a plain-language passage (italic); claims are tagged [D] derived, [T] literature, [P] postulate, [O] open, with † marking memory-sourced citations pending verification. The Euclidean/Lorentzian caveat of the main checkpoint is inherited throughout.*

**Abstract.** If Born reciprocity is exact and spontaneously broken, phase space carries two causal structures: the familiar light cone of position space and its image in momentum space. The momentum-space cone bounds the rate of momentum change — a maximum force, c̃ = ℏc/λ², equal to c⁴/G ≈ 1.2 × 10⁴⁴ N at the Planck value of the Born length. We develop the special relativity of the momentum polarization: the dual Lorentz group ("force boosts"), the composition law for forces, force-dilation of clocks, the duality of the mass shell and an invariant-length shell, and the identification of dual-inertial frames with free fall. The construction explains why force appears exactly additive in all terrestrial and astrophysical experience short of black-hole mergers, ties the framework to the maximum-force conjecture in general relativity, and locates the one natural arena where dual-kinematic corrections could be order unity.

---

## 1. Two causal cones

*In plain terms: Our universe has a speed limit — nothing outruns light through space. If position and momentum are true equals, there must be a second limit of the same kind governing motion through momentum space. Motion through momentum space is what we call force. So the twin of the speed of light is a maximum force, and its natural value is enormous: about 10⁴⁴ newtons, the scale black holes reach when they collide.*

The broken vacuum equips phase space with H = diag(g, g⁻¹) [D — compatibility theorem]: position space carries the metric g and momentum space its inverse. Each metric defines a null cone. Ours bounds trajectories x(t): |dx/dt| ≤ c. The dual cone bounds trajectories p(t):

$$
\left|\frac{d\mathbf p}{dt}\right| \;\leq\; \tilde c \;=\; \frac{\varepsilon}{\lambda/c} \;=\; \frac{\hbar c}{\lambda^2},
$$

where λ is the Born length and ε = ℏ/λ its conjugate momentum scale. The only length the gravitational sector supplies is the Planck length, λ² = ℏG/c³, giving

$$
\boxed{\ \tilde c = \frac{c^4}{G} \approx 1.2\times10^{44}\ \mathrm{N}.\ }
$$

This value is not unfamiliar. A maximum force c⁴/4G was conjectured within general relativity as the "maximum tension principle" [1†], with a companion maximum luminosity c⁵/4G approached by binary black-hole mergers; a maximal *acceleration* from a phase-space metric is older still [2†]. The framework's contribution is a reason: a maximum force is the statement that nothing outruns light in the momentum polarization. The factor of 4 is not fixed here [O], and the conjecture's contested status in the GR literature is noted [T]. One refinement from the main program: the dual cone is the causal structure of the *slaved* geometry g⁻¹; the independently dynamical part of momentum-space geometry is the massive field X, which modifies the dual cone only at short range in momentum [D — §7 of the checkpoint].

## 2. Force boosts

*In plain terms: Einstein's relativity is built from "boosts" — the rule for translating between observers moving at constant velocity. The momentum version is built from translating between observers under constant force. The same algebra follows: forces stop adding linearly near the maximum, exactly as velocities stop adding linearly near light speed, and observers under different forces disagree about simultaneity — not across distances, but across differences in momentum.*

The dual interval on (t, **p**) is ds̃² = c̃²dt² − d**p**², preserved by rotations in the (c̃t, p) planes — the dual Lorentz group [D — structural]. A dual boost of parameter F carries the force-free frame to a uniformly forced one:

$$
\mathbf p' = \tilde\gamma(\mathbf p - \mathbf F t), \qquad t' = \tilde\gamma\left(t - \frac{\mathbf F\cdot\mathbf p}{\tilde c^2}\right), \qquad \tilde\gamma = \left(1 - F^2/\tilde c^2\right)^{-1/2}.
$$

Three consequences transcribe directly from the familiar case:

1. **Relativity of simultaneity across momentum.** Events at equal t but different p are non-simultaneous in a forced frame — simultaneity depends on momentum location as, for us, it depends on position.
2. **Force composition.** With dual rapidity F = c̃ tanh φ and rapidities additive,
$$
F_1 \oplus F_2 = \frac{F_1 + F_2}{1 + F_1 F_2/\tilde c^2},
$$
so forces saturate at c̃ rather than accumulate without bound [D].
3. **The Galilean limit is everything we know.** For F ≪ c̃ the transformation reduces to the ordinary passage to an accelerated frame, with its familiar pseudo-forces, and composition reduces to addition. The strongest sustained macroscopic force in nature — on a kilogram at a neutron-star surface, ~10¹² N — gives γ̃ − 1 ≈ ½(F/c̃)² ~ 10⁻⁶⁵. Force *looks* exactly additive for the same reason velocity looked exactly additive before 1905: no accessible process approaches the limit. The single natural exception is a comparable-mass black-hole merger, which operates at F ~ c̃ by construction; if dual-kinematic corrections have any observable expression, merger and ringdown dynamics are where they would be order unity [O — flagged, not derived].

## 3. Force dilation and its mirror

*In plain terms: In ordinary relativity, fast clocks run slow. In the momentum version, hard-pushed clocks run slow — a system under enormous force ages more slowly than an unforced one, by the same square-root formula with force replacing velocity. Below 10⁴³ newtons the effect is utterly negligible, which is why nobody has noticed.*

The dual proper time of a trajectory p(t) is

$$
d\tilde\tau = dt\sqrt{1 - \frac{1}{\tilde c^2}\left|\frac{d\mathbf p}{dt}\right|^2} = dt\sqrt{1 - F^2/\tilde c^2},
$$

so sustained force dilates the internal evolution of (conjugate-polarized) systems as sustained velocity dilates ours [D — structural; which physical clocks respond is polarization-dependent, O]. The mirror of length contraction: a forced system's extent *in momentum* — its momentum spread — contracts by γ̃ in the force direction. Both effects are unmeasurably small below merger-scale forces (§2).

## 4. Invariants: the mass shell and the length shell

*In plain terms: In our relativity, the quantity every observer agrees on is a particle's mass. In the momentum version, the corresponding invariant is a length — every particle of the mirror polarization carries an unchangeable size the way ours carry an unchangeable mass. This was Born's original hope in 1938: a physics with a fundamental mass and a fundamental length on equal footing. A consistency check falls out: length times maximum force is an energy, and at the Planck length it is exactly the Planck energy.*

Our invariant hypersurface is the mass shell, p_μp^μ = m²c². Its Born image is a position-space hyperboloid,

$$
x_\mu x^\mu = \lambda_\chi^2,
$$

an **invariant-length shell**: conjugate quanta are characterized by an irreducible extent λ_χ as ours are by mass [D — structural; this recovers Born's 1938–49 program of a self-dual physics with both m and λ fundamental [3†, 4†]]. Two anchors:

- **Closure at the self-dual point.** The dual rest-energy relation is E = λ c̃ (length × maximum force). At λ = l_P: E = l_P · c⁴/G = √(ℏc⁵/G) — the Planck energy, exactly [D]. The dual E = mc² returns the right corner of physics.
- **Contact with phenomenology.** The conjugate quantum's invariant extent fixes its intrinsic momentum-space width μ ~ ℏ/λ_χ — which is precisely the gate scale of the dark-matter sector, v* = √2 μ/m_χ. The knee in the dark-matter self-interaction curve is, in this reading, a *dual-relativistic invariant of the dark sector* made visible in galactic dynamics [D — structural].

## 5. Inertia, dualized

*In plain terms: In their mechanics, "standing still" means feeling no force — which, on our books, is free fall. An astronaut coasting in orbit is, to the momentum polarization, at rest. Their version of uniform motion is constant force; their version of inertia is resistance not to acceleration but to* changes *in force. And their principle of relativity — physics looks the same in all unforced frames — is a statement we already believe under another name: the equivalence principle.*

The dual-inertial class consists of trajectories with dp/dt constant: rest (dp/dt = 0, i.e., force-free motion — our free fall) and uniform dual motion (constant force — our Rindler frames). The dual first law: an undisturbed system maintains its state of force. The dual second law, structurally, makes λ_χ the measure of resistance to force-*change* [conjecture-tier; the full dual dynamics awaits the formalization of §6]. The handshake worth recording [D — structural]: *the dual principle of relativity — equivalence of all force-free frames — is the equivalence principle*, arrived at from kinematics rather than gravitation. In this framework Einstein's two relativity principles are the two polarizations of one statement.

## 6. What is shared, what is broken, what is open

*In plain terms: The two relativities are not perfect mirror images, because the universe broke the symmetry. They share time, and they share gravity's pull. But our light cone is enforced by a massless field and theirs by a massive one, so ours reaches across the universe and theirs is short-ranged. And a technical honesty note: the tidiest version of this construction treats space and momentum as partners while leaving time alone; the fully four-dimensional version, in which energy and time also trade places, is deeper and not yet built.*

Shared: the time coordinate (in the 3+1 presentation used here) and the massless graviton, so both polarizations fall identically. Broken: the long-range/short-range asymmetry — our null structure is policed by massless gravity, the dual structure's dynamical part by the massive X, so dual-geometric effects are Yukawa-cut in momentum [D — checkpoint §7]. Open [O]: the fully covariant construction with the four-dimensional Born map (t ↔ E), in which the dual "time" direction is our energy axis — the natural home of this paper's kinematics and a required step before the dual dynamics (their Maxwell, their field theory) can be written. One free consistency check already available: since our massless dispersion E = c|p| *is* the dual null cone, the Fermi-LAT bounds excluding linear photon-dispersion violations [T] constrain both cones at once — every test of our light cone's rigidity has been, unknowingly, a test of theirs.

## 7. Summary of tethers

Kinematic structure fixed [D]: dual interval, force boosts, γ̃, force-composition law, force dilation, invariant-length shell, dual-inertial = free-fall identification. Numerical anchors: c̃ = c⁴/G; E(l_P) = E_Planck; γ̃ − 1 ~ 10⁻⁶⁵ at neutron-star forces. Literature tethers: maximum-tension conjecture [1†], maximal acceleration [2†], Born's self-dual program [3†, 4†]. Open [O]: the factor 4; the 4D covariant construction; dual dynamics; whether merger-band gravitational-wave data can bound dual-kinematic corrections.

---

## References

*† = cited from model memory; verify before external use.*

[1]† G. W. Gibbons, "The maximum tension principle in general relativity," Found. Phys. 32, 1891 (2002), hep-th/0210109; C. Schiller, "General relativity and cosmology derived from principle of maximum force," Int. J. Theor. Phys. 44, 1629 (2005).
[2]† E. R. Caianiello, "Is there a maximal acceleration?" Lett. Nuovo Cim. 32, 65 (1981).
[3]† M. Born, "A suggestion for unifying quantum theory and relativity," Proc. R. Soc. Lond. A 165, 291 (1938).
[4]† M. Born, "Reciprocity theory of elementary particles," Rev. Mod. Phys. 21, 463 (1949).

*Companion documents: the working checkpoint (broken-born-checkpoint-v2.md) for the geometric sector this paper's causal structure inherits; the popular account (universes-other-half.md) for the framework at large.*
