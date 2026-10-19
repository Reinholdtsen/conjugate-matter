"""Step 4 support calculations (own code). Constants as in step2a.py (PDG 2024 / Planck 2018)."""
import numpy as np
from math import pi, sqrt, log, log10
from scipy.integrate import quad, solve_ivp
from scipy.special import kn, zeta
from scipy.optimize import brentq

MPl = 1.220890e19; MPl_red = MPl/sqrt(8*pi); s0 = 2891.2; rhoc = 1.053672e-5; Oc = 0.120
rho_DM = Oc*rhoc
alpha = 1/137.035999; e_em = sqrt(4*pi*alpha)
gd = sqrt(16*pi*alpha); e_psi = gd/2; h_m = 4*pi/gd   # magnetic charge g_m = 2 pi/e_psi
GeV_s = 6.582119569e-25; hbarc = 1.973269804e-14; GeV2cm2 = 3.893794e-28; GeV_g = 1.78266192e-24
yr = 3.156e7
def hdr(t): print("\n" + "="*8 + " " + t + " " + "="*8)

# crude SM g*s(T) (same construction as step2c_psi.py, simplified with step thresholds for speed)
def gs_sm(T):
    g = 2 + 7/8*6
    for m, dof, f in [(0.000511,4,1),(0.10566,4,1),(1.777,4,1),(80.4,6,0),(91.19,3,0),(125.1,1,0),(172.7,12,1)]:
        if T > m/3: g += (7/8 if f else 1)*dof
    if T > 0.15:
        g += 16
        for m in [0.0022,0.0047,0.095,1.27,4.18]:
            if T > m/3: g += 7/8*12
    else:
        if T > 0.14/3: g += 3
    return g

# ------------------------------------------------------------------ 1. psi thermalisation with SM through eps
hdr("1. Freeze-in of psi from SM via its visible millicharge eps*e (s-channel f fbar -> gamma* -> psi psibar)")
# charged SM fermions: (mass, N_c Q^2)
fermions = [(0.000511,1),(0.10566,1),(1.777,1),(0.0022,4/3),(0.0047,1/3),(0.095,1/3),(1.27,4/3),(4.18,1/3),(172.7,4/3)]
def gamma_rate(T, m, eps):
    """reaction density [GeV^4] for all f fbar -> psi psibar, massless Boltzmann initial states (valid T >> m_f),
    gamma = g_f^2 T/(32 pi^4) * sum N_c Q^2 * int ds sigma(s) s^{3/2} K1(sqrt(s)/T), sigma color/spin averaged."""
    def sig(s):
        b = sqrt(max(0.0, 1-4*m*m/s)); return 4*pi*alpha**2*eps**2/(3*s)*b*(3-b*b)/2
    NQ = sum(nq for mf, nq in fermions if T > mf/3 and (T > 0.15 or nq == 1))  # quarks only above QCD transition
    smin = 4*m*m
    I = quad(lambda s: sig(s)*s**1.5*kn(1, sqrt(s)/T), smin*(1+1e-9), max(smin, T*T)*400, limit=200)[0]
    return 4*T/(32*pi**4)*NQ*I
def Hub(T): return 1.66*sqrt(gs_sm(T))*T**2/MPl
def s_ent(T): return 2*pi**2/45*gs_sm(T)*T**3
for eps in [1e-8, 1e-7, 1e-6]:
    row = []
    for m in [0.003, 0.03, 0.3, 3.0, 30.0]:
        # yield of psi (particles) produced: dY/dlnT = -gamma/(s H)
        lT = np.linspace(np.log(100*m), np.log(m/30), 300)
        Ys = [gamma_rate(np.exp(t), m, eps)/(s_ent(np.exp(t))*Hub(np.exp(t))) for t in lT]
        Y_FI = np.trapezoid(Ys, -lT)
        Yeq = 2*3*zeta(3)/(4*pi**2)/(2*pi**2/45*gs_sm(m))   # relativistic equilibrium yield, one Dirac particle (g=2)
        row.append(f"m={m:g}GeV: Y_FI/Y_eq={Y_FI/Yeq:.2e}")
    print(f"eps={eps:.0e}: " + "; ".join(row))
# rate ratio at T = m
for eps in [1e-7, 1e-6]:
    print(f"eps={eps:.0e}: Gamma/H at T=m (Gamma=gamma/n_eq,psi): " + "; ".join(
        f"m={m:g}: {gamma_rate(m, m, eps)/(2*3*zeta(3)/(4*pi**2)*m**3)/Hub(m):.2e}" for m in [0.003, 0.03, 0.3, 3.0, 30.0]))

hdr("2. Delta N_eff if the hidden sector re-thermalises with the SM and gamma' decouples at T_d (Adshead et al. eq. 2.17)")
def dN(Td, g_hs=2.0):
    return 8/7*(11/4)**(4/3)*(3.91/gs_sm(Td))**(4/3)*g_hs/2
for Td in [0.0005, 0.005, 0.05, 0.1, 0.2, 0.3, 1.0, 3.0, 10.0, 30.0]:
    print(f"T_d={Td:g} GeV: g*s={gs_sm(Td):.2f}  DeltaN_eff(gamma' only)={dN(Td):.3f}  (if psi entropy also dumped into gamma' after decoupling: x(9/2)^(4/3) -> {dN(Td)*(9/2)**(4/3):.2f})")

# ------------------------------------------------------------------ 3. monopole abundance with Kibble-Zurek + annihilation (LMW 2607.20843 framework)
hdr("3. Monopole relic: KZ production + diffusive/radiative capture (LMW 2607.20843 eqs. 13,16,18,28-30) with manuscript parameters")
z3 = zeta(3)
b_psi = 3/(4*pi**2)*z3*8*(h_m*e_psi/(4*pi))**2        # psi doublet: 2 Dirac x 4 spin states, |h q|/4pi = 1/2
b_W = 3/(4*pi**2)*z3*6*(h_m*gd/(4*pi))**2             # W'+-: 6 states, |h q|/4pi = 1
print(f"h = g_m = {h_m:.3f}, e_psi = {e_psi:.4f}, b_psi = {b_psi:.4f}, b_W' = {b_W:.4f}")
def monopole(M, v, xi, lam=0.1, init="KZ", gv=106.75):
    mW = gd*v
    Tc = v
    Tvis_i = Tc/xi
    H_i = 1.66*sqrt(gv)*Tvis_i**2/MPl
    s_i = 2*pi**2/45*gv*Tvis_i**3
    n_i = lam*H_i*Tc**2 if init == "KZ" else H_i**3
    Y0 = n_i/s_i
    def D(Th):
        Drad = (h_m**2/(4*pi))**2/M**2*(M/Th)**0.9
        b = b_psi + (b_W if Th > mW else 0.0)
        Tstop = M/b**2*(4*pi/h_m**2)**2
        Ddiff = h_m**2/(b*Th**2) if Th > Tstop else 0.0
        return Drad + Ddiff, Tstop
    def rhs(lx, y):
        x = np.exp(lx); T = M/x; Th = xi*T
        s = 2*pi**2/45*gv*T**3; H = 1.66*sqrt(gv)*T**2/MPl
        Y = np.exp(y[0])
        return [-D(Th)[0]*s/H*Y]       # d lnY/d lnx = -D s Y / H
    x0 = M/Tvis_i
    sol = solve_ivp(rhs, [np.log(x0), np.log(x0*1e8)], [np.log(Y0)], method="LSODA", rtol=1e-8, atol=1e-10, max_step=0.05)
    Yf = np.exp(sol.y[0, -1])
    return Y0, Yf, D(xi*Tvis_i)[1]
Y_DM = rho_DM/(3e13*s0)
print(f"Y needed for Omega_DM at M=3e13: {Y_DM:.3e}")
for v in [8.092e11, 1.446e12]:
    for xi in [0.76, 0.5]:
        for init, lam in [("Kibble(one per H^-3)", None), ("KZ", 0.1), ("KZ", 1.0)]:
            Y0, Yf, Tstop = monopole(3e13, v, xi, lam=lam if lam else 0.1, init="KZ" if init == "KZ" else "K")
            print(f"v={v:.2e} xi={xi} {init}{'' if lam is None else ' lambda='+str(lam)}: Y_init={Y0:.2e} Y_final={Yf:.2e} "
                  f"-> Omega/Omega_DM={Yf/Y_DM:.2e}  (diffusive capture stops at T_hid={Tstop:.2e}; T_c={v:.2e}, m_W'={gd*v:.2e})")
# LMW analytic eq. (25) evaluated at the manuscript's parameters (their e = smallest hidden charge, b with fermions)
for v in [8.092e11, 1.446e12]:
    for b in [b_psi, b_psi + b_W, 10.0]:
        B = 0.76**4
        Om = 0.382*(v/1e8)**2*(B/1e-3)**0.25*(b/10)**-1*(e_psi/0.2)**4*(106.75/200)**-0.25*(16/200)**-0.25
        print(f"LMW eq.(25) at v={v:.2e}, B=xi^4 (xi=0.76), b={b:.3f}, e={e_psi:.3f}: Omega_M = {Om:.2e}")
# first-order transition: bubbles per Hubble volume ~ (beta/H)^3 -> p ~ 104 (beta/H)^3
for bH in [1, 10, 100]:
    print(f"first-order with beta/H={bH}: p ~ {104.3*bH**3:.1e}")

# ------------------------------------------------------------------ 4. psi kinetic coupling to the gamma' bath (DAO)
hdr("4. psi - gamma' kinetic decoupling (dark Thomson scattering)")
Tg0 = 2.7255*8.617333e-14   # GeV
h = 0.674; H0 = 100*h*1e5/3.0857e24*GeV_s  # GeV
Om_m = 0.143/h**2; Om_r = 4.18e-5/h**2
def Hz(z): return H0*sqrt(Om_r*(1+z)**4 + Om_m*(1+z)**3)
for dNe in [0.286, 0.1, 0.05]:
    Th0 = (dNe*7/8)**0.25*(4/11)**(1/3)*Tg0
    for m in [0.03, 0.3, 3.0, 30.0]:
        sT = 8*pi/3*alpha**2/m**2
        def G(z): return 4/3*(pi**2/15*(Th0*(1+z))**4)*sT/m
        zdec = brentq(lambda lz: np.log(G(10**lz)/Hz(10**lz)), 0, 12)
        # gamma' opacity from psi (fraction f of DM)
        f = 0.1; npsi0 = f*rho_DM/m*hbarc**3  # GeV^3
        zfs = None
        try:
            zfs = 10**brentq(lambda lz: np.log(npsi0*(1+10**lz)**3*sT/Hz(10**lz)), 0, 14)
        except ValueError:
            zfs = float('nan')
        print(f"DeltaN={dNe} (T_h0/T_g0={Th0/Tg0:.3f}) m_psi={m:g} GeV: psi kinetically decouples from gamma' at z = {10**zdec:.2e}; "
              f"gamma' mean free path ~ Hubble (f=0.1) at z = {zfs:.2e}")

# ------------------------------------------------------------------ 5. magnetic-plasma frequency of the monopole DM
hdr("5. Monopole 'plasma' frequency (collective long-range effects, cf. Lasenby 2007.00667)")
for lab, rho in [("local 0.4 GeV/cm3", 0.4), ("cluster ~1e-2 GeV/cm3", 1e-2), ("cosmic mean", rho_DM)]:
    M = 3e13
    n = rho/M*hbarc**3  # GeV^3
    wp = sqrt(4*pi*34.259*n/M)  # GeV
    print(f"{lab}: omega_p = {wp/GeV_s:.2e} s^-1, 1/omega_p = {1/(wp/GeV_s)/yr:.2e} yr")

# ------------------------------------------------------------------ 6. Higgs portal lambda_p |H|^2 Tr Phi^2
hdr("6. Higgs portal (allowed by all stated symmetries)")
for v in [8.092e11, 1.446e12]:
    print(f"v={v:.2e}: lambda_p v^2 <= m_h^2 (125 GeV)^2 needs lambda_p <= {(125/v)**2:.1e}")
# thermalisation at T~v by 2->2 via portal: Gamma ~ n sigma, sigma ~ lambda^2/(16 pi s), <s>~18 T^2, n ~ 1.2 T^3/pi^2 x 4 (Higgs doublet)
for T in [1e12]:
    lam_eq = sqrt(1.66*sqrt(122.75)*T/MPl/(4*1.2/pi**2/(16*pi*18)))
    print(f"portal equilibrates sectors at T={T:.0e} if lambda_p >~ {lam_eq:.1e}")

# ------------------------------------------------------------------ 7. psi annihilation vs BBN for m_psi ~ MeV
hdr("7. psi annihilation epoch vs BBN (hidden x_f ~ 20-25, T_h/T from entropy, xi0=0.76)")
R = 16*0.76**3/106.75
for m in [0.001, 0.003, 0.01, 0.03]:
    # after psi annihilation hidden dof 2; before 9. T_h/T at T~m: (R*gs/9)^(1/3)
    Th_T = (R*gs_sm(m/20)/2)**(1/3)
    Tvis_f = m/20/Th_T
    print(f"m_psi={m*1e3:g} MeV: hidden freeze-out T_h ~ m/20 = {m/20*1e3:.3g} MeV at T_vis ~ {Tvis_f*1e3:.3g} MeV (BBN D-formation ~0.07 MeV; n/p freeze-out ~0.8 MeV)")
