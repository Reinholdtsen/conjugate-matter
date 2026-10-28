"""Timing and correctness test of the C pair kernel against a direct numpy evaluation (N = 300),
including a finite-difference check that xdot - w = dH/dp and wdot = -dH/dx (Hamiltonian reading)."""
import numpy as np, time, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from run_nbody import deriv
rng = np.random.default_rng(0)
n = 300; Gm = 1.0/n; eps = 3.0; vs = 0.4; b = 0.1
x = rng.normal(size=(n,3)); w = rng.normal(scale=0.4, size=(n,3))
xd, wd, phi = deriv(x, w, Gm, eps, 1/vs**2, b*b, 1)
# numpy reference
dx = x[:,None,:]-x[None,:,:]; dw = w[:,None,:]-w[None,:,:]
r2 = (dx**2).sum(-1)+b*b; np.fill_diagonal(r2, np.inf)
W = np.exp(-0.5*(dw**2).sum(-1)/vs**2)
rinv = 1/np.sqrt(r2)
wd_ref = -(Gm*(1+eps*W)*rinv**3)[:,:,None]*dx; wd_ref = wd_ref.sum(1)
xd_ref = w + ((eps*Gm/vs**2)*W*rinv)[:,:,None].__mul__(dw).sum(1)
phi_ref = -(Gm*(1+eps*W)*rinv).sum(1)
print("max |wdot - ref| =", np.abs(wd-wd_ref).max(), " max |xdot - ref| =", np.abs(xd-xd_ref).max(), " max |phi-ref| =", np.abs(phi-phi_ref).max())
# finite-difference check of Hamilton's equations: H = sum m w^2/2 + (1/2) sum m phi  (m = Gm here since G=1, M=1)
def H(x, w):
    _, _, ph = deriv(x, w, Gm, eps, 1/vs**2, b*b, 1)
    return 0.5*Gm*np.sum(w**2) + 0.5*Gm*np.sum(ph)
i, k, h = 7, 1, 1e-6
xp = x.copy(); xp[i,k] += h; xm = x.copy(); xm[i,k] -= h
wp = w.copy(); wp[i,k] += h; wm = w.copy(); wm[i,k] -= h
dHdx = (H(xp,w)-H(xm,w))/(2*h); dHdw = (H(x,wp)-H(x,wm))/(2*h)
print(f"Hamilton check particle {i} comp {k}: -dH/dx / m = {-dHdx/Gm:.10f} vs wdot = {wd[i,k]:.10f}; dH/dw / m = {dHdw/Gm:.10f} vs xdot = {xd[i,k]:.10f}")
for N in (1000, 2000, 4000):
    x = rng.normal(size=(N,3)); w = rng.normal(scale=0.4, size=(N,3))
    t = time.time()
    for _ in range(5): deriv(x, w, 1.0/N, 3.0, 1/0.16, 0.01, 1)
    print(f"N={N}: {(time.time()-t)/5*1e3:.1f} ms per evaluation")
