# The Broken-Born Program: A Working Checkpoint
### Spontaneously broken reciprocity, a massive momentum-space graviton, polarized charge lattices, and the dark-sector trilemma

*Version 2.0 (checkpoint). Supersedes v1.0. Every section opens with a plain-language passage (italic), followed by the technical record. Provenance tags: **[D]** derived in this program, **[T]** established literature, **[P]** postulate, **[O]** open, **[V]** machine-verified this session. References carry **[S]** (retrieved by live search during this project) or **†** (cited from model memory — verify against the source before external use).*

---

## 1. Two abstracts

*In plain terms: Quantum mechanics treats position and momentum as perfect equals; everything else in physics plays favorites. This program treats the equality as a real symmetry that the universe hides, the way a magnet hides the symmetry of its own laws. Following the idea with honest mathematics killed its most cherished consequence — dark matter clumping in velocity instead of space — but forced the survivors into a tight structure: gravity acquires a hidden massive twin whose vacuum energy cancels by symmetry; dark energy becomes a compass angle of the vacuum with a testable drift; the sharpness of dark matter's self-interaction cutoff becomes a diagnostic of what dark matter fundamentally is; and the choice of "which particles are electric" turns out to be the same mathematical move as the choice of "which directions are position" — suggesting the dark sector could be particles, a condensate, or knots.*

**Technical abstract.** We develop an effective framework in which Born reciprocity — the (x,p) → (p,−x) symmetry of quantum kinematics [1†, 2†] — is exact and spontaneously broken. Consistency forces only the symplectic form to be rigid, with the neutral metric η emergent as the order parameter; the geometric sector then organizes into a modular field Z = X + iY on the Siegel domain Sp(2d,ℝ)/U(d): Im Z the spacetime metric, Re Z a second symmetric tensor, reciprocity acting as Z → −Z⁻¹, and the Lagrangian Grassmannian Λ(d) — home of the dark-energy field — as the Shilov boundary. A chain of structural results (a compatibility theorem [V]; the multi-graviton no-go [8†]; a signature obstruction; an explicit tuning test [V]) forces X to be a **massive spin-2** field in the interchange-symmetric branch of Hassan–Rosen bimetric gravity [10†, 11†] with the second frame confined to Λ(4). A four-line identity [V] shows a flat aligned vacuum forces the wedge sector's vacuum energy to vanish exactly; the branch is adjacent to, and contains, the partially-massless parameter point [24S]. Conjugate matter survives as gated self-interacting dark matter whose gate is X-exchange; collective momentum-space clumping is proven non-mandatory everywhere and falsified where it would have been mandatory. The electric–magnetic charge lattice, with its Dirac–Schwinger–Zwanziger symplectic pairing [17†], furnishes a second arena in which the same polarization choice recurs, motivating a three-way question about the dark sector's microstructure: particles, condensate, or topological solitons.

---

## 2. Methodological preface: provenance and verification

*In plain terms: This document was produced in dialogue between a human (intuition, direction, veto power) and an AI (derivation, counterexamples, drafting). AI-generated physics has a known failure mode — fluent confabulation — so every claim here carries a tag saying where it came from, and every piece of load-bearing algebra has been checked by machine, independently of the AI that first wrote it down. What no machine can check is whether the algebra is attached to the right physics; that verdict belongs to expert readers and, ultimately, to data.*

Claims are stratified. **Tier 1** (explicit algebra): verified this session by an independent numerical/exact-integer battery — seven tests covering the compatibility theorem (both directions, including the proof's individual block identities), the Siegel parametrization (I[Z]² = −1, H > 0, det H = 1 across the whole family), the anticommutator block structure, the linearized potential (Tr(S²)/ε² → 4Tr(h²) to six digits, visibly ≠ the Fierz–Pauli form), the palindrome identity as exact integers, the binomial linearization coefficients, and the exclusion of p₄ from the linear span of elementary symmetric polynomials (rms residual 3.29). All seven passed **[V]**. **Tier 2** (literature): correct at the level of well-worn results; exact numbers, conventions, and attributions are flagged † pending source checks. **Tier 3** (novel structural physics): plausibility-tier reasoning; honest prior per claim ~50–80% pending expert review; the selection-versus-derivation bias is acknowledged explicitly where it operates (§7.4). Negative results (§9, §7.1) are the most reliable Tier-3 items, since the program's incentive gradient ran against them.

---

## 3. The question

*In plain terms: In 1938 Max Born noticed that quantum mechanics contains a perfect swap symmetry between position and momentum — the mathematics doesn't care which is which — yet everything real breaks the tie. Atoms are small in space, not in speed; forces fade with distance, never with velocity difference; Einstein curved space and left momentum flat. Born asked why nature uses only half its own symmetry. The question sat for 88 years. Our answer begins: the symmetry is real, and the universe hides it by being forced to point somewhere — because the uncertainty principle forbids any world from being sharp in both variables at once.*

Quantum kinematics is exactly invariant under ρ: (x,p) → (p,−x); the Fourier transform implements it unitarily [1†, 2†]. The asymmetry is dynamical: x-local interactions, the momentum-space mass shell, and general relativity's flat momentum fibers — the last an architectural assumption, not a measurement, and false in the one exactly solved quantum gravity (2+1d, where momenta live on a curved group manifold [5†]; curved momentum space has an independent lineage from Snyder [4†] through relative locality [6†]). The program: ρ is exact and spontaneously broken. The breaking is *mandatory*: [x,p] = iℏ forbids joint locality, so any world with local physics must select a Lagrangian polarization. The magnet must point.

---

## 4. Postulates

*In plain terms: Five rules. One of them, mid-construction, was vetoed by the theory's own mathematics — we had frozen too much background, and the frozen version forbade dark energy and collapsed the theory into plain general relativity. The repair was forced and philosophically right: the structure that says which directions are "position" should be chosen by the vacuum, not written into the rulebook.*

**P1** Physics on phase space with symplectic form ω and positive generalized metric H. [P]
**P2′** Only ω is rigid (symplectic rigidity ≡ constancy of ℏ). The neutral metric η is emergent — the order parameter, η = HJ, with the real structure J chosen spontaneously. [P; the correction from the original P2 is *forced*: a nontriviality theorem (§5) shows the theory has content beyond GR + SIDM iff η is emergent. [D]]
**P3** The action is invariant under the Born rotation generated by I = ω⁻¹H. [P]
**P4** Matter comes in x-polarized (Standard Model) and p-polarized (χ) representations; both couple universally to H; gauge forces do not cross polarizations. [P]
**P5** The vacuum selects a polarization; ours is x-tilted; the mirror vacuum is equally lawful. [P]

---

## 5. The kinematic core and the compatibility theorem

*In plain terms: Three geometric structures can coexist on phase space: the quantum bookkeeping, the metric, and the position/momentum splitter. If you freeze the bookkeeping and the splitter, we proved only one restrictive shape of universe is allowed — momentum's geometry exactly mirrors space's, phase-space volume is locked, and nothing new can exist. Elegant and sterile: this is the theorem that forced the postulate repair.*

With ω, η standard, I = ω⁻¹H, J = η⁻¹H, K = η⁻¹ω satisfy I² = −1, J² = K² = +1, IJ = K — a split-quaternion algebra (Born geometry [3†]; a unique compatible connection exists [7†]).

**Compatibility theorem [D][V].** Positive H satisfying both (η⁻¹H)² = 1 and (ω⁻¹H)² = −1 are exactly H = diag(g, g⁻¹), g ∈ Sym⁺(d). *Proof:* the (2,1) blocks of the two conditions give AC^T + CA = 0 and CA − AC^T = 0, hence AC^T = 0; positivity gives C = 0; the diagonal blocks give B = A⁻¹. ∎ (Both directions and the individual block identities machine-checked.)

Corollaries: det H = 1 identically (ℏ-rigidity is *geometric*, and — machine-verified — persists across the whole modular family of §6); no Kalb–Ramond analog; g̃ = g⁻¹ slaved. Under strict P2 the compatible polarizations are discrete, so no Grassmannian, no Maslov circle, no dark-energy field, and S_H is a functional of g alone: **nontriviality theorem** — the program has content iff η is emergent. Hence P2 → P2′.

---

## 6. The modular field

*In plain terms: After the repair, all the geometry condenses into one complex object Z on a classical mathematical space, Siegel's domain. Its imaginary part is the metric of spacetime. Its real part is a genuinely new field — the local wobble of the position/momentum split. The founding symmetry acts on Z as "take minus the reciprocal"; the fixed point Z = i is the vacuum; the circle |Z| = 1 is the duality between our expanding universe and its contracting conjugate; and dark energy lives on the domain's boundary as a phase.*

With only ω rigid, H ranges over Sp(2d,ℝ)/U(d): Z = X + iY (symmetric; Y > 0), H_Z the standard generalized metric (I[Z]² = −1 machine-verified [V]). Identifications [D]: **Im Z = g**; the η-compatible locus X = 0 is the vacuum slice of §5. **Re Z = X**, the momentum graviton — the fluctuation of the emergent polarization. **ρ: Z → −Z⁻¹** (Möbius; d = 1 check), fixed point Z = i; at X = 0 it is scale-factor duality g → g⁻¹, and the cosmological constraint a·ã = 1 (§10) is the |Z| = 1 locus. **Λ(d) is the Shilov boundary** of the Siegel domain [T]; the dark-energy field τ is the Maslov phase of the boundary variable, its periodicity a fact of topology (π₁(U(d)/O(d)) = ℤ).

---

## 7. The massive momentum graviton (Debt 1)

*In plain terms: The new field X wants, by symmetry, to be a second copy of gravity — and nature forbids identical twins of the graviton: two interacting massless gravities are mathematically inconsistent. (This, we found, is the structural reason string theory's version of doubled geometry works while the symplectic version stalled since Born: string theory's partner field is a harmless different animal; the symplectic partner of the graviton is another graviton.) The only exit is mass, and the theory supplies it automatically: the instant the vacuum picks which half of phase space is "position," X swallows the redundant symmetry and becomes heavy. The health check came down to a tuning test — failed in one formulation, passed in the one the geometry prefers — and the passing version paid an unexpected dividend: X's entire contribution to the energy of empty space cancels exactly, by symmetry.*

**7.1 The chain [D + T].** (i) The rigid Sp(2d,ℝ) contains Z → Z + B (B symmetric): X is shift-symmetric — axion-like, never auxiliary. (ii) Locally, dual diffeomorphisms act as δX_μν = ∂₍μλ_ν₎ — a second linearized-diff gauge field, because X is *symmetric* (contrast DFT's antisymmetric B-field: the symmetry type of the rigid pairing dictates the partner's spin). Massless X is excluded by the multi-graviton no-go [8†]; ungauged X by Lorentz signature. (iii) The polarization choice spontaneously breaks the dual diffs; X eats the four Goldstones and emerges massive, M_X = the polarization-breaking scale. The unique consistent structure for massive spin-2 is Fierz–Pauli/dRGT/Hassan–Rosen [9†, 10†, 11†].

**7.2 The tuning test [D][V].** The Higgs sector is a misalignment potential in {J, I[Z]} = [[S,A],[A,S]], S = Y + XY⁻¹X − Y⁻¹, A = [X, Y⁻¹] (blocks machine-verified). *Metric-tier* implementations fail twice: quadratic mass m²Tr(h²) with no −(Tr h)² (non-FP at linear order — the 66.58-vs-63.72 test of §2), and nonlinear structure Tr(g²) + Tr(g⁻²) provably outside the linear-in-eₙ span (T7). Boulware–Deser ghost. *Frame-tier* couplings — wedge polynomials of the symplectic vielbein E (H = EᵀE) with the polarization frame E₀[J] — are the Hinterbichler–Rosen class [12†], ghost-free by construction; J, E, and the Born connection share the first-order tier, so this is the geometrically minimal formulation.

**7.3 Palindrome and the vacuum-energy identity [D][V].** Reciprocity acts on the wedge sector as frame exchange, forcing **βₙ = β₄₋ₙ**. Then V(1) = 2T exactly (integer identity: [2,8,6] = 2·[1,4,3]), so a flat aligned vacuum (V(1) = T) forces **T = 0 and V(1) = 0**: *the wedge sector contributes zero cosmological constant, by symmetry.* Scope, stated carefully: this cancels the spin-2 interaction potential's vacuum contribution at the aligned point — it does **not** by itself address matter-loop vacuum energy, the "old" cosmological-constant problem, on which bimetric theory is otherwise no better placed than GR [22S].

**7.4 Literature position (updated by this session's search — honesty upgrade).** Exchange-symmetric bimetric potentials are *not* unexplored territory. (a) The interchange-symmetric parameter choice appears in the partially-massless (PM) bimetric literature: the PM point β₀ = 3α⁻²β₂, β₁ = β₃ = 0, β₄ = 3α²β₂ makes the potential g↔f symmetric, with proportional de Sitter solutions of undetermined ratio [24S]. At α = 1 the PM point lies **inside** our palindromic branch — so partially massless gravity, with its celebrated extra gauge symmetry, is a special point of the reciprocity-symmetric family, raising the open question of whether reciprocity is the origin of the PM symmetry [O]. Note the PM point sits at Λ ≠ 0 with c undetermined; our flat-aligned-vacuum identity selects a *different* point of the same branch (β₁ ≠ 0 generically, β₀ = −4β₁ − 3β₂). (b) The theme "exchange symmetry cancels vacuum energy in a two-metric theory" has a precedent in a different mechanism: Hossenfelder's exchange-symmetric bimetric, where twin-sector source terms cancel identically [25S]. Our identity is sector-internal (no twin matter required) and, to our current knowledge, distinct — but the novelty claim is hereby **downgraded from "likely standalone result" to "requires detailed comparison with the PM and exchange-symmetric literature,"** queued as an open item. This is the selection-versus-derivation bias check of §2 operating as intended.

**7.5 Spectrum [D].** Five βₙ → two parameters (M_X ∝ 2(β₁+β₂); one cubic shape). Massless graviton = reciprocity-even (GW graviton-mass bounds satisfied identically); X = reciprocity-odd; SM couplings gravitational-strength and Yukawa-cut at 1/M_X; τ un-eaten (compact J-sector, not the Stückelberg sector).

**Born's answer, as this program states it:** momentum-space geometry is dynamical — a reciprocity-odd massive spin-2, its mass born of the polarization choice, its dynamics the reciprocity-symmetric branch of bimetric gravity with the second frame confined to compact Λ(4), its wedge vacuum energy zero by identity. Momentum space gravitates, massively and invisibly to everything not polarized its way — which is simultaneously why the symmetry is real and why its second metric was never seen.

---

## 8. Conjugate matter and the gate (Debt 2)

*In plain terms: Dark matter, here, is ordinary matter's mirror-polarized cousin: it falls and bends light like everything else, but its private force operates only between particles moving at nearly the same velocity — a gate in relative speed. We first postulated the gate; now we know its mechanism: two conjugate particles exchange the massive momentum-graviton, and can only do so where their momentum-space wavepackets overlap. The observational fingerprint is a knee: self-interaction strong in cold dwarf galaxies, off in hot clusters — and the knee's sharpness is itself a diagnostic.*

χ propagates on g (equivalence principle; Bullet-Cluster-safe) with nonrelativistic amplitude M(k,q) = 4πα̃m_χ/(q² + m_φ²)·F(k²/μ²), k the incoming *relative* momentum — the variable no x-local mediator produces, delivered by X-exchange between dual-stress bilinears, with μ the χ quantum's intrinsic momentum-fiber width [D — mechanism; shape [O]]. σ_T(v) = σ₀F(v²/v*²): robust knee at v*; tail (Gaussian vs rational) diagnoses the vertex completion; isotropic below the gate versus Yukawa forward-peaking. Benchmark: m_χ ≈ 70 MeV·α̃^{2/3}(σ₀/m ÷ 30 cm²g⁻¹)^{−1/3}. Main open quantitative item: the dual-stress enhancement (nuclear-scale σ₀ with gravitational SM couplings) [O].

---

## 9. Obituary: the death of momentum clumping (Debt 3)

*In plain terms: The founding image of this program — dark matter flocking by velocity, invisible murmurations clumping in speed rather than space — was tested three ways and failed all three. For particles, the collective pull falls short by thirty orders of magnitude: never. The mathematics then said collective behavior could exist only if dark matter is a wave — and on the wave side, the one place flocking became mandatory predicted the tiniest galaxies should have bled their dark matter away. They are, in fact, the most dark-matter-rich objects known. The founding intuition died by its own mathematics, which is the machinery working: a theory that cannot lose bets cannot win them. The autopsy yielded one new experimental question — the knee's sharpness distinguishes particle dark matter from wave dark matter — and, in §12, one loophole for individual knots.*

(i) **Particle island [D].** Mean-field criterion g·n_gate ≥ m·min(σ,v*)² fails by 10²⁸–10³¹ at the scattering benchmark; below threshold there is no growth; the H-theorem closes the collisional route. **Classicality theorem:** satisfying the criterion at fixed σ₀/m forces m ≲ 0.1 meV, where N_occ ~ 10²⁰ — collective momentum-space behavior and classical particles are mutually exclusive. (ii) **Wave island [D + T].** Gated wave-kinetic rate Γ ≈ c·g²ρ²min(σ,v*)⁴/(m³σ⁶) (Bose-enhanced, LPT-style [13†]; coefficients [O]). If the gated channel also makes dwarf cores, condensation is mandatory only in ultra-faint dwarfs (Segue 1: rate ratio ~660; condensation ~10⁴ yr), whose attractive endpoint cycles above M_crit ≈ 2.9×10⁻³⁰(m/eV)^{−7/4} M_⊙ [14†] and drains the halo — **falsified** by observed UFD density and longevity; the light-mass escape is closed independently [15†, Lyman-α]. With coupling free, streams are tunable across ~10 orders: optional, never required. (iii) **Net theorem:** velocity-space clumping is nowhere mandatory — forbidden (particles), fatal (committed wave), decorative (free wave). Salvage: the **island discriminant** (knee shape: sharp cutoff ⇒ particle χ; (v*/σ)⁴ ⇒ wave χ) and free relic abundance via misalignment on the wave island.

---

## 10. Cosmology

*In plain terms: Our expanding universe and its contracting conjugate are one motion written twice, like a number and its reciprocal — a relation forced by the constancy of Planck's constant and identical to the |Z| = 1 circle of the modular field. Dark energy is the compass angle of the vacuum's polarization, confined by topology to a circle, so it must drift, can never cross the phantom line, and eventually goes negative — at which point our expansion halts and reverses, an event that in the conjugate ledger is a collapsing universe rebounding. The sky is voting now: DESI's hints of weakening dark energy are exactly the required drift.*

**Constraint [D]:** ω-rigidity fixes the comoving phase-space cell: a·ã = 1 (ℏ does not run) — the |Z| = 1 self-dual locus. **Dictionary [D — corrected en route]:** with one shared lapse, a dual-frame fluid contributes w_eff = −w̃ (superseding an earlier −2 − w̃; the constraint's Jacobian changed the answer — rigor's job). Dual stiff ↦ Λ; dual Λ ↦ stiff; dual curvature ↦ negative dark radiation; dust ↦ dust; the dual Einstein term is an a⁻⁶ step in G_eff. **Dark energy [D + T]:** τ is hilltop quintessence on the Maslov circle, V = V₀[1 + cos(τ/f)], periodicity by topology; strictly w ≥ −1; thawing corridor wₐ ≈ −1.5(1 + w₀); two parameters (f, τᵢ) for three observables (w₀, wₐ, t_turn) — one over-constraint. Current data: compelling evidence for weakening dark energy with phantom behavior less significant (non-phantom compatible at ~2σ) and high posterior preference for a future anti-de Sitter transition and collapse in negative-minimum quintessence fits [19S, 20S, 21S]. The turnaround is the conjugate bounce by constraint identity. §7.3 guarantees the wedge sector contributes nothing that competes with τ.

---

## 11. Polarized charge lattices: monopoles, duality frames, and the recurring matrix

*In plain terms: We buried the idea that conjugate-space monopoles explain why our compasses find no north-without-south — wrong lever for that lock, and inflation already closed the case. But the burial split the claim in two, and the second half stood up: if such objects exist, they must matter, because everything gravitates. Meanwhile the companion conjecture — a whole magnetic mirror-family for every electric particle, magnetic quarks included — turns out to be famous physics: proposed in 1977, named in 1994, and suspected today of being the very mechanism that confines quarks. Its non-observation has the same explanatory shape as our hidden second metric: the duality is real, and its own structure keeps the twin in the attic. Deepest of all: choosing which particles count as "electric" is mathematically the same move as choosing which directions count as "position" — the same rotation matrix generates both dualities. Two intuitions, one operation.*

**11.1 The monopole audit, revised [D].** As an explanation of the null result: dead — the relevant duality is electric–magnetic (E↔B, g → 1/g), not x↔p, and inflationary dilution already accounts for absence [T]. As ontology: alive and consequence-bearing — by P4, conjugate-sector solitons gravitate; "true but irrelevant" is the empty set (a correction supplied by P.R.). Their laboratory shadow is real: Weyl semimetals host catalogued families of momentum-space Berry-curvature monopoles [16†] — right geometry, different flux.

**11.2 The full dual spectrum [T].** The conjecture that every electrically charged particle has a magnetic counterpart is Montonen–Olive duality [17†-adjacent; 18†], exact in maximally supersymmetric Yang–Mills; "magnetic quarks" is standard vocabulary via Seiberg duality [18†]; and the dual-superconductor picture of confinement — chromomagnetic monopole condensation squeezing color-electric flux into strings — is the leading mechanism for why free quarks are never seen [T, 't Hooft–Mandelstam†]. Non-observation is structural: Dirac's condition e·g ~ 2π pins the magnetic coupling near 4π/e² ≈ 34 — the magnetic world is our strong-coupling mirror, heavy and bound. *Same explanatory shape as §7: the duality is genuine, and its structure hides its second half.*

**11.3 The identification [D — structural; math T].** The Dirac–Schwinger–Zwanziger pairing ⟨q, q′⟩ = e₁g₂ − e₂g₁ ∈ 2πℤ is an antisymmetric integer form: **the charge lattice is a symplectic space** [17†]. Mutual locality (which charges can share one Lagrangian) is ⟨q,q′⟩ = 0: a **Lagrangian sublattice**. Choosing a duality frame — which particles are "electric" (fundamental) versus "magnetic" (solitonic) — is choosing a Lagrangian polarization of charge space, in the literature's own words. S-duality acts on the complexified coupling by τ_c → −1/τ_c, generated by the same [[0,1],[−1,0]] rotation as Born's ρ and our Z → −Z⁻¹: the third appearance of one matrix in this program. Conjecture [O]: the phase-space polarization (P5) and the charge-lattice polarization are components of one enlarged modular structure — the BBT-native analog of T- and S-duality cohabiting inside U-duality in string theory [T].

---

## 12. The dark-sector trilemma: particles, condensate, or knots

*In plain terms: The program now offers three different answers to "what is dark matter, fundamentally?" — mirror-polarized particles; a field-condensate of the momentum-graviton itself; or topological knots, the conjugate sector's monopoles. Knots are attractive for a quiet reason: dark matter's absolute stability over thirteen billion years is a puzzle, and topology answers it for free — a knot cannot untie. And knots slip through the loophole in our own no-clumping theorem: that theorem killed collective flocking, gases curdling under mutual attraction; it never touched a single object localized in momentum space because it is a knot, not a flock.*

Candidates, with discriminators [D — framework; each candidate O]:

| Candidate | Origin | Stability | Distinctive handle |
|---|---|---|---|
| **χ particles** (§8) | p-polarized matter field | assumed | knee at v*, sharp tail; isotropic scattering; permanent direct-detection null |
| **X-condensate** | oscillating massive spin-2 (bigravity-DM lineage [23†]) | m_X-protected | unifies dark sector with geometry; coherent-field signatures; knee shape wave-like |
| **Conjugate knots** | topological solitons of a p-local gauge sector (§11) | **free** (topological charge) | superheavy relics; essentially collisionless; compact-object probes (lensing) if heavy; p-localization by topology — the Debt-3 loophole, since §9's theorems address collective dynamics, not imposed topology [O: "solitons of p-local gauge theories are p-localized" is duality-plausible, underived] |

The 5.4 : 1 abundance question (polarization-genesis) applies to all three; the knot option inherits the monopole-abundance machinery of standard cosmology with inflationary dilution acting on both sectors at once.

---

## 13. Predictions and kill conditions

*In plain terms: A theory is its list of ways to die. Here is this one's, updated.*

| # | Observable | Standard expectation | Broken-Born requirement | Killed by |
|---|---|---|---|---|
| 1 | σ_T(v) across halo masses | CDM none; Yukawa SIDM power-law + Coulomb log | Knee at v* ~ 10² km/s; zero cluster signal (particle χ) | Robust self-interaction at v ≫ v*; knee excluded in the 150–400 km/s band |
| 2 | Scattering anisotropy | Forward-peaked (light mediators) | Isotropic below the gate | Morphology demanding forward peaking |
| 3 | **Island discriminant** | (not previously posed) | Knee tail: sharp ⇒ particle; (v*/σ)⁴ ⇒ wave | Diagnostic — selects the branch, incl. trilemma row |
| 4 | Dark energy w(z) | w ≡ −1 | Thawing, w₀ > −1, wₐ < 0, never phantom; drift persists in DESI DR3 | DR3+ constant −1 (kills τ-sector); robust intrinsic w < −1 (kills outright) |
| 5 | Fate of expansion | Eternal de Sitter | Turnaround = conjugate bounce | (Long horizon; near-term test is row 4) |
| 6 | Gravitational waves | m_g = 0 | Massless eigenstate exactly massless (reciprocity-even) | Nonzero mass attributed to the even eigenstate |
| 7 | Direct detection / colliders | WIMP-type signal eventually | **Permanent null** (all three trilemma candidates SM-decoupled) | Any confirmed non-gravitational DM–SM coupling |
| 8 | Magnetic monopoles (ours) | Model-dependent | Permanent null; Berry-curvature monopoles in solids as the only shadow | Direct detection |
| 9 | Photon dispersion | GR none; some QG linear | Linear exactly zero (ρ²-protected); quadratic suppressed | Confirmed linear-in-E dispersion |
| 10 | Early universe | Standard G, N_eff | Optional a⁻⁶ G_eff step; closed dual curvature ⇒ negative ΔN_eff | (Knob-bounded; CMB-S4 probes) |
| 11 | Dark-sector microstructure | (not previously posed) | Particles / condensate / knots separable via rows 1–3 + compact-object lensing + coherence signatures | Diagnostic |

Withdrawn with cause: velocity-space granularity in halos; Fornax friction suppression (obituary §9).

---

## 14. Open problems

*In plain terms: What is honestly unfinished — none of it, any longer, about whether the structure can exist.*

1. First-principles reduction of the frame-tier wedge sector from S_H (class selected, not derived) [O].
2. **PM-adjacency:** detailed comparison of the palindromic branch with partially-massless bimetric [24S]; is reciprocity the origin of the PM symmetry? Convention-careful check of the vacuum-energy identity against [24S, 25S] — the queued novelty audit [O].
3. Lorentzian dressing of the Euclidean-rigorous skeleton [O].
4. Gate shape (X propagator on momentum fibers; Gaussian vs rational — now observable) [O].
5. Dual-stress enhancement parametrics [O].
6. τ–Stückelberg mixing matrix [O].
7. Polarization-genesis: Ω_χ : Ω_b = 5.4 : 1 [O].
8. Charge-lattice polarization: formalize §11.3's unification; conjugate gauge sectors and their soliton spectrum; "p-local solitons are p-localized" [O].
9. Trilemma discrimination program (§12) [O].
10. Literature battery completion; every † reference source-checked [O].

---

## 15. Assessment

*In plain terms: Is there anything here? The founding image is dead, killed by this program's own calculations — the strongest evidence the machinery is honest. What survived is structural, and it survived tellingly: four consecutive consistency tests each forced the theory onto the unique consistent structure available, the last one paying out a vacuum-energy cancellation nobody ordered — though this session's literature check demoted that from "likely new" to "adjacent to known territory, comparison required," which is the process working, not failing. The program has produced one observation that stands regardless of its fate (the symplectic partner of the graviton is another graviton — why string theory's doubling works and Born's stalled), one identity awaiting a novelty verdict, one new experimental question (the knee-shape discriminant), one structural unification (polarization of phase space and of charge space as one move), and a three-way question about dark matter's nature with named discriminators. Its nearest trial is DESI's next release. That is a live research program; the word "theory" still waits on items 1–3 above.*

Lakatos ledger: **hard core** (spontaneously broken reciprocity, ω-only rigidity) intact, twice sharpened by forced corrections (P2′; the w-dictionary). **Progressive signs:** forced convergence onto consistency islands; predictions not previously posed (rows 3, 11); an unsolicited identity (§7.3); one over-constraint (DE sector); the §11.3 unification generating new questions. **Degeneration risks:** tunable wave-island collective sector (quarantined); gate tail not yet forced; the novelty demotion of §7.4 as a standing caution. **Falsification exposure:** genuine and near-term (rows 1, 4, 7).

---

## Appendix A: Audit of founding suppositions (P.R., with fates)

1. Symmetrize QM around conjugate variables — **alive; the hard core** (Born reciprocity, spontaneously broken, ω-only rigid).
2. A coexisting conjugate universe — **alive, transformed**: one state, two ledgers.
3. Matter clumps in momentum space — **dead as dynamics** (§9); **loophole**: topological p-localization of individual solitons untouched (§12).
4. Dark matter is conjugate matter — **alive, modified**: x-clumping, gated self-force; now one corner of a trilemma.
5. Monopoles live in conjugate space, explaining non-detection — **split**: as explanation, dead (wrong duality; inflation suffices); as ontology, alive and consequence-bearing (P.R.'s "true-but-irrelevant is measure zero"), feeding the knot candidate.
6. Conjugate universe shrinks as ours expands — **promoted to theorem** (a·ã = 1 from ℏ-rigidity; the |Z| = 1 locus).
7. Our expansion reverses at their bounce — **alive, corrected**: one event, two ledgers; live at DESI DR3.
8. Synchronized, not causal; Fourier/holography — **alive** (the dictionary); holographic tie loosened, echoed in τ's boundary residence.
9. Their collapse is our acceleration — **dead twice** (w = −2 falsified; corrected dictionary removed the mechanism).
10. Momentum space has its own gravity — **vindicated, transformed**: dynamical, massive, reciprocity-odd (§7).
11. A full magnetic mirror-family, quarks included — **alive as established physics** (Montonen–Olive, Seiberg, dual superconductor), absorbed as §11 with the polarization identification as the program-native addition.

---

## References

*[S] = retrieved by live search during this project; † = cited from model memory — verify before external use.*

[1]† M. Born, "A suggestion for unifying quantum theory and relativity," Proc. R. Soc. Lond. A 165, 291 (1938).
[2]† M. Born, "Reciprocity theory of elementary particles," Rev. Mod. Phys. 21, 463 (1949).
[3]† L. Freidel, R. G. Leigh, D. Minic, "Born reciprocity in string theory and the nature of spacetime," Phys. Lett. B 730, 302 (2014); "Quantum gravity, dynamical phase space and string theory," Int. J. Mod. Phys. D 23, 1442006 (2014).
[4]† H. S. Snyder, "Quantized space-time," Phys. Rev. 71, 38 (1947).
[5]† H.-J. Matschull, M. Welling, "Quantum mechanics of a point particle in 2+1 dimensional gravity," Class. Quantum Grav. 15, 2981 (1998), gr-qc/9708054.
[6]† G. Amelino-Camelia, L. Freidel, J. Kowalski-Glikman, L. Smolin, "The principle of relative locality," Phys. Rev. D 84, 084010 (2011), arXiv:1101.0931.
[7]† L. Freidel, F. J. Rudolph, D. Svoboda, "A unique connection for Born geometry," Commun. Math. Phys. (2019), arXiv:1806.05992.
[8]† N. Boulanger, T. Damour, L. Gualtieri, M. Henneaux, "Inconsistency of interacting, multi-graviton theories," Nucl. Phys. B 597, 127 (2001), hep-th/0007220.
[9]† C. de Rham, G. Gabadadze, A. J. Tolley, "Resummation of massive gravity," Phys. Rev. Lett. 106, 231101 (2011), arXiv:1011.1232.
[10]† S. F. Hassan, R. A. Rosen, "Resolving the ghost problem in non-linear massive gravity," Phys. Rev. Lett. 108, 041101 (2012), arXiv:1106.3344.
[11]† S. F. Hassan, R. A. Rosen, "Bimetric gravity from ghost-free massive gravity," JHEP 1202, 126 (2012), arXiv:1109.3515.
[12]† K. Hinterbichler, R. A. Rosen, "Interacting spin-2 fields," JHEP 1207, 047 (2012), arXiv:1203.5783.
[13]† D. G. Levkov, A. G. Panin, I. I. Tkachev, "Gravitational Bose–Einstein condensation in the kinetic regime," Phys. Rev. Lett. 121, 151301 (2018); "Relativistic axions from collapsing Bose stars," Phys. Rev. Lett. 118, 011301 (2017).
[14]† P.-H. Chavanis, "Mass–radius relation of self-gravitating Bose–Einstein condensates with attractive self-interaction," Phys. Rev. D 84, 043531 (2011), arXiv:1103.2050.
[15]† N. Dalal, A. Kravtsov, "Excluding fuzzy dark matter with sizes and stellar kinematics of ultrafaint dwarf galaxies," Phys. Rev. D 106, 063517 (2022), arXiv:2203.05750.
[16]† S.-Y. Xu et al., "Discovery of a Weyl fermion semimetal," Science 349, 613 (2015); B. Q. Lv et al., Phys. Rev. X 5, 031013 (2015).
[17]† P. A. M. Dirac, Proc. R. Soc. Lond. A 133, 60 (1931); J. Schwinger, Phys. Rev. 144, 1087 (1966); D. Zwanziger, Phys. Rev. 176, 1489 (1968).
[18]† C. Montonen, D. Olive, "Magnetic monopoles as gauge particles?" Phys. Lett. B 72, 117 (1977); N. Seiberg, "Electric–magnetic duality in supersymmetric non-abelian gauge theories," Nucl. Phys. B 435, 129 (1995), hep-th/9411149.
[19][S] I. D. Gialamas, G. Hütsi, M. Raidal, J. Urrutia, M. Vasar, H. Veermäe, "Quintessence and phantoms in light of DESI 2025," arXiv:2506.21542.
[20][S] L. A. Ureña-López et al. (DESI), axion-quintessence analysis of DESI data, arXiv:2503.20178.
[21]† DESI Collaboration, DR2 BAO cosmology results (2025), arXiv:2503.14738.
[22][S] A. Schmidt-May, M. von Strauss, "Recent developments in bimetric theory," J. Phys. A 49, 183001 (2016), arXiv:1512.00021.
[23]† E. Babichev, L. Marzola, M. Raidal, A. Schmidt-May, F. Urban, H. Veermäe, M. von Strauss, "Bigravitational origin of dark matter," Phys. Rev. D 94, 084055 (2016), arXiv:1607.03497.
[24][S] Partially massless bimetric gravity and its exchange-symmetric parameter point, arXiv:1609.09515.
[25][S] S. Hossenfelder, "A bi-metric theory with exchange symmetry," Phys. Rev. D 78, 044015 (2008), arXiv:0807.2838.

---

*Provenance: conjecture and direction, P. R.; derivations, counterexamples, verification battery, and drafting, Claude (Anthropic). Working checkpoint — not for submission until the † audit (open item 10) completes.*
