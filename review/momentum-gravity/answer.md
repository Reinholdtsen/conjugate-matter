Round 3 is finished and checked. Two agents checked this answer against the scripts' printed outputs and the final critic's rulings, and their fixes are applied. A third did a blind second derivation of the gate question. Both answers stand.

## Answers

- **Would momentum gravity look like a perturbation of gravity that depends on two bodies' relative velocity?** No, not between ordinary bodies.
  - The program's momentum gravity X adds a short-range term: V = −(Gm₁m₂/r)(1 + (4/3)e^(−r/λ_X)). This holds in the program's aligned vacuum (background ratio u = 1), with λ_X < 37.7 μm provided the Sun and planets are not screened [V][S].
  - X is not velocity-gated at any range. Its relative-velocity dependence is the ordinary relativistic spin-2 factor: 1 + 2.4×10⁻⁷ at 120 km/s, against 1 + 3.2×10⁻⁷ for ordinary gravity [D, executed].
  - Two other readings of "momentum gravity" give corrections that depend on force, both negligible [D]:
    - #13's kinematics: (F/c̃)² ≈ 4×10⁻⁴⁴ for Sun–Earth, or zero if free fall is dual rest.
    - The Siegel reading (flag 39, open): about 3×10⁻²⁶.
  - A universal term gated on two bodies' relative velocity is excluded [D; data [S]; checked twice]:
    - |ε| < 8.7×10⁻⁹ for gate widths of 0.2–2100 km/s in the record's convention (ε = strength relative to gravity).
    - 3.5×10⁻¹¹ at the record's 120 km/s.
  - The program's one velocity gate is χ–χ scattering at contact range, not a change to the 1/r law.
- **Is the obituary premature?** No.
  - It tested the program's contact gate on all three branches [D, record]:
    - For particle χ, the collective pull falls short by 10²⁸–10³¹. The record's ungated wiki-build script reproduces this.
    - For wave χ whose gate also makes dwarf cores, clumping would be mandatory in ultra-faint dwarfs and would drain them. Observation rules that out.
    - With the coupling free, wave χ can still form streams. But their strength is tunable over ~10 orders, so they predict nothing.
  - So the obituary says clumping is nowhere *required*. It does not say clumping cannot happen.
  - Your long-range version is a different model, and the record has no field that could carry it.
  - At the record's gate width, observations allow ε ≲ 0.06–0.18, while clumping needs ε > 1.

## Your long-range version (χ only, gated in relative velocity)

- **Allowed strength at 120 km/s** [D; derived twice independently; a compressed DESI Lyman-α estimate, not a full likelihood]:
  - ε < 0.06 (matter) to 0.11 (gas) in the record's reading. There the gate acts on canonical momentum, the momentum in the record's equations, which here is not mass × velocity.
  - ε < 0.06–0.18 if the force is read as acting at fixed velocity.
  - In the record's reading the force lowers small-scale power. Older eBOSS data then prefer ε ≈ 0.05 strongly in formal terms (χ² falls from 26.3 to 1.9).
  - That is not evidence. Those data sit 4.9σ from Planck, and any suppression near that scale relieves the tension. The compression also assumes a ΛCDM spectrum shape, and DESI agrees with Planck.
  - Open [O]: whether the record's reading is the right classical limit for a long-range force. It separates physical from canonical velocities by up to 11.5×, and its linear theory breaks down above ε ≈ 2.2.
- **What clumping needs** [D]:
  - ε > 1 at every gate width. The allowed strength is therefore at least 6× too small (9× in the record's reading).
  - At least 4.24 wherever the dispersion exceeds the gate.
  - The local model's own thresholds are at least 28 (Milky Way) and 690 (clusters). Both lie beyond the model's validity, so treat them as indicative only.
- **Narrow gates (below 30 km/s), the corner I left open:**
  - **N-body** (29 runs; gate as wide as, or 2.5× wider than, the dispersion; record's reading) [D, executed; isolated cored halo]:
    - No velocity-selected clumps, streams or flows at ε = 1, 3 or 10 over 43 free-fall times, which is 0.1–0.6 Gyr in a dwarf.
    - The runs detect clumps holding 2% of the mass, but streams only from 5%.
  - **Observational estimates**, rerun by the final critic with corrected formulas [D; estimates, not likelihoods]:
    - ε ≈ 2 is excluded from 10 km/s up in both readings, by the reionization optical depth and dwarf densities.
    - ε ≈ 3 is excluded at 5–30 km/s in the fixed-velocity reading. The record's reading gives no number there, because its linear theory breaks down.
    - ε ≈ 1 is in tension above 20–30 km/s and disfavoured from 3–5 km/s up. The evidence is an optical depth 2.7σ high, dwarf densities ×2.3–2.8, small-scale Lyman-α, and Segue 1 heating if early clumps survive.
  - **Not computed:**
    - Gates below 3 km/s, where clumping would need ε of about 4 to 10, beyond the model's validity.
    - Gates narrower than the dispersion.
    - Instabilities slower than 43 free-fall times.
- **Cores:** making dwarf cores this way takes ε ≈ 3.6×10³¹ [D, three independent recomputations].
  - So the force can't do the job the gate was introduced for, and any strength would be a free parameter ("decorative").
  - The corner also needs a second gate scale, 4–40× below 120 km/s.
- **Theory** [D; citations [S]]:
  - For any finite spin, exchange makes the force *grow* with relative velocity. Spin 3500–5000 would raise it by order one at 120 km/s, but never switch it off.
  - Massless spin ≥ 3 is excluded (Weinberg 1964; Porrati 2008), and so are finitely many massive spin > 2 (Afkhami-Jeddi–Kundu–Tajdini 2019).
  - An infinite tower of spins would need cancellations of order 10^5421169. A medium gives dependence on velocity relative to the medium, not between the bodies.
  - One known framework has your shape: continuous-spin exchange (Schuster–Toro–Zhou 2023, eq. 129). The theory checker and I each read it in the paper.
    - The correction depends only on relative velocity and vanishes for bodies moving together.
    - But its switch-on velocity falls with distance, and it is worked out only for a scalar toy current.
    - It has no gravitational version, and the record has no such field.

## What changed since my interim answer

- **Lyman-α:** 0.03–0.3 becomes 0.06–0.11 (record's reading).
  - Run 2's model used a wrong force formula; both checkers found this independently.
  - The run-2 critic's 0.34 counted one term twice.
- **Thresholds:**
  - Milky Way: "28–161" becomes "at least 28, or none if the halo re-settles".
  - Clusters: "at least 152" becomes "at least 690".
  - All of these lie beyond the model's validity.
- **Sagittarius:** "1–3" becomes "of order 1 (0.2–2.5)". The 10% limit it rests on has no confidence level and is disputed.
- **Withdrawn: "gating χ–χ gravity itself is also excluded."**
  - Lensing against dynamics cannot see it, and χ could settle into a slower bound state.
  - It sits outside the record only because of the equivalence-principle postulate, and it is observationally untested.
- **Ordinary bodies:**
  - 3.5×10⁻¹¹, from Mars's perihelion. My "2×10⁻¹¹ from Mercury" used the other gate convention.
  - Below ~0.3 km/s, ε ~ 1 is excluded only qualitatively.
- **Vainshtein windows:** if this branch screens at all, they are roughly 0.3–9 pc up to 4.4 kpc.

## Pre-registrations (written before launch, kept out of agents' reach)

- **Round 3, right:**
  - The run-2 reading would be judged neither Hamiltonian nor Lagrangian.
  - The record and run-2 numbers reproduce.
  - A source correction: the BOSS limit is driven by the background expansion, which the gated model lacks, so it is not a bound here.
  - The ordinary-matter envelope stays below 10⁻⁸, and literature corrections stay under 3×.
  - The theory items.
  - No clumping in the N-body; stronger than predicted, none up to ε = 10.
- **Round 3, wrong:**
  - Lyman-α: I predicted 0.1–0.5 and got 0.057/0.106. I had anchored on the critic's unreviewed 0.34.
  - Sagittarius: I predicted 1–3 and got 0.2–2.5.
  - The corner: I predicted no robust exclusion, but ε ≈ 2–3 is excluded from 5–10 km/s up.
- **Round 3, missed:** continuous spin; the sign flip in the record's reading; flag 1.
- **Round 3, weakest link:** the compressed likelihood's shape was a real problem, and the N-body held up. The actual failures were formula errors in two linear models, which I did not name.
- **Gate derivation, right:** the verdict, the degree-2 polynomial with velocity scale c, the record building no fiber structure, and the [P]/[O] tag.
  - The weakest link I named, the polarization, held up: it is Lorentz-invariant.
- **Gate derivation, missed:** one reading of the fiber overlap is just an ordinary 10 pm potential.

## Candidate flags (for your ruling)

1. **#11 §8: the gate is a postulate, not derived.** High severity for the program, no effect on the obituary.
   - Two independent derivations agree, the second blind and pre-registered [D][V].
   - Exchanging §7's X cannot produce the gate, whatever the vertices. The pair's relative momentum enters only as a polynomial with velocity scale c: 2.4×10⁻⁷ at 120 km/s.
   - #6 §4's fiber overlap has two readings. One is an ordinary 10 pm potential with power-law tails and no gate. The other is a pair interaction that gives the gate but contains no X.
   - The record builds neither, and its section condition makes every field independent of the fiber coordinates.
   - Suggested tags: [P] for the gate and μ, and [O] for the mechanism.
   - This would reopen what HANDOFF records as #5 "paying Debt 2's mechanism".
   - It would also touch #11's abstract and §§8, 12, 13 (rows 1–3) and 15, #8 §5, and the wiki's gate-mechanism page.
   - Open: whether Debt 3's surviving island discriminant (the knee shape telling particle χ from wave χ) still holds.
2. **#13 §2 against §5 (low).** §2 says a merger "operates at F ~ c̃", but §5 makes free fall dual rest.
3. **Diameter note §8.2, Vainshtein radius (low).** The critic-numbers checker and I each read Enander–Mörtsell eqs. 38–43.
   - [verify/phase_space_diameter.py:383](verify/phase_space_diameter.py#L383) uses the formula that assumes one mode mass is zero. In the program's vacuum that would make X massless.
   - The applicable formulas give 1.5–3.8×10⁻¹² m for 1 kg. Under one of them the rounding check on line 384 fails.
   - The conclusion, that lab masses are unscreened, holds.
4. **Debt 3a's criterion when the gate is narrower than the dispersion (low; next to flag 19).**
   - Linearized, it reads g·n·Λ_g ≥ m·σ².
   - 3a's form overstates the Milky Way shortfall about 3×; the verdict is unchanged.

## Process

- **Round 3:** all seven agents finished, blind. The corner agent had used two flawed formulas; the final critic reran its estimates, the edges moved 1.5–3×, and the map stands.
- **Script locations:** the new numbers come from executed scripts in [mg/](/home/paul/.claude/projects/-home-paul-git-reinholdtsen-conjugate-matter/7156ee3a-6166-4b9e-84c4-fb9703a50211/mg/). None of these is gated yet. The 37.7 μm comes from the gated `verify/` script.
- **Repository:** no file was changed.

## Recommendation

- Keep the obituary.
- Rule on flag 1 first. It changes the program's dark-matter standing more than anything in your question did.
- On your "go":
  - Write calc notes on the long-range variant and on the gate mechanism.
  - Move their key scripts into `verify/` and wire them into `scripts/check.sh`.
  - Add the obituary's three-branch scope to its page.
  - File the flags.
- If "premature" rests on a specific observation, name it and I'll test it. Note that plain cold dark matter already predicts ~10¹⁴ fine velocity streams near the Sun [T][S]. The founding image predicted about ten broad ones, so only a stream like that would test it.
