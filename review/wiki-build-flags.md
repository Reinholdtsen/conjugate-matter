# Wiki build — suspected errors in the source documents

*Found by the fresh-context verifiers of the wiki depth pass (2026-10-21). The wiki quotes
every source faithfully and corrects none of these; each needs Paul's ruling. Where
arithmetic is involved, the verifier's executed check was in the session scratchpad and
is not part of `verify/`; a ruling that accepts a flag should add the check there.*

1. **Null-Lagrangian polarizations are not discrete for d ≥ 2.** `notes/debt1a-geometric-core.md`
   §B (line 27), echoed in #11 §5 and #9 §3: the ω-Lagrangian, η-null polarizations are
   "discrete — the 2^d coordinate-type splittings, GL(d)-rigid". For any subspace V ⊂ ℝ^d,
   V ⊕ V^⊥ (V in x, V^⊥ in p) is ω-Lagrangian and η-null, so they form continuous
   Grassmannian families Gr(k, d). The conclusion survives: det² (Maslov phase) is constant
   (±1) on each family, so no Maslov circle and no τ; the x-polarization is isolated.
   Found by the wave-1 verifier (postulates batch); scratch evidence
   `(session scratchpad) postulates/verifier_null_lagrangians.py` (d = 2, 3). Suggested wording:
   "no continuous family through the x-polarization; det² is constant, so no Maslov circle".
2. **"I is odd in K" (toy note §5, line 152).** I[W] = ∫(∫W)² ≥ 0 cannot be odd under
   K → −K; the gated values 0.4070 and 0.3600 show only that I is not invariant under it.
   Suggested wording: "I is not invariant under K → −K". ADJ4 F3 and toy note §2 use "a
   coupling odd in K" as a requirement, which is fine.
3. **The misalignment potential's zero set is larger than stated (#7 §2).** `notes/debt1a-iii-tuning-test.md`
   §1–§2 says {J₀, I[Z]} vanishes exactly on "X = 0 and Y = Y⁻¹". The blocks are A = [X, Y⁻¹] and
   S = Y + XY⁻¹X − Y⁻¹; with A = 0 (X, Y commuting) S = (Y² + X² − 1)Y⁻¹, so the zero set is
   {X, Y commute, X² + Y² = 1}, which contains points with X ≠ 0. At d = 1 it is the whole
   circle |Z| = 1 (the self-dual locus), not only Z = i. Consequence for the tuning test: at
   quadratic order x is a flat direction (consistent with battery T4's Tr(S²)/ε² → 4Tr(h²)).
   Found by the tuning verifier (wave 2). Needs a ruling: is the degeneracy along |Z| = 1
   intended, and does it affect the vacuum structure claims?
4. **Missing −h² in the expansion of S (#7 §2 item 2).** "S = 2h + x² + O(3)" should be
   S = 2h + x² − h² + O(3) (Y⁻¹ = 1 − h + h² − …). Executed checks by two agents:
   `(session scratchpad) tuning/s_expansion.py`, `(session scratchpad) spin2a/check_S_expansion.py`. The
   quadratic-order Fierz–Pauli test (T4) is unaffected (it uses only S ≈ 2h).
5. **M_X ∝ 2(β₁+β₂) should probably be M_X² (#11 §7.5, #9 §5 item 6).** Their source, #8 §3,
   writes "m_FP² ∝ β₁ + 2β₂ + β₃ = 2(β₁+β₂), i.e. M_X"; the β-combination fixes the squared
   Fierz–Pauli mass [T]. Flagged independently by three agents. Notation only.
6. **"By symmetry rather than tuning" overstates the vacuum-energy identity (#1 v0.6, #10).**
   The flatness condition V(1) = T is itself one condition on the βₙ, and #8 §3 counts T = 0 as
   removing a parameter. #8 §2's wording is the accurate one. #11 §7.3 says "by symmetry";
   worth checking it against this.
7. **"The unique consistent structure" (#11 §7.1)** drops #6 §3's qualifier "exactly one *known*
   consistent structure" for massive spin-2. Mild overstatement.
8. **#8 §3 "five-function freedom"**: the βₙ are constants (#7 §2), so "five-parameter".
9. **#11 ref [24][S] (arXiv:1609.09515)** has no authors and its title may be a description
   rather than the paper's title. Being [S], it falls outside the † battery (OP10).
10. **Smaller pointers and wording.**
    - #1 §1 P2 points to §5 for the dark-energy potential; it is in §3.
    - `notes/toy-lagrangian.md` lists "ρ sits inside a continuous U(1)" as unpredicted although
      its Predictions section anticipated the restored U(1) in 1+1.
    - `verify/toy_s5.py` part C still says "built from K"; v2 §5 says built from (H, K),
      SO(2)-covariant.
    - The round-4 referee's audit notes use "boost" for two different families (the squeezes
      diag(a, 1/a) and the hyperbolic boosts).
