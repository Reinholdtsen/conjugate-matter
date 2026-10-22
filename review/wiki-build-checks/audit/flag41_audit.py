#!/usr/bin/env python3
"""
Flag 41 audit (review/wiki-build-flags.md): does any executed code in the program show
model II's (complex Grosse-Wulkenhaar) "restoration under quantization", which toy note
section 6 lists under "Shown (each by executed code)"?

Part A: static audit. Extract every check() from verify/toy_*.py with ast; list the
         section-6 "Shown" items; find which checks touch the complex model, and whether any
         code samples or integrates the complex model's quantum measure exp(-S).
Part B: independent test of the finite-truncation statement <odd observable> = 0, by a
         Metropolis sample of exp(-S) for the complex model (mu2 = 4, lam = 1, as in toy_gw.py).
         This checks the easy, exact-by-symmetry half of the claim, not the no-volume-factor step.

Run:  /home/paul/git/reinholdtsen/conjugate-matter/.venv/bin/python flag41_audit.py
"""
import ast, re, sys
from pathlib import Path
import numpy as np

REPO = Path("/home/paul/git/reinholdtsen/conjugate-matter")

# ---------------- Part A: static audit
note = (REPO / "papers/reciprocity-toy-models.md").read_text().splitlines()
i0 = next(i for i, l in enumerate(note) if l.startswith("**Shown**"))
i1 = next(i for i, l in enumerate(note) if l.startswith("**Not shown:**"))
shown = [l[2:] for l in note[i0 + 1:i1] if l.startswith("- ")]
print("== Part A: toy note section 6")
print(f"heading (line {i0 + 1}): {note[i0]!r}")
for k, s in enumerate(shown, 1):
    print(f"  Shown item {k}: {s}")
print(f"number of Shown items: {len(shown)}")
rest_items = [k for k, s in enumerate(shown, 1) if "restoration" in s]
print(f"items mentioning restoration: {rest_items}")

# section 4 restoration subsection: does it carry a script pointer?
j0 = next(i for i, l in enumerate(note) if l.startswith("**Model II, complex fields: restoration.**"))
j1 = next(i for i, l in enumerate(note) if l.startswith("**Model I: the ρ-preserving potential.**"))
sub = "\n".join(note[j0:j1])
print(f"section 4 restoration subsection lines {j0 + 1}-{j1}: script pointer present? "
      f"{bool(re.search(r'toy_\w+\.py', sub))}")
print(f"  contains 'not proven': {'not proven' in sub}; contains 'We have not carried it out': "
      f"{'We have not carried it out' in sub}")

def check_names(path):
    tree = ast.parse(path.read_text())
    out = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and getattr(node.func, "id", None) == "check" and node.args:
            a = node.args[0]
            if isinstance(a, ast.Constant):
                out.append((a.lineno, a.value))
            elif isinstance(a, ast.JoinedStr):
                out.append((a.lineno, "".join(v.value if isinstance(v, ast.Constant) else "{..}" for v in a.values)))
    return sorted(out)

print("\n== Part A: checks in the gated toy scripts")
all_checks = {}
for name in ("toy_coset.py", "toy_gw.py", "toy_s4.py", "toy_s5.py"):
    all_checks[name] = check_names(REPO / "verify" / name)
    print(f"{name}: {len(all_checks[name])} checks")

gw = all_checks["toy_gw.py"]
complex_checks = [(ln, n) for ln, n in gw if "complex" in n.lower() or ln >= 140 and ln <= 154]
print("\ntoy_gw.py checks on the complex model (by name, or in its S2 vacua block):")
for ln, n in complex_checks:
    print(f"  line {ln}: {n}")

# Does any code evaluate a quantum expectation of the complex model?
src = (REPO / "verify/toy_gw.py").read_text()
tree = ast.parse(src)
funcs = {n.name: n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)}
def calls_in(node):
    return {getattr(c.func, "id", None) for c in ast.walk(node) if isinstance(c, ast.Call)}
print("\nfunctions in toy_gw.py that build a Hessian / one-loop free energy, and the action they call:")
for fname, f in funcs.items():
    if "hess" in fname:
        print(f"  {fname} calls {sorted(x for x in calls_in(f) if x and x.startswith('S_'))}")
oneloop_lines = [i + 1 for i, l in enumerate(src.splitlines()) if "np.log(ev" in l]
print(f"  lines computing 0.5*sum(log(eigenvalues)) (one-loop free energies): {oneloop_lines}")
# a Metropolis acceptance line compares a uniform random number with exp(-dE/T) or exp(-dS)
def is_accept(l):
    return "rng.random(" in l and "np.exp(" in l and "<" in l
for name in ("toy_gw.py", "toy_coset.py", "toy_s4.py", "toy_s5.py"):
    hits = [i + 1 for i, l in enumerate((REPO / "verify" / name).read_text().splitlines()) if is_accept(l)]
    print(f"  {name}: Metropolis acceptance lines (sampling a Boltzmann/quantum weight): {hits}")
uses_complex = [i + 1 for i, l in enumerate(src.splitlines()) if "S_complex(" in l]
print(f"  toy_gw.py lines calling S_complex: {uses_complex}")
print("  (S_complex is only evaluated at given configurations: symmetry checks, descent, flatness.)")

# ---------------- Part B: independent finite-truncation Monte Carlo
print("\n== Part B: Metropolis sample of exp(-S), complex model, mu2 = 4, lam = 1")
MU2, LAM = 4.0, 1.0
def run(N, seed, chains=16, sweeps=20000, therm=2000, step=0.6):
    rng = np.random.default_rng(seed)
    idx = np.add.outer(np.arange(N), np.arange(N)) + 1.0
    def S(phi):  # batch over chains
        P = np.einsum("cji,cjk->cik", phi.conj(), phi)          # phi^dagger phi
        return (np.sum((idx - MU2)*np.abs(phi)**2, axis=(1, 2))
                + LAM*np.einsum("cij,cji->c", P, P).real)
    phi = (rng.normal(size=(chains, N, N)) + 1j*rng.normal(size=(chains, N, N)))*0.5
    s = S(phi)
    O, A, acc, tot = [], [], 0, 0
    for sw in range(therm + sweeps):
        for m in range(N):
            for n in range(N):
                new = phi.copy()
                new[:, m, n] += step*(rng.normal(size=chains) + 1j*rng.normal(size=chains))
                sn = S(new)
                ok = rng.random(chains) < np.exp(-np.clip(sn - s, -50, 50))
                phi[ok] = new[ok]; s = np.where(ok, sn, s)
                acc += ok.sum(); tot += chains
        if sw >= therm:
            b = phi[:, 0, 0].conj()*phi[:, 1, 1]
            O.append(b.real); A.append(np.abs(b))
    O, A = np.array(O), np.array(A)
    return O.mean(), A.mean(), acc/tot

classical = np.sqrt(1.5*0.5)   # |phi00| |phi11| in the classical vacuum (q0 = 1.5, q1 = 0.5)
print(f"classical vacuum: Re(conj(phi00) phi11) = {classical:.4f} cos(beta); odd under the duality (beta -> beta + pi)")
for N in (2, 3):
    res = np.array([run(N, seed=1000*N + k) for k in range(4)])
    mO, mA = res[:, 0].mean(), res[:, 1].mean()
    eO, eA = res[:, 0].std(ddof=1)/2, res[:, 1].std(ddof=1)/2
    print(f"  N={N}: <Re(conj(phi00) phi11)> = {mO:+.4f} +- {eO:.4f}   <|conj(phi00) phi11|> = {mA:.4f} +- {eA:.4f}"
          f"   (4 seeds x 16 chains; acceptance {res[:, 2].mean():.2f})")
print("Reading: the duality-odd bilinear averages to zero within errors while its modulus does not;")
print("this is the exact-by-symmetry finite-truncation statement. It does not test the no-volume-factor step.")
