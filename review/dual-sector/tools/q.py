"""q.py PHRASE [PHRASE...]: verified statements (statements.json) and missed passages (missed.md) containing all phrases."""
import json, sys, re
from pathlib import Path
P = Path(__file__).parent
phr = [p.lower() for p in sys.argv[1:]]
for s in json.loads((P / "statements.json").read_text()):
    if all(p in s["quote"].lower() for p in phr):
        print(f"[{s['paper']} | {s['where'][:70]} | {s['verdict']} | {s['quote_check'][:28]}]\n  {s['quote']}\n")
for line in (P / "missed.md").read_text().splitlines():
    if all(p in line.lower() for p in phr):
        print("MISSED:", line[:700], "\n")
