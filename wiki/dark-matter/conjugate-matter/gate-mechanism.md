---
title: "The gate mechanism: X exchange over fiber overlap"
weight: 30
status: alive
description: "χ couples to X through the dual stress; integrating X out gives a contact operator acting over the overlap of momentum-fiber wavepackets, with μ the χ quantum's fiber width."
provenance: [D]
sources:
  - "notes/debt1a-ii-X-classification.md §4"
  - "notes/debt1a-ii-X-classification.md §1"
  - "notes/debt1a-ii-X-classification.md §3"
  - "notes/debt1a-geometric-core.md §E"
  - "notes/debt1a-geometric-core.md §D"
  - "notes/broken-born-theory.md 'Addendum (v0.3, overnight)'"
  - "notes/broken-born-theory.md 'Addendum (v0.4)'"
  - "notes/broken-born-theory.md §3"
  - "notes/broken-born-theory.md §5.1"
  - "papers/broken-born-checkpoint-v2.md §8"
  - "papers/broken-born-checkpoint-v2.md §14 item 3"
  - "notes/debt1a-iv-beta-coefficients.md §5"
  - "notes/broken-born-program-v1.md §6"
  - "papers/conjugate-special-relativity.md §4"
  - "HANDOFF.md §2"
  - "HANDOFF.md §4"
---

*The gate mechanism is the program's derivation of [the velocity gate](/wiki/dark-matter/conjugate-matter/velocity-gate): two particles of [conjugate matter](/wiki/dark-matter/conjugate-matter) interact by exchanging the massive [momentum graviton X](/wiki/gravity/momentum-graviton), and they can do so only where their wavepackets overlap in momentum space. A conjugate quantum has a finite width μ along the momentum directions, as an atomic nucleus has a finite radius in space. A nucleus's size cuts off its scattering at large momentum transfer; the χ quantum's momentum width cuts off its interaction at large relative momentum, which is the same construction with position and momentum exchanged. Because X is heavy, its exchange acts as a contact interaction, and the overlap of the two wavepackets supplies the gate. The derivation is structural: it fixes what the interaction depends on, but the exact shape of the cutoff depends on a propagator and a profile that no document has computed.*

**Status:** Alive — [D — structural, with one honest downgrade] in calc note #6 (`notes/debt1a-ii-X-classification.md` §4), [D — structural] in calc note #5 (`notes/debt1a-geometric-core.md` §E), and [D — mechanism; shape [O]] in the checkpoint (#11 §8) — no explicit X propagator, vertex or overlap integral exists in any source, and no `verify/` script covers it.

## The statement

[The checkpoint](/wiki/history/documents/checkpoint) states the result in one clause of its amplitude for χ: the dependence on the incoming relative momentum k is "delivered by X-exchange between dual-stress bilinears, with μ the χ quantum's intrinsic momentum-fiber width [D — mechanism; shape [O]]" (#11 §8). The derivation behind it is calc note #6's paragraph on the gate, in [the Debt-1 calc notes](/wiki/history/documents/debt-1-notes):

> "**Gate (Debt 2).** Integrating out massive X between χ bilinears gives the contact four-χ operator. The relative-momentum dependence enters through the χ quanta's **intrinsic momentum-space extent**: p-polarized quanta are extended objects on the momentum fiber with width μ, and they exchange X only over their fiber overlap — the dual of how x-extended composites acquire form factors F(qR). Wavepacket overlap of Gaussian profiles gives exactly e^{−(p₁−p₂)²/2μ²} — the postulated gate, with **μ = the χ quantum's own p-width**, a physical identification the EFT lacked. *However*: tree-level exchange with generic vertices yields rational (power-law-tailed) gates; the Gaussian requires the Gaussian fiber profile." (`notes/debt1a-ii-X-classification.md` §4)

EFT is effective field theory, here the lab notebook's v0.1 amplitude, in which μ was a free scale. The momentum fiber is the set of momentum directions of phase space attached to each point of spacetime.

## Background [T]

Three pieces of standard physics carry the argument.

### Integrating out a heavy carrier

A force carried by a field of mass M has a propagator proportional to 1/(q² + M²) in the momentum transfer q. When every transfer in a process is small compared with M, the propagator is nearly the constant 1/M², and the exchange acts as a contact interaction among the four external particles, with a strength proportional to the square of the coupling divided by M² [T]. The standard example is Fermi's four-fermion theory of beta decay, the low-energy form of the exchange of the heavy W boson [T]. In position the contact form means the force has a range of order 1/M, short compared with the distances of interest [T]. Replacing the heavy field by the contact term it produces is called integrating it out, and it is the basic step of effective field theory [T].

### Form factors

An object of finite size scatters as a point particle multiplied by a form factor F(q), the Fourier transform of its charge distribution [T]. For an object of radius R, F(q) is close to 1 when the transfer is small, qR ≪ 1, and falls off once q exceeds about 1/R, because the scattered waves from different parts of the object then interfere destructively [T]. The shape of the falloff follows the shape of the distribution: a Gaussian distribution has a Gaussian form factor, while a distribution with an exponential edge has a rational form factor that falls off as a power of q [T]. Electron scattering measures the sizes of nuclei and of the proton in this way [T]. Calc note #6 calls such objects "x-extended composites": extended in position, with form factors in the transfer q.

### Wavepacket overlap

A quantum state with a definite profile in momentum, of width μ, is a wavepacket in momentum space [T]. The overlap integral of two Gaussian profiles is itself a Gaussian in the separation of their centres [T]; its width depends on how the widths of the profiles are defined.

## The derivation as the sources give it

1. **The coupling.** Conjugate matter couples universally to the generalized metric H (postulate [P4](/wiki/program/postulates/p4-polarized-matter)), and to the part of H that X carries through the [dual stress T̃](/wiki/dark-matter/conjugate-matter/dual-stress), "moments involving momentum-derivatives of the χ bilinear" (#5 §E).
2. **The exchange.** "Exchange of X between two such bilinears yields a four-point amplitude that depends on the **incoming relative momenta** of the pair — the variable no x-local mediator can produce, and exactly the variable the gate was postulated in" (#5 §E). Here "x-local" means local in position.
3. **X is massive.** Calc note #6 shows that X cannot be massless ([why X must be massive](/wiki/gravity/momentum-graviton/forcing-chain)) and acquires its mass when the vacuum selects a polarization, "mass M_X = the polarization-breaking scale" (§3; [the gravitational Higgs mechanism](/wiki/gravity/momentum-graviton/gravitational-higgs)).
4. **Integrating it out.** Because X is massive, "Integrating out massive X between χ bilinears gives the contact four-χ operator" (#6 §4): a contact interaction among four χ fields, as in the background above.
5. **Where the momentum dependence enters.** A contact interaction alone carries no dependence on k. #6 locates it in the χ quanta themselves: "p-polarized quanta are extended objects on the momentum fiber with width μ, and they exchange X only over their fiber overlap". The coupling acts only where the two quanta's momentum profiles overlap, so it falls off when their momenta differ by much more than μ.
6. **The Gaussian case.** If the profiles are Gaussian, the overlap "gives exactly e^{−(p₁−p₂)²/2μ²} — the postulated gate", which identifies μ with "the χ quantum's own p-width" (#6 §4). The note states this result without showing the overlap integral.
7. **The downgrade.** "*However*: tree-level exchange with generic vertices yields rational (power-law-tailed) gates; the Gaussian requires the Gaussian fiber profile" (#6 §4). Tree-level amplitudes are built from propagators and polynomial vertices, which are rational functions of the momenta [T]; a Gaussian can enter only through the external profiles. Which case holds is [Open: the gate shape (OP4)](/wiki/dark-matter/conjugate-matter/gate-shape).

The tag on #6's section is "[D — structural, with one honest downgrade]". The steps are stated, not computed: no source writes the χ–X vertex, the X propagator on the momentum fibers, the χ quantum's profile or the overlap integral. Step 3 rests on a chain that calc note #6 calls "the Euclidean-rigorous skeleton" (§3), derived for a positive-definite metric; its extension to the Lorentzian signature of spacetime is open, item 3 of #11 §14 ([Open: Lorentzian dressing](/wiki/phase-space/born-geometry/lorentzian-dressing)).

## Position and momentum exchanged

#6 calls the fiber overlap "the dual of how x-extended composites acquire form factors F(qR)". The correspondence is a swap of position and momentum, the swap that [Born reciprocity](/wiki/phase-space/reciprocity/born-reciprocity) performs:

| | Extended in position (a nucleus) | Extended in momentum (a χ quantum) |
| --- | --- | --- |
| Size | radius R | fiber width μ |
| The interaction is cut off when | the transfer q exceeds about 1/R [T] | the two momentum profiles stop overlapping, for p₁ − p₂ large compared with μ (#6 §4) |
| Variable of the cutoff | q, the momentum transfer | p₁ − p₂ in #6 §4; k, the incoming relative momentum, in #11 §8 |
| Gaussian profile gives | a Gaussian form factor [T] | the Gaussian gate (#6 §4) |

A nucleus is extended in the variable conjugate to q, and its form factor depends on q; a χ quantum is extended in momentum, and the gate depends on how far apart in momentum the two quanta are. In signal terms, an ordinary contact force acts where two waveforms overlap; the gate acts only where their spectra overlap as well.

## What μ is

Since the v0.4 addendum, μ is a property of a single χ quantum: "μ is identified as the χ quantum's intrinsic momentum-fiber width, with a Gaussian gate iff the fiber profile is Gaussian" ([the lab notebook](/wiki/history/documents/lab-notebook), #1 'Addendum (v0.4)'). Before it, μ was a free scale of the momentum-space sector (#1 §3).

The lab notebook converts μ into the gate velocity, v\* ≡ √2μ/m_χ (#1 §5.1), the location of the knee in [the gated scattering law](/wiki/dark-matter/conjugate-matter/scattering-law). #11 does not restate this definition. At [the scattering benchmark](/wiki/dark-matter/conjugate-matter/benchmark) the notebook gives "μ = m_χv\*/√2 ≈ 20 keV (α̃ ≈ 1)" (#1 §5.1), a number found only in the lab notebook and not machine-checked.

## What it paid

The mechanism is the payment on Debt 2 ([the three debts](/wiki/history/debts)). Calc note #8's close-out: "**Debt 2:** mechanism paid (X-exchange, μ = fiber width); shape completion open (Gaussian vs rational tail — now also an observable discriminant)" (`notes/debt1a-iv-beta-coefficients.md` §5). [The handoff](/wiki/history/documents/handoff) lists "gate = X-exchange; gate variable = incoming relative momentum; μ = χ's momentum-fiber width" among the live results (`HANDOFF.md` §2).

It also cost the lab notebook's sharpest prediction. #6 §4 continues:

> "Honest downgrade to the flagship: **row 1's 'exponential cliff' weakens to 'sharp knee at v\*, with the tail shape (Gaussian vs rational) a diagnostic of the vertex completion.'** The knee's existence and location are robust; its steepness is model-internal information, not a guaranteed exponential."

(The note writes v_\* for v\*.) The knee is tested in [row 1](/wiki/predictions/self-interaction-knee) of the predictions table.

## Scope and caveats

- **Structural only.** The mechanism fixes the variable of the gate and identifies μ; it does not compute F. #11 §8 tags the mechanism [D] and the shape [O].
- **Two exponents.** The overlap form e^{−(p₁−p₂)²/2μ²} and the lab notebook's postulated e^{−k²/μ²}, with k = m_χv_rel/2 (#1 §3), are not reconciled in any source ([the velocity gate](/wiki/dark-matter/conjugate-matter/velocity-gate#two-conventions-not-reconciled)).
- **The transfer mediator.** The amplitude of #11 §8 keeps the factor 4πα̃m_χ/(q² + m_φ²), with m_φ the mass of the carrier of the momentum transfer. No source relates m_φ to M_X, and the benchmark's choice m_φ ~ m_χ was made in v0.1, before the mechanism was found (#1 §5.1).
- **The strength.** The mechanism explains why the interaction depends on relative momentum, not why it is as strong as dwarf-galaxy cores require; that is [Open: the dual-stress enhancement (OP5)](/wiki/dark-matter/conjugate-matter/dual-stress-enhancement).

## The reading in conjugate special relativity

The paper on [conjugate special relativity](/wiki/conjugate-relativity), #13, gives μ a kinematic origin. Its Born image of the mass shell is an "invariant-length shell": "conjugate quanta are characterized by an irreducible extent λ_χ as ours are by mass" [D — structural] (§4). It then reads the gate scale from that extent:

> "The conjugate quantum's invariant extent fixes its intrinsic momentum-space width μ ~ ℏ/λ_χ — which is precisely the gate scale of the dark-matter sector, v\* = √2 μ/m_χ. The knee in the dark-matter self-interaction curve is, in this reading, a *dual-relativistic invariant of the dark sector* made visible in galactic dynamics [D — structural]." (#13 §4)

The relation μ ~ ℏ/λ_χ is a reciprocal relation between a width in momentum and an extent in position, the relation between the widths of a waveform and its spectrum. #13 has not been through review, and it uses both λ_χ and m_χ for the conjugate quantum, while the checkpoint gives χ ordinary kinematics with mass m_χ; the two are not reconciled ([the invariant-length shell](/wiki/conjugate-relativity/invariant-length-shell)).

## Superseded: earlier forms of the mechanism

The mechanism reached its present form in three steps.

- **v0.1: a scale of the momentum-space metric.** The lab notebook routed χ's self-interaction "through the g̃ block" and took μ as "a scale μ of the g̃ sector", with the gate's existence a postulate [P] (#1 §3); see [the velocity gate](/wiki/dark-matter/conjugate-matter/velocity-gate#superseded-the-gaussian-gate-of-v01).
- **Calc note #5: μ from the masses.** The first identification of the carrier wrote the scale in terms of two masses:

  ```text
  gate = momentum-graviton exchange,    μ ↔ (M_X, M_B) parametrically
  ```

  (`notes/debt1a-geometric-core.md` §E). M_B is the mass scale of the lab notebook's geometric action, S_H = ½M_B²∫_Σ √|H| R_B[H], an integral over the section Σ, from which the Planck mass follows (#1 §3). Calc note #6 replaced the relation with μ = the χ quantum's own width, a property of the matter field rather than of the geometry, and no later document returns to M_X and M_B as the source of μ.
- **Calc note #5: an auxiliary X.** #5 §D listed three possible outcomes for X at quadratic order. The second, an auxiliary X with no derivatives, would have been integrated out to "a *contact, momentum-structured* four-χ operator, i.e. the gate delivered directly", and #5 §E notes that "outcome 2 gives it most cheaply". Calc note #6 §1 closed that route: constant shifts of X are exact symmetries, so "'auxiliary X' (the soft outcome 2) is off the table at the fundamental level: X appears only through derivatives, so it propagates or it doesn't exist" ([shift symmetry](/wiki/gravity/momentum-graviton/shift-symmetry)). The contact operator of the current mechanism comes from integrating out a massive, propagating X instead.

## Chat-only: the gate as a dual Newtonian limit

[The handoff](/wiki/history/documents/handoff) records, among results that exist only in the original conversation, a comparison of the program's field equations with general relativity that ends in the gate: "dual Newtonian limit = Yukawa in momentum = the gate" (`HANDOFF.md` §4). No document derives a Yukawa form in momentum or describes the gate as a Newtonian limit; the documented counterpart is the mechanism on this page. Its status is conjecture; see [Two gravitational charges and the conjugate field equations (chat-only)](/wiki/gravity/momentum-graviton/chat-only-results).

## Sources

- `papers/broken-born-checkpoint-v2.md` §8 — the checkpoint's statement and tags; §14 item 3 — Lorentzian dressing open
- `notes/broken-born-program-v1.md` §6 — v1's statement, the same as #11's
- `notes/debt1a-ii-X-classification.md` §4 — integrating out X, fiber overlap, the Gaussian case, the rational-tail downgrade, the cliff weakened to a knee; §3 — X massive, M_X the polarization-breaking scale, the Euclidean-rigorous skeleton; §1 — auxiliary X excluded by the shift symmetry
- `notes/debt1a-geometric-core.md` §E — the four-point amplitude; the superseded μ ↔ (M_X, M_B) identification; §D — the auxiliary outcome
- `notes/debt1a-iv-beta-coefficients.md` §5 — Debt 2's mechanism paid, shape open
- `HANDOFF.md` §2 — the mechanism among the live results; §4 — the chat-only dual Newtonian limit
- `papers/conjugate-special-relativity.md` §4 — μ ~ ℏ/λ_χ as the gate scale
- `notes/broken-born-theory.md` 'Addendum (v0.3, overnight)', 'Addendum (v0.4)' — the mechanism and the fiber width in the lab notebook; §3 — the v0.1 carrier and M_B in S_H; §5.1 — v\* ≡ √2μ/m_χ, μ ≈ 20 keV, m_φ ~ m_χ
