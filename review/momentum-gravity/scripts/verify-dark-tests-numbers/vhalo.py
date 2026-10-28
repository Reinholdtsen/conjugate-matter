"""Small-halo collapse proxy (K11): sigma(M, z) with the gated transfer evaluated AT each redshift
(the enhancement grows with time), top-hat filter, EH98 no-wiggle P_lin (dagger), sigma8 = 0.8111.
Collapse redshift z_c: sigma(M, z_c) = 1.686 (1-sigma peak), density proxy (1+z_c)^3 (heuristic [T]).
Kernel options as in vgrowth.py ('B' = agent's, 'A' = reading-A consistent).
"""
import sys
import numpy as np
import vgrowth as G
import vpk as P
import vcosmo as C

h = C.h
rho_m = C.Om*2.775e11*h*h          # Msun/Mpc^3 (2.775e11 h^2 Msun/Mpc^3, dagger)

def evolve_snap(kMpc, eps, vstar, zouts, gate="gauss", dens="B", antidrag=True, N=8000, a_i=1e-5):
    k = np.asarray(kMpc, float)[None, :]
    e = np.asarray(eps, float)[:, None]
    RB, RA, RV = G.kernels(gate)
    Rd_tab = RB if dens == "B" else RA
    x0, x1 = np.log(a_i), 0.0
    xs = np.linspace(x0, x1, N+1); dx = xs[1]-xs[0]
    xdrag = np.log(1/(1+G.zdrag))
    shape = np.broadcast(k, e).shape
    dc = np.ones(shape); dcp = 0.5*np.ones(shape); db = np.zeros(shape); dbp = np.zeros(shape)
    xo = np.log(1/(1+np.asarray(zouts)))
    snaps = {}
    def rhs(x, dc, dcp, db, dbp, bon):
        a = np.exp(x); e2 = G.E2(a)
        Omc = G.Oc/a**3/e2; Omb = G.Ob/a**3/e2
        sc = vstar/(a*G.H0*np.sqrt(e2)); y = k*sc
        Rd = G.interp_k(Rd_tab, y); Rv = G.interp_k(RV, y) if antidrag else 0*y
        fric = 2+G.dlnH(a); src = 1.5*(Omc*dc+Omb*db)
        return dcp, -(fric-0.5*e*Omc*Rv)*dcp+src+1.5*e*Omc*Rd*dc, dbp, (-fric*dbp+src)*bon
    j = 0
    order = np.argsort(xo)
    for i in range(N):
        x = xs[i]
        bon = 1.0 if x+dx/2 >= xdrag else 0.0
        if bon == 0.0:
            db[:] = 0; dbp[:] = 0
        s1 = rhs(x, dc, dcp, db, dbp, bon)
        s2 = rhs(x+dx/2, dc+dx/2*s1[0], dcp+dx/2*s1[1], db+dx/2*s1[2], dbp+dx/2*s1[3], bon)
        s3 = rhs(x+dx/2, dc+dx/2*s2[0], dcp+dx/2*s2[1], db+dx/2*s2[2], dbp+dx/2*s2[3], bon)
        s4 = rhs(x+dx, dc+dx*s3[0], dcp+dx*s3[1], db+dx*s3[2], dbp+dx*s3[3], bon)
        dcn = dc+dx/6*(s1[0]+2*s2[0]+2*s3[0]+s4[0]); dcpn = dcp+dx/6*(s1[1]+2*s2[1]+2*s3[1]+s4[1])
        dbn = db+dx/6*(s1[2]+2*s2[2]+2*s3[2]+s4[2]); dbpn = dbp+dx/6*(s1[3]+2*s2[3]+2*s3[3]+s4[3])
        while j < len(order) and xs[i] <= xo[order[j]] <= xs[i+1]:
            t = (xo[order[j]]-xs[i])/dx
            snaps[order[j]] = ((1-t)*dc+t*dcn, (1-t)*db+t*dbn)
            j += 1
        dc, dcp, db, dbp = dcn, dcpn, dbn, dbpn
    return snaps

kk = np.logspace(-2, 2.5, 320)     # 1/Mpc for the sigma integral (top-hat cuts off high k)

def sigma_M(M, Pk):
    R = (3*M/(4*np.pi*rho_m))**(1/3)
    integrand = kk**3*Pk*P.tophat(kk*R)**2/(2*np.pi**2)
    return np.sqrt(np.trapezoid(integrand, np.log(kk)))

if __name__ == "__main__":
    cases = [(0.0285, 120), (0.081, 120), (0.348, 30), (1.14, 30), (0.775, 20), (3.08, 10)]
    if len(sys.argv) > 1 and sys.argv[1] == "A":
        dens = "A"
    else:
        dens = "B"
    zouts = np.concatenate([np.linspace(0, 10, 101), np.linspace(10.25, 60, 200)])
    PEH0 = np.interp(np.log(kk), np.log(P.kgrid), P.P_EH)
    print("kernel", dens)
    for (eps, vs) in cases:
        snaps = evolve_snap(kk, [0.0, eps], vs, zouts, dens=dens)
        for M in [1e8, 1e9]:
            sL = []; sG = []
            for iz, zz in enumerate(zouts):
                dc, db = snaps[iz]
                dm = (G.Oc*dc+G.Ob*db)/(G.Oc+G.Ob)
                T2 = (dm[1]/dm[0])**2
                Pz = PEH0*P.Dz(zz)**2
                sL.append(sigma_M(M, Pz)); sG.append(sigma_M(M, Pz*T2))
            sL = np.array(sL); sG = np.array(sG)
            def zc(s):
                # sigma decreasing with z; find where = 1.686
                idx = np.where(s < 1.686)[0]
                if len(idx) == 0: return np.nan
                i = idx[0]
                if i == 0: return 0.0
                return np.interp(1.686, [s[i], s[i-1]], [zouts[i], zouts[i-1]])
            zl, zg = zc(sL), zc(sG)
            print("eps=%.4f v*=%4d M=%.0e: sigma(z=0) LCDM %.3f gated %.3f | z_c LCDM %.2f gated %.2f | (1+z_c)^3 ratio %.3f"
                  % (eps, vs, M, sL[0], sG[0], zl, zg, ((1+zg)/(1+zl))**3))
