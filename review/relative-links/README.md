# The relative-links record (2026-11-06 to 2026-11-07)

The record of two changes to the wiki: the papers moved from `papers/` to `wiki/papers/` so that the site publishes
them (2026-11-06), and every citation became a link (2026-11-07). The root `CLAUDE.md`, "Since the handoff", states
the results; `wiki/CLAUDE.md`, Links, states the rules that follow from them. No claim's status changed.

## Files

- `scripts/` — the scripts, as they ran from `work/papers-move/` (they find the repository root two folders up and
  write their outputs to `work/papers-move/`; copy them back there to rerun them):
  - `rewrite_paths.py` — every path to the four papers, `papers/X.md` to `wiki/papers/X.md`, in every tracked file;
  - `frontmatter.py` — each paper's `# H1` became its frontmatter title, with weight, `status: record` and a description;
  - `subsection_headings.py` — the papers' 15 numbered bold subsection titles became `###` headings;
  - `github_anchors.py`, `fit_github_rule.py` — fetched GitHub's heading anchors for every pushed Markdown file and
    checked the slug rule that became `github_slug` in `scripts/check-wiki.py` (4,555 of 4,555 headings agree);
  - `relink.py` — the rewrite of the wiki's links: absolute links to relative paths, code paths to links, section
    citations to links of their heading, by the rules in its docstring;
  - `unlink.py` — the inverse of `relink.py`, which rebuilt the wiki as it was before the rewrite so that the rules
    could be tightened and run again; for every page not edited by hand, its output equalled `HEAD` with
    `rewrite_paths.py` applied;
  - `hand_fixes.py` — four wrong links the audits named after the rules were tightened, fixed by hand.
- `github-anchors.json` — `github_anchors.py`'s output: per file, the source headings and GitHub's anchors.
- `relink-links.tsv` — every section link `relink.py` made (file, line, label, document, rule, context).
- `relink-unresolved.tsv` — every section citation it left plain, and why.
- `audit/` — three audits by independent agents, each given the sampled links and the documents, not the rules'
  expected accuracy:
  - `a-links.tsv`, `a-verdicts.tsv` — 160 links of the first version's two weakest rules (80 nearest document, 80
    page sources): 152 correct, 8 wrong (3 and 5). The page-sources rule was then dropped and the others tightened;
  - `b-links.tsv`, `b-verdicts.tsv` — 115 links of the first version's other rules (50 attached, 50 continuation,
    15 "of"): all correct. The auditor also reported 55 wrong links outside its sample, in its final message, not in
    the file; 44 of the 49 distinct cases were right or plain after the rules were tightened;
  - `u-plain.tsv`, `u-verdicts.tsv` — 60 citations the first version left plain: 58 determinable by a careful
    reader, 2 sections of outside papers;
  - `c-links.tsv`, `c-verdicts.tsv` — 100 fresh links of the tightened nearest-document rule, none seen before:
    98 correct, 2 wrong;
  - `rules-of-sample.json` — which rule made each row of `a-links.tsv` and `b-links.tsv`, kept out of the auditors'
    files.

The wiki as it stood before the rewrite, the build logs and a throwaway test site stayed in `work/papers-move/`.
