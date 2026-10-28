"""Independent two-fluid linear growth with the Hubble-flow-gated chi-only force (K5-K7, K10, K11).

Model (same physical reductions as the agent states, re-implemented from scratch):
  sub-horizon; radiation and massive neutrino smooth; CDM (chi) feels gravity + gated force;
  baryons feel gravity only, held at delta_b = 0 before z_drag = 1059.94 (Planck 2018, dagger), pressureless after.
  delta_c'' + (2 + dlnH/dlna - A/H) delta_c' = 1.5 [Om_c(a) d_c + Om_b(a) d_b + eps Om_c(a) Rd(y) d_c]
  delta_b'' + (2 + dlnH/dlna) delta_b'       = 1.5 [Om_c(a) d_c + Om_b(a) d_b]
  A/H = (eps/2) Om_c(a) Rv(y)   (anti-drag), y = k s_c, s_c = v*/(aH) comoving.
Density kernel options: 'B' = agent's R (static effective potential), 'A' = reading-A kernel
  R_A(y) = Int_0^1 R_B(y mu) d mu (derived in vkernels.py). Anti-drag on/off.
Integrator: classical RK4 in ln a with N steps (different variable layout from the agent's; checked by
  step doubling). Initial conditions at a = 1e-5: delta_c = 1, delta_c' = 0.5 (ratio insensitive; checked).
"""
import numpy as np
import mpmath as mp
import vcosmo as C

h = C.h
Oc = C.omc/h**2
Ob = C.omb/h**2
Om, Or, OL = C.Om, C.Or, C.OL
zdrag = 1059.94
c_kms = C.c_kms
H0 = C.H0

# ------------- kernel tables
ytab = np.logspace(-4, 4, 1601)
def _RB_gauss(y):
    x = mp.mpf(y)/mp.sqrt(2)
    return float(mp.sqrt(2)*y*mp.sqrt(mp.pi)/2*mp.exp(-x*x)*mp.erfi(x))
def _RB_rat(y):
    b = mp.sqrt(2)*y
    return float(y/mp.sqrt(2)*(mp.exp(-b)*mp.ei(b)-mp.exp(b)*mp.ei(-b)))

def _build(fun):
    RB = np.array([fun(y) for y in ytab])
    xg, wg = np.polynomial.legendre.leggauss(200)
    mu = 0.5*(xg+1); w = 0.5*wg
    ly = np.log(ytab)
    def RBi(yy):
        yy = np.maximum(yy, 1e-12)
        out = np.interp(np.log(yy), ly, RB)
        small = yy < ytab[0]
        return np.where(small, RB[0]*(yy/ytab[0])**2, out)
    RA = np.array([np.sum(w*RBi(y*mu)) for y in ytab])
    RV = np.array([3*np.sum(w*mu**2*RBi(y*mu)) for y in ytab])
    return RB, RA, RV

_cache = {}
def kernels(gate):
    if gate not in _cache:
        _cache[gate] = _build(_RB_gauss if gate == "gauss" else _RB_rat)
    return _cache[gate]

def interp_k(tab, y):
    ly = np.log(ytab)
    yy = np.maximum(y, 1e-12)
    out = np.interp(np.log(yy), ly, tab)
    return np.where(yy < ytab[0], tab[0]*(yy/ytab[0])**2, out)

# ------------- background helpers
def E2(a): return Or/a**4+Om/a**3+OL
def dlnH(a): return (-4*Or/a**4-3*Om/a**3)/(2*E2(a))

def evolve(kMpc, eps, vstar, z_end=3.0, gate="gauss", dens="B", antidrag=True, ungated=False,
           N=6000, a_i=1e-5, dcp0=0.5, return_all=False):
    """kMpc: array (nk,), eps: array (ne,). Returns delta_c, delta_b at z_end, shape (ne, nk)."""
    k = np.asarray(kMpc, float)[None, :]
    e = np.asarray(eps, float)[:, None]
    RB, RA, RV = kernels(gate)
    Rd_tab = RB if dens == "B" else RA
    x0, x1 = np.log(a_i), np.log(1/(1+z_end))
    xs = np.linspace(x0, x1, N+1); dx = xs[1]-xs[0]
    xdrag = np.log(1/(1+zdrag))
    shape = np.broadcast(k, e).shape
    dc = np.ones(shape); dcp = dcp0*np.ones(shape)
    db = np.zeros(shape); dbp = np.zeros(shape)
    def rhs(x, dc, dcp, db, dbp, bary_on):
        a = np.exp(x)
        e2 = E2(a)
        Omc = Oc/a**3/e2; Omb = Ob/a**3/e2
        Hk = H0*np.sqrt(e2)                       # km/s/Mpc
        sc = vstar/(a*Hk)                          # comoving Mpc
        y = k*sc
        if ungated:
            Rd = np.ones_like(y); Rv = np.zeros_like(y)
        else:
            Rd = interp_k(Rd_tab, y)
            Rv = interp_k(RV, y) if antidrag else np.zeros_like(y)
        fric = 2+dlnH(a)
        src_g = 1.5*(Omc*dc+Omb*db)
        ddc = -(fric-0.5*e*Omc*Rv)*dcp+src_g+1.5*e*Omc*Rd*dc
        ddb = (-fric*dbp+src_g)*bary_on
        return dcp, ddc, dbp, ddb
    for i in range(N):
        x = xs[i]
        bon = 1.0 if x+dx/2 >= xdrag else 0.0
        if bon == 0.0:
            db[:] = 0; dbp[:] = 0
        s1 = rhs(x, dc, dcp, db, dbp, bon)
        s2 = rhs(x+dx/2, dc+dx/2*s1[0], dcp+dx/2*s1[1], db+dx/2*s1[2], dbp+dx/2*s1[3], bon)
        s3 = rhs(x+dx/2, dc+dx/2*s2[0], dcp+dx/2*s2[1], db+dx/2*s2[2], dbp+dx/2*s2[3], bon)
        s4 = rhs(x+dx, dc+dx*s3[0], dcp+dx*s3[1], db+dx*s3[2], dbp+dx*s3[3], bon)
        dc = dc+dx/6*(s1[0]+2*s2[0]+2*s3[0]+s4[0])
        dcp = dcp+dx/6*(s1[1]+2*s2[1]+2*s3[1]+s4[1])
        db = db+dx/6*(s1[2]+2*s2[2]+2*s3[2]+s4[2])
        dbp = dbp+dx/6*(s1[3]+2*s2[3]+2*s3[3]+s4[3])
    return dc, db

def transfer(kMpc, eps, vstar, **kw):
    """Returns T_m^2, T_b^2 (gated/LCDM power ratio) for total (c+b) matter and baryons, shape (ne, nk)."""
    eps = np.atleast_1d(np.asarray(eps, float))
    e_all = np.concatenate([[0.0], eps])
    dc, db = evolve(kMpc, e_all, vstar, **kw)
    dm = (Oc*dc+Ob*db)/(Oc+Ob)
    Tm2 = (dm[1:]/dm[0:1])**2
    Tb2 = (db[1:]/db[0:1])**2
    return Tm2, Tb2

if __name__ == "__main__":
    z = 3
    conv = float(C.H(z))/(1+z)
    kp = 0.009*conv
    dl = 0.02
    ks = kp*np.exp(np.array([-dl, 0, dl]))
    print("k_p = %.4f /Mpc" % kp)
    for dens in ["B", "A"]:
        for ad in [True, False]:
            Tm2, Tb2 = transfer(ks, [0.1, 0.3, 1.0], 120.0, dens=dens, antidrag=ad)
            for j, e in enumerate([0.1, 0.3, 1.0]):
                dn_m = (np.log(Tm2[j, 2])-np.log(Tm2[j, 0]))/(2*dl)
                dn_b = (np.log(Tb2[j, 2])-np.log(Tb2[j, 0]))/(2*dl)
                print("dens=%s antidrag=%-5s eps=%.1f v*=120: T_m^2(kp)=%.4f dn_m=%+.4f | T_b^2=%.4f dn_b=%+.4f"
                      % (dens, ad, e, Tm2[j, 1], dn_m, Tb2[j, 1], dn_b))
    # step-doubling and IC checks
    T1, _ = transfer([kp], [0.3], 120.0, N=3000)
    T2, _ = transfer([kp], [0.3], 120.0, N=12000)
    T3, _ = transfer([kp], [0.3], 120.0, N=6000, dcp0=1.0)
    T4, _ = transfer([kp], [0.3], 120.0, N=6000, dcp0=0.0)
    print("numerics: T_m(kp, eps=0.3) N=3000 %.7f  N=12000 %.7f  IC dc'=1: %.7f  IC dc'=0: %.7f"
          % (np.sqrt(T1[0, 0]), np.sqrt(T2[0, 0]), np.sqrt(T3[0, 0]), np.sqrt(T4[0, 0])))
    # T_m at 3/Mpc and 10/Mpc for eps=0.3, v*=120 (agent: 1.12, 1.87, 2.72)
    Tm2, Tb2 = transfer([kp, 3.0, 10.0], [0.3], 120.0)
    print("eps=0.3, v*=120: T_m at k_p, 3/Mpc, 10/Mpc = %.3f %.3f %.3f" % tuple(np.sqrt(Tm2[0])))
    Tm2, Tb2 = transfer([kp], [0.03], 120.0)
    print("eps=0.03, v*=120: T_b^2/T_m^2 at k_p = %.4f" % (Tb2[0, 0]/Tm2[0, 0]))
    # ungated reading: T^2 at eps=0.01
    Tm2, Tb2 = transfer(ks, [0.01], 120.0, ungated=True)
    print("ungated eps=0.01: T_m^2(kp)=%.4f dn=%+.5f ; T_b^2=%.4f" % (Tm2[0, 1], (np.log(Tm2[0, 2])-np.log(Tm2[0, 0]))/(2*dl), Tb2[0, 1]))
