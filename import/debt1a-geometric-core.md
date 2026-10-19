# Debt 1, Chunk A — the geometric core, linearized groundwork
### (plus an unplanned payment on Debt 2)

*Overnight working note. Status: two rigorous results, one axiom correction forced, one mechanism identified, one decisive computation defined but not completed.*

---

## A. The compatibility theorem [D — rigorous]

**Claim.** On flat phase space with ω and η both in standard form, the positive generalized metrics H satisfying the full Born algebra — (η⁻¹H)² = +1 **and** (ω⁻¹H)² = −1 — are exactly

$$
H = \begin{pmatrix} g & 0 \\ 0 & g^{-1} \end{pmatrix}, \qquad g \in \mathrm{Sym}^+(d).
$$

**Proof.** Write H in blocks $\begin{pmatrix} A & C \\ C^T & B\end{pmatrix}$. The (2,1) blocks of the two conditions give $AC^T + CA = 0$ and $CA - AC^T = 0$, hence $AC^T = 0$; positivity makes $A$ invertible, so $C = 0$. The diagonal blocks then give $BA = AB = 1$, so $B = A^{-1}$. ∎

**Corollaries.**
1. **det H = 1 identically.** The generalized metric is unimodular: phase-space volume is not a dynamical field. ℏ-rigidity is manifest in the geometry, not imposed on it.
2. **No Kalb–Ramond analog.** The off-diagonal block — DFT's B-field — is frozen out by the extra symplectic compatibility. Born geometry with both structures rigid is *stiffer* than DFT.
3. **The momentum metric is slaved: g̃ = g⁻¹ pointwise.** No independent momentum-space geometry survives.

## B. The inconsistency, and the forced repair [D — structural]

Corollary 3 collides with the theory as documented. Under strict P2 (ω **and** η rigid):

- The space of polarizations compatible with both structures (ω-Lagrangian *and* η-null) is **discrete** — the 2^d coordinate-type splittings, GL(d)-rigid. No Lagrangian Grassmannian, no Maslov circle, **no τ field**. The dark-energy sector as constructed contradicts P2.
- With H = diag(g, g⁻¹), S_H is a functional of g alone: a pure metric theory. No momentum graviton, hence no geometric origin for the χ gate either.

Call this **Branch R** (rigid): BBT reduces to GR + one bespoke SIDM model, with w ≡ −1 and the gate unexplained. On Branch R the program has no content of its own — and it is *already disfavored* if DESI's drift is real.

**The repair (P2′).** Freeze ω only — that is genuinely ℏ — and let **η be emergent: the order parameter itself.** Concretely: the fundamental pair is (ω, H); the derived complex structure is I = ω⁻¹H; the vacuum spontaneously selects a real structure J (an involution anticommuting with I), and η ≡ HJ. The space of H-compatible real structures on (ℝ^{2d}, I) is

$$
\{J\} \;\cong\; U(d)/O(d) \;=\; \Lambda(d),
$$

the Lagrangian Grassmannian — π₁ = ℤ, Maslov circle intact, τ restored, and the earlier observation that reciprocity flips η now reads correctly as *the broken symmetry moving the order parameter.* This is also the philosophically right assignment: η is the structure that says which directions are position — of course that is what the vacuum decides, not the background.

**Program-nontriviality theorem:** BBT has content beyond GR + SIDM **iff** η is emergent. P2 → P2′ is not optional. (The flagship doc's axiom list is corrected in the v0.3 addendum.)

## C. The modular field [D — structural; math facts standard]

With P2′, the dynamical space opens up: positive H compatible with ω alone form the **Siegel domain** Sp(2d,ℝ)/U(d), coordinatized by a complex symmetric matrix

$$
Z = X + iY, \qquad Y > 0, \qquad
H_Z = \begin{pmatrix} Y + XY^{-1}X & XY^{-1} \\ Y^{-1}X & Y^{-1} \end{pmatrix}.
$$

Identifications, each checkable against everything derived so far:

- **Im Z = Y = g**, the spacetime metric. At X = 0, H = diag(g, g⁻¹): the η-compatible locus of Theorem A is precisely the vacuum slice.
- **Re Z = X**, a *new symmetric tensor*: the momentum graviton. It is exactly the fluctuation that breaks η-compatibility — i.e., the local wobble of the emergent polarization, "which way the x/p split points, here."
- **Born reciprocity acts as Z → −Z⁻¹** (Möbius action of the I-rotation; d = 1 check: matrix [[0,1],[−1,0]] gives Z → −1/Z). Fixed point Z = i: the self-dual vacuum of the earlier turns, now as modular geometry. The cosmological constraint a·ã = 1 is the |Z| = 1 self-dual circle — the minisuperspace duality was the shadow of this modular action.
- **Λ(d) is the Shilov boundary of the Siegel domain** [standard]. The τ field — arg det of the boundary variable — is the phase of Z's boundary value.

One object now carries the whole geometric program: **metric (Im Z), momentum geometry and gate mediator (Re Z), scale-factor duality (|Z|), dark energy (boundary phase of Z).** Born's debt, restated exactly: *the field equation for momentum-space geometry is the Re Z sector of S_H.*

## D. Quadratic spectrum and the ghost question [partial]

Field content on the broken vacuum: h_μν (10, graviton) ⊕ X_μν (10, momentum graviton) ⊕ Λ(d) σ-modes (10: τ plus nine, of which inverse-Higgs constraints likely eliminate most [O]) ⊕ matter. Good signs: the Siegel target metric Tr(Y⁻¹dZ Y⁻¹dZ̄) is positive-definite, and the DFT precedent (graviton + B-field + dilaton, ghost-free) shows doubled-geometry kinetic operators can be healthy [T]. The decisive check is now well-posed: expand the generalized curvature scalar of (ω, H_Z) to quadratic order in X about X = 0 on the section, with ω-generalized diffeomorphisms as the gauge symmetry, and classify X as one of:

1. **healthy propagating** → dynamical momentum-space gravity (Born's dream, linearized);
2. **auxiliary** (no derivatives at quadratic order) → integrate out → a *contact, momentum-structured* four-χ operator, i.e. the gate delivered directly;
3. **ghost** → fatal to the geometric sector.

Outcomes 1 and 2 both serve the program; only 3 kills. Not completed tonight; it is the single most important remaining calculation, and it is now a defined computation rather than a slogan.

## E. Debt 2 — the mechanism, found [D — structural]

The gate's origin falls out of §C. Conjugate matter couples to H universally (P4); its coupling to the X-block is through the **dual stress** T̃ — moments involving momentum-derivatives of the χ bilinear. Exchange of X between two such bilinears yields a four-point amplitude that depends on the **incoming relative momenta** of the pair — the variable no x-local mediator can produce, and exactly the variable the gate was postulated in. Structurally:

$$
\text{gate} \;=\; \text{momentum-graviton exchange}, \qquad \mu \;\leftrightarrow\; (M_X,\,M_B)\ \text{parametrically}.
$$

The gate *shape* is the X propagator's structure on the momentum fibers — open [O], and downstream of the §D classification (outcome 2 gives it most cheaply). SM safety: X is massive and couples to x-polarized matter only through its (suppressed) dual stress; short-range, fifth-force-safe — to be verified when the propagator exists [O].

## F. Ledger after tonight

**Paid:** the compatibility theorem; discovery and repair of an axiom-level inconsistency (P2 → P2′, with a nontriviality theorem making the repair mandatory); Born's debt reframed from slogan to a specific sector of a specific field (Re Z); Debt 2's mechanism identified (gate = X-exchange); unimodularity of H (det H = 1) as the geometric face of ℏ-rigidity; the modular unification (reciprocity = Z → −Z⁻¹, cosmological duality = |Z| = 1).

**Now precisely open:** (1) the quadratic X classification of §D — *do this next*; (2) gate shape from the X propagator; (3) the origin of τ's potential under P2′ (what explicitly breaks Λ(d) rotations — candidate: the section choice itself, or matter loops); (4) inverse-Higgs accounting of the nine heavy moduli; (5) connection uniqueness for the (ω, H)-only structure (FRS proved it for the full triple; the para-Hermitian literature — Svoboda, Marotta–Szabo — is the nearest neighbor).
