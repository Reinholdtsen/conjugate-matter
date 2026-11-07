"""Split WF-A's journal into one file per agent: wfA/<label>.json (reader) and wfA/<label>-verify.json."""
import json, sys
from pathlib import Path
J = Path("/home/paul/.claude/projects/-home-paul-git-reinholdtsen-conjugate-matter/45bf8e69-9188-453c-ad62-de0e44f5c85b/subagents/workflows/wf_c9a159be-379/journal.jsonl")
OUT = Path(__file__).parent
label = {}
n = 0
for line in J.open():
    d = json.loads(line)
    if d["type"] == "started":
        label[d["agentId"]] = d["label"]
    elif d["type"] == "result":
        lab = label.get(d["agentId"], d["agentId"])
        r = d["result"]
        if isinstance(r, str):
            try: r = json.loads(r)
            except Exception: pass
        (OUT / f"{lab}.json").write_text(json.dumps(r, indent=1, ensure_ascii=False), encoding="utf-8")
        n += 1
print(n, "results written:", sorted(p.stem for p in OUT.glob("*.json")))
