# Audit of flag 3, numeric part (d = 4, the program's dimension).
# Anchor independent of the paper: Siegel's Moebius action Z -> (AZ+B)(CZ+D)^-1 of Sp(2d,R)
# on the Siegel upper half space, and the stabilizer of J0 inside Sp(2d,R) (computed, not assumed).
import numpy as np
from itertools import combinations_with_replacement

rng = np.random.default_rng(20261021)
d = 4
Id = np.eye(d); Zr = np.zeros((d, d)); I2d = np.eye(2*d)
omega = np.block([[Zr, Id], [-Id, Zr]])
J0 = np.block([[Zr, Id], [Id, Zr]])          # = eta_0, the vacuum polarization of #7
eta0 = J0.copy()
oinv = np.linalg.inv(omega)

def HZ(X, Y):
    Yi = np.linalg.inv(Y)
    return np.block([[Y + X@Yi@X, X@Yi], [Yi@X, Yi]])
def IZ(X, Y): return oinv@HZ(X, Y)
def anti(X, Y):
    I = IZ(X, Y); return J0@I + I@J0
def ZtoXY(Z): return Z.real, Z.imag
def sym(m): return (m + m.T)/2
def expm(Mt):
    # scaling and squaring with a 30-term Taylor series (no scipy in the venv)
    n = max(0, int(np.ceil(np.log2(max(np.linalg.norm(Mt, 1), 1e-16)))) + 4)
    A = Mt/2**n; E = np.eye(len(Mt)); T = np.eye(len(Mt))
    for k in range(1, 30):
        T = T@A/k; E = E + T
    for _ in range(n): E = E@E
    return E
def moebius(g, Z):
    A, B, C, D = g[:d, :d], g[:d, d:], g[d:, :d], g[d:, d:]
    return (A@Z + B)@np.linalg.inv(C@Z + D)

# --- 0. Anchor: equivariance of H_Z under Siegel's action (fix the convention by test) ---
X = sym(rng.standard_normal((d, d))); a = rng.standard_normal((d, d)); Y = a@a.T + Id
g = expm(oinv@sym(rng.standard_normal((2*d, 2*d)))*0.3)  # omega^-1 * symmetric = element of sp(2d)
print("0. g symplectic (g^T omega g = omega):", np.allclose(g.T@omega@g, omega))
Zg = moebius(g, X + 1j*Y); Xg, Yg = ZtoXY(Zg)
cand1 = np.linalg.inv(g).T@HZ(X, Y)@np.linalg.inv(g); cand2 = g@HZ(X, Y)@g.T
print("   H_{g.Z} = g^-T H_Z g^-1 :", np.allclose(HZ(Xg, Yg), cand1),
      "| H_{g.Z} = g H_Z g^T :", np.allclose(HZ(Xg, Yg), cand2))

# --- 1. Stabilizer of J0 in sp(2d): solve the linear conditions, get its dimension ---
basis = []
for i in range(2*d):
    for j in range(2*d):
        E = np.zeros((2*d, 2*d)); E[i, j] = 1; basis.append(E)
rows = []
for E in basis:
    rows.append(np.concatenate([(E.T@omega + omega@E).ravel(), (E@J0 - J0@E).ravel()]))
Mlin = np.array(rows).T
_, sv, Vt = np.linalg.svd(Mlin)
null = Vt[np.sum(sv > 1e-10):]
print("1. dim of sp(2d) ∩ commutant(J0) =", len(null), "(d^2 =", d*d, ")")
gens = [v.reshape(2*d, 2*d) for v in null]
# the compact part (stabilizer of Z = i as well) and the rest
iZ = 1j*Id
def dZ_at_i(Xi):  # derivative of the Moebius action at Z = i along generator Xi
    t = 1e-6
    return (moebius(expm(t*Xi), iZ) - moebius(expm(-t*Xi), iZ))/(2*t)
Dmat = np.array([np.concatenate([dZ_at_i(G).real.ravel(), dZ_at_i(G).imag.ravel()]) for G in gens])
rk = np.linalg.matrix_rank(Dmat, tol=1e-6)
print("   orbit Stab(J0).i has dimension", rk, "(d(d+1)/2 =", d*(d+1)//2, "); stabilizer of i inside it:", len(gens) - rk, "(dim O(d) =", d*(d-1)//2, ")")
dX = Dmat[:, :d*d]; dY = Dmat[:, d*d:]
print("   tangent of the orbit at Z = i is purely along X: max|dY| =", float(np.abs(dY).max()), " max|dX| =", round(float(np.abs(dX).max()), 4))

# --- 2. Points of the orbit lie on the zero set and have X != 0 ---
print("2. random finite elements of Stab(J0) acting on Z = i:")
for k in range(3):
    G = sum(rng.standard_normal()*Gk for Gk in gens)
    s = expm(G)
    Zo = moebius(s, iZ); Xo, Yo = ZtoXY(Zo)
    print(f"   |X| = {np.linalg.norm(Xo):.4f}, min eig Y = {np.linalg.eigvalsh(sym(Yo)).min():.4f}, "
          f"|Y - Y^-1| = {np.linalg.norm(Yo - np.linalg.inv(Yo)):.4f}, |{{J0,I[Z]}}| = {np.linalg.norm(anti(Xo, sym(Yo))):.2e}, "
          f"|[X,Y]| = {np.linalg.norm(Xo@Yo - Yo@Xo):.2e}, |X^2+Y^2-1| = {np.linalg.norm(Xo@Xo + Yo@Yo - Id):.2e}, "
          f"|Z Zbar - 1| = {np.linalg.norm(Zo@Zo.conj() - Id):.2e}")

# --- 3. Linearization at the vacuum: kernel dimension of (x, h) -> {J0, I[Z]} ---
symbasis = []
for (i, j) in combinations_with_replacement(range(d), 2):
    E = np.zeros((d, d)); E[i, j] = E[j, i] = 1; symbasis.append(E)
n = len(symbasis)
cols = []
t = 1e-6
for which in ("x", "h"):
    for E in symbasis:
        if which == "x": p, m = anti(t*E, Id), anti(-t*E, Id)
        else:            p, m = anti(Zr, Id + t*E), anti(Zr, Id - t*E)
        cols.append(((p - m)/(2*t)).ravel())
L = np.array(cols).T
svL = np.linalg.svd(L, compute_uv=False)
print("3. linearized map at Z = i: rank", int(np.sum(svL > 1e-6)), "of", 2*n, "; kernel dimension", int(np.sum(svL <= 1e-6)),
      "; columns for x-directions max norm:", float(np.abs(L[:, :n]).max()))

# --- 4. A positive-norm potential V = ||{J0,I[Z]}||_F^2 along the curved valley and along straight x ---
X1 = sym(rng.standard_normal((d, d))); X1 = X1/np.linalg.norm(X1, 2)  # spectral norm 1
w, Q = np.linalg.eigh(X1)
print("4. V = ||{J0,I[Z]}||_F^2:")
for tt in [0.1, 0.5, 0.9]:
    Xv = tt*X1; Yv = Q@np.diag(np.sqrt(1 - (tt*w)**2))@Q.T
    Vval = np.linalg.norm(anti(Xv, Yv))**2
    Vline = np.linalg.norm(anti(Xv, Id))**2
    print(f"   t = {tt}: valley X = t X1, Y = sqrt(1 - X^2): V = {Vval:.2e} | straight line X = t X1, Y = 1: V = {Vline:.4e}, V/t^4 = {Vline/tt**4:.4f}")
# Hessian of V at the vacuum by central differences in the 2n coordinates
def Vcoord(c):
    Xc = sum(ci*E for ci, E in zip(c[:n], symbasis)); Yc = Id + sum(ci*E for ci, E in zip(c[n:], symbasis))
    return np.linalg.norm(anti(Xc, Yc))**2
hstep = 1e-4; Hs = np.zeros((2*n, 2*n)); e = np.eye(2*n)
for i in range(2*n):
    for j in range(i, 2*n):
        val = (Vcoord(hstep*(e[i]+e[j])) - Vcoord(hstep*(e[i]-e[j])) - Vcoord(hstep*(-e[i]+e[j])) + Vcoord(-hstep*(e[i]+e[j])))/(4*hstep**2)
        Hs[i, j] = Hs[j, i] = val
ev = np.linalg.eigvalsh(Hs)
print("   Hessian of V at Z = i: number of ~zero eigenvalues =", int(np.sum(np.abs(ev) < 1e-4)), "of", 2*n,
      "; x-x block max |entry| =", f"{np.abs(Hs[:n, :n]).max():.1e}", "; smallest nonzero eigenvalue =", round(float(ev[np.abs(ev) >= 1e-4].min()), 4))

# --- 5. The program's own definition (#5 B, #11 sections 4-5): J compatible with H iff J is an involution
#        anticommuting with I = omega^-1 H; then eta = H J is a neutral metric and (I, J, K) close.
print("5. P2' definition on the zero set vs off it:")
Xz = Q@np.diag(0.6*np.sign(w))@Q.T; Yz = Q@np.diag(np.full(d, 0.8))@Q.T   # on the zero set, X != 0
Xo2 = 0.3*X1; Yo2 = Id                                                     # off it
for label, (Xa, Ya) in [("on zero set (X != 0)", (Xz, Yz)), ("off zero set", (Xo2, Yo2))]:
    H = HZ(Xa, Ya); eta = H@J0
    Ia = oinv@H; Ja = np.linalg.inv(eta)@H; Ka = np.linalg.inv(eta)@omega if np.allclose(eta, eta.T) else None
    sig = np.linalg.eigvalsh(sym(eta))
    out = f"   {label}: |{{J0,I}}| = {np.linalg.norm(J0@Ia + Ia@J0):.2e}, eta = H J0 symmetric: {np.allclose(eta, eta.T)}"
    if Ka is not None:
        out += (f", signature (+{int(np.sum(sig > 0))}, -{int(np.sum(sig < 0))}), I^2=-1: {np.allclose(Ia@Ia, -I2d)}, "
                f"J^2=1: {np.allclose(Ja@Ja, I2d)}, K^2=1: {np.allclose(Ka@Ka, I2d)}, IJ=K: {np.allclose(Ia@Ja, Ka)}, eta == eta_0: {np.allclose(eta, eta0)}")
    print(out)

# --- 6. Readings a steelman could invoke, each tested ---
print("6. alternative readings of 'compatible locus':")
Ygen = a@a.T + Id
print("   (b) eta_0-compatible slice (#5 C, #11 6): (eta0^-1 H_Z)^2 = 1 at X = 0, generic Y:",
      np.allclose((eta0@HZ(Zr, Ygen))@(eta0@HZ(Zr, Ygen)), I2d), "; at the X != 0 zero-set point:",
      np.allclose((eta0@HZ(Xz, Yz))@(eta0@HZ(Xz, Yz)), I2d))
lam = np.linalg.eigvalsh(Ygen)
print("   (c) on X = 0 the anticommutator is [[Y - Y^-1, 0],[0, Y - Y^-1]]:",
      np.allclose(anti(Zr, Ygen), np.block([[Ygen - np.linalg.inv(Ygen), Zr], [Zr, Ygen - np.linalg.inv(Ygen)]])),
      "; eigenvalues lam - 1/lam vanish only at lam = 1 for lam > 0; for this Y:", np.round(lam - 1/lam, 4))
JZ = lambda Xa, Ya: eta0@HZ(Xa, Ya)  # J[Z] = eta0^-1 H_Z (eta0^-1 = eta0)
for label, (Xa, Ya) in [("X = 0, generic Y", (Zr, Ygen)), ("X != 0 zero-set point", (Xz, Yz))]:
    Ja = JZ(Xa, Ya); Ia = IZ(Xa, Ya)
    print(f"   (e) {{J[Z], I[Z]}} with J[Z] = eta0^-1 H_Z, at {label}: {np.linalg.norm(Ja@Ia + Ia@Ja):.2e}")
print("   (d) J0 = eta0^-1 H_Z forces H_Z = eta0 J0 =", "identity" if np.allclose(eta0@J0, I2d) else "not identity", "-> Z = i only")
