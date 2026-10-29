# Wiki build — suspected errors in the source documents

*Found by the fresh-context verifiers of the wiki depth pass (2026-10-21). The wiki quotes
every source faithfully and corrects none of these; each needs Paul's ruling. Where
arithmetic is involved, the verifier's executed check is in `review/wiki-build-checks/`
with its output; it is not part of `verify/`, and a ruling that accepts a flag should add
the check there.*

**Audit (2026-10-22).** Every flag below was re-checked by independent agents told to refute it:
two for each of the eleven mathematical flags (one steelmanning the source, one recomputing from
scratch), one for each of the rest. Result for flags 1–42: 32 confirmed, 8 depend on a convention or a reading
(the source is defensible under one the documents support), 2 unclear (they rest on model memory),
none refuted. Each flag carries its verdict; the full verdicts are in
`review/wiki-build-checks/flag-audit.json` and the auditors' scripts and outputs in
`review/wiki-build-checks/audit/`.

**Where to start**, by consequence for the program's claims:

- **27**: the dark-energy potential as written cannot go negative, so the turnaround (prediction
  row 5, and t_turn in the over-constraint) needs an unwritten offset or another mechanism.
- **55**: the dark-matter gate's mechanism is not derived: exchanging the record's X cannot produce
  it; the suggested tags are [P] for the gate and [O] for its mechanism (#11 §8, abstract, §§12,
  13 rows 1–3, 15).
- **43**: the program's thawing corridor itself lies in the CPL quadrant that reads as a crossing;
  what separates it from DR2's crossing is the slope (z = 2 against z ≈ 0.4), not the quadrant.
  This bears on how row 4's pressure is stated, not on whether it exists.
- **23**: a·ã = 1 holds on the whole vacuum slice X = 0; the |Z| = 1 identification needs a ruling
  (#11 §6, §10; #5 §C; #1 v0.3; HANDOFF §2).
- **39**: #11 states two different actions of ρ on the spin-2 sector, and they give the graviton
  opposite parities.
- **3**: the misalignment potential vanishes on a larger set than stated, with a flat valley.
- **6**: the vacuum-energy identity needs one tuning (T = 0); "by symmetry rather than tuning"
  overstates it.
- **49**: the dual Einstein–Hilbert term behind #11 §10's a⁻⁶ step (row 10) is not derived, so
  every bound on the dual frame tests a postulate.
- **27 (addendum), 46**: with the potential as written, row 5 needs a closed universe, and closure
  moves the over-constraint to Ω_k.
- **1**: the η-null Lagrangian polarizations form continuous families for d ≥ 2; the conclusion
  (no Maslov circle) survives.
- **33, 34**: `verify/soliton_obituary.py` claims more coverage than it has, and calls typed-in
  constants "PDG and Planck 2018 values".
- **42, 41**: a toy-note revision recorded as applied was not carried out; a result listed as
  shown by executed code rests on an analytic argument.
- **5, 28**: M_X should be M_X²; the formula beside "≈ 34" should be π/e², not 4π/e².
- The rest are wording, pointers, dates and references.

1. **Null-Lagrangian polarizations are not discrete for d ≥ 2.** `notes/geometric-core.md`
   §B (line 27), echoed in #11 §5 and #9 §3: the ω-Lagrangian, η-null polarizations are
   "discrete — the 2^d coordinate-type splittings, GL(d)-rigid". For any subspace V ⊂ ℝ^d,
   V ⊕ V^⊥ (V in x, V^⊥ in p) is ω-Lagrangian and η-null, so they form continuous
   Grassmannian families Gr(k, d). The conclusion survives: det² (Maslov phase) is constant
   (±1) on each family, so no Maslov circle and no τ; the x-polarization is isolated.
   Found by the wave-1 verifier (postulates batch); scratch evidence
   `review/wiki-build-checks/verifier_null_lagrangians.py` (d = 2, 3). Suggested wording:
   "no continuous family through the x-polarization; det² is constant, so no Maslov circle".
   **Audit (2026-10-22): confirmed by 2 independent checks (one steelmanning the source, one recomputing from scratch).** Wrong as written for d ≥ 2, including the program's d = 4. The ω-Lagrangian, η-null polarizations are exactly V ⊕ V^⊥: d+1 continuous GL(d)-orbits Gr(k,d), not 2^d rigid points. The flag's rescue holds: det² = (−1)^(d−k) is constant on each family and the x-polarization is isolated, so there is no Maslov circle and no τ.
2. **"I is odd in K" (toy note §5, line 152).** I[W] = ∫(∫W)² ≥ 0 cannot be odd under
   K → −K; the gated values 0.4070 and 0.3600 show only that I is not invariant under it.
   Suggested wording: "I is not invariant under K → −K". ADJ4 F3 and toy note §2 use "a
   coupling odd in K" as a requirement, which is fine.
   **Audit (2026-10-22): confirmed by 1 independent check.** I[W] = ∫(∫W)² ≥ 0 in both vacua (0.4070, 0.3600); oddness would need I(−K) = −I(K). I has a K-odd part but is not odd. ADJ4 F3, citing I_K as its example of a K-odd coupling, shares the slip.
3. **The misalignment potential's zero set is larger than stated (#7 §2).** `notes/tuning-test.md`
   §1–§2 says {J₀, I[Z]} vanishes exactly on "X = 0 and Y = Y⁻¹". The blocks are A = [X, Y⁻¹] and
   S = Y + XY⁻¹X − Y⁻¹; with A = 0 (X, Y commuting) S = (Y² + X² − 1)Y⁻¹, so the zero set is
   {X, Y commute, X² + Y² = 1}, which contains points with X ≠ 0. At d = 1 it is the whole
   circle |Z| = 1 (the self-dual locus), not only Z = i. Consequence for the tuning test: at
   quadratic order x is a flat direction (consistent with battery T4's Tr(S²)/ε² → 4Tr(h²)).
   Found by the tuning verifier (wave 2). Needs a ruling: is the degeneracy along |Z| = 1
   intended, and does it affect the vacuum structure claims?
   **Audit (2026-10-22): confirmed by 2 independent checks (one steelmanning the source, one recomputing from scratch).** Wrong as written. By #7 §1's own definition (the anticommutator's zero set) and #5 §B's P2′ compatibility, the locus is {[X,Y]=0, X²+Y²=1}: 10-dimensional at d=4, the arc |Z|=1 at d=1, exactly flat along a valley tangent to x. Only adding X=0 (η₀-compatibility) or rigid η₀ (abandoned P2) gives Z=i. The two-tensor conclusion survives.
4. **Missing −h² in the expansion of S (#7 §2 item 2).** "S = 2h + x² + O(3)" should be
   S = 2h + x² − h² + O(3) (Y⁻¹ = 1 − h + h² − …). Executed checks by two agents:
   `review/wiki-build-checks/s_expansion.py` (a second agent's independent check agreed). The
   quadratic-order Fierz–Pauli test (T4) is unaffected (it uses only S ≈ 2h).
   **Audit (2026-10-22): confirmed by 1 independent check.** #7 defines Y = 1 + h; then S = 2h + x² − h² + O(3), so the source drops −h². The line is exact only for Y = e^h, which no document uses, or under h ~ x² counting, which contradicts its own "at quadratic order". Harmless to the conclusions: Tr(S²)'s quadratic term is exactly 4Tr(h²).
5. **M_X ∝ 2(β₁+β₂) should probably be M_X² (#11 §7.5, #9 §5 item 6).** Their source, #8 §3,
   writes "m_FP² ∝ β₁ + 2β₂ + β₃ = 2(β₁+β₂), i.e. M_X"; the β-combination fixes the squared
   Fierz–Pauli mass [T]. Flagged independently by three agents. Notation only.
   **Audit (2026-10-22): confirmed by 2 independent checks (one steelmanning the source, one recomputing from scratch).** #11 §7.5 and #9 §5 item 6 drop the square that their source, #8 §3, carries. M_X is a mass in the same paragraph (Yukawa range 1/M_X), the documents use ∝ strictly elsewhere, and the potential is linear in βₙ, so M_X² ∝ 2(β₁+β₂). Notation only: the two-parameter count stands and no number depends on it.
6. **"By symmetry rather than tuning" overstates the vacuum-energy identity (#1 v0.6, #10).**
   The flatness condition V(1) = T is itself one condition on the βₙ, and #8 §3 counts T = 0 as
   removing a parameter. #8 §2's wording is the accurate one. #11 §7.3 says "by symmetry";
   worth checking it against this. The phrase also appears in #11's plain-language passages
   (§1, §7), #9 §5 and #8 §2's closing sentence, so a ruling should cover those too.
   **Audit (2026-10-22): confirmed by 2 independent checks (one steelmanning the source, one recomputing from scratch).** The palindrome kills only the odd tadpole, giving V(1) = 2T; the even tadpole, setting the aligned vacuum's cosmological constant m⁴T/M², stays free. Zero needs T = 0, one tuning: #8 §3 counts it, #11 §7.4 says flatness 'selects' a point, the palindromic PM point has T = 6β₂ ≠ 0. #8 §2's 'two tunings' holds only at fixed c = 1.
7. **"The unique consistent structure" (#11 §7.1)** drops #6 §3's qualifier "exactly one *known*
   consistent structure" for massive spin-2. Mild overstatement. #6 §5, #9 §5 item 3, #11 §15
   and HANDOFF §1 also drop "known"; #6 §3 and #7 §5 keep it.
   **Audit (2026-10-22): confirmed by 1 independent check.** #6 §3 says 'exactly one known consistent structure'; #11 §7.1 says 'The unique consistent structure'. #6 §5, #9 §5 item 3, #11 §15 and HANDOFF §1 also drop 'known'; #7 §5 keeps it. Nothing cited proves uniqueness.
8. **#8 §3 "five-function freedom"**: the βₙ are constants (#7 §2), so "five-parameter".
   **Audit (2026-10-22): confirmed by 1 independent check.** #8 §3 says 'HR bimetric's five-function freedom collapses to two numbers'. The freedom is five constants βₙ (#7 §2: 'constants βₙ'; #8's own count 'five βₙ → … two'), so 'five-parameter' is meant.
9. **#11 ref [24][S] (arXiv:1609.09515)** has no authors and its title may be a description
   rather than the paper's title. Being [S], it falls outside the † battery (OP10).
   **Audit (2026-10-22): confirmed by 1 independent check.** #11 [24][S] has no authors and an unquoted, descriptive title. arXiv:1609.09515 is Apolo, Hassan, Lundkvist, 'Gauge and global symmetries of the candidate partially massless bimetric gravity', PRD 94, 124055 (2016). As [S], OP10's † battery skips it.
10. **Smaller pointers and wording.**
    - #1 §1 P2 points to §5 for the dark-energy potential; it is in §3.
    - `notes/toy-lagrangian.md` lists "ρ sits inside a continuous U(1)" as unpredicted although
      its Predictions section anticipated the restored U(1) in 1+1.
    - `verify/toy_s5.py` part C still says "built from K"; v2 §5 says built from (H, K),
      SO(2)-covariant.
    - The round-4 referee's audit notes use "boost" for two different families (the squeezes
      diag(a, 1/a) and the hyperbolic boosts).
   **Audit (2026-10-22): confirmed by 1 independent check.** All four hold: #1 P2 cites §5 for the potential (it is §3); the worklog's Predictions already had 'the continuous U(1) … that contains ρ'; toy_s5.py part C says 'built from K'; round-4 notes call two families 'boost'.
11. **Tadpole growth in model II: ln N or 2 ln N.** The toy note v2 §4 says the level-0
    tadpole grows as "ln N" (a harmonic sum); the round-4 referee and the adjudication (F6,
    revision 4) say 2 ln N; `verify/toy_gw.py` checks only one harmonic series. Recorded as
    unresolved in the wiki's register of conflicts between sources (`wiki/history/documents/source-conflicts.md`, entry C29).
   **Audit (2026-10-22): depends on a convention or reading.** Both are logarithmic. The level-0 tadpole holds two equal harmonic sums (row, column): Σ_k(G0k+Gk0) ≈ 2 ln N is the referee's T₀; one sum ≈ ln N is the note's; the averaged vertex is ≈ 4 ln N. Normalization only.
12. **V_b's zero mode is not an exact squeeze symmetry.** `review/round4-adjudication.md` F2 and
    revision 1 call it an "exact" squeeze symmetry; a sympy check by the toy-coset verifier
    finds V_b not squeeze-invariant off K = ±K_ref. The toy note v2's "not symmetry-protected"
    is the accurate statement (conflicts register, entry C28); the wiki follows v2.
   **Audit (2026-10-22): confirmed by 2 independent checks (one steelmanning the source, one recomputing from scratch).** The adjudication's 'exact symmetry' is wrong for V_b. The squeeze leaves V_λ and the kinetic terms invariant but not V_b, whose Tr KᵀK breaks it; no nonzero sp(2) generator preserves V_b. The zero mode is an exact classical flat line, but the fluctuation masses vary along it, so no symmetry protects it. Toy note v2 is right.
13. **Minor: ⟨|m|⟩ = 0.954 ± 0.0001 "at every size" (toy note §4).** `verify/toy_s4.py` prints
    ± 0.0000 at L = 64; the note's figure is a conservative bound, not the printed value.
   **Audit (2026-10-22): confirmed by 1 independent check.** toy_s4.py prints ± 0.0001 at L = 16 and 32 but ± 0.0000 at L = 64. The note's '± 0.0001 at every size' is an upper bound, matching the gate's test (SEM < 0.0002), not the printed value.
14. **Minor notation (#7 §2): "Tr(g²) = p₄ of the square-root eigenvalues".** This holds for the
    eigenvalues of √(f⁻¹g); for √(g⁻¹f), the matrix bimetric potentials use, it gives Tr(g⁻²)
    (spin2-b verifier's executed check). The conclusion (outside the eₙ span, battery T7) stands.
   **Audit (2026-10-22): depends on a convention or reading.** Right for the eigenvalues of √(f⁻¹g), the square roots of g's eigenvalues at f = 1. Wrong for the √(g⁻¹f) the sentence names: there p₄ = Tr(g⁻²), and Tr(g²) is not even a polynomial in those eₙ. #7 fixes neither root nor measure. #8 §1's exchange identity makes the √(f⁻¹g) presentation equivalent under a fixed measure. Conclusion stands.
15. **Minor wording (#6 §2, `notes/x-classification.md` line 17): "η
    antisymmetric-pairing vs ω"** reads as calling η antisymmetric; η is the symmetric
    (neutral) metric and ω the antisymmetric form.
   **Audit (2026-10-22): confirmed by 1 independent check.** #6 §2 writes 'η antisymmetric-pairing vs ω', attaching 'antisymmetric' to η, the symmetric neutral metric. The intent is probably 'η gives an antisymmetric partner'. #11 §7.1 already rewords it ('the symmetry type of the rigid pairing').
16. **A ✓ without a script.** HANDOFF §2 marks the clumping shortfall "fails by 10²⁸–10³¹" as
    machine-verified, but no `verify/` script checks it (#11 §9 tags it [D]). The wiki
    verifier's recomputation `review/wiki-build-checks/stream_stability_check.py` reproduces it and
    could be moved into `verify/`.
   **Audit (2026-10-22): confirmed by 1 independent check.** HANDOFF §2 marks 'criterion fails by 10²⁸–10³¹' with ✓ (machine-verified), but no verify/ script or check.sh entry covers the clumping problem, and #11 §9 tags it [D]. The scratch stream_stability_check.py reproduces the ratios (3.9e-28, 2.9e-31).
   **Addendum (2026-10-28).** `verify/velocity_gated_gravity.py` (§D) now ports 3a's arithmetic
   into the gate and reproduces both ratios, with the linearized values beside them (flag 58). The
   ✓ is now backed by a script; #11 §9's tag [D] is unchanged until Paul rules. "10²⁸–10³¹" quotes
   the ratios' exponents; the shortfall factors are 2.6×10²⁷ and 3.5×10³⁰.

17. **Two gate conventions, a √2 in μ.** #6 §4 writes the gate as e^{−(p₁−p₂)²/2μ²}, #1 §3 as
    e^{−k²/μ²} with k the relative momentum. With p₁ − p₂ = 2k these differ by √2 in μ, so with
    #6's fiber width the knee sits at v\* = μ/m_χ rather than #1's v\* ≡ √2μ/m_χ; #13 §4 mixes
    the two. No stated number changes. Check: `review/wiki-build-checks/gate_conventions.py`.
   **Audit (2026-10-22): depends on a convention or reading (both of 2 checks).** The √2 is real only if #6's e^{−(p₁−p₂)²/2μ²} is read as the amplitude gate. #6 never defines its width or overlap. Its expression equals #1 §5.1's rate factor e^{−v²/v*²} with #1's μ. #1 v0.4, #8, #9, #11 §8 and HANDOFF identify #1's μ with the fiber width, so #13 §4 is right under that convention. No number changes.
18. **Minor date (#1 §8): baryogenesis reached "maturity … in 1966".** Sakharov's conditions are
    usually dated 1967 (model memory, †, unchecked). Conflicts register, entry C54.
   **Audit (2026-10-22): unclear (rests on model memory).** #1 §8 does say 'the same maturity baryogenesis had in 1966', naming no work. The 1967 dating of Sakharov's conditions is model memory; no repository file independently dates it, so under the † rule it stays unverified.
19. **Minor: the classicality corollary's regime (#2, calc note #2).** The corollary evaluates the
    broad-gate formula at Milky Way conditions, which 3a itself treats as the narrow-gate
    regime. `review/wiki-build-checks/stream_stability_check.py` prints m_crit ≈ 1.4e-13 GeV (broad
    form) and 4.2e-14 GeV (narrow form, v\* fixed); N_occ ≫ 1 either way, so the conclusion
    (collective behaviour needs wave dark matter) is unchanged.
   **Audit (2026-10-22): depends on a convention or reading.** The flag's facts hold: 3a applies the broad-gate form at Milky Way conditions (0.4, 155 km/s), which its own table treats as narrow-gate. Read as a ceiling, the corollary is right: 3a's narrow form is at most 0.064× the broad, so 1.4e-13 GeV caps m, as #11 §9 ('forces m ≲ 0.1 meV') uses it. Read as the Milky Way threshold, it is about 3× high (4.2e-14 GeV).
20. **#11 reference [23]† pairs one paper's title with another's arXiv number.** It gives the title
    and journal of "Bigravitational origin of dark matter" (Phys. Rev. D 94, 084055, which is
    arXiv:1604.08564) with arXiv:1607.03497, the companion paper "Heavy spin-2 Dark Matter".
    Found by the dm-candidates verifier by live search. For the † battery (OP10).
   **Audit (2026-10-22): confirmed by 1 independent check.** #11 [23]† pairs the title and journal of 'Bigravitational origin of dark matter' (PRD 94, 084055 = arXiv:1604.08564) with arXiv:1607.03497, which is 'Heavy spin-2 Dark Matter' (JCAP 09 (2016) 016). Confirmed by live fetch.
21. **Minor attribution (round-3 ruling 3).** The ruling says the referee's Kibble–Zurek integration
    gave "1e9–1e12 overproduction"; the integration itself gave 1.1e12–2.2e12
    (`review/round3/referee/step4.out`). The 1e9 lower end comes from the Liveoak–Maharana–Wells
    analytic estimate (1.2e9–2.2e11). The verdict is unaffected (overproduction either way).
   **Audit (2026-10-22): confirmed by 1 independent check.** Ruling 3 attributes '1e9–1e12 overproduction' to the referee's Kibble–Zurek integration. step4.out's integration gives 1.14e12–2.22e12; the 1e9 end is the LMW eq. (25) analytic estimate (1.24e9–2.16e11), which the referee's notes list separately.
22. **Minor: Planck's N_eff interval (#14 §4).** #14 gives "2.99 +- 0.34"; the round-3 referee's
    audit records Planck eq. 67b as +0.34/−0.33. The 0.286 bound uses only the +0.34 side, so
    nothing changes.
   **Audit (2026-10-22): confirmed by 1 independent check.** #14 §4 writes 'N_eff = 2.99 +- 0.34 at 95%'; the referee's verbatim quote of Planck 2018 VI eq. (67b) is '2.99 +0.34 −0.33'. The 0.286 bound uses only the upper side (2.99 + 0.34 − 3.044).
23. **a·ã = 1 and the |Z| = 1 locus (#11 §6, §10).** #11 identifies the cosmological constraint
    a·ã = 1 with the |Z| = 1 locus. At X = 0, H_Z = diag(Y, Y⁻¹); with g = a² = Y and the
    momentum block ã² = Y⁻¹, a·ã = 1 holds along the whole imaginary axis (it is det H = 1),
    while |Z| = 1 meets that axis only at Z = i. Either the identification needs a different
    reading of a and ã, or it is a slip. The identification also appears in #5 §C, #1 addendum
    v0.3 and HANDOFF §2, so a ruling should cover all four. The same check reproduces the corrected dictionary
    w_eff = −w̃ and the falsified heuristic −2 − w̃. Check:
    `review/wiki-build-checks/self_dual_locus.py`.
   **Audit (2026-10-22): confirmed by 2 independent checks (one steelmanning the source, one recomputing from scratch).** With the sources' a² = Im Z = Y and ã² = momentum block Y⁻¹, a·ã = 1 holds on the whole vacuum slice X = 0 (it is det H = 1). |Z| = 1 crosses that slice only at Z = i and is the self-dual locus a = ã. No reading the documents support rescues the identification, and no number changes.
24. **Minor: "square exactly at the bounce" (HANDOFF §4, chat-only).** The phase-space diameter
    relation does not say which bounce. If it is the turnaround, the rectangle would be most
    elongated there, not square. The wiki states the ambiguity.
   **Audit (2026-10-22): confirmed by 1 independent check.** HANDOFF §4 says the rectangle is square 'exactly at the bounce' without saying which. With D_x·D_p fixed, the aspect ratio grows with a (10⁹² today), so it is square near a ~ 10⁻⁴⁶ a₀, and most elongated at the turnaround.
25. **Minor pointer: #1 §1 P2 and §4 cite "§7" for the cosmological constraint**, which is derived
    in #1 §6 (conflicts register, entry C21).
   **Audit (2026-10-22): confirmed by 1 independent check.** #1 P2 ('a ã = const (§7)') and §4's ghost accounting ('the P2 constraint (§7)') point to §7, but the constraint is derived in §6, 'Cosmology I: the constraint and the corrected dictionary'. §7 only uses it.
26. **Minor: DESI DR3 as "three-year data" (HANDOFF §2).** DR2 (arXiv:2503.14738) already covers
    three years of operations (live-searched by the cosmo-de writer). The wiki quotes HANDOFF.
   **Audit (2026-10-22): confirmed by 1 independent check.** HANDOFF §2 calls DESI DR3 'three-year data', but the DR2 paper #11 cites as [21S] (arXiv:2503.14738) says its measurements are 'based on three years of operation'. Confirmed by live fetch of the abstract.
27. **The dark-energy potential cannot turn negative as written (#11 §10, #9, #1 §7).** The
    turnaround ("eventually goes negative", "turnaround after V(τ) < 0") needs V < 0, but the
    stated potential V = V₀[1 + cos(τ/f)] has minimum 0 for V₀ > 0. #1 §7 says "a cosine
    potential is negative over half its range", which is true of V₀cos(τ/f) but not of
    V₀[1 + cos(τ/f)]. Either the potential carries a negative offset not written down, or the
    turnaround needs another mechanism. This bears on prediction row 5 (turnaround = conjugate
    bounce) and on the dark-energy over-constraint (t_turn). Conflicts register, entry C20. Check:
    `review/wiki-build-checks/v_sign_check.py`.
   **Audit (2026-10-22): confirmed by 2 independent checks (one steelmanning the source, one recomputing from scratch).** Confirmed; no defensible reading exists. V₀[1+cos(τ/f)] never changes sign for either sign of V₀, and V₀ < 0 cannot be dark energy (w ≥ 1). Under the documents' own flat Friedmann equation a turnaround needs ρ = 0, unreachable with V ≥ 0; turnarounds appear only for an offset c < 1. As written, t_turn is undefined.
   **Addendum (2026-10-27, closed-universe investigation).** The "other mechanism" exists if the
   universe is closed. In closed V₀[1 + cos(τ/f)] histories, τ passes its minimum and oscillates as
   dust, and curvature then reverses the expansion with V ≥ 0 throughout. With τ frozen at the hilltop
   there is no turnaround, and flat or open universes never turn around. So "eventually goes
   negative" (#11 §10) and "eventual negative V ⇒ turnaround" (`HANDOFF.md` §2) name the wrong cause,
   and row 5 holds only if k = +1. Round-5 R11 states that a closed turnaround exists; flag 50 adds its
   conditions. `notes/closed-universe.md` §2. Check: `verify/closed_universe.py` §B.
28. **The formula for our magnetic coupling (#11 §11.2).** #11 says Dirac's e·g ~ 2π "pins the
    magnetic coupling near 4π/e² ≈ 34". With α = e²/4π, 4π/e² = 1/α ≈ 137; e·g = 2π gives
    g²/4π = π/e² = 1/(4α) ≈ 34.26. The number 34 is right; the formula written beside it is
    not. (This 34 is our own magnetic coupling, distinct from the dead α_d ≈ 34 of the
    soliton episode.) Check: `review/wiki-build-checks/dirac_coupling_check.py`.
   **Audit (2026-10-22): confirmed by 2 independent checks (one steelmanning the source, one recomputing from scratch).** I derived Dirac's condition independently (Wu–Yang, in HL and Gaussian units). It gives α·α_m = 1/4 at the minimum, so 34 = 1/(4α) = π/e² is right. In the program's own convention α = e²/4π (#14 §2, v3-worklog R2), 4π/e² = 1/α ≈ 137, which is the e·g = 4π value. In Gaussian units it is 1722. Only reading e as twice the elementary charge rescues the formula, and that reading contradicts e·g ~ 2π.
29. **#13 cites #11 §7 for a claim #11 does not make.** #13 §1 and §6 tag X's effect being "in
    momentum" as "[D — checkpoint §7]". #11 §7 never mentions a dual cone, and §7.5 says
    "Yukawa-cut at 1/M_X", a range in position. The momentum reading appears only among the
    chat-only results (HANDOFF §4).
   **Audit (2026-10-22): confirmed by 1 independent check.** #13 §1 and §6 tag X's 'short range in momentum' / 'Yukawa-cut in momentum' [D — checkpoint §7]. #11 mentions no cone; §7.5 has SM couplings 'Yukawa-cut at 1/M_X', a position range. Only chat-only HANDOFF §4 says 'Yukawa in momentum'.
30. **Minor: #13 §1 tags its two causal cones "[D — compatibility theorem]".** That theorem's g is
    positive-definite and has no null cone; the cones need the Lorentzian dressing, which is
    open (OP3).
   **Audit (2026-10-22): depends on a convention or reading.** The tag sits on H = diag(g, g⁻¹), which the theorem gives; the untagged cone sentence presumes Lorentzian g (open, #11 §14 item 3), covered only by #13's header caveat. Whether that blanket caveat suffices is a tagging-convention call.
31. **Lead, not a confirmed error: "~10 orders" for quadratic photon dispersion (#1 §4).** #1 says
    quadratic effects at M_B ~ M_P sit "~10 orders below current sensitivity"; no script backs it.
    With a Fermi-LAT quadratic bound E_QG,2 ~ 1.3×10¹¹ GeV taken from model memory (†, Vasileiou
    et al. 2013), the gap is about 8 orders in the energy scale and about 16 in the size of the
    effect. Verify the bound before acting. Check: `review/wiki-build-checks/quadratic_gap.py`.
   **Audit (2026-10-22): depends on a convention or reading.** Bound verified [S]: Fermi-LAT E_QG,2 > 1.3×10¹¹ GeV. '~10' holds only loosely, counting orders in the energy scale (how Lorentz-violation limits are quoted; #1's 'Planck-scale dispersion' parallels it): 8.0–8.6, or 7.3–7.9 with #1's reduced M_P. Counting the effect's size (delay, ξ), as 'effects below sensitivity' suggests: 14.5–17, so wrong. 'Consistent' survives.
32. **Lead, from model memory (†): CMB-S4's status.** #11 names CMB-S4 as the probe for row 10;
    the project may have lost its US funding in 2025. Unchecked; an item for the † battery
    (OP10), not a source error.
   **Audit (2026-10-22): unclear (rests on model memory).** #11 §13 row 10 does name CMB-S4 ('Knob-bounded; CMB-S4 probes'). The funding-loss lead is model memory and no repository file addresses CMB-S4's status; the flag itself calls it a lead, not a source error.
33. **`verify/soliton_obituary.py` claims more coverage than it has.** Its docstring says it
    recomputes "every number that review/round3-adjudication.md and the §12 obituary … quote",
    and its closing line prints "every number the round-3 record quotes reproduces". The
    method-verification writer found it does not check the referee's numbers in rulings 3 and
    4, ruling 6's figure, or the surviving benchmark arithmetic (flux, densities, σ_T/M). The
    wiki describes what the script checks, not what it claims. A gate's self-description is
    part of the calibration Paul relies on.
   **Audit (2026-10-22): confirmed by 1 independent check.** Wrong as written. The adjudication quotes six computed figures for the candidate that the script never recomputes: the referee's KZ and Boltzmann ranges, ruling 6's ≳20–30 MeV, α_m≈34, ε~1e-7–1e-6 and '×1.6'. Only reading 'quote' as 'recomputed' rescues the claim, and that is circular. §12's '[V]' claim is accurate. The flag's flux/densities/σ_T/M item has no quoted number.
34. **Minor: the same script calls its constants "PDG and Planck 2018 values"** without the
    caveat its predecessor `knot_numbers.py` carried (constants from model memory, except the
    N_eff bound). The values are typed in, not retrieved.
   **Audit (2026-10-22): confirmed by 1 independent check.** soliton_obituary.py says 'Reference constants: PDG and Planck 2018 values'; knot_numbers.py (git 96f58da) said they 'are from model memory except the N_eff bound (Planck 2018 VI, live-checked)'. The constants are hard-coded; the caveat was dropped.
35. **Minor pointer: `review/round3-preregistration.md` line 5** cites HANDOFF §6 for the 2-for-2
    pre-registration record; it is in HANDOFF §5.
   **Audit (2026-10-22): confirmed by 1 independent check.** round3-preregistration.md line 5 cites HANDOFF §6 for rounds 1–2 being pre-registered and scoring 2 for 2. HANDOFF §6 never mentions pre-registration; the 2-for-2 record is §5, line 83.
36. **Minor pointer: "66.58 vs 63.72" placed in #11 §2.** `verify/battery.py`'s docstring and
    #11 §7.2 say the figures are in #11 §2, which does not print them; they are in HANDOFF §5.
   **Audit (2026-10-22): confirmed by 1 independent check.** battery.py's docstring says #11 §2 quotes '66.58 vs 63.72; rms 3.29', and #11 §7.2 cites 'the 66.58-vs-63.72 test of §2'. §2 prints only 'rms residual 3.29'; the pair appears in HANDOFF §5 and §7.2 itself.
37. **`README.md` still describes the program as explaining "missing magnetic monopoles".**
    HANDOFF §2 and #11 §11.1 list conjugate monopoles as the explanation of non-detection as
    dead (wrong duality; inflation suffices).
   **Audit (2026-10-22): confirmed by 1 independent check.** README.md reads 'Physics hypothesis explaining dark matter and missing magnetic monopoles'. HANDOFF §2 lists conjugate monopoles as the explanation of non-detection under Dead, and #11 §11.1 says 'As an explanation of the null result: dead'.
38. **Root `CLAUDE.md`: two stale details.** "Since the handoff" says "#11 is now v2.1" (the file
    is v2.2, as a later bullet says), and its Layout names two of the six scripts
    `scripts/check.sh` runs (the four toy scripts are missing). Its Layout and the
    `scripts/check.sh` header also say arbitration scripts go in `verify/` and the gate; the
    round-3 and round-4 arbitration scripts are in `review/` and are not run.
   **Audit (2026-10-22): confirmed by 1 independent check.** CLAUDE.md line 41 says '#11 is now v2.1' (file is v2.2; line 46 says v2.2). Layout line 27 names two of check.sh's six scripts. CLAUDE.md and check.sh say arbitration scripts go in verify/; rounds 3–4's sit unrun in review/.
39. **Two actions of ρ on the spin-2 sector, unreconciled (#11 §6 vs §7.3).** #8 §3 and #11 §7.5
    say the massless graviton is reciprocity-even and X reciprocity-odd. That holds under the
    action the documents state for the spin-2 sector, the frame exchange g ↔ f (#8 §1, #11 §7.3,
    #1 v0.6, #9 §5), which the palindrome also needs. Under #11 §6's ρ: Z → −Z⁻¹, the
    linearization at the fixed point Z = i is −(x + ih) for every d: the metric fluctuation h
    flips sign together with X. The documents assert both actions and do not show how one
    becomes the other for the massless mode. Check: `review/wiki-build-checks/rho_parity.py`.
   **Audit (2026-10-22): depends on a convention or reading (both of 2 checks).** Right under the action the documents state for the spin-2 sector, frame exchange (#8 §1, #11 §7.3, #1 v0.6, #9 §5), which the palindrome also needs. Wrong under #11 §6's Möbius map if the graviton is δIm Z: all Z fluctuations are odd there. X is odd either way. (The flag first said the documents do not state which action applies; the audit found they state both, and the flag was reworded to say so.)
40. **The naive toy potential is unbounded even at frozen H (root `CLAUDE.md`, round-4 lesson).**
    CLAUDE.md says round 4 "found a potential that was bounded only at frozen H". At the gated
    couplings λ = μ = 1 with H = 1 fixed, V = −4μ + 4μu² + (λ − 4μ)t², whose frozen-H Hessian
    has the eigenvalue −6; V falls to −30004 at t = 100. It is bounded at frozen H only on the
    circle K(φ) or for λ ≥ 4μ. Check: `review/wiki-build-checks/frozen_h_naive.py`.
   **Audit (2026-10-22): depends on a convention or reading (both of 2 checks).** Flag's mathematics holds: with only H frozen (K free on its hyperboloid, as §2 defines), the naive potential is unbounded below at the gated λ=μ=1, and K_ref is a frozen-H saddle (Hessian eigenvalue −6). The sentence holds only under the documents' 'frozen-H reduction', which also confines K to K(φ), or for λ ≥ 4μ.
41. **Minor overclaim (toy note §6).** It lists the complex model's "restoration under
    quantization" as "Shown (each by executed code)". The result rests on §4's analytic
    argument; `verify/toy_gw.py` checks only its premise.
   **Audit (2026-10-22): confirmed by 1 independent check.** §6 lists the complex model's restoration under "Shown (each by executed code)", but no script computes any quantum quantity of the complex model. toy_gw.py gates only the exact U(1)^N×U(1)^N symmetry and the classical vacua. The worklog itself tags the result [D] "by an exact argument", and no document supports a looser reading. The conclusion stands; the label overclaims.
42. **A revision recorded as applied that was not (round-4 adjudication, toy worklog).** Both say
    every accepted revision was applied, but toy note v2 §4 says the Langmann–Szabo–Zarembo
    comparison (revision 4) was "not carried out".
   **Audit (2026-10-22): confirmed by 1 independent check.** Revision 4 asks v2 to 'compare with Langmann–Szabo–Zarembo'. v2 §4 calls their exact solution 'the natural independent check' and says 'We have not carried it out.' Yet the adjudication heading and the worklog record every revision as applied. A looser reading (LSZ 'Accepted, as citations and reframing') fails: revision 6 covers the citation separately, and v2 reports no comparison.

43. **The thawing corridor lies in the CPL quadrant that reads as a phantom crossing, and no document
    says so (#11 §10; #1 §7 item 2; #9 §8).** On the corridor wₐ = −1.5(1 + w₀),
    w₀ + wₐ + 1 = −(1 + w₀)/2, which is negative for every w₀ > −1. Every corridor point therefore
    has w₀ > −1 and w₀ + wₐ < −1, the quadrant in which a CPL fit w(a) = w₀ + wₐ(1 − a) passes
    below −1 in the past. That is the quadrant of DESI DR2's fits ([21S]). #11 §10 states the
    corridor and DR2's crossing in one paragraph without relating them. #1 §7 item 2 compares
    signs only ("the sign pattern DESI reports").
    The quadrant comes from the straight line, not from the field. Numerically integrated
    V₀[1 + cos(τ/f)] fields that never fall below −1 (36 histories in one audit, 88 in the other)
    give CPL fits in the same quadrant under every fitting convention tried, with
    −wₐ/(1 + w₀) from about 1.4 to 2.4, and up to 3.9 when Ω_m is fitted without a CMB anchor.
    What separates the corridor from DR2 is the slope, which sets where the line crosses −1.
    The corridor's line crosses at z = 2 for every w₀; DR2's fits cross at z ≈ 0.35–0.50,
    with −wₐ/(1 + w₀) ≈ 3.0–3.8 (DR2 Table 5, fetched [S] by one auditor). A rough Gaussian
    approximation built from DR2's quoted pivot values puts the corridor line outside DR2's 95%
    region for DESI+CMB and for DESI+CMB+DESY5. The pressure #11 §10 and the root `CLAUDE.md`
    describe therefore stands. It rests on the crossing redshift (DR2 calls the preference
    "rather independent of parametrization choices"), not on the quadrant, which a field
    that never crosses can also occupy. Checks: `review/wiki-build-checks/corridor/`
    (`corridor_algebra.py`, `hilltop_cpl.py`, `dr2_comparison.py`, `dr2_asym_check.py`; and
    `c1_symbolic.py`–`c5_convexity.py` with `cosmo.py`).
   **Audit (2026-10-22): confirmed by 2 independent checks (one steelmanning the documents, one recomputing from scratch).** Both found the algebra right and the observation absent from every document. Both found the quadrant shared with the never-phantom field's own fits. The steelman adds that the corridor's slope, not its quadrant, keeps it away from DR2's crossing; #11 §10's defence is consistent with this.

44. **Minor, not yet audited: "Without the gauge invariance" (#6 §2).** `notes/x-classification.md`
    line 21: "Without the gauge invariance, no ghost-free two-derivative kinetic term for a
    Lorentz-covariant symmetric tensor exists … [T — standard]". Read literally, the full
    linearized diffeomorphism invariance is not needed: a kinetic term invariant only under the
    transverse diffeomorphisms (∂^μξ_μ = 0) plus Weyl rescalings, as in linearized unimodular
    gravity, is ghost-free (van der Bij, van Dam and Ng 1982 †; Álvarez, Blas, Garriga and
    Verdaguer 2006 †). That is still a gauge symmetry, so the program's conclusion, that X must be
    gauged, is unaffected; only "the gauge invariance" overstates. Raised by the verifier of
    `wiki/gravity/spin-2-fields/signature-obstruction.md`, which states the exception; the
    references are from model memory.
   **Audit (2026-10-22): not yet audited.** Raised after the flag audit; it has had one check (the page verifier's sympy check that the transverse-diffeomorphism-plus-Weyl term is not invariant under the full linearized diffeomorphisms), not two independent refuters.

## Found by the closed-universe investigation (2026-10-27)

*Raised by the analyses of `notes/closed-universe.md`. Each was then checked by two fresh-context
verifiers, one re-deriving and one recomputing or re-reading the sources. The audit lines give their
verdicts. Arithmetic is checked in `verify/closed_universe.py`. The analyses, verdicts and scripts
are in `review/closed-universe/`.*

45. **The 93.8% figure and its citations (#1 §7 item 3; #11 §10).** #1 says quintessence fits
    "with a potential possessing a negative minimum find a 93.8% preference for a future transition
    to anti-de Sitter space with eventual cosmological collapse" (Gialamas et al. 2025,
    arXiv:2506.21542, #11's [19]). That paper fits a Higgs-like quartic V₀ + m²φ²/2 + λφ⁴/4 in a flat
    universe with the sign of the vacuum energy left free. The 93.8% is the posterior probability
    that the vacuum energy is negative: 12.2% for a future transition plus 81.6% for a vacuum already
    negative today. "Future transition … collapse" is the paper's own abstract wording; the
    description of the fitted potential is not. #11 §10 cites [19S, 20S, 21S] for "high posterior
    preference for a future anti-de Sitter transition and collapse in negative-minimum quintessence
    fits". Only [19] supports the clause: [20] (Ureña-López et al., arXiv:2503.20178) fits
    V₀[1 + cos] with null spatial curvature and mentions no anti-de Sitter phase or collapse. Neither
    paper bears on the program's V ≥ 0 potential, whose closed future is a positive-energy recollapse
    (flag 27 addendum). Wiki pages quoting the figure: `conjugate-bounce`, `fate-of-expansion`,
    `quintessence`, `potential-sign`, `lab-notebook`.
   **Audit (2026-10-27): confirmed by 2 independent checks of the sources' TeX, one partly.** Both
   confirm the misdescribed model and the 12.2% + 81.6% split. The second holds that the
   "future transition … collapse" wording is the abstract's own, which leaves the model description
   and the compound citation as the errors.
46. **Closure moves the over-constraint (#11 §10; #1 §7 item 4).** Both say (w₀, wₐ, t_turn)
    depend on (f, τᵢ) alone: "three measurements, two parameters". With V ≥ 0 a turnaround exists
    only in a closed universe (flag 27 addendum). There t_turn = (π/2)(Ω_m + Ω_d)|Ω_k|^{−3/2}/H₀,
    which at fixed (w₀, wₐ) scales as |Ω_k|^{−3/2}, so Ω_k is a third input. Ω_k can be measured, so
    the over-constraint moves to (f, τᵢ, Ω_k) rather than vanishing. But the data bound t_turn only
    from below (t_turn > 5×10⁵ Gyr given closure), so the turnaround time can never test the count. `notes/closed-universe.md` §2. Check: `verify/closed_universe.py` §B, §C.
   **Audit (2026-10-27): confirmed by 2 independent checks.** One adds that the over-constraint
   relocates rather than fails, the wording used here.
47. **"The Fourier transform implements it unitarily" needs a scope if closure is adopted (#11 §3).**
    The sentence is true on ℝ^d, which #11's flat cosmology assumes. On a closed position space (S³,
    or a torus) position has a continuous spectrum and momentum a discrete one, so no unitary map
    exchanges them. Locally the flat statement holds to relative order (σ/R)². Wiki pages repeat
    the sentence unscoped, among them `fourier-transform`, `born-reciprocity`,
    `spontaneous-symmetry-breaking` and `p3-reciprocity`. `notes/closed-universe.md` §5.
   **Audit (2026-10-27): depends on a convention or reading (1 upheld as a scope restriction, 1
   partly upheld).** Not an error under the record's flat assumption; an error once k = +1.
48. **A closed universe does not close momentum space (#1 §6 table and §9 row 10; #11 §10 and §13
    row 10).** The dictionary reads "closed dual space ⇒ negative ΔN_eff", and row 10 lists
    "closed dual curvature ⇒ negative ΔN_eff". Under the slaved block g̃ = g⁻¹
    (`notes/geometric-core.md` Corollary 3) the momentum fibre's metric is the same at every
    p, for any X. The fibre is therefore flat (k̃ = 0), and k = +1 does not induce k̃ = +1. The
    effect needs a separate postulate of a curved, compact momentum space, which no document states;
    `wiki/predictions/early-universe-step.md` already notes that k̃ is undefined in #1. A symmetric
    reading, k̃ = k, survives N_eff, BBN and the observed momentum range only for a Born length below
    1.3 μm, and never together with standard inflation. `notes/closed-universe.md` §4.
    Check: `verify/closed_universe.py` §E.
   **Audit (2026-10-27): confirmed as a tension by 2 independent checks.** One notes that the record
   keeps k̃ as an optional knob rather than asserting a closed dual space, so the gap is the
   unstated postulate.
49. **The dual Einstein–Hilbert term is not derived (#1 §3 and §6; #11 §10 and §14).** #1 §6's
    minisuperspace equation, tagged [D], uses a dual Einstein–Hilbert term (in ã and its derivative,
    with its own mass M̃). #1 §3 reduces S_H only for the g-block and tags it "[D, schematic]"; no
    document derives the dual term from S_H. #11 §10's "the dual Einstein term is an a⁻⁶ step in
    G_eff" and row 10's a⁻⁶ step rest on it, and #11 §14 item 1 lists only the wedge-sector reduction
    as open. Until the term is derived, the a⁻⁶ step and every bound on the dual frame test a
    postulate. `notes/closed-universe.md` §7.
   **Audit (2026-10-27): partly upheld by 2 independent checks.** Both confirm that no derivation
   exists. Both note that √|H| = 1 holds if |H| is the full 2d-dimensional determinant (det H = 1,
   #11 §5), which the record does not say.
50. **The closed turnaround's conditions and prior art (round-5 R11; diameter note §6, "At the
    turnaround [D]").** "A closed universe can turn around with V ≥ 0" is true. It needs
    a_max ≥ Ω_m/|Ω_k| and, at H = 0, ρ_m + 2ρ_r + 4K − 2V ≥ 0, where K is τ's kinetic energy density
    (a maximum of a needs ä ≤ 0). The mechanism, recollapse of a closed universe with oscillating
    quintessence, is published (Barrow 1987 †; Tipler et al., gr-qc/0003082 [S], retrieved by a
    verifier). The diameter note states it inside a paragraph tagged [D] where [T] applies.
    `notes/closed-universe.md` §2. Check: `verify/closed_universe.py` §B.
   **Audit (2026-10-27): partly upheld by 2 independent checks.** Both find the statement true and
   the two conditions correct, so an omission rather than an error. The source check upholds the
   citation gap.
51. **β₁ > 0 is required and never stated (diameter note §8.2; round-5 R1).** On the palindromic
    zero-vacuum branch, the aligned branch y(ρ) is bounded for β₁ = 0. For β₁ < 0 the hot branch
    ends at a broken vacuum with negative Λ_g and violates the Higuchi bound. The record says only
    when broken vacua exist. `notes/closed-universe.md` §6.
   **Audit (2026-10-27): confirmed by 2 independent checks** (a repository-wide search finds no
   statement of β₁ > 0).
52. **#11 §10 omits that G_eff doubles for H ≫ M_X.** "§7.3 guarantees the wedge sector contributes
    nothing that competes with τ" holds for the dark-energy density. But on the branch
    the effective Planck mass rises from M_g² to 2M_g² as the universe cools through H ~ M_X, so
    G_eff = 2G_N early, with the halfway point at T ≈ 1.55–1.58 TeV for the smallest allowed M_X. No
    document states the step. The guarantee itself comes from the exact (1 − y)⁴/y relation on the
    branch, not from §7.3's aligned-point identity alone. `notes/closed-universe.md` §6.
   **Audit (2026-10-27): confirmed by 2 independent checks, as an omission.**
53. **"Trivially satisfied by a heavy X": the conclusion holds, the reasoning does not (#14 §1;
    `review/v3-worklog.md` R7; quoted on `wiki/gravity/spin-2-fields/bimetric-cosmology.md`).** The
    fixed-mass Higuchi argument fails once 2(H² + k/a²) > M_X², at TeV temperatures for the smallest
    M_X, and during inflation unless M_X > √2·H_inf. The bound still holds through the dressed mass:
    m_FP²(y) − 2(H² + k/a²) = −yρ_y/(3M_g²) > 0 on the β₁ > 0 branch. The live problem in that regime
    is a different one: Könnig's scalar gradient instability for w > −1/2 above about 1.3 TeV, which
    equal Planck masses do not escape. `notes/closed-universe.md` §6.
   **Audit (2026-10-27): confirmed by 1 independent check, partly by 1** (the conclusion stands).
54. **The τ potential's origin is uncited in #1 and #11.** V₀[1 + cos(τ/f)] is the
    pseudo-Nambu–Goldstone potential of Frieman, Hill, Stebbins and Waga 1995 (astro-ph/9505060,
    eq. 6, retrieved [S] by a verifier). The wiki already credits it with † (`quintessence`,
    `axion-like-fields`, `references`), which can become [S].
   **Audit (2026-10-27): upheld for #1 and #11 by 1 check; not upheld for the wiki.**

## Found by the momentum-gravity investigation (2026-10-27)

*Raised while answering Paul's question whether the velocity-clumping obituary is premature
(`notes/velocity-gated-gravity.md`, `notes/gate-mechanism.md`). The audit lines say who found and
who checked each. Arithmetic is checked in `verify/gate_mechanism.py` (55) and
`verify/velocity_gated_gravity.py` (56–58). The analyses, verdicts and scripts are in
`review/momentum-gravity/`.*

55. **The gate's mechanism is not derived (high; #11 §8: "[D — mechanism; shape [O]]").** #11 §7 builds
    X as one massive spin-2 field on spacetime. Every on-shell χ–χ–X vertex then depends only on
    the transfer t, so exchanging X gives an amplitude that depends on the incoming relative
    momentum k only as a polynomial of degree at most two in k², with velocity scale c: 2.4×10⁻⁷
    at 120 km/s, where the gate is 0.61. #6 §4's fiber overlap, written out in the two natural ways
    (a reconstruction: the record defines no overlap), is either an ordinary x-local potential of
    range ħ/μ ≈ 10 pm with power-law tails, or a pair-channel interaction that gives the gate but
    contains no X. The record constructs neither, and its section condition
    makes X independent of the fiber coordinates. Suggested tags: [P] for the gate F(k²/μ²) and μ,
    as #1 §3 (v0.1) had them; [O] for the mechanism; tree-level X exchange excluded [D][V]. §14
    item 4 asks only about the shape and presupposes an X propagator on the fibers that §7 does not
    have. Text that depends on the tag: #11's technical abstract, §8 (plain-language passage and
    tag), §12's χ row, §13 rows 1–3, §15; #6 §4; #5 §E; #8 §5 ("mechanism found"); HANDOFF §2 and §3
    (#5 "finds the gate's mechanism"); the wiki's gate-mechanism, gate-shape and dual-stress pages. It
    also opens whether row 3's island discriminant survives.
    `notes/gate-mechanism.md`. The velocity-clumping obituary is unaffected.
   **Audit (2026-10-27): confirmed by 2 independent derivations,** the second blind and
   pre-registered. The run-3 theory verifier raised it; a blind run-4 derivation reached the same
   verdict and added the two readings of the fiber overlap.
   **Ruling (2026-10-28): deferred by Paul.** #11 and the documents that depend on the tag stay as
   they are.
56. **#13 §2 against #13 §5 on gravitating pairs (low).** §2 says a black-hole merger "operates
    at F ~ c̃ by construction", using the gravitational force between the holes; §5 identifies dual rest with free
    fall. Merging black holes are in free fall, so under §5 their dual-kinematic correction is zero.
    For the Sun and Earth the two readings give (1/2)(F/c̃)² = 4.3×10⁻⁴⁴ and 0; both are negligible,
    but the paper gives two answers. `notes/velocity-gated-gravity.md` §2.
   **Audit (2026-10-27): raised by 1 agent (the run-3 theory verifier), upheld by the final
   critic.**
57. **The diameter note's Vainshtein radius uses the formula for a massless mode (low;
    `papers/phase-space-diameter.md` §8.2; `verify/phase_space_diameter.py:383–384`).** The check
    uses r_V³ = 2r_S λ², which is Enander and Mörtsell's eq. 43 and assumes one mode mass m₁ = 0. In
    the program's palindromic vacuum that would make X massless. Their eqs. 40–41, which apply,
    give 1.5–3.8×10⁻¹² m for 1 kg at a 50 μm range; under eq. 41 the check's rounding to 10⁻¹² m
    would fail. The conclusion, that laboratory masses are unscreened, holds. If this branch screens
    at all, the screened windows for λ_X would open at roughly 0.3–9 pc and close at Enander and
    Mörtsell's 4.4 kpc, the edge of their linear-theory lensing window [T][S]. Whether it screens is
    open. `notes/velocity-gated-gravity.md` §10.
   **Audit (2026-10-27): the source equations were read twice [S]:** by the run-3 critic-numbers
   verifier, and by the drafting session (its fetch is in the session transcript, not the record).
   The final critic adopted the verifier's ruling without rechecking them.
58. **Calc note #2's narrow-gate criterion (low; next to flag 19).** 3a writes the threshold as
    g·n_gate ≥ m·min(σ, v*)². Its substitution σ → v* is the threshold of a cold stream that already
    exists, not of a smooth halo. Linearized, the halo's dispersion stays: g·n·Λ_g ≥ m·σ². In the
    Milky Way 3a's form overstates the shortfall about 3× (2.9×10⁻³¹ against 8.7×10⁻³¹), the
    non-conservative direction for the obituary; in the dwarf core and the cluster it errs the
    other way. The verdict (10²⁸–10³¹ short) is unchanged. `notes/velocity-gated-gravity.md` §4.
   **Audit (2026-10-27): confirmed by 2 independent checks** (the run-2 clumping verifiers); both
   found the analysis's statement of the direction at the Milky Way wrong.

The executed checks referred to above are in `review/wiki-build-checks/` with their outputs, except
flags 27 (addendum) and 45–54, whose arithmetic is in `verify/closed_universe.py`, and flags 55–58,
whose arithmetic is in `verify/gate_mechanism.py` and `verify/velocity_gated_gravity.py`.
