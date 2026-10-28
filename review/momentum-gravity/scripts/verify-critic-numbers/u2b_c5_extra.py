"""verify-critic-numbers: extra c5 cases, my radial solver (imported from u2), compared with the critic's
table where the critic used the narrow-gate asymptote Q/Lambda_g (marked * in c5.out) or a coarser grid."""
import sys, importlib.util, io, contextlib
spec = importlib.util.spec_from_file_location("u2", "/home/paul/.claude/projects/-home-paul-git-reinholdtsen-conjugate-matter/7156ee3a-6166-4b9e-84c4-fb9703a50211/mg/verify-critic-numbers/u2_c5_static_thresholds.py")
# load only the definitions: exec the file up to the first print
src = open(spec.origin).read()
defs = src[:src.index('print("== anchors")')]
ns = {}
exec(defs, ns)
Radial, crit, lam_g_closed, W_pair = ns['Radial'], ns['crit'], ns['lam_g_closed'], ns['W_pair']
for label, r, Qs in (("dwarf core v*=10", 3.0, (1.0966, 4.3865)), ("MW v*=30", 155/30, (4.9348, 24.77)),
                     ("MW v*=10", 15.5, (4.9348, 24.77))):
    S = Radial(r)
    out = [f"Q={Q}: {crit(S, Q):.4g} (asymptote Q/Lam_g = {Q/lam_g_closed(r):.4g})" for Q in Qs]
    print(f"{label:18s} r = {r:6.3f}: crossover {1/lam_g_closed(r):.4g}; " + "; ".join(out), flush=True)
