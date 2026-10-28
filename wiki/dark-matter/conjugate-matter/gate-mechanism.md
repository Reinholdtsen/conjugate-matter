---
title: "The gate mechanism: X exchange over fiber overlap"
weight: 30
status: alive
description: "The record's derivation of the gate: χ couples to X through the dual stress, and integrating X out gives a contact operator acting over the overlap of momentum-fiber wavepackets, with μ the χ quantum's fiber width; the gate-mechanism note of 2026-10-28 finds that exchanging X cannot produce the gate, and flag 55 proposes [P] for the gate and [O] for its mechanism, pending Paul's ruling."
provenance: [D]
sources:
  - "notes/debt1a-ii-X-classification.md §4"
  - "notes/debt1a-ii-X-classification.md §1"
  - "notes/debt1a-ii-X-classification.md §2"
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
  - "review/wiki-build-flags.md items 17, 55"
  - "notes/gate-mechanism.md §1"
  - "notes/gate-mechanism.md §2"
  - "notes/gate-mechanism.md §3"
  - "notes/gate-mechanism.md §4"
  - "notes/gate-mechanism.md §5"
  - "notes/gate-mechanism.md §6"
  - "verify/gate_mechanism.py"
  - "review/momentum-gravity/README.md"
  - "review/momentum-gravity/preregistration-run4.md"
---

*The gate mechanism is the program's derivation of [the velocity gate](/wiki/dark-matter/conjugate-matter/velocity-gate): two particles of [conjugate matter](/wiki/dark-matter/conjugate-matter) interact by exchanging the massive [momentum graviton X](/wiki/gravity/momentum-graviton), and they can do so only where their wavepackets overlap in momentum space. A conjugate quantum has a finite width μ along the momentum directions, as an atomic nucleus has a finite radius in space. A nucleus's size cuts off its scattering at large momentum transfer; the χ quantum's momentum width cuts off its interaction at large relative momentum, which is the same construction with position and momentum exchanged. Because X is heavy, its exchange acts as a contact interaction, and the overlap of the two wavepackets supplies the gate. The derivation is structural: it fixes what the interaction depends on, but the exact shape of the cutoff depends on a propagator and a profile that no document has computed. A working note of 2026-10-28 tested the derivation and found that it does not hold. When two particles exchange X, each end of the exchange depends only on how much momentum passed through it, so the exchange depends on the pair's relative velocity only through corrections whose velocity scale is the speed of light; at galactic speeds they change the interaction by parts in ten million, where the gate would switch it off. The note proposes that the gate return to the status of a postulate and that its mechanism be counted open. That proposal, flag 55, awaits Paul's ruling, and the checkpoint still tags the mechanism as derived.*

**Status:** Alive in the record, and not derived according to a later note — the record's tags are [D — structural] in calc note #6 (`notes/debt1a-ii-X-classification.md` §4), whose tag also records one downgrade (step 7 below), [D — structural] in calc note #5 (`notes/debt1a-geometric-core.md` §E), and [D — mechanism; shape [O]] in the checkpoint (#11 §8) — no explicit X propagator, vertex or overlap integral exists in any source. `notes/gate-mechanism.md` (2026-10-28; two independent derivations, the second blind and pre-registered; not reviewed) finds that exchanging the X of #11 §7 cannot produce the gate, and flag 55 in `review/wiki-build-flags.md`, rated high, proposes [P] for the gate F(k²/μ²) and μ and [O] for the mechanism, pending Paul's ruling; #11 is unchanged until he rules ([exchanging X cannot produce the gate](#exchanging-x-cannot-produce-the-gate); [what flag 55 proposes](#what-flag-55-proposes)). The note's arithmetic and algebra are rerun in `verify/gate_mechanism.py` ([the gate-mechanism script](/wiki/method/verification/gate-mechanism-script)), which does not test their physics.

## The statement

[The checkpoint](/wiki/history/documents/checkpoint) states the result in one clause of its amplitude for χ: the dependence on the incoming relative momentum k is "delivered by X-exchange between dual-stress bilinears, with μ the χ quantum's intrinsic momentum-fiber width [D — mechanism; shape [O]]" (#11 §8). The derivation behind it is calc note #6's paragraph on the gate, in [the Debt-1 calc notes](/wiki/history/documents/debt-1-notes):

> "**Gate (Debt 2).** Integrating out massive X between χ bilinears gives the contact four-χ operator. The relative-momentum dependence enters through the χ quanta's **intrinsic momentum-space extent**: p-polarized quanta are extended objects on the momentum fiber with width μ, and they exchange X only over their fiber overlap — the dual of how x-extended composites acquire form factors F(qR). Wavepacket overlap of Gaussian profiles gives exactly e^{−(p₁−p₂)²/2μ²} — the postulated gate, with **μ = the χ quantum's own p-width**, a physical identification the EFT lacked. *However*: tree-level exchange with generic vertices yields rational (power-law-tailed) gates; the Gaussian requires the Gaussian fiber profile." (`notes/debt1a-ii-X-classification.md` §4)

EFT is effective field theory, here the lab notebook's v0.1 amplitude, in which μ was a free scale. The [momentum fiber](/wiki/phase-space/reciprocity/momentum-fibers#quanta-with-a-width-along-the-fiber) is the set of momentum directions of phase space attached to each point of spacetime.

## Background [T]

Three pieces of standard physics carry the argument.

### Integrating out a heavy carrier

A force carried by a field of mass M has a propagator proportional to 1/(q² + M²) in the momentum transfer q. When every transfer in a process is small compared with M, the propagator is nearly the constant 1/M², and the exchange acts as a contact interaction among the four external particles, with a strength proportional to the square of the coupling divided by M² [T]. The standard example is Fermi's four-fermion theory of beta decay, the low-energy form of the exchange of the heavy W boson [T]. In position the contact form means the force has a range of order 1/M, short compared with the distances of interest [T]. Replacing the heavy field by the contact term it produces is called integrating it out, and it is the basic step of effective field theory [T].

### Form factors

An object of finite size scatters as a point particle multiplied by a form factor F(q), the [Fourier transform](/wiki/phase-space/reciprocity/fourier-transform) of its charge distribution [T]. For an object of radius R, F(q) is close to 1 when the transfer is small, qR ≪ 1, and falls off once q exceeds about 1/R, because the scattered waves from different parts of the object then interfere destructively [T]. The shape of the falloff follows the shape of the distribution: a Gaussian distribution has a Gaussian form factor, while a distribution with an exponential edge has a rational form factor that falls off as a power of q [T]. Electron scattering measures the sizes of nuclei and of the proton in this way [T]. Calc note #6 calls such objects "x-extended composites": extended in position, with form factors in the transfer q.

### Wavepacket overlap

A quantum state with a definite profile in momentum, of width μ, is a wavepacket in momentum space [T]. The overlap integral of two Gaussian profiles is itself a Gaussian in the separation of their centres [T]; its width depends on how the widths of the profiles are defined.

## The derivation as the sources give it

1. **The coupling.** Conjugate matter couples universally to the [generalized metric](/wiki/phase-space/born-geometry/born-structures) H (postulate [P4](/wiki/program/postulates/p4-polarized-matter)), and to the part of H that X carries through the [dual stress T̃](/wiki/dark-matter/conjugate-matter/dual-stress), "moments involving momentum-derivatives of the χ bilinear" (#5 §E).
2. **The exchange.** "Exchange of X between two such bilinears yields a four-point amplitude that depends on the **incoming relative momenta** of the pair — the variable no x-local mediator can produce, and exactly the variable the gate was postulated in" (#5 §E). Here "x-local" means local in position.
3. **X is massive.** Calc note #6 shows that X cannot be massless ([why X must be massive](/wiki/gravity/momentum-graviton/forcing-chain)) and acquires its mass when the vacuum selects a polarization, "mass M_X = the polarization-breaking scale" (§2–§3; [the gravitational Higgs mechanism](/wiki/gravity/momentum-graviton/gravitational-higgs)).
4. **Integrating it out.** Because X is massive, "Integrating out massive X between χ bilinears gives the contact four-χ operator" (#6 §4): a contact interaction among four χ fields, as in the background above.
5. **Where the momentum dependence enters.** A contact interaction alone carries no dependence on k. #6 locates it in the χ quanta themselves: "p-polarized quanta are extended objects on the momentum fiber with width μ, and they exchange X only over their fiber overlap". The coupling acts only where the two quanta's momentum profiles overlap, so it falls off when their momenta differ by much more than μ.
6. **The Gaussian case.** If the profiles are Gaussian, the overlap "gives exactly e^{−(p₁−p₂)²/2μ²} — the postulated gate", which identifies μ with "the χ quantum's own p-width" (#6 §4). The note states this result without showing the overlap integral.
7. **The downgrade.** "*However*: tree-level exchange with generic vertices yields rational (power-law-tailed) gates; the Gaussian requires the Gaussian fiber profile" (#6 §4). Tree-level amplitudes are built from propagators and polynomial vertices, which are rational functions of the momenta [T]; a Gaussian can enter only through the external profiles. Which case holds is [Open: the gate shape (OP4)](/wiki/dark-matter/conjugate-matter/gate-shape).

#6 tags the section [D — structural] and records one downgrade, step 7. The steps are stated, not computed: no source writes the χ–X vertex, the X propagator on the momentum fibers, the χ quantum's profile or the overlap integral. Step 3 rests on a chain that calc note #6 calls "the Euclidean-rigorous skeleton" (§3), derived for a positive-definite metric; its extension to the Lorentzian signature of spacetime is open, item 3 of #11 §14 ([Open: Lorentzian dressing](/wiki/phase-space/born-geometry/lorentzian-dressing)).

## Exchanging X cannot produce the gate

The gate-mechanism note, `notes/gate-mechanism.md` (2026-10-28), asks whether the derivation above holds. The question arose while answering Paul's question about momentum gravity (`notes/velocity-gated-gravity.md`; [X between ordinary bodies](/wiki/gravity/momentum-graviton/ordinary-bodies)), where the gate's origin decides whether a long-range version could exist (§1). Two independent derivations agree on the central result: the first by a theory verifier in run 3 of the momentum-gravity investigation, the second blind, with an expected outcome sealed beforehand outside its reach, in run 4 ([pre-registration](/wiki/method/review/pre-registration)). Results that only one of them computed are marked "one derivation" below, as the note marks them. The note has not been through a blind review round, and no further agent checked either derivation's own results; `verify/gate_mechanism.py` "reruns their arithmetic and algebra; it does not test their physics" (§6).

The note's conventions (§1): the amplitude gate is e^{−k²/μ²} = e^{−v²/v_a²}, with v the relative speed and v_a = √2 v\*; the cross-section gate is e^{−v²/v\*²}. The record's μ ≈ 20 keV and v\* ≈ 120 km/s are not exactly consistent. The second derivation takes μc = 20 keV at m = 70 MeV, so v\* = 121.1 km/s and ħ/μ = 9.87 pm; the first takes v\* = 120 km/s, so μc = 19.81 keV and ħ/μ = 9.96 pm. They differ by 0.95%, and "about 10 pm" covers both. Flag 17's √2 question is untouched (§1; [two conventions, not reconciled](/wiki/dark-matter/conjugate-matter/velocity-gate#two-conventions-not-reconciled)).

The amplitudes below are written with the Mandelstam variables of two-body scattering [T]: s is the square of the total energy in the centre-of-mass frame, and t and u are the squares of the two possible momentum transfers, t = −q² for the transfer q. In the centre-of-mass frame with equal masses, s − u = 4m² + 8k² − q² (§2).

### Each vertex depends only on the transfer [D][V]

For χ on its mass shell, any χ(p_in)–χ(p_out)–X vertex depends, in a Lorentz-invariant way, only on t = (p_in − p_out)², since p_in·p_out = m² − t/2. This holds for local, derivative and form-factor vertices alike, and both derivations reach it (§2). A nonlocal "dual stress" weighted along the fiber adds nothing: the fiber coordinate of a χ\*χ bilinear is the average momentum (p_in + p_out)/2, so a fiber weight w becomes w(m² − t/4) (one derivation). In signal terms, each end of the exchange depends on how much momentum passed through it, not on how fast the other particle was moving.

### A polynomial whose velocity scale is c [D][V]

- **Degree two.** t-channel exchange of a massive spin-2 field with the most general scalar vertex, V = F₁PP + F₂(Pℓ + ℓP) + F₃ℓℓ + F₄m²η, gives the numerator N_t = A(t) + B(t)(s − u) + C(t)(s − u)², with C = F₁². At fixed transfer q the amplitude therefore depends on k only as a polynomial of degree at most two in k²; no denominator in k appears (§2).
- **The pole and the rest.** The residue at t = M_X² is (2/3)F₁²(4m² − M_X²)²P₂(z_t), with z_t = (s − u)/(4m² − M_X²) and P₂ the Legendre polynomial of degree 2, independent of F₂–F₄. The remainder is a polynomial contact term. A gate placed there would carry no X pole and no dependence on M_X, so it would not be X exchange [T: contact terms depend on field redefinitions] (§2).
- **Minimal coupling.** With the coupling X_μνT^μν the forward numerator is N(k,0)/N(0,0) = 1 + 6k²/m² + 6k⁴/m⁴. This is P₂(γ) with γ = 1 + 2k²/m², the factor (3γ² − 1)/2 that the first derivation finds for any massive spin-2 exchange ([X between ordinary bodies](/wiki/gravity/momentum-graviton/ordinary-bodies#its-velocity-dependence-is-relativistic)). A Dirac χ gives the same coefficient, 6.00, in the amplitudes that preserve spin, and 2.00 in the spin-flip amplitude, both of order one (one derivation) (§2).
- **The size.** At 120 km/s the k-dependence changes the amplitude by 2.4×10⁻⁷, and at 1500 km/s by 3.8×10⁻⁵; over the same range the gate e^{−k²/μ²} falls from 0.61 to 5×10⁻³⁴. The k-dependence reaches order one at a relative speed of 0.816c, 1429 times v_a = 171 km/s, reading k = mv/2 as at low speed; read relativistically, 6k²/m² = 1 at 0.661c. Either way the velocity scale is c (§2).
- **A polynomial cannot gate** (one derivation). For the general vertex at q = 0, N_t = n₀ + 64F₁²m²k² + 64F₁²k⁴. The k-dependent coefficients are non-negative, so the forward numerator never decreases with k² except towards a single zero. Moving its k-scale down to μ needs n₀ cancelled to about (μ/m)² ≈ 1/(1.2×10⁷), and the amplitude then grows with k. No polynomial of degree two in x = k²/μ² with P(0) = 1 stays below 0.903 in magnitude on x ∈ [1, 76.7], the range from v_a to 1500 km/s (§2).
- **Any finite spin.** The first derivation reaches the same result for spin J: the residue is a degree-J polynomial in γ = u₁·u₂, P_J(γ) for a massive carrier, and it increases with velocity ([what could carry a relative-velocity gate](/wiki/dark-matter/conjugate-matter/gate-carriers#finite-spin)).

### The other channels, the exact form and loops

- **The u channel** [D][V; one derivation]. For identical χ the forward term is −1/(4k² + M_X²), rational in k with scale M_X/2. Added to the t-channel term, the forward amplitude falls to half its k = 0 value, (M_X² + 2k²)/(M_X² + 4k²) → 1/2, not to zero, a halving computed for a spin-0 carrier: "the same Yukawa force seen at backward angles" (§2).
- **The s channel** [D][V; one derivation]. It needs a χ and an antiparticle, and a halo of asymmetric χ contains none. The asymmetric relic is stated only in #1 §5.3, which is superseded as reference but is the only document that states it ([the lab notebook](/wiki/history/documents/lab-notebook)). Its residue is d-wave, (32/3)G₁²k⁴P₂(cos θ), and vanishes at threshold: the opposite of a gate (§2).
- **#11 §8's form read as an exact amplitude** [D][V][T]. h(t)F(k²/μ²) with a t-channel pole in h has residue F(s), which is not a polynomial; the residue at a spin-J pole is proportional to P_J(z_t) [T]. The Gaussian and the rational F both have nonzero Legendre coefficients at every order computed (l = 0–6), so the form would need exchanged particles of every spin at one mass. The first derivation finds the same from the other side: a tower of spins reproduces the Gaussian gate only through terms about 10^5421169 times the net ([a tower of spins](/wiki/dark-matter/conjugate-matter/gate-carriers#a-tower-of-spins)) (§2).
- **Beyond tree level** [D; number V; one derivation]. Iterated exchange of a heavy X brings in momentum scales of order M_X and Bohr-type scales, not μ. A scale μ appears only by tuning a near-threshold state with inverse scattering length 1/a = μ. That gives σ = 4πa²/(1 + k²a²): rational, saturating the unitarity limit, and standard resonant [self-interacting dark matter](/wiki/dark-matter/halo-astrophysics/self-interacting-dark-matter) (prior art †; the note cites Chu, Garcia-Cely and Murayama 2019 †). At m = 70 MeV, σ/m = 9.8×10⁷ cm²/g, 3.3×10⁶ times [the benchmark](/wiki/dark-matter/conjugate-matter/benchmark)'s 30 cm²/g. It is not the record's gate (§2).

### The vacuum polarization supplies no velocity [D][V; one derivation]

One might expect the vacuum's choice of a split between position and momentum to give the vertex something to measure velocities against. The note finds that it does not (§4):

- With Lorentzian g, the blocks ω, η, K, J, H and the [Born rotation](/wiki/phase-space/reciprocity/born-reciprocity) ρ are all invariant under L = diag(Λ, Λ^{−T}), with residuals below 10⁻¹⁵. ρ flips K and J: the vacuum breaks ρ, not Lorentz symmetry. A Lorentz-invariant J cannot make a t-channel vertex depend on anything but t, and it supplies no momentum scale.
- With the positive-definite H that [the compatibility theorem](/wiki/phase-space/born-geometry/compatibility-theorem) assumes, J and H are not Lorentz-invariant: positivity needs a preferred frame ([Open: Lorentzian dressing (OP3)](/wiki/phase-space/born-geometry/lorentzian-dressing)).
- A preferred frame gates the wrong velocity (one derivation each). With a frame u, a per-leg profile gives e^{−k²/μ²}·e^{−m²V²/μ²}, the record's gate times a suppression in the pair's velocity V through the frame: 0.26, 4.7×10⁻⁶ and 4.9×10⁻²² at V = 100, 300 and 600 km/s. A medium, or a mediator whose own speed is of order v\*, gives the same kind of dependence ([a medium](/wiki/dark-matter/conjugate-matter/gate-carriers#a-medium)).

## The fiber overlap, read two ways

#6 §4 lets two quanta exchange X "only over their fiber overlap" but never writes the overlap down. The gate-mechanism note writes it down in the two natural ways: "These two readings are this note's reconstruction; the theorems about each are derived" (§3).

### Reading R1: the two quanta's phase-space densities overlap [D][V; one derivation]

- With momentum conservation, the fiber separation of the two bilinears equals a momentum transfer.
- As an operator, ∫dx dp dp′ W(x,p)S(p − p′)W(x,p′), with W the [Wigner function](/wiki/phase-space/reciprocity/wigner-function) and S a kernel of width μ, is an ordinary x-local two-body potential of range ħ/μ = 9.87 pm. It is a Gaussian potential.
- Its Born amplitude is S(q) + S(q_u), with q_u the transfer of the exchange term. At q → 0 it is 1 + e^{−2k²/μ²}: #6's e^{−(p₁−p₂)²/2μ²} is the forward value of the exchange term alone, and the amplitude tends to 1, not 0, at large k.
- Its cross-section tails are power laws even for Gaussian profiles: 2πμ⁴/k⁴ for identical χ and 2πμ²/k² for distinguishable species, where a Yukawa force gives π ln k/k⁴. "A Gaussian fiber profile therefore does not give a Gaussian tail, contrary to #6 §4" (§3).

Under R1, χ's self-interaction is ordinary short-range [self-interacting dark matter](/wiki/dark-matter/halo-astrophysics/self-interacting-dark-matter) with power-law tails (§5).

### Reading R2: the pair channel [D][V; one derivation]

- A vertex ∫dy g̃(y)χ(x + y/2)χ(x − y/2) depends on the pair's relative momentum. The separable amplitude g(k)g\*(k′) is |g(k)|² on shell: isotropic, and exactly #11 §8's gate when the transfer factor is flat. It falls faster than any power of k.
- It factorizes only in the s channel (pair → an object carrying χ-number 2 → pair), never in the t channel. It has no X pole, and a neutral spin-2 X cannot be its carrier.
- It is nonlocal in the pair's relative coordinate over ħ/μ ≈ 10 pm.

### What #6's rational gates are [D][V]

The rationality of tree amplitudes sits in the transfer: the propagator 1/(q² + M_X²) and form factors in t. Integrated over angle these give a light mediator's knee in [σ_T(v)](/wiki/dark-matter/halo-astrophysics/transfer-cross-section) with a power-law tail. That is [row 1](/wiki/predictions/self-interaction-knee)'s "standard expectation" column, not a gate in k. Both derivations reach this; the first adds that such a completion leaves the forward (q → 0) amplitude ungated, which is the quantity Debt 3a's collective model uses (§3).

### Neither reading is in the record [D, record audit]

- No χχX vertex, X propagator on the fibers, χ fiber profile, formula for the [dual stress T̃](/wiki/dark-matter/conjugate-matter/dual-stress), overlap integral or verify script exists; the note searched `papers/`, `notes/` and `HANDOFF.md` (§3).
- [The section condition](/wiki/symmetry-breaking/section-condition) (#1 §2; #5 §D) makes H_Z, and with it X, depend on x only. The fiber metric is constant along each fiber, so "X propagator on momentum fibers" has no meaning within #11 §7.
- #11 §8's "the variable no x-local mediator produces" holds only for the direct Born term. Exchange terms and near-threshold states of x-local forces do depend on k at fixed q. §8 also assigns the variable to X, which §7 builds as x-local.
- #13 §4 identifies μ with ħ/λ_χ, an extent in position ([the reading in conjugate special relativity](#the-reading-in-conjugate-special-relativity)). Standard form-factor physics turns that into a form factor in the transfer q at scale μ, not a gate in k [T].

### The range of a fiber gate [D][V; one derivation, the first]

The first derivation modelled the overlap as F^{1/2}(k)V(r)F^{1/2}(k): the gate inserted by hand around a separate potential V. In that model a fiber-overlap gate is not tied to contact range. With a long-range V, the exact quantum expectation for wavepackets equals the classical gated value to 3.4×10⁻³ at 3 ħ/μ, 5.1×10⁻⁵ at 100 ħ/μ, and better than 10⁻⁵ from 300 ħ/μ on. What makes the record's gate contact-range is X's mass: λ_X < 37.7 μm at u = 1, unscreened ([the laboratory bound on X's range](/wiki/gravity/momentum-graviton/range-bound)). The model says nothing about whether a carrier for a long-range gate exists. It does not contradict reading R1 or R2, and both derivations conclude that no local carrier of finite spin delivers the gate (§3). The long-range model is tested on its own in [Conjecture: a long-range velocity-gated attraction among χ](/wiki/dark-matter/momentum-clumping/long-range-gated-attraction).

## What flag 55 proposes

The note's plain-language summary of its consequence: "the gate itself is not refuted. What fails is the claim that it has been derived. It returns to what the lab notebook first called it, a postulate. The mechanism is open, and tree-level exchange of the program's own X is ruled out as that mechanism" (§5).

**The proposed tags** [D] (flag 55 in `review/wiki-build-flags.md`, rated high, for Paul's ruling; §5):

- the gate F(k²/μ²) and μ: [P], as #1 §3 (v0.1) tagged them ([superseded: earlier forms](#superseded-earlier-forms-of-the-mechanism));
- the mechanism: [O];
- tree-level t-channel exchange of §7's X as the mechanism: excluded [D][V];
- a conditional [D] is not available: the only condition that yields the gate, a pair-channel kernel g(k)g(k′), contains the gate and does not involve X.

#11 §14 item 4 ([Open: the gate shape (OP4)](/wiki/dark-matter/conjugate-matter/gate-shape)) does not cover the gap: it treats the mechanism as settled, presupposes an X propagator on the fibers that §7 does not have, and its Gaussian-against-rational split is not a dichotomy of gates in k (§5). The flag's audit reads: "confirmed by 2 independent derivations, the second blind and pre-registered."

**Text that depends on the tag** (§5): #11's technical abstract ("whose gate is X-exchange"), §8 (the plain-language passage, "now we know its mechanism", and the tag), §12's χ row ("sharp tail"), §13 rows 1–3 ([row 1](/wiki/predictions/self-interaction-knee), [row 2](/wiki/predictions/scattering-isotropy), [row 3](/wiki/predictions/island-discriminant)) and §15 ("gate tail not yet forced"); #6 §4, #5 §E, #8 §5 ("**Debt 2:** mechanism paid (X-exchange, μ = fiber width)"), `HANDOFF.md` §2 ("gate = X-exchange") and §3 (#5 "pays Debt 2's mechanism"); and this page, [the gate shape](/wiki/dark-matter/conjugate-matter/gate-shape) and [dual stress T̃](/wiki/dark-matter/conjugate-matter/dual-stress).

**What does not change** [V] (§5):

- The benchmark arithmetic is contact Born physics and needs no mechanism: σ₀ = 16πα̃²m²/m_φ⁴ with α̃ = 1 and m_φ = m_χ gives σ₀/m = 32.0 cm²/g at 70 MeV, or m = 71.5 MeV for 30 cm²/g; the conventions give μ/m = 2.857×10⁻⁴, v\* = 121.1 km/s and v_a = 171.3 km/s ([the scattering benchmark](/wiki/dark-matter/conjugate-matter/benchmark)).
- The velocity-clumping obituary is unaffected. "If anything it is strengthened: a completion whose only velocity dependence is a knee in σ_T(v) leaves the forward amplitude, which drives collective behaviour, ungated" ([Obituary: velocity clumping](/wiki/dark-matter/momentum-clumping/founding-image#what-the-obituary-covers)).

**What becomes open** [O] (§5):

- Row 3's [island discriminant](/wiki/predictions/island-discriminant) reads a sharp tail as particle χ and a (v\*/σ)⁴ tail as wave χ. Under reading R1 the particle tail is a power law, the same functional class as the wave island's. Whether the discriminant survives is open.
- Whether the program keeps the gate as a postulate, or rewrites χ's self-interaction as reading R1's x-local potential of range ~10 pm, which is ordinary short-range self-interacting dark matter with power-law tails and would remove the program-specific content of rows 1–3.
- Whether any construction tied to the program's geometry yields a pair-channel form factor for χχ, for example a composite carrying χ-number 2. Nothing in the record points to one.
- If a Gaussian form factor in s is kept, whether microcausality and unitarity are acceptable at the nonlocality scale ħ/μ ≈ 10 pm.
- Whether a doubled, phase-space field theory for χ that drops the section condition could define a relative momentum consistent with momentum conservation.
- The coupling's strength ([Open: the dual-stress enhancement (OP5)](/wiki/dark-matter/conjugate-matter/dual-stress-enhancement)) stays open whatever the mechanism.

These are listed on [open problems and the queue](/wiki/status/open-problems).

**Caveats from the second derivation** (§6). The main theorem is tree level on a flat background with the [Fierz–Pauli](/wiki/gravity/spin-2-fields/fierz-pauli) numerator. [Hassan–Rosen](/wiki/gravity/spin-2-fields/hassan-rosen-bimetric) nonlinearities and the van Dam–Veltman–Zakharov subtleties change the t-dependence and normalization, not the degree in s. The Lorentzian check transplants the program's block structures to Lorentzian g; the record's theorems assume positive H (OP3). Cross-section normalizations use unit couplings; only shapes and tail laws are compared.

**The pre-registration, scored** (§6; `review/momentum-gravity/preregistration-run4.md`). Right: the polynomial of degree two in s with velocity scale c; the record builds no fiber structure; #6 §4's "rational gates" are not a gate in k. Partly right: the verdict matched the hedged alternative ("unsupported" for the tag as written), not the first choice ("conditional"), which the derivation rules out, since no conditional [D] is available; the tag matched only in its [P] branch, and not on the stated condition, since the derivation gives [P] to the gate itself, not to a fiber-resolving X, and finds that §14 item 4 does not cover the gap. The weakest link named, the polarization, held up: it is Lorentz-invariant. "The scenario it guarded against, a ruling of [P] rather than [O], partly happened, for a different reason." Missed: reading R1, in which the fiber overlap is an ordinary potential of range ~10 pm.

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

The lab notebook converts μ into the gate velocity, v\* ≡ √2μ/m_χ (#1 §5.1), the location of the knee in [the gated scattering law](/wiki/dark-matter/conjugate-matter/scattering-law). #11 does not restate this definition. At [the scattering benchmark](/wiki/dark-matter/conjugate-matter/benchmark) the notebook gives "μ = m_χv\*/√2 ≈ 20 keV (α̃ ≈ 1)" (#1 §5.1), a number found only in the lab notebook and not machine-checked. The definition of v\* was written for v0.1's e^{−k²/μ²}; a suspected factor of √2 in μ between that form and #6's overlap form, which matters once μ is read as the fiber width, is recorded for a ruling in `review/wiki-build-flags.md` item 17. The flag notes that no stated number changes; this page quotes the sources as written.

## What it closed and what it gave up

The mechanism answers the question Debt 2 posed, where the gate comes from ([the three debts](/wiki/history/debts)). Calc note #8's close-out: "**Debt 2:** mechanism paid (X-exchange, μ = fiber width); shape completion open (Gaussian vs rational tail — now also an observable discriminant)" (`notes/debt1a-iv-beta-coefficients.md` §5). [The handoff](/wiki/history/documents/handoff) lists "gate = X-exchange; gate variable = incoming relative momentum; μ = χ's momentum-fiber width" among the live results (`HANDOFF.md` §2). Flag 55 proposes that the payment does not stand: the gate-mechanism note finds that exchanging X cannot produce the gate, and #8 §5's close-out and the handoff's §2 and §3 are among the text that depends on the tag ([what flag 55 proposes](#what-flag-55-proposes)).

It also gave up the lab notebook's sharpest prediction. #6 §4 records it as a downgrade of the flagship row:

> "**row 1's 'exponential cliff' weakens to 'sharp knee at v\*, with the tail shape (Gaussian vs rational) a diagnostic of the vertex completion.'** The knee's existence and location are robust; its steepness is model-internal information, not a guaranteed exponential."

(The note writes v_\* for v\*.) The knee is tested in [row 1](/wiki/predictions/self-interaction-knee) of [the predictions table](/wiki/predictions).

## Scope and caveats

- **Structural only.** The mechanism fixes the variable of the gate and identifies μ; it does not compute F. #11 §8 tags the mechanism [D] and the shape [O].
- **Not derived, according to flag 55.** The gate-mechanism note finds that exchanging #11 §7's X gives a dependence on k with velocity scale c, not the gate, and that #6's fiber overlap, written out, is either an ordinary x-local potential or a pair-channel interaction that contains no X ([exchanging X cannot produce the gate](#exchanging-x-cannot-produce-the-gate); [the fiber overlap, read two ways](#the-fiber-overlap-read-two-ways)). Paul has not ruled.
- **Two exponents.** The overlap form e^{−(p₁−p₂)²/2μ²} and the lab notebook's postulated e^{−k²/μ²}, with k = m_χv_rel/2 (#1 §3), are not reconciled in any source ([the velocity gate](/wiki/dark-matter/conjugate-matter/velocity-gate#two-conventions-not-reconciled)).
- **The transfer mediator.** The amplitude of #11 §8 keeps the factor 4πα̃m_χ/(q² + m_φ²), with m_φ the mass of the carrier of the momentum transfer. No source relates m_φ to M_X, and the benchmark's choice m_φ ~ m_χ was made in v0.1, before the mechanism was found (#1 §5.1).
- **The strength.** The mechanism explains why the interaction depends on relative momentum, not why it is as strong as dwarf-galaxy cores require; that is [Open: the dual-stress enhancement (OP5)](/wiki/dark-matter/conjugate-matter/dual-stress-enhancement).

## The reading in conjugate special relativity

The paper on [conjugate special relativity](/wiki/conjugate-relativity), #13, gives μ a kinematic origin. Its Born image of the mass shell is an "invariant-length shell": "conjugate quanta are characterized by an irreducible extent λ_χ as ours are by mass" [D — structural] (§4). It then reads the gate scale from that extent:

> "The conjugate quantum's invariant extent fixes its intrinsic momentum-space width μ ~ ℏ/λ_χ — which is precisely the gate scale of the dark-matter sector, v\* = √2 μ/m_χ. The knee in the dark-matter self-interaction curve is, in this reading, a *dual-relativistic invariant of the dark sector* made visible in galactic dynamics [D — structural]." (#13 §4)

The relation μ ~ ℏ/λ_χ is a reciprocal relation between a width in momentum and an extent in position, the relation between the widths of a waveform and its spectrum. #13 combines #6's fiber width with the lab notebook's v\*, the mix that `review/wiki-build-flags.md` item 17 records. #13 has not been through review, and it uses both λ_χ and m_χ for the conjugate quantum, while the checkpoint gives χ ordinary kinematics with mass m_χ; the two are not reconciled ([the invariant-length shell](/wiki/conjugate-relativity/invariant-length-shell)).

## Superseded: earlier forms of the mechanism

The mechanism reached its present form in three steps.

- **v0.1: a scale of the momentum-space metric.** The lab notebook routed χ's self-interaction "through the g̃ block" and took μ as "a scale μ of the g̃ sector", with the gate's existence a postulate [P] (#1 §3); see [the velocity gate](/wiki/dark-matter/conjugate-matter/velocity-gate#superseded-the-gaussian-gate-of-v01). Flag 55 proposes returning the gate and μ to this tag, [P], with the mechanism [O] ([what flag 55 proposes](#what-flag-55-proposes)).
- **Calc note #5: μ from the masses.** The first identification of the carrier wrote the scale in terms of two masses:

  ```text
  gate = momentum-graviton exchange,    μ ↔ (M_X, M_B) parametrically
  ```

  (`notes/debt1a-geometric-core.md` §E). M_B is the mass scale of the lab notebook's geometric action, S_H = ½M_B²∫_Σ √|H| R_B[H], an integral over the section Σ, from which the [Planck mass](/wiki/gravity/spin-2-fields/planck-units#where-a-document-states-no-convention) follows (#1 §3). Calc note #6 replaced the relation with μ = the χ quantum's own width, a property of the matter field rather than of the geometry, and no later document returns to M_X and M_B as the source of μ.
- **Calc note #5: an auxiliary X.** #5 §D listed three possible outcomes for X at quadratic order. The second, an auxiliary X with no derivatives, would have been integrated out to "a *contact, momentum-structured* four-χ operator, i.e. the gate delivered directly", and #5 §E places the gate shape "downstream of the §D classification (outcome 2 gives it most cheaply)". Calc note #6 §1 closed that route: constant shifts of X are exact symmetries, so "'auxiliary X' (the soft outcome 2) is off the table at the fundamental level: X appears only through derivatives, so it propagates or it doesn't exist" ([shift symmetry](/wiki/gravity/momentum-graviton/shift-symmetry)). The contact operator of the current mechanism comes from integrating out a massive, propagating X instead.

## Chat-only: the gate as a dual Newtonian limit

[The handoff](/wiki/history/documents/handoff) records, among results that exist only in the original conversation, a comparison of the program's field equations with [general relativity](/wiki/gravity/spin-2-fields/general-relativity) that ends in the gate: "dual Newtonian limit = Yukawa in momentum = the gate" (`HANDOFF.md` §4). No document derives a [Yukawa form in momentum](/wiki/gravity/spin-2-fields/yukawa-forces#conjugate-special-relativity-a-range-in-momentum) or describes the gate as a Newtonian limit; the documented counterpart is the mechanism on this page. Its status is conjecture; see [Two gravitational charges and the conjugate field equations (chat-only)](/wiki/gravity/momentum-graviton/chat-only-results).

## Sources

- `papers/broken-born-checkpoint-v2.md` §8 — the checkpoint's statement and tags; §14 item 3 — Lorentzian dressing open
- `notes/broken-born-program-v1.md` §6 — v1's statement, the same as #11's
- `notes/debt1a-ii-X-classification.md` §4 — integrating out X, fiber overlap, the Gaussian case, the rational-tail downgrade, the cliff weakened to a knee; §2 — the massless option excluded; §3 — M_X the polarization-breaking scale, the Euclidean-rigorous skeleton; §1 — auxiliary X excluded by the shift symmetry
- `notes/debt1a-geometric-core.md` §E — the four-point amplitude; the superseded μ ↔ (M_X, M_B) identification; §D — the auxiliary outcome
- `notes/debt1a-iv-beta-coefficients.md` §5 — Debt 2's close-out: mechanism "paid", shape open
- `HANDOFF.md` §2 — the mechanism among the live results; §4 — the chat-only dual Newtonian limit
- `papers/conjugate-special-relativity.md` §4 — μ ~ ℏ/λ_χ as the gate scale
- `notes/broken-born-theory.md` 'Addendum (v0.3, overnight)', 'Addendum (v0.4)' — the mechanism and the fiber width in the lab notebook; §3 — the v0.1 carrier and M_B in S_H; §5.1 — v\* ≡ √2μ/m_χ, μ ≈ 20 keV, m_φ ~ m_χ
- `review/wiki-build-flags.md` item 17 — the suspected √2 in μ between the two gate conventions, awaiting a ruling; item 55 — the mechanism not derived, with the proposed tags, the text that depends on them and the audit, awaiting Paul's ruling
- `notes/gate-mechanism.md` (2026-10-28, not reviewed) §1 — the question, the record's statements, the two derivations and the conventions; §2 — the vertex, the degree-two polynomial, its velocity scale, the other channels, the exact form, loops and the resonance; §3 — readings R1 and R2, the rational gates, the record audit and the range of a fiber gate; §4 — the polarization and a preferred frame; §5 — the proposed tags, the dependent text, what does not change and what becomes open; §6 — what each derivation gave, the caveats and the pre-registration scored
- `verify/gate_mechanism.py` — reruns the note's arithmetic and algebra ([the gate-mechanism script](/wiki/method/verification/gate-mechanism-script))
- `review/momentum-gravity/README.md` — the investigation's runs; `review/momentum-gravity/preregistration-run4.md` — the second derivation's sealed expectation
