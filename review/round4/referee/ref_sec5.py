"""Referee check of Sec. 5: null lines of eta = omega K, section condition, I_K for the stated test state."""
import sympy as sp
import numpy as np

om = sp.Matrix([[0, 1], [-1, 0]]); rho = sp.Matrix([[0, 1], [-1, 0]])
phi = sp.symbols('phi', real=True)
K = sp.Matrix([[sp.cos(phi), sp.sin(phi)], [sp.sin(phi), -sp.cos(phi)]])
eta = om*K
print("== null lines")
print("  eta symmetric:", sp.simplify(eta - eta.T) == sp.zeros(2), " det eta =", sp.simplify(eta.det()))
t = sp.symbols('t', real=True)
v = sp.Matrix([sp.cos(t), sp.sin(t)])
q = sp.simplify((v.T*eta*v)[0, 0])
print("  v(t)^T eta v(t) =", q)
print("  q at t=phi/2:", sp.simplify(q.subs(t, phi/2)), " at t=phi/2+pi/2:", sp.simplify(q.subs(t, phi/2+sp.pi/2)))
# sin(phi-2t) has exactly two zeros per period pi in t; numerically count zeros for random phi
import numpy as _np
for ph in _np.random.default_rng(3).uniform(0, 2*_np.pi, 3):
    tt = _np.linspace(0, _np.pi, 200001)[:-1]; qq = _np.sin(ph - 2*tt)
    print(f"    phi={ph:.4f}: sign changes of q on [0,pi) = {_np.sum(_np.sign(qq[1:]) != _np.sign(qq[:-1]))}")
ep = sp.Matrix([sp.cos(phi/2), sp.sin(phi/2)]); em = sp.Matrix([-sp.sin(phi/2), sp.cos(phi/2)])
print("  K e+ - e+ =", sp.simplify(K*ep - ep).T, "  K e- + e- =", sp.simplify(K*em + em).T)
print("  -> eigenline angles phi/2 and phi/2+pi/2; null set {phi/2, phi/2+pi/2} matches for all phi")
print("  (-eta) null lines: same quadratic form up to sign:", sp.simplify(((v.T*(-eta)*v)[0, 0]) + q) == 0)
r1 = sp.simplify(rho.inv()*ep)
print("  rho^-1 e+ parallel to e-? cross =", sp.simplify(r1[0]*em[1] - r1[1]*em[0]))

print("\n== section condition in null coordinates (phi=0: eta = [[0,-1],[-1,0]])")
eta0 = eta.subs(phi, 0); etainv = eta0.inv()
print("  eta0 =", eta0.tolist(), " eta0^-1 =", etainv.tolist())
u, w = sp.symbols('u w', real=True)   # u along e+ (x-axis), w along e- (p-axis)
F, G = sp.Function('F'), sp.Function('G')
def pair(f, g):
    gf = sp.Matrix([sp.diff(f, u), sp.diff(f, w)]); gg = sp.Matrix([sp.diff(g, u), sp.diff(g, w)])
    return sp.simplify((gf.T*etainv*gg)[0, 0])
def box(f):
    H = sp.Matrix([[sp.diff(f, u, u), sp.diff(f, u, w)], [sp.diff(f, w, u), sp.diff(f, w, w)]])
    return sp.simplify((etainv*H).trace())
print("  F(u),G(u): pair =", pair(F(u), G(u)), " box F =", box(F(u)))
print("  F(w),G(w): pair =", pair(F(w), G(w)))
print("  F(u),G(w): pair =", pair(F(u), G(w)))
print("  F(u)+G(w) with itself: pair =", pair(F(u)+G(w), F(u)+G(w)), " box =", box(F(u)+G(w)))
print("  with -eta: F(u),G(w) pair =", sp.simplify(-pair(F(u), G(w))))

print("\n== I_K for psi ~ exp(-(x-1.3)^2/0.7) + 0.6 exp(-(x+1.3)^2/0.7), hbar = 1")
x = np.linspace(-30, 30, 2**15); dx = x[1]-x[0]
psi = np.exp(-(x-1.3)**2/0.7) + 0.6*np.exp(-(x+1.3)**2/0.7)
psi = psi/np.sqrt(np.sum(np.abs(psi)**2)*dx)
p = 2*np.pi*np.fft.fftfreq(x.size, d=dx); dp = abs(p[1]-p[0])
psit = np.fft.fft(psi)*dx/np.sqrt(2*np.pi)*np.exp(-1j*p*x[0])
print("  norms:", np.sum(np.abs(psi)**2)*dx, np.sum(np.abs(psit)**2)*dp)
Ix = np.sum(np.abs(psi)**4)*dx
Ip = np.sum(np.abs(psit)**4)*dp
print(f"  I_(+K_ref) = int |psi(x)|^4 dx = {Ix:.6f}")
print(f"  I_(-K_ref) = int |psi~(p)|^4 dp = {Ip:.6f}")
# via an explicit Wigner function on a grid (independent of the marginal shortcut)
xg = np.linspace(-6, 6, 481); pg = np.linspace(-8, 8, 641); dxg = xg[1]-xg[0]; dpg = pg[1]-pg[0]
yg = np.linspace(-12, 12, 1201); dyg = yg[1]-yg[0]
def psi_f(z):
    a = np.exp(-(z-1.3)**2/0.7) + 0.6*np.exp(-(z+1.3)**2/0.7)
    return a
nrm = np.sqrt(np.sum(np.abs(psi_f(x))**2)*dx)
W = np.zeros((xg.size, pg.size))
E = np.exp(-1j*np.outer(yg, pg))
for i, xx in enumerate(xg):
    c = psi_f(xx + yg/2)*np.conj(psi_f(xx - yg/2))/nrm**2
    W[i] = np.real(c @ E)*dyg/(2*np.pi)
print("  int W =", np.sum(W)*dxg*dpg, "  int W^2 =", np.sum(W**2)*dxg*dpg, "  1/2pi =", 1/(2*np.pi))
Ixw = np.sum((np.sum(W, axis=1)*dpg)**2)*dxg
Ipw = np.sum((np.sum(W, axis=0)*dxg)**2)*dpg
print(f"  from Wigner marginals: I_+ = {Ixw:.6f}, I_- = {Ipw:.6f}")
# combined map psi -> F psi, K -> -K: I_{-K}[F psi] = int |F F psi (p)|^4 = int |psi(-p)|^4
psiFF = np.fft.fft(psit)*dp/np.sqrt(2*np.pi)  # F applied twice ~ parity (on the fft grid ordering)
print(f"  I_(-K)[F psi] = int |F(F psi)|^4 = {np.sum(np.abs(psiFF)**4)*dp:.6f}  (should equal I_(+K)[psi] = {Ix:.6f})")

print("\n== covariance under rotations R(a) in SO(2) (H = 1 kept fixed) vs a boost (needs a scale)")
def I_general(W, xg, pg, e_plus, e_minus):
    """I = int du ( int dv W(u e+ + v e-) )^2 using interpolation of W; e+-, given as columns."""
    from scipy.interpolate import RegularGridInterpolator
    f = RegularGridInterpolator((xg, pg), W, bounds_error=False, fill_value=0.0)
    us = np.linspace(-7, 7, 561); vs = np.linspace(-9, 9, 721); du = us[1]-us[0]; dv = vs[1]-vs[0]
    UU, VV = np.meshgrid(us, vs, indexing='ij')
    pts = UU[..., None]*e_plus[None, None, :] + VV[..., None]*e_minus[None, None, :]
    vals = f(pts.reshape(-1, 2)).reshape(UU.shape)
    marg = vals.sum(axis=1)*dv
    return np.sum(marg**2)*du
# a rotated state W_R(z) = W(R^-1 z) and rotated K: e+- -> R e+-
a = 0.4
Rm = np.array([[np.cos(a), -np.sin(a)], [np.sin(a), np.cos(a)]])
from scipy.interpolate import RegularGridInterpolator
fW = RegularGridInterpolator((xg, pg), W, bounds_error=False, fill_value=0.0)
XX, PP = np.meshgrid(xg, pg, indexing='ij')
pts = np.stack([XX.ravel(), PP.ravel()], 1) @ Rm  # R^-1 z = R^T z ; row-vector form z @ R
WR = fW(pts).reshape(XX.shape)
e1, e2 = np.array([1.0, 0.0]), np.array([0.0, 1.0])
print("  I_K0[W] (interp) =", I_general(W, xg, pg, e1, e2))
print("  I_{R K0 R^-1}[W_R] =", I_general(WR, xg, pg, Rm @ e1, Rm @ e2))
# boost S = diag(l, 1/l): eigenlines of S K0 S^-1 are still the axes; the measure split du dv is ambiguous
for lam_ in (1.0, 2.0):
    print(f"  same K0, parametrisation e+ = {lam_} e1, e- = e2/{lam_} (du dv area preserved): I = {I_general(W, xg, pg, lam_*e1, e2/lam_):.6f}")
