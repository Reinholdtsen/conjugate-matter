"""Index check for the strong-gating spectrum (MW, r = 155/120). For the m=0 sector, count the
static eigenvalues above (k/k_J)^2 separately for perturbations even (n_e) and odd (n_o) in v_z,
using the same (v_z, v_perp) quadrature as dynamic_eig.py (symmetric form). Compare n_e - n_o with
the number of purely growing modes found by the brute-force dynamic runs (copied from their
.out files). A Hamiltonian-Krein-type count (dagger: Grillakis 1990; Kapitula-Kevrekidis-Sandstede
2004; Pelinovsky 2005, from memory) predicts at least |n_e - n_o| purely growing modes."""
import numpy as np, sys
sys.path.insert(0, '/home/paul/.claude/projects/-home-paul-git-reinholdtsen-conjugate-matter/7156ee3a-6166-4b9e-84c4-fb9703a50211/mg/verify-clumping-derivation')
from dynamic_eig import i0e
r = 155/120; vs = 1/r
Lz, hz, npp = 5.0, 0.05, 10
vz = np.linspace(-Lz, Lz, int(round(2*Lz/hz)) + 1); h = vz[1] - vz[0]
t, wgl = np.polynomial.laguerre.laggauss(npp); vp = np.sqrt(2*t)
pz = np.exp(-vz**2/2)/np.sqrt(2*np.pi)
Wz = np.exp(-(vz[:, None]-vz[None, :])**2/(2*vs**2))
X = vp[:, None]*vp[None, :]/vs**2
Wp = np.exp(-(vp[:, None]-vp[None, :])**2/(2*vs**2))*i0e(X)
sz = np.sqrt(pz*h); sp_ = np.sqrt(wgl)          # perp: p_perp absorbed in the Laguerre weight
# even/odd projection in v_z (grid symmetric about 0)
n = len(vz); half = n//2
Pe = np.zeros((half+1, n)); Po = np.zeros((half, n))
for i in range(half):
    Pe[i, i] = Pe[i, n-1-i] = 1/np.sqrt(2); Po[i, i] = 1/np.sqrt(2); Po[i, n-1-i] = -1/np.sqrt(2)
Pe[half, half] = 1.0
Kz_g = sz[:, None]*Wz*sz[None, :]; Kp_g = sp_[:, None]*Wp*sp_[None, :]
az = sz; ap = sp_
def counts(k2, gt):
    out = []
    for P in (Pe, Po):
        Kz = P @ Kz_g @ P.T; a = P @ az
        K = gt*np.kron(Kz, Kp_g) + np.kron(np.outer(a, a), np.outer(ap, ap))
        ev = np.linalg.eigvalsh(K)
        out.append(int((ev > k2).sum()))
    return out
found = {19.7392: {240: 1, 255: 1, 272: 1, 280.7: 1, 283: 0, 290: 0, 320: 0, 500: 0, 700: 2, 850: 2, 1000: 2, 1200: 2,
                   1400: 0, 1700: 0, 2000: 0, 3000: 3, 3500: 3, 4200: 3, 5000: 3, 19000: 4, 23000: 4},
         4.9348: {56.14: 1, 280.7: 2, 1000: 3, 3000: 0},
         24.77: {800: 2, 1000: 2, 1200: 2, 1400: 2, 1700: 0, 4500: 3, 5500: 3, 22000: 4, 26000: 4}}
print("check: gravity only, kap^2=0.99 ->", counts(0.99, 0.0), "(expect [1, 0])")
for k2, d in found.items():
    for gt, npg in d.items():
        ne, no = counts(k2, gt)
        flag = "ok" if npg >= abs(ne-no) else "VIOLATES"
        print(f"kap^2={k2} gt={gt:g}: n_e={ne}, n_o={no}, |n_e-n_o|={abs(ne-no)}, purely growing found={npg}  {flag}")
