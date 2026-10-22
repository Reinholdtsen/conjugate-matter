import runpy, io, contextlib
import numpy as np
buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    ns = runpy.run_path("flag6_audit.py")
sqrt_eigs, P, gR, fR, esym = ns['sqrt_eigs'], ns['P'], ns['gR'], ns['fR'], ns['esym']
rng = np.random.default_rng(7)
for k in [1.9687, 2.718281828, 0.7310585786]:
    s0 = sqrt_eigs(gR, fR); s1 = sqrt_eigs(gR, fR / k**2) * k
    br = rng.standard_normal(5)
    p0 = P(gR, fR, br); p1 = P(gR, fR / k**2, [br[n] * k**n for n in range(5)])
    print(f"k={k}: max|s0-s1|/s0 = {np.max(np.abs(s0-s1)/s0):.3e}; P0={p0!r} P1={p1!r} rel={abs(p0-p1)/abs(p0):.3e}")
# perturb gR slightly off-structure to rule out a degenerate special case
g2 = gR + 0.37 * np.eye(4); f2 = fR @ fR / 50 + np.eye(4)
k = 3.3
br = rng.standard_normal(5)
p0 = P(g2, f2, br); p1 = P(g2, f2 / k**2, [br[n] * k**n for n in range(5)])
print(f"other g,f, k={k}: P0={p0!r} P1={p1!r} rel={abs(p0-p1)/abs(p0):.3e}")
