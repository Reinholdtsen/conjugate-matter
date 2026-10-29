# Does exchanging X produce the dark-matter gate?

*Working note, 2026-10-28. Status: computed. Two independent derivations agree on the central result (§2): the
first by a theory verifier in run 3 of the momentum-gravity investigation, the second blind and pre-registered in
run 4. Results that only one of them computed are marked "one derivation" where they appear. The note has not been
through a blind review round. Every number and algebraic result is recomputed in `verify/gate_mechanism.py`. The
derivations, their scripts and the pre-registration are in `review/momentum-gravity/`. The result is proposed to
Paul as flag 55 in `review/wiki-build-flags.md`; #11 is unchanged until he rules.
Conjecture and direction, P.R.; derivations, counterexamples, verification, drafting, Claude (Anthropic).*

## 1. The question and what the record says

*In plain terms: the program's dark matter scatters off itself only when two particles move at nearly the same
velocity. The record says this gate follows from the two particles exchanging the momentum graviton X. This note
asks whether it does. The question came up while answering Paul's question about momentum gravity
(`notes/velocity-gated-gravity.md`), where the gate's origin decides whether a long-range version could exist.*

**What the record says.**
- #11 §8: the χ–χ amplitude is M(k,q) = 4πα̃m_χ/(q² + m_φ²)·F(k²/μ²), with k the incoming relative momentum, "the
  variable no x-local mediator produces, delivered by X-exchange between dual-stress bilinears, with μ the χ
  quantum's intrinsic momentum-fiber width [D — mechanism; shape [O]]".
- #6 §4: integrating out the massive X gives a contact four-χ operator. "p-polarized quanta are extended objects on
  the momentum fiber with width μ, and they exchange X only over their fiber overlap". "Wavepacket overlap of
  Gaussian profiles gives exactly e^{−(p₁−p₂)²/2μ²}". It adds: "tree-level exchange with generic vertices yields
  rational (power-law-tailed) gates; the Gaussian requires the Gaussian fiber profile."
- #5 §E: "gate = momentum-graviton exchange", with "the gate *shape* … the X propagator's structure on the momentum
  fibers — open [O]". HANDOFF §3 credits #5 with finding "the gate's mechanism".
- #11 §14 item 4 lists as open only the "Gate shape (X propagator on momentum fibers; Gaussian vs rational — now
  observable) [O]".
- #11 §7 builds X as one massive spin-2 field on spacetime: δX_μν = ∂_(μλ_ν), with Standard-Model couplings
  "Yukawa-cut at 1/M_X" (§7.5).

**Method.**
- First derivation: the run-3 theory verifier, checking the run-2 critic's claim that no local carrier gives a
  gate (`review/momentum-gravity/run3/verify-critic-theory.json`, scripts in `scripts/verify-critic-theory/`).
- Second derivation: a blind agent given the neutral question "does the record derive its velocity gate from
  X-exchange, and is #11 §8's tag supported?", with an expected outcome sealed beforehand outside its reach
  (`run4/gate-derivation.json`, scripts in `scripts/derivation-gate-mechanism/`; scored in §6).
- Conventions: the amplitude gate is e^{−k²/μ²} = e^{−v²/v_a²}, with v the relative speed and v_a = √2 v*; the
  cross-section gate is e^{−v²/v*²}. Flag 17's √2 question is untouched by anything here.
- The record's μ ≈ 20 keV and v* ≈ 120 km/s are not exactly consistent, and the two derivations read them
  differently. The second takes μc = 20 keV at m = 70 MeV, so v* = 121.1 km/s and ħ/μ = 9.87 pm; every
  μ-dependent number of §§2–5 uses this. The first takes v* = 120 km/s, so μc = 19.81 keV and ħ/μ = 9.96 pm. They
  differ by 0.95%; "about 10 pm" below covers both.

## 2. Exchanging the X of §7 cannot produce the gate

*In plain terms: when two particles exchange a field quantum, each end of the exchange depends only on how much momentum
passed through it, not how fast the other particle was moving. The dependence on the pair's relative velocity
that remains is a short polynomial whose natural velocity scale is the speed of light. At galactic speeds it
changes the amplitude by parts in ten million, where the gate would switch the interaction off.*

**Each vertex depends only on the transfer** [D][V; both derivations].
- For on-shell χ, any χ(p_in)–χ(p_out)–X vertex depends Lorentz-invariantly only on t = (p_in − p_out)², since
  p_in·p_out = m² − t/2. This holds for local, derivative and form-factor vertices alike.
- It holds also for a nonlocal "dual stress" weighted along the fiber: the fiber coordinate of a χ*χ bilinear is
  the average momentum (p_in + p_out)/2, so a fiber weight w becomes w(m² − t/4) (one derivation).

**The exchange amplitude is a polynomial of degree two** [D][V].
- t-channel exchange of a massive spin-2 field with the most general scalar vertex
  V = F₁PP + F₂(Pℓ + ℓP) + F₃ℓℓ + F₄m²η gives the numerator N_t = A(t) + B(t)(s − u) + C(t)(s − u)², with
  C = F₁².
- Since s − u = 4m² + 8k² − q², at fixed transfer q the amplitude depends on k only as a polynomial of degree at
  most two in k². No denominator in k appears.
- The pole part is fixed: the residue at t = M_X² is (2/3)F₁²(4m² − M_X²)²P₂(z_t), with z_t = (s − u)/(4m² − M_X²),
  independent of F₂–F₄. The remainder is a polynomial contact term. A gate placed there would carry no X pole
  and no dependence on M_X, so it would not be X exchange [T: contact terms depend on field redefinitions].
- The first derivation reaches the same result for any spin J: the residue is a degree-J polynomial in γ = u₁·u₂,
  P_J(γ) for a massive carrier, and it increases with velocity (`notes/velocity-gated-gravity.md` §9).

**Its velocity scale is c** [D][V].
- With the minimal coupling X_μνT^μν, the forward numerator is N(k,0)/N(0,0) = 1 + 6k²/m² + 6k⁴/m⁴. This is
  P₂(γ) with γ = 1 + 2k²/m², the first derivation's spin-2 factor (3γ² − 1)/2.
- A Dirac χ gives the same coefficient, 6.00, in the amplitudes that preserve spin; the spin-flip amplitude has
  coefficient 2.00. Both are of order one (one derivation).
- At 120 km/s this changes the amplitude by 2.4×10⁻⁷, and at 1500 km/s by 3.8×10⁻⁵. Over the same range the
  gate e^{−k²/μ²} falls from 0.61 to 5×10⁻³⁴.
- The k-dependence reaches order one at a relative speed of 0.816c, 1429 times v_a = 171 km/s, reading k = mv/2 as
  at low speed. Read relativistically, 6k²/m² = 1 at 0.661c. Either way the velocity scale is c.

**A polynomial cannot gate** [D][V; one derivation].
- For the general vertex at q = 0, N_t = n₀ + 64F₁²m²k² + 64F₁²k⁴. The k-dependent coefficients are non-negative,
  so the forward numerator never decreases with k² except towards a single zero.
- Moving its k-scale down to μ needs n₀ cancelled to about (μ/m)² ≈ 1/(1.2×10⁷), and the amplitude then grows
  with k.
- No polynomial of degree two in x = k²/μ² with P(0) = 1 stays below 0.903 in magnitude on x ∈ [1, 76.7], the
  range from v_a to 1500 km/s.

**The other channels do not gate either** [D][V; one derivation].
- u channel, for identical χ: a forward term −1/(4k² + M_X²), rational in k with scale M_X/2. Added to the
  t-channel term, the forward amplitude falls to half its k = 0 value, (M_X² + 2k²)/(M_X² + 4k²) → 1/2, not to
  zero (computed for a spin-0 carrier). This is the same Yukawa force seen at backward angles.
- s channel: it needs χχ̄. A halo of asymmetric χ contains none; the asymmetric relic is stated only in #1 §5.3,
  which is superseded as reference but is the only document that states it. Its residue is d-wave,
  (32/3)G₁²k⁴P₂(cos θ), and vanishes at threshold: the opposite of a gate.

**Read as an exact amplitude, §8's form needs every spin** [D][V][T].
- h(t)F(k²/μ²) with a t-channel pole in h has residue F(s), which is not a polynomial. The residue at a spin-J pole
  is proportional to P_J(z_t) [T].
- The Gaussian and the rational F both have nonzero Legendre coefficients at every order computed (l = 0–6). The
  form would need exchanged particles of every spin at one mass.
- The first derivation finds the same from the other side: a tower of spins reproduces the Gaussian gate only
  through terms about 10^5421169 times the net (`notes/velocity-gated-gravity.md` §9).

**Beyond tree level** [D; number V; one derivation].
- Iterated exchange of a heavy X brings in momentum scales of order M_X and Bohr-type scales, not μ.
- A scale μ appears only by tuning a near-threshold state with inverse scattering length 1/a = μ. That gives
  σ = 4πa²/(1 + k²a²): rational, unitarity-saturating, and standard resonant self-interacting dark matter (prior
  art †). At m = 70 MeV, σ/m = 9.8×10⁷ cm²/g, 3.3×10⁶ times the benchmark's 30 cm²/g. It is not the record's gate.

## 3. The fiber overlap, read two ways

*In plain terms: #6 pictures each dark-matter quantum as a small blob along the momentum directions and lets two
quanta interact only where their blobs overlap. The record never writes the overlap down. Written down in the two
natural ways, it gives either an ordinary short-range force, about ten picometres in range, or a gate that has
nothing to do with X. These two readings are this note's reconstruction; the theorems about each are derived.*

**Reading R1: the two quanta's phase-space densities overlap** [D][V; one derivation].
- With momentum conservation, the fiber separation of the two bilinears equals a momentum transfer.
- As an operator, ∫dx dp dp′ W(x,p)S(p − p′)W(x,p′), with S a kernel of width μ, is an ordinary x-local two-body
  potential of range ħ/μ = 9.87 pm. It is a Gaussian potential.
- Its Born amplitude is S(q) + S(q_u). At q → 0 it is 1 + e^{−2k²/μ²}: #6's e^{−(p₁−p₂)²/2μ²} is the forward value
  of the exchange term alone, and the amplitude tends to 1, not 0, at large k.
- Its cross-section tails are power laws even for Gaussian profiles: 2πμ⁴/k⁴ for identical χ and 2πμ²/k² for
  distinguishable species. A Yukawa force gives π ln k/k⁴. A Gaussian fiber profile therefore does not give a
  Gaussian tail, contrary to #6 §4.

**Reading R2: the pair channel** [D][V; one derivation].
- A vertex ∫dy g̃(y)χ(x + y/2)χ(x − y/2) depends on the pair's relative momentum. The separable amplitude g(k)g*(k′) is
  |g(k)|² on shell: isotropic, and exactly §8's gate when the transfer factor is flat. It falls faster than any
  power of k.
- It factorizes only in the s channel (pair → an object carrying χ-number 2 → pair), never in the t channel. It has
  no X pole, and a neutral spin-2 X cannot be its carrier.
- It is nonlocal in the pair's relative coordinate over ħ/μ ≈ 10 pm.

**What #6 §4's "rational gates" are** [D][V].
- The rationality of tree amplitudes sits in the transfer: the propagator 1/(q² + M_X²) and form factors in t.
  Integrated over angle these give a light mediator's knee in σ_T(v) with a power-law tail. That is #11 §13 row 1's
  "standard expectation" column, not a gate in k.
- Both derivations reach this; the first adds that such a completion leaves the forward (q → 0) amplitude ungated,
  which is the quantity calc note #2's collective model uses.

**Neither reading is in the record** [D, record audit].
- No χχX vertex, X propagator on the fibers, χ fiber profile, formula for the dual stress T̃, overlap integral or
  verify script exists (`/usr/bin/grep` over `papers/`, `notes/`, `HANDOFF.md`).
- The section condition (#1 §2; #5 §D) makes H_Z, and with it X, depend on x only. The fiber metric is constant
  along each fiber, so "X propagator on momentum fibers" has no meaning within §7.
- §8's "the variable no x-local mediator produces" holds only for the direct Born term. Exchange terms and
  near-threshold states of x-local forces do depend on k at fixed q. §8 also assigns the variable to X, which §7
  builds as x-local.
- #13 §4 identifies μ with ħ/λ_χ, an extent in position. Standard form-factor physics turns that into a form
  factor in the transfer q at scale μ, not a gate in k [T].

**The range of a fiber gate** [D][V; one derivation, the first].
- The first derivation modelled the overlap as F^{1/2}(k)V(r)F^{1/2}(k): the gate inserted by hand around a
  separate potential V. In that model a fiber-overlap gate is not tied to contact range. With a long-range V, the
  exact quantum expectation for wavepackets equals the classical gated value to 3.4×10⁻³ at 3 ħ/μ, 5.1×10⁻⁵ at
  100 ħ/μ, and better than 10⁻⁵ from 300 ħ/μ on.
- What makes the record's gate contact-range is X's mass: λ_X < 37.7 μm at u = 1, unscreened
  (`papers/phase-space-diameter.md` §8.2).
- The model says nothing about whether a carrier for a long-range gate exists. It does not contradict reading R1
  or R2, and both derivations conclude that no local carrier of finite spin delivers the gate.

## 4. The vacuum polarization does not supply the missing structure

*In plain terms: the program's vacuum picks a split between position and momentum. One might hope that choice
gives the vertex something to measure velocities against. It does not: in spacetime of the usual signature the
choice looks the same to every inertial observer. A preferred rest frame would supply a velocity, but the
resulting effect would depend on each pair's motion through that frame, not on the two particles' relative
velocity.*

**The polarization is Lorentz-invariant** [D][V; one derivation].
- With Lorentzian g, the blocks ω, η, K, J, H and the Born rotation ρ are all invariant under
  L = diag(Λ, Λ^{−T}) (residuals below 10⁻¹⁵). ρ flips K and J: the vacuum breaks ρ, not Lorentz symmetry.
- A Lorentz-invariant J cannot make a t-channel vertex depend on anything but t, and it supplies no momentum
  scale.
- With the positive-definite H that the compatibility theorem assumes, J and H are not Lorentz-invariant:
  positivity needs a preferred frame (OP3).

**A preferred frame gates the wrong velocity** [D][V; one derivation each].
- With a frame u, a per-leg profile gives e^{−k²/μ²}·e^{−m²V²/μ²}, using Σ|mV + k_i|² = 4m²V² + 4k². This is the
  record's gate times a suppression in the pair's velocity V through the frame: 0.26, 4.7×10⁻⁶ and 4.9×10⁻²² at
  V = 100, 300 and 600 km/s.
- A medium, or a mediator whose own speed is of order v*, gives the same kind of dependence. Side by side, two
  co-moving bodies feel 1/√(1 − V²/c_s²) times the static force (the first derivation;
  `notes/velocity-gated-gravity.md` §9).

## 5. What follows for the record

*In plain terms: the gate itself is not refuted. What fails is the claim that it has been derived. It returns to
what the lab notebook first called it, a postulate. The mechanism is open, and tree-level exchange of the
program's own X is ruled out as that mechanism.*

**Proposed tags** [D] (flag 55, for Paul's ruling).
- The gate F(k²/μ²) and μ: [P], as #1 §3 (v0.1) tagged them.
- The mechanism: [O].
- Tree-level t-channel exchange of §7's X as the mechanism: excluded [D][V].
- A conditional [D] is not available: the only condition that yields the gate, a pair-channel kernel g(k)g(k′),
  contains the gate and does not involve X.
- §14 item 4 does not cover the gap. It treats the mechanism as settled, presupposes an X propagator on the fibers
  that §7 does not have, and its Gaussian-against-rational split is not a dichotomy of gates in k (§3).

**Text that depends on the tag.**
- #11: the technical abstract ("whose gate is X-exchange"); §8, the plain-language passage ("now we know its
  mechanism") and the tag; §12's χ row ("sharp tail"); §13 rows 1–3; §15 ("gate tail not yet forced").
- #6 §4, #5 §E, #8 §5 ("**The gate problem:** mechanism found (X-exchange, μ = fiber width)"), HANDOFF §2
  ("gate = X-exchange") and §3 (#5 "finds the gate's mechanism").
- The wiki's gate-mechanism, gate-shape and dual-stress pages.

**What does not change** [V].
- The benchmark arithmetic is contact Born physics and needs no mechanism: σ₀ = 16πα̃²m²/m_φ⁴ with α̃ = 1 and
  m_φ = m_χ gives σ₀/m = 32.0 cm²/g at 70 MeV, or m = 71.5 MeV for 30 cm²/g. The conventions give μ/m = 2.857×10⁻⁴,
  v* = 121.1 km/s and v_a = 171.3 km/s.
- The velocity-clumping obituary is unaffected. If anything it is strengthened: a completion whose only velocity
  dependence is a knee in σ_T(v) leaves the forward amplitude, which drives collective behaviour, ungated (§3).

**What becomes open** [O].
- Row 3's island discriminant reads a sharp tail as particle χ and a (v*/σ)⁴ tail as wave χ. Under reading R1 the
  particle tail is a power law, the same functional class as the wave island's. Whether the discriminant survives
  is open.
- Whether the program keeps the gate as a postulate, or rewrites χ's self-interaction as reading R1's x-local
  potential of range ~10 pm, which is ordinary short-range self-interacting dark matter with power-law tails and
  would remove the program-specific content of rows 1–3.
- Whether any construction tied to the program's geometry yields a pair-channel form factor for χχ, for example a
  composite carrying χ-number 2. Nothing in the record points to one.
- If a Gaussian form factor in s is kept, whether microcausality and unitarity are acceptable at the nonlocality
  scale ħ/μ ≈ 10 pm.
- Whether a doubled, phase-space field theory for χ that drops the section condition could define a relative
  momentum consistent with momentum conservation.
- The coupling's strength (OP5, the dual-stress enhancement) stays open whatever the mechanism.

## 6. Record

*In plain terms: how the two derivations were made, what each checked, and how the sealed expectation scored.*

**The two derivations.**
- Both derive the central result of §2: an on-shell vertex depends only on t, so single exchange of a finite-spin
  carrier gives a residue polynomial in the pair's velocity, with velocity scale c.
- The first derivation also gives: the spin-J generalization, the spin tower, the gate's range and the medium
  (§§2–4). The second also gives: the general spin-2 vertex and its pole/contact split, the Dirac case, the
  polynomial bound, the u and s channels, the resonance, readings R1 and R2 with their tails, the record audit,
  the polarization's Lorentz invariance and the preferred frame.
- Neither derivation's own results were checked by a further agent. `verify/gate_mechanism.py` reruns their
  arithmetic and algebra; it does not test their physics.
- Caveats from the second derivation: the main theorem is tree level on a flat background with the Fierz–Pauli
  numerator. Hassan–Rosen nonlinearities and vDVZ subtleties change the t-dependence and normalization, not the
  degree in s. The Lorentzian check transplants the program's block structures to Lorentzian g; the record's
  theorems assume positive H (OP3). Cross-section normalizations use unit couplings; only shapes and tail laws
  are compared.

**Pre-registration of the second derivation, scored** (`review/momentum-gravity/preregistration-run4.md`).
- Right: the polynomial of degree two in s with velocity scale c; the record builds no fiber structure; #6 §4's
  "rational gates" are not a gate in k.
- Partly right: the verdict matched the hedged alternative ("unsupported" for the tag as written), not the first
  choice ("conditional"), which the derivation rules out: no conditional [D] is available. The tag matched only in
  its [P] branch, and not on the stated condition: the derivation gives [P] to the gate itself, not to a
  fiber-resolving X, and finds that §14 item 4 does not cover the gap.
- The weakest link named, the polarization, held up: it is Lorentz-invariant. The scenario it guarded against, a
  ruling of [P] rather than [O], partly happened, for a different reason.
- Missed: reading R1, in which the fiber overlap is an ordinary potential of range ~10 pm.

## Sources

- #11 `papers/broken-born-checkpoint-v2.md` §§1, 7, 8, 12–15; #6 `notes/x-classification.md` §4;
  #5 `notes/geometric-core.md` §§D, E; #1 `notes/broken-born-theory.md` §§2, 3, 5.3; #13
  `papers/conjugate-special-relativity.md` §4; HANDOFF §§2, 3; `papers/phase-space-diameter.md` §8.2.
- `review/momentum-gravity/run3/verify-critic-theory.json` and `run4/gate-derivation.json`, with the scripts named
  there.
- Fierz–Pauli propagator; factorization of pole residues into P_J(z_t); effective-range expansion [T].
- Resonant self-interacting dark matter (e.g. Chu, Garcia-Cely and Murayama 2019) †.
