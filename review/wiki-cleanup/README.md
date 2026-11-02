# The wiki clean-up, 2026-10-30 to 2026-11-01

Paul, 2026-10-30, on `wiki/summary.md`: "The tone sounds like an airing of dirty laundry. Can you tell why. This argument
between you and me has no place in this wiki. An executive summary also does not need to list corpses. And the answer to
'Is anything new' does not even list my core conjectures! What is up with that? Also, the executive summary is way too long.
Please clean things up. Go through the entire wiki and verify consistency."

The baseline is commit 6989941. Only `wiki/`, `scripts/check-wiki.py`, the root `CLAUDE.md`, `site/content/_index.md` and
this folder changed. The source documents keep their wording, including the narrative the wiki no longer tells.

## What was done

1. By hand: `wiki/summary.md`, 8,513 words before its Sources section, became one page of 792 (both by the gate's count);
   `wiki/_index.md`; the rule "State the claim, not the
   discussion" in `wiki/CLAUDE.md`. `wiki/status/graveyard.md` moved last among the registers (weight 10 → 70), the one
   change of a frontmatter weight.
2. Rewrite: 41 agents, 286 pages, following `BRIEF.md` and `SPECIAL.md` (`rewrite-result.json`).
3. Verification: 41 fresh agents compared each page with the baseline and made 243 repairs: 36 for evidence lost, 44 for
   distortion or addition, 88 for residual narrative, 59 for prose damage, 16 others (`verify-result.json`).
4. Consistency: 13 sweeps by topic across the whole wiki made 167 fixes against the sources. Each sweep's fixes then
   went to an auditor told to refute them, which corrected 14 (`consistency-result.json`).
5. `scripts/check-wiki.py` gained three checks: `status` (title, status line and register agree with a page's status), `voice`
   (wording that tells how a status came about) and `summary` (length, no dead or under-review pages, P.R.'s conjectures).

Machine comparison with the baseline: no page's title, status or provenance changed, and no folded status heading was lost.
Every new number was traced to a source or a `verify/` output. Pages no agent needed to edit were covered only by the sweeps'
searches and the machine checks.

The subagents used about 35 million tokens, and the verification pass hit the account's weekly limit on the way.

## Choices the record cannot settle

Each is P.R.'s. No page decides them, and pages state both sides where they matter.

- **"Kills outright" (row 4).** Does a robust intrinsic w < −1 kill the τ sector (#1 §7 item 1, #14 §5) or the whole framework
  (`HANDOFF.md` §2)? #11 §13 leaves the scope open.
- **"The empty set" or "measure zero".** #11 §11.1 and App. A item 5 attribute two wordings to P.R. for conjugate monopoles
  that exist and have no effect. The first says there is no such case, the second that such cases are negligible.
- **χ and the X-condensate as `alive`.** #11 §12 tags each candidate [O], and their pages have status `alive`, while the
  third candidate has status `conjecture`. Likewise App. A item 4 is "alive" with no [O].
- **A literature check of the conjectures.** The record holds none, and the † battery (OP10) only checks citations already made.
- **Row 8.** Should "Permanent null" carry a qualification for the shared-photon form, as flag 63 proposes for row 7?
- **Scope notes in the sources.** Round-3 Decision 3's "no candidate left to serve" against Decision 2's scope; the diameter
  note's §9 rows for the self-dual length against the root file's "under review".
- **The URL `/wiki/cosmology/scale-factor-duality/self-dual-length-obituary`** names a page that is under review. It stays, since
  moving it means fixing every inbound link.
- **Pending flags**, among them 55, 63, 6, 9, 11, 19, 23, 24, 27, 29 and 56 (`review/wiki-build-flags.md`).

## Conflicts in the sources that no flag covers

Pages quote each source as written. None changes a claim's status.

- #11 App. A item 5 says "open in both halves", then calls the ontology half "alive and consequence-bearing", as §11.1 does.
- #11 §11.4 says p-localization has been "open since v2.0"; §14 item 8 says v2.1 closed it and v2.4 reopened it, and still says "the §12 obituary".
- #11's v2.4 change note says "the v2.0 candidate that #14 never modeled"; §12's verdict says "The candidate it modeled".
- #11 §10's italic passage ("exactly the required drift") against its 'Under pressure' paragraph.
- #11 §4 "Only ω is rigid" beside "more structure than ω alone".
- #11 §8 writes one F for the amplitude's gate and the cross-section's; with #1's definitions, the same F needs F(x/2)² = F(x), which holds for the Gaussian and not for the rational forms.
- #11 §8's m_φ: #1 §5.1 makes it a heavy mediator, §8 says "delivered by X-exchange", and no document relates m_φ to M_X.
- #11 §9 (i) "forces m ≲ 0.1 meV" names no halo; #2 evaluates it for the Milky Way, and flag 19's audit prints 26 meV for Segue 1.
- #11 §9: "Results (i)–(iii) stand" beside Scenario A, on which (iii)'s "fatal" leg rests, under review.
- #11 §13 row 8 "Permanent null" against §11.4's shared-photon analogs (flag 63 covers rows 7 and 11 only).
- #11 §14 item 12 tags π₁ and π₂ [T] "with the maps behind them gated"; `notes/closed-universe.md` §8 tags π₁ [T][V], π₂ [T].
- #11 §7 confines the second frame to Λ(4); #8 and `notes/closed-universe.md` §6 treat f as dynamical.
- #11 §4 "ε ≲ 10⁻¹³" against the round-3 referee's reading of the cited figure as a floor.
- Round-3 Decision 1 says mixing is zero if hidden charge conjugation is "a gauged symmetry"; P4 says "exact".
- Round-3 Decision 2 keeps "the trilemma becomes two program-native candidates"; #11 §12 counts three.
- Round-4 F4 says "the referee's normalization is half of mine", but the two lists do not map by a factor of two.
- Round 5 R11 and the diameter note §6 call the program's cosmology flat; #11 never says so.
- `HANDOFF.md` §1 "Three blind AI reviews returned verdict B" against §6's two rounds and an incomplete third; §2 "removed the mechanism" against #11 §10's route.
- `HANDOFF.md` §2 dates DR3 "late 2026"; `review/closed-universe/analyses/observations.json` finds only conference slides giving other dates.
- The root `CLAUDE.md` and #11's v2.4 note both say three founding ideas, and name different trios; the root names the diameter note v1.1 beside "note v1.2"; it lists the supersymmetry burden under the separate-photon form, while #11 §11.4 says either form.
- Row 7's flag 63 proposes wording "for a v2.4.1", though #11 is v2.5; flag 38 names rounds 3 and 4 where round 5's arbitration script stands the same way; flag 46's "5×10⁵ Gyr" against the note's bounds; flag 48's "never" drops the condition λ ≥ l_P.
- `notes/knot-dark-matter-standalone.md`'s banner and the `verify/soliton_obituary.py` docstring still say the soliton candidate is retired.
- `notes/closed-universe.md` gives τ's first minimum a = 1.34–18.5; `verify/closed_universe.py`, 1.34–18.9.
- #13 §3 "Below 10⁴³ newtons the effect is utterly negligible", while γ̃ − 1 = 0.0034 at that force; the diameter note's §5 "only" list against its §8 "two places".
- Smaller points: `verify/toy_s4.py`'s docstring; `review/round4/adjudicator/ctrl.out` against the toy note's control values; `verify/phase_space_diameter.py`'s docstring on where its anchors sit; the note's reference [P1]; Segue 1's age, 13 Gyr or 12 Gyr; `verify/closed_universe.py`'s label "#13's criterion".
