# Broken-Born Program — Handoff to Claude Code

**Purpose of this document.** Everything a fresh Claude Code session needs to continue this project. Read this first; the artifacts listed in §3 travel with it. It is self-sufficient — nothing essential lives only in the originating chat session or in claude.ai memory. (A running ledger also exists at memory path `/areas/conjugate-matter-hypothesis.md` on claude.ai surfaces; if that memory store is visible to you, it corroborates but adds nothing critical beyond this document.)

---

## 1. What this project is

- **Project:** "Broken-Born program" (BBT) — a speculative physics research program developed September–October 2026.
- **Hard core:** Born reciprocity — the (x,p) → (p,−x) symmetry of quantum kinematics — taken as exact and spontaneously broken, with only the symplectic form ω rigid (ℏ-rigidity) and the neutral metric η emergent as the order parameter.
- **Participants:** Paul (P.R.) — conjecture, direction, veto; Claude — derivations, counterexamples, drafting, verification. Attribution in all papers follows this split.
- **Honest status:** a Lakatosian research program, not a theory. Three blind AI reviews returned verdict B ("flawed but salvageable"). Zero fabricated citations across all checks. The founding intuition (dark matter clumping in momentum space) was falsified by the program's own calculations; the structural core survived four consecutive consistency tests by being forced onto unique consistent structures each time.

## 2. Scientific state (one screen)

**Alive (derived, machine-verified where marked ✓):**
- Compatibility theorem: ω,η both rigid ⇒ H = diag(g,g⁻¹), det H = 1, momentum metric slaved g̃ = g⁻¹ ✓
- P2′ correction: strict rigidity trivializes the theory (nontriviality theorem); η must be emergent
- Modular field Z = X + iY on Siegel domain Sp(2d,R)/U(d); Im Z = metric, Re Z = X = momentum graviton; reciprocity = Z → −1/Z; a·ã = 1 is the |Z|=1 locus; dark energy τ = Maslov phase of the Shilov boundary Λ(4) ✓ (parametrization identities)
- X is forced massive: shift symmetry ⇒ never auxiliary; δX = ∂λ ⇒ second graviton; massless excluded (Boulanger–Damour–Gualtieri–Henneaux no-go); mass via Higgsed dual diffeomorphisms. Geometric sector = interchange-symmetric (palindromic βₙ = β₄₋ₙ) Hassan–Rosen bimetric, second frame confined to compact Λ(4)
- Palindrome/Λ theorem: V(1) = 2T exactly ⇒ flat aligned vacuum forces wedge-sector vacuum energy = 0 ✓ (integer identity [2,8,6] = 2·[1,4,3]). Novelty DOWNGRADED after literature check: the partially-massless (PM) bimetric point (arXiv:1609.09515) is g↔f symmetric and sits inside the palindromic branch; Hossenfelder arXiv:0807.2838 has a different exchange-symmetric cancellation. Detailed comparison still owed.
- Metric-tier Higgs potentials fail Fierz–Pauli (m²Tr h², no −(Tr h)² ✓; Tr(g²)+Tr(g⁻²) outside HR span ✓); frame-tier (vielbein wedge, Hinterbichler–Rosen class) passes — "passes iff formulated in first-order variables"
- Cosmology: duality dictionary w_eff = −w̃ (corrected from an earlier wrong −2−w̃); τ = hilltop/axion quintessence on the Maslov circle; thawing, w ≥ −1 always, eventual negative V ⇒ turnaround = conjugate bounce (one event, two descriptions). Consistent with DESI DR1/DR2 drift hints.
- Dark matter sector: gated self-interaction (gate = X-exchange; gate variable = incoming relative momentum; μ = χ's momentum-fiber width); knee at v*; knee-tail shape = particle-vs-wave "island discriminant" (new observable)
- Maximum force c̃ = c⁴/G as the momentum-space light speed (matches Gibbons–Schiller maximum-force conjecture up to the factor 4); dual special relativity (force boosts, force dilation, invariant length λ, Planck closure E = l_P·c⁴/G = E_Planck; dual inertial frames = free fall ⇒ equivalence principle as the dual relativity principle)
- Charge-lattice identification: DSZ pairing is symplectic; duality frame choice = Lagrangian polarization, same [[0,1],[−1,0]] generator as Born rotation and S-duality. Current best DM candidate: superheavy (~10¹³–10¹⁷ GeV) topological solitons (π₂ monopole-class) of a separate, strongly coupled dual gauge sector — "dark by sector separation," NOT magnetically charged under our photon.

**Dead (killed by own calculations — keep dead):**
- DM clumping in momentum space as dynamics: impossible for particle DM (criterion fails by 10²⁸–10³¹ ✓), fatal where mandatory on the wave island (ultra-faint dwarfs would be drained; Segue 1 intact), tunable elsewhere. Rows withdrawn permanently. Loophole: *topological* p-localization of individual solitons untouched.
- "Conjugate collapse powers our expansion": first version gave w = −2 (falsified); corrected dictionary removed the mechanism (dual dust ↦ dust).
- Conjugate monopoles as the *explanation* of our monopole non-detection (wrong duality; inflation suffices). As ontology they're alive (the soliton candidate).
- α_d ≈ 34 via Dirac quantization against our photon (round-1 reviewer's valid kill: can't use our DSZ lattice and then deny coupling to our photon). Restated in v2 as reciprocity-acts-as-modular-S on the coupling — explicitly the load-bearing conjecture; without it α_d is a free strong coupling.

**Open (the real frontier):**
1. Toy Lagrangian in which ρ is a genuine Noether symmetry, spontaneously broken, η the order parameter also selecting the electric sublattice (acceptance criterion #1; both reviewers independently named it)
2. Strong-coupling relic freeze-out at α_d ~ 34: Sommerfeld-enhanced annihilation vs. the √N topological-charge floor (Kibble leaves a net-charge residue annihilation cannot remove — chat-only idea, not yet in any paper; this bounds the relic abundance between Kibble ceiling and √N floor)
3. UV stability of sector separation / kinetic mixing (incl. the disputed gravity-induced mixing channel — see §6)
4. PM-point comparison and the Λ=0 novelty audit
5. First-principles wedge reduction from S_H; Lorentzian dressing of the Euclidean skeleton
6. Gate shape (X propagator on momentum fibers); dual-stress enhancement parametrics
7. Polarization-genesis (the Ω_DM:Ω_b = 5.4:1 ratio)
8. Dark-sector trilemma discrimination: particles vs X-condensate vs solitons

**External clock:** DESI DR3 (three-year data, expected late 2026). Kill conditions: robust constant w = −1 kills the τ sector; robust intrinsic w < −1 kills the framework outright; continued thawing drift keeps it alive (shared with other dynamical-DE models).

## 3. Artifact inventory (creation order)

| # | File | Status | What it is |
|---|------|--------|------------|
| 1 | `broken-born-theory.md` | v0.6 — superseded as reference, KEEP for audit trail | Original rigorous formalization (postulates, action, predictions table) plus addenda v0.2–v0.6 recording each debt payment and correction in sequence. The program's lab notebook. |
| 2 | `debt3a-stream-stability.md` | final | Calc note: Vlasov stability of the gated interaction; instability criterion; fails by 10²⁸–10³¹ at benchmark; classicality theorem (collective behavior ⇒ wave DM, m ≲ 0.1 meV) |
| 3 | `debt3b-wave-island.md` | final | Calc note: gated wave-kinetic condensation rate; island discriminant (exponential vs (v*/σ)⁴); Scenario A mandatory only in ultra-faint dwarfs; Scenario B tunable; misalignment fixes relic debt |
| 4 | `debt3c-ufd-endpoint.md` | final — closes Debt 3 (negative) | Calc note: Segue 1 endpoint; bosenova drain; Scenario A falsified; net theorem "velocity clumping nowhere mandatory" |
| 5 | `debt1a-geometric-core.md` | final | Calc note: compatibility theorem proof; P2→P2′ inconsistency + repair; Siegel/modular field identification; gate mechanism = X-exchange (pays Debt 2's mechanism) |
| 6 | `debt1a-ii-X-classification.md` | final | Calc note: shift symmetry; X = second graviton; massless/ungauged excluded; massive spin-2 via Higgsed dual diffs; "symplectic partner of the graviton is another graviton" |
| 7 | `debt1a-iii-tuning-test.md` | final | Calc note: {J,I[Z]} blocks computed; metric tier fails FP twice; frame tier (HR wedge class) passes; constrained-bimetric picture |
| 8 | `debt1a-iv-beta-coefficients.md` | final — closes Debt 1 (structural) | Calc note: palindrome βₙ = β₄₋ₙ; V(1) = 2T ⇒ Λ_wedge = 0; parameters 5→2; spectrum/parities |
| 9 | `broken-born-program-v1.md` | v1.0 — superseded by #11 | First paper-shaped consolidation; lay passage opening every section; tag system [D]/[T]/[P]/[O] |
| 10 | `angle-of-the-mirror.md` | final (journey article) | Pop-sci #1: narrative of the program including the deaths. Register note: "independent developer" (NOT "retired"). |
| 11 | `broken-born-checkpoint-v2.md` | **v2.0 — CURRENT REFERENCE for the full program** | Supersedes #1 and #9. Adds: methodological preface + 7-test machine-verification battery; charge-lattice §11; dark-sector trilemma §12; 25 references flagged † (memory — verify) vs [S] (live-searched); PM/Hossenfelder novelty downgrade; Appendix A supposition audit (11 items with fates) |
| 12 | `universes-other-half.md` | final (destination article) | Pop-sci #2: the framework presented as if confirmed; wave/spectrum analogy spine; includes magnetic identification, transparency argument, magnetic-quark/dual-superconductor section, dual SR, equivalence-principle unification. Register: serious-scientist plain language (see §7). |
| 13 | `conjugate-special-relativity.md` | final | Short paper: dual SR — force boosts, F-composition, force dilation, invariant-length shell, c̃ = c⁴/G, Planck closure, dual inertia = free fall; lay passages per section |
| 14 | `knot-dark-matter-standalone.md` | **v2 — CURRENT blind-review manuscript** | Self-contained max-symmetry DM proposal (superheavy dual-sector solitons) written for context-free review; v2 incorporates all valid round-1 findings. Round-2 findings NOT yet incorporated (pending v3 — list in §6). |
| 15 | `skeptic-review-console.html` | tool, current | Browser page that sends #14 verbatim to a fresh Claude (claude-sonnet-4-6, web search on, adversarial referee prompt) via the keyless artifact API route; auto-runs on load; copy button. Used for review rounds 1–2. |

Paul also holds two referee-report text files (round 1 and round 2 outputs of #15). Their verdicts and the adjudications are summarized in §6, which is sufficient if those files are absent.

**Recommended read order for a fresh session:** #11 → #14 → §6 of this handoff → calc notes (#2–#8) only as needed per task.

## 4. Results that exist ONLY in the chat (not in any artifact)

- **Phase-space diameter relation:** D_x · D_p = h · N^(1/3) per dimension (cosmic time–bandwidth theorem); the constant = the universe's photon count/entropy (~10⁹⁰, i.e. ~10³⁰ h per dimension); rectangle square (D_x = D_p in Planck units) exactly at the bounce; aspect ratio today ~10⁹² = a clock measuring distance from self-duality. Conjecture-tier; candidate for a future note.
- **√N topological floor** argument against the Sommerfeld catastrophe (open item #2 above).
- **Two gravitational charges:** ordinary stress-energy (sources massless graviton) vs dual stress "how energy is structured across momentum" (sources X); independent numbers; equivalence principle intact; whether invariant length λ and dual charge lock together = "dual equivalence principle" open question.
- **GR-vs-conjugate equation comparison:** slaved layer g̃ = g⁻¹ is algebraic (Einstein's equation does double duty); dual Newtonian limit = Yukawa in momentum = the gate; X-waves massive, 5 polarizations, frequency floor.
- **Momentum-space black holes:** velocity traps; our horizon read in dual ledger = max-force surface (hovering at horizon requires F → c⁴/G); dual Hawking quanta are position-space-huge. Conjecture tier; partially in #12.
- **Full adjudications of review rounds 1–2** with executed arbitration code (summarized in §6).

## 5. Verification protocol (the method — keep using it)

- **Tag every claim:** [D] derived here / [T] literature / [P] postulate / [O] open / [V] machine-verified. Citations: † = from model memory, verify before external use; [S] = live-searched this project.
- **Iron rule:** no arithmetic by eyeball. Any disputed or asserted number gets executed code with printed output. This is load-bearing — see §6.
- **Pre-registration:** before each review round, the expected verdict and weakest link were written down in advance (scored 2-for-2 on verdicts). Continue the practice; it calibrates trust.
- **7-test battery (all passed ✓):** T1 compatibility theorem both directions + proof block identities; T2 Siegel parametrization (I[Z]² = −1, H ≻ 0, det H = 1 off-vacuum); T3 {J₀,I[Z]} = [[S,A],[A,S]] blocks; T4 Tr(S²)/ε² → 4Tr(h²) ≠ FP form (66.58 vs 63.72 at seed 0); T5 palindrome V(1) = 2T as exact integers; T6 eₙ(1+δ) linear coefficients = C(3,n−1); T7 p₄ outside linear span of eₙ (lstsq rms ≈ 3.29). Code in Appendix A — re-run it first to confirm environment parity.

## 6. Review history and the measured failure mode

**Round 1** (fresh Sonnet, web search, blind): verdict **B / medium**. Valid hits, all incorporated in #14 v2: α_d-from-our-DSZ contradiction (restated as reciprocity-as-S conjecture); Preskill citation inverted (fixed); kinetic mixing unaddressed (postulate + ε ≲ 10⁻⁵ exclusion added); "knots" → π₂ monopole-class (renamed); GW backgrounds added; toy-Lagrangian demand adopted as acceptance criterion #1. Reviewer's own errors (machine-arbitrated): GeV→gram conversion off 10³; σ_T/M misread as σ_T (off ~10⁴³); insinuated the compatibility theorem might be false (it is machine-verified).

**Round 2** (same protocol, on v2): verdict **B near B/C / medium**; weakest link = the α_d derivation ("matrix coincidence ≠ physical identity" / "numerology"). Valid hits, **PENDING for v3 of #14**: SUSY-exactness burden for Montonen–Olive (either reciprocity supplies the rigidity or the dual sector is approximately SUSY); coupling-convention/running spread (α at transition scale drags 34 toward ~6–8; present α_d as free-but-strong, with reciprocity-as-S as the point-selecting hypothesis); extended Parker bound (Adams et al. 1993: F ≲ 10⁻¹⁶(m/10¹⁷ GeV) ⇒ our-U(1) exclusion is ~7 orders, not 5 — cite it); gravity-induced kinetic mixing dispute (reviewer claims a graviton-loop mixing mechanism needing no bi-charged matter; its formula was uncited and unverified — v2's "forbidden to all orders" is too strong either way; soften and resolve by literature); entropy-dilution caveat; name an explicit candidate group (dual SU(2)→U(1) suffices); bimetric cosmological-branch instability severity (mass hierarchy may evade — the analyses assume light second metric; early universe remains open; cite properly). Reviewer's own errors (machine-arbitrated): fed ρ_DM = 1.26×10⁻³ GeV/cm³ instead of 1.26×10⁻⁶ (the manuscript's own number) — with the right input the closure lands within 3%; conflated mean vs local density labels (manuscript's 1.3×10⁻²² mean and one-per-25-km³ local are both exactly right).

**Measured failure mode (both rounds + consistent):** fresh LLM referees are strong on structure, literature and logic; **unreliable on unaided arithmetic** (3 confident order-of-magnitude indictments, all reviewer unit errors, 0 surviving). Hence the iron rule. Claude Code's native execution removes this failure mode — that's the main reason the project is moving to you.

**Round 3 (incomplete):** an execution-verified blind audit agent (fresh context, shell+Python+web, 5-step protocol: citation verification incl. Preskill/extended-Parker; full numeric re-check in Python; independent sympy/numpy re-derivation of the compatibility theorem; conceptual audit incl. gravity-induced mixing literature; A/B/C verdict with four verified/failed/unverifiable lists) was dispatched 2026-10-17 and died partway on a rate limit after reporting "most citations and core numbers checked; several omitted-constraint literature checks remaining." **Suggested first task in Claude Code: re-run this audit natively** on #14 (v2 or, better, after cutting v3 with the §6 pending list) — you have the execution tools to do it yourself in a sandboxed subagent or directly.

## 7. Working conventions and user preferences

- Paul is an independent developer (Stanford Ginzton Lab research past in scanning acoustic microscopy — Fourier-domain physics, the origin of his intuition). **Not retired** — he corrected this explicitly; never describe him as retired.
- He cannot independently verify most of the technical physics and has asked for explicit legit-vs-hallucination calibration: keep the tier tags, keep machine-verifying, keep pre-registering, keep reporting negative results prominently. Honest obituaries are part of the deliverable.
- Work pattern: chunked tasks with state saved after each chunk; he triggers continuation with "go"; he may be away — save progress so any session can resume cold.
- Prose register for science writing: serious scientist explaining abstract material in plain language. NO anthropomorphizing ("nature plays favorites"), NO moralizing, NO detective-story reveals — he reads these as "glib AI." Wave/Fourier analogies (waveform vs spectrum) work for him personally; ball-rolling and dual-ledger/bookkeeping metaphors did not land.
- Papers follow the house pattern: every section opens with an italic plain-language passage, then the technical record with tags.
- Attribution line in papers: "conjecture and direction, P.R.; derivations, counterexamples, verification, drafting, Claude (Anthropic)." All †-flagged citations must be source-verified before anything goes external.
- Format preference (stored): simple bullets over prose paragraphs for working communication; make the call and recommend rather than asking questions he can't answer.

## 8. Ranked next-actions queue

1. **Cut v3 of `knot-dark-matter-standalone.md`** applying the §6 pending list (mechanical, ~1 session).
2. **Re-run the execution-verified blind audit** on v3 (protocol in §6; you have native execution + web).
3. **√N-floor freeze-out estimate** (open item #2) — resolves "Sommerfeld probably fatal" into a number; Preskill-style kinetic calculation; decides whether the soliton candidate's abundance window exists.
4. **Toy Lagrangian** (acceptance criterion #1) — the item both independent reviewers named as the gate to verdict A. Hardest; highest value. Start in 0+1 or 1+1 dimensions on the Siegel disk.
5. **PM-point comparison** (is reciprocity the origin of the partially-massless symmetry? does the Λ=0 identity survive convention-careful comparison with arXiv:1609.09515 / 0807.2838 / the Schmidt-May–von Strauss review's no-protecting-symmetry statement?).
6. Literature battery completion: every † reference in #11 and #13 source-checked; resolve the gravity-induced kinetic mixing question.
7. Optional write-ups: phase-space diameter relation note (§4); LaTeX/arXiv shaping only after 1–5.

## 9. Repo suggestion (optional)

```
broken-born/
  HANDOFF.md                  (this file; point CLAUDE.md at it)
  papers/     → #11, #13, #14 (+ future v3)
  popsci/     → #10, #12
  notes/      → #1–#8 (calc notes + original flagship with addenda)
  review/     → #15, round-1/round-2 referee reports, adjudications
  verify/     → Appendix A battery as battery.py; future arbitration scripts
```

## Appendix A — machine-verification battery (re-run first)

```python
import numpy as np
from math import comb
from itertools import combinations
np.random.seed(0)
d=4
Id=np.eye(d); Zr=np.zeros((d,d))
def randsym(s=1.0):
    m=np.random.randn(d,d)*s; return (m+m.T)/2
def posdef():
    a=np.random.randn(d,d); return a@a.T + d*np.eye(d)
omega=np.block([[Zr,Id],[-Id,Zr]])
eta=np.block([[Zr,Id],[Id,Zr]])
blk=lambda M,i,j: M[i*d:(i+1)*d, j*d:(j+1)*d]

# T1: compatibility theorem
g=posdef()
H=np.block([[g,Zr],[Zr,np.linalg.inv(g)]])
J=np.linalg.inv(eta)@H; Ic=np.linalg.inv(omega)@H
print("T1a diag(g,g^-1) satisfies both:", np.allclose(J@J,np.eye(2*d)) and np.allclose(Ic@Ic,-np.eye(2*d)))
A=posdef(); B=posdef(); C=np.random.randn(d,d)*0.3
H2=np.block([[A,C],[C.T,B]])
J2=np.linalg.inv(eta)@H2; I2=np.linalg.inv(omega)@H2
print("T1b generic violates:", (not np.allclose(J2@J2,np.eye(2*d))) or (not np.allclose(I2@I2,-np.eye(2*d))))
print("T1c proof blocks:", np.allclose(blk(J2@J2,1,0), A@C.T + C@A), np.allclose(blk(I2@I2,1,0), C@A - A@C.T))

# T2: Siegel parametrization
X=randsym(); Y=posdef(); Yi=np.linalg.inv(Y)
HZ=np.block([[Y+X@Yi@X, X@Yi],[Yi@X, Yi]])
IZ=np.linalg.inv(omega)@HZ
print("T2:", np.allclose(IZ@IZ,-np.eye(2*d)), np.allclose(HZ,HZ.T),
      np.isclose(np.linalg.det(HZ),1.0), bool(np.all(np.linalg.eigvalsh(HZ)>0)))

# T3: anticommutator blocks {J0,I[Z]} = [[S,A],[A,S]]
M=eta@IZ+IZ@eta
S=Y+X@Yi@X-Yi; Ac=X@Yi-Yi@X
print("T3:", all([np.allclose(blk(M,0,0),S), np.allclose(blk(M,0,1),Ac),
      np.allclose(blk(M,1,0),Ac), np.allclose(blk(M,1,1),S)]))

# T4: linearized potential is non-Fierz-Pauli
h=randsym(); x=randsym()
for eps in [1e-4, 1e-5]:
    Ye=Id+eps*h; Xe=eps*x; Yei=np.linalg.inv(Ye)
    Se=Ye+Xe@Yei@Xe-Yei
    print(f"T4 eps={eps}: {np.trace(Se@Se)/eps**2:.4f} vs 4Tr(h^2)={4*np.trace(h@h):.4f} vs FP={4*(np.trace(h@h)-np.trace(h)**2):.4f}")

# T5: palindrome V(1)=2T, exact integers
V1=[comb(4,0)+comb(4,4), comb(4,1)+comb(4,3), comb(4,2)]
T =[comb(3,3),           comb(3,0)+comb(3,2), comb(3,1)]
print("T5 V(1)-2T =",[V1[i]-2*T[i] for i in range(3)])

# T6: e_n linearization coefficients
delta=randsym(1e-6)
lam=np.linalg.eigvalsh(Id+delta)
def en(vals,n): return sum(np.prod(c) for c in combinations(vals,n)) if n>0 else 1.0
tr=np.trace(delta)
print("T6:", [round((en(lam,n)-comb(4,n))/tr,4) for n in range(5)], "expect [0,1,3,3,1]")

# T7: p4 outside linear span of e_n
rng=np.random.default_rng(1)
E=[];P=[]
for _ in range(300):
    s=rng.uniform(0.5,2.0,size=4)
    E.append([en(s,n) for n in range(5)]); P.append(np.sum(s**4))
E=np.array(E);P=np.array(P)
coef,res,rank,_=np.linalg.lstsq(E,P,rcond=None)
rms=np.sqrt(res[0]/len(P)) if len(res) else np.linalg.norm(E@coef-P)/np.sqrt(len(P))
print(f"T7 rms residual = {rms:.4f} (nonzero => outside span)")
```

Expected: T1–T3 all True; T4 converges to 4Tr(h²) and visibly ≠ FP; T5 = [0,0,0]; T6 = [0,1,3,3,1]; T7 rms ≈ 3.3.

---
*Handoff prepared 2026-10-19 from the originating claude.ai session. The audit-agent round (§6, round 3) was incomplete at handoff; treat its partial finding ("citations and core numbers check out so far") as unconfirmed until re-run.*
