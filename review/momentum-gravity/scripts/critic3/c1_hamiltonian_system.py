"""Round-3 critic, check c1: which Hamiltonian-reading linear system is right, c4b (round-2 critic)
or D2 (round-3 dark-tests derivation verifier), and what Lyman-alpha bound follows.

Model (hypothetical, outside the record): chi-only U = -Gt m^2 W(|w - w'|/v*)/r, W = exp(-t^2/2),
eps = Gt/G, gate argument = relative canonical momentum per mass (Hubble flow + peculiar).

Own derivation (written out in the critic's notes; summarized here).  Proper coordinates, cold chi fluid,
pi = canonical momentum per mass = H r + w; per-unit-mass Hamiltonian h = pi^2/2 + Phi_N + psi(r, pi),
psi = -Gt Int rho_c(r') W(|pi - pi_c(r')|/v*)/|r - r'| d^3r'.
  continuity : u_pec = w + d psi/d pi                (anomalous velocity A)
  momentum   : Dw/Dt + H u_pec = -grad dPhi - d psi/d r |_pi
Linear Fourier coefficients (y = k v*/H, k physical; kappa = (4 pi/3) Gt rho_c/H^2 = (eps/2) Omega_c):
  force at fixed pi, from delta : 3 kappa R1(y)        R1 = y Int W j1(yt) dt
  force at fixed pi, from w     : kappa R_v(y) (anti-drag)   R_v = 1 + 3 Int W'(t) g(yt) dt, g = j0 - 2 j1/x
  anomalous velocity, from delta: 3 i kappa v* J(y)   J = Int t W'(t) j1(yt) dt   (< 0: outflow)
  anomalous velocity, from w    : kappa B(y)          B = 1 + 3 Int [t W'' g(yt) + 2 W' j1(yt)/(yt)] dt
With theta = -i k w/H, ' = d/dlna, this gives (my algebra, then the two identities below):
  delta' = (1 + kappa B) theta + 3 kappa y J delta
  theta' = -(2 + Hdot/H^2) theta + 1.5 (Om_c d_c + Om_b d_b) + 3 kappa (R1 - yJ) d_c + kappa (R_v - B) theta
  identities: R1 - yJ = R (R = y Int sin(yt) W dt, kernel of grad[W(s/s_c)/s]); R_v - B = -3 yJ.
So the momentum equation's density coupling is 3 kappa R: the -H*A_delta term is already inside R.
c4b uses R for the gated force AND adds -H*A_delta again (an extra -3 kappa yJ d_c).
The same structure follows in comoving canonical variables, where the Hubble subtraction is in the
generating function and d/dx at fixed comoving momentum differentiates the gate's Hubble part (kernel R).

This script: (1) kernels from the definitions above by direct quadrature (not from closed forms or from
other agents' identities), with the identities checked numerically; (2) an own background
(Planck 2018 TT,TE,EE+lowE+lensing+BAO column, dagger: h = 0.6766, omega_c = 0.11933, omega_b = 0.02242,
massless neutrinos) and RK4 growth (baryons held at zero before z_drag = 1060, dagger);
(3) T^2, dn at the DESI pivot for five systems; (4) compressed-DESI bounds; (5) the eBOSS fit.
Data inputs (checked [S] by the round-3 dark-tests verifiers, not by me): DESI DR1 Delta^2 = 0.379 +- 0.032,
n = -2.309 +- 0.019, r = -0.1738; Planck baseline 0.3495, -2.3052 (errors 0.0083, 0.0032);
eBOSS 0.310 +- 0.020, -2.340 +- 0.006, r = 0.512.
"""
import numpy as np

# ---------------- (1) kernels by direct quadrature ----------------
t = np.linspace(0.0, 12.0, 120001)
W = np.exp(-t**2 / 2); Wp = -t * W; Wpp = (t**2 - 1) * W


def sph(x):
    x = np.asarray(x, float)
    j0 = np.empty_like(x); j1 = np.empty_like(x); g = np.empty_like(x); j1x = np.empty_like(x)
    s = np.abs(x) < 1e-2
    xs = x[s]
    j0[s] = 1 - xs**2 / 6 + xs**4 / 120
    j1[s] = xs / 3 - xs**3 / 30
    j1x[s] = 1 / 3 - xs**2 / 30 + xs**4 / 840
    xl = x[~s]
    j0[~s] = np.sin(xl) / xl
    j1[~s] = np.sin(xl) / xl**2 - np.cos(xl) / xl
    j1x[~s] = j1[~s] / xl
    g = j0 - 2 * j1x
    return j0, j1, j1x, g


def kernels(y):
    _, j1, j1x, g = sph(y * t)
    R = y * np.trapezoid(np.sin(y * t) * W, t)
    R1 = y * np.trapezoid(W * j1, t)
    J = np.trapezoid(t * Wp * j1, t)
    Rv = 1 + 3 * np.trapezoid(Wp * g, t)
    B = 1 + 3 * np.trapezoid(t * Wpp * g + 2 * Wp * j1x, t)
    return R, R1, J, Rv, B


print("(1) kernels by direct quadrature of their definitions")
for y in (0.3, 1.0, 1.08, 1.413, 3.0):
    R, R1, J, Rv, B = kernels(y)
    mu, wmu = np.polynomial.legendre.leggauss(64); mu = 0.5 * (mu + 1); wmu = 0.5 * wmu
    Rmu = np.array([kernels(y * m)[0] for m in mu])
    print(f"  y = {y:5.3f}: R = {R:.6f}  R1 = {R1:.6f}  J = {J:+.6f}  R_v = {Rv:.6f}  B = {B:+.6f} | "
          f"R1 - yJ - R = {R1 - y*J - R:+.1e}; R_v - B + 3yJ = {Rv - B + 3*y*J:+.1e}; "
          f"R1 - Int R(y mu) = {R1 - np.sum(wmu*Rmu):+.1e}; R_v - 3 Int mu^2 R = {Rv - 3*np.sum(wmu*mu**2*Rmu):+.1e}")
print("  [anchors from other agents: VDD v3_kernels.out at y = 1.08: R 0.803130, R1 0.311446, Rv 0.536423, B -0.938630;"
      " c4b at y = 1: R 0.72478, R_v 0.47699, R_a -0.87168, J_W -0.44956]")

ly = np.linspace(np.log(1e-3), np.log(300.0), 700)
TAB = np.array([kernels(np.exp(l)) for l in ly])   # columns R, R1, J, Rv, B
ASYM = np.array([1.0, 1.0, 0.0, 1.0, 1.0])


def K(y):
    l = np.log(np.maximum(y, 1e-30))
    out = []
    for c in range(5):
        v = np.interp(l, ly, TAB[:, c])
        v = np.where(l > ly[-1], ASYM[c], v)
        if c in (0, 1, 3):           # R, R1, Rv ~ y^2 at small y
            v = np.where(l < ly[0], TAB[0, c] * (np.exp(l) / np.exp(ly[0]))**2, v)
        out.append(v)
    return out
i_min = np.argmin(TAB[:, 4])
print(f"  min B = {TAB[i_min, 4]:+.4f} at y = {np.exp(ly[i_min]):.3f}  ->  1 + kappa B = 0 at kappa = {-1/TAB[i_min, 4]:.3f}")

# ---------------- (2) background ----------------
h = 0.6766; omc, omb = 0.11933, 0.02242
H0 = 100 * h
Oc, Ob = omc / h**2, omb / h**2
Om = Oc + Ob
Orad = 2.4728e-5 * (1 + 0.2271 * 3.046) / h**2
OL = 1 - Om - Orad
fc, fb = Oc / Om, Ob / Om
E = lambda a: np.sqrt(Orad / a**4 + Om / a**3 + OL)
HdH2 = lambda a: (-2 * Orad / a**4 - 1.5 * Om / a**3) / E(a)**2
Omm = lambda a: Om / a**3 / E(a)**2
a_drag = 1 / 1061.0
zp = 3.0; ap = 1 / (1 + zp)
kp = 0.009 * H0 * E(ap) * ap            # comoving 1/Mpc
print(f"(2) background: Om = {Om:.4f}; pivot k_p = 0.009 s/km at z = 3 -> {kp:.4f} /Mpc; y_p(v*=120) = {kp*120/(ap*H0*E(ap)):.4f}")


def grow(k, eps, vs, sysname, a_end=ap, a_i=1e-6, nstep=16000):
    k, eps = np.broadcast_arrays(np.asarray(k, float), np.asarray(eps, float))
    N0, N1 = np.log(a_i), np.log(a_end); dN = (N1 - N0) / nstep
    dc = np.ones(k.shape); th = np.zeros(k.shape); db = np.zeros(k.shape); tb = np.zeros(k.shape)

    def rhs(N, dc, th, db, tb):
        a = np.exp(N)
        om = Omm(a); oc, ob = fc * om, fb * om
        fr = -(2 + HdH2(a)); grav = 1.5 * (oc * dc + ob * db)
        y = k * vs / (a * H0 * E(a))
        R, R1, J, Rv, B = K(y)
        kap = 0.5 * eps * oc
        if sysname == "lcdm":
            ddc, dth = th, fr * th + grav
        elif sysname == "agent":          # dark-tests K4 as implemented: R density + force-law anti-drag
            ddc, dth = th, fr * th + grav + 3 * kap * R * dc + kap * Rv * th
        elif sysname == "F":              # force law, correct density kernel R1
            ddc, dth = th, fr * th + grav + 3 * kap * R1 * dc + kap * Rv * th
        elif sysname == "H":              # Hamiltonian, written before using the identities
            ddc = (1 + kap * B) * th + 3 * kap * y * J * dc
            dth = fr * th + grav + 3 * kap * (R1 - y * J) * dc + kap * (Rv - B) * th
        elif sysname == "c4b":            # c4b: R for the gated force plus -H*A_delta again
            ddc = (1 + kap * B) * th + 3 * kap * y * J * dc
            dth = fr * th + grav + 3 * kap * R * dc - 3 * kap * y * J * dc + kap * (Rv - B) * th
        else:
            raise ValueError(sysname)
        if a >= a_drag:
            ddb, dtb = tb, fr * tb + grav
        else:
            ddb, dtb = 0 * db, 0 * tb
        return np.array([ddc, dth, ddb, dtb])

    Y = np.array([dc, th, db, tb]); N = N0
    for _ in range(nstep):
        k1 = rhs(N, *Y); k2 = rhs(N + dN/2, *(Y + dN/2*k1)); k3 = rhs(N + dN/2, *(Y + dN/2*k2)); k4 = rhs(N + dN, *(Y + dN*k3))
        Y = Y + dN/6*(k1 + 2*k2 + 2*k3 + k4); N += dN
    return fc * Y[0] + fb * Y[2], Y[2]


dl = 0.05
kk3 = kp * np.exp(np.array([-dl, 0.0, dl]))
m0, b0 = grow(kk3, 0.0, 120.0, "lcdm")


def resp(eps_arr, vs, sysname):
    eps_arr = np.atleast_1d(eps_arr)
    kg, eg = np.meshgrid(kk3, eps_arr, indexing="ij")
    m, b = grow(kg, eg, vs, sysname)
    Tm2 = (m / m0[:, None])**2; Tb2 = (b / b0[:, None])**2
    return (Tm2[1], (np.log(Tm2[2]) - np.log(Tm2[0])) / (2*dl),
            Tb2[1], (np.log(Tb2[2]) - np.log(Tb2[0])) / (2*dl))


print("(3) DESI pivot, v* = 120 km/s, z = 3: T_m^2, dn_m | T_b^2, dn_b")
ref = {"agent": "agent 1.0783 +0.1308", "F": "VDD iii 1.0355 +0.0636; VDN A 1.0355 +0.0636",
       "H": "VDD i 0.9480 -0.0599", "c4b": "c4b 0.9861 +0.0047; VDD transcription 0.9864 +0.0050"}
for s in ("agent", "F", "H", "c4b"):
    r = resp([0.1, 1.0], 120.0, s)
    print(f"  {s:5s}: eps=0.1: {r[0][0]:.4f} {r[1][0]:+.4f} | {r[2][0]:.4f} {r[3][0]:+.4f} ; "
          f"eps=1: {r[0][1]:.4f} {r[1][1]:+.4f} | {r[2][1]:.4f} {r[3][1]:+.4f}   [{ref[s]} at eps=0.1]")
r12 = resp([0.1], 120.0, "H")
for ns_ in (8000, 32000):
    mm, _ = grow(np.array([kp]), np.array([0.1]), 120.0, "H", nstep=ns_)
    mmo, _ = grow(np.array([kp]), np.array([0.0]), 120.0, "lcdm", nstep=ns_)
    print(f"  step test H, eps=0.1: nstep={ns_}: T_m^2 = {(mm[0]/mmo[0])**2:.6f}")

print("    scale dependence, H and c4b, eps = 0.1, v* = 120, z = 3: T_m^2 at k = 0.1, 0.3, 0.693, 1.5, 3, 10 /Mpc")
kks = np.array([0.1, 0.3, kp, 1.5, 3.0, 10.0])
mo, _ = grow(kks, 0.0, 120.0, "lcdm")
for s in ("H", "c4b", "F"):
    mm, _ = grow(kks, 0.1 + 0 * kks, 120.0, s)
    print(f"    {s:4s}: " + " ".join(f"{v:.4f}" for v in (mm / mo)**2))

# ---------------- (4) compressed-DESI bounds ----------------
D0, n0 = 0.3495, -2.3052


def make_chi2(d, sD, sn, rho, base_err):
    C = np.array([[sD**2 + base_err[0]**2, rho*sD*sn], [rho*sD*sn, sn**2 + base_err[1]**2]])
    Ci = np.linalg.inv(C)
    def chi2(T2, dn):
        v = np.array([D0*T2 - d[0], n0 + dn - d[1]])
        return np.einsum("i...,ij,j...->...", v, Ci, v)
    return chi2


desi_b = make_chi2((0.379, -2.309), 0.032, 0.019, -0.1738, (0.0083, 0.0032))
desi_0 = make_chi2((0.379, -2.309), 0.032, 0.019, -0.1738, (0.0, 0.0))
eboss = make_chi2((0.310, -2.340), 0.020, 0.006, 0.512, (0.0083, 0.0032))


_RESP = {}


def bound(vs, sysname, chi2, emax, n=41):
    key = (vs, sysname, emax, n)
    eg = np.concatenate([[0.0], np.geomspace(emax * 1e-3, emax, n)])
    if key not in _RESP:
        _RESP[key] = resp(eg, vs, sysname)
    Tm2, dnm, Tb2, dnb = _RESP[key]
    out = []
    for T2, dn in ((Tm2, dnm), (Tb2, dnb)):
        ef = np.linspace(0, emax, 40001)
        c2 = chi2(np.interp(ef, eg, T2), np.interp(ef, eg, dn))
        i0 = np.argmin(c2); ab = np.where((c2 > c2[i0] + 3.84) & (ef > ef[i0]))[0]
        out.append((ef[ab[0]] if len(ab) else np.inf, ef[i0], c2[0], c2[i0]))
    return out


print("(4) compressed-DESI bounds on eps (Delta chi^2 = 3.84 above the minimum over eps >= 0), matter / gas ratio")
for vs, emax in ((30.0, 6.0), (120.0, 1.0), (300.0, 0.6)):
    for s in ("H", "F", "c4b"):
        bb = bound(vs, s, desi_b, emax); b0_ = bound(vs, s, desi_0, emax)
        print(f"  v* = {vs:5.0f} {s:4s}: with baseline errors {bb[0][0]:.4f} / {bb[1][0]:.4f} ; "
              f"DESI errors only {b0_[0][0]:.4f} / {b0_[1][0]:.4f}")
print("  [VDD v3_lya_withbase.out: 120: i 0.0572/0.1069, iii 0.0585/0.1760; 30: i 0.3649/1.1573, iii 0.7820/2.5790;"
      " 300: i 0.0147/0.1643, iii 0.0202/0.0421.  c4b (DESI errors only): 120 0.3405/0.2959; 30 0.8166/2.4110; 300 0.0113/0.0410]")

# ---------------- (5) eBOSS in the H reading ----------------
for vs, emax in ((120.0, 0.3), (30.0, 1.5)):
    bb = bound(vs, "H", eboss, emax)
    print(f"(5) eBOSS compressed, H reading, v* = {vs:.0f}: matter: chi2(0) = {bb[0][2]:.2f}, best eps = {bb[0][1]:.4f} "
          f"(chi2 = {bb[0][3]:.2f}), upper bound {bb[0][0]:.4f}   [VDD: 120: 26.31 -> 1.89 at 0.054, bound 0.0744; 30: best 0.31, bound 0.44]")
