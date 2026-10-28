"""
v3_cosmo.py -- verifier's own background cosmology, kernel tables and linear growth
integrator for the gated chi-only force, in four linear systems (N = ln a, ' = d/dN,
Theta = -i k u/(aH), kappa = (eps/2) Omega_c(a), y = k v*/(aH)):

 'lcdm'  : no gated force.
 'iii'   : force law (vdot = -grad_x U at fixed v; xdot = v):
           d' = Th ; Th' = -(2+Hd/H^2)Th + 1.5 Om d_m + 3 kappa R1 d + kappa Rv Th
 'agent' : the system K4 states (density kernel RA instead of R1, same anti-drag):
           Th' = ... + 3 kappa RA d + kappa Rv Th
 'i'     : Hamiltonian, gate on canonical momenta (exact in eps, linear in amplitude):
           d' = (1 + kappa B) Thw + 3 kappa y J d
           Thw' = -(2+Hd/H^2)Thw + 1.5 Om d_m + 3 kappa RA d - 3 kappa y J Thw
 'ii'    : Lagrangian, gate on velocities (exact in eps):
           Thu = (Thw + 3 kappa y J d)/(1 - kappa B) ; d' = Thu
           Thw' = -(1+Hd/H^2)Thw - Thu + 1.5 Om d_m + 3 kappa R1 d + kappa Rv Thu
Baryons: gravity only, held at zero before z_drag, pressureless after.  Radiation and
neutrinos smooth.  Kernels from v3_kernels.py identities (checked there by brute force):
 R1 = int_0^1 RA(y mu) dmu, Rv = 3 int_0^1 mu^2 RA(y mu) dmu, J = (R1 - RA)/y, B = Rv + 3yJ.
"""
import numpy as np
import mpmath as mp

# ---- Planck 2018 base LCDM (TT,TE,EE+lowE+lensing; Table 2 of arXiv:1807.06209) ----
h = 0.6736
OCH2, OBH2 = 0.1200, 0.02237
ONUH2 = 0.06/93.14             # one massive nu, sum 0.06 eV (standard 93.14 eV relation)
TCMB, NEFF = 2.7255, 3.046
OGH2 = 2.4728e-5*(TCMB/2.7255)**4   # photons from a_rad T^4
ORH2 = OGH2*(1 + NEFF*(7/8)*(4/11)**(4/3))
H0 = 100*h                     # km/s/Mpc
Oc, Ob, Onu, Or = OCH2/h**2, OBH2/h**2, ONUH2/h**2, ORH2/h**2
Om = Oc + Ob + Onu
OL = 1 - Om - Or
Z_DRAG = 1059.94               # Planck 2018 Table 2
C_KMS = 299792.458

def E2(a): return Or/a**4 + Om/a**3 + OL
def Hof(a): return H0*np.sqrt(E2(a))
def Om_a(a, which):
    d = {'c': Oc, 'b': Ob, 'm': Om}[which]
    return d/a**3/E2(a)
def Orad_a(a): return Or/a**4/E2(a)
def HdotH2(a): return -1.5*Om/a**3/E2(a) - 2*Or/a**4/E2(a)

# ---- kernel tables ----
def _RA_gauss(y):
    x = mp.mpf(y)/mp.sqrt(2)
    return mp.sqrt(2)*y*mp.sqrt(mp.pi)/2*mp.exp(-x**2)*mp.erfi(x)

def _RA_rational(y):
    # y int_0^inf sin(yt) * 2/(t^2+2) dt ; int sin(bx)/(x^2+c^2) = [e^{-bc}Ei(bc) - e^{bc}Ei(-bc)]/(2c)
    c = mp.sqrt(2); b = mp.mpf(y)
    return y*2*(mp.exp(-b*c)*mp.ei(b*c) - mp.exp(b*c)*mp.ei(-b*c))/(2*c)

_TAB = {}
def kernel_table(gate):
    if gate in _TAB: return _TAB[gate]
    RAf = _RA_gauss if gate == 'gauss' else _RA_rational
    ly = np.linspace(np.log(1e-4), np.log(1e4), 1601)
    mus, wts = np.polynomial.legendre.leggauss(64)
    mus = 0.5*(mus+1); wts = 0.5*wts
    RA = np.zeros_like(ly); R1 = np.zeros_like(ly); Rv = np.zeros_like(ly)
    for i, l in enumerate(ly):
        y = float(np.exp(l))
        RA[i] = float(RAf(y))
        vals = np.array([float(RAf(y*m)) for m in mus])
        R1[i] = np.sum(wts*vals)
        Rv[i] = 3*np.sum(wts*mus**2*vals)
    yy = np.exp(ly)
    J = (R1 - RA)/yy
    B = Rv + 3*yy*J
    _TAB[gate] = (ly, dict(RA=RA, R1=R1, Rv=Rv, yJ=yy*J, B=B))
    return _TAB[gate]

def kern(gate, y):
    ly, T = kernel_table(gate)
    l = np.clip(np.log(y), ly[0], ly[-1])
    return {k: np.interp(l, ly, v) for k, v in T.items()}

# ---- growth ----
def grow(k, eps, vstar, reading, gate='gauss', a_end=0.25, a_ini=1e-5, nstep=6000,
         ic_slope=0.5, return_all=False):
    """k [1/Mpc comoving] and eps arrays broadcastable; returns (d_c, d_b, d_m) at a_end."""
    k = np.asarray(k, float); eps = np.asarray(eps, float)
    shape = np.broadcast(k, eps).shape
    k = np.broadcast_to(k, shape); eps = np.broadcast_to(eps, shape)
    N0, N1 = np.log(a_ini), np.log(a_end)
    dN = (N1 - N0)/nstep
    Ndrag = np.log(1/(1+Z_DRAG))
    dc = np.ones(shape); th = np.full(shape, ic_slope)   # th = Theta_c or Theta_w
    db = np.zeros(shape); tb = np.zeros(shape)

    def rhs(N, dc, th, db, tb, baryons_on):
        a = np.exp(N)
        Oca, Oba = Om_a(a, 'c'), Om_a(a, 'b')
        fr = -(2 + HdotH2(a))
        grav = 1.5*(Oca*dc + Oba*db)
        if reading == 'lcdm':
            ddc = th; dth = fr*th + grav
        else:
            y = k*vstar/(a*Hof(a))
            K = kern(gate, y)
            kap = 0.5*eps*Oca
            if reading == 'iii':
                ddc = th; dth = fr*th + grav + 3*kap*K['R1']*dc + kap*K['Rv']*th
            elif reading == 'agent':
                ddc = th; dth = fr*th + grav + 3*kap*K['RA']*dc + kap*K['Rv']*th
            elif reading == 'agent_noad':
                ddc = th; dth = fr*th + grav + 3*kap*K['RA']*dc
            elif reading == 'i':
                ddc = (1 + kap*K['B'])*th + 3*kap*K['yJ']*dc
                dth = fr*th + grav + 3*kap*K['RA']*dc - 3*kap*K['yJ']*th
            elif reading == 'ii':
                thu = (th + 3*kap*K['yJ']*dc)/(1 - kap*K['B'])
                ddc = thu
                dth = -(1 + HdotH2(a))*th - thu + grav + 3*kap*K['R1']*dc + kap*K['Rv']*thu
            elif reading == 'c4b':         # critic c4b's 'consistent' system, transcribed:
                # same as 'i' except the gated density force uses RA (not R1) while the
                # Hubble term on the anomalous velocity's density part (-3 kappa yJ d) is kept
                ddc = (1 + kap*K['B'])*th + 3*kap*K['yJ']*dc
                dth = fr*th + grav + 3*kap*K['RA']*dc - 3*kap*K['yJ']*dc - 3*kap*K['yJ']*th
            elif reading == 'ungated':     # W = 1 (peculiar-gate limit in the force-law reading)
                ddc = th; dth = fr*th + grav + 3*kap*dc
            else:
                raise ValueError(reading)
        if baryons_on:
            ddb = tb; dtb = fr*tb + grav
        else:
            ddb = np.zeros(shape); dtb = np.zeros(shape)
        return ddc, dth, ddb, dtb

    N = N0
    for i in range(nstep):
        bon = N >= Ndrag
        y0 = (dc, th, db, tb)
        k1 = rhs(N, *y0, bon)
        y1 = [v + 0.5*dN*kk for v, kk in zip(y0, k1)]
        k2 = rhs(N+0.5*dN, *y1, bon)
        y2 = [v + 0.5*dN*kk for v, kk in zip(y0, k2)]
        k3 = rhs(N+0.5*dN, *y2, bon)
        y3 = [v + dN*kk for v, kk in zip(y0, k3)]
        k4 = rhs(N+dN, *y3, bon)
        dc, th, db, tb = [v + dN/6*(q1 + 2*q2 + 2*q3 + q4) for v, q1, q2, q3, q4 in zip(y0, k1, k2, k3, k4)]
        N += dN
    a = np.exp(N)
    dm = (Om_a(a,'c')*dc + Om_a(a,'b')*db)/(Om_a(a,'c') + Om_a(a,'b'))
    return dc, db, dm

def kpivot(kv=0.009, z=3.0):
    a = 1/(1+z)
    return kv*Hof(a)*a        # comoving 1/Mpc

if __name__ == '__main__':
    # background anchors (independent published values)
    aa = np.logspace(-9, 0, 200001)
    integrand = 1/(aa*Hof(aa))
    t0 = np.trapezoid(integrand, aa)*(3.0857e19/3.15576e16)   # Mpc/(km/s) -> Gyr
    print(f"Omega_m = {Om:.4f}, Omega_r h^2 = {ORH2:.4e}, Omega_L = {OL:.4f}")
    print(f"Age = {t0:.3f} Gyr   [Planck 2018 Table 2: 13.797 +- 0.023]")
    print(f"z_eq (rho_m = rho_r) = {Om/Or - 1:.1f}   [Planck 2018 Table 2: 3402 +- 26]")
    print(f"k_p(z=3) = {kpivot():.4f} /Mpc = {kpivot()/h:.4f} h/Mpc")
    # EdS-like analytic anchors: growth exponents in a matter-only, local-limit model
    # are tested in v3_eds_check.py
    # LCDM growth anchor: D(z=0)/a vs Carroll-Press-Turner fit (dagger)
    dc, db, dm = grow(np.array([1.0]), 0.0, 120, 'lcdm', a_end=1.0)
    dc3, db3, dm3 = grow(np.array([1.0]), 0.0, 120, 'lcdm', a_end=0.25)
    print(f"LCDM growth D(z=0)/D(z=3) = {dm[0]/dm3[0]:.4f}")
    Omz = lambda z: Om*(1+z)**3/(Om*(1+z)**3 + OL)
    gCPT = lambda z: 2.5*Omz(z)/(Omz(z)**(4/7) - (1-Omz(z)) + (1+Omz(z)/2)*(1+(1-Omz(z))/70))
    print(f"CPT fit (dagger) D(0)/D(3) = {gCPT(0)/(gCPT(3)/4):.4f}")
