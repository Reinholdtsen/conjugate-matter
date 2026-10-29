# The Broken-Born Program
### Spontaneously broken reciprocity, a massive momentum-space graviton, and the fate of conjugate matter

*Version 1.0 — consolidation of the full development arc. Each section opens with a plain-language passage, then the technical record. Provenance tags: [D] derived here, [T] established literature, [P] postulate, [O] open.*

---

## 0. Two abstracts

**In plain terms.** *Quantum mechanics treats position and momentum with perfect even-handedness; the rest of physics plays favorites. This document develops the idea that the even-handedness is a real symmetry of nature, hidden the way a magnet hides the symmetry of its own laws. Following that idea with honest mathematics killed its most cherished consequence — dark matter clumping in velocity rather than in space — but forced the survivors into a sharp, economical structure: gravity acquires a hidden massive twin, that twin's contribution to the energy of empty space cancels exactly by symmetry, dark energy becomes a compass angle of the vacuum with a testable drift, and dark matter's self-interaction gains a diagnostic shape. The result is a research program with two free parameters per sector, kill conditions on every claim, and its trial date set by ongoing surveys.*

**Technical abstract.** We develop an effective framework in which Born reciprocity — the (x, p) → (p, −x) symmetry of quantum kinematics — is exact and spontaneously broken. Consistency forces the symplectic form alone to be rigid, with the neutral metric η emergent as the order parameter; the geometric sector then organizes into a single modular field Z = X + iY on the Siegel domain, with Im Z the spacetime metric, Re Z a second symmetric tensor, reciprocity acting as Z → −Z⁻¹, and the Lagrangian Grassmannian (dark energy's home) as the Shilov boundary. A chain of structural theorems — a compatibility theorem, the multi-graviton no-go, a signature obstruction, and an explicit tuning test — forces X to be a massive spin-2 field in the interchange-symmetric branch of Hassan–Rosen bimetric gravity with the second frame confined to the compact space Λ(4). In that branch a four-line theorem shows a flat aligned vacuum forces the massive sector's vacuum energy to vanish exactly. The conjugate-matter sector survives as gated self-interacting dark matter whose gate is X-exchange; its collective (momentum-clumping) phenomenology is proven non-mandatory everywhere and falsified where it would have been mandatory. Cosmology reduces to hilltop axion-like quintessence on the Maslov circle: thawing, never phantom, with an eventual turnaround identified with the conjugate frame's bounce by constraint. Predictions, kill conditions, and the honest open residue are catalogued.

---

## 1. The question

**In plain terms.** *In 1938 Max Born noticed that quantum mechanics contains a perfect swap symmetry between position and momentum — the mathematics doesn't care which is which — yet everything real breaks the tie. Atoms are small in space, not in speed; forces weaken with distance, never with velocity difference; Einstein curved space and left momentum flat. Born asked why nature uses only half of its own symmetry, and the question sat unanswered for 88 years. Our starting move: the symmetry is real, and the universe hides it the way a cooled magnet hides the rotational symmetry of its laws — by being forced to point somewhere.*

The kinematics of quantum mechanics is exactly invariant under the Born rotation ρ: (x, p) → (p, −x); the Fourier transform implements it unitarily and the canonical commutator is blind to it. All asymmetry lives in dynamics: Hamiltonians are p²/2m + V(x), interactions are local in x, the mass shell is a momentum-space structure with no positional twin, and general relativity curves x-space while leaving momentum fibers flat — an assumption of the formalism, not a measurement, and one that is *false* in the one exactly solved quantum gravity (2+1 dimensions, where momentum space is a curved group manifold) [T]. The program: promote ρ to an exact, spontaneously broken symmetry and follow the consequences until they are falsified or forced into shape. The uncertainty principle guarantees the breaking is mandatory, not optional: nothing can be local in both variables at once, so any universe with local physics must pick a polarization. The choice is the magnet's direction.

## 2. Postulates — including the one the mathematics rejected

**In plain terms.** *Five rules define the game. Mid-construction, the theory's own mathematics vetoed one of them: we had frozen too much of the background, and the frozen version turned out to forbid dark energy and to reduce everything to plain general relativity. The repair was forced, and it was also the philosophically right move — the structure that says which directions count as "position" should be decided by the vacuum, not written into the rulebook.*

- **P1 (Arena).** Physics on phase space carrying a symplectic form ω and a positive generalized metric H. [P]
- **P2′ (Rigidity — corrected).** Only ω is non-dynamical: symplectic rigidity is the constancy of ℏ. The neutral metric η is *not* fundamental; it is the order parameter, η = HJ, with the real structure J chosen spontaneously. [P; the correction from the original P2 is forced by the theorems of §3 and §5 — a nontriviality theorem shows the theory has content beyond GR + SIDM *iff* η is emergent [D].]
- **P3 (Reciprocity).** The action is invariant under the Born rotation generated by I = ω⁻¹H. [P]
- **P4 (Polarized matter, universal gravity).** Matter comes in x-polarized (Standard Model) and p-polarized (χ) representations; both couple universally to H; gauge forces do not cross polarizations. [P]
- **P5 (Spontaneous breaking).** The vacuum selects a polarization; ours is x-tilted; the mirror vacuum is equally lawful. [P]

## 3. The kinematic core and the compatibility theorem

**In plain terms.** *Three geometric structures can live on phase space: the quantum structure (ω), the metric (H), and the position/momentum splitter (η). We proved that if you freeze the first and third, only one restrictive shape of universe is allowed — momentum's geometry exactly mirrors space's, nothing new can exist, and the volume of phase space is locked. Elegant, and sterile: this is the calculation that forced the repair of the postulates.*

With ω and η standard, the endomorphisms I = ω⁻¹H, J = η⁻¹H, K = η⁻¹ω obey I² = −1, J² = K² = +1, IJ = K — a split-quaternion algebra (Born geometry in the sense of Freidel–Leigh–Minic [T]; a unique compatible connection exists [T: Freidel–Rudolph–Svoboda 2018]).

**Compatibility theorem [D].** The positive H satisfying both (η⁻¹H)² = 1 and (ω⁻¹H)² = −1 are exactly H = diag(g, g⁻¹), g ∈ Sym⁺(d). *Proof:* the (2,1) blocks of the two conditions give AC^T + CA = 0 and CA − AC^T = 0, hence AC^T = 0; positivity forces C = 0; the diagonal blocks force B = A⁻¹. ∎

Corollaries: det H = 1 identically (unimodularity: ℏ-rigidity is *built into* the geometry); no Kalb–Ramond analog; momentum metric slaved, g̃ = g⁻¹. Under strict P2 the space of compatible polarizations is discrete (the 2^d coordinate splittings), so there is no Grassmannian, no Maslov circle, no τ — no dark-energy sector — and S_H is a functional of g alone. Hence the nontriviality theorem of §2 and the repair P2 → P2′.

## 4. The modular field

**In plain terms.** *After the repair, everything geometric condenses into a single complex object Z, living on a classical mathematical space (Siegel's domain). Its imaginary part is the metric of spacetime. Its real part is a brand-new field — the local wobble of the position/momentum split. The founding symmetry acts on Z as "take minus the reciprocal," the same operation that relates a number to its inverse; the self-dual point Z = i is the vacuum, the circle |Z| = 1 is the cosmological duality between our expanding universe and its contracting conjugate, and dark energy lives on the boundary of the domain as a phase.*

With only ω rigid, H ranges over Sp(2d,ℝ)/U(d), coordinatized by Z = X + iY (Y > 0, both symmetric), with the standard generalized-metric parametrization (verified explicitly: I[Z]² = −1). Identifications, each cross-checked against the independent derivations elsewhere in the arc [D]:

- **Im Z = g** (the metric); the η-compatible locus X = 0 is precisely the vacuum slice of the compatibility theorem.
- **Re Z = X**: the momentum graviton — the fluctuation of the emergent polarization.
- **Reciprocity = Z → −Z⁻¹** (Möbius action; d = 1 matrix check), fixed point Z = i. At X = 0 it sends g → g⁻¹: scale-factor duality. The minisuperspace constraint a·ã = 1 (§8) is the |Z| = 1 locus.
- **Λ(d) = the Shilov boundary of the Siegel domain** [T]; the dark-energy field τ is the Maslov phase of the boundary variable, its 2πf periodicity a fact of topology (π₁(U(d)/O(d)) = ℤ), not a modeling choice.

## 5. The second graviton and its mass (the field-equation problem: solved)

**In plain terms.** *The new field X wants, by symmetry, to be a second copy of gravity — and nature forbids identical twins of the graviton: two interacting massless gravities are mathematically inconsistent. (This, we found, is the deep reason string theory's version of doubled geometry works: its partner field is a harmless different animal, while the symplectic partner of the graviton is another graviton.) The only exit is mass, and the theory supplies it automatically: the instant the vacuum picks which half of phase space is "position," X swallows the redundant symmetry and becomes heavy. Checking that this is ghost-free came down to a tuning test — failed in one formulation, passed in the one the geometry prefers — and the passing version delivered a bonus: by a four-line theorem, X's entire contribution to the energy of empty space cancels exactly. A cosmological-constant cancellation for free, from symmetry.*

The chain, each link load-bearing:

1. **Shift symmetry [D].** The rigid Sp(2d,ℝ) contains Z → Z + B (B symmetric): X is axion-like — no potential from geometry, "auxiliary" excluded.
2. **Gauge structure and no-go [D+T].** Locally, dual diffeomorphisms act as δX_μν = ∂₍μλ_ν₎ — a second copy of linearized diffs, because X is symmetric. Massless: excluded by the multi-graviton no-go (Boulanger–Damour–Gualtieri–Henneaux) since X must couple. Ungauged: excluded by Lorentz signature (wrong-sign mixed components). Contrast DFT, whose partner is the antisymmetric B-field — a 2-form, spin-harmless: *the symmetry type of the rigid pairing dictates the partner's spin, which is why η-doubling (strings) exists and ω-doubling stalled since Born.*
3. **The mass [D].** The polarization choice spontaneously breaks the dual diffs; X eats the four Goldstones (gravitational Higgs) and emerges as a massive spin-2 with M_X the polarization-breaking scale. The unique consistent home for a massive spin-2 coupled to gravity is the Fierz–Pauli/dRGT/Hassan–Rosen structure [T].
4. **The tuning test [D — both branches computed].** The Higgs sector is a misalignment potential in {J, I[Z]} = [[S, A],[A, S]] with S = Y + XY⁻¹X − Y⁻¹, A = [X, Y⁻¹] (computed exactly). *Metric-tier* implementations fail twice over: the quadratic mass comes out m²Tr(h²) with no −(Tr h)² (non-Fierz–Pauli at linear order), and the nonlinear structure contains Tr(g²) + Tr(g⁻²), provably outside the linear-in-eₙ Hassan–Rosen span. Boulware–Deser ghost. *Frame-tier* implementations — wedge polynomials of the symplectic vielbein E (H = EᵀE) with the polarization frame E₀[J] — are the Hinterbichler–Rosen class [T], ghost-free by construction. J, E, and the Born connection all live on the first-order tier: the passing formulation is the geometrically minimal one.
5. **The palindrome and the Λ theorem [D — rigorous].** Reciprocity acts on the wedge sector as frame exchange, forcing βₙ = β₄₋ₙ — identifying the theory as the interchange-symmetric branch of bimetric gravity and supplying that branch's previously missing raison d'être. Then, with eₙ(1) = C(4,n) and tadpole T = β₁ + 3β₂ + 3β₃ + β₄: the palindrome gives **V(1) = 2T**, so a flat aligned vacuum (V(1) = T) forces **T = 0 and V(1) = 0 exactly.** One condition does what generic bimetric needs two tunings for: *the massive sector's vacuum energy is zero by symmetry.* Dark energy is left entirely to τ — deriving the architecture §8 had assumed. (Literature check on whether this Λ = 0 property of symmetric bimetric was previously noticed: flagged [O]; if not, it is a standalone result.)
6. **Spectrum and parameters [D].** Five βₙ → two (M_X ∝ 2(β₁+β₂) and one cubic-shape parameter). Massless graviton = reciprocity-even (GW graviton-mass bounds satisfied identically); X = reciprocity-odd; SM couplings to X are gravitational-strength and Yukawa-cut at 1/M_X; τ is not eaten (it lives in the compact J-sector, not the Stückelberg sector).

**Born's answer, as this program states it:** momentum-space geometry is dynamical — a reciprocity-odd *massive* spin-2 field, its mass born of the polarization choice, its dynamics the reciprocity-symmetric branch of Hassan–Rosen bimetric with the second frame confined to the compact Λ(4). Momentum space gravitates, massively and invisibly to everything not polarized its way. That is simultaneously why the symmetry is real and why its second metric was never seen.

## 6. Conjugate matter and the gate (the gate problem: mechanism found)

**In plain terms.** *Dark matter, here, is ordinary matter's mirror-polarized cousin: it falls and bends light like anything else, but its private force only operates between particles moving at nearly the same velocity — a "gate" in relative speed. We originally postulated the gate; now we know where it comes from: two conjugate particles interact by exchanging the massive momentum-graviton X, and they can only do so where their momentum-space wavepackets overlap. The gate's width is the particle's own size in momentum space. The observational fingerprint is a knee in the self-interaction strength: strong in cold dwarf galaxies, switching off in hot clusters — with the sharpness of the knee now itself a diagnostic.*

χ propagates on g (equivalence principle, Bullet-Cluster-safe) with nonrelativistic self-interaction amplitude M(k, q) = 4πα̃m_χ/(q² + m_φ²) · F(k²/μ²), where q is transfer and k the incoming *relative* momentum — the variable no x-local mediator can produce, delivered here by X-exchange between dual-stress bilinears with μ identified as the χ quantum's intrinsic momentum-fiber width [D — mechanism; shape [O]]. Consequences: σ_T(v) = σ₀ F(v²/v*²) with a robust knee at v* and a tail (Gaussian vs rational) that diagnoses the vertex completion; isotropic scattering below the gate versus the forward peaking of light-mediator Yukawa models; benchmark m_χ ≈ 70 MeV·α̃^{2/3}(σ₀/m ÷ 30 cm²g⁻¹)^{−1/3} for particle-χ, with the wave-χ alternative in §7. The main open quantitative item: the dual-stress enhancement parametrics — why σ₀ can be nuclear-scale while SM–X couplings stay gravitational [O].

## 7. The death of momentum clumping (the clumping problem: closed, negative)

**In plain terms.** *The founding image of this whole program was dark matter flocking by velocity — invisible starling-murmurations clumping in speed rather than space. We tested it three ways and it failed all three. For ordinary particles, the collective pull falls short by a factor of a million trillion trillion: never. The mathematics itself then said collective behavior could only exist if dark matter is a wave, not particles — and on the wave side, the one place flocking became mandatory, it predicted that the tiniest galaxies should have bled their dark matter away. The tiniest galaxies are, in fact, the most dark-matter-rich objects known. The founding intuition died by its own mathematics — which is the machinery working: a theory that cannot lose bets cannot win them. The autopsy yielded one genuinely new idea: the sharpness of the self-interaction knee now distinguishes particle dark matter from wave dark matter, a question nobody was previously asking the data.*

Three results [D]:

1. **Particle island.** Mean-field Vlasov analysis gives the instability criterion g·n_gate ≥ m·min(σ, v*)²; at the scattering benchmark (coupling already fixed by dwarf cores) it fails by 10²⁸–10³¹ in every environment. Below threshold there is no growth at all; the H-theorem closes the collisional route. **Classicality theorem:** satisfying the criterion at fixed σ₀/m forces m ≲ 0.1 meV, where N_occ ~ 10²⁰ — collective momentum-space behavior and classical-particle dark matter are mutually exclusive.
2. **Wave island.** The gated wave-kinetic condensation rate is Γ ≈ c·g²ρ²min(σ, v*)⁴/(m³σ⁶) (Bose-enhanced, LPT-style [T]; coefficients to calibrate [O]). If the gated channel also makes dwarf cores, condensation is mandatory only in ultra-faint dwarfs (Segue 1: rate ratio ≈ 660, condensation time ~10⁴ yr) — where the attractive endpoint cycles through collapse above M_crit ≈ 2.9×10⁻³⁰(m/eV)^{−7/4} M_⊙ and *drains the halo*. Observed UFDs are the densest, oldest, most DM-dominated systems known: **falsified.** The light-mass escape is independently excluded (UFD heating bounds ≈ 3×10⁻¹⁹ eV, Dalal & Kravtsov 2022 [T — verify figure]; Lyman-α). With the coupling left free instead, streams are merely tunable across ~10 orders — optional, never required.
3. **Net theorem:** nowhere in viable parameter space is velocity-space clumping mandatory — forbidden (particles), fatal (wave, committed coupling), decorative (wave, free coupling). Salvage: the **island discriminant** — self-interaction suppression is a sharp knee for particle χ but (v*/σ)⁴ for wave χ, so the knee's *shape* identifies dark matter's fundamental nature; and the wave island gets its relic abundance from misalignment for free, closing a separate open problem.

## 8. Cosmology

**In plain terms.** *Our expanding universe and its contracting conjugate are one motion described twice — like a number and its reciprocal — a relation that turns out to be forced by the constancy of Planck's constant, and to be the |Z| = 1 circle of the modular field. Dark energy is the compass angle of the vacuum's polarization, confined by topology to a circle, so its potential must be periodic: it therefore drifts, can never cross the phantom line, and eventually goes negative — at which point our expansion halts and reverses, an event that in the conjugate description is a collapsing universe rebounding. The sky is currently voting: the DESI survey's hints of weakening dark energy are exactly the drift this sector requires, and its next data release is this framework's nearest trial date.*

- **The constraint [D].** ω-rigidity fixes the comoving phase-space cell: a·ã = 1. Not an assumption — the statement that ℏ does not run; geometrically, the |Z| = 1 self-dual locus.
- **The dictionary [D — corrected en route].** With one shared lapse, a dual-frame fluid contributes w_eff = −w̃ (superseding an earlier heuristic −2 − w̃; the Lagrange-multiplier treatment changed the answer, which is what rigor is for). Dual stiff ↦ Λ; dual Λ ↦ stiff; dual curvature ↦ (negative) dark radiation; dust ↦ dust. The dual Einstein term itself is an a⁻⁶ step in G_eff — an optional early-universe fingerprint.
- **Dark energy [D+T].** τ is hilltop quintessence on the Maslov circle: V = V₀[1 + cos(τ/f)], periodicity by topology, V₀ fixed by Ω_DE, two remaining parameters (f, τᵢ) for three observables (w₀, wₐ, t_turn) — one over-constraint. Strictly w ≥ −1; thawing corridor wₐ ≈ −1.5(1+w₀). Current fits: DESI-era analyses report compelling evidence for weakening dark energy with the phantom interpretation less significant (non-phantom compatible at ~2σ), and quintessence fits with negative-minimum potentials prefer a future anti-de-Sitter transition and collapse at high posterior odds (Gialamas et al. 2025, arXiv:2506.21542; axion-type fits: Ureña-López et al. 2025, arXiv:2503.20178) [T — refresh citations before publication]. The turnaround is the conjugate bounce by the constraint identity: one event, two descriptions. §5's Λ theorem guarantees the massive-gravity sector contributes nothing to compete with τ.

## 9. Predictions and kill conditions

**In plain terms.** *A theory is its list of ways to die. Here is this one's.*

| # | Observable | Standard expectation | Broken-Born requirement | Killed by |
|---|---|---|---|---|
| 1 | σ_T(v) across halo masses | CDM: none; Yukawa SIDM: power-law tail with Coulomb log | Knee at v* ~ 10² km/s; tail shape = vertex diagnostic; zero cluster signal (particle χ) | Robust self-interaction at v ≫ v*; knee excluded in 150–400 km/s band |
| 2 | Scattering anisotropy (halo relaxation morphology) | Forward-peaked (light mediators) | Isotropic below the gate | Morphology demanding forward-peaked kernels |
| 3 | **Island discriminant** | — (question not previously posed) | Knee sharpness: sharp cutoff ⇒ particle χ; (v*/σ)⁴ ⇒ wave χ | (Diagnostic, not a kill: identifies the branch) |
| 4 | Dark energy w(z) | w ≡ −1 | Thawing drift, w₀ > −1, wₐ < 0, on the thawing corridor; **never phantom**; drift persists in DESI DR3 | DR3+ converging on constant −1 (kills τ-sector); robust intrinsic w < −1 (kills outright) |
| 5 | Fate of expansion | Eternal de Sitter | Turnaround after V(τ) < 0 = conjugate bounce | (Long-horizon; near-term test is row 4) |
| 6 | Gravitational waves | m_g = 0 | Massless eigenstate exactly massless (reciprocity-even); massive X short-range | Any nonzero graviton mass attributed to the even eigenstate |
| 7 | Direct detection / collider DM | Eventually expected (WIMP-type) | **Permanent null** — χ (or X-condensate) has no non-gravitational SM coupling | Any confirmed DM–SM non-gravitational coupling |
| 8 | Magnetic monopoles | Model-dependent | Permanent null; Berry-curvature monopoles in solids as the only shadow | Direct detection |
| 9 | Photon dispersion | GR: none; some QG: linear | Linear term exactly zero (protected by ρ²); quadratic allowed, suppressed | Confirmed linear-in-E dispersion |
| 10 | Early universe | Standard G, N_eff | Optional a⁻⁶ G_eff step; closed dual curvature ⇒ negative ΔN_eff | (Bounds constrain knobs; CMB-S4 probes) |

Withdrawn with cause, permanently: velocity-space granularity in halos; Fornax friction suppression (rows 3–4 of earlier versions; obituary in §7).

## 10. Open problems

**In plain terms.** *What is honestly unfinished — none of it, any longer, a question of whether the structure can exist.*

1. First-principles reduction of the frame-tier wedge sector from S_H (the class was selected by minimality + consistency, not derived line-by-line) [O].
2. Lorentzian dressing of the Euclidean-rigorous skeleton (stabilizer U(1,3); the FP/HR machinery is exactly the tool it lands on) [O].
3. Gate shape: the X propagator on momentum fibers; Gaussian vs rational tail (now doubly motivated — it is observable) [O].
4. Dual-stress enhancement parametrics: σ₀ nuclear-scale with gravitational SM couplings [O].
5. τ–Stückelberg mixing matrix; expected small by compactness [O].
6. Polarization-genesis: the 5.4 : 1 ratio Ω_χ : Ω_b — the program's baryogenesis analog [O].
7. X-condensate as the dark matter itself (bigravity-DM-style), potentially eliminating χ and unifying the dark sector with the geometry [O — direction, deliberately unopened].
8. Literature verifications: symmetric-bimetric Λ = 0; LPT coefficient calibration; Dalal–Kravtsov exact bound [O].

## 11. Assessment

**In plain terms.** *Is there anything here? The founding intuition is dead — killed by this program's own calculations, which is the strongest evidence the machinery is honest. What survived was not the picturesque part but the structural part, and it survived in a specific, telling way: four consecutive consistency tests, each of which could have ended the geometric sector, instead forced it onto the unique consistent structure available at that junction — and the last one yielded a cosmological-constant cancellation nobody ordered. Programs that keep predicting novel facts are progressive; programs that only redescribe are degenerating. This one has produced at least two results that stand on their own regardless of its fate — the observation that the symplectic partner of the graviton is another graviton (explaining why string theory's doubling works and Born's stalled), and the palindrome theorem cancelling the symmetric-bimetric vacuum energy — plus one new experimental question (the knee-shape island discriminant). Its nearest trial is DESI's next release. That is a live research program by any standard in use.*

The Lakatos appraisal, plainly: **hard core** — spontaneously broken reciprocity with ω-only rigidity — intact and sharpened by the P2 → P2′ correction. **Progressive signs** — forced convergence onto consistency islands (no-go → Higgs → HR class → palindrome); novel predictions not previously posed (island discriminant; knee shape; even-eigenstate masslessness as a bimetric-parity statement); an unsolicited theorem (Λ_wedge = 0); one over-constraint in the DE sector. **Degeneration risks** — the wave-island collective sector is tunable (flagged, quarantined); the gate's tail shape is not yet forced. **Falsification exposure** — genuine and near-term (rows 1, 4, 7). The word "theory" awaits items 1–2 of §10; the phrase "research program," used precisely, is earned now.

*Provenance note: developed in dialogue; conjecture and direction by P. R.; derivations, counterexamples, and drafting by Claude (Anthropic). All citations flagged [T — verify] should be checked against sources before any submission.*
