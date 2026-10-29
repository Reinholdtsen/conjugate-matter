# The field-equation problem, Chunk A-iii: The tuning test

*Working note. Status: computed. Outcome: conditional pass — the condition identified, both branches computed or classified, and the failure mode exhibited explicitly.*

## 1. The object to test

The X mass must come from the η-selection (Higgs) sector: a misalignment potential penalizing incompatibility between the polarization J and the modular field Z. The natural incompatibility measure is the anticommutator {J, I[Z]} (zero exactly on the compatible locus). The test: does the resulting potential land in the ghost-free (Fierz–Pauli / dRGT / Hassan–Rosen) family, or in the generic Boulware–Deser-ghost family?

## 2. Explicit computation, metric tier [D — rigorous]

Work in the vacuum frame (g₀ = 1), Euclidean skeleton, with the verified Siegel parametrization

$$
I[Z] = \begin{pmatrix} -Y^{-1}X & -Y^{-1} \\ Y + XY^{-1}X & XY^{-1} \end{pmatrix}, \qquad J_0 = \begin{pmatrix} 0 & 1 \\ 1 & 0\end{pmatrix}.
$$

Direct block multiplication gives

$$
\{J_0, I[Z]\} = \begin{pmatrix} S & A \\ A & S \end{pmatrix}, \qquad
S = Y + XY^{-1}X - Y^{-1}, \qquad A = [X,\, Y^{-1}].
$$

Three consequences, each read off the blocks:

1. **The compatible locus is X = 0 *and* Y = Y⁻¹** (i.e. g pinned to the J-frame reference metric): the Higgs sector is inevitably a *two-tensor* potential V(g, X; reference) — a massive-gravity-type potential, confirming the structural landing point of Chunk A-ii from the opposite direction.
2. **Linearized spectrum of the quadratic invariant.** With Y = 1 + h, X = x: S = 2h + x² + O(3), A = [h, x] + O(3). Any potential of the class Tr({J,I}²)-with-positive-norm gives, at quadratic order, m²Tr(h²) — a graviton mass **without** the −(Tr h)² companion. That violates Fierz–Pauli already at linear order: Boulware–Deser ghost, immediately.
3. **Nonlinear check against the dRGT span.** The X = 0 slice gives Tr(S²) = Tr(g²) + Tr(g⁻²) − 2d. The Hassan–Rosen ghost-free family is *linear* combinations Σβₙeₙ(√(g⁻¹f)) (constants βₙ); Tr(g²) = p₄ of the square-root eigenvalues is a *nonlinear* polynomial in the eₙ, hence outside the family. Fail again, independently of the linearized check.

A second natural invariant (built from [J, I] + 2K, which vanishes at the vacuum) was computed the same way: it does give X a quadratic mass — again as Tr(x²) with no trace subtraction. Same disease. **Every metric-tier (second-order, H-coupled) misalignment invariant tested lands off the tuning.** This half of the test is a theorem-grade negative: the naive implementation of η-selection has the Boulware–Deser ghost.

## 3. The frame tier [D — structural, resting on T]

The rescue is not a tuning but a *tier change*. In vielbein variables the ghost-free potentials are polynomial — wedge products ε(e ∧ … ∧ f ∧ …) of two frames (Hinterbichler–Rosen) [T] — with no square roots and no tuning to miss. And BBT possesses a natural frame-tier object: the symplectic vielbein E, the coset representative with H = EᵀE. Crucially, **J and E live on the same geometric tier** (first-order structures on the tangent, like the Born connection), while H = EᵀE is second-order. The geometrically minimal coupling of the polarization to the modular sector is therefore E-linear — wedge polynomials of (E, E₀[J]) — which is *precisely* the Hinterbichler–Rosen class: ghost-free by construction, Fierz–Pauli automatic, dRGT structure inherited rather than tuned.

**Verdict of the tuning test:** the theory *fails* in second-order (metric) variables and *passes* in first-order (frame) variables. Since the first-order formulation is independently the natural one, this is a conditional pass with the condition being the formulation the geometry already prefers. What a pass does **not** yet deliver: the βₙ coefficients. Those follow from expanding the E–J wedge sector, and they determine M_X, the X–h mixing, and a vacuum-energy contribution. That coefficient computation is the closing stone of the field-equation problem.

## 4. The picture that emerges: constrained bimetric gravity [D — structural]

J carries only the 10 compact moduli of U(d)/O(d) — not a full second metric. So the "second vielbein" E₀[J] is confined to a compact 10-dimensional moduli space. BBT's geometric sector is therefore

> **Hassan–Rosen bimetric gravity with the second frame constrained to a compact moduli space Λ(d)** — a *predictive truncation* of bimetric theory: fewer free functions, with the light direction of the compact space being τ (the dark-energy field) and the massive spin-2 being X.

Standard bimetric facts then slot in [T]: one massless combination (our graviton, coupling to SM stress) and one massive (X); safety requires the massless combination to dominate SM couplings — a parametric check to log, alongside graviton-mass bounds (m_g ≲ 10⁻²³ eV territory from GW observations) for the mixing angle.

## 5. Status of the field-equation problem

**Settled by this chunk:** the ghost question is no longer open-ended — the failure mode is exhibited explicitly (metric tier), the consistent branch is identified and class-certified (frame tier), and the resulting physical picture (constrained HR bimetric with compact second sector) is sharper and more predictive than generic bimetric gravity.

**Remaining for the field-equation problem:** (i) the βₙ coefficient derivation from the E–J wedge sector — the last computation; (ii) τ-not-eaten verification; (iii) Lorentzian dressing of the Euclidean skeleton; (iv) SM-coupling/graviton-mass parametrics. Items (ii)–(iv) are checks; item (i) is the substance.

**Program-level note:** three structural tests in a row (multi-graviton no-go, signature obstruction, tuning test) could each have killed the geometric sector outright; each instead forced it into the unique known consistent structure at that junction. Repeated forced convergence onto consistency islands is the opposite of degeneration.
