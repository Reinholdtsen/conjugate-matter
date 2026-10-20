"""Extra Sec. 4 checks: spin-wave formula on the lattice, control-run scaling, residual symmetry of the potential."""
import numpy as np, sympy as sp
T, J = 0.6, 1.0
def sw_M(L):
    k = 2*np.pi*np.arange(L)/L
    lam = 4 - 2*np.cos(k)[:, None] - 2*np.cos(k)[None, :]
    lam[0, 0] = np.inf
    return np.exp(-0.5*(T/J)*np.sum(1/lam)/L**2)
for L in (16, 32, 64, 128):
    print(f"Gaussian spin-wave lattice <|M|>(L={L}) = {sw_M(L):.4f}")
print(f"lattice Gaussian ratio M(64)/M(16) = {sw_M(64)/sw_M(16):.4f};  closed form (64/16)^(-T/4piJ) = {(64/16)**(-T/(4*np.pi*J)):.4f}")
print(f"manuscript h=0 ratio 0.776/0.838 = {0.776/0.838:.4f}; referee MC ratio 0.7673/0.8371 = {0.7673/0.8371:.4f}")
ms = np.array([0.078, 0.033, 0.014]); mine = np.array([0.0630, 0.0318, 0.0156]); Ls = np.array([16, 32, 64])
print("control T=3: manuscript exponent d ln m / d ln L =", np.polyfit(np.log(Ls), np.log(ms), 1)[0],
      "; referee =", np.polyfit(np.log(Ls), np.log(mine), 1)[0], "; disordered-phase expectation -1")
print("control L=16: manuscript/referee =", 0.078/0.0630)
# residual symmetry of -mu[Tr(K K_ref)]^2 inside Sp(2,R): S^-1 K_ref S = +-K_ref
a, b, c, d = sp.symbols('a b c d')
S = sp.Matrix([[a, b], [c, d]]); Kr = sp.diag(1, -1)
for sgn in (1, -1):
    sol = sp.solve(list(S*(sgn*Kr) - Kr*S) + [a*d - b*c - 1], [a, b, c, d], dict=True)
    print(f"S^-1 K_ref S = {sgn:+d} K_ref, det S = 1: solutions {sol}")
th = sp.symbols('th', real=True)
R = sp.Matrix([[sp.cos(th), -sp.sin(th)], [sp.sin(th), sp.cos(th)]])
print("SO(2) elements preserving {+-K_ref}: R^-1 K_ref R =", sp.simplify(R.inv()*Kr*R).tolist(), "-> need sin(2th)=0: th in {0, pi/2, pi, 3pi/2} = {1, -rho?, -1, rho}")
rho = sp.Matrix([[0, 1], [-1, 0]])
print("R(pi/2) =", R.subs(th, sp.pi/2).tolist(), " R(3pi/2) =", R.subs(th, 3*sp.pi/2).tolist(), " rho =", rho.tolist(), " rho^4 =", (rho**4).tolist())
