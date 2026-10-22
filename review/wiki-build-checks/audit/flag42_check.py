"""Flag 42 audit: is the Langmann-Szabo-Zarembo comparison (round-4 revision 4)
recorded as applied while toy note v2 says it was not carried out?

Read-only: reads repository files and git objects; writes nothing in the repo.
"""
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

REPO = Path(sys.argv[1] if len(sys.argv) > 1 else "/home/paul/git/reinholdtsen/conjugate-matter")


def read(rel):
    return (REPO / rel).read_text(encoding="utf-8")


def git(*args):
    return subprocess.run(["git", "-C", str(REPO), *args], capture_output=True,
                          text=True, check=True).stdout


def norm(s):
    return re.sub(r"\s+", " ", s)


def section(text, start_pat, end_pat):
    m = re.search(start_pat, text, re.M)
    if not m:
        return ""
    rest = text[m.start():]
    e = re.search(end_pat, rest[1:], re.M)
    return rest if not e else rest[: e.start() + 1]


LSZ_PAT = re.compile(r"Zarembo|LSZ|0308043|exact solution|exactly solvable|\[8\]", re.I)

print("== 1. Round-4 adjudication ==")
adj = read("review/round4-adjudication.md")
head = [l for l in adj.splitlines() if l.startswith("## Revisions")]
print("revisions heading:", head)
print("heading claims 'applied':", any("applied" in h for h in head))
rev = section(adj, r"^## Revisions", r"^## ")
rev4 = norm(section(rev, r"^4\. ", r"^5\. "))
rev6 = norm(section(rev, r"^6\. ", r"^\Z"))
print("revision 4:", rev4.strip())
print("revision 4 asks 'compare with Langmann–Szabo–Zarembo':",
      "compare with Langmann–Szabo–Zarembo" in rev4)
print("revision 6 separately asks 'add LSZ':", "add LSZ" in rev6)
omit = [l for l in adj.splitlines() if l.startswith("| Omitted prior work")]
print("omitted-prior-work ruling says 'Accepted, as citations and reframing':",
      bool(omit) and "Accepted, as citations and reframing" in omit[0])
score = [l for l in adj.splitlines() if "must be restated" in l]
print("pre-registration scoring line:", [norm(s) for s in score])

print("\n== 2. Referee's request (audit notes) ==")
notes = read("review/round4/referee/audit-notes.md")
for l in notes.splitlines():
    if re.search(r"LSZ|Zarembo", l):
        print("  >", norm(l)[:240])

print("\n== 3. Toy note v2 (papers/reciprocity-toy-models.md) ==")
toy = read("papers/reciprocity-toy-models.md")
cur = None
hits = []
for i, l in enumerate(toy.splitlines(), 1):
    if l.startswith("## "):
        cur = l[3:].strip()
    if LSZ_PAT.search(l):
        hits.append((i, cur, l.strip()[:160]))
for h in hits:
    print("  line %d [%s]: %s" % h)
s4 = section(toy, r"^## 4\.", r"^## 5\.")
print("§4 contains 'We have not carried it out.':", "We have not carried it out." in s4)
print("§4 states any result of [8] (agree/consistent/confirm/differ):",
      bool(re.search(r"\[8\][^\n]*(agree|consistent|confirm|differ|match)", s4)))
s6 = section(toy, r"^## 6\.", r"^## References")
notshown = section(s6, r"^\*\*Not shown", r"^\*\*Motivation")
print("§6 'Not shown' list mentions the LSZ check:", bool(LSZ_PAT.search(notshown)))

print("\n== 4. Toy worklog (notes/toy-lagrangian.md) ==")
wl = read("notes/toy-lagrangian.md")
wr = section(wl, r"^## Write-up and review", r"^## ")
print("claims 'v2 applies every accepted revision':", "v2 applies every accepted revision" in wr)
m = re.search(r"v2 applies every accepted revision:\*\*\n(.*?)\n- Two drafting", wr, re.S)
bullets = re.findall(r"^  - (.*(?:\n    .*)*)", m.group(1), re.M)
print("number of applied-revision bullets:", len(bullets))
for b in bullets:
    print("   *", norm(b))
print("any bullet mentions LSZ / Zarembo / comparison / exact solution:",
      any(re.search(r"Zarembo|LSZ|compar|exact solution", b, re.I) for b in bullets))

print("\n== 5. Gated scripts (verify/) ==")
vhits = [p.name for p in sorted((REPO / "verify").glob("*.py"))
         if re.search(r"Zarembo|LSZ|0308043", p.read_text(encoding="utf-8"))]
print("verify/ scripts mentioning LSZ:", vhits)

print("\n== 6. Git record ==")
for c in ("6606734", "5ca7d81"):
    print(c, git("log", "-1", "--format=%ad | %s", "--date=iso", c).strip())
t1 = datetime.fromisoformat(git("log", "-1", "--format=%aI", "6606734").strip())
t2 = datetime.fromisoformat(git("log", "-1", "--format=%aI", "5ca7d81").strip())
print("seconds between v2 commit and 'mark v2 revisions applied':", (t2 - t1).total_seconds())
msg = git("log", "-1", "--format=%B", "6606734")
print("6606734 message claims 'applies every revision accepted in round 4':",
      "applies every revision accepted in round 4" in norm(msg))
print("6606734 message mentions LSZ/Zarembo/comparison:",
      bool(re.search(r"Zarembo|LSZ|compar", msg, re.I)))
diff = git("show", "6606734", "--", "papers/reciprocity-toy-models.md")
print("6606734 itself adds the 'not carried it out' line:",
      any(l.startswith("+") and "We have not carried it out" in l for l in diff.splitlines()))
v1 = git("show", "d9a06ac:papers/reciprocity-toy-models.md")
print("v1 (as reviewed, d9a06ac) mentions LSZ at all:", bool(re.search(r"Zarembo|0308043", v1)))

print("\n== 7. Other summaries of the same claim ==")
ck = read("papers/broken-born-checkpoint-v2.md")
item11 = [l for l in ck.splitlines() if "v2 applies" in l]
print("#11:", [norm(l).strip()[-80:] for l in item11])
cm = read("CLAUDE.md")
print("CLAUDE.md:", [norm(l).strip()[-60:] for l in cm.splitlines() if "v2 applies" in l])
open_ends = section(cm, r"^- The toy Lagrangian", r"^- HANDOFF")
print("CLAUDE.md toy open ends mention LSZ:", bool(LSZ_PAT.search(open_ends)))
print("#11 item 11 'Still open' mentions LSZ:", any(LSZ_PAT.search(l) for l in item11))
