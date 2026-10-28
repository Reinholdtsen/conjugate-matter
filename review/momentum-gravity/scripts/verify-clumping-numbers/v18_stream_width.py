"""Verifier v18: per-component width of the pure-gate top mode delta f = p1^1/2 * psi0 (1D grid eigenvector,
no Mehler formula), vs analytic [1/2 + sqrt(1+4r^2)/2]^-1/2 and sqrt(v*/sigma)."""
import numpy as np
for r in [1000/120, 8.333, 32.0]:
    x, h = np.linspace(-10, 10, 4001, retstep=True)
    u1 = (2*np.pi)**-0.25*np.exp(-x**2/4)
    K = (u1[:, None]*np.exp(-0.5*r*r*(x[:, None]-x[None, :])**2)*u1[None, :])*h
    lam, V = np.linalg.eigh(K)
    psi = V[:, -1]; psi *= np.sign(psi[2000])
    df = u1*psi
    s_num = np.sqrt(np.sum(x**2*df)/np.sum(df))
    s_an = (0.5 + np.sqrt(1+4*r*r)/2)**-0.5
    print(f"r={r:.4f}: width numerical={s_num:.4f}, analytic={s_an:.4f}, sqrt(v*/sigma)={np.sqrt(1/r):.4f}, 3D rms={np.sqrt(3)*s_num:.4f}")
