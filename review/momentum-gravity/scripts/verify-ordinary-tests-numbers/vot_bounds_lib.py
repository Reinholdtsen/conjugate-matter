# Independent recomputation of the round-2 ordinary-tests bounds (claims O9-O16, O23) for
# V = -(G m1 m2/r)[1 + eps W(|v1-v2|/v*)], gate on centre-of-mass relative velocity.
# Written without reading the agent's bounds.py.  Inputs, all checked by live search this session:
#   GM_sun, GM_EM, GM_E(LLR), SLR GM_E (Ries 1992, Dunn 1999): DE430 lunar memo (Williams, Boggs, Folkner 2013)
#   planet a, e, P: NASA Planetary Fact Sheet (updated 18 Mar 2025) - rounded values as printed there
#   supplementary perihelion precessions: Pitjev & Pitjeva 2013 Astron. Lett. 39, 141, Table 5 (mas/yr; x100 -> mas/cy)
#   LLR anomalous perigee precession, 2 sigma upper limit 270 muas/yr: Adelberger, Heckel, Nelson 2003, sec. 4.5
#   double pulsar Pb, e, M, omega-dot, Pb-dot test 1.3e-4 (95%): Kramer et al. 2021 PRX 11, 041050
#   Cassini gamma - 1 = (2.1 +- 2.3)e-5: Bertotti et al. 2003 via Will 2014
#   Eros: flyby mass (7.2 +- 1.8)e15 kg at 965 m/s (Yeomans et al. 1999); orbital mass 6.687e15 kg
#   Talmadge et al. 1988 eta_p (one-sided 2 sigma) via Will 1998 Table 4
# Planet masses are neglected in the orbital speeds (largest effect: Jupiter, 0.05% in u).
import numpy as np

GMsun = 132712440041.94          # km^3/s^2
GMEM = 403503.2355
c = 299792.458                   # km/s
RAD2MAS = 180/np.pi*3600e3

planets = {  # a [1e6 km], e, P [days], supplementary precession [mas/cy], sigma [mas/cy]
    'Mercury': (57.9, 0.206, 88.0, -2.0, 3.0),
    'Venus': (108.2, 0.007, 224.7, 2.6, 1.6),
    'Earth': (149.6, 0.017, 365.2, 0.19, 0.19),
    'Mars': (228.0, 0.094, 687.0, -0.020, 0.037),
    'Jupiter': (778.5, 0.049, 4331., 58.7, 28.3),
    'Saturn': (1432.0, 0.052, 10747., -0.32, 0.47),
}
moon = dict(a=384400., e=0.0549)
vLAG = np.sqrt(398600.4356/12270.)   # LAGEOS a = 12270 km

def shapes(name):
    if name == 'gauss':
        W = lambda u: np.exp(-u**2)
        dW = lambda u: -2*u*np.exp(-u**2)
    else:
        W = lambda u: 1/(1 + u**2)
        dW = lambda u: -2*u/(1 + u**2)**2
    K = lambda u: W(u) - u*dW(u)
    return W, dW, K

NE = 4096
Egrid = np.arange(NE)*2*np.pi/NE
def adv_per_orbit(dW, uc, e):
    """first-order apsidal advance per orbit per unit eps: 2 pi sqrt(1-e^2)/e dPhi/de,
    Phi(e) = <W(uc s)>_E, s = sqrt((1+e cosE)/(1-e cosE)); dPhi/de by differentiating under the
    integral (ds/de = cosE/(s (1-e cosE)^2)); periodic trapezoid rule."""
    cE = np.cos(Egrid)
    s = np.sqrt((1 + e*cE)/(1 - e*cE))
    dsde = cE/(s*(1 - e*cE)**2)
    dPhi = np.mean(dW(uc*s)*uc*dsde)
    return 2*np.pi*np.sqrt(1 - e**2)/e*dPhi

def two_sided(x, sig):          # largest |value| inside the 2 sigma interval
    return max(abs(x - 2*sig), abs(x + 2*sig))

# double pulsar
Pb = 0.1022515592973*86400.     # s
e_dp = 0.087777023
GMdp = 2.587052*GMsun
a_dp = (GMdp*Pb**2/(4*np.pi**2))**(1/3)
v_dp = np.sqrt(GMdp/a_dp)
omdot = 16.899323               # deg/yr
dGR_per_orbit = np.radians(omdot)*Pb/(365.25*86400)
# mass-bias factor: masses from omega-dot and Shapiro s (Kramer et al. 2021 sec. VI.2.1)
mA, mB = 1.338185, 1.248868; M = mA + mB
dlnM = 1.5; dlnmB = 2/3*dlnM; dlnmA = (M*dlnM - mB*dlnmB)/mA
fac_s = dlnmA + dlnmB - dlnM/3
fac_R = 5/3*1.5
dp_limit = 1.3e-4/fac_s

def bounds(vstar, shape):
    W, dW, K = shapes(shape)
    out = {}
    for nm, (a6, e, P, x, sg) in planets.items():
        uc = np.sqrt(GMsun/(a6*1e6))/vstar
        sig = adv_per_orbit(dW, uc, e)*36525/P*RAD2MAS      # mas/cy per unit eps
        out['prec ' + nm] = two_sided(x, sg)/abs(sig) if sig != 0 else np.inf
    # LLR perigee
    vM = np.sqrt(GMEM/moon['a'])
    PM = 2*np.pi*np.sqrt(moon['a']**3/GMEM)/86400
    sigM = adv_per_orbit(dW, vM/vstar, moon['e'])*365.25/PM*RAD2MAS*1e3   # muas/yr per eps
    out['LLR perigee'] = 270./abs(sigM)
    # GM_E LLR vs SLR
    dK = K(vM/vstar) - K(vLAG/vstar)
    for lab, gslr, sslr in [('Ries', 398600.4356, 0.0004), ('Dunn', 398600.4360, 0.0002)]:
        x = (398600.4354 - gslr)/gslr
        sg = np.hypot(0.0005, sslr)/gslr
        out['GM_E LLR-SLR ' + lab] = two_sided(x, sg)/abs(dK) if dK != 0 else np.inf
    # double pulsar
    sdp = adv_per_orbit(dW, v_dp/vstar, e_dp)/dGR_per_orbit
    out['double pulsar'] = dp_limit/abs(sdp)
    # Cassini: gamma_fit - 1 = -2 eps K(u_E); eps K in [-(2.1+4.6)/2, (4.6-2.1)/2] e-5
    uE = np.sqrt(GMsun/149.6e6)/vstar
    out['Cassini'] = (2.1 + 4.6)/2*1e-5/K(uE)
    # Eros: M_fly/M_orb - 1 = eps (W(u_fly) - K(u_orb))
    vorb = np.sqrt(6.674e-20*6.687e15/35.)    # km/s, G in km^3 kg^-1 s^-2 (CODATA, dagger)
    xE = 7.2/6.687 - 1; sE = 1.8/6.687
    dE = W(0.965/vstar) - K(vorb/vstar)
    out['Eros'] = two_sided(xE, sE)/abs(dE)
    # Talmadge: eta_p = (1/3) eps (K(u_p) - K(u_E)); bounds used as symmetric magnitudes
    for nm, b in [('Mercury', 1.4e-8), ('Venus', 1.5e-9), ('Mars', 6.5e-10), ('Jupiter', 6e-8)]:
        up = np.sqrt(GMsun/(planets[nm][0]*1e6))/vstar
        d = (K(up) - K(uE))/3
        out['Kepler ' + nm + '/Earth'] = b/abs(d) if d != 0 else np.inf
    return out

